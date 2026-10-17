# Especificação curada — Mecanismos efetores do sistema imune (UC03 P1, Imunologia; 64 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing (seções FirstAid burst respiratório, NK, macrófagos, neutrófilos, fagocitose, interação macrófago-linfócito, IFN-γ)
# → 23 notas vivas desta aula (22 antiga) e outras cópias vivas por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [
    "_FirstAid_02_Immunology_03_Immune_Responses_07_Respiratory_burst_Basics_base.txt",
    "_FirstAid_02_Immunology_02_Cellular_Components_05_Functions_of_natural_killer_cells_base.txt",
    "_FirstAid_10_Hematology_and_Oncology_02_Anatomy_12_Natural_killer_cells_base.txt",
    "_FirstAid_02_Immunology_02_Cellular_Components_08_Macrophage_lymphocyte_interaction_base.txt",
    "_FirstAid_10_Hematology_and_Oncology_02_Anatomy_06_Macrophages_Basics_base.txt",
    "_FirstAid_04_Pathology_02_Inflammation_05_Leukocyte_extravasation_Phagocytosis_base.txt",
    "_FirstAid_10_Hematology_and_Oncology_02_Anatomy_02_Neutrophils_Basics_base.txt",
    "_FirstAid_02_Immunology_03_Immune_Responses_06_Important_cytokines_03_From_Th1_cells_Secreted_By_Th1_IFN_y_base.txt",
]
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-im22-20261017a"
SHORT = "im22n"
LESSON = "2026-uc03-imunologia-22-mecanismos-efetores"
DECK = "NEBLI::UC03::P1::Imunologia::Mecanismos efetores imunes"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"im22-{n}.png": f"img/im22-{n}.png" for n in ("mo-subtipos", "mo-reg")}
IMG = lambda n, w=420: f'<img src="im22-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (FirstAid burst, NK, macrófagos, neutrófilos, fagocitose, IFN-γ; busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
# Vaga da 08 (ainda não instalada): preencher com a cópia NEBLI de 1487642714884 (burst respiratório usa O2 e NADPH oxidase).
IM08 = {"BURST": None}
_V = "entra a cópia NEBLI viva"
EXCLUIDOS = [(n, f"{a}: {_V}") for n, a in [
 (1487117308213, "NK: perforina e granzimas"), (1487117310594, "IFN α/β ativam NK"), (1487117314403, "NK mata célula sem MHC I"),
 (1487117328797, "IgG media ADCC"), (1487116849895, "sinal 2 B7/CD28"), (1487117002637, "CD40 do linfócito B"),
 (1489970364081, "IFN-γ ativa macrófagos"), (1520300810177, "CD40L/CD40"), (1489970456186, "IFN-γ de NK e Th1"),
 (1497451553581, "IFN-γ induz iNOS"), (1487642718524, "HClO, produto final do burst"), (1487642722079, "NADPH oxidase"),
 (1487642730357, "mieloperoxidase"), (1487642661164, "fagossomo e fagolisossomo"), (1479267358567, "neutrófilo na inflamação aguda"),
 (1487639081947, "edema e neutrófilos"), (1487640104877, "LTB4"), (1487642652400, "quimiotáticos de neutrófilo"),
 (1487642782702, "lactoferrina"), (1487642795725, "IL-8 dos macrófagos"), (1479267390511, "monócito → macrófago"),
 (1479267395454, "macrófagos fagocitam"), (1487640028986, "CD14/TLR4"), (1487642816623, "inflamação crônica"),
 (1489970091921, "IL-8"), (1489970137869, "IL-12"), (1489970181312, "TNF-α"), (1520716108281, "M1"), (1520717070355, "M2")]] + [
 (1489970516941, "IFN-γ aumenta MHC II: aula 20 (cópia viva lá)"),
 (1489970247629, "TNF mantém o granuloma: aula 47 Inflamação granulomatosa (cópia viva lá)"),
 (1520299562982, "via do NF-κB a partir dos PRR: aula 08 (Reconhecimento inato)"),
 (1487642714884, "burst respiratório: instalado pela aula 08 — entra a cópia dela (vaga IM08)"),
 (1487642780676, "piocianina da Pseudomonas: microbiologia, fora das lâminas"),
 (1520301002174, "influxo de K+ no burst: detalhe fora das lâminas"),
 (1578537487044, "sinalização das citocinas por tirosina-quinases não receptoras: detalhe fora das lâminas"),
 (1489971140322, "CCR5 no HIV: aula de infecção viral"),
]
FORA_DO_RECORTE = [
 "Lâminas 2–12: reconhecimento inato (TLR, NOD, inflamassoma) — aula 08; aqui só as notas vivas desta aula.",
 "Mediadores da inflamação e migração leucocitária em detalhe: aulas 37/38.",
 "Apresentação de antígenos e ativação T: aula 20; memória e contração: aulas 07 e 45.",
]
A_, B_, C_, D_, E_, F_ = "A-reconhecimento", "B-celulas-citocinas", "C-fagocitose-burst", "D-nk-adcc", "E-macrofagos", "F-linfocitos-t"

