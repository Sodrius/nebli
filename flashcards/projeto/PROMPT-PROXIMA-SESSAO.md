# Prompt para abrir a próxima conversa (Claude) — colar inteiro

continua fazendo os decks, a partir do ponto em que a conversa anterior parou. Entre por `~/NEBLI/CLAUDE.md` → `ESTADO-ATUAL.md` › Retomar aqui → `flashcards/projeto/EXECUCAO-DECK-AULA.md` (passos 0–7, em ordem, sem pular). Leia só as entradas novas do FEEDBACKS (desde F-20261016-CLAUDE-09) e os ANTI-EXEMPLARES antes de escrever qualquer autoral.

A Micro da P3 foi refeita inteira em 16/10 (43, 44, 48, 50; corridas `…-v2-2026-10-16`). Se Davi deu feedback nela, aplique primeiro (correções nos specs + `build.py --delta` + `nebli.delta`). Depois, o próximo deck é o que ele pedir; sem pedido, **UC03 P1 · 04 Radiografia e ultrassom**, corrida pré-aberta em `arquivos-trabalho/deck-aula-uc03-rd04-radiografia-ultrassom-v2-2026-10-16` (41 lâminas de 2026; nada lido).

Regras que valem (gates duros; não se contornam, corrige-se o deck):
- `PIPELINE_VERSAO = 4`: autoral ≤ 20% dos cards; até 30% só com `AUTORAL_EXCECAO` e com reticência (contando autorais antigos mantidos por sh()); `SECOES_DA_AULA` declaradas e toda nota delas no deck ou em `EXCLUIDOS` com motivo. Deck sem teto de cards.
- Doenças pelo livro da UC; as que não estão nas lâminas com cobertura mínima (1–3 cards AnKing).
- Refação de aula em estudo: `acervo()` no spec, `nebli.refacao` antes do apply, `nebli.extra_vivo` para imagens pedidas, `nebli.apaga_retirados refacao-v2` ao fim (backup).
- Busca nos três caminhos em todos os acervos e decks NEBLI vivos; HY 1–2 é verde.
- Sem Tab (o Codex faz depois); gates com `NEBLI_SEM_TAB=1`.
- Ao terminar: relato (MEMORY §11) com o prompt de Tab do Codex, ESTADO-ATUAL, memória, commit e push; deixar o próximo deck preparado e este prompt atualizado.
