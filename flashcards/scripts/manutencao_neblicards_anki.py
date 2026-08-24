#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Manutencao dos NEBLIcards ja existentes no Anki.

Faz duas coisas seguras:
  1. Remove "Source/Fonte" visivel de NEBLIcards autorais, preservando creditos
     de imagem do tipo "Photo credit:".
  2. Marca cards autorais sem imagem em campos visuais com NEBLI::needs_image,
     e os com imagem com NEBLI::image_extra.

Uso:
  python flashcards/scripts/manutencao_neblicards_anki.py --dry-run
  python flashcards/scripts/manutencao_neblicards_anki.py --apply
"""
import argparse
import re
import sys

from nebli_anki import call

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

QUERY = '(tag:NEBLI::neblicard-autoral OR tag:NEBLI::gerado)'
SOURCE_FIELDS = {"Source", "Sources", "source", "sources", "Fonte", "Fontes"}
NEEDS = "NEBLI::needs_image"
HASIMG = "NEBLI::image_extra"


def strip_source_lines(html):
    if not html:
        return html
    # Preserve real image credits; remove provenance/source labels that show
    # manufacturing rather than image attribution.
    lines = re.split(r"(<br\s*/?>|\n)", html)
    out = []
    skip_next_sep = False
    for part in lines:
        plain = re.sub(r"<[^>]+>", " ", part)
        low = plain.strip().lower()
        is_source = (
            re.match(r"^(source|sources|fonte|fontes)\s*[:\-]", low)
            and "photo credit" not in low
            and "image licensed" not in low
            and "cc by" not in low
        )
        if is_source:
            skip_next_sep = True
            continue
        if skip_next_sep and re.match(r"^(<br\s*/?>|\n)$", part):
            skip_next_sep = False
            continue
        skip_next_sep = False
        out.append(part)
    return "".join(out).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not args.apply and not args.dry_run:
        args.dry_run = True

    ids = call("findNotes", query=QUERY)
    print(f"NEBLIcards autorais/gerados: {len(ids)}")
    changed_fields = 0
    has_img, needs_img = [], []
    cleared_source_fields = 0

    for n in call("notesInfo", notes=ids):
        nid = n["noteId"]
        fields = n.get("fields", {})
        updates = {}

        for name, val in fields.items():
            raw = val.get("value", "")
            if name in SOURCE_FIELDS and raw.strip():
                updates[name] = ""
                cleared_source_fields += 1
                continue
            cleaned = strip_source_lines(raw)
            if cleaned != raw:
                updates[name] = cleaned

        image_html = " ".join(
            val.get("value", "")
            for name, val in fields.items()
            if name.lower() in {"extra", "image", "imagem", "occludedimage", "remarks"}
        )
        if "<img" in image_html.lower():
            has_img.append(nid)
        else:
            needs_img.append(nid)

        if updates:
            changed_fields += 1
            if args.apply:
                call("updateNoteFields", note={"id": nid, "fields": updates})

    if args.apply:
        if has_img:
            call("addTags", notes=has_img, tags=HASIMG)
            call("removeTags", notes=has_img, tags=NEEDS)
        if needs_img:
            call("addTags", notes=needs_img, tags=NEEDS)
            call("removeTags", notes=needs_img, tags=HASIMG)

    print(f"notes com campos/source visivel a limpar: {changed_fields}")
    print(f"campos Source/Sources/Fonte zerados: {cleared_source_fields}")
    print(f"com imagem no Extra: {len(has_img)}")
    print(f"sem imagem no Extra -> {NEEDS}: {len(needs_img)}")
    print("modo:", "apply" if args.apply else "dry-run")


if __name__ == "__main__":
    main()
