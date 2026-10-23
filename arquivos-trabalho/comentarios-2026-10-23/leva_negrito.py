#!/usr/bin/env python3
"""Leva de 23/10 (F-20261023-CLAUDE-02): negrito de contexto em todo autoral que não tinha e reescrita dos de custo-efetividade baixa
que repetem erros do GUIA_CARDS. Uma janela de escrita."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita, em_tela

A = Anki()
CLOZE = re.compile(r"\{\{c\d+::.*?\}\}", re.S)
T = {  # nid: termo a negritar (fora do cloze)
 1791627545924: "Liver cells and neurons", 1791627546050: "Gene expression", 1791627546174: "gene regulation", 1791627546427: "actin, tubulin and GAPDH",
 1791627546802: "eukaryotic activators and repressors", 1791627546928: "single gene", 1791627547475: "RNA polymerase II", 1791627549526: "tissue-specific enhancer",
 1791627549652: "LexA–Gal4 hybrid", 1791627549777: "In bacteria", 1791627550877: "JAK kinases", 1791627551003: "High phosphate", 1791627551127: "Insulin",
 1792082060658: "TATA promoter", 1792082060961: "preinitiation complex", 1792082068909: "high phosphate",
 1791631344117: "acetyl groups", 1791631344241: "remove acetyl groups", 1791631346241: "CpG sites", 1792082177137: "acetylated histone lysines",
 1792083296387: "paracoccidioidomycosis",
 1791625426408: "antigen-presenting cells", 1791625427531: "dendritic cells", 1791625428033: "primary infection", 1791743340457: "Necrotic tissue",
 1792083501161: "B-1 cells", 1791743339982: "microbial nucleic acids", 1791743340159: "Cytosolic", 1791743340332: "β-glucans",
 1791743340632: "Monosodium urate crystals", 1791625424832: "T cell recognition", 1791625421906: "same pathogen", 1791743344060: "Neutrophil extracellular traps (NETs)",
 1791629595872: "classical complement pathway", 1791743340759: "gout", 1791743342383: "acute inflammation", 1791743346909: "neurogenic inflammation",
 1791743347082: "Mast-cell", 1791743349282: "Lipoxins and resolvins", 1791743349458: "During resolution",
 1791625422907: "double-negative thymocytes", 1791625423557: "Double-positive thymocytes", 1791625424356: "CD8 coreceptor", 1791625425082: "thymocytes",
 1791625427658: "antigen is cleared", 1791625427783: "survive the contraction", 1791625427907: "Central memory T cells", 1791625428283: "immunological synapse",
 1791625429158: "IL-2", 1791625429283: "Activated CD4+ T cells", 1791625429407: "Activated T cells", 1791625429533: "Repeated stimulation",
 1791625431007: "CTL", 1791625431133: "releasing its granules", 1791625431508: "helper subset", 1791625433083: "Induced Tregs",
 1791625433208: "master transcription factor", 1791625434983: "Tregs", 1791625435406: "Treg-derived", 1791625435532: "TGF-β secreted by Tregs",
 1791625436032: "TGF-β alone", 1791625436156: "Th17 cells", 1791625436282: "two subsets' programs", 1791629594347: "B-cell activation",
 1791163022242: "three domains of life", 1791576665314: "prokaryotes", 1791576665465: "bacteria that live with us",
 1791576665617: "first antibiotic choice", 1791576665990: "solid media", 1791576666141: "Most bacteria", 1791576666292: "Viruses",
 1791576667142: "Bacilli", 1791576667442: "Spiral bacteria", 1791576667593: "Plasmids, flagella, pili, capsule and spores", 1791576667741: "bacterial cytoplasmic membrane",
 1791576667893: "bacterial cytoplasmic membrane", 1791576668193: "sugar is phosphorylated", 1791576668341: "bacterial membrane", 1791576668493: "toward a chemical signal",
 1791576668792: "Gram stain", 1791576669540: "cell wall", 1791576669693: "Peptidoglycan", 1791576671341: "Teichoic acids", 1791576671491: "Teichoic acids",
 1791576672240: "Gram-negative outer membrane", 1791576673415: "Gram-negative outer membrane", 1791576676315: "bacterial flagellum", 1791576676715: "Flagella",
 1791576677216: "pili", 1791576677667: "endospores", 1791576677967: "endospore", 1791576678116: "Endospore formers", 1791576678318: "spores",
 1791576679117: "reserves", 1791576679567: "surface layer of protein", 1791576680665: "biocides and antibiotics",
 1791557940633: "colonies", 1791557940956: "fungal cell wall", 1791575690369: "Yeasts", 1791575691218: "Hyphae",
 1792677736555: "viral capsid", 1792677739093: "icosahedral capsid", 1792677739352: "helical symmetry", 1792677743147: "viral genome",
 1792695019166: "After uncoating", 1792695019665: "CD4", 1792695020689: "endocytic entry", 1792695022241: "Early viral mRNAs",
 1792695023512: "DNA viruses", 1792695024423: "simplest DNA virus", 1792695026450: "linear DNA", 1792695027415: "SV40 large T antigen",
 1792695027663: "circular genome", 1792695027916: "HPV", 1792695029538: "Cancer caused by viruses", 1792695029787: "Polyoma and papillomaviruses",
 1792695030040: "Adenovirus", 1792695030714: "Herpesvirus", 1792695031215: "Herpesvirus linear DNA", 1792695032265: "vaccinia DNA",
 1792695032585: "Parvoviruses", 1792695032839: "Parvovirus single-stranded DNA", 1792695033339: "reovirus core", 1792695033589: "Host cells",
 1792695036065: "Influenza", 1792695052637: "RdRp of RNA viruses", 1792695052983: "(-) RNA viruses", 1792695054193: "maturation",
 1792695054492: "Inclusion bodies", 1792695055945: "Before budding", 1792695056542: "HTLV-1", 1792695063312: "broad-spectrum antiviral",
 1792695063612: "HCV", 1791141186163: "pleural cavity", 1791141186755: "pericardial cavity", 1791141188142: "subcutaneous edema",
 1791141188737: "Edema", 1791141190312: "Congestion", 1791147081622: "thermal inversion", 1791147082428: "air pollution",
 1791147083370: "emitted directly from a source", 1791147084271: "Ground-level ozone", 1791716432998: "M. tuberculosis",
 1791022173275: "cirrhosis", 1791022169824: "hepatic hemangioma", 1791022170976: "hepatic hemangioma", 1791022171899: "fatty liver",
 1791022172025: "fatty liver", 1791022172800: "alcoholic cirrhosis", 1791022174376: "portal hypertension",
 1791034105561: "terminal ileum", 1790981522079: "terminal ileum", 1790981522826: "pre-aortic lymph nodes",
 1792713394204: "portal blood", 1792713410554: "paraumbilical veins", 1792713411555: "functional right and left liver", 1792713412304: "surgical segments",
 1790979869985: "increases appetite", 1790980013307: "gastric glands", 1790980911173: "proliferative compartment", 1790980911279: "apoptosis",
 1790980911405: "intestinal epithelial cells", 1790980911781: "intestinal stem cells", 1790980916280: "Paneth cells",
 1791000309552: "pancreatic lipase", 1791000311101: "electroneutral", 1791000311226: "distal colon", 1791000311352: "paracellular water flow",
 1791035328086: "cholesteryl esters", 1791035338192: "small intestine", 1791051794902: "Maltose", 1790999272782: "smooth muscle",
 1791023819869: "peristalsis", 1790999833329: "GI smooth muscle contraction", 1790999834254: "swallowing", 1790999838053: "Strong colonic contractions",
 1790999838304: "Rectal distension", 1791575024195: "slow wave", 1791762418521: "dose-response curve", 1791762421022: "same receptor",
 1791826292220: "maximal response", 1791826294319: "therapeutic index", 1792624457204: "IV bolus", 1792624458275: "semilog plot",
 1792624463275: "half-lives", 1792624466325: "steady state", 1792657537231: "volume of distribution", 1792657541196: "half-life",
 1792657544384: "clearance doubles", 1792657545614: "first-order kinetics", 1790999838179: "Food entering the stomach",
}
NOVO = {  # custo-efetividade baixa (erro já no GUIA_CARDS): reescritos para carregar um processo
 1791631342791: {"Text": "Because <b>nucleosomes</b> cover promoters, a eukaryotic gene is {{c1::off}} until activators open its chromatin",
                 "Extra": "- In bacteria the default is the opposite: RNA polymerase reaches naked DNA and repressors must stop it"},
 1791631343592: {"Text": "Histone <b>N-terminal tails</b> stick out of the nucleosome, so enzymes can {{c1::acetylate}} them and loosen the chromatin",
                 "Extra": "- Acetylation neutralizes the lysine positive charge, so the tail grips the DNA less<br>- Tail-to-tail contacts are what compact nucleosomes into fibers"},
 1791631344666: {"Text": '<div data-nebli-organizacao="true"><b>Histone tail marks</b> and their effect:<br>- acetylation: {{c1::opens}} chromatin, gene active<br>- methylation: active or silent, depending on the {{c2::lysine}} marked<br>- the marks are read by proteins that recruit the next enzymes</div>',
                 "Extra": "- So the same histone can carry an on or off message, which reader proteins translate"},
 1791631346967: {"Text": "<b>Epigenetic</b> states are gene-expression patterns that persist through {{c1::cell division}} without changing the DNA sequence",
                 "Extra": "- They are copied by maintenance DNA methylation and by histone marks restored after replication<br>- This is how a liver cell keeps making liver cells"},
 1792082183634: {"Text": "After replication, <b>histone marks</b> are restored because a {{c1::reader}} domain binds the old mark and a writer copies it to new nucleosomes",
                 "Extra": "- Old histones are split between the two daughter strands, so each daughter keeps a template of the marks"},
 1791163022863: {"Text": "A visible bacterial <b>colony</b> is a {{c1::clone}}: millions of cells grown from a single cell",
                 "Extra": "- That is why picking one colony gives a pure culture of one species"},
 1791743342606: {"Text": "After the first wave of <b>neutrophils</b>, {{c1::monocytes}} dominate by about 1–2 days and become macrophages",
                 "Extra": "- Neutrophils are short-lived and die by apoptosis; monocytes live longer and clear the debris"},
 1791743343634: {"Text": "The chemokine <b>eotaxin</b> preferentially recruits {{c1::eosinophils}}",
                 "Extra": "- It binds CCR3 on eosinophils, which is why allergic and parasitic inflammation is eosinophil-rich"},
}


def bold_fora(texto, termo):
    partes, clozes = CLOZE.split(texto), CLOZE.findall(texto)
    for i, p in enumerate(partes):
        plano = re.sub(r"&nbsp;", " ", p)
        j = plano.find(termo)
        if j >= 0 and plano is not p:
            p = plano
        if j >= 0:
            partes[i] = p[:j] + f"<b>{termo}</b>" + p[j + len(termo):]
            return "".join(x for par in zip(partes, clozes + [""]) for x in par)
    return None


if __name__ == "__main__":
    notas = {n["noteId"]: n for n in A("notesInfo", notes=list(set(T) | set(NOVO)))}
    plano, falhas = {}, []
    for nid, termo in T.items():
        if nid in NOVO:
            continue
        novo = bold_fora(notas[nid]["fields"]["Text"]["value"], termo)
        if novo is None:
            falhas.append((nid, termo))
        else:
            plano[nid] = {"Text": novo}
    plano.update(NOVO)
    if falhas:
        raise SystemExit(f"termos não achados: {falhas}")
    print(len(plano), "notas")
    if "--simular" in sys.argv:
        sys.exit()
    atual = em_tela(A); feitos = []
    with escrita(A, "leva negrito e custo-efetividade 23/10", sync=False):
        for nid, f in plano.items():
            if nid in atual:
                continue
            A("updateNoteFields", note={"id": nid, "fields": f}); feitos.append(nid)
        A("addTags", notes=feitos, tags="NEBLI::feedback::leva-20261023")
    print(json.dumps({"alterados": len(feitos), "pulados": [n for n in plano if n not in feitos]}))
