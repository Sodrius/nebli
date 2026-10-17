# Especificação curada — Regulação hormonal do metabolismo e da massa corpórea (UC03 P1, Bioquímica; 62 lâminas, partes I e II).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing (seções FirstAid grelina, leptina, endocanabinoides, hipotálamo lateral e ventromedial, síndrome metabólica, análogos de GLP-1)
# → cópias vivas do GR2, da Integração metabólica e da UC08 por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06 (só notas do baralho AnKing)
    "_FirstAid_08_Endocrine_03_Physiology_13_Appetite_regulation_01_Ghrelin.txt",
    "_FirstAid_08_Endocrine_03_Physiology_13_Appetite_regulation_02_Leptin.txt",
    "_FirstAid_08_Endocrine_03_Physiology_13_Appetite_regulation_03_Endocannabinoids.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_02_Anatomy_and_Physiology_12_Hypothalamus_01_Lateral_nucleus.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_02_Anatomy_and_Physiology_12_Hypothalamus_02_Ventromedial_nucleus.txt",
    "_FirstAid_08_Endocrine_04_Pathology_15_Diabetes_mellitus_02_Chronic_Complications_Metabolic_Syndrome.txt",
    "_FirstAid_08_Endocrine_05_Pharm_01_Diabetes_mellitus_therapy_GLP_1_Analogs.txt",
]
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-bq16-20261017a"
SHORT = "bq16n"
LESSON = "2026-uc03-bioquimica-16-regulacao-hormonal-massa-corporea"
DECK = "NEBLI::UC03::P1::Bioquímica::Regulação hormonal e massa corpórea"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"bq16-{n}.png": f"img/bq16-{n}.png" for n in ("lipostatica", "ampk", "ob-leptina", "parabiose", "arqueado")}
IMG = lambda n, w=440: f'<img src="bq16-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (FirstAid regulação do apetite, hipotálamo, síndrome metabólica, GLP-1; "
         "busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt: AMPK, adiponectina, MC4R/POMC/NPY/AgRP, CCK, "
         "malonil-CoA, PFK-2, UCP-1, IMC, receptor de leptina, TNF/IL-6); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
_GR2 = "disfunção da célula β e tipos de diabetes: GR2 Diabetes (P2), fora das lâminas desta aula"
_FARM = "efeito adverso/indicação de antidiabético: farmacologia do diabetes, fora das lâminas"
EXCLUIDOS = [
 (1482022013033, "grelina aumenta o apetite: entra a cópia NEBLI viva (sh-1790979869860)"),
 (1462849442061, "GLP-1 e saciedade pelo esvaziamento gástrico: entra a cópia NEBLI viva (sh-1791052302525)"),
 (1584134136210, "adipocinas e resistência à insulina: entra a cópia NEBLI do GR2 (sh-1791054013396)"),
 (1584135730369, "gordura visceral e resistência à insulina: entra a cópia NEBLI do GR2 (sh-1791054012972)"),
 (1584133908547, _GR2), (1584133969374, _GR2 + " (há cópia viva no GR2)"), (1584134939832, _GR2 + " (há cópia viva no GR2)"),
 (1584135130853, "MODY: " + _GR2),
 (1500918912754, "repete ak-sm-criterios (mesmo mnemônico sem a lista)"),
 (1462849394748, "GLP-1: mais insulina e saciedade — entra a cópia NEBLI do GR2 (sh-1791054014570)"),
 (1462849434995, "repete ak-glp1-glucagon-esvaziamento (queda do glucagon)"),
 (1462849457192, _FARM), (1462849475077, _FARM), (1462849488980, _FARM),
]
FORA_DO_RECORTE = [
 "Eixo hipotálamo-hipófise, estresse (adrenalina/cortisol) e classificação das doenças endócrinas: aula 10 (Ação hormonal).",
 "Peptídeos intestinais além de GLP-1 e grelina (CCK, PYY, amilina): só citados na tabela da lâmina 29.",
 "Optogenética: técnica ilustrativa, no verso de au-arqueado.",
]
A_, B_, C_, D_, E_ = "A-homeostase-obesidade", "B-resistencia-insulina", "C-leptina-adipocinas", "D-apetite", "E-ampk"

