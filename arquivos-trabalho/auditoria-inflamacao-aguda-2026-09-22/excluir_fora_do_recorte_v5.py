"""Exclui cópias NEBLI que não pertencem ao deck-aula aprovado.

Suspensão é reservada a card bom que o estudante quer pausar. Estes itens já
foram julgados ruins, excessivos ou laterais ao recorte; o AnKing original não
é tocado. Um APKG com agendamento é criado antes da remoção.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from inspecionar_v2 import call
from recalibrar_v3 import DECK, key_tag, load_current, map_entries, selected_entries

OUT = Path(__file__).resolve().parent / "revisao-v2"


def target():
    notes, cards = load_current()
    by_tag = map_entries(notes)
    _, excluded = selected_entries()
    note_ids = [by_tag[key_tag(entry)]["noteId"] for entry in excluded]
    card_ids = [card_id for entry in excluded for card_id in by_tag[key_tag(entry)]["cards"]]
    by_card = {card["cardId"]: card for card in cards}
    if not all(by_card[card_id]["queue"] == -1 for card_id in card_ids):
        raise RuntimeError("Há alvo não suspenso; interrompido para não apagar card ativo")
    return notes, cards, excluded, note_ids, card_ids, by_card


def check():
    _, _, entries, note_ids, card_ids, by_card = target()
    return {
        "deck": DECK,
        "notes_to_delete": len(note_ids),
        "cards_to_delete": len(card_ids),
        "keys": [entry["key"] for entry in entries],
        "all_suspended": True,
        "total_reps_to_delete": sum(by_card[card_id]["reps"] for card_id in card_ids),
        "cards_with_reps": [
            {"card_id": card_id, "reps": by_card[card_id]["reps"]}
            for card_id in card_ids if by_card[card_id]["reps"]
        ],
    }


def apply():
    before_notes, before_cards, entries, note_ids, card_ids, by_card = target()
    safety = OUT / "backup-antes-exclusao-v5.apkg"
    call("exportPackage", deck=DECK, path=str(safety.resolve()), includeSched=True)
    call("deleteNotes", notes=note_ids)
    after_notes, after_cards = load_current()
    if set(note_ids) & {note["noteId"] for note in after_notes}:
        raise RuntimeError("Alguma nota alvo não foi removida")
    if len(after_notes) != len(before_notes) - len(note_ids):
        raise RuntimeError("Contagem de notas inesperada")
    if len(after_cards) != len(before_cards) - len(card_ids):
        raise RuntimeError("Contagem de cards inesperada")
    if call("findCards", query=f'deck:"{DECK}" is:suspended'):
        raise RuntimeError("Há cards suspensos restantes; revisar antes de declarar estado final")
    package = OUT / "Inflamacao aguda.apkg"
    call("exportPackage", deck=DECK, path=str(package.resolve()), includeSched=True)
    receipt = {
        "at": datetime.now(timezone.utc).isoformat(),
        "deck": DECK,
        "deleted_notes": len(note_ids),
        "deleted_cards": len(card_ids),
        "deleted_keys": [entry["key"] for entry in entries],
        "reps_in_deleted_cards": sum(by_card[card_id]["reps"] for card_id in card_ids),
        "backup_before_deletion": str(safety.resolve()),
        "backup_sha256": hashlib.sha256(safety.read_bytes()).hexdigest(),
        "package": str(package.resolve()),
        "package_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
        "remaining_notes": len(after_notes),
        "remaining_cards": len(after_cards),
        "suspended_cards": 0,
        "original_AnKing_source": "not modified",
    }
    (OUT / "receipt-v5-exclusion.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("check", "apply"))
    args = parser.parse_args()
    if args.mode == "check":
        print(json.dumps(check(), ensure_ascii=False, indent=2))
    else:
        apply()
