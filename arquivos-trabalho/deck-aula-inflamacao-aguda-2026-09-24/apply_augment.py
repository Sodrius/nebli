"""Install reviewed X2 gaps and one shared identity with an exclusive Anki lock."""
import base64
import json
from collections import Counter
from datetime import datetime, timezone
from apply import call, digest, identity, save, HERE, LOCK, PLAN, MODEL_NAMES, TAG

SHARED_NID = 1790190268740
SHARED_SOURCE_NID = 1487642726245

def main():
    aug = json.loads((HERE / "augment-plan.json").read_text(encoding="utf-8"))
    receipt = json.loads((HERE / "receipt.json").read_text(encoding="utf-8"))
    with LOCK.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps({"executor": "Codex", "lesson": "X2 augmentation",
                                 "at": datetime.now(timezone.utc).isoformat()}))
    try:
        assert call("getActiveProfile") == PLAN["profile"]
        existing = call("findCards", query=f'deck:"{PLAN["target_deck"]}"')
        assert len(existing) == PLAN["totals"]["cards"]
        ids = [e["source_nid"] for e in aug["entries"] if e["source_nid"]]
        sources = {n["noteId"]: n for n in call("notesInfo", notes=ids)}
        for e in aug["entries"]:
            nid = e["source_nid"]
            if nid:
                fields = {k: v["value"] for k, v in sources[nid]["fields"].items()}
                assert digest(fields) == e["source_fields_hash"], nid
            assert not call("findNotes", query=f'tag:"{identity(e)}"'), identity(e)
        shared = call("notesInfo", notes=[SHARED_NID])[0]
        assert identity({"source_nid": SHARED_SOURCE_NID}) in shared["tags"]
        save("before-augment.json", {"at": datetime.now(timezone.utc).isoformat(),
                                     "target_cards": existing, "sources": list(sources.values()),
                                     "shared": shared})
        for name in aug["media"]:
            path = HERE / name
            stored = call("storeMediaFile", filename=name,
                          data=base64.b64encode(path.read_bytes()).decode("ascii"))
            assert stored == name, (name, stored)
        new_rows = []
        for e in aug["entries"]:
            tags = list(dict.fromkeys(e["source_tags"] + [TAG, identity(e),
                                          f'NEBLI::origem::{e["origin"]}']))
            note_id = call("addNote", note={"deckName": PLAN["target_deck"],
                          "modelName": MODEL_NAMES[e["source_model"]], "fields": e["fields"],
                          "tags": tags, "options": {"allowDuplicate": True}})
            assert note_id, identity(e)
            note = call("notesInfo", notes=[note_id])[0]
            cards = call("cardsInfo", cards=note["cards"])
            assert len(cards) == e["expected_cards"], (identity(e), len(cards))
            wrong = [c["cardId"] for c in cards if c["deckName"] != PLAN["target_deck"]]
            if wrong:
                assert not any(c["reps"] for c in cards)
                call("changeDeck", cards=wrong, deck=PLAN["target_deck"])
                cards = call("cardsInfo", cards=note["cards"])
            flag = 5 if e["pink"] else (3 if e["high_yield"] else 0)
            if flag:
                for c in cards:
                    call("setSpecificValueOfCard", card=c["cardId"], keys=["flags"],
                         newValues=[flag], warning_check=True)
            row = {"identity": identity(e), "source_nid": e["source_nid"],
                   "note_id": note_id, "card_ids": [c["cardId"] for c in cards],
                   "flag": flag, "origin": e["origin"]}
            new_rows.append(row)
            with (HERE / "journal.jsonl").open("a", encoding="utf-8") as stream:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        call("addTags", notes=[SHARED_NID], tags=TAG)
        shared_now = call("notesInfo", notes=[SHARED_NID])[0]
        assert TAG in shared_now["tags"]
        all_entries = PLAN["entries"] + aug["entries"]
        plan = dict(PLAN)
        plan["entries"] = all_entries
        plan["shared"] = [{"note_id": SHARED_NID, "source_nid": SHARED_SOURCE_NID,
                           "lesson_tag": TAG, "physical_deck":
                           call("cardsInfo", cards=shared_now["cards"])[0]["deckName"]}]
        plan["totals"] = {"notes": len(all_entries),
                          "cards": sum(e["expected_cards"] for e in all_entries),
                          "by_source": dict(Counter({
                              origin: sum(e["expected_cards"] for e in all_entries if e["origin"] == origin)
                              for origin in {e["origin"] for e in all_entries}})),
                          "pink": sum(e["expected_cards"] for e in all_entries if e["pink"]),
                          "green": sum(e["expected_cards"] for e in all_entries if e["high_yield"] and not e["pink"]),
                          "authorial": sum(e["origin"] == "Autoral" for e in all_entries),
                          "shared_cards": len(shared_now["cards"])}
        save("plan-initial.json", PLAN)
        save("plan.json", plan)
        receipt["created"].extend(new_rows)
        receipt["totals"] = plan["totals"]
        receipt["shared"] = plan["shared"]
        save("receipt.json", receipt)
        print(json.dumps(plan["totals"], ensure_ascii=False))
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
