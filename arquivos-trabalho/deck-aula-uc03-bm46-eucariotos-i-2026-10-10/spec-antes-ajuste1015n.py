# Especificação curada — Regulação da expressão gênica em eucariotos I (UC03 P3, Biologia Molecular; Prof. Alexandre Bruni Cardoso, 2026; 39 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-bm46-20261010a"
SHORT = "bm46"
LESSON = "2026-uc03-biologia-molecular-46-expressao-eucariotos-i"
DECK = "NEBLI::UC03::P3::Biologia Molecular::Expressão gênica em eucariotos I"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-02) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 20 consultas, 10/10): ")
EXCLUIDOS = [
 (1467833441597, "cada gene com seu promotor: repete promotor"),
 (1467833716981, "elementos de resposta no enhancer: detalhe de nome fora da aula"),
 (1462913309820, "glitazonas e PPAR-γ: farmacologia fora da aula"),
 (1467833768807, "leucine zipper do CREB: tipos de domínio só na aula antiga"),
]
FORA_DO_RECORTE = ["regulação pós-transcricional e RNAs (aulas seguintes)", "domínios de ligação ao DNA e repressores (aula antiga, não dada em 2026)"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_ = ("A-por-que-regular", "B-maquinaria-e-sequencias", "C-gal4-universalidade-modularidade", "D-sinais")
CARDS = [
 # ---------- A. Por que e em que nível regular (slides 2–8) ----------
 au("mesmo-genoma", "Liver cells and neurons carry the same {{c1::genome}} yet express different genes", {1: V}, A_,
    "Mesmo genoma, genes expressos diferentes", "2–3", "central", "sem card nos acervos sobre diferenciação por expressão gênica.", [1467682184880, 1467833682877],
    "Verde: ideia de abertura (fígado × neurônio, lagarta × borboleta)."),
 au("niveis", "Gene expression can be controlled at transcriptional, post-transcriptional, translational and {{c1::post-translational}} levels", {1: R}, A_,
    "Níveis de regulação", "4", "lateral", "sem card de níveis de regulação.", [1467682246440, 1495595300874], "Rosa: esquema da lâmina 4."),
 au("iniciacao", "Most gene regulation happens at the {{c1::initiation}} of transcription", {1: V}, A_,
    "Iniciação da transcrição é o ponto principal", "4 e 6", "central", "sem card nos acervos.", [1467833651277, 1467833682877], "Verde: foco da aula (lâminas 4 e 6)."),
 au("porque-regular", "Besides saving energy, regulating gene expression drives cell {{c1::differentiation}} during development", {1: Z}, A_,
    "Por que regular", "7", "central", "sem card nos acervos.", [1467833771481, 1467682184880], "Azul: lâmina 7."),
 au("housekeeping", "{{c1::Housekeeping}} genes, such as actin, tubulin and GAPDH, are expressed at steady levels in all cells", {1: V}, A_,
    "Genes constitutivos", "8", "central", "consulta 'housekeeping' sem card pertinente.", [1481335328926, 1467833682877], "Verde: lâmina 8."),
 au("regulados", "Regulated genes, such as alcohol dehydrogenase in the liver, are expressed only in certain {{c1::cell types}} or times", {1: Z}, A_,
    "Genes regulados", "8", "central", "sem card nos acervos.", [1481335328926, 1467833771481], "Azul: lâmina 8."),
 # ---------- B. Bactérias × eucariotos, maquinaria e sequências (slides 9–17) ----------
 au("cis-trans", "Regulatory DNA sequences act in {{c1::cis}}, while the transcription factors that bind them act in trans", {1: Z}, B_,
    "Elementos em cis, fatores em trans", "9", "central", "consulta cis-acting/trans-acting sem card.", [1467833682877, 1467833689549], "Azul: lâmina 9."),
 au("indireto", "Unlike bacterial regulators, eukaryotic activators and repressors mostly act on RNA polymerase II {{c1::indirectly}}", {1: V}, B_,
    "Ação indireta sobre a Pol II", "9 e 17; monitoria; Alberts cap. 7", "central", "sem card nos acervos.", [1467833693475, 1467833651277],
    "Verde: diferença central bactéria × eucarioto (objetivo 1).", extra="- They act through the Mediator, general factors and chromatin modifiers"),
 au("combinatorio", "In multicellular organisms, a single gene is often controlled by {{c1::dozens}} of transcription factors", {1: Z}, B_,
    "Controle combinatório", "9; Ib lâmina 17; Alberts", "central", "sem card nos acervos.", [1467833697927, 1467833682877], "Azul: lâmina 9."),
 ak("dna-dobra", 1467833724957, {1: Z}, B_, "DNA dobra para aproximar enhancer e promotor", 9, "Azul: alças das lâminas 9 e 17."),
 ak("heterocromatina", 1467682184880, {1: V}, B_, "Heterocromatina é inativa e inacessível", 9, "Verde: HY; 'cromatina inibe o acesso' (lâmina 9); provas 2024 e 2025."),
 ak("acetilacao", 1467682246440, {1: V, 2: Z}, B_, "Acetilação de histonas ativa a transcrição", 9, "Verde c1 (HY), azul c2; modificadores de cromatina (lâminas 9, 17, 22); provas 2024 e 2025."),
 au("maquinaria", "Besides RNA polymerase II, eukaryotic transcription needs general transcription factors and the {{c1::Mediator}} complex", {1: Z}, B_,
    "Pol II + GTFs + Mediador", "10; monitoria; Alberts cap. 7", "central", "consulta 'mediator' sem card.", [1467833651277, 1467833666692],
    "Azul: lâmina 10.", extra="- In bacteria, the sigma factor alone recognizes the promoter<br>- The eukaryotic machinery has more than 60 proteins"),
 ak("promotor", 1467833651277, {1: V, 2: Z}, B_, "Promotor: Pol II e fatores gerais", 11, "Verde c1 (HY), azul c2; lâminas 11–12."),
 ak("enhancer-distancia", 1467833712322, {1: V}, B_, "Enhancers perto, longe ou no íntron", 11, "Verde: HY; lâmina 11."),
 ak("gtf-promotor", 1467833666692, {1: Z}, B_, "Promotor liga fatores gerais", 12, "Azul: fatores gerais da lâmina 12."),
 ak("especificos-enhancer", 1467833697927, {1: Z}, B_, "Enhancer liga fatores específicos", 12, "Azul: fatores específicos da lâmina 12."),
 ak("tata", 1467833654903, {1: V}, B_, "TATA e CAAT box", 13, "Verde: HY; lâmina 13."),
 au("tbp", "The TATA box is recognized by {{c1::TBP}}, the TATA-binding protein", {1: V}, B_,
    "TBP/TFIID reconhece o TATA", "13; monitoria; aula antiga (Ia)", "central", "consultas TFIID e 'TATA-binding protein' sem card.", [1467833654903, 1467833666692],
    "Verde: lâmina 13 e monitoria.", extra="- TBP is a subunit of the general factor TFIID"),
 au("bre", "In the RNA polymerase II promoter, the BRE element next to the TATA box is recognized by {{c1::TFIIB}}", {1: R}, B_,
    "BRE reconhecido por TFIIB", "13; monitoria", "lateral", "sem card nos acervos.", [1467833654903, 1467833666692], "Rosa: tabela da lâmina 13."),
 ak("enhancer-def", 1467833682877, {1: V}, B_, "Enhancer liga fatores específicos e aumenta a expressão", 14, "Verde: HY; lâmina 14 (objetivo 2)."),
 ak("silencer", 1467833689549, {1: V}, B_, "Silencer liga repressores", 14, "Verde: HY; repressores no saldo do enhancer (lâmina 14)."),
 au("sinergia", "Activators bound to one enhancer act {{c1::synergistically}}, so a gene turns on strongly only when several signals coincide", {1: Z}, B_,
    "Sinergia e integração de sinais", "16; Alberts (integração)", "central", "sem card nos acervos.", [1467833682877, 1467833697927],
    "Azul: lâmina 16.", extra="- Two activators together give far more than the sum of each alone"),
 # ---------- C. Sistema Gal: universalidade e modularidade (slides 19–28) ----------
 au("gal4", "The yeast activator {{c1::Gal4}} turns on the genes that metabolize galactose", {1: Z}, C_,
    "Sistema Gal e Gal4", "19; monitoria", "central", "sem card nos acervos.", [1467833762279, 1467833771481],
    "Azul: lâmina 19.", extra="- Like the lac operon in function, but each GAL gene has its own promoter"),
 au("uas", "Gal4 binds one to four sites in the {{c1::UAS}} (upstream activating sequence) of its target genes", {1: R}, C_,
    "UAS", "20", "lateral", "sem card nos acervos.", [1467833682877, 1467833716981], "Rosa: lâmina 20."),
 au("dois-dominios", "Eukaryotic activators have separate {{c1::DNA-binding}} and activation domains", {1: V}, C_,
    "Domínios separados nos ativadores", "21; Alberts cap. 7", "central", "sem card de domínios do ativador.", [1467833758513, 1467833697927], "Verde: lâmina 21."),
 au("gal4-ativacao", "The activation domain of Gal4 recruits TFIID, the Mediator and {{c1::chromatin}}-modifying proteins", {1: Z}, C_,
    "O que o domínio de ativação faz", "22; Alberts cap. 7", "central", "sem card nos acervos.", [1467682246440, 1467833693475], "Azul: lâmina 22."),
 au("universalidade", "Gal4 activates a gene with a TATA box and a UAS in any eukaryotic cell, showing the {{c1::universality}} of transcriptional activation", {1: Z}, C_,
    "Princípio da universalidade", "23–26; monitoria", "central", "sem card nos acervos.", [1467833693475, 1467833682877],
    "Azul: objetivo 3 (princípio da aula, menos longitudinal).", extra="- The activator–machinery interface is conserved in yeast, plants and humans"),
 au("gal4-uas-ferramenta", "Expressing Gal4 under a tissue-specific enhancer turns on a UAS-linked {{c1::transgene}} only in that tissue", {1: R}, C_,
    "Gal4–UAS como ferramenta", "24–25", "lateral", "sem card nos acervos.", [1467833771481, 1467833682877], "Rosa: lâminas 24–25 (UAS:GFP)."),
 au("modularidade", "In a LexA–Gal4 hybrid, LexA anchors the protein to DNA while the Gal4 {{c1::activation}} domain turns on transcription", {1: Z}, C_,
    "Princípio da modularidade", "27–28; monitoria; Alberts", "central", "sem card nos acervos.", [1467833758513, 1467833697927],
    "Azul: objetivo 3 (experimento da aula).", extra="- Without its activation domain, Gal4 binds DNA but activates nothing"),
 # ---------- D. Como sinais chegam aos fatores de transcrição (slides 30–38) ----------
 au("sinal-direto", "In bacteria, the signal usually binds the transcription factor {{c1::directly}}, whereas eukaryotic signals often act through signaling pathways", {1: Z}, D_,
    "Sinal direto × transdução", "30; monitoria (PHO)", "central", "sem card nos acervos.", [1467833762279, 1496162213476], "Azul: objetivo 4."),
 au("formas-ativar", "A eukaryotic transcription factor can be switched on by ligand binding, phosphorylation, unmasking or {{c1::nuclear entry}}", {1: Z}, D_,
    "Formas de ativar um fator", "31; prova 2025 P3 1.5", "central", "sem card nos acervos.", [1496162213476, 1463883738825], "Azul: lâmina 31."),
 au("receptor-nuclear", "Nuclear receptors are transcription factors that bind DNA only after binding their lipid-soluble {{c1::hormone}}", {1: V}, D_,
    "Receptores nucleares", "32–33; monitoria", "central", "AnKing tem receptores específicos (T3, GR), não a definição.", [1462038493029, 1463883738825], "Verde: lâminas 32–33."),
 ak("t3", 1462038493029, {1: V}, D_, "T3 e receptor nuclear estimulam transcrição", 32, "Verde: HY; tiroxina da lâmina 32."),
 ak("zinco", 1467833758513, {1: V}, D_, "Dedo de zinco nos receptores de esteroides", 33, "Verde: HY; superfamília da lâmina 33."),
 ak("gr-citoplasma", 1463883728414, {1: V}, D_, "GR livre no citoplasma", 34, "Verde: HY; lâminas 34–35."),
 ak("gr-nucleo", 1463883738825, {1: V, 2: Z}, D_, "GR ligado vai ao núcleo e ao GRE", 35, "Verde c1 (HY), azul c2; GR–GFP com cortisol (lâmina 35)."),
 au("fosforilacao", "Phosphorylation can switch a transcription factor off by blocking its {{c1::DNA binding}} or by keeping it out of the {{c2::nucleus}}", {1: V, 2: V}, D_,
    "Duas formas de a fosforilação inibir um fator", "36; prova 2019 P3 5.2; monitoria (PHO)", "prova", "sem card nos acervos.", [1496162213476, 1496162245188],
    "Verdes: lâmina 36 e prova 2019."),
 au("jak-stat", "Cytokine-activated JAK kinases phosphorylate {{c1::STAT}} transcription factors", {1: Z}, D_,
    "Via JAK–STAT", "36", "central", "consulta JAK-STAT só com ruído no AnKing.", [1578537487044, 1496162213476], "Azul: figura da lâmina 36."),
 au("foxo1", "Insulin, through AKT, phosphorylates FOXO1 and moves it out of the {{c1::nucleus}}", {1: Z}, D_,
    "FOXO1 e insulina", "37–38", "central", "consulta FOXO sem card.", [1462131726115, 1496162213476], "Azul: lâminas 37–38."),
 au("pho4", "High phosphate inactivates the yeast activator Pho4 by {{c1::phosphorylation}}", {1: R}, D_,
    "Sistema PHO", "36; monitoria P3 aula 4; prova 2019", "prova", "sem card nos acervos.", [1496162213476, 1463883728414],
    "Rosa: exemplo da monitoria e da prova 2019, ligado à lâmina 36."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
 "mesmo-genoma": "- What changes is the set of genes expressed",
 "niveis": "- Transcriptional control is the most important",
 "iniciacao": "- Stopping early avoids wasting RNA and protein synthesis",
 "porque-regular": "- Responses can depend on location and timing",
 "housekeeping": "- They sustain functions common to every cell",
 "regulados": "- They act as markers of differentiation",
 "cis-trans": "- Cis elements sit on the same DNA molecule as the gene",
 "combinatorio": "- This combinatorial control lets few factors specify many patterns",
 "dna-dobra": "- Looping lets distant enhancers reach the promoter",
 "heterocromatina": "- Chromatin packing limits access of the transcription machinery",
 "promotor": "- RNA polymerase II cannot recognize the promoter by itself",
 "bre": "- INR and DPE are recognized by TFIID",
 "uas": "- The UAS works like an enhancer",
 "dois-dominios": "- In bacterial CAP, both functions lie in one protein surface",
 "gal4-ativacao": "- Gal4 does not contact RNA polymerase II directly",
 "gal4-uas-ferramenta": "- Lets researchers express a gene only in chosen tissues",
 "sinal-direto": "- Example: lactose binds the lac repressor directly",
 "formas-ativar": "- Also protein synthesis, adding a subunit or release from a membrane",
 "receptor-nuclear": "- Steroids, thyroid hormone, vitamin D and retinoic acid use them",
 "gr-citoplasma": "- Held in the cytoplasm by heat shock proteins",
 "fosforilacao": "- Pho4 and FOXO1 are both excluded from the nucleus when phosphorylated",
 "jak-stat": "- Phosphorylated STATs dimerize and enter the nucleus",
 "pho4": "- Phosphorylated Pho4 binds DNA poorly and is kept out of the nucleus",
 "foxo1": "- Gluconeogenic genes then switch off",
}
DUPLICACAO = {
 "gal4-ativacao": "ganho: o que o domínio de ativação recruta; heterocromatina/acetilação cobram o estado da cromatina",
 "foxo1": "ganho: exemplo humano (insulina–AKT–FOXO1) da exclusão nuclear; fosforilacao cobra o princípio",
 "fosforilacao": "ganho: as duas formas de inibição pela fosforilação (prova 2019); foxo1/formas-ativar cobram exemplos",
}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
