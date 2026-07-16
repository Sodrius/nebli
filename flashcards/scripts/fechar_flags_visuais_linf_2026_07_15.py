#!/usr/bin/env python3
"""Resolve duas flags novas, corrige o card visual de elastica e restaura controles."""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anki import call

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "arquivos-trabalho" / "mutirao-qualidade" / "feedback"
NOTES = [1783971579208, 1783971990964, 1783971993033]
FLAG_CARDS = [1783971990965, 1783971993033]
GREEN_SIBLINGS = [1783971560389, 1783971560390]


def reviewer_card():
    try:
        return call("guiCurrentCard")
    except RuntimeError as exc:
        if "not currently active" in str(exc):
            return None
        raise


def normalized(tags, role):
    drop = ("img::", "NEBLI::image_status::", "NEBLI::image_role::", "NEBLI::visual_need::")
    kept = [t for t in tags if not t.startswith(drop) and t != "NEBLI::needs_image"]
    kept += ["NEBLI::image_extra", "NEBLI::image_status::approved",
             f"NEBLI::image_role::{role}", "NEBLI::visual_need::recommended",
             "NEBLI::feedback_resolved::2026-07-15"]
    return sorted(set(kept))


def main():
    if current := reviewer_card():
        raise SystemExit(f"Reviewer ativo no card {current.get('cardId')}; lote adiado")
    notes = call("notesInfo", notes=NOTES)
    by_id = {n["noteId"]: n for n in notes}
    cards = call("cardsInfo", cards=FLAG_CARDS + GREEN_SIBLINGS)
    OUT.mkdir(parents=True, exist_ok=True)
    ledger = {
        "generated_at": dt.datetime.now().astimezone().isoformat(),
        "notes_before": [{"note_id": n["noteId"], "fields": {k: v["value"] for k, v in n["fields"].items()},
                          "tags": n.get("tags", [])} for n in notes],
        "cards_before": [{k: c.get(k) for k in ("cardId", "note", "ord", "queue", "type", "due",
                           "interval", "factor", "reps", "lapses", "left", "flags")} for c in cards],
    }
    path = OUT / "LEDGER-FLAGS-VISUAIS-LINF-2026-07-15.json"
    path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    repairs = {
        1783971579208: {
            "Text": "The tunica media of an elastic artery contains numerous concentric {{c1::elastic lamellae}}.",
            "Extra": ('Elastic lamellae store energy during systole and recoil during diastole, smoothing pulsatile flow.'
                      '<br><br><img src="paste-065224c731df26128c670de194d94627984c751e.png">'
                      '<br><i style="font-size:10pt;">Magnified elastic artery from imported Histology/LLU deck.</i>'),
            "role": "recognition",
        },
        1783971990964: {
            "Text": "The organ that filters lymph and receives many afferent but one efferent lymphatic vessel is the {{c1::lymph node}}.",
            "Extra": ('Lymph enters along the convex surface, crosses subcapsular and medullary sinuses, and exits at the hilum; the spleen filters blood.'
                      '<br><br><img src="a10fc17517aad74736e4bb8bd3204683.webp">'
                      '<br><i style="font-size:10pt;">Lymph-node flow diagram from imported Histology deck.</i>'),
            "role": "context",
        },
        1783971993033: {
            "Text": "B-cell follicles occupy the {{c1::cortex}} of a lymph node.",
            "Extra": ('The paracortex is predominantly T-cell territory; cortical nodules/follicles are B-cell zones.'
                      '<br><br><img src="4fec3b7870196676ce8e6557f443ef44.webp">'
                      '<br><i style="font-size:10pt;">Lymph-node cortex micrograph from imported Histology deck.</i>'),
            "role": "recognition",
        },
    }
    actions = []
    for nid, item in repairs.items():
        note = by_id[nid]
        actions.append({"action": "updateNoteFields", "params": {"note": {"id": nid,
            "fields": {"Text": item["Text"], "Extra": item["Extra"]}}}})
        old, new = set(note.get("tags", [])), set(normalized(note.get("tags", []), item["role"]))
        if old - new:
            actions.append({"action": "removeTags", "params": {"notes": [nid], "tags": " ".join(sorted(old-new))}})
        if new - old:
            actions.append({"action": "addTags", "params": {"notes": [nid], "tags": " ".join(sorted(new-old))}})
    suspended_green = [c["cardId"] for c in cards if c.get("cardId") in GREEN_SIBLINGS and c.get("queue") == -1]
    if suspended_green:
        actions.append({"action": "unsuspend", "params": {"cards": suspended_green}})
    if current := reviewer_card():
        raise SystemExit(f"Reviewer abriu no card {current.get('cardId')}; zero mutacoes aplicadas")
    result = call("multi", actions=actions)
    if errors := [x for x in result if isinstance(x, dict) and x.get("error")]:
        raise RuntimeError(errors)
    # Esta instalacao nao expoe setFlag; o setter inteiro foi verificado aqui.
    for cid in FLAG_CARDS:
        call("setSpecificValueOfCard", card=cid, keys=["flags"], newValues=[0], warning_check=True)
    after_cards = call("cardsInfo", cards=FLAG_CARDS + GREEN_SIBLINGS)
    post = {
        "completed_at": dt.datetime.now().astimezone().isoformat(),
        "flags_remaining": [c["cardId"] for c in after_cards if c.get("cardId") in FLAG_CARDS and c.get("flags")],
        "green_siblings_suspended": [c["cardId"] for c in after_cards if c.get("cardId") in GREEN_SIBLINGS and c.get("queue") == -1],
        "actions": len(actions),
    }
    ledger["postcheck"] = post
    path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if post["flags_remaining"] or post["green_siblings_suspended"]:
        raise RuntimeError(post)
    print(json.dumps(post, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
