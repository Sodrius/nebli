# Especificação curada — 54 RNAs não codificadores (UC03 P3, Biologia Molecular; Prof. Alexandre Bruni-Cardoso; 86 lâminas). Pipeline v8
# (23/10): cada autoral nasce de uma motivação congelada na E3 (motivacoes.json); o AnKing entra onde responde ao mapa.
# História: o RNA regula porque dobra e porque pareia. Em bactéria o próprio transcrito muda de forma (atenuação do trp, riboswitch) e o
# CRISPR usa um RNA-guia em trans, com o reparo decidindo entre nocaute e edição. Em eucariotos, dsRNA vira siRNA pela Dicer e guia o
# RISC a cortar o mRNA (forte, recicla); o miRNA usa a mesma via com pareamento imperfeito (muitos alvos, modula). O Xist, RNA longo,
# recobre o X que o transcreve e traz repressores: heterocromatina herdada, fêmeas mosaicas.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 8
SECOES_MOTIVO = ""
SECOES_DA_AULA = [
    "_FirstAid_01_Biochem_03_Laboratory_Techniques_10_Gene_expression_modifications_01_RNA_interference_MicroRNA.txt",
    "_FirstAid_01_Biochem_03_Laboratory_Techniques_10_Gene_expression_modifications_01_RNA_interference_Small_Interfering_RNA.txt",
    "_FirstAid_01_Biochem_03_Laboratory_Techniques_02_CRISPR_Cas9.txt",
    "_Bootcamp_Genetics_05_Laboratory_Techniques_02_CRISPR_Cas9.txt",
    "_FirstAid_01_Biochem_04_Genetics_05_Modes_of_inheritance_04_X_linked_dominant_Lyonization.txt",
]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-bm54-20261023a"
SHORT = "bm54"
LESSON = "2026-uc03-biologia-molecular-54-rnas-nao-codificadores"
DECK = "NEBLI::UC03::P3::Biologia Molecular::RNAs não codificadores"
CRITERIOS = "MEMORY.md + pipeline v8 (EXECUCAO-DECK-AULA) + FEEDBACKS até F-20261023-CLAUDE-04 + GUIA_CARDS.md de 23/10"
MEDIA = {}
BUSCA = ("Três caminhos (23/10): seções de recurso do AnKing (RNA interference, CRISPR/Cas9, Lyonization, Gene expression, Chromatin; busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em AnKing, acervos externos e NEBLI vivo, uma consulta por "
         "motivação (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


EXCLUIDOS = [
 (1520274742115, "repete 1469146766774 (metilação de citosina na lionização)"),
 (1520275652643, "localização do corpúsculo de Barr na periferia do núcleo: detalhe de citologia fora do que a aula ensina"),
 (1467927108504, "mRNA guardado no corpo P para tradução futura: a aula mostra o corpo P só como destino de degradação"),
 (1719432902825, "repete 1467927177492 (miRNA silencia mRNA)"),
 (1554354487069, "frameshift genérico (MCAT): a cadeia indel → quadro de leitura está no card autoral do NHEJ"),
 (1468549155531, "palíndromo de sítios de restrição: clonagem, fora da aula"),
 (1468549185535, "clonagem molecular: outra aula de técnicas"),
 (1468549189226, "clonagem molecular: outra aula de técnicas"),
 (1468549192518, "clonagem molecular: outra aula de técnicas"),
 (1468549196500, "clonagem molecular: outra aula de técnicas"),
 (1468549202187, "clonagem molecular: outra aula de técnicas"),
]
FORA_DO_RECORTE = [
 "miR-31 e metástase de câncer de mama (versão anterior da aula, lâminas 77–81): fora das lâminas de 2026; o princípio (miRNA reduz vários alvos, supressor se os alvos promovem metástase) fica no AnKing de miRNA e câncer.",
 "Patisiran, Nobel 2006, 2020 e 2024, livro de Doudna: motivação histórica das lâminas 18, 20, 24 e 32.",
 "Repressor do trp e sistema Gal4: 29 Operon e 46/52 Eucariotos.",
 "Imunologia do interferon em detalhe: 63 Resposta imune aos vírus; aqui só o porquê de usar siRNA curto em mamíferos.",
]
A_, B_, C_, D_, E_, F_ = "A-rna-regula", "B-procariotos-cis", "C-crispr", "D-sirna", "E-mirna", "F-xist"

CARDS = [
 # ---------- Por que o RNA regula (lâmina 4) ----------
 au("au-rna-regula", ORG("<b>Regulatory RNAs</b> act by<br>- {{c1::folding}} (riboswitch)<br>- {{c1::base pairing}} (siRNA)<br>- {{c1::scaffolding}} (Xist)"),
    "V-pilar", A_, "Dobra, pareamento e arcabouço", 4, "lâminas 2–5; transcrição; prova 2024 P3 2.8 (como ncRNAs regulam)", motivacao="m1",
    organizador=True, extra="RNA is single-stranded, so it folds into shapes that proteins and small molecules recognize.<br>It is still a nucleic acid, so it pairs with a complementary RNA or DNA.<br>A long RNA can also hold proteins together on chromatin, like a scaffold."),
 # ---------- Atenuação do trp (lâminas 7–9) ----------
 K(1467833424428, "V-hy", B_, "Terminador: grampo rico em GC", 9, "lâmina 9 (grampo terminador da atenuação é um terminador de transcrição de procarioto)"),
 au("au-trp-alto", "When <b>tryptophan</b> is high, the ribosome reads the leader fast, so the {{c1::terminator}} hairpin forms and transcription {{c2::stops}}",
    "V-pilar", B_, "Trp alto: ribossomo rápido, grampo 3:4, para", 9, "lâminas 7–9; transcrição", motivacao="m2",
    extra="A fast ribosome covers region 2 of the leader, so regions 3 and 4 pair into a GC-rich stem followed by a run of U's, the classic bacterial terminator.<br>Plenty of tryptophan means the trp genes are not needed, so stopping early saves energy."),
 au("au-trp-baixo", "When <b>tryptophan</b> is low, the ribosome {{c1::stalls}} at the Trp codons, so the 2:3 hairpin forms and transcription {{c2::continues}}",
    "A-aula", B_, "Trp baixo: ribossomo parado, grampo 2:3, segue", 9, "lâminas 8–9; transcrição", motivacao="m3",
    extra="A stalled ribosome leaves region 2 free to pair with region 3, so 3:4 cannot form.<br>The 2:3 hairpin is not a terminator, so RNA polymerase goes on to transcribe the trp genes that make more tryptophan."),
 au("au-trp-acoplada", "Eukaryotes cannot use <b>attenuation</b>, because transcription is in the {{c1::nucleus}} and translation in the {{c2::cytoplasm}}",
    "A-aula", B_, "Atenuação exige transcrição e tradução acopladas", 9, "lâminas 8–9; transcrição", motivacao="m4",
    extra="In bacteria the ribosome follows RNA polymerase and translates the leader while it is still being made, and that timing is what lets the ribosome choose the hairpin.<br>With a nuclear envelope, the ribosome never meets the nascent leader."),
 # ---------- Riboswitch (lâmina 11) ----------
 au("au-riboswitch", "A <b>riboswitch</b> changes shape when a {{c1::small molecule}} binds it, hiding the {{c2::Shine-Dalgarno}} sequence",
    "A-aula", B_, "Riboswitch: molécula pequena muda a dobra", 11, "lâmina 11; transcrição", motivacao="m5",
    extra="With the Shine-Dalgarno hidden, the ribosome cannot start translation, so the gene is switched off.<br>Other riboswitches form a terminator instead, which stops transcription.<br>The RNA senses the metabolite itself, with no regulatory protein, as the SAM riboswitch does."),
 # ---------- CRISPR (lâminas 13–17) ----------
 au("au-crispr-memoria", "CRISPR <b>spacers</b> are stored {{c1::phage}} DNA, and their RNA copies guide {{c2::Cas}} to cut the virus on reinfection",
    "A-aula", C_, "CRISPR é a memória imune da bactéria", 13, "lâminas 13–14; transcrição", motivacao="m6",
    extra="Each new infection adds a spacer at one end of the array, so the array is a ledger of past exposures in order.<br>The crRNA pairs with the tracrRNA and loads Cas9, an endonuclease that cuts the matching DNA."),
 K(1519849478653, "A-aula", C_, "CRISPR/Cas9 como ferramenta", 16, "lâmina 16 (edição genética com CRISPR/Cas9)"),
 K(1519849576725, "A-aula", C_, "Cas9 + RNA-guia", 15, "lâmina 15 (sgRNA leva a Cas9 ao DNA complementar)"),
 au("au-crispr-pam", "<b>Cas9</b> cuts only where the 20-nt guide pairs with DNA that sits next to a {{c1::PAM}}",
    "A-aula", C_, "PAM limita onde a Cas9 corta", 16, "lâmina 16; transcrição", motivacao="m7",
    extra="PAM stands for protospacer adjacent motif, and Cas9 needs it to open the DNA next to the target.<br>Changing the guide sequence retargets Cas9, so one new sgRNA is designed for each gene to edit."),
 K(1519849762394, "A-aula", C_, "NHEJ repara o corte e dá nocaute", 16, "lâmina 16 (NHEJ → nocaute)"),
 K(1516938350345, "V-hy", C_, "NHEJ é propenso a erro", 16, "lâmina 16 (NHEJ gera indel porque não há molde)"),
 au("au-crispr-nhej", "<b>NHEJ</b> repair of a Cas9 cut leaves {{c1::indels}} that shift the reading frame, so the gene is {{c2::knocked out}}",
    "V-pilar", C_, "Indel → quadro de leitura → nocaute", 16, "lâmina 16; transcrição; exercício 5", motivacao="m8",
    extra="A shifted reading frame usually creates a premature stop codon, so the protein is truncated and loses function.<br>Cutting near the start codon makes this loss of function more likely, which is why knockouts target the beginning of the gene."),
 K(1519850675647, "A-aula", C_, "Molde de reparo → edição precisa", 16, "lâmina 16 (HDR com molde)"),
 K(1516937730893, "A-aula", C_, "Recombinação homóloga não é propensa a erro", 16, "lâmina 16 (HDR dá edição precisa)"),
 # ---------- RNAi por siRNA (lâminas 20–24) ----------
 K(1468605745938, "A-aula", D_, "RNAi: dsRNA complementar silencia o gene", 20, "lâmina 20 (definição de RNAi)"),
 au("au-fire-mello", "Silencing is triggered by {{c1::double-stranded}} RNA, since in <b>C. elegans</b> the sense or antisense strand alone did nothing",
    "A-aula", D_, "Só a dupla fita silencia (Fire e Mello)", 21, "lâmina 21; transcrição", motivacao="m10",
    extra="Worms injected with the duplex twitched like mutants of the muscle protein, while the single strands did nothing.<br>So the trigger is the duplex, which the cell then processes into siRNAs."),
 au("au-sirna-via", "{{c1::Dicer}} cuts <b>dsRNA</b> into ~21-bp siRNAs, and RISC uses one strand to guide {{c2::Argonaute}} to cut the matching mRNA",
    "V-pilar", D_, "Dicer → RISC → Argonauta", 22, "lâmina 22; transcrição", motivacao="m11",
    extra="The other strand, called the passenger, is discarded, so the strand that stays is the guide.<br>Argonaute cuts only when the pairing is perfect, which is what separates siRNA from miRNA."),
 K(1728260304903, "A-aula", D_, "siRNA: pareamento perfeito, degradação", 22, "lâmina 22 (siRNA corta o mRNA complementar)",
   fields_override={"Extra": "A miRNA is <i>endogenous</i> and pairs imperfectly, so the binding itself silences expression.<br>A siRNA is <i>exogenous</i> and pairs perfectly, so it recruits RISC, which cleaves the target mRNA."}),
 au("au-sirna-recicla", "After cleavage, <b>RISC</b> is {{c1::released}} to cut other mRNAs, so one siRNA silences {{c2::many}} copies",
    "A-aula", D_, "mRNA cortado é degradado e o RISC é reciclado", 22, "lâmina 22; transcrição", motivacao="m12",
    extra="The cut mRNA lacks its cap or its poly-A tail, so exonucleases degrade it.<br>Because the RISC is recycled, one siRNA can silence many copies, which is why siRNA silencing is strong."),
 au("au-dicer-mutante", "In a <b>Dicer</b> mutant, long dsRNA fails because it is never {{c1::processed}} into siRNAs",
    "A-aula", D_, "Mutante dicer: dsRNA longo não age, siRNA curto sim", 22, "lâmina 22; exercício 4 (bicoid e dicer)", motivacao="m13",
    extra="Short siRNAs injected directly still silence the gene, because they bypass Dicer.<br>In normal embryos, bicoid dsRNA gives the bicoid mutant phenotype, because the dsRNA is processed into siRNAs."),
 au("au-interferon-dsrna", "In <b>mammals</b>, long dsRNA triggers an {{c1::interferon}} response that halts translation, so RNAi uses short siRNAs",
    "A-aula", D_, "Em mamíferos, dsRNA longo dispara interferon", 23, "lâmina 23; transcrição (lâmina 63 da versão anterior)", motivacao="m14",
    extra="Long dsRNA looks like viral RNA to the cell: PKR stops protein synthesis and RNase L degrades mRNA.<br>siRNAs of about 21 bp escape this alarm, so they silence one gene without shutting the cell down."),
 K(1497450277629, "R-detalhe", D_, "dsRNA viral → interferon", 23, "lâmina 23 (fala: dsRNA longo lido como vírus)"),
 au("au-knockdown", "<b>RNAi</b> lowers mRNA levels ({{c1::knockdown}}), whereas <b>CRISPR/NHEJ</b> damages the gene itself ({{c1::knockout}})",
    "A-aula", D_, "Knockdown × nocaute", 23, "lâminas 16 e 23; transcrição", motivacao="m15",
    extra="A siRNA delivered in a liposome is transient, whereas a lentiviral shRNA integrated in the genome silences permanently.<br>Knockdown leaves some protein, so the phenotype can be milder than a knockout."),
 au("au-rnai-defesa", "Natural <b>siRNAs</b> come mainly from viral dsRNA and active {{c1::transposons}}, so RNAi works as a cell {{c2::defense}}",
    "R-detalhe", D_, "siRNAs naturais: vírus e transposons", 24, "lâminas 64–66 (versão anterior); transcrição; Alberts cap. 7", motivacao="m24",
    extra="Endogenous siRNAs that degrade host mRNAs are rare.<br>The same Dicer and RISC machinery serves miRNAs, which are encoded in the genome."),
 # ---------- miRNA (lâminas 25–30) ----------
 K(1467927177492, "A-aula", E_, "miRNA: RNA pequeno não codificador", 25, "lâmina 25 (definição de miRNA)"),
 au("au-mirna-biogenese", "The <b>pri-miRNA</b> hairpin is cut by {{c1::Drosha}} in the nucleus and by {{c2::Dicer}} in the cytoplasm",
    "A-aula", E_, "Drosha no núcleo, Dicer no citoplasma", 27, "lâminas 26–28; transcrição; prova 2019 P4 1.2", motivacao="m16",
    extra="Between the two cuts, exportin 5 carries the pre-miRNA of about 70 nt to the cytoplasm.<br>Because miRNA genes code no protein, they can sit inside introns or in polycistronic clusters."),
 K(1467927184068, "A-aula", E_, "miRNA silencia o mRNA", 28, "lâmina 28 (miRNA reprime a tradução ou degrada)"),
 au("au-mirna-imperfeito", "A <b>miRNA</b> that pairs imperfectly with the 3′ UTR does not trigger cutting, and RISC {{c1::represses translation}} instead",
    "V-pilar", E_, "Pareamento imperfeito: reprime a tradução", 29, "lâminas 28–29; transcrição; prova 2025 P3 1.6", motivacao="m17",
    extra="Perfect pairing, as in plants and with siRNA, activates Argonaute cleavage.<br>The repressed mRNA is sent to P-bodies and later degraded."),
 K(1467927104082, "R-detalhe", E_, "Corpos P: degradação final", 30, "lâmina 30 (miRNA leva o mRNA ao corpo P)"),
 K(1467927192491, "A-aula", E_, "miRNA anormal e câncer", 29, "prova 2019 P4 1.3; lâmina 29 (muitos alvos)"),
 au("au-mirna-sirna", "A <b>miRNA</b> pairs {{c1::imperfectly}} and tunes many targets, whereas a <b>siRNA</b> pairs {{c1::perfectly}} and silences one strongly",
    "A-aula", E_, "miRNA modula muitos alvos; siRNA silencia um", 30, "lâmina 30; transcrição; objetivo 2 da aula", motivacao="m18",
    extra="A miRNA-RISC stays bound to its mRNA, one to one, so it only tunes expression.<br>A siRNA-RISC is recycled, so it silences strongly.<br>Because one miRNA has many targets, predicting them is hard."),
 # ---------- Xist e inativação do X (lâminas 34–41) ----------
 au("au-x-mosaico", "A female <b>embryo</b> cell silences one X-chromosome {{c1::at random}} and passes it on, so females are {{c2::mosaics}}",
    "A-aula", F_, "Inativação aleatória e herdada: mosaico", 36, "lâminas 35–36; transcrição; Alberts cap. 7", motivacao="m19",
    extra="The X is inactivated at about the 32 to 64 cell stage.<br>Each patch of adult tissue descends from a cell that silenced the same X."),
 K(1469146766774, "V-hy", F_, "Lionização: X condensado, heterocromatina", 36, "lâmina 36 (um X inativado e condensado)"),
 K(1469146770793, "V-hy", F_, "Corpúsculo de Barr = lionização", 36, "lâmina 36 (nome da inativação do X)"),
 au("au-x-portadora", "Because <b>X-inactivation</b> is random, a heterozygous {{c1::carrier}} of an X-linked mutation may be {{c2::asymptomatic}}",
    "A-aula", F_, "Portadora heterozigota assintomática; calico", 37, "lâminas 37–38; transcrição", motivacao="m20",
    extra="Enough cells silence the mutant X to keep normal function.<br>Calico cats are female for the same reason: the patches show which X is active."),
 au("au-xist", "<b>Xist</b> RNA stays on the X-chromosome that transcribes it and recruits {{c1::Polycomb}} complexes, so that chromosome is {{c2::silenced}}",
    "V-pilar", F_, "Xist recobre o próprio X e recruta repressores", 39, "lâminas 34 e 39; transcrição; exercício 6c; prova 2024 P3 2.8", motivacao="m21",
    extra="Xist is a long noncoding RNA of about 20 kb that acts as a scaffold: it coats the X through an anchoring protein, not by base pairing.<br>Unlike siRNA or miRNA, it needs no target RNA."),
 au("au-xi-marcas", "The inactive <b>X-chromosome</b> loses histone {{c1::acetylation}} and gains {{c2::methylation}}, so its chromatin becomes compact",
    "A-aula", F_, "Xi: menos acetilação, mais metilação de H3", 41, "lâminas 40–41; transcrição; exercício 6c", motivacao="m22",
    extra="The marks are copied to daughter cells, so the X stays silent without Xist.<br>Hypoacetylated, methylated chromatin is heterochromatin."),
 K(1467682194916, "V-hy", F_, "Corpúsculo de Barr é heterocromatina", 41, "lâmina 41 (Xi compacto)"),
 au("au-xist-posicional", "<b>XIST</b> inserted into one extra chromosome 21 would {{c1::silence}} it, because XIST acts on the chromosome that makes it",
    "A-aula", F_, "Efeito posicional: Xist silencia o cromossomo que o carrega", 39, "lâmina 39; exercício 6a (XIST na trissomia 21)", motivacao="m23",
    extra="The same effect silences an autosome in which an X-inactivation center has been inserted.<br>The silenced copy gains the inactive-X marks: low acetylation, high methylation."),
]
for c in CARDS:
    if c["kind"] == "autoral":
        c["text"] = _re.sub(r"\{\{c(\d+)::(.*?)((?:::[^}]*)?)\}\}", lambda m: "{{c%s::<b>%s</b>%s}}" % (m.group(1), m.group(2), m.group(3)), c["text"])

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1467833424428": "In attenuation this hairpin sits in the leader RNA, and with high tryptophan it ends transcription before the trp genes.",
 "ak1519849576725": "The sgRNA is one RNA that fuses the crRNA and the tracrRNA, so only its 20-nt guide has to be redesigned for a new target.",
 "ak1519849762394": "Without NHEJ or homologous repair the cut would be lethal, so the repair pathway is what makes editing possible.",
 "ak1468605745938": "The cell uses Dicer and RISC for this, and delivered in a liposome it is transient, a knockdown.",
 "ak1467927192491": "Example: miR-31 falls as breast cancer becomes metastatic, so it acts as a tumor suppressor.",
 "ak1497450277629": "The cell reads cytosolic viral dsRNA as an infection, so interferon-induced enzymes shut down the infected cell.",
 "ak1467927104082": "Here the mRNA held by a miRNA-RISC is kept away from ribosomes, decapped and degraded.",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {
 "au-trp-acoplada": "ganho: nucleus e cytoplasm são respostas de outros assuntos no AnKing; aqui a consequência, que eucarioto não atenua",
 "au-xi-marcas": "ganho: o AnKing dá a metilação de citosina da lionização; aqui as marcas de histona do X inativo, que a lâmina 40 pergunta",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {"objetivo": "Entender como RNAs não codificadores regulam a expressão (dobra, pareamento, arcabouço): atenuação e riboswitch, CRISPR, RNAi por siRNA e miRNA, e o Xist na inativação do X.",
          "centrais": [
           ["RNA regula por dobra, pareamento e arcabouço", "au-rna-regula"],
           ["atenuação do trp", "au-trp-alto"],
           ["CRISPR: guia e reparo", "au-crispr-nhej"],
           ["via do siRNA", "au-sirna-via"],
           ["miRNA", "au-mirna-imperfeito"],
           ["inativação do X", "au-xist"]],
          "exemplos": ["au-riboswitch", "au-fire-mello", "au-x-portadora", "au-xist-posicional"],
          "outras_aulas": ["29 Operon em procariotos", "46 Expressão em eucariotos I", "52 Expressão em eucariotos II", "18 Recombinação"]}
import re as _r2
CARDS.sort(key=lambda c: int(_r2.search(r"\d+", c["evid"]).group()))
