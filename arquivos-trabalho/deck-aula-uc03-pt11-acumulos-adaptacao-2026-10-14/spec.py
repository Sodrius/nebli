# Especificação curada — Acúmulos e adaptação celular (UC03 P1, Patologia; Prof. Luiz F. Ferraz da Silva).
# Sequência = parte I Adaptação (lâminas 1–30) + parte II Acúmulos (31–60). Morte celular = 09; envelhecimento = 13; neoplasia/displasia = P4.
RUN_ID = "uc03-pt11-20261014a"
SHORT = "pt11"
LESSON = "2026-uc03-patologia-11-acumulos-adaptacao"
DECK = "NEBLI::UC03::P1::Patologia::Acúmulos e adaptação celular"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por seções inteiras (B&B Cellular Adaptations; FirstAid adaptations e calcification; busca/tags-secao.txt) e por frases "
         "(pigmentos, esteatose, hemocromatose; busca/anking.txt); cópias NEBLI vivas conferidas por nid de origem, 14/10: ")
EXCLUIDOS = [
 (1468101721156, "lábil: coberto pelo organizador a-tecidos (três classes)"),
 (1463345947474, "HPB sem risco de câncer: nuance clínica fora das lâminas"),
 (1482203859036, "Barrett: metaplasia do esôfago não citada na aula (o exemplo da aula é o fumante)"),
 (1476583144320, "vitamina A e metaplasia: não citada"),
 (1487461112379, "displasia: aula de neoplasias (P4)"),
 (1486590815608, "HFE/cromossomo 6: genética da hemocromatose fora do recorte"),
 (1518398479841, "caquexia em doenças crônicas: só uma linha de Extra (causa de atrofia)"),
]
FORA_DO_RECORTE = [
 "Morte celular (necrose/apoptose): aula 09; aqui só a atrofia por apoptose associada.",
 "Displasia e neoplasia: P4.",
 "Tabela das glicogenoses (lâmina 48): bioquímica; aqui só o princípio do acúmulo de glicogênio.",
 "Ilustrações: fisiculturistas, Prometeu, tatuagem, Mr. Burns.",
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


ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
G = lambda *k: {i: V for i in k}
NAO = "o AnKing não tem este conjunto/nome como card (só fatos isolados ou outra formulação)."
EP_CONJ = [1487460256729, 1487458829921, 1487461060183]       # tipo de adaptação → nome
EP_ACUM = [1486590985316, 1486522804267, 1472160925535]       # substância acumulada → nome/aspecto

A_, B_, C_, D_, E_, F_ = "A-adaptacao-geral", "B-hipertrofia", "C-hiperplasia", "D-atrofia-metaplasia", "E-acumulos-lipides-proteinas", "F-calcificacao-pigmentos"

CARDS = [
 # ---------- A. Adaptação: conceito e tecidos (1–5) ----------
 au("a-tecidos", ORG("<b>Tissues</b> by capacity to divide:<br>- {{c1::labile}}: divide continuously (epithelia, bone marrow)<br>- {{c2::stable}}: quiescent but can divide (liver, kidney, fibroblasts)<br>- {{c3::permanent}}: cannot divide (neurons, cardiac and skeletal muscle)"),
    G(1, 2, 3), A_, "Tecidos lábeis, estáveis e permanentes", 3, "central", NAO, EP_CONJ, "Verde: lâmina 3; decide se a adaptação é hipertrofia ou hiperplasia.",
    extra="- Permanent tissues can adapt only by hypertrophy"),
 ak("ak-permanente-hipertrofia", 1487460268378, G(1), A_, "Tecido permanente só hipertrofia", 3, "Verde: HY 3; prova 2018 P1 1.4 (miocárdio permanente)."),
 au("a-tipos", ORG("The four cellular <b>adaptations</b>:<br>- {{c1::hyperplasia}}<br>- {{c2::hypertrophy}}<br>- {{c3::atrophy}}<br>- {{c4::metaplasia}}"),
    G(1, 2, 3, 4), A_, "As quatro adaptações", 5, "central", NAO, EP_CONJ, "Verde: lâmina 5.", duplicacao_ok="ganho: conjunto das quatro adaptações; os AnKing definem cada uma",
    extra="- Adaptation reaches a new steady state while the cell stays viable"),

 # ---------- B. Hipertrofia (6–14) ----------
 ak("ak-hipertrofia", 1487460256729, {1: Z}, B_, "Hipertrofia = aumento do tamanho", 6, "Azul: HY 3; definição da lâmina 6.",
    extra_add="- No new cells: the existing ones grow"),
 ak("ak-hipertrofia-genes", 1487460262238, G(1), B_, "Hipertrofia: ativação gênica e síntese proteica", 6, "Verde: HY 2; lâminas 6 e 11."),
 au("b-utero", "During pregnancy, {{c1::estrogen}} enlarges the <b>uterus</b> by smooth muscle hypertrophy and hyperplasia",
    {1: Z}, B_, "Hipertrofia fisiológica hormonal", "7; cruzadas 7", "central", NAO, EP_CONJ, "Azul: exemplo fisiológico da lâmina 7.",
    extra="- Weight training causes physiologic hypertrophy by increased workload"),
 ak("ak-hve", 1471276964931, G(1), B_, "Hipertrofia patológica do VE", 8, "Verde: HY 1; lâmina 8 (hipertensão)."),
 au("b-gatilhos", ORG("Triggers of <b>cardiac hypertrophy</b>:<br>- mechanical {{c1::stretch}}<br>- {{c2::α-adrenergic}} agonists and angiotensin<br>- {{c3::growth factors}} (e.g., IGF-1)"),
    G(1, 2, 3), B_, "Gatilhos da hipertrofia", "10–12; prova 2018 P1 1.4", "prova", NAO, EP_CONJ, "Verde: prova 2018.",
    extra="- They converge on transcription factors (GATA4, NFAT, MEF2)<br>- Beyond its limit, the heart dilates and fails"),
 au("b-genes-fetais", "<b>Hypertrophied myocytes</b> re-express fetal genes such as atrial natriuretic factor and {{c1::β-myosin heavy chain}}",
    {1: R}, B_, "Reexpressão de genes fetais", 13, "lateral", NAO, EP_CONJ, "Rosa: lâmina 13; detalhe molecular (revisão 15/10).",
    extra="- β-MHC contracts more slowly but spends less energy"),

 # ---------- C. Hiperplasia (15–19) ----------
 ak("ak-hiperplasia", 1487458829921, {1: Z}, C_, "Hiperplasia = aumento do número", 15, "Azul: HY 3; definição (cruzadas 12)."),
 au("c-fisiologica", ORG("Physiologic <b>hyperplasia</b>:<br>- {{c1::hormonal}}: breast and uterus in pregnancy<br>- {{c2::compensatory}}: liver regrowth after partial hepatectomy"),
    G(1, 2), C_, "Hiperplasia hormonal × compensatória", "15–17; cruzadas 1, 2, 15", "central", NAO, EP_CONJ, "Verde: lâminas 15–17."),
 au("c-endometrio", "Excess {{c1::estrogen}} relative to progesterone causes <b>endometrial hyperplasia</b>, fertile ground for carcinoma",
    {1: Z}, C_, "Hiperplasia patológica", 18, "central", NAO, EP_CONJ, "Azul: lâmina 18.", duplicacao_ok="ganho: estímulo patológico (desequilíbrio estrógeno/progesterona); b-utero cobra o estímulo fisiológico",
    extra="- Androgens cause prostatic hyperplasia; viruses cause warts"),
 au("c-controlada", "<b>Hyperplasia</b> stays controlled and regresses when the stimulus is removed, whereas {{c1::neoplasia}} keeps proliferating autonomously",
    {1: Z}, C_, "Hiperplasia × neoplasia", "18; cruzadas 20", "central", NAO, EP_CONJ, "Azul: lâmina 18.",
    duplicacao_ok="ganho: diferença com neoplasia; o AnKing define hiperplasia pelo número de células"),

 # ---------- D. Atrofia, hipoplasia, metaplasia (20–29) ----------
 ak("ak-atrofia", 1487460276914, {1: Z}, D_, "Atrofia = redução por tamanho ou número", 20, "Azul: HY 3; lâmina 20."),
 au("d-causas-atrofia", ORG("Causes of pathologic <b>atrophy</b>:<br>- {{c1::disuse}} (bedridden patients)<br>- loss of {{c2::innervation}}<br>- {{c3::ischemia}} (senile atrophy)<br>- inadequate nutrition<br>- loss of hormonal stimulation"),
    {1: Z, 2: Z, 3: Z}, D_, "Causas de atrofia", "22; cruzadas 3, 9, 17", "central", NAO, EP_CONJ, "Azul: lâmina 22.",
    extra="- Cachexia (TNF in cancer and inflammation) causes muscle atrophy"),
 ak("ak-mama-menopausa", 1463356283395, G(1), D_, "Atrofia por perda hormonal", 22, "Verde: HY 1; menopausa (lâmina 22)."),
 ak("ak-proteassomo", 1487461046220, G(1), D_, "Atrofia: ubiquitina-proteassomo", 23, "Verde: HY 1; lâmina 23 (cruzadas 4)."),
 ak("ak-autofagia", 1487461053514, G(1), D_, "Atrofia: autofagia", 23, "Verde: HY 1; lâmina 23."),
 sh(1792026504769, "verde", D_, "Atrofia por apoptose", 23, "Verde: atrofia por redução do número; viva na 09."),
 ak("ak-hipoplasia", 1487461143308, G(1), D_, "Hipoplasia", 27, "Verde: HY 2; lâmina 27."),
 ak("ak-aplasia", 1487461136378, G(1), D_, "Aplasia", 27, "Verde: HY 2; lâmina 27."),
 ak("ak-metaplasia", 1487461060183, {1: Z}, D_, "Metaplasia = substituição de um tipo celular", 28, "Azul: HY 3; lâmina 28."),
 ak("ak-metaplasia-tronco", 1487461072030, G(1), D_, "Metaplasia por reprogramação de células-tronco", 28, "Verde: HY 2; lâmina 28 (cruzadas 18)."),
 au("d-fumante", "In smokers, the ciliated columnar epithelium of the bronchi is replaced by {{c1::stratified squamous}} epithelium",
    G(1), D_, "Metaplasia escamosa do fumante", "28–29; cruzadas 25", "central", NAO, EP_CONJ, "Verde: exemplo da lâmina 28.",
    extra="- Tougher, but loses mucus secretion and ciliary clearance"),
 ak("ak-metaplasia-cancer", 1487461083189, G(1), D_, "Metaplasia pode evoluir para câncer", 28, "Verde: HY 2; lâmina 28."),

 # ---------- E. Acúmulos: lipídios, proteínas, glicogênio (32–48) ----------
 au("e-mecanismos", ORG("Mechanisms of intracellular <b>accumulation</b>:<br>- excess production or slow metabolism, e.g., {{c1::fatty liver}}<br>- defective folding, transport or enzyme, e.g., {{c2::lysosomal storage}} diseases<br>- indigestible exogenous material, e.g., {{c3::anthracosis}}"),
    G(1, 2, 3), E_, "Mecanismos de acúmulo", "33–34", "central", NAO, EP_ACUM, "Verde: lâminas 33–34."),
 sh(1791022171477, "verde", E_, "Esteatose macrovesicular", 35, "Verde: lâmina 35; viva na Correlação."),
 au("e-diabetes", "In uncontrolled diabetes, lack of insulin activates adipose {{c1::hormone-sensitive lipase}}, flooding the liver with fatty acids",
    G(1), E_, "Esteatose por excesso de ácidos graxos", "37; provas 2023 P1 2.5 e 2024 P1 2.10", "prova", NAO, EP_ACUM, "Verde: lâmina 37; provas 2023/2024.",
    extra="- Fasting and malnutrition mobilize fatty acids the same way"),
 au("e-vldl", "Hepatocytes export triglycerides only after packaging them with {{c1::apoproteins}} into VLDL",
    G(1), E_, "Exportação de lipídios do hepatócito", "38; cruzadas 5", "central", NAO, EP_ACUM, "Verde: lâmina 38."),
 ak("ak-ccl4", 1487470267945, G(1, 2), E_, "CCl₄ reduz apolipoproteínas → esteatose", 38, "Verde: HY 2; lâmina 38."),
 ak("ak-kwashiorkor", 1476584121141, G(1), E_, "Desnutrição reduz apolipoproteínas", 39, "Verde: HY 2; lâmina 39 (inanição)."),
 sh(1791022171771, "azul", E_, "Esteatose alcoólica reversível", 39, "Azul: álcool (lâmina 39); viva na Correlação."),
 ak("ak-alcool-nadh", 1476651936610, {1: Z, 2: Z}, E_, "Álcool: NADH alto → glicerol-3-fosfato → triglicerídeos", 39, "Azul: lâmina 39; provas 2016 (efeito do álcool sobre o fígado) e 2019 (mecanismo da esteatose). Revisão 15/10."),
 ak("ak-xantoma", 1472160925535, G(1, 2, 3), E_, "Xantomas: histiócitos carregados de lipídio", 41, "Verde: HY 1; lâmina 41."),
 au("e-espumosas", "<b>Macrophages</b> that engulf cholesterol become {{c1::foam}} cells, seen in atherosclerotic plaques and xanthomas",
    G(1), E_, "Células espumosas", "41–42; cruzadas 19", "central", NAO, EP_ACUM, "Verde: lâminas 41–42."),
 au("e-russell", "Plasma cells overproducing immunoglobulin, as in myeloma, accumulate it as eosinophilic {{c1::Russell bodies}}",
    {1: Z}, E_, "Acúmulo de proteína por excesso de produção", "44; prova 2024 P1 1.5", "prova", NAO, EP_ACUM, "Azul: prova 2024."),
 au("e-gotas-hialinas", "In heavy proteinuria, proximal tubule cells accumulate reabsorbed protein as eosinophilic {{c1::hyaline droplets}}",
    {1: R}, E_, "Acúmulo de proteína por reabsorção", 44, "lateral", NAO, EP_ACUM, "Rosa: exemplo da lâmina 44."),
 au("e-glicogenio", "<b>Glycogen</b> accumulates in cells in poorly controlled {{c1::diabetes}} and in inherited glycogen storage diseases",
    {1: Z}, E_, "Acúmulo de glicogênio", 47, "central", NAO, EP_ACUM, "Azul: lâmina 47.", duplicacao_ok="ganho: acúmulo de glicogênio; e-diabetes cobra a lipase"),

 # ---------- F. Calcificação e pigmentos (49–58) ----------
 ak("ak-distrofica", 1487470017343, G(1), F_, "Calcificação distrófica: tecido necrótico", 49, "Verde: HY 2; lâmina 49."),
 ak("ak-distrofica-normocalcemia", 1487470068885, G(1), F_, "Distrófica com cálcio normal", 49, "Verde: HY 2; lâmina 49."),
 ak("ak-metastatica", 1487470072763, G(1), F_, "Metastática: tecido normal", 49, "Verde: HY 2; lâmina 49."),
 ak("ak-metastatica-hipercalcemia", 1487470077436, G(1), F_, "Metastática por hipercalcemia", 49, "Verde: HY 2; lâmina 49."),
 au("f-causas-metastatica", ORG("Causes of <b>metastatic calcification</b>:<br>- excess {{c1::PTH}}<br>- bone destruction (myeloma, metastases)<br>- vitamin {{c2::D}} disorders<br>- {{c3::renal failure}} (phosphate retention)"),
    {1: Z, 2: Z, 3: Z}, F_, "Causas de calcificação metastática", "51; cruzadas 14", "central", NAO, EP_ACUM, "Azul: lâmina 51."),
 au("f-antracose", "Inhaled carbon dust stored in lung macrophages, the most common exogenous pigment, is {{c1::anthracosis}}",
    G(1), F_, "Antracose", "52; provas 2017 P1 2.2 e 2019 P1 4.1; cruzadas 21", "prova", NAO, EP_ACUM, "Verde: provas 2017 e 2019.",
    extra="- Sources: air pollution and smoking; tattoo ink is another exogenous pigment",
    duplicacao_ok="ganho: o organizador e-mecanismos usa a antracose só como exemplo"),
 ak("ak-lipofuscina", 1486590985316, G(1), F_, "Lipofuscina", 53, "Verde: HY 1; lâmina 53."),
 au("f-atrofia-parda", "Lipofuscin accumulating in atrophic cells, as in the aging heart, produces {{c1::brown atrophy}}",
    {1: Z}, F_, "Atrofia parda", "53; cruzadas 26", "central", NAO, EP_ACUM, "Azul: lâmina 53.",
    extra="- Lipofuscin comes from lipid peroxidation of membranes and is harmless"),
 au("f-melanina", "<b>Melanin</b>, the only endogenous brown pigment, is made from tyrosine by {{c1::tyrosinase}} in melanocytes",
    {1: Z}, F_, "Melanina", 54, "central", NAO, EP_ACUM, "Azul: lâmina 54."),
 au("f-hemossiderina", "Iron stored as ferritin aggregates into golden-brown {{c1::hemosiderin}} granules after hemorrhage or repeated transfusions",
    G(1), F_, "Hemossiderina", "55–56; cruzadas 6", "central", NAO, EP_ACUM, "Verde: lâminas 55–56."),
 sh(1791810363896, "azul", F_, "Prussian blue cora ferro", 56, "Azul: coloração azul da lâmina 56; viva na 03."),
 ak("ak-hemocromatose", 1486590838863, G(1, 4), F_, "Tríade da hemocromatose", 57, "Verde: HY 1; lâmina 57."),
 au("f-ictericia", "<b>Bilirubin</b>, derived from heme but lacking iron, stains tissues yellow-green in {{c1::jaundice}}",
    G(1), F_, "Bilirrubina e icterícia", "58; prova 2018 P1 1.17; cruzadas 8", "prova", NAO, EP_ACUM, "Verde: lâmina 58; prova 2018."),
]

SEM_IMAGEM = "fato ou conjunto sem estrutura a reconhecer em imagem; a aula usa fotos só como ilustração"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM

BOLD = {"b-gatilhos": [], "c-endometrio": ["estrogen"], "d-fumante": ["smokers"], "e-diabetes": ["uncontrolled diabetes"], "e-vldl": ["Hepatocytes"],
        "e-russell": ["Plasma cells"], "e-gotas-hialinas": ["proteinuria"], "f-antracose": ["carbon dust"], "f-atrofia-parda": ["Lipofuscin"],
        "f-hemossiderina": ["ferritin"], "c-fisiologica": []}
for c in CARDS:
    for ph in BOLD.get(c["key"], []):
        if c["kind"] == "autoral" and f"<b>{ph}</b>" not in c["text"] and ph in c["text"]:
            c["text"] = c["text"].replace(ph, f"<b>{ph}</b>", 1)

VERSO = {"ak-alcool-nadh": "- The same high NADH/NAD+ ratio slows fatty acid β-oxidation, so fat builds up in hepatocytes", 
 "c-fisiologica": "- Removing the stimulus ends the proliferation",
 "c-controlada": "- Neoplastic cells ignore growth and stop signals",
 "e-mecanismos": "- A fourth route: abnormal proteins that cannot be degraded",
 "e-vldl": "- Starvation and CCl₄ reduce apoprotein synthesis, trapping fat",
 "e-espumosas": "- Their foamy look comes from cholesterol vacuoles",
 "e-russell": "- Excess or misassembled immunoglobulin cannot be exported",
 "e-gotas-hialinas": "- Leaked protein is reabsorbed faster than it can be digested",
 "e-glicogenio": "- In diabetes, glycogen appears in renal tubules and liver",
 "f-causas-metastatica": "- All raise serum calcium or phosphate",
 "f-melanina": "- Melanocytes transfer it to keratinocytes",
 "f-hemossiderina": "- Iron + apoferritin → ferritin micelles → hemosiderin granules",
 "f-ictericia": "- Hemosiderin keeps the iron; bilirubin is the iron-free part of heme",
 "ak-permanente-hipertrofia": "- Example: the myocardium thickens in hypertension instead of adding cells",
 "ak-hipertrofia-genes": "- More contractile proteins and organelles per cell",
 "ak-hve": "- Concentric hypertrophy lowers wall stress",
 "ak-hiperplasia": "- Possible only in tissues whose cells can divide",
 "ak-atrofia": "- Cells shrink to a size compatible with survival; they are not dead",
 "ak-mama-menopausa": "- Loss of estrogen removes the trophic stimulus",
 "ak-proteassomo": "- Protein synthesis falls and degradation rises",
 "ak-autofagia": "- The cell digests its own organelles in lysosomes",
 "ak-hipoplasia": "- The organ never reached normal size; it is not atrophy",
 "ak-aplasia": "- The extreme form: the organ never developed",
 "ak-metaplasia": "- One adult cell type is replaced by another adult type",
 "ak-metaplasia-tronco": "- It is reprogramming, not dedifferentiation of mature cells",
 "ak-metaplasia-cancer": "- If the stimulus persists, dysplasia and carcinoma may follow",
 "ak-ccl4": "- Without apoproteins, triglycerides cannot leave as VLDL",
 "ak-kwashiorkor": "- Protein deficiency limits apoprotein synthesis",
 "ak-xantoma": "- Cholesterol accumulates in macrophages (foam cells)",
 "ak-distrofica": "- Examples: caseous necrosis, atherosclerotic plaques, old scars, damaged valves",
 "ak-distrofica-normocalcemia": "- It depends on local tissue damage, not on serum calcium",
 "ak-metastatica": "- Kidney, lung and gastric mucosa are typical sites",
 "ak-metastatica-hipercalcemia": "- Serum calcium or phosphate is high",
 "ak-lipofuscina": "- Product of lipid peroxidation stored in lysosomes",
 "ak-hemocromatose": "- Excess iron deposits as hemosiderin and damages organs via free radicals",
 "a-tipos": "- Hyperplasia and hypertrophy often occur together",
}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Reconhecer e explicar as adaptações celulares (hipertrofia, hiperplasia, atrofia, metaplasia) pelos seus mecanismos e pelo tipo de tecido, e os principais acúmulos intracelulares (lipídios, colesterol, proteínas, glicogênio, cálcio, pigmentos) pelo mecanismo que os causa.",
 "centrais": [
   ("adaptação e tecidos", "a-tecidos", "ak-permanente-hipertrofia", "a-tipos"),
   ("hipertrofia", "ak-hipertrofia", "ak-hipertrofia-genes", "b-utero", "ak-hve", "b-gatilhos", "b-genes-fetais"),
   ("hiperplasia", "ak-hiperplasia", "c-fisiologica", "c-endometrio", "c-controlada"),
   ("atrofia, hipoplasia, metaplasia", "ak-atrofia", "d-causas-atrofia", "ak-mama-menopausa", "ak-proteassomo", "ak-autofagia", "sh-1792026504769", "ak-hipoplasia", "ak-aplasia", "ak-metaplasia", "ak-metaplasia-tronco", "d-fumante", "ak-metaplasia-cancer"),
   ("acúmulos", "e-mecanismos", "sh-1791022171477", "e-diabetes", "e-vldl", "ak-ccl4", "ak-kwashiorkor", "sh-1791022171771", "ak-alcool-nadh", "ak-xantoma", "e-espumosas", "e-russell", "e-gotas-hialinas", "e-glicogenio"),
   ("calcificação e pigmentos", "ak-distrofica", "ak-distrofica-normocalcemia", "ak-metastatica", "ak-metastatica-hipercalcemia", "f-causas-metastatica", "f-antracose", "ak-lipofuscina", "f-atrofia-parda", "f-melanina", "f-hemossiderina", "sh-1791810363896", "ak-hemocromatose", "f-ictericia"),
 ],
 "exemplos": ["fisiculturistas", "Prometeu", "osteoporose", "tatuagem", "asma (músculo liso)"],
 "outras_aulas": [("morte celular", "09 Lesão celular"), ("envelhecimento", "13 Envelhecimento"), ("displasia e neoplasia", "P4"), ("inflamação crônica (remodelamento)", "62")],
}

