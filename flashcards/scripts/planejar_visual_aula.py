#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Semeia o plano visual da aula antes da redação dos cards.

As heurísticas nunca aprovam uma imagem: apenas impedem que a decisão visual
fique para o fim. O editor confirma ou ajusta cada linha antes de gerar cards.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


IO_WORDS = re.compile(r"anatom|vas[oa]|art[ée]r|vei[ao]|nervo|músculo|osso|órgão|camada|corte|histolog|tecido|lâmina|folículo|túbulo|glândula|corpúsculo|radiolog|ecg|dermat|lesão", re.I)
EXTRA_WORDS = re.compile(r"mecanismo|fluxo|via |transporte|cascata|ciclo|contração|secreção|sinaliza|metabol|fisiolog|farmaco|compar|relaç", re.I)


def read_checklist(path: Path) -> list[tuple[str, str]]:
    rows = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line or line.startswith("#"):
            continue
        cells = line.split("\t")
        if len(cells) >= 2:
            rows.append((cells[0].strip(), cells[1].strip()))
    return rows


def seed(concept_id: str, goal: str) -> dict:
    if IO_WORDS.search(goal):
        return {"concept_id": concept_id, "importance": "support", "learning_goal": goal,
                "strategy": "io_required", "image_role": "recognition",
                "visual_task": "confirmar se o aluno precisa reconhecer/localizar esta estrutura",
                "rationale": "semeado por vocabulário estrutural; confirmar antes da produção",
                "needs_editorial_confirmation": True,
                "io": {"board_id": f"{concept_id}-board", "targets": [{"label": goal}]}}
    if EXTRA_WORDS.search(goal):
        return {"concept_id": concept_id, "importance": "support", "learning_goal": goal,
                "strategy": "extra_recommended", "image_role": "mechanism",
                "visual_task": "explicar a relação ou mecanismo depois do recall",
                "rationale": "semeado por vocabulário de processo; confirmar a figura mínima útil",
                "needs_editorial_confirmation": True}
    return {"concept_id": concept_id, "importance": "support", "learning_goal": goal,
            "strategy": "none", "image_role": "none",
            "visual_task": "não há relação visual recuperável neste objetivo",
            "rationale": "semeado como conceito predominantemente verbal; revisar se a aula exigir reconhecimento",
            "needs_editorial_confirmation": True}


def main() -> int:
    parser = argparse.ArgumentParser(description="Semeia plano visual de uma aula a partir da checklist.")
    parser.add_argument("checklist", type=Path)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    out = args.out or args.checklist.with_name(f"plano-visual-{args.slug}.json")
    plan = {"visual_plan_version": "v1", "slug": args.slug,
            "concepts": [seed(cid, goal) for cid, goal in read_checklist(args.checklist)]}
    out.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {out} | {len(plan['concepts'])} decisões visuais pendentes de confirmação editorial")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
