# NEBLI — entrada de toda sessão (Codex e qualquer executor; mesmo conteúdo do CLAUDE.md)

1. [ESTADO-ATUAL.md](ESTADO-ATUAL.md) › **Retomar aqui** e **Quem está com o quê**: o que fazer agora e o que outro executor já pegou.
2. [MEMORY.md](MEMORY.md): **a regra única e vigente** do que Davi quer (reorganizada em 13/10; versões antigas em `arquivo/` não são norma). Das [FEEDBACKS](flashcards/projeto/FEEDBACKS.md), ler só as entradas novas desde a última sessão.
3. Para fazer um deck: [EXECUCAO-DECK-AULA](flashcards/projeto/EXECUCAO-DECK-AULA.md), **passos em ordem, de E0 a E8, sem pular**. Abrir pelo molde v15; a auditoria aprovada já é gate no E7.

**Decisão de 03/11, pronta no molde v13:** nos próximos decks, cada autoral parte do que quer ensinar e de um exemplar aprovado do mesmo tipo de informação; ver [GUIA-2](flashcards/projeto/GUIA-2-EXEMPLARES.md), MEMORY §2 e E5/E7 do pipeline. A [auditoria de cobertura em dois sentidos](flashcards/projeto/PROPOSTA-AUDITORIA-COBERTURA-2026-11-03.md) foi **aprovada em 03/11** e integra E2/E3/E7: cada relação de `aprender` aponta cards recuperáveis, e todo card do plano é conferido contra a aula no E7, com gate duro antes da entrega. Acompanhamento em 7/14 dias e prova curta extra foram rejeitados; Davi cuidará do FSRS.

## Pedido curto

“Faz a aula X”, “continua”, `/deck-aula X` ou só o nome da aula = executar o roteiro inteiro até o deck entregue (instalado **sem Tab**, gates duros 100%, pacote da UC, sync) e relatar no formato do MEMORY §11. Com revisor independente de autorais autorizado em 25/10, sem plano para aprovar, sem pedir permissão, sem parar no meio. **Desde 16/10 noite (F-20261016-CLAUDE-11): rodar as aulas em sequência, cada uma pelo pipeline inteiro, até Davi pedir para parar**; feedback que chegar é aplicado antes do deck seguinte. Plano vigente: [PLANO-ANKING-PRIMEIRO](flashcards/projeto/PLANO-ANKING-PRIMEIRO-2026-10-15.md). Tabs: o Codex gera quando Davi pedir.

Antes do próximo E0, conferir a rodada de 03/11 em `arquivos-trabalho/comentarios-2026-11-03/RESULTADO.md`: as duas pendências identificadas não são correções concluídas. Coletar comentários novos no Anki e aplicar o fluxo de sete passos aos novos pedidos; não reabrir os 30 casos já fechados sem mudança posterior de Davi.

## Limites que não mudam

- Davi estuda no Anki enquanto o executor trabalha: nunca tocar a nota em tela nem irmãos; escrita só por `nebli.decks.escrita()`; sync quando ele estiver ocioso.
- Outro executor (Claude ou Codex) trabalha em paralelo: reivindicar a aula no ESTADO-ATUAL antes; não mexer no que ele reivindicou; reler antes de gravar.
- Preservar originais AnKing, IDs/histórico, comentários, marcas e suspensões pessoais. Não apagar notas sem autorização de Davi e backup. Arquivar documentos superados em `arquivo/` com hash.
- Feedback novo: literal em FEEDBACKS → regra **reescrita no lugar** no MEMORY (sem acrescentar camada) → check no lint/gate quando mecanizável.
- Não fabricar leitura, busca, teste ou revisão. Gate aprovado não prova julgamento.
- **AnKing-primeiro com gates duros** (MEMORY §5): busca nos três caminhos em todos os acervos, `busca/cobertura.tsv`, autoral só para lacuna provada, **20% dos cards** (30% com `AUTORAL_EXCECAO`; acima disso quando a aula exige, com todo autoral no mapa — o teto nunca corta conteúdo da aula, F-20261029-CLAUDE-02), **todo AnKing do conteúdo da aula entra, sem teto de cards** (`PIPELINE_VERSAO = 9`, `SECOES_DA_AULA`) e relido contra os ANTI-EXEMPLARES. O `apply` recusa instalar sem isso.

## Outras rotas (só sob pedido)

**“Revisão pós-prova da UC/prova X”** → [REVISAO-POS-PROVA](flashcards/projeto/REVISAO-POS-PROVA.md): investigar fontes + deck vivo, preparar sugestões completas e aguardar aprovação de Davi antes de qualquer mudança no Anki. Não acionar a fila de aulas.

Índice do projeto: [README.md](README.md). Pedido explícito de “E1 + cards” (E1 + deck) inclui a E1: `didatica/E1.md`. Cadernos: `banco/CLAUDE.md` e `ROLES.md`. Typst: `typst-template/CLAUDE.md`. Site, liga e Etimologia: preservar.
