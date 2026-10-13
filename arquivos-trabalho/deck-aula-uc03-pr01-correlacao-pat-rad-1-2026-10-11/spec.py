# Especificação curada — Correlação patológica-radiológica 1 (UC03 P1, Patologia + Radiologia, aula 06; lâminas Ia (33) e Ib (43), só imagens).
# Ordem = lâminas de Ib (Ia é o caso 1 isolado). Caso 1: homem de 60 anos, tabagista, tosse e febre → enfisema + pneumonia do lobo inferior esquerdo
# com derrame pleural; caso 2: homem de 20 anos com aumento testicular → seminoma e radiografia de tórax para metástase.
# Aula de correlação = ler a imagem e ligá-la à lesão. A física e a terminologia dos métodos já estão nas aulas 02/04/05 (entram por sh()).
# Tumores (biologia, metástase, marcadores) têm aulas próprias na P3: do seminoma fica só o reconhecer na imagem e na peça.
# Feita direto pelo coordenador (Opus) em 13/10/2026, sem agente, a partir de inventario.py.
RUN_ID = "uc03-pr01-20261013a"
SHORT = "pr01"
LESSON = "2026-uc03-patologia-radiologia-06-correlacao-1"
DECK = "NEBLI::UC03::P1::Patologia::Correlação patológica-radiológica 1"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261012-CLAUDE-02) + plano vigente, 13/10/2026"
_IMG = ("rx-enfisema", "tc-bolhas", "macro-bolhas", "histo-normal", "histo-enfisema", "rx-consolidacao", "rx-comparacao", "us-derrame",
        "tc-derrame", "cito-neutrofilos", "rx-menisco", "silhueta-esquema", "rx-lingula", "rx-lobo-inferior", "macro-pneumonia", "histo-pneumonia",
        "us-testiculo-normal", "us-nodulo", "doppler-nodulo", "macro-seminoma", "macro-seminoma-corte", "histo-seminoma", "rx-perfil", "rx-pa-normal")
MEDIA = {f"pr01-{n}.png": f"img/pr01-{n}.png" for n in _IMG}
F = lambda n, w=460: f'<img src="pr01-{n}.png" width="{w}">'
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 40 consultas; busca/anking2.txt, 21 consultas sobre bordas cardíacas, "
         "silhueta, consolidação, derrame, bolha, ultrassom testicular, metástase), cópias NEBLI vivas das aulas 04, 23 e 24 conferidas, 13/10: ")
FALTA = "AnKing e externos não têm o achado de imagem desta aula nem a correlação imagem → lesão (só a doença em texto ou casos de outras áreas)."
EXCLUIDOS = [
 (1468531923039, "deficiência de α1-antitripsina: não é o caso da aula (tabagista); panacinar fica fora"),
 (1473627994933, "enfisema panacinar por α1-antitripsina: fora do caso"),
 (1473548445520, "agentes da pneumonia lobar: microbiologia da Patogenicidade, a aula não discute agente"),
 (1474503845229, "sopro brônquico/egofonia: semiologia, fora da aula"),
 (1495891478051, "tratamento do derrame parapneumônico: clínica, fora do recorte"),
 (1474503822233, "desvio da traqueia no derrame grande: aula 04 (Radiografia), apostila de RD aula 2"),
 (1463339983674, "radiossensibilidade e prognóstico do seminoma: oncologia clínica, fora da aula"),
 (1463340008364, "PLAP: marcador tumoral, aula de tumores"),
 (1463339928621, "transiluminação: semiologia, a aula usa ultrassom"),
 (1473733209170, "metástases em bala de canhão: aula 24 Angiogênese e metástases"),
 (1505849451028, "orquiectomia inguinal: conduta, fora da aula"),
 (1473548457637, "fase de congestão da pneumonia lobar: não mostrada isoladamente; a aula mostra a hepatização"),
 (1473548476620, "resolução da pneumonia lobar: fora das lâminas"),
 (1555363662790, "imagem de pneumonia do lobo médio sem pergunta própria: o alvo (silhueta do lobo médio) virou card autoral"),
]
FORA_DO_RECORTE = [
 "Lâmina 22 (aglomerados de células epiteliais atípicas no líquido): sem transcrição, não dá para afirmar se são células malignas ou mesoteliais reativas; pergunta ao Davi.",
 "Anatomia fina dos contornos do mediastino e dos hilos (lâminas 5 e 7): é da aula 04; aqui só as bordas cardíacas usadas no sinal da silhueta.",
 "Histologia do testículo normal (lâmina 39) e anatomia do epidídimo (lâmina 33): referência normal para contraste; histologia é da UC02.",
 "Apostila de RD: desvio de traqueia/coração (atelectasia × derrame × pneumonia) é da aula 04; broncograma aéreo é citado como frequente em provas, mas não aparece nas lâminas desta aula: pergunta ao Davi.",
 "Biologia dos tumores de células germinativas, marcadores e vias de metástase: aulas 17–24 da Patologia (P3).",
]


