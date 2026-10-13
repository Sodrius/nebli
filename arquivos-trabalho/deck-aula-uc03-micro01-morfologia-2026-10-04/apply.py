"""Instala a aula (plan.json) com lock, diário, snapshot e readback. Uso: apply.py"""
import base64, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita

A = Anki(); plan = json.loads((HERE / "plan.json").read_text())
DECK, LESSON, LESSON_TAG = plan["deck"], plan["lesson_id"], f'NEBLI::{plan["lesson_id"]}'
RANK = {3: 3, 4: 2, 5: 1}  # verde > azul > rosa
FLAG = {"verde": 3, "azul": 4, "rosa": 5}
BASE = {"an01": 0, "an02": 100000, "bt03": 200000, "bt04": 300000, "an07": 400000, "fi08": 500000, "fi09": 600000, "fi05": 700000, "fi06": 800000, "pr02": 1190000, "micro01": 1400000}[plan["short"]]  # faixa da aula na fila de novos
journal = (HERE / "journal.jsonl").open("a")
canon = lambda d: re.sub(r" \(\d+\)", "", d)


def log(**k):
    k["at"] = datetime.now(timezone.utc).isoformat(); journal.write(json.dumps(k, ensure_ascii=False) + "\n"); journal.flush()


def ensure_clones():
    """Clona os tipos NEBLI v1 (sem NEBLI_Comentario) em v2 com o campo ao fim; tipo novo não muda o esquema dos existentes."""
    for new, old in plan.get("clones", {}).items():
        if new in A("modelNames"):
            continue
        t = A("modelTemplates", modelName=old)
        A("createModel", modelName=new, inOrderFields=A("modelFieldNames", modelName=old) + ["NEBLI_Comentario"],
          css=A("modelStyling", modelName=old)["css"], isCloze=any("{{cloze:" in v["Front"] for v in t.values()),
          cardTemplates=[{"Name": k, "Front": v["Front"], "Back": v["Back"]} for k, v in t.items()])
        got = A("modelTemplates", modelName=new)
        if list(got) != list(t) or any(got[k] != t[k] for k in t):
            raise SystemExit(f"clone {new}: templates divergem de {old}")
        log(op="createModel", model=new, clone_of=old)


