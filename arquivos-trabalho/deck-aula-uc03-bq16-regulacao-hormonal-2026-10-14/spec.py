# Especificação curada — Regulação hormonal do metabolismo e da massa corpórea (UC03 P1, Bioquímica; Profa. Deborah; partes I (39) + II (23) = 62 lâminas).
# A parte II repete a I e acrescenta AMPK (48–50) e camundongos ob/db (52–56). Ação dos hormônios em si = aula 10.
RUN_ID = "uc03-bq16-20261014a"
SHORT = "bq16"
LESSON = "2026-uc03-bioquimica-16-regulacao-hormonal-massa-corporea"
DECK = "NEBLI::UC03::P1::Bioquímica::Regulação hormonal e massa corpórea"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (leptin, ghrelin, adiponectin, neuropeptide Y, POMC, MC4, AMPK, acetyl-CoA carboxylase, BMI, GLP-1, metabolic syndrome, arcuate, "
         "thermogenin, PFK-2, malonyl-CoA; busca/anking.txt) e cópias NEBLI vivas (UC08, Integração I/II), 14/10: ")
EXCLUIDOS = [
 (1482022023195, "leptina com cloze no verbo (decrease); autoral c-leptina cobra o nome"),
 (1481418796366, "área lateral do hipotálamo: a aula usa o núcleo arqueado"),
 (1481418798641, "área lateral do hipotálamo: a aula usa o núcleo arqueado"),
 (1482022016433, "grelina no jejum: a cópia viva de grelina já cobre"),
 (1461871709857, "família POMC (ACTH, β-endorfina): endócrino; aqui só o α-MSH"),
]
FORA_DO_RECORTE = ["Eixos hipotálamo-hipófise e doenças endócrinas (lâminas 4–8, 40–44): panorama; só a resposta ao estresse tem card.",
                   "Parabiose (23–24, 55–56): raciocínio no Tab; o card cobra ob (leptina) e db (receptor).", "Vídeos (13, 30, 37, 47, 58): dispensados."]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
G = lambda *k: {i: V for i in k}
NAO = "o AnKing não tem este fato como card."
EP = [1482022023195, 1578537123614, 1462913225002]
A_, B_, C_, D_ = "A-homeostase-e-obesidade", "B-AMPK", "C-adipocinas", "D-apetite"

