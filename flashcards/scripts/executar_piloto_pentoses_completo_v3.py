#!/usr/bin/env python3
from pathlib import Path

source = Path(__file__).with_name("executar_piloto_pentoses_completo.py")
code = source.read_text(encoding="utf-8")
code = code.replace(
    "exec(compile(code, str(source), \"exec\"))",
    "code = code.replace('_par_bioq-20-pentoses-radicais-livres-teste-completo/', '_par_bioq-20-pentoses-radicais-livres-teste/')\ncode = code.replace('figuras/bioq-20-pentoses-radicais-livres-teste-completo', 'figuras/bioq-20-pentoses-radicais-livres-teste')\nexec(compile(code, str(source), \"exec\"))",
)
exec(compile(code, str(source), "exec"))
