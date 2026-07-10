# Curadoria AnKing — bioq-glicogenio

**Título:** Metabolismo do glicogênio
**UC/Prova:** UC01/P4 · **Gerado em:** 2026-07-04
**Total curado (kept):** 44 · **Alvo:** 30–50 · **Cobertura AnKing:** 9/17 COBERTOS (4 parciais, 4 lacunas)
**Tag-âncora:** `NEBLI::bioq-glicogenio`

Perfil **decoreba** (metabolismo): enzimas, regulação e as 4 glicogenoses da E1 vêm com completude. O AnKing Step1 cobre com força a parte factual (enzima→doença, fosforilação recíproca), mas **não carda** os "porquês" mecanísticos que a E1 ensina (problema osmótico, fosfoglicomutase, glicogenina, custo de 2 ATP) — esses viram LACUNA apontando slide + Lehninger cap. 15.

## Checklist-alvo (da E1) — fonte-verdade
Fonte: E1 de `typst-build/bioq-glicogenio.pdf` (PARTES I–III). Também em `arquivos-trabalho/checklist-bioq-glicogenio.tsv`.

| id | Frase-alvo (o que um card teria que testar) | Termos |
|---|---|---|
| 1.1 | Por que polimerizar: problema osmótico (glicose livre puxa água; glicogênio conta como 1 partícula) | glycogen / osmotic |
| 1.2 | Árvore ramificada: extremidades redutora vs não-redutoras; ramos = velocidade; ligações α-1,4 e α-1,6 | branching / non-reducing |
| 1.3 | Fígado (tampão da glicemia, exporta) vs músculo (egoísta, consumo próprio) | liver / muscle glycogen |
| 2.1 | Glicogenólise: fosforilase usa fosfato (fosforólise) → glicose-1-fosfato; economiza 1 ATP | phosphorylase / phosphorolysis |
| 2.2 | Enzima desramificadora bifuncional: transferase + α-1,6-glicosidase; limit dextrin | debranching / glucanotransferase |
| 2.3 | Glicose-6-fosfatase no fígado/rim mas não no músculo — decide o destino da G6P | glucose-6-phosphatase |
| 2.4 | Fosfoglicomutase move o fosfato do C1 para o C6 (G1P → G6P) | phosphoglucomutase |
| 2.5 | Glicogênese: glicose ativada como UDP-glicose (via UTP; Leloir) | UDP-glucose |
| 2.6 | Glicogênio sintase alonga por ligação α-1,4; enzima limitante da síntese | glycogen synthase |
| 2.7 | Glicogenina: primer que se autoglicosila e dá o núcleo inicial | glycogenin |
| 2.8 | Enzima ramificadora cria as ligações α-1,6 (ramos) | branching enzyme |
| 2.9 | Custo de 2 ATP por glicose incorporada (hidrólise irreversível do pirofosfato) | 2 ATP / pyrophosphate |
| 3.1 | Regulação alostérica: músculo lê AMP (ativa fosforilase), fígado lê glicose; ATP/G6P inibem | allosteric / AMP |
| 3.2 | Cascata glucagon/epinefrina: GPCR → adenilil-ciclase → cAMP → PKA → fosforilase quinase; amplificação | glucagon / cascade |
| 3.3 | Fosforilação recíproca: um fosfato ativa fosforilase e inativa sintase (nunca correm juntas) | phosphorylation reciprocal |
| 3.4 | Insulina → PP1 desfosforila (inverte); fosfodiesterase degrada cAMP | insulin / PP1 |
| 3.5 | Glicogenoses: von Gierke (I, G6Pase), Pompe (II, maltase ácida), Cori (III, desramificadora), McArdle (V, fosforilase muscular) | von Gierke / Pompe / Cori / McArdle |

## Camada 1 — tags candidatas (grossa)
Saída de `buscar_tags_lote.py checklist-bioq-glicogenio.tsv --md` (122 tags brutas; abaixo só as CANDIDATAS on-topic; o resto = RUÍDO — lisossomais/esfingolipidoses, inibidores de fosfodiesterase da farmaco autonômica, simpaticomiméticos, tireoide, cinética hexo/glucoquinase).

