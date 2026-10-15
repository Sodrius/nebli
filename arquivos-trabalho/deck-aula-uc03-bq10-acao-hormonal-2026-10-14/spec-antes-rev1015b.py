# Especificação curada — Mecanismos de ação hormonal / Controle hormonal (UC03 P1, Bioquímica; Profa. Deborah; 56 lâminas = parte II da turma).
# Foco da aula (transcrição): insulina e glucagon no metabolismo do glicogênio. Diabetes e regulação da massa corpórea = aula 16.
RUN_ID = "uc03-bq10-20261014a"
SHORT = "bq10"
LESSON = "2026-uc03-bioquimica-10-acao-hormonal"
DECK = "NEBLI::UC03::P1::Bioquímica::Ação hormonal"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (GLUT-2, GLUT-4, glucokinase, ATP-sensitive K, sulfonylureas, diazoxide, C-peptide, glucagon, glycogen synthase/phosphorylase, "
         "protein phosphatase, insulin receptor, Gs, tyrosine hydroxylase, PNMT, deiodinase, TBG, steroid hormone, nuclear receptor, cortisol, CRH, paracrine, autocrine; "
         "busca/anking*.txt) e cópias NEBLI vivas de Integração metabólica I/II, 14/10: ")
EXCLUIDOS = [
 (1462127759504, "cloze c1 no verbo (phosphorylated); glucokinase no β/fígado vem de 1474164741147"),
 (1472435618038, "cloze no verbo (dimerizes); a tirosina-quinase do receptor vai em autoral com o nome no cloze (prova 2017)"),
 (1461867864150, "cloze no verbo (dimerizes); 1461867876279 cobre o receptor como fator de transcrição"),
 (1462131701878, "fígado e adiposo: o ponto da aula é o músculo sem receptor de glucagon (autoral d-musculo)"),
 (1461852697255, "colesterol como precursor já está no organizador de classes químicas"),
 (1462849313819, "meglitinidas: não citadas"),
 (1461985737790, "deficiência de deiodinase: não citada"),
]
FORA_DO_RECORTE = ["Diabetes tipo 1/2 e obesidade: aula 16 (Regulação hormonal do metabolismo).", "Sintomas de hipo/hipertireoidismo (lâmina 46): só Tab.",
                   "Esteroidogênese enzima a enzima (21-hidroxilase etc.): UC de endócrino.", "RIA (lâmina 12) e história da insulina (21): só Tab.",
                   "Disruptores endócrinos (55): só Tab."]


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
EP = [1461867085192, 1461857273344, 1462128186045]
A_, B_, C_, D_, E_, F_, H_ = "A-hormonios-e-receptores", "B-insulina", "C-glicogenio", "D-glucagon", "E-catecolaminas", "F-tireoide", "G-esteroides"

