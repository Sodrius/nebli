# TEMPLATE_API — assinaturas dos helpers do nebli_v2_apostila.typ

**Leitura para REDATOR-E1 e QUESTIONADOR.** Substitui a leitura do `.typ` inteiro (32KB) por esta vista parcial (~2k tokens). Se precisar do detalhe de implementação de um helper específico (ex: para ajustar estilo), abra a função no `nebli_v2_apostila.typ` pelo nome.

**Cabeçalho obrigatório em todo `etapaN.typ`:**
```typst
#import "../typst-template/nebli_v2_apostila.typ": *
```

---

## Cores canônicas (constantes)

`navy`, `teal`, `teal-light`, `gold`, `red-alert`, `blue-clin`, `green-cons`, `violet`, `slate`, `gray-bg`, `gray-border`, `text-main`, `text-light`, `bg-clinica`, `bg-atencao`, `bg-mini`, `bg-resumo`, `bg-prova-mc`, `bg-prova-ce`, `bg-prova-discursiva`, `borda-prova-mc`, `borda-prova-ce`, `borda-prova-discursiva`, `blue-light` (deprecated).

## Fontes

`titulo-fam = ("Montserrat",)` · `corpo-fam = ("Merriweather",)`

---

## Estrutura de página e seções

### `pagina-padrao(corpo)`
Wrapper de página A4 com header/footer canônicos. Aplicado via `#show: pagina-padrao` no `main.typ`.

### `set-etapa(nome)`
Atualiza o state da etapa para o header.
```typst
#set-etapa("Etapa 1 — texto didático")
```

### `etapa-header(titulo)`
Página de abertura de etapa com título grande. Chamado pelo `main.typ`.

### `parte-title(titulo, primeira: false)`
Cabeçalho de PARTE da E1.
```typst
#parte-title("PARTE I — As peças", primeira: true)
```

### `subtopico(titulo)`
Cabeçalho de subtópico (1.1, 1.2…). Numbering manual.
```typst
#subtopico("1.1 — Bases nitrogenadas")
```

---

## Boxes didáticos

### `intro-box(conteudo)`
Box cinza de introdução do resumo (antes da PARTE I). 1 por E1.
```typst
#intro-box[Antes de mergulhar em X, fixar o porquê...]
```

### `atencao-box(titulo, conteudo)`
Box vermelho — confusão crítica com consequência grave (inversão conceitual destruidora ou risco clínico letal). **Cota máxima: 1-2 por PARTE.**
```typst
#atencao-box("Cuidado com a inversão", [Aluno tende a achar que...])
```

### `confusao-prevista(titulo, aluno_acha, mecanismo)`
Box gold (canônico 2026-05-26) — sub-padrão do atencao-box para confusões com expectativa errada nomeável ("X não é Y"). Visualmente mais leve que o vermelho, estrutura fixa em 2 movimentos. Reservar atencao-box vermelho para risco clínico letal; confusao-prevista para inversões conceituais comuns. Soma-se à cota total de boxes da PARTE.
```typst
#confusao-prevista(
  titulo: "Despolarização não é inversão de polaridade",
  aluno_acha: [aluno acha que despolarizar = interior virar positivo],
  mecanismo: [na verdade, despolarizar = SAIR DO REPOUSO — pode ir de -70 para -50 (continua negativo, só menos). Inversão é sub-categoria rara (overshoot).],
)
```

### `clinica-box(titulo, conteudo)`
Box azul — ponte para clínica. Máximo 1 por subtópico.
```typst
#clinica-box("Anemia falciforme", [Mutação em Glu→Val no códon 6...])
```

### `sintese-box(numero, conteudo)`
Síntese ao final de um subtópico. Numerada.

### `mini-resumo(conteudo)`
Resumo em parágrafo longo (>5 linhas) — em meio do texto.
```typst
#mini-resumo[X causa Y → consequência Z.]
```

### `conclusao-box(conteudo)`
Box âmbar fechando a Etapa 1 (Conclusão integradora). 1 por E1.

---

## Figuras

### `figura-nebli(caminho, legenda: none, largura: 65%, ..rest)`
Figura centralizada com legenda. **Path com `/` inicial obrigatório.**
```typst
#figura-nebli("/figuras/acidos-nucleicos/slide-14.png",
  largura: 65%,
  legenda: [Repare como purinas têm anel duplo...])
```

### `figura-lateral(caminho, legenda: [], texto: [], lado: "right", largura-figura: 38%)`
Grid 2 colunas: texto à esquerda/direita + figura ao lado. Use quando parágrafo é médio (~80–120 palavras) e figura é estrutural pequena.
```typst
#figura-lateral("/figuras/glicose/slide-32.png",
  lado: "right",
  largura-figura: 38%,
  texto: [Na projeção de Fischer, o C com OH à direita...],
  legenda: [D-glicose])
```

