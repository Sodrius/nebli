#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Aplica um lote de etimologia no Anki de forma idempotente e SUSPENSA.

Seguranca (plano secao 16):
  - dry-run por padrao; --apply para efetivar;
  - identifica cada card por tag imutavel etim_uid::<uid>;
  - cria ou atualiza idempotentemente (nunca duplica);
  - publica SEMPRE suspenso;
  - snapshot previo do estado em releases/;
  - manifesto UID -> noteId ao final.

Uso:
  python flashcards/scripts/validate_etymology.py            # rode o lint antes
  python flashcards/scripts/release_etymology.py             # dry-run
  python flashcards/scripts/release_etymology.py --apply     # cria/atualiza suspenso
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from anki import call

ETIM = Path(__file__).resolve().parents[1] / "etimologia"
DEFAULT_LOTE = ETIM / "cards" / "lote-00.json"
MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"


def find_note_by_uid(uid: str) -> int | None:
    ids = call("findNotes", query=f"tag:etim_uid::{uid}")
    return ids[0] if ids else None


def main(lote_path: Path, apply: bool) -> int:
    lote = json.loads(lote_path.read_text(encoding="utf-8"))
    cards = lote["cards"]

    existing_decks = set(call("deckNames"))
    plan = []  # (uid, action, note_id)
    snapshot = []

    for c in cards:
        uid = c["uid"]
        if c["deck"] not in existing_decks:
            raise RuntimeError(f"deck ausente no Anki: {c['deck']} (rode criar_deck_etimologia.py --apply)")
        nid = find_note_by_uid(uid)
        if nid:
            info = call("notesInfo", notes=[nid])[0]
            snapshot.append({"uid": uid, "noteId": nid,
                             "Text": info["fields"]["Text"]["value"],
                             "Extra": info["fields"]["Extra"]["value"],
                             "tags": info["tags"]})
            plan.append((uid, "update", nid))
        else:
            plan.append((uid, "create", None))

    n_create = sum(1 for _, a, _ in plan if a == "create")
    n_update = sum(1 for _, a, _ in plan if a == "update")
    print(f"lote: {lote_path.name} | cards: {len(cards)}")
    print(f"a criar: {n_create} | a atualizar: {n_update}")

    if not apply:
        for uid, action, nid in plan:
            print(f"  DRY-RUN {action:6} {uid}" + (f" (note {nid})" if nid else ""))
        print("\nNada foi alterado. Use --apply para efetivar (publica suspenso).")
        return 0

    rel_dir = ETIM / "releases" / f"lote-00-{time.strftime('%Y%m%d-%H%M%S')}"
    rel_dir.mkdir(parents=True, exist_ok=True)
    (rel_dir / "snapshot-pre.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest = {}
    for c, (uid, action, nid) in zip(cards, plan):
        fields = {"Text": c["text"], "Extra": (c.get("extra") or "").replace("\n", "<br>")}
        tags = c.get("tags", [])
        if action == "create":
            nid = call("addNote", note={
                "deckName": c["deck"], "modelName": MODEL,
                "fields": fields, "tags": tags,
                "options": {"allowDuplicate": False},
            })
        else:
            call("updateNoteFields", note={"id": nid, "fields": fields})
            call("addTags", notes=[nid], tags=" ".join(tags))
        card_ids = call("findCards", query=f"nid:{nid}")
        call("suspend", cards=card_ids)
        manifest[uid] = {"noteId": nid, "cardIds": card_ids, "action": action, "deck": c["deck"]}
        print(f"  {action:6} {uid} -> note {nid} (suspenso)")

    (rel_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nOK: {n_create} criados, {n_update} atualizados, todos SUSPENSOS.")
    print(f"Snapshot + manifesto em: {rel_dir}")
    print("Sync UP no container e revise no celular; dessuspenda apos sua revisao.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", type=Path, default=DEFAULT_LOTE)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    raise SystemExit(main(args.lote, args.apply))
