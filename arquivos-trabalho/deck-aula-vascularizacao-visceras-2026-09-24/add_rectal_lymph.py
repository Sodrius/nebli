"""Add two source-verified AnKing rectal lymph cards to the live X1 deck."""
import json
from datetime import datetime, timezone
from apply import call, digest, HERE, LOCK, MODEL_NAMES

IDS = {1486771351448, 1486771380083}

def main():
    with LOCK.open("x", encoding="utf-8") as file:
        file.write(json.dumps({"executor": "Codex", "lesson": "X1 rectal lymph completion",
                               "at": datetime.now(timezone.utc).isoformat()}))
    try:
        plan = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
        path = HERE / "receipt.json"
        receipt = json.loads(path.read_text(encoding="utf-8"))
        entries = [e for e in plan["entries"] if e["source_nid"] in IDS]
        if len(entries) != 2:
            raise RuntimeError("Expected two planned additions")
        if call("getActiveProfile") != plan["profile"]:
            raise RuntimeError("Profile changed")
        source = {n["noteId"]: n for n in call("notesInfo", notes=list(IDS))}
        before = {"deck_cards": call("findCards", query=f'deck:"{plan["target_deck"]}"'),
                  "source_notes": list(source.values())}
        (HERE / "before-rectal-lymph-add.json").write_text(
            json.dumps(before, ensure_ascii=False, indent=2), encoding="utf-8")
        for entry in entries:
            nid = entry["source_nid"]
            if digest({k: v["value"] for k, v in source[nid]["fields"].items()}) != entry["source_fields_hash"]:
                raise RuntimeError(f"Source changed: {nid}")
            tag = f'NEBLI::source::nid-{nid}'
            if call("findNotes", query=f'tag:"{tag}"'):
                raise RuntimeError(f"Identity already present: {nid}")
            model = MODEL_NAMES[entry["source_model"]]
            note_id = call("addNote", note={"deckName": plan["target_deck"],
                                             "modelName": model, "fields": entry["fields"],
                                             "tags": list(dict.fromkeys(entry["source_tags"] +
                                                [f'NEBLI::{plan["lesson_id"]}', tag, "NEBLI::origem::AnKing"])),
                                             "options": {"allowDuplicate": True}})
            note = call("notesInfo", notes=[note_id])[0]
            cards = call("cardsInfo", cards=note["cards"])
            if len(cards) != 1 or cards[0]["deckName"] != plan["target_deck"]:
                raise RuntimeError(f"Card placement/count issue: {nid}")
            flag = 5 if entry["pink"] else (3 if entry["high_yield"] else 0)
            if flag:
                call("setSpecificValueOfCard", card=cards[0]["cardId"],
                     keys=["flags"], newValues=[flag], warning_check=True)
            receipt["created"].append({"identity": tag, "source_nid": nid,
                                       "note_id": note_id, "card_ids": [cards[0]["cardId"]],
                                       "flag": flag, "origin": "AnKing"})
        receipt["totals"] = plan["totals"]
        path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Added two rectal lymph cards")
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
