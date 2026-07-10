# Checkpoint apostilas históricas — OPERAÇÃO FECHADA

**Última atualização:** 2026-05-25 — Todas as 6 fases concluídas
**Status:** ✓ OPERAÇÃO COMPLETA

## Concluído

- **Phase A** ✓ — 33 PDFs copiados para `resumos-gerados/apostilas-historicas/` + `INDICE.md` gerado.
- **Phase B** ✓ — 33 .txt + 33 -estrutura.json + `_resumo-estrutura.md` em `arquivos-trabalho/apostilas-historicas/`.
- **Phase C** ✓ — Agents `revisor-pdf-didatico.md` e `revisor-pdf-profundo.md` criados em `.claude/agents/` (não foram carregados em runtime — substituído por `general-purpose` com `model` override e prompts inline em `_prompt-didatico.md` / `_prompt-profundo.md`).
- **Phase D** ✓ — 33 didáticos (Sonnet) + 33 profundos (Opus) = **66 relatórios** em `arquivos-trabalho/apostilas-historicas/`.
- **Phase E** ✓ — Meta-análise em `arquivos-trabalho/META-ANALISE-APOSTILAS-HISTORICAS.md` (7 seções + apêndice).
- **Phase F** ✓ — Lições para REDATOR-NEBLI em `arquivos-trabalho/LICOES-PARA-REDATOR-NEBLI.md` (8 seções + patches literais).

## Sumário quantitativo

- **Vereditos T2:** 18 APROVAR + 15 APROVAR COM RESSALVAS / 33. Score médio 4.22/5.
- **Vereditos T3:** 33 APROVAR COM RESERVAS / 33 (nenhum bloqueio).
- **Achado mais crítico:** UC01-BC-07-divisao-celular tem gabarito ERRADO em 13/30 questões objetivas (43%).
- **Bug-família template:** header "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" fantasma em 13/33 PDFs (correção 1 linha).
- **Erro recorrente principal:** paridade distratoras Q26-Q30 (ratio 1.4-2.8×) em ~17/33 PDFs.

## Artefatos entregues

1. `resumos-gerados/apostilas-historicas/` — 33 PDFs + `INDICE.md`.
2. `arquivos-trabalho/apostilas-historicas/` — 33 .txt + 33 .json + 66 relatórios + 2 prompts canônicos (`_prompt-didatico.md`, `_prompt-profundo.md`) + `_resumo-estrutura.md`.
3. `arquivos-trabalho/META-ANALISE-APOSTILAS-HISTORICAS.md` — meta-análise consolidada.
4. `arquivos-trabalho/LICOES-PARA-REDATOR-NEBLI.md` — patches literais para `redator-e1.md`, `questionador.md`, `CLAUDE.md`, `precompile-check.py`, `EXEMPLARES.md`, `errosComuns_nebli.md`.
5. `typst-build/organizar_apostilas_historicas.py` + `typst-build/preparar_revisao_apostila.py` — scripts da operação.
6. `.claude/agents/revisor-pdf-didatico.md` + `revisor-pdf-profundo.md` — agents para uso futuro (não rodaram nesta sessão).

## Limitações declaradas

1. **Análise visual degradada em 40/66 relatórios** — `pdftoppm` bloqueado no sandbox; agents usaram metadata JSON + texto extraído como proxy. Bugs visuais reportados são reais e confirmáveis; cobertura estética é incompleta.
2. **Identidade dos PDFs:** todos os 33 são output do próprio pipeline NEBLI (não apostilas externas como o INDICE sugere). Exercício virou auto-calibração.
3. **Nenhum patch foi aplicado** — todos os 8 próximos passos sugeridos em §8 do `LICOES-PARA-REDATOR-NEBLI.md` ficam para Davi decidir/executar.
