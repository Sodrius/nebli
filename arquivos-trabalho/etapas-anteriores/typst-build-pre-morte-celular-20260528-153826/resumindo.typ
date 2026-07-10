#import "../typst-template/nebli_v2_apostila.typ": *

#resumindo-page((
  (
    "Default é morrer",
    [Em organismo multicelular, a célula só vive enquanto recebe sinais externos (fatores de sobrevivência) que bloqueiam o programa interno de apoptose. Sem sinal, o programa-padrão é morte. Sobreviver é decisão ativa.],
  ),
  (
    "Três tipos de sinal extracelular",
    [Mitógenos disparam divisão (G1→S, liberam freios como Rb). Fatores de crescimento aumentam síntese e diminuem degradação de proteínas (massa celular). Fatores de sobrevivência bloqueiam apoptose. Mesma molécula (PDGF) pode atuar como mais de um tipo.],
  ),
  (
    "Homeostase tecidual",
    [Tecido mantém número constante acoplando divisão e morte. Desbalanço para mais morte gera doenças degenerativas (Alzheimer, Parkinson, AIDS, infarto, anemia aplástica); desbalanço para menos morte gera câncer, autoimunes (lúpus), infecções persistentes.],
  ),
  (
    "Taxonomia moderna (Galluzzi 2018)",
    [ACD = acidental, sem programa (trauma extremo). RCD = regulada, com via molecular dedicada (apoptose, necroptose, autosis, piroptose, ferroptose). PCD = subset fisiológico da RCD (escultura embrionária, renovação epitelial).],
  ),
  (
    "Apoptose — morfologia limpa",
    [Célula encolhe (não incha), cromatina condensa e fragmenta (endonucleases), envelope nuclear se desfaz, blebbing forma corpos apoptóticos. Membrana plasmática permanece íntegra até fagocitose. Sem DAMPs, sem inflamação. Processo requer ATP — sem ATP vai para necrose.],
  ),
  (
    "Sinal 'coma-me' (fosfatidilserina)",
    [Em célula viva, flipase ATP-dependente mantém PS na face interna. Em apoptose, caspases inativam flipase e ativam scramblase — PS aparece externamente. Macrófagos com receptores TIM4/BAI1/estabilina reconhecem PS, fagocitam silenciosamente e produzem IL-10/TGF-β (anti-inflamatórias).],
  ),
  (
    "Caspases — iniciadoras × executoras",
    [Iniciadoras (caspase-2, -8, -9, -10) têm pró-domínio longo (DED ou CARD), ativam-se por proximidade em plataformas (DISC, apoptossomo). Executoras (caspase-3, -6, -7) ativam-se por clivagem, degradam centenas de substratos (lâmina nuclear, citoesqueleto, ICAD libera CAD-DNAse).],
  ),
  (
    "Via extrínseca",
    [Ligante (FasL/TNF/TRAIL) ativa receptor de morte (Fas/TNFR1) → agrupa DDs → recruta FADD via DD-DD → recruta pró-caspase-8 via DED-DED → forma DISC → caspase-8 ativa cliva caspase-3 (tipo I) ou Bid (tipo II). Inibida por receptores armadilha e FLIP.],
  ),
  (
    "Via intrínseca",
    [Estímulo interno (dano DNA, hipóxia, estresse) ativa BH3-only → BAX/BAK formam poro na membrana mitocondrial externa (MOMP) → citocromo c escapa + Smac/Diablo → Apaf-1 oligomeriza em apoptossomo (7 raios) → recruta pró-caspase-9 via CARD-CARD → caspase-9 cliva caspase-3.],
  ),
  (
    "Família Bcl-2 (3 classes)",
    [Efetoras pró-morte: BAX, BAK, BOK — formam o poro do MOMP. Antiapoptóticas: Bcl-2, Bcl-X#sub[L], Mcl-1 — sequestram efetoras. BH3-only: ativadoras (Bid, Bim, Puma) ligam BAX/BAK; sensibilizadoras (Bad, Noxa) ocupam antiapoptóticas. Razão pró/anti decide MOMP.],
  ),
  (
    "Crosstalk extrínseca → intrínseca",
    [Em células tipo II (hepatócitos), caspase-8 cliva Bid → tBid migra à mitocôndria, ativa BAX/BAK como BH3-only ativador, dispara MOMP. Sinal extrínseco vira sinal intrínseco com amplificação massiva. Direção é sempre extrínseca→intrínseca, nunca o oposto.],
  ),
  (
    "IAPs e Smac/Diablo",
    [IAPs (XIAP, cIAP1, cIAP2) bloqueiam caspases ativas — segunda camada de freio após Bcl-2. Smac/Diablo escapa junto com citocromo c no MOMP, desloca IAPs e libera as caspases. Sistema de duas chaves: BAX/BAK abrem a primeira, Smac/Diablo abre a segunda.],
  ),
  (
    "Fatores de sobrevivência — 3 alavancas",
    [(1) Transcricional: receptor → NF-κB/CREB → mais Bcl-2/Bcl-X#sub[L]. (2) PI3K/Akt fosforila Bad, inativando-o (sequestrado por 14-3-3). (3) MAP-cinase regula IAPs, mantendo caspases inibidas. Os três somam: célula bem sinalizada resiste massivamente a estímulos pró-apoptóticos.],
  ),
  (
    "Autofagia (Tipo 2)",
    [Membrana dupla envolve citoplasma → autofagossomo → funde com lisossomo → degrada e recicla. Primariamente citoprotetora em jejum/hipoxia. Excesso prolongado pode levar a autosis (morte autofágica, depende de Na⁺/K⁺-ATPase). Muitos autofagossomos não significam morte por autofagia.],
  ),
  (
    "Necroptose (Tipo 3)",
    [TNF/Fas com caspase-8 BLOQUEADA: RIPK1 e RIPK3 se associam, fosforilam MLKL → MLKL oligomeriza, fura membrana plasmática → célula incha, lisa, libera DAMPs, inflama. Plano B inflamatório quando patógenos (CMV) inibem caspase-8 para impedir apoptose silenciosa.],
  ),
  (
    "Outras RCDs (visão de mapa)",
    [Piroptose: caspase-1 (inflamassoma) cliva gasdermina D (poros) + pró-IL-1β/IL-18 (citocinas). Ferroptose: peroxidação lipídica dependente de ferro, sem caspases (GPX4 inibida). NETose: exclusiva de neutrófilos, extrude redes de cromatina. Parthanatos: PARP-1 hiperativada, exaustão de NAD⁺/ATP.],
  ),
  (
    "p53 — guardião do genoma",
    [Em ~50% dos cânceres está mutado. Normalmente degradada por MDM2. Dano de DNA → ATM/ATR fosforilam p53 → estabiliza → ativa p21 (para G1, dá tempo para reparar) OU Puma/Noxa/Bax (apoptose se dano irrecuperável). Sem p53, célula com DNA quebrado segue dividindo e acumula mutações.],
  ),
  (
    "Clínica integradora",
    [Drogas pró-apoptóticas em oncologia: venetoclax (BH3-mimético) ataca leucemias dependentes de Bcl-2. Necrostatinas inibem necroptose em isquemia-reperfusão (infarto, AVC, transplante). Próxima geração: morte imunogênica deliberada em tumores. Morte celular virou alvo terapêutico direto.],
  ),
))
