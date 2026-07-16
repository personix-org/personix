#!/usr/bin/env python3
"""Generátor titulkového překryvu pro pamfletové infografiky.

Vstup:  imgboxes/{img}.json  — ruční rámečky (bbox+angle, nebo path+thickness)
        trans/{lang}.json    — překlady {originální text: přeložený text}
Výstup: out/{lang}/{img}.webp — obrázek s přeloženými titulky

Zakryje originál tmavým titulkovým boxem/pásem a vysadí překlad:
 · obdélník: box (respektuje natočení), text vycentrovaný, auto-zalomený a auto-zmenšený
 · cesta:    tmavý pás podél křivky, písmena vysazená po křivce (natočená dle tečny)
"""
import sys, os, json, math, glob
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont, TTCollection

BK = os.path.dirname(os.path.abspath(__file__))
GFX = "/Users/pavelkudrna/RiderProjects/new-world-order/Prezentace/Info Graphics/v5"
BOXES, TRANS, OUT = f"{BK}/imgboxes", f"{BK}/trans", f"{BK}/out"

DARK = (26, 20, 15, 255)      # titulkový podklad (plná krytí — originál musí zmizet)
LIGHT = (250, 245, 235, 255)  # barva písma
PAD = 8                       # rezerva boxu kolem textu

# ADAPTIVNÍ PODKLAD: místo tmavého boxu vezmi barvu podkladu, ať titulek splyne s grafikou.
#
# Vzorkuje se VNITŘEK boxu. Originální text tam sice je, ale zabírá menšinu plochy —
# a dominantní barva je přesně ta statistika, kterou menšina nepřeváží. Vnitřek navíc
# vrací barvu přímo pod titulkem. (Dřív se bral prstenec kolem boxu, aby se text
# „obešel" — jenže prstenec zavadí o obrys bubliny nebo kresbu a barvu to zkreslí víc
# než text uvnitř. Změřeno na 1618 boxech: vnitřek trefí 89 %, prstenec 79 %.)
#
# Dominanta, ne medián: pár procent cizích pixelů medián s rozptylovým prahem přehodilo
# na tmavý box, i když pod ním byla čistá bílá. Gate = jaký podíl plochy dominanta
# pokrývá; na kresbě žádná barva nepřeváží → přiznaný tmavý box.
ADAPTIVE = os.environ.get("ADAPTIVE", "1") != "0"
RING = 10          # šířka prstence vně boxu (záloha, když vnitřek nevyjde)
TOL = 28           # tolerance kolem barvy podkladu (co ještě počítat jako „stejná barva")
# Práh posazený do MEZERY v rozdělení (pět nejhorších boxů má 0,14–0,18, pak skok na 0,23;
# medián je 0,70). Kdyby seděl uprostřed masy, o barvě rozhoduje šum a dvě stejné cedule
# vedle sebe vyjdou každá jinak. Takhle propadne jen skutečná kresba — 5 boxů z 1618.
COVER_MIN = 0.20   # pod touhle jednolitostí je podklad členitý → tmavý box
LUMA_MID = 140     # jas, pod kterým sázíme světlé písmo (a nad ním tmavé)

def _inside_px(base, x0, y0, x1, y1, ang=0):
    """Pixely vnitřku boxu (originální text je menšina, podklad neovlivní).

    U natočeného rámečku se musí vzorkovat natočený obdélník, ne jeho vodorovný
    obal — do toho spadne kus okolní kresby (u svislé cedule na koši třeba celá
    drátěná mřížka) a podklad by z toho vyšel úplně mimo.
    """
    W, H = base.size
    if ang:
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        w, h = x1 - x0, y1 - y0
        d = int(math.hypot(w, h)) + 4
        sq = base.crop((int(cx - d/2), int(cy - d/2), int(cx + d/2), int(cy + d/2)))
        sq = sq.rotate(ang, resample=Image.BICUBIC)   # srovnej rámeček do vodorovna
        m = sq.width / 2
        box = (int(m - w/2), int(m - h/2), int(m + w/2), int(m + h/2))
        if box[2] - box[0] < 3 or box[3] - box[1] < 3: return []
        return list(sq.crop(box).convert("RGB").getdata())
    a, b = max(0, int(x0)), max(0, int(y0))
    c, d = min(W, int(x1)), min(H, int(y1))
    if c - a < 3 or d - b < 3: return []
    return list(base.crop((a, b, c, d)).convert("RGB").getdata())

