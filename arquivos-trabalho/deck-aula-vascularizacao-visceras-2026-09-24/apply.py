"""Apply and verify the reviewed X1 plan without touching source notes/models."""
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).parent
ROOT = HERE.parent
PLAN = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
LOCK = ROOT / "ANKI-ESCRITA.lock"
TAG = f'NEBLI::{PLAN["lesson_id"]}'
MODEL_NAMES = {
    "AnKingOverhaul (AnKing Step Deck / AnKingMed)": "NEBLI UC08 Visceral AnKing v1",
    "Anatomy": "NEBLI UC08 Visceral Anatomy v1",
    "Cloze deletion": "NEBLI UC08 Visceral Dope Cloze v1",
    "Cloze-b12d6": "NEBLI UC08 Visceral Dorian Cloze v1",
}

def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    with urlopen(Request("http://127.0.0.1:8765", data=payload,
                         headers={"Content-Type": "application/json"}), timeout=120) as res:
        value = json.load(res)
    if value["error"]:
        raise RuntimeError(f"{action}: {value['error']}")
    return value["result"]

def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()

def identity(entry):
    return (f'NEBLI::source::nid-{entry["source_nid"]}' if entry["source_nid"]
            else f'NEBLI::authored::{entry["key"]}')

def snapshot_sources():
    ids = [e["source_nid"] for e in PLAN["entries"] if e["source_nid"]]
    return {x["noteId"]: x for x in call("notesInfo", notes=ids)}

def check():
    if call("getActiveProfile") != PLAN["profile"]:
        raise RuntimeError("Active profile changed")
    sources = snapshot_sources()
    for entry in PLAN["entries"]:
        nid = entry["source_nid"]
        if nid and (nid not in sources or digest({k: v["value"] for k, v in sources[nid]["fields"].items()}) != entry["source_fields_hash"]):
            raise RuntimeError(f"Source changed or missing: {nid}")
        found = call("findNotes", query=f'tag:"{identity(entry)}"')
        if found:
            raise RuntimeError(f"NEBLI identity already exists: {identity(entry)} -> {found}")
    if call("findCards", query=f'deck:"{PLAN["target_deck"]}"'):
        raise RuntimeError("Target deck contains cards; reconcile before applying")
    media = Path(call("getMediaDirPath"))
    for name in ["MSA-Arteries_of_Posterior_Abdominal_Wall16.jpg",
                 "MSA-Arteries_of_Stomach_Liver_and_Spleen14.jpg",
                 "MSA-Arteries_of_Large_Intestine15.jpg",
                 "MSA-Hepatic_Portal_Vein_Tributaries-Portocaval_Anastomoses19.jpg",
                 "MSA-Veins_of_Rectum_and_Anal_Canal14.jpg",
                 "MSA-Arteries_of_Female_Pelvis12.jpg"]:
        if not (media / name).is_file():
            raise RuntimeError(f"Missing atlas image: {name}")
    return sources

def clone_model(source_name):
    name = MODEL_NAMES[source_name]
    fields = call("modelFieldNames", modelName=source_name)
    templates = copy.deepcopy(call("modelTemplates", modelName=source_name))
    css = call("modelStyling", modelName=source_name)["css"]
    if source_name == "Anatomy":
        templates["1"]["Front"] = (
            '{{#1a}}<span id=title>[{{Title}}]</span><br><br>'
            '<span id=question>What is being shown here at "1"?</span><br><br>'
            '{{OccludedImage}}{{/1a}}'
        )
    if name not in call("modelNames"):
        call("createModel", modelName=name, inOrderFields=fields, css=css,
             isCloze=source_name != "Anatomy",
             cardTemplates=[{"Name": k, **v} for k, v in templates.items()])
    if call("modelFieldNames", modelName=name) != fields or call("modelTemplates", modelName=name) != templates:
        raise RuntimeError(f"Clone model differs: {name}")
    return name

def apply():
    with LOCK.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps({"executor": "Codex", "lesson": PLAN["lesson_id"],
                                 "at": datetime.now(timezone.utc).isoformat()}))
    journal = HERE / "journal.jsonl"
    try:
        sources = check()
        save("before-apply.json", {"at": datetime.now(timezone.utc).isoformat(),
                                   "profile": PLAN["profile"], "source_notes": list(sources.values()),
                                   "target_cards": [], "selected": PLAN["totals"]})
        call("createDeck", deck=PLAN["target_deck"])
        models = {name: clone_model(name) for name in sorted({e["source_model"] for e in PLAN["entries"]})}
        created = []
        for entry in PLAN["entries"]:
            fields = entry["fields"]
            tags = list(dict.fromkeys(entry["source_tags"] + [TAG, identity(entry),
                                                                f'NEBLI::origem::{entry["origin"].replace(" ", "-")}']))
            note_id = call("addNote", note={"deckName": PLAN["target_deck"],
                                             "modelName": models[entry["source_model"]],
                                             "fields": fields, "tags": tags,
                                             "options": {"allowDuplicate": True}})
            if not note_id:
                raise RuntimeError(f"Failed to add: {identity(entry)}")
            note = call("notesInfo", notes=[note_id])[0]
            cards = call("cardsInfo", cards=note["cards"])
            if len(cards) != entry["expected_cards"]:
                raise RuntimeError(f"Unexpected card count on {identity(entry)}: {len(cards)}")
            other_deck = [c for c in cards if c["deckName"] != PLAN["target_deck"]]
            if other_deck:
                if any(c["reps"] for c in other_deck):
                    raise RuntimeError("Reviewed card in wrong deck")
                call("changeDeck", cards=[c["cardId"] for c in other_deck], deck=PLAN["target_deck"])
                cards = call("cardsInfo", cards=note["cards"])
            flag = 5 if entry["pink"] else (3 if entry["high_yield"] else 0)
            for card in cards:
                if flag:
                    call("setSpecificValueOfCard", card=card["cardId"],
                         keys=["flags"], newValues=[flag], warning_check=True)
            row = {"identity": identity(entry), "source_nid": entry["source_nid"],
                   "note_id": note_id, "card_ids": [c["cardId"] for c in cards],
                   "flag": flag, "origin": entry["origin"]}
            created.append(row)
            with journal.open("a", encoding="utf-8") as stream:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        save("receipt.json", {"created": created, "totals": PLAN["totals"],
                              "profile": PLAN["profile"], "deck": PLAN["target_deck"]})
    finally:
        LOCK.unlink(missing_ok=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2 or sys.argv[1] not in {"check", "apply"}:
        raise SystemExit("usage: apply.py check|apply")
    if sys.argv[1] == "check":
        check()
        print(json.dumps(PLAN["totals"], ensure_ascii=False))
    else:
        apply()
        print("Applied", PLAN["totals"])
