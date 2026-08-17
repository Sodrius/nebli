#!/usr/bin/env python3
"""Valida evidência concreta de calibração e ordem da E1 antes do release."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

APPROVED_UC02 = {
    "typst-build/_par_bioq-23-aminoacidos-ureia/etapa1.typ",
    "typst-build/_par_histo-07-osseo/etapa1.typ",
    "typst-build/_par_biomol-25-mutacao-reparo-recombinacao/etapa1.typ",
    "typst-build/_par_biomol-26-dna-recombinante-pcr/etapa1.typ",
}
REQUIRED_PASSES = {"fonte_e1", "iniciante_zero", "didatica_voz", "pdf_visual"}


def _text(value: Any) -> str:
    return str(value or "").strip()


def validate_e1_calibration(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    release = data.get("release_gate") if isinstance(data.get("release_gate"), dict) else {}
    review = release.get("e1_review") if isinstance(release.get("e1_review"), dict) else {}

    canon = review.get("calibration_canon")
    if not isinstance(canon, list):
        errors.append("e1_review.calibration_canon[] obrigatório")
        canon = []
    canon_text = " ".join(_text(item) for item in canon).casefold()
    if "exemplares.md" not in canon_text or not all(str(n) in canon_text for n in (1, 8, 14, 17)):
        errors.append("calibration_canon deve registrar EXEMPLARES.md categorias 1, 8, 14 e 17")
    if "anti-exemplares.md" not in canon_text:
        errors.append("calibration_canon deve registrar ANTI-EXEMPLARES.md")

    exemplars = review.get("calibration_exemplars")
    if not isinstance(exemplars, list):
        errors.append("e1_review.calibration_exemplars[] obrigatório")
        exemplars = []
    normalized = {_text(item).replace("\\", "/") for item in exemplars if _text(item)}
    approved = normalized & APPROVED_UC02
    if len(approved) < 2:
        errors.append("calibration_exemplars exige pelo menos dois exemplares UC02 canônicos distintos")
    unknown = sorted(normalized - APPROVED_UC02)
    if unknown:
        errors.append("calibration_exemplars contém caminho fora do conjunto canônico: " + ", ".join(unknown))

    if review.get("matrix_frozen_before_drafting") is not True:
        errors.append("e1_review.matrix_frozen_before_drafting=true obrigatório")
    matrix = release.get("source_to_e1_matrix")
    if not isinstance(matrix, list) or not matrix:
        errors.append("source_to_e1_matrix precisa existir antes da redação")

    passes = review.get("review_passes")
    if not isinstance(passes, list):
        errors.append("e1_review.review_passes[] obrigatório")
        passes = []
    missing = sorted(REQUIRED_PASSES - {_text(item) for item in passes})
    if missing:
        errors.append("review_passes incompleto: " + ", ".join(missing))

    summary = _text(review.get("calibration_summary"))
    if len(summary) < 80:
        errors.append("e1_review.calibration_summary deve explicar como os exemplares calibraram esta E1")

    return {
        "passed": not errors,
        "errors": errors,
        "approved_uc02_exemplars": sorted(approved),
        "review_passes": sorted({_text(item) for item in passes if _text(item)}),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck_data", type=Path)
    args = parser.parse_args()
    data = json.loads(args.deck_data.read_text(encoding="utf-8"))
    result = validate_e1_calibration(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
