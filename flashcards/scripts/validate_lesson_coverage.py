#!/usr/bin/env python3
"""Valida a matriz obrigatória E1 ampliada -> fontes -> deck-aula -> E2.

Uso: python flashcards/scripts/validate_lesson_coverage.py caminho/manifesto.json
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path


SOURCES = {"anking", "other_deck", "own"}
DECISIONS = {"nuclear", "supporting", "no_card"}


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
    if not isinstance(facts, list):
        errors.append("facts deve ser uma lista dos conceitos que realmente receberão card")
        facts = []
    seen: set[str] = set()
    inventory_ids: set[str] = set()
    inventory_decisions: dict[str, str] = {}
    for row in inventory:
        iid = str(row.get("id", "")).strip()
        decision = str(row.get("card_decision") or row.get("importance") or "").lower().strip()
        anchor = str(row.get("e1_anchor", "")).strip()
        if not iid or iid in inventory_ids:
            errors.append(f"id de inventário ausente/duplicado: {iid or '?'}")
            continue
        inventory_ids.add(iid)
        inventory_decisions[iid] = decision
        if decision not in DECISIONS:
            errors.append(f"{iid}: card_decision deve ser nuclear|supporting|no_card")
        if not anchor or normalise(anchor) not in e1:
            errors.append(f"{iid}: e1_inventory exige âncora literal existente na E1")
        if decision == "no_card" and not str(row.get("decision_reason", "")).strip():
            warnings.append(f"{iid}: no_card sem decision_reason; recomendável registrar por que não merece revisão")
    nuclear = covered = own = 0
    for row in facts:
        fid = str(row.get("id", "")).strip()
        if not fid or fid in seen:
            errors.append(f"id de fato ausente/duplicado: {fid or '?'}")
        seen.add(fid)
        anchor = str(row.get("e1_anchor", "")).strip()
        if not anchor or normalise(anchor) not in e1:
            errors.append(f"{fid}: âncora ausente da E1 ampliada")
        importance = str(row.get("importance") or inventory_decisions.get(fid, "")).lower()
        if importance not in {"nuclear", "supporting"}:
            errors.append(f"{fid}: importance deve ser nuclear|supporting")
        if importance == "nuclear":
            nuclear += 1
        if fid not in inventory_ids:
            errors.append(f"{fid}: fato não existe no e1_inventory")
        elif inventory_decisions.get(fid) == "no_card":
            errors.append(f"{fid}: conceito no_card não pode ter rota de card")
        elif inventory_decisions.get(fid) in {"nuclear", "supporting"} and importance != inventory_decisions[fid]:
            errors.append(f"{fid}: importance diverge do card_decision do inventário")
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
    missing_nuclear = sorted(i for i, d in inventory_decisions.items() if d == "nuclear" and i not in fact_ids)
    if missing_nuclear:
        errors.append("conceitos nucleares sem rota no deck-aula: " + ", ".join(missing_nuclear))
    return {"passed": not errors, "errors": errors, "warnings": warnings,
            "facts": len(facts), "inventory": len(inventory_ids), "nuclear": nuclear,
            "covered": covered, "own": own,
            "supporting_skipped": sum(1 for i, d in inventory_decisions.items()
                                      if d == "supporting" and i not in fact_ids),
            "no_card": sum(1 for d in inventory_decisions.values() if d == "no_card")}


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


def verify_apkg(spec: dict, apkg: Path) -> tuple[list[str], int]:
    """Confere card_refs e contagem real dentro de um .apkg, sem AnkiConnect."""
    if not apkg.exists():
        return [f".apkg inexistente: {apkg}"], 0
    try:
        with zipfile.ZipFile(apkg) as zf:
            names = zf.namelist()
            collection = next((n for n in ("collection.anki21", "collection.anki2") if n in names), None)
            if not collection:
                return [".apkg sem collection.anki21/collection.anki2"], 0
            with tempfile.TemporaryDirectory() as td:
                db = Path(td) / Path(collection).name
                db.write_bytes(zf.read(collection))
                con = sqlite3.connect(db)
                try:
                    note_rows = con.execute("select flds from notes").fetchall()
                    card_count = con.execute("select count(*) from cards").fetchone()[0]
                finally:
                    con.close()
    except Exception as exc:
        return [f"falha ao auditar .apkg: {exc}"], 0
    normalised_notes = [normalise(str(row[0]).replace("\x1f", " ")) for row in note_rows]
    corpus = "\n".join(normalised_notes)
    errors = []
    approved_refs: list[str] = []
    for row in spec.get("facts", []):
        for ref in (row.get("route") or {}).get("card_refs", []):
            ref_norm = normalise(str(ref))
            approved_refs.append(ref_norm)
            if ref_norm not in corpus:
                errors.append(f"{row.get('id')}: card_ref não encontrado no .apkg: {ref}")
    for idx, note in enumerate(normalised_notes, 1):
        if approved_refs and not any(ref and ref in note for ref in approved_refs):
            errors.append(f"nota {idx} do .apkg não consta no manifesto de admissão")
    expected = (spec.get("load_profile") or {}).get("estimated_cards")
    if isinstance(expected, int) and card_count != expected:
        errors.append(f"contagem .apkg diverge do manifesto: {card_count} real != {expected} estimado")
    return errors, int(card_count)


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
