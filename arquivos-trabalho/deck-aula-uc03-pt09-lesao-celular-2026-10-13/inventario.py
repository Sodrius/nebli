"""Inventário atômico de Lesão celular, necrose e apoptose (UC03 P1; Patologia; Ferraz da Silva), escrito antes da seleção (14/10).
Sequência = lâminas Ia (47); 21–47 idênticas à Ib (versão da pasta pessoal). Material lido: lâminas (visual/Ia, visual/Ib), transcrição Ia inteira
e trechos de ênfase da Ib, palavras-cruzadas com gabarito, monitoria P1 aula 1, provas pat-02 e Robbins cap. 1 (livros/robbins-cap1-lesao.txt).
"""
PREFIXO = "pt09"
AULA = "Lesão celular, necrose e apoptose (UC03 P1; Patologia; Ferraz da Silva)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"

SLIDES = [
 (1, "capa", "Capa (mecanismos de lesão)", []),
 (2, "conteudo", "Resposta celular: adaptação, lesão reversível, irreversível, necrose/apoptose", [("a1", "Desfechos: necrose e apoptose", "ak-dois-mecanismos")]),
 (3, "conteudo", "Exemplos: adaptação, lesão reversível, irreversível", [("a2", "Angina reversível", "ak-angina"), ("a3", "Infarto irreversível", "ak-iam"),
   ("a4", "Hipertensão/Alzheimer como adaptação", EXC + "adaptação é da aula 11")]),
 (4, "conteudo", "Miócito: hipertrofia × lesão", [("a5", "Hipertrofia", EXC + "adaptação, aula 11")]),
 (5, "conteudo", "Causas de lesão celular", [("a6", "Privação de oxigênio e demais causas", "a-hipoxia")]),
 (6, "conteudo", "Gráfico: função, bioquímica, ultraestrutura, microscopia, macroscopia", [("a7", "Sequência das alterações", "a-gross")]),
 (7, "conteudo", "Lesão reversível: edema, alteração gordurosa, alterações ultraestruturais", [("a8", "Edema celular", "ak-edema"), ("a9", "Bolhas e microvilosidades", "ak-bolhas"),
   ("a10", "Desligamento de polissomos", "ak-ribossomos"), ("a11", "Alterações nucleares", "ak-cromatina"), ("a12", "Alteração gordurosa", EXC + "esteatose é da aula 11 (acúmulos)")]),
 (8, "conteudo", "Critérios de irreversibilidade", [("a13", "Permeabilidade de membrana e destruição de DNA/proteínas", "b-criterios")]),
 (9, "conteudo", "Túbulos renais normal/reversível/irreversível", [("a14", "Perda do núcleo", "ak-nucleo")]),
 (10, "conteudo", "Microscopia eletrônica da lesão", [("a15", "Condensação da cromatina", "ak-cromatina")]),
 (11, "conteudo", "Aplicação clínica: mioglobina, CK-MB, troponina", [("a16", "Enzimas no sangue = irreversível", "ak-enzimas"), ("a17", "Transaminases/lipase", "b-transaminases")]),
 (12, "conteudo", "Mecanismos (esquema geral)", [("a18", "Quatro mecanismos", "c-mecanismos")]),
 (13, "conteudo", "Isquemia → ↓ATP → bomba, glicólise, ribossomos", [("a19", "Falta de ATP", "ak-atp"), ("a20", "Bombas", "ak-bombas"), ("a21", "Ácido lático e pH", "c-lactato")]),
 (14, "conteudo", "Radicais livres e antioxidantes", [("a22", "Redução incompleta", "c-reducao"), ("a23", "Superóxido", "ak-superoxido"), ("a24", "SOD", "ak-sod"),
   ("a25", "Catalase e glutationa peroxidase", ["ak-catalase", "ak-glutationa"]), ("a26", "Efeitos: peroxidação, oxidação", "ak-peroxidacao")]),
 (15, "conteudo", "Reperfusão (transplante)", [("a27", "Lesão de reperfusão", "ak-reperfusao")]),
 (16, "conteudo", "Mitocôndria: transição de permeabilidade, citocromo c", [("a28", "Necrose × apoptose pela mitocôndria", "c-mitocondria")]),
 (17, "conteudo", "Cálcio e enzimas", [("a29", "Fosfolipases, proteases, endonucleases, ATPases", "c-calcio")]),
 (18, "conteudo", "Diagrama: ATP, radicais, cálcio, mitocôndria", [("a30", "Mecanismos combinados", "c-mecanismos")]),
 (19, "conteudo", "Dano de membrana", [("a31", "Convergência no dano de membrana", ["c-calcio", "ak-peroxidacao"])]),
 (20, "conteudo", "Dobramento proteico", [("a32", "Chaperonas e proteínas mal dobradas", "c-chaperonas")]),
 (21, "capa", "Capa (necrose e apoptose)", []),
 (22, "conteudo", "Esquema da resposta celular (repetido)", [("a33", "Necrose e apoptose", "ak-dois-mecanismos")]),
 (23, "conteudo", "Necrose × apoptose: definições", [("a34", "Necrose patológica", "ak-nunca-fisiologica"), ("a35", "Apoptose sem inflamação", "ak-apoptose-sem-inflamacao")]),
 (24, "conteudo", "Necrose: esquema de isquemia e membrana (repetido)", [("a36", "Mecanismos", "c-mecanismos")]),
 (25, "conteudo", "Necrose: enzimas lisossômicas, inflamação, célula × arcabouço", [("a37", "Digestão por enzimas lisossômicas", "ak-lisossomos")]),
 (26, "conteudo", "Morfologia necrose × apoptose (esquema)", [("a38", "Morfologia comparada", ["ak-morfologia-apoptose", "ak-lisossomos"])]),
 (27, "conteudo", "Necrose: eosinofilia, picnose e cariorrexe", [("a39", "Eosinofilia", "ak-eosinofilia"), ("a40", "Alterações nucleares", "d-nucleo")]),
 (28, "conteudo", "Necrose coagulativa", [("a41", "Arcabouço mantido, fantasmas", "ak-coagulativa"), ("a42", "Circulação terminal/infarto", "ak-coagulativa-isquemia")]),
 (29, "conteudo", "Necrose liquefativa", [("a43", "Cérebro e abscesso", "ak-liquefativa")]),
 (30, "conteudo", "Necrose caseosa", [("a44", "Tuberculose", S(1791716427402))]),
 (31, "conteudo", "Caseosa: microscopia", [("a45", "Granuloma caseoso", EXC + "aula 47 Inflamação granulomatosa")]),
 (32, "conteudo", "Necrose gordurosa", [("a46", "Pancreatite", "ak-gordurosa"), ("a47", "Saponificação", "ak-saponificacao")]),
 (33, "conteudo", "Gordurosa: microscopia", [("a48", "Aspecto microscópico", "ak-saponificacao")]),
 (34, "conteudo", "Necrose fibrinoide", [("a49", "Vasos e imunocomplexos", "ak-fibrinoide")]),
 (35, "conteudo", "Necrose gangrenosa", [("a50", "Membros", "ak-gangrenosa")]),
 (36, "conteudo", "Apoptose: causas fisiológicas e patológicas", [("a51", "Fisiológicas", "e-fisiologica"), ("a52", "Atrofia patológica", "ak-atrofia")]),
 (37, "conteudo", "Apoptose: etapas (sinalização, controle, execução, remoção)", [("a53", "Execução por caspases", "ak-caspases")]),
 (38, "conteudo", "Vias intrínseca e extrínseca", [("a54", "BCL-2 e citocromo c", "ak-bcl2-citc"), ("a55", "Citocromo c → caspases", "ak-citc-caspases"), ("a56", "Fas/FasL", S(1791625429657))]),
 (39, "conteudo", "Morfologia e esquema geral", [("a57", "Contração, condensação, bolhas", "ak-morfologia-apoptose")]),
 (40, "conteudo", "Morfologia (esquema)", [("a58", "Corpos apoptóticos e fagocitose", "ak-corpos-apoptoticos")]),
 (41, "conteudo", "Imagens de apoptose", [("a59", "Corpo apoptótico", "ak-corpos-apoptoticos")]),
 (42, "conteudo", "Pró × antiapoptóticos", [("a60", "BAX/BAK", "ak-bax"), ("a61", "BCL-2/BCL-xL", "ak-bcl2-anti")]),
 (43, "conteudo", "Tabela necrose × apoptose", [("a62", "Diferenças", ["ak-apoptose-sem-inflamacao", "ak-morfologia-apoptose"])]),
 (44, "conteudo", "Correlações clínicas da apoptose", [("a63", "p53 e BAX/BAK", "ak-p53"), ("a64", "CTL", S(1791625429957)), ("a65", "Deficiente × excessiva", "e-doencas")]),
 (45, "conteudo", "Necroptose", [("a66", "Necroptose", EXC + "o professor disse para não entrar em detalhes")]),
 (46, "capa", "Ilustração humorística", []),
 (47, "capa", "Foto da Faculdade (encerramento)", []),
]
JUSTIFICATIVAS = {1: "capa", 21: "capa", 46: "ilustração sem conteúdo", 47: "encerramento"}
CAPITULO = [("Robbins cap. 1 (lesão e morte celular)", [
 ("l1", "Lesão reversível e irreversível", ["ak-edema", "b-criterios"]), ("l2", "Depleção de ATP", "ak-atp"), ("l3", "Dano mitocondrial", "c-mitocondria"),
 ("l4", "Influxo de cálcio", "c-calcio"), ("l5", "Estresse oxidativo", ["c-reducao", "ak-peroxidacao"]), ("l6", "Reperfusão", "ak-reperfusao"),
 ("l7", "Padrões de necrose", ["ak-coagulativa", "ak-liquefativa", "ak-gordurosa", "ak-fibrinoide", "ak-gangrenosa"]),
 ("l8", "Vias da apoptose", ["ak-bcl2-citc", S(1791625429657)])])]