CARDS = [
 # ---------- A. Reconhecimento (lâminas 3–11) ----------
 sh(1791780342851, "azul", A_, "PRR ativados por PAMP e DAMP", 3, "lâminas 3 e 5; card desta aula"),
 sh(1791743339358, "azul", A_, "CD14 é correceptor do TLR4 para LPS", 8, "lâminas 8 e 15; card desta aula"),
 sh(1791743339740, "azul", A_, "Inflamassoma reconhece células mortas e micróbios", 11, "lâmina 11; card desta aula"),
 sh(1791743339860, "azul", A_, "Inflamassoma aumenta IL-1β e IL-18", 11, "lâmina 11; card desta aula"),
 # ---------- B. Células e citocinas (lâminas 13–22) ----------
 ak("ak-il1", 1489970022577, "A-step", B_, "Macrófagos secretam IL-1", 13, "lâmina 13; seção"),
 ak("ak-il6", 1489970054827, "A-step", B_, "Macrófagos secretam IL-6", 13, "lâmina 13; seção"),
 sh(1791780360378, "azul", B_, "Macrófagos secretam IL-8", 13, "card vivo"),
 sh(1791625433782, "azul", B_, "Macrófagos secretam IL-12", 13, "lâminas 13 e 46; card vivo"),
 sh(1791743347685, "azul", B_, "TNF-α dos macrófagos: caquexia e choque", 13, "lâmina 13; card vivo"),
 ak("ak-neutrofilo-comum", 1479267349398, "A-step", B_, "Neutrófilo é o leucócito mais comum", 14, "lâminas 14 e 30; seção"),
 sh(1791780342036, "verde", B_, "Neutrófilo domina a inflamação aguda", 14, "lâmina 14; card vivo"),
 ak("ak-neutrofilo-bacteria", 1479267366025, "A-aula", B_, "Neutrófilos sobem nas infecções bacterianas", 14, "lâmina 14; seção"),
 ak("ak-neutrofilo-imagem", 1479267369344, "A-step", B_, "Neutrófilo (imagem)", 14, "lâmina 14 (fotos das células); seção"),
 ak("ak-neutrofilo-fagocita", 1479267372624, "A-step", B_, "Neutrófilos são fagócitos", 14, "lâminas 14 e 31; seção"),
 sh(1791780359733, "azul", B_, "Quimiotáticos de neutrófilo: IL-8, C5a, LTB4", 16, "lâminas 16–17 e 31; prova 2015 P1 1.4; card vivo"),
 sh(1791743347807, "azul", B_, "IL-8 dos macrófagos recruta neutrófilos", 16, "card vivo"),
 sh(1791780360504, "azul", B_, "LTB4 atrai neutrófilos", 17, "lâmina 17; card vivo"),
 sh(1791780341641, "azul", B_, "Inflamação aguda: edema e neutrófilos", 20, "lâminas 20–21; prova 2024 P1 2.11; card vivo"),
 sh(1791023299492, "azul", B_, "Paneth secretam lisozima e defensinas", 22, "lâmina 22 (peptídeos antimicrobianos); card vivo"),
 sh(1791647814494, "rosa", B_, "Lactoferrina quela ferro", 22, "lâmina 22 (secreções); card desta aula"),
 # ---------- C. Fagocitose e burst (lâminas 23–33) ----------
 ak("ak-fagocitose", 1487642657848, "A-aula", C_, "Após extravasar, leucócitos fagocitam", 23, "lâmina 23; seção"),
 sh(1791780361129, "azul", C_, "Pseudópodos formam o fagossomo", 23, "lâmina 23; card vivo"),
 sh(1791629595447, "azul", C_, "IgG na cápsula: fagocitose por FcR", 24, "lâminas 24–25; card da 49"),
 sh(1791667096988, "verde", C_, "C3b e IgG são as opsoninas", 26, "lâminas 26–27; provas 2017 P1 4.3 e 2015 P1 2.3; card desta aula"),
 sh(1791780361432, "verde", C_, "NADPH oxidase: O2 → superóxido", 28, "lâmina 28; card desta aula"),
 ak("ak-sod", 1487642726245, "V-hy", C_, "Superóxido dismutase: O2− → H2O2", 28, "lâmina 28; seção"),
 sh(1791780361607, "verde", C_, "Mieloperoxidase: H2O2 → HClO", 28, "lâminas 28 e 32; prova 2015 P1 1.4; card desta aula"),
 sh(1791780361781, "azul", C_, "HClO é o produto final do burst", 28, "lâmina 28; card vivo"),
 ak("ak-o2-independente", 1487642775452, "R-detalhe", C_, "Morte independente de O2 é menos eficaz", 28, "seção"),
 sh(1791743343884, "azul", C_, "DGC: defeito da NADPH oxidase", 28, "card desta aula"),
 sh(1791625430456, "azul", C_, "NOS: arginina → citrulina + NO", 29, "lâmina 29; card desta aula"),
 sh(1791780362080, "verde", C_, "NO + superóxido → peroxinitrito", 29, "lâmina 29; card desta aula"),
 sh(1791625430632, "azul", C_, "IFN-γ induz iNOS", 29, "lâmina 29; card desta aula"),
 sh(1791743344060, "verde", C_, "NETs: redes de cromatina com antimicrobianos", 33, "lâmina 33; prova 2015 P1 1.4; card da 37"),
 # ---------- D. NK e ADCC (lâminas 34–37) ----------
 sh(1791629596121, "verde", D_, "ADCC: NK pelo FcγRIII (CD16)", 34, "lâmina 34; provas 2017 P1 4.3 e 2015 P2 2.6; card desta aula"),
 ak("ak-nk-cd16", 1487117321802, "A-step", D_, "NK mata via CD16 e Fc da IgG", 34, "lâmina 34; seção"),
 sh(1791629595996, "azul", D_, "IgG media ADCC", 34, "lâmina 34; card da 49"),
 ak("ak-nk-inata", 1487117304665, "V-hy", D_, "NK é linfócito da imunidade inata", 35, "lâmina 35; prova 2024 P1 2.11; seção"),
 ak("ak-nk-cd56", 1489971106127, "A-aula", D_, "NK: CD16 e CD56", 35, "lâmina 35; seção"),
 sh(1791625433908, "azul", D_, "IFN-γ vem de NK e Th1", 35, "lâmina 35; card vivo"),
 ak("ak-nk-il2-il12", 1487117312582, "A-step", D_, "IL-2 e IL-12 ativam NK", 35, "seção"),
 sh(1791984891204, "azul", D_, "IFN α/β ativam NK", 35, "card vivo"),
 sh(1791984891454, "verde", D_, "NK mata célula sem MHC I", 36, "lâmina 36; prova 2015 P2 7.2; card desta aula"),
 ak("ak-nk-tumor", 1518053116398, "A-aula", D_, "Tumor que perde MHC I é morto pela NK", 36, "lâmina 36; prova 2015 P2 7.2; seção"),
 ak("ak-ifn-antitumor", 1497203002753, "A-step", D_, "Interferons ativam NK e CD8 contra tumor", 36, "seção"),
 sh(1791984891827, "verde", D_, "NK: perforina e granzimas → apoptose", 37, "lâmina 37; prova 2015 P2 2.6; card desta aula"),
 # ---------- E. Macrófagos (lâminas 38–43) ----------
 sh(1791716410077, "azul", E_, "Macrófagos vêm dos monócitos", 38, "lâmina 38; card vivo"),
 au("au-residente", "Most <b>tissue-resident macrophages</b> derive from embryonic precursors and {{c1::self-renew}} locally, unlike monocyte-derived inflammatory macrophages",
    "A-aula", E_, "Macrófagos residentes × inflamatórios", 39, "lâminas 38–39; transcrição (residentes vindos do saco vitelino)",
    extra="- Names by tissue: Kupffer cells, microglia, alveolar macrophages, osteoclasts, histiocytes, mesangial cells<br>" + IMG("mo-subtipos", 400)),
 sh(1791743341958, "azul", E_, "Macrófagos fagocitam bactérias, debris, hemácias", 39, "card vivo"),
 ak("ak-macrofago-tardio", 1487642786172, "A-aula", E_, "Macrófagos predominam após 2–3 dias", 39, "seção"),
 ak("ak-lisozima", 1487642791049, "A-step", E_, "Lisozima do macrófago", 39, "seção"),
 ak("ak-cd14", 1523410787293, "R-detalhe", E_, "CD14 marca a linhagem monócito-macrófago", 39, "seção"),
 sh(1791983679757, "azul", E_, "Inflamação crônica: macrófagos, linfócitos, plasmócitos", 39, "card vivo"),
 sh(1791625434032, "verde", E_, "Macrófago M1 pelo Th1", 40, "lâmina 40; card desta aula"),
 sh(1791625430208, "verde", E_, "IFN-γ ativa macrófagos a matar", 40, "lâminas 40 e 52; prova 2016 P2 3.2; card vivo"),
 sh(1791625434457, "verde", E_, "Macrófago M2 pelo Th2", 41, "lâminas 41 e 62; card desta aula"),
 au("au-mreg", "<b>Regulatory macrophages</b>, induced by IL-10 from regulatory T cells, have {{c1::anti-inflammatory}} activity",
    "A-aula", E_, "Macrófago regulador", 42, "lâmina 42; transcrição",
    extra="- Immune complexes, prostaglandins, glucocorticoids and apoptotic cells also induce them<br>" + IMG("mo-reg", 400)),
 ak("ak-cd40l", 1489970973404, "A-step", E_, "CD40L nos linfócitos T auxiliares", 43, "lâminas 43 e 52; seção"),
 sh(1791625430082, "azul", E_, "CD40L/CD40 reforça macrófago-linfócito", 43, "card vivo"),
 sh(1791625431258, "azul", E_, "B precisa de CD40/CD40L", 43, "card vivo"),
 sh(1791625428533, "azul", E_, "Sinal 2: B7/CD28", 43, "card vivo"),
 # ---------- F. Linfócitos T (lâminas 45–64) ----------
 sh(1791625425207, "verde", F_, "T naive recircula nos linfonodos; efetor vai ao tecido", 45, "lâminas 45–48; card desta aula"),
 sh(1791625432733, "azul", F_, "Th17 induzido por IL-1, IL-6 e TGF-β", 50, "lâminas 50 e 55; card desta aula"),
 sh(1791625429957, "verde", F_, "CD8 mata células infectadas, tumorais e enxerto", 51, "lâminas 51 e 64; prova 2017 P2 2.9; card vivo"),
 sh(1791625422657, "verde", F_, "Th1 ativa macrófagos e CTL", 53, "lâminas 53 e 61; card vivo"),
 sh(1791625431758, "azul", F_, "Th1 secreta IFN-γ e IL-2", 53, "card vivo"),
 sh(1791625432007, "azul", F_, "Th2 recruta eosinófilos", 54, "lâmina 54; card vivo"),
 sh(1791625432133, "azul", F_, "Th2 promove IgE", 54, "lâmina 54; card vivo"),
 sh(1791625422039, "verde", F_, "Th17 recruta neutrófilos contra extracelulares", 55, "lâmina 55; card desta aula"),
 sh(1791743340332, "azul", F_, "Dectina-1 reconhece β-glucanos dos fungos", 56, "lâmina 56; card da 37"),
 sh(1792175043737, "azul", F_, "Defeito de IL-17: candidíase mucocutânea", 56, "lâmina 56 (Th17 contra Candida); card da 44"),
 sh(1791593462592, "verde", F_, "CTL: perforinas e granzimas", 57, "lâminas 57–58; prova 2015 P2 2.7; card vivo"),
 sh(1791625430882, "azul", F_, "CTL: FasL/Fas", 58, "lâmina 58; card vivo"),
 sh(1791625421906, "azul", F_, "Mesmo patógeno: doença localizada ou disseminada pelo Th", 63, "lâmina 63 (leishmaniose); card da 45"),
 sh(1791625425933, "verde", F_, "Hanseníase tuberculoide: Th1", 63, "lâmina 63; card desta aula"),
 sh(1791625426108, "verde", F_, "Hanseníase virchowiana: Th2", 63, "lâmina 63; card desta aula"),
]
_IM08 = [("BURST", "verde", C_, "Burst respiratório usa O2 e NADPH oxidase", 28, "lâmina 28; card da 08")]
for _k, _c, _b, _a, _s, _m in _IM08:
    if IM08[_k]:
        CARDS.append(sh(IM08[_k], _c, _b, _a, _s, _m))

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak-il1": "- IL-1 causes fever and acts on endothelium",
 "ak-il6": "- IL-6 drives fever and acute-phase proteins",
 "ak-neutrofilo-comum": "- Made in the bone marrow, they circulate looking for invaders",
 "ak-neutrofilo-bacteria": "- Dead neutrophils that killed microbes form pus",
 "ak-neutrofilo-imagem": "- Multilobed nucleus",
 "ak-neutrofilo-fagocita": "- They kill with the oxidative burst and NETs",
 "ak-fagocitose": "- The phagosome fuses with lysosomes to kill the microbe",
 "ak-sod": "- Then myeloperoxidase turns H2O2 into hypochlorous acid",
 "ak-o2-independente": "- Lysozyme, lactoferrin and defensins act without oxygen",
 "ak-nk-cd16": "- Antibody bridges the NK cell to the target, an innate cell using an adaptive molecule",
 "ak-nk-inata": "- No TCR; kills virus-infected and tumor cells",
 "ak-nk-cd56": "- CD16 is the Fc receptor used in ADCC",
 "ak-nk-il2-il12": "- IL-12 from macrophages links innate cells to NK activation",
 "ak-nk-tumor": "- Missing MHC I is like losing an identity card",
 "ak-ifn-antitumor": "- Type I and type II interferons both boost cytotoxicity",
 "ak-macrofago-tardio": "- Monocytes enter the tissue and become macrophages",
 "ak-lisozima": "- Lysozyme breaks bacterial peptidoglycan",
 "ak-cd14": "- CD14 is also the LPS co-receptor with TLR4",
 "ak-cd40l": "- CD40L helps activate macrophages and B cells",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (origem dos macrófagos, macrófago regulador) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula (Nature Reviews), sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "im22-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "im22-mo-subtipos.png": "Lâmina 38: origem de monócitos, macrófagos e CD na medula, sangue e tecido; verso de au-residente.",
 "im22-mo-reg.png": "Lâmina 42: Treg (IL-10) e outros sinais induzem o macrófago regulador anti-inflamatório; verso de au-mreg.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Rever como o reconhecimento leva a mecanismos efetores: fagocitose e opsonização, burst oxidativo e NO, neutrófilos e NETs, "
             "NK e ADCC, plasticidade dos macrófagos, migração dos T efetores e as funções de Th1, Th2, Th17 e CTL.",
 "centrais": [
   ("fagocitose", "ak-fagocitose", "sh-1791780361129"),
   ("macrófagos", "au-residente", "ak-macrofago-tardio"),
 ],
 "exemplos": ["Candida e Th17", "leishmaniose e hanseníase", "pus", "tumor sem MHC I"],
 "outras_aulas": [("reconhecimento inato", "08"), ("inflamação aguda", "37/38"), ("apresentação", "20"), ("ativação T", "45")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
