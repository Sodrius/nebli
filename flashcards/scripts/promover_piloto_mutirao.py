#!/usr/bin/env python3
"""Promove o piloto aprovado do staging para os decks NEBLI, com rollback."""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

from nebli_anki import call

STAMP = "2026-07-15"


def plain_fields(note: dict) -> dict[str, str]:
    return {name: item.get("value", "") for name, item in note["fields"].items()}


def set_field(fields: dict[str, str], names: tuple[str, ...], value: str) -> None:
    for name in names:
        if name in fields:
            fields[name] = value
            return
    raise RuntimeError(f"campo ausente: {names}")


def set_text(fields: dict[str, str], value: str) -> None:
    set_field(fields, ("Text", "Texto", "Front", "Question", "Pergunta", "Cloze"), value)


def set_extra(fields: dict[str, str], value: str) -> None:
    set_field(fields, ("Extra", "Remarks", "Back Extra", "Explicacao", "Explicação"), value)


def deck_for(note_id: int) -> str:
    cards = call("findCards", query=f"nid:{note_id}")
    if not cards:
        raise RuntimeError(f"note sem card: {note_id}")
    return call("cardsInfo", cards=[cards[0]])[0]["deckName"]


def add_tags(note_ids: list[int], tags: list[str]) -> None:
    if note_ids and tags:
        call("addTags", notes=note_ids, tags=" ".join(sorted(set(tags))))


def clone(source: dict, deck: str, tags: list[str], text: str | None = None,
          extra: str | None = None, extra_append: str = "") -> int:
    fields = plain_fields(source)
    if text is not None:
        set_text(fields, text)
    if extra is not None:
        set_extra(fields, extra)
    elif extra_append:
        current = fields.get("Extra", "")
        if extra_append not in current:
            fields["Extra"] = current + extra_append
    return call("addNote", note={
        "deckName": deck,
        "modelName": source["modelName"],
        "fields": fields,
        "tags": sorted(set(source.get("tags", []) + tags)),
        "options": {"allowDuplicate": True},
    })


def update(note: dict, text: str | None = None, extra: str | None = None,
           extra_append: str = "") -> None:
    fields = plain_fields(note)
    changed = {}
    if text is not None:
        set_text(fields, text)
        changed["Text"] = fields.get("Text", text)
    if extra is not None:
        set_extra(fields, extra)
        changed["Extra"] = fields.get("Extra", extra)
    elif extra_append and extra_append not in fields.get("Extra", ""):
        changed["Extra"] = fields.get("Extra", "") + extra_append
    if changed:
        call("updateNoteFields", note={"id": note["noteId"], "fields": changed})


def suspend_extra_cloze_cards(note_id: int) -> list[int]:
    cards = call("findCards", query=f"nid:{note_id}")
    info = call("cardsInfo", cards=cards) if cards else []
    extra = [c["cardId"] for c in info if c.get("ord", 0) > 0]
    if extra:
        call("suspend", cards=extra)
    return extra