def _ring_px(base, x0, y0, x1, y1):
    """Pixely prstence kolem boxu — záloha, když vnitřek nepřeváží (těsný box)."""
    W, H = base.size
    ox0, oy0 = max(0, int(x0) - RING), max(0, int(y0) - RING)
    ox1, oy1 = min(W, int(x1) + RING), min(H, int(y1) + RING)
    if ox1 - ox0 < 3 or oy1 - oy0 < 3: return []
    outer = base.crop((ox0, oy0, ox1, oy1)).convert("RGB")
    px = list(outer.getdata())
    iw, ih = outer.size
    ix0, iy0 = int(x0) - ox0, int(y0) - oy0
    ix1, iy1 = int(x1) - ox0, int(y1) - oy0
    return [px[y*iw + x] for y in range(ih) for x in range(iw)
            if not (ix0 <= x < ix1 and iy0 <= y < iy1)]

def _dominant(px):
    """(barva podkladu, jak je jednolitý 0–1) — text z výřezu odfiltruje prahem.

    Hledat jeden nejčastější odstín nestačí: podklad bývá stínovaný (sloup, pás),
    takže se v histogramu roztříští na desítky odstínů a žádný nepřeváží. Text je
    ale vůči podkladu vždycky vysoce kontrastní, takže stačí rozdělit pixely jasem
    na dvě třídy (Otsu) a vzít tu početnější — ta je podklad i s texturou.
    Jednolitost = jak málo ta třída sama kolísá; kresba kolísá hodně → tmavý box.
    """
    if len(px) < 12: return None, 0.0
    lum = [c[0]*0.299 + c[1]*0.587 + c[2]*0.114 for c in px]
    hist = [0]*256
    for l in lum: hist[int(l)] += 1
    tot = len(lum); sm = sum(i*hist[i] for i in range(256))
    best, thr, wB, sB = -1.0, 128, 0, 0.0
    for t in range(256):
        wB += hist[t]
        if wB == 0: continue
        wF = tot - wB
        if wF == 0: break
        sB += t * hist[t]
        mB, mF = sB/wB, (sm - sB)/wF
        var = wB * wF * (mB - mF) ** 2      # mezitřídní rozptyl
        if var > best: best, thr = var, t
    bg = [c for c, l in zip(px, lum) if l > thr]
    if len(bg) < len(px) / 2:               # početnější třída je podklad
        bg = [c for c, l in zip(px, lum) if l <= thr]
    if len(bg) < 8: return None, 0.0
    # Barvu ber z MEDIÁNU té třídy a započítej jen pixely kolem něj: samotná třída
    # do sebe nabere i obrys cedule a stín, a průměr přes ně by barvu stáhl jinam.
    med = tuple(sorted(c[i] for c in bg)[len(bg)//2] for i in range(3))
    near = [c for c in px if all(abs(c[i] - med[i]) <= TOL for i in range(3))]
    if len(near) < 8: return None, 0.0
    col = tuple(int(sum(c[i] for c in near) / len(near)) for i in range(3))
    return col, len(near) / len(px)         # jednolitost = podíl plochy držící podklad

def _ink(col):
    """Barva písma podle jasu podkladu."""
    lum = col[0]*0.299 + col[1]*0.587 + col[2]*0.114
    return (20, 16, 12, 255) if lum >= LUMA_MID else LIGHT

# Ruční barvy pro hrstku boxů, kde automat nedosáhne (viz komentář v plate_overrides.json).
try:
    OVERRIDES = json.load(open(f"{BK}/plate_overrides.json"))
except Exception:
    OVERRIDES = {}

def plate(base, x0, y0, x1, y1, ang=0, img=None, text=None):
    """Vrať (barva podkladu, barva písma) pro titulek na této pozici."""
    if not ADAPTIVE: return DARK, LIGHT
    ov = OVERRIDES.get(img, {}).get(text) if img else None
    if ov:
        col = tuple(ov)
        return col + (255,), _ink(col)
    col, cover = _dominant(_inside_px(base, x0, y0, x1, y1, ang))
    if col is None or cover < COVER_MIN:   # box natěsno kolem textu → zkus okolí
        col, cover = _dominant(_ring_px(base, x0, y0, x1, y1))
    if col is None or cover < COVER_MIN:
        return DARK, LIGHT                 # členitý podklad → přiznaný tmavý titulek
    return (col[0], col[1], col[2], 255), _ink(col)

SYS = "/System/Library/Fonts"
FONTS = {
    "ja": f"{SYS}/ヒラギノ角ゴシック W6.ttc",
    "ko": f"{SYS}/AppleSDGothicNeo.ttc",
    "zh-cn": f"{SYS}/Hiragino Sans GB.ttc", "zh-tw": f"{SYS}/Hiragino Sans GB.ttc",
    "zh-hk": f"{SYS}/Hiragino Sans GB.ttc",
    "hi": f"{SYS}/Supplemental/Devanagari Sangam MN.ttc",
    "th": f"{SYS}/Supplemental/Thonburi.ttc",
    "ar": f"{SYS}/Supplemental/Arial Unicode.ttf",
    "he": f"{SYS}/Supplemental/Arial Unicode.ttf",
    "hy": f"{SYS}/Supplemental/Arial Unicode.ttf",
}
DEFAULT_FONT = f"{SYS}/Supplemental/Arial Bold.ttf"
RTL = {"ar", "he"}

_fc = {}
def font(lang, size):
    key = (lang, size)
    if key not in _fc:
        path = FONTS.get(lang, DEFAULT_FONT)
        try: _fc[key] = ImageFont.truetype(path, size)
        except Exception: _fc[key] = ImageFont.truetype(DEFAULT_FONT, size)
    return _fc[key]

FALLBACK_FONT = f"{SYS}/Supplemental/Arial Unicode.ttf"  # doplní symboly, co hlavní font nemá (✓ ∝ ₁ ₂)
_fbc = {}
def fbfont(size):
    if size not in _fbc:
        _fbc[size] = ImageFont.truetype(FALLBACK_FONT, size)
    return _fbc[size]

_cmc = {}
def main_cmap(lang):
    """Množina znaků, které HLAVNÍ font jazyka umí (rozhoduje o fallbacku)."""
    path = FONTS.get(lang, DEFAULT_FONT)
    if path in _cmc: return _cmc[path]
    chars = set()
    try:
        chars |= set(TTFont(path, fontNumber=0).getBestCmap().keys())
    except Exception:
        try:
            for f in TTCollection(path).fonts:
                try: chars |= set(f.getBestCmap().keys())
                except Exception: pass
        except Exception: pass
    _cmc[path] = chars
    return chars

def _fb(ch, f, lang):
    """Vyber font pro jeden znak: hlavní, nebo fallback když ho hlavní nemá."""
    o = ord(ch)
    if o < 0x20 or o in main_cmap(lang): return f
    return fbfont(f.size)

def _native(s, lang):
    cm = main_cmap(lang)
    return all(ord(c) < 0x20 or ord(c) in cm for c in s)

def _runs(s, f, lang):
    """Rozděl řádek na SOUVISLÉ úseky se stejným fontem.

    Sázet znak po znaku by rozbilo skládání písma (dévanágarí/thajština/arabština
    kreslí matry a ligatury až v kontextu — izolovaný znak vyjde jako prázdný
    kroužek). Uvnitř úseku proto text zůstává vcelku a fallback dostane jen
    ty znaky, které hlavní font opravdu nemá.
    """
    cm = main_cmap(lang)
    runs, cur, cur_fb = [], "", None
    for ch in s:
        fb = not (ord(ch) < 0x20 or ord(ch) in cm)
        if cur and fb != cur_fb:
            runs.append((cur, cur_fb)); cur = ""
        cur += ch; cur_fb = fb
    if cur: runs.append((cur, cur_fb))
    return [(t, fbfont(f.size) if fb else f) for t, fb in runs]

def measure(d, s, f, lang):
    """Šířka textu s respektem k fallback fontu (jinak by se špatně centroval)."""
    if _native(s, lang):
        return d.textlength(s, font=f)
    return sum(d.textlength(t, font=ff) for t, ff in _runs(s, f, lang))

def draw_line(d, xy, s, f, lang, fill):
    """Vysaď řádek; úseky mimo hlavní font jdou z fallbacku."""
    if _native(s, lang):
        d.text(xy, s, font=f, fill=fill); return
    x, y = xy
    for t, ff in _runs(s, f, lang):
        d.text((x, y), t, font=ff, fill=fill)
        x += d.textlength(t, font=ff)

def shape(text, lang):
    """RTL: přeskládat písmena (arabština potřebuje i tvarování)."""
    if lang not in RTL: return text
    try:
        from bidi.algorithm import get_display
        if lang == "ar":
            import arabic_reshaper
            text = arabic_reshaper.reshape(text)
        return get_display(text)
    except Exception:
        return text

def wrap(d, text, f, maxw, lang):
    """Zalom text na řádky, aby se vešel do šířky."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if measure(d, t, f, lang) <= maxw or not cur: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

MIN_SZ = 6    # dolní mez čitelnosti; delší jazyky se vejdou zmenšením písma, box se NEMĚNÍ

def ink_extent(d, lines, f, lh):
    """Svislé hranice SKUTEČNÉHO tisku bloku řádků (ne nominální obálky písma).

    Nominální výška řádku je u některých písem hodně vedle skutečných glyfů —
    arabština a hebrejština sedí v řádku níž a přetečou dolů, i když podle
    čísel se vejdou. Proto se měří i sází podle inkoustu, ne podle obálky.
    """
    tops, bots = [], []
    for i, ln in enumerate(lines):
        bb = d.textbbox((0, i*lh), ln, font=f)
        tops.append(bb[1]); bots.append(bb[3])
    if not tops: return 0, 0
    return min(tops), max(bots)

def fit_box(d, text, lang, bw, bh):
    """Najdi největší písmo, aby se (zalomený) text vešel do rámečku.
    Rámeček je daný ručně a NEMĚNÍ se — přizpůsobuje se písmo (nutný kompromis
    u delších jazyků). Zkouší i těsnější řádkování, než sáhne po menším písmu."""
    bw, bh = max(bw - 2*PAD, 8), max(bh - 2*PAD, 8)
    for sz in range(int(bh), MIN_SZ - 1, -1):
        f = font(lang, sz)
        lines = wrap(d, text, f, bw, lang)
        if any(measure(d, l, f, lang) > bw for l in lines): continue
        for lead in (1.18, 1.08, 1.0):     # postupně stahuj řádkování, ať smíš zůstat větší
            lh = max(1, int(sz * lead))
            if lh * len(lines) > bh: continue
            top, bot = ink_extent(d, lines, f, lh)
            if bot - top <= bh:            # musí se vejít i SKUTEČNÝ tisk, nejen obálka
                return f, lines, lh, lh*len(lines)
    f = font(lang, MIN_SZ)
    lines = wrap(d, text, f, bw, lang)
    lh = max(1, int(MIN_SZ * 1.0))
    return f, lines, lh, lh*len(lines)

def draw_rect(base, b, txt, lang, phase, colors=(DARK, LIGHT)):
    """Obdélníkový titulek. phase='bg' = jen podklad, phase='tx' = jen text.
    Dvě fáze, aby box souseda nepřekryl už vysazený text (boxy se často dotýkají)."""
    PLATE, INK = colors
    x0, y0, x1, y1 = b["bbox"]
    x0, y0, x1, y1 = min(x0,x1), min(y0,y1), max(x0,x1), max(y0,y1)
    W, H = base.size
    ang = b.get("angle", 0) or 0
    # Rámeček kreslený přes okraj: POSUŇ ho dovnitř (zachová velikost i geometrii).
    # NIKDY neořezávej bbox — u natočených by se posunul střed a box by minul text.
    if not ang:
        if x0 < 0: x1 -= x0; x0 = 0
        if y0 < 0: y1 -= y0; y0 = 0
        if x1 > W: x0 -= (x1-W); x1 = W
        if y1 > H: y0 -= (y1-H); y1 = H
        x0, y0 = max(0, x0), max(0, y0)
    w, h = int(x1-x0), int(y1-y0)
    if w < 4 or h < 4: return
    m = PAD  # rezerva, aby originál jistě zmizel
    TW, TH = w + 2*m, h + 2*m   # rámeček se NIKDY nemění — přizpůsobí se písmo
    probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    f, lines, lh, _ = fit_box(probe, shape(txt, lang), lang, TW, TH)
    tile = Image.new("RGBA", (TW, TH), (0,0,0,0))
    td = ImageDraw.Draw(tile)
    if phase == "bg":
        td.rounded_rectangle([0, 0, TW-1, TH-1], radius=min(12, TH//2), fill=PLATE)
    else:
        # Centruj podle SKUTEČNÉHO tisku, ne podle nominální obálky písma: u arabštiny
        # a hebrejštiny sedí glyfy v řádku níž, takže centrování podle obálky vysadí
        # ink pod spodní hranu rámečku (a u boxů dole i mimo obrázek).
        top, bot = ink_extent(td, lines, f, lh)
        ty = (TH - (bot - top)) / 2 - top
        for i, ln in enumerate(lines):
            tw = measure(td, ln, f, lang)
            draw_line(td, ((TW - tw)/2, ty + i*lh), ln, f, lang, INK)
    if ang:
        tile = tile.rotate(-ang, expand=True, resample=Image.BICUBIC)
    cx, cy = (x0+x1)/2, (y0+y1)/2
    px, py = int(cx - tile.width/2), int(cy - tile.height/2)
    # paste zvládne i zápornou pozici (přesah se ořízne) — na rozdíl od alpha_composite
    layer = Image.new("RGBA", base.size, (0,0,0,0))
    layer.paste(tile, (px, py), tile)
    base.alpha_composite(layer)

def polyline_len(pts):
    segs, tot = [], 0.0
    for i in range(len(pts)-1):
        d = math.dist(pts[i], pts[i+1])
        segs.append(d); tot += d
    return segs, tot

def point_at(pts, segs, s):
    """Bod a úhel tečny ve vzdálenosti s podél lomené čáry."""
    acc = 0.0
    for i, sl in enumerate(segs):
        if sl <= 0: continue
        if acc + sl >= s or i == len(segs)-1:
            t = max(0.0, min(1.0, (s - acc) / sl))
            (ax, ay), (bx, by) = pts[i], pts[i+1]
            x, y = ax + (bx-ax)*t, ay + (by-ay)*t
            ang = math.degrees(math.atan2(by-ay, bx-ax))
            return x, y, ang
        acc += sl
    return pts[-1][0], pts[-1][1], 0.0

def draw_path(base, b, txt, lang, phase, colors=(DARK, LIGHT)):
    """Ohýbaný titulek — pás podél cesty + písmena po křivce (dle tečny)."""
    PLATE, INK = colors
    pts = [tuple(p) for p in b["path"]]
    # zahoď duplicitní body
    pts = [p for i, p in enumerate(pts) if i == 0 or math.dist(p, pts[i-1]) > 1]
    if len(pts) < 2: return
    th = int(b.get("thickness", 60))
    segs, total = polyline_len(pts)
    if total < 4: return

    # 1) zakrytí originálu pásem podél cesty
    if phase == "bg":
        layer = Image.new("RGBA", base.size, (0,0,0,0))
        ld = ImageDraw.Draw(layer)
        ld.line(pts, fill=PLATE, width=th, joint="curve")
        for p in (pts[0], pts[-1]):  # kulaté konce
            ld.ellipse([p[0]-th//2, p[1]-th//2, p[0]+th//2, p[1]+th//2], fill=PLATE)
        base.alpha_composite(layer)
        return

    # 2) text po křivce — velikost tak, aby délkou sedl na cestu a výškou do pásu
    d0 = ImageDraw.Draw(base)
    s = shape(txt, lang)
    if lang in RTL: s = s[::-1]  # po křivce sázíme zleva doprava
    size = max(8, int(th * 0.72))
    for _ in range(40):
        f = font(lang, size)
        if measure(d0, s, f, lang) <= total * 0.97 or size <= 8: break
        size -= 1
    f = font(lang, size)
    tw = measure(d0, s, f, lang)
    cur = max(0.0, (total - tw) / 2)  # vycentruj text na cestě

    for ch in s:
        gf = _fb(ch, f, lang)
        cw = d0.textlength(ch, font=gf)
        x, y, ang = point_at(pts, segs, cur + cw/2)
        gl = Image.new("RGBA", (int(cw)+size, int(size*1.8)+size), (0,0,0,0))
        gd = ImageDraw.Draw(gl)
        gd.text((size/2, size/2), ch, font=gf, fill=INK)
        gl = gl.rotate(-ang, expand=True, resample=Image.BICUBIC)
        base.alpha_composite(gl, (int(x - gl.width/2), int(y - gl.height/2)))
        cur += cw

def render(img_name, lang, trans):
    src = f"{GFX}/{img_name}.webp"
    boxes = json.load(open(f"{BOXES}/{img_name}.json"))
    base = Image.open(src).convert("RGBA")
    # Barvu podkladu změř z NEDOTČENÉHO originálu — jakmile se začne kreslit,
    # prstenec kolem boxu už vidí sousední titulky, ne grafiku.
    colors = []
    for b in boxes:
        if b.get("path"):
            xs = [p[0] for p in b["path"]]; ys = [p[1] for p in b["path"]]
            th = int(b.get("thickness", 60))
            colors.append(plate(base, min(xs)-th/2, min(ys)-th/2, max(xs)+th/2, max(ys)+th/2,
                                0, img_name, b["text"]))
        else:
            x0, y0, x1, y1 = b["bbox"]
            colors.append(plate(base, min(x0,x1), min(y0,y1), max(x0,x1), max(y0,y1),
                                b.get("angle", 0) or 0, img_name, b["text"]))
    # DVĚ FÁZE: nejdřív všechny podklady, pak všechny texty.
    # Jinak by box souseda (rámečky se často dotýkají) přebil už vysazený text.
    for phase in ("bg", "tx"):
        for b, col in zip(boxes, colors):
            txt = trans.get(b["text"], b["text"])  # bez překladu → originál
            if not txt.strip(): continue
            if b.get("path"): draw_path(base, b, txt, lang, phase, col)
            else: draw_rect(base, b, txt, lang, phase, col)
    os.makedirs(f"{OUT}/{lang}", exist_ok=True)
    dst = f"{OUT}/{lang}/{img_name}.webp"
    base.convert("RGB").save(dst, "WEBP", quality=88, method=4)
    return dst

if __name__ == "__main__":
    lang = sys.argv[1]
    imgs = sys.argv[2:] or [os.path.splitext(os.path.basename(p))[0] for p in glob.glob(f"{BOXES}/*.json")]
    tf = f"{TRANS}/{lang}.json"
    trans = json.load(open(tf)) if os.path.exists(tf) else {}
    for n in imgs:
        if not os.path.exists(f"{GFX}/{n}.webp"): continue
        print("→", render(n, lang, trans))
