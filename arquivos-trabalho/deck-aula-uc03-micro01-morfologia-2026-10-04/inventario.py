"""Inventário atômico da Morfologia e estrutura das bactérias (45 lâminas do PDF I; PDF II e III são versões da mesma aula, com 4
lâminas a mais no II: Chlamydia/Mycoplasma por Giemsa, PAMPs e as respostas da lista). Escrito em 09/10 (F-20261009-CLAUDE-02) antes
de selecionar os cards, a partir de: fontes/slides.pdf.txt, fontes/slides-II.pdf.txt, apostila de veteranos aula 1 (pp. 13–16 de
../deck-aula-uc03-mb12-fungos-2026-10-09/fontes/veterano-microbio.txt), monitoria P1 aula 1 (fontes/monitoria/micro-P1.txt pp. 40–41),
Trabulsi cap. 2 (fontes/trabulsi-cap2-pp7-23.txt) e provas UC03 (fontes/provas-originais.txt). Para python3 -m nebli.inventario.
"""
PREFIXO = "micro01"
AULA = "Morfologia e estrutura das bactérias (UC03, Microbiologia, aula 1; Profa. Elisabete Vicente)"
EXC = "EXC: "
JUSTIFICATIVAS = {"capa": "capa, bibliografia ou abertura de bloco, sem conteúdo"}

