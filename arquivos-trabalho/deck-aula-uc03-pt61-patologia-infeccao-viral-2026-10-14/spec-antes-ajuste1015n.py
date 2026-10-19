# Especificação curada — Patologia da infecção viral (UC03 P3, Patologia; Prof. Luiz F. Ferraz da Silva; 29 lâminas).
# Padrão refinado de 14/10 (ordem estrita das lâminas; aprofundamento básico; casos de fronteira em percurso-aula.md).
# Tropismo/patogênese = 59; transformação por HPV/HBV = P4 (agentes carcinogênicos biológicos); inflamação crônica = 62; IHC/colorações = 03.
RUN_ID = "uc03-pt61-20261014a"
SHORT = "pt61"
LESSON = "2026-uc03-patologia-61-patologia-infeccao-viral"
DECK = "NEBLI::UC03::P3::Patologia::Patologia da infecção viral"
CRITERIOS = "MEMORY.md (14/10, F-20261014-CLAUDE-02) + PLANO-CONTINUACAO-DECKS (C1–C7) + PLANO-CARDS-TABS, 14/10/2026"
_IMG = {"negri": "jpeg", "sarampo": "jpeg", "sincicio": "jpeg", "coilocito": "jpeg", "cinetica": "png", "interferon": "jpeg",
        "estado-antiviral": "jpeg", "nk": "jpeg", "ciclo-hbv": "jpeg", "vidro-fosco": "jpeg", "ihc-hbsag": "jpeg", "ihc-hbcag": "jpeg",
        "portal": "jpeg", "necrose": "jpeg", "apoptose": "jpeg", "interface": "jpeg", "linfocito-b": "jpeg", "cd8": "jpeg", "tricromico": "jpeg"}
MEDIA = {f"pt61-{n}.{e}": f"img/pt61-{n}.{e}" for n, e in _IMG.items()}
F = lambda n, w=440: f'<img src="pt61-{n}.{_IMG[n]}" width="{w}">'
V, Z, R = 3, 4, 5
BUSCA = ("AnKing e Referências Externas por frases e sinônimos (busca/anking.txt, 35 consultas; busca/anking2.txt, 12), cópias NEBLI vivas "
         "de toda a UC03 conferidas por tema (NK, interferon, apoptose, células gigantes, fígado, IHC), 14/10: ")
EXCLUIDOS = [
 (1502152318872, "Cowdry bodies em herpesvírus: herpes não está nas lâminas de 2026; Cowdry citado só no Extra do sarampo"),
 (1503861947945, "CMV ‘olho de coruja’: vírus da monitoria antiga, fora das lâminas atuais"),
 (1506628692802, "vírus com corpúsculos de Councilman (HAV, febre amarela): lista lateral; o autoral pergunta o conceito"),
 (1463105909117, "HPV E6 → p53: mecanismo de transformação, aula de agentes carcinogênicos biológicos (P4)"),
 (1506553260599, "sorologia do HBV: Micro/clínica, fora das lâminas"),
 (1506551427767, "HBV tem envelope (sim/não): coberto pelo card de estrutura (HBsAg no envelope)"),
 (1497450277629, "enzimas induzidas por IFN levando à apoptose: mecanismo molecular, no Tab do estado antiviral"),
 (1506299214372, "células de Warthin-Finkeldey em linfócitos: sarampo linfonodal, fora das lâminas"),
]
FORA_DO_RECORTE = [
 "Vírus da monitoria antiga ausentes das lâminas de 2026: CMV, HSV, EBV, adenovírus, VSR, influenza, zika, HIV, febre amarela.",
 "Mecanismos de transformação (HPV E6/E7, HBV e carcinoma hepatocelular): P4, agentes carcinogênicos biológicos.",
 "Tropismo e receptores virais: aula 59 Patogênese da infecção viral.",
 "Sorologia das hepatites e tratamento antiviral: Micro/clínica.",
]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


