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

# ---- Completude 15/10 (auditoria de cobertura do Codex; F-20261015-CLAUDE-03): inventário por informação ----
_M = "Completude 15/10: informação da lâmina que estava só no Tab."
def _sl(c): return int(_re.search(r"\d+", str(c["evid"])).group())
def _no_slide(n, card):
    i = next((i for i, c in enumerate(CARDS) if _sl(c) >= n), len(CARDS)); CARDS.insert(i, card)
_no_slide(3, au("a-niveis", ORG("Three levels of <b>metabolic regulation</b>:<br>- {{c1::allosteric}} modulation of enzyme activity<br>- {{c2::covalent}} modification (phosphorylation)<br>- change in enzyme {{c3::expression}}"),
    G(1, 2, 3), A_, "Níveis de regulação metabólica", "3", "central", NAO, EP, "Verde: lâmina 3. " + _M,
    extra="- From seconds (allosteric) to hours (expression)"))
_no_slide(8, au("a-pontos", ORG("Points where a <b>hormone response</b> is regulated:<br>1. biosynthesis<br>2. {{c1::storage}}<br>3. secretion<br>4. {{c2::transport}} in the blood<br>5. {{c3::recognition}} by the receptor<br>6. response<br>7. {{c4::degradation}}"),
    G(1, 2, 3, 4), A_, "Pontos de regulação da resposta hormonal", "8", "central", NAO, EP, "Verde: lâmina 8, organizador da aula (auditoria). " + _M))
_no_slide(11, au("a-neuro", ORG("<b>Hormone</b> × <b>neurotransmitter</b>:<br>- hormone: carried in the {{c1::blood}} to distant targets, slower<br>- neurotransmitter: crosses the {{c2::synapse}}, fast and brief"),
    G(1, 2), A_, "Hormônio × neurotransmissor", "11; 40", "central", NAO, EP, "Verde: lâminas 11 e 40. " + _M,
    extra="- Epinephrine and norepinephrine play both roles"))
_no_slide(12, au("a-ria", "{{c1::Radioimmunoassay}} measures a <b>hormone</b> by letting it compete with a radiolabeled copy of itself for a limited amount of antibody",
    {1: Z}, A_, "Princípio do RIA", "12", "central", NAO, EP, "Azul: lâmina 12 (figura da competição). " + _M,
    extra="- The more hormone in the sample, the less radioactivity stays bound to the antibody"))
_no_slide(22, ak("ak-preprohormonio", 1461852688246, G(1), B_, "Pré-pró-hormônio", "22", "Verde: HY 2; lâmina 22 (processamento de hormônio peptídico, princípio antes da insulina). " + _M))
_no_slide(22, ak("ak-sinal-re", 1473527940967, G(1), B_, "Peptídeo sinal leva ao RE", "22", "Verde: HY 1; lâmina 22. " + _M))
_no_slide(22, ak("ak-prohormonio", 1473609351966, G(1), B_, "Pró-hormônio vai ao Golgi", "22", "Verde: HY 2; lâmina 22. " + _M))
_no_slide(24, sh(1792045263527, "verde", B_, "Captação de glicose dependente × independente de insulina", "24", "Verde: lâmina 24 (tabela dos GLUTs); organizador vivo na UC21. " + _M))
_no_slide(24, sh(1791647346246, "azul", B_, "GLUT-1", "24", "Azul: lâmina 24; viva na Bioquímica 25. " + _M))
_no_slide(24, sh(1791647346370, "azul", B_, "GLUT-3", "24", "Azul: lâmina 24; viva na Bioquímica 25. " + _M))
CARDS.append(au("h-disruptores", "Synthetic chemicals that mimic or block <b>hormones</b>, such as bisphenol A, are called {{c1::endocrine disruptors}}",
    {1: R}, H_, "Disruptores endócrinos", "55", "lateral", NAO, EP, "Rosa: lâmina 55. " + _M,
    extra="- Many bind nuclear receptors such as the estrogen receptor"))

# ---- Ciclo planejar-fazer-revisar 15/10 (F-20261015-CLAUDE-04): transcrição inteira inventariada por informação ----
_M2 = "Completude 15/10: informação da transcrição/lâmina sem card; compreensão ou conexão pedida por Davi."
_no_slide(2, au("a-futil", "Opposing pathways such as <b>glycogen synthesis and breakdown</b> are regulated reciprocally to avoid wasteful {{c1::futile cycles}}",
    G(1), A_, "Por que regular: ciclos fúteis", "2", "central", NAO, EP, "Verde: lâmina 2 e transcrição (analogia do trânsito). " + _M2,
    extra="- If both ran at once, ATP would be spent with no net product"))
