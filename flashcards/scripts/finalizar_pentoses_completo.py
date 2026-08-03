#!/usr/bin/env python3
"""Gera o lote final com rótulo inglês e permite cópias autorais por deck."""
from pathlib import Path

root = Path(__file__).resolve().parents[2]
build = root / "flashcards/scripts/build_card.py"
text = build.read_text(encoding="utf-8")
text = text.replace('"options": {"allowDuplicate": False}', '"options": {"allowDuplicate": True}')
build.write_text(text, encoding="utf-8")

source = Path(__file__).with_name("executar_piloto_pentoses_completo_v3.py")
code = source.read_text(encoding="utf-8")
code = code.replace(
    "exec(compile(code, str(source), \"exec\"))",
    "code = code.replace('\\\"theme_label\\\": \\\"Bioquímica\\\"', '\\\"theme_label\\\": \\\"Biochemistry\\\"')\nexec(compile(code, str(source), \"exec\"))",
)
exec(compile(code, str(source), "exec"))
