"""Inventário atômico da 57 Princípios gerais dos vírus (UC03 P3; Microbiologia; Prof. Enrique Boccardo), escrito ANTES de escolher cards
(17/10, pipeline v4). Sequência = 127 lâminas: Propriedades Gerais dos Vírus I (1–73) e II (74–127, a mesma aula sem a parte de
história), vistas nesta sessão (io/g0..g10). O arquivo "Transcrição da Aula" da turma é só o texto das lâminas (conferido: idêntico),
sem fala do professor. Lido nesta sessão: provas (índice micro-13 e busca por Baltimore, capsídeo, envelope, nucleocapsídeo),
apostila UC3 e apostila guia de Micro (Estrutura viral, Classificação) e monitoria P3 de Micro.
"""
PREFIXO = "mb57"
AULA = "Princípios gerais dos vírus (UC03 P3; Microbiologia; Prof. Enrique Boccardo)"
EXC = "EXC: "

_F, _L = "figura", "logistica"
_HIST = EXC + "história e curiosidades sem cobrança (FORA_DO_RECORTE)"
PARTE_I = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Fatos interessantes: nuvem de vírus, genomas virais no nosso genoma, massa dos fagos", [("a1", "Curiosidades", _HIST)]),
 (3, _F, "Vírus nos oceanos e no corpo; genomas de HIV no planeta", []),
 (4, "conteudo", "Mortes por causa no mundo (2019)", [("a2", "Infecções virais entre as causas", _HIST)]),
 (5, _F, "Mortes em crianças < 5 anos", []),
 (6, "conteudo", "COVID-19: ~7 milhões de mortes", [("a3", "Pandemia", _HIST)]),
 (7, "conteudo", "Panorama das infecções virais por órgão", [("a4", "Vírus por sistema", EXC + "panorama clínico das aulas de patologia/infectologia")]),
 (8, _L, "Divisória: história", []),
 (9, "conteudo", "Estela egípcia com poliomielite (3700 a.C.)", [("a5", "Poliomielite antiga", _HIST)]),
 (10, "conteudo", "Faraó Siptah: pé equino da poliomielite", [("a6", "Poliomielite antiga", _HIST)]),
 (11, "conteudo", "Ramsés V: varíola", [("a7", "Varíola antiga", _HIST)]),
 (12, "conteudo", "Koch e Pasteur: teoria dos germes", [("a8", "Teoria dos germes", "sh-1791746115401")]),
 (13, "conteudo", "Postulados de Koch", [("a9", "Quatro postulados", "sh-1791746115401")]),
 (14, "conteudo", "Adolf Mayer: mosaico do tabaco transmissível", [("a10", "Mosaico do tabaco", _HIST)]),
 (15, "conteudo", "Iwanowski e Beijerinck: agente filtrável (contagium vivum fluidum)", [("a11", "Vírus passa pelo filtro", "sh-1791666344216")]),
 (16, _F, "Folhas com mosaico", []),
 (17, _F, "Tulipas com variegação", []),
 (18, "conteudo", "Loeffler e Frosch: febre aftosa", [("a12", "Vírus em animais", _HIST)]),
 (19, _F, "Texto sobre Loeffler e Frosch", []),
 (20, "conteudo", "Twort e d'Herelle: bacteriófagos", [("a13", "Bacteriófago", "ak-fago")]),
 (21, "conteudo", "Definição: parasitas submicroscópicos intracelulares obrigatórios; montados, não crescem",
  [("a14", "Montagem a partir de componentes", "au-definicao"), ("a15", "Sem metabolismo próprio", "ak-sem-metabolismo"), ("a16", "Submicroscópicos", "sh-1791576666292")]),
 (22, "conteudo", "Tabela vírus × bactéria × Mycoplasma × Rickettsia × Chlamydia (vazia)", [("a17", "Critérios de comparação", "au-definicao")]),
 (23, "conteudo", "Tabela: bactéria típica", [("a18", "Bactéria: tudo sim, insensível a interferon", "ak-interferon")]),
 (24, "conteudo", "Tabela: Mycoplasma (sem ácido murâmico)", [("a19", "Sem parede", "sh-1791576675192")]),
 (25, "conteudo", "Tabela: Rickettsia (não cresce em meio artificial)", [("a20", "Intracelular obrigatória", ["ak-rickettsia", "ak-rickettsia-coa"])]),
 (26, "conteudo", "Tabela: Chlamydia (sem ATP, sem ácido murâmico)", [("a21", "Sem ATP", "ak-chlamydia-atp"), ("a22", "Coram mal", "sh-1791576673916")]),
 (27, "conteudo", "Tabela: vírus (sensível a interferon, passa no filtro)", [("a23", "Interferon", "ak-interferon"), ("a24", "Filtro", "sh-1791666344216")]),
 (28, "conteudo", "Dois sistemas de classificação", [("a25", "Hierárquico e Baltimore", ["au-hierarquico", "au-baltimore"])]),
 (29, "conteudo", "Sistema hierárquico (Lwoff, 1962)", [("a26", "Pelas características do vírus", "au-hierarquico")]),
 (30, "conteudo", "Quatro características: ácido nucleico, simetria, envelope, dimensões", [("a27", "Quatro critérios", "au-hierarquico")]),
 (31, _F, "Famílias de RNA (Harrison)", []),
 (32, _F, "Famílias de RNA segmentado e retrovírus", []),
 (33, _F, "Famílias de DNA", []),
 (34, _F, "Ordem → família → gênero → espécie", []),
 (35, "conteudo", "ICTV", [("a28", "Taxonomia oficial", EXC + "taxonomia do ICTV (FORA_DO_RECORTE)")]),
 (36, _F, "Site do ICTV", []),
 (37, _F, "Código do ICTV", []),
 (38, "conteudo", "Sistema de Baltimore: todo vírus produz mRNA", [("a29", "Caminho até o mRNA", "au-baltimore")]),
 (39, "conteudo", "Grupos I–VII", [("a30", "Polaridade", ["ak-polaridade", "ak-rna-mrna", "ak-rna-mais-uso"]), ("a31", "RNA negativo", ["ak-rna-menos", "ak-rna-menos-pol", "ak-rna-menos-infec"]),
  ("a32", "Transcrição reversa", "ak-transcricao-reversa")]),
 (40, "conteudo", "Esquema de Baltimore", [("a33", "Grupos convergem no mRNA", "au-baltimore")]),
 (41, _F, "Critérios × famílias de DNA", []),
 (42, _F, "Critérios × famílias de RNA", []),
 (43, _L, "Divisória: estrutura viral", []),
 (44, "conteudo", "Tamanho relativo: bactéria, Chlamydia, pox, herpes, influenza, polio", [("a34", "20–300 nm", "sh-1791576666292"), ("a35", "Poxvírus o maior", "ak-pox-maior")]),
 (45, _F, "Tamanho relativo (escala)", []),
 (46, "conteudo", "Tamanho dos vírus de DNA (ME)", [("a36", "Parvovírus o menor", "ak-parvo-menor")]),
 (47, _F, "Vírus de RNA (+) na ME", []),
 (48, _F, "Vírus de RNA (−) na ME", []),
 (49, _F, "Tamanho de vírus humanos (ViralZone)", []),
 (50, _F, "Vírus gigantes", []),
 (51, "conteudo", "Componentes: genoma, capsídeo, nucleocapsídeo, simetria, envelope", [("a37", "Nucleocapsídeo", "au-nucleocapsideo"), ("a38", "DNA ou RNA no capsídeo", "ak-capsideo"),
  ("a39", "Envelope da célula", "ak-envelope")]),
 (52, "conteudo", "O genoma garante replicação, empacotamento, alteração da célula", [("a40", "Funções do genoma", "au-definicao")]),
 (53, "conteudo", "Simples/dupla fita, circular, +/−, segmentado", [("a41", "DNA dupla fita", ["ak-dna-genoma", "ak-parvo-ss"]), ("a42", "RNA fita simples", ["ak-rna-ss", "ak-reo-ds"]),
  ("a43", "Segmentado", "ak-segmentado")]),
 (54, "conteudo", "Cinco estruturas básicas com exemplos", [("a44", "Cinco estruturas", "au-estruturas"), ("a45", "Nu = icosaédrico", "ak-nus-icosa"), ("a46", "Envelopado: ambos", "ak-envelopados-forma"),
  ("a47", "Icosaédrico ou helicoidal", "ak-formas")]),
 (55, "conteudo", "Cinco tipos de simetria (esquema)", [("a48", "Esquema", "au-estruturas")]),
 (56, _F, "TMV, adenovírus, influenza, fago T4", []),
 (57, "conteudo", "Simetria icosaédrica", [("a49", "Icosaedro", "ak-formas")]),
 (58, _F, "Capsídeos icosaédricos", []),
 (59, "conteudo", "Simetria helicoidal (TMV, VSV)", [("a50", "Hélice", "ak-formas")]),
 (60, _F, "Ebola helicoidal", []),
 (61, "conteudo", "Helicoidal envelopado (influenza)", [("a51", "RNA − helicoidais", "ak-helicoidais-menos")]),
 (62, _F, "Vírus da raiva", []),
 (63, "conteudo", "Simetria complexa: fago T e poxvírus", [("a52", "Poxvírus", ["ak-pox-dna", "ak-pox-tijolo"])]),
 (64, "conteudo", "Poxvírus: membranas, core, enzimas", [("a53", "Core em halter", "ak-pox-halter"), ("a54", "Envelope próprio", "ak-pox-envelope")]),
 (65, "conteudo", "Outros componentes: hemaglutinina, neuraminidase, RNA polimerase", [("a55", "HA e NA", ["ak-ha", "ak-na"]), ("a56", "Polimerase", "ak-rna-menos-pol")]),
 (66, "conteudo", "HIV: gp120, gp41, p24, p17, transcriptase reversa, integrase, protease", [("a57", "Componentes do HIV", ["ak-hiv-p24", "ak-hiv-env", "ak-hiv-pol"])]),
 (67, "conteudo", "Envelope viral (ME)", [("a58", "Glicoproteínas", "ak-glicoproteinas"), ("a59", "Sensível a solventes", ["ak-alcool", "sh-1791666340816"]),
  ("a60", "Nu × envelopado", ["au-nu", "sh-1791666340691"])]),
 (68, "conteudo", "Envelope adquirido por brotamento", [("a61", "Brotamento", "ak-envelope")]),
 (69, _F, "Tabela de vírus humanos (família, genoma, capsídeo, envelope)", []),
 (70, "conteudo", "Resumo: ácido nucleico e estrutura do vírion", [("a62", "RNA como mRNA", "ak-rna-mrna"), ("a63", "Retrovírus diploide", "ak-retro-diploide")]),
 (71, _F, "Esquemas de vírions", []),
 (72, "conteudo", "Resumo geral", [("a64", "Partícula para transmissão", "au-definicao")]),
 (73, _L, "Agradecimento", []),
]
_ESPELHO = {74: 2, 75: 3, 76: 3, 77: 7, 78: 21, 125: 70, 126: 72, 127: 73}
_ESPELHO.update({79 + i: 22 + i for i in range(6)})       # 79–84 ↔ 22–27
_ESPELHO.update({85 + i: 28 + i for i in range(15)})      # 85–99 ↔ 28–42
_ESPELHO.update({100 + i: 43 + i for i in range(6)})      # 100–105 ↔ 43–48
_ESPELHO.update({106 + i: 51 + i for i in range(19)})     # 106–124 ↔ 51–69
_I = {s[0]: s for s in PARTE_I}
PARTE_II = []
for _n in range(74, 128):
    _o = _I[_ESPELHO[_n]]
    _tipo = "figura" if _o[1] == "figura" else ("logistica" if _o[1] in ("logistica", "capa") else _o[1])
    PARTE_II.append((_n, _tipo, _o[2] + f" (repete a lâmina {_o[0]})", [(f"b{_n}-{k}", t, c) for k, t, c in _o[3]]))
