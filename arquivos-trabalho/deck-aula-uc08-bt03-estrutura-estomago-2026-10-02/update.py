"""Delta pós-instalação da BT03 (02/10): texto e Extra dos autorais revistos depois do teste cego."""
import base64, json, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita
A = Anki(); plan = json.loads((HERE / "plan.json").read_text()); rec = json.loads((HERE / "receipt.json").read_text())
nid = {n["key"]: n["nid"] for n in rec["notes"]}
log = (HERE / "journal.jsonl").open("a")
with escrita(A, f"BT03 delta autorais {plan['run_id']}"):
    for e in plan["entries"]:
        if e["origin"] not in ("Autoral", "Histology"): continue
        n = A("notesInfo", notes=[nid[e["key"]]])[0]
        if n["fields"]["NEBLI_Comentario"]["value"] or any(c["reps"] for c in A("cardsInfo", cards=n["cards"])): raise SystemExit(f"{e['key']}: já estudado ou comentado")
        new = {k: e["fields"][k] for k in ("Text", "Extra") if n["fields"][k]["value"] != e["fields"][k]}
        if not new: continue
        A("updateNoteFields", note={"id": nid[e["key"]], "fields": new})
        got = A("notesInfo", notes=[nid[e["key"]]])[0]
        if any(got["fields"][k]["value"] != v for k, v in new.items()) or len(got["cards"]) != len(e["cards"]): raise SystemExit(f"{e['key']}: readback divergente")
        log.write(json.dumps({"op": "updateAutoral", "key": e["key"], "de": {k: n["fields"][k]["value"] for k in new}, "at": datetime.now(timezone.utc).isoformat()}, ensure_ascii=False) + "\n")
print("ok")
