#!/bin/bash
# Postaví pamflet (PDF + EPUB) ve všech jazycích, které mají lokalizované infografiky.
#
# Na jazyk:  check.py → render.py → expand.py → build.sh (PDF) → build-epub.sh (EPUB)
# EPUB musí běžet AŽ PO build.sh — bere si obrázky z figures/, které build.sh vyrobí.
#
# Hotové soubory jdou do STAGE_DIR mimo git: veřejné repo personix je schválně
# malé (181 MB) a 45 jazyků × ~70 MB by ho nafouklo přes 3 GB, navíc při každém
# přesázení znovu — historie se v gitu nikdy nezmenšuje. Na server se odsud
# posílá zvlášť.
#
# Mezivýsledky (out/<lang>, figures/) se po každém jazyce mažou — jinak by běh
# sežral ~3 GB navíc. Jsou plně regenerovatelné z imgboxes + trans.
#
# Použití:  ./build-all.sh [lang ...]     (bez argumentů = všechny přeložené jazyky)
set -uo pipefail

BOXTOOL="$HOME/Downloads/personix-boxtool"
PAMPHLET="$(cd "$(dirname "$0")" && pwd)"
STAGE_DIR="${STAGE_DIR:-$HOME/Downloads/personix-pamflety}"
PY="$BOXTOOL/venv/bin/python"

[ -x "$PY" ] || { echo "CHYBA: chybí $PY — boxtool venv"; exit 1; }
command -v pandoc >/dev/null || { echo "CHYBA: chybí pandoc (EPUB)"; exit 1; }
mkdir -p "$STAGE_DIR"

if [ $# -gt 0 ]; then
  LANGS=("$@")
else
  LANGS=()
  while IFS= read -r f; do
    l=$(basename "$f" .json)
    # jen jazyky, které mají i zdrojové MD pamfletu
    [ -d "$PAMPHLET/$l/build" ] && LANGS+=("$l")
  done < <(find "$BOXTOOL/trans" -maxdepth 1 -name '*.json' | sort)
fi

echo "Jazyků k sestavení: ${#LANGS[@]}"
echo "Cíl: $STAGE_DIR"
echo "Volno na disku: $(df -h / | awk 'NR==2{print $4}')"
echo

ok=(); failed=()
started=$(date +%s)

for lang in "${LANGS[@]}"; do
  echo "═══════════ $lang ═══════════"
  cd "$BOXTOOL" || exit 1

  if ! "$PY" check.py "$lang" >/dev/null 2>&1; then
    echo "[$lang] SELHAL: check.py (chybí překlady nebo glyfy)"; failed+=("$lang:check"); continue
  fi
  if ! "$PY" render.py "$lang" >/dev/null 2>&1; then
    echo "[$lang] SELHAL: render.py"; failed+=("$lang:render"); continue
  fi
  if ! "$PY" expand.py "$lang" >/dev/null 2>&1; then
    echo "[$lang] SELHAL: expand.py"; failed+=("$lang:expand"); continue
  fi

  cd "$PAMPHLET/$lang/build" || { failed+=("$lang:nodir"); continue; }

  if ! INFOGRAPHICS_DIR="$BOXTOOL/out/$lang" ./build.sh >"/tmp/build-$lang.log" 2>&1; then
    echo "[$lang] SELHAL: build.sh — log /tmp/build-$lang.log"; failed+=("$lang:pdf")
    rm -rf "$BOXTOOL/out/$lang"; continue
  fi

  pdf="pamphlet-v6-$lang.pdf"
  if [ -f "$pdf" ]; then
    cp "$pdf" "$STAGE_DIR/"
    echo "[$lang] PDF  $(ls -l "$pdf" | awk '{printf "%.0f MB", $5/1048576}'), $(pdfinfo "$pdf" 2>/dev/null | awk '/^Pages/{print $2}') stran"
  else
    echo "[$lang] SELHAL: build prošel, ale PDF nikde"; failed+=("$lang:nopdf")
    rm -rf "$BOXTOOL/out/$lang"; continue
  fi

  if ./build-epub.sh >"/tmp/epub-$lang.log" 2>&1; then
    epub="pamphlet-v6-$lang.epub"
    if [ -f "$epub" ]; then
      cp "$epub" "$STAGE_DIR/"
      echo "[$lang] EPUB $(ls -l "$epub" | awk '{printf "%.0f MB", $5/1048576}')"
      ok+=("$lang")
    else
      echo "[$lang] EPUB nevznikl"; failed+=("$lang:noepub")
    fi
  else
    echo "[$lang] SELHAL: build-epub.sh — log /tmp/epub-$lang.log"; failed+=("$lang:epub")
  fi

  # uklidit — vše regenerovatelné, jinak ~200 MB na jazyk navíc
  rm -rf "$BOXTOOL/out/$lang"
  rm -f "$PAMPHLET/$lang/build/"*.pdf "$PAMPHLET/$lang/build/"*.epub
  rm -rf "$PAMPHLET/$lang/build/figures"
done

elapsed=$(( ($(date +%s) - started) / 60 ))
echo
echo "════════════════════════════════════════"
echo "HOTOVO za ${elapsed} min: ${#ok[@]} OK, ${#failed[@]} selhalo"
if [ ${#failed[@]} -gt 0 ]; then echo "Selhaly:"; printf "  %s\n" "${failed[@]}"; fi
echo "Ve stage: $(ls "$STAGE_DIR"/*.pdf 2>/dev/null | wc -l | tr -d ' ') PDF, $(ls "$STAGE_DIR"/*.epub 2>/dev/null | wc -l | tr -d ' ') EPUB, $(du -sh "$STAGE_DIR" 2>/dev/null | cut -f1)"
echo "Volno na disku: $(df -h / | awk 'NR==2{print $4}')"
