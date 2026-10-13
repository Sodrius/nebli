# Especificação curada — Morfologia e estrutura das bactérias (UC03 P2, Microbiologia, aula 1; Profa. Elisabete Vicente; 45 lâminas).
# Reconstrução pelo Claude em 09/10/2026 (F-20261009-CLAUDE-02: "aulas de microbio: tá faltando coisa que foi dada"). A versão Codex
# (spec-codex-antes-reconstrucao.py) usou só o PDF I, pôs um Extra genérico em todos os cards e trocou o texto de notas AnKing.
# Base: lâminas I (45) + extras do PDF II (49: Chlamydia/Mycoplasma por Giemsa, respostas da lista de questões), apostila de
# veteranos aula 1, monitoria P1 aula 1, Trabulsi cap. 2, provas UC03 (2017, 2021–2024). Ordem = lâminas. AnKing primeiro (a seção
# Basic Bacteriology cobre quase tudo); autoral curto só onde o acervo não tem; detalhe pequeno em rosa.
# Notas com revisão preservadas pela chave: lta, flagellar-basal, capsule-phago (texto desta última é adaptação da versão Codex).
RUN_ID = 'uc03-micro01-20261009a'; SHORT = 'micro01'; LESSON = '2026-uc03-microbiologia-26-morfologia-estrutura-bacteriana'
DECK = 'NEBLI::UC03::P2::Microbiologia::Morfologia e estrutura das bactérias'
CRITERIOS = 'MEMORY.md + FEEDBACKS (até F-20261009-CLAUDE-02) + PLANO-AJUSTES-ANKI-2026-10-08, 09/10/2026'
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step (seção FirstAid Basic Bacteriology, NinjaNerd Bacteria Structure) e Referências Externas, 09/10 "
         "(busca/anking-0910-a.txt e -b.txt): ")


def ak(key, src, flags, b, alvo, s, m, nota="", origin=None, **kw):
    d = dict(key=key, kind='text', src=src, manter=True, flags=flags, bloco=b, alvo=alvo, evid=f'Slide {s}', motivo=m,
             sem_imagem='bacteriologia geral: a figura da lâmina não acrescenta recuperação', **kw)
    if nota: d['extra_add'] = f'- {nota}'
    if origin: d['origin'] = origin
    return d


def au(key, text, flags, b, alvo, s, autoria, falta, esp, m, extra='', dup=''):
    return dict(key=key, kind='autoral', text=text, extra=extra, flags=flags, bloco=b, alvo=alvo, evid=f'Slide {s}', autoria=autoria,
                busca=BUSCA + falta, espelhos=esp, motivo=m, duplicacao_ok=dup,
                sem_imagem='conceito de bacteriologia geral; figura não melhora a recuperação')


