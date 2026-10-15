# Especificação curada — Envelhecimento celular e tecidual (UC03 P1, Patologia; Prof. Luiz F. Ferraz da Silva; 22 lâminas).
# Telomerase em detalhe = aula 85 (Telômeros e reparo do DNA); câncer = P4; Alzheimer/apoptose = 09.
RUN_ID = "uc03-pt13-20261014a"
SHORT = "pt13"
LESSON = "2026-uc03-patologia-13-envelhecimento"
DECK = "NEBLI::UC03::P1::Patologia::Envelhecimento celular e tecidual"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (telomerase, telomeres, Werner, progeria, sirtuin, caloric restriction, aging, presbyopia, presbycusis, senescence; "
         "busca/anking.txt) e cópias NEBLI vivas das aulas 09 e 11, 14/10: ")
EXCLUIDOS = [
 (1467771904154, "telomerase adiciona TTAGGG: detalhe molecular da aula 85 (Telômeros e reparo do DNA)"),
 (1467771924957, "progéria e telomerase: a aula usa Werner como exemplo de envelhecimento precoce"),
 (1522105602652, "síndrome de Bloom: não citada"),
]
FORA_DO_RECORTE = ["Telomerase em detalhe: aula 85.", "Câncer e telomerase como marca do câncer: P4 (aqui só a relação básica).",
                   "Tabela-resumo de alterações por sistema (lâmina 21): só os itens com card; o resto no Tab."]


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
NAO = "o AnKing não tem este conceito/nome da aula como card."
EP = [1468531927104, 1473359822159, 1467771922095]
A_, B_, C_ = "A-conceitos", "B-mecanismos", "C-sistemas"