EP_LESAO = [1487117293576, 1521424292009, 1506459892639]        # mecanismo de lesão celular por vírus/células
EP_ACHADO = [1516474665512, 1385335604751, 1715273523479]       # achado histológico → nome
EP_IMUNE = [1489970693302, 1487117314403, 1520301453074]        # resposta antiviral
EP_HBV = [1506551930834, 1715273523479, 1521424595880]          # HBV e fígado
NAO = "AnKing e externos não têm este alvo geral (só vírus/doença específica ou outra formulação)."

A_, B_, C_, D_, E_ = "A-duas-vias", "B-efeitos-celulares", "C-resposta-do-hospedeiro", "D-hbv", "E-hepatite"
ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'

CARDS = [
 # ---------- A. Lâmina 2 ----------
 au("a-dano-duplo", ORG("<b>Viral disease</b> injures tissue by two routes:<br>- direct {{c1::cytopathic effect}} of viral replication<br>- the host {{c2::immune response}} against infected cells"),
    {1: V, 2: V}, A_, "Duas vias de lesão na infecção viral", "2; Robbins p. 343", "central", NAO, EP_LESAO,
    "Verde: princípio que organiza a aula inteira (lâmina 2); em tópicos (F-20261014-CLAUDE-03).", duplicacao_ok="ganho: organizador das duas vias; b-cpe define o termo",
    extra="- A third outcome is transformation of the infected cell (neoplasia)"),

 # ---------- B. Lâminas 3–8 ----------
 au("b-efeitos", ORG("<b>Viruses</b> injure infected cells by:<br>- cell death by {{c1::lysis}} or {{c1::apoptosis}}<br>- {{c2::cytopathic changes}} such as inclusions and syncytia<br>- {{c3::transformation}}, which can lead to neoplasia"),
    {1: V, 2: V, 3: V}, B_, "Organizador dos efeitos dos vírus sobre a célula", "3–4", "central", NAO, EP_LESAO,
    "Verde: organiza as lâminas 3–4; cloze em cada item (F-20261014-CLAUDE-03).", duplicacao_ok="ganho: composição do conjunto; b-apoptose e b-cpe aprofundam itens",
    extra="- Lysis spills cell contents and triggers acute inflammation<br>- Other cytopathic changes: blocked host protein synthesis, cytoskeleton depolymerization, mitotic arrest"),
 au("b-apoptose", "Viral assembly can overload the endoplasmic reticulum, and this {{c1::ER stress}} drives the infected cell into <b>apoptosis</b>",
    {1: R}, B_, "Como vírus induzem apoptose", "3–4; Robbins p. 344", "lateral", NAO, EP_LESAO,
    "Rosa: aprofundamento do item apoptose (a apoptose em si é cobrada no organizador); cloze no mecanismo nomeado (F-20261014-CLAUDE-04).",
    extra="- Some viruses also carry pro-apoptotic proteins (e.g., HIV Vpr)<br>- Apoptosis removes the cell without spilling its contents, unlike lysis"),
 au("b-sintese", "Some viruses, such as <b>poliovirus</b>, block host {{c1::protein synthesis}} while still translating their own mRNA",
    {1: R}, B_, "Bloqueio da síntese proteica do hospedeiro", "3–4; Robbins p. 343", "lateral", NAO, EP_LESAO,
    "Rosa: aprofundamento básico de um item da lâmina 3 (caso de fronteira)."),
 au("b-cpe", "Structural changes caused directly by viral replication in infected cells, such as inclusions and syncytia, are the {{c1::cytopathic effect}}",
    {1: V}, B_, "Definição de efeito citopático", "4–5; prova 2024 P3 1.2; prova 2017 P3 1.3", "prova", NAO, EP_ACHADO,
    "Verde: conceito central das lâminas 4–8, cobrado em 2024 e 2017.",
    extra="- Seen on histology, it lets the pathologist suspect a viral infection"),
 au("b-inclusao", "Accumulations of viral proteins or particles at the site of viral assembly appear as {{c1::inclusion bodies}}",
    {1: Z}, B_, "Corpúsculo de inclusão", "5; prova 2024 P3 1.2; Robbins p. 343", "prova", NAO, EP_ACHADO,
    "Azul: prova 2024 (inclusão por acúmulo de subunidades).",
    extra="- They may be nuclear or cytoplasmic, depending on where the virus replicates"),
 ak("ak-negri", 1516474665512, {1: V, 2: V}, B_, "Inclusão citoplasmática: Negri (raiva)", 5, "Verde: HY 2; exemplo da lâmina 5.",
    extra_add="- Neuron with a Negri body (arrow)<br>" + F("negri")),
 au("b-sarampo", F("sarampo", 380) + "<br>Measles virus can form eosinophilic {{c1::intranuclear}} inclusions in infected cells",
    {1: Z}, B_, "Inclusão nuclear: sarampo", 6, "central", NAO, EP_ACHADO, "Azul: exemplo da lâmina 6.",
    extra="- Pathologists call these Cowdry type A inclusions<br>- Measles also fuses cells into giant cells"),
 au("b-sincicio", F("sincicio", 300) + "<br>Multinucleated cells formed when viral fusion proteins fuse an infected cell with its neighbors are {{c1::syncytia}}",
    {1: V}, B_, "Sincício (reconhecer e definir)", "7; prova 2015 P2 4.3", "central", NAO, EP_ACHADO, "Verde: lâmina 7; reconhecer na imagem."),
 ak("ak-proteina-f", 1506459892639, {1: V}, B_, "Proteína F causa sincícios", 7, "Verde: HY 1; mecanismo do sincício da lâmina 7."),
 au("b-sincicio-granuloma", "A viral syncytial giant cell lacks the epithelioid macrophages and {{c1::lymphocyte rim}} of a granuloma giant cell",
    {1: Z}, B_, "Célula gigante viral × de granuloma", "7; prova 2017 P3 1.3", "prova", NAO, EP_ACHADO,
    "Azul: discriminante da prova 2017.", extra="- Granuloma giant cells come from fused macrophages, inside an organized granuloma"),
 ak("ak-coilocito", 1385335604751, {1: V, 2: V, 3: V}, B_, "Coilócito (HPV)", 8, "Verde: HY 1; lâmina 8 e prova 2016.",
    extra_add=F("coilocito")),
 au("b-hpv16", "Koilocytes with dysplasia point to a high-risk HPV type such as HPV {{c1::16}}, linked to cervical carcinoma",
    {1: Z}, B_, "Coilocitose e HPV de alto risco", "8; 4; prova 2016 P3 1.2", "prova", NAO, EP_ACHADO, "Azul: prova 2016.",
    extra="- Low-risk types (e.g., HPV 6, 11, 2) cause benign warts<br>- How HPV transforms cells is detailed in the carcinogenic agents lesson"),

 # ---------- C. Lâminas 9–13 ----------
 au("c-resposta", ORG("<b>Host response</b> to viruses:<br>- acute phase: {{c1::barriers}}, {{c1::NK cells}}, {{c1::macrophages}}, {{c1::complement}}<br>- subacute and chronic phases: {{c2::T lymphocytes}}, {{c2::B cells}} and {{c2::antibodies}}"),
    {1: V, 2: V}, C_, "Organizador: resposta inata (aguda) × adaptativa (subaguda/crônica)", "9", "central", NAO, EP_IMUNE,
    "Verde: organiza a lâmina 9; itens de cada fase ocultos juntos (o conjunto é o alvo; F-20261014-CLAUDE-03)."),
 au("c-cinetica", "In acute viral infection, interferon and NK activity peak within days, whereas T cells peak around day {{c1::8–10}}",
    {1: R}, C_, "Cinética da resposta antiviral", 10, "lateral", NAO, EP_IMUNE, "Rosa: leitura do gráfico da lâmina 10 (caso de fronteira).",
    extra="- Antibodies rise later and persist<br>" + F("cinetica")),
 ak("ak-ifn", 1489970693302, {1: V}, C_, "IFN-α/β: produzidos pela célula infectada, agem nas vizinhas", 11, "Verde: HY 1; lâmina 11.",
    extra_add=F("interferon")),
 au("c-estado-antiviral", "Type I interferon puts neighboring cells into an {{c1::antiviral state}}, degrading mRNA and inhibiting protein synthesis",
    {1: Z}, C_, "Estado antiviral", 12, "central", NAO, EP_IMUNE, "Azul: lâmina 12.", extra=F("estado-antiviral")),
 ak("ak-ifn-mhc", 1520301453074, {1: V}, C_, "IFN tipo I aumenta MHC-I", 12, "Verde: HY 1; lâmina 12."),
 ak("ak-ifn-nk", 1487117310594, {1: V}, C_, "IFN tipo I ativa NK", 12, "Verde: HY 1; lâmina 12."),
 ak("ak-nk-mhc", 1487117314403, {1: V, 2: V}, C_, "NK mata células sem MHC-I", 13, "Verde: HY 1; lâmina 13."),
 ak("ak-nk-perforina", 1487117308213, {1: V}, C_, "NK mata por perforina e granzimas", 13, "Verde: HY 2; lâmina 13."),

 # ---------- D. Lâminas 14–18 ----------
 au("d-hbv-estrutura", "In <b>hepatitis B virus</b>, {{c1::HBsAg}} lies in the lipid envelope, whereas {{c2::HBcAg}} forms the core around the DNA",
    {1: V, 2: V}, D_, "Estrutura do HBV: HBsAg × HBcAg", 14, "central", NAO, EP_HBV, "Verde: lâmina 14; base das lâminas 17–18.",
    extra="- HBeAg is a secreted form related to the core protein"),
 au("d-cccdna", "In the hepatocyte nucleus, HBV DNA is converted into {{c1::cccDNA}}, the stable template for viral transcription",
    {1: Z}, D_, "cccDNA no ciclo do HBV", 15, "central", NAO, EP_HBV, "Azul: lâmina 15; explica a persistência da infecção.",
    extra="- cccDNA = covalently closed circular DNA<br>" + F("ciclo-hbv")),
 ak("ak-hbv-rt", 1506551930834, {1: Z}, D_, "Transcriptase reversa do HBV", 15, "Azul: HY 3; ciclo da lâmina 15."),
 ak("ak-vidro", 1715273523479, {1: V, 2: V}, D_, "Hepatócito em vidro despolido (HBV crônico)", 16, "Verde: achado da lâmina 16.",
    extra_add=F("vidro-fosco")),
 au("d-vidro-hbsag", "<b>Ground-glass hepatocytes</b> owe their finely granular cytoplasm to accumulated {{c1::HBsAg}} in the endoplasmic reticulum",
    {1: V}, D_, "Por que vidro despolido", "16–17; Robbins p. 859", "central", NAO, EP_HBV, "Verde: liga as lâminas 16 e 17.",
    duplicacao_ok="ganho: mecanismo (HBsAg acumulado); o AnKing pergunta o nome do achado"),
 sh(1791810364524, "azul", D_, "IHC localiza proteínas in situ", 17, "Azul: princípio da IHC (aula 03) antes das lâminas 17–18."),
 sh(1791810365149, "rosa", D_, "Cromógeno DAB marrom", 17, "Rosa: a cor marrom das lâminas 17–18 (aula 03)."),
 au("d-ihc", "On HBV immunohistochemistry, HBsAg stains the hepatocyte {{c1::cytoplasm}}, whereas HBcAg stains the {{c2::nucleus}}",
    {1: Z, 2: Z}, D_, "IHC de HBsAg × HBcAg", "17–18", "central", NAO, EP_HBV, "Azul: lâminas 17 e 18.", duplicacao_ok="ganho: localização de cada antígeno na IHC; nenhum outro card pergunta núcleo × citoplasma",
    extra=F("ihc-hbsag", 300) + " " + F("ihc-hbcag", 300)),

 # ---------- E. Lâminas 19–29 ----------
 au("e-portal", "In chronic viral hepatitis, the mononuclear infiltrate concentrates in the {{c1::portal tracts}}, where blood and inflammatory cells enter the lobule",
    {1: Z}, E_, "Infiltrado portal na hepatite crônica", "19; prova 2017 P3 4.1", "prova", NAO, EP_HBV, "Azul: lâmina 19 e prova 2017.",
    extra=F("portal")),
 sh(1791022170201, "azul", E_, "Tríade portal", 20, "Azul: fígado normal da lâmina 20 (Correlação)."),
 sh(1791022170551, "rosa", E_, "Zona III centrolobular", 20, "Rosa: zonas 1–3 numeradas na lâmina 20 (Correlação)."),
 ak("ak-balonizacao", 1521424292009, {1: Z}, E_, "Necrose do hepatócito: balonização", "21–22", "Azul: HY 3; lesão hepatocitária das lâminas 21–22."),
 ak("ak-necrose-ponte", 1521424595880, {1: V}, E_, "Necrose em ponte", 23, "Verde: HY 1; necrose extensa da lâmina 23.",
    extra_add=F("necrose")),
 sh(1791625429957, "verde", E_, "CD8 mata células infectadas por apoptose", 24, "Verde: princípio da apoptose da lâmina 24 (aula 45)."),
 au("e-councilman", F("apoptose", 300) + "<br>Apoptotic hepatocytes shrink into dense eosinophilic {{c1::Councilman bodies}}",
    {1: V}, E_, "Corpúsculo de Councilman (reconhecer)", "24; Robbins p. 859", "central", NAO, EP_HBV, "Verde: lâmina 24.",
    extra="- Usually killed by antiviral CD8+ T cells and quickly removed by macrophages"),
 au("e-interface", "Inflammation spilling from the portal tract into the adjacent periportal hepatocytes is called {{c1::interface}} hepatitis",
    {1: V}, E_, "Hepatite de interface", "25; Robbins p. 860", "central", NAO, EP_HBV, "Verde: distribuição da lesão (lâmina 25).",
    extra="- Persistent interface injury heralds progressive liver damage<br>" + F("interface")),
 au("e-linfocito-b", "In chronic viral hepatitis, {{c1::B}} lymphocytes cluster in portal lymphoid aggregates",
    {1: Z}, E_, "Perfil B: agregados linfoides portais", 26, "central", NAO, EP_HBV, "Azul: lâmina 26.", extra=F("linfocito-b")),
 au("e-imunopatologia", "Hepatocyte injury in hepatitis B comes mainly from {{c1::CD8+ T cells}} attacking infected hepatocytes, not from the virus itself",
    {1: V}, E_, "Lesão do HBV é imunomediada", "27; Robbins p. 344", "central", NAO, EP_HBV,
    "Verde: lâmina 27; fecha a lâmina 2 (resposta imune como causa da lesão).", extra=F("cd8"),
    duplicacao_ok="ganho: aplicação à hepatite B; o compartilhado da 45 pergunta o mecanismo geral (apoptose)"),
 sh(1791022173275, "azul", E_, "Reticulina delineia nódulos", 28, "Azul: coloração da lâmina 28 (Correlação)."),
 sh(1791810362575, "azul", E_, "Tricrômico cora colágeno de azul", 29, "Azul: coloração da lâmina 29 (aula 03)."),
 au("e-fibrose", "Repeated immune-mediated injury in chronic hepatitis forms fibrous septa linking portal tracts, called {{c1::bridging fibrosis}}",
    {1: V}, E_, "Fibrose em ponte", "28–29; Robbins p. 861", "central", NAO, EP_HBV, "Verde: alteração arquitetural das lâminas 28–29.",
    extra="- The more aggressive the immune response, the faster the fibrosis<br>" + F("tricromico")),
 sh(1791022172624, "verde", E_, "Cirrose: fibrose + nódulos regenerativos", 29, "Verde: desfecho da lâmina 29 (Correlação)."),
]

