"""Inventário atômico de Fisiologia bacteriana (UC03 P2, Microbiologia; Profa. Elisabete Vicente; 50 lâminas de 2026 na pasta pessoal 27).
Escrito em 10/10/2026 antes da seleção: lâminas (visual/folha-NN), PDF da turma (versão anterior, 37 lâminas, fontes/turma.txt),
monitoria P1 aula 2 (fontes/monitoria-p1.txt), guia de veteranos de Microbiologia aula 2 (fontes/apostila-veteranos-micro.txt),
provas micro-02 (11 subquestões, quase todas sobre a curva de crescimento), apostila NEBLI E1 (apoio).
"""
PREFIXO = "mb27"
AULA = "Fisiologia bacteriana (UC03 P2; Profa. Elisabete Vicente)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Nutrição e crescimento", [("def", "Crescimento = aumento do número por divisão binária", "crescimento-def"), ("subs", "Fonte de energia, carbono e nitrogênio", "quimio-hetero")]),
 (3, "conteudo", "Nutrientes", [("cnsp", "C, N, S, P compõem a maior parte do peso seco; íons", "macronutrientes")]),
 (4, "conteudo", "Classificação nutricional", [("trofico", "Quimiorganoheterotróficas: patógenos humanos", "quimio-hetero")]),
 (5, "conteudo", "pH", [("ph", "Maioria neutrófila, pH ideal 7", "ph-neutro")]),
 (6, "conteudo", "Temperatura", [("temp", "Psicrófilos, mesófilos (E. coli), termófilos", "mesofilos")]),
 (7, "conteudo", "Ambientes extremos", [("extremos", "Ambientes de extremófilos", EXC + "figura ecológica sem item médico")]),
 (8, "conteudo", "Aeração", [
   ("aero", "Aeróbios estritos, microaerófilos, anaeróbios estritos (C. tetani), facultativos (E. coli)", ["aerobio-sod", "microaerofilo", "facultativo", "clostridium-anaerobio"]),
   ("tubos", "Crescimento em tubo conforme O₂", "tubo-aerobio")]),
 (9, "conteudo", "Sal e força iônica", [("sal", "Halotolerantes (S. aureus), halófilos, não halófilos (E. coli)", "halotolerante")]),
 (10, "conteudo", "Papel do ferro", [("fe", "Cofator; imunidade nutricional; sideróforos; regulon Fur", ["ferro-imunidade", "lactoferrina", "sideroforo", "fur"])]),
 (11, "conteudo", "Ferro: micronutriente crítico", [("fe2", "Dita o crescimento; transferrina, lactoferrina, ferritina; sideróforos, hemolisinas", ["ferro-critico", "ferro-imunidade", "sideroforo"])]),
 (12, "conteudo", "Produção de energia", [("fermentacao", "Fermentação: baixa eficiência, sem aceptor; fosforilação no substrato", ["substrato", "fermentacao-nad"])]),
 (13, "conteudo", "ATP", [("atp", "Ligação rica em energia", "substrato")]),
 (14, "conteudo", "Estágios I e II da fermentação", [("est12", "Glicólise: 2 NADH, ATP, piruvato", "substrato")]),
 (15, "conteudo", "Estágio III", [("est3", "Consumo de NADH e produto da fermentação", "fermentacao-nad")]),
 (16, "conteudo", "Respiração × fermentação", [("resp", "Glicólise prepara a respiração; cadeia na membrana", ["membrana-cadeia", "anaerobio-fermenta"])]),
 (17, "conteudo", "Respiração aeróbia e anaeróbia", [("aer", "O₂ aceptor final; anaeróbia usa nitrato, sulfato…", ["membrana-cadeia", "respiracao-anaerobia", "o2-aceptor"])]),
 (18, "conteudo", "Figura: fermentação", [("fig18", "Produtos de fermentação", "fermentacao-produtos")]),
 (19, "conteudo", "Glicólise e Krebs", [("fig19", "Piruvato: lactato (anaeróbio) ou acetil-CoA (aeróbio)", "fermentacao-nad")]),
 (20, "conteudo", "Metabolismo bacteriano (esquema)", [("fig20", "Esquema geral", EXC + "esquema geral de revisão sem item próprio")]),
 (21, "conteudo", "Crescimento: diluições e semeadura", [("diluicao", "Contagem por diluição seriada e semeadura", "esgotamento")]),
 (22, "conteudo", "Curva de crescimento", [("curva", "Lag, log, estacionária, declínio", ["curva-fases", "lag", "estacionaria", "declinio"])]),
 (23, "conteudo", "Curva e virulência de S. aureus", [("virulencia", "Adesinas na fase exponencial; toxinas na estacionária", "virulencia-fase")]),
 (24, "conteudo", "Fases da curva", [("fases", "Lag: massa sem divisão; log: velocidade máxima; estacionária; declínio", ["lag", "log-geracao", "estacionaria", "declinio"])]),
 (25, "conteudo", "Composição dos meios", [("composicao", "Hidrolisados (C, N), carboidratos, tampões, inibidores, indicadores", ["indicador", "seletivo"])]),
 (26, "conteudo", "Tipos de meio", [("tipos", "Não seletivos (TSA, sangue), seletivos/diferenciais (MC, SS, VB), enriquecimento", ["seletivo", "sangue-nao-seletivo", "enriquecimento-salmonella"])]),
 (27, "conteudo", "Enterobactérias em meios seletivos", [("entero", "Crescem em meios seletivos MacConkey e Teague", "maconkey")]),
 (28, "conteudo", "Seletividade dos meios", [("selet", "MC pouco, SS moderado, VB alto; caldo de enriquecimento", ["maconkey", "enriquecimento-salmonella"])]),
 (29, "conteudo", "Nutrientes especiais", [("especiais", "Enriquecidos", "enriquecido")]),
 (30, "conteudo", "Ágar MacConkey", [("mc", "Lactose, sais biliares e cristal violeta, vermelho neutro", ["maconkey", "maconkey-lactose", "lactose-rosa"])]),
 (31, "conteudo", "MacConkey (foto)", [("mc-foto", "Colônias", "lactose-rosa")]),
 (32, "conteudo", "Ágar SS", [("ss", "Altamente seletivo; tiossulfato/citrato férrico detecta H₂S", "ss-h2s")]),
 (33, "conteudo", "Ágar SS (foto)", [("ss-foto", "Composição", "ss-h2s")]),
 (34, "conteudo", "Ágar sangue", [("sangue", "Base rica + 5% sangue; padrões de hemólise", ["sangue-nao-seletivo", "beta-hemolise", "alfa-hemolise", "gama-hemolise"])]),
 (35, "conteudo", "Ágar chocolate", [("chocolate", "Aquecido: libera fatores X e V", ["chocolate", "chocolate-fatores"])]),
 (36, "conteudo", "Meios simples (TSA)", [("tsa", "Colônia em 12–48 h", "esgotamento")]),
 (37, "conteudo", "Isolamento de não exigentes", [("isolamento", "Semeadura em meios comuns", "esgotamento")]),
 (38, "conteudo", "Isolamento (figura)", [("isol-fig", "Placas", "esgotamento")]),
 (39, "conteudo", "Colônias isoladas", [("colonias", "Obtenção de colônias isoladas", "esgotamento")]),
 (40, "conteudo", "Esgotamento do inóculo", [("esgot", "Técnica de esgotamento", "esgotamento")]),
 (41, "conteudo", "Condições de incubação", [("incubacao", "Atmosfera, temperatura, período", "esgotamento")]),
 (42, "conteudo", "FCF-USP (foto)", [("foto42", "Laboratório", EXC + "foto institucional")]),
 (43, "conteudo", "Identificação bioquímica", [("bioq", "Provas bioquímicas (TSI, fermentação de açúcares)", "rugai")]),
 (44, "conteudo", "Meio IAL/Rugai", [("rugai", "Um tubo, várias provas (indol, H₂S, gás, ureia, lisina, motilidade)", "rugai")]),
 (45, "conteudo", "Meios cromogênicos", [("cromo", "Identificação por cor sem provas confirmatórias", "cromogenico")]),
 (46, "conteudo", "Cromogênico urinário", [("uri", "E. coli vermelha, E. faecalis azul…", "cromogenico")]),
 (47, "conteudo", "Cromogênico para Candida", [("candida", "C. albicans verde", "cromo-candida")]),
 (48, "conteudo", "Testes de sensibilidade", [("tsa-ab", "Disco-difusão, CIM (microdiluição, Etest), automatizados", "antibiograma")]),
 (49, "conteudo", "Cromogênicos para MRSA e VRE", [("mrsa", "MRSA e VRE", "mrsa-vre")]),
 (50, "capa", "Encerramento", []),
]
JUSTIFICATIVAS = {"capa": "capa ou encerramento, sem conteúdo"}

