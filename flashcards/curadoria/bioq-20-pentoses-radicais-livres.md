# Curadoria AnKing — bioq-20-pentoses-radicais-livres

**Título:** Via das Pentoses-Fosfato: NADPH, Ribose e Defesa Antioxidante
**UC/Prova:** UC02/P4 · **Gerado em:** 2026-07-05
**Total curado (kept):** 45 · **Alvo:** 30–50 · **Cobertura AnKing:** 7/13 COBERTOS (5 parciais, 1 lacuna)
**Tag-âncora:** `NEBLI::bioq-20-pentoses-radicais-livres`

Perfil **decoreba** (metabolismo): enzimas, produtos e o circuito NADPH→glutationa→hemácia vêm com força. O AnKing Step1 cobre com competência a fase oxidativa (G6PD, saldo 2 NADPH + CO2), o circuito glutationa (GSH/GSSG, peroxidase, redutase), as ERO (cascata superóxido→H2O2→•OH, Fenton, SOD/catalase) e a deficiência de G6PD (X-linked, favismo, primaquina, resistência à malária). **Não carda**: a distinção NADPH≠NADH pelo fosfato-etiqueta (1.3), os 4 cenários de demanda (2.4), a regulação alostérica G6PD-NADPH/NADP+ (2.5), nem transcetolase/transaldolase por nome (2.3). Esses viram PARCIAL/LACUNA apontando a E1 + slide.

## Checklist-alvo (da E1) — fonte-verdade
Fonte: `typst-build/_par_bioq-20-pentoses-radicais-livres/etapa1.typ`. Também em `arquivos-trabalho/checklist-bioq-20-pentoses-radicais-livres.tsv`.

| id | Frase-alvo (o que um card teria que testar) | Termos |
|---|---|---|
| 1.1 | Três destinos da G6P: glicogênio (reserva), glicólise (energia) ou via das pentoses (construção) — a via NÃO gera ATP | pentose_phosphate\|HMP_shunt\|G6P\|hexose_monophosphate |
| 1.2 | Dois produtos da via: NADPH (poder redutor) e ribose-5-fosfato (esqueleto de nucleotídeos); sem saldo de ATP | NADPH\|ribose_5_phosphate\|pentose_phosphate\|nucleotide_synthesis |
| 1.3 | NADPH ≠ NADH: fosfato extra é etiqueta; NADH alimenta cadeia respiratória; NADPH constrói e protege | NADPH\|NADH\|reducing_power\|cofactor |
| 1.4 | Onde/quando: citosol; ~20% da glicose; ativo em fígado/tecido adiposo/glândula mamária/córtex adrenal/hemácia; hemácia = única fonte de NADPH | pentose_phosphate_pathway\|liver\|adipose\|adrenal_cortex\|red_blood_cell |
| 2.1 | Duas fases: OXIDATIVA (irreversível, gera NADPH + CO2 + ribose) e NÃO-OXIDATIVA (reversível, rearranja açúcares, sem NADPH) | oxidative_phase\|non_oxidative_phase\|HMP_shunt\|irreversible |
| 2.2 | Fase oxidativa: G6PD (passo controlador, irreversível) → 6-fosfogliconato desidrogenase (descarboxila, libera CO2, gera 2º NADPH) → ribulose-5-P; saldo: 2 NADPH + 1 CO2 + pentose | G6PD\|glucose_6_phosphate_dehydrogenase\|6_phosphogluconate\|ribulose_5_phosphate\|NADPH |
| 2.3 | Fase não-oxidativa: transcetolase (2C) + transaldolase (3C) interconvertem pentoses em F6P e G3P (intermediários da glicólise); reversível | transketolase\|transaldolase\|non_oxidative\|fructose_6_phosphate\|glyceraldehyde_3_phosphate |
| 2.4 | Quatro cenários de demanda: só ribose (só não-oxidativa), NADPH=ribose (oxidativa), muito NADPH/pouca ribose (oxidativa+reciclagem), NADPH+ATP (oxidativa+glicólise) | HMP_shunt\|NADPH\|ribose\|demand\|lipogenesis |
| 2.5 | Regulação: G6PD inibida por NADPH (inibição por produto), ativada por NADP+; razão NADPH/NADP+ é o sensor | G6PD_regulation\|NADPH_inhibition\|product_inhibition\|rate_limiting |
| 3.1 | Radicais livres: cascata ERO (O2→superóxido→H2O2→radical hidroxila); reação de Fenton (H2O2 + Fe2+ → hidroxila); superóxido dismutase e catalase | reactive_oxygen_species\|ROS\|superoxide\|hydrogen_peroxide\|hydroxyl_radical\|Fenton\|superoxide_dismutase\|catalase |
| 3.2 | Glutationa: GSH doa elétrons ao H2O2 (via glutationa peroxidase) → forma GSSG; glutationa redutase regenera 2 GSH gastando NADPH; circuito G6PD→NADPH→glutationa→ERO neutralizada | glutathione\|GSH\|GSSG\|glutathione_reductase\|glutathione_peroxidase\|NADPH |
| 3.3 | Hemácia: sem mitocôndria (única fonte NADPH = via das pentoses), sem reposição de enzimas; NADPH mantém Fe2+; falha → corpos de Heinz → hemólise | red_blood_cell\|Heinz_bodies\|hemolysis\|RBC\|NADPH\|hemoglobin |
| 3.4 | Deficiência de G6PD: enzimopatia mais comum (~400M); hemólise por oxidante (primaquina, sulfas, infecção, favas); ligada ao X; resistência à malária (P. falciparum) | G6PD_deficiency\|favism\|primaquine\|hemolytic_anemia\|X_linked\|malaria_resistance |

