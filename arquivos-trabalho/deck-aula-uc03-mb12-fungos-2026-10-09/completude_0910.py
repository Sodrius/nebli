"""F-20261009-CLAUDE-02 ("a aula de fungo fugiu do que era para ser... tá faltando coisa que teve e tem coisa que não foi dada"):
refaz o spec contra o material de base (61 lâminas do Taborda; apostila de veteranos aula 8; monitoria P2 aula 9; Benedito; provas
2017/2018/2024/2025; Trabulsi 64). Roda uma vez sobre spec-antes-completude.py e grava spec.py.

Sai: aflatoxina → carcinoma hepático e α-amanitina → RNA pol II (não dados na aula). Ganha card próprio cada ideia que antes só
aparecia no verso de outro card (menção no verso não é cobertura)."""
import re
from pathlib import Path

HERE = Path(__file__).parent
s = (HERE / "spec-antes-completude.py").read_text()
E1, E2, E3 = 1500401344665, 1500243882463, 1499970409878  # espelhos AnKing de micologia básica (eucarioto, Aspergillus só bolor, dimorfismo)


def rep(old, new):
    global s
    assert old in s, old[:70]
    s = s.replace(old, new)


def drop(key):
    global s
    i = s.index(f' ak("{key}"')
    j = s.index("\n", s.index('"),', i))
    s = s[:i] + s[j + 1:]


def after(key, block):
    global s
    i = s.index(f'("{key}"')
    m = re.compile(r"\n ?(ak|au|sh)\(|\n # |\n\]").search(s, i + 10)
    s = s[:m.start()] + "\n" + block.strip("\n") + s[m.start():]


def A(key, text, flags, bloco, alvo, slide, autoria, falta, motivo, extra="", esp=(E1, E2), dup=""):
    fl = "{" + ", ".join(f"{k}: {v}" for k, v in flags.items()) + "}"
    return (f' au("{key}", {text!r}, {fl}, {bloco}, {alvo!r}, {slide!r}, {autoria!r}, {falta!r}, [{esp[0]}, {esp[1]}], {motivo!r}'
            + (f", extra={extra!r}" if extra else "") + (f", duplicacao_ok={dup!r}" if dup else "") + "),")


V, Z, R = "V", "Z", "R"
s = s.replace("Critérios até F-20261009-CLAUDE-01.", "Critérios até F-20261009-CLAUDE-02 (completude e fidelidade, refeito em 09/10 à tarde).")

# ---- deriva: sai o que a aula não deu ----
drop("aflatoxina-chc")
drop("amanitina")
s = s.replace(' "aflatoxina-chc": "A mycotoxin: a toxic fungal metabolite in food, not an infection",\n', "")
s = s.replace(' "amanitina": "Death cap mushrooms cause liver failure by blocking mRNA synthesis",\n', "")
rep('ak("aflatoxina-graos", 1517779158524, {1: V}, A_, "Aflatoxina em grãos e nozes mal armazenados", 10, "Verde: HY (2); grãos contaminados do slide 10."),',
    'ak("aflatoxina-graos", 1517779158524, {1: V}, A_, "Aflatoxina em grãos e nozes mal armazenados", 10, "Verde: HY (2); grãos contaminados do slide 10.", extra_add="- A mycotoxin: a toxic fungal metabolite in food, not an infection"),')

# ---- cards existentes que passam a cobrar o par que a aula dá ----
rep('"Most fungi live as {{c1::<b>saprobes</b>}}, decomposing dead organic matter in soil and food"',
    '"Fungi that feed on dead organic matter are {{c1::<b>saprobes</b>}}, while those that feed on living hosts are {{c2::<b>parasites</b>}}"')
