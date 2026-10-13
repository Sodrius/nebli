"""Inventário atômico de Prática 1 – morfologia da célula bacteriana e técnicas de assepsia e cultivo (UC03 P2, Microbiologia; Profa.
Elisabete Vicente). A "lâmina" é o roteiro de aulas práticas (36 pp.): T/P1 (Gram) e T/P2 (meios) são desta aula; T/P3–T/P5 (controle,
antibiograma, microbiota) ficam para as aulas de Controle microbiológico, Antibióticos e Prática 3. Escrito em 10/10/2026 antes da seleção.
Muitos alvos já existem em Morfologia (aula 26) e Fisiologia (aula 27): ficam lá e são associados aqui (F-20261010-CLAUDE-04).
"""
PREFIXO = "mb28"
AULA = "Prática 1 – morfologia e técnicas de assepsia e cultivo (UC03 P2; Profa. Elisabete Vicente)"
EXC = "EXC: "
OUTRA = EXC + "roteiro de outra prática (controle, antibiograma ou microbiota), coberto na aula correspondente"

SLIDES = [
 (1, "capa", "Capa do roteiro", []),
 (2, "capa", "Sumário", []),
 (3, "conteudo", "Normas de segurança", [("risco", "Quatro classes de risco biológico", "risco-classes"), ("epi", "EPIs × EPCs", "epc")]),
 (4, "conteudo", "Morfologia microscópica", [
   ("formas", "Cocos, bacilos, espirilos", "sh-1791576666442"),
   ("arranjos", "Estreptococos, estreptobacilos, estafilococos, sarcinas", ["sh-1791576666842", "sh-1791576667142", "sh-1791576666993", "sarcina"]),
   ("espiral", "Espiroquetas flexíveis × espirilos rígidos; vibriões", ["sh-1791576667442", "sh-1791576667293"])]),
 (5, "conteudo", "Colorações", [
   ("basico", "Célula negativa atrai corantes básicos", "corante-basico"),
   ("tipos", "Simples, diferencial (Gram, Ziehl-Neelsen), especial", "diferencial"),
   ("mordente", "Iodo é mordente no Gram", "mordente"),
   ("gram", "Gram separa positivas e negativas; complexo violeta-lugol; álcool", ["sh-1791576668792", "sh-1791576668942"])]),
 (6, "conteudo", "Prática: coloração de Gram", [
   ("fixacao", "Esfregaço fixado na chama", "fixacao"),
   ("passos", "Cristal violeta, lugol, álcool, fucsina", "contracorante")]),
 (7, "conteudo", "Resultados do Gram", [("result", "E. coli negativo; Bacillus, Staphylococcus, Streptococcus positivos", ["sh-1791163024625", "sh-1791163025158"])]),
 (8, "conteudo", "Meio líquido × sólido", [("agar", "Sólido = mesmo meio + 2% ágar", "agar-2"), ("usos", "Líquido: curva; sólido: colônias isoladas", ["sh-1791647815469", "sh-1791647815594"])]),
 (9, "conteudo", "Semeadura", [("semeadura", "Alça flambada; esgotamento", "sh-1791647815594")]),
 (10, "conteudo", "Questões: turvação e colônias", [("turvo", "Meio límpido fica turvo", "sh-1791647815469"), ("colonia", "Colônia vem de uma célula", "sh-1791647815594")]),
 (11, "conteudo", "Composição dos meios", [
   ("minimo", "Meio mínimo: sais + glicose (M9)", "meio-minimo"),
   ("complexo", "Meio complexo: hidrolisado de proteína; Mueller-Hinton para antibiograma", "mueller"),
   ("sangue", "Ágar sangue: hemólise α, β, γ com exemplos", ["sh-1791647817820", "sh-1791647817944", "sh-1791647818070", "sh-1791647818194", "hemolise-exemplos"])]),
 (12, "conteudo", "Chocolate, Thayer-Martin, MacConkey", [
   ("choc", "Chocolate para Neisseria e Haemophilus", ["sh-1791647818320", "sh-1791647818444"]),
   ("tm", "Thayer-Martin: antibióticos, seleciona Neisseria", ["thayer-martin", "thayer-vanco"]),
   ("mc", "MacConkey: Lac+ vermelhas, Lac− incolores", ["sh-1791647817219", "sh-1791647817444", "lac-negativo"])]),
 (13, "conteudo", "Manitol-salgado e cetrimida", [
   ("manitol", "7,5% NaCl; S. aureus amarelo", ["manitol-sal", "manitol-amarelo"]),
   ("cetrimida", "Seleciona P. aeruginosa; piocianina", "cetrimida")]),
 (14, "conteudo", "Outros meios (continuação)", [("outros", "Continuação de meios", "sh-1791647816844")]),
 (15, "conteudo", "Questões da T/P2", [("quest", "Questões de estudo", "sh-1791647816720")]),
] + [(n, "conteudo", "Roteiro de outra prática", [("outra-%d" % n, "Controle, antibiograma ou microbiota", OUTRA)]) for n in range(16, 37)]
JUSTIFICATIVAS = {"capa": "capa ou sumário, sem conteúdo"}

CAPITULO = [("Trabulsi 6ª ed., cap. 2 (morfologia e estrutura; coloração de Gram)", [
   ("tb-formas", "Formas e arranjos", ["sh-1791576666442", "sarcina"]),
   ("tb-gram", "Gram: cristal violeta, lugol, álcool, fucsina", ["mordente", "contracorante", "sh-1791576668792"])])]

EXERCICIOS = [
 ("Provas UC03 (índice micro-03)", [("p2023", "2023 P2 3.3: por que não usar Gram no escarro (BAAR → Ziehl-Neelsen)", "diferencial")]),
]
