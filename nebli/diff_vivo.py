"""Diferença entre o plan.json de uma corrida e as notas vivas (campos), antes de aplicar uma delta.

    python3 -m nebli.diff_vivo arquivos-trabalho/<corrida>
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

from nebli.decks import Anki


def same(a, b):
    """Igualdade de campo ignorando a normalização de HTML que o Anki faz ao gravar (/>, </div>, espaços)."""
    n = lambda x: re.sub(r"\s+|</[a-z0-9]+>|<div>|<br\s*/?>", "", re.sub(r"\s*/>", ">", x or ""))
    return n(a) == n(b)


def main(run):
    run = Path(run); A = Anki()
    plan = json.loads((run / "plan.json").read_text()); rec = json.loads((run / "receipt.json").read_text())
    nid = {n["key"]: n["nid"] for n in rec["notes"]}
    live = {n["noteId"]: n for n in A("notesInfo", notes=list(nid.values())) if n}
    c, ex = Counter(), {}
    for e in plan["entries"]:
        n = live.get(nid.get(e["key"]))
        if not n: c["nova"] += 1; continue
        for f, v in e["fields"].items():
            if f != "NEBLI_Comentario" and f in n["fields"] and not same(n["fields"][f]["value"], v):
                c[f] += 1; ex.setdefault(f, e["key"])
    print(run.name, dict(c), ex)


if __name__ == "__main__":
    main(sys.argv[1])
