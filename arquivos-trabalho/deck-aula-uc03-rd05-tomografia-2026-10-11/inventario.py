"""Inventário atômico de Tomografia computadorizada (UC03 P1, Radiologia; Preceptoria 2024, João Vitor Dutra Vieira; 96 lâminas).
Material de base lido inteiro: lâminas 2024 (pptx da pasta pessoal = turma I, 96 lâminas), lâminas 2023 (turma II, 101) e 2020 (turma III, 57; mesmo conteúdo),
transcrição da aula (86 páginas, versão 2023), bibliografia da aula (Física básica da TC, Leite/Amaro/Otaduy), e-book ESR cap. 3 (Tomografia Computadorizada),
provas pelo índice rad-03, monitoria P1 (aula 2, TC do abdome) e apostilas de veteranos (Guia de Radiologia, Ilustrativa, Tudo que você precisa saber de RD).
Cada ideia aponta para o card que a pergunta (chave do spec, lista, "sh-<nid>" ou "EXC: motivo" só em lâmina). Menção no verso não conta.
"""
PREFIXO = "rd05"
AULA = "Tomografia computadorizada (UC03 P1; Radiologia; Preceptoria 2024)"
EXC = "EXC: "
JUSTIFICATIVAS = {}
ILUS = EXC + "exemplo ilustrativo ou doença usada para ilustrar a lâmina; sem card próprio (F-20261012-CLAUDE-01)"
REP = EXC + "repete a lâmina anterior (mesma figura com destaque); coberta pelo card da lâmina de origem"
OUTRA = EXC + "tema de outra aula do cronograma"
S = lambda n: f"sh-{n}"
TCDEF, NAOH, HIST = S(1791810567122), S(1791810569096), S(1791810565746)
RXSEC, RECON, RAPIDO, RADIACAO = S(1791810569222), S(1791810576172), S(1791810573868), S(1791810574120)
FASEC, FASEF, VO, JOSSEA = S(1791810576422), S(1791810576547), S(1791810577296), S(1791810577972)
HIPER, HIPO, ISO = S(1791810578222), S(1791810578347), S(1791810578471)
ARTDEF, ARTMET, ARTMOV = S(1791810579220), S(1791810579347), S(1791810579472)
ACR, ACRN, CIV = S(1791810568546), S(1791810568671), S(1791810574747)

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "capa", "Semiologia radiológica (título de seção)", []),
 (3, "conteudo", "Lateralidade na radiologia", [("a1", "Radiografia de tórax com D à esquerda da imagem: o lado direito do paciente aparece à esquerda do observador", "lateralidade")]),
 (4, "conteudo", "Resolução de imagem", [
   ("a2", "Resolução espacial: distinguir estruturas adjacentes (mais pixels)", "res-espacial"),
   ("a3", "Resolução de contraste: distinguir diferenças de intensidade, aumentada pelo meio de contraste", "res-contraste")]),
 (5, "capa", "Métodos de imagem (título de seção)", []),
 (6, "conteudo", "Métodos de imagem: TC sem e com contraste (arterial, venosa, tardia, cistotomografia, angiotomografia)", [
   ("a4", "Angiotomografia = TC com contraste IV em fase arterial", "angio-tc"),
   ("a5", "Fases arterial, venosa e tardia", "fases-ordem"),
   ("a6", "Cistotomografia", EXC + "uso específico listado em 'Outros'; sem desenvolvimento na aula (pergunta ao Davi)")]),
 (7, "conteudo", "Métodos não são hierárquicos (diagramas riscados)", [("a7", "RM não é superior à TC, que não é superior ao RX; métodos se complementam", NAOH)]),
 (8, "conteudo", "Objetivo = melhor cuidado do paciente", [("a8", "O pedido adequado, em benefício do paciente, é o objetivo", HIST)]),
 (9, "conteudo", "Tomografia computadorizada (título)", [("a9", "Definição de TC", TCDEF)]),
 (10, "conteudo", "Equipamento: gantry, mesa, console, bomba injetora", [
   ("a10", "Gantry (anel com tubo e detectores) e mesa", "gantry"),
   ("a11", "Console do computador onde o técnico planeja e adquire", EXC + "ambiente da sala de comando; o planejamento está no card do scout"),
   ("a12", "Bomba injetora de contraste EV", "injetora")]),
 (11, "conteudo", "Fotos do gantry e da bomba injetora", [("a13", "Gantry e bomba injetora EV", ["gantry", "injetora"])]),
 (12, "conteudo", "Interior do gantry: tubo de raios X e arco de detectores", [
   ("a14", "Tubo de raios X oposto ao arco de detectores", "tubo-detectores"),
   ("a15", "Detector converte fótons em sinal analógico e depois digital (bibliografia)", "detector-sinal")]),
 (13, "video", "Vídeo do gantry girando", []),
 (14, "conteudo", "Contraste iodado: EV, VO e VR", [("a16", "Contraste iodado endovenoso", CIV), ("a17", "Contraste iodado por via oral e retal", VO)]),
 (15, "conteudo", "Contraste baritado: VO e VR", [("a18", "Bário por via oral e retal", "bario-tc")]),
 (16, "conteudo", "Dados brutos → reconstrução (axial, sagital, coronal, 3D, MIP, MinIP, outros)", [
   ("a19", "Reconstrução multiplanar e 3D a partir de uma aquisição", RECON),
   ("a20", "Plano axial é o realmente adquirido", "axial-nativo"),
   ("a21", "MIP", "mip"), ("a22", "MinIP", "minip")]),
 (17, "conteudo", "Imagens axial, sagital, coronal e reformatação 3D", [
   ("a23", "Reconhecer axial", "img-axial"), ("a24", "Reconhecer sagital", "img-sagital"),
   ("a25", "Reconhecer coronal", "img-coronal"), ("a26", "Reconhecer reformatação 3D", "img-3d")]),
 (18, "conteudo", "Anatomia × radiografia × tomografia", [("a27", "Radiografia sobrepõe estruturas; TC é seccional", RXSEC)]),
 (19, "capa", "Aquisição da imagem (título de seção)", []),
 (20, "conteudo", "Dados brutos com o gantry em destaque", [("a28", "Aquisição no gantry gera dados brutos", REP)]),
 (21, "conteudo", "Duas fontes de luz projetam duas sombras", [("a29", "Duas projeções distinguem o que uma só sobrepõe", "projecoes")]),
 (22, "conteudo", "'ONE view is NO view!'", [("a30", "Uma projeção não basta", "projecoes")]),
 (23, "conteudo", "Esquema de projeções: objeto sobreposto com um feixe, separado com dois", [("a31", "Várias projeções separam estruturas sobrepostas", "projecoes")]),
 (24, "conteudo", "Radiografia localizadora (scout)", [("a32", "Scout planeja a região a ser adquirida", "scout")]),
 (25, "conteudo", "Esquemas do feixe e dos detectores no gantry", [("a33", "Feixe em leque e giro ao redor do paciente", ["leque", "tubo-detectores"])]),
 (26, "conteudo", "Esquema: tubo, colimador, detectores, computador, monitor", [("a34", "Colimador estreita o feixe e define a espessura do corte", "colimador")]),
 (27, "conteudo", "Evolução da TC: 1ª a 3ª gerações", [
   ("a35", "1ª geração: um detector e translação-rotação lentos", "primeira-geracao"),
   ("a36", "3ª geração: tubo e fileira de detectores giram juntos (a mais usada hoje)", "terceira-geracao"),
   ("a36b", "2ª geração: vários detectores e translação-rotação", EXC + "detalhe histórico das gerações intermediárias; pergunta ao Davi")]),
 (28, "conteudo", "Evolução da TC: 4ª e 5ª gerações", [("a37", "4ª geração (anel fixo de detectores) e 5ª (feixe de elétrons), de custo alto", EXC + "detalhe histórico; pergunta ao Davi")]),
 (29, "conteudo", "Evolução da TC: slip rings", [("a38", "Slip rings permitem rotação contínua", "slip-rings")]),
 (30, "conteudo", "Evolução da TC: 6ª geração helicoidal", [("a39", "Helicoidal: tubo gira contínuo", "helicoidal")]),
 (31, "conteudo", "Evolução da TC: 7ª geração helicoidal e multislice (64 fileiras no HC)", [("a40", "Multislice com várias fileiras de detectores", ["multislice", "single-multi"])]),
 (32, "conteudo", "Arco de detectores e fileira de detectores", [("a41", "Fileiras de detectores", "single-multi")]),
 (33, "conteudo", "Single slice × multislice", [("a42", "Uma fileira × várias fileiras", "single-multi")]),
 (34, "conteudo", "Helicoidal e multislice: mais resolução, menos tempo", [
   ("a43", "Helicoidal: exame contínuo", "helicoidal"), ("a44", "Multislice: várias fatias por acionamento do tubo", "multislice"),
   ("a45", "Mais resolução, menos tempo de exame", "multislice-ganho"),
   ("a46", "Helicoidal em uma apneia (livro ESR)", "helicoidal-apneia")]),
 (35, "capa", "Interpretação dos dados brutos (título de seção)", []),
 (36, "conteudo", "Dados brutos com a reconstrução em destaque", [("a47", "Computador reconstrói os dados brutos", REP)]),
 (37, "conteudo", "Voxel: pixel 2D → voxel 3D; matriz 512×512; 260.000 pixels", [
   ("a48", "Voxel", "voxel"), ("a49", "Eixos x e y definidos pela matriz 512×512", "matriz"),
   ("a50", "260.000 pixels", "pixels-260k"), ("a51", "Eixo z é a espessura do corte", ["voxel", "espessura-corte"]),
   ("a52", "Campo de visão e tamanho do pixel (bibliografia)", "fov")]),
 (38, "conteudo", "Problema A+B=7...: reconstrução algébrica de uma matriz 2×2", [("a53", "Reconstrução matemática dos dados", "retroprojecao")]),
 (39, "conteudo", "Retroprojeção em matriz de células", [("a54", "Retroprojeção reconstrói a imagem das somas medidas", "retroprojecao")]),
 (40, "conteudo", "Ponto reconstruído com 2, 4, 8, 16 e 32 projeções", [("a55", "Mais projeções, imagem mais nítida", "mais-projecoes")]),
 (41, "conteudo", "Ilustração geométrica de camadas de voxels", [("a56", "Voxels em camadas", REP)]),
 (42, "conteudo", "'CT scan: fatiamos o corpo como um pão'", [("a57", "TC corta o corpo em fatias axiais", ILUS)]),
 (43, "capa", "Formação da imagem (título de seção)", []),
 (44, "conteudo", "Dados brutos com a imagem em destaque", [("a58", "Imagem final no monitor", REP)]),
 (45, "conteudo", "Unidades Hounsfield: quantificar densidades, escala de cinza, água = 0, fórmula", [("a59", "Definição da unidade Hounsfield", "hu-def")]),
 (46, "conteudo", "Escala de Hounsfield: ar −1000, gordura, água 0, músculo, sangue, contraste IV ~250, osso 1000", [
   ("a60", "Ar −1000", "hu-ar"), ("a61", "Água 0", "hu-agua"), ("a62", "Gordura negativa", "hu-gordura"), ("a63", "Osso +1000", "hu-osso"),
   ("a64", "Contraste IV ~250", "hu-contraste"), ("a65", "Músculo e sangue", ["hu-musculo", "hu-sangue-agudo"])]),
 (47, "conteudo", "Tubo, detectores e ar, água, osso a −1000, 0 e 1000 UH", [("a66", "Quanto mais atenua, mais branco", "hu-branco")]),
 (48, "conteudo", "Tabela de faixas de UH no crânio (osso, substância branca, músculo, cinzenta, hemorragia, LCR, gordura, ar)", [
   ("a67", "Hemorragia aguda 65–95 UH", "hu-sangue-agudo"), ("a68", "Substância branca × cinzenta", "hu-substancia"),
   ("a69", "Músculo 20–40 UH", "hu-musculo"), ("a70", "LCR = água = 0 UH", "hu-agua")]),
 (49, "conteudo", "Janelas e níveis: recurso computacional; olho 20–64 tons; TC ≥ 2000 valores; 256 tons", [
   ("a71", "Por que janelas", "janela-motivo"), ("a72", "Números de tons de cinza", "olho-cinzas")]),
 (50, "conteudo", "Janela, nível e limites branco/preto", [
   ("a73", "Nível = centro", "janela-nivel"), ("a74", "Largura = faixa", "janela-largura"), ("a75", "Acima = branco, abaixo = preto", "janela-limites")]),
 (51, "conteudo", "Exemplo nível 50, janela 200", [("a76", "Janela −50 a 150", "janela-exemplo")]),
 (52, "conteudo", "Janelas de partes moles, parênquima pulmonar e osso", [
   ("a77", "Reconhecer janela de partes moles", "img-janela-partes-moles"), ("a78", "Reconhecer janela de pulmão", "img-janela-pulmao"),
   ("a79", "Reconhecer janela óssea", "img-janela-osso"), ("a80", "Janela óssea na fratura", JOSSEA)]),
 (53, "conteudo", "Escolha da janela por estrutura, com parênquima encefálico", [("a81", "Janelas por estrutura", REP)]),
 (54, "conteudo", "Isquemia do parênquima encefálico (AVC) em janela estreita", [("a82", "AVC visto em janela estreita", ILUS)]),
 (55, "conteudo", "Janela ampla × janela estreita", [("a83", "Janela ampla", "janela-ampla"), ("a84", "Janela estreita", "janela-estreita")]),
 (56, "conteudo", "Hiperatenuante e hipoatenuante", [
   ("a85", "Hiperatenuante", HIPER), ("a86", "Hipoatenuante", HIPO), ("a87", "Isoatenuante (bibliografia)", ISO),
   ("a88", "Tecido de referência (bibliografia)", "referencia-lesao"), ("a89", "Cálcio hiperatenuante (prova)", "calcio-hiper")]),
 (57, "capa", "Técnicas do exame (título de seção)", []),
 (58, "conteudo", "TC sem contraste ou com contraste EV, VO, VR; fases e tempos de aquisição", [
   ("a90", "Sem contraste", "sem-contraste"), ("a91", "Sequência das fases", "fases-ordem"),
   ("a92", "Tempos: angiográfica 15 s, arterial 30 s, portal 70 s, nefrográfica 90 s, equilíbrio 3 min, excretora 7 min", ["tempo-arterial", "tempo-portal", "tempo-tardia", "fases-ordem"]),
   ("a93", "Fase angiográfica", "fase-angiografica"), ("a94", "Fase excretora", "fase-excretora"),
   ("a95", "Com contraste há várias aquisições", "contraste-multiaquisicao")]),
 (59, "conteudo", "Fotos de contraste iodado EV, VO, VR", [
   ("a96", "Contraste iodado EV", CIV), ("a97", "Contraste realça vasos", "contraste-realce-vasos"), ("a98", "Função renal antes do contraste", "contraste-rim")]),
 (60, "conteudo", "Fotos de contraste baritado VO e VR", [("a99", "Contraste baritado", "bario-tc")]),
 (61, "conteudo", "Exame trifásico (sem, arterial, portal, equilíbrio)", [("a100", "Quatro aquisições do trifásico", "trifasico"), ("a101", "Arterial antes da venosa", FASEC)]),
 (62, "conteudo", "Fase sem contraste (esquema e TC)", [("a102", "Reconhecer TC sem contraste", "img-sem-contraste")]),
 (63, "conteudo", "Fase arterial (esquema e TC)", [
   ("a103", "Reconhecer fase arterial", "img-arterial"), ("a104", "Arterial mostra nódulo hipervascular", "fase-arterial-nodulo"),
   ("a105", "Arterial define córtex renal", "fase-arterial-rim"), ("a106", "Fases caracterizam nódulos hepáticos", FASEF)]),
 (64, "conteudo", "Fase venosa/portal (esquema e TC)", [("a107", "Reconhecer fase portal", "img-portal"), ("a108", "Portal mostra veia porta", "fase-portal-veias")]),
 (65, "conteudo", "Fase tardia (esquema e TC)", [("a109", "Reconhecer fase tardia", "img-tardia"), ("a110", "Equilíbrio: pelve renal", "fase-equilibrio-pelve")]),
 (66, "conteudo", "Cinco fases lado a lado (sem, arterial, portal, equilíbrio, nefrográfica)", [("a111", "Fase nefrográfica", "fase-nefrografica")]),
 (67, "conteudo", "Contraste EV isolado e com água VO, retal ou oral", [
   ("a112", "Água oral distende as alças", "agua-vo"), ("a113", "Contraste retal × oral", "retal-colo"), ("a114", "Contraste oral enche as alças", VO)]),
 (68, "conteudo", "Artefato de endurecimento do feixe (metal)", [
   ("a115", "Definição de artefato", ARTDEF), ("a116", "Reconhecer artefato de metal", "img-artefato-metal"),
   ("a117", "Metal gera artefato", ARTMET), ("a118", "Mecanismo do endurecimento (livro ESR)", "endurecimento-feixe")]),
 (69, "conteudo", "Artefato de movimentação", [
   ("a119", "Reconhecer artefato de movimento", "img-artefato-mov"), ("a120", "Movimento gera artefato", ARTMOV), ("a121", "Volume parcial (monitoria, livro)", "volume-parcial")]),
 (70, "conteudo", "Meme do panorama que deu errado", [("a122", "Ilustração de artefato de movimento", ILUS)]),
 (71, "capa", "Anatomia TC (título de seção)", []),
] + [(n, "conteudo", "Anatomia seccional do abdome: axial com linha de nível no coronal", [("a%d" % (123 + n - 72), "Corte axial de abdome sem rótulos",
      EXC + "anatomia seccional do abdome sem rótulos; o professor disse que passa 'rapidão' e a anatomia do abdome é de UC08")]) for n in range(72, 85)] + [
 (85, "capa", "Exemplos de achados (título de seção)", []),
 (86, "conteudo", "Apendicite aguda não complicada, com escala de UH", [("a136", "Gordura inflamada mais densa que gordura normal", ILUS)]),
 (87, "conteudo", "Esteatose hepática, com escala de UH", [("a137", "Fígado gorduroso hipoatenuante", ILUS)]),
 (88, "conteudo", "Pneumotórax: radiografia e TC em janela de pulmão", [("a138", "Pneumotórax mais visível na TC", ILUS)]),
 (89, "conteudo", "Vantagens e desvantagens da TC", [
   ("a139", "Rápido e excelente resolução espacial", RAPIDO), ("a140", "Boa resolução de contraste", "boa-res-contraste"),
   ("a141", "Imagens seccionais e multiplanares", RECON), ("a142", "Remove a superposição", "sem-superposicao"),
   ("a143", "Representação quantitativa", "quantitativa"), ("a144", "Radiação", RADIACAO),
   ("a145", "Contraste nem sempre obrigatório", "res-contraste"), ("a146", "Envolve transporte", "sem-leito")]),
 (90, "conteudo", "O que queremos? Solicitar o método adequado e reconhecer achados que não esperam o radiologista", [
   ("a147", "Solicitar o método apropriado", HIST), ("a148", "Achados que não esperam o radiologista", "achados-urgentes")]),
 (91, "conteudo", "Como? ACR Appropriateness Criteria (1–3, 4–6, 7–9)", [("a149", "ACR", ACR), ("a150", "Notas do ACR", ACRN)]),
 (92, "conteudo", "Tabela ACR de dor no hipocôndrio direito", [("a151", "Exemplo de tabela ACR", EXC + "exemplo ilustrativo (dor no hipocôndrio direito); a lógica 1–9 está nos cards do ACR")]),
 (93, "conteudo", "Mensagens finais", [
   ("a152", "Método volumétrico computadorizado", TCDEF), ("a153", "Radiação ionizante", RADIACAO), ("a154", "Com ou sem contraste", "contraste-multiaquisicao"),
   ("a155", "Boa resolução espacial e de contraste", ["res-espacial", "res-contraste"]), ("a156", "Pedido adequado à hipótese", HIST),
   ("a157", "Métodos se complementam", NAOH)]),
 (94, "conteudo", "Sir Godfrey Hounsfield, Nobel de Medicina de 1979", [("a158", "Hounsfield inventou a TC e ganhou o Nobel", "hounsfield-nobel")]),
 (95, "conteudo", "Primeira TC de crânio (1971) e TC atual (2023)", [("a159", "Primeira imagem de TC em 1971", "hounsfield-nobel")]),
 (96, "capa", "Obrigado", []),
]
CAPITULO = [("E-book ESR de radiologia na graduação, cap. 3 Tomografia Computadorizada (bibliografia básica da turma)", [
  ("l1", "Componentes: tubo, gantry com detectores opostos, computador; filtro, colimador, cintilador e fotodiodo", ["tubo-detectores", "colimador", "detector-sinal"]),
  ("l2", "Gerações: a 3ª é a mais usada hoje", "terceira-geracao"),
  ("l3", "TC de dupla energia e de contagem de fótons", EXC + "tecnologias avançadas fora da aula; pergunta ao Davi"),
  ("l4", "Varredura axial × helicoidal e suas vantagens (apneia única, multifásica)", ["helicoidal", "helicoidal-apneia", "contraste-multiaquisicao"]),
  ("l5", "Pitch", EXC + "parâmetro técnico não ensinado na aula; pergunta ao Davi"),
  ("l6", "Escala de Hounsfield: água 0, ar −1000, tecidos relativos", ["hu-def", "hu-ar", "hu-agua", "hu-gordura", "hu-osso"]),
  ("l7", "Retroprojeção filtrada e reconstrução iterativa", ["retroprojecao"]),
  ("l8", "Kernel e espessura do corte", ["espessura-corte"]),
  ("l9", "Janelas: nível e largura; partes moles, pulmão, osso", ["janela-nivel", "janela-largura", "img-janela-pulmao"]),
  ("l10", "Resolução espacial e de contraste e seus fatores", ["res-espacial", "res-contraste"]),
  ("l11", "Artefatos: endurecimento do feixe, estrias, movimento, volume parcial", ["endurecimento-feixe", "img-artefato-mov", "volume-parcial"]),
  ("l12", "Artefatos de truncamento, feixe cônico, anel e pseudorrealce", EXC + "artefatos além dos ensinados na aula; pergunta ao Davi"),
  ("l13", "Índices de dose (CTDI) e modulação de dose", EXC + "parâmetros de dose não ensinados na aula; radiação está no card da aula 02"),
  ("l14", "Anatomia seccional de pescoço, tórax e abdome", EXC + "anatomia seccional é de outras UCs; a aula passa 'rapidão'"),
  ("l15", "Mensagens finais: UH diferenciam hemorragia, calcificação e líquido", ["hu-sangue-agudo", "calcio-hiper", "hu-agua"])])]
