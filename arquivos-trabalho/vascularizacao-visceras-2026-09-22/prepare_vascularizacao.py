"""Prepara o plano auditável do deck, sem escrever no Anki."""
import hashlib
import json
import re
from pathlib import Path

from inventory_vascularizacao import call

ROOT = Path(__file__).resolve().parent
LESSON = "2026-uc08-anatomia-07-vascularizacao-das-visceras"
DECK = "NEBLI::UC08::Anatomia::Vascularização das vísceras"
HY_TAG = "#AK_Step1_v12::#Low/HighYield::1-HighYield"

ANKING = [
    1486767263733, 1486767276770, 1486767287058, 1486767295417,
    1486767304293, 1486767314237, 1486767323251, 1486767327881,
    1486767330571, 1486767333068, 1486767335503, 1486767337959,
    1486767341284, 1486767346792, 1486767349883, 1486767352903,
    1486767364212, 1486767367274, 1486767395683,
    1486771299461, 1486771343412, 1486771346144, 1486771359798,
    1486771372707, 1486771374861, 1486771390217,
    1486945231564, 1486945235222, 1486945239368, 1486945243332,
    1486945247167, 1486945252224, 1521079313083,
]

EXTERNAL_CLOZE = [
    1461962333435,  # jejunum: few arcades, long vasa recta
    1461962581720,  # inferior pancreaticoduodenal from SMA
    1461962601941,  # ileocolic/right/middle colic from SMA
    1461962631680,  # left colic/sigmoid/superior rectal from IMA
    1461966031438,  # cisterna chyli
    1527683179954,  # portal vein formation
]

ANATOMY_FIELDS = {
    1349477488373: ["2a", "10a", "11a", "13a"],
    1349477488376: ["2a", "3a", "5a", "6a", "7a", "8a", "9a", "10a", "11a", "12a"],
    1349477488369: [f"{index}a" for index in range(1, 13)],
    1349477488443: ["2a", "3a", "4a", "12a", "13a", "14a"],
    1349477488690: ["5a", "6a", "8a", "10a", "12a"],
}


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def fields_plain(note):
    return {name: field["value"] for name, field in note["fields"].items()}


def clozes(text):
    return sorted({int(value) for value in re.findall(r"\{\{c(\d+)::", text)})


def objective_for(note_id):
    if note_id in ANATOMY_FIELDS:
        return {
            1349477488373: "overview-major-unpaired-arteries",
            1349477488376: "celiac-and-stomach-identification",
            1349477488369: "mesenteric-branches-identification",
            1349477488443: "portal-tributaries-identification",
            1349477488690: "rectal-venous-identification",
        }[note_id]
    if note_id in {1486945231564, 1486945235222, 1486945239368, 1486945243332, 1486945247167, 1486945252224, 1461966031438}:
        return "lymphatic-drainage"
    if note_id in {1486771299461, 1486771343412, 1486771346144, 1486771359798, 1486771372707, 1486771374861, 1486771390217}:
        return "rectal-supply-and-drainage"
    if note_id in {1527683179954}:
        return "portal-vein-formation"
    if note_id in {1461962333435}:
        return "jejunal-vs-ileal-vessels"
    if note_id in {1461962581720, 1521079313083}:
        return "pancreaticoduodenal-anastomosis"
    if note_id in {1461962601941, 1461962631680}:
        return "mesenteric-branch-trees"
    return "celiac-and-gastric-branch-trees"


def main():
    ids = ANKING + EXTERNAL_CLOZE + list(ANATOMY_FIELDS)
    notes = {note["noteId"]: note for note in call("notesInfo", notes=ids)}
    missing = sorted(set(ids) - set(notes))
    if missing:
        raise RuntimeError(f"Fontes ausentes: {missing}")
    entries = []
    for note_id in ids:
        source = notes[note_id]
        fields = fields_plain(source)
        if note_id in ANATOMY_FIELDS:
            selected = set(ANATOMY_FIELDS[note_id])
            for name in [f"{index}a" for index in range(1, 21)]:
                if name not in selected:
                    fields[name] = ""
            expected_cards = len(selected)
            origin = "Dope Anatomy"
            selected_fields = sorted(selected, key=lambda x: int(x[:-1]))
        else:
            expected_cards = len(clozes(fields.get("Text", "")))
            if not expected_cards:
                raise RuntimeError(f"Fonte cloze sem cloze: {note_id}")
            origin = "AnKing" if note_id in ANKING else ("Dorian" if note_id == 1527683179954 else "Dope Anatomy")
            selected_fields = []
        entries.append({
            "key": f"source-{note_id}",
            "source_nid": note_id,
            "source_model": source["modelName"],
            "source_tags": source["tags"],
            "source_fields_hash": digest(source["fields"]),
            "fields": fields,
            "origin": origin,
            "objective": objective_for(note_id),
            "selected_fields": selected_fields,
            "expected_cards": expected_cards,
            "high_yield": HY_TAG in source["tags"],
        })
    duplicates = {
        entry["source_nid"]: call("findNotes", query=f'tag:"NEBLI::source::nid-{entry["source_nid"]}"')
        for entry in entries
    }
    collisions = {nid: found for nid, found in duplicates.items() if found}
    if collisions:
        raise RuntimeError(f"Cópias NEBLI já existem e exigem associação, não duplicação: {collisions}")
    plan = {
        "lesson_id": LESSON,
        "target_deck": DECK,
        "profile_evidence": call("getMediaDirPath"),
        "source_folder": "https://drive.google.com/drive/folders/1anr09zp44SG100cQsQ-4jMVk6b0rcM2W",
        "source_files": [
            "https://drive.google.com/file/d/11av61qam0wT32PMSpF-ccJU01bQxkkTe/view",
            "https://drive.google.com/file/d/1BcxSlwtGAinTf0zl9pM0L6gF4bn2VOF8/view",
            "https://drive.google.com/file/d/1eMVHceE-oNvdZWDoxkEBKROSBV1bzuX5/view",
        ],
        "entries": entries,
        "totals": {
            "notes": len(entries),
            "cards": sum(entry["expected_cards"] for entry in entries),
            "AnKing_cards": sum(entry["expected_cards"] for entry in entries if entry["origin"] == "AnKing"),
            "Dope_Anatomy_cards": sum(entry["expected_cards"] for entry in entries if entry["origin"] == "Dope Anatomy"),
            "Dorian_cards": sum(entry["expected_cards"] for entry in entries if entry["origin"] == "Dorian"),
            "authored_cards": 0,
            "green_high_yield_cards": sum(entry["expected_cards"] for entry in entries if entry["high_yield"]),
        },
        "flags": {"red": "improve", "green": "explicit AnKing 1-HighYield"},
        "scope_rule": "content taught/required, not every example; no recursive prerequisite expansion",
    }
    (ROOT / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(plan["totals"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
