# Infographic subtitle overlay (pamphlet i18n)

Localizes the pamphlet's baked-in-English infographics into 46 languages by
overlaying subtitle-style captions on top of the original English text.

Manual box placement beat OCR and vision detection, so positions are drawn by
hand once per image; then translations are poured in per language and images are
generated mechanically.

Each caption takes the colour of whatever it sits on, so it reads as part of the
artwork rather than as a patch. The colour is sampled from the source image, so
it does not depend on the language — every language gets the same plate.

## Layout

| Path | What |
|------|------|
| `server.py` + `index.html` | Box editor (HTTP :8770): draw / move / rotate / path, copy-paste |
| `imgboxes/*.json` | **Hand-drawn boxes** per image — `[{text, role, bbox, angle, joined}]` or `{text, path, thickness}`. Irreplaceable manual work. |
| `imgtexts/*.json` | English text list per image (left panel of the editor) |
| `all_texts.json` | Flat list of all 1406 unique English strings (translation input) |
| `trans/{lang}.json` | `{english: translated}` per language |
| `render.py` | Generator: reads `imgboxes` + `trans/{lang}`, writes `out/{lang}/*.webp` |
| `check.py` | Pre-render validation: JSON completeness + glyph coverage (catches tofu) |
| `pair.py` | Pairs an ordered translation list (`trans_raw/{lang}.json`) with the English keys |
| `plate_overrides.json` | Hand-picked plate colour for the handful of boxes the sampler cannot reach |
| `gallery.py` | Side-by-side HTML gallery (original vs translated) for review |
| `mask.py` | Coverage diagnostic (magenta over every box → readable text = a gap) |

Generated output (`out/`, `mask/`, `venv/`, `trans_raw/`) is git-ignored — it is
rebuilt from the sources above.

## Regenerate one language

```
./venv/bin/python render.py de          # → out/de/*.webp
./venv/bin/python check.py de            # validate first
./venv/bin/python gallery.py de          # → gallery-de.html
```

## Plate colour

Sampled from *inside* the box: the original English text is there, but it is a
minority of the area, so it does not sway the result. Sampling a ring around the
box instead was measurably worse (79% of boxes vs 89%) — a ring catches the
speech-bubble outline or nearby artwork.

Text and background are separated by an Otsu luminance split rather than by
picking the most common shade, because a shaded pillar or band spreads across
dozens of shades and no single one wins. The larger class is the background; its
median gives the colour, and the share of the box holding that colour decides
whether the box is on flat ground (take the colour) or over artwork (fall back to
a dark subtitle box, which reads as a deliberate overlay).

Rotated boxes are sampled rotated — sampling their upright bounding box drags in
surrounding artwork.

The threshold sits in the gap in the measured distribution, far below the bulk of
real backgrounds. A threshold in the middle of the distribution lets noise decide,
and two identical labels side by side come out differently — which is exactly what
a reader notices.

`ADAPTIVE=0` restores the plain dark box everywhere.

## Vertical fit

Both the autofit and the centring go by the **ink** — the real glyph bounds —
not by the font's nominal line height. Arabic, Hebrew, Thai, Devanagari and
Armenian glyphs sit lower in the line than the nominal box suggests, so centring
on the envelope pushed the ink below the box: it clipped 55% of Arabic captions
(and the image edge cut the ones near the bottom). Latin, Cyrillic, Greek, CJK
and Korean never showed it, which is why it survived a visual check.

## Fonts

Latin/Cyrillic/Greek/Vietnamese ride on Arial Bold; CJK, Devanagari, Thai,
Arabic, Hebrew and Armenian each get a script-specific system font. A per-glyph
fallback to Arial Unicode fills in symbols the main font lacks (✓ ∝ ₁ ₂). RTL
(ar/he) is reshaped via arabic_reshaper + python-bidi.

Image source: `~/RiderProjects/new-world-order/Prezentace/Info Graphics/v5`
(2528×1696 and other resolutions; read dynamically per image).

Translations are machine-generated.
