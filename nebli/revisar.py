"""Despeja os cards vivos de uma aula para a revisão final card a card (F-20261003-CLAUDE-15).

    python3 -m nebli.revisar arquivos-trabalho/<corrida> [--de N] [--ate M]

Uma linha por nota, na ordem da aula: chave, origem, cores por card, texto visível com [clozes], verso resumido,
figuras (arquivo) e comentário de Davi. Compartilhados vêm no fim.
"""
import html
import json
import re
import sys
from pathlib import Path

from nebli.decks import Anki

COR = {0: "-", 1: "R", 3: "V", 4: "A", 5: "P"}


def clean(s):
    s = re.sub(r"<img[^>]*src=\"([^\"]+)\"[^>]*>", r" [IMG \1] ", s or "")
    s = re.sub(r"<br\s*/?>|</div>|</li>", " / ", s)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def main(argv):
    run = Path(argv[0]); A = Anki()
    a = dict(zip(argv[1::2], argv[2::2]))
    plan = json.loads((run / "plan.json").read_text()); rec = json.loads((run / "receipt.json").read_text())
    nid = {n["key"]: n["nid"] for n in rec["notes"]}
    keys = [e["key"] for e in plan["entries"]][int(a.get("--de", 0)):int(a.get("--ate", 9999))]
    info = {n["noteId"]: n for n in A("notesInfo", notes=[nid[k] for k in keys])}
    for i, e in enumerate(plan["entries"]):
        if e["key"] not in keys: continue
        n = info[nid[e["key"]]]; f = {k: v["value"] for k, v in n["fields"].items()}
        cards = sorted(A("cardsInfo", cards=n["cards"]), key=lambda c: c["ord"])
        cores = "".join(COR.get(c["flags"], "?") + ("s" if c["queue"] == -1 else "") for c in cards)
        front = clean(f.get("Text") or f.get("Header") or f.get("Front") or "")
        front = re.sub(r"\{\{c(\d+)::(.*?)(::.*?)?\}\}", r"[\2]", front)
        if e.get("kind") == "slideio":
            front = "IO: " + clean(f.get("Remarks", ""))[:120]
        back = clean(f.get("Extra", "") or f.get("Back Extra", ""))
        imgsx = re.findall(r"\[IMG ([^\]]+)\]", back); back = re.sub(r"\[IMG [^\]]+\]", "", back).strip()
        com = clean(f.get("NEBLI_Comentario", ""))
        print(f"{i:03d} {e['key']} | {e['origin'][:6]} | {cores} | {e.get('evid','')[:8]}\n    F: {front[:300]}\n    V: {back[:180]}"
              + (f"\n    IMG: {', '.join(x[:24] for x in imgsx[:3])}" if imgsx else "\n    IMG: —") + (f"\n    COMENTÁRIO: {com}" if com else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