_no_slide(3, au("a-fosforilacao", "Protein <b>kinases</b> add phosphate from ATP to {{c1::serine, threonine or tyrosine}} residues, and phosphatases remove it",
    {1: Z}, A_, "Modificação covalente", "3", "central", NAO, EP, "Azul: transcrição (lâmina 3). " + _M2,
    extra="- Phosphorylation can switch an enzyme on (phosphorylase) or off (glycogen synthase)"))
_no_slide(15, au("a-afinidade", "<b>Hormones</b> act at very low concentrations because their receptors bind them with high {{c1::affinity}}",
    {1: Z}, A_, "Receptores de alta afinidade", "15", "central", NAO, EP, "Azul: lâminas 7 e 15. " + _M2))
_no_slide(26, au("b-cadeia-secrecao", ORG("<b>Insulin secretion</b> by the β cell:<br>1. glucose enters by {{c1::GLUT-2}}<br>2. glycolysis raises {{c2::ATP}}<br>3. ATP closes K-ATP channels → depolarization<br>4. {{c3::Ca2+}} enters → insulin exocytosis"),
    G(1, 2, 3), B_, "Cadeia da secreção de insulina", "26", "central", NAO, EP, "Verde: lâmina 26 (lista em sequência). " + _M2,
    duplicacao_ok="compreensão: a sequência inteira; os cards isolados cobram cada elo"))
_no_slide(31, sh(1791647345020, "azul", C_, "Fosforilase hepática inibida pela glicose", "31", "Azul: transcrição (fosforilase a do fígado regulada pela glicose); viva na Bioquímica 25. " + _M2))
_no_slide(32, au("c-mapa-glicogenio", ORG("Hormones and <b>glycogen</b>:<br>- insulin: PKB inhibits GSK3 and activates {{c1::PP1}} → synthase on, phosphorylase off<br>- glucagon and epinephrine: cAMP → {{c2::PKA}} → phosphorylase kinase → phosphorylase on"),
    G(1, 2), C_, "Insulina × glucagon sobre o glicogênio", "32", "central", NAO, EP, "Verde: lâminas 30–32 e transcrição. " + _M2,
    duplicacao_ok="conexão entre os cards de GSK3, PP1, PKA e fosforilase-quinase"))
_no_slide(33, sh(1792045262876, "verde", B_, "Ações da insulina", "33", "Verde: lâmina 33 e transcrição (efeitos por tecido); organizador vivo na UC21. " + _M2))
_no_slide(35, au("d-secrecao-glucagon", ORG("<b>Glucagon secretion</b> by α cells:<br>- stimulated by {{c1::hypoglycemia}}, epinephrine and amino acids<br>- inhibited by {{c2::insulin}}, ketone bodies and urea"),
    {1: Z, 2: Z}, D_, "Estímulos e inibidores do glucagon", "35", "central", NAO, EP, "Azul: lâmina 35. " + _M2,
    duplicacao_ok="compreensão; os AnKing cobram hipoglicemia e insulina isoladas"))
_no_slide(38, au("d-glucagon-figado", ORG("<b>Glucagon</b> in the liver:<br>- ↑ glycogen breakdown<br>- ↑ {{c1::gluconeogenesis}}<br>- ↓ glycolysis<br>- ↑ fatty acid oxidation and {{c2::ketone body}} synthesis"),
    G(1, 2), D_, "Efeitos do glucagon", "38", "central", NAO, EP, "Verde: lâmina 38 e transcrição. " + _M2,
    extra="- Ketone bodies are a packaged form of acetyl-CoA for the brain in prolonged fasting"))
_no_slide(40, au("e-sintese-catecol", ORG("<b>Catecholamine</b> synthesis:<br>phenylalanine → {{c1::tyrosine}} → DOPA → {{c2::dopamine}} → norepinephrine → {{c3::epinephrine}}"),
    G(1, 2, 3), E_, "Via das catecolaminas", "40", "central", NAO, EP, "Verde: lâmina 40. " + _M2,
    duplicacao_ok="compreensão da via; os AnKing cobram as enzimas"))
