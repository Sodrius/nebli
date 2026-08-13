#!/usr/bin/env python3
"""Gate estrutural e visual da E1 canônica.

Impede que uma apostila seja liberada como documento Typst autônomo e contorne
o design system Nebli. A inspeção de pixels continua humana, mas precisa ser
registrada explicitamente após a renderização de todas as páginas.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


FORMAT_REVIEW_FLAGS = (
    "canonical_template_used",
    "all_pages_rendered",
    "layout_reviewed",
    "paragraph_hierarchy_preserved",
    "images_legible_and_integrated",
    "no_clipping_or_overflow",
    "independent_visual_review_passed",
)

TEMPLATE_IMPORT = "nebli_v2_apostila.typ"
REQUIRED_STAGE_HELPERS = {
    "intro-box": 1,
    "parte-title": 1,
    "subtopico": 1,
    "conclusao-box": 1,
}
FORBIDDEN_GLOBAL_PATTERNS = {
    "#set page": r"(?m)^\s*#set\s+page\s*\(",
    "#set par": r"(?m)^\s*#set\s+par\s*\(",
    "#show strong": r"(?m)^\s*#show\s+strong\s*:",
    "helper local de capa": r"(?m)^\s*#let\s+capa\b",
    "helper local de parte": r"(?m)^\s*#let\s+(?:parte-title|part)\b",
    "helper local de tópico": r"(?m)^\s*#let\s+(?:subtopico|topic)\b",
}


def _resolve(base: Path, raw: Any) -> Path:
    path = Path(str(raw or ""))
    return path if path.is_absolute() else (base / path).resolve()


def _read(path: Path, label: str, errors: list[str]) -> str:
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"{label} inexistente ou vazio: {path}")
        return ""
    return path.read_text(encoding="utf-8-sig")


def validate_e1_formatting(release: dict[str, Any], deck_data_path: Path) -> list[str]:
    errors: list[str] = []
    base = deck_data_path.parent.resolve()
    source_path = _resolve(base, release.get("e1_source"))
    source = _read(source_path, "e1_source", errors)
    lesson_dir = source_path.parent
    main = _read(lesson_dir / "main.typ", "main.typ canônico", errors)
    resumindo = _read(lesson_dir / "resumindo.typ", "resumindo.typ canônico", errors)

    if source:
        if TEMPLATE_IMPORT not in source or not re.search(
            r'(?m)^\s*#import\s+"[^"]*nebli_v2_apostila\.typ"\s*:\s*\*', source
        ):
            errors.append("E1 deve importar o template oficial nebli_v2_apostila.typ")
        for label, pattern in FORBIDDEN_GLOBAL_PATTERNS.items():
            if re.search(pattern, source):
                errors.append(f"E1 não pode redefinir {label}; use o template oficial")
        for helper, minimum in REQUIRED_STAGE_HELPERS.items():
            count = len(re.findall(rf"#{re.escape(helper)}\s*[\[(]", source))
            if count < minimum:
                errors.append(f"E1 deve usar #{helper} do template oficial")

    if main:
        checks = {
            "importar o template oficial": TEMPLATE_IMPORT in main,
            "aplicar #show: pagina-padrao": bool(re.search(r"#show\s*:\s*pagina-padrao", main)),
            "usar #capa": "#capa(" in main,
            "usar #sumario": "#sumario(" in main,
            "usar #etapa-header": "#etapa-header(" in main,
            "incluir etapa1.typ": bool(re.search(r'#include\s+"etapa1\.typ"', main)),
            "incluir resumindo.typ": bool(re.search(r'#include\s+"resumindo\.typ"', main)),
        }
        for label, passed in checks.items():
            if not passed:
                errors.append(f"main.typ deve {label}")

    if resumindo:
        if TEMPLATE_IMPORT not in resumindo:
            errors.append("resumindo.typ deve importar o template oficial")
        if "#resumindo-page(" not in resumindo:
            errors.append("resumindo.typ deve usar #resumindo-page")

    review = release.get("e1_format_review")
    if not isinstance(review, dict):
        errors.append("e1_format_review obrigatório")
        review = {}
    for flag in FORMAT_REVIEW_FLAGS:
        if review.get(flag) is not True:
            errors.append(f"e1_format_review.{flag}=true é obrigatório")
    defects = review.get("unresolved_visual_defects")
    if not isinstance(defects, list):
        errors.append("e1_format_review.unresolved_visual_defects deve ser lista")
    elif defects:
        errors.append("e1_format_review.unresolved_visual_defects precisa estar vazio para liberar")
    if not str(review.get("summary") or "").strip():
        errors.append("e1_format_review.summary obrigatório")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck_data", type=Path)
    args = parser.parse_args()
    data = json.loads(args.deck_data.read_text(encoding="utf-8"))
    release = data.get("release_gate") if isinstance(data.get("release_gate"), dict) else {}
    errors = validate_e1_formatting(release, args.deck_data.resolve())
    print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
