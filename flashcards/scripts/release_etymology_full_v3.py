#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Importa o deck integral v3, absorve o piloto pt2 e retira os pilotos do Anki.

Idempotente por UID estável; todo o material entra suspenso.
"""
from __future__ import annotations

import argparse
import json
import time
from collections import defaultdict
from pathlib import Path

from nebli_anki import call

ETIM = Path(__file__).resolve().parents[1] / "etimologia"
PAYLOAD = ETIM / "cards" / "cards_approved_v3.json"
MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"
FULL_TAG = "etim_full_v3"
PILOT_PT2_TAG = "etim_pilot_pt2"
PILOT_V2_TAG = "etim_v2"
PILOT_PT2_DECK = "NEBLI::Etimologia::Piloto pt2"


def reviewer_guard() -> None:
    try:
        current = call("guiCurrentCard")
    except RuntimeError as exc:
        if "not currently active" in str(exc):
            return
        raise
    if current:
        raise RuntimeError("Reviewer ativo: sincronização bloqueada")


def uid_from_tags(tags: list[str]) -> str | None:
    for tag in tags:
        if tag.startswith("etim_uid::"):
            return tag.split("::", 1)[1]
    return None


def chunks(items: list, size: int) -> list[list]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def notes_info_for_tag(tag: str) -> list[dict]:
    ids = call("findNotes", query=f"tag:{tag}")
    # Uma chamada reduz drasticamente a latência do AnkiConnect para o lote final.
    return call("notesInfo", notes=ids) if ids else []


def main(apply: bool) -> int:
    reviewer_guard()
    payload = json.loads(PAYLOAD.read_text(encoding="utf-8"))
    if payload.get("approval_gate") != "user_authorized_full_generation":
        raise RuntimeError("gate de geração integral autorizado pelo usuário ausente")
    cards = payload["cards"]
    expected_count = int(payload.get("stats", {}).get("notes", len(cards)))
    if len(cards) != expected_count or len({c["uid"] for c in cards}) != len(cards):
        raise RuntimeError("payload integral inválido ou com UIDs repetidos")
    if set(call("modelFieldNames", modelName=MODEL)) < {"Text", "Extra"}:
        raise RuntimeError("modelo AnKing não possui os campos Text e Extra")

    existing_info = notes_info_for_tag(FULL_TAG) + notes_info_for_tag(PILOT_PT2_TAG)
    existing: dict[str, dict] = {}
    for note in existing_info:
        uid = uid_from_tags(note["tags"])
        if uid:
            existing[uid] = note
    creates = [c for c in cards if c["uid"] not in existing]
    updates = [c for c in cards if c["uid"] in existing]
    updates_needed = [c for c in updates if (
        existing[c["uid"]]["fields"]["Text"]["value"] != c["text"]
        or existing[c["uid"]]["fields"]["Extra"]["value"] != c["extra"]
        or not set(c["tags"]).issubset(set(existing[c["uid"]]["tags"]))
    )]
    old_v2 = notes_info_for_tag(PILOT_V2_TAG)
    print(f"integral v3: {len(cards)} notas/cards | criar {len(creates)} | atualizar {len(updates)} | retirar piloto v2 {len(old_v2)}")
    if not apply:
        print("Dry-run: nenhuma alteração no Anki.")
        return 0

    release = ETIM / "releases" / f"full-v3-{time.strftime('%Y%m%d-%H%M%S')}"
    release.mkdir(parents=True, exist_ok=True)
    snapshot = {
        "reused_pt2_or_prior_full": [{
            "noteId": n["noteId"], "uid": uid_from_tags(n["tags"]),
            "Text": n["fields"]["Text"]["value"], "Extra": n["fields"]["Extra"]["value"],
            "tags": n["tags"], "cards": n.get("cards", []),
        } for n in existing_info],
        "pilot_v2_to_remove": [{
            "noteId": n["noteId"], "uid": uid_from_tags(n["tags"]),
            "Text": n["fields"]["Text"]["value"], "Extra": n["fields"]["Extra"]["value"],
            "tags": n["tags"], "cards": n.get("cards", []),
        } for n in old_v2],
    }
    (release / "snapshot-pre.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    for deck in sorted({c["deck"] for c in cards}):
        call("createDeck", deck=deck)
    created = 0
    for part in chunks(creates, 75):
        note_ids = call("addNotes", notes=[{
            "deckName": c["deck"], "modelName": MODEL,
            "fields": {"Text": c["text"], "Extra": c["extra"]},
            "tags": c["tags"], "options": {"allowDuplicate": False},
        } for c in part])
        if len(note_ids) != len(part) or any(note_id is None for note_id in note_ids):
            raise RuntimeError("addNotes recusou uma ou mais notas")
        created += len(note_ids)

    update_actions = []
    for c in updates_needed:
        note_id = existing[c["uid"]]["noteId"]
        update_actions.extend([
            {"action": "updateNoteFields", "params": {"note": {"id": note_id, "fields": {"Text": c["text"], "Extra": c["extra"]}}}},
            {"action": "addTags", "params": {"notes": [note_id], "tags": " ".join(c["tags"])}},
        ])
    for part in chunks(update_actions, 50):
        result = call("multi", actions=part)
        failures = [x for x in result if isinstance(x, dict) and x.get("error")]
        if failures:
            raise RuntimeError(f"falha ao atualizar: {failures[:3]}")

    full_info = notes_info_for_tag(FULL_TAG)
    if len(full_info) != len(cards):
        raise RuntimeError(f"contagem v3 divergente: {len(full_info)}/{len(cards)} notas")
    expected = {c["uid"]: c for c in cards}
    deck_cards: dict[str, list[int]] = defaultdict(list)
    field_errors = []
    for note in full_info:
        uid = uid_from_tags(note["tags"])
        card = expected.get(uid or "")
        if not card:
            field_errors.append(f"UID ausente: {uid}")
            continue
        if note["fields"]["Text"]["value"] != card["text"] or note["fields"]["Extra"]["value"] != card["extra"]:
            field_errors.append(f"campos divergentes: {uid}")
        deck_cards[card["deck"]].extend(note.get("cards", []))
    if field_errors:
        raise RuntimeError("; ".join(field_errors[:5]))
    for deck, card_ids in deck_cards.items():
        if card_ids:
            call("changeDeck", cards=card_ids, deck=deck)

    # O piloto pt2 é reaproveitado como parte do integral, mas deixa de existir como piloto.
    pt2_ids = call("findNotes", query=f"tag:{PILOT_PT2_TAG}")
    if pt2_ids:
        call("removeTags", notes=pt2_ids, tags=f"{PILOT_PT2_TAG} terminologia::status::piloto_pt2")

    # O piloto v2 é obsoleto e separado: remove-se somente as notas com esta tag exata,
    # preservadas no snapshot da release para auditoria/recuperação manual.
    old_v2_ids = call("findNotes", query=f"tag:{PILOT_V2_TAG}")
    if old_v2_ids:
        call("deleteNotes", notes=old_v2_ids)

    full_card_ids = call("findCards", query=f"tag:{FULL_TAG}")
    if len(full_card_ids) != len(cards):
        raise RuntimeError(f"contagem de cards v3 divergente: {len(full_card_ids)}/{len(cards)}")
    call("suspend", cards=full_card_ids)
    render_sample_ids = full_card_ids[:20]
    rendered = call("cardsInfo", cards=render_sample_ids)
    if len(rendered) != len(render_sample_ids) or any(not x.get("question") or not x.get("answer") for x in rendered):
        raise RuntimeError("verificação de renderização falhou")
    if len(call("findCards", query=f"tag:{FULL_TAG} is:suspended")) != len(cards):
        raise RuntimeError("suspensão incompleta")
    if call("findNotes", query=f"tag:{PILOT_PT2_TAG}") or call("findNotes", query=f"tag:{PILOT_V2_TAG}"):
        raise RuntimeError("sobraram notas de piloto após a migração")

    if not call("findCards", query=f'deck:"{PILOT_PT2_DECK}"') and PILOT_PT2_DECK in call("deckNames"):
        # A API recente exige cardsToo=True. A consulta anterior garante 0 cards
        # neste deck específico; portanto não há cards a apagar nesta chamada.
        call("deleteDecks", decks=[PILOT_PT2_DECK], cardsToo=True)

    manifest = {
        "notes": len(full_info), "cards": len(full_card_ids), "suspended": True,
        "created_this_run": created, "updated_or_reused": len(updates), "updated_this_run": len(updates_needed),
        "pilot_v2_removed_notes": len(old_v2), "pilot_pt2_rehomed_notes": len(pt2_ids),
        "rendered_sample": len(rendered), "source": str(PAYLOAD),
    }
    (release / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (ETIM / "reports" / "anki_import_full_v3.md").write_text(
        "# Sincronização do deck integral v3\n\n"
        f"- Notas/cards finais: {len(full_info)}\n- Criadas nesta execução: {created}\n- Reaproveitadas: {len(updates)}\n"
        f"- Piloto pt2 reclassificado: {len(pt2_ids)} notas\n- Piloto v2 removido: {len(old_v2)} notas\n"
        f"- Todas suspensas: sim\n- Renderização relida: {len(rendered)}/{len(render_sample_ids)}\n"
        f"- Release: `{release.name}`\n",
        encoding="utf-8")
    print(f"OK: {len(full_info)} notas/cards v3 suspensos; {created} criadas; piloto v2 removido {len(old_v2)}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    raise SystemExit(main(parser.parse_args().apply))
