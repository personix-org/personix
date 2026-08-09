#!/usr/bin/env python3
"""Poskládá EPUB metadata z PŘEKLADŮ, KTERÉ UŽ V REPU JSOU — nic nepřekládá.

Proč to existuje: epub/metadata.yaml je ve všech 48 jazycích doslovná kopie
anglického, včetně `language: en`. Přeložený titul přitom v repu je — jen je
historicky roztroušený na třech místech a u každého jazyka leží jinde:

  1. build/pamphlet.tex               pdftitle / pdfsubject   (odtud ho bere PDF)
  2. 00-index.md                      frontmatter title / subtitle
  3. build/frontmatter/colophon.tex   tiráž (jediný zdroj pro ca a kk)

Bere se první zdroj, kde text není shodný s angličtinou. Změřeno: samotný
pamphlet.tex pokryje 20 jazyků, index dalších 25, colophon zbylé 2 — teprve
všechny tři dohromady dají 48/48. U `en` je shoda s angličtinou správný výsledek,
protože je to originál.

Použití:
    epub-meta.py <lang>                      → title|… subtitle|… (kontrola)
    epub-meta.py <lang> --yaml <šablona>     → celý metadata.yaml na stdout
"""
import os
import re
import sys

EN_TITLE = "Personix — Uncompromising Change"
EN_SUBTITLE = "An Uncensorable and Incorruptible Decentralized Reputation Network"

# ISBN pro EPUB — každý formát nese vlastní číslo (PDF má svoje v tiráži).
# Zdroj přidělení: personix-kampan/pamflet-metadata-48jazyku.csv (sloupec isbn_epub).
# Doplňuje se, jak NKP uvolňuje zbytek bloku 978-80-88573.
ISBN_EPUB = {
    "en": "978-80-88573-01-2",
    "cs": "978-80-88573-03-6",
}

HERE = os.path.dirname(os.path.abspath(__file__))

# Písma sázená zprava doleva — čtečka jinak listuje knihu obráceně.
RTL = {"ar", "he", "fa", "ur"}


def _from_tex(lang, field):
    path = f"{HERE}/{lang}/build/pamphlet.tex"
    if not os.path.exists(path):
        return None
    match = re.search(field + r"=\{([^}]*)\}", open(path, encoding="utf-8").read())
    return match.group(1).replace("---", "—").strip() if match else None


def _from_index(lang, field):
    path = f"{HERE}/{lang}/00-index.md"
    if not os.path.exists(path):
        return None
    for line in open(path, encoding="utf-8"):
        match = re.match(rf'^{field}:\s*"(.*)"\s*$', line)
        if match:
            return match.group(1).strip()
    return None


def _from_colophon(lang, which):
    path = f"{HERE}/{lang}/build/frontmatter/colophon.tex"
    if not os.path.exists(path):
        return None
    text = open(path, encoding="utf-8").read()
    match = re.search(r"\\textbf\{Personix\s*---\s*([^}]*)\}\\\\\[0\.3em\]\s*\n(.+?)\\\\", text)
    if not match:
        return None
    if which == "title":
        return f"Personix — {match.group(1).strip()}"
    return match.group(2).strip()


def _pick(english, *getters):
    for get in getters:
        value = get()
        if value and value != english:
            return value
    return english


def resolve(lang):
    title = _pick(
        EN_TITLE,
        lambda: _from_tex(lang, "pdftitle"),
        lambda: _from_index(lang, "title"),
        lambda: _from_colophon(lang, "title"),
    )
    subtitle = _pick(
        EN_SUBTITLE,
        lambda: _from_tex(lang, "pdfsubject"),
        lambda: _from_index(lang, "subtitle"),
        lambda: _from_colophon(lang, "sub"),
    )
    return title, subtitle


def _yaml_escape(value):
    return value.replace("\\", "\\\\").replace('"', '\\"')


def render_yaml(lang, template_path):
    title, subtitle = resolve(lang)
    out = []
    for line in open(template_path, encoding="utf-8").read().splitlines():
        if re.match(r"^title:", line):
            out.append(f'title: "{_yaml_escape(title)}"')
        elif re.match(r"^subtitle:", line):
            out.append(f'subtitle: "{_yaml_escape(subtitle)}"')
        elif re.match(r"^language:", line):
            out.append(f"language: {lang}")
            # pandoc čte pro EPUB `lang`, ne `language` — bez toho zůstane kniha anglická
            out.append(f"lang: {lang}")
            if lang in RTL:
                out.append("dir: rtl")
                out.append("page-progression-direction: rtl")
        else:
            out.append(line)
    isbn = ISBN_EPUB.get(lang)
    if isbn:
        out.append("identifier:")
        out.append("  - scheme: ISBN")
        out.append(f"    text: {isbn}")
    return "\n".join(out) + "\n"


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    lang = argv[1]
    if "--yaml" in argv:
        template = argv[argv.index("--yaml") + 1]
        sys.stdout.write(render_yaml(lang, template))
    else:
        title, subtitle = resolve(lang)
        print(f"title|{title}")
        print(f"subtitle|{subtitle}")


if __name__ == "__main__":
    main(sys.argv)
