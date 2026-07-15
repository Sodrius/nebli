#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""set_novos_dia.py -- ajusta novos/dia de um deck via AnkiConnect e sincroniza.

Uso:
    python flashcards/scripts/set_novos_dia.py 15
    python flashcards/scripts/set_novos_dia.py 15 --apply
    python flashcards/scripts/set_novos_dia.py 15 --no-sync

Serve pro regime do Davi: NEBLI = 15 novos/dia permanente. Para cram, preferir
`planejar_modo_prova.py`. Sem --apply este script e somente leitura.
"""
import argparse
import json
import sys
import urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ANKI = "http://localhost:8765"
DEFAULT_DECK = "NEBLI"


def inv(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    with urllib.request.urlopen(urllib.request.Request(ANKI, payload), timeout=60) as r:
        d = json.load(r)
    if d.get("error"):
        raise RuntimeError(f"{action}: {d['error']}")
    return d["result"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("novos", type=int, help="novos/dia")
    ap.add_argument("--deck", default=DEFAULT_DECK, help='deck alvo (default: "NEBLI")')
    ap.add_argument("--rev", type=int, default=None, help="revisoes/dia (max reviews)")
    ap.add_argument("--no-sync", action="store_true")
    ap.add_argument("--apply", action="store_true", help="confirma a gravacao no Anki")
    a = ap.parse_args()
    cfg = inv("getDeckConfig", deck=a.deck)
    antes_new = cfg["new"]["perDay"]
    antes_rev = cfg["rev"]["perDay"]
    depois_rev = a.rev if a.rev is not None else antes_rev
    print(f"deck: {a.deck} | novos/dia: {antes_new} -> {a.novos} | rev/dia: {antes_rev} -> {depois_rev}")
    if not a.apply:
        print("[DRY-RUN] nada gravado. Use --apply para confirmar.")
        return
    cfg["new"]["perDay"] = a.novos
    if a.rev is not None:
        cfg["rev"]["perDay"] = a.rev
    inv("saveDeckConfig", config=cfg)
    if not a.no_sync:
        inv("sync")
        print("sync OK")


if __name__ == "__main__":
    main()
