// NEBLI mindmap — amostra-3 v2 (Typst nativo + badges didáticos)
// Render: typst compile --font-path ../../fonts amostra-3-v2-typst-blocks.typ amostra-3-v2.pdf
//
// Mudanças v2 vs v1:
// 1. Badge circular com nº da reação (R1, R3, R6, R7, R10) em cada enzima.
// 2. Cor do badge codifica fase:
//    - âmbar (gold) = INVESTIMENTO (R1–R5, gasta ATP)
//    - teal         = PAGAMENTO  (R6–R10, gera ATP/NADH)
// 3. Linha "substrato → produto" abaixo do nome da enzima.
// 4. Mini-legenda no rodapé explica o código de cor + a virada R5→R6.

#set page(width: 21cm, height: auto, margin: 1cm, fill: rgb("#FAFBFC"))
#set text(font: "Merriweather", size: 9pt, fill: rgb("#1E3A5F"))

#let navy = rgb("#1E3A5F")
#let teal = rgb("#4DA6A6")
#let gold = rgb("#D4A017")
#let gray-bg = rgb("#F5F5F5")
#let teal-soft = rgb("#E6F2F0")
#let gold-soft = rgb("#FFF6E0")

#let centro(titulo, sub) = block(
  fill: navy, width: 100%, inset: 14pt, radius: 6pt,
  align(center, stack(spacing: 4pt,
    text(font: "Montserrat", weight: "bold", size: 13pt, fill: white, titulo),
    text(size: 9pt, fill: rgb("#CFE0F0"), sub)
  ))
)

#let parte-cabeca(numero, titulo, faixa-r) = block(
  fill: teal, width: 100%, inset: 8pt, radius: 4pt,
  align(center, stack(spacing: 2pt,
    text(font: "Montserrat", weight: "bold", size: 10pt, fill: white,
      [PARTE #numero · #titulo]),
    text(font: "Montserrat", size: 7.5pt, fill: rgb("#CFE0F0"), tracking: 0.8pt,
      upper(faixa-r))
  ))
)

// Badge circular com nº da reação. fase: "inv" (âmbar) ou "pag" (teal).
#let badge(rotulo, fase) = {
  let cor = if fase == "inv" { gold } else { teal }
  box(
    fill: cor, radius: 100%,
    inset: (x: 6pt, y: 3pt),
    text(font: "Montserrat", weight: "bold", size: 7.5pt, fill: white, tracking: 0.3pt,
      rotulo)
  )
}

// Bloco de enzima: badge + nome + reação substrato→produto + nota
#let enzima(badge-rot, fase, nome, reacao, nota) = block(
  fill: if fase == "inv" { gold-soft } else { teal-soft },
  stroke: (left: 3pt + (if fase == "inv" { gold } else { teal })),
  width: 100%,
  inset: (x: 9pt, y: 6pt), radius: 3pt,
  stack(spacing: 3pt,
    stack(dir: ltr, spacing: 6pt,
      badge(badge-rot, fase),
      text(font: "Montserrat", weight: "bold", size: 9pt, fill: navy, nome)
    ),
    text(size: 8.5pt, fill: rgb("#222222"), reacao),
    text(size: 8pt, fill: rgb("#666666"), style: "italic", nota)
  )
)

// Bloco neutro (sem badge — para destinos, balanço, regulação geral)
#let no(titulo, corpo) = block(
  fill: gray-bg, stroke: (left: 3pt + navy), width: 100%,
  inset: (x: 9pt, y: 6pt), radius: 3pt,
  stack(spacing: 3pt,
    text(font: "Montserrat", weight: "bold", size: 9pt, fill: navy, titulo),
    text(size: 8.5pt, fill: rgb("#444444"), corpo)
  )
)

// ===== Renderização =====

#centro("Glicólise", "glicose → 2 piruvato · +2 ATP · +2 NADH · 10 reações")

#v(10pt)
#align(center, line(length: 80%, stroke: 0.5pt + teal))
#v(8pt)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 10pt,
  row-gutter: 6pt,

  // === Cabeças com faixa de reações ===
  parte-cabeca("I", "Preparatória", "R1–R5 · gasta 2 ATP"),
  parte-cabeca("II", "Geração",     "R6–R10 · rende 4 ATP + 2 NADH"),
  parte-cabeca("III", "Regulação",  "controle + destinos"),

  // === Linha 1: enzima principal de cada PARTE ===
  enzima("R1", "inv", "Hexoquinase",
    [glicose → glicose-6-P],
    [gasta 1 ATP · sequestra glicose na célula]),
  enzima("R6", "pag", "GAPDH",
    [G3P → 1,3-BPG],
    [oxida e fosforila · gera 1 NADH]),
  no("Regulação da PFK-1",
    [↑ AMP, F2,6-BP · ↓ ATP, citrato · ponto-chave da via]),

  // === Linha 2 ===
  enzima("R3", "inv", "PFK-1",
    [F6P → frutose-1,6-BP],
    [gasta 1 ATP · irreversível · regulatório-chave]),
  enzima("R7", "pag", "PGK",
    [1,3-BPG → 3-PG],
    [1º ATP por substrato]),
  no("Sinalização hormonal",
    [glucagon → PKA → ↓ PFK-2 → ↓ F2,6-BP → freia glicólise]),

  // === Linha 3 ===
  enzima("R4", "inv", "Aldolase",
    [F1,6-BP → 2 trioses],
    [clivagem em DHAP + G3P · interconversíveis via R5]),
  enzima("R10", "pag", "Piruvato-quinase",
    [PEP → piruvato],
    [2º ATP por substrato · irreversível]),
  no("Destinos do piruvato",
    [aeróbio → acetil-CoA → Krebs · anaeróbio → lactato (Cori)]),

  // === Linha 4 (balanço) ===
  no("Virada R5 → R6",
    [fim do investimento, começo do pagamento · célula passa a render]),
  no("Balanço por glicose",
    [+4 ATP (R7+R10, ×2) − 2 ATP (R1+R3) = +2 ATP líquido · +2 NADH · 2 piruvato]),
  no("Fermentação",
    [piruvato → lactato regenera NAD⁺ · permite glicólise sem O₂]),
)

#v(12pt)

// ===== Legenda =====
#block(fill: gray-bg, inset: 8pt, radius: 4pt, width: 100%,
  stack(dir: ltr, spacing: 14pt,
    stack(dir: ltr, spacing: 5pt,
      badge("R1", "inv"),
      text(size: 8.5pt, [Investimento (R1–R5) · gasta ATP])
    ),
    stack(dir: ltr, spacing: 5pt,
      badge("R6", "pag"),
      text(size: 8.5pt, [Pagamento (R6–R10) · gera ATP + NADH])
    ),
    text(size: 8pt, style: "italic", fill: rgb("#666666"),
      [R2, R5, R8, R9 omitidas no mapa — isomerases e mutases sem ATP/NADH envolvido])
  )
)
