#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Valida um lote de cards de etimologia contra o schema + regras de QA do plano.

Uso:
  python flashcards/scripts/validate_etymology.py
  python flashcards/scripts/validate_etymology.py --lote flashcards/etimologia/cards/lote-00.json

Exit 0 = sem erros (warnings nao bloqueiam). Exit 1 = ha erros.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ETIM = Path(__file__).resolve().parents[1] / "etimologia"
DEFAULT_LOTE = ETIM / "cards" / "lote-00.json"
DEFAULT_RETIDO = ETIM / "assessments" / "lote-00-retido.json"
MANIFEST = ETIM / "deck_structure.json"

UID_RE = re.compile(r"^etim-[a-z0-9-]+$")
CLOZE_RE = re.compile(r"\{\{c(\d+)::(.*?)(?:::.*?)?\}\}", re.DOTALL)
REQUIRED = ["uid", "deck", "kind", "text", "extra", "source_etymology", "source_medical", "status"]


def norm(s: str) -> str:
    """minusculas sem acento, para comparacao robusta PT-BR."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower()


def words(s: str) -> int:
    return len(re.findall(r"\S+", s))


def valid_decks(manifest: Path) -> set[str]:
    data = json.loads(manifest.read_text(encoding="utf-8"))
    root = data["root"]
    out = {root}
    for g in data["decks"]:
        parent = f'{root}::{g["name"]}'
        out.add(parent)
        for c in g.get("children", []):
            out.add(f"{parent}::{c}")
    return out


def main(lote_path: Path, retido_path: Path) -> int:
    lote = json.loads(lote_path.read_text(encoding="utf-8"))
    cards = lote["cards"]
    decks = valid_decks(MANIFEST)

    retido = json.loads(retido_path.read_text(encoding="utf-8"))
    leak_terms = [norm(t) for t in retido["leakage_terms_ptbr"]]

    errors: list[str] = []
    warns: list[str] = []
    seen_uid: set[str] = set()
    seen_text: dict[str, str] = {}
    seen_answer: dict[str, str] = {}

    for c in cards:
        uid = c.get("uid", "<sem-uid>")

        for k in REQUIRED:
            if k not in c or c[k] in (None, "", [], {}):
                errors.append(f"[{uid}] campo obrigatorio ausente/vazio: {k}")

        if not UID_RE.match(uid):
            errors.append(f"[{uid}] uid fora do padrao ^etim-[a-z0-9-]+$")
        if uid in seen_uid:
            errors.append(f"[{uid}] uid duplicado")
        seen_uid.add(uid)

        deck = c.get("deck", "")
        if deck not in decks:
            errors.append(f"[{uid}] deck inexistente no manifesto: {deck}")

        text = c.get("text", "")
        clozes = CLOZE_RE.findall(text)
        nums = [int(n) for n, _ in clozes]
        if nums.count(1) != 1:
            errors.append(f"[{uid}] deve ter exatamente um c1 (achou {nums.count(1)})")
        if any(n >= 2 for n in nums):
            errors.append(f"[{uid}] contem c2+ (proibido): c{[n for n in nums if n>=2]}")

        # resposta do cloze nao pode vazar no restante visivel do Text
        for n, ans in clozes:
            if n != "1":
                continue
            visible = CLOZE_RE.sub("____", text)
            if norm(ans) and norm(ans) in norm(visible):
                warns.append(f"[{uid}] possivel vazamento: resposta '{ans}' aparece no texto visivel")
            key_a = norm(ans)
            if key_a in seen_answer:
                warns.append(f"[{uid}] resposta c1 repetida de {seen_answer[key_a]}: '{ans}'")
            else:
                seen_answer[key_a] = uid

        wt = words(text)
        if wt < 6 or wt > 32:
            warns.append(f"[{uid}] Text com {wt} palavras (alvo ~10-24)")

        extra = c.get("extra", "")
        we = words(extra)
        if we > 90:
            errors.append(f"[{uid}] Extra com {we} palavras (teto 90)")
        elif we < 20:
            warns.append(f"[{uid}] Extra curto ({we} palavras; alvo 35-70)")

        for fld in ("source_etymology", "source_medical"):
            v = c.get(fld)
            if not isinstance(v, list) or len(v) < 1:
                errors.append(f"[{uid}] {fld} precisa de >=1 fonte")

        # high-risk exige limite explicito
        is_hr = "etim::high_risk" in c.get("tags", []) or c.get("kind") == "exception"
        has_limit = bool(c.get("inference_limit")) or ("limite" in norm(extra))
        if is_hr and not has_limit:
            errors.append(f"[{uid}] high-risk/excecao sem 'Limite'/inference_limit")

        # dedup por texto normalizado
        key_t = norm(CLOZE_RE.sub("__", text))
        if key_t in seen_text:
            errors.append(f"[{uid}] Text duplicado de {seen_text[key_t]}")
        else:
            seen_text[key_t] = uid

        # LEAKAGE: nenhum termo retido pode aparecer em Text/Extra
        hay = norm(text + " " + extra)
        for term, raw in zip(leak_terms, retido["leakage_terms_ptbr"]):
            if re.search(r"\b" + re.escape(term) + r"\b", hay):
                errors.append(f"[{uid}] VAZAMENTO de item retido: '{raw}'")

    print(f"lote: {lote_path.name} | cards: {len(cards)}")
    print(f"termos retidos monitorados: {len(leak_terms)}")
    print(f"erros: {len(errors)} | warnings: {len(warns)}\n")
    for w in warns:
        print("  WARN ", w)
    for e in errors:
        print("  ERRO ", e)

    if errors:
        print(f"\nFALHOU: {len(errors)} erro(s).")
        return 1
    print("\nOK: schema, cloze, fontes, high-risk e leakage passaram.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", type=Path, default=DEFAULT_LOTE)
    ap.add_argument("--retido", type=Path, default=DEFAULT_RETIDO)
    args = ap.parse_args()
    raise SystemExit(main(args.lote, args.retido))
