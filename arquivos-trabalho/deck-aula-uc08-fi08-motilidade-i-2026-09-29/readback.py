"""Readback por identidade a partir do journal (somente leitura) + recibo. Uso: readback.py"""
import json, re, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).parent; sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki
A = Anki(); plan = json.loads((HERE / "plan.json").read_text())
nids = {}
for line in (HERE / "journal.jsonl").read_text().splitlines():
    j = json.loads(line)
    if j["op"] == "addNote": nids[j["key"]] = j["nid"]
canon = lambda d: re.sub(r" \(\d+\)", "", d)
problems, results = [], []
for e in plan["entries"]:
    n = A("notesInfo", notes=[nids[e["key"]]])[0]
    if any(n["fields"][k]["value"] != v for k, v in e["fields"].items()): problems.append(f"campos {e['key']}")
    if set(n["tags"]) != set(e["tags"]): problems.append(f"tags {e['key']}")
    cards = A("cardsInfo", cards=n["cards"])
    if sorted(c["ord"] for c in cards) != sorted(x["ord"] for x in e["cards"]): problems.append(f"ords {e['key']}")
    for c in cards:
        exp = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
        if c["flags"] != exp: problems.append(f"flag {e['key']}")
        if canon(c["deckName"]) != plan["deck"]: problems.append(f"deck {e['key']}")
        if c["queue"] == -1: problems.append(f"suspenso {e['key']}")
    results.append({"key": e["key"], "nid": n["noteId"], "cards": {str(c["cardId"]): {"ord": c["ord"], "flag": c["flags"]} for c in cards}})
q = f'"tag:NEBLI::{plan["lesson_id"]}"'
allc = A("findCards", query=q)
rec = {"run_id": plan["run_id"], "selection_hash": plan["selection_hash"], "deck": plan["deck"], "notes": results,
       "cards_in_lesson": len(allc), "expected": plan["totais"]["cards"],
       "green": len(A("findCards", query=q + " flag:3")), "blue": len(A("findCards", query=q + " flag:4")),
       "problems": problems, "at": datetime.now(timezone.utc).isoformat()}
(HERE / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
print(json.dumps({k: rec[k] for k in ("cards_in_lesson", "expected", "green", "blue", "problems")}, ensure_ascii=False))