CARDS = [
 au("a-senescencia", ORG("Two faces of <b>aging</b>:<br>- {{c1::senescence}}: the natural, expected decline of functional reserve<br>- {{c2::senility}}: changes caused by diseases that affect the elderly"),
    G(1, 2), A_, "Senescência × senilidade", "2; prova 2024 P1 1.3; cruzadas 6, 11", "prova", NAO, EP, "Verde: lâmina 2; prova 2024.",
    extra="- Bone loss within the expected range is senescence; a fracture from osteoporosis is senility"),
 au("a-reserva", "With <b>aging</b>, organs keep their basal function but lose {{c1::functional reserve}}, the extra capacity used under stress",
    G(1), A_, "Reserva funcional", "3; provas 2015, 2016, 2017, 2019; cruzadas 17", "prova", NAO, EP, "Verde: lâmina 3; muitas provas.",
    extra="- So the same pneumonia or drug dose hurts an elderly patient more than a young adult"),
 au("b-mecanismos", ORG("General mechanisms of <b>cellular aging</b>:<br>- accumulated {{c1::DNA damage}}<br>- replicative senescence from {{c2::telomere}} shortening<br>- loss of protein homeostasis (damaged {{c3::proteins}})<br>- altered nutrient sensing (insulin/IGF, TOR)"),
    G(1, 2, 3), B_, "Mecanismos do envelhecimento celular", "4–10", "central", NAO, EP, "Verde: esquema das lâminas 4–10.", extra="- Their effects add up over decades; DNA repair and protein homeostasis counteract aging"),
 au("b-telomeros", "Each cell division shortens the <b>telomeres</b> until the cell stops dividing, a state called replicative {{c1::senescence}}",
    G(1), B_, "Encurtamento dos telômeros", "6; cruzadas 5, 6, 15", "central", NAO, EP, "Verde: lâmina 6.",
    extra="- Telomeres are repeated DNA sequences that protect chromosome ends"),
 au("b-celulas-telomerase", "Unlike <b>somatic cells</b>, {{c1::germ}} cells and stem cells keep their telomeres long through telomerase",
    {1: Z}, B_, "Quem mantém telomerase", "6; cruzadas 3, 8", "central", NAO, EP, "Azul: gráfico da lâmina 6.", extra="- Telomerase is a reverse transcriptase that rebuilds telomeric repeats"),
 ak("ak-telomerase-cancer", 1467771922095, G(1), B_, "Telomerase aumentada no câncer", 6, "Verde: HY 2; células tumorais no gráfico da lâmina 6 (prova 2016).",
    extra_add="- Cancer cells escape replicative senescence"),
 sh(1792026498880, "azul", B_, "Radicais livres oxidam lipídios, DNA e proteínas", 8, "Azul: lâmina 8; viva na 09."),
 au("b-sirtuinas", "<b>Caloric restriction</b> slows aging partly by activating {{c1::sirtuins}}, which favor DNA repair and protein homeostasis",
    {1: Z}, B_, "Sensores de nutrientes e sirtuínas", "10; cruzadas 4", "central", NAO, EP, "Azul: lâmina 10.", extra="- Reduced insulin/IGF and TOR signaling also extend lifespan in animal models"),
 au("b-werner", "<b>Werner syndrome</b> causes premature aging through a defective DNA {{c1::helicase}}, impairing DNA repair",
    {1: Z}, B_, "Síndrome de Werner", "11; cruzadas 10", "central", NAO, EP, "Azul: lâmina 11.", extra="- Patients look elderly in their 30s–40s, showing that failed DNA repair accelerates aging"),
 ak("ak-rugas", 1468531927104, G(1, 2), C_, "Pele: menos colágeno e elastina", 12, "Verde: HY 2; lâmina 12 (cruzadas 12, 14)."),
 ak("ak-presbiacusia", 1480908643571, G(1, 2), C_, "Presbiacusia", 12, "Verde: HY 2; lâmina 12."),
 ak("ak-presbiopia", 1484603491110, {1: R, 2: R}, C_, "Presbiopia", 12, "Rosa: HY 5; lâmina 12."),
 ak("ak-complacencia-pulmonar", 1473359822159, G(1), C_, "Pulmão do idoso: complacência aumentada", 13, "Verde: HY 1; lâminas 13–14 (perda de elasticidade)."),
 sh(1792026992843, "azul", C_, "Lipofuscina do envelhecimento", 15, "Azul: pigmento do idoso (cruzadas 7); viva na 11."),
 ak("ak-rigidez-arterial", 1470850169002, G(1), C_, "Artérias mais rígidas", 17, "Verde: HY 2; lâminas 17 e 20."),
 au("c-tfg", "By age 90, the <b>glomerular filtration rate</b> falls to about {{c1::half}} of the young adult value",
    {1: Z}, C_, "Queda da filtração glomerular", "18; prova 2017 P1 1.5; cruzadas 1", "prova", NAO, EP, "Azul: lâmina 18; prova 2017.",
    extra="- About 1% per year after 50; renally cleared drugs need lower doses"),
 au("c-sarcopenia", "<b>Age-related muscle loss</b>, called {{c1::sarcopenia}}, lowers creatinine production, so serum creatinine can look normal despite a falling GFR",
    {1: Z}, C_, "Sarcopenia e creatinina do idoso", "19; provas pat-04 (creatinina do idoso)", "prova", NAO, EP, "Azul: lâmina 19 (locomotor); provas com creatinina baixa no idoso. Revisão 15/10.",
    extra="- Creatinine comes from muscle creatine and is excreted only by the kidney"),
]
SEM_IMAGEM = "conceito ou fato sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {
 "ak-rugas": "- The skin also loses turgor because the matrix holds less water",
 "ak-presbiacusia": "- Listed among the general changes of aging",
 "ak-presbiopia": "- The lens loses elasticity",
 "ak-complacencia-pulmonar": "- Loss of elastic recoil; chest wall becomes stiffer and residual volume rises",
 "ak-rigidez-arterial": "- Systolic pressure tends to rise",
}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Distinguir senescência de senilidade, explicar a perda de reserva funcional e os mecanismos gerais do envelhecimento celular, e reconhecer as principais alterações por sistema.",
 "centrais": [
   ("conceitos", "a-senescencia", "a-reserva"),
   ("mecanismos", "b-mecanismos", "b-telomeros", "b-celulas-telomerase", "ak-telomerase-cancer", "sh-1792026498880", "b-sirtuinas", "b-werner"),
   ("sistemas", "ak-rugas", "ak-presbiacusia", "ak-presbiopia", "ak-complacencia-pulmonar", "sh-1792026992843", "ak-rigidez-arterial", "c-tfg", "c-sarcopenia"),
 ],
 "exemplos": ["Werner (fotos)", "Alzheimer", "osteopenia", "VEF1 em fumantes"],
 "outras_aulas": [("telomerase", "85 Telômeros e reparo do DNA"), ("apoptose e Alzheimer", "09 Lesão celular"), ("lipofuscina", "11 Acúmulos")],
}
_M2 = "Completude 15/10: transcrição inteira inventariada por informação (F-20261015-CLAUDE-04; auditoria)."
_SI = "conceito ou organizador sem estrutura a reconhecer em imagem"
CARDS.append(au("b-cicatrizacao", "Wounds and gastric injuries heal more slowly in the <b>elderly</b> because {{c1::replicative senescence}} limits the replacement of lost cells",
    G(1), B_, "Conexão: senescência replicativa → reparo lento", "6", "central", NAO, EP, "Verde: transcrição (consequência da senescência celular). " + _M2,
    extra="- Labile and stable tissues are the most affected, since they depend on cell division"))
