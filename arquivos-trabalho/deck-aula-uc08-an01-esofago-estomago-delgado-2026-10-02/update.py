"""Delta pós-instalação (02/10): nome da estrutura em negrito no Remarks das 18 oclusões BlueLink (verso), para o Tab conhecer o alvo."""
import json, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita
A = Anki(); plan = json.loads((HERE / "plan.json").read_text()); rec = json.loads((HERE / "receipt.json").read_text())
nid = {n["key"]: n["nid"] for n in rec["notes"]}
log = (HERE / "journal.jsonl").open("a")
with escrita(A, f"AN01 delta Remarks {plan['run_id']}"):
    for e in plan["entries"]:
        if e["kind"] != "bluelink": continue
        n = A("notesInfo", notes=[nid[e["key"]]])[0]
        other = {k: v["value"] for k, v in n["fields"].items() if k != "Remarks"}
        norm = lambda x: x.replace(" />", ">")  # o Anki normaliza <img ... /> depois de gravar
        if any(norm(other[k]) != norm(e["fields"][k]) for k in other): raise SystemExit(f"{e['key']}: nota mudou desde a instalação")
        A("updateNoteFields", note={"id": nid[e["key"]], "fields": {"Remarks": e["fields"]["Remarks"]}})
        got = A("notesInfo", notes=[nid[e["key"]]])[0]["fields"]["Remarks"]["value"]
        if got != e["fields"]["Remarks"]: raise SystemExit(f"{e['key']}: readback divergente")
        log.write(json.dumps({"op": "updateRemarks", "key": e["key"], "nid": nid[e["key"]], "de": n["fields"]["Remarks"]["value"], "at": datetime.now(timezone.utc).isoformat()}, ensure_ascii=False) + "\n")
print("ok")
