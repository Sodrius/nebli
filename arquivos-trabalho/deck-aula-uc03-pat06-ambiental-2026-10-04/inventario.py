"""Inventário atômico da Patologia ambiental (lâminas 17–51 do PDF da UC; numeração do PDF), 09/10 (F-20261009-CLAUDE-02).
Fontes: fontes/slides.txt e PDF (vistas), apostila de veteranos aula 7 (fontes/veteranos-patologia-integral.txt pp. 33–34), Robbins
cap. 9 (fontes/robbins-cap9-ambiental-pp407-427.txt: poluição do ar, CO), provas P2 2024 e 2025 (fontes/provas-originais-ambiental.txt).
Para python3 -m nebli.inventario. As lâminas 1–16 do PDF são de Edema e congestão (outra aula): entram como capa/fora."""
PREFIXO = "pat06"
AULA = "Patologia ambiental (UC03, Patologia, aula 24; Prof. Luiz Fernando Ferraz da Silva)"
EXC = "EXC: "
JUSTIFICATIVAS = {"capa": "capa, encerramento ou lâmina de outra aula (Edema, 1–16) no mesmo PDF"}

SLIDES = [
 (17, "capa", "Capa", []),
 (18, "conteudo", "A história da poluição (o fogo)", [("fogo", "Fogo para aquecer, iluminar e cozinhar", "revolucao-industrial")]),
 (19, "conteudo", "Revolução Industrial", [("industrial", "Salto da poluição após a Revolução Industrial", "revolucao-industrial")]),
 (20, "conteudo", "Grande Nevoeiro de 1952", [
   ("nevoeiro", "4.000 mortes em 1 semana; >8.000 em 3 semanas", "grande-nevoeiro"),
   ("inversao", "Inversão térmica prendeu a poluição ao nível do chão (apostila)", "inversao-termica")]),
 (21, "conteudo", "Mortes diárias × fumaça em dezembro de 1952", [("curva", "Mortes acompanham a concentração de fumaça", "grande-nevoeiro")]),
 (22, "conteudo", "Pirâmide dos efeitos", [("piramide", "Mortes, internações, consultas, medicação, inflamação subclínica; gravidade × número de afetados", "iceberg")]),
 (23, "conteudo", "Mudanças climáticas (IPCC)", [("gee", "Gases de efeito estufa: CO2 e metano, combustível fóssil (aula II)", "gee")]),
 (24, "conteudo", "Mudanças climáticas", [("calor", "Calor extremo, ondas de calor (aula II)", "ondas-calor")]),
 (25, "conteudo", "Mudanças climáticas", [("vetores", "Doenças por vetores e pela água (aula II)", "vetores")]),
 (26, "conteudo", "Mudanças climáticas", [("ozonio", "Ozônio e asma (aula II)", "ozonio-asma")]),
 (27, "conteudo", "Mudanças climáticas", [("polen", "Pólen e alergias (aula II)", "polen")]),
 (28, "conteudo", "Mudanças climáticas e saúde", [("enchentes", "Enchentes e fungos (aula II)", "enchentes-fungos")]),
 (29, "conteudo", "Megacidades: população urbana", [("urbano", "Crescimento da população urbana (IBGE)", "oms-pm25")]),
 (30, "conteudo", "Atlas ambiental de São Paulo", [("atlas", "Mapa ambiental de SP", EXC + "mapa ilustrativo")]),
 (31, "conteudo", "Megacidades (imagem)", [("img31", "Imagem", EXC + "lâmina só com imagem")]),
 (32, "conteudo", "Megacidades (imagem)", [("img32", "Imagem", EXC + "lâmina só com imagem")]),
 (33, "conteudo", "Megacidades (imagem)", [("img33", "Imagem", EXC + "lâmina só com imagem")]),
 (34, "conteudo", "Concentrações × diretriz da OMS", [("oms", "28/20/16 µg/m³ × diretriz OMS 10 µg/m³", "oms-pm25")]),
 (35, "conteudo", "Poluentes primários e secundários", [
   ("veiculos", "Veículos: principal fonte em SP (palavras-cruzadas)", "veiculos-sp"),
   ("fontes", "Indústrias, veículos, biomassa: SO2, NOx, MP, HPA, CO, metais", ["fontes-poluentes", "primario"]),
   ("secundarios", "O3, NO2, H2SO4, sulfatos (secundários)", "secundario"),
   ("co", "CO entre os poluentes (Robbins: carboxi-hemoglobina)", ["cohb", "co-affinity"])]),
 (36, "conteudo", "Material particulado", [
   ("composicao", "Nitratos, sulfatos, metais, HPA sobre núcleo de carbono", "mp-nucleo"),
   ("fontes-mp", "Fontes naturais e antropogênicas", "mp-nucleo"),
   ("diametro", "Classificação pelo diâmetro aerodinâmico", "pm-diametro")]),
 (37, "conteudo", "PM10, PM2,5, ultrafinas", [
   ("deposicao", "Tamanho define o sítio de deposição", "pm-deposicao"),
   ("antracose", "Macrófagos guardam o carbono (apostila: antracose)", ["antracose", "alveolar-macrophage"]),
   ("arvores", "Árvores retêm partículas (apostila, palavras-cruzadas)", "arvores")]),
 (38, "conteudo", "NO2 × função (gráfico)", [("no2", "NO2 e efeito respiratório", "cilia-clearance")]),
 (39, "conteudo", "Poluição atmosférica (imagem)", [("img39", "Imagem", EXC + "lâmina só com imagem")]),
 (40, "conteudo", "PM2,5 e mortalidade (Pope 2000)", [("mortalidade", "Mortalidade ajustada sobe com PM2,5; SP 28 µg/m³", "pm-mortalidade")]),
 (41, "conteudo", "Expectativa de vida × PM2,5", [("expectativa", "Menos PM2,5, mais expectativa de vida", "expectativa-vida")]),
 (42, "conteudo", "Área luminal coronariana (filtrado × poluído)", [("lumen", "Poluição reduz a luz coronariana", "lumen-parede")]),
 (43, "conteudo", "Poluição e saúde (imagem)", [("img43", "Imagem", "lumen-parede")]),
 (44, "conteudo", "Poluição e aterosclerose", [
   ("ldl", "Oxidação de LDL; anticorpos anti-LDLox; placa mais espessa sem mais lipídio", ["ldl-placa", "oxidized-ldl"])]),
 (45, "conteudo", "Mills 2007 (efeitos cardiovasculares)", [("mills", "Partículas e efeitos cardiovasculares", "inflamacao-sistemica")]),
 (46, "conteudo", "Poluição e saúde vascular", [("vascular", "Disfunção endotelial e trombose", ["disfuncao-endotelial", "endothelial-no"])]),
 (47, "conteudo", "Biomassa", [("biomassa", "Uso doméstico de biomassa", "biomassa-tabaco")]),
 (48, "conteudo", "Biomassa no mundo (Salvi 2009)", [("salvi", "Proporção de domicílios com biomassa", "biomassa-rural")]),
 (49, "conteudo", "Biomassa indoor", [("indoor", "Efeitos da exposição indoor", "biomassa-tabaco")]),
 (50, "conteudo", "Mecanismos", [
   ("irritacao", "Irritação química: olhos, coriza, lacrimejamento", "irritacao"),
   ("mucociliar", "Alterações mucociliares e infecções", ["biomassa-pneumonia", "pneumonia-defense", "cilia-clearance"]),
   ("oxidativo", "Reações oxidativas, IL-6/IL-8, granulócitos", "estresse-oxidativo"),
   ("dpoc", "Inflamação crônica, função pulmonar, DPOC", "dpoc"),
   ("sistemico", "Transposição da barreira epitelial, efeitos sistêmicos", "barreira-sistemica")]),
 (51, "conteudo", "COVID-19", [("covid", "Título", EXC + "só o título; sem conteúdo")]),
]

