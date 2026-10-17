# Especificação curada — Geração de diversidade de anticorpos por recombinação (UC03 P1, Biologia Molecular; 25 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing (seções FirstAid diversidade de anticorpos, hipermutação, troca de classe, JNHE, recombinação homóloga, reparo por excisão de base)
# → cópias vivas (49, 51, antiga 18, 46) por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [
    "_FirstAid_02_Immunology_03_Immune_Responses_01_Antibody_structure_and_function_Diversity_base.txt",
    "_FirstAid_02_Immunology_03_Immune_Responses_01_Antibody_structure_and_function_Specificity_base.txt",
    "_FirstAid_02_Immunology_03_Immune_Responses_02_Immunoglobulin_isotypes_01_IgG_Class_Switching_base.txt",
    "_FirstAid_01_Biochem_01_Molecular_07_DNA_repair_01_Double_strand_Nonhomologous_End_Joining_base.txt",
    "_FirstAid_01_Biochem_01_Molecular_07_DNA_repair_01_Double_strand_Homologous_Recombination_base.txt",
    "_FirstAid_01_Biochem_01_Molecular_07_DNA_repair_02_Single_strand_Base_Excision_Repair_base.txt",
]
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-bm18-20261017a"
SHORT = "bm18n"
LESSON = "2026-uc03-biologia-molecular-18-recombinacao"
DECK = "NEBLI::UC03::P1::Biologia Molecular::Recombinação V(D)J"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"bm18-{n}.png": f"img/bm18-{n}.png" for n in ("vj", "rss", "juncional", "aid")}
IMG = lambda n, w=420: f'<img src="bm18-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (FirstAid diversidade de anticorpos, troca de classe, reparo de quebra dupla, "
         "excisão de base; busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em todos os "
         "acervos e NEBLI vivo (busca/semantica.jsonl). ")
# Vagas da 17 (ainda não instalada): preencher com as cópias NEBLI de 1486945114357 (TdT) e 1487117161213 (troca para IgE).
IM17 = {"TDT": 1792241814320, "SWITCH_IGE": 1792241808513}
_C = lambda c, a: f"{a}: entra a cópia NEBLI viva (sh-{c})"
_BRCA = "BRCA1/2 e câncer: aula de oncogenes e supressores, fora das lâminas"
_BER = "detalhe enzimático do reparo por excisão de base: aula de reparo do DNA (UC1/UC2, 85), fora das lâminas"
EXCLUIDOS = [
 (1486945028810, _C(1791629589497, "V(D)J na pesada")), (1486945095844, _C(1791629589672, "D-J antes de V-DJ")),
 (1486945100917, _C(1791629589797, "VJ na leve")), (1486945105493, _C(1791629589372, "RAG1/RAG2")),
 (1486945119290, _C(1791629589120, "combinação H/L")), (1487117121383, _C(1791629594472, "hipermutação")),
 (1487117143873, _C(1791629594096, "centro germinativo")), (1487117152018, _C(1791625431383, "CD40L")),
 (1487117156031, _C(1791629594773, "IgA por IL-5/TGF-β")), (1516938350345, _C(1791630175220, "JNHE sujeita a erro")),
 (1486945114357, "TdT: instalado pela aula 17 — entra a cópia dela (vaga IM17)"),
 (1487117161213, "troca para IgE por IL-4/IL-13: instalado pela aula 17 — entra a cópia dela (vaga IM17)"),
 (1487117055356, "papaína: estrutura da Ig, aula 17"), (1487117063416, "pepsina: estrutura da Ig, aula 17"),
 (1516937404658, _BRCA), (1516937636586, _BRCA), (1517965672372, _BRCA),
 (1516939735510, "repete ak-reparo-scid (JNHE defeituosa na ataxia-telangiectasia e talvez no SCID)"),
 (1467819801792, _BER), (1467819810778, _BER), (1467819815746, _BER), (1467819819593, _BER),
]
FORA_DO_RECORTE = [
 "Estrutura e classes de imunoglobulina: aula 17 (Reconhecimento adaptativo).",
 "Tolerância central e eliminação de B autorreativos: aula de imunologia; aqui só a pergunta final.",
 "Números exatos de segmentos (35/76 V kappa, 40/300 V pesada): variam entre fontes; o card cobra o princípio multiplicativo.",
]
A_, B_, C_, D_, E_ = "A-desafio", "B-recombinacao", "C-juncao-reparo", "D-hipermutacao", "E-troca-classe"