_no_slide(41, au("e-epinefrina", ORG("<b>Epinephrine</b> in stress:<br>- heart: ↑ rate and blood pressure<br>- muscle: ↑ {{c1::glycogenolysis}} and glycolysis for ATP<br>- liver: ↑ gluconeogenesis<br>- pancreas: ↑ glucagon, ↓ {{c2::insulin}}"),
    G(1, 2), E_, "Efeitos sistêmicos da epinefrina", "41", "central", NAO, EP, "Verde: lâmina 41 e transcrição. " + _M2))
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))

# versos e ajustes da completude 15/10
def _c(k): return next(c for c in CARDS if c["key"] == k)
_EX = {"a-pontos": "- Each step is a control point: drugs and diseases can act on any of them",
       "a-afinidade": "- Nanomolar hormone levels are enough because binding is so tight",
       "b-cadeia-secrecao": "- Sulfonylureas act at step 3, closing the K-ATP channel without glucose",
       "c-mapa-glicogenio": "- Insulin also activates phosphodiesterase, lowering cAMP and switching PKA off",
       "d-secrecao-glucagon": "- Glucagon is a 29-amino-acid peptide from pancreatic α cells",
       "e-sintese-catecol": "- Tyrosine hydroxylase is the rate-limiting step; PNMT in the adrenal medulla makes epinephrine",
       "e-epinefrina": "- Same Gs → cAMP → PKA cascade as glucagon, but muscle has only epinephrine receptors"}
for _k, _x in _EX.items():
    _c(_k)["extra"] = _x
for _k, _x in {"ak-preprohormonio": "- Example: preproinsulin", "ak-sinal-re": "- The signal peptide is then cleaved off", "ak-prohormonio": "- Example: proinsulin, cleaved in secretory granules into insulin and C-peptide"}.items():
    _c(_k)["extra_add"] = _x
