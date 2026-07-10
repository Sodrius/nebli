# blueprint-step1.md — calibração externa por aula (Step 1 + ganchos de residência BR)

> **Status:** CANÔNICO v1 (2026-06-30). Plugado no pipeline: `CLAUDE.md` § References + `ROLES.md` Redator diretriz 16 + Questionador § "Segunda régua". Refinar conforme Davi traga questões reais.
> **Papel:** artefato de **calibração**, igual ao `banco/indice/banco_slim.json`. O Redator/Questionador consulta este arquivo para decidir *onde aprofundar 1-2 frases na E1* e *que ângulo de Aplicação cobrar na E2/E3*. **Nada deste arquivo vai colado no PDF.** O foco continua sendo o slide do professor — isto só informa a profundidade e o gancho.

## Como usar (regra de leitura)

1. O foco do resumo é **o slide**. O blueprint nunca sequestra o tema da aula.
2. Antes de redigir a E1 de um slug, olhe a linha correspondente:
   - **Aprofundar (E1):** 1-2 frases extras de mecanismo no ponto indicado, *quando o slide já abriu o assunto*. Se o slide não tocou, não força.
   - **Ângulo E2/E3:** 1 questão de Aplicação (ou o texto motivador de uma Integração) pode usar o cenário indicado. Não vira cota — é sugestão calibrada.
   - **Gancho clínico BR:** cenário que bancas de residência (HC-FMUSP/Einstein/UNICAMP) usam para cobrar aquele mecanismo. Serve ao texto motivador e ao Mapa de Confusões, não como conteúdo.
3. **Coluna "Rendimento externo":** ALTO = vale aprofundar/cobrar; MÉDIO = gancho pontual; BAIXO = manter foco puro no slide, sem clínica forçada.
4. Em conflito entre este arquivo e o slide → **o slide vence** (espelha "exemplar vence regra abstrata").

## Por que Step 1 e não as provas literais

USMLE não libera provas passadas — só blueprint público de conteúdo (NBME content outline) + First Aid como mapa de alto rendimento. Residência BR é majoritariamente clínica (descasa do 1º ano básico), então entra apenas como **biblioteca de ganchos clínicos**, não como calibrador de profundidade. O domínio do Step 1 (bioquímica, fisiologia, biocel, biomol, genética, imuno) é o que casa com UC01/UC02.

---

## UC01

### P1 — Estrutura

