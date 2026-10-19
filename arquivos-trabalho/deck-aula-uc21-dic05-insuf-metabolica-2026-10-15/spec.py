# Especificação curada — UC21 DIC-I, Caso 5: Insuficiência metabólica — diabete melito (1º semestre 2026; caso de 10 páginas com 12 perguntas).
# Regra da UC21 (MEMORY): o caso guia a cobertura; o que responde às perguntas oficiais = verde; o resto azul/rosa. GR2 Diabetes (UC03) e Bioquímica 10/25/33 já têm quase tudo: sh().
# Aula do 1º semestre → entra suspensa. Ordem = perguntas 1→12 (páginas 7–9 do caso), depois do relato clínico (3–6).
RUN_ID = "uc21-dic05-20261015a"
SHORT = "dic05"
LESSON = "2026-uc21-dic-05-insuficiencia-metabolica"
DECK = "NEBLI::UC21::Grandes insuficiências::Caso 5 — Insuficiência metabólica"
CRITERIOS = "MEMORY.md (UC21: caso guia, perguntas = verde) + ANTI-EXEMPLARES-CARDS (14/10), 15/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (DKA, infection, β-hydroxybutyrate, prerenal, BUN:creatinine, renal threshold, SGLT2, GLUT-1/3, insulin-independent, somatostatin, acanthosis, "
         "celiac, Hashimoto, anabolic insulin; busca/anking.txt) e cópias NEBLI vivas do GR2 Diabetes e Bioquímica 10/25/33, 15/10: ")
EXCLUIDOS = [
 (1524165085062, "infecção precipita hiperglicemia, cloze em 'hyper': e-desencadeantes cobra o nome"),
 (1462327309654, "dois corpos cetônicos no DM1: o card dos três corpos cetônicos (Integração II) cobre"),
 (1462128449086, "causa da acidose = cetoácidos: coberto pelo card de lipólise → cetonas"),
 (1462326105448, "DM1 = deficiência de insulina: trivial diante do card de definição"),
]
FORA_DO_RECORTE = ["Tratamento farmacológico detalhado (tipos de insulina, antidiabéticos orais): GR2.", "Mucormicose na CAD: fora do caso.",
                   "Relatório do grupo, 6c (diabetes insipidus): hipótese errada; o card segue a diurese osmótica."]


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
NAO = "o AnKing não tem este fato do caso como card."
EP = [1462327329868, 1475353385337, 1524165085062]
A_, B_, C_, D_, E_, F_, H_ = "A-caso", "B-DM-e-diagnostico", "C-insulina", "D-transportadores", "E-cetoacidose", "F-agua-e-eletrolitos", "G-complicacoes-e-cuidado"

