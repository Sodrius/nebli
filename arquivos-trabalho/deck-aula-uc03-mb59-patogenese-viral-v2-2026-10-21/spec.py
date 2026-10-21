# Especificação curada — 64 Patogênese da infecção viral (UC03 P3, Microbiologia; 178 lâminas = 3 versões da mesma aula; a fala segue a versão III, lâminas 120–178).
# Ciclo básico: princípios da patogênese viral (entrada, disseminação, padrões de infecção, determinantes da doença, virulência, tropismo e evasão); vírus específicos só como exemplo de um princípio.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = "A aula ensina princípios de patogênese (infecção produtiva × abortiva, viremia, padrões de infecção, suscetibilidade, permissividade e acessibilidade, evasão ativa × passiva) que o AnKing só traz por vírus específico; busca nos três caminhos não achou esses cards."
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb59-20261021a"
SHORT = "mb59"
LESSON = "2026-uc03-microbiologia-59-patogenese-viral"
DECK = "NEBLI::UC03::P3::Microbiologia::Patogênese da infecção viral"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261021-CLAUDE-01 + ANTI-EXEMPLARES §1–16, 21/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (21/10): seções de recurso do AnKing (Bootcamp, mecanismos de infectividade viral; busca/secoes); palavra-chave e significado "
         "em AnKing, Referências Externas e NEBLI vivo (busca/semantica.jsonl, uma consulta por conceito). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)



A_, B_, C_, D_, E_, F_, G_, H_ = "A-infeccao", "B-entrada", "C-disseminacao", "D-padroes", "E-patogenese", "F-virulencia", "G-tropismo", "H-evasao"
EXCLUIDOS = []
FORA_DO_RECORTE = [
    "Lâminas 1–119 (versões I e II da mesma aula, por outros professores): repetem a versão III (lâminas 120–178), que é a que a transcrição acompanha.",
    "Figuras de livro e de artigos (ciclo do EBV, curvas de carga viral de HBV e HCV em detalhe, mapa de latências do EBV): ilustram, não ensinam alvo.",
    "Clínica dos vírus (sintomas de rinite, laringite, bronquiolite; quadro da hepatite; câncer cervical em detalhe), diagnóstico e tratamento: são da patologia e da UC19.",
    "Latência 0 a 3 do EBV e genes expressos em cada uma: detalhe de virologia molecular sem cobrança nas provas.",
]

FAIXAS = [[120, 178]]

