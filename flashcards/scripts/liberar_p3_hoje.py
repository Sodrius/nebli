#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""liberar_p3_hoje.py -- boost temporario para estudar P3 hoje.

Regime canonico:
  - NEBLI (topo) fica em 15 novos/dia para retencao longa.
  - NEBLI::UC02::P3 ganha 150 novos/dia hoje para cram da prova.

O script nao mexe no AnKing original. Ele cria um preset separado para P3,
porque o topo NEBLI fica em 15 novos/dia. Se P3 compartilhar o mesmo preset do
topo, aumentar P3 tambem aumenta o geral, ou restaurar o geral derruba P3.
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
BASE_DECK = "NEBLI"
P3_DECK = "NEBLI::UC02::P3"
P3_CONFIG_NAME = "NEBLI P3 hoje"


def inv(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKI, payload, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    if data.get("error"):
        raise RuntimeError(f"{action}: {data['error']}")
    return data["result"]


def set_limits(deck, new, rev):
    inv("createDeck", deck=deck)
    cfg = inv("getDeckConfig", deck=deck)
    before = (cfg.get("new", {}).get("perDay"), cfg.get("rev", {}).get("perDay"))
    cfg["new"]["perDay"] = new
    cfg["rev"]["perDay"] = rev
    inv("saveDeckConfig", config=cfg)
    after = (new, rev)
    print(f"{deck}: new/rev {before} -> {after} | preset={cfg.get('name', '?')}")


def ensure_separate_p3_config():
    base_cfg = inv("getDeckConfig", deck=BASE_DECK)
    p3_cfg = inv("getDeckConfig", deck=P3_DECK)
    if p3_cfg.get("name") == P3_CONFIG_NAME:
        return p3_cfg.get("id")

    configs = inv("getDeckConfigs")
    config_id = None
    for cfg in configs:
        if cfg.get("name") == P3_CONFIG_NAME:
            config_id = cfg.get("id")
            break
    if config_id is None:
        config_id = inv("cloneDeckConfigId", cloneFrom=base_cfg["id"], name=P3_CONFIG_NAME)

    inv("setDeckConfigId", decks=[P3_DECK], configId=config_id)
    return config_id


def count(query):
    return len(inv("findCards", query=query))


def main():
    parser = argparse.ArgumentParser(description="LEGADO: prefira planejar_modo_prova.py")
    parser.add_argument("--apply", action="store_true", help="confirma o boost legado de 150 novos")
    args = parser.parse_args()
    try:
        inv("version")
    except Exception as e:
        print("AnkiConnect fora do ar. Abra o Anki com o add-on 2055492159 e rode de novo.")
        print(f"Detalhe: {e}")
        return 3

    p3_total = count(f'deck:"{P3_DECK}"')
    p3_new_active = count(f'deck:"{P3_DECK}" is:new -is:suspended')
    p3_active = count(f'deck:"{P3_DECK}" -is:suspended')
    print(f"P3 agora: {p3_total} cards totais | {p3_active} ativos | {p3_new_active} novos ativos")

    if not args.apply:
        print("[PREVIEW] nada alterado. Para cram, prefira planejar_modo_prova.py.")
        print("Use --apply apenas se quiser conscientemente aprender 150 novos no FSRS.")
        return 0

    if p3_new_active < 150:
        print("AVISO: ha menos de 150 cards novos ativos em P3; o limite fica 150, mas o Anki so mostra o que existir.")

    ensure_separate_p3_config()
    set_limits(P3_DECK, 150, 9999)
    set_limits(BASE_DECK, 15, 9999)
    inv("sync")
    print("OK: P3 liberado para 150 novos hoje; NEBLI mantido em 15 novos/dia. Sync disparado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
