// NEBLI mindmap — Citoesqueleto (teste de escala do formato)
// Render: typst compile --font-path ../../fonts amostra-citoesqueleto.typ amostra-citoesqueleto.pdf
//
// Por que esse tema testa o formato:
// - NÃO tem enzimas numeradas → badge precisa virar "categoria estrutural"
// - NÃO tem fases gasto/ganho → cor precisa codificar outra dimensão
// - 3 PARTES são CATEGORIAS PARALELAS (não etapas de processo)
//
// Adaptação: cor codifica tipo de filamento (3 categorias).
// Badge vira sigla curta do filamento (MF, MT, FI).
// Pegada dialogal mantida — monitor explicando "o que faz, por que importa".

#set page(width: 21cm, height: auto, margin: 1cm, fill: rgb("#FAFBFC"))
#set text(font: "Merriweather", size: 9pt, fill: rgb("#1E3A5F"))

#let navy = rgb("#1E3A5F")
#let teal = rgb("#4DA6A6")
#let gold = rgb("#D4A017")
#let red-alert = rgb("#C0392B")
#let blue-clin = rgb("#2E86AB")
#let gray-bg = rgb("#F5F5F5")

#let teal-soft = rgb("#E6F2F0")
#let gold-soft = rgb("#FFF6E0")
#let blue-soft = rgb("#E6EEF5")

#let centro(titulo, sub) = block(
  fill: navy, width: 100%, inset: 14pt, radius: 6pt,
  align(center, stack(spacing: 5pt,
    text(font: "Montserrat", weight: "bold", size: 13pt, fill: white, titulo),
    text(size: 9pt, fill: rgb("#CFE0F0"), style: "italic", sub)
  ))
)

#let parte-cabeca(numero, titulo, cor-base, faixa) = block(
  fill: cor-base, width: 100%, inset: 8pt, radius: 4pt,
  align(center, stack(spacing: 3pt,
    text(font: "Montserrat", weight: "bold", size: 10pt, fill: white,
      [PARTE #numero · #titulo]),
    text(size: 8pt, fill: rgb("#FFFFFF").lighten(15%), style: "italic", faixa)
  ))
)

#let badge(rotulo, cor) = box(
  fill: cor, radius: 100%,
  inset: (x: 6pt, y: 3pt),
  text(font: "Montserrat", weight: "bold", size: 7.5pt, fill: white, tracking: 0.3pt, rotulo)
)

// Bloco-componente: badge + nome + linha técnica + fala dialogal
#let comp(badge-rot, cor, fundo, nome, tecnica, fala) = block(
  fill: fundo,
  stroke: (left: 3pt + cor),
  width: 100%,
  inset: (x: 9pt, y: 7pt), radius: 3pt,
  stack(spacing: 4pt,
    stack(dir: ltr, spacing: 6pt,
      badge(badge-rot, cor),
      text(font: "Montserrat", weight: "bold", size: 9pt, fill: navy, nome)
    ),
    text(font: "Montserrat", size: 8pt, fill: rgb("#555555"), tracking: 0.2pt, tecnica),
    text(size: 8.5pt, fill: rgb("#222222"), style: "italic", fala)
  )
)

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
  "Citoesqueleto",
  "três sistemas de fibras dão à célula forma, força e movimento — cada um especializado"
)

#v(10pt)
#align(center, line(length: 80%, stroke: 0.5pt + teal))
#v(8pt)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 10pt,
  row-gutter: 6pt,

  // === Cabeças por categoria ===
  parte-cabeca("I", "Microfilamentos", teal,
    "actina · finos · movimento de superfície"),
  parte-cabeca("II", "Microtúbulos", gold,
    "tubulina · trilhos do transporte interno"),
  parte-cabeca("III", "Filamentos Intermediários", blue-clin,
    "proteínas variadas · resistência mecânica"),

  // === Linha 1 — proteína-base ===
  comp("MF", teal, teal-soft, "Actina G → Actina F",
    [monômero → polímero helicoidal · 7 nm],
    [monômeros se encaixam em fila — célula monta e desmonta esses fios em segundos quando precisa]),
  comp("MT", gold, gold-soft, "α/β-tubulina → microtúbulo",
    [dímero → tubo oco · 25 nm · 13 protofilamentos],
    [tubo oco rígido — funciona como trilho de trem dentro da célula, com direção definida]),
  comp("FI", blue-clin, blue-soft, "Subunidade fibrosa → corda",
    [monômero alongado → cabo trançado · 10 nm],
    [trançam como corda de barco — não se desfazem fácil, aguentam tração sem quebrar]),

  // === Linha 2 — motor associado ===
  comp("MF", teal, teal-soft, "Miosina",
    [motor que caminha sobre actina],
    [puxa actina pra fazer músculo contrair, célula se mover, citocinese fechar no fim da mitose]),
  comp("MT", gold, gold-soft, "Cinesina + Dineína",
    [motores opostos: anterógrado vs retrógrado],
    [cinesina leva carga pra periferia, dineína traz de volta — vesículas pegam carona nesses trilhos]),
  comp("FI", blue-clin, blue-soft, "Sem motor associado",
    [estruturais, não dinâmicos],
    [diferente dos outros dois: não tem motor porque a função é só segurar, não mover]),

  // === Linha 3 — papel celular ===
  comp("MF", teal, teal-soft, "Córtex celular",
    [malha sob a membrana plasmática],
    [forma microvilosidades, lamelipódios e filopódios — tudo que faz a borda da célula se mexer]),
  comp("MT", gold, gold-soft, "MTOC + fuso mitótico",
    [centro organizador · âncora dos MTs],
    [centrosomo nucleia os microtúbulos · no fim da mitose vira o fuso que separa os cromossomos]),
  comp("FI", blue-clin, blue-soft, "Tipos teciduais",
    [queratina (epitélio) · vimentina (mesênquima) · laminas (núcleo)],
    [cada tecido tem o seu — patologista usa essas proteínas pra dizer de onde veio um tumor]),

  // === Linha 4 — clínica/integração ===
  no-fala("Drogas que travam o citoesqueleto",
    [colchicina e taxol agem nos MT — quimioterapia explora a divisão celular dependente do fuso mitótico]),
  no-fala("Quem dá forma, quem move",
    [MF e MT são dinâmicos (montam e desmontam) · FI são estáticos (uma vez prontos, ficam)]),
  no-fala("Integração",
    [os 3 sistemas conversam — junções aderentes ligam MF entre células, desmossomos ligam FI, hemidesmossomos ligam FI à matriz]),
)

#v(12pt)

// ===== Legenda =====
#block(fill: gray-bg, inset: 8pt, radius: 4pt, width: 100%,
  stack(dir: ltr, spacing: 14pt,
    stack(dir: ltr, spacing: 5pt, badge("MF", teal),
      text(size: 8.5pt, [Microfilamentos · actina · 7 nm])),
    stack(dir: ltr, spacing: 5pt, badge("MT", gold),
      text(size: 8.5pt, [Microtúbulos · tubulina · 25 nm])),
    stack(dir: ltr, spacing: 5pt, badge("FI", blue-clin),
      text(size: 8.5pt, [Filamentos intermediários · 10 nm])),
  )
)
