// ===========================================================
// NEBLI v2 — APOSTILA
// Criado em 2026-05-14 (B6 radical aplicado).
// Identidade visual: cara de apostila clássica brasileira, calibrada
// para leitura longa. Inspiração: Bernoulli, Poliedro, Anglo Vestibulares,
// com tipografia editorial moderna.
//
// Decisões editoriais:
// - Corpo: Merriweather 10pt (canônico — Crimson Pro testado em 2026-05-19
//   e rejeitado por Davi; revertido na mesma sessão).
// - Títulos: Montserrat (sans geométrica). Par clássico com Merriweather.
// - Leading 1.55× (was ~1.45× em v1). Padrão de textbook longo.
// - Paleta: navy serenado + teal saturado + âmbar terroso. Backgrounds
//   warm para reduzir fadiga visual em sessões longas.
// - Boxes com cantos arredondados (radius 5pt), respiro maior entre
//   subtópicos. Diferencia visualmente do v1.
// - Compatibilidade total de assinaturas com v1: REDATOR/QUESTIONADOR
//   não mudam nada.
// ===========================================================

// ======= PALETA APOSTILA =======
// Navy serenado (~ +20% warmth vs v1)
#let navy        = rgb("#1E3A5F")
// Teal apostila (mais saturado, "biblioteca")
#let teal        = rgb("#0E6B7A")
#let teal-light  = rgb("#E3F1F2")
// Âmbar terroso (mais quente que o gold v1)
#let gold        = rgb("#C58A1D")
// Vermelho-alerta (preservado, é canônico)
#let red-alert   = rgb("#C0392B")
// Azul clínico (preservado)
#let blue-clin   = rgb("#2874A6")
// Verde consolidação (preservado, taxonomia)
#let green-cons  = rgb("#1E8449")
// Violeta aplicação (preservado, taxonomia)
#let violet      = rgb("#7D3C98")
// Slate / grafite (NOVO 2026-05-15 -- cor canônica para discursiva da E4)
#let slate       = rgb("#475569")
// Cinzas warm (apostila)
#let gray-bg     = rgb("#F5F3EE")
#let gray-border = rgb("#D8D2C5")
#let text-main   = rgb("#1F2E3D")
#let text-light  = rgb("#5B6B7A")
// Backgrounds dos boxes — todos warm
#let bg-clinica  = rgb("#EBF2F8")
#let bg-atencao  = rgb("#FAEBEA")
#let bg-mini     = rgb("#F4F7F2")
#let bg-resumo   = rgb("#FDF6E3")  // creme-âmbar (solarized light)
// Backgrounds canônicos da E4 (Etapa 4 -- questões de fundamentos) por FORMATO.
// Canônico 2026-05-15: cor de cada quest. da E4 = formato (MC/C-E/discursiva),
// não nível. (E2 segue com cores por categoria: verde/azul/violeta.)
#let bg-prova-mc         = rgb("#EBF2F8")  // mesmo do bg-clinica -- azul-claro
#let bg-prova-ce         = rgb("#FFFBF0")  // âmbar-creme (era o default antigo)
#let bg-prova-discursiva = rgb("#F1F2F4")  // cinza-claro slate
#let borda-prova-mc         = blue-clin
#let borda-prova-ce         = rgb("#EAD18A")  // âmbar mais escuro
#let borda-prova-discursiva = slate
// [DEPRECATED] mantido só p/ compat com helpers legacy
#let blue-light  = rgb("#5DADE2")

// ======= FAMÍLIAS DE FONTE =======
// Merriweather: serif desenhada para leitura longa, peso 400/700, com itálico.
// Montserrat: sans geométrica, hierarquia clara para títulos e badges.
// Ambas em fonts/ do projeto, carregadas via `--font-path ../fonts`.
// NOTA 2026-05-19: Crimson Pro foi testada e rejeitada por Davi na mesma sessão.
// Arquivos crimsonpro-*.ttf permanecem em fonts/ mas NÃO são canônicos.
// Corpo = Merriweather. Não alterar sem aprovação explícita de Davi.
#let titulo-fam = ("Montserrat",)
#let corpo-fam  = ("Merriweather",)

// ======= Página padrão =======
// Margens ligeiramente maiores que o v1 — mais respiro nas bordas.
// Header com tracking maior, footer com número de página simples.
#let pagina-padrao(corpo) = {
  set page(
    paper: "a4",
    margin: (top: 1.7cm, bottom: 1.8cm, left: 1.9cm, right: 1.9cm),
    header: context {
      // Canonico 2026-09-06: o header nao pode ler `state.get()`, porque o
      // update de `set-etapa` no topo do corpo de uma pagina e resolvido
      // DEPOIS do header dessa mesma pagina -- resultado: toda pagina de
      // banner de secao (Sumario, Etapa 1/2/3, Resumindo, Gabarito) exibia o
      // nome da secao ANTERIOR. Bug pego pelo `auditar_pdf_visual` como
      // "header dessincronizado". A correcao troca state por marcadores
      // consultados por numero de pagina: o marcador que cai NA pagina conta
      // para ela, e a defasagem some.
      let pg = here().page()
      let marcas = query(<nebli-etapa>).filter(m => m.location().page() <= pg)
      let val = if marcas.len() > 0 { marcas.last().value } else { "" }
      grid(columns: (1fr, 1fr),
        align: (left, right),
        text(font: titulo-fam, weight: "bold", size: 8pt, fill: rgb("#B8B8B8"), tracking: 3pt, "NEBLI"),
        text(font: titulo-fam, size: 8pt, fill: rgb("#B8B8B8"), tracking: 1pt, upper(val))
      )
    },
    footer: align(center,
      text(font: titulo-fam, size: 9pt, fill: rgb("#888888"), context counter(page).display())
    ),
  )
  // Corpo em Merriweather 10pt (canônico 2026-05-18 — restaura tamanho usado
  // até CITOESQUELETO em 17/maio, antes da subida temporária para 11pt).
  // Tentativa de 9pt + Crimson Pro em 2026-05-19: revertida por Davi na mesma sessão.
  set text(font: corpo-fam, size: 10pt, fill: text-main)
  // Sem indentação de primeira linha (canônico 2026-05-19): apostila, não livro.
  // Spacing entre parágrafos generoso (canônico 2026-05-19 v2 após Davi):
  // 1.2em substitui visualmente a indentação. Leading subido para 1.0em
  // para aliviar a densidade vertical de Merriweather 10pt.
  set par(justify: true, leading: 1.0em, first-line-indent: 0em, spacing: 1.2em, linebreaks: "optimized")
  set heading(numbering: none)
  // Negrito em PRETO (canônico 2026-05-19 v2 após Davi): negrito em navy parecia link
  // e ficava menos profissional. Preto puro dá peso sem mudar a cor da página.
  // Itálico em text-main com leve opacidade (text-light parecia "linkado").
  show strong: set text(fill: text-main)
  show emph: set text(fill: text-light)
  // Footnotes canônicas (sem alteração funcional)
  set footnote.entry(separator: line(length: 30%, stroke: 0.5pt + gray-border))
  show footnote.entry: it => text(size: 8.5pt, fill: text-light, it)
  corpo
}

