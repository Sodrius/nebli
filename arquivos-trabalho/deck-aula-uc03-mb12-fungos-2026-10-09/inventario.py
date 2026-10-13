"""Inventário atômico da Biologia geral dos fungos (61 lâminas, Taborda), refeito em 09/10 à tarde (F-20261009-CLAUDE-02) para
python3 -m nebli.inventario. Fontes lidas inteiras antes da seleção: lâminas (visual/folha-01..11, fontes/slides.txt), apostila de
veteranos aula 8 (fontes/veterano-microbio.txt pp. 35–36), monitoria P2 aula 9 (fontes/monitoria-p2.txt pp. 55–58), apresentação do
Prof. Benedito Correa (fontes/transcricao.txt), Trabulsi 64.1–64.2, provas 2017 P2, 2018 P2, 2024 P3, 2025 P3 (fontes/provas).
A versão anterior (inventario-antes-completude.py) ligava ideias a cards que não as cobram (imóveis → eucarioto, pH → mesófilos,
liquens → sapróbios, Whittaker → glicogênio); aqui cada ideia aponta para o card que a pergunta.
"""
PREFIXO = "mb43"
AULA = "Biologia geral dos fungos (UC03, aula 43; Prof. Carlos P. Taborda)"
EXC = "EXC: "
JUSTIFICATIVAS = {"revisao": "revisão de biologia celular/geral, sem alvo novo desta aula"}

