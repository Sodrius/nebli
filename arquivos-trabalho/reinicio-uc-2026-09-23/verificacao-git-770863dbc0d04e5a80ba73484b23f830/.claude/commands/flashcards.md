---
description: Alias do pipeline atual de deck-aula Anki; RemNote foi aposentado
argument-hint: <nome, link ou pasta da aula> [observações]
---

Argumentos recebidos: $ARGUMENTS

Este comando não gera os antigos 8 flashcards RemNote. Eles foram aposentados.

Execute exatamente o fluxo definido em `.claude/commands/deck-aula.md`, usando `$ARGUMENTS` como nome/link/pasta e observações da aula. A leitura canônica obrigatória é:

1. `flashcards/projeto/README.md`;
2. `flashcards/projeto/CALIBRACAO-ESCALA-V4.md` (prevalece sobre v3);
3. `flashcards/projeto/CONTRATO-DE-QUALIDADE.md` e `OPERACAO-CODEX-CLAUDE.md` no mesmo diretório;
4. `flashcards/projeto/EXECUCAO-DECK-AULA.md`, `ACERVOS-REFERENCIA.md`, `PUBLICACAO-POR-UC.md` no mesmo diretório e caso real mais parecido.

Entrega atual: APKG único da UC inteira, comprimido e sem flags no arquivo; E1/guia por aula. Rosa no Anki já indica candidatos pós-prova; manter é o padrão. Respeitar a limpeza manual: não restaurar pacotes ou notas históricas.

Se houver conflito com regras antigas de RemNote, `/resumo`, `FLASHCARDS.md`, loop Card→E1, E2/E3, cota fixa ou dessuspensão em massa, ignore as regras antigas para esta tarefa.