---

## Badges (para questões)

`#badge-consolidacao` (verde) · `#badge-integracao` (azul) · `#badge-aplicacao` (violeta) · `#badge-prioritario` (vermelho — só E4).

`#badge-rel-alta` (âmbar) — deprecated, não usar em resumos novos.

---

## Questões da Etapa 2 (sem gabarito inline — cor por categoria)

### `questao-mc(numero, badge, enunciado, alts)`
Múltipla escolha A–E. `alts` é tupla de pares `("LETRA", [texto])`.
```typst
#questao-mc("01", badge-consolidacao,
  [Sobre a estrutura do DNA, é correto afirmar:],
  (("A", [O DNA é uma molécula de fita simples...]),
   ("B", [A timina pareia com a guanina...]),
   ("C", [As fitas são antiparalelas...]),
   ("D", [O esqueleto é de proteínas...]),
   ("E", [...])))
```

### `questao-ce(numero, badge, enunciado, itens)`
4 itens certo/errado. `itens` é **tupla de pares `("MARCADOR", [conteudo])`** — o helper itera `(rom, conteudo)` e imprime `rom.` em negrito antes de cada item. Gate hard: sempre 4 pares (I–IV).
```typst
#questao-ce("05", badge-integracao,
  [Julgue os itens sobre Watson-Crick:],
  (("I",   [A=T forma 2 pontes de hidrogênio]),
   ("II",  [G≡C forma 3 pontes de hidrogênio]),
   ("III", [Pareamento ocorre entre purina e pirimidina]),
   ("IV",  [As fitas são antiparalelas e complementares])))
```
> ⚠ **Armadilha:** `([item1], [item2], ...)` (tupla plana) é a assinatura ERRADA — causa erro de compilação. Sempre usar pares `("I",[...])`.  Diferente de `prova-ce` (E4) que tem assinatura diferente.

---

## Discursivas da Etapa 3

### `discursiva(numero, enunciado, modelo, titulo-q: none)`
Pergunta mecanística + modelo de resposta ≤100 palavras (Q5 ≤130).
```typst
#discursiva("Q1",
  [Explique por que a hexoquinase aprisiona a glicose na célula.],
  [A hexoquinase fosforila a glicose...])
```

---

## Questões da Etapa 4 (gabarito inline — cor por FORMATO)

### `prova-mc(badge, enunciado, alts, gabarito-letra, justificativa)`
MC com gabarito inline. Cor azul-claro (`bg-prova-mc`).
```typst
#prova-mc(badge-prioritario,
  [Em um experimento clássico...],
  (("A", [...]), ("B", [...]), ...),
  "C",
  [Explicação curta de por que C: ...])
```

### `prova-ce(badge, enunciado, itens, gabarito-itens, justificativa)`
C/E com gabarito inline. Cor âmbar (`bg-prova-ce`).
```typst
#prova-ce(none,
  [Julgue:],
  ([...], [...], [...], [...]),
  "CEEC",
  [Explicação: ...])
```

### `prova-discursiva(badge, enunciado, modelo)`
Discursiva da E4. Cor cinza-slate (`bg-prova-discursiva`).

### `prova-block(...)` — alias de `prova-mc` (compat legacy).

---

## Glossário e termos

### `termo-nota(termo, def)`
Footnote para termo técnico denso na 1ª aparição.
```typst
#termo-nota[acetilcolina][principal neurotransmissor da JNM, liberado via SNARE]
```
5–10 por E1. Saída: `acetilcolina¹` + footnote.

### `sigla(abreviacao, expansao)`
Footnote automática para sigla na 1ª aparição. **String entre aspas, content entre colchetes.**
```typst
#sigla("ATP", [adenosina trifosfato — moeda energética da célula])
```
Subsequente: só `"ATP"`, sem footnote. Sem teto.

### `glossario-siglas-page()` — DEPRECATED. No-op silencioso. Não chamar em resumos novos.

---

## Capa, sumário, gabarito, resumindo, mapa-parte

### `capa(titulo, subtitulo, meta)`
1ª página. `meta` = tupla de pares `("Rotulo", "valor")`. **Regra canônica 2026-05-17 (revista 2026-05-26):** sem indicador de calendário em parte alguma da capa — proibido bloco/prova (P1/P2/P3), número de aula, código de slug, turma. Tema seco no título, disciplina seca no subtítulo (ou subtítulo vazio). Campos do meta: **Disciplina · Onde estudar · Onde aprofundar** (este último canônico 2026-06-30). "Nota de uso" foi removida em 2026-05-26 a pedido de Davi.