// ======= Atualiza a string do header =======
#let set-etapa(nome) = [#metadata(nome)<nebli-etapa>]

// ======= Banner de etapa =======
// Caixa navy com cantos arredondados (apostila moderna, não bandeira chapada).
#let etapa-header(titulo) = {
  pagebreak(weak: true)
  set-etapa(titulo)
  block(
    fill: navy, inset: (x: 20pt, y: 14pt), width: 100%, radius: 4pt,
    text(font: titulo-fam, size: 17pt, weight: "bold", fill: white, tracking: 0.5pt, titulo)
  )
  v(12pt)
}

// ======= PARTE (PARTE I, II, III) =======
// Linha dupla decorativa abaixo — fino + grosso — visual editorial.
#let parte-title(titulo, primeira: false) = {
  if not primeira { pagebreak(weak: true) }
  // Canônico 2026-05-19 v2 (após Davi): PARTE sobe para 16pt + mais respiro
  // acima/abaixo. Hierarquia visual clara em relação ao subtopico (11pt teal).
  block(below: 12pt, breakable: false,
    stack(
      text(font: titulo-fam, size: 16pt, weight: "bold", fill: navy, tracking: 0.3pt, titulo),
      v(6pt),
      line(length: 100%, stroke: 2.5pt + teal),
      v(1.5pt),
      line(length: 100%, stroke: 0.5pt + teal),
    )
  )
}

// ======= Subtópico (1.1, 1.2.) =======
// Canônico 2026-05-19 v2 (após Davi): desceu para 11pt para criar hierarquia
// clara com PARTE (16pt). Mantém cor teal — identidade visual de subseção.
#let subtopico(titulo) = {
  v(10pt)
  block(below: 8pt, breakable: false,
    text(font: titulo-fam, size: 11pt, weight: "bold", fill: teal, tracking: 0.2pt, titulo)
  )
}

// ======= Boxes (canto arredondado, padding maior) =======
// Canonico 2026-05-15: `set par(first-line-indent: 0em)` interno em todos
// os boxes (intro, atencao, clinica, sintese, mini-resumo, conclusao). O
// 1.1em do pagina-padrao herda para dentro dos boxes e deixa recuo estranho
// em caixas pequenas. Mesmo tratamento ja aplicado nos helpers de questao.
#let _box(bg, borda-cor, conteudo, titulo: none, titulo-cor: none, borda-l: 4pt) = {
  block(
    fill: bg,
    stroke: (left: borda-l + borda-cor),
    inset: (x: 15pt, y: 11pt),
    width: 100%,
    radius: 5pt,
    breakable: false,
    {
      set par(first-line-indent: 0em)
      if titulo != none {
        text(font: titulo-fam, weight: "bold", size: 10pt, fill: titulo-cor, tracking: 0.2pt, titulo)
        v(4pt)
      }
      set text(size: 10pt)
      conteudo
    }
  )
}

#let intro-box(conteudo) = _box(gray-bg, navy, conteudo, borda-l: 5pt)

#let atencao-box(titulo, conteudo) = _box(bg-atencao, red-alert, conteudo,
  titulo: titulo, titulo-cor: red-alert, borda-l: 5pt)

// ======= #confusao-prevista — box editorial para inversao conceitual =======
// Canonico 2026-05-26. Sub-padrao do atencao-box especifico para confusoes
// onde o aluno tem expectativa errada nomeavel ("X NAO eh Y"). Diferente do
// atencao-box generico: visualmente mais leve (gold em vez de vermelho) e
// estrutura fixa em 2 movimentos -- "aluno acha" + "mecanismo correto".
//
// Quando usar:
//   - Titulo deve ser negacao curta ("Despolarizacao nao e inversao") OU
//     equacao errada nomeada ("Ka x pKa = constante? Nao.").
//   - Confusao tem inversao de polaridade conceitual mas SEM consequencia
//     clinica letal. Para risco clinico imediato (cianeto -> Complexo IV),
//     usar atencao-box vermelho.
//
// Cota: 1-2 por PARTE (somam-se ao limite total de boxes da PARTE).
//
// Uso:
//   #confusao-prevista(
//     titulo: "Despolarizacao nao e inversao de polaridade",
//     aluno_acha: [aluno acha que despolarizar = interior virar positivo],
//     mecanismo: [na verdade, despolarizar significa SAIR DO REPOUSO -- pode
//                 ir de -70 para -50 (continua negativo, so menos). Inversao
//                 e sub-categoria rara (overshoot).],
//   )
#let confusao-prevista(titulo: none, aluno_acha: [], mecanismo: []) = block(
  fill: rgb("#FDF8E8"),  // bege claro -- contraste com bg-atencao vermelho-rosado
  stroke: (left: 5pt + gold),
  inset: (x: 15pt, y: 11pt),
  width: 100%,
  radius: 5pt,
  breakable: false,
  {
    set par(first-line-indent: 0em)
    if titulo != none {
      text(font: titulo-fam, weight: "bold", size: 10pt, fill: rgb("#8B6914"),
        tracking: 0.2pt, titulo)
      v(5pt)
    }
    set text(size: 10pt)
    [#text(weight: "bold", fill: rgb("#8B6914"))[Aluno costuma achar: ] #aluno_acha]
    v(3pt)
    [#text(weight: "bold", fill: rgb("#8B6914"))[Mecanismo correto: ] #mecanismo]
  }
)

#let clinica-box(titulo, conteudo) = _box(bg-clinica, blue-clin, conteudo,
  titulo: titulo, titulo-cor: blue-clin, borda-l: 5pt)

#let sintese-box(numero, conteudo) = block(
  fill: teal-light,
  stroke: (left: 5pt + teal),
  inset: (x: 15pt, y: 11pt),
  width: 100%,
  radius: 5pt,
  breakable: false,
  {
    set par(first-line-indent: 0em)
    set text(size: 10pt)
    [#text(weight: "bold", fill: teal)[Síntese #numero —] #conteudo]
  }
)

#let mini-resumo(conteudo) = block(
  fill: bg-mini,
  stroke: (left: 3pt + teal),
  inset: (x: 13pt, y: 8pt),
  width: 100%,
  radius: 4pt,
  breakable: false,
  {
    set par(first-line-indent: 0em)
    set text(size: 10pt, style: "italic")
    [#text(weight: "bold", fill: teal, style: "normal")[Resumindo até aqui:] #conteudo]
  }
)

