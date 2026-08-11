import hashlib
import json
import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "gerar_manifesto_ankidroid.py"
FINALIZER = Path(__file__).parents[1] / "scripts" / "finalizar_entrega_canonica.py"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def authored_fallback():
    return {
        "source": "authored",
        "text": "Bacterial lipopolysaccharide is sensed by {{c1::TLR4}}.",
        "extra": "O TLR4 reconhece LPS bacteriano na imunidade inata.",
        "front_language": "en",
        "extra_language": "pt-BR",
        "retrieval_target": "Identificar o receptor inato que reconhece LPS.",
        "authored_quality": {
            "single_retrieval": True,
            "unambiguous_prompt": True,
            "no_functional_duplicate": True,
            "extra_only_supports_answer": True,
            "medical_english_reviewed": True,
        },
    }


def canonical_data(tmp_path: Path) -> dict:
    e1 = tmp_path / "etapa1.typ"
    e1.write_text(
        "O lipopolissacarídeo bacteriano é reconhecido pelo TLR4 na membrana, "
        "iniciando a resposta imune inata.",
        encoding="utf-8",
    )
    pdf = tmp_path / "Reconhecimento inato - E1.pdf"
    pdf.write_bytes(b"%PDF-1.4\nNEBLI E1\n")
    card = {
        "card_key": "tlr4-lps",
        "concept_id": "c-tlr4",
        "source": "anking",
        "query": "TLR4 lipopolysaccharide innate immune recognition",
        "aliases": ["TLR4 LPS recognition"],
        "search_queries": [
            "TLR4 lipopolysaccharide innate immune recognition",
            "TLR4 LPS recognition",
        ],
        "expected_answers": ["TLR4"],
        "anking_required": True,
        "atomic": True,
        "relevant": True,
        "tier": "nucleo",
        "fallback": authored_fallback(),
    }
    return {
        "metadata": {
            "uc": "UC03",
            "prova": "P1",
            "componente": "Imunologia",
            "nome_curto": "Reconhecimento inato",
        },
        "release_gate": {
            "schema": "nebli-e1-deck-release-v1",
            "e1_source": e1.name,
            "e1_source_sha256": sha(e1),
            "e1_pdf": pdf.name,
            "e1_pdf_sha256": sha(pdf),
            "card_budget_hard_max": 25,
            "e1_review": {
                "slide_inventory_complete": True,
                "objectives_covered": True,
                "core_coverage_complete": True,
                "mechanisms_explicit": True,
                "visual_information_explained": True,
                "core_study_without_slides": True,
                "step1_depth_reviewed": True,
                "card_content_anchored": True,
                "independent_review_passed": True,
                "notes_review_status": "unavailable",
                "unresolved_core_omissions": [],
                "unresolved_ambiguities": [],
                "summary": "E1 cobre o core da aula e integra apenas o aprofundamento diretamente útil.",
            },
            "concepts": [{
                "concept_id": "c-tlr4",
                "importance": "nuclear",
                "e1_anchor": "O lipopolissacarídeo bacteriano é reconhecido pelo TLR4 na membrana",
                "coverage_quality": 3,
                "card_keys": ["tlr4-lps"],
                "step1": {
                    "decision": "incorporated",
                    "same_theme": True,
                    "source_ref": "AnKing TLR4/LPS note",
                    "rationale": "Explicita o receptor do mecanismo apresentado no slide.",
                },
            }],
        },
        "cards": [card],
    }


def run_canonical(tmp_path: Path, data: dict):
    deck = tmp_path / "deck-data.json"
    deck.write_text(json.dumps(data), encoding="utf-8")
    out = tmp_path / "lesson.ankidroid.json"
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--slug", "reconhecimento-inato",
         "--deck-data", str(deck), "--out", str(out)],
        capture_output=True,
        text=True,
    )
    return proc, out


def direct_authored_card() -> dict:
    return {
        "card_key": "tlr4-lps",
        "concept_id": "c-tlr4",
        "tier": "nucleo",
        "atomic": True,
        "relevant": True,
        **authored_fallback(),
        "anking_search_complete": True,
        "anking_search_queries": [
            "TLR4 lipopolysaccharide recognition",
            "TLR4 LPS innate immunity",
            "bacterial LPS pattern recognition receptor",
        ],
        "anking_search_scope_expanded": True,
        "anking_siblings_reviewed": True,
        "anking_candidates_reviewed": 0,
        "anking_rejection_reason": "No exact AnKing retrieval remained after expanded sibling review.",
    }