**`valor` pode ser string OU lista** (canônico 2026-06-30): string → linha simples; **lista → bullets navy** (cada item um `•`), usado pelo bloco "Onde aprofundar". Quem gera é o `gerar_main.py` a partir do `meta` em lista no Tema Card — itens são conteúdo Typst (negrito `*...*` ok; `#`/`_` das tags AnKing são escapados automaticamente). Fonte do conteúdo: `referencias-externas/onde-aprofundar.md`.
```typst
#capa("Ácidos nucleicos",
  "Biologia Molecular",
  (("Disciplina", "Biologia Molecular"),
   ("Onde estudar", "Lehninger Cap. 8 + Alberts Cap. 4"),
   ("Onde aprofundar", (        // valor em lista → bullets
     "*Assistir/ler* — B&B / Bootcamp · NinjaNerd · Sketchy · UWorld · Pathoma: não cobre",
     "*Dessuspender no AnKing v12* — decks sob #AK_Step1_v12::",
     "#FirstAid::01_Biochem::01_Nucleotides — 42 cards"))))
```

### `sumario(estrutura)`
Sumário em 2 níveis. Veja o `main.typ` do #6 (Ácidos Nucleicos) para exemplo completo.

### `gabarito-bloco(titulo, items)` / `gabarito-page(blocos)`
Gabarito consolidado da E2, organizado por categoria.
```typst
#gabarito-page((
  ("Consolidação (Q01–Q10)", (("01", "C"), ("02", "CEEC"), ...)),
  ("Integração (Q11–Q25)", (...)),
  ("Aplicação (Q26–Q30)", (...)),
))
```

### `resumindo-page(secoes)`
Página "Resumindo" — 1 página, 2 colunas, banner âmbar. Chamada **logo após Conclusão integradora da E1**, antes da E2. REDATOR-E1 entrega `resumindo.typ` com a estrutura `secoes-resumindo`.

### `mapa-parte(parte: none, centro: [], nos: (), arestas: (), fecha-com: none)`
Mapa hub-and-spoke ao final de cada PARTE da E1. **Limites operacionais:** `centro` ≤12 palavras, `no.titulo` ≤3, `no.texto` ≤10–12, label da aresta ≤3–4, `fecha-com` ≤18.
```typst
#mapa-parte(
  parte: "I",
  centro: [Forma manda na função],
  nos: ((titulo: "1.1", texto: [Bases purina/pirimidina]),
        (titulo: "1.2", texto: [Ribose vs desoxirribose]),
        (titulo: "1.3", texto: [Ligação N-glicosídica])),
  arestas: ((), ()),
  fecha-com: [Da peça ao polímero, passamos para a PARTE II.],
)
```

---

## Mindmap de fechamento da Etapa 1 — SUSPENSO 2026-05-28

> ⚠ **SUSPENSO** a pedido de Davi em 2026-05-28. Resumos NOVOS não devem chamar `#mindmap-fechamento(...)`. O helper continua no template como **no-op silencioso** para compat retroativa (não quebra compilação, não renderiza nada). Documentação abaixo preservada como referência histórica caso seja ressuscitado.

### `mindmap-fechamento(tema, mensagem, estacoes, com-setas, rodape-titulo, cartoes)` — SUSPENSO

Fecha a E1 com 1 página de revisão visual. **Substituiu** `mapa-parte` (suspenso 2026-05-19) entre 2026-05-22 e 2026-05-28. REDATOR-E1 chamava logo após a Conclusão integradora e antes do `resumindo-page(...)`.

**Estrutura em 3 zonas:**
1. **MENSAGEM** — título caixa alta + frase-síntese italicizada (a única frase que o aluno LEVA EMBORA).
2. **NARRATIVA** — 3 estações em fila. Setas → entre elas se há ordem temporal (`com-setas: true`); sem setas se são categorias paralelas (`com-setas: false`).
3. **DETALHE** — 3 cartões pequenos no rodapé (regulação, clínica, integração — varia por tema).

**Parâmetros:**
- `tema: str` — caixa alta no topo, ex: `"GLICÓLISE"`.
- `mensagem: str` — frase-síntese, 15–25 palavras, voz dialogal.
- `estacoes: array de 3 dicts` — cada um com `rotulo`, `titulo`, `fala`, `cor` (`"a"|"b"|"c"|"neutra"`) e `destaque: bool` (opcional, engorda título — usar no nó-pivô).
- `com-setas: bool` — `true` para temas com ordem (Glicólise: inv→virada→pag), `false` para paralelos (Citoesqueleto: MF·MT·FI).
- `rodape-titulo: str` (opcional) — etiqueta acima dos cartões.
- `cartoes: array de 3 dicts` — cada um com `titulo` e `frase` (15–25 palavras italicizadas).