| Slug | Rend. | Aprofundar na E1 (1-2 frases) | Ângulo E2/E3 | Gancho clínico BR |
|---|---|---|---|---|
| bioq-01-reacoes-quimicas | MÉDIO | ΔG vs ΔG°′; por que reação acoplada (ATP) puxa reação endergônica | Aplicação: prever direção de reação dado ΔG | — |
| fisio-01-introducao | MÉDIO | Compartimentos hídricos (ICF/ECF), regra 60-40-20; osmolaridade efetiva | Integração com transporte de água (P3) | Desidratação iso/hiper/hipotônica |
| biocel-01-membrana-bicamada | ALTO | Fluidez (colesterol bidirecional), assimetria de fosfolípides, flippase/scramblase | Aplicação: fosfatidilserina externalizada = sinal de apoptose (liga biocel-08) | — |
| bioq-02-ph-tampoes | ALTO | Henderson-Hasselbalch; bicarbonato como tampão fisiológico; por que pKa perto de 6,1 importa | Aplicação numérica: prever pH dado HCO₃⁻/CO₂ | Distúrbio ácido-base (gasometria) — clássico de residência |
| bioq-03-lipideos | ALTO | Surfactante (DPPC) e tensão superficial; relação Laplace; SDR do prematuro | Aplicação: por que prematuro faz SDR (déficit surfactante) | SDR neonatal, relação L/S — banca de pediatria |
| bioq-04-aminoacidos | ALTO | Classificação por cadeia lateral; pKa de ionizáveis; aa essenciais | Consolidação: titulação de aa; ponto isoelétrico | — |
| fisio-02-transporte-membrana | ALTO | Primário vs secundário; Na/K-ATPase estequiometria 3:2; simporte/antiporte | Aplicação: ouabaína/digoxina inibe Na/K-ATPase → ↑Ca intracelular | Intoxicação digitálica — residência clínica |
| bioq-05-proteinas-estrutura | ALTO | α-hélice/folha-β; ligação de H; por que prolina quebra hélice | Consolidação: nível estrutural afetado por mutação | — |
| bioq-06-agregacao-proteinas | ALTO | Amiloide (folha-β cruzada); priônica (PrPc→PrPsc); chaperonas | Aplicação: doença de Alzheimer/priônica como falha de enovelamento | Amiloidose, doenças priônicas |
| biocel-02-tecnicas-citoesqueleto | MÉDIO | Actina/microtúbulo/filamento intermediário; dinâmica + drogas (taxol, colchicina) | Aplicação: colchicina na gota; taxol/vincristina como quimioterápico | Gota (colchicina), quimioterapia |
| bioq-07-purificacao-proteinas | BAIXO | — (técnica; baixo rendimento Step 1) | — | — |
| bioq-08a-hemoglobina-I | ALTO | Cooperatividade (T↔R); curva sigmoide; efeito Bohr | Consolidação: deslocamento da curva (pH, CO₂, 2,3-BPG, temp) | — |
| bioq-08b-hemoglobina-II | ALTO | HbF vs HbA (2,3-BPG); HbS (substituição Glu→Val); metaHb | Aplicação: anemia falciforme — mecanismo molecular da polimerização | Falciforme, talassemia — banca de hematologia |
| biocel-03-compartimentos-I | ALTO | Sinal-peptídeo/SRP; RE rugoso; via secretora | Aplicação: I-cell disease (falha de manose-6-fosfato) | — |
| fisio-03-potencial-repouso | ALTO | Equação de Nernst/Goldman; por que repouso ≈ E_K; permeabilidade ao K | Consolidação numérica: prever E_ion | Hipercalemia → alteração de excitabilidade |
| biocel-04-compartimentos-II | ALTO | Golgi/glicosilação; lisossomo; endossomo; tráfego vesicular (clatrina/COP) | Aplicação: doenças de depósito lisossômico | Tay-Sachs, Gaucher |
| fisio-04-propriedades-passivas | MÉDIO | Constante de tempo/espaço; cabo; por que mielina ↑ velocidade | Integração com potencial de ação (P2) | Esclerose múltipla (desmielinização) |
| biocel-05-compartimentos-III | MÉDIO | Mitocôndria/peroxissomo; importação pós-traducional | Aplicação: doença peroxissomal (Zellweger) | — |

### P2 — Função 1

| Slug | Rend. | Aprofundar na E1 (1-2 frases) | Ângulo E2/E3 | Gancho clínico BR |
|---|---|---|---|---|
| fisio-05-potencial-acao | ALTO | Canais Na/K voltagem-dependentes; período refratário; tudo-ou-nada | Consolidação: fase × canal; efeito de bloqueador | Anestésico local (bloqueio Na), arritmia |
| bioq-10-enzimas-I-cinetica | ALTO | Km/Vmax; Michaelis-Menten; Lineweaver-Burk; eficiência catalítica | Consolidação numérica: ler gráfico, prever Km/Vmax | (aula marcada "ÓTIMO RESUMO" por Davi) |
| bioq-11-enzimas-II-regulacao | ALTO | Inibição competitiva/não-comp/incompetitiva (efeito em Km/Vmax); alostérica; covalente | Aplicação: identificar tipo de inibição por gráfico; fármaco como inibidor | Metotrexato (DHFR), estatina (HMG-CoA red), IECA |
| bioq-12-cinetica-enzimatica-lab | MÉDIO | Liga ao gráfico de cinética; controle experimental | Aplicação numérica | — |
| fisio-06-transmissao-sinaptica | ALTO | Cálcio→exocitose; receptor nicotínico; recaptação; EPSP/IPSP | Aplicação: miastenia gravis, botulínica, organofosforado | Miastenia, intoxicação por organofosforado |
| fisio-07-sinalizacao-I | ALTO | GPCR; cascata cAMP/PKA; IP3/DAG/Ca; amplificação | Consolidação: ligante→segundo mensageiro→efeito | Cólera (Gs travado), coqueluche (Gi) |
| bioq-13-carboidratos | MÉDIO | Glicosídicas α/β; glicogênio vs amido vs celulose; GAGs | Integração com glicólise/glicogênio | Intolerância à lactose |
| fisio-08-sinalizacao-II | ALTO | Receptor tirosina-quinase (insulina); JAK-STAT; receptor nuclear | Aplicação: resistência à insulina; sinalização de hormônio esteroide | Diabetes tipo 2 (sinalização da insulina) |
| bioq-14-introducao-metabolismo | ALTO | Estados alimentado/jejum; órgãos-chave; ATP como moeda; NAD⁺/NADH | Integração-âncora para todo o metabolismo | — |
| bioq-15-glicolise | ALTO | Passos irreversíveis (HK, PFK-1, PK); regulação (PFK-1 por ATP/AMP/F2,6BP); destino do piruvato | Aplicação: deficiência de PK → anemia hemolítica; efeito Warburg | Anemia hemolítica por def. de PK; câncer (Warburg) |

