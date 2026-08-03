#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sincroniza o piloto pt2 de modo idempotente e sempre suspenso."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from anki import call

ETIM = Path(__file__).resolve().parents[1] / "etimologia"
PILOT = ETIM / "cards" / "cards_pilot_pt2.json"
MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"
TAG = "etim_pilot_pt2"


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
        if tag.startswith("etim_uid::etim-pt2-"):
            return tag.split("::", 1)[1]
    return None


def main(apply: bool) -> int:
    reviewer_guard()
    payload = json.loads(PILOT.read_text(encoding="utf-8"))
    if payload.get("approval_gate") != "pilot_pt2_pending_user_review":
        raise RuntimeError("gate humano do piloto pt2 ausente")
    cards = payload["cards"]
    if apply:
        for deck in sorted({c["deck"] for c in cards}):
            call("createDeck", deck=deck)
    existing_ids = call("findNotes", query=f"tag:{TAG}")
    existing_info = call("notesInfo", notes=existing_ids) if existing_ids else []
    existing = {uid_from_tags(x["tags"]): x for x in existing_info if uid_from_tags(x["tags"])}
    creates = [c for c in cards if c["uid"] not in existing]
    updates = [c for c in cards if c["uid"] in existing]
    print(f"piloto pt2: {len(cards)} notas/cards | criar {len(creates)} | atualizar {len(updates)}")
    if not apply:
        print("Dry-run: nenhuma alteração no Anki.")
        return 0

    rel = ETIM / "releases" / f"pilot-pt2-{time.strftime('%Y%m%d-%H%M%S')}"
    rel.mkdir(parents=True, exist_ok=True)
    snapshot = [{
        "noteId": x["noteId"], "uid": uid_from_tags(x["tags"]),
        "Text": x["fields"]["Text"]["value"], "Extra": x["fields"]["Extra"]["value"],
        "tags": x["tags"],
    } for x in existing_info]
    (rel / "snapshot-pre.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    new_ids: list[int] = []
    if creates:
        notes = [{
            "deckName": c["deck"], "modelName": MODEL,
            "fields": {"Text": c["text"], "Extra": c["extra"]},
            "tags": c["tags"], "options": {"allowDuplicate": False},
        } for c in creates]
        new_ids = call("addNotes", notes=notes)
        if any(nid is None for nid in new_ids):
            raise RuntimeError("addNotes recusou uma ou mais notas")

    actions = []
    for c in updates:
        nid = existing[c["uid"]]["noteId"]
        actions += [
            {"action": "updateNoteFields", "params": {"note": {"id": nid, "fields": {"Text": c["text"], "Extra": c["extra"]}}}},
            {"action": "addTags", "params": {"notes": [nid], "tags": " ".join(c["tags"])}},
        ]
    for start in range(0, len(actions), 50):
        result = call("multi", actions=actions[start:start + 50])
        failures = [x for x in result if isinstance(x, dict) and x.get("error")]
        if failures:
            raise RuntimeError(f"falha no lote de atualização: {failures[:3]}")

    note_ids = call("findNotes", query=f"tag:{TAG}")
    card_ids = call("findCards", query=f"tag:{TAG}")
    if len(note_ids) != len(cards) or len(card_ids) != len(cards):
        raise RuntimeError(f"contagem divergente: {len(note_ids)} notas, {len(card_ids)} cards")
    call("suspend", cards=card_ids)
    info = call("cardsInfo", cards=card_ids[:10])
    if len(info) != min(10, len(card_ids)) or any(not x.get("question") or not x.get("answer") for x in info):
        raise RuntimeError("smoke test de renderização falhou")
    suspended_ids = call("findCards", query=f"tag:{TAG} is:suspended")
    if len(suspended_ids) != len(card_ids):
        raise RuntimeError(f"suspensão incompleta: {len(suspended_ids)}/{len(card_ids)}")

    manifest = {
        "notes": len(note_ids), "cards": len(card_ids), "suspended": True,
        "created": len(creates), "updated": len(updates), "sample_rendered": len(info),
        "source": str(PILOT),
    }
    (rel / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (ETIM / "reports" / "anki_import_pt2.md").write_text(
        "# Sincronização do piloto pt2\n\n"
        f"- Notas/cards: {len(note_ids)}\n- Criadas: {len(creates)}\n- Atualizadas: {len(updates)}\n"
        f"- Suspensas: sim\n- Renderização relida: {len(info)}/10\n- Release: `{rel.name}`\n",
        encoding="utf-8")
    print(f"OK: {len(note_ids)} notas/cards suspensos; render {len(info)}/10; release {rel.name}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--apply", action="store_true")
    raise SystemExit(main(parser.parse_args().apply))
