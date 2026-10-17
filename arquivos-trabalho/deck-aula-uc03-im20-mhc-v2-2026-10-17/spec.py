# Especificação curada — MHC: captura, processamento e apresentação de antígenos (UC03 P1, Imunologia; 75 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing (seções FirstAid MHC I e II, ativação T, células dendríticas) → cópias vivas (antiga 20, 07, 37, 45, 61) por sh()
# → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
_M = "_FirstAid_02_Immunology_02_Cellular_Components_03_Major_histocompatibility_complex_I_and_II"
SECOES_DA_AULA = [_M + "_base.txt", _M + "_Basics_base.txt", _M + "_MHC_II_base.txt",
    "_FirstAid_02_Immunology_02_Cellular_Components_11_T_and_B_cell_activation_01_T_cell_activation_T_Activation_base.txt",
    "_FirstAid_10_Hematology_and_Oncology_02_Anatomy_07_Dendritic_cells_base.txt"]
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-im20-20261017a"
SHORT = "im20n"
LESSON = "2026-uc03-imunologia-20-mhc-apresentacao"
DECK = "NEBLI::UC03::P1::Imunologia::MHC e apresentação de antígenos"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"im20-{n}.png": f"img/im20-{n}.png" for n in ("haplotipos", "ancoras", "clip", "pdc", "mhc1-montagem")}
IMG = lambda n, w=420: f'<img src="im20-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (FirstAid MHC I e II, ativação T, células dendríticas, HLA; busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
# Vaga da 07 (ainda não instalada): preencher com a cópia NEBLI de 1486945137995 (antígenos chegam pelos linfáticos aferentes).
IM07 = {"LINFATICO": None}
_C = lambda c, a: f"{a}: entra a cópia NEBLI viva (sh-{c})"
_HLA = "tipagem HLA (microcitotoxicidade, cultura mista): aula 66 Bases imunes dos transplantes"
EXCLUIDOS = [
 (1486952638474, _C(1791625424657, "MHC I liga CD8")), (1486952653362, _C(1791625424957, "β2-microglobulina")),
 (1487115889320, _C(1791625426657, "MHC I apresenta antígeno endógeno")), (1487116826422, _C(1791625426833, "proteassoma e TAP")),
 (1520301453074, _C(1791984890952, "IFN tipo I aumenta MHC I")), (1486952670744, _C(1791625424481, "MHC II liga CD4")),
 (1486952685707, _C(1791625427233, "cadeia invariante")), (1487116831797, _C(1791625427059, "MHC II apresenta antígeno exógeno")),
 (1487116836334, _C(1791625427358, "liberação da cadeia invariante no endossomo")), (1487116841407, _C(1791625428408, "sinal 1")),
 (1487116849895, _C(1791625428533, "sinal 2 B7/CD28")), (1520300810177, _C(1791625430082, "CD40/CD40L")),
 (1479267468509, _C(1791625422291, "CD liga inato e adquirido")),
 (1516063346538, _HLA), (1516063419308, _HLA), (1516063580163, _HLA),
 (1486867704942, "T naive com um único TCR: aula 17 (Reconhecimento adaptativo)"),
 (1523570028468, "clonalidade pelo rearranjo do TCR: aulas 17 e 51"),
]
FORA_DO_RECORTE = [
 "Lâminas 2–24: inflamação, homeostase e receptores inatos (TLR, inflamassoma) — aulas 08 e 37.",
 "Diferenciação Th1/Th2/Th17/Treg e efetores do CD8: aulas 45 e 22; aqui só o elo apresentação → subtipo.",
 "Tipagem HLA e rejeição: aula 66.",
]
A_, B_, C_, D_, E_ = "A-reconhecimento", "B-celulas-dendriticas", "C-mhc", "D-processamento", "E-ativacao"

