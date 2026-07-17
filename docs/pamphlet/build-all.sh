#!/bin/bash
# Postaví pamflet (PDF + EPUB) ve všech jazycích, které mají lokalizované infografiky.
#
# Paralelně: render, tectonic i pandoc jsou jednovláknové, takže jeden jazyk vytíží
# jedno jádro a zbytek stroje se válí. Jazyky jsou na sobě nezávislé (vlastní
# out/<lang> i build/<lang>), takže se pouští po dávkách — viz JOBS.
#
# Hotové soubory jdou do STAGE_DIR mimo git: veřejné repo personix je schválně
# malé (181 MB) a 46 jazyků × ~70 MB by ho nafouklo přes 3 GB, navíc při každém
# přesázení znovu — historie se v gitu nikdy nezmenšuje. Na server se odsud
# posílá zvlášť (deploy/sync-pamphlets.sh v personix-web).
#
# Použití:
#   ./build-all.sh                 # všechny jazyky, co ještě nejsou ve stage
#   ./build-all.sh de fr ja        # jen vyjmenované (staví se vždy, i hotové)
#   JOBS=8 ./build-all.sh          # jiný počet souběžných jazyků
#   FORCE=1 ./build-all.sh         # přestavět i to, co už ve stage je
set -uo pipefail

BOXTOOL="${BOXTOOL:-$HOME/Downloads/personix-boxtool}"
PAMPHLET="$(cd "$(dirname "$0")" && pwd)"
STAGE_DIR="${STAGE_DIR:-$HOME/Downloads/personix-pamflety}"
PY="$BOXTOOL/venv/bin/python"

# Necháváme pár jader systému — plné obsazení jen zpomalí všechno ostatní.
JOBS="${JOBS:-$(( $(sysctl -n hw.ncpu 2>/dev/null || echo 4) - 5 ))}"
[ "$JOBS" -lt 1 ] && JOBS=1

[ -x "$PY" ] || { echo "CHYBA: chybí $PY — boxtool venv"; exit 1; }
[ -x "$PAMPHLET/build-one.sh" ] || { echo "CHYBA: chybí build-one.sh"; exit 1; }
command -v pandoc >/dev/null || { echo "CHYBA: chybí pandoc (EPUB)"; exit 1; }
mkdir -p "$STAGE_DIR"

if [ $# -gt 0 ]; then
    LANGS=("$@")
else
    LANGS=()
    while IFS= read -r f; do
        l=$(basename "$f" .json)
        # jen jazyky, které mají i zdrojové MD pamfletu
        [ -d "$PAMPHLET/$l/build" ] || continue
        # hotové přeskoč, ať se dvouhodinová práce neopakuje
        if [ -z "${FORCE:-}" ] && [ -f "$STAGE_DIR/pamphlet-v6-$l.pdf" ] && [ -f "$STAGE_DIR/pamphlet-v6-$l.epub" ]; then
            continue
        fi
        LANGS+=("$l")
    done < <(find "$BOXTOOL/trans" -maxdepth 1 -name '*.json' | sort)
fi

if [ ${#LANGS[@]} -eq 0 ]; then
    echo "Není co stavět — vše už je ve $STAGE_DIR (FORCE=1 přestaví)."
    exit 0
fi

echo "Jazyků k sestavení: ${#LANGS[@]}  (souběžně: $JOBS)"
echo "Cíl: $STAGE_DIR"
echo "Volno na disku: $(df -h / | awk 'NR==2{print $4}')"
# Na baterii macOS strká výpočet na úsporná jádra — sazba pak trvá 30 min místo 5.
pmset -g batt 2>/dev/null | head -1
echo

started=$(date +%s)
printf '%s\n' "${LANGS[@]}" | xargs -P "$JOBS" -I{} "$PAMPHLET/build-one.sh" {}
elapsed=$(( ($(date +%s) - started) / 60 ))

echo
echo "════════════════════════════════════════"
pdfs=$(ls "$STAGE_DIR"/pamphlet-v6-*.pdf 2>/dev/null | wc -l | tr -d ' ')
epubs=$(ls "$STAGE_DIR"/pamphlet-v6-*.epub 2>/dev/null | wc -l | tr -d ' ')
echo "HOTOVO za ${elapsed} min"
echo "Ve stage: $pdfs PDF, $epubs EPUB, $(du -sh "$STAGE_DIR" 2>/dev/null | cut -f1)"

# Co chybí — ať se na tichý výpadek nepřijde až na webu
missing=()
for l in "${LANGS[@]}"; do
    [ -f "$STAGE_DIR/pamphlet-v6-$l.pdf" ] || missing+=("$l:pdf")
    [ -f "$STAGE_DIR/pamphlet-v6-$l.epub" ] || missing+=("$l:epub")
done
if [ ${#missing[@]} -gt 0 ]; then
    echo "CHYBÍ (${#missing[@]}): ${missing[*]}"
    echo "Logy: /tmp/pamphlet-<lang>.log"
else
    echo "Všechny požadované jazyky mají PDF i EPUB."
fi
echo "Volno na disku: $(df -h / | awk 'NR==2{print $4}')"
