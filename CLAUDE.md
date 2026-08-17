# CLAUDE.md — execução canônica do NEBLI

Este arquivo descreve **como executar** o pipeline. Não cria nem substitui regras pedagógicas.

## Regra de isolamento da E1

A reforma v13 é uma reforma **dos flashcards e do backend de entrega**. Ela não altera o contrato, a voz, a profundidade, a estrutura, a calibração ou a qualidade visual da E1.

A E1 é produzida e congelada **antes** de qualquer leitura de `FLASHCARDS.md` ou `EXEMPLARES-CARDS.md`. Regras de seleção de cards, ganho da aula, orçamento de cards ou formato APKG nunca podem reduzir, resumir, reorganizar ou contaminar a E1.

Para produzir a E1, leia e aplique integralmente, nesta ordem:

1. `docs/canon/E1.md`;
2. as categorias de `EXEMPLARES.md` exigidas por `docs/canon/E1.md`;
3. os exemplares UC02 indicados por `docs/canon/E1.md`;
4. `ANTI-EXEMPLARES.md` nos sintomas relevantes;
5. `didatica/estudo-didatica-tom-dialogal.md` e `didatica/ajustes-finos-recentes.md` quando indicado pelo contrato.

A matriz fonte → E1 continua cobrindo a aula inteira conforme `docs/canon/E1.md`. Conteúdo que depois for classificado como pré-requisito, revisão, contexto, exemplo ou menção para fins de **deck** não é automaticamente excluído da E1. A E1 continua autocontida, didática e completa.

Somente depois de a E1 passar pelas quatro revisões canônicas e ser congelada é permitido abrir as regras de flashcards.

## Autoridades dos flashcards

Depois de congelar a E1, leia:

1. `FLASHCARDS.md` — regras de seleção e qualidade dos cards;
2. `EXEMPLARES-CARDS.md` — exemplos e anti-exemplos dos cards;
3. `config/pipeline.json` — parâmetros mecânicos ativos.

Não usar `MEMORY.md`, planos antigos, documentos legacy, decks anteriores ou contexto pessoal para decidir cards.

## Entradas permitidas para seleção de cards

- materiais da aula atual;
- E1 já congelada a partir desses materiais;
- planilha mestra, usada para posição curricular e aulas anteriores relevantes.

Não consultar decks antigos para inferir o que o usuário já estudou.

## Fluxo v13

1. Identificar UC, prova, componente e aula na planilha mestra.
2. Ler **todos** os materiais da aula.
3. Construir a matriz fonte → E1 e produzir a E1 conforme `docs/canon/E1.md`, com a calibração obrigatória pelos exemplares e didática canônicos.
4. Executar as quatro passadas da E1: fonte → E1, aluno inicial zero, didática/voz e PDF visual. Corrigir todas as pendências e **congelar a E1**.
5. Só agora ler `FLASHCARDS.md` e `EXEMPLARES-CARDS.md`.
6. Extrair `curriculum_context` da planilha mestra (`current_lesson` + `prior_lessons` relevantes).
7. Classificar os conceitos da aula conforme `FLASHCARDS.md` e preencher a matriz de ganho em `release_gate.concepts[]`.
8. Rodar o gate do ganho da aula antes da autoria:
   `python flashcards/scripts/validar_ganho_aula.py <deck-data.json>`
9. Congelar o núcleo de retenção e o `card_budget_hard_max`.
10. Autorar somente os cards autorizados pela matriz.
11. Executar o passe card → E1 previsto em `docs/canon/E1.md` **apenas para aprofundamentos aceitos do mesmo mecanismo**. Se esse passe alterar a E1, repetir as quatro revisões e congelá-la novamente. Ele nunca autoriza enxugar a E1 para caber no deck.
12. Validar 100% dos cards:
   `python flashcards/scripts/validar_deck_card_a_card.py <deck-data.json> --out <validation.json>`
13. Fazer a revisão final do conjunto depois da última alteração.
14. Finalizar a entrega:
   `python flashcards/scripts/finalizar_entrega_canonica.py --slug <slug> --deck-data <deck-data.json> --validation-report <validation.json> --out-dir <pasta>`
15. Entregar somente os artefatos visíveis finais.

## Saída canônica

Cada aula entrega:

- `<Aula> - E1.pdf`;
- `<slug>.apkg` pronto para importar diretamente no Anki/AnkiDroid.

O backend canônico é **APKG offline**. Companion, manifesto AnkiDroid e AnkiConnect não fazem parte do fluxo normal.

O APKG deve ser gerado por `flashcards/scripts/exportar_apkg_canonico.py` e reaberto/auditado por `flashcards/scripts/audit_apkg.py` antes da entrega.

## Regras operacionais importantes

- E1 e deck têm contratos diferentes: completude da E1 não implica cardificação, e exclusão do deck não implica exclusão da E1;
- não ler regras/few-shots de flashcards antes de congelar a primeira versão revisada da E1;
- não escrever cards durante a primeira leitura;
- não criar card antes de a matriz de ganho estar classificada;
- não alterar cards depois da validação sem gerar novo relatório;
- regressões de feedback fazem parte da CI obrigatória;
- qualquer falha no gate de ganho, validação card-a-card, release da E1 ou auditoria APKG bloqueia a entrega;
- `card_key` é identidade estável: correções de conteúdo não devem criar uma nova identidade lógica para o mesmo card.

## Fonte de verdade

Se houver conflito:

1. `docs/canon/E1.md` governa **exclusivamente a E1**;
2. `FLASHCARDS.md` governa **exclusivamente política dos cards**;
3. `EXEMPLARES-CARDS.md` governa exemplos de cards;
4. `CLAUDE.md` governa a ordem operacional e os artefatos;
5. `config/pipeline.json` e os validadores governam invariantes mecânicos.

Nenhuma regra de flashcards tem precedência sobre `docs/canon/E1.md` na produção da E1.