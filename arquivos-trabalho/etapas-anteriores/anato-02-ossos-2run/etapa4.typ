#import "../typst-template/nebli_v2_apostila.typ": *

// =========================================================================
// ETAPA 4 — SEMI-GLOSSÁRIO OSTEOLÓGICO (custom desta corrida, 2026-06-19)
//
// Não confundir com a antiga E4 do banco (removida em 2026-05-22).
// Esta E4 é um catálogo nominal compacto pedido pelo Davi para esta corrida:
// nomes que ficaram fora da prosa da E1 (porque a E1 foi otimizada pra
// mecanismo) ganham aqui uma linha curta com definição funcional.
// =========================================================================

#v(0.4em)
#block(width: 100%, inset: (top: 0.4em, bottom: 0.6em))[
  #text(size: 9pt, fill: text-light, style: "italic")[
    Catálogo nominal de referência. A E1 carrega o eixo mecânico e a categoria-mãe; este semi-glossário lista os nomes individuais com definição funcional curta, para uso de consulta. Cada nome aparece uma vez na E1 ou em legenda de figura; aqui você reencontra o catálogo completo.
  ]
]

// =====================================================
// 1. ACIDENTES ÓSSEOS — depressões e orifícios
// =====================================================

#text(size: 11.5pt, weight: "bold", fill: navy, font: titulo-fam)[
  1. Acidentes ósseos — depressões e orifícios
]
#v(0.3em)
#text(size: 9.5pt, fill: text-light, style: "italic")[
  Onde algo passa ou se acomoda — vasos, nervos, ligamentos, tendões, encaixes articulares.
]
#v(0.4em)

#table(
  columns: (1fr, 3fr),
  inset: (x: 6pt, y: 5pt),
  align: (left, left),
  stroke: 0.4pt + gray-border,
  fill: (col, row) => if calc.rem(row, 2) == 0 { gray-bg } else { white },

  [*Incisura*], [Entalhe (chanfradura) na margem de um osso, onde um vaso, nervo ou tendão se acomoda. Ex.: incisura escapular.],
  [*Fissura*], [Fenda estreita entre partes adjacentes de ossos para passagem de nervos e vasos sanguíneos. Ex.: fissura orbital superior.],
  [*Forame*], [Orifício discreto através do qual passam vasos sanguíneos, nervos ou ligamentos. Ex.: forame magno, forame oval.],
  [*Fossa*], [Depressão rasa na superfície do osso. Pode acomodar músculo, articulação ou víscera. Ex.: fossa olecraniana do úmero.],
  [*Meato*], [Orifício tubuliforme — canal alongado dentro do osso. Ex.: meato acústico externo, meato acústico interno.],
  [*Sulco*], [Calha ao longo da superfície óssea que acomoda um vaso sanguíneo ou tendão. Ex.: sulco bicipital do úmero.],
)

#v(0.8em)

// =====================================================
// 2. ACIDENTES ÓSSEOS — processos articulares (lisos)
// =====================================================

#text(size: 11.5pt, weight: "bold", fill: navy, font: titulo-fam)[
  2. Acidentes ósseos — processos articulares (lisos)
]
#v(0.3em)
#text(size: 9.5pt, fill: text-light, style: "italic")[
  Projeções com superfície lisa coberta por cartilagem articular — entram em articulações móveis.
]
#v(0.4em)

#table(
  columns: (1fr, 3fr),
  inset: (x: 6pt, y: 5pt),
  align: (left, left),
  stroke: 0.4pt + gray-border,
  fill: (col, row) => if calc.rem(row, 2) == 0 { gray-bg } else { white },

  [*Côndilo*], [Protuberância arredondada grande com superfície articular lisa, na extremidade do osso. Ocorre em pares. Ex.: côndilos do fêmur.],
  [*Cabeça*], [Projeção articular grande e arredondada apoiada num colo (segmento estreito). Ex.: cabeça do fêmur, cabeça do úmero.],
  [*Capítulo*], [Cabeça articular pequena e redonda. Ex.: capítulo do úmero (articula com a cabeça do rádio).],
  [*Fóvea*], [Face articular convexa ou côncava plana e lisa. Ex.: fóvea da cabeça do fêmur (depressão central onde se prende o ligamento da cabeça).],
)

#v(0.8em)

// =====================================================
// 3. ACIDENTES ÓSSEOS — processos de fixação (rugosos)
// =====================================================

#text(size: 11.5pt, weight: "bold", fill: navy, font: titulo-fam)[
  3. Acidentes ósseos — processos de fixação para tecido conjuntivo (rugosos)
]
#v(0.3em)
#text(size: 9.5pt, fill: text-light, style: "italic")[
  Projeções rugosas onde tendões e ligamentos se ancoram. Acentuam-se em resposta à tração repetida ao longo da vida.
]
#v(0.4em)

#table(
  columns: (1fr, 3fr),
  inset: (x: 6pt, y: 5pt),
  align: (left, left),
  stroke: 0.4pt + gray-border,
  fill: (col, row) => if calc.rem(row, 2) == 0 { gray-bg } else { white },

  [*Crista*], [Crista proeminente ou projeção alongada. Ex.: crista ilíaca, crista tibial.],
  [*Epicôndilo*], [Projeção normalmente rugosa acima do côndilo. Ex.: epicôndilo medial e lateral do úmero.],
  [*Espinha*], [Processo semelhante a um espinho. Ex.: espinha ilíaca ântero-superior, espinha da escápula.],
  [*Linha*], [Margem menos proeminente que a crista — uma faixa rugosa longa e estreita. Ex.: linha áspera do fêmur.],
  [*Processo espinhoso*], [Parte que se projeta semelhante a um espinho, geralmente grande. Ex.: processos espinhosos das vértebras.],
  [*Protuberância*], [Projeção arredondada do osso. Ex.: protuberância occipital externa.],
  [*Trocânter*], [Projeção muito grande. Ex.: trocânter maior e menor do fêmur (inserções de glúteos e iliopsoas).],
  [*Tróclea*], [Semelhante a uma roda ou funciona como roldana — guia para tendão deslizar. Ex.: tróclea do úmero (articula com ulna), tróclea do tálus.],
  [*Tubérculo*], [Projeção arredondada de tamanho variável. Ex.: tubérculo maior e menor do úmero.],
  [*Tuberosidade (ou túber)*], [Projeção de tamanho variável com superfície rugosa, onde se ancora tendão grande. Ex.: tuberosidade do deltóide (úmero), tuberosidade isquiática.],
)

