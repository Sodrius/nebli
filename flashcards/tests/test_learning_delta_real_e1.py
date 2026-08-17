import copy, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from validar_ganho_aula import validate_learning_delta

ROOT = Path(__file__).parents[2]
REAL_E1 = ROOT / "typst-build" / "_par_histo-07-osseo" / "etapa1.typ"


def _real_case():
    text = REAL_E1.read_text(encoding="utf-8")
    assert "No resumo anterior fechamos a cartilagem" in text
    assert "matriz extracelular" in text and "mineralizada" in text
    return {
        "curriculum_context": {
            "current_lesson": {"id": "histo-07-osseo", "title": "Tecido ósseo"},
            "prior_lessons": [{"id": "histo-cartilagem", "title": "Cartilagem"}],
        },
        "release_gate": {
            "learning_delta_review": {
                "whole_lesson_read_before_cards": True,
                "master_sheet_context_used": True,
                "claims_classified_before_authorship": True,
                "source_materials": [str(REAL_E1.relative_to(ROOT)), "planilha-mestra"],
                "summary": "A aula usa cartilagem como base anterior e ensina como novidade a matriz óssea mineralizada.",
            },
            "concepts": [
                {
                    "concept_id": "cartilagem-base",
                    "learning_role": "revisao",
                    "curriculum_ref": "histo-cartilagem",
                    "teaching_evidence": [{
                        "source": "e1",
                        "locator": "1.1 De onde vem e por que importa",
                        "rationale": "A própria E1 marca o conteúdo de cartilagem como pertencente ao resumo anterior.",
                    }],
                    "retention_class": "e1_only",
                    "exclusion_reason": "Serve de comparação e pré-requisito; não é o ganho novo da aula de osso.",
                    "e1_anchor": "No resumo anterior fechamos a cartilagem como conjuntivo especializado de matriz hidratada, avascular",
                    "card_keys": [],
                },
                {
                    "concept_id": "mineralizacao-ossea",
                    "learning_role": "foco_novo",
                    "lesson_gain": "A mineralização por hidroxiapatita muda as propriedades mecânicas e fisiológicas da matriz óssea.",
                    "curriculum_ref": "histo-07-osseo",
                    "teaching_evidence": [{
                        "source": "e1",
                        "locator": "1.1–1.3 — identidade, solução mecânica e composição",
                        "rationale": "A E1 desenvolve repetidamente mineralização, hidroxiapatita e suas consequências como eixo da aula.",
                    }],
                    "retention_class": "must_recall",
                    "e1_anchor": "Essa mineralização muda quatro coisas de uma vez",
                    "card_keys": ["osseo-mineralizacao-01"],
                },
            ],
        },
        "cards": [{"card_key": "osseo-mineralizacao-01", "concept_id": "mineralizacao-ossea"}],
    }


def test_real_e1_excludes_recap_and_keeps_lesson_gain():
    data = _real_case()
    result = validate_learning_delta(data)
    assert result["passed"], result["errors"]
    assert result["card_eligible_concepts"] == 1
    assert result["excluded_support_concepts"] == 1


def test_real_e1_blocks_card_for_previous_cartilage_content():
    data = _real_case()
    bad = copy.deepcopy(data)
    bad["release_gate"]["concepts"][0]["card_keys"] = ["cartilagem-revisao-01"]
    bad["cards"].append({"card_key": "cartilagem-revisao-01", "concept_id": "cartilagem-base"})
    result = validate_learning_delta(bad)
    assert not result["passed"]
    assert any("learning_role=revisao não pode ter card_keys" in error for error in result["errors"])
    assert any("não representa ganho da aula" in error for error in result["errors"])
