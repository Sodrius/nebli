"""Inventário atômico de Micoses superficiais e cutâneas (UC03 P3, Microbiologia; aula de 2026 do Prof. Benedito Corrêa, 55 lâminas,
Drive pessoal 44 - Micoses cutâneas). Escrito em 10/10/2026 antes da seleção, a partir de: lâminas 2026 (visual/folha-01..10,
fontes/slides.txt, objetivos na lâmina 55); material da pasta da turma (Taborda 2024/2020 e "transcrição", fontes/turma/), usado como
complementar; monitoria P2 aula 10 (fontes/monitoria-p2.txt pp. 59–60); provas do índice micro-09 (fontes/provas.txt); Trabulsi
(livros/trabulsi-micoses-superficiais-cutaneas.txt). Cada ideia aponta para o card que a pergunta.
"""
PREFIXO = "mb44"
AULA = "Micoses superficiais e cutâneas (UC03 P3; Prof. Benedito Corrêa, 2026)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Três tipos de manifestação dos fungos", [("tipos", "Alergia, toxicose (micetismo/micotoxicose) e infecção", "tipos-doenca")]),
 (3, "conteudo", "Classificação: superficiais e cutâneas", [
   ("superficial-pv", "Superficial: pitiríase versicolor (Malassezia)", "classificacao"),
   ("cutaneas", "Cutâneas: dermatófitos (Trichophyton, Nannizzia, Epidermophyton) e candidose", ["classificacao", "dermatofitos-tinea"])]),
 (4, "conteudo", "Classificação: subcutâneas e sistêmicas", [("subcut-sist", "Esporotricose; histoplasmose, PCM, criptococose, candidose, aspergilose",
   EXC + "lista das aulas seguintes (micoses subcutâneas e sistêmicas), sem alvo desta aula")]),
 (5, "conteudo", "Aspectos gerais", [
   ("def-superficial", "Micose superficial: restrita ao estrato córneo, pouca ou nenhuma resposta imune", ["superficial-imune", "estrato-corneo-pv"]),
   ("def-dermatofitose", "Dermatofitose: dermatófitos que usam queratina; pele, pelos, unhas", "dermatofitose-def"),
   ("piedra-negra", "Piedra negra", "piedra-negra"), ("piedra-branca", "Piedra branca", "piedra-branca"), ("tinha-negra", "Tinha negra", "tinea-nigra"),
   ("nao-dermatofitos", "Micoses cutâneas por não dermatófitos e candidíase", ["classificacao", "nao-dermatofitos"])]),
 (6, "conteudo", "Anatomia da pele", [("pele", "Epiderme, derme e subcutâneo com microbiota", EXC + "figura de revisão de histologia da pele, sem alvo próprio")]),
 (7, "conteudo", "Epidemiologia global", [("prevalencia", "20–25% da população; 30–70% portadores assintomáticos", "portadores")]),
 (8, "conteudo", "Habitat", [
   ("habitat", "Geofílicos, zoofílicos, antropofílicos", "habitat"),
   ("graves", "Geofílicos e zoofílicos são mais ancestrais e causam infecção mais grave", "geofilico-grave")]),
 (9, "conteudo", "Fontes de infecção", [
   ("direta", "Transmissão direta (animais, pessoas)", "pets"),
   ("indireta", "Transmissão indireta (pisos, objetos)", "transmissao-indireta")]),
 (10, "conteudo", "Localização por gênero", [("localizacao", "Trichophyton pele/pelo/unha; Microsporum sem unha; Epidermophyton sem pelo; Nannizzia sem unha", "localizacao")]),
 (11, "conteudo", "Fatores de virulência", [
   ("queratinase", "Queratinases", "sh-1791557945582"),
   ("outras", "Elastases, colagenase, desoxirribonuclease", "outras-enzimas")]),
 (12, "conteudo", "Patogenia", [
   ("inoculacao", "Inoculação de artroconídios/hifas em pele com lesão", "artroconidios"),
   ("centrifuga", "Crescimento circular e centrífugo na camada córnea", "crescimento-centrifugo"),
   ("limitada", "Limitada ao estrato córneo, que não tem imunidade específica, mas gera inflamação", ["estrato-corneo-inflamacao", "estrato-imunidade"])]),
 (13, "conteudo", "Patogenia: fatores do fungo e do hospedeiro", [
   ("hospedeiro", "Integridade da epiderme, umidade, calçado, populações fechadas", ["atletas", "umidade"]),
   ("imunidade", "Fatores imunológicos do hospedeiro", "imunidade-t")]),
 (14, "conteudo", "Tinea corporis", [
   ("corporis", "Lesões anulares no corpo", ["tinea-corporis", "corporis-imagem"]),
   ("ringworm", "Tinha = ringworm, pruriginosa", ["tinea-corporis", "pruriginosa"])]),
 (15, "conteudo", "Tinea corporis (extensa)", [("corporis-extensa", "Lesões confluentes", "corporis-imagem")]),
 (16, "conteudo", "Tinea pedis", [("pedis", "Pés, espaços interdigitais", "tinea-pedis")]),
 (17, "conteudo", "Tinha imbricata", [("imbricata", "Trichophyton concentricum", "imbricata")]),
 (18, "conteudo", "Tinea pedis (fotos)", [("pedis-fotos", "Formas plantares/interdigitais", "tinea-pedis")]),
 (19, "conteudo", "Tinea cruris", [("cruris", "Região inguinal", ["tinea-cruris", "recorrencia-cruris"])]),
 (20, "conteudo", "Tinea cruris (foto)", [("cruris-foto", "Placa de borda ativa", "tinea-cruris")]),
 (21, "conteudo", "Tinea manum", [("manum", "Mãos", "tinea-manum")]),
 (22, "conteudo", "Trichophyton indotineae", [
   ("indotineae", "Dermatofitose emergente; 1º caso no Brasil", "indotineae"),
   ("sqle", "Mutação em esqualeno epoxidase → resistência à terbinafina", ["indotineae", "alilaminas"])]),
 (23, "conteudo", "Dermatofítides", [("ide", "Lesões à distância nas mãos (reação a antígenos)", "dermatofitide")]),
 (24, "conteudo", "Tinea unguium", [("unguium", "Onicomicose por dermatófito", "onicomicose")]),
 (25, "conteudo", "Patogenia da onicomicose", [("distal", "Dermatófito: distal → proximal; levedura: prega proximal", "onicomicose-distal")]),
 (26, "conteudo", "Tinea unguium (foto)", [("unguium-foto", "Unhas espessadas e distróficas", "onicomicose")]),
 (27, "conteudo", "Onicomicose por Candida", [("candida-unha", "Candida na unha", "onicomicose-distal")]),
 (28, "conteudo", "Candidose oral", [("sapinho", "C. albicans: estomatite cremosa (sapinho)", ["sapinho", "candida-t"])]),
 (29, "conteudo", "Candidose cutânea", [("cutanea", "Perioral e interdigital", ["candidiase-cutanea", "intertrigo"])]),
 (30, "conteudo", "Tinea capitis", [("capitis", "Microsporum canis e Trichophyton tonsurans", ["tinea-capitis", "capitis-tonsurans"])]),
 (31, "conteudo", "Dermatofitose por M. canis em cão", [("canis", "Animais como fonte (M. canis)", "canis-animais")]),
 (32, "conteudo", "Diagnóstico e identificação", [
   ("etapas", "Exame direto/histopatológico, cultura, identificação macro e micro", ["koh-hifas", "cicloheximida", "canis-macroconidio"]),
   ("its", "Sequenciamento da região ITS", "its"),
   ("complementares", "Sorologia e testes intradérmicos", EXC + "citados como complementares, sem detalhe na aula")]),
 (33, "conteudo", "Prevalência no Brasil", [("rubrum", "T. rubrum predomina (66%); T. pedis e unguium mais comuns", "rubrum-prevalencia")]),
 (34, "conteudo", "Cultivo", [
   ("meios", "Sabouraud + cloranfenicol + cicloheximida (Mycosel), DTM", "cicloheximida"),
   ("condicoes", "25 °C por 1–2 semanas", "cultivo-25")]),
 (35, "conteudo", "Técnica do carpete", [("carpete", "Isolamento em animais sadios", "carpete")]),
 (36, "conteudo", "Coleta de amostras", [("coleta", "Pele (borda), pelo, unha", "coleta-borda")]),
 (37, "conteudo", "Exame direto com KOH", [("koh", "KOH 10–40%: hifas septadas hialinas", ["koh-hifas", "koh-onicomicose"])]),
 (38, "conteudo", "Filamentos de dermatófitos", [("filamentos", "Hifas no micológico direto", "koh-hifas")]),
 (39, "conteudo", "Microsporia", [("microsporia", "Pelo parasitado por M. canis (ectotrix)", "ectothrix")]),
 (40, "conteudo", "Tricofícia", [("tricoficia", "Pelo parasitado por Trichophyton (endotrix)", ["endotrix", "ectothrix"])]),
 (41, "conteudo", "Exame direto e cultivo", [("resumo", "KOH + cultivo de M. canis e N. gypsea", ["koh-hifas", "canis-macroconidio", "gypsea"])]),
 (42, "conteudo", "Microcultivo", [("microcultivo", "Técnica de microcultivo", "microcultivo")]),
 (43, "conteudo", "M. canis", [("canis-micro", "Colônia amarela; macroconídios fusiformes de parede grossa", "canis-macroconidio")]),
 (44, "conteudo", "M. gypseum", [("gypsea-micro", "Macroconídios elipsoides de parede fina", "gypsea")]),
 (45, "conteudo", "T. mentagrophytes", [("mentagrophytes", "Microconídios em cacho", "mentagrophytes")]),
 (46, "conteudo", "T. rubrum", [("rubrum-micro", "Reverso vermelho; microconídios em gota", "rubrum-reverso")]),
 (47, "conteudo", "E. floccosum", [("floccosum", "Macroconídios em clava, sem microconídios", "epidermophyton")]),
 (48, "conteudo", "Micoses superficiais: pitiríase versicolor", [("pv-agente", "Malassezia spp. (furfur, globosa, restricta, obtusa)", "malassezia-pv")]),
 (49, "conteudo", "Pitiríase versicolor (fotos)", [("pv-clinica", "Manchas hipo/hipercrômicas no tronco", ["pv-manchas", "pv-tronco"])]),
 (50, "conteudo", "Epidemiologia da PV", [
   ("pv-epi", "Adultos e adolescentes (mais oleosidade); até 60% nos trópicos", ["pv-sebo", "furfur-flora"]),
   ("pv-mecanismo", "Ácidos da degradação de lipídeos alteram a pigmentação (monitoria)", "pv-acido")]),
 (51, "conteudo", "Malassezia no exame direto", [("pv-koh", "Leveduras agrupadas e hifas curtas (espaguete e almôndegas)", "spaghetti")]),
 (52, "conteudo", "M. furfur: colônia e leveduras", [("lipo", "Colônias em meio com lipídeos", "lipodependente")]),
 (53, "conteudo", "Candidíase: exame direto", [("candida-direto", "Leveduras e hifas/pseudo-hifas", ["koh-candida", "pseudohifas"])]),
 (54, "conteudo", "Candidíase: isolamento", [("candida-cultura", "Sabouraud + cloranfenicol: colônias cremosas", ["candida-sabouraud", "pseudohifas"])]),
 (55, "conteudo", "Objetivos", [("objetivos", "Exemplos, definição, habitat, fontes e localização, virulência, diagnóstico, PV",
   ["classificacao", "dermatofitose-def", "habitat", "localizacao", "sh-1791557945582", "koh-hifas", "malassezia-pv"])]),
]

