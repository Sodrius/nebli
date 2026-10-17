# Especificação curada — Grand Round 4: Paracoccidioidomicose (UC03 P3; 67 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = lâminas. Todo o AnKing de PCM (5 seções de recurso, as mesmas 10 notas) já tem cópia NEBLI viva na 50 Micoses sistêmicas
# (e o dimorfismo na 43) → entra por sh(); granuloma (Inflamação granulomatosa, Lesão celular, Ativação de linfócitos T), prata
# (Diagnóstico patológico) e mecanismo dos antifúngicos (43, Antibióticos) também por sh(). Autoral SÓ para lacuna provada
# (busca/cobertura.tsv): o que o caso e a radiologia ensinam e o AnKing não tem.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ("Grand Round de caso: o AnKing de PCM (10 notas) já entra inteiro por cópias NEBLI; o que sobra são achados do caso e da "
                   "radiologia sem nenhum card em AnKing, externos ou NEBLI vivo (busca/anking.txt: butterfly, moriform, immunodiffusion, "
                   "adrenal+paracocc, TMP-SMX+fungo, lymphoma+mimic sem PCM; busca/semantica.jsonl), por isso 8 autorais em 33 cards")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-gr53-20261017a"
SHORT = "gr53n"
LESSON = "2026-uc03-grand-round-04-paracoccidioidomicose"
DECK = "NEBLI::UC03::P3::Grand Round::Grand Round 4 (paracoccidioidomicose)"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"gr53-{n}.jpg": f"img/gr53-{n}.jpg" for n in ("tc-mediastino", "padroes")}
IMG = lambda n, w=460: f'<img src="gr53-{n}.jpg" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (Paracoccidioides em Bootcamp, FirstAid, Physeo, Pixorize, SketchyMicro; "
         "antifúngicos, sulfonamidas e granuloma para conferir cópias; busca/secoes); palavra-chave em AnKing e Referências Externas "
         "(busca/anking.txt: paracoccidioid, lymphoma, mulberry/moriform, butterfly, TMP-SMX, immunodiffusion, adrenal, Grocott, ergosterol, "
         "glucan synthase, PABA, caseous); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
_C50 = "entra a cópia NEBLI viva da 50 Micoses sistêmicas (sh-{})"
EXCLUIDOS = [
 (1499975610400, _C50.format(1791630902842)), (1499975827249, _C50.format(1791630904467)),
 (1499976133630, "entra a cópia NEBLI viva da 43 Biologia dos fungos (sh-1791557944405)"),
 (1499976239948, _C50.format(1792176892756)), (1499976310064, _C50.format(1791630903143)),
 (1499976355327, _C50.format(1791630903892)), (1499976536055, _C50.format(1791630904294)),
 (1499976619643, _C50.format(1791630904067)), (1499976865408, _C50.format(1791630905091)),
 (1499976938219, _C50.format(1791630905219)),
]
FORA_DO_RECORTE = [
 "Histórico (Lutz 1908, Splendore, Almeida, Negroni, Lacaz, Medellín 1971): só ilustração; o dimorfismo térmico entra.",
 "Topografia digestiva, pele polimorfa e neuroparacoccidioidomicose (lâminas 43–45): detalhe clínico sem cobrança em prova.",
 "Exames laboratoriais e sorologias do caso: dados do paciente, sem conceito próprio.",
 "Toxicidades e doses dos antifúngicos: farmacologia clínica (aula 43 e farmacologia).",
]
A_, B_, C_, D_, E_ = "A-caso", "B-anatomopatologico", "C-agente-imunidade", "D-clinica-radiologia", "E-tratamento"