CARDS = [
 # A — homeostase energética e obesidade (2–18)
 ak("ak-imc", 1543085033888, G(1), A_, "IMC: sobrepeso e obesidade", "3", "Verde: tabela de IMC da lâmina 3.",
    extra_add="- BMI = weight (kg) / height² (m²)"),
 au("a-estresse", ORG("Response to <b>stress</b>:<br>- short term: the adrenal medulla releases {{c1::epinephrine}}<br>- long term: ACTH makes the adrenal cortex release {{c2::cortisol}}"),
    {1: Z, 2: Z}, A_, "Estresse curto e prolongado", "6; 42", "central", NAO, EP, "Azul: lâminas 6 e 42; transcrição.",
    extra="- Epinephrine: glycogen breakdown, heart rate<br>- Cortisol: gluconeogenesis"),
 au("a-lipostatica", "The <b>lipostatic theory</b> holds that the body keeps its {{c1::adipose tissue}} mass roughly constant by adjusting food intake and energy expenditure",
    G(1), A_, "Teoria lipostática", "11; 20; 45", "central", NAO, EP, "Verde: lâminas 11, 20 e 45; transcrição.",
    extra="- Energy consumed = energy used + energy stored"),
 au("a-inflamacao", "In <b>obesity</b>, macrophages in adipose tissue release {{c1::TNF-α}} and IL-6, creating low-grade inflammation that worsens insulin resistance",
    {1: Z}, A_, "Inflamação do tecido adiposo", "17", "central", NAO, EP, "Azul: lâmina 17; gabarito 2023 P1 2.3 (inflamação).",
    extra="- Adiponectin falls at the same time"),
 au("a-ceramidas", "Excess fat in <b>muscle and liver</b> raises {{c1::DAG and ceramides}}, which activate serine kinases that block insulin receptor signaling",
    {1: Z}, A_, "Lipotoxicidade e resistência à insulina", "18; 15", "central", NAO, EP, "Azul: lâminas 15 e 18.",
    extra="- Insulin resistance plus β-cell failure leads to type 2 diabetes"),
 # B — AMPK (47–50)
 au("b-ampk", "The cell's main energy sensor, activated when <b>AMP</b> rises, is {{c1::AMPK}} (AMP-activated protein kinase)",
    G(1), B_, "AMPK", "48; 47", "central", NAO, EP, "Verde: lâmina 48; transcrição (sensor principal).",
    extra="- It turns on ATP-producing pathways and turns off biosynthesis to save ATP<br>- LKB1 also activates it"),
 au("b-acc", "<b>AMPK</b> blocks lipogenesis by phosphorylating and inhibiting {{c1::acetyl-CoA carboxylase}}",
    G(1), B_, "AMPK inibe ACC", "49", "central", NAO, EP, "Verde: lâmina 49; transcrição.", duplicacao_ok="ganho: quem inibe a ACC (AMPK); ak-acc cobra a ACC como etapa limitante",
    extra="- Less malonyl-CoA releases CAT-1, so fatty acid oxidation increases"),
 ak("ak-acc", 1475894369854, {1: Z}, B_, "ACC é a etapa limitante da lipogênese", "49", "Azul: lâmina 49.",
    extra_add="- It converts acetyl-CoA into malonyl-CoA"),
 sh(1791729319038, "azul", B_, "Malonil-CoA inibe CAT-1", "49", "Azul: lâmina 49; viva em Integração II."),
 au("b-pfk2", "<b>AMPK</b> speeds glycolysis by activating {{c1::PFK-2}}, which raises fructose-2,6-bisphosphate, the activator of PFK-1",
    {1: Z}, B_, "AMPK ativa a glicólise", "50", "central", NAO, EP, "Azul: lâmina 50; transcrição.", extra="- More ATP is produced when energy is low"),
 ak("ak-metformina", 1462913225002, {1: Z}, B_, "Metformina ativa AMPK", "50", "Azul: HY 1; liga AMPK à clínica.", clinica_lateral="fármaco de exemplo; o alvo é a AMPK (b-ampk verde)",
    extra_add="- Same sensor the lesson describes as the master energy regulator"),
 # C — adipocinas e leptina (21–28; 51–57)
 au("c-leptina", "{{c1::Leptin}}, secreted by <b>adipocytes</b> in proportion to fat stores, acts on the <b>hypothalamus</b> to produce satiety",
    G(1), C_, "Leptina", "22; 20; 21", "central", NAO, EP, "Verde: lâminas 20–22; prova 2023 P1 2.3.",
    extra="- After a meal leptin rises; in fasting it falls"),
 au("c-ob", "<b>Leptin</b> is encoded by the {{c1::ob}} gene, whose mutation makes mice massively obese",
    G(1), C_, "Gene ob", "22; 52; 53", "central", NAO, EP, "Verde: lâminas 22, 52–53; transcrição (67 g → 35 g).", extra="- Given leptin, they eat less and drop from 67 g to 35 g"),
 au("c-db", "<b>db/db mice</b> stay obese even when given leptin, because they lack a functional leptin {{c1::receptor}}",
    G(1), C_, "Gene db", "23; 54; 55", "central", NAO, EP, "Verde: lâminas 23–24 e 54–56; transcrição (parabiose).",
    extra="- In parabiosis, the db/db partner's excess leptin starves the normal or ob/ob mouse"),
 ak("ak-leptina-obesos", 1578537123614, G(1), C_, "Obesos têm leptina alta", "25; 57; prova 2023 P1 2.3", "Verde: HY 1; prova 2023 P1 2.3.",
    extra_add="- Leptin treatment does not help them: they are leptin resistant, much like insulin resistance"),
 au("c-resistencia", "<b>Obese people</b> stay hungry despite high leptin because their hypothalamus responds poorly to it, a state called {{c1::leptin resistance}}",
    G(1), C_, "Resistência à leptina", "25; 57; prova 2023 P1 2.3", "prova", NAO, EP, "Verde: prova 2023 P1 2.3 (por que obesos com leptina alta continuam obesos); lâminas 25 e 57. Revisão 15/10: estava só no Extra.",
    extra="- Inflammation and insulin resistance blunt leptin signaling in the arcuate nucleus"),
 sh(1791647352594, "azul", C_, "Termogenina (UCP-1)", "26", "Azul: lâmina 26 (efeitos periféricos da leptina, UCP); viva em Integração I."),
 au("c-adiponectina", "{{c1::Adiponectin}}, an <b>adipokine</b> that is higher in lean people, activates AMPK and improves insulin sensitivity",
    G(1), C_, "Adiponectina", "51; 27", "central", NAO, EP, "Verde: lâminas 27 e 51; transcrição.", duplicacao_ok="ganho: adiponectina ativa AMPK; ak-ppar cobra glitazonas",
    extra="- Obese people have less (TNF-α inhibits it); its deficiency mimics type 2 diabetes"),
 ak("ak-ppar-adiponectina", 1462913323101, G(1), C_, "Glitazonas aumentam adiponectina", "51; 27", "Verde: liga adiponectina à aula 10 (PPAR-γ)."),
 # D — apetite: intestino e cérebro (29–38; 59–62)
 sh(1790979869860, "verde", D_, "Grelina aumenta o apetite", "31; 59", "Verde: lâminas 31 e 59; viva na UC08."),
 sh(1791052302525, "azul", D_, "GLP-1 e saciedade", "38; 31", "Azul: lâmina 38 (Ozempic, Mounjaro); prova 2023 P1 2.3."),
 au("d-arqueado", ORG("In the hypothalamic <b>arcuate nucleus</b>:<br>- {{c1::POMC/CART::neurons}} neurons, activated by leptin, promote satiety<br>- {{c1::NPY/AgRP::neurons}} neurons, activated by ghrelin, promote hunger"),
    G(1), D_, "Neurônios do núcleo arqueado", "32; 60", "central", NAO, EP, "Verde: lâminas 32–34 e 59–60; transcrição.",
    extra="- AgRP neurons also inhibit POMC neurons"),
 au("d-msh", "<b>POMC neurons</b> release {{c1::α-MSH}}, which binds MC4R on satiety neurons and makes us stop eating",
    G(1), D_, "α-MSH e MC4R", "34; 60", "central", NAO, EP, "Verde: lâminas 34 e 60; transcrição.",
    extra="- Mutations in MC4R are a known genetic cause of human obesity"),
 au("d-optogenetica", "{{c1::Optogenetics}} maps <b>neuron</b> function by expressing a light-activated ion channel in chosen neurons",
    {1: R}, D_, "Optogenética", "35; 61", "lateral", NAO, EP, "Rosa: lâminas 35–36 e 61.", extra="- Used to show which hypothalamic neurons drive hunger or satiety"),
]
SEM_IMAGEM = "fato bioquímico sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
DUPLICACAO = {"a-eixo": "cascata hipotálamo–hipófise–tireoide (TRH/TSH); ak-crh cobra o ramo CRH/ACTH do estresse"}
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Explicar como o organismo mantém a massa de tecido adiposo (teoria lipostática), o papel da AMPK como sensor de energia, das adipocinas (leptina, adiponectina) e dos sinais intestinais e hipotalâmicos do apetite, e por que a obesidade gera resistência à insulina e à leptina.",
 "centrais": [
   ("homeostase e obesidade", "ak-imc", "a-estresse", "a-lipostatica", "a-inflamacao", "a-ceramidas"),
   ("AMPK", "b-ampk", "b-acc", "ak-acc", "sh-1791729319038", "b-pfk2", "ak-metformina"),
   ("adipocinas", "c-leptina", "c-ob", "c-db", "ak-leptina-obesos", "c-resistencia", "sh-1791647352594", "c-adiponectina", "ak-ppar-adiponectina"),
   ("apetite", "sh-1790979869860", "sh-1791052302525", "d-arqueado", "d-msh", "d-optogenetica"),
 ],
 "exemplos": ["parabiose de Coleman", "criança com deficiência de leptina", "Ozempic/Mounjaro"],
 "outras_aulas": [("ação dos hormônios", "10 Ação hormonal"), ("jejum e alimentado", "25 e 33 Integração metabólica")],
}
_M2 = "Completude 15/10: transcrição inteira inventariada por informação (F-20261015-CLAUDE-04; auditoria)."
_SI = "conceito ou organizador sem estrutura a reconhecer em imagem"
_NOVOS = []
def _n(card): _NOVOS.append(card["key"]); CARDS.append(card)
_n(au("a-eixo", ORG("<b>Neuroendocrine</b> cascade to cold:<br>1. {{c1::hypothalamus}}: TRH<br>2. anterior {{c2::pituitary}}: TSH<br>3. thyroid: T3 and T4<br>4. target tissues respond"),
    G(1, 2), A_, "Eixo hipotálamo → hipófise → glândula → alvo", "4", "central", NAO, EP, "Verde: lâminas 4–5 e transcrição (estava só no Tab). " + _M2,
    extra="- Each level amplifies the signal; the final hormone feeds back on the upper levels"))