def test_canonical_release_binds_reviewed_e1_core_and_anking(tmp_path):
    proc, out = run_canonical(tmp_path, canonical_data(tmp_path))
    assert proc.returncode == 0, proc.stderr
    manifest = json.loads(out.read_text(encoding="utf-8"))
    assert manifest["release_gate"]["passed"] is True
    assert manifest["release_gate"]["nuclear_concept_count"] == 1
    assert manifest["release_gate"]["covered_nuclear_count"] == 1
    assert manifest["cards"][0]["anking_required"] is True
    assert "etapa1.typ" not in json.dumps(manifest)


def test_missing_e1_semantic_review_blocks_release(tmp_path):
    data = canonical_data(tmp_path)
    data["release_gate"]["e1_review"]["core_study_without_slides"] = False
    proc, out = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert not out.exists()
    assert "core_study_without_slides" in (proc.stdout + proc.stderr)


def test_nuclear_concept_without_quality_two_blocks_release(tmp_path):
    data = canonical_data(tmp_path)
    data["release_gate"]["concepts"][0]["coverage_quality"] = 1
    proc, _ = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert "coverage_quality" in (proc.stdout + proc.stderr)


def test_anking_card_cannot_be_silently_replaced_by_fallback(tmp_path):
    data = canonical_data(tmp_path)
    data["cards"][0]["anking_required"] = False
    proc, _ = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert "anking_required=true" in (proc.stdout + proc.stderr)


def test_direct_authorship_requires_broad_documented_anking_search(tmp_path):
    data = canonical_data(tmp_path)
    card = data["cards"][0]
    card.clear()
    card.update({
        "card_key": "tlr4-lps",
        "concept_id": "c-tlr4",
        "tier": "nucleo",
        "atomic": True,
        "relevant": True,
        **authored_fallback(),
        "anking_search_complete": True,
        "anking_search_queries": ["TLR4"],
        "anking_search_scope_expanded": True,
        "anking_siblings_reviewed": True,
        "anking_candidates_reviewed": 0,
        "anking_rejection_reason": "No exact AnKing retrieval remained after expanded review.",
    })
    proc, _ = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert "3 buscas AnKing" in (proc.stdout + proc.stderr)


def test_authored_card_can_reuse_didactic_anking_image_without_embedding_bytes(tmp_path):
    data = canonical_data(tmp_path)
    card = direct_authored_card()
    card["anking_images"] = [{
        "key": "tlr4_visual",
        "query": "TLR4 lipopolysaccharide plasma membrane",
        "search_queries": [
            "TLR4 lipopolysaccharide plasma membrane",
            "TLR4 LPS membrane receptor",
        ],
        "expected_answers": ["TLR4"],
        "media_index": 0,
        "cognitive_purpose": "Relacionar o receptor ao ligante e à localização de membrana.",
        "didactic_value_reviewed": True,
    }]
    data["cards"] = [card]
    proc, out = run_canonical(tmp_path, data)
    assert proc.returncode == 0, proc.stderr
    manifest = json.loads(out.read_text(encoding="utf-8"))
    generated = manifest["cards"][0]
    assert generated["anking_media_refs"][0]["key"] == "tlr4_visual"
    assert "nebli-anking-media://tlr4_visual" in generated["extra"]
    assert manifest["media"] == []


def test_slide_image_is_blocked_without_prior_anking_visual_rejection(tmp_path):
    image = tmp_path / "slide.png"
    image.write_bytes(b"real-slide-image")
    data = canonical_data(tmp_path)
    card = direct_authored_card()
    card["extra_images"] = [{
        "path": image.name,
        "source_credit": "Slide 12 da aula",
        "cognitive_purpose": "Distinguir receptor, ligante e localização no esquema.",
        "didactic_value_reviewed": True,
    }]
    data["cards"] = [card]
    proc, out = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert not out.exists()
    assert "busca visual AnKing completa" in (proc.stdout + proc.stderr)


