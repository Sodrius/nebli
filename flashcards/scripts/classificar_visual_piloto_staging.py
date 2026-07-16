#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica taxonomia visual manual ao piloto de staging."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict

from anki import call


QUERY = "tag:NEBLI::mutirao_piloto"
CONTROL_PREFIXES = ("NEBLI::visual_need::", "NEBLI::image_role::", "NEBLI::image_status::")


def source_id(tags: list[str]) -> int | None:
    for tag in tags:
        if tag.startswith("NEBLI::source_note::"):
            return int(tag.rsplit("::", 1)[-1])
    return None


def classify(note: dict) -> tuple[str, str, str]:
    tags = note.get("tags", [])
    model = note.get("modelName", "")
    sid = source_id(tags)
    if "IO" in model or "Image Occlusion" in model:
        return "required", "recognition", "approved"
    if "NEBLI::source_real::1661651431347" in tags or "NEBLI::source_real::1661651452430" in tags:
        return "required", "recognition", "approved"
    if sid in {1783971579208, 1783971560388, 1783971587557}:
        return "recommended", "comparison", "approved"
    if sid in {1783971760947, 1783971773414, 1783971788011, 1783971790084}:
        return "recommended", "mechanism", "approved"
    if sid in {1783971812959, 1783971990964, 1783971993033}:
        return "recommended", "localization", "approved" if sid == 1783971812959 else "pending_review"
    if sid in {1783811939361, 1783811944451, 1783811944466, 1783811944471, 1783971575038, 1783971602229}:
        return "recommended", "schema", "missing"
    if sid in {1783811939294, 1783971957137, 1783971961342}:
        return "none", "none", "missing"
    return "optional", "context", "missing"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", default=QUERY)
    parser.add_argument("--output")
    args = parser.parse_args()
    ids = call("findNotes", query=args.query)
    notes = call("notesInfo", notes=ids)
    add_groups = defaultdict(list)
    remove_groups = defaultdict(list)
    rows = []
    for note in notes:
        need, role, status = classify(note)
        nid = note["noteId"]
        for tag in note.get("tags", []):
            if tag.startswith(CONTROL_PREFIXES):
                remove_groups[tag].append(nid)
        for tag in (f"NEBLI::visual_need::{need}", f"NEBLI::image_role::{role}", f"NEBLI::image_status::{status}"):
            add_groups[tag].append(nid)
        rows.append({"note_id": nid, "source_note_id": source_id(note.get("tags", [])), "visual_need": need, "image_role": role, "image_status": status})
    for tag, note_ids in remove_groups.items():
        call("removeTags", notes=note_ids, tags=tag)
    for tag, note_ids in add_groups.items():
        call("addTags", notes=note_ids, tags=tag)
    payload = json.dumps(rows, ensure_ascii=False, indent=2)
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
