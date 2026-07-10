// ============================================================
// caderno_v1.typ — Template Typst para cadernos de questões.
//
// Design: editorial sóbrio, anônimo. Crimson Pro (corpo serifa)
// + Montserrat (UI/labels). Paleta azul-petróleo + bege papel +
// âmbar. Sem identificação de autor, instituição ou marca.
//
// Helpers exportados:
//   caderno-doc(prova, uc_label, total, periodo, blocos)
//   capa
//   sumario(grupos)
//   abertura-bloco(nome, descricao)
//   questao-mc(id, prova, ano, aula, enunciado, alternativas)
//   questao-ce(id, prova, ano, aula, enunciado, itens)
//   secao-discursivas(questoes)
//   gabarito-consolidado(respostas)
//   apendice-explicacoes(questoes)
//
// Compilação:
//   typst compile --root .. --font-path ../fonts caderno.typ caderno.pdf
// ============================================================

// ---------- Paleta ----------
#let cor-primaria   = rgb("#1a4d6d")   // azul-petróleo
#let cor-secundaria = rgb("#3a3633")   // cinza-grafite
#let cor-acento     = rgb("#c97545")   // âmbar / terracota
#let cor-papel      = rgb("#fafaf8")   // off-white
#let cor-texto      = rgb("#1a1816")
#let cor-suave      = rgb("#5a5754")
#let cor-borda      = rgb("#d4d2ce")
#let cor-armadilha-bg = rgb("#fef5ef")
#let cor-gabarito-bg  = rgb("#f0f7fa")

// ---------- Famílias tipográficas ----------
// Merriweather: serifa estática com cobertura PT-BR completa.
// (Crimson Pro variável tinha fallback para LibertinusSerif em alguns
//  glifos, o que misturava tipografia no PDF.)
#let corpo-fam = ("Merriweather",)
#let ui-fam = ("Montserrat",)

// ---------- Setup global do documento ----------
#let caderno-doc(
  prova: "P?",
  uc_label: "Unidade Curricular",
  total: 0,
  periodo: "—",
  blocos: (),
  doc,
) = {
  set document(title: "Caderno " + prova + " — " + uc_label, author: "")

  set page(
    paper: "a4",
    margin: (top: 1.8cm, bottom: 2.0cm, left: 1.7cm, right: 1.7cm),
    fill: cor-papel,
    numbering: (n, total) => {
      // numeração só a partir da página 2
      if n > 1 {
        text(font: ui-fam, size: 8.5pt, fill: cor-suave)[#n]
      }
    },
  )

  set text(
    font: corpo-fam,
    size: 10.5pt,
    lang: "pt",
    region: "BR",
    fill: cor-texto,
    hyphenate: true,
  )

  set par(
    leading: 0.62em,
    spacing: 0.85em,
    first-line-indent: 0pt,
    justify: true,
  )

  // Heading defaults — usaremos UI font, mas helpers sobrescrevem
  show heading: set text(font: ui-fam, fill: cor-primaria)

  // Override de link (não usamos muito mas garante consistência)
  show link: set text(fill: cor-primaria)

  doc
}

// ---------- CAPA ----------
#let capa-caderno(
  prova: "",
  uc_label: "",
  total: 0,
  periodo: "—",
  blocos: (),
) = {
  // página de capa
  set page(margin: (top: 4.5cm, bottom: 3cm, left: 2.5cm, right: 2.5cm))
  align(center)[
    #text(font: ui-fam, size: 10pt, weight: 600, fill: cor-primaria,
          tracking: 2.5pt)[CADERNO DE QUESTÕES]
    #v(0.4cm)
    #text(font: ui-fam, size: 56pt, weight: 700, fill: cor-primaria,
          tracking: -1pt)[#prova]
    #v(0.2cm)
    #text(font: ui-fam, size: 18pt, weight: 600, fill: cor-secundaria)[#uc_label]
    #v(1.4cm)
    #text(font: ui-fam, size: 10.5pt, fill: cor-suave)[
      #total questões · período #periodo
    ]
    #v(2.2cm)
    #text(font: ui-fam, size: 8.5pt, weight: 600, fill: cor-suave,
          tracking: 1.5pt)[CONTEÚDO PROGRAMÁTICO]
    #v(0.5cm)
    #block(width: 11cm)[
      #set align(center)
      #set par(justify: false)
      #for (i, b) in blocos.enumerate() [
        #box(
          inset: (x: 0.5cm, y: 0.25cm),
          stroke: 0.5pt + cor-borda,
          radius: 2pt,
          fill: white,
        )[#text(font: ui-fam, size: 9pt, weight: 500, fill: cor-secundaria)[#b]]
        #h(0.25cm)
      ]
    ]
  ]
  pagebreak()
}

