"""Inventário atômico de Mecanismos de virulência e patogenicidade bacterianos, escrito a partir do material de base lido inteiro:
lâminas 2026 da Profa. Carla Taddei (visual/folha-NN, fontes/slides.txt, 41 lâminas), material docente da turma (Profa. Elisabete
Vicente, Patogenicidade Bacteriana I–III, 2025, e as duas transcrições), monitoria P2 aulas 6 e 8, apostila de veteranos (só o sumário
do capítulo foi extraído), provas (índice micro-07-patogenicidade-bacteriana) e Trabulsi 6ª ed., caps. 17.1 (da própria Profa. Taddei),
17.2, 17.3, 18 e 19 (livros/trabulsi-cap17-19-virulencia.txt).
Cada ideia aponta para o card que a pergunta (chave do spec, lista, "sh-<nid>" ou "EXC: motivo" só em lâmina). Menção no verso não conta.
"""
PREFIXO = "mb35"
AULA = "Mecanismos de virulência e patogenicidade bacterianos (UC03 P2; Profa. Carla Taddei, 2026)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa (Taddei, relação patógeno-hospedeiro)", []),
 (2, "conteudo", "Inflamação e infecção", [
   ("inflamacao", "Inflamação: resposta protetora mediada por fatores do plasma e células; reparo e fibrose",
    EXC + "definição de inflamação é alvo das aulas de Inflamação (IM37/IM38), que têm deck próprio"),
   ("infeccao", "Infecção: contaminação, penetração e multiplicação de um patógeno", ["infeccao-def", "colonizacao-infeccao"])]),
 (3, "conteudo", "Defesas dos tecidos e do sangue", [
   ("defesas", "Defesas do hospedeiro: barreiras, muco/cílios, proteínas que sequestram ferro", ["transferrina", "ciliostase"])]),
 (4, "conteudo", "Figura sem texto (defesas)", [("figura-defesas", "Esquema de defesas do hospedeiro", ["transferrina"])]),
 (5, "conteudo", "Patogenicidade × virulência", [
   ("pat-vir", "Patogenicidade = capacidade de causar infecção; virulência = medida quantitativa", ["patogenicidade-virulencia", "ld50", "ld50-curva"]),
   ("virulentas-oportunistas", "Bactérias virulentas × oportunistas", ["oportunista", "endogena"]),
   ("equilibrio", "Estado de equilíbrio; estabelecimento da infecção; portas de entrada", ["ecoli-patogenica", "koch"])]),
 (6, "conteudo", "Hooper 2009: simbionte × patógeno", [("hooper", "O mesmo nicho pode ter simbionte ou patógeno conforme a relação", "nutrientes-patogeno")]),
 (7, "conteudo", "Fases do processo infeccioso", [
   ("incubacao", "Período de incubação", "fases-infeccao"),
   ("prodromica", "Fase prodrômica: sintomas inespecíficos", "prodromica"),
   ("aguda-convalescenca", "Doença aguda e convalescência", "fases-infeccao"),
   ("iceberg", "Infecção sem doença clínica (base do iceberg)", ["iceberg", "periodo-latente"])]),
 (8, "conteudo", "Relação parasito-hospedeiro (figura)", [("relacao", "Relação parasito-hospedeiro", "nutrientes-patogeno")]),
 (9, "conteudo", "Mecanismos de virulência: transmissão", [("portas", "Portas de entrada: mucosas, pele, via parenteral; sítios mais frequentes", "portas-entrada")]),
 (10, "conteudo", "Mecanismos microbianos de patogenicidade (esquema)", [
   ("portas-10", "Portas de entrada", "portas-entrada"),
   ("etapas", "Número de micróbios, aderência, penetração/evasão, lesão", "etapas-infeccao"),
   ("lesao", "Lesão direta, toxinas, hipersensibilidade", ["toxinas-def", "febre-reumatica"])]),
 (11, "conteudo", "Antígenos e fatores de virulência (perguntas)", [("perguntas", "O que são antígenos e fatores de virulência", "fatores-virulencia")]),
 (12, "conteudo", "Fatores de virulência", [
   ("fv-def", "Estruturas e metabólitos para adesão, invasão, escape e toxinas", "fatores-virulencia"),
   ("exo-endo", "Exotoxinas e endotoxinas", ["exotoxinas-proteinas", "endotoxina-membrana"])]),
 (13, "conteudo", "Antígenos bacterianos I", [("ag-1", "Membrana, proteínas de membrana externa, polissacarídeos, LPS, cápsula", "antigenos")]),
 (14, "conteudo", "Antígenos bacterianos II", [("ag-2", "Flagelos, fímbrias, proteínas secretadas, toxinas, pili", ["antigenos", "pili-flagelo"])]),
 (15, "conteudo", "Fatores de aderência", [
   ("adesinas-def", "Adesinas ligam receptores específicos; glico/lipoproteínas; pili, fímbrias", "adesinas"),
   ("por-que", "Aderência impede a expulsão (cílios, secreções, peristaltismo)", "adesao-expulsao")]),
 (16, "conteudo", "Adesão mediada por adesinas", [
   ("receptores", "Receptores: glico/lipoproteínas e matriz extracelular", "adesinas"),
   ("pili-tipo-iv", "Pili tipo IV (E. coli), flagelos, adesinas não fimbriais", ["adesinas-tipos", "epec-adesao"]),
   ("exemplos-pili", "Exemplos de pili: Neisseria, S. pyogenes, UPEC", ["pili-neisseria", "strepto-adesao", "upec-pili"])]),
 (17, "conteudo", "Dano celular (figura EPEC)", [("dano", "Adesão íntima e lesão de microvilosidades", ["lesao-ae", "epec-tir"])]),
 (18, "conteudo", "Sistema de secreção tipo III", [
   ("t3ss-def", "Libera proteínas dentro da célula hospedeira", "t3ss"),
   ("t3ss-flagelo", ">20 genes, semelhantes aos do flagelo", "t3ss-flagelo"),
   ("t3ss-especies", "Variações em Salmonella (2 anéis) e Shigella (bulbo e pescoço)", ["t3ss-salmonella", "t3ss-shigella", "salmonella-spi1"]),
   ("espa", "Seringa de EspA forma poros na membrana do hospedeiro", "t3ss")]),
 (19, "conteudo", "Invasão e disseminação", [
   ("invasao", "Invasão de células e disseminação", ["invasao-disenteria", "intracelular-facultativo", "invasina-yersinia"]),
   ("eiec", "EIEC semelhante à Shigella", "eiec-shigella")]),
 (20, "conteudo", "Shigella: célula M, macrófago, actina", [
   ("celula-m", "Entrada por células M e escape do macrófago", "shigella-celulaM"),
   ("actina", "Motilidade intracelular por polimerização de actina; disseminação célula a célula", "shigella-actina")]),
 (21, "conteudo", "Adesinas não fimbriais", [
   ("autotransportadoras", "Autotransportadoras, proteínas de membrana externa, LPS", ["adesinas-tipos", "opa"]),
   ("fha", "FHA de Bordetella pertussis", "adesinas-tipos"),
   ("mscramm", "MSCRAMM de Gram-positivas", ["mscramm", "teicoico-adesao"])]),
 (22, "conteudo", "Figura T3SS (Donnenberg)", [("fig-t3ss", "Esquema da seringa", "t3ss")]),
 (23, "conteudo", "Sistemas de secreção", [
   ("sete", "Sete sistemas de secreção", "secrecao-sete"),
   ("t2ss", "Tipo II: 12–14 proteínas, passagem pelo periplasma", "t2ss")]),
 (24, "conteudo", "Exotoxinas × endotoxinas", [
   ("toxina-def", "Substâncias solúveis que alteram o metabolismo do hospedeiro", "toxinas-def"),
   ("exo", "Exotoxinas: excretadas por células vivas, polipeptídeos, G+ e G−, instáveis, antigênicas, muito tóxicas",
    ["exotoxinas-proteinas", "exotoxina-propriedades", "exotoxina-tipos", "ab-toxina", "superantigeno"]),
   ("endo", "Endotoxinas: parede de G−, liberadas na lise, LPS, estáveis, pouco imunogênicas",
    ["endotoxina-membrana", "endotoxina-morte", "endotoxina-lps", "endotoxina-propriedades"])]),
 (25, "conteudo", "Exemplos de exotoxinas", [
   ("eritrogenica", "Eritrogênica do S. pyogenes", "eritrogenica"),
   ("colerica", "Enterotoxina colérica: diarreia intensa", ["colera", "etec-lt", "etec-toxinas", "etec-viajante"]),
   ("estafilococica", "Enterotoxina estafilocócica", "estafilo-enterotoxina"),
   ("ehec", "Toxina Shiga-like da EHEC (material da turma)", ["ehec-disenteria", "ehec-vero", "ehec-stx"])]),
 (26, "conteudo", "Endotoxinas", [
   ("lps-efeitos", "LPS: febre, leucopenia, hipoglicemia, hipotensão", ["lps-efeitos", "lps-cid", "sh-1791163032499", "lps-estrutura"]),
   ("pg", "Peptidoglicano de G+: efeitos semelhantes, menos potentes", "peptidoglicano-endotoxina")]),
 (27, "conteudo", "Características das exotoxinas", [
   ("sem-febre", "Em geral não produzem febre", "exotoxina-propriedades"),
   ("plasmideos", "Controladas por genes extracromossômicos", ["genes-toxinas", "genetica-virulencia"])]),
 (28, "conteudo", "Características das endotoxinas", [
   ("toxoide", "Não viram toxoide", "toxoide"),
   ("receptores-febre", "Sem receptores específicos; produzem febre; genes cromossômicos", ["endotoxina-propriedades", "genes-toxinas"])]),
 (29, "conteudo", "LPS e choque", [
   ("especies-lps", "Enterobactérias, Neisseria, Bordetella", "lps-gram"),
   ("citocinas", "Citocinas → colapso cardiovascular, choque", ["lps-citocinas", "sh-1791014719025"]),
   ("pg-29", "Peptidoglicano com efeito semelhante", "peptidoglicano-endotoxina")]),
 (30, "conteudo", "Enzimas", [
   ("degradam", "Lecitinase, colagenase, coagulase, hialuronidase, estreptoquinase, citolisinas",
    ["enzimas-tecido", "hialuronidase", "estreptoquinase", "coagulase", "leucocidina", "perfringens-lecitinase"]),
   ("iga1", "IgA1 protease de N. gonorrhoeae, N. meningitidis, H. influenzae, S. pneumoniae", ["iga-protease", "iga-especies"])]),
 (31, "conteudo", "Escape do sistema imune", [
   ("iga-31", "IgA1 protease", "iga-protease"),
   ("componentes", "Adquirir componentes do hospedeiro na superfície", ["camuflagem", "mimetismo"]),
   ("c5a", "C5a peptidase", "c5a-peptidase"),
   ("variacao", "Variação antigênica; Salmonella", ["variacao-antigenica", "salmonella-fase"])]),
 (32, "conteudo", "Fatores antifagocíticos: cápsula", [
   ("capsula", "Repulsão eletroquímica; reduz ativação do complemento", ["sh-1791163040622", "capsula-repulsao"]),
   ("capsula-exemplos", "Pneumococo, meningococo (material da turma)", ["pneumococo-capsula", "capsula-neisseria"]),
   ("outros-antifago", "Proteína A, proteína M (material da turma)", ["proteina-a", "proteina-a-mecanismo", "proteina-m"])]),
 (33, "conteudo", "Captação de ferro", [
   ("ferro", "Sideróforos captam ferro do hospedeiro", ["sh-1791647814244", "sh-1791647814120", "sh-1791647814370", "siderofos-tipos"])]),
 (34, "conteudo", "Biofilmes", [
   ("biofilme", "Microcolônias em exopolissacarídeo, superfícies bióticas ou abióticas, fonte de infecção",
    ["biofilme-def", "sh-1791576680215", "mutans-placa"]),
   ("protecao", "Protegidas do sistema imune e de antibióticos", "biofilme-protecao")]),
 (35, "conteudo", "Figura de biofilme", [("fig-biofilme", "Etapas de formação do biofilme", "biofilme-def")]),
 (36, "conteudo", "Quorum sensing I", [
   ("qs-def", "Comunicação dependente de densidade populacional", "quorum-def"),
   ("ahl", "Acil-homosserina lactonas em Gram-negativas", "quorum-gramneg")]),
 (37, "conteudo", "Quorum sensing II", [
   ("peptideos", "Peptídeos em Gram-positivas", "quorum-grampos"),
   ("ai2", "AI-2 em Gram-positivas e negativas", "quorum-ai2")]),
 (38, "conteudo", "Quorum sensing III", [("ai3", "AI-3: comunicação bactéria-hospedeiro", "quorum-ai3")]),
 (39, "conteudo", "Figura WJCC 2015", [("fig-wjcc", "Figura de revisão sem texto próprio", EXC + "figura de artigo sem legenda; o conteúdo de quorum sensing está nas lâminas 36–38")]),
 (40, "conteudo", "Tabela: fator de virulência × função", [
   ("pili-40", "Pili: aderência às mucosas", "adesinas"),
   ("actina-40", "Rearranjo de actina: células não fagocíticas fagocitam", "induz-fagocitose"),
   ("celulas-m-40", "Invasão de células M", "celulas-m"),
   ("motilidade", "Motilidade e quimiotaxia", "motilidade"),
   ("siga", "sIgA proteases", "iga-protease"),
   ("sideroforos-40", "Sideróforos", "sh-1791647814244"),
   ("capsula-40", "Cápsulas", "capsula-repulsao"),
   ("ag-o", "Alterações no antígeno O: sem MAC, resistência ao soro", "antigeno-o"),
   ("c5a-40", "C5a peptidase", "c5a-peptidase"),
   ("toxicas", "Proteínas tóxicas matam fagócitos e reduzem o burst oxidativo", "proteinas-toxicas"),
   ("variacao-40", "Variação nos antígenos de superfície", "variacao-antigenica")]),
 (41, "capa", "Encerramento", []),
]

