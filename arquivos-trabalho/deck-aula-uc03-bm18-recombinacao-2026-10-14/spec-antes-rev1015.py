# Especificação curada — Geração de diversidade de anticorpos por recombinação (UC03 P1, Biologia molecular; Prof. Alexandre Bruni-Cardoso; 25 lâminas, 4 vídeos).
# A aula 49 (Ativação de linfócitos B) já tem estrutura da Ig, RAG, V(D)J da cadeia pesada, AID e hipermutação: entram por sh(). Esta aula acrescenta o mecanismo molecular.
RUN_ID = "uc03-bm18-20261014a"
SHORT = "bm18"
LESSON = "2026-uc03-biologia-molecular-18-recombinacao"
DECK = "NEBLI::UC03::P1::Biologia Molecular::Recombinação V(D)J"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (RAG, TdT, Artemis, recombination signal, allelic exclusion, Ku70, kappa light chain, Fab, Fc region, variable region, hypervariable, "
         "multiple myeloma M spike, SCID, Omenn, AID, class switching, NHEJ, uracil glycosylase, translesion; busca/anking*.txt) e cópias NEBLI vivas da aula 49 e da 54, 14/10: ")
EXCLUIDOS = [
 (1516938209170, "ATM e complexo MRN no NHEJ: detalhe de reparo além da aula; Artemis vai em autoral"),
 (1496110744913, "razão kappa:lambda 3:1 em tecido: a aula dá ~60% kappa no soro; card autoral segue a aula"),
 (1480564160094, "TdT como marcador de leucemia linfoblástica: hematologia"),
]
FORA_DO_RECORTE = ["Tolerância central em detalhe: aulas de Imunologia (17 Reconhecimento adaptativo).", "Diferenças funcionais entre classes de Ig (lâmina 10, tabela): aula 49 e Imunologia."]


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
NAO = "o AnKing não tem este passo molecular como card."
EP = [1486945114357, 1486945028810, 1486945095844]
A_, B_, C_, D_ = "A-desafio-e-estrutura", "B-recombinacao-VDJ", "C-reparo-e-diversidade-juncional", "D-hipermutacao-e-troca"

