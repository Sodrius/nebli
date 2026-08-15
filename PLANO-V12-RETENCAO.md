# Plano v12 — deck de retenção, orçamento derivado e loop de feedback

> Escrito em 2026-08-15, depois da corrida `patologia-adaptacao-celular-acumulos` e da
> leitura dos comentários card a card no `.apkg` exportado. Alvo: `pipeline_version=e1-deck-v12`.
> Este arquivo é plano de execução, não canon. Cada fase termina com edição do canon
> correspondente em `docs/canon/` e do `config/pipeline.json`.

## O diagnóstico em uma frase

O pipeline v11 produz uma E1 boa e um deck que carda **a compreensão** da aula — princípio
organizador, mecanismo, relação causal — quando deveria cardar **o que precisa ser levado
adiante e não se deduz na hora da revisão**. O teto de 25 agravou isso: para caber, a ablação
cortou justamente o material específico (esteatose alcoólica, calcificação metastática,
melanina, antracose, glicogenoses) e manteve os cards genéricos, que são os que o Davi
marcou como inúteis.

Evidência direta, do `.apkg`:

- `c01` — "adaptação preserva a {{c1::viabilidade}}": *"conceitos altamente genéricos, que não
  são da aula em específico… só ocupam espaço"*.
- `c02` — "o que separa os desfechos é o {{c1::tempo}}": *"não adiciona nenhum conhecimento…
  relação meio esculambanhada"*.
- `pato01-c009`, `c013`, `c015`, `c018`: pedem **imagem no Extra**, **mais conceitos por card
  no enunciado e no comentário** e **hide all / guess all** para listas de três.
- Flags vermelhas sem comentário em `pato01-c002` e `c017` (interpretadas como "revisar").

E a evidência interna, de `flashcards/PESQUISA-BOM-CARD.md` (500 cards do AnKing dissecados):
86% single-cloze mas 14% multi-cloze **do mesmo fato**; frente com mediana de 17 palavras;
Extra em 83% dos cards, mediana 20 palavras, com mecanismo, discriminador ou mnemônico;
**47% com imagem**; 23% com hint no cloze. O nosso deck saiu com 0% de imagem no Extra,
0% de hint, 0% de multi-cloze e frentes de 25 a 35 palavras.

---

## Fase 0 — Destravar o ambiente e a reprodutibilidade

Sem isto, toda corrida repete trabalho manual e a auditoria visual continua sendo feita a olho.

1. **Hook de sessão** (`.claude/hooks`, via skill `session-start-hook`): instala `typst`,
   `pymupdf`, `pillow`, `numpy`, `zstandard` e confere as fontes do template. Hoje cada sessão
   web começa sem compilador.
2. **`typst-build/extrair_slides_transcricao.py`**, versionado: recebe os PDFs de transcrição,
   extrai as imagens embutidas, detecta a área útil do slide, remove faixa de título, webcam,
   e-mail de rodapé e logo, e emite `slide-*.png` mais o `MAPA_CONTEUDO.txt`. Foi quase metade
   do tempo da última corrida, feito em script descartável no scratchpad.
3. **`main.typ` deixa de ser ignorado** (`.gitignore`) ou passa a ser gerado por Tema Card via
   `gerar_main.py`. Hoje a corrida não se reconstrói a partir do repo.
4. **`flashcards/scripts/checar_ancoras.py`** e normalização de pontuação no
   `validar_release_e1_deck.py::_normalise`: âncora que atravessa `*negrito*,` falha hoje por
   causa de um espaço antes da vírgula. Custou duas rodadas.
5. **Scripts órfãos entram na `EXECUCAO.md`**: `precompile-check.py` antes de compilar,
   `auditar_pdf.py` + `auditar_pdf_visual.py` + `pos_pipeline_check.py` depois. O
   `auditar_pdf_visual.py` existe exatamente para pegar "Resumindo passando de 2 páginas" e
   "página com mancha < 40%" — os dois defeitos que caçamos a olho na última corrida. O gate
   passa a exigir a saída deles.
6. **Versão única na documentação**: `MEMORY.md` diz v10, `flashcards/DECK-AULA-PIPELINE.md`
   diz v9 e ainda manda buscar no AnKing antes de autorar (regra suspensa). Um
   `test_versao_docs.py` compara o que os `.md` afirmam com `config/pipeline.json`.

**Pronto quando:** uma corrida nova roda do PDF ao manifesto sem script ad-hoc, e o gate
recusa E1 sem relatório do `auditar_pdf_visual`.

---

## Fase 1 — Contrato de card v2 (o coração do problema)

### 1.1 Tipo de retenção declarado, de vocabulário fechado

Todo card passa a declarar `retention_type`, escolhido de uma lista que **não contém**
princípio, mecanismo geral nem relação organizativa:

