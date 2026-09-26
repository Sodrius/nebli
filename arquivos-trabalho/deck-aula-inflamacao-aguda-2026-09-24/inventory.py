"""Fresh read-only candidate inventory for UC03 X2."""
import json
from collections import defaultdict
from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).parent
QUERIES = [
    "acute inflammation", "cardinal signs", "exudate", "transudate", "vascular permeability",
    "vasodilation", "stasis", "endothelial contraction", "endothelial injury", "transcytosis",
    "histamine", "PAF", "leukotriene", "neutrophil", "margination", "rolling", "selectin",
    "sialyl lewis", "integrin", "ICAM", "VCAM", "PECAM", "diapedesis", "chemotaxis",
    "C5a", "IL-8", "TNF", "IL-1", "lymphangitis", "phagocytosis", "opsonization",
    "abscess", "phlegmon", "ulcer", "suppurative", "serous inflammation", "fibrinous inflammation",
    "inflammation resolution", "lipoxin", "nitric oxide", "exsudato", "flegmão",
]
CORPORA = ["Referências::Anking Step Deck", "Referências::Referências Externas"]

def call(action, **params):
    data = json.dumps({"action": action, "version": 6, "params": params}).encode()
    with urlopen(Request("http://127.0.0.1:8765", data=data,
                         headers={"Content-Type": "application/json"}), timeout=120) as res:
        value = json.load(res)
    if value["error"]:
        raise RuntimeError(value["error"])
    return value["result"]

def batches(items, n=100):
    for i in range(0, len(items), n):
        yield items[i:i+n]

def main():
    results = defaultdict(set)
    for corpus in CORPORA:
        for term in QUERIES:
            query = f'deck:"{corpus}" "{term}"'
            results[corpus].update(call("findNotes", query=query))
    ids = sorted(set.union(*map(set, results.values())))
    notes = [x for group in batches(ids) for x in call("notesInfo", notes=group)]
    card_ids = [cid for n in notes for cid in n["cards"]]
    cards = {c["cardId"]: c for group in batches(card_ids) for c in call("cardsInfo", cards=group)}
    out = {"profile": call("getActiveProfile"), "queries": QUERIES,
           "corpora": {key: len(value) for key, value in results.items()},
           "notes": [{"nid": n["noteId"], "model": n["modelName"],
                      "fields": {k: v["value"] for k, v in n["fields"].items()},
                      "tags": n["tags"], "cards": [{"cid": cid, "deck": cards[cid]["deckName"],
                      "flags": cards[cid]["flags"], "queue": cards[cid]["queue"]} for cid in n["cards"]]}
                     for n in notes]}
    (HERE / "inventory.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"profile": out["profile"], "corpora": out["corpora"],
                      "notes": len(notes), "cards": len(card_ids)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