CARDS = [
 # ---------- A. O desafio (lâminas 5–12) ----------
 au("au-desafio", "Over 10^7 <b>antibody specificities</b> come from about 25,000 genes because variable regions are built by somatic {{c1::recombination}}",
    "V-pilar", A_, "O desafio da diversidade", 5, "lâminas 5, 9, 12 e 24; transcrição I; exercícios 1, 5 e 8",
    extra="- Combinatorial diversity multiplies the numbers of V, D and J segments, then heavy × light chains<br>"
          "- Each B cell makes one specificity, as the monoclonal myeloma protein showed"),
 sh(1791629589247, "azul", A_, "V(D)J nos linfócitos imaturos, antes do antígeno", 7, "lâmina 7; card vivo"),
 sh(1791629590897, "azul", A_, "Cada B faz cadeia leve kappa ou lambda", 8, "lâmina 8; transcrição III; card vivo"),
 # ---------- B. Recombinação V(D)J (lâminas 11–16) ----------
 au("au-irreversivel", "V(D)J recombination <b>deletes</b> the intervening DNA, so it is irreversible and brings the V promoter near the {{c1::enhancer}}",
    "V-pilar", B_, "Recombinação irreversível ativa o promotor", 11, "lâmina 11; transcrição II; exercício 3",
    extra="- Splicing then joins VJ (or VDJ) to the constant region in the mRNA<br>" + IMG("vj", 360)),
 sh(1791627547052, "azul", B_, "Enhancer distante age dobrando o DNA", 11, "lâmina 11; card da 46"),
 sh(1791629589797, "verde", B_, "VJ na cadeia leve", 11, "lâmina 11; card vivo"),
 sh(1791629589497, "verde", B_, "V(D)J na cadeia pesada", 11, "lâmina 11; card vivo"),
 sh(1791629589672, "verde", B_, "D-J primeiro, depois V-DJ", 11, "lâmina 11; exercício 3; card vivo"),
 sh(1791629589120, "azul", B_, "Combinação aleatória das cadeias H e L", 12, "lâminas 12 e 24; card vivo"),
 au("au-regra-12-23", "<b>RAG</b> joins a signal with a 12-bp spacer only to one with a {{c1::23}}-bp spacer",
    "V-prova", B_, "Regra 12/23", 13, "lâminas 13 e 16; transcrição III; prova 2024 P1 1.6; exercício 4",
    extra="- So V always joins J (light chain) or D (heavy chain)<br>- Each signal is a conserved heptamer and nonamer separated by the spacer<br>- RAG nicks one strand and the free 3′-OH forms a hairpin, a double-strand break<br>" + IMG("rss", 420)),
 au("au-exclusao-alelica", "A productive rearrangement on one allele blocks the other allele, called allelic {{c1::exclusion}}, so each <b>B cell</b> has one specificity",
    "A-aula", B_, "Exclusão alélica", 14, "lâmina 14; transcrição III",
    extra="- If the first allele fails, the second one gets a try<br>- Kappa rearranges before lambda, so about 60% of antibodies use kappa"),
 sh(1791629589372, "verde", B_, "RAG1 e RAG2 fazem a recombinação", 15, "lâmina 15; card vivo"),
 sh(1792166982691, "azul", B_, "Mutação de RAG causa SCID", 15, "transcrição III (nocaute de RAG sem B e T); card da 51"),
 # ---------- C. Junção e reparo (lâminas 17–21) ----------
 au("au-juncional", "Asymmetric opening of the coding-end hairpins adds palindromic {{c1::P nucleotides}} at <b>V(D)J junctions</b>, raising junctional diversity",
    "A-aula", C_, "Diversidade juncional (nucleotídeos P)", 17, "lâminas 17, 21 e 25; transcrição III; exercício 6",
    extra="- TdT adds random N nucleotides without a template; exonucleases remove others<br>"
          "- About two thirds of junctions shift the reading frame and are nonproductive<br>" + IMG("juncional", 380)),
 ak("ak-nhej-ciclo", 1516938061553, "A-step", C_, "JNHE ocorre em todo o ciclo", 18, "lâmina 18; seção"),
 ak("ak-artemis", 1516938209170, "A-aula", C_, "JNHE: ATM, MRN e Artemis", 18, "lâmina 21 (Artemis abre o grampo); transcrição III; seção"),
 ak("ak-ds-break", 1467819823153, "V-hy", C_, "Quebra dupla: JNHE e recombinação homóloga", 19, "lâmina 19; seção"),
 ak("ak-hr-cromatide", 1516937292174, "V-hy", C_, "Recombinação homóloga usa a cromátide irmã (após S)", 19, "lâmina 19; seção"),
 ak("ak-hr-fiel", 1516937730893, "A-step", C_, "Recombinação homóloga não é sujeita a erro", 19, "lâmina 19; seção"),
 sh(1791630175220, "verde", C_, "JNHE é sujeita a erro", 19, "lâminas 19–20; card vivo"),
 ak("ak-reparo-scid", 1467819833068, "A-step", C_, "Reparo de quebra dupla defeituoso: AT, Fanconi, SCID", 20, "seção"),
 ak("ak-ataxia", 1487727707397, "R-detalhe", C_, "Ataxia-telangiectasia: falha no reparo de quebra dupla", 20, "seção"),
 # ---------- D. Hipermutação (lâmina 22) ----------
 au("au-aid", "In activated <b>B cells</b>, AID deaminates cytosine to {{c1::uracil}} in variable regions, starting somatic hypermutation",
    "V-prova", D_, "AID e hipermutação somática", 22, "lâmina 22; transcrição IV; prova 2023 P1 2.8; exercício 7",
    extra="- Replication over U:G gives C→T; uracil glycosylase leaves an abasic site filled at random by translesion polymerases<br>"
          "- Selection of higher-affinity clones is affinity maturation<br>" + IMG("aid", 420)),
 sh(1791629595072, "verde", D_, "Hipermutação e troca de classe dependem de AID", 22, "lâminas 22–23; card vivo"),
 sh(1791629594472, "azul", D_, "Hipermutação com maturação da afinidade", 22, "lâmina 22; prova 2023 P1 2.8; card vivo"),
 ak("ak-desaminacao", 1467819760893, "A-aula", D_, "Desaminação de citosina em uracila", 22, "lâmina 22; seção"),
 ak("ak-ber-desaminacao", 1467819790375, "A-step", D_, "Excisão de base corrige desaminação", 22, "lâmina 22 (UNG); seção"),
 ak("ak-glicosilase", 1467819793606, "A-aula", D_, "Glicosilase remove a base e cria sítio AP", 22, "lâmina 22 (sítio abásico); seção"),
 # ---------- E. Troca de classe (lâmina 23) ----------
 au("au-troca-dna", "<b>Class switching</b> deletes the constant-region DNA between two {{c1::switch}} regions, keeping the same VDJ",
    "V-prova", E_, "Troca de classe por recombinação", 23, "lâmina 23; transcrição II; provas 2024 P1 1.6 e 2018 P1 1.14",
    extra="- It depends on AID and happens after antigen activation, in the periphery<br>- It changes function, not specificity, so it adds no diversity"),
 sh(1791629594096, "azul", E_, "Troca de classe no centro germinativo", 23, "card vivo"),
 sh(1791625431383, "azul", E_, "Troca de classe: CD40L e citocinas", 23, "card vivo"),
 sh(1791629594773, "azul", E_, "Troca para IgA: IL-5 e TGF-β", 23, "card vivo"),
 sh(1792166990290, "azul", E_, "Hiper-IgM: troca de classe defeituosa", 23, "card da 51"),
 sh(1792166990541, "azul", E_, "Hiper-IgM: IgA, IgG e IgE baixas", 23, "card da 51"),
]
_IM17 = [("TDT", "azul", C_, "TdT insere nucleotídeos N", 17, "lâmina 17; card da 17"),
         ("SWITCH_IGE", "rosa", E_, "Troca para IgE: IL-4 e IL-13", 23, "card da 17")]
