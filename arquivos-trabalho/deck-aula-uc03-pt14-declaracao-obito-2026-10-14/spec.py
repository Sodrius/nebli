# Especificação curada — Declaração de óbito: conceitos gerais (UC03 P1, Patologia; Prof. Luiz F. Ferraz da Silva; 20 lâminas).
# Tema brasileiro sem AnKing equivalente: deck autoral, conferido contra ANTI-EXEMPLARES-CARDS.
RUN_ID = "uc03-pt14-20261014a"
SHORT = "pt14"
LESSON = "2026-uc03-patologia-14-declaracao-obito"
DECK = "NEBLI::UC03::P1::Patologia::Declaração de óbito"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing e Referências Externas por frases (death certificate, underlying cause, immediate cause, cause of death, coroner, medical examiner; "
         "busca/anking.txt), 14/10: ")
EXCLUIDOS = []
FORA_DO_RECORTE = ["Preenchimento completo dos demais campos da DO: bibliografia da aula (manual), não as lâminas.", "Casos clínicos das lâminas 7–16: ilustração da Parte I/II."]


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
G = lambda *k: {i: V for i in k}
NAO = "o AnKing não cobre a declaração de óbito brasileira (só certidões de outros sistemas)."
EP = [1487642929698, 1487469763555, 1471898845279]
A_, B_, C_ = "A-definicao-e-quem-assina", "B-causas", "C-erros-e-casos-especiais"

CARDS = [
 au("a-sim", "The <b>death certificate</b> (Declaração de Óbito) is the base document of Brazil's {{c1::Mortality Information System}} (SIM)",
    {1: Z}, A_, "DO como base do SIM", 2, "central", NAO, EP, "Azul: lâmina 2."),
 au("a-usos", ORG("The <b>death certificate</b> is used for:<br>- issuing the civil {{c1::death record}}<br>- mortality {{c2::statistics}}<br>- epidemiologic {{c3::surveillance}}"),
    {1: Z, 2: Z, 3: Z}, A_, "Relevância da DO", 2, "central", NAO, EP, "Azul: lâmina 2."),
 au("a-fetal", "A <b>fetal death</b> requires a death certificate from {{c1::20}} weeks of gestation and/or {{c2::500}} g",
    G(1, 2), A_, "Quando emitir: óbito fetal", 3, "central", NAO, EP, "Verde: lâmina 3.",
    extra="- Any liveborn child who dies needs one, regardless of birth weight or gestational age"),
 au("a-natural", ORG("Who signs a <b>natural death</b> certificate:<br>- with medical care: the {{c1::attending}} physician<br>- without medical care: the {{c2::SVO}} physician"),
    G(1, 2), A_, "Quem assina: morte natural", 4, "central", NAO, EP, "Verde: lâmina 4.",
    extra="- SVO = death verification service; in hospitals the on-duty physician may sign; without an SVO, any physician"),
 au("a-violenta", "In a <b>violent death</b>, the death certificate is signed by the {{c1::forensic physician}} (IML) or, where there is no IML, by a physician appointed by the judge or police",
    G(1), A_, "Quem assina: morte violenta", 5, "central", NAO, EP, "Verde: lâmina 5.",
    extra="- Violent deaths include accidents, suicides and homicides"),
 au("b-parte-i", ORG("<b>Part I</b> of the death certificate, one diagnosis per line:<br>- line a: {{c1::immediate}} (terminal) cause<br>- lines b and c: {{c2::intermediate}} causes<br>- line d: {{c3::underlying}} (basic) cause"),
    G(1, 2, 3), B_, "Linhas da Parte I", "6; provas 2016 P2 2.12 e 2019 P1 1.12", "prova", NAO, EP, "Verde: lâmina 6; provas 2016 e 2019.",
    extra="- Each line is the consequence of the line below it"),
 au("b-parte-ii", "<b>Conditions</b> that contributed to death without belonging to the causal chain go in {{c1::Part II}} of the death certificate",
    G(1), B_, "Parte II", "6; prova 2019 P1 1.12", "prova", NAO, EP, "Verde: lâmina 6; prova 2019.",
    extra="- Example: diabetes in a patient who died of a ruptured aortic aneurysm"),
 au("b-causa-basica", "<b>Mortality statistics</b> are tabulated by the {{c1::underlying}} cause of death, the disease that started the chain of events",
    {1: Z}, B_, "Por que a causa básica importa", "6; 2", "central", NAO, EP, "Azul: liga as lâminas 2 e 6.", extra="- That is why a wrong underlying cause distorts public health data",
    duplicacao_ok="ganho: função epidemiológica da causa básica; b-parte-i cobra a posição na linha d"),
 au("b-intervalo", "Each line of <b>Part I</b> also records the approximate {{c1::time interval}} between the onset of that condition and death",
    {1: Z}, B_, "Intervalo de tempo", 8, "central", NAO, EP, "Azul: coluna de tempo nos exemplos (lâminas 8–16)."),
 au("c-erros", "<b>Cardiorespiratory arrest</b> and multiple organ failure should not be written as causes, because they are {{c1::modes of dying}}, not diseases",
    G(1), C_, "Erros mais comuns", 17, "central", NAO, EP, "Verde: lâmina 17.", extra="- Every death ends in cardiorespiratory arrest; the certificate must name the disease that caused it"),
 au("c-campo-59", "In a <b>natural death</b>, the certifier should also record the absence of signs of {{c1::violence}} (field 59)",
    {1: R}, C_, "Campo 59", 18, "lateral", NAO, EP, "Rosa: lâmina 18."),
 au("c-meta-traumatica", "A <b>death days after trauma</b>, even from a later complication such as pneumonia, is still a {{c1::violent}} death and goes to the IML",
    {1: Z}, C_, "Mortes metatraumáticas", 19, "central", NAO, EP, "Azul: lâmina 19.",
    extra="- Deaths in the emergency room without a known diagnosis go to the SVO if natural"),
]
SEM_IMAGEM = "regra documental sem estrutura a reconhecer em imagem"
for c in CARDS:
    c["sem_imagem"] = SEM_IMAGEM
