"""Leva o deck já instalado de uma corrida ao plan.json atual (depois de corrigir a spec e rodar build.py --delta).

    python3 -m nebli.sincroniza_aula arquivos-trabalho/<corrida> [--aplicar]

Para cada entrada do plano acha a nota viva (tag NEBLI::source::nid-* ou campo Text/ID); atualiza campos, tags, bandeiras e
posição na fila de novos. Se o conjunto de cards mudou (cloze retirado/acrescentado), recria a nota, só quando nenhum card
dela tem revisão. Nota própria da aula que saiu do plano é apagada, também só sem revisão. Escrita por nebli.decks.escrita
(sync=False), nunca na nota em tela; leitura posterior; diário em journal.jsonl.
"""
import json
import sys
from pathlib import Path

from nebli.decks import Anki, em_tela, escrita


def main(argv):
    run = Path(argv[0]); apply_ = "--aplicar" in argv
    plan = json.loads((run / "plan.json").read_text()); A = Anki()
    base = json.loads(Path("config/fila-novos.json").read_text())["faixas"][plan["short"]]
    info = {n["noteId"]: n for n in A("notesInfo", notes=A("findNotes", query=f'"tag:NEBLI::{plan["lesson_id"]}"'))}
    own = {n for n, i in info.items() if not any(t.startswith("NEBLI::compartilhado::") for t in i["tags"])}

    receipt = json.loads((run / "receipt.json").read_text())
    rec = {x["key"]: x["nid"] for x in receipt["notes"]}

    def match(e):
        if rec.get(e["key"]) in own:
            return [rec[e["key"]]]
        src = [t for t in e["tags"] if t.startswith("NEBLI::source::")]
        if src:
            return [n for n in own if src[0] in info[n]["tags"]]
        k = "Text" if "Text" in e["fields"] else "ID (hidden)"
        return [n for n in own if k in info[n]["fields"] and info[n]["fields"][k]["value"] == e["fields"][k]]

    acts, used = [], set()
    for e in plan["entries"]:
        m = match(e)
        if len(m) != 1:
            print("sem par único:", e["key"], m); return 1
        n = m[0]; used.add(n)
        cards = A("cardsInfo", cards=A("findCards", query=f"nid:{n}"))
        if sorted(c["ord"] for c in cards) != sorted(x["ord"] for x in e["cards"]):
            if any(c["reps"] for c in cards):
                print("cards mudaram e há revisão:", e["key"]); return 1
            acts.append(("recria", e, n, cards))
            continue
        i = info[n]
        flags = [(c["cardId"], x["flag"]) for c in cards for x in e["cards"] if x["ord"] == c["ord"] and c["flags"] != x["flag"] and c["flags"] in (0, 3, 4, 5)]
        if any(i["fields"][k]["value"] != v for k, v in e["fields"].items()) or set(i["tags"]) != set(e["tags"]) or flags:
            acts.append(("atualiza", e, n, cards))
        else:
            acts.append(("fila", e, n, cards))
    gone = [n for n in own - used]
    for n in gone:
        if any(c["reps"] for c in A("cardsInfo", cards=A("findCards", query=f"nid:{n}"))):
            print("nota fora do plano com revisão:", n); return 1
    print([(a, e["key"]) for a, e, _, _ in acts if a != "fila"], "apagar:", gone)
    if not apply_:
        return 0
    if em_tela(A) & ({n for _, _, n, _ in acts} | set(gone)):
        print("nota em tela; adiar"); return 1
    log = []
    with escrita(A, f"sincroniza {plan['short']}", sync=False):
        if gone:
            A("deleteNotes", notes=gone); log.append({"op": "deleteNotes", "nids": gone})
        for a, e, n, cards in acts:
            if a == "recria":
                A("deleteNotes", notes=[n])
                n = A("addNote", note={"deckName": plan["deck"], "modelName": e["model"], "fields": e["fields"], "tags": e["tags"], "options": {"allowDuplicate": True}})
                cards = A("cardsInfo", cards=A("findCards", query=f"nid:{n}")); log.append({"op": "recria", "key": e["key"], "nid": n}); rec[e["key"]] = n
            elif a == "atualiza":
                A("updateNoteFields", note={"id": n, "fields": e["fields"]})
                rm = [t for t in info[n]["tags"] if t not in e["tags"]]
                if rm: A("removeTags", notes=[n], tags=" ".join(rm))
                A("addTags", notes=[n], tags=" ".join(e["tags"])); log.append({"op": "atualiza", "key": e["key"], "nid": n})
            for c in cards:
                x = next(x for x in e["cards"] if x["ord"] == c["ord"])
                if a == "recria" or c["flags"] in (0, 3, 4, 5):
                    A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[x["flag"]], warning_check=True)
                A("setSpecificValueOfCard", card=c["cardId"], keys=["due"], newValues=[base + e["order"] * 10 + c["ord"]], warning_check=True)
    prev = {x["key"]: x for x in receipt["notes"]}
    receipt["notes"] = [dict(prev.get(e["key"], {}), key=e["key"], nid=rec[e["key"]]) for e in plan["entries"] if e["key"] in rec]
    for x in receipt["notes"]:
        if prev.get(x["key"], {}).get("nid") != x["nid"]:
            x.pop("cards", None)
    (run / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=1))
    bad = []
    live = {n["noteId"]: n for n in A("notesInfo", notes=A("findNotes", query=f'"tag:NEBLI::{plan["lesson_id"]}"'))}
    ncards = len(A("findCards", query=f'"tag:NEBLI::{plan["lesson_id"]}" -"tag:NEBLI::compartilhado::*"'))
    for e in plan["entries"]:
        info = live; own = set(live)
        m = match(e)
        if len(m) != 1 or any(live[m[0]]["fields"][k]["value"] != v for k, v in e["fields"].items()) or set(live[m[0]]["tags"]) != set(e["tags"]):
            bad.append(e["key"])
    if ncards != plan["totais"]["cards"]:
        bad.append(f"cards {ncards} != {plan['totais']['cards']}")
    print("falhas:", bad)
    with open(run / "journal.jsonl", "a") as j:
        j.write(json.dumps({"op": "sincroniza", "acoes": log, "falhas": bad}, ensure_ascii=False) + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
