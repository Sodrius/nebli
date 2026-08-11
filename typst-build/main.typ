// ================================================================
// MAIN.TYP -- imuno-02-organizacao-sistema-imune | pipeline e1-deck-v9
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Organização e funcionamento do sistema imune",
  "Imunologia",
  (
    ("Disciplina", "Imunologia — Curso de Medicina"),
    ("Onde estudar", "Abbas · Imunologia Celular e Molecular, cap. 1 e 2 · Murphy (Janeway) · Immunobiology, cap. 1 e 9"),
    ("Onde aprofundar", "Boards & Beyond (Immunology — Lymphoid Organs) · Sketchy Immuno · First Aid, Immunology — Lymphoid Structures e Leukocyte Extravasation · AnKing Step 1 v12, decks de órgãos linfoides, tráfego celular e quimiocinas"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Um sistema que precisa falar a língua do lado de fora", (
      "1.1 O problema: manter a homeostasia sem conhecer o inimigo",
      "1.2 O tradutor universal e o preço de um repertório clonal",
      "1.3 O alarme: quem grita no tecido e o que cada grito informa",
      "1.4 O que a inata faz com o alarme",
    )),
    ("PARTE II — Do lugar onde os linfócitos nascem ao lugar onde eles encontram", (
      "2.1 Órgãos linfoides primários",
      "2.2 A seleção tímica: duas provas, três destinos",
      "2.3 Órgãos linfoides secundários: o mapa dos endereços",
      "2.4 A circulação do linfócito naïve e a porta chamada HEV",
      "2.5 O que muda quando o linfócito é ativado",
    )),
    ("PARTE III — Dentro do órgão linfoide: como uma informação vira resposta", (
      "3.1 As condições estruturais: probabilidade como estratégia",
      "3.2 As três células apresentadoras",
      "3.3 A aferência: linfonodo, baço e MALT",
      "3.4 A geografia interna: áreas T, folículos B e centro germinativo",
      "3.5 A eferência e o relógio da resposta",
      "3.6 Resposta ou tolerância",
    )),
    ("PARTE IV — As moléculas que escrevem o endereço", (
      "4.1 Moléculas de adesão: uma conversa em etapas",
      "4.2 Quimiocinas: o gradiente que diz para onde ir",
      "4.3 Revendo o sistema inteiro em um só esquema",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"
