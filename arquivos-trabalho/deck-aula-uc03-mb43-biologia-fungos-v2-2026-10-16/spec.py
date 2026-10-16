# Especificação curada — 43 Biologia geral dos fungos (UC03 P3, Microbiologia; Prof. Carlos P. Taborda; 61 lâminas). Refação v2 (F-20261016-CLAUDE-08):
# “excesso de autoral baboseira e falta do que importa”. Gerada a partir de inventario.py (escrito antes). Ordem = slides.
# AnKing → externos → autoral só para lacuna provada em busca/cobertura.tsv. Notas da corrida antiga que ficam entram por sh() (histórico preservado):
# as cópias de AnKing e os autorais que Davi elogiou ou corrigiu; o resto da aula antiga é retirado (nebli.retira, tag NEBLI::retirado::refacao-v2).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4  # 3 = teto de autoral (20%; 35% com AUTORAL_EXCECAO); 4 = todo AnKing das SECOES_DA_AULA entra ou é excluído com motivo
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ("Micologia geral quase não existe no AnKing (Step 1 cobra espécie): palavra-chave sem nota para sporangi*, basidi*, mycel*; "
                   "94 consultas por significado sem definição de hifa cenocítica, micélio, conídio, clamidoconídio, pleomorfismo. Davi autorizou até 30% (F-20261016-CLAUDE-09).")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb43-20261016a"
SHORT = "mb43"
LESSON = "2026-uc03-microbiologia-43-biologia-fungos"
DECK = "NEBLI::UC03::P3::Microbiologia::Biologia geral dos fungos"
CRITERIOS = "EXECUCAO-DECK-AULA (passos 0–7) + MEMORY §2–§8 + ANTI-EXEMPLARES + F-20261016-CLAUDE-04/06/08, 16/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (16/10): seções de recurso do AnKing (busca/secoes: Mycology, Fungi, Antifungal, Fungal — 78 seções); palavra-chave em AnKing "
         "e Referências Externas (busca/anking.txt); significado em todos os acervos e nos decks NEBLI vivos (busca/semantica.jsonl, 94 consultas). ")

EXCLUIDOS = [
 # seções da aula (antifúngicos por alvo; visão geral de fungos)
 (1509741919338, "alilaminas (terbinafina): lâmina 27 só traz equinocandinas, polienos, azóis e 5-FC; terbinafina é da aula 44 (tratamento de dermatófitos)"),
 (1509742310437, "griseofulvina: não está na lâmina 27; tratamento de dermatófitos, aula 44"),
 (1499975288531, "KOH e cultura no diagnóstico das micoses sistêmicas: aulas 50/55"),
 (1499975410107, "sorologia IgM das micoses sistêmicas: aula 50"),
 # candidatos lidos na busca e recusados
 (1517779391301, "aflatoxina e TP53: carcinogênese, aula de agentes carcinogênicos"),
 (1496159440092, "micróbios oncogênicos do CHC: aula de agentes carcinogênicos"),
 (1556238870116, "imagem de identificação de várias espécies (irmãos de outras micoses): aulas 44/50/55"),
 (1500244315193, "composição da cápsula do Cryptococcus: aula 50"),
 (1509743058195, "repete o fato de sh-1791557942183 (polienos ligam ergosterol e abrem poros)"),
 (1509742814980, "repete o fato de sh-1791557941207 (ergosterol na membrana)"),
 (1509751969962, "repete ak1509742717818 (equinocandina age na parede)"),
 (1500152000410, "queratinase dos dermatófitos: aula 44 (Davi: “card no deck errado”)"),
 (1500335727221, "Pneumocystis é fungo: não está nas lâminas; oportunistas, aula 50"),
 (1500234149130, "Candida com pseudo-hifas a 20 °C: repete sh-1791557943483; detalhe da aula 50"),
 (1716931103425, "repete o 80S de sh-1791557941506"),
 (1554561168711, "repete o 80S de sh-1791557941506"),
 (1556854709564, "glicogênio nos animais: biologia geral (UC01), não fala de fungos"),
 (1559146913373, "amido nas plantas: biologia geral (UC01)"),
 (1559146782371, "celulose nas plantas: biologia geral (UC01); o contraste está em sh-1791557940956"),
 (1500246419118, "ágar Sabouraud: prática de micologia, aula 55"),
 (1509744002911, "toxicidade renal da anfotericina: farmacologia clínica, fora do recorte (a lâmina só diz “toxicidade em mamíferos”)"),
 (1509743217032, "uso clínico da anfotericina: tratamento, fora do recorte"),
]
FORA_DO_RECORTE = [
 "Importância dos fungos (fermentação, queijos, penicilina, micorrizas, bioluminescência, decomposição) e curiosidades (edifícios doentes, nariz branco, anfíbios, dinossauros, Chernobyl): ilustração, sem card (MEMORY §3; ANTI-EXEMPLARES §4/§15).",
 "Toxicidades e usos clínicos dos antifúngicos (anfotericina renal, azóis e CYP450, griseofulvina, terbinafina): farmacologia clínica e aula 44.",
 "Taxonomia fina (Myxomycota, Dikarya, classificação de 2019, Mucoromycota/Zoopagomycota): só no Extra/Tab, sem card de acervo.",
]
A_, B_, C_, D_, E_, F_, G_, H_, I_, J_ = ("A-importancia", "B-classificacao", "C-macroscopia", "D-celula", "E-antifungicos", "F-taxonomia",
                                          "G-leveduras", "H-bolores", "I-sexuada", "J-nutricao")

