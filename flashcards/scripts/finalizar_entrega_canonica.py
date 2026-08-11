#!/usr/bin/env python3
"""Fecha o pipeline v8 e materializa somente E1/PDF + manifesto do Companion."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from validar_deck_card_a_card import validate_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--deck-data", type=Path, required=True)
    parser.add_argument("--validation-report", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    deck_path = args.deck_data.resolve()
    report_path = args.validation_report.resolve()
    deck = json.loads(deck_path.read_text(encoding="utf-8"))
    report = json.loads(report_path.read_text(encoding="utf-8"))
    result = validate_report(report, 0.82, 0.06)
    if not result["ok"]:
        raise SystemExit("ERRO: validação card a card reprovada: " + json.dumps(result, ensure_ascii=False))

    deck_keys = {
        str(card.get("card_key") or "").strip()
        for card in deck.get("cards", []) if isinstance(card, dict)
    }
    report_keys = {
        str(card.get("card_key") or "").strip()
        for card in report.get("cards", []) if isinstance(card, dict)
    }
    if deck_keys != report_keys:
        raise SystemExit("ERRO: validation-report não corresponde exatamente aos cards de deck-data")
    release = deck.get("release_gate") or {}
    if result["expected_card_count"] != len(deck_keys):
        raise SystemExit("ERRO: contagem validada diverge do deck-data")
    if result["card_budget_hard_max"] != release.get("card_budget_hard_max"):
        raise SystemExit("ERRO: teto validado diverge do release_gate")

    e1_pdf = Path(str(release.get("e1_pdf") or ""))
    if not e1_pdf.is_absolute():
        e1_pdf = (deck_path.parent / e1_pdf).resolve()
    metadata = deck.get("metadata") or {}
    lesson_name = str(metadata.get("nome_curto") or args.slug).strip().replace("/", "-")
    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    final_pdf = out_dir / f"{lesson_name} - E1.pdf"
    final_manifest = out_dir / f"{args.slug}.ankidroid.json"

    generator = Path(__file__).with_name("gerar_manifesto_ankidroid.py")
    with tempfile.TemporaryDirectory(prefix="nebli-release-", dir=out_dir) as raw:
        temp = Path(raw)
        temp_manifest = temp / final_manifest.name
        proc = subprocess.run(
            [sys.executable, str(generator), "--slug", args.slug,
             "--deck-data", str(deck_path), "--out", str(temp_manifest)],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            raise SystemExit(proc.stderr or proc.stdout or "ERRO: gerador de manifesto falhou")
        temp_pdf = temp / final_pdf.name
        shutil.copy2(e1_pdf, temp_pdf)
        temp_pdf.replace(final_pdf)
        temp_manifest.replace(final_manifest)

    print(final_pdf)
    print(final_manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