def ak(key, src, cor, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=cor if isinstance(cor, dict) else {1: cor}, bloco=bloco, alvo=alvo,
             evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, cor, bloco, alvo, slide, autoria, espelhos, motivo, extra="", dup=""):
    import re
    n = sorted({int(x) for x in re.findall(r"\{\{c(\d+)::", text)})
    return dict(key=key, kind="autoral", text=text, extra=extra, flags={i: cor for i in n}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}",
                autoria=autoria, busca=BUSCA + FALTA, espelhos=espelhos, motivo=motivo, duplicacao_ok=dup)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


EP_CXR = [1473628054935, 1473628062986, 1567711702034]
EP_PATH = [1473548436921, 1473548462128, 1463339990695]
EP_IMG = [1555363662790, 1532390823154, 1496180350957]
EP_US = [1463334201001, 1463339998840, 1463339972200]

# compartilhados vivos
S_INCID, S_HIPER, S_PERFIL = 1791810586046, 1791844788752, 1791844792172          # rd02 incidências; rd04 hiperatenuante, perfil
S_SIL, S_SILPN, S_ANEC = 1791844797227, 1791844797478, 1791844801330             # rd04 silhueta, silhueta-pneumonia, anecoico
S_ANTRA, S_EXSUD, S_EMPI = 1791592721894, 1791169089006, 1791577164590           # pat06 antracose; pat05 exsudato, empiema