SLIDES = [
 (1, "capa", "Capa (Taborda, ICB)", []),
 (2, "capa", "Abertura do bloco 'Fungos, vida humana e natureza'", []),
 (3, "conteudo", "Agentes fermentadores", [("fermentacao", "Leveduras fermentam açúcar (pão, cerveja, vinho)", "fermentacao"),
   ("importancia", "Importância médica crescente dos fungos", "importancia-medica")]),
 (4, "conteudo", "Fungos comestíveis", [("comestiveis", "Fungos comestíveis e queijos", "queijos")]),
 (5, "conteudo", "Antibióticos naturais", [("antibioticos", "Penicilina obtida do Penicillium", "penicilina")]),
 (6, "conteudo", "Fungos bioluminescentes", [("bioluminescencia", "Bioluminescência com uso biotecnológico", EXC + "curiosidade em foto, sem texto além do título")]),
 (7, "conteudo", "Decomposição e micorrizas", [
   ("decompositor", "Decomposição de matéria orgânica (sapróbios)", "saprofita"),
   ("micorriza", "Associação com raiz de planta: micorrizas", "micorriza")]),
 (8, "conteudo", "Síndrome dos edifícios doentes", [("edificios", "Fadiga, cefaleia, irritação de olhos/nariz/vias aéreas em >20% dos ocupantes", "edificios")]),
 (9, "conteudo", "Decomposição de alimentos", [("mofo-pao", "Rhizopus, mofo do pão", "rhizopus-pao")]),
 (10, "conteudo", "Micotoxinas", [
   ("micotoxicose", "Micotoxinas em alimentos causam micotoxicose", "micotoxicose"),
   ("micotoxina-graos", "Aflatoxina em grãos e nozes mal armazenados", "aflatoxina-graos")]),
 (11, "conteudo", "Doença do algodão e síndrome do nariz branco", [("animais", "Fungos causam doença em peixes e morcegos", EXC + "exemplos em foto de doença animal, fora do recorte médico")]),
 (12, "conteudo", "Doenças de plantas", [("plantas", "Fungos fitopatogênicos", EXC + "lâmina só com fotos")]),
 (13, "conteudo", "Insetos", [("insetos", "Fungos parasitam insetos", EXC + "fotos ilustrativas")]),
 (14, "conteudo", "Quitrídios em anfíbios", [("quitridio", "Quitrídios (Chytridiomycota) aquáticos", EXC + "ilustração de anfíbios; Davi: 'não teve isso na aula' (comentário 10/10)")]),
 (15, "conteudo", "Extinção dos dinossauros?", [("dinossauros", "Hipótese fungos × dinossauros; endotermia", "endotermia")]),
 (16, "conteudo", "Chernobyl: melanina e radiação", [("melanina-radiacao", "Fungos melanizados crescem mais sob radiação ionizante", "melanina")]),
 (17, "conteudo", "Classificação histórica", [
   ("whittaker", "Antes de 1969 em Plantae; Whittaker 1969 cria o reino Fungi", "whittaker"),
   ("woess", "Woese 1994: árvore por sequência de DNA", "animais")]),
 (18, "conteudo", "Árvore filogenética", [("animais-proximos", "Fungos mais próximos de animais que de plantas", "animais")]),
 (19, "conteudo", "Aspectos macroscópicos", [
   ("colonia-bolor", "Bolores: algodonosa, aveludada, pulverulenta", "colonias"),
   ("colonia-levedura", "Leveduras: cremosa, pastosa, cerebriforme", "colonias")]),
 (20, "conteudo", "Diferenças em relação às plantas", [
   ("sem-clorofila", "Sem clorofila", "heterotrofo"),
   ("sem-celulose", "Sem celulose na parede (exceto aquáticos)", "quitina"),
   ("sem-amido", "Não armazenam amido; glicogênio", "glicogenio"),
   ("quitina-animais", "Quitina e glicogênio os aproximam dos animais", ["quitina", "glicogenio"])]),
 (21, "conteudo", "Características dos fungos", [
   ("eucariontes", "Eucariontes", "eucarioto"),
   ("parede", "Parede com quitina e β-glucana", "quitina"),
   ("imoveis", "Imóveis", "imoveis"),
   ("absortivos", "Absortivos", "exoenzimas"),
   ("glicogenio", "Armazenam glicogênio", "glicogenio"),
   ("nao-fotossinteticos", "Não fotossintéticos", "heterotrofo"),
   ("sem-tecido", "Não formam tecido verdadeiro", "sem-tecido"),
   ("uni-pluri", "Unicelulares ou pluricelulares", ["levedura-bolor", "hifas", "hifa-septada"]),
   ("lisina", "Lisina pela via do ácido aminoadípico", "lisina"),
   ("cristas", "Cristas mitocondriais achatadas", "cristas")]),
 (22, "conteudo", "Estrutura da célula fúngica", [
   ("parede-protecao", "Parede: proteção e forma; melanina", ["parede-funcao", "quitina", "melanina"]),
   ("ergosterol", "Membrana com ergosterol", "ergosterol"),
   ("nucleo-linear", "Núcleo com cromossomo linear e membrana nuclear", "dna-linear"),
   ("organelas", "Mitocôndria, RE, Golgi, ribossomos", "ribossomo-80s"),
   ("capsula", "Cápsula (Cryptococcus)", ["capsula", "capsula-fagocitose"])]),
 (23, "conteudo", "Camadas da parede", [("camadas", "Externa manana/proteína; interna glucanas e quitina", ["quitina", "parede-camadas"])]),
 (24, "conteudo", "Parede por espécie", [("parede-especies", "Composição varia (cápsula, melanina, α-1,3-glucana)", "alfa-glucana")]),
 (25, "revisao", "Modelo geral de membrana", []),
 (26, "conteudo", "Membrana dos fungos", [("membrana-ergosterol", "Ergosterol na membrana fúngica", "ergosterol")]),
 (27, "conteudo", "Antifúngicos e alvos", [
   ("equinocandina", "Equinocandinas inibem a síntese de β-glucana", "equinocandina"),
   ("polieno", "Polienos ligam ergosterol e formam poros", "polienos"),
   ("polieno-eletrolitos", "Vazamento de K+ e Na+", "polienos"),
   ("polieno-toxicidade", "Toxicidade em mamíferos", "anfo-toxicidade"),
   ("azois", "Azóis inibem a síntese de ergosterol", "azois"),
   ("flucitosina", "5-FC vira 5-FU e inibe DNA", "flucitosina-5fu"),
   ("flucitosina-medula", "Mielossupressão", "flucitosina-medula")]),
 (28, "capa", "Abertura: base da taxonomia", []),
 (29, "revisao", "Hierarquia taxonômica (reino → espécie)", []),
 (30, "conteudo", "Estados do ciclo", [
   ("anamorfo", "Estado anamórfico = assexuado", "teleomorfo"),
   ("teleomorfo", "Estado teleomórfico = sexuado", "teleomorfo")]),
 (31, "conteudo", "Dificuldades da taxonomia", [
   ("especies", "~100 mil espécies descritas, ~5,1 milhões existentes", "molecular"),
   ("nomes-fases", "Fases com nomes distintos; nome sexuado tem prioridade", "nome-sexuado"),
   ("molecular", "Técnicas moleculares essenciais", "molecular")]),
 (32, "conteudo", "Filos clássicos", [("filos-classicos", "Zygo, Basidio, Asco, Deutero; Oomycota em Chromista", ["zigosporo", "basidio", "asco", "deuteromycetes", "oomycetes"])]),
 (33, "conteudo", "Myxomycota × Eumycota", [("myxo", "Fungos do lodo agora em Protista; Eumycota = verdadeiros", "mixomicetos")]),
 (34, "conteudo", "Taxonomia dos anos 2000", [("dikarya", "Subreino Dikarya = Asco + Basidio", "filos-medicos")]),
 (35, "conteudo", "Proposta 2019: 9 filos", [
   ("medicos-asco-basidio", "Asco e Basidio: maior parte dos fungos de interesse médico", "filos-medicos"),
   ("mucoromycota", "Mucoromycota: Mucor, Rhizopus, Lichtheimia", "mucoromycota"),
   ("zoopago", "Zoopagomycota: Conidiobolus e Basidiobolus", "zoopagomycota")]),
 (36, "capa", "Abertura: reprodução das leveduras", []),
 (37, "conteudo", "Reprodução das leveduras", [
   ("brotamento", "Brotamento", "brotamento"),
   ("cissiparidade", "Cissiparidade", "brotamento"),
   ("pseudomicelio", "Pseudomicélio", "pseudohifa"),
   ("blastoconidio", "Blastoconídio", "brotamento"),
   ("clamidoconidio", "Clamidoconídio", "clamidoconidio"),
   ("ascos-levedura", "Sexuada: ascos com ascósporos", "asco")]),
 (38, "conteudo", "Etapas do brotamento", [("etapas", "Núcleo divide e migra para o broto, que se separa", "brotamento")]),
 (39, "conteudo", "Pseudo-hifas na Candida", [("candida", "Pseudo-hifas na invasão por Candida", "candida-pseudohifa")]),
 (40, "conteudo", "Reprodução blástica", [("pseudohifa-def", "Gêmulas que não se separam = pseudo-hifas", "pseudohifa")]),
 (41, "capa", "Abertura: reprodução dos bolores", []),
 (42, "conteudo", "Reprodução assexuada dos bolores", [("assexuada-bolor", "Esporos assexuados nas hifas aéreas", ["conidios", "micelio-vegetativo"])]),
 (43, "conteudo", "Conídios externos", [
   ("conidio", "Conídios externos no conidióforo", "conidios"),
   ("vesicula", "Aspergillus: conidióforo com vesícula", "aspergillus-conidioforo"),
   ("macro-micro", "Macroconídio, microconídio, conídios sésseis", "macro-microconidio")]),
 (44, "conteudo", "Conídios internos (Rhizopus)", [
   ("esporangio", "Esporangiósporos no esporângio, sobre o esporangióforo", ["esporangio", "conidio-esporangio"]),
   ("hifa-vegetativa", "Hifa vegetativa", "micelio-vegetativo")]),
 (45, "conteudo", "Dimorfismo térmico", [
   ("temperaturas", "35–37 °C levedura; 25–27 °C bolor", "dimorfismo-temperatura"),
   ("ambiente-hospedeiro", "Bolor no ambiente, levedura no hospedeiro", "dimorfismo"),
   ("paracocci", "Paracoccidioides brasiliensis", "paracocci-dimorfico")]),
 (46, "conteudo", "Reprodução sexuada", [
   ("gametas-flagelados", "Fungos aquáticos com gametas flagelados", EXC + "detalhe de fungos aquáticos sem alvo médico"),
   ("plasmogamia", "Plasmogamia", "sexuada"),
   ("dicariotico", "Fase heterocariótica/dicariótica n + n", "dicario"),
   ("cariogamia-meiose", "Cariogamia e meiose geram esporos sexuados", "sexuada")]),
 (47, "capa", "Abertura: estruturas reprodutivas na classificação", []),
 (48, "conteudo", "Antigo filo Zygomycota", [
   ("sapro", "Sapróbios, eventualmente infecciosos", "mucor-hifa"),
   ("cenocitico", "Micélio cenocítico", ["septos", "mucor-hifa"]),
   ("zigosporo", "Reprodução sexuada (zigosporângio)", "zigosporo")]),
 (49, "conteudo", "Pilobolus", [("pilobolus", "Esporângios explosivos em fezes de gado", EXC + "exemplo em foto, curiosidade")]),
 (50, "conteudo", "Filo Basidiomycota", [("basidio", "Cogumelos; basidiósporos no basídio (basidioma)", "basidio")]),
 (51, "conteudo", "Amanita e Geastrum", [("amanita", "Amanita altamente venenosa (micetismo)", "micotoxicose")]),
 (52, "conteudo", "Filo Ascomycota", [
   ("ascomycota", "Micro a macroscópicos, filamentosos ou leveduriformes", "asco"),
   ("asco", "Ascósporos dentro do asco, em ascomas", "asco")]),
 (53, "conteudo", "Pezizaceae", [("apotecio", "Apotécio em forma de copo", EXC + "exemplo em foto")]),
 (54, "capa", "Abertura: ecologia e nutrição", []),
 (55, "conteudo", "Vias de dispersão", [
   ("dispersao", "Ar, água, homem, animais, insetos", "anemofilos"),
   ("inalacao", "Infecção por inalação de propágulos", "anemofilos")]),
 (56, "conteudo", "Nutrição por absorção", [
   ("exoenzimas", "Exoenzimas degradam macromoléculas; transporte", "exoenzimas"),
   ("queratinase", "Queratinases", "queratinase")]),
 (57, "conteudo", "Nutrientes", [
   ("carbono-nitrogenio", "Carbono (glicose), nitrogênio (nitrato, NH4, peptona)", "nutrientes"),
   ("oligoelementos", "Fe, Zn, Mn, Cu, Ca; vitaminas", "nutrientes")]),
 (58, "conteudo", "Temperatura", [
   ("mesofilos", "Fungos médicos mesófilos (20–30 °C)", "mesofilos"),
   ("dimorficos", "Dimórficos: 22–28 °C filamentosos; 33–37 °C leveduriformes", "dimorfismo-temperatura")]),
 (59, "conteudo", "Umidade e atividade de água", [("aw", "Aw 0,65: fungos não crescem", "atividade-agua")]),
 (60, "conteudo", "pH", [("ph", "pH ótimo ~6,5; leveduras 2,5–8,5; filamentosos 1,5–11", "ph")]),
 (61, "conteudo", "Liquens", [("liquen", "Mutualismo fungo + alga/cianobactéria (micobionte, fotobionte)", "liquen")]),
]

