"""Verifica a entrega final de 88 cards e o APKG v2."""
import collections
import html
import json
import re
import sqlite3
import tempfile
import zipfile
from pathlib import Path

from inventory_vascularizacao import call
from prepare_vascularizacao import DECK, ROOT


def main():
    receipt = json.loads((ROOT / "receipt-v2.json").read_text(encoding="utf-8"))
    notes = call("notesInfo", notes=receipt["all_note_ids"])
    cards = call("cardsInfo", cards=[card for note in notes for card in note["cards"]])
    errors = []
    if len(notes) != 47 or len(cards) != 88:
        errors.append(["counts", len(notes), len(cards)])
    if any(card["deckName"] != DECK for card in cards):
        errors.append(["wrong_deck"])
    if any(card["queue"] == -1 for card in cards):
        errors.append(["suspended"])
    red = call("findCards", query=f'deck:"{DECK}" flag:1')
    green = call("findCards", query=f'deck:"{DECK}" flag:3')
    if red or len(green) != 37:
        errors.append(["flags", len(red), len(green)])

    required = set()
    forbidden = ["Faculdade:", "Step 1:", "High yield:", "Low yield:"]
    for note in notes:
        for field in note["fields"].values():
            for name in re.findall(r'<img[^>]+src=["\x27]([^"\x27]+)', field["value"], re.I):
                name = html.unescape(name)
                if not name.startswith(("http:", "https:", "data:")):
                    required.add(name)
    for card in cards:
        rendered = f'{card.get("question", "")} {card.get("answer", "")}'
        for marker in forbidden:
            if marker in rendered:
                errors.append(["visible_meta", card["cardId"], marker])
        if "{{c" in rendered:
            errors.append(["unrendered_cloze", card["cardId"]])
    missing_live = sorted(name for name in required if not (Path(call("getMediaDirPath")) / name).exists())
    if missing_live:
        errors.append(["missing_live_media", missing_live])

    package = Path(receipt["package"])
    package_info = {}
    with zipfile.ZipFile(package) as archive:
        names = archive.namelist()
        media = json.loads(archive.read("media"))
        missing_package = sorted(required - set(media.values()))
        if missing_package:
            errors.append(["missing_package_media", missing_package])
        sqlite_name = next((name for name in names if name in {"collection.anki2", "collection.anki21"}), None)
        if sqlite_name:
            with tempfile.TemporaryDirectory(prefix="nebli-vascular-v2-") as temporary:
                db = Path(temporary) / sqlite_name
                db.write_bytes(archive.read(sqlite_name))
                connection = sqlite3.connect(f"{db.as_uri()}?mode=ro", uri=True)
                package_info["notes"] = connection.execute("select count(*) from notes").fetchone()[0]
                package_info["cards"] = connection.execute("select count(*) from cards").fetchone()[0]
                connection.close()
        package_info.update({"files": len(names), "media": len(media)})
        if package_info.get("notes") != 47 or package_info.get("cards") != 88:
            errors.append(["package_counts", package_info])

    outcome = {
        "status": "failed" if errors else "passed",
        "notes": len(notes), "cards": len(cards),
        "cards_by_origin": receipt["cards_by_origin"],
        "green_high_yield": len(green), "red_improve": len(red),
        "suspended": sum(card["queue"] == -1 for card in cards),
        "authorial": 1,
        "authorial_reason": receipt["authorial_reason"],
        "required_media": len(required), "package": package_info,
        "errors": errors,
        "limitations": [
            "Nenhuma prova antiga específica desta aula foi localizada.",
            "Sincronização com AnkiWeb e abertura no Mac/Android não foram verificadas deste Windows.",
        ],
    }
    save_path = ROOT / "verification-v2.json"
    save_path.write_text(json.dumps(outcome, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(outcome, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
