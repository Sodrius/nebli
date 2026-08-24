#!/usr/bin/env python3
"""Fecha o lote de feedback NEBLI de 2026-07-15 com snapshot e ledger.

Ordem da transacao: snapshot -> reparos -> novos cards -> flags -> filas ->
arquivamento de comentarios -> pos-condicoes. Suspensoes estruturais permanecem.
"""
from __future__ import annotations

import base64
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nebli_anki import call

STAMP = "2026-07-15"
OUT = Path("arquivos-trabalho/mutirao-qualidade/feedback")
TARGETS = [
    1783811944436, 1783971558300, 1783971566659, 1783971568750,
    1783971570862, 1783971577114, 1783971600144, 1783971602229,
    1783971604310, 1783971950832, 1783971957137, 1783971961342,
    1783971980435,
]

REPAIRS = {
    1783811944436: (
        "During gastrulation, epiblast cells that remain at the surface become {{c1::ectoderm}}.",
        "Cells that ingress deepest replace the hypoblast and form endoderm; cells that settle between endoderm and ectoderm form mesoderm.",
    ),
    1783971558300: (
        "Blood flows down a {{c1::decreasing}} pressure gradient: artery → arteriole → capillary → venule → vein.",
        "The pressure drop is greatest across arterioles, whose resistance regulates downstream capillary flow.",
    ),
    1783971566659: (
        "The luminal surface of blood vessels is lined by {{c1::simple squamous epithelium}} called endothelium.",
        "Endothelial cells form a thin, low-resistance interface between blood and the vessel wall.",
    ),
    1783971568750: (
        "Endothelial nitric oxide relaxes vascular smooth muscle, producing {{c1::vasodilation::process}}.",
        "NO diffuses into smooth muscle and activates soluble guanylyl cyclase, increasing cGMP and lowering contractile tone.",
    ),
    1783971570862: (
        "At a vessel injury, endothelial {{c1::von Willebrand factor (vWF)}} promotes platelet adhesion.",
        "vWF is a multimeric adhesive glycoprotein that bridges exposed subendothelial collagen to platelet GPIb; it also carries factor VIII.",
    ),
    1783971577114: (
        "An artery whose tunica media is dominated by smooth muscle is a {{c1::muscular artery}}.",
        "Muscular arteries (for example radial, tibial, and splenic arteries) regulate caliber to distribute blood to organs.",
    ),
    1783971600144: (
        "Venous valves are semilunar folds of the {{c1::tunica intima}}.",
        "Valves prevent reflux; incompetence permits venous pooling and contributes to varicosities.",
    ),
    1783971602229: (
        "Discontinuous endothelial junctions that form flap-like entry portals in initial lymphatics are {{c1::button junctions}}.",
        "Overlapping endothelial flaps act as microvalves; anchoring filaments favor opening when interstitial pressure rises.",
    ),
    1783971604310: (
        "Compared with veins, lymphatic collecting vessels contain many more {{c1::valves}}.",
        "Because lymph has no central pump, valves convert intermittent compression by skeletal muscle and nearby arteries into forward flow.",
    ),
    1783971950832: (
        "Bone marrow and thymus are {{c1::primary lymphoid organs}}, where lymphocytes develop and mature.",
        "Primary organs generate immunocompetent lymphocytes before antigen-driven activation.",
    ),
}

SPLITS = {
    1783971600144: (
        "The main external force propelling venous blood from the limbs is the {{c1::skeletal muscle pump}}.",
        "Muscle contraction compresses veins; valves enforce one-way flow toward the heart.",
    ),
    1783971950832: (
        "Lymph nodes, spleen, and MALT are {{c1::secondary lymphoid organs}}, where mature lymphocytes encounter antigen.",
        "Secondary organs organize antigen presentation and expansion of activated lymphocyte clones.",
    ),
}


def fields(note):
    return {k: v.get("value", "") for k, v in note["fields"].items()}


def front_field(note):
    for name in ("Text", "Texto", "Front", "Question", "Pergunta", "Cloze"):
        if name in note["fields"]:
            return name
    raise RuntimeError(f"sem campo de frente: {note['noteId']}")


