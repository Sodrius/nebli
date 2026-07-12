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
| 2026-07-12 | glicogênio | 50 | 1 (em curso) | distinguível (15/9) | crédito Physeo ausente; imagem por subtópico; formato GSD |

### Estado do treino glicogênio (após rodada 1) — o que corrigir na rodada 2
Discriminador: **distinguível**, tell dominante = **ausência do crédito de imagem** nos meus cards. Aplicar em lote no `flashcards/treino/glicogenio-treino.json`:
1. **[CRÉDITO] Card que reusa imagem Physeo herda o crédito exato:** `Image licensed by Physeo and used with permission.` (é o que os irmãos AnKing carregam; a ausência foi o tell #1).
2. **[IMAGEM POR SUBTÓPICO] Cards de doença de depósito (GSD) usam a imagem-mãe de GSD** `8412e62f35b76d85fa69d4b05169138d.webp`, não a geral `efa5f694…`. Mapear imagem por subtópico, não uma só pro tema todo.
3. **[FORMATO GSD] Imitar o formato AnKing de GSD:** "X disease is also known as glycogen storage disease type {{c1::…}}" com multi-cloze + mnemônico embutido ("One Gierke", "ABCD: Andersen→Branching, Cori→Debranching").
4. **[VERSO] Manter glosa telegráfica** (Reversible. / Uses Pi, not water.) — passou bem; verso vazio também blendou. Não virar prosa.
Depois: re-rodar `card_mirror_blind.py glicogenio` → discriminar → repetir até o critério de parada.
