"""Read-only verification of the live X1 deck against the new plan."""
import json
import re
from collections import Counter
from pathlib import Path
from apply import call, digest, HERE, PLAN

def main():
    receipt = json.loads((HERE / "receipt.json").read_text(encoding="utf-8"))
    before = json.loads((HERE / "before-apply.json").read_text(encoding="utf-8"))
    cards_expected = [cid for row in receipt["created"] for cid in row["card_ids"]]
    live = call("cardsInfo", cards=cards_expected)
    live_ids = call("findCards", query=f'deck:"{PLAN["target_deck"]}"')
    source_ids = [n["noteId"] for n in before["source_notes"]]
    now_source = {n["noteId"]: n for n in call("notesInfo", notes=source_ids)}
    changed_sources = [n["noteId"] for n in before["source_notes"]
                       if digest(n["fields"]) != digest(now_source[n["noteId"]]["fields"])]
    flags = Counter(c["flags"] for c in live)
    missing_answer = [c["cardId"] for c in live if not re.sub(r"<[^>]+>", "", c.get("answer", "")).strip()]
    missing_question = [c["cardId"] for c in live if not re.sub(r"<[^>]+>", "", c.get("question", "")).strip()]
    suspended = [c["cardId"] for c in live if c["queue"] == -1]
    media = Path(call("getMediaDirPath"))
    notes = call("notesInfo", notes=[r["note_id"] for r in receipt["created"]])
    missing_media = []
    for note in notes:
        for field in note["fields"].values():
            for name in re.findall(r'<img[^>]*src="([^"]+)"', field["value"]):
                if not (media / name).is_file():
                    missing_media.append([note["noteId"], name])
    result = {"profile": call("getActiveProfile"), "deck": PLAN["target_deck"],
              "notes": len(notes), "cards": len(live), "deck_cards": len(live_ids),
              "ids_match": set(cards_expected) == set(live_ids),
              "flags": dict(flags), "suspended": suspended,
              "changed_source_fields": changed_sources,
              "missing_question": missing_question, "missing_answer": missing_answer,
              "missing_media": missing_media}
    (HERE / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    assert result["profile"] == PLAN["profile"]
    assert result["notes"] == PLAN["totals"]["notes"]
    assert result["cards"] == PLAN["totals"]["cards"]
    assert result["ids_match"]
    assert flags[5] == PLAN["totals"]["pink"]
    assert flags[3] == PLAN["totals"]["green"]
    assert not (suspended or changed_sources or missing_question or missing_answer or missing_media)

if __name__ == "__main__":
    main()
