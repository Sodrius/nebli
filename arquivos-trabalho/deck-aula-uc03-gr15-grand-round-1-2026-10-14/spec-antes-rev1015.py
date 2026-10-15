# Especificação curada — Grand Round 1, Esquizofrenia (UC03 P1; Elkis, Ferraz da Silva, Leite, Barbuto; 57 lâminas).
# Grand Round integra Psiquiatria (sintomas, curso), Radiologia (TC × RM), Bioquímica (dopamina, COMT) e Imunologia (privilégio imune, neuroinflamação).
RUN_ID = "uc03-gr15-20261014a"
SHORT = "gr15"
LESSON = "2026-uc03-grand-round-01-esquizofrenia"
DECK = "NEBLI::UC03::P1::Grand Round::Grand Round 1 (esquizofrenia)"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (schizophrenia, positive/negative symptoms, mesolimbic, nigrostriatal, tuberoinfundibular, mesocortical, COMT, cannabis, "
         "lateral ventricles, schizoaffective, clozapine, immune privilege, risperidone; busca/anking.txt) e cópias NEBLI vivas (Radiologia 02, 12), 14/10: ")
EXCLUIDOS = [
 (1483845005621, "via mesolímbica e sintomas positivos com cloze no verbo: 1541613861907 cobra as duas vias juntas"),
 (1483844989020, "via mesocortical e sintomas negativos com cloze no verbo: 1541613861907 cobra as duas vias juntas"),
 (1484687004511, "critérios diagnósticos do DSM: não estão na aula"),
 (1455311471937, "discinesia tardia: farmacologia, fora do GR"),
]
FORA_DO_RECORTE = ["TC × RM (lâminas 14–20): revisão das aulas de Radiologia; entra o compartilhado de radiação.", "Estigma e Brian Wilson (49–57): só Tab; o card cobra o diagnóstico de transtorno esquizoafetivo.",
                   "Vias de apoptose (38): aula 09 (Lesão celular)."]


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
NAO = "o AnKing não tem este fato da aula como card."
EP = [1541613861907, 1509647553855, 1484687045054]
A_, B_, C_, D_ = "A-clinica-e-curso", "B-imagem", "C-dopamina-e-modelo", "D-neuroimunologia"

