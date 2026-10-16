# Especificação curada — Diagnóstico patológico: ferramentas do diagnóstico patológico (UC03 P1, Patologia; Prof. Luiz F. Ferraz da Silva; 31 lâminas).
# Ordem = slides. AnKing → externos → autoral SÓ para lacuna provada em busca/cobertura.tsv (gate duro), último do último caso.
# Modelo vivo: arquivos-trabalho/deck-aula-uc03-rd02-diagnostico-radiologico-v2-2026-10-16/spec.py (16/10).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 2  # 2 = busca também nos decks NEBLI vivos (gate duro)
PIPELINE = "anking-primeiro"  # F-20261015-CLAUDE-06: liga os gates duros (cobertura_anking, cores_rubrica, inducao_clozes); não remover
RUN_ID = "uc03-pt03-20261016a"
SHORT = "pt03"
LESSON = "2026-uc03-patologia-03-diagnostico-patologico"
DECK = "NEBLI::UC03::P1::Patologia::Diagnóstico patológico"
CRITERIOS = "EXECUCAO-DECK-AULA (passos 0–7, 16/10) + MEMORY §3/§5/§6/§8 + ANTI-EXEMPLARES, 16/10/2026"
MEDIA = {f"pt03-{n}.png": f"img/pt03-{n}.png" for n in ("he", "ihq")}
IMG = lambda n, w=420: f'<img src="pt03-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (16/10): seções de recurso do AnKing (busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt); "
         "significado em todos os acervos (busca/semantica.jsonl). ")
EXCLUIDOS = [
 (1486590976651, "Prussian blue para hemossiderina × lipofuscina: acúmulos, aula 11"),
 (1468605679141, "FISH (segunda nota): repete ak-fish"),
 (1496165476691, "tireoglobulina na IHQ: neoplasias; a aula usa só o PSA como exemplo"),
 (1475363999923, "padrões de imunofluorescência renal: nefrologia (clínica estreita)"),
 (1474253775264, "PAS e glicogenoses: repete ak-pas (mesma resposta)"),
 (1521264448683, "diastase com PAS: detalhe técnico além da aula"),
 (1500419413812, "Ziehl em Nocardia e Cryptosporidium: microbiologia; a aula só pede BAAR"),
 (1496165216576, "marcadores de IHQ (citoqueratina, vimentina, desmina, GFAP…): aula de neoplasias; aqui só o exemplo do PSA"),
 (1468250126050, "Kartagener e dineína: biologia celular; aqui só a ME como ferramenta"),
 (1532689568162, "PAAF em nódulo de tireoide (outras notas): clínica; entra só a nota HY"),
 (1500418458789, "Ziehl e carbol-fucsina: já vivo no GR3/micro; entra o compartilhado com micolato"),
]
FORA_DO_RECORTE = [
 "Aterosclerose e idades do infarto (lâminas 7, 9, 10): aulas próprias (hemostasia/infarto).",
 "Autópsia em detalhe (monobloco, SVOC, funções): aula 14 Declaração de óbito.",
 "Lista completa de colorações (Masson, Picro-Sirius, Verhoeff, Alcian blue, Fontana-Masson): o professor pediu para não decorar; ficam no Extra do PAS.",
]
A_, B_, C_, D_ = "A-modelo-da-doenca", "B-patologia-e-areas", "C-macroscopia-e-processamento", "D-ferramentas"

