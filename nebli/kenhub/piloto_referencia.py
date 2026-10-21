"""Monta o piloto visual privado da Referência externa, sem tocar no Anki."""
from __future__ import annotations

import hashlib
import base64
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw

from nebli.kenhub import mascara
from nebli.kenhub.referencia_externa import CONFIG, MANIFEST, PRIVATE, STATE, _read, _sha
from nebli.decks import Anki, escrita

UNITS = [
    {"domain": "anatomia", "module": "Membro superior", "order": 1,
     "slug": "upper-arm-bones-and-ligaments", "title": "Húmero e escápula", "path": "anatomia/humero-e-escapula"},
    {"domain": "anatomia", "module": "Membro superior", "order": 2,
     "slug": "main-arteries-found-in-upper-limb", "title": "Artérias principais do membro superior", "path": "anatomia/arterias-principais-membro-superior"},
    {"domain": "histologia", "module": "Histologia geral", "order": 1,
     "slug": "types-of-loose-connective-tissue", "title": "Tecido conjuntivo frouxo", "path": "histologia/tecido-conjuntivo-frouxo"},
]
MODEL = "NEBLI Kenhub Referência v1"
FIELDS = ["Nome PT", "Nome EN", "Imagem Frente", "Imagem Verso", "Fonte", "ID (hidden)", "NEBLI_Comentario", "NEBLI_Resposta"]
FRONT = '<div class="ref-wrap">{{Imagem Frente}}</div>'
BACK = '<div class="ref-wrap">{{Imagem Verso}}</div>'
CSS = ".card{margin:0;padding:4px;text-align:center;background:#fff}.nightMode .card,.night_mode .card{background:#222}.ref-wrap img{max-width:100%;max-height:calc(100vh - 8px);width:auto;height:auto}"


def _compor(base: Image.Image, overlay: bytes) -> Image.Image:
    import io
    ov = Image.open(io.BytesIO(overlay)).convert("RGBA")
    if ov.size != (base.width * mascara.ESCALA, base.height * mascara.ESCALA):
        raise ValueError("overlay em dimensão inesperada")
    fundo = base.resize(ov.size, Image.Resampling.LANCZOS).convert("RGBA")
    return Image.alpha_composite(fundo, ov).convert("RGB")


