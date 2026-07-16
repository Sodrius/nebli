#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lint_neblicard.py -- gate barato contra cloze induzivel.

Entrada:
  1) JSON do build_card.py, com {"cards":[{"text": "...", "extra": "..."}]}
     ou schemas legados NEBLI, com {"cards":[{"texto/front/Text": "..."}]} ou {"gerados":[{"Text": "..."}]}.
  2) ou texto cru com uma frente por linha.

Saida:
  - PASS / MIRROR / REJECT por card.
  - Exit 1 se houver REJECT; exit 2 se houver apenas MIRROR; exit 0 se PASS.

O linter olha so a frente (Text). Extra explicativo nao e punido: o problema
que ele pega e reconhecimento na pergunta, nao explicacao no verso.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

STOP = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "cell", "cells",
    "disease", "for", "from", "has", "have", "in", "into", "is", "it", "its",
    "may", "of", "on", "or", "syndrome", "that", "the", "their", "this", "to",
    "via", "when", "which", "with",
}
DOMAIN_GENERIC = {
    "artery", "body", "bone", "canal", "duct", "factor", "fluid", "gland",
    "layer", "muscle", "nerve", "organ", "protein", "receptor", "tissue",
    "vein", "vessel",
}
CAUSAL = [
    "because", "due to", "leads to", "lead to", "results in", "resulting in",
    "causes", "via", "so that", "thereby", "in order to", "passively",
    "actively", "allowing", "mediated by", "driven by", "converted to",
]
NUM_PREFIX = {
    "one": ["mono", "uni"], "1": ["mono", "uni"],
    "two": ["bi", "di"], "2": ["bi", "di"],
    "three": ["tri"], "3": ["tri"],
    "four": ["tetra", "quad"], "4": ["tetra", "quad"],
    "five": ["penta"], "5": ["penta"],
}

CLOZE_RE = re.compile(r"\{\{c(\d+)::([^}:]+?)(?:::([^}]*))?\}\}")
TAG_RE = re.compile(r"<[^>]+>")
BOLD_RE = re.compile(r"(<b>|<strong>|\*\*)(.*?)(</b>|</strong>|\*\*)", re.I | re.S)


def strip_html(s):
    return html.unescape(TAG_RE.sub(" ", s or ""))


def content_words(s):
    s = strip_html(s).replace("-", " ")
    words = re.findall(r"[A-Za-z][A-Za-z0-9+\-]*|\d+", s)
    out = []
    for w in words:
        lw = w.lower().strip("-")
        if lw and lw not in STOP:
            out.append(lw)
    return out


def stem_word(w):
    w = w.lower()
    for suf in ("ization", "ation", "ingly", "edly", "ing", "ed", "ies", "es", "s"):
        if len(w) > len(suf) + 4 and w.endswith(suf):
            w = w[: -len(suf)]
            break
    return w[:7] if len(w) > 7 else w


def clozes(text):
    return [{"idx": m.group(1), "answer": m.group(2), "span": m.group(0)} for m in CLOZE_RE.finditer(text)]


def visible_stem(text):
    return CLOZE_RE.sub(" ", text)


def is_acronym(s):
    clean = re.sub(r"[^A-Za-z0-9]", "", strip_html(s))
    if len(clean) < 3 or len(clean) > 8:
        return False
    uppers = sum(1 for c in clean if c.isupper())
    return uppers >= 2 and uppers >= len(clean) / 2


def acronym_letters(s):
    clean = re.sub(r"[^A-Za-z]", "", strip_html(s))
    return "".join(c for c in clean if c.isupper()) or clean.upper()


def sigla_self_give(stem, answer):
    if not is_acronym(answer):
        return False
    letters = acronym_letters(answer)
    if len(letters) < 3:
        return False
    words = content_words(stem)
    for i in range(0, len(words) - len(letters) + 1):
        if "".join(w[0].upper() for w in words[i : i + len(letters)]) == letters:
            return True
    return False


def bold_spans_in_stem(text):
    stem = visible_stem(text)
    return [m.group(2) for m in BOLD_RE.finditer(stem)]


