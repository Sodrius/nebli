# Especificação curada — Regulação da expressão gênica em eucariotos II (UC03 P3, Biologia Molecular; Prof. Bruni-Cardoso; 53 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-bm52-20261010a"
SHORT = "bm52"
LESSON = "2026-uc03-biologia-molecular-52-expressao-eucariotos-ii"
DECK = "NEBLI::UC03::P3::Biologia Molecular::Expressão gênica em eucariotos II"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-02) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt), seções FirstAid de estrutura da cromatina, metilação, acetilação e HDACi (busca/tags-secao.txt), 10/10: ")
EXCLUIDOS = [
 (1495600999571, "histona acetilada desenrola o DNA: repete acetil-carga e o card compartilhado"),
 (1467682210281, "nucleossomo sem H1 = 10 nm: o card do nucleossomo já diz 10 nm"),
 (1467682233616, "imprinting: não tratado na aula"),
 (1467682225986, "metilação no reparo de procariotos: fora da aula"),
 (1467682203692, "heterocromatina como maior empacotamento: repete hetero-condensada"),
]
FORA_DO_RECORTE = ["imprinting (Prader-Willi/Angelman)", "detalhes de drogas epigenéticas além dos HDACi", "link de vídeo"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_ = ("A-cromatina", "B-remodeladores", "C-modificacoes-covalentes", "D-silenciamento", "E-epigenetica")
CARDS = [
 # ---------- A. Estrutura da cromatina (slides 2–10) ----------
 au("basal-restritivo", "Unlike bacteria, the basal state of eukaryotic transcription is {{c1::restrictive}}, because DNA is packed in chromatin", {1: V}, A_,
    "Estado basal restritivo", "3; transcrição; monitoria", "central", "sem card nos acervos.", [1467680889892, 1467682246440],
    "Verde: ideia que abre a aula.", extra="- Regulatory sites must be uncovered before transcription"),
 ak("nucleossomo", 1467680889892, {1: V, 2: Z}, A_, "Nucleossomo e fibra de 10 nm", 4, "Verde c1, azul c2; lâminas 4–5."),
 ak("fibra-30", 1467682218464, {1: Z}, A_, "Fibra de 30 nm com H1", 4, "Azul: lâmina 4."),
 ak("octamero", 1467682119151, {1: Z}, A_, "Pares de H2A, H2B, H3, H4", 6, "Azul: lâminas 6–7."),
 ak("h1", 1467682112238, {1: Z}, A_, "H1 de ligação", 8, "Azul: lâmina 8."),
 ak("lisina-arginina", 1467682100570, {1: Z}, A_, "Histonas ricas em lisina e arginina", 9, "Azul: lâmina 9."),
 au("caudas", "Histone N-terminal {{c1::tails}} are needed to fold nucleosomes into the 30-nm fiber", {1: Z}, A_,
    "Caudas e fibra de 30 nm", "10; monitoria", "central", "sem card nos acervos.", [1467682218464, 1467680889892],
    "Azul: lâmina 10.", extra="- They also stabilize DNA wrapping around the octamer"),
 # ---------- B. Remodeladores (slides 12–17) ----------
 au("tf-remodelador", "Some activators bind closed chromatin and then recruit {{c1::remodeling}} complexes that expose nearby sites", {1: Z}, B_,
    "Fator de transcrição recruta remodelador", "13–14", "central", "sem card nos acervos.", [1467682246440, 1467680889892],
    "Azul: lâmina 13.", extra="- Factors can also bind right after replication, before nucleosomes reform"),
 au("remodelador-atp", "Nucleosome remodeling complexes slide, transfer or loosen nucleosomes using energy from {{c1::ATP}}", {1: V}, B_,
    "Remodeladores dependentes de ATP", "15–16; objetivo 1; monitoria", "central", "sem card nos acervos.", [1467680889892, 1467682246440], "Verde: objetivo 1 da aula."),
 au("pol-desaloja", "As RNA polymerase transcribes a gene, histone octamers are displaced and then reassemble {{c1::behind}} it", {1: R}, B_,
    "Transcrição desaloja nucleossomos", "17", "lateral", "sem card nos acervos.", [1467680889892, 1467682246440], "Rosa: lâmina 17."),
 # ---------- C. Modificações covalentes (slides 18–30) ----------
 au("hat", "{{c1::Histone acetyltransferases}} (HATs) acetylate the ε-amino group of lysines in histone tails", {1: V}, C_,
    "HAT", "19–20; objetivo 2", "central", "AnKing não nomeia HAT.", [1467682246440, 1495601106573], "Verde: objetivo 2."),
 au("hdac", "{{c1::Histone deacetylases}} (HDACs) remove acetyl groups from histone lysines", {1: Z}, C_,
    "HDAC", "19–20; objetivo 2", "central", "AnKing cita HDAC só nos inibidores.", [1495601106573, 1495601288347], "Azul: irmão recíproco de hat."),
 sh(1791627547302, "verde", C_, "Acetilação ativa a transcrição", 22, "Verde: nota já existente de Eucariotos I."),
 au("acetil-carga", "Acetylation neutralizes the positive charge of lysine, lowering histone affinity for {{c1::DNA}}", {1: V}, C_,
    "Por que acetilação descompacta", "21–22; monitoria; prova 2024 P3 2.10", "prova", "AnKing dá o efeito, não o mecanismo.", [1467682246440, 1495601106573],
    "Verde: pergunta da lâmina 21.", extra="- It also weakens contacts between adjacent nucleosomes"),
 ak("desacetilada", 1495601106573, {1: V, 2: Z}, C_, "Desacetilação compacta", 22, "Verde c1 (HY), azul c2."),
 au("outras-mod", "Besides acetylation, histone tails can be methylated and {{c1::phosphorylated}}", {1: Z}, C_,
    "Metilação e fosforilação de histonas", "23–24", "central", "sem card nos acervos.", [1467682246440, 1495601106573], "Azul: lâmina 23."),
 au("codigo", "The {{c1::histone code}} hypothesis says that combinations of tail modifications set a chromatin region's function", {1: V}, C_,
    "Código de histonas", "27; objetivo 3; monitoria", "central", "sem card nos acervos.", [1467682246440, 1495601106573], "Verde: objetivo 3."),
 au("leitores", "Histone marks recruit {{c1::reader}} proteins that recognize specific modifications", {1: Z}, C_,
    "Proteínas leitoras", "26–27", "central", "sem card nos acervos.", [1467682246440, 1495601106573],
    "Azul: lâmina 26.", extra="- Bromodomains read acetylated lysines"),
 au("ativador-cromatina", "Besides the transcription machinery, activators recruit HATs and nucleosome {{c1::remodeling}} complexes", {1: Z}, C_,
    "Ativadores abrem a cromatina", "28–29; objetivo 4", "central", "sem card nos acervos.", [1467682246440, 1495601106573],
    "Azul: lâmina 29.", duplicacao_ok="ganho: tf-remodelador é a ligação à cromatina fechada; aqui é o que o ativador recruta junto da maquinaria"),
 au("ho-swi5", "At the yeast HO gene, Swi5 opens chromatin so that a second activator, {{c1::SBF}}, can bind", {1: R}, C_,
    "Swi5 e SBF no gene HO", "29; objetivo 4; monitoria", "lateral", "sem card nos acervos.", [1467682246440, 1495601106573],
    "Rosa: exemplo do objetivo 4.", extra="- Swi5 recruits a remodeler and a HAT; SBF then recruits the machinery"),
 au("repressor-cromatina", "Repressors favor chromatin {{c1::condensation}} by recruiting histone deacetylases", {1: Z}, C_,
    "Repressores compactam", "30", "central", "sem card nos acervos.", [1495601106573, 1467682246440], "Azul: lâmina 30."),
 # ---------- D. Silenciamento: heterocromatina e metilação do DNA (slides 31–40) ----------
 sh(1791627547178, "verde", D_, "Heterocromatina é inativa", 32, "Verde: nota já existente de Eucariotos I."),
 ak("hetero-condensada", 1467682160443, {1: V}, D_, "Heterocromatina condensada", 32, "Verde: HY; lâmina 32."),
 au("constitutiva", "{{c1::Constitutive}} heterochromatin stays condensed in every cell, as at centromeres and repeats", {1: Z}, D_,
    "Heterocromatina constitutiva", "32; monitoria", "central", "sem card nos acervos.", [1467682160443, 1467682184880], "Azul: lâmina 32."),
 au("facultativa", "Facultative heterochromatin depends on cell type or cycle phase, as in the inactive {{c1::X}} chromosome", {1: Z}, D_,
    "Heterocromatina facultativa", "32", "central", "sem card nos acervos.", [1467682160443, 1467682184880], "Azul: lâmina 32."),
 ak("hetero-me", 1467682168594, {1: V}, D_, "Heterocromatina escura na ME", 33, "Verde: HY; lâmina 33."),
 ak("eucromatina-me", 1467682176839, {1: Z}, D_, "Eucromatina clara na ME", 33, "Azul: HY recíproco de hetero-me (F-20261010-CLAUDE-03).", hy_repete="hetero-me"),
 au("hp1", "Methylated histone H3 recruits {{c1::HP1}}, which self-associates and packs chromatin into heterochromatin", {1: V}, D_,
    "Metilação de H3 e HP1", "34, 40; objetivo 5; transcrição", "central", "sem card nos acervos.", [1467682184880, 1467682160443],
    "Verde: objetivo 5.", extra="- HP1 binds methyl-lysine through its chromodomain"),
 au("dnmt", "{{c1::DNA methyltransferases}} add a methyl group from SAM to cytosine, making 5-methylcytosine", {1: Z}, D_,
    "DNMT e 5-metilcitosina", "35", "central", "sem card nos acervos.", [1467682230375, 1467682246440], "Azul: lâmina 35."),
 ak("cpg-reprime", 1467682230375, {1: V, 2: V, 3: Z}, D_, "Metilação de CpG reprime", 38, "Verdes c1–c2, azul c3; objetivo 5."),
 au("ilhas-cpg", "CpG islands, usually unmethylated, are concentrated in gene {{c1::promoters}}", {1: V}, D_,
    "Ilhas CpG nos promotores", "36–37", "central", "sem card nos acervos.", [1467682230375, 1467682246440], "Verde: lâmina 36."),
 au("cpg-80", "About {{c1::80%}} of CpG dinucleotides in the mammalian genome are methylated", {1: R}, D_,
    "~80% dos CpG metilados", "37", "lateral", "sem card nos acervos.", [1467682230375, 1467682246440], "Rosa: lâmina 37."),
 au("dna-hdac", "Methylated cytosines silence genes by recruiting histone deacetylases and nucleosome {{c1::remodelers}}", {1: Z}, D_,
    "Citosinas metiladas recrutam HDAC", "39; transcrição", "central", "sem card nos acervos.", [1467682230375, 1495601106573],
    "Azul: lâmina 39.", duplicacao_ok="ganho: liga metilação do DNA à desacetilação; ativador-cromatina trata do recrutamento por ativadores"),
 # ---------- E. Epigenética (slides 41–52; iPS da transcrição) ----------
 au("epigenetica", "Epigenetic marks are passed on through cell {{c1::divisions}} without changing the DNA sequence", {1: V}, E_,
    "Definição de epigenética", "42–44; prova 2025 P3 1.5", "prova", "sem card de definição.", [1467682230375, 1467682246440],
    "Verde: lâmina 42.", extra="- Main carriers: histone modifications and DNA methylation"),
 au("manutencao", "After replication, a {{c1::maintenance}} DNA methyltransferase copies methylation onto the new strand", {1: V}, E_,
    "DNMT de manutenção", "45–46", "central", "sem card nos acervos.", [1467682230375, 1467682246440],
    "Verde: como a marca é herdada.", extra="- It recognizes hemimethylated CpG"),
 au("gemeos", "Identical twins accumulate DNA methylation {{c1::differences}} as they age", {1: R}, E_,
    "Gêmeos monozigóticos", "47", "lateral", "sem card nos acervos.", [1467682230375, 1467682246440], "Rosa: lâmina 47."),
 au("abelha", "Royal jelly lowers Dnmt3 activity, so honeybee larvae develop into {{c1::queens}}", {1: R}, E_,
    "Abelha rainha", "48–49", "lateral", "sem card nos acervos.", [1467682230375, 1467682246440],
    "Rosa: lâminas 48–49.", extra="- Silencing dnmt3 with siRNA has the same effect without royal jelly"),
 ak("hdaci", 1495601288347, {1: V, 2: Z}, E_, "HDACi reativam supressores", 51, "Verde c1 (HY), azul c2; lâmina 51."),
 ak("hdaci-drogas", 1495600662766, {1: R}, E_, "Panobinostat e vorinostat", 52, "Verde: HY; lâmina 52. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 au("ips", "Adult fibroblasts can be reprogrammed into {{c1::induced pluripotent}} stem cells by four transcription factors", {1: Z}, E_,
    "Células iPS", "52; transcrição", "central", "sem card nos acervos.", [1495601288347, 1467682230375], "Azul: bloco de iPS da transcrição."),
 au("ips-oncogene", "Therapeutic use of iPS cells is limited because two of the factors, c-Myc and Klf4, are {{c1::oncogenes}}", {1: R}, E_,
    "Risco das iPS", "52; transcrição", "lateral", "sem card nos acervos.", [1495601288347, 1467682230375],
    "Rosa: transcrição.", extra="- Delivery by a retrovirus is a second obstacle"),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {'nucleossomo': '- About 147 bp of DNA wrap the histone octamer nearly twice',
 'fibra-30': '- The 30-nm fiber is the condensed form; 10 nm is beads on a string',
 'octamero': '- An H3–H4 tetramer plus two H2A–H2B dimers',
 'lisina-arginina': '- Their positive charge binds the negative DNA backbone at any sequence',
 'remodelador-atp': '- Unlike HATs and HDACs, they do not covalently modify histones',
 'pol-desaloja': '- Nucleosomes are rearranged whenever a gene is transcribed',
 'hat': '- Acetylation usually marks transcriptionally active regions',
 'hdac': '- Deacetylation favors condensed, inactive chromatin',
 'outras-mod': '- Lysines can also be methylated; serines and threonines are phosphorylated',
 'codigo': '- Readers bind specific combinations and recruit other proteins',
 'ativador-cromatina': '- This makes the promoter accessible to the transcription machinery',
 'repressor-cromatina': '- Absence of acetylation is usually linked to inactive regions',
 'hetero-condensada': '- It is the highest order of chromosome packaging',
 'constitutiva': '- Also at telomeres',
 'facultativa': '- It can switch between condensed and open states',
 'hetero-me': '- Clusters near the nucleolus and nuclear envelope',
 'eucromatina-me': '- Most interphase chromatin is euchromatin',
 'dnmt': '- SAM = S-adenosylmethionine, the methyl donor',
 'ilhas-cpg': '- Elsewhere in the genome most CpGs are methylated',
 'cpg-80': '- CpG is scarce in coding regions and enriched in promoters',
 'dna-hdac': '- Methylated CpG islands also attract histone methyltransferases',
 'gemeos': '- Shows environment shaping the epigenome',
 'hdaci': '- Approved for some lymphomas and multiple myeloma',
 'hdaci-drogas': '- Vorinostat treats cutaneous T-cell lymphoma',
 'ips': '- iPS cells self-renew and differentiate into many cell types'}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
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
