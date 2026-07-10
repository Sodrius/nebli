// ===========================================================
// NEBLI — SVG HELPERS
// Criado em 2026-05-14 para resolver o erro #1 dos SVGs NEBLI:
// texto cortado / fora da caixa.
//
// CAUSA RAIZ do bug:
//   O subagente que escreve o SVG calcula a largura do <text>
//   assumindo fontes do navegador (DejaVu/Arial). No PDF compilado
//   pelo Typst, a fonte real é Merriweather/Montserrat — métricas
//   diferentes — e o label estoura o container.
//
// SOLUÇÃO:
//   Em vez de embutir <text> dentro do SVG, o REDATOR usa
//   `#figura-rotulada()` aqui definido: ele recebe a imagem-base
//   (PNG ou SVG SEM texto) + uma lista de rótulos com posição
//   relativa, e POSICIONA O TEXTO VIA TYPST (place()). O Typst
//   mede o texto com a fonte correta, então não há descalibração.
//
// USO DEFAULT a partir de 2026-05-14:
//   - Diagrama gerado em SVG SEM <text> (só formas, setas, cores)
//   - Rótulos via #figura-rotulada(...) em Typst
//   - Passo 4-bis (teste de label isolado) só necessário para SVGs
//     legacy que ainda têm <text> embutido.
// ===========================================================

#import "nebli_v2_apostila.typ": *

// ======= Rótulo individual =======
// (x, y) são frações da imagem-base (0.0 a 1.0).
// `ancor` define onde o ponto (x,y) ancora o label:
//   "tl" top-left, "tr" top-right, "bl" bottom-left, "br" bottom-right,
//   "c" center, "tc" top-center, "bc" bottom-center.
#let _label-ancor(ancor) = {
  if ancor == "tl"      { (top + left,    0pt,  0pt) }
  else if ancor == "tr" { (top + right,   0pt,  0pt) }
  else if ancor == "bl" { (bottom + left, 0pt,  0pt) }
  else if ancor == "br" { (bottom + right,0pt,  0pt) }
  else if ancor == "tc" { (top + center,  0pt,  0pt) }
  else if ancor == "bc" { (bottom + center,0pt, 0pt) }
  else                  { (center + horizon, 0pt, 0pt) }
}

// ======= Figura rotulada =======
// imagem: caminho do PNG/SVG base (sem texto)
// largura: largura total do bloco (default 80%)
// rotulos: array de dicionários com chaves:
//   - x, y: posição relativa 0–1 (canto superior-esquerdo = 0,0)
//   - texto: conteúdo do rótulo (string ou content)
//   - cor: cor do texto (default navy)
//   - ancor: "tl","tr","bl","br","c","tc","bc" (default "c")
//   - tamanho: pt (default 9)
//   - peso: "regular" ou "bold" (default "regular")
//   - fundo: cor de fundo da caixinha (default white com 92% opacidade)
//   - sem-fundo: true para texto sem caixinha (default false)
// legenda: caption abaixo, em itálico
//
// Como o Typst mede o texto com a fonte real (Merriweather),
// não há erro de width-estimation. O label sempre cabe.
#let figura-rotulada(imagem, rotulos: (), largura: 80%, legenda: none) = {
  v(10pt)
  align(center,
    block(breakable: false, width: largura,
      stack(
        // Container relativo: imagem base + place() para cada label
        box(width: 100%,
          {
            // Imagem ocupa a caixa toda
            image(imagem, width: 100%)
            // Rótulos sobre a imagem — place() com dx/dy em frações da caixa
            for r in rotulos {
              let cor       = r.at("cor",       default: navy)
              let ancor     = r.at("ancor",     default: "c")
              let tamanho   = r.at("tamanho",   default: 9pt)
              let peso      = r.at("peso",      default: "regular")
              let sem-fundo = r.at("sem-fundo", default: false)
              let fundo     = r.at("fundo",     default: rgb(255, 255, 255, 235))
              let texto-conteudo = if peso == "bold" {
                text(font: titulo-fam, size: tamanho, weight: "bold",
                  fill: cor, r.texto)
              } else {
                text(font: corpo-fam, size: tamanho, fill: cor, r.texto)
              }
              let etiqueta = if sem-fundo {
                texto-conteudo
              } else {
                box(fill: fundo, inset: (x: 3pt, y: 1.5pt),
                  radius: 2pt, stroke: 0.3pt + gray-border,
                  texto-conteudo)
              }
              place(
                top + left,
                dx: r.x * 100%,
                dy: r.y * 100%,
                etiqueta
              )
            }
          }
        ),
        if legenda != none {
          [
            #v(7pt)
            #align(left,
              text(size: 9.5pt, style: "italic", fill: text-light, legenda)
            )
          ]
        }
      )
    )
  )
  v(10pt)
}

// ======= Cronologia temporal =======
// Caixa numerada com escala de tempo real (P3 da spec).
// passos: array de (tempo, descricao)
//   tempo: ex "200 μs", "1 ms"
//   descricao: o que acontece
#let cronologia(titulo: none, passos) = {
  block(
    fill: rgb("#F4F7F2"),
    stroke: (left: 4pt + teal),
    inset: (x: 15pt, y: 12pt),
    width: 100%,
    radius: 5pt,
    breakable: false,
    below: 14pt,
    {
      if titulo != none {
        text(font: titulo-fam, weight: "bold", size: 10pt, fill: teal,
          tracking: 0.3pt, titulo)
        v(7pt)
      }
      let i = 1
      for (tempo, descricao) in passos {
        block(below: 6pt,
          grid(
            columns: (auto, 1.6cm, 1fr),
            column-gutter: 8pt,
            // Número
            box(fill: teal, inset: (x: 6pt, y: 1pt), radius: 8pt,
              text(font: titulo-fam, size: 8pt, weight: "bold",
                fill: white, str(i))),
            // Tempo
            text(font: titulo-fam, weight: "bold", size: 9.5pt,
              fill: navy, tempo),
            // Descrição
            text(size: 10pt, descricao)
          )
        )
        i = i + 1
      }
    }
  )
}

// ======= Tabela comparativa NEBLI =======
// Para os 3 casos canônicos do CLAUDE.md (§Bullets e tabelas):
//   (a) comparativos com 3+ dimensões
//   (c) critérios diagnósticos
// cabecalho: array de strings (1ª linha)
// linhas: array de arrays
#let tabela-comparativa(cabecalho, linhas, larguras: none) = {
  v(8pt)
  let cols = if larguras != none { larguras } else { (1fr,) * cabecalho.len() }
  block(breakable: false,
    table(
      columns: cols,
      stroke: 0.5pt + gray-border,
      align: (col, row) => if row == 0 { center + horizon } else { left + horizon },
      // Cabeçalho
      ..cabecalho.map(c => table.cell(
        fill: navy,
        text(font: titulo-fam, weight: "bold", size: 9.5pt,
          fill: white, tracking: 0.3pt, c)
      )),
      // Linhas
      ..linhas.flatten().map(c => [#text(size: 10pt, c)])
    )
  )
  v(8pt)
}
