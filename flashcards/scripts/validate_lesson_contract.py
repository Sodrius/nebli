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
LESSON_SIZES = {"small", "medium", "large"}
CARD_FORMATS = {"cloze", "basic", "image_occlusion"}
ATOMICITY_DECISIONS = {"approved", "exception"}
ATOMICITY_EXCEPTIONS = {"coherent_visual_map"}
IO_BEHAVIORS = {"hide_all_guess_all", "hide_one_guess_one"}
CLOZE_RE = re.compile(r"\{\{c(\d+)::(.*?)(?:::[^}]*)?\}\}", re.I)


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


def _word_count(value: str) -> int:
    clean = re.sub(r"<[^>]+>", " ", value or "")
    return len(re.findall(r"[^\W_]+(?:[-'][^\W_]+)*", clean, flags=re.UNICODE))


def _search_errors(cid: str, search: dict, source: str) -> list[str]:
    errors = []
    families = search.get("query_families") or {}
    nonempty = {
        key for key, values in families.items()
        if isinstance(values, list) and any(str(value).strip() for value in values)
    }
    if search.get("status") != "complete":
        errors.append(f"{cid}: candidate_search.status deve ser complete")
    if not {"pt", "en"} <= nonempty:
        errors.append(f"{cid}: busca exige famílias PT e EN")
    if len(nonempty) < 3:
        errors.append(f"{cid}: busca exige ao menos 3 famílias independentes")
    if search.get("siblings_reviewed") is not True:
        errors.append(f"{cid}: busca exige revisão de cards irmãos/tags")
    if source == "authored":
        if search.get("anking_count") is None or search.get("external_count") is None:
            errors.append(f"{cid}: autoria exige contagem AnKing e externa")
        if not str(search.get("rejection_rationale", "")).strip():
            errors.append(f"{cid}: autoria exige rejeição documentada das fontes reais")
    return errors