### P3 — Função 2 / Molecular

| Slug | Rend. | Aprofundar na E1 (1-2 frases) | Ângulo E2/E3 | Gancho clínico BR |
|---|---|---|---|---|
| bioq-16-gliconeogenese | ALTO | 4 enzimas que contornam glicólise (PC, PEPCK, F1,6BPase, G6Pase); ciclo de Cori; regulação recíproca | Aplicação: von Gierke (def. G6Pase) → hipoglicemia + hepatomegalia | Doença de von Gierke; hipoglicemia de jejum |
| fisio-09-transporte-agua | ALTO | Aquaporinas; osmose; gradiente medular; ADH | Integração com osmolaridade (fisio-01) | SIADH, diabetes insipidus |
| bioq-17-ciclo-krebs-TE-I | ALTO | Passos que geram NADH/FADH₂; enzimas reguladas (IDH, α-KG-DH); anaplerose | Consolidação: rendimento por volta; ponto de regulação | Deficiência de piruvato-desidrogenase (acidose láctica) |
| biomol-20-acidos-nucleicos | ALTO | Watson-Crick; antiparalelismo; Tm e conteúdo GC; estrutura de nucleotídeo | Consolidação: prever Tm; complementaridade | — |
| biomol-21-replicacao-dna | ALTO | Origem, helicase, primase, pol III/I, Okazaki, ligase; direção 5'→3'; telomerase | Aplicação: fármaco que bloqueia replicação; defeito de telomerase | Quimioterápicos, progéria |
| biomol-22-transcricao | ALTO | RNA pol II; promotor/TATA; cap, cauda poliA, splicing; íntron/éxon | Aplicação: α-amanitina (pol II); talassemia por defeito de splicing | β-talassemia (splicing) |
| bioq-19-simulacao-mitocondrial | MÉDIO | Liga à cadeia respiratória; controle respiratório | Integração com bioq-18 | — |
| biomol-23-traducao | ALTO | Código (degeneração, wobble); ribossomo; iniciação/elongação/terminação; antibióticos | Aplicação: antibiótico por etapa (aminoglicosídeo, macrolídeo); mutação nonsense | Mecanismo de antibióticos — micro de residência |
| biomol-24-regulacao-expressao | ALTO | Operon (procarioto); enhancer/silencer; metilação; cromatina (acetilação) | Aplicação: epigenética e câncer; imprinting | Síndromes de imprinting (Prader-Willi/Angelman) |
| biocel-06-nucleo-interfasico | MÉDIO | Envoltório nuclear, poro, lâmina; eucromatina/heterocromatina | Integração com regulação gênica | Laminopatias |
| bioq-18-transporte-eletrons-II | ALTO | Complexos I-IV; quimiosmose; ATP-sintase; desacopladores; inibidores por complexo | Aplicação: cianeto (IV), rotenona (I), oligomicina; def. CoQ10 | Intoxicação por cianeto; doença mitocondrial |
| biocel-07-divisao-celular | ALTO | Ciclo (G1/S/G2/M); ciclina-CDK; checkpoints; APC/C-securina-separatase; p53/Rb | Aplicação: perda de checkpoint → câncer; quimioterápico por fase | Câncer (p53, Rb); quimioterapia ciclo-específica |
| biocel-08-morte-celular | ALTO | Apoptose intrínseca (citocromo c, Bax/Bak, Bcl-2) vs extrínseca (Fas); caspases; vs necrose | Aplicação: Bcl-2 e linfoma; apoptose vs necrose na clínica | Linfoma folicular (t14;18 Bcl-2); isquemia |

---

## UC02

### P1 — Tecidos básicos + introdução à anatomia