A, B, C, D, E, F = ('A-introducao', 'B-morfologia', 'C-membrana', 'D-parede-e-gram', 'E-coloracoes-especiais', 'F-demais-estruturas')
G = [1500401358701, 1500401344665]  # espelhos: procariotos/eucariotos (AnKing básico)
CARDS = [
 # ---------- A. Introdução (lâminas 3–6) ----------
 au('tres-dominios', 'Woese defined the three domains of life (Bacteria, Archaea, Eukarya) by comparing {{c1::<b>ribosomal RNA</b>}} sequences', {1: V}, A,
    'Três domínios por sequência de rRNA', '3–4; apostila veteranos aula 1; monitoria P1', 'central', "'16S rRNA', 'Woese' sem card.", G,
    'Verde: abertura da aula (lâminas 3–4) e da apostila.', extra='- Bacteria appeared about 3.8 billion years ago; eukaryotes only after oxygen rose'),
 au('arqueias', '{{c1::<b>Archaea</b>}} are prokaryotes distinct from bacteria that often live in extreme environments', {1: Z}, A,
    'Arqueias', '4; apostila veteranos aula 1; monitoria P1', 'central', "'archaea' sem card próprio.", G,
    'Azul: domínio Archaea na árvore da lâmina 4 e na apostila.', extra='- Extreme habitats are common, not a rule<br>- Some produce methane'),
 au('microbiota', 'Most bacteria that live with us are {{c1::<b>commensal</b>}} or mutualistic, and only a small minority cause disease', {1: Z}, A,
    'Bactérias do bem e ruins', '5; monitoria P1', 'central', "'normal flora' só por espécie.", [1491774985388, 1500498491769],
    "Azul: 'bactérias do bem e bactérias ruins' (lâmina 5).", extra='- Mutualists make vitamins and train the immune response'),
 au('gram-conduta', 'A {{c1::<b>Gram stain</b>}} of the specimen can guide the first antibiotic choice while culture is pending', {1: V}, A,
    'Morfologia e Gram guiam a conduta inicial', '6; prova UC03 P2 1.5', 'prova', "'Gram stain empiric*' só traz condutas de casos.", [1500401546879, 1500401620724],
    'Verde: lâmina 6 (morfologia é a primeira etapa) e prova (bacterioscopia orienta a antibioticoterapia inicial).',
    extra='- Then biochemical tests, antibiogram, serology, PCR or sequencing'),
 # ---------- B. Morfologia macro e microscópica (lâminas 7–10) ----------
 au('colonia', 'A visible bacterial colony usually arises from one {{c1::<b>cell</b>}}', {1: V}, B,
    'Colônia como clone', '7–8', 'central', "'colony' sem card.", [1500405795435, 1500401924808],
    'Verde: morfologia macroscópica (lâminas 7–8).', extra='- One colony holds about 10<sup>8</sup> cells'),
 au('meio-diferencial', '{{c1::<b>Differential</b>}} solid media show colonies of different colors (e.g., lactose fermenters) or hemolysis patterns', {1: R}, B,
    'Meios diferenciais', '8', 'lateral', 'sem card de meio diferencial.', [1500415766286, 1500401546879], 'Rosa: lâmina 8.'),
 au('tamanho', 'Most bacteria measure {{c1::<b>1–5 µm</b>}}, so they are seen with the light microscope at about 1000× under oil immersion', {1: Z}, B,
    'Tamanho e microscópio óptico', '9; Trabulsi 2; prova 2017 P2 2.5', 'prova', "'oil immersion', 'light microscope' sem card.", [1500415526630, 1500401358701],
    'Azul: lâmina 9 e tabela bactéria × fungo da prova.', extra='- Cocci about 1 µm; bacilli about 2–3 × 1 µm; fungi 3–40 µm'),
 au('virus-me', 'Viruses (about 20–200 nm) can only be seen with the {{c1::<b>electron</b>}} microscope', {1: Z}, B,
    'Vírus só ao ME', '9; monitoria P1', 'central', "'electron microscop* virus*' só traz achados de doenças.", [1500415526630, 1500401358701],
    'Azul: comparação de tamanhos da lâmina 9.'),
 ak('formas', 1500415526630, {1: Z, 2: Z, 3: Z}, B, 'Formas: cocos, bacilos, cocobacilos', 10, 'Azuis: formas da lâmina 10 (HY 5).',
    nota='Plus spiral forms: vibrios, spirilla and spirochetes'),
 ak('diplococos', 1500415717345, {1: V}, B, 'Diplococos', 10, 'Verde: HY 1; arranjo da apostila.'),
 ak('estreptococos', 1500415766286, {1: V}, B, 'Estreptococos em cadeia', 10, 'Verde: HY 1; arranjo da lâmina 10.'),
 ak('estafilococos', 1500415783303, {1: V}, B, 'Estafilococos em cacho', 10, 'Verde: HY 1; arranjo da lâmina 10.'),
 au('estreptobacilos', 'Bacilli that stay in chains after division are called {{c1::<b>streptobacilli</b>}}', {1: R}, B,
    'Estreptobacilos', '10; Trabulsi 2', 'lateral', "'streptobacill*' sem card.", [1500415766286, 1500415526630], 'Rosa: rótulo da lâmina 10.'),
 ak('vibriao', 1500416644544, {1: V}, B, 'Vibrião em vírgula', 10, 'Verde: HY 1; Vibrio cholerae na lâmina 10.'),
 au('espiroqueta', 'Spiral bacteria with a {{c1::<b>flexible</b>}} body are spirochetes, whereas rigid spirals are spirilla', {1: Z}, B,
    'Espiroquetas × espirilos', '10; apostila veteranos aula 1; Trabulsi 2', 'central', "'spirochete*' só traz doenças.", [1500416644544, 1500415526630],
    'Azul: espiroquetas flexíveis × espirilos rígidos (lâmina 10).', extra='- Spirochetes: <i>Treponema</i>, <i>Leptospira</i>, <i>Borrelia</i><br>- Spirilla move with polar flagella'),
 # ---------- C. Estruturas; membrana citoplasmática (lâminas 11–13) ----------
 au('essenciais', 'Plasmids, flagella, pili, capsule and spores are {{c1::<b>non-essential</b>}} bacterial structures, present only in some bacteria', {1: Z}, C,
    'Estruturas essenciais × não essenciais', '11; monitoria P1; Trabulsi 2; questão 13', 'central', 'sem card de estrutura essencial.', G,
    'Azul: divisão da lâmina 11; questão 13 da lista.', extra='- Essential: cytoplasmic membrane, ribosomes, nucleoid'),
 au('membrana-sem-esterol', 'Unlike eukaryotic membranes, the bacterial cytoplasmic membrane has no {{c1::<b>sterols</b>}}', {1: V}, C,
    'Membrana sem esteróis', '12; apostila veteranos aula 1; Trabulsi 2', 'central', "'cell membrane bacteria sterol*' só traz a exceção do Mycoplasma.",
    [1500402206974, 1516130459979], 'Verde: diferença química central (apostila e Trabulsi).', extra='- Exception: <i>Mycoplasma</i>, which has no wall'),
 au('membrana-composicao', 'The bacterial cytoplasmic membrane is about 60% {{c1::<b>protein</b>}} and 40% phospholipid', {1: R}, C,
    'Composição 60/40', '12; monitoria P1', 'lateral', 'sem card de composição.', G, 'Rosa: número da lâmina 12.'),
 ak('cadeia-respiratoria', 1500403037776, {1: V}, C, 'Transporte de elétrons na membrana', 13, 'Verde: produção de energia na membrana (lâmina 13, apostila).',
    nota='Bacteria have no mitochondria: the membrane does their job'),
 au('translocacao-grupo', 'In {{c1::<b>group translocation</b>}}, a sugar is phosphorylated as it crosses the bacterial membrane', {1: Z}, C,
    'Transporte: translocação de grupo', '13; Trabulsi 2', 'central', "'group translocation' sem card.", [1500403037776, 1500401358701],
    'Azul: tipos de transporte da lâmina 13.', extra='- Also facilitated diffusion (no energy) and active transport (ATP)'),
 au('membrana-sintese', 'The bacterial membrane builds wall polymers (peptidoglycan, LPS) and secretes {{c1::<b>hydrolytic</b>}} enzymes', {1: R}, C,
    'Biossíntese e secreção na membrana', '13; apostila veteranos aula 1', 'lateral', 'sem card.', [1500403037776, 1500401924808],
    'Rosa: funções 3 e 4 da lâmina 13.', extra='- Some DNA replication proteins also sit in the membrane'),
 au('taxia', 'Bacterial movement toward a chemical signal is called {{c1::<b>chemotaxis</b>}}', {1: R}, C,
    'Taxia', '13 e 36; monitoria P1; Trabulsi 2', 'lateral', "'chemotaxis bacteria' só traz leucócitos.", [1500405949770, 1500403037776], 'Rosa: função 5 da lâmina 13.', extra='- Toward light: phototaxis'),
 # ---------- D. Parede celular e Gram (lâminas 14–27) ----------
 ak('gram-parede', 1500401620724, {1: V}, D, 'Gram distingue pela parede', 14, 'Verde: questão 2 da lista (estrutura que separa os dois grupos).',
    nota='Christian Gram described the stain in 1884'),
 au('gram-alcool', 'In the Gram stain, {{c1::<b>alcohol</b>}} washes the crystal violet–iodine complex out of Gram-negatives, which then take the red counterstain', {1: V}, D,
    'Etapas do Gram', '15–16; apostila veteranos aula 1; Trabulsi 2', 'central', "'decoloriz*', 'safranin' sem as etapas.", [1500417256509, 1500401591194],
    'Verde: técnica de Gram da apostila e do Trabulsi.', extra='- Order: crystal violet, iodine (lugol), alcohol, fuchsin or safranin'),
 ak('gram-cristal', 1500417256509, {1: V}, D, 'Peptidoglicano espesso retém cristal violeta', 16, 'Verde: por que o Gram-positivo fica roxo.'),
 ak('gram-purple', 1500401546879, {1: V}, D, 'Gram-positivo roxo', 16, 'Verde: leitura do Gram.'),
 ak('gram-pink', 1500401591194, {1: V}, D, 'Gram-negativo rosa', 16, 'Verde: leitura do Gram.'),
 au('parede-osmotica', 'The cell wall keeps bacteria from bursting under their high internal {{c1::<b>osmotic</b>}} pressure', {1: V}, D,
    'Funções da parede', '17; apostila veteranos aula 1; Trabulsi 2', 'central', "'osmotic cell wall' só traz β-lactâmicos.", [1514435402463, 1500401924808],
    'Verde: funções da lâmina 17.', extra='- It also gives the cell its shape and helps form the septum in division'),
 au('pg-percentual', 'Peptidoglycan makes up 15–60% of a Gram-positive cell, but only about {{c1::<b>5%</b>}} of a Gram-negative one', {1: R}, D,
    'Percentual de peptidoglicano', '17 e 21; apostila veteranos aula 1', 'lateral', 'sem card.', [1500401721497, 1500401818042], 'Rosa: números da lâmina 17.'),
 ak('pg-nagnam', 1500401924808, {1: V, 2: V}, D, 'Peptidoglicano NAG e NAM', 18, 'Verdes: estrutura do peptidoglicano (lâmina 18).'),
 ak('pg-peptideo', 1500402112697, {1: Z, 2: Z}, D, 'Peptídeos ligam-se ao NAM', 18, 'Azuis: tetrapeptídeos do Trabulsi e lâmina 18.'),
 ak('dala', 1489333776291, {1: V}, D, 'D-Ala-D-Ala no peptidoglicano', 18, 'Verde: HY 2; último aminoácido do tetrapeptídeo (Trabulsi).'),
 ak('penicilina-divisao', 1514435402463, {1: Z}, D, 'Penicilina mata quando a bactéria cresce', 18, "Azul: apostila ('as células-filhas morrem ao se dividir').",
    nota='The veteran guide: penicillin acts on wall assembly, so it works best on Gram-positives'),
 ak('gp-thick', 1500401721497, {1: V}, D, 'Parede Gram-positiva espessa', 19, 'Verde: comparação estrutural.'),
 ak('lta-gram', 1500401762436, {1: V, 2: V}, D, 'Ácidos (lipo)teicoicos só em Gram-positivos', 20, 'Verdes: questão 6 da lista.'),
 ak('lta', 1500403192082, {1: Z}, D, 'Ácido lipoteicoico estimula a resposta imune', 21, 'Azul: nota com revisão preservada.',
    nota='Teichoic acids are also cell antigens used for serologic identification'),
 au('teicoico-autolisina', 'Teichoic acids regulate {{c1::<b>autolysins</b>}}, letting the wall be remodeled during division without lysis', {1: Z}, D,
    'Ácidos teicoicos regulam autolisinas', '21; apostila veteranos aula 1; Trabulsi 2', 'central', "'teichoic' só traz LTA e imunidade.", [1500401762436, 1500403192082],
    'Azul: propriedade da lâmina 21.'),
 au('teicoico-funcoes', 'Teichoic acids also bind {{c1::<b>cations</b>}}, act as host adhesins and serve as phage receptors', {1: R}, D,
    'Outras funções dos ácidos teicoicos', '21; apostila veteranos aula 1', 'lateral', "'teichoic' sem essas funções.", [1500401762436, 1500403192082],
    'Rosa: demais propriedades da lâmina 21.', extra='- Their phosphate groups carry negative charge'),
 ak('gn-outer', 1500401818042, {1: V, 2: V}, D, 'Gram-negativo: periplasma e membrana externa', 22, 'Verdes: questão 4 da lista.'),
 ak('periplasma', 1500403322662, {1: V, 2: V}, D, 'Periplasma entre as membranas', 23, 'Verdes: questão 7 da lista.'),
 ak('periplasma-enzimas', 1500403421264, {1: Z}, D, 'Enzimas do periplasma inativam antibióticos', 23, 'Azul: β-lactamase periplasmática (apostila, Trabulsi).'),
 au('porinas', '{{c1::<b>Porins</b>}} let small hydrophilic molecules cross the Gram-negative outer membrane', {1: V}, D,
    'Porinas', '23–24; apostila veteranos aula 1; monitoria P1; Trabulsi 2', 'central', "'porin*' só traz farmacologia.", [1500401818042, 1500403683098],
    'Verde: seletividade da membrana externa (apostila e monitoria).', extra='- Passage depends on molecule size, not on specificity'),
 au('membrana-externa-barreira', "The Gram-negative outer membrane keeps out lysozyme, bile salts and some antibiotics such as {{c1::<b>penicillin</b>}}", {1: Z}, D,
    'Membrana externa como barreira', '24; apostila veteranos aula 1; Trabulsi 2', 'central', "'outer membrane lysozyme/penicillin' sem card.", [1500401818042, 1500403421264],
    'Azul: barreira da apostila e do Trabulsi.'),
 ak('lps-outer', 1500403683098, {1: V, 2: V, 3: V}, D, 'LPS na membrana externa de Gram-negativos', 23, 'Verdes: questão 5 da lista.'),
 ak('lps-parts', 1500403730274, {1: Z, 2: V, 3: V}, D, 'Componentes do LPS', 23, 'Verdes: lipídio A e antígeno O da lâmina 23; azul: polissacarídeo central.'),
 ak('lipid-a', 1500403894345, {1: V}, D, 'Lipídio A é a endotoxina', 23, 'Verde: endotoxina (lâmina 23; prova E. coli).', nota='LPS = endotoxin: it causes fever'),
 ak('o-antigen', 1500403990466, {1: Z}, D, 'Antígeno O', 23, 'Azul: antígeno somático O (lâmina 23).'),
 ak('cocos-positivos', 1500415806490, {1: V, 2: Z}, D, 'Maioria dos cocos é Gram-positiva', 27, 'Verde c1 (HY 1), azul c2: generalização da lista da lâmina 27.'),
 ak('bacilos-negativos', 1500416119700, {1: V}, D, 'Maioria dos bacilos é Gram-negativa', 27, 'Verde: HY 1; exceções Bacillus, Clostridium, Listeria.'),
 # ---------- E. Bactérias que o Gram não mostra (lâminas 28–32) ----------
 ak('intracelulares-gram', 1500417845213, {1: V, 2: V, 3: Z, 4: R, 5: Z}, E, 'Intracelulares não coram bem ao Gram', 28, 'Verdes c1–c2 (HY 1): questão 8 da lista; exemplos azuis; Legionella rosa (fora da aula).'),
 ak('micobacteria-zn', 1500402778103, {1: V, 2: V, 3: V}, E, 'Ácido micólico e Ziehl-Neelsen', 29, 'Verdes: lâmina 29 e questão 9.'),
 ak('zn-fucsina', 1500418458789, {1: V, 2: V}, E, 'Ziehl-Neelsen usa fucsina fenicada', 29, 'Verdes: HY 1; protocolo da lâmina 29.',
    nota='Acid-fast bacilli (BAAR) stay red; the background takes methylene blue'),
 ak('campo-escuro', 1502040652936, {1: V}, E, 'Treponema ao campo escuro', 30, 'Verde: espiroquetas finas demais para o Gram (lâmina 30).',
    nota='Spirochetes are too thin for Gram, though their envelope is Gram-negative'),
 ak('prata-treponema', 1516067477257, {1: V}, E, 'Espessamento com prata', 30, 'Verde: HY 2; impregnação por prata (lâmina 30, questão 3).'),
 ak('chlamydia-giemsa', 1501984301125, {1: V}, E, 'Chlamydia ao Giemsa', 31, 'Verde: lâmina 31 e PDF II p. 33.',
    nota='Too small and obligately intracellular: we see dense cytoplasmic inclusions'),
 ak('mycoplasma', 1500402206974, {1: V, 2: V, 3: V}, E, 'Mycoplasma sem parede, com esteróis', 32, 'Verdes: lâmina 32 e questão 8.',
    nota='The smallest bacteria (about 0.3 µm); diagnosis by PCR; penicillins do not work'),
 # ---------- F. Demais estruturas (lâminas 33–44) ----------
 ak('nucleoide', 1500401372694, {1: Z}, F, 'Nucleoide livre no citoplasma', 34, 'Azul: material genético (lâmina 34).'),
 ak('dna-circular', 1716930573427, {1: Z, 2: Z}, F, 'Cromossomo circular', 34, 'Azuis: DNA cromossomal circular (apostila).', origin='MCAT'),
 ak('plasmid', 1500405795435, {1: V}, F, 'Plasmídeo', 34, 'Verde: DNA acessório (lâmina 34, questão 13).',
    nota='Present in some isolates of a species and absent in others'),
 ak('ribossomo-70s', 1500405985333, {1: V}, F, 'Ribossomo 70S (50S + 30S)', 35, 'Verde: ribossomos procarióticos (lâmina 35).'),
 ak('flagelo', 1500405949770, {1: V}, F, 'Flagelo para motilidade', 36, 'Verde: função do flagelo (lâmina 36, questão 10).'),
 au('flagelo-partes', 'A bacterial flagellum has a basal body, a hook and a long filament made of {{c1::<b>flagellin</b>}}', {1: Z}, F,
    'Partes do flagelo', '36; monitoria P1; Trabulsi 2', 'central', "'flagellin' só traz PRR.", [1500405949770, 1520299451730],
    'Azul: composição da lâmina 36.', extra='- Speed: 200–500 µm/s'),
 ak('flagellar-basal', 1714580117082, {1: Z}, F, 'Corpo basal gera o torque', 36, 'Azul: nota com revisão preservada.'),
 au('flagelo-posicao', 'Flagella spread all over the cell surface are {{c1::<b>peritrichous</b>}}, whereas a tuft at one pole is {{c2::<b>lophotrichous</b>}}', {1: Z, 2: R}, F,
    'Disposição dos flagelos', '37; Trabulsi 2', 'central', "'peritrichous', 'lophotrichous' sem card.", [1500405949770, 1500416644544],
    'Azul c1, rosa c2: disposições da lâmina 37.', extra='- Monotrichous: one polar flagellum; amphitrichous: one at each pole'),
 ak('pili-funcoes', 1500405416810, {1: V}, F, 'Pili: adesão e conjugação', 38, 'Verde: funções da lâmina 38; questão 10.'),
 ak('fimbriae-uti', 1500405519933, {1: V}, F, 'Fímbrias da E. coli e ITU', 38, 'Verde: adesão (lâmina 38; prova E. coli).'),
 au('pili-fago', 'Some pili serve as receptors for {{c1::<b>bacteriophages</b>}}', {1: R}, F,
    'Pili como receptores de fagos', '38–39', 'lateral', "'pili phage' sem card.", [1500405416810, 1500673825876], 'Rosa: função da lâmina 38 e foto da lâmina 39.'),
 ak('conjugacao', 1500673825876, {1: V}, F, 'Conjugação pelo pilus sexual', 39, 'Verde: plasmídeo transferido por conjugação (lâmina 39).'),
 ak('esporo-dormente', 1500406328514, {1: Z}, F, 'Esporo é forma dormente', 40, 'Azul: esporos (lâmina 40).'),
 au('esporo-indutores', 'Bacteria form endospores when {{c1::<b>nutrients</b>}} run out or the environment turns hostile', {1: Z}, F,
    'Indutores da esporulação', '40; apostila veteranos aula 1; Trabulsi 2', 'central', "'endospore*' sem os indutores.", [1500406328514, 1506122411482],
    'Azul: agentes indutores da lâmina 40.', extra='- Also drying, high temperature, chemicals and radiation'),
 ak('esporo-resistente', 1500406397088, {1: V}, F, 'Esporo sobrevive anos em condições extremas', 40, 'Verde: resistência (lâminas 40–41).'),
 au('esporo-generos', 'Endospore formers are mostly Gram-positive rods of the genera {{c1::<b>Bacillus</b>}} and {{c2::<b>Clostridium</b>}}', {1: V, 2: V}, F,
    'Bacillus e Clostridium', '41; apostila veteranos aula 1; questão 12', 'central', "'endospore*' sem os gêneros.", [1506120920952, 1522248504847],
    'Verdes: lâmina 41 e questão 12 (esporos não estão em todas as bactérias).', extra='- They live mainly in soil'),
 au('esporo-posicao', 'Depending on the species, the endospore sits at a {{c1::<b>terminal</b>}}, subterminal or central position', {1: R}, F,
    'Posição do esporo', '40', 'lateral', "'spore terminal' sem card.", [1500406328514, 1506122411482], 'Rosa: figura da lâmina 40.'),
 au('wirtz', 'The {{c1::<b>Wirtz</b>}} stain colors bacterial spores green and vegetative cells red', {1: R}, F,
    'Coloração de Wirtz', '41; questão 9', 'lateral', "'Wirtz' sem card.", [1500418458789, 1506122411482], 'Rosa: lâmina 41 e resposta da questão 9.'),
 ak('spore-core', 1506122411482, {1: V}, F, 'Ácido dipicolínico no esporo', 41, 'Verde: resistência ao calor (apostila: núcleo desidratado).'),
 ak('spore-cortex', 1500406911196, {1: R, 2: R}, F, 'Córtex de peptidoglicano', 41, 'Rosas: esporogênese da apostila (camadas de peptidoglicano).'),
 ak('spore-boiling', 1522248504847, {1: V}, F, 'Esporo resiste à fervura', 41, 'Verde: ponte com controle microbiológico.'),
 au('granulos', 'Bacteria store reserves as insoluble {{c1::<b>granules</b>}} (polyphosphate, PHB, sulfur), so internal osmotic pressure does not rise', {1: Z}, F,
    'Grânulos de reserva', '42; monitoria P1; Trabulsi 2; questão 11', 'central', "'polyphosphate', 'metachromatic' sem card bacteriano.", [1500406328514, 1500401372694],
    'Azul: lâmina 42 e questão 11.', extra='- Polyhydroxybutyrate can be made into biodegradable plastic'),
 ak('capsula-definida', 1500405311709, {1: V}, F, 'Cápsula: camada definida e aderida', 43, 'Verde: questão 14 da lista.'),
 ak('glicocalice', 1500405222910, {1: Z}, F, 'Camada mucosa/glicocálice irregular', 43, 'Azul: camada mucosa da lâmina 43 e questão 14.'),
 ak('capsule-phago', 1506213628784, {1: V}, F, 'Cápsula inibe a fagocitose', 44, 'Verde: nota com revisão preservada (texto adaptado na versão Codex).',
    text='A bacterial capsule increases virulence by inhibiting {{c1::phagocytosis}}'),
 ak('pneumococo-capsula', 1503185369445, {1: V}, F, 'Cápsula do pneumococo', 44, 'Verde: HY 1; exemplo Gram-positivo da lâmina 44 (perda da cápsula, perda de virulência).'),
 ak('ecoli-capsula', 1510188103396, {1: V}, F, 'E. coli tem cápsula (antígeno K)', 44, 'Verde: HY 1; lâmina 44 e prova (E. coli: cápsula com antígeno K).',
    nota='The E. coli capsule carries the K antigen'),
 au('camada-s', 'The {{c1::<b>S-layer</b>}} is a surface layer of protein, mainly in archaea', {1: R}, F,
    'Camada S', '43; Trabulsi 2', 'lateral', "'S-layer' sem card.", [1500405311709, 1500405222910], 'Rosa: rótulo da lâmina 43.'),
 ak('biofilme-epidermidis', 1503084290841, {1: V}, F, 'Biofilme do S. epidermidis em próteses', 44, 'Verde: exemplo clínico da lâmina 44.'),
 ak('biofilme-pseudomonas', 1506213366727, {1: V}, F, 'Pseudomonas na fibrose cística', 44, 'Verde: HY 1; exemplo da lâmina 44 (biofilme no pulmão).'),
 ak('mutans-carie', 1503187580974, {1: Z}, F, 'S. mutans e cárie', 44, 'Azul: adesão ao dente e placa (lâmina 44).'),
 au('biofilme-resistencia', 'Bacteria inside a {{c1::<b>biofilm</b>}} resist biocides and antibiotics much better than free cells', {1: Z}, F,
    'Biofilme protege', '44; apostila veteranos aula 1; Trabulsi 2', 'central', "'biofilm* antibiotic*' sem card.", [1503084290841, 1500405332195],
    'Azul: vantagem do biofilme (apostila, Trabulsi).', extra='- Outer layers shield the denser inner layers'),
]
EXCLUIDOS = [
 (1500674235789, 'conjugação normal só transfere plasmídeo: detalhe da aula de genética bacteriana'),
 (1489092893676, 'PBP/transpeptidase: mecanismo de antibiótico, aula 05'),
 (1500403557504, 'LPS dirige a resposta imune: repete lps-outer e lipid-a'),
]
FORA_DO_RECORTE = ['mecanismos de ação de antibióticos (aula 05)', 'genética bacteriana e Hfr (aula 06)',
                   'fisiologia e crescimento bacteriano (aula 02)', 'doenças de cada patógeno citado como exemplo (lâmina 27)']

