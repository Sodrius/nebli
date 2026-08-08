#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEBLI -- curar_anking_local.py
Cura cards do AnKing v11 (clonado do GitHub langfield/anking-v11) filtrando
por keyword no Text + Extra e/ou por match de tag, gerando um JSON no
formato do NEBLIcard (compatível com empacotar_apkg.py).

Modo tablet/sem-PC (canon 2026-08-08): Davi sem PC, sem AnkiConnect, sem
AnkiHub. Este script usa o AnKing v11 como fonte offline — clonado em
/workspace/langfield/anking-v11 (~6.5 GB, 24k cards). Não é o v12
canônico (v12 tem erratas/updates), mas cobre >95% do mesmo material.

Uso:
    python3 flashcards/scripts/curar_anking_local.py <slug> --keywords "esôfago,estômago,duodeno,jejuno,íleo,papila,Treitz" [--limit 60] [--section "Zanki GI"] [--fields "Text,Extra"]

Saídas:
    flashcards/curadoria/<slug>-anking-v11.json  (formato NEBLIcard-compatível)
    figuras/<slug>_anking/*                       (imagens copiadas do _media)

O JSON emitido tem o formato aceito por empacotar_apkg.py:
{
  "meta": {
    "uc": "...", "prova": "...", "materia": "...", "aula_curta": "...",
    "slug": "<slug>-anking", "fonte": "anking-v11"
  },
  "cards": [{"id": "...", "type": "cloze", "front": "...", "extra": "...", "image": "...", "tags": [...]}, ...]
}

Notas de design:
- Cards do AnKing são Cloze deletion no formato Text + Extra. Preservamos essa forma.
- Rótulo temático NEBLI (<b>Anatomia.</b>) NÃO é adicionado, pois preserva
  identidade AnKing intocada (canon: AnKing intocado). Cards vão marcados
  com tag NEBLI::anking-v11-curado pra separar dos autorais.
- Imagens embutidas no HTML dos fields são resolvidas contra _media/ do
  AnKing e copiadas pra figuras/<slug>_anking/ (empacotar_apkg lê de lá).
"""

from __future__ import annotations
import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent.parent
ANKING_ROOT = Path("/workspace/langfield/anking-v11")
MEDIA_DIRS = [
    ANKING_ROOT / "_media",
    ANKING_ROOT / "Step 1" / "_media",
    ANKING_ROOT / "Step 1" / "Zanki Step Decks" / "_media",
    ANKING_ROOT / "Step 1" / "Zanki Step Decks" / "Zanki GI" / "_media",
    ANKING_ROOT / "Step 1" / "Zanki Step Decks" / "Zanki GI" / "GI Physiology + Embryo, Anatomy" / "_media",
    ANKING_ROOT / "Step 1" / "Zanki Step Decks" / "Zanki GI" / "GI Pathology" / "_media",
    ANKING_ROOT / "Step 1" / "Lolnotacop" / "_media",
    ANKING_ROOT / "Step 1" / "Zanki Pharmacology" / "_media",
]

FIELD_HEADERS = ["Text", "Extra", "Lecture Notes", "Missed Questions",
                 "Pathoma", "Boards and Beyond", "First Aid", "Sketchy",
                 "Pixorize", "Physeo", "OME", "Additional Resources",
                 "One by one"]


def parse_card(path: Path) -> Optional[dict]:
    """Lê 1 arquivo .md do AnKing e retorna dict com tags + fields."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return None

    lines = text.split("\n")
    meta = {}
    fields = {}

    # header (linha ## Note até primeira linha ### xxx)
    i = 0
    if lines and lines[0].strip() == "## Note":
        i = 1
    while i < len(lines) and not lines[i].startswith("### "):
        line = lines[i].strip()
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
        i += 1

    # fields (linhas ### xxx até proxima ### ou EOF)
    current_field = None
    current_lines = []
    while i < len(lines):
        line = lines[i]
        if line.startswith("### "):
            if current_field:
                fields[current_field] = "\n".join(current_lines).strip()
            current_field = line[4:].strip()
            current_lines = []
        else:
            current_lines.append(line)
        i += 1
    if current_field:
        fields[current_field] = "\n".join(current_lines).strip()

    return {"meta": meta, "fields": fields, "path": str(path.relative_to(ANKING_ROOT))}


def strip_html(s: str) -> str:
    """Remove tags HTML pra busca por keyword no texto puro."""
    return re.sub(r"<[^>]+>", " ", s)


def matches_keywords(card: dict, keywords: list, search_fields: list) -> tuple[bool, list]:
    """Verifica se card casa com pelo menos uma keyword nos fields buscados.

    Retorna (bool, lista de keywords que casaram)."""
    text_blob = ""
    for f in search_fields:
        text_blob += " " + strip_html(card["fields"].get(f, ""))
    text_blob_low = text_blob.lower()
    matched = [k for k in keywords if k.lower() in text_blob_low]
    return len(matched) > 0, matched


def find_media_file(name: str) -> Optional[Path]:
    """Procura arquivo de mídia (imagem) nos diretórios _media do AnKing."""
    for d in MEDIA_DIRS:
        p = d / name
        if p.exists():
            return p
    return None


def extract_images(html: str) -> list:
    """Extrai src das tags img no HTML."""
    return re.findall(r'<img\s+[^>]*src="([^"]+)"', html)


def guid_from_nid(nid: str) -> str:
    return hashlib.sha256(f"anking-v11-{nid}".encode()).hexdigest()[:16]


def curar(slug: str, keywords: list, limit: int, sections: list,
          search_fields: list, meta_uc: str, meta_prova: str, meta_materia: str,
          meta_aula: str):

    # Coleta candidatos
    candidatos = []
    for section in sections:
        section_path = ANKING_ROOT / section
        if not section_path.exists():
            print(f"! seção não existe: {section}", file=sys.stderr)
            continue
        for md in section_path.rglob("*.md"):
            card = parse_card(md)
            if not card:
                continue
            ok, matched = matches_keywords(card, keywords, search_fields)
            if ok:
                card["matched_keywords"] = matched
                candidatos.append(card)

    print(f"-> {len(candidatos)} candidatos encontrados em {len(sections)} seção(ões)")
    candidatos.sort(key=lambda c: (-len(c["matched_keywords"]), c["meta"].get("nid", "")))
    escolhidos = candidatos[:limit]
    print(f"-> {len(escolhidos)} escolhidos (limit={limit})")

    # Prepara pasta de mídia
    fig_dir = ROOT / f"figuras/{slug}_anking"
    fig_dir.mkdir(parents=True, exist_ok=True)

    cards_out = []
    imgs_copiadas = 0
    imgs_faltando = 0

    for c in escolhidos:
        nid = c["meta"].get("nid", "?")
        text = c["fields"].get("Text", "")
        extra = c["fields"].get("Extra", "")
        first_aid = c["fields"].get("First Aid", "")

        # Se Extra vazio, usar First Aid como Extra
        if not extra.strip() and first_aid.strip():
            extra = first_aid

        # Extrai imagens do Text primeiro; se nenhuma, tenta Extra/First Aid
        img_field = ""
        for source_field in [text, extra, first_aid]:
            imgs = extract_images(source_field)
            for img_src in imgs:
                # url decode básico
                img_name = re.sub(r"%20", " ", img_src)
                media = find_media_file(img_name)
                if media:
                    dst = fig_dir / media.name
                    if not dst.exists():
                        try:
                            shutil.copy2(media, dst)
                        except Exception:
                            pass
                    img_field = f'<img src="{media.name}">'
                    imgs_copiadas += 1
                    break
                else:
                    imgs_faltando += 1
            if img_field:
                break

        # Remove imgs do Text/Extra (empacotar_apkg embute Image separado)
        text_clean = re.sub(r'<img\s+[^>]*/?>', '', text).strip()
        extra_clean = re.sub(r'<img\s+[^>]*/?>', '', extra).strip()

        # Preserva tags AnKing + adiciona tag NEBLI de curadoria
        tags = c["meta"].get("tags", "").split(", ")
        tags = [t for t in tags if t.strip()]
        tags.append(f"NEBLI::{slug}")
        tags.append("NEBLI::anking-v11-curado")

        cards_out.append({
            "id": f"anking-v11-{nid}",
            "type": "cloze",
            "front": text_clean,
            "extra": extra_clean,
            "image": f"figuras/{slug}_anking/{media.name}" if img_field else "",
            "tags": tags,
            "_nid_original": nid,
            "_matched_keywords": c["matched_keywords"],
            "_path_original": c["path"],
        })

    saida = {
        "meta": {
            "uc": meta_uc,
            "prova": meta_prova,
            "materia": meta_materia,
            "aula_curta": meta_aula,
            "slug": f"{slug}-anking",
            "fonte": "anking-v11 (langfield/anking-v11 GitHub, clonado)",
            "keywords_usadas": keywords,
            "secoes_buscadas": sections,
            "total_candidatos": len(candidatos),
        },
        "cards": cards_out,
    }

    out_path = ROOT / f"flashcards/curadoria/{slug}-anking-v11.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"-> {len(cards_out)} cards → {out_path.relative_to(ROOT)}")
    print(f"-> imagens: {imgs_copiadas} copiadas, {imgs_faltando} faltando (buscar em outros _media/)")
    print(f"-> fig_dir: {fig_dir.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser(description="Cura cards do AnKing v11 local por keyword.")
    ap.add_argument("slug", help="slug da aula (usado no JSON e na pasta de mídia)")
    ap.add_argument("--keywords", required=True, help="palavras-chave separadas por vírgula (case-insensitive)")
    ap.add_argument("--limit", type=int, default=60, help="máximo de cards a incluir (default 60)")
    ap.add_argument("--sections", default="Step 1/Zanki Step Decks/Zanki GI",
                    help="subdiretórios do AnKing a buscar (separados por ';', relativo a /workspace/langfield/anking-v11)")
    ap.add_argument("--fields", default="Text,Extra,First Aid",
                    help="fields a buscar por keyword (separados por ','; default Text,Extra,First Aid)")
    ap.add_argument("--uc", default="UC-8")
    ap.add_argument("--prova", default="P1")
    ap.add_argument("--materia", default="Anatomia")
    ap.add_argument("--aula", default="")
    args = ap.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    sections = [s.strip() for s in args.sections.split(";") if s.strip()]
    fields = [f.strip() for f in args.fields.split(",") if f.strip()]
    aula = args.aula or args.slug

    curar(args.slug, keywords, args.limit, sections, fields,
          args.uc, args.prova, args.materia, aula)


if __name__ == "__main__":
    main()
