#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Opera a fila Card -> E1 sem alterar material didático silenciosamente.

Um candidato só pode ser importado como card canônico após estar ``anchored``.
``anchorable`` produz um patch editorial revisável; ``outside`` fica documentado
como fora de escopo, em vez de virar um fato órfão no Anki.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
import re


DECISIONS = {"anchored", "anchorable", "outside"}


ROOT = Path(__file__).resolve().parents[2]


def _norm(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().casefold()


def validate(queue: dict) -> tuple[list[str], list[dict]]:
    errors, patches = [], []
    if not queue.get("slug"):
        errors.append("slug ausente")
    if not queue.get("e1_file"):
        errors.append("e1_file ausente")
        e1_text = ""
    else:
        e1_path = Path(queue["e1_file"])
        if not e1_path.is_absolute():
            e1_path = ROOT / e1_path
        if not e1_path.exists():
            errors.append(f"e1_file inexistente: {e1_path}")
            e1_text = ""
        else:
            e1_text = e1_path.read_text(encoding="utf-8-sig")
    for index, item in enumerate(queue.get("candidates", []), 1):
        prefix = f"candidate {index}: "
        if item.get("decision") not in DECISIONS:
            errors.append(prefix + "decision deve ser anchored|anchorable|outside")
        if not item.get("concept_id") or not item.get("rationale"):
            errors.append(prefix + "concept_id e rationale são obrigatórios")
        if item.get("decision") == "anchored" and not (item.get("e1_anchor") or {}).get("quote"):
            errors.append(prefix + "anchored exige e1_anchor.quote")
        elif item.get("decision") == "anchored" and _norm(item["e1_anchor"]["quote"]) not in _norm(e1_text):
            errors.append(prefix + "e1_anchor.quote não encontrado na E1")
        if item.get("decision") == "anchorable":
            patch = item.get("e1_patch") or {}
            if not patch.get("insert_after") or not patch.get("text") or not patch.get("source_refs"):
                errors.append(prefix + "anchorable exige e1_patch com ponto, texto e fontes")
            else:
                patches.append(item)
    return errors, patches


def render_patches(queue: dict, patches: list[dict]) -> str:
    out = [f"# Patches E1 pendentes — {queue['slug']}", "",
           "Não aplicar automaticamente: revisar precisão, voz pedagógica e posição na E1.", ""]
    for item in patches:
        patch = item["e1_patch"]
        out += [f"## {item.get('candidate_id', item['concept_id'])} — {item['concept_id']}",
                f"**Inserir após:** {patch['insert_after']}", "",
                patch["text"], "",
                f"**Fontes:** {', '.join(patch['source_refs'])}",
                f"**Por que:** {item['rationale']}", ""]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Valida e materializa a fila Card -> E1.")
    ap.add_argument("queue", type=Path)
    ap.add_argument("--patch-report", type=Path)
    args = ap.parse_args()
    queue = json.loads(args.queue.read_text(encoding="utf-8-sig"))
    errors, patches = validate(queue)
    if args.patch_report and patches:
        args.patch_report.parent.mkdir(parents=True, exist_ok=True)
        args.patch_report.write_text(render_patches(queue, patches), encoding="utf-8")
        print(f"patch report: {args.patch_report}")
    print(json.dumps({"candidates": len(queue.get("candidates", [])), "patches": len(patches),
                      "errors": errors, "passed": not errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
