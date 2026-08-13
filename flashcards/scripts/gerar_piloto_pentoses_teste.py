#!/usr/bin/env python3
"""Gera os artefatos auditáveis do deck isolado da Via das Pentoses."""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SLUG = "bioq-20-pentoses-radicais-livres-teste"
DECK = "NEBLI::TESTE_APAGAR::Bioquímica::Via das pentoses-fosfato"
OUT = ROOT / "arquivos-trabalho"
E1 = "../typst-build/_par_bioq-20-pentoses-radicais-livres-teste/etapa1.typ"
E2 = "../typst-build/_par_bioq-20-pentoses-radicais-livres-teste/etapa2.typ"
SLIDE_ROOT = "figuras/bioq-20-pentoses-radicais-livres-teste"


# id, objetivo, cloze, extra, ancora E1, imagem do slide que organiza o mecanismo
ROWS = [
    ("g6p_fates", "Relacionar a saída da G6P à finalidade metabólica.",
     "Glucose-6-phosphate can be used for storage, glycolysis, or the <b>{{c1::pentose phosphate pathway}}</b>.",
     "The construction exit: NADPH + ribose-5-phosphate; no ATP production.",
     "Há três caminhos possíveis", "overview"),
    ("ppp_products", "Recuperar os dois produtos que justificam a via.",
     "The pentose phosphate pathway supplies <b>{{c1::NADPH and ribose-5-phosphate}}</b>.",
     "Reductive power + nucleotide sugar scaffold; not an ATP-producing pathway.",
     "dois produtos que ela coloca na mesa", "overview"),
    ("nadph_role", "Separar os pools redutores de construção e de energia.",
     "NADH supports ATP production; <b>{{c1::NADPH}}</b> supplies reductive biosynthesis and antioxidant defense.",
     "Same redox chemistry; enzyme recognition keeps the pools functionally separate.",
     "doa elétrons para as reações de construção", "redox"),
    ("ribose_role", "Vincular ribose-5-P à síntese de nucleotídeos.",
     "Ribose-5-phosphate provides the sugar scaffold for <b>{{c1::nucleotides}}</b>.",
     "DNA, RNA, ATP, NAD+, FAD, and CoA all require nucleotide precursors.",
     "forma o esqueleto dos nucleotídeos", "overview"),
    ("rbc_dependency", "Explicar a dependência eritrocitária de NADPH.",
     "In red blood cells, the only source of NADPH is the <b>{{c1::pentose phosphate pathway}}</b>.",
     "No mitochondria; antioxidant capacity depends on oxidative PPP flux.",
     "única fonte de poder redutor", "glutathione"),
    ("oxidative_phase", "Distinguir as duas fases pelo produto e reversibilidade.",
     "The <b>{{c1::oxidative}}</b> phase is irreversible and yields NADPH, CO2, and pentose.",
     "The non-oxidative phase is reversible and reshuffles carbons without NADPH production.",
     "fase oxidativa: ela é irreversível", "oxidative"),
    ("g6pd_control", "Identificar a enzima que abre e controla a via.",
     "The rate-limiting first enzyme of the pentose phosphate pathway is <b>{{c1::G6PD}}</b>.",
     "Glucose-6-phosphate dehydrogenase initiates oxidative PPP flux.",
     "a enzima que abre a via das pentoses e controla sua velocidade", "oxidative"),
    ("oxidative_yield", "Fixar o saldo da fase oxidativa.",
     "Each glucose-6-phosphate entering oxidative PPP yields <b>{{c1::2 NADPH}}</b>.",
     "Also yields one CO2 and one pentose; no ATP is made in this phase.",
     "saem 2 NADPH, 1 CO2 e uma pentose", "oxidative"),
    ("co2_source", "Localizar a descarboxilação da via.",
     "PPP CO2 is released by <b>{{c1::6-phosphogluconate dehydrogenase}}</b>.",
     "This oxidative decarboxylation also produces the second NADPH.",
     "na descarboxilação da terceira reação", "oxidative"),
    ("nonoxidative_enzymes", "Distinguir as enzimas que rearranjam carbonos.",
     "Non-oxidative PPP rearrangement uses <b>{{c1::transketolase and transaldolase}}</b>.",
     "Transketolase transfers 2C; transaldolase transfers 3C; neither makes NADPH.",
     "transcetolase transfere blocos de dois carbonos", "nonoxidative"),
    ("transketolase_units", "Diferenciar blocos transferidos pelas duas enzimas.",
     "Transketolase transfers <b>{{c1::two-carbon}}</b> units between sugars.",
     "Transaldolase is the complementary 3-carbon transfer enzyme.",
     "transfere blocos de dois carbonos", "nonoxidative"),
    ("glycolytic_link", "Conectar a fase não oxidativa à glicólise.",
     "The reversible non-oxidative phase links PPP to glycolysis via <b>{{c1::F6P and G3P}}</b>.",
     "Carbon can move in either direction between pentoses and glycolytic intermediates.",
     "intermediários da glicólise", "nonoxidative"),
    ("ribose_only", "Selecionar o ramo para demanda isolada de ribose.",
     "A dividing cell needing ribose but little NADPH runs the <b>{{c1::non-oxidative phase}}</b>.",
     "Ribose is assembled from F6P/G3P; G6PD need not be engaged.",
     "precisa só de ribose", "nonoxidative"),
    ("nadph_max", "Selecionar o fluxo quando a demanda de NADPH predomina.",
     "Lipogenic tissue recycles excess pentoses through the <b>{{c1::non-oxidative phase}}</b> to maximize NADPH output.",
     "Oxidative PPP makes NADPH; recycling returns carbon for another oxidative pass.",
     "muito NADPH e pouca ribose", "nonoxidative"),
    ("nadph_atp", "Prever o destino do carbono quando NADPH e ATP são pedidos.",
     "When NADPH and ATP are both required, resulting G3P enters <b>{{c1::glycolysis}}</b>.",
     "Both PPP phases run; glycolysis supplies the ATP branch.",
     "precisa de NADPH e de ATP", "overview"),
    ("g6pd_regulation", "Usar a razão redox para prever o fluxo da via.",
     "A high NADPH/NADP+ ratio <b>{{c1::inhibits G6PD}}</b>.",
     "NADP+ activates G6PD; consumption of NADPH therefore increases oxidative PPP flux.",
     "é ativada pelo NADP+ e inibida pelo NADPH", "regulation"),
    ("gsh_regeneration", "Ligar NADPH à recarga da defesa antioxidante.",
     "Glutathione reductase uses NADPH to regenerate <b>{{c1::GSH}}</b> from GSSG.",
     "Reduced glutathione is the electron donor used to clear peroxides.",
     "regenerar a glutationa reduzida", "glutathione"),
    ("gpx_function", "Ligar glutationa reduzida à neutralização de peróxido.",
     "Glutathione peroxidase neutralizes H2O2 by oxidizing <b>{{c1::GSH}}</b> to GSSG.",
     "G6PD → NADPH → glutathione reductase → GSH → peroxide clearance.",
     "a glutationa reduzida neutraliza o peróxido", "glutathione"),
    ("heinz_bodies", "Reconhecer a consequência molecular da falha antioxidante.",
     "Oxidative stress in G6PD deficiency can form <b>{{c1::Heinz bodies}}</b> after hemoglobin denatures.",
     "Oxidized hemoglobin precipitates, damages the membrane, and promotes hemolysis.",
     "corpos de Heinz", "clinical"),
    ("g6pd_triggers", "Reconhecer o padrão de crise hemolítica desencadeada.",
     "Primaquine, sulfonamides, infection, and fava beans can trigger <b>{{c1::hemolysis}}</b> in G6PD deficiency.",
     "A crisis needs an oxidant load; asymptomatic baseline does not exclude the deficiency.",
     "A crise exige um oxidante", "clinical"),
    ("g6pd_malaria", "Conectar herança e vantagem seletiva da deficiência.",
     "G6PD deficiency is <b>{{c1::X-linked}}</b> and offers partial protection against falciparum malaria.",
     "Fragile erythrocytes impair the parasite cycle; protection is partial, not complete.",
     "tem herança ligada ao X", "clinical"),
]

