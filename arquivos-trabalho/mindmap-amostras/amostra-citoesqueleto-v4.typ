// NEBLI mindmap — Citoesqueleto v4 (mesmo molde do v4 Glicólise)
// Render: typst compile --font-path ../../fonts amostra-citoesqueleto-v4.typ amostra-citoesqueleto-v4.pdf
//
// Teste de escala: o molde v4 (3 zonas) funciona em tema sem ordem temporal?
// Citoesqueleto não tem progressão (MF→MT→FI não é uma sequência), são
// categorias paralelas. Diferenças deliberadas vs Glicólise v4:
//   - Sem setas → entre estações (não há "vira aquilo")
//   - Cada estação tem cor própria (3 categorias, não 2 fases + 1 virada)
//   - Mensagem central enfatiza paralelismo, não progressão

#set page(width: 21cm, height: auto, margin: 1.2cm, fill: rgb("#FAFBFC"))
#set text(font: "Merriweather", size: 9pt, fill: rgb("#1E3A5F"))

#let navy = rgb("#1E3A5F")
#let teal = rgb("#4DA6A6")
#let gold = rgb("#D4A017")
#let blue-clin = rgb("#2E86AB")
#let gray-bg = rgb("#F5F5F5")
#let teal-soft = rgb("#E6F2F0")
#let gold-soft = rgb("#FFF6E0")
#let blue-soft = rgb("#E6EEF5")
#let line-muted = rgb("#CFD8DC")

// ===== ZONA 1 — MENSAGEM =====

#block(width: 100%, inset: (x: 0pt, y: 12pt),
  stack(spacing: 6pt,
    align(center,
      text(font: "Montserrat", weight: "bold", size: 20pt, fill: navy, tracking: 0.4pt,
        "CITOESQUELETO")
    ),
    align(center,
      text(font: "Merriweather", size: 12pt, style: "italic", fill: rgb("#444444"),
        "actina mexe a borda, microtúbulos transportam por dentro, filamentos intermediários aguentam o tranco")
    ),
  )
)

#align(center, line(length: 12%, stroke: 1.5pt + gold))

#v(18pt)

// ===== ZONA 2 — NARRATIVA (3 categorias paralelas, sem setas) =====

#let estacao(rotulo, titulo, frase, cor-base, cor-fundo) = block(
  fill: cor-fundo,
  stroke: (left: 4pt + cor-base),
  width: 100%,
  inset: (x: 14pt, y: 12pt),
  radius: 4pt,
  stack(spacing: 6pt,
    text(font: "Montserrat", weight: "bold", size: 8pt, fill: cor-base, tracking: 1.2pt,
      upper(rotulo)),
    text(font: "Montserrat", weight: "bold", size: 12pt, fill: navy,
      titulo),
    text(size: 9pt, style: "italic", fill: rgb("#333333"), frase)
  )
)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 12pt,

  estacao(
    "Microfilamentos · 7 nm · dinâmicos",
    "Actina e miosina",
    [actina-G se encaixa em fila virando actina-F — miosina puxa esses fios pra contrair músculo, mover a célula e fechar a citocinese],
    teal, teal-soft
  ),

  estacao(
    "Microtúbulos · 25 nm · dinâmicos",
    "Tubulina, cinesina e dineína",
    [tubo oco rígido funciona como trilho — cinesina leva carga pra periferia, dineína traz de volta, e no fim da mitose tudo vira fuso],
    gold, gold-soft
  ),

  estacao(
    "Filamentos intermediários · 10 nm · estáticos",
    "Trançam como corda de barco",
    [não têm motor e não se desfazem — queratina no epitélio, vimentina no mesênquima, laminas no núcleo: cada tecido tem o seu],
    blue-clin, blue-soft
  ),
)

#v(20pt)

// ===== ZONA 3 — DETALHE =====

#align(center,
  text(font: "Montserrat", weight: "bold", size: 8pt, fill: rgb("#888888"), tracking: 1.5pt,
    upper("Por que importa · drogas · integração entre os 3"))
)

#v(8pt)

#let cartao(titulo, frase) = block(
  fill: white,
  stroke: 0.5pt + line-muted,
  width: 100%,
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  stack(spacing: 4pt,
    text(font: "Montserrat", weight: "bold", size: 8.5pt, fill: navy, titulo),
    text(size: 8.5pt, fill: rgb("#444444"), style: "italic", frase)
  )
)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 10pt,

  cartao(
    "Quimioterapia",
    [colchicina e taxol travam microtúbulos — célula em divisão não monta o fuso e morre antes de terminar a mitose]
  ),
  cartao(
    "Identidade tecidual",
    [patologista usa qual FI o tumor expressa pra dizer de onde veio: queratina = epitelial, vimentina = mesenquimal]
  ),
  cartao(
    "Os 3 conversam",
    [junções aderentes ligam MF entre células, desmossomos ligam FI célula-célula, hemidesmossomos ligam FI à matriz]
  ),
)
