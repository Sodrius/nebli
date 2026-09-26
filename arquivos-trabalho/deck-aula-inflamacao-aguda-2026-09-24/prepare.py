"""Curate the first X2 batch from the current Anki inventory, never old receipts."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
INV = json.loads((HERE / "inventory.json").read_text(encoding="utf-8"))
BY_ID = {n["nid"]: n for n in INV["notes"]}
DECK = "NEBLI::UC03::P2::Patologia::Inflamação aguda"
LESSON = "2026-uc03-patologia-38-inflamacao-aguda"
HY = "#AK_Step1_v12::#Low/HighYield::1-HighYield"

# Chosen by reading live AnKing fronts/Extras against the 43-page teaching PDF.
# The first batch is installed early; visual morphology and local gaps follow.
SELECTED = {
    "definition_triggers": [1487639081947, 1487639986876, 1487639996379],
    "vascular_mediators": [1487640104877, 1487640116450, 1487640128726,
                           1487640236977, 1487640245670, 1487640276680],
    "recruitment": [1487640326189, 1487642457129, 1487642460355, 1487642540692,
                    1487642575587, 1487642584713, 1487642586907, 1487642598269,
                    1487642602159, 1487642611448, 1487642614060, 1487642645625,
                    1487642652400],
    "effectors": [1487640219508, 1487642657848, 1487642661164, 1487642714884,
                  1487642722079, 1487642730357, 1487642786172],
    "morphology": [1487469883647, 1545331567296],
}
PINK = {
    1487642457129: "Slide 16–18; isolated sequence prompt duplicates the full recruitment chain",
    1487642540692: "Slide 16–21; isolated sequence prompt duplicates molecular rolling cards",
    1487642598269: "Slide 21–23; isolated sequence prompt duplicates molecular adhesion cards",
    1487642645625: "Slide 23–28; isolated sequence prompt duplicates transendothelial sequence",
}
EMPTY_EXTRA = {1487642586907, 1487642652400, 1487642722079}
EXTRA_OVERRIDE = {
    1487639081947: '<img src="2345445fb87e2792412cc9ab9675cb4b.webp" width="613">'
                   '<br><small>Photo: Calicut Medical College, CC BY-SA 4.0, via Wikimedia Commons.</small>',
    1487469883647: '<img src="fe5b7ca1ea637da274be316b836f6c7e.webp" width="602">'
                   '<br><small>Photo: Dr Graham Beards, CC BY-SA 3.0, via Wikimedia Commons.</small>',
    1545331567296: 'An abscess is a localized collection of pus.'
                   '<br><small>Photo: Amrith Raj, CC BY-SA 3.0, via Wikimedia Commons.</small>',
}

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()

def main():
    entries = []
    for objective, ids in SELECTED.items():
        for nid in ids:
            n = BY_ID[nid]
            assert n["cards"][0]["deck"].startswith("Referências::Anking Step Deck"), nid
            fields = {name: (n["fields"][name] if name in {"Text", "Extra"} else "")
                      for name in n["fields"]}
            if nid in EMPTY_EXTRA:
                fields["Extra"] = ""
            if nid in EXTRA_OVERRIDE:
                fields["Extra"] = EXTRA_OVERRIDE[nid]
            count = len(set(re.findall(r"\{\{c(\d+)::", fields["Text"])))
            assert count == len(n["cards"]), (nid, count, len(n["cards"]))
            entries.append({"source_nid": nid, "source_deck": n["cards"][0]["deck"],
                            "source_model": n["model"], "source_fields_hash": digest(n["fields"]),
                            "source_tags": n["tags"], "origin": "AnKing", "objective": objective,
                            "fields": fields, "expected_cards": count, "high_yield": HY in n["tags"],
                            "pink": nid in PINK, "pink_reason": PINK.get(nid, "")})
    plan = {"lesson_id": LESSON, "target_deck": DECK, "profile": INV["profile"],
            "source_folder": "https://drive.google.com/drive/folders/1apmeYFBAs8fHkc1wMw7AIsGdHUOtIxT3",
            "source_inventory": "inventory.json", "entries": entries,
            "totals": {"notes": len(entries), "cards": sum(e["expected_cards"] for e in entries),
                       "by_source": {"AnKing": sum(e["expected_cards"] for e in entries)},
                       "pink": sum(e["expected_cards"] for e in entries if e["pink"]),
                       "green": sum(e["expected_cards"] for e in entries if e["high_yield"] and not e["pink"]),
                       "authorial": 0}}
    (HERE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(plan["totals"], ensure_ascii=False))

if __name__ == "__main__":
    main()
