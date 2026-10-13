"""Inventário atômico de Inflamação aguda (UC03 P2, Patologia; Prof. Luiz Fernando Ferraz da Silva, 43 lâminas), escrito a partir do material de base lido:
lâminas (visual/folha-01..08, fontes/slides.txt), transcrição da turma (idêntica ao texto das lâminas), palavras-cruzadas e gabarito, bibliografia da aula
(vídeos dispensados; artigo de inflamassomas), monitoria P2 aula 7, apostila de veteranos (Guia de Patologia, aula 8; UC3.pdf, inflamação aguda), provas
(índice pat-07-inflamacao-aguda) e Robbins (cap. 2, pp. 43-69).
Cada ideia aponta para o card que a pergunta (chave do spec, lista, "sh-<nid>" ou "EXC: motivo" só em lâmina). Menção no verso não conta.
"""
PREFIXO = "pt38"
AULA = "Inflamação aguda (UC03 P2; Prof. Luiz Fernando Ferraz da Silva)"
EXC = "EXC: "
SIGNS = ["sh-1791743340881", "sh-1791743341010", "sh-1791743341134", "sh-1791743341258", "sh-1791743341385"]
AA = ["sh-1791743344484", "sh-1791743344682", "sh-1791743345233", "sh-1791743345958", "sh-1791743346434", "sh-1791743345060", "sh-1791743345583", "sh-1791743344934"]
FIG_EXT = ["passo-1", "passo-2", "passo-3", "passo-4", "selectina-sialyl", "adesao-integrina", "pecam", "quimioatraentes"]

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Definição e sinais", [
   ("def", "Resposta inicial ao dano tecidual visando restabelecer a homeostase", "def"),
   ("sinais", "Sinais flogísticos: calor, rubor, tumor, dor, perda funcional", SIGNS),
   ("mecanismo-sinais", "Rubor e calor por vasodilatação; dor por lesão e mediadores", ["rubor-calor", "dor-mecanismo"]),
   ("foto-pe", "Foto clínica do pé inflamado", EXC + "foto clínica ilustra os sinais, sem card de foto clínica (MEMORY 10/10); os sinais têm cards próprios"),
   ("ite", "Sufixo -ite para inflamação", "sufixo-ite")]),
 (3, "conteudo", "Desencadeantes", [
   ("causas", "Infecções, necrose tecidual, corpo estranho", "causas"),
   ("causas2", "Reações de hipersensibilidade, agentes químicos e físicos", "causas-outras"),
   ("marca", "Edema e neutrófilos marcam a inflamação aguda", ["edema-neutrofilos", "neutrofilo-celula"])]),
 (4, "conteudo", "Alterações iniciais (figura vascular)", [
   ("sequencia", "Vasoconstrição breve, vasodilatação arteriolar, aumento do leito capilar", "sh-1791743342383"),
   ("tres", "Fluxo aumentado, extravasamento de proteínas (edema) e emigração de neutrófilos", "tres-componentes")]),
 (5, "conteudo", "Alterações iniciais (receptores e inflamassoma)", [
   ("prr", "Receptores de reconhecimento de padrões e PAMPs", "prr"),
   ("tlr", "TLRs de superfície e endossomais, ativação de NF-κB e citocinas", ["sh-1791743339611", "sh-1791743339358", "sh-1791743339982"]),
   ("inflamassoma", "Inflamassoma NLRP3, efluxo de K+, cristais, IL-1β", ["sh-1791743339740", "sh-1791743339860", "sh-1791743340632", "nlrp3-asc"]),
   ("damps", "DAMPs da necrose", "sh-1791743340457"),
   ("piroptose", "Caspase-1 e piroptose (bibliografia II)", "piroptose")]),
 (6, "conteudo", "Exsudato × transudato (figura)", [
   ("exsudato", "Exsudato por aumento de permeabilidade com vasodilatação e estase", "exsudato-def"),
   ("transudato", "Transudato por pressão hidrostática aumentada ou oncótica diminuída", ["transudato-def", "transudato-causas"])]),
 (7, "conteudo", "Exsudato × transudato (tabela)", [
   ("proteina", "Proteína maior que 3 g/dL no exsudato", "exsudato-proteina"),
   ("densidade", "Densidade maior que 1020", "exsudato-densidade"),
   ("celulas", "Células frequentes no exsudato, raras no transudato", ["exsudato-def", "transudato-def"]),
   ("dhl", "DHL maior que 200 no exsudato", ["exsudato-ldh", "transudato-ldh"]),
   ("foto-exsudato", "Foto de exsudato fibrinopurulento em serosa", EXC + "foto de peça com exsudato, sem rótulo; o conceito está nos cards de exsudato e pus"),
   ("pus", "Pus: exsudato purulento (palavras-cruzadas)", ["pus-def", "sh-1791577164590"]),
   ("derrame", "Derrame exsudativo por permeabilidade aumentada", "sh-1791169089006")]),
 (8, "conteudo", "Alterações de fluxo e calibre", [
   ("vasodilatacao", "Vasodilatação (calor e rubor) por histamina e NO", "sh-1791743341507"),
   ("arteriolas", "Vasodilatação arteriolar e abertura de capilares", "arteriolas"),
   ("estase", "Extravasamento, queda do fluxo, concentração de hemácias e viscosidade", "estase")]),
 (9, "conteudo", "Aumento da permeabilidade (I)", [
   ("contracao", "Contração endotelial em vênulas por histamina", ["sh-1791169090157", "contracao-rapida"]),
   ("lesao-direta", "Lesão endotelial direta por queimadura e toxinas", "lesao-direta"),
   ("tardio", "Extravasamento tardio e prolongado", "permeabilidade-tardia")]),
 (10, "conteudo", "Aumento da permeabilidade (II)", [
   ("leucocitos", "Lesão mediada por leucócitos", "lesao-leucocitos"),
   ("transcitose", "Transcitose induzida por VEGF", "transcitose")]),
 (11, "conteudo", "Resposta linfática", [
   ("linfa", "Proliferação e aumento da drenagem", "linfa"),
   ("linfadenopatia", "Relevância das linfadenopatias", ["linfadenopatia", "linfangite"])]),
 (12, "conteudo", "Mediadores importantes (vascular)", [
   ("histamina", "Histamina: mastócitos e plaquetas; vasodilatação e permeabilidade", ["histamina-fonte", "sh-1791743341507"]),
   ("pg", "Prostaglandinas: vasodilatação", "sh-1791743344808"),
   ("lt", "Leucotrienos: permeabilidade", "sh-1791169336677"),
   ("paf", "PAF: vasodilatação e permeabilidade", "paf"),
   ("no", "NO: endotélio e macrófagos; vasodilatação", "no-fonte"),
   ("cininas", "Bradicinina, calicreína, fator XII", ["sh-1791169090006", "sh-1791743344308", "sh-1791743344184"])]),
 (13, "conteudo", "Via do ácido araquidônico (figura)", [
   ("aa", "Fosfolipase A2, COX, 5-lipoxigenase, PG, TXA2, PGI2, leucotrienos", AA),
   ("farmacos", "Esteroides inibem fosfolipase; AINEs inibem COX", ["sh-1791743346434", "sh-1791743345958"])]),
 (14, "conteudo", "Histologia: congestão e estase", [("congestao", "Pulmão normal × congestão vascular e estase", "congestao-histologia")]),
 (15, "conteudo", "Células efetoras e complemento", [
   ("residentes", "Macrófago e mastócito (tecido)", ["residentes", "sh-1791743342260"]),
   ("neutrofilo", "Neutrófilo (recrutado)", "neutrofilo-celula"),
   ("plaquetas", "Plaquetas", "plaquetas"),
   ("eosinofilos", "Eosinófilos", ["eosinofilo", "eosinofilo-mbp"]),
   ("complemento", "Complemento: C3a/C5a (inflamação), C3b (fagocitose), MAC (lise)", ["sh-1791667097913", "sh-1791667098038", "sh-1791667096988", "sh-1791667096563"])]),
 (16, "conteudo", "Recrutamento (lista de etapas)", [
   ("estimulos", "Recrutamento por complemento, fatores plaquetários e citocinas", ["sh-1791667098038", "tnf-il1-endotelio"]),
   ("sequencia", "Marginação, rolamento, adesão, transmigração, quimiotaxia", ["passo-1", "passo-2", "passo-3", "passo-4"]),
   ("local", "Extravasamento em vênulas pós-capilares", "venulas-extravasamento")]),
 (17, "conteudo", "Figura das etapas (Robbins 2-4)", [("fig-etapas", "Moléculas de cada etapa: selectinas, integrinas, ICAM-1, PECAM-1", FIG_EXT)]),
 (18, "conteudo", "Marginação", [("marginacao", "Lentificação do fluxo e concentração de leucócitos", ["margina-periferia", "marginacao-causa"])]),
 (19, "conteudo", "Figura das etapas (repetição)", [("fig-etapas-b", "Mesma figura das etapas", FIG_EXT)]),
 (20, "conteudo", "Histologia: infiltrado neutrofílico", [("neutrofilos", "Neutrófilos no tecido", "neutrofilo-histologia")]),
 (21, "conteudo", "Rolamento", [
   ("selectinas", "Selectinas e Sialyl-Lewis", ["selectina-sialyl", "selectina-speed"]),
   ("baixa-afinidade", "Moléculas constitutivas do leucócito de baixa afinidade", "rolamento-fraco"),
   ("induzidas", "E e P-selectina induzidas; ativação endotelial por TNF e IL-1", ["e-selectina", "sh-1791743342733", "sh-1791743342910", "tnf-il1-endotelio"]),
   ("lad2", "LAD tipo 2 (Sialyl-Lewis X; Robbins)", "lad2")]),
 (22, "conteudo", "Figura das etapas (repetição)", [("fig-etapas-c", "Mesma figura das etapas", FIG_EXT)]),
 (23, "conteudo", "Adesão", [
   ("integrinas", "Integrina de alta afinidade e ligantes VCAM/ICAM; aderência firme", ["adesao-integrina", "icam-vcam", "icam-tnf", "integrina-afinidade", "sh-1791743343033"]),
   ("lad1", "LAD tipo 1 e ausência de pus (Robbins)", ["sh-1791743343209", "lad-pus"])]),
 (24, "conteudo", "Figura das etapas (repetição)", [("fig-etapas-d", "Mesma figura das etapas", FIG_EXT)]),
 (25, "conteudo", "Transmigração e diapedese", [
   ("pecam", "Permeabilidade aumentada e PECAM", "pecam"),
   ("citoesqueleto", "Alteração do citoesqueleto e metaloproteinases", "colagenase")]),
 (26, "conteudo", "Figura das etapas (repetição)", [("fig-etapas-e", "Mesma figura das etapas", FIG_EXT)]),
 (27, "conteudo", "Histologia: infiltrado e extravasamento", [("histo-miocardio", "Infiltrado neutrofílico em tecido", ["tempo-neutrofilos", "neutrofilo-histologia"])]),
 (28, "conteudo", "Quimiotaxia", [
   ("def", "Movimento progressivo ao longo do gradiente", "quimiotaxia-def"),
   ("agentes", "Produtos bacterianos e citocinas IL-8, C5a, LTB4", ["quimioatraentes", "formil"])]),
 (29, "conteudo", "Cinética do infiltrado (gráfico)", [
   ("cinetica", "Edema, neutrófilos e monócitos ao longo dos dias", ["cinetica", "tempo-neutrofilos", "sh-1791743342606"])]),
 (30, "conteudo", "Histologia: normal, congestão e infiltrado", [
   ("normal", "Pulmão normal (painel A)", EXC + "painel de referência sem alvo próprio; a comparação está nos cards de congestão e infiltrado"),
   ("congestao", "Congestão vascular e estase (painel B)", "congestao-histologia"),
   ("infiltrado", "Infiltrado de leucócitos (painel C)", "histologia-infiltrado")]),
 (31, "conteudo", "Mediadores importantes (celular)", [
   ("lt-quimio", "Leucotrienos: quimiotaxia", "ltb4"),
   ("c3a-c5a", "C3a e C5a: recrutamento e quimiotaxia", "sh-1791667098038"),
   ("il8", "IL-8: macrófagos; quimiotaxia", ["sh-1791743347807", "il8-macrofagos"]),
   ("tnf", "TNF: moléculas de adesão e efeitos sistêmicos", ["tnf-il1-endotelio", "sh-1791743347685"]),
   ("il1", "IL-1: moléculas de adesão, efeitos sistêmicos e febre", ["tnf-il1-endotelio", "sh-1791743347261"])]),
 (32, "conteudo", "Efeitos de TNF e IL-1 (figura)", [
   ("locais", "Efeitos locais no endotélio, leucócitos e fibroblastos", ["tnf-il1-endotelio", "tnf-fibroblasto"]),
   ("sistemicos", "Febre, leucocitose, proteínas de fase aguda, apetite e sono", "tnf-il1-sistemicos")]),
 (33, "conteudo", "Fagocitose e destruição (figura)", [
   ("etapas", "Reconhecimento e ligação, englobamento, fagolisossomo", ["fagocitose-etapas", "fagossomo", "manose", "sh-1791667096988"]),
   ("oxidativo", "NADPH oxidase, superóxido, MPO, HClO, iNOS e peroxinitrito", ["nadph-oxidase", "mpo", "hclo", "sh-1791743343758", "sh-1791625430632", "peroxinitrito"]),
   ("defeitos", "Doença granulomatosa crônica e Chédiak-Higashi (Robbins)", ["sh-1791743343884", "nbt", "chediak", "lyst"]),
   ("grânulos", "Enzimas e lisozima dos grânulos", "lisozima")]),
 (34, "conteudo", "Mecanismos efetores: reconhecimento", [
   ("receptores", "Receptores Toll, GPCR, de citocinas e fagocíticos", ["receptores-gpcr", "sh-1791625430208", "sh-1791743339358"]),
   ("resposta", "Mudanças do citoesqueleto, quimiotaxia, aumento de avidez, destruição de micróbios", ["quimiotaxia-def", "integrina-afinidade", "nadph-oxidase"])]),
 (35, "conteudo", "Mecanismos efetores: remoção", [("remocao", "Fagocitose e morte dos micróbios", ["fagocitose-etapas", "nadph-oxidase", "fagossomo"])]),
 (36, "conteudo", "Efeitos regulatórios", [
   ("meiavida", "Meia-vida curta de células e mediadores", ["meia-vida", "sh-1791743349036"]),
   ("aa", "Alternância na cascata do ácido araquidônico (lipoxinas)", "sh-1791743349282"),
   ("m1m2", "Macrófago M1 × M2 (IL-10, TGF-β)", ["sh-1520716108281", "sh-1791743349160"])]),
 (37, "conteudo", "Desdobramentos: destino das células", [
   ("fluido", "Líquido drenado pelos linfáticos, macrófagos limpam restos", "resolucao-passos"),
   ("apoptose", "Apoptose de neutrófilos e eferocitose", ["sh-1791743349036", "sh-1791743349458"])]),
 (38, "conteudo", "Desdobramentos: resolução, fibrose, cronificação", [
   ("resolucao", "Resolução completa", "resolucao"),
   ("fibrose", "Fibrose com perda de função", "fibrose"),
   ("cronica", "Inflamação crônica: infiltrado mononuclear, angiogênese, fibrose", ["cronificacao", "cronica-caracteristicas"]),
   ("abscesso", "Formação de pus (abscesso) e cura", "abscesso-def")]),
 (39, "conteudo", "Padrões morfológicos: úlcera", [
   ("def", "Úlcera", "ulcera-def"),
   ("macro", "Úlcera gástrica, aspecto macroscópico", "ulcera-macro"),
   ("micro", "Úlcera, aspecto microscópico", ["ulcera-micro", "ulcera-aguda"])]),
 (40, "conteudo", "Padrões morfológicos: flegmão", [
   ("def", "Flegmão", ["flegmao-def", "flegmao-cavidade"]),
   ("macro", "Flegmão, aspecto macroscópico", "flegmao-macro"),
   ("micro", "Flegmão, aspecto microscópico", "flegmao-micro")]),
 (41, "conteudo", "Padrões morfológicos: abscesso", [
   ("def", "Abscesso", ["abscesso-def", "abscesso-liquefacao"]),
   ("macro", "Abscesso pulmonar, aspecto macroscópico", "abscesso-macro"),
   ("exemplo", "Abscesso estafilocócico", "sh-1791763648295")]),
 (42, "conteudo", "Padrões morfológicos: abscesso (histologia)", [
   ("micro", "Abscesso, aspecto microscópico", ["abscesso-micro", "abscesso-estrutura"])]),
 (43, "capa", "Encerramento (personagem de desenho animado)", []),
]
JUSTIFICATIVAS = {}
CAPITULO = [("Robbins Bases Patológicas, cap. 2 (Inflamação aguda e crônica), pp. 43-69", [
   ("rb-tres", "Três componentes da inflamação aguda", "tres-componentes"),
   ("rb-estimulos", "Estímulos: infecção, necrose, corpo estranho, reações imunes", ["causas", "causas-outras"]),
   ("rb-exsudato", "Exsudato, transudato, edema e pus", ["exsudato-def", "transudato-def", "pus-def"]),
   ("rb-vasodil", "Vasodilatação arteriolar, estase", ["arteriolas", "estase"]),
   ("rb-permeab", "Mecanismos de permeabilidade, venulas, duração", ["sh-1791169090157", "contracao-rapida", "lesao-direta", "lesao-leucocitos", "transcitose", "permeabilidade-tardia"]),
   ("rb-linfa", "Linfáticos, linfangite e linfadenite", ["linfa", "linfangite", "linfadenopatia"]),
   ("rb-extravasamento", "Etapas, selectinas, integrinas, PECAM-1, quimiotaxia", FIG_EXT),
   ("rb-formil", "Peptídeos N-formilmetionina como quimioatraentes", "formil"),
   ("rb-tempo", "Neutrófilos nas primeiras 6-24 h, monócitos em 24-48 h", ["tempo-neutrofilos", "sh-1791743342606"]),
   ("rb-fagocitose", "Fagocitose, explosão oxidativa, MPO, NO", ["fagocitose-etapas", "nadph-oxidase", "mpo", "peroxinitrito", "lisozima"]),
   ("rb-defeitos", "Defeitos funcionais: LAD, CGD, Chédiak-Higashi", ["sh-1791743343209", "lad2", "sh-1791743343884", "chediak"]),
   ("rb-m1m2", "Macrófagos M1 e M2", "sh-1520716108281"),
   ("rb-celulas-residentes", "Mastócitos e macrófagos teciduais", "residentes"),
   ("rb-termino", "Término da inflamação: meia-vida, apoptose, lipoxinas, IL-10", ["meia-vida", "sh-1791743349036", "sh-1791743349282", "sh-1791743349160"]),
   ("rb-mediadores", "Histamina, PG, LT, PAF, NO, cininas, complemento", ["histamina-fonte", "sh-1791743344808", "sh-1791169336677", "paf", "no-fonte", "sh-1791169090006", "sh-1791667097913"]),
   ("rb-aa", "Ácido araquidônico, COX, LOX, anti-inflamatórios", AA),
   ("rb-citocinas", "TNF, IL-1, quimiocinas", ["tnf-il1-endotelio", "tnf-il1-sistemicos", "sh-1791743347807", "sh-1791743347261"]),
   ("rb-kinina", "Calicreína e fator XII", ["sh-1791743344308", "sh-1791743344184"]),
   ("rb-desfechos", "Resolução, fibrose, inflamação crônica", ["resolucao", "fibrose", "cronificacao"]),
   ("rb-serosa", "Inflamação serosa", "serosa"),
   ("rb-fibrinosa", "Inflamação fibrinosa", "fibrinosa"),
   ("rb-supurativa", "Inflamação supurativa e abscesso", ["abscesso-def", "abscesso-estrutura"]),
   ("rb-ulcera", "Úlcera", ["ulcera-def", "ulcera-aguda"]),
   ("rb-plaquetas", "Plaquetas e serotonina", "plaquetas"),
   ("rb-resolucao", "Resolução: macrófagos e linfáticos", "resolucao-passos")])]
