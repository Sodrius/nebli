#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""set_novos_dia.py -- ajusta novos/dia (e opcional revisoes/dia) do AnKing Step Deck via AnkiConnect e sincroniza.

Uso:
    python flashcards/scripts/set_novos_dia.py 25          # novos/dia=25
    python flashcards/scripts/set_novos_dia.py 150 --rev 150
    python flashcards/scripts/set_novos_dia.py 25 --no-sync

Serve pro regime do Davi: amanha 150 (catch-up P4), depois 25/dia com teto ~150/dia.
O flip 150->25 e agendado via Task Scheduler chamando este script com 25.
"""
import json, sys, argparse, urllib.request

ANKI = "http://localhost:8765"
DECK = "AnKing Step Deck"


def inv(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    with urllib.request.urlopen(urllib.request.Request(ANKI, payload), timeout=60) as r:
        d = json.load(r)
    if d.get("error"):
        raise RuntimeError(f"{action}: {d['error']}")
    return d["result"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("novos", type=int, help="novos/dia")
    ap.add_argument("--rev", type=int, default=None, help="revisoes/dia (max reviews)")
    ap.add_argument("--no-sync", action="store_true")
    a = ap.parse_args()
    cfg = inv("getDeckConfig", deck=DECK)
    antes_new = cfg["new"]["perDay"]
    antes_rev = cfg["rev"]["perDay"]
    cfg["new"]["perDay"] = a.novos
    if a.rev is not None:
        cfg["rev"]["perDay"] = a.rev
    inv("saveDeckConfig", config=cfg)
    print(f"novos/dia: {antes_new} -> {a.novos}" + (f" | rev/dia: {antes_rev} -> {a.rev}" if a.rev is not None else ""))
    if not a.no_sync:
        inv("sync")
        print("sync OK")


if __name__ == "__main__":
    main()
