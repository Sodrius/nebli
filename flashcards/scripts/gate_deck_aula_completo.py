#!/usr/bin/env python3
"""Gate hard para fechamento de deck-aula completo e AnKing-primeiro.

Uso: python gate_deck_aula_completo.py matriz.json [--verify-anki]
Exige o contrato ``deck-aula-v2``; manifestos antigos não podem fechar uma aula nova.
"""
from __future__ import annotations

import argparse, json, math, sys
from pathlib import Path

from validate_lesson_coverage import validate, verify_anki


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--verify-anki", action="store_true")
    args = ap.parse_args()
    spec = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    errors: list[str] = []
    if spec.get("deck_aula_gate") != "v2":
        errors.append("deck_aula_gate=v2 obrigatório: manifestação v1 não pode fechar deck novo")
    base_result = validate({**spec, "lesson_pipeline": "deck-aula-v1"}, args.manifest.parent.resolve())
    errors += base_result["errors"]
    inventory = spec.get("e1_inventory", [])
    facts = spec.get("facts", [])
    fact_ids = {f.get("id") for f in facts}
    for row in inventory:
        if not row.get("id") or not row.get("e1_anchor") or row.get("importance") not in {"nuclear", "supporting"}:
            errors.append("todo item do inventário E1 exige id, âncora literal e importância")
    if {r.get("id") for r in inventory} != fact_ids:
        errors.append("inventário atomizado da E1 e fatos roteados divergem")
    audit = spec.get("source_audit") or {}
    if not audit.get("pool_path") or not Path(audit["pool_path"]).exists():
        errors.append("source_audit.pool_path existente é obrigatório")
    candidates = audit.get("candidates_by_fact") or {}
    real_nuclear = 0
    nuclear = 0
    for fact in facts:
        fid = fact.get("id")
        route = fact.get("route") or {}
        if fid not in candidates:
            errors.append(f"{fid}: falta evidência de busca AnKing card-a-card")
        evidence = candidates.get(fid) or {}
        if not evidence.get("searched_tags") or "candidate_count" not in evidence:
            errors.append(f"{fid}: busca AnKing sem tags e contagem de candidatos")
        if fact.get("importance") == "nuclear":
            nuclear += 1
            if route.get("source") in {"anking", "other_deck"}:
                real_nuclear += 1
        if route.get("source") == "own":
            probe = route.get("prior_search") or {}
            if probe.get("anking") != "insufficient" or not evidence.get("rejection_rationale"):
                errors.append(f"{fid}: autoria só após rejeição documentada dos candidatos AnKing")
    minimum = math.ceil(nuclear * 0.60)
    if real_nuclear < minimum:
        errors.append(f"AnKing-primeiro falhou: {real_nuclear}/{nuclear} nucleares reais; mínimo {minimum}")
    enrich = spec.get("e1_enrichments") or []
    if not enrich:
        errors.append("passe Step 1→E1 ausente: nenhum enriquecimento foi auditado")
    for row in enrich:
        if not row.get("source_ref") or not row.get("e1_anchor") or not row.get("selection_reason"):
            errors.append("enriquecimento Step 1 exige card-fonte, âncora E1 e motivo de incorporação")
    if args.verify_anki:
        errors += verify_anki(spec)
    result = {"passed": not errors, "nuclear": nuclear, "real_nuclear": real_nuclear, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
