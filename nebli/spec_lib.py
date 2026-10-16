"""Auxiliares comuns do spec de deck-aula no pipeline AnKing-primeiro (F-20261015-CLAUDE-06/07, F-20261016-CLAUDE-01).

Uso no spec.py da corrida (o molde já faz isto):

    from nebli.spec_lib import ak, au, sh, ORG, finalizar
    CARDS = [...]
    finalizar(CARDS, HERE, RUB, BUSCA)   # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca registrada por autoral

- `ak(key, nid, cod, bloco, alvo, slide, motivo)`: nota de acervo (AnKing ou externo); `cod` é o código da rubrica (V-pilar, V-prova,
  A-aula, A-step, R-detalhe, R-org) e vale para todos os clozes (Davi suspende os irmãos que não quiser).
- `au(key, text, cod, bloco, alvo, slide, motivo, extra=...)`: autoral; `cod` pode ser "A-aula/R-detalhe" com `cores={1: "A", 2: "R"}`.
- `finalizar` recusa (SystemExit) card sem código de rubrica; o gate duro confere de novo.
"""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

V, Z, R = 3, 4, 5
COR = {"V": V, "A": Z, "R": R}
NOME = {"V": "verde", "A": "azul", "R": "rosa"}
CODIGOS = ("V-pilar", "V-prova", "A-aula", "A-step", "R-detalhe", "R-org")
ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
CLOZE = re.compile(r"\{\{c(\d+)::(.*?)\}\}", re.S)


def ak(key, src, cod, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags={}, cod=cod, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin:
        d["origin"] = origin
    return d


def au(key, text, cod, bloco, alvo, slide, motivo, extra="", cores=None, espelhos=(1487463871778, 1487470255062, 1487469931164),
       autoria="central", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags={}, cod=cod, cores=cores or {}, bloco=bloco, alvo=alvo,
                evid=f"Slide {slide}", autoria=autoria, busca="", espelhos=list(espelhos), motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


def _call(a, **p):
    return json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps({"action": a, "version": 6, "params": p}).encode())))["result"]


def dicas(t):
    """F-20261016-CLAUDE-01: índice que esconde 3+ itens recebe a primeira letra como dica em cada lacuna."""
    conta = {}
    for n, _ in CLOZE.findall(t):
        conta[n] = conta.get(n, 0) + 1

    def sub(m):
        n, corpo = m.group(1), m.group(2)
        if conta[n] < 3 or "::" in corpo:
            return m.group(0)
        letra = re.sub(r"<[^>]+>", "", corpo).strip()[0]
        return "{{c%s::%s::%s…}}" % (n, corpo, letra)
    return CLOZE.sub(sub, t)


def finalizar(cards, here: Path, busca_base: str):
    """Aplica as regras mecânicas do pipeline a CARDS, no lugar."""
    ids = [c["src"] for c in cards if c["kind"] == "text"]
    clozes = {n["noteId"]: sorted({int(x) for x in re.findall(r"\{\{c(\d+)::", n["fields"].get("Text", {}).get("value", ""))})
              for n in _call("notesInfo", notes=ids)} if ids else {}
    cob = {}
    tsv = here / "busca" / "cobertura.tsv"
    if tsv.exists():
        cob = {l.split("\t")[0]: l.rstrip("\n").split("\t") for l in tsv.read_text(encoding="utf-8").splitlines()[1:]}
    for c in cards:
        if c["kind"] == "compartilhado":
            continue
        cod = c.pop("cod")
        if any(x not in CODIGOS for x in cod.split("/")):
            raise SystemExit(f"{c['key']}: código de rubrica inválido {cod!r} (use {', '.join(CODIGOS)})")
        c["motivo"] = f"{cod}: {c['motivo']}"
        if c["kind"] == "text":
            c["flags"] = {n: COR[cod[0]] for n in clozes.get(c["src"], [1])}
        else:
            cores = c.pop("cores")
            ns = sorted({int(n) for n, _ in CLOZE.findall(c["text"])})
            c["flags"] = {n: COR[cores.get(n, cod[0])] for n in ns}
            c["text"] = dicas(c["text"])
            if c["key"] in cob:
                c["busca"] = busca_base + cob[c["key"]][6] + " Candidatos lidos: " + cob[c["key"]][4] + "."
    return cards
