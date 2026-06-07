#!/usr/bin/env bash
# Build pamphlet-v6-cz.pdf — landscape A5 ebook from Czech markdown sources.
# Mirrors docs/pamphlet/en/build/build.sh — CZ adjustments:
#   * sources: ../<cz-chapter-dir>/<cz-name>.md
#   * graphics: pre-built PNGs in figures/; optional regen from external
#     Info Graphics/v5-cz/ via INFOGRAPHICS_DIR env var (defaults to the
#     new-world-order checkout if it exists).
#   * strip_top_section: Czech chapter titles
#   * pamphlet.tex: Czech metadata, babel czech, Czech chapter names
#
# Idempotent.
#
# Usage:
#   ./build.sh                                      # finální PDF
#   ./build.sh --clean                              # vyčistit intermediates
#   ./build.sh --watermark                          # PRACOVNÍ VERZE PDF
#                                                   # výstup: pamphlet-v6-cz-DRAFT.pdf
#   ./build.sh --watermark-text "K REVIZI"          # vlastní text razítka
#   ./build.sh --watermark --watermark-banner "..." # vlastní banner v záhlaví/patičce

set -euo pipefail

BUILD_DIR="$(cd "$(dirname "$0")" && pwd)"
PAMPHLET_DIR="$(cd "$BUILD_DIR/.." && pwd)"
REPO_ROOT="$(cd "$PAMPHLET_DIR/../.." && pwd)"
# v6: Info Graphics live outside personix repo. Allow override via env var,
# otherwise probe the historical new-world-order checkout.
: "${INFOGRAPHICS_DIR:=$HOME/RiderProjects/new-world-order/Prezentace/Info Graphics/v5-cz}"
if [ -d "$INFOGRAPHICS_DIR" ]; then
  GFX_DIR="$(cd "$INFOGRAPHICS_DIR" && pwd)"
else
  echo "NOTE: INFOGRAPHICS_DIR not found ($INFOGRAPHICS_DIR) — will use pre-built PNGs in figures/."
  GFX_DIR=""
fi

cd "$BUILD_DIR"

# ----- 0. Argument parsing -----
CLEAN=0
WATERMARK=0
PRINT=0
WATERMARK_TEXT="PRACOVNÍ VERZE — NEŠÍŘIT"
WATERMARK_BANNER="Před redakční úpravou"
while [ $# -gt 0 ]; do
  case "$1" in
    --clean) CLEAN=1 ;;
    --watermark) WATERMARK=1 ;;
    --watermark=*) WATERMARK=1; WATERMARK_TEXT="${1#*=}" ;;
    --watermark-text) shift; WATERMARK_TEXT="$1"; WATERMARK=1 ;;
    --watermark-banner) shift; WATERMARK_BANNER="$1"; WATERMARK=1 ;;
    --print) PRINT=1 ;;   # tisková varianta → pamphlet-v6-cz-interior.pdf
    -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
    *) echo "ERROR: unknown argument '$1'"; exit 1 ;;
  esac
  shift
done

# ----- 1. Tooling check -----
need() { command -v "$1" >/dev/null 2>&1 || { echo "ERROR: '$1' is not on PATH"; MISSING=1; }; }
MISSING=0
need dwebp
need pandoc
need tectonic
need sips      # macOS built-in
need pngquant  # brew install pngquant
if [ "$MISSING" -ne 0 ]; then
  cat <<EOF

To install missing tools on macOS:
  brew install webp pandoc tectonic pngquant

EOF
  exit 1
fi

# ----- 2. Optional clean -----
if [ "$CLEAN" = "1" ]; then
  rm -rf chapters figures *.pdf *.aux *.toc *.out *.log *.fls *.fdb_latexmk \
         pamphlet-draft.tex watermark.tex
  echo "cleaned."
fi

# ----- 3. Make subfolders if missing -----
mkdir -p chapters figures frontmatter backmatter

# ----- 4. WebP → PNG → resize → pngquant -----
# PRINT: full resolution, no downscale / no lossy pngquant (300 DPI for the
# printer). SCREEN: 1800 px + pngquant (small ebook). Print regenerates figures/
# from scratch so a previous screen build's downscaled PNGs aren't reused.
if [ "$PRINT" = "1" ]; then
  echo "[1/5] webp -> png (PLNÉ rozlišení pro tisk, bez resize/pngquant)"
  rm -f figures/v5-*.png
