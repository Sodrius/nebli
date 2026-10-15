# Especificação curada — Prática 3: identificação bacteriana / diagnóstico das infecções bacterianas (UC03 P2, Microbiologia; Profa. Elisabete Vicente; 42 lâminas, versão A 2023).
# Meios de cultura, hemólise, catalase/coagulase, Ziehl-Neelsen, Xpert e MIC já vivos (mb26, 27, 28, 32, 35, GR3): entram por sh(). P2 → entra suspensa.
RUN_ID = "uc03-mb40-20261015a"
SHORT = "mb40"
LESSON = "2026-uc03-microbiologia-40-pratica-3"
DECK = "NEBLI::UC03::P2::Microbiologia::Prática 3 — identificação bacteriana"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 15/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (chancre, secondary/tertiary syphilis, gumma, benzathine, yaws, bacitracin, optochin, Lowenstein, minimum inhibitory, MALDI, ELISA, PCR, dark-field; "
         "busca/anking.txt) e cópias NEBLI vivas das aulas 26, 27, 28, 32, 35 e GR3, 15/10: ")
EXCLUIDOS = [
 (1500748709824, "β-hemolítico e bacitracina com cloze em 'β': os cards de GAS e GBS cobram o nome"),
 (1500748915300, "α-hemolítico e optoquina: o card de S. pneumoniae cobra"),
 (1468605422972, "PCR definição: já vivo em Patologia 03 (compartilhado)"),
]
FORA_DO_RECORTE = ["Tabelas de provas para Enterobacteriaceae (EPM, MILi, citrato; lâminas 19–20): detalhe de bancada; só Tab.", "Bejel e bouba (14–15): rosa.",
                   "Calendário vacinal (40): UC de pediatria; Tab.", "Questões para revisão (41): usadas como alvo."]


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
EP = [1502041417776, 1500748877622, 1489091253860]
A_, B_, C_, D_, E_, F_ = "A-amostra", "B-microscopia-e-sifilis", "C-cultivo", "D-provas-bioquimicas", "E-sorologia-e-sensibilidade", "F-molecular-e-automacao"