VERSO = {"a-sim": "- It feeds official mortality data nationwide", "a-usos": "- Errors in it distort public health data",
         "c-campo-59": "- Protects the certifier and documents the natural manner of death", "b-intervalo": "- Intervals should grow from line a to line d"}
DUPLICACAO = {}
for c in CARDS:
    if c["key"] in VERSO:
        c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[c["key"]]
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Saber quando emitir e quem assina a declaração de óbito e preencher as causas da morte (Parte I em cadeia causal até a causa básica; Parte II), evitando os erros comuns.",
 "centrais": [("definição e quem assina", "a-sim", "a-usos", "a-fetal", "a-natural", "a-violenta"),
              ("causas", "b-parte-i", "b-parte-ii", "b-causa-basica", "b-intervalo"),
              ("erros e casos especiais", "c-erros", "c-campo-59", "c-meta-traumatica")],
 "exemplos": ["esquistossomose e varizes", "megacólon chagásico", "COVID-19", "aneurisma de aorta"],
 "outras_aulas": [("autópsia", "03 Diagnóstico patológico")],
}
_M = "Completude 15/10 (auditoria): caso da aula com recuperação aplicada; o deck precisa provar que o aluno monta a cadeia, não só recita as linhas."
CARDS.append(au("c-caso-varizes", ORG("<b>Death certificate</b>, diabetic with schistosomiasis, died vomiting blood:<br>- a: {{c1::hypovolemic shock}}<br>- b: {{c1::ruptured varices}}<br>- c: {{c1::portal hypertension}}<br>- d: {{c1::schistosomiasis}}<br>- Part II: {{c2::diabetes}}"),
    {1: Z, 2: Z}, B_, "Caso: varizes esofágicas", "10; prova 2019 P1 1.12", "prova", NAO, EP, "Azul: lâminas 9–10; prova 2019 (preencher Parte I e II). " + _M,
    extra="- Diabetes contributed but is not in the causal chain, so it goes to Part II", duplicacao_ok="caso aplicado das regras b-parte-i e b-parte-ii"))
CARDS.append(au("c-caso-aneurisma", ORG("<b>Death certificate</b>, diabetic with recent COVID-19, ruptured aortic aneurysm:<br>- a: {{c1::hypovolemic shock}}<br>- b: {{c1::hemorrhage}}<br>- c: {{c1::aortic aneurysm}}<br>- Part II: {{c2::COVID-19}} and diabetes"),
    {1: Z, 2: Z}, B_, "Caso: aneurisma roto com COVID na Parte II", "16", "central", NAO, EP, "Azul: lâminas 15–16 (a COVID recente não é a causa básica). " + _M,
    extra="- The infection was real but did not cause the rupture, so it is a contributing condition", duplicacao_ok="caso aplicado das regras b-parte-i e b-parte-ii"))
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    if _c_["key"] in ("c-caso-varizes", "c-caso-aneurisma"): _c_["sem_imagem"] = "caso clínico em texto; preencher a declaração não depende de imagem"
