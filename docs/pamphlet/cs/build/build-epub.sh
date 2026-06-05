#!/usr/bin/env bash
# build-epub.sh — produkuje reflowable EPUB CZ pamfletu, vedle fixed-layout PDF.
# Stejné markdown zdroje, jiný výstupní cíl.
#
# Output: pamphlet-v6-cz.epub  (nebo pamphlet-v6-cz-DRAFT.epub s --watermark)
#
# Usage:
#   ./build-epub.sh
#   ./build-epub.sh --watermark
#   ./build-epub.sh --watermark-text "K REVIZI"
#   ./build-epub.sh --watermark-banner "Před redakční úpravou"
#
# Strategy:
#   1. Předpoklad: main ./build.sh proběhl (figures/*.png musí existovat).
#   2. Konkatenovat CZ kapitoly v kanonickém pořadí, rewritnout Obsidian
#      ![[...]] refs a .webp paths na figures/*.png.
#   3. S --watermark: před každou kapitolu vložit draft banner div a CSS
#      pravidla s body::before diagonálním razítkem.
#   4. Pandoc → EPUB3 s metadata + stylesheet.

set -euo pipefail

BUILD_DIR="$(cd "$(dirname "$0")" && pwd)"
PAMPHLET_DIR="$(cd "$BUILD_DIR/.." && pwd)"
EPUB_DIR="$BUILD_DIR/epub"

cd "$BUILD_DIR"

# ----- 0. Argument parsing -----
WATERMARK=0
WATERMARK_TEXT="PRACOVNÍ VERZE — NEŠÍŘIT"
WATERMARK_BANNER="Před redakční úpravou"
while [ $# -gt 0 ]; do
  case "$1" in
    --watermark) WATERMARK=1 ;;
    --watermark=*) WATERMARK=1; WATERMARK_TEXT="${1#*=}" ;;
    --watermark-text) shift; WATERMARK_TEXT="$1"; WATERMARK=1 ;;
    --watermark-banner) shift; WATERMARK_BANNER="$1"; WATERMARK=1 ;;
    -h|--help) sed -n '2,30p' "$0"; exit 0 ;;
    *) echo "ERROR: unknown argument '$1'"; exit 1 ;;
  esac
  shift
done

command -v pandoc >/dev/null || { echo "ERROR: pandoc missing"; exit 1; }
[ -d figures ] || { echo "ERROR: figures/ not found — spusť ./build.sh nejdřív"; exit 1; }

echo "[1/3] preparing combined markdown"

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
COMBINED="$TMP/combined.md"

# Pořadí odpovídá master pamphlet.tex (jen mainmatter — title page přichází z
# metadata.yaml, glossary na konci).
SOURCES=(
  "$PAMPHLET_DIR/01-uvod/01-uvod.md"
  "$PAMPHLET_DIR/02-predpoklady/01-predpoklady.md"
  "$PAMPHLET_DIR/03-nastroj/01-sit.md"
  "$PAMPHLET_DIR/03-nastroj/02-necenzurovatelnost.md"
  "$PAMPHLET_DIR/03-nastroj/03-pochybnosti.md"
  "$PAMPHLET_DIR/03-nastroj/04-dobrovolnost-a-svoboda.md"
  "$PAMPHLET_DIR/03-nastroj/05-prepinac-svoboda-totalita.md"
  "$PAMPHLET_DIR/03-nastroj/06-oracle-problem.md"
  "$PAMPHLET_DIR/04-overovani/01-konsenzus.md"
  "$PAMPHLET_DIR/04-overovani/02-role-a-autority/01-prehled-roli.md"
  "$PAMPHLET_DIR/04-overovani/02-role-a-autority/02-vydavatel.md"
  "$PAMPHLET_DIR/04-overovani/02-role-a-autority/03-autorita.md"
  "$PAMPHLET_DIR/04-overovani/02-role-a-autority/04-overovatel.md"
  "$PAMPHLET_DIR/04-overovani/02-role-a-autority/05-subjekt.md"
  "$PAMPHLET_DIR/04-overovani/02-role-a-autority/06-pozorovatel.md"
  "$PAMPHLET_DIR/04-overovani/02-role-a-autority/07-delegovani.md"
  "$PAMPHLET_DIR/04-overovani/02-role-a-autority/08-komunikace.md"
  "$PAMPHLET_DIR/04-overovani/03-emergentni-smlouva.md"
  "$PAMPHLET_DIR/04-overovani/05-poskytovani-informaci.md"
  "$PAMPHLET_DIR/07-zlocin-a-trest/01-zlocin-a-trest.md"
  "$PAMPHLET_DIR/08-sleduj-penize/01-sleduj-penize.md"
  "$PAMPHLET_DIR/08-sleduj-penize/03-prechod/01-evoluce.md"
  "$PAMPHLET_DIR/08-sleduj-penize/03-prechod/02-ctyri-nastroje.md"
  "$PAMPHLET_DIR/08-sleduj-penize/03-prechod/03-danovy-system.md"
  "$PAMPHLET_DIR/08-sleduj-penize/03-prechod/04-esr.md"
  "$PAMPHLET_DIR/08-sleduj-penize/03-prechod/05-alokace-dani.md"
  "$PAMPHLET_DIR/08-sleduj-penize/03-prechod/06-vyjednavaci-platforma.md"
  "$PAMPHLET_DIR/08-sleduj-penize/03-prechod/07-obcanstvi.md"
  "$PAMPHLET_DIR/08-sleduj-penize/03-prechod/08-reverzibilita.md"
  "$PAMPHLET_DIR/09-zaver/01-zaver.md"
  "$EPUB_DIR/donate.md"
  "$PAMPHLET_DIR/10-rejstrik/rejstrik-pojmu.md"
)

