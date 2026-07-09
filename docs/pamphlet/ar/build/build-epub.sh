#!/usr/bin/env bash
# build-epub.sh — produces a reflowable EPUB of the pamphlet, alongside the
# fixed-layout PDF. Same markdown sources, different output target.
#
# Output: pamphlet-v6-en.epub
#
# Strategy:
#   1. Run main build first to ensure figures/*.png and post-processed
#      chapters/*.tex exist (we reuse the figures, but read markdown directly).
#   2. Concatenate chapter markdowns in canonical order, rewrite Obsidian-
#      style refs, swap .webp paths to figures/*.png (Apple Books / Calibre /
#      most readers don't support WebP).
#   3. Hand the result to pandoc with EPUB stylesheet + metadata.

set -euo pipefail

BUILD_DIR="$(cd "$(dirname "$0")" && pwd)"
PAMPHLET_DIR="$(cd "$BUILD_DIR/.." && pwd)"
EPUB_DIR="$BUILD_DIR/epub"

cd "$BUILD_DIR"

# Need pandoc + figure pngs
command -v pandoc >/dev/null || { echo "ERROR: pandoc missing"; exit 1; }
[ -d figures ] || { echo "ERROR: figures/ not found — run ./build.sh first"; exit 1; }

echo "[1/3] preparing combined markdown"

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
COMBINED="$TMP/combined.md"

# Order matches master pamphlet.tex (mainmatter only — title page comes from
# metadata.yaml, glossary appended at the end).
SOURCES=(
  "$PAMPHLET_DIR/01-intro/01-intro.md"
  "$PAMPHLET_DIR/02-prerequisites/01-prerequisites.md"
  "$PAMPHLET_DIR/03-tool/01-network.md"
  "$PAMPHLET_DIR/03-tool/02-uncensorability.md"
  "$PAMPHLET_DIR/03-tool/03-doubts.md"
  "$PAMPHLET_DIR/03-tool/04-voluntariness-and-freedom.md"
  "$PAMPHLET_DIR/03-tool/05-freedom-totalitarianism-switch.md"
  "$PAMPHLET_DIR/03-tool/06-oracle-problem.md"
  "$PAMPHLET_DIR/04-verification/01-consensus.md"
  "$PAMPHLET_DIR/04-verification/02-roles-and-authorities/01-roles-overview.md"
  "$PAMPHLET_DIR/04-verification/02-roles-and-authorities/02-publisher.md"
  "$PAMPHLET_DIR/04-verification/02-roles-and-authorities/03-authority.md"
  "$PAMPHLET_DIR/04-verification/02-roles-and-authorities/04-verifier.md"
  "$PAMPHLET_DIR/04-verification/02-roles-and-authorities/05-subject.md"
  "$PAMPHLET_DIR/04-verification/02-roles-and-authorities/06-observer.md"
  "$PAMPHLET_DIR/04-verification/02-roles-and-authorities/07-delegation.md"
  "$PAMPHLET_DIR/04-verification/02-roles-and-authorities/08-communication.md"
  "$PAMPHLET_DIR/04-verification/03-emergent-contract.md"
  "$PAMPHLET_DIR/04-verification/05-information-provision.md"
  "$PAMPHLET_DIR/07-crime-and-punishment/01-crime-and-punishment.md"
  "$PAMPHLET_DIR/08-follow-the-money/01-follow-the-money.md"
  "$PAMPHLET_DIR/08-follow-the-money/03-transition/01-evolution.md"
  "$PAMPHLET_DIR/08-follow-the-money/03-transition/02-four-tools.md"
  "$PAMPHLET_DIR/08-follow-the-money/03-transition/03-tax-system.md"
  "$PAMPHLET_DIR/08-follow-the-money/03-transition/04-esr.md"
  "$PAMPHLET_DIR/08-follow-the-money/03-transition/05-tax-allocation.md"
  "$PAMPHLET_DIR/08-follow-the-money/03-transition/06-negotiation-platform.md"
  "$PAMPHLET_DIR/08-follow-the-money/03-transition/07-citizenship.md"
  "$PAMPHLET_DIR/08-follow-the-money/03-transition/08-reversibility.md"
  "$PAMPHLET_DIR/09-conclusion/01-conclusion.md"
  "$EPUB_DIR/donate.md"
  "$PAMPHLET_DIR/10-index/glossary.md"
)

# Strip per-file YAML frontmatter (only the top-level metadata.yaml feeds
# pandoc), drop Obsidian-style embeds (![[v5-...#EN]]) entirely, and rewrite
# .webp image refs to .png so the EPUB reader actually displays them.
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

# Drop Obsidian wikilink embeds: ![[v5-foo#EN]]
text = re.sub(r'!\[\[[^\]]+\]\]\s*\n?', '', text)

# Rewrite .webp image refs to figures/v5-<name>.png (paths used by main build)
def rewrite(m):
    alt = m.group(1)
    name = m.group(2)
    return f'![{alt}](figures/v5-{name}.png)'
text = re.sub(
    r'!\[([^\]]*)\]\((?:[^)]*?/)?v5-([a-z0-9-]+)\.webp\)',
    rewrite, text)

# Tighten consecutive blank lines, ensure terminal newline + page-break.
text = re.sub(r'\n{3,}', '\n\n', text).strip() + '\n\n'
print(text)
PY
done

echo "[2/3] pandoc -> epub3"
pandoc \
  --from=markdown+pipe_tables+yaml_metadata_block+raw_html+raw_tex \
  --to=epub3 \
  --metadata-file="$EPUB_DIR/metadata.yaml" \
  --css="$EPUB_DIR/style.css" \
  --toc --toc-depth=2 \
  --split-level=1 \
  --resource-path="$BUILD_DIR" \
  -o pamphlet-v6-en.epub \
  "$COMBINED"

echo "[3/3] done"
echo
echo "BUILD OK: $BUILD_DIR/pamphlet-v6-en.epub"
ls -lh pamphlet-v6-en.epub
