"""Alinha bandeiras e tags de cor do deck instalado ao plan.json da corrida (depois de mudar cores na spec e rodar build.py).

    python3 -m nebli.recolor arquivos-trabalho/<corrida> [--aplicar]

Sem --aplicar só lista as diferenças. Mexe apenas nas notas próprias da aula (não nas compartilhadas): troca a tag
`NEBLI::cor::<lesson>::*` pelas do plano e ajusta a bandeira de cada card, sem baixar bandeira de card que também
pertence a outra aula com cor maior. Escrita pelo protocolo `nebli.decks.escrita` (sync=False) com leitura posterior.
"""
import json
import sys
from pathlib import Path

from nebli.decks import Anki, em_tela, escrita

RANK = {3: 3, 4: 2, 5: 1, 0: 0}
FLAG = {"verde": 3, "azul": 4, "rosa": 5}


def note_for(entry, info):
    src = [t for t in entry["tags"] if t.startswith("NEBLI::source::nid-")]
    if src:
        found = [n for n, i in info.items() if src[0] in i["tags"]]
    else:
        found = [n for n, i in info.items() if i["fields"].get("Text", {}).get("value") == entry["fields"].get("Text")]
    return found[0] if len(found) == 1 else None


def other_flag(tags, lesson):
    best = 0
    for t in tags:
        if t.startswith("NEBLI::cor::") and not t.startswith(f"NEBLI::cor::{lesson}::"):
            best = max(best, RANK[FLAG.get(t.split("::")[-1], 0)])
    return best


def main(argv):
    run = Path(argv[0]); apply_ = "--aplicar" in argv
    plan = json.loads((run / "plan.json").read_text())
    lesson = plan["lesson_id"]
    A = Anki()
    nids = A("findNotes", query=f'"tag:NEBLI::{lesson}"')
    info = {n["noteId"]: n for n in A("notesInfo", notes=nids)}
    todo = []
    for e in plan["entries"]:
        nid = note_for(e, info)
        if nid is None:
            print("sem nota viva:", e["key"]); continue
        want_tags = sorted(t for t in e["tags"] if t.startswith(f"NEBLI::cor::{lesson}::"))
        have_tags = sorted(t for t in info[nid]["tags"] if t.startswith(f"NEBLI::cor::{lesson}::"))
        cards = {c["ord"]: c for c in A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))}
        floor = other_flag(info[nid]["tags"], lesson)
        flags = []
        for c in e["cards"]:
            live = cards.get(c["ord"])
            if not live:
                continue
            want = c["flag"] if RANK[c["flag"]] >= floor else live["flags"]
            if live["flags"] != want:
                flags.append((live["cardId"], live["flags"], want))
        if want_tags != have_tags or flags:
            todo.append((e["key"], nid, have_tags, want_tags, flags))
    for nid_s, c in plan.get("compartilhados", {}).items():
        nid = int(nid_s)
        tags = A("notesInfo", notes=[nid])[0]["tags"]
        have = sorted(t for t in tags if t.startswith(f"NEBLI::cor::{lesson}::"))
        want = [f"NEBLI::cor::{lesson}::{c['cor']}"]
        after = [t for t in tags if not t.startswith(f"NEBLI::cor::{lesson}::")] + want
        top = max(RANK[FLAG[t.split("::")[-1]]] for t in after if t.startswith("NEBLI::cor::") and t.split("::")[-1] in FLAG)
        target = next(f for f, r in RANK.items() if r == top and f)
        flags = [(x["cardId"], x["flags"], target) for x in A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))
                 if x["flags"] in (0, 3, 4, 5) and x["flags"] != target]
        if have != want or flags:
            todo.append((f"sh-{nid}", nid, have, want, flags))
    for key, nid, have, want, flags in todo:
        print(key, have, "→", want, [(f[1], f[2]) for f in flags])
    if not apply_ or not todo:
        print(f"{len(todo)} notas com diferença" + ("" if apply_ else " (sem --aplicar)"))
        return 0
    if em_tela(A) & {t[1] for t in todo}:
        print("nota em tela; adiar"); return 1
    with escrita(A, f"recolor {lesson}", sync=False):
        for key, nid, have, want, flags in todo:
            if have:
                A("removeTags", notes=[nid], tags=" ".join(have))
            A("addTags", notes=[nid], tags=" ".join(want))
            for cid, _, flag in flags:
                A("setSpecificValueOfCard", card=cid, keys=["flags"], newValues=[flag], warning_check=True)
    bad = []
    for key, nid, have, want, flags in todo:
        tags = A("notesInfo", notes=[nid])[0]["tags"]
        if not all(t in tags for t in want):
            bad.append(key)
        for cid, _, flag in flags:
            if A("cardsInfo", cards=[cid])[0]["flags"] != flag:
                bad.append(key)
    print(f"{len(todo)} notas ajustadas; falhas: {bad}")
    with open(run / "journal.jsonl", "a") as j:
        j.write(json.dumps({"op": "recolor", "notas": [t[0] for t in todo], "falhas": bad}) + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