CARDS = [
 # A — o caso (3–6)
 au("a-caso", ORG("<b>Case 5</b> (boy, 15, drowsy, Kussmaul breathing):<br>- diagnosis: type 1 diabetes in {{c1::diabetic ketoacidosis}}<br>- triggers: missed insulin and a thigh {{c2::abscess}}"),
    G(1, 2), A_, "Síntese do caso", "3; 4", "central", NAO, EP, "Verde: o caso todo; pergunta 3.",
    extra="- 60 days of polyuria, polydipsia and weight loss<br>- Glucose 298 mg/dL, pH 7.01, HCO3 9 mEq/L, K+ 6.5 mEq/L, creatinine 2.3 mg/dL<br>- The abscess grew Streptococcus pyogenes"),
 # B — DM e diagnóstico (pergunta 1 e 3)
 sh(1791054010222, "verde", B_, "Definição de DM", "7", "Verde: pergunta 1a; viva no GR2."),
 sh(1791054010997, "verde", B_, "DM1: destruição por T CD8", "7", "Verde: perguntas 1a e 3; viva no GR2."),
 sh(1791054012847, "verde", B_, "Resistência à insulina no DM2", "7", "Verde: pergunta 1a; viva no GR2."),
 sh(1791054007644, "verde", B_, "Sintomas clássicos sugerem DM1", "7", "Verde: perguntas 1b e 3; viva no GR2."),
 sh(1791054007769, "verde", B_, "Glicemia casual ≥ 200 com sintomas", "7", "Verde: pergunta 1b; viva no GR2."),
 sh(1791054008396, "verde", B_, "Jejum ≥ 126", "7", "Verde: pergunta 1b; viva no GR2."),
 sh(1791054008544, "verde", B_, "TOTG 2 h ≥ 200", "7", "Verde: pergunta 1b; viva no GR2."),
 sh(1791054008670, "verde", B_, "HbA1c ≥ 6,5%", "7", "Verde: pergunta 1b; viva no GR2."),
 au("b-precoce", "Early diagnosis matters because <b>diabetes</b> is the leading cause of adult blindness, of {{c1::end-stage kidney disease}} and of non-traumatic amputation",
    G(1), B_, "Por que diagnosticar cedo", "7", "central", NAO, EP, "Verde: pergunta 1c.",
    extra="- Many people live with silent hyperglycemia for years"),
 # C — insulina (pergunta 2)
 sh(1791647354296, "verde", C_, "GLUT-2 na célula β", "7", "Verde: pergunta 2a; viva na Bioquímica 10."),
 sh(1791729317165, "verde", C_, "ATP fecha canal de K+", "7", "Verde: pergunta 2a; viva na Bioquímica 33."),
 sh(1792027894938, "verde", C_, "Ca2+ dispara exocitose", "7", "Verde: pergunta 2a; viva na Bioquímica 10."),
 au("c-anabolica", ORG("Actions of <b>insulin</b>:<br>- anabolic: glucose uptake, glycogen, protein and {{c1::fat synthesis}}<br>- anti-catabolic: blocks glycogenolysis, proteolysis, {{c2::lipolysis}} and ketogenesis"),
    G(1, 2), C_, "Ações anabólicas e anticatabólicas", "7", "central", NAO, EP, "Verde: pergunta 2b.",
    extra="- Losing the anti-catabolic action is what produces ketoacidosis"),
 sh(1791054013222, "verde", C_, "Contrarreguladores induzem resistência", "7", "Verde: pergunta 2c; viva no GR2."),
 sh(1791054011246, "verde", C_, "Glucagon eleva a glicemia", "7", "Verde: pergunta 2c; viva no GR2."),
 au("c-paracrina", "Besides its endocrine action, <b>insulin</b> acts in a {{c1::paracrine}} way inside the islet, lowering glucagon release by neighboring α cells",
    G(1), C_, "Insulina parácrina e autócrina", "7", "central", NAO, EP, "Verde: pergunta 2d.",
    extra="- It also acts on the β cell itself (autocrine)"),
 sh(1792027895739, "verde", C_, "Receptor tirosina-quinase", "7", "Verde: pergunta 2e; viva na Bioquímica 10."),
 sh(1792027895991, "azul", C_, "Autofosforilação e IRS-1", "7", "Azul: pergunta 2e; viva na Bioquímica 10."),
 au("c-dependentes", ORG("Glucose uptake and <b>insulin</b>:<br>- insulin-dependent (GLUT-4): skeletal muscle, heart, {{c1::adipose tissue}}<br>- insulin-independent: brain, {{c2::red blood cells}}, liver"),
    G(1, 2), C_, "Tecidos dependentes e independentes", "7", "central", NAO, EP, "Verde: pergunta 2f.",
    extra="- Advantage: the brain gets glucose whatever the hormones<br>- Drawback: these tissues cannot adjust uptake, and they are damaged by hyperglycemia"),
 # D — transportadores (pergunta 4)
 sh(1791054011372, "verde", D_, "Insulina insere GLUT-4", "8", "Verde: pergunta 4a; viva no GR2."),
 sh(1792027896339, "azul", D_, "PI3K leva GLUT-4 à membrana", "8", "Azul: pergunta 4a; viva na Bioquímica 10."),
 sh(1791647346120, "verde", D_, "GLUT-2 bidirecional", "8", "Verde: pergunta 4b; viva na Bioquímica 25."),
 au("d-km", "Because hepatic <b>GLUT-2</b> has a high {{c1::Km}}, the liver takes up glucose mainly when blood glucose is high, sparing glucose for the brain in fasting",
    G(1), D_, "Km alto do GLUT-2", "8", "central", NAO, EP, "Verde: pergunta 4b.",
    extra="- The same transporter lets glucose made by the liver leave to the blood"),
 au("d-tm", "The renal <b>tubular maximum</b> for glucose reabsorption is about {{c1::375}} mg/min, mostly through SGLT2 in the proximal tubule",
    G(1), D_, "Tm de glicose", "8", "central", NAO, EP, "Verde: pergunta 4c.",
    extra="- Normal filtered load is about 125 mg/min"),
 au("d-limiar", "<b>Glucose</b> starts to appear in the urine when plasma glucose exceeds the renal threshold of about {{c1::180}} mg/dL",
    G(1), D_, "Limiar renal", "8", "central", NAO, EP, "Verde: pergunta 4c; o caso tem glicosúria com glicemia 260–298.",
    extra="- Glycosuria appears before the Tm because nephrons differ in their maximum"),
 # E — cetoacidose (perguntas 5 e 7)
 sh(1791054012018, "verde", E_, "Kussmaul compensa acidose", "8", "Verde: pergunta 5; viva no GR2."),
 au("e-gasometria", "In the <b>blood gas</b>, pH 7.01 with HCO3− 9 mEq/L and PaCO2 24 mmHg is metabolic acidosis with {{c1::respiratory compensation}}",
    G(1), E_, "Leitura da gasometria", "8; 5", "central", NAO, EP, "Verde: pergunta 5; tabela do caso.",
    extra="- Base excess −15.4 mEq/L"),
 sh(1791054012198, "verde", E_, "Ânion gap aumentado", "8", "Verde: pergunta 5; viva no GR2."),
 sh(1791054011545, "verde", E_, "Glucagon sem oposição", "8", "Verde: pergunta 5; viva no GR2."),
 sh(1791054011671, "verde", E_, "Lipólise → corpos cetônicos", "8", "Verde: pergunta 5; viva no GR2."),
 sh(1791729323438, "azul", E_, "Três corpos cetônicos", "8", "Azul: pergunta 5; viva na Bioquímica 33."),
 au("e-desencadeantes", "The usual triggers of <b>diabetic ketoacidosis</b> are missed insulin doses and {{c1::infection}}, whose stress hormones raise glucose and ketone production",
    G(1), E_, "Desencadeantes da CAD", "8; 9; 4", "central", NAO, EP, "Verde: perguntas 5 e 8 (abscesso e insulina omitida).",
    extra="- Cortisol, catecolamines and glucagon rise during infection"),
 sh(1791054012447, "verde", E_, "EHH: insulina residual impede cetose", "8", "Verde: pergunta 7; viva no GR2."),
 au("e-insulina-dm2", "Early <b>type 2 diabetes</b> shows {{c1::hyperinsulinemia}}, as β cells compensate for insulin resistance",
    {1: Z}, E_, "Insulina plasmática no DM2", "8", "central", NAO, EP, "Azul: pergunta 7.",
    duplicacao_ok="ganho: fase inicial; o sh do GR2 cobra a queda tardia", extra="- So type 2 patients rarely make ketones"),
 sh(1791054012596, "azul", E_, "No DM2 avançado a insulina cai", "8", "Azul: pergunta 7; viva no GR2."),
 # F — água e eletrólitos (pergunta 6)
 ak("ak-prerrenal", 1475353367528, G(1, 2), F_, "Azotemia pré-renal", "8", "Verde: pergunta 6a (creatinina 2,3 por desidratação)."),
 ak("ak-bun", 1475353385337, {1: Z}, F_, "Ureia:creatinina > 20 no pré-renal", "8", "Azul: pergunta 6a."),
 sh(1791054007900, "verde", F_, "K+ sérico alto no DM1 descompensado", "8", "Verde: pergunta 6b; viva no GR2."),
 sh(1791054008019, "verde", F_, "K+ intracelular baixo", "8", "Verde: pergunta 6b; viva no GR2."),
 au("e-k-total", "In <b>diabetic ketoacidosis</b>, total body potassium is {{c1::depleted}} by osmotic diuresis even when serum potassium is high",
    G(1), F_, "K+ corporal total", "8", "central", NAO, EP, "Verde: pergunta 6b.",
    extra="- Insulin treatment drives K+ back into cells and can cause hypokalemia, so K+ is monitored and replaced"),
 sh(1791054008148, "azul", F_, "Insulina ativa Na+/K+-ATPase", "8", "Azul: pergunta 6b; viva no GR2."),
 sh(1791054012320, "verde", F_, "Diurese osmótica", "8", "Verde: pergunta 6c; viva no GR2."),
 au("f-osm", "Dilute urine in large volume despite <b>dehydration</b> here is not diabetes insipidus but {{c1::osmotic diuresis}} from glycosuria",
    {1: Z}, F_, "Osmolaridade no caso", "8", "central", NAO, EP, "Azul: pergunta 6c.", duplicacao_ok="ganho: diferencia de diabetes insípido (erro do relatório); o sh do GR2 cobra o mecanismo",
    extra="- Plasma osmolality ≈ 2 × Na + glucose/18 + urea/6<br>- Not diabetes insipidus: ADH works, but glucose holds water in the tubule"),
 sh(1791054008272, "verde", F_, "Tratamento: fluidos, insulina, K+", "8; 6", "Verde: conduta do caso (hidratação e insulina); viva no GR2."),
 # G — autoimunidade, complicações e cuidado (perguntas 8–12)
 sh(1791054010623, "verde", H_, "HLA-DR3/DR4", "9", "Verde: pergunta 8; viva no GR2."),
 sh(1791054009046, "verde", H_, "Anti-GAD", "9", "Verde: pergunta 8; viva no GR2."),
 sh(1791054009172, "azul", H_, "Síndrome poliglandular tipo 2", "9", "Azul: pergunta 8 (família com doenças autoimunes); viva no GR2."),
 sh(1791054018897, "verde", H_, "DM predispõe a infecção", "9", "Verde: pergunta 8; viva no GR2."),
 au("g-vias", ORG("Pathways by which <b>chronic hyperglycemia</b> damages tissues:<br>- advanced glycation end products (AGEs)<br>- {{c1::polyol}} pathway (sorbitol)<br>- {{c2::protein kinase C}} activation<br>- hexosamine pathway"),
    G(1, 2), H_, "Quatro vias de lesão", "9", "central", NAO, EP, "Verde: pergunta 9 (fisiopatologia molecular).",
    extra="- All converge on oxidative stress"),
 sh(1791054015322, "verde", H_, "Glicação não enzimática", "9", "Verde: pergunta 9; viva no GR2."),
 sh(1791054016196, "verde", H_, "Sorbitol e aldose redutase", "9", "Verde: pergunta 9; viva no GR2."),
 sh(1791054016847, "verde", H_, "Retinopatia: pericitos", "9", "Verde: pergunta 9; viva no GR2."),
 sh(1791054017972, "verde", H_, "Nefropatia: Kimmelstiel-Wilson", "9", "Verde: pergunta 9; viva no GR2."),
 sh(1791054016421, "verde", H_, "Neuropatia", "9", "Verde: pergunta 9; viva no GR2."),
 sh(1791054019147, "verde", H_, "IAM: principal causa de morte", "9", "Verde: pergunta 9; viva no GR2."),
 au("g-adesao", "To improve an adolescent's adherence to <b>insulin</b>, patient-centered care explores his {{c1::illness experience}} (shame, fear of being different) and agrees on goals with him",
    {1: Z}, H_, "MCP e adesão", "9", "central", NAO, EP, "Azul: pergunta 10.",
    extra="- Threats (blindness, amputation) made him shut down<br>- Discreet insulin pens and links to his sport can help"),
 au("g-exercicio", "A patient with <b>type 1 diabetes</b> who exercises should be warned about {{c1::hypoglycemia}} and may lower insulin or eat carbohydrate beforehand",
    {1: Z}, H_, "Atividade física", "9", "central", NAO, EP, "Azul: pergunta 11.",
    extra="- Carbohydrate counting lets him match insulin to each meal"),
 au("g-etica", "Blaming the mother harshly breaks the <b>Code of Medical Ethics</b> duty to treat patients and families with {{c1::civility}} and respect for their dignity",
    {1: R}, H_, "Ética da comunicação", "9", "lateral", NAO, EP, "Rosa: pergunta 12.",
    extra="- Article 23 of the Brazilian Code of Medical Ethics"),
]
SEM_IMAGEM = "fato clínico ou fisiológico sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {"ak-prerrenal": "- Here, dehydration from osmotic diuresis lowers renal perfusion", "ak-bun": "- Urea is reabsorbed with sodium and water when perfusion falls"}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if VERSO.get(k):
        c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Raciocinar o caso de DM1 em cetoacidose: definição e diagnóstico de DM, secreção e ações da insulina, transportadores de glicose e limiar renal, fisiopatologia da CAD (gasometria, desencadeantes, potássio, água), diferença com o DM2/EHH, autoimunidade, complicações crônicas e o cuidado centrado no adolescente.",
 "centrais": [
   ("caso", "a-caso"),
   ("DM e diagnóstico", "sh-1791054010222", "sh-1791054010997", "sh-1791054012847", "sh-1791054007644", "sh-1791054007769", "sh-1791054008396", "sh-1791054008544", "sh-1791054008670", "b-precoce"),
   ("insulina", "sh-1791647354296", "sh-1791729317165", "sh-1792027894938", "c-anabolica", "sh-1791054013222", "sh-1791054011246", "c-paracrina", "sh-1792027895739", "sh-1792027895991", "c-dependentes"),
   ("transportadores", "sh-1791054011372", "sh-1792027896339", "sh-1791647346120", "d-km", "d-tm", "d-limiar"),
   ("cetoacidose", "sh-1791054012018", "e-gasometria", "sh-1791054012198", "sh-1791054011545", "sh-1791054011671", "sh-1791729323438", "e-desencadeantes", "sh-1791054012447", "e-insulina-dm2", "sh-1791054012596"),
   ("água e eletrólitos", "ak-prerrenal", "ak-bun", "sh-1791054007900", "sh-1791054008019", "e-k-total", "sh-1791054008148", "sh-1791054012320", "f-osm", "sh-1791054008272"),
   ("complicações e cuidado", "sh-1791054010623", "sh-1791054009046", "sh-1791054009172", "sh-1791054018897", "g-vias", "sh-1791054015322", "sh-1791054016196", "sh-1791054016847", "sh-1791054017972", "sh-1791054016421", "sh-1791054019147", "g-adesao", "g-exercicio", "g-etica"),
 ],
 "exemplos": ["JSP, 15 anos", "impetigo → abscesso por S. pyogenes", "médico que culpou a mãe"],
 "outras_aulas": [("diabetes", "UC03 GR2"), ("ação hormonal", "UC03 Bioquímica 10"), ("integração metabólica", "UC03 Bioquímica 25 e 33")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
