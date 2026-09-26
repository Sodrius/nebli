"""Fresh, read-only Anki inventory for UC08 visceral vascularization."""
import json
import re
from pathlib import Path

from urllib.request import Request, urlopen

OUT = Path(__file__).parent
API = "http://127.0.0.1:8765"
TERMS = {
    "celiac": ["celiac", "coeliac", "celíaco"],
    "gastric": ["gastric artery", "gastroepiploic", "gastroomental"],
    "splenic": ["splenic artery", "short gastric"],
    "hepatic": ["common hepatic", "proper hepatic", "gastroduodenal"],
    "pancreaticoduodenal": ["pancreaticoduodenal", "pancreatic duodenal"],
    "mesenteric": ["superior mesenteric", "inferior mesenteric"],
    "jejunal_ileal": ["jejunal artery", "ileal artery", "vasa recta", "arterial arcade"],
    "colic": ["ileocolic", "right colic", "middle colic", "left colic", "sigmoid artery", "marginal artery"],
    "rectal": ["superior rectal", "middle rectal", "inferior rectal", "rectal vein"],
    "portal": ["portal vein", "splenic vein", "mesenteric vein"],
    "lymph": ["cisterna chyli", "intestinal trunk", "celiac lymph", "mesenteric lymph", "rectal lymph"],
}


def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    request = Request(API, data=payload, headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=90) as resp:
        data = json.load(resp)
    if data.get("error"):
        raise RuntimeError(f"{action}: {data['error']}")
    return data["result"]


def main():
    found = {}
    query_counts = {}
    for group, terms in TERMS.items():
        for term in terms:
            query = f'"{term}"'
            ids = call("findNotes", query=query)
            query_counts[f"{group}:{term}"] = len(ids)
            for nid in ids:
                found.setdefault(nid, set()).add(group)
    rows = []
    for i in range(0, len(found), 100):
        ids = list(found)[i:i+100]
        for note in call("notesInfo", notes=ids):
            fields = {k: v["value"] for k, v in note["fields"].items()}
            plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", " ".join(fields.values())))
            rows.append({"nid": note["noteId"], "model": note["modelName"], "tags": note["tags"], "fields": fields, "cards": note["cards"], "groups": sorted(found[note["noteId"]]), "preview": plain[:450]})
    card_ids = [cid for row in rows for cid in row["cards"]]
    cards = []
    for i in range(0, len(card_ids), 100):
        cards.extend(call("cardsInfo", cards=card_ids[i:i+100]))
    by_nid = {}
    for card in cards:
        by_nid.setdefault(card["note"], []).append({"cid": card["cardId"], "deck": card["deckName"], "ord": card["ord"], "queue": card["queue"], "flags": card["flags"]})
    for row in rows:
        row["cards"] = by_nid.get(row["nid"], [])
    output = {"profile": call("getActiveProfile"), "queries": query_counts, "notes": rows}
    (OUT / "inventory.json").write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    from collections import Counter
    corpora = Counter(card["deckName"].split("::")[0] for card in cards)
    print(json.dumps({"notes": len(rows), "cards": len(cards), "corpora": corpora, "queries": query_counts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
