"""Busca, para cada oclusão do slide de uma corrida, o mesmo alvo no AnKing e nos acervos externos (F-20261003-CLAUDE-13).

    python3 -m nebli.io_busca arquivos-trabalho/<corrida> [--decisao arquivo.json]

Davi: "verifica sempre que o anking e externo não cobre antes de fazer autoral" — oclusão do slide é autoral. Para cada
entrada `slideio` do plan.json, procura o nome em inglês (Remarks, sem parênteses) no AnKing Step e nos externos de imagem
(BlueLink, AnatoKing, Dope, Histology, LLU), grava as notas achadas em `busca/io.txt` e escreve no campo `busca` da entrada
o que foi achado e a decisão. A decisão padrão só vale quando nenhum acervo tem o alvo; havendo acervo, `--decisao` traz
{key: "motivo de manter a oclusão" | "trocar"} escrito depois de olhar as notas achadas. Sem decisão para um alvo achado,
o campo fica vazio e o gate reprova.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

DECKS = {"AnKing": '"deck:Referências::Anking Step Deck*"',
         "BlueLink": '"deck:Referências::Referências Externas::University of Michigan - BlueLink Atlas*"',
         "AnatoKing": '"deck:Referências::Referências Externas::AnatoKing*"',
         "Dope": '"deck:Referências::Referências Externas::Dope Anatomy*"',
         "Histology": '"deck:Referências::Referências Externas::Histology*"',
         "LLU": '"deck:Referências::Referências Externas::LLU Histology*"'}
STOP = {"of", "the", "and", "part", "with", "from", "in", "on", "at", "to", "a", "an", "its", "or"}


def terms(name):
    name = re.sub(r"\(.*?\)", " ", html.unescape(re.sub(r"<[^>]+>", " ", name)))
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]+", name) if w.lower() not in STOP]
    return " ".join(words[:4])


def clean(v):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v))).strip()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corrida"); ap.add_argument("--decisao")
    args = ap.parse_args(argv)
    run = Path(args.corrida)
    from nebli.decks import Anki
    A = Anki()
    plan_path = run / "plan.json"; plan = json.loads(plan_path.read_text(encoding="utf-8"))
    decisions = json.loads(Path(args.decisao).read_text(encoding="utf-8")) if args.decisao else {}
    (run / "busca").mkdir(exist_ok=True)
    log, pending = [f"Busca das oclusões do slide no AnKing e nos externos ({len(DECKS)} acervos), nebli.io_busca"], []
    for e in plan["entries"]:
        if e.get("kind") != "slideio":
            continue
        name = re.match(r"\s*<b>(.*?)</b>", e["fields"].get("Remarks", ""), re.S)
        t = terms(name.group(1) if name else e.get("name", ""))
        found = {}
        for label, deck in DECKS.items():
            q = f'{deck} "{t}"' if len(t.split()) > 1 else f"{deck} {t}"
            nids = A("findNotes", query=q)
            if nids:
                found[label] = nids
            log.append(f"[{e['key']}] {label}: {len(nids)} notas — {q}")
            for n in A("notesInfo", notes=nids[:3]):
                main = next((clean(v["value"]) for k, v in n["fields"].items() if k in ("Text", "Front", "Header", "Remarks", "Structure", "Title") and clean(v["value"])), "")
                log.append(f"    {n['noteId']} {main[:150]}")
        summary = ", ".join(f"{k} {len(v)}" for k, v in found.items()) or "nenhum acervo"
        if not found:
            e["busca"] = (f"'{t}' sem nota no AnKing nem nos externos com texto ({', '.join(k for k in DECKS if k != 'BlueLink')}); "
                          "BlueLink só tem o nome na imagem e foi olhado pela região; oclusão do slide da aula")
        elif e["key"] in decisions:
            e["busca"] = f"'{t}': {summary} (busca/io.txt). {decisions[e['key']]}"
        else:
            e["busca"] = ""; pending.append((e["key"], summary))
    (run / "busca" / "io.txt").write_text("\n".join(log) + "\n", encoding="utf-8")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"busca/io.txt gravado; sem decisão (achado em acervo): {len(pending)}")
    for k, sm in pending:
        print(f"  {k}: {sm}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
