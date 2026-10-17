"""Inventário atômico de Mecanismos efetores do sistema imune (UC03 P1; Imunologia; Prof. Niels Câmara), escrito ANTES de escolher
cards (17/10, pipeline v4). Sequência = 64 lâminas (fontes/slides.pdf = pasta pessoal = turma, mesmo texto), vistas inteiras nesta sessão
(io/g0..g5). Lido nesta sessão: transcrição integral, provas imuno-05, monitoria P1, mapas imunológicos 1–3, apostila UC3, apostila
guia (seção da imunidade inata), Abbas 8ª ed. cap. 4 (fagocitose e morte microbiana).
Fronteira (MEMORY §3): reconhecimento inato (TLR, NOD, inflamassoma) é da 08; inflamação aguda e mediadores, da 37/38; apresentação e
ativação T, da 20/45; 23 notas vivas já levam a etiqueta desta aula (22 antiga) e entram por sh(), com outras cópias vivas.
"""
PREFIXO = "im22"
AULA = "Mecanismos efetores do sistema imune (UC03 P1; Imunologia)"
EXC = "EXC: "
BURST = "sh-1792240189395"
_08 = EXC + "recapitulação do reconhecimento inato (aula 08)"

SLIDES = [(1, "capa", "Capa", [])] + [
 (2, "conteudo", "Sistema imune como sistema de reconhecimento", [("a1", "Perigo → homeostase", _08)]),
 (3, "conteudo", "Perigo → receptor → função efetora (imediata ou tardia)", [("a2", "Função efetora", "sh-1791780342851")]),
 (4, "secao", "Sistema de reconhecimento", []),
 (5, "conteudo", "Receptores de PAMP por patógeno", [("a3", "PRR", "sh-1791780342851")]),
 (6, "conteudo", "PRR solúveis, de membrana e citoplasmáticos", [("a4", "PRR", _08)]),
 (7, "conteudo", "Receptores Toll (mosca × humano)", [("a5", "Toll", _08)]),
 (8, "conteudo", "TLR4 e CD14: fagócito-oxidase, iNOS, citocinas", [("a6", "CD14/TLR4", "sh-1791743339358")]),
 (9, "conteudo", "Família NOD citosólica", [("a7", "NOD", _08)]),
 (10, "conteudo", "NOD1 (DAP) e NOD2 (MDP)", [("a8", "NOD1/NOD2", _08)]),
 (11, "conteudo", "Inflamassoma: caspase, IL-1β, piroptose", [("a9", "Inflamassoma", ["sh-1791743339740", "sh-1791743339860"])]),
 (12, "conteudo", "Quem faz o reconhecimento?", [("a10", "Pergunta", EXC + "pergunta retórica")]),
 (13, "conteudo", "Células, moléculas e órgãos; citocinas", [("a11", "Citocinas dos macrófagos", ["ak-il1", "ak-il6", "sh-1791780360378", "sh-1791625433782", "sh-1791743347685"])]),
 (14, "conteudo", "Células do processo inflamatório", [("a12", "Neutrófilo", ["ak-neutrofilo-comum", "sh-1791780342036", "ak-neutrofilo-bacteria", "ak-neutrofilo-imagem", "ak-neutrofilo-fagocita"])]),
 (15, "conteudo", "Receptores do macrófago (TLR, dectina, CR, scavenger, manose, FcR)", [("a13", "Receptores", "sh-1791743339358")]),
 (16, "conteudo", "Citocinas e quimiocinas (autócrina, parácrina, endócrina)", [("a14", "Quimiocinas", ["sh-1791780359733", "sh-1791743347807"])]),
 (17, "conteudo", "Migração leucocitária por quimioatraentes", [("a15", "Quimiotaxia", ["sh-1791780360504", "sh-1791780359733"])]),
 (18, "conteudo", "Mediadores da inflamação", [("a16", "Mediadores", EXC + "mediadores: aula 38 Inflamação aguda")]),
 (19, "conteudo", "Quais são os mecanismos efetores?", [("a17", "Pergunta", EXC + "pergunta retórica")]),
 (20, "conteudo", "Imunidade natural × adquirida", [("a18", "Inata × adquirida", "sh-1791780341641")]),
 (21, "conteudo", "Inata (horas) × adaptativa (dias)", [("a19", "Tempo", "sh-1791780341641")]),
 (22, "conteudo", "Não celulares: barreiras, secreções, peptídeos antimicrobianos", [("a20", "Defensinas e lactoferrina", ["sh-1791023299492", "sh-1791647814494"])]),
 (23, "conteudo", "Fagocitose: englobamento e fagossomo", [("a21", "Fagocitose", ["ak-fagocitose", "sh-1791780361129"])]),
 (24, "conteudo", "Fagocitose: sinalização pelo FcγR", [("a22", "FcR", "sh-1791629595447")]),
 (25, "conteudo", "Fagocitose com IgG", [("a23", "IgG opsoniza", "sh-1791629595447")]),
 (26, "conteudo", "Opsonização: C3b, FcR", [("a24", "Opsoninas", "sh-1791667096988")]),
 (27, "conteudo", "Sem × com opsoninas", [("a25", "Opsonização melhora a fagocitose", "sh-1791667096988")]),
 (28, "conteudo", "ROS: NADPH oxidase, SOD, MPO → HOCl", [("a26", "Burst", [BURST, "sh-1791780361432", "ak-sod", "sh-1791780361607", "sh-1791780361781", "ak-o2-independente", "sh-1791743343884"])]),
 (29, "conteudo", "NO: NOS (arginina → citrulina), peroxinitrito", [("a27", "NO e peroxinitrito", ["sh-1791625430456", "sh-1791780362080", "sh-1791625430632"])]),
 (30, "conteudo", "Neutrófilos: origem na medula", [("a28", "Origem", "ak-neutrofilo-comum")]),
 (31, "conteudo", "Neutrófilos: adesão, extravasamento, fagocitose, burst, NETs", [("a29", "Funções", ["sh-1791780359733", "ak-neutrofilo-fagocita"])]),
 (32, "conteudo", "Neutrófilo: Nox2, MPO, iNOS", [("a30", "Burst do neutrófilo", "sh-1791780361607")]),
 (33, "conteudo", "NETs", [("a31", "NETs", "sh-1791743344060")]),
 (34, "conteudo", "ADCC (CD16)", [("a32", "ADCC", ["sh-1791629596121", "ak-nk-cd16", "sh-1791629595996"])]),
 (35, "conteudo", "Células NK: sem TCR, tumores e vírus, IFN-γ", [("a33", "NK", ["ak-nk-inata", "ak-nk-cd56", "sh-1791625433908", "ak-nk-il2-il12", "sh-1791984891204"])]),
 (36, "conteudo", "NK: KIR e MHC I; ADCC", [("a34", "MHC I ausente", ["sh-1791984891454", "ak-nk-tumor", "ak-ifn-antitumor"])]),
 (37, "conteudo", "NK: perforina e granzimas", [("a35", "Perforina/granzima", "sh-1791984891827")]),
 (38, "conteudo", "Macrófagos: origem (monócito)", [("a36", "Monócito → macrófago", ["sh-1791716410077", "au-residente"])]),
 (39, "conteudo", "Macrófagos teciduais (Kupffer, micróglia, alveolar…)", [("a37", "Residentes", ["au-residente", "sh-1791743341958", "ak-macrofago-tardio", "ak-lisozima", "ak-cd14", "sh-1791983679757"])]),
 (40, "conteudo", "M1 classicamente ativado", [("a38", "M1", ["sh-1791625434032", "sh-1791625430208"])]),
 (41, "conteudo", "M2 reparador", [("a39", "M2", "sh-1791625434457")]),
 (42, "conteudo", "Macrófago regulador", [("a40", "Mreg", "au-mreg")]),
 (43, "conteudo", "Macrófago e células T (IL-12, IFN-γ, IL-10)", [("a41", "Interação", ["ak-cd40l", "sh-1791625430082", "sh-1791625431258", "sh-1791625428533"])]),
 (44, "secao", "Mecanismos efetores dos linfócitos T", []),
 (45, "conteudo", "Migração dos T naive (recirculação)", [("a42", "Naive × efetor", "sh-1791625425207")]),
 (46, "conteudo", "Início da resposta adaptativa (TLR → Th1/Th2)", [("a43", "IL-12 → Th1", "sh-1791625433782")]),
 (47, "conteudo", "Migração dos T efetores", [("a44", "Efetores vão ao tecido", "sh-1791625425207")]),
 (48, "conteudo", "Receptores de endereçamento por tecido", [("a45", "Homing", "sh-1791625425207")]),
 (49, "conteudo", "Apresentação de antígenos", [("a46", "Apresentação", EXC + "apresentação: aula 20")]),
 (50, "conteudo", "Apresentação e diferenciação (Th2, Th17, Th1)", [("a47", "Subtipos", "sh-1791625432733")]),
 (51, "conteudo", "Imunidade mediada por células: CD4 e CD8", [("a48", "CTL mata infectada", "sh-1791625429957")]),
 (52, "conteudo", "Ativação de macrófagos pelo Th1 (IFN-γ, CD40L)", [("a49", "IFN-γ ativa macrófago", ["sh-1791625430208", "sh-1791625430082"])]),
 (53, "conteudo", "Funções Th1", [("a50", "Th1", ["sh-1791625422657", "sh-1791625431758"])]),
 (54, "conteudo", "Funções Th2", [("a51", "Th2", ["sh-1791625432007", "sh-1791625432133"])]),
 (55, "conteudo", "Th17: IL-6 + TGF-β, IL-17", [("a52", "Th17", ["sh-1791625432733", "sh-1791625422039"])]),
 (56, "conteudo", "Th17 contra Candida (dectina-1)", [("a53", "Candida", ["sh-1791743340332", "sh-1792175043737"])]),
 (57, "conteudo", "CTL: MHC I, grânulos, perforina e granzimas", [("a54", "CTL", "sh-1791593462592")]),
 (58, "conteudo", "Lise das células-alvo", [("a55", "Fas", "sh-1791625430882")]),
 (59, "secao", "Resumindo", []),
 (60, "conteudo", "Dinâmica: reconhecimento, ativação, efeito, homeostase, memória", [("a56", "Dinâmica", EXC + "memória e contração: aulas 07 e 45")]),
 (61, "conteudo", "CD4 Th1 ativa macrófagos", [("a57", "CD4 ajuda", "sh-1791625422657")]),
 (62, "conteudo", "Th2 limita a ativação do macrófago", [("a58", "Th2 inibe", "sh-1791625434457")]),
 (63, "conteudo", "Th1 ou Th2? Leishmania, hanseníase", [("a59", "Equilíbrio", ["sh-1791625421906", "sh-1791625425933", "sh-1791625426108"])]),
 (64, "conteudo", "Papel dos linfócitos T (humoral × celular)", [("a60", "Resumo", "sh-1791625429957")]),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "secao": "título de seção"}
