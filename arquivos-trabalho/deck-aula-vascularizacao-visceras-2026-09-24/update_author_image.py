"""Replace the authored card's support image with the lecture's original figure."""
import base64
import json
from datetime import datetime, timezone
from apply import call, HERE, LOCK

def main():
    with LOCK.open("x", encoding="utf-8") as file:
        file.write(json.dumps({"executor": "Codex", "lesson": "X1 authored image",
                               "at": datetime.now(timezone.utc).isoformat()}))
    try:
        plan = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
        receipt = json.loads((HERE / "receipt.json").read_text(encoding="utf-8"))
        row = next(r for r in receipt["created"] if r["origin"] == "Autoral")
        target = next(e for e in plan["entries"] if e["origin"] == "Autoral")
        note = call("notesInfo", notes=[row["note_id"]])[0]
        (HERE / "before-author-image-update.json").write_text(
            json.dumps(note, ensure_ascii=False, indent=2), encoding="utf-8")
        image = HERE / "nebli_uc08_rectal_arteries_slide22.jpeg"
        name = call("storeMediaFile", filename=image.name,
                    data=base64.b64encode(image.read_bytes()).decode("ascii"))
        if name != image.name:
            raise RuntimeError(f"Unexpected media filename: {name}")
        call("updateNoteFields", note={"id": row["note_id"],
                                       "fields": {"Extra": target["fields"]["Extra"]}})
        updated = call("notesInfo", notes=[row["note_id"]])[0]
        if updated["fields"]["Extra"]["value"] != target["fields"]["Extra"]:
            raise RuntimeError("Readback mismatch")
        print(name, row["note_id"])
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
