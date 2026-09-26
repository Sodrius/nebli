"""Read live Pathoma acute tag neighbors absent from the lexical inventory."""
import json
from pathlib import Path
from inventory import call, batches, HERE

def main():
    path = HERE / "inventory.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    have = {n["nid"] for n in data["notes"]}
    tagged = set(call("findNotes", query="tag:*Pathoma::02_Inflammation::01_Acute_Inflammation*"))
    ids = sorted(tagged - have)
    notes = [x for group in batches(ids) for x in call("notesInfo", notes=group)]
    card_ids = [cid for n in notes for cid in n["cards"]]
    cards = {c["cardId"]: c for group in batches(card_ids) for c in call("cardsInfo", cards=group)}
    for n in notes:
        data["notes"].append({"nid": n["noteId"], "model": n["modelName"],
            "fields": {k: v["value"] for k, v in n["fields"].items()}, "tags": n["tags"],
            "cards": [{"cid": cid, "deck": cards[cid]["deckName"],
                       "flags": cards[cid]["flags"], "queue": cards[cid]["queue"]}
                      for cid in n["cards"]]})
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Added {len(notes)} Pathoma neighbors; total {len(data['notes'])}")

if __name__ == "__main__":
    main()
