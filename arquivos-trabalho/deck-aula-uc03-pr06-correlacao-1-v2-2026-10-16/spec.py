# Especificação curada — Correlação patológica-radiológica 1 (UC03 P1, Patologia + Radiologia; 43 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing → associados das aulas 02, 04, 23, 24 e 19 por sh() → autoral SÓ para lacuna provada em busca/cobertura.tsv (gate duro).
# Aula de correlação: ler a imagem e ligá-la à peça e à lâmina; a física e os termos ficam nas aulas de radiologia (sh).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06: todo AnKing do conteúdo entra
    "_FirstAid_15_Repro_39_Testicular_tumors_Seminoma.txt",
    "_FirstAid_16_Respiratory_24_Pneumonia_Lobar.txt",
    "_FirstAid_16_Respiratory_25_Natural_history_lobar_Red_Hepatization.txt",
]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"  # F-20261015-CLAUDE-06: liga os gates duros (cobertura_anking, cores_rubrica, inducao_clozes); não remover
RUN_ID = "uc03-pr06-20261016a"
SHORT = "pr06"
LESSON = "2026-uc03-patologia-radiologia-06-correlacao-1"
DECK = "NEBLI::UC03::P1::Patologia::Correlação patológica-radiológica 1"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 16/10/2026"
_IMGS = ("rx-consolidacao", "rx-menisco", "us-derrame", "rx-lobo-inferior", "tc-bolhas", "us-nodulo")
MEDIA = {f"pr06-{n}.png": f"img/pr06-{n}.png" for n in _IMGS}
IMG = lambda n, w=420: f'<img src="pr06-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (16/10): seções de recurso do AnKing (FirstAid seminoma, pneumonia lobar e história natural; busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt: enfisema, bolha, antracose, pneumonia lobar, broncograma, derrame, "
         "exsudato, empiema, silhueta, seminoma, tumor testicular, orquiectomia, atelectasia); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
# Cards da 04 (silhueta, átrio direito, duas incidências, enfisema no RX, hemitórax opaco), associados depois de a 04 estar instalada (16/10).
RD04 = {"SILHUETA": None, "ATRIO": None, "DUAS": None, "ENFISEMA": None, "HEMITORAX": None}
EXCLUIDOS = [
 (1473548504699, "seção FirstAid pneumonia lobar: Klebsiella por aspiração é microbiologia (aula de bactérias)"),
 (1473548512472, "seção FirstAid: escarro em geleia de groselha da Klebsiella já existe em cópia NEBLI da microbiologia (1791763664220)"),
 (1791763664220, "cópia NEBLI do card da Klebsiella (microbiologia); fora desta correlação"),
 (1473548517793, "seção FirstAid: abscesso por Klebsiella é microbiologia"),
 (1474503845229, "seção FirstAid: sopro brônquico e egofonia são semiologia do exame físico, não imagem nem peça"),
 (1474503849368, "seção FirstAid: estertores são semiologia"),
 (1474503853594, "seção FirstAid: macicez à percussão é semiologia"),
 (1474503857395, "seção FirstAid: frêmito aumentado é semiologia"),
 (1524151971478, "seção história natural: pergunta da composição repete ak-hep-vermelha"),
 (1524151749002, "fase de congestão por composição do exsudato: repete ak-pn-congestao"),
 (1524152032953, "hepatização cinzenta por composição do exsudato: repete ak-hep-cinzenta"),
 (1496181891349, "diafragma retificado na DPOC: repete ak-enf-rx"),
 (1473627994933, "enfisema panacinar por deficiência de α1-antitripsina: o caso é de tabagista (centroacinar); α1AT fica para pulmão/genética"),
 (1473627946233, "perda de recuo elástico: fisiologia respiratória, não correlação de imagem"),
 (1473359817001, "tórax em tonel: repete ak-enf-rx (diâmetro AP aumentado)"),
 (1527620356647, "imagem de pneumonia do lobo médio (externo): repete ak-pn-rx (AnKing, mesma imagem de lobo médio)"),
 (1576691167062, "broncograma aéreo na insuficiência cardíaca: outra doença"),
 (1555364449472, "toracocentese como próximo passo: conduta clínica"),
 (1553817132878, "critérios de derrame parapneumônico complicado (pH, glicose): conduta, acima do caso"),
 (1474503812564, "macicez no derrame: semiologia"),
 (1474503805629, "murmúrio diminuído no derrame: semiologia"),
 (1463188002544, "disgerminoma equivale ao seminoma: tumor de ovário, outra aula"),
 (1557170257567, "tabela de marcadores seminoma × não seminoma: repete ak-marcadores-seminoma"),
 (1589285885939, "criptorquidia e câncer testicular: repete ak-criptorquidia"),
 (1463340099569, "tumor germinativo misto: além do caso (seminoma puro)"),
 (1535325668811, "Doppler na torção testicular: urologia; a aula usa o Doppler para a lesão"),
 (1584556086271, "torção com ecotextura heterogênea: urologia"),
 (1561067734495, "MCAT: definição de TC, aula 05"),
 (1463339978379, "Klinefelter como fator de risco de tumor testicular: o Robbins (cap. 21) diz que Klinefelter eleva o tumor germinativo do mediastino, não do testículo; criptorquidia fica em ak-criptorquidia"),
]
FORA_DO_RECORTE = [
 "Roteiro ABCDE de leitura do RX e anatomia dos hilos (lâminas 4 e 7): sem fato a decorar.",
 "Semiologia (macicez, frêmito, sopro brônquico, egofonia): aula de semiologia; a correlação é imagem × peça × lâmina.",
 "Cavitação tuberculosa (prova 2025 P3): aulas de micobactérias e Grand Round 3.",
 "Torção testicular e Doppler de simetria (apostila UC3): urologia.",
 "Fisiologia da DPOC (complacência, CRF, DLCO): aulas de fisiologia respiratória.",
]
A_, B_, C_, D_, E_, F_, G_ = ("A-leitura-rx", "B-enfisema", "C-pneumonia-imagem", "D-derrame", "E-silhueta", "F-pneumonia-patologia", "G-testiculo")

