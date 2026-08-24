#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Importa somente o piloto v2, idempotente e suspenso."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from nebli_anki import call

ETIM = Path(__file__).resolve().parents[1] / "etimologia"
PILOT = ETIM / "cards" / "cards_pilot_v2.json"
MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"


def reviewer_guard() -> None:
    try:
        current = call("guiCurrentCard")
    except RuntimeError as exc:
        if "not currently active" in str(exc): return
        raise
    if current:
        raise RuntimeError("Reviewer ativo: importação bloqueada por ANTI-EXEMPLARES A11")


def uid_from_tags(tags):
    for tag in tags:
        if tag.startswith("etim_uid::etim-v2-"): return tag.split("::", 1)[1]
    return None


def main(apply: bool) -> int:
    reviewer_guard()
    payload = json.loads(PILOT.read_text(encoding="utf-8"))
    cards = payload["cards"]
    if payload.get("approval_gate") != "pilot_pending_user_review":
        raise RuntimeError("gate do piloto ausente")
    decks = set(call("deckNames"))
    absent = sorted({c["deck"] for c in cards} - decks)
    if absent: raise RuntimeError(f"decks ausentes: {absent}")
    existing_ids = call("findNotes", query="tag:etim_v2")
    existing_info = call("notesInfo", notes=existing_ids) if existing_ids else []
    existing = {uid_from_tags(x["tags"]): x for x in existing_info if uid_from_tags(x["tags"])}
    creates = [c for c in cards if c["uid"] not in existing]
    updates = [c for c in cards if c["uid"] in existing]
    print(f"piloto: {len(cards)} notas / {sum(c['number_of_cards'] for c in cards)} cards")
    print(f"criar: {len(creates)} | atualizar: {len(updates)} | sempre suspensos")
    if not apply:
        print("Dry-run concluído; nenhuma alteração.")
        return 0
    rel = ETIM / "releases" / f"pilot-v2-{time.strftime('%Y%m%d-%H%M%S')}"
    rel.mkdir(parents=True, exist_ok=True)
    snapshot = [{"noteId": x["noteId"], "uid": uid_from_tags(x["tags"]),
                 "Text": x["fields"]["Text"]["value"], "Extra": x["fields"]["Extra"]["value"],
                 "tags": x["tags"]} for x in existing_info if uid_from_tags(x["tags"]) in {c["uid"] for c in cards}]
    (rel / "snapshot-pre.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
    new_ids = []
    if creates:
        notes = [{"deckName": c["deck"], "modelName": MODEL,
                  "fields": {"Text": c["text"], "Extra": c["extra"]}, "tags": c["tags"],
                  "options": {"allowDuplicate": False}} for c in creates]
        new_ids = call("addNotes", notes=notes)
        if any(x is None for x in new_ids): raise RuntimeError("addNotes recusou uma ou mais notas")
    actions = []
    for c in updates:
        nid = existing[c["uid"]]["noteId"]
        actions.extend([
            {"action": "updateNoteFields", "params": {"note": {"id": nid, "fields": {"Text": c["text"], "Extra": c["extra"]}}}},
            {"action": "addTags", "params": {"notes": [nid], "tags": " ".join(c["tags"])}},
        ])
    for start in range(0, len(actions), 50):
        results = call("multi", actions=actions[start:start + 50])
        failures = [x for x in results if isinstance(x, dict) and x.get("error")]
        if failures: raise RuntimeError(f"falha em atualização multi: {failures[:3]}")
    note_ids = new_ids + [existing[c["uid"]]["noteId"] for c in updates]
    card_ids = call("findCards", query="tag:etim_v2")
    call("suspend", cards=card_ids)
    info = call("cardsInfo", cards=card_ids[:5]) if card_ids else []
    if not info or any(not x.get("question") or not x.get("answer") for x in info):
        raise RuntimeError("smoke test de renderização falhou")
    manifest = {"notes": len(note_ids), "cards": len(card_ids), "suspended": True,
                "created": len(creates), "updated": len(updates), "sample_rendered": len(info)}
    (rel / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (ETIM / "reports" / "anki_import.md").write_text(
        f"# Importação do piloto v2\n\n- Notas: {len(note_ids)}\n- Cards: {len(card_ids)}\n- Criadas: {len(creates)}\n- Atualizadas: {len(updates)}\n- Suspensos: sim\n- Renderização relida: {len(info)}/5\n- Release: `{rel.name}`\n",
        encoding="utf-8")
    print(f"OK: {len(note_ids)} notas, {len(card_ids)} cards suspensos; render {len(info)}/5.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true")
    raise SystemExit(main(ap.parse_args().apply))
