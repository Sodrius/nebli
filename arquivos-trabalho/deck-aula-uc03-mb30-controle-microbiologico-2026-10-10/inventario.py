"""Inventário atômico de Controle microbiológico (UC03 P2, Microbiologia, aula 30; Prof. Nilton Lincopan; 57 lâminas de 2026, pasta pessoal).
Escrito em 10/10/2026 antes da seleção: lâminas (visual/folha-NN), Aula 04 da turma (Profa. Elisabete Vicente, I e II: valor D, '99,9%',
indicadores biológicos, plasma, químicos esterilizantes, resistência a biocidas, questões de revisão), bibliografias I/II (Timenetsky), prova
2025 P2 3.3 (índice micro-04), monitoria P2 aula 3, apostila guia de Micro aula 3, Trabulsi 6ª cap. 7 (livros/trabulsi-07.txt).
Aula 08 da turma = roteiro prático (biossegurança, antibiograma, antimicrobianos naturais) e videoaula de semeadura: outras aulas.
"""
PREFIXO = "mb30"
AULA = "Controle microbiológico (UC03 P2; Prof. Nilton Lincopan)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Micro-organismos", [("dominios", "Bactérias, fungos, vírus, parasitas", EXC + "abertura, revisão")]),
 (3, "conteudo", "Bactérias microscópicas", [("micro", "Vistas ao microscópio", EXC + "abertura, revisão")]),
 (4, "conteudo", "Imagem de bactérias", [("img", "Bactérias em esfregaço", EXC + "ilustração")]),
 (5, "conteudo", "Bactérias em todo lugar", [("todo-lugar", "Ubiquidade", EXC + "abertura")]),
 (6, "conteudo", "Crescimento rápido", [("fissao", "Fissão binária", "sh-1791647812370"), ("formula", "NF = Ni × 2^n", "crescimento-exp")]),
 (7, "conteudo", "Microbiota humana", [("microbiota", "Microbiota", EXC + "abertura; microbiota em Homem-ambiente")]),
 (8, "conteudo", "Microbiota se compartilha", [("compartilha", "Contato com animais", EXC + "abertura")]),
 (9, "conteudo", "Boas, nocivas, oportunistas", [("tipos", "L. casei, M. tuberculosis, E. coli", "probioticos")]),
 (10, "conteudo", "Probióticos", [("probioticos", "Bactérias boas como probióticos", "probioticos")]),
 (11, "conteudo", "Infecções", [("infeccoes", "Lista de infecções", EXC + "contexto clínico, sem item de controle")]),
 (12, "conteudo", "Transmissão direta", [("direta", "Mãos", "transmissao")]),
 (13, "conteudo", "Transmissão indireta", [("aerossol", "Aerossóis", "transmissao")]),
 (14, "conteudo", "Contaminação de alimentos", [("alimentos", "Bactérias em alimentos", "zona-perigo")]),
 (15, "conteudo", "Crescimento em alimentos", [("zona", "Zona de perigo 5–60 °C", "zona-perigo")]),
 (16, "conteudo", "Sistema imune", [("imune", "Imunocompetente × imunossuprimido", EXC + "contexto")]),
 (17, "conteudo", "Exemplos de controle", [("exemplos", "Painel A–I de controle", ["limpeza", "antissepsia", "autoclave-vapor"])]),
 (18, "conteudo", "Mumificação", [("natrao", "Natrão", "historia")]),
 (19, "conteudo", "Conservação na Mesopotâmia", [("salga", "Conservação de alimentos", "historia")]),
 (20, "conteudo", "Cobre e prata", [("cobre", "Água em recipientes de cobre e prata", "historia")]),
 (21, "conteudo", "Esterilização > desinfecção > antissepsia > limpeza", [("hierarquia", "Graus de eliminação", ["esterilizacao", "desinfeccao", "desinfeccao-esporos", "antissepsia", "assepsia"])]),
 (22, "conteudo", "Escala de resistência", [("topo", "Esporos", ["resistencia-topo", "sh-1791163038847"]), ("mico", "Micobactérias", "micobacterias"),
                                              ("virus-nus", "Vírus pequenos não lipídicos", "virus-nus"), ("meio", "Fungos e bactérias vegetativas", "envelopados"),
                                              ("base", "Vírus lipídicos", "envelopados")]),
 (23, "conteudo", "Mapa do controle microbiano", [("mapa", "Físico, químico, in vivo", ["calor-umido-seco", "filtracao", "antibiotico"])]),
 (24, "conteudo", "Alvos letais", [("alvos", "Membrana, proteínas, metabolismo, ácidos nucleicos, oxidação", "alvos")]),
 (25, "conteudo", "Total × parcial", [("total-parcial", "Esterilização; desinfecção; antissepsia", ["esterilizacao", "antissepsia"])]),
 (26, "conteudo", "Cida × stático", [("cida", "Morte × inibição", "cida-statico")]),
 (27, "conteudo", "Morte exponencial", [("exp", "Um log por minuto", ["morte-exponencial", "valor-d", "mata-999"])]),
 (28, "conteudo", "Carga × tempo", [("carga", "Carga maior, mais tempo", ["carga", "esteril-prob"])]),
 (29, "conteudo", "Semmelweis", [("semmelweis", "Lavagem das mãos e febre puerperal", "semmelweis")]),
 (30, "conteudo", "GBS e prevenção", [("gbs", "Rastreio e profilaxia intraparto", "gbs")]),
 (31, "conteudo", "Limpeza", [("limpeza", "Limpeza manual com detergente; EPI", "limpeza")]),
 (32, "conteudo", "Caso de Pseudomonas", [("caso", "Balanopostite por Pseudomonas MDR", EXC + "ilustração clínica")]),
 (33, "conteudo", "Definição de esterilização", [("def", "Destruir ou separar totalmente, incluindo esporos", "esterilizacao")]),
 (34, "conteudo", "Lister", [("lister", "Fenol em cirurgia", "lister")]),
 (35, "conteudo", "Spray de ácido carbólico", [("spray", "Cirurgia com fenol", "lister")]),
 (36, "conteudo", "Métodos físicos, químicos e biológicos", [("metodos", "Classificação dos métodos", ["metodos-bio", "assepsia"])]),
 (37, "conteudo", "Árvore da temperatura", [("arvore", "Calor seco/úmido, com/sem pressão, frio", ["calor-umido-seco", "sh-1791163039477", "tindalizacao", "frio"])]),
 (38, "conteudo", "Calor seco direto", [("flambagem", "Bico de Bunsen", "flambagem")]),
 (39, "conteudo", "Forno Pasteur", [("forno", "180 °C × 1 h", ["forno", "indicador-seco"])]),
 (40, "conteudo", "Autoclave", [("autoclave", "Calor úmido + pressão", ["autoclave-vapor", "autoclave-param", "autoclave-esporo", "indicador-autoclave"])]),
 (41, "conteudo", "Autoclave (foto)", [("foto", "Material autoclavado", "autoclave-vapor")]),
 (42, "conteudo", "Pasteurização", [("pasteur", "LTLT, HTST, UHT", ["pasteurizacao", "pasteur-tempos"])]),
 (43, "conteudo", "Filtração", [("filtracao", "Filtros < 0,45 µm para termossensíveis", "filtracao")]),
 (44, "conteudo", "Tabela de poros", [("poros", "Poros e micróbios retidos", "filtro-022")]),
 (45, "conteudo", "HEPA", [("hepa", "Fluxo laminar", "hepa")]),
 (46, "conteudo", "Espectro UV-visível", [("espectro", "Espectro", "uv-dimero")]),
 (47, "conteudo", "Luz UV germicida", [("uv", "Lâmpadas de 260 nm", ["uv-penetracao", "gama"])]),
 (48, "conteudo", "UVA/UVB/UVC e dímeros", [("dimero", "Dímeros de timina", "uv-dimero")]),
 (49, "conteudo", "Desinfecção e antissepsia", [("def", "Desinfecção em objetos; antissepsia em tecidos", ["antissepsia", "desinfeccao-esporos", "termossensivel", "oxido-etileno", "glutaraldeido", "esporicidas", "esporocida-esterilizante"])]),
 (50, "conteudo", "Álcoois", [("alcool", "Etílico 70%, desnaturação", ["alcool-desnatura", "alcool-70", "membranas", "nao-esporicidas", "cdiff"])]),
 (51, "conteudo", "Triclosan", [("triclosan", "Inibe ácidos graxos; resistência", ["triclosan", "resistencia-biocida"])]),
 (52, "conteudo", "Iodo", [("iodo", "Oxidante, amplo espectro", "iodo")]),
 (53, "conteudo", "Cloro", [("cloro", "HOCl", "cloro")]),
 (54, "conteudo", "Agentes oxidantes", [("h2o2", "Peróxido 3%", "peroxido")]),
 (55, "conteudo", "Clorexidina", [("clorex", "Biguanida 0,12–0,20%", "clorexidina")]),
 (56, "conteudo", "Amônios quaternários", [("quats", "Benzalcônio, cetilpiridínio", "quaternarios")]),
 (57, "conteudo", "Antibióticos", [("atb", "Ponte para antibióticos", "antibiotico")]),
]
JUSTIFICATIVAS = {"capa": "capa, sem conteúdo"}