CARDS.append(au("c-gerais", ORG("General changes of <b>aging</b>:<br>- height: −1 cm/decade, dehydrated {{c1::intervertebral discs}}<br>- less body {{c2::water}}<br>- skin: less turgor<br>- senses decline"),
    {1: Z, 2: Z}, C_, "Mudanças gerais do envelhecimento", "12", "central", NAO, EP, "Azul: lâmina 12 e transcrição (lista estava fora). " + _M2,
    extra="- Fibroblasts make fewer proteoglycans, so tissues hold less water"))
CARDS.append(au("c-pulmao-idoso", ORG("The aging <b>lung</b>:<br>- weaker chest expansion<br>- less efficient {{c1::mucociliary}} clearance and cough reflex, so more infections<br>- less elastic recoil, so FEV1/FVC drifts toward {{c2::70}}%"),
    {1: Z, 2: Z}, C_, "Pulmão do idoso", "14", "central", NAO, EP, "Azul: lâminas 13–14 e transcrição. " + _M2,
    extra="- Below 70% is the threshold used for obstructive disease"))
CARDS.append(au("c-tabagismo", "Quitting <b>smoking</b> restores the normal {{c1::slope}} of FEV1 decline, but the function already lost is not regained",
    {1: Z}, C_, "Tabagismo e perda de reserva", "14", "central", NAO, EP, "Azul: lâmina 14 e transcrição (curvas de VEF1). " + _M2,
    extra="- A susceptible smoker may reach at 50 the lung function of an 85-year-old"))
CARDS.append(au("c-uso", "Physical and intellectual activity slow the decline of <b>functional reserve</b> in the elderly because {{c1::disuse}} causes atrophy",
    {1: Z}, C_, "Conexão: desuso → atrofia (aula 11)", "15", "central", NAO, EP, "Azul: transcrição (sistema nervoso); conexão com a aula 11. " + _M2))
CARDS.append(au("c-urina", "The <b>elderly</b> dehydrate easily on hot days because their kidneys lose urinary {{c1::concentrating ability}}",
    {1: Z}, C_, "Rim do idoso: concentração urinária", "18", "central", NAO, EP, "Azul: lâmina 18 e transcrição. " + _M2,
    extra="- Renal blood flow falls about 1% per year after 50"))
CARDS.append(au("c-doacao", "A young <b>kidney donor</b> regains much of the lost GFR through compensatory {{c1::hyperplasia}} of the remaining kidney, which an elderly donor does poorly",
    {1: Z}, C_, "Conexão: doação de rim ↔ hiperplasia compensatória (aula 11)", "18", "central", NAO, EP, "Azul: transcrição (rim é tecido estável; telômeros curtos no idoso). " + _M2))
CARDS.append(au("c-sistemas", ORG("<b>Aging</b> by system:<br>- lungs: less elastic recoil<br>- arteries: more {{c1::stiffness}}<br>- kidneys: lower {{c2::GFR}}<br>- muscle: {{c3::sarcopenia}}<br>- brain: fewer neurons"),
    G(1, 2, 3), C_, "Mapa por sistemas", "21", "central", NAO, EP, "Verde: lâmina 21 (quadro-resumo; auditoria). " + _M2,
    extra="- Every item is the same idea: loss of functional reserve", duplicacao_ok="organizador do quadro-resumo; cada sistema tem card próprio"))
for _c_ in CARDS:
    if _c_["key"] in ("b-cicatrizacao", "c-gerais", "c-pulmao-idoso", "c-tabagismo", "c-uso", "c-urina", "c-doacao", "c-sistemas"):
        _c_["sem_imagem"] = _SI
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    _x_ = {"c-uso": "- Use keeps cells working near their capacity; the same applies to bone and muscle",
           "c-doacao": "- Older donors have shorter telomeres and less capacity to proliferate"}.get(_c_["key"])
    if _x_: _c_["extra"] = _x_