## Camada 1 — tags candidatas (grossa)
Saída de `buscar_tags_lote.py checklist-bioq-20-pentoses-radicais-livres.tsv --md` (578 tags brutas; abaixo só as CANDIDATAS on-topic; o resto = RUÍDO — neuro/esclerose múltipla, aterosclerose/doença cardiovascular, próstata, osteoporose, doença hepática cirrótica, Plasmodium sem contexto G6PD, hemólise autoimune genérica, regimes de controle de pressão, neoplasias variadas).

| Leaf-tag (recurso::caminho) | #cards | Conceitos | Classe | Decisão |
|---|---|---|---|---|
| Bootcamp::Biochemistry::07_Oxidative_Stress::02_Pentose_Phosphate_Pathway:_Uses_of_NADPH_and_Clinical_Implications | ~39 | 1.1,1.2,1.3,1.4,2.1,2.2,2.3,2.4,2.5,3.2,3.3 | CANDIDATA | Camada 2 — núcleo da aula |
| Bootcamp::Biochemistry::07_Oxidative_Stress::01_Pentose_Phosphate_Pathway | ~17 | 1.1,1.2,1.4,2.1,2.3,2.4 | CANDIDATA | Camada 2 |
| Bootcamp::Hematology_and_Oncology::04_Normocytic_Anemia::06_G6PD_Deficiency | ~40 | 1.1,2.2,3.4 | CANDIDATA | Camada 2 |
| FirstAid::01_Biochem::06_Metabolism::16_Pentose_phosphate_pathway | ~16 | 1.1,1.2,1.4,2.1,2.3,2.4 | CANDIDATA | Camada 2 |
| FirstAid::01_Biochem::06_Metabolism::17_Glucose-6-phosphate_dehydrogenase_deficiency | ~36 | 1.1,2.2,3.4 | CANDIDATA | Camada 2 |
| FirstAid::04_Pathology::01_Cellular_Injury::07_Free_radical_injury | ~15 | 3.1 | CANDIDATA | Camada 2 — cascata ERO |
| B&B::04_Biochem::02_Metabolism::05_HMP_Shunt (+ Extra) | ~68 | 1.1,1.2,1.4,2.1,2.3,2.4,3.2,3.3,3.4 | CANDIDATA | Camada 2 — maior fonte |
| B&B::18_Pathology::01_General::03_Free_Radicals (+ Extra) | ~55 | 3.1 | CANDIDATA | Camada 2 — ERO/Fenton |
| Physeo::05_Biochem::05_Metabolism::12_HMP_Shunt | ~63 | 1.1,2.1,2.4 | CANDIDATA | Camada 2 |
| SketchyBiochem::01_Metabolism::01_Carbohydrates::13_Pentose_Phosphate_Pathway_&_G6PD_Deficiency | ~40 | 1.1,1.2,1.4,2.1,2.2,2.3,2.4,3.4 | CANDIDATA | Camada 2 |
| SketchyPath::09_Blood_&_Coagulation::02_Normocytic_&_Macrocytic_Anemias::03_G6PD_Deficiency_&_Autoimmune_Hemolytic_Anemia_(AIHA) | ~62 | 1.1,2.2,3.4 | CANDIDATA | Camada 2 — maioria cai em AIHA (DROP) |
| Bootcamp::Biochemistry::12_Vitamins::07_Vitamin_E_Antioxidant_Pathway_and_Functions | ~8 | 3.1,3.2 | CANDIDATA | Camada 2 — só os 2 cards de glutationa/•OH |
| Pathoma::01_Growth_Adaptations::04_Free_Radical_Injury | ~14 | 3.1 | CANDIDATA | Camada 2 |
| DirtyMedicine::01_Biochemistry_&_Genetics::03_HMP_Shunt_(Pentose_Pathway) | ~18 | 1.1,2.1,2.3,2.4 | CANDIDATA | Camada 2 |
| Pixorize::01_Biochemistry::02_Biochemical_Pathways::11_HMP_Shunt_(Pentose_Phosphate_Pathway) | ~20 | 1.1,1.2,1.4,2.1,2.3,2.4 | CANDIDATA | Camada 2 |
| Pixorize::01_Biochemistry::03_Metabolic_Disorders::04_G6PD_Deficiency | ~28 | 1.1,2.2,3.4 | CANDIDATA | Camada 2 |
| Physeo::11_Pathology::07_General_Pathology::05_Free_Radical_Injury | ~15 | 3.1 | CANDIDATA | Camada 2 |

