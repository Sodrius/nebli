# Curadoria de cards — bioq-26-controle-hormonal (Controle Hormonal)

**Data:** 2026-08-09 · **Fonte do deck:** 100% NEBLIcards autorais.

## Por que não houve camada AnKing nem externos

Esta corrida rodou num ambiente **sem coleção Anki e sem AnkiConnect** (container remoto). As camadas 1 (AnKing curado) e 2 (decks externos: BlueLink, Dope, Histology/LLU, Dorian) dependem das duas coisas, então não puderam rodar. Consequência declarada: **todo subtópico foi tratado como lacuna tipo-a** e coberto por NEBLIcard autoral gerado da E1 desta corrida.

Isso é uma **inversão temporária da ordem de prioridade canônica** (AnKing → externo → autoral) e deve ser revisitada quando o export do AnKing estiver disponível: cards autorais que o AnKing já cobre melhor devem ser substituídos.

## Gates aplicados

| Gate | Resultado |
|---|---|
| Gate absoluto B2 (card ancorado na E1) | 88/88 — cada card carrega `e1_anchor` com a frase da E1 |
| `lint_neblicard.py` | 88/88 PASS (0 REJECT, 0 MIRROR) após 1 correção (`name_in_stem_head`) |
| `card-mirror` (lote cego 24: 12 meus + 12 AnKing reais) | 10/12 pegos · 2 passaram como AnKing · 0 falso-positivo · veredito "quase indistinguível" |
| Reescritas aplicadas pós-mirror | 8 frentes (mecanismo-no-stem, fato-não-clozado, cauda editorial, negação dupla) + linha de crédito de imagem |
| Formato R9 | 88/88 cloze único (`c1`), negrito, ≤3 palavras, Extra PT obrigatório |
| Imagem | 29/88 com figura no Extra (só onde a figura É o mecanismo) |

## Cobertura por subtópico (rubrica R6)

Todos os 14 subtópicos com nota 3 (fato + mecanismo). Total 88 cards — banda "aula grande" é 65–90, então está no teto: **poda esperada do Davi**, não lacuna.

| Subtópico | Cards |
|---|---|
| 1.1 Por que existe controle hormonal | 4 |
| 1.2 Classes químicas e solubilidade | 7 |
| 1.3 Alcance do sinal | 4 |
| 1.4 Receptor e transdutores | 5 |
| 1.5 Amplificação e desligamento | 5 |
| 2.1 Insulina: pré-pró → grânulo | 5 |
| 2.2 Célula beta como sensor | 11 |
| 2.3 Sinalização da insulina | 6 |
| 2.4 Glicogênio: controle recíproco | 6 |
| 2.5 Glucagon e adrenalina | 10 |
| 3.1 Receptor nuclear | 4 |
| 3.2 Tireoidianos | 8 |
| 3.3 Esteroides e eixo HPA | 5 |
| 3.4 Cortisol, Addison/Cushing, disruptores | 8 |

## Entrega

- `flashcards/cards-nebli/bioq-26-controle-hormonal.json` — fonte-verdade dos 88 cards
- `flashcards/decks-apkg/Controle Hormonal.apkg` — importável, note type **AnKingOverhaul real** (model id 1659130414530, extraído do próprio .apkg do Davi), deck `NEBLI::UC02::P4::Bioquímica::Controle Hormonal`
- `arquivos-trabalho/card-mirror-lote-bioq-26.md` + relatório do discriminador

## Pendências

- Reprocessar contra o AnKing v11/v12 quando o export estiver disponível: trocar autoral por curado onde o AnKing cobre melhor, e manter o autoral só nas lacunas reais.
- `montar_deck_aula.py` + `gate_deck_aula_completo.py --verify-anki` não rodaram (exigem Anki vivo) — o `.apkg` substitui o apply nesta corrida.