#v(0.8em)

// =====================================================
// 4. OSSOS PNEUMÁTICOS — quem é quem
// =====================================================

#text(size: 11.5pt, weight: "bold", fill: navy, font: titulo-fam)[
  4. Ossos pneumáticos — quem é quem
]
#v(0.3em)
#text(size: 9.5pt, fill: text-light, style: "italic")[
  Ossos ocos com cavidades de ar revestidas por mucosa. Aliviam peso, ressoam a voz, condicionam o ar inspirado.
]
#v(0.4em)

#table(
  columns: (1fr, 3fr),
  inset: (x: 6pt, y: 5pt),
  align: (left, left),
  stroke: 0.4pt + gray-border,
  fill: (col, row) => if calc.rem(row, 2) == 0 { gray-bg } else { white },

  [*Frontal*], [Osso da fronte. Abriga os seios frontais, sobre os olhos. Drena no meato médio do nariz.],
  [*Maxilar*], [Osso superior do maxilar. Abriga o seio maxilar — o maior dos seios paranasais. Drena no meato médio (alto), por isso obstrui com facilidade.],
  [*Etmóide*], [Osso da base do crânio entre os olhos. Cavidades pequenas e múltiplas (células etmoidais). Forma boa parte da parede medial da órbita.],
  [*Esfenóide*], [Osso central da base do crânio. Abriga os seios esfenoidais, posteriores. Sela túrcica fica neste osso (onde repousa a hipófise).],
  [*Temporal*], [Osso lateral do crânio. Pneumático em outro registro — guarda as cavidades da orelha média e do meato acústico interno, não seio paranasal típico.],
)

#v(0.8em)

// =====================================================
// 5. ORGANIZAÇÃO DO ESQUELETO — quem mora em cada caixa
// =====================================================

#text(size: 11.5pt, weight: "bold", fill: navy, font: titulo-fam)[
  5. Organização do esqueleto — quem mora em cada caixa
]
#v(0.3em)
#text(size: 9.5pt, fill: text-light, style: "italic")[
  206 ossos no adulto. Duas grandes divisões funcionais.
]
#v(0.4em)

#table(
  columns: (1fr, 3fr),
  inset: (x: 6pt, y: 5pt),
  align: (left, left),
  stroke: 0.4pt + gray-border,
  fill: (col, row) => if calc.rem(row, 2) == 0 { gray-bg } else { white },

  [*Esqueleto axial (80)*], [Ossos da cabeça (crânio), pescoço (hióide + vértebras cervicais) e tronco (costelas, esterno, vértebras torácicas, lombares, sacrais, cóccix). Função predominante: proteção e suporte axial.],
  [*Esqueleto apendicular (126)*], [Ossos dos membros superiores e inferiores + cíngulos. Função predominante: locomoção e manipulação.],
  [*Cíngulo escapular*], [Clavícula + escápula. Conecta o membro superior ao esqueleto axial. Móvel — permite amplitude do ombro.],
  [*Cíngulo pélvico (pelve óssea)*], [Osso do quadril (ílio + ísquio + púbis fusionados) + sacro. Conecta o membro inferior ao esqueleto axial. Quase imóvel — transmite carga do tronco aos membros.],
)

#v(0.8em)

// =====================================================
// 6. TIPOS DE OSSOS POR LOCALIZAÇÃO (extras)
// =====================================================

#text(size: 11.5pt, weight: "bold", fill: navy, font: titulo-fam)[
  6. Tipos de ossos por localização — variações
]
#v(0.3em)
#text(size: 9.5pt, fill: text-light, style: "italic")[
  Categorias que não entram na morfologia clássica mas merecem nome próprio.
]
#v(0.4em)

#table(
  columns: (1fr, 3fr),
  inset: (x: 6pt, y: 5pt),
  align: (left, left),
  stroke: 0.4pt + gray-border,
  fill: (col, row) => if calc.rem(row, 2) == 0 { gray-bg } else { white },

  [*Sesamóide*], [Osso pequeno e arredondado encaixado dentro de um tendão. Aumenta o braço de alavanca do músculo. Patela é o exemplo nuclear (sesamóide do quadríceps).],
  [*Pneumático*], [Osso oco com cavidades de ar revestidas por mucosa. Frontal, maxilar, etmóide, esfenóide, temporal (este último em registro de cavidades da orelha).],
  [*Heterotópico*], [Ossificação patológica de tecidos moles (músculo, ligamento) no adulto após trauma ou inflamação. Não é a ossificação fisiológica do embrião.],
  [*Acessório (supranumerário)*], [Centro de ossificação que não fusionou ao osso principal e permaneceu separado. Variação anatômica do tarso e do carpo principalmente.],
  [*Sutural (ou wormiano)*], [Pequeno osso extra dentro das suturas do crânio — ilha óssea entre as bordas de dois ossos planos vizinhos.],
)