else
  echo "[1/5] webp -> png -> resize -> pngquant"
fi
if [ -n "$GFX_DIR" ]; then
  for f in "$GFX_DIR"/v5-*.webp; do
    [ -f "$f" ] || continue
    base=$(basename "$f" .webp)
    case "$base" in
      v5-cover-prebal*) continue;;  # portrait covers excluded (no landscape variant needed)
    esac
    # Prefer composite from v5-cz/expanded/ (CZ centre overlaid on EN expanded edges)
    src="$f"
    if [ -f "$GFX_DIR/expanded/$base.webp" ]; then
      src="$GFX_DIR/expanded/$base.webp"
    fi
    out="figures/${base}.png"
    if [ ! -f "$out" ] || [ "$src" -nt "$out" ]; then
      dwebp -quiet "$src" -o "$out"
      if [ "$PRINT" != "1" ]; then
        sips -Z 1800 --setProperty formatOptions normal "$out" >/dev/null 2>&1 || true
        pngquant --skip-if-larger --quality=65-85 --speed=3 --strip --force --output "$out" "$out" 2>/dev/null || true
      fi
    fi
  done
  # Cover landscape: pull from v5-cz directly (composite picks up automatically)
  for cand in "$GFX_DIR/v5-cover-landscape.webp" "$GFX_DIR/v5-cover-landscape.png"; do
    if [ -f "$cand" ]; then
      out="figures/v5-cover-landscape.png"
      if [ "${cand##*.}" = "webp" ]; then
        [ ! -f "$out" ] || [ "$cand" -nt "$out" ] && dwebp -quiet "$cand" -o "$out"
      else
        cp -f "$cand" "$out"
      fi
    fi
  done
fi
# Donation QR codes (Bitcoin on-chain + Lightning) — sourced from branding/figures
# (the public repo carries the WebP masters; src/Web lives only in personix-web).
QR_DIR="$REPO_ROOT/branding/figures"
if [ -d "$QR_DIR" ]; then
  for qr in bitcoin-onchain-qr bitcoin-lightning-qr; do
    src="$QR_DIR/${qr}.webp"
    out="figures/${qr}.png"
    if [ -f "$src" ] && { [ ! -f "$out" ] || [ "$src" -nt "$out" ]; }; then
      dwebp -quiet "$src" -o "$out"
    fi
  done
fi

# ----- 5. Pandoc MD → TeX (per source file) -----
echo "[2/5] pandoc md -> tex"

# v6: 08-sleduj-penize/03-prechod/ je rozbitá do komponent.
# Před pandoc-em je smergujeme do jednoho .merged.md (H1→H2 shift,
# strip frontmatter, prepend "Navrhovaný přechod" section header).
PRECHOD_DIR="$PAMPHLET_DIR/08-sleduj-penize/03-prechod"
PRECHOD_MERGED="$PRECHOD_DIR/.merged.md"
needs_merge=0
[ ! -f "$PRECHOD_MERGED" ] && needs_merge=1
if [ "$needs_merge" = "0" ]; then
  for f in "$PRECHOD_DIR"/[0-9]*.md; do
    [ "$f" -nt "$PRECHOD_MERGED" ] && needs_merge=1 && break
  done
fi
if [ "$needs_merge" = "1" ]; then
  {
    echo "# Navrhovaný přechod k nástupci státu"
    echo ""
    for f in "$PRECHOD_DIR"/[0-9]*.md; do
      awk '/^---$/{c++; next} c<2{next} {print}' "$f" | sed 's/^# /## /'
      echo ""
    done
  } > "$PRECHOD_MERGED"
fi