#let conclusao-box(conteudo) = block(
  fill: bg-clinica,
  stroke: 1.5pt + blue-clin,
  inset: (x: 15pt, y: 13pt),
  width: 100%,
  radius: 6pt,
  breakable: false,
  {
    set par(first-line-indent: 0em)
    text(font: titulo-fam, weight: "bold", size: 11.5pt, fill: blue-clin, tracking: 0.3pt, "Conclusão integradora")
    v(6pt)
    conteudo
  }
)

// ======= Figura NEBLI (com legenda) =======
// Caption ligeiramente maior (9.5pt vs 9pt) e mais respiro.
// Canônico 2026-05-15: largura default reduzida de 80% -> 65%. Figuras
// menores reduzem o "espaço vazio" das páginas com imagem. Quando o
// REDATOR realmente precisar de figura maior (estrutura complexa,
// micrografia), passa explicitamente -- ex: figura-nebli(..., largura: 85%).
#let figura-nebli(caminho, legenda: none, largura: 65%, ..rest) = {
  // Canonico 2026-05-16: legenda virou named arg (era positional).
  // Permite chamada #figura-nebli("path", legenda: [...], largura: 65%).
  // Compat retroativo: pega do 1o positional se nao for passado named.
  let legenda = if legenda != none { legenda }
    else if rest.pos().len() >= 1 { rest.pos().at(0) }
    else { [] }
  // Canonico 2026-07-02: figura FLUTUANTE (placement: auto). Antes era um
  // bloco inline breakable:false que, quando nao cabia no rodape da pagina,
  // era empurrado inteiro para a proxima -- deixando um buraco branco feio.
  // Como float, o Typst posiciona a figura no topo/rodape da pagina e deixa
  // o texto do corpo preencher o espaco. Imagem + legenda seguem juntas.
  figure(
    placement: auto,
    caption: none,
    numbering: none,
    supplement: none,
    block(breakable: false,
      stack(
        image(caminho, width: largura),
        v(6pt),
        align(left,
          text(size: 9.5pt, style: "italic", fill: text-light, legenda)
        )
      )
    )
  )
}

// ======= Figura LATERAL (texto fluindo ao lado) =======
// Canônico 2026-05-15: helper para integrar figura no fluxo do texto,
// em vez de empurrar a figura para uma linha sozinha que deixa espaço vazio.
// O REDATOR passa o parágrafo (ou parágrafos) que falam da figura como
// `texto`, e a figura aparece ao lado.
//
// USO:
//   #figura-lateral(
//     "figuras/atp/estrutura.png",
//     legenda: [Repare como os três fosfatos concentram carga negativa.],
//     texto: [A molécula de ATP carrega energia química principalmente nas
//       ligações fosfodiéster terminais. Quando uma dessas ligações é
//       hidrolisada, o sistema libera ~7,3 kcal/mol em condições padrão.
//       Note na figura como a distância entre os fosfatos β e γ é a região
//       de maior densidade eletrônica.],
//     lado: "right",          // ou "left"
//     largura-figura: 38%,    // default; deixar entre 30% e 45%
//   )
//
// LIMITES: o `texto` precisa ser longo o suficiente para "casar" com a
// altura da figura. Se texto < figura, sobra branco abaixo do texto; se
// texto > figura, o restante do texto continua abaixo do grid. Para textos
// curtos, prefira #figura-nebli centralizada.
#let figura-lateral(caminho, legenda: [], texto: [], lado: "right", largura-figura: 38%) = {
  let largura-texto = 100% - largura-figura - 4%
  let figura-block = block(breakable: false,
    stack(
      image(caminho, width: 100%),
      v(5pt),
      text(size: 9pt, style: "italic", fill: text-light, legenda)
    )
  )
  v(6pt)
  if lado == "right" {
    grid(
      columns: (largura-texto, largura-figura),
      column-gutter: 12pt,
      align: (top, top),
      texto, figura-block
    )
  } else {
    grid(
      columns: (largura-figura, largura-texto),
      column-gutter: 12pt,
      align: (top, top),
      figura-block, texto
    )
  }
  v(6pt)
}

// ======= Badges (nível das questões) =======
#let _badge(cor, texto) = box(
  fill: cor, inset: (x: 7pt, y: 2pt), radius: 10pt, baseline: 1pt,
  text(font: titulo-fam, size: 7.5pt, weight: "bold", fill: white, tracking: 0.5pt, texto)
)
// TAXONOMIA CANÔNICA (preservada):
//   Consolidação = VERDE  (fácil)
//   Integração   = AZUL   (médio)
//   Aplicação    = VIOLETA (difícil)
#let badge-consolidacao = _badge(green-cons, "Consolidação")
#let badge-integracao   = _badge(blue-clin,  "Integração")
#let badge-aplicacao    = _badge(violet,     "Aplicação")
#let badge-prioritario  = _badge(red-alert,  "Prioritário")

// Badge de relevância clínica (capa) -- [DEPRECATED 2026-05-13]
#let badge-rel-alta = box(fill: gold, inset: (x: 7pt, y: 2pt), radius: 10pt, baseline: 1pt,
  text(font: titulo-fam, size: 7.5pt, weight: "bold", fill: white, "Alta"))

