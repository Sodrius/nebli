#!/usr/bin/env python3
"""Dosagem curada dos 10 plates Dope/Anatomy da P3.

Mantém três alvos nucleares por plate (quatro no mapa fetal) e suspende,
sem apagar, os demais cards. A seleção foi feita após inspeção do plate e dos
rótulos, não por posição automática.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

from nebli_anki import call


KEEP = {
    1783972283469: [1, 4, 7],   # RCA, coronary sinus, LAD
    1783972285540: [3, 4, 7],   # SVC, pericardium, aortic arch
    1783972287626: [4, 6, 9],   # SVC, pulmonary trunk, aortic arch
    1783972289693: [2, 3, 5],   # aortic valve, IV septum, fossa ovalis
    1783972291783: [1, 3, 4],   # SVC, fossa ovalis, IVC
    1783972293854: [1, 2, 5],   # tricuspid, chordae, moderator band
    1783972295935: [2, 3, 7],   # aortic, mitral, tricuspid valves
    1783972595204: [6, 7, 8],   # thoracic aorta, bronchial artery, arch
    1783972597290: [2, 3, 9],   # SVC, azygos, hemiazygos
    1783972599369: [1, 2, 3, 4],  # three fetal shunts + umbilical vein
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    notes = {n["noteId"]: n for n in call("notesInfo", notes=list(KEEP))}
    rows, to_suspend = [], []
    for nid, keep_fields in KEEP.items():
        note = notes[nid]
        cards = call("cardsInfo", cards=call("findCards", query=f"nid:{nid}"))
        card_rows = []
        for card in cards:
            field_no = card["ord"] + 1
            label = note["fields"].get(f"{field_no}a", {}).get("value", "")
            keep = field_no in keep_fields
            card_rows.append({"card_id": card["cardId"], "field_no": field_no,
                              "label": label, "keep": keep, "queue_before": card["queue"]})
            if not keep and card["queue"] != -1:
                to_suspend.append(card["cardId"])
        rows.append({"note_id": nid, "title": note["fields"]["Title"]["value"],
                     "kept_fields": keep_fields, "cards": card_rows})
    if to_suspend:
        call("suspend", cards=to_suspend)
    for nid, fields in KEEP.items():
        call("addTags", notes=[nid], tags=(
            f"NEBLI::io_curated::2026-07-15 NEBLI::io_target_count::{len(fields)} "
            "NEBLI::visual_gate::required NEBLI::visual_need::required "
            "NEBLI::image_role::recognition NEBLI::image_status::approved"
        ))
    payload = {"generated_at": dt.datetime.now().astimezone().isoformat(),
               "rule": "semantic manual selection; 3 targets per plate, 4 for fetal circulation",
               "suspended_card_ids": to_suspend, "notes": rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"notes": len(rows), "kept": sum(len(v) for v in KEEP.values()),
                      "newly_suspended": len(to_suspend)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