CAPITULO = [("Trabulsi 6ª ed., cap. 7 — Controle dos micro-organismos (pdf pp. 89–98)", [
   ("tb-termos", "Terminologia: esterilização absoluta, desinfecção, antissepsia, assepsia, bacteriostase", ["esterilizacao", "antissepsia", "assepsia", "cida-statico"]),
   ("tb-calor", "Calor úmido desnatura, seco oxida; D; morte exponencial; 10^-6", ["calor-umido-seco", "valor-d", "morte-exponencial", "esteril-prob"]),
   ("tb-indicadores", "Indicadores biológicos por método", ["indicador-autoclave", "indicador-seco"]),
   ("tb-radiacao", "Gama ioniza água; UV dímeros, 260 nm, baixa penetração", ["gama", "uv-dimero", "uv-penetracao"]),
   ("tb-quimicos", "Álcool com água, aldeídos alquilam, cloro HOCl, quaternários inativados por sabão", ["alcool-70", "glutaraldeido", "cloro", "quaternarios"])])]

EXERCICIOS = [
 ("Aula 04 da turma (Profa. Elisabete Vicente, I e II)", [
   ("tu-cida", "Atividade stática × cida; decréscimo em log", ["cida-statico", "valor-d"]),
   ("tu-indicadores", "G. stearothermophilus (úmido), B. subtilis/atrophaeus (seco), B. pumilus (gama), Deinococcus (UV)", ["indicador-autoclave", "indicador-seco"]),
   ("tu-plasma", "Plasma de H2O2 a 35–45 °C", "termossensivel"),
   ("tu-quimicos", "Formol/glutaraldeído 10 h; óxido de etileno", ["glutaraldeido", "oxido-etileno"]),
   ("tu-resistencia", "Resistência intrínseca/adquirida a biocidas", "resistencia-biocida"),
   ("tu-999", "'Mata 99,9%': 10^6 → 10^3", "mata-999"),
   ("tu-questoes", "Questões: desinfetante × antisséptico × antibiótico; esporocida × esterilizante; termossensível", ["antibiotico", "esporocida-esterilizante", "termossensivel"])]),
 ("Provas UC03 (índice micro-04)", [
   ("p2025", "2025 P2 3.3: esterilizar material após biópsia de M. tuberculosis (termorresistente × termossensível)", ["autoclave-param", "termossensivel", "micobacterias", "glutaraldeido"])]),
 ("Monitoria P2, aula 3", [
   ("mon-log", "População em escala log; 99,9%", "mata-999"),
   ("mon-calor", "Autoclave 120 °C 15–20 min; forno 160 °C 1–2 h; fervura; pasteurização", ["autoclave-param", "forno", "pasteurizacao"]),
   ("mon-filtro", "Filtração separa sem matar", "filtracao")]),
 ("Apostila guia de veteranos, aula 3", [
   ("gv-calor", "Úmido desnatura, seco oxida", "calor-umido-seco"),
   ("gv-quimicos", "Álcool com água; cloro HOCl; água oxigenada e catalase", ["alcool-70", "cloro", "peroxido"])]),
]