CAPITULO = [("Trabulsi 6ª ed., caps. 3 (nutrição e metabolismo) e 4 (crescimento)", [
   ("tb-classificacao", "Classificação nutricional; quimio-heterotróficos", "quimio-hetero"),
   ("tb-temperatura", "Psicrófilos, mesófilos, termófilos", "mesofilos"),
   ("tb-fases", "Fases da curva; tempo de geração (E. coli ~20 min)", ["curva-fases", "log-geracao", "geracao-ecoli"]),
   ("tb-energia", "Fermentação × respiração", ["substrato", "respiracao-anaerobia"])])]

EXERCICIOS = [
 ("Provas UC03 (índice micro-02)", [
   ("p-curva", "2015–2025: construir e interpretar a curva (lag, log, estacionária, declínio)", ["curva-fases", "lag", "estacionaria", "declinio"]),
   ("p-geracao", "2018 P1 1.9 e 2025 P2 3.2: fase log depende do tempo de geração (E. coli × M. tuberculosis)", ["log-geracao", "geracao-ecoli"]),
   ("p-antibiotico", "2024 P2 1.10 e 2019 P2 2.4: antibiótico mais eficaz na fase log", "antibiotico-log"),
   ("p-lag", "2023 P2 1.4: cultura demora pela fase lag", "lag")]),
 ("Monitoria P1, aula 2", [
   ("mon-binaria", "Divisão binária; tempo de geração; crescimento em PG", ["crescimento-def", "log-geracao"]),
   ("mon-quorum", "Estacionária por limitação de nutrientes e quorum sensing", "estacionaria"),
   ("mon-turbidez", "Quantificação por turvação (espectrofotômetro)", "turbidez")]),
]
