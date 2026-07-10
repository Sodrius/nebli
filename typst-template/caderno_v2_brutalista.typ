/*
 * CADERNO DE QUESTÕES — IDENTIDADE BRUTALISTA (v2, 2026-05-24)
 *
 * Adaptação da identidade brutalista (Claude Design 2026-05-22) para
 * a API do pipeline gerar_caderno.py.
 *
 * MEMÓRIA DESCRITIVA (do designer):
 * Brutalismo funcional — a forma segue a função, sem ornamento. Grid
 * rígido, tipografia monocromática, hierarquia por peso e tamanho.
 * O material é sério; o design não compete com o conteúdo, ele o
 * organiza.
 *
 * Tipografia: Montserrat em toda a extensão (família única, peso
 * variável). Neo-grotesca de desenho preciso, legibilidade alta em
 * corpo pequeno, distinção clara entre pesos.
 * Cromática: Preto puro #000000 sobre branco aquecido #FFFEF8. Único
 * acento cinza #666666 para metadados.
 * Diferenciação de formato por estrutura, não por cor:
 *   - MC: círculos vazios para marcação
 *   - CE: boxes C/E lado a lado
 *   - Discursiva: linhas pautadas
 * Gabarito: tabela 5 colunas, fonte monoespaçada, compacta.
 */

// ---------- Paleta ----------
#let cor-tinta = rgb("#000000")
#let cor-papel = rgb("#FFFEF8")
#let cor-suave = rgb("#666666")
#let cor-borda-leve = rgb("#CCCCCC")
#let cor-aviso-fundo = rgb("#F8F8F8")
#let cor-aviso-texto = rgb("#999999")

// ---------- Famílias tipográficas ----------
#let corpo-fam = ("Montserrat",)
#let mono-fam = ("DejaVu Sans Mono",)


// ============================================================
// SETUP DO DOCUMENTO (wrapper show:)
// ============================================================

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
    margin: (top: 1.8cm, bottom: 2cm, left: 1.8cm, right: 1.8cm),
    fill: cor-papel,
    numbering: (n, total) => {
      if n > 1 {
        text(font: corpo-fam, size: 8pt, weight: "light", fill: cor-suave)[#n]
      }
    },
    number-align: center,
  )

  set text(
    font: corpo-fam,
    size: 10.5pt,
    lang: "pt",
    region: "BR",
    fill: cor-tinta,
    hyphenate: true,
  )

  set par(
    justify: true,
    leading: 0.6em,
    spacing: 1em,
    first-line-indent: 0pt,
  )

  doc
}


// ============================================================
// CAPA
// ============================================================

#let capa-caderno(
  prova: "",
  uc_label: "",
  total: 0,
  periodo: "—",
  blocos: (),
) = {
  set page(numbering: none)
  set align(left)

  v(6cm)

  text(size: 72pt, weight: "bold", prova)

  v(1.5cm)

  text(size: 14pt, weight: "regular", uc_label)

  v(0.8cm)

  text(size: 11pt, weight: "light", fill: cor-suave)[
    #total questões · #periodo
  ]

  v(2cm)

  if blocos.len() > 0 {
    text(size: 9pt, weight: "light", fill: cor-suave)[
      #blocos.join(" · ")
    ]
  }

  pagebreak()
}


// ============================================================
// SUMÁRIO
// ============================================================
// Recebe grupos = ((bloco, aulas: ((titulo, n_questoes), ...)), ...)

#let sumario(grupos) = {
  text(size: 20pt, weight: "bold")[SUMÁRIO]
  v(1.5em)

  for g in grupos {
    text(size: 12pt, weight: "bold")[#g.bloco]
    v(0.5em)

    for aula in g.aulas {
      grid(
        columns: (1fr, auto),
        text(size: 9.5pt, weight: "regular")[#aula.titulo],
        text(size: 9.5pt, weight: "light", fill: cor-suave)[#aula.n_questoes],
      )
      v(0.3em)
    }

    v(1.2em)
  }

  pagebreak()
}


// ============================================================
// ABERTURA DE BLOCO (cabeçalho de disciplina dentro do corpo)
// ============================================================

#let abertura-bloco(nome, descricao) = {
  v(0.5em)
  text(size: 16pt, weight: "bold")[#upper(nome)]
  if descricao != none and descricao != "" {
    v(0.2em)
    text(size: 9.5pt, weight: "light", fill: cor-suave)[#descricao]
  }
  v(1em)
}


// ============================================================
// HELPER INTERNO: AVISO DE FIGURA REFERENCIADA
// ============================================================

#let _bloco-figura(figura: none, precisa-figura: false, descricao: none) = {
  if figura != none and figura != "" {
    v(0.4em)
    align(center)[
      #box(stroke: 0.5pt + cor-borda-leve, inset: 6pt)[
        #image("/banco/figuras/" + figura, width: 85%)
      ]
    ]
    v(0.4em)
  } else if precisa-figura {
    v(0.4em)
    rect(
      width: 100%,
      stroke: 0.5pt + cor-borda-leve,
      fill: cor-aviso-fundo,
      inset: 0.6cm,
    )[
      #align(center)[
        #text(size: 8.5pt, fill: cor-aviso-texto, style: "italic")[
          #if descricao != none and descricao != "" [#descricao]
          else [figura referenciada — consultar prova original]
        ]
      ]
    ]
    v(0.4em)
  }
}


// ============================================================
// BADGE DE METADADOS (linha única acima do enunciado)
// ============================================================

#let _badge(id, prova, ano, aula) = {
  text(size: 8pt, weight: "light", fill: cor-suave)[
    #id · #prova · #ano · #aula
  ]
}


