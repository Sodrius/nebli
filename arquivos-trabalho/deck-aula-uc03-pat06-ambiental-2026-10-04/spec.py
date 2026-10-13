# Especificação curada — Patologia ambiental (UC03 P2, Patologia, aula 24; Prof. Luiz Fernando Ferraz da Silva; lâminas 17–51).
# Reconstrução pelo Claude em 09/10/2026 (F-20261009-CLAUDE-02: "aula de pato também acho que algumas coisas fugiram"). A versão
# Codex (spec-codex-antes-reconstrucao.py) tinha 9 cards de CO, pneumoconiose do carvão em dobro, histologia de macrófago e lesão
# por fumaça, todos com o Extra genérico "Connect the fact to inhaled pollutants…", e não contava a história da aula.
# Base: lâminas 17–51 (vistas), apostila de veteranos aula 7 (fontes/veteranos-patologia-integral.txt pp. 33–34), Robbins cap. 9
# (poluição do ar e CO), provas P2 2024 (1.18: inflamação sistêmica, disfunção endotelial, defesas pulmonares, muco) e 2025 (4.3:
# biomassa → disfunção mucociliar, macrófagos hipoativos → pneumonia). AnKing quase não tem poluição atmosférica (busca 09/10).
# Deck sem revisão e todo suspenso (pós-P2): novos entram suspensos.
RUN_ID = 'uc03-pat06-20261009a'; SHORT = 'pat06'; LESSON = '2026-uc03-patologia-24-patologia-ambiental'
DECK = 'NEBLI::UC03::P2::Patologia::Patologia ambiental'
CRITERIOS = 'MEMORY.md + FEEDBACKS (até F-20261009-CLAUDE-03), 09/10/2026'
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = "AnKing Step e Referências Externas, 09/10 ('anthracosis', 'ozone', 'particulate matter', 'air pollution', 'biomass', 'smog', 'thermal inversion', 'pollution atherosclerosis'): "


def ak(key, src, flags, b, alvo, s, m, nota='', **kw):
    d = dict(key=key, kind='text', src=src, manter=True, flags=flags, bloco=b, alvo=alvo, evid=f'Slide {s}', motivo=m,
             sem_imagem='mecanismo ou relação; a figura da lâmina não acrescenta recuperação', **kw)
    if nota: d['extra_add'] = f'- {nota}'
    return d


def au(key, text, flags, b, alvo, s, autoria, falta, esp, m, extra):
    return dict(key=key, kind='autoral', text=text, extra=extra, flags=flags, bloco=b, alvo=alvo, evid=f'Slide {s}', autoria=autoria,
                busca=BUSCA + falta, espelhos=esp, motivo=m, sem_imagem='definição ou relação causal; figura não melhora a recuperação')