_M2 = "Completude 15/10: lâminas e transcrição inventariadas por informação (F-20261015-CLAUDE-04; auditoria)."
G = lambda *k: {i: V for i in k}
CARDS.append(au("a-definicao", "A change in <b>cell size, number or type</b> that reaches a new steady state while keeping the cell alive is a cellular {{c1::adaptation}}",
    {1: V}, A_, "Definição de adaptação", "5", "central", NAO, EP_CONJ, "Verde: lâmina 5. " + _M2,
    extra="- The stimulus is sublethal; if it ends, the tissue tends to return to normal"))
CARDS.append(au("b-fisio-pato", ORG("<b>Hypertrophy</b>:<br>- physiologic: more functional demand or hormones, e.g. skeletal muscle in training, {{c1::uterus}} in pregnancy<br>- pathologic: {{c2::myocardium}} in hypertension or aortic valve disease"),
    {1: Z, 2: Z}, B_, "Hipertrofia fisiológica × patológica", "8", "central", NAO, EP_CONJ, "Azul: lâminas 6–8. " + _M2))
CARDS.append(au("b-limite", "When a stress exceeds the capacity of <b>adaptation</b>, as in a heart that can hypertrophy no further, the cell suffers {{c1::injury}} and may die",
    {1: V}, B_, "Conexão: limite da adaptação → lesão (aula 09)", "10", "central", NAO, EP_CONJ, "Verde: lâmina 10 (limite da adaptação; dilatação e insuficiência cardíaca); conexão com a aula 09. " + _M2,
    extra="- Adaptation, reversible injury and cell death form one continuum"))
