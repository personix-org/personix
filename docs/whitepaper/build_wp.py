#!/usr/bin/env python3
"""Sestaví přeloženou verzi whitepaperu do PDF.

Překlady sdílejí preambuli s anglickým originálem, která je psaná pro pdfLaTeX
(`inputenc` + `fontenc` + `times`). Tectonic jede na XeTeX, kde tahle trojice
tiše zahodí glyfy, které Cork encoding nezná — cyrilici, řečtinu, vietnamské
tóny, ázerbájdžánské ě. Skript proto preambuli před sestavením přepíše na
`fontspec` a podle písma jazyka doplní odpovídající rodinu fontů.

Použití:
    python3 build_wp.py <kód jazyka> [...]      # whitepaper-<kód>.tex → PDF
    python3 build_wp.py --all                   # všechny nalezené překlady

Hotová PDF putují do `release/whitepaper-<kód>.pdf`.
"""
import os, re, shutil, subprocess, sys, glob, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
RELEASE = os.path.abspath(os.path.join(HERE, '..', '..', 'release'))

# Písmo → font, který ho pokrývá. Hodnoty jsou systémové fonty macOS.
CJK = {'ja': 'Hiragino Sans', 'zh-cn': 'Hiragino Sans GB', 'zh-hk': 'Hiragino Sans GB',
       'zh-tw': 'Hiragino Sans GB', 'ko': 'Apple SD Gothic Neo'}
# Tyhle jazyky potřebují vlastní hlavní font, protože Times New Roman jejich
# glyfy nemá. Arménština dostává Arial Unicode MS — Mshtakan ani Noto Sans
# Armenian se u pamfletu neosvědčily.
SCRIPT = {'hi': 'Kohinoor Devanagari', 'th': 'Thonburi', 'hy': 'Arial Unicode MS'}
# Arial Unicode MS jako jediný pokrývá arabštinu i hebrejštinu spolu s latinkou,
# takže jména a zkratky v textu nezůstanou jako prázdné obdélníky.
RTL = {'ar': 'Arial Unicode MS', 'he': 'Arial Unicode MS'}

# Očekávaná velikost PDF podle písma. Latinka spadlá k 74 kB znamená, že se
# glyfy vytratily — sestavení přitom skončí bez chyby, velikost je jediný signál.
# Korejština sedí na spodní hranici pásma CJK, protože hangul se subsetuje
# úsporněji než čínské znaky — kolem 230 kB je u ní normální stav.
EXPECTED_KB = {'latin': (150, 260), 'cjk': (200, 600), 'script': (90, 200)}

PREAMBLE_OLD = re.compile(
    r'\\usepackage\[utf8\]\{inputenc\}\s*\n'
    r'\\usepackage\[T1\]\{fontenc\}\s*\n'
    r'\\usepackage\{times\}')


def font_block(lang):
    """Vrátí blok preambule s nastavením fontů pro daný jazyk."""
    lines = ['\\usepackage{fontspec}']
    if lang in SCRIPT:
        lines.append('\\setmainfont{%s}' % SCRIPT[lang])
    elif lang in RTL:
        lines.append('\\setmainfont{%s}' % RTL[lang])
    else:
        lines.append('\\setmainfont{Times New Roman}')
    if lang in CJK:
        lines.append('\\usepackage{xeCJK}')
        lines.append('\\setCJKmainfont{%s}' % CJK[lang])
    return '\n'.join(lines)


def patch(src, lang):
    """Přepíše preambuli na XeTeX a doplní fonty i obousměrné sázení."""
    out = PREAMBLE_OLD.sub(lambda m: font_block(lang), src, count=1)
    if out == src:
        raise SystemExit('preambule nenalezena — zkontroluj %s' % lang)
    if lang in RTL:
        # bidi musí stát až těsně před začátkem dokumentu, jinak koliduje
        # s amsmath a sestavení spadne na \@@leqno.
        out = out.replace('\\begin{document}',
                          '\\usepackage{bidi}\n\\begin{document}', 1)
    return out


def size_class(lang):
    if lang in CJK:
        return 'cjk'
    if lang in SCRIPT or lang in RTL:
        return 'script'
    return 'latin'


def build(lang):
    tex = os.path.join(HERE, 'whitepaper-%s.tex' % lang)
    if not os.path.exists(tex):
        return lang, False, 'zdroj chybí'
    with tempfile.TemporaryDirectory() as work:
        open(os.path.join(work, 'wp.tex'), 'w', encoding='utf-8').write(
            patch(open(tex, encoding='utf-8').read(), lang))
        for extra in ('references.bib',):
            shutil.copy(os.path.join(HERE, extra), work)
        if os.path.isdir(os.path.join(HERE, 'infographics')):
            shutil.copytree(os.path.join(HERE, 'infographics'),
                            os.path.join(work, 'infographics'))
        r = subprocess.run(['tectonic', 'wp.tex'], cwd=work,
                           capture_output=True, text=True)
        pdf = os.path.join(work, 'wp.pdf')
        if not os.path.exists(pdf):
            return lang, False, (r.stderr or '')[-400:]
        kb = os.path.getsize(pdf) // 1024
        lo, hi = EXPECTED_KB[size_class(lang)]
        note = '%d kB' % kb
        if not (lo <= kb <= hi):
            note += ' ⚠ mimo očekávaný rozsah %d–%d' % (lo, hi)
        shutil.copy(pdf, os.path.join(RELEASE, 'whitepaper-%s.pdf' % lang))
        return lang, True, note


def main(argv):
    if not argv:
        raise SystemExit(__doc__)
    if argv[0] == '--all':
        langs = sorted(os.path.basename(p)[len('whitepaper-'):-4]
                       for p in glob.glob(os.path.join(HERE, 'whitepaper-*.tex'))
                       if not p.endswith('-cz.tex'))
    else:
        langs = argv
    failed = []
    for lang in langs:
        lang, ok, note = build(lang)
        print('%-8s %s %s' % (lang, 'OK  ' if ok else 'CHYBA', note), flush=True)
        if not ok:
            failed.append(lang)
    print('\nhotovo %d/%d' % (len(langs) - len(failed), len(langs)))
    if failed:
        print('selhalo:', ' '.join(failed))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
