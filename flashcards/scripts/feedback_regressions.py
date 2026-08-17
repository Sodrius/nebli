#!/usr/bin/env python3
"""Aplica, como gate, os defeitos que o usuário já apontou uma vez.

O registro fica em `flashcards/tests/feedback_regressions.json`. A maior parte
das entradas é coberta por uma regra estrutural do validador — idioma, cloze
múltiplo, resposta abstrata, ablação, orçamento. Restam os erros de **conteúdo**,
que nenhuma regra estrutural alcança: quando o usuário diz que `-trofia` responde
por desenvolvimento e não por crescimento, só um par proibido explícito impede a
reincidência.

Este módulo aplica esses pares. Cada um nasce de um comentário real e morre
quando o card certo passa a existir.
"""
from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
from typing import Any

REGISTRY = Path(__file__).resolve().parents[1] / "tests" / "feedback_regressions.json"
CLOZE_RE = re.compile(r"\{\{c(\d+)::([^}:]+)(?:::[^}]*)?}}", re.I | re.S)


def _normalise(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


@lru_cache(maxsize=1)
def load(path: str | None = None) -> dict[str, Any]:
    return json.loads(Path(path or REGISTRY).read_text(encoding="utf-8"))


def forbidden_pairs() -> list[dict[str, Any]]:
    return [entry for entry in load().get("regressions", []) if entry.get("forbidden_pair")]


def regression_failures(card: dict[str, Any]) -> list[str]:
    """Reprova o card que repete um erro de conteúdo já apontado."""
    text = str(card.get("text") or "")
    stem = _normalise(CLOZE_RE.sub(" ", text))
    answers = {_normalise(match.group(2)) for match in CLOZE_RE.finditer(text)}
    failures: list[str] = []
    for entry in forbidden_pairs():
        pair = entry["forbidden_pair"]
        needle = _normalise(str(pair.get("stem_contains") or ""))
        answer = _normalise(str(pair.get("answer_is") or ""))
        if needle and answer and needle in stem and answer in answers:
            failures.append(f"regression:{entry['id']}")
    return failures