SLIDES = [
 (1, "capa", "Capa e roteiro", []),
 (2, "capa", "Bibliografia recomendada", []),
 (3, "conteudo", "Surgimento da vida e três domínios", [("dominios", "Bactéria, Arqueia, Eucarioto; LUCA; bactérias há ~3,8 bilhões de anos", "tres-dominios")]),
 (4, "conteudo", "Árvore de Woese por rRNA", [
   ("woese-rrna", "Woese 1977: três domínios pela sequência do rRNA", "tres-dominios"),
   ("arqueias", "Arqueias como domínio próprio", "arqueias")]),
 (5, "conteudo", "Bactérias do bem e ruins", [("simbiose", "Maioria mutualista/comensal; minoria patogênica", "microbiota")]),
 (6, "conteudo", "Por que estudar morfologia", [("diagnostico", "Morfologia é a 1ª etapa do diagnóstico; depois bioquímica, antibiograma, PCR", "gram-conduta")]),
 (7, "conteudo", "Morfologia macro e microscópica", [("colonia", "Colônia em meio sólido (~10^8 células)", "colonia")]),
 (8, "conteudo", "Morfologia macroscópica", [
   ("colonia-celulas", "Cada colônia tem ~10^8 células", "colonia"),
   ("meio-diferencial", "Meios diferenciais: cores (lac+/lac-) e hemólise", "meio-diferencial")]),
 (9, "conteudo", "Dimensões: vírus, bactérias, fungos", [
   ("tamanho", "Bactérias ~1–5 µm, vistas a 1000× com óleo de imersão", "tamanho"),
   ("virus", "Vírus (~200 nm) só ao microscópio eletrônico", "virus-me")]),
 (10, "conteudo", "Morfologia microscópica", [
   ("formas", "Cocos, bacilos, espiralados", "formas"),
   ("arranjos-cocos", "Diplococos, estreptococos, estafilococos", ["diplococos", "estreptococos", "estafilococos"]),
   ("estreptobacilos", "Estreptobacilos", "estreptobacilos"),
   ("vibriao", "Vibriões em vírgula (V. cholerae)", "vibriao"),
   ("espiroquetas-espirilos", "Espiroquetas flexíveis × espirilos rígidos", "espiroqueta")]),
 (11, "conteudo", "Estruturas essenciais e não essenciais", [("essenciais", "Essenciais × não essenciais", "essenciais")]),
 (12, "conteudo", "Membrana citoplasmática", [
   ("composicao", "Proteínas 60% em bicamada fosfolipídica 40%", "membrana-composicao"),
   ("sem-esterol", "Sem esteróis (apostila, Trabulsi)", "membrana-sem-esterol")]),
 (13, "conteudo", "Funções da membrana", [
   ("transporte", "Transporte: difusão facilitada, ativo, translocação de grupo", "translocacao-grupo"),
   ("energia", "Transporte de elétrons e fosforilação oxidativa", "cadeia-respiratoria"),
   ("biossintese", "Biossíntese de lipídios, peptidoglicano, teicoicos, LPS; duplicação do DNA", "membrana-sintese"),
   ("secrecao", "Excreção de enzimas hidrolíticas", "membrana-sintese"),
   ("taxia", "Taxia: quimiotaxia e fototaxia", "taxia")]),
 (14, "conteudo", "Gram-positivas e Gram-negativas", [("gram-1884", "Gram (1884) separa pela parede", "gram-parede")]),
 (15, "conteudo", "Importância do Gram", [("dois-grupos", "Gram divide a maioria das bactérias em dois grupos", "gram-parede")]),
 (16, "conteudo", "Coloração de Gram", [
   ("etapas", "Cristal violeta, lugol, álcool, fucsina", "gram-alcool"),
   ("retencao", "Gram-positiva retém o cristal violeta", "gram-cristal"),
   ("cores", "Gram-positiva roxa; Gram-negativa vermelha", ["gram-purple", "gram-pink"])]),
 (17, "conteudo", "Parede celular: funções e estrutura", [
   ("funcoes", "Forma, pressão osmótica, divisão", "parede-osmotica"),
   ("percentual", "Mureína 15–60% em Gram+ × ~5% em Gram-", "pg-percentual")]),
 (18, "conteudo", "Peptidoglicano (mureína)", [
   ("nag-nam", "NAG e NAM", "pg-nagnam"),
   ("tetrapeptideo", "Tetrapeptídeos ligados ao NAM; D-Ala", ["pg-peptideo", "dala"])]),
 (19, "conteudo", "Parede Gram-positiva", [("espessa", "Peptidoglicano espesso", "gp-thick")]),
 (20, "conteudo", "Ácido teicoico (ribitol)", [("teicoico", "Ácidos teicoicos na parede Gram-positiva", "lta-gram")]),
 (21, "conteudo", "Propriedades dos ácidos teicoicos", [
   ("cations", "Facilitam entrada e saída de cátions", "teicoico-funcoes"),
   ("autolisinas", "Regulam autolisinas", "teicoico-autolisina"),
   ("fagos", "Receptores de bacteriófagos", "teicoico-funcoes"),
   ("adesinas", "Adesinas ao epitélio", "teicoico-funcoes"),
   ("antigenos", "Antígenos para identificação sorológica", "lta")]),
 (22, "conteudo", "Parede Gram-negativa", [("estrutura", "Parede fina com membrana externa", "gn-outer")]),
 (23, "conteudo", "LPS e periplasma", [
   ("lps", "LPS: lipídio A (endotoxina) e polissacarídeo O (antígeno O)", ["lps-outer", "lps-parts", "lipid-a", "o-antigen"]),
   ("periplasma", "Espaço periplasmático entre as membranas", "periplasma")]),
 (24, "conteudo", "Composição da parede Gram-negativa", [("composicao", "Poucas camadas de peptidoglicano, periplasma, membrana externa com LPS", ["gn-outer", "lps-outer"])]),
 (25, "conteudo", "Esquema Gram+ × Gram-", [("esquema", "Comparação esquemática das paredes", ["gp-thick", "gn-outer"])]),
 (26, "conteudo", "Comparação Gram+ × Gram-", [("comparacao", "Diferenças estruturais entre as paredes", "gram-parede")]),
 (27, "conteudo", "Patógenos Gram+ e Gram-", [
   ("exemplos-positivos", "Gram+: Bacillus, Staphylococcus, Streptococcus, Enterococcus, Clostridium, Listeria", "cocos-positivos"),
   ("exemplos-negativos", "Gram-: E. coli, Salmonella, Shigella, Vibrio, Neisseria, Legionella", "bacilos-negativos")]),
 (28, "conteudo", "Bactérias que não coram ao Gram", [("nao-coram", "Algumas bactérias não se coram pelo Gram", "intracelulares-gram")]),
 (29, "conteudo", "Micobactérias e Ziehl-Neelsen", [
   ("acido-micolico", "Parede rica em ácidos micólicos", "micobacteria-zn"),
   ("zn", "ZN: fucsina fenicada, álcool-ácido, azul de metileno; BAAR vermelho", "zn-fucsina")]),
 (30, "conteudo", "Espiroquetas", [
   ("finas", "Estrutura Gram-negativa, finas demais para o Gram", "campo-escuro"),
   ("metodos", "Prata, campo escuro, imunofluorescência", ["campo-escuro", "prata-treponema"])]),
 (31, "conteudo", "Chlamydia trachomatis", [("chlamydia", "Intracelular obrigatória e pequena: Giemsa e efeito citopático", "chlamydia-giemsa")]),
 (32, "conteudo", "Mycoplasma e conclusão", [
   ("mycoplasma", "Sem parede, 0,3 µm, diagnóstico por PCR", "mycoplasma"),
   ("conclusao", "Gram dá coco/bacilo Gram+/Gram-; ZN para micobactéria", ["gram-parede", "micobacteria-zn"])]),
 (33, "capa", "Abertura: demais estruturas", []),
 (34, "conteudo", "Material genético", [
   ("nucleoide", "Nucleoide: DNA cromossomal", ["nucleoide", "dna-circular"]),
   ("plasmidio", "DNA plasmidial", "plasmid")]),
 (35, "conteudo", "Ribossomos", [("ribossomos", "Ribossomos procariotos × eucariotos", "ribossomo-70s")]),
 (36, "conteudo", "Flagelos", [
   ("funcao", "Movimento (taxia), 200–500 µm/s", "flagelo"),
   ("partes", "Estrutura basal, gancho, filamento de flagelina", ["flagelo-partes", "flagellar-basal"])]),
 (37, "conteudo", "Localização dos flagelos", [("posicao", "Polar, monotríquio, anfitríquio, lofotríquio, peritríquio", "flagelo-posicao")]),
 (38, "conteudo", "Pili ou fímbrias", [
   ("sexual", "Pili sexual", "conjugacao"),
   ("fagos", "Sítios aceptores de vírus", "pili-fago"),
   ("adesao", "Adesão a células de mamíferos", ["pili-funcoes", "fimbriae-uti"])]),
 (39, "conteudo", "Flagelo × pili", [
   ("comparacao", "Flagelo motilidade; fímbria adesão, conjugação, receptor de fago", ["flagelo", "pili-funcoes"]),
   ("conjugacao", "Plasmídeo transferido por conjugação", "conjugacao")]),
 (40, "conteudo", "Esporos: formação", [
   ("indutores", "Falta de nutrientes, secagem, temperatura, agentes químicos", "esporo-indutores"),
   ("posicao", "Terminais, subterminais, centrais", "esporo-posicao"),
   ("dormencia", "Forma dormente e resistente que germina anos depois", ["esporo-dormente", "esporo-resistente"])]),
 (41, "conteudo", "Esporos: gêneros", [
   ("generos", "Bacillus e Clostridium, Gram-positivos, no solo", "esporo-generos"),
   ("wirtz", "Coloração de Wirtz: esporos verdes, bactérias vermelhas", "wirtz")]),
 (42, "conteudo", "Grânulos citoplasmáticos", [("granulos", "Fósforo, enxofre, PHB como reserva", "granulos")]),
 (43, "conteudo", "Substâncias poliméricas extracelulares", [
   ("capsula", "Cápsula: estrutura definida", "capsula-definida"),
   ("mucosa", "Camada mucosa", "glicocalice"),
   ("camada-s", "Camada S", "camada-s")]),
 (44, "conteudo", "Glicocálice, biofilme e cápsulas", [
   ("biofilme", "Glicocálice forma biofilme em pele, válvulas, cateteres", ["biofilme-epidermidis", "biofilme-resistencia"]),
   ("exemplos-biofilme", "P. aeruginosa na fibrose cística; S. epidermidis e viridans na endocardite; S. mutans na cárie", ["biofilme-pseudomonas", "mutans-carie", "biofilme-epidermidis"]),
   ("capsula-exemplos", "Cápsula em Gram- (E. coli, N. meningitidis, Klebsiella, H. influenzae) e Gram+ (S. pneumoniae)", ["pneumococo-capsula", "ecoli-capsula"]),
   ("capsula-fagocitose", "Cápsula dificulta a fagocitose (monitoria)", "capsule-phago")]),
 (45, "conteudo", "Lista de questões", [("questoes", "Questões 1–14 (respondidas no PDF II)", ["gram-parede", "lps-outer", "lta-gram", "periplasma", "mycoplasma"])]),
]