CARDS = [
    # Definições (lâminas 120–122)
    au("au-infecao-def", "In {{c1::productive}} infection the virus makes new infectious virions, while in {{c1::abortive}} infection it does not",
       "V-pilar", A_, "Infecção produtiva × abortiva", 122, "lâminas 121–122; transcrição (infecção produtiva e abortiva; infecção não é doença)",
       extra="- Infection is not the same as disease: many infections are subclinical<br>- The virus is an obligate intracellular parasite"),
    # Portas de entrada (lâminas 124–127)
    K(1473289461901, "A-aula", B_, "Epitélio respiratório: escada mucociliar", 124, "lâmina 124 (a via respiratória tem muco, cílios e IgA); seção de pneumonia"),
    K(1516325251980, "A-aula", B_, "Influenza: transmissão por gotículas respiratórias", 124, "lâmina 124 (aerossóis); seção Bootcamp de virologia"),
    K(1506297282227, "A-aula", B_, "Paramixovírus (sarampo): gotículas respiratórias", 124, "lâmina 124 e transcrição (o sarampo entra pela via respiratória e se espalha)"),
    K(1516222322469, "A-aula", B_, "Rinovírus entra por ICAM-1", 127, "lâmina 127 (muitos receptores virais são moléculas de adesão: ICAM-1 e CAR); seção Bootcamp de virologia"),
    K(1608908651007, "A-aula", B_, "Coronavírus liga ACE2 nos pneumócitos tipo II", 127, "lâmina 127 e transcrição (receptor viral e célula-alvo no epitélio respiratório)"),
    # Via digestiva e disseminação (lâminas 128–130)
    K(1506610615157, "A-aula", B_, "Hepatite A: estável ao ácido", 128, "lâmina 128 (vírus entéricos resistem a pH, enzimas e bile)"),
    K(1516237532611, "A-aula", B_, "Gastroenterite viral: norovírus e rotavírus", 128, "lâmina 128 (vírus entéricos com infecção localizada)"),
    K(1516665596498, "A-aula", B_, "Rotavírus: via fecal-oral", 128, "lâmina 128 (vírus entéricos: infecção localizada com diarreia); seção Bootcamp de virologia"),
    K(1516218470870, "A-aula", B_, "Poliovírus: via fecal-oral", 128, "lâmina 128 (infecção sistêmica após replicar no intestino)"),
    au("au-viremia", "<b>Viremia</b> is {{c1::active}} if the virus replicated in organs and {{c2::passive}} if injected (insect, transfusion)",
       "V-pilar", C_, "Viremia ativa × passiva", 130, "lâminas 129–130; transcrição (sítio primário → linfa e sangue → sítio secundário)",
       extra="- Primary site of replication at the portal of entry; secondary site in the target organs<br>- Passive viremia: mosquito bite, contaminated needle or transfusion, dog bite"),
    # Padrões de infecção (lâminas 131–147)
    K(1506291152635, "A-aula", D_, "VZV: reativação por estresse, idade ou imunossupressão", 135, "lâmina 135 (reativação da latência)"),
    K(1503860841762, "A-aula", D_, "CMV: reativação em imunossuprimidos", 135, "lâmina 135 (reativação da latência)"),
    K(1503858394947, "A-aula", D_, "CMV: latente em células mononucleares", 135, "lâminas 135–137 (herpesvírus: latência)"),
    K(1506291111598, "A-aula", D_, "VZV: latente nos gânglios da raiz dorsal", 135, "lâmina 135 (herpesvírus: latência)"),
    K(1502153397982, "A-aula", D_, "HSV-1: latente no gânglio trigeminal", 136, "lâmina 136 (latência e reativação do HSV)"),
    K(1502152875721, "A-aula", D_, "Estresse reativa o HSV-1", 136, "lâmina 136 (reativação por estímulos como o estresse)"),
    K(1502154338212, "A-aula", D_, "HSV-2: latente nos gânglios sacrais", 136, "lâmina 136 (latência do HSV)"),
    K(1503854748516, "A-aula", D_, "EBV: latente em linfócitos B", 137, "lâmina 137 e transcrição (ciclo lítico no epitélio, latência nas células B de memória)"),
    K(1506552371527, "A-aula", D_, "HBV em recém-nascidos: 90% de infecção crônica", 140, "lâmina 140 e transcrição (via vertical → crônica; adulto → aguda em 90%)"),
    K(1506552065089, "A-aula", D_, "HBV: transmissão da mãe para o bebê no parto", 140, "lâmina 140 (via vertical)"),
    K(1506552205472, "A-aula", D_, "HBV é menos crônica que o HCV", 141, "lâminas 139–142 (padrão agudo e crônico das hepatites)"),
    K(1506630060423, "A-aula", D_, "HCV: 60–80% evoluem para infecção crônica", 142, "lâmina 142 (hepatite C: padrão crônico)"),
    K(1502067560663, "A-aula", D_, "HIV: latência clínica por até 10 anos", 144, "lâmina 144 e transcrição (padrão progressivo, set point e latência clínica)"),
    au("au-latencia-vs", "In HIV <b>clinical latency</b> the virus {{c1::replicates}} constantly, unlike the latency of herpesviruses",
       "A-aula", D_, "Conexão: latência viral × latência clínica", 144, "lâmina 144 e transcrição (a latência clínica do HIV não é latência viral)",
       extra="- Herpesvirus latency: the productive cycle is off and can be reactivated<br>- HIV clinical latency: no symptoms but constant replication until CD4 T cells fall"),
    au("au-padroes", ORG("<b>Infection patterns</b>:<br>- HSV and EBV: {{c1::latent}}<br>- HBV and HCV: {{c2::persistent}}<br>- HIV: {{c3::progressive}}"),
       "A-aula", D_, "Padrões de infecção viral e vírus típicos", 145, "lâminas 145–147; transcrição (aguda, latente, persistente e progressiva)",
       extra="- Acute infection has a clear start and end, even if it lasts months (HBV)<br>- The pattern depends on the virus, tropism, route, host response and immune evasion"),
    # Patogênese e fatores (lâminas 148–155)
    au("au-patogenese", ORG("<b>Viral pathogenesis</b>:<br>- tissue {{c1::destruction}}<br>- inflammatory {{c2::cytokines}}<br>- cell {{c3::dysfunction}}"),
       "A-aula", E_, "Patogênese: destruição, citocinas e disfunção celular", 150, "lâmina 150; transcrição (destruição do tecido, citocinas inflamatórias, disfunção e efeito parácrino)",
       extra="- Some viruses also induce tumors<br>- Severe cases of influenza and COVID-19 can be immunopathology, in which the inflammatory response causes the damage"),
    au("au-3-fatores", ORG("<b>Productive infection</b> needs:<br>- {{c1::susceptibility}}: receptor<br>- {{c2::permissiveness}}: cell factors for replication<br>- {{c3::accessibility}} to the target cell"),
       "V-pilar", E_, "Infecção produtiva: suscetibilidade, permissividade e acessibilidade", 152, "lâminas 151–152; transcrição e apostila guia de Micro (hemácia não é permissiva; febre amarela só é acessível pelo mosquito)",
       extra="- The immune response also decides whether the infection is established, eliminated or persists<br>- A red cell may bind the virus but has no machinery to replicate it"),
    au("au-virulencia", "Viral <b>virulence factors</b>, such as the rotavirus {{c1::NSP4}}, favor replication, spread, immune evasion or direct toxicity",
       "A-aula", F_, "Fatores de virulência", 155, "lâminas 153–155; transcrição (moléculas que dão capacidade replicativa, evasão ou toxicidade direta)",
       extra="- Virulence is the relative capacity of a virus to cause disease<br>- It depends on the viral variant, the dose, the route and host susceptibility"),
    K(1516665751235, "V-pilar", F_, "Rotavírus: enterotoxina NSP4 causa diarreia aquosa", 157, "lâminas 156–157 (NSP4 como fator de virulência); seção Bootcamp de virologia"),
    K(1516665990169, "A-aula", F_, "NSP4 aumenta a permeabilidade ao Cl−", 157, "lâmina 157 (cálcio intracelular, saída de cloro e de água)"),
    K(1516666902436, "A-aula", F_, "Rotavírus causa deficiência secundária de lactase", 157, "lâmina 157 (destruição das células produtoras de lactase: diarreia osmótica)"),
    K(1516323168130, "A-aula", F_, "Virada antigênica: pandemias de influenza", 159, "lâmina 159 (pandemias × vírus sazonais: diferença de virulência)"),
    K(1394068322402, "A-aula", F_, "Condiloma acuminado: HPV 6 ou 11", 161, "lâminas 160–162 (HPV de baixo risco: verrugas)"),
    K(1493218180866, "A-aula", F_, "HPV nas cordas vocais: papilomatose laríngea", 162, "lâmina 162 (a região anatômica muda a gravidade)"),
    K(1405375421095, "A-aula", F_, "HPV 16 e 18: principais causas de câncer cervical", 163, "lâminas 163–164 (tipos de alto risco: 16 e 18 respondem por 70%)"),
    # Tropismo (lâminas 165–167)
    K(1516222409950, "A-aula", G_, "Rinovírus cresce melhor a 33 °C", 166, "lâmina 166 (rinofaringe, temperatura mais baixa)"),
    K(1516222135232, "A-aula", G_, "Rinovírus é lábil ao ácido", 166, "lâmina 166 (se engolido, é inativado no estômago)"),
    K(1516218404816, "A-aula", G_, "Poliovírus é estável ao ácido", 167, "lâmina 167 (pequenas mudanças no capsídeo mudam o tropismo)"),
    K(1516219553378, "A-aula", G_, "Vacina Sabin: poliovírus vivo atenuado", 167, "lâmina 167 (menos virulento: não chega ao sistema nervoso)"),
    # Evasão (lâminas 168–175)
    au("au-evasao", ORG("<b>Viral immune evasion</b>:<br>- active: needs viral {{c1::proteins}}<br>- passive: {{c2::inoculum}}, tropism, route<br>- passive: {{c3::variability}}"),
       "A-aula", H_, "Evasão ativa × passiva", 168, "lâmina 168; transcrição (evasão ativa requer síntese de proteínas virais; passiva não)",
       extra="- Active: HPV E6 and E7 alter the interferon response; latency in EBV<br>- Passive: a large inoculum, a tropism far from the immune response, the route of infection"),
    K(1463105909117, "A-aula", H_, "HPV de alto risco: E6 destrói p53", 169, "lâmina 169 (as proteínas E6 e E7 alteram a resposta da célula)"),
    K(1463105915437, "A-aula", H_, "HPV de alto risco: E7 destrói Rb", 169, "lâmina 169 (as proteínas E6 e E7 alteram a resposta da célula)"),
    K(1502718274711, "A-aula", H_, "HPV infecta o estrato basal", 173, "lâminas 173–174 (o ciclo ocorre nas camadas suprabasais, longe da resposta imune)"),
    K(1516474304091, "A-aula", H_, "Raiva: viaja retrógrado pelos nervos periféricos", 174, "lâmina 174 (tropismo neuronal como evasão passiva)"),
    K(1506629766099, "A-aula", H_, "HCV: variabilidade antigênica do envelope", 175, "lâmina 175 (a variabilidade de vírus de RNA dificulta a resposta)"),
]