# Verso curto onde o AnKing veio sem Extra (créditos removidos) ou o autoral ainda não tinha explicação (09/10)
NOTAS = {
 'meio-diferencial': 'Blood agar shows hemolysis; lactose media separate lac+ from lac- colonies',
 'virus-me': 'Bacteria and fungi are already visible with the light microscope',
 'estreptobacilos': 'Bacilli divide only across their short axis, so they form few arrangements',
 'membrana-composicao': 'Mg²⁺ and Ca²⁺ help hold the membrane together',
 'gram-purple': 'They keep the crystal violet–iodine complex in their thick wall',
 'gram-pink': 'They lose the violet with alcohol and take the red counterstain',
 'pg-percentual': 'Gram-negatives add an outer membrane instead',
 'pg-nagnam': 'Peptidoglycan (murein) exists only in bacteria',
 'pg-peptideo': 'Cross-links between these peptides give the wall its rigidity',
 'lta-gram': 'Lipoteichoic acid is anchored in the membrane; wall teichoic acid binds peptidoglycan',
 'teicoico-autolisina': 'Autolysins cut peptidoglycan at set points so new units can be inserted',
 'periplasma': 'It holds the thin peptidoglycan, hydrolytic enzymes and transport proteins',
 'membrana-externa-barreira': 'Nutrients still get in through porins',
 'cocos-positivos': '<i>Neisseria</i> (Gram-negative diplococci) is the classic exception',
 'bacilos-negativos': '<i>Bacillus</i>, <i>Clostridium</i> and <i>Listeria</i> are Gram-positive rods',
 'dna-circular': 'Usually a single circular double-stranded chromosome in the nucleoid',
 'pili-fago': 'The lesson shows a phage attached to an <i>E. coli</i> pilus',
 'conjugacao': 'Plasmids carrying resistance genes spread this way',
 'esporo-dormente': 'A bacterial spore is not reproductive: one cell makes one spore',
 'esporo-posicao': 'Position helps identify the species (terminal in <i>C. tetani</i>)',
 'wirtz': 'Malachite green with heat stains the spore; safranin stains the cell',
 'spore-cortex': 'From inside out: core, cortex, coat',
 'camada-s': 'It supports cells that lack true peptidoglycan',
 'capsule-phago': 'Losing the capsule can cost a bacterium its virulence (<i>S. pneumoniae</i>)',
 'biofilme-epidermidis': 'Its glycocalyx glues it to catheters and heart valves',
}
DUP = {'membrana-sem-esterol': 'ganho: regra geral (procarioto sem esterol); o AnKing cobra a exceção do Mycoplasma',
       'esporo-generos': 'ganho: os dois gêneros formadores de esporo; os AnKing cobram espécies isoladas',
       'biofilme-resistencia': 'ganho: por que o biofilme protege; os AnKing cobram exemplos clínicos'}
for c in CARDS:
    n = NOTAS.get(c['key'])
    if n:
        if c['kind'] == 'autoral':
            c['extra'] = (c['extra'] + '<br>' if c.get('extra') else '') + f'- {n}'
        else:
            c['extra_add'] = (c['extra_add'] + '<br>' if c.get('extra_add') else '') + f'- {n}'
    if c['key'] in DUP:
        c['duplicacao_ok'] = DUP[c['key']]