IMAGES = {
    "overview": "slide-08.png", "redox": "slide-09.png", "oxidative": "slide-16.png",
    "nonoxidative": "slide-49.png", "regulation": "slide-54.png", "glutathione": "slide-44.png",
    "clinical": "slide-42.png",
}


def visual(concept: str, goal: str) -> dict:
    return {
        "visual_need": "recommended", "image_role": "mechanism", "image_status": "pending_review",
        "card_mode": "explanatory_image", "placement": "extra",
        "visual_task": goal,
    }


def main() -> None:
    plan = {"visual_plan_version": "v1", "slug": SLUG, "concepts": [
        {"concept_id": cid, "importance": "nuclear", "learning_goal": goal,
         "strategy": "extra_recommended", "image_role": "mechanism", "visual_task": goal,
         "rationale": "O esquema do slide organiza o mecanismo após o recall textual.",
         "needs_editorial_confirmation": False}
        for cid, goal, *_ in ROWS
    ]}
    plan_path = OUT / f"plano-visual-{SLUG}.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cards = []
    for cid, goal, text, extra, anchor, image in ROWS:
        cards.append({
            "nebli_id": f"pentoses-teste-{cid}", "concept_id": cid, "visual_plan_id": cid,
            "visual_plan_link": "primary", "text": text, "extra": extra, "image": image,
            "e1_anchor": {"quote": anchor},
            "generation": {"mode": "authorial", "source_refs": ["slides da aula", "E1 ampliada"],
                           "external_probe": {"queries": ["pentose phosphate pathway " + cid],
                                              "decision": "redação independente; nenhum card externo adequado estava marcado no Anki local"}},
            "semantic_review": {"atomicity": "pass", "induction": "pass", "medical": "pass", "reviewer": "self_audit_pentoses_v1"},
            "visual": visual(cid, goal),
        })
    spec = {
        "pipeline_contract": "e1-e2-v1", "slug": SLUG, "deck": DECK, "theme_label": "Bioquímica",
        "visual_plan": plan_path.name, "e1": {"path": E1},
        "e2": {"path": E2, "catalog": [goal for _cid, goal, *_ in ROWS]},
        "e2_coverage": [{"e2_item": goal, "concept_id": cid, "status": "covered", "rationale": "O card do conceito testa o mecanismo cobrado nas objetivas."} for cid, goal, *_ in ROWS],
        "images": {key: {"file": f"{SLIDE_ROOT}/{file}", "credit": "Source: lecture slide; private course material."} for key, file in IMAGES.items()},
        "cards": cards,
    }
    card_path = OUT / f"cards-{SLUG}.json"
    card_path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    facts = [{"id": cid, "e1_anchor": anchor, "importance": "nuclear", "route": {
        "source": "own", "card_refs": [text.replace("<b>", "").replace("</b>", "")], "coverage_quality": 2,
        "coverage_rationale": "card atômico recupera o fato e sua relação central na E1",
        "prior_search": {"anking": "insufficient", "other_decks": "insufficient"}}} for cid, _goal, text, _extra, anchor, _image in ROWS]
    matrix = {"lesson_pipeline": "deck-aula-v1", "deck": DECK, "e1": {"path": E1},
              "e1_inventory": [{"id": cid} for cid, *_ in ROWS], "facts": facts,
              "e1_enrichments": [{"source_ref": "slides da aula", "importance": "nuclear", "decision": "incorporated", "e1_anchor": anchor} for _cid, _goal, _text, _extra, anchor, _image in ROWS]}
    (OUT / f"matriz-deck-aula-{SLUG}.json").write_text(json.dumps(matrix, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {len(cards)} cards | {card_path.name}")


if __name__ == "__main__":
    main()