| Slug | Rend. | Aprofundar na E1 (1-2 frases) | Ângulo E2/E3 | Gancho clínico BR |
|---|---|---|---|---|
| histo-03-tecidos-epiteliais | MÉDIO | Classificação; junções (oclusão, aderente, gap, desmossomo); polaridade | Aplicação: pênfigo (desmossomo); metaplasia | Pênfigo/penfigoide; metaplasia de Barrett |
| histo-04-tecido-conjuntivo | ALTO | Colágeno (síntese, hidroxilação dep. vit C); MEC; fibroblasto | Aplicação: escorbuto; Ehlers-Danlos; osteogênese imperfeita | Escorbuto; colagenopatias |
| histo-05-tecido-adiposo | MÉDIO | Branco vs marrom (UCP1/termogênese); leptina | Integração com metabolismo de lipídios | Obesidade, sinalização da leptina |
| histo-02-hematopoese | ALTO | Hierarquia de células-tronco; linhagens; eritropoetina; sítios por idade | Aplicação: ler hemograma; onde EPO age | Anemias, leucemias — hematologia de residência |
| biocel-09-diferenciacao-celular | ALTO | Potência (toti/pluri/multi); determinação vs diferenciação; fatores de transcrição-mestre | Integração com regulação gênica (biomol-24) | Células-tronco, terapia regenerativa |
| histo-06-metastase-epitelio-conjuntivo | ALTO | Transição epitélio-mesênquima; degradação de MEC (MMP); membrana basal | Aplicação: cascata metastática; invasão | Carcinoma — estadiamento, metástase |
| anato-01-intro-planos-eixos | BAIXO | — (nomenclatura; baixo rendimento externo) | — | — |

### P2 — Tecidos de suporte + DNA + lipídios + pentoses

| Slug | Rend. | Aprofundar na E1 (1-2 frases) | Ângulo E2/E3 | Gancho clínico BR |
|---|---|---|---|---|
| anato-02-ossos-generalidades | BAIXO | — (anatomia macro; gancho só via histo-07) | — | — |
| histo-07-cartilaginoso-osseo | ALTO | Osteoblasto/clasto/cito; remodelação; RANKL/OPG; ossificação endo/intramembranosa | Aplicação: osteoporose; bisfosfonato; hiperparatireoidismo | Osteoporose, doença de Paget |
| anato-03-articulacoes | BAIXO | — | — | Artrites (gancho clínico só) |
| bioq-20-pentoses-radicais-livres | ALTO | Via das pentoses gera NADPH + ribose; G6PD; glutationa; estresse oxidativo | Aplicação: def. de G6PD → hemólise por oxidante | Def. G6PD (favismo, primaquina) — clássico |
| biomol-25-mutacao-reparo-recombinacao | ALTO | Tipos de mutação; reparo (excisão de base/nucleotídeo, mismatch); recombinação | Aplicação: xeroderma pigmentoso; Lynch (mismatch); BRCA | Xeroderma; câncer hereditário (Lynch, BRCA) |
| anato-04-musculos | BAIXO | — (gancho via histo-08) | — | — |
| histo-08-tecido-muscular | ALTO | Sarcômero; acoplamento excitação-contração; Ca/troponina; tipos de fibra | Aplicação: distrofia (distrofina); rigor mortis | Distrofia de Duchenne |
| bioq-21-lipideos-rotas | ALTO | β-oxidação (carnitina-shuttle); cetogênese; síntese de ác. graxo (citrato/malonil-CoA) | Aplicação: def. de carnitina/MCAD; cetoacidose | MCAD; cetoacidose diabética |
| bioq-22-lipideos-regulacao | ALTO | Insulina/glucagon na lipólise; malonil-CoA inibe CPT-1; regulação recíproca síntese/degradação | Integração com jejum/alimentado (bioq-14) | Dislipidemia, esteatose hepática |

### P3 — Circulatório/linfático + nervoso + embriologia + imuno

