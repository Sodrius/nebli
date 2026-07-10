// ===========================================================
// NEBLI v3 — estilo canônico em Typst
// Substituto de typst para o template HTML + WeasyPrint
// Tipografia: DejaVu Sans (títulos) + DejaVu Serif (corpo).
// Paleta espelhada do template HTML canônico.
// ===========================================================

#let navy        = rgb("#1B2A4A")
#let teal        = rgb("#2A7A6B")
#let teal-light  = rgb("#E8F5F1")
#let gold        = rgb("#D4920A")
#let red-alert   = rgb("#C0392B")
#let blue-clin   = rgb("#2874A6")
#let green-cons  = rgb("#1E8449")  // badge consolidação (TAXONOMIA: verde — fácil)
#let blue-light  = rgb("#5DADE2")  // [DEPRECATED 2026-05-13 — antes era badge consolidação]
#let violet      = rgb("#7D3C98")  // badge aplicação (TAXONOMIA: violeta — difícil)
#let gray-bg     = rgb("#F4F4F4")
#let gray-border = rgb("#D5D8DC")
#let text-main   = rgb("#2C3E50")
#let text-light  = rgb("#5D6D7E")
#let bg-clinica  = rgb("#EBF5FB")
#let bg-atencao  = rgb("#FDEDEC")
#let bg-mini     = rgb("#F8FAF9")
#let bg-resumo   = rgb("#FEF9E7")

// Mesmas fontes do PDF HTML antigo (WeasyPrint caía no DejaVu por não
// conseguir carregar as woff2 do projeto, que eram Thin/Light, não Regular).
// O "look" canônico dos resumos passados é DejaVu Sans + DejaVu Serif.
#let titulo-fam = ("DejaVu Sans",)
#let corpo-fam  = ("DejaVu Serif",)

// ======= Página padrão =======
#let pagina-padrao(corpo) = {
  set page(
    paper: "a4",
    margin: (top: 1.8cm, bottom: 2cm, left: 1.7cm, right: 1.7cm),
    header: context {
      let val = state("etapa", "").get()
      grid(columns: (1fr, 1fr),
        align: (left, right),
        text(font: titulo-fam, weight: "bold", size: 8pt, fill: rgb("#CCCCCC"), tracking: 2pt, "NEBLI"),
        text(font: titulo-fam, size: 8pt, fill: rgb("#CCCCCC"), val)
      )
    },
    footer: align(center, text(font: titulo-fam, size: 9pt, fill: rgb("#999999"), context counter(page).display())),
  )
  set text(font: corpo-fam, size: 10.5pt, fill: text-main, lang: "pt", region: "BR", hyphenate: false)
  set par(justify: true, leading: 0.78em, first-line-indent: 0em, linebreaks: "optimized")
  set heading(numbering: none)
  show strong: set text(fill: navy)
  show emph: set text(fill: text-light)
  // Footnotes canônicas NEBLI (compactas, discretas) — ver helper #termo-nota
  set footnote.entry(separator: line(length: 30%, stroke: 0.5pt + gray-border))
  show footnote.entry: it => text(size: 8pt, fill: text-light, it)
  corpo
}

// ======= Atualiza a string do header =======
#let set-etapa(nome) = state("etapa", "").update(nome)

// ======= Banner de etapa =======
#let etapa-header(titulo) = {
  pagebreak(weak: true)
  set-etapa(titulo)
  block(
    fill: navy, inset: (x: 18pt, y: 12pt), width: 100%, radius: 0pt,
    text(font: titulo-fam, size: 16pt, weight: "bold", fill: white, titulo)
  )
  v(12pt)
}

// ======= Parte (PARTE I, II, III) =======
#let parte-title(titulo, primeira: false) = {
  if not primeira { v(8pt) }
  block(below: 12pt, breakable: false,
    stack(
      text(font: titulo-fam, size: 14pt, weight: "bold", fill: navy, titulo),
      v(4pt),
      line(length: 100%, stroke: 2.5pt + teal)
    )
  )
}

// ======= Subtópico (1.1, 1.2…) =======
#let subtopico(titulo) = {
  v(10pt)
  block(below: 6pt, breakable: false,
    text(font: titulo-fam, size: 11.5pt, weight: "bold", fill: teal, titulo)
  )
}

// ======= Boxes =======
#let _box(bg, borda-cor, conteudo, titulo: none, titulo-cor: none, borda-l: 4pt) = {
  block(
    fill: bg,
    stroke: (left: borda-l + borda-cor),
    inset: (x: 14pt, y: 10pt),
    width: 100%,
    radius: 0pt,
    breakable: false,
    {
      if titulo != none {
        text(font: titulo-fam, weight: "bold", size: 9.5pt, fill: titulo-cor, titulo)
        v(3pt)
      }
      set text(size: 9.5pt)
      conteudo
    }
  )
}

