#!/usr/bin/env python3
"""Normaliza e valida o metadata schema11 usado por importadores Anki atuais.

O writer v13 usa collection.anki2 por compatibilidade. JSON sintaticamente válido
não basta: o backend do Anki desserializa col.decks/model/dconf em structs schema11.
Este módulo garante os campos obrigatórios antes de qualquer APKG ser entregue.
"""
from __future__ import annotations

import json
import os
import sqlite3
import tempfile
import zipfile
from pathlib import Path
from typing import Any

TODAY_KEYS = ("lrnToday", "revToday", "newToday", "timeToday")
DECK_REQUIRED = {"id", "name", "usn", "dyn", "collapsed", "conf", *TODAY_KEYS}
MODEL_REQUIRED = {"id", "name", "type", "mod", "usn", "sortf", "tmpls", "flds"}
DCONF_REQUIRED = {"id", "mod", "name", "usn", "maxTaken", "autoplay", "timer", "new", "rev", "lapse"}
NEW_REQUIRED = {"delays", "initialFactor", "ints", "order", "perDay"}
REV_REQUIRED = {"ease4", "ivlFct", "maxIvl", "perDay"}
LAPSE_REQUIRED = {"delays", "leechAction", "leechFails", "minInt", "mult"}


def _missing(value: dict[str, Any], required: set[str]) -> list[str]:
    return sorted(required - set(value))


def schema11_metadata_errors(decks: dict[str, Any], models: dict[str, Any], dconf: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not decks:
        errors.append("schema11: col.decks vazio")
    for key, deck in decks.items():
        if not isinstance(deck, dict):
            errors.append(f"schema11: deck {key} não é objeto")
            continue
        missing = _missing(deck, DECK_REQUIRED)
        if missing:
            errors.append(f"schema11: deck {key} sem campos: {', '.join(missing)}")
        for today in TODAY_KEYS:
            value = deck.get(today)
            if not isinstance(value, list) or len(value) < 2:
                errors.append(f"schema11: deck {key}.{today} deve ser [dia, quantidade]")
        if not isinstance(deck.get("dyn"), (int, bool)):
            errors.append(f"schema11: deck {key}.dyn deve ser inteiro/bool")

    if not models:
        errors.append("schema11: col.models vazio")
    for key, model in models.items():
        if not isinstance(model, dict):
            errors.append(f"schema11: model {key} não é objeto")
            continue
        missing = _missing(model, MODEL_REQUIRED)
        if missing:
            errors.append(f"schema11: model {key} sem campos: {', '.join(missing)}")
        for index, field in enumerate(model.get("flds") or []):
            if not isinstance(field, dict) or not {"name", "sticky", "rtl", "font", "size"}.issubset(field):
                errors.append(f"schema11: model {key}.flds[{index}] incompleto")
        for index, template in enumerate(model.get("tmpls") or []):
            if not isinstance(template, dict) or not {"name", "qfmt"}.issubset(template):
                errors.append(f"schema11: model {key}.tmpls[{index}] incompleto")

    if not dconf:
        errors.append("schema11: col.dconf vazio")
    for key, conf in dconf.items():
        if not isinstance(conf, dict):
            errors.append(f"schema11: dconf {key} não é objeto")
            continue
        missing = _missing(conf, DCONF_REQUIRED)
        if missing:
            errors.append(f"schema11: dconf {key} sem campos: {', '.join(missing)}")
            continue
        for section, required in (("new", NEW_REQUIRED), ("rev", REV_REQUIRED), ("lapse", LAPSE_REQUIRED)):
            value = conf.get(section)
            if not isinstance(value, dict):
                errors.append(f"schema11: dconf {key}.{section} não é objeto")
            else:
                miss = _missing(value, required)
                if miss:
                    errors.append(f"schema11: dconf {key}.{section} sem campos: {', '.join(miss)}")
    return errors


def _metadata(db: sqlite3.Connection) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    row = db.execute("SELECT decks, models, dconf FROM col LIMIT 1").fetchone()
    if row is None:
        raise ValueError("APKG sem linha col")
    return tuple(json.loads(raw or "{}") for raw in row)  # type: ignore[return-value]


def normalize_legacy_collection(collection: Path) -> dict[str, Any]:
    db = sqlite3.connect(collection)
    try:
        decks, models, dconf = _metadata(db)
        changed = False
        for deck in decks.values():
            if not isinstance(deck, dict):
                continue
            for key in TODAY_KEYS:
                if key not in deck:
                    deck[key] = [0, 0]
                    changed = True
            if "browserCollapsed" not in deck:
                deck["browserCollapsed"] = False
                changed = True
        if changed:
            db.execute("UPDATE col SET decks=?", (json.dumps(decks, ensure_ascii=False),))
            db.commit()
        errors = schema11_metadata_errors(decks, models, dconf)
        return {"passed": not errors, "changed": changed, "errors": errors, "deck_count": len(decks), "model_count": len(models), "dconf_count": len(dconf)}
    finally:
        db.close()


def normalize_apkg(apkg: Path) -> dict[str, Any]:
    apkg = apkg.resolve()
    with tempfile.TemporaryDirectory(prefix="nebli-schema11-", dir=apkg.parent) as raw:
        temp = Path(raw)
        collection = temp / "collection.anki2"
        rebuilt = temp / "rebuilt.apkg"
        with zipfile.ZipFile(apkg, "r") as source:
            if "collection.anki2" not in source.namelist():
                return {"passed": False, "changed": False, "errors": ["schema11: collection.anki2 ausente"]}
            collection.write_bytes(source.read("collection.anki2"))
            result = normalize_legacy_collection(collection)
            if not result["passed"]:
                return result
            with zipfile.ZipFile(rebuilt, "w", compression=zipfile.ZIP_DEFLATED) as target:
                for info in source.infolist():
                    if info.filename == "collection.anki2":
                        target.writestr(info, collection.read_bytes())
                    else:
                        target.writestr(info, source.read(info.filename))
        os.replace(rebuilt, apkg)
        return result


def validate_apkg_schema11(apkg: Path) -> dict[str, Any]:
    with zipfile.ZipFile(apkg, "r") as package, tempfile.NamedTemporaryFile(suffix=".anki2") as temp:
        if "collection.anki2" not in package.namelist():
            return {"passed": False, "errors": ["schema11: collection.anki2 ausente"]}
        temp.write(package.read("collection.anki2")); temp.flush()
        db = sqlite3.connect(temp.name)
        try:
            decks, models, dconf = _metadata(db)
        finally:
            db.close()
        errors = schema11_metadata_errors(decks, models, dconf)
        return {"passed": not errors, "errors": errors, "deck_count": len(decks), "model_count": len(models), "dconf_count": len(dconf)}