CARDS = [
 # ---------- A. O caso: forma aguda/juvenil (lâminas 2–25) ----------
 sh(1792065187180, "verde", A_, "Formas aguda/juvenil × crônica do adulto", 2, "V-pilar: menino de 6 anos com linfonodos (lâminas 2–9, 41); card da 50"),
 sh(1791630903892, "azul", A_, "Linfadenopatia cervical, axilar e inguinal", 3, "A-aula: lâminas 3, 4 e 8; card da 50"),
 au("au-linfoma", "In children, <b>juvenile paracoccidioidomycosis</b> with fever and generalized lymphadenopathy is often mistaken for {{c1::lymphoma}}",
    "V-pilar", A_, "PCM juvenil simula linfoma", 6, "lâminas 5–6 (imprint sugestivo de linfoma não Hodgkin, quimioterapia iniciada)",
    extra="- The case: a 6-year-old boy with 2 months of fever and enlarged nodes, sent home as flu, dengue, sinusitis and pneumonia<br>"
          "- Review of the biopsy showed granulomas full of yeasts"),
 sh(1791630902842, "azul", A_, "PCM endêmica da América do Sul", 7, "A-aula: lâmina 7 (zona periurbana); card da 50"),
 au("au-necrose", "On CT, <b>juvenile paracoccidioidomycosis</b> shows conglomerate lymph nodes with central {{c1::necrosis}}",
    "A-aula", A_, "Linfonodos necróticos na forma juvenil", 19, "lâminas 16, 19, 23 e 50 (TC de tórax e abdome; forma infanto-juvenil)",
    extra="- Mediastinal, hilar, axillary and abdominal nodes, with hepatosplenomegaly<br>"
          "- Lung lesions are rare in the juvenile form; lytic bone lesions may occur<br>" + IMG("tc-mediastino")),
 sh(1791630905219, "azul", A_, "Disseminada: anfotericina B", 25, "A-aula: lâmina 25 (anfotericina B pela gravidade); card da 50"),
 # ---------- B. Anatomopatológico (lâminas 28–31) ----------
 sh(1791716404503, "verde", B_, "Granuloma: histiócitos epitelioides", 28, "V-prova: lâmina 28; prova 2024 P3 2.7 (PCM forma granuloma); card da Inflamação granulomatosa"),
 sh(1791910088374, "azul", B_, "Granuloma caseoso", 28, "A-aula: lâmina 28 (necrose caseosa); card da Inflamação granulomatosa"),
 sh(1792117378746, "azul", B_, "Necrose caseosa em TB e fungos", 28, "A-aula: lâmina 28; card da Lesão celular"),
 sh(1792150762061, "azul", B_, "Prata (Grocott) cora fungos", 30, "A-aula: lâminas 30–31 e 40; card do Diagnóstico patológico"),
 sh(1792176892756, "azul", B_, "Levedura maior que a hemácia", 30, "A-aula: lâmina 30 (ampla variação de tamanho); card da 50"),
 sh(1791630904467, "verde", B_, "Gemulação múltipla em roda de leme", 31, "V-prova: lâmina 31; prova 2015 P2 29.2 (exame direto); card da 50"),
 # ---------- C. Agente e imunidade (lâminas 33–36) ----------
 sh(1791557944405, "azul", C_, "PCM é dimórfica", 33, "A-aula: lâmina 33 (Negroni, dimorfismo térmico); card da 43"),
 sh(1791630903143, "azul", C_, "Inalação de conídios", 35, "A-aula: lâminas 35 e 38; card da 50"),
 sh(1791744812583, "azul", C_, "Bolor inalado, levedura no tecido", 35, "A-aula: lâmina 35; card da 50"),
 sh(1791630908545, "azul", C_, "Estradiol bloqueia a transição bolor → levedura", 35, "A-aula: lâmina 35; apostila UC3; card da 50"),
 sh(1792083296387, "verde", C_, "Proteção pela imunidade celular", 36, "V-prova: lâmina 36; prova 2024 P3 2.7; card da 50"),
 sh(1791625436658, "verde", C_, "Th1 e IFN-γ formam o granuloma", 36, "V-prova: prova 2024 P3 2.7 (IFN-γ ativa macrófagos e forma granuloma); card da Ativação de linfócitos T"),
 # ---------- D. Clínica e radiologia (lâminas 38–60) ----------
 sh(1791630904294, "azul", D_, "Pulmão → linfonodos → granulomas", 38, "A-aula: lâmina 38 (porta de entrada); card da 50"),
 au("au-dissociacao", "In <b>chronic pulmonary paracoccidioidomycosis</b>, extensive radiographic lesions with few symptoms are called clinical-radiological {{c1::dissociation}}",
    "A-aula", D_, "Dissociação clínico-radiológica", 38, "lâminas 38 e 60",
    extra="- Hypoxemia and an obstructive pattern are common<br>- Treatment improves the X-ray but not lung function (fibrosis)"),
 sh(1791630904067, "azul", D_, "Úlceras de mucosa oral e respiratória", 42, "A-aula: lâmina 42; card da 50"),
 au("au-moriforme", "The oral lesion of <b>paracoccidioidomycosis</b> is a slow ulcer with a finely granular base called {{c1::moriform stomatitis}}",
    "A-aula", D_, "Estomatite moriforme", 42, "lâmina 42",
    extra="- Very suggestive, though not pathognomonic<br>- The periodontium is rich in fungi; teeth may loosen<br>- Hoarseness and dysphagia when larynx and pharynx are involved"),
 sh(1791557944155, "azul", D_, "Endêmicos: bolor no solo, levedura no corpo", 48, "A-aula: lâmina 48 (endêmicos em indivíduos saudáveis); card da 43"),
 sh(1792170501780, "azul", D_, "Oportunistas no imunocomprometido", 48, "A-aula: lâmina 48 (Aspergillus, Candida, Cryptococcus, Pneumocystis); card da 43"),
 au("au-borboleta", "On chest X-ray, <b>chronic paracoccidioidomycosis</b> gives bilateral, symmetric central infiltrates in a {{c1::butterfly-wing}} pattern",
    "A-aula", D_, "Asa de borboleta no RX", 52, "lâminas 52, 53 e 60",
    extra="- Middle third of the lungs, posterior; on CT diffuse, middle and lower fields<br>"
          "- Patterns: pneumonic, nodular, interstitial, fibrotic or mixed<br>" + IMG("padroes")),
 au("au-adrenal", "In Brazil, <b>paracoccidioidomycosis</b>, like tuberculosis, can destroy the {{c1::adrenal glands}} and cause Addison disease",
    "A-aula", D_, "Adrenais acometidas", 60, "lâmina 60 (pneumopatia com lesões mucocutâneas, laringe/traqueia e adrenais)",
    extra="- Suspect it when diffuse lung disease coexists with mucocutaneous and laryngeal lesions"),
 # ---------- E. Tratamento e cura (lâminas 63–67) ----------
 sh(1791630905091, "azul", E_, "PCM local: azol", 63, "A-aula: lâminas 63 e 65 (itraconazol); card da 50"),
 sh(1791557942007, "azul", E_, "Equinocandinas: glucana-sintase", 63, "A-aula: lâmina 63; card da 43"),
 sh(1792170505829, "azul", E_, "Flucitosina: síntese de DNA/RNA", 63, "A-aula: lâmina 63; card da 43"),
 sh(1791557942183, "azul", E_, "Polienos ligam ergosterol e formam poros", 64, "A-aula: lâmina 64 (anfotericina B); card da 43"),
 sh(1792170504428, "azul", E_, "Azóis inibem a 14α-desmetilase", 65, "A-aula: lâmina 65 (a lâmina atribui ao itraconazol a glucana-sintase; o alvo correto é a 14α-desmetilase); card da 43"),
 au("au-sulfa", "Besides itraconazole, <b>paracoccidioidomycosis</b> can be treated with {{c1::sulfamethoxazole-trimethoprim}}, which blocks fungal folate synthesis",
    "A-aula", E_, "Sulfa na PCM", 66, "lâmina 66 (sulfamídicos); monitoria e apostila (tratamento)",
    extra="- Amphotericin B is reserved for severe disseminated disease, as in the case"),
 sh(1791668523238, "azul", E_, "SMX: análogo do PABA", 66, "A-aula: lâmina 66 (inibição competitiva do PABA); card dos Antibióticos"),
 au("au-cura", "Cure of <b>paracoccidioidomycosis</b> needs clinical, mycological, radiological and immunological criteria, the last by negative double {{c1::immunodiffusion}}",
    "A-aula", E_, "Critérios de cura", 67, "lâmina 67",
    extra="- Immunological: negative titers, or stable low titers<br>- Radiological: opacities become linear (scarring)<br>- Mycological: negative direct exam of sputum"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (TC dos linfonodos necróticos, padrões do RX) estão nos cards do conceito"
SLIDE_SEM_ALT = "imagem do próprio caso ou da série da preceptoria de radiologia, sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "gr53-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "gr53-tc-mediastino.jpg": "Lâmina 18: TC de tórax com contraste do caso, massas linfonodais mediastinais com áreas hipodensas; verso de au-necrose.",
 "gr53-padroes.jpg": "Lâmina 53: quatro RX da forma crônica (pneumônico, nodular, intersticial, fibrótico), centrais e simétricos; verso de au-borboleta.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Reconhecer a forma aguda/juvenil da PCM (linfonodos necróticos que simulam linfoma), o diagnóstico anatomopatológico "
             "(granuloma, Grocott, roda de leme), a imunidade celular que forma o granuloma, a clínica e a radiologia da forma crônica e "
             "o tratamento com seus mecanismos e critérios de cura.",
 "centrais": [
   ("forma juvenil", "sh-1792065187180", "au-linfoma", "au-necrose"),
   ("anatomopatológico", "sh-1791716404503", "sh-1791630904467"),
   ("imunidade", "sh-1792083296387", "sh-1791625436658"),
 ],
 "exemplos": ["menino de 6 anos de Guarulhos", "menino de 14 anos com PCM tratada aos 5", "Adolpho Lutz 1908"],
 "outras_aulas": [("micoses sistêmicas", "50 Micoses sistêmicas (sh)"), ("mecanismo dos antifúngicos", "43 Biologia dos fungos (sh)"),
                  ("granuloma", "Inflamação granulomatosa (sh)"), ("sulfonamidas", "Antibióticos e resistência (sh)"),
                  ("ncRNAs do P. brasiliensis (prova 2024 P3 2.8)", "54 RNAs não codificadores")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
