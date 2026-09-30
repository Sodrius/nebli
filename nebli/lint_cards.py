"""Confere se cards autorais passariam por AnKing às cegas (medidas objetivas, antes de instalar).

Referência medida em 30/09/2026 numa amostra de 1.500 notas AnKing v12 (First Aid): 1,3% usam ";",
mediana de 15 palavras (90% até 23), 75% com um único cloze, 29% em forma de pergunta. O padrão
AnKing cobra UM nome (o cloze) dentro de uma frase que ensina o processo inteiro, curta.

Uso:
    python3 -m nebli.lint_cards arquivos-trabalho/<corrida>/plan.json   # entries do plano (antes de instalar)
    python3 -m nebli.lint_cards --anki '"tag:NEBLI::<aula>" "tag:NEBLI::origem::Autoral"'  # notas vivas
Sai com código 1 se algum card autoral falhar em regra dura. Métrica não substitui leitura:
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
PT = re.compile(r"\b(que|não|são|está|pelo|pela|uma|dos|das|com|para|da|do|na|no|em|é|ao|células?)\b", re.I)
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
    if portuguese(plain(extra_html)):
        problems.append(("aviso", "Extra em português"))
    if re.search(r"\b(whereas|while|but)\b.*\{\{c\d+::", text_html) and len(clozes) >= 2:
        problems.append(("aviso", "contraste com 2+ clozes: conferir se não são dois cards"))
    return problems


def from_plan(path):
    plan = json.loads(Path(path).read_text(encoding="utf-8"))
    for entry in plan["entries"]:
        if entry.get("origin") == "Autoral":
            fields = entry["fields"]
            yield entry["key"], fields.get("Text", ""), fields.get("Extra", "")


def from_anki(query):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from nebli.decks import Anki
    call = Anki()
    ids = call("findNotes", query=query)
    for start in range(0, len(ids), 200):
        for note in call("notesInfo", notes=ids[start:start + 200]):
            fields = note["fields"]
            yield str(note["noteId"]), fields.get("Text", {}).get("value", ""), fields.get("Extra", {}).get("value", "")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("plano", nargs="?")
    parser.add_argument("--anki")
    args = parser.parse_args()
    if not args.plano and not args.anki:
        parser.error("informe plan.json ou --anki '<busca>'")
    cards = from_plan(args.plano) if args.plano else from_anki(args.anki)
    total = hard = 0
    for key, text, extra in cards:
        total += 1
        problems = check(key, text, extra)
        if problems:
            hard += any(level == "dura" for level, _ in problems)
            print(f"{key}: " + " | ".join(f"[{level}] {msg}" for level, msg in problems))
            print(f"    {plain(text)[:160]}")
    print(f"{total} autorais conferidos; {hard} reprovados em regra dura.")
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