def snapshot(note_ids: list[int]) -> dict:
    notes = call("notesInfo", notes=note_ids)
    cards = call("findCards", query=" OR ".join(f"nid:{nid}" for nid in note_ids))
    card_info = call("cardsInfo", cards=cards) if cards else []
    return {
        "generated_at": dt.datetime.now().astimezone().isoformat(),
        "notes": [{
            "note_id": n["noteId"], "model": n["modelName"],
            "fields": plain_fields(n), "tags": n.get("tags", []),
        } for n in notes],
        "cards": [{
            "card_id": c["cardId"], "note_id": c["note"], "deck": c["deckName"],
            "queue": c["queue"], "type": c["type"], "flags": c.get("flags", 0),
        } for c in card_info],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    source_ids = [n["source_note_id"] for n in manifest["notes"]]
    replacement_ids = [rid for n in manifest["notes"] for rid in n.get("replacement_note_ids", [])]
    all_info = {n["noteId"]: n for n in call("notesInfo", notes=sorted(set(source_ids + replacement_ids)))}
    if missing := sorted(set(source_ids + replacement_ids) - set(all_info)):
        raise RuntimeError(f"notes ausentes: {missing}")

    promoted_ids = call("findNotes", query=f'tag:"NEBLI::mutirao_promoted::{STAMP}"')
    promoted = call("notesInfo", notes=promoted_ids) if promoted_ids else []
    promoted_originals = {n["noteId"] for n in promoted if n["noteId"] in source_ids}
    existing_created: dict[tuple[int, str], list[int]] = {}
    for note in promoted:
        tags = note.get("tags", [])
        sid_tag = next((t for t in tags if t.startswith("NEBLI::source_note::")), None)
        if not sid_tag or note["noteId"] in source_ids:
            continue
        sid = int(sid_tag.rsplit("::", 1)[-1])
        kind = next((t for t in tags if t.startswith("NEBLI::source_real::") or t == "NEBLI::split_part::2"), "created")
        existing_created.setdefault((sid, kind), []).append(note["noteId"])

    args.output_dir.mkdir(parents=True, exist_ok=True)
    before_path = args.output_dir / f"ROLLBACK-PILOTO-BEFORE-{STAMP}.json"
    # Em retomadas após timeout, nunca substituir a fotografia realmente anterior.
    if before_path.exists():
        before = json.loads(before_path.read_text(encoding="utf-8-sig"))
    else:
        before = snapshot(source_ids)
        before_path.write_text(json.dumps(before, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    media_path = args.manifest.parent / "assets" / "Gray770-en-1280.png"
    media_name = None
    if media_path.exists():
        raw = media_path.read_bytes()
        media_name = hashlib.sha256(raw).hexdigest()[:32] + ".png"
        call("storeMediaFile", filename=media_name, data=base64.b64encode(raw).decode("ascii"))

    result = []
    created_all = []
    for item in manifest["notes"]:
        sid, action = item["source_note_id"], item["action"]
        expected_kinds = [f"NEBLI::source_real::{rid}" for rid in item.get("replacement_note_ids", [])]
        if action == "split":
            expected_kinds.append("NEBLI::split_part::2")
        already_created = [nid for kind in expected_kinds for nid in existing_created.get((sid, kind), [])]
        if sid in promoted_originals and len(already_created) == len(expected_kinds):
            created_all += already_created
            result.append({"source_note_id": sid, "action": action, "deck": deck_for(sid),
                           "created_note_ids": already_created, "suspended_card_ids": [], "status": "existing"})
            continue
        source, deck = all_info[sid], deck_for(sid)
        common = [f"NEBLI::mutirao_promoted::{STAMP}", f"NEBLI::mutirao_action::{action}",
                  f"NEBLI::source_note::{sid}", f"NEBLI::importance::{item.get('importance', 'unclassified')}",
                  f"NEBLI::cognitive_role::{item.get('cognitive_role', 'unclassified')}"]
        created, suspended = [], []

        if action in {"rewrite", "replace_and_rewrite"}:
            update(source, text=item["new_text"], extra=item["new_extra"])
            add_tags([sid], common)
            suspended += suspend_extra_cloze_cards(sid)
        elif action == "keep_with_credit_fix":
            credit = ('<br><br>Photo credit: BruceBlaus, "Blausen 0657 MultipolarNeuron", '
                      'CC BY 3.0, via Wikimedia Commons. '
                      'https://commons.wikimedia.org/wiki/File:Blausen_0657_MultipolarNeuron.png')
            update(source, extra_append=credit)
            old_visual = [t for t in source.get("tags", []) if t.startswith("NEBLI::image_status::")]
            for tag in old_visual:
                call("removeTags", notes=[sid], tags=tag)
            add_tags([sid], common + ["NEBLI::visual_need::required", "NEBLI::image_role::recognition", "NEBLI::image_status::approved"])
        elif action == "keep_control":
            add_tags([sid], common)
        elif action == "split":
            first, second = item["new_cards"]
            extra1, extra2 = first["extra"], second["extra"]
            if media_name:
                credit = (f'<br><img src="{media_name}"><br>Image: Mysid, based on Gray\'s '
                          'Anatomy plate 770; public domain, via Wikimedia Commons.')
                extra1 += credit
                extra2 += credit
            update(source, text=first["text"], extra=extra1)
            add_tags([sid], common + ["NEBLI::split_part::1"])
            suspended += suspend_extra_cloze_cards(sid)
            query = f'tag:"NEBLI::source_note::{sid}" tag:"NEBLI::split_part::2" tag:"NEBLI::mutirao_promoted::{STAMP}"'
            existing = call("findNotes", query=query)
            if existing:
                created += existing
            else:
                created.append(clone(source, deck, common + ["NEBLI::split_part::2"], second["text"], extra2))
        elif action == "replace":
            cards = call("findCards", query=f"nid:{sid}")
            if cards:
                call("suspend", cards=cards)
                suspended += cards
            add_tags([sid], common + [f"NEBLI::mutirao_replaced::{STAMP}"])
        else:
            raise RuntimeError(f"ação desconhecida: {action}")

        overrides = item.get("replacement_overrides", {})
        for rid in item.get("replacement_note_ids", []):
            query = f'tag:"NEBLI::source_note::{sid}" tag:"NEBLI::source_real::{rid}" tag:"NEBLI::mutirao_promoted::{STAMP}"'
            existing = call("findNotes", query=query)
            if existing:
                created += existing
                continue
            override = overrides.get(str(rid), {})
            tags = common + ["NEBLI::reference_copy", f"NEBLI::source_real::{rid}"]
            if override:
                tags += ["NEBLI::reference_adapted", "NEBLI::lint_pass"]
            nid = clone(all_info[rid], deck, tags, text=override.get("Text"), extra_append=override.get("Extra_append", ""))
            created.append(nid)
        created_all += created
        result.append({"source_note_id": sid, "action": action, "deck": deck,
                       "created_note_ids": created, "suspended_card_ids": sorted(set(suspended))})

    out = {
        "generated_at": dt.datetime.now().astimezone().isoformat(),
        "manifest": str(args.manifest), "before_snapshot": str(before_path),
        "created_note_ids": created_all, "actions": result,
    }
    out_path = args.output_dir / f"PROMOCAO-PILOTO-{STAMP}.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out_path)
    print(json.dumps({"sources": len(source_ids), "created_notes": len(created_all)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
