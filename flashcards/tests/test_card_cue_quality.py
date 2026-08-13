import sys
from pathlib import Path


SCRIPTS = Path(__file__).parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from card_cue_quality import (  # noqa: E402
    deterministic_cue_failures,
    portuguese_front_failures,
    semantic_cue_review_failures,
)


def reviewed(text: str) -> dict:
    return {
        "text": text,
        "authored_quality": {"portuguese_reviewed": True},
        "cue_quality": {
            "cloze_role": "mecanismo",
            "knowledge_required": True,
            "grammar_only_solvable": False,
            "lexical_leak": False,
            "answer_visible_elsewhere": False,
            "blind_review_passed": True,
            "plausible_alternatives": [],
            "confounders_checked": ["morfologia"],
            "ambiguity_review": "O mecanismo é determinado pela pista patológica específica.",
        },
    }


def test_portuguese_front_passes_and_english_prose_fails():
    assert portuguese_front_failures(
        "A fixação imediata impede a {{c1::autólise}}.", "pt-BR"
    ) == []
    failures = portuguese_front_failures(
        "The tissue is preserved by {{c1::fixation}} during processing.", "pt-BR"
    )
    assert "front_appears_english" in failures


def test_visible_answer_is_a_deterministic_leak():
    failures = deterministic_cue_failures(
        "A autólise é evitada pela prevenção da {{c1::autólise}}."
    )
    assert "cloze_answer_visible_in_prompt" in failures


def test_semantic_review_requires_knowledge_and_blind_review():
    card = reviewed("A fixação imediata impede a {{c1::autólise}}.")
    assert semantic_cue_review_failures(card, strict=True) == []
    card["cue_quality"]["grammar_only_solvable"] = True
    card["cue_quality"]["plausible_alternatives"] = ["degradação"]
    failures = semantic_cue_review_failures(card, strict=True)
    assert "cue_quality.grammar_only_solvable" in failures
    assert "cue_quality.unresolved_plausible_alternatives" in failures