| Subárvore candidata | #cards | Classe | Decisão |
|---|---|---|---|
| Bootcamp::Biochemistry::08_Glycogen (glicogênese/glicogenólise/regulação/5 doenças) | ~130 | CANDIDATA | Camada 2 — núcleo da aula |
| FirstAid::01_Biochem::06_Metabolism::36_Glycogen / 37_Glycogen_storage_diseases / 35_Glycogen_regulation | 18+ | CANDIDATA | Camada 2 |
| Physeo::05_Biochem::05_Metabolism::07_Glycogen / 08_Von_Gierke_&_Cori / 09_Pompe_&_Mcardle | 68+ | CANDIDATA | Camada 2 |
| FirstAid/Physeo::…::Lysosomal_storage_diseases (esfingolipidoses) | 53+50 | RUÍDO | rejeita (fora da aula; só Pompe é lisossomal e vem pela subárvore glicogênio) |
| …::Phosphodiesterase_inhibitors / Sympathomimetics / Glucagon endócrino | vários | RUÍDO | rejeita (farmaco/fisio endócrina, não a cascata do glicogênio) |

Pool unificado (dedup por note): **108 notes únicos** em `arquivos-trabalho/anking-pool-bioq-glicogenio.json`.

## Camada 2 — curadoria card-a-card (108 lidos → 44 kept)
Keep/drop pelo gate (conceito na E1) + perfil decoreba (card carrega mecanismo). Índices referem `_pool-glicogenio-legivel.txt`.

**KEPT por cluster (44):**
- **Regulação hormonal / recíproca (3.3, 3.4):** 2, 4 (insulina↓/glucagon↑ glicemia via glicogênio), 12, 13, 14, 15 (quarteto da fosforilação recíproca: fosfo→fosforilase ativa/sintase inativa; desfosfo→inverte), 38 (sintase inibida por AMP/epi/glucagon), 39 (sintase ativada por insulina/G6P).
- **Glicogênese (2.5, 2.6, 2.8):** 32 (sintase = limitante), 34 (G1P→UDP-glicose via UDP-glicose pirofosforilase), 35 (UDP-glicose→glicogênio), 36 (sintase faz α-1,4), 37 (ramificadora faz α-1,6).
- **Glicogenólise / desramificação (2.1, 2.2):** 33 (fosforilase = limitante), 40 (fosforilase libera G1P até 4 resíduos), 41 (transferase move 3 resíduos), 42 (α-1,6-glicosidase corta o último → glicose livre), 43 (α-1,4-glicosidase/maltase ácida lisossomal — base do Pompe), 44 (limit dextrins), 96 (fosforilase adiciona Pi sem ATP = fosforólise).
- **Destino da G6P / fígado×músculo (1.3, 2.3):** 49 (músculo: G6P presa, queimada no exercício — sem G6Pase), 85 (G6P→glicose via G6Pase, fígado/rim), 89 (glicogenólise hepática = fonte de glicose no jejum entre refeições).
- **Regulação alostérica (3.1):** 47 (AMP ativa fosforilase no músculo), 48 (ATP/insulina/G6P inibem fosforilase).
- **Cascata (3.2):** 45 (epinefrina ativa fosforilase via receptor β), 104 (Ca²⁺ + fosforilase quinase sincronizam glicogenólise à contração).
- **Glicogenoses (3.5):** von Gierke 51 (AR), 52 (=GSD I), 53 (=G6Pase), 54 (glicogênio fígado/rim, hepatomegalia), 56 (gliconeogênese+glicogenólise comprometidas, fígado afetado não músculo); Pompe 59 (=GSD II), 60 (=maltase ácida lisossomal α-1,4), 61 (cardiomegalia); Cori 64 (=GSD III), 65 (=desramificadora), 66 (limit dextrin acumula); McArdle 71 (=GSD V), 72 (=fosforilase muscular/miofosforilase), 73 (cãibras no exercício); recall 81 (hipoglicemia grave=von Gierke), 82 (limit dextrin=Cori), 83 (↑glicogênio muscular=McArdle).

**DROP (categorias, 64 cards):**
- Sinalização do receptor de insulina (dimerização, IRS-1, SH2, PI3K, GLUT4): 8, 9, 10, 11, 105 — mecanismo além da E1.
- Cinética hexoquinase×glucoquinase (Km/Vmax/indução/feedback): 17–29 — tópico separado (fosforilação da glicose).
- Glicólise/anaeróbia/NADH: 16; intolerância hereditária à frutose: 30, 31 — outras vias.
- Colorações histológicas (PAS, oil red O, diastase): 50, 87, 88, 103 — histo/pato.
- GSD IV (Andersen) e VI (Hers): 69, 70, 77, 78, 79, 80 — a E1 lista só I/II/III/V.
- Clínica USMLE além da linha da E1 (labs de von Gierke lactato/ácido úrico/gota/adenoma, tratamento cornstarch, mioglobinúria/arritmia/second-wind/curva de lactato/vinhetas): 3, 5, 6, 7, 46, 55, 57, 58, 62, 63, 67, 68, 74, 75, 76, 84, 86, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 106, 107, 108, 1.

