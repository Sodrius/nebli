#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zerar_deck_anking.py -- re-suspende TODOS os cards ativos (reversivel).

Deixa o deck "zerado" pra reconstruir com blocos curados. Antes de suspender,
marca os cards ativos com uma tag de resgate NEBLI::zerado::<data> -- assim o
"reversivel" e real: reverter = dessuspender essa tag.

NAO apaga nada, NAO mexe em histórico/agendamento (so troca o estado suspenso).

Uso:
    python flashcards/scripts/zerar_deck_anking.py --dry-run      # conta os ativos
    python flashcards/scripts/zerar_deck_anking.py                # zera (suspende)
    python flashcards/scripts/zerar_deck_anking.py --reverter --data 2026-07-04
    python flashcards/scripts/zerar_deck_anking.py --reverter --dry-run --data 2026-07-04
"""
import json, sys, argparse, datetime, urllib.request, urllib.error

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ANKICONNECT = "http://localhost:8765"


def _invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload)
    with urllib.request.urlopen(req, timeout=30) as resp:
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


def main():
    ap = argparse.ArgumentParser(description="Re-suspende todos os cards ativos (reversivel via tag de resgate).")
    ap.add_argument("--dry-run", action="store_true", help="so conta, nao mexe")
    ap.add_argument("--reverter", action="store_true", help="dessuspende a tag de resgate de --data")
    ap.add_argument("--data", default=datetime.date.today().isoformat(),
                    help="data da tag de resgate (default hoje). Ex.: 2026-07-04")
    args = ap.parse_args()

    if not _anki_vivo():
        print("AnkiConnect fora do ar. Abra o Anki (add-on 2055492159) e tente de novo.")
        sys.exit(3)

    resgate = f"NEBLI::zerado::{args.data}"

    if args.reverter:
        cards = _invoke("findCards", query=f'"tag:{resgate}"')
        print(f"Reverter zeragem de {args.data}: {len(cards)} cards sob {resgate}.")
        if not args.dry_run and cards:
            _invoke("unsuspend", cards=cards)
            print("  -> dessuspensos (voltaram ao estado ativo).")
        elif args.dry_run:
            print("  [DRY-RUN] rode sem --dry-run para dessuspender.")
        return

    ativos = _invoke("findCards", query="-is:suspended")
    print(f"Cards ATIVOS agora: {len(ativos)}.{'  [DRY-RUN]' if args.dry_run else ''}")
    if not ativos:
        print("Deck ja esta zerado (nada ativo).")
        return
    if args.dry_run:
        print(f"SERIAM marcados com {resgate} e suspensos {len(ativos)} cards.")
        print("Rode sem --dry-run para aplicar. Reversivel depois com --reverter --data " + args.data)
        return

    # marca a tag de resgate nos NOTES desses cards (via cardsToNotes) antes de suspender
    nids = _invoke("cardsToNotes", cards=ativos)
    _invoke("addTags", notes=nids, tags=resgate)
    _invoke("suspend", cards=ativos)
    print(f"Zerado: {len(ativos)} cards suspensos e marcados com {resgate}.")
    print(f"Reverter tudo: python flashcards/scripts/zerar_deck_anking.py --reverter --data {args.data}")


if __name__ == "__main__":
    main()
