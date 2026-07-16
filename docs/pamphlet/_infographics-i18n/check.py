#!/usr/bin/env python3
"""Validace překladu PŘED renderem — chytne useknutý JSON i tofu (chybějící glyfy).

Použití:  ./venv/bin/python check.py <lang> [<lang> ...]
Kontroluje:
 1) trans/{lang}.json jde načíst, má přesně tytéž klíče jako EN sada (žádný chybí/přebývá)
 2) každý znak přeložené hodnoty existuje v cmapě fontu zvoleného pro daný jazyk
    (jinak by render vysadil prázdný obdélníček — tofu)
Návrat: 0 = OK, 1 = problém (vypíše co).
"""
import sys, os, json, glob
from fontTools.ttLib import TTFont, TTCollection

BK = os.path.dirname(os.path.abspath(__file__))
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
FALLBACK_FONT = f"{SYS}/Supplemental/Arial Unicode.ttf"  # render doplní odsud symboly (✓ ∝ ₁ ₂)

_cm = {}
def _chars(path):
    if path in _cm: return _cm[path]
    chars = set()
    try:
        chars |= set(TTFont(path, fontNumber=0).getBestCmap().keys())
    except Exception:
        try:
            for f in TTCollection(path).fonts:
                try: chars |= set(f.getBestCmap().keys())
                except Exception: pass
        except Exception: pass
    _cm[path] = chars
    return chars

def cmap_for(lang):
    # znak je OK, pokud ho umí HLAVNÍ font jazyka NEBO fallback (render sáhne po fallbacku)
    return _chars(FONTS.get(lang, DEFAULT_FONT)) | _chars(FALLBACK_FONT)

# znaky, které font pokrývat nemusí (mezery, řídící) — ignoruj
IGNORE = set(range(0x20)) | {0x20, 0xA0, 0x200b, 0x200c, 0x200d, 0x200e, 0x200f, 0xfeff}

def en_keys():
    seen = {}
    for p in sorted(glob.glob(f"{BK}/imgboxes/*.json")):
        for b in json.load(open(p)):
            t = b["text"].strip()
            if t: seen[t] = 1
    return set(seen.keys())

def check(lang, keys):
    tf = f"{BK}/trans/{lang}.json"
    if not os.path.exists(tf):
        print(f"[{lang}] CHYBÍ soubor {tf}"); return False
    try:
        d = json.load(open(tf))
    except Exception as e:
        print(f"[{lang}] JSON nejde načíst: {e}"); return False
    tk = set(d.keys())
    miss = keys - tk
    extra = tk - keys
    ok = True
    if miss:
        print(f"[{lang}] CHYBÍ {len(miss)} klíčů, např.: {list(miss)[:3]}"); ok = False
    if extra:
        print(f"[{lang}] PŘEBÝVÁ {len(extra)} klíčů (změněný klíč?), např.: {list(extra)[:3]}"); ok = False
    empty = [k for k in keys & tk if not str(d[k]).strip()]
    if empty:
        print(f"[{lang}] {len(empty)} prázdných hodnot, např.: {empty[:3]}"); ok = False
    cm = cmap_for(lang)
    badchars, samples = set(), []
    for k in keys & tk:
        for ch in str(d[k]):
            o = ord(ch)
            if o in IGNORE: continue
            if o not in cm:
                badchars.add(ch)
                if len(samples) < 5: samples.append((ch, hex(o), d[k][:30]))
    if badchars:
        print(f"[{lang}] TOFU — {len(badchars)} znaků mimo font: {sorted(badchars)[:20]}")
        for s in samples: print(f"         {s}")
        ok = False
    if ok:
        print(f"[{lang}] OK — {len(tk)} překladů, glyfy pokryté")
    return ok

if __name__ == "__main__":
    keys = en_keys()
    langs = sys.argv[1:] or [os.path.splitext(os.path.basename(p))[0] for p in glob.glob(f"{BK}/trans/*.json")]
    allok = all(check(l, keys) for l in sorted(langs))
    sys.exit(0 if allok else 1)
