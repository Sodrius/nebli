# Especificação curada — Biologia geral dos fungos (UC03 P3, Microbiologia, aula 43; Prof. Carlos Pelleschi Taborda; 61 lâminas).
# Reconstrução pelo Claude em 09/10/2026 (plano de 08/10: substituir a versão Codex de 03–04/10, 66 cards nunca estudados).
# Feita a partir de inventario-aula.json/planejamento.json (escritos antes). Ordem = slides. Critérios até F-20261009-CLAUDE-01.
# AnKing → MCAT/externos → autoral. A micologia básica (parede, hifas, reprodução, ecologia) quase não existe no AnKing nem no
# MCAT (busca/anking.txt, busca/ext.txt): os autorais ficam só no que é central ou cobrado em prova; detalhes laterais vão ao
# Extra/Tab (Davi, 08/10: "ainda há mt card autoral"). Exceção local de autoria já registrada em gates (F-20261004-CODEX-02).
RUN_ID = "uc03-mb43-20261009a"
SHORT = "mb43"
LESSON = "2026-uc03-microbiologia-43-biologia-fungos"
DECK = "NEBLI::UC03::P3::Microbiologia::Biologia geral dos fungos"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261009-CLAUDE-01) + PLANO-AJUSTES-ANKI-2026-10-08, 09/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre, todos os campos (busca/anking.txt, 40 consultas; busca/ext.txt, "
         "7 consultas; nebli.busca_acervos, 09/10): ")
