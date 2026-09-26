"""Read-only cross-deck duplicate audit from the live NEBLI collection."""
import html
import json
import re
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

from apply import call, HERE


def clean(value):
    value = re.sub(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", r"\1", value, flags=re.I | re.S)
    value = re.sub(r"<img[^>]*>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value).lower()
    return " ".join(re.findall(r"[\wÀ-ÿ]+", value, flags=re.U))


def main():
    ids = call("findNotes", query="deck:NEBLI")
    notes = []
    for start in range(0, len(ids), 200):
        notes.extend(call("notesInfo", notes=ids[start:start + 200]))
    x2_tag = "NEBLI::2026-uc03-patologia-38-inflamacao-aguda"
    rows = []
    by_source = defaultdict(list)
    for n in notes:
        fields = n["fields"]
        source = [t for t in n["tags"] if t.startswith("NEBLI::source::")]
        for tag in source:
            by_source[tag].append(n["noteId"])
        primary = next((fields[k]["value"] for k in ("Text", "Front", "Question", "Pergunta", "1a") if k in fields), "")
        row = {"nid": n["noteId"], "deck": n["cards"][0] if n["cards"] else None,
               "model": n["modelName"], "x2": x2_tag in n["tags"],
               "source": source, "text": clean(primary)[:600]}
        rows.append(row)
    card_ids = [n["cards"][0] for n in notes if n["cards"]]
    cardinfo = []
    for start in range(0, len(card_ids), 200):
        cardinfo.extend(call("cardsInfo", cards=card_ids[start:start + 200]))
    deck_by_card = {c["cardId"]: c["deckName"] for c in cardinfo}
    for row in rows:
        row["deck"] = deck_by_card.get(row["deck"], "")
    exact_source = [{"source": source, "notes": matches} for source, matches in by_source.items() if len(matches) > 1]
    by_text = defaultdict(list)
    for row in rows:
        if len(row["text"]) >= 20:
            by_text[row["text"]].append(row)
    exact_question = [{"text": value, "notes": [{"nid": x["nid"], "deck": x["deck"]} for x in matches]}
                      for value, matches in by_text.items() if len({x["deck"] for x in matches}) > 1]
    x2 = [r for r in rows if r["x2"]]
    other = [r for r in rows if not r["x2"]]
    near = []
    for a in x2:
        ta = set(a["text"].split())
        if len(ta) < 4:
            continue
        for b in other:
            tb = set(b["text"].split())
            if len(tb) < 4:
                continue
            overlap = len(ta & tb) / len(ta | tb)
            if overlap < .45:
                continue
            ratio = SequenceMatcher(None, a["text"], b["text"]).ratio()
            if overlap >= .62 or ratio >= .78:
                near.append({"x2_nid": a["nid"], "other_nid": b["nid"], "other_deck": b["deck"],
                             "jaccard": round(overlap, 3), "sequence": round(ratio, 3),
                             "x2": a["text"], "other": b["text"]})
    result = {"notes_scanned": len(rows), "decks_scanned": sorted({x["deck"] for x in rows}),
              "x2_notes": len(x2), "exact_source": exact_source, "exact_question_cross_deck": exact_question,
              "near_x2_other": sorted(near, key=lambda x: max(x["jaccard"], x["sequence"]), reverse=True)}
    (HERE / "duplicate-audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v if k in ("notes_scanned", "x2_notes") else len(v)
                      for k, v in result.items()}, ensure_ascii=False))
    print(json.dumps(result["near_x2_other"][:25], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
