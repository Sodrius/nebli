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
from nebli.acervos import catalogar, salvar_catalogo, registrar, file_hash

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
    if mx <= 0:
        raise ValueError("--max precisa ser positivo")
    run = Path(argv[0]).resolve().parents[1]
    catalog = catalogar(call)
    salvar_catalogo(run, catalog)
    out, records = [], []
    for par in pares:
        rot, termos = par.split("=", 1)
        coverage = []
        out.append(f"### {rot} | Externos | {termos} | consulta individual em cada acervo abaixo")
        for corpus in catalog['corpora']:
            nome, deck = corpus['nome'], corpus['consulta']
            query = f"{deck} ({termos})"
            ns = sorted(set(call("findNotes", query=query)))
            coverage.append({'acervo': nome, 'consulta': query, 'total_acervo': corpus['total'],
                             'status': 'consultado' if ns else 'sem_resultados',
                             'encontrados': len(ns), 'exibidos': min(mx, len(ns)),
                             'truncado': len(ns) > mx, 'ids': ns})
            out.append(f"### {rot} | {nome} | {termos} | {len(ns)} notas; exibidas {min(mx, len(ns))}")
            for n in call("notesInfo", notes=ns[:mx]) if ns else []:
                hy = [x.split("::")[-1] for x in n["tags"] if "HighYield" in x]
                out.append(f"  {n['noteId']} [{n['modelName'][:14]}] {hy[0] if hy else ''} {frente(n['fields'])[:190]}")
        records.append({'chave': rot, 'consulta': termos, 'catalogo_sha256': catalog['sha256'],
                        'cobertura_acervos': coverage})
    target = Path(argv[0]).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(out) + "\n", encoding="utf-8")
    for record in records:
        registrar(run, 'palavra-chave', dict(record, arquivo=str(target.relative_to(run)), arquivo_sha256=file_hash(target)))
    print("\n".join(l for l in out if l.startswith("###")))


if __name__ == "__main__":
    main(sys.argv[1:])