CARDS = [
 # ---------- Caso 1 e leitura do RX (lâminas 2–7) ----------
 ak("ak-enf-tabaco", 1473627980218, "V-prova", B_, "Tabagismo é a principal causa de enfisema", 2, "caso 1 (tabagista 30 anos-maço); prova 2015 P1sub 3.6 (pneumonia secundária ao enfisema)"),
 ak("ak-febre-consolidacao", 1543669837575, "A-step", C_, "Febre + tosse + consolidação = pneumonia", 2, "caso 1 (tosse produtiva e febre há 3 dias)"),
 # ---------- B. Enfisema: RX, TC, peça, histologia (lâminas 8–16) ----------
 ak("ak-enf-rx", 1473628054935, "V-prova", B_, "Enfisema no RX: diâmetro AP e diafragma retificado", 8, "lâmina 8 (RX de 6 meses atrás); Grande Resumo (hiperinsuflação, retificação)"),
 ak("ak-enf-lucencia", 1473628062986, "A-step", B_, "Enfisema no RX: hipertransparência", 8, "lâmina 8; prova 2015 P1sub (descrever áreas pelo termo)",
    extra_add="- More air and less tissue attenuate fewer X-rays, so the lungs look darker"),
 au("au-bolhas-tc", "In a smoker's chest <b>CT</b>, thin-walled, air-filled spaces larger than 1 cm are emphysematous {{c1::bullae}}",
    "A-aula", B_, "Bolhas enfisematosas na TC", 9, "lâmina 9; Grande Resumo P1 p. 52 (áreas hipoatenuantes = bolhas enfisematosas)",
    extra="- On CT they are hypoattenuating (air), with no visible wall vessels<br>- They come from destroyed alveolar walls; rupture causes pneumothorax<br>" + IMG("tc-bolhas", 380)),
 sh(1791593313366, "rosa", B_, "Diâmetro AP aumentado na TC do fumante", 9, "lâmina 9 (TC do tabagista); card da correlação 2"),
 sh(1791592721894, "azul", B_, "Antracose", 10, "lâmina 10 (pulmão negro); Grande Resumo (deposição de carbono); card da patologia ambiental"),
 ak("ak-enf-destruicao", 1473627940622, "V-hy", B_, "Enfisema: destruição dos sacos alveolares", 11, "lâminas 11 e 15 (peça e histologia)"),
 ak("ak-enf-protease", 1473627957778, "A-step", B_, "Enfisema: desequilíbrio protease-antiprotease", 11, "Grande Resumo (destruição alveolar por processos inflamatórios); Robbins"),
 ak("ak-bolha-pneumotorax", 1473733383452, "A-step", B_, "Bolha rompida → pneumotórax secundário", 12, "lâmina 12 (bolhas subpleurais); Grande Resumo (estouro das bolhas → ar entre as pleuras)"),
 ak("ak-enf-centriacinar", 1473627988643, "V-pilar", B_, "Tabagismo → enfisema centroacinar nos lobos superiores", 13, "lâminas 12–13 (bolhas apicais); caso 1"),
 ak("ak-enf-aumento", 1473627929151, "A-step", B_, "Enfisema: espaços aéreos aumentados", 15, "lâminas 14–15 (histologia normal × enfisema)"),
 ak("ak-enf-neutrofilos", 1473627965295, "R-detalhe", B_, "Neutrófilos e macrófagos liberam proteases", 15, "par de ak-enf-protease (mecanismo da destruição)"),
 # ---------- C. Pneumonia na imagem (lâminas 17–18) ----------
 au("au-consolidacao", "On a chest radiograph, a white lung area where <b>alveolar air</b> was replaced by exudate is a {{c1::consolidation}}",
    "V-prova", C_, "Consolidação", 17, "lâmina 17; provas 2024 P2 1.4 e 2019 P1 1.10 (descrever a opacidade/condensação)",
    extra="- In Portuguese exams: condensação or opacidade; air bronchograms may show inside it<br>- Here: pneumonia in the left mid and lower lung<br>" + IMG("rx-consolidacao", 300)),
 ak("ak-pn-rx", 1555363662790, "A-step", C_, "RX de pneumonia (lobo médio)", 17, "lâmina 17 (reconhecer a pneumonia no RX); figura AnKing com broncograma aéreo"),
 sh(1792141774459, "azul", C_, "RX de tórax diagnostica pneumonia", 17, "lâmina 17; card da 02"),
 au("au-costofrenico", "The earliest radiographic sign of a <b>pleural effusion</b> is blunting of the {{c1::costophrenic}} angle",
    "A-aula", D_, "Velamento do seio costofrênico", 18, "lâminas 18 e 24 (RX atual × 6 meses atrás); Grande Resumo (opacidade na região do seio costofrênico); apostila guia",
    extra="- Fluid settles first in the lowest point of the pleural space, the lateral and posterior costophrenic recesses<br>- Lateral films show smaller amounts than PA"),
 # ---------- D. Derrame pleural (lâminas 19–23) ----------
 au("au-us-derrame", "On ultrasound, a <b>pleural effusion</b> appears as an {{c1::anechoic}} collection above the diaphragm",
    "A-aula", D_, "Derrame ao US", 19, "lâmina 19; Grande Resumo (substância escura, anecoica, entre pulmão e diafragma)",
    extra="- Simple fluid reflects no echoes; septations or debris suggest exudate or empyema<br>- US also guides the needle for thoracentesis<br>" + IMG("us-derrame", 360)),
 ak("ak-traqueia-derrame", 1474503822233, "A-step", D_, "Derrame grande empurra a traqueia para o outro lado", 20, "lâmina 20 (TC: derrame grande à esquerda); apostila guia (derrame direciona coração e traqueia ao lado oposto)"),
 ak("ak-traqueia-atelectasia", 1474503841320, "A-step", D_, "Atelectasia puxa a traqueia", 20, "apostila guia (atelectasia × derrame × pneumonia no hemitórax opaco)",
    extra_add="- Pneumonia alone does not shift the trachea or heart"),
 ak("ak-parapneumonico", 1534592594457, "A-step", D_, "Derrame parapneumônico não complicado: exsudato estéril", 21, "lâmina 21 (neutrófilos no líquido); prova 2017 P1 3.1 (derrame com Klebsiella)"),
 sh(1791577164590, "azul", D_, "Empiema: pus no espaço pleural", 21, "lâmina 21; card das aulas 23 e 38"),
 sh(1791141194538, "azul", D_, "Exsudato: proteína alta", 21, "lâmina 21 (derrame inflamatório); card da 23"),
 sh(1791592954543, "rosa", D_, "Exsudato: razão proteína pleural/sérica > 0,5", 21, "card da 23"),
 sh(1791169089006, "azul", D_, "Exsudato: permeabilidade (malignidade, pneumonia)", 21, "lâminas 21–22 (pneumonia e câncer no mesmo derrame); card da 23"),
 sh(1791780346752, "rosa", D_, "Pus: exsudato purulento", 21, "lâmina 21; card da 38"),
 ak("ak-adenoca-derrame", 1473733237107, "A-step", D_, "Adenocarcinoma de pulmão → derrame pleural", 22, "lâmina 22 (grupos de células de adenocarcinoma); Grande Resumo (células neoplásicas agrupadas)"),
 ak("ak-derrame-maligno", 1557352878027, "A-step", D_, "Derrame maligno é exsudativo", 22, "lâmina 22"),
 ak("ak-derrame-hemorragico", 1555365315648, "R-detalhe", D_, "Derrame hemorrágico: malignidade ou TEP", 22, "par de ak-derrame-maligno"),
 au("au-menisco", "<b>Pleural fluid</b> climbing the lateral chest wall with a concave upper border forms the {{c1::meniscus}} sign",
    "A-aula", D_, "Sinal do menisco", 23, "lâmina 23 (título); Grande Resumo (sinal do menisco); apostila guia (forma de menisco ou U)",
    extra="- Surface tension and lung recoil pull the fluid up along the wall<br>- It marks a free effusion on an upright PA film<br>" + IMG("rx-menisco", 220)),
 ak("ak-derrame-rx", 1555365775573, "A-step", D_, "RX de derrame pleural", 23, "lâmina 23; figura AnKing de derrame à esquerda com menisco",
    extra_add="- Note the concave upper border (meniscus) and the lost left costophrenic angle"),
 sh(1791577166763, "rosa", D_, "Derrame = edema em cavidade", 23, "lâmina 23; card da 23"),
 # ---------- E. Silhueta (lâminas 25–28) ----------
 ak("ak-lingula", 1474511892721, "R-detalhe", E_, "Língula é do pulmão esquerdo", 26, "lâmina 26 (lobos e língula)",
    extra_add="- The lingula touches the left heart border, so its consolidation erases that border"),
 au("au-lobo-inferior", "A <b>left lower lobe</b> consolidation spares the heart border but erases the left {{c1::hemidiaphragm}} contour",
    "A-aula", E_, "Lobo inferior esquerdo apaga o diafragma", 28, "lâminas 27–28 (língula × lobo inferior); apostila UC3 p. 24; Grande Resumo (sinal da silhueta)",
    extra="- The lower lobe lies behind the heart and on the diaphragm; the lateral view confirms it<br>" + IMG("rx-lobo-inferior", 420)),
 # ---------- F. Pneumonia lobar: peça e histologia (lâminas 29–31) ----------
 ak("ak-pn-lobar", 1473548430236, "V-hy", F_, "Pneumonia lobar: consolidação de um lobo inteiro", 29, "lâmina 29 (peça); seção FirstAid"),
 ak("ak-hep-cinzenta", 1473548472722, "V-pilar", F_, "Hepatização cinzenta", 29, "lâmina 29 (peça acinzentada); seção FirstAid"),
 ak("ak-pn-congestao", 1473548457637, "A-step", F_, "Congestão: primeira fase", 30, "lâmina 30 (alvéolos congestos); seção FirstAid"),
 ak("ak-hep-vermelha", 1473548462128, "V-pilar", F_, "Hepatização vermelha", 30, "lâmina 30; seção FirstAid"),
 ak("ak-pn-resolucao", 1473548476620, "A-step", F_, "Resolução por pneumócitos II", 30, "fase final (Robbins); seção FirstAid"),
 ak("ak-pn-exsudato", 1473548436921, "V-hy", F_, "Exsudato neutrofílico intra-alveolar", 31, "lâmina 31; Grande Resumo (neutrófilos)"),
 ak("ak-pn-agente", 1473548445520, "V-hy", F_, "Agentes: pneumococo e Klebsiella", 31, "seção FirstAid; prova 2017 P1 3.1 (Klebsiella no derrame)"),
 ak("ak-broncopneumonia", 1473548523852, "R-detalhe", F_, "Broncopneumonia: focos em torno dos bronquíolos", 31, "contraste com a lobar (Robbins)"),
 sh(1791592724520, "rosa", F_, "Biomassa predispõe a pneumonia", 31, "prova 2025 P2 4.3 (biomassa e pneumonia); card da patologia ambiental"),
 # ---------- G. Caso 2: testículo (lâminas 32–41) ----------
 ak("ak-tumor-transiluminacao", 1463339928621, "V-hy", G_, "Tumor testicular: massa firme que não transilumina", 32, "caso 2 (aumento testicular há 6 meses, sem trauma nem febre)"),
 ak("ak-gct-classe", 1463339968803, "V-hy", G_, "> 95% dos tumores testiculares são germinativos", 32, "caso 2"),
 ak("ak-criptorquidia", 1463334097647, "V-hy", G_, "Criptorquidia → tumor germinativo (seminoma)", 32, "fator de risco do caso 2"),
 au("au-us-nodulo", "A solid {{c1::hypoechoic}} nodule inside the <b>testis</b> of a young man suggests a germ cell tumor",
    "V-pilar", G_, "Nódulo testicular hipoecoico", 35, "lâminas 33–36 (testículo normal homogêneo, nódulo, Doppler); apostila UC3 p. 24 (heterogeneidade nodular)",
    extra="- The normal testis is homogeneous; color Doppler shows flow inside the nodule, so it is solid tissue<br>- Next: tumor markers, chest X-ray and inguinal orchiectomy<br>" + IMG("us-nodulo", 360)),
 ak("ak-seminoma-comum", 1463339972200, "V-hy", G_, "Seminoma é o tumor testicular mais comum", 37, "lâmina 37; seção FirstAid"),
 ak("ak-seminoma-macro", 1463339998840, "V-hy", G_, "Seminoma: massa homogênea sem hemorragia nem necrose", 38, "lâminas 37–38 (peça); seção FirstAid"),
 ak("ak-seminoma-histo", 1463339990695, "V-hy", G_, "Seminoma: células claras em ovo frito", 40, "lâminas 39–40 (túbulos normais × seminoma); seção FirstAid",
    extra_add="- Fibrous septa with lymphocytes separate the sheets of tumor cells"),
 ak("ak-metastase-pulmao", 1557143263003, "V-prova", G_, "Jovem com nódulos pulmonares e dor lombar: tumor testicular", 41, "lâmina 41 (por que RX de tórax?); Grande Resumo (rastrear metástases)"),
 ak("ak-retroperitoneo", 1521738561049, "A-step", G_, "Metástase para linfonodos retroperitoneais", 41, "lâmina 41; Robbins (disseminação linfática para para-aórticos)",
    extra_add="- Testicular lymph drains to para-aortic nodes, following the gonadal vessels from their embryonic origin"),
 ak("ak-seminoma-prognostico", 1463339983674, "V-hy", G_, "Seminoma: radiossensível, metástase tardia, bom prognóstico", 41, "lâmina 41; seção FirstAid"),
 ak("ak-nao-seminoma", 1463339987206, "A-step", G_, "Não seminoma: metástase precoce", 41, "par do anterior"),
 ak("ak-orquiectomia", 1505849451028, "A-step", G_, "Conduta: orquiectomia radical inguinal", 41, "lâmina 41 (e agora?)"),
 ak("ak-marcadores-seminoma", 1494965833255, "A-step", G_, "Seminoma: AFP e β-hCG normais", 41, "marcadores pedidos com o RX (Robbins)"),
 ak("ak-plap", 1463340008364, "R-detalhe", G_, "Seminoma: PLAP elevada", 41, "seção FirstAid"),
 ak("ak-hcg-seminoma", 1463340004334, "R-detalhe", G_, "Seminoma raramente eleva hCG", 41, "seção FirstAid"),
]
_SH04 = [("SILHUETA", "verde", E_, "Sinal da silhueta", 25, "lâminas 25 e 27 (título; língula apaga a borda esquerda); card da 04"),
         ("ATRIO", "azul", A_, "Átrio direito forma a borda direita", 5, "lâmina 5 (PA anotado); card da 04"),
         ("DUAS", "azul", A_, "PA e perfil", 6, "lâminas 6 e 27 (perfil localiza a opacidade); card da 04"),
         ("ENFISEMA", "azul", B_, "RX do enfisema (costelas, transparência)", 8, "lâmina 8; card da 04"),
         ("HEMITORAX", "azul", D_, "Hemitórax opaco", 20, "lâmina 20 (pulmão colapsado ao lado do derrame); card da 04")]