def extra_field(note):
    for name in ("Extra", "Remarks", "Back Extra", "Explicacao", "Explicação"):
        if name in note["fields"]:
            return name
    raise RuntimeError(f"sem campo Extra: {note['noteId']}")


def get_all_nebli_notes():
    ids = call("findNotes", query="tag:NEBLI::*")
    return call("notesInfo", notes=ids) if ids else []


def card_snapshot(card):
    return {k: card.get(k) for k in ("cardId", "note", "deckName", "ord", "queue", "type", "flags")}


def normalize_tags(tags, *, visual="optional", status="not_needed", role="context"):
    bad_prefixes = ("img::", "NEBLI::image_", "NEBLI::visual_need::", "NEBLI_comentario::")
    kept = [t for t in tags if not t.startswith(bad_prefixes)]
    kept += [f"NEBLI::visual_need::{visual}", f"NEBLI::image_status::{status}",
             f"NEBLI::image_role::{role}", f"NEBLI::feedback_resolved::{STAMP}"]
    return sorted(set(kept))


def set_tags(nid, old, new):
    remove = sorted(set(old) - set(new))
    add = sorted(set(new) - set(old))
    if remove:
        call("removeTags", notes=[nid], tags=" ".join(remove))
    if add:
        call("addTags", notes=[nid], tags=" ".join(add))


def update_repair(note, text, extra):
    call("updateNoteFields", note={"id": note["noteId"], "fields": {
        front_field(note): text, extra_field(note): extra,
    }})
    set_tags(note["noteId"], note.get("tags", []), normalize_tags(note.get("tags", [])))


def clone_atomic(note, deck, text, extra, kind):
    existing = call("findNotes", query=(
        f'tag:"NEBLI::source_note::{note["noteId"]}" '
        f'tag:"NEBLI::split_part::{kind}" -nid:{note["noteId"]}'
    ))
    if existing:
        return existing[0]
    fs = fields(note)
    fs[front_field(note)] = text
    fs[extra_field(note)] = extra
    if "NEBLI_Comentario" in fs:
        fs["NEBLI_Comentario"] = ""
    if "NEBLI_Resposta" in fs:
        fs["NEBLI_Resposta"] = ""
    tags = normalize_tags(note.get("tags", [])) + [
        f"NEBLI::source_note::{note['noteId']}", f"NEBLI::split_part::{kind}",
    ]
    return call("addNote", note={"deckName": deck, "modelName": note["modelName"],
        "fields": fs, "tags": sorted(set(tags)), "options": {"allowDuplicate": True}})


def make_thymus_io(source_note, deck):
    existing = call("findNotes", query=(
        f'tag:"NEBLI::source_note::{source_note}" '
        'tag:"NEBLI::image_status::approved" note:"IO-one by one (AnKing Step Deck / AnKingMed)"'
    ))
    if existing:
        return existing[0], "existing", "existing"
    source = OUT / "09eef7eceecc6ad0163959e46b1cba32.webp"
    if not source.exists():
        raw = call("retrieveMediaFile", filename=source.name)
        source.write_bytes(base64.b64decode(raw))
    # Um unico lobulo infantil; evita que outros rotulos Co/M revelem a resposta.
    crop = Image.open(source).convert("RGB").crop((65, 350, 250, 520))
    local = OUT / "thymus-lobule-cortex-medulla.png"
    crop.save(local, "PNG")
    raw = local.read_bytes()
    media = hashlib.sha256(raw).hexdigest()[:32] + ".png"
    call("storeMediaFile", filename=media, data=base64.b64encode(raw).decode("ascii"))
    model = "IO-one by one (AnKing Step Deck / AnKingMed)"
    fs = {name: "" for name in call("modelFieldNames", modelName=model)}
    fs.update({
        "Image": f'<img src="{media}">',
        "Header": "Thymus histology — identify the highlighted region",
        "I0": "[#!occlusions [[rect0::31,14,32,25]]<br>[[rect0::139,14,27,25]] #]<br>active",
        "Extra": "The cortex is darker because it is densely packed with immature thymocytes; the medulla is paler and contains fewer lymphocytes. Source crop: imported Histology deck, Fig. 14-8.",
    })
    nid = call("addNote", note={"deckName": deck, "modelName": model, "fields": fs,
        "tags": ["NEBLI::histo-11-orgaos-linfaticos", "NEBLI::feedback_resolved::2026-07-15",
                 "NEBLI::image_role::recognition", "NEBLI::image_status::approved",
                 "NEBLI::visual_need::required", f"NEBLI::source_note::{source_note}"],
        "options": {"allowDuplicate": True}})
    return nid, str(local), media


