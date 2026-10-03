"""Převod Obsidian calloutů (> [!typ] Titulek) na pandoc fenced divy pro EPUB.

Výstup `::::: {.callout .typ}` s volitelným `.callout-title` dostane od pandocu
třídy, na které míří styly v style.css. Callouty typu `bug` jsou autorovy
pracovní poznámky a do knihy nepatří.
"""
import re
import sys

HEAD = re.compile(r'^>\s*\[!([A-Za-z]+)\][+-]?[ \t]*(.*)$')
DROPPED = {'bug'}


def _strip_quote(line):
    return re.sub(r'^> ?', '', line)


def convert(text):
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        m = HEAD.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        kind, title = m.group(1).lower(), m.group(2).strip()
        j = i + 1
        while j < len(lines) and lines[j].startswith('>'):
            j += 1
        body = [_strip_quote(l) for l in lines[i + 1:j]]
        i = j
        if kind in DROPPED:
            continue
        out.append('')
        out.append(f'::::: {{.callout .{kind}}}')
        if title:
            out += [':::: {.callout-title}', title, '::::', '']
        out += body
        out += [':::::', '']
    return '\n'.join(out)


if __name__ == '__main__':
    sys.stdout.write(convert(sys.stdin.read()))
