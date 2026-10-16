"""Inventário atômico de Diagnóstico patológico — Ferramentas do diagnóstico patológico (UC03 P1; Patologia; Prof. Luiz F. Ferraz da Silva),
escrito ANTES da seleção (16/10, pipeline AnKing-primeiro v2). 31 lâminas (fontes/slides.pdf). Lido nesta corrida: lâminas, transcrição
integral, apostila guia de Patologia (Aula 1), UC3.pdf (Ferramentas de Diagnóstico Patológico), monitoria P1 (aula suprimida), provas pat-01
(30 subquestões; quase todas “eco” de outras aulas), palavras-cruzadas com gabarito, Robbins cap. 1 (introdução; confirma).
Aula introdutória: etiologia/patogênese/infarto/aterosclerose têm aulas próprias; aqui fica a ferramenta e o modelo geral da doença.
"""
PREFIXO = "pt03"
AULA = "Diagnóstico patológico (UC03 P1; Patologia; Ferraz da Silva)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Patologia: alterações estruturais, bioquímicas e funcionais", [("a1", "Três tipos de alteração", "au-sequencia-doenca")]),
 (3, "conteudo", "Etiologia → patogênese → alterações morfológicas e funcionais → manifestações clínicas", [("a2", "Sequência do processo de doença", "au-sequencia-doenca")]),
 (4, "conteudo", "Etiologia: o que causa; genéticos e adquiridos; única ou múltipla", [("a3", "Etiologia", "au-etiologia")]),
 (5, "conteudo", "Patogênese: como; mecanismos genéticos e bioquímicos; importância médica", [("a4", "Patogênese", "au-patogenese")]),
 (6, "conteudo", "Cigarro, dieta, DNA (ilustração)", [("a5", "Exemplos", EXC + "ilustração de causas adquiridas e genéticas")]),
 (7, "conteudo", "Patogênese da aterosclerose (esquema)", [("a6", "Aterosclerose", EXC + "aula própria (hemostasia/aterosclerose)")]),
 (8, "conteudo", "Alterações morfológicas: secundárias; macro, micro, ultraestrutura; presença e grau; primeira detecção", [("a7", "Níveis e grau", "au-morfologia")]),
 (9, "conteudo", "Infarto agudo, subagudo e cicatrizado", [("a8", "Idades do infarto", EXC + "aula 69 (infarto)")]),
 (10, "conteudo", "Trombo coronariano na TC e na peça", [("a9", "Exemplo", EXC + "aula 69 (infarto)")]),
 (11, "conteudo", "Manifestações clínicas: como a doença aparece à beira do leito", [("a10", "Manifestações", "au-sequencia-doenca")]),
 (12, "conteudo", "Fluxograma clínico (febre reumática → IC)", [("a11", "Raciocínio em fluxograma", EXC + "exemplo de raciocínio; cardiologia")]),
 (13, "conteudo", "Patologia geral × de órgãos e sistemas", [("a12", "Divisão da patologia", "au-patologia-geral")]),
 (14, "conteudo", "Patologia na assistência: autópsia, cirúrgica, citopatologia, clínica, forense", [("a13", "Áreas", "au-areas")]),
 (15, "conteudo", "Ferramentas: HE, ME, histoquímica, imuno-histoquímica/imunofluorescência, molecular", [("a14", "Ferramentas e o que mostram", "au-ferramentas")]),
 (16, "conteudo", "Macroscopia: fresco ou fixado, pesos, cortes, fotografia, representação", [("a15", "Fixação e representação", "au-macroscopia")]),
 (17, "conteudo", "Macroscopia (fotos)", [("a16", "Cassete", "au-processamento")]),
 (18, "conteudo", "Processamento: processador, blocos de parafina", [("a17", "Parafina", "au-processamento")]),
 (19, "conteudo", "Processamento: micrótomo, lâminas, HE", [("a18", "Micrótomo", "au-processamento")]),
 (20, "conteudo", "Interação patologia–radiologia: punção guiada por US", [("a19", "Punção aspirativa por agulha fina", "ak-faf")]),
 (21, "conteudo", "Esfregaço em monocamada", [("a20", "Esfregaço", "ak-faf")]),
 (22, "conteudo", "Olho e cérebro (ilustração)", [("a21", "Metáfora", EXC + "ilustração")]),
 (23, "conteudo", "HE: principal método, rápido, núcleo × citoplasma", [("a22", "HE", "au-he")]),
 (24, "conteudo", "Microscopia eletrônica: poucos centros, seleção prévia, doenças específicas", [("a23", "ME e discinesia ciliar", "au-me")]),
 (25, "conteudo", "Histoquímica: colágeno, fibra elástica, membrana basal", [("a24", "Masson e colágeno", EXC + "“não quero que vocês decorem isso”; no Extra do PAS"), ("a25", "PAS", "ak-pas"),
   ("a26", "Picro-Sirius, Verhoeff, resorcina-fucsina", EXC + "o professor: “não quero que vocês decorem isso”; ficam no Extra")]),
 (26, "conteudo", "Histoquímica: microrganismos (BH, Grocott, Ziehl)", [("a27", "Ziehl-Neelsen", "sh-1791576674292"), ("a28", "Prata para fungos", "ak-prata")]),
 (27, "conteudo", "Histoquímica: muco, gordura, ferro, melanina", [("a29", "Ferro: Prussian blue (Perls)", "ak-ferro"), ("a30", "Gordura: Oil Red O", "ak-oilred"),
   ("a31", "Alcian blue, Fontana-Masson", EXC + "“não quero que vocês decorem isso”")]),
 (28, "conteudo", "Imuno-histoquímica: +24 h; anticorpo primário e secundário; DAB", [("a32", "Princípio da IHQ", "au-ihq")]),
 (29, "conteudo", "IHQ: padrão de localização (núcleo × membrana)", [("a33", "Localização", "au-ihq"), ("a34", "Origem do tumor (PSA)", ["ak-ihq-tumor", "ak-psa"])]),
 (30, "conteudo", "Imunofluorescência", [("a35", "IF", "au-if")]),
 (31, "conteudo", "Testes moleculares: PCR, hibridização in situ", [("a36", "FISH", "ak-fish"), ("a37", "Terapia-alvo", "au-molecular")]),
]
JUSTIFICATIVAS = {}
CAPITULO = [("Robbins cap. 1 (introdução à patologia; confirma)", [
 ("l1", "Etiologia, patogenia, alterações morfológicas, manifestações", ["au-sequencia-doenca", "au-etiologia", "au-patogenese"]),
 ("l2", "Patologia geral × sistêmica", "au-patologia-geral")])]
