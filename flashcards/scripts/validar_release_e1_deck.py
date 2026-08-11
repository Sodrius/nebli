#!/usr/bin/env python3
"""Hard gate semântico/estrutural da entrega canônica E1 + Deck-Aula.

O gate liga o arquivo final do deck à E1 realmente revisada. Assim, um lote
card-a-card válido não consegue esconder uma lacuna nuclear, uma E1 rasa ou um
aprofundamento Step 1 sem âncora.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


SCHEMA = "nebli-e1-deck-release-v1"
# docs/canon/SELECAO-DE-CARDS.md §2: o teto sai do que a aula cobra, não do porte.
CARDS_PER_OBJECTIVE = 4
BUDGET_FLOOR = 12
BUDGET_CEILING = 32
REVIEW_FLAGS = (
    "slide_inventory_complete",
    "objectives_covered",
    "core_coverage_complete",
    "mechanisms_explicit",
    "visual_information_explained",
    "core_study_without_slides",
    "step1_depth_reviewed",
    "card_content_anchored",
    "independent_review_passed",
)


def _normalise(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = re.sub(r"#(?:sigla|termo-nota)\([^)]*\)", " ", value)
    value = re.sub(r"[#*_`\[\]{}()]", " ", value)
    return re.sub(r"\s+", " ", value).strip().casefold()


def _resolve(base: Path, raw: Any) -> Path:
    path = Path(str(raw or ""))
    return path if path.is_absolute() else (base / path).resolve()


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_release(data: dict[str, Any], deck_data_path: Path) -> dict[str, Any]:
    errors: list[str] = []
    release = data.get("release_gate")
    if not isinstance(release, dict):
        return {"passed": False, "errors": ["release_gate obrigatório no pipeline canônico"]}
    if release.get("schema") != SCHEMA:
        errors.append(f"release_gate.schema deve ser {SCHEMA}")

    base = deck_data_path.parent.resolve()
    source_path = _resolve(base, release.get("e1_source"))
    pdf_path = _resolve(base, release.get("e1_pdf"))
    source_text = ""
    for label, path, hash_key in (
        ("e1_source", source_path, "e1_source_sha256"),
        ("e1_pdf", pdf_path, "e1_pdf_sha256"),
    ):
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"{label} inexistente ou vazio: {release.get(label, '')}")
            continue
        expected = str(release.get(hash_key) or "").strip()
        if not expected:
            errors.append(f"{hash_key} obrigatório")
        elif expected != _sha256(path):
            errors.append(f"{hash_key} diverge do artefato revisado")
        if label == "e1_source":
            source_text = _normalise(path.read_text(encoding="utf-8-sig"))

    review = release.get("e1_review")
    if not isinstance(review, dict):
        errors.append("e1_review obrigatório")
        review = {}
    for flag in REVIEW_FLAGS:
        if review.get(flag) is not True:
            errors.append(f"e1_review.{flag}=true é obrigatório")
    if review.get("notes_review_status") not in {"covered", "unavailable"}:
        errors.append("e1_review.notes_review_status deve ser covered|unavailable")
    if not str(review.get("summary") or "").strip():
        errors.append("e1_review.summary obrigatório")
    for key in ("unresolved_core_omissions", "unresolved_ambiguities"):
        value = review.get(key)
        if not isinstance(value, list):
            errors.append(f"e1_review.{key} deve ser lista")
        elif value:
            errors.append(f"e1_review.{key} precisa estar vazio para liberar")

    cards = data.get("cards") if isinstance(data.get("cards"), list) else []
    card_keys = {
        str(card.get("card_key") or "").strip()
        for card in cards if isinstance(card, dict) and str(card.get("card_key") or "").strip()
    }
    hard_max = release.get("card_budget_hard_max")
    if not isinstance(hard_max, int) or isinstance(hard_max, bool) or hard_max < 1:
        errors.append("release_gate.card_budget_hard_max deve ser inteiro positivo")
        hard_max = 0
    elif len(cards) > hard_max:
        errors.append(f"deck tem {len(cards)} cards e excede hard_max={hard_max}")

    objectives = release.get("objective_count")
    per_objective = release.get("cards_per_objective", CARDS_PER_OBJECTIVE)
    if not isinstance(objectives, int) or isinstance(objectives, bool) or objectives < 1:
        errors.append("release_gate.objective_count deve ser inteiro positivo")
    elif isinstance(per_objective, int) and not isinstance(per_objective, bool) and per_objective > 0:
        derived = max(BUDGET_FLOOR, min(BUDGET_CEILING, per_objective * objectives))
        if isinstance(hard_max, int) and hard_max > derived:
            errors.append(
                f"card_budget_hard_max={hard_max} excede o teto derivado dos objetivos ({derived})"
            )
    else:
        errors.append("release_gate.cards_per_objective inválido")

    enrichment = [
        card for card in cards
        if isinstance(card, dict) and card.get("step1_enrichment") is True
    ]
    if cards and len(enrichment) * 4 > len(cards):
        errors.append(
            f"cards de aprofundamento Step 1 ({len(enrichment)}) excedem 1/4 do deck ({len(cards)})"
        )

    concepts = release.get("concepts")
    if not isinstance(concepts, list) or not concepts:
        errors.append("release_gate.concepts[] obrigatório e não vazio")
        concepts = []
    seen_concepts: set[str] = set()
    referenced_cards: set[str] = set()
    nuclear = covered_nuclear = 0
    importance_by_concept: dict[str, str] = {}
    for row in concepts:
        if not isinstance(row, dict):
            errors.append("release_gate.concepts contém item não-objeto")
            continue
        cid = str(row.get("concept_id") or "").strip()
        if not cid or cid in seen_concepts:
            errors.append(f"concept_id ausente/duplicado: {cid or '?'}")
        seen_concepts.add(cid)
        importance = str(row.get("importance") or "").lower()
        if importance not in {"nuclear", "supporting", "optional"}:
            errors.append(f"{cid}: importance inválido")
        importance_by_concept[cid] = importance
        if importance == "nuclear":
            nuclear += 1
        anchor = str(row.get("e1_anchor") or "").strip()
        if not anchor or (source_text and _normalise(anchor) not in source_text):
            errors.append(f"{cid}: âncora literal ausente da E1 revisada")
        quality = row.get("coverage_quality")
        minimum = 2 if importance == "nuclear" else 1
        if not isinstance(quality, int) or isinstance(quality, bool) or quality < minimum or quality > 3:
            errors.append(f"{cid}: coverage_quality deve ser {minimum}..3")
        elif importance == "nuclear":
            covered_nuclear += 1
        refs = row.get("card_keys")
        if not isinstance(refs, list):
            errors.append(f"{cid}: card_keys deve ser lista")
            refs = []
        if not refs:
            # docs/canon/SELECAO-DE-CARDS.md §4: cobertura é da E1, não do card.
            # Conceito sem card é decisão legítima, mas nunca silenciosa.
            reason = str(row.get("no_card_reason") or "").strip()
            if len(reason) < 20:
                errors.append(f"{cid}: conceito sem card exige no_card_reason concreto")
        for ref in refs:
            key = str(ref).strip()
            if key not in card_keys:
                errors.append(f"{cid}: card_key inexistente: {key}")
            referenced_cards.add(key)
        step1 = row.get("step1") or {}
        decision = step1.get("decision")
        if decision not in {"not_applicable", "incorporated", "rejected"}:
            errors.append(f"{cid}: step1.decision inválido")
        elif decision == "incorporated":
            if step1.get("same_theme") is not True:
                errors.append(f"{cid}: Step 1 incorporado exige same_theme=true")
            for key in ("source_ref", "rationale"):
                if not str(step1.get(key) or "").strip():
                    errors.append(f"{cid}: Step 1 incorporado exige {key}")
        elif decision == "rejected" and not str(step1.get("rationale") or "").strip():
            errors.append(f"{cid}: Step 1 rejeitado exige rationale")

    if nuclear < 1:
        errors.append("release_gate precisa declarar ao menos um conceito nuclear")
    if nuclear != covered_nuclear:
        errors.append("nem todos os conceitos nucleares atingem cobertura >=2")
    unreferenced = sorted(card_keys - referenced_cards)
    if unreferenced:
        errors.append("cards sem conceito de cobertura: " + ", ".join(unreferenced))

    for card in cards:
        if not isinstance(card, dict):
            continue
        key = str(card.get("card_key") or "").strip()
        cid = str(card.get("concept_id") or "").strip()
        if cid not in seen_concepts:
            errors.append(f"{key}: concept_id fora do release_gate: {cid}")
            continue
        expected_tier = "optional" if importance_by_concept.get(cid) == "optional" else "nucleo"
        actual_tier = str(card.get("tier") or "nucleo").lower()
        if actual_tier != expected_tier:
            errors.append(f"{key}: tier={actual_tier} diverge de importance={importance_by_concept.get(cid)}")

    return {
        "passed": not errors,
        "errors": errors,
        "schema": SCHEMA,
        "card_budget_hard_max": hard_max,
        "concept_count": len(concepts),
        "nuclear_concept_count": nuclear,
        "covered_nuclear_count": covered_nuclear,
        "e1_source_sha256": str(release.get("e1_source_sha256") or ""),
        "e1_pdf_sha256": str(release.get("e1_pdf_sha256") or ""),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck_data", type=Path)
    args = parser.parse_args()
    data = json.loads(args.deck_data.read_text(encoding="utf-8"))
    result = validate_release(data, args.deck_data.resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