// ============================================================
// QUESTÃO MC
// ============================================================

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
    below: 1.5em,
    [
      #_badge(id, prova, ano, aula)
      #v(0.4em)
      #text(size: 10.5pt, weight: "medium")[#enunciado]
      #_bloco-figura(figura: figura,
                     precisa-figura: precisa-figura,
                     descricao: figura-descricao)
      #v(0.6em)
      #for (letra, texto) in alternativas {
        grid(
          columns: (1.2cm, 1fr),
          gutter: 0.4cm,
          align(left + horizon)[
            #circle(radius: 0.32em, stroke: 1pt + cor-tinta)
            #h(0.3em)
            #text(weight: "medium")[#letra]
          ],
          text[#texto],
        )
        v(0.35em)
      }
    ],
  )
}


// ============================================================
// QUESTÃO CE
// ============================================================

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
    below: 1.5em,
    [
      #_badge(id, prova, ano, aula)
      #v(0.4em)
      #text(size: 10.5pt, weight: "medium")[#enunciado]
      #_bloco-figura(figura: figura,
                     precisa-figura: precisa-figura,
                     descricao: figura-descricao)
      #v(0.6em)
      #for (marker, texto) in itens {
        grid(
          columns: (1.2cm, 1fr, 2.1cm),
          gutter: 0.4cm,
          align(left + horizon)[
            #text(weight: "medium")[#marker]
          ],
          text[#texto],
          grid(
            columns: (1fr, 1fr),
            gutter: 0.2cm,
            rect(width: 100%, height: 1.2em, stroke: 1pt + cor-tinta)[
              #align(center + horizon)[
                #text(size: 8pt, weight: "medium")[C]
              ]
            ],
            rect(width: 100%, height: 1.2em, stroke: 1pt + cor-tinta)[
              #align(center + horizon)[
                #text(size: 8pt, weight: "medium")[E]
              ]
            ],
          ),
        )
        v(0.4em)
      }
    ],
  )
}


// ============================================================
// SEÇÃO DE DISCURSIVAS
// ============================================================
// questoes = ((id, prova, ano, aula, enunciado, linhas, figura?,
//              precisa-figura?, figura-descricao?, permite-quebra?), ...)

#let secao-discursivas(questoes) = {
  if questoes.len() == 0 { return }
  pagebreak(weak: true)
  v(0.5em)
  text(size: 16pt, weight: "bold")[QUESTÕES DISCURSIVAS]
  v(1.5em)

  for q in questoes {
    let linhas = q.at("linhas", default: 14)
    // Enunciado em bloco indivisível para não quebrar entre páginas
    block(
      breakable: false,
      below: 0.6em,
      [
        #_badge(q.id, q.prova, q.ano, q.aula)
        #v(0.4em)
        #text(size: 10.5pt, weight: "medium")[#q.enunciado]
        #_bloco-figura(
          figura: q.at("figura", default: none),
          precisa-figura: q.at("precisa-figura", default: false),
          descricao: q.at("figura-descricao", default: none),
        )
      ],
    )
    // Linhas pautadas: bloco SEPARADO, pode quebrar entre páginas
    block(
      breakable: true,
      below: 1.5em,
      [
        #v(0.4em)
        #for i in range(linhas) {
          v(0.05cm)
          line(length: 100%, stroke: 0.5pt + cor-borda-leve)
          v(0.55cm)
        }
      ],
    )
  }
}


// ============================================================
// GABARITO CONSOLIDADO
// ============================================================
// respostas = ((id: str, resposta: str), ...)

#let gabarito-consolidado(respostas) = {
  if respostas.len() == 0 { return }
  pagebreak(weak: true)

  text(size: 20pt, weight: "bold")[GABARITO]
  v(1.5em)

  set text(font: mono-fam, size: 9pt)

  // Processa na ordem original. Itens curtos viram chunks de 5; quando
  // bate um longo (CE), fecha o chunk atual, renderiza o longo em linha
  // cheia, continua. Preserva sequência exata da prova.
  let chunks-curtos = ()  // lista de chunks (cada chunk = lista de até 5 itens)
  let chunk-atual = ()
  // bloco_typo é o tipo de cada item na ordem: "C" curto ou "L" longo
  // mas mais simples: percorrer e armazenar uma lista de "segmentos" onde
  // cada segmento é ("chunk", [items]) ou ("longo", item)
  let segmentos = ()
  for r in respostas {
    if r.resposta.len() <= 3 {
      chunk-atual.push(r)
      if chunk-atual.len() == 5 {
        segmentos.push(("chunk", chunk-atual))
        chunk-atual = ()
      }
    } else {
      if chunk-atual.len() > 0 {
        segmentos.push(("chunk", chunk-atual))
        chunk-atual = ()
      }
      segmentos.push(("longo", r))
    }
  }
  if chunk-atual.len() > 0 {
    segmentos.push(("chunk", chunk-atual))
  }

  for seg in segmentos {
    let (tipo, payload) = seg
    if tipo == "chunk" {
      let cells = payload.map(r => [#r.id#h(0.5em)#r.resposta])
      while calc.rem(cells.len(), 5) != 0 {
        cells.push([])
      }
      grid(
        columns: (1fr,) * 5,
        gutter: 0.8em,
        ..cells
      )
      v(0.4em)
    } else {
      // longo (CE)
      grid(
        columns: (1.5cm, 1fr),
        gutter: 0.4em,
        [#payload.id],
        [#payload.resposta],
      )
      v(0.3em)
    }
  }
}