**Paleta:** `"a"` = gold (investimento/categoria 1), `"b"` = teal (pagamento/categoria 2), `"c"` = blue-clin (categoria 3), `"neutra"` = navy/gray (pivô conceitual).

**Exemplo — tema com ordem (Glicólise):**
```typst
#mindmap-fechamento(
  tema: "GLICÓLISE",
  mensagem: "a célula investe 2 ATP no começo para ganhar 4 no fim — saldo +2 ATP, +2 NADH, 2 piruvato",
  com-setas: true,
  estacoes: (
    (rotulo: "Fase preparatória · R1–R5", titulo: "Hexoquinase e PFK-1",
     fala: [a célula paga 2 ATP pra prender a glicose e cortar em duas — PFK-1 fecha a porta], cor: "a"),
    (rotulo: "Virada · R5 → R6", titulo: "Para de gastar, começa a ganhar",
     fala: [todo passo daqui pra frente conta dobrado — a glicose virou duas trioses], cor: "neutra", destaque: true),
    (rotulo: "Fase de geração · R6–R10", titulo: "GAPDH e Piruvato-quinase",
     fala: [GAPDH solta o NADH; PGK e piruvato-quinase devolvem 4 ATP], cor: "b"),
  ),
  rodape-titulo: "Quando ligar · pra onde vai · por que importa",
  cartoes: (
    (titulo: "Quem manda na velocidade", frase: [PFK-1 é o termostato — ↑AMP/F2,6-BP, ↓ATP/citrato]),
    (titulo: "Pra onde vai o piruvato", frase: [com O₂ → Krebs; sem O₂ → lactato regenera NAD⁺]),
    (titulo: "Por que isso importa", frase: [única via que rende ATP sem O₂ — hemácia, músculo, tumor]),
  ),
)
```

**Exemplo — tema sem ordem (Citoesqueleto, categorias paralelas):**
```typst
#mindmap-fechamento(
  tema: "CITOESQUELETO",
  mensagem: "actina mexe a borda, microtúbulos transportam por dentro, FI aguentam o tranco",
  com-setas: false,
  estacoes: (
    (rotulo: "Microfilamentos · 7 nm · dinâmicos", titulo: "Actina e miosina",
     fala: [actina-G se encaixa em fila virando actina-F — miosina puxa pra contrair músculo], cor: "b"),
    (rotulo: "Microtúbulos · 25 nm · dinâmicos", titulo: "Tubulina, cinesina e dineína",
     fala: [tubo oco como trilho — cinesina pra periferia, dineína de volta], cor: "a"),
    (rotulo: "FI · 10 nm · estáticos", titulo: "Trançam como corda",
     fala: [não têm motor — queratina no epitélio, vimentina no mesênquima, laminas no núcleo], cor: "c"),
  ),
  rodape-titulo: "Por que importa · drogas · integração",
  cartoes: (
    (titulo: "Quimioterapia", frase: [colchicina e taxol travam MT — célula em divisão morre antes da mitose]),
    (titulo: "Identidade tecidual", frase: [patologista usa FI pra identificar origem do tumor]),
    (titulo: "Os 3 conversam", frase: [junções aderentes-MF, desmossomos-FI, hemidesmossomos-FI/matriz]),
  ),
)
```

### `mindmap-estacao(rotulo, titulo, fala, cor-base, cor-fundo, destaque: false)`
Helper de baixo nível. Use apenas se o tema escapa do schema dos 3 padrões e você precisa montar manualmente. Recomendado: usar `mindmap-fechamento` direto.

### `mindmap-cartao(titulo, frase)`
Cartão pequeno do rodapé. Mesma observação acima.

### Regras editoriais (canônicas)
- **3 estações sempre** (não 2, não 4).
- **3 cartões sempre.**
- **Frase-síntese, falas e frases dos cartões em voz dialogal** — monitor explicando, não label seco. Proibido: mnemônico forçado, pergunta retórica, gíria.
- **Caber em 1 página é dado.** Se estourar, reduzir conteúdo (eliminar nó, encurtar fala) — nunca comprimir leading/tamanho.

---

## NEBLIcards (E5 em standby — não usar em resumos novos)

`neblicard(contexto, pergunta, resposta)` · `cloze(t)` · `seta` — mantidos só por compat. Pipeline canônico não chama mais.

---

**Resumo:** 38 helpers (35 anteriores + `mindmap-fechamento` + `mindmap-estacao` + `mindmap-cartao`). Para detalhe de implementação, abra o `nebli_v2_apostila.typ` pelo nome. Para casos de uso real, ver os 6 resumos compilados em `resumos-gerados/` + a amostra do helper `mindmap-fechamento` em `arquivos-trabalho/mindmap-amostras/`.