CARDS = [
 # A — clínica e curso (2–11)
 ak("ak-psicose", 1484686918152, G(1), A_, "Psicose", "2; 4", "Verde: caso (surto psicótico); lâmina 4."),
 au("a-sintomas", ORG("Symptom groups of <b>schizophrenia</b>:<br>- positive: {{c1::delusions, hallucinations}}<br>- negative: {{c2::blunted affect, avolition}}<br>- cognitive: attention and memory deficits"),
    G(1, 2), A_, "Grupos de sintomas", "4", "central", NAO, EP, "Verde: lâmina 4; caso (isolado, poucas atividades = negativos).",
    extra="- Disorganized thought and behavior and mood symptoms also occur"),
 au("a-panss", "Severity of positive and negative symptoms of <b>schizophrenia</b> is rated with the {{c1::PANSS}} scale",
    {1: R}, A_, "PANSS", "5; 6", "lateral", NAO, EP, "Rosa: lâminas 5–6.",
    extra="- Positive and Negative Syndrome Scale (Kay, 1987)"),
 au("a-estagios", ORG("Stages of <b>schizophrenia</b>:<br>1. premorbid (subtle motor and social delays)<br>2. {{c1::prodromal}} (school decline, isolation)<br>3. progressive (first psychotic episode)<br>4. {{c2::chronic}} (negative symptoms, disability)"),
    {1: Z, 2: Z}, A_, "Estágios da doença", "7; 8", "central", NAO, EP, "Azul: lâminas 7–8.",
    extra="- Neurodegenerative processes are limited to the early years after onset"),
 au("a-sexo", "<b>Schizophrenia</b> starts earlier in {{c1::men::sex}}, with peak onset at 20–24 years",
    {1: Z}, A_, "Idade de início e sexo", "9", "central", NAO, EP, "Azul: lâmina 9.",
    extra="- Women have a later peak and a second one after 45 years"),
 au("a-neurodesenvolvimento", "Obstetric complications, low birth weight and intrauterine infection raise <b>schizophrenia</b> risk, supporting the {{c1::neurodevelopmental}} hypothesis",
    G(1), A_, "Hipótese do neurodesenvolvimento", "11; 10", "central", NAO, EP, "Verde: lâmina 11; o fio do GR.",
    extra="- Advanced paternal age is another early risk factor"),
 # B — imagem (12–22)
 ak("ak-ventriculos", 1509647553855, G(1), B_, "Ventriculomegalia", "13; 12", "Verde: lâminas 12–13.",
    extra_add="- Gray matter loss progresses with each psychotic episode"),
 sh(1791810579895, "azul", B_, "RM sem radiação ionizante", "20", "Azul: tabela TC × RM da lâmina 20; viva na aula 02."),
 # C — dopamina e modelo (23–36)
 ak("ak-vias", 1541613861907, G(1), C_, "Vias dopaminérgicas e sintomas", "24; 25", "Verde: lâminas 24–25 (hipótese dopaminérgica)."),
 au("c-d1-d2", "In the <b>dopamine hypothesis</b>, positive symptoms come from mesolimbic {{c1::D2::D1/D2}} hyperactivity and negative symptoms from cortical {{c1::D1::D1/D2}} hypoactivity",
    G(1), C_, "Receptores D1 e D2", "25", "central", NAO, EP, "Verde: lâmina 25.", extra="- Antipsychotics block D2, so they treat positive more than negative symptoms",
    duplicacao_ok="ganho: o receptor de cada via; ak-vias cobra as vias"),
 ak("ak-alvo", 1483845020612, {1: Z}, C_, "Alvo dos antipsicóticos", "24; 23", "Azul: lâmina 23 (antipsicóticos bloqueiam D2)."),
 ak("ak-nigro", 1483845029571, {1: Z}, C_, "Bloqueio nigroestriatal", "24", "Azul: lâmina 24.",
    extra_add="- Antipsychotics blocking D2 here cause parkinsonism-like effects"),
 ak("ak-tubero", 1483845044133, {1: Z}, C_, "Bloqueio tuberoinfundibular", "24", "Azul: lâmina 24.",
    extra_add="- Dopamine normally inhibits prolactin release"),
 ak("ak-comt", 1485226927627, G(1, 2), C_, "COMT degrada dopamina", "26", "Verde: lâmina 26."),
 au("c-comt-val", "The COMT <b>{{c1::Val::Val/Met}} allele</b> breaks down prefrontal dopamine faster, worsening prefrontal performance and possibly raising schizophrenia risk",
    {1: Z}, C_, "Alelos Val e Met da COMT", "27", "central", NAO, EP, "Azul: lâmina 27.",
    extra="- The Met allele is protective<br>- COMT lies on chromosome 22q"),
 ak("ak-maconha", 1484687045054, G(1), C_, "Maconha e psicose", "28", "Verde: lâmina 28 (dose-resposta aos 18 anos)."),
 au("c-modelo", ORG("Developmental model of <b>psychosis</b>:<br>- early factors (obstetric complications, genes) → {{c1::cognitive deficits}}<br>- proximal factors (cannabis, chronic social anxiety) → {{c2::dopamine dysregulation}} → psychosis"),
    {1: Z, 2: V}, C_, "Modelo de fatores precoces e proximais", "29; 35", "central", NAO, EP, "Verde/azul: lâminas 29–35.",
    extra="- Symptoms usually start around 20 years of age"),
 ak("ak-clozapina", 1485220015721, {1: Z}, C_, "Clozapina no refratário", "36; 2", "Azul: caso sem melhora com risperidona; lâmina 36."),
 # D — sinapse, inflamação e privilégio imune (37–48)
 au("d-espinhas", "In <b>schizophrenia</b>, cortical neurons have smaller soma and fewer {{c1::dendritic spines}}, attributed to sublethal apoptotic signaling at the synapse",
    {1: Z}, D_, "Patologia sináptica", "37; 39", "central", NAO, EP, "Azul: lâminas 37–39.",
    extra="- Neurons are not lost; their connections shrink"),
 au("d-il1", "Brain volume loss in <b>schizophrenia</b> correlates with inflammatory markers such as {{c1::IL-1β}} and with microglial activation",
    {1: Z}, D_, "Neuroinflamação", "40; 41", "central", NAO, EP, "Azul: lâminas 40–42.",
    extra="- Exercise lowers IL-6 and may help cognition"),
 au("d-privilegio", "Grafts placed in the <b>brain</b> survive unless the host was already sensitized, showing the CNS {{c1::immune privilege}}",
    G(1), D_, "Privilégio imunológico do SNC", "43; 45", "central", NAO, EP, "Verde: lâminas 43–45 (Medawar, 1948).",
    extra="- Immune responses have two steps: sensitization and response; the brain blocks mainly sensitization"),
 au("d-linfaticos", "<b>CNS immune privilege</b> is relative, because the brain drains to cervical lymph nodes through {{c1::meningeal lymphatic}} vessels",
    {1: Z}, D_, "Linfáticos meníngeos", "44; 46", "central", NAO, EP, "Azul: lâminas 44–46 (comunicação bidirecional).", extra="- Communication between brain and immune system runs both ways"),
 ak("ak-esquizoafetivo", 1484687016622, {1: R}, D_, "Transtorno esquizoafetivo", "55", "Rosa: diagnóstico de Brian Wilson (lâmina 55)."),
]
SEM_IMAGEM = "fato clínico ou mecanismo sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {"ak-psicose": "- The case: a 30-year-old with schizophrenia since 25, agitated and aggressive", "ak-vias": "- Mesolimbic hyperactivity → positive; mesocortical hypoactivity → negative",
         "ak-alvo": "- Antipsychotics block D2 receptors", "ak-comt": "- MAO also degrades dopamine, to DOPAC and HVA", "ak-maconha": "- Risk rises with the number of times used by age 18",
         "ak-clozapina": "- The patient on risperidone was not improving", "d-privilegio": "", "ak-esquizoafetivo": "- Brian Wilson of the Beach Boys received this diagnosis",
         "ak-ventriculos": ""}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if VERSO.get(k):
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Reconhecer os grupos de sintomas e o curso da esquizofrenia, os achados de imagem, a hipótese dopaminérgica com o modelo de fatores precoces e proximais, e as pontes com a neuroimunologia (privilégio imune, neuroinflamação).",
 "centrais": [
   ("clínica e curso", "ak-psicose", "a-sintomas", "a-panss", "a-estagios", "a-sexo", "a-neurodesenvolvimento"),
   ("imagem", "ak-ventriculos", "sh-1791810579895"),
   ("dopamina e modelo", "ak-vias", "c-d1-d2", "ak-alvo", "ak-nigro", "ak-tubero", "ak-comt", "c-comt-val", "ak-maconha", "c-modelo", "ak-clozapina"),
   ("neuroimunologia", "d-espinhas", "d-il1", "d-privilegio", "d-linfaticos", "ak-esquizoafetivo"),
 ],
 "exemplos": ["caso do paciente em uso de risperidona", "Brian Wilson", "frases estigmatizantes"],
 "outras_aulas": [("TC e RM", "05 Tomografia e 12 Ressonância"), ("apoptose", "09 Lesão celular"), ("catecolaminas", "10 Ação hormonal")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
