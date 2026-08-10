#!/usr/bin/env python3
"""Audit the real exported APKG without Anki or AnkiConnect."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

from apkg_utils import decks_map, media_references, models_map, note_fields, open_collection


CLOZE_RE = re.compile(r"\{\{c(\d+)::(.*?)(?:::[^}]*)?\}\}", re.I)


def _word_count(value: str) -> int:
    clean = re.sub(r"<[^>]+>", " ", value or "")
    return len(re.findall(r"[^\W_]+(?:[-'][^\W_]+)*", clean, flags=re.UNICODE))


def _cloze_source_fields(model: dict, fields: list[str]) -> list[str]:
    """Inspect only fields rendered through Anki's cloze filter.

    AnKing note types contain many auxiliary fields; cloze-like text in an Extra
    field must not be counted as a second retrieval target.
    """
    field_defs = model.get("flds") or []
    names = [str(field.get("name", "")) for field in field_defs]
    templates = " ".join(
        str(template.get(key, ""))
        for template in (model.get("tmpls") or [])
        for key in ("qfmt", "afmt")
    )
    referenced = {
        match.strip().casefold()
        for match in re.findall(r"\{\{cloze:([^}]+)\}\}", templates, flags=re.I)
    }
    indexes = [index for index, name in enumerate(names) if name.casefold() in referenced]
    if not indexes:
        indexes = [
            index for index, name in enumerate(names)
            if name.strip().casefold() in {"text", "front"}
        ]
    if not indexes:
        indexes = [0] if fields else []
    return [fields[index] for index in indexes if index < len(fields)]


def audit(apkg: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    with open_collection(apkg) as (db, package, media_map, member):
        models = models_map(db)
        decks = decks_map(db)
        notes = list(db.execute("SELECT id, guid, mid, tags, flds FROM notes"))
        cards = list(db.execute("SELECT id, nid, did, ord FROM cards"))
        package_names = set(package.namelist())
        filenames = set(media_map.values())
        physical_media = set(media_map.keys())
        missing_physical = sorted(key for key in physical_media if key not in package_names)
        if missing_physical:
            errors.append(f"{len(missing_physical)} entradas do mapa de mídia não existem no ZIP")

        guid_counts = Counter(row["guid"] for row in notes)
        duplicate_guids = sorted(guid for guid, count in guid_counts.items() if count > 1)
        if duplicate_guids:
            errors.append(f"{len(duplicate_guids)} GUIDs de nota duplicados")

        note_ids = {row["id"] for row in notes}
        orphan_cards = [row["id"] for row in cards if row["nid"] not in note_ids]
        if orphan_cards:
            errors.append(f"{len(orphan_cards)} cards sem nota")

        referenced_media: set[str] = set()
        empty_notes = 0
        cloze_notes_without_cloze = 0
        non_atomic_cloze_notes = 0
        cloze_answers_over_limit = 0
        exceptional_three_word_clozes = 0
        io_notes = 0
        nuclear = optional = mixed = 0
        for row in notes:
            fields = note_fields(row["flds"])
            referenced_media.update(media_references(fields))
            if not any(re.sub(r"<[^>]+>", "", field).strip() for field in fields):
                empty_notes += 1
            model = models.get(int(row["mid"]), {})
            model_name = str(model.get("name", ""))
            if "cloze" in model_name.casefold():
                cloze_fields = _cloze_source_fields(model, fields)
                clozes = [match for field in cloze_fields for match in CLOZE_RE.findall(field)]
                if not clozes:
                    cloze_notes_without_cloze += 1
                else:
                    if len(clozes) != 1 or {index for index, _answer in clozes} != {"1"}:
                        non_atomic_cloze_notes += 1
                    for _index, answer in clozes:
                        words = _word_count(answer)
                        cloze_answers_over_limit += int(words > 3)
                        exceptional_three_word_clozes += int(words == 3)
            if "image occlusion" in model_name.casefold() or any("occlusion" in field.casefold() for field in fields):
                io_notes += 1
            tags = set((row["tags"] or "").split())
            has_nuclear = bool(tags & {"nucleo", "núcleo"})
            has_optional = "opcional" in tags
            nuclear += int(has_nuclear)
            optional += int(has_optional)
            mixed += int(has_nuclear and has_optional)

        missing_references = sorted(ref for ref in referenced_media if ref not in filenames)
        if missing_references:
            errors.append(f"{len(missing_references)} referências HTML apontam para mídia ausente")
        if empty_notes:
            errors.append(f"{empty_notes} notas sem conteúdo visível")
        if cloze_notes_without_cloze:
            errors.append(f"{cloze_notes_without_cloze} notas de modelo Cloze não contêm cloze")
        if non_atomic_cloze_notes:
            errors.append(f"{non_atomic_cloze_notes} notas Cloze têm múltiplas recuperações/índices")
        if cloze_answers_over_limit:
            errors.append(f"{cloze_answers_over_limit} respostas de cloze excedem 3 palavras")
        if exceptional_three_word_clozes:
            warnings.append(
                f"{exceptional_three_word_clozes} clozes de 3 palavras exigem justificativa no contrato"
            )
        if mixed:
            errors.append(f"{mixed} notas misturam tags nucleo e opcional")
        unused_media = filenames - referenced_media
        if unused_media:
            warnings.append(f"{len(unused_media)} arquivos de mídia não referenciados")
        if not notes or not cards:
            errors.append("pacote sem notas ou cards")

        return {
            "passed": not errors,
            "package": str(apkg),
            "collection_member": member,
            "notes": len(notes),
            "cards": len(cards),
            "decks": len(decks),
            "models": len(models),
            "image_occlusion_notes": io_notes,
            "non_atomic_cloze_notes": non_atomic_cloze_notes,
            "cloze_answers_over_limit": cloze_answers_over_limit,
            "exceptional_three_word_clozes": exceptional_three_word_clozes,
            "nuclear_notes": nuclear,
            "optional_notes": optional,
            "referenced_media": len(referenced_media),
            "packaged_media": len(filenames),
            "errors": errors,
            "warnings": warnings,
            "samples": {
                "missing_media": missing_references[:20],
                "duplicate_guids": duplicate_guids[:20],
            },
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apkg", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    try:
        result = audit(args.apkg.resolve())
    except Exception as exc:
        result = {"passed": False, "errors": [str(exc)], "warnings": []}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