A_, B_, C_, D_, E_, G_ = "A-leitura-rx", "B-enfisema", "C-pneumonia", "D-derrame", "E-silhueta", "G-seminoma"
CARDS = [
 # ---------- A. Caso 1 e leitura da radiografia normal (lâminas 2–7) ----------
 sh(S_INCID, "azul", A_, "Associação: PA e perfil", 3, "Azul: a aula abre o caso pelas duas incidências."),
 sh(S_HIPER, "azul", A_, "Associação: área branca = hiperatenuante", 4, "Azul: prova 2015 pede o nome das 'áreas mais brancas'."),
 au("bordas-cardiacas", "On a PA chest film, the right heart border is the right {{c1::atrium}} and the left border is mainly the left {{c2::ventricle}}",
    Z, A_, "Bordas cardíacas na radiografia PA", 5, "central", EP_CXR, "Azul: lâmina 5 rotula as bordas; base do sinal da silhueta (lâminas 25–28).",
    extra=F("rx-pa-normal") + "<br>- The aortic knob and pulmonary trunk form the upper left border"),
 au("perfil-coluna", "On a normal lateral chest radiograph, the lower thoracic spine looks progressively {{c1::darker}} toward the diaphragm",
    Z, A_, "Perfil: pulmão mais radiotransparente embaixo", 6, "central", EP_CXR, "Azul: lâmina 6 ('lungs become more radiolucent').",
    extra=F("rx-perfil") + "<br>- A lower-lobe opacity breaks this gradient over the spine"),
 au("perfil-hemidiafragma", "On a lateral chest radiograph, the anterior part of the {{c1::left}} hemidiaphragm is hidden by the heart",
    R, A_, "Perfil: hemidiafragmas direito e esquerdo", 6, "lateral", EP_CXR, "Rosa: setas vermelha e azul da lâmina 6, detalhe de leitura.",
    extra="- The right hemidiaphragm is seen along its whole length"),

 # ---------- B. Enfisema (lâminas 8–16) ----------
 ak("enfisema-rx", 1473628054935, {1: V, 2: V}, B_, "RX do enfisema: diâmetro AP e diafragma retificado", 8,
    "Verde: radiografia de 6 meses antes, achado central do caso.", extra_add=F("rx-enfisema")),
 ak("enfisema-lucencia", 1473628062986, V, B_, "RX do enfisema: hipertransparência", 8, "Verde: HY; o termo que a prova pede para descrever a radiografia."),
 au("enfisema-correlacao", "The lungs look hyperlucent on radiographs in emphysema because destroyed alveolar walls leave more {{c1::air}} and less tissue",
    V, B_, "Correlação: hipertransparência = paredes destruídas", 8, "central", EP_PATH, "Verde: a ligação imagem → lesão que a aula ensina.",
    extra="- Less tissue attenuates fewer X-rays"),
 ak("enfisema-destruicao", 1473627940622, {1: V, 2: V, 3: V}, B_, "Enfisema: destruição dos sacos alveolares", 14,
    "Verde: definição da lesão mostrada na macro e na histologia."),
 ak("enfisema-aumento", 1473627929151, Z, B_, "Enfisema: aumento dos espaços aéreos", 15, "Azul: HY que repete a definição do card da destruição.", hy_repete="enfisema-destruicao"),
 ak("enfisema-tabaco", 1473627988643, {1: V, 2: V, 3: V}, B_, "Tabagismo → enfisema centroacinar em lobos superiores", 9,
    "Verde: HY; o caso é de tabagista e a TC mostra lobos superiores."),
 au("tc-bolhas", F("tc-bolhas") + "<br>The large, thin-walled air spaces in this smoker's chest <b>CT</b> are emphysematous {{c1::bullae}}",
    V, B_, "TC: bolhas de enfisema", 9, "central", EP_IMG, "Verde: TC do caso (lâmina 9); reconhecer a lesão na imagem.",
    extra="- They are hypoattenuating, like air"),
 au("bolha-def", "An emphysematous air space larger than {{c1::1 cm}} is called a bulla", R, B_, "Definição de bolha", 11, "lateral", EP_PATH,
    "Rosa: tamanho que define a bolha da peça (lâmina 11).", extra=F("macro-bolhas")),
 sh(S_ANTRA, "rosa", B_, "Associação: antracose na peça do fumante", 10, "Rosa: pigmento negro do pulmão na lâmina 10."),
 au("histo-enfisema", F("histo-enfisema") + "<br>This lung histology with enlarged air spaces and thin, broken septa shows {{c1::emphysema}}",
    Z, B_, "Histologia do enfisema", 15, "central", EP_PATH, "Azul: lâmina 15 contra o normal da 14; reconhecer na lâmina.",
    extra="- Normal lung for comparison:<br>" + F("histo-normal", 360)),

 # ---------- C. Pneumonia: radiografia e patologia (lâminas 17–18, 29–31) ----------
 au("consolidacao-def", "On a chest radiograph, a lung area that turns white because alveolar air is replaced by exudate is called a {{c1::consolidation}}",
    V, C_, "Consolidação = opacidade por preenchimento alveolar", 17, "prova", EP_CXR,
    "Verde: provas 2019 e 2024 pedem 'opacidade/condensação' para descrever o achado.", extra=F("rx-consolidacao") + "<br>- It is a type of opacity"),
 au("comparar-previo", "Comparing with a {{c1::previous}} radiograph shows whether a finding is new", Z, C_, "Comparar com exame anterior", 18,
    "central", EP_IMG, "Azul: lâminas 18 e 24 ('6 meses atrás' × 'atual').", extra=F("rx-comparacao")),
 ak("pn-exsudato", 1473548436921, {1: V, 2: V}, C_, "Pneumonia lobar: exsudato intra-alveolar de neutrófilos", 31,
    "Verde: HY; a lesão que forma a consolidação da radiografia (lâminas 30–31).", extra_add=F("histo-pneumonia")),
 ak("pn-hep-vermelha", 1473548462128, V, C_, "Pneumonia lobar: hepatização vermelha", 30, "Verde: HY; alvéolos com exsudato e hemácias (lâmina 30)."),
 ak("pn-hep-cinzenta", 1473548472722, V, C_, "Pneumonia lobar: hepatização cinzenta", 29, "Verde: HY; peça da lâmina 29.",
    extra_add=F("macro-pneumonia")),

 # ---------- D. Derrame pleural (lâminas 19–24) ----------
 au("us-derrame", F("us-derrame") + "<br>On ultrasound, a pleural effusion appears as an {{c1::anechoic}} collection above the diaphragm",
    Z, D_, "US: derrame pleural anecoico", 19, "central", EP_US, "Azul: lâmina 19, aplicação do termo da aula 04.",
    extra="- Fluid does not reflect sound", dup="ganho: aplica o termo ao derrame da imagem do caso"),
 sh(S_ANEC, "azul", D_, "Associação: líquido é anecoico", 19, "Azul: termo usado na lâmina 19."),
 au("tc-derrame", F("tc-derrame") + "<br>On supine chest <b>CT</b>, a pleural effusion collects in the {{c1::posterior}} pleural space",
    Z, D_, "TC: derrame posterior dependente", 20, "central", EP_IMG, "Azul: lâmina 20.", extra="- Fluid falls to the dependent part of the chest"),
 au("atelectasia-compressiva", "Lung next to a large pleural effusion collapses, a {{c1::compressive}} atelectasis", R, D_, "Atelectasia compressiva", 20,
    "lateral", EP_PATH, "Rosa: pulmão colabado junto ao derrame na TC (lâmina 20).", extra="- The collapsed lung is airless and denser"),
 au("derrame-neutrofilos", F("cito-neutrofilos") + "<br>A pleural fluid full of {{c1::neutrophils}} next to a pneumonia indicates an infected exudate",
    Z, D_, "Citologia do derrame: neutrófilos", 21, "central", EP_PATH, "Azul: lâmina 21; prova 2017 (derrame puncionado no caso de pneumonia).",
    extra="- An effusion next to a pneumonia is parapneumonic", dup="ganho: reconhecer o exsudato na citologia do líquido"),
 sh(S_EXSUD, "azul", D_, "Associação: exsudato por permeabilidade", 21, "Azul: o derrame do caso é exsudato."),
 sh(S_EMPI, "azul", D_, "Associação: empiema", 21, "Azul: líquido purulento da lâmina 21."),
 au("menisco", F("rx-menisco", 300) + "<br>Fluid climbing the lateral chest wall with a concave upper border is the {{c1::meniscus}} sign of pleural effusion",
    V, D_, "Sinal do menisco", 23, "central", EP_CXR, "Verde: sinal nomeado na lâmina 23 e na apostila de RD."),
 au("costofrenico", "The earliest sign of a pleural effusion on a PA chest radiograph is blunting of the {{c1::costophrenic}} angle",
    V, D_, "Velamento do seio costofrênico", 23, "central", EP_CXR, "Verde: apostila de RD e lâminas 4/24 (seios livres × velados).",
    extra="- Fluid gathers first in the lowest part of the pleural space"),

 # ---------- E. Sinal da silhueta e lobos (lâminas 25–28) ----------
 sh(S_SIL, "verde", E_, "Associação: sinal da silhueta", 25, "Verde: título da lâmina 25."),
 sh(S_SILPN, "verde", E_, "Associação: pneumonia apaga a borda cardíaca", 25, "Verde: base da lâmina 25."),
 au("silhueta-lingula", F("rx-lingula") + "<br>An opacity that blurs the left heart border lies in the {{c1::lingula}}",
    V, E_, "Lingula apaga a borda cardíaca esquerda", 27, "central", EP_IMG, "Verde: lâminas 25 e 27, localizar o lobo pelo contorno perdido.",
    extra="- The lingula touches the left ventricle in front"),
 au("silhueta-lobo-inferior", F("rx-lobo-inferior") + "<br>A left lower lobe opacity keeps the heart border but blurs the {{c1::diaphragm}}",
    V, E_, "Lobo inferior apaga o diafragma", 28, "central", EP_IMG, "Verde: lâminas 25 e 28 (caso do paciente).",
    extra="- The lower lobe lies behind the heart, on the diaphragm<br>" + F("silhueta-esquema", 360)),
 au("silhueta-lobo-medio", "An opacity that blurs the right heart border lies in the right {{c1::middle}} lobe", R, E_, "Lobo médio apaga a borda direita", 26,
    "lateral", EP_IMG, "Rosa: lado direito equivalente ao da lingula (anatomia da lâmina 26).", extra="- It touches the right atrium"),
 ak("lingula", 1474511892721, R, E_, "Lingula é do pulmão esquerdo", 26, "Rosa: anatomia da lâmina 26."),
 sh(S_PERFIL, "azul", E_, "Associação: perfil localiza a opacidade", 27, "Azul: lâminas 27–28 confirmam o lobo no perfil."),

 # ---------- G. Caso 2: massa testicular (lâminas 32–41) ----------
 au("us-testiculo-normal", F("us-testiculo-normal") + "<br>On ultrasound, the normal testis has a {{c1::homogeneous}} echotexture",
    R, G_, "US do testículo normal", 33, "lateral", EP_US, "Rosa: referência normal da lâmina 33."),
 au("nodulo-hipoecoico", F("us-nodulo") + "<br>A solid {{c1::hypoechoic}} nodule inside the testis of a young man is suspicious for a germ cell tumor",
    V, G_, "Nódulo testicular hipoecoico", 35, "central", EP_US, "Verde: achado central do caso 2.",
    extra="- An intratesticular solid mass is treated as malignant until proven otherwise",
    dup="ganho: aplica o termo hipoecoico ao nódulo testicular"),
 au("doppler-nodulo", F("doppler-nodulo") + "<br>Color <b>Doppler</b> flow inside a testicular nodule shows that it is a {{c1::solid}} vascularized lesion",
    Z, G_, "Doppler mostra fluxo no nódulo", 36, "central", EP_US, "Azul: lâminas 34 e 36.", extra="- A simple cyst has no internal flow"),
 ak("seminoma-comum", 1463339972200, V, G_, "Seminoma é o tumor testicular mais comum", 37, "Verde: HY; diagnóstico do caso 2."),
 ak("seminoma-macro", 1463339998840, V, G_, "Seminoma: massa homogênea sem hemorragia", 38, "Verde: peça das lâminas 37–38.",
    extra_add=F("macro-seminoma-corte")),
 ak("seminoma-histo", 1463339990695, V, G_, "Seminoma: células claras em 'ovo frito'", 40, "Verde: histologia da lâmina 40.",
    extra_add=F("histo-seminoma")),
 au("rx-metastase", "In a young man with a testicular tumor, a chest radiograph looks for {{c1::lung}} metastases",
    V, G_, "Por que RX de tórax: metástase pulmonar", 41, "central", EP_IMG, "Verde: pergunta final da aula (lâmina 41).",
    extra="- Staging tells how far the tumor has spread"),
]

