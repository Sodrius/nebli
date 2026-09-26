"""Materializa o plano auditado no Anki sem alterar as notas-fonte.

Uso:
    python apply_vascularizacao.py check
    python apply_vascularizacao.py apply
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from inventory_vascularizacao import call
from prepare_vascularizacao import DECK, LESSON, ROOT, digest


TAG = f"NEBLI::{LESSON}"
MODEL_NAMES = {
    "AnKingOverhaul (AnKing Step Deck / AnKingMed)": "NEBLI AnKing independente - v3",
    "Anatomy": "NEBLI Anatomy independente - v1",
    "Cloze deletion": "NEBLI Dope Cloze independente - v1",
    "Cloze-b12d6": "NEBLI Dorian Cloze independente - v1",
}
CLOZE_MODELS = {
    "AnKingOverhaul (AnKing Step Deck / AnKingMed)",
    "Cloze deletion",
    "Cloze-b12d6",
}


def save(name: str, value: object) -> None:
    (ROOT / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def identity(entry: dict) -> str:
    return f'NEBLI::source::nid-{entry["source_nid"]}'


def note_plain(note: dict) -> dict[str, str]:
    return {name: value["value"] for name, value in note["fields"].items()}


def source_snapshot(plan: dict) -> dict[int, dict]:
    ids = [entry["source_nid"] for entry in plan["entries"]]
    return {note["noteId"]: note for note in call("notesInfo", notes=ids)}


def model_snapshot(plan: dict) -> dict[str, dict]:
    names = sorted({entry["source_model"] for entry in plan["entries"]})
    return {
        name: {
            "fields": call("modelFieldNames", modelName=name),
            "templates": call("modelTemplates", modelName=name),
            "styling": call("modelStyling", modelName=name),
        }
        for name in names
    }


def preflight(plan: dict) -> dict:
    problems: list[str] = []
    if call("getMediaDirPath") != plan["profile_evidence"]:
        problems.append("O perfil ativo do Anki mudou.")
    if DECK != plan["target_deck"] or LESSON != plan["lesson_id"]:
        problems.append("Constantes e plano não correspondem.")
    if len({entry["key"] for entry in plan["entries"]}) != len(plan["entries"]):
        problems.append("Há chaves repetidas no plano.")

    sources = source_snapshot(plan)
    for entry in plan["entries"]:
        source = sources.get(entry["source_nid"])
        if source is None:
            problems.append(f'Fonte ausente: {entry["source_nid"]}')
            continue
        if digest(source["fields"]) != entry["source_fields_hash"]:
            problems.append(f'Campos da fonte mudaram: {entry["source_nid"]}')
        found = call("findNotes", query=f'tag:"{identity(entry)}"')
        if found:
            problems.append(f'Cópia NEBLI já existe para {entry["source_nid"]}: {found}')

    existing_target = call("findCards", query=f'deck:"{DECK}"')
    if existing_target:
        problems.append(f'O deck-alvo já contém {len(existing_target)} cards.')
    if problems:
        raise RuntimeError("\n".join(problems))
    return {
        "status": "ok",
        "notes": plan["totals"]["notes"],
        "cards": plan["totals"]["cards"],
        "authored_cards": plan["totals"]["authored_cards"],
        "green_cards": plan["totals"]["green_high_yield_cards"],
        "profile": plan["profile_evidence"],
    }


def ensure_clone_model(source_name: str) -> str:
    target_name = MODEL_NAMES[source_name]
    fields = call("modelFieldNames", modelName=source_name)
    templates = copy.deepcopy(call("modelTemplates", modelName=source_name))
    styling = call("modelStyling", modelName=source_name)
    if source_name == "Anatomy":
        # O template original gera um card 1 vazio sempre que o campo 2a existe.
        # A cópia NEBLI independente corrige apenas esse defeito do template;
        # a fonte Dope e os demais templates permanecem intocados.
        templates["1"]["Front"] = """{{#1a}}
<span id=title>[{{Title}}]</span><br><br>
<span id=question>What is being shown here at \"1\"?</span><br><br>
{{OccludedImage}}
{{/1a}}"""
    if target_name not in call("modelNames"):
        call(
            "createModel",
            modelName=target_name,
            inOrderFields=fields,
            css=styling["css"],
            isCloze=source_name in CLOZE_MODELS,
            cardTemplates=[{"Name": name, **template} for name, template in templates.items()],
        )
    elif call("modelTemplates", modelName=target_name) != templates:
        call("updateModelTemplates", model={"name": target_name, "templates": templates})
    if call("modelFieldNames", modelName=target_name) != fields:
        raise RuntimeError(f"Campos divergentes no modelo clonado: {target_name}")
    if call("modelTemplates", modelName=target_name) != templates:
        raise RuntimeError(f"Templates divergentes no modelo clonado: {target_name}")
    if call("modelStyling", modelName=target_name)["css"] != styling["css"]:
        raise RuntimeError(f"CSS divergente no modelo clonado: {target_name}")
    return target_name


def apply(plan: dict) -> None:
    lock = ROOT / "apply.lock"
    with lock.open("x", encoding="utf-8") as handle:
        handle.write(datetime.now(timezone.utc).isoformat())

    journal = ROOT / "journal.jsonl"

    def log(action: str, result: object) -> None:
        with journal.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {
                        "at": datetime.now(timezone.utc).isoformat(),
                        "action": action,
                        "result": result,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    try:
        preflight_result = preflight(plan)
        original_notes = source_snapshot(plan)
        original_models = model_snapshot(plan)
        snapshot = {
            "at": datetime.now(timezone.utc).isoformat(),
            "preflight": preflight_result,
            "notes": list(original_notes.values()),
            "models": original_models,
            "target_cards_before": call("findCards", query=f'deck:"{DECK}"'),
        }
        save("before-apply.json", snapshot)
        log("snapshot", {"notes": len(original_notes), "models": len(original_models)})

        call("createDeck", deck=DECK)
        cloned_models = {
            source_name: ensure_clone_model(source_name)
            for source_name in sorted(original_models)
        }

        results = []
        green_cards: list[int] = []
        for entry in plan["entries"]:
            model = cloned_models[entry["source_model"]]
            model_fields = call("modelFieldNames", modelName=model)
            fields = {name: "" for name in model_fields}
            fields.update(entry["fields"])
            if "ankihub_id" in fields:
                fields["ankihub_id"] = ""
            tags = list(
                dict.fromkeys(
                    entry["source_tags"]
                    + [
                        TAG,
                        identity(entry),
                        f'NEBLI::objetivo::{entry["objective"]}',
                        f'NEBLI::origem::{entry["origin"].replace(" ", "-")}',
                    ]
                )
            )
            log("before-add", {"key": entry["key"], "model": model})
            note_id = call(
                "addNote",
                note={
                    "deckName": DECK,
                    "modelName": model,
                    "fields": fields,
                    "tags": tags,
                    "options": {"allowDuplicate": True},
                },
            )
            if not note_id:
                raise RuntimeError(f'Falha ao criar {entry["key"]}')
            note = call("notesInfo", notes=[note_id])[0]
            if note_plain(note) != fields:
                raise RuntimeError(f'Campos divergentes após criação: {entry["key"]}')
            cards = call("cardsInfo", cards=note["cards"])
            if len(cards) != entry["expected_cards"]:
                raise RuntimeError(
                    f'Número de cards inesperado em {entry["key"]}: '
                    f'{len(cards)} != {entry["expected_cards"]}'
                )
            misplaced = [card for card in cards if card["deckName"] != DECK]
            if misplaced:
                if any(card["reps"] != 0 for card in misplaced):
                    raise RuntimeError(f'Card revisado fora do deck: {entry["key"]}')
                call("changeDeck", cards=[card["cardId"] for card in misplaced], deck=DECK)
                cards = call("cardsInfo", cards=note["cards"])
            if any(card["deckName"] != DECK for card in cards):
                raise RuntimeError(f'Cards permanecem fora do deck: {entry["key"]}')
            card_ids = [card["cardId"] for card in cards]
            if entry["high_yield"]:
                green_cards.extend(card_ids)
            result = {
                "key": entry["key"],
                "source_nid": entry["source_nid"],
                "new_nid": note_id,
                "origin": entry["origin"],
                "objective": entry["objective"],
                "cards": card_ids,
                "high_yield": entry["high_yield"],
            }
            results.append(result)
            log("created", result)

        for card_id in green_cards:
            call(
                "setSpecificValueOfCard",
                card=card_id,
                keys=["flags"],
                newValues=[3],
                warning_check=True,
            )

        # Pós-condições na coleção viva.
        all_cards = call("findCards", query=f'deck:"{DECK}"')
        if len(all_cards) != plan["totals"]["cards"]:
            raise RuntimeError(f"Total final incorreto: {len(all_cards)}")
        if call("findCards", query=f'deck:"{DECK}" is:suspended'):
            raise RuntimeError("Há cards suspensos no deck recém-criado.")
        red = call("findCards", query=f'deck:"{DECK}" flag:1')
        green = call("findCards", query=f'deck:"{DECK}" flag:3')
        if red:
            raise RuntimeError(f"Há cards vermelhos inesperados: {red}")
        if set(green) != set(green_cards):
            raise RuntimeError("As bandeiras verdes não correspondem ao plano.")

        # As fontes e seus modelos devem permanecer byte-a-byte equivalentes no readback.
        current_sources = source_snapshot(plan)
        for note_id, original in original_notes.items():
            current = current_sources[note_id]
            if current["fields"] != original["fields"] or current["tags"] != original["tags"]:
                raise RuntimeError(f"A fonte {note_id} foi alterada.")
        if model_snapshot(plan) != original_models:
            raise RuntimeError("Um modelo-fonte foi alterado.")

        package = ROOT / "Vascularizacao das visceras.apkg"
        if not call("exportPackage", deck=DECK, path=str(package.resolve()), includeSched=True):
            raise RuntimeError("Falha ao exportar o APKG.")
        receipt = {
            "at": datetime.now(timezone.utc).isoformat(),
            "lesson_id": LESSON,
            "deck": DECK,
            "plan_hash": digest(plan),
            "notes": len(results),
            "cards": len(all_cards),
            "cards_by_origin": plan["totals"],
            "green_high_yield_cards": len(green),
            "red_improve_cards": len(red),
            "suspended_cards": 0,
            "authorial_cards": 0,
            "source_notes_and_models_unchanged": True,
            "package": str(package.resolve()),
            "package_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
            "results": results,
        }
        save("receipt.json", receipt)
        log("complete", {key: value for key, value in receipt.items() if key != "results"})
        print(
            json.dumps(
                {key: value for key, value in receipt.items() if key != "results"},
                ensure_ascii=False,
                indent=2,
            )
        )
    finally:
        lock.unlink(missing_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["check", "apply"])
    arguments = parser.parse_args()
    active_plan = json.loads((ROOT / "plan.json").read_text(encoding="utf-8"))
    if arguments.mode == "check":
        print(json.dumps(preflight(active_plan), ensure_ascii=False, indent=2))
    else:
        apply(active_plan)