_CZ = _re.compile(r"\{\{c(\d+)::((?:(?!\}\}).)*?)(::(?:(?!\}\}).)*?)?\}\}", _re.S)
def _bold_cloze(t):
    def sub(m):
        corpo = m.group(2)
        if "<b>" not in corpo and "<strong>" not in corpo:
            corpo = f"<b>{corpo}</b>"
        return "{{c%s::%s%s}}" % (m.group(1), corpo, m.group(3) or "")
    return _CZ.sub(sub, t)
for _c in CARDS:
    if _c["kind"] == "autoral":
        _c["text"] = _bold_cloze(_c["text"])

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1473289461901": "- Together with IgA and macrophages, it keeps most inhaled viruses from reaching the cells",
 "ak1506297282227": "- Measles enters by the respiratory route, then reaches other organs and immune cells (viremia), with the rash in the periphery",
 "ak1516325251980": "- Aerosols spread influenza and coronavirus; contaminated hands and fomites spread rhinovirus",
 "ak1516222322469": "- Adenoviruses and coxsackieviruses use CAR, a tight-junction molecule, and can disrupt the epithelium",
 "ak1608908651007": "- Susceptibility needs the receptor; permissiveness needs the cell machinery for replication",
 "ak1506610615157": "- Enteric viruses face the acid stomach, digestive enzymes and bile salts",
 "ak1516665596498": "- Localized enteric infection: replication in the intestinal epithelium and release in the stool",
 "ak1516218470870": "- It replicates in the intestine, reaches the blood (viremia) and then the central nervous system",
 "ak1503858394947": "- Latency: the productive cycle is off, but it can be reactivated",
 "ak1506291152635": "- Reactivation can be triggered by stress, aging or immunosuppression",
 "ak1503860841762": "- Reactivation is seen in organ transplant and AIDS patients",
 "ak1502154338212": "- Reactivated genital herpes returns along the sensory nerves",
 "ak1506552065089": "- Vertical transmission raises the chance of chronic infection",
 "ak1516237532611": "- They are non-enveloped, resist the gut environment and are shed in the stool",
 "ak1506291111598": "- Latency: the productive cycle is off, but it can be reactivated",
 "ak1502153397982": "- The virus infects the epithelium, goes up the neuron and switches to latency",
 "ak1502152875721": "- The reactivated virus comes back down the axon and replicates in the epithelium",
 "ak1503854748516": "- EBV has a lytic cycle in the epithelium and latency in memory B cells, where it is invisible to the immune system",
 "ak1506552371527": "- Infection by the vertical route becomes chronic more often than infection in adults",
 "ak1506552205472": "- In adults HBV is usually acute and cleared in about six months",
 "ak1506630060423": "- Hepatitis C is chronic in most cases, with the viral genome detected for more than six months",
 "ak1502067560663": "- Viral load set point after the acute phase predicts how fast AIDS develops",
 "ak1516665751235": "- NSP4 also acts on neighboring uninfected cells (paracrine effect)",
 "ak1516665990169": "- NSP4 raises intracellular calcium, chloride leaves the cell and water follows",
 "ak1516666902436": "- Undigested lactose draws water into the gut: osmotic diarrhea, so milk worsens it",
 "ak1516323168130": "- Pandemic strains kill millions, seasonal strains much less",
 "ak1394068322402": "- Low-risk HPV types cause warts and low-grade lesions",
 "ak1405375421095": "- High-risk types cause nearly all cervical cancers; HPV 16 and 18 together about 70%",
 "ak1516222409950": "- The cooler nasopharynx is a favorable microenvironment",
 "ak1516222135232": "- If swallowed, it is inactivated by the stomach acid, so it replicates in the respiratory epithelium",
 "ak1516218404816": "- A poliovirus close relative of rhinovirus can cross the acid stomach and bile because of small capsid changes",
 "ak1516219553378": "- The attenuated strain replicates in the gut but does not reach the central nervous system",
 "ak1463105909117": "- E6 and E7 also alter the innate response of the cell to the virus",
 "ak1463105915437": "- E6 and E7 also alter the innate response of the cell to the virus",
 "ak1502718274711": "- The virus cycle occurs in suprabasal layers, away from the dermis where the immune response acts",
 "ak1516474304091": "- Inside axons the virus is far from the immune response",
 "ak1506629766099": "- RNA viruses mutate more: influenza and HIV vary a lot",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