_n(au("a-hipofise", ORG("Hormones of the <b>pituitary</b>:<br>- anterior: ACTH, TSH, FSH, LH, GH and {{c1::prolactin}}<br>- posterior: {{c2::oxytocin}} and vasopressin"),
    {1: Z, 2: Z}, A_, "Hipófise anterior × posterior", "5", "central", NAO, EP, "Azul: lâmina 5 e transcrição. " + _M2,
    extra="- The posterior lobe only stores hormones made by hypothalamic neurons"))
_n(au("b-mapa-ampk", ORG("When energy is low, active <b>AMPK</b>:<br>- switches off lipid synthesis (ACC) and protein synthesis ({{c1::mTOR}})<br>- switches on glucose uptake, glycolysis (PFK-2) and fatty acid {{c2::oxidation}}"),
    G(1, 2), B_, "Mapa da AMPK", "48", "central", NAO, EP, "Verde: lâminas 48–50 e transcrição. " + _M2,
    extra="- When ATP is restored, AMP falls and AMPK turns off", duplicacao_ok="compreensão: os cards de ACC e PFK-2 cobram cada alvo"))
_n(au("c-parabiose", "In <b>parabiosis</b>, a db/db mouse makes its normal partner starve because it releases large amounts of {{c1::leptin}} that it cannot sense itself",
    {1: Z}, C_, "Conexão: lógica da parabiose", "24", "central", NAO, EP, "Azul: lâminas 23–24 e transcrição (raciocínio pedido pela professora). " + _M2,
    extra="- Joined to an ob/ob mouse, the db/db partner's leptin makes the ob/ob mouse lose weight"))