def main():
    with escrita(A, f"{plan['short'].upper()} {plan['run_id']}"):
        ensure_clones()
        shared_ids = [int(k) for k in plan["compartilhados"]]
        if set(A("findNotes", query=f'"tag:{LESSON_TAG}"')) - set(shared_ids):
            raise SystemExit("A aula já tem cards — reconciliar antes de reaplicar")
        shared = A("notesInfo", notes=shared_ids)
        before = {"decks_uc08": [d for d in A("deckNames") if d.startswith("NEBLI") and "UC08" in d],
                  "compartilhados": {str(n["noteId"]): {"tags": n["tags"], "cards": {str(c["cardId"]): c["flags"] for c in A("cardsInfo", cards=n["cards"])}} for n in shared},
                  "at": datetime.now(timezone.utc).isoformat()}
        (HERE / "before.json").write_text(json.dumps(before, ensure_ascii=False, indent=1))
        for name, rel in plan["media"].items():
            if not A("retrieveMediaFile", filename=name):
                A("storeMediaFile", filename=name, data=base64.b64encode((HERE / rel).read_bytes()).decode()); log(op="media", file=name)
        A("createDeck", deck=DECK); log(op="createDeck", deck=DECK)
        root = A("getDeckConfig", deck="NEBLI")
        chain = ["::".join(DECK.split("::")[:i]) for i in range(2, DECK.count("::") + 2)]
        wrong = [d for d in chain if A("getDeckConfig", deck=d)["id"] != root["id"]]
        if wrong: A("setDeckConfigId", decks=wrong, configId=root["id"]); log(op="preset", decks=wrong)
        results = []
        for e in plan["entries"]:  # ordem do plano = sequência da aula: criação e fila de novos seguem os slides
            nid = A("addNote", note={"deckName": DECK, "modelName": e["model"], "fields": e["fields"], "tags": e["tags"],
                                     "options": {"allowDuplicate": True}})
            log(op="addNote", key=e["key"], nid=nid)
            cards = A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))
            ords = sorted(c["ord"] for c in cards); want = sorted(x["ord"] for x in e["cards"])
            if ords != want: raise RuntimeError(f"{e['key']}: ords {ords} != {want}")
            for c in cards:
                flag = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
                A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[flag], warning_check=True)
            for c in cards:  # fila de novos na ordem dos slides
                A("setSpecificValueOfCard", card=c["cardId"], keys=["due"], newValues=[BASE + e["order"] * 10 + c["ord"]], warning_check=True)
            results.append({"key": e["key"], "nid": nid})
        # compartilhados: só tags (aula, cor e posição nesta aula); bandeira sobe apenas se a cor nova for maior e não houver marca pessoal
        for n in shared:
            s = plan["compartilhados"][str(n["noteId"])]
            old = " ".join(f"NEBLI::cor::{LESSON}::{x}" for x in FLAG if x != s["cor"])
            A("removeTags", notes=[n["noteId"]], tags=old)
            A("addTags", notes=[n["noteId"]], tags=f"{LESSON_TAG} NEBLI::compartilhado::{plan['short']} NEBLI::cor::{LESSON}::{s['cor']} {s['ordem_tag']}")
            for c in A("cardsInfo", cards=n["cards"]):
                if c["flags"] in RANK and RANK[FLAG[s["cor"]]] > RANK[c["flags"]]:
                    A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[FLAG[s["cor"]]], warning_check=True)
                    log(op="flag-compartilhado", card=c["cardId"], de=c["flags"], para=FLAG[s["cor"]])
            log(op="addTags-compartilhado", nid=n["noteId"], cor=s["cor"], ordem=s["ordem_tag"])
        problems = []
        for r, e in zip(results, plan["entries"]):
            n = A("notesInfo", notes=[r["nid"]])[0]
            if any(n["fields"][k]["value"] != v for k, v in e["fields"].items()): problems.append(f"campos {e['key']}")
            if n["fields"]["NEBLI_Comentario"]["value"]: problems.append(f"comentario {e['key']}")
            if set(n["tags"]) != set(e["tags"]): problems.append(f"tags {e['key']}")
            ci = A("cardsInfo", cards=n["cards"])
            for c in ci:
                exp = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
                if c["flags"] != exp: problems.append(f"flag {e['key']}")
                if canon(c["deckName"]) != DECK: problems.append(f"deck {e['key']}")
                if c["queue"] == -1: problems.append(f"suspenso {e['key']}")
            r["cards"] = {str(c["cardId"]): {"ord": c["ord"], "flag": c["flags"]} for c in ci}
        for n in A("notesInfo", notes=shared_ids):
            for c in A("cardsInfo", cards=n["cards"]):
                if canon(c["deckName"]) == DECK: problems.append(f"compartilhado movido {n['noteId']}")
        flags = [c["flag"] for r in results for c in r["cards"].values()]
        rec = {"run_id": plan["run_id"], "selection_hash": plan["selection_hash"], "deck": DECK, "notes": results,
               "cards_tag_aula": len(A("findCards", query=f'"tag:{LESSON_TAG}"')),
               "cards_new_lesson": len(flags), "expected": plan["totais"]["cards"],
               "green": flags.count(3), "blue": flags.count(4), "pink": flags.count(5),
               "compartilhados_tag": shared_ids, "problems": problems, "at": datetime.now(timezone.utc).isoformat()}
        (HERE / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
        print(json.dumps({k: rec[k] for k in ("cards_new_lesson", "expected", "green", "blue", "pink", "cards_tag_aula", "problems")}, ensure_ascii=False))
        if problems or rec["cards_new_lesson"] != plan["totais"]["cards"]: raise SystemExit("Readback divergente — ver receipt.json (sem sync)")
    log(op="sync-solicitado-pelo-escrita")


if __name__ == "__main__":
    main()
