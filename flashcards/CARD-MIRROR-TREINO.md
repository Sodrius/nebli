# CARD-MIRROR-TREINO — protocolo de treino de geração de cards

> **Pedido do Davi (2026-07-12):** "gerar 50 cards de algum conteúdo só pra você aprender a gerar cards como os do AnKing, com o conteúdo das lacunas — daí você fica rodando pra aprender, até ser realmente indistinguível." Este é o processo repetível. Depende do loop adversarial de `CARD-MIRROR-PLANO.md` e alimenta `CARD-MIRROR-RUBRICA.md`.

## Objetivo
Treinar a **geração** (não só o conserto) de NEBLIcards no estilo AnKing, usando um lote grande (~50) como campo de prática. Os cards de treino são **sandbox** — vivem em `flashcards/treino/<topico>-treino.json`, **não** entram no deck vivo (respeita o gate B2: sem E1, não vira deck-aula). O produto do treino é a **habilidade destilada na rubrica**, não os 50 cards.

## Por que 50 e por que "das lacunas"
- **Volume** dá variedade de forma (afirmação-cloze, pergunta-fato, C/E, mnemônico, multi-cloze) — o discriminador acha padrões que 5 cards escondem.
- **Conteúdo de lacuna** = fatos FMUSP/conceituais que o AnKing cobre mal (contagem, ordem, "por quê") OU um tema rico onde o AnKing tem set grande pra comparar. O treino aprende **forma**, então serve tema com muitos cards AnKing (comparação farta).

## Os 6 passos de uma rodada de treino
1. **Escolher tema** com set AnKing rico (probe: `findNotes "<tema>"` ≥ ~80 cards) e pegar a **imagem-mãe** (mais compartilhada) + amostra de 12–15 cards reais.
2. **Gerar N cards** em `flashcards/treino/<tema>-treino.json`, aplicando TODA a `CARD-MIRROR-RUBRICA.md`: EN, cloze single curto no token de maior valor, frente ~10–20 palavras, Extra **fragmento telegráfico** (não prosa), sem travessão/aspas curvas/referência a banca, imagem-mãe reusada com crédito herdado.
3. **Lote cego**: amostrar K NEBLI + K AnKing reais (mesmo tema), embaralhar, remover selo/tag, numerar; chave à parte.
4. **Discriminar**: rodar o agente `card-mirror` (ou `claude` genérico com o prompt do card-mirror). Coletar acurácia + tells.
5. **Refinar em lote**: corrigir o(s) tell(s) recorrente(s) em TODOS os cards de treino de uma vez (não card-a-card); registrar cada tell novo na rubrica.
6. **Repetir 3–5** até o discriminador cair a ~chance E declarar chute. Gravar a curva de convergência em `arquivos-trabalho/card-mirror-treino-<tema>.md`.

## Critério de parada
Discriminador ≤ ~55–60% de acurácia **e** ≥1 falso-positivo (confunde AnKing real com NEBLI) **e** veredito "chute/≈ indistinguível". Resíduos inerentes ao conteúdo (número que o AnKing não carda) são aceitos e anotados, não perseguidos.

## Colheita do treino
- Todo tell novo → linha na rubrica (vira regra permanente).
- Quando a rubrica estabilizar (uma rodada de treino nova passa de primeira, sem tell novo), converter em `lint_neblicard.py` (checagem determinística pré-inserção) e considerar o padrão "aprendido".
- Só então os NEBLIcards de produção (com E1 + gate) herdam a garantia de nascer nativos.

## Log de treinos
| Data | Tema | N | Rodadas | Acurácia final | Tells novos → rubrica |
|---|---|---|---|---|---|
| 2026-07-12 | glicogênio | 50 | 3 | **46% (abaixo do acaso); 0/12 pegos; discriminador confessou indistinguível** | crédito Physeo (string exata); imagem por subtópico; vocabulário de formato AnKing |
| 2026-07-12 | pentoses+radicais (com resumo) | 50 | **1 (de primeira!)** | **42% (abaixo do acaso); 0/12 pegos; 2 falsos-positivos** | crédito casado à FONTE da imagem (Physeo≠OpenStax≠Flickr) |

### Pentoses — ACERTOU DE PRIMEIRA (prova de transferência)
Aplicando a rubrica inteira de saída, os 50 cards já nasceram indistinguíveis: **rodada 1 = 0/12 pegos, 42% de acurácia, 2 falsos-positivos** (o discriminador só marcou como NEBLI 2 cards AnKing minimalistas — por *ausência* de crédito, e errou os dois). Glicogênio precisou de 3 rodadas; pentoses, de 1 — o aprendizado ficou no arquivo, não na conversa. Conteúdo ancorado na E1 de `bioq-20-pentoses-radicais-livres`. Novo tell aprendido: **a string de crédito casa com a FONTE da imagem** — Physeo → `Image licensed by Physeo… Purchase full access here.`; OpenStax → `Photo credit: OpenStax, CC BY 4.0`; foto de esfregaço → `Photo credit: Ed Uthman, CC BY 2.0, via Flickr`. Reusar imagem de subtópico A com crédito de subtópico B seria o tell.

### Treino glicogênio — CONVERGIU (3 rodadas)
Curva: **R1** 15/9 distinguível (tell = crédito ausente + imagem errada por subtópico) → **R2** discriminador confuso, 3 falsos-positivos, pegou 1/12 (tell residual = a string de crédito estava pela metade) → **R3** completado o boilerplate Physeo exato (`… used with permission. Purchase full access here.`): **0/12 pegos, 46% de acurácia, falso-positivo num AnKing real, e confissão de indistinguibilidade.** Tells destilados na `CARD-MIRROR-RUBRICA.md` (§ Treino glicogênio + § Meta — hierarquia de tells). Cards finais: `flashcards/treino/glicogenio-treino.json` v2. **Padrão de geração considerado APRENDIDO** → próximo passo natural: `lint_neblicard.py` (guarda determinística).
