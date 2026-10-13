"""v2: varicosidades → modelo AnKing v3 + sem dica 'pl.'; NO ganha 'EEI = ...' no Extra. Só essas duas notas."""
import json, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).parent; sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita
A = Anki(); plan = json.loads((HERE / "plan.json").read_text())
rec = json.loads((HERE / "receipt-v1.json").read_text())
nid = {n["key"]: n["nid"] for n in rec["notes"]}
E = {e["key"]: e for e in plan["entries"]}
j = (HERE / "journal.jsonl").open("a")
def log(**k): k["at"] = datetime.now(timezone.utc).isoformat(); j.write(json.dumps(k, ensure_ascii=False) + "\n"); j.flush()
before = A("notesInfo", notes=[nid["varicosidades"], nid["no-relaxa"]])
(HERE / "before-v2.json").write_text(json.dumps(before, ensure_ascii=False, indent=1))
with escrita(A, "FI08 v2 ajustes"):
    v = E["varicosidades"]
    A("updateNoteModel", note={"id": nid["varicosidades"], "modelName": v["model"], "fields": v["fields"], "tags": v["tags"]})
    log(op="updateNoteModel", key="varicosidades", nid=nid["varicosidades"], model=v["model"])
    A("updateNoteFields", note={"id": nid["no-relaxa"], "fields": {"Extra": E["no-relaxa"]["fields"]["Extra"]}})
    log(op="updateNoteFields", key="no-relaxa", nid=nid["no-relaxa"], fields=["Extra"])
    after = A("notesInfo", notes=[nid["varicosidades"]])[0]
    ci = A("cardsInfo", cards=after["cards"])
    print(after["modelName"], [(c["cardId"], c["ord"], c["flags"]) for c in ci], "antes:", before[0]["cards"])
