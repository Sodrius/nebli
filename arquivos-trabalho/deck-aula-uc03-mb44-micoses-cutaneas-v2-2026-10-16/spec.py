# Especificação curada — 44 Micoses superficiais e cutâneas (UC03 P3, Microbiologia; Prof. Benedito Corrêa, lâminas 2026; 55 lâminas).
# Refação v2 (F-20261016-CLAUDE-08/09): AnKing primeiro; cópias NEBLI vivas por sh() (acervo()); autorais antigos só os corrigidos/elogiados por Davi
# ou cobrados; escopo de micoses pelo Trabulsi (cap. 66: superficiais estritas, dermatofitoses, não dermatófitos, leveduroses); as que não estão
# nas lâminas (tinha negra, piedras, onicomicose por não dermatófito) com cobertura mínima (organizador antigo). Ordem = slides.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ("Classificação das micoses, habitat e fontes dos dermatófitos, fatores de virulência, ecto/endotrix e as micoses superficiais estritas "
                   "não têm card no AnKing (busca nos três caminhos em busca/); Davi autorizou até 30% na Micro P3 (F-20261016-CLAUDE-09).")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb44-20261016a"
SHORT = "mb44"
LESSON = "2026-uc03-microbiologia-44-micoses-cutaneas"
DECK = "NEBLI::UC03::P3::Microbiologia::Micoses superficiais e cutâneas"
CRITERIOS = "EXECUCAO-DECK-AULA (passos 0–7) + MEMORY §2–§8 + ANTI-EXEMPLARES + F-20261016-CLAUDE-08/09, 16/10/2026"
MEDIA = {"mb44-microsporum-canis-macroconidios.png": "img/mb44-microsporum-canis-macroconidios.png"}
BUSCA = ("Três caminhos (16/10): seções de recurso (busca/secoes: Cutaneous, Dermatophyt, Malassezia, Tinea, Candida, Skin_Infections); palavra-chave "
         "(busca/anking.txt); significado em todos os acervos e decks NEBLI vivos (busca/semantica.jsonl). ")
A = lambda nid, cod, bloco, alvo, slide, motivo, **kw: acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)

EXCLUIDOS = [
 (1500053847214, "efeito adverso da griseofulvina (GI): farmacologia clínica, fora do recorte"),
 (1556238897815, "imagem de identificação de várias espécies (irmãos de outras micoses): aula 55 / outras aulas"),
 (1500054719314, "esporotricose: aula 48 (micoses subcutâneas)"),
 (1500055367426, "esporotricose: aula 48"),
 (1500055544157, "esporotricose: aula 48"),
 (1500151811249, "esporotricose: aula 48"),
 (1488680793140, "pseudofoliculite da barba: não é micose"),
 (1488680796722, "pseudofoliculite da barba: não é micose"),
 (1518567297527, "pitiríase rósea: não é micose"),
 (1548722722283, "repete 1500243739726 (corrimento em queijo cottage da candidíase vaginal)"),
 (1474580722813, "conduta (gargarejo após corticoide inalado): fora do recorte"),
 (1520458741002, "conduta na candidíase vulvovaginal recorrente: fora do recorte"),
 (1509745802661, "fluconazol na candidíase mucocutânea: tratamento sistêmico, aula 50"),
 (1500236922530, "candidíase disseminada: aula 50"),
 (1509751792392, "hepatotoxicidade da terbinafina: farmacologia clínica, fora do recorte"),
 (1500233417765, "Candida como principal oportunista: aula 50"),
]
FORA_DO_RECORTE = [
 "Identificação de espécies de dermatófito em cultura (N. gypsea, T. mentagrophytes, T. rubrum, E. floccosum), microcultivo e técnica do carpete: prática de micologia (aula 55); só o macroconídio do M. canis, com imagem, que Davi pediu.",
 "Candidíase sistêmica, esofágica e candidemia, e o tratamento sistêmico: aula 50.",
 "Epidemiologia em números (20–25% da população, 30–70% portadores, mapas de prevalência): sem card (§4).",
]
A_, B_, C_, D_, E_, F_, G_ = ("A-classificacao", "B-dermatofitos", "C-tinhas", "D-candida", "E-tinha-capitis", "F-diagnostico", "G-malassezia")
IMG = '<img src="mb44-microsporum-canis-macroconidios.png" width="300">'