> **Sem classe PURA** (canônico 2026-07-04): toda tag CANDIDATA passou pela Camada 2 — nenhum card entrou sem ser lido.

Pool unificado (dedup por nota): **169 notas únicas** em `arquivos-trabalho/anking-pool-bioq-20-pentoses-radicais-livres.json`.

## Camada 2 — curadoria card-a-card (169 lidos → 45 kept)
Keep/drop pelo gate (conceito na E1) + perfil decoreba (card carrega mecanismo). Índices referem a ordem no pool.

**KEPT por cluster (45):**

- **Localização e produtos da via (1.1, 1.2, 1.4):** De1m5OEf4j (HMP no citoplasma), dxAS[ISwR7 (ribose-5-P para síntese de nucleotídeos), DkO](+hW%- (HMP não usa nem produz ATP), o8,26,Y&]~ (HMP ativo em glândula adrenal/fígado/glândula mamária/hemácias), Iyy]|!MP+X (no fígado: NADPH para FA/colesterol/esteroides), xPE~:zK#N* (síntese de ácidos graxos requer NADPH do HMP shunt + enzima málica), cgqJg20-*) (síntese de purinas começa com ribose-5-P), i%-Bph=qn> (NADPH usado em processos anabólicos — vs NAD+ nos catabólicos), kD4h(2?{>4 (HMP fornece NADPH para reações redutoras: glutationa, FA, colesterol).

- **Fase oxidativa (2.1, 2.2):** e,lljGR7?S (G6P → ribulose-5-P via G6PD; 6-fosfogliconato como intermediário), sVq]8w|)=y (saldo: 1 CO2 + 2 NADPH por G6P), PRUpVM*i5+ (conversão G6P→ribulose-5-P é IRREVERSÍVEL), RaEDQ5]]10 (G6PD = enzima limitante do HMP shunt).

- **Fase não-oxidativa / elo com glicólise (2.3):** ih8HIyFIk- (ribulose-5-P → ribose-5-P; também → G3P + F6P; reação reversível).