# Ajuste 15/10 noite (F-20261015-CLAUDE-05): apostila guia de Patologia Aula 4 e monitoria P1 aula 3 lidas; Robbins cap. 1 (envelhecimento) já lido.
_M3 = "Ajuste 15/10 noite (F-20261015-CLAUDE-05)."
_SI3 = "conceito sem estrutura a reconhecer em imagem"
CARDS += [
 ak("ak-ttaggg", 1467771904154, {1: V, 2: V}, B_, "Telomerase adiciona TTAGGG", "6", "Verde: lâmina 6 e apostila guia Aula 4 cap. 2 (telômeros TTAGGG; telomerase com RNA próprio); HY 2. " + _M3, sem_imagem=_SI3),
 ak("ak-telomerase-rt", 1467771911742, {1: Z}, B_, "Telomerase é transcriptase reversa", "6", "Azul: apostila guia Aula 4 cap. 2 (usa o próprio RNA como molde). " + _M3,
    hy_repete="telomerase já verde em ak-ttaggg; aqui o tipo de enzima", sem_imagem=_SI3),
 au("b-dna-quebrado", "Critically short <b>telomeres</b> are read as {{c1::broken DNA}}, triggering the DNA damage response and cell-cycle arrest",
    {1: Z}, B_, "Telômero curto = DNA quebrado", "6", "central", NAO, EP, "Azul: apostila guia Aula 4 cap. 2. " + _M3,
    extra="- Unprotected ends could also fuse or be degraded"),
 au("b-proteostase", "With age, falling {{c1::chaperone}} and proteasome activity lets damaged <b>proteins</b> accumulate, a loss of protein homeostasis",
    {1: Z}, B_, "Perda da homeostase proteica", "9", "central", NAO, EP, "Azul: lâmina 9 e monitoria P1 aula 3. " + _M3,
    extra="- Misfolded proteins that persist can trigger apoptosis"),
 au("b-igf", "<b>Lifespan</b> of model organisms, from worms to mice, is extended by reduced signaling through the {{c1::insulin/IGF-1}} receptor",
    {1: Z}, B_, "Sinalização insulina/IGF-1 e longevidade", "10", "central", NAO, EP, "Azul: lâmina 10 (sensores de nutrientes) e apostila guia Aula 4 cap. 2. " + _M3,
    extra="- Caloric restriction acts on the same nutrient-sensing pathways (TOR, sirtuins)"),
 au("b-antioxidantes", "Transgenic <b>flies</b> overexpressing superoxide dismutase and {{c1::catalase}} live longer, supporting the free-radical theory of aging",
    {1: R}, B_, "Antioxidantes e longevidade", "8", "lateral", NAO, EP, "Rosa: apostila guia Aula 4 cap. 2. " + _M3,
    extra="- Species with lower mitochondrial superoxide production tend to live longer"),
 au("c-cerebro", "Normal <b>brain aging</b> reduces neuron number, brain weight and nerve conduction without necessarily impairing {{c1::cognition}}",
    {1: Z}, C_, "Envelhecimento cerebral normal", "15", "central", NAO, EP, "Azul: lâmina 15 e monitoria P1 aula 3. " + _M3,
    extra="- Dementia such as Alzheimer disease is senility, not senescence"),
 au("c-coracao", "In the aging <b>heart</b>, collagen deposition thickens the {{c1::valves}} and the ventricle becomes less compliant, lowering maximal heart rate and output",
    {1: Z}, C_, "Coração do idoso", "17; 20", "central", NAO, EP, "Azul: lâminas 17 e 20 e monitoria P1 aula 3. " + _M3,
    extra="- Lipofuscin accumulates in the aged myocardium"),
 au("c-fluxo-renal", "After age 50, <b>renal blood flow</b> falls about {{c1::1%}} per year",
    {1: R}, C_, "Fluxo renal no idoso", "18", "lateral", NAO, EP, "Rosa: monitoria P1 aula 3. " + _M3,
    extra="- Even so, the kidneys keep about twice the reserve needed at rest"),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    if _c_["key"] in ("b-dna-quebrado", "b-proteostase", "b-igf", "b-antioxidantes", "c-cerebro", "c-coracao", "c-fluxo-renal"):
        _c_["sem_imagem"] = _SI3