for _k, _c, _b, _a, _s, _m in _SH04:
    if RD04[_k]:
        CARDS.append(sh(RD04[_k], _c, _b, _a, _s, _m))
CARDS.append(sh(1792141774955, "verde", C_, "Termos de cada método (radiopaco, hiperatenuante)", 17, "prova 2015 P1sub 3.1 (nome das áreas mais brancas); card da 02"))

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (TC com bolhas, consolidação, menisco, US do derrame, lobo inferior, nódulo testicular, RX AnKing) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula, sem equivalente nos acervos (busca sem acerto para o conceito)"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "pr06-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {  # chave: "- linha curta" para nota de acervo sem Extra útil
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "pr06-tc-bolhas.png": "Lâmina 9: TC de tórax sem contraste, janela de pulmão, com muitas bolhas de paredes finas; verso de au-bolhas-tc.",
 "pr06-rx-consolidacao.png": "Lâmina 17: RX PA na entrada do PS com opacidade no campo médio/inferior esquerdo (seta); verso de au-consolidacao.",
 "pr06-us-derrame.png": "Lâmina 19: US do hemitórax com coleção anecoica acima do diafragma; verso de au-us-derrame.",
 "pr06-rx-menisco.png": "Lâmina 23: RX com derrame subindo pela parede lateral em forma de menisco; verso de au-menisco.",
 "pr06-rx-lobo-inferior.png": "Lâmina 28: PA e perfil com opacidade do lobo inferior esquerdo (setas azuis), borda cardíaca preservada; verso de au-lobo-inferior.",
 "pr06-us-nodulo.png": "Lâmina 35: US testicular com nódulo hipoecoico intratesticular delimitado por cursores; verso de au-us-nodulo.",
 "1fbc5c2e2909a72d787b7008104b1ad9.webp": "AnKing: RX PA com pneumonia do lobo médio (consolidação com broncograma); frente de ak-pn-rx.",
 "30b08626f09679318efc307a232d9265.jpg": "AnKing: RX PA com grande derrame à esquerda, borda superior côncava e seio costofrênico apagado; frente de ak-derrame-rx.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Correlacionar imagem, peça e lâmina em dois casos: tabagista com enfisema que desenvolve pneumonia lobar com derrame pleural "
             "(parapneumônico e com células de adenocarcinoma) e jovem com seminoma testicular, usando os sinais radiológicos (silhueta, menisco).",
 "centrais": [
   ("enfisema", "ak-enf-centriacinar", "ak-enf-destruicao", "ak-enf-rx", "au-bolhas-tc"),
   ("pneumonia lobar", "au-consolidacao", "ak-hep-vermelha", "ak-hep-cinzenta", "ak-pn-exsudato"),
   ("derrame pleural", "au-menisco", "au-us-derrame", "ak-parapneumonico", "ak-derrame-maligno"),
   ("seminoma", "au-us-nodulo", "ak-seminoma-macro", "ak-seminoma-histo", "ak-metastase-pulmao"),
 ],
 "exemplos": ["enfisema do tabagista", "pneumonia da língula", "derrame parapneumônico", "derrame maligno", "seminoma"],
 "outras_aulas": [("termos, incidências, silhueta, atenuação", "02 e 04 (sh)"), ("antracose, biomassa", "24 Patologia ambiental (sh)"),
                  ("exsudato, transudato, derrame", "23 Edema e congestão (sh)"), ("tuberculose cavitária", "micobactérias e GR3")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