# v6: 04-overovani/02-role-a-autority/ je rozbitá do komponent.
# Před pandoc-em je smergujeme do jednoho .merged.md (H1→H2 shift,
# strip frontmatter, prepend "Role v ověřovací transakci a autority" section header).
# Komponenty jsou očíslované 01–08 podle pořadí v textu — glob je seřadí správně.
ROLE_DIR="$PAMPHLET_DIR/04-overovani/02-role-a-autority"
ROLE_MERGED="$ROLE_DIR/.merged.md"
role_needs_merge=0
[ ! -f "$ROLE_MERGED" ] && role_needs_merge=1
if [ "$role_needs_merge" = "0" ]; then
  for f in "$ROLE_DIR"/[0-9]*.md; do
    [ "$f" -nt "$ROLE_MERGED" ] && role_needs_merge=1 && break
  done
fi
if [ "$role_needs_merge" = "1" ]; then
  {
    echo "# Role v ověřovací transakci a autority"
    echo ""
    for f in "$ROLE_DIR"/[0-9]*.md; do
      awk '/^---$/{c++; next} c<2{next} {print}' "$f" | sed 's/^# /## /'
      echo ""
    done
  } > "$ROLE_MERGED"
fi

P() {
  local src="$1" dst="$BUILD_DIR/chapters/$2"
  if [ ! -f "$dst" ] || [ "$src" -nt "$dst" ]; then
    pandoc --top-level-division=section -t latex --wrap=preserve -o "$dst" "$src"
    NEW_TEX="$NEW_TEX $dst"
  fi
}
NEW_TEX=""
cd "$PAMPHLET_DIR"
P 01-uvod/01-uvod.md                        intro-a-v4.tex
P 02-predpoklady/01-predpoklady.md          prereq-01.tex
P 03-nastroj/01-sit.md                      tool-01-network.tex
P 03-nastroj/02-necenzurovatelnost.md       tool-02-uncensorability.tex
P 03-nastroj/03-pochybnosti.md              tool-03-doubts.tex
P 03-nastroj/04-dobrovolnost-a-svoboda.md   tool-04-voluntariness.tex
P 03-nastroj/05-prepinac-svoboda-totalita.md tool-05-switch.tex
P 03-nastroj/06-oracle-problem.md           tool-06-oracle.tex
P 04-overovani/01-konsenzus.md              verif-01-consensus.tex
P 04-overovani/02-role-a-autority/.merged.md verif-02-roles.tex
P 04-overovani/03-emergentni-smlouva.md     verif-03-contract.tex
P 04-overovani/05-poskytovani-informaci.md  verif-05-info-sharing.tex
P 07-zlocin-a-trest/01-zlocin-a-trest.md    crime-01.tex
P 08-sleduj-penize/01-sleduj-penize.md      money-01.tex
P 08-sleduj-penize/03-prechod/.merged.md    money-03-transition.tex
P 09-zaver/01-zaver.md                      concl-c-fusion.tex
P 10-rejstrik/rejstrik-pojmu.md             glossary.tex
cd "$BUILD_DIR"

# ----- 6. Post-process new TeX files -----
if [ -n "$NEW_TEX" ]; then
  echo "[3/5] post-process: rewrite figures + drop wikilink residue"
  perl -i -0pe 's{\\begin\{figure\}.*?\\end\{figure\}}{my $b=$&; ($b =~ /(v5-[a-z0-9-]+)\.webp/) ? "\\fullpagefigure{figures/$1.png}" : $b}gse' $NEW_TEX
  perl -i -ne 'print unless /^\s*!\{\[\}\{\[\}v5-[a-z0-9-]+\\#(EN|CS|CZ)\{\]\}\{\]\}\s*$/' $NEW_TEX

  perl -i -0pe '
    s{\\begin\{quote\}\s*\{\[\}\!(note|important|warning|danger|quote|example|idea)\{\]\}\s*([^\n]*?)\n(.*?)\\end\{quote\}}
     {"\\begin{cb$1box}{$2}\n$3\\end{cb$1box}"}gsie;
  ' $NEW_TEX

  # v6: [!bug] callouty jsou Pavlovy scratch poznámky pro reorganizaci — vyhodit z PDF.
  perl -i -0pe '
    s{\\begin\{quote\}\s*\{\[\}\!bug\{\]\}\s*[^\n]*\n.*?\\end\{quote\}\s*}{}gsie;
  ' $NEW_TEX

fi