rep('"Sapróbios decompositores", "7; Trabulsi 64.2; prova 2015 P2 29.3"', '"Sapróbios × parasitas", "7; apostila veteranos aula 8; Trabulsi 64.2; prova 2015 P2 29.3"')
rep('{1: Z}, A_,\n    "Sapróbios × parasitas"', '{1: Z, 2: Z}, A_,\n    "Sapróbios × parasitas"')
rep('extra="- Others live as <b>parasites</b> or <b>mutualists</b>: mycorrhizae (plant roots), lichens (algae)"),',
    'extra="- Saprobes are the main decomposers that recycle nutrients"),')
rep('"Yeasts reproduce asexually mainly by {{c1::<b>budding</b>}}, pinching off a daughter cell"',
    '"Yeasts reproduce asexually mainly by {{c1::<b>budding</b>}}, which gives unequal cells, whereas {{c2::<b>binary fission</b>}} gives two equal cells"')
rep('{1: V}, D_,\n    "Brotamento"', '{1: V, 2: Z}, D_,\n    "Brotamento × cissiparidade"')
rep('extra="- The bud is a <b>blastoconidium</b><br>- Some yeasts split equally by binary fission"),', 'extra="- The bud is a <b>blastoconidium</b>"),')
rep('"Fungal sexual reproduction starts with fusion of cytoplasms, {{c1::<b>plasmogamy</b>}}, and later fusion of nuclei, {{c2::<b>karyogamy</b>}}"',
    '"In fungal sexual reproduction, {{c1::<b>plasmogamy</b>}} (fusion of cytoplasms) comes first, then {{c2::<b>karyogamy</b>}} (fusion of nuclei) and {{c3::<b>meiosis</b>}}"')
rep('{1: Z, 2: Z}, D_,\n    "Plasmogamia e cariogamia"', '{1: Z, 2: Z, 3: Z}, D_,\n    "Plasmogamia, cariogamia, meiose"')
rep('extra="- In between, cells carry two haploid nuclei (<b>dikaryon</b>, n+n)<br>- Meiosis then makes the sexual spores<br>- Aquatic fungi (chytrids) have flagellated gametes"),',
    'extra="- Spores made by meiosis count as sexual: they carry new gene combinations"),')
# versos que listavam alvos da aula: o alvo ganha card próprio, o verso fica com o porquê
rep('extra="- Kept in kingdom Plantae until Whittaker (1969)<br>- Slime molds were moved out to Protista"),', 'extra="- Woese\'s DNA-based tree (1994) placed fungi beside animals"),')
rep('extra="- Outer layer rich in <b>mannoproteins</b><br>- Molds have more chitin than yeasts"),', 'extra="- Outer layer rich in <b>mannoproteins</b>"),')
rep('extra="- Large multicelled <b>macroconidia</b>, small <b>microconidia</b><br>- Thick-walled resting cells: <b>chlamydoconidia</b>"),', 'extra="- Asexual spores are made by mitosis"),')
rep('extra="- Most molds have <b>septate</b> hyphae<br>- A mass of hyphae is a <b>mycelium</b>"),', 'extra="- Most molds have <b>septate</b> hyphae"),')
rep('extra="- With Basidiomycota they form the Dikarya, home of most medically important fungi"),', 'extra="- Ascospores form inside the ascus: internal sexual spores"),')
rep('extra="- No chlorophyll, so they are <b>heterotrophs</b><br>- Carbon from sugars (glucose); nitrogen from nitrate, ammonium or peptone"),', 'extra="- Lipases, proteinases and keratinases break down macromolecules"),')
rep('extra="- Best pH about 6.5 (yeasts 2.5–8.5, molds 1.5–11)"),', 'extra="- Psychrophiles grow in the cold, thermophiles in heat"),')
rep(' "aspergillus-inalacao": "Air is the main dispersal route for fungal spores; indoor mold overgrowth also causes sick building syndrome",\n',
    ' "aspergillus-inalacao": "Conidia are small enough to reach the alveoli",\n')

