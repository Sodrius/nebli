#!/usr/bin/env python3
from pathlib import Path

source = Path(__file__).with_name("gerar_curadoria_pentoses_completa.py")
code = source.read_text(encoding="utf-8").replace('CP:0.`KnC.`', 'CP:0.`KnC.')
exec(compile(code, str(source), "exec"))
