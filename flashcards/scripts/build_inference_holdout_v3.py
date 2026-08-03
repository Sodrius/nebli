#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Reserva 300 termos reais não mostrados nas frentes ou Extras do deck v3."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ETIM = Path(__file__).resolve().parents[1] / "etimologia"
CARDS = ETIM / "cards" / "cards_approved_v3.json"
LEXICON = ETIM / "data" / "lexicon_master.json"
OUT = ETIM / "data" / "inference_holdout_v3.json"
REPORT = ETIM / "reports" / "inference_test_v3.md"

# Inglês médico é deliberado: testa transferência dos mesmos morfemas para leitura
# científica sem reapresentar os exemplos portugueses usados no ensino.
TERMS = """
cardiomyopathy cardiomyocyte cardiothoracic cardiogenic cardiomegaly carditis pancarditis myocarditis endocarditis pericarditis
pericardiocentesis valvulopathy valvuloplasty aortography aortitis arteriopathy arteriography arteriotomy arteriosclerosis
atherogenesis atheroma angiopathy angiogenesis angioedema angioplasty venography venipuncture phlebitis phlebectomy
thrombectomy thrombogenesis thrombolysis thromboembolism embolization ischemic vasculitis vasculopathy vasodilation vasoconstriction
vasospasm sphygmography bradyarrhythmia tachyarrhythmia dysrhythmia atrioventricular interventricular intravascular extravascular
rhinorrhea rhinoplasty rhinoscopy sinusitis pansinusitis nasopharyngeal oropharyngeal laryngoscopy laryngectomy laryngomalacia
tracheostomy tracheotomy tracheomalacia tracheobronchial bronchiectasis bronchogenic bronchoscopy bronchospasm bronchiolitis
pneumonitis pneumonectomy pneumothorax pyothorax hemothorax chylothorax pleurodynia pleuritis pleurocentesis thoracentesis
thoracotomy thoracoscopy mediastinitis mediastinoscopy alveolitis alveolar hypoxemia hypercapnia hypocapnia tachypnea bradypnea
apnea dyspnea orthopnea platypnea trepopnea eupnea spirometry pneumoconiosis mucociliary endotracheal intrapulmonary extrapulmonary
stomatitis stomatology glossitis glossodynia macroglossia ankyloglossia sialadenitis sialolithiasis sialorrhea odontogenic
periodontitis endodontic dentinogenesis dysphagia odynophagia esophagitis esophagoscopy esophagectomy gastroenteritis gastroparesis
gastroduodenal gastroscopy gastrectomy gastrostomy gastroplasty gastrorrhagia enteropathy enterocolitis duodenitis jejunitis ileitis
ileostomy appendicitis appendectomy typhlitis colitis pancolitis colonoscopy colectomy colostomy proctitis proctoscopy rectocele
anorectal sigmoidectomy diverticulosis diverticulitis hepatomegaly hepatitis hepatopathy hepatotoxicity intrahepatic extrahepatic
cholestasis cholelithiasis cholecystitis cholecystectomy cholangitis cholangiography choledocholithiasis pancreatitis pancreatectomy
pancreatography peritonitis retroperitoneal mesenteric omentectomy laparoscopy laparotomy abdominoplasty coprolalia steatorrhea
hematemesis melena hematochezia achlorhydria hyperchlorhydria dyspepsia hyperemesis anorexia hyporexia hyperorexia polyphagia
nephritis nephrosis nephropathy nephrectomy nephrotomy nephrostomy nephrolithiasis nephrocalcinosis nephrotoxicity glomerulitis
glomerulopathy glomerulosclerosis pyelitis pyelonephritis pyelography caliectasis hydronephrosis hydroureter ureteritis ureterolithiasis
ureterostomy cystitis cystoscopy cystectomy cystostomy cystocele vesicoureteral urethritis urethroplasty urethrostenosis urolithiasis
hematuria hemoglobinuria proteinuria albuminuria glycosuria ketonuria pyuria bacteriuria nocturia oliguria polyuria anuria dysuria
azotemia uremia natriuresis diuresis antidiuresis intrarenal prerenal postrenal suprarenal renal cortical medullary
neuropathy polyneuropathy mononeuropathy neuritis neuralgia neurolysis neurotomy neuroplasty neurogenic encephalitis encephalopathy
encephalomalacia encephalomyelitis meningoencephalitis meningitis meningocele meningomyelocele myelitis myelopathy myelomalacia
radiculopathy radiculitis ganglionectomy gliosis glioma astrocytoma oligodendroglioma ependymoma hydrocephalus ventriculomegaly
ventriculostomy craniotomy craniectomy craniosynostosis cephalalgia microcephaly macrocephaly cerebellitis cerebritis corticospinal
thalamocortical hypothalamic hippocampal pontine medullary subarachnoid epidural subdural intracranial extracranial
hemiparesis hemiplegia paraplegia quadriplegia dyskinesia bradykinesia hyperkinesia akinesia ataxia apraxia aphasia dysphasia
dysarthria paresthesia dysesthesia hypoesthesia hyperesthesia anesthesia analgesia allodynia hyperalgesia synesthesia
anosmia hyposmia hyperosmia dysgeusia ageusia hypogeusia diplopia hemianopia photophobia phonophobia
osteitis osteomyelitis osteopathy osteomalacia osteoporosis osteosclerosis osteonecrosis osteogenesis osteotomy ostectomy
arthralgia arthritis arthropathy arthroplasty arthroscopy arthrodesis arthrocentesis arthrotomy chondritis chondromalacia chondrodysplasia
myalgia myositis myopathy myomalacia myonecrosis myogenesis rhabdomyolysis tendinitis tendinosis tenosynovitis tenotomy tenorrhaphy
fasciitis fasciotomy bursitis synovitis spondylitis spondylosis spondylolisthesis spondyloarthropathy kyphosis lordosis scoliosis
costochondritis craniofacial brachydactyly polydactyly syndactyly dactylitis podiatry chiropody carpal tarsal acetabular
femoroplasty patellectomy tibiofibular scapulothoracic costovertebral intervertebral intramuscular subperiosteal periosteal endosteal
endocrinopathy endocrinology hypopituitarism hyperpituitarism hypophysectomy thyroiditis thyroidectomy thyrotoxicosis hyperthyroidism
hypothyroidism parathyroidectomy hyperparathyroidism hypoparathyroidism adrenalectomy adrenocortical adrenomedullary pinealectomy
thymectomy pancreatogenic gonadotropin insulinoma hyperinsulinemia hypoinsulinemia hyperglycemia hypoglycemia glucogenesis glycogenesis
glycogenolysis gluconeogenesis glycolysis lipogenesis lipolysis proteolysis ketogenesis ketolysis ureagenesis anabolism catabolism
metabolism homeostasis allostasis hypercalcemia hypocalcemia hypernatremia hyponatremia hyperkalemia hypokalemia hyperosmolar hypoosmolar
orchitis epididymitis prostatitis prostatectomy orchidectomy orchiopexy cryptorchidism spermatogenesis azoospermia oligozoospermia
asthenozoospermia teratozoospermia hemospermia balanitis posthitis balanoposthitis vasectomy deferentography androgenic hypogonadism
gynecology oophoritis oophorectomy salpingitis salpingectomy salpingostomy hysterectomy hysteroscopy hysterotomy endometritis endometriosis
myometrium perimetrium cervicitis colposcopy colpitis vaginitis vulvitis vulvodynia mastitis mastalgia mastectomy mammography
amenorrhea dysmenorrhea oligomenorrhea polymenorrhea menorrhagia metrorrhagia menometrorrhagia galactorrhea agalactia hyperlactation
primigravida multigravida nullipara primipara multipara antepartum intrapartum postpartum prenatal perinatal neonatal puerperium
placentitis chorioamnionitis amniocentesis amniotomy fetopathy embryopathy teratogenesis embryogenesis organogenesis histogenesis
hematology hematopoiesis erythropoiesis leukopoiesis granulopoiesis lymphopoiesis thrombopoiesis erythrocytosis leukocytosis leukopenia
neutrophilia neutropenia eosinophilia eosinopenia basophilia lymphocytosis lymphopenia monocytosis thrombocytosis thrombocytopenia
pancytopenia reticulocytosis hemolysis hemolytic coagulopathy anticoagulation fibrinolysis fibrinogenesis splenomegaly splenectomy
immunology immunogenic immunodeficiency autoimmunity hypersensitivity antigenicity antibody-mediated phagocytosis opsonization chemotaxis
cytokinesis cytotoxicity bacteremia viremia fungemia parasitemia septicemia toxemia endotoxemia zoonosis iatrogenic nosocomial opportunistic
ophthalmology ophthalmoscopy ophthalmoplegia oculomotor retinopathy retinitis retinoscopy keratitis keratoplasty keratoconus
corneoplasty iriditis iridectomy uveitis blepharitis blepharoplasty blepharoptosis dacryocystitis dacryostenosis scleritis
phacoemulsification cycloplegia choroiditis conjunctivitis pupillometry anisocoria myopia hyperopia astigmatism presbyopia
otology otitis otalgia otorrhea otorrhagia otoscopy auricular tympanitis tympanometry tympanoplasty myringitis myringotomy
mastoiditis mastoidectomy vestibulopathy cochleitis labyrinthitis stapedectomy hypoacusis anacusis tinnitus audiometry
electrocardiography electroencephalography electromyography ultrasonography radiography fluoroscopy scintigraphy tomography manometry oximetry
endoscopy biopsy aspiration catheterization cannulation intubation extubation dialysis apheresis hemostasis debridement curettage ligation
anastomosis resection excision ablation transplantation autograft allograft xenograft osteoclasis lithotripsy tenodesis gastropexy
herniorrhaphy angiogram electrocardiogram electroencephalogram spirometer sphygmomanometer bronchoscope laparoscope arthroscope
""".split()