SEM_IMAGEM = "conceito ou correlação sem estrutura própria a identificar; as imagens do caso estão nos cards de reconhecimento"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "sem_imagem" not in c and "<img" not in c.get("text", "") and "<img" not in c.get("extra", "") \
            and "<img" not in c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM

BOLD = {
 "bordas-cardiacas": ["right heart border", "left border"], "perfil-coluna": ["lateral chest radiograph"], "perfil-hemidiafragma": ["lateral chest radiograph"],
 "enfisema-correlacao": ["hyperlucent"], "bolha-def": ["bulla"], "histo-enfisema": ["thin, broken septa"], "consolidacao-def": ["exudate"],
 "comparar-previo": ["new"], "consolidacao-correlacao": ["consolidation"], "us-derrame": ["pleural effusion"], "tc-derrame": ["pleural effusion"],
 "atelectasia-compressiva": ["pleural effusion"], "derrame-neutrofilos": ["pleural fluid"], "menisco": ["concave"], "costofrenico": ["earliest sign"],
 "silhueta-lingula": ["left heart border"], "silhueta-lobo-inferior": ["keeps the heart border"], "silhueta-lobo-medio": ["right heart border"],
 "us-testiculo-normal": ["normal testis"], "nodulo-hipoecoico": ["inside the testis"], "rx-metastase": ["chest radiograph"], "tc-bolhas": ["thin-walled"],
}
for c in CARDS:
    for ph in BOLD.get(c["key"], []):
        if c["kind"] == "autoral" and f"<b>{ph}</b>" not in c["text"] and ph in c["text"]:
            c["text"] = c["text"].replace(ph, f"<b>{ph}</b>", 1)

