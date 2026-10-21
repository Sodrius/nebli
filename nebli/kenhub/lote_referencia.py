"""Monta localmente uma leva visual da Referência Externa Kenhub.

Não escreve no Anki. A entrada é um catálogo JSON privado com dez unidades; a
saída contém imagens ciano, folhas de contato, cobertura e identidades estáveis.
"""
from __future__ import annotations

import hashlib
import io
import base64
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from nebli.kenhub import mascara
from nebli.kenhub.piloto_referencia import _compor, _folhas
from nebli.kenhub.piloto_referencia import MODEL
from nebli.kenhub.referencia_externa import CONFIG, _read as _read_config, anki_write_plan_gate, checkpoint_gate
from nebli.decks import Anki, escrita, em_tela


UNIT_TAG_PREFIX = "NEBLI::referencia-externa::unidade::"


def _aliases_by_canonical(reused: list[dict]) -> dict[str, list[str]]:
    """Canonical id -> every unit that reuses it, including same-batch written cards."""
    aliases: dict[str, set[str]] = {}
    for row in reused:
        canonical, unit = row.get("canonical"), row.get("unit")
        if canonical and unit:
            aliases.setdefault(canonical, set()).add(unit)
    return {canonical: sorted(units) for canonical, units in aliases.items()}


def _unit_tags(unit: str, stable_id: str, aliases: dict[str, list[str]]) -> list[str]:
    """All ownership tags a new canonical note must receive on its first write."""
    return [UNIT_TAG_PREFIX + slug for slug in dict.fromkeys([unit, *aliases.get(stable_id, [])])]


