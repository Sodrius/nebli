# Especificação curada — Biologia geral dos fungos (UC03 P3, Microbiologia, aula 43; Prof. Carlos Pelleschi Taborda; 61 lâminas).
# Reconstrução pelo Claude em 09/10/2026 (plano de 08/10: substituir a versão Codex de 03–04/10, 66 cards nunca estudados).
# Feita a partir de inventario-aula.json/planejamento.json (escritos antes). Ordem = slides. Critérios até F-20261009-CLAUDE-02 (completude e fidelidade, refeito em 09/10 à tarde).
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
    extra="- Fungi are also eaten (mushrooms) and ripen cheeses"),
 au("penicilina", 'The first antibiotic, penicillin, was obtained from the mold {{c1::<i><b>Penicillium</b></i>}}', {1: Z}, A_, 'Antibióticos naturais (penicilina)', '5; Benedito p. 4', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'penicillin Penicillium' sem card.", [1500401344665, 1500243882463], "Azul: 'antibióticos naturais' do slide 5.", extra='- Cephalosporins and griseofulvin also come from fungi'),
 au("saprofita", "Fungi that feed on dead organic matter are {{c1::<b>saprobes</b>}}, while those that feed on living hosts are {{c2::<b>parasites</b>}}", {1: Z, 2: Z}, A_,
    "Sapróbios × parasitas", "7; apostila veteranos aula 8; Trabulsi 64.2; prova 2015 P2 29.3", "prova", "nenhum card AnKing/MCAT define sapróbio (busca 'saprophyt*', 'decompos*').",
    [1500243882463, 1500401344665], "Azul: 'características do fungo em saprofitismo' (prova 2015).",
    extra="- Saprobes are the main decomposers that recycle nutrients"),
 au("micorriza", '{{c1::<b>Mycorrhizae</b>}} are mutualistic associations between fungi and plant roots', {1: Z}, A_, 'Micorrizas', '7', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'mycorrhiz*' sem card.", [1500401344665, 1500243882463], "Azul: 'associação com a raiz da planta – micorrizas' do slide 7.", extra="- The fungus extends the root's reach for water and minerals"),
 au("edificios", 'In {{c1::<b>sick building</b>}} syndrome, indoor fungi cause fatigue, headache and airway irritation in more than 20% of occupants', {1: R}, A_, 'Síndrome dos edifícios doentes', '8', 'lateral', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'sick building' sem card.", [1500401344665, 1500243882463], 'Rosa: lâmina 8 inteira sobre o tema; detalhe ambiental.', extra='- Damp, poorly ventilated buildings favor mold'),
 ak("rhizopus-pao", 1500333766310, {1: V, 2: V}, A_, "Rhizopus, mofo do pão", 9, "Verde: HY (1); mofo do pão do slide 9 e Benedito p. 41."),
 au("micotoxicose", 'Eating food with fungal toxins causes {{c1::<b>mycotoxicosis</b>}}, whereas eating a poisonous mushroom (e.g., <i>Amanita</i>) causes {{c2::<b>mycetism</b>}}', {1: Z, 2: Z}, A_, 'Micotoxicose × micetismo', '10 e 51; Benedito p. 5', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'mycotoxi*', 'mycetism' sem card; AnKing tem só aflatoxina.", [1517779158524, 1500401344665], 'Azuis: micotoxinas (slide 10) e Amanita venenosa (slide 51), separadas por Benedito.', extra='- Neither is an infection: the harm comes from the toxin'),
 ak("aflatoxina-graos", 1517779158524, {1: Z}, A_, "Aflatoxina em grãos e nozes mal armazenados", 10, "Verde: HY (2); grãos contaminados do slide 10. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", extra_add="- A mycotoxin: a toxic fungal metabolite in food, not an infection", clinica_lateral=True),
 au("quitridio", '{{c1::<b>Chytrids</b>}} (Chytridiomycota) are aquatic fungi whose spores swim with a flagellum', {1: Z}, A_, 'Quitrídios: aquáticos, esporos flagelados', '14 e 46; Benedito p. 9', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'chytrid*' sem card.", [1500401344665, 1500243882463], 'Azul: quitrídio do slide 14 e gametas flagelados de fungos aquáticos (slide 46).', extra='- A chytrid is wiping out amphibians worldwide'),
 au("melanina", "{{c1::<b>Melanin</b>}} deposited in the fungal cell wall protects the fungus against ionizing radiation", {1: R}, A_,
    "Melanina na parede: proteção (Chernobyl)", "16 e 22", "lateral", "sem card de melanina fúngica no AnKing/MCAT (busca 'melanin fung*').",
    [1500244482455, 1468250158738], "Rosa: experimento de Chernobyl; liga com 'parede: proteção, melanina' do slide 22.",
    extra="- Melanized fungi even grew faster under radiation"),
 au("whittaker", 'Fungi were classified as {{c1::<b>plants</b>}} until Whittaker gave them their own kingdom in 1969', {1: Z}, B_, 'Whittaker 1969: reino Fungi', '17–18; apostila veteranos aula 8', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'Whittaker', 'five kingdom*' sem card.", [1500401344665, 1500243882463], 'Azul: abertura da apostila e slides 17–18.', extra='- Five kingdoms: Monera, Protista, Fungi, Plantae, Animalia'),
 # ---------- B. Características e célula fúngica (slides 17–26) ----------
 au("animais", "Genetic analysis shows that fungi are more closely related to {{c1::<b>animals</b>}} than to plants", {1: Z}, B_,
    "Fungos mais próximos de animais", "18; Prof. Dave (taxonomia); Strong Medicine", "central", "nenhum card AnKing/MCAT sobre a posição filogenética dos fungos.",
    [1500401344665, 1716930573427], "Azul: árvore do slide 18; explica por que antifúngicos são tóxicos.",
    extra="- Woese's DNA-based tree (1994) placed fungi beside animals"),
 au("colonias", "{{c1::<b>Yeasts</b>}} form creamy, pasty colonies, whereas {{c2::<b>molds</b>}} form cottony, velvety or powdery ones", {1: Z, 2: Z}, B_,
    "Colônia de levedura × bolor", "19; Trabulsi fig. 64.1.3", "prova", "AnKing só cita bolor/levedura por espécie; nenhuma descrição de colônia.",
    [1500243882463, 1499970409878], "Azuis: aspecto macroscópico do slide 19 (prática de micologia).",
    extra="- Telling them apart is the first step in culture identification", duplicacao_ok="ganho: reconhecimento macroscópico; os AnKing cobram forma por espécie"),
 au("heterotrofo", 'Fungi lack chlorophyll, so they are {{c1::<b>heterotrophs</b>}} that need preformed organic matter', {1: V}, B_, 'Sem clorofila: heterotróficos', '20–21; apostila veteranos aula 8; monitoria P2', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'fung* heterotroph*', 'chlorophyll' sem card.", [1500401344665, 1500243882463], 'Verde: primeira diferença em relação às plantas (slide 20) e base do modo de vida.', extra='- They live as saprobes, parasites or mutualists'),
 au("glicogenio", "Like animals, fungi store glucose as {{c1::<b>glycogen</b>}} rather than starch", {1: V}, B_,
    "Reserva de glicogênio", "20–21; Trabulsi 64", "central", "AnKing só tem glicogênio humano; nada sobre reserva fúngica.",
    [1474253775264, 1468250158738], "Verde: traço que define o reino e o aproxima dos animais.",
    extra="- Plants store <b>starch</b>"),
 au("quitina", "Unlike plant (cellulose) and bacterial (peptidoglycan) walls, the fungal cell wall is built of {{c1::<b>chitin</b>}} and β-glucans", {1: V}, B_,
    "Parede de quitina e β-glucana", "20–23; prova 2018 P2 1.3", "prova", "AnKing cita parede só pelos antifúngicos; nenhum card de quitina.",
    [1509751969962, 1717015923409], "Verde: parede fungo × bactéria cobrada em 2018 e base das equinocandinas.",
    extra="- Outer layer rich in <b>mannoproteins</b>"),
 au("quitina-levedura", 'Yeast cell walls contain {{c1::<b>less</b>}} chitin than mold walls', {1: Z}, B_, 'Leveduras têm menos quitina que bolores', '22–24; apostila veteranos aula 8; monitoria P2', 'central', 'busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): nenhum card de quitina.', [1500401344665, 1500243882463], 'Azul: ênfase da apostila e da monitoria.', extra='- Wall: glucans, chitin and mannans in all fungi'),
 ak("eucarioto", 1500401344665, {1: Z}, B_, "Fungos são eucariotos", 21, "Azul: base; fungo × bactéria nas provas 2017/2018."),
 au("imoveis", 'Fungal cells are {{c1::<b>nonmotile</b>}}, unlike many bacteria', {1: Z}, B_, 'Imóveis', '21; Benedito p. 44; prova 2017 P2 2.5', 'prova', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'fung* motil*' sem card.", [1500401344665, 1500243882463], "Azul: 'imóveis' do slide 21; motilidade na tabela fungo × bactéria.", extra='- Exception: flagellated spores of aquatic chytrids'),
 au("sem-tecido", 'Even multicellular fungi never organize into true {{c1::<b>tissues</b>}}', {1: Z}, B_, 'Não formam tecido verdadeiro', '21; apostila veteranos aula 8; Benedito p. 7', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'fung* tissue*' só traz micoses.", [1500401344665, 1500243882463], "Azul: 'não formam tecido verdadeiro' do slide 21 e da apostila.", extra='- Molds are filaments of cells (hyphae), not organs'),
 au("lisina", 'Fungi make lysine by the {{c1::<b>α-aminoadipate</b>}} pathway', {1: R}, B_, 'Lisina pela via do aminoadipato', '21', 'lateral', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'lysine aminoadip*' sem card.", [1500401344665, 1500243882463], 'Rosa: traço bioquímico próprio listado no slide 21.', extra='- Bacteria and plants use the diaminopimelate pathway'),
 au("cristas", 'Fungal mitochondria have {{c1::<b>flattened</b>}} (plate-like) cristae', {1: R}, B_, 'Cristas mitocondriais achatadas', '21', 'lateral', 'busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): sem card de cristas fúngicas.', [1500401344665, 1500243882463], 'Rosa: último traço do slide 21.', extra='- Another trait shared with animals'),
 au("tamanho", 'Fungal cells (about 3–10 µm) are {{c1::<b>larger</b>}} than bacteria (1–5 µm)', {1: Z}, B_, 'Tamanho: fungo maior que bactéria', '21; Benedito p. 44; prova 2017 P2 2.5', 'prova', 'busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): sem card de tamanho fúngico.', [1500401344665, 1500243882463], 'Azul: tabela fungo × bactéria cobrada em 2017.', extra='- Viruses: 0.02–0.2 µm'),
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
    extra="- Many medical fungi are known only by their anamorph"),
 au("nome-sexuado", "Once a fungus's sexual stage is found, its {{c1::<b>sexual</b>}} (teleomorph) name takes priority", {1: R}, D_, 'Prioridade do nome da fase sexuada', '31', 'lateral', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'teleomorph OR anamorph' sem card.", [1500401344665, 1500243882463], 'Rosa: regra de nomenclatura do slide 31.', extra='- Medical fungi often keep their familiar asexual names'),
 au("molecular", 'Because morphology is unreliable, fungi are now classified mainly by {{c1::<b>molecular</b>}} (DNA) methods', {1: Z}, D_, 'Classificação molecular', '31; apostila veteranos aula 8', 'central', 'busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): sem card de taxonomia fúngica.', [1500401344665, 1500243882463], "Azul: 'técnicas moleculares são essenciais' (slide 31) e apostila.", extra='- About 100,000 species described of an estimated 5 million'),
 au("mixomicetos", 'Slime molds (Myxomycota), once grouped with fungi, are now classified as {{c1::<b>protists</b>}}', {1: R}, D_, 'Fungos do lodo agora em Protista', '33', 'lateral', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'slime mold*' sem card.", [1500401344665, 1500243882463], 'Rosa: reclassificação do slide 33.', extra='- True fungi = Eumycota'),
 au("filos-medicos", 'Most fungi of medical interest belong to {{c1::<b>Ascomycota</b>}} and {{c2::<b>Basidiomycota</b>}}', {1: V, 2: V}, D_, 'Asco e Basidio: maioria dos fungos médicos', '34–35; monitoria P2', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'Ascomycota OR Basidiomycota' sem card.", [1500401344665, 1500243882463], 'Verdes: destaque circulado do slide 35.', extra='- Together they form the subkingdom <b>Dikarya</b>'),
 au("mucoromycota", '<i>Mucor</i>, <i>Rhizopus</i> and <i>Lichtheimia</i> now belong to the phylum {{c1::<b>Mucoromycota</b>}}', {1: Z}, D_, 'Mucoromycota', '35 e 48', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'Mucorales OR zygomycete*' sem card.", [1500334133616, 1500333766310], 'Azul: gêneros anotados no slide 35; antigo Zygomycota (48).', extra='- Formerly Zygomycota'),
 au("brotamento", "Yeasts reproduce asexually mainly by {{c1::<b>budding</b>}}, which gives unequal cells, whereas {{c2::<b>binary fission</b>}} gives two equal cells", {1: V, 2: Z}, D_,
    "Brotamento × cissiparidade", "37–38; prova 2017 P2 2.4", "prova", "AnKing só cita brotamento por espécie (Blastomyces, Cryptococcus), não o processo.",
    [1499972082394, 1500246246409], "Verde: reprodução da levedura, cobrada em 2017.",
    extra="- The bud is a <b>blastoconidium</b>"),
 au("clamidoconidio", 'Thick-walled resting spores formed from hyphal or yeast cells are {{c1::<b>chlamydoconidia</b>}}', {1: Z}, D_, 'Clamidoconídio', '37; Trabulsi 64.1', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'chlamydo*' só traz Chlamydia.", [1500401344665, 1500243882463], 'Azul: rótulo do slide 37; estrutura de resistência no Trabulsi.', extra='- <i>Candida albicans</i> forms them'),
 au("pseudohifa", "Yeast buds that fail to separate form chains called {{c1::<b>pseudohyphae</b>}}", {1: V}, D_,
    "Pseudo-hifa", "37 e 40", "central", "AnKing cobra pseudo-hifa só como achado da Candida (1557752615914), não como se forma.",
    [1557752615914, 1500234149130], "Verde: forma de invasão da Candida (slide 39).",
    extra="- Unlike true hyphae, they are pinched at each junction", duplicacao_ok="ganho: como a pseudo-hifa se forma; o AnKing cobra o achado da Candida"),
 ak("candida-pseudohifa", 1557752615914, {1: V}, D_, "Candida: pseudo-hifas ± leveduras brotando", 39, "Verde: 'pseudo-hifas na invasão por Candida' (slide 39)."),
 au("micelio", 'A mass of branching hyphae is called a {{c1::<b>mycelium</b>}}', {1: V}, D_, 'Hifas formam o micélio', '42–44; apostila veteranos aula 8; monitoria P2', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'mycelium' só no Extra de Aspergillus.", [1500401344665, 1500243882463], 'Verde: estrutura somática dos bolores (apostila e Benedito).', extra='- Hyphae are the tubular filaments that make up molds'),
 au("micelio-vegetativo", 'The {{c1::<b>vegetative</b>}} mycelium grows into the substrate to absorb nutrients, whereas the {{c2::<b>aerial</b>}} mycelium bears the spores', {1: V, 2: V}, D_, 'Micélio vegetativo × aéreo (reprodutivo)', '44; apostila veteranos aula 8; monitoria P2; Benedito p. 14', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'aerial hypha*' sem card.", [1500401344665, 1500243882463], "Verdes: 'hifa vegetativa' do slide 44 e a divisão da apostila.", extra='- Reproductive structures are the basis of mold identification'),
 au("crescimento-apical", 'Hyphae grow by elongating at their {{c1::<b>tips</b>}}, and a hyphal fragment can start a new colony', {1: R}, D_, 'Crescimento apical e fragmentação', '42; monitoria P2', 'lateral', 'busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): sem card de crescimento de hifa.', [1500401344665, 1500243882463], 'Rosa: detalhe da monitoria.', extra='- Fragmentation is a simple form of asexual reproduction'),
 au("conidios", "<i>Aspergillus</i> and <i>Penicillium</i> spread by asexual spores borne externally on hyphae, called {{c1::<b>conidia</b>}}", {1: V}, D_,
    "Conídios", "42–43; Trabulsi 64.1", "central", "AnKing só tem conidióforo do Aspergillus e artroconídio do Coccidioides.",
    [1500238914091, 1500152894219], "Verde: principal propágulo assexuado e via de infecção.",
    extra="- Asexual spores are made by mitosis"),
 au("macro-microconidio", 'Molds may bear large multicelled {{c1::<b>macroconidia</b>}} and small single-celled {{c2::<b>microconidia</b>}}', {1: Z, 2: Z}, D_, 'Macro e microconídios', '43; prova 2025 P3 1.1', 'prova', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'macroconid* OR microconid*' sem card.", [1500238914091, 1499970409878], 'Azuis: rótulos do slide 43; microconídios inalados na prova 2025.', extra='- Inhaled microconidia transmit <i>Histoplasma</i>'),
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
 au("pleomorfismo", 'Changes in fungal form that do <u>not</u> depend on temperature are called {{c1::<b>pleomorphism</b>}}', {1: Z}, D_, 'Pleomorfismo × dimorfismo', '45; monitoria P2; Benedito p. 27', 'central', 'busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): sem card de pleomorfismo.', [1499970409878, 1499976133630], 'Azul: contraste com dimorfismo térmico da monitoria.', extra='- Thermal dimorphism depends on temperature (and CO₂) and is reversible'),
 au("sexuada", "In fungal sexual reproduction, {{c1::<b>plasmogamy</b>}} (fusion of cytoplasms) comes first, then {{c2::<b>karyogamy</b>}} (fusion of nuclei) and {{c3::<b>meiosis</b>}}", {1: Z, 2: Z, 3: Z}, D_,
    "Plasmogamia, cariogamia, meiose", "46; monitoria P2", "central", "nenhum card AnKing/MCAT de ciclo sexual fúngico.",
    [1509742361304, 1500333766310], "Azuis: sequência da reprodução sexuada do slide 46.",
    extra="- Spores made by meiosis count as sexual: they carry new gene combinations"),
 au("dicario", 'After plasmogamy, the two parental nuclei may stay apart in a {{c1::<b>dikaryotic</b>}} (n + n) phase', {1: Z}, D_, 'Fase dicariótica', '46; Benedito p. 8', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'dikaryo*' sem card.", [1500401344665, 1500243882463], "Azul: 'fase heterocariótica, n + n' do slide 46.", extra='- Long-lasting in Ascomycota and Basidiomycota (Dikarya)'),
 # ---------- E. Filos de interesse médico (slides 48–53) ----------
 au("septos", "Fungal hyphae without cross-walls, with many nuclei in one cytoplasm, are {{c1::<b>coenocytic</b>}}", {1: V}, E_,
    "Hifa cenocítica × septada", "44 e 48; Trabulsi fig. 64.1.5", "central", "AnKing só cobra 'non-septated' do Mucor.",
    [1500334133616, 1500238441939], "Verde: hifa septada × cenocítica separa os grandes grupos de bolores.",
    extra="- Most molds have <b>septate</b> hyphae"),
 ak("mucor-hifa", 1500334133616, {1: V, 2: V}, E_, "Mucor/Rhizopus: hifas não septadas", 48, "Verdes: HY (2); micélio cenocítico do antigo Zygomycota."),
 au("zigosporo", 'The sexual spore of <i>Mucor</i> and <i>Rhizopus</i> (former Zygomycota) is the {{c1::<b>zygospore</b>}}', {1: Z}, E_, 'Zigósporo', '48; monitoria P2; Benedito p. 9', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'zygospore*' sem card.", [1500334133616, 1500333766310], 'Azul: reprodução sexuada do antigo Zygomycota (slide 48).', extra='- Their asexual spores are sporangiospores'),
 au("basidio", "In mushrooms (Basidiomycota), each sexual spore buds from the tip of a {{c1::<b>basidium</b>}}", {1: Z}, E_,
    "Basídio", "50; Trabulsi fig. 64.1.11", "central", "nenhum card de basídio no AnKing/MCAT.",
    [1500238914091, 1500333766310], "Azul: estrutura que define o filo (slide 50).",
    extra="- Basidia line the gills of the mushroom cap"),
 au("asco", "Which sac-like cell holds the sexual spores (usually eight) of Ascomycota?<br><br>{{c1::<b>Ascus</b>}}", {1: Z}, E_,
    "Asco", "52; Trabulsi fig. 64.1.12", "central", "nenhum card de asco no AnKing/MCAT.",
    [1500238914091, 1500333766310], "Azul: estrutura que define o filo (slide 52).",
    extra="- Ascospores form inside the ascus: internal sexual spores"),
 # ---------- F. Ecologia e nutrição (slides 55–61) ----------
 au("anemofilos", 'Fungal spores spread mostly through the {{c1::<b>air</b>}}, and inhaled spores cause respiratory allergies', {1: Z}, F_, 'Dispersão pelo ar; anemófilos e alergias', '55; Benedito pp. 29–33; Trabulsi 64.2', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'fung* allerg* spore*' sem card.", [1500401344665, 1500243882463], 'Azul: vias de dispersão (slide 55) e fungos anemófilos do Benedito.', extra='- Also by water, soil, animals and insects'),
 ak("aspergillus-inalacao", 1500239016754, {1: V}, F_, "Aspergillus transmitido por inalação", 55, "Verde: HY (2); ar como via de dispersão (slide 55)."),
 au("exoenzimas", "Fungi digest food <u>outside</u> the cell with secreted {{c1::<b>exoenzymes</b>}}, then absorb the small molecules", {1: V}, F_,
    "Nutrição por absorção", "56–57", "central", "nenhum card AnKing/MCAT de osmotrofia.",
    [1500152000410, 1509742036852], "Verde: modo de vida que define o reino.",
    extra="- Lipases, proteinases and keratinases break down macromolecules"),
 ak("queratinase", 1500152000410, {1: Z, 2: Z}, F_, "Queratinase dos dermatófitos", 56, "Azuis: queratinases do slide 56; liga com a aula de micoses cutâneas."),
 au("nutrientes", 'Fungi need organic carbon such as {{c1::<b>glucose</b>}}, but can take nitrogen from nitrate or ammonium', {1: R}, F_, 'Nutrientes: carbono orgânico, nitrogênio inorgânico', '57; apostila veteranos aula 8', 'lateral', 'busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): sem card de nutrição fúngica.', [1500401344665, 1500243882463], 'Rosa: fontes do slide 57.', extra='- Trace metals and vitamins are needed in tiny amounts'),
 au("mesofilos", "Most medically important fungi are {{c1::<b>mesophiles</b>}}, growing best at 20–30 °C", {1: Z}, F_,
    "Mesófilos", "58; prova 2018 P2 1.4", "prova", "nenhum card de temperatura de crescimento fúngico.",
    [1500054938635, 1500234149130], "Azul: fatores ambientais cobrados em 2018.",
    extra="- Psychrophiles grow in the cold, thermophiles in heat"),
 au("aerobios", 'Most fungi are obligate {{c1::<b>aerobes</b>}}, although fermenting yeasts are facultative anaerobes', {1: Z}, F_, 'Aeróbios obrigatórios', '58; apostila veteranos aula 8; monitoria P2; Benedito p. 38', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'fung* aerob*' sem card.", [1500401344665, 1500243882463], 'Azul: aeração como fator de crescimento (apostila).', extra='- Sexual reproduction needs an oxygen-rich atmosphere'),
 au("luz", 'Fungi grow vegetatively in the dark but need {{c1::<b>light</b>}} to form reproductive structures', {1: Z}, F_, 'Luz: reprodução', '58; apostila veteranos aula 8; monitoria P2', 'central', 'busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): sem card de luz e fungos.', [1500401344665, 1500243882463], 'Azul: fator ambiental da apostila e da monitoria.', extra='- Direct sunlight kills fungi (UV)'),
 au("atividade-agua", "Fungi stop growing when the water activity of their substrate falls to about {{c1::<b>0.65</b>}}", {1: Z}, F_,
    "Atividade de água mínima", "59; prova 2018 P2 1.4", "prova", "nenhum card de atividade de água.",
    [1500054938635, 1517779158524], "Azul: umidade como fator ambiental cobrado em 2018.",
    extra="- Dry storage prevents mold in grains and buildings"),
 au("ph", 'Most fungi grow best at a pH of about {{c1::<b>6.5</b>}}, but tolerate a wide range', {1: Z}, F_, 'pH ótimo ~6,5', '60; prova 2018 P2 1.4', 'prova', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'fung* pH' sem card.", [1500401344665, 1500243882463], 'Azul: pH no slide 60 e na prova 2018.', extra='- 6.5 is the value on the slide and in the 2018 exam key (the veteran guide says 5.6)<br>- Yeasts tolerate pH 2.5–8.5; molds 1.5–11'),
 au("liquen", 'A {{c1::<b>lichen</b>}} is a mutualism between a fungus and an alga or cyanobacterium', {1: Z}, F_, 'Liquens', '61; Benedito p. 34', 'central', "busca 09/10 (AnKing, MCAT, Histology, LLU, Dope, AnatoKing): 'lichen*' só traz líquen escleroso.", [1500401344665, 1500243882463], 'Azul: lâmina final.', extra='- Fungus (mycobiont) protects; alga (photobiont) photosynthesizes<br>- 98% of lichen fungi are ascomycetes'),
]

NOTAS = {
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
 "aspergillus-inalacao": "Conidia are small enough to reach the alveoli",
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


# ---- Revisão do Opus (11/10/2026, REVISAO-OPUS.md; F-20261011-CLAUDE-04: faltava a parte introdutória) ----
import re as _re
def _c(key):
    return next(c for c in CARDS if c["key"] == key)


def _cor(key, cor):
    c = _c(key); c["flags"] = {n: cor for n in c["flags"]}
    if c["kind"] == "text": c["clinica_lateral"] = True


def _ak(key, text=None, extra=None, **kw):
    c = _c(key); fo = c.setdefault("fields_override", {})
    if text: fo["Text"] = text
    if extra is not None: c.pop("extra_add", None); fo["Extra"] = extra
    c.update(kw)


def _novo(key, text, cor, bloco, alvo, slide, autoria, extra, esp):
    n = sorted({int(x) for x in _re.findall(r"\{\{c(\d+)::", text)})
    CARDS.append(au(key, text, {i: cor for i in n}, bloco, alvo, slide, autoria, "sem card nos acervos (revisão do Opus).", esp, "Revisão do Opus.", extra=extra))


# fugas e erros
_ak("rhizopus-pao", extra="- Rhizopus forms sporangia full of sporangiospores", clinica_lateral=True); _cor("rhizopus-pao", Z)
_cor("mucor-hifa", Z)
_ak("dimorfismo", extra="- Most endemic systemic fungi (Histoplasma, Paracoccidioides) are thermally dimorphic<br>- Cryptococcus and Candida are not")
_ak("paracocci-dimorfico", text="<i><b>Paracoccidioides brasiliensis</b></i> is a {{c1::thermally dimorphic}} fungus that grows as a mold at 25 °C and as a yeast at 37 °C")
_ak("flucitosina-medula", extra="- It causes bone marrow suppression")
_ak("aflatoxina-graos", extra="- Mycotoxins contaminate stored grains such as corn and wheat")
_cor("capsula-fagocitose", Z)
CARDS[:] = [c for c in CARDS if c["key"] not in ("aspergillus-inalacao", "polienos-eletrolitos", "quitridio")]
# detalhe específico vira rosa; definição de modo de vida e prioridade do teleomorfo sobem
for k in ("quitina-levedura", "mucoromycota", "clamidoconidio", "pleomorfismo", "dicario", "zigosporo", "luz", "liquen", "micorriza"):
    _cor(k, R)
_cor("saprofita", V); _cor("nome-sexuado", Z)
_c("pleomorfismo")["extra"] = "- Example: loss of conidia and sterile mycelium after repeated subculture"
# lacunas (G1–G8, G10–G13)
_novo("levedura-bolor", "<b>Yeasts</b> are {{c1::unicellular}} fungi, whereas <b>molds</b> are {{c2::multicellular}} fungi made of filaments", V, B_, "Levedura unicelular × bolor filamentoso", "21; 19", "central", "- A yeast cell does both vegetative and reproductive work by itself", [1499970409878, 1500334133616])
_novo("hifas", "The body (<b>thallus</b>) of a <b>mold</b> is made of long tubular filaments called {{c1::hyphae}}", V, B_, "Talo do bolor = hifas", "21; Benedito p. 7", "central", "- A mass of hyphae is a mycelium", [1500334133616, 1499970409878])
_novo("hifa-septada", "In most <b>molds</b>, cross-walls called {{c1::septa}} divide the <b>hyphae</b> into cells", V, B_, "Hifa septada", "21; Benedito p. 10", "central", "- Hyphae without septa are coenocytic, as in Mucor and Rhizopus", [1500334133616, 1499970409878])
_novo("parede-funcao", "The fungal <b>cell wall</b> gives the cell its {{c1::shape}} and protects it from <b>osmotic lysis</b>", Z, B_, "Função da parede", "22", "central", "- It is the target of echinocandins", [1500244482455, 1499970409878])
_novo("parede-camadas", "In the fungal <b>cell wall</b>, {{c1::chitin}} forms the innermost layer, next to the <b>membrane</b>", R, B_, "Camadas da parede", "23", "lateral", "- β-glucans lie above it, and mannoproteins form the outer layer", [1500244482455, 1499970409878])
_novo("deuteromycetes", "Fungi with no known <b>sexual stage</b> were grouped as {{c1::Deuteromycetes}} (fungi imperfecti)", Z, D_, "Deuteromycetes", "32", "central", "- Most fungi of medical interest are known only by their asexual form", [1499970409878, 1500334133616])
_novo("oomycetes", "<b>Oomycetes</b> (water molds) look like fungi but belong to the kingdom {{c1::Chromista}}", R, E_, "Oomycota fora de Fungi", "32", "lateral", "- Their wall is mostly cellulose, not chitin", [1499970409878, 1500334133616])
_novo("conidio-esporangio", "<b>Conidia</b> form {{c1::outside}} any sac, whereas <b>sporangiospores</b> form {{c2::inside}} a sporangium", Z, D_, "Conídio externo × esporangiósporo interno", "43, 44", "central", "- Aspergillus and Penicillium make conidia, while Rhizopus and Mucor make sporangiospores", [1500334133616, 1500333766310])
_novo("importancia-medica", "Fungal infections have become more important mainly in {{c1::immunocompromised}} and <b>hospitalized</b> patients", Z, A_, "Importância médica crescente", "3; monitoria", "prova", "- Only a small fraction of fungal species harm humans", [1499970409878, 1500244482455])
_novo("endotermia", "Mammalian {{c1::endothermy}} (~37 °C) may protect against most <b>fungi</b>, which cannot grow at that temperature", R, A_, "Endotermia protege dos fungos", "15", "lateral", "- Casadevall linked this to the extinction of the dinosaurs", [1499970409878, 1500244482455])
_novo("zoopagomycota", "The genera <b>Conidiobolus</b> and <b>Basidiobolus</b> belong to the phylum {{c1::Zoopagomycota}}", R, E_, "Zoopagomycota", "35", "lateral", "- They were formerly in Zygomycota", [1500334133616, 1500333766310])
_novo("queijos", "<b>Penicillium</b> molds are used to ripen cheeses such as {{c1::Roquefort}} and Camembert", R, A_, "Fungos na maturação de queijos", "4", "lateral", "- Yeasts ferment bread, beer and wine", [1500333766310, 1499970409878])
_ak("dimorfismo", text="<i><b>Histoplasma</b>, <b>Paracoccidioides</b> and other endemic systemic fungi</i> are found in the {{c1::mold}} form in <u>soil</u> and the {{c1::yeast}} form in the <u>body</u>")

# ---- Revisão por prova 15/10 (F-20261015-CLAUDE-03): organizadores de mapa mental, em tópicos ----
ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
_MOT = "Revisão 15/10: organizador de mapa mental pedido por Davi."
_EP = [c["src"] for c in CARDS if c["kind"] == "text"][:2]
def _sl(c): return int(_re.search(r"\d+", str(c["evid"])).group())
def _no_slide(n, card):
    i = next(i for i, c in enumerate(CARDS) if _sl(c) >= n); CARDS.insert(i, card)
_no_slide(21, au("org-fungo-bacteria", ORG("<b>Fungi</b> × bacteria:<br>- cell: {{c1::eukaryotic}} × prokaryotic<br>- wall: {{c2::chitin}} × peptidoglycan<br>- ribosomes: {{c3::80S}} × 70S<br>- membrane sterol: {{c4::ergosterol}} × none"),
    {1: V, 2: V, 3: V, 4: V}, B_, "Fungos × bactérias", "21", "prova", "nenhum card dos acervos.", _EP, "Verde: lâmina 21; provas 2017 P2 2.5 e 2018 P2 1.3 (tabela fungo × bactéria). " + _MOT,
    duplicacao_ok="organizador da comparação cobrada em prova"))
_no_slide(21, au("org-formas", ORG("Forms of <b>fungi</b>:<br>- {{c1::yeast}}: single budding cells<br>- {{c2::mold}}: hyphae forming a mycelium<br>- {{c3::dimorphic}}: yeast at 37 °C, mold at 25 °C"),
    {1: V, 2: V, 3: V}, B_, "Formas morfológicas", "21", "prova", "nenhum card dos acervos.", _EP, "Verde: lâminas 19–21 e 45; provas 2017 e 2018 (forma e dimorfismo). " + _MOT,
    duplicacao_ok="organizador; cada forma tem cards de detalhe"))
_no_slide(27, au("org-antifungicos", ORG("<b>Antifungals</b> by target:<br>- bind ergosterol: {{c1::polyenes}}<br>- block ergosterol synthesis: {{c2::azoles}}<br>- block β-glucan synthesis: {{c3::echinocandins}}<br>- block nucleic acid synthesis: {{c4::flucytosine}}"),
    {1: V, 2: V, 3: V, 4: V}, C_, "Antifúngicos por alvo", "27", "central", "nenhum card dos acervos.", _EP, "Verde: lâmina 27 (antifúngicos e alvos). " + _MOT,
    duplicacao_ok="organizador; os AnKing de cada classe trazem o mecanismo"))
_no_slide(48, au("org-esporos-sexuados", ORG("Sexual spores by <b>phylum</b>:<br>- Mucoromycota (old Zygomycota): {{c1::zygospore}}<br>- Basidiomycota: {{c2::basidiospores}} on a basidium<br>- Ascomycota: {{c3::ascospores}} inside an ascus"),
    {1: Z, 2: Z, 3: Z}, D_, "Esporos sexuados por filo", "48", "central", "nenhum card dos acervos.", _EP, "Azul: lâminas 48–52. " + _MOT,
    duplicacao_ok="organizador; cada filo tem card próprio"))

# textos vivos (correções de comentários de Davi feitas ao vivo) trazidos à spec, 15/10
_c('colonias')["text"] = "{{c1::<b>Yeasts::Yeasts/Molds</b>}} form creamy, pasty colonies, whereas {{c1::<b>molds::ye</b><b>asts/molds</b>}} form cottony, velvety or powdery ones"
_c('colonias')["extra"] = "- Telling them apart is the first step in culture identification<br><br><img src=\"nebli-trabulsi-fig-64-1-3.png\" style=\"max-width:100%;max-height:52vh\">"
_c('colonias')["flags"] = {n: list(_c('colonias')["flags"].values())[0] for n in [1]}
_c('mucoromycota')["text"] = "<img src=\"nebli-mb43-arvore-fungos-oculto.png\" style=\"max-width:100%;max-height:45vh\"><br>The phylum that now includes <i>Mucor</i>, <i>Rhizopus</i> and <i>Lichtheimia</i> is {{c1::<b>Mucoromycota</b>}}"
_c('mucoromycota')["extra"] = "- These genera were formerly grouped in Zygomycota<br>- Most fungi of medical interest are Ascomycota and Basidiomycota<br><img src=\"nebli-mb43-arvore-fungos.png\" style=\"max-width:100%;max-height:52vh\">"
_c('mucoromycota')["flags"] = {n: list(_c('mucoromycota')["flags"].values())[0] for n in [1]}
_c('conidio-esporangio')["text"] = "Asexual <b>spores</b> formed freely on hyphae are {{c1::conidia}}, whereas spores formed inside a sac (sporangium) are sporangiospores"
_c('conidio-esporangio')["extra"] = "- Aspergillus and Penicillium make conidia, while Rhizopus and Mucor make sporangiospores"
_c('conidio-esporangio')["flags"] = {n: list(_c('conidio-esporangio')["flags"].values())[0] for n in [1]}
for _c_ in CARDS:
    _x_ = {"org-fungo-bacteria": "- Fungi are also larger (3–10 µm vs 1–5 µm); these differences are drug targets",
           "org-formas": "- Candida also forms pseudohyphae from buds that do not separate",
           "org-antifungicos": "- Polyenes: amphotericin B, nystatin; allylamines (terbinafine) also block ergosterol synthesis; human cells lack ergosterol and β-glucan",
           "org-esporos-sexuados": "- Most fungi of medical interest are Ascomycota or Basidiomycota"}.get(_c_["key"])
    if _x_: _c_["extra"] = _x_
