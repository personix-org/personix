#!/usr/bin/env python3
"""Doplní out/{lang}/expanded/ — A5 plátno pro sazbu pamfletu.

Ruční expanded z GIMPu (v5/expanded/) je originál vycentrovaný na vyšším plátně
s dokresleným pruhem nahoře a dole. Změřeno na 63 obrázcích: posun je vždy přesně
(výška_expanded - výška_originálu) // 2, odchylka jen ze ztrátové komprese. Pruhy
tedy stačí převzít a doprostřed vložit lokalizovanou verzi — ruční práce se pro
každý jazyk neopakuje.

Obálka (v5-cover-landscape) je výjimka: její expanded je přemalovaný, ne dopočitatelný.
Nechává se bez expanded, build pak sáhne po lokalizovaném originálu (poměr 1.420 vs
1.419, vizuálně totéž).
"""
from PIL import Image
import sys, os, glob

V = "/Users/pavelkudrna/RiderProjects/new-world-order/Prezentace/Info Graphics/v5"

def main(lang, only=None):
    src = f"out/{lang}"
    if not os.path.isdir(src):
        sys.exit(f"CHYBA: {src} neexistuje — pusť nejdřív render.py {lang}")
    dst = f"{src}/expanded"
    os.makedirs(dst, exist_ok=True)
    made = skipped = 0
    for f in sorted(glob.glob(f"{src}/*.webp")):
        b = os.path.basename(f)
        if only and b != only:
            continue
        ref = f"{V}/expanded/{b}"
        if not os.path.exists(ref):
            skipped += 1; continue
        loc = Image.open(f).convert("RGB")
        exp = Image.open(ref).convert("RGB")
        if exp.width != loc.width:
            # obálka — nedopočitatelná, build vezme neexpandovaný originál
            skipped += 1; continue
        dy = (exp.height - loc.height) // 2
        out = exp.copy()
        out.paste(loc, (0, dy))
        out.save(f"{dst}/{b}", "WEBP", quality=92, method=6)
        made += 1
    print(f"[{lang}] expanded: {made} vyrobeno, {skipped} bez expanded (obálka → originál)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("použití: expand.py <lang> [jen-tenhle-soubor.webp]")
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
