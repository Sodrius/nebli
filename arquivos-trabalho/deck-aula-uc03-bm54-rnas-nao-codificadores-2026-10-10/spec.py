# Especificação curada — RNAs não codificadores (UC03 P3, Biologia Molecular; Prof. Alexandre Bruni-Cardoso; 42 + 44 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-bm54-20261010a"
SHORT = "bm54"
LESSON = "2026-uc03-biologia-molecular-54-rnas-nao-codificadores"
DECK = "NEBLI::UC03::P3::Biologia Molecular::RNAs não codificadores"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-02) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 28 consultas; busca/ext.txt), 10/10: ")
EXCLUIDOS = [
 (1467927108504, "mRNA armazenado em P-bodies: a aula mostra só Argonauta e DCP1a nos P-bodies"),
 (1520274742115, "metilação do DNA na lionização: repete metilacao-citosina"),
 (1520275652643, "Barr body na periferia do núcleo: não citado"),
 (1516937730893, "recombinação homóloga sem erro: aula foca o molde no knock-in"),
 (1467682246440, "acetilação ativa transcrição: já no deck de Eucariotos I; aqui o card do X inativo"),
 (1487550541119, "TTR familiar: o patisiran entra como card próprio"),
]
FORA_DO_RECORTE = ["prêmios Nobel e links (lâminas 18, 20, 31–32, 51)", "detalhes do reparo de DNA (aula de Telômeros e reparo)", "amiloidose além do alvo do patisiran"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_, G_ = ("A-visao-geral", "B-atenuacao", "C-riboswitch", "D-crispr", "E-rnai-sirna", "F-mirna", "G-lncrna-xist")
CARDS = [
 # ---------- A. Visão geral (slides 2–6) ----------
 ak("mirna-def", 1467927177492, {1: V}, A_, "miRNA é RNA não codificador regulatório", 2, "Verde: definição que abre a aula (lâminas 2, 30, 67)."),
 au("pareamento", "Regulatory RNAs find their targets by {{c1::base pairing}} with complementary RNA or DNA", {1: Z}, A_,
    "RNA reconhece alvo por pareamento", "4, 45", "central", "consultas noncoding/RNAi sem card geral.", [1467927177492, 1468605745938], "Azul: lâmina 4."),
 au("cis", "Attenuation and riboswitches act in {{c1::cis}}, through folding of the transcript itself", {1: Z}, A_,
    "Procariotos: regulação em cis", "6, 10, 46", "central", "sem card nos acervos.", [1467927177492, 1468605745938], "Azul: esquema das lâminas 6 e 19."),
 au("trans", "CRISPR RNAs, siRNAs and miRNAs act in {{c1::trans}}, by pairing with other nucleic acids", {1: Z}, A_,
    "Regulação em trans", "6, 19, 48", "central", "sem card nos acervos.", [1519849576725, 1468605745938], "Azul: lâminas 6 e 19."),
 # ---------- B. Atenuação do operon trp (slides 7–9) ----------
 au("trp-atenuacao", "Besides its repressor, the trp operon is controlled by {{c1::attenuation}}", {1: Z}, B_,
    "Operon trp: repressor e atenuação", "7; Watson cap. 20", "central", "consultas trp operon/attenuation sem card.", [1468605745938, 1467927177492], "Azul: lâmina 7."),
 au("trp-alto", "When tryptophan is high, the ribosome quickly finishes the leader peptide and a {{c1::terminator}} hairpin stops transcription", {1: V}, B_,
    "Trp alto: grampo terminador", "9", "central", "sem card nos acervos.", [1468605745938, 1467927177492],
    "Verde: mecanismo central da atenuação.", extra="- The terminator is the 3:4 stem-loop"),
 au("trp-baixo", "When tryptophan is low, the ribosome stalls at the leader Trp codons and an alternative {{c1::antiterminator}} hairpin forms", {1: Z}, B_,
    "Trp baixo: antiterminador", "9", "central", "sem card nos acervos.", [1468605745938, 1467927177492],
    "Azul: lâmina 9.", extra="- The 2:3 stem-loop lets RNA polymerase continue into the trp genes"),
 au("acoplamento", "Attenuation works only because bacterial transcription and {{c1::translation}} are coupled", {1: R}, B_,
    "Acoplamento transcrição-tradução", "9; Watson cap. 20", "lateral", "sem card nos acervos.", [1468605745938, 1467927177492],
    "Rosa: aprofundamento da lâmina 9.", extra="- The ribosome translates the leader while the RNA is still being made"),
 # ---------- C. Riboswitches (slide 11) ----------
 au("riboswitch", "{{c1::Riboswitches}} are 5′ UTR structures that change shape when they bind a small molecule", {1: V}, C_,
    "Riboswitch", "3, 11", "central", "consulta riboswitch* sem card.", [1467927177492, 1468605745938],
    "Verde: segundo mecanismo em cis.", extra="- Example: a riboswitch that binds SAM"),
 au("riboswitch-rbs", "A riboswitch can block translation by folding over the {{c1::ribosome-binding site}}", {1: Z}, C_,
    "Riboswitch na tradução", "11", "central", "sem card nos acervos.", [1467927177492, 1468605745938],
    "Azul: lâmina 11.", extra="- Other riboswitches form a transcriptional terminator instead"),
 # ---------- D. CRISPR (slides 13–17) ----------
 au("crispr-imune", "In bacteria, CRISPR keeps pieces of {{c1::phage}} DNA so the cell can destroy the same virus on reinfection", {1: V}, D_,
    "CRISPR como imunidade bacteriana", "13, 49", "central", "AnKing trata CRISPR só como ferramenta.", [1519849478653, 1519849576725], "Verde: lâmina 13."),
 au("espacadores", "Bits of phage DNA from earlier infections are stored as spacers between the {{c1::repeats}} of the CRISPR locus", {1: Z}, D_,
    "Espaçadores entre repetições", "13", "central", "sem card nos acervos.", [1519849478653, 1519849576725],
    "Azul: lâmina 13.", extra="- They are transcribed into crRNAs that guide Cas to the matching DNA"),
 au("tracrrna", "In natural CRISPR, the crRNA pairs with a second RNA, the {{c1::tracrRNA}}, to load Cas9", {1: Z}, D_,
    "crRNA + tracrRNA", "14–15", "central", "sem card nos acervos.", [1519849576725, 1519849478653], "Azul: lâminas 14–15."),
 au("sgrna", "In the lab, crRNA and tracrRNA are fused into one {{c1::single-guide}} RNA", {1: Z}, D_,
    "sgRNA", "15", "central", "sem card nos acervos.", [1519849576725, 1519849478653], "Azul: lâmina 15."),
 ak("crispr-ferramenta", 1519849478653, {1: V}, D_, "CRISPR/Cas9 edita genomas", 16, "Verde: lâmina 16."),
 ak("cas9-guia", 1519849576725, {1: V, 2: V}, D_, "Cas9 + RNA guia", 16, "Verdes: núcleo da ferramenta."),
 au("pam", "Cas9 cuts only next to a short {{c1::PAM}} sequence in the target DNA", {1: Z}, D_,
    "PAM", "16", "central", "consulta 'protospacer' sem card.", [1519849576725, 1519849478653],
    "Azul: lâmina 16.", extra="- Protospacer adjacent motif"),
 ak("nhej-knockout", 1519849762394, {1: Z}, D_, "NHEJ repara o corte → knockout", 16, "Azul: lâmina 16 e exercício 5."),
 ak("nhej-erro", 1516938350345, {1: V}, D_, "NHEJ é sujeito a erro", 16, "Verde: HY; explica as indels do knockout."),
 ak("molde-knockin", 1519850675647, {1: Z}, D_, "Molde de reparo para knock-in", 16, "Azul: lâmina 16 e exercício 5."),
 au("falciforme", "The first approved CRISPR therapy (2023) edits patients' blood stem cells to treat {{c1::sickle cell}} disease", {1: R}, D_,
    "Terapia CRISPR na anemia falciforme", "17", "lateral", "consultas exagamglogene/Casgevy sem card.", [1519849478653, 1519849576725], "Rosa: lâmina 17."),
 # ---------- E. RNAi e siRNA (slides 20–24, 53–66) ----------
 ak("rnai", 1468605745938, {1: V, 2: Z}, E_, "RNAi faz knockdown", 20, "Verde c1 (objetivo 1 da aula), azul c2. Extra corrigido: o AnKing atribuía a repressão parcial a bloquear 'transcription factor binding'.",
    extra="- In cells, Dicer cuts the dsRNA and RISC degrades the target mRNA<br>- An exact match usually degrades the mRNA; a partial match represses its translation"),
 au("fire-mello", "Fire and Mello silenced a C. elegans muscle gene only when they injected {{c1::double-stranded}} RNA, not either strand alone", {1: V}, E_,
    "Experimento de Fire e Mello", "21, 53, 55", "central", "sem card nos acervos.", [1468605745938, 1467927177492],
    "Verde: experimento fundador; exercício 4.", extra="- The worms twitched like muscle-protein mutants"),
 au("dicer", "{{c1::Dicer}} cuts double-stranded RNA into short duplexes of about 21 bp", {1: V}, E_,
    "Dicer gera siRNA", "22, 28, 56; exercício 4", "central", "consulta Dicer só achou o card de RNAi.", [1468605745938, 1467927184068],
    "Verde: passo central da via; exercício 4 (mutante dicer).", extra="- Dicer is an RNase III; siRNAs are about 21 bp and miRNA duplexes about 22 nt"),
 au("risc-fita", "RISC discards the {{c1::sense}} strand of the siRNA and keeps the antisense strand as a guide", {1: Z}, E_,
    "RISC mantém a fita guia", "22, 56", "central", "consulta RISC sem card.", [1468605745938, 1467927184068], "Azul: lâmina 22."),
 au("argonauta", "When the guide pairs perfectly with an mRNA, the RISC protein {{c1::Argonaute}} cleaves it", {1: V}, E_,
    "Argonauta cliva com pareamento perfeito", "22, 56, 71", "prova", "consulta argonaute sem card.", [1467927184068, 1468605745938],
    "Verde: prova 2025 P3 1.6.", extra="- The mRNA is then degraded"),
 au("interferon", "In mammalian cells, long dsRNA triggers an {{c1::interferon}} response that blocks all translation", {1: Z}, E_,
    "dsRNA longo em mamíferos", "62–63", "central", "consulta dsRNA interferon sem card.", [1468605745938, 1467927184068],
    "Azul: lâmina 63.", extra="- That is why short siRNAs, not long dsRNA, are used in mammalian cells"),
 au("sirna-origem", "Natural siRNAs come mainly from viral infection and active {{c1::transposons}}", {1: R}, E_,
    "Origem dos siRNAs naturais", "65", "lateral", "sem card nos acervos.", [1468605745938, 1467927177492], "Rosa: lâmina 65."),
 au("patisiran", "Patisiran, the first approved siRNA drug, silences {{c1::transthyretin}} in hereditary amyloidosis", {1: R}, E_,
    "Patisiran", "24", "lateral", "consulta patisiran sem card.", [1468605745938, 1487550541119],
    "Rosa: lâmina 24.", extra="- Approved in 2018 for the polyneuropathy of hATTR"),
 # ---------- F. miRNA (slides 25–30, 67–81) ----------
 au("sirna-mirna", "siRNAs come from long exogenous dsRNA, whereas miRNAs come from genome-encoded {{c1::hairpin}} transcripts", {1: V}, F_,
    "Origem: siRNA × miRNA", "25–26, 30, 67, 74", "central", "AnKing não compara siRNA e miRNA.", [1467927177492, 1468605745938],
    "Verde: objetivo 2 da aula.", extra="- Both then share Dicer and RISC"),
 au("lin4", "The first miRNA, lin-4, was found in {{c1::C. elegans}}, where it represses lin-14 during larval development", {1: R}, F_,
    "lin-4", "25, 29", "lateral", "sem card nos acervos.", [1467927177492, 1467927184068], "Rosa: lâmina 25."),
 au("muitos-alvos", "A single miRNA usually regulates {{c1::many}} target mRNAs", {1: Z}, F_,
    "miRNA tem muitos alvos", "25, 29, 73", "central", "sem card nos acervos.", [1467927177492, 1467927184068],
    "Azul: lâminas 25 e 29.", extra="- miRNAs regulate over 60% of human mRNAs"),
 au("drosha", "In the nucleus, {{c1::Drosha}} cuts the pri-miRNA into a ~70-nt pre-miRNA hairpin", {1: V}, F_,
    "Drosha", "27, 69; prova 2019 P4 1.2", "prova", "consulta Drosha sem card.", [1467927177492, 1467927184068], "Verde: biogênese cobrada em 2019."),
 au("exportina", "The pre-miRNA leaves the nucleus through {{c1::exportin 5}}", {1: Z}, F_,
    "Exportina 5", "27, 69", "central", "consulta 'exportin 5' sem card.", [1467927177492, 1467927184068],
    "Azul: lâmina 27.", extra="- Drosha acts in the nucleus; Dicer acts in the cytoplasm"),
 ak("mirna-silencia", 1467927184068, {1: Z}, F_, "miRNA silencia e reduz tradução", 28, "Azul: lâmina 28."),
 au("imperfeito", "Imperfect pairing between miRNA and mRNA makes RISC {{c1::repress translation}} instead of cutting the mRNA", {1: V}, F_,
    "Pareamento imperfeito reprime tradução", "29, 72; prova 2025 P3 1.6", "prova", "AnKing diz só 'silencing'.", [1467927184068, 1467927177492],
    "Verde: prova 2025.", extra="- In plants, miRNAs pair perfectly and cleave"),
 au("utr3", "Animal miRNAs usually bind sites in the target mRNA {{c1::3′ UTR}}", {1: Z}, F_,
    "Sítios na 3'-UTR", "29, 80; prova 2024 P3 2.9", "prova", "sem card nos acervos.", [1467927184068, 1467927177492],
    "Azul: lâminas 29 e 80.", extra="- Reporter genes carrying the 3′ UTR test a candidate target"),
 au("recicla", "After cutting an mRNA, siRNA–RISC is {{c1::recycled}}, whereas miRNA–RISC stays bound to its mRNA", {1: R}, F_,
    "RISC reciclado × associado", "75", "lateral", "sem card nos acervos.", [1467927184068, 1468605745938], "Rosa: lâmina 75."),
 ak("p-bodies", 1467927104082, {1: R}, F_, "P-bodies", 76, "Rosa: lâmina 76 (Argonauta e DCP1a)."),
 ak("mirna-cancer", 1467927192491, {1: Z}, F_, "miRNAs alterados em neoplasias", 77, "Azul: lâmina 77."),
 au("mir31", "In breast cancer cell lines, miR-31 levels fall as cells become more {{c1::metastatic}}", {1: Z}, F_,
    "miR-31 inverso à metástase", "78; prova 2019 P4", "prova", "consulta 'miR-31' sem card.", [1467927192491, 1467927184068], "Azul: lâmina 78."),
 au("mir31-supressor", "miR-31 acts as a {{c1::tumor suppressor}}, blocking metastasis by repressing motility genes such as RhoA", {1: V}, F_,
    "miR-31 supressor de metástase", "79–81; prova 2019 P4 1.3", "prova", "sem card nos acervos.", [1467927192491, 1467927184068],
    "Verde: prova 2019.", extra="- Reactivating miR-31 can reverse metastases in mice"),
 # ---------- G. lncRNAs e Xist (slides 33–41, 82–86) ----------
 au("lnc-200", "Long noncoding RNAs are defined as longer than {{c1::200}} nucleotides", {1: Z}, G_,
    "lncRNA > 200 nt", "34", "central", "consulta lncRNA sem card.", [1467927177492, 1469146770793], "Azul: lâmina 34."),
 au("lnc-scaffold", "Many lncRNAs act as {{c1::scaffolds}} that bring proteins together on DNA or chromatin", {1: Z}, G_,
    "lncRNA como arcabouço", "4, 34, 83; prova 2024 P3 2.8", "prova", "sem card nos acervos.", [1467927177492, 1469146770793], "Azul: prova 2024."),
 au("dose", "{{c1::X inactivation}} solves the dosage imbalance of two X chromosomes in female mammals", {1: V}, G_,
    "Compensação de dose", "35, 83", "central", "consulta 'dosage compensation' sem card.", [1469146770793, 1469146766774], "Verde: por que o X é inativado."),
 au("aleatoria", "In the early embryo, which X is inactivated is chosen {{c1::randomly}}, and the choice is kept in all daughter cells", {1: V}, G_,
    "Inativação aleatória e herdada", "36, 83", "central", "AnKing não diz que a escolha é aleatória.", [1469146770793, 1469146766774],
    "Verde: lâmina 36.", extra="- About the 32–64-cell stage"),
 au("mosaico", "Because of random X inactivation, adult females are genetic {{c1::mosaics}}", {1: Z}, G_,
    "Fêmeas são mosaicos", "36, 83", "central", "sem card nos acervos.", [1469146770793, 1469146766774], "Azul: lâmina 36."),
 au("portadoras", "Mosaicism explains why heterozygous carriers of X-linked mutations may be {{c1::asymptomatic}}", {1: Z}, G_,
    "Portadoras assintomáticas", "37, 83", "central", "sem card nos acervos.", [1469146770793, 1469146766774],
    "Azul: lâmina 37.", extra="- Example: carriers of color blindness"),
 au("calico", "Calico cats are almost always {{c1::female}}", {1: R}, G_,
    "Gato calico", "38", "lateral", "consulta calico sem card.", [1469146770793, 1469146766774],
    "Rosa: lâmina 38.", extra="- The fur color gene is on the X, so patches show which X is active"),
 au("xist", "X inactivation is driven by the long noncoding RNA {{c1::Xist}}", {1: V}, G_,
    "Xist", "39, 84", "central", "consultas XIST sem card do lncRNA.", [1469146770793, 1469146766774],
    "Verde: exemplo central da aula.", extra="- About 20 kb long"),
 au("xist-recobre", "Xist is transcribed from the X that will be inactivated and {{c1::coats}} that same chromosome", {1: V}, G_,
    "Xist recobre o X inativo", "39, 84", "central", "sem card nos acervos.", [1469146770793, 1467682194916],
    "Verde: lâmina 39.", extra="- It then recruits chromatin-modifying proteins"),
 au("xi-histonas", "The inactive X has low histone {{c1::acetylation}} and high histone methylation", {1: V}, G_,
    "Marcas do X inativo", "40–41, 85–86; prova 2024 P3 2.10", "prova", "AnKing tem acetilação geral, não do X inativo.", [1467682194916, 1469146766774],
    "Verde: pergunta da aula e prova 2024.", extra="- Hypoacetylated, methylated chromatin is compact heterochromatin"),
 ak("lionizacao", 1469146770793, {1: V}, G_, "Corpúsculo de Barr = lionização", 41, "Verde: HY; nome do fenômeno. Extra corrigido: o AnKing dizia 'day 16 in the blastocyst'; a aula dá 32–64 células.",
    extra="- Occurs early in embryogenesis, at about the 32–64-cell stage<br>- It is both random and fixed in somatic cells"),
 ak("metilacao-citosina", 1469146766774, {1: V}, G_, "Metilação de citosina no X inativo", 41, "Verde: HY; marca do DNA do X inativo. Extra reescrito: o AnKing dizia que os dois X expressam Xist; a aula diz que Xist sai do X a inativar.",
    extra="- Xist RNA, made by the X that will be silenced, coats it and recruits chromatin-silencing proteins<br>- The silenced X becomes a Barr body"),
 ak("barr-heterocromatina", 1467682194916, {1: V}, G_, "Corpúsculo de Barr é heterocromatina", 41, "Verde: HY."),
 au("xist-down", "Inserting XIST into one extra chromosome has been proposed as a way to silence trisomy {{c1::21}}", {1: R}, G_,
    "XIST na trissomia 21", "41; exercício 6", "lateral", "sem card nos acervos.", [1469146770793, 1467682194916], "Rosa: exercício 6 da turma."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {'pareamento': '- RNAs can also fold into functional 3D structures and recruit proteins to chromatin',
 'lnc-scaffold': '- Xist is the example: it brings repressive complexes to the X chromosome',
 'cis': '- Regulation in cis acts on the same molecule that carries the signal',
 'trans': '- They are separate RNAs that find a different target',
 'trp-atenuacao': '- The repressor acts at the operator; attenuation acts on the leader RNA',
 'crispr-imune': '- It works like an adaptive immune system of bacteria',
 'tracrrna': '- The crRNA gives specificity; the tracrRNA binds Cas9',
 'sgrna': '- Changing the 20-nt guide retargets Cas9 to any DNA sequence',
 'falciforme': '- Edited stem cells are returned to the bone marrow and make healthy red cells',
 'risc-fita': '- The antisense strand is complementary to the target mRNA',
 'lin4': '- Discovered by Ambros and Ruvkun in 1993',
 'drosha': '- Drosha is an RNase III, like Dicer',
 'lnc-200': '- Many are spliced, and some come from the antisense strand of a coding gene',
 'dose': '- Without it, X-linked genes would be expressed twice as much in females',
 'mosaico': '- Each patch descends from a cell that silenced the same X',
 'xist-down': '- The targeted chromosome would gain inactive-X marks: low acetylation, high methylation',
 'sirna-origem': '- Endogenous siRNAs that degrade mRNAs are rare compared with miRNAs',
 'recicla': '- Cleavage frees the siRNA–RISC to find another mRNA',
 'mirna-cancer': '- Example: loss of miR-31 in metastatic breast cancer',
 'mir31': '- Measured by RT-PCR across non-tumorigenic, tumorigenic and metastatic lines'}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
DUPLICACAO = {}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
