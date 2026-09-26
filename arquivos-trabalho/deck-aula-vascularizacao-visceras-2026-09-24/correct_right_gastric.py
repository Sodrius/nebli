"""Remove one newly made, contradictory NEBLI copy after full readback backup."""
import json
from datetime import datetime, timezone
from apply import call, HERE, LOCK

SOURCE_NID = 1461962122525

def main():
    with LOCK.open("x", encoding="utf-8") as file:
        file.write(json.dumps({"executor": "Codex", "lesson": "X1 right gastric correction",
                               "at": datetime.now(timezone.utc).isoformat()}))
    try:
        path = HERE / "receipt.json"
        receipt = json.loads(path.read_text(encoding="utf-8"))
        rows = [r for r in receipt["created"] if r["source_nid"] == SOURCE_NID]
        if not rows and (HERE / "removed-copy-backup.json").exists():
            receipt["totals"] = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))["totals"]
            path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
            print("Receipt synchronized with corrected plan.")
            return
        if len(rows) != 1:
            raise RuntimeError(f"Expected one copied note, found {len(rows)}")
        row = rows[0]
        found = call("findNotes", query='tag:"NEBLI::source::nid-1461962122525"')
        if found:
            notes = call("notesInfo", notes=[row["note_id"]])
            cards = call("cardsInfo", cards=row["card_ids"])
            if len(notes) != 1 or any(c["reps"] for c in cards):
                raise RuntimeError("Copy already reviewed or missing")
            if found != [row["note_id"]]:
                raise RuntimeError("Identity mismatch")
            (HERE / "removed-copy-backup.json").write_text(
                json.dumps({"reason": "Contradictory right gastric origin/Extra in source copy",
                            "note": notes[0], "cards": cards}, ensure_ascii=False, indent=2), encoding="utf-8")
            call("deleteNotes", notes=[row["note_id"]])
        elif not (HERE / "removed-copy-backup.json").exists():
            raise RuntimeError("Deleted copy has no backup")
        if call("findNotes", query='tag:"NEBLI::source::nid-1461962122525"'):
            raise RuntimeError("Deletion not confirmed")
        receipt["created"] = [r for r in receipt["created"] if r["source_nid"] != SOURCE_NID]
        receipt["totals"] = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))["totals"]
        path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Removed one contradictory NEBLI copy; source note preserved.")
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
