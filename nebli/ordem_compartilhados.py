"""Associa (tags da aula, cor e posição) e alinha a tag de posição (NEBLI::ordem::<curto>-NN) dos compartilhados de uma corrida ao plan.json, depois de uma delta.

    python3 -m nebli.ordem_compartilhados arquivos-trabalho/<corrida>
"""
import json
import sys
from pathlib import Path

from nebli.decks import Anki, escrita


def main(argv):
    run = Path(argv[0]); plan = json.loads((run / "plan.json").read_text()); A = Anki(); short = plan["short"]
    moves = []
    for nid, s in plan.get("compartilhados", {}).items():
        new = s["ordem_tag"] if s["ordem_tag"].startswith("NEBLI") else "NEBLI::ordem::" + s["ordem_tag"]
        n = A("notesInfo", notes=[int(nid)])[0]
        old = [t for t in n["tags"] if t.startswith(f"NEBLI::ordem::{short}-") and t != new]
        want = [new, f"NEBLI::{plan['lesson_id']}", f"NEBLI::compartilhado::{short}", f"NEBLI::cor::{plan['lesson_id']}::{s['cor']}"]
        if old or any(t not in n["tags"] for t in want):
            moves.append((int(nid), old, " ".join(want)))
    with escrita(A, f"ordem compartilhados {short}", sync=False):
        for nid, old, new in moves:
            if old: A("removeTags", notes=[nid], tags=" ".join(old))
            A("addTags", notes=[nid], tags=new)
    print(len(moves), "compartilhados realinhados")


if __name__ == "__main__":
    main(sys.argv[1:])