CAPITULO = [
 ("Robbins cap. 9 (poluição do ar)", [
   ("poluentes", "Poluentes externos (ozônio, SO2, partículas) e CO", ["secundario", "cohb"]),
   ("co", "CO: afinidade pela hemoglobina, hipóxia", "co-affinity")]),
]

EXERCICIOS = [
 ("Apostila de veteranos, aula 7", [
   ("nevoeiro", "Grande Nevoeiro: inversão térmica, >8 mil mortes, internações, inflamação subclínica", ["grande-nevoeiro", "inversao-termica", "iceberg"]),
   ("mp", "MP: núcleo de carbono inerte com substâncias tóxicas; diâmetro aerodinâmico; macrófagos", ["mp-nucleo", "pm-diametro", "antracose"]),
   ("saude", "Luz/parede coronariana e pulmonar; LDL oxidada; expectativa de vida", ["lumen-parede", "ldl-placa", "expectativa-vida"]),
   ("biomassa", "Biomassa comparável ao tabaco; rural não protege; irritação, infecções, DPOC", ["biomassa-tabaco", "biomassa-rural", "irritacao", "dpoc"])]),
 ("Patologia Ambiental II — Mudanças climáticas e saúde (Thais Mauad, 20 lâminas)", [
   ("ii-definicao", "Aquecimento por GEE (CO2, metano) da atividade humana", "gee"),
   ("ii-calor", "Calor extremo: mortalidade, doença renal, vulneráveis", "ondas-calor"),
   ("ii-infeccao", "Vetores, água, alimentos, solo (fungos)", ["vetores", "dengue-aedes"]),
   ("ii-ozonio", "Ozônio secundário (NOx + sol); irritante, asma", ["secundario", "ozonio-asma"]),
   ("ii-mp", "MP fino atinge o sangue; MP × calor", "pm-deposicao"),
   ("ii-alergia", "Pólen: estação mais longa, mais alergênico", "polen"),
   ("ii-enchentes", "Fungos após enchentes", "enchentes-fungos")]),
 ("Palavras-cruzadas da aula (gabarito; parte de poluição)", [
   ("pc-translocacao", "Translocação do MP para o sangue", "barreira-sistemica"),
   ("pc-ozonio", "Ozônio tóxico nas camadas baixas", "secundario"),
   ("pc-veiculos", "Veículos, principal fonte em SP", "veiculos-sp"),
   ("pc-antracose", "Pigmento acumulado no pulmão", "antracose"),
   ("pc-cardiaco", "Aumento de alterações cardíacas agudas", "inflamacao-sistemica"),
   ("pc-arvores", "Retenção de poluentes pelas árvores", "arvores")]),
 ("Provas UC03 P2", [
   ("2024-sistemica", "2024 1.18: inflamação sistêmica (IL-6, TNF) e infarto", "inflamacao-sistemica"),
   ("2024-endotelio", "2024 1.18: disfunção endotelial (menos NO)", "disfuncao-endotelial"),
   ("2024-defesas", "2024 1.18: macrófagos e cílios lesados, muco alterado → pneumonia", ["alveolar-macrophage", "cilia-clearance"]),
   ("2025-biomassa", "2025 4.3: biomassa → disfunção mucociliar, macrófagos hipoativos → pneumonia", "biomassa-pneumonia")]),
]
