"""Inventário atômico de Lesão celular, necrose e apoptose (UC03 P1; Patologia; Prof. Luiz F. Ferraz da Silva), escrito ANTES da seleção
(15/10, pipeline AnKing-primeiro, F-20261015-CLAUDE-06/07). Sequência = lâminas Ia (47): 1–20 mecanismos de lesão; 21–47 necrose e apoptose
(= Ib da pasta pessoal). Lido inteiro nesta corrida: lâminas (visual/Ia), transcrições Ia e Ib, apostila guia de Patologia (Aula 2),
monitoria P1 (aula 1), UC3.pdf (Mecanismos de lesão), provas pat-02 (51 subquestões), palavras-cruzadas com gabarito; Robbins cap. 1 só confirma.
Cada ideia aponta para a chave do card (spec), "sh-<nid>" ou "EXC: motivo".
"""
PREFIXO = "pt09"
AULA = "Lesão celular, necrose e apoptose (UC03 P1; Patologia; Ferraz da Silva)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"

SLIDES = [
 (1, "capa", "Capa (mecanismos de lesão)", []),
 (2, "conteudo", "Resposta celular: homeostase → adaptação / lesão reversível → irreversível → necrose ou apoptose", [
   ("a1", "Os dois desfechos de morte: necrose e apoptose", "ak-dois-mecanismos"),
   ("a2", "Lesão irreversível termina em morte celular", "ak-fim-irreversivel"),
   ("a3", "Estímulo leve e transitório → reversível; intenso e progressivo → irreversível", "au-reversivel-irreversivel")]),
 (3, "conteudo", "Exemplos: adaptação (HAS, Alzheimer), reversível (hipóxia, AIT), irreversível (hepatite aguda, IAM)", [
   ("a4", "Angina = lesão reversível", "ak-angina"), ("a5", "Infarto = lesão irreversível (necrose)", "ak-iam"),
   ("a6", "Hepatite aguda viral = lesão irreversível do hepatócito", "ak-hepatite-viral"),
   ("a7", "HAS e Alzheimer como adaptação", EXC + "adaptação é a aula 11 (Acúmulos e adaptação)")]),
 (4, "conteudo", "Miócito: hipertrofia × lesão reversível × morte", [("a8", "Hipertrofia", EXC + "adaptação, aula 11")]),
 (5, "conteudo", "Causas de lesão celular (7)", [
   ("a9", "Lista das causas", "au-causas"), ("a10", "Hipóxia = menor entrega de O2", "ak-hipoxia"),
   ("a11", "Isquemia = perda de fluxo", "ak-isquemia"), ("a12", "CO/anemia reduzem o conteúdo de O2", "ak-co")]),
 (6, "conteudo", "Gráfico: função → bioquímica → ultraestrutura → microscopia → macroscopia", [
   ("a14", "Ordem das alterações no tempo", "au-sequencia"), ("a15", "Isquemia miocárdica total > 30 min = irreversível", "ak-30min"),
   ("a16", "Células mais sensíveis (neurônio) passam à irreversibilidade antes", "au-sequencia")]),
 (7, "conteudo", "Lesão reversível: edema celular, alteração gordurosa, alterações ultraestruturais", [
   ("a17", "Edema celular é o marco da reversível", "ak-edema"), ("a18", "Bolhas e perda de microvilosidades", "ak-bolhas"),
   ("a19", "Desligamento de ribossomos/polissomos", "ak-ribossomos"), ("a20", "Condensação da cromatina", "ak-cromatina"),
   ("a21", "Alteração gordurosa (esteatose)", EXC + "esteatose é da aula 11 (acúmulos); o professor remete a ela")]),
 (8, "conteudo", "Critérios de irreversibilidade", [
   ("a22", "Marco da irreversível: dano de membrana", "ak-marco-irreversivel"),
   ("a23", "Dois critérios: perda da permeabilidade de membrana e destruição excessiva de DNA/proteínas", "au-criterios")]),
 (9, "conteudo", "Túbulo renal: normal, reversível, irreversível", [("a24", "Perda do núcleo = morte celular", "ak-perda-nucleo")]),
 (10, "conteudo", "Microscopia eletrônica da lesão", [("a25", "Cromatina condensada; bolhas", ["ak-cromatina", "ak-bolhas"])]),
 (11, "conteudo", "Aplicação clínica: mioglobina, CK-MB, troponina", [
   ("a26", "Enzima intracelular no sangue = lesão irreversível", "ak-enzimas-soro"), ("a27", "Troponina I", "ak-troponina"),
   ("a28", "Amilase/lipase na pancreatite", "ak-amilase-lipase")]),
 (12, "conteudo", "Mecanismos (esquema geral: mitocôndria, Ca²⁺, membrana, proteínas/DNA)", [("a29", "Alvos/mecanismos da lesão", "au-mecanismos")]),
 (13, "conteudo", "Isquemia → ↓ATP → bomba, glicólise, ribossomos", [
   ("a30", "Falta de ATP", "ak-atp"), ("a31", "Bombas Na⁺/K⁺ e Ca²⁺ param", "ak-bombas"),
   ("a32", "Glicólise anaeróbia → ácido lático → ↓pH → condensação da cromatina", "au-lactato")]),
 (14, "conteudo", "Radicais livres: redução incompleta, Fenton, antioxidantes, efeitos", [
   ("a33", "Redução incompleta do O2 (1, 2, 3 elétrons)", ["ak-superoxido", "ak-peroxido", "ak-hidroxila"]),
   ("a34", "Hidroxila é o mais lesivo", "ak-hidroxila-pior"), ("a35", "Fenton (metais)", "ak-fenton"), ("a36", "Radiação ionizante", "ak-radiacao"),
   ("a37", "Efeitos: peroxidação lipídica, oxidação de proteínas e DNA", "ak-efeitos-radicais"),
   ("a38", "SOD", "ak-sod"), ("a39", "Catalase e glutationa peroxidase", "ak-catalase-gpx"), ("a40", "Antioxidantes", "ak-antioxidantes")]),
 (15, "conteudo", "Reperfusão (transplante renal: queda de função)", [("a41", "Lesão de reperfusão por radicais livres", ["ak-reperfusao-trombolise", "ak-reperfusao-radicais"])]),
 (16, "conteudo", "Mitocôndria: transição de permeabilidade → necrose; citocromo c → apoptose", [("a42", "Dano mitocondrial leva a necrose ou apoptose", "ak-citc-iniciadoras")]),
 (17, "conteudo", "Cálcio e enzimas", [("a43", "Entrada de Ca²⁺", "ak-calcio-entrada"), ("a44", "Ca²⁺ ativa fosfolipases, proteases, endonucleases, ATPases", "au-calcio-enzimas")]),
 (18, "conteudo", "Diagrama: ATP, radicais, cálcio, mitocôndria", [("a45", "Mecanismos combinados", "au-mecanismos")]),
 (19, "conteudo", "Dano de membrana", [("a46", "Membrana lisossômica: hidrolases no citosol", "ak-lisossomo"), ("a47", "Convergência no dano de membrana", ["au-calcio-enzimas", "ak-efeitos-radicais"])]),
 (20, "conteudo", "Dobramento proteico: chaperonas; Creutzfeldt-Jakob", [("a48", "Proteína mal dobrada não corrigida → apoptose", "au-mal-dobradas")]),
 (21, "capa", "Capa (necrose e apoptose)", []),
 (22, "conteudo", "Esquema da resposta celular (repetido da lâmina 2)", [("a49", "Necrose e apoptose", "ak-dois-mecanismos")]),
 (23, "conteudo", "Necrose × apoptose: definições", [
   ("a50", "Necrose: patológica, inflamatória, grupos de células", ["ak-necrose-patologica", "ak-necrose-inflamatoria", "ak-necrose-grupos"]),
   ("a51", "Apoptose: programada, dependente de ATP, sem inflamação, células isoladas", ["ak-apoptose-programada", "ak-apoptose-sem-inflamacao", "ak-apoptose-isoladas"])]),
 (24, "conteudo", "Necrose: esquema de isquemia e membrana (repetido)", [("a52", "Mecanismos", "au-mecanismos")]),
 (25, "conteudo", "Necrose: enzimas lisossômicas, recrutamento inflamatório, célula × arcabouço", [("a53", "Digestão por enzimas lisossômicas e inflamação", ["ak-lisossomo", "ak-necrose-inflamatoria"])]),
 (26, "conteudo", "Morfologia necrose × apoptose (esquema)", [("a54", "Figuras de mielina (reversível)", "ak-mielina"), ("a55", "Vacuolização mitocondrial (irreversível)", "ak-vacuolizacao")]),
 (27, "conteudo", "Necrose: eosinofilia, picnose, cariorrexe", [
   ("a56", "Eosinofilia", "ak-eosina"), ("a57", "Picnose", "ak-picnose"), ("a58", "Cariorrexe", "ak-cariorrexe"), ("a59", "Cariólise", "ak-cariolise")]),
 (28, "conteudo", "Necrose coagulativa", [
   ("a60", "Os seis tipos de necrose", "au-tipos-necrose"), ("a61", "Arquitetura preservada, núcleo some (fantasmas)", "ak-coag-arquitetura"),
   ("a62", "Enzimas proteolíticas desnaturadas", "ak-coag-enzimas"), ("a63", "Infarto isquêmico de qualquer órgão, menos o cérebro", "ak-coag-infarto"),
   ("a64", "Circulação terminal: infarto pálido", "ak-infarto-palido")]),
 (29, "conteudo", "Necrose liquefativa", [
   ("a65", "Lise enzimática", "ak-liq-lise"), ("a66", "Cérebro e abscessos", "ak-liq-cerebro-abscesso"),
   ("a67", "Cérebro: arcabouço é das próprias células (glia)", "ak-liq-cerebro-abscesso"), ("a68", "Neutrófilos no abscesso", "ak-neutrofilos"),
   ("a69", "Cavitação tardia no cérebro", "ak-cavitacao"), ("a70", "Abscesso pulmonar (Klebsiella)", "ak-klebsiella")]),
 (30, "conteudo", "Necrose caseosa", [("a71", "Tuberculose e fungos", "ak-caseosa-tb"), ("a72", "Aspecto de queijo", S(1791716427402)),
   ("a73", "Células fragmentadas e debris com halo inflamatório", "ak-caseosa-debris")]),
 (31, "conteudo", "Caseosa: microscopia (granuloma)", [("a74", "Granuloma caseoso", EXC + "aula 47 Inflamação granulomatosa")]),
 (32, "conteudo", "Necrose gordurosa", [("a75", "Pancreatite aguda ou trauma", "ak-gordurosa-causas"), ("a76", "Gordura peripancreática", "ak-gordurosa-peripancreatica"),
   ("a77", "Saponificação", "ak-saponificacao"), ("a78", "Aspecto branco-calcário", "ak-gordurosa-calcario")]),
 (33, "conteudo", "Gordurosa: microscopia", [("a79", "Saponificação azul-escura no HE", "ak-saponificacao-he")]),
 (34, "conteudo", "Necrose fibrinoide", [("a80", "Parede de vasos", "ak-fibrinoide-vasos"), ("a81", "HAS maligna e vasculite", "ak-fibrinoide-has"),
   ("a82", "Rosa brilhante", "ak-fibrinoide-rosa"), ("a83", "Vasculite com imunocomplexos na parede", "ak-fibrinoide-has")]),
 (35, "conteudo", "Necrose gangrenosa", [("a84", "Membros e TGI, isquemia crônica", "ak-gangrena-local"), ("a85", "Seca (mumificada)", "ak-gangrena-seca"),
   ("a86", "Úmida (infecção)", "ak-gangrena-umida"), ("a87", "Reconhecer gangrena", "ak-gangrena-imagem")]),
 (36, "conteudo", "Apoptose: causas fisiológicas e patológicas", [("a88", "Fisiológicas × patológicas", "au-apoptose-causas"), ("a89", "Atrofia por apoptose", "ak-atrofia"),
   ("a90", "Células infectadas mortas por CD8", S(1791625429957))]),
 (37, "conteudo", "Apoptose: etapas (sinalização, controle, execução, remoção)", [("a91", "Execução por caspases", "ak-caspases")]),
 (38, "conteudo", "Vias intrínseca e extrínseca", [
   ("a92", "Endonucleases e proteases", ["ak-endonucleases", "ak-proteases"]), ("a93", "Inativação do BCL-2", "ak-bcl2-inativacao"),
   ("a94", "BCL-2 mantém a membrana externa impermeável ao citocromo c", "ak-bcl2-citc"), ("a95", "Sensores BH3 (dano ao DNA, radiação, falta de fator) inativam o BCL-2", "ak-bcl2-inativacao"),
   ("a96", "Citocromo c ativa caspases iniciadoras", "ak-citc-iniciadoras"), ("a97", "Caspases iniciadoras 9 (intrínseca) e 8 (extrínseca); executoras", "au-caspases"),
   ("a98", "Fas/FasL e TNF", S(1791625429657)), ("a99", "Via do CD8", "ak-cd8")]),
 (39, "conteudo", "Morfologia: contração, condensação, bolhas, corpos apoptóticos, fagocitose", [("a100", "Morfologia", "ak-apoptose-morfologia")]),
 (40, "conteudo", "Morfologia (esquema)", [("a101", "Corpos apoptóticos fagocitados por macrófagos", "ak-corpos-apoptoticos")]),
 (41, "conteudo", "Imagens de apoptose", [("a102", "Citoplasma eosinofílico", "ak-apoptose-eosinofilica"), ("a103", "Núcleo basofílico", "ak-apoptose-basofilico")]),
 (42, "conteudo", "Pró × antiapoptóticos", [("a104", "BAX/BAK pró", "ak-bax-pro"), ("a105", "BCL-2/BCL-xL anti", "ak-bcl2-anti"), ("a106", "p53 ativa BAX/BAK", "ak-p53-bax"),
   ("a107", "IAP e FLIP", EXC + "nomes da tabela sem mecanismo ensinado; linha no Extra do card antiapoptótico (caso de fronteira)")]),
 (43, "conteudo", "Tabela necrose × apoptose", [("a108", "Tamanho, núcleo, membrana, conteúdo, inflamação, papel", "au-tabela-necrose-apoptose")]),
 (44, "conteudo", "Correlações clínicas da apoptose", [("a109", "p53: apoptose se o reparo falha", "ak-p53-reparo"),
   ("a110", "Apoptose deficiente (autoimunidade, câncer) × excessiva (neurodegeneração)", "au-apoptose-doencas")]),
 (45, "conteudo", "Necroptose", [("a111", "Necroptose: necrose programada quando a caspase-8 falha", "au-necroptose")]),
 (46, "capa", "Ilustração humorística", []),
 (47, "capa", "Foto da Faculdade (encerramento)", []),
]
JUSTIFICATIVAS = {1: "capa", 21: "capa", 46: "ilustração sem conteúdo", 47: "encerramento"}
CAPITULO = [("Robbins cap. 1 (lesão e morte celular; confirma, não origina)", [
 ("l1", "Lesão reversível e irreversível", ["ak-edema", "au-criterios"]), ("l2", "Depleção de ATP", "ak-atp"), ("l3", "Dano mitocondrial", "ak-citc-iniciadoras"),
 ("l4", "Influxo de cálcio", "au-calcio-enzimas"), ("l5", "Estresse oxidativo", ["ak-superoxido", "ak-efeitos-radicais"]), ("l6", "Reperfusão", "ak-reperfusao-radicais"),
 ("l7", "Padrões de necrose", "au-tipos-necrose"), ("l8", "Vias da apoptose", ["ak-bcl2-citc", S(1791625429657)])])]
