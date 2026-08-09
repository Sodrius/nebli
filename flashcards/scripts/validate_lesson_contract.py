#!/usr/bin/env python3
"""Hard gate for the canonical E1 + deck lesson contract (v3)."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


IMPORTANCE = {"nuclear", "supporting", "optional"}
SOURCES = {"anking", "external_deck", "authored"}
STEP1 = {"not_applicable", "incorporated", "rejected"}
VISUAL_NEED = {"required", "recommended", "optional", "none"}
VISUAL_ROLE = {"recognition", "localization", "mechanism", "comparison", "schema", "context", "none"}
VISUAL_MODE = {"image_occlusion", "image_prompt", "explanatory_image", "none"}
VISUAL_STATUS = {"approved", "pending", "not_needed", "rejected"}
ORIGINS = {"slide", "objective", "e1", "step1"}


def normalise(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value or "")
    value = re.sub(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", r"\1", value, flags=re.I)
    value = re.sub(r"[#*_`\[\]]", " ", value)
    return re.sub(r"\s+", " ", value).strip().casefold()


def _legacy_keys(value, prefix=""):
    found = []
    if isinstance(value, dict):
        for key, child in value.items():
            here = f"{prefix}.{key}" if prefix else key
            if key.casefold() in {"e2", "e3", "remnote", "e2_coverage", "e3_coverage"}:
                found.append(here)
            found.extend(_legacy_keys(child, here))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(_legacy_keys(child, f"{prefix}[{index}]"))
    return found


def _resolve(base: Path, raw: str) -> Path:
    path = Path(raw)
    return path if path.is_absolute() else (base / path).resolve()


def _asset_errors(cid: str, visual: dict, base: Path) -> list[str]:
    errors = []
    need, role, mode, status = (visual.get("need"), visual.get("role"),
                                visual.get("mode"), visual.get("status"))
    if need not in VISUAL_NEED: errors.append(f"{cid}: visual.need inválido")
    if role not in VISUAL_ROLE: errors.append(f"{cid}: visual.role inválido")
    if mode not in VISUAL_MODE: errors.append(f"{cid}: visual.mode inválido")
    if status not in VISUAL_STATUS: errors.append(f"{cid}: visual.status inválido")
    if need != "none" and not str(visual.get("task", "")).strip():
        errors.append(f"{cid}: visual.task ausente")
    if need == "none" and (role != "none" or mode != "none" or status != "not_needed"):
        errors.append(f"{cid}: visual none contraditório")
    if role in {"recognition", "localization"} and mode not in {"image_occlusion", "image_prompt"}:
        errors.append(f"{cid}: reconhecer/localizar exige IO ou prompt visual")
    if role in {"mechanism", "schema"} and mode not in {"explanatory_image", "none"}:
        errors.append(f"{cid}: mecanismo/esquema deve usar imagem explicativa no Extra")
    if need == "required" and status != "approved":
        errors.append(f"{cid}: visual obrigatório ainda não aprovado")
    if status == "approved":
        asset = visual.get("asset") or {}
        for key in ("file", "source_type", "source_locator", "credit", "hash", "preview"):
            if not str(asset.get(key, "")).strip(): errors.append(f"{cid}: visual.asset.{key} ausente")
        for key in ("file", "preview"):
            raw = str(asset.get(key, "")).strip()
            if raw and not _resolve(base, raw).exists(): errors.append(f"{cid}: {key} visual inexistente: {raw}")
        if asset.get("answer_leakage") is not False:
            errors.append(f"{cid}: ativo aprovado exige answer_leakage=false")
        if mode == "image_occlusion":
            masks = visual.get("masks")
            if not isinstance(masks, list) or not masks:
                errors.append(f"{cid}: IO aprovado exige masks[]")
    return errors


def validate(spec: dict, manifest_path: Path, allow_pending_private: bool = False) -> dict:
    errors, warnings = [], []
    base = manifest_path.parent.resolve()
    if spec.get("pipeline_version") != "e1-deck-v3":
        errors.append("pipeline_version deve ser e1-deck-v3")
    legacy = _legacy_keys(spec)
    if legacy: errors.append("chaves legadas proibidas: " + ", ".join(legacy))
    for key in ("slug", "title", "deck", "optional_deck"):
        if not str(spec.get(key, "")).strip(): errors.append(f"{key} obrigatório")
    if spec.get("optional_deck") and not str(spec["optional_deck"]).endswith("::Optional"):
        errors.append("optional_deck deve terminar em ::Optional")

    e1_raw = str((spec.get("e1") or {}).get("path", "")).strip()
    e1_path = _resolve(base, e1_raw) if e1_raw else None
    e1_text = ""
    if not e1_path or not e1_path.exists():
        errors.append("e1.path inexistente")
    else:
        e1_text = normalise(e1_path.read_text(encoding="utf-8-sig"))
        expected = str((spec.get("e1") or {}).get("sha256", "")).strip()
        actual = hashlib.sha256(e1_path.read_bytes()).hexdigest()
        if spec.get("status") == "frozen" and not expected:
            errors.append("contrato frozen exige e1.sha256")
        elif expected and expected != actual:
            errors.append("E1 mudou após o congelamento (sha256 divergente)")

    private = spec.get("private_sources") or {}
    anking = private.get("anking_index") or {}
    if anking.get("status") != "ready":
        message = "índice privado do AnKing não está pronto"
        (warnings if allow_pending_private else errors).append(message)
    elif not str(anking.get("path", "")).strip():
        errors.append("anking_index ready exige path")
    else:
        index_path = _resolve(base, str(anking["path"]))
        if not index_path.is_file():
            errors.append(f"anking_index inexistente: {anking['path']}")
        if not str(anking.get("sha256", "")).strip():
            errors.append("anking_index ready exige sha256 da fonte privada")

    concepts = spec.get("concepts")
    if not isinstance(concepts, list) or not concepts:
        errors.append("concepts[] obrigatório e não vazio")
        concepts = []
    seen = set(); counts = {source: 0 for source in SOURCES}; nuclear = covered = 0
    for row in concepts:
        cid = str(row.get("id", "")).strip()
        if not cid or cid in seen: errors.append(f"concept id ausente/duplicado: {cid or '?'}")
        seen.add(cid)
        for key in ("name_pt", "name_en", "subtopic"):
            if not str(row.get(key, "")).strip(): errors.append(f"{cid}: {key} obrigatório")
        origins = row.get("origins")
        if not isinstance(origins, list) or not origins or not set(origins) <= ORIGINS:
            errors.append(f"{cid}: origins inválido")
        importance = row.get("importance")
        if importance not in IMPORTANCE: errors.append(f"{cid}: importance inválido")
        if importance == "nuclear": nuclear += 1
        anchor = str(row.get("e1_anchor", "")).strip()
        if not anchor or (e1_text and normalise(anchor) not in e1_text):
            errors.append(f"{cid}: âncora literal ausente da E1")

        step1 = row.get("step1") or {}
        decision = step1.get("decision")
        if decision not in STEP1: errors.append(f"{cid}: step1.decision inválido")
        if decision == "incorporated":
            if step1.get("same_theme") is not True: errors.append(f"{cid}: Step 1 incorporado exige same_theme=true")
            for key in ("source_ref", "rationale"):
                if not str(step1.get(key, "")).strip(): errors.append(f"{cid}: Step 1 incorporado exige {key}")
            if "step1" not in (origins or []): errors.append(f"{cid}: enriquecimento incorporado exige origem step1")

        errors.extend(_asset_errors(cid, row.get("visual") or {}, base))

        route = row.get("route") or {}; source = route.get("source")
        if source not in SOURCES:
            errors.append(f"{cid}: route.source inválido")
            continue
        counts[source] += 1
        refs = route.get("card_refs")
        if not isinstance(refs, list) or not refs: errors.append(f"{cid}: route.card_refs vazio")
        quality = route.get("coverage_quality")
        if not isinstance(quality, int) or quality not in {0, 1, 2, 3}:
            errors.append(f"{cid}: coverage_quality deve ser 0..3")
        elif importance == "nuclear" and quality < 2:
            errors.append(f"{cid}: nuclear exige coverage_quality >=2")
        else: covered += 1
        if not str(route.get("coverage_rationale", "")).strip():
            errors.append(f"{cid}: coverage_rationale ausente")
        search = route.get("candidate_search") or {}
        if not isinstance(search.get("queries"), list) or not search.get("queries"):
            errors.append(f"{cid}: candidate_search.queries obrigatório")
        if source == "authored":
            if search.get("anking_count") is None or search.get("external_count") is None:
                errors.append(f"{cid}: autoria exige contagem AnKing e externa")
            if not str(search.get("rejection_rationale", "")).strip():
                errors.append(f"{cid}: autoria exige rejeição documentada das fontes reais")
            if route.get("source_guid"):
                errors.append(f"{cid}: autoral não pode declarar source_guid")
        elif not str(route.get("source_guid", "")).strip():
            errors.append(f"{cid}: cópia real exige source_guid")

        tags = set(row.get("tags") or [])
        expected_tag = {"nuclear": "nucleo", "supporting": "apoio", "optional": "opcional"}.get(importance)
        if expected_tag and expected_tag not in tags: errors.append(f"{cid}: falta tag {expected_tag}")
        if "nucleo" in tags and "opcional" in tags: errors.append(f"{cid}: nucleo e opcional misturados")

    return {"passed": not errors, "errors": errors, "warnings": warnings,
            "concepts": len(concepts), "nuclear": nuclear, "covered": covered,
            "cards_by_source": counts}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--allow-pending-private-source", action="store_true")
    args = parser.parse_args()
    spec = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    result = validate(spec, args.manifest, args.allow_pending_private_source)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