CARDS = [
 # A — coleta (2–6)
 au("a-etapas", ORG("Steps of <b>bacterial diagnosis</b>:<br>1. specimen collection<br>2. {{c1::staining and microscopy}}<br>3. {{c2::culture}} with isolated colonies<br>4. biochemical tests<br>5. serology and susceptibility testing"),
    G(1, 2), A_, "Etapas do diagnóstico", "2; 17", "central", NAO, EP, "Verde: lâmina 2; questão de revisão 2.",
    extra="- Molecular and automated methods can shortcut culture"),
 au("a-antes-atb", "Samples for <b>bacterial culture</b> must be collected {{c1::before antibiotics}} are started",
    G(1), A_, "Coleta antes do antibiótico", "5", "central", NAO, EP, "Verde: lâmina 5.",
    extra="- The doctor should also tell the lab the suspected diagnosis"),
 au("a-representativa", "A <b>respiratory specimen</b> for culture must be sputum, not {{c1::saliva}}, so that it represents the infection",
    {1: Z}, A_, "Amostra representativa", "5", "central", NAO, EP, "Azul: lâmina 5."),
 au("a-esteril", "Normally <b>sterile sites</b>, where any bacterium grown is significant, include blood, {{c1::cerebrospinal fluid}}, joint fluid and pleural fluid",
    G(1), A_, "Sítio estéril × com microbiota", "5", "central", NAO, EP, "Verde: lâmina 5.",
    extra="- Growth from sites with normal microbiota needs interpretation"),
 # B — microscopia e sífilis (7–15)
 sh(1791576665617, "verde", B_, "Gram orienta o 1º antibiótico", "7", "Verde: lâmina 7; viva na aula 26."),
 sh(1791780535460, "verde", B_, "Ziehl-Neelsen", "8", "Verde: lâmina 8; viva no GR3."),
 au("b-lepra", "In suspected <b>leprosy</b>, acid-fast bacilli are searched for in a smear from the {{c1::earlobe}} or nasal secretions",
    {1: Z}, B_, "Hanseníase: lóbulo da orelha", "8; 3", "central", NAO, EP, "Azul: lâminas 3 e 8.",
    extra="- Mycobacterium leprae cannot be cultured in the lab"),
 sh(1791576674741, "verde", B_, "Campo escuro para T. pallidum", "9; 7", "Verde: lâmina 7; viva na aula 26."),
 ak("ak-cancro", 1502041417776, G(1, 2, 3, 4), B_, "Sífilis primária: cancro indolor", "11", "Verde: HY 1; lâmina 11 (cancro duro).",
    extra_add="- The chancre heals spontaneously; treatment is benzathine penicillin"),
 ak("ak-secundaria", 1502041641334, G(1, 2), B_, "Sífilis secundária: exantema", "12", "Verde: HY 1; lâmina 12 (mão)."),
 ak("ak-goma", 1502042167565, G(1), B_, "Sífilis terciária: gomas", "13", "Verde: HY 1; lâmina 13.",
    extra_add="- Tertiary syphilis also causes aortic aneurysms and neurosyphilis, 3–15 years later"),
 au("b-bejel", "The other <b>Treponema pallidum</b> subspecies cause the non-venereal treponematoses {{c1::bejel}} (endemic syphilis) and yaws",
    {1: R}, B_, "Bejel e bouba", "14; 15; 9", "lateral", NAO, EP, "Rosa: lâminas 9 e 14–15.",
    extra="- Spread by skin contact; yaws also by fomites"),
 # C — cultivo (16)
 sh(1791647817820, "verde", C_, "Ágar sangue", "16", "Verde: lâmina 16; viva na aula 27."),
 sh(1791647818320, "verde", C_, "Ágar chocolate", "16", "Verde: lâmina 16; viva na aula 27."),
 sh(1791647817219, "verde", C_, "MacConkey para Gram-negativos", "16", "Verde: lâmina 16; viva na aula 27."),
 sh(1791648194669, "azul", C_, "Lactose-negativos incolores", "19", "Azul: lâmina 19; viva na aula 28."),
 sh(1791648194793, "azul", C_, "Manitol salgado", "16", "Azul: lâmina 16; viva na aula 28."),
 au("c-lj", "<b>Mycobacterium tuberculosis</b> is cultured on {{c1::Löwenstein-Jensen}} medium, the gold standard for diagnosis despite its slow growth",
    G(1), C_, "Löwenstein-Jensen", "16; 37", "central", NAO, EP, "Verde: lâminas 16 e 37."),
 au("c-anaerobios", "<b>Anaerobes</b> are cultured in an anaerobic jar or chamber, or in liquid {{c1::thioglycolate}} medium",
    {1: R}, C_, "Cultivo de anaeróbios", "16", "lateral", NAO, EP, "Rosa: lâmina 16."),
 # D — provas bioquímicas (17–25)
 sh(1791763646494, "verde", D_, "Algoritmo Gram+: catalase", "24", "Verde: lâminas 23–24; viva na aula 35."),
 sh(1791763646344, "verde", D_, "Catalase: bolhas de O2", "24", "Verde: lâmina 24; viva na aula 35."),
 au("d-micrococcus", "Among <b>catalase-positive cocci</b>, Staphylococcus ferments glucose, whereas {{c1::Micrococcus}} only oxidizes it",
    {1: Z}, D_, "Prova O/F", "25; 22", "central", NAO, EP, "Azul: lâminas 22–25.",
    extra="- This is the oxidation/fermentation (O/F) test<br>- Micrococcus is a nonpathogenic aerobe of skin and mucosa"),
 sh(1791746129003, "verde", D_, "S. aureus coagulase-positivo", "25", "Verde: lâmina 25; viva na aula 35."),
 sh(1791763650819, "azul", D_, "Novobiocina resistente", "25", "Azul: lâmina 25; viva na aula 35."),
 ak("ak-gas", 1500748877622, G(1, 2), D_, "GAS: bacitracina sensível", "25", "Verde: HY 1; lâmina 25."),
 ak("ak-gbs", 1500748791992, G(1, 2), D_, "GBS: bacitracina resistente", "25", "Verde: HY 1; lâmina 25."),
 ak("ak-pneumo", 1500751600428, G(1, 2), D_, "S. pneumoniae: optoquina sensível", "25", "Verde: HY 1; lâmina 25."),
 # E — sorologia e sensibilidade (26–30)
 ak("ak-elisa", 1468605649044, G(1, 2), E_, "ELISA: anticorpo ligado a enzima", "26; 27", "Verde: lâminas 26–27."),
 au("e-sorologia", "<b>Serology</b> matters most for bacteria that cannot be cultured in vitro, such as {{c1::rickettsiae}}, comparing antibody titers at onset and two weeks later",
    {1: Z}, E_, "Quando usar sorologia", "27; 28", "central", NAO, EP, "Azul: lâminas 27–28; questão de revisão 14.",
    extra="- A rise in titer confirms recent infection"),
 sh(1791625436533, "azul", E_, "Teste tuberculínico (hipersensibilidade tardia)", "28", "Azul: lâmina 28; viva no GR3."),
 sh(1791647818945, "verde", E_, "Antibiograma: disco e MIC", "29", "Verde: lâmina 29; viva na aula 27."),
 sh(1791668526789, "verde", E_, "Definição de MIC", "30", "Verde: lâmina 30; viva na aula 32."),
 # F — molecular e automação (31–40)
 au("f-pcr", "<b>PCR</b> detects bacteria directly in tiny samples without prior culture and can distinguish pathogenic strains by detecting {{c1::virulence}} genes",
    {1: Z}, F_, "Vantagens da PCR", "31; 32", "central", NAO, EP, "Azul: lâminas 31–32."),
 au("f-sequenciamento", "<b>DNA sequencing</b> identifies hard-to-culture bacteria such as {{c1::Chlamydia}}",
    {1: Z}, F_, "Sequenciamento", "33", "central", NAO, EP, "Azul: lâmina 33.",
    extra="- Also used when M. tuberculosis fails to grow"),
 au("f-maldi", "{{c1::MALDI-TOF}} <b>mass spectrometry</b> identifies bacteria in minutes by comparing their protein pattern with a database",
    G(1), F_, "MALDI-TOF", "36", "central", NAO, EP, "Verde: lâmina 36; questão de revisão 18.",
    extra="- It does not rely on biochemical tests"),
 au("f-latex", "<b>Latex agglutination</b> detects bacterial antigens in CSF quickly but does not replace {{c1::culture}} to confirm bacterial meningitis",
    {1: Z}, F_, "Aglutinação em látex", "35", "central", NAO, EP, "Azul: lâmina 35."),
 sh(1791780540526, "verde", F_, "Xpert MTB/RIF", "37", "Verde: lâmina 37; viva no GR3."),
 au("f-rpob", "<b>Xpert</b> detects rifampicin resistance through mutations in the {{c1::rpoB}} gene",
    {1: Z}, F_, "Gene rpoB", "37", "central", NAO, EP, "Azul: lâmina 37; Identificação IV.",
    extra="- Results in about 2 hours"),
 au("f-resistencia", "Stopping <b>antibiotics</b> early or using them unnecessarily selects resistant superbugs such as {{c1::MRSA}}",
    G(1), F_, "Seleção de resistentes", "38", "central", NAO, EP, "Verde: lâmina 38."),
]
SEM_IMAGEM = "fato de laboratório sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {"a-representativa": "- Not from the fistulous tract or wound surface", "c-lj": "- Ziehl-Neelsen smear first; culture takes weeks", "c-anaerobios": "- Thioglycolate removes oxygen from the medium",
         "ak-elisa": "- Used for antibodies in serum and for circulating exotoxins", "f-pcr": "- Useful in biopsies and doubtful TB", "f-latex": "- Detects S. pneumoniae, N. meningitidis, H. influenzae b",
         "ak-gas": "", "ak-secundaria": "- Lesions are full of treponemes and also heal spontaneously", "f-resistencia": "- MRSA = methicillin-resistant Staphylococcus aureus<br>- Antibiotics are of little use in viral infections",
         "ak-gbs": "", "ak-pneumo": "- Viridans streptococci are optochin-resistant"}
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
 "objetivo": "Seguir as etapas do diagnóstico bacteriano (coleta correta, microscopia, cultivo em meios seletivos/diferenciais, provas bioquímicas dos cocos Gram-positivos, sorologia, antibiograma/MIC, PCR, sequenciamento, MALDI-TOF, Xpert) e reconhecer a sífilis pela clínica e pelo campo escuro.",
 "centrais": [
   ("amostra", "a-etapas", "a-antes-atb", "a-representativa", "a-esteril"),
   ("microscopia e sífilis", "sh-1791576665617", "sh-1791780535460", "b-lepra", "sh-1791576674741", "ak-cancro", "ak-secundaria", "ak-goma", "b-bejel"),
   ("cultivo", "sh-1791647817820", "sh-1791647818320", "sh-1791647817219", "sh-1791648194669", "sh-1791648194793", "c-lj", "c-anaerobios"),
   ("provas bioquímicas", "sh-1791763646494", "sh-1791763646344", "d-micrococcus", "sh-1791746129003", "sh-1791763650819", "ak-gas", "ak-gbs", "ak-pneumo"),
   ("sorologia e sensibilidade", "ak-elisa", "e-sorologia", "sh-1791625436533", "sh-1791647818945", "sh-1791668526789"),
   ("molecular e automação", "f-pcr", "f-sequenciamento", "f-maldi", "f-latex", "sh-1791780540526", "f-rpob", "f-resistencia"),
 ],
 "exemplos": ["tuberculose (baciloscopia × cultura × Xpert)", "hanseníase", "meningite", "MRSA"],
 "outras_aulas": [("meios e hemólise", "27"), ("Gram e assepsia", "26 e 28"), ("algoritmo Gram+", "35"), ("TB", "GR3")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
