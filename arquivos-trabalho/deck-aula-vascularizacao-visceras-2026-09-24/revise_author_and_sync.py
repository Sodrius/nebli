"""Apply the cross-feedback wording to X1 and sync its live deck."""
import json
from datetime import datetime, timezone
from apply import call, HERE, LOCK


def main():
    plan = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
    receipt = json.loads((HERE / "receipt.json").read_text(encoding="utf-8"))
    row = next(r for r in receipt["created"] if r["origin"] == "Autoral")
    target = next(e for e in plan["entries"] if e["origin"] == "Autoral")
    with LOCK.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps({"executor": "Codex", "lesson": "X1 wording and sync",
                                 "at": datetime.now(timezone.utc).isoformat()}))
    try:
        assert call("getActiveProfile") == plan["profile"]
        note = call("notesInfo", notes=[row["note_id"]])[0]
        (HERE / "before-author-wording-update.json").write_text(
            json.dumps(note, ensure_ascii=False, indent=2), encoding="utf-8")
        fields = {name: target["fields"][name] for name in ("Text", "Extra")}
        call("updateNoteFields", note={"id": row["note_id"], "fields": fields})
        readback = call("notesInfo", notes=[row["note_id"]])[0]
        assert all(readback["fields"][name]["value"] == value for name, value in fields.items())
        result = call("sync")
        (HERE / "sync-result.json").write_text(
            json.dumps({"at": datetime.now(timezone.utc).isoformat(),
                        "result": result}, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"note_id": row["note_id"], "sync": result}, ensure_ascii=False))
    finally:
        LOCK.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
