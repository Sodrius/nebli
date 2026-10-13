"""Atualiza campos das notas da aula que divergem de plan.json (mesma identidade; backup; readback). Uso: update.py"""
import json, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).parent; sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita
A = Anki(); plan = json.loads((HERE / "plan.json").read_text())
nid = {r["key"]: r["nid"] for r in json.loads((HERE / "receipt-v1.json").read_text())["notes"]}
j = (HERE / "journal.jsonl").open("a")
diff = []
for e in plan["entries"]:
    n = A("notesInfo", notes=[nid[e["key"]]])[0]
    if any(n["fields"][k]["value"] != v for k, v in e["fields"].items()): diff.append((e, n))
print("a atualizar:", [e["key"] for e, _ in diff])
if diff:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    (HERE / f"backup-update-{stamp}.json").write_text(json.dumps([n for _, n in diff], ensure_ascii=False))
    with escrita(A, f"AN01 update {plan['selection_hash']}"):
        for e, n in diff:
            A("updateNoteFields", note={"id": n["noteId"], "fields": e["fields"]})
            j.write(json.dumps({"op": "updateNoteFields", "key": e["key"], "nid": n["noteId"], "at": datetime.now(timezone.utc).isoformat()}) + "\n")
        bad = [e["key"] for e, n in diff if any(A("notesInfo", notes=[n["noteId"]])[0]["fields"][k]["value"] != v for k, v in e["fields"].items())]
        print("readback divergente:", bad or "nenhum")
        if bad: raise SystemExit("divergência — sem sync")
rec = json.loads((HERE / "receipt-v1.json").read_text()); rec["selection_hash"] = plan["selection_hash"]; rec["updated"] = [e["key"] for e, _ in diff]
(HERE / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