SLIDES = PARTE_I + PARTE_II
JUSTIFICATIVAS = {"capa": "capa sem conteúdo", "figura": "figura ou tabela de exemplo; o conceito está na lâmina de texto vizinha",
                  "logistica": "divisória, agradecimento ou repetição"}
CAPITULO = [("Apostila UC3 e apostila guia de Micro (Estrutura e classificação dos vírus)", [
 ("l1", "Parasitas intracelulares obrigatórios", "au-definicao"),
 ("l2", "Capsídeo, nucleocapsídeo, envelope", ["au-nucleocapsideo", "ak-envelope"]),
 ("l3", "Simetrias icosaédrica, helicoidal e complexa", ["ak-formas", "au-estruturas"]),
 ("l4", "Baltimore", "au-baltimore")])]
EXERCICIOS = [
 ("Provas UC03 (índice micro-13 e busca por termo)", [
   ("p1", "Por que um vírus fecal-oral não é envelopado (2025 P3 2.3)", "au-nu"),
   ("p2", "Estrutura → via de transmissão (2024 P3 1.5; 2019 P3 3.2)", ["au-nu", "sh-1791666340816"]),
   ("p3", "Importância do envelope (2018 P3 5.2)", "ak-glicoproteinas"),
   ("p4", "Simetria e envoltório na ME (2015 P2 4.1)", "ak-envelopados-forma"),
   ("p5", "Sensibilidade ao éter e detergentes: envelope (2015 P2 4.2)", ["ak-alcool", "au-nucleocapsideo"]),
   ("p6", "Espículas: glicoproteínas do envelope que reconhecem receptores (2015 P2 4.4)", "ak-glicoproteinas"),
   ("p7", "Genoma RNA fita simples positivo (2015 P2 4.5)", "ak-polaridade"),
   ("p8", "Grupo de Baltimore (2018 P3 1.3; 2015 P2 2.3)", "au-baltimore")]),
]
