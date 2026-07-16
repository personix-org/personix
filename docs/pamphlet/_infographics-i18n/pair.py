#!/usr/bin/env python3
"""Spáruj list překladů (trans_raw/{lang}.json) s EN originály (all_texts.json) → trans/{lang}.json.
Párování podle POŘADÍ (agent nemění klíče, jen dodá hodnoty ve stejném sledu) — neprůstřelné.
Použití: ./venv/bin/python pair.py <lang> [<lang> ...]
"""
import sys, os, json
BK = os.path.dirname(os.path.abspath(__file__))
en = json.load(open(f"{BK}/all_texts.json"))
for lang in sys.argv[1:]:
    rf = f"{BK}/trans_raw/{lang}.json"
    if not os.path.exists(rf):
        print(f"[{lang}] chybí trans_raw/{lang}.json"); continue
    raw = json.load(open(rf))
    if len(raw) != len(en):
        print(f"[{lang}] NEÚPLNÉ: {len(raw)}/{len(en)} — dopřeložit zbytek (od indexu {len(raw)})"); continue
    d = {en[i]: raw[i] for i in range(len(en))}
    json.dump(d, open(f"{BK}/trans/{lang}.json", "w"), ensure_ascii=False, indent=1)
    print(f"[{lang}] spárováno {len(d)} → trans/{lang}.json")
