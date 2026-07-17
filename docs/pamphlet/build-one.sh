#!/bin/bash
# Postaví pamflet (PDF + EPUB) v JEDNOM jazyce. Volá se z build-all.sh, ale jde
# pustit i samostatně:  ./build-one.sh de
#
# Každý jazyk má vlastní out/<lang> i build/<lang>, takže víc instancí může běžet
# souběžně bez kolize. Render, tectonic i pandoc jsou jednovláknové — jeden jazyk
# vytíží jedno jádro, proto se paralelizuje po jazycích, ne uvnitř.
set -uo pipefail

lang="${1:-}"
[ -n "$lang" ] || { echo "použití: build-one.sh <lang>"; exit 2; }
# Skript dělá `rm -rf "$BOXTOOL/out/$lang"` — bez validace by `build-one.sh ..`
# smazal celý boxtool. Povol jen tvar kódu kultury (de, pt-br, es-419, zh-cn).
echo "$lang" | grep -qE '^[a-z]{2}(-[a-z0-9]+)?$' || { echo "CHYBA: neplatný kód jazyka: $lang"; exit 2; }

BOXTOOL="${BOXTOOL:-$HOME/Downloads/personix-boxtool}"
PAMPHLET="$(cd "$(dirname "$0")" && pwd)"
STAGE_DIR="${STAGE_DIR:-$HOME/Downloads/personix-pamflety}"
PY="$BOXTOOL/venv/bin/python"
LOG="/tmp/pamphlet-$lang.log"

mkdir -p "$STAGE_DIR"
cd "$BOXTOOL" || exit 1

{
    echo "=== $lang: check ==="
    "$PY" check.py "$lang"    || { echo "SELHAL: check.py"; exit 1; }
    echo "=== $lang: render ==="
    "$PY" render.py "$lang"   || { echo "SELHAL: render.py"; exit 1; }
    echo "=== $lang: expand ==="
    "$PY" expand.py "$lang"   || { echo "SELHAL: expand.py"; exit 1; }
} >>"$LOG" 2>&1 || { echo "[$lang] SELHAL: příprava obrázků — log $LOG"; rm -rf "$BOXTOOL/out/$lang"; exit 1; }

cd "$PAMPHLET/$lang/build" || { echo "[$lang] SELHAL: chybí adresář"; exit 1; }

if ! INFOGRAPHICS_DIR="$BOXTOOL/out/$lang" ./build.sh >>"$LOG" 2>&1; then
    echo "[$lang] SELHAL: build.sh — log $LOG"
    rm -rf "$BOXTOOL/out/$lang"
    exit 1
fi

pdf="pamphlet-v6-$lang.pdf"
if [ ! -f "$pdf" ]; then
    echo "[$lang] SELHAL: build prošel, ale PDF nikde"
    rm -rf "$BOXTOOL/out/$lang"
    exit 1
fi
cp "$pdf" "$STAGE_DIR/"
pdfsize=$(ls -l "$pdf" | awk '{printf "%.0f MB", $5/1048576}')
pages=$(pdfinfo "$pdf" 2>/dev/null | awk '/^Pages/{print $2}')

epubmsg="EPUB —"
if ./build-epub.sh >>"$LOG" 2>&1 && [ -f "pamphlet-v6-$lang.epub" ]; then
    cp "pamphlet-v6-$lang.epub" "$STAGE_DIR/"
    epubmsg="EPUB $(ls -l "pamphlet-v6-$lang.epub" | awk '{printf "%.0f MB", $5/1048576}')"
else
    echo "[$lang] VAROVÁNÍ: EPUB nevznikl — log $LOG"
fi

# uklidit — vše regenerovatelné, jinak ~200 MB na jazyk navíc
rm -rf "$BOXTOOL/out/$lang"
rm -f "$PAMPHLET/$lang/build/"*.pdf "$PAMPHLET/$lang/build/"*.epub
rm -rf "$PAMPHLET/$lang/build/figures"

echo "[$lang] OK — PDF $pdfsize, $pages stran, $epubmsg"
