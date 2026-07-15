#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Restaura o subdeck P3 para o ritmo normal depois do cram."""
import argparse
import json
import sys
import urllib.request

ANKI = "http://localhost:8765"
P3_DECK = "NEBLI::UC02::P3"


def inv(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKI, payload, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    if data.get("error"):
        raise RuntimeError(f"{action}: {data['error']}")
    return data["result"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="confirma a restauracao")
    args = parser.parse_args()
    cfg = inv("getDeckConfig", deck=P3_DECK)
    before = (cfg["new"]["perDay"], cfg["rev"]["perDay"], cfg.get("name", "?"))
    if not args.apply:
        print(f"[PREVIEW] {P3_DECK}: {before} -> (15, 9999). Nada alterado.")
        return
    cfg["new"]["perDay"] = 15
    cfg["rev"]["perDay"] = 9999
    inv("saveDeckConfig", config=cfg)
    inv("sync")
    print(f"{P3_DECK}: {before} -> (15, 9999, {cfg.get('name', '?')})")


if __name__ == "__main__":
    sys.exit(main())