VERSO = {
 "enfisema-lucencia": "- Destroyed alveolar walls leave more air and less tissue",
 "bolha-def": "- Bullae are usually subpleural and apical",
 "comparar-previo": "- The film from 6 months earlier had no consolidation or effusion",
 "menisco": "- Fluid rises higher along the lateral chest wall than in the middle",
 "pn-exsudato": "- This exudate is what turns the lobe white on the radiograph",
 "us-testiculo-normal": "- A focal area of different echogenicity breaks this pattern",
 "seminoma-comum": "- It peaks in young men, like the patient of case 2",
 "seminoma-histo": "- Fibrous septa between the sheets carry lymphocytes",
}
DUPLICACAO = {
 "perfil-hemidiafragma": "ganho: leitura do perfil normal; a resposta 'left' coincide só por acaso com outros cards",
 "histo-enfisema": "ganho: reconhecer o enfisema na histologia do caso",
 "tc-derrame": "ganho: localizar o derrame na TC do caso",
 "silhueta-lobo-inferior": "ganho: o lobo inferior apaga o diafragma no sinal da silhueta, alvo diferente do diafragma retificado do enfisema",
}
SLIDE_SEM_ALT = "imagem do próprio caso clínico da aula; reconhecer a imagem do caso é o objetivo da correlação e não há figura equivalente no AnKing"
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = VERSO[k] + ("<br>" + c["extra"] if c.get("extra") else "")
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
    if "pr01-" in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))