def numeric_parenthetical_give(stem, answer):
    ans = " ".join(content_words(answer))
    ans_stems = {stem_word(w) for w in content_words(answer)}
    for p in re.findall(r"\(([^)]*)\)", stem):
        p_words = content_words(p)
        p_stems = {stem_word(w) for w in p_words}
        if ans_stems & p_stems:
            return True
        for n, prefixes in NUM_PREFIX.items():
            if n in p_words and any(a.startswith(pref) for a in ans_stems for pref in prefixes):
                return True
        if ans in p.lower() and ans:
            return True
    return False


def causal_count(stem):
    low = strip_html(stem).lower()
    return sum(1 for marker in CAUSAL if marker in low)


def lint_text(text):
    text = text or ""
    cs = clozes(text)
    if not cs:
        return {"status": "REJECT", "score": 99, "flags": ["no_cloze"], "text": text}
    stem = visible_stem(text)
    stem_roots = {stem_word(w) for w in content_words(stem) if w not in DOMAIN_GENERIC}
    flags = []
    hard = []
    score = 0
    distinct_indexes = sorted({c["idx"] for c in cs})
    if distinct_indexes != ["1"]:
        hard.append("multiple_cloze_indexes:" + ",".join(distinct_indexes))
    if len(cs) > 3:
        flags.append(f"many_same_card_targets:{len(cs)}")
        score += 3
    ccount = causal_count(stem)
    visible_bold_spans = bold_spans_in_stem(text)
    for c in cs:
        ans_words = [w for w in content_words(c["answer"]) if w not in DOMAIN_GENERIC]
        ans_roots = {stem_word(w) for w in ans_words}
        overlap = {r for r in ans_roots & stem_roots if len(r) >= 4}
        if overlap:
            head = stem_word(ans_words[-1]) if ans_words else ""
            if head in overlap:
                hard.append(f"name_in_stem_head:{','.join(sorted(overlap))}")
            else:
                flags.append(f"name_in_stem:{','.join(sorted(overlap))}")
                score += 2
        cw = len(ans_words)
        if cw >= 7:
            flags.append(f"cloze_dump:{cw}_content_words")
            score += 3
        elif cw >= 4:
            flags.append(f"long_cloze:{cw}_content_words")
            score += 1
        if sigla_self_give(stem, c["answer"]):
            hard.append("acronym_expansion_visible")
        if numeric_parenthetical_give(stem, c["answer"]):
            hard.append("parenthetical_give")
        for b in visible_bold_spans:
            b_roots = {stem_word(w) for w in content_words(b)}
            if ans_roots & b_roots:
                hard.append("bold_matches_answer")
        if visible_bold_spans and cw >= 4:
            hard.append("bold_label_with_description_cloze")
        if ccount >= 2 and cw <= 3:
            flags.append(f"mechanism_in_stem:{ccount}_causal_markers")
            score += 3
        elif ccount == 1:
            flags.append("possible_mechanism_in_stem")
            score += 1
    if hard:
        return {"status": "REJECT", "score": 99, "flags": sorted(set(hard + flags)), "text": text}
    if score >= 5:
        return {"status": "REJECT", "score": score, "flags": sorted(set(flags)), "text": text}
    if score >= 3:
        return {"status": "MIRROR", "score": score, "flags": sorted(set(flags)), "text": text}
    return {"status": "PASS", "score": score, "flags": sorted(set(flags)), "text": text}


def card_text(c):
    return c.get("text") or c.get("texto") or c.get("front") or c.get("Text") or ""


def load_cards(path):
    raw = Path(path).read_text(encoding="utf-8-sig")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return [{"text": line.strip()} for line in raw.splitlines() if line.strip()]
    if isinstance(data, dict) and "cards" in data:
        return data["cards"]
    if isinstance(data, dict) and "gerados" in data:
        return data["gerados"]
    if isinstance(data, list):
        return data
    raise SystemExit("Formato nao reconhecido: use JSON com cards[] ou texto linha-a-linha.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true", help="saida JSON completa")
    args = ap.parse_args()
    results = [lint_text(card_text(c)) for c in load_cards(args.path)]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for i, r in enumerate(results, 1):
            flag_txt = "; ".join(r["flags"]) if r["flags"] else "-"
            print(f"{i:03d} {r['status']:6s} score={r['score']:2} flags={flag_txt}")
    statuses = {r["status"] for r in results}
    if "REJECT" in statuses:
        return 1
    if "MIRROR" in statuses:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())