def written_fallback_gate(cards: list[dict]) -> list[str]:
    """Written fallbacks teach one relation and never expose provenance visibly."""
    problems = []
    for card in cards:
        stable = card.get("stable_id", "?")
        visible = " ".join(str(card.get(k, "")) for k in ("text", "extra"))
        plain = re.sub(r"<[^>]+>", " ", visible)
        plain = re.sub(r"\s+", " ", plain).strip()
        if re.search(r"\bkenhub\b", plain, re.I):
            problems.append(f"G48 {stable}: fallback exibe Kenhub no conteúdo visível")
        clozes = re.findall(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", visible, re.S)
        context = re.sub(r"\{\{c\d+::.*?(?:::[^}]*)?\}\}", "___", plain)
        list_prompt = re.search(
            r"(?:^|[.!?]\s*)(?:quais|liste|enumere|estruturas?|componentes?|partes?)\b|"
            r"\b(?:inclui|incluem|é formado por|são formados por)\s*[:\-]",
            context, re.I,
        )
        cloze_list = any(len(re.findall(r"(?:,|;|<br\s*/?>|\n)", answer, re.I)) >= 2 for answer in clozes)
        if len(clozes) != 1 or list_prompt or cloze_list:
            problems.append(f"G48 {stable}: fallback escrito enumerativo; esperado um fato relacional atômico")
        lexical = re.sub(r"[_\W]+", "", context, flags=re.UNICODE)
        if len(lexical) < 18:
            problems.append(f"G48 {stable}: fallback sem contexto relacional suficiente")
    return problems


def reuse_canonical_gate(reused: list[dict], canonical_ids: set[str]) -> list[str]:
    """G50: every reuse must point directly to an existing canonical note."""
    problems = []
    reused_ids = {row.get("stable_id") for row in reused if row.get("stable_id")}
    for row in reused:
        canonical = row.get("canonical")
        if not canonical:
            problems.append(f"G50 {row.get('unit','?')}/{row.get('structure','?')}: canonical ausente")
        elif canonical in reused_ids:
            problems.append(f"G50 {row.get('unit','?')}/{row.get('structure','?')}: cadeia de reuso")
        elif canonical not in canonical_ids:
            problems.append(f"G50 {row.get('unit','?')}/{row.get('structure','?')}: canonical inexistente {canonical}")
    return problems


def global_catalog_live_gate(catalog: dict, live_notes: list[dict], expected_units: int = 235) -> list[str]:
    """Compare the official catalog with unit tags from a read-only live snapshot."""
    units = catalog.get("units", catalog.get("catalog", []))
    official = [u.get("slug") for u in units if isinstance(u, dict) and u.get("slug")]
    problems = []
    if len(official) != expected_units:
        problems.append(f"G49 catálogo oficial tem {len(official)} unidades, esperado {expected_units}")
    counts = {slug: official.count(slug) for slug in set(official)}
    duplicates = sorted(slug for slug, count in counts.items() if count > 1)
    if duplicates:
        problems.append(f"G49 slugs duplicados no catálogo oficial: {duplicates[:8]}")
    live = set()
    for note in live_notes:
        for tag in note.get("tags", []):
            if tag.startswith(UNIT_TAG_PREFIX):
                live.add(tag[len(UNIT_TAG_PREFIX):])
    wanted = set(official)
    missing, extra = sorted(wanted - live), sorted(live - wanted)
    if missing:
        problems.append(f"G49 unidades oficiais sem tag viva ({len(missing)}): {missing[:8]}")
    if extra:
        problems.append(f"G49 tags vivas fora do catálogo ({len(extra)}): {extra[:8]}")
    return problems


def _read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _whole_image_overlays(size: tuple[int, int], label: str) -> tuple[bytes, bytes, dict]:
    """Fallback explícito para conceitos representados pela figura inteira, sem alvo verde local."""
    w, h = size; scale = mascara.ESCALA
    def layer(text: str) -> bytes:
        im = Image.new("RGBA", (w * scale, h * scale), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        font_size = (28 if text == "?" else max(22, int(w / 30))) * scale
        try: font = ImageFont.truetype(mascara.FONTE, font_size, index=1)
        except OSError: font = ImageFont.load_default()
        max_width = int(w * .54) * scale
        words=text.split(); lines=[]; cur=""
        for word in words:
            nxt=(cur+" "+word).strip()
            if not cur or d.textlength(nxt,font=font) <= max_width: cur=nxt
            else: lines.append(cur); cur=word
        lines.append(cur)
        line_h=int(font_size*1.18); box_w=int(max(d.textlength(x,font=font) for x in lines)+24*scale)
        box_h=line_h*len(lines)+16*scale; x=16*scale; y=16*scale
        d.rounded_rectangle((x,y,x+box_w,y+box_h),radius=7*scale,fill=(232,251,255,242),
                            outline=(0,174,199,255),width=2*scale)
        ty=y+(box_h-line_h*len(lines))/2
        for line in lines:
            lw=d.textlength(line,font=font); d.text((x+(box_w-lw)/2,ty),line,font=font,fill=(20,28,30,255)); ty+=line_h
        b=io.BytesIO(); im.save(b,"PNG",optimize=True); return b.getvalue()
    return layer("?"), layer(label), {"mode":"whole_image","arrow":False,"reason":"conceito representado pela figura inteira"}


def build(catalog: Path) -> dict:
    batch = _read(catalog)
    expected_units = int(batch.get("expected_units", 50))
    final_batch = bool(batch.get("final_batch", False))
    if expected_units != (35 if final_batch else 50):
        raise SystemExit(f"G40: tamanho declarado inválido ({expected_units})")
    if len(batch.get("units", [])) != expected_units:
        raise SystemExit(f"G40: catálogo da leva precisa ter exatamente {expected_units} unidades")
    out = catalog.parent / "build-ciano"
    out.mkdir(parents=True, exist_ok=True)
    report = {"schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
              "theme": "ciano", "catalog": str(catalog), "units": [], "cards": [],
              "exceptions": [], "written": [], "reused": [], "whole_image": [], "failures": []}
    exact: dict[tuple[str, str], str] = {}
    written_exact: dict[str, str] = {}
    canonical_ids: set[str] = set()
    # Deduplicação global antes de renderizar: evita custo e cadeias de reuso.
    for previous in sorted(catalog.parent.parent.glob("lote-*/build-ciano/relatorio.json")):
        if previous == out / "relatorio.json": continue
        prior=_read(previous)
        for c in prior.get("cards", []):
            exact[(c["structure"],c["source_sha256"])]=c["stable_id"]
            canonical_ids.add(c["stable_id"])
        for c in prior.get("written", []):
            written_exact[c["structure"]]=c["stable_id"]
            canonical_ids.add(c["stable_id"])
    for unit in batch["units"]:
        src = Path(unit["source_dir"]) / "itens.json"
        data = _read(src)
        urec = {**unit, "targets": len(data["itens"]), "built": 0, "written": 0, "reused": 0,
                "exceptions": [], "state": "BUILT"}
        written_specs = {x["structure"]: x for x in unit.get("written_cards", [])}
        for item in data["itens"]:
            if item.get("sem_figura"):
                spec = written_specs.get(item["slug"])
                wid = f"khref-text:{unit['slug']}:{item['slug']}" if spec else None
                exc = {"unit": unit["slug"], "structure": item["slug"], "reason": "sem_figura"}
                if wid:
                    canonical=spec.get("reuse_id") or written_exact.get(item["slug"])
                    exc["written_id"] = canonical or wid
                    if canonical:
                        report["reused"].append({"unit":unit["slug"],"structure":item["slug"],"canonical":canonical})
                        urec["reused"] += 1
                    else:
                        report["written"].append({"stable_id": wid, "unit": unit["slug"],
                            "structure": item["slug"], "text": spec["text"], "extra": spec["extra"]})
                        written_exact[item["slug"]]=wid; urec["written"] += 1
                report["exceptions"].append(exc); urec["exceptions"].append(exc); continue
            image = src.parent / item["arquivo"]
            source_sha = hashlib.sha256(image.read_bytes()).hexdigest()
            key = (item["slug"], source_sha)
            stable = f"khref:{unit['slug']}:{item['slug']}:ciano"
            if key in exact:
                reuse = {"unit": unit["slug"], "structure": item["slug"], "canonical": exact[key]}
                report["reused"].append(reuse); urec["reused"] += 1; continue
            try:
                base = Image.open(image).convert("RGB")
                region = mascara.regiao(str(image))
                name = item.get("nome_pt") or item["nome_en"]
                try:
                    front, back, meta = mascara.overlays(base.size, region, name, cobrir=False, tema="ciano")
                except ValueError as exc:
                    if "não há lugar" not in str(exc): raise
                    front, back, meta = _whole_image_overlays(base.size, name)
                    report["whole_image"].append({"unit":unit["slug"],"structure":item["slug"],"reason":str(exc)})
                dest = out / f"{unit['module_order']:02d}-{unit['module_slug']}" / f"{unit['unit_order']:02d}-{unit['slug']}"
                dest.mkdir(parents=True, exist_ok=True)
                stem = hashlib.sha256(stable.encode()).hexdigest()[:20]
                fp, bp = dest / f"{stem}-front.jpg", dest / f"{stem}-back.jpg"
                _compor(base, front).save(fp, quality=90)
                _compor(base, back).save(bp, quality=90)
                report["cards"].append({"stable_id": stable, "unit": unit["slug"],
                    "structure": item["slug"], "name": name, "name_en": item["nome_en"],
                    "source_sha256": source_sha, "front": str(fp), "back": str(bp), "meta": meta})
                exact[key] = stable; urec["built"] += 1
            except ValueError as exc:
                if "sem marcação verde" in str(exc):
                    try:
                        base = Image.open(image).convert("RGB"); name = item.get("nome_pt") or item["nome_en"]
                        front, back, meta = _whole_image_overlays(base.size, name)
                        dest = out / f"{unit['module_order']:02d}-{unit['module_slug']}" / f"{unit['unit_order']:02d}-{unit['slug']}"
                        dest.mkdir(parents=True, exist_ok=True); stem = hashlib.sha256(stable.encode()).hexdigest()[:20]
                        fp, bp = dest / f"{stem}-front.jpg", dest / f"{stem}-back.jpg"
                        _compor(base, front).save(fp, quality=90); _compor(base, back).save(bp, quality=90)
                        report["cards"].append({"stable_id":stable,"unit":unit["slug"],"structure":item["slug"],
                            "name":name,"name_en":item["nome_en"],"source_sha256":source_sha,
                            "front":str(fp),"back":str(bp),"meta":meta})
                        report["whole_image"].append({"unit":unit["slug"],"structure":item["slug"],"reason":str(exc)})
                        exact[key]=stable; urec["built"]+=1
                    except Exception as fallback_exc:
                        report["failures"].append({"unit":unit["slug"],"structure":item["slug"],"error":str(fallback_exc)})
                else: report["failures"].append({"unit":unit["slug"],"structure":item["slug"],"error":str(exc)})
            except Exception as exc:
                report["failures"].append({"unit":unit["slug"],"structure":item["slug"],"error":str(exc)})
        report["units"].append(urec)
    rows = [{"name": r["name"], "front": r["front"], "back": r["back"]} for r in report["cards"]]
    report["contact_sheets"] = _folhas(rows, out / "folhas", per=8)
    if report["failures"]:
        report["gate_problems"] = [f"montagem: {len(report['failures'])} falhas"]
    else:
        for u in report["units"]: u["state"] = "VERIFIED"
        report["gate_problems"] = checkpoint_gate({"units": report["units"]}, final=final_batch)
        report["gate_problems"] += written_fallback_gate(report["written"])
        report["gate_problems"] += written_fallback_gate(batch.get("canonical_updates", []))
        canonical_ids.update(c["stable_id"] for c in report["cards"])
        canonical_ids.update(c["stable_id"] for c in report["written"])
        report["gate_problems"] += reuse_canonical_gate(report["reused"], canonical_ids)
    report["gate_ok"] = not report["gate_problems"]
    (out / "relatorio.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"cards": len(report["cards"]), "written": len(report["written"]), "reused": len(report["reused"]),
                      "exceptions": len(report["exceptions"]), "failures": len(report["failures"]),
                      "sheets": len(report["contact_sheets"]), "gate_ok": report["gate_ok"],
                      "out": str(out)}, ensure_ascii=False))
    return report