A, B, C, D, E = 'A-historia-e-contexto', 'B-poluentes', 'C-particulado', 'D-poluicao-e-saude', 'E-biomassa-e-mecanismos'
G = [1473638455081, 1473289461901]
CARDS = [
 # ---------- A. História e contexto (17–34) ----------
 au('revolucao-industrial', 'Air pollution rose sharply with the fossil-fuel combustion of the {{c1::Industrial Revolution}}', {1: R}, A,
    'História da poluição', 19, 'lateral', 'sem card.', G, 'Rosa: lâminas 18–19 e apostila (do fogo à indústria).',
    '- Fire was used for heat, light and cooking long before'),
 au('grande-nevoeiro', 'The 1952 London {{c1::Great Smog}} killed about 4,000 people in one week', {1: Z}, A,
    'Grande Nevoeiro de 1952', 20, 'central', "'smog' sem card.", G, 'Azul: lâminas 20–21 e apostila.',
    '- Deaths rose to over 8,000 within weeks'),
 au('inversao-termica', 'A thermal inversion traps pollutants near the {{c1::ground}}', {1: V}, A, 'Inversão térmica', 20, 'central',
    "'thermal inversion' sem card.", G, 'Verde: mecanismo do Grande Nevoeiro (apostila).',
    '- A warm air layer above cooler surface air blocks vertical dispersion'),
 au('iceberg', 'The largest hidden burden of air pollution is {{c1::subclinical inflammation}}', {1: V}, A, 'Pirâmide dos efeitos', 22, 'central',
    'sem card.', G, 'Verde: pirâmide da lâmina 22 (mortes no topo; inflamação subclínica na base).',
    '- From top to bottom: deaths, admissions, medical visits, medication use, subclinical inflammation<br>- Severity falls as the number affected rises'),
 # ---------- A2. Mudanças climáticas (lâminas 23–28; aula II, Profa. Thais Mauad, 20 lâminas) ----------
 au('gee', 'Most greenhouse-gas warming comes from {{c1::carbon dioxide}} and methane released mainly by burning fossil fuels', {1: V}, A,
    'Gases de efeito estufa', '23; Ambiental II 2', 'central', "'greenhouse' só traz anestésicos.", G, 'Verde: definição da aula II (CO2 e metano > 90% do impacto).',
    '- Agriculture and deforestation also add to them'),
 au('ondas-calor', 'Heat waves raise overall {{c1::mortality}}, as in France in 2003 with over 70,000 excess deaths', {1: R}, A,
    'Calor extremo', '24; Ambiental II 7', 'lateral', "'heatwave' só traz insolação.", G, 'Rosa: exemplo da aula II.',
    '- Also dehydration and chronic kidney disease in cane cutters; elderly, children and outdoor workers are most vulnerable'),
 au('vetores', 'Warmer, wetter weather spreads {{c1::vector}}-borne diseases such as dengue, zika and chikungunya', {1: Z}, A,
    'Doenças por vetores', '25; Ambiental II 9', 'central', 'sem card de clima e vetores.', [1506627695686, 1522430399029], 'Azul: agentes infecciosos da aula II.',
    '- Floods spread waterborne disease (leptospirosis, cholera); warmer, drier soil favors fungi'),
 ak('dengue-aedes', 1506627695686, {1: V}, A, 'Dengue transmitida pelo Aedes', 25, 'Verde: HY 1; exemplo de vetor da aula II.', nota='Climate change widens the range of Aedes mosquitoes'),
 au('ozonio-asma', 'Ozone irritates the airway mucosa, worsening {{c1::asthma}} and lowering lung function in children', {1: Z}, A,
    'Ozônio e saúde', '26; Ambiental II 13', 'central', "'ozone' sem card.", G, 'Azul: aula II (ozônio cresce com a temperatura).',
    '- Warming raises ozone levels and ozone-related deaths'),
 au('polen', 'Warming lengthens the {{c1::pollen}} season and makes pollen more allergenic, raising asthma admissions', {1: Z}, A,
    'Alergias e asma', '27; Ambiental II 14', 'central', "'pollen' só em rinite alérgica.", [1473536756997, 1473638455081], 'Azul: aula II.',
    '- Pollen and ozone act together'),
 au('enchentes-fungos', 'After floods, indoor {{c1::mold}} growth causes allergic respiratory disease', {1: R}, A,
    'Enchentes e fungos', '28; Ambiental II 17', 'lateral', 'sem card.', G, 'Rosa: exemplo pós-Katrina da aula II.',
    '- Sudden temperature swings also favor respiratory infections'),
 au('oms-pm25', 'São Paulo’s yearly PM2.5 (about 28 µg/m³) is roughly {{c1::three}} times the WHO guideline shown in the lesson (10 µg/m³)', {1: R}, A,
    'Megacidades: PM2.5 em São Paulo × OMS', 34, 'lateral', 'sem card.', G, 'Rosa: números da lâmina 34.',
    '- Most of the population now lives in cities, where traffic dominates emissions'),
 # ---------- B. Poluentes (35) ----------
 au('fontes-poluentes', 'Vehicles and industry mainly emit sulfur, nitrogen and carbon oxides, metals and {{c1::particulate matter}}', {1: V}, B,
    'Fontes e principais poluentes', 35, 'central', 'sem card.', G, 'Verde: esquema da lâmina 35 e apostila.',
    '- Biomass burning adds carbon monoxide, particles and polycyclic aromatic hydrocarbons'),
 au('veiculos-sp', 'In São Paulo, the main source of air pollutants is {{c1::vehicles}}', {1: Z}, B,
    'Veículos como principal fonte em SP', '35; palavras-cruzadas', 'central', 'sem card.', G, 'Azul: pista das palavras-cruzadas da aula e lâmina 35.',
    '- Heavy diesel vehicles emit most particulate matter'),
 au('primario', 'A pollutant emitted directly from a source is {{c1::primary}}', {1: V}, B, 'Poluente primário', 35, 'central', 'sem card.', G,
    'Verde: organiza a lâmina 35.', '- SO₂, NOx, CO and particles from exhaust and chimneys'),
 au('secundario', 'Ground-level ozone is a {{c1::secondary}} pollutant', {1: V}, B, 'Poluente secundário', 35, 'central', "'ozone' sem card.", G,
    'Verde: conceito da lâmina 35.', '- It forms in the air from precursors (NOx, hydrocarbons) under sunlight; sulfuric acid and sulfates are other examples'),
 ak('cohb', 1473385249608, {1: V, 2: Z}, B, 'Carboxiemoglobina', 35, 'Verde e azul: CO entre os poluentes da lâmina 35 e Robbins cap. 9.',
    nota='CO comes from incomplete combustion (vehicles, biomass)'),
 ak('co-affinity', 1473385253436, {1: V}, B, 'Afinidade do CO pela hemoglobina', 35, 'Verde: HY 2; por que pouco CO já causa hipóxia (Robbins).', nota='So even low CO concentrations cause tissue hypoxia'),
 # ---------- C. Material particulado (36–39) ----------
 au('mp-nucleo', 'Particulate matter has an inert {{c1::carbon}} core coated with toxic nitrates, sulfates, metals and PAHs', {1: V}, C,
    'Composição do material particulado', 36, 'central', "'particulate matter' só em Histology.", G, 'Verde: lâmina 36 e apostila.',
    '- Natural sources: soil, ocean, volcanoes, forests; human sources: traffic, industry, incomplete combustion'),
 au('pm-diametro', 'Particulate matter is classified by its aerodynamic {{c1::diameter}}, which decides where it deposits', {1: V}, C,
    'Classificação pelo diâmetro aerodinâmico', 36, 'central', 'sem card.', G, 'Verde: classificação da lâmina 36.',
    '- PM10 and PM2.5 are upper size limits, not different substances'),
 au('pm-deposicao', 'Fine particles ({{c1::PM2.5}}) reach the alveoli, while ultrafine particles can cross into the blood', {1: V}, C,
    'PM10, PM2.5 e ultrafinas', 37, 'central', 'sem card.', G, 'Verde: lâmina 37 (Saldiva) e prova 2024.',
    '- PM10 deposits mainly in the upper airways'),
 au('arvores', 'Trees {{c1::retain}} particulate matter, so pollution is lower inside wooded parks', {1: R}, C,
    'Árvores retêm partículas', '37; apostila veteranos aula 7; palavras-cruzadas', 'lateral', 'sem card.', G, 'Rosa: apostila e palavras-cruzadas.',
    '- Green areas also soften heat islands'),
 ak('antracose', 1473638455081, {1: V}, C, 'Antracose: macrófagos com carbono', 37, 'Verde: macrófagos não digerem o núcleo de carbono (apostila).',
    nota='The carbon core cannot be digested, so macrophages store it'),
 ak('alveolar-macrophage', 1473289622374, {1: V}, C, 'Macrófago alveolar remove partículas', 37, 'Verde: HY 2; defesa alveolar da prova 2024.'),
 ak('cilia-clearance', 1473289461901, {1: V, 2: Z}, C, 'Depuração mucociliar', 38, 'Verde: defesa que a poluição altera (lâmina 50, provas).', nota='Pollution and biomass smoke impair this clearance'),
 # ---------- D. Poluição e saúde (40–46) ----------
 au('pm-mortalidade', 'Long-term exposure to fine particulate matter (PM2.5) increases {{c1::cardiopulmonary}} mortality', {1: V}, D,
    'PM2.5 e mortalidade', 40, 'central', 'sem card.', G, 'Verde: Pope et al. 2000 na lâmina 40.',
    '- The association holds even below regulatory standards'),
 au('expectativa-vida', 'Cities with more PM2.5 have a lower {{c1::life expectancy}}', {1: Z}, D, 'PM2.5 e expectativa de vida', 41, 'central', 'sem card.', G,
    'Azul: lâmina 41 e apostila.', '- Higher pollution also means more hospital admissions and costs'),
 au('lumen-parede', 'In exposed animals, polluted air reduces the lumen-to-wall ratio of {{c1::coronary}} and pulmonary arterioles', {1: Z}, D,
    'Remodelamento vascular coronariano e pulmonar', 42, 'central', 'sem card.', G, 'Azul: lâmina 42 e apostila.',
    '- Filtered air protects the lumen'),
 au('ldl-placa', 'Air pollution enhances {{c1::LDL oxidation}} and thickens atherosclerotic plaques without raising their lipid content', {1: V}, D,
    'Poluição e aterosclerose', 44, 'central', "'pollution atherosclerosis' sem card.", [1471811979298, 1473638455081],
    'Verde: lâmina 44 e apostila.', '- It also raises autoantibodies against oxidized LDL (anti-LDLox)'),
 ak('oxidized-ldl', 1471811979298, {1: V, 2: R, 3: R}, D, 'LDL oxidada captada por macrófagos', 44, 'Verde c1 (HY 1): mecanismo da placa da lâmina 44; rosas: detalhes do receptor.', nota='Pollution enhances this oxidation'),
 au('inflamacao-sistemica', 'Inhaled fine particles raise systemic {{c1::IL-6}} and TNF-α, promoting atherosclerosis and plaque rupture', {1: V}, D,
    'Inflamação sistêmica e infarto', 45, 'prova', 'sem card.', [1471811979298, 1474340552038], 'Verde: prova 2024 (1.18).',
    '- This links a polluted day to myocardial infarction'),
 au('disfuncao-endotelial', 'Air pollutants cause endothelial dysfunction with less {{c1::nitric oxide}}, favoring vasoconstriction and thrombosis', {1: V}, D,
    'Disfunção endotelial', 46, 'prova', 'sem card.', [1474340552038, 1471811979298], 'Verde: prova 2024 (1.18) e lâminas 45–46.',
    '- Less coronary flow raises the risk of ischemic events'),
 ak('endothelial-no', 1474340552038, {1: V, 2: Z}, D, 'Endotélio produz PGI2 e NO', 46, 'Verde c1 (HY 2): o que a disfunção endotelial tira.'),
 # ---------- E. Biomassa e mecanismos (47–50) ----------
 au('biomassa-tabaco', 'Indoor biomass smoke from cooking or heating harms health about as much as {{c1::tobacco}} smoke', {1: V}, E,
    'Biomassa indoor', 47, 'central', "'biomass', 'wood smoke' sem card.", G, 'Verde: lâminas 47–49 e apostila.',
    '- Countries that rely on biomass have more admissions for asthma and hypertension'),
 au('biomassa-rural', 'Living in the {{c1::countryside}} does not protect from pollution when homes burn wood or biomass', {1: R}, E,
    'Poluição também é rural', 48, 'lateral', 'sem card.', G, 'Rosa: apostila (macrófagos com carbono em crianças da Etiópia).',
    '- Airway macrophages of exposed rural children carry carbon'),
 au('irritacao', 'Gases and particles irritate the eyes and nose, causing tearing, itching and {{c1::coryza}}', {1: R}, E,
    'Irritação química', 50, 'lateral', 'sem card.', G, 'Rosa: ramo da irritação na lâmina 50.', '- Also changes the mucus and increases expectoration'),
 au('estresse-oxidativo', 'Particles trigger {{c1::oxidative}} reactions in the airways and release of IL-6 and IL-8, recruiting granulocytes', {1: Z}, E,
    'Reações oxidativas e citocinas', 50, 'central', 'sem card.', G, 'Azul: ramo do PM na lâmina 50.',
    '- Antioxidants in the lining fluid are consumed'),
 au('biomassa-pneumonia', 'Biomass smoke impairs mucociliary clearance and alveolar macrophages, predisposing to bacterial {{c1::pneumonia}}', {1: V}, E,
    'Biomassa e infecção respiratória', 50, 'prova', 'sem card.', [1473548355407, 1473289461901], 'Verde: prova 2025 (4.3) e lâmina 50.',
    '- Dry air and damaged epithelium add to the risk'),
 ak('pneumonia-defense', 1473548355407, {1: V}, E, 'Defesas prejudicadas favorecem pneumonia', 50, 'Verde: HY 1; base geral do card anterior.'),
 au('dpoc', 'Chronic exposure to biomass smoke causes chronic airway inflammation that lowers lung function and leads to {{c1::COPD}}', {1: V}, E,
    'Inflamação crônica e DPOC', 50, 'central', "'biomass COPD' sem card.", G, 'Verde: lâmina 50 e apostila (queda da função pulmonar).',
    '- Wheezing is a common symptom'),
 au('barreira-sistemica', 'Fine particles cross the airway {{c1::epithelial barrier}} and cause systemic effects', {1: V}, E,
    'Transposição da barreira e efeitos sistêmicos', 50, 'central', 'sem card.', G, 'Verde: ramo final da lâmina 50.',
    '- Ultrafine particles reach the blood and distant organs'),
]
EXCLUIDOS = [(1473385257949, 'curva de dissociação no CO: fisiologia de CO além da aula'), (1473385273967, 'liberação de O2 no CO: idem'),
             (1473385280374, 'capacidade de O2 no CO: idem'), (1473385287565, 'PaO2 no CO: idem'), (1474253531615, 'CO e complexo IV: idem'),
             (1473466860013, 'CO reduz CaO2: idem'), (1503840888417, 'vinheta de cefaleia por CO: clínica fora da aula'),
             (1473638444755, 'pneumoconiose do carvão: ocupacional, outra aula'), (1524150216368, 'lesão por inalação de fumaça: não dada'),
             (1471811989477, 'célula espumosa: aterosclerose geral, aula de vasos'), (1471811997810, 'remodelamento da placa: idem'),
             (1703597789293, 'macrófago alveolar (Histology): repete alveolar-macrophage'), (1703596428399, 'idem'),
             (1701206425104, 'fagocitose em geral: imunologia'), (1555791674668, 'movimento ciliar: repete cilia-clearance'),
             (1703592029357, 'cílios bronquiolares: histologia'), (1556143323229, 'muco prende partículas: repete cilia-clearance'),
             (1487292580228, 'cor cereja no CO: sinal clínico do Robbins, a aula não aprofunda'), (1473548369834, 'pneumonia viral e escada mucociliar: o exemplo da aula é a biomassa')]
FORA_DO_RECORTE = ['epigenética (palavras-cruzadas de 2016 juntavam outra aula)', 'COVID-19 (lâmina 51, só título)',
                   'tratamento da intoxicação por CO', 'pneumoconioses ocupacionais']

for c in CARDS:
    if c['key'] == 'disfuncao-endotelial':
        c['duplicacao_ok'] = 'ganho: o efeito da poluição sobre o endotélio (prova 2024); o AnKing cobra a função normal'