REVISAO = {
 "bordas-cardiacas": "lido no deck vivo; encurtado para caber no limite de palavras; figura da lâmina 5 no verso",
 "menisco": "figura recortada sem o título 'Sinal do menisco' para não vazar a resposta",
 "silhueta-lobo-inferior": "PA da lâmina 28 confere: contorno cardíaco visível, diafragma apagado; esquema no verso",
 "silhueta-lingula": "PA da lâmina 27 confere: borda cardíaca esquerda apagada",
 "tc-derrame": "TC da lâmina 20: derrame esquerdo posterior com pulmão colabado",
 "bolha-def": "Robbins cap. 15: bolhas > 1 cm",
}

ESCOPO = {
 "objetivo": "Ler as imagens de dois casos e ligar cada achado à lesão (correlação radiologia + patologia)",
 "centrais": [("hipertransparência do enfisema = paredes alveolares destruídas", "enfisema-correlacao", "enfisema-rx"),
              ("consolidação = alvéolos cheios de exsudato", "consolidacao-def", "pn-exsudato"),
              ("derrame pleural: menisco e seio costofrênico", "menisco", "costofrenico"),
              ("sinal da silhueta localiza o lobo", "silhueta-lingula", "silhueta-lobo-inferior"),
              ("nódulo testicular hipoecoico sólido = suspeita de tumor germinativo", "nodulo-hipoecoico"),
              ("seminoma na peça e na histologia", "seminoma-macro", "seminoma-histo"),
              ("radiografia de tórax para metástase", "rx-metastase")],
 "exemplos": ["lâmina 22 (aglomerados no líquido pleural)", "histologia do testículo normal", "anatomia do epidídimo"],
 "outras_aulas": [("física e termos dos métodos", "02/04/05 Radiologia"), ("biologia, marcadores e metástase dos tumores", "17–24 Patologia"),
                  ("agentes das pneumonias", "35 Patogenicidade"), ("exsudato e empiema", "23 Edema e congestão")],
}