CARDS = [
 # ---------- A. Reconhecimento (lâminas 20–28) ----------
 sh(1791625422291, "verde", A_, "CD liga imunidade inata e adquirida", 20, "lâminas 20 e 22; card da 37"),
 sh(1791625432383, "azul", A_, "Th1 induzido por IL-12 e IFN-γ", 21, "lâminas 21 e 65; card da 45"),
 sh(1791625426282, "verde", A_, "T só reconhece antígeno com peptídeo", 23, "lâmina 23 (BCR vê moléculas inteiras, TCR processadas); card vivo"),
 sh(1791625424832, "verde", A_, "Reconhecimento T restrito ao MHC", 24, "lâminas 24, 39 e 48; card da 20"),
 sh(1791625424657, "verde", A_, "MHC I liga TCR e CD8", 26, "lâminas 26 e 46; card da 20"),
 sh(1791625424481, "verde", A_, "MHC II liga TCR e CD4", 26, "lâminas 26 e 47; card da 20"),
 # ---------- B. Células dendríticas (lâminas 30–38) ----------
 ak("ak-mhc-apresenta", 1486952617561, "A-aula", B_, "MHC das CAA apresenta fragmentos ao T", 30, "lâmina 30; seção"),
 sh(1791625425333, "verde", B_, "CD amadurece ao migrar: mais MHC e coestímulo", 32, "lâminas 32, 37 e 38; prova 2017 P4 1.6; card da 20"),
 ak("ak-langerhans", 1479267502899, "A-aula", B_, "Na pele, CD = célula de Langerhans", 33, "lâmina 33; seção"),
 sh(1791625425478, "azul", B_, "Langerhans apresenta antígeno ao T naive", 33, "lâmina 33; card da 20"),
 sh(1791625426408, "verde", B_, "CD é a CAA mais potente", 34, "lâminas 34–35; card da 07"),
 sh(1791625426532, "azul", B_, "B7 nas CAA (B, macrófago, CD)", 34, "lâminas 34 e 38; card vivo"),
 au("au-pdc", "<b>Plasmacytoid dendritic cells</b> sense viral nucleic acids through TLR7 and TLR9 and secrete type I {{c1::interferons}}",
    "A-aula", B_, "CD plasmocitoide", 36, "lâmina 36; transcrição (SARS-CoV-2 reduz o IFN tipo I)",
    extra="- Conventional dendritic cells are the ones that present antigen to naive T cells<br>" + IMG("pdc", 420)),
 # ---------- C. MHC (lâminas 40–49) ----------
 ak("ak-mhc1-cadeias", 1486952644614, "A-aula", C_, "MHC I: uma cadeia longa e uma curta", 40, "lâminas 40 e 45; seção"),
 ak("ak-mhc2-cadeias", 1486952677289, "A-aula", C_, "MHC II: duas cadeias de tamanho igual", 40, "lâminas 40 e 45; seção"),
 ak("ak-hla", 1486952620697, "A-aula", C_, "MHC é codificado pelos genes HLA", 41, "lâmina 41; seção"),
 ak("ak-mhc1-abc", 1486952623418, "V-hy", C_, "HLA-A, B e C = MHC I", 41, "lâmina 41; seção"),
 ak("ak-mhc2-dp", 1486952657292, "V-hy", C_, "HLA-DP, DQ e DR = MHC II", 41, "lâmina 41; seção"),
 au("au-codominante", "<b>HLA genes</b> are expressed {{c1::codominantly}} and inherited as one haplotype from each parent",
    "A-aula", C_, "Herança codominante do HLA", 42, "lâmina 42; transcrição (haplótipos, irmãos); prova 2015 P2sub 3.3",
    extra="- A sibling has a 25% chance of sharing both haplotypes, which is why unrelated donor registries are needed<br>" + IMG("haplotipos", 380)),
 au("au-polimorfismo", "<b>MHC genes</b> are the most {{c1::polymorphic}} in the genome, and each MHC molecule binds many peptides through anchor residues",
    "A-aula", C_, "Polimorfismo e resíduos âncora", 43, "lâminas 43–44; transcrição; prova 2015 P2sub 3.3 (rejeição de transplante)",
    extra="- Polymorphism makes people differ, which drives graft rejection<br>" + IMG("ancoras", 420)),
 ak("ak-mhc1-seis", 1486952689393, "R-detalhe", C_, "Seis tipos de MHC I por célula", 43, "lâmina 43 (poligenia); seção"),
 ak("ak-mhc1-fenda", 1486952649215, "V-hy", C_, "MHC I: fenda menor (8–10 aa)", 45, "lâminas 45 e 68; seção"),
 ak("ak-mhc2-fenda", 1486952681913, "V-hy", C_, "MHC II: fenda maior (13–17 aa)", 45, "lâminas 45 e 68; seção"),
 sh(1791625424957, "azul", C_, "β2-microglobulina acompanha o MHC I", 45, "lâmina 45; card da 20"),
 ak("ak-mhc1-nucleadas", 1486952630150, "V-prova", C_, "MHC I em todas as células nucleadas e plaquetas", 46, "lâmina 46; provas 2015 P2 2.7 e 7.3"),
 ak("ak-plaquetas", 1486956337697, "R-detalhe", C_, "Plaquetas expressam MHC I", 46, "seção"),
 ak("ak-mhc2-apc", 1486952664370, "V-prova", C_, "MHC II só nas CAA", 47, "lâminas 35 e 47; prova 2015 P2 7.3"),
 sh(1791625423282, "azul", C_, "Seleção positiva: TCR que liga MHC próprio", 48, "lâmina 48; prova 2015 P2 6.2; card da 07"),
 ak("ak-superantigeno", 1487117336631, "V-hy", C_, "Superantígeno une TCR β ao MHC II sem processamento", 49, "lâmina 49; transcrição; seção"),
 ak("ak-superantigeno-cd4", 1487117356804, "A-step", C_, "Superantígeno ativa qualquer CD4: tempestade de citocinas", 49, "seção"),
 # ---------- D. Processamento (lâminas 50–61) ----------
 sh(1791625426657, "verde", D_, "MHC I apresenta antígeno endógeno ao CD8", 50, "lâminas 50, 55 e 67; prova 2015 P2 2.7; card da 20"),
 sh(1791625427059, "verde", D_, "MHC II apresenta antígeno exógeno ao CD4", 50, "lâminas 50, 56 e 67; card da 20"),
 sh(1791625426833, "verde", D_, "Proteassoma no citosol e TAP para o RE", 51, "lâminas 51–53 e 70; provas 2015 P2 7.1 e 7.2; card da 20"),
 au("au-mhc-vazio", "An <b>MHC class I</b> molecule leaves the endoplasmic reticulum only after binding a {{c1::peptide}}",
    "A-aula", D_, "MHC I só é exportado com peptídeo", 54, "lâmina 54; transcrição; prova 2015 P2 7.2 (inibição de TAP)",
    extra="- So viral TAP inhibitors (HSV) lower surface MHC I and escape CD8 cells<br>" + IMG("mhc1-montagem", 440)),
 sh(1791625427358, "azul", D_, "Peptídeo entra no MHC II após saída da cadeia invariante", 56, "lâminas 56–57; card da 20"),
 sh(1791625427233, "azul", D_, "Cadeia invariante associada ao MHC II", 58, "lâmina 58; card da 20"),
 au("au-hla-dm", "In the endosome, <b>HLA-DM</b> removes {{c1::CLIP}} from MHC class II so antigenic peptides can bind",
    "A-aula", D_, "HLA-DM troca o CLIP", 58, "lâmina 58; Abbas cap. 3",
    extra="- CLIP is the invariant-chain fragment left in the groove<br>" + IMG("clip", 380)),
 sh(1791625427531, "verde", D_, "Apresentação cruzada nas CD", 60, "lâminas 60–61 e 69; prova 2017 P2 2.9; card da 07"),
 ak("ak-mhc1-tumor", 1496163155030, "A-aula", D_, "Proteínas anormais (mutadas) no MHC I", 69, "transcrição (célula tumoral → CD8); seção"),
 # ---------- E. Ativação (lâminas 62–71) ----------
 sh(1791625428408, "verde", E_, "Sinal 1: TCR + MHC/peptídeo", 62, "lâminas 27 e 62; card da 45"),
 sh(1791625428533, "verde", E_, "Sinal 2: B7 (CD80/86) + CD28", 62, "lâminas 62–63; prova 2015 P2 3.3; card da 45"),
 sh(1791625430082, "azul", E_, "CD40L do T com CD40", 63, "lâmina 63; card da 45"),
 sh(1791625431758, "azul", E_, "Th1 secreta IFN-γ e IL-2", 64, "lâminas 28 e 64; card da 45"),
 sh(1791625432007, "azul", E_, "Th2 recruta eosinófilos", 64, "lâmina 64; card da 45"),
 sh(1791984890952, "azul", E_, "IFN tipo I aumenta MHC I", 70, "lâmina 70; card da 61"),
 sh(1791625430332, "azul", E_, "IFN-γ aumenta MHC II", 71, "lâmina 71; card vivo"),
]
_IM07 = [("LINFATICO", "azul", B_, "Antígenos chegam pelos linfáticos aferentes", 31, "lâmina 31; card da 07")]
for _k, _c, _b, _a, _s, _m in _IM07:
    if IM07[_k]:
        CARDS.append(sh(IM07[_k], _c, _b, _a, _s, _m))

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak-mhc-apresenta": "- T cells need antigen captured, processed and presented",
 "ak-langerhans": "- They carry antigen from the epidermis to lymph nodes",
 "ak-mhc1-cadeias": "- The α chain plus β2-microglobulin",
 "ak-mhc2-cadeias": "- α and β chains, both forming the groove",
 "ak-hla": "- MHC in humans is called HLA",
 "ak-mhc1-abc": "- Class I genes present to CD8 T cells",
 "ak-mhc2-dp": "- Class II genes present to CD4 T cells",
 "ak-mhc1-seis": "- Two alleles each of HLA-A, B and C",
 "ak-mhc1-fenda": "- Closed at both ends, fits short proteasome peptides",
 "ak-mhc2-fenda": "- Open at both ends, fits longer endosomal peptides",
 "ak-mhc1-nucleadas": "- So any infected or tumor cell can show peptides to CD8 cells",
 "ak-plaquetas": "- Red blood cells lack MHC I",
 "ak-mhc2-apc": "- Restricting class II limits who can activate the powerful CD4 cell",
 "ak-superantigeno": "- Explains very fast, massive reactions such as toxic shock",
 "ak-superantigeno-cd4": "- Up to 20% of T cells, a cytokine storm",
 "ak-mhc1-tumor": "- Tumor proteins processed by the proteasome activate CD8 cells",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (haplótipos, âncoras, CLIP, CD, montagem do MHC I) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula (Abbas, Kuby), sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "im20-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "im20-haplotipos.png": "Lâmina 42: pais com dois haplótipos HLA e as quatro combinações possíveis nos filhos; verso de au-codominante.",
 "im20-ancoras.png": "Lâmina 44: peptídeos de ovalbumina e influenza na fenda do MHC com resíduos âncora (P2, P5, P8/9); verso de au-polimorfismo.",
 "im20-clip.png": "Lâmina 58: MHC II + cadeia invariante → CLIP → HLA-DM troca CLIP por peptídeo; HLA-DO regula; verso de au-hla-dm.",
 "im20-pdc.png": "Lâmina 36: CD convencional × plasmocitoide (TLR7/9, IFN-α/β); verso de au-pdc.",
 "im20-mhc1-montagem.png": "Lâmina 54: montagem do MHC I no RE (calnexina, tapasina, TAP) e exportação só com peptídeo; verso de au-mhc-vazio.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Entender como as CAA (sobretudo a célula dendrítica) capturam, processam e apresentam antígenos; a estrutura, os genes e o "
             "polimorfismo do MHC; as vias citosólica (MHC I → CD8) e endocítica (MHC II → CD4), a apresentação cruzada, os superantígenos "
             "e os dois sinais da ativação T.",
 "centrais": [
   ("classes de MHC", "ak-mhc1-nucleadas", "ak-mhc2-apc"),
   ("genética do HLA", "au-codominante", "au-polimorfismo"),
   ("vias de processamento", "sh-1791625426657", "au-mhc-vazio"),
 ],
 "exemplos": ["SARS-CoV-2 e IFN tipo I", "HSV inibe TAP", "choque tóxico por superantígeno", "transplante de medula"],
 "outras_aulas": [("receptores inatos e inflamassoma", "08 e 37"), ("subtipos Th", "45"), ("seleção tímica", "07"), ("tipagem HLA", "66")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