CARDS = [
 # ---------- A. Modelo da doença (lâminas 2–11) ----------
 au("au-sequencia-doenca", ORG("A <b>disease process</b> unfolds as:<br>1. {{c1::Etiology}} (cause)<br>2. {{c1::Pathogenesis}} (mechanism)<br>3. {{c2::Morphologic}} and functional changes<br>4. {{c2::Clinical}} manifestations"),
    "V-pilar", A_, "Etiologia → patogênese → alterações → manifestações", 3, "esquema da lâmina 3; Robbins cap. 1",
    extra="- Pathology studies structural, biochemical and functional changes, which are intertwined"),
 au("au-etiologia", "<b>Etiology</b>, the cause of a disease, can be {{c1::genetic::g…/a…}} or {{c1::acquired::g…/a…}}",
    "V-pilar", A_, "Etiologia: genética ou adquirida", 4, "lâmina 4; palavras-cruzadas",
    extra="- It can be single (pneumococcus → pneumonia) or multiple (diabetes: genes plus diet)<br>- An external cause, such as a microbe, is called an etiologic agent"),
 au("au-patogenese", "The {{c1::pathogenesis}} of a disease is the <b>mechanism</b> by which its cause produces it",
    "V-pilar", A_, "Patogênese = mecanismo", 5, "lâmina 5; palavras-cruzadas",
    extra="- Knowing it guides treatment: antipyretics act on inflammation, antibiotics do nothing against a viral flu<br>- Often used as a synonym of pathophysiology"),
 au("au-morfologia", "<b>Morphologic changes</b> show not only whether a disease is present but also its {{c1::grade}}",
    "A-aula", A_, "Alterações morfológicas definem presença e grau", 8, "lâmina 8",
    extra="- They are studied grossly, microscopically and ultrastructurally, and are usually the first way disease is detected"),
 # ---------- B. Patologia e suas áreas (lâminas 13–15) ----------
 au("au-patologia-geral", "<b>Pathology</b> is divided into {{c1::general}} pathology (cell injury, inflammation, neoplasia) and {{c1::systemic}} (organ) pathology",
    "A-aula", B_, "Patologia geral × de órgãos", 13, "lâmina 13; Robbins cap. 1",
    extra="- UC03 is general pathology: mechanisms that happen in any organ"),
 au("au-areas", ORG("Areas of <b>pathology</b> in patient care:<br>- {{c1::Autopsy}}<br>- {{c1::Surgical}} pathology<br>- {{c1::Cytopathology}}<br>- {{c2::Clinical}} pathology<br>- {{c2::Forensic}} pathology"),
    "A-aula", B_, "Cinco áreas da patologia", 14, "lâmina 14; apostila guia",
    extra="- Clinical pathology runs the laboratory tests; forensic pathology investigates external causes of death"),
 au("au-ferramentas", ORG("<b>Pathology tools</b>:<br>- {{c1::H&E}}: structure<br>- {{c2::Electron microscopy}}: ultrastructure<br>- {{c3::Histochemistry}}: dyes for specific substances<br>"
                          "- {{c4::Immunohistochemistry}}: antibodies to proteins<br>- {{c5::Molecular}} pathology: mutations"),
    "V-pilar", B_, "Ferramentas e o que cada uma mostra", 15, "lâmina 15; apostila guia cap. 2; palavras-cruzadas",
    extra="- They are complementary, and H&E is always the first one"),
 # ---------- C. Macroscopia e processamento (lâminas 16–21) ----------
 au("au-macroscopia", "<b>Surgical specimens</b> are usually fixed in {{c1::formalin}} before gross examination and sampling",
    "A-aula", C_, "Fixação em formol e representação", 16, "lâmina 16 e transcrição",
    extra="- Only representative pieces of the lesion go to histology: the whole organ cannot be sectioned"),
 au("au-processamento", ORG("<b>Tissue processing</b> for histology:<br>1. {{c1::Fixation}} in formalin<br>2. Embedding in {{c1::paraffin}}<br>3. Cutting on a {{c1::microtome}}<br>4. Staining"),
    "A-aula", C_, "Etapas do processamento", 18, "lâminas 17–19",
    extra="- Paraffin makes the tissue firm enough to cut slices a few micrometers thick"),
 ak("ak-faf", 1462228531057, "A-step", C_, "Punção aspirativa por agulha fina", 20, "lâminas 20–21 (punção guiada por US); palavras-cruzadas",
    extra="- FNA collects cells (cytopathology) without removing the lesion, often guided by ultrasound<br>- Cells are smeared as a monolayer; cervical scrapings use the Papanicolaou stain"),
 au("au-congelacao", "A quick <b>intraoperative</b> pathology diagnosis is made on a {{c1::frozen section}}",
    "R-detalhe", C_, "Exame intraoperatório por congelação", 20, "palavras-cruzadas da aula",
    extra="- The tissue is frozen instead of embedded in paraffin, so the answer comes during surgery"),
 # ---------- D. Ferramentas (lâminas 23–31) ----------
 au("au-he", "In <b>H&E</b>, hematoxylin stains the {{c1::nucleus::n…/c…}} purple and eosin stains the {{c1::cytoplasm::n…/c…}} pink",
    "V-pilar", D_, "HE: núcleo × citoplasma", 23, "lâmina 23; palavras-cruzadas",
    extra="- The first and main stain: fast and shows tissue architecture<br>" + IMG("he")),
 au("au-me", "{{c1::Electron microscopy}} diagnoses <b>primary ciliary dyskinesia</b> by showing defective cilia microtubules",
    "A-aula", D_, "ME e discinesia ciliar", 24, "lâmina 24 e transcrição",
    extra="- Few centers have it; tissue must be fixed in glutaraldehyde, so it is planned before the biopsy"),
 ak("ak-pas", 1475982859127, "A-step", D_, "PAS: glicogênio", 25, "lâmina 25 (membrana basal, muco) e transcrição (glicogênio)"),
 sh(1791576674292, "verde", D_, "Ziehl-Neelsen: micobactérias", 26, "HY 1; lâmina 26 (BAAR); nota viva do GR3 e da micro 26"),
 ak("ak-prata", 1500419514988, "A-step", D_, "Prata (Grocott) para fungos", 26, "lâmina 26 (Grocott)"),
 ak("ak-ferro", 1478834342914, "A-step", D_, "Prussian blue (Perls) para ferro", 27, "lâmina 27 (ferro)"),
 ak("ak-oilred", 1475982852075, "R-detalhe", D_, "Oil Red O para gordura", 27, "lâmina 27 (gordura)"),
 au("au-ihq", "<b>Immunohistochemistry</b> finds a specific protein in tissue with a primary antibody revealed by a labeled {{c1::secondary}} antibody",
    "V-pilar", D_, "Princípio da IHQ", 28, "lâmina 28; provas 2018 P4 e 2015 P3sub",
    extra="- The brown color comes from the DAB chromogen; it adds about 24 h to the report<br>- Where it stains (nucleus or membrane) also informs<br>" + IMG("ihq", 460)),
 ak("ak-ihq-tumor", 1496165181235, "A-aula", D_, "IHQ caracteriza tumores", 29, "transcrição (tipo e origem do câncer); provas 2018 P4 e 2015 P3sub"),
 ak("ak-psa", 1496165396128, "A-step", D_, "IHQ para PSA: origem prostática", 29, "exemplo da transcrição (adenocarcinoma de próstata); palavras-cruzadas (linhagem tumoral)"),
 au("au-if", "<b>Immunofluorescence</b> reveals antibodies with a fluorescent label and is widely used in {{c1::kidney}} and skin biopsies",
    "A-aula", D_, "Imunofluorescência", 30, "lâmina 30; palavras-cruzadas (pele e rim)",
    extra="- The background is dark, and several markers can be seen at once in different colors"),
 ak("ak-fish", 1468605672126, "A-step", D_, "FISH", 31, "hibridização in situ da lâmina 31"),
 au("au-molecular", "<b>Molecular tests</b> (PCR, FISH) find the tumor alteration that makes a patient eligible for {{c1::targeted}} therapy",
    "A-aula", D_, "Patologia molecular e terapia-alvo", 31, "lâmina 31; provas 2018 P4 e 2015 P3sub",
    extra="- The expensive drug only works if the tumor has the targeted receptor or mutation"),
]

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "conceito, área ou técnica sem estrutura a reconhecer; as imagens que ensinam estão nos cards de HE e IHQ (e nas fotos do AnKing)"
SLIDE_SEM_ALT = "imagem da própria lâmina da aula (HE de miocárdio, IHQ nuclear × de membrana), sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "pt03-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {
 "ak-pas": "- Also outlines basement membranes and mucus<br>- Other stains in the lesson (not to memorize): Masson trichrome and Picro-Sirius (collagen), Verhoeff (elastic fibers), Alcian blue (mucus), Fontana-Masson (melanin)",
 "ak-prata": "- Fungi turn black against the background",
 "ak-ferro": "- Iron deposits turn blue (e.g., hemosiderosis, hemochromatosis)",
 "ak-oilred": "- Fat dissolves in routine paraffin processing, so it needs frozen tissue",
"ak-ihq-tumor": "- Shows which protein each tumor cell expresses, so it defines type and origin",
 "ak-psa": "- Cells of each organ express their own proteins, so IHC tells where a tumor came from",
 "ak-fish": "- Shows extra gene copies or translocations directly on the cells",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"au-ferramentas": "ganho: aqui o nome sai da função na lista das ferramentas da lâmina 15; em ak-ihq-tumor, do uso em tumores"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "pt03-he.png": "Lâmina 23: miocárdio em HE (núcleos roxos, citoplasma rosa, infiltrado); verso do card de HE.",
 "pt03-ihq.png": "Lâmina 29: IHQ com marcação nuclear (esquerda) e de membrana (direita), DAB marrom; e-mail e logotipo cortados; verso do card de IHQ.",
}
REVISAO = {
 "despejo": "Despejo lido inteiro (23 notas da aula + compartilhado do Ziehl): frentes sem campo perdido, clozes certos, imagens de HE e IHQ nos versos certos, cores pela rubrica.",
 "corrigidos": ["au-processamento: verso trocado por um porquê (a parafina deixa cortar fatias finas)"],
}
ESCOPO = {
 "objetivo": "Entender o modelo da doença (etiologia, patogênese, alterações morfológicas, manifestações), as áreas da patologia e as ferramentas do diagnóstico patológico (macroscopia, processamento, HE, ME, histoquímica, IHQ, IF, molecular) e o que cada uma mostra.",
 "centrais": [
   ("modelo da doença", "au-sequencia-doenca", "au-etiologia", "au-patogenese", "au-morfologia"),
   ("patologia e ferramentas", "au-patologia-geral", "au-areas", "au-ferramentas", "au-macroscopia", "au-processamento", "ak-faf"),
   ("colorações e técnicas", "au-he", "au-me", "ak-pas", "sh-1791576674292", "ak-prata", "ak-ferro", "ak-oilred", "au-ihq", "ak-ihq-tumor", "ak-psa", "au-if", "ak-fish", "au-molecular"),
 ],
 "exemplos": ["pneumonia", "aterosclerose", "infarto", "discinesia ciliar", "adenocarcinoma de próstata"],
 "outras_aulas": [("aterosclerose e infarto", "69 Hemostasia, trombose, embolia e infarto"), ("autópsia e declaração de óbito", "14 Declaração de óbito"), ("acúmulos e pigmentos", "11 Acúmulos e adaptação")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
