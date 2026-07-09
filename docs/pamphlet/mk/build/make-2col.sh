#!/usr/bin/env bash
# Build the EXPERIMENTAL two-column print PDF.
#   1. refresh chapters/ + figures/ from markdown (via build.sh --print)
#   2. transform chapters/ → chapters2col/ (multicol + full-width blocks)
#   3. compile pamphlet-print-2col.tex
# Output: pamphlet-v6-en-print-2col.pdf  (not a committed deliverable)
set -euo pipefail
cd "$(dirname "$0")"

echo "[1/3] refresh chapters + figures (build.sh --print)"
./build.sh --print >/dev/null

echo "[2/3] transform chapters -> chapters2col (multicol + full-width)"
rm -rf chapters2col
python3 transform-2col.py chapters chapters2col

echo "[3/3] tectonic compile (2col)"
tectonic pamphlet-print-2col.tex
cp -f pamphlet-print-2col.pdf pamphlet-v6-en-print-2col.pdf

echo
echo "DONE: $(pwd)/pamphlet-v6-en-print-2col.pdf"
pdfinfo pamphlet-v6-en-print-2col.pdf 2>/dev/null | grep -E 'Pages|Page size' || true
