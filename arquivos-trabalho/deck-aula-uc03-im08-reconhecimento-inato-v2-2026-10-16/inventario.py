"""Inventário atômico de Reconhecimento inato no sistema imune (UC03 P1; Imunologia; Barbuto), escrito ANTES de escolher cards
(16/10, pipeline v4). Sequência = 23 lâminas (fontes/slides.pdf = turma III = pasta pessoal), vistas inteiras nesta sessão (io/g0..g2).
Lido nesta sessão: transcrição integral (44 pp.), provas im02, apostila guia de Imunologia, monitoria P1 e mapa imunológico, UC3
(texto da corrida antiga), Abbas Básica cap. 2 (receptores). Lâminas I e II da turma conferidas (mesmo conteúdo).
Fronteira (MEMORY §3): PRR, DAMP, TLR4/CD14, TLR endossomais, inflamassoma, IFN tipo I, citotoxicidade, fagocitose, febre e
mediadores lipídicos já têm cópias NEBLI das aulas 37/38, 61, 45, 31 e 51 → sh(). Inata × adaptativa (memória, especificidade,
rapidez, diversidade, barreira física) fica na 07; aqui ficam as células e barreiras químicas/fisiológicas da imunidade inata.
"""
PREFIXO = "im08"
AULA = "Reconhecimento inato no sistema imune (UC03 P1; Imunologia)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Objetivos: PRR, famílias e TLR, vias, citocinas e quimiocinas", [("a1", "Objetivos", EXC + "lista de objetivos; cada um vira cards nas lâminas seguintes")]),
 (3, "conteudo", "Recapitulando: repertório completo, gerado ao acaso, com seleção; respostas diferentes", [("a2", "Recapitulação da 07", EXC + "recapitula a aula 07 (seleção e repertório: cards de lá)")]),
 (4, "conteudo", "Seleção nos órgãos linfoides primários: próprio × não próprio", [("a3", "Recapitulação", EXC + "recapitula a aula 07")]),
 (5, "conteudo", "Resposta × tolerância, ambas com memória; estado homeostático do tecido decide", [("a4", "Recapitulação", EXC + "recapitula a aula 07 (au-tolerancia)")]),
 (6, "conteudo", "Reconhecimento hierárquico: PRR (inata, padrões) × receptores clonais (adquirida, antígenos)", [
   ("a5", "PRR reconhecem padrões moleculares", ["sh-1791780342851", "ak-prr-ligantes"]), ("a6", "Células da imunidade inata", ["ak-inata-macrofagos", "ak-inata-neutrofilos", "ak-inata-nk"])]),
 (7, "conteudo", "Ponte inata-adquirida: APC captura, processa, apresenta", [("a7", "DC como ponte", EXC + "apresentação de antígeno é da 07 e da 20 (sh lá)")]),
 (8, "conteudo", "Famílias de PRR e localização (CLR, scavenger, TLR, NLR, RLR, ALR); DAMP × PAMP", [
   ("a8", "PRR em todos os compartimentos", "au-prr-locais"), ("a9", "DAMPs do tecido lesado", "sh-1791743340457"),
   ("a10", "NOD e RIG no citoplasma", "sh-1791743340159"), ("a11", "Dectina-1 reconhece β-glucana", "sh-1791743340332"), ("a12", "TLR em células inatas e adaptativas", "ak-tlr-ambas")]),
 (9, "conteudo", "Da sinalização à efetuação: IFN tipo I, citotoxicidade, fagocitose, mediadores; febre", [
   ("a13", "Febre é defesa", "au-febre-defesa"), ("a14", "Barreiras químicas e fisiológicas", ["ak-barreira-quimica", "ak-barreira-fisiologica"]),
   ("a15", "Resistência inata atravessa gerações", "ak-inata-geracoes")]),
 (10, "conteudo", "IFN: ação solidária da célula infectada; efeitos sistêmicos", [
   ("a16", "IFN α/β protegem as vizinhas", ["sh-1791984890453", "sh-1791984890700"]), ("a17", "Vírus induzem IFN por sensores citosólicos", "ak-virus-ifn"),
   ("a18", "IFN aumenta MHC I e ativa NK", ["sh-1791984890952", "sh-1791984891204"])]),
 (11, "conteudo", "Citotoxicidade: suicídio induzido; grânulos ou Fas-FasL; apoptose", [
   ("a19", "Perforina e granzima", ["sh-1791984891827", "sh-1791593462592"]), ("a20", "FasL–Fas", "sh-1791625430882")]),
 (12, "conteudo", "Fagocitose em etapas: quimiotaxia, opsonização, zíper, fagossomo, lisossomo, explosão respiratória", [
   ("a21", "Etapas da fagocitose", "sh-1791780361006"), ("a22", "Opsoninas C3b e IgG", "sh-1791667096988"),
   ("a23", "Explosão respiratória", ["ak-explosao", "sh-1791743343758"])]),
 (13, "conteudo", "Mediadores: citocinas pleiotrópicas (IL, GF/CSF, IFN, quimiocinas), lipídicos, exossomos", [
   ("a24", "Citocinas são pleiotrópicas", "au-pleiotropia"), ("a25", "Mediadores lipídicos do ácido araquidônico", ["sh-1791743344682", "sh-1791743345233"])]),
 (14, "conteudo", "Exemplos: IL-1…IL-17, G-CSF, GM-CSF, TNF, IFN tipo I e II, quimiocinas", [
   ("a26", "IL-6 e fase aguda; anti-IL-6", ["sh-1791743347558", "ak-tocilizumabe"]), ("a27", "G-CSF como remédio", ["ak-filgrastim", "ak-gcsf-neutropenia"])]),
 (15, "conteudo", "Paul Ehrlich, Nobel 1908: química da célula e remédio racional", [("a28", "Citação", EXC + "citação histórica")]),
 (16, "conteudo", "Ligantes dos TLR (TLR1–11, localização, origem)", [
   ("a29", "TLR4 + CD14 reconhecem LPS", "sh-1791743339358"), ("a30", "TLR de ácidos nucleicos nos endossomos", "sh-1791743339982"),
   ("a31", "Imiquimode ativa TLR7", "ak-imiquimode")]),
 (17, "conteudo", "Ligantes de RLR, NLR (NOD1/2) e CLR (dectina)", [("a32", "NOD2 e Crohn", "ak-nod2-crohn"), ("a33", "NOD/RIG", "sh-1791743340159")]),
 (18, "conteudo", "Vias dos TLR: MyD88 → NF-κB/AP-1 (citocinas); TRIF → IRF (IFN tipo I); AKT, caspase 8, inflamassoma", [
   ("a34", "MyD88 × TRIF", "au-myd88-trif"), ("a35", "TLR ativa NF-κB", ["au-myd88-trif", "ak-ikb"])]),
 (19, "conteudo", "Figura de vias dos TLR (Gay 2014)", [("a36", "Vias se cruzam", "au-myd88-trif")]),
 (20, "conteudo", "Inflamassoma: NLR forma plataforma → caspase-1 → IL-1β e IL-18; doenças inflamatórias hereditárias", [
   ("a37", "Inflamassoma", ["sh-1791743339740", "sh-1791743339860", "sh-1791780343453"]), ("a38", "Piroptose", "sh-1791780343873"),
   ("a39", "Doenças autoinflamatórias", "sh-1792166997617")]),
 (21, "conteudo", "Ativação do NLRP3: sinais de perigo, montagem, caspase, clivagem da pró-IL-1β", [
   ("a40", "Dois sinais para liberar IL-1β", "au-inflamassoma-sinais"), ("a41", "Cristais de urato ativam NLRP3", "sh-1791743340632")]),
 (22, "conteudo", "Em resumo: produtos armazenados, modificados, produzidos após ativação, degradação; plasticidade", [
   ("a42", "IL-1 e febre", ["sh-1791743347261", "sh-1791743347433", "ak-pirogenos"]), ("a43", "PGE2 na febre", "sh-1791743344934")]),
 (23, "conteudo", "Leitura complementar", [("a44", "Referências", EXC + "artigos de leitura complementar")]),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo"}
