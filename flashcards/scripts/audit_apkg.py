#!/usr/bin/env python3
"""Audita o APKG v13 real, offline e no escopo exato do deck NEBLI."""
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
FEEDBACK_FIELDS = ("NEBLI_Comentario", "NEBLI_Resposta", "NEBLI_Historico")


def _field_by_name(names: list[str], fields: list[str], wanted: str) -> str:
    for index, name in enumerate(names):
        if name.casefold() == wanted.casefold() and index < len(fields):
            return fields[index] or ""
    return ""


def _word_count(value: str) -> int:
    clean = re.sub(r"<[^>]+>", " ", value or "")
    return len(re.findall(r"[^\W_]+(?:[-'][^\W_]+)*", clean, flags=re.UNICODE))


def _cloze_source_fields(model: dict, fields: list[str]) -> list[str]:
    names = [str(field.get("name", "")) for field in (model.get("flds") or [])]
    templates = " ".join(str(template.get(key, "")) for template in (model.get("tmpls") or []) for key in ("qfmt", "afmt"))
    referenced = {match.strip().casefold() for match in re.findall(r"\{\{cloze:([^}]+)\}\}", templates, flags=re.I)}
    indexes = [index for index, name in enumerate(names) if name.casefold() in referenced]
    if not indexes:
        indexes = [index for index, name in enumerate(names) if name.strip().casefold() in {"text", "front"}]
    if not indexes and fields:
        indexes = [0]
    return [fields[index] for index in indexes if index < len(fields)]


def _deck_display(name: str) -> str:
    return (name or "").replace("\x1f", "::")


def _notes_in_deck(db, decks: dict, deck: str) -> set[int] | None:
    if not deck:
        return None
    wanted = {
        int(did) for did, value in decks.items()
        if (_deck_display(str((value or {}).get("name", ""))) == deck
            or _deck_display(str((value or {}).get("name", ""))).startswith(deck + "::"))
    }
    if not wanted:
        raise ValueError(f"deck não encontrado no pacote: {deck}")
    return {int(row["nid"]) for row in db.execute("SELECT nid, did FROM cards") if int(row["did"]) in wanted}


