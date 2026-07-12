# PLANO — Deck-prova P3 UC02 (rodar em conversa NOVA)

> Handoff 2026-07-12. Davi pediu o **deck-prova da P3 completo, sério e organizado** — o primeiro deck "de verdade" (os anteriores foram TESTE e não contam). Rodar numa conversa separada (a de origem ficou longa). Ritmo escolhido: **curar as 8 de enfiada e entregar o P3 fechado** (menos checkpoints).

## Escopo — 8 aulas (todas com E1; imuno e depuração ficam FORA, sem resumo)
Prova pelo cronograma `cronogramas/cronograma UC2 2026 v 1 de julho.pdf` (coluna "Cai em" → P3 = Histo/Anato/Embrio; 16/jul). E1 = fonte-verdade do gate B2 (typ no workspace OU PDF no Drive/resumos-gerados).

| # | Aula | Componente (Drive) | E1 |
|---|---|---|---|
| 1 | Anatomia circ/linf I (pt1) | Anatomia / 05 | `arquivos-trabalho/etapas-anteriores/anato-05-circulatorio-linfatico-I/etapa1.typ` |
| 2 | Anatomia circ/linf I (pt2) | Anatomia / 05 | Drive PDF "Sistema circulatório e linfático pt2 - Etapas 1 a 3" (+ typ `anato-05-sistema-linfatico`) |
| 3 | Anatomia circ/linf II | Anatomia / 06 | Drive PDF "Sistema circulatório e linfático II - Etapas 1 a 3" |
| 4 | Histologia dos vasos | Bio celular/tec / 08 | `.../histo-09-vasos-sanguineos-linfaticos/etapa1.typ` |
| 5 | Tecido nervoso | Bio celular/tec / 09 | `.../histo-10-tecido-nervoso/etapa1.typ` |
| 6 | Histologia dos órgãos linfáticos | Bio celular/tec / 10 | `.../histo-11-orgaos-linfaticos/etapa1.typ` |
| 7 | Embriologia I | Bio celular/tec / 11 | resumos-gerados/"Embriologia I - Etapas 1 a 3- ML.pdf" |
| 8 | Embriologia II e III | Bio celular/tec / 12 | resumos-gerados/"Embriologia II e III - Etapas 1 a 3 - ML.pdf" |

**FORA (sem E1, ficam sem resumo por decisão do Davi):** Distúrbios da imunidade (imuno-01), Funções de depuração (bioq-25).

## Processo por aula (SÉRIO — o padrão novo)
Para cada uma: busca AnKing por conceito (`descobrir_cards_por_conceito`) → Camada 2 keep/drop (perfil decoreba onde couber) → **gate B2** contra a E1 (nada de card órfão) → **NEBLIcards indistinguíveis** pras lacunas tipo-a (rubrica `CARD-MIRROR-RUBRICA.md`: imagem-mãe de irmão + crédito casado, verso telegráfico, EN) → **Revisor-completude** (agente Sonnet, 3 notas + patches) → aplicar em `NEBLI::UC02::P3::<Componente>::<Aula>`. Carga viável por aula (banda peso×rendimento, `FLASHCARDS.md`). AnKing intocado — só cópias no NEBLI.

## Entrega
- **Um `.apkg` por aula** → sobe pra pasta da aula no Drive (`subir_drive.py`, ver `DRIVE-ESTRUTURA.md`), nomeado `<Aula>.apkg`. **Componente, não prova** (o Drive é por componente).
- **Um `P3.apkg` combinado** (o deck-prova inteiro) — o Anki é por prova; salvar o combinado onde o Davi achar (sugerir pasta `UC02/` raiz ou uma pasta "Decks Anki"). Confirmar o destino com ele.
- Reportar: completude (3 notas E1×slide, E2×E1, cards×E1) + carga por aula + o que virou NEBLIcard.

## Regras que já valem (não reabrir)
- Drive headless via rclone `nebli-drive` (refresh_token; `DRIVE-ESTRUTURA.md`).
- Profundidade elevada + dial `profundidade` + blocos clínicos maiores + bloco roxo (`CLAUDE.md` § Profundidade).
- Estrutura Anki `NEBLI::UC::Prova::Componente::Aula`; AnKing 100% suspenso como referência.
- Bandeiras (vermelha explica+suspende / laranja re-julga / verde exemplar); Ctrl+1 consertado.