CAPITULO = [("Trabulsi, micoses (aspectos gerais e diagnóstico)", [
   ("tb-transmissao", "Dermatofitoses transmitidas de homem, animal ou solo", ["habitat", "transmissao-indireta"]),
   ("tb-enzimas", "Queratinases, elastases, sulfitase na implantação", ["sh-1791557945582", "outras-enzimas"]),
   ("tb-koh", "Exame direto com KOH é o método mais usado", "koh-hifas"),
   ("tb-ecto", "Pelo: artroconídios ecto, endo ou ectoendotrix", "ectothrix"),
   ("tb-pv-cultura", "Malassezia cresce em meio com azeite (lipídeos)", "lipodependente")])]

EXERCICIOS = [
 ("Provas UC03 (índice micro-09)", [
   ("p2025", "2025 P3 4.4: patogenia das superficiais (queratinólise, inflamação local) e imunossupressão", ["estrato-corneo-inflamacao", "imunidade-t", "sh-1791557945582"]),
   ("p2024", "2024 P3 2.6: levedura × dermatófito (filamentoso, conídios)", "filamentoso"),
   ("p2019", "2019 P2 3.1: gêneros e fontes de contato dos dermatófitos", ["habitat", "pets", "localizacao"])]),
 ("Monitoria P2, aula 10", [
   ("mon-queratinase", "Dermatófitos degradam queratina com queratinase", "sh-1791557945582"),
   ("mon-transmissao", "Contato direto e objetos (piso, tesoura)", "transmissao-indireta"),
   ("mon-pv", "Malassezia inibe melanina; manchas em cacho de uva", ["pv-acido", "spaghetti"]),
   ("mon-piedras", "Piedra branca (Trichosporon) × negra (Piedraia hortae)", ["piedra-branca", "piedra-negra"]),
   ("mon-tinea-nigra", "Tinea nigra por Hortaea werneckii", "tinea-nigra"),
   ("mon-unhas", "Unhas atingidas da porção distal para a proximal", "onicomicose-distal"),
   ("mon-ide", "Dermatofítides: lesões à distância nas mãos", "dermatofitide"),
   ("mon-candida", "Candida em unhas, interdígitos e dobras", "intertrigo")]),
]