exec((HERE / "exclusoes.py").read_text(encoding="utf-8")) if (HERE / "exclusoes.py").exists() else None

SEM_IMAGEM = "fato ou conjunto sem estrutura a reconhecer; as figuras da aula são esquemas de livro e fotografias clínicas"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
DUPLICACAO = {"au-virulencia": "o card do NSP4 diz o efeito da proteína; este define fator de virulência em geral, com o NSP4 como exemplo", "au-latencia-vs": "au-padroes cita HSV/EBV como latentes e HIV como progressivo; este contrasta o significado de latência nos dois casos", "au-evasao": "E6 e E7 também têm cards próprios; aqui é o quadro ativa × passiva"}
for _k, _v in DUPLICACAO.items():
    _c = next((c for c in CARDS if c["key"] == _k), None)
    if _c:
        _c["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
    "objetivo": "Explicar como um vírus infecta o hospedeiro suscetível: portas de entrada e disseminação, padrões de infecção, determinantes da doença, virulência, tropismo e evasão da resposta imune.",
    "centrais": [("infecção", "au-infecao-def"), ("disseminação", "au-viremia"), ("padrões", "au-padroes"), ("determinantes", "au-patogenese", "au-3-fatores"), ("evasão", "au-evasao")],
    "exemplos": ["rotavírus", "HPV", "influenza", "rinovírus × poliovírus", "HIV"],
    "outras_aulas": [("replicação viral", "58 Multiplicação viral"), ("resposta imune a vírus", "63 Resposta imune a vírus e fungos"), ("carcinógenos virais", "78 Agentes carcinogênicos biológicos"), ("HIV em detalhe", "aula de HIV")],
}
_slide = lambda c: int(_re.search(r"\d+", c["evid"]).group())
CARDS.sort(key=_slide)
