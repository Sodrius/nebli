# CLAUDE.md — execução canônica do NEBLI

Este arquivo descreve **como executar** o pipeline. A política pedagógica da E1 continua em `docs/canon/E1.md`; a política pedagógica dos cards continua em `FLASHCARDS.md`.

## Princípio operacional

A corrida tem duas fases pedagógicas independentes e sequenciais:

1. **ensinar a aula** — construir e congelar a E1;
2. **reter o ganho da aula** — selecionar e fabricar os cards a partir da E1 aprovada.

Não usar critérios de seleção de cards para encurtar, simplificar ou excluir conteúdo necessário da E1.

## Fase A — E1

1. Identificar UC, prova, componente, número e título da aula na planilha mestra.
2. Ler todos os materiais da aula e inventariar objetivos, slides, blocos textuais, perguntas orientadoras, notas e informação visual relevante.
3. Ler `docs/canon/E1.md` integralmente.
4. Fazer a calibração **antes de redigir**:
   - categorias universais 1, 8 e 14 de `EXEMPLARES.md`;
   - categoria 17 de `EXEMPLARES.md`;
   - categorias temáticas pertinentes;
   - sintomas relevantes de `ANTI-EXEMPLARES.md`;
   - documentos didáticos indicados por `docs/canon/E1.md` quando aplicáveis;
   - pelo menos dois exemplares UC02 adequados dentre os apontados por `docs/canon/E1.md`.
5. Construir `source_to_e1_matrix` com uma linha por unidade relevante da fonte e congelá-la **antes do primeiro parágrafo**.
6. Produzir `main.typ`, `etapa1.typ` e `resumindo.typ` usando o template canônico.
7. Executar as quatro revisões obrigatórias:
   - fonte → E1;
   - aluno inicial zero;
   - didática/voz comparada aos exemplares;
   - PDF visual renderizado página por página.
8. Preencher evidência concreta da calibração e revisão no `e1_review`.
9. A E1 só congela com zero lacuna nuclear, zero ambiguidade aberta, zero lacuna de iniciante e zero defeito visual.

Nenhum card é autorado antes desse congelamento.

## Fase B — ganho da aula e cards

Somente depois da E1 aprovada:

1. Ler `FLASHCARDS.md`.
2. Ler `EXEMPLARES-CARDS.md`.
3. Extrair `curriculum_context` da planilha mestra (`current_lesson` + aulas anteriores relevantes).
4. Classificar os claims da aula por `learning_role` e preencher `release_gate.concepts[]`.
5. Rodar:
   `python flashcards/scripts/validar_ganho_aula.py <deck-data.json>`
6. Congelar o núcleo de retenção e `card_budget_hard_max`.
7. Autorar somente cards autorizados pela matriz de ganho.
8. Validar 100% dos cards:
   `python flashcards/scripts/validar_deck_card_a_card.py <deck-data.json> --out <validation.json>`
9. Fazer revisão independente do conjunto final, ligada ao hash exato do lote.

Para selecionar cards, usar somente materiais da aula atual, E1 aprovada e planilha mestra. Não consultar decks anteriores para inferir o que o aluno já estudou.

## Fase C — entrega

Finalizar com:

`python flashcards/scripts/finalizar_entrega_canonica.py --slug <slug> --deck-data <deck-data.json> --validation-report <validation.json> --out-dir <pasta>`

A saída visível é:

- `<Aula> - E1.pdf`;
- `<slug>.apkg` pronto para importar diretamente no Anki/AnkiDroid.

O backend canônico é APKG offline. Companion, manifesto AnkiDroid e AnkiConnect não fazem parte do fluxo normal.

O `.apkg` deve ser gerado por `flashcards/scripts/exportar_apkg_canonico.py`, reaberto e auditado por `flashcards/scripts/audit_apkg.py`. A entrega é bloqueada se a estrutura legada do pacote não for compatível com o schema aceito pelo importador atual do Anki.

## Fonte de verdade

Em caso de conflito:

1. `docs/canon/E1.md` governa a E1;
2. `EXEMPLARES.md`/`ANTI-EXEMPLARES.md` calibram a E1;
3. `FLASHCARDS.md` governa os cards;
4. `EXEMPLARES-CARDS.md` exemplifica os cards;
5. `CLAUDE.md` governa a ordem operacional;
6. `config/pipeline.json` e validadores governam invariantes mecânicos.

Uma declaração de revisão não substitui evidência. Se a E1, os cards ou o pacote mudarem depois da revisão correspondente, a evidência anterior deixa de valer.