CAPITULO = [
 ("Trabulsi cap. 2", [
   ("forma-arranjo", "Cocos, bacilos, espirilos; diplo/estrepto/estafilococos; vibrião, espirilo, espiroqueta", ["formas", "estreptococos", "espiroqueta"]),
   ("gram-tecnica", "Técnica de Gram: cristal violeta, lugol, álcool, fucsina", "gram-alcool"),
   ("membrana", "Membrana 60/40, sem esteróis; transporte; cadeia respiratória", ["membrana-sem-esterol", "translocacao-grupo", "cadeia-respiratoria"]),
   ("parede", "Pressão osmótica 15–20 atm; peptidoglicano NAG/NAM e tetrapeptídeos", ["parede-osmotica", "pg-nagnam", "pg-peptideo"]),
   ("teicoicos", "Ácidos teicoicos: cátions, autolisinas, fagos, adesão, antígenos", ["teicoico-autolisina", "teicoico-funcoes"]),
   ("membrana-externa", "LPS, porinas, barreira a penicilina e lisozima; periplasma com β-lactamase", ["porinas", "membrana-externa-barreira", "periplasma-enzimas"]),
   ("spe", "Cápsula × camada mucosa; camada S; biofilme e resistência a biocidas", ["capsula-definida", "glicocalice", "camada-s", "biofilme-resistencia"]),
   ("flagelos-fimbrias", "Flagelo (basal, gancho, flagelina); fímbrias de adesão e sexual", ["flagelo-partes", "pili-funcoes"]),
   ("granulos", "Grânulos de reserva sem elevar a pressão osmótica", "granulos"),
   ("esporos", "Esporogênese, ácido dipicolínico, resistência ao calor", ["spore-core", "spore-cortex", "spore-boiling"])]),
]