CAPITULO = [("Abbas Básica cap. 2 (receptores da imunidade inata) (confirma)", [
 ("l1", "TLR, NLR, RLR, CLR e localização", ["au-prr-locais", "sh-1791743339982", "sh-1791743340159"]),
 ("l2", "Inflamassoma e IL-1", ["sh-1791743339740", "sh-1791780343453"]), ("l3", "IFN tipo I", "sh-1791984890453")])]
EXERCICIOS = [
 ("Provas UC03 (índice im02)", [
   ("p1", "Como bacilos/microrganismos são reconhecidos pelas células inatas: PRR, TLR (2017 P1 1.8 e 3.4; 2015 P1 1.2)", ["sh-1791780342851", "ak-prr-ligantes", "au-myd88-trif"]),
   ("p2", "Destruição celular do infarto e inflamação: DAMPs (2017 P1 2.5)", "sh-1791743340457"),
   ("p3", "Imunidade inata antiviral: IFN e NK (2025 P3 2.5; 2019 P1 3.2; 2016 P2 1.1; 2015 P2sub 2.1)", ["sh-1791984890453", "sh-1791984891827", "ak-virus-ifn"]),
   ("p4", "Por que a inata não gera memória; primeira linha (2024 P2 2.1–2.2)", ["ak-barreira-quimica", "ak-inata-macrofagos"]),
   ("p5", "Neutrófilos no tecido: fagocitose e explosão respiratória (2015 P1sub 1.4)", ["sh-1791780361006", "ak-explosao"]),
   ("p6", "Imunidade treinada pelo BCG (2025 P2 7.1)", "ak-inata-macrofagos")]),
 ("Monitoria P1 (aula 2) e mapa imunológico", [("m1", "PRR, PAMP, DAMP, TLR, inflamassoma", ["sh-1791780342851", "sh-1791743339740"]),
   ("m2", "Citocinas e febre", ["au-pleiotropia", "sh-1791743347261"])]),
]
