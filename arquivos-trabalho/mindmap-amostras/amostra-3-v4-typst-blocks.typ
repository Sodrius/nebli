// NEBLI mindmap — amostra-3 v4 (intenção editorial, não enciclopédia)
// Render: typst compile --font-path ../../fonts amostra-3-v4-typst-blocks.typ amostra-3-v4.pdf
//
// Mudanças v4 vs v3:
// - Saiu do layout tabular 3×4. Agora tem 3 zonas verticais:
//     (1) ZONA-MENSAGEM no topo — a única frase que o aluno LEVA EMBORA
//     (2) ZONA-NARRATIVA no meio — 3 estações em fila, contando a história
//     (3) ZONA-DETALHE no rodapé — 3 cartões de regulação/destinos/clínica
// - Caiu de 12 nós para 9.
// - Tipografia varia: mensagem 14pt italic, estação 11pt bold, detalhe 9pt regular.
// - Setas/conectores entre as estações (a narrativa flui, não fica estática).
// - Cor com mais contraste mas menos saturação — só 2 cores quentes (gold = gasto),
//   2 cores frias (teal = ganho). Cinza é o "neutro" de fundo.
//
// Princípio editorial: cada bloco responde "se o aluno esquecer isso, ele
// entendeu o tema?". Se sim → fora do mapa. Curadoria, não inventário.

#set page(width: 21cm, height: auto, margin: 1.2cm, fill: rgb("#FAFBFC"))
#set text(font: "Merriweather", size: 9pt, fill: rgb("#1E3A5F"))

#let navy = rgb("#1E3A5F")
#let teal = rgb("#4DA6A6")
#let gold = rgb("#D4A017")
#let gray-bg = rgb("#F5F5F5")
#let teal-soft = rgb("#E6F2F0")
#let gold-soft = rgb("#FFF6E0")
#let line-muted = rgb("#CFD8DC")

// ===== ZONA 1 — A MENSAGEM (o que o aluno LEVA EMBORA) =====
// Bloco grande, tipografia editorial, sem decoração demais.
// O subtítulo é a única frase que o aluno deveria conseguir falar
// fechando o livro: "a célula gasta 2 ATP no começo pra ganhar 4 no fim".

#block(width: 100%, inset: (x: 0pt, y: 12pt),
  stack(spacing: 6pt,
    align(center,
      text(font: "Montserrat", weight: "bold", size: 20pt, fill: navy, tracking: 0.4pt,
        "GLICÓLISE")
    ),
    align(center,
      text(font: "Merriweather", size: 12pt, style: "italic", fill: rgb("#444444"),
        "a célula investe 2 ATP no começo para ganhar 4 no fim — saldo +2 ATP, +2 NADH, 2 piruvato")
    ),
  )
)

#align(center, line(length: 12%, stroke: 1.5pt + gold))

#v(18pt)

// ===== ZONA 2 — A NARRATIVA (3 estações em fila) =====
// Não são "3 PARTES iguais". São 3 momentos com peso narrativo distinto:
//   INVESTIMENTO → VIRADA → PAGAMENTO
// A virada (R5→R6) ganha destaque visual porque é o ponto-conceito.

#let estacao(rotulo, titulo, frase, cor-base, cor-fundo, centro: false) = block(
  fill: cor-fundo,
  stroke: (left: 4pt + cor-base),
  width: 100%,
  inset: (x: 14pt, y: 12pt),
  radius: 4pt,
  stack(spacing: 6pt,
    text(font: "Montserrat", weight: "bold", size: 8pt, fill: cor-base, tracking: 1.2pt,
      upper(rotulo)),
    text(font: "Montserrat", weight: "bold", size: if centro { 13pt } else { 12pt }, fill: navy,
      titulo),
    text(size: 9pt, style: "italic", fill: rgb("#333333"), frase)
  )
)

#grid(
  columns: (1fr, auto, 1fr, auto, 1fr),
  column-gutter: 8pt,
  align: horizon,

  estacao(
    "Fase preparatória · R1–R5",
    "Hexoquinase e PFK-1",
    [a célula paga 2 ATP pra prender a glicose dentro e cortar a molécula em duas — PFK-1 fecha a porta, daqui não volta],
    gold, gold-soft
  ),

  // Seta →
  text(size: 18pt, fill: line-muted, "→"),

  estacao(
    "Virada · R5 → R6",
    "Para de gastar, começa a ganhar",
    [todo passo daqui pra frente conta dobrado — a glicose virou duas trioses, e cada uma vai render ATP separadamente],
    navy, gray-bg, centro: true
  ),

  // Seta →
  text(size: 18pt, fill: line-muted, "→"),

  estacao(
    "Fase de geração · R6–R10",
    "GAPDH e Piruvato-quinase",
    [GAPDH solta o NADH, PGK e piruvato-quinase devolvem 4 ATP — saldo só não é +6 porque os 2 do começo já foram gastos],
    teal, teal-soft
  ),
)

#v(20pt)

// ===== ZONA 3 — DETALHE (regulação / destinos / clínica) =====
// Cartões menores, paridade horizontal, tipografia mais discreta.
// Não competem com a narrativa central — são "pra quem quiser saber mais".

#align(center,
  text(font: "Montserrat", weight: "bold", size: 8pt, fill: rgb("#888888"), tracking: 1.5pt,
    upper("Quando ligar · pra onde vai · por que importa"))
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
    "Quem manda na velocidade",
    [PFK-1 é o termostato — sobe com AMP e F2,6-BP, desce com ATP e citrato; glucagon freia via PKA]
  ),
  cartao(
    "Pra onde vai o piruvato",
    [com O₂ → acetil-CoA → Krebs; sem O₂ → lactato pra regenerar NAD⁺ e a glicólise não travar]
  ),
  cartao(
    "Por que isso importa",
    [única via que rende ATP sem oxigênio — hemácia, músculo em esforço e tumor dependem dela]
  ),
)
