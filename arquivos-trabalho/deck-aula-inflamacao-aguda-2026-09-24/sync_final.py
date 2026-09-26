"""Sync the verified X2 deck and record the AnkiConnect response."""
import json
from datetime import datetime, timezone
from apply import call, HERE, LOCK

def main():
    with LOCK.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps({"executor": "Codex", "lesson": "X2 final sync",
                                 "at": datetime.now(timezone.utc).isoformat()}))
    try:
        verification = json.loads((HERE / "verification.json").read_text(encoding="utf-8"))
        assert verification["profile"] == call("getActiveProfile")
        assert verification["notes"] == 41 and verification["cards"] == 60
        assert verification["flags"].get("5") == 8
        result = call("sync")
        record = {"at": datetime.now(timezone.utc).isoformat(), "result": result,
                  "notes": 41, "cards": 60, "pink": 8}
        (HERE / "sync-final.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(record, ensure_ascii=False))
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