rep('extra="- Fungi also give us cheeses and antibiotics (<b>penicillin</b> from <i>Penicillium</i>)"),', 'extra="- Fungi are also eaten (mushrooms) and ripen cheeses"),')
rep('extra="- Each stage may carry its own name; the sexual one takes priority<br>- Molecular techniques now drive classification"),', 'extra="- Many medical fungi are known only by their anamorph"),')
B = "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): "
# ---- A. Fungos, vida humana e natureza ----
after("fermentacao", A("penicilina", "The first antibiotic, penicillin, was obtained from the mold {{c1::<i><b>Penicillium</b></i>}}", {1: Z}, "A_",
    "Antibióticos naturais (penicilina)", "5; Benedito p. 4", "central", B + "'penicillin Penicillium' sem card.",
    "Azul: 'antibióticos naturais' do slide 5.", extra="- Cephalosporins and griseofulvin also come from fungi"))
after("saprofita", A("micorriza", "{{c1::<b>Mycorrhizae</b>}} are mutualistic associations between fungi and plant roots", {1: Z}, "A_",
    "Micorrizas", "7", "central", B + "'mycorrhiz*' sem card.", "Azul: 'associação com a raiz da planta – micorrizas' do slide 7.",
    extra="- The fungus extends the root's reach for water and minerals"))
after("micorriza", A("edificios", "In {{c1::<b>sick building</b>}} syndrome, indoor fungi cause fatigue, headache and airway irritation in more than 20% of occupants", {1: R}, "A_",
    "Síndrome dos edifícios doentes", "8", "lateral", B + "'sick building' sem card.", "Rosa: lâmina 8 inteira sobre o tema; detalhe ambiental.",
    extra="- Damp, poorly ventilated buildings favor mold"))
after("rhizopus-pao", A("micotoxicose", "Eating food with fungal toxins causes {{c1::<b>mycotoxicosis</b>}}, whereas eating a poisonous mushroom (e.g., <i>Amanita</i>) causes {{c2::<b>mycetism</b>}}", {1: Z, 2: Z}, "A_",
    "Micotoxicose × micetismo", "10 e 51; Benedito p. 5", "central", B + "'mycotoxi*', 'mycetism' sem card; AnKing tem só aflatoxina.",
    "Azuis: micotoxinas (slide 10) e Amanita venenosa (slide 51), separadas por Benedito.", extra="- Neither is an infection: the harm comes from the toxin", esp=(1517779158524, E1)))
after("aflatoxina-graos", A("quitridio", "{{c1::<b>Chytrids</b>}} (Chytridiomycota) are aquatic fungi whose spores swim with a flagellum", {1: Z}, "A_",
    "Quitrídios: aquáticos, esporos flagelados", "14 e 46; Benedito p. 9", "central", B + "'chytrid*' sem card.",
    "Azul: quitrídio do slide 14 e gametas flagelados de fungos aquáticos (slide 46).", extra="- A chytrid is wiping out amphibians worldwide"))
# ---- B. Características ----
after("melanina", A("whittaker", "Fungi were classified as {{c1::<b>plants</b>}} until Whittaker gave them their own kingdom in 1969", {1: Z}, "B_",
    "Whittaker 1969: reino Fungi", "17–18; apostila veteranos aula 8", "central", B + "'Whittaker', 'five kingdom*' sem card.",
    "Azul: abertura da apostila e slides 17–18.", extra="- Five kingdoms: Monera, Protista, Fungi, Plantae, Animalia"))
after("colonias", A("heterotrofo", "Fungi lack chlorophyll, so they are {{c1::<b>heterotrophs</b>}} that need preformed organic matter", {1: V}, "B_",
    "Sem clorofila: heterotróficos", "20–21; apostila veteranos aula 8; monitoria P2", "central", B + "'fung* heterotroph*', 'chlorophyll' sem card.",
    "Verde: primeira diferença em relação às plantas (slide 20) e base do modo de vida.", extra="- They live as saprobes, parasites or mutualists"))