// ======= Questão MC =======
// Canônico 2026-05-15: `set par(first-line-indent: 0em)` interno.
// Questões digitadas (estilo prova) não têm recuo de parágrafo no enunciado --
// o recuo da prosa do corpo é estilo livro; o estilo questão é flush-left.
#let questao-mc(numero, badge, enunciado, alts) = block(below: 16pt, breakable: true, {
  set par(first-line-indent: 0em)
  text(font: titulo-fam, size: 11pt, weight: "bold", fill: navy, [Questão #numero ])
  h(5pt)
  badge
  v(6pt)
  enunciado
  v(5pt)
  for (letra, conteudo) in alts {
    pad(left: 10pt, [*#letra)* #conteudo])
    v(3pt)
  }
  v(7pt)
  line(length: 100%, stroke: 0.5pt + gray-border)
})

// ======= Questão C/E =======
#let questao-ce(numero, badge, enunciado, itens) = block(below: 16pt, breakable: true, {
  set par(first-line-indent: 0em)
  text(font: titulo-fam, size: 11pt, weight: "bold", fill: navy, [Questão #numero ])
  h(5pt)
  badge
  v(6pt)
  enunciado
  v(2pt)
  text(size: 9.5pt, style: "italic", fill: text-light, "Cada item deve ser julgado de forma independente.")
  v(5pt)
  for (rom, conteudo) in itens {
    pad(left: 10pt, [#text(weight: "bold")[#rom.] #conteudo])
    v(3pt)
  }
  v(7pt)
  line(length: 100%, stroke: 0.5pt + gray-border)
})

// ======= Discursiva =======
#let discursiva(numero, enunciado, modelo, titulo-q: none) = block(
  fill: rgb("#F0F7F4"),
  stroke: 1pt + teal,
  inset: (x: 15pt, y: 13pt),
  width: 100%,
  radius: 5pt,
  breakable: false,
  below: 18pt,
  {
    set par(first-line-indent: 0em)
    text(font: titulo-fam, weight: "bold", size: 11.5pt, fill: navy,
      if titulo-q != none { titulo-q } else [Questão #numero]
    )
    v(5pt)
    enunciado
    v(9pt)
    block(
      fill: rgb("#E5F0EC"),
      stroke: 1pt + teal,
      inset: (x: 13pt, y: 11pt),
      radius: 4pt,
      {
        text(font: titulo-fam, weight: "bold", size: 9pt, fill: teal, tracking: 1pt, "MODELO DE RESPOSTA")
        v(5pt)
        set text(size: 10.5pt)
        modelo
      }
    )
  }
)

// ======= Prova-blocks (Etapa 4 -- questões de fundamentos) =======
// Canônico 2026-05-15: cor de cada bloco da E4 = FORMATO da questão.
//   MC          -> azul-clínico  (bg-prova-mc / borda-prova-mc)
//   C/E         -> âmbar-creme   (bg-prova-ce / borda-prova-ce)
//   Discursiva  -> grafite slate (bg-prova-discursiva / borda-prova-discursiva)
// Razão: o aluno bate o olho e sabe o tipo da questão antes de ler o enunciado.
// (E2 segue com cores por CATEGORIA -- verde/azul/violeta. Só a E4 usa por formato.)
//
// Todos os blocos compartilham:
//   - `set par(first-line-indent: 0em)` interno (estilo questão digitada)
//   - badge no topo (Prioritário ou nada)
//   - gabarito INLINE com justificativa logo abaixo (não acumular no final)

// MC - múltipla escolha
#let prova-mc(badge, enunciado, alts, gabarito-letra, justificativa) = block(
  fill: bg-prova-mc,
  stroke: 1pt + borda-prova-mc,
  inset: (x: 15pt, y: 13pt),
  width: 100%,
  radius: 4pt,
  breakable: true,
  below: 16pt,
  {
    set par(first-line-indent: 0em)
    badge
    v(6pt)
    enunciado
    v(5pt)
    for (letra, conteudo) in alts {
      pad(left: 10pt, [*#letra)* #conteudo])
      v(3pt)
    }
    v(7pt)
    block(
      fill: teal-light, stroke: (left: 3pt + borda-prova-mc),
      inset: (x: 13pt, y: 9pt),
      width: 100%,
      radius: 3pt,
      {
        set text(size: 10pt)
        [#text(weight: "bold", fill: borda-prova-mc)[Gabarito #gabarito-letra —] #justificativa]
      }
    )
  }
)

// C/E - certo/errado (4 itens)
// `itens` = lista de (rotulo, conteudo) (ex: ("I", [item I]), ("II", [...]))
// `gabarito-itens` = lista de "C" ou "E" na mesma ordem dos itens
#let prova-ce(badge, enunciado, itens, gabarito-itens, justificativa) = block(
  fill: bg-prova-ce,
  stroke: 1pt + borda-prova-ce,
  inset: (x: 15pt, y: 13pt),
  width: 100%,
  radius: 4pt,
  breakable: true,
  below: 16pt,
  {
    set par(first-line-indent: 0em)
    badge
    v(6pt)
    enunciado
    v(2pt)
    text(size: 9.5pt, style: "italic", fill: text-light,
      "Cada item deve ser julgado de forma independente.")
    v(5pt)
    for (rotulo, conteudo) in itens {
      pad(left: 10pt, [#text(weight: "bold")[#rotulo.] #conteudo])
      v(3pt)
    }
    v(7pt)
    block(
      fill: bg-resumo, stroke: (left: 3pt + gold),
      inset: (x: 13pt, y: 9pt),
      width: 100%,
      radius: 3pt,
      {
        set text(size: 10pt)
        let gab-str = gabarito-itens.join(" · ")
        [#text(weight: "bold", fill: gold)[Gabarito #gab-str —] #justificativa]
      }
    )
  }
)

// Discursiva - texto livre, com gabarito-modelo abaixo
#let prova-discursiva(badge, enunciado, modelo) = block(
  fill: bg-prova-discursiva,
  stroke: 1pt + borda-prova-discursiva,
  inset: (x: 15pt, y: 13pt),
  width: 100%,
  radius: 4pt,
  breakable: true,
  below: 16pt,
  {
    set par(first-line-indent: 0em)
    badge
    v(6pt)
    enunciado
    v(7pt)
    block(
      fill: rgb("#E4E6EA"), stroke: (left: 3pt + slate),
      inset: (x: 13pt, y: 9pt),
      width: 100%,
      radius: 3pt,
      {
        set text(size: 10pt)
        text(font: titulo-fam, weight: "bold", size: 9pt, fill: slate,
          tracking: 0.8pt, "GABARITO -- RESPOSTA MODELO")
        v(4pt)
        modelo
      }
    )
  }
)

// Alias legacy: #prova-block(...) continua sendo MC. Não usar em resumos novos.
#let prova-block = prova-mc

// ======= NEBLIcard =======
#let neblicard(contexto, pergunta, resposta) = block(
  stroke: (left: 4pt + teal, top: 0.5pt + gray-border, right: 0.5pt + gray-border, bottom: 0.5pt + gray-border),
  inset: (x: 15pt, y: 12pt),
  width: 100%,
  radius: 4pt,
  breakable: false,
  below: 13pt,
  {
    text(font: titulo-fam, weight: "bold", size: 8.5pt, fill: teal,
      tracking: 0.6pt, upper(contexto))
    v(5pt)
    text(font: corpo-fam, weight: "bold", size: 11pt, fill: navy, pergunta)
    v(7pt)
    line(length: 100%, stroke: 0.4pt + gray-border)
    v(7pt)
    set text(size: 10.5pt)
    resposta
  }
)

#let seta = text(weight: "bold", fill: teal, " → ")
#let cloze(t) = box(fill: rgb("#FFF3CD"), inset: (x: 3pt, y: 1pt), radius: 2pt,
  text(weight: "bold", fill: navy, t))

// ======= Capa =======
// Faixa navy mais alta (13cm), linha gold decorativa abaixo do título,
// Montserrat com tracking maior nos rótulos.
#let capa(titulo, subtitulo, meta) = {
  set page(paper: "a4", margin: 0pt, header: none, footer: none,
    background: place(top + left,
      rect(width: 21cm, height: 13cm, fill: navy, stroke: none)
    )
  )

  // TEXTO SOBRE A FAIXA NAVY
  // Desabilita justify do pagina-padrao na capa (causaria espaçamento exagerado no título).
  set par(justify: false, first-line-indent: 0em, leading: 0.65em)
  block(width: 100%, height: 13cm, inset: (x: 19mm, y: 0pt),
    {
      v(6.0cm)
      text(font: titulo-fam, weight: "bold", size: 10pt,
        fill: rgb("#9FA8B8"), tracking: 7pt, upper("NEBLI · APOSTILA"))
      v(10pt)
      // Título length-aware (canônico 2026-07-07, pedido de Davi: "título grande
      // na capa"). 30pt só para temas curtos de uma linha; títulos longos encolhem
      // em degraus para não engolir a faixa navy nem quebrar mal. Ver ERROS.md #19.
      {
        let s = if type(titulo) == str { titulo } else { repr(titulo) }
        let n = s.len()
        let tsize = if n <= 22 { 30pt } else if n <= 34 { 26pt } else if n <= 48 { 22pt } else { 19pt }
        text(font: titulo-fam, weight: "bold", size: tsize, fill: white, tracking: 0.3pt, titulo)
      }
      v(12pt)
      text(font: titulo-fam, size: 12pt, fill: rgb("#CCD2DC"), subtitulo)
      // Linha gold removida em 2026-05-15 por preferência de Davi.
    }
  )

  // META
  // Compactado 2026-07-01 (pedido de Davi: "capa sempre cabe numa página").
  // Bloco de tamanho variável ("Onde aprofundar" com N bullets) exige meta
  // enxuta: texto menor, gutter de linha menor, inset reduzido.
  block(width: 100%, inset: (x: 19mm, y: 9mm),
    {
      set text(font: titulo-fam, size: 8pt)
      for (rotulo, valor) in meta {
        block(below: 5pt,
          grid(columns: (4.4cm, 1fr), column-gutter: 7pt,
            text(weight: "bold", fill: navy, tracking: 0.3pt, [#rotulo:]),
            text(fill: text-main, valor)
          )
        )
      }
      v(6pt)
      block(stroke: (top: 0.5pt + rgb("#D0D0D0")), inset: (top: 8pt),
        text(font: corpo-fam, size: 8pt, style: "italic", fill: rgb("#666"),
          "Material elaborado a partir dos slides da disciplina. Recomenda-se estudar com o material original aberto ao lado, pois o resumo complementa — não substitui — a aula."))
    }
  )

  // RODAPÉ
  // Canônico 2026-05-17: rodapé identificador na capa, duas linhas.
  // Linha 1 = autoria ("Davi Sousa — Turma 114"). Linha 2 = contato/PIX.
  // A regra "sem calendário em qualquer parte do PDF" continua valendo
  // para o bloco meta (Disciplina · Onde estudar — "Nota de uso" removida em 2026-05-26) e para
  // o corpo. O rodapé é identificação de autoria, não calendário do
  // material — é a assinatura do autor. Decisão revertida (a remoção
  // da linha de turma em 2026-05-15 valia para a faixa navy, mas o
  // rodapé identificador também foi tirado por engano).
  place(bottom + center,
    block(width: 100%, fill: gray-bg, stroke: (top: 0.5pt + gray-border),
      inset: (x: 19mm, y: 11pt),
      {
        set par(justify: false, first-line-indent: 0em, leading: 0.55em)
        align(center,
          text(font: titulo-fam, size: 9pt, weight: "bold", fill: rgb("#444"),
            "Davi Sousa — Turma 114")
        )
        v(3pt)
        align(center,
          text(font: titulo-fam, size: 8.5pt, weight: "bold", fill: rgb("#555"),
            "(61) 98264-7208  ·  dpbdes@gmail.com  ·  PIX: dpbdes@gmail.com")
        )
      }
    )
  )

  pagebreak()
}

// ======= Antes da aula (pré-aula) — canônico 2026-08-28 =======
// Seção de abertura que fica ENTRE a capa e o sumário. Duas páginas de prosa
// contínua na voz NEBLI, contando a história da aula e plantando os termos que
// o professor vai usar como se o aluno já soubesse. Sem figura, sem bullet,
// sem questão — é leitura de cinco minutos na véspera, não estudo.
//
// Faixa TEAL (a capa é navy, o Resumindo é gold, a etapa é navy): o teal marca
// que isto vem ANTES do material, não dentro dele. Corpo 10.5pt e margens mais
// largas que o miolo — o texto respira porque a leitura aqui é corrida, não
// consultiva.
#let pre-aula-page(conteudo) = {
  set page(margin: (top: 2.0cm, bottom: 2.1cm, left: 2.2cm, right: 2.2cm))
  set-etapa("Antes da aula")
  block(fill: teal, inset: (x: 18pt, y: 10pt), width: 100%, radius: 4pt,
    text(font: titulo-fam, weight: "bold", size: 14pt, fill: white,
      tracking: 1.5pt, "Antes da aula")
  )
  v(7pt)
  block(below: 15pt,
    text(font: corpo-fam, size: 8.5pt, style: "italic", fill: text-light,
      "Cinco minutos de leitura para chegar na aula sabendo o caminho — o material completo vem depois dela.")
  )
  set par(justify: true, leading: 1.02em, spacing: 1.15em, first-line-indent: 0em)
  set text(size: 10.5pt)
  conteudo
  pagebreak()
}

// ======= Sumário =======
// Visual mais "apostila clássica": rótulos da etapa em caixa-alta com tracking,
// parte em teal, itens em corpo serif com pontilhado opcional via dot leaders.
#let sumario(estrutura) = {
  set page(margin: (top: 2.0cm, bottom: 2.1cm, left: 1.9cm, right: 1.9cm))
  set-etapa("Sumário")
  text(font: titulo-fam, size: 19pt, weight: "bold", fill: navy, tracking: 0.3pt, "Sumário")
  block(below: 4pt, line(length: 100%, stroke: 2.5pt + teal))
  block(below: 18pt, line(length: 100%, stroke: 0.5pt + teal))
  // Canônico 2026-05-19 v2 (após Davi): hierarquia mais forte.
  // ETAPA em 11pt navy bold (era 10pt) — peso de seção primária.
  // PARTE em 10pt teal bold (era 9.5pt) — peso médio.
  // Subitens em 9.5pt corpo — peso menor, contraste maior.
  for (etapa, partes) in estrutura {
    block(below: 10pt,
      text(font: titulo-fam, weight: "bold", size: 11pt, fill: navy, tracking: 0.8pt, upper(etapa))
    )
    for (parte, itens) in partes {
      if parte != none {
        block(below: 7pt,
          pad(left: 8pt,
            text(font: titulo-fam, weight: "bold", size: 10pt, fill: teal, tracking: 0.2pt, parte))
        )
      }
      for it in itens {
        block(below: 5pt,
          pad(left: 22pt,
            text(font: corpo-fam, size: 9.5pt, it))
        )
      }
    }
    v(14pt)
  }
  pagebreak()
}

// ======= Gabarito grid =======
// Canonico 2026-05-26: layout em 3 colunas com ordem column-major (lê
// cima-pra-baixo dentro de cada coluna), corrigindo o bug em que grid
// row-major do Typst entregava ordem zigue-zague (Q06 depois de Q08).
// Bug original em ~16/33 PDFs historicos. UC01-BC-07 chegou a marcar
// letra ERRADA em 43% das questoes por causa desse desalinhamento.
#let gabarito-bloco(titulo, items) = {
  block(below: 7pt,
    text(font: titulo-fam, weight: "bold", size: 10pt, fill: teal,
      tracking: 0.6pt, upper(titulo))
  )
  // Canonico 2026-06-24 (item 14): leitura HORIZONTAL, esquerda->direita,
  // linha a linha -> "Q1 Q2 Q3 Q4 Q5 / Q6 Q7 Q8 Q9 Q10 / ...". Row-major
  // NATIVO do Typst, sem reordenacao manual: o que se le e exatamente
  // items[0], items[1], ... na ordem das questoes. Isso elimina o risco de
  // letra desalinhada que o reorder column-major (2026-05-26) reintroduzia.
  let cols = 5
  grid(
    columns: (1fr,) * cols, gutter: 12pt, row-gutter: 6pt,
    ..items.map(it => {
      let (q, g) = it
      [#text(weight: "bold", fill: navy)[Q#q] #g]
    })
  )
  v(11pt)
}

#let gabarito-page(blocos) = {
  pagebreak(weak: true)
  set-etapa("Gabarito — Etapa 2")
  text(font: titulo-fam, size: 17pt, weight: "bold", fill: navy, tracking: 0.3pt, "Gabarito — Etapa 2")
  block(below: 18pt, line(length: 100%, stroke: 2pt + teal))
  for (titulo, items) in blocos {
    gabarito-bloco(titulo, items)
  }
}

// ======= Footnote canônica NEBLI (termo técnico) =======
// Footnote por página para termo TÉCNICO DENSO (acetilcolina, thiohemiacetal).
// Diferente do helper #sigla, que é para ABREVIAÇÕES (ATP, JNM, NADH).
// Uso:
//   #termo-nota[acetilcolina][principal neurotransmissor da JNM, ...]
// Calibração: 5-10 footnotes por resumo.
#let termo-nota(termo, def) = {
  [#termo#footnote[#text(font: titulo-fam, weight: "bold", size: 8.5pt, fill: navy, termo) #text(size: 8.5pt, fill: text-light)[-- #def]]]
}

// ======= Glossário de siglas -- SISTEMA CANÔNICO 2026-05-15 =======
// REESCRITO: glossário vive no RODAPÉ de cada página, não como
// seção final acumulada.
//
// COMPORTAMENTO:
//   - Sigla estreia no texto -> footnote automática naquela página com a
//     expansão completa. Aluno tem o glossário sempre à mão da leitura.
//   - Sigla repete em outra página -> só o texto da sigla, sem footnote.
//   - Sem mais seção "Glossário de siglas" no fim do PDF.
//
// COMO USAR:
//   #sigla("ATP", [adenosina trifosfato -- moeda energética da célula])
//
//   Primeira aparição:  "ATP^1"  + footnote "^1 ATP -- adenosina trifosfato..."
//   Aparições seguintes: só "ATP" sem decoração nem footnote.
//
// USO CANÔNICO: passe a abreviação como STRING, não como content.
//   CERTO:  #sigla("ATP", [adenosina trifosfato])
//   ERRADO: #sigla[ATP][adenosina trifosfato]
//
// VERSÕES ANTERIORES:
//   - 2026-05-13: helper #glossario() -- DEPRECATED.
//   - 2026-05-14: registry em state + #glossario-siglas-page() no fim do PDF
//     -- DEPRECATED em 2026-05-15. O helper #glossario-siglas-page() abaixo
//     existe só para compatibilidade com resumos compilados antes disso.

// State que rastreia siglas já vistas (para não duplicar a footnote).
#let _siglas-vistas = state("siglas-vistas", ())

// Helper #sigla -- renderiza no texto; primeira aparição inclui footnote.
#let sigla(abreviacao, expansao) = {
  let abr-str = if type(abreviacao) == str { abreviacao } else { repr(abreviacao) }
  // Decide a renderização com base no state ATUAL.
  context {
    let vistas = _siglas-vistas.get()
    if vistas.contains(abr-str) {
      // Já apareceu em página anterior -- só o texto plano.
      [#abr-str]
    } else {
      // Primeira aparição -- texto + footnote com expansão.
      [#abr-str#footnote[#text(font: titulo-fam, weight: "bold", size: 8.5pt, fill: navy, abr-str) #text(size: 8.5pt, fill: text-light)[-- #expansao]]]
    }
  }
  // Marca como vista para todas as aparições subsequentes.
  // (state.update se aplica ao que vem DEPOIS no fluxo do documento.)
  _siglas-vistas.update(v => if v.contains(abr-str) { v } else { v + (abr-str,) })
}

// Helper #glossario-siglas-page -- DEPRECATED 2026-05-15.
// Mantido só para que resumos antigos que ainda chamam esta função compilem
// sem erro. Em resumos novos, NÃO chamar -- as siglas viram footnote no
// rodapé via #sigla(...) e não há mais seção dedicada no fim do PDF.
#let glossario-siglas-page() = {
  // No-op silencioso.
}

// ======= Mapa conceitual de PARTE =======
// Canonico 2026-05-15 (L5, Fase 1): visualizador hub-and-spoke ao final
// de cada PARTE da Etapa 1. Substitui o "mapa conceitual em prosa" antigo.
//
// Layout fixo: 1 no central (navy) -> 3 nos-filhos em linha horizontal
// (teal / gold / red-alert) com setas e labels de aresta + linha de
// fechamento opcional. PARTE com 4-5 subtopicos: decisao deferida.
//
// LIMITES OPERACIONAIS (canônico 2026-05-15 -- aprendido na auditoria #5
// Carboidratos): centro <=12 palavras, no.titulo <=3, no.texto <=10-12,
// label aresta <=3-4, fecha-com <=18. Texto maior quebra o grid 5-colunas
// (labels caem dentro dos nos, palavras truncam). Se nao couber, REESCREVA.
//
// LIMITES OPERACIONAIS (canônico 2026-05-15 -- aprendido na auditoria #5
// Carboidratos, em que a PARTE III truncou labels e nós):
//   - "centro"        : ate ~12 palavras (cabe confortavelmente no bloco navy).
//   - "no.titulo"     : ate ~3 palavras (rótulo curto, ex.: "Necessidade").
//   - "no.texto"      : ate ~10-12 palavras (frase única curta).
//   - label da aresta : ate ~3-4 palavras (ex.: "demanda exige").
//   - "fecha-com"     : ate ~18 palavras (uma frase de ponte).
// Textos maiores que isso quebram o grid 5-colunas (no/seta/no/seta/no):
// labels caem dentro dos nos, palavras truncam horizontalmente.
// Se o conteudo nao couber nesses limites, REESCREVER -- nao aumentar a
// figura, nao reduzir font-size, nao tentar quebrar em 2 linhas.
//
// Uso:
//   #mapa-parte(
//     parte: [Parte I -- A glicose chega ao palco],
//     centro: [Por que e como a glicose vira ATP],
//     nos: (
//       (id: "1.1", titulo: [Necessidade], texto: [cerebro/hemacia ...]),
//       (id: "1.2", titulo: [Transporte], texto: [GLUTs e SGLTs ...]),
//       (id: "1.3", titulo: [Via citosolica], texto: [2 ATP -> 4 ATP ...]),
//     ),
//     arestas: (
//       ("1.1", "1.2", [demanda exige]),
//       ("1.2", "1.3", [substrato alimenta]),
//     ),
//     fecha-com: [Moldura pronta -- agora a quimica propriamente dita.],
//   )
//
// As arestas sao tuplas (id-origem, id-destino, label). Para o layout fixo
// de 3 nos so os labels das 2 arestas (1->2 e 2->3) sao usados; os ids
// ficam como documentacao semantica. O bloco inteiro e breakable: false.
#let mapa-parte(parte: none, centro: [], nos: (), arestas: (), fecha-com: none) = block(
  breakable: false,
  width: 100%,
  above: 20pt,
  below: 12pt,
  {
    // Cabecalho: rotulo "MAPA CONCEITUAL" + nome da PARTE
    align(center,
      text(font: titulo-fam, weight: "bold", size: 8pt, fill: text-light,
        tracking: 1.6pt, upper("Mapa conceitual"))
    )
    v(3pt)
    if parte != none {
      align(center,
        text(font: titulo-fam, weight: "bold", size: 10.5pt, fill: navy,
          tracking: 0.2pt, parte)
      )
      v(10pt)
    } else {
      v(8pt)
    }

    // No central (navy, texto branco)
    align(center,
      block(
        fill: navy,
        inset: (x: 18pt, y: 12pt),
        radius: 5pt,
        width: 70%,
        breakable: false,
        align(center,
          text(font: titulo-fam, weight: "bold", size: 11.5pt,
            fill: white, tracking: 0.3pt, centro)
        )
      )
    )

    // Conector vertical (seta para baixo)
    v(2pt)
    align(center, text(size: 16pt, weight: "bold", fill: teal, "▼"))
    v(2pt)

    // Paleta rotativa dos 3 nos-filhos
    let cores-filhos = (
      (bg: teal-light, borda: teal,      tit: teal),
      (bg: bg-resumo,  borda: gold,      tit: gold),
      (bg: bg-atencao, borda: red-alert, tit: red-alert),
    )

    // Renderiza um no-filho
    let render-no(no, cor) = block(
      fill: cor.bg,
      stroke: (left: 4pt + cor.borda),
      inset: (x: 10pt, y: 9pt),
      radius: 4pt,
      width: 100%,
      breakable: false,
      {
        set par(first-line-indent: 0em, leading: 0.55em, justify: false)
        text(font: titulo-fam, weight: "bold", size: 9.5pt, fill: cor.tit,
          tracking: 0.2pt, [#no.id -- #no.titulo])
        v(4pt)
        set text(size: 8.8pt, fill: text-main)
        no.texto
      }
    )

    // Renderiza seta horizontal entre dois nos (com label da aresta)
    let render-seta(label) = align(center + horizon,
      stack(dir: ttb, spacing: 2pt,
        align(center,
          text(font: titulo-fam, size: 7.5pt, fill: text-light, style: "italic", label)
        ),
        align(center,
          text(size: 15pt, weight: "bold", fill: teal, "▸")
        )
      )
    )

    // Defensivo: completa com vazios se vier menos de 3 nos
    let n1 = if nos.len() >= 1 { nos.at(0) } else { (id: "?", titulo: [], texto: []) }
    let n2 = if nos.len() >= 2 { nos.at(1) } else { (id: "?", titulo: [], texto: []) }
    let n3 = if nos.len() >= 3 { nos.at(2) } else { (id: "?", titulo: [], texto: []) }
    let label-a1 = if arestas.len() >= 1 { arestas.at(0).at(2) } else { [] }
    let label-a2 = if arestas.len() >= 2 { arestas.at(1).at(2) } else { [] }

    // Grid 5 colunas: no1 / seta1 / no2 / seta2 / no3
    grid(
      columns: (1fr, auto, 1fr, auto, 1fr),
      column-gutter: 5pt,
      align: horizon,
      render-no(n1, cores-filhos.at(0)),
      render-seta(label-a1),
      render-no(n2, cores-filhos.at(1)),
      render-seta(label-a2),
      render-no(n3, cores-filhos.at(2)),
    )

    // Linha de fechamento (opcional, italico, navy)
    if fecha-com != none {
      v(12pt)
      align(center,
        block(width: 92%,
          align(center,
            text(font: titulo-fam, size: 10pt, style: "italic", fill: navy, fecha-com)
          )
        )
      )
    }
  }
)

// ======= Resumindo =======
// Banner gold mais "apostila" -- full-bleed visual, tracking generoso.
//
// POSICAO CANONICA 2026-05-15: o Resumindo agora aparece LOGO APOS a
// Conclusao integradora da Etapa 1 (antes da E2), nao mais no fim do PDF.
// O COMPILADOR posiciona; este helper so gera o conteudo.
#let resumindo-page(secoes) = {
  pagebreak(weak: true)
  set-etapa("Resumindo")
  block(fill: gold, inset: (x: 18pt, y: 10pt), width: 100%, radius: 4pt,
    text(font: titulo-fam, weight: "bold", size: 14pt, fill: white, tracking: 1.5pt, "Resumindo")
  )
  v(16pt)
  // TESTE 2026-05-20 (#28 Krebs): colbreak() e columns() explicita testados —
  // ambos NAO eliminam a "pagina fantasma" pos-Resumindo. Bug eh estrutural
  // do `pagebreak(weak: true)` do etapa-header subsequente. Pendencia
  // canonica para sessao de manutencao do template (investigar troca por
  // state.get + condicional).
  show: columns.with(2, gutter: 14pt)
  set par(justify: false, leading: 0.95em, spacing: 0.75em)
  for (idx, par-secao) in secoes.enumerate() {
    let (titulo, corpo) = par-secao
    if idx > 0 {
      v(6pt)
      line(length: 100%, stroke: 0.4pt + gray-border)
      v(6pt)
    }
    block(breakable: false, {
      text(font: titulo-fam, weight: "bold", size: 10.5pt, fill: navy, tracking: 0.3pt, titulo)
      v(4pt)
      set text(size: 9.5pt)
      corpo
    })
  }
}

// ====================================================================
// MINDMAP DE FECHAMENTO DA E1 (canônico 2026-05-22)
// ====================================================================
// Substitui o helper `#mapa-parte` (suspenso 2026-05-19).
//
// Filosofia: revisão visual rápida no fim da E1. NÃO é inventário; é
// curadoria. Cada peça responde: "se o aluno esquecer disso, ele ainda
// entendeu o tema?". Se sim → não entra no mapa.
//
// Estrutura em 3 zonas:
//   1. MENSAGEM — título grande + frase-síntese (a única coisa que o
//      aluno LEVA EMBORA se esquecer tudo o resto).
//   2. NARRATIVA — 3 estações em fila. Setas entre elas se houver
//      ordem temporal (Glicólise: inv → virada → pag); sem setas se
//      forem categorias paralelas (Citoesqueleto: MF · MT · FI).
//   3. DETALHE — 3 cartões pequenos no rodapé (regulação, destinos,
//      clínica, integração — varia por tema).
//
// Regra de redação (REDATOR-E1 §Mindmap de fechamento):
//   - Frase-síntese: 1 sentença, 15-25 palavras, voz dialogal
//   - Estação: rótulo (8pt all-caps) + título (12pt bold) + fala (9pt italic, 18-30 palavras)
//   - Cartão: título (8.5pt bold) + frase (8.5pt italic, 15-25 palavras)
//   - Tom: monitor explicando — sem chiste, sem mnemônico forçado
//
// Caber em 1 página é dado. Se estourar, REDUZIR conteúdo (não comprimir).

#let mindmap-cartao(titulo, frase) = block(
  fill: white,
  stroke: 0.5pt + rgb("#CFD8DC"),
  width: 100%,
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stack(spacing: 4pt,
    text(font: titulo-fam, weight: "bold", size: 8.5pt, fill: navy, titulo),
    text(size: 8.5pt, fill: rgb("#444444"), style: "italic", frase)
  )
)

#let mindmap-estacao(rotulo, titulo, fala, cor-base, cor-fundo, destaque: false) = block(
  fill: cor-fundo,
  stroke: (left: 4pt + cor-base),
  width: 100%,
  inset: (x: 14pt, y: 12pt),
  radius: 4pt,
  stack(spacing: 6pt,
    text(font: titulo-fam, weight: "bold", size: 8pt, fill: cor-base, tracking: 1.2pt,
      upper(rotulo)),
    text(font: titulo-fam, weight: "bold", size: if destaque { 13pt } else { 12pt }, fill: navy,
      titulo),
    text(size: 9pt, style: "italic", fill: rgb("#333333"), fala)
  )
)

// Paleta de cores nomeadas para `cor:` das estações.
// "a" / "b" / "c" / "neutra" abstraem a cor — REDATOR escolhe semanticamente.
#let _mindmap-cor(nome) = (
  "a":      (base: gold,    fundo: rgb("#FFF6E0")),
  "b":      (base: teal,    fundo: rgb("#E6F2F0")),
  "c":      (base: blue-clin, fundo: rgb("#E6EEF5")),
  "neutra": (base: navy,    fundo: gray-bg),
).at(nome)

