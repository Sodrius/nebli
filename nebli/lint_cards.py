"""Confere se cards autorais passariam por AnKing às cegas (medidas objetivas, antes de instalar).

Referência medida em 30/09/2026 numa amostra de 1.500 notas AnKing v12 (First Aid): 1,3% usam ";",
mediana de 15 palavras (90% até 23), 75% com um único cloze, 29% em forma de pergunta. Extra: 25%
vazio; nos demais, mediana de 19 palavras (p90 51), em bullets "- " curtos com termo em negrito, sem
parágrafo explicativo nem comentário de curadoria (o porquê fica na explicação do Tab). O padrão
AnKing cobra UM nome (o cloze) dentro de uma frase que ensina o processo inteiro, curta.

Uso:
    python3 -m nebli.lint_cards arquivos-trabalho/<corrida>/plan.json   # entries do plano (antes de instalar)
    python3 -m nebli.lint_cards --anki '"tag:NEBLI::<aula>" "tag:NEBLI::origem::Autoral"'  # notas vivas
No plan.json, cada autoral precisa de "autoria": "central" | "prova" | "lateral", de "busca" preenchida e de
"espelhos": [nid, nid, ...] (2–3 cards AnKing vizinhos usados como molde; ver nebli/espelhos.py);
autoria acima de 15% dos cards gera aviso de auditoria, não cota. Sai com código 1 se algum card autoral falhar em regra dura. Métrica não substitui leitura:
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
MAX_SENT_WORDS = 20     # F-20261016-CLAUDE-03: autoral em frase, um pouco menor que o p90
MAX_ORG_WORDS = 26      # organizador/quadro em tópicos
MAX_CLOZES = 3          # acima disso vira lista; AnKing: 75% com 1
MAX_EXTRA = 34          # Extra AnKing: 25% vazio, mediana 19, p75 34
MAX_EXTRA_HARD = 51     # p90
# "no" e "do" ficam de fora: também são palavras inglesas ("no C5a", "do not").
PT = re.compile(r"\b(que|não|são|está|pelo|pela|uma|um|dos|das|com|para|da|de|na|em|é|e|o|os|ao|tem|células?)\b", re.I)
EN = re.compile(r"\b(the|of|and|is|which|with|to|in|by|a|an)\b", re.I)
CLOZE = re.compile(r"\{\{c(\d+)::(.*?)(?:::.*?)?\}\}", re.S)
VAZIAS = {"this", "that", "with", "from", "into", "they", "their", "them", "have", "only", "also", "when", "which", "where", "while", "more", "most", "than", "each", "both"}
GENERICOS = {"encode", "encodes", "toxic", "dna", "rna", "protein", "proteins", "virus", "viruses", "cell", "cells", "host", "enzyme",
             "enzymes", "step", "steps", "their own", "own", "process", "function", "structure", "change", "molecule"}


def plain(value):
    value = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


CHEM = re.compile(r"\b(?:Na|K|Ca|Cl|H|Fe|Mg|O|e\.g\.|i\.e\.)(?=\W|$)")


def portuguese(text):
    text = CHEM.sub(" ", text)  # "Na", "O", "e.g." não são português
    return len(text.split()) > 4 and len(PT.findall(text)) > len(EN.findall(text))


def check(key, text_html, extra_html=""):
    """Lista de (gravidade, problema). 'dura' reprova; 'aviso' pede olhar."""
    text = plain(CLOZE.sub(lambda m: m.group(2), text_html))
    problems = []
    organizacao = 'data-nebli-organizacao="true"' in text_html
    pista_cid = organizacao and 'data-nebli-pista="CID"' in text_html
    if ";" in text:
        problems.append(("dura", "';' junta duas afirmações: dividir em cards ou reescrever numa frase só"))
    if re.search(r"(?<!\d):(?!\d)", text) and not organizacao:
        problems.append(("dura", "':' na frente: AnKing escreve frase corrida, sem rótulo nem dois pontos (F-20261001-CLAUDE-16)"))
    words = len(text.split())
    # F-20261016-CLAUDE-03: “os cards ficaram um pouco grandes… autorais, na maior parte dos casos, num tamanho um pouco menor, com uma indução de qualidade”
    limite = MAX_ORG_WORDS if organizacao else MAX_SENT_WORDS
    if words > limite:
        problems.append(("dura", f"{words} palavras ({'organizador' if organizacao else 'frase'}: máximo {limite}; AnKing: mediana 15)"))
    elif not organizacao and words > 16:
        problems.append(("aviso", f"{words} palavras (AnKing: mediana 15): dá para encurtar mantendo a indução?"))
    clozes = {m.group(1) for m in CLOZE.finditer(text_html)}
    if len(clozes) > MAX_CLOZES:
        problems.append(("aviso", f"{len(clozes)} clozes: vira lista; preferir um nome por card"))
    if portuguese(text) and not pista_cid:
        problems.append(("dura", "frente em português (novos cards em inglês)"))
    if text and not re.search(r"<(?:b|strong)\b", text_html or "") and not re.search(r"\{\{c\d+::\s*<(?:b|strong)\b", text_html or ""):
        problems.append(("dura", "sem negrito: AnKing negrita 1–3 termos de contexto (95% das notas, mediana 2; F-20261011-CLAUDE-01)"))
    if re.search(r"\b(?:the (?:lesson|lecture)|slide \d+)\b", text, re.I):
        problems.append(("dura", "frente com metacomentário de aula/slide: o card não cita a aula"))
    if re.search(r"\b(?:according to (?:the )?source|the source (?:contrasts|states|says)|given in the source)\b", text, re.I):
        problems.append(("dura", "frente com metacomentário de fonte: resolver a incerteza fora do card"))
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
    if re.search(r"\b(the lecture|in the lecture|in the lesson|the lesson|the transcript|transcript cites|in the figure|exercise question|slide \d+|this card|these patterns)\b", extra, re.I):
        problems.append(("dura", "Extra com metacomentário de curadoria"))
    # F-20261022-CLAUDE-08 (58: “autorais de baixa qualidade”): o cloze esconde o termo específico que se decora, nunca uma palavra
    # genérica que qualquer frase aceitaria (encode, toxic, DNA, protein…).
    genericos = [a for a in (plain(m.group(2)).lower().strip(" .") for m in CLOZE.finditer(text_html)) if a in GENERICOS]
    if genericos:
        problems.append(("dura", f"cloze em palavra genérica ({', '.join(genericos)}): esconder o termo específico que se decora"))
    # F-20261022-CLAUDE-08: verso autoral tem de ensinar algo além da frente, não repeti-la
    palavras = lambda t: {w for w in re.findall(r"[a-z][a-z'-]{3,}", t.lower()) if w not in VAZIAS}
    ext, fre = palavras(extra), palavras(text)
    if len(ext) >= 3 and len(ext & fre) / len(ext) >= 0.7:
        problems.append(("dura", "Extra repete a frente: o verso tem de trazer o porquê, a consequência ou o contraste"))
    if re.search(r"\b(whereas|while|but)\b.*\{\{c\d+::", text_html) and len(clozes) >= 2:
        problems.append(("aviso", "contraste com 2+ clozes: conferir se não são dois cards"))
        # F-20261015-CLAUDE-05 (onicomicose: “já pontuei 300 cards nesse estilo, que são ruins”): par complementar em
        # índices diferentes deixa um lado entregar o outro; o mesmo índice (c1/c1, dica x/y se ambíguo) é o padrão.
        if len(set(re.findall(r"\{\{c(\d+)::", text_html))) == 2 and re.search(r"\b(whereas|while|unlike)\b", plain(text_html), re.I):
            problems.append(("aviso", "CONTRASTE EM DOIS ÍNDICES: se o par é complementar (saber um lado dá o outro), usar o mesmo índice (c1/c1)"))
    return problems


# F-20261023-CLAUDE-01 (comentários de 23/10): regras que valem a partir do PIPELINE_VERSAO 7.
SIMBOLO = re.compile(r"(?<![\w-])(?!(?:A|I)\b)([A-Z])(?![\w+.'’-])(?!\s*(?:cells?|lymphocytes?|antigens?|phase|ring|wave|waves|=))")
SIMBOLO_OK = re.compile(r"(?:vitamin|type|hepatitis|influenza|group|complex|phase|latency|class|factor|chain|zone|protein|band|line|segment|HLA|lane)\s*$", re.I)


def check_v7(text_html):
    """'dura': (1) negrito de contexto FORA do cloze (Davi: “NEGRITO … gate-hard, checado card a card”); (2) frase com 3+ lacunas ou
    lista numerada em linha vira tópicos em pé (“AJUSTA PARA SER EM TÓPICOS”; “3 clozes, um só card e tópicos”); (3) símbolo de uma
    letra sem definição no próprio card (“um card tem que fazer sentido sozinho / isso do E não faz sentido sozinho”)."""
    probs = []
    organizacao = 'data-nebli-organizacao="true"' in text_html
    fora = CLOZE.sub(" ", text_html)
    if not re.search(r"<(?:b|strong)\b", fora):
        probs.append(("dura", "sem negrito de contexto fora do cloze: negritar 1–2 termos que situam o card (AnKing)"))
    if not organizacao and (len(CLOZE.findall(text_html)) >= 3 or re.search(r"(?:^|\s)[1-3]\.\s", plain(text_html))):
        probs.append(("dura", "enumeração de 3+ itens em frase: escrever como organizador em tópicos, um item por linha"))
    txt = plain(CLOZE.sub(lambda m: m.group(2), text_html))
    for m in SIMBOLO.finditer(txt):
        antes = txt[:m.start()]
        definido = re.search(rf"\({m.group(1)}\)|{m.group(1)}\s*=|\({m.group(1)},", txt)
        if not SIMBOLO_OK.search(antes) and not definido:
            probs.append(("dura", f"símbolo '{m.group(1)}' sem definição: o card tem de fazer sentido sozinho (escrever o nome)"))
            break
    return probs


def justification(entry):
    """Autoral só para alvo central da aula ou cobrado em prova, sem AnKing/associado equivalente
    (F-20260930-CLAUDE-19: autoria excessiva em detalhes na Imuno P2)."""
    problems = []
    if entry.get("autoria") not in ("central", "prova", "lateral"):
        problems.append(("dura", "autoral sem 'autoria': 'central', 'prova' ou 'lateral' (este vai com bandeira rosa)"))
    if not str(entry.get("busca", "")).strip():
        problems.append(("dura", "autoral sem 'busca': rotas AnKing/alternativos consultadas e por que não servem"))
    mirrors = entry.get("espelhos")
    if not isinstance(mirrors, list) or len(mirrors) < 2:
        problems.append(("dura", "autoral sem 'espelhos': 2–3 nids de cards AnKing vizinhos que serviram de molde "
                                 "(python3 -m nebli.espelhos <termos>)"))
    return problems


def from_plan(path):
    plan = json.loads(Path(path).read_text(encoding="utf-8"))
    entries = plan["entries"]
    autorais = [e for e in entries if e.get("origin") == "Autoral"]
    cards = lambda es: sum(len(e.get("cards", [])) or 1 for e in es)
    if entries and cards(autorais) > 0.15 * cards(entries):
        print(f"[aviso] {cards(autorais)} de {cards(entries)} cards são autorais (>15%): auditar busca e espelhos; preservar a completude")
    evidence = plan.get("busca_externos")
    if autorais and not (evidence and (Path(path).parent / evidence).exists()):
        yield ("plano", "", "", [("dura", "há autorais e o plano não aponta 'busca_externos': arquivo da corrida com a busca feita em "
                                         "Referências Externas (MCAT, AnatoKing, Dope etc.) antes de autorar")])
    v7 = int(plan.get("pipeline_versao") or 1) >= 7
    for entry in autorais:
        fields = entry["fields"]
        yield entry["key"], fields.get("Text", ""), fields.get("Extra", ""), justification(entry) + (check_v7(fields.get("Text", "")) if v7 else [])


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
        problems = (check(key, text, extra) if text else []) + extra_problems
        if problems:
            hard += any(level == "dura" for level, _ in problems)
            print(f"{key}: " + " | ".join(f"[{level}] {msg}" for level, msg in problems))
            print(f"    {plain(text)[:160]}")
    print(f"{total} autorais conferidos; {hard} reprovados em regra dura.")
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
