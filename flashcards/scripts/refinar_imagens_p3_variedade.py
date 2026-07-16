#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Refina imagens P3 com diversidade e pertinencia card-especifica.

Este script complementa `substituir_imagens_p3_candidatas.py`.
Ele e deliberadamente conservador:

- troca apenas quando encontra imagem externa com match textual forte;
- evita repetir a mesma imagem em muitos cards do mesmo slug;
- nao apaga midia;
- se nao houver candidato bom, marca o card como candidato a IO/manual.

Uso:
  python flashcards/scripts/refinar_imagens_p3_variedade.py --dry-run
  python flashcards/scripts/refinar_imagens_p3_variedade.py --apply
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
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "flashcards" / "auditorias"

TARGET_QUERY = (
    "tag:NEBLI::* "
    "(tag:NEBLI::image_status::pending_review "
    "OR tag:NEBLI::image_status::context_needs_specific_review)"
)

IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
SRC_RE = re.compile(r'<img[^>]+src="([^"]+)"[^>]*>', re.I)
TAG_RE = re.compile(r"<[^>]+>")
CLOZE_RE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", re.S)

STOP = {
    "the", "and", "or", "of", "to", "in", "a", "an", "by", "with", "from",
    "is", "are", "as", "on", "for", "this", "that", "which", "what", "when",
    "where", "into", "via", "its", "has", "have", "image", "source", "deck",
    "cell", "cells", "tissue", "system", "main", "only", "called", "called",
    "called", "function", "region", "structure", "body", "inside", "outside",
}

STATIC_QUERIES = {
    "NEBLI::histo-09-vasos": [
        'tag:H::CirculatorySystem',
        'tag:H::* artery',
        'tag:H::* arteriole',
        'tag:H::* capillary',
        'tag:H::* vein',
        '"magnified image" artery',
        '"magnified image" vein',
    ],
    "NEBLI::histo-10-tecido-nervoso": [
        'tag:H::NervousSystem',
        'tag:H::* neuron',
        'tag:H::* astrocyte',
        'tag:H::* microglia',
        'tag:H::* ependymal',
        '"magnified image" neuron',
        '"magnified image" nerve',
    ],
    "NEBLI::histo-11-orgaos-linfaticos": [
        'tag:H::LymphoidOrgans',
        'tag:H::* thymus',
        'tag:H::* spleen',
        'tag:H::* lymph',
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
        'tag:Dope::Anatomy::Thorax lymph',
        'tag:Dope::Anatomy::Abdomen lymph',
        'tag:*Anatomy_Clinical_Correlates::* lymph',
        'tag:H::* lymph',
    ],
}


def call(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]