- **Circuito glutationa / NADPH (3.2):** rKBHTacy;) (nas hemácias, HMP fornece NADPH para redução de H2O2 via glutationa reduzida), kg.u)A]t,2 (GSSG → 2 GSH via glutationa redutase, cofatores NADPH + FAD), mE}6gDA!&i (glutationa redutase requer NADPH, fornecido pela G6PD), jUF4v|84_] (G6P → 6-fosfogliconato via G6PD: 1 NADPH; esse NADPH alimenta a glutationa redutase), 0*#qZdz=w (GSH reduzida → GSSG via glutationa peroxidase), L)B@LYazn3 (GSSG = glutationa oxidada), CP:0.`KnC. (H2O2 → H2O via glutationa peroxidase), Jk/cgK.iLY (H2O2 neutralizado por glutationa reduzida), bK!25KI#Qc (NADPH da G6PD necessário para regenerar GSH; deficiência de G6PD reduz essa capacidade).

- **Hemácia no fio da navalha (3.3):** i+FczPGWU9 (hemácias expostas a estresse oxidativo por H2O2), pwbs?YbRFb (corpos de Heinz em hemácias com deficiência de G6PD), BL/E.K+A{j (corpos de Heinz = precipitação de hemoglobina desnaturada), end43ObgsH (na deficiência de G6PD, estresse oxidativo → corpos de Heinz).

- **Cascata ERO + Fenton (3.1):** BlbX;4W7F1 (hemocromatose: dano via radicais livres; Fe2+ → reação de Fenton), p=#mU)uj~~ (O2 + 1e → superóxido O2−), c!X=ETj{4* (O2 + 2e → H2O2), s1%l0plglB (O2 + 3e → radical hidroxila •OH), r;]Q/Z3N.w (radical hidroxila = radical de O2 mais danoso), I#VextE;Uv (metais livres → radicais livres via reação de Fenton), hC#!`n>lw* (radicais livres → peroxidação lipídica + oxidação de DNA/proteínas), gfL8ap+/>U (superóxido dismutase reduz O2− a H2O2), ACBL/at9$] (catalase + glutationa peroxidase reduzem H2O2).

- **Deficiência de G6PD (3.4):** O9HT%FH3,t (deficiência de G6PD = meia-vida reduzida da enzima), k8$^{ST^)3 (deficiência de G6PD = X-linked recessiva), M_4=n14ge$ (deficiência de G6PD → hemácias suscetíveis ao estresse oxidativo — NADPH reduzido → GSH reduzida), z;/L<+/|1. (alta frequência do alelo mutante G6PD = proteção contra P. falciparum), b0#~aAYzGn (causa mais comum de estresse oxidativo em G6PD = infecção), w+]0}+^93D (favas mediterrâneas = fonte de estresse oxidativo — favismo), Qrk`G!A`I} (sulfonamidas contraindicas em G6PD; outros incluem antimaláricos como primaquina), n5fCjT7B|r (primaquina → estresse oxidativo, contraindicada em G6PD), p<O[WXYXLS (deficiência de G6PD = enzimopatia mais comum das hemácias).

**DROP (categorias, 124 cards):**
- AIHA (autoimune hemolítica) — IgG/IgM, Coombs, warm/cold agglutinin, SLE/CLL associação, tratamento: [3], [67]–[94], [145], [154]–[155], [160], [165], [167] — AIHA não está na E1.
- Hexoquinase/glucoquinase (entrada de glicose na célula, Km/Vmax): [4], [5] — tópico separado, não ensinado na E1.
- Vitaminas antioxidantes (E, A, C) como tópico principal: [39]–[41] — não está na E1.
- Ciclo de Krebs intermediário / CYP2E1 / álcool / etanol: [6], [43] — fora da E1.
- Burst respiratório neutrofílico / CGD: [21], [119]–[131], [140]–[141], [148]–[150], [169] — neutrófilos/CGD não estão na E1.
- Vitamina B1 (tiamina) / Wernicke-Korsakoff: [36]–[38], [95], [164] — fora da E1.
- Variantes africana/mediterrânea de G6PD (meia-vida comparada): [53], [54] — E1 não discute variantes.
- Clínica USMLE além da E1: hemoglobinúria + dor lombar, labs da hemólise (haptoglobina, bilirrubina, LDH), Heinz preparation, diagnóstico enzimático semanas pós-crise, vinhetas clínicas AA/malária: [51], [52], [57]–[58], [63], [65]–[66], [142]–[144], [146]–[147], [151]–[153], [166], [168].
- CCl4, acetaminofeno/NAPQI, Wilson disease, lipofuscina, hemochromatosis diagnóstico, zonas hepáticas, fase I/II drogas, radiação ionizante, reperfusão cardíaca: [1], [2], [6], [96 parcialmente — apenas a Fenton mantida], [97]–[104], [108], [116]–[118], [129]–[134], [138], [158], [161]–[163] — fora do escopo da E1.
- Transferrina/ceruloplasmina como carreadores: [115] — não está na E1.
- Duplicatas (ATP / sin mecanismo adicional): [11], [13], [19], [28], [30], [34] — drop; conceito coberto por outras cards com mais mecanismo.
- Clonalidade tumoral via G6PD isoformas: [135]–[137], [156]–[157] — fora da E1.
- Antimalarial "Queen DAP" mnemônico / outras drogas específicas: [63], [139], [152]–[153] — E1 menciona primaquina e sulfas; mnemônicos detalhados além da linha.

## Cobertura por PARTE da E1 (gap-analysis)

### PARTE I — O que a via entrega e por que ela existe
| id | Cobertura | #cards | Fonte da lacuna (se PARCIAL/LACUNA) |
|---|---|---|---|
| 1.1 Três destinos da G6P: glicogênio/glicólise/via das pentoses | PARCIAL | 2 | E1 §1.1 + slide-08: framing dos 3 destinos não cardificado; [DkO](+hW%-] (sem ATP) e [kD4h(2?{>4] (NADPH para reações redutoras) cobrem a via das pentoses, mas não enumeram os 3 competidores |
| 1.2 Dois produtos: NADPH (poder redutor) e ribose-5-P (nucleotídeos); sem ATP | COBERTO | 4 | — (dxAS[ISwR7, DkO](+hW%-, kD4h(2?{>4, cgqJg20-*)) |
| 1.3 NADPH ≠ NADH: fosfato extra é etiqueta; papéis opostos (anabólico vs catabólico) | PARCIAL | 1 | E1 §1.3 (fosfato extra como etiqueta, razão NAD+/NADH ~1000 vs NADPH/NADP+ alto) — [i%-Bph=qn>] cobre o papel anabólico do NADPH mas não a estrutura do fosfato-etiqueta |
| 1.4 Onde/quando: citosol, fígado/adrenal/glândula mamária/hemácia; hemácia = única fonte NADPH | COBERTO | 3 | — (De1m5OEf4j, o8,26,Y&]~, Iyy]|!MP+X) |

### PARTE II — Como a via funciona por dentro
| id | Cobertura | #cards | Fonte da lacuna (se PARCIAL/LACUNA) |
|---|---|---|---|
| 2.1 Duas fases: OXIDATIVA (irreversível, faz NADPH + CO2 + ribose) e NÃO-OXIDATIVA (reversível, rearranja açúcares) | PARCIAL | 2 | E1 §2.1 — [PRUpVM*i5+] cobre irreversibilidade da oxidativa; [ih8HIyFIk-] cobre reversibilidade da não-oxidativa; nenhum card enquadra as duas como unidade contrastante |
| 2.2 Fase oxidativa: G6PD (passo controlador), 6-fosfogliconato, ribulose-5-P; saldo 2 NADPH + CO2 | COBERTO | 4 | — (RaEDQ5]]10, e,lljGR7?S, sVq]8w|)=y, PRUpVM*i5+) |
| 2.3 Fase não-oxidativa: transcetolase (2C) + transaldolase (3C); F6P e G3P = elo com glicólise | PARCIAL | 1 | slide-49 + E1 §2.3 — [ih8HIyFIk-] cobre ribulose-5-P → ribose-5-P + → G3P/F6P mas não nomeia transcetolase/transaldolase |
| 2.4 Quatro cenários de demanda (só ribose / NADPH=ribose / muito NADPH / NADPH+ATP) | LACUNA | 0 | E1 §2.4 (tabela de cenários) + slide-18 — AnKing Step1 não carda os 4 cenários como unidade; estudar pela E1 e pelo slide |
| 2.5 Regulação: G6PD inibida por NADPH, ativada por NADP+; razão NADPH/NADP+ como sensor | PARCIAL | 1 | slide-51 + E1 §2.5 — [RaEDQ5]]10] nomeia G6PD como rate-limiting mas não cobre a inibição por NADPH/ativação por NADP+ |

