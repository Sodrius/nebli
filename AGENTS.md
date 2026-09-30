# NEBLI — instruções de entrada

Para E1, cards, Anki, curadoria e arquitetura, ler primeiro `flashcards/projeto/README.md` e seguir a ordem: `MEMORY.md`, `flashcards/projeto/FEEDBACKS.md` e, na execução, `flashcards/projeto/EXECUCAO-DECK-AULA.md`. Isso vale para mensagem comum em toda nova sessão. As respostas de calibração já estão consolidadas; não pedir que Davi reensine suas preferências.

MEMORY é a única memória normativa dos decks. O pipeline padrão é **E1 + cards**, com exceções e estado na memória/fila. UC08: `flashcards/projeto/RECONSTRUCAO-UC08.md`; fontes/modelos: `flashcards/projeto/ACERVOS-REFERENCIA.md`. E1 quando aplicável: `didatica/E1.md`. Não usar divisão de tarefas, idioma ou ritmo de handoffs antigos. E2/E3 são histórico.

Todo feedback recebido por qualquer executor vai ao registro único nesta sessão. Atualizar a preferência em seu lugar no MEMORY; não espalhar regras pela fila. Aplicar melhorias às próximas entregas; alterar deck anterior só quando Davi pedir. Demonstrar aplicação dos critérios na revisão, não apenas leitura dos arquivos.

**Dois gates de todo deck novo (F-20260930-CLAUDE-16):** (1) autoral indistinguível do AnKing às cegas — uma frase que ensina o processo e oculta um nome, sem “;” juntando afirmações, ≤ ~20 palavras, frente e Extra em inglês; `python3 -m nebli.lint_cards <plan.json>` sem reprovação dura + amostra cega com `card-mirror`; (2) explicações do Tab geradas pela tag da aula (`python3 -m nebli.explicacoes gerar '"tag:NEBLI::<aula>"'`, nunca `deck:"NEBLI::..."` exato) e `resumo '"tag:NEBLI::<aula>"'` com `faltando: 0` e `desatualizada: 0` antes de entregar. Detalhes no MEMORY e no roteiro §3/§6. Antes de entregar, percorrer a tabela “Erros já cometidos” do MEMORY.

Preservar originais, estudo, edições, flags, suspensões pessoais e trabalho local não relacionado. Escrita Anki usa `nebli.decks.escrita()` e `arquivos-trabalho/ANKI-ESCRITA.lock`, conforme o roteiro. Auditoria/planejamento são somente leitura externa, salvo correção solicitada. Não restaurar artefatos limpos manualmente nem reclassificar a coleção toda.

Outras tarefas: `CLAUDE.md` e `MEMORY.md`. Regras de etimologia não governam cards médicos. Versões integrais e fila antiga em `flashcards/projeto/HISTORICO.md`; não são instruções atuais.
