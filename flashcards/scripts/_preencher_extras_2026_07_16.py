#!/usr/bin/env python3
"""Preenche Extra vazio (A13) — feedback 2026-07-16. Preserva <img> existente."""
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

TONSIL = "Palatine tonsil: non-encapsulated MALT lined by stratified squamous epithelium that dips into deep crypts; it has no afferent lymphatics."
SPLEEN = "Spleen: white pulp (lymphoid sheaths around central arterioles) plus red pulp (cords of Billroth and sinusoids) that filters aged RBCs."
NODE = "Lymph node: encapsulated, organized into cortex (B-cell follicles), paracortex (T cells), and medulla; it filters afferent lymph."
THYMUS = "Thymus: dark cortex (dense immature thymocytes) and pale medulla (Hassall corpuscles); site of T-cell education, involutes after puberty."

E = {
1667446964787: TONSIL, 1667446986960: TONSIL, 1783972024857: TONSIL, 1783972026933: TONSIL,
1667447025198: SPLEEN, 1667447043977: SPLEEN, 1783972029012: SPLEEN, 1783972031098: SPLEEN,
1667447081179: NODE, 1667447091099: NODE, 1783972033193: NODE, 1783972035293: NODE,
1667447136741: THYMUS, 1667447150694: THYMUS, 1783972037352: THYMUS, 1783972039421: THYMUS,
1783811944342: "The notochord is transient axial mesoderm; only its core persists postnatally, as the nucleus pulposus, whose herniation causes disc disease.",
1783811944349: "Neural crest is the great migratory population: melanocytes, PNS ganglia, Schwann cells, adrenal medulla, and much of the facial skeleton.",
1783811944357: "The anterior then posterior neuropore close by the end of week 4; failure gives anencephaly or spina bifida.",
1783811944365: "Cranial neural crest builds the facial bones, much of the skull, and odontoblasts — an exception to the rule that bone comes from mesoderm.",
1783811944373: "Mesoderm gives the musculoskeletal system, connective tissue, and serous linings — the middle layer, the flesh between epithelia.",
1783811944380: "Blood, vessels, and lymphatics are mesoderm-derived; hematopoiesis starts in the yolk sac, then shifts to liver and marrow.",
1783811944387: "The urinary system arises from intermediate mesoderm, alongside the gonads.",
1783811944395: "Gonads come from intermediate mesoderm, but the germ cells themselves migrate in from the yolk sac.",
1783811944415: "Endoderm lines the gut tube and buds off its glands — lungs, liver, pancreas, thyroid — the epithelia of the inner tube.",
1783971750550: "Bipolar neurons are rare, confined to special senses: retina, olfactory epithelium, and the cochlear/vestibular ganglia.",
1783971765121: "Lipofuscin is the wear-and-tear pigment: indigestible lipid-protein residue in lysosomes that accumulates with age; harmless.",
1783971804666: "The Purkinje layer is the cerebellar cortex output: a single row of large GABAergic neurons projecting to the deep nuclei.",
1783971978359: "Both are born in the bone marrow, but the T cell leaves to be educated in the thymus, while the B cell matures in place.",
1783971988862: "Thymic involution: peak size near puberty, then progressive replacement by fat, so T-cell output falls with age.",
1783971997245: "The subcapsular sinus receives afferent lymph and is where the node first samples antigen; a clear space just under the capsule.",
1783972003526: "Red pulp filters blood: RBCs squeeze from the cords through slits into sinusoids, and aged or abnormal cells are culled by macrophages.",
1783972266375: "Lacteals give intestinal lymph its milky look (chyle): dietary long-chain fats bypass the portal vein and enter lymph as chylomicrons.",
1783972437727: "Lymphedema is protein-rich interstitial fluid that lymph failed to clear; classically after axillary node dissection in breast cancer.",
1783972460570: "The right lymphatic duct drains only the right head/neck, right arm, and right thorax; everything else drains via the thoracic duct.",
1784109308569: "The paracortex is the T-cell zone, fed by high endothelial venules; it expands during cell-mediated (viral) responses.",
}

info = {n["noteId"]: n for n in call("notesInfo", notes=list(E.keys()))}
done = 0
for nid, txt in E.items():
    f = info[nid]["fields"]
    if "Extra" not in f:
        print("SEM campo Extra:", nid); continue
    cur = f["Extra"]["value"] or ""
    imgs = "".join(re.findall(r"<img[^>]*>", cur))
    newval = (imgs + "<br>" + txt) if imgs else txt
    call("updateNoteFields", note={"id": nid, "fields": {"Extra": newval}})
    done += 1
print("Extras preenchidos:", done)

# verificacao
info2 = call("notesInfo", notes=call("findNotes", query="tag:NEBLI::*"))
still = [n["noteId"] for n in info2 if "Extra" in n["fields"]
         and not re.sub("<[^>]+>", " ", n["fields"]["Extra"]["value"]).strip()]
print("Extra ainda vazio:", len(still), still[:12])
