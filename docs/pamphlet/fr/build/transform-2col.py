#!/usr/bin/env python3
"""Transform per-chapter .tex for the two-column print build.

Wraps running text in \\begin{multicols}{2} … \\end{multicols}, but pulls
"full-width" blocks OUT of the columns so they span the whole page:
  * callout boxes        \\begin{cb...box} … \\end{cb...box}
  * long tables          \\begin{longtable} … \\end{longtable}
  * full-page figures    \\fullpagefigure{...} / \\fullpagefigureimmediate{...}

This keeps body text in balanced columns (multicol balances), while callouts /
tables / figures break the columns and run full width — the magazine layout
Pavel asked for. Oversized callouts may still split across pages; that is
handled by the LaTeX side (nobreak=false + continues/continued markers).

Usage: transform-2col.py <srcdir> <dstdir>
"""
import os, re, sys, glob

CALLOUT_BEGIN = re.compile(r'\\begin\{(cb\w+box)\}')
LT_BEGIN      = re.compile(r'\\begin\{longtable\}')
LT_END        = re.compile(r'\\end\{longtable\}')
LTCAP         = re.compile(r'\\def\\LTcaptype')  # pandoc wraps longtable in {\def\LTcaptype{none} … }
FIG           = re.compile(r'\\fullpagefigure(?:immediate)?\b')

OPEN  = r'\begin{multicols}{2}'
CLOSE = r'\end{multicols}'


def segment(lines):
    """Split into (kind, block_lines) where kind is 'text' or 'fw'."""
    segs, text = [], []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        mcb = CALLOUT_BEGIN.search(line)
        if mcb:
            if text:
                segs.append(('text', text)); text = []
            env = mcb.group(1)
            end = re.compile(r'\\end\{' + re.escape(env) + r'\}')
            block = [line]; i += 1
            while i < n:
                block.append(lines[i])
                if end.search(lines[i]):
                    i += 1; break
                i += 1
            segs.append(('fw', block)); continue
        if LTCAP.search(line) or LT_BEGIN.search(line):
            if text:
                segs.append(('text', text)); text = []
            started_cap = bool(LTCAP.search(line))
            block = [line]; i += 1
            while i < n and not LT_END.search(lines[i]):
                block.append(lines[i]); i += 1
            if i < n:                       # the \end{longtable} line
                block.append(lines[i]); i += 1
            if started_cap:                 # absorb the closing } of the captype group
                while i < n and lines[i].strip() == '':
                    block.append(lines[i]); i += 1
                if i < n and lines[i].strip() == '}':
                    block.append(lines[i]); i += 1
            segs.append(('fw', block)); continue
        if FIG.search(line):
            if text:
                segs.append(('text', text)); text = []
            segs.append(('fw', [line])); i += 1; continue
        text.append(line); i += 1
    if text:
        segs.append(('text', text))
    return segs


def transform(src):
    segs = segment(src.split('\n'))
    out = []
    for kind, block in segs:
        if kind == 'text' and ''.join(block).strip():
            out.append(OPEN)
            out.extend(block)
            out.append(CLOSE)
        else:
            # whitespace-only text or a full-width block — emit bare
            out.extend(block)
    return '\n'.join(out)


def main():
    srcdir, dstdir = sys.argv[1], sys.argv[2]
    os.makedirs(dstdir, exist_ok=True)
    for path in sorted(glob.glob(os.path.join(srcdir, '*.tex'))):
        name = os.path.basename(path)
        with open(path, encoding='utf-8') as f:
            src = f.read()
        # glossary stays single-column (master \inputs chapters/glossary.tex)
        out = src if name == 'glossary.tex' else transform(src)
        with open(os.path.join(dstdir, name), 'w', encoding='utf-8') as f:
            f.write(out)
    print(f'transformed {len(glob.glob(os.path.join(srcdir, "*.tex")))} files → {dstdir}')


if __name__ == '__main__':
    main()
