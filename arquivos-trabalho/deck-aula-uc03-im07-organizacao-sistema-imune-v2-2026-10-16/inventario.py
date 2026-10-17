"""Inventário atômico de Organização e funcionamento do sistema imune (UC03 P1; Imunologia; Barbuto, 2020), escrito ANTES de escolher
cards (16/10, pipeline v4). Sequência = 26 lâminas (fontes/slides.pdf = turma II = pasta pessoal), vistas inteiras nesta sessão (io/g0..g2).
Lido nesta sessão: transcrição integral (50 pp.), provas im01, monitoria P1 (Imunologia, aula 1) e mapa imunológico, apostila guia de
Imunologia e UC3 (texto da corrida antiga), Abbas Básica cap. 1 (tecidos). Lâminas I da turma (41, versão antiga) conferidas.
O professor diz que os objetivos 4 e 5 (adesão e quimiocinas, lâminas 22–23, em cinza) não são o foco desta aula: entram poucos cards.
Fronteira (MEMORY §3): seleção tímica, DC, recirculação, centro germinativo, FDC, Peyer e M cells já têm cópias NEBLI das aulas 45, 49,
38, 08, 51 e UC08 → sh(); MHC e apresentação (aula 20), reconhecimento inato (08) e inflamação (37/38) ficam lá.
"""
PREFIXO = "im07"
AULA = "Organização e funcionamento do sistema imune (UC03 P1; Imunologia)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "The dragon is tame, mas o treinamento é trabalhoso", [("a1", "Motivação", EXC + "frase motivacional")]),
 (3, "conteudo", "Objetivos do tema", [("a2", "Objetivos", EXC + "lista de objetivos; cada um vira cards nas lâminas seguintes")]),
 (4, "conteudo", "Papel do SI: homeostasia; sistemas nervoso e imune incluem o exterior (sinais moleculares)", [
   ("a3", "Inato × adaptativo: barreiras são inatas", "ak-inata-barreiras")]),
 (5, "conteudo", "Tradutor universal: repertório completo distribuído clonalmente (T e B) reconhece antígenos", [
   ("a4", "Adaptativo é específico e diverso", ["ak-adaptativa-especifica", "ak-adaptativa-diversa"]), ("a5", "Inato: pouca diversidade, inespecífico", ["ak-inata-inespecifica", "ak-inata-diversidade"])]),
 (6, "conteudo", "SI em ação: barreiras; células do tecido (DAMPs), macrófagos, mastócitos, endotélio, ILC; resposta inata", [
   ("a6", "Sentinelas: macrófagos e mastócitos", ["sh-1791780352647", "sh-1791743342260"]), ("a7", "Tecido lesado libera DAMPs", "sh-1791743340457"),
   ("a8", "Endotélio expressa moléculas de adesão", "sh-1791780358855")]),
 (7, "conteudo", "Fagocitose (vídeo)", [("a9", "Fagocitose", EXC + "ilustração; fagocitose é da aula 08 e 38")]),
 (8, "conteudo", "Citotoxicidade celular (vídeo)", [("a10", "Citotoxicidade", EXC + "ilustração; citotoxicidade é da aula 22")]),
 (9, "conteudo", "SI em ação + resposta adquirida direcionada pelas inatas", [("a11", "Inata é rápida; adquirida demora", ["ak-inata-rapida", "ak-adaptativa-lenta"]),
   ("a12", "Memória só na adaptativa", ["ak-inata-memoria", "ak-adaptativa-memoria"])]),
 (10, "conteudo", "Primários: gera genes dos receptores clonais, seleciona úteis, isolamento; timo: interação com APC, deleção clonal, Treg", [
   ("a13", "Seleção positiva no córtex", "sh-1791625423407"), ("a14", "Seleção negativa na medula", ["sh-1791625423808", "sh-1791625423683"]),
   ("a15", "AIRE expressa autoantígenos", "sh-1791625423932"), ("a16", "Tolerância central × periférica", "sh-1792166970267"),
   ("a17", "Córtex e medula do timo", ["ak-timo-cortex", "ak-timo-medula", "ak-hassall"])]),
 (11, "conteudo", "Primários (timo → T, medula → B) e secundários (linfonodo, baço, Peyer, apêndice, Waldeyer, aglomerados)", [
   ("a18", "Medula óssea produz e matura B", ["ak-mo-producao", "ak-mo-b"]), ("a19", "Timo matura T", "sh-1791625422783"),
   ("a20", "Secundários: encontro com antígeno", ["ak-secundarios", "sh-1791629588022"]), ("a21", "MALT e Peyer", ["sh-1791023357519", "sh-1790980914855"])]),
 (12, "conteudo", "Do secundário aos tecidos periféricos: ação", [("a22", "Ativação no linfonodo drenante", "sh-1791716419826")]),
 (13, "conteudo", "Circulação do naive: primário → sangue → HEV → secundário → linfa → sangue", [
   ("a23", "Entrada pelas HEV", "sh-1791625425583"), ("a24", "Linfa volta ao sangue pelo ducto torácico", "sh-1791577165815"),
   ("a25", "Naive recircula; efetor vai ao tecido", "sh-1791625425207")]),
 (14, "conteudo", "Circulação do T ativado: vigilância dos tecidos; endereçamento por moléculas de adesão", [("a26", "Efetor vai ao tecido", "sh-1791625425207")]),
 (15, "conteudo", "Geração somática e aleatória; distribuição aleatória; redistribuição contínua; fluidez", [("a27", "Fluidez", EXC + "síntese conceitual sem fato a decorar; a recirculação entra nas lâminas 13–14")]),
 (16, "conteudo", "Esquema: alarme → recrutamento → paisagem molecular → órgão linfoide → resposta ou tolerância", [
   ("a28", "Sem lesão, tolerância", "au-tolerancia"), ("a29", "Vacina: resposta secundária mais rápida", "sh-1791629597796")]),
 (17, "conteudo", "Secundários: fluxo contínuo, muitos linfócitos e APC → aumenta a chance de encontro", [("a30", "Secundários concentram antígeno e linfócitos", "ak-secundarios")]),
 (18, "conteudo", "APC: DC (única que ativa naive, apresentação cruzada, direciona), macrófago, linfócito B (seletiva)", [
   ("a31", "DC ativa o T naive", ["sh-1791625426408", "sh-1791625422291"]), ("a32", "Apresentação cruzada", "sh-1791625427531"),
   ("a33", "B apresenta antígeno captado pela Ig", ["au-b-apc", "sh-1791629593971"])]),
 (19, "conteudo", "Aferência: linfonodo (linfa), baço (sangue), MALT (luz, células M, DC)", [
   ("a34", "Antígeno chega pela linfa aferente", "ak-aferente"), ("a35", "Baço: zona marginal capta antígeno do sangue", ["ak-zona-marginal", "ak-zona-marginal-captura", "sh-1792083501161"]),
   ("a36", "Células M e DC na placa de Peyer", ["sh-1790980915172", "sh-1791780605649"]), ("a37", "Peyer → plasmócitos IgA", "sh-1790980915277"),
   ("a38", "Asplenia: encapsulados e IgM", ["ak-esplenectomia-vacina", "ak-baco-igm"])]),
 (20, "conteudo", "Áreas T (paracórtex, PALS, interfolicular) e B (folículos, centro germinativo, FDC); expansão clonal", [
   ("a39", "Folículos no córtex externo", ["ak-foliculos", "ak-foliculo-b", "ak-foliculo-primario", "sh-1791625425757"]),
   ("a40", "Paracórtex", ["ak-paracortex", "ak-paracortex-viral", "sh-1792166984740"]), ("a41", "Centro germinativo na resposta humoral", "sh-1791629593848"),
   ("a42", "Hiperplasia folicular × paracortical", ["ak-hiperplasia-folicular", "ak-hiperplasia-paracortical"]),
   ("a43", "PALS e polpa branca", ["ak-pals", "ak-polpa-branca", "ak-baco-t", "ak-baco-b"]), ("a44", "FDC guarda antígeno", "sh-1791629594223")]),
 (21, "conteudo", "Eferência: plasmócitos (cordões medulares, polpa vermelha, medula óssea), anticorpos; T ativado → tecido", [
   ("a45", "Medula do linfonodo", ["ak-medula-ln", "ak-seios-eferente", "ak-seios-macrofagos", "ak-cordoes"]), ("a46", "Polpa vermelha", "ak-polpa-vermelha"),
   ("a47", "Plasmócitos na medula óssea; mieloma", "ak-plasmocito-mo"), ("a48", "Expansão leva ~2 semanas", "sh-1791625428033"),
   ("a49", "Janela imunológica", "ak-janela-hiv")]),
 (22, "conteudo", "Moléculas de adesão: selectinas, integrinas β2 (CD18), superfamília das Ig, mucinas", [
   ("a50", "Famílias de adesão", "au-adesao"), ("a51", "Selectinas e sialil-Lewis X", "sh-1791780357418"), ("a52", "LAD1: CD18", "sh-1791743343209")]),
 (23, "conteudo", "Quimiocinas (CXC, CC, CX3C, XC; IL-8) e mediadores (C3a, C5a, lipídicos)", [
   ("a53", "Famílias de quimiocinas", "au-quimiocinas"), ("a54", "Quimiotáticos de neutrófilo", ["sh-1791780359733", "sh-1791780360378"])]),
 (24, "conteudo", "Revendo o sistema em ação (repetida)", [("a55", "Resposta × tolerância", "au-tolerancia")]),
 (25, "conteudo", "Resumo dos secundários", [("a56", "Resumo", "ak-secundarios")]),
 (26, "conteudo", "Leitura complementar (Lakkis; Kruetzmann; Laurence; Matthews)", [("a57", "Artigos", EXC + "referências; o achado de Kruetzmann (memória IgM no baço) entra em ak-baco-igm")]),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo"}