CARDS = [
 # A. Classificação das micoses (lâminas 2–5)
 au("au-classificacao", ORG("Depth of the <b>mycosis</b> in each example:<br>1. Sporotrichosis: {{c1::subcutaneous}}<br>2. Pityriasis versicolor: {{c1::superficial}}<br>"
                            "3. Histoplasmosis: {{c1::systemic}}<br>4. Dermatophytosis: {{c1::cutaneous}}"),
    "V-pilar", A_, "Classificação por profundidade", 3, "lâminas 3–4; apostila guia cap. 1; Trabulsi cap. 66",
    extra="- Superficial: outer stratum corneum and hair surface; cutaneous: keratin of skin, hair and nails; subcutaneous: implanted by trauma; systemic: inhaled, reaches organs<br>"
          "- Out of depth order on purpose, so the disease, not the list position, recalls the class",
    espelhos=(1500233417765, 1500052207462, 1500051183614)),
 sh(1792064698883, "verde", A_, "Superficial × cutânea", 5, "V-prova: lâmina 5; prova 2025 P3 4.4 (patogenia das superficiais); autoral antigo mantido"),
 sh(1792064618158, "azul", A_, "Principais micoses superficiais e agentes", 5, "A-aula: lâmina 5; Trabulsi cap. 66 (superficiais estritas): cobertura mínima de tinha negra e piedras"),
 sh(1792064618759, "azul", A_, "Principais micoses cutâneas", 5, "A-aula: lâmina 5; Trabulsi cap. 66 (dermatofitoses, leveduroses, não dermatófitos)"),
 # B. Dermatófitos: definição, habitat, fontes, localização, virulência, patogenia (5–13)
 A(1500051969973, "A-aula", B_, "Dermatófitos → tinha", 5, "lâmina 5 (dermatofitose)"),
 A(1500052444077, "A-aula", B_, "Tinha = ringworm", 5, "lâmina 5"),
 A(1500052207462, "A-aula", B_, "Dermatófitos na pele", 5, "lâmina 5"),
 A(1500052358184, "V-pilar", B_, "Os três gêneros de dermatófitos", 3, "lâmina 3; prova 2019 P2 3.1 (gêneros); UC3.pdf “saber os 3 gêneros”"),
 sh(1791626776803, "verde", B_, "Dermatófitos não passam do estrato córneo", 6, "V-prova: lâminas 6 e 12; prova 2025 P3 4.4; autoral antigo com imagem elogiada por Davi"),
 sh(1791626775626, "verde", B_, "Geofílico, zoofílico, antropofílico", 8, "V-prova: lâmina 8; objetivo da aula; prova 2019 P2 3.1 (fontes); autoral antigo mantido"),
 A(1500052841281, "A-aula", B_, "Animais como fonte", 9, "lâmina 9 (transmissão direta); prova 2019 P2 3.1"),
 sh(1791626776127, "azul", B_, "Fômites", 9, "A-aula: lâmina 9 (transmissão indireta); prova 2019 P2 3.1; autoral antigo mantido"),
 A(1500052763799, "R-detalhe", B_, "Atletas", 9, "lâmina 9; apostila (colchões de judô, pisos de banheiro)"),
 sh(1791626776253, "verde", B_, "Gênero × pele/pelo/unha", 10, "V-pilar: lâmina 10; objetivo da aula; tabela ajustada por Davi em 15/10"),
 A(1500152000410, "A-aula", B_, "Queratinase", 11, "lâmina 11 (fatores de virulência); prova 2025 P3 4.4 (queratinólise)"),
 sh(1791626776427, "azul", B_, "Elastases, colagenase, DNase", 11, "A-aula: lâmina 11; objetivo da aula; autoral antigo mantido"),
 sh(1791626776553, "azul", B_, "Inoculação de artroconídios", 12, "A-aula: lâmina 12; apostila; Taborda 2020 p. 21; autoral antigo mantido"),
 A(1669737153829, "A-aula", B_, "Imunossuprimido: tinha extensa", 13, "lâmina 13 (fatores do hospedeiro); prova 2025 P3 4.4 (imunossupressão)"),
 # C. Tinhas (14–26)
 A(1500052605836, "A-aula", C_, "Tinha do corpo", 14, "lâminas 14–15"),
 A(1505160761819, "R-detalhe", C_, "Tinha do corpo (imagem)", 14, "lâminas 14–15"),
 A(1516587677463, "R-detalhe", C_, "Borda ativa, centro claro", 14, "lâminas 14–15 (lesão circular, crescimento centrífugo)"),
 A(1582144175845, "R-detalhe", C_, "Tinha do corpo (imagem)", 15, "lâmina 15"),
 A(1500052912297, "A-aula", C_, "Prurido", 14, "lâminas 14–21"),
 sh(1791626777678, "azul", C_, "Pé de atleta = tinha do pé", 16, "A-aula: lâminas 16 e 18; autoral antigo mantido"),
 A(1581260145423, "R-detalhe", C_, "Tinha do pé → celulite", 18, "lâmina 18"),
 A(1500052626060, "A-aula", C_, "Tinha crural", 19, "lâminas 19–20"),
 A(1555800414777, "R-detalhe", C_, "Autoinfecção: crural a partir do pé", 19, "lâminas 18–20"),
 A(1692574789340, "R-detalhe", C_, "Crural recorrente: procurar outros focos", 20, "lâminas 18–20"),
 sh(1791626778303, "azul", C_, "T. indotineae resiste à terbinafina", 22, "A-aula: lâmina 22 (dermatofitose emergente, mutação SQLE); autoral antigo mantido"),
 A(1509741919338, "V-hy", C_, "Alilaminas: esqualeno epoxidase", 22, "lâmina 22 (alvo da terbinafina)"),
 A(1509741728595, "V-hy", C_, "Azóis e alilaminas: síntese de ergosterol", 22, "lâmina 22; nota da aula 43"),
 A(1500053322321, "V-hy", C_, "Tinha localizada: antifúngico tópico", 22, "lâmina 22; tratamento ligado ao alvo da terbinafina"),
 A(1509746577022, "V-hy", C_, "Azóis tópicos na tinha", 22, "lâmina 22"),
 A(1500053449197, "V-hy", C_, "Terbinafina oral: onicomicose e capitis", 22, "lâmina 22"),
 A(1543421392197, "A-step", C_, "Capitis e onicomicose pedem via oral", 22, "lâmina 22; Bootcamp"),
 A(1509751339127, "V-hy", C_, "Terbinafina é fungicida", 22, "lâmina 22"),
 A(1509751239610, "V-hy", C_, "Griseofulvina é fungistática", 22, "lâmina 22"),
 A(1500053600334, "V-hy", C_, "Griseofulvina oral nas formas graves", 22, "lâmina 22"),
 A(1500053746842, "V-hy", C_, "Griseofulvina se deposita na queratina", 22, "lâmina 22; aula 43 deixou a griseofulvina para cá"),
 A(1509742310437, "V-hy", C_, "Griseofulvina: fuso mitótico", 22, "lâmina 22"),
 A(1509750504912, "V-hy", C_, "Griseofulvina: microtúbulos", 22, "lâmina 22"),
 A(1509751441530, "V-hy", C_, "Alilaminas acumulam esqualeno", 22, "lâmina 22 (alvo da terbinafina)"),
 A(1509751663968, "V-hy", C_, "Sufixo -fina das alilaminas", 22, "lâmina 22"),
 A(1509751158016, "V-hy", C_, "Capitis infantil: griseofulvina ou terbinafina oral", 30, "lâmina 30"),
 A(1509747453719, "A-step", C_, "Griseofulvina nas dermatofitoses superficiais", 22, "lâmina 22"),
 sh(1791626778603, "azul", C_, "Dermatofítide", 23, "A-aula: lâmina 23; apostila e monitoria; autoral antigo mantido"),
 A(1500053417089, "V-hy", C_, "Onicomicose / tinha da unha", 24, "lâminas 24–26"),
 sh(1791626778904, "verde", C_, "Unha: distal (dermatófito) × proximal (Candida)", 25, "V-pilar: lâmina 25; apostila; ajustado por Davi em 15/10"),
 A(1546271297640, "R-detalhe", C_, "Onicomicose: KOH confirma", 26, "lâminas 26 e 37"),
 # D. Candidíase mucocutânea (27–29, 53–54)
 A(1500234684400, "V-hy", D_, "Candida na microbiota oral e GI", 28, "lâmina 28; apostila (fonte endógena)"),
 A(1500243661654, "V-hy", D_, "Sapinho: Candida albicans", 28, "lâmina 28 (estomatite cremosa ou sapinho)"),
 A(1500235087296, "V-hy", D_, "Placas brancas que se raspam", 28, "lâmina 28"),
 A(1500235281810, "R-detalhe", D_, "Leucoplasia não se raspa", 28, "lâmina 28 (contraste com o sapinho)"),
 A(1482191403303, "R-detalhe", D_, "Candidíase oral no imunocomprometido", 28, "lâmina 28"),
 A(1581365759971, "R-detalhe", D_, "Raspagem pode sangrar", 28, "lâmina 28"),
 A(1474580716506, "V-hy", D_, "Corticoide inalado → candidíase orofaríngea", 28, "lâmina 28; Trabulsi (corticoterapia predispõe)"),
 A(1500234954735, "V-hy", D_, "Imunocomprometido ou corticoide oral", 28, "lâmina 28; Trabulsi (fatores predisponentes)"),
 A(1502224452270, "A-aula", D_, "Deficiência de T → Candida superficial", 28, "Trabulsi: imunidade celular; nota viva compartilhada"),
 A(1517771826170, "V-hy", D_, "Candidíase mucocutânea crônica: IL-17/AIRE", 28, "Trabulsi (candidíase mucocutânea crônica)"),
 A(1500234829361, "V-hy", D_, "Dermatite da fralda por Candida", 29, "lâmina 29 (candidose cutânea); Trabulsi (umidade)"),
 A(1516590197504, "R-detalhe", D_, "Lesões satélites na fralda", 29, "lâmina 29"),
 A(1535402608704, "A-aula", D_, "Intertrigo submamário", 29, "lâmina 29; apostila (dobra submamária)"),
 A(1500235637454, "V-hy", D_, "Diabetes predispõe a Candida", 29, "lâmina 29; Trabulsi (doença de base)"),
 A(1500243739726, "V-hy", D_, "Candidíase vaginal", 29, "Trabulsi (leveduroses mucocutâneas); Taborda 2020 p. 53 (exame direto vaginal)"),
 A(1500235811939, "V-hy", D_, "Fármacos que predispõem à candidíase vaginal", 29, "Trabulsi (antibioticoterapia destrói a microbiota)"),
 A(1500236404263, "V-hy", D_, "pH vaginal > 4,5", 29, "Trabulsi (leveduroses)"),
 A(1500237000985, "V-hy", D_, "Candidíase local: azol tópico", 29, "lâmina 29"),
 A(1500237136393, "V-hy", D_, "Candidíase oral: nistatina", 28, "lâmina 28"),
 A(1509744422330, "V-hy", D_, "Nistatina age em Candida", 28, "lâmina 28"),
 A(1509744598051, "V-hy", D_, "Nistatina: oral e vaginal", 28, "lâmina 28"),
 # E. Tinha do couro cabeludo (30–31)
 A(1500152247775, "V-hy", E_, "Tinha capitis: crianças", 30, "lâmina 30"),
 A(1539532978728, "A-step", E_, "Capitis: T. tonsurans", 30, "lâmina 30 (Trichophyton tonsurans)"),
 A(1578250039053, "A-step", E_, "Placa de alopecia com pelos do mesmo tamanho", 30, "lâmina 30"),
 A(1516579288623, "R-detalhe", E_, "Pontos negros no couro cabeludo", 30, "lâmina 30"),
 A(1516579387663, "R-detalhe", E_, "Capitis em crianças afrodescendentes", 30, "lâmina 30"),
 sh(1791626779652, "azul", E_, "Capitis por M. canis (cães e gatos)", 31, "A-aula: lâminas 30–31; autoral antigo mantido"),
 # F. Diagnóstico (32–47)
 A(1500053129177, "R-detalhe", F_, "Lâmpada de Wood: Microsporum", 32, "lâmina 32 (diagnóstico); Trabulsi"),
 sh(1791626781378, "azul", F_, "Sabouraud com cicloheximida e cloranfenicol", 34, "A-aula: lâmina 34 (meios de isolamento); autoral antigo mantido"),
 A(1500052968870, "V-hy", F_, "KOH mostra hifas", 37, "lâminas 37–38 (KOH 10–40%)"),
 A(1557752933497, "A-aula", F_, "Hifas septadas ramificadas no KOH", 37, "lâmina 37 (hifas septadas hialinas)"),
 au("au-ecto-endotrix", "<b>Dermatophyte spores</b> coating the outside of the hair shaft form an {{c1::ectothrix::ectothrix/endothrix}} infection, and spores inside it an {{c1::endothrix::ectothrix/endothrix}} infection",
    "R-detalhe", F_, "Ectotrix × endotrix", 39, "lâminas 39–40 (pelo parasitado por Microsporum e Trichophyton); Trabulsi tab. 66.1",
    extra="- Microsporum canis is typically ectothrix; Trichophyton tonsurans is endothrix, giving the black-dot tinea capitis",
    espelhos=(1539532978728, 1578250039053, 1500053129177)),
 au("au-canis-macroconidio", f"Which dermatophyte forms the spindle-shaped, thick-walled <b>macroconidia</b> shown below?<br>{IMG}<br>{{{{c1::Microsporum canis}}}}",
    "R-detalhe", F_, "Macroconídio do M. canis", 43, "lâmina 43 (M. canis, microscopia); comentário de Davi pedindo imagem",
    extra="- Microsporum macroconidia are rough and thick-walled; Epidermophyton has club-shaped smooth macroconidia and no microconidia",
    espelhos=(1556238807061, 1500053129177, 1500238914091)),
 A(1500235321247, "V-hy", D_, "KOH no diagnóstico de candidíase", 53, "lâmina 53 (exame direto)"),
 A(1548722722826, "A-aula", D_, "Pseudo-hifas e brotamento no KOH: Candida", 53, "lâminas 53–54 (leveduras e/ou pseudo-hifas)"),
 # G. Pitiríase versicolor e Malassezia (48–52)
 A(1500050017109, "V-hy", G_, "Malassezia → pitiríase versicolor", 48, "lâmina 48"),
 A(1500050525224, "V-hy", G_, "Manchas hipo ou hiperpigmentadas", 49, "lâmina 49"),
 A(1500050773382, "V-hy", G_, "Tórax e dorso", 49, "lâmina 49"),
 A(1504829332498, "R-detalhe", G_, "Hipocromia após verão", 49, "lâminas 49–50"),
 A(1544385358722, "R-detalhe", G_, "Manchas após acampamento de verão", 49, "lâminas 49–50"),
 A(1584725712974, "R-detalhe", G_, "Pitiríase versicolor (imagem)", 49, "lâmina 49"),
 A(1500050370771, "V-hy", G_, "Malassezia da microbiota; calor e umidade", 50, "lâmina 50; Taborda 2020 p. 7"),
 A(1500050853067, "V-hy", G_, "Ácidos da degradação lipídica lesam melanócitos", 50, "lâmina 50; apostila (inibe a melanogênese)"),
 A(1500051071890, "V-hy", G_, "M. furfur produz ácidos que lesam melanócitos", 50, "lâmina 50"),
 A(1500051183614, "A-aula", G_, "Malassezia no estrato córneo", 50, "lâmina 5 (superficial)"),
 A(1517329278337, "A-step", G_, "Dermatite seborreica e Malassezia", 50, "Taborda 2020 p. 5; UC3.pdf; Trabulsi"),
 A(1500051342572, "R-detalhe", G_, "Malassezia no imunocomprometido", 50, "Taborda 2020 p. 5 (sepse); UC3.pdf"),
 A(1500051405360, "V-hy", G_, "Fungemia em neonato com NPT", 50, "Taborda 2020 (infecção sistêmica); levedura lipodependente"),
 A(1500051612651, "A-step", G_, "Lipofílica: risco na NPT", 50, "Taborda 2020 p. 7 (lipodependente)"),
 A(1500050268188, "V-hy", G_, "Espaguete com almôndegas no KOH", 51, "lâminas 51–52"),
 A(1517329530875, "R-detalhe", G_, "Dermatite seborreica: cetoconazol ou selênio", 50, "Taborda 2020 p. 5"),
 A(1500051897611, "V-hy", G_, "Sulfeto de selênio", 52, "lâmina 52; tratamento tópico (apostila)"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1500052444077": "- The name comes from the ring-shaped lesion that grows outward, not from a worm",
 "ak1500052207462": "- They live on keratin, so they stay in the dead outer layer of skin, hair and nails",
 "ak1669737153829": "- T cells and macrophages normally contain the fungus at the border; without them it spreads and recurs",
 "ak1500052605836": "- The lesion grows outward in a ring with an active, scaly border and clearer center",
 "ak1500052626060": "- Warm, moist groin skin favors the fungus; it often comes from the patient's own feet",
 "ak1500053322321": "- The fungus is confined to the stratum corneum, so a cream reaches it",
 "ak1509746577022": "- Azoles block ergosterol synthesis (14α-demethylase)",
 "ak1500053449197": "- Hair follicles and nails are out of reach of creams, so the drug must arrive through the blood",
 "ak1509751339127": "- Terbinafine blocks squalene epoxidase, and squalene accumulates to toxic levels",
 "ak1509751239610": "- Griseofulvin only stops mitosis, so the fungus is held back while new keratin grows out",
 "ak1500053600334": "- It reaches the new keratin from inside, through the blood",
 "ak1509750504912": "- Binding microtubules stops the mitotic spindle of the fungal cell",
 "ak1509747453719": "- It accumulates in newly formed keratin, where dermatophytes grow",
 "ak1500053417089": "- Dermatophytes enter at the distal nail edge, where the hyponychium is exposed",
 "ak1500234684400": "- Candidiasis is usually endogenous: the patient's own Candida overgrows when defenses fall",
 "ak1500235087296": "- Leukoplakia is epithelial and cannot be scraped; thrush is a fungal plaque on top",
 "ak1474580716506": "- Steroid deposited in the mouth suppresses local immunity",
 "ak1500234954735": "- Steroids reduce T-cell and phagocyte function at the mucosa",
 "ak1517771826170": "- Th17 cells and IL-17 recruit neutrophils that control Candida on skin and mucosa",
 "ak1500234829361": "- Moisture and occlusion soften the skin, and Candida adheres and invades",
 "ak1500235637454": "- Hyperglycemia feeds the yeast and impairs neutrophils",
 "ak1500243739726": "- Antibiotics, pregnancy, diabetes and steroids upset the vaginal flora",
 "ak1500236404263": "- Lactobacilli keep the vagina acidic; Candida grows at that normal acidic pH",
 "ak1500237000985": "- Local infection only needs a drug at the surface",
 "ak1500237136393": "- Nystatin is not absorbed from the gut, so it acts only on the mucosa",
 "ak1509744422330": "- Nystatin is a polyene: it binds ergosterol and opens pores",
 "ak1509744598051": "- Too toxic for systemic use, nystatin is used only topically",
 "ak1500152247775": "- After puberty, fatty acids in sebum protect the scalp",
 "ak1539532978728": "- Anthropophilic, passed between children by combs and contact",
 "ak1500053129177": "- Microsporum hair fluoresces green; Trichophyton tonsurans (endothrix) does not",
 "ak1500052968870": "- KOH dissolves keratin and leaves the fungal walls visible",
 "ak1500050525224": "- The patches do not tan, because the fungus's acids injure melanocytes",
 "ak1500050773382": "- These sites have many sebaceous glands, and Malassezia needs lipids",
 "ak1500050370771": "- It colonizes the skin from the first weeks of life and turns pathogenic in heat, humidity and oily skin",
 "ak1500050853067": "- Azelaic acid from skin lipids inhibits tyrosinase, so pigment drops",
 "ak1500051071890": "- The fungus breaks down skin lipids into dicarboxylic acids",
 "ak1500051183614": "- A superficial mycosis stays in the outermost dead layer and provokes almost no inflammation",
 "ak1500051405360": "- Lipid emulsions in parenteral nutrition feed this lipid-dependent yeast",
 "ak1500051897611": "- Shedding the stratum corneum removes the layer where the fungus lives",
 "ak1516587677463": "- The fungus spreads outward and the old center heals, leaving a ring",
 "ak1582144175845": "- Annular, scaly plaques with a raised border are the classic picture",
 "ak1581260145423": "- Cracked skin between the toes lets bacteria in",
 "ak1692574789340": "- Untreated feet or nails keep reseeding the groin",
 "ak1543421392197": "- Topical drugs do not reach the hair follicle or the nail plate",
 "ak1509742310437": "- It binds tubulin and stops the fungal mitotic spindle",
 "ak1509751441530": "- Blocking squalene epoxidase leaves toxic squalene in the cell and no ergosterol",
 "ak1509751663968": "- Terbinafine and naftifine are allylamines",
 "ak1509751158016": "- The fungus is inside the hair follicle, out of reach of creams",
 "ak1500235281810": "- Thrush is a removable fungal plaque; leukoplakia is thickened epithelium",
 "ak1482191403303": "- Low T-cell immunity lets oral Candida overgrow",
 "ak1581365759971": "- Scraping removes the plaque from inflamed mucosa underneath",
 "ak1516590197504": "- Satellite papules beyond the main plaque point to Candida rather than irritant dermatitis",
 "ak1516579288623": "- Hairs broken at the scalp surface by endothrix invasion look like black dots",
 "ak1516579387663": "- Trichophyton tonsurans, an endothrix species, predominates in this group",
 "ak1504829332498": "- Tanned skin around the patches makes the hypopigmentation visible after summer",
 "ak1544385358722": "- Heat and sweating favor Malassezia overgrowth",
 "ak1584725712974": "- Many small, scaly hypopigmented macules on the trunk",
 "ak1500051342572": "- Immunosuppression lets the commensal yeast cause folliculitis or invasive infection",
 "ak1500051612651": "- It needs lipids from outside, which intravenous lipid emulsions supply",
 "ak1517329278337": "- Malassezia breaks down sebum lipids into irritating fatty acids",
 "ak1517329530875": "- Both reduce the Malassezia load on the skin",
 "ak1669737153829": "- T cells and macrophages normally contain the fungus at the border; without them it spreads and recurs",
 "ak1500235321247": "- KOH dissolves epithelial cells and leaves yeasts and pseudohyphae visible",
 "ak1548722722826": "- Yeast cells budding with chains of pseudohyphae; dermatophytes show true septate hyphae",
 "ak1557752933497": "- Septate, hyaline hyphae in skin scales mean a dermatophyte",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"au-canis-macroconidio": "ganho: reconhecer o M. canis pelo macroconídio na microscopia (identificação), enquanto o card antigo liga o M. canis à capitis por animais"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {"mb44-microsporum-canis-macroconidios.png": "recorte da lâmina 43 (microscopia do M. canis): macroconídios fusiformes de parede espessa, sem legenda; Davi pediu imagem neste card"}
REVISAO = {"despejo": "Despejo lido inteiro (54 notas novas) e as notas mantidas relidas: frentes completas, clozes certos, imagem do M. canis sem legenda, versos com porquê, cores pela rubrica.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Classificar as micoses por profundidade, entender os dermatófitos (gêneros, habitat, fontes, localização, virulência, patogenia no estrato córneo), "
             "reconhecer as tinhas e a candidíase mucocutânea, o diagnóstico (KOH, cultura) e a pitiríase versicolor; superficiais estritas com cobertura mínima.",
 "centrais": [
   ("classificação por profundidade", "au-classificacao", "sh-1792064698883"),
   ("três gêneros de dermatófitos", "ak1500052358184"),
   ("dermatófitos e o estrato córneo", "sh-1791626776803", "sh-1791626776253"),
   ("habitat e fontes", "sh-1791626775626", "sh-1791626776127"),
   ("unha: distal × proximal", "sh-1791626778904"),
 ],
 "exemplos": ["mapas de prevalência", "fotos de tinhas sem card próprio", "isolamento em animais (carpete)", "microcultivo"],
 "outras_aulas": ["48 Micoses subcutâneas (esporotricose)", "50 Micoses sistêmicas (candidíase invasiva)", "55 Prática de micologia (identificação de espécies)", "43 Biologia dos fungos (antifúngicos por alvo)"],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
