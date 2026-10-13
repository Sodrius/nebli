"""Coleta dos comentários de Davi nos cards (campo NEBLI_Comentario), para aprender o padrão e corrigir (F-20261003-CLAUDE-15).

    python3 -m nebli.comentarios            # lista os comentários novos ou mudados desde a última coleta e grava o registro
    python3 -m nebli.comentarios --todos    # lista todos

Davi: "tô deixando vários comentários pra vc aprender"; "quando for ver os comentários, não apaga eles, vai mantendo".
Nada é apagado no Anki. O registro (flashcards/projeto/comentarios-cards.jsonl) guarda cada versão vista, com data, aula,
origem e o texto do card, para virar regra no MEMORY e gate quando houver padrão.
"""
import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from nebli.decks import Anki

LOG = Path(__file__).resolve().parents[1] / "flashcards/projeto/comentarios-cards.jsonl"


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def main(argv):
    A = Anki()
    seen = {}
    if LOG.exists():
        for l in LOG.read_text().splitlines():
            r = json.loads(l); seen[r["nid"]] = r["comentario"]
    nids = A("findNotes", query="NEBLI_Comentario:_*")
    new = []
    for n in A("notesInfo", notes=nids):
        c = clean(n["fields"]["NEBLI_Comentario"]["value"])
        if "--todos" in argv or seen.get(n["noteId"]) != c:
            f = n["fields"]
            new.append({"nid": n["noteId"], "comentario": c,
                        "aula": next((t.split("::")[1] for t in n["tags"] if t.startswith("NEBLI::2026-")), ""),
                        "origem": next((t.split("::")[-1] for t in n["tags"] if t.startswith("NEBLI::origem::")), ""),
                        "card": clean((f.get("Text") or f.get("Header") or f.get("Front") or {}).get("value", ""))[:200],
                        "visto_em": datetime.now(timezone.utc).isoformat()})
    for r in new:
        print(f"{r['nid']} [{r['aula'][:40]}|{r['origem']}] {r['comentario']}\n    card: {r['card'][:160]}")
    if "--todos" not in argv and new:
        with LOG.open("a") as h:
            for r in new: h.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(new)} comentário(s) {'listados' if '--todos' in argv else 'novos registrados'}")


if __name__ == "__main__":
    main(sys.argv[1:])
