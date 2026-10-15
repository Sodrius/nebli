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
    {1: R}, B_, "Kappa antes de lambda", "14", "lateral", NAO, EP, "Rosa: transcrição III; proporção (revisão 15/10).",
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
    {1: R}, C_, "Recombinação homóloga", "19", "lateral", NAO, EP, "Rosa: lâmina 19; contraste com NHEJ, reparo é de outra aula (revisão 15/10).",
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
    {1: R}, D_, "Glicosilase e síntese translesão", "22", "lateral", NAO, EP, "Rosa: lâmina 22; transcrição IV (revisão 15/10)."),
 sh(1791629594472, "verde", D_, "Hipermutação e maturação de afinidade", "22", "Verde: lâmina 22; prova 2023; viva na aula 49."),
 au("d-troca", "<b>Class switching</b> deletes DNA between switch regions to change the heavy-chain {{c1::constant}} region, keeping the same antigen specificity",
    G(1), D_, "Troca de classe", "23", "central", NAO, EP, "Verde: lâmina 23 (não gera diversidade).",
    extra="- Also depends on AID"),
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
   ("hipermutação e troca", "sh-1791629595072", "d-uracila", "d-translesao", "sh-1791629594472", "d-troca"),
 ],
 "exemplos": ["vírus da pólio e epítopos", "mieloma múltiplo", "Tonegawa (Nobel 1987)"],
 "outras_aulas": [("ativação de linfócitos B", "49"), ("NHEJ e CRISPR", "54 RNAs não codificadores"), ("tolerância", "17 Reconhecimento adaptativo")],
}
_M2 = "Completude 15/10: quatro transcrições inventariadas (F-20261015-CLAUDE-04)."
CARDS.append(au("a-genes-diversidade", "Humans make about 10^7–10^8 different <b>antibodies</b> with only about 25,000 protein-coding genes, so receptor diversity must be generated by {{c1::somatic recombination}}",
    G(1), A_, "O desafio: genes demais seriam necessários", "4", "central", NAO, EP, "Verde: lâmina 4 e transcrição I (o problema que a aula resolve). " + _M2,
    extra="- A ready-made gene for each antibody could never anticipate new pathogens"))
CARDS.append(au("a-um-clone", "Each <b>B cell</b> makes antibody of a single specificity, as shown by the one dominant immunoglobulin of {{c1::multiple myeloma}}",
    {1: Z}, A_, "Um linfócito, um anticorpo", "6", "central", NAO, EP, "Azul: transcrição I (o mieloma prova a especialização); conexão com o pico M. " + _M2,
    extra="- The tumor is the clonal expansion of one plasma cell"))
CARDS.append(au("b-transposons", "<b>RAG1 and RAG2</b> work like transposases, suggesting that V(D)J recombination evolved from {{c1::transposons}}",
    {1: R}, B_, "Origem evolutiva", "16", "lateral", NAO, EP, "Rosa: transcrições I e III. " + _M2))
CARDS.append(au("d-autorreativos", "Random V(D)J joining inevitably creates some <b>self-reactive B cells</b>, and their removal in the bone marrow is called {{c1::central tolerance}}",
    {1: Z}, D_, "Conexão: recombinação aleatória → tolerância", "25", "central", NAO, EP, "Azul: lâmina 25 e transcrição IV (consequência indesejada; auditoria pediu conexão curta). " + _M2,
    extra="- When it fails, autoimmune diseases such as type 1 diabetes or lupus can arise"))
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    if _c_["key"] == "b-transposons": _c_["extra"] = "- Transposon enzymes also cut DNA at specific signal sequences and rejoin the ends"
# Ajuste 15/10 noite (F-20261015-CLAUDE-05): Abbas Básica cap. 4 (produção de receptores diversos; maturação B) lido;
# apostila guia Imuno Aula 4 e monitoria P1 aula 4 conferidas.
_M3 = "Ajuste 15/10 noite (F-20261015-CLAUDE-05)."
CARDS += [
 au("a-tres-loci", "<b>Immunoglobulins</b> are encoded by three loci on different chromosomes, one for the heavy chain and two for the κ and {{c1::λ}} light chains",
    {1: Z}, A_, "Três loci de Ig", "8", "central", NAO, EP, "Azul: monitoria P1 aula 4 e apostila guia Aula 4 cap. 1. " + _M3,
    extra="- Each B cell uses only one light-chain type, κ or λ"),
 au("b-ordem-cadeias", "Developing <b>B cells</b> rearrange the {{c1::heavy::heavy/light}} chain first, at the pro-B stage, and only then the light chain",
    {1: Z}, B_, "Pesada antes da leve", "11", "central", NAO, EP, "Azul: apostila guia Aula 4 cap. 1 e Abbas cap. 4 (pró-B → pré-B → B imatura). " + _M3,
    extra="- The light chain lacks D segments, so it needs a single V–J join"),
 sh(1791629587148, "rosa", B_, "Pré-B: μ citoplasmático", "11", "Rosa: Abbas cap. 4 (estágios de maturação B); viva na 49. " + _M3),
 au("b-pre-bcr", "In <b>pre-B cells</b> the μ heavy chain pairs with a {{c1::surrogate light chain}}, forming the pre-BCR that checks the heavy chain works",
    {1: Z}, B_, "Pré-BCR: primeiro ponto de controle", "14", "central", "consultas surrogate/pre-BCR sem card (15/10 noite).", EP, "Azul: Abbas cap. 4 (pré-BCR, primeiro ponto de controle, exclusão alélica). " + _M3,
    extra="- The same signal stops heavy-chain rearrangement on the other allele and starts κ rearrangement"),
 au("b-splicing", "After <b>V(D)J joining</b>, RNA {{c1::splicing}} removes the intron between the J segment and the constant-region exon",
    {1: Z}, B_, "Splicing une VDJ à região C", "11", "central", NAO, EP, "Azul: monitoria P1 aula 4 e Abbas fig. 4-11. " + _M3,
    extra="- The DNA between V, D and J is deleted; the J–C intron is removed only in the RNA"),
 au("b-heptamero", "<b>RAG</b> cuts DNA exactly at the edge of the {{c1::heptamer}}, while the nonamer serves as its binding site",
    {1: R}, B_, "Heptâmero = corte; nonâmero = ligação", "13", "lateral", NAO, EP, "Rosa: apostila guia Aula 4 cap. 3. " + _M3,
    extra="- The 12- or 23-bp spacer between them enforces the 12/23 rule"),
 au("c-exonuclease", "Besides added P and N nucleotides, {{c1::exonucleases}} trim bases from the <b>coding ends</b>, adding to junctional diversity",
    {1: R}, C_, "Exonucleases na diversidade juncional", "17", "lateral", NAO, EP, "Rosa: Abbas cap. 4 (três alterações na junção) e apostila guia Aula 4 cap. 3. " + _M3,
    extra="- Junctional changes concentrate variability in CDR3"),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
CARDS.append(au("a-policlonal", "Because most <b>antigens</b> carry several epitopes, the normal antibody response is {{c1::polyclonal}}, unlike the single clone of myeloma",
    {1: Z}, A_, "Resposta policlonal", "7", "central", NAO, EP, "Azul: exercício 8 (gp120 do HIV: mono ou policlonal?) e UC3.pdf p. 127. " + _M3,
    extra="- Each clone recognizes one epitope of the antigen"))
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    if _c_["key"] == "ak-mieloma": _c_["clinica_lateral"] = "mieloma é a prova histórica de um clone = um anticorpo; doença é da Pato/hemato"
