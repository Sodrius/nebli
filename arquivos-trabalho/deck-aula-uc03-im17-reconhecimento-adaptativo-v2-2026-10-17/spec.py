# Especificação curada — Reconhecimento pelo sistema imune na resposta adquirida (UC03 P1, Imunologia; 18 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing (seções FirstAid estrutura/função dos anticorpos, isotipos IgG/IgA/IgM/IgE, troca de classe) → cópias vivas da 49, da 18 e da 20
# por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
_S = "_FirstAid_02_Immunology_03_Immune_Responses_"
SECOES_DA_AULA = [_S + n + "_base.txt" for n in (
    "01_Antibody_structure_and_function_B_Cell_Receptor", "01_Antibody_structure_and_function_Diversity",
    "01_Antibody_structure_and_function_Specificity", "01_Antibody_structure_and_function_Structure",
    "01_Antibody_structure_and_function_T_Cell_Receptor", "02_Immunoglobulin_isotypes_Basics", "02_Immunoglobulin_isotypes_01_IgG",
    "02_Immunoglobulin_isotypes_01_IgG_Class_Switching", "02_Immunoglobulin_isotypes_02_IgA", "02_Immunoglobulin_isotypes_03_IGM",
    "02_Immunoglobulin_isotypes_05_IgE")]
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-im17-20261017a"
SHORT = "im17n"
LESSON = "2026-uc03-imunologia-17-reconhecimento-adaptativo"
DECK = "NEBLI::UC03::P1::Imunologia::Reconhecimento imune adaptativo"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"im17-{n}.png": f"img/im17-{n}.png" for n in ("humoral-celular", "eletroforese", "troca-classe", "estrutura")}
IMG = lambda n, w=440: f'<img src="im17-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (FirstAid estrutura e função dos anticorpos, isotipos, troca de classe, mieloma; "
         "busca/secoes); palavra-chave em AnKing e Referências Externas; significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
# Vagas da 07 (ainda não instalada): preencher com as cópias NEBLI de 1486867612235 (específica) e 1486867618953 (memória).
IM07 = {"ESPEC": None, "MEMORIA": None}
_C = lambda c, a: f"{a}: entra a cópia NEBLI viva (sh-{c})"
EXCLUIDOS = [
 (1486867654077, _C(1791629587397, "IgM e IgD no B naive")), (1486867658485, _C(1791629588145, "BCR bivalente")),
 (1486867662727, _C(1791629590722, "dobradiça")), (1486867667014, _C(1791629591146, "Igα/Igβ")),
 (1486945028810, _C(1791629589497, "V(D)J na cadeia pesada")), (1486945095844, _C(1791629589672, "D-J antes de V-DJ")),
 (1486945100917, _C(1791629589797, "VJ na cadeia leve")), (1486945105493, _C(1791629589372, "RAG1/RAG2")),
 (1486945119290, _C(1791629589120, "combinação H/L")), (1487117121383, _C(1791629594472, "hipermutação somática")),
 (1486867676959, _C(1791629588272, "idiotipo pelo Fab")), (1486867685826, _C(1791629588447, "isotipo pelo Fc")),
 (1486867696248, _C(1791629588622, "cadeia pesada no Fab e Fc")), (1486867700749, _C(1791629588747, "cadeia leve só no Fab")),
 (1486867708925, _C(1791629588872, "TCR αβ monovalente")), (1486867712651, _C(1791625428158, "CD3")),
 (1487117165317, _C(1791629598047, "IgG na resposta secundária")), (1487117187498, _C(1791629595747, "IgM e IgG fixam complemento")),
 (1487117191334, _C(1791629597298, "IgG atravessa a placenta")), (1487117197858, _C(1791629595321, "IgG opsoniza")),
 (1487117328797, _C(1791629595996, "ADCC por IgG")), (1487117143873, _C(1791629594096, "troca de classe no centro germinativo")),
 (1487117152018, _C(1791625431383, "CD40L e citocinas")), (1487117156031, _C(1791629594773, "IgA por IL-5 e TGF-β")),
 (1487117209824, _C(1791629596622, "IgA a mais produzida")), (1487117219869, _C(1791629591820, "IgA dímero com cadeia J")),
 (1487117223955, _C(1791629596922, "transcitose da IgA")), (1487117234083, _C(1791629597547, "IgA no colostro")),
 (1487117238120, _C(1791629597172, "IgA nas secreções")), (1487117251418, _C(1791629596747, "receptor poli-Ig")),
 (1487117255825, _C(1791629597045, "componente secretor")), (1487117074086, _C(1791629591997, "IgM monômero na membrana")),
 (1487117077263, _C(1791629591646, "IgM pentâmero")), (1487117100809, _C(1791629597922, "IgM primeiro")),
 (1487117260690, _C(1791629596372, "IgE em mastócitos")), (1487117266817, _C(1791629596247, "IgE contra vermes")),
 (1487117174952, "IgG fixa complemento: repete sh-1791629595747 (IgM e IgG fixam complemento)"),
 (1487117179318, "IgG atravessa a placenta: repete sh-1791629597298"),
 (1487117090100, "IgM fixa complemento: repete sh-1791629595747"),
 (1574313842839, "doença relacionada a IgG4: reumatologia, fora das lâminas"),
]
FORA_DO_RECORTE = [
 "Mieloma múltiplo como doença (CRAB, rim, amiloidose): aula de hematologia; aqui só o pico monoclonal e a cadeia leve.",
 "Detalhe da recombinação V(D)J, RAG, TdT e hipermutação: aula 18 (Recombinação), entram por sh e como referência.",
 "Rede idiotípica de Jerne e idiotipos públicos: só citados.",
]
A_, B_, C_, D_, E_ = "A-resposta-adquirida", "B-anticorpos-soro", "C-estrutura", "D-classes", "E-diversidade"