JUSTIFICATIVAS = {}

CAPITULO = [("Trabulsi 6ª ed., caps. 17.1 (Taddei & Martinez), 17.2, 17.3, 18 e 19 (pdf pp. 175–208)", [
   ("tb-etapas", "Instalação da doença em contato, invasão e disseminação", "etapas-infeccao"),
   ("tb-pat-vir", "Patogenicidade = causar dano; virulência = capacidade relativa, dependente do hospedeiro", "patogenicidade-virulencia"),
   ("tb-aderencia", "Aderência é pré-requisito e impede a expulsão mecânica", "adesao-expulsao"),
   ("tb-fimbrias-afimbriais", "Adesinas fimbriais (mais comuns em Gram-negativas) e afimbriais", "adesinas-tipos"),
   ("tb-mscramm", "MSCRAMMs ligam colágeno, fibronectina e ácido hialurônico", "mscramm"),
   ("tb-biofilme", "Biofilme começa pela adesão e se mantém por exopolissacarídeos", ["biofilme-def", "biofilme-protecao"]),
   ("tb-intracelular", "Invasores intracelulares obrigatórios e facultativos", "intracelular-facultativo"),
   ("tb-entrada", "Entrada por invasina de alta afinidade (Yersinia) ou por rearranjo do citoesqueleto (Salmonella, Shigella)",
    ["invasina-yersinia", "induz-fagocitose"]),
   ("tb-ferro", "Ferro livre baixíssimo; transferrina e lactoferrina; sideróforos", ["transferrina", "sh-1791647814244", "siderofos-tipos"]),
   ("tb-fur", "Fur regula a captação de ferro", "sh-1791647814370"),
   ("tb-exo-endo", "Quadro exotoxina × endotoxina (fonte, estabilidade, toxoide, febre)",
    ["exotoxina-propriedades", "endotoxina-propriedades", "toxoide"]),
   ("tb-lps", "Lipídeo A, cerne e cadeia O; LPS → citocinas e choque", ["lps-estrutura", "lps-citocinas"]),
   ("tb-superantigeno", "Superantígenos ativam células T de forma inespecífica (TSST, pirogênica)", "superantigeno"),
   ("tb-tipos-exotoxina", "Exotoxinas ativas na superfície, formadoras de poro e A–B", ["exotoxina-tipos", "ab-toxina"]),
   ("tb-evasinas", "Evasinas: cápsula, proteína A, IgA protease, variação antigênica", ["capsula-repulsao", "proteina-a-mecanismo", "iga-protease", "variacao-antigenica"]),
   ("tb-genetica", "Genes de virulência em plasmídeos, fagos, transposons e ilhas de patogenicidade",
    ["genetica-virulencia", "salmonella-spi1", "genes-toxinas"]),
   ("tb-secrecao", "Sistemas de secreção tipos I–VII; tipo III em Salmonella e Shigella", ["secrecao-sete", "t3ss", "t2ss"])])]

