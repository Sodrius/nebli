# Especificação curada — Lesão celular, necrose e apoptose (UC03 P1, Patologia; Prof. Luiz F. Ferraz da Silva; 47 lâminas Ia).
# Pipeline AnKing-primeiro (F-20261015-CLAUDE-06/07), piloto de calibração. Ordem = lâminas. Autoral só para lacuna provada em
# busca/cobertura.tsv (três caminhos, todos os acervos). Adaptação = aula 11; granuloma = 47; CD8/Fas = 45; infarto em detalhe = aula própria.
# Aula antiga (P1): entra suspensa. Sem Tab (Codex depois).
import json as _json, pathlib as _pl, re as _re

PIPELINE = "anking-primeiro"
RUN_ID = "uc03-pt09-20261015b"
SHORT = "pt09"
LESSON = "2026-uc03-patologia-09-lesao-celular"
DECK = "NEBLI::UC03::P1::Patologia::Lesão celular, necrose e apoptose"
CRITERIOS = "MEMORY.md §5 (AnKing-primeiro, gates duros) + ANTI-EXEMPLARES-CARDS + PLANO-ANKING-PRIMEIRO, 15/10/2026"
MEDIA = {f"pt09-{n}": f"img/pt09-{n}" for n in ("resposta.png", "sequencia.png", "tubulo.jpeg", "coagulativa.jpeg", "liquefativa.png", "gordurosa.png")}
IMG = lambda n, w=440: f'<img src="pt09-{n}" width="{w}">'
V, Z, R = 3, 4, 5
BUSCA = ("Três caminhos (15/10): seções inteiras de B&B Cell Injury/Free Radicals/Apoptosis/Necrosis, FirstAid Cellular Injury, Pathoma "
         "Cellular Injury/Cell Death/Free Radical, Bootcamp Cellular Injury/Necrosis/Apoptotic Pathways, OME Necrosis/Apoptosis (busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos (busca/semantica.jsonl). ")
EXCLUIDOS = [
 (1487469783753, "forma preservada: mesma ideia de ak-coag-arquitetura, que pede o núcleo e os contornos"),
 (1481771836484, "AVC isquêmico → liquefativa: repete ak-liq-cerebro-abscesso"),
 (1487469880635, "neutrófilos no infarto cerebral: repete ak-neutrofilos (abscesso), que é o caso da lâmina"),
 (1487469886411, "pâncreas liquefativo: a lâmina põe o pâncreas como gordurosa; evitar confusão (caso de fronteira)"),
 (1471899221722, "necrose em banda de contração: aula de infarto"),
 (1471899328126, "linha do tempo do infarto (4–24 h): aula de infarto"),
 (1487470222716, "DNA em escada: técnica de laboratório não ensinada"),
 (1496162483849, "BCL-2/BCL-xL estabilizam a membrana: repete ak-bcl2-citc"),
 (1487117300306, "Fas-L/Fas com liberação de TNF: formulação confusa; a via entra pelo compartilhado da aula 45"),
 (1487470217383, "ALPS: clínica estreita (Davi: clínica só ampla e HY)"),
 (1496162849677, "linfoma folicular: aula de neoplasias; cloze em hipermutação somática"),
 (1486952724628, "seleção negativa: aula de Imunologia (tolerância)"),
 (1478834050609, "ferritina e Fenton: fora das lâminas"),
 (1487470260293, "proteínas carreadoras de metal: fora das lâminas"),
 (1520708594283, "contratilidade some em 60 s: detalhe de fisiologia cardíaca"),
 (1525458045044, "edema citotóxico neuronal: neurologia; ak-edema cobre o edema celular"),
]
FORA_DO_RECORTE = [
 "Adaptação celular (hipertrofia, hiperplasia, atrofia, metaplasia; lâminas 3–4 e apostila caps. 2–3): aula 11 Acúmulos e adaptação.",
 "Alteração gordurosa/esteatose (lâmina 7): aula 11.",
 "Granuloma caseoso em detalhe (lâmina 31): aula 47.",
 "Infarto do miocárdio em detalhe (linha do tempo, bandas de contração, infarto vermelho): aula de infarto (69).",
 "Linfoma folicular/BCL-2 como oncogene: aulas de neoplasia.",
]

_CL = {}  # clozes de cada nota de acervo, lidos do Anki: todos os irmãos entram (Davi suspende)


def _clozes(nid):
    if not _CL:
        import urllib.request
        def call(a, **p):
            return _json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", _json.dumps({"action": a, "version": 6, "params": p}).encode())))["result"]
        ids = [c["src"] for c in CARDS if c["kind"] == "text"]
        for n in call("notesInfo", notes=ids):
            _CL[n["noteId"]] = sorted({int(x) for x in _re.findall(r"\{\{c(\d+)::", n["fields"]["Text"]["value"])})
    return _CL[nid]


