// NEBLI mindmap — amostra Typst nativo (blocos hierárquicos, sem lib externa)
// Render: typst compile --font-path ../../fonts amostra-3-typst-blocks.typ amostra-3.pdf
//
// Filosofia: em vez de grafo nó-aresta, hierarquia visual em 3 colunas
// (uma por PARTE), com bloco-centro acima conectando tudo. Sem setas —
// alinhamento vertical + cor já comunicam relação.

#set page(width: 21cm, height: auto, margin: 1cm, fill: rgb("#FAFBFC"))
#set text(font: "Merriweather", size: 9pt, fill: rgb("#1E3A5F"))

#let navy = rgb("#1E3A5F")
#let teal = rgb("#4DA6A6")
#let gold = rgb("#D4A017")
#let gray-bg = rgb("#F5F5F5")

#let centro(titulo, sub) = block(
  fill: navy, width: 100%, inset: 14pt, radius: 6pt,
  align(center, stack(spacing: 4pt,
    text(font: "Montserrat", weight: "bold", size: 13pt, fill: white, titulo),
    text(size: 9pt, fill: rgb("#CFE0F0"), sub)
  ))
)

#let parte-cabeca(numero, titulo) = block(
  fill: teal, width: 100%, inset: 8pt, radius: 4pt,
  align(center, text(font: "Montserrat", weight: "bold", size: 10pt, fill: white,
    [PARTE #numero · #titulo]))
)

#let no(titulo, corpo) = block(
  fill: gray-bg, stroke: (left: 3pt + teal), width: 100%,
  inset: (x: 9pt, y: 6pt), radius: 3pt,
  stack(spacing: 3pt,
    text(font: "Montserrat", weight: "bold", size: 9pt, fill: navy, titulo),
    text(size: 8.5pt, fill: rgb("#444444"), corpo)
  )
)

#let no-destaque(titulo, corpo) = block(
  fill: rgb("#FFF6E0"), stroke: (left: 3pt + gold), width: 100%,
  inset: (x: 9pt, y: 6pt), radius: 3pt,
  stack(spacing: 3pt,
    text(font: "Montserrat", weight: "bold", size: 9pt, fill: navy, titulo),
    text(size: 8.5pt, fill: rgb("#444444"), corpo)
  )
)

// ===== Renderização =====

#centro("Glicólise", "glicose → 2 piruvato · +2 ATP · +2 NADH")

#v(10pt)

// Linha decorativa conectando centro às 3 PARTES
#align(center, line(length: 80%, stroke: 0.5pt + teal))

#v(8pt)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 10pt,
  row-gutter: 6pt,

  // === Cabeças ===
  parte-cabeca("I", "Preparatória"),
  parte-cabeca("II", "Geração"),
  parte-cabeca("III", "Regulação"),

  // === Nó 1 (resumo da PARTE) ===
  no("Consome 2 ATP",
    "investimento inicial para sequestrar e ativar a glicose"),
  no("Rende 4 ATP + 2 NADH",
    "fosforilação ao nível do substrato; saldo líquido +2 ATP"),
  no("Destinos do piruvato",
    "aeróbio → Krebs; anaeróbio → lactato (Cori)"),

  // === Nó 2 (enzima/regulação principal) ===
  no-destaque("Hexoquinase",
    "glicose → G6P · sequestra glicose na célula"),
  no-destaque("GAPDH",
    "oxida e fosforila gliceraldeído-3-P; gera NADH"),
  no-destaque("PFK-1",
    "↑ AMP, F2,6BP · ↓ ATP, citrato (ponto-chave de regulação)"),

  // === Nó 3 ===
  no("PFK-1",
    "F6P → F1,6BP · passo irreversível-chave"),
  no("PGK",
    "1º ATP por fosforilação ao nível do substrato"),
  no("Glucagon",
    "PKA → ↓ PFK-2 → ↓ F2,6BP → inibe PFK-1"),

  // === Nó 4 ===
  no("Aldolase",
    "F1,6BP → 2 trioses interconversíveis"),
  no("Piruvato-quinase",
    "PEP → piruvato · irreversível · 2º ATP por substrato"),
  no("Balanço final",
    "2 ATP líquido · 2 NADH · 2 piruvato"),
)