CARDS = [
 # ---------- A. Homeostase e obesidade (lâminas 2–14) ----------
 au("au-lipostatica", "The <b>lipostatic theory</b> holds that {{c1::adipose tissue}} mass is kept constant by signals adjusting food intake and energy expenditure",
    "V-pilar", A_, "Teoria lipostática", 2, "lâminas 2, 11, 20 e 45; transcrição; Lehninger cap. 23",
    extra="- Leptin from fat cells is the main signal of the fat store<br>" + IMG("lipostatica", 380)),
 ak("ak-imc", 1543085033888, "A-aula", A_, "IMC ≥ 25 sobrepeso, ≥ 30 obesidade", 3, "lâmina 3 (tabela de IMC)"),
 ak("ak-lateral-fome", 1481418791050, "A-aula", A_, "Hipotálamo lateral = fome", 10, "lâmina 10; seção"),
 ak("ak-vmh-saciedade", 1481418777586, "A-aula", A_, "Hipotálamo ventromedial = saciedade", 10, "lâmina 10; seção"),
 ak("ak-endocanabinoides", 1462810116955, "R-detalhe", A_, "Endocanabinoides aumentam o apetite", 12, "lâmina 12 (recompensa); seção"),
 ak("ak-sm-riscos", 1584135569745, "A-aula", A_, "Síndrome metabólica: DCV, EHNA, DM2", 14, "lâmina 14 (doenças da obesidade); seção"),
 ak("ak-obesidade-ri", 1584133764526, "A-aula", A_, "Obesidade abdominal → resistência à insulina", 14, "lâminas 14–15; prova 2023 P1 2.2 (eco); seção"),
 # ---------- B. Resistência à insulina e síndrome metabólica (lâminas 15–18) ----------
 ak("ak-sm-criterios", 1500918912753, "A-step", B_, "Critérios da síndrome metabólica", 15, "lâmina 15; seção"),
 sh(1791054012972, "azul", B_, "Gordura visceral → resistência à insulina", 15, "lâmina 15; card do GR2"),
 ak("ak-sm-familia", 1584136093433, "R-detalhe", B_, "História familiar: risco não modificável", 15, "seção"),
 ak("ak-sm-x", 1584136164929, "R-detalhe", B_, "Síndrome X", 15, "seção"),
 sh(1791054012719, "azul", B_, "Hiperinsulinemia reduz receptores de insulina", 16, "lâmina 16; card da Integração metabólica/GR2"),
 ak("ak-tg-ffa-insulina", 1584134575365, "V-hy", B_, "TAG e AGL intracelulares inibem a sinalização da insulina", 16, "lâminas 16 e 18 (DAG, ceramida); seção"),
 sh(1791593465414, "azul", B_, "Macrófagos do tecido adiposo viram pró-inflamatórios", 17, "lâmina 17; card do GR2"),
 sh(1791593465568, "azul", B_, "TNF do tecido adiposo inflamado bloqueia a insulina", 17, "lâmina 17; prova 2025 P2 1.8 (eco); card do GR2"),
 sh(1791054013396, "azul", B_, "Adipocinas e resistência à insulina", 17, "lâmina 17; card do GR2"),
 sh(1791054013222, "azul", B_, "Fosforilação em serina do receptor de insulina", 18, "lâmina 18 (serina-quinases); card do GR2"),
 # ---------- C. Leptina e adipocinas (lâminas 20–28) ----------
 ak("ak-leptina", 1482022023195, "V-hy", C_, "Leptina: dos adipócitos, reduz o apetite", 20, "lâmina 20; seção"),
 au("au-ob", "<b>ob/ob mice</b> cannot make {{c1::leptin}}, so they become obese and lose weight when leptin is given",
    "V-pilar", C_, "Camundongo ob/ob", 22, "lâminas 22 e 52–53 (67 g → 35 g); transcrição; Lehninger",
    extra="- The OB gene encodes leptin<br>" + IMG("ob-leptina", 380)),
 au("au-db", "<b>db/db mice</b> lack the leptin {{c1::receptor}}, so they stay obese even with high leptin",
    "V-pilar", C_, "Camundongo db/db e parabiose", 24, "lâminas 23–24 e 54–56 (parabiose de Coleman)",
    extra="- In parabiosis, the db/db partner's excess leptin starves a normal or ob/ob mouse<br>" + IMG("parabiose", 420)),
 au("au-resistencia-leptina", "<b>Leptin treatment</b> fails in most obese humans, who already have high leptin and leptin {{c1::resistance}}",
    "V-prova", C_, "Resistência à leptina", 25, "lâminas 25 e 57; prova 2023 P1 2.3",
    extra="- Like insulin resistance; insulin resistance and inflammation impair leptin signaling"),
 ak("ak-leptina-obesos", 1578537123614, "V-prova", C_, "Obesos têm leptina alta", 25, "lâmina 25; prova 2023 P1 2.3; seção"),
 sh(1791647352594, "azul", C_, "Termogenina (UCP-1) na gordura marrom", 26, "lâmina 26 (leptina → simpático → UCP); card da Integração metabólica"),
 au("au-adiponectina", "<b>Adiponectin</b>, an adipose hormone, is lower in obesity and activates {{c1::AMPK}}, raising insulin sensitivity",
    "V-pilar", C_, "Adiponectina", 27, "lâminas 27–28 e 51; transcrição; Lehninger",
    extra="- TNF-α inhibits its production; its deficiency mimics type 2 diabetes"),
 ak("ak-pparg-adiponectina", 1462913323101, "A-step", C_, "Glitazonas aumentam a adiponectina", 27, "lâmina 27"),
 # ---------- D. Apetite (lâminas 29–38) ----------
 sh(1790979869860, "azul", D_, "Grelina aumenta o apetite", 29, "lâminas 29 e 31; card vivo"),
 sh(1791052302525, "azul", D_, "GLP-1 dá saciedade pelo esvaziamento gástrico", 29, "lâmina 29; card vivo"),
 sh(1791054014570, "verde", D_, "GLP-1: mais insulina e saciedade", 29, "lâminas 29 e 38; prova 2023 P1 2.3; card do GR2"),
 ak("ak-grelina-jejum", 1482022016433, "V-hy", D_, "Grelina sobe no jejum", 31, "lâmina 31; seção"),
 ak("ak-grelina-sono", 1462810025802, "R-detalhe", D_, "Privação de sono aumenta a grelina", 31, "seção"),
 ak("ak-leptina-sono", 1462810098191, "R-detalhe", D_, "Privação de sono reduz a leptina", 31, "seção"),
 ak("ak-prader", 1482022018540, "A-step", D_, "Prader-Willi: grelina alta", 31, "seção"),
 ak("ak-bypass", 1482022020682, "A-step", D_, "Grelina cai após bypass gástrico", 31, "seção"),
 au("au-arqueado", "<b>Leptin</b> activates arcuate POMC/CART neurons, whose α-MSH acts on {{c1::MC4R}} to cause satiety",
    "V-pilar", D_, "Leptina, POMC e MC4R", 32, "lâminas 32–35 e 59–61; transcrição; Lehninger",
    extra="- MC4R mutations are a known genetic cause of human obesity<br>- Circuits were mapped by optogenetics (light-gated channels in chosen neurons)<br>" + IMG("arqueado", 420)),
 ak("ak-pomc", 1461871709857, "A-step", D_, "POMC origina ACTH, MSH, β-endorfina", 32, "lâmina 32 (α-MSH vem da POMC)"),
 au("au-agrp", "<b>Ghrelin</b> activates arcuate {{c1::NPY/AgRP}} neurons, which inhibit satiety neurons and increase hunger",
    "A-aula", D_, "Grelina e NPY/AgRP", 32, "lâminas 32, 36 e 59; transcrição",
    extra="- AgRP blocks MC4R; leptin inhibits these neurons"),
 ak("ak-vmh-leptina", 1481418782211, "A-step", D_, "Ventromedial estimulado pela leptina", 33, "lâmina 33; seção"),
 ak("ak-lateral-leptina", 1481418798641, "A-step", D_, "Leptina inibe o hipotálamo lateral", 33, "lâmina 33; seção"),
 ak("ak-glp1-exemplos", 1462849387815, "A-aula", D_, "Exenatida, liraglutida, semaglutida", 38, "lâmina 38 (Ozempic, Wegovy); seção"),
 ak("ak-glp1-glucagon-esvaziamento", 1462849402751, "A-step", D_, "GLP-1: menos glucagon e esvaziamento lento", 38, "lâmina 38; seção"),
 # ---------- E. AMPK (lâminas 48–50) ----------
 au("au-ampk", "<b>AMPK</b>, activated by a high {{c1::AMP}}/ATP ratio, switches on ATP-producing pathways and off biosynthesis",
    "V-pilar", E_, "AMPK, sensor de energia", 48, "lâminas 48–50; transcrição; Lehninger",
    extra="- It phosphorylates and inhibits acetyl-CoA carboxylase, so less malonyl-CoA allows fatty acid oxidation<br>"
          "- It activates PFK-2, raising fructose-2,6-bisphosphate and glycolysis<br>" + IMG("ampk", 380)),
 ak("ak-metformina-ampk", 1462913225002, "A-step", E_, "Metformina ativa AMPK", 48, "lâmina 48"),
 ak("ak-acc", 1475894369854, "A-aula", E_, "ACC: enzima limitante da síntese de ácidos graxos", 49, "lâmina 49"),
 sh(1791729319038, "azul", E_, "Malonil-CoA inibe a CAT-1", 49, "lâmina 49; card da Integração metabólica"),
 ak("ak-pfk2", 1474164770942, "A-step", E_, "PFK-2 produz frutose-2,6-bisfosfato", 50, "lâmina 50"),
 sh(1791647347495, "azul", E_, "PFK-2/F2,6BPase: enzima bifuncional", 50, "lâmina 50; card da Integração metabólica"),
 sh(1791647347996, "azul", E_, "PFK-1 ativada por AMP e F2,6BP", 50, "lâmina 50; card da Integração metabólica"),
 ak("ak-lateral-lesao", 1481418794101, "A-step", D_, "Lesão do lateral → anorexia", 62, "lâmina 62; seção"),
 ak("ak-vmh-lesao", 1481418779919, "A-step", D_, "Lesão do ventromedial → hiperfagia", 62, "lâmina 62; seção"),
 ak("ak-lateral-grelina", 1481418796366, "A-step", D_, "Grelina estimula o hipotálamo lateral", 62, "lâmina 62; seção"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak-imc": "- BMI = weight / height²",
 "ak-lateral-fome": "- Ghrelin stimulates it and leptin inhibits it",
 "ak-vmh-saciedade": "- Leptin stimulates it",
 "ak-endocanabinoides": "- Food also stimulates reward pathways",
 "ak-sm-riscos": "- Obesity raises coronary disease, diabetes, hypertension, cancer, sleep apnea and osteoarthritis",
 "ak-obesidade-ri": "- Excess triglyceride leads to insulin resistance in liver, muscle and vessels",
 "ak-sm-criterios": "- Obesity, glucose, blood pressure, triglycerides and low HDL",
 "ak-sm-familia": "- Genes and environment both contribute",
 "ak-sm-x": "- Its core is insulin resistance",
 "ak-tg-ffa-insulina": "- Diacylglycerol and ceramide activate serine kinases that block the insulin receptor",
 "ak-leptina": "- Its levels follow fat mass",
 "ak-leptina-obesos": "- They are leptin resistant, not leptin deficient",
 "ak-pparg-adiponectina": "- Adiponectin also stimulates fatty acid oxidation through AMPK",
  "ak-grelina-jejum": "- Ghrelin falls after eating while leptin rises",
 "ak-grelina-sono": "- Short sleep favors hunger",
 "ak-leptina-sono": "- Short sleep favors hunger",
 "ak-prader": "- Hyperphagia and obesity",
 "ak-bypass": "- One reason appetite drops after surgery",
 "ak-pomc": "- α-MSH from arcuate POMC neurons signals satiety",
 "ak-vmh-leptina": "- Leptin acts on the arcuate nucleus and its hypothalamic targets",
 "ak-lateral-leptina": "- Leptin inhibits NPY/AgRP neurons",
 "ak-glp1-exemplos": "- Ozempic and Wegovy are semaglutide",
 "ak-glp1-glucagon-esvaziamento": "- They reduce appetite and cravings",
 "ak-metformina-ampk": "- AMPK is the cell's energy sensor",
 "ak-acc": "- AMPK phosphorylates and inhibits it",
 "ak-pfk2": "- AMPK activates PFK-2",
 "ak-lateral-lesao": "- The lateral area drives hunger",
 "ak-vmh-lesao": "- The ventromedial area drives satiety",
 "ak-lateral-grelina": "- Ghrelin comes from the stomach in fasting",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (lipostática, ob/ob, parabiose, arqueado, AMPK) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula (Lehninger, Coleman, Nature Reviews), sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "bq16-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {"au-ob": "ganho: o experimento do camundongo sem leptina (ob/ob) que emagrece com leptina; ak-leptina só diz quem secreta e o efeito", "au-resistencia-leptina": "ganho: por que a leptina não trata o obeso (resistência); ak-leptina-obesos só diz que a leptina é alta"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "bq16-lipostatica.png": "Lâmina 20: teoria lipostática — tecido adiposo, leptina, ingestão e oxidação; verso de au-lipostatica.",
 "bq16-ampk.png": "Lâmina 48: AMPK ativada por AMP/LKB1, inibe vias de síntese e ativa as que geram ATP; verso de au-ampk.",
 "bq16-ob-leptina.png": "Lâmina 53: camundongo ob/ob 67 g × ob/ob tratado com leptina 35 g; verso de au-ob.",
 "bq16-parabiose.png": "Lâmina 56: resultados da parabiose de Coleman (db/db, ob/ob, selvagem); verso de au-db.",
 "bq16-arqueado.png": "Lâmina 60: neurônios NPY/AgRP × POMC/CART, α-MSH no MC4R, receptor de leptina; verso de au-arqueado.",
}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (37 notas novas, 43 cards; frentes, clozes, versos, imagens e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Explicar a teoria lipostática, como leptina, adiponectina, grelina e GLP-1 regulam o apetite e o metabolismo, os circuitos "
             "do núcleo arqueado, a resistência à leptina e à insulina na obesidade e a AMPK como sensor de energia.",
 "centrais": [
   ("lipostática", "au-lipostatica", "ak-leptina"),
   ("leptina", "au-ob", "au-db"),
   ("resistência à leptina", "au-resistencia-leptina", "ak-leptina-obesos"),
   ("adipocinas", "au-adiponectina", "ak-pparg-adiponectina"),
   ("apetite", "au-arqueado", "au-agrp"),
   ("energia", "au-ampk", "ak-acc", "ak-pfk2"),
 ],
 "exemplos": ["ob/ob tratado com leptina", "parabiose de Coleman", "Ozempic", "optogenética"],
 "outras_aulas": [("eixo neuroendócrino e estresse", "10 Ação hormonal"), ("resistência à insulina", "GR2 Diabetes (sh)"),
                  ("glicólise e lipogênese", "25/33 Integração metabólica (sh)"), ("grelina e GLP-1 no TGI", "UC08 (sh)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
