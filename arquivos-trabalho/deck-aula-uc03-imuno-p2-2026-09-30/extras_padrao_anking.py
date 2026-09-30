"""Reescreve o Extra dos autorais da Imuno P2 no formato AnKing (pedido de Davi, 30/09: "a quantidade de palavras
dos autorais tá alta, especialmente comentário, destoando do anking. tem que manter todo tipo de padrão").
AnKing: bullets "- " curtos, termo-chave em negrito, sem parágrafo explicativo (o porquê fica no Tab).
Uso: python3 extras_padrao_anking.py [--aplicar]
"""
import json, sys
from datetime import datetime
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita

NEW = {
    1790781880668: "- C1q binds the <b>CH2</b> domain of IgG and the <b>CH3</b> domain of IgM",
    1790781881517: "- Natural IgM and CRP can still trigger the <b>classical</b> pathway early",
    1790781882992: "- Cleavage yields <b>iC3b</b>, which cannot form convertases but still opsonizes",
    1790781884793: "- No C3b opsonization, no C5a, no MAC",
    1790781884893: "- Can cause <b>atypical HUS</b> (complement injury to glomerular endothelium)",
    1790781885018: "- C4 is used by the classical and lectin pathways, not the alternative pathway",
    1790781919539: "- TLR3 = dsRNA, TLR7/8 = ssRNA, TLR9 = CpG DNA",
    1790781919682: "- RIG-I-like receptor signaling induces <b>type I interferons</b>",
    1790781919789: "- Key receptor for <b>Candida</b> recognition",
    1790781919889: "- Examples: <b>ATP</b>, <b>HMGB1</b>, uric acid, heat shock proteins",
    1790781919988: "- Explains IL-1–driven inflammation in acute <b>gout</b> (IL-1 blockade can treat it)",
    1790781920520: "- Contain histones and granule enzymes such as <b>elastase</b> and <b>MPO</b>",
    1790781920620: "- CGRP is a potent vasodilator released with substance P",
    1790781920874: "- Lipoxins come from arachidonic acid, resolvins from <b>omega-3</b> fatty acids",
    1790806714968: "- Screening test for suspected complement deficiency",
    1790806715118: "- Requires factor B, factor D and properdin plus C3 and C5–C9",
    1790806715268: "- Absent CH50 <b>and</b> AH50 points to a C3 or terminal (C5–C9) deficiency",
}


def main(apply):
    A = Anki()
    notes = A("notesInfo", notes=list(NEW))
    problems = [str(n.get("noteId")) for n in notes if not n or "NEBLI::origem::Autoral" not in n["tags"]]
    print(f"{len(NEW)} Extras a reescrever; problemas: {problems or 'nenhum'}")
    for n in notes:
        print(f"  {n['noteId']}: {len(NEW[n['noteId']].split())} palavras")
    if problems or not apply:
        return
    (HERE / f"extras-before-{datetime.now():%H%M%S}.json").write_text(
        json.dumps({str(n["noteId"]): n["fields"]["Extra"]["value"] for n in notes}, ensure_ascii=False, indent=1))
    with escrita(A, "Imuno P2: Extra dos autorais no formato AnKing"):
        for nid, extra in NEW.items():
            A("updateNoteFields", note={"id": nid, "fields": {"Extra": extra}})
    back = {n["noteId"]: n["fields"]["Extra"]["value"] == NEW[n["noteId"]] for n in A("notesInfo", notes=list(NEW))}
    (HERE / "extras-receipt.json").write_text(json.dumps({str(k): v for k, v in back.items()}, indent=1))
    print("readback ok" if all(back.values()) else f"DIVERGENTE: {back}")


if __name__ == "__main__":
    main("--aplicar" in sys.argv)