CARDS = [
 # A. Fungos, vida humana e natureza (lâminas 2–16): só o que tem alvo
 ak("ak1499968803765", 1499968803765, "R-detalhe", A_, "Infecção grave em imunocomprometidos", 2, "monitoria, considerações iniciais (imunocomprometidos e infecção hospitalar)"),
 sh(1791557939905, "verde", A_, "Rhizopus, bolor do pão", 9, "V-hy: lâmina 9 (bolor do pão) e 44 (Rhizopus); nota viva da aula antiga, histórico mantido"),
 sh(1791557940256, "verde", A_, "Aflatoxina em grãos e castanhas", 10, "V-hy: lâmina 10 (micotoxinas); UC3.pdf p. 272"),
 ak("ak1486591290032", 1486591290032, "V-hy", A_, "Aflatoxina → carcinoma hepatocelular", 10, "lâmina 10; UC3.pdf cita esôfago, o AnKing corrige para fígado",
    extra_add="- Aflatoxin's classic cancer target is the liver, not the esophagus"),
 # B. Classificação (17–18)
 sh(1791557941081, "azul", B_, "Fungos são eucariontes", 18, "A-aula: lâmina 18 (árvore de Woese); apostila guia cap. 2"),
 # C. Macroscopia (19)
 sh(1792065024004, "verde", C_, "Levedura, bolor e dimórfico", 19, "V-pilar: lâminas 19 e 45; provas 2017/2018 (dimorfismo); autoral antigo mantido (organiza a aula)"),
 sh(1791557940633, "azul", C_, "Colônia de levedura × de bolor", 19, "A-aula: lâmina 19; apostila guia; autoral antigo corrigido por Davi em 14/10"),
 # D. Célula fúngica (20–26)
 sh(1791557940956, "verde", D_, "Parede de quitina e β-glucana", 20, "V-prova: lâminas 20–23; provas 2018 P2 1.3 e 2025 P3 1.2; autoral antigo mantido"),
 sh(1791576675592, "azul", D_, "DNA linear dos eucariontes", 22, "A-aula: lâmina 22 (cromossomo linear); prova 2017 (fungo × bactéria); nota viva da aula 26"),
 ak("ak1716930728791", 1716930728791, "R-detalhe", D_, "DNA no núcleo × nucleoide", 22, "lâmina 22 (núcleo com membrana); prova 2017 P2 2.5 (tipo de núcleo)", origin="MCAT"),
 ak("ak1716930924622", 1716930924622, "R-detalhe", D_, "Organelas com membrana", 22, "lâmina 22 (RE, mitocôndria, Golgi); prova 2017 P2 2.5 (mitocôndria)", origin="MCAT"),
 sh(1791557941506, "azul", D_, "Ribossomo 80S", 22, "A-aula: prova 2017 P2 2.5 (80S × 70S); nota viva da aula antiga"),
 sh(1791557941633, "verde", D_, "Cryptococcus: levedura com cápsula", 22, "V-hy: lâmina 22 (cápsula, Cryptococcus spp.); nota viva compartilhada com a aula 50"),
 sh(1791557941758, "azul", D_, "Cápsula antifagocitária", 22, "A-aula: lâmina 22; UC3.pdf p. 274 (cápsula modula a resposta imune); nota viva compartilhada com a aula 50"),
 sh(1791557941879, "verde", D_, "α-glucana na fase de levedura", 24, "V-prova: lâmina 24; prova 2025 P3 1.2; Trabulsi tab. 64.1.1; autoral antigo corrigido por Davi em 15/10"),
 sh(1791557941207, "verde", D_, "Ergosterol na membrana", 26, "V-hy: lâminas 22 e 26; apostila guia"),
 # E. Antifúngicos por alvo (27)
 sh(1792065031181, "verde", E_, "Antifúngicos por alvo", 27, "V-pilar: lâmina 27; autoral antigo elogiado por Davi (“BOM CARD!!!!! ajuda a organizar bem as ideias”)"),
 ak("ak1509753380809", 1509753380809, "V-hy", E_, "Polienos: anfotericina B e nistatina", 27, "lâmina 27 (polyenes such as amphotericin B)"),
 sh(1791557942183, "verde", E_, "Polienos ligam ergosterol e abrem poros", 27, "V-hy: lâmina 27"),
 ak("ak1509743161238", 1509743161238, "V-hy", E_, "Polienos: perda de eletrólitos", 27, "lâmina 27 (leakage of K+ and Na+)"),
 sh(1791557942482, "azul", E_, "Toxicidade da anfotericina: colesterol", 27, "A-aula: lâmina 27 (also confers mammalian toxicity)"),
 ak("ak1509742000812", 1509742000812, "V-hy", E_, "Azóis: 14α-desmetilase", 27, "lâmina 27 (azoles inhibit the enzyme that synthesizes ergosterol)"),
 sh(1791557942606, "verde", E_, "Azóis: lanosterol → ergosterol", 27, "V-hy: lâmina 27"),
 ak("ak1509741728595", 1509741728595, "V-hy", E_, "Síntese de ergosterol a partir do esqualeno", 27, "lâmina 27; seção FirstAid Antifungal therapy"),
 sh(1791557942007, "verde", E_, "Equinocandinas: β-glucana sintase", 27, "V-hy: lâmina 27 (inhibit the enzyme that synthesizes β-glucans)"),
 ak("ak1509742141238", 1509742141238, "V-hy", E_, "Equinocandinas inibem a β-glucana", 27, "lâmina 27"),
 ak("ak1509742717818", 1509742717818, "V-hy", E_, "Equinocandinas inibem a parede", 27, "lâmina 27 (“penicillin of antifungals”)"),
 sh(1791557942752, "azul", E_, "5-FC → 5-FU na célula fúngica", 27, "A-aula: lâmina 27 (5-FC is converted to 5-FU)"),
 ak("ak1509742443199", 1509742443199, "A-aula", E_, "Antifúngico convertido em 5-FU", 27, "lâmina 27"),
 ak("ak1509742489846", 1509742489846, "V-hy", E_, "5-FC inibe DNA/RNA", 27, "lâmina 27 (to inhibit DNA synthesis)"),
 ak("ak1509742586045", 1509742586045, "R-detalhe", E_, "Citosina desaminase", 27, "lâmina 27; HY 4"),
 sh(1791557942932, "verde", E_, "5-FC: mielossupressão", 27, "V-hy: lâmina 27 (side effect is myelosuppression)"),
 # F. Taxonomia (28–35)
 au("au-teleomorfo", "A fungus's <b>sexual stage</b> is its {{c1::teleomorph::teleomorph/anamorph}}, and its <b>asexual stage</b> is its {{c1::anamorph::teleomorph/anamorph}}",
    "A-aula", F_, "Fase teleomórfica × anamórfica", 30, "lâminas 30–31; UC3.pdf p. 275; Trabulsi 64.1",
    extra="- Once the sexual stage is found, its genus and species name takes priority<br>- Cryptococcus neoformans (anamorph) is Filobasidiella in its sexual stage",
    espelhos=(1509813157750, 1499971667817, 1500401344665)),
 # G. Leveduras (36–40)
 sh(1791575690369, "verde", G_, "Brotamento × fissão binária", 37, "V-prova: lâminas 37–39; prova 2017 P2 2.4 (brotamento); autoral antigo mantido"),
 sh(1791557943483, "azul", G_, "Candida: pseudo-hifas e brotamento", 39, "A-aula: lâminas 39–40 (pseudo-hifas na invasão por Candida)"),
 au("au-pseudohifa", "Yeast buds that elongate and stay attached in chains form {{c1::pseudohyphae}}, as in <b>Candida</b> invading tissue",
    "A-aula", G_, "Pseudo-hifa: brotos que não se separam", 40, "lâminas 37–40; UC3.pdf p. 277; Trabulsi fig. 64.1.4",
    extra="- True hyphae are tubes with parallel walls; pseudohyphae are chains of elongated buds, pinched at each junction",
    espelhos=(1557752615914, 1500234149130, 1500055361936)),
 au("au-clamidoconidio", "Round, thick-walled <b>resting cells</b> that fungi form under adverse conditions are {{c1::chlamydoconidia}}",
    "R-detalhe", G_, "Clamidoconídio: resistência", 37, "lâmina 37 (clamidoconídio); UC3.pdf p. 278; Trabulsi 64.1",
    extra="- They survive lack of nutrients, water or a bad temperature, like a resistance form; Candida albicans forms them on corn meal agar",
    espelhos=(1500234149130, 1500243540399, 1500234023725)),
 # H. Bolores (41–45)
 sh(1791575691218, "verde", H_, "Hifa cresce pela ponta", 42, "V-pilar: lâminas 41–42; monitoria; autoral antigo elogiado por Davi (“é isso que espero”)"),
 ak("ak1500238441939", 1500238441939, "V-hy", H_, "Aspergillus: hifa septada, ângulo agudo", 42, "lâmina 42 (Aspergillus); monitoria (hifas septadas)",
    extra_add="- Septa are cross-walls; hyphae without them (Mucor, Rhizopus) are coenocytic, with many nuclei in one cytoplasm"),
 ak("ak1500243882463", 1500243882463, "V-hy", H_, "Aspergillus só como bolor", 43, "lâmina 43 (conídios externos)",
    extra_add="- A mold grows as a mycelium: vegetative hyphae inside the substrate absorb food, aerial hyphae bear the spores"),
 sh(1791557943732, "verde", H_, "Aspergillus: conidióforos", 43, "V-hy: lâmina 43 (conidióforo, vesícula, conídio)"),
 sh(1791557944724, "verde", H_, "Mucor/Rhizopus: hifa sem septo", 44, "V-hy: lâmina 44 (Rhizopus, esporângio)"),
 sh(1791557944405, "verde", H_, "Paracoccidioides: dimorfismo térmico", 45, "V-prova: lâmina 45; provas 2018 P2 1.1 e 2017 P2 2.6"),
 sh(1791557944155, "verde", H_, "Bolor no solo, levedura no corpo", 45, "V-prova: lâmina 45; prova 2017 P2 2.6 (37 °C → levedura)"),
 ak("ak1500233665851", 1500233665851, "V-hy", H_, "Candida é dimórfica", 45, "lâminas 37–40 e 45; Trabulsi 64.3 (Candida inverte o dimorfismo)",
    extra_add="- Yeast buds that elongate without separating form pseudohyphae; thick-walled resting cells are chlamydoconidia"),
 ak("ak1500234258289", 1500234258289, "R-detalhe", H_, "Candida inverte o dimorfismo", 45, "Trabulsi 64.3: na Candida a forma de tecido é a filamentosa"),
 sh(1791630909466, "verde", H_, "Candida: tubo germinativo a 37 °C", 45, "V-hy: lâmina 45 (dimorfismo); nota viva da aula 50"),
 au("au-micelio-vegetativo-aereo", "The {{c1::vegetative::vegetative/aerial}} <b>mycelium</b> of a mold grows into the substrate, and the {{c1::aerial::vegetative/aerial}} mycelium bears spores",
    "A-aula", H_, "Micélio vegetativo × aéreo", 42, "apostila guia cap. 2; monitoria 2.1; UC3.pdf p. 276; Trabulsi 64.1",
    extra="- The aerial mycelium differentiates into reproductive structures, which are used to identify the species",
    espelhos=(1500243882463, 1500238441939, 1500334133616)),
 au("au-cenocitica", "<b>Hyphae</b> without cross-walls, with many nuclei sharing one cytoplasm, are {{c1::coenocytic}}",
    "A-aula", H_, "Hifa cenocítica", 44, "lâmina 48 (micélio cenocítico); monitoria 2.1; Trabulsi fig. 64.1.5",
    extra="- Mucor and Rhizopus (Mucoromycota) are coenocytic; Aspergillus and dermatophytes have septate hyphae",
    espelhos=(1500334133616, 1500238441939, 1557752933497)),
 au("au-conidio-esporangiosporo", "<b>Asexual spores</b> borne on a conidiophore are {{c1::conidia::conidia/sporangiospores}}, and those formed inside a sporangium are {{c1::sporangiospores::conidia/sporangiospores}}",
    "A-aula", H_, "Conídio × esporangiósporo", 43, "lâminas 43–44; material complementar p. 12; monitoria 3; Trabulsi quadro 64.1.2",
    extra="- Aspergillus and Penicillium make conidia; Rhizopus and Mucor release sporangiospores when the sporangium breaks",
    espelhos=(1500238914091, 1500333766310, 1500239016754)),
 au("au-pleomorfismo", "A change in <b>fungal form</b> that does <u>not</u> depend on temperature is {{c1::pleomorphism}}",
    "R-detalhe", H_, "Pleomorfismo × dimorfismo", 45, "monitoria 2.3; material complementar p. 27; Trabulsi 64.1/64.3",
    extra="- Old cultures, e.g. of dermatophytes, lose their conidia; dimorphism instead depends on temperature and is reversible",
    espelhos=(1499971667817, 1499970254984, 1500233665851)),
 # I. Reprodução sexuada e filos (46–53)
 au("au-reproducao-sexuada", ORG("Steps of <b>fungal sexual reproduction</b>, in order:<br>1. {{c1::Plasmogamy}} (fusion of cytoplasms)<br>"
                                 "2. {{c1::Karyogamy}} (fusion of nuclei)<br>3. {{c1::Meiosis}}, giving haploid sexual spores"),
    "A-aula", I_, "Plasmogamia → cariogamia → meiose", 46, "lâmina 46; apostila guia cap. 2; UC3.pdf p. 277; monitoria (esporos sexuais)",
    extra="- Between plasmogamy and karyogamy the two parental nuclei can coexist as a dikaryon (n + n)<br>"
          "- Sexual spore by phylum: zygospore (Mucoromycota), basidiospore (Basidiomycota), ascospore (Ascomycota)",
    espelhos=(1462935608373, 1462984495155, 1509813157750)),
 ak("ak1467833857831", 1467833857831, "V-hy", I_, "α-amanitina inibe a RNA polimerase II", 51, "lâmina 51 (Amanita, altamente venenosa)",
    extra_add="- Poisoning by eating a toxic mushroom is mycetism; by eating food with mold toxins, mycotoxicosis"),
 au("au-basidio-asco", "<b>Sexual spores</b> form outside a club-shaped cell in {{c1::Basidiomycota::Ascomycota/Basidiomycota}} and inside a sac in {{c1::Ascomycota::Ascomycota/Basidiomycota}}",
    "A-aula", I_, "Basidiósporo externo × ascósporo interno", 50, "lâminas 50 e 52; material complementar p. 12; Trabulsi 64.1",
    extra="- The club-shaped cell is the basidium; the sac is the ascus, usually with eight ascospores<br>- Mushrooms are basidiomycetes; most medically important fungi are in these two phyla",
    espelhos=(1500238914091, 1509813157750, 1462935608373)),
 # J. Ecologia e nutrição (54–61)
 au("au-absorcao", "<b>Fungi</b> digest food outside the cell with secreted {{c1::exoenzymes}}, then absorb the small molecules",
    "A-aula", J_, "Nutrição por absorção", 56, "lâmina 56 (nutrição por absorção/osmotrofia); apostila guia cap. 3; Trabulsi 64.3",
    extra="- Lipases, proteinases, lactases and keratinases break macromolecules into pieces that cross the membrane",
    espelhos=(1500152000410, 1500401344665, 1476583926797)),
 au("au-mesofilos", "Most <b>medically important fungi</b> are {{c1::mesophiles}}, growing best at 20–30 °C",
    "A-aula", J_, "Mesófilos", 58, "lâmina 58; apostila guia cap. 3; prova 2018 P2 1.4",
    extra="- Psychrophiles prefer cold and thermophiles heat; dimorphic fungi switch to yeast at 35–37 °C",
    espelhos=(1500234149130, 1499970409878, 1499970254984)),
 au("au-fatores-ambientais", ORG("Main <b>environmental factors</b> that control fungal growth:<br>1. {{c1::Temperature}}<br>"
                                 "2. Air {{c1::humidity}} (water activity)<br>3. {{c1::pH}}"),
    "A-aula", J_, "Temperatura, umidade e pH", 58, "lâminas 58–60; prova 2018 P2 1.4 (três fatores ambientais)",
    extra="- Below a water activity of about 0.65 fungi stop growing<br>- Optimal pH is about 6.5 (yeasts 2.5–8.5, molds 1.5–11)",
    espelhos=(1499970254984, 1500050370771, 1500234829361)),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1499968803765": "- Healthy innate immunity clears most fungi; invasive mycoses exploit neutropenia, steroids, AIDS and hospital devices",
 "ak1509753380809": "- Polyenes target ergosterol, the sterol that replaces cholesterol in fungal membranes",
 "ak1509743161238": "- The pores let K⁺ and Na⁺ leak out, so the fungal cell dies",
 "ak1509742000812": "- Without 14α-demethylase, lanosterol is not turned into ergosterol and the membrane fails",
 "ak1509741728595": "- Allylamines block an earlier step (squalene epoxidase); azoles block 14α-demethylase",
 "ak1509742141238": "- β-glucan is a wall polysaccharide human cells lack, so the drug is selective",
 "ak1509742717818": "- Like penicillin in bacteria, they hit a wall that human cells do not have",
 "ak1509742443199": "- Fungal cytosine deaminase makes 5-FU inside the fungus; human cells lack the enzyme",
 "ak1509742489846": "- 5-FU is incorporated into RNA and its metabolite blocks thymidylate synthase, stopping DNA synthesis",
 "ak1509742586045": "- Human cells lack cytosine deaminase, which is why flucytosine is selective",
 "ak1500234258289": "- Most dimorphic fungi are molds outside and yeasts in tissue; Candida is the reverse",
 "ak1716930728791": "- Fungi, as eukaryotes, keep their linear chromosomes inside a nuclear envelope",
 "ak1716930924622": "- Fungal cells have mitochondria, ER and Golgi; bacteria have none of these organelles",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {"a4f1e75a5b1491196418ea0abb030230.webp": "Extra dos dois cards MCAT: célula eucariótica × procariótica rotulada (núcleo com membrana, mitocôndria, ribossomos × nucleoide); nítida, no verso, ensina a diferença que a prova 2017 cobra"}
REVISAO = {
 "despejo": "Despejo lido inteiro (21 notas novas) e as 27 notas mantidas relidas no Anki: frentes completas, clozes certos, dica de 1ª letra nos organizadores de 3 itens, versos com porquê, cores pela rubrica. Corrigido: metatexto no verso da aflatoxina.",
 "corrigidos": ["ak1486591290032"],
}
ESCOPO = {
 "objetivo": "Entender o que é um fungo (eucarionte heterotrófico, parede de quitina/glucana, ergosterol), suas formas (levedura, bolor, dimórfico), "
             "como se reproduz (brotamento, hifas e conídios, ciclo sexual), como se classifica e o que controla seu crescimento, e como os antifúngicos exploram essas diferenças.",
 "centrais": [
   ("formas e dimorfismo", "sh-1792065024004", "sh-1791557944405", "sh-1791557944155"),
   ("célula fúngica: parede e membrana", "sh-1791557940956", "sh-1791557941879", "sh-1791557941207"),
   ("antifúngicos exploram parede e ergosterol", "sh-1792065031181", "ak1509753380809", "ak1509742000812"),
   ("reprodução assexuada das leveduras", "sh-1791575690369"),
   ("crescimento dos bolores", "sh-1791575691218"),
   ("fatores de crescimento", "au-fatores-ambientais"),
 ],
 "exemplos": ["fermentação (pão, cerveja)", "queijos e cogumelos", "penicilina do Penicillium", "micorrizas e líquens", "edifícios doentes",
              "quitrídios, nariz branco, Chernobyl (melanina)", "Pilobolus, Geastrum, Pezizaceae"],
 "outras_aulas": ["44 Micoses cutâneas (terbinafina, griseofulvina, queratinase)", "50 Micoses sistêmicas (Cryptococcus, Histoplasma, Paracoccidioides em detalhe)",
                  "55 Prática de micologia (Sabouraud, identificação)", "Agentes carcinogênicos biológicos (aflatoxina e TP53)"],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
