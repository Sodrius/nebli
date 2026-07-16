#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove imagens ruins/inadequadas de cards P3 e marca a decisao visual.

Nao apaga arquivos de media; apenas remove o bloco de imagem do campo Extra.
"""
import argparse
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ANKICONNECT = "http://localhost:8765"
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "flashcards" / "auditorias"

IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
SRC_RE = re.compile(r'<img[^>]+src="([^"]+)"[^>]*>', re.I)
TAG_RE = re.compile(r"<[^>]+>")
CLOZE_RE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", re.S)

# Cards conceituais em que a imagem atual atrapalha mais do que ajuda.
NO_IMAGE_NEEDED = {
    1783811939294,  # gonadal environment decides gametogenesis direction
    1783811939313,  # maternal age / diplotene arrest
    1783811939325,  # protamines
    1783971572973,  # endothelial injury -> plaque
    1783971775488,  # rabies/tetanus retrograde transport
    1783971978359,  # B vs T maturation site
    1783971988862,  # thymic involution
    1783972009783,  # splenectomy / encapsulated bacteria
    1783972437727,  # lymphedema
    1783972464734,  # chylothorax
    1783972580135,  # SVC syndrome
}

# Cards que precisam de imagem/IO especifica, mas a atual nao resolve.
NEEDS_SPECIFIC = {
    1783811939299,  # meiosis I
    1783811939305,  # pachytene crossing-over
    1783811939309,  # asymmetric oogenesis
    1783811939321,  # cortical granules
    1783811939329,  # acrosome membrane fusion
    1783811939333,  # capacitation
    1783811939341,  # ZP3/calcium/acrosome reaction
    1783811939346,  # ZP2/ZP3 cortical block
    1783972266375,  # lacteals/chyle
    1783972441844,  # anchoring filaments
    1783972445971,  # node afferent/efferent anatomy
    1783972460570,  # right lymphatic duct drainage
    1783971595936,  # capillary basal lamina comparison
    1783971750550,  # bipolar neuron morphology
    1783971765121,  # lipofuscin in neuron
    1783971804666,  # cerebellar cortex layers
    1783971986746,  # Hassall corpuscle
    1783971997245,  # subcapsular sinus
    1783972001438,  # PALS
    1783972003526,  # red pulp cords/sinusoids
}


def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]


def clean_text(value):
    value = CLOZE_RE.sub(r"\1", value or "")
    value = TAG_RE.sub(" ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def remove_last_image_block(extra):
    srcs = SRC_RE.findall(extra or "")
    if not srcs:
        return extra or "", 0
    cleaned = extra or ""
    removed = 0
    while True:
        srcs = SRC_RE.findall(cleaned)
        if not srcs:
            break
        last = srcs[-1]
        pos = cleaned.rfind(last)
        img_pos = cleaned.rfind("<img", 0, pos)
        if img_pos == -1:
            break
        end = cleaned.find(">", img_pos)
        end = len(cleaned) if end == -1 else end + 1
        br_pos = cleaned.rfind("<br><br>", 0, img_pos)
        credit_end = end
        next_brbr = cleaned.find("<br><br>", end)
        if next_brbr != -1:
            tail = cleaned[end:next_brbr]
            if "Image from" in tail or "OpenStax" in tail or "Fonte visual" in tail:
                credit_end = next_brbr
        else:
            tail = cleaned[end:]
            if "Image from" in tail or "OpenStax" in tail or "Fonte visual" in tail:
                credit_end = len(cleaned)
        cut_start = br_pos if br_pos != -1 else img_pos
        cleaned = cleaned[:cut_start].rstrip() + cleaned[credit_end:]
        removed += 1
    return cleaned.strip(), removed


def front(note):
    for name in ("Text", "Front", "Header"):
        if name in note.get("fields", {}):
            return clean_text(note["fields"][name]["value"])
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not args.apply and not args.dry_run:
        args.dry_run = True

    ids = sorted(NO_IMAGE_NEEDED | NEEDS_SPECIFIC)
    notes = call("notesInfo", notes=ids)
    rows = []
    for note in notes:
        nid = note["noteId"]
        extra = note.get("fields", {}).get("Extra", {}).get("value", "")
        new_extra, removed = remove_last_image_block(extra)
        if nid in NO_IMAGE_NEEDED:
            decision = "no_image_needed"
            add = "NEBLI::visual_need::none NEBLI::image_status::removed_not_needed img::removida"
            remove = (
                "NEBLI::image_status::context_needs_specific_review "
                "NEBLI::image_status::needs_specific_review "
                "NEBLI::image_status::needs_io_or_manual "
                "NEBLI::image_status::needs_specific_internet_or_io "
                "NEBLI::io_candidate img::generica img::substituir"
            )
        else:
            decision = "needs_specific_image_or_io"
            add = "NEBLI::visual_need::required NEBLI::image_status::missing_specific img::ausente"
            remove = "NEBLI::image_status::context_needs_specific_review img::generica img::substituir"
        rows.append((nid, decision, removed, front(note)[:160]))
        if args.apply:
            if removed:
                call("updateNoteFields", note={"id": nid, "fields": {"Extra": new_extra}})
            call("addTags", notes=[nid], tags=add)
            call("removeTags", notes=[nid], tags=remove)

    OUT.mkdir(parents=True, exist_ok=True)
    report = OUT / "REMOCAO-IMAGENS-RUINS-P3-2026-07-14.md"
    lines = [
        "# Remocao de imagens ruins/inadequadas P3",
        "",
        f"Modo: {'apply' if args.apply else 'dry-run'}",
        f"Notas avaliadas: {len(rows)}",
        f"Blocos de imagem removidos: {sum(r[2] for r in rows)}",
        "",
        "## Detalhe",
        "",
    ]
    for nid, decision, removed, txt in rows:
        lines.append(f"- `{nid}` `{decision}` removed={removed}: {txt}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("avaliadas:", len(rows))
    print("removidas:", sum(r[2] for r in rows))
    print("relatorio:", report)
    print("modo:", "apply" if args.apply else "dry-run")


if __name__ == "__main__":
    main()