CARDS.append(ak("ak-hpb", 1463345940337, {1: V}, C_, "Hiperplasia prostática por andrógenos", "18", "Verde: HY 1; lâmina 18 (andrógenos → hiperplasia prostática). " + _M2, extra_add="- Androgens (DHT) drive it, an example of pathologic hormonal hyperplasia"))
CARDS.append(au("c-viral", "Some viruses, such as {{c1::papillomaviruses}}, stimulate <b>epithelial hyperplasia</b> that forms warts",
    {1: R}, C_, "Hiperplasia viral", "18", "lateral", NAO, EP_CONJ, "Rosa: lâmina 18 (infecções virais: pólipos, verrugas). " + _M2))
CARDS.append(au("d-atrofia-fisio", "Physiologic <b>atrophy</b> removes structures no longer needed, such as the {{c1::thyroglossal duct}} and notochord in the embryo or the uterus after delivery",
    {1: R}, D_, "Atrofia fisiológica", "21", "lateral", NAO, EP_CONJ, "Rosa: lâmina 21. " + _M2))
CARDS.append(au("d-mecanismo-atrofia", ORG("Mechanism of <b>atrophy</b>:<br>- less protein synthesis, e.g. less {{c1::insulin}} or workload<br>- more degradation by {{c2::ubiquitin–proteasome}} and autophagy<br>- degradation driven by glucocorticoids, thyroid hormone, {{c3::TNF-α}} and IL-1β"),
    G(1, 2, 3), D_, "Mecanismo geral e mediadores da atrofia", "24", "central", NAO, EP_CONJ, "Verde: lâminas 23–24 (mediadores estavam só no Tab; auditoria). " + _M2,
    extra="- The same pathway causes the muscle wasting of cancer cachexia", duplicacao_ok="compreensão que liga os AnKing de proteassomo e autofagia aos mediadores"))
