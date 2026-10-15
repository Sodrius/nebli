"""Inventário atômico de Patologia da infecção viral (UC03 P3, Patologia; Ferraz da Silva; 29 lâminas), escrito antes da seleção (14/10).
Material de base lido inteiro: lâminas (visual/folha-01..05; imagens extraídas em img/raw), “transcrição” da turma (= texto das lâminas),
provas por termo (fontes/provas-pt61.txt; índice pat-09 vazio), monitoria P3 aula 9 (pp. 56–58), Robbins cap. 8 (pp. 343–344) e cap. 18
(pp. 853–861). Palavras-cruzadas da pasta da turma = da aula de Inflamação crônica (arquivo trocado): descartadas.
"""
PREFIXO = "pt61"
AULA = "Patologia da infecção viral (UC03 P3; Patologia; Ferraz da Silva)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Aspectos patológicos: biologia do vírus e padrão de resposta imune", [("a1", "Lesão pelo vírus e pela resposta imune", "a-dano-duplo")]),
 (3, "conteudo", "Efeitos dos vírus sobre a célula/tecido (lista)", [
   ("a2", "Lise celular", "b-efeitos"), ("a3", "Apoptose", "b-apoptose"), ("a4", "Bloqueio de síntese proteica", "b-sintese"),
   ("a5", "Formação de sincícios", "b-sincicio"), ("a6", "Despolimerização do citoesqueleto e interrupção do ciclo mitótico", "b-efeitos"),
   ("a7", "Transformação e proliferação celular", "b-efeitos")]),
 (4, "conteudo", "Efeitos agrupados: lise → inflamação aguda; efeito citopático; transformação → neoplasia", [
   ("a8", "Lise leva a inflamação aguda", "b-efeitos"), ("a9", "Efeito citopático (agrupamento)", "b-cpe"), ("a10", "Transformação leva a neoplasia", "b-efeitos")]),
 (5, "conteudo", "Efeito citopático: inclusão citoplasmática (raiva)", [("a11", "Inclusão por acúmulo de componentes virais", "b-inclusao"), ("a12", "Negri na raiva", "ak-negri")]),
 (6, "conteudo", "Efeito citopático: inclusão nuclear (sarampo)", [("a13", "Inclusão nuclear do sarampo", "b-sarampo")]),
 (7, "conteudo", "Efeito citopático: formação de sincícios", [("a14", "Sincício (imagem)", "b-sincicio"), ("a15", "Proteína de fusão", "ak-proteina-f")]),
 (8, "conteudo", "Efeito citopático: coilocitose", [("a16", "Coilócito do HPV", "ak-coilocito")]),
 (9, "conteudo", "Resposta: agudos → inata (barreiras, NK, macrófagos, complemento); subagudos/crônicos → adaptativa", [("a17", "Inata × adaptativa por fase", "c-resposta")]),
 (10, "conteudo", "Gráfico: cinética de vírus, IFN-I, NK, linfócitos T, anticorpos", [("a18", "Sequência temporal da resposta", "c-cinetica")]),
 (11, "conteudo", "Papel do interferon (célula infectada → vizinhas → proteínas antivirais)", [("a19", "IFN produzido pela célula infectada age nas vizinhas", "ak-ifn")]),
 (12, "conteudo", "Interferon: estado antiviral, ↑MHC-I, ativação de NK/Tc/macrófagos", [("a20", "Estado antiviral", "c-estado-antiviral"),
   ("a21", "Aumento de MHC-I", "ak-ifn-mhc"), ("a22", "Ativação de NK", "ak-ifn-nk")]),
 (13, "conteudo", "Célula NK: receptores ativador/inibidor, MHC-I, perforina e granzimas", [("a23", "Ausência de MHC-I", "ak-nk-mhc"),
   ("a24", "Equilíbrio de receptores", "ak-nk-mhc"), ("a25", "Perforina e granzimas", "ak-nk-perforina")]),
 (14, "conteudo", "HBV: estrutura (envelope, HBsAg, HBcAg, HBeAg, DNA polimerase)", [("a26", "HBsAg × HBcAg", "d-hbv-estrutura")]),
 (15, "conteudo", "HBV: ciclo (entrada, cccDNA, transcrição, montagem, transcrição reversa)", [("a27", "cccDNA", "d-cccdna"), ("a28", "Transcriptase reversa", "ak-hbv-rt")]),
 (16, "conteudo", "HBV: efeito citopático (vidro despolido)", [("a29", "Vidro despolido", "ak-vidro"), ("a30", "Causa: HBsAg acumulado", "d-vidro-hbsag")]),
 (17, "conteudo", "IHC HBsAg", [("a31", "Princípio da IHC", S(1791810364524)), ("a32", "Cor marrom (DAB)", S(1791810365149)), ("a33", "HBsAg citoplasmático", "d-ihc")]),
 (18, "conteudo", "IHC HBcAg", [("a34", "HBcAg nuclear", "d-ihc")]),
 (19, "conteudo", "Processo inflamatório crônico (agregado portal)", [("a35", "Infiltrado mononuclear portal", "e-portal")]),
 (20, "conteudo", "Fígado normal (zonas 1–3)", [("a36", "Trato portal", S(1791022170201)), ("a37", "Zonas do ácino", S(1791022170551))]),
 (21, "conteudo", "Lesão hepatocitária: necrose focal", [("a38", "Necrose do hepatócito", "ak-balonizacao")]),
 (22, "conteudo", "Lesão hepatocitária: necrose com infiltrado", [("a39", "Necrose com inflamação", "ak-balonizacao")]),
 (23, "conteudo", "Lesão hepatocitária: necrose extensa", [("a40", "Necrose em ponte", "ak-necrose-ponte")]),
 (24, "conteudo", "Lesão hepatocitária: indução de apoptose", [("a41", "Apoptose por CD8", S(1791625429957)), ("a42", "Corpúsculo de Councilman", "e-councilman")]),
 (25, "conteudo", "Distribuição da lesão (periportal)", [("a43", "Hepatite de interface", "e-interface")]),
 (26, "conteudo", "Perfil de resposta: linfócito B", [("a44", "B em agregados portais", "e-linfocito-b")]),
 (27, "conteudo", "Perfil de resposta: linfócito T CD8", [("a45", "CD8 como causa da lesão", "e-imunopatologia")]),
 (28, "conteudo", "Alteração arquitetural (reticulina): agressividade da resposta", [("a46", "Reticulina", S(1791022173275)), ("a47", "Septos e nódulos", "e-fibrose")]),
 (29, "conteudo", "Alteração arquitetural (tricrômico)", [("a48", "Tricrômico azul", S(1791810362575)), ("a49", "Fibrose em ponte", "e-fibrose"), ("a50", "Cirrose", S(1791022172624))]),
]
JUSTIFICATIVAS = {}
CAPITULO = [
 ("Robbins cap. 8, pp. 343–344 (mecanismos de lesão viral)", [
   ("l1", "Efeitos citopáticos diretos (bloqueio de síntese, apoptose)", ["b-sintese", "b-apoptose"]),
   ("l2", "Resposta imune antiviral lesa (CTL no HBV)", "e-imunopatologia"), ("l3", "Transformação", "b-efeitos"),
   ("l4", "Tropismo e receptores", EXC + "aula 59 Patogênese da infecção viral")]),
 ("Robbins cap. 18, pp. 853–861 (hepatite viral)", [
   ("l5", "Vidro despolido por HBsAg", "d-vidro-hbsag"), ("l6", "Balonização", "ak-balonizacao"), ("l7", "Apoptose por CD8", "e-councilman"),
   ("l8", "Necrose em ponte", "ak-necrose-ponte"), ("l9", "Hepatite de interface", "e-interface"), ("l10", "Fibrose em ponte e cirrose", ["e-fibrose", S(1791022172624)]),
   ("l11", "Esteatose no HCV", EXC + "a aula usa o HBV; caso de fronteira")]),
]
EXERCICIOS = [
 ("Provas UC03 (busca por termo; índice pat-09 vazio)", [
   ("p1", "2024 P3 1.2: efeito citopático por acúmulo de subunidades (inclusão)", ["b-cpe", "b-inclusao"]),
   ("p2", "2017 P3 1.3: célula gigante sincicial × de granuloma", ["b-sincicio", "b-sincicio-granuloma"]),
   ("p3", "2016 P3 1.2: coilocitose e HPV 16", ["ak-coilocito", "b-hpv16"]),
   ("p4", "2018 P3 1.7: reconhecimento viral, IFN-α/β, resposta e repercussões", ["ak-ifn", "e-imunopatologia"]),
   ("p5", "2017 P3 4.1: mononucleares no espaço porta", "e-portal")]),
 ("Monitoria P3 Patologia, aula 9", [
   ("m1", "Efeito citopático e inclusões", ["b-cpe", "b-inclusao"]), ("m2", "Vidro despolido e spill-over (interface)", ["ak-vidro", "e-interface"]),
   ("m3", "Vírus ausentes das lâminas atuais (CMV, HSV, EBV, adenovírus, VSR, influenza, zika, HIV, febre amarela)", EXC + "versão antiga da aula; casos de fronteira")]),
]