def _folhas(records, out: Path, per=8):
    out.mkdir(parents=True, exist_ok=True)
    files=[]
    for n in range(0, len(records), per):
        group=records[n:n+per]; canvas=Image.new("RGB",(1440, ((len(group)+1)//2)*390),"white"); d=ImageDraw.Draw(canvas)
        for k,r in enumerate(group):
            x=(k%2)*720; y=(k//2)*390; d.text((x+8,y+5),f"{n+k+1}. {r['name']}",fill=(20,20,20))
            for j,key in enumerate(("front","back")):
                im=Image.open(r[key]).convert("RGB"); im.thumbnail((350,340)); canvas.paste(im,(x+j*355,y+35))
        f=out/f"folha-{n//per+1:02d}.jpg"; canvas.save(f,quality=88); files.append(str(f))
    return files


def build() -> dict:
    cfg=_read(CONFIG); approval=PRIVATE/cfg["authorization"]["approval_file"]
    if not approval.exists() or _read(approval).get("config_sha256") != _sha(CONFIG):
        raise SystemExit("piloto sem autorização válida")
    run=PRIVATE/f"piloto-{datetime.now():%Y-%m-%d}"; run.mkdir(parents=True,exist_ok=True)
    report={"run":str(run),"created_at":datetime.now(timezone.utc).isoformat(),"units":[],"cards":[],"exceptions":[],"failures":[]}
    for unit in UNITS:
        src=PRIVATE/unit["path"]/"itens.json"; data=_read(src); urec={**unit,"targets":len(data["itens"]),"built":0}
        for item in data["itens"]:
            if item.get("sem_figura"):
                report["exceptions"].append({"unit":unit["slug"],"structure":item["slug"],"reason":"sem_figura"}); continue
            image=src.parent/item["arquivo"]
            try:
                region=mascara.regiao(str(image)); base=Image.open(image).convert("RGB")
                rec={"unit":unit["slug"],"structure":item["slug"],"name":item.get("nome_pt") or item["nome_en"],
                     "name_en":item["nome_en"],"source_sha256":hashlib.sha256(image.read_bytes()).hexdigest(),"themes":{}}
                for theme in cfg["visual_themes"]:
                    front,back,meta=mascara.overlays(base.size,region,rec["name"],cobrir=False,tema=theme)
                    dest=run/theme/unit["slug"]; dest.mkdir(parents=True,exist_ok=True)
                    fp,bp=dest/f"{item['slug']}-front.jpg",dest/f"{item['slug']}-back.jpg"
                    _compor(base,front).save(fp,quality=90); _compor(base,back).save(bp,quality=90)
                    rec["themes"][theme]={"front":str(fp),"back":str(bp),"meta":meta}
                report["cards"].append(rec); urec["built"]+=1
            except Exception as exc:
                report["failures"].append({"unit":unit["slug"],"structure":item["slug"],"error":str(exc)})
        report["units"].append(urec)
    for theme in cfg["visual_themes"]:
        rows=[{"name":r["name"],"front":r["themes"][theme]["front"],"back":r["themes"][theme]["back"]}
              for r in report["cards"] if theme in r["themes"]]
        report.setdefault("contact_sheets",{})[theme]=_folhas(rows,run/"folhas"/theme)
    # Gates locais do piloto: lote não vazio, 3 unidades, exceções explícitas e nenhum erro de montagem.
    if len(report["units"]) != 3: report["failures"].append({"gate":"G38","error":"piloto sem três unidades"})
    if not report["cards"]: report["failures"].append({"gate":"G39","error":"piloto vazio"})
    report["gate_ok"] = not report["failures"]
    (run/"relatorio.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    manifest=_read(MANIFEST); manifest["pilot_units"]=UNITS; manifest["pilot_run"]=str(run); manifest["pilot_gate_ok"]=report["gate_ok"]
    MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    with STATE.open("a") as f:
        for u in report["units"]: f.write(json.dumps({"at":report["created_at"],"unit":u["slug"],"state":"BUILT","cards":u["built"]})+"\n")
    print(json.dumps({"cards":len(report["cards"]),"exceptions":len(report["exceptions"]),"failures":len(report["failures"]),
                      "sheets":{k:len(v) for k,v in report["contact_sheets"].items()},"run":str(run)},ensure_ascii=False))
    return report


def install() -> dict:
    """Instala as duas variantes do piloto em subdecks separados, sempre suspensas; sem sync."""
    cfg=_read(CONFIG); approval=PRIVATE/cfg["authorization"]["approval_file"]
    if not approval.exists() or _read(approval).get("config_sha256") != _sha(CONFIG):
        raise SystemExit("instalação recusada: piloto sem autorização válida")
    manifest=_read(MANIFEST); run=Path(manifest.get("pilot_run", "")); report=_read(run/"relatorio.json")
    if not report.get("gate_ok") or report.get("failures"):
        raise SystemExit("instalação recusada: relatório do piloto não passou")
    A=Anki(); created=[]; existing=[]; media_names={}
    root=cfg["deck_root"]
    with escrita(A,"piloto Referência externa Kenhub (âmbar+ciano, tudo suspenso)",sync=False):
        if MODEL not in A("modelNames"):
            A("createModel",modelName=MODEL,inOrderFields=FIELDS,css=CSS,isCloze=False,
              cardTemplates=[{"Name":"Identificação visual","Front":FRONT,"Back":BACK}])
        for unit in UNITS:
            for theme in cfg["visual_themes"]:
                domain=unit["domain"].capitalize()
                A("createDeck", deck=f"{root}::Piloto::{theme.capitalize()}::{domain}::{unit['module']}::{unit['order']:02d} {unit['title']}")
        for rec in report["cards"]:
            unit=next(u for u in UNITS if u["slug"]==rec["unit"])
            for theme in cfg["visual_themes"]:
                stable=f"khref:{rec['unit']}:{rec['structure']}:{theme}"
                found=A("findNotes",query=f'"ID (hidden):{stable}"')
                if found: existing.extend(found); continue
                files={}
                for side in ("front","back"):
                    p=Path(rec["themes"][theme][side]); name=f"khref-{hashlib.sha256(stable.encode()).hexdigest()[:16]}-{side}.jpg"
                    A("storeMediaFile",filename=name,data=base64.b64encode(p.read_bytes()).decode()); files[side]=name
                    media_names[name]=hashlib.sha256(p.read_bytes()).hexdigest()
                domain=unit["domain"].capitalize()
                deck=f"{root}::Piloto::{theme.capitalize()}::{domain}::{unit['module']}::{unit['order']:02d} {unit['title']}"
                nid=A("addNote",note={"deckName":deck,"modelName":MODEL,"options":{"allowDuplicate":True},"fields":{
                    "Nome PT":rec["name"],"Nome EN":rec["name_en"],
                    "Imagem Frente":f'<img src="{files["front"]}">',"Imagem Verso":f'<img src="{files["back"]}">',
                    "Fonte":"Kenhub","ID (hidden)":stable,"NEBLI_Comentario":"","NEBLI_Resposta":""},
                    "tags":["NEBLI::fonte::kenhub","NEBLI::referencia-externa::kenhub","NEBLI::referencia-externa::piloto",
                            f"NEBLI::referencia-externa::tema::{theme}",f"NEBLI::referencia-externa::unidade::{rec['unit']}"]})
                if not nid: raise RuntimeError(f"addNote falhou: {stable}")
                cards=A("findCards",query=f"nid:{nid}"); A("suspend",cards=cards); created.append(nid)
        ids=A("findNotes",query='tag:NEBLI::referencia-externa::piloto')
        cards=A("findCards",query='tag:NEBLI::referencia-externa::piloto')
        susp=A("areSuspended",cards=cards)
        if len(ids)!=190 or len(cards)!=190 or not all(susp):
            raise RuntimeError(f"readback falhou: notas={len(ids)} cards={len(cards)} suspensos={sum(susp)}")
    receipt={"at":datetime.now(timezone.utc).isoformat(),"root":root,"model":MODEL,"created":created,"existing":existing,
             "notes":len(ids),"cards":len(cards),"suspended":sum(susp),"media":media_names,"sync":False}
    (run/"receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
    with STATE.open("a") as f:
        f.write(json.dumps({"at":receipt["at"],"state":"INSTALLED","notes":len(ids),"cards":len(cards),"suspended":sum(susp)})+"\n")
    print(json.dumps({"created":len(created),"existing":len(existing),"notes":len(ids),"cards":len(cards),"suspended":sum(susp)},ensure_ascii=False))
    return receipt


def reconcile() -> dict:
    """Atualiza mídia e hierarquia do piloto no lugar; preserva IDs, comentários e suspensão."""
    cfg=_read(CONFIG); manifest=_read(MANIFEST); run=Path(manifest["pilot_run"]); report=_read(run/"relatorio.json")
    A=Anki(); root=cfg["deck_root"]; old_root="Referência::Referência externa::Kenhub"; updated=[]
    with escrita(A,"reconciliar visual e hierarquia do piloto Kenhub",sync=False):
        for unit in UNITS:
            for theme in cfg["visual_themes"]:
                domain=unit["domain"].capitalize()
                A("createDeck",deck=f"{root}::Piloto::{theme.capitalize()}::{domain}::{unit['module']}::{unit['order']:02d} {unit['title']}")
        for rec in report["cards"]:
            unit=next(u for u in UNITS if u["slug"]==rec["unit"]); domain=unit["domain"].capitalize()
            for theme in cfg["visual_themes"]:
                stable=f"khref:{rec['unit']}:{rec['structure']}:{theme}"
                ids=A("findNotes",query=f'"ID (hidden):{stable}"')
                if len(ids)!=1: raise RuntimeError(f"identidade {stable}: {len(ids)} notas")
                files={}
                for side in ("front","back"):
                    p=Path(rec["themes"][theme][side]); name=f"khref-{hashlib.sha256(stable.encode()).hexdigest()[:16]}-{side}.jpg"
                    A("storeMediaFile",filename=name,data=base64.b64encode(p.read_bytes()).decode()); files[side]=name
                A("updateNoteFields",note={"id":ids[0],"fields":{"Imagem Frente":f'<img src="{files["front"]}">',
                                                                   "Imagem Verso":f'<img src="{files["back"]}">'}})
                cards=A("findCards",query=f"nid:{ids[0]}")
                deck=f"{root}::Piloto::{theme.capitalize()}::{domain}::{unit['module']}::{unit['order']:02d} {unit['title']}"
                A("changeDeck",cards=cards,deck=deck); updated.append(ids[0])
        cards=A("findCards",query='tag:NEBLI::referencia-externa::piloto'); info=A("cardsInfo",cards=cards)
        susp=A("areSuspended",cards=cards)
        if len(updated)!=190 or len(cards)!=190 or not all(susp) or any(not x["deckName"].startswith(root+"::") for x in info):
            raise RuntimeError("readback da reconciliação falhou")
        if not A("findCards",query=f'deck:"{old_root}"'):
            antigos=[d for d in A("deckNames") if d==old_root or d.startswith(old_root+"::")]
            if antigos: A("deleteDecks",decks=[old_root],cardsToo=False)
    receipt={"at":datetime.now(timezone.utc).isoformat(),"updated":len(updated),"cards":len(cards),"suspended":sum(susp),
             "root":root,"decks":sorted({x["deckName"] for x in info}),"sync":False}
    (run/"reconcile-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(receipt,ensure_ascii=False))
    return receipt


if __name__ == "__main__":
    import sys
    reconcile() if sys.argv[1:] == ["--reconcile"] else install() if sys.argv[1:] == ["--install"] else build()