SEM_IMAGEM = "relação ou nome sem estrutura própria a reconhecer; as figuras que ensinam estão nos cards de achado e nos Extras"
SLIDE_SEM_ALT = "figura da própria lâmina da aula, sem equivalente no AnKing; é o achado ou o esquema que a aula ensina"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "pt61-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {
 "b-sintese": "- The virus hijacks the ribosomes for its own proteins",
 "b-sincicio": "- Fusion spreads the virus cell to cell without exposure to antibodies",
 "c-resposta": "- Innate defenses act in hours to days; adaptive responses need about a week",
 "c-estado-antiviral": "- Interferon-induced enzymes (PKR, OAS–RNase L) block viral translation",
 "ak-nk-perforina": "- Perforin opens pores; granzymes enter and activate caspases",
 "d-vidro-hbsag": "- Immunostaining for HBsAg confirms the cytoplasmic accumulation",
 "d-ihc": "- HBcAg in nuclei reflects active viral replication",
 "e-portal": "- Portal tracts are where blood-borne virus and leukocytes first meet the hepatocytes",
 "ak-necrose-ponte": "- Confluent necrosis links portal tracts and central veins",
 "e-linfocito-b": "- B cells and plasma cells in aggregates produce antiviral antibodies",
 "e-imunopatologia": "- HBV itself is poorly cytopathic; clearing infected hepatocytes causes the hepatitis",
 "ak-proteina-f": "- Measles and RSV use F proteins; HIV uses gp41",
 "ak-ifn-mhc": "- More MHC I lets CD8+ T cells see infected cells",
 "ak-ifn-nk": "- NK cells are the early cellular defense before T cells expand",
 "ak-nk-mhc": "- MHC I engages NK inhibitory receptors; when it is lost, activating signals win and the NK cell kills<br>- Many viruses reduce MHC I to escape CD8+ T cells, which exposes them to NK cells<br>" + F("nk"),
 "ak-hbv-rt": "- HBV is a DNA virus that replicates through an RNA intermediate",
 "ak-balonizacao": "- Swollen, pale hepatocytes in acute viral hepatitis",
}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