CAPITULO.append(("Mello Júnior, Radiologia Básica, cap. 1 (seção Tomografia computadorizada)", [
  ("m1", "TC dá cortes axiais com resolução muito superior; cerca de 250 tons de cinza contra 25 da radiografia", ["res-espacial", "olho-cinzas"]),
  ("m2", "Unidades Hounsfield: água 0, ar −1000, gordura −50 a −100; janelas de crânio (óssea e partes moles) e tórax (pulmão e mediastino)", ["hu-def", "hu-gordura", "img-janela-osso", "img-janela-pulmao"]),
  ("m3", "Hiperdenso, hipodenso e isodenso são comparativos", [HIPER, HIPO, ISO])]))
EXERCICIOS = [
 ("Provas UC03 (índice rad-03, 54 subquestões 2015–2025)", [
  ("p1", "Identificar a modalidade TC pelos termos hiper e hipoatenuante", [HIPER, HIPO, "calcio-hiper"]),
  ("p2", "Mecanismo de formação: tubo emite, detectores opostos, atenuação, reconstrução em planos", ["tubo-detectores", "hu-branco", RECON]),
  ("p3", "Contraste IV: aorta e rins hiperatenuantes; angio-TC em fase arterial; plano de reconstrução", ["contraste-realce-vasos", "angio-tc", "img-sagital", "img-coronal"]),
  ("p4", "Cuidados na TC: dose elevada e toxicidade renal do contraste", [RADIACAO, "contraste-rim"]),
  ("p5", "TC não vai ao leito; resolução anatômica melhor que US e RX; RM mais cara e demorada", ["sem-leito", "res-espacial"]),
  ("p6", "Descrever lesões (vidro fosco, massa pancreática hipercaptante, lesão óssea)", ["calcio-hiper", "hu-gordura", "hu-sangue-agudo"])]),
 ("Monitoria P1, aula 2 (TC do abdome)", [
  ("m1", "Obtenção: tubo, colimador, detectores, cortes helicoidais e multislice", ["tubo-detectores", "colimador", "helicoidal", "multislice"]),
  ("m2", "Densidades: ar −1000 preto, água 0 cinza, osso +1000 branco", ["hu-ar", "hu-agua", "hu-osso"]),
  ("m3", "Janela: centro e largura; partes moles perto de 0; pulmão perto de −1000", ["janela-nivel", "janela-largura", "img-janela-pulmao"]),
  ("m4", "Hiperatenuante e hipoatenuante", [HIPER, HIPO]),
  ("m5", "Vantagens (detalhe, rapidez, três planos) e desvantagens (radiação, sem mobilidade, contraste)", ["boa-res-contraste", RADIACAO, "sem-leito"]),
  ("m6", "Fases do contraste e o que cada uma mostra; sem contraste para osso, calcificações e cálculos", ["sem-contraste", "fase-angiografica", "fase-arterial-nodulo", "fase-portal-veias", "fase-nefrografica", "fase-equilibrio-pelve"]),
  ("m7", "Artefatos: metal (strike), movimento, volume parcial", ["img-artefato-metal", "img-artefato-mov", "volume-parcial"])]),
 ("Apostilas de veteranos (Guia de Radiologia aula 3, Ilustrativa, Tudo que você precisa saber de RD)", [
  ("v1", "Valores de UH: ar −1000, gordura −120 a −80, água 0, músculo 50, osso 300–350", ["hu-ar", "hu-gordura", "hu-agua", "hu-musculo", "hu-osso"]),
  ("v2", "Isoatenuante, hipo e hiperatenuante", [ISO, HIPO, HIPER]),
  ("v3", "Fases e tempos: angiográfica 15 s a excretora 7 min; TC de abdome em quatro formas (sem, EV, VO, VR)", ["fases-ordem", "tempo-arterial", "tempo-portal", "tempo-tardia", "retal-colo"]),
  ("v4", "Adenoma adrenal rico em lipídeos tem UH baixo e washout rápido", ["hu-gordura", "hu-agua"]),
  ("v5", "Casos de embolia pulmonar (angio-TC) e massa pancreática", ["angio-tc", "contraste-realce-vasos"])])]


