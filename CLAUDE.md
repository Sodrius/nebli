# CLAUDE.md — execução canônica do NEBLI

Este arquivo descreve **como executar** o pipeline. Não duplica regras pedagógicas.

## Autoridades

Antes de produzir cards, leia nesta ordem:

1. `FLASHCARDS.md` — todas as regras de seleção e qualidade;
2. `EXEMPLARES-CARDS.md` — exemplos e anti-exemplos;
3. `docs/canon/E1.md` — contrato da E1;
4. `config/pipeline.json` — parâmetros mecânicos ativos.

Não usar `MEMORY.md`, planos antigos, documentos legacy, decks anteriores ou contexto pessoal para decidir cards.

## Entradas permitidas para seleção de cards

- materiais da aula atual;
- E1 construída a partir desses materiais;
- planilha mestra, usada para posição curricular e aulas anteriores relevantes.

Não consultar decks antigos para inferir o que o usuário já estudou.

## Fluxo v13

1. Identificar UC, prova, componente e aula na planilha mestra.
2. Ler **todos** os materiais da aula antes de autorar cards.
3. Construir/revisar a E1 conforme `docs/canon/E1.md`.
4. Extrair `curriculum_context` da planilha mestra (`current_lesson` + `prior_lessons` relevantes).
5. Classificar os conceitos da aula conforme `FLASHCARDS.md` e preencher a matriz de ganho em `release_gate.concepts[]`.
6. Rodar o gate do ganho da aula antes da autoria:
   `python flashcards/scripts/validar_ganho_aula.py <deck-data.json>`
7. Congelar o núcleo de retenção e o `card_budget_hard_max`.
8. Autorar somente os cards autorizados pela matriz.
9. Validar 100% dos cards:
   `python flashcards/scripts/validar_deck_card_a_card.py <deck-data.json> --out <validation.json>`
10. Fazer a revisão final do conjunto depois da última alteração.
11. Finalizar a entrega:
   `python flashcards/scripts/finalizar_entrega_canonica.py --slug <slug> --deck-data <deck-data.json> --validation-report <validation.json> --out-dir <pasta>`
12. Entregar somente os artefatos visíveis finais.

## Saída canônica

Cada aula entrega:

- `<Aula> - E1.pdf`;
- `<slug>.apkg` pronto para importar diretamente no Anki/AnkiDroid.

O backend canônico é **APKG offline**. Companion, manifesto AnkiDroid e AnkiConnect não fazem parte do fluxo normal.

O APKG deve ser gerado por `flashcards/scripts/exportar_apkg_canonico.py` e reaberto/auditado por `flashcards/scripts/audit_apkg.py` antes da entrega.

## Regras operacionais importantes

- não escrever cards durante a primeira leitura;
- não criar card antes de a matriz de ganho estar classificada;
- não alterar cards depois da validação sem gerar novo relatório;
- regressões de feedback fazem parte da CI obrigatória;
- qualquer falha no gate de ganho, validação card-a-card, release da E1 ou auditoria APKG bloqueia a entrega;
- `card_key` é identidade estável: correções de conteúdo não devem criar uma nova identidade lógica para o mesmo card.

## Fonte de verdade

Se houver conflito entre documentos antigos e os arquivos acima, prevalecem:

1. `FLASHCARDS.md` para política de cards;
2. `EXEMPLARES-CARDS.md` para exemplos;
3. `CLAUDE.md` para execução;
4. `config/pipeline.json` e os validadores para invariantes mecânicos.
