#!/usr/bin/env python3
"""Maska: zakryje všechny označené rámečky/cesty plnou barvou, text NEvysází.
Co na výsledku zůstane čitelné = text BEZ rámečku (mezera v označení)."""
import os, json, glob, math
from PIL import Image, ImageDraw
BK = os.path.dirname(os.path.abspath(__file__))
GFX = "/Users/pavelkudrna/RiderProjects/new-world-order/Prezentace/Info Graphics/v5"
OUT = f"{BK}/mask"
os.makedirs(OUT, exist_ok=True)
MAG = (255, 0, 200, 255)  # křiklavá barva — jasně odliší zakryté oblasti

for p in sorted(glob.glob(f"{BK}/imgboxes/*.json")):
    n = os.path.splitext(os.path.basename(p))[0]
    src = f"{GFX}/{n}.webp"
    if not os.path.exists(src): continue
    im = Image.open(src).convert("RGBA")
    W, H = im.size
    for b in json.load(open(p)):
        if b.get("path"):
            pts = [tuple(q) for q in b["path"]]
            pts = [q for i,q in enumerate(pts) if i==0 or math.dist(q,pts[i-1])>1]
            if len(pts) < 2: continue
            th = int(b.get("thickness",60))
            lay = Image.new("RGBA", im.size, (0,0,0,0)); d = ImageDraw.Draw(lay)
            d.line(pts, fill=MAG, width=th, joint="curve")
            for q in (pts[0], pts[-1]):
                d.ellipse([q[0]-th//2,q[1]-th//2,q[0]+th//2,q[1]+th//2], fill=MAG)
            im.alpha_composite(lay)
        else:
            x0,y0,x1,y1 = b["bbox"]
            x0,y0,x1,y1 = min(x0,x1),min(y0,y1),max(x0,x1),max(y0,y1)
            a = b.get("angle",0) or 0
            if not a:   # nerotovaný přes okraj → POSUŇ dovnitř (neořezávej!)
                if x0<0: x1-=x0; x0=0
                if y0<0: y1-=y0; y0=0
                if x1>W: x0-=(x1-W); x1=W
                if y1>H: y0-=(y1-H); y1=H
                x0,y0 = max(0,x0), max(0,y0)
            w,h = int(x1-x0), int(y1-y0)
            if w<4 or h<4: continue
            m = 8
            tile = Image.new("RGBA",(w+2*m,h+2*m),(0,0,0,0))
            ImageDraw.Draw(tile).rounded_rectangle([0,0,w+2*m-1,h+2*m-1], radius=min(12,h//2), fill=MAG)
            if a: tile = tile.rotate(-a, expand=True, resample=Image.BICUBIC)
            lay = Image.new("RGBA", im.size, (0,0,0,0))
            lay.paste(tile, (int((x0+x1)/2 - tile.width/2), int((y0+y1)/2 - tile.height/2)), tile)
            im.alpha_composite(lay)
    im.convert("RGB").save(f"{OUT}/{n}.webp", "WEBP", quality=80, method=4)
print("masek:", len(glob.glob(f"{OUT}/*.webp")))
