#!/usr/bin/env python3
"""Gate hard para fechamento de deck-aula completo e AnKing-primeiro.

Uso: python gate_deck_aula_completo.py matriz.json [--verify-anki]
Exige o contrato ``deck-aula-v2``; manifestos antigos não podem fechar uma aula nova.
"""
from __future__ import annotations

import argparse, json, re, sys
from pathlib import Path

from validate_lesson_coverage import validate, verify_anki, verify_apkg


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--verify-anki", action="store_true")
    ap.add_argument("--verify-apkg", type=Path,
                    help="valida o pacote offline quando AnkiConnect não está disponível")
    args = ap.parse_args()
    spec = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    errors: list[str] = []
    warnings: list[str] = []
    if spec.get("deck_aula_gate") != "v2":
        errors.append("deck_aula_gate=v2 obrigatório: manifestação v1 não pode fechar deck novo")
    base_result = validate({**spec, "lesson_pipeline": "deck-aula-v1"}, args.manifest.parent.resolve())
    errors += base_result["errors"]
    inventory = spec.get("e1_inventory", [])
    facts = spec.get("facts", [])
    fact_ids = {f.get("id") for f in facts}
    decisions = {}
    for row in inventory:
        decision = str(row.get("card_decision") or row.get("importance") or "").lower()
        decisions[row.get("id")] = decision
        if not row.get("id") or not row.get("e1_anchor") or decision not in {"nuclear", "supporting", "no_card"}:
            errors.append("todo item do inventário exige id, âncora literal e card_decision válido")
    missing_nuclear = sorted(str(i) for i, d in decisions.items() if d == "nuclear" and i not in fact_ids)
    if missing_nuclear:
        errors.append("nucleares sem card: " + ", ".join(missing_nuclear))
    routed_no_card = sorted(str(i) for i, d in decisions.items() if d == "no_card" and i in fact_ids)
    if routed_no_card:
        errors.append("no_card roteado indevidamente: " + ", ".join(routed_no_card))
    audit = spec.get("source_audit") or {}
    if not audit.get("pool_path") or not Path(audit["pool_path"]).exists():
        errors.append("source_audit.pool_path existente é obrigatório")
    candidates = audit.get("candidates_by_fact") or {}
    nuclear = 0
    targets: dict[str, str] = {}
    for fact in facts:
        fid = fact.get("id")
        route = fact.get("route") or {}
        if fid not in candidates:
            errors.append(f"{fid}: falta evidência de busca AnKing card-a-card")
        evidence = candidates.get(fid) or {}
        if not evidence.get("searched_tags") or "candidate_count" not in evidence:
            errors.append(f"{fid}: busca AnKing sem tags e contagem de candidatos")
        if str(fact.get("importance") or decisions.get(fid, "")).lower() == "nuclear":
            nuclear += 1
        target = re.sub(r"\s+", " ", str(route.get("retrieval_target", "")).casefold()).strip()
        if not target:
            errors.append(f"{fid}: retrieval_target ausente")
        elif target in targets:
            errors.append(f"{fid}: retrieval_target duplica {targets[target]}: {route.get('retrieval_target')}")
        else:
            targets[target] = str(fid)
        if route.get("source") == "own":
            probe = route.get("prior_search") or {}
            if (probe.get("anking") != "insufficient"
                    or probe.get("other_decks") != "insufficient"
                    or not evidence.get("rejection_rationale")):
                errors.append(f"{fid}: autoria só após rejeição documentada de AnKing e outros decks")
        visual = fact.get("visual") or {}
        if visual.get("need") == "required" and visual.get("status") != "approved":
            errors.append(f"{fid}: visual required sem ativo aprovado")
    enrich = spec.get("e1_enrichments") or []
    for row in enrich:
        if not row.get("source_ref") or not row.get("e1_anchor") or not row.get("selection_reason"):
            errors.append("enriquecimento Step 1 exige card-fonte, âncora E1 e motivo de incorporação")
    load = spec.get("load_profile") or {}
    estimated = load.get("estimated_cards")
    size = str(load.get("lecture_size", "")).lower()
    ceilings = {"small": 25, "medium": 40, "large": 55}
    if size not in ceilings:
        errors.append("load_profile.lecture_size deve ser small|medium|large")
    if not isinstance(estimated, int) or estimated < 0:
        errors.append("load_profile.estimated_cards é obrigatório e deve ser inteiro >=0")
    else:
        if size in ceilings and estimated > ceilings[size]:
            warnings.append(f"{estimated} cards acima do guardrail usual para aula {size} (~{ceilings[size]})")
        if estimated > 60 and (not load.get("redundancy_reviewed")
                               or not str(load.get("over_ceiling_reason", "")).strip()):
            errors.append("deck >60 cards exige redundancy_reviewed=true + over_ceiling_reason")
    if args.verify_anki:
        errors += verify_anki(spec)
    actual_apkg_cards = None
    if args.verify_apkg:
        apkg_errors, actual_apkg_cards = verify_apkg(spec, args.verify_apkg)
        errors += apkg_errors
    result = {"passed": not errors, "nuclear": nuclear, "estimated_cards": estimated,
              "apkg_cards": actual_apkg_cards, "warnings": warnings, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