def test_slide_image_with_didactic_evidence_is_embedded_and_auditable(tmp_path):
    image = tmp_path / "slide.png"
    image.write_bytes(b"real-slide-image")
    data = canonical_data(tmp_path)
    card = direct_authored_card()
    card["extra_images"] = [{
        "path": image.name,
        "source_credit": "Slide 12 da aula",
        "cognitive_purpose": "Distinguir receptor, ligante e localização no esquema.",
        "didactic_value_reviewed": True,
        "anking_visual_search_complete": True,
        "anking_visual_rejection_reason": (
            "No AnKing image represented the lesson-specific scheme without distracting labels."
        ),
    }]
    data["cards"] = [card]
    proc, out = run_canonical(tmp_path, data)
    assert proc.returncode == 0, proc.stderr
    manifest = json.loads(out.read_text(encoding="utf-8"))
    generated = manifest["cards"][0]
    assert generated["visual_evidence"][0]["didactic_value_reviewed"] is True
    assert generated["visual_evidence"][0]["origin"] == "slide_or_external"
    assert len(manifest["media"]) == 1


def test_io_canonical_contract_is_hide_two_guess_two(tmp_path):
    image = tmp_path / "io.png"
    image.write_bytes(b"real-io-image")
    data = canonical_data(tmp_path)
    io = {
        "card_key": "tlr4-lps",
        "concept_id": "c-tlr4",
        "source": "io",
        "tier": "nucleo",
        "atomic": True,
        "relevant": True,
        "mode": "hide_two_guess_two",
        "image_path": image.name,
        "answers": ["TLR4", "LPS"],
        "pair_rationale": "Receptor and ligand form a single coherent recognition pair.",
        "masks": [
            {"x": 0.1, "y": 0.1, "w": 0.2, "h": 0.1},
            {"x": 0.6, "y": 0.6, "w": 0.2, "h": 0.1},
        ],
        "coherent_set": True,
        "masks_labels_not_structures": True,
        "question_preview_validated": True,
        "answer_preview_validated": True,
        "visual_ok": True,
        "real_source": True,
        "answer_leak": False,
        "source_credit": "Slide 12 da aula",
        "cognitive_purpose": "Recuperar conjuntamente o receptor e o ligante do mecanismo.",
        "didactic_value_reviewed": True,
        "anking_search_complete": True,
        "anking_search_queries": ["TLR4 LPS", "TLR4 receptor", "LPS innate immunity"],
        "anking_search_scope_expanded": True,
        "anking_siblings_reviewed": True,
        "anking_candidates_reviewed": 0,
        "anking_rejection_reason": "No exact AnKing retrieval replaced this label-localization task.",
    }
    data["cards"] = [io]
    proc, out = run_canonical(tmp_path, data)
    assert proc.returncode == 0, proc.stderr
    assert json.loads(out.read_text(encoding="utf-8"))["cards"][0]["mode"] == "hide_two_guess_two"

    io["masks"].append({"x": 0.3, "y": 0.3, "w": 0.1, "h": 0.1})
    io["answers"].append("MyD88")
    proc, _ = run_canonical(tmp_path, data)
    assert proc.returncode != 0
    assert "no máximo 2 máscaras" in (proc.stdout + proc.stderr)


def test_finalizer_materializes_only_user_visible_e1_and_manifest(tmp_path):
    data = canonical_data(tmp_path)
    deck = tmp_path / "deck-data.json"
    deck.write_text(json.dumps(data), encoding="utf-8")
    report = tmp_path / "validacao-cards.json"
    report.write_text(json.dumps({
        "expected_card_count": 1,
        "card_budget_hard_max": 25,
        "cards": [{
            "card_key": "tlr4-lps",
            "concept_id": "c-tlr4",
            "source": "anking",
            "tier": "nucleo",
            "selected": True,
            "atomic": True,
            "relevant": True,
            "e1_anchor_ok": True,
            "source_safe": True,
            "same_note_type": True,
            "same_fields": True,
            "media_ok": True,
            "sibling_policy_ok": True,
            "fallback_validated": True,
            "search_queries_ok": True,
            "expected_answers_ok": True,
            "anking_marker_ok": True,
            "anking_required": True,
            "resolved_without_fallback": True,
            "score": 0.94,
            "second_score": 0.60,
            "exact_phrase": True,
            "requires_visual": False,
        }],
    }), encoding="utf-8")
    out = tmp_path / "entrega"
    proc = subprocess.run(
        [sys.executable, str(FINALIZER), "--slug", "reconhecimento-inato",
         "--deck-data", str(deck), "--validation-report", str(report),
         "--out-dir", str(out)],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    assert sorted(path.name for path in out.iterdir()) == [
        "Reconhecimento inato - E1.pdf",
        "reconhecimento-inato.ankidroid.json",
    ]
