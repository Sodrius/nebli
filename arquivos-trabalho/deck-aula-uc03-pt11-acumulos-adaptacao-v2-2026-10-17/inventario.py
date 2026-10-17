"""Inventário atômico de Adaptação celular + Acúmulos celulares e teciduais (UC03 P1; Patologia; Luiz Fernando Ferraz da Silva),
escrito ANTES de escolher cards (17/10, pipeline v4). Sequência = 60 lâminas (fontes/slides.pdf = turma I adaptação 30 + II acúmulos 30
= pasta pessoal), vistas inteiras nesta sessão (io/g0..g4). Lido nesta sessão: transcrições I e II (116 pp.), provas pat-03, monitoria P1,
apostila guia de Patologia e UC3 (texto da corrida antiga), palavras-cruzadas e bibliografia da aula; Robbins cap. 1 (consulta).
Fronteira (MEMORY §3): esteatose, antracose, células de insuficiência cardíaca, Prussian blue, apoptose na atrofia e proteínas mal dobradas
já têm cópias NEBLI de 19 (correlação 2), 24 (ambiental), 23 (edema), 03 (diagnóstico), 09 (lesão celular) e GR2 → sh().
"""
PREFIXO = "pt11"
AULA = "Adaptação celular e acúmulos (UC03 P1; Patologia)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa (Adaptação celular)", []),
 (2, "conteudo", "Esquema lesão celular: adaptação × lesão reversível × irreversível", [("a1", "Esquema", EXC + "recapitula a aula 09 (lesão celular); a adaptação entra nas lâminas seguintes")]),
 (3, "conteudo", "Tecidos lábeis, estáveis e permanentes", [("a2", "Tipos de tecido pela capacidade de dividir", ["ak-labeis", "ak-estaveis", "ak-permanentes"])]),
 (4, "conteudo", "Cardiomiócito: adaptação (hipertrofia) × lesão × morte", [("a3", "Hipertrofia como adaptação", "ak-hipertrofia-def")]),
 (5, "conteudo", "Adaptação: novo equilíbrio preservando a viabilidade; hiperplasia, hipertrofia, atrofia, metaplasia", [
   ("a4", "Quatro adaptações", ["ak-hipertrofia-def", "ak-hiperplasia-def", "ak-atrofia-def", "ak-metaplasia-def"])]),
 (6, "conteudo", "Hipertrofia: células maiores, não mais células", [("a5", "Hipertrofia sintetiza proteínas e organelas", "ak-hipertrofia-genes")]),
 (7, "conteudo", "Hipertrofia fisiológica: demanda, hormônios (útero)", [("a6", "Útero gravídico", "ak-hipertrofia-genes")]),
 (8, "conteudo", "Hipertrofia patológica: miocárdio na hipertensão e estenose aórtica", [("a7", "Músculo cardíaco só hipertrofia", "ak-permanentes")]),
 (9, "conteudo", "Histologia: miocárdio normal × hipertrófico", [("a8", "Fibras mais grossas", "ak-hipertrofia-def")]),
 (10, "conteudo", "Desencadeantes: estiramento, α-adrenérgicos; limite da adaptação → dilatação e IC", [("a9", "Gatilhos da hipertrofia", "au-hipertrofia-gatilhos")]),
 (11, "conteudo", "Mecanismos: sensores, fatores de transcrição, genes fetais", [("a10", "Sinalização", "au-hipertrofia-gatilhos")]),
 (12, "conteudo", "Genética e mecanismos (Robbins)", [("a11", "Genes fetais", "au-hipertrofia-fetal")]),
 (13, "conteudo", "Re-expressão de genes embrionários: ANF, β-MHC; genes imediatos; proteínas constitutivas", [("a12", "ANF e β-miosina", "au-hipertrofia-fetal")]),
 (14, "conteudo", "Hipertrofia do músculo liso brônquico na asma", [("a13", "Remodelamento na asma", "sh-1791983686733")]),
 (15, "conteudo", "Hiperplasia fisiológica (hormonal, compensatória) e patológica", [("a14", "Proliferação controlada", "ak-hiperplasia-controlada")]),
 (16, "conteudo", "Regeneração hepática após hepatectomia parcial (Prometeu)", [("a15", "Fígado é tecido estável", "ak-estaveis")]),
 (17, "conteudo", "Hiperplasia fisiológica: mama, útero, medula; compensatória: fígado, pulmão; onde não ocorre", [("a16", "Hiperplasia", ["ak-hiperplasia-def", "ak-permanentes"])]),
 (18, "conteudo", "Hiperplasia patológica: endométrio, próstata, vírus, cicatriz; diferença com neoplasia", [
   ("a17", "Endométrio → risco de carcinoma", "ak-endometrio"), ("a18", "HPB sem risco de câncer", "ak-hpb"), ("a19", "Policlonal × monoclonal", "ak-policlonal")]),
 (19, "conteudo", "Imagens de hiperplasia (próstata)", [("a20", "HPB", "ak-hpb")]),
 (20, "conteudo", "Atrofia: perda de substância; células não mortas", [("a21", "Atrofia", "ak-atrofia-def")]),
 (21, "conteudo", "Atrofia fisiológica, patológica, local, difusa", [("a22", "Atrofia por menos células: apoptose", "sh-1792117383096")]),
 (22, "conteudo", "Causas de atrofia: desuso, denervação, isquemia, nutrição, hormônio, compressão", [("a23", "Causas", "au-atrofia-causas")]),
 (23, "conteudo", "Mecanismo: menos síntese, mais degradação (ubiquitina-proteassomo, autofagia)", [
   ("a24", "Degradação proteica", ["ak-ubiquitina-atrofia", "ak-autofagia-atrofia", "ak-proteassomo"])]),
 (24, "conteudo", "Degradação: corticoide, tireoide, TNF, IL-1; síntese: insulina", [("a25", "Equilíbrio síntese × degradação", ["sh-1791729316911", "ak-tireoide-degradacao", "sh-1791729320088"])]),
 (25, "conteudo", "Rim atrófico (isquemia)", [("a26", "Isquemia atrofia o rim", "au-atrofia-causas")]),
 (26, "conteudo", "Osteoporose como atrofia do osso", [("a27", "Desuso", "au-atrofia-causas")]),
 (27, "conteudo", "Hipoplasia: órgão que nunca se desenvolveu; aplasia", [("a28", "Hipoplasia, aplasia, agenesia", ["ak-hipoplasia", "ak-aplasia", "ak-aplasia-fa", "ak-agenesia"])]),
 (28, "conteudo", "Metaplasia: troca de tipo adulto por outro; células-tronco; fumo; transformação maligna", [
   ("a29", "Metaplasia", ["ak-metaplasia-irritante", "ak-metaplasia-tronco", "ak-metaplasia-reversivel", "ak-metaplasia-cancer"]),
   ("a30", "Barrett", ["ak-barrett", "sh-1790972065735"]), ("a31", "Vitamina A e metaplasia", ["ak-vit-a", "ak-vit-a-diferenciacao"])]),
 (29, "conteudo", "Metaplasia escamosa e mesenquimal (esquema Robbins)", [("a32", "Metaplasia óssea do músculo", "ak-miosite")]),
 (30, "conteudo", "I love Pathology", [("a33", "Humor", EXC + "imagem de humor")]),
 (31, "capa", "Capa (Acúmulos)", []),
 (32, "conteudo", "Acúmulos: constituinte normal, substância anormal, pigmento", [("a34", "Classificação", EXC + "classificação geral; cada tipo entra nas lâminas seguintes")]),
 (33, "conteudo", "Quatro mecanismos de acúmulo (Robbins)", [("a35", "Proteína mal dobrada", "sh-1792117372320")]),
 (34, "conteudo", "Toxicidade, localização, produzir × armazenar", [("a36", "Critérios", EXC + "critérios gerais sem fato próprio")]),
 (35, "conteudo", "Esteatose: fígado; desnutrição, alcoolismo, doenças metabólicas", [
   ("a37", "Esteatose macrovesicular, reversível", ["sh-1791022171477", "sh-1791022171668", "sh-1791022171771"])]),
 (36, "conteudo", "Metabolismo de lípides no hepatócito (esquema)", [("a38", "Exportação por VLDL", "ak-ccl4")]),
 (37, "conteudo", "Excesso de ácidos graxos: jejum, diabetes (lipase hormônio-sensível)", [("a39", "Diabetes: lipólise e AGL", "sh-1791054011671")]),
 (38, "conteudo", "Exportação requer apoproteína: inanição, tetracloreto de carbono", [("a40", "Menos apolipoproteína", ["ak-ccl4", "ak-kwashiorkor"])]),
 (39, "conteudo", "Álcool: desnutrição, lesão direta, acetato", [("a41", "NADH e acetaldeído", ["ak-nadh", "sh-1791022172501"])]),
 (40, "conteudo", "Fígado esteatótico: macro e micro", [("a42", "Fígado amarelo e gorduroso", "sh-1791022171668")]),
 (41, "conteudo", "Colesterol: aterosclerose, colesterolose, xantomas", [("a43", "Xantomas", "ak-xantoma"), ("a44", "Células espumosas", "ak-foam")]),
 (42, "conteudo", "Placa de ateroma", [("a45", "Ateroma", "ak-foam")]),
 (43, "conteudo", "Colesterolose da vesícula", [("a46", "Vesícula em morango", "au-colesterolose")]),
 (44, "conteudo", "Proteínas: glóbulos; mieloma; reabsorção tubular", [("a47", "Cadeias leves nos túbulos", "ak-bence-jones")]),
 (45, "conteudo", "Chaperonas e ubiquitina (Robbins)", [("a48", "Proteínas mal dobradas", "sh-1792117372320")]),
 (46, "conteudo", "Placa senil (amiloide) no córtex", [("a49", "Alzheimer: amiloide β", ["ak-alzheimer-ab", "ak-placa-neuritica"])]),
 (47, "conteudo", "Glicogênio: diabetes, glicogenoses", [("a50", "Glicogenose", "ak-von-gierke")]),
 (48, "conteudo", "Tabela de glicogenoses", [("a51", "Tabela", EXC + "o professor diz que não é preciso saber a tabela")]),
 (49, "conteudo", "Calcificação distrófica × metastática", [("a52", "Distrófica na necrose; metastática em tecido normal", ["ak-dist-necrose", "ak-meta-normal"])]),
 (50, "conteudo", "Distrófica: necrose caseosa, aterosclerose, valvas, tumores, cicatrizes", [
   ("a53", "Distrófica: localizada, cálcio normal", ["ak-dist-local", "ak-dist-normocalcemia", "ak-ateroma-calcificado"])]),
 (51, "conteudo", "Metastática: PTH, destruição óssea, vitamina D, insuficiência renal", [
   ("a54", "Metastática: hipercalcemia, difusa", ["ak-meta-hipercalcemia", "ak-meta-difusa", "ak-meta-calcemia", "ak-meta-locais", "ak-hpt"])]),
 (52, "conteudo", "Pigmentos exógenos: tatuagem, antracose", [("a55", "Antracose", ["sh-1791592721894", "ak-antracose-linfonodo"])]),
 (53, "conteudo", "Lipofuscina: envelhecimento, peroxidação lipídica, atrofia parda", [
   ("a56", "Lipofuscina", ["ak-lipofuscina", "ak-lipofuscina-lisossomo", "ak-lipofuscina-locais"]), ("a57", "Atrofia parda", "au-atrofia-parda")]),
 (54, "conteudo", "Melanina: tirosina → DOPA, tirosinase", [("a58", "Tirosinase", "ak-tirosinase")]),
 (55, "conteudo", "Hemossiderina: ferro da hemoglobina; ferritina; fígado, medula, baço", [("a59", "Hemossiderina e Perls", ["sh-1792150762535", "sh-1791142466364"])]),
 (56, "conteudo", "Hemorragias, hemólises, transfusões, absorção de ferro", [("a60", "Hemossiderinúria", "ak-hemossiderinuria")]),
 (57, "conteudo", "Hemocromatose: pele bronze, diabetes, arritmias", [("a61", "Hemocromatose", ["ak-hemocromatose", "ak-hemo-lipo"])]),
 (58, "conteudo", "Bilirrubina: sem ferro; icterícia", [("a62", "Bilirrubina e icterícia", ["ak-ictericia", "ak-protoporfirina"])]),
 (59, "conteudo", "Quadro de pigmentos (exógenos, endógenos, hemoglobinógenos)", [("a63", "Quadro", EXC + "síntese em diagrama; cada pigmento tem card nas lâminas 52–58")]),
 (60, "conteudo", "I love Pathology", [("a64", "Humor", EXC + "imagem de humor")]),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo"}
