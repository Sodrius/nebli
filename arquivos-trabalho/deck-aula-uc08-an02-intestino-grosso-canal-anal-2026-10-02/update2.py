"""Delta 2 da AN02 (02/10, F-20261002-CLAUDE-09): oclusões do próprio slide, retirada de 7 AnatoKing, ordem estrita dos slides (tags + fila)."""
import base64, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita
A = Anki(); plan = json.loads((HERE / "plan.json").read_text()); old = json.loads((HERE / (sys.argv[1] if len(sys.argv) > 1 else "receipt-v1.json")).read_text())
DECK, LESSON_TAG, SHORT = plan["deck"], f'NEBLI::{plan["lesson_id"]}', plan["short"]
nid = {n["key"]: n["nid"] for n in old["notes"]}
BASE = {"an01": 0, "an02": 100000}.get(SHORT, 0)  # faixa da aula na fila de novos
keys = {e["key"] for e in plan["entries"]}
journal = (HERE / "journal.jsonl").open("a")
def log(**k): k["at"] = datetime.now(timezone.utc).isoformat(); journal.write(json.dumps(k, ensure_ascii=False) + "\n"); journal.flush()

with escrita(A, f"AN02 delta 2 {plan['run_id']}"):
    gone = {k: v for k, v in nid.items() if k not in keys}
    for k, v in gone.items():
        cards = A("cardsInfo", cards=A("findCards", query=f"nid:{v}"))
        if any(c["reps"] or c["flags"] not in (3, 4, 5) for c in cards) or A("notesInfo", notes=[v])[0]["fields"]["NEBLI_Comentario"]["value"]:
            raise SystemExit(f"{k}: já estudado, marcado ou comentado; não apagar")
    if gone:
        A("deleteNotes", notes=list(gone.values())); log(op="deleteNotes", notas=gone)
    for name, rel in plan["media"].items():
        data = base64.b64encode((HERE / rel).read_bytes()).decode()
        if A("retrieveMediaFile", filename=name) != data:
            A("storeMediaFile", filename=name, data=data); log(op="media", file=name)
    results = []
    for e in plan["entries"]:
        if e["key"] in nid:
            n = e_nid = nid[e["key"]]
            tags = A("notesInfo", notes=[n])[0]["tags"]
            stale = [t for t in tags if t.startswith(f"NEBLI::ordem::{SHORT}-")]
            new = next(t for t in e["tags"] if t.startswith(f"NEBLI::ordem::{SHORT}-"))
            if stale != [new]:
                A("removeTags", notes=[n], tags=" ".join(stale)); A("addTags", notes=[n], tags=new); log(op="ordem", key=e["key"], de=stale, para=new)
        else:
            e_nid = A("addNote", note={"deckName": DECK, "modelName": e["model"], "fields": e["fields"], "tags": e["tags"], "options": {"allowDuplicate": True}})
            log(op="addNote", key=e["key"], nid=e_nid)
        cards = A("cardsInfo", cards=A("findCards", query=f"nid:{e_nid}"))
        if sorted(c["ord"] for c in cards) != sorted(x["ord"] for x in e["cards"]): raise RuntimeError(f"{e['key']}: ords divergentes")
        for c in cards:
            flag = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
            if e["key"] not in nid: A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[flag], warning_check=True)
            if c["type"] == 0:  # só card novo: posição na fila = ordem da aula
                A("setSpecificValueOfCard", card=c["cardId"], keys=["due"], newValues=[BASE + e["order"] * 10 + c["ord"]], warning_check=True)
        results.append({"key": e["key"], "nid": e_nid})
    for n, sdata in plan.get("compartilhados", {}).items():  # compartilhados: só a posição nesta aula
        tags = A("notesInfo", notes=[int(n)])[0]["tags"]
        stale = [t for t in tags if t.startswith(f"NEBLI::ordem::{SHORT}-")]
        if stale != [sdata["ordem_tag"]]:
            A("removeTags", notes=[int(n)], tags=" ".join(stale)); A("addTags", notes=[int(n)], tags=sdata["ordem_tag"]); log(op="ordem-compartilhado", nid=n, para=sdata["ordem_tag"])
    problems = []
    for r, e in zip(results, plan["entries"]):
        n = A("notesInfo", notes=[r["nid"]])[0]
        if set(n["tags"]) != set(e["tags"]): problems.append(f"tags {e['key']}")
        if n["fields"]["NEBLI_Comentario"]["value"]: problems.append(f"comentario {e['key']}")
        ci = A("cardsInfo", cards=n["cards"])
        for c in ci:
            if c["flags"] != next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"]): problems.append(f"flag {e['key']}")
            if c["type"] == 0 and c["due"] != BASE + e["order"] * 10 + c["ord"]: problems.append(f"due {e['key']}")
            if c["queue"] == -1: problems.append(f"suspenso {e['key']}")
        r["cards"] = {str(c["cardId"]): {"ord": c["ord"], "flag": c["flags"]} for c in ci}
    flags = [c["flag"] for r in results for c in r["cards"].values()]
    rec = {"run_id": plan["run_id"], "selection_hash": plan["selection_hash"], "deck": DECK, "notes": results, "apagadas": gone,
           "cards_tag_aula": len(A("findCards", query=f'"tag:{LESSON_TAG}"')), "cards_new_lesson": len(flags), "expected": plan["totais"]["cards"],
           "green": flags.count(3), "blue": flags.count(4), "pink": flags.count(5), "problems": problems, "at": datetime.now(timezone.utc).isoformat()}
    (HERE / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    print(json.dumps({k: rec[k] for k in ("cards_new_lesson", "expected", "green", "blue", "pink", "cards_tag_aula", "problems")}, ensure_ascii=False))
    if problems or rec["cards_new_lesson"] != rec["expected"]: raise SystemExit("Readback divergente")