_n(au("d-cart-drogas", "<b>POMC/CART neurons</b> are also stimulated by cocaine and {{c1::amphetamine}}, which explains the loss of appetite these drugs cause",
    {1: R}, D_, "CART e drogas", "32", "lateral", NAO, EP, "Rosa: transcrição. " + _M2))
_n(au("d-cadeia-apetite", ORG("Appetite signals in the <b>arcuate nucleus</b>:<br>- fasting: stomach {{c1::ghrelin}} → AgRP/NPY neurons → hunger<br>- fed: {{c2::leptin}} and insulin → POMC neurons → α-MSH on {{c3::MC4R}} → satiety"),
    G(1, 2, 3), D_, "Cadeia completa do apetite", "34", "central", NAO, EP, "Verde: lâminas 31–34 e transcrição; auditoria pediu a cadeia inteira. " + _M2,
    extra="- MC4R mutations cause obesity because satiety is never signaled", duplicacao_ok="compreensão que liga d-arqueado e d-msh"))
for _c_ in CARDS:
    if _c_["key"] in _NOVOS: _c_["sem_imagem"] = _SI
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    if _c_["key"] == "d-cart-drogas": _c_["extra"] = "- CART = cocaine- and amphetamine-regulated transcript"
# Ajuste 15/10 noite (F-20261015-CLAUDE-05): lâminas 6, 8, 12, 15–17, 22, 26, 29, 31, 38 e 48–51 relidas contra o Lehninger cap. 23
# (massa corporal, lido de novo nas pp. 961–965), o UC3.pdf (pp. 70–71 e 254–255) e a apostila de exercícios de Bioquímica (II.1–5).
_M3 = "Ajuste 15/10 noite (F-20261015-CLAUDE-05)."
FORA_DO_RECORTE[0] = "Eixos hipotálamo-hipófise (lâminas 4–7, 40–43): panorama com cascata, hipófise e estresse em card; doenças endócrinas (8, 44) só pela classificação e pelo tumor de hipófise do exercício II.4."
CARDS += [
 ak("ak-crh", 1462053147855, {2: V}, A_, "CRH → POMC/ACTH", "6", "Verde: lâmina 6 (estresse prolongado: hipotálamo → CRH → ACTH) e exercício II.1B; HY 2. " + _M3,
    extra_add="- Cortisol then raises gluconeogenesis and mobilizes protein and fat"),
 sh(1791054013222, "azul", A_, "Glucagon, cortisol e adrenalina: resistência à insulina", "6", "Azul: exercício II.1 (hormônios do estresse integram a resposta metabólica); viva no GR1. " + _M3),
 au("a-endocrinas", ORG("How are <b>endocrine disorders</b> classified?<br>1. gland {{c1::hyposecretion}} (hormone deficiency)<br>2. gland {{c1::hypersecretion}} (hormone excess)<br>3. {{c2::tumors}} of endocrine glands"),
    {1: R, 2: R}, A_, "Classificação das doenças endócrinas", "8; 44", "lateral", NAO, EP, "Rosa: quadro da lâmina 8 (classification). " + _M3,
    extra="- Causes include gland injury, congenital defects, infections and feedback failures"),
 ak("ak-cushing", 1462380546437, {1: Z}, A_, "Doença de Cushing: adenoma de hipófise", "8", "Azul: exercício II.4 (tumor de hipófise e consequência metabólica). " + _M3, clinica_lateral="tumor de hipófise pedido no exercício II.4; o alvo da aula é a consequência metabólica",
    extra_add="- Excess cortisol raises blood glucose by gluconeogenesis and insulin resistance"),
 au("a-recompensa", "Palatable food activates the brain's {{c1::reward}} pathways, one reason <b>obesity</b> rose once food became always available",
    {1: R}, A_, "Por que a obesidade aumentou", "12", "lateral", NAO, EP, "Rosa: lâmina 12 (fatores: comida disponível, recompensa, genética, ambiente, microbiota). " + _M3,
    extra="- Genetics, environment and the gut microbiota also contribute"),
 sh(1791729325413, "azul", A_, "Síndrome metabólica", "15", "Azul: lâmina 15 (obesidade → síndrome metabólica); viva em Integração II. " + _M3),
 sh(1791729324668, "azul", A_, "DM2: resistência + deficiência relativa", "16", "Azul: lâmina 16 (pré-diabetes: resistência e disfunção da célula β); viva em Integração II. " + _M3),
 au("a-endotelio", "<b>Obesity</b>-driven inflammation damages the endothelium, which makes less {{c1::nitric oxide}} and more ROS",
    {1: R}, A_, "Disfunção endotelial na obesidade", "17", "lateral", NAO, EP, "Rosa: último quadro da lâmina 17. " + _M3,
    extra="- This links obesity to hypertension and atherosclerosis"),
 au("c-ob-frio", "<b>ob/ob mice</b> are cold-sensitive as well as obese, because leptin also drives {{c1::thermogenesis}}",
    {1: R}, C_, "ob/ob: sensibilidade ao frio", "22", "lateral", NAO, EP, "Rosa: lâmina 22 (apetite voraz, obesidade, síndrome metabólica, sensibilidade ao frio). " + _M3,
    extra="- Without leptin the brain reads a starving state and cuts heat production"),
 au("c-simpatico", "<b>Leptin</b> stimulates the {{c1::sympathetic}} nervous system, raising heart rate, blood pressure and brown-fat thermogenesis",
    {1: Z}, C_, "Leptina ativa o simpático", "26", "central", NAO, EP, "Azul: lâmina 26 (efeitos periféricos), Lehninger p. 962 e UC3.pdf p. 70. " + _M3,
    extra="- Norepinephrine → β3 receptor → cAMP → PKA, which induces UCP1 (thermogenin) and activates hormone-sensitive lipase"),
 au("c-jak-stat", "The <b>leptin receptor</b> signals through the {{c1::JAK-STAT}} pathway, turning on POMC transcription in the hypothalamus",
    {1: Z}, C_, "Leptina: via JAK-STAT", "22", "central", NAO, EP, "Azul: Lehninger fig. 23-36 (via de sinalização da leptina). " + _M3,
    extra="- STATs are phosphorylated by JAK, dimerize and enter the nucleus"),
 au("c-jejum", "Falling <b>leptin</b> in fasting lowers thyroid and sex hormones and raises glucocorticoids, so the leptin system mainly defends against {{c1::starvation}}",
    {1: Z}, C_, "Leptina e jejum", "25", "central", NAO, EP, "Azul: Lehninger p. 963 (o sistema evoluiu para a fome) e UC3.pdf p. 255. " + _M3,
    extra="- Minimizing energy use and mobilizing stores helps survive famine"),
 sh(1790999837254, "azul", D_, "PYY diminui o apetite", "29", "Azul: lâmina 29 (peptídeos gastrointestinais de saciedade) e Lehninger fig. 23-35; viva na UC08. " + _M3),
 au("d-orexigenico", "Hormones that increase appetite, such as <b>ghrelin</b>, are called {{c1::orexigenic}}",
    {1: Z}, D_, "Orexigênico × anorexigênico", "31", "central", NAO, EP, "Azul: UC3.pdf p. 254 e Lehninger p. 962. " + _M3,
    extra="- Leptin, insulin, PYY and GLP-1 are anorexigenic"),
 au("d-grelina-refeicao", "Blood <b>ghrelin</b> peaks just {{c1::before::before/after}} a meal and falls quickly after eating",
    {1: R}, D_, "Grelina sobe antes da refeição", "31", "lateral", NAO, EP, "Rosa: UC3.pdf p. 71. " + _M3,
    extra="- Ghrelin also stimulates growth hormone release"),
 au("d-npy", "Levels of the hunger neuropeptide {{c1::NPY}} rise in <b>fasting</b> and stay high in ob/ob and db/db mice",
    {1: R}, D_, "NPY alto no jejum e nos mutantes", "32; 33", "lateral", NAO, EP, "Rosa: Lehninger p. 962 e lâmina 33. " + _M3,
    extra="- Without leptin signaling, NPY release is never restrained"),
 au("d-insulina", "Besides leptin, {{c1::insulin}} acts on <b>arcuate neurons</b> to inhibit NPY and stimulate α-MSH, reducing food intake",
    {1: Z}, D_, "Insulina também age no arqueado", "31; 34", "central", NAO, EP, "Azul: lâmina 31 e Lehninger fig. 23-35. " + _M3,
    extra="- Both hormones rise in proportion to body fat"),
 au("d-reciproca", "The two groups of <b>arcuate neurons</b> {{c1::inhibit each other}}, so a signal that activates the hunger neurons silences the satiety neurons",
    {1: R}, D_, "Inibição recíproca", "33", "lateral", NAO, EP, "Rosa: lâmina 33 e Lehninger fig. 23-35. " + _M3,
    extra="- This sharpens the switch between eating and stopping"),
 ak("ak-glp1-agonistas", 1462849387815, {1: Z}, D_, "Agonistas de GLP-1 (semaglutida)", "38", "Azul: lâmina 38 (Ozempic) e prova 2023 P1 2.3. " + _M3, clinica_lateral="fármaco de exemplo da lâmina 38; o mecanismo (GLP-1) é verde no card compartilhado",
    extra_add="- They mimic the gut hormone GLP-1: more insulin, slower gastric emptying, satiety"),
 au("d-tirzepatida", "<b>Tirzepatide</b> (Mounjaro) activates the GLP-1 receptor and also the {{c1::GIP}} receptor",
    {1: R}, D_, "Tirzepatida: GLP-1 + GIP", "38", "lateral", "consulta tirzepatide sem card (15/10 noite).", EP, "Rosa: lâmina 38. " + _M3,
    extra="- GIP is the other incretin released by the gut after a meal"),
 au("b-hmg", "<b>AMPK</b> also blocks cholesterol synthesis by phosphorylating and inactivating {{c1::HMG-CoA reductase}}",
    {1: R}, B_, "AMPK inibe HMG-CoA redutase", "49", "lateral", NAO, EP, "Rosa: Lehninger p. 964 (AMPK e síntese de lipídeos). " + _M3,
    extra="- Low energy shuts down every costly lipid synthesis pathway"),
]
for _c_ in CARDS:
    if _c_["key"] == "c-adiponectina" and "TNF" not in _c_.get("extra", ""):
        _c_["extra"] = (_c_.get("extra", "") + "<br>" if _c_.get("extra") else "") + "- TNF-α suppresses adiponectin in obesity"
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
CARDS.append(au("c-irs2", "<b>Leptin</b> makes liver and muscle more sensitive to insulin, since both hormones lead to phosphorylation of {{c1::IRS-2}}",
    {1: R}, C_, "Leptina e insulina: IRS-2", "31", "lateral", NAO, EP, "Rosa: apostila guia (Biomol) Aula 2 cap. 5 e Lehninger fig. 23-37. " + _M3,
    extra="- Phosphorylated IRS-2 activates PI3K, which also reduces food intake"))
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    if _c_["key"] == "a-eixo":
        _c_["duplicacao_ok"] = "'pituitary' da cascata TRH/TSH; ak-cushing cobra o adenoma hipofisário secretor de ACTH (outro alvo)"
