"""Verificação somente leitura da coleção viva e do pacote exportado."""
from __future__ import annotations

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


def main() -> None:
    plan = json.loads((ROOT / "plan.json").read_text(encoding="utf-8"))
    receipt = json.loads((ROOT / "receipt.json").read_text(encoding="utf-8"))
    note_ids = [result["new_nid"] for result in receipt["results"]]
    notes = call("notesInfo", notes=note_ids)
    card_ids = [card for note in notes for card in note["cards"]]
    cards = call("cardsInfo", cards=card_ids)
    errors: list[object] = []

    if len(notes) != plan["totals"]["notes"]:
        errors.append(["live_note_count", len(notes)])
    if len(cards) != plan["totals"]["cards"]:
        errors.append(["live_card_count", len(cards)])
    if any(card["deckName"] != DECK for card in cards):
        errors.append(["wrong_deck"])
    if any(card["queue"] == -1 for card in cards):
        errors.append(["suspended_cards"])
    red = call("findCards", query=f'deck:"{DECK}" flag:1')
    green = call("findCards", query=f'deck:"{DECK}" flag:3')
    if red:
        errors.append(["red_flags", red])
    if len(green) != plan["totals"]["green_high_yield_cards"]:
        errors.append(["green_count", len(green)])

    # Conteúdo visível: proíbe o antigo rodapé/comentário metalinguístico.
    # Tags técnicas aparecem no contêiner nativo (retrátil) do modelo AnKing;
    # isso não é o antigo comentário metalinguístico inserido no verso do card.
    forbidden = ["Faculdade:", "Step 1:", "High yield:", "Low yield:"]
    for card in cards:
        visible = f'{card.get("question", "")} {card.get("answer", "")}'
        for marker in forbidden:
            if marker in visible:
                errors.append(["visible_meta", card["cardId"], marker])
        if "{{c" in card.get("question", "") or "{{c" in card.get("answer", ""):
            errors.append(["unrendered_cloze", card["cardId"]])

    required_media: set[str] = set()
    for note in notes:
        for field in note["fields"].values():
            for name in re.findall(r'<img[^>]+src=["\x27]([^"\x27]+)', field["value"], re.I):
                decoded = html.unescape(name)
                if not decoded.startswith(("http:", "https:", "data:")):
                    required_media.add(decoded)
    media_dir = Path(plan["profile_evidence"])
    missing_live = sorted(name for name in required_media if not (media_dir / name).exists())
    if missing_live:
        errors.append(["missing_live_media", missing_live])

    package = Path(receipt["package"])
    package_summary = {"files": 0, "media": 0, "notes": None, "cards": None}
    with zipfile.ZipFile(package) as archive:
        names = archive.namelist()
        package_summary["files"] = len(names)
        media = json.loads(archive.read("media"))
        package_summary["media"] = len(media)
        missing_package = sorted(required_media - set(media.values()))
        if missing_package:
            errors.append(["missing_package_media", missing_package])
        db_names = [name for name in names if name.startswith("collection.anki")]
        # collection.anki21b usa o formato novo; o APKG ainda inclui anki2 legível
        # nas versões que suportam a checagem SQLite direta.
        sqlite_name = next((name for name in db_names if name in {"collection.anki2", "collection.anki21"}), None)
        if sqlite_name:
            with tempfile.TemporaryDirectory(prefix="nebli-vascular-check-") as temporary:
                db = Path(temporary) / sqlite_name
                db.write_bytes(archive.read(sqlite_name))
                connection = sqlite3.connect(f"{db.as_uri()}?mode=ro", uri=True)
                package_summary["notes"] = connection.execute("select count(*) from notes").fetchone()[0]
                package_summary["cards"] = connection.execute("select count(*) from cards").fetchone()[0]
                connection.close()
            if package_summary["notes"] != len(notes) or package_summary["cards"] != len(cards):
                errors.append(["package_counts", package_summary])

    by_origin = collections.Counter(
        result["origin"]
        for result in receipt["results"]
        for _ in result["cards"]
    )
    by_objective = collections.Counter(
        result["objective"]
        for result in receipt["results"]
        for _ in result["cards"]
    )
    verification = {
        "status": "failed" if errors else "passed",
        "notes": len(notes),
        "cards": len(cards),
        "cards_by_origin": dict(by_origin),
        "cards_by_objective": dict(by_objective),
        "green_high_yield": len(green),
        "red_improve": len(red),
        "suspended": sum(card["queue"] == -1 for card in cards),
        "authorial": 0,
        "required_media": len(required_media),
        "package": package_summary,
        "errors": errors,
        "limitations": [
            "Nenhuma prova antiga específica desta aula foi localizada na pasta/Drive pesquisado.",
            "Sincronização com AnkiWeb e abertura no Mac/Android não são verificáveis deste Windows.",
        ],
    }
    (ROOT / "verification.json").write_text(
        json.dumps(verification, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(verification, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
