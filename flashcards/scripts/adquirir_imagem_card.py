#!/usr/bin/env python3
"""Baixa e registra uma imagem específica para o Extra de um card.

Exige fonte, crédito e licença declarados; não aceita imagem apenas "do tema".
Uso: python adquirir_imagem_card.py --card-id X --url URL --source-type web \
 --credit "OpenStax, CC BY 4.0" --license-status open_ok --role mechanism \
 --task "mostrar a reação acrossômica" --out arquivos-trabalho/imagens-card
"""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import urllib.request
from datetime import date
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--card-id", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--source-type", required=True, choices=["anking", "external_deck", "atlas", "web", "slide", "local_figures"])
    ap.add_argument("--credit", required=True)
    ap.add_argument("--license-status", required=True, choices=["open_ok", "noncommercial_ok", "private_only", "internal"])
    ap.add_argument("--role", required=True, choices=["recognition", "localization", "mechanism", "comparison", "schema", "context"])
    ap.add_argument("--task", required=True)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    if len(args.task.strip()) < 12:
        raise SystemExit("visual_task precisa explicar a função da imagem neste card")
    req = urllib.request.Request(args.url, headers={"User-Agent": "NEBLI-card-image/1.0"})
    with urllib.request.urlopen(req, timeout=45) as response:
        content = response.read()
        mime = response.headers.get_content_type()
    ext = mimetypes.guess_extension(mime) or Path(args.url).suffix or ".img"
    digest = hashlib.sha256(content).hexdigest()
    args.out.mkdir(parents=True, exist_ok=True)
    asset = args.out / f"{digest}{ext}"
    asset.write_bytes(content)
    manifest = {
        "card_id": args.card_id, "file": str(asset), "url": args.url,
        "source_type": args.source_type, "credit": args.credit,
        "license_status": args.license_status, "retrieved_at": str(date.today()),
        "image_role": args.role, "visual_task": args.task, "hash": digest,
        "image_score": None, "status": "pending_editorial_review",
        "extra_html": f'<img src="{asset.name}"><div>{args.credit}</div>',
    }
    path = args.out / f"{args.card_id}-image.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
