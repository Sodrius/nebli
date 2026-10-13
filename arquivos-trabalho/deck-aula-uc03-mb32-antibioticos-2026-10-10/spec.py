# Especificação curada — Antibióticos, resistência e antibiograma (UC03 P2, Microbiologia, aula 32; Prof. Nilton Lincopan; 99 lâminas de 2026).
# Gerada a partir de inventario.py (escrito antes). Fontes: lâminas 2026, aula da turma "Mecanismos de ação de antibióticos" (Aula 05, 2024),
# provas micro-05 (2025 P2 1.3–1.5, 2024 P2 1.8–1.10, 2023, 2019, 2018, 2017), monitoria P2 aula 4, guia de veteranos aula 4. Vídeos dispensados (F-06).
# Foco em mecanismo e resistência (F-04); clínica e farmacologia lateral entram rosa. Ordem = slides.
RUN_ID = "uc03-mb32-20261010a"
SHORT = "mb32"
LESSON = "2026-uc03-microbiologia-32-antibioticos-resistencia"
DECK = "NEBLI::UC03::P2::Microbiologia::Antibióticos e resistência"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-06) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por seções Bootcamp/B&B '07_Antimicrobials' (busca/tags-secao.txt, 862 notas) e texto livre em AnKing e Referências Externas "
         "(busca/anking.txt: β-lactâmicos, β-lactamases, PBP/MRSA, vancomicina, quinolonas, síntese proteica, sulfas, polimixinas/daptomicina, "
         "toxicidade, resistência/plasmídeos/biofilme, CIM/disco, estático/cida, ESBL/KPC), 10/10: ")
EXCLUIDOS = [
 (1503602391827, "β-lactamases em plasmídeos (HY 4): coberto pelo autoral de conjugação de plasmídeos"),
 (1503682232653, "cefalosporinas mimetizam D-ala-D-ala: repete o card da penicilina"),
 (1506032880639, "aminoglicosídeos causam leitura errada do mRNA: detalhe do mesmo mecanismo do 30S"),
 (1403560526372, "mecanismo do cloranfenicol: só a toxicidade entra na aula"),
 (1489092893676, "β-lactâmicos inibem transpeptidases: repete 1503600789007"),
 (1505341710664, "tratamento do MRSA com vancomicina: farmacologia/clínica, a aula só cita a escolha"),
 (1503191048613, "tratamento de VRE (linezolida, tigeciclina): clínica lateral à compreensão"),
 (1508429660003, "dapsona: fora da aula"),
 (1489873889112, "fidaxomicina e sigma: fora da aula"),
]
FORA_DO_RECORTE = [
 "Lâminas 2–3 (RAM no Brasil) e 73–74 (rios e vida selvagem): contexto de saúde única, sem item cobrado",
 "Lâminas 32–35 (figuras de mecanismo e vídeo) e 83–86 (placas de E-test): figuras sem texto novo",
 "Lâminas 89–92: listas de antibióticos por sítio e por organismo (empírico): clínica, será de Farmacologia (UC19)",
 "Custos (turma 106), farmacocinética PK/PD (lâmina 52) e doses",
 "Roteiro prático de antibiograma (Aula 08 da turma): cai na Prática 2",
]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


WALL = [1503600789007, 1503603239057]
PROT = [1505672514005, 1506032634763]
GYR = [1508430090586, 1508364963869]
RES = [1503602269788, 1484873258290]
A_, B_, C_, D_, E_, F_, G_, H_, I_, J_ = ("A-historia-e-selecao", "B-classificacao", "C-parede", "D-quinolonas", "E-sintese-proteica", "F-membrana",
                                          "G-sulfas", "H-uso-racional", "I-resistencia", "J-antibiograma")
