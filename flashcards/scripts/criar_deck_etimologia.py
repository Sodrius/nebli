#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Cria e valida a arvore NEBLI::Etimologia sem tocar em cards.

Dry-run por padrao:
  python flashcards/scripts/criar_deck_etimologia.py

Aplicacao explicita:
  python flashcards/scripts/criar_deck_etimologia.py --apply
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from nebli_anki import call


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "etimologia" / "deck_structure.json"


def load_manifest(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("root") != "NEBLI::Etimologia":
        raise ValueError("manifesto deve ter root=NEBLI::Etimologia")
    return data


def deck_names(data: dict) -> list[str]:
    root = data["root"]
    names = [root]
    for group in data.get("decks", []):
        parent = f'{root}::{group["name"]}'
        names.append(parent)
        for child in group.get("children", []):
            names.append(f"{parent}::{child}")
    if len(names) != len(set(names)):
        raise ValueError("manifesto contem decks duplicados")
    return names


def main(manifest_path: Path, apply: bool) -> int:
    data = load_manifest(manifest_path)
    wanted = deck_names(data)
    before = set(call("deckNames"))
    missing = [name for name in wanted if name not in before]

    print(f"manifesto: {manifest_path}")
    print(f"decks declarados: {len(wanted)}")
    print(f"ja existentes: {len(wanted) - len(missing)}")
    print(f"a criar: {len(missing)}")

    if not apply:
        for name in missing:
            print(f"  DRY-RUN {name}")
        print("Nada foi alterado. Use --apply para criar.")
        return 0

    for name in missing:
        call("createDeck", deck=name)

    after = set(call("deckNames"))
    absent = [name for name in wanted if name not in after]
    unexpected = sorted(name for name in after if name.startswith(data["root"] + "::") and name not in wanted)
    if absent:
        raise RuntimeError(f"validacao falhou; decks ausentes: {absent}")

    print(f"Criados: {len(missing)}")
    print(f"Validados: {len(wanted)}/{len(wanted)}")
    if unexpected:
        print("Aviso: ha decks adicionais sob a raiz:")
        for name in unexpected:
            print(f"  {name}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    raise SystemExit(main(args.manifest, args.apply))