EXERCICIOS = [
 ("Provas UC03 (índice pat-07-inflamacao-aguda)", [
   ("pr-2025-exsudato", "2025 P2 1.2: líquido exsudato, rico em proteína e neutrófilos, por permeabilidade", ["exsudato-def", "exsudato-proteina", "exsudato-ldh"]),
   ("pr-2025-flegmao", "2025 P2 2.2: padrão flegmonoso na fáscia", ["flegmao-def", "flegmao-cavidade"]),
   ("pr-2024-moleculas", "2024 P2 1.16: moléculas para a fase vascular e a celular (COX, corticoides, adesão)", ["sh-1791743345958", "sh-1791743346434", "adesao-integrina", "contracao-rapida"]),
   ("pr-2023-biopsia", "2023 P2 1.8: biópsia da úlcera mostra inflamação aguda com neutrófilos, congestão e edema", ["edema-neutrofilos", "congestao-histologia", "ulcera-aguda"]),
   ("pr-2023-vermelhidao", "2023 P2 2.4: vermelhidão por vasodilatação e permeabilidade", ["rubor-calor", "tres-componentes"]),
   ("pr-2019-necrose", "2019 P1 1.7: necrose como padrão principal na infecção bacteriana", "necrose-bacteria"),
   ("pr-2019-reconhecimento", "2019 P2 2.11: mecanismos de reconhecimento e resposta na inflamação aguda", ["prr", "tres-componentes"]),
   ("pr-2018-abscesso", "2018 P2 3.3: lesão bem delimitada com conteúdo liquefeito é abscesso", ["abscesso-def", "abscesso-liquefacao"]),
   ("pr-2017-edema", "2017 P1 1.7: edema pós-operatório por aumento de permeabilidade", ["tres-componentes", "exsudato-def"]),
   ("pr-2017-klebsiella", "2017 P1 3.5: necrose liquefativa e abscesso", ["necrose-bacteria", "abscesso-liquefacao"]),
   ("pr-2017-esquema", "2017 P2 1.13: vasodilatação (NO, histamina, bradicinina) e três mecanismos de permeabilidade", ["sh-1791743341507", "sh-1791169090006", "sh-1791169090157", "lesao-direta", "lesao-leucocitos"]),
   ("pr-2016-rolamento", "2016 P1 1.6: rolamento (selectina, Sialyl-Lewis) × adesão (ICAM, VCAM)", ["selectina-sialyl", "adesao-integrina", "icam-vcam"]),
   ("pr-2016-associe", "2016 P1 1.7: IL-1 febre, TNF, exsudato, C3a, iNOS, pus", ["sh-1791743347261", "sh-1791743347685", "exsudato-def", "sh-1791667097913", "no-fonte", "pus-def"]),
   ("pr-2016-sinais", "2016 P1 1.8: sinais flogísticos em caso de colecistite", SIGNS + ["dor-mecanismo", "rubor-calor"]),
   ("pr-2016-densidade", "2016 P1 2.6: densidade 1000 não condiz com exsudato", "exsudato-densidade"),
   ("pr-2015-apendice", "2015 P2sub 4.1/4.2: achados macro e microscópicos e alterações vasculares do apêndice", ["edema-neutrofilos", "tres-componentes", "lesao-direta", "contracao-rapida"])]),
 ("Monitoria P2, aula 7 (Inflamação aguda)", [
   ("mo-definicao", "Resposta inicial ao dano, cinco sinais, desencadeantes", ["def", "causas", "causas-outras"]),
   ("mo-vascular", "Vasodilatação, transudato que vira exsudato, estase", ["arteriolas", "estase", "exsudato-def", "transudato-def"]),
   ("mo-permeab", "Contração endotelial, lesão direta, lesão por leucócitos, transcitose, linfática", ["sh-1791169090157", "lesao-direta", "lesao-leucocitos", "transcitose", "linfa"]),
   ("mo-celular", "Complemento, marginação, rolamento, adesão, diapedese, quimiotaxia, ciclo de retroalimentação", FIG_EXT),
   ("mo-leucotrienos", "Leucotrienos: permeabilidade e quimiotaxia", ["sh-1791169336677", "ltb4"]),
   ("mo-efetores", "Reconhecimento, remoção e regulação; M1 para M2", ["receptores-gpcr", "fagocitose-etapas", "meia-vida", "sh-1520716108281"]),
   ("mo-desdobramentos", "Resolução, cronificação e fibrose", ["resolucao", "cronificacao", "fibrose"]),
   ("mo-padroes", "Flegmão, úlcera, abscesso", ["flegmao-def", "ulcera-def", "abscesso-liquefacao"]),
   ("mo-antiinflamatorios", "Anti-inflamatórios inibem COX ou fosfolipase", ["sh-1791743345958", "sh-1791743346434"])]),
 ("Apostila de veteranos (Guia de Patologia aula 8; UC3.pdf)", [
   ("ve-sinais", "Calor e rubor por vasodilatação, tumor por edema, dor por compressão e lesão", ["rubor-calor", "dor-mecanismo"]),
   ("ve-fibrina", "Fibrina compartimenta a inflamação", "fibrina-compartimenta"),
   ("ve-bradicinina", "Bradicinina, histamina, NO e eicosanoides", ["sh-1791169090006", "sh-1791743341507"] + AA),
   ("ve-paf", "PAF e predisposição a trombose", "paf"),
   ("ve-tlr-nlr", "TLR, NF-κB, NLR e inflamassoma NLRP3", ["sh-1791743339611", "sh-1791743339740", "nlrp3-asc", "piroptose"]),
   ("ve-diapedese", "Selectinas, ICAM-1, PECAM-1, metaloproteinases", ["selectina-sialyl", "adesao-integrina", "pecam", "colagenase"]),
   ("ve-m1m2", "Macrófagos M1 e M2", "sh-1520716108281")]),
 ("Palavras-cruzadas e gabarito (Material Complementar III e IV)", [
   ("pc-vasos", "Vênulas, arteríolas, rubor, tumor, dor, NO, iNOS", ["rubor-calor", "arteriolas", "no-fonte", "sh-1791743341507"]),
   ("pc-adesao", "VCAM, Sialyl-Lewis X, integrinas, PECAM, retração endotelial, leucócitos", ["adesao-integrina", "icam-vcam", "selectina-sialyl", "pecam", "lesao-leucocitos", "contracao-rapida"]),
   ("pc-celulas", "Neutrófilo, macrófago, eosinófilo", ["neutrofilo-celula", "eosinofilo", "residentes"]),
   ("pc-farmacos", "COX, esteroides, prostaglandinas", ["sh-1791743345958", "sh-1791743346434", "sh-1791743344808"]),
   ("pc-fluidos", "Exsudato, transudato, pus", ["exsudato-def", "transudato-def", "pus-def"]),
   ("pc-padroes", "Abscesso, cronificação, sufixo -ite, miosite, estresse oxidativo", ["abscesso-def", "cronificacao", "sufixo-ite", "nadph-oxidase"]),
   ("pc-tnf", "TNF-α e efeitos sistêmicos", "tnf-il1-sistemicos"),
   ("pc-quimiotaxia", "Quimiotaxia", "quimiotaxia-def")]),
 ("Bibliografia da aula II (Strowig et al., Inflamassomas, Nature 2012)", [
   ("bib-inflamassoma", "Inflamassomas ativam caspase-1, IL-1β e piroptose; NLRP3 e cristais", ["sh-1791743339740", "sh-1791743339860", "sh-1791743340632", "piroptose", "nlrp3-asc"])]),
]
