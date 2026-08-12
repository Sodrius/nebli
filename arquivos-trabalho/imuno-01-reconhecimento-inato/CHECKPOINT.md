# CHECKPOINT — imuno-01-reconhecimento-inato

**Fase:** concluída (E1 congelada, deck validado, manifesto gerado).
**Data:** 2026-08-12 · pipeline `e1-deck-v9`.

## Identidade

`NEBLI::UC03::P1::Imunologia::Reconhecimento inato`

UC03 e componente vêm do slide de abertura ("Unidade curricular-3", Prof. José
Alexandre M. Barbuto). A prova foi confirmada pelo Davi como **P1** — o repo
registrava UC03 com prova/componente pendentes desde a curadoria da Radiologia.

## Fontes

- Slides: `PDF2024TAIMReconhSIInato_1.pdf`, 23 slides, extraídos para
  `figuras/imuno-01-reconhecimento-inato/slide-01..23.png`.
- Transcrição integral da aula (44 páginas) usada como nota do professor —
  `e1_review.notes_review_status = "covered"`.
- As tabelas de ligantes dos slides 16 e 17 são imagens: foram lidas da imagem e
  transcritas para a E1 com localização e origem do ligante.

## Artefatos

| arquivo | papel |
|---|---|
| `typst-build/etapa1.typ` + `resumindo.typ` + `main.typ` | E1 fonte (22 páginas) |
| `typst-build/main.pdf` | E1 compilada, hash no release gate |
| `_montar_deck_data.py` | monta o plano; editar aqui, nunca o JSON |
| `deck-data.json` | 52 cards, 36 conceitos |
| `validacao-cards.json` | **derivado** do deck-data |
| `entregas/imuno-01-reconhecimento-inato/` | os dois arquivos visíveis ao Davi |

## Resultado dos gates

- release gate `nebli-e1-deck-release-v1`: aprovado; 36 conceitos, 28 nucleares,
  28 cobertos; todas as âncoras conferidas literalmente contra a E1 fonte.
- lint de qualidade funcional: 0 problemas em 52 cards.
- gate card a card: `expected = validated = passed = 52`, `failed = 0`,
  teto 54.
- manifesto `nebli-ankidroid-deck-v3` gerado com 2 mídias embutidas (SHA-256).

## Composição do deck

50 autorais + 2 Image Occlusion. Distribuição por bloco da E1: 5 (recap e
contexto), 15 (famílias de PRR e ligantes), 15 (vias do TLR e inflamassoma),
17 (efetuação e citocinas) — proporcional ao peso dos slides.

IO 1 — mapa das vias do TLR (slide 18, recortado para retirar a legenda que
soletra NF-κB e IRF): máscaras sobre `NF-kB` e `IRFs`.
IO 2 — figura do NLRP3 (Schroder & Tschopp 2010, no slide 21): máscaras sobre
`P2X7` e `Pannexin-1`. Previews de pergunta e resposta renderizados e conferidos
visualmente; sem vazamento em nenhum dos dois.

## Procedência da busca AnKing

Todos os 52 cards em `anking_search_mode: "unavailable"`: a coleção AnKing vive
no AnkiDroid do tablet e não está ao alcance de uma sessão de planejamento. O
motivo está registrado card a card e a distribuição aparece em
`search.anking_search_modes` no manifesto. Ver
`arquivos-trabalho/DIAGNOSTICO-PIPELINE-2026-08-12.md`.

## Instalação

Primeira tentativa (2026-08-12) bloqueada pelo Companion:
`k22-io-vias IO gate: [io_mode_must_be_hide_all_guess_all]`. Rollback correto,
nada parcial ficou. Causa: o APK do tablet foi compilado do commit `942e665`
(#18) e é anterior à renomeação do token de IO feita no #19 — o deck estava
certo, o vocabulário é que era novo demais para o aparelho.

Manifesto regerado com `mode: hide_all_guess_all` (mesma regra: duas máscaras,
duas respostas coerentes; `io_mode_contract` registra o nome canônico). O gate
daquele APK foi reimplementado e rodado contra o manifesto novo: 52/52.

## Pendência

Instalar o manifesto regerado e conferir o recibo
(`installed_card_count == 52`). Enquanto o recibo não existir, a aula não está
fechada pela definição de pronto do canônico.

Quando o Companion do tablet for reinstalado a partir deste repo, atualizar
`config/pipeline.json → ankidroid.installed_companion.io_mode_token` para
`hide_two_guess_two` e registrar a data — só depois de um recibo real.
