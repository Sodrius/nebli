#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica imagens OpenStax em cards de embriologia P3 quando ha pertinencia.

Nao tenta "cobrir" todos os cards. Usa figuras OpenStax apenas para alvos em
que a figura treina o processo especifico: clivagem/blastocisto, gastrulacao,
neurulacao e dobramento. O restante fica marcado para imagem especifica/IO.
"""
import base64
import html
import json
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ANKICONNECT = "http://localhost:8765"
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "flashcards" / "auditorias"

FIGURES = {
    "cleavage": {
        "file": "nebli_openstax_ap2e_28_5_preembryonic_development.webp",
        "url": "https://openstax.org/apps/image-cdn/v1/f%3Dwebp/apps/archive/20260604.144757/resources/bf32ce2bdd43df5dc92052915f816e9f912a3b65",
        "credit": "OpenStax Anatomy & Physiology 2e, Fig. 28.5 (CC BY-NC-SA).",
    },
    "gastrulation": {
        "file": "nebli_openstax_ap2e_28_9_germ_layers.webp",
        "url": "https://openstax.org/apps/image-cdn/v1/f%3Dwebp/apps/archive/20260604.144757/resources/9c163e061a5bd0ee52b56aed155ac3083230942a",
        "credit": "OpenStax Anatomy & Physiology 2e, Fig. 28.9 (CC BY-NC-SA).",
    },
    "neurulation": {
        "file": "nebli_openstax_ap2e_28_13_neurulation.webp",
        "url": "https://openstax.org/apps/image-cdn/v1/f%3Dwebp/apps/archive/20260604.144757/resources/10869e065f7133a1cb5821a6139c5f85cd46368d",
        "credit": "OpenStax Anatomy & Physiology 2e, Fig. 28.13 (CC BY-NC-SA).",
    },
    "folding": {
        "file": "nebli_openstax_ap2e_28_14_embryonic_folding.webp",
        "url": "https://openstax.org/apps/image-cdn/v1/f%3Dwebp/apps/archive/20260604.144757/resources/4a7fa2c5af63f94ace36aca2f7cb6bd84b42e2b4",
        "credit": "OpenStax Anatomy & Physiology 2e, Fig. 28.14 (CC BY-NC-SA).",
    },
}

IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
SRC_RE = re.compile(r'<img[^>]+src="([^"]+)"[^>]*>', re.I)
TAG_RE = re.compile(r"<[^>]+>")
CLOZE_RE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", re.S)


def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]


def clean(value):
    value = CLOZE_RE.sub(r"\1", value or "")
    value = TAG_RE.sub(" ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def note_text(note):
    return " ".join(clean(f.get("value", "")) for f in note.get("fields", {}).values()).lower()


def choose_figure(text):
    if any(k in text for k in ["clivagem", "cleavage", "mórula", "morula", "blastocisto", "blastocyst", "blastômero", "blastomere", "zigoto", "zygote", "zona pelúcida", "zona pellucida"]):
        return "cleavage"
    if any(k in text for k in ["gastrulação", "gastrulation", "linha primitiva", "primitive streak", "epiblasto", "epiblast", "endoderma", "ectoderma", "mesoderma", "germ layer", "folheto"]):
        return "gastrulation"
    if any(k in text for k in ["neurulação", "neurulation", "tubo neural", "neural tube", "crista neural", "neural crest", "neuroporo", "folic", "ácido fólico", "somito", "somite"]):
        return "neurulation"
    if any(k in text for k in ["dobramento", "folding", "céfalo", "cephalo", "caudal", "lateral", "intestino primitivo", "primitive gut", "bucofaríngea", "cloacal"]):
        return "folding"
    return None


def store_figures():
    for fig in FIGURES.values():
        raw = urllib.request.urlopen(fig["url"], timeout=60).read()
        call("storeMediaFile", filename=fig["file"], data=base64.b64encode(raw).decode("ascii"))


def replace_extra_image(extra, filename, credit):
    cleaned = extra or ""
    srcs = SRC_RE.findall(cleaned)
    if srcs:
        last = srcs[-1]
        pos = cleaned.rfind(last)
        img_pos = cleaned.rfind("<img", 0, pos)
        br_pos = cleaned.rfind("<br><br>", 0, img_pos if img_pos != -1 else pos)
        cut = br_pos if br_pos != -1 else img_pos
        if cut != -1:
            cleaned = cleaned[:cut]
    block = f'<br><br><img src="{filename}"><br><i style="font-size:10pt;">{credit}</i>'
    return cleaned.rstrip() + block


def main():
    apply = "--apply" in sys.argv
    dry = "--dry-run" in sys.argv or not apply
    store_figures()
    ids = call("findNotes", query=(
        "(tag:NEBLI::embrio-01-gametogenese-fertilizacao "
        "OR tag:NEBLI::embrio-02-03-gastrulacao-neurulacao) "
        "tag:NEBLI::image_status::context_needs_specific_review"
    ))
    notes = call("notesInfo", notes=ids)
    rows = []
    changed = []
    manual = []
    for note in notes:
        text = note_text(note)
        key = choose_figure(text)
        if not key:
            manual.append(note["noteId"])
            rows.append((note["noteId"], "manual", "sem figura OpenStax especifica"))
            if apply:
                call(
                    "addTags",
                    notes=[note["noteId"]],
                    tags="NEBLI::image_status::needs_specific_internet_or_io img::revisar",
                )
            continue
        fig = FIGURES[key]
        rows.append((note["noteId"], key, fig["file"]))
        changed.append(note["noteId"])
        if apply:
            extra = note.get("fields", {}).get("Extra", {}).get("value", "")
            new_extra = replace_extra_image(extra, fig["file"], fig["credit"])
            call("updateNoteFields", note={"id": note["noteId"], "fields": {"Extra": new_extra}})
            call(
                "addTags",
                notes=[note["noteId"]],
                tags="NEBLI::image_status::pending_review NEBLI::internet_image::openstax img::revisar",
            )
            call(
                "removeTags",
                notes=[note["noteId"]],
                tags="NEBLI::image_status::context_needs_specific_review img::generica img::substituir",
            )

    OUT.mkdir(parents=True, exist_ok=True)
    report = OUT / "OPENSTAX-EMBRIO-P3-2026-07-14.md"
    counts = Counter(r[1] for r in rows)
    lines = [
        "# Imagens OpenStax em embriologia P3",
        "",
        f"Modo: {'apply' if apply else 'dry-run'}",
        f"Notas avaliadas: {len(rows)}",
        f"Imagens aplicaveis: {len(changed)}",
        f"Marcadas para imagem especifica/IO: {len(manual)}",
        "",
        "## Resumo",
        "",
    ]
    for k, v in counts.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Detalhe", ""]
    for nid, action, detail in rows:
        lines.append(f"- `{nid}` -> `{action}`: {detail}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("avaliadas:", len(rows))
    print("imagens:", len(changed))
    print("manual/io:", len(manual))
    print("relatorio:", report)
    print("modo:", "apply" if apply else "dry-run")


if __name__ == "__main__":
    main()
