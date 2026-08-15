// ================================================================
// MAIN.TYP -- patologia-adaptacao-celular-acumulos
// ================================================================

#import "../../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
#capa(
  "Adaptação celular e acúmulos",
  "Patologia Geral",
  (
    ("Disciplina", "Patologia Geral"),
    ("Onde estudar", "Robbins & Cotran — Bases Patológicas das Doenças, cap. de adaptações celulares, lesão e morte celular · Robbins Patologia Básica, mesmo capítulo · Bogliolo — Patologia Geral, capítulos de degenerações e pigmentações"),
  ),
)

// ======= SUMÁRIO =======
#sumario((
  ("Etapa 1 — Texto didático", (
    ("PARTE I — A célula sob estresse e o princípio da adaptação", (
      "1.1 Estresse, adaptação e o novo estado de equilíbrio",
      "1.2 O que o tecido pode fazer depende de ele poder se dividir",
      "1.3 As quatro respostas adaptativas",
    )),
    ("PARTE II — Crescer: hipertrofia e hiperplasia", (
      "2.1 Hipertrofia: a mesma quantidade de células, cada uma maior",
      "2.2 Hipertrofia fisiológica e patológica",
      "2.3 Do estímulo ao gene: como a hipertrofia é montada",
      "2.4 O limite da adaptação e a virada para a insuficiência",
      "2.5 Hiperplasia: aumento do número de células",
    )),
    ("PARTE III — Encolher e trocar: atrofia e metaplasia", (
      "3.1 Atrofia: a célula que se retrai para caber na demanda",
      "3.2 Quando a atrofia acontece",
      "3.3 O mecanismo da atrofia: ubiquitina, proteassomo e autofagia",
      "3.4 Atrofia, hipoplasia e aplasia",
      "3.5 Metaplasia: trocar o tipo celular por outro mais resistente",
    )),
    ("PARTE IV — Acúmulos intracelulares", (
      "4.1 Por que uma célula acumula alguma coisa",
      "4.2 Esteatose e o trânsito normal de lipídios no hepatócito",
      "4.3 As três vias que levam à esteatose",
      "4.4 Colesterol fora do fígado",
      "4.5 Proteínas e glicogênio",
    )),
    ("PARTE V — Calcificações e pigmentos", (
      "5.1 Calcificação distrófica e calcificação metastática",
      "5.2 Pigmentos exógenos, lipofuscina e melanina",
      "5.3 Pigmentos derivados da hemoglobina",
    )),
  )),
))

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"
