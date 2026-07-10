#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""configurar_ritmo_anking.py -- fixa o ritmo do deck AnKing (novos/dia, revisoes/dia).

O ritmo NAO e alavanca de curadoria: nao importa quantos cards cada aula
dessuspende, quem controla quantos AFLORAM por dia e o deck config do Anki.
Dessuspender 40 cards/aula sem isso inunda a fila de novos. Este script seta,
via AnkiConnect, o grupo de opcoes do deck AnKing para:

    new.perDay = 25    (introducao: 25 cards novos por dia -- alvo do Davi)
    rev.perDay = 150   (teto de revisao: permite chegar a 150 revisoes/dia)

Nota: os 25 sao INTRODUCAO; as 150 revisoes se preenchem conforme os blocos
NEBLI:: se acumulam ao longo dos dias (backlog de cards maturando). No dia 1 o
deck ainda nao tem 150 pra revisar -- o teto so libera o topo.

Uso:
    python flashcards/scripts/configurar_ritmo_anking.py --dry-run
    python flashcards/scripts/configurar_ritmo_anking.py
    python flashcards/scripts/configurar_ritmo_anking.py --deck "AnKing Step Deck" --new 25 --rev 150
"""
import argparse
import json
import sys
import urllib.request
import urllib.error

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ANKICONNECT = "http://localhost:8765"


def _invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload)
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]


def _anki_vivo():
    try:
        _invoke("version")
        return True
    except (urllib.error.URLError, OSError, RuntimeError):
        return False


def achar_deck(preferido=None):
    """Nome do deck AnKing na colecao. Usa o preferido se existir, senao o
    primeiro que contenha 'anking' (case-insensitive)."""
    nomes = _invoke("deckNames")
    if preferido and preferido in nomes:
        return preferido
    for n in nomes:
        if "anking" in n.lower():
            return n
    return None


def main():
    ap = argparse.ArgumentParser(description="Fixa novos/dia e revisoes/dia do deck AnKing.")
    ap.add_argument("--deck", help="nome do deck (default: auto-detecta 'AnKing')")
    ap.add_argument("--new", type=int, default=25, help="cards novos por dia (default 25)")
    ap.add_argument("--rev", type=int, default=150, help="teto de revisoes por dia (default 150)")
    ap.add_argument("--dry-run", action="store_true", help="mostra atual e proposto, nao grava")
    args = ap.parse_args()

    if not _anki_vivo():
        print("AnkiConnect fora do ar (Anki fechado ou add-on 2055492159 ausente).")
        print(f"Config manual: no deck AnKing, engrenagem > Options > "
              f"New cards/day = {args.new}, Maximum reviews/day = {args.rev}.")
        return 3

    deck = achar_deck(args.deck)
    if not deck:
        print("ERRO: nao achei um deck com 'AnKing' no nome. Passe --deck \"<nome>\".", file=sys.stderr)
        print("  decks:", ", ".join(_invoke("deckNames")), file=sys.stderr)
        return 2

    cfg = _invoke("getDeckConfig", deck=deck)
    atual_new = cfg.get("new", {}).get("perDay")
    atual_rev = cfg.get("rev", {}).get("perDay")
    print(f"Deck: {deck}  (grupo de opcoes: {cfg.get('name', '?')})")
    print(f"  novos/dia:     {atual_new}  ->  {args.new}")
    print(f"  revisoes/dia:  {atual_rev}  ->  {args.rev}")

    if args.dry_run:
        print("\n[DRY-RUN] nada gravado. Rode sem --dry-run para aplicar.")
        return 0

    if atual_new == args.new and atual_rev == args.rev:
        print("\nJa esta no ritmo pedido; nada a fazer.")
        return 0

    cfg["new"]["perDay"] = args.new
    cfg["rev"]["perDay"] = args.rev
    _invoke("saveDeckConfig", config=cfg)
    print(f"\nOK: ritmo do grupo '{cfg.get('name','?')}' fixado em {args.new} novos/dia, "
          f"{args.rev} revisoes/dia.")
    print("  (os 25 sao introducao; as 150 revisoes enchem conforme os blocos NEBLI:: maturam.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
