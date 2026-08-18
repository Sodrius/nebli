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

# Um termo médico em inglês pode aparecer legitimamente em uma frente portuguesa
# ("hairpins", "pre-BCR", "Ku70/Ku80"), então o gate nunca olha termos técnicos:
# conta apenas marcadores de prosa inglesa que não existem em português.
#
# Palavras como "a", "e", "as", "da", "do", "no", "na" ficam de fora de propósito:
# são artigos e preposições portuguesas e acusariam frases corretas.
ENGLISH_FUNCTION_WORDS = {
    "the", "an", "is", "are", "was", "were", "by", "with", "when",
    "which", "that", "from", "into", "during", "because", "requires", "uses",
    "of", "in", "to", "and", "for", "its", "can", "may", "does", "than",
    "both", "after", "before", "without", "through", "between", "each",
    "this", "these", "their", "not", "only", "also", "but", "while",
    "whereas", "occurs", "contains", "leaves", "produces", "determines",
    "called", "unlike", "besides", "yields", "follows", "belongs",
    "within", "against", "across", "below", "above", "such", "still",
    "able", "first", "second", "higher", "lower", "increasing", "using",
    "require", "requires", "prevents", "preserves", "identifies", "improves",
    "reduces", "insert", "inserts", "specific",
}

# Duas ocorrências já caracterizam prosa inglesa. O limiar antigo (três) deixava
# passar as frases curtas e técnicas, que são a maioria num deck médico.
ENGLISH_MARKER_THRESHOLD = 2