EXERCICIOS = [
 ("Lista de questões da aula (respostas no PDF II, pp. 48–49)", [
   ("q1", "Importância: morfologia é a 1ª etapa da identificação", "gram-conduta"),
   ("q2", "Estrutura que separa em dois grupos: a parede", "gram-parede"),
   ("q3", "Gram ajuda; ZN para micobactérias; prata para espiraladas", ["gram-alcool", "zn-fucsina", "prata-treponema"]),
   ("q4", "Gram+ peptidoglicano espesso × Gram- fino com membrana externa", ["gp-thick", "gn-outer"]),
   ("q5", "LPS na membrana externa de Gram-negativas", "lps-outer"),
   ("q6", "Ácidos teicoicos em Gram-positivas", "lta-gram"),
   ("q7", "Periplasma em Gram-negativas", "periplasma"),
   ("q8", "Nem todas coram ao Gram: micobactéria, espiraladas, Mycoplasma", ["intracelulares-gram", "mycoplasma", "campo-escuro"]),
   ("q9", "Outras colorações: ZN, Wirtz, Giemsa, prata", ["zn-fucsina", "wirtz", "chlamydia-giemsa"]),
   ("q10", "Flagelo motilidade × pili adesão/conjugação/fagos", ["flagelo", "pili-funcoes"]),
   ("q11", "Grânulos de reserva", "granulos"),
   ("q12", "Esporos só em alguns gêneros", "esporo-generos"),
   ("q13", "Cromossomo em todas; plasmídeo só em alguns isolados", ["essenciais", "plasmid"]),
   ("q14", "Cápsula rígida e definida × camada mucosa menos definida", ["capsula-definida", "glicocalice"])]),
 ("Apostila de veteranos, aula 1", [
   ("arqueias", "Arqueobactérias: procariotos, ambientes extremos, metanogênicas", "arqueias"),
   ("penicilina", "Penicilina afeta a montagem da parede; mais efeito em Gram+; mata ao dividir", "penicilina-divisao"),
   ("membrana", "Membrana sem esteróis; citocromos como a mitocôndria", ["membrana-sem-esterol", "cadeia-respiratoria"]),
   ("lps-endotoxina", "LPS = endotoxina, febre", "lipid-a"),
   ("porinas", "Membrana externa barreira; porinas", ["porinas", "membrana-externa-barreira"]),
   ("biofilme", "Biofilme dá vantagem e sobrevida", "biofilme-resistencia"),
   ("endosporos", "Endósporos em Clostridium e Bacillus quando faltam água/nutrientes", ["esporo-generos", "esporo-indutores"])]),
 ("Monitoria P1, aula 1", [
   ("nao-patogenicas", "99% das bactérias não são prejudiciais", "microbiota"),
   ("microscopia", "Vírus só ao ME; bactérias e fungos ao MO", ["virus-me", "tamanho"]),
   ("essenciais", "Membrana e ribossomo essenciais; parede, flagelo, pili, esporo, cápsula não", "essenciais"),
   ("granulos", "Grânulos polimerizados para não elevar a pressão osmótica", "granulos")]),
 ("Provas UC03", [
   ("bacteria-fungo", "2017 P2 2.5: bactéria × fungo (tamanho, núcleo, 70S, parede)", ["tamanho", "ribossomo-70s", "nucleoide"]),
   ("gram-conduta", "P2 1.5: bacterioscopia pelo Gram orienta a antibioticoterapia inicial", "gram-conduta"),
   ("ecoli-virulencia", "E. coli: fímbrias (ITU), LPS, cápsula com antígeno K", ["fimbriae-uti", "lipid-a", "ecoli-capsula"]),
   ("treponema", "2023: Treponema com estrutura Gram-negativa, flagelos", "campo-escuro")]),
]
