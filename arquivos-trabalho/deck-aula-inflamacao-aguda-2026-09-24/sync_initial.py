"""Verify the installed first batch, align its option preset, and sync."""
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from apply import call, HERE, LOCK, PLAN

def main():
    with LOCK.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps({"executor": "Codex", "lesson": "X2 initial sync",
                                 "at": datetime.now(timezone.utc).isoformat()}))
    try:
        assert call("getActiveProfile") == PLAN["profile"]
        for deck in ["NEBLI", "NEBLI::UC03", "NEBLI::UC03::P2", "NEBLI::UC03::P2::Patologia"]:
            call("createDeck", deck=deck)
        script = HERE.parents[1] / "flashcards" / "scripts" / "nebli_novos.py"
        subprocess.run([sys.executable, str(script), "--alinhar"], check=True)
        receipt = json.loads((HERE / "receipt.json").read_text(encoding="utf-8"))
        ids = [cid for row in receipt["created"] for cid in row["card_ids"]]
        cards = call("cardsInfo", cards=ids)
        flags = Counter(c["flags"] for c in cards)
        assert len(cards) == PLAN["totals"]["cards"]
        assert flags[5] == PLAN["totals"]["pink"]
        assert flags[3] == PLAN["totals"]["green"]
        assert all(c["deckName"] == PLAN["target_deck"] for c in cards)
        assert all(c["queue"] != -1 for c in cards)
        result = call("sync")
        record = {"at": datetime.now(timezone.utc).isoformat(), "stage": "initial",
                  "cards": len(cards), "flags": dict(flags), "sync_result": result}
        (HERE / "sync-initial.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(record, ensure_ascii=False))
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
