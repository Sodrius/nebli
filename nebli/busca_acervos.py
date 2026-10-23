"""Busca de candidatos nos acervos de referência, em TEXTO LIVRE (todos os campos), por alvo.

Lição de 09/10: restringir a `Text:*termo*` perdia cards dos acervos externos (Histology/MCAT guardam o termo em outros
campos ou com marcação no meio). Cada consulta roda no AnKing e em Referências Externas separadamente; o resultado vai
para o arquivo da corrida (busca/anking.txt) com nid, modelo, HY e frente.

    python3 -m nebli.busca_acervos <saida.txt> "rótulo=termos de busca do Anki" ["rótulo=..." ...] [--max 30]
"""
import html
import json
import re
import sys
import urllib.request

DECKS = {"AnKing": '"deck:Referências::Anking Step Deck*"', "Externos": '"deck:Referências::Referências Externas*"'}


def call(a, **p):
    r = json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps({"action": a, "version": 6, "params": p}).encode())))
    if r["error"]:
        raise RuntimeError(r["error"])
    return r["result"]


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def frente(f):
    for k in ("Text", "Front", "Header", "Remarks", "Title"):
        if k in f and f[k]["value"].strip():
            return clean(f[k]["value"])
    return clean(next(iter(f.values()))["value"])


def main(argv):
    from pathlib import Path
    from nebli.etapa import exigir_planejamento
    exigir_planejamento(Path(argv[0]).resolve().parents[1], "a busca por palavra")  # F-20261023-CLAUDE-02
    mx = int(argv[argv.index("--max") + 1]) if "--max" in argv else 30
    pares = [a for a in argv[1:] if "=" in a and not a.startswith("--")]
    out = []
    for par in pares:
        rot, termos = par.split("=", 1)
        for nome, deck in DECKS.items():
            ns = call("findNotes", query=f"{deck} ({termos})")  # parênteses: OR sem eles escapa do filtro de deck
            out.append(f"### {rot} | {nome} | {termos} | {len(ns)} notas")
            for n in call("notesInfo", notes=ns[:mx]):
                hy = [x.split("::")[-1] for x in n["tags"] if "HighYield" in x]
                sub = next((x.split("::")[1] for x in n["tags"] if x.startswith("#AK_") and "::" in x), "")
                out.append(f"  {n['noteId']} [{n['modelName'][:14]}] {hy[0] if hy else ''} {frente(n['fields'])[:190]}")
    open(argv[0], "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(l for l in out if l.startswith("###")))


if __name__ == "__main__":
    main(sys.argv[1:])