EXCLUIDOS = [
 (1509742814980, "ergosterol na membrana: repete 1468250158738 (mesmo alvo, HY menor)"),
 (1509743058195, "polienos formam poros: repete 1509742201770"),
 (1509742443199, "flucitosina → 5-FU: repete 1509742361304"),
 (1509742586045, "citosina desaminase: detalhe enzimático fora do slide"),
 (1500234258289, "Candida inverte o dimorfismo: detalhe da aula de candidíase"),
 (1500243540399, "tubo germinativo: teste diagnóstico da aula de micologia prática/candidíase"),
 (1500244315193, "antígeno capsular polissacarídico: repete o card da cápsula"),
 (1500245573893, "tinta da China: diagnóstico da criptococose, aula de micoses sistêmicas"),
 (1500238441939, "ângulo de ramificação do Aspergillus: aula de micoses oportunistas"),
 (1499968902834, "Histoplasma e fezes de aves/morcegos: micoses sistêmicas"),
]
FORA_DO_RECORTE = ["micoses específicas (cutâneas, subcutâneas, sistêmicas e oportunistas): aulas seguintes da P3",
                   "uso clínico dos antifúngicos (indicações, toxicidades além das do slide)",
                   "testes diagnósticos (KOH, tinta da China, tubo germinativo)"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


A_, B_, C_, D_, E_, F_ = ("A-importancia", "B-caracteristicas-e-celula", "C-antifungicos", "D-taxonomia-e-reproducao",
                          "E-filos", "F-ecologia-e-nutricao")
CARDS = [
 # ---------- A. Fungos, vida humana e natureza (slides 3–16) ----------
 au("fermentacao", "In bread and beer making, <b>yeasts</b> ferment sugar into ethanol and {{c1::<b>CO₂</b>}}", {1: R}, A_,
    "Leveduras fermentadoras", "3; Benedito p. 4", "lateral", "AnKing/MCAT não têm fermentação por levedura (busca 'fermentation yeast', 'Saccharomyces').",
    [1500401344665, 1500333766310], "Rosa: abre o bloco de importância; útil, pouco ganho longitudinal.",
    extra="- Fungi also give us cheeses and antibiotics (<b>penicillin</b> from <i>Penicillium</i>)"),
 au("saprofita", "Most fungi live as {{c1::<b>saprobes</b>}}, decomposing dead organic matter in soil and food", {1: Z}, A_,
    "Sapróbios decompositores", "7; Trabulsi 64.2; prova 2015 P2 29.3", "prova", "nenhum card AnKing/MCAT define sapróbio (busca 'saprophyt*', 'decompos*').",
    [1500243882463, 1500401344665], "Azul: 'características do fungo em saprofitismo' (prova 2015).",
    extra="- Others live as <b>parasites</b> or <b>mutualists</b>: mycorrhizae (plant roots), lichens (algae)"),
 ak("rhizopus-pao", 1500333766310, {1: V, 2: V}, A_, "Rhizopus, mofo do pão", 9, "Verde: HY (1); mofo do pão do slide 9 e Benedito p. 41."),
 ak("aflatoxina-chc", 1486591290032, {1: V, 2: V}, A_, "Micotoxina: aflatoxina do Aspergillus → hepatocarcinoma", 10, "Verde: HY (2); micotoxinas do slide 10."),
 ak("aflatoxina-graos", 1517779158524, {1: V}, A_, "Aflatoxina em grãos e nozes mal armazenados", 10, "Verde: HY (2); grãos contaminados do slide 10."),
 au("melanina", "{{c1::<b>Melanin</b>}} deposited in the fungal cell wall protects the fungus against ionizing radiation", {1: R}, A_,
    "Melanina na parede: proteção (Chernobyl)", "16 e 22", "lateral", "sem card de melanina fúngica no AnKing/MCAT (busca 'melanin fung*').",
    [1500244482455, 1468250158738], "Rosa: experimento de Chernobyl; liga com 'parede: proteção, melanina' do slide 22.",
    extra="- Melanized fungi even grew faster under radiation"),
 # ---------- B. Características e célula fúngica (slides 17–26) ----------
 au("animais", "Genetic analysis shows that fungi are more closely related to {{c1::<b>animals</b>}} than to plants", {1: Z}, B_,
    "Fungos mais próximos de animais", "18; Prof. Dave (taxonomia); Strong Medicine", "central", "nenhum card AnKing/MCAT sobre a posição filogenética dos fungos.",
    [1500401344665, 1716930573427], "Azul: árvore do slide 18; explica por que antifúngicos são tóxicos.",
    extra="- Kept in kingdom Plantae until Whittaker (1969)<br>- Slime molds were moved out to Protista"),
 au("colonias", "{{c1::<b>Yeasts</b>}} form creamy, pasty colonies, whereas {{c2::<b>molds</b>}} form cottony, velvety or powdery ones", {1: Z, 2: Z}, B_,
    "Colônia de levedura × bolor", "19; Trabulsi fig. 64.1.3", "prova", "AnKing só cita bolor/levedura por espécie; nenhuma descrição de colônia.",
    [1500243882463, 1499970409878], "Azuis: aspecto macroscópico do slide 19 (prática de micologia).",
    extra="- Telling them apart is the first step in culture identification", duplicacao_ok="ganho: reconhecimento macroscópico; os AnKing cobram forma por espécie"),
 au("glicogenio", "Like animals, fungi store glucose as {{c1::<b>glycogen</b>}} rather than starch", {1: V}, B_,
    "Reserva de glicogênio", "20–21; Trabulsi 64", "central", "AnKing só tem glicogênio humano; nada sobre reserva fúngica.",
    [1474253775264, 1468250158738], "Verde: traço que define o reino e o aproxima dos animais.",
    extra="- Plants store <b>starch</b>"),
 au("quitina", "Unlike plant (cellulose) and bacterial (peptidoglycan) walls, the fungal cell wall is built of {{c1::<b>chitin</b>}} and β-glucans", {1: V}, B_,
    "Parede de quitina e β-glucana", "20–23; prova 2018 P2 1.3", "prova", "AnKing cita parede só pelos antifúngicos; nenhum card de quitina.",
    [1509751969962, 1717015923409], "Verde: parede fungo × bactéria cobrada em 2018 e base das equinocandinas.",
    extra="- Outer layer rich in <b>mannoproteins</b><br>- Molds have more chitin than yeasts"),
 ak("eucarioto", 1500401344665, {1: Z}, B_, "Fungos são eucariotos", 21, "Azul: base; fungo × bactéria nas provas 2017/2018."),
 ak("ergosterol", 1468250158738, {1: V}, B_, "Ergosterol na membrana fúngica", 22, "Verde: HY (1); slides 22 e 26."),
 ak("dna-linear", 1716930573427, {1: Z, 2: Z}, B_, "Cromossomos lineares (eucarioto)", 22, "Azuis: 'núcleo com cromossomo linear' do slide 22.", origin="MCAT"),
 ak("ribossomo-80s", 1500406123742, {1: Z}, B_, "Ribossomo 80S", 22, "Azul: fungo × bactéria (80S × 70S) da prova 2017."),
 ak("capsula", 1525446605993, {1: V}, B_, "Cápsula polissacarídica do Cryptococcus", 22, "Verde: HY (1); cápsula do slide 22."),
 ak("capsula-fagocitose", 1500244482455, {1: V}, B_, "Cápsula antifagocitária", 22, "Verde: virulência da cápsula cobrada em 2024 P3 2.5."),
 au("alfa-glucana", "In dimorphic fungi, the <b>yeast</b> phase at 37 °C has more {{c1::<b>α-glucan</b>}} in its wall than the mold phase", {1: Z}, B_,
    "Parede da fase leveduriforme: α-glucana", "24; Trabulsi tab. 64.1.1; prova 2025 P3 1.2", "prova", "nenhum card de α-glucana no AnKing/MCAT.",
    [1509742036852, 1499970409878], "Azul: parede e dimorfismo cobrados em 2025 P3.",
    extra="- Mold phase (25 °C): more <b>β-glucan</b><br>- The switch helps the yeast evade host defenses"),
 # ---------- C. Antifúngicos (slide 27) ----------
 ak("equinocandina", 1509742036852, {1: V, 2: V}, C_, "Equinocandinas inibem a β-1,3-glucana sintase", 27, "Verdes: HY (1); slide 27."),
 ak("polienos", 1509742201770, {1: V, 2: V}, C_, "Polienos ligam ergosterol e abrem poros", 27, "Verdes: HY (1); slide 27."),
 ak("polienos-eletrolitos", 1509743161238, {1: V}, C_, "Polienos: vazamento de eletrólitos", 27, "Verde: HY (2); 'leakage of K+ and Na+' no slide 27."),
 ak("anfo-toxicidade", 1509743373899, {1: Z}, C_, "Anfotericina tóxica por ligar colesterol", 27, "Azul: 'mammalian toxicity' no slide 27."),
 ak("azois", 1509745062370, {1: V}, C_, "Azóis bloqueiam lanosterol → ergosterol", 27, "Verde: HY (1); slide 27."),
 ak("flucitosina-5fu", 1509742361304, {1: Z, 2: Z}, C_, "Flucitosina vira 5-FU na célula fúngica", 27, "Azuis: slide 27; HY menor."),
 ak("flucitosina-medula", 1509742681361, {1: V}, C_, "Flucitosina: mielossupressão", 27, "Verde: HY (1); 'myelosuppression' no slide 27."),
 # ---------- D. Taxonomia e reprodução (slides 30–46) ----------
 au("teleomorfo", "A fungus's sexual stage is its {{c1::<b>teleomorph</b>}} and its asexual stage is its {{c2::<b>anamorph</b>}}", {1: Z, 2: Z}, D_,
    "Teleomorfo × anamorfo", "30–31; Trabulsi 64.1", "central", "nenhum card AnKing/MCAT sobre teleomorfo/anamorfo.",
    [1499970409878, 1500243882463], "Azuis: estados do ciclo (slide 30) e nomes das fases (31).",
    extra="- Each stage may carry its own name; the sexual one takes priority<br>- Molecular techniques now drive classification"),
 au("brotamento", "Yeasts reproduce asexually mainly by {{c1::<b>budding</b>}}, pinching off a daughter cell", {1: V}, D_,
    "Brotamento", "37–38; prova 2017 P2 2.4", "prova", "AnKing só cita brotamento por espécie (Blastomyces, Cryptococcus), não o processo.",
    [1499972082394, 1500246246409], "Verde: reprodução da levedura, cobrada em 2017.",
    extra="- The bud is a <b>blastoconidium</b><br>- Some yeasts split equally by binary fission"),
 au("pseudohifa", "Yeast buds that fail to separate form chains called {{c1::<b>pseudohyphae</b>}}", {1: V}, D_,
    "Pseudo-hifa", "37 e 40", "central", "AnKing cobra pseudo-hifa só como achado da Candida (1557752615914), não como se forma.",
    [1557752615914, 1500234149130], "Verde: forma de invasão da Candida (slide 39).",
    extra="- Unlike true hyphae, they are pinched at each junction", duplicacao_ok="ganho: como a pseudo-hifa se forma; o AnKing cobra o achado da Candida"),
 ak("candida-pseudohifa", 1557752615914, {1: V}, D_, "Candida: pseudo-hifas ± leveduras brotando", 39, "Verde: 'pseudo-hifas na invasão por Candida' (slide 39)."),
 au("conidios", "<i>Aspergillus</i> and <i>Penicillium</i> spread by asexual spores borne externally on hyphae, called {{c1::<b>conidia</b>}}", {1: V}, D_,
    "Conídios", "42–43; Trabulsi 64.1", "central", "AnKing só tem conidióforo do Aspergillus e artroconídio do Coccidioides.",
    [1500238914091, 1500152894219], "Verde: principal propágulo assexuado e via de infecção.",
    extra="- Large multicelled <b>macroconidia</b>, small <b>microconidia</b><br>- Thick-walled resting cells: <b>chlamydoconidia</b>"),
 ak("aspergillus-conidioforo", 1500238914091, {1: V, 2: V}, D_, "Aspergillus forma conidióforos", 43, "Verdes: HY (1); vesícula e conidióforo do slide 43."),
 au("esporangio", "The black heads of bread mold (<i>Rhizopus</i>) are {{c1::<b>sporangia</b>}}, sacs full of asexual spores", {1: Z}, D_,
    "Esporângio (conídio interno)", "44; Trabulsi fig. 64.1.8", "central", "AnKing cita Rhizopus como mofo, não o esporângio.",
    [1500333766310, 1500334133616], "Azul: esporo interno × externo (slides 43–44).",
    extra="- Spores are released when the sporangium bursts"),
 ak("dimorfismo", 1499970409878, {1: V}, D_, "Dimórficos: bolor no solo, levedura no corpo", 45, "Verde: dimorfismo térmico central (slide 45; provas 2017, 2018)."),
 au("dimorfismo-temperatura", "Thermally dimorphic fungi grow as yeasts at {{c1::<b>35–37</b>}} °C and as molds at 25 °C", {1: V}, D_,
    "Temperaturas do dimorfismo", "45 e 58; prova 2018 P2 1.1", "prova", "AnKing dá o dimorfismo por espécie, sem as temperaturas.",
    [1499970409878, 1500234149130], "Verde: temperaturas cobradas em 2018 P2.",
    extra="- 'Mold in the cold, yeast in the heat'", duplicacao_ok="ganho: as temperaturas; o AnKing cobra solo × corpo"),
 ak("paracocci-dimorfico", 1499976133630, {1: Z}, D_, "Paracoccidioides é dimórfico", 45, "Azul: exemplo do slide 45."),
 au("sexuada", "Fungal sexual reproduction starts with fusion of cytoplasms, {{c1::<b>plasmogamy</b>}}, and later fusion of nuclei, {{c2::<b>karyogamy</b>}}", {1: Z, 2: Z}, D_,
    "Plasmogamia e cariogamia", "46; monitoria P2", "central", "nenhum card AnKing/MCAT de ciclo sexual fúngico.",
    [1509742361304, 1500333766310], "Azuis: sequência da reprodução sexuada do slide 46.",
    extra="- In between, cells carry two haploid nuclei (<b>dikaryon</b>, n+n)<br>- Meiosis then makes the sexual spores<br>- Aquatic fungi (chytrids) have flagellated gametes"),
 # ---------- E. Filos de interesse médico (slides 48–53) ----------
 au("septos", "Fungal hyphae without cross-walls, with many nuclei in one cytoplasm, are {{c1::<b>coenocytic</b>}}", {1: V}, E_,
    "Hifa cenocítica × septada", "44 e 48; Trabulsi fig. 64.1.5", "central", "AnKing só cobra 'non-septated' do Mucor.",
    [1500334133616, 1500238441939], "Verde: hifa septada × cenocítica separa os grandes grupos de bolores.",
    extra="- Most molds have <b>septate</b> hyphae<br>- A mass of hyphae is a <b>mycelium</b>"),
 ak("mucor-hifa", 1500334133616, {1: V, 2: V}, E_, "Mucor/Rhizopus: hifas não septadas", 48, "Verdes: HY (2); micélio cenocítico do antigo Zygomycota."),
 au("basidio", "In mushrooms (Basidiomycota), each sexual spore buds from the tip of a {{c1::<b>basidium</b>}}", {1: Z}, E_,
    "Basídio", "50; Trabulsi fig. 64.1.11", "central", "nenhum card de basídio no AnKing/MCAT.",
    [1500238914091, 1500333766310], "Azul: estrutura que define o filo (slide 50).",
    extra="- Basidia line the gills of the mushroom cap"),
 ak("amanitina", 1467833857831, {1: V, 2: V}, E_, "Amanita: α-amanitina inibe RNA polimerase II", 51, "Verdes: HY (2); Amanita venenosa do slide 51."),
 au("asco", "Which sac-like cell holds the sexual spores (usually eight) of Ascomycota?<br><br>{{c1::<b>Ascus</b>}}", {1: Z}, E_,
    "Asco", "52; Trabulsi fig. 64.1.12", "central", "nenhum card de asco no AnKing/MCAT.",
    [1500238914091, 1500333766310], "Azul: estrutura que define o filo (slide 52).",
    extra="- With Basidiomycota they form the Dikarya, home of most medically important fungi"),
 # ---------- F. Ecologia e nutrição (slides 55–61) ----------
 ak("aspergillus-inalacao", 1500239016754, {1: V}, F_, "Aspergillus transmitido por inalação", 55, "Verde: HY (2); ar como via de dispersão (slide 55)."),
 au("exoenzimas", "Fungi digest food <u>outside</u> the cell with secreted {{c1::<b>exoenzymes</b>}}, then absorb the small molecules", {1: V}, F_,
    "Nutrição por absorção", "56–57", "central", "nenhum card AnKing/MCAT de osmotrofia.",
    [1500152000410, 1509742036852], "Verde: modo de vida que define o reino.",
    extra="- No chlorophyll, so they are <b>heterotrophs</b><br>- Carbon from sugars (glucose); nitrogen from nitrate, ammonium or peptone"),
 ak("queratinase", 1500152000410, {1: Z, 2: Z}, F_, "Queratinase dos dermatófitos", 56, "Azuis: queratinases do slide 56; liga com a aula de micoses cutâneas."),
 au("mesofilos", "Most medically important fungi are {{c1::<b>mesophiles</b>}}, growing best at 20–30 °C", {1: Z}, F_,
    "Mesófilos", "58; prova 2018 P2 1.4", "prova", "nenhum card de temperatura de crescimento fúngico.",
    [1500054938635, 1500234149130], "Azul: fatores ambientais cobrados em 2018.",
    extra="- Best pH about 6.5 (yeasts 2.5–8.5, molds 1.5–11)"),
 au("atividade-agua", "Fungi stop growing when the water activity of their substrate falls to about {{c1::<b>0.65</b>}}", {1: Z}, F_,
    "Atividade de água mínima", "59; prova 2018 P2 1.4", "prova", "nenhum card de atividade de água.",
    [1500054938635, 1517779158524], "Azul: umidade como fator ambiental cobrado em 2018.",
    extra="- Dry storage prevents mold in grains and buildings"),
]

NOTAS = {
 "aflatoxina-chc": "A mycotoxin: a toxic fungal metabolite in food, not an infection",
 "eucarioto": "Nucleus, mitochondria and 80S ribosomes, unlike bacteria",
 "ergosterol": "Takes the place of cholesterol, so it is the main antifungal target",
 "dna-linear": "Fungi, as eukaryotes, have linear chromosomes inside a nucleus",
 "ribossomo-80s": "Bacteria have 70S, which is why antibacterials spare fungi",
 "capsula": "The capsule is the target of India ink staining",
 "equinocandina": "No β-glucan, weak wall, osmotic lysis",
 "anfo-toxicidade": "Explains its kidney toxicity",
 "azois": "Less ergosterol, leaky membrane, growth stops",
 "flucitosina-5fu": "5-FU then blocks DNA and RNA synthesis",
 "flucitosina-medula": "5-FU also hits rapidly dividing marrow cells",
 "candida-pseudohifa": "Pseudohyphae help Candida invade tissue",
 "aspergillus-conidioforo": "Conidia radiate from a swollen vesicle on top of the conidiophore",
 "paracocci-dimorfico": "The Brazilian endemic mycosis (paracoccidioidomycosis)",
 "mucor-hifa": "Formerly Zygomycota, now Mucoromycota; sexual spore is the zygospore",
 "amanitina": "Death cap mushrooms cause liver failure by blocking mRNA synthesis",
 "aspergillus-inalacao": "Air is the main dispersal route for fungal spores; indoor mold overgrowth also causes sick building syndrome",
}

IMAGENS = {
 "colonias": "nebli-trabulsi-fig-64-1-3.png",
 "brotamento": "nebli-trabulsi-fig-64-1-4.png",
 "pseudohifa": "nebli-mb43-brotamento-completo.png",
 "septos": "nebli-trabulsi-fig-64-1-5.png",
 "esporangio": "nebli-trabulsi-fig-64-1-8.png",
 "basidio": "nebli-mb43-basidio.png",
 "asco": "nebli-trabulsi-fig-64-1-12.png",
}
for nome in set(IMAGENS.values()):
    MEDIA[nome] = f"img/{nome}"
for c in CARDS:
    if c["key"] in NOTAS:
        c["extra_add"] = f"- {NOTAS[c['key']]}"
    if c["key"] in IMAGENS:
        img = f'<img src="{IMAGENS[c["key"]]}" style="max-width:100%;max-height:52vh">'
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br><br>" if c["extra"] else "") + img
        else:
            c["extra_add"] = (c.get("extra_add", "") + "<br><br>" if c.get("extra_add") else "") + img