// ---------- SUMÁRIO ----------
// grupos = ((bloco: str, aulas: ((titulo: str, n_questoes: int), ...)), ...)
#let sumario(grupos) = {
  v(0.3cm)
  align(center, text(font: ui-fam, size: 22pt, weight: 700,
                     fill: cor-primaria)[Sumário])
  v(0.8cm)
  for g in grupos {
    block(
      below: 0.7cm,
      breakable: false,
      [
        #text(font: ui-fam, size: 13pt, weight: 700, fill: cor-primaria)[#g.bloco]
        #v(-0.15cm)
        #line(length: 100%, stroke: 1.5pt + cor-primaria)
        #v(0.2cm)
        #for a in g.aulas {
          grid(
            columns: (1fr, auto),
            gutter: 0.5cm,
            text(size: 10pt)[#a.titulo],
            text(font: ui-fam, size: 9.5pt, weight: 600, fill: cor-suave)[
              #a.n_questoes questões
            ],
          )
          v(0.12cm)
          line(length: 100%, stroke: 0.4pt + cor-borda)
          v(0.12cm)
        }
      ],
    )
  }
  pagebreak()
}

// ---------- ABERTURA DE BLOCO ----------
#let abertura-bloco(nome, descricao) = {
  v(0.8cm)
  block(
    breakable: false,
    spacing: 0.6cm,
    [
      #line(length: 100%, stroke: 3pt + cor-primaria)
      #v(0.25cm)
      #text(font: ui-fam, size: 20pt, weight: 700, fill: cor-primaria)[#nome]
      #v(0.15cm)
      #text(size: 10pt, fill: cor-suave, style: "italic")[#descricao]
      #v(0.15cm)
      #line(length: 100%, stroke: 0.5pt + cor-borda)
    ],
  )
  v(0.3cm)
}

// ---------- BLOCO DE FIGURA / AVISO ----------
// Se `figura` for caminho de arquivo existente → embute imagem
// Se `precisa_figura` true e sem arquivo → aviso visual
#let bloco-figura(figura: none, precisa-figura: false, descricao: none) = {
  if figura != none and figura != "" {
    v(0.3cm)
    align(center)[
      #box(stroke: 0.5pt + cor-borda, inset: 6pt, radius: 2pt)[
        #image("/banco/figuras/" + figura, width: 85%)
      ]
    ]
    v(0.2cm)
  } else if precisa-figura {
    v(0.25cm)
    block(
      width: 100%,
      fill: cor-armadilha-bg,
      stroke: (left: 2pt + cor-acento),
      inset: (x: 0.4cm, y: 0.3cm),
      [
        #text(font: ui-fam, size: 8pt, weight: 700,
              fill: cor-acento, tracking: 1pt)[FIGURA REFERENCIADA]
        #v(0.1cm)
        #text(size: 9pt, fill: cor-suave, style: "italic")[
          #if descricao != none and descricao != "" [
            #descricao
          ] else [
            Esta questão usa uma figura/gráfico no enunciado original
            que não está disponível no banco. Consulte a prova original
            ou recorte e salve em `banco/figuras/q-XXXX.png` e adicione
            `figura: q-XXXX.png` ao frontmatter.
          ]
        ]
      ],
    )
    v(0.15cm)
  }
}

