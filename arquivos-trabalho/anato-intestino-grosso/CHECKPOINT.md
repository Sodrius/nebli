# CHECKPOINT — anato-intestino-grosso

**Aula:** Intestino grosso, reto e canal anal · Anatomia · Profa. Dra. Patrícia Castelucci (ICB/USP)
**Contexto:** UC-8 Digestório (Med5043), Prova 1, Turma B — aula em 10/08.
**Deck:** `NEBLI::Digestório::P1::Anatomia::Intestino grosso, reto e canal anal` (+ `::Optional`)
**Fase atual:** 11 — entrega.

## Fontes

| Fonte | Papel |
|---|---|
| `Alunos_ Intestino grosso_reto_canal anal_FINAL_2026.pdf` (27 p.) | escopo e figuras |
| `ROTEIRO_ intestino grosso_Final_2026.pdf` | lista de identificação da prática (22 alvos) |
| `Perguntas orientadoras Intestino Grosso.pdf` | 3 casos / 7 perguntas |
| `cronogramas/digestorio-uc8-med5043-2026.md` | UC, prova, componente, data |

Texto extraído em `fontes/`; páginas renderizadas em `paginas/`.

## Decisões

- **Porte grande**, teto de cards congelado em **50** antes da busca; entrega com **47**
  (32 núcleo · 10 apoio · 5 opcionais). Faixa de sanidade para aula grande: 35–55.
- **11 Image Occlusion** cobrem a lista inteira do roteiro prático, cada um como mapa
  coerente em `hide_all_guess_all`. Três deles usam **peça cadavérica real** do acervo da
  professora, porque a prática cobra reconhecimento sem as cores do atlas.
- **Regra de máscara aplicada em todos os IO:** cobre-se o **nome da estrutura e todo texto
  que a defina ou localize**, inclusive as legendas entre parênteses. A primeira versão
  deixava essas legendas visíveis; a revisão mostrou que "(espaço entre as colunas)" ou
  "6-10 cm, tecido linfoide" entregam a identidade e transformam reconhecimento em leitura.
  Fica visível só o que não nomeia nem define: crédito da fonte e título de orientação.
- **Rótulos rasterizados** dentro das pranchas (ex.: "Tênia omental" impressa na figura de
  Moore) foram mascarados junto — senão o mesmo nome ficaria visível em outro ponto do mapa.
- **Note type de IO trocado.** O `IO-one by one (AnKing)` não mostra imagem na frente
  ("please flip to the backside"), depende de JS de add-on e referencia mídia AnKing que
  não acompanha o pacote. Criado `IO NEBLI - Image Occlusion (mapa coerente)`, com as duas
  imagens já renderizadas (pergunta mascarada / resposta revelada).
- **Cloze:** 36 autorais, um único `c1`, uma ocorrência. Nenhum acima de 2 palavras.
- **E1 corrigida antes dos cards** em dois pontos: o gate de âncora literal reprovou os
  cards de Crohn e retocolite ulcerativa, que cobravam conteúdo do slide 17 ausente da E1;
  a E1 ganhou o box de doença inflamatória intestinal e os cards voltaram.

## Step 1

Aceitos (explicados na E1 antes do card): convergência das três tênias na base do apêndice;
anastomose portocava do canal anal (desenhada no slide 23).
Recusados: Hirschsprung, ponto de Griffiths, estadiamento/conduta do câncer colorretal,
e as nove regiões abdominais como card. Justificativas em `contrato-cobertura.json`
(`step1_decisions`).

## Revisão independente

Três revisores somente leitura rodaram sobre os artefatos completos. Nenhum BLOCK.
Correções aplicadas: card das válvulas anais (item do roteiro sem card), legendas do IO do
canal anal e do ceco que definiam a estrutura e entregavam a resposta, enunciado do IO dos
esfíncteres e recorte da figura das posições do apêndice. Um achado foi rejeitado com
evidência (suposto typo em `innervation`, inexistente no contrato). Destino de cada achado
em `revisao-independente.json`.

## Pendência real

O **índice privado do AnKing não é alcançável neste ambiente de execução**: ele existe no
Drive (`Anking/AnKing-index-v2`, 564 MB descompactado, pacote-fonte de 5,9 GB), mas o canal
MCP do Drive devolve arquivos em base64 pelo contexto do modelo. A ordem canônica
AnKing → externos → autoral não pôde ser executada no passo 1.

Feito no lugar: busca real no único corpus AnKing-derivado local
(`flashcards/decks-apkg/P3 - UC02 completo.apkg`, 247 notas) com famílias PT, EN e
mecanismo — 4 acertos de texto, todos de outras aulas, nenhum candidato. Todos os 47 cards
estão marcados `source: authored` com
`candidate_search.status = blocked_private_index_unreachable`, prontos para recuradoria.
Correção proposta em `RETROSPECTIVA-PROCESSO.md`.

## Artefatos

- `Intestino grosso, reto e canal anal - E1.pdf` (17 p.) ← `typst-build/anato-intestino-grosso/`
- `Intestino grosso, reto e canal anal.apkg` (47 cards, 29 mídias)
- `contrato-cobertura.json` · `relatorio-montagem.json` · `auditoria-apkg.json`
- `previews/` — 94 PNGs: pergunta e resposta de todos os 47 cards, renderizados em Chromium
- `revisao-independente.json` · `relatorio-final-anato-intestino-grosso.json`
- `io/` — imagem, manifesto e previews de cada Image Occlusion

## Próximo passo literal

Importar o `.apkg` no AnkiDroid e conferir na tela do celular os 11 IO e a fila de 25/dia.
