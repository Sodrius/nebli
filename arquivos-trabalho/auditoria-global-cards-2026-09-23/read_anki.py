"""Read-only snapshot of the four medical NEBLI decks via AnkiConnect."""
import json
import urllib.request
from pathlib import Path


def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    request = urllib.request.Request(
        "http://127.0.0.1:8765", payload, {"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    if data["error"]:
        raise RuntimeError(data["error"])
    return data["result"]


queries = {
    "inflamacao": "deck:NEBLI::UC03::P2::Patologia*",
    "complemento": "deck:NEBLI::UC03::P2::Imunologia*",
    "vascularizacao": "deck:NEBLI::UC08::Anatomia*",
    "intestinos": "deck:NEBLI::UC08::Biologia*",
}
snapshot = {}
for name, query in queries.items():
    card_ids = call("findCards", query=query)
    cards = call("cardsInfo", cards=card_ids)
    note_ids = list(dict.fromkeys(card["note"] for card in cards))
    notes = call("notesInfo", notes=note_ids)
    snapshot[name] = {"cards": cards, "notes": notes}

Path(__file__).with_name("snapshot.json").write_text(
    json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8"
)
print({name: (len(item["notes"]), len(item["cards"])) for name, item in snapshot.items()})
