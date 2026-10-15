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
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