CAPITULO = [
 ("Trabulsi 64.1–64.2", [
   ("parede-dimorfica", "Fase M (25 °C) mais β-glucana; fase Y (37 °C) mais α-glucana", "alfa-glucana"),
   ("hifas", "Hifa septada × cenocítica; micélio vegetativo × aéreo", ["septos", "micelio-vegetativo"]),
   ("clamidoconidio", "Clamidoconídio, estrutura de resistência", "clamidoconidio"),
   ("dispersao-ar", "Ar é a principal via; anemófilos e alergias", "anemofilos")]),
]

EXERCICIOS = [
 ("Provas UC03", [
   ("fungo-bacteria", "2017 P2 2.5: fungo × bactéria (tamanho, núcleo, 80S, mitocôndria, parede, motilidade)", ["tamanho", "eucarioto", "ribossomo-80s", "imoveis"]),
   ("parede-bacteria", "2018 P2 1.3: parede fúngica (glucana, quitina) × peptideoglicano", "quitina"),
   ("fatores", "2018 P2 1.4: temperatura, umidade, pH", ["mesofilos", "atividade-agua", "ph"]),
   ("brotamento", "2017 P2 2.4: brotamento, reprodução assexuada da levedura", "brotamento"),
   ("dimorfismo", "2017 P2 2.6 e 2018 P2 1.1: dimorfismo térmico", ["dimorfismo-temperatura", "dimorfismo"]),
   ("capsula", "2024 P3 2.5: vantagens da cápsula", "capsula-fagocitose"),
   ("parede-dimorfismo", "2025 P3 1.2: parede no dimorfismo (α × β-glucana)", "alfa-glucana"),
   ("microconidios", "2025 P3 1.1: microconídios inalados", "macro-microconidio")]),
 ("Apostila de veteranos, aula 8", [
   ("saprofitas-parasitas", "Saprofíticos (matéria morta) × parasitários (viva)", "saprofita"),
   ("quitina-levedura", "Leveduras têm menos quitina que bolores", "quitina-levedura"),
   ("membrana-efeitos", "Membrana parecida com a humana: antifúngicos com efeitos colaterais", "anfo-toxicidade"),
   ("micelio", "Conjunto de hifas = micélio; vegetativo × aéreo/reprodutivo", ["micelio", "micelio-vegetativo"]),
   ("aerobios", "Maioria aeróbios obrigatórios; leveduras fermentadoras facultativas", "aerobios"),
   ("luz", "Vegetativo no escuro; reprodução precisa de luz; sol direto fungicida", "luz"),
   ("umidade", "Precisam de muita umidade; controle em silos e museus", "atividade-agua")]),
 ("Monitoria P2, aula 9", [
   ("pleomorfismo", "Pleomorfismo (independe de temperatura) × dimorfismo", "pleomorfismo"),
   ("crescimento-apical", "Hifas crescem pelas pontas; fragmentos originam novo fungo", "crescimento-apical"),
   ("fissao", "Brotamento (células desiguais) × fissão binária (iguais)", "brotamento"),
   ("zigosporo", "Zigomicetos: esporangiósporos (assexuados) e zigósporos (sexuados)", "zigosporo")]),
 ("Benedito Correa (material complementar)", [
   ("micetismo", "Intoxicações: micetismo × micotoxicoses", "micotoxicose"),
   ("esporos-ecto-endo", "Esporos externos (conídio, basidiósporo) × internos (esporangiósporo, ascósporo)", ["conidios", "esporangio", "basidio", "asco"]),
   ("anemofilos", "Fungos anemófilos e alergias respiratórias", "anemofilos")]),
]
