# CHECKPOINT — imuno-01-reconhecimento-inato

Pipeline: `e1-deck-v9` · backend `ankidroid` · schema `nebli-ankidroid-deck-v3`
Release gate: `nebli-e1-deck-release-v1`

## Metadados do Deck-Aula

| Campo | Valor | Como foi inferido |
|---|---|---|
| UC | UC03 | slide 1: "Unidade curricular-3 — Curso de Medicina" |
| Prova | P1 | primeira aula do bloco de Imunologia da UC03 (sequência "aula passada = quimiocinas/órgãos linfoides"); não há cronograma de UC03 no repo |
| Componente | Imunologia | tema e professor (José Alexandre M. Barbuto, Imunologia) |
| Nome curto | Reconhecimento inato | título do slide 1 |

Deck canônico: `NEBLI::UC03::P1::Imunologia::Reconhecimento inato`

## Fontes

- `PDF2024TAIMReconhSIInato_1.pdf` — 23 slides (renderizados em `figuras/imuno-01-reconhecimento-inato/`).
- Transcrição da aula em PDF — 44 páginas, texto integral do professor.
- Objetivos declarados no slide 2 (4 objetivos).

## Fases

| Fase | Estado |
|---|---|
| 1. Entrada/metadados | concluída |
| 2. Contrato de cobertura + orçamento | concluída — porte grande, `card_budget.hard_max = 40` congelado |
| 3. E1 + revisão independente | concluída — `typst-build/etapa1.typ` + PDF |
| 4. Atomização das recuperações | concluída |
| 5. Busca AnKing | **bloqueada pelo ambiente** — ver abaixo |
| 6. Autorais | concluída |
| 7. Visual/IO | concluída — 1 IO sobre slide 8 (localização subcelular dos ALR) |
| 8. `deck-data.json` | concluída |
| 9. Gate card a card | concluída — 39/39 |
| 10. Entrega canônica | concluída — `entregas/imuno-01-reconhecimento-inato/` |

## Resultado

- E1: 17 páginas (4 partes, 17 subtópicos, 6 figuras da aula interpretadas).
- Deck: **39 cards** — 37 nucleares + 2 opcionais; 38 autorais cloze + 1 Image
  Occlusion. Teto congelado em 40.
- Gate card a card: `expected = validated = passed = 39`, `failed = 0`.
- Release gate: 39 conceitos, 37 nucleares, 37 com cobertura ≥ 2.
- Entrega: `entregas/imuno-01-reconhecimento-inato/`.
- Falta somente o recibo do Companion no tablet
  (`installed_card_count == 39`), que não pode ser produzido deste ambiente.

## Decisão registrada: fonte AnKing indisponível nesta sessão

A ordem canônica de fonte é AnKing → deck externo → autoral. A resolução AnKing
do v9 acontece na coleção local do AnkiDroid (tablet) ou por índice privado
local; **nenhum dos dois existe neste ambiente de execução** (container remoto,
sem coleção, sem índice, e o canônico proíbe versionar AnKing no repo).

Consequência aplicada:

- nenhum card foi planejado como `source="anking"`, porque não seria possível
  validar a nota, o sibling e a renderização realmente selecionados (ERROS 46);
- nenhum card declara `anking_search_complete=true`, porque a busca não ocorreu;
- o deck-data declara `anking_source_availability.available=false` com motivo, e
  cada card autoral/IO registra `anking_search_status="source_unavailable"` mais
  `anking_upgrade_queries[]` — as consultas exatas que uma sessão com coleção
  deve rodar para promover o card a AnKing;
- o manifesto carrega esse bloco, de modo que a limitação fica auditável em vez
  de ser mascarada por evidência de busca fabricada.

Regra correspondente registrada em `ERROS.md` (item 52).

## Pendências para a próxima sessão com coleção AnKing

Rodar `anking_upgrade_queries` de cada card e promover a AnKing os que tiverem
nota adequada (a recuperação precisa ser a mesma, não tema vizinho). O restante
permanece autoral.