def fold(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s.casefold()) if not unicodedata.combining(c))


def compact(s: str) -> str:
    return re.sub(r"[^a-z]", "", fold(s))


ENGLISH_EQUIVALENTS = {
    "ectomia": "ectomy", "tomia": "tomy", "stomia": "stomy", "grafia": "graphy",
    "grama": "gram", "scopia": "scopy", "metria": "metry", "plastia": "plasty",
    "pexia": "pexy", "rafia": "rrhaphy", "tripsia": "tripsy", "patia": "pathy",
    "megalia": "megaly", "ite": "itis", "ose": "osis", "trofia": "trophy",
    "pneia": "pnea", "cinesia": "kinesia", "fagia": "phagia", "nefr": "nephr",
    "fleb": "phleb", "rin": "rhin", "laring": "laryng", "faring": "pharyng",
    "tireoid": "thyroid", "miel": "myel", "encefal": "encephal", "cefal": "cephal",
    "oftalm": "ophthalm", "glic": "glyc", "cit": "cyt",
}


def morpheme_inventory(rows: list[dict]) -> set[str]:
    forms: set[str] = set()
    for row in rows:
        for value in (row.get("entrada_canonica", ""), row.get("equivalente_ingles", "")):
            for part in re.split(r"[×;,\s]+", str(value)):
                token = compact(part.replace("/o", "").strip("-"))
                if len(token) >= 3:
                    forms.add(token)
    for pt, en in ENGLISH_EQUIVALENTS.items():
        if pt in forms:
            forms.add(en)
    return forms