// ---------- BADGE LATERAL (compartilhado) ----------
#let badge-questao(id, prova, ano, aula) = {
  set text(font: ui-fam, size: 7.5pt, fill: cor-suave)
  stack(
    spacing: 0.15em,
    text(size: 11.5pt, weight: 700, fill: cor-primaria)[#id],
    text(weight: 500)[#prova · #ano],
    text(weight: 500)[#aula],
  )
}

// ---------- QUESTÃO MC ----------
// alternativas = (("A", content), ("B", content), ...)
#let questao-mc(
  id: "?",
  prova: "P?",
  ano: "—",
  aula: "",
  enunciado: [],
  alternativas: (),
  figura: none,
  precisa-figura: false,
  figura-descricao: none,
  permite-quebra: false,
) = {
  block(
    breakable: permite-quebra,
    below: 0.5cm,
    [
      #grid(
        columns: (2.1cm, 1fr),
        gutter: 0.3cm,
        badge-questao(id, prova, ano, aula),
        block(
          width: 100%,
          inset: (x: 0.5cm, y: 0.45cm),
          stroke: 0.5pt + cor-borda,
          radius: 2.5pt,
          fill: white,
          [
            #enunciado
            #bloco-figura(figura: figura,
                          precisa-figura: precisa-figura,
                          descricao: figura-descricao)
            #v(0.2cm)
            #for (letra, texto) in alternativas {
              grid(
                columns: (0.8cm, 1fr),
                gutter: 0.3cm,
                text(font: ui-fam, weight: 700, fill: cor-primaria)[#letra)],
                texto,
              )
              v(0.12cm)
            }
          ],
        ),
      )
    ],
  )
}

// ---------- QUESTÃO CE ----------
// itens = (("1", content), ("2", content), ...)  ou  (("A", content), ...)
#let questao-ce(
  id: "?",
  prova: "P?",
  ano: "—",
  aula: "",
  enunciado: [],
  itens: (),
  figura: none,
  precisa-figura: false,
  figura-descricao: none,
  permite-quebra: false,
) = {
  block(
    breakable: permite-quebra,
    below: 0.5cm,
    [
      #grid(
        columns: (2.1cm, 1fr),
        gutter: 0.3cm,
        badge-questao(id, prova, ano, aula),
        block(
          width: 100%,
          inset: (x: 0.5cm, y: 0.45cm),
          stroke: 0.5pt + cor-borda,
          radius: 2.5pt,
          fill: white,
          [
            #enunciado
            #bloco-figura(figura: figura,
                          precisa-figura: precisa-figura,
                          descricao: figura-descricao)
            #v(0.25cm)
            #for (marker, texto) in itens {
              grid(
                columns: (0.8cm, 1fr, 1.6cm),
                gutter: 0.3cm,
                text(font: ui-fam, weight: 700, fill: cor-primaria)[#marker.],
                texto,
                align(right)[
                  #box(width: 0.55cm, height: 0.55cm,
                       stroke: 0.7pt + cor-primaria, radius: 1pt)[
                    #align(center+horizon)[#text(font: ui-fam, size: 8pt, weight: 600)[C]]
                  ]
                  #h(0.1cm)
                  #box(width: 0.55cm, height: 0.55cm,
                       stroke: 0.7pt + cor-primaria, radius: 1pt)[
                    #align(center+horizon)[#text(font: ui-fam, size: 8pt, weight: 600)[E]]
                  ]
                ],
              )
              v(0.18cm)
            }
          ],
        ),
      )
    ],
  )
}