| `retention_type` | o que é | exemplo desta aula |
|---|---|---|
| `entidade_nomeada` | nome próprio de estrutura, enzima, via, doença | tirosinase; lipase hormônio-sensível; ducto tireoglosso |
| `valor` | número, prazo, proporção, limiar | útero até 40× o volume; hemocromatose 1:200 a 1:500 |
| `discriminador` | o que separa duas entidades parecidas | distrófica × metastática; atrofia × hipoplasia |
| `associacao_clinica` | achado ligado a doença ou conduta | pigmentação bronze + diabetes + arritmia = hemocromatose |
| `sequencia` | ordem que não se deduz | roxo → biliverdina → hemossiderina |
| `achado_morfologico` | o que se vê na lâmina ou na peça | citoplasma rendilhado; núcleo rechaçado à periferia |
| `epônimo_ou_coloração` | nome de método ou de síndrome | Perls cora ferro em azul; von Gierke |

Card que não se encaixa em nenhum tipo **não vira card** — vira parágrafo de E1. Isso bloqueia
`c01` e `c02` na origem, e é verificável por script (`validar_deck_card_a_card.py`).

### 1.2 Teste de especificidade

Dois filtros, ambos obrigatórios:

- **Não-dedutível:** se a resposta se deduz do enunciado por raciocínio, no momento da revisão,
  o card cai. Cada card declara `why_not_derivable` em uma linha.
- **Da aula:** se alguém que nunca assistiu a esta aula responderia, o card cai. O termo da
  resposta precisa ocorrer na fonte (transcrição ou slide), não apenas na E1.

A `GENERIC` do validador (hoje sete palavras) vira uma blocklist de verdade, incluindo
`viabilidade`, `tempo`, `contato`, `parada`, `função`, `equilíbrio`, `adaptação` e afins como
**resposta** — continuam livres no enunciado.

### 1.3 Cloze: hint, irmãos e resposta como entidade

- **Hint liberado** (`{{c1::resposta::dica}}`) — 23% do AnKing usa, e é a correção direta da
  queixa "cloze que abre espaço pra múltiplas interpretações". O `CLOZE_RE` já suporta.
- **Multi-cloze irmão liberado**, de 2 a 4, quando os brancos são partes **do mesmo fato** ou
  itens de uma lista fechada: o "hide all, guess all" pedido no comentário do cálcio. Continua
  proibido empilhar fatos independentes. `cloze_occurrences_per_card` deixa de ser `1`.
- **Resposta deixa de ser limitada a 1–3 palavras**: passa a ser "um token de valor", que pode
  ser uma entidade de cinco palavras (`Gastrointestinal stromal tumor (GIST)` é AnKing puro).
  O que se mantém é: apagar o token de maior valor, nunca palavra de enchimento.

### 1.4 Frente e Extra

- **Frente**: alvo de 12 a 22 palavras (mediana AnKing 17), contexto suficiente para a
  recuperação, sem definição nua. As minhas frentes de 30+ palavras viram exceção justificada.
- **Extra vira anotação com imagem**, não parágrafo de monitor:
  - imagem obrigatória quando o fato é visual — reaproveitando o recorte que a E1 já usa,
    com crédito. A infraestrutura existe e está desligada por hábito:
    `gerar_manifesto_ankidroid.py::_embed_authored_extra_images` e
    `ankidroid.authored_extra_media_direct_install: true`;
  - conteúdo em três modos do AnKing: mecanismo curto, discriminador anti-confusão, mnemônico;
  - os "assuntos laterais" pedidos nos comentários entram aqui — é o que permite cobrir a aula
    inteira sem inflar o número de cards;
  - `max_extra_words` de 100 para 150, com a regra de forma valendo mais que o número:
    fragmento telegráfico, não oração encadeada.

### 1.5 O teto vira orçamento derivado

**Esta é a mudança central.** Hoje: `default_hard_max.large = 25`, `enforce_contract_hard_max:
true`, e a corrida corta conteúdo até caber. Passa a ser:

```
orçamento = número de itens de retenção que são, ao mesmo tempo:
            (a) de tipo válido em 1.1,
            (b) não-deriváveis por 1.2,
            (c) presentes na fonte da aula.
```

- O teto numérico deixa de bloquear. `manual_review_above` permanece só como **gatilho de
  revisão** — acima dele, a corrida explica em uma linha por que a aula é grande.
- Entra o **piso**, que é o gate que faltava: todo conceito nuclear, específico e não-derivável
  **precisa** de card. `retention_class: e1_only` deixa de ser saída para conceito nuclear.
- `sanity_ranges` deixa de ser faixa-alvo e vira estatística de acompanhamento.
- Aula dupla continua sendo um deck só, porque o orçamento agora acompanha o conteúdo.

