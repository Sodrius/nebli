"""Confere se cards autorais passariam por AnKing às cegas (medidas objetivas, antes de instalar).

Referência medida em 30/09/2026 numa amostra de 1.500 notas AnKing v12 (First Aid): 1,3% usam ";",
mediana de 15 palavras (90% até 23), 75% com um único cloze, 29% em forma de pergunta. Extra: 25%
vazio; nos demais, mediana de 19 palavras (p90 51), em bullets "- " curtos com termo em negrito, sem
parágrafo explicativo nem comentário de curadoria (o porquê fica na explicação do Tab). O padrão
AnKing cobra UM nome (o cloze) dentro de uma frase que ensina o processo inteiro, curta.

Uso:
    python3 -m nebli.lint_cards arquivos-trabalho/<corrida>/plan.json   # entries do plano (antes de instalar)
    python3 -m nebli.lint_cards --anki '"tag:NEBLI::<aula>" "tag:NEBLI::origem::Autoral"'  # notas vivas
No plan.json, cada autoral precisa de "autoria": "central" | "prova" e de "busca" preenchida;
autoria acima de 20% dos cards gera aviso. Sai com código 1 se algum card autoral falhar em regra dura. Métrica não substitui leitura:
passar aqui é o mínimo, não prova qualidade.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

MAX_WORDS = 23          # p90 AnKing
MAX_CLOZES = 3          # acima disso vira lista; AnKing: 75% com 1
MAX_EXTRA = 34          # Extra AnKing: 25% vazio, mediana 19, p75 34
MAX_EXTRA_HARD = 51     # p90
# "no" e "do" ficam de fora: também são palavras inglesas ("no C5a", "do not").
PT = re.compile(r"\b(que|não|são|está|pelo|pela|uma|um|dos|das|com|para|da|de|na|em|é|e|o|os|ao|tem|células?)\b", re.I)
EN = re.compile(r"\b(the|of|and|is|which|with|to|in|by|a|an)\b", re.I)
CLOZE = re.compile(r"\{\{c(\d+)::(.*?)(?:::.*?)?\}\}", re.S)


def plain(value):
    value = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def portuguese(text):
    return len(text.split()) > 4 and len(PT.findall(text)) > len(EN.findall(text))


def check(key, text_html, extra_html=""):
    """Lista de (gravidade, problema). 'dura' reprova; 'aviso' pede olhar."""
    text = plain(CLOZE.sub(lambda m: m.group(2), text_html))
    problems = []
    if ";" in text:
        problems.append(("dura", "';' junta duas afirmações: dividir em cards ou reescrever numa frase só"))
    words = len(text.split())
    if words > MAX_WORDS:
        problems.append(("dura" if words > 30 else "aviso", f"{words} palavras (AnKing: mediana 15, p90 {MAX_WORDS})"))
    clozes = {m.group(1) for m in CLOZE.finditer(text_html)}
    if len(clozes) > MAX_CLOZES:
        problems.append(("aviso", f"{len(clozes)} clozes: vira lista; preferir um nome por card"))
    if portuguese(text):
        problems.append(("dura", "frente em português (novos cards em inglês)"))
    extra = plain(re.sub(r"<img[^>]*>", " ", extra_html or ""))
    extra_words = len(extra.split())
    if portuguese(extra):
        problems.append(("dura", "Extra em português"))
    if extra_words > MAX_EXTRA_HARD:
        problems.append(("dura", f"Extra com {extra_words} palavras (AnKing: mediana 19, p90 {MAX_EXTRA_HARD})"))
    elif extra_words > MAX_EXTRA:
        problems.append(("aviso", f"Extra com {extra_words} palavras (AnKing p75 {MAX_EXTRA})"))
    if extra_words > 15 and not re.search(r"(^|<br\s*/?>|<div>)\s*-\s", extra_html or ""):
        problems.append(("aviso", "Extra em parágrafo: AnKing usa bullets '- ' curtos com termo em negrito"))
    if re.search(r"\b(the lecture|in the lecture|this card|these patterns|this is)\b", extra, re.I):
        problems.append(("dura", "Extra com metacomentário de curadoria"))
    if re.search(r"\b(whereas|while|but)\b.*\{\{c\d+::", text_html) and len(clozes) >= 2:
        problems.append(("aviso", "contraste com 2+ clozes: conferir se não são dois cards"))
    return problems


def justification(entry):
    """Autoral só para alvo central da aula ou cobrado em prova, sem AnKing/associado equivalente
    (F-20260930-CLAUDE-19: autoria excessiva em detalhes na Imuno P2)."""
    problems = []
    if entry.get("autoria") not in ("central", "prova", "lateral"):
        problems.append(("dura", "autoral sem 'autoria': 'central', 'prova' ou 'lateral' (este vai com bandeira rosa)"))
    if not str(entry.get("busca", "")).strip():
        problems.append(("dura", "autoral sem 'busca': rotas AnKing/alternativos consultadas e por que não servem"))
    return problems


def from_plan(path):
    plan = json.loads(Path(path).read_text(encoding="utf-8"))
    entries = plan["entries"]
    autorais = [e for e in entries if e.get("origin") == "Autoral"]
    cards = lambda es: sum(len(e.get("cards", [])) or 1 for e in es)
    if entries and cards(autorais) > 0.2 * cards(entries):
        print(f"[aviso] {cards(autorais)} de {cards(entries)} cards são autorais (>20%): refazer a busca antes de aceitar")
    for entry in autorais:
        fields = entry["fields"]
        yield entry["key"], fields.get("Text", ""), fields.get("Extra", ""), justification(entry)


def from_anki(query):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from nebli.decks import Anki
    call = Anki()
    ids = call("findNotes", query=query)
    for start in range(0, len(ids), 200):
        for note in call("notesInfo", notes=ids[start:start + 200]):
            fields = note["fields"]
            yield (str(note["noteId"]), fields.get("Text", {}).get("value", ""),
                   fields.get("Extra", {}).get("value", ""), [])


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("plano", nargs="?")
    parser.add_argument("--anki")
    args = parser.parse_args()
    if not args.plano and not args.anki:
        parser.error("informe plan.json ou --anki '<busca>'")
    cards = from_plan(args.plano) if args.plano else from_anki(args.anki)
    total = hard = 0
    for key, text, extra, extra_problems in cards:
        total += 1
        problems = check(key, text, extra) + extra_problems
        if problems:
            hard += any(level == "dura" for level, _ in problems)
            print(f"{key}: " + " | ".join(f"[{level}] {msg}" for level, msg in problems))
            print(f"    {plain(text)[:160]}")
    print(f"{total} autorais conferidos; {hard} reprovados em regra dura.")
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
