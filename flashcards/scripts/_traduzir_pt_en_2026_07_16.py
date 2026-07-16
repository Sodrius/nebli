#!/usr/bin/env python3
"""Traducao PT->EN dos 22 cards autorais de embriologia (feedback 2026-07-16 / A17).
Preserva posicao de cloze, <img> do original e linhas de credito de figura."""
import json, urllib.request, sys, re
sys.stdout.reconfigure(encoding="utf-8")

def call(a, **p):
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        "http://localhost:8765",
        data=json.dumps({"action": a, "version": 6, "params": p}).encode(),
        headers={"Content-Type": "application/json"})))
    if r.get("error"):
        raise RuntimeError("%s: %s" % (a, r["error"]))
    return r["result"]

CR5 = "<br>OpenStax Anatomy &amp; Physiology 2e, Fig. 28.5 (CC BY-NC-SA)."
CR9 = "<br>OpenStax Anatomy &amp; Physiology 2e, Fig. 28.9 (CC BY-NC-SA)."
CR13 = "<br>OpenStax Anatomy &amp; Physiology 2e, Fig. 28.13 (CC BY-NC-SA)."

T = {
1783811939299: ("The reduction from 2N to N happens in {{c1::meiosis I}}, which separates homologous chromosomes; meiosis II only separates sister chromatids and does not change ploidy.",
 "That is why meiosis I is reductional and meiosis II is equational (a mitosis of an already-haploid cell). Classic error: thinking ploidy falls in the second division."),
1783811939305: ("Crossing-over — the physical exchange of segments between paired homologs — occurs in {{c1::pachytene}} of the long prophase of meiosis I.",
 "It is a source of genetic diversity, together with the random assortment of which homolog goes to each cell. It happens before the homologs separate."),
1783811939309: ("In oogenesis, the division of the cytoplasm is {{c1::asymmetric}}: almost all the content stays in one oocyte and the other, tiny daughter cell is discarded as a polar body.",
 "This thrift lets the oocyte stockpile reserves to nourish the embryo in its first days. It contrasts with spermatogenesis, whose division is symmetric (4 equivalent spermatids)."),
1783811939317: ("In the zona pellucida, the glycoprotein {{c1::ZP3}} acts as the sperm receptor and triggers the acrosome reaction; ZP2 guides passage afterward.",
 "Fixing ZP3 = trigger and ZP2 = guide explains why, after fertilization, cleaving ZP2 and altering ZP3 locks the door against any other sperm." + CR5),
1783811939321: ("Cortical granules are enzyme-preloaded vesicles in the cortex of the {{c1::oocyte}}, waiting for the fusion trigger to block polyspermy.",
 "They belong to the oocyte, not the sperm — key detail: the block to polyspermy is the work of the female gamete."),
1783811939325: ("In spermiogenesis, the nucleus is hypercondensed by swapping histones for {{c1::protamines}}, smaller proteins that pack the DNA into the smallest possible volume.",
 "The nucleus becomes transcriptionally silent and protected for the journey. In parallel: expulsion of water/RNA, assembly of the acrosome from the Golgi, formation of the flagellum, and shedding of the cytoplasm."),
1783811939333: ("Capacitation occurs in the {{c1::female reproductive tract}} (7–12 h) and removes cholesterol from the head membrane, making it fluid and ready to fuse with the acrosome.",
 "Distinct from motility (acquired earlier, in the epididymis) and from the acrosome reaction (the pinpoint trigger at the zona). Capacitation enables; the reaction executes. That is why IVF must capacitate sperm in the lab."),
1783811939337: ("To cross the corona radiata, the sperm releases {{c1::hyaluronidase}}, which digests the hyaluronic acid that glues the follicular cells together — and at this point the acrosome is still intact.",
 "The corona is overcome from outside, without detonating the main payload. Only contact with ZP3 in the zona pellucida triggers the acrosome reaction." + CR5),
1783811939346: ("After fusion, the calcium wave in the oocyte dumps the cortical granules, which cleave {{c1::ZP2}} and alter ZP3, locking the zona against further sperm.",
 "This is the cortical reaction. Since ZP3 was the lock and ZP2 the guide, modifying them disables the binding sites. A second, faster defense is the change in the electrical potential of the oocyte membrane."),
1783811939351: ("If the block to polyspermy fails and two sperm fertilize, a {{c1::triploid (69 chromosomes)}} zygote forms, which is nonviable.",
 "Monospermy does not depend on preventing crossing of the zona (several can cross it), but on only one sperm fusing with the membrane and triggering the cortical reaction that bars the rest." + CR5),
1783811939355: ("In the human zygote, the maternal and paternal pronuclei do not fuse immediately: each replicates its DNA and the chromosomes only truly mix at the {{c1::first mitotic division}}, when all 46 line up together on the spindle.",
 "This mixing is syngamy. Before it, there are two separate genomes inside the same cell. After fusion the oocyte also completes meiosis II and expels the 2nd polar body." + CR5),
1783811939366: ("In the blastocyst, the inner cell mass and the trophectoderm share the same genome; what decides each cell fate is its {{c1::position}} (inside vs outside), not the DNA.",
 "Inner cell mass (inside) → embryo; trophectoderm (outside) → embryonic portion of the placenta. It is the first fate decision of life. The blastocyst hatches from the zona pellucida before implanting (~day 6)." + CR5),
1783811944420: ("In gastrulation, the three germ layers (ecto, meso, endo) all arise from the {{c1::epiblast}}; the hypoblast is pushed aside and becomes extraembryonic tissue.",
 "That is why hypoblast ≠ endoderm: the endoderm forms when epiblast cells migrate downward and replace the hypoblast (which goes on to form the yolk sac)." + CR9),
1783811944426: ("Appearing in the epiblast (~day 15), the primitive streak gives the embryo a midline and, with it, the {{c1::craniocaudal}} axis and bilateral symmetry.",
 "Before it, the disc was symmetric like a plate. It is also the gateway through which epiblast cells ingress inward." + CR9),
1783811944431: ("At the cranial end of the primitive streak is the primitive node, the organizer from which the cells that form the {{c1::notochord}} emerge.",
 "The node is the command center of gastrulation; the notochord born from it will, soon after, induce the entire nervous system." + CR9),
1783811944442: ("The conversion of an adhered epithelial epiblast cell into a migratory mesenchymal cell is called {{c1::EMT (epithelial–mesenchymal transition)}} — the engine of ingression.",
 "The cell breaks its junctions, loses polarity, and gains the ability to crawl. Without EMT no cell would leave the sheet. The neural crest reuses this same EMT later to migrate." + CR9),
1783811944446: ("The notochord becomes only the {{c1::nucleus pulposus}} of the intervertebral disc — the bony body of the vertebrae comes from the somite (paraxial mesoderm), not from it.",
 "Classic confusion. The notochord is axial mesoderm and has 3 roles: a provisional rigid axis, the future nucleus pulposus, and inducer of the neural plate." + CR9),
1783811944456: ("Folic acid prevents neural tube defects because it feeds the {{c1::DNA synthesis}} of the intense cell proliferation that seals the neuropores.",
 "The window is early (3rd–4th week, often before the woman knows she is pregnant), so supplementation must begin before conception." + CR13),
1783811944460: ("When the neural folds fuse, the neural crest is left at the junction, undergoes a {{c1::new EMT}}, and migrates throughout the embryo — hence its nickname, the 4th germ layer.",
 "Three populations leave the neuroectoderm: the neural tube (CNS, at the center), the neural crest (PNS, melanocytes and face — migrates), and the epidermis (closes over the top)." + CR9),
1783811944463: ("The paraxial mesoderm segments into repeated blocks, the {{c1::somites}}, each giving rise to a vertebra, its ribs, the skeletal muscle, and the dermis of the back of that segment.",
 "It is the segmentation of the somites that explains the repeated vertebra-after-vertebra pattern. Remember: the bony body of the vertebra comes from here; the notochord makes only the nucleus pulposus." + CR9),
1783811944474: ("In craniocaudal folding, the cranial and caudal folds curve {{c1::ventrally}}, giving the embryo the shape of a C that closes over its own belly.",
 "The engine is unequal growth: the neural tube and somites grow more than the edges, and the dorsal amniotic cavity pushes the ends downward. This is three-dimensionality along the head–tail axis." + CR13),
1783811944482: ("At the two points where mesoderm never intervened, ecto and endoderm stay in direct contact and form membranes that rupture: the buccopharyngeal opens the {{c1::mouth}} and the cloacal opens the anus.",
 "The buccopharyngeal comes from the prechordal plate (anterior); the cloacal is posterior. They are fragile points, destined to rupture to open the digestive tube to the exterior." + CR9),
}

def imgs(html):
    return "".join(re.findall(r"<img[^>]*>", html or ""))

info = {n["noteId"]: n for n in call("notesInfo", notes=list(T.keys()))}
done = 0
for nid, (front, extra) in T.items():
    f = info[nid]["fields"]
    of = f["Text"]["value"]
    oe = f["Extra"]["value"] if "Extra" in f else ""
    call("updateNoteFields", note={"id": nid, "fields": {
        "Text": front + imgs(of), "Extra": extra + imgs(oe)}})
    done += 1
print("Traduzidos PT->EN:", done)

info2 = call("notesInfo", notes=call("findNotes", query="tag:NEBLI::*"))
PT = re.compile(r"[ãõçáâàéêíóôú]", re.I)
left = [n["noteId"] for n in info2
        if PT.search(re.sub("<[^>]+>", " ", list(n["fields"].values())[0]["value"]))]
print("Cards com PT restante na frente:", len(left), left[:12])
