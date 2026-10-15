"""Inventário de Mecanismos efetores imunes (UC03 P1; Imunologia; 64 lâminas = turma), escrito antes da seleção (15/10).
Material: lâminas, transcrição (lida inteira), provas imuno-05 (32 itens; 10 próprios)."""
PREFIXO = "im22"
AULA = "Mecanismos efetores imunes (UC03 P1; Imunologia)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"
X = lambda n, t, m="aula 08; Tab": (n, "conteudo", t, [(f"x{n}", t, EXC + m)])
SLIDES = [
 (1, "capa", "Capa", []),
 X(2, "Sistema de reconhecimento", "revisão; Tab"),
 (3, "conteudo", "Função efetora imediata × tardia", [("a1", "Imediata/tardia", "a-imediata")]),
 X(4, "Abertura", "abertura"), (5, "conteudo", "PRR de PAMPs", [("r5", "PRR reconhecem PAMP", S(1791780342851))]), (6, "conteudo", "PRR solúveis/membrana/citoplasma", [("r6", "Famílias e localização", S(1792029609563))]), X(7, "Toll na mosca"), (8, "conteudo", "TLR4 e efeitos", [("r8", "TLR4/CD14 e LPS", S(1791743339358)), ("r8b", "MyD88 → NF-κB", S(1792029614609))]),
 X(9, "NOD"), (10, "conteudo", "NOD1 e NOD2", [("r10", "NOD2 e muramil dipeptídeo", S(1792029613859))]), (11, "conteudo", "Inflamassoma", [("r11", "Inflamassoma e IL-1β/IL-18", [S(1791743339740), S(1791743339860)])]), X(12, "Quem reconhece?", "abertura"),
 X(13, "Células, moléculas e órgãos", "revisão; Tab"), (14, "conteudo", "Células da inflamação", [("r14", "Residentes iniciam a inflamação", S(1791780352647))]),
 (15, "conteudo", "Receptores do macrófago", [("a2", "Fc, C3b, manose", "b-opsonizacao")]),
 X(16, "Citocinas e quimiocinas", "aula 08"), X(17, "Quimioatraentes", "aula 38"), X(18, "Mediadores", "aula 38"), X(19, "Abertura", "abertura"),
 (20, "conteudo", "Inata × adquirida", [("r20", "Dois níveis de reconhecimento", S(1792029608910))]), X(21, "Linha do tempo", "aula 08"),
 (22, "conteudo", "Não celulares", [("a3", "Peptídeos", "a-peptideos"), ("a3b", "Barreiras físicas e secreções", "a-barreiras")]),
 (23, "conteudo", "Fagocitose", [("a4", "Fagossomo", "b-opsonizacao")]),
 X(24, "Sinalização da fagocitose", "detalhe molecular; Tab"), (25, "conteudo", "Etapas da fagocitose", [("a4b", "Quimiotaxia, adesão/opsonização, englobamento, fusão com lisossomo, morte", S(1792029611637))]),
 (26, "conteudo", "Opsonização: receptores", [("a5", "C3b e Fc", ["b-opsonizacao", S(1791667096988)])]),
 (27, "conteudo", "Com e sem opsoninas", [("a6", "Eficiência", "b-opsonizacao")]),
 (28, "conteudo", "ROS", [("a7", "NADPH oxidase, MPO", [S(1791780361432), S(1791780361607)])]),
 (29, "conteudo", "NO e RNS", [("a8", "NOS, peroxinitrito", [S(1791625430456), S(1791780362080)])]),
 (30, "conteudo", "Neutrófilos: origem", [("a9", "45–70%", "b-pus")]),
 (31, "conteudo", "Neutrófilos: funções", [("a10", "Burst e morte", ["b-pus", "b-nao-apc", S(1791647814494), S(1791743343884)])]),
 (32, "conteudo", "Neutrófilos: espécies reativas", [("a11", "NETs", "b-nets")]),
 (33, "conteudo", "NETs", [("a12", "NETose", "b-nets")]),
 (34, "conteudo", "ADCC", [("a13", "CD16", [S(1791629596121), "b-adcc"])]),
 (35, "conteudo", "Células NK", [("a14", "Sem TCR", "c-nk")]),
 (36, "conteudo", "NK: KIR", [("a15", "MHC I", [S(1791984891454), "c-kir"])]),
 (37, "conteudo", "NK: perforina", [("a16", "Granzimas", S(1791984891827))]),
 (38, "conteudo", "Origem dos macrófagos", [("a17", "Residentes × infiltrantes", "d-residentes")]),
 (39, "conteudo", "Subtipos por órgão", [("a18", "Nomes", "d-nomes")]),
 (40, "conteudo", "M1", [("a19", "Clássico", S(1791625434032))]),
 (41, "conteudo", "M2", [("a20", "Reparo", S(1791625434457))]),
 (42, "conteudo", "Mreg", [("a21", "IL-10", "d-mreg"), ("a21b", "Perfis M1, M2, regulador lado a lado", ["d-mreg", S(1791625434032), S(1791625434457)])]),
 (43, "conteudo", "Macrófagos e T", [("a22", "Interação", "d-mreg")]),
 X(44, "Abertura", "abertura"),
 (45, "conteudo", "Migração de T naive", [("a23", "Recirculação", S(1791625425207))]),
 X(46, "Início da resposta adaptativa", "aula 20"),
 (47, "conteudo", "Migração de T efetor", [("a24", "Selectinas, integrinas", S(1791625425207))]),
 (48, "conteudo", "Endereçamento", [("a25", "Receptores de quimiocina", "e-homing")]),
 X(49, "Apresentação de antígenos", "aula 20"), X(50, "Apresentação e diferenciação", "aula 45"),
 (51, "conteudo", "Imunidade celular", [("a26", "CD4 × CD8", "e-cd4-cd8")]),
 (52, "conteudo", "Ativação de macrófagos", [("a27", "IFN-γ, CD40L", ["e-th1", S(1791625430632)])]),
 (53, "conteudo", "Funções Th1", [("a28", "Th1", "e-th1")]),
 (54, "conteudo", "Funções Th2", [("a29", "Th2", "e-th2")]),
 (55, "conteudo", "Th17", [("a30", "IL-6 + TGF-β", S(1791625432733)), ("a30b", "Subtipo conforme a ameaça", "e-subtipo-ameaca")]),
 (56, "conteudo", "Th17 e Candida", [("a31", "Dectina → Th17", ["e-candida", S(1791625422039)])]),
 (57, "conteudo", "CTL", [("a32", "MHC I, grânulos", "e-ctl")]),
 (58, "conteudo", "Lise da célula-alvo", [("a33", "Granzimas", "e-ctl")]),
 X(59, "Resumindo", "abertura"),
 (60, "conteudo", "Dinâmica da resposta", [("a34", "Memória", "e-memoria")]),
 (61, "conteudo", "CD4 Th1", [("a35", "Macrófago", "e-th1")]),
 (62, "conteudo", "Th2 limita macrófago", [("a36", "Supressão", "e-th2")]),
 (63, "conteudo", "Th1 × Th2", [("a37", "Hanseníase", [S(1791625425933), S(1791625426108)])]),
 (64, "conteudo", "Papel dos linfócitos T", [("a38", "Humoral × celular", "e-cd4-cd8")]),
]
JUSTIFICATIVAS = {1: "capa"}
CAPITULO = [("Transcrição da aula", [("t1", "Pus", "b-pus"), ("t2", "Residentes do saco vitelino", "d-residentes"), ("t3", "CD4 ajuda, CD8 mata", "e-cd4-cd8"), ("t4", "Só adaptativa tem memória", "e-memoria")])]
EXERCICIOS = [("Provas UC03 (imuno-05)", [("p1", "2017 P1 4.3: anticorpos antivirais e ADCC", [S(1791629596121), "b-adcc"]), ("p2", "2015 P1 1.4 e 2.3: opsonização", "b-opsonizacao"),
   ("p3", "2015 P2 2.7: granzima e perforina", "e-ctl"), ("p4", "2024 P1 2.11: NK", "c-nk"), ("p5", "2015 P2 7.2: TAP inibido pelo HHV-1 → menos MHC I, CD8 falha, NK age", "c-tap-nk")])]