EXERCICIOS = [
 ("Provas UC03 (pat-02)", [
   ("p1", "2024 P1 2.1: gangrena", ["ak-gangrena-local", "ak-gangrena-imagem"]),
   ("p2", "2024 P1 2.8: isquemia, ATP, permeabilidade, fosfolipases, endonucleases", ["au-calcio-enzimas", "au-criterios"]),
   ("p3", "2023 P1 1.5–1.6: amilase, necrose gordurosa, saponificação", ["ak-amilase-lipase", "ak-gordurosa-peripancreatica", "ak-saponificacao"]),
   ("p4", "2019 P1 2.3: isquemia → necrose no AVC", ["ak-isquemia", "ak-liq-cerebro-abscesso"]),
   ("p5", "2018 P1 1.16: radicais livres, peroxidação, irreversibilidade", ["ak-efeitos-radicais", "ak-enzimas-soro"]),
   ("p6", "2018 P3 1.4: AST/ALT = lesão irreversível do hepatócito", ["ak-enzimas-soro", "ak-hepatite-viral"]),
   ("p7", "2018 P3 3.4 e 2016 P2 2.11: infarto cerebral liquefativo; arcabouço do SNC", "ak-liq-cerebro-abscesso"),
   ("p8", "2017 P1 1.3 e 2018 P1 2.2: atrofia por apoptose", "ak-atrofia"),
   ("p9", "2017 P1 2.3: troponina/CK-MB", ["ak-troponina", "ak-enzimas-soro"]),
   ("p10", "2017 P1 3.5: Klebsiella → abscesso liquefativo", "ak-klebsiella"),
   ("p11", "2016 P1 2.8: necrose gordurosa", "ak-gordurosa-peripancreatica"),
   ("p12", "2016 P1 3.7: Bcl-2, citocromo c, via intrínseca na atrofia", ["ak-bcl2-citc", "ak-bcl2-inativacao"]),
   ("p13", "2016 P2 1.6: CD8 induz apoptose na infecção viral", S(1791625429957)),
   ("p14", "2016 P3 2.3: p53 estimula BAX", "ak-p53-bax"),
   ("p15", "2015 P1 3.1: ácido lático, pH e influxo de Na⁺/Ca²⁺", ["au-lactato", "ak-bombas"]),
   ("p16", "2015 P1 3.2: indicador de irreversibilidade = liberação de enzimas", "ak-enzimas-soro"),
   ("p17", "2015 P1 3.4: lesão de reperfusão após t-PA", "ak-reperfusao-trombolise"),
   ("p18", "2015 P1sub 1.2: edema + picnose + ausência de núcleo", ["ak-picnose", "ak-perda-nucleo"]),
   ("p19", "2015 P1sub 4: diferenças necrose × apoptose", "au-tabela-necrose-apoptose")]),
 ("Palavras-cruzadas da aula (gabarito)", [
   ("x1", "Ácido lático; redução do pH", "au-lactato"), ("x2", "Mitocôndria como reservatório de Ca²⁺", "au-calcio-enzimas"), ("x3", "Eosinofilia", "ak-eosina"),
   ("x4", "Inflamação ausente na apoptose", "ak-apoptose-sem-inflamacao"), ("x5", "Alterações ultraestruturais precoces", "au-sequencia"),
   ("x6", "Permeabilidade", "au-criterios"), ("x7", "Edema celular", "ak-edema"), ("x8", "Corpúsculos apoptóticos", "ak-corpos-apoptoticos"),
   ("x9", "Mutação → apoptose", "ak-p53-reparo"), ("x10", "Transaminases", "ak-enzimas-soro"), ("x11", "Peroxidação", "ak-efeitos-radicais"),
   ("x12", "Isquemia", "ak-isquemia"), ("x13", "Reperfusão (transplante)", "ak-reperfusao-radicais"), ("x14", "Alzheimer (apoptose excessiva)", "au-apoptose-doencas"),
   ("x15", "Fisiológica (involução)", "au-apoptose-causas"), ("x16", "Picnose", "ak-picnose"), ("x17", "Fantasmas celulares", "ak-coag-arquitetura"),
   ("x18", "Desprendimento dos ribossomos", "ak-ribossomos"), ("x19", "Glutationa", "ak-antioxidantes"), ("x20", "Intensidade do estímulo", "au-reversivel-irreversivel"),
   ("x21", "Fosfolipases", "au-calcio-enzimas"), ("x22", "Coração 1 h após infarto: nenhuma alteração macroscópica", "au-sequencia"),
   ("x23", "Via extrínseca (Fas/FasL)", S(1791625429657)), ("x24", "Redução incompleta do O2", "ak-superoxido"), ("x25", "Caseosa", "ak-caseosa-tb"),
   ("x26", "Chaperonas", "au-mal-dobradas"), ("x27", "Caspases", "ak-caspases"), ("x28", "Fagocitose", "ak-corpos-apoptoticos"),
   ("x29", "Citocromo c", "ak-citc-iniciadoras"), ("x30", "Liquefativa", "ak-liq-cerebro-abscesso"), ("x31", "ATP e bomba de Na⁺", "ak-bombas"),
   ("x32", "Caspases 8, 9, 10 = iniciadoras", "au-caspases"), ("x33", "Sensor pró-apoptótico ativado por radiação", "ak-bcl2-inativacao"),
   ("x34", "Hepatite B: hepatócitos mortos por apoptose", S(1791625429957)), ("x35", "Autofagia", EXC + "citada só no Extra do AnKing; não é alvo das lâminas")]),
 ("Monitoria P1, aula 1", [("m1", "Reversível/irreversível, mecanismos, tipos de necrose, apoptose", ["au-criterios", "au-mecanismos", "au-tipos-necrose", "au-apoptose-causas"])]),
 ("Apostila guia de Patologia, Aula 2", [("ap1", "Isquemia × hipóxia; cianeto; fígado glicolítico", "ak-isquemia"),
   ("ap2", "Proteínas BH3 e caspase 9; caspases 8 e 9 desencadeantes", ["ak-bcl2-inativacao", "au-caspases"]),
   ("ap3", "Adaptações (hipertrofia, hiperplasia, atrofia, metaplasia)", EXC + "aula 11 Acúmulos e adaptação")]),
]
