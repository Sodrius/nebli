#!/usr/bin/env python3
"""Finaliza feedback e remove staging em um unico lote, fora do Reviewer."""
from __future__ import annotations

import datetime as dt
import base64
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nebli_anki import call

STAMP = "2026-07-15"
ROOT = Path("arquivos-trabalho/mutirao-qualidade")
LEDGER = ROOT / "feedback" / f"LEDGER-FEEDBACK-FECHADO-{STAMP}.json"
RESULT = ROOT / "feedback" / f"FINALIZACAO-FEEDBACK-STAGING-{STAMP}.json"
STAGING_DECK = "NEBLI::STAGING::Mutirao qualidade::Piloto 2026-07-15"


def values(note):
    return {k: v.get("value", "") for k, v in note.get("fields", {}).items()}


def main():
    try:
        current = call("guiCurrentCard")
    except RuntimeError as exc:
        if "not currently active" not in str(exc):
            raise
        current = None
    if current:
        print(json.dumps({"status": "deferred_reviewer_active", "card_id": current.get("cardId")}, indent=2))
        raise SystemExit(75)

    ledger = json.loads(LEDGER.read_text(encoding="utf-8-sig"))
    original_feedback = []
    for n in ledger["notes_before"]:
        fs = n.get("fields", {})
        if fs.get("NEBLI_Comentario", "").strip() or any(
                t.startswith("NEBLI_comentario::") for t in n.get("tags", [])):
            original_feedback.append(n["note_id"])

    flag_ids = sorted(set(ledger.get("flag_card_ids", [])))
    involved = sorted(set([n["note_id"] for n in ledger["notes_before"]]
                          + ledger.get("created_note_ids", [])))
    notes = call("notesInfo", notes=involved)
    by_note = {n["noteId"]: n for n in notes}
    cards = call("cardsInfo", cards=call("findCards", query=" OR ".join(f"nid:{n}" for n in involved)))

    to_unsuspend, to_suspend = [], []
    structural_markers = ("mutirao_replaced", "replaced_archive", "replaced_by_image_occlusion",
                          "blocked_required_visual", "io_peripheral")
    for c in cards:
        tags = by_note[c["note"]].get("tags", [])
        structural = c.get("ord", 0) > 0 or any(
            marker in tag for marker in structural_markers for tag in tags)
        (to_suspend if structural else to_unsuspend).append(c["cardId"])

    feedback_now = call("notesInfo", notes=original_feedback) if original_feedback else []
    comment_tags = sorted({t for n in feedback_now for t in n.get("tags", [])
                           if t.startswith("NEBLI_comentario::")})
    actions = []
    # Corrige o piloto IO do timo: crop sem o segundo rotulo "M" visivel e
    # caixas calibradas sobre Co/M. O arquivo foi inspecionado antes da carga.
    io_ids = call("findNotes", query=(
        'tag:"NEBLI::source_note::1783971980435" '
        'tag:"NEBLI::image_status::approved" note:"IO-one by one (AnKing Step Deck / AnKingMed)"'
    ))
    io_asset = ROOT / "feedback" / "thymus-lobule-cortex-medulla-v2.png"
    if len(io_ids) != 1 or not io_asset.exists():
        raise RuntimeError(f"IO do timo nao esta univoco/pronto: ids={io_ids}, asset={io_asset.exists()}")
    io_raw = io_asset.read_bytes()
    io_media = hashlib.sha256(io_raw).hexdigest()[:32] + ".png"
    actions.append({"action": "storeMediaFile", "params": {
        "filename": io_media, "data": base64.b64encode(io_raw).decode("ascii")}})
    actions.append({"action": "updateNoteFields", "params": {"note": {"id": io_ids[0], "fields": {
        "Image": f'<img src="{io_media}">',
        "I0": "[#!occlusions [[rect0::18,14,26,22]]<br>[[rect0::105,14,20,22]] #]<br>active",
    }}}})
    for n in feedback_now:
        blank = {name: "" for name in ("NEBLI_Comentario", "NEBLI_Resposta")
                 if name in n.get("fields", {}) and n["fields"][name].get("value", "")}
        if blank:
            actions.append({"action": "updateNoteFields", "params": {"note": {"id": n["noteId"], "fields": blank}}})
    if comment_tags:
        actions.append({"action": "removeTags", "params": {"notes": original_feedback,
                                                               "tags": " ".join(comment_tags)}})
    if original_feedback:
        actions.append({"action": "addTags", "params": {"notes": original_feedback,
            "tags": f"NEBLI::feedback_resolved::{STAMP}"}})
    if flag_ids:
        actions.append({"action": "setFlag", "params": {"cards": flag_ids, "flag": 0}})
    if to_suspend:
        actions.append({"action": "suspend", "params": {"cards": sorted(set(to_suspend))}})
    if to_unsuspend:
        actions.append({"action": "unsuspend", "params": {"cards": sorted(set(to_unsuspend))}})

    staging_ids = call("findNotes", query=f'deck:"{STAGING_DECK}"')
    staging_notes = call("notesInfo", notes=staging_ids) if staging_ids else []
    unpromoted = []
    source_ids = []
    staging_sources = {}
    for n in staging_notes:
        source_tag = next((t for t in n.get("tags", []) if t.startswith("NEBLI::source_note::")), None)
        if not source_tag:
            unpromoted.append({"staging": n["noteId"], "reason": "missing_source_tag"})
            continue
        sid = int(source_tag.rsplit("::", 1)[-1])
        source_ids.append(sid)
        staging_sources[n["noteId"]] = sid
    promoted = {n["noteId"]: n for n in call("notesInfo", notes=sorted(set(source_ids)))} if source_ids else {}
    for staging_id, sid in staging_sources.items():
        source = promoted.get(sid)
        if not source or not any(t == f"NEBLI::mutirao_promoted::{STAMP}" for t in source.get("tags", [])):
            unpromoted.append({"staging": staging_id, "source": sid, "reason": "source_not_promoted"})
    if unpromoted:
        raise RuntimeError(f"staging ainda util; promocao incompleta: {unpromoted}")
    if staging_ids:
        actions.append({"action": "deleteNotes", "params": {"notes": staging_ids}})
        actions.append({"action": "deleteDecks", "params": {
            "decks": ["NEBLI::STAGING"], "cardsToo": True}})

    batch_result = call("multi", actions=actions)
    errors = [r for r in batch_result if isinstance(r, dict) and r.get("error")]
    if errors:
        raise RuntimeError(f"falha no lote: {errors}")

    remaining_flags = sorted(set(sum((call("findCards", query=f"tag:NEBLI::* flag:{f}")
                                      for f in range(1, 8)), [])))
    after_feedback = call("notesInfo", notes=original_feedback) if original_feedback else []
    remaining_comments = [n["noteId"] for n in after_feedback
        if n.get("fields", {}).get("NEBLI_Comentario", {}).get("value", "").strip()]
    remaining_staging = call("findNotes", query="tag:NEBLI::staging")
    result = {
        "generated_at": dt.datetime.now().astimezone().isoformat(),
        "status": "complete" if not (remaining_flags or remaining_comments or remaining_staging) else "failed",
        "flags_cleared": len(flag_ids), "comments_closed": len(original_feedback),
        "unsuspended_study_cards": len(set(to_unsuspend)),
        "structural_suspensions_preserved": len(set(to_suspend)),
        "staging_notes_deleted": len(staging_ids),
        "remaining_flags": remaining_flags, "remaining_comments": remaining_comments,
        "remaining_staging": remaining_staging, "batch_actions": len(actions),
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if result["status"] != "complete":
        raise RuntimeError(result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