for _k, _c, _b, _a, _s, _m in _IM17:
    if IM17[_k]:
        CARDS.append(sh(IM17[_k], _c, _b, _a, _s, _m))

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak-nhej-ciclo": "- It needs no sister chromatid, unlike homologous recombination",
 "ak-artemis": "- In V(D)J recombination, Artemis opens the RAG-made hairpins",
 "ak-ds-break": "- V(D)J recombination uses NHEJ to join the broken ends",
 "ak-hr-cromatide": "- So it works only in dividing cells",
 "ak-hr-fiel": "- NHEJ, by contrast, loses or adds nucleotides",
 "ak-reparo-scid": "- Defects in V(D)J joining enzymes (RAG, Artemis) block B and T development",
 "ak-ataxia": "- ATM senses double-strand breaks",
 "ak-desaminacao": "- AID does this on purpose in the variable regions of activated B cells",
 "ak-ber-desaminacao": "- In hypermutation, error-prone repair of the uracil adds mutations",
 "ak-glicosilase": "- Translesion polymerases fill the abasic site with random bases",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (V–J, RSS, junção, AID) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula (Alberts, Watson), sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "bm18-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {"au-desafio": "ganho: o problema numérico (10^7 anticorpos × 25 mil genes) que motiva a recombinação; os sh descrevem o mecanismo"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "bm18-vj.png": "Lâmina 11: junção V–J da cadeia kappa (DNA germinativo → DNA do B → transcrito → splicing → mRNA → cadeia leve); verso de au-irreversivel.",
 "bm18-rss.png": "Lâmina 13: sequências sinal (heptâmero, espaçador 12/23, nonâmero) e seu arranjo nos loci H, κ e λ; verso de au-regra-12-23.",
 "bm18-juncional.png": "Lâmina 17: abertura do grampo, nucleotídeos P e N (TdT), aparo e junção; verso de au-juncional.",
 "bm18-aid.png": "Lâmina 22: AID desamina C em U, par U:G, glicosilase, sítio abásico e polimerases translesão; verso de au-aid.",
}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (17 notas novas, 21 cards; frentes, clozes, versos, imagens e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Explicar como a recombinação V(D)J, a diversidade juncional, a combinação H/L e a hipermutação somática geram a diversidade "
             "de anticorpos, incluindo RSS/RAG, JNHE, exclusão alélica, AID e a troca de classe.",
 "centrais": [
   ("desafio", "au-desafio", "sh-1791629589120"),
   ("recombinação", "au-irreversivel", "sh-1791629589672"),
   ("RSS", "au-regra-12-23", "sh-1791629589372"),
   ("hipermutação", "au-aid", "ak-glicosilase"),
   ("troca de classe", "au-troca-dna", "sh-1791629594096"),
 ],
 "exemplos": ["mieloma múltiplo (um clone)", "nocaute de RAG", "cálculo 35×5 e 40×23×6"],
 "outras_aulas": [("estrutura e classes de Ig", "17 Reconhecimento adaptativo"), ("SCID e hiper-IgM", "51 Distúrbios do SI (sh)"),
                  ("reparo do DNA", "85 Telômeros e reparo"), ("tolerância central", "imunologia")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
