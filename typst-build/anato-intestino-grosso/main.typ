// ================================================================
// MAIN.TYP -- anato-intestino-grosso
// Pipeline canônico E1 + deck (docs/canon/PIPELINE-E1-DECK.md).
// O PDF termina após E1/Resumindo: E2, E3 e RemNote estão suspensos.
// ================================================================

#import "../../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

#capa(
  "Intestino grosso, reto e canal anal",
  "Anatomia do Sistema Digestório",
  (
    ("Disciplina", "Anatomia — Profa. Dra. Patrícia Castelucci (ICB/USP)"),
    ("Onde estudar", "Moore · Anatomia orientada para a clínica (cap. Abdome e Pelve) · Netter, Atlas de Anatomia · Prometheus, Atlas de Anatomia · Sobotta, Atlas de Anatomia Humana"),
  ),
)

#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — Partes, mobilidade e marcas de superfície", (
      "1.1 As dez partes, na ordem do trânsito",
      "1.2 Fixo e móvel: a mobilidade decide a doença",
      "1.3 As três marcas de superfície",
    )),
    ("PARTE II — Junção ileocecal e apêndice", (
      "2.1 Por dentro do ceco: a válvula ileocecal",
      "2.2 O apêndice vermiforme: onde está e como se acha",
    )),
    ("PARTE III — O reto", (
      "3.1 Trajeto, flexuras e ampola",
      "3.2 A flexura anorretal e o puborretal",
      "3.3 As relações peritoneais do reto",
    )),
    ("PARTE IV — O canal anal e a linha pectinada", (
      "4.1 O relevo interno do canal anal",
      "4.2 A linha pectinada e suas consequências",
      "4.3 Os dois esfíncteres e a continência",
    )),
  )),
))

#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

#include "resumindo.typ"
