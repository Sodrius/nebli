#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gate mecanico do manifesto visual de cards NEBLI.

O validador não julga medicina nem qualidade estética. Ele impede que um card
seja declarado visualmente resolvido sem intenção, fonte, crédito, licença e
evidência de preview. Use revisão humana para atribuir image_score e leakage.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


NEEDS = {"required", "recommended", "optional", "none"}
ROLES = {"recognition", "localization", "mechanism", "comparison", "schema", "context", "none"}
STATUSES = {"approved", "pending_review", "context_only", "needs_specific_review", "needs_credit", "missing", "rejected"}
LICENSES = {"open_ok", "noncommercial_ok", "private_only", "internal", "unknown_reject"}


def validate(row: dict, base: Path) -> list[str]:
    errors: list[str] = []
    nid = row.get("note_id", "sem_note_id")
    prefix = f"note {nid}: "
    need = row.get("visual_need")
    role = row.get("image_role")
    status = row.get("image_status")
    if need not in NEEDS:
        errors.append(prefix + "visual_need inválido/ausente")
    if role not in ROLES:
        errors.append(prefix + "image_role inválido/ausente")
    if status not in STATUSES:
        errors.append(prefix + "image_status inválido/ausente")
    if need != "none" and not str(row.get("visual_task", "")).strip():
        errors.append(prefix + "visual_task ausente")
    if role == "context" and need == "required":
        errors.append(prefix + "context nunca resolve visual_need=required")

    asset = row.get("asset") or {}
    if need == "none":
        if asset.get("file") and status == "approved":
            errors.append(prefix + "imagem decorativa aprovada apesar de visual_need=none")
        return errors

    if status == "approved":
        score = row.get("image_score")
        if not isinstance(score, (int, float)) or score < 2:
            errors.append(prefix + "approved exige image_score>=2")
        if row.get("answer_leakage") is not False:
            errors.append(prefix + "approved exige answer_leakage=false")
        for key in ("file", "source_type", "credit", "license_status", "retrieved_at", "hash"):
            if not asset.get(key):
                errors.append(prefix + f"asset.{key} ausente")
        if asset.get("license_status") not in LICENSES:
            errors.append(prefix + "asset.license_status inválido")
        if asset.get("source_type") in {"web", "atlas", "external_deck", "slide"} and not asset.get("source_locator"):
            errors.append(prefix + "asset.source_locator ausente")
        preview = row.get("preview_path")
        if not preview:
            errors.append(prefix + "preview_path ausente")
        elif not (base / preview).exists() and not Path(preview).exists():
            errors.append(prefix + f"preview inexistente: {preview}")

    if need == "required" and status != "approved":
        errors.append(prefix + "required ainda bloqueado: image_status != approved")

    if row.get("card_mode") == "image_occlusion":
        if role not in {"recognition", "localization", "comparison"}:
            errors.append(prefix + "IO exige role recognition/localization/comparison")
        if not isinstance(row.get("target_count"), int) or row.get("target_count", 0) < 1:
            errors.append(prefix + "IO exige target_count>=1")
        if row.get("all_duplicate_labels_masked") is not True:
            errors.append(prefix + "IO exige all_duplicate_labels_masked=true")
    elif row.get("card_mode") == "explanatory_image":
        if row.get("placement") != "extra":
            errors.append(prefix + "imagem explicativa deve ficar no Extra")
    elif row.get("card_mode") == "image_prompt":
        if role not in {"recognition", "localization", "comparison"}:
            errors.append(prefix + "image_prompt exige role visual")
        if row.get("placement") != "front":
            errors.append(prefix + "image_prompt deve ficar na frente")
    else:
        errors.append(prefix + "card_mode inválido/ausente")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    rows = data.get("cards", data) if isinstance(data, dict) else data
    if not isinstance(rows, list):
        raise SystemExit("Manifesto deve ser lista ou objeto com cards[].")
    errors = [err for row in rows for err in validate(row, args.manifest.parent)]
    result = {"cards": len(rows), "errors": errors, "passed": not errors}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"cards: {len(rows)}")
        print(f"errors: {len(errors)}")
        for err in errors:
            print("- " + err)
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