BOLD = {
 "a-dano-duplo": ["Viral disease"], "b-apoptose": ["Some viruses"], "b-cpe": ["Structural changes"], "b-inclusao": ["viral proteins or particles"],
 "b-sarampo": ["Measles virus"], "b-sincicio": ["Multinucleated cells"], "b-sincicio-granuloma": ["viral syncytial giant cell"], "b-hpv16": ["Koilocytes"],
 "c-cinetica": ["acute viral infection"], "c-estado-antiviral": ["Type I interferon"], "c-nk-receptores": ["NK cell killing"], "d-cccdna": ["hepatocyte nucleus"],
 "d-ihc": ["HBV immunohistochemistry"], "e-portal": ["chronic viral hepatitis"], "e-councilman": ["Apoptotic hepatocytes"], "e-interface": ["Inflammation spilling"],
 "e-linfocito-b": ["chronic viral hepatitis"], "e-imunopatologia": ["Hepatocyte injury"], "e-fibrose": ["Repeated immune-mediated injury"],
}
for c in CARDS:
    for ph in BOLD.get(c["key"], []):
        if c["kind"] == "autoral" and f"<b>{ph}</b>" not in c["text"] and ph in c["text"]:
            c["text"] = c["text"].replace(ph, f"<b>{ph}</b>", 1)

