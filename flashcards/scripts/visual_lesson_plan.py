#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrato do plano visual que nasce antes dos cards de uma aula."""
from __future__ import annotations

import json
from pathlib import Path


STRATEGIES = {"io_required", "extra_recommended", "optional", "none"}
IMPORTANCE = {"nuclear", "support", "optional"}
ROLES = {"recognition", "localization", "mechanism", "comparison", "schema", "context", "none"}


def load_plan(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def validate_plan(plan: dict) -> tuple[list[str], dict[str, dict]]:
    errors: list[str] = []
    concepts = plan.get("concepts")
    if plan.get("visual_plan_version") != "v1":
        errors.append("visual_plan_version deve ser v1")
    if not isinstance(concepts, list) or not concepts:
        return errors + ["concepts deve ser lista não vazia"], {}
    index: dict[str, dict] = {}
    for number, row in enumerate(concepts, 1):
        where = f"plano visual {number}"
        cid = str(row.get("concept_id", "")).strip()
        if not cid:
            errors.append(f"{where}: concept_id ausente")
            continue
        if cid in index:
            errors.append(f"{where}: concept_id duplicado: {cid}")
        index[cid] = row
        if row.get("importance") not in IMPORTANCE:
            errors.append(f"{where}: importance inválida")
        if not str(row.get("learning_goal", "")).strip():
            errors.append(f"{where}: learning_goal ausente")
        if row.get("strategy") not in STRATEGIES:
            errors.append(f"{where}: strategy inválida")
        if row.get("image_role") not in ROLES:
            errors.append(f"{where}: image_role inválido")
        if not str(row.get("visual_task", "")).strip():
            errors.append(f"{where}: visual_task ausente")
        if not str(row.get("rationale", "")).strip():
            errors.append(f"{where}: rationale ausente")
        strategy = row.get("strategy")
        if strategy == "io_required":
            if row.get("image_role") not in {"recognition", "localization", "comparison"}:
                errors.append(f"{where}: io_required exige role visual de reconhecimento/localização")
            io = row.get("io") or {}
            targets = io.get("targets")
            if not isinstance(targets, list) or not 1 <= len(targets) <= 4:
                errors.append(f"{where}: IO exige 1–4 targets nucleares por prancha")
            elif any(not str(target.get("label", "")).strip() for target in targets if isinstance(target, dict)):
                errors.append(f"{where}: cada alvo IO exige label")
            if not str(io.get("board_id", "")).strip():
                errors.append(f"{where}: IO exige board_id")
        elif strategy == "extra_recommended":
            if row.get("image_role") not in {"mechanism", "comparison", "schema", "localization"}:
                errors.append(f"{where}: extra_recommended exige mecanismo/comparação/esquema/localização")
        elif strategy == "none" and row.get("image_role") != "none":
            errors.append(f"{where}: strategy=none exige image_role=none")
    return errors, index


def compatible(card_visual: dict, plan: dict, link: str) -> str | None:
    """Garante que a decisão do card não contradiz o objetivo visual da aula."""
    strategy = plan["strategy"]
    mode = card_visual.get("card_mode")
    placement = card_visual.get("placement")
    if strategy == "none" and card_visual.get("visual_need") != "none":
        return "plano visual define none; card não pode inserir imagem decorativa"
    if strategy == "extra_recommended" and link == "primary" and (mode != "explanatory_image" or placement != "extra"):
        return "plano visual pede imagem explicativa no Extra"
    if strategy == "io_required" and link == "primary" and mode != "image_occlusion":
        return "plano visual pede IO; card primário deve ser image_occlusion"
    if strategy == "io_required" and link == "paired_cloze" and mode == "image_occlusion":
        return "paired_cloze não deve declarar image_occlusion"
    return None
