# PLANO — Imagens na explicação (Extra) dos NEBLIcards

> Criado 2026-07-13. Davi: "ainda sinto falta de imagens nas explicações — em MUITOS casos cabem (conceito que pode ser visualizado). Aprenda quando colocar, explorando cards de outros decks com imagem na explicação + a explicação, pra copiar." Este é o plano pra tocar amanhã.

## 1. O achado (por que isso importa) — medido, não opinado

Contei via AnkiConnect quantos cards têm `<img>` **no campo Extra**:

| Deck | Total | Extra com imagem | % |
|---|---:|---:|---:|
| **AnKing Step Deck** | 28.650 | 16.284 | **57%** |
| Referências Externas::Histology | 1.667 | 1.651 | **99%** |
| 100 Concepts (Dorian) | 244 | 227 | **93%** |

**Conclusão:** a imagem no Extra não é enfeite — é o **default AnKing**. Mais da metade dos cards e quase 100% dos de histologia/clínica têm imagem na explicação. Os meus NEBLIcards P3 saíram quase todos com Extra só-texto. É a maior lacuna de craft que sobrou depois do rebuild EN.

## 2. O que a imagem do Extra É (visto de perto, 2 imagens reais abertas)

Abri imagens reais de Extra do AnKing:
- **Capilar (OpenStax):** diagrama limpo rotulado do *leito capilar* — arteríola, esfíncter pré-capilar, metarteríola, canal de escoamento, anastomose AV. **Mostra exatamente o que o card cobra.**
- **Fluxo do coração:** esquema de setas câmara→câmara (VD→AP→pulmão→AE→VE→aorta) + coraçãozinho rotulado no canto. **Processo/fluxo desenhado.**

Regra destilada: **o Extra image mostra a própria coisa que o card testa**, como diagrama rotulado / micrografia / foto clínica — reforço visual do recall, não decoração.

## 3. QUANDO colocar imagem no Extra — rubrica de decisão (concept → image)

Pergunta-gatilho por card: **"esse conceito tem forma no espaço / uma cara reconhecível?"** Se sim → imagem no Extra. Mapeamento por tipo de conceito (derivado da amostra real):

| Tipo de conceito | Põe imagem? | Que imagem | Fonte típica |
|---|---|---|---|
| Estrutura anatômica / relação espacial | **SIM** | atlas/line-art rotulado | OpenStax, Netter (Dope), BlueLink |
| Histologia (célula, tecido, lâmina) | **SIM (quase sempre)** | micrografia H&E | LLU, Junqueira, histologyguide |
| Processo / via / fluxo (cadeia de passos) | **SIM** | esquema de setas/fluxograma | OpenStax, Servier |
| Morfologia / achado patológico | **SIM** | foto clínica / gross / radiografia | Wikimedia (Heilman), Frontiers |
| Comparação (A vs B) | **SIM** | figura lado-a-lado | OpenStax, Sketchy-style |
| Número puro / razão / definição verbal | **NÃO (ou genérica)** | — deixa Extra texto | — |
| Regra/mnemônico sem forma | NÃO | — | — |

Heurística de piso: **se o card tem uma estrutura, tecido, órgão, via ou achado visível no enunciado → tem que ter imagem no Extra.** Só escapam os puramente abstratos (razão L/E, "o que é um antígeno").

## 4. COMO fazer (o craft — copiar o AnKing)

1. **Imagem-mãe por SUBTÓPICO, reusada.** O AnKing usa a MESMA imagem no Extra de todos os cards irmãos de um subtópico (ex.: todos os cards do leito capilar reusam o diagrama OpenStax do leito capilar). Barato, consistente, e já fica em cache no device. → montar um **mapa subtópico → imagem-mãe** por aula.
2. **Reusar as figuras que JÁ baixei pro IO como imagem-mãe do Extra.** As figuras OpenStax que virei IO (neurulação, sistema linfático, e a do leito capilar) servem *também* de imagem-mãe de Extra dos cards de texto do mesmo subtópico. Uma figura, dois usos (IO + Extra).
3. **Linha de crédito sempre**, casada com a fonte real (`Photo credit: OpenStax, CC BY 4.0`; `Photo credit: <autor>, CC BY-SA X.X, via Wikimedia Commons`). Ver regra de crédito em `flashcards/CARD-MIRROR-RUBRICA.md`.
4. **Largura ~400px** (o `build_card.py` já normaliza pra ≤600 e reencoda com nome hasheado — assinatura AnKing).
5. **Texto do Extra continua telegráfico** OU explicativo (feature deliberada do Davi) — a imagem entra ABAIXO do texto, com `<br><br>`. Os dois convivem (o build já faz isso).

## 5. Tooling — o que muda (e o que já existe)

- **`build_card.py` JÁ suporta Extra com imagem.** O schema tem `images{}` (por chave, com file/url + credit) e cada card tem `image: "<chave>"`. Eu simplesmente **não populei** isso no rebuild P3. A mudança é **editorial** (decidir quais cards recebem imagem + achar a imagem-mãe), não de código.
- **A construir (pequeno):** `mapa-imagem-mae-<slug>.json` por aula (subtópico → arquivo/URL + crédito). O `build_card.py` lê e aplica.
- **Lint opcional:** estender o futuro `lint_neblicard.py` pra **flaggar card cujo enunciado tem substantivo-estrutura mas Extra sem `<img>`** — pega o "esqueci a imagem" automaticamente.
- **Loop de aprendizado:** continuar minerando pares (Extra-texto + imagem) reais do AnKing pra `flashcards/EXEMPLARES-CARDS.md` — few-shot de "quando e que imagem", pra eu copiar cada vez melhor. Amostra inicial em `arquivos-trabalho/_extra-img-samples.json`.

## 6. Plano de execução (amanhã)

**Retrofit P3 (aplicar aos 8 decks já feitos):**
1. Por aula, listar os subtópicos visualizáveis (rubrica §3) e escolher 1 imagem-mãe cada (reusar as OpenStax do IO + puxar de LLU/Dope/OpenStax/Wikimedia o que faltar).
2. Gravar `mapa-imagem-mae-<slug>.json`.
3. Rodar um passe que **anexa a imagem-mãe ao Extra** dos cards do subtópico (novo helper `add_extra_image.py`, ou re-rodar build com o campo `image` populado; para os já aplicados, um `updateNoteFields` do Extra concatenando `<br><br><img…>+crédito`).
4. Re-exportar + sync.

**Forward (todo deck novo):** a rubric §3 vira parte do `/deck-aula` — todo card visualizável nasce com imagem-mãe do subtópico. Meta declarável: **≥ metade dos cards de uma aula de anato/histo com imagem no Extra** (bench AnKing = 57%; histo = ~99%).

**Prioridade de retrofit (maior ganho primeiro):** histologia (vasos, órgãos linfáticos, tecido nervoso — onde AnKing é ~99% imagem) → anatomia (coração, vasos) → embrio (já tem IO; anexar esquemas ao Extra dos cards de texto).

## 7. Métrica de sucesso
Rodar de novo a contagem `Extra:re:<img>` nos decks NEBLI e chegar perto do bench: **anato/histo ≥ 50-60% dos cards com imagem no Extra**, cada uma mostrando a própria coisa que o card cobra, com crédito. Hoje estamos perto de 0%.