# Respostas abstratas que servem a qualquer frase e não exigem conhecimento
# médico. Bilíngue porque o deck já saiu em inglês uma vez.
ABSTRACT_ANSWERS = {
    # herdadas do gate anterior
    "coisa", "processo", "estrutura", "funcao", "mecanismo", "elemento",
    "substancia",
    # medidas no deck UC03 de 2026-08-17
    "time", "size", "probability", "memory", "injury", "replication",
    "transcription", "maturation", "conformation", "receptor", "adhesion",
    "compensation", "architecture", "sampling", "sectioning", "antibodies",
    "amplitude", "air", "fever", "mortality",
    # equivalentes portugueses
    "tempo", "tamanho", "probabilidade", "memoria", "lesao", "replicacao",
    "transcricao", "maturacao", "conformacao", "adesao", "compensacao",
    "arquitetura", "amostragem", "anticorpos", "ar", "febre", "mortalidade",
    "duracao", "intervalo", "atraso", "quantidade", "resposta", "efeito",
    "alteracao", "mudanca", "aumento", "reducao", "presenca", "ausencia",
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
    if markers >= ENGLISH_MARKER_THRESHOLD:
        failures.append(f"{field}_appears_english")
    return failures


def abstract_answer_failures(text: str) -> list[str]:
    """Reprova o cloze cuja resposta serve a qualquer frase.

    Só alcança respostas de uma palavra: uma expressão médica composta
    ("ausência congênita de luz") não é abstrata pelo mesmo motivo.
    """
    failures: list[str] = []
    for answer in cloze_answers(text):
        if _normalise(answer) in ABSTRACT_ANSWERS:
            failures.append("generic_cloze")
    return failures


def alternative_answer_failures(card: dict[str, Any]) -> list[str]:
    """Reprova a resposta que oferece duas saídas ("x ou y", "x/y").

    Nasce do comentário: "é horrível que haja x ou y, o certo é que haja uma
    palavra só; duas palavras não aumentam o valor pedagógico, só atrapalham,
    porque dificultam a reter."

    Nome composto legítimo (RAG1/RAG2, regra 12/23) continua possível, mas
    precisa ser declarado em `compound_answer_reason` — como já acontece com o
    cloze de três palavras.
    """
    if str(card.get("compound_answer_reason") or "").strip():
        return []
    for answer in cloze_answers(str(card.get("text") or "")):
        if "/" in answer or re.search(r"\bou\b", answer, re.I):
            return ["cloze_answer_offers_alternatives"]
    return []


def anchor_coverage_failures(card: dict[str, Any]) -> list[str]:
    """A resposta precisa existir na âncora da E1.

    Nasce dos comentários "não sei o que é evaginação sacular" e "não compreendi
    esse": quando o termo da resposta não foi ensinado na E1, o card cobra o que
    o aluno não teve como aprender. É a regra 2 de `ERROS.md` tornada mecânica.
    """
    anchor = _normalise(str(card.get("e1_anchor") or ""))
    if not anchor:
        return []
    anchor_words = set(anchor.split())
    for answer in cloze_answers(str(card.get("text") or "")):
        words = [word for word in _normalise(answer).split() if len(word) >= 4]
        if words and not any(word in anchor_words for word in words):
            return ["answer_not_in_e1_anchor"]
    return []


_TARGET_STOPWORDS = {
    "recuperar", "identificar", "lembrar", "reconhecer", "nomear", "indicar",
    "qual", "que", "para", "pelo", "pela", "dos", "das", "com", "sem", "uma",
    "seu", "sua", "este", "esta", "esse", "essa", "onde", "quando", "como",
}


def _content_words(value: str) -> set[str]:
    return {
        word for word in _normalise(value).split()
        if len(word) >= 4 and word not in _TARGET_STOPWORDS
    }


def discriminator_placement_failures(card: dict[str, Any]) -> list[str]:
    """Acusa o card cuja informação discriminante mora só no Extra.

    A frente sozinha precisa sustentar a recuperação declarada. Quando nenhuma
    palavra de conteúdo do `retrieval_target` aparece na frente visível e duas
    ou mais aparecem no Extra, quem ensina é o verso — e o verso só é lido
    depois de responder.
    """
    target = _content_words(str(card.get("retrieval_target") or ""))
    if not target:
        return []
    stem = _content_words(visible_stem(str(card.get("text") or "")))
    extra = _content_words(str(card.get("extra") or ""))
    if target & stem:
        return []
    return ["discriminator_only_in_extra"] if len(target & extra) >= 2 else []


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

# ---------------------------------------------------------------------------
# Dica de tipo no cloze (A14)
# ---------------------------------------------------------------------------
# Feedback registrado do usuário: "dentro do cloze poderia estar escrito
# (processo) para eu saber que o cloze de dilatação era um processo, algo que
# não dava para saber sozinho". Sem a dica, o erro vem de ambiguidade sobre a
# categoria da resposta, não de desconhecer o conteúdo.
#
# A regra alcança apenas respostas de UMA palavra: expressão de duas palavras
# ("fosforilação oxidativa", "citocromo c", "radicais livres") já nomeia a
# própria categoria. Quando a frase realmente entrega o tipo, o card declara
# `type_hint_not_needed_reason`, no mesmo padrão de `three_word_cloze_reason`.

CLOZE_WITH_HINT_RE = re.compile(r"\{\{c(\d+)::([^}:]+)::([^}]*)}}", re.I | re.S)


def cloze_hints(text: str) -> list[str]:
    return [match.group(3).strip() for match in CLOZE_WITH_HINT_RE.finditer(text or "")]


def type_hint_failures(card: dict[str, Any]) -> list[str]:
    text = str(card.get("text") or "")
    answers = cloze_answers(text)
    if not answers:
        return []
    hints = cloze_hints(text)
    failures: list[str] = []

    single_word = [a for a in answers if len(_normalise(a).split()) == 1]
    if single_word and not hints and not str(card.get("type_hint_not_needed_reason") or "").strip():
        failures.append("single_word_cloze_requires_type_hint")

    # A dica delimita a categoria; se ela repete a resposta, entrega o card.
    for hint in hints:
        if not hint:
            failures.append("empty_type_hint")
            continue
        hint_words = {w for w in _normalise(hint).split() if len(w) >= 4}
        for answer in answers:
            answer_words = {w for w in _normalise(answer).split() if len(w) >= 4}
            if _normalise(hint) == _normalise(answer) or (hint_words & answer_words):
                failures.append("type_hint_leaks_answer")
    return failures
