#!/usr/bin/env python3
"""Fecha o pipeline canônico somente se relatório e artefatos ainda forem idênticos."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import hashlib
from pathlib import Path

from validar_deck_card_a_card import validate_report
from canonical_cards import content_sha256, ordered_card_set_sha256, referenced_media_hashes, sha256_obj


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
    if report.get("schema") != "nebli-card-validation-v2" or report.get("ok") is not True:
        raise SystemExit("ERRO: relatório de validação ausente, antigo ou reprovado")

    deck_cards = [card for card in deck.get("cards", []) if isinstance(card, dict)]
    deck_rows = [{"card_key": str(card.get("card_key") or ""), "content_sha256": content_sha256(card)} for card in deck_cards]
    report_rows = [{"card_key": str(card.get("card_key") or ""), "content_sha256": str(card.get("content_sha256") or "")} for card in report.get("cards", []) if isinstance(card, dict)]
    if deck_rows != report_rows:
        raise SystemExit("ERRO: cards, ordem ou conteúdo mudaram depois da validação")
    deck_set_hash = ordered_card_set_sha256(deck_cards)
    if report.get("ordered_card_set_sha256") != deck_set_hash:
        raise SystemExit("ERRO: hash do conjunto ordenado diverge do relatório")
    if report.get("media", []) != referenced_media_hashes(deck_cards, deck_path.parent):
        raise SystemExit("ERRO: mídia mudou depois da revisão")
    release = deck.get("release_gate") or {}
    if report.get("expected_card_count") != len(deck_cards):
        raise SystemExit("ERRO: contagem validada diverge do deck-data")
    if report.get("card_budget_hard_max") != release.get("card_budget_hard_max"):
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
        manifest = json.loads(temp_manifest.read_text(encoding="utf-8"))
        manifest_rows = [{"card_key": str(c.get("card_key") or ""), "content_sha256": str(c.get("content_sha256") or "")} for c in manifest.get("cards", [])]
        if manifest_rows != report_rows or manifest.get("ordered_card_set_sha256") != deck_set_hash:
            raise SystemExit("ERRO: manifesto gerado não contém exatamente os cards aprovados")
        manifest["validation_report_sha256"] = hashlib.sha256(report_path.read_bytes()).hexdigest()
        manifest.pop("manifest_sha256", None)
        manifest["manifest_sha256"] = sha256_obj(manifest)
        temp_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temp_pdf = temp / final_pdf.name
        shutil.copy2(e1_pdf, temp_pdf)
        temp_pdf.replace(final_pdf)
        temp_manifest.replace(final_manifest)

    print(final_pdf)
    print(final_manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