CARDS = [
 # ---------- A. História, seleção e toxicidade (lâminas 4–19) ----------
 au("criterios", "Antibiotic choice weighs the pathogen's Gram type and spectrum, the infection site, the host's immune state and its {{c1::MIC}}", {1: Z}, A_,
    "Critérios de seleção", "4; turma 105; monitoria", "central", "sem card de critérios de seleção.", WALL,
    "Azul: lâmina 4.", extra="- Toxicity, cost and route also count"),
 ak("tox-bebe-cinzento", 1403561007139, {1: R}, A_, "Cloranfenicol: síndrome do bebê cinzento", 5, "Rosa: toxicidade citada na lâmina 5; HY 2, clínica lateral (F-04).", clinica_lateral=True),
 ak("tox-dentes", 1505669971508, {1: R}, A_, "Tetraciclinas: dentes e ossos", 5, "Rosa: lâmina 5; HY 1, clínica lateral (F-04).", clinica_lateral=True),
 ak("tox-oto-nefro", 1506031666960, {1: R}, A_, "Aminoglicosídeos: oto e nefrotoxicidade", 5, "Rosa: lâmina 5; HY 1, clínica lateral (F-04).", clinica_lateral=True),
 au("selecao-toxicidade", "Antibiotics are useful because they act on targets absent from human cells, a property called {{c1::selective}} toxicity", {1: V}, A_,
    "Toxicidade seletiva", "4–5, 51; turma; guia de veteranos", "central", "AnKing não nomeia o princípio.", WALL,
    "Verde: ideia que organiza a aula.", extra="- Targets: cell wall, bacterial ribosome, folate synthesis, DNA gyrase"),
 au("quimio", "Chemotherapeutics such as sulfonamides and quinolones are {{c1::synthetic}} compounds, whereas antibiotics are made by microorganisms", {1: Z}, A_,
    "Quimioterápico × antibiótico", "9–14; turma; monitoria", "central", "sem card.", WALL,
    "Azul: lâminas 12 e 14.", extra="- Penicillin comes from <i>Penicillium</i>, streptomycin from <i>Streptomyces griseus</i>"),
 au("ehrlich", "Paul Ehrlich introduced the first synthetic chemotherapeutic, the arsenic compound {{c1::Salvarsan}}, in 1910", {1: R}, A_,
    "Ehrlich e Salvarsan", "10–11; monitoria", "lateral", "sem card histórico.", WALL, "Rosa: história.", extra="- Domagk's sulfonamides followed in 1935 and Fleming's penicillin in 1942"),
 au("metabolito", "Antibiotics are secondary metabolites, produced mainly in the {{c1::stationary}} phase of growth", {1: Z}, A_,
    "Antibióticos como metabólitos secundários", "15–17; turma", "central", "sem card.", WALL,
    "Azul: lâminas 15–17.", extra="- Bacteriocins, like those of <i>Pseudomonas aeruginosa</i>, are made the same way"),
 # ---------- B. Classificação (lâminas 20–25) ----------
 au("espectro-amplo", "Broad-spectrum antibiotics also destroy the normal {{c1::microbiota}}, letting resistant opportunists overgrow", {1: Z}, B_,
    "Espectro e microbiota", "20; guia de veteranos", "central", "sem card.", WALL,
    "Azul: lâmina 20.", extra="- A narrow, directed spectrum spares the competitors"),
 au("estatico", "A {{c1::bacteriostatic}} antibiotic only halts growth, so the host immune system must clear the infection", {1: V}, B_,
    "Bacteriostático", "23; guia; prova 2024 P2 1.10", "prova", "AnKing só rotula cada droga.", WALL,
    "Verde: lâmina 23 e prova 2024.", extra="- Sulfonamides, tetracyclines and erythromycin are bacteriostatic"),
 sh(1791647816594, "azul", B_, "Estáticos agem melhor na fase log", 23, "Nota viva da Fisiologia bacteriana; resposta da prova 2024 P2 1.10."),
 au("cida", "Bactericidal drugs are preferred in meningitis and in {{c1::immunocompromised}} patients", {1: Z}, B_,
    "Quando preferir bactericida", "23; guia de veteranos", "central", "sem card.", WALL,
    "Azul: guia.", extra="- They kill without depending on host defenses"),
 au("quatro-alvos", "Antibiotics act mainly by blocking cell wall, protein or nucleic acid synthesis, or by disrupting the {{c1::membrane}}", {1: V}, B_,
    "Quatro mecanismos de ação", "24–25; guia", "central", "sem card.", WALL,
    "Verde: lâmina 24.", extra="- Sulfonamides block a fifth target, folate metabolism"),
 # ---------- C. Parede (lâminas 26–40) ----------
 au("parede-so-cresce", "Cell wall inhibitors kill only bacteria that are {{c1::growing}}, because they block the building of new peptidoglycan", {1: V}, C_,
    "Parede só mata célula em crescimento", "26; guia de veteranos", "central", "AnKing não liga crescimento ao efeito.", WALL,
    "Verde: guia.", extra="- Bacteria with no wall synthesis, such as resting cells, are spared"),
 ak("blac-pbp", 1503600789007, {1: V}, C_, "β-lactâmicos inibem PBPs", 27, "Verde: lâmina 27 (HY 2)."),
 ak("blac-dala", 1503603239057, {1: V}, C_, "Penicilina mimetiza D-ala-D-ala", 27, "Verde: HY 1."),
 ak("blac-cida", 1489092729957, {1: V}, C_, "β-lactâmicos são bactericidas", 27, "Verde: HY 1; lâmina 27."),
 sh(1791576670517, "azul", C_, "Inibir a transpeptidase não mata diretamente", 36, "Nota viva da Morfologia; liga a lâmina 36 (bactericida) às autolisinas."),
 ak("osmolise", 1503603067923, {1: Z}, C_, "Morte por osmólise", 36, "Azul: HY 3; lâmina 36."),
 au("penicilina-natural", "Natural penicillins have a narrow spectrum and are destroyed by {{c1::β-lactamases}}", {1: Z}, C_,
    "Penicilinas naturais", "28; guia de veteranos", "central", "sem card.", WALL,
    "Azul: lâmina 28.", extra="- Penicillin G and V, the first group", duplicacao_ok="ganho: espectro e fragilidade da penicilina natural; blactamase-pbp lista mecanismos de resistência"),
 ak("aminopenicilina", 1489341109037, {1: Z}, C_, "Aminopenicilinas: amplo espectro", 28, "Azul: HY 3; lâmina 28."),
 ak("antiestafilo", 1489338078152, {1: V}, C_, "Antiestafilocócicas resistem à penicilinase", 28, "Verde: HY 2; lâmina 28 (oxacilina, meticilina)."),
 ak("cefalo-blact", 1489354783439, {1: Z}, C_, "Cefalosporinas resistem às β-lactamases", 29, "Azul: HY 3."),
 ak("ceftarolina", 1489355257551, {1: R}, C_, "Ceftarolina liga a PBP alterada do MRSA", 29, "Rosa: HY 3; 5ª geração, detalhe da lâmina 29."),
 au("cefalo-geracoes", "Cefotaxime and ceftriaxone belong to the {{c1::third}} generation of cephalosporins", {1: R}, C_,
    "Gerações de cefalosporinas", "29; turma 23", "lateral", "AnKing lista gerações em sentido inverso.", WALL, "Rosa: lista da lâmina 29.",
    extra="- First: cefazolin; fourth: cefepime; fifth: ceftaroline"),
 ak("carbapenem-esbl", 1505266119200, {1: Z}, C_, "Carbapenêmicos contra ESBL", 30, "Azul: HY 3; lâmina 30."),
 au("carbapenem-ultimo", "Carbapenems such as imipenem and meropenem are broad-spectrum agents kept as a {{c1::last}} therapeutic alternative", {1: Z}, C_,
    "Carbapenêmicos: última alternativa", "30; turma 24", "central", "sem card.", WALL, "Azul: lâmina 30."),
 au("aztreonam", "The monobactam aztreonam acts only on Gram-negative bacteria, including producers of {{c1::metallo}}-β-lactamases", {1: R}, C_,
    "Aztreonam", "31; turma 25", "lateral", "sem card.", WALL, "Rosa: lâmina 31."),
 ak("inibidor-blac", 1503672347649, {1: V}, C_, "Clavulanato inibe β-lactamases", 37, "Verde: HY 2; lâminas 37–38 e 60 da turma."),
 au("inibidor-como", "Clavulanate, sulbactam and tazobactam protect their partner antibiotic by inactivating the bacterial {{c1::β-lactamase}}", {1: V}, C_,
    "Como o inibidor protege o antibiótico", "37–38; turma 59–60; monitoria", "central", "AnKing só dá o par amoxicilina-clavulanato.", WALL,
    "Verde: monitoria.", extra="- Pairs: amoxicillin–clavulanate, ampicillin–sulbactam, piperacillin–tazobactam",
    duplicacao_ok="Ganho: ação do inibidor sobre a β-lactamase; card AnKing cobra a enzima como mecanismo de resistência."),
 au("avibactam", "Ceftazidime-avibactam pairs a cephalosporin with a β-lactamase inhibitor that is active against {{c1::KPC}} producers", {1: R}, C_,
    "Ceftazidima-avibactam", "19, 29, 37", "lateral", "sem card.", WALL, "Rosa: lâminas 19, 29 e 37."),
 au("vanco-gram-pos", "Vancomycin is too large and hydrophilic to cross the Gram-negative outer membrane, so it acts only on {{c1::Gram-positive}} bacteria", {1: V}, C_,
    "Por que vancomicina só age em Gram-positivos", "39; monitoria; guia", "central", "AnKing não explica o espectro.", WALL,
    "Verde: lâmina 39 e monitoria."),
 ak("vanco-dala", 1505341800984, {1: V}, C_, "Vancomicina liga D-ala-D-ala", 39, "Verde: HY 1; lâmina 39."),
 au("vanco-vs-blac", "Unlike β-lactams, vancomycin binds the D-ala-D-ala substrate itself rather than the {{c1::enzyme}}", {1: Z}, C_,
    "Vancomicina liga o substrato, β-lactâmico liga a enzima", "26, 39; turma 44", "central", "sem card do contraste.", WALL,
    "Azul: lâminas 26 e 39.", duplicacao_ok="ganho: contrasta alvo (substrato × enzima); vanco-dala cobra o nome da droga"),
 # ---------- D. Quinolonas (lâminas 41–43) ----------
 ak("quin-girase", 1508430090586, {1: V}, D_, "Quinolonas inibem girase e topoisomerase IV", 41, "Verde: HY 1; lâminas 41–43."),
 au("quin-cida", "Fluoroquinolones are {{c1::bactericidal}}, because blocking gyrase leaves lethal DNA breaks", {1: Z}, D_,
    "Quinolonas são bactericidas", "23, 41–43; turma 28", "central", "sem card.", GYR, "Azul: lâmina 23.",
    extra="- Gyrase inhibition causes lethal DNA damage, not just arrest", duplicacao_ok="ganho: classe das quinolonas; blac-cida cobra os β-lactâmicos"),
 au("quin-resist", "Mutation of the {{c1::gyrA}} gene is the main mechanism of fluoroquinolone resistance in Gram-positive and Gram-negative bacteria", {1: V}, D_,
    "Resistência a quinolonas: gyrA", "63; prova 2025 P2 1.4", "prova", "AnKing cita topoisomerase só como alvo.", GYR, "Verde: prova 2025."),
 # ---------- E. Síntese proteica (lâminas 44–47) ----------
 ak("mnemonico-30-50", 1506272992776, {1: V}, E_, "30S × 50S: AT em 30, CCEL em 50", 44, "Verde: HY 1; lâmina 44 (todos os grupos)."),
 ak("macrolideo-50s", 1505672514005, {1: V}, E_, "Macrolídeos: 23S rRNA do 50S", 45, "Verde: HY 1; lâmina 45."),
 au("macrolideo-gram", "Macrolides are large molecules that cross the Gram-negative outer membrane poorly, so they are used mainly against {{c1::Gram-positive}} bacteria", {1: Z}, E_,
    "Macrolídeos e Gram-positivos", "45; monitoria", "central", "AnKing não liga tamanho ao espectro.", PROT, "Azul: lâmina 45."),
 ak("aminoglicosideo-30s", 1506032634763, {1: V}, E_, "Aminoglicosídeos: 30S, iniciação", 46, "Verde: HY 1; lâmina 46."),
 ak("aminoglicosideo-o2", 1500498334911, {1: V}, E_, "Aminoglicosídeos precisam de O2", 46, "Verde: HY 2; por que não agem em anaeróbios."),
 ak("tetraciclina-30s", 1505667598387, {1: V}, E_, "Tetraciclinas: 30S, bloqueiam o aminoacil-tRNA", 47, "Verde: HY 1; lâmina 47."),
 ak("tetraciclina-intra", 1403557897769, {1: V}, E_, "Tetraciclinas agem em bactérias intracelulares", 47, "Verde: HY 2; Mycoplasma, Chlamydia, Rickettsia (lâmina 47)."),
 au("ribossomo-mito", "Some protein synthesis inhibitors are toxic to humans because {{c1::mitochondrial}} ribosomes resemble bacterial ribosomes", {1: Z}, E_,
    "Toxicidade pelos ribossomos mitocondriais", "44; guia de veteranos", "central", "sem card.", PROT, "Azul: guia.", extra="- Bacterial ribosomes are 70S: 30S + 50S subunits"),
 # ---------- F. Membrana (lâminas 48–50) ----------
 au("polimixina-lps", "Polymyxins are cationic detergents that bind the negatively charged {{c1::LPS}} of the Gram-negative outer membrane", {1: V}, F_,
    "Polimixinas e LPS", "48–50; turma 55–56", "central", "AnKing só cita polimixina como salvamento.", WALL, "Verde: lâminas 48–50.",
    extra="- Polymyxin B and polymyxin E (colistin) disrupt the outer membrane"),
 ak("polimixina-mdr", 1514419769692, {1: Z}, F_, "Polimixinas como resgate em Gram-negativos MDR", 49, "Azul: HY 3."),
 ak("daptomicina", 1505671257156, {1: R}, F_, "Daptomicina age em Gram-positivos", 19, "Rosa: HY 3; só listada na lâmina 19."),
 # ---------- G. Sulfas (lâmina 51) ----------
 ak("sulfa-paba", 1508364963869, {1: V}, G_, "Sulfa: análogo do PABA, inibe di-hidropteroato sintase", 51, "Verde: HY 1; lâmina 51 (antagonismo competitivo)."),
 au("sulfa-seletiva", "Sulfonamides are selectively toxic because human cells cannot make folate and take it from the {{c1::diet}}", {1: Z}, G_,
    "Seletividade das sulfas", "51; turma 57–58", "central", "sem card.", GYR, "Azul: lâmina 51."),
 au("trimetoprima", "Trimethoprim blocks {{c1::dihydrofolate reductase}}, the step after the one blocked by sulfonamides", {1: Z}, G_,
    "Trimetoprima", "12; turma 57", "central", "AnKing só cita a enzima.", GYR, "Azul: SXT é citado nas lâminas 12 e 90–92.",
    extra="- Together they act in sequence on folate synthesis"),
 ak("sulfa-kernicterus", 1508367757945, {1: R}, G_, "Sulfonamidas e kernicterus", 5, "Rosa: toxicidade da lâmina 5; HY 2, clínica lateral (F-04).", clinica_lateral=True),
 # ---------- H. Uso racional (lâminas 53, 99) ----------
 au("uso-racional", "Rational antibiotic use means prescription only, the right dose, the right interval and the right {{c1::duration}}", {1: Z}, H_,
    "Uso racional", "53, 99; turma 127", "central", "sem card.", RES, "Azul: lâminas 53 e 99.", extra="- Prescription only, and only when really needed"),
 au("associacao-tb", "Long therapies such as tuberculosis combine several antibiotics to delay the emergence of {{c1::resistance}}", {1: Z}, H_,
    "Associação para retardar resistência", "99; turma 127; prova 2023 P2 3.4", "prova", "sem card.", RES, "Azul: prova 2023.", duplicacao_ok="ganho: associação de drogas contra resistência; o AnKing do porina trata de um mecanismo"),
 # ---------- I. Resistência (lâminas 54–74) ----------
 au("mdr", "An MDR bacterium is nonsusceptible to at least one drug in {{c1::at least three}} antimicrobial categories", {1: Z}, I_,
    "MDR", "55; guia de veteranos", "central", "sem card.", RES, "Azul: lâmina 55."),
 au("xdr", "An XDR bacterium remains susceptible to drugs in only {{c1::1–2}} antimicrobial categories", {1: R}, I_,
    "XDR", "55; guia de veteranos", "lateral", "sem card.", RES, "Rosa: lâmina 55.", extra="- Pan-resistant bacteria resist every available drug"),
 au("pressao-seletiva", "Antibiotic overuse selects resistant bacteria through {{c1::natural}} selection", {1: V}, I_,
    "Pressão seletiva", "60; monitoria; guia", "central", "sem card.", RES, "Verde: lâmina 60.",
    extra="- Hospitals, crowded animal farms and disinfectant excess favor it"),
 au("adquirida", "Acquired resistance arises through chromosomal {{c1::mutation}} or horizontal gene transfer", {1: Z}, I_,
    "Resistência adquirida", "60, 62–65", "central", "sem card.", RES, "Azul: lâminas 60–65."),
 ak("blactamase-pbp", 1503602269788, {1: V}, I_, "Resistência a penicilinas: β-lactamase ou PBP", 56, "Verde: HY 1; lâmina 56."),
 ak("mrsa-pbp", 1484873258290, {1: V}, I_, "MRSA altera as PBPs", 64, "Verde: HY 1; lâmina 64."),
 au("meca", "MRSA carries the {{c1::mecA}} gene, which encodes PBP2a, a penicillin-binding protein with low affinity for β-lactams", {1: V}, I_,
    "mecA e PBP2a", "64; prova 2024 P2 1.9", "prova", "AnKing não nomeia mecA.", RES, "Verde: prova 2024."),
 au("pbp-gram-pos", "Altered penicillin-binding proteins are the main β-lactam resistance mechanism of {{c1::Gram-positive}} bacteria", {1: Z}, I_,
    "PBP alterada em Gram-positivos", "63; monitoria", "central", "sem card.", RES, "Azul: lâmina 63.",
    extra="- Gram-negative bacteria rely mostly on β-lactamases"),
 au("blactamase-gram-neg", "{{c1::β-lactamase}} production is the main β-lactam resistance mechanism of Gram-negative bacteria", {1: Z}, I_,
    "β-lactamase em Gram-negativos", "66; monitoria", "central", "sem card.", RES, "Azul: lâmina 66.", extra="- Often encoded on plasmids and shared by conjugation",
    duplicacao_ok="ganho: liga β-lactamase ao Gram-negativo; blactamase-pbp lista os dois mecanismos"),
 ak("vre-dlac", 1485883313550, {1: V}, I_, "VRE troca D-ala-D-ala por D-ala-D-lac", 69, "Verde: HY 1; resistência à vancomicina (lâmina 69)."),
 au("esbl", "Extended-spectrum β-lactamases (ESBL), such as CTX-M, hydrolyze cephalosporins but spare {{c1::carbapenems}}", {1: Z}, I_,
    "ESBL e CTX-M", "72; turma 30", "central", "AnKing só cita ESBL como indicação de carbapenêmico.", RES, "Azul: lâmina 72.", duplicacao_ok="ganho: ESBL e CTX-M; carbapenem-esbl cobra a classe de droga"),
 au("carbapenemase", "KPC, NDM and OXA are {{c1::carbapenemases}}, which hydrolyze even last-resort β-lactams", {1: Z}, I_,
    "Carbapenemases", "72", "central", "sem card.", RES, "Azul: lâmina 72 (grupo crítico da OMS)."),
 ak("porina", 1489093323901, {1: V}, I_, "Gram-negativos reduzem porinas", 67, "Verde: HY 2; lâmina 67."),
 au("oprd", "Loss or modification of the porin {{c1::OprD}} makes the outer membrane of <i>Pseudomonas</i> impermeable to carbapenems", {1: R}, I_,
    "Impermeabilidade por perda de OprD", "56, 67", "lateral", "sem card.", RES, "Rosa: lâmina 56."),
 ak("efluxo-tetra", 1505670365051, {1: Z}, I_, "Bomba de efluxo (tetraciclinas)", 68, "Azul: HY 3; lâmina 68."),
 au("mexab", "In <i>Pseudomonas aeruginosa</i>, the {{c1::MexAB-OprM}} efflux pump expels several classes of antibiotics", {1: R}, I_,
    "MexAB-OprM", "56, 68", "lateral", "sem card.", RES, "Rosa: lâmina 56."),
 au("biofilme", "A biofilm matrix on catheters shields bacteria from {{c1::macrophages}} and antibiotics", {1: Z}, I_,
    "Biofilme", "56–59; monitoria", "central", "AnKing só cita biofilme de estafilococo.", RES, "Azul: lâminas 57–59."),
 au("conjugacao", "Resistance genes on {{c1::plasmids}} spread between bacteria by conjugation", {1: V}, I_,
    "Plasmídeos e conjugação", "65; prova 2017 P1 3.3; monitoria", "prova", "sem card do plasmídeo de resistência.", RES, "Verde: prova 2017.",
    extra="- Transformation (free DNA) and transduction (phages) are the other routes"),
 au("mcr", "Plasmid-borne {{c1::mcr}} genes make colistin ineffective by modifying the LPS", {1: Z}, I_,
    "Resistência a colistina por mcr", "56, 69", "central", "sem card.", RES, "Azul: lâminas 56 e 69.",
    extra="- Described in 2015, decades after colistin was introduced in 1949"),
 au("saude-unica", "In the One Health view, resistant bacteria circulate between humans, animals and the {{c1::environment}}", {1: R}, I_,
    "Saúde única", "7, 71–74", "lateral", "sem card.", RES, "Rosa: lâminas 71–74."),
 au("resistencia-rapida", "Resistance to penicillin emerged only {{c1::three}} years after its clinical use began, in 1945", {1: R}, I_,
    "Linha do tempo", "69", "lateral", "sem card.", RES, "Rosa: tabela da lâmina 69."),
 # ---------- J. Antibiograma (lâminas 75–99) ----------
 au("objetivo-abg", "The antibiogram aims to predict in {{c1::vitro}} what will happen in vivo", {1: V}, J_,
    "Objetivo do antibiograma", "76; turma 62", "central", "sem card.", RES, "Verde: lâmina 76.", extra="- It guides therapy and monitors resistance epidemiology"),
 ak("cim", 1489091253860, {1: V}, J_, "CIM", 80, "Verde: HY 3; prova 2025 P2 1.3–1.5."),
 au("cim-leitura", "A strain is considered susceptible when its MIC is {{c1::below}} the breakpoint set for that antibiotic", {1: V}, J_,
    "Interpretar a CIM", "77, 80; prova 2025 P2 1.3, 2024 P2 1.8", "prova", "sem card.", RES, "Verde: provas 2024 e 2025.",
    extra="- The lower the MIC, the more active the drug"),
 au("cbm", "The minimum bactericidal concentration (MBC) is the lowest antibiotic concentration that {{c1::kills}} the microorganism", {1: Z}, J_,
    "CBM", "87; turma 77; guia", "central", "sem card.", RES, "Azul: lâmina 87.", extra="- Obtained by subculturing the clear tubes of a MIC dilution series"),
 au("cmax", "To be effective, the blood concentration of an antibiotic should reach {{c1::4–8}} times its MIC", {1: R}, J_,
    "Cmax × CIM", "81; turma 76", "lateral", "sem card.", RES, "Rosa: lâmina 81.", extra="- In cerebrospinal fluid, about 10 times"),
 au("diluicao", "Broth dilution tests use {{c1::two-fold}} serial dilutions of the antibiotic in Mueller-Hinton broth", {1: R}, J_,
    "Diluição em caldo", "79–80; turma 67–68", "lateral", "sem card.", RES, "Rosa: lâminas 79–80."),
 au("mcfarland", "The antibiogram inoculum is adjusted to the {{c1::0.5 McFarland}} turbidity standard", {1: R}, J_,
    "Padronização do inóculo", "79; turma 69–70, 101", "lateral", "sem card.", RES, "Rosa: turma."),
 au("etest", "The E-test strip carries an antibiotic gradient and gives a {{c1::quantitative}} MIC on agar", {1: Z}, J_,
    "E-test", "82; turma 90", "central", "sem card.", RES, "Azul: lâmina 82.", extra="- Flexible and good for fastidious bacteria, but costly"),
 au("disco", "In the Kirby-Bauer test, the {{c1::diameter}} of the inhibition halo around each antibiotic disk defines susceptibility", {1: V}, J_,
    "Disco-difusão", "88; monitoria; guia", "central", "sem card.", RES, "Verde: lâmina 88 e monitoria.", extra="- Measured in millimeters after 18–24 h at 35 °C"),
 au("halo-maior", "For the same antibiotic under standardized conditions, a {{c1::larger}} inhibition halo generally indicates greater in-vitro susceptibility", {1: Z}, J_,
    "Halo maior, mais sensível", "88, 97; prova 2023 P2 1.11", "prova", "sem card.", RES, "Azul: prova 2023.", extra="- Interpret each diameter using organism- and drug-specific breakpoints; a lower MIC generally indicates greater susceptibility"),
 au("intermediario", "An intermediate susceptibility result may still support treatment when antibiotic {{c1::exposure is increased}}", {1: R}, J_,
    "Intermediário", "93; turma 121", "lateral", "sem card.", RES, "Rosa: lâmina 93."),
 au("duplo-halo", "With a double inhibition halo on the plate, one measures the {{c1::inner}} diameter", {1: R}, J_,
    "Duplo halo", "95; turma 122", "lateral", "sem card.", RES, "Rosa: turma."),
 au("colonia-satelite", "Satellite colonies or a mixed culture on the plate call for repeating the test from an {{c1::isolated}} colony", {1: Z}, J_,
    "Critérios de qualidade", "96; turma 123", "central", "sem card.", RES, "Azul: lâmina 96."),
 au("gram-empirico", "While culture and antibiogram take days, a Gram stain of the specimen already allows an {{c1::empirical}} antibiotic choice", {1: V}, J_,
    "Gram guia o empírico", "4; guia; prova 2023 P2 1.5, 2019 P1 1.5", "prova", "sem card.", RES, "Verde: provas 2019 e 2023.",
    extra="- The choice is adjusted after culture and antibiogram"),
 au("grupo-a", "In antibiogram reports, group {{c1::A}} antibiotics are the first-line agents tested and routinely reported", {1: R}, J_,
    "Grupos A, B e C", "91–92; turma 113", "lateral", "sem card.", RES, "Rosa: lâminas 91–92."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
 'saude-unica': '- Hence the focus on antibiotic use in agriculture and sanitation',
 'avibactam': '- It does not inhibit metallo-β-lactamases such as NDM',
 'vanco-vs-blac': '- β-lactamases cannot hydrolyze vancomycin',
 'carbapenem-ultimo': '- They resist hydrolysis by most β-lactamases',
 'aztreonam': '- ESBL and KPC enzymes still hydrolyze it',
 'vanco-gram-pos': '- Glycopeptides include vancomycin and teicoplanin',
 'macrolideo-gram': '- Azithromycin and erythromycin',
 'sulfa-seletiva': '- Bacteria must synthesize folate',
 'mdr': '- Resistant classes are counted, not individual drugs',
 'xdr': '- This counts active antimicrobial categories, not individual antibiotics',
 'oprd': '- OprD normally admits carbapenems',
 'mexab': '- Efflux also lowers intracellular drug concentration',
 'biofilme': '- Matrix of exopolysaccharides forms on abiotic and biotic surfaces',
 'adquirida': '- Intrinsic resistance, by contrast, is a trait of the species',
 'quin-resist': '- Also parC (topoisomerase IV) mutations',
 'meca': '- Carried on a mobile genetic element, the SCCmec cassette',
 'resistencia-rapida': '- Vancomycin resistance took 27 years to appear',
 'esbl': '- Often plasmid-encoded and found in <i>Escherichia coli</i> and <i>Klebsiella</i>',
 'carbapenemase': '- Carbapenem-resistant bacteria are in the WHO critical priority group',
 'diluicao': '- The MIC is read at the first clear tube',
 'mcfarland': '- About 10<sup>8</sup> CFU/mL',
 'grupo-a': '- Groups B and C are tested and reported selectively',
 'intermediario': '- Increased exposure may come from dosing or high concentration at the infection site',
 'duplo-halo': '- The inner halo is the one read',
 'colonia-satelite': '- Heteroresistance may also explain odd halos',
 'associacao-tb': '- Different mechanisms of action are combined',
 'tox-bebe-cinzento': '- Chloramphenicol: a classic side effect in preterm infants',
 'tox-dentes': '- Avoided in pregnancy and in children',
 'tox-oto-nefro': '- Worsened by loop diuretics',
 'blac-pbp': '- PBPs are the transpeptidases that cross-link peptidoglycan',
 'blac-dala': '- The antibiotic acts as a false substrate',
 'blac-cida': '- Death follows wall weakening and osmotic lysis',
 'osmolise': '- Autolysins also help to degrade the wall',
 'aminopenicilina': '- Ampicillin and amoxicillin, with a spectrum reaching some Gram-negatives',
 'antiestafilo': '- Oxacillin, nafcillin and dicloxacillin',
 'cefalo-blact': '- Hence their role against many penicillin-resistant bacteria',
 'ceftarolina': '- A fifth-generation cephalosporin with anti-MRSA activity',
 'carbapenem-esbl': '- Imipenem and meropenem are hydrolyzed by carbapenemases only',
 'inibidor-blac': '- Used with amoxicillin as amoxicillin-clavulanate',
 'vanco-dala': '- A glycopeptide that blocks transglycosylation and transpeptidation',
 'quin-girase': '- Gyrase and topoisomerase IV are essential for DNA replication',
 'mnemonico-30-50': '- Aminoglycosides and tetracyclines bind 30S; chloramphenicol, clindamycin, erythromycin and linezolid bind 50S',
 'macrolideo-50s': '- Erythromycin, clarithromycin and azithromycin',
 'aminoglicosideo-30s': '- Bactericidal, unlike most protein synthesis inhibitors',
 'aminoglicosideo-o2': '- Their uptake depends on oxygen-driven transport',
 'tetraciclina-30s': '- Reversible binding, so the effect is bacteriostatic',
 'tetraciclina-intra': '- They penetrate human cells',
 'polimixina-mdr': '- Colistin is polymyxin E',
 'daptomicina': '- A lipopeptide that depolarizes the cell membrane',
 'sulfa-paba': '- Competitive antagonism: PABA is the substrate',
 'sulfa-kernicterus': '- Displace bilirubin from albumin',
 'blactamase-pbp': '- Two routes: destroy the drug or change its target',
 'mrsa-pbp': '- Cross-resistant to all β-lactams except ceftaroline',
 'vre-dlac': '- Vancomycin no longer binds the altered terminal',
 'porina': '- Fewer porins means less drug entry',
 'efluxo-tetra': '- Efflux is a common route of multidrug resistance',
 'cim': '- Expressed in µg/mL',
}
VERSO = {k: v for k, v in VERSO.items() if v}
DUPLICACAO = {}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]

