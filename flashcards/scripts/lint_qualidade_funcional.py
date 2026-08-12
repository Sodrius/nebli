#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lint mecânico da qualidade FUNCIONAL da recuperação (ERROS.md 36–47).

Motivação
---------
Até aqui, todas as regras de "o card é bom?" viviam apenas em prosa. O gate
card-a-card checava forma (um `c1`, cloze curto, Extra em português) e nada
impedia um card formalmente perfeito de cobrar uma palavra genérica, vazar a
resposta na própria frente, esconder metade de um par canônico ou repetir a
recuperação de outro card. Este módulo transforma essas regras em checagens
executáveis sobre o texto real do card.

Escopo: só o que é decidível pelo conteúdo. Julgamentos de mérito continuam
declarados (`atomic`, `relevant`, `authored_quality`), mas deixam de ser a
única barreira.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any, Iterable

CLOZE_RE = re.compile(r"\{\{c(\d+)::([^}:]+)(?:::[^}]*)?}}", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")

# Respostas que a gramática entrega ou que aceitam vários sinônimos defensáveis.
# ERROS.md 37 e 43.
GENERIC_ANSWERS = {
    # inglês
    "activation", "adaptation", "answer", "change", "context", "death",
    "decrease", "destruction", "elimination", "function", "increase",
    "inflammation", "mechanism", "migration", "modulation", "plasticity",
    "process", "production", "regulation", "release", "response", "signal",
    "signaling", "signalling", "stimulus", "cell", "cells", "molecule",
    "protein", "receptor", "pathway", "effect", "result", "action",
    # português
    "adaptacao", "ativacao", "contexto", "destruicao", "eliminacao",
    "inflamacao", "mecanismo", "migracao", "morte", "plasticidade",
    "processo", "producao", "regulacao", "resposta", "sinal", "via",
}

ENUMERATION_RE = re.compile(
    r"\b(list|lists|name (?:two|three|four|the two|the three)|which two|which three|"
    r"cite|enumerate|give (?:two|three)|both .* and .*\?)\b",
    re.I,
)

# "X and {{c1::Y}}" — mostrar metade do par canônico e cobrar a outra metade.
HALF_PAIR_RE = re.compile(
    r"\b([A-Za-zÀ-ÿ0-9\-]{2,})\s+(?:and|e|or|ou|/)\s+\{\{c1::", re.I
)

MULTI_ANSWER_RE = re.compile(r"[,;/]|\band\b|\bor\b|\be\b|\bou\b", re.I)


def _strip_tags(text: str) -> str:
    return TAG_RE.sub(" ", text or "")


def _fold(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", text).strip().casefold()


def _words(text: str) -> list[str]:
    return [w for w in re.split(r"[^\wÀ-ÿ\-]+", _fold(text)) if w]


def _visible_front(text: str) -> str:
    """Frente como o aluno vê na pergunta: cloze substituído pela lacuna."""
    return _strip_tags(CLOZE_RE.sub(" [...] ", text or ""))


def _authored_bodies(card: dict[str, Any]) -> Iterable[tuple[str, dict[str, Any]]]:
    """Devolve (rótulo, corpo autoral) de um card e do seu fallback autoral."""
    key = str(card.get("card_key") or "?")
    if str(card.get("source") or "").lower() == "authored":
        yield key, card
    fallback = card.get("fallback")
    if isinstance(fallback, dict) and str(fallback.get("source") or "").lower() == "authored":
        yield f"{key}.fallback", fallback


def lint_authored(where: str, card: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    text = str(card.get("text") or "")
    matches = list(CLOZE_RE.finditer(text))
    if len(matches) != 1:
        # forma já é barrada pelo gerador; aqui só evitamos falso positivo
        return problems
    answer = _strip_tags(matches[0].group(2)).strip()
    answer_folded = _fold(answer)
    visible = _visible_front(text)

    if answer_folded in GENERIC_ANSWERS and not str(card.get("generic_answer_reason") or "").strip():
        # a lista bloqueia o uso preguiçoso; quando o termo comum É a resposta
        # precisa, o card registra por escrito o que torna a pista determinante
        problems.append(f"{where}: cloze genérico/previsível: {answer!r} (ERROS 37/43)")

    if MULTI_ANSWER_RE.search(answer):
        problems.append(f"{where}: cloze cobra mais de uma resposta: {answer!r} (ERROS 13/44)")

    # vazamento: a resposta (ou uma palavra longa dela) reaparece na parte visível
    for token in _words(answer):
        if len(token) >= 4 and token in _words(visible):
            problems.append(
                f"{where}: a resposta {answer!r} vaza na frente (token {token!r}) (ERROS 44)"
            )
            break

    if ENUMERATION_RE.search(visible):
        problems.append(f"{where}: frente pede enumeração/lista (ERROS 13)")

    half_pair = HALF_PAIR_RE.search(text)
    if half_pair and not str(card.get("pair_is_unit_reason") or "").strip():
        problems.append(
            f"{where}: mostra {half_pair.group(1)!r} e esconde só o par; "
            "exige pair_is_unit_reason (ERROS 38)"
        )

    if len(visible.replace("[...]", "").strip()) < 25:
        problems.append(f"{where}: frente curta demais para tornar a resposta inequívoca")

    return problems


def lint_io(where: str, card: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    answers = card.get("answers")
    if isinstance(answers, list):
        folded = [_fold(str(a)) for a in answers]
        if len(set(folded)) != len(folded):
            problems.append(f"{where}: IO com respostas repetidas (ERROS 21)")
        for answer in folded:
            if answer in GENERIC_ANSWERS:
                problems.append(f"{where}: máscara IO cobra rótulo genérico: {answer!r}")
    return problems


def lint_cards(cards: list[dict[str, Any]]) -> list[str]:
    problems: list[str] = []
    answers_seen: dict[str, str] = {}
    targets_seen: dict[str, str] = {}

    for card in cards:
        if not isinstance(card, dict):
            continue
        key = str(card.get("card_key") or "?")
        if str(card.get("source") or "").lower() == "io":
            problems.extend(lint_io(key, card))

        for where, body in _authored_bodies(card):
            problems.extend(lint_authored(where, body))

            matches = list(CLOZE_RE.finditer(str(body.get("text") or "")))
            if len(matches) == 1:
                answer = _fold(_strip_tags(matches[0].group(2)))
                # a mesma resposta em dois cards é duplicata funcional até prova
                # em contrário (ERROS 12/13/44)
                if answer in answers_seen and answers_seen[answer].split(".")[0] != key:
                    if not str(body.get("duplicate_answer_reason") or "").strip():
                        problems.append(
                            f"{where}: mesma resposta de {answers_seen[answer]} "
                            f"({answer!r}); exige duplicate_answer_reason (ERROS 12)"
                        )
                answers_seen.setdefault(answer, where)

            target = _fold(str(body.get("retrieval_target") or ""))
            if target:
                if target in targets_seen and targets_seen[target].split(".")[0] != key:
                    problems.append(
                        f"{where}: retrieval_target idêntico ao de {targets_seen[target]} (ERROS 12)"
                    )
                targets_seen.setdefault(target, where)

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck_data", type=Path)
    args = parser.parse_args()
    data = json.loads(args.deck_data.read_text(encoding="utf-8"))
    cards = data.get("cards") if isinstance(data.get("cards"), list) else []
    problems = lint_cards(cards)
    for problem in problems:
        print(problem)
    print(f"cards={len(cards)} problemas={len(problems)}")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