CAPITULO = [("Abbas 8ª ed. cap. 4 (fagocitose e morte microbiana)", [
 ("l1", "Fagocitose e opsonização", ["ak-fagocitose", "sh-1791667096988"]), ("l2", "Burst e NO", ["sh-1791780361432", "sh-1791780362080"]),
 ("l3", "NK", "sh-1791984891454"), ("l4", "Macrófagos M1/M2", ["sh-1791625434032", "au-mreg"])])]
EXERCICIOS = [("Provas UC03 (índice imuno-05)", [
   ("p1", "Diferença entre resposta inata e adquirida (2024 P1 2.11)", ["ak-nk-inata", "sh-1791780341641"]),
   ("p2", "Anticorpos nas infecções virais: opsonização, ADCC (2017 P1 4.3)", ["sh-1791667096988", "sh-1791629596121"]),
   ("p3", "Fungo fagocitado induz CD8 (2017 P2 2.9)", "sh-1791625429957"),
   ("p4", "AIDS: mecanismo efetor comprometido na reativação (2016 P2 3.2)", ["sh-1791625430208", "sh-1791625422657"]),
   ("p5", "Neutrófilos nos tecidos: migração, fagocitose, burst, NETs (2015 P1 1.4)", ["sh-1791780359733", "sh-1791780361607", "sh-1791743344060"]),
   ("p6", "Complemento e opsonização (2015 P1 2.3)", "sh-1791667096988"),
   ("p7", "Anticorpos e outros efetores contra o HBV (2015 P2 2.6)", ["sh-1791629596121", "sh-1791984891827"]),
   ("p8", "Citotoxicidade do CD8: perforina e granzimas (2015 P2 2.7)", ["sh-1791593462592", "sh-1791625430882"]),
   ("p9", "Do fungo à ativação de linfócitos (2015 P2 3.3)", ["sh-1791625422657", "sh-1791625432733"]),
   ("p10", "Inibição de TAP pelo HHV-1 e as NK (2015 P2 7.2)", ["sh-1791984891454", "ak-nk-tumor"])])]
