# NEBLI — entrada de contexto do projeto

> **Atualização vigente de 25/09/2026:** após README, ler `flashcards/projeto/CALIBRACAO-2026-09-25.md` antes da v4. Azul (4) substitui rosa; acervo amplo e núcleo desejado de até 35 cards/aula são seleções distintas. Sem cor não significa núcleo. Auditoria e correções em `flashcards/projeto/AUDITORIA-2026-09-25.md`. O modo do lote continua só deck/sem upload. Não reaplicar scripts antigos com flags/seleções superadas.

Para tarefas de decks-aula, Anki, curadoria e arquitetura de flashcards:

0. **Lote em andamento (24/09/2026):** os decks da UC03 P2 e da UC08 P1 são divididos entre Claude e Codex pela fila `flashcards/projeto/FILA-UC03-P2-UC08-P1.md`. Leia o "Modo deste lote" (só deck, sem E1/guia; decks apagados refeitos do zero) O Codex faz **somente as aulas da "Fila do Codex"** (UC03 Patologia/Imunologia; UC08 Anatomia/Biologia Tecidual). Marque a aula antes de começar, use o lock `arquivos-trabalho/ANKI-ESCRITA.lock` para escrever no Anki e incorpore as "Dicas de Davi" registradas na fila. Bibliografia por matéria: README § Bibliografia por matéria.

1. Leia `flashcards/projeto/README.md` antes de propor regras ou agir.
2. Primeiro leia `flashcards/projeto/CALIBRACAO-ESCALA-V4.md` (30 respostas vigentes), `CONTRATO-DE-QUALIDADE.md` e `OPERACAO-CODEX-CLAUDE.md` no mesmo diretório. A v4 prevalece sobre a v3 e pilotos. Para executar uma aula, leia `flashcards/projeto/EXECUCAO-DECK-AULA.md`, `ACERVOS-REFERENCIA.md`, `PUBLICACAO-POR-UC.md` no mesmo diretório e o caso real mais parecido. V3 é histórico opcional. Para construir automação, leia `flashcards/projeto/ARQUITETURA.md` e `flashcards/projeto/IMPLEMENTACAO.md`.
   As decisões de `README.md` § “Decisões fechadas — não perguntar novamente” já foram respondidas pelo usuário; não as transforme novamente em questionário.
3. O formato AnKing-first do piloto foi aprovado. Melhorar cobertura dentro do escopo da aula, sem torná-la autossuficiente nem incluir recursivamente pré-requisitos.
4. Preserve originais AnKing, histórico, edições, bandeiras e suspensões pessoais. Pedidos de planejamento/auditoria não autorizam mutações externas.
5. Documentação é especificação; verifique o que foi efetivamente implementado antes de afirmar que o comando único funciona.
6. Última atualização: APKG único da UC inteira, comprimido e sem flags no arquivo, atualizado a cada aula; flags da coleção preservadas. Rosa já sinaliza candidatos pós-prova, mas padrão é manter; Davi decide suspender. Respeitar limpeza manual e jamais restaurar decks excluídos de recibos/pacotes antigos. Descobrir acervos externos dinamicamente, incluindo os novos. Instruções atuais do usuário prevalecem. A v1 em `arquivos-trabalho/arquitetura-nebli/` é histórica quando conflitar com a v2.

Para outras tarefas, consulte as instruções pertinentes em `CLAUDE.md` e o estado em `MEMORY.md`, sem aplicar regras especiais de etimologia aos decks médicos. Preserve mudanças locais não relacionadas.
