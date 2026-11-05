"""Inventário atômico da 65 Reparo tecidual e cicatrização de feridas v3 (UC03 P3; Patologia; Luiz Fernando Ferraz da Silva; 45 lâminas), escrito em 04/11 a partir do material lido nesta sessão:
lâminas (visual/folha-01..08), transcrição inteira, apostila guia (Aula 9), monitoria P3 (aula 11), UC3.pdf pp.447–453, provas, cruzadas e Robbins cap. 3. Ordem = ordem das lâminas.
Chaves c-* são planejadas; na E5 viram a chave do spec (au) ou ak<nid> (AnKing).
"""
PREFIXO = "pt65"
AULA = "Reparo tecidual e cicatrização de feridas (UC03 P3; Patologia)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Balanço proliferativo: regeneração × reparo (esquema de Robbins)", [("a", "Quatro destinos da lesão", "c-org-destinos")]),
 (3, "conteudo", "Células e arcabouços: lóbulo hepático com e sem lesão da matriz", [("a", "Arcabouço decide regeneração ou cicatriz", "c-arcabouco"), ("b", "Hepatite aguda × crônica", "c-hep-agudo-cronico"), ("c", "Cérebro e baço: arcabouço diferente", "c-cerebro-arcabouco")]),
 (4, "conteudo", "Atividade proliferativa: lábeis, estáveis, permanentes", [("a", "Três grupos", "c-org-tecidos"), ("b", "Regenerar × cicatrizar", "c-regenera-cicatriza")]),
 (5, "conteudo", "Células-tronco: pluripotente → comprometida", [("a", "Níveis de potência", "c-tronco-niveis")]),
 (6, "conteudo", "Células-tronco somáticas: pele, intestino, fígado, córnea", [("a", "Restrição ao tecido", "c-tronco-somatica"), ("b", "Nichos", "c-org-nichos")]),
 (7, "conteudo", "Ciclo celular: G0 e G1", [("a", "Estável em G0 sai por fator de crescimento", "c-g0")]),
 (8, "conteudo", "Tabela de fatores de crescimento", [("a", "Alvos dos fatores", "c-org-fatores"), ("b", "TGF-β", "c-tgfb"), ("c", "VEGF", "c-vegf")]),
 (9, "conteudo", "Importância prática dos fatores", [("a", "Mesmos fatores no reparo e na neoplasia", "c-fator-neoplasia"), ("b", "HER2, anti-TNF", "EXC: clínica e farmacologia (UC19 e aulas de tumores)")]),
 (10, "conteudo", "Regeneração × reparo; TNF × TGF; crescimento compensatório do fígado", [("a", "Definição de regeneração", "c-regeneracao-def"), ("b", "Fígado remanescente cresce", "c-crescimento-comp"), ("c", "Priming e progressão", "c-g0")]),
 (11, "conteudo", "Matriz extracelular: funções e componentes", [("a", "Funções", "c-mec-funcoes"), ("b", "Fibrilares × não fibrilares", "c-mec-fibrilar")]),
 (12, "conteudo", "Matriz: integrinas, citoesqueleto e núcleo", [("a", "Sinalização célula-matriz", "c-integrinas")]),
 (13, "conteudo", "Reparo e cicatrização: cinco etapas e gráfico", [("a", "Etapas e fases", "c-org-fases")]),
 (14, "conteudo", "Cicatrização: ferida fina × com cicatriz (24 h, 3–7 dias, semanas)", [("a", "Primeira × segunda intenção", "c-intencoes"), ("b", "Ponto cirúrgico", "c-ponto")]),
 (15, "conteudo", "Fases: hemostasia, inflamatória, proliferativa, maturação", [("a", "Quatro fases", "c-org-fases")]),
 (16, "conteudo", "Gráfico das três fases sobrepostas", [("a", "Tempos", "c-org-fases")]),
 (17, "conteudo", "Fases: hemostasia e inflamação juntas", [("a", "Colchete", "c-org-fases")]),
 (18, "conteudo", "Hemostasia: vasoconstrição e plug primário", [("a", "Plug primário", "c-plug")]),
 (19, "conteudo", "Hemostasia: plug secundário e fibrina", [("a", "Plug secundário", "c-plug"), ("b", "Cascata", "EXC: cascata da coagulação é da aula 69")]),
 (20, "conteudo", "Plaqueta libera mediadores: vasodilatação e permeabilidade", [("a", "Plaqueta inicia a inflamação", "c-plaqueta-mediadores")]),
 (21, "conteudo", "Fase inflamatória: neutrófilos, macrófagos, TGF-β, corticoide", [("a", "Neutrófilo primeiro", "c-neutrofilo-primeiro"), ("b", "M2 e TGF-β", "c-m2-reparo"), ("c", "Corticoide", "c-corticoide")]),
 (22, "conteudo", "Macrófago M1 × M2", [("a", "M1 × M2", "c-m1-m2")]),
 (23, "conteudo", "Citocinas: TNF, TGF-β, IL-1 destacadas", [("a", "TNF e IL-1 × TGF-β", "c-tnf-tgf")]),
 (24, "conteudo", "Células e oxigênio ao longo dos dias", [("a", "Sequência celular", "c-neutrofilo-primeiro"), ("b", "Oxigênio", "EXC: curva de oxigênio é detalhe; o professor só a comenta de passagem")]),
 (25, "conteudo", "Inflamatória (dia 3): fatores no leito", [("a", "Mediadores", "c-fibroblasto-fatores")]),
 (26, "conteudo", "Fase proliferativa: granulação e contração/reepitelização", [("a", "Tempos", "c-prolif-tempo")]),
 (27, "conteudo", "Fibroblasto, colágeno III e I; AINH e vitamina A", [("a", "Fatores do fibroblasto", "c-fibroblasto-fatores"), ("b", "Drogas que o diminuem", "c-fibroblasto-drogas"), ("c", "III × I", "c-colageno-iii-i")]),
 (28, "conteudo", "Síntese e montagem do colágeno", [("a", "Hidroxilação, tripla hélice", "c-vitc")]),
 (29, "conteudo", "Colágeno por dia: III (1–2), I (3–4, 20–21)", [("a", "III → I", "c-colageno-iii-i")]),
 (30, "conteudo", "Curvas celulares e de matriz; micrografia de fibras", [("a", "Colágeno e força tênsil no tempo", "c-colageno-iii-i")]),
 (31, "conteudo", "Angiogênese", [("a", "Hipóxia, VEGF", "c-angiogenese"), ("b", "Vasos imaturos", "c-vasos-imaturos")]),
 (32, "conteudo", "Tecido de granulação (foto da ferida)", [("a", "Leito vermelho", "c-granulacao"), ("b", "Desbridar", "c-desbridamento")]),
 (33, "conteudo", "Tecido de granulação (histologia)", [("a", "Três componentes", "c-granulacao")]),
 (34, "conteudo", "Reepitelização e neovascularização (dia 5)", [("a", "Granulação sob a reepitelização", "c-reepitelizacao")]),
 (35, "conteudo", "Reepitelização: camadas da epiderme", [("a", "Epiderme nova", "c-reepitelizacao")]),
 (36, "conteudo", "Maturação: 21 dias a 2 anos; 80% na 12ª semana", [("a", "O que ocorre", "c-maturacao"), ("b", "Força", "c-forca-tensil"), ("c", "MMP e remodelação", "c-mmp")]),
 (37, "conteudo", "Fotos da cicatrização por dia (0 a 14)", [("a", "Ilustração", "c-miofibroblasto")]),
 (38, "conteudo", "Curvas de força tênsil", [("a", "Nunca 100%", "c-forca-tensil"), ("b", "Hérnia incisional", "c-hernia-incisional")]),
 (39, "conteudo", "Úlcera do pé e histologia (segunda intenção)", [("a", "Segunda intenção", "c-intencoes")]),
 (40, "conteudo", "Ferida fina × com cicatriz e contração", [("a", "Contração", "c-miofibroblasto")]),
 (41, "conteudo", "Gráfico das fases (Robbins)", [("a", "Fases", "c-org-fases"), ("b", "Fatores que atrasam", "c-fatores-atraso"), ("c", "Infecção e deiscência", "c-segunda-infeccao"), ("d", "Imunossupressão", "c-imunossupressao"), ("e", "Glicação", "c-glicacao")]),
 (42, "conteudo", "Reparo na inflamação: papéis do macrófago", [("a", "Cinco papéis", "c-macrofago-reparo")]),
 (43, "conteudo", "Persistência do estímulo e fibrose", [("a", "Síntese ↑ e degradação ↓", "c-fibrose-mec"), ("b", "Crohn", "c-crohn")]),
 (44, "conteudo", "Destinos da lesão: regeneração, reparo, fibrose", [("a", "Três destinos", "c-org-destinos"), ("b", "Queloide", "c-queloide")]),
 (45, "capa", "Encerramento", []),
]
JUSTIFICATIVAS = {}
CAPITULO = [("Robbins, Bases Patológicas das Doenças, cap. 3", [["p", "Arcabouço, tipos de tecido e células-tronco", "c-arcabouco"], ["q", "Cura de feridas cutâneas: fases, primeira e segunda intenção, granulação", "c-intencoes"], ["r", "Aspectos patológicos: queloide, deiscência", "c-queloide"], ["s", "Fibrose e TGF-β", "c-fibrose-mec"], ["t", "Metaloproteinases e remodelação", "c-mmp"]])]
EXERCICIOS = [["Provas UC03 (índice pat-11-reparo-tecidual-cicatrizacao)", [["u", "2025 P3 4.2 fase inflamatória", "c-imunossupressao"], ["v", "2025 P3 4.3 primeira × segunda intenção", "c-intencoes"], ["w", "2016 P2 2.4 tecido de granulação", "c-granulacao"], ["x", "2015 P2sub 3.1 ponto", "c-ponto"]]], ["Monitoria P3, aula 11 (reparo)", [["y", "Regeneração × reparo e arcabouço", "c-arcabouco"]]], ["Apostila guia de Patologia, aula 9", [["z", "Tip e stalk cells; Notch", "EXC: só na apostila; entra se houver card de acervo"]]], ["Palavras-cruzadas da aula", [["aa", "Macrófago, queloide, miofibroblasto, MMP, hérnia incisional", "c-queloide"]]]]
