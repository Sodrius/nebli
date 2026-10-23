"""Inventário atômico da 46 Expressão gênica em eucariotos I (UC03 P3; Biologia Molecular; Prof. Alexandre Bruni Cardoso; 39 lâminas), escrito em
23/10 (refação v8) a partir do material lido: as 39 lâminas vistas em visual/folha-01..07 (e o Ib com os extras 40–42), a fala inteira (anotações
do PDF da turma, versão Ia), provas, exercícios Q1–3 e Alberts cap. 7. Destinos preenchidos depois da busca (E4).
"""
PREFIXO = "bm46"
AULA = "Expressão gênica em eucariotos I (UC03 P3; Biologia Molecular; Prof. Alexandre Bruni Cardoso)"
EXC = "EXC: "
_C = "conteudo"
D = {}  # item do mapa → chaves dos cards (preenchido depois da busca)

def _d(k):
    v = D.get(k, [])
    return v if len(v) != 1 else v[0]

SLIDES = [
 (1, "capa", "Capa", []),
 (2, _C, "Regulação em eucariotos: fígado e neurônio", [("2a", "Mesmo genoma, genes diferentes por célula", _d("p1-2"))]),
 (3, _C, "O genoma é o mesmo; o que muda é o conjunto de genes expressos", [("3a", "O que muda é o conjunto de genes expressos", _d("p1-2"))]),
 (4, _C, "Níveis de regulação; a iniciação é a mais importante", [("4a", "Regulação em vários níveis, sobretudo na iniciação", _d("p1-2"))]),
 (5, _C, "Uma célula expressa 30–60% dos genes", [("5a", "Nível de expressão varia por célula", _d("p1-1"))]),
 (6, "logistica", "Objetivos da aula", []),
 (7, _C, "Por que regular: energia, ambiente, diferenciação", [("7a", "Economia, resposta ao ambiente e diferenciação", _d("p1-2"))]),
 (8, _C, "Genes constitutivos × regulados", [("8a", "Housekeeping × regulado", _d("p1-1"))]),
 (9, _C, "Procarioto × eucarioto", [("9a", "Ativador indireto, cromatina, dezenas de fatores", _d("p2-1")), ("9b", "Cromatina reprime", _d("p2-2")), ("9c", "Alças levam sequências distantes", _d("p2-3"))]),
 (10, _C, "Maquinaria eucariótica é mais complexa", [("10a", "Pol II + GTFs + Mediador × cerne + sigma", _d("p2-1"))]),
 (11, _C, "Regiões regulatórias mais extensas", [("11a", "Enhancers e elementos regulatórios", _d("p4-1")), ("11b", "Alça de DNA", _d("p4-2"))]),
 (12, _C, "Fatores gerais × específicos", [("12a", "Gerais necessários, específicos regulam", _d("p3-1"))]),
 (13, _C, "Promotor da Pol II", [("13a", "TBP/TFIID reconhece o TATA", _d("p3-2"))]),
 (14, _C, "Estrutura de um enhancer", [("14a", "Enhancer com vários sítios, à distância", _d("p4-1"))]),
 (15, _C, "Um enhancer, vários genes; um gene, vários enhancers", [("15a", "Enhancers múltiplos", _d("p4-1"))]),
 (16, _C, "Ativadores em sinergia", [("16a", "Sinergia e integração de sinal", _d("p5-1")), ("16b", "Especificidade por combinação", _d("p5-2"))]),
 (17, _C, "Alça, Mediador e modificadores de cromatina", [("17a", "Ativador contata Mediador e gerais, nunca a Pol II", _d("p2-1")), ("17b", "Mediador integra sinais e é coativador", _d("p5-3")), ("17c", "Recrutamento × alosteria", _d("p6-1")), ("17d", "Repressores", _d("p6-2"))]),
 (18, "logistica", "Sistema Gal: universalidade e modularidade", []),
 (19, _C, "O sistema Gal", [("19a", "Gal4 governa genes de galactose", _d("p7-1"))]),
 (20, _C, "Gal4 e os sítios UAS", [("20a", "1–4 sítios UAS", _d("p7-1"))]),
 (21, _C, "Domínios de ligação e de ativação", [("21a", "Funções em domínios separados", _d("p7-1")), ("21b", "Ligação tudo ou nada, ativação incremental", _d("p6-3"))]),
 (22, _C, "O que o domínio de ativação faz", [("22a", "Liga TFIID, Mediador e modificadores de cromatina", _d("p7-1"))]),
 (23, _C, "Universalidade da ativação", [("23a", "Gal4 ativa em outras células", _d("p7-2"))]),
 (24, _C, "Universalidade: promotor com TATA e UAS", [("24a", "Reporter UAS-TATA", _d("p7-2"))]),
 (25, "fora_do_recorte", "UAS:GFP em mosca, peixe e planta", []),
 (26, _C, "Interface ativador–maquinaria conservada", [("26a", "Interface conservada", _d("p7-2"))]),
 (27, _C, "Modularidade dos fatores", [("27a", "Módulos independentes", _d("p7-3"))]),
 (28, _C, "Dois experimentos de modularidade", [("28a", "Gal4 sem ativação; LexA-Gal4", _d("p7-3"))]),
 (29, "logistica", "Como sinais afetam a expressão", []),
 (30, _C, "Em bactéria o sinal liga direto ao fator", [("30a", "Sinal direto na bactéria", _d("p8-1"))]),
 (31, _C, "Sete maneiras de regular a atividade do fator", [("31a", "Ligante, modificação, desmascaramento, entrada no núcleo", _d("p8-1"))]),
 (32, _C, "Hormônios lipofílicos ligam receptores nucleares", [("32a", "Esteroides cruzam a membrana", _d("p8-3"))]),
 (33, _C, "Receptores nucleares são ativadores dependentes do hormônio", [("33a", "Receptor só liga o DNA com hormônio; dedo de zinco", _d("p8-3"))]),
 (34, _C, "Regulação por esteroide e receptor nuclear", [("34a", "Ciclo do receptor", _d("p8-4"))]),
 (35, _C, "Receptor de glicocorticoide e cortisol", [("35a", "GR: citoplasma → núcleo", _d("p8-4"))]),
 (36, _C, "Ativadores controlados por fosforilação", [("36a", "Fosforilação muda ligação ou localização", _d("p8-5"))]),
 (37, _C, "FOXO1 e a glicemia", [("37a", "Insulina → AKT → FOXO1 fora do núcleo", _d("p8-5"))]),
 (38, _C, "GFP-FOXO1 e insulina", [("38a", "FOXO1 sai do núcleo com insulina", _d("p8-5"))]),
 (39, "capa", "Bibliografia", []),
]
JUSTIFICATIVAS = {"capa": "capa ou bibliografia, sem conteúdo", "logistica": "roteiro, objetivos ou divisória que repete os tópicos",
 "fora_do_recorte": "figura de animais transgênicos que ilustra a universalidade sem texto próprio; o princípio está no card da lâmina 23"}
CAPITULO = [("Alberts 5ª ed., cap. 7 (controle da expressão gênica)", [
 ("l1", "Ativadores modulares, Mediador e integração de sinais", _d("p7-1")),
 ("l2", "Sinergia e controle combinatório", _d("p5-1")),
 ("l3", "Fosforilação e localização de fatores", _d("p8-5"))])]
EXERCICIOS = [
 ("Exercícios de BM, regulação 1 e 2 (Q1–3)", [
  ("e1", "Diferenças procarioto × eucarioto", _d("p2-1")), ("e2", "Duplo híbrido e modularidade", _d("p7-3")), ("e3", "Experimento de universalidade", _d("p7-2"))]),
 ("Provas biomol-07", [
  ("q1", "Fosforilação inibindo um fator (2019 P3 5.2)", _d("p8-5")), ("q2", "Esteroide × peptídeo (2019 P3 5.4)", _d("p8-3")),
  ("q3", "Mecanismos transcricionais do dimorfismo (2025 P3 1.5)", _d("p5-1"))])]