after("eucarioto", A("imoveis", "Fungal cells are {{c1::<b>nonmotile</b>}}, unlike many bacteria", {1: Z}, "B_",
    "Imóveis", "21; Benedito p. 44; prova 2017 P2 2.5", "prova", B + "'fung* motil*' sem card.",
    "Azul: 'imóveis' do slide 21; motilidade na tabela fungo × bactéria.", extra="- Exception: flagellated spores of aquatic chytrids"))
after("imoveis", A("sem-tecido", "Even multicellular fungi never organize into true {{c1::<b>tissues</b>}}", {1: Z}, "B_",
    "Não formam tecido verdadeiro", "21; apostila veteranos aula 8; Benedito p. 7", "central", B + "'fung* tissue*' só traz micoses.",
    "Azul: 'não formam tecido verdadeiro' do slide 21 e da apostila.", extra="- Molds are filaments of cells (hyphae), not organs"))
after("sem-tecido", A("lisina", "Fungi make lysine by the {{c1::<b>α-aminoadipate</b>}} pathway", {1: R}, "B_",
    "Lisina pela via do aminoadipato", "21", "lateral", B + "'lysine aminoadip*' sem card.",
    "Rosa: traço bioquímico próprio listado no slide 21.", extra="- Bacteria and plants use the diaminopimelate pathway"))
after("lisina", A("cristas", "Fungal mitochondria have {{c1::<b>flattened</b>}} (plate-like) cristae", {1: R}, "B_",
    "Cristas mitocondriais achatadas", "21", "lateral", B + "sem card de cristas fúngicas.", "Rosa: último traço do slide 21.",
    extra="- Another trait shared with animals"))
after("cristas", A("tamanho", "Fungal cells (about 3–10 µm) are {{c1::<b>larger</b>}} than bacteria (1–5 µm)", {1: Z}, "B_",
    "Tamanho: fungo maior que bactéria", "21; Benedito p. 44; prova 2017 P2 2.5", "prova", B + "sem card de tamanho fúngico.",
    "Azul: tabela fungo × bactéria cobrada em 2017.", extra="- Viruses: 0.02–0.2 µm"))
after("quitina", A("quitina-levedura", "Yeast cell walls contain {{c1::<b>less</b>}} chitin than mold walls", {1: Z}, "B_",
    "Leveduras têm menos quitina que bolores", "22–24; apostila veteranos aula 8; monitoria P2", "central", B + "nenhum card de quitina.",
    "Azul: ênfase da apostila e da monitoria.", extra="- Wall: glucans, chitin and mannans in all fungi"))
# ---- D. Taxonomia e reprodução ----
after("teleomorfo", A("nome-sexuado", "Once a fungus's sexual stage is found, its {{c1::<b>sexual</b>}} (teleomorph) name takes priority", {1: R}, "D_",
    "Prioridade do nome da fase sexuada", "31", "lateral", B + "'teleomorph OR anamorph' sem card.",
    "Rosa: regra de nomenclatura do slide 31.", extra="- Medical fungi often keep their familiar asexual names"))
after("nome-sexuado", A("molecular", "Because morphology is unreliable, fungi are now classified mainly by {{c1::<b>molecular</b>}} (DNA) methods", {1: Z}, "D_",
    "Classificação molecular", "31; apostila veteranos aula 8", "central", B + "sem card de taxonomia fúngica.",
    "Azul: 'técnicas moleculares são essenciais' (slide 31) e apostila.", extra="- About 100,000 species described of an estimated 5 million"))
after("molecular", A("mixomicetos", "Slime molds (Myxomycota), once grouped with fungi, are now classified as {{c1::<b>protists</b>}}", {1: R}, "D_",
    "Fungos do lodo agora em Protista", "33", "lateral", B + "'slime mold*' sem card.", "Rosa: reclassificação do slide 33.",
    extra="- True fungi = Eumycota"))
