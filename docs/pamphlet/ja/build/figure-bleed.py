#!/usr/bin/env python3
"""Soft-edge ("spadačka") preparation for full-page figures (PRINT build).

DEFAULT MODE — used for figures whose border is clean background (the majority):
the figure keeps its size/ratio and only its outermost ~2 % (background pixels)
is feathered to transparent, so the edge dissolves into the page tint
(figbg@<name>, taken from the contact edge). Content stays crisp; no blur, no
scaling, no mirroring. The print master draws this with keepaspectratio inside a
safe zone leaving ≥5 mm to the trim.

Figures whose CONTENT or a dark/coloured field runs to the border are handled
individually (see FULLBLEED list in build.sh / the per-figure override) — a flat
or feathered margin can't blend there, so those go full-bleed to the trim
instead. This script intentionally does ONE thing (feather) and does not try a
global transform that would damage the figures that were already fine.

A 1–3 px darker antialiased cut line on the border is trimmed first.

Output: RGBA PNG in <outdir>, same basename, same (trimmed) pixel size.
Usage: figure-bleed.py <figures-dir> <out-dir> [basename-glob]
"""
import sys, os, glob
from PIL import Image, ImageChops

INSET = 0.004     # crop the antialiased cut line (fraction of min side)
FEATHER = 0.020   # outer fraction of WIDTH that fades to transparent


def _ramp(n, f):
    p = [255] * n
    for i in range(f):
        v = int(round(255 * (i + 1) / (f + 1)))
        p[i] = v; p[n - 1 - i] = v
    return p


def _axis(profile, w, h, horizontal):
    if horizontal:
        ln = Image.new("L", (len(profile), 1)); ln.putdata(profile)
    else:
        ln = Image.new("L", (1, len(profile))); ln.putdata(profile)
    return ln.resize((w, h))


def process(path, outdir):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    inset = max(2, int(round(INSET * min(w, h))))
    im = im.crop((inset, inset, w - inset, h - inset))
    w, h = im.size
    f = max(1, int(round(FEATHER * w)))
    alpha = ImageChops.darker(_axis(_ramp(w, f), w, h, True),
                              _axis(_ramp(h, f), w, h, False))
    im.putalpha(alpha)
    os.makedirs(outdir, exist_ok=True)
    im.save(os.path.join(outdir, os.path.basename(path)))


def main():
    figdir, outdir = sys.argv[1], sys.argv[2]
    pat = sys.argv[3] if len(sys.argv) > 3 else "v5-*.png"
    files = sorted(glob.glob(os.path.join(figdir, pat)))
    for fp in files:
        process(fp, outdir)
    print(f"soft-edged {len(files)} figure(s) -> {outdir}  (FEATHER={FEATHER})")


if __name__ == "__main__":
    main()
