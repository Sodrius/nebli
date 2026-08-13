#!/usr/bin/env python3
"""Regras compartilhadas de idioma e qualidade cognitiva para clozes NEBLI."""
from __future__ import annotations

import re
import unicodedata
from typing import Any


CLOZE_RE = re.compile(r"\{\{c(\d+)::([^}:]+)(?:::[^}]*)?}}", re.I | re.S)
PT_LANGUAGES = {"pt", "pt-br"}
CLOZE_ROLES = {
    "mecanismo",
    "consequencia",
    "discriminador",
    "valor",
    "direcao",
    "rotulo_especifico",
}

# Um termo médico em inglês pode aparecer legitimamente em uma frente portuguesa.
# O gate só acusa prosa inglesa quando vários conectores muito frequentes aparecem.
ENGLISH_FUNCTION_WORDS = {
    "the", "an", "is", "are", "was", "were", "by", "with", "when",
    "which", "that", "from", "into", "during", "because", "requires", "uses",
}


def _plain(value: str) -> str:
    return re.sub(r"<[^>]+>", " ", value or "")


def _normalise(value: str) -> str:
    value = unicodedata.normalize("NFKD", _plain(value))
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def visible_stem(text: str) -> str:
    return CLOZE_RE.sub(" ", text or "")


def cloze_answers(text: str) -> list[str]:
    return [match.group(2).strip() for match in CLOZE_RE.finditer(text or "")]


def deterministic_cue_failures(text: str) -> list[str]:
    """Detecta vazamentos verificáveis sem tentar substituir a revisão semântica."""
    failures: list[str] = []
    answers = cloze_answers(text)
    if len(answers) != 1:
        return failures
    answer = _normalise(answers[0])
    stem = _normalise(visible_stem(text))
    if answer and re.search(rf"(?:^| ){re.escape(answer)}(?: |$)", stem):
        failures.append("cloze_answer_visible_in_prompt")
    return failures


def portuguese_text_failures(text: str, language: str, field: str) -> list[str]:
    failures: list[str] = []
    if str(language or "").casefold() not in PT_LANGUAGES:
        failures.append(f"{field}_language_not_pt")
    markers = sum(
        word in ENGLISH_FUNCTION_WORDS
        for word in _normalise(visible_stem(text)).split()
    )
    if markers >= 3:
        failures.append(f"{field}_appears_english")
    return failures


def portuguese_front_failures(text: str, language: str) -> list[str]:
    return portuguese_text_failures(text, language, "front")


def semantic_cue_review_failures(card: dict[str, Any], *, strict: bool) -> list[str]:
    failures = deterministic_cue_failures(str(card.get("text") or ""))
    if not strict:
        return failures

    authored = card.get("authored_quality")
    if not isinstance(authored, dict):
        failures.append("authored_quality_missing")
    elif authored.get("portuguese_reviewed") is not True:
        failures.append("authored_quality.portuguese_reviewed")

    cue = card.get("cue_quality")
    if not isinstance(cue, dict):
        failures.append("cue_quality_missing")
        return failures

    role = str(cue.get("cloze_role") or "").casefold()
    if role not in CLOZE_ROLES:
        failures.append("cue_quality.cloze_role")
    for key in ("knowledge_required", "blind_review_passed"):
        if cue.get(key) is not True:
            failures.append(f"cue_quality.{key}")
    for key in ("grammar_only_solvable", "lexical_leak", "answer_visible_elsewhere"):
        if cue.get(key) is not False:
            failures.append(f"cue_quality.{key}")

    alternatives = cue.get("plausible_alternatives")
    if not isinstance(alternatives, list):
        failures.append("cue_quality.plausible_alternatives_must_be_list")
    elif alternatives:
        failures.append("cue_quality.unresolved_plausible_alternatives")
    confounders = cue.get("confounders_checked")
    if not isinstance(confounders, list):
        failures.append("cue_quality.confounders_checked_must_be_list")
    if len(str(cue.get("ambiguity_review") or "").strip()) < 20:
        failures.append("cue_quality.ambiguity_review")
    return failures