| Slug | Rend. | Aprofundar na E1 (1-2 frases) | Ângulo E2/E3 | Gancho clínico BR |
|---|---|---|---|---|
| anato-05-circulatorio-linfatico-I | BAIXO | — (anatomia macro) | — | Gancho via histo-09 |
| histo-09-vasos-sanguineos-linfaticos | MÉDIO | Túnicas; endotélio (NO, von Willebrand); capilar contínuo/fenestrado/sinusoide | Aplicação: aterosclerose começa no endotélio | Aterosclerose, HAS |
| bioq-25-depuracao | ALTO | Bilirrubina (conjugação UGT); ureia; clearance; metabolismo de fármacos (CYP fase I/II) | Aplicação: icterícia pré/intra/pós-hepática; Gilbert; Crigler-Najjar | Icterícia neonatal; síndromes de Gilbert |
| histo-10-tecido-nervoso | ALTO | Neurônio/glia; bainha de mielina (Schwann vs oligodendrócito); barreira hematoencefálica | Aplicação: Guillain-Barré vs EM (PNS vs SNC) | Guillain-Barré, esclerose múltipla |
| anato-06-circulatorio-linfatico-II | BAIXO | — | — | — |
| biomol-26-dna-recombinante-pcr | ALTO | PCR (desnaturação/anelamento/extensão); enzimas de restrição; sequenciamento; clonagem | Aplicação: diagnóstico molecular; PCR na prática clínica | Diagnóstico molecular, RT-PCR |
| histo-11-orgaos-linfaticos | ALTO | Timo (seleção T); linfonodo (zonas B/T); baço (polpa branca/vermelha) | Integração com imuno-01 | Esplenectomia e infecção encapsulada |
| embrio-01-gametogenese-fertilizacao | MÉDIO | Meiose (não-disjunção); espermato vs ovogênese; capacitação | Aplicação: trissomias por não-disjunção (idade materna) | Síndrome de Down, aneuploidias |
| bioq-23-aminoacidos-ureia | ALTO | Ciclo da ureia (CPS-I, OTC); transaminação; destino do esqueleto carbônico | Aplicação: hiperamonemia; def. de OTC; encefalopatia hepática | Hiperamonemia; erros inatos do metabolismo |
| embrio-02-blastocisto-gastrulacao | MÉDIO | Folhetos germinativos e derivados; implantação | Aplicação: derivado de cada folheto | Defeitos de implantação |
| embrio-03-neurulacao | MÉDIO | Tubo neural; fechamento; ác. fólico | Aplicação: defeito de tubo neural (espinha bífida); papel do folato | DTN e suplementação de folato |
| imuno-01-disturbios-imunidade | ALTO | Inata vs adaptativa; hipersensibilidade I-IV; imunodeficiências; complemento | Aplicação: classificar reação (anafilaxia, citotóxica, imunocomplexo, tardia) | Hipersensibilidade — clássico de residência |
| bioq-24-glicogenio | ALTO | Síntese (glicogênio-sintase) vs degradação (fosforilase); regulação hormonal; ramificação | Aplicação: von Gierke vs Pompe vs McArdle vs Cori | Glicogenoses |
| biomol-27-bacterias-patogenicas | MÉDIO | Identificação molecular; Gram; fatores de virulência | Aplicação: diagnóstico microbiológico | Microbiologia clínica |

---

## Síntese — onde o aprofundamento mais agrega (top picks)

Aulas onde Step 1 + clínica de residência convergem fortemente e o aprofundamento de 1-2 frases / ângulo de Aplicação rende mais:

- **bioq-15-glicolise, bioq-16-gliconeogenese, bioq-24-glicogenio** — eixo glicídico com glicogenoses nomeadas (von Gierke, Pompe, McArdle).
- **bioq-18-transporte-eletrons-II** — inibidores por complexo + cianeto (inversão letal já é `#atencao-box` canônico).
- **bioq-08b-hemoglobina-II** — falciforme/talassemia (molecular→clínico direto).
- **bioq-20-pentoses** — G6PD/favismo.
- **bioq-23-aminoacidos-ureia** — ciclo da ureia e hiperamonemia.
- **biocel-07/08** — ciclo celular e apoptose ligados a câncer (p53, Bcl-2).
- **imuno-01** — hipersensibilidade I-IV.
- **histo-04-conjuntivo** — colágeno/vitamina C (escorbuto).

## Limitações desta v1

- Mapeamento feito por conhecimento do blueprint Step 1 (estável) + padrões de residência BR, **sem provas literais** (USMLE não as libera; residência BR está fragmentada/paywall).
- Ganchos de residência são representativos, não exaustivos — refinar conforme Davi traga questões reais.
- Aulas BAIXO rendimento ficam deliberadamente vazias: o sinal "não force clínica aqui" é tão útil quanto o "aprofunde aqui".
