#!/usr/bin/env python3
"""Gera a matriz auditável E1 ampliada -> deck-aula do teste de Embriologia I."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLUG = "embrio-01-gametogenese-fertilizacao-teste"
DECK = "NEBLI::TESTE_APAGAR::Embriologia I — Gametogênese e fertilização"

ROWS = [
 ("pgc", "células germinativas primordiais", "Primordial germ cells migrate", "anking"),
 ("oocyte_arrest", "ovócito secundário", "secondary oocyte arrested", "anking"),
 ("spermiogenesis", "espermiogênese", "undergo spermiogenesis", "anking"),
 ("capacitation", "capacitação", "Capacitation makes sperm", "own"),
 ("zona", "zona pelúcida", "zona pellucida is the glycoprotein", "own"),
 ("acrosome", "reação acrossômica", "acrosome reaction exposes", "own"),
 ("cortical", "grânulos corticais", "Cortical granules lie", "own"),
 ("polyspermy", "polispermia", "Cortical granule exocytosis", "own"),
 ("pronuclei", "pró-núcleo feminino", "Each human pronucleus", "own"),
 ("cleavage", "clivagem", "Cleavage produces smaller", "own"),
 ("compaction", "compactação", "Compaction creates", "own"),
 ("blastocyst", "blastocele", "fluid-filled cavity", "own"),
 ("hatching", "eclosão", "Blastocyst hatching", "own"),
 ("sertoli_leydig", "células de Sertoli", "male gonads consist", "anking"),
 ("blood_testis", "barreira hematotesticular", "Tight junctions", "anking"),
 ("axis", "GnRH pulsátil", "pituitary hormone", "anking"),
 ("follicle", "folículo ovariano", "functional unit of the ovaries", "anking"),
 ("aromatase", "aromatase", "aromatase activity", "anking"),
 ("ovulation", "14 dias antes", "days prior to menses", "anking"),
 ("corpus_luteum", "corpo lúteo", "luteal phase", "anking"),
 ("hcg", "sinciciotrofoblasto", "syncytiotrophoblasts", "anking"),
 ("anovulation", "ciclo anovulatório", "Anovulatory cycle results", "anking"),
 ("pcos", "síndrome dos ovários policísticos", "Patients with PCOS", "anking"),
]

def main():
    facts=[]
    for fid, anchor, ref, source in ROWS:
        route={"source":source,"card_refs":[ref],"coverage_quality":2,
               "coverage_rationale":"recupera o mecanismo ou a relação central da E1 ampliada"}
        if source == "own":
            route["prior_search"]={"anking":"insufficient","other_decks":"insufficient"}
        facts.append({"id":fid,"e1_anchor":anchor,"importance":"nuclear","route":route})
    spec={"lesson_pipeline":"deck-aula-v1","deck":DECK,
          "e1":{"path":"../typst-build/_par_embrio-01-gametogenese-fertilizacao-teste/etapa1.typ"},
          "e1_inventory":[{"id":x["id"]} for x in facts],"facts":facts,
          "e1_enrichments":[
            {"source_ref":"AnKing Step 1 curadoria ampliada","decision":"incorporated","importance":"nuclear","e1_anchor":"O testículo integra células germinativas"},
            {"source_ref":"AnKing Step 1 curadoria ampliada","decision":"incorporated","importance":"nuclear","e1_anchor":"O folículo e o ciclo preparam"},
            {"source_ref":"AnKing Step 1 curadoria ampliada","decision":"incorporated","importance":"nuclear","e1_anchor":"Implantação muda o controle hormonal"}]}
    out=ROOT/"arquivos-trabalho"/f"matriz-deck-aula-{SLUG}.json"
    out.write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding="utf-8")
    print(out)
if __name__=="__main__": main()
