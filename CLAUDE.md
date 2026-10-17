# NEBLI — entrada de toda sessão

1. [ESTADO-ATUAL.md](ESTADO-ATUAL.md) › **Retomar aqui** e **Quem está com o quê**: o que fazer agora e o que outro executor já pegou.
2. [MEMORY.md](MEMORY.md): **a regra única e vigente** do que Davi quer (reorganizada em 13/10; versões antigas em `arquivo/` não são norma). Das [FEEDBACKS](flashcards/projeto/FEEDBACKS.md), ler só as entradas novas desde a última sessão.
3. Para fazer um deck: [EXECUCAO-DECK-AULA](flashcards/projeto/EXECUCAO-DECK-AULA.md) — **passos em ordem, do 0 ao 7, sem pular** (reescrito 16/10).

## Pedido curto

“Faz a aula X”, “continua”, `/deck-aula X` ou só o nome da aula = executar o roteiro inteiro até o deck entregue (instalado **sem Tab**, gates duros 100%, pacote da UC, sync) e relatar no formato do MEMORY §11. Sem agente, sem plano para aprovar, sem pedir permissão, sem parar no meio. **Desde 16/10 noite (F-20261016-CLAUDE-11): rodar as aulas em sequência, cada uma pelo pipeline inteiro, até Davi pedir para parar**; feedback que chegar é aplicado antes do deck seguinte. Plano vigente: [PLANO-ANKING-PRIMEIRO](flashcards/projeto/PLANO-ANKING-PRIMEIRO-2026-10-15.md).

## Limites que não mudam

- Davi estuda no Anki enquanto o executor trabalha: nunca tocar a nota em tela nem irmãos; escrita só por `nebli.decks.escrita()`; sync quando ele estiver ocioso.
- Outro executor (Codex) trabalha em paralelo: reivindicar a aula no ESTADO-ATUAL antes; não mexer no que ele reivindicou; reler antes de gravar.
- Preservar originais AnKing, IDs/histórico, comentários, marcas e suspensões pessoais. Não apagar notas sem autorização de Davi e backup. Arquivar documentos superados em `arquivo/` com hash.
- Feedback novo: literal em FEEDBACKS → regra **reescrita no lugar** no MEMORY (sem acrescentar camada) → check no lint/gate quando mecanizável.
- Não fabricar leitura, busca, teste ou revisão. Gate aprovado não prova julgamento.
- **AnKing-primeiro com gates duros** (MEMORY §5): busca nos três caminhos em todos os acervos, `busca/cobertura.tsv`, autoral só para lacuna provada, **no máximo 20% dos cards** (35% só com `AUTORAL_EXCECAO`), **todo AnKing do conteúdo da aula entra, sem teto de cards** (`PIPELINE_VERSAO = 4`, `SECOES_DA_AULA`) e relido contra os ANTI-EXEMPLARES. O `apply` recusa instalar sem isso.

## Outras rotas (só sob pedido)

Índice do projeto: [README.md](README.md). Pedido explícito de “E1 + cards” (E1 + deck) inclui a E1: `didatica/E1.md`. Cadernos: `banco/CLAUDE.md` e `ROLES.md`. Typst: `typst-template/CLAUDE.md`. Site, liga e Etimologia: preservar.
