"""Diagnóstico portátil, somente leitura no Anki; não gera/aprova decks."""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

READ_ACTIONS = frozenset({
    "version", "getActiveProfile", "deckNames", "findCards", "cardsInfo",
    "notesInfo", "modelFieldNames", "modelTemplates", "modelNames",
})
FLAGS = {1: "melhorar", 2: "comentario_pendente", 3: "high_yield", 5: "candidato_suspensao_pos_prova"}
CORPORA = {
    "AnKing Step Deck": "mecanismos, relações e Step pertinente",
    "Referências Externas::Dope Anatomy": "relações anatômicas e pranchas",
    "Referências Externas::100 Concepts (Dorian)": "relações anatômicas",
    "Referências Externas::Histology": "histologia",
    "Referências Externas::LLU Histology": "reconhecimento histológico",
    "Referências Externas::University of Michigan - BlueLink Atlas": "anatomia visual",
}


class ReadOnlyAnki:
    def __init__(self, endpoint="http://127.0.0.1:8765"):
        self.endpoint = endpoint

    def __call__(self, action, **params):
        if action not in READ_ACTIONS:
            raise ValueError(f"Ação proibida no diagnóstico: {action}")
        body = json.dumps({"action": action, "version": 6, "params": params}).encode()
        req = urllib.request.Request(self.endpoint, body, {"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as response:
            data = json.load(response)
        if data.get("error"):
            raise RuntimeError(f"{action}: {data['error']}")
        return data["result"]


def deck_query(name):
    return 'deck:"' + name.replace("\\", "\\\\").replace('"', '\\"') + '"'


def chunks(values, size=100):
    for offset in range(0, len(values), size):
        yield values[offset:offset + size]


def discover_corpora(decks):
    """Descobre acervos por segmento, mesmo após mudança de pasta-pai."""
    found = {}
    for deck in decks:
        parts = deck.split("::")
        if "Referências Externas" in parts:
            pos = parts.index("Referências Externas")
            if len(parts) > pos + 1:
                root = "::".join(parts[:pos + 2])
                name = parts[pos + 1]
                found[root] = CORPORA.get("Referências Externas::" + name,
                    "acervo externo: classificar adequação antes de selecionar")
        elif parts[-1] == "AnKing Step Deck":
            found[deck] = CORPORA["AnKing Step Deck"]
    return dict(sorted(found.items(), key=lambda item: ("Referências Externas" in item[0], item[0])))


def collect(call, catalog=False):
    report = {"schema_version": 1, "at": datetime.now(timezone.utc).isoformat(),
              "status": "observed", "errors": [], "read_only_anki": True,
              "drive": "verificar no conector deste executor; não testado por este script",
              "sync": "não testado", "semantic_quality": "não auditada"}
    report["version"] = call("version")
    try:
        report["profile"] = call("getActiveProfile")
    except Exception as error:
        report["profile"] = None
        report["errors"].append(str(error))
    decks = call("deckNames")
    report["corpora"] = []
    model_names = set()
    discovered = discover_corpora(decks)
    all_models = call("modelNames") if catalog else []
    report["discovery"] = {"mode": "live_deck_tree", "decks": decks,
                           "full_structural_catalog_requested": catalog}
    for deck, use in discovered.items():
        exists = any(d == deck or d.startswith(deck + "::") for d in decks)
        ids = call("findCards", query=deck_query(deck)) if exists else []
        # Amostra estrutural apenas; cada candidato escolhido exige leitura integral.
        sample_ids = sorted(set(ids[:3] + ids[-3:]))
        sample = call("cardsInfo", cards=sample_ids) if sample_ids else []
        models = sorted({c["modelName"] for c in sample})
        model_names.update(models)
        entry = {"deck": deck, "use": use, "cards": len(ids),
                                  "available": bool(ids), "query": deck_query(deck),
                                  "sample_card_ids": sample_ids, "sample_models": models,
                                  "model_inventory_complete": False}
        if catalog:
            entry["subdecks"] = {d: len(call("findCards", query=deck_query(d)))
                                  for d in decks if d.startswith(deck + "::")}
            entry["models"] = []
            covered = set()
            for model in all_models:
                query = deck_query(deck) + " " + deck_query(model).replace("deck:", "note:", 1)
                matches = set(call("findCards", query=query)).intersection(ids)
                if not matches:
                    continue
                covered.update(matches)
                model_names.add(model)
                samples = call("cardsInfo", cards=sorted(matches)[:2])
                note_ids = sorted({c["note"] for c in samples})
                sample_notes = call("notesInfo", notes=note_ids)
                entry["models"].append({"name": model, "cards": len(matches),
                    "sample_card_ids": sorted(matches)[:2], "sample_note_ids": note_ids,
                    "sample_tags": sorted({t for n in sample_notes for t in n["tags"]})[:40]})
            entry["model_inventory_complete"] = covered == set(ids)
            entry["unmapped_cards"] = len(set(ids) - covered)
        report["corpora"].append(entry)
    medical_ids = call("findCards", query='deck:NEBLI::UC*')
    cards = [c for batch in chunks(medical_ids) for c in call("cardsInfo", cards=batch)]
    notes = sorted({c["note"] for c in cards})
    comments = []
    for batch in chunks(notes):
        for note in call("notesInfo", notes=batch):
            value = note.get("fields", {}).get("NEBLI_Comentario", {}).get("value", "").strip()
            if value:
                comments.append({"note_id": note["noteId"], "card_ids": note["cards"], "comment": value})
    # cardsInfo padrão não retorna flags em todas as instalações. Consultar
    # pelo mecanismo de busca; ausência de campo jamais significa flag zero.
    medical_set = set(medical_ids)
    flag_ids = {str(flag): sorted(medical_set.intersection(call(
        "findCards", query=f'deck:NEBLI::UC* flag:{flag}'))) for flag in range(8)}
    if set().union(*(set(ids) for ids in flag_ids.values())) != medical_set:
        report["errors"].append("Cards sem bandeira determinada; coleção pode ter mudado durante leitura.")
    report["medical"] = {
        "cards": len(cards), "notes": len(notes),
        "by_deck": dict(Counter(c["deckName"] for c in cards)),
        "flags": {flag: len(ids) for flag, ids in flag_ids.items()},
        "suspended": sum(c.get("queue") == -1 for c in cards),
        "never_reviewed": sum(c.get("reps", 0) == 0 for c in cards),
        "comments": comments,
        "red_or_orange_ids": flag_ids["1"] + flag_ids["2"],
    }
    report["sample_model_structure"] = {}
    for model in sorted(model_names):
        report["sample_model_structure"][model] = {
            "fields": call("modelFieldNames", modelName=model),
            "templates": call("modelTemplates", modelName=model),
        }
    report["local_tools"] = {"typst_cli": bool(shutil.which("typst")),
                             "typst_python": importlib.util.find_spec("typst") is not None,
                             "claude_cli": bool(shutil.which("claude"))}
    if report["errors"]:
        report["status"] = "partial"
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint", default="http://127.0.0.1:8765")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--catalog", action="store_true", help="mapear todos os modelos e subdecks, sem auditoria semântica integral")
    args = parser.parse_args()
    # Recibos são imutáveis por padrão: escolha outro nome para uma nova leitura.
    if args.output.exists():
        parser.error("Arquivo já existe; informe outro nome de diagnóstico.")
    try:
        report = collect(ReadOnlyAnki(args.endpoint), catalog=args.catalog)
    except Exception as error:
        report = {"status": "failed", "read_only_anki": True, "error": str(error)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps({"status": report["status"], "output": str(args.output),
                      "medical_cards": report.get("medical", {}).get("cards"),
                      "corpora": [{"deck": c["deck"], "cards": c["cards"]}
                                  for c in report.get("corpora", [])]}, ensure_ascii=False))
    return 0 if report["status"] == "observed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