EXERCICIOS = [
 ("Provas UC03 (pat-02)", [
   ("p1", "2024 P1 2.1: gangrena", "ak-gangrenosa"), ("p2", "2024 P1 2.8: isquemia, ATP, permeabilidade, fosfolipases, endonucleases", ["c-calcio", "b-criterios"]),
   ("p3", "2023 P1 1.6: necrose gordurosa", ["ak-gordurosa", "ak-saponificacao"]), ("p4", "2019 P1 2.3: isquemia → necrose", "a-hipoxia"),
   ("p5", "2018 P1 1.16: radicais livres e irreversibilidade", ["ak-peroxidacao", "ak-enzimas"]), ("p6", "2018 P3 1.4: AST/ALT", "b-transaminases"),
   ("p7", "2018 P3 3.4: infarto cerebral liquefativo", "ak-liquefativa"), ("p8", "2017 P1 1.3: atrofia por apoptose", "ak-atrofia"),
   ("p9", "2017 P1 2.3: troponina/CK-MB", "ak-enzimas"), ("p10", "2016 P1 2.8: necrose gordurosa", "ak-gordurosa"),
   ("p11", "2016 P1 3.7: Bcl-2 e afinamento cortical", "ak-bcl2-anti"), ("p12", "2015 P1 3.1: ácido lático e Na⁺", ["c-lactato", "ak-bombas"]),
   ("p13", "2015 P1 3.2: indicador de irreversibilidade", "ak-enzimas"), ("p14", "2015 P1 3.4: lesão de reperfusão", "ak-reperfusao"),
   ("p15", "2015 P1sub 1.2: edema + picnose", "d-nucleo")]),
 ("Palavras-cruzadas da aula", [("x1", "Ácido lático, pH", "c-lactato"), ("x2", "Mitocôndria como reservatório de cálcio", "c-calcio"),
   ("x3", "Glutationa", "ak-glutationa"), ("x4", "Fosfolipase", "c-calcio"), ("x5", "Transaminases", "b-transaminases"), ("x6", "Picnose", "d-nucleo"),
   ("x7", "Citocromo c", "c-mitocondria"), ("x8", "p53", "ak-p53"), ("x9", "Chaperonas", "c-chaperonas"), ("x10", "Fantasmas", "ak-coagulativa"),
   ("x11", "Reperfusão", "ak-reperfusao"), ("x12", "Via extrínseca", S(1791625429657)), ("x13", "Alzheimer", "e-doencas")]),
 ("Monitoria P1, aula 1", [("m1", "Lesão reversível/irreversível, mecanismos, tipos de necrose, apoptose", ["b-criterios", "c-mecanismos", "ak-coagulativa"])]),
]
