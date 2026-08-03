#!/usr/bin/env python3
"""Torna o gate AnKing-primeiro parte explícita do comando /resumo."""
from pathlib import Path

root = Path(__file__).resolve().parents[2]
command = root / ".claude/commands/resumo.md"
text = command.read_text(encoding="utf-8")
marker = "\n### Gate deck-aula completo (obrigatório)\n"
block = marker + """Antes de escrever a E2 e antes de mover o PDF, o deck-aula precisa fechar no contrato `deck-aula-v2`: E1 atomizada por âncora literal; busca AnKing card-a-card por fato; cards AnKing/external primeiro; autoria apenas com rejeição documentada; e enriquecimentos Step 1 já incorporados na E1. Rode `python flashcards/scripts/gate_deck_aula_completo.py arquivos-trabalho/matriz-deck-aula-<slug>.json --verify-anki`. Exit diferente de zero bloqueia E2, PDF e exportação. `PENDENTE-GERADO` não é estado de ship: a lacuna deve virar card e entrar no deck antes de fechar.\n"""
if marker not in text:
    text += block
command.write_text(text, encoding="utf-8")

pipeline = root / "flashcards/DECK-AULA-PIPELINE.md"
text = pipeline.read_text(encoding="utf-8")
marker = "\n## Gate hard v2 — fechamento bloqueado\n"
block = marker + """Uma aula nova não fecha com cobertura parcial. O manifesto deve declarar `deck_aula_gate: v2`, inventário atomizado com âncora literal de cada fato E1, pool AnKing consultado por fato e razão de keep/drop. Pelo menos 60% dos fatos nucleares devem entrar como cópia de card real AnKing/deck externo quando há candidatos; um card autoral só é permitido com a rejeição documentada do pool. Todo aprofundamento Step 1 selecionado deve estar na E1 antes da E2, com âncora literal. `gate_deck_aula_completo.py --verify-anki` é bloqueante para E2, PDF e .apkg; `PENDENTE-GERADO` é fila de trabalho, nunca estado de entrega.\n"""
if marker not in text:
    text += block
pipeline.write_text(text, encoding="utf-8")
print("OK: gate v2 ligado em /resumo e documentado no pipeline")
