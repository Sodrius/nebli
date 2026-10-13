"""Instala a seleção revisada da FI08 (plan.json) com lock, diário e readback. Uso: apply.py [--dry-run]"""
import base64, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita

A = Anki()
plan = json.loads((HERE / "plan.json").read_text())
DECK = plan["deck"]
MEDIA = {"nebli-uc08-fi08-juncao-neuroefetora.jpeg": HERE / "fontes" / "p5_img0.jpeg"}
journal = (HERE / "journal.jsonl").open("a")


def log(**k):
    k["at"] = datetime.now(timezone.utc).isoformat(); journal.write(json.dumps(k, ensure_ascii=False) + "\n"); journal.flush()


def canon(d): return re.sub(r" \(\d+\)", "", d)


def main(dry):
    before = {"medical_cards": len(A("findCards", query='"deck:NEBLI::*"')) if False else None}
    if dry:
        print("dry-run: nada escrito"); return
    with escrita(A, f"FI08 {plan['run_id']}"):
        names = A("deckNames")
        before = {"decks_uc08": [d for d in names if d.startswith("NEBLI::UC08")],
                  "cards_nebli": len(A("findCards", query='deck:NEBLI -deck:NEBLI-deck*'))}
        (HERE / "before.json").write_text(json.dumps(before, ensure_ascii=False, indent=1))
        if A("findCards", query=f'"deck:{DECK}"'):
            raise SystemExit("Deck da aula já tem cards — reconciliar antes de reaplicar")
        A("createDeck", deck=DECK); log(op="createDeck", deck=DECK)
        root_cfg = A("getDeckConfig", deck="NEBLI")
        chain = ["::".join(DECK.split("::")[:i]) for i in range(2, DECK.count("::") + 2)]
        wrong = [d for d in chain if A("getDeckConfig", deck=d)["id"] != root_cfg["id"]]
        if wrong: A("setDeckConfigId", decks=wrong, configId=root_cfg["id"]); log(op="preset", decks=wrong, config=root_cfg["id"])
        for name, path in MEDIA.items():
            A("storeMediaFile", filename=name, data=base64.b64encode(path.read_bytes()).decode()); log(op="media", file=name)
        results = []
        for e in plan["entries"]:
            nid = A("addNote", note={"deckName": DECK, "modelName": e["model"], "fields": e["fields"], "tags": e["tags"],
                                     "options": {"allowDuplicate": True}})
            log(op="addNote", key=e["key"], nid=nid)
            cards = A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))
            ords = sorted(c["ord"] for c in cards); want = sorted(x["ord"] for x in e["cards"])
            if ords != want: raise RuntimeError(f"{e['key']}: ords {ords} != {want}")
            for c in cards:
                flag = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
                A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[flag], warning_check=True)
            log(op="flags", key=e["key"], cards={c["cardId"]: c["ord"] for c in cards})
            results.append({"key": e["key"], "nid": nid, "cards": {str(c["cardId"]): c["ord"] for c in cards}})
        # readback
        problems = []
        for r, e in zip(results, plan["entries"]):
            n = A("notesInfo", notes=[r["nid"]])[0]
            if any(n["fields"][k]["value"] != v for k, v in e["fields"].items()): problems.append(f"campos {e['key']}")
            for c in A("cardsInfo", cards=[int(x) for x in r["cards"]]):
                exp = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
                if c["flags"] != exp: problems.append(f"flag {e['key']} {c['cardId']}")
                if canon(c["deckName"]) != DECK: problems.append(f"deck {e['key']}")
                if c["queue"] == -1: problems.append(f"suspenso {e['key']}")
        allc = A("findCards", query=f'"deck:{DECK}"')
        receipt = {"run_id": plan["run_id"], "selection_hash": plan["selection_hash"], "deck": DECK, "notes": results,
                   "cards_in_deck": len(allc), "expected": plan["totais"]["cards"],
                   "green": len(A("findCards", query=f'"deck:{DECK}" flag:3')), "blue": len(A("findCards", query=f'"deck:{DECK}" flag:4')),
                   "problems": problems, "before": before, "at": datetime.now(timezone.utc).isoformat()}
        (HERE / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=1))
        print(json.dumps({k: receipt[k] for k in ("cards_in_deck", "expected", "green", "blue", "problems")}, ensure_ascii=False))
        if problems or len(allc) != plan["totais"]["cards"]: raise SystemExit("Readback divergente — ver receipt.json")
    log(op="sync-solicitado-pelo-escrita")


if __name__ == "__main__":
    main("--dry-run" in sys.argv)