def _card_errors(card: dict, known_concepts: set[str], base: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    card_id = str(card.get("id", "")).strip() or "?"
    prefix = f"card {card_id}: "
    concept_ids = card.get("concept_ids")
    if not isinstance(concept_ids, list) or not concept_ids:
        errors.append(prefix + "concept_ids obrigatório")
        concept_ids = []
    unknown = sorted(set(str(value) for value in concept_ids) - known_concepts)
    if unknown:
        errors.append(prefix + "conceitos inexistentes: " + ", ".join(unknown))
    if card.get("source") not in SOURCES:
        errors.append(prefix + "source inválido")
    card_format = card.get("format")
    if card_format not in CARD_FORMATS:
        errors.append(prefix + "format inválido")
    if not str(card.get("retrieval_target", "")).strip():
        errors.append(prefix + "retrieval_target ausente")
    generated = card.get("generated_card_count")
    if not isinstance(generated, int) or isinstance(generated, bool) or generated < 1:
        errors.append(prefix + "generated_card_count deve ser inteiro positivo")
        generated = 0
    elif generated != 1:
        errors.append(prefix + "cada entrada cards[] deve representar exatamente 1 card Anki")

    atomicity = card.get("atomicity") or {}
    decision = atomicity.get("decision")
    if decision not in ATOMICITY_DECISIONS:
        errors.append(prefix + "atomicity.decision inválido")
    if not str(atomicity.get("rationale", "")).strip():
        errors.append(prefix + "atomicity.rationale ausente")
    if decision == "exception":
        if atomicity.get("exception") not in ATOMICITY_EXCEPTIONS:
            errors.append(prefix + "exceção de atomicidade inválida")
        if card_format != "image_occlusion":
            errors.append(prefix + "exceção multi-alvo só vale para IO")
    elif atomicity.get("exception"):
        errors.append(prefix + "atomicity.exception contraditória")

    if card_format == "cloze":
        matches = CLOZE_RE.findall(str(card.get("text", "")))
        if len(matches) != 1:
            errors.append(prefix + "cloze exige uma única ocorrência")
        elif matches[0][0] != "1":
            errors.append(prefix + "cloze deve usar somente c1")
        else:
            words = _word_count(matches[0][1])
            if words < 1:
                errors.append(prefix + "resposta de cloze vazia")
            elif words > 3:
                errors.append(prefix + f"cloze excede 3 palavras ({words})")
            elif words == 3 and not str(card.get("cloze_exception_reason", "")).strip():
                errors.append(prefix + "cloze de 3 palavras exige cloze_exception_reason")
        if len(concept_ids) != 1:
            errors.append(prefix + "cloze atômico exige exatamente um conceito")
    elif card_format == "basic":
        for key in ("prompt", "answer"):
            if not str(card.get(key, "")).strip():
                errors.append(prefix + f"basic exige {key}")
        if len(concept_ids) != 1:
            errors.append(prefix + "basic atômico exige exatamente um conceito")
    elif card_format == "image_occlusion":
        io = card.get("io") or {}
        behavior = io.get("behavior")
        if behavior not in IO_BEHAVIORS:
            errors.append(prefix + "io.behavior inválido")
        masks = io.get("masks")
        if not isinstance(masks, list) or not masks:
            errors.append(prefix + "IO exige masks[]")
            masks = []
        for index, mask in enumerate(masks, start=1):
            label = str(mask.get("label", "")).strip()
            if not label:
                errors.append(prefix + f"máscara {index} sem label")
            box = mask.get("box_px")
            if not isinstance(box, list) or len(box) != 4 or not all(isinstance(v, int) for v in box):
                errors.append(prefix + f"máscara {index} exige box_px com 4 inteiros")
            if mask.get("covers") != "answer_label":
                errors.append(prefix + f"máscara {index} deve cobrir answer_label")
        if len(masks) > 1:
            if behavior != "hide_all_guess_all":
                errors.append(prefix + "IO multi-rótulo exige hide_all_guess_all")
            if decision != "exception" or atomicity.get("exception") != "coherent_visual_map":
                errors.append(prefix + "IO multi-rótulo exige exceção coherent_visual_map")
        qa = io.get("qa") or {}
        for key in ("masks_cover_answer_labels", "visual_clues_remain_visible",
                    "all_answers_hidden", "all_duplicate_labels_masked",
                    "question_preview_reviewed", "answer_preview_reviewed"):
            if qa.get(key) is not True:
                errors.append(prefix + f"io.qa.{key} deve ser true")
        for key in ("question_preview", "answer_preview"):
            raw = str(io.get(key, "")).strip()
            if not raw:
                errors.append(prefix + f"io.{key} ausente")
            elif not _resolve(base, raw).is_file():
                errors.append(prefix + f"io.{key} inexistente: {raw}")
    return errors, generated


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

    budget = spec.get("card_budget") or {}
    if budget.get("lesson_size") not in LESSON_SIZES:
        errors.append("card_budget.lesson_size inválido")
    hard_max = budget.get("hard_max")
    if not isinstance(hard_max, int) or isinstance(hard_max, bool) or hard_max < 1:
        errors.append("card_budget.hard_max deve ser inteiro positivo")
        hard_max = 0
    expected_total = budget.get("expected_total_cards")
    if not isinstance(expected_total, int) or isinstance(expected_total, bool) or expected_total < 1:
        errors.append("card_budget.expected_total_cards deve ser inteiro positivo")
        expected_total = 0
    if not str(budget.get("rationale", "")).strip():
        errors.append("card_budget.rationale obrigatório")
    if hard_max > 60:
        if budget.get("manual_scope_review") != "approved":
            errors.append("teto acima de 60 exige manual_scope_review=approved")
        if not str(budget.get("review_rationale", "")).strip():
            errors.append("teto acima de 60 exige review_rationale")

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
    concept_sources: dict[str, str] = {}
    concept_card_refs: dict[str, list[str]] = {}
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
        concept_sources[cid] = source
        refs = route.get("card_refs")
        if not isinstance(refs, list) or not refs: errors.append(f"{cid}: route.card_refs vazio")
        else: concept_card_refs[cid] = [str(ref) for ref in refs]
        quality = route.get("coverage_quality")
        if not isinstance(quality, int) or quality not in {0, 1, 2, 3}:
            errors.append(f"{cid}: coverage_quality deve ser 0..3")
        elif importance == "nuclear" and quality < 2:
            errors.append(f"{cid}: nuclear exige coverage_quality >=2")
        else: covered += 1
        if not str(route.get("coverage_rationale", "")).strip():
            errors.append(f"{cid}: coverage_rationale ausente")
        search = route.get("candidate_search") or {}
        errors.extend(_search_errors(cid, search, source))
        if source == "authored":
            if route.get("source_guid"):
                errors.append(f"{cid}: autoral não pode declarar source_guid")
        elif not str(route.get("source_guid", "")).strip():
            errors.append(f"{cid}: cópia real exige source_guid")

        tags = set(row.get("tags") or [])
        expected_tag = {"nuclear": "nucleo", "supporting": "apoio", "optional": "opcional"}.get(importance)
        if expected_tag and expected_tag not in tags: errors.append(f"{cid}: falta tag {expected_tag}")
        if "nucleo" in tags and "opcional" in tags: errors.append(f"{cid}: nucleo e opcional misturados")

    cards = spec.get("cards")
    if not isinstance(cards, list) or not cards:
        errors.append("cards[] obrigatório e não vazio")
        cards = []
    card_ids: set[str] = set()
    generated_total = 0
    generated_by_source = {source: 0 for source in SOURCES}
    card_concepts: dict[str, list[str]] = {}
    for card in cards:
        card_id = str(card.get("id", "")).strip()
        if not card_id or card_id in card_ids:
            errors.append(f"card id ausente/duplicado: {card_id or '?'}")
        card_ids.add(card_id)
        card_errors, generated = _card_errors(card, seen, base)
        errors.extend(card_errors)
        generated_total += generated
        if card.get("source") in generated_by_source:
            generated_by_source[card["source"]] += generated
        card_concepts[card_id] = [str(value) for value in (card.get("concept_ids") or [])]
        source = card.get("source")
        for cid in card_concepts[card_id]:
            if cid in concept_sources and source != concept_sources[cid]:
                errors.append(f"card {card_id}: source diverge de route.source de {cid}")

    referenced_cards = {ref for refs in concept_card_refs.values() for ref in refs}
    for cid, refs in concept_card_refs.items():
        for ref in refs:
            if ref not in card_ids:
                errors.append(f"{cid}: card_ref inexistente: {ref}")
            elif cid not in card_concepts.get(ref, []):
                errors.append(f"{cid}: card_ref {ref} não declara o conceito")
    for card_id in sorted(card_ids - referenced_cards):
        errors.append(f"card {card_id}: não referenciado por nenhum conceito")
    if generated_total != expected_total:
        errors.append(
            f"card_budget.expected_total_cards={expected_total} diverge do total previsto={generated_total}"
        )
    if hard_max and generated_total > hard_max:
        errors.append(f"total previsto de cards ({generated_total}) excede hard_max ({hard_max})")

    return {"passed": not errors, "errors": errors, "warnings": warnings,
            "concepts": len(concepts), "nuclear": nuclear, "covered": covered,
            "concepts_by_source": counts, "cards_by_source": generated_by_source,
            "expected_total_cards": generated_total,
            "card_hard_max": hard_max}


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
