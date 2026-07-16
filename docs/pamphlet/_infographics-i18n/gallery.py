#!/usr/bin/env python3
"""Vytvoří HTML galerii vygenerovaných obrázků pro rychlou kontrolu v prohlížeči.
Použití:  python3 gallery.py de          → out/de/gallery.html
          python3 gallery.py de --mask   → galerie masek (kontrola pokrytí)
Vedle sebe: ORIGINÁL | PŘELOŽENÝ — aby šlo srovnat na jeden pohled.
"""
import sys, os, glob, json

BK = os.path.dirname(os.path.abspath(__file__))
GFX = "/Users/pavelkudrna/RiderProjects/new-world-order/Prezentace/Info Graphics/v5"

lang = sys.argv[1] if len(sys.argv) > 1 else "de"
mask_mode = "--mask" in sys.argv
src_dir = f"{BK}/mask" if mask_mode else f"{BK}/out/{lang}"
title = f"Masky (kontrola pokrytí)" if mask_mode else f"Titulky — {lang.upper()}"

imgs = sorted(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(f"{src_dir}/*.webp"))
rows = []
for i, n in enumerate(imgs, 1):
    rows.append(f"""
<section id="i{i}">
  <h2><span class="num">{i}/{len(imgs)}</span> {n}</h2>
  <div class="pair">
    <figure><figcaption>originál (EN)</figcaption><img loading="lazy" src="file://{GFX}/{n}.webp"></figure>
    <figure><figcaption>{'maska' if mask_mode else lang}</figcaption><img loading="lazy" src="{'mask' if mask_mode else 'out/'+lang}/{n}.webp"></figure>
  </div>
</section>""")

html = f"""<!doctype html><html lang="cs"><head><meta charset="utf-8">
<title>{title}</title>
<style>
 body{{margin:0;background:#15171a;color:#e8e8e8;font:14px/1.5 -apple-system,Segoe UI,sans-serif}}
 header{{position:sticky;top:0;background:#0d0e10;padding:10px 18px;border-bottom:1px solid #333;z-index:9}}
 header h1{{margin:0;font-size:16px}} header p{{margin:4px 0 0;color:#9ad;font-size:12px}}
 section{{padding:18px;border-bottom:1px solid #2a2d31}}
 h2{{font-size:14px;margin:0 0 8px;color:#ccc;font-weight:600}}
 .num{{background:#2a4d6a;color:#cef;padding:2px 7px;border-radius:5px;margin-right:8px;font-size:12px}}
 .pair{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
 figure{{margin:0}} figcaption{{font-size:11px;color:#888;margin-bottom:4px;text-transform:uppercase;letter-spacing:.5px}}
 img{{width:100%;border:1px solid #333;border-radius:6px;background:#000}}
 @media(max-width:1100px){{.pair{{grid-template-columns:1fr}}}}
</style></head><body>
<header><h1>{title}</h1><p>{len(imgs)} obrázků · vlevo originál, vpravo výsledek · scrolluj a porovnávej</p></header>
{''.join(rows)}
</body></html>"""

out = f"{BK}/gallery-{'mask' if mask_mode else lang}.html"
open(out, "w").write(html)
print("→", out)