#let intro-box(conteudo) = _box(gray-bg, navy, conteudo, borda-l: 5pt)

#let atencao-box(titulo, conteudo) = _box(bg-atencao, red-alert, conteudo,
  titulo: titulo, titulo-cor: red-alert, borda-l: 5pt)

#let clinica-box(titulo, conteudo) = _box(bg-clinica, blue-clin, conteudo,
  titulo: titulo, titulo-cor: blue-clin, borda-l: 5pt)

#let sintese-box(numero, conteudo) = block(
  fill: teal-light,
  stroke: (left: 5pt + teal),
  inset: (x: 14pt, y: 10pt),
  width: 100%,
  breakable: false,
  {
    set text(size: 9.5pt)
    [#text(weight: "bold", fill: teal)[Síntese #numero —] #conteudo]
  }
)

#let mini-resumo(conteudo) = block(
  fill: bg-mini,
  stroke: (left: 3pt + teal),
  inset: (x: 12pt, y: 7pt),
  width: 100%,
  breakable: false,
  {
    set text(size: 9.5pt, style: "italic")
    [#text(weight: "bold", fill: teal, style: "normal")[Resumindo até aqui:] #conteudo]
  }
)

#let conclusao-box(conteudo) = block(
  fill: bg-clinica,
  stroke: 1.5pt + blue-clin,
  inset: (x: 14pt, y: 12pt),
  width: 100%,
  radius: 4pt,
  breakable: false,
  {
    text(font: titulo-fam, weight: "bold", size: 11pt, fill: blue-clin, "Conclusão integradora")
    v(5pt)
    conteudo
  }
)

// ======= Figura NEBLI (com legenda) =======
#let figura-nebli(caminho, legenda, largura: 80%) = {
  v(8pt)
  align(center,
    block(breakable: false,
      stack(
        image(caminho, width: largura),
        v(6pt),
        align(left,
          text(size: 9pt, style: "italic", fill: text-light, legenda)
        )
      )
    )
  )
  v(8pt)
}

// ======= Badges (nível das questões) =======
#let _badge(cor, texto) = box(
  fill: cor, inset: (x: 6pt, y: 1.5pt), radius: 8pt, baseline: 1pt,
  text(font: titulo-fam, size: 7.5pt, weight: "bold", fill: white, texto)
)
// TAXONOMIA CANÔNICA (definida em 2026-05-13):
//   Consolidação = VERDE  (fácil — recall direto, definições, mecanismos isolados)
//   Integração   = AZUL   (médio — conectar dois ou mais subtópicos)
//   Aplicação    = VIOLETA (difícil — cenário clínico/aplicação raciocínio)
#let badge-consolidacao = _badge(green-cons, "Consolidação")
#let badge-integracao   = _badge(blue-clin,  "Integração")
#let badge-aplicacao    = _badge(violet,     "Aplicação")
#let badge-prioritario  = _badge(red-alert,  "Prioritário")

// Badge de relevância clínica (capa) — [DEPRECATED 2026-05-13]
// Relevância clínica não aparece mais na capa do PDF. Manter o helper apenas
// para compatibilidade com resumos antigos; NÃO usar em resumos novos.
#let badge-rel-alta = box(fill: gold, inset: (x: 6pt, y: 1.5pt), radius: 8pt, baseline: 1pt,
  text(font: titulo-fam, size: 7.5pt, weight: "bold", fill: white, "Alta"))

