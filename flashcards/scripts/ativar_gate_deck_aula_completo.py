#!/usr/bin/env python3
"""Torna o gate AnKing-primeiro parte explícita do comando /resumo."""
from pathlib import Path

root = Path(__file__).resolve().parents[2]
command = root / ".claude/commands/resumo.md"
text = command.read_text(encoding="utf-8")
marker = "\n### Gate deck-aula completo (obrigatório)\n"
block = marker + """Antes de escrever a E2 e antes de mover o PDF, o deck-aula precisa fechar no contrato `deck-aula-v2`: conceitos classificados `nuclear|supporting|no_card`; 100% dos nucleares cobertos; AnKing e externos antes de autoria; retrieval targets sem duplicata; visual obrigatório resolvido; volume revisado. Rode `python flashcards/scripts/gate_deck_aula_completo.py arquivos-trabalho/matriz-deck-aula-<slug>.json --verify-anki`. Exit diferente de zero bloqueia E2, PDF e exportação.\n"""
if marker not in text:
    text += block
command.write_text(text, encoding="utf-8")

pipeline = root / "flashcards/DECK-AULA-PIPELINE.md"
text = pipeline.read_text(encoding="utf-8")
marker = "\n## Gate hard v2 — fechamento bloqueado\n"
block = marker + """Uma aula nova não fecha com nuclear descoberto. O manifesto declara `deck_aula_gate: v2`, inventário com `card_decision`, busca AnKing card-a-card e autoria somente depois de AnKing + outros decks insuficientes. Não existe quota global de fonte nem quota por subtópico. `gate_deck_aula_completo.py --verify-anki` é bloqueante para E2, PDF e .apkg.\n"""
if marker not in text:
    text += block
pipeline.write_text(text, encoding="utf-8")
print("OK: gate v2 ligado em /resumo e documentado no pipeline")
