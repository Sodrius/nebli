<!-- Razão-mestra da curadoria AnKing v12 por aula.
     Este arquivo é o AVISO VIVO: mostra, a cada momento, quais cards já foram
     dessuspendidos no deck do Davi, por aula, para ele poder AJUSTAR.
     Atualizado automaticamente por aplicar_curadoria_anking.py.
     Método: flashcards/CURADORIA-ANKING.md -->

# Curadoria AnKing v12 — razão-mestra por aula

Revisão espaçada de longo prazo: cada aula do NEBLI vira um bloco de **30–50 cards muito bem curados** do AnKing v12, dessuspendidos no deck e marcados com a tag-âncora `NEBLI::<slug>`. Este documento é o painel de controle — mostra o que já está no deck e onde ajustar.

**Regime de estudo (canônico):** 150 revisões/dia faça chuva faça sol · **25 cards novos/dia** (sustentável). Fixado no deck por `python flashcards/scripts/configurar_ritmo_anking.py` (new/day=25, rev/day=150) — não importa quantos cards cada aula dessuspende, só 25 novos afloram por dia. Os 25 são introdução; as 150 revisões enchem conforme os blocos `NEBLI::` maturam.

**Fila pendente-gerado:** conceito-chave da E1 sem card real bom no AnKing entra como `PENDENTE-GERADO` no manifesto + `arquivos-trabalho/cobertura-<slug>.json` — enfileirado para card NEBLI cloze gerado numa **sessão futura de calibração** (não gerar antes de destilar/validar o padrão de bom card; ver `calibrar-antes-de-gerar-cards`).

## Como ajustar um bloco no Anki
No **Browse** do Anki, digite a tag-âncora da aula:
- `tag:NEBLI::anato-06-circulatorio-linfatico-II` → vê exatamente os cards daquela aula.
- Tirou um card? `Ctrl+J` re-suspende (não apaga). Quer ver os suspensos: `tag:NEBLI::<slug> is:suspended`.
- Para reverter uma aula inteira: `python flashcards/scripts/aplicar_curadoria_anking.py <slug> --reverter`.

## Estado das aulas

| Aula (slug) | UC/Prova | Status | #cards | Dessusp. em | Cobertura AnKing | Lacunas → fonte | Tag-âncora |
|---|---|---|---|---|---|---|---|
| bioq-glicogenio | UC0?/P? | aplicado (card-a-card) | 68 | 2026-07-05 | — | — | `NEBLI::bioq-glicogenio` |
| bioq-lipideos (cetona/colesterol) | UC02/P? | aplicado (lote1, tag-level) | 42 | 2026-07-02 | — | — | (por tag FirstAid `…40_Ketone_bodies` · `*Cholesterol_Synthesis`) |
| bioq-20-pentoses-radicais-livres | UC02/P4 | aplicado (card-a-card) | 63 | 2026-07-07 | 7/13 (5 parciais, 1 lacuna) | 1.1/1.3/2.1/2.3/2.4/2.5 → slide + E1 | `NEBLI::bioq-20-pentoses-radicais-livres` |
| bioq-aminoacidos-ureia | UC02/P? | aplicado (lote1, tag-level) | 48 | 2026-07-02 | — | — | (por tag FirstAid `…23_Urea_cycle`) |
| bioq-dna-mutacao-reparo | UC02/P? | aplicado (lote1, tag-level) | 56 | 2026-07-02 | — | — | (por tag FirstAid `…07_DNA_repair` · `08_Mutations`) |
| bioq-dna-recombinante | UC02/P? | aplicado (lote1, tag-level) | 35 | 2026-07-02 | — | — | (por tag FirstAid `03_Laboratory_Techniques…`) |
| histo-10-tecido-nervoso | UC02/P3 | aplicado (lote1, tag-level) | 58 | 2026-07-02 | — | — | (por tag FirstAid `…01_Cells_of_the_nervous_system`) |
| histo-09-vasos-sanguineos-linfaticos | UC02/P3 | aplicado (lote1, tag-level) | 16 | 2026-07-02 | — | — | (por tag FirstAid `07_Cardiovascular::02_Anatomy::*Blood_Vessels`) |
| anato-05-circulatorio-linfatico-I | UC02/P3 | aplicado (lote1, tag-level) | 26 | 2026-07-02 | — | — | (por tag FirstAid `07_Cardiovascular::02_Anatomy::01_Heart_anatomy`) |

| anato-06-circulatorio-linfatico-II | UC0?/P? | aplicado (card-a-card) | 42 | 2026-07-04 | 5/8 COBERTOS | 1.1/2.1/3.2 parciais → slide+Netter | `NEBLI::anato-06-circulatorio-linfatico-II` |

> **⚠ DECK ZERADO em 2026-07-03.** Os 336 cards do lote1 (9 linhas acima) foram **re-suspensos** e marcados `NEBLI::zerado::2026-07-03` — não estão mais ativos. Reverter tudo: `python flashcards/scripts/zerar_deck_anking.py --reverter --data 2026-07-03`. **Único bloco ATIVO agora: ANATO-06 (49 cards).** Reconstrução por conteúdo de prova em andamento.

## Notas
- As 9 primeiras linhas vêm do **lote1** (`arquivos-trabalho/dessuspender-uc02-lote1.md`), aplicado por tag inteira do FirstAid, antes do método de curadoria card-a-card existir. Não têm manifesto `<slug>.md` nem tag-âncora `NEBLI::`. Quando forem re-curadas pelo método novo, a linha é atualizada e ganha a tag-âncora.
- Deixados de fora de propósito no lote1 (Davi quer enxuto): aminoacidopatias, DNA replicação, transcrição/tradução, hiperlipidemia, drogas hipolipemiantes, neurotransmissores/dermátomos.
- Entradas novas (a partir do método card-a-card) trazem `#cards` reais, `%cobertura` e `lacunas→fonte` preenchidos pelo manifesto da aula.
| biomol-25-mutacao-reparo-recombinacao | UC0?/P? | aplicado (card-a-card) | 55 | 2026-07-05 | — | — | `NEBLI::biomol-25-mutacao-reparo-recombinacao` |
| bioq-21-lipideos-rotas | UC0?/P? | aplicado (card-a-card) | 106 | 2026-07-05 | — | — | `NEBLI::bioq-21-lipideos-rotas` |
| bioq-23-aminoacidos-ureia | UC0?/P? | aplicado (card-a-card) | 135 | 2026-07-05 | — | — | `NEBLI::bioq-23-aminoacidos-ureia` |
| biomol-26-dna-recombinante-pcr | UC0?/P? | aplicado (card-a-card) | 34 | 2026-07-05 | — | — | `NEBLI::biomol-26-dna-recombinante-pcr` |
| embrio-gastrulacao-neurulacao | UC02/P3 | ⏳ seleção feita, APPLY PENDENTE (sem Anki vivo) | ~35-45 est. | 2026-07-10 | 6/12 COBERTOS · 4 parc · 2 lac | 1.4 EMT / 3.2 dobramento → slide+Moore | `NEBLI::embrio-gastrulacao-neurulacao` |