CARDS.append(ak("ak-barrett", 1482203859036, {1: V, 2: V}, D_, "Metaplasia de Barrett", "29", "Verde: HY 1; lâmina 29 (esquemas de metaplasia). " + _M2))
CARDS.append(au("f-sitios-distrofica", ORG("Typical sites of <b>dystrophic calcification</b>:<br>- {{c1::caseous necrosis}} (tuberculosis)<br>- atherosclerotic plaques<br>- damaged or aged {{c2::heart valves}}<br>- necrotic tumors and old scars"),
    {1: Z, 2: Z}, F_, "Onde ocorre a calcificação distrófica", "50", "central", NAO, EP_ACUM, "Azul: lâmina 50. " + _M2,
    extra="- All are dead or damaged tissue, so calcium levels stay normal"))
CARDS.append(au("f-mapa-pigmentos", ORG("<b>Pigments</b> in tissues:<br>- exogenous: carbon ({{c1::anthracosis}}), tattoo ink<br>- endogenous: {{c2::lipofuscin}} (aging), melanin, {{c3::hemosiderin}} (iron) and bilirubin (jaundice)"),
    G(1, 2, 3), F_, "Mapa dos pigmentos", "52", "central", NAO, EP_ACUM, "Verde: lâminas 52–59 (classificação final estava só implícita; auditoria). " + _M2,
    extra="- Hemosiderin has iron; bilirubin, also from hemoglobin, has none", duplicacao_ok="organizador; cada pigmento tem card próprio"))
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    _x_ = {"b-fisio-pato": "- Both use the same machinery: more protein synthesis and larger cells, without new cells in permanent tissues",
           "c-viral": "- Wound healing also involves hyperplasia of connective tissue",
           "d-atrofia-fisio": "- Pathologic atrophy instead follows disuse, denervation, ischemia, malnutrition or hormone loss"}.get(_c_["key"])
    if _x_: _c_["extra"] = _x_
    if _c_["key"] in ("a-definicao", "b-fisio-pato", "b-limite", "c-viral", "d-atrofia-fisio", "d-mecanismo-atrofia", "f-sitios-distrofica", "f-mapa-pigmentos") and "<img" not in _c_.get("text", ""):
        _c_["sem_imagem"] = "conceito ou organizador; a morfologia correspondente tem card próprio com imagem"
    if _c_["key"] == "d-fumante": _c_["duplicacao_ok"] = "metaplasia escamosa do fumante; Barrett é outra direção (escamoso → colunar)"