// ======= Questão MC =======
#let questao-mc(numero, badge, enunciado, alts) = block(below: 14pt, breakable: false, {
  text(font: titulo-fam, size: 10.5pt, weight: "bold", fill: navy, [Questão #numero ])
  h(4pt)
  badge
  v(5pt)
  enunciado
  v(4pt)
  for (letra, conteudo) in alts {
    pad(left: 8pt, [*#letra)* #conteudo])
    v(2pt)
  }
  v(6pt)
  line(length: 100%, stroke: 0.5pt + gray-border)
})

// ======= Questão C/E =======
#let questao-ce(numero, badge, enunciado, itens) = block(below: 14pt, breakable: false, {
  text(font: titulo-fam, size: 10.5pt, weight: "bold", fill: navy, [Questão #numero ])
  h(4pt)
  badge
  v(5pt)
  enunciado
  v(2pt)
  text(size: 9.5pt, style: "italic", fill: text-light, "Cada item deve ser julgado de forma independente.")
  v(4pt)
  for (rom, conteudo) in itens {
    pad(left: 8pt, [#text(weight: "bold")[#rom.] #conteudo])
    v(2pt)
  }
  v(6pt)
  line(length: 100%, stroke: 0.5pt + gray-border)
})

// ======= Discursiva =======
#let discursiva(numero, enunciado, modelo, titulo-q: none) = block(
  fill: rgb("#F0F7F4"),
  stroke: 1pt + teal,
  inset: (x: 14pt, y: 12pt),
  width: 100%,
  radius: 4pt,
  breakable: false,
  below: 16pt,
  {
    text(font: titulo-fam, weight: "bold", size: 11pt, fill: navy,
      if titulo-q != none { titulo-q } else [Questão #numero]
    )
    v(4pt)
    enunciado
    v(8pt)
    block(
      fill: rgb("#E8F4F0"),
      stroke: 1pt + teal,
      inset: (x: 12pt, y: 10pt),
      radius: 3pt,
      {
        text(font: titulo-fam, weight: "bold", size: 8.5pt, fill: teal, tracking: 1pt, "MODELO DE RESPOSTA")
        v(4pt)
        set text(size: 10pt)
        modelo
      }
    )
  }
)

// ======= Prova-block (Etapa 4) =======
#let prova-block(badge, enunciado, alts, gabarito-letra, justificativa) = block(
  fill: rgb("#FFFBF0"),
  stroke: 1pt + rgb("#F0D78C"),
  inset: (x: 14pt, y: 12pt),
  width: 100%,
  radius: 3pt,
  breakable: false,
  below: 14pt,
  {
    badge
    v(5pt)
    enunciado
    v(4pt)
    for (letra, conteudo) in alts {
      pad(left: 8pt, [*#letra)* #conteudo])
      v(2pt)
    }
    v(6pt)
    block(
      fill: teal-light, stroke: (left: 3pt + teal),
      inset: (x: 12pt, y: 8pt),
      width: 100%,
      {
        set text(size: 9.5pt)
        [#text(weight: "bold", fill: teal)[Gabarito #gabarito-letra —] #justificativa]
      }
    )
  }
)

// ======= NEBLIcard =======
#let neblicard(contexto, pergunta, resposta) = block(
  stroke: (left: 4pt + teal, top: 0.5pt + gray-border, right: 0.5pt + gray-border, bottom: 0.5pt + gray-border),
  inset: (x: 14pt, y: 11pt),
  width: 100%,
  radius: 3pt,
  breakable: false,
  below: 12pt,
  {
    text(font: titulo-fam, weight: "bold", size: 8.5pt, fill: teal,
      tracking: 0.6pt, upper(contexto))
    v(4pt)
    text(font: corpo-fam, weight: "bold", size: 10.5pt, fill: navy, pergunta)
    v(6pt)
    line(length: 100%, stroke: 0.4pt + gray-border)
    v(6pt)
    set text(size: 10pt)
    resposta
  }
)

#let seta = text(weight: "bold", fill: teal, " → ")
#let cloze(t) = box(fill: rgb("#FFF3CD"), inset: (x: 3pt, y: 1pt), radius: 2pt,
  text(weight: "bold", fill: navy, t))

// ======= Capa =======
#let capa(titulo, subtitulo, meta) = {
  set page(paper: "a4", margin: 0pt, header: none, footer: none,
    background: place(top + left,
      rect(width: 21cm, height: 12.5cm, fill: navy, stroke: none)
    )
  )

  // TEXTO SOBRE A FAIXA NAVY
  block(width: 100%, height: 12.5cm, inset: (x: 18mm, y: 0pt),
    {
      v(7cm)
      text(font: titulo-fam, weight: "bold", size: 10pt,
        fill: rgb("#AAB1C0"), tracking: 6pt, upper("NEBLI · UC1"))
      v(8pt)
      text(font: titulo-fam, weight: "bold", size: 28pt, fill: white, titulo)
      v(6pt)
      text(font: titulo-fam, size: 12pt, fill: rgb("#D5DAE3"), subtitulo)
    }
  )

  // META
  block(width: 100%, inset: (x: 18mm, y: 14mm),
    {
      set text(font: titulo-fam, size: 9.5pt)
      for (rotulo, valor) in meta {
        block(below: 7pt,
          grid(columns: (4.5cm, 1fr), column-gutter: 6pt,
            text(weight: "bold", fill: navy, [#rotulo:]),
            valor
          )
        )
      }
      v(8pt)
      block(stroke: (top: 0.5pt + rgb("#E0E0E0")), inset: (top: 9pt),
        text(font: corpo-fam, size: 9pt, style: "italic", fill: rgb("#666"),
          "Material elaborado a partir dos slides da disciplina. Recomenda-se estudar com o material original aberto ao lado, pois o resumo complementa — não substitui — a aula."))
    }
  )

  // RODAPE
  place(bottom + center,
    block(width: 100%, fill: gray-bg, stroke: (top: 0.5pt + gray-border),
      inset: (x: 18mm, y: 12pt),
      align(center, stack(
        text(font: titulo-fam, size: 8.5pt, fill: rgb("#888"), "Davi Sousa — Turma 114"),
        v(3pt),
        text(font: titulo-fam, size: 8.5pt, weight: "bold", fill: rgb("#555"),
          "(61) 98264-7208  ·  dpbdes@gmail.com  ·  PIX: dpbdes@gmail.com")
      ))
    )
  )

  pagebreak()
}

// ======= Sumário =======
#let sumario(estrutura) = {
  set page(margin: (top: 1.8cm, bottom: 2cm, left: 1.7cm, right: 1.7cm))
  set-etapa("Sumário")
  text(font: titulo-fam, size: 18pt, weight: "bold", fill: navy, "Sumário")
  block(below: 18pt, line(length: 100%, stroke: 2.5pt + teal))
  for (etapa, partes) in estrutura {
    block(below: 4pt,
      text(font: titulo-fam, weight: "bold", size: 10pt, fill: navy, tracking: 0.5pt, upper(etapa))
    )
    for (parte, itens) in partes {
      if parte != none {
        block(below: 2pt,
          pad(left: 8pt,
            text(font: titulo-fam, weight: "bold", size: 9.5pt, fill: teal, parte))
        )
      }
      for it in itens {
        block(below: 1.5pt,
          pad(left: 20pt,
            text(size: 9pt, it))
        )
      }
    }
    v(6pt)
  }
  pagebreak()
}

// ======= Gabarito grid =======
#let gabarito-bloco(titulo, items) = {
  block(below: 6pt,
    text(font: titulo-fam, weight: "bold", size: 10pt, fill: teal,
      tracking: 0.5pt, upper(titulo))
  )
  let cols = 5
  grid(
    columns: (1fr,) * cols, gutter: 6pt, row-gutter: 4pt,
    ..items.map(((q, g)) => [#text(weight: "bold", fill: navy)[Q#q] #g])
  )
  v(10pt)
}

#let gabarito-page(blocos) = {
  pagebreak(weak: true)
  set-etapa("Gabarito — Etapa 2")
  text(font: titulo-fam, size: 16pt, weight: "bold", fill: navy, "Gabarito — Etapa 2")
  block(below: 16pt, line(length: 100%, stroke: 2pt + teal))
  for (titulo, items) in blocos {
    gabarito-bloco(titulo, items)
  }
}

// ======= Footnote canônica NEBLI =======
// Substituto do glossário (descontinuado em 2026-05-13).
// Uso: #termo-nota[acetilcolina][principal neurotransmissor da JNM, liberado em vesículas via SNARE]
// Aparece como "acetilcolina¹" no texto + nota no rodapé da página.
// Calibração: 5–10 footnotes por resumo. Apenas termos novos críticos com alto reuso.
#let termo-nota(termo, def) = {
  [#termo#footnote[#text(font: titulo-fam, weight: "bold", size: 8pt, fill: navy, termo) #text(size: 8pt, fill: text-light)[— #def]]]
}

// ======= Glossário [DEPRECATED 2026-05-13] =======
// NÃO usar em resumos novos. Substituto: #termo-nota nas páginas da Etapa 1.
// Função mantida apenas para retrocompatibilidade com PDFs antigos.
#let glossario(intro, termos) = {
  pagebreak(weak: true)
  set-etapa("Glossário")
  text(font: titulo-fam, size: 16pt, weight: "bold", fill: navy, "Glossário")
  block(below: 14pt, line(length: 100%, stroke: 2pt + teal))
  block(below: 12pt,
    text(font: corpo-fam, size: 9.5pt, style: "italic", fill: text-light, intro)
  )
  show: columns.with(2, gutter: 12pt)
  for (termo, definicao) in termos {
    block(below: 7pt, breakable: false,
      [#text(font: titulo-fam, weight: "bold", size: 9.5pt, fill: navy, termo) #h(2pt)— #text(size: 9.5pt, definicao)]
    )
  }
}

// ======= Resumindo =======
#let resumindo-page(secoes) = {
  pagebreak(weak: true)
  set-etapa("Resumindo")
  block(fill: gold, inset: (x: 16pt, y: 8pt), width: 100%,
    text(font: titulo-fam, weight: "bold", size: 13pt, fill: white, tracking: 1pt, "Resumindo")
  )
  v(10pt)
  show: columns.with(2, gutter: 10pt)
  for (titulo, corpo) in secoes {
    block(below: 8pt, breakable: false, {
      text(font: titulo-fam, weight: "bold", size: 9.5pt, fill: navy, titulo)
      v(2pt)
      set text(size: 9pt)
      corpo
    })
  }
}
