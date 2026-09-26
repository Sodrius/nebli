"""Aplica uma seleção de cards existentes como cópias NEBLI idempotentes."""
from __future__ import annotations
import argparse, json, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "http://127.0.0.1:8765"

def call(action: str, **params):
    body=json.dumps({"action":action,"version":6,"params":params}).encode()
    request=urllib.request.Request(API,body,{"Content-Type":"application/json"})
    with urllib.request.urlopen(request,timeout=90) as response: data=json.load(response)
    if data.get("error"): raise RuntimeError(f"{action}: {data['error']}")
    return data["result"]

def source_tag(nid: int) -> str: return f"NEBLI::source::nid-{nid}"

def existing(nid: int) -> list[int]:
    # A identidade é global; o deck pode ter sido alterado/interrompido antes
    # da leitura de confirmação e não pode causar uma segunda cópia.
    return call("findNotes",query=f'tag:"{source_tag(nid)}"')

def move_to_deck(note_ids: list[int], deck: str) -> None:
    cards=[]
    for note in call("notesInfo",notes=note_ids): cards.extend(note["cards"])
    if cards: call("changeDeck",cards=cards,deck=deck)

def card_ids_for_notes(note_ids: list[int]) -> list[int]:
    return [card_id for note in call("notesInfo",notes=note_ids) for card_id in note["cards"]]

def resume_explicitly(source_nids: list[int]) -> list[int]:
    """The only path in this program allowed to lift a manual suspension."""
    cards=[]
    for source_nid in source_nids:
        copies=existing(source_nid)
        if not copies: raise RuntimeError(f"não há cópia NEBLI para a origem {source_nid}")
        cards.extend(card_ids_for_notes(copies))
    if cards: call("unsuspend",cards=cards)
    return cards

def suspended_count(source_nids: list[int]) -> int:
    copies=[copy for source_nid in source_nids for copy in existing(source_nid)]
    cards=card_ids_for_notes(copies) if copies else []
    return sum(card["queue"] == -1 for card in call("cardsInfo",cards=cards)) if cards else 0

def apply(selection_path: Path, export: Path | None, dry_run: bool, resume_sources: list[int]) -> dict:
    spec=json.loads(selection_path.read_text(encoding="utf-8")); deck=spec["target_deck"]
    if call("version") != 6: raise RuntimeError("versão AnkiConnect incompatível")
    # Suspensões manuais são preservadas por padrão, inclusive ao reexecutar,
    # mover de deck ou exportar. Só --resume-source chama unsuspend.
    resumed=[] if dry_run else resume_explicitly(resume_sources)
    if not dry_run: call("createDeck",deck=deck)
    created=[]; already=[]; unknown=[]
    for candidate in spec["candidates"]:
        nid=candidate["source_nid"]; found=existing(nid)
        if found:
            if not dry_run: move_to_deck(found,deck)
            already.append({"source_nid":nid,"target_nids":found}); continue
        source=call("notesInfo",notes=[nid])
        if len(source) != 1: raise RuntimeError(f"fonte ausente: {nid}")
        note=source[0]
        fields={name:value["value"] for name,value in note["fields"].items() if name != "ankihub_id"}
        tags=list(dict.fromkeys(note["tags"]+["NEBLI::2026-uc03-patologia-38-inflamacao-aguda","NEBLI::anking-copy",source_tag(nid)]))
        operation={"deckName":deck,"modelName":note["modelName"],"fields":fields,"tags":tags,"options":{"allowDuplicate":True}}
        if dry_run: created.append({"source_nid":nid,"status":"planned"}); continue
        try:
            target_nid=call("addNote",note=operation)
        except (TimeoutError, urllib.error.URLError) as error:
            reconciled=existing(nid)
            if reconciled: created.append({"source_nid":nid,"target_nids":reconciled,"reconciled_after_error":str(error)})
            else: unknown.append({"source_nid":nid,"error":str(error)})
            continue
        confirmed=existing(nid)
        if not confirmed: unknown.append({"source_nid":nid,"returned_nid":target_nid,"error":"addNote sem readback"})
        else:
            move_to_deck(confirmed,deck)
            created.append({"source_nid":nid,"target_nids":confirmed})
    exported=None
    if export and not dry_run and not unknown:
        export.parent.mkdir(parents=True,exist_ok=True)
        if not call("exportPackage",deck=deck,path=str(export.resolve()),includeSched=False): raise RuntimeError("exportPackage falhou")
        exported=str(export.resolve())
    source_nids=[candidate["source_nid"] for candidate in spec["candidates"]]
    receipt={"schema_version":1,"lesson_id":spec["lesson_id"],"deck":deck,"at":datetime.now(timezone.utc).isoformat(),"created":created,"already_present":already,"unknown":unknown,"exported":exported,"source_count":len(source_nids),"manual_suspension_policy":"preserve; only --resume-source may unsuspend","resumed_explicitly":resumed,"suspended_observed":suspended_count(source_nids)}
    receipt_path=Path("artifacts")/spec["lesson_id"]/"anki"/"receipt.json"; receipt_path.parent.mkdir(parents=True,exist_ok=True); receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"created":len(created),"already_present":len(already),"unknown":len(unknown),"resumed_explicitly":len(resumed),"suspended_observed":receipt["suspended_observed"],"exported":exported,"receipt":str(receipt_path)},ensure_ascii=False))
    if unknown: raise SystemExit(1)

if __name__ == "__main__":
    p=argparse.ArgumentParser(); p.add_argument("selection",type=Path); p.add_argument("--export",type=Path); p.add_argument("--dry-run",action="store_true"); p.add_argument("--resume-source",type=int,nargs="*",default=[],help="única forma de dessuspender: informe os nids de origem explicitamente"); a=p.parse_args(); apply(a.selection,a.export,a.dry_run,a.resume_source)