# Análise do deck-prova 2026-10-13: itens cujo card saiu desta aula passam a exclusão com o motivo.
_RETIRADOS = {"lateralidade": "repetido", "injetora": "detalhe-tecnico", "detector-sinal": "detalhe-tecnico", "bario-tc": "detalhe", "mip": "detalhe-tecnico", "minip": "detalhe-tecnico", "leque": "detalhe-tecnico", "primeira-geracao": "detalhe-tecnico", "terceira-geracao": "detalhe-tecnico", "slip-rings": "detalhe-tecnico", "single-multi": "repetido", "helicoidal-apneia": "detalhe", "multislice-ganho": "repetido", "matriz": "detalhe-numerico", "pixels-260k": "detalhe-numerico", "fov": "detalhe-tecnico", "espessura-corte": "detalhe-tecnico", "retroprojecao": "detalhe-tecnico", "mais-projecoes": "detalhe-tecnico", "hu-contraste": "detalhe-numerico", "hu-branco": "repetido", "hu-musculo": "detalhe-numerico", "hu-sangue-agudo": "detalhe-numerico", "hu-substancia": "detalhe", "olho-cinzas": "detalhe-numerico", "janela-exemplo": "detalhe-numerico", "calcio-hiper": "repetido", "tempo-arterial": "detalhe-numerico", "tempo-portal": "detalhe-numerico", "tempo-tardia": "detalhe-numerico", "fase-angiografica": "detalhe-numerico", "fase-excretora": "detalhe-numerico", "trifasico": "repetido", "fase-arterial-rim": "detalhe", "fase-equilibrio-pelve": "detalhe", "fase-nefrografica": "detalhe", "agua-vo": "detalhe", "retal-colo": "detalhe", "endurecimento-feixe": "detalhe-tecnico", "volume-parcial": "detalhe-tecnico", "sem-superposicao": "repetido", "quantitativa": "repetido", "boa-res-contraste": "repetido", "sem-leito": "repetido", "sh-1791810568671": "detalhe-numerico"}
def _remap(dest):
    ds = [dest] if isinstance(dest, str) else list(dest)
    if any(isinstance(d, str) and d.startswith('EXC') for d in ds): return dest
    keep = [d for d in ds if d not in _RETIRADOS]
    if keep: return keep[0] if isinstance(dest, str) else keep
    return 'EXC: ' + 'tirado na análise do deck-prova (' + _RETIRADOS[ds[0]] + '): além do nível de ciclo básico desta aula ou repetido em outra aula'
SLIDES = [(n, t, tit, [(i, x, _remap(d)) for i, x, d in items]) for n, t, tit, items in SLIDES]
CAPITULO = [(t, [(i, x, _remap(d)) for i, x, d in items]) for t, items in globals().get('CAPITULO', [])]
EXERCICIOS = [(t, [(i, x, _remap(d)) for i, x, d in items]) for t, items in globals().get('EXERCICIOS', [])]