def install(catalog: Path) -> dict:
    """Instala a leva pronta numa única janela de escrita, sempre suspensa e sem sync."""
    cfg = _read_config(CONFIG); batch = _read(catalog); report = _read(catalog.parent / "build-ciano" / "relatorio.json")
    if not report.get("gate_ok") or report.get("failures"):
        raise SystemExit("instalação bloqueada: montagem não passou nos gates")
    final_batch = bool(batch.get("final_batch", False))
    expected_units = int(batch.get("expected_units", 50))
    problems = checkpoint_gate({"units": report["units"]}, final=final_batch)
    plan = {"prepared_outside_anki": True, "write_sessions": 1, "readbacks": 1,
            "per_card_calls": 0, "sync": False}
    problems += anki_write_plan_gate(plan)
    if problems: raise SystemExit("\n".join(problems))
    A = Anki()
    if MODEL not in A("modelNames"): raise SystemExit(f"tipo de nota ausente: {MODEL}")
    text_model = "NEBLI UC07 AnKing v1"
    if text_model not in A("modelNames"): raise SystemExit(f"tipo de nota ausente: {text_model}")
    live = A("notesInfo", notes=A("findNotes", query='tag:NEBLI::referencia-externa::kenhub'))
    live_ids = {}
    live_by_id = {}
    for n in live:
        stable=n["fields"].get("ID (hidden)",{}).get("value") or n["fields"].get("ankihub_id",{}).get("value")
        if stable:
            live_ids[stable]=n["noteId"]
            live_by_id[stable]=n
    aliases = _aliases_by_canonical(report["reused"])
    reuse_tag_actions=[]
    for unit in sorted({r["unit"] for r in report["reused"]}):
        nids=sorted({live_ids[r["canonical"]] for r in report["reused"] if r["unit"]==unit and r["canonical"] in live_ids})
        if nids: reuse_tag_actions.append({"action":"addTags","version":6,"params":{"notes":nids,
            "tags":f"NEBLI::referencia-externa::unidade::{unit}"}})
    units = {u["slug"]: u for u in batch["units"]}; root = cfg["deck_root"]
    media_actions=[]; notes=[]; expected=[]
    for card in report["cards"]:
        stable=card["stable_id"]
        if stable in live_ids: continue
        unit=units[card["unit"]]
        deck=f"{root}::{unit['domain']}::{unit['module_order']:02d} {unit['module']}::{unit['section_order']:02d} {unit['section']}::{unit['unit_order']:02d} {unit['title']}"
        files={}
        for side in ("front","back"):
            p=Path(card[side]); name=f"khref-{hashlib.sha256(stable.encode()).hexdigest()[:20]}-{side}.jpg"
            media_actions.append({"action":"storeMediaFile","version":6,"params":{"filename":name,"path":str(p)}})
            files[side]=name
        unit_tags = _unit_tags(card["unit"], stable, aliases)
        notes.append({"deckName":deck,"modelName":MODEL,"options":{"allowDuplicate":True},"fields":{
            "Nome PT":card["name"],"Nome EN":card["name_en"],"Imagem Frente":f'<img src="{files["front"]}">',
            "Imagem Verso":f'<img src="{files["back"]}">',"Fonte":"Kenhub","ID (hidden)":stable,
            "NEBLI_Comentario":"","NEBLI_Resposta":""},"tags":["NEBLI::fonte::kenhub",
            "NEBLI::referencia-externa::kenhub","NEBLI::referencia-externa::tema::ciano",
            f"NEBLI::referencia-externa::lote::{batch['batch']:03d}",f"NEBLI::referencia-externa::modulo::{unit['module_slug']}",*unit_tags]})
        expected.append(stable)
    text_fields=A("modelFieldNames",modelName=text_model)
    for card in report.get("written", []):
        if card["stable_id"] in live_ids: continue
        unit=units[card["unit"]]
        deck=f"{root}::{unit['domain']}::{unit['module_order']:02d} {unit['module']}::{unit['section_order']:02d} {unit['section']}::{unit['unit_order']:02d} {unit['title']}"
        fields={f:"" for f in text_fields}; fields["Text"]=card["text"]
        fields["Extra"]=card["extra"]; fields["ankihub_id"]=card["stable_id"]
        unit_tags = _unit_tags(card["unit"], card["stable_id"], aliases)
        # Um fallback escrito também pode ser o canônico de alvos repetidos
        # dentro da própria leva. As aliases precisam nascer na nota nova;
        # antes ela só era etiquetada na aula de origem e o G47 vivo falhava.
        notes.append({"deckName":deck,"modelName":text_model,"options":{"allowDuplicate":True},"fields":fields,
          "tags":["NEBLI::fonte::kenhub","NEBLI::referencia-externa::kenhub","NEBLI::referencia-externa::tema::ciano",
          "NEBLI::referencia-externa::texto-sem-figura",f"NEBLI::referencia-externa::lote::{batch['batch']:03d}",
          *unit_tags]})
    deck_actions=[]
    for unit in batch["units"]:
        deck=f"{root}::{unit['domain']}::{unit['module_order']:02d} {unit['module']}::{unit['section_order']:02d} {unit['section']}::{unit['unit_order']:02d} {unit['title']}"
        deck_actions.append({"action":"createDeck","version":6,"params":{"deck":deck}})
    visible_source_updates=[]
    for n in live:
        if "NEBLI::referencia-externa::texto-sem-figura" not in n["tags"]: continue
        old=n["fields"].get("Extra",{}).get("value","")
        new=old.removeprefix("<b>Kenhub</b><br>")
        if new != old: visible_source_updates.append({"action":"updateNoteFields","version":6,
            "params":{"note":{"id":n["noteId"],"fields":{"Extra":new}}}})
    canonical_updates=[]
    for spec in batch.get("canonical_updates", []):
        stable=spec["stable_id"]
        if stable not in live_by_id:
            raise SystemExit(f"G51: canônico a corrigir não existe ao vivo: {stable}")
        canonical_updates.append({"action":"updateNoteFields","version":6,
            "params":{"note":{"id":live_ids[stable],"fields":{"Text":spec["text"],"Extra":spec["extra"]}}}})
    touched={a["params"]["note"]["id"] for a in visible_source_updates}
    touched.update(a["params"]["note"]["id"] for a in canonical_updates)
    touched.update(n for a in reuse_tag_actions for n in a["params"]["notes"])
    if em_tela(A).intersection(touched): raise SystemExit("adiado: uma nota que seria atualizada está em tela")
    with escrita(A, f"Referência Kenhub lote {batch['batch']:03d} ({expected_units} unidades, ciano)", sync=False):
        first=A("multi",actions=deck_actions)
        if any(x.get("error") for x in first): raise RuntimeError(first)
        if visible_source_updates:
            cleaned=A("multi",actions=visible_source_updates)
            if any(x.get("error") for x in cleaned): raise RuntimeError(cleaned)
        if canonical_updates:
            corrected=A("multi",actions=canonical_updates)
            if any(x.get("error") for x in corrected): raise RuntimeError(corrected)
        if reuse_tag_actions:
            linked=A("multi",actions=reuse_tag_actions)
            if any(x.get("error") for x in linked): raise RuntimeError(linked)
        for i in range(0,len(media_actions),25):
            result=A("multi",actions=media_actions[i:i+25])
            if any(x.get("error") for x in result): raise RuntimeError(result)
        nids=A("addNotes",notes=notes)
        if len(nids)!=len(notes) or any(n is None for n in nids): raise RuntimeError("addNotes incompleto")
        new_cards=[c for n in A("notesInfo",notes=nids) for c in n["cards"]]
        A("suspend",cards=new_cards)
        rb=A("multi",actions=[
          {"action":"findNotes","version":6,"params":{"query":f'tag:NEBLI::referencia-externa::lote::{batch["batch"]:03d}'}},
          {"action":"findCards","version":6,"params":{"query":f'tag:NEBLI::referencia-externa::lote::{batch["batch"]:03d}'}},
          {"action":"areSuspended","version":6,"params":{"cards":new_cards}},
        ] + [{"action":"findNotes","version":6,"params":{"query":f'"tag:NEBLI::referencia-externa::unidade::{u["slug"]}"'}} for u in batch["units"]])
    got_notes,got_cards,suspended=[x["result"] for x in rb[:3]]
    expected_total=len(report["cards"])+len(report.get("written", []))
    if len(got_notes)!=expected_total or len(got_cards)!=expected_total or not all(suspended):
        raise RuntimeError({"notes":len(got_notes),"cards":len(got_cards),"suspended":sum(suspended)})
    coverage=[]
    for unit,res in zip(batch["units"],rb[3:]):
        want=len(_read(Path(unit["source_dir"])/"itens.json")["itens"]); got=len(res["result"])
        if want!=got: coverage.append({"unit":unit["slug"],"targets":want,"linked":got})
    if coverage: raise RuntimeError({"G47_live_coverage":coverage})
    receipt={"at":datetime.now(timezone.utc).isoformat(),"batch":batch["batch"],"units":expected_units,
             "created":len(nids),"existing":expected_total-len(nids),"cards":len(got_cards),
             "suspended":sum(suspended),"media":len(media_actions),"write_plan":plan,"sync":False}
    (catalog.parent/"receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(receipt,ensure_ascii=False)); return receipt


if __name__ == "__main__":
    import sys
    install(Path(sys.argv[2])) if sys.argv[1:2] == ["--install"] else build(Path(sys.argv[1]))
