#!/usr/bin/env python3
"""Executa o gerador do piloto após aplicar a correção sintática local."""
from pathlib import Path

source = Path(__file__).with_name("gerar_piloto_pentoses_teste.py")
code = source.read_text(encoding="utf-8").replace(
    '"other_decks": "insufficient"}} for cid, _goal, text, _extra, anchor, _image in ROWS]',
    '"other_decks": "insufficient"}}} for cid, _goal, text, _extra, anchor, _image in ROWS]',
)
exec(compile(code, str(source), "exec"))