CARDS = [
 # ---------- A. Resposta adquirida (lâminas 3–6) ----------
 sh(1791629587397, "azul", A_, "B naive expressa IgM e IgD", 3, "lâmina 3 (receptor clonal); card da 49"),
 ak("ak-tcr-unico", 1486867704942, "A-step", A_, "T naive expressa um único TCR", 3, "lâmina 3 (um receptor por linfócito); seção"),
 sh(1791625424832, "verde", A_, "Reconhecimento T restrito ao MHC", 4, "lâmina 4; transcrição; prova 2015 P2 6.1; card da 20"),
 sh(1791629588997, "azul", A_, "TCR nunca é secretado", 4, "lâmina 4 (B reconhece direto); card da 49"),
 au("au-humoral-celular", "Immunity transferred to another animal by <b>serum</b> is {{c1::humoral}}, while immunity transferred only by cells is cellular",
    "V-pilar", A_, "Imunidade humoral × celular", 6, "lâminas 6 e 18; transcrição (definição pela transferência)",
    extra="- Humoral immunity depends on antibodies, but both usually need T-cell help<br>" + IMG("humoral-celular", 420)),
 ak("ak-humoral", 1487116986135, "A-aula", A_, "Humoral: anticorpos de plasmócitos", 6, "lâmina 6"),
 sh(1791625429833, "azul", A_, "Imunidade celular contra agentes intracelulares", 6, "lâmina 6; card vivo"),
 # ---------- B. Anticorpos no soro (lâminas 7–10) ----------
 au("au-gamaglobulinas", "Repeated <b>hyperimmunization</b> enlarges the {{c1::gamma globulin}} peak of serum electrophoresis, so antibodies were called gamma globulins",
    "A-aula", B_, "Anticorpos são gamaglobulinas", 7, "lâmina 7; transcrição",
    extra="- A single immunization does not change the profile, because the body is always making antibodies<br>" + IMG("eletroforese", 420)),
 ak("ak-mm-monoclonal", 1481335802501, "A-aula", B_, "Mieloma: proliferação monoclonal de plasmócitos", 8, "lâmina 8"),
 ak("ak-mm-spike", 1481335848197, "V-prova", B_, "Mieloma: pico M na eletroforese", 8, "lâmina 8; prova 2024 P1 1.4"),
 ak("ak-mm-igg", 1481335857397, "A-step", B_, "Pico M: IgG ou IgA monoclonal", 8, "lâmina 8"),
 ak("ak-mm-bence-jones", 1481335896023, "A-step", B_, "Bence Jones: cadeia leve livre na urina", 9, "lâmina 9 (proteínas do mieloma)"),
 au("au-avidez", "<b>Class switching</b> from IgM to IgG keeps specificity and affinity, but IgM pentamers have higher {{c1::avidity}}",
    "V-prova", B_, "Troca de classe e avidez", 10, "lâminas 10 e 15; transcrição (ênfase: o isotipo não muda afinidade); prova 2017 P1 4.4",
    extra="- Affinity is the strength of one binding site; avidity is the overall binding of the molecule (10 sites in IgM)<br>"
          "- The same plasma cell can switch class<br>" + IMG("troca-classe", 400)),
 sh(1791629594646, "verde", B_, "Troca de classe mantém a região variável", 10, "lâmina 10; prova 2017 P1 4.4; card da 49"),
 sh(1791629594096, "azul", B_, "Troca de classe no centro germinativo", 10, "lâmina 10; card da 49"),
 sh(1791625431383, "azul", B_, "Troca de classe: CD40L e citocinas do Th", 10, "lâmina 10; card vivo"),
 sh(1791629594773, "azul", B_, "Troca para IgA: IL-5 e TGF-β", 10, "card da 49"),
 ak("ak-switch-ige", 1487117161213, "R-detalhe", B_, "Troca para IgE: IL-4 e IL-13", 10, "seção"),
 # ---------- C. Estrutura (lâminas 11–13) ----------
 ak("ak-papaina", 1487117055356, "V-prova", C_, "Papaína: 2 Fab + 1 Fc", 11, "lâmina 11; prova 2024 P1 1.7; seção"),
 ak("ak-pepsina", 1487117063416, "V-hy", C_, "Pepsina: F(ab')2 bivalente", 11, "lâmina 11; seção"),
 sh(1791629588622, "verde", C_, "Cadeia pesada no Fab e no Fc", 11, "lâmina 11; card vivo"),
 sh(1791629588747, "azul", C_, "Cadeia leve só no Fab", 11, "lâmina 11; card vivo"),
 sh(1791629588145, "azul", C_, "BCR: duas cadeias pesadas e duas leves", 11, "lâmina 11; card vivo"),
 sh(1791629590722, "azul", C_, "Dobradiça dá flexibilidade", 11, "lâmina 11; card vivo"),
 au("au-cdr", "The <b>antigen-binding site</b> is formed by the {{c1::variable}} regions of the heavy and light chains, in the Fab",
    "V-prova", C_, "Sítio de ligação nas regiões variáveis", 11, "lâminas 11 e 13; transcrição (CDR); provas 2018 P1 1.14 e 2017 P3 1.6",
    extra="- A few hypervariable loops, the CDRs, contact the antigen; changing them changes specificity<br>"
          "- Effector functions depend on the heavy-chain constant regions in the Fc<br>" + IMG("estrutura", 360)),
 sh(1791629588447, "azul", C_, "Isotipo definido pelo Fc", 12, "lâmina 12; card vivo"),
 sh(1791629588272, "azul", C_, "Idiotipo definido pelo Fab", 12, "lâmina 12; prova 2024 P1 1.7; card vivo"),
 au("au-alotipos", "<b>Allotypes</b> are allelic antibody variants that differ between {{c1::individuals}} of the same species",
    "A-aula", C_, "Alotipos", 12, "lâmina 12; transcrição",
    extra="- Isotypes are the same in all individuals; idiotypes differ among antibodies of one person<br>- Repeated transfusions can sensitize against allotypes"),
 sh(1791629595321, "azul", C_, "IgG opsoniza", 13, "lâmina 13; prova 2017 P3 1.6; card da 49"),
 sh(1791629595747, "azul", C_, "IgM e IgG fixam complemento", 13, "lâmina 13; card da 49"),
 sh(1791629597298, "verde", C_, "IgG atravessa a placenta", 13, "lâmina 13; prova 2015 P2 5.1; card da 49"),
 sh(1791629597547, "azul", C_, "IgA no colostro", 13, "lâmina 13; card da 49"),
 sh(1791629595996, "azul", C_, "IgG media ADCC", 13, "lâmina 13 (ativação celular); card da 49"),
 # ---------- D. Classes (lâminas 14–15) ----------
 sh(1791629591646, "verde", D_, "IgM secretada é pentâmero", 14, "lâmina 14; prova 2024 P3 3.2; card da 49"),
 sh(1791629597922, "verde", D_, "IgM é a primeira na infecção", 14, "lâmina 14; prova 2015 P2 5.1; card da 49"),
 ak("ak-igm-primaria", 1487117104655, "A-step", D_, "IgM: principal na resposta primária", 14, "lâmina 14; seção"),
 ak("ak-igm-placenta", 1487117096735, "A-step", D_, "IgM não atravessa a placenta", 14, "seção"),
 ak("ak-igm-10", 1487117081885, "R-detalhe", D_, "IgM liga 10 antígenos", 14, "lâmina 14 (avidez); seção"),
 ak("ak-valencia", 1487117108862, "A-step", D_, "Valência = número de sítios", 14, "seção"),
 ak("ak-igm-valencia", 1487117115624, "A-step", D_, "IgM tem a maior valência", 14, "seção"),
 sh(1791629598047, "azul", D_, "IgG domina a resposta secundária", 14, "lâmina 14 (memória); card da 49"),
 ak("ak-igg-abundante", 1487117169828, "V-hy", D_, "IgG é a mais abundante no soro", 14, "lâmina 14; seção"),
 ak("ak-afinidade", 1487117112350, "A-step", D_, "Afinidade = força de um sítio", 14, "lâmina 15; seção"),
 ak("ak-igg-afinidade", 1487117118637, "A-step", D_, "IgG: maior afinidade (após maturação)", 14, "seção"),
 sh(1791629596372, "azul", D_, "IgE se liga a mastócitos e basófilos", 14, "lâmina 14; prova 2015 P2 5.1; card da 49"),
 ak("ak-ige-hipersensibilidade", 1487117263860, "A-aula", D_, "IgE: hipersensibilidade tipo I", 14, "lâmina 14 (emergências); transcrição (alergia)"),
 sh(1791629596247, "azul", D_, "IgE contra vermes via eosinófilos", 14, "lâmina 14; card da 49"),
 ak("ak-ige-rara", 1487117269713, "A-step", D_, "IgE é a menos abundante no soro", 14, "transcrição (difícil de achar); seção"),
 sh(1791629596622, "azul", D_, "IgA é a mais produzida", 14, "lâmina 14; transcrição; card da 49"),
 ak("ak-iga-monomero", 1487117216624, "A-step", D_, "IgA circula como monômero", 14, "seção"),
 sh(1791629591820, "azul", D_, "IgA secretada: dímero com cadeia J", 14, "card da 49"),
 sh(1791629596922, "azul", D_, "IgA atravessa o epitélio por transcitose", 14, "card da 49"),
 ak("ak-iga-tgi", 1487117227757, "A-aula", D_, "IgA protege o trato gastrointestinal", 14, "lâmina 14 (mucosas); seção"),
 sh(1791629597172, "azul", D_, "IgA nas secreções", 14, "card da 49"),
 ak("ak-iga-complemento", 1487117240890, "A-step", D_, "IgA não fixa complemento", 14, "lâmina 14 (anti-inflamatória); seção"),
 ak("ak-iga-placenta", 1487117247126, "A-step", D_, "IgA não atravessa a placenta", 14, "seção"),
 sh(1791629596747, "azul", D_, "IgA cruza a mucosa pelo receptor poli-Ig", 14, "prova 2015 P2 5.3; card da 49"),
 sh(1791629597045, "azul", D_, "Componente secretor protege a IgA", 14, "prova 2015 P2 5.3; card da 49"),
 sh(1791629591997, "azul", D_, "IgM monômero na membrana do B", 15, "lâmina 15; prova 2024 P3 3.2; card da 49"),
 ak("ak-plasmocito-um", 1487117272282, "A-step", D_, "Cada plasmócito secreta um isotipo", 15, "seção"),
 ak("ak-monomero", 1487117070760, "R-detalhe", D_, "Todos os isotipos existem como monômero", 15, "seção"),
 sh(1791629591146, "azul", D_, "Sinalização do BCR por Igα/Igβ", 15, "card da 49"),
 # ---------- E. Diversidade (lâminas 16–17) ----------
 au("au-tonegawa", "<b>Tonegawa</b> showed that V and C gene segments, distant in germ cells, are joined by somatic {{c1::recombination}} in lymphocytes",
    "A-aula", E_, "Recombinação somática (Tonegawa)", 16, "lâminas 9, 16 e 18; transcrição (Dreyer & Bennett, Jerne, Tonegawa)",
    extra="- Dreyer and Bennett had seen a shared constant part and a variable part in myeloma proteins<br>- The repertoire is built, not stored in the genome"),
 sh(1791629589497, "azul", E_, "V(D)J na cadeia pesada", 16, "lâmina 16; card vivo"),
 sh(1791629589672, "azul", E_, "D-J antes de V-DJ", 16, "card vivo"),
 sh(1791629589797, "azul", E_, "VJ na cadeia leve", 16, "card vivo"),
 sh(1791629589372, "azul", E_, "RAG1 e RAG2", 16, "card vivo"),
 ak("ak-tdt", 1486945114357, "A-step", E_, "TdT insere nucleotídeos na junção", 16, "lâmina 18 (mecanismos complementares); prova 2018 P1 1.14; seção"),
 sh(1791629589120, "azul", E_, "Combinação aleatória de cadeias H e L", 16, "prova 2018 P1 1.14; card vivo"),
 sh(1791629594472, "azul", E_, "Hipermutação somática e maturação da afinidade", 16, "card vivo"),
 sh(1791629588872, "azul", E_, "TCR αβ monovalente", 17, "lâmina 17; card vivo"),
 sh(1791625428158, "azul", E_, "CD3 sinaliza pelo TCR", 17, "card vivo"),
 ak("ak-tcr-rigido", 1486867718130, "R-detalhe", E_, "TCR é rígido (sem dobradiça)", 17, "seção"),
 ak("ak-tcr-clonalidade", 1523570028468, "A-step", E_, "Rearranjo do TCR mostra clonalidade", 17, "lâmina 17 (Allison: anticorpo contra um linfoma T); seção"),
]
_IM07 = [("ESPEC", "verde", A_, "Imunidade adaptativa é específica", 5, "lâmina 5; card da 07"),
         ("MEMORIA", "verde", A_, "Imunidade adaptativa tem memória", 5, "lâmina 5; card da 07")]