# 6f) CZ-specific: substitute glyphs absent from Palatino + math-mode artefacts
# from translation. Idempotent.
# Python is used because perl -CSD on macOS was failing to write back the
# substitutions for unicode literals reliably.
echo "[3a/5] CZ glyph substitutions"
python3 - "$BUILD_DIR" <<'PY'
import sys, glob, os, re
build = sys.argv[1]
SUBS = [
    # CZ markdown sometimes contains bare "$" inside arrow descriptions where
    # the author meant "→". Pandoc passes the $ through; LaTeX then reads CZ
    # words around it as math identifiers (cmmi10) and warns about each char.
    ('„$"', '„$\\rightarrow$"'),
    # Unicode arrow → has no glyph in Palatino; use math-mode arrow which the
    # default math font (Latin Modern) renders without complaint.
    ('→',  '$\\rightarrow$'),
    ('↦',  '$\\mapsto$'),
]
for tex in glob.glob(os.path.join(build, 'chapters', '*.tex')):
    with open(tex, 'r', encoding='utf-8') as f:
        src = f.read()
    new = src
    for a, b in SUBS:
        new = new.replace(a, b)
    if new != src:
        with open(tex, 'w', encoding='utf-8') as f:
            f.write(new)
PY

# 6c) Strip top-level \section{<chapter title>} from chapter TeX files
strip_top_section() {
  local tex="$1" rgx="$2"
  if [ -f "$tex" ]; then
    perl -i -ne 'BEGIN{$f=0} print unless m|^\\section\{'"$rgx"'\}\\label\{[^}]+\}\s*$| && !$f++' "$tex"
  fi
}
strip_top_section "$BUILD_DIR/chapters/glossary.tex"   'Rejstřík pojmů'
strip_top_section "$BUILD_DIR/chapters/prereq-01.tex"  'Nezbytné předpoklady změny'
strip_top_section "$BUILD_DIR/chapters/crime-01.tex"   'Zločin a trest'
strip_top_section "$BUILD_DIR/chapters/money-01.tex"   'Sleduj stopu peněz'

# 6c.2) Promote leading \subsection -> \section in money-01.tex
if [ -f "$BUILD_DIR/chapters/money-01.tex" ]; then
  perl -i -pe 's|^\\subsection\{(Dosavadní shrnutí\|Metodika)\}|\\section{$1}|' \
    "$BUILD_DIR/chapters/money-01.tex"
fi

# 6c.3) Insert manual hyphenation breakpoints into long Czech words used in
# the glossary table. Czech babel adds patterns but a few compound terms still
# overflow the narrow longtable column.
if [ -f "$BUILD_DIR/chapters/glossary.tex" ]; then
  perl -i -pe '
    s|\\textbf\{Compartmentalizace\}|\\textbf{Com\\-part\\-men\\-tal\\-i\\-za\\-ce}|g;
    s|\\textbf\{Necenzurovatelnost\}|\\textbf{Ne\\-cen\\-zu\\-ro\\-va\\-tel\\-nost}|g;
    s|\\textbf\{Nezkorumpovatelnost\}|\\textbf{Ne\\-zko\\-rum\\-po\\-va\\-tel\\-nost}|g;
    s|\\textbf\{Decentralizace\}|\\textbf{De\\-cen\\-tra\\-li\\-za\\-ce}|g;
  ' "$BUILD_DIR/chapters/glossary.tex"
fi

# 6c.4) Promote oversized "Nezkorumpovatelnost" callout to splittable variant.
if [ -f "$BUILD_DIR/chapters/prereq-01.tex" ]; then
  perl -i -0pe '
    s|\\begin\{cbimportantbox\}\{Nezkorumpovatelnost\}(.*?)\\end\{cbimportantbox\}|\\begin{cbimportantsplitbox}{Nezkorumpovatelnost}$1\\end{cbimportantsplitbox}|gs;
  ' "$BUILD_DIR/chapters/prereq-01.tex"
fi

# 6e) Drop optional bg-colour args from \fullpagefigure[...]{figures/X.png}.
echo "[3b/5] normalise \\fullpagefigure refs"
python3 - "$BUILD_DIR" <<'PY'
import sys, os, re, glob

build = sys.argv[1]

