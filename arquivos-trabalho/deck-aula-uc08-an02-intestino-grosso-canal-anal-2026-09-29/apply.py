"""Instala a aula (plan.json) com lock, diário, snapshot e readback. Uso: apply.py"""
import base64, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita

A = Anki(); plan = json.loads((HERE / "plan.json").read_text())
DECK, LESSON_TAG = plan["deck"], f'NEBLI::{plan["lesson_id"]}'
M_IOE = "NEBLI Image Occlusion Enhanced+ independente - v1"
M_AK = "NEBLI UC08 AnatoKing V2 v1"
journal = (HERE / "journal.jsonl").open("a")
canon = lambda d: re.sub(r" \(\d+\)", "", d)


def log(**k):
    k["at"] = datetime.now(timezone.utc).isoformat(); journal.write(json.dumps(k, ensure_ascii=False) + "\n"); journal.flush()


def ensure_ioe_model():
    if M_IOE in A("modelNames"): return
    src = "Image Occlusion Enhanced+"
    t = A("modelTemplates", modelName=src)
    A("createModel", modelName=M_IOE, inOrderFields=A("modelFieldNames", modelName=src),
      css=A("modelStyling", modelName=src)["css"], isCloze=False,
      cardTemplates=[{"Name": k, "Front": v["Front"], "Back": v["Back"]} for k, v in t.items()])
    log(op="createModel", model=M_IOE, clone_of=src)


def enlarge_anatoking():
    """F-C23: imagem principal do AnatoKing maior — só no clone NEBLI (0 notas antes desta corrida)."""
    css = A("modelStyling", modelName=M_AK)["css"]
    new = css.replace("img {\n  max-width: 65%;\n  max-height: 55%;", "img {\n  max-width: 95%;\n  max-height: none;")
    new = re.sub(r"(#extra img,\n#misnomers img,\n#cadaver img,\n#imaging img,\n#model img \{\n  max-width: )40%;", r"\g<1>95%;", new)
    if new != css:
        (HERE / "backup-css-anatoking.css").write_text(css)
        A("updateModelStyling", model={"name": M_AK, "css": new}); log(op="updateModelStyling", model=M_AK)


def main():
    with escrita(A, f"{plan['short'].upper()} {plan['run_id']}"):
        if A("findCards", query=f'"tag:{LESSON_TAG}"'):
            raise SystemExit("A aula já tem cards — reconciliar antes de reaplicar")
        n_ak = len(A("findNotes", query=f'"note:{M_AK}"'))
        shared = A("notesInfo", notes=[int(k) for k in plan["compartilhados"]])
        before = {"decks_uc08": [d for d in A("deckNames") if d.startswith("NEBLI::UC08")], "notes_anatoking_clone": n_ak,
                  "compartilhados": {str(n["noteId"]): n["tags"] for n in shared}, "at": datetime.now(timezone.utc).isoformat()}
        (HERE / "before.json").write_text(json.dumps(before, ensure_ascii=False, indent=1))
        ensure_ioe_model()
        if n_ak == 0: enlarge_anatoking()
        for name, rel in plan["media"].items():
            if not A("retrieveMediaFile", filename=name):
                A("storeMediaFile", filename=name, data=base64.b64encode((HERE / rel).read_bytes()).decode()); log(op="media", file=name)
        A("createDeck", deck=DECK); log(op="createDeck", deck=DECK)
        root = A("getDeckConfig", deck="NEBLI")
        chain = ["::".join(DECK.split("::")[:i]) for i in range(2, DECK.count("::") + 2)]
        wrong = [d for d in chain if A("getDeckConfig", deck=d)["id"] != root["id"]]
        if wrong: A("setDeckConfigId", decks=wrong, configId=root["id"]); log(op="preset", decks=wrong)
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
            results.append({"key": e["key"], "nid": nid})
        # associação dos alvos já vivos em FI08/BT03: só tags, sem conteúdo/flag/deck
        A("addTags", notes=[int(k) for k in plan["compartilhados"]], tags=f"{LESSON_TAG} NEBLI::compartilhado::{plan['short']}")
        log(op="addTags-compartilhados", notes=list(plan["compartilhados"]))
        problems = []
        for r, e in zip(results, plan["entries"]):
            n = A("notesInfo", notes=[r["nid"]])[0]
            if any(n["fields"][k]["value"] != v for k, v in e["fields"].items()): problems.append(f"campos {e['key']}")
            if set(n["tags"]) != set(e["tags"]): problems.append(f"tags {e['key']}")
            ci = A("cardsInfo", cards=n["cards"])
            for c in ci:
                exp = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
                if c["flags"] != exp: problems.append(f"flag {e['key']}")
                if canon(c["deckName"]) != DECK: problems.append(f"deck {e['key']}")
                if c["queue"] == -1: problems.append(f"suspenso {e['key']}")
            r["cards"] = {str(c["cardId"]): {"ord": c["ord"], "flag": c["flags"]} for c in ci}
        for n in A("notesInfo", notes=[int(k) for k in plan["compartilhados"]]):
            old = before["compartilhados"][str(n["noteId"])]
            if set(n["tags"]) != set(old) | {LESSON_TAG, f"NEBLI::compartilhado::{plan['short']}"}: problems.append(f"tags compartilhado {n['noteId']}")
            for c in A("cardsInfo", cards=n["cards"]):
                if "Anatomia" in c["deckName"]: problems.append(f"compartilhado movido {n['noteId']}")
        q = f'"deck:{DECK}"'
        rec = {"run_id": plan["run_id"], "selection_hash": plan["selection_hash"], "deck": DECK, "notes": results,
               "cards_in_deck": len(A("findCards", query=f'"tag:{LESSON_TAG}" "note:{M_IOE}" or "tag:{LESSON_TAG}"')),
               "cards_new_lesson": sum(len(r["cards"]) for r in results), "expected": plan["totais"]["cards"],
               "green": sum(1 for r in results for c in r["cards"].values() if c["flag"] == 3),
               "blue": sum(1 for r in results for c in r["cards"].values() if c["flag"] == 4),
               "compartilhados_tag": list(plan["compartilhados"]), "problems": problems, "at": datetime.now(timezone.utc).isoformat()}
        (HERE / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
        print(json.dumps({k: rec[k] for k in ("cards_new_lesson", "expected", "green", "blue", "problems")}, ensure_ascii=False))
        if problems or rec["cards_new_lesson"] != plan["totais"]["cards"]: raise SystemExit("Readback divergente — ver receipt.json (sem sync)")
    log(op="sync-solicitado-pelo-escrita")


if __name__ == "__main__":
    main()