CAPITULO = [("Robbins cap. 1 (adaptações, acúmulos, calcificação) (confirma)", [
 ("l1", "Hipertrofia, hiperplasia, atrofia, metaplasia", ["ak-hipertrofia-def", "ak-hiperplasia-def", "ak-atrofia-def", "ak-metaplasia-def"]),
 ("l2", "Esteatose e colesterol", ["sh-1791022171477", "ak-foam"]), ("l3", "Calcificação", ["ak-dist-necrose", "ak-meta-normal"]),
 ("l4", "Pigmentos", ["ak-lipofuscina", "sh-1792150762535"])])]
EXERCICIOS = [
 ("Provas UC03 (índice pat-03)", [
   ("p1", "Mecanismo da esteatose: mais ácidos graxos, menos apolipoproteína, álcool (2024 P1 2.10, 2023 P1 2.5, 2016 P1 2.3)", ["sh-1791054011671", "ak-ccl4", "ak-nadh"]),
   ("p2", "Acúmulo na doença principal (2024 P1 1.5)", ["sh-1791022171477", "ak-hemocromatose"]),
   ("p3", "Mecanismo da atrofia: apoptose (2017 P1 1.3)", "sh-1792117383096"),
   ("p4", "Antracose no pulmão e linfonodos (2017 P1 2.2, 2016 P1 2.7)", ["sh-1791592721894", "ak-antracose-linfonodo"]),
   ("p5", "Bilirrubina na mucosa ocular; colesterol na vesícula (2016 P1 1.5)", ["ak-ictericia", "au-colesterolose"]),
   ("p6", "Lipofuscina nos neurônios (2016 P1 3.8)", "ak-lipofuscina"),
   ("p7", "Hipertrofia cardiáca na hipertensão: estiramento, α-adrenérgicos, genes fetais (2018 P1 1.4, 2016 P1 3.2)", ["au-hipertrofia-gatilhos", "au-hipertrofia-fetal"]),
   ("p8", "Acúmulos e adaptações num caso clínico (2019 P1 4.1; 2018 P1 1.17)", ["sh-1791022171477", "ak-hipertrofia-def"])]),
 ("Monitoria P1 e apostila guia de Patologia", [
   ("m1", "Adaptações e tecidos", ["ak-labeis", "ak-hipertrofia-def"]), ("m2", "Esteatose e pigmentos", ["sh-1791022171477", "ak-lipofuscina"]),
   ("m3", "Calcificação", ["ak-dist-necrose", "ak-meta-normal"])]),
 ("Palavras-cruzadas da turma (Adaptações e acúmulos)", [
   ("c1", "Denervação e desuso causam atrofia; atrofia do ex-atleta", "au-atrofia-causas"),
   ("c2", "Menos síntese e mais degradação de proteínas na atrofia", ["sh-1791729316911", "ak-ubiquitina-atrofia"]),
   ("c3", "Útero: hipertrofia hormonal; aumento do órgão pelo tamanho das células", ["ak-hipertrofia-genes", "ak-hipertrofia-def"]),
   ("c4", "Hiperplasia: mais células; hormonal; Prometeu", ["ak-hiperplasia-def", "ak-estaveis"]),
   ("c5", "Metabolismo do hepatócito e gotículas de gordura (esteatose)", ["sh-1791022171477", "ak-ccl4"]),
   ("c6", "Bilirrubina na icterícia; hemossiderina na politransfusão", ["ak-ictericia", "ak-hemossiderinuria", "sh-1792150762535"])]),
 ("Bibliografia da aula (Cacciapuoti 2011: mecanismos da hipertrofia ventricular na hipertensão)", [
   ("b1", "Angiotensina II, endotelina, noradrenalina e estiramento disparam a hipertrofia", "au-hipertrofia-gatilhos")]),
]
