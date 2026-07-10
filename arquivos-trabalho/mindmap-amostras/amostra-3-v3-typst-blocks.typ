// NEBLI mindmap — amostra-3 v3 (Typst nativo + badges + voz dialogal)
// Render: typst compile --font-path ../../fonts amostra-3-v3-typst-blocks.typ amostra-3-v3.pdf
//
// Mudanças v3 vs v2:
// - Linha de nota de cada enzima reescrita em voz dialogal (monitor explicando).
// - Faixa de cabeça da PARTE com tom didático, não label seco.
// - Nós sem badge (Virada, Balanço, Destinos) ganham frases inteiras.
// - Calibração: ~12–18 palavras na nota dialogal (cabe num post-it).
//
// Duplo registro tipográfico:
// - Linha técnica (substrato → produto): etiqueta seca pra olhar de relance.
// - Linha italicizada: monitor cochichando o porquê.

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
  align(center, stack(spacing: 5pt,
    text(font: "Montserrat", weight: "bold", size: 13pt, fill: white, titulo),
    text(size: 9pt, fill: rgb("#CFE0F0"), style: "italic", sub)
  ))
)

#let parte-cabeca(numero, titulo, faixa) = block(
  fill: teal, width: 100%, inset: 8pt, radius: 4pt,
  align(center, stack(spacing: 3pt,
    text(font: "Montserrat", weight: "bold", size: 10pt, fill: white,
      [PARTE #numero · #titulo]),
    text(size: 8pt, fill: rgb("#E6F2F0"), style: "italic", faixa)
  ))
)

#let badge(rotulo, fase) = {
  let cor = if fase == "inv" { gold } else { teal }
  box(
    fill: cor, radius: 100%,
    inset: (x: 6pt, y: 3pt),
    text(font: "Montserrat", weight: "bold", size: 7.5pt, fill: white, tracking: 0.3pt,
      rotulo)
  )
}

// Bloco de enzima com voz dialogal na nota
#let enzima(badge-rot, fase, nome, reacao, fala) = block(
  fill: if fase == "inv" { gold-soft } else { teal-soft },
  stroke: (left: 3pt + (if fase == "inv" { gold } else { teal })),
  width: 100%,
  inset: (x: 9pt, y: 7pt), radius: 3pt,
  stack(spacing: 4pt,
    stack(dir: ltr, spacing: 6pt,
      badge(badge-rot, fase),
      text(font: "Montserrat", weight: "bold", size: 9pt, fill: navy, nome)
    ),
    text(font: "Montserrat", size: 8pt, fill: rgb("#555555"), tracking: 0.2pt, reacao),
    text(size: 8.5pt, fill: rgb("#222222"), style: "italic", fala)
  )
)

// Nó dialogal puro (sem badge, sem linha técnica — só monitor falando)
#let no-fala(titulo, fala) = block(
  fill: gray-bg, stroke: (left: 3pt + navy), width: 100%,
  inset: (x: 9pt, y: 7pt), radius: 3pt,
  stack(spacing: 4pt,
    text(font: "Montserrat", weight: "bold", size: 9pt, fill: navy, titulo),
    text(size: 8.5pt, fill: rgb("#222222"), style: "italic", fala)
  )
)

// ===== Renderização =====

#centro(
  "Glicólise",
  "a célula quebra a glicose em dois pedaços, paga 2 ATP no começo e ganha 4 no final — saldo: +2 ATP e 2 NADH"
)

#v(10pt)
#align(center, line(length: 80%, stroke: 0.5pt + teal))
#v(8pt)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 10pt,
  row-gutter: 6pt,

  // === Cabeças com voz dialogal na faixa ===
  parte-cabeca("I", "Preparatória",
    "primeiro a célula investe — gasta 2 ATP pra preparar a glicose"),
  parte-cabeca("II", "Geração",
    "agora ela colhe — 4 ATP saem, mais 2 NADH de bônus"),
  parte-cabeca("III", "Regulação",
    "quando ligar, quando desligar, pra onde o piruvato vai"),

  // === Linha 1 ===
  enzima("R1", "inv", "Hexoquinase",
    [glicose → glicose-6-P],
    [paga 1 ATP pra grudar um fosfato — glicose agora não sai mais da célula, ficou marcada]),
  enzima("R6", "pag", "GAPDH",
    [G3P → 1,3-BPG],
    [aqui sai o NADH: arranca 2 elétrons do açúcar e empacota num carregador pra cadeia respiratória]),
  no-fala("Regulação da PFK-1",
    [é o termostato da via: ↑ AMP e F2,6-BP aceleram, ↑ ATP e citrato freiam — célula cheia desliga sozinha]),

  // === Linha 2 ===
  enzima("R3", "inv", "PFK-1",
    [F6P → frutose-1,6-BP],
    [paga o 2º ATP e fecha a porta — passo irreversível, daqui não tem como voltar atrás]),
  enzima("R7", "pag", "PGK",
    [1,3-BPG → 3-PG],
    [primeiro ATP que retorna pra célula — direto do substrato, sem precisar da cadeia respiratória]),
  no-fala("Sinalização hormonal",
    [glucagon avisa "tá faltando glicose no sangue" → cascata PKA → derruba F2,6-BP → PFK-1 desacelera]),

  // === Linha 3 ===
  enzima("R4", "inv", "Aldolase",
    [F1,6-BP → 2 trioses],
    [parte a molécula no meio — uma glicose vira duas peças pequenas, daqui pra frente tudo conta dobrado]),
  enzima("R10", "pag", "Piruvato-quinase",
    [PEP → piruvato],
    [último ATP que sai · irreversível · entrega o piruvato pronto pro destino que a célula escolher]),
  no-fala("Destinos do piruvato",
    [com O₂ vai pro Krebs virar acetil-CoA · sem O₂ vira lactato pra regenerar NAD⁺ e a glicólise não travar]),

  // === Linha 4 ===
  no-fala("Virada R5 → R6",
    [aqui a célula para de gastar e começa a ganhar — fim da fase de investimento, início do retorno]),
  no-fala("Balanço por glicose",
    [+4 ATP (R7+R10, ×2 porque vira duas trioses) − 2 ATP (R1+R3) = +2 ATP líquido · +2 NADH · 2 piruvato]),
  no-fala("Fermentação",
    [sem oxigênio o NADH não tem onde descarregar — lactato regenera NAD⁺ e a glicólise continua girando]),
)

#v(12pt)

// ===== Legenda =====
#block(fill: gray-bg, inset: 8pt, radius: 4pt, width: 100%,
  stack(dir: ltr, spacing: 14pt,
    stack(dir: ltr, spacing: 5pt,
      badge("R1", "inv"),
      text(size: 8.5pt, [Investimento (R1–R5) · célula gasta ATP])
    ),
    stack(dir: ltr, spacing: 5pt,
      badge("R6", "pag"),
      text(size: 8.5pt, [Pagamento (R6–R10) · célula colhe ATP + NADH])
    ),
    text(size: 8pt, style: "italic", fill: rgb("#666666"),
      [R2, R5, R8, R9 são isomerases/mutases sem ATP/NADH — fora do mapa pra não saturar])
  )
)