def clear_flags(card_ids):
    if not card_ids:
        return "none"
    try:
        call("setFlag", cards=card_ids, flag=0)
        return "setFlag"
    except RuntimeError:
        for cid in card_ids:
            call("setSpecificValueOfCard", card=cid, keys=["flags"], newValues=[0], warning_check=True)
        return "setSpecificValueOfCard"


def main():
    try:
        current = call("guiCurrentCard")
    except RuntimeError as exc:
        if "not currently active" not in str(exc):
            raise
        current = None
    if current:
        print(json.dumps({"status": "deferred_reviewer_active", "card_id": current.get("cardId")}, indent=2))
        raise SystemExit(75)
    OUT.mkdir(parents=True, exist_ok=True)
    all_notes = get_all_nebli_notes()
    by_id = {n["noteId"]: n for n in all_notes}
    feedback_notes = [n for n in all_notes if
        n.get("fields", {}).get("NEBLI_Comentario", {}).get("value", "").strip()
        or any(t.startswith("NEBLI_comentario::") for t in n.get("tags", []))]
    flag_ids = sorted(set(sum((call("findCards", query=f"tag:NEBLI::* flag:{f}") for f in range(1, 8)), [])))
    involved = sorted(set(TARGETS + [n["noteId"] for n in feedback_notes]
                          + (call("cardsToNotes", cards=flag_ids) if flag_ids else [])))
    involved_notes = call("notesInfo", notes=involved)
    all_cards = call("findCards", query=" OR ".join(f"nid:{nid}" for nid in involved))
    card_info = call("cardsInfo", cards=all_cards) if all_cards else []
    deck_by_note = {}
    for c in card_info:
        deck_by_note.setdefault(c["note"], c["deckName"])
    fresh_ledger = {
        "generated_at": dt.datetime.now().astimezone().isoformat(),
        "scope": "feedback, flags e suspensoes sinalizados; suspensoes estruturais preservadas",
        "notes_before": [{"note_id": n["noteId"], "model": n["modelName"],
            "fields": fields(n), "tags": n.get("tags", [])} for n in involved_notes],
        "cards_before": [card_snapshot(c) for c in card_info],
        "flag_card_ids": flag_ids,
        "created_note_ids": [], "decisions": [],
    }
    ledger_path = OUT / f"LEDGER-FEEDBACK-FECHADO-{STAMP}.json"
    if ledger_path.exists():
        ledger = json.loads(ledger_path.read_text(encoding="utf-8-sig"))
        ledger["resumed_at"] = dt.datetime.now().astimezone().isoformat()
        ledger.setdefault("created_note_ids", [])
        ledger.setdefault("decisions", [])
    else:
        ledger = fresh_ledger
        ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for nid, (text, extra) in REPAIRS.items():
        update_repair(by_id[nid], text, extra)
        ledger["decisions"].append({"note_id": nid, "action": "rewrite_and_remove_bad_image"})

    for nid, (text, extra) in SPLITS.items():
        created = clone_atomic(by_id[nid], deck_by_note[nid], text, extra, "2")
        if created not in ledger["created_note_ids"]:
            ledger["created_note_ids"].append(created)
        ledger["decisions"].append({"note_id": nid, "action": "split", "created_note_id": created})

    # O original do TCR ja possui substituto ativo promovido; apenas explicita o arquivo.
    for nid in (1783971957137,):
        tags = normalize_tags(by_id[nid].get("tags", [])) + ["NEBLI::suspension_reason::replaced_archive"]
        set_tags(nid, by_id[nid].get("tags", []), sorted(set(tags)))
        ledger["decisions"].append({"note_id": nid, "action": "keep_replaced_archive"})

    io_nid, io_asset, io_media = make_thymus_io(1783971980435, deck_by_note[1783971980435])
    if io_nid not in ledger["created_note_ids"]:
        ledger["created_note_ids"].append(io_nid)
    old = by_id[1783971980435]
    tags = normalize_tags(old.get("tags", [])) + ["NEBLI::mutirao_replaced::2026-07-15",
        "NEBLI::suspension_reason::replaced_by_image_occlusion"]
    set_tags(old["noteId"], old.get("tags", []), sorted(set(tags)))
    ledger["decisions"].append({"note_id": old["noteId"], "action": "replace_with_io",
        "created_note_id": io_nid, "asset": io_asset, "media": io_media})

    # Arquiva comentario/resposta nos campos do ledger e limpa o sinal operacional.
    for note in feedback_notes:
        changes = {}
        for name in ("NEBLI_Comentario", "NEBLI_Resposta"):
            if name in note.get("fields", {}) and note["fields"][name].get("value", ""):
                changes[name] = ""
        if changes:
            call("updateNoteFields", note={"id": note["noteId"], "fields": changes})
        current = call("notesInfo", notes=[note["noteId"]])[0]
        new_tags = [t for t in current.get("tags", []) if not t.startswith("NEBLI_comentario::")]
        new_tags.append(f"NEBLI::feedback_resolved::{STAMP}")
        set_tags(note["noteId"], current.get("tags", []), sorted(set(new_tags)))

    flag_method = clear_flags(flag_ids)

    # Estado de estudo: ord 0 volta; clozes obsoletos e originais substituidos ficam fora.
    refreshed_ids = sorted(set(involved + ledger["created_note_ids"]))
    refreshed_cards = call("cardsInfo", cards=call("findCards", query=" OR ".join(f"nid:{n}" for n in refreshed_ids)))
    refreshed_notes = {n["noteId"]: n for n in call("notesInfo", notes=refreshed_ids)}
    to_unsuspend, to_suspend = [], []
    for c in refreshed_cards:
        n = refreshed_notes[c["note"]]
        tags = n.get("tags", [])
        structural = (c.get("ord", 0) > 0 or any("replaced" in t or "blocked_required_visual" in t
                     or "replaced_by_image_occlusion" in t for t in tags))
        if structural:
            to_suspend.append(c["cardId"])
        elif c["note"] in involved or c["note"] in ledger["created_note_ids"]:
            to_unsuspend.append(c["cardId"])
    if to_suspend:
        call("suspend", cards=sorted(set(to_suspend)))
    if to_unsuspend:
        call("unsuspend", cards=sorted(set(to_unsuspend)))

    ledger.update({"flag_method": flag_method, "unsuspended_card_ids": sorted(set(to_unsuspend)),
                   "structural_suspended_card_ids": sorted(set(to_suspend))})
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    remaining_flags = sum((call("findCards", query=f"tag:NEBLI::* flag:{f}") for f in range(1, 8)), [])
    remaining_comments = [n["noteId"] for n in get_all_nebli_notes() if
        n.get("fields", {}).get("NEBLI_Comentario", {}).get("value", "").strip()]
    if remaining_flags or remaining_comments:
        raise RuntimeError(f"pos-condicao falhou: flags={remaining_flags}, comments={remaining_comments}")
    result = {"ledger": str(ledger_path), "repaired": len(REPAIRS), "split_created": len(SPLITS),
              "io_created_note": io_nid, "flags_cleared": len(flag_ids),
              "comments_cleared": len(feedback_notes), "unsuspended": len(set(to_unsuspend)),
              "structural_suspensions_preserved": len(set(to_suspend))}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
