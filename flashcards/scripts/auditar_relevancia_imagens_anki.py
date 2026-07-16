#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audita a pertinencia das imagens dos cards NEBLI no Anki.

Regra central: imagem de contexto por aula/tema nao conta como resolvida. A
imagem precisa treinar o conteudo do card especifico. Este script e
conservador: nao apaga midia nem remove HTML; marca tags de revisao e gera um
relatorio para substituicao/remocao.

Uso:
  python flashcards/scripts/auditar_relevancia_imagens_anki.py --dry-run
  python flashcards/scripts/auditar_relevancia_imagens_anki.py --apply
"""
import argparse
import html
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from anki import call

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "flashcards" / "auditorias"
QUERY = "(tag:NEBLI::neblicard-autoral OR tag:NEBLI::gerado OR tag:NEBLI::externo)"

T_CONTEXT = "NEBLI::image_status::context_needs_specific_review"
T_NEEDS_SPECIFIC = "NEBLI::image_status::needs_specific_review"
T_STATUS_OK = "NEBLI::image_status::ok"
T_STATUS_MISSING = "NEBLI::image_status::missing"
T_STATUS_UNNEEDED = "NEBLI::image_status::unneeded_present"
T_CONTEXT_OLD = "NEBLI::image_context_needs_specific_review"
T_HAS_IMAGE = "NEBLI::image_extra"
T_NEEDS_IMAGE = "NEBLI::needs_image"
T_GENERIC = "img::generica"
T_REVIEW = "img::revisar"
T_SUBSTITUTE = "img::substituir"
T_ABSENT = "img::ausente"
T_OK = "img::ok"

CONTROL_PREFIXES = (
    "NEBLI::visual_need::",
    "NEBLI::image_role::",
    "NEBLI::image_status::",
)

VISUAL_RECOMMENDED_PREFIXES = (
    "NEBLI::embrio-",
)

IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
CLOZE_RE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", re.S)
TAG_RE = re.compile(r"<[^>]+>")


def strip_html(value):
    value = CLOZE_RE.sub(r"\1", value or "")
    value = TAG_RE.sub(" ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def note_text(note):
    fields = note.get("fields", {})
    parts = []
    for name in ("Text", "Texto", "Header", "Image", "Extra", "Remarks"):
        if name in fields:
            parts.append(strip_html(fields[name].get("value", "")))
    return " ".join(p for p in parts if p)


def has_image(note):
    for field in note.get("fields", {}).values():
        if IMG_RE.search(field.get("value", "")):
            return True
    return False


def slug_tags(note):
    return [t for t in note.get("tags", []) if t.startswith(("NEBLI::histo-", "NEBLI::anato-", "NEBLI::embrio-", "NEBLI::bioq-", "NEBLI::biomol-", "NEBLI::imuno-"))]


def infer_visual_need(note):
    tags = note.get("tags", [])
    model = note.get("modelName", "")
    if "IO" in model or "Image Occlusion" in model:
        return "required", "recognition"
    # Disciplina não define necessidade visual. Required exige tarefa visual
    # explícita ou um note type de Image Occlusion.
    if "NEBLI::visual_gate::required" in tags or "NEBLI::io_candidate" in tags:
        return "required", "recognition"
    if any(t.startswith(VISUAL_RECOMMENDED_PREFIXES) for t in tags):
        return "recommended", "schema"
    text = note_text(note).lower()
    visual_terms = [
        "micrograph", "lâmina", "lamina", "identify in", "shown", "image",
        "plate", "section", "corte", "localize", "localise",
    ]
    if any(term in text for term in visual_terms):
        return "recommended", "recognition"
    return "optional", "context"


def classify(note):
    tags = set(note.get("tags", []))
    visual_need, role = infer_visual_need(note)
    img = has_image(note)
    context_marker = T_CONTEXT_OLD in tags or T_CONTEXT in tags
    explicitly_approved = "NEBLI::image_status::approved" in tags or T_STATUS_OK in tags

    status = "approved"
    specificity = "unknown"
    score = 2 if img else 0
    reasons = []
    add = set()
    remove = set()

    if explicitly_approved and img:
        status = "approved"
        specificity = "reviewed_card_specific"
        score = 2
        remove |= {T_REVIEW, T_SUBSTITUTE, T_NEEDS_SPECIFIC, T_CONTEXT, T_CONTEXT_OLD, T_NEEDS_IMAGE, T_ABSENT}
        reasons.append("aprovação visual explícita preservada")
    elif not img and visual_need in {"required", "recommended"}:
        status = "missing"
        specificity = "absent"
        score = 0
        add |= {T_NEEDS_IMAGE, T_ABSENT, T_STATUS_MISSING}
        remove |= {T_HAS_IMAGE, T_OK}
        reasons.append("sem imagem em campos visuais")
    elif not img:
        status = "not_needed"
        specificity = "text_sufficient"
        score = 0
        remove |= {T_NEEDS_IMAGE, T_ABSENT, T_REVIEW, T_SUBSTITUTE, T_NEEDS_SPECIFIC}
        reasons.append("texto suficiente; ausência de imagem não bloqueia")
    elif context_marker:
        status = "context_needs_specific_review"
        specificity = "context_only"
        score = 1
        add |= {T_CONTEXT, T_NEEDS_SPECIFIC, T_CONTEXT_OLD, T_REVIEW, T_SUBSTITUTE}
        remove |= {T_OK}
        reasons.append("imagem marcada como contexto por aula/tema; nao e especifica ao card")
    else:
        status = "pending_review"
        specificity = "needs_manual_specificity_review"
        score = 2
        add |= {T_REVIEW, T_NEEDS_SPECIFIC}
        reasons.append("imagem existe, mas ainda nao ha auditoria de pertinencia card-especifica")

    if visual_need == "required" and (not img or score < 2):
        add |= {T_NEEDS_SPECIFIC, T_SUBSTITUTE}
        reasons.append("visual_need=required exige imagem especifica ou IO aprovado")

    # Heuristica: uma mesma imagem de contexto em muitos cards quase sempre e
    # ampla demais para ser final; ja vem marcada pelo script de enriquecimento.
    if specificity == "context_only":
        add.add(T_GENERIC)
        reasons.append("substituir por imagem do conceito cobrado, nao do tema da aula")

    add |= {
        f"NEBLI::visual_need::{visual_need}",
        f"NEBLI::image_role::{role}",
        f"NEBLI::image_status::{status}",
    }
    for tag in tags:
        if tag.startswith(CONTROL_PREFIXES) and tag not in add:
            remove.add(tag)

    return {
        "note_id": note["noteId"],
        "model": note.get("modelName", ""),
        "tags": note.get("tags", []),
        "slugs": slug_tags(note),
        "text": note_text(note)[:260],
        "has_image": img,
        "visual_need": visual_need,
        "image_role": role,
        "image_status": status,
        "specificity": specificity,
        "image_score": score,
        "reasons": reasons,
        "add_tags": sorted(add),
        "remove_tags": sorted(remove),
    }


def write_report(rows):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "AUDITORIA-RELEVANCIA-IMAGENS-ANKI-2026-07-14.md"
    counts = Counter(r["image_status"] for r in rows)
    by_slug = defaultdict(Counter)
    for r in rows:
        key = r["slugs"][0] if r["slugs"] else "sem_slug"
        by_slug[key][r["image_status"]] += 1

    lines = [
        "# Auditoria de relevancia das imagens no Anki",
        "",
        "Regra aplicada: imagem de contexto por tema/aula nao conta como resolvida.",
        "A imagem precisa treinar o conteudo do card especifico.",
        "",
        "## Resumo",
        "",
    ]
    for k, v in counts.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Por slug", ""]
    for slug, counter in sorted(by_slug.items()):
        parts = ", ".join(f"{k}={v}" for k, v in counter.items())
        lines.append(f"- `{slug}`: {parts}")
    lines += ["", "## Cards para revisar/substituir", ""]
    for r in rows:
        if r["image_status"] == "approved":
            continue
        slug = ", ".join(r["slugs"]) or "sem_slug"
        lines += [
            f"### Note {r['note_id']} - {slug}",
            "",
            f"- modelo: `{r['model']}`",
            f"- visual_need: `{r['visual_need']}`",
            f"- image_role: `{r['image_role']}`",
            f"- image_status: `{r['image_status']}`",
            f"- specificity: `{r['specificity']}`",
            f"- image_score: `{r['image_score']}`",
            f"- motivos: {'; '.join(r['reasons'])}",
            f"- texto: {r['text']}",
            "",
        ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--query", default=QUERY)
    args = ap.parse_args()
    if not args.apply and not args.dry_run:
        args.dry_run = True

    ids = call("findNotes", query=args.query)
    notes = call("notesInfo", notes=ids)
    rows = [classify(note) for note in notes]
    report = write_report(rows)

    if args.apply:
        add_groups = defaultdict(list)
        remove_groups = defaultdict(list)
        for row in rows:
            nid = row["note_id"]
            for tag in row["add_tags"]:
                add_groups[tag].append(nid)
            for tag in row["remove_tags"]:
                remove_groups[tag].append(nid)
        for tag, note_ids in add_groups.items():
            call("addTags", notes=note_ids, tags=tag)
        for tag, note_ids in remove_groups.items():
            call("removeTags", notes=note_ids, tags=tag)

    print(f"notas auditadas: {len(rows)}")
    print("status:", dict(Counter(r["image_status"] for r in rows)))
    print("relatorio:", report)
    print("modo:", "apply" if args.apply else "dry-run")


if __name__ == "__main__":
    main()