def clean(value):
    value = IMG_RE.sub(" [img] ", value or "")
    value = CLOZE_RE.sub(r"\1", value)
    value = TAG_RE.sub(" ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def cloze_targets(value):
    out = []
    for m in CLOZE_RE.finditer(value or ""):
        target = clean(m.group(1))
        target = re.sub(r"\([^)]*\)", " ", target)
        for chunk in re.split(r"[/,;→]| and | or |\+", target):
            chunk = re.sub(r"\s+", " ", chunk).strip()
            if 3 <= len(chunk) <= 45:
                out.append(chunk)
    return list(dict.fromkeys(out))


def note_text(note):
    return " ".join(clean(f.get("value", "")) for f in note.get("fields", {}).values())


def front_text(note):
    for name in ("Text", "Front", "Header"):
        if name in note.get("fields", {}):
            return note["fields"][name]["value"]
    return next(iter(note.get("fields", {}).values()), {"value": ""})["value"]


def keywords(text):
    words = re.findall(r"[A-Za-z][A-Za-z\-]{2,}", text.lower())
    out = []
    for w in words:
        w = w.strip("-")
        if w not in STOP and len(w) > 3:
            out.append(w)
    return list(dict.fromkeys(out))


def image_srcs(value):
    return SRC_RE.findall(value or "")


def first_image_html(note):
    for field in note.get("fields", {}).values():
        m = IMG_RE.search(field.get("value", ""))
        if m:
            return m.group(0)
    return None


def first_src_from_img(img):
    m = SRC_RE.search(img or "")
    return m.group(1) if m else ""


def current_srcs(note):
    out = []
    for field in note.get("fields", {}).values():
        out += image_srcs(field.get("value", ""))
    return out


def slug_of(note):
    for tag in note.get("tags", []):
        if tag in STATIC_QUERIES:
            return tag
    for tag in note.get("tags", []):
        if tag.startswith("NEBLI::") and ("histo-" in tag or "anato-" in tag or "embrio-" in tag):
            return tag
    return "sem_slug"


def source_credit(note):
    tags = " ".join(note.get("tags", []))
    model = note.get("modelName", "")
    if "BlueLink" in tags:
        return "Image from BlueLink Atlas, University of Michigan."
    if "Dope" in tags or model == "Anatomy":
        return "Image from imported Dope Anatomy deck."
    if "Histology" in model or "H::" in tags or "LLU" in model:
        return "Image from imported Histology/LLU deck."
    if "AnKing" in model or "#AK_" in tags:
        return "Image from imported AnKing card."
    return "Image from imported Anki reference deck."


def dynamic_queries(slug, terms):
    queries = list(STATIC_QUERIES.get(slug, []))
    selected = []
    for term in terms:
        t = re.sub(r"[^A-Za-z0-9 '\\-]", " ", term).strip()
        if not t or len(t) < 4:
            continue
        selected.append(t)
    for term in selected[:3]:
        qt = f'"{term}"' if " " in term else term
        if "histo-" in slug:
            queries.append(f"tag:H::* {qt}")
        elif "anato-" in slug:
            if "circ-linf" in slug:
                queries.append(f"tag:Dope::Anatomy::Thorax {qt}")
            elif "sistema-linfatico" in slug:
                queries.append(f"tag:Dope::Anatomy::Thorax {qt}")
                queries.append(f"tag:Dope::Anatomy::Abdomen {qt}")
            queries.append(f"tag:*Anatomy_Clinical_Correlates::* {qt}")
        elif "embrio-" in slug:
            queries.append(f'deck:"AnKing Step Deck" {qt}')
    return list(dict.fromkeys(queries))


query_cache = {}
note_cache = {}


def cached_find(query):
    if query not in query_cache:
        query_cache[query] = call("findNotes", query=query)
    return query_cache[query]


def cached_notes(ids):
    missing = [nid for nid in ids if nid not in note_cache]
    if missing:
        for note in call("notesInfo", notes=missing):
            note_cache[note["noteId"]] = note
    return [note_cache[nid] for nid in ids if nid in note_cache]


def fetch_candidates(slug, terms, per_query=18, max_notes=70):
    seen = set()
    ids = []
    for q in dynamic_queries(slug, terms):
        try:
            found = cached_find(q)
        except Exception:
            continue
        for nid in found[:per_query]:
            if nid not in seen:
                seen.add(nid)
                ids.append(nid)
            if len(ids) >= max_notes:
                break
        if len(ids) >= max_notes:
            break
    if not ids:
        return []
    out = []
    for note in cached_notes(ids):
        img = first_image_html(note)
        if not img:
            continue
        text = note_text(note)
        out.append({
            "note_id": note["noteId"],
            "model": note.get("modelName", ""),
            "tags": note.get("tags", []),
            "text": text,
            "keys": set(keywords(text)),
            "img": img,
            "src": first_src_from_img(img),
            "credit": source_credit(note),
        })
    return out


def score(target_keys, targets, cand):
    overlap = sorted(target_keys & cand["keys"])
    strong = [k for k in overlap if len(k) >= 5]
    s = len(strong)
    ctext = cand["text"].lower()
    exact = []
    for t in targets:
        tclean = clean(t).lower()
        if len(tclean) >= 4 and tclean in ctext:
            exact.append(t)
            s += 2
    return s, strong, exact


def replace_extra_image(extra, image_html, credit):
    cleaned = extra or ""
    srcs = image_srcs(cleaned)
    if srcs:
        last = srcs[-1]
        pos = cleaned.rfind(last)
        img_pos = cleaned.rfind("<img", 0, pos)
        br_pos = cleaned.rfind("<br><br>", 0, img_pos if img_pos != -1 else pos)
        cut = br_pos if br_pos != -1 else img_pos
        if cut != -1:
            cleaned = cleaned[:cut]
    block = f'<br><br>{image_html}<br><i style="font-size:10pt;">{credit}</i>'
    return cleaned.rstrip() + block


def should_refine(note, repeated_threshold):
    tags = set(note.get("tags", []))
    if "NEBLI::image_status::context_needs_specific_review" in tags:
        return True
    srcs = current_srcs(note)
    return bool(srcs and max(src_counts_by_slug[slug_of(note)].get(s, 0) for s in srcs) >= repeated_threshold)


src_counts_by_slug = defaultdict(Counter)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-score", type=int, default=3)
    ap.add_argument("--repeated-threshold", type=int, default=5)
    ap.add_argument("--slug", help="Processar apenas um slug/tag NEBLI especifico")
    ap.add_argument("--limit", type=int, default=0, help="Limite de notas alvo para debug")
    args = ap.parse_args()
    if not args.apply and not args.dry_run:
        args.dry_run = True

    query = TARGET_QUERY if not args.slug else f"{TARGET_QUERY} tag:{args.slug}"
    ids = call("findNotes", query=query)
    if args.limit:
        ids = ids[:args.limit]
    notes = call("notesInfo", notes=ids)
    for note in notes:
        slug = slug_of(note)
        for src in current_srcs(note):
            src_counts_by_slug[slug][src] += 1

    used_after = defaultdict(Counter)
    for slug, counter in src_counts_by_slug.items():
        used_after[slug].update(counter)

    rows = []
    changed = []
    io_marked = []
    for note in notes:
        slug = slug_of(note)
        if not should_refine(note, args.repeated_threshold):
            rows.append((note["noteId"], slug, "skip", 0, "", "imagem nao repetida/contextual"))
            continue

        front = front_text(note)
        targets = cloze_targets(front)
        text = note_text(note)
        target_keys = set(keywords(text + " " + " ".join(targets)))
        candidates = fetch_candidates(slug, targets)
        current = set(current_srcs(note))

        best = None
        best_tuple = (-999, 999, "")
        best_meta = (0, [], [])
        for cand in candidates:
            if not cand["src"] or cand["src"] in current:
                continue
            s, overlap, exact = score(target_keys, targets, cand)
            if s < args.min_score:
                continue
            repeat_penalty = used_after[slug][cand["src"]]
            rank = (s, -repeat_penalty, cand["src"])
            if rank > best_tuple:
                best = cand
                best_tuple = rank
                best_meta = (s, overlap, exact)

        if best:
            s, overlap, exact = best_meta
            rows.append((
                note["noteId"], slug, "replace", s,
                ",".join((exact + overlap)[:10]),
                f"{best['note_id']} {best['src']}",
            ))
            changed.append((note, best))
            used_after[slug][best["src"]] += 1
            if args.apply:
                extra = note.get("fields", {}).get("Extra", {}).get("value", "")
                new_extra = replace_extra_image(extra, best["img"], best["credit"])
                call("updateNoteFields", note={"id": note["noteId"], "fields": {"Extra": new_extra}})
                call(
                    "addTags",
                    notes=[note["noteId"]],
                    tags="NEBLI::image_status::pending_review NEBLI::image_variety_pass img::revisar",
                )
                call(
                    "removeTags",
                    notes=[note["noteId"]],
                    tags=(
                        "img::generica img::substituir "
                        "NEBLI::image_status::context_needs_specific_review "
                        "NEBLI::image_context_needs_specific_review"
                    ),
                )
            continue

        mark_io = ("histo-" in slug or "anato-" in slug)
        status = "io_candidate" if mark_io else "manual_or_optional"
        rows.append((note["noteId"], slug, status, 0, ",".join(targets[:5]), "sem imagem externa forte"))
        if mark_io:
            io_marked.append(note["noteId"])
            if args.apply:
                call(
                    "addTags",
                    notes=[note["noteId"]],
                    tags="NEBLI::io_candidate NEBLI::image_status::needs_io_or_manual img::revisar",
                )

    OUT.mkdir(parents=True, exist_ok=True)
    report = OUT / "REFINO-IMAGENS-P3-VARIEDADE-2026-07-14.md"
    counts = Counter(r[2] for r in rows)
    lines = [
        "# Refino de imagens P3: variedade e pertinencia",
        "",
        f"Modo: {'apply' if args.apply else 'dry-run'}",
        f"Notas avaliadas: {len(rows)}",
        f"Trocas aplicaveis: {len(changed)}",
        f"Marcadas como IO/manual: {len(io_marked)}",
        f"Min score: {args.min_score}",
        f"Repeated threshold: {args.repeated_threshold}",
        "",
        "## Resumo",
        "",
    ]
    for k, v in counts.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Detalhe", ""]
    for nid, slug, action, s, overlap, decision in rows:
        lines.append(f"- `{nid}` `{slug}` {action} score={s} match=`{overlap}` -> {decision}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("avaliadas:", len(rows))
    print("trocas:", len(changed))
    print("io/manual:", len(io_marked))
    print("relatorio:", report)
    print("modo:", "apply" if args.apply else "dry-run")


if __name__ == "__main__":
    main()
