# Prompt para abrir a próxima conversa (Claude) — colar inteiro

continua fazendo os decks da UC03 que não têm deck-aula, a partir do ponto em que a conversa anterior parou. Entre por `~/NEBLI/CLAUDE.md` → `ESTADO-ATUAL.md` › Retomar aqui → o **PIPELINE DE GERAÇÃO DE DECK v6** (`flashcards/projeto/EXECUCAO-DECK-AULA.md`, etapas E0–E8, sem pular). Leia as entradas novas do FEEDBACKS (desde F-20261022-CLAUDE-08) e regenere/leia EXEMPLARES e ANTI-EXEMPLARES antes de escrever qualquer autoral.

**O que mudou em 22/10 (F-20261022-CLAUDE-06), gate duro:** depois de ler TODO o material (lâminas, transcrição, apostilas, monitoria, provas, livro, ≥1 vídeo de canal que Davi segue) e antes de buscar, responder em `compreensao-aula.json` (molde já na corrida): o que a aula ensina, onde se encaixa, o que lembrar e, bloco a bloco das lâminas, o que o professor ensina e o papel do bloco (motivação, princípio, exemplo, resumo, repetição). Postar um resumo curto no chat e seguir. O deck nasce disso, segue o slide em ordem e conteúdo, o exemplo clínico vem depois do princípio e nunca vira carro-chefe; ao fechar, `fidelidade` bloco a bloco contra o deck vivo. Autoral sem teto (`PIPELINE_VERSAO = 5`), mas só depois de provar nos três caminhos que AnKing e todas as Referências Externas não têm o card. Modelo vivo: `arquivos-trabalho/deck-aula-uc03-mb57-principios-virus-v2-2026-10-22` (88/88).

**Próximo deck:** UC03 P3 · 60 Virologia prática (pasta da turma `Microbiologia/Aula 20 - Virologia Prática`: Ia e Ib; corrida antiga `deck-aula-uc03-mb60-virologia-pratica-v2-2026-10-21`, deck não está mais no Anki). A 59 foi entregue em 23/10 (modelo: `…mb59…-v2-2026-10-22`). Modelo vivo do pipeline v6: 58 (`…mb58…-v3-2026-10-22`): compreensão por processo, reconstruções das provas, ciclos completos. A 57 foi feita no v5.

**Fila depois:** 61 Patologia da infecção viral → 63 Imune a vírus e fungos → 64 Hipersensibilidade → 65 Reparo → 69 Hemostasia → 70 Choque e CIVD → 55, 56, 53 e as de tumores (74–79, 81–85), conferindo slides na pasta da turma de cada uma.

Regras que valem (gates duros; não se contornam, corrige-se o deck):
- `SECOES_DA_AULA` declaradas e toda nota delas no deck ou em `EXCLUIDOS` com motivo; todos os irmãos; deck sem teto de cards.
- Clínica lateral ≤ 7%, doença no alvo ≤ 10%; imagem de cada card conferida (`imagens-batem.json`); mapa de profundidade antes dos cards e revisão com raciocínio depois.
- Sem Tab (o Codex faz depois); gates com `NEBLI_SEM_TAB=1`.
- Ao terminar: relato (MEMORY §11), ESTADO-ATUAL, commit e push, sync se Davi não estiver revisando; deixar o próximo deck preparado e este prompt atualizado.