_c("a-fosforilacao")["text"] = "Enzymes that transfer phosphate from ATP to <b>serine, threonine or tyrosine</b> residues are protein {{c1::kinases}}, and phosphatases remove it"
_c("d-glucagon-figado")["duplicacao_ok"] = "compreensão: efeitos do glucagon reunidos; os AnKing cobram cada um"
_c("e-epinefrina")["duplicacao_ok"] = "compreensão: efeitos sistêmicos reunidos"
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
# Ajuste 15/10 noite (F-20261015-CLAUDE-05): apostila guia de Biologia Molecular, Aula 1 (Conceitos de ação e regulação hormonal),
# lida inteira; UC3.pdf (mecanismos de ação hormonal) conferido; Lehninger cap. 23 já lido. Cards vivos de Integração I/II, 37/38 e 16 associados.
_M3 = "Ajuste 15/10 noite: apostila guia Biomol Aula 1 (F-20261015-CLAUDE-05)."
CARDS += [
 sh(1791743344484, "azul", A_, "Ácido araquidônico via fosfolipase A2", "9", "Azul: apostila guia Aula 1 (eicosanoides por fosfolipase A2). " + _M3),
 ak("ak-pomc", 1461871709857, {1: V}, A_, "POMC: um gene, vários hormônios", "9", "Verde: apostila guia Aula 1 cap. 2 (POMC → ACTH, endorfinas, lipotropinas); HY 2. " + _M3,
    extra_add="- The same precursor is cut at different sites in different cells"),
 ak("ak-no-gc", 1461865838545, {1: R}, A_, "NO: guanilato ciclase citosólica", "14", "Rosa: apostila guia Aula 1 cap. 2 (NO lipofílico é exceção à regra hidrossolúvel × lipossolúvel). " + _M3),
 au("a-amplificacao", "Each level of a <b>hormonal cascade</b> amplifies the signal, so nanograms of CRH end as milligrams of cortisol, roughly a {{c1::million}}-fold gain",
    {1: R}, A_, "Amplificação da cascata", "16", "lateral", NAO, EP, "Rosa: apostila guia Aula 1 cap. 5. " + _M3,
    extra="- Each level is also a point for negative feedback"),
 sh(1791647346496, "azul", B_, "GLUT2: Km alto", "24", "Azul: apostila guia Aula 1 cap. 3 (GLUT2 de Km alto na célula β); viva em Integração I. " + _M3),
 sh(1791647346994, "azul", B_, "Glicoquinase não inibida por G6P", "25", "Azul: apostila guia Aula 1 cap. 3 (por isso o ATP sobe na célula β); viva em Integração I. " + _M3),
 ak("ak-receptor-insulina", 1462128028823, {1: R}, B_, "Receptor de insulina α2β2", "33", "Rosa: apostila guia Aula 1 cap. 3 (α liga insulina, β autofosforila). " + _M3,
    extra_add="- Insulin binds the α subunits; the β subunits carry the tyrosine kinase"),
 ak("ak-tireoglobulina", 1461984665340, {1: Z, 2: Z}, F_, "Tireoglobulina", "42", "Azul: apostila guia Aula 1 cap. 4 (T3/T4 a partir da tireoglobulina do coloide). " + _M3),
 sh(1792089754676, "azul", "G-esteroides", "Doença de Cushing", "54", "Azul: lâmina 54 (Addison e Cushing); viva na 16. " + _M3),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
CARDS += [
 au("b-hipoglicemia", "Hypoglycemia from excess <b>insulin</b> triggers {{c1::adrenergic}} symptoms such as tremor and sweating, and prolonged lack of glucose damages the brain",
    {1: Z}, B_, "Sintomas da hiperinsulinemia", "28", "central", NAO, [1524013224124, 1477447327155], "Azul: exercício de Bioquímica I.2 e I.6 (insulinoma). " + _M3,
    extra="- The brain depends on blood glucose and cannot use fatty acids"),
 sh(1791647348245, "azul", D_, "Músculo não libera glicose", "41", "Azul: exercício de Bioquímica I.3 (epinefrina: glicose no fígado, piruvato no músculo); viva em Integração I/II. " + _M3),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
CARDS += [
 au("a-dessensibilizacao", "Continuous exposure to a <b>hormone</b> weakens the response through receptor {{c1::desensitization}}, by inactivating or internalizing the receptor",
    {1: Z}, A_, "Dessensibilização", "15", "central", NAO, EP, "Azul: UC3.pdf p. 62 (características da transdução de sinal). " + _M3,
    extra="- When the stimulus falls below a threshold, the system becomes sensitive again"),
 ak("ak-metilxantinas", 1472435600503, {2: Z, 1: Z}, A_, "Cafeína inibe fosfodiesterase", "16", "Azul: UC3.pdf p. 63 (teobromina e cafeína prolongam o AMPc). " + _M3),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
# HY 1–2 em azul: justificativa explícita (ajuste 15/10 noite; antes passavam sem motivo registrado).
_HY = {"ak-pde": ("hy_repete", "o alvo AMPc → PKA já é verde em ak-camp-pka; a degradação completa o ciclo"),
       "ak-equimolar": ("hy_repete", "peptídeo C já verde em ak-peptideo-c; equimolaridade é o corolário"),
       "ak-insulinoma": ("clinica_lateral", "exemplo clínico das lâminas 27–28 (agonistas de KATP)"),
       "ak-pnmt": ("hy_repete", "a via inteira é verde em e-sintese-catecol"),
       "ak-resistencia": ("hy_repete", "efeito contrarregulador já no mapa da epinefrina (e-epinefrina)"),
       "ak-ppar": ("clinica_lateral", "fármaco de exemplo da tabela de receptores nucleares (lâmina 48)"),
       "ak-crh-acth": ("hy_repete", "eixo CRH/ACTH já coberto no deck 16 (verde) e aqui só como retroalimentação"),
       "ak-desmolase": ("clinica_lateral", "enzima da síntese adrenal: detalhe da lâmina 51, aprofundado no endócrino"),
       "ak-lipolise": ("hy_repete", "efeito gliconeogênico do cortisol já verde no compartilhado da lâmina 53"),
       "ak-addison": ("clinica_lateral", "doença citada na lâmina 54 como ilustração")}
for _c_ in CARDS:
    if _c_["key"] in _HY: _c_[_HY[_c_["key"]][0]] = _HY[_c_["key"]][1]
    if _c_["key"] == "b-tirosina-quinase": _c_["duplicacao_ok"] = "regra geral do receptor de insulina; ak-receptor-insulina cobra a estrutura α2β2"
    if _c_["key"] == "ak-metilxantinas": _c_["extra_add"] = "- More cAMP prolongs the effects of epinephrine"