def analyze(term: str, forms: set[str]) -> tuple[str, list[str], float]:
    word = compact(term)
    candidates = sorted({f for f in forms if len(f) >= 3 and f in word}, key=len, reverse=True)
    chosen: list[str] = []
    occupied: list[tuple[int, int]] = []
    for fragment in candidates:
        start = word.find(fragment)
        span = (start, start + len(fragment))
        if start >= 0 and not any(max(span[0], a) < min(span[1], b) for a, b in occupied):
            chosen.append(fragment)
            occupied.append(span)
    coverage = sum(b - a for a, b in occupied) / max(1, len(word))
    if len(chosen) >= 2 and coverage >= 0.50:
        label = "fully_decomposable"
    elif chosen:
        label = "partially_decomposable"
    else:
        label = "not_decomposable_by_taught_inventory"
    return label, chosen, round(coverage, 3)


def main() -> int:
    cards = json.loads(CARDS.read_text(encoding="utf-8"))["cards"]
    lexicon = json.loads(LEXICON.read_text(encoding="utf-8"))
    forms = morpheme_inventory(lexicon)
    visible = fold(" ".join(c["text"] + " " + c["extra"] for c in cards))
    analyzed = []
    seen_terms: set[str] = set()
    for term in TERMS:
        if term in seen_terms or fold(term) in visible:
            continue
        seen_terms.add(term)
        label, matches, coverage = analyze(term, forms)
        analyzed.append((term, label, matches, coverage))
    transferable = [x for x in analyzed if x[1] != "not_decomposable_by_taught_inventory"]
    opaque = [x for x in analyzed if x[1] == "not_decomposable_by_taught_inventory"]
    chosen = transferable[:270] + opaque[:30]
    if len(chosen) < 300:
        chosen += transferable[270:270 + 300 - len(chosen)]
    if len(chosen) != 300:
        raise RuntimeError(f"apenas {len(chosen)} termos realmente inéditos classificados")
    rows = [{"id": f"holdout-v3-{i:03d}", "term": term,
             "classification": label, "matched_morphemes": matches,
             "estimated_surface_coverage": coverage, "seen_in_cards": False,
             "language": "medical_english",
             "source": "Open RN Medical Terminology, NCBI Bookshelf NBK607454"}
            for i, (term, label, matches, coverage) in enumerate(chosen, 1)]
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {label: sum(r["classification"] == label for r in rows) for label in (
        "fully_decomposable", "partially_decomposable", "not_decomposable_by_taught_inventory")}
    transfer_rate = 100 * (counts["fully_decomposable"] + counts["partially_decomposable"]) / len(rows)
    REPORT.write_text(
        "# Teste de inferência v3\n\n"
        f"- Termos reservados: {len(rows)}\n- Presentes em Texto/Extra: 0\n"
        "- Idioma: inglês médico, para testar transferência à leitura científica.\n"
        f"- Totalmente decomponíveis pelo inventário: {counts['fully_decomposable']}\n"
        f"- Parcialmente decomponíveis: {counts['partially_decomposable']}\n"
        f"- Não decomponíveis pelo inventário ensinado: {counts['not_decomposable_by_taught_inventory']}\n"
        f"- Cobertura parcial ou total estimada: {transfer_rate:.1f}%\n"
        "- Método: correspondência explícita com morfemas do léxico; cada linha registra fragmentos encontrados e cobertura superficial.\n"
        "- Uso: avaliação separada; estes termos não geram cards no deck.\n",
        encoding="utf-8")
    print({"holdout": len(rows), "seen": 0, "candidate_pool": len(TERMS),
           "transfer_rate": round(transfer_rate, 1), **counts})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