EXERCICIOS = [
 ("Material docente da turma: Patogenicidade Bacteriana I–III (Profa. Vicente, 2025) e transcrições I e II", [
   ("tu-koch", "Postulados de Koch", "koch"),
   ("tu-def", "Patógeno, doença, hospedeiro, infecção", "infeccao-def"),
   ("tu-ld50", "LD50 estima a virulência", ["ld50", "ld50-curva"]),
   ("tu-etapas", "Adesão, colonização e disseminação", "etapas-infeccao"),
   ("tu-pili", "Fímbrias/pili × flagelos", "pili-flagelo"),
   ("tu-teicoico", "Ácidos teicoico e lipoteicoico de S. pyogenes na adesão", ["teicoico-adesao", "strepto-adesao"]),
   ("tu-proteina-m", "Proteínas M, F e T do S. pyogenes", ["proteina-m", "strepto-adesao"]),
   ("tu-epec", "EPEC: BFP plasmidial (fraca) e intimina/Tir cromossomais (firme); diarreia infantil",
    ["epec-sem-toxina", "epec-adesao", "epec-tir", "lesao-ae", "epec-crianca"]),
   ("tu-neisseria", "N. gonorrhoeae: pili e variação antigênica; Opa", ["pili-neisseria", "opa"]),
   ("tu-capsula", "Cápsula de N. meningitidis e pneumococo liso × rugoso", ["capsula-neisseria", "pneumococo-capsula"]),
   ("tu-biofilme", "Biofilme e camada limosa de S. mutans na cárie", ["biofilme-def", "mutans-placa"]),
   ("tu-multiplicacao", "Sideróforos e tropismo na multiplicação", "sh-1791647814244"),
   ("tu-etec", "ETEC: LT/ST plasmidiais, cAMP/cGMP, diarreia do viajante", ["etec-lt", "etec-toxinas", "etec-viajante"]),
   ("tu-ehec", "EHEC: adesão íntima, toxina Shiga, disenteria", ["ehec-disenteria", "ehec-vero", "ehec-stx"]),
   ("tu-tetano", "Toxina tetânica: bloqueia glicina, paralisia espástica, tétano neonatal",
    ["tetano-toxina", "tetano-espastica", "tetano-snare", "tetano-glicina", "tetano-formas"]),
   ("tu-botulismo", "Toxina botulínica: bloqueia acetilcolina, paralisia flácida; uso clínico", ["botulinica", "botox"]),
   ("tu-perfringens", "C. perfringens: toxina alfa (lecitinase), gangrena gasosa, câmara hiperbárica",
    ["perfringens-alfa", "perfringens-lecitinase", "gangrena-gasosa"]),
   ("tu-cdiff", "C. difficile: toxinas A e B após antibioticoterapia; colite pseudomembranosa", ["cdiff-toxinas", "cdiff-toxinab", "cdiff-colite"]),
   ("tu-difteria", "Difteria: pseudomembrana e toxina", "difteria-toxina"),
   ("tu-eritrogenica", "Toxinas eritrogênicas", "eritrogenica"),
   ("tu-enzimas", "Enzimas: obtenção de nutrientes e degradação de tecidos", ["enzimas-tecido", "hialuronidase", "estreptoquinase", "coagulase", "leucocidina"]),
   ("tu-invasao", "Invasão de células e disenteria bacilar (Shigella, EIEC)", ["invasao-disenteria", "eiec-shigella", "shigella-actina"]),
   ("tu-hpylori", "Vacúolos e urease de H. pylori", ["hpylori-vaca", "sh-1790980015534"]),
   ("tu-proteina-a", "Proteína A liga Fc da IgG", ["proteina-a", "proteina-a-mecanismo"]),
   ("tu-iga", "Proteases de IgA", "iga-protease"),
   ("tu-salmonella", "Variação de fase H1/H2 da Salmonella", "salmonella-fase"),
   ("tu-tb", "M. tuberculosis: sobrevive no macrófago, bloqueia fusão fagossomo-lisossomo; formas e tratamento",
    ["tb-fagossomo", "tb-manlam", "tb-formas", "tb-tratamento"]),
   ("tu-epidemiologia", "Períodos de incubação, latência e transmissibilidade", "periodo-latente"),
   ("tu-patotipos", "Patotipos de E. coli e ITU por E. coli", ["eaec-daec", "ecoli-itu", "pielonefrite"]),
   ("tu-strepto", "S. pyogenes: febre reumática e GNPE", ["febre-reumatica", "gnpe-proteina-m"])]),
 ("Monitoria P2, aulas 6 e 8 (Patogenicidade bacteriana I e II)", [
   ("mo-colonizacao", "Colonização × infecção; primária × oportunista", ["colonizacao-infeccao", "oportunista"]),
   ("mo-pat-vir", "Patogenicidade qualitativa × virulência quantitativa", "patogenicidade-virulencia"),
   ("mo-endogena", "Infecção endógena × exógena", "endogena"),
   ("mo-iceberg", "Iceberg da infecção; latência", ["iceberg", "periodo-latente"]),
   ("mo-portas", "Portas de entrada", "portas-entrada"),
   ("mo-defesas", "Defesas de mucosa: muco, cílios, ciliostase", "ciliostase"),
   ("mo-adesao", "Adesinas fimbriais e não fimbriais; fímbrias mais comuns em G−", ["adesinas", "adesinas-tipos"]),
   ("mo-invasao", "Extracelular, intracelular obrigatória ou facultativa; indução de fagocitose",
    ["intracelular-facultativo", "induz-fagocitose"]),
   ("mo-fagossomo", "Sobrevivência no fagossomo (inibição da fusão)", "tb-fagossomo"),
   ("mo-enzimas", "Coagulase, fibrinolisina, hialuronidase, colagenase", ["coagulase", "estreptoquinase", "hialuronidase", "enzimas-tecido"]),
   ("mo-evasinas", "Cápsula, proteína A, proteases, variação antigênica, mimetismo molecular",
    ["capsula-repulsao", "proteina-a-mecanismo", "iga-protease", "variacao-antigenica", "mimetismo"]),
   ("mo-lps", "LPS: antígeno O, lipídeo A, cerne", ["lps-estrutura", "sh-1791163032499"]),
   ("mo-exo-tipos", "Exotoxinas A–B, formadoras de poro, superantígenos", ["exotoxina-tipos", "ab-toxina", "superantigeno"]),
   ("mo-tetano-botulismo", "Tétano espástico × botulismo flácido; cólera via cAMP", ["tetano-espastica", "botulinica", "colera"]),
   ("mo-genetica", "Genes de virulência por transferência horizontal", "genetica-virulencia"),
   ("mo-epec", "EPEC: fímbria plasmidial, intimina e Tir", ["epec-adesao", "epec-tir"]),
   ("mo-teicoico", "Ácidos teicoicos na adesão de G+", "teicoico-adesao"),
   ("mo-etec", "ETEC: LT e ST", ["etec-lt", "etec-toxinas"]),
   ("mo-ld50", "LD50 e distância até a LD100", ["ld50", "ld50-curva"]),
   ("mo-ferro", "Sideróforos", "sh-1791647814244")]),
 ("Provas UC03 (índice micro-07-patogenicidade-bacteriana)", [
   ("pr-2025-pielo", "2025 P2 1.3: E. coli na pielonefrite (fímbrias P, ascensão)", ["ecoli-itu", "pielonefrite", "upec-pili"]),
   ("pr-2025-pyogenes", "2025 P2 2.3: superantígenos do S. pyogenes × adesão local da E. coli", ["superantigeno", "hialuronidase"]),
   ("pr-2024-aureus", "2024 P2 1.11: fatores do S. aureus na pneumonia (adesinas de matriz, proteína A, coagulase)",
    ["mscramm", "proteina-a-mecanismo", "coagulase"]),
   ("pr-2023-endogena", "2023 P2: S. aureus da microbiota translocado; E. coli nas vias biliares", "endogena"),
   ("pr-2019-variacao", "2019 P2 2.5: variação antigênica e perda de eficácia vacinal", "variacao-antigenica"),
   ("pr-2018-lps", "2018: LPS de Gram-negativa e febre", ["lps-efeitos", "endotoxina-membrana"]),
   ("pr-2018-meningococo", "2018 P2: LPS, pili e cápsula de N. meningitidis", ["capsula-neisseria", "pili-neisseria"]),
   ("pr-2017-patotipos", "2017: mecanismos de E. coli (EPEC adesão, ETEC toxina)", ["epec-adesao", "etec-lt"]),
   ("pr-2015-pneumococo", "2015 P1: cápsula e IgA protease do pneumococo", ["pneumococo-capsula", "iga-especies"])]),
 ("Apostila de veteranos (Microbiologia), aula 6: só o sumário foi extraído", [
   ("ve-capitulos", "Conceitos, etapas, acesso, adesão, invasão, evasão, danos teciduais", "etapas-infeccao")]),
]