// ---------- SEÇÃO DISCURSIVAS ----------
// questoes = (((id, prova, ano, aula, enunciado, linhas), ...))
#let secao-discursivas(questoes) = {
  if questoes.len() == 0 { return }
  pagebreak(weak: true)
  v(0.3cm)
  align(center, text(font: ui-fam, size: 20pt, weight: 700,
                     fill: cor-primaria)[Questões Discursivas])
  v(-0.15cm)
  align(center, line(length: 4cm, stroke: 2pt + cor-primaria))
  v(0.8cm)

  for q in questoes {
    let linhas = q.at("linhas", default: 12)
    let altura = linhas * 0.65cm
    block(
      breakable: q.at("permite-quebra", default: false),
      below: 0.7cm,
      [
        #grid(
          columns: (2.1cm, 1fr),
          gutter: 0.3cm,
          badge-questao(q.id, q.prova, q.ano, q.aula),
          block(
            width: 100%,
            inset: (x: 0.5cm, y: 0.45cm),
            stroke: 0.5pt + cor-borda,
            radius: 2.5pt,
            fill: white,
            [
              #q.enunciado
              #bloco-figura(
                figura: q.at("figura", default: none),
                precisa-figura: q.at("precisa-figura", default: false),
                descricao: q.at("figura-descricao", default: none),
              )
              #v(0.3cm)
              // espaço pautado
              #block(
                width: 100%,
                height: altura,
                stroke: none,
                inset: 0pt,
                {
                  let n_linhas = calc.floor(linhas)
                  for i in range(n_linhas) {
                    line(length: 100%, stroke: 0.4pt + cor-borda)
                    v(0.65cm - 0.4pt, weak: false)
                  }
                },
              )
            ],
          ),
        )
      ],
    )
  }
}

// ---------- GABARITO CONSOLIDADO ----------
// respostas = ((id, resposta), ...)
#let gabarito-consolidado(respostas) = {
  if respostas.len() == 0 { return }
  pagebreak(weak: true)
  v(0.3cm)
  align(center, text(font: ui-fam, size: 22pt, weight: 700,
                     fill: cor-primaria)[Gabarito])
  v(0.8cm)
  // grid 5 colunas
  block(
    width: 16cm,
    [
      #set align(center)
      #grid(
        columns: (1fr,) * 5,
        gutter: 0.25cm,
        ..respostas.map(r => block(
          width: 100%,
          inset: (x: 0.3cm, y: 0.25cm),
          stroke: 0.5pt + cor-borda,
          radius: 2pt,
          fill: white,
          [
            #grid(
              columns: (1fr, auto),
              gutter: 0.2cm,
              text(font: ui-fam, size: 9pt, weight: 700, fill: cor-suave)[#r.id],
              text(font: ui-fam, size: 9.5pt, weight: 700, fill: cor-primaria)[#r.resposta],
            )
          ],
        )),
      )
    ],
  )
}

// ---------- APÊNDICE DE EXPLICAÇÕES ----------
// questoes = (((id, prova, ano, aula, resumo, armadilha, explicacao, gabarito), ...))
#let apendice-explicacoes(questoes) = {
  if questoes.len() == 0 { return }
  pagebreak()
  // página de abertura do apêndice
  v(2cm)
  align(center)[
    #line(length: 6cm, stroke: 2pt + cor-primaria)
    #v(0.3cm)
    #text(font: ui-fam, size: 11pt, weight: 700, fill: cor-primaria,
          tracking: 3pt)[DESTACÁVEL]
    #v(1.5cm)
    #text(font: ui-fam, size: 28pt, weight: 700, fill: cor-primaria)[Explicações Detalhadas]
  ]
  pagebreak()

  for q in questoes {
    block(
      breakable: true,
      below: 1cm,
      [
        #grid(
          columns: (2.1cm, 1fr),
          gutter: 0.3cm,
          badge-questao(q.id, q.prova, q.ano, q.aula),
          block(
            width: 100%,
            [
              #text(weight: 600, fill: cor-secundaria)[#q.resumo]
              #v(0.3cm)
              // armadilha em destaque
              #block(
                width: 100%,
                fill: cor-armadilha-bg,
                stroke: (left: 2.5pt + cor-acento),
                inset: (x: 0.4cm, y: 0.3cm),
                [
                  #text(font: ui-fam, size: 7.5pt, weight: 700,
                        fill: cor-acento, tracking: 1.2pt)[ARMADILHA COMUM]
                  #v(0.15cm)
                  #text(size: 9.5pt)[#q.armadilha]
                ],
              )
              #v(0.35cm)
              #q.explicacao
              #v(0.3cm)
              #box(
                fill: cor-gabarito-bg,
                inset: (x: 0.4cm, y: 0.2cm),
                radius: 2pt,
                text(font: ui-fam, size: 9.5pt, weight: 700,
                     fill: cor-primaria)[Gabarito: #q.gabarito],
              )
            ],
          ),
        )
      ],
    )
  }
}