## Cobertura por PARTE da E1 (gap-analysis)

### PARTE I — Por que guardar como glicogênio
| id | Cobertura | #cards | Fonte da lacuna (se PARCIAL/LACUNA) |
|---|---|---|---|
| 1.1 Problema osmótico da polimerização | LACUNA | 0 | slide-01/02 + Lehninger cap.15 — AnKing Step1 não carda o "porquê" osmótico |
| 1.2 Árvore ramificada; redutora×não-redutoras; α-1,4 e α-1,6 | PARCIAL | 2 | slide-03/04 + E1: as ligações estão cardadas (36/37), mas extremidade redutora×não-redutora não |
| 1.3 Fígado (exporta) × músculo (consumo próprio) | COBERTO | 3 | — (49, 85, 89) |

### PARTE II — As duas vias
| id | Cobertura | #cards | Fonte da lacuna |
|---|---|---|---|
| 2.1 Glicogenólise: fosforólise → G1P; economia de 1 ATP | COBERTO | 3 | — (33, 40, 96) |
| 2.2 Desramificadora bifuncional; limit dextrin | COBERTO | 4 | — (41, 42, 43, 44) |
| 2.3 G6-fosfatase fígado/rim, não músculo | COBERTO | 2 | — (49, 85) |
| 2.4 Fosfoglicomutase (G1P → G6P) | LACUNA | 0 | slide-08 + Lehninger — sem card dedicado no AnKing |
| 2.5 UDP-glicose (ativação por UTP; Leloir) | COBERTO | 2 | — (34, 35) |
| 2.6 Glicogênio sintase α-1,4; enzima limitante | COBERTO | 4 | — (32, 35, 36, 39) |
| 2.7 Glicogenina (primer autoglicosilante) | LACUNA | 0 | slide-14 + Lehninger — AnKing não carda glicogenina |
| 2.8 Enzima ramificadora (α-1,6) | COBERTO | 1 | — (37) |
| 2.9 Custo de 2 ATP / hidrólise do pirofosfato | LACUNA | 0 | slide-16 + E1 (a conta passo a passo) — sem card no AnKing |

### PARTE III — A regulação
| id | Cobertura | #cards | Fonte da lacuna |
|---|---|---|---|
| 3.1 Alostérico: músculo AMP, fígado glicose; ATP/G6P inibem | PARCIAL | 2 | slide-24 + E1: AMP-músculo (47) e inibição por ATP/G6P (48) cardados; sensor de glicose hepático não |
| 3.2 Cascata glucagon/epi → cAMP → PKA → fosforilase quinase | PARCIAL | 2 | slide-27 + E1 (cascata completa) / FirstAid Adenylyl_Cyclase: epi→fosforilase (45) e Ca²⁺→quinase (104) cardados; elo adenilil-ciclase/cAMP/PKA não |
| 3.3 Fosforilação recíproca (um fosfato, efeitos opostos) | COBERTO | 5 | — (12, 13, 14, 15, 38) |
| 3.4 Insulina → PP1; fosfodiesterase degrada cAMP | PARCIAL | 4 | slide-30 + E1: insulina=armazenar cardada (2,4,14,15,39); PP1 e fosfodiesterase nomeadas não |
| 3.5 Glicogenoses I/II/III/V | COBERTO | 17 | — (bloco von Gierke/Pompe/Cori/McArdle + recall) |

## Resumo de lacunas → onde completar (proativo)
- **Problema osmótico (1.1), fosfoglicomutase (2.4), glicogenina (2.7), custo de 2 ATP (2.9):** o AnKing Step1 não carda esses "porquês" mecanísticos — estudar pelo **slide da Profa. MHG + Lehninger cap. 15** e pela própria E1, que os ensina em prosa.
- **Extremidade redutora×não-redutora (1.2), sensor de glicose hepático (3.1), elo adenilil-ciclase/cAMP/PKA (3.2), PP1/fosfodiesterase (3.4):** parcialmente cardados; completar pelo slide + E1.

44 cards do AnKing cobrem com força as enzimas, a fosforilação recíproca e as quatro glicogenoses da E1; os quatro "porquês" mecanísticos (osmose, fosfoglicomutase, glicogenina, custo de 2 ATP) o Step1 não carda — ficam com o slide + Lehninger, como marcado.