# Strip per-file YAML frontmatter, drop Obsidian-style embeds (![[v5-...#CZ]])
# úplně, a přepsat .webp image refs na .png aby je EPUB reader zobrazil.
> "$COMBINED"
for src in "${SOURCES[@]}"; do
  if [ ! -f "$src" ]; then
    echo "WARNING: missing source $src — skipping" >&2
    continue
  fi
  python3 - "$src" >> "$COMBINED" <<'PY'
import re, sys
path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Strip leading YAML frontmatter
text = re.sub(r'\A---\n.*?\n---\n', '', text, count=1, flags=re.DOTALL)

# Drop Obsidian wikilink embeds: ![[v5-foo#CZ]] / #EN / #CS
text = re.sub(r'!\[\[[^\]]+\]\]\s*\n?', '', text)

# Rewrite .webp image refs to figures/v5-<name>.png (paths used by main build)
def rewrite(m):
    alt = m.group(1)
    name = m.group(2)
    return f'![{alt}](figures/v5-{name}.png)'
text = re.sub(
    r'!\[([^\]]*)\]\((?:[^)]*?/)?v5-([a-z0-9-]+)\.webp\)',
    rewrite, text)

# Tighten blank lines, ensure terminal newline + page-break.
text = re.sub(r'\n{3,}', '\n\n', text).strip() + '\n\n'
print(text)
PY
done

echo "[2/3] pandoc -> epub3"

if [ "$WATERMARK" = "1" ]; then
  CSS_FILE="$TMP/style-draft.css"
  cp "$EPUB_DIR/style.css" "$CSS_FILE"
  cat >> "$CSS_FILE" <<EOF

/* ----- Watermark overlay (build-epub.sh --watermark) ----- */
.draft-banner {
  display: block;
  text-align: center;
  font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  font-size: 0.85em;
  font-weight: bold;
  color: #B83838;
  background: #fbe6e6;
  border: 1px solid #B83838;
  padding: 0.3em 0.6em;
  margin: 0 0 1.4em 0;
  letter-spacing: 0.05em;
}
.draft-banner .sub {
  display: block;
  font-weight: normal;
  font-style: italic;
  font-size: 0.85em;
  margin-top: 0.15em;
  letter-spacing: 0;
}
body::before {
  content: "$WATERMARK_TEXT";
  position: fixed;
  top: 40%;
  left: -10%;
  width: 120%;
  text-align: center;
  font-family: "Helvetica Neue", sans-serif;
  font-weight: bold;
  font-size: 3em;
  color: rgba(184, 56, 56, 0.10);
  transform: rotate(-22deg);
  pointer-events: none;
  z-index: 0;
}
EOF
  OUTPUT="pamphlet-v6-cz-DRAFT.epub"

  python3 - "$COMBINED" "$WATERMARK_TEXT" "$WATERMARK_BANNER" <<'PY'
import sys, re
path, big, banner = sys.argv[1:4]
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
def html_escape(s):
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
big_e = html_escape(big)
banner_e = html_escape(banner)
inject = (f'\n\n::: {{.draft-banner}}\n'
          f'{big_e}<span class="sub">{banner_e}</span>\n'
          f':::\n\n')
out = []
for line in text.splitlines(keepends=True):
    out.append(line)
    if re.match(r'^# [^#]', line):
        out.append(inject)
final = inject + ''.join(out)
with open(path, 'w', encoding='utf-8') as f:
    f.write(final)
PY
else
  CSS_FILE="$EPUB_DIR/style.css"
  OUTPUT="pamphlet-v6-cz.epub"
fi

pandoc \
  --from=markdown+pipe_tables+yaml_metadata_block+raw_html+raw_tex+fenced_divs \
  --to=epub3 \
  --metadata-file="$EPUB_DIR/metadata.yaml" \
  --css="$CSS_FILE" \
  --toc --toc-depth=2 \
  --split-level=1 \
  --resource-path="$BUILD_DIR" \
  -o "$OUTPUT" \
  "$COMBINED"

echo "[3/3] done"
echo
echo "BUILD OK: $BUILD_DIR/$OUTPUT"
ls -lh "$OUTPUT"
