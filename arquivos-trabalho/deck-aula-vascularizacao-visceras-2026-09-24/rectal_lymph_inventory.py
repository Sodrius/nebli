"""Read-only second search for rectal lymphatic coverage."""
import json
import re
from pathlib import Path
from apply import call, HERE

terms = ['"pectinate" "lymph"', '"rectum" "lymph"', '"anal canal" "lymph"']
hits = {q: call("findNotes", query=q) for q in terms}
ids = sorted(set().union(*hits.values()))
notes = call("notesInfo", notes=ids)
cards = call("cardsInfo", cards=[cid for n in notes for cid in n["cards"]])
by_nid = {}
for c in cards:
    by_nid.setdefault(c["note"], []).append({"cid": c["cardId"], "deck": c["deckName"],
                                               "ord": c["ord"], "queue": c["queue"], "flags": c["flags"]})
rows = []
for n in notes:
    fields = {k: v["value"] for k, v in n["fields"].items()}
    plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", " ".join(fields.values())))
    rows.append({"nid": n["noteId"], "model": n["modelName"], "tags": n["tags"],
                 "fields": fields, "cards": by_nid.get(n["noteId"], []), "preview": plain[:450]})
(HERE / "inventory-rectal-lymph.json").write_text(
    json.dumps({"queries": hits, "notes": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
print({"queries": {q: len(v) for q, v in hits.items()}, "notes": len(rows)})
