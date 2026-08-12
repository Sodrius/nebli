// ================================================================
// MAIN.TYP -- imuno-01-reconhecimento-inato | pipeline e1-deck-v9
// E2/E3 desligados no canônico v9: apenas Etapa 1 + Resumindo.
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Reconhecimento inato no sistema imune",
  "Imunologia",
  (
    ("Disciplina", "Imunologia — Prof. José Alexandre M. Barbuto"),
    ("Onde estudar", "Abbas · Imunologia Celular e Molecular, cap. 4 (Imunidade inata) · Murphy · Janeway's Immunobiology, cap. 3"),
    ("Onde aprofundar", [
      • Takeuchi O, Akira S. Pattern recognition receptors and inflammation. #emph[Cell] 2010;140:805–820 \
      • Schroder K, Tschopp J. The inflammasomes. #emph[Cell] 2010;140(6):821–32 \
      • Gay NJ, Symmons MF, Gangloff M, Bryant CE. Assembly and localization of Toll-like receptor signalling complexes. #emph[Oncogene] 2014;14(8):546–58
    ]),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Duas maneiras de reconhecer", (
      "1.1 Repertório clonal: aleatório e selecionado",
      "1.2 Resposta ou tolerância: decide o tecido",
      "1.3 Hierarquia: homeostasia antes do antígeno",
      "1.4 A ponte: apresentação de antígenos",
      "1.5 PAMP, DAMP e a ideia de perigo",
    )),
    ("PARTE II — Famílias de PRR e geografia celular", (
      "2.1 Seis famílias e quatro endereços",
      "2.2 Por que o endereço prediz o ligante",
      "2.3 Os TLR, um a um",
      "2.4 Além dos TLR: RLR, NLR e CLR",
      "2.5 De onde vem o nome Toll",
    )),
    ("PARTE III — Da sinalização à plataforma", (
      "3.1 Como um TLR liga",
      "3.2 MyD88 e TRIF: dois destinos",
      "3.3 A anatomia do citoplasma",
      "3.4 O inflamassoma: uma plataforma que corta",
      "3.5 NLRP3: por que dois sinais",
    )),
    ("PARTE IV — Estratégias e linguagem das citocinas", (
      "4.1 O que a resposta inata tenta fazer",
      "4.2 Interferons do tipo I",
      "4.3 Citotoxicidade celular",
      "4.4 Fagocitose em etapas",
      "4.5 Citocinas: a linguagem",
      "4.6 Quimiocinas e nomes que voltam",
      "4.7 Plasticidade da resposta inata",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#set-etapa("Etapa 1 — texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"