def audit(apkg: Path, deck: str = "") -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    with open_collection(apkg) as (db, package, media_map, member):
        models = models_map(db); decks = decks_map(db); scope = _notes_in_deck(db, decks, deck)
        notes = list(db.execute("SELECT id, guid, mid, tags, flds FROM notes")); cards = list(db.execute("SELECT id, nid, did, ord FROM cards"))
        if scope is not None:
            notes = [row for row in notes if int(row["id"]) in scope]; cards = [row for row in cards if int(row["nid"]) in scope]
        if not notes or not cards:
            errors.append("pacote/deck sem notas ou cards")

        package_names = set(package.namelist()); filenames = set(media_map.values())
        missing_physical = sorted(key for key in media_map if key not in package_names)
        if missing_physical:
            errors.append(f"{len(missing_physical)} entradas do mapa de mídia não existem no ZIP")
        guid_counts = Counter(row["guid"] for row in notes); duplicate_guids = sorted(guid for guid,count in guid_counts.items() if count > 1)
        if duplicate_guids:
            errors.append(f"{len(duplicate_guids)} GUIDs de nota duplicados")
        note_ids = {int(row["id"]) for row in notes}; orphan = [row["id"] for row in cards if int(row["nid"]) not in note_ids]
        if orphan:
            errors.append(f"{len(orphan)} cards sem nota")

        referenced_media: set[str] = set(); answer_index: dict[str, list[tuple[int,str]]] = {}; comments = []
        empty_notes = non_atomic = over_limit = three_words = io_notes = 0
        nuclear = optional = mixed = english = generic = no_tier = no_concept = no_feedback = io_source_leak = io_answer_repeat = 0

        for row in notes:
            fields = note_fields(row["flds"]); referenced_media.update(media_references(fields)); model = models.get(int(row["mid"]), {})
            names = [str(field.get("name", "")) for field in (model.get("flds") or [])]; model_name = str(model.get("name", ""))
            if not any(re.sub(r"<[^>]+>", "", field).strip() for field in fields): empty_notes += 1
            tags = set((row["tags"] or "").split()); has_nuclear = "nucleo" in tags or "núcleo" in tags; has_optional = "opcional" in tags
            nuclear += int(has_nuclear); optional += int(has_optional); mixed += int(has_nuclear and has_optional)
            nebli = any(tag.startswith("NEBLI::") for tag in tags)
            if nebli:
                if not any(tag.startswith("NEBLI::tier::") for tag in tags): no_tier += 1
                if not any(tag.startswith("NEBLI::concept::") for tag in tags): no_concept += 1
                lowered = {name.casefold() for name in names}
                if not all(field.casefold() in lowered for field in FEEDBACK_FIELDS): no_feedback += 1
            comment = _field_by_name(names, fields, "NEBLI_Comentario")
            if comment.strip(): comments.append({"note_id": int(row["id"]), "comment": re.sub(r"<[^>]+>", " ", comment).strip()[:200]})

            cloze_fields = _cloze_source_fields(model, fields); clozes = [match for field in cloze_fields for match in CLOZE_RE.findall(field)]
            is_cloze = bool(clozes) or "cloze" in model_name.casefold()
            if is_cloze:
                if len(clozes) != 1 or {index for index,_ in clozes} != {"1"}: non_atomic += 1
                front = " ".join(cloze_fields)
                if portuguese_front_failures(front, "pt-BR"): english += 1
                if abstract_answer_failures(front): generic += 1
                rationale = _field_by_name(names, fields, "DerivationRationale")
                for _index, answer in clozes:
                    words = _word_count(answer); over_limit += int(words > 3); three_words += int(words == 3)
                    key = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", answer)).strip().casefold()
                    if key: answer_index.setdefault(key, []).append((int(row["id"]), rationale.strip()))

            if "image occlusion" in model_name.casefold():
                io_notes += 1; answer_field = _field_by_name(names, fields, "Answer"); source_field = _field_by_name(names, fields, "Source")
                plain_answer = re.sub(r"<[^>]+>", "", answer_field)
                if source_field.strip() and source_field.strip() in plain_answer: io_source_leak += 1
                if "nebli-io-answers" in answer_field: io_answer_repeat += 1

        missing_refs = sorted(ref for ref in referenced_media if ref not in filenames)
        if missing_refs: errors.append(f"{len(missing_refs)} referências HTML apontam para mídia ausente")
        if empty_notes: errors.append(f"{empty_notes} notas sem conteúdo visível")
        if non_atomic: errors.append(f"{non_atomic} notas Cloze têm múltiplas recuperações/índices")
        if over_limit: errors.append(f"{over_limit} respostas de cloze excedem 3 palavras")
        if three_words: warnings.append(f"{three_words} clozes de 3 palavras: justificativa deve ter sido validada antes do empacotamento")
        if mixed: errors.append(f"{mixed} notas misturam tags nucleo e opcional")
        if english: errors.append(f"{english} frentes não estão em português")
        if generic: errors.append(f"{generic} clozes têm resposta abstrata")

        duplicate_answers = {answer: rows for answer,rows in answer_index.items() if len(rows)>1}
        unjustified = {answer: rows for answer,rows in duplicate_answers.items() if any(len(reason)<12 for _nid,reason in rows)}
        justified = {answer: rows for answer,rows in duplicate_answers.items() if answer not in unjustified}
        if unjustified: errors.append(f"{len(unjustified)} respostas duplicadas sem derivation_rationale em todos os cards")
        if justified: warnings.append(f"{len(justified)} respostas duplicadas justificadas por recuperações distintas")
        if io_answer_repeat: errors.append(f"{io_answer_repeat} cards IO repetem a resposta abaixo da imagem")
        if io_source_leak: errors.append(f"{io_source_leak} cards IO imprimem o crédito na resposta")
        if no_tier: errors.append(f"{no_tier} notas sem tag NEBLI::tier")
        if no_concept: errors.append(f"{no_concept} notas sem tag NEBLI::concept")
        if no_feedback: errors.append(f"{no_feedback} notas sem os três campos de feedback NEBLI")
        if comments: warnings.append(f"{len(comments)} notas com comentário do usuário")
        unused = filenames - referenced_media
        if unused: warnings.append(f"{len(unused)} arquivos de mídia não referenciados")

        return {
            "passed": not errors, "package": str(apkg), "deck": deck or "(coleção inteira)", "collection_member": member,
            "notes": len(notes), "cards": len(cards), "decks": len(decks), "models": len(models), "image_occlusion_notes": io_notes,
            "non_atomic_cloze_notes": non_atomic, "cloze_answers_over_limit": over_limit, "exceptional_three_word_clozes": three_words,
            "nuclear_notes": nuclear, "optional_notes": optional, "english_fronts": english, "generic_clozes": generic,
            "duplicate_answers": len(duplicate_answers), "justified_duplicate_answers": len(justified), "unjustified_duplicate_answers": len(unjustified),
            "io_answer_repeated": io_answer_repeat, "io_source_in_answer": io_source_leak, "notes_without_tier": no_tier,
            "notes_without_concept": no_concept, "notes_without_feedback_field": no_feedback, "pending_comments": len(comments),
            "visually_dependent_fraction": round(io_notes/len(notes),3) if notes else 0.0, "referenced_media": len(referenced_media), "packaged_media": len(filenames),
            "errors": errors, "warnings": warnings,
            "samples": {"missing_media": missing_refs[:20], "duplicate_guids": duplicate_guids[:20], "unjustified_duplicate_answers": dict(list(unjustified.items())[:20]), "comments": comments[:20]}
        }


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("apkg",type=Path); parser.add_argument("--deck",default=""); parser.add_argument("--json-out",type=Path); args=parser.parse_args()
    try: result=audit(args.apkg.resolve(),args.deck)
    except Exception as exc: result={"passed":False,"errors":[str(exc)],"warnings":[]}
    rendered=json.dumps(result,ensure_ascii=False,indent=2); print(rendered)
    if args.json_out: args.json_out.parent.mkdir(parents=True,exist_ok=True); args.json_out.write_text(rendered+"\n",encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__=="__main__": sys.exit(main())