# Segunda leitura científica: o slide é direção de estudo, mas seus absolutos
# farmacológicos não devem virar uma regra falsa para decorar.
SCIENTIFIC_CORRECTIONS = {
 "cmax": {"text": "For concentration-dependent antibiotics, the ratio of peak drug concentration to MIC is called {{c1::Cmax/MIC}}",
          "extra": "- The slide's 4–8× blood and 10× CSF figures are not universal targets; PK/PD goals depend on drug, organism and site."},
 "cefalo-blact": {"text": "Cephalosporin stability against bacterial β-lactamases is {{c1::variable}} across drugs and enzymes",
                   "extra": "- ESBL and AmpC enzymes can hydrolyze many cephalosporins; interpret the isolate's susceptibility."},
 "aztreonam": {"text": "Aztreonam is stable to {{c1::metallo-β-lactamases}}, but co-produced serine β-lactamases may still inactivate it",
                "extra": "- Activity against an MBL producer requires susceptibility testing; ESBL or KPC coproduction can remove aztreonam activity.",
                "duplicacao_ok": "Ganho: distingue estabilidade do aztreonam frente a metalo-β-lactamases; AnKing só cobra β-lactamase como resistência à penicilina."},
 "cim-leitura": {"text": "An isolate is susceptible when its MIC {{c1::does not exceed}} the susceptible breakpoint for that organism–drug pair",
                 "extra": "- Equality with the susceptible breakpoint is included; compare MICs only within the relevant drug and breakpoint system."},
 "quin-resist": {"text": "Fluoroquinolone resistance can arise through mutation of {{c1::gyrA}} (DNA gyrase) or parC/grlA (topoisomerase IV)",
                 "extra": "- The dominant target varies with species and fluoroquinolone; efflux or reduced entry may add resistance."},
 "oprd": {"text": "In <i>Pseudomonas</i>, loss of the {{c1::OprD}} porin can reduce imipenem entry",
          "extra": "- Other carbapenems, including meropenem, may be affected differently and need individual susceptibility results."},
 "vanco-dala": {"text": "<b>Vancomycin</b> binds the {{c1::<b>D-alanyl-D-alanine</b>}} terminus of peptidoglycan precursors",
                "extra": "- Vancomycin binds the already formed D-Ala-D-Ala terminus of the precursor and obstructs peptidoglycan assembly; β-lactams bind PBPs."},
 "macrolideo-50s": {"text": "Macrolides bind 23S rRNA of the 50S ribosome and obstruct the peptide {{c1::exit tunnel}} during elongation",
                     "extra": '- Erythromycin, clarithromycin and azithromycin are examples.<br><img src="2cdae956a5f35cedc4314f0b7f46b1d8.png" width="976">'},
 "mcr": {"text": "Plasmid-borne {{c1::mcr}} genes encode enzymes that modify LPS and can confer colistin resistance",
         "extra": "- The phenotype depends on the allele and expression; confirm susceptibility by MIC testing."},
 "cida": {"text": "Bactericidal drugs may be favored for bacterial meningitis or severe infection in an {{c1::immunocompromised}} patient, depending on the pathogen and site",
          "extra": "- Bactericidal activity is measured in vitro; clinical cure still depends on exposure, infection site and host response."},
 "disco": {"text": "In the Kirby–Bauer test, the inhibition-zone {{c1::diameter}} is compared with organism–drug breakpoints to classify susceptibility",
           "extra": "- Measure in millimeters after standardized incubation; diameter alone is not a clinical category."},
 "selecao-toxicidade": {"text": "Antibiotics can have {{c1::selective}} toxicity by acting on bacterial features absent or sufficiently different in human cells",
                       "extra": "- Examples include the cell wall, bacterial ribosome, folate synthesis and DNA gyrase; selectivity is not absolute."},
 "tox-dentes": {"text": "Which antibiotic class may discolor developing teeth after relevant fetal or childhood exposure?<br><br>{{c1::Tetracyclines}}",
                "extra": "- Calcium binding explains tooth and bone deposition. Avoidance depends on agent, age and duration; short doxycycline courses and breastfeeding are not categorically forbidden."},
 "macrolideo-gram": {"text": "Macrolides classically favor {{c1::Gram-positive}} coverage, although azithromycin also acts on some Gram-negatives and atypical bacteria",
                      "extra": "- Spectrum depends on the molecule and organism; Gram-negative coverage cannot be inferred from the class name alone."},
 "meca": {"text": "Most MRSA strains carry {{c1::mecA}}, encoding the low-β-lactam-affinity PBP2a",
          "extra": "- mecA lies in SCCmec; mecC is a less common alternative."},
}
for c in CARDS:
    update = SCIENTIFIC_CORRECTIONS.get(c["key"])
    if update:
        c.update(update)
        if "extra" in update:
            c.pop("extra_add", None)