EXERCICIOS = [
 ("Provas UC03 (pat-01)", [
   ("p1", "2018 P4 1.3 e 2015 P3sub 2.2: IHQ e caracterização molecular guiam a terapia", ["au-ihq", "au-molecular"]),
   ("p2", "2019 P3 1.5: marcadores imuno-histoquímicos numa autópsia", "au-ihq")]),
 ("Palavras-cruzadas da aula (gabarito)", [
   ("x1", "Punção aspirativa por agulha fina", "ak-faf"), ("x2", "HE", "au-he"), ("x3", "Congelação (intraoperatório)", "au-congelacao"),
   ("x4", "Imunofluorescência (pele e rim)", "au-if"), ("x5", "Papanicolau", "ak-faf"), ("x6", "Patogênese", "au-patogenese"),
   ("x7", "Etiologia; agente etiológico", "au-etiologia"), ("x8", "Patologia molecular", "au-molecular"), ("x9", "Histoquímica", "au-ferramentas"),
   ("x10", "Biópsia; biópsia por agulha grossa (core)", EXC + "termo citado só nas cruzadas"), ("x11", "Imuno-histoquímica na linhagem dos tumores", "ak-psa"),
   ("x12", "Autópsia: monobloco, Virchow, SVOC, controle de qualidade", EXC + "autópsia em detalhe: aula 14 (declaração de óbito)")]),
 ("Apostila guia de Patologia, Aula 1", [("ap1", "Ferramentas complementares", "au-ferramentas"), ("ap2", "Autópsia: funções e declínio", EXC + "aula 14")]),
 ("UC3.pdf, Ferramentas de Diagnóstico Patológico", [("u1", "Etiologia/patogênese; macroscopia; HE; ME; histoquímica", ["au-sequencia-doenca", "au-macroscopia", "au-he"])]),
 ("Monitoria P1", [("m1", "Aula suprimida pelos monitores", EXC + "sem conteúdo desta aula")]),
]