CAPITULO = [("Abbas Básica cap. 1 (tecidos do sistema imune) (confirma)", [
 ("l1", "Linfonodo: folículos, paracórtex, HEV, medula", ["ak-foliculos", "ak-paracortex", "sh-1791625425583", "ak-medula-ln"]),
 ("l2", "Baço: polpa branca, PALS, zona marginal", ["ak-polpa-branca", "ak-pals", "ak-zona-marginal"]),
 ("l3", "Recirculação de naive e efetores", "sh-1791625425207")])]
EXERCICIOS = [
 ("Provas UC03 (índice im01)", [
   ("p1", "Principal diferença entre resposta inata e adquirida (2024 P1 2.11)", ["ak-adaptativa-especifica", "ak-inata-memoria", "ak-adaptativa-memoria"]),
   ("p2", "Resposta celular no linfonodo aumentado: regiões e células (2023 P2 2.3)", ["ak-paracortex-viral", "ak-hiperplasia-paracortical", "sh-1791625426408"]),
   ("p3", "Linfonodo normal × sarampo (2019 P1 3.3)", ["ak-paracortex-viral", "sh-1791629593848"]),
   ("p4", "Resposta CD8 contra o core do HBV (2018 P1 1.11)", "sh-1791625427531"),
   ("p5", "Imunidade da mucosa digestiva (2018 P3 5.6)", ["sh-1790980915172", "sh-1790980915277"]),
   ("p6", "Seleção no timo e por que a da medula é menos estrita (2015 P2sub 6.1, 6.3)", ["sh-1791625423407", "sh-1791625423808"]),
   ("p7", "Tregs e tolerância periférica (2025 P3 4.1)", "sh-1792166970267")]),
 ("Monitoria P1 (Imunologia aula 1) e mapa imunológico", [
   ("m1", "Inata × adaptativa", ["ak-inata-rapida", "ak-adaptativa-lenta"]), ("m2", "Órgãos linfoides primários e secundários", ["ak-mo-producao", "ak-secundarios"]),
   ("m3", "Recirculação e HEV", ["sh-1791625425583", "sh-1791625425207"])]),
 ("Palavras-cruzadas da turma (gabarito)", [("c1", "Seleção negativa no timo; AIRE; medula óssea matura B", ["sh-1791625423808", "sh-1791625423932", "ak-mo-b"]),
   ("c2", "Transmigração e LFA-1 (adesão forte)", ["au-adesao", "sh-1791743343209"]), ("c3", "BALT (MALT respiratório)", "sh-1791023357519"),
   ("c4", "Plasmócitos de vida curta e longa", "ak-plasmocito-mo"),
   ("c5", "Bursa, mastócito, eosinófilo, neutrófilo, ROS, inflamassoma, MHC, CD3, fagocitose, CTLA-4, imunoterapia, defensinas, autoinflamatórias, basófilos", EXC + "termos das aulas 08, 20, 22, 37/38, 45 e 51 (a cruzada cobre a UC inteira)")]),
]