after("mixomicetos", A("filos-medicos", "Most fungi of medical interest belong to {{c1::<b>Ascomycota</b>}} and {{c2::<b>Basidiomycota</b>}}", {1: V, 2: V}, "D_",
    "Asco e Basidio: maioria dos fungos médicos", "34–35; monitoria P2", "central", B + "'Ascomycota OR Basidiomycota' sem card.",
    "Verdes: destaque circulado do slide 35.", extra="- Together they form the subkingdom <b>Dikarya</b>"))
after("filos-medicos", A("mucoromycota", "<i>Mucor</i>, <i>Rhizopus</i> and <i>Lichtheimia</i> now belong to the phylum {{c1::<b>Mucoromycota</b>}}", {1: Z}, "D_",
    "Mucoromycota", "35 e 48", "central", B + "'Mucorales OR zygomycete*' sem card.",
    "Azul: gêneros anotados no slide 35; antigo Zygomycota (48).", extra="- Formerly Zygomycota", esp=(1500334133616, 1500333766310)))
after("brotamento", A("clamidoconidio", "Thick-walled resting spores formed from hyphal or yeast cells are {{c1::<b>chlamydoconidia</b>}}", {1: Z}, "D_",
    "Clamidoconídio", "37; Trabulsi 64.1", "central", B + "'chlamydo*' só traz Chlamydia.",
    "Azul: rótulo do slide 37; estrutura de resistência no Trabulsi.", extra="- <i>Candida albicans</i> forms them"))
after("candida-pseudohifa", A("micelio", "A mass of branching hyphae is called a {{c1::<b>mycelium</b>}}", {1: V}, "D_",
    "Hifas formam o micélio", "42–44; apostila veteranos aula 8; monitoria P2", "central", B + "'mycelium' só no Extra de Aspergillus.",
    "Verde: estrutura somática dos bolores (apostila e Benedito).", extra="- Hyphae are the tubular filaments that make up molds"))
after("micelio", A("micelio-vegetativo", "The {{c1::<b>vegetative</b>}} mycelium grows into the substrate to absorb nutrients, whereas the {{c2::<b>aerial</b>}} mycelium bears the spores", {1: V, 2: V}, "D_",
    "Micélio vegetativo × aéreo (reprodutivo)", "44; apostila veteranos aula 8; monitoria P2; Benedito p. 14", "central", B + "'aerial hypha*' sem card.",
    "Verdes: 'hifa vegetativa' do slide 44 e a divisão da apostila.", extra="- Reproductive structures are the basis of mold identification"))
after("micelio-vegetativo", A("crescimento-apical", "Hyphae grow by elongating at their {{c1::<b>tips</b>}}, and a hyphal fragment can start a new colony", {1: R}, "D_",
    "Crescimento apical e fragmentação", "42; monitoria P2", "lateral", B + "sem card de crescimento de hifa.", "Rosa: detalhe da monitoria.", extra="- Fragmentation is a simple form of asexual reproduction"))
after("conidios", A("macro-microconidio", "Molds may bear large multicelled {{c1::<b>macroconidia</b>}} and small single-celled {{c2::<b>microconidia</b>}}", {1: Z, 2: Z}, "D_",
    "Macro e microconídios", "43; prova 2025 P3 1.1", "prova", B + "'macroconid* OR microconid*' sem card.",
    "Azuis: rótulos do slide 43; microconídios inalados na prova 2025.", extra="- Inhaled microconidia transmit <i>Histoplasma</i>", esp=(1500238914091, E3)))
after("paracocci-dimorfico", A("pleomorfismo", "Changes in fungal form that do <u>not</u> depend on temperature are called {{c1::<b>pleomorphism</b>}}", {1: Z}, "D_",
    "Pleomorfismo × dimorfismo", "45; monitoria P2; Benedito p. 27", "central", B + "sem card de pleomorfismo.",
    "Azul: contraste com dimorfismo térmico da monitoria.", extra="- Thermal dimorphism depends on temperature (and CO₂) and is reversible", esp=(E3, 1499976133630)))