IMAGENS_VISTAS = {
 "pt61-negri.jpeg": "Lâmina 5: neurônio com inclusão citoplasmática eosinofílica (seta); legível.",
 "pt61-sarampo.jpeg": "Lâmina 6: células com inclusão intranuclear eosinofílica e halo; sem legenda.",
 "pt61-sincicio.jpeg": "Lâmina 7: células multinucleadas em cultura; sem legenda.",
 "pt61-coilocito.jpeg": "Lâmina 8: coilócitos com halo perinuclear em esfregaço.",
 "pt61-cinetica.png": "Lâmina 10: curvas de vírus, IFN-I, NK, linfócitos T e anticorpos por dia; rótulos visíveis, só no Extra.",
 "pt61-interferon.jpeg": "Lâmina 11: esquema do IFN da célula infectada para as vizinhas (rótulos em português); Extra.",
 "pt61-estado-antiviral.jpeg": "Lâmina 12: IFN, aumento de MHC-I, ativação de NK/Tc e estado antiviral; Extra.",
 "pt61-nk.jpeg": "Lâmina 13: receptores ativador e inibidor da NK, MHC-I, perforina; Extra.",
 "pt61-ciclo-hbv.jpeg": "Lâmina 15: ciclo do HBV com cccDNA; mostra a resposta, só no Extra.",
 "pt61-vidro-fosco.jpeg": "Lâmina 16: hepatócitos em vidro despolido (seta).",
 "pt61-ihc-hbsag.jpeg": "Lâmina 17: IHC HBsAg citoplasmático marrom.",
 "pt61-ihc-hbcag.jpeg": "Lâmina 18: IHC HBcAg nuclear marrom.",
 "pt61-portal.jpeg": "Lâmina 19: trato portal expandido por agregado linfoide.",
 "pt61-necrose.jpeg": "Lâmina 23: necrose extensa com infiltrado e colapso.",
 "pt61-apoptose.jpeg": "Lâmina 24: corpúsculo apoptótico eosinofílico denso entre hepatócitos.",
 "pt61-interface.jpeg": "Lâmina 25: infiltrado avançando do trato portal sobre hepatócitos periportais.",
 "pt61-linfocito-b.jpeg": "Lâmina 26: IHC de linfócitos B em agregados portais.",
 "pt61-cd8.jpeg": "Lâmina 27: IHC de CD8 no infiltrado portal/periportal.",
 "pt61-tricromico.jpeg": "Lâmina 29: tricrômico com septos fibrosos azuis e nódulos.",
}