// Helper principal.
//
// Parâmetros:
//   tema: string — nome do tema em caixa alta no topo (ex: "GLICÓLISE")
//   mensagem: string — frase-síntese italicizada
//   estacoes: array de 3 dicionários, cada um com:
//     - rotulo: string (8pt all-caps, ex: "Fase preparatória · R1–R5")
//     - titulo: string (12pt bold, ex: "Hexoquinase e PFK-1")
//     - fala: string (9pt italic, voz dialogal)
//     - cor: "a" | "b" | "c" | "neutra"
//     - destaque: bool (opcional, true engorda título; use no nó-pivô)
//   com-setas: bool — true para temas com ordem temporal, false para paralelos
//   rodape-titulo: string (opcional) — ex: "Quando ligar · pra onde vai · por que importa"
//   cartoes: array de 3 dicionários, cada um com:
//     - titulo: string
//     - frase: string
// SUSPENSO 2026-05-28 (canônico): mapa mental de fechamento da E1 removido
// do pipeline a pedido de Davi. Helper agora é no-op silencioso para preservar
// compatibilidade retroativa de resumos antigos que ainda chamem
// #mindmap-fechamento(...) — mesmo padrão de #neblicard / #cloze.
// Resumos NOVOS não devem chamar este helper.
#let mindmap-fechamento(
  tema: "",
  mensagem: "",
  estacoes: (),
  com-setas: false,
  rodape-titulo: none,
  cartoes: (),
) = none

