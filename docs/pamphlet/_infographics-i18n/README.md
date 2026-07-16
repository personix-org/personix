# Infographic subtitle overlay (pamphlet i18n)

Localizes the pamphlet's baked-in-English infographics into 46 languages by
overlaying subtitle-style captions (dark box + light translated text) on top of
the original English text — the same visible-overlay convention as the web cover.

Manual box placement beat OCR and vision detection, so positions are drawn by
hand once per image; then translations are poured in per language and images are
generated mechanically.

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

## Fonts

Latin/Cyrillic/Greek/Vietnamese ride on Arial Bold; CJK, Devanagari, Thai,
Arabic, Hebrew and Armenian each get a script-specific system font. A per-glyph
fallback to Arial Unicode fills in symbols the main font lacks (✓ ∝ ₁ ₂). RTL
(ar/he) is reshaped via arabic_reshaper + python-bidi.

Image source: `~/RiderProjects/new-world-order/Prezentace/Info Graphics/v5`
(2528×1696 and other resolutions; read dynamically per image).

Translations are machine-generated.
