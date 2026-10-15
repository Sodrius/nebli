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
 ak("ak-metformina", 1462913225002, {1: Z}, B_, "Metformina ativa AMPK", "50", "Azul: HY 1; liga AMPK à clínica.",
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
DUPLICACAO = {}
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
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
