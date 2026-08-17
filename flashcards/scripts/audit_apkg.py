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
from card_cue_quality import abstract_answer_failures, portuguese_front_failures


CLOZE_RE = re.compile(r"\{\{c(\d+)::(.*?)(?:::[^}]*)?\}\}", re.I)

FEEDBACK_FIELDS = ("NEBLI_Comentario", "NEBLI_Resposta")


def ModelFields_supportsFeedback(names: list[str]) -> bool:
    """Espelha ModelFields.supportsFeedback do Companion."""
    lowered = {name.casefold() for name in names}
    return all(field.casefold() in lowered for field in FEEDBACK_FIELDS)


def _field_by_name(names: list[str], fields: list[str], wanted: str) -> str:
    for index, name in enumerate(names):
        if name.casefold() == wanted.casefold() and index < len(fields):
            return fields[index] or ""
    return ""


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


def _deck_display(name: str) -> str:
    return (name or "").replace("\x1f", "::")


def _notes_in_deck(db, decks: dict, deck: str) -> set[int] | None:
    """Ids de nota cujos cards vivem no deck alvo ou num subdeck dele.

    Sem isso a auditoria olha a coleção inteira: no `.apkg` de 2026-08-17, as 149
    notas da prova ficavam diluídas em 547, e o relatório dizia "aprovado".
    """
    if not deck:
        return None
    wanted = set()
    for did, value in decks.items():
        # decks_map devolve o objeto do deck, não o nome cru.
        name = _deck_display(str((value or {}).get("name", "")))
        if name == deck or name.startswith(deck + "::"):
            wanted.add(int(did))
    if not wanted:
        raise ValueError(f"deck não encontrado no pacote: {deck}")
    return {int(row["nid"]) for row in db.execute("SELECT nid, did FROM cards") if int(row["did"]) in wanted}


def audit(apkg: Path, deck: str = "") -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    with open_collection(apkg) as (db, package, media_map, member):
        models = models_map(db)
        decks = decks_map(db)
        scope = _notes_in_deck(db, decks, deck)
        notes = list(db.execute("SELECT id, guid, mid, tags, flds FROM notes"))
        cards = list(db.execute("SELECT id, nid, did, ord FROM cards"))
        if scope is not None:
            notes = [row for row in notes if int(row["id"]) in scope]
            cards = [row for row in cards if int(row["nid"]) in scope]
            if not notes:
                errors.append(f"deck sem notas: {deck}")
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
        without_tier = without_concept = without_feedback_field = 0
        english_fronts = generic_clozes = io_source_in_answer = io_answer_repeated = 0
        comments: list[dict] = []
        answer_index: dict[str, list[int]] = {}
        for row in notes:
            fields = note_fields(row["flds"])
            referenced_media.update(media_references(fields))
            if not any(re.sub(r"<[^>]+>", "", field).strip() for field in fields):
                empty_notes += 1
            model = models.get(int(row["mid"]), {})
            model_name = str(model.get("name", ""))
            cloze_fields = _cloze_source_fields(model, fields)
            # O nome do note type não diz se a nota é cloze: o modelo usado pelo
            # deck chama-se "AnKingOverhaul" e não contém a palavra "cloze".
            # Quem decide é o conteúdo.
            is_cloze = any(CLOZE_RE.search(field or "") for field in cloze_fields)
            if is_cloze or "cloze" in model_name.casefold():
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

            # --- qualidade do card, não só integridade do pacote --------------
            names = [str(field.get("name", "")) for field in (model.get("flds") or [])]
            # Identidade só é exigida de nota instalada pelo NEBLI: uma nota
            # importada de outra origem não deve ser julgada por este contrato.
            nebli_note = any(tag.startswith("NEBLI::") for tag in tags)
            if nebli_note:
                if not any(tag.startswith("NEBLI::tier::") for tag in tags): without_tier += 1
                if not any(tag.startswith("NEBLI::concept::") for tag in tags): without_concept += 1
                if not ModelFields_supportsFeedback(names): without_feedback_field += 1
            comment = _field_by_name(names, fields, "NEBLI_Comentario")
            if comment.strip(): comments.append({"note_id": int(row["id"]), "comment": re.sub(r"<[^>]+>", " ", comment).strip()[:200]})
            if is_cloze:
                front = " ".join(cloze_fields)
                if portuguese_front_failures(front, "pt-BR"): english_fronts += 1
                if abstract_answer_failures(front): generic_clozes += 1
                for _index, answer in CLOZE_RE.findall(front):
                    key = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", answer)).strip().casefold()
                    if key: answer_index.setdefault(key, []).append(int(row["id"]))
            if "image occlusion" in model_name.casefold():
                answer_field = _field_by_name(names, fields, "Answer")
                source_field = _field_by_name(names, fields, "Source")
                plain_answer = re.sub(r"<[^>]+>", "", answer_field)
                if source_field.strip() and source_field.strip() in plain_answer: io_source_in_answer += 1
                if "nebli-io-answers" in answer_field: io_answer_repeated += 1

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
        duplicate_answers = {answer: ids for answer, ids in answer_index.items() if len(ids) > 1}
        if english_fronts:
            errors.append(f"{english_fronts} frentes não estão em português")
        if generic_clozes:
            errors.append(f"{generic_clozes} clozes têm resposta abstrata")
        if duplicate_answers:
            errors.append(f"{len(duplicate_answers)} respostas de cloze aparecem em mais de um card")
        if io_answer_repeated:
            errors.append(f"{io_answer_repeated} cards IO repetem a resposta abaixo da imagem")
        if io_source_in_answer:
            errors.append(f"{io_source_in_answer} cards IO imprimem o crédito na resposta")
        if without_tier:
            errors.append(f"{without_tier} notas sem tag NEBLI::tier")
        if without_concept:
            errors.append(f"{without_concept} notas sem tag NEBLI::concept")
        if without_feedback_field:
            warnings.append(f"{without_feedback_field} notas em note type sem campo de comentário")
        if comments:
            warnings.append(f"{len(comments)} notas com comentário do usuário a responder")
        unused_media = filenames - referenced_media
        if unused_media:
            warnings.append(f"{len(unused_media)} arquivos de mídia não referenciados")
        if not notes or not cards:
            errors.append("pacote sem notas ou cards")

        return {
            "passed": not errors,
            "package": str(apkg),
            "deck": deck or "(coleção inteira)",
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
            "english_fronts": english_fronts,
            "generic_clozes": generic_clozes,
            "duplicate_answers": len(duplicate_answers),
            "io_answer_repeated": io_answer_repeated,
            "io_source_in_answer": io_source_in_answer,
            "notes_without_tier": without_tier,
            "notes_without_concept": without_concept,
            "notes_without_feedback_field": without_feedback_field,
            "pending_comments": len(comments),
            "visually_dependent_fraction": round(io_notes / len(notes), 3) if notes else 0.0,
            "referenced_media": len(referenced_media),
            "packaged_media": len(filenames),
            "errors": errors,
            "warnings": warnings,
            "samples": {
                "missing_media": missing_references[:20],
                "duplicate_guids": duplicate_guids[:20],
                "duplicate_answers": dict(list(duplicate_answers.items())[:20]),
                "comments": comments[:20],
            },
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apkg", type=Path)
    parser.add_argument("--deck", default="", help='deck alvo, ex.: "NEBLI::UC03::P1::Patologia::Ferramentas"')
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    try:
        result = audit(args.apkg.resolve(), args.deck)
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