CARDS = [
 # A — o que são, classes, receptores (2–18)
 au("a-distancia", ORG("Hormone signaling by <b>distance</b>:<br>- {{c1::endocrine}}: through the blood to distant cells<br>- {{c2::paracrine}}: to neighboring cells, without the blood<br>- {{c3::autocrine}}: back on the cell that secreted it"),
    G(1, 2, 3), A_, "Classificação pelo transporte", "10", "central", NAO, EP, "Verde: lâmina 10; transcrição.",
    extra="- The same molecule can act in more than one way"),
 au("a-classes", ORG("Hormone classes by <b>chemical origin</b>:<br>- peptides (insulin, glucagon): from prohormones<br>- catecholamines: from {{c1::tyrosine}}<br>- eicosanoids: from {{c2::arachidonic acid}}<br>- steroids: from {{c3::cholesterol}}"),
    G(1, 2, 3), A_, "Classificação química", "9; 17–18", "central", NAO, EP, "Verde: lâminas 9 e 17.", duplicacao_ok="ganho: classe ↔ precursor; tirosina hidroxilase e desmolase cobram enzimas",
    extra="- Thyroid hormones also derive from tyrosine, but act like steroids (nuclear receptor)"),
 ak("ak-peptideo-receptor", 1461867085192, G(1), A_, "Peptídeos × lipossolúveis: onde fica o receptor", "15", "Verde: HY 1; lâmina 15; provas 2017 e 2024.",
    extra_add="- Steroid and thyroid hormones cross the membrane and bind intracellular receptors"),
 ak("ak-peptideo-tempo", 1461867860665, G(1), A_, "Velocidade de ação", "16", "Verde: HY 1; legenda da lâmina 15."),
 au("a-receptores", ORG("Four classes of <b>receptors</b> (response time):<br>- {{c1::ion channel}} receptors (milliseconds)<br>- {{c2::G protein-coupled}} receptors (seconds)<br>- {{c3::enzyme-linked}} receptors, e.g. tyrosine kinase (hours)<br>- {{c4::nuclear}} receptors (hours)"),
    {1: Z, 2: V, 3: V, 4: V}, A_, "Tipos de transdutores", "14; 13", "central", NAO, EP, "Verde/azul: lâminas 13–14; transcrição destaca tirosina-quinase e proteína G.", duplicacao_ok="ganho: as quatro classes lado a lado; os outros cards cobram um receptor cada",
    extra="- Insulin uses a tyrosine kinase receptor; glucagon and epinephrine use G protein-coupled receptors"),
 ak("ak-gs-ac", 1461857237570, {1: V, 2: Z}, A_, "Gs ativa adenilato ciclase", "16", "Verde: HY 1; lâmina 16 e 37."),
 ak("ak-camp-pka", 1461857273344, G(1, 2), A_, "AMPc ativa PKA", "16", "Verde: HY 1; lâminas 16 e 37.",
    extra_add="- Each step amplifies the signal: one hormone molecule yields many active enzymes"),
 ak("ak-pde", 1461857288204, {2: Z}, A_, "Fosfodiesterase encerra o sinal", "16", "Azul: HY 1; transcrição (insulina ativa a fosfodiesterase).",
    extra_add="- Insulin activates phosphodiesterase, lowering cAMP and turning off PKA"),
 # B — insulina (19–28)
 ak("ak-peptideo-c", 1462122652771, G(1), B_, "Pró-insulina → insulina + peptídeo C", "22", "Verde: HY 1; lâmina 22."),
 ak("ak-equimolar", 1462122681020, {1: Z}, B_, "Peptídeo C equimolar", "22", "Azul: HY 1; liga a 22 ao insulinoma (28).",
    extra_add="- So C-peptide measures the patient's own insulin secretion"),
 sh(1791054011372, "verde", B_, "GLUT-4 dependente de insulina", "24", "Verde: lâmina 24; viva em Integração I."),
 sh(1791647354296, "verde", B_, "GLUT-2 na célula β", "24; 26", "Verde: lâminas 24 e 26; viva em Integração I."),
 ak("ak-glicoquinase", 1474164741147, G(1), B_, "Glicoquinase no fígado e na célula β", "25; 26", "Verde: lâminas 25–26."),
 sh(1791647346746, "azul", B_, "Km alto da glicoquinase", "25", "Azul: gráfico da lâmina 25; viva em Integração I."),
 sh(1791729317165, "verde", B_, "ATP fecha canal de K+ na célula β", "26", "Verde: lâmina 26; viva em Integração II."),
 au("b-calcio", "In the <b>β cell</b>, depolarization opens voltage-gated {{c1::Ca2+}} channels, and the calcium influx triggers insulin exocytosis",
    G(1), B_, "Cálcio dispara a secreção", "26", "central", NAO, EP, "Verde: lâmina 26; transcrição.",
    extra="- Sequence: glucose → ATP → K+ channel closes → depolarization → Ca2+ enters → insulin released"),
 sh(1791054014146, "verde", B_, "Sulfonilureias fecham o canal de K+", "27", "Verde: lâmina 27; viva."),
 ak("ak-insulinoma", 1462327792664, {1: Z}, B_, "Insulinoma: peptídeo C alto", "28", "Azul: HY 1; lâmina 28."),
 au("b-diazoxido", "Hypoglycemia from an <b>insulinoma</b> can be treated with {{c1::diazoxide}}, which opens ATP-sensitive K+ channels and blocks insulin release",
    {1: R}, B_, "Agonista do KATP no insulinoma", "28", "lateral", NAO, EP, "Azul: lâmina 28 (Proglycem).",
    extra="- Definitive treatment is surgical removal; minoxidil acts on the same channels"),
 au("b-tirosina-quinase", "The <b>insulin receptor</b> has intrinsic {{c1::tyrosine kinase}} activity, so insulin signals through a phosphorylation cascade rather than cAMP",
    G(1), B_, "Receptor de insulina", "32; 33; prova 2017 P1 4.1", "prova", NAO, EP, "Verde: prova 2017; transcrição.",
    extra="- The receptor phosphorylates itself and then IRS-1"),
 ak("ak-irs1", 1472435625919, G(1, 2), B_, "Autofosforilação e IRS-1", "32; 33; prova 2017 P1 4.1", "Verde: prova 2017 (IRS1)."),
 ak("ak-pi3k", 1472435639812, {1: Z}, B_, "PI3K leva GLUT-4 à membrana", "32; 33", "Azul: liga receptor a GLUT-4.",
    extra_add="- PI3K activates PKB (Akt), which mediates most metabolic effects of insulin"),
 # C — glicogênio (29–33)
 sh(1791647344895, "verde", C_, "Fosforilase fosforilada = ativa", "30", "Verde: lâminas 30–32; transcrição."),
 sh(1791647345145, "verde", C_, "Sintase fosforilada = inativa", "30", "Verde: lâminas 30–32; transcrição."),
 sh(1791647351996, "azul", C_, "AMP ativa a fosforilase no músculo", "31", "Azul: lâmina 31; transcrição."),
 au("c-gsk3", "<b>Insulin</b> activates PKB (Akt), which inactivates {{c1::GSK3}}, the kinase that phosphorylates and inactivates glycogen synthase",
    G(1), C_, "Insulina inibe GSK3", "32", "central", NAO, EP, "Verde: lâmina 32; transcrição insiste.",
    extra="- GSK3 = glycogen synthase kinase 3"),
 au("c-pp1", "<b>Insulin</b> also activates {{c1::protein phosphatase 1}}, which dephosphorylates glycogen synthase (activating it) and phosphorylase (inactivating it)",
    G(1), C_, "Insulina ativa a fosfatase", "32", "central", NAO, EP, "Verde: lâmina 32 (fosfatase ativa); transcrição.",
    duplicacao_ok="ganho: enzima nova (PP1); c-gsk3 cobra a outra via", extra="- Glucagon and epinephrine do the opposite: they inhibit PP1 and activate PKA"),
 # D — glucagon (34–38)
 sh(1791647354044, "verde", D_, "Hipoglicemia estimula glucagon", "35", "Verde: lâmina 35."),
 sh(1791054011119, "verde", D_, "Insulina inibe glucagon", "35", "Verde: lâmina 35."),
 au("d-proglucagon", "Proglucagon is cleaved into <b>glucagon</b> in pancreatic α cells, but in intestinal L cells into {{c1::GLP-1}}, an incretin that enhances insulin secretion",
    {1: Z}, D_, "Processamento do pró-glucagon", "36", "central", NAO, EP, "Azul: lâmina 36.",
    extra="- Different prohormone convertases in each tissue (PC2 in α cells, PC1/3 in intestinal L cells)"),
 au("d-fosforilase-quinase", "<b>Glucagon</b>-activated PKA phosphorylates {{c1::phosphorylase kinase}}, which in turn activates glycogen phosphorylase",
    G(1), D_, "Cascata do glucagon", "37", "central", NAO, EP, "Verde: lâmina 37; transcrição."),
 au("d-musculo", "In <b>skeletal muscle</b>, glycogen breakdown is triggered by {{c1::epinephrine}}, since muscle has no glucagon receptors",
    {1: Z}, D_, "Músculo: epinefrina, não glucagon", "37", "central", NAO, EP, "Azul: lâmina 37 (epinephrine (muscle) or glucagon (liver)).",
    extra="- Muscle glycogen fuels the muscle itself; liver glycogen supplies blood glucose"),
 sh(1791054011246, "verde", D_, "Glucagon: glicogenólise e gliconeogênese", "38", "Verde: lâmina 38."),
 # E — catecolaminas (39–41)
 ak("ak-tirosina-hidroxilase", 1476416089486, {2: V}, E_, "Tirosina hidroxilase", "40", "Verde: HY 1; lâmina 40 (etapa limitante).",
    extra_add="- This is the rate-limiting step of catecholamine synthesis"),
 ak("ak-pnmt", 1476416112396, {5: Z}, E_, "PNMT forma adrenalina", "40", "Azul: HY 1; lâmina 40."),
 ak("ak-resistencia", 1524705541467, {1: Z}, E_, "Hormônios contrarreguladores e resistência à insulina", "41; 54", "Azul: HY 1; transcrição (corticoide simula diabetes)."),
 # F — tireoide (42–46)
 ak("ak-tbg", 1461985749010, G(1), F_, "TBG transporta T3/T4", "42", "Verde: HY 1; lâmina 44."),
 au("f-mct8", "<b>Thyroid hormones</b> enter target cells through membrane transporters such as {{c1::MCT8}}",
    {1: Z}, F_, "Transportador de membrana", "42; prova 2017 P1 3.7", "prova", NAO, EP, "Azul: prova 2017; lâmina 42.",
    extra="- Although lipophilic, they need a transporter to cross the membrane"),
 ak("ak-deiodinase", 1461986013689, {1: V, 2: Z, 3: V}, F_, "5'-deiodinase: T4 → T3 e rT3", "42; 43", "Verde: HY 1; lâminas 42–45."),
 ak("ak-t3-afinidade", 1461986072634, {1: Z}, F_, "T3 tem mais afinidade", "45", "Azul: lâmina 45."),
 ak("ak-t3-nuclear", 1462038445101, G(1), F_, "T3 age em receptor nuclear", "45; provas 2017 e 2024", "Verde: HY 1; provas 2017 e 2024."),
 au("f-rxr", "The <b>thyroid hormone receptor</b> binds DNA as a heterodimer with {{c1::RXR}} (retinoid X receptor)",
    {1: Z}, F_, "Heterodímero TR–RXR", "45", "central", NAO, EP, "Azul: lâmina 45."),
 sh(1791627550153, "verde", F_, "Complexo T3–receptor ativa transcrição", "45", "Verde: lâmina 45; provas 2017 e 2024."),
 ak("ak-t3-bmr", 1493668150043, G(1), F_, "Efeito metabólico: Na+/K+-ATPase, consumo de O2", "46; prova 2024 P1 2.2", "Verde: HY 1; prova 2024 (efeitos metabólicos do hormônio tireoidiano); lâmina 46. Revisão 15/10."),
 ak("ak-t3-catabolico", 1462038565107, {1: Z, 2: Z}, F_, "Efeito metabólico: vias catabólicas", "46; prova 2024 P1 2.2", "Azul: prova 2024 (lipólise, glicogenólise); lâmina 46. Revisão 15/10."),
 # G — esteroides (47–54)
 ak("ak-sre", 1461867876279, G(1, 2), H_, "Receptor esteroide é fator de transcrição", "49", "Verde: lâminas 48–49."),
 ak("ak-ppar", 1462913309820, {1: Z, 2: Z}, H_, "PPAR-γ como receptor nuclear", "49; 48; prova 2024 P4 1.3", "Azul: tabela da lâmina 48; prova 2024 P4."),
 ak("ak-crh-acth", 1462053341905, {1: Z}, H_, "Cortisol inibe CRH e ACTH", "50", "Azul: lâmina 50."),
 ak("ak-desmolase", 1462049746964, {1: R}, H_, "Desmolase: etapa limitante", "51", "Rosa: lâmina 51."),
 au("g-hsp90", "Without its hormone, the <b>glucocorticoid receptor</b> stays in the cytoplasm bound to heat shock protein {{c1::HSP90}}",
    {1: Z}, H_, "Receptor de glicocorticoide no citoplasma", "52", "central", NAO, EP, "Azul: lâmina 52.",
    extra="- Cortisol binding releases HSP90 and lets the receptor enter the nucleus"),
 sh(1791729316737, "verde", H_, "Glicocorticoides estimulam gliconeogênese", "53", "Verde: lâmina 53."),
 ak("ak-lipolise", 1462061159065, {1: Z}, H_, "Glicocorticoides e lipólise", "54", "Azul: lâminas 53–54."),
 ak("ak-addison", 1462066580065, {1: Z}, H_, "Addison: os três eixos caem", "54", "Azul: HY 1; lâmina 54."),
]
SEM_IMAGEM = "fato bioquímico sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {
 "ak-peptideo-tempo": "- Membrane receptors modify existing enzymes; nuclear receptors must make new proteins",
 "ak-gs-ac": "- Glucagon and epinephrine receptors couple to Gs",
 "ak-peptideo-c": "- The connecting peptide links the A and B chains in proinsulin",
 "ak-glicoquinase": "- Its high Km lets these organs respond to rising blood glucose",
 "ak-insulinoma": "- Exogenous insulin instead gives high insulin with low C-peptide",
 "ak-irs1": "- IRS-1 docks the next proteins in the cascade, such as PI3K",
 "ak-pnmt": "- Occurs in the adrenal medulla, which is why epinephrine is mainly an adrenal hormone",
 "ak-resistencia": "- Explains why prolonged corticosteroid use can mimic diabetes",
 "ak-tbg": "- Only the free fraction is active",
 "ak-deiodinase": "- T4 is mostly a prohormone; T3 is the active form",
 "ak-t3-afinidade": "- That is why converting T4 to T3 in tissues matters",
 "ak-t3-nuclear": "- It then acts as a transcription factor",
 "ak-sre": "- The response takes hours because new proteins must be made",
 "ak-ppar": "- PPAR-γ appears in the table of nuclear receptors with fatty acid ligands",
 "ak-crh-acth": "- Negative feedback of the hypothalamus–pituitary–adrenal axis",
 "ak-desmolase": "- Cholesterol → pregnenolone, first step of all steroid hormones",
 "ak-lipolise": "- Glycerol is a gluconeogenic substrate",
 "ak-addison": "- Autoimmune destruction of the whole adrenal cortex",
 "f-rxr": "- Many nuclear receptors (vitamin D, PPAR, retinoic acid) also pair with RXR",
 "d-fosforilase-quinase": "- Each step amplifies: glucagon → cAMP → PKA → phosphorylase kinase → phosphorylase",
}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Classificar hormônios e receptores, explicar a secreção de insulina e a sinalização de insulina e glucagon sobre o glicogênio, e reconhecer como catecolaminas, hormônios tireoidianos e esteroides agem.",
 "centrais": [
   ("hormônios e receptores", "a-classes", "a-distancia", "ak-peptideo-receptor", "ak-peptideo-tempo", "a-receptores", "ak-gs-ac", "ak-camp-pka", "ak-pde"),
   ("insulina", "ak-peptideo-c", "ak-equimolar", "sh-1791054011372", "sh-1791647354296", "ak-glicoquinase", "sh-1791647346746", "sh-1791729317165", "b-calcio",
    "sh-1791054014146", "ak-insulinoma", "b-diazoxido", "b-tirosina-quinase", "ak-irs1", "ak-pi3k"),
   ("glicogênio", "sh-1791647344895", "sh-1791647345145", "sh-1791647351996", "c-gsk3", "c-pp1"),
   ("glucagon", "sh-1791647354044", "sh-1791054011119", "d-proglucagon", "d-fosforilase-quinase", "d-musculo", "sh-1791054011246"),
   ("catecolaminas", "ak-tirosina-hidroxilase", "ak-pnmt", "ak-resistencia"),
   ("tireoide", "ak-tbg", "f-mct8", "ak-deiodinase", "ak-t3-afinidade", "ak-t3-nuclear", "f-rxr", "sh-1791627550153", "ak-t3-bmr", "ak-t3-catabolico"),
   ("esteroides", "ak-sre", "ak-ppar", "ak-crh-acth", "ak-desmolase", "g-hsp90", "sh-1791729316737", "ak-lipolise", "ak-addison"),
 ],
 "exemplos": ["história da insulina", "minoxidil", "sintomas de hipo/hipertireoidismo", "disruptores endócrinos"],
 "outras_aulas": [("diabetes e massa corpórea", "16 Regulação hormonal do metabolismo"), ("integração no jejum/alimentado", "25 e 33 Integração metabólica")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