### PARTE III — NADPH contra os radicais livres
| id | Cobertura | #cards | Fonte da lacuna (se PARCIAL/LACUNA) |
|---|---|---|---|
| 3.1 Radicais livres: cascata ERO; reação de Fenton (H2O2 + Fe2+); superóxido dismutase e catalase | COBERTO | 9 | — (p=#mU)uj~~, c!X=ETj{4*, s1%l0plglB, r;]Q/Z3N.w, I#VextE;Uv, hC#!`n>lw*, BlbX;4W7F1, gfL8ap+/>U, ACBL/at9$]) |
| 3.2 Glutationa: GSH/GSSG, peroxidase neutraliza H2O2, redutase regenera GSH gastando NADPH | COBERTO | 9 | — (kg.u)A]t,2, mE}6gDA!&i, jUF4v|84_], 0*#qZdz=w, L)B@LYazn3, CP:0.`KnC., rKBHTacy;), Jk/cgK.iLY, bK!25KI#Qc) |
| 3.3 Hemácia: sem mitocôndria; dependência 100% da via das pentoses; corpos de Heinz → hemólise | COBERTO | 4 | — (i+FczPGWU9, pwbs?YbRFb, BL/E.K+A{j, end43ObgsH) |
| 3.4 Deficiência de G6PD: enzimopatia mais comum; hemólise por oxidante; X-linked; resistência à malária | COBERTO | 9 | — (O9HT%FH3,t, k8$^{ST^)3, M_4=n14ge$, z;/L<+/|1., b0#~aAYzGn, w+]0}+^93D, Qrk`G!A`I}, n5fCjT7B|r, p<O[WXYXLS) |

## Resumo de lacunas → onde completar (proativo)
- **1.1 (três destinos da G6P):** AnKing não enquadra a decisão entre os 3 destinos competidores. Estudar pelo **slide-08 + E1 §1.1** (o mini-resumo "G6P tem 3 saídas" está na prosa introdutória).
- **1.3 (NADPH ≠ NADH — fosfato-etiqueta e razões opostas):** AnKing cobre papel anabólico vs catabólico em geral, mas não a estrutura do fosfato extra como discriminante. Estudar pelo **slide-09 + E1 §1.3** (figura NADPH vs NADH em vermelho).
- **2.1 (duas fases como unidade contrastante):** nenhum card enquadra as duas fases lado-a-lado. Estudar pelo **E1 §2.1** (intro que define irreversível vs reversível antes de detalhar cada fase).
- **2.3 (transcetolase e transaldolase por nome):** AnKing cobre o produto (ribose-5-P → G3P/F6P) mas não as enzimas. Estudar pelo **slide-49 + E1 §2.3** (transcetolase = 2C, transaldolase = 3C).
- **2.4 (quatro cenários de demanda — LACUNA):** AnKing Step1 não carda os 4 cenários. Estudar pela **E1 §2.4** (tabela: demanda | qual ramo | gera NADPH?) + slide-18.
- **2.5 (regulação G6PD por NADPH/NADP+):** AnKing só cita G6PD como rate-limiting, sem a inibição por produto. Estudar pelo **slide-51 + E1 §2.5** (termostato NADPH/NADP+).

45 cards do AnKing cobrem com força o circuito glutationa, a fase oxidativa, a cascata de ERO e a deficiência de G6PD; a estrutura NADPH≠NADH, os 4 cenários de demanda, a regulação alostérica e as enzimas da fase não-oxidativa ficam com o slide + E1, como marcado.