**Efeito medido nesta aula:** dos 25 cards, 4 a 6 saem por serem genéricos (c01, c02 e
similares) e entram algo entre 20 e 28 itens hoje jogados para `e1_only` ou nem listados —
glicogenoses e von Gierke, tetracloreto de carbono, colesterolose e vesícula em morango,
xantomas, antracose, melanina e tirosinase, mieloma, célula tubular renal, atrofia parda,
biliverdina, as quatro causas de calcificação metastática, Barrett com células caliciformes,
hiperplasia prostática após os setenta, HPV e pólipos, desequilíbrio estrógeno-progesterona,
útero 40×, caquexia e TNF, corticoide e tireoidiano contra insulina, ducto tireoglosso.
**O deck sai de 25 para algo entre 45 e 55 cards**, com frente menor, Extra com imagem e menos
card por conceito organizativo.

---

## Fase 2 — Calibração contra o AnKing e revisão independente de verdade

1. **Antes de congelar o núcleo**, a corrida lê `flashcards/PESQUISA-BOM-CARD.md` (parte 1) e
   um recorte do `ANKING-DOSSIE-TEXTO.md` do mesmo domínio. É leitura de rubrica; a cópia
   segue proibida (`anking.allow_source_copy: false`).
2. **Depois de autorar**, roda o teste cego com `card_mirror_blind.py` e o agente `card-mirror`:
   mistura os cards novos com AnKing reais do mesmo tema e mede se o discriminador distingue.
   O resultado entra no release gate como número, não como booleano.
3. **A revisão independente passa a ser independente**: `revisor-cobertura` e
   `revisor-cards-visual` assinam `independent_review_passed` e
   `rendered_pdf_visual_review_passed`. Hoje quem autora é quem assina — o gate não distingue,
   e isso é uma fragilidade de honestidade, não de forma.

---

## Fase 3 — Fechar o loop do feedback

1. **`flashcards/scripts/ler_feedback_apkg.py`**: lê `.apkg`/`.colpkg` exportado do AnkiDroid,
   descomprime o `collection.anki21b` (zstd), extrai `NEBLI_Comentario`, flags e as tags
   `NEBLI::card::<slug>::<card_key>` e `NEBLI::hash::<16 hex>`, casa com o `deck-data.json` e
   grava `flashcards/feedback/<slug>.json`. A checagem de hash já funciona: `c01` →
   `b5b8df86ea055dbd` bate com o `content_sha256` do manifesto, então dá para saber se o card
   mudou depois do comentário.
2. **Campos de comentário no note type de Image Occlusion**: `NEBLI Image Occlusion v1` não tem
   `NEBLI_Comentario` nem `NEBLI_Resposta` (o AnKingOverhaul tem). Hoje não há onde comentar
   card de imagem. Correção no `AnkiBridge.java::ensureIoModel` mais migração das notas
   existentes.
3. **Passo zero da `EXECUCAO.md`**: ler o feedback pendente da aula anterior. O release gate
   bloqueia enquanto houver comentário sem resposta ou sem correção aplicada.
4. **Recibo do Companion**: o `finalizar_entrega_canonica.py` emite recibo pendente e a corrida
   seguinte exige o anterior. Hoje o passo 9 nunca fecha e ninguém percebe instalação falha.

---

## Fase 4 — Visual, Image Occlusion e didática da E1

1. **IO deixa de depender de rótulo pré-existente.** Em patologia, o que se cobra é reconhecer
   padrão, e quase nenhuma lâmina da aula vem rotulada — por isso saíram só 2 IO em 25 cards.
   Passa a ser permitido **desenhar o rótulo em português sobre a imagem** e mascarar esse
   rótulo. Alternativa complementar: card visual simples, imagem na frente e nome atrás.
2. **Imagem do Extra reaproveita o recorte da E1**, com o mesmo crédito — custo marginal zero
   por aula, já que o recorte é feito uma vez.
3. **Didática da E1**: uma `clinica-box` por PARTE quando o tema permite (asma, insuficiência
   cardíaca, refluxo, hemocromatose ficaram sem) e mais `figura-lateral`, que reduz os rodapés
   vazios que sobraram nas páginas 5 e 24.

---

## Ordem de execução e critério de aceite

| Ordem | Fase | Por que primeiro | Aceite |
|---|---|---|---|
| 1 | Fase 1 (contrato) | é o que o Davi está sentindo em cada revisão | esta aula refeita, 45–55 cards, nenhum respondível sem ter visto a aula |
| 2 | Fase 0 (ambiente) | destrava a velocidade das corridas seguintes | corrida do PDF ao manifesto sem script descartável |
| 3 | Fase 3 (feedback) | fecha o ciclo que hoje depende de eu ler `.apkg` na mão | comentário vira issue de card automaticamente |
| 4 | Fase 2 (calibração) | precisa do contrato novo para valer | teste cego no nível do acaso |
| 5 | Fase 4 (visual) | maior custo por card, menor urgência | IO com rótulo próprio funcionando em lâmina sem rótulo |

**Prova de fogo do plano inteiro:** refazer `patologia-adaptacao-celular-acumulos` sob o v12 e
comparar deck a deck com o v11, card a card, com os comentários do `.apkg` como gabarito.
