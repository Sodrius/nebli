#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrato canônico E1 -> card -> E2, incluindo decisão visual.

O contrato é deliberadamente estrito apenas para specs novos que declaram
``pipeline_contract: e1-e2-v1``. Assim, os JSONs legados continuam legíveis,
mas nenhum lote novo pode pular a evidência, a revisão declarada, a proveniência
da redação ou a decisão visual por card.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from validar_manifesto_visual import validate as validate_visual
from visual_lesson_plan import compatible as visual_compatible
from visual_lesson_plan import load_plan, validate_plan


CONTRACT = "e1-e2-v1"
MODES = {"authorial", "external_copy"}
DECISIONS = {"covered", "outside_scope"}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def _path(value: str, base: Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (base / path).resolve()


def _normalise(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    # Achata macros Typst para que uma âncora possa citar texto adjacente a
    # #termo-nota[...] sem ter de repetir a marcação editorial da E1.
    text = re.sub(r"#[\w-]+\[", "", text)
    text = re.sub(r"[\[\]*_`#]", " ", text)
    return re.sub(r"\s+", " ", text).strip().casefold()


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_e2_items(text: str) -> list[str]:
    """Extrai alvos mínimos da E2 sem confundir alternativa com conceito.

    Primeiro aproveita macros de termos/siglas; em seguida, usa o enunciado de
    macros de questão como alvo de auditoria. O curador pode substituir/adiar
    esses IDs com ``e2_catalog`` explícito na spec.
    """
    items: list[str] = []
    seen: set[str] = set()

    def add(value: str) -> None:
        value = _normalise(value)
        if value and value not in seen:
            seen.add(value)
            items.append(value)

    for match in re.finditer(r"#termo-nota\[([^\]]+)\]", text):
        add(match.group(1))
    for match in re.finditer(r'#sigla\("([^"]+)"', text):
        add(match.group(1))
    question_matches = list(re.finditer(r"#(?:quest[aã]o|pergunta|question)(?:-[\w]+)?\s*\(", text, re.I))
    for number, match in enumerate(question_matches):
        end = question_matches[number + 1].start() if number + 1 < len(question_matches) else len(text)
        start = text.find("[", match.end(), end)
        if start < 0:
            continue
        depth, index = 0, start
        while index < len(text):
            if text[index] == "[":
                depth += 1
            elif text[index] == "]":
                depth -= 1
                if not depth:
                    add(text[start + 1:index])
                    break
            index += 1
    return items


def _visual_row(card: dict) -> dict:
    visual = card.get("visual") or {}
    return {"note_id": card.get("nebli_id", "sem_id"), **visual}


def validate_spec(spec: dict, base: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    if spec.get("pipeline_contract") != CONTRACT:
        return {"errors": [f"pipeline_contract deve ser '{CONTRACT}'"], "warnings": []}

    e1 = spec.get("e1") or {}
    if not e1.get("path"):
        return {"errors": ["e1.path ausente"], "warnings": []}
    e1_path = _path(e1["path"], base)
    if not e1_path.exists():
        return {"errors": [f"E1 inexistente: {e1_path}"], "warnings": []}
    e1_text = _read(e1_path)
    e1_norm = _normalise(e1_text)
    if e1.get("sha256") and e1["sha256"] != _sha(e1_path):
        errors.append("E1 mudou desde a ancoragem (sha256 divergente)")

    visual_index: dict[str, dict] = {}
    plan_ref = spec.get("visual_plan")
    if not plan_ref:
        errors.append("visual_plan ausente: a aula precisa decidir IO, Extra ou none antes dos cards")
    else:
        plan_path = _path(str(plan_ref), base)
        if not plan_path.exists():
            errors.append(f"plano visual inexistente: {plan_path}")
        else:
            plan_errors, visual_index = validate_plan(load_plan(plan_path))
            errors.extend(f"plano visual: {error}" for error in plan_errors)

    e2_items: list[str] = []
    e2 = spec.get("e2") or {}
    if e2.get("path"):
        e2_path = _path(e2["path"], base)
        if not e2_path.exists():
            errors.append(f"E2 inexistente: {e2_path}")
        else:
            e2_text = _read(e2_path)
            e2_items = list(e2.get("catalog") or extract_e2_items(e2_text))
            if e2.get("sha256") and e2["sha256"] != _sha(e2_path):
                errors.append("E2 mudou desde a matriz (sha256 divergente)")
    elif e2.get("catalog"):
        e2_items = list(e2["catalog"])
    else:
        warnings.append("sem E2: cobertura de avaliação não foi auditada")

    cards = spec.get("cards")
    if not isinstance(cards, list) or not cards:
        errors.append("cards deve ser uma lista não vazia")
        cards = []
    ids: set[str] = set()
    card_concepts: set[str] = set()
    for number, card in enumerate(cards, 1):
        where = f"card {number}"
        cid = str(card.get("nebli_id", "")).strip()
        if not cid:
            errors.append(f"{where}: nebli_id ausente")
        elif cid in ids:
            errors.append(f"{where}: nebli_id duplicado: {cid}")
        ids.add(cid)
        concept = str(card.get("concept_id", "")).strip()
        if not concept:
            errors.append(f"{where}: concept_id ausente")
        else:
            card_concepts.add(concept)

        anchor = card.get("e1_anchor") or {}
        quote = str(anchor.get("quote", "")).strip()
        if not quote:
            errors.append(f"{where}: e1_anchor.quote ausente")
        elif _normalise(quote) not in e1_norm:
            errors.append(f"{where}: âncora E1 não encontrada literalmente")

        generation = card.get("generation") or {}
        mode = generation.get("mode")
        if mode not in MODES:
            errors.append(f"{where}: generation.mode inválido")
        if not isinstance(generation.get("source_refs"), list) or not generation.get("source_refs"):
            errors.append(f"{where}: generation.source_refs ausente")
        if mode == "authorial":
            probe = generation.get("external_probe") or {}
            if not probe.get("queries") or not str(probe.get("decision", "")).strip():
                errors.append(f"{where}: autoria exige external_probe com queries e decisão")
        if mode == "external_copy" and not generation.get("external_card_ref"):
            errors.append(f"{where}: cópia externa exige external_card_ref")

        review = card.get("semantic_review") or {}
        for key in ("atomicity", "induction", "medical"):
            if review.get(key) != "pass":
                errors.append(f"{where}: semantic_review.{key} deve ser 'pass'")
        if not str(review.get("reviewer", "")).strip():
            errors.append(f"{where}: semantic_review.reviewer ausente")
        if not str((card.get("visual") or {}).get("visual_task", "")).strip():
            errors.append(f"{where}: visual.visual_task ausente (inclusive quando visual_need=none)")
        errors.extend(validate_visual(_visual_row(card), base))
        plan_id = str(card.get("visual_plan_id", "")).strip()
        plan_link = str(card.get("visual_plan_link", "")).strip()
        if not plan_id:
            errors.append(f"{where}: visual_plan_id ausente")
        elif plan_id not in visual_index:
            errors.append(f"{where}: visual_plan_id não existe no plano: {plan_id}")
        elif plan_link not in {"primary", "paired_cloze"}:
            errors.append(f"{where}: visual_plan_link deve ser primary|paired_cloze")
        else:
            if visual_index[plan_id].get("needs_editorial_confirmation") is True:
                errors.append(f"{where}: decisão visual ainda precisa de confirmação editorial: {plan_id}")
            visual_error = visual_compatible(card.get("visual") or {}, visual_index[plan_id], plan_link)
            if visual_error:
                errors.append(f"{where}: {visual_error}")

    coverage = spec.get("e2_coverage")
    if e2_items and not isinstance(coverage, list):
        errors.append("e2_coverage obrigatório quando há E2")
        coverage = []
    seen_e2: set[str] = set()
    for row in coverage or []:
        target = _normalise(str(row.get("e2_item", "")))
        concept = str(row.get("concept_id", "")).strip()
        decision = row.get("status")
        if target not in {_normalise(x) for x in e2_items}:
            errors.append(f"e2_coverage aponta alvo desconhecido: {row.get('e2_item')}")
        seen_e2.add(target)
        if decision not in DECISIONS:
            errors.append("e2_coverage.status deve ser covered|outside_scope")
        if not str(row.get("rationale", "")).strip():
            errors.append("e2_coverage.rationale ausente")
        if decision == "covered" and concept not in card_concepts:
            errors.append(f"E2 coberta sem card do concept_id {concept}")
    for item in e2_items:
        if _normalise(item) not in seen_e2:
            errors.append(f"alvo E2 sem destino: {item}")

    return {
        "errors": errors,
        "warnings": warnings,
        "cards": len(cards),
        "e1_sha256": _sha(e1_path),
        "e2_items": len(e2_items),
        "passed": not errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida o contrato canônico E1 -> card -> E2.")
    parser.add_argument("spec", type=Path)
    args = parser.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8-sig"))
    result = validate_spec(spec, args.spec.parent.resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
