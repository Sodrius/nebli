"""Plan lecture-specific gaps after the early AnKing installation."""
import json
import re
from collections import Counter
from prepare import HERE, INV, BY_ID, HY, digest

MEDIA = [
    "nebli_x2_exudate_table.png", "nebli_x2_permeability_early.png",
    "nebli_x2_permeability_late.png", "nebli_x2_ulcer.png",
    "nebli_x2_phlegmon.png", "nebli_x2_stasis.png", "nebli_x2_mediator_table.png",
]

def source_entry(nid, objective, text, extra):
    n = BY_ID[nid]
    assert n["cards"][0]["deck"].startswith("Referências::Anking Step Deck")
    fields = {name: "" for name in n["fields"]}
    fields["Text"], fields["Extra"] = text, extra
    return {"source_nid": nid, "source_deck": n["cards"][0]["deck"],
            "source_model": n["model"], "source_fields_hash": digest(n["fields"]),
            "source_tags": n["tags"], "origin": "AnKing", "objective": objective,
            "fields": fields, "expected_cards": len(set(re.findall(r"\{\{c(\d+)::", text))),
            "high_yield": HY in n["tags"], "pink": False, "pink_reason": ""}

def author(key, objective, text, extra, pink_reason=""):
    model = BY_ID[1487639081947]
    fields = {name: "" for name in model["fields"]}
    fields["Text"], fields["Extra"] = text, extra
    return {"source_nid": None, "source_deck": None, "source_model": model["model"],
            "source_fields_hash": None, "source_tags": [], "origin": "Autoral", "key": key,
            "objective": objective, "fields": fields,
            "expected_cards": len(set(re.findall(r"\{\{c(\d+)::", text))),
            "high_yield": False, "pink": bool(pink_reason), "pink_reason": pink_reason}

def main():
    entries = [
        source_entry(1487727429546, "recruitment",
            BY_ID[1487727429546]["fields"]["Text"],
            "PECAM-1 helps the leukocyte cross endothelial junctions in postcapillary venules."),
        source_entry(1535296447535, "exudate_transudate",
            "With leaky venules, edema fluid is a {{c1::protein-rich exudate}}; "
            "intact vessels yield a {{c2::protein-poor transudate}}.",
            'Exudate also carries more cells and LDH; transudate reflects altered hydrostatic or oncotic forces.'
            '<br><img src="nebli_x2_exudate_table.png" width="530">'),
        author("arteriolar-signs", "signs",
            "An inflamed focus becomes red and warm as local arterioles {{c1::dilate}}.",
            "Histamine and NO are the vascular mediators emphasized in the lecture."),
        author("stasis-marginates", "vascular_to_cellular",
            "As plasma escapes, hemoconcentrated blood slows; this {{c1::stasis}} brings leukocytes against the vessel wall.",
            'The slower stream links permeability to margination.'
            '<br><img src="nebli_x2_stasis.png" width="500">'),
        author("permeability-early", "permeability",
            "Histamine opens venular gaps by {{c1::endothelial contraction}}; burns leak through {{c2::direct endothelial injury}}.",
            'Contraction is brief; direct injury can last hours to days.'
            '<br><img src="nebli_x2_permeability_early.png" width="420">'),
        author("permeability-late", "permeability",
            "Adherent leukocytes prolong the leak by {{c1::injuring endothelium}}; VEGF moves plasma through {{c2::transcytosis}}.",
            'These are two additional permeability routes shown in the lecture.'
            '<br><img src="nebli_x2_permeability_late.png" width="420">'),
        author("ulcer-visual", "morphology",
            '<img src="nebli_x2_ulcer.png" width="500"><br>'
            'The lost epithelial surface forms an {{c1::ulcer}}.',
            'The slide shows a break in the surface epithelium with underlying acute inflammation.'),
        author("phlegmon-visual", "morphology",
            '<img src="nebli_x2_phlegmon.png" width="500"><br>'
            'Diffuse suppuration tracking across tissue planes is a {{c1::phlegmon}}.',
            'Unlike a circumscribed abscess, this pattern has no organized wall.'),
        author("paf-vascular", "vascular_mediators",
            "Leukocytes release {{c1::PAF}}, which dilates local vessels and increases permeability.",
            'The lecture lists both vascular effects in its mediator table.'
            '<br><img src="nebli_x2_mediator_table.png" width="530">',
            "Slide 12 table; lower long-term value than the main vascular mechanism"),
        author("exudate-cutoffs", "exudate_transudate",
            "In the lecture table, exudate exceeds {{c1::3 g/dL}} protein, {{c2::1.020}} density, and {{c3::200}} LDH.",
            'These are the course table thresholds; use the accompanying mechanism card for the enduring distinction.'
            '<br><img src="nebli_x2_exudate_table.png" width="530">',
            "Slide 7 course-specific numerical cutoffs; useful for the exam, low long-term value"),
    ]
    assert all(e["expected_cards"] for e in entries)
    (HERE / "augment-plan.json").write_text(json.dumps({"entries": entries, "media": MEDIA},
        ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"notes": len(entries), "cards": sum(e["expected_cards"] for e in entries),
                      "pink": sum(e["expected_cards"] for e in entries if e["pink"]),
                      "origins": dict(Counter(e["origin"] for e in entries))}, ensure_ascii=False))

if __name__ == "__main__":
    main()