after("sexuada", A("dicario", "After plasmogamy, the two parental nuclei may stay apart in a {{c1::<b>dikaryotic</b>}} (n + n) phase", {1: Z}, "D_",
    "Fase dicariótica", "46; Benedito p. 8", "central", B + "'dikaryo*' sem card.",
    "Azul: 'fase heterocariótica, n + n' do slide 46.", extra="- Long-lasting in Ascomycota and Basidiomycota (Dikarya)"))
# ---- E. Filos ----
after("mucor-hifa", A("zigosporo", "The sexual spore of <i>Mucor</i> and <i>Rhizopus</i> (former Zygomycota) is the {{c1::<b>zygospore</b>}}", {1: Z}, "E_",
    "Zigósporo", "48; monitoria P2; Benedito p. 9", "central", B + "'zygospore*' sem card.",
    "Azul: reprodução sexuada do antigo Zygomycota (slide 48).", extra="- Their asexual spores are sporangiospores", esp=(1500334133616, 1500333766310)))
# ---- F. Ecologia e nutrição ----
s = s.replace(' ak("aspergillus-inalacao"', A("anemofilos", "Fungal spores spread mostly through the {{c1::<b>air</b>}}, and inhaled spores cause respiratory allergies", {1: Z}, "F_",
    "Dispersão pelo ar; anemófilos e alergias", "55; Benedito pp. 29–33; Trabulsi 64.2", "central", B + "'fung* allerg* spore*' sem card.",
    "Azul: vias de dispersão (slide 55) e fungos anemófilos do Benedito.", extra="- Also by water, soil, animals and insects") + "\n" + ' ak("aspergillus-inalacao"', 1)
after("queratinase", A("nutrientes", "Fungi need organic carbon such as {{c1::<b>glucose</b>}}, but can take nitrogen from nitrate or ammonium", {1: R}, "F_",
    "Nutrientes: carbono orgânico, nitrogênio inorgânico", "57; apostila veteranos aula 8", "lateral", B + "sem card de nutrição fúngica.",
    "Rosa: fontes do slide 57.", extra="- Trace metals and vitamins are needed in tiny amounts"))
after("mesofilos", A("aerobios", "Most fungi are obligate {{c1::<b>aerobes</b>}}, although fermenting yeasts are facultative anaerobes", {1: Z}, "F_",
    "Aeróbios obrigatórios", "58; apostila veteranos aula 8; monitoria P2; Benedito p. 38", "central", B + "'fung* aerob*' sem card.",
    "Azul: aeração como fator de crescimento (apostila).", extra="- Sexual reproduction needs an oxygen-rich atmosphere"))
after("aerobios", A("luz", "Fungi grow vegetatively in the dark but need {{c1::<b>light</b>}} to form reproductive structures", {1: Z}, "F_",
    "Luz: reprodução", "58; apostila veteranos aula 8; monitoria P2", "central", B + "sem card de luz e fungos.",
    "Azul: fator ambiental da apostila e da monitoria.", extra="- Direct sunlight kills fungi (UV)"))
after("atividade-agua", A("ph", "Most fungi grow best at a pH of about {{c1::<b>6.5</b>}}, but tolerate a wide range", {1: Z}, "F_",
    "pH ótimo ~6,5", "60; prova 2018 P2 1.4", "prova", B + "'fung* pH' sem card.",
    "Azul: pH no slide 60 e na prova 2018.", extra="- 6.5 is the value on the slide and in the 2018 exam key (the veteran guide says 5.6)<br>- Yeasts tolerate pH 2.5–8.5; molds 1.5–11"))
after("ph", A("liquen", "A {{c1::<b>lichen</b>}} is a mutualism between a fungus and an alga or cyanobacterium", {1: Z}, "F_",
    "Liquens", "61; Benedito p. 34", "central", B + "'lichen*' só traz líquen escleroso.",
    "Azul: lâmina final.", extra="- Fungus (mycobiont) protects; alga (photobiont) photosynthesizes<br>- 98% of lichen fungi are ascomycetes"))

(HERE / "spec.py").write_text(s)
print("ok")
