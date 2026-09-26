"""Remove lateral content from three X2 clone Extras, preserving originals."""
import json
from datetime import datetime, timezone
from apply import call, HERE, LOCK
from prepare import EXTRA_OVERRIDE

def main():
    plan = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
    receipt = json.loads((HERE / "receipt.json").read_text(encoding="utf-8"))
    by_source = {r["source_nid"]: r for r in receipt["created"] if r["source_nid"]}
    with LOCK.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps({"executor": "Codex", "lesson": "X2 Extra scope cleanup",
                                 "at": datetime.now(timezone.utc).isoformat()}))
    try:
        assert call("getActiveProfile") == plan["profile"]
        snapshots = call("notesInfo", notes=[by_source[nid]["note_id"] for nid in EXTRA_OVERRIDE])
        (HERE / "before-extra-cleanup.json").write_text(
            json.dumps(snapshots, ensure_ascii=False, indent=2), encoding="utf-8")
        for nid, extra in EXTRA_OVERRIDE.items():
            note_id = by_source[nid]["note_id"]
            call("updateNoteFields", note={"id": note_id, "fields": {"Extra": extra}})
            now = call("notesInfo", notes=[note_id])[0]
            assert now["fields"]["Extra"]["value"] == extra, nid
            entry = next(e for e in plan["entries"] if e["source_nid"] == nid)
            entry["fields"]["Extra"] = extra
        (HERE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
        result = call("sync")
        (HERE / "sync-after-extra-cleanup.json").write_text(json.dumps({
            "at": datetime.now(timezone.utc).isoformat(), "result": result,
            "cleaned_source_ids": sorted(EXTRA_OVERRIDE)}, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"cleaned_source_ids": sorted(EXTRA_OVERRIDE), "sync": result}))
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
