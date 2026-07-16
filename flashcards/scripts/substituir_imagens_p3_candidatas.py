#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Substitui imagens contextuais P3 por imagens candidatas mais especificas.

Conservador por design: so altera cards quando ha match textual razoavel entre
o card NEBLI e um card externo com imagem. Nao apaga midia. Cards sem match ficam
marcados para substituicao manual/IO.

Uso:
  python flashcards/scripts/substituir_imagens_p3_candidatas.py --dry-run
  python flashcards/scripts/substituir_imagens_p3_candidatas.py --apply
"""
import argparse
import html
import json
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


ANKICONNECT = "http://localhost:8765"


def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "flashcards" / "auditorias"
PROGRESS = OUT / "_troca_imagens_progress.log"


def log(msg):
    OUT.mkdir(parents=True, exist_ok=True)
    with PROGRESS.open("a", encoding="utf-8") as f:
        f.write(str(msg) + "\n")

TARGET_QUERY = "tag:NEBLI::image_status::context_needs_specific_review"

SOURCE_BY_SLUG = {
    "NEBLI::histo-09-vasos": [
        'tag:H::CirculatorySystem',
        '"magnified image" artery',
        '"magnified image" vein',
    ],
    "NEBLI::histo-10-tecido-nervoso": [
        'tag:H::NervousSystem',
        '"magnified image" neuron',
        '"magnified image" nerve',
    ],
    "NEBLI::histo-11-orgaos-linfaticos": [
        'tag:H::LymphoidOrgans',
        'tag:H::* thymus',
        '"magnified image" thymus',
        '"magnified image" spleen',
    ],
    "NEBLI::anato-05-circ-linf-I": [
        'tag:Dope::Anatomy::Thorax',
        'tag:BlueLink::Heart',
    ],
    "NEBLI::anato-06-circ-linf-II": [
        'tag:Dope::Anatomy::Thorax',
        'tag:BlueLink::SuperiorMediastinum+RootOfNeck',
        'tag:BlueLink::Heart',
    ],
    "NEBLI::anato-05-sistema-linfatico": [
        'tag:Dope::Anatomy::Abdomen lymph',
        'tag:*Anatomy_Clinical_Correlates::* lymph',
        'tag:H::* lymph',
    ],
    "NEBLI::embrio-01-gametogenese-fertilizacao": [
        'meiosis oocyte',
        'spermatogenesis fertilization',
        'zona pellucida acrosome',
    ],
    "NEBLI::embrio-02-03-gastrulacao-neurulacao": [
        'gastrulation neurulation',
        'notochord somite',
        'primitive streak',
    ],
}

STOP = {
    "the", "and", "or", "of", "to", "in", "a", "an", "by", "with", "from",
    "is", "are", "as", "on", "for", "this", "that", "which", "what", "when",
    "where", "into", "via", "it", "its", "be", "has", "have", "image", "img",
    "card", "extra", "source", "from", "imported", "deck", "aula", "slide",
}

IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
SRC_RE = re.compile(r'<img[^>]+src="([^"]+)"[^>]*>', re.I)
TAG_RE = re.compile(r"<[^>]+>")
CLOZE_RE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", re.S)


def clean(value):
    value = IMG_RE.sub(" [img] ", value or "")
    value = CLOZE_RE.sub(r"\1", value)
    value = TAG_RE.sub(" ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def note_plain(note):
    parts = []
    for field in note.get("fields", {}).values():
        txt = clean(field.get("value", ""))
        if txt:
            parts.append(txt)
    return " ".join(parts)


def keywords(text):
    words = re.findall(r"[A-Za-z][A-Za-z\-]{2,}", text.lower())
    out = []
    for w in words:
        w = w.strip("-")
        if w not in STOP and len(w) > 3:
            out.append(w)
    # Keep order but remove duplicates.
    return list(dict.fromkeys(out))


def first_image_html(note):
    for field in note.get("fields", {}).values():
        value = field.get("value", "")
        m = IMG_RE.search(value)
        if m:
            return m.group(0)
    return None


def slug_of(note):
    for tag in note.get("tags", []):
        if tag in SOURCE_BY_SLUG:
            return tag
    return None


def source_credit(note):
    tags = " ".join(note.get("tags", []))
    model = note.get("modelName", "")
    if "BlueLink" in tags:
        return "Image from BlueLink Atlas, University of Michigan."
    if "Dope" in tags or "Anatomy" in model:
        return "Image from imported Dope Anatomy deck."
    if "Histology" in model or "H::" in tags or "LLU" in model:
        return "Image from imported Histology/LLU deck."
    if "AnKing" in model or "#AK_" in tags:
        return "Image from imported AnKing card."
    return "Image from imported Anki reference deck."


def candidate_pool(slug):
    log(f"candidate_pool start {slug}")
    seen = set()
    note_ids = []
    out = []
    for q in SOURCE_BY_SLUG.get(slug, []):
        try:
            log(f"find source {slug}: {q}")
            ids = call("findNotes", query=q)
            log(f"source ids {len(ids)}")
        except Exception:
            continue
        for nid in ids[:15]:
            if nid not in seen:
                seen.add(nid)
                note_ids.append(nid)
    if not note_ids:
        return out
    log(f"source notesInfo {len(note_ids[:45])}")
    for note in call("notesInfo", notes=note_ids[:45]):
        nid = note["noteId"]
        img = first_image_html(note)
        if not img:
            continue
        text = note_plain(note)
        out.append({
            "note_id": nid,
            "model": note.get("modelName", ""),
            "tags": note.get("tags", []),
            "text": text,
            "keys": set(keywords(text)),
            "img": img,
            "credit": source_credit(note),
        })
    return out


def score(target_keys, cand):
    if not target_keys:
        return 0, []
    overlap = sorted(target_keys & cand["keys"])
    strong = [k for k in overlap if len(k) >= 5]
    return len(strong), strong


def replace_context_image(extra, image_html, credit):
    block = f'<br><br>{image_html}<br><i style="font-size:10pt;">{credit}</i>'
    cleaned = extra or ""
    markers = [
        "Image from imported Histology deck.",
        "Image from BlueLink Atlas, University of Michigan.",
        "Image from imported Dope Anatomy deck.",
        "Fonte visual: slide da aula.",
    ]
    for marker in markers:
        pos = cleaned.rfind(marker)
        if pos != -1:
            img_pos = cleaned.rfind("<img", 0, pos)
            br_pos = cleaned.rfind("<br><br>", 0, img_pos if img_pos != -1 else pos)
            cut = br_pos if br_pos != -1 else img_pos
            if cut != -1:
                cleaned = cleaned[:cut]
            break
    return cleaned.rstrip() + block


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-score", type=int, default=2)
    ap.add_argument("--slug", help="Processar apenas um slug/tag NEBLI especifico")
    args = ap.parse_args()
    if not args.apply and not args.dry_run:
        args.dry_run = True

    query = TARGET_QUERY if not args.slug else f"{TARGET_QUERY} tag:{args.slug}"
    PROGRESS.write_text("", encoding="utf-8")
    log(f"query alvo: {query}")
    ids = call("findNotes", query=query)
    log(f"ids alvo: {len(ids)}")
    notes = call("notesInfo", notes=ids)
    log(f"notes carregadas: {len(notes)}")
    pools = {}
    rows = []
    changed = []
    for note in notes:
        slug = slug_of(note)
        if not slug:
            rows.append((note["noteId"], "sem_slug", 0, "", "sem slug/fonte"))
            continue
        if slug not in pools:
            log(f"carregando pool: {slug}")
            pools[slug] = candidate_pool(slug)
        log(f"pool size {slug}: {len(pools[slug])}")
        target_text = note_plain(note)
        target_keys = set(keywords(target_text))
        best = None
        best_score, best_overlap = 0, []
        for cand in pools[slug]:
            s, ov = score(target_keys, cand)
            if s > best_score:
                best, best_score, best_overlap = cand, s, ov
        if not best or best_score < args.min_score:
            rows.append((note["noteId"], slug, best_score, ",".join(best_overlap), "sem candidato confiavel"))
            continue
        rows.append((note["noteId"], slug, best_score, ",".join(best_overlap[:12]), f"substituir por {best['note_id']}"))
        changed.append((note["noteId"], best))
        if args.apply:
            extra = note.get("fields", {}).get("Extra", {}).get("value", "")
            new_extra = replace_context_image(extra, best["img"], best["credit"])
            call("updateNoteFields", note={"id": note["noteId"], "fields": {"Extra": new_extra}})
            call("addTags", notes=[note["noteId"]], tags="NEBLI::image_status::pending_review img::revisar")
            call(
                "removeTags",
                notes=[note["noteId"]],
                tags=(
                    "img::generica img::substituir "
                    "NEBLI::image_status::context_needs_specific_review "
                    "NEBLI::image_status::needs_specific_review "
                    "NEBLI::image_context_needs_specific_review"
                ),
            )

    OUT.mkdir(parents=True, exist_ok=True)
    report = OUT / "TROCA-IMAGENS-P3-CANDIDATAS-2026-07-14.md"
    counts = Counter(r[4].split()[0] for r in rows)
    lines = [
        "# Troca de imagens P3 por candidatas especificas",
        "",
        f"Modo: {'apply' if args.apply else 'dry-run'}",
        f"Notas avaliadas: {len(rows)}",
        f"Notas com troca candidata: {len(changed)}",
        f"Min score: {args.min_score}",
        "",
        "## Resumo",
        "",
    ]
    for k, v in counts.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Detalhe", ""]
    for nid, slug, s, ov, decision in rows:
        lines.append(f"- `{nid}` `{slug}` score={s} overlap=`{ov}` -> {decision}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"avaliadas: {len(rows)}")
    print(f"trocas candidatas: {len(changed)}")
    print("relatorio:", report)
    print("modo:", "apply" if args.apply else "dry-run")


if __name__ == "__main__":
    main()