pat_bg  = re.compile(r'\\fullpagefigure\[[^\]]*\]\{(figures/[^}]+\.png)\}')
pat_exp = re.compile(r'\\fullpagefigure\{figures/expanded/([^}]+\.png)\}')

for tex in glob.glob(os.path.join(build, 'chapters', '*.tex')) + [os.path.join(build, 'pamphlet.tex')]:
    with open(tex, 'r', encoding='utf-8') as f:
        src = f.read()
    new = pat_bg.sub(r'\\fullpagefigure{\1}', src)
    new = pat_exp.sub(r'\\fullpagefigure{figures/\1}', new)
    if new != src:
        with open(tex, 'w', encoding='utf-8') as f:
            f.write(new)
PY

# ----- 7. Compile -----
if [ "$PRINT" = "1" ]; then
  echo "[3c/5] per-figure background colours -> figbg.tex"
  python3 figure-bgcolors.py figures > figbg.tex
  echo "[3d/5] soft-edged (feathered) figures -> figures-bleed/"
  python3 figure-bleed.py figures figures-bleed
  echo "[4/5] tectonic compile (TISKOVÁ varianta — vnitřek knihy)"
  tectonic pamphlet-print.tex
  cp -f pamphlet-print.pdf pamphlet-v6-cz-interior.pdf
  echo "[5/5] done"
  echo
  echo "BUILD OK (tiskový vnitřek): $BUILD_DIR/pamphlet-v6-cz-interior.pdf"
  ls -lh pamphlet-v6-cz-interior.pdf
  pdfinfo pamphlet-v6-cz-interior.pdf 2>/dev/null | grep -E 'Pages|Page size|Title|Author' || true
  PAGES=$(pdfinfo pamphlet-v6-cz-interior.pdf 2>/dev/null | awk '/Pages/{print $2}')
  if [ -n "$PAGES" ]; then
    echo "  → $PAGES stran = $((PAGES/2)) listů (mod 4 = $((PAGES%4)) — musí být 0)"
  fi
elif [ "$WATERMARK" = "1" ]; then
  echo "[4/5] tectonic compile (PRACOVNÍ VERZE watermark mode)"
  python3 - "$BUILD_DIR/watermark.tex.template" "$BUILD_DIR/watermark.tex" \
          "$WATERMARK_TEXT" "$WATERMARK_BANNER" <<'PY'
import sys
src, dst, big, banner = sys.argv[1:5]
with open(src, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('__DRAFT_BIG__', big).replace('__DRAFT_BANNER__', banner)
with open(dst, 'w', encoding='utf-8') as f:
    f.write(text)
PY
  python3 - "$BUILD_DIR/pamphlet.tex" "$BUILD_DIR/pamphlet-draft.tex" <<'PY'
import sys
src, dst = sys.argv[1:3]
with open(src, 'r', encoding='utf-8') as f:
    text = f.read()
inject = '% --- Watermark (injected by build.sh --watermark) ---\n' \
         '\\input{watermark.tex}\n'
needle = '\\begin{document}'
if needle not in text:
    raise SystemExit("pamphlet.tex: \\begin{document} not found")
text = text.replace(needle, inject + needle, 1)
with open(dst, 'w', encoding='utf-8') as f:
    f.write(text)
PY
  tectonic pamphlet-draft.tex
  cp -f pamphlet-draft.pdf pamphlet-v6-cz-DRAFT.pdf
  echo "[5/5] done"
  echo
  echo "BUILD OK (s razítkem): $BUILD_DIR/pamphlet-v6-cz-DRAFT.pdf"
  ls -lh pamphlet-v6-cz-DRAFT.pdf
  pdfinfo pamphlet-v6-cz-DRAFT.pdf 2>/dev/null | grep -E 'Pages|Page size|Title|Author' || true
else
  echo "[4/5] tectonic compile"
  tectonic pamphlet.tex
  cp -f pamphlet.pdf pamphlet-v6-cz.pdf
  echo "[5/5] done"
  echo
  echo "BUILD OK: $BUILD_DIR/pamphlet-v6-cz.pdf"
  ls -lh pamphlet-v6-cz.pdf
  pdfinfo pamphlet-v6-cz.pdf 2>/dev/null | grep -E 'Pages|Page size|Title|Author' || true
fi