for _k, _c, _b, _a, _s, _m in _IM07:
    if IM07[_k]:
        CARDS.append(sh(IM07[_k], _c, _b, _a, _s, _m))

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak-tcr-unico": "- Each lymphocyte carries a single receptor; the repertoire is distributed clonally",
 "ak-humoral": "- Defined historically by transfer with serum",
 "ak-mm-monoclonal": "- Myeloma proteins let Dreyer and Bennett study one homogeneous antibody",
 "ak-mm-spike": "- A narrow, tall peak in the gamma region: one clone",
 "ak-mm-igg": "- Each myeloma secretes one homogeneous immunoglobulin",
 "ak-mm-bence-jones": "- Light chains are kappa or lambda",
 "ak-switch-ige": "- IgE is made for violent, immediate reactions",
 "ak-papaina": "- Fab binds antigen; Fc is the crystallizable fragment",
 "ak-pepsina": "- Pepsin digests the Fc and leaves the two Fab arms joined at the hinge",
 "ak-igm-primaria": "- Ten binding sites give high avidity before selection improves the fit",
 "ak-igm-placenta": "- Too large; it also activates complement and inflammation early",
 "ak-igm-10": "- Five monomers with two sites each",
 "ak-valencia": "- Avidity grows with valence",
 "ak-igm-valencia": "- Hence its high avidity even with low affinity",
 "ak-igg-abundante": "- Small, monomeric and long-lived, it carries memory",
 "ak-afinidade": "- The isotype itself does not change affinity",
 "ak-igg-afinidade": "- Higher affinity comes from affinity maturation over time, not from the isotype",
 "ak-ige-hipersensibilidade": "- Discovered through allergy",
 "ak-ige-rara": "- Most IgE sits bound to mast cells",
 "ak-iga-monomero": "- Secreted IgA is a dimer",
 "ak-iga-tgi": "- It prevents infection without inflammation",
 "ak-iga-complemento": "- An anti-inflammatory antibody for mucosae",
 "ak-iga-placenta": "- It reaches the newborn through milk instead",
 "ak-plasmocito-um": "- IgD is a membrane receptor and is not normally secreted",
 "ak-monomero": "- IgM and IgA polymers form after synthesis",
 "ak-tdt": "- Adds diversity at the junctions",
 "ak-tcr-rigido": "- The TCR sees peptide bound to MHC",
 "ak-tcr-clonalidade": "- The TCR was found as a clone-specific molecule on a T lymphoma",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (transferência, eletroforese, troca de classe, estrutura) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula, sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "im17-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "im17-humoral-celular.png": "Lâmina 6: animal imune; soro transfere imunidade humoral, células transferem imunidade celular; verso de au-humoral-celular.",
 "im17-eletroforese.png": "Lâmina 7: eletroforese do soro (albumina, α1, α2, β, γ) e aumento da gama na hiperimunização; verso de au-gamaglobulinas.",
 "im17-troca-classe.png": "Lâmina 10: IgM seguida de IgG na resposta primária; a mesma célula troca a classe; verso de au-avidez.",
 "im17-estrutura.png": "Lâmina 11: imunoglobulina com VH/VL, CH1–CH3, dobradiça, Fab e Fc; verso de au-cdr.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Entender a resposta adquirida (específica, com memória; humoral × celular), identificar anticorpos no soro, descrever a estrutura "
             "da imunoglobulina (Fab, Fc, cadeias, regiões V e C, isotipos, alotipos, idiotipos), as funções de cada classe, a troca de classe "
             "e a geração da diversidade por recombinação somática.",
 "centrais": [
   ("humoral × celular", "au-humoral-celular", "ak-humoral"),
   ("estrutura", "au-cdr", "sh-1791629588447"),
   ("troca de classe", "au-avidez", "sh-1791629594096"),
   ("papaína", "ak-papaina", "ak-pepsina"),
   ("mieloma", "ak-mm-spike", "ak-mm-igg"),
 ],
 "exemplos": ["camundongo imunizado com bactéria atenuada", "mieloma de Dreyer & Bennett", "linfoma T de Allison", "transfusões e alotipos"],
 "outras_aulas": [("BCR, classes e troca de classe", "49 Ativação de células B (sh)"), ("V(D)J", "18 Recombinação (sh)"),
                  ("restrição ao MHC", "20 MHC (sh)"), ("especificidade e memória", "07 Organização do SI (vaga IM07)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
