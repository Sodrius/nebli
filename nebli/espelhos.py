"""Espelhos de um autoral: 2–3 cards AnKing reais, vizinhos do alvo, que o autoral imita como irmão.

Em vez de seguir uma receita geral de estilo, cada autoral nasce ao lado de cards AnKing do mesmo
assunto/função: mesma construção, mesmo tipo de alvo oculto, mesmo hábito de negrito e de Extra.
Os espelhos são, em geral, os candidatos lidos e recusados na busca (cobrem o vizinho, não o alvo).

    python3 -m nebli.espelhos "aldose reductase" sorbitol cataract [--n 3] [--excluir nid ...]

Termos em inglês, do mais ao menos específico. No plan.json, o autoral registra
"espelhos": [nid, nid, ...]; o lint reprova autoral sem pelo menos dois.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys

DECK = '"deck:Referências::Anking Step Deck*"'
MIN = 2


def rank(hits, n=3):
    """hits: [(peso do termo, [nids])]. Mais termos casados primeiro; depois os mais específicos."""
    score, count = collections.Counter(), collections.Counter()
    for weight, nids in hits:
        for nid in set(nids):
            score[nid] += weight
            count[nid] += 1
    return sorted(score, key=lambda nid: (-count[nid], -score[nid], nid))[:n]


def search(call, terms, exclude=(), n=3, deck=DECK):
    exclude = {int(x) for x in exclude}
    hits = []
    for index, term in enumerate(terms):
        clean = re.sub(r'["\\]', " ", term).strip()
        if clean:
            found = call("findNotes", query=f'{deck} "{clean}"')
            # termo raro pesa mais: é o que aproxima o espelho do alvo
            hits.append(((len(terms) - index) / (1 + len(found)) ** 0.5, [x for x in found if x not in exclude]))
    top = rank(hits, n)
    info = {x["noteId"]: x for x in call("notesInfo", notes=top)} if top else {}
    return [{"nid": nid, "text": info[nid]["fields"]["Text"]["value"],
             "extra": info[nid]["fields"].get("Extra", {}).get("value", "")} for nid in top if nid in info]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("termos", nargs="+")
    parser.add_argument("--n", type=int, default=3)
    parser.add_argument("--excluir", nargs="*", default=[])
    args = parser.parse_args(argv)
    from nebli.decks import Anki
    found = search(Anki(), args.termos, args.excluir, args.n)
    json.dump(found, sys.stdout, ensure_ascii=False, indent=1)
    print()
    return 0 if len(found) >= MIN else 1


if __name__ == "__main__":
    sys.exit(main())