REVISAO = {}

ESCOPO = {
 "objetivo": "Explicar como os vírus lesam tecidos (efeito citopático direto e resposta imune), reconhecer os efeitos citopáticos da aula e aplicar tudo à hepatite B: estrutura, efeito citopático, resposta e lesão imunomediada até a fibrose.",
 "centrais": [
   ("duas vias de lesão", "a-dano-duplo"),
   ("efeitos sobre a célula e efeito citopático", "b-efeitos", "b-apoptose", "b-sintese", "b-cpe", "b-inclusao", "ak-negri", "b-sarampo", "b-sincicio", "ak-proteina-f", "b-sincicio-granuloma", "ak-coilocito", "b-hpv16"),
   ("resposta do hospedeiro", "c-resposta", "c-cinetica", "ak-ifn", "c-estado-antiviral", "ak-ifn-mhc", "ak-ifn-nk", "ak-nk-mhc", "ak-nk-perforina"),
   ("HBV: vírus e efeito citopático", "d-hbv-estrutura", "d-cccdna", "ak-hbv-rt", "ak-vidro", "d-vidro-hbsag", "d-ihc"),
   ("hepatite: lesão e reparo", "e-portal", "ak-balonizacao", "ak-necrose-ponte", "e-councilman", "e-interface", "e-linfocito-b", "e-imunopatologia", "e-fibrose"),
 ],
 "exemplos": ["raiva", "sarampo", "HPV", "hepatite B (exemplo integrador)"],
 "outras_aulas": [("tropismo e patogênese", "59 Patogênese da infecção viral"), ("transformação viral", "P4 Agentes carcinogênicos biológicos"),
                  ("inflamação crônica", "62 Inflamação crônica"), ("IHC e colorações", "03 Diagnóstico patológico"), ("subtipos de linfócitos", "45 Ativação de linfócitos T")],
}

import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
