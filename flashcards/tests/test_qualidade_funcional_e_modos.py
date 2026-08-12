"""Regressões das três correções de pipeline de 2026-08-12.

1. o relatório card-a-card é derivado do deck, não escrito à mão;
2. a qualidade funcional da recuperação é linteada mecanicamente;
3. a procedência da busca AnKing é declarada com honestidade em vez de
   fabricada quando a coleção não está ao alcance da sessão.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from derivar_validacao_cards import derive  # noqa: E402
from lint_qualidade_funcional import lint_cards  # noqa: E402
from validar_deck_card_a_card import validate_report  # noqa: E402

GENERATOR = SCRIPTS / "gerar_manifesto_ankidroid.py"


def _authored(text, **extra):
    card = {
        "source": "authored",
        "text": text,
        "extra": "Explicação curta em português.",
        "front_language": "en",
        "extra_language": "pt-BR",
        "retrieval_target": extra.pop("retrieval_target", "Uma recuperação específica."),
        "authored_quality": {
            "single_retrieval": True,
            "unambiguous_prompt": True,
            "no_functional_duplicate": True,
            "extra_only_supports_answer": True,
            "medical_english_reviewed": True,
        },
    }
    card.update(extra)
    return card


def _card(key, concept, body):
    return {"card_key": key, "concept_id": concept, "atomic": True, "relevant": True,
            "tier": "nucleo", **body}


# ---------------------------------------------------------------- lint funcional

def test_generic_cloze_answer_is_blocked():
    cards = [_card("c1", "k1", _authored("The innate sensor triggers an {{c1::activation}}."))]
    problems = lint_cards(cards)
    assert any("genérico" in p for p in problems)


def test_answer_leaking_in_the_front_is_blocked():
    cards = [_card("c1", "k1", _authored(
        "The caspase-1 platform activates {{c1::caspase-1}} inside the inflammasome."))]
    assert any("vaza" in p for p in lint_cards(cards))


def test_half_of_a_canonical_pair_requires_justification():
    text = "The inflammasome matures IL-18 and {{c1::IL-1beta}} after caspase cleavage."
    assert any("par" in p for p in lint_cards([_card("c1", "k1", _authored(text))]))
    justified = _authored(text, pair_is_unit_reason="O par IL-1β/IL-18 é a unidade cobrada.")
    assert not any("par" in p for p in lint_cards([_card("c1", "k1", justified)]))


def test_same_answer_twice_is_a_functional_duplicate():
    cards = [
        _card("a", "k1", _authored("Bacterial lipopolysaccharide is sensed by {{c1::TLR4}}.")),
        _card("b", "k2", _authored("Endotoxin from Gram-negative walls binds {{c1::TLR4}}.",
                                   retrieval_target="Outro alvo.")),
    ]
    assert any("mesma resposta" in p for p in lint_cards(cards))


def test_enumeration_front_is_blocked():
    cards = [_card("c1", "k1", _authored(
        "Name three cytoplasmic sensors of viral RNA such as {{c1::MDA5}} in the cytosol."))]
    assert any("enumeração" in p for p in lint_cards(cards))


# ------------------------------------------------------- relatório derivado

def _deck(tmp_path, cards, anchor="o tlr4 reconhece o lipopolissacarideo"):
    e1 = tmp_path / "etapa1.typ"
    e1.write_text("Na membrana plasmatica o TLR4 reconhece o lipopolissacarideo bacteriano.",
                  encoding="utf-8")
    return {
        "metadata": {"uc": "UC03", "prova": "P1", "componente": "Imunologia", "nome_curto": "Inato"},
        "release_gate": {
            "schema": "nebli-e1-deck-release-v1",
            "e1_source": "etapa1.typ",
            "card_budget_hard_max": 10,
            "concepts": [{"concept_id": "k1", "e1_anchor": anchor}],
        },
        "cards": cards,
    }


def test_declared_numbers_cannot_diverge_from_the_real_card(tmp_path):
    """Antes, o relatório dizia cloze_words=1 e o gate acreditava."""
    long_cloze = _authored(
        "The endosomal sensor of double-stranded viral RNA is "
        "{{c1::the Toll-like receptor three}}.")
    deck = _deck(tmp_path, [_card("c1", "k1", long_cloze)])
    path = tmp_path / "deck-data.json"
    path.write_text(json.dumps(deck), encoding="utf-8")
    report = derive(deck, path)
    assert report["cards"][0]["cloze_words"] == 4
    result = validate_report(report, 0.82, 0.06)
    assert not result["ok"]
    assert "cloze_words>3" in result["cards"][0]["failures"]


def test_anchor_absent_from_the_e1_fails_the_derived_report(tmp_path):
    deck = _deck(tmp_path, [_card("c1", "k1", _authored(
        "Bacterial lipopolysaccharide is sensed by {{c1::TLR4}}.",
        anking_search_mode="unavailable",
        anking_deferral_reason="A coleção AnKing vive no tablet e não está ao alcance desta sessão de planejamento."))],
        anchor="frase que nunca apareceu na e1")
    path = tmp_path / "deck-data.json"
    path.write_text(json.dumps(deck), encoding="utf-8")
    report = derive(deck, path)
    assert report["cards"][0]["e1_anchor_ok"] is False
    assert "e1_anchor_ok" in validate_report(report, 0.82, 0.06)["cards"][0]["failures"]


def test_derived_report_passes_for_an_honest_authored_card(tmp_path):
    deck = _deck(tmp_path, [_card("c1", "k1", _authored(
        "Bacterial lipopolysaccharide is sensed by {{c1::TLR4}}.",
        anking_search_mode="unavailable",
        anking_deferral_reason="A coleção AnKing vive no tablet e não está ao alcance desta sessão de planejamento."))])
    path = tmp_path / "deck-data.json"
    path.write_text(json.dumps(deck), encoding="utf-8")
    result = validate_report(derive(deck, path), 0.82, 0.06)
    assert result["ok"], result["cards"]


# --------------------------------------------------- procedência da busca

def test_unavailable_mode_still_demands_a_concrete_reason(tmp_path):
    deck = _deck(tmp_path, [_card("c1", "k1", _authored(
        "Bacterial lipopolysaccharide is sensed by {{c1::TLR4}}.",
        anking_search_mode="unavailable", anking_deferral_reason="sem coleção"))])
    path = tmp_path / "deck-data.json"
    path.write_text(json.dumps(deck), encoding="utf-8")
    result = validate_report(derive(deck, path), 0.82, 0.06)
    assert "anking_deferral_reason_ok" in result["cards"][0]["failures"]


def test_local_source_cannot_claim_that_nobody_will_search(tmp_path):
    card = _card("c1", "k1", {
        "source": "anking",
        "query": "TLR4 lipopolysaccharide",
        "search_queries": ["TLR4 lipopolysaccharide", "LPS innate receptor", "endotoxin sensor"],
        "expected_answers": ["TLR4"],
        "anking_search_mode": "unavailable",
        "fallback": _authored("Bacterial lipopolysaccharide is sensed by {{c1::TLR4}}."),
    })
    deck = _deck(tmp_path, [card])
    path = tmp_path / "deck-data.json"
    path.write_text(json.dumps(deck), encoding="utf-8")
    result = validate_report(derive(deck, path), 0.82, 0.06)
    assert "local_source_without_search" in result["cards"][0]["failures"]


def test_deferred_search_validates_the_plan_not_the_unresolved_result(tmp_path):
    card = _card("c1", "k1", {
        "source": "anking",
        "query": "TLR4 lipopolysaccharide",
        "search_queries": ["TLR4 lipopolysaccharide", "LPS innate receptor", "endotoxin sensor"],
        "expected_answers": ["TLR4"],
        "anking_search_mode": "device_deferred",
        "anking_deferral_reason": "A busca roda no Companion, único ponto do fluxo com a coleção AnKing real.",
        "fallback": _authored("Bacterial lipopolysaccharide is sensed by {{c1::TLR4}}."),
    })
    deck = _deck(tmp_path, [card])
    path = tmp_path / "deck-data.json"
    path.write_text(json.dumps(deck), encoding="utf-8")
    result = validate_report(derive(deck, path), 0.82, 0.06)
    assert result["ok"], result["cards"]

    card["anking_required"] = True
    result = validate_report(derive(deck, path), 0.82, 0.06)
    assert "deferred_search_cannot_be_anking_required" in result["cards"][0]["failures"]


def test_generator_rejects_a_deck_that_fails_the_functional_lint(tmp_path):
    e1 = tmp_path / "etapa1.typ"
    e1.write_text("Na membrana plasmatica o TLR4 reconhece o lipopolissacarideo bacteriano.",
                  encoding="utf-8")
    pdf = tmp_path / "Inato - E1.pdf"
    pdf.write_bytes(b"%PDF-1.4\nNEBLI\n")
    card = _card("c1", "k1", _authored(
        "The innate sensor triggers an {{c1::activation}} of the cell response.",
        anking_search_mode="unavailable",
        anking_deferral_reason="A coleção AnKing vive no tablet e não está ao alcance desta sessão de planejamento."))
    deck = {
        "metadata": {"uc": "UC03", "prova": "P1", "componente": "Imunologia", "nome_curto": "Inato"},
        "release_gate": {
            "schema": "nebli-e1-deck-release-v1",
            "e1_source": "etapa1.typ",
            "e1_source_sha256": hashlib.sha256(e1.read_bytes()).hexdigest(),
            "e1_pdf": "Inato - E1.pdf",
            "e1_pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
            "card_budget_hard_max": 10,
            "e1_review": {
                "slide_inventory_complete": True, "objectives_covered": True,
                "core_coverage_complete": True, "mechanisms_explicit": True,
                "visual_information_explained": True, "core_study_without_slides": True,
                "step1_depth_reviewed": True, "card_content_anchored": True,
                "independent_review_passed": True, "notes_review_status": "covered",
                "unresolved_core_omissions": [], "unresolved_ambiguities": [],
                "summary": "Revisão concluída.",
            },
            "concepts": [{
                "concept_id": "k1", "importance": "nuclear",
                "e1_anchor": "o TLR4 reconhece o lipopolissacarideo",
                "coverage_quality": 3, "card_keys": ["c1"],
                "step1": {"decision": "not_applicable"},
            }],
        },
        "cards": [card],
    }
    path = tmp_path / "deck-data.json"
    path.write_text(json.dumps(deck, ensure_ascii=False), encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(GENERATOR), "--slug", "inato", "--deck-data", str(path),
         "--out", str(tmp_path / "out.json")],
        capture_output=True, text=True,
    )
    assert proc.returncode != 0
    assert "lint de qualidade funcional" in (proc.stderr + proc.stdout)
