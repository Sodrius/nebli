#!/usr/bin/env python3
"""Valida a matriz obrigatória E1 ampliada -> fontes -> deck-aula -> E2.

Uso: python flashcards/scripts/validate_lesson_coverage.py caminho/manifesto.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path


SOURCES = {"anking", "other_deck", "own"}


def normalise(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value or "")
    value = re.sub(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", r"\1", value, flags=re.I)
    value = re.sub(r"#[\w-]+\[", "", value)
    value = re.sub(r"[\[\]*_`#]", " ", value)
    return re.sub(r"\s+", " ", value).strip().casefold()


def validate(spec: dict, base: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    if spec.get("lesson_pipeline") != "deck-aula-v1":
        return {"passed": False, "errors": ["lesson_pipeline deve ser deck-aula-v1"], "warnings": []}
    e1_ref = str((spec.get("e1") or {}).get("path", "")).strip()
    e1_path = (base / e1_ref).resolve() if e1_ref else None
    if not e1_path or not e1_path.exists():
        return {"passed": False, "errors": ["e1.path inexistente"], "warnings": []}
    e1 = normalise(e1_path.read_text(encoding="utf-8-sig"))
    inventory = spec.get("e1_inventory")
    if not isinstance(inventory, list) or not inventory:
        errors.append("e1_inventory deve declarar todos os fatos-chave extraídos da E1")
        inventory = []
    facts = spec.get("facts")
    if not isinstance(facts, list) or not facts:
        errors.append("facts deve conter os fatos-chave da E1")
        facts = []
    seen: set[str] = set()
    inventory_ids = {str(row.get("id", "")).strip() for row in inventory}
    nuclear = covered = own = 0
    for row in facts:
        fid = str(row.get("id", "")).strip()
        if not fid or fid in seen:
            errors.append(f"id de fato ausente/duplicado: {fid or '?'}")
        seen.add(fid)
        anchor = str(row.get("e1_anchor", "")).strip()
        if not anchor or normalise(anchor) not in e1:
            errors.append(f"{fid}: âncora ausente da E1 ampliada")
        importance = str(row.get("importance", "")).lower()
        if importance not in {"nuclear", "supporting"}:
            errors.append(f"{fid}: importance deve ser nuclear|supporting")
        if importance == "nuclear":
            nuclear += 1
        if fid not in inventory_ids:
            errors.append(f"{fid}: fato não existe no e1_inventory")
        route = row.get("route") or {}
        source = str(route.get("source", "")).lower()
        refs = route.get("card_refs")
        if source not in SOURCES or not isinstance(refs, list) or not refs:
            errors.append(f"{fid}: rota precisa de source e card_refs")
            continue
        covered += 1
        quality = route.get("coverage_quality")
        if not isinstance(quality, int) or quality not in {0, 1, 2, 3}:
            errors.append(f"{fid}: coverage_quality deve ser inteiro de 0 a 3")
        elif importance == "nuclear" and quality < 2:
            errors.append(f"{fid}: fato nuclear requer coverage_quality >=2")
        elif importance == "supporting" and quality < 1:
            errors.append(f"{fid}: fato de apoio requer coverage_quality >=1")
        if not str(route.get("coverage_rationale", "")).strip():
            errors.append(f"{fid}: coverage_rationale ausente")
        if source == "own":
            own += 1
            probe = route.get("prior_search") or {}
            if not probe.get("anking") or not probe.get("other_decks"):
                errors.append(f"{fid}: autoria exige buscas AnKing e outros decks")
            if probe.get("anking") == "adequate" or probe.get("other_decks") == "adequate":
                errors.append(f"{fid}: autoral duplica fonte adequada")
    enrichments = spec.get("e1_enrichments", [])
    for row in enrichments:
        if not row.get("source_ref") or not row.get("decision") in {"incorporated", "dispensed"}:
            errors.append("enriquecimento E1 sem fonte ou decisão")
        if row.get("importance") == "nuclear" and row.get("decision") != "incorporated":
            errors.append("enriquecimento nuclear deve ser incorporado à E1")
        quote = str(row.get("e1_anchor", "")).strip()
        if row.get("decision") == "incorporated" and (not quote or normalise(quote) not in e1):
            errors.append("enriquecimento incorporado sem âncora na E1")
    fact_ids = {str(row.get("id", "")).strip() for row in facts}
    omitted = sorted(inventory_ids - fact_ids)
    if omitted:
        errors.append("fatos do e1_inventory sem rota no deck-aula: " + ", ".join(omitted))
    return {"passed": not errors, "errors": errors, "warnings": warnings,
            "facts": len(facts), "inventory": len(inventory_ids), "nuclear": nuclear,
            "covered": covered, "own": own}


def verify_anki(spec: dict) -> list[str]:
    """Confere, após importação, que cada referência realmente chegou ao deck-aula.

    card_refs são trechos estáveis do campo Text; a conferência não depende de GUID.
    """
    deck = str(spec.get("deck", "")).strip()
    if not deck:
        return ["deck ausente para auditoria pós-importação"]
    payload = json.dumps({"action": "findNotes", "version": 6,
                          "params": {"query": f'deck:"{deck}"'}}).encode()
    try:
        req = urllib.request.Request("http://localhost:8765", payload,
                                     {"Content-Type": "application/json"})
        result = json.load(urllib.request.urlopen(req, timeout=30))
        ids = result.get("result", [])
        payload = json.dumps({"action": "notesInfo", "version": 6,
                              "params": {"notes": ids}}).encode()
        req = urllib.request.Request("http://localhost:8765", payload,
                                     {"Content-Type": "application/json"})
        notes = json.load(urllib.request.urlopen(req, timeout=30)).get("result", [])
    except Exception as exc:
        return [f"auditoria Anki indisponível: {exc}"]
    corpus = "\n".join(normalise(next(iter(n.get("fields", {}).values()), {}).get("value", "")) for n in notes)
    errors = []
    for row in spec.get("facts", []):
        for ref in (row.get("route") or {}).get("card_refs", []):
            if normalise(str(ref)) not in corpus:
                errors.append(f"{row.get('id')}: card_ref não encontrado no deck: {ref}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--verify-anki", action="store_true")
    args = parser.parse_args()
    spec = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    result = validate(spec, args.manifest.parent.resolve())
    if args.verify_anki:
        result["errors"].extend(verify_anki(spec))
        result["passed"] = not result["errors"]
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
