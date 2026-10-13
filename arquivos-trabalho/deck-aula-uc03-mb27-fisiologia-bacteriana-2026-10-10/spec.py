# Especificação curada — Fisiologia bacteriana (UC03 P2, Microbiologia; Profa. Elisabete Vicente; 50 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-mb27-20261010a"
SHORT = "mb27"
LESSON = "2026-uc03-microbiologia-27-fisiologia-bacteriana"
DECK = "NEBLI::UC03::P2::Microbiologia::Fisiologia bacteriana"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-04) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 14 consultas), seções FirstAid de bacteriologia básica, meios e anaeróbios (busca/tags-secao.txt), 10/10: ")
EXCLUIDOS = [
 (1500491169533, "Thayer-Martin: meio não citado na aula"),
 (1500496491175, "EMB: meio não citado"),
 (1500498963820, "clindamicina para anaeróbios: clínica fora da aula (F-20261010-CLAUDE-04)"),
 (1500499083027, "metronidazol: clínica fora da aula"),
 (1500498334911, "aminoglicosídeos e anaeróbios: aula de antibióticos"),
]
FORA_DO_RECORTE = ["meios específicos não citados (Thayer-Martin, EMB, Löwenstein)", "tratamento de infecções por anaeróbios", "provas bioquímicas individuais (aula prática)"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_ = ("A-nutricao", "B-fatores-fisicos", "C-ferro", "D-energia", "E-crescimento", "F-meios-identificacao")
CARDS = [
 # ---------- A. Nutrição (slides 2–4) ----------
 au("crescimento-def", "Bacteria multiply by {{c1::binary fission}}, so growth means an increase in cell number", {1: V}, A_,
    "Crescimento = aumento do número", "2; monitoria", "central", "sem card nos acervos.", [1500671879509, 1500672960517],
    "Verde: definição que abre a aula.", extra="- Each daughter cell gets one old and one new DNA strand"),
 au("macronutrientes", "Carbon, nitrogen, sulfur and {{c1::phosphorus}} make up most of the bacterial dry weight", {1: R}, A_,
    "Macronutrientes", "3", "lateral", "sem card nos acervos.", [1500491274684, 1500490858110], "Rosa: lâmina 3.", extra="- Carbon alone is about half of the dry weight"),
 au("quimio-hetero", "Bacteria that cause human disease are {{c1::chemoheterotrophs}}, using organic compounds for energy and carbon", {1: V}, A_,
    "Patógenos são quimio-heterotróficos", "2, 4", "central", "sem card nos acervos.", [1500491274684, 1500498597825], "Verde: lâminas 2 e 4."),
 # ---------- B. Fatores físicos (slides 5–9) ----------
 au("ph-neutro", "Most bacteria grow best at a pH near {{c1::7}}", {1: Z}, B_,
    "pH ótimo neutro", "5", "central", "sem card nos acervos.", [1500491274684, 1500498597825], "Azul: lâmina 5.", extra="- They keep cytoplasmic pH near neutral with proton pumps"),
 au("mesofilos", "Bacteria that infect humans are {{c1::mesophiles}}, growing best near body temperature", {1: V}, B_,
    "Patógenos são mesófilos", "6", "central", "sem card nos acervos.", [1500497965459, 1500499431143],
    "Verde: lâmina 6.", extra="- Psychrophiles prefer cold; thermophiles prefer heat"),
 ak("aerobio-sod", 1500497653901, {1: V, 2: Z}, B_, "Aeróbios têm SOD e catalase", 8, "Verde c1, azul c2; lâmina 8."),
 ak("o2-aceptor", 1500497965459, {1: Z}, B_, "O₂ é aceptor final no aeróbio", 8, "Azul: lâminas 8 e 17. Extra do AnKing corrigido: dizia que só aeróbios respiram.", extra="- Facultative anaerobes also respire; anaerobic respiration uses other acceptors such as nitrate"),
 au("microaerofilo", "{{c1::Microaerophiles}} need oxygen, but only at low concentrations", {1: Z}, B_,
    "Microaerófilos", "8", "central", "sem card nos acervos.", [1500497653901, 1500499431143], "Azul: lâmina 8."),
 ak("facultativo", 1500499431143, {1: V}, B_, "Anaeróbio facultativo", 8, "Verde: lâmina 8 (E. coli)."),
 ak("clostridium-anaerobio", 1500498894447, {1: V, 2: Z}, B_, "Clostridium é anaeróbio estrito", 8, "Verde c1, azul c2; exemplo da lâmina 8 (C. tetani)."),
 au("tubo-aerobio", "In a liquid culture tube, obligate aerobes grow at the {{c1::top}}, where oxygen is highest", {1: Z}, B_,
    "Crescimento no tubo conforme o O₂", "8", "central", "sem card nos acervos.", [1500497653901, 1500499431143],
    "Azul: figura da lâmina 8.", extra="- Obligate anaerobes at the bottom; facultatives throughout, densest at the top"),
 au("halotolerante", "Staphylococcus aureus is {{c1::halotolerant}}, growing at salt levels that inhibit most bacteria", {1: R}, B_,
    "Halotolerância de S. aureus", "9", "lateral", "sem card nos acervos.", [1500493788099, 1500420138936], "Rosa: exemplo da lâmina 9."),
 # ---------- C. Ferro (slides 10–11) ----------
 au("ferro-critico", "Iron is a critical micronutrient that sets the pace of bacterial growth and turns on {{c1::virulence}} mechanisms", {1: Z}, C_,
    "Ferro como micronutriente crítico", "10–11", "central", "sem card nos acervos.", [1487642782702, 1520444212406], "Azul: lâmina 11."),
 au("ferro-imunidade", "Keeping iron bound to transferrin, lactoferrin and ferritin to starve microbes is called {{c1::nutritional immunity}}", {1: V}, C_,
    "Imunidade nutricional", "10–11", "central", "sem card nos acervos.", [1487642782702, 1520444212406], "Verde: lâminas 10–11."),
 ak("lactoferrina", 1487642782702, {1: Z, 2: V}, C_, "Lactoferrina quela ferro", 11, "Verde c2 (quelação), azul c1."),
 au("sideroforo", "Pathogenic bacteria capture host iron with secreted chelators called {{c1::siderophores}}", {1: V}, C_,
    "Sideróforos", "10–11", "central", "consulta siderophore* só com Rhizopus.", [1487642782702, 1500335381221],
    "Verde: lâminas 10–11.", extra="- Others lyse red cells (hemolysins) or bind transferrin directly"),
 au("fur", "When iron is low, the repressor {{c1::Fur}} is inactive, so siderophore and toxin genes are expressed", {1: R}, C_,
    "Regulon Fur", "10", "lateral", "sem card nos acervos.", [1487642782702, 1500335381221],
    "Rosa: lâmina 10.", extra="- Example: diphtheria toxin is made under iron starvation"),
 # ---------- D. Energia (slides 12–20) ----------
 au("substrato", "In fermentation, ATP is made only by {{c1::substrate-level}} phosphorylation", {1: V}, D_,
    "Fermentação: fosforilação no substrato", "12–14", "central", "consulta substrate-level sem card.", [1500498597825, 1500498676105], "Verde: lâmina 12."),
 au("fermentacao-nad", "Fermentation regenerates NAD+ by using pyruvate-derived compounds as the final {{c1::electron acceptor}}", {1: Z}, D_,
    "Fermentação regenera NAD⁺", "15, 19", "central", "sem card nos acervos.", [1500498597825, 1500498676105],
    "Azul: lâmina 15.", extra="- Lactic acid bacteria: glucose → lactate"),
 ak("anaerobio-fermenta", 1500498597825, {1: Z}, D_, "Anaeróbios estritos fermentam", 16, "Azul: lâmina 16."),
 ak("fermentacao-produtos", 1500498676105, {1: Z, 2: Z}, D_, "Produtos da fermentação", 18, "Azuis: lâmina 18."),
 au("membrana-cadeia", "In bacteria, the electron transport chain lies in the {{c1::plasma membrane}}", {1: V}, D_,
    "Cadeia respiratória na membrana", "16–17", "central", "sem card nos acervos.", [1500497965459, 1500498050972],
    "Verde: lâmina 17.", extra="- In eukaryotes it lies in the mitochondria"),
 au("respiracao-anaerobia", "In anaerobic respiration, a molecule other than O2, such as {{c1::nitrate}}, is the final electron acceptor", {1: Z}, D_,
    "Respiração anaeróbia", "17", "central", "sem card nos acervos.", [1500497965459, 1500499484551],
    "Azul: lâmina 17.", extra="- Efficiency is between aerobic respiration and fermentation"),
 # ---------- E. Crescimento (slides 21–24; provas) ----------
 ak("curva-fases", 1500671879509, {1: V}, E_, "Fases da curva de crescimento", 22, "Verde: cobrada em quase todas as provas."),
 au("lag", "In the {{c1::lag}} phase, bacteria adapt and gain mass but barely divide", {1: V}, E_,
    "Fase lag", "22, 24; provas 2023, 2019", "prova", "AnKing só lista as fases.", [1500671879509, 1500672960517],
    "Verde: provas.", extra="- It explains why cultures take time to turn positive"),
 ak("log-geracao", 1500672960517, {1: V}, E_, "Fase log depende do tempo de geração", 24, "Verde: provas 2018 e 2025."),
 au("geracao-ecoli", "Under ideal conditions, Escherichia coli divides about every {{c1::20}} minutes", {1: Z}, E_,
    "Tempo de geração comparado", "24; prova 2025 P2 3.2; monitoria", "prova", "sem card nos acervos.", [1500672960517, 1582847241587], "Azul: prova 2025."),
 au("estacionaria", "In the stationary phase, new cells are balanced by cell {{c1::death}} as nutrients run out and wastes build up", {1: V}, E_,
    "Fase estacionária", "22, 24; provas; monitoria", "prova", "sem card nos acervos.", [1500671879509, 1500672960517],
    "Verde: provas.", extra="- Quorum-sensing signals also accumulate"),
 au("declinio", "In the decline phase, deaths outnumber divisions until the culture may become {{c1::sterile}}", {1: Z}, E_,
    "Fase de declínio", "22, 24; provas", "prova", "sem card nos acervos.", [1500671879509, 1500672960517], "Azul: lâmina 24."),
 au("virulencia-fase", "Staphylococcus aureus expresses adhesins in the exponential phase and secretes most toxins in the {{c1::stationary}} phase", {1: Z}, E_,
    "Curva e fatores de virulência", "23", "central", "sem card nos acervos.", [1500671879509, 1500493788099], "Azul: lâmina 23."),
 au("antibiotico-log", "Antibiotics that block cell growth work best on bacteria in the {{c1::log}} phase", {1: V}, E_,
    "Antibiótico mais eficaz na fase log", "24; provas 2024 P2 1.10, 2019 P2 2.4", "prova", "sem card nos acervos.", [1500672960517, 1500671879509], "Verde: provas."),
 au("turbidez", "Bacterial growth in broth can be followed by the rise in {{c1::turbidity}} measured in a spectrophotometer", {1: R}, E_,
    "Medida por turvação", "21; monitoria", "lateral", "sem card nos acervos.", [1500671879509, 1500672960517],
    "Rosa: monitoria.", extra="- Colony counts after serial dilution measure viable cells"),
 # ---------- F. Meios, isolamento e identificação (slides 25–49) ----------
 ak("seletivo", 1500490858110, {1: Z}, F_, "Meio seletivo", 26, "Azul: lâminas 25–26."),
 ak("indicador", 1500491508023, {1: Z}, F_, "Meio indicador (diferencial)", 25, "Azul: lâmina 25."),
 ak("enriquecido", 1500491274684, {1: R}, F_, "Meio enriquecido", 29, "Rosa: lâmina 29."),
 ak("maconkey", 1500496061553, {1: V, 2: V, 3: Z}, F_, "MacConkey seletivo para Gram-negativos", 30, "Verdes c1–c2, azul c3; lâminas 27–31."),
 ak("maconkey-lactose", 1500496166406, {1: V}, F_, "MacConkey diferencia fermentadores de lactose", 30, "Verde: lâmina 30."),
 ak("lactose-rosa", 1402600814505, {1: Z}, F_, "Fermentadores de lactose ficam rosa", 31, "Azul: HY que repete maconkey-lactose (F-20261010-CLAUDE-03).", hy_repete="maconkey-lactose"),
 au("ss-h2s", "In SS agar, thiosulfate and ferric citrate reveal {{c1::H2S}} production as black colonies", {1: Z}, F_,
    "Ágar SS detecta H₂S", "32–33", "central", "sem card nos acervos.", [1500496061553, 1500490858110],
    "Azul: lâmina 32.", extra="- SS agar is highly selective for Salmonella and Shigella"),
 au("enriquecimento-salmonella", "Tetrathionate and selenite broths are {{c1::enrichment}} media that favor Salmonella and Shigella from stool", {1: R}, F_,
    "Caldos de enriquecimento", "26, 28", "lateral", "sem card nos acervos.", [1500491274684, 1500490858110], "Rosa: lâminas 26 e 28."),
 ak("sangue-nao-seletivo", 1500491213487, {1: Z}, F_, "Ágar sangue não seletivo", 34, "Azul: lâminas 26 e 34."),
 ak("beta-hemolise", 1500492032825, {1: V}, F_, "β-hemólise", 34, "Verde: padrões de hemólise da lâmina 34."),
 ak("alfa-hemolise", 1500492267320, {1: Z}, F_, "α-hemólise", 34, "Azul: HY recíproco de beta-hemolise (F-20261010-CLAUDE-03).", hy_repete="beta-hemolise"),
 ak("gama-hemolise", 1500492284543, {1: Z}, F_, "γ-hemólise", 34, "Azul: HY recíproco de beta-hemolise (F-20261010-CLAUDE-03).", hy_repete="beta-hemolise"),
 ak("chocolate", 1500493993054, {1: Z}, F_, "Ágar chocolate: hemácias lisadas pelo calor", 35, "Azul: lâmina 35."),
 au("chocolate-fatores", "Heating blood in chocolate agar releases factors X (hemin) and V ({{c1::NAD}}) for fastidious bacteria", {1: Z}, F_,
    "Fatores X e V", "35", "central", "sem card do mecanismo nos acervos.", [1500493993054, 1500491657086],
    "Azul: lâmina 35.", extra="- In plain blood agar, red-cell enzymes inactivate factor V"),
 au("esgotamento", "Streaking a plate dilutes the inoculum so that single cells grow into {{c1::isolated colonies}}", {1: V}, F_,
    "Esgotamento do inóculo", "21, 37–40", "central", "sem card nos acervos.", [1500491213487, 1500490858110],
    "Verde: lâminas 39–40.", extra="- An isolated colony is a pure culture for identification"),
 au("rugai", "The Rugai (IAL) tube tests several traits at once, including indole, H2S, urease, lysine and {{c1::motility}}", {1: R}, F_,
    "Meio de Rugai", "44", "lateral", "sem card nos acervos.", [1500491508023, 1500496166406], "Rosa: lâmina 44."),
 au("cromogenico", "Chromogenic media identify bacteria by colony {{c1::color}} produced by species-specific enzymes", {1: Z}, F_,
    "Meios cromogênicos", "45–46", "central", "consulta chromogenic sem card.", [1500491508023, 1500496166406],
    "Azul: lâminas 45–46.", extra="- One plate, without confirmatory tests, e.g. urinary pathogens"),
 au("cromo-candida", "On chromogenic Candida agar, Candida albicans grows as {{c1::green}} colonies", {1: R}, F_,
    "Cromogênico de Candida", "47", "lateral", "sem card nos acervos.", [1500491508023, 1500234684400], "Rosa: lâmina 47."),
 au("antibiograma", "Antibiotic susceptibility is tested by disk diffusion, {{c1::MIC}} methods (microdilution, E-test) or automated systems", {1: Z}, F_,
    "Testes de sensibilidade", "48", "central", "sem card nos acervos.", [1500491213487, 1500490858110], "Azul: lâmina 48."),
 au("mrsa-vre", "Chromogenic screening media can detect MRSA and vancomycin-resistant {{c1::enterococci}}", {1: R}, F_,
    "Cromogênicos para MRSA e VRE", "49", "lateral", "sem card nos acervos.", [1500491508023, 1500493788099], "Rosa: lâmina 49."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {'quimio-hetero': '- Plants are photosynthetic; animals and most bacteria are chemoheterotrophs',
 'microaerofilo': '- In a tube they grow just below the surface',
 'facultativo': '- Example in the lesson: E. coli',
 'halotolerante': '- Non-halophiles such as Escherichia coli stop growing at high salt',
 'ferro-critico': '- Iron is a cofactor for cytochromes, catalase, SOD and DNA synthesis',
 'ferro-imunidade': '- Free iron in the host is almost zero',
 'lactoferrina': '- Found in mucosal secretions and neutrophils',
 'substrato': '- Glycolysis yields a net 2 ATP per glucose',
 'curva-fases': '- Plus a decline (death) phase at the end',
 'declinio': '- Cells autolyze as macromolecules are degraded',
 'virulencia-fase': '- Example adhesins: clumping factor, fibronectin-binding protein; toxins later',
 'log-geracao': '- Population grows as X = X0 · 2^n',
 'geracao-ecoli': '- M. tuberculosis takes about a day, so TB cultures take weeks',
 'antibiotico-log': '- Bacteriostatic and cell-wall drugs need active division',
 'indicador': '- A pH indicator shows which colonies ferment a sugar',
 'seletivo': '- Inhibitors include dyes, bile salts and heavy metals',
 'enriquecimento-salmonella': '- They suppress competing gut flora before plating',
 'maconkey': '- Crystal violet also inhibits gram-positives',
 'sangue-nao-seletivo': '- Base rich in peptone plus 5% sheep blood',
 'chocolate': '- Heated to about 80 °C',
 'rugai': '- Upper (slant) and lower parts read different reactions',
 'cromo-candida': '- C. tropicalis is metallic blue; C. krusei is pink',
 'antibiograma': '- Example: reduced zones around carbapenem disks (ertapenem, imipenem, meropenem)',
 'mrsa-vre': '- Colonies change color only if the resistant strain grows'}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
DUPLICACAO = {"virulencia-fase": "ganho: liga a fase estacionária à expressão de toxinas; curva-fases só nomeia as fases"}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
