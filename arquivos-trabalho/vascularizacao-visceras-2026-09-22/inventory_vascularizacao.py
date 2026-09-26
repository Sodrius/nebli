"""Inventário somente leitura para a aula de vascularização das vísceras."""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import requests

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent


def call(action, **params):
    response = requests.post(
        "http://127.0.0.1:8765",
        json={"action": action, "version": 6, "params": params},
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    if data["error"]:
        raise RuntimeError(data["error"])
    return data["result"]


QUERIES = {
    "celiac": '"celiac" OR "coeliac" OR "celíac"',
    "gastric": '"gastric artery" OR "gastrica" OR "gástrica"',
    "splenic": '"splenic artery" OR "arteria esplenica" OR "artéria esplênica"',
    "hepatic": '"common hepatic" OR "proper hepatic" OR "gastroduodenal"',
    "pancreaticoduodenal": '"pancreaticoduodenal" OR "pancreatic duodenal" OR "pancreatoduodenal"',
    "gastroepiploic": '"gastroepiploic" OR "gastro-omental" OR "gastroomental" OR "gastromental"',
    "sma": '"superior mesenteric" OR "mesentérica superior" OR "mesenterica superior"',
    "ima": '"inferior mesenteric" OR "mesentérica inferior" OR "mesenterica inferior"',
    "jejunal_ileal": '"jejunal arteries" OR "ileal arteries" OR "vasa recta" OR "arterial arcades"',
    "colic": '"ileocolic" OR "right colic" OR "middle colic" OR "left colic" OR "sigmoid arteries"',
    "marginal": '"marginal artery" OR "artery of Drummond" OR "arc of Riolan"',
    "rectal": '"superior rectal" OR "middle rectal" OR "inferior rectal" OR "rectal vein"',
    "portal": '"portal vein" OR "portal venous" OR "portocaval" OR "porto-systemic"',
    "lymph": '"cisterna chyli" OR "intestinal trunk" OR "preaortic lymph" OR "celiac lymph" OR "mesenteric lymph"',
}


def strip_html(value):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", value or "")).strip()


def main():
    hits = defaultdict(set)
    for label, query in QUERIES.items():
        try:
            ids = call("findNotes", query=query)
        except RuntimeError:
            ids = []
            for term in re.findall(r'"([^"]+)"', query):
                ids.extend(call("findNotes", query=term))
        hits[label].update(ids)
    all_ids = sorted(set().union(*hits.values()))
    notes = call("notesInfo", notes=all_ids)
    cards = call("cardsInfo", cards=[card for note in notes for card in note["cards"]])
    card_by_note = defaultdict(list)
    for card in cards:
        card_by_note[card["note"]].append(card)
    rows = []
    for note in notes:
        fields = {name: field["value"] for name, field in note["fields"].items()}
        searchable = " ".join(strip_html(value) for value in fields.values())
        rows.append({
            "noteId": note["noteId"],
            "modelName": note["modelName"],
            "tags": note["tags"],
            "fields": fields,
            "cards": card_by_note[note["noteId"]],
            "matched_queries": sorted(label for label, ids in hits.items() if note["noteId"] in ids),
            "preview": searchable[:500],
        })
    snapshot = {
        "media_dir": call("getMediaDirPath"),
        "decks": call("deckNames"),
        "models": call("modelNames"),
        "queries": QUERIES,
        "counts_by_query": {label: len(ids) for label, ids in hits.items()},
        "notes": rows,
    }
    (ROOT / "inventory.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "notes": len(rows),
        "cards": len(cards),
        "counts_by_query": snapshot["counts_by_query"],
        "models": sorted({row["modelName"] for row in rows}),
        "decks": sorted({card["deckName"] for card in cards}),
        "media_dir": snapshot["media_dir"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
