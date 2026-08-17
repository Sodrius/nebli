#!/usr/bin/env python3
"""Gate do ganho marginal da aula.

Valida a classificação feita a partir dos materiais atuais + contexto curricular
extraído da planilha mestra. O gate impede que pré-requisitos, revisões,
contexto, exemplos e menções recebam cards.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

CARD_ELIGIBLE_ROLES = {"foco_novo", "relacao_nova", "aprofundamento_novo"}
NON_CARD_ROLES = {"pre_requisito", "revisao", "contexto", "exemplo", "mencao"}
ALL_ROLES = CARD_ELIGIBLE_ROLES | NON_CARD_ROLES
EVIDENCE_SOURCES = {"slide", "e1", "master_sheet"}


def _text(value: Any) -> str:
    return str(value or "").strip()


def _validate_evidence(value: Any, where: str, errors: list[str]) -> list[dict[str, Any]]:
    if not isinstance(value, list) or not value:
        errors.append(f"{where}.teaching_evidence[] obrigatório")
        return []
    valid: list[dict[str, Any]] = []
    for index, raw in enumerate(value):
        if not isinstance(raw, dict):
            errors.append(f"{where}.teaching_evidence[{index}] inválida")
            continue
        source = _text(raw.get("source"))
        locator = _text(raw.get("locator"))
        rationale = _text(raw.get("rationale"))
        if source not in EVIDENCE_SOURCES:
            errors.append(f"{where}.teaching_evidence[{index}].source inválida")
        if len(locator) < 3:
            errors.append(f"{where}.teaching_evidence[{index}].locator obrigatório")
        if len(rationale) < 12:
            errors.append(f"{where}.teaching_evidence[{index}].rationale precisa explicar a função pedagógica")
        if source in EVIDENCE_SOURCES and locator and rationale:
            valid.append(raw)
    return valid


def validate_learning_delta(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    context = data.get("curriculum_context")
    if not isinstance(context, dict):
        errors.append("curriculum_context obrigatório: deve vir da planilha mestra")
        context = {}
    current = context.get("current_lesson")
    if not isinstance(current, dict) or not _text(current.get("title")):
        errors.append("curriculum_context.current_lesson.title obrigatório")
    prior = context.get("prior_lessons")
    if not isinstance(prior, list):
        errors.append("curriculum_context.prior_lessons deve ser lista")
        prior = []
    prior_ids = {_text(row.get("id")) for row in prior if isinstance(row, dict) and _text(row.get("id"))}
    current_id = _text(current.get("id")) if isinstance(current, dict) else ""

    release = data.get("release_gate")
    if not isinstance(release, dict):
        errors.append("release_gate obrigatório")
        release = {}
    review = release.get("learning_delta_review")
    if not isinstance(review, dict):
        errors.append("release_gate.learning_delta_review obrigatório")
        review = {}
    for flag in ("whole_lesson_read_before_cards", "master_sheet_context_used", "claims_classified_before_authorship"):
        if review.get(flag) is not True:
            errors.append(f"learning_delta_review.{flag}=true obrigatório")
    if len(_text(review.get("summary"))) < 20:
        errors.append("learning_delta_review.summary deve resumir o ganho específico da aula")
    materials = review.get("source_materials")
    if not isinstance(materials, list) or not [_text(item) for item in materials if _text(item)]:
        errors.append("learning_delta_review.source_materials[] obrigatório")

    cards = [card for card in data.get("cards", []) if isinstance(card, dict)] if isinstance(data.get("cards"), list) else []
    cards_by_key = {_text(card.get("card_key")): card for card in cards if _text(card.get("card_key"))}
    concepts = release.get("concepts")
    if not isinstance(concepts, list) or not concepts:
        errors.append("release_gate.concepts[] obrigatório")
        concepts = []

    role_by_concept: dict[str, str] = {}
    card_eligible_count = 0
    excluded_count = 0
    for index, row in enumerate(concepts):
        if not isinstance(row, dict):
            continue
        cid = _text(row.get("concept_id")) or f"index:{index}"
        where = f"concept:{cid}"
        role = _text(row.get("learning_role"))
        if role not in ALL_ROLES:
            errors.append(f"{where}.learning_role inválido")
            continue
        role_by_concept[cid] = role
        evidence = _validate_evidence(row.get("teaching_evidence"), where, errors)
        refs = row.get("card_keys")
        refs = refs if isinstance(refs, list) else []
        refs = [_text(ref) for ref in refs if _text(ref)]
        curriculum_ref = _text(row.get("curriculum_ref"))
        allowed_refs = prior_ids | ({current_id} if current_id else set()) | {"baseline"}
        if curriculum_ref and curriculum_ref not in allowed_refs:
            errors.append(f"{where}.curriculum_ref não existe no contexto curricular")

        if role in CARD_ELIGIBLE_ROLES:
            card_eligible_count += 1
            if len(_text(row.get("lesson_gain"))) < 20:
                errors.append(f"{where}.lesson_gain obrigatório para conteúdo novo")
            if not any(_text(item.get("source")) in {"slide", "e1"} for item in evidence):
                errors.append(f"{where} precisa de evidência positiva de ensino no slide/E1")
            if role == "aprofundamento_novo":
                step1 = row.get("step1") if isinstance(row.get("step1"), dict) else {}
                if step1.get("decision") != "incorporated":
                    errors.append(f"{where}: aprofundamento_novo exige step1.decision=incorporated")
        else:
            excluded_count += 1
            if refs:
                errors.append(f"{where}: learning_role={role} não pode ter card_keys")
            if _text(row.get("retention_class")) not in {"e1_only", "derivable"}:
                errors.append(f"{where}: conteúdo de suporte deve ser e1_only|derivable")
            if not _text(row.get("exclusion_reason")):
                errors.append(f"{where}.exclusion_reason obrigatório")

        for ref in refs:
            if ref not in cards_by_key:
                errors.append(f"{where}: card_key inexistente: {ref}")

    for card in cards:
        key = _text(card.get("card_key")) or "?"
        cid = _text(card.get("concept_id"))
        role = role_by_concept.get(cid)
        if role not in CARD_ELIGIBLE_ROLES:
            errors.append(f"card:{key}: concept_id={cid} não representa ganho da aula")

    return {
        "passed": not errors,
        "errors": errors,
        "schema": "nebli-learning-delta-v1",
        "card_eligible_concepts": card_eligible_count,
        "excluded_support_concepts": excluded_count,
        "cards": len(cards),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck_data", type=Path)
    args = parser.parse_args()
    data = json.loads(args.deck_data.read_text(encoding="utf-8"))
    result = validate_learning_delta(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
