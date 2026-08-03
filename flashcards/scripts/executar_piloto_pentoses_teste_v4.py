#!/usr/bin/env python3
"""Executa o gerador com a frente de ribose sem pista lexical."""
from pathlib import Path

source = Path(__file__).with_name("gerar_piloto_pentoses_teste.py")
code = source.read_text(encoding="utf-8").replace(
    '"other_decks": "insufficient"}} for cid, _goal, text, _extra, anchor, _image in ROWS]',
    '"other_decks": "insufficient"}}} for cid, _goal, text, _extra, anchor, _image in ROWS]',
)
for old, new in {
    'Glucose-6-phosphate can be used': 'G6P can be used',
    'NADPH and ribose-5-phosphate}}</b>.': 'ribose-5-phosphate}}</b>.',
    'fase oxidativa: ela é irreversível': 'fase oxidativa',
    'saem 2 NADPH, 1 CO2 e uma pentose': '2 NADPH',
    'transcetolase transfere blocos de dois carbonos': 'transcetolase',
    'regenerar a glutationa reduzida': 'glutationa',
    'a glutationa reduzida neutraliza o peróxido': 'peróxido',
    'tem herança ligada ao X': 'malária',
}.items():
    code = code.replace(old, new)
code = code.replace(
    'The pentose phosphate pathway supplies <b>{{c1::ribose-5-phosphate}}</b>.',
    'This metabolic route supplies NADPH and <b>{{c1::ribose-5-phosphate}}</b>.',
)
exec(compile(code, str(source), "exec"))
