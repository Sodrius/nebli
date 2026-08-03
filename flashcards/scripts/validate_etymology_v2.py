#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Valida candidatos ou piloto v2 sem alterar o Anki."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

DEFAULT = Path(__file__).resolve().parents[1] / "etimologia" / "cards" / "cards_pilot_v2.json"


def words(s: str) -> int:
    return len(re.findall(r"\S+", re.sub(r"<[^>]+>", " ", s)))


def main(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    cards = data["cards"]
    policy = data.get("policy", data.get("limits", {}))
    is_pt2 = path.name == "cards_pilot_pt2.json"
    is_v3 = path.name == "cards_approved_v3.json"
    text_limit = int(policy.get("text_words", 25 if is_v3 else 18))
    extra_limit = int(policy.get("extra_words", policy.get("extra_words_max", 40 if is_v3 else 10)))
    answer_limit = int(policy.get("cloze_answer_words", 6))
    errors = []
    seen_text = {}
    seen_uid = set()
    stats = Counter()
    for c in cards:
        uid = c.get("uid", "<sem-uid>")
        if uid in seen_uid: errors.append(f"{uid}: UID duplicado")
        seen_uid.add(uid)
        clozes = re.findall(r"\{\{c(\d+)::(.*?)\}\}", c.get("text", ""))
        nums = [int(n) for n, _ in clozes]
        if not 1 <= len(clozes) <= 3: errors.append(f"{uid}: {len(clozes)} clozes")
        if nums and sorted(set(nums)) != list(range(1, max(nums) + 1)): errors.append(f"{uid}: numeração de cloze")
        if words(c["text"]) > text_limit: errors.append(f"{uid}: Text {words(c['text'])} palavras")
        if words(c.get("extra", "")) > extra_limit: errors.append(f"{uid}: Extra {words(c['extra'])} palavras")
        if any(words(answer) > answer_limit for _, answer in clozes): errors.append(f"{uid}: resposta cloze longa")
        if not c.get("extra", "").strip(): errors.append(f"{uid}: Extra vazio")
        if len(c.get("tags", [])) > (6 if is_v3 else (5 if is_pt2 else 4)): errors.append(f"{uid}: tags demais")
        if not c.get("source_etymology") or not c.get("source_medical"): errors.append(f"{uid}: fonte ausente")
        if is_pt2 or is_v3:
            if not c["text"].startswith("<b>Etimologia.</b> "): errors.append(f"{uid}: tema neutro ausente")
            if re.findall(r"<b>\{\{c(\d+)::(.*?)\}\}</b>", c["text"]) != clozes:
                errors.append(f"{uid}: cloze sem negrito integral")
            if any(n != "1" for n, _ in clozes): errors.append(f"{uid}: contraste fragmentado em c2/c3")
            if c["kind"] == "contrast" and len(clozes) < 2 and "×" in c.get("canonical_form", ""):
                errors.append(f"{uid}: contraste não conjunto")
            if c["kind"] == "transfer" and not ("+" in c["extra"] and "=" in c["extra"]):
                errors.append(f"{uid}: Extra não decompõe e interpreta")
            generic = ("referente a ", "preserva esse núcleo", "partes:", "evita trocar")
            if any(x in c["extra"].casefold() for x in generic): errors.append(f"{uid}: Extra genérico")
        key = re.sub(r"\{\{c\d+::.*?\}\}", "___", re.sub(r"<[^>]+>", "", c["text"]).lower())
        if key in seen_text: errors.append(f"{uid}: texto equivalente a {seen_text[key]}")
        seen_text[key] = uid
        stats[c["kind"]] += c.get("number_of_cards", 1)
    expected = sum(c.get("number_of_cards", 1) for c in cards)
    if path.name == "cards_pilot_v2.json" and expected != 120: errors.append(f"piloto tem {expected}, esperado 120")
    if is_pt2 and expected != 82: errors.append(f"piloto pt2 tem {expected}, esperado 82")
    print(f"arquivo: {path.name} | notas: {len(cards)} | cards: {expected}")
    print("distribuição:", dict(stats))
    print(f"erros: {len(errors)}")
    for e in errors: print("ERRO", e)
    return 1 if errors else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=Path, nargs="?", default=DEFAULT)
    raise SystemExit(main(ap.parse_args().path))