def ak(key, src, cor, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
G = lambda *k: {i: V for i in k}
EP_CONJ = [1487470255062, 1487469931164, 1487470105872]   # conjunto nomeado em uma nota AnKing
EP_FATO = [1487463871778, 1487469733350, 1487463914329]   # fato pontual de lesão celular
A_, B_, C_, D_, E_ = "A-resposta-e-causas", "B-reversivel-irreversivel", "C-mecanismos", "D-necrose", "E-apoptose"

CARDS = [
 # ---------- A. Resposta à agressão e causas (Ia 2–6) ----------
 ak("ak-dois-mecanismos", 1487469763555, V, A_, "Necrose e apoptose: os dois tipos de morte celular", 2, "Verde: HY 2; esquema da lâmina 2, base de toda a aula."),
 ak("ak-fim-irreversivel", 1487467497291, V, A_, "Lesão irreversível termina em morte celular", 2, "Verde: lâmina 2 (seta irreversível → morte)."),
 au("au-reversivel-irreversivel", "Whether an <b>injured cell</b> recovers or dies depends mainly on the {{c1::intensity}} and {{c1::duration}} of the injurious stimulus",
    G(1), A_, "Intensidade e duração decidem reversível × irreversível", "2; cruzadas 24", "central", "", EP_FATO,
    "Verde: princípio da lâmina 2 (leve e transitório → reversível; intenso e progressivo → irreversível); palavras-cruzadas.",
    extra="- Mild and transient → reversible injury; severe and progressive → irreversible injury<br>" + IMG("resposta.png", 420)),
 ak("ak-angina", 1471880379381, V, A_, "Angina = lesão reversível", 3, "Verde: HY 2; exemplo de lesão reversível da lâmina 3.",
    extra_add="- Blood flow returns before the myocytes pass the point of no return"),
 ak("ak-iam", 1471898845279, V, A_, "Infarto = lesão irreversível", 3, "Verde: HY 1; exemplo de lesão irreversível da lâmina 3."),
 ak("ak-hepatite-viral", 1521424037362, Z, A_, "Hepatite viral aguda: necrose/apoptose do hepatócito", 3, "Azul: HY 2; exemplo da lâmina 3 (hepatite aguda) e provas 2018/2016 (AST/ALT).", clinica_lateral="hepatite viral tem aula própria; aqui é só exemplo de lesão irreversível"),
 au("au-causas", ORG("<b>Main causes of cell injury</b>:<br>1. {{c1::Oxygen deprivation}}<br>2. {{c1::Physical}} agents<br>3. {{c1::Chemicals}} and drugs<br>"
                     "4. {{c2::Infections}}<br>5. {{c2::Immune}} reactions<br>6. {{c2::Genetic}} defects<br>7. {{c2::Nutritional}} imbalances"),
    {1: Z, 2: Z}, A_, "As sete causas de lesão celular", "5", "central", "", EP_CONJ, "Azul: lista da lâmina 5, monitoria P1 e apostila guia Aula 2.",
    extra="- Oxygen deprivation is the most common, usually through ischemia"),
 ak("ak-hipoxia", 1473466841624, V, A_, "Hipóxia = menor entrega de O2", 5, "Verde: primeira causa da lâmina 5."),
 ak("ak-isquemia", 1473466862672, V, A_, "Isquemia = perda de fluxo", 5, "Verde: causa mais comum (cruzadas 15; prova 2019).",
    extra_add="- Ischemia injures faster than hypoxia alone: flow also stops bringing glucose and removing wastes"),
 ak("ak-co", 1473466860013, R, A_, "CO reduz o conteúdo de O2", 5, "Rosa: HY 2; apostila guia (hipóxia sem isquemia: pneumonia, anemia, CO).", clinica_lateral="intoxicação por CO é exemplo da apostila, não alvo da lâmina"),
 au("au-sequencia", ORG("After <b>cell injury</b> begins, changes become detectable in this order:<br>1. {{c1::Biochemical}} alterations (loss of function)<br>2. {{c1::Ultrastructural}} changes<br>"
                        "3. {{c2::Light microscopic}} changes<br>4. {{c2::Gross}} morphologic changes"),
    {1: V, 2: V}, A_, "Ordem em que as alterações aparecem", "6; cruzadas 8 e 26", "central", "", EP_CONJ,
    "Verde: gráfico da lâmina 6; palavras-cruzadas (ultraestruturais precoces; coração sem alteração macroscópica após 1 h).",
    extra="- An infarcted heart still looks normal to the naked eye after 1 hour<br>- Sensitive cells such as neurons cross into irreversibility sooner<br>" + IMG("sequencia.png", 420)),
 ak("ak-30min", 1520709378524, V, A_, "Isquemia miocárdica total > 30 min = irreversível", 6, "Verde (HY do recorte): HY 2; ponto sem retorno do gráfico da lâmina 6 no exemplo do coração."),

 # ---------- B. Reversível × irreversível (Ia 7–11) ----------
 ak("ak-edema", 1487463887140, V, B_, "Marco da lesão reversível: edema celular", 7, "Verde: HY 1; lâmina 7 e cruzadas 9."),
 ak("ak-bolhas", 1487463894466, V, B_, "Bolhas e perda de microvilosidades", 7, "Verde: HY 1; lâmina 7."),
 ak("ak-ribossomos", 1487463900987, V, B_, "Desligamento de ribossomos/polissomos", 7, "Verde: HY 1; lâmina 7 e cruzadas 22."),
 ak("ak-cromatina", 1521136890400, V, B_, "Condensação da cromatina", 7, "Verde: HY 1; lâminas 7 e 10.",
    extra_add="- Low pH from lactic acid clumps the chromatin"),
 ak("ak-marco-irreversivel", 1487463907439, V, B_, "Marco da irreversível: dano de membrana", 8, "Verde: HY 1; critério da lâmina 8."),
 au("au-criterios", ORG("<b>Irreversible cell injury</b> is defined by two criteria:<br>1. loss of plasma {{c1::membrane}} permeability<br>2. excessive destruction of {{c1::DNA}} and proteins"),
    G(1), B_, "Os dois critérios de irreversibilidade", "8; prova 2024 P1 2.8; cruzadas 7", "prova", "", EP_CONJ, "Verde: lâmina 8; provas 2024 e 2015.",
    extra="- In hypoxia, membrane damage usually comes first; in severe genetic damage, DNA destruction does",
    duplicacao_ok="ganho: o par de critérios da lâmina 8; ak-marco-irreversivel pede só o marco de membrana"),
 ak("ak-perda-nucleo", 1487469733350, V, B_, "Perda do núcleo = morte celular", 9, "Verde: HY 1; túbulos da lâmina 9.",
    extra_add="- A normal tubule, B reversible injury (swollen, nuclei kept), C irreversible injury (nuclei lost)<br>" + IMG("tubulo.jpeg", 500)),
 ak("ak-enzimas-soro", 1487463914329, V, B_, "Enzima intracelular no sangue = lesão irreversível", 11, "Verde: HY 2; lâmina 11; provas 2017, 2015, 2018 (AST/ALT); cruzadas 13.",
    extra_add="- Enzymes leave the cell only through a damaged membrane: troponin and CK-MB (heart), AST and ALT (liver), lipase and amylase (pancreas)"),
 ak("ak-troponina", 1471899071838, V, B_, "Troponina I", 11, "Verde (HY do recorte): HY 1; gráfico da lâmina 11 (mioglobina, CK-MB, troponina); prova 2017. Clínica ampla."),
 ak("ak-amilase-lipase", 1482971327560, V, B_, "Amilase/lipase na pancreatite", 11, "Verde (HY do recorte): HY 2; exemplo da transcrição e provas 2023/2016. Clínica ampla."),

 # ---------- C. Mecanismos (Ia 12–20) ----------
 au("au-mecanismos", ORG("<b>Cell injury</b> results from damage to four main targets:<br>1. {{c1::Mitochondria}} (↓ ATP, ↑ free radicals)<br>2. {{c1::Calcium}} homeostasis (Ca²⁺ influx)<br>"
                         "3. Cell {{c1::membranes}}<br>4. {{c1::DNA}} and protein folding"),
    G(1), C_, "Os quatro alvos/mecanismos da lesão", "12; 18", "central", "", EP_CONJ, "Verde: esquema das lâminas 12 e 18; monitoria P1 e apostila guia cap. 5.",
    extra="- They feed each other: low ATP lets Ca²⁺ in, Ca²⁺ and free radicals damage mitochondria and membranes"),
 ak("ak-atp", 1487463871778, V, C_, "Falta de ATP", 13, "Verde: HY 1; lâmina 13."),
 ak("ak-bombas", 1487463879752, V, C_, "Bombas Na⁺/K⁺ e Ca²⁺ param", 13, "Verde: HY 1; lâmina 13; prova 2015 P1 3.1; cruzadas 31."),
 au("au-lactato", "In <b>hypoxic cells</b>, anaerobic glycolysis consumes glycogen and builds up {{c1::lactic acid}}, lowering intracellular pH",
    G(1), C_, "Glicólise anaeróbia → ácido lático → ↓pH", "13; prova 2015 P1 3.1; cruzadas 3", "prova", "", EP_FATO, "Verde: lâmina 13; prova 2015; palavras-cruzadas.",
    extra="- The acid pH is what clumps the nuclear chromatin"),
 ak("ak-superoxido", 1487470227188, Z, C_, "1 elétron: superóxido", 14, "Azul: redução incompleta do O2 (lâmina 14; cruzadas 28)."),
 ak("ak-peroxido", 1487470229408, Z, C_, "2 elétrons: peróxido de hidrogênio", 14, "Azul: lâmina 14 (SOD → H2O2)."),
 ak("ak-hidroxila", 1487470231445, Z, C_, "3 elétrons: hidroxila", 14, "Azul: lâmina 14 (Fenton → •OH)."),
 ak("ak-hidroxila-pior", 1487470236560, Z, C_, "Hidroxila é o radical mais lesivo", 14, "Azul: lâmina 14."),
 ak("ak-fenton", 1487470238614, R, C_, "Reação de Fenton (metais)", 14, "Rosa: reação mostrada na lâmina 14 e citada na transcrição."),
 ak("ak-radiacao", 1487470234455, R, C_, "Radiação ionizante gera •OH", 14, "Rosa: fonte de radicais na lâmina 14 (radiação)."),
 ak("ak-efeitos-radicais", 1487470244885, V, C_, "Peroxidação lipídica; oxidação de proteínas e DNA", 14, "Verde: lâmina 14; provas 2018/2019; cruzadas 14."),
 ak("ak-sod", 1487470252945, V, C_, "SOD", 14, "Verde: antioxidante da lâmina 14."),
 ak("ak-catalase-gpx", 1487470255062, V, C_, "Catalase e glutationa peroxidase", 14, "Verde: HY 1; lâmina 14; cruzadas 23."),
 ak("ak-antioxidantes", 1487470250734, V, C_, "Antioxidantes (glutationa, vitaminas)", 14, "Verde (HY do recorte): lâmina 14 e transcrição (quelantes de radicais)."),
 ak("ak-reperfusao-trombolise", 1487470274721, V, C_, "Lesão de reperfusão após trombólise", 15, "Verde: HY 1; lâmina 15; prova 2015 P1 3.4."),
 ak("ak-reperfusao-radicais", 1471899234512, V, C_, "Reperfusão gera radicais livres", 15, "Verde: HY 1; mecanismo da lâmina 15; cruzadas 17.",
    extra_add="- Same reason a transplanted kidney loses function right after its vessels are reconnected"),
 ak("ak-citc-iniciadoras", 1496161956265, V, C_, "Citocromo c ativa caspases iniciadoras", 16, "Verde: HY 1; lâmina 16 (mitocôndria → apoptose); cruzadas 35.",
    extra_add="- If the mitochondrion instead loses its membrane potential (permeability transition), ATP production stops and the cell dies by necrosis"),
 ak("ak-calcio-entrada", 1487463918664, V, C_, "Entrada de Ca²⁺", 17, "Verde: HY 1; lâmina 17."),
 au("au-calcio-enzimas", ORG("High cytosolic <b>Ca²⁺</b> in injured cells activates:<br>- {{c1::phospholipases}} → membrane damage<br>- {{c1::proteases}} → cytoskeleton and membrane damage<br>"
                             "- {{c1::endonucleases}} → DNA damage<br>- {{c1::ATPases}} → faster ATP loss"),
    G(1), C_, "Enzimas ativadas pelo cálcio", "17; prova 2024 P1 2.8; cruzadas 25", "prova", "", EP_CONJ, "Verde: lâmina 17; prova 2024; palavras-cruzadas.",
    extra="- Ca²⁺ comes from outside the cell and from mitochondrial and ER stores, all kept by ATP-dependent pumps"),
 ak("ak-lisossomo", 1487463924702, V, C_, "Membrana lisossômica: hidrolases no citosol", 19, "Verde (HY do recorte): HY 2; dano de membrana (lâminas 19 e 25)."),
 au("au-mal-dobradas", "<b>Misfolded proteins</b> that {{c1::chaperones}} cannot refold accumulate and push the cell into apoptosis",
    {1: Z}, C_, "Proteínas mal dobradas e chaperonas", "20; cruzadas 30", "central", "", EP_FATO, "Azul: lâmina 20; palavras-cruzadas.",
    extra="- Example: prion diseases such as Creutzfeldt-Jakob"),

 # ---------- D. Necrose (Ia 22–35) ----------
 ak("ak-necrose-patologica", 1487469766823, V, D_, "Necrose nunca é fisiológica", 23, "Verde: definição da lâmina 23; tabela da 43."),
 ak("ak-necrose-inflamatoria", 1487469774152, V, D_, "Necrose é inflamatória", 23, "Verde: lâminas 23 e 25."),
 ak("ak-necrose-grupos", 1487469778711, V, D_, "Necrose: grupos de células", 23, "Verde (HY do recorte): HY 2; contraste com a apoptose."),
 ak("ak-apoptose-programada", 1487470119549, V, D_, "Apoptose: morte programada dependente de ATP", 23, "Verde: definição da lâmina 23."),
 ak("ak-apoptose-sem-inflamacao", 1487470122628, V, D_, "Apoptose sem inflamação", 23, "Verde: lâmina 23; cruzadas 4.",
    extra_add="- The membrane stays intact, so nothing leaks and apoptotic bodies are quietly phagocytosed"),
 ak("ak-apoptose-isoladas", 1487470125519, V, D_, "Apoptose: células isoladas", 23, "Verde (HY do recorte): HY 2; contraste com a necrose."),
 ak("ak-mielina", 1582762485024, V, D_, "Figuras de mielina (reversível)", 26, "Verde (HY do recorte): HY 2; rótulo do esquema da lâmina 26."),
 ak("ak-vacuolizacao", 1487463922315, V, D_, "Vacuolização mitocondrial (irreversível)", 26, "Verde (HY do recorte): HY 1; densidades mitocondriais do esquema da lâmina 26."),
 ak("ak-eosina", 1520442532258, V, D_, "Eosinofilia da necrose", 27, "Verde: lâmina 27; cruzadas 6.",
    extra_add="- Denatured proteins bind eosin and the basophilic RNA is lost"),
 ak("ak-picnose", 1487469750801, V, D_, "Picnose", 27, "Verde: lâmina 27; prova 2015 P1sub; cruzadas 19."),
 ak("ak-cariorrexe", 1487469755479, V, D_, "Cariorrexe", 27, "Verde: lâmina 27."),
 ak("ak-cariolise", 1487469759701, V, D_, "Cariólise", 27, "Verde (HY do recorte): HY 2; completa a sequência nuclear da lâmina 27."),
 au("au-tipos-necrose", ORG("<b>Morphologic patterns of necrosis</b>:<br>1. {{c1::Coagulative}}<br>2. {{c1::Liquefactive}}<br>3. {{c1::Caseous}}<br>4. {{c2::Fat}}<br>5. {{c2::Fibrinoid}}<br>6. {{c2::Gangrenous}}"),
    {1: V, 2: V}, D_, "Os seis padrões de necrose", "28–35", "central", "", EP_CONJ, "Verde: as lâminas 28–35 apresentam os seis tipos; apostila guia cap. 4; monitoria P1.",
    extra="- Coagulative and liquefactive are the two basic patterns; the others are special settings"),
 ak("ak-coag-arquitetura", 1487469807276, V, D_, "Coagulativa: arquitetura preservada, núcleo some", 28, "Verde: HY 1; lâmina 28 (fantasmas); cruzadas 21.",
    extra_add=IMG("coagulativa.jpeg", 420)),
 ak("ak-coag-enzimas", 1487469825199, V, D_, "Coagulativa: enzimas proteolíticas desnaturadas", 28, "Verde: o porquê da arquitetura mantida (lâmina 28)."),
 ak("ak-coag-infarto", 1487469816961, V, D_, "Coagulativa: infarto de qualquer órgão menos o cérebro", 28, "Verde: HY 1; lâmina 28."),
 ak("ak-infarto-palido", 1487469835042, V, D_, "Circulação terminal: infarto pálido", 28, "Verde (HY do recorte): HY 2; tecidos de circulação terminal da lâmina 28 (coração, baço)."),
 ak("ak-liq-lise", 1487469864434, V, D_, "Liquefativa: lise enzimática", 29, "Verde: lâmina 29."),
 ak("ak-liq-cerebro-abscesso", 1487469877849, V, D_, "Liquefativa: cérebro e abscessos", 29, "Verde: HY 1; lâmina 29; provas 2019, 2018, 2016; cruzadas 36.",
    extra_add="- The brain has almost no collagen framework: its scaffold is the neurons' and glial cells' own processes, which die too<br>" + IMG("liquefativa.png", 460)),
 ak("ak-neutrofilos", 1487469883647, V, D_, "Neutrófilos digerem o abscesso", 29, "Verde (HY do recorte): HY 2; transcrição (colagenases, elastases de neutrófilos)."),
 ak("ak-cavitacao", 1487469868022, V, D_, "Cavitação tardia no cérebro", 29, "Verde (HY do recorte): HY 1; o “buraco” no cérebro da lâmina 29."),
 ak("ak-klebsiella", 1525611579376, V, D_, "Abscesso pulmonar (Klebsiella) é liquefativo", 29, "Verde (HY do recorte): HY 1; prova 2017 P1 3.5."),
 ak("ak-caseosa-tb", 1487469962274, V, D_, "Caseosa: tuberculose e fungos", 30, "Verde: lâmina 30; cruzadas 29."),
 sh(1791716427402, "verde", D_, "Caseosa: aspecto de queijo", 30, "Verde: o nome “caseosa” (queijo) da lâmina 30; nota viva do GR3."),
 ak("ak-caseosa-debris", 1487469968141, V, D_, "Caseosa: debris com halo de linfócitos e macrófagos", 30, "Verde (HY do recorte): descrição literal da lâmina 30."),
 ak("ak-gordurosa-causas", 1487469975903, V, D_, "Gordurosa: pancreatite aguda ou trauma", 32, "Verde: lâmina 32.",
    extra_add=IMG("gordurosa.png", 420)),
 ak("ak-gordurosa-peripancreatica", 1482971299269, V, D_, "Gordura peripancreática", 32, "Verde: HY 1; provas 2023/2016."),
 ak("ak-saponificacao", 1487469981667, V, D_, "Saponificação", 32, "Verde: prova 2016 P1 2.8 e transcrição.",
    extra_add="- Leaked lipase splits fat into fatty acids, which bind Ca²⁺ and turn chalky"),
 ak("ak-gordurosa-calcario", 1487469971218, V, D_, "Aspecto branco-calcário", 32, "Verde (HY do recorte): HY 1; macroscopia da lâmina 32 (“pingos de vela”)."),
 ak("ak-saponificacao-he", 1487469993914, R, D_, "Saponificação azul-escura no HE", 33, "Rosa: microscopia da lâmina 33."),
 ak("ak-fibrinoide-vasos", 1487470100826, V, D_, "Fibrinoide: parede de vasos", 34, "Verde: lâmina 34."),
 ak("ak-fibrinoide-has", 1487470105872, V, D_, "Fibrinoide: HAS maligna e vasculite", 34, "Verde (HY do recorte): HY 1; vasculites da lâmina 34. Clínica ampla."),
 ak("ak-fibrinoide-rosa", 1487470115450, V, D_, "Fibrinoide: rosa brilhante", 34, "Verde (HY do recorte): HY 1; imagem da lâmina 34."),
 ak("ak-gangrena-local", 1487469931164, V, D_, "Gangrena: isquemia crônica de extremidades e TGI", 35, "Verde: lâmina 35; prova 2024 P1 2.1.",
    extra_add="- Gangrene is necrosis of several tissue layers at once (skin, subcutis, muscle)"),
 ak("ak-gangrena-seca", 1487469894582, Z, D_, "Gangrena seca (mumificada)", 35, "Azul: tipo da lâmina 35."),
 ak("ak-gangrena-umida", 1487469938790, Z, D_, "Gangrena úmida (superinfecção)", 35, "Azul: transcrição (risco de infecção do tecido morto)."),
 ak("ak-gangrena-imagem", 1545331820247, Z, D_, "Reconhecer gangrena", 35, "Azul: foto como a da lâmina 35 e da prova 2024."),

 # ---------- E. Apoptose (Ia 36–45) ----------
 au("au-apoptose-causas", ORG("<b>Physiologic</b> apoptosis:<br>- {{c1::embryogenesis}}<br>- hormonal {{c1::involution}}<br>- immune tolerance<br>- inflammatory cell turnover<br>"
                              "<b>Pathologic</b> apoptosis:<br>- {{c2::DNA damage}}<br>- {{c2::misfolded proteins}}<br>- viral infection<br>- atrophy"),
    {1: Z, 2: Z}, E_, "Causas fisiológicas × patológicas de apoptose", "36; cruzadas 20", "central", "", EP_CONJ, "Azul: lista da lâmina 36; monitoria P1; palavras-cruzadas.",
    extra="- Example of involution: mammary epithelium after weaning"),
 ak("ak-atrofia", 1487461041752, V, E_, "Atrofia por apoptose", 36, "Verde: HY 1; lâmina 36; provas 2017 e 2018."),
 sh(1791625429957, "azul", E_, "CD8 mata célula infectada por apoptose", 36, "Azul: lâminas 36 e 44; prova 2016 P2; cruzadas 16; nota viva da aula 45."),
 ak("ak-caspases", 1487470148526, V, E_, "Apoptose mediada por caspases", 37, "Verde: HY 1; execução (lâmina 37); cruzadas 32."),
 ak("ak-endonucleases", 1487470154743, V, E_, "Endonucleases quebram o DNA", 38, "Verde: HY 1; lâmina 38."),
 ak("ak-proteases", 1487470156809, V, E_, "Proteases quebram o citoesqueleto", 38, "Verde: HY 1; lâmina 38."),
 ak("ak-bcl2-inativacao", 1487470158626, V, E_, "Via intrínseca: inativação do BCL-2", 38, "Verde: HY 1; lâmina 38; prova 2016 P1 3.7.",
    extra_add="- Sensors of the BH3-only family (activated by DNA damage, radiation or loss of growth factors) neutralize BCL-2"),
 ak("ak-bcl2-citc", 1487470164855, V, E_, "BCL-2 segura o citocromo c", 38, "Verde: HY 1; lâmina 38."),
 au("au-caspases", ORG("<b>Caspases</b> of apoptosis:<br>- initiator, intrinsic pathway: caspase-{{c1::9}}<br>- initiator, extrinsic pathway: caspase-{{c1::8}}<br>- executioner: caspase-{{c2::3}}"),
    {1: V, 2: Z}, E_, "Caspases iniciadoras 9 e 8; executora 3", "38; cruzadas 1", "central", "", EP_CONJ, "Verde (iniciadoras): lâmina 38, apostila guia cap. 6; azul (executora).",
    extra="- Both pathways converge on the executioner caspases, which cut the cell's proteins and DNA"),
 sh(1791625429657, "verde", E_, "Via extrínseca: Fas-L/CD95 ou TNF", 38, "Verde: lâmina 38; cruzadas 27; nota viva da aula 45."),
 ak("ak-cd8", 1487470208377, V, E_, "Via extrínseca pelo CD8", 38, "Verde (HY do recorte): HY 1; lâminas 38 e 44."),
 ak("ak-apoptose-morfologia", 1487470128060, V, E_, "Morfologia: retração, condensação, bolhas", 39, "Verde: HY 1; lâminas 39–40."),
 ak("ak-corpos-apoptoticos", 1487470141075, V, E_, "Corpos apoptóticos fagocitados", 40, "Verde: lâmina 40; cruzadas 11 e 33.",
    extra_add="- Apoptotic cells expose “eat-me” signals on their surface, so phagocytes remove them before anything leaks"),
 ak("ak-apoptose-eosinofilica", 1487470130414, V, E_, "Citoplasma eosinofílico", 41, "Verde (HY do recorte): imagem da lâmina 41."),
 ak("ak-apoptose-basofilico", 1487470134272, V, E_, "Núcleo basofílico", 41, "Verde (HY do recorte): imagem da lâmina 41."),
 ak("ak-bax-pro", 1487470180854, V, E_, "BAX/BAK pró-apoptóticos", 42, "Verde: HY 1; tabela da lâmina 42."),
 ak("ak-bcl2-anti", 1487470187106, V, E_, "BCL-2/BCL-xL antiapoptóticos", 42, "Verde: HY 1; tabela da lâmina 42.",
    extra_add="- The table also lists IAPs (inhibit caspases) and FLIP (binds caspase-8 and blocks the extrinsic pathway)"),
 ak("ak-p53-bax", 1496161930377, V, E_, "p53 ativa BAX/BAK", 42, "Verde: HY 1; lâminas 42 e 44; prova 2016 P3."),
 au("au-tabela-necrose-apoptose", ORG("<table><tr><th></th><th><b>Necrosis</b></th><th><b>Apoptosis</b></th></tr>"
                                      "<tr><td>Cell size</td><td>{{c1::Swollen}}</td><td>{{c1::Shrunken}}</td></tr>"
                                      "<tr><td>Plasma membrane</td><td>{{c2::Disrupted}}</td><td>{{c2::Intact}}</td></tr>"
                                      "<tr><td>Contents</td><td>{{c3::Leak out}}</td><td>{{c3::Retained}}</td></tr>"
                                      "<tr><td>Inflammation</td><td>Yes</td><td>No</td></tr></table>"),
    G(1, 2, 3), E_, "Tabela necrose × apoptose", "43; prova 2015 P1sub", "prova", "", EP_CONJ, "Verde: tabela da lâmina 43; prova 2015.",
    extra="- Necrosis: a messy death of many cells after lethal damage; apoptosis: a tidy, programmed death of single cells",
    duplicacao_ok="ganho: tabela da lâmina 43 em quadro; os AnKing cobrem inflamação e papel, não tamanho, membrana e conteúdo"),
 ak("ak-p53-reparo", 1496161914384, V, E_, "p53: apoptose se o reparo falha", 44, "Verde: HY 1; lâmina 44; cruzadas 12."),
 au("au-apoptose-doencas", "Too little <b>apoptosis</b> favors {{c1::cancer}} and autoimmunity, whereas too much apoptosis underlies {{c2::neurodegenerative}} diseases",
    {1: Z, 2: Z}, E_, "Apoptose deficiente × excessiva", "44; cruzadas 18; provas 2017/2018", "prova", "", EP_FATO, "Azul: lâmina 44; provas 2017/2018 (Alzheimer).",
    extra="- Example of excess: loss of neurons and synapses in Alzheimer disease"),
 au("au-necroptose", "<b>Programmed necrosis</b>, started by TNF when caspase-8 cannot be activated, is called {{c1::necroptosis}}",
    {1: R}, E_, "Necroptose", "45", "lateral", "", EP_FATO, "Rosa: lâmina 45 (o professor mostrou sem detalhar).",
    extra="- RIP kinases switch the death signal to the mitochondria: ATP falls, free radicals rise and the cell dies like a necrosis"),
]

# todos os irmãos entram (F-20261015-CLAUDE-07): a cor vale para todos os clozes da nota
for c in CARDS:
    if c["kind"] == "text" and isinstance(c["flags"], int):
        c["flags"] = {n: c["flags"] for n in _clozes(c["src"])}

SEM_IMAGEM = "fato ou conjunto sem estrutura a reconhecer; as imagens que ensinam estão nos cards de túbulo, coagulativa, liquefativa, gordurosa, gangrena e nos organizadores"
SLIDE_SEM_ALT = "figura da própria lâmina da aula, sem equivalente no AnKing"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "pt09-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {
 "ak-fim-irreversivel": "- Past the point of no return the cell dies by necrosis or apoptosis",
 "ak-iam": "- Ischemia lasted long enough for membranes and DNA to be destroyed",
 "ak-hipoxia": "- Without O2, oxidative phosphorylation stops and ATP falls",
 "ak-30min": "- Up to ~30 min, restoring flow still rescues the myocytes",
 "ak-troponina": "- It is a contractile protein: it reaches the blood only when the myocyte membrane breaks",
 "ak-hidroxila-pior": "- It reacts instantly with lipids, proteins and DNA",
 "ak-radiacao": "- That is why radiation damages cells through free radicals",
 "ak-sod": "- H2O2 is then removed by catalase or glutathione peroxidase",
 "ak-antioxidantes": "- When radicals outpace these defenses, oxidative stress injures the cell",
 "ak-necrose-inflamatoria": "- Leaked cell contents recruit inflammatory cells",
 "ak-necrose-grupos": "- The same injury (e.g., ischemia) hits a whole territory of cells",
 "ak-apoptose-programada": "- The cell activates its own caspases: a death it carries out itself",
 "ak-apoptose-isoladas": "- Each cell is removed alone, without disturbing its neighbors",
 "ak-mielina": "- Whorls of damaged membrane lipids seen in swollen cells",
 "ak-coag-infarto": "- In the brain there is no collagen framework, so the dead tissue liquefies instead",
 "ak-neutrofilos": "- Their collagenases and elastases also destroy the framework, so the tissue liquefies",
 "ak-caseosa-debris": "- The granuloma's macrophages and lymphocytes surround the cheese-like center",
 "ak-saponificacao-he": "- Calcium soaps bind hematoxylin",
 "ak-fibrinoide-has": "- Both injure the vessel wall, where plasma proteins and immune complexes leak in",
 "ak-fibrinoide-rosa": "- Leaked fibrin and plasma proteins stain like fibrin",
 "ak-gangrena-seca": "- Coagulative necrosis of a limb that dries out without infection",
 "ak-gangrena-imagem": "- Necrosis of skin, subcutis and muscle together, from poor blood supply",
 "ak-caspases": "- They are proteases kept inactive until the death signal",
 "ak-endonucleases": "- DNA is cut between nucleosomes, fragmenting the nucleus",
 "ak-proteases": "- Without its cytoskeleton the cell shrinks and buds into apoptotic bodies",
 "ak-apoptose-morfologia": "- The cell shrinks instead of swelling, unlike necrosis",
 "ak-p53-reparo": "- This keeps mutated cells from dividing, protecting against cancer",
}
DUPLICACAO = {
 "au-mecanismos": "ganho: mapa dos quatro alvos (lâminas 12 e 18); os AnKing cobram cada mecanismo isolado",
 "au-calcio-enzimas": "ganho: conjunto das enzimas ativadas pelo Ca²⁺ (lâmina 17, prova 2024); os AnKing de caspase/protease são da apoptose",
 "au-tipos-necrose": "ganho: os seis padrões juntos; os AnKing cobram cada tipo",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
for c in CARDS:
    if c["key"] in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[c["key"]]
        else:
            c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
IMAGENS_VISTAS = {
 "pt09-resposta.png": "Lâmina Ia 2 (Robbins): esquema homeostase → adaptação / lesão → reversível ou irreversível → necrose/apoptose; no verso do card de intensidade e duração.",
 "pt09-sequencia.png": "Lâmina Ia 6 (Robbins): gráfico função × bioquímica × ultraestrutura × microscopia × macroscopia no tempo; no verso do organizador da sequência.",
 "pt09-tubulo.jpeg": "Lâmina Ia 9 (Robbins): túbulos normal (A), reversível com edema (B), irreversível sem núcleos (C); no verso.",
 "pt09-coagulativa.jpeg": "Lâmina Ia 28: miocárdio com necrose coagulativa (fibras eosinofílicas sem núcleo) e neutrófilos; no verso.",
 "pt09-liquefativa.png": "Lâmina Ia 29: pulmão com abscesso, cérebro com área amolecida/cavitada e histologia; texto da lâmina cortado; no verso.",
 "pt09-gordurosa.png": "Lâmina Ia 32: pâncreas com focos branco-calcários de necrose gordurosa; logotipo cortado; no verso.",
}
REVISAO = {
 "ak-bombas": "AnKing original com cloze em “decreased” (fraco); preservado e levado a Davi",
 "ak-hepatite-viral": "AnKing original com cloze em “viral”; azul como exemplo; levado a Davi",
 "au-tabela-necrose-apoptose": "tabela renderizada conferida: 3 linhas com cloze, inflamação visível",
 "ak-gangrena-imagem": "foto dos dedos na frente; nenhum rótulo entrega",
}
ESCOPO = {
 "objetivo": "Entender como uma agressão leva a lesão reversível ou irreversível (critérios e marcadores), pelos mecanismos (ATP, mitocôndria, cálcio, radicais livres, membrana, dobramento), e reconhecer as duas mortes celulares: necrose (padrões) e apoptose (causas, vias, morfologia, doenças).",
 "centrais": [
   ("desfechos da agressão", "ak-dois-mecanismos", "au-reversivel-irreversivel", "ak-angina", "ak-iam", "au-causas", "ak-hipoxia", "ak-isquemia", "au-sequencia"),
   ("reversível × irreversível", "ak-edema", "ak-bolhas", "ak-ribossomos", "ak-cromatina", "au-criterios", "ak-marco-irreversivel", "ak-perda-nucleo", "ak-enzimas-soro", "ak-troponina"),
   ("mecanismos de lesão", "au-mecanismos", "ak-atp", "ak-bombas", "au-lactato", "ak-superoxido", "ak-efeitos-radicais", "ak-sod", "ak-catalase-gpx", "ak-reperfusao-radicais", "ak-citc-iniciadoras", "au-calcio-enzimas", "au-mal-dobradas"),
   ("necrose", "ak-necrose-patologica", "ak-necrose-inflamatoria", "ak-eosina", "ak-picnose", "au-tipos-necrose", "ak-coag-arquitetura", "ak-coag-infarto", "ak-liq-cerebro-abscesso", "ak-caseosa-tb", "ak-gordurosa-peripancreatica", "ak-saponificacao", "ak-fibrinoide-vasos", "ak-gangrena-local"),
   ("apoptose", "ak-apoptose-programada", "ak-apoptose-sem-inflamacao", "au-apoptose-causas", "ak-atrofia", "ak-caspases", "ak-bcl2-inativacao", "ak-bcl2-citc", "au-caspases", "sh-1791625429657", "ak-apoptose-morfologia", "ak-corpos-apoptoticos", "ak-p53-bax", "au-tabela-necrose-apoptose", "au-apoptose-doencas"),
 ],
 "exemplos": ["hipertensão/Alzheimer (adaptação)", "queimadura solar", "tabagismo", "transplante renal (reperfusão)", "doença de Creutzfeldt-Jakob", "pancreatite (lipase)"],
 "outras_aulas": [("adaptação e esteatose", "11 Acúmulos e adaptação"), ("granuloma caseoso", "47 Inflamação granulomatosa"), ("CD8, Fas, perforinas", "45 Ativação de linfócitos T"), ("infarto", "69 Hemostasia, trombose, embolia e infarto")],
}
# busca que não achou card, por autoral (de busca/cobertura.tsv, gate duro)
_COB = {l.split("\t")[0]: l.rstrip("\n").split("\t") for l in (_pl.Path(__file__).parent / "busca" / "cobertura.tsv").read_text(encoding="utf-8").splitlines()[1:]}
for c in CARDS:
    if c["kind"] == "autoral" and c["key"] in _COB:
        c["busca"] = BUSCA + _COB[c["key"]][6] + " Candidatos lidos: " + _COB[c["key"]][4] + "."
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