CARDS = [
 # A — desafio e estrutura (3–10)
 au("a-epitopo", "The part of an <b>antigen</b> bound by an antibody, usually 10–12 amino acids of a protein, is the {{c1::epitope}}",
    G(1), A_, "Epítopo", "5; exercício 1", "central", NAO, EP, "Verde: lâmina 5; exercício 1.",
    extra="- We can make roughly 10⁷–10⁸ different antibodies"),
 au("a-diversidade", ORG("Sources of <b>antibody diversity</b>:<br>1. {{c1::combinatorial}} joining of V(D)J segments<br>2. pairing of heavy and light chains<br>3. {{c2::junctional}} diversity from imprecise joining<br>4. {{c3::somatic hypermutation}} after antigen contact"),
    G(1, 2, 3), A_, "Mecanismos de diversidade", "9; 24; prova 2018 P1 1.14", "prova", NAO, EP, "Verde: lâmina 24; prova 2018.",
    extra="- The genome has only ~25,000 genes, so antibodies cannot each have their own gene<br>- Class switching changes function, not diversity"),
 ak("ak-mieloma", 1481335848197, {1: Z}, A_, "Mieloma: pico monoclonal", "7; 6", "Azul: transcrição I (mieloma prova que cada linfócito faz um anticorpo).",
    extra_add="- Most serum antibody is a single species, from one expanded plasma cell clone<br>- So each B cell makes antibody of one specificity"),
 sh(1791629588145, "verde", A_, "Duas cadeias pesadas e duas leves", "8", "Verde: lâmina 8; viva na aula 49."),
 sh(1791629588272, "azul", A_, "Idiotipo no Fab", "8", "Azul: lâmina 8 (região variável); viva na aula 49."),
 sh(1791629588447, "azul", A_, "Isotipo no Fc", "10", "Azul: lâmina 10 (região constante define a classe); viva na aula 49."),
 # B — recombinação V(D)J (11–16)
 sh(1791629589247, "verde", B_, "V(D)J antes do antígeno", "11", "Verde: lâmina 11; viva na aula 49."),
 au("b-d", "<b>Light-chain</b> variable regions are built from V and J segments, while heavy chains also use {{c1::D (diversity)}} segments",
    G(1), B_, "Segmentos V, D e J", "11; 12", "central", NAO, EP, "Verde: lâminas 11–12; transcrição II.",
    extra="- Kappa: ~35–76 V × 5 J; heavy chain: ~40 V × 23 D × 6 J"),
 sh(1791629589497, "verde", B_, "V(D)J na cadeia pesada", "11", "Verde: lâmina 11; viva na aula 49."),
 sh(1791629589672, "verde", B_, "D–J antes de V–DJ", "11", "Verde: transcrição II; viva na aula 49."),
 au("b-enhancer", "Joining <b>V to J</b> deletes the DNA in between and brings the V promoter close to the {{c1::enhancer}}, allowing efficient transcription",
    {1: Z}, B_, "Promotor e enhancer", "11", "central", NAO, EP, "Azul: transcrição II.",
    extra="- The deletion makes the choice irreversible"),
 au("b-cmu", "A newly rearranged <b>heavy chain</b> is first transcribed with the {{c1::Cμ}} constant region, so the first antibody a B cell makes is IgM",
    {1: Z}, B_, "Primeira Ig é IgM", "11; 23", "central", NAO, EP, "Azul: transcrição II (parada de transcrição após Cμ)."),
 sh(1791629589120, "azul", B_, "Combinação aleatória de cadeias", "12", "Azul: lâmina 12; viva na aula 49."),
 au("b-rss", "Each <b>recombination signal sequence</b> has a conserved heptamer and {{c1::nonamer}} separated by a 12- or 23-bp spacer",
    {1: Z}, B_, "Sequências sinal", "13; prova 2024 P1 1.6", "prova", NAO, EP, "Azul: lâmina 13; prova 2024.",
    extra="- The spacer sequence is random; only its length matters"),
 au("b-12-23", "By the {{c1::12/23}} rule, a <b>signal sequence</b> with a 12-bp spacer joins only one with a 23-bp spacer, so V never joins V",
    G(1), B_, "Regra 12/23", "13; prova 2024 P1 1.6; exercício 4", "prova", NAO, EP, "Verde: lâmina 13; prova 2024; exercício 4.",
    extra="- In the heavy chain, D is flanked by 12-bp spacers and V and J by 23-bp spacers"),
 au("b-exclusao", "Once one <b>allele</b> makes a functional chain, rearrangement of the other allele stops, a process called {{c1::allelic exclusion}}",
    G(1), B_, "Exclusão alélica", "14", "central", NAO, EP, "Verde: lâmina 14; transcrição III.",
    extra="- Each B cell therefore expresses a single antibody specificity<br>- If the first allele fails, the second can still try"),
 au("b-kappa", "The {{c1::kappa::kappa/lambda}} <b>light-chain</b> locus rearranges first, which is why about 60% of antibodies carry kappa chains",
    {1: Z}, B_, "Kappa antes de lambda", "14", "central", NAO, EP, "Azul: transcrição III.",
    extra="- Lambda rearranges only if both kappa alleles fail"),
 sh(1791629589372, "verde", B_, "RAG1 e RAG2", "15", "Verde: lâmina 15; viva na aula 49."),
 au("b-rag2", "<b>RAG1</b> binds the signal sequence and recruits RAG2, the partner with {{c1::endonuclease}} activity that nicks the DNA",
    {1: Z}, B_, "Papel de RAG1 e RAG2", "15; 16", "central", NAO, EP, "Azul: lâminas 15–16; transcrição III; prova 2024.",
    extra="- Cutting needs both paired signals together in a recombination synapse"),
 au("b-grampo", "After the <b>RAG</b> nick, the free 3′-OH attacks the opposite strand and seals each coding end into a {{c1::hairpin}}",
    {1: Z}, B_, "Formação do grampo", "15; 16", "central", NAO, EP, "Azul: lâminas 15–16.",
    extra="- This creates a double-strand break; the excised signal segment is circularized and discarded"),
 au("b-scid", "Animals lacking <b>RAG1 or RAG2</b> make neither B nor T cells, causing {{c1::severe combined immunodeficiency}}",
    {1: Z}, B_, "Nocaute de RAG", "15", "central", NAO, EP, "Azul: transcrição III.",
    extra="- RAG enzymes evolved from transposon proteins"),
 # C — reparo e diversidade juncional (17–21)
 au("c-homologa", "<b>Homologous recombination</b> repairs double-strand breaks without errors but needs the {{c1::sister chromatid}} as template",
    {1: Z}, C_, "Recombinação homóloga", "19", "central", NAO, EP, "Azul: lâmina 19; transcrição III.",
    extra="- In non-dividing cells, error-prone NHEJ is used instead"),
 sh(1791630175220, "verde", C_, "NHEJ é propenso a erro", "20", "Verde: lâmina 20; viva na aula 54."),
 au("c-ku", "In <b>NHEJ</b>, {{c1::Ku}} proteins bind the broken DNA ends and recruit nucleases, polymerases and DNA ligase",
    {1: Z}, C_, "Proteínas Ku", "20", "central", NAO, EP, "Azul: lâmina 20."),
 au("c-artemis", "The {{c1::Artemis}} endonuclease opens the <b>coding-end hairpins</b> off-center, creating palindromic P nucleotides",
    {1: Z}, C_, "Artemis e nucleotídeos P", "21; 17", "central", NAO, EP, "Azul: lâmina 17; transcrição III."),
 ak("ak-tdt", 1486945114357, G(1), C_, "TdT e nucleotídeos N", "21; 17", "Verde: lâmina 17; prova 2018."),
 au("c-quadro", "<b>Junctional</b> insertions or deletions that are not a multiple of {{c1::3}} shift the reading frame, so many rearrangements are nonproductive",
    G(1), C_, "Rearranjos não produtivos", "25; 17", "central", NAO, EP, "Verde: lâmina 25; transcrição IV.",
    extra="- B cells that never make a functional receptor die in the bone marrow"),
 # D — hipermutação e troca de classe (22–25)
 sh(1791629595072, "verde", D_, "AID", "22", "Verde: lâmina 22; viva na aula 49."),
 au("d-uracila", "<b>AID</b> deaminates cytosine to {{c1::uracil}} in the variable-region DNA, creating a mismatch opposite guanine",
    G(1), D_, "AID gera uracila", "22; prova 2023 P1 2.8", "prova", NAO, EP, "Verde: lâmina 22; prova 2023.",
    extra="- If not repaired, replication turns it into a C→T mutation"),
 au("d-translesao", "<b>Uracil DNA glycosylase</b> removes the uracil, and error-prone {{c1::translesion}} polymerases fill the abasic site with any base",
    {1: Z}, D_, "Glicosilase e síntese translesão", "22", "central", NAO, EP, "Azul: lâmina 22; transcrição IV."),
 sh(1791629594472, "verde", D_, "Hipermutação e maturação de afinidade", "22", "Verde: lâmina 22; prova 2023; viva na aula 49."),
 au("d-troca", "<b>Class switching</b> deletes DNA between switch regions to change the heavy-chain {{c1::constant}} region, keeping the same antigen specificity",
    G(1), D_, "Troca de classe", "23", "central", NAO, EP, "Verde: lâmina 23 (não gera diversidade).",
    extra="- Also depends on AID"),
 au("d-tolerancia", "Failure to remove <b>self-reactive B cells</b> in the bone marrow, a breakdown of {{c1::tolerance}}, causes autoimmune disease",
    {1: Z}, D_, "Autorreatividade e tolerância", "25", "central", NAO, EP, "Azul: lâmina 25; transcrição IV.",
    extra="- Examples: type 1 diabetes, rheumatoid arthritis, lupus"),
]
SEM_IMAGEM = "passo molecular sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {"c-ku": "- Ku bridges the two ends", "c-artemis": "- Exonucleases may also remove nucleotides", "ak-tdt": "- It adds N nucleotides without a template",
         "d-translesao": "- Translesion polymerases are low-processivity, so mutations stay local", "b-cmu": "- Switching to IgG, IgE or IgA comes later, after antigen"}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if VERSO.get(k):
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Explicar como poucos genes geram ~10⁸ anticorpos: segmentos V(D)J, regra 12/23, RAG1/2, reparo por NHEJ com diversidade juncional (Artemis, TdT), exclusão alélica, hipermutação somática por AID e troca de classe, e as consequências (rearranjos não produtivos, autorreatividade).",
 "centrais": [
   ("desafio e estrutura", "a-epitopo", "a-diversidade", "ak-mieloma", "sh-1791629588145", "sh-1791629588272", "sh-1791629588447"),
   ("recombinação V(D)J", "sh-1791629589247", "b-d", "sh-1791629589497", "sh-1791629589672", "b-enhancer", "b-cmu", "sh-1791629589120", "b-rss", "b-12-23", "b-exclusao", "b-kappa",
    "sh-1791629589372", "b-rag2", "b-grampo", "b-scid"),
   ("reparo e diversidade juncional", "c-homologa", "sh-1791630175220", "c-ku", "c-artemis", "ak-tdt", "c-quadro"),
   ("hipermutação e troca", "sh-1791629595072", "d-uracila", "d-translesao", "sh-1791629594472", "d-troca", "d-tolerancia"),
 ],
 "exemplos": ["vírus da pólio e epítopos", "mieloma múltiplo", "Tonegawa (Nobel 1987)"],
 "outras_aulas": [("ativação de linfócitos B", "49"), ("NHEJ e CRISPR", "54 RNAs não codificadores"), ("tolerância", "17 Reconhecimento adaptativo")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
