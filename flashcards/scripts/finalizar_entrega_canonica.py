#!/usr/bin/env python3
"""Fecha E1 + deck somente se ganho, cards, release e APKG estiverem aprovados."""
from __future__ import annotations
import argparse, hashlib, json, shutil, tempfile
from pathlib import Path
from audit_apkg import audit
from canonical_cards import content_sha256, ordered_card_set_sha256, referenced_media_hashes
from exportar_apkg_canonico import canonical_deck_name, export_apkg
from validar_ganho_aula import validate_learning_delta
from validar_release_e1_deck import validate_release


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--slug",required=True); p.add_argument("--deck-data",type=Path,required=True); p.add_argument("--validation-report",type=Path,required=True); p.add_argument("--out-dir",type=Path,required=True); a=p.parse_args()
    deck_path=a.deck_data.resolve(); report_path=a.validation_report.resolve(); deck=json.loads(deck_path.read_text(encoding="utf-8")); report=json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("schema")!="nebli-card-validation-v2" or report.get("ok") is not True: raise SystemExit("ERRO: relatório de validação ausente, antigo ou reprovado")
    cards=[c for c in deck.get("cards",[]) if isinstance(c,dict)]; deck_rows=[{"card_key":str(c.get("card_key") or ""),"content_sha256":content_sha256(c)} for c in cards]; report_rows=[{"card_key":str(c.get("card_key") or ""),"content_sha256":str(c.get("content_sha256") or "")} for c in report.get("cards",[]) if isinstance(c,dict)]
    if deck_rows!=report_rows: raise SystemExit("ERRO: cards, ordem ou conteúdo mudaram depois da validação")
    set_hash=ordered_card_set_sha256(cards)
    if report.get("ordered_card_set_sha256")!=set_hash: raise SystemExit("ERRO: hash do conjunto ordenado diverge do relatório")
    if report.get("media",[])!=referenced_media_hashes(cards,deck_path.parent): raise SystemExit("ERRO: mídia mudou depois da revisão")
    gain=validate_learning_delta(deck)
    if not gain.get("passed"): raise SystemExit("ERRO: gate de ganho da aula reprovado:\n- "+"\n- ".join(gain.get("errors") or []))
    rel=validate_release(deck,deck_path)
    if not rel.get("passed"): raise SystemExit("ERRO: release E1/deck reprovado:\n- "+"\n- ".join(rel.get("errors") or []))
    release=deck.get("release_gate") or {}
    if report.get("expected_card_count")!=len(cards): raise SystemExit("ERRO: contagem validada diverge do deck-data")
    if report.get("card_budget_hard_max")!=release.get("card_budget_hard_max"): raise SystemExit("ERRO: teto validado diverge do release_gate")
    e1=Path(str(release.get("e1_pdf") or "")); e1=e1 if e1.is_absolute() else (deck_path.parent/e1).resolve(); meta=deck.get("metadata") or {}; lesson=str(meta.get("nome_curto") or a.slug).strip().replace("/","-")
    out=a.out_dir.resolve(); out.mkdir(parents=True,exist_ok=True); final_pdf=out/f"{lesson} - E1.pdf"; final_apkg=out/f"{a.slug}.apkg"
    with tempfile.TemporaryDirectory(prefix="nebli-release-",dir=out) as raw:
        temp=Path(raw); temp_apkg=temp/final_apkg.name; exp=export_apkg(deck,deck_path,temp_apkg); expected=canonical_deck_name(deck)
        if exp.get("deck_name")!=expected or exp.get("card_count")!=len(cards): raise SystemExit("ERRO: exportador APKG não preservou deck/contagem aprovados")
        audited=audit(temp_apkg,expected)
        if not audited.get("passed"): raise SystemExit("ERRO: auditoria APKG reprovada:\n- "+"\n- ".join(audited.get("errors") or []))
        if audited.get("notes")!=len(cards) or audited.get("cards")!=len(cards): raise SystemExit("ERRO: APKG auditado não contém exatamente os cards aprovados")
        proof=dict(audited); proof["validation_report_sha256"]=hashlib.sha256(report_path.read_bytes()).hexdigest(); proof["ordered_card_set_sha256"]=set_hash; (temp/"apkg-audit.json").write_text(json.dumps(proof,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        tpdf=temp/final_pdf.name; shutil.copy2(e1,tpdf); tpdf.replace(final_pdf); temp_apkg.replace(final_apkg)
    print(final_pdf); print(final_apkg); return 0


if __name__=="__main__": raise SystemExit(main())