// (corpo abaixo preservado em comentário só para referência caso o helper seja
// ressuscitado no futuro — não está em uso.)
#let _mindmap-fechamento-LEGACY(
  tema: "",
  mensagem: "",
  estacoes: (),
  com-setas: false,
  rodape-titulo: none,
  cartoes: (),
) = {
  assert(estacoes.len() == 3, message: "mindmap-fechamento exige exatamente 3 estações")
  assert(cartoes.len() == 3, message: "mindmap-fechamento exige exatamente 3 cartões")

  pagebreak(weak: true)

  // ===== ZONA 1 — MENSAGEM =====
  block(width: 100%, inset: (x: 0pt, y: 12pt),
    stack(spacing: 6pt,
      align(center,
        text(font: titulo-fam, weight: "bold", size: 20pt, fill: navy, tracking: 0.4pt,
          tema)
      ),
      align(center,
        text(font: corpo-fam, size: 12pt, style: "italic", fill: rgb("#444444"),
          mensagem)
      ),
    )
  )
  align(center, line(length: 12%, stroke: 1.5pt + gold))
  v(18pt)

  // ===== ZONA 2 — NARRATIVA =====
  let estacao-bloco(e) = {
    let cor = _mindmap-cor(e.cor)
    mindmap-estacao(
      e.rotulo, e.titulo, e.fala,
      cor.base, cor.fundo,
      destaque: e.at("destaque", default: false),
    )
  }

  if com-setas {
    let seta = align(horizon,
      text(size: 18pt, fill: rgb("#CFD8DC"), "→"))
    grid(
      columns: (1fr, auto, 1fr, auto, 1fr),
      column-gutter: 8pt,
      align: horizon,
      estacao-bloco(estacoes.at(0)),
      seta,
      estacao-bloco(estacoes.at(1)),
      seta,
      estacao-bloco(estacoes.at(2)),
    )
  } else {
    grid(
      columns: (1fr, 1fr, 1fr),
      column-gutter: 12pt,
      ..estacoes.map(estacao-bloco),
    )
  }

  v(20pt)

  // ===== ZONA 3 — DETALHE =====
  if rodape-titulo != none {
    align(center,
      text(font: titulo-fam, weight: "bold", size: 8pt, fill: rgb("#888888"), tracking: 1.5pt,
        upper(rodape-titulo)))
    v(8pt)
  }

  grid(
    columns: (1fr, 1fr, 1fr),
    column-gutter: 10pt,
    ..cartoes.map(c => mindmap-cartao(c.titulo, c.frase)),
  )
}
