"""Fecha três lacunas explícitas: linfa retal e artéria retal média.

Dois cards vêm do AnKing; um card curto é autoral porque a busca no acervo não
encontrou a origem da artéria retal média em nenhum deck acessível.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone

from inventory_vascularizacao import call
from prepare_vascularizacao import DECK, LESSON, ROOT, digest


TAG = f"NEBLI::{LESSON}"
SOURCE_MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"
TARGET_MODEL = "NEBLI AnKing independente - v3"
NEW_SOURCES = [1486771351448, 1486771380083]
AUTHORIAL_KEY = f"NEBLI::lesson-local::{LESSON}::middle-rectal-artery"
EXPECTED_BEFORE = {"notes": 44, "cards": 85, "green": 37}
EXPECTED_AFTER = {"notes": 47, "cards": 88, "green": 37}


def save(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def plain(note):
    return {name: field["value"] for name, field in note["fields"].items()}


def fingerprint(cards):
    keys = [
        "note", "ord", "type", "queue", "due", "interval", "factor",
        "reps", "lapses", "left", "odue", "odid", "flags",
    ]
    return {card["cardId"]: {key: card.get(key) for key in keys} for card in cards}


def add_note(fields, tags):
    target_fields = {name: "" for name in call("modelFieldNames", modelName=TARGET_MODEL)}
    target_fields.update(fields)
    if "ankihub_id" in target_fields:
        target_fields["ankihub_id"] = ""
    note_id = call(
        "addNote",
        note={
            "deckName": DECK,
            "modelName": TARGET_MODEL,
            "fields": target_fields,
            "tags": tags,
            "options": {"allowDuplicate": True},
        },
    )
    note = call("notesInfo", notes=[note_id])[0]
    cards = call("cardsInfo", cards=note["cards"])
    if len(cards) != 1:
        raise RuntimeError(f"Nota {note_id} gerou {len(cards)} cards.")
    if cards[0]["deckName"] != DECK:
        if cards[0]["reps"] != 0:
            raise RuntimeError("Card novo fora do deck já possui revisão.")
        call("changeDeck", cards=[cards[0]["cardId"]], deck=DECK)
        cards = call("cardsInfo", cards=note["cards"])
    if plain(note) != target_fields or cards[0]["deckName"] != DECK:
        raise RuntimeError(f"Readback falhou para {note_id}.")
    return note_id, cards[0]["cardId"]


def main():
    receipt = json.loads((ROOT / "receipt.json").read_text(encoding="utf-8"))
    current_note_ids = [result["new_nid"] for result in receipt["results"]]
    current_notes = call("notesInfo", notes=current_note_ids)
    current_cards = call("cardsInfo", cards=[card for note in current_notes for card in note["cards"]])
    green_before = call("findCards", query=f'deck:"{DECK}" flag:3')
    if len(current_notes) != EXPECTED_BEFORE["notes"] or len(current_cards) != EXPECTED_BEFORE["cards"]:
        raise RuntimeError("Estado inicial do deck não corresponde à entrega v1.")
    if len(green_before) != EXPECTED_BEFORE["green"]:
        raise RuntimeError("Bandeiras verdes mudaram desde a entrega v1.")
    if call("findCards", query=f'deck:"{DECK}" flag:1'):
        raise RuntimeError("Há feedback vermelho novo; recalibração cancelada.")
    if call("findCards", query=f'deck:"{DECK}" is:suspended'):
        raise RuntimeError("Há suspensão nova; recalibração cancelada.")
    existing_state = fingerprint(current_cards)

    sources = {note["noteId"]: note for note in call("notesInfo", notes=NEW_SOURCES)}
    if set(sources) != set(NEW_SOURCES):
        raise RuntimeError("Fonte nova ausente.")
    for source_id in NEW_SOURCES:
        found = call("findNotes", query=f'tag:"NEBLI::source::nid-{source_id}"')
        if found:
            raise RuntimeError(f"Fonte {source_id} já possui cópia: {found}")
    if call("findNotes", query=f'tag:"{AUTHORIAL_KEY}"'):
        raise RuntimeError("Card autoral já existe.")

    backup = ROOT / "backup-antes-recalibracao-v2.apkg"
    if not backup.exists():
        if not call("exportPackage", deck=DECK, path=str(backup.resolve()), includeSched=True):
            raise RuntimeError("Falha no backup pré-recalibração.")
    snapshot = {
        "at": datetime.now(timezone.utc).isoformat(),
        "existing_notes": current_notes,
        "existing_cards": current_cards,
        "new_sources": list(sources.values()),
        "backup": str(backup.resolve()),
    }
    save("before-recalibration-v2.json", snapshot)

    results = []
    for source_id in NEW_SOURCES:
        source = sources[source_id]
        fields = plain(source)
        note_id, card_id = add_note(
            fields,
            list(dict.fromkeys(source["tags"] + [
                TAG,
                f"NEBLI::source::nid-{source_id}",
                "NEBLI::objetivo::rectal-lymphatic-drainage",
                "NEBLI::origem::AnKing",
            ])),
        )
        results.append({
            "key": f"source-{source_id}", "source_nid": source_id,
            "source_hash": digest(source["fields"]), "new_nid": note_id,
            "cards": [card_id], "origin": "AnKing",
            "objective": "rectal-lymphatic-drainage", "high_yield": False,
        })

    authorial_fields = {
        "Text": (
            "The <b>middle rectal artery</b> most commonly arises from the "
            "{{c1::<b>anterior division of the internal iliac artery</b>}}"
        ),
        "Extra": "",
    }
    authorial_nid, authorial_card = add_note(
        authorial_fields,
        [
            TAG, AUTHORIAL_KEY,
            "NEBLI::objetivo::rectal-arterial-supply",
            "NEBLI::origem::Autoral",
        ],
    )
    results.append({
        "key": "authorial-middle-rectal-artery", "source_nid": None,
        "new_nid": authorial_nid, "cards": [authorial_card],
        "origin": "Autoral", "objective": "rectal-arterial-supply",
        "high_yield": False,
        "reason": "Conteúdo explícito no slide; ausente após buscas no AnKing, Dope Anatomy e demais decks acessíveis.",
    })

    # Nenhum estado anterior pode mudar.
    current_after = call("cardsInfo", cards=list(existing_state))
    if fingerprint(current_after) != existing_state:
        raise RuntimeError("Agendamento, fila ou bandeira de card preexistente mudou.")
    for source_id, original in sources.items():
        current = call("notesInfo", notes=[source_id])[0]
        if current["fields"] != original["fields"] or current["tags"] != original["tags"]:
            raise RuntimeError(f"Fonte nova {source_id} foi alterada.")

    final_note_ids = current_note_ids + [result["new_nid"] for result in results]
    final_notes = call("notesInfo", notes=final_note_ids)
    final_cards = call("cardsInfo", cards=[card for note in final_notes for card in note["cards"]])
    green_after = call("findCards", query=f'deck:"{DECK}" flag:3')
    if len(final_notes) != EXPECTED_AFTER["notes"] or len(final_cards) != EXPECTED_AFTER["cards"]:
        raise RuntimeError("Contagem final incorreta.")
    if set(green_after) != set(green_before):
        raise RuntimeError("Bandeiras verdes mudaram.")
    if call("findCards", query=f'deck:"{DECK}" flag:1'):
        raise RuntimeError("Bandeira vermelha inesperada.")
    if call("findCards", query=f'deck:"{DECK}" is:suspended'):
        raise RuntimeError("Suspensão inesperada.")

    package = ROOT / "Vascularizacao das visceras v2.apkg"
    if not call("exportPackage", deck=DECK, path=str(package.resolve()), includeSched=True):
        raise RuntimeError("Falha ao exportar pacote v2.")
    final_receipt = {
        "at": datetime.now(timezone.utc).isoformat(),
        "lesson_id": LESSON,
        "deck": DECK,
        "base_receipt_sha256": hashlib.sha256((ROOT / "receipt.json").read_bytes()).hexdigest(),
        "notes": len(final_notes),
        "cards": len(final_cards),
        "cards_by_origin": {"AnKing": 43, "Dope Anatomy": 42, "Dorian": 2, "Autoral": 1},
        "green_high_yield_cards": len(green_after),
        "red_improve_cards": 0,
        "suspended_cards": 0,
        "authorial_cards": 1,
        "authorial_reason": results[-1]["reason"],
        "new_results": results,
        "all_note_ids": final_note_ids,
        "package": str(package.resolve()),
        "package_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
        "existing_scheduling_flags_and_sources_unchanged": True,
    }
    save("receipt-v2.json", final_receipt)
    print(json.dumps(final_receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
