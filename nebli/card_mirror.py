"""Reproducible, text-only blind comparisons; never connects to Anki.

Only blind.json may be given to a judge. private-key.json contains the seed,
original records and a complete normalization audit. The seed is NOT a secret
key: protect the entire input and private file from the judge.

Symmetric normalization v2 (independent of origin): decode HTML entities;
replace block boundaries with newlines and lists with bullets; preserve text,
clozes, emphasis and sub/superscripts; drop HTML attributes/comments and
script/style content; replace image/audio assets with generic markers (retain
instructional image alt text, excluding exported filenames); remove only complete, explicitly labelled source/credit/
copyright/license lines; canonicalize whitespace. No length truncation.
All transformations have before/after values in the private audit, and original
records are preserved. Images themselves are not judged: visual cards need a
separate image evaluation. Normalization can lose visual meaning and does not
certify that a text-only item is suitable for evaluation.

grouped_split keeps connected components of shared group_id OR duplicate
normalized fronts together. This is conservative (ignores cloze numbering and
Extras), prevents sibling leakage when group_id is supplied, and does not detect
semantic paraphrases. Group IDs must identify the same note/concept globally.
It does not promise exact split sizes or stratification: inspect distributions.
"""

import argparse
import hashlib
from html.parser import HTMLParser
import json
import math
import os
from pathlib import Path
import random
import re


VERSION = 1
ORIGINS = ("AnKing", "Autoral")
NORMALIZATION = "symmetric-text-v2"
INTERPRETATION = (
    "Chance-level accuracy does not prove indistinguishability. Below-chance "
    "results may encode an inverted origin signature. Repeated tuning on the "
    "same items invalidates a held-out evaluation. Wilson intervals describe "
    "item accuracy under independence, not clustered sibling uncertainty or "
    "pedagogical quality. Single-origin groups have undefined AUC and balanced "
    "accuracy. A text-only test does not evaluate images."
)


def _canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False,
                      separators=(",", ":"))


def _digest(value):
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _id(value):
    if isinstance(value, bool) or not isinstance(value, (str, int)) or value == "":
        raise ValueError("id/group_id must be a nonempty string or integer")
    return str(value)


def validate_records(records):
    if not isinstance(records, list) or not records:
        raise ValueError("input must be a nonempty JSON list")
    seen = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("every record must be an object")
        if not {"id", "origin", "family", "text", "extra"} <= record.keys():
            raise ValueError("record requires id, origin, family, text, extra")
        rid = _id(record["id"])
        if rid in seen:
            raise ValueError("duplicate source id: " + rid)
        seen.add(rid)
        if record["origin"] not in ORIGINS:
            raise ValueError("origin must be AnKing or Autoral")
        for field in ("family", "text", "extra"):
            if not isinstance(record[field], str):
                raise ValueError(field + " must be a string")
        if not record["family"].strip() or not record["text"].strip():
            raise ValueError("family and text must be nonempty")
        if record.get("group_id") is not None:
            _id(record["group_id"])
    _canonical(records)  # reject non-JSON provenance, NaN and Infinity


class _RenderedText(HTMLParser):
    BLOCKS = {"div", "p", "br", "ul", "ol", "table", "tr", "section", "hr"}
    MARKS = {"b": "**", "strong": "**", "i": "_", "em": "_",
             "sub": "_{", "sup": "^{"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.hidden.append(tag)
        if self.hidden:
            return
        if tag in self.BLOCKS:
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag in {"td", "th"}:
            self.parts.append(" | ")
        elif tag in self.MARKS:
            self.parts.append(self.MARKS[tag])
        elif tag == "img":
            alt = dict(attrs).get("alt")
            # Exported filenames are provenance, not instructional alt text.
            if alt and (re.match(r"\s*File:", alt, re.I) or
                        re.search(r"\.(?:png|jpe?g|gif|webp|svg)\s*$", alt, re.I)):
                alt = None
            self.parts.append("[image]" + ((" " + alt) if alt else ""))
        elif tag in {"audio", "video", "source"}:
            self.parts.append("[media]")

    def handle_endtag(self, tag):
        if self.hidden:
            if tag == self.hidden[-1]:
                self.hidden.pop()
            return
        if tag in self.BLOCKS:
            self.parts.append("\n")
        elif tag in {"sub", "sup"}:
            self.parts.append("}")
        elif tag in self.MARKS:
            self.parts.append(self.MARKS[tag])

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def normalize_field(raw):
    """Return (normalized text, audit); no origin is accepted or consulted."""
    if not isinstance(raw, str):
        raise ValueError("field must be a string")
    audit = []

    def change(rule, before, after):
        if before != after:
            audit.append({"rule": rule, "before": before, "after": after})
        return after

    parser = _RenderedText()
    parser.feed(raw)
    parser.close()
    value = change("html-to-semantic-text-and-anonymous-media", raw,
                   "".join(parser.parts))
    value = change("anki-audio-path-to-marker", value,
                   re.sub(r"\[sound:[^\]]+\]", "[audio]", value, flags=re.I))
    # Strict whole-line labels, not arbitrary URLs or brand substrings in prose.
    label = re.compile(
        r"^\s*(?:[-*]\s*)?(?:\*\*|_)?"
        r"(?:sources?|credits?|(?:image|photo) credits?(?:\(s\))?|copyright|licen[cs]e|last updated)"
        r"(?:\*\*|_)?\s*:\s*.+$", re.I)
    licensing = re.compile(r"^\s*(?:[-*]\s*)?(?:©\s*.+|(?:image|photo) licensed (?:by|under) .+)$", re.I)
    lines = []
    for line in value.splitlines():
        # Nested HTML emphasis can produce ___Photo credit: ...___ after render.
        label_text = re.sub(r"[*_]", "", line)
        if (label.fullmatch(label_text) or licensing.fullmatch(label_text)) and "{{c" not in line.lower():
            audit.append({"rule": "explicit-provenance-line", "before": line,
                          "after": ""})
        else:
            # Some AnKing Extras append a credit to an image caption without a
            # <br>; preserve the caption and remove only the labelled suffix.
            inline_credit = re.search(r"(?<![A-Za-z])(?:photo|image) credits?(?:\(s\))?\s*:\s*", line, re.I)
            if inline_credit and "{{c" not in line[inline_credit.start():].lower():
                kept = line[:inline_credit.start()].rstrip(" *_")
                audit.append({"rule": "explicit-provenance-suffix", "before": line,
                              "after": kept})
                if kept:
                    lines.append(kept)
            else:
                lines.append(line)
    value = "\n".join(lines)
    normalized = "\n".join(re.sub(r"[^\S\n]+", " ", line).strip()
                           for line in value.splitlines())
    normalized = re.sub(r"\n{3,}", "\n\n", normalized).strip()
    return change("whitespace", value, normalized), audit


def duplicate_fingerprint(record):
    """Conservative front identity: ignore markup, cloze index, case/spacing."""
    text, _ = normalize_field(record["text"])
    text = re.sub(r"\{\{c\d+::", "{{c::", text, flags=re.I)
    text = re.sub(r"[*_]", "", text)
    return _digest(" ".join(text.casefold().split()))


def leakage_components(records):
    validate_records(records)
    parent = list(range(len(records)))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    seen = {}
    for i, record in enumerate(records):
        keys = [("front", duplicate_fingerprint(record))]
        if record.get("group_id") is not None:
            keys.append(("group", _id(record["group_id"])))
        for key in keys:
            if key in seen:
                parent[root(i)] = root(seen[key])
            else:
                seen[key] = i
    groups = {}
    for i, record in enumerate(records):
        groups.setdefault(root(i), []).append(record)
    return list(groups.values())


def grouped_split(records, seed, fractions=None):
    """Return split->records with transitive siblings/duplicates kept together.

    Sizes are approximate; group integrity takes precedence. Run once before
    exposing examples to writer/judge; save the resulting assignment privately.
    """
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    if fractions is None:
        fractions = {"train": .6, "development": .2, "holdout": .2}
    if (not fractions or any(not isinstance(k, str) or not k for k in fractions)
            or any(isinstance(v, bool) or not isinstance(v, (int, float))
                   or not math.isfinite(v) or v <= 0 for v in fractions.values())
            or not math.isclose(sum(fractions.values()), 1.0)):
        raise ValueError("split fractions must be positive, finite and sum to 1")
    components = leakage_components(records)
    # Canonical order makes assignments independent of input record order.
    components.sort(key=lambda group: sorted(_id(r["id"]) for r in group))
    random.Random(seed).shuffle(components)
    components.sort(key=len, reverse=True)
    result = {name: [] for name in fractions}
    for component in components:
        name = max(fractions, key=lambda k: len(records) * fractions[k] - len(result[k]))
        result[name].extend(sorted(component, key=lambda r: _id(r["id"])))
    return result


def build_batch(records, seed, mode="front_extra"):
    validate_records(records)
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    if mode not in {"front", "front_extra"}:
        raise ValueError("mode must be front or front_extra")
    rng = random.Random(seed)
    ordered = sorted(records, key=lambda r: _id(r["id"]))
    rng.shuffle(ordered)
    blind, private = [], []
    used = set()
    for record in ordered:
        rid = "%032x" % rng.getrandbits(128)
        while rid in used:
            rid = "%032x" % rng.getrandbits(128)
        used.add(rid)
        front, front_audit = normalize_field(record["text"])
        extra, extra_audit = normalize_field(record["extra"])
        if not front:
            raise ValueError("empty front after normalization: " + _id(record["id"]))
        if mode == "front" and extra:
            extra_audit.append({"rule": "front-mode-omit-extra", "before": extra,
                                "after": ""})
            extra = ""
        blind.append({"id": rid, "text": front, "extra": extra,
                      "family": record["family"]})
        private.append({"id": rid, "source_id": record["id"],
                        "origin": record["origin"], "family": record["family"],
                        "provenance": record,
                        "normalization": {"text": front_audit, "extra": extra_audit}})
    key = {"manifest": {"version": VERSION, "seed": seed, "mode": mode,
                        "normalization": NORMALIZATION, "input_sha256": _digest(records),
                        "blind_sha256": _digest(blind), "count": len(blind),
                        "limitations": INTERPRETATION}, "records": private}
    return blind, key


def _auc(rows):
    positives = sum(y for y, _ in rows)
    negatives = len(rows) - positives
    if not positives or not negatives:
        return None
    ordered = sorted(rows, key=lambda row: row[1])
    rank_sum, start = 0.0, 0
    while start < len(ordered):
        end = start + 1
        while end < len(ordered) and ordered[end][1] == ordered[start][1]:
            end += 1
        rank_sum += sum(y for y, _ in ordered[start:end]) * ((start + 1 + end) / 2)
        start = end
    return (rank_sum - positives * (positives + 1) / 2) / (positives * negatives)


def _metrics(rows):
    n = len(rows)
    tp = sum(y == 1 and p >= .5 for y, p in rows)
    tn = sum(y == 0 and p < .5 for y, p in rows)
    fp = sum(y == 0 and p >= .5 for y, p in rows)
    fn = sum(y == 1 and p < .5 for y, p in rows)
    accuracy = (tp + tn) / n
    positive_recall = tp / (tp + fn) if tp + fn else None
    negative_recall = tn / (tn + fp) if tn + fp else None
    balanced = ((positive_recall + negative_recall) / 2
                if positive_recall is not None and negative_recall is not None else None)
    z = 1.959963984540054
    denominator = 1 + z * z / n
    center = (accuracy + z * z / (2 * n)) / denominator
    radius = z * math.sqrt(accuracy * (1 - accuracy) / n + z * z / (4 * n * n)) / denominator
    eps = 1e-15
    clipped = [(y, min(1 - eps, max(eps, p))) for y, p in rows]
    auc = _auc(rows)
    return {"n": n, "accuracy": accuracy, "balanced_accuracy": balanced,
            "confusion": {"tp_autoral": tp, "tn_anking": tn,
                          "fp_autoral": fp, "fn_autoral": fn},
            "recall": {"Autoral": positive_recall, "AnKing": negative_recall},
            "auc": auc, "inverted_auc": 1 - auc if auc is not None else None,
            "inverted_balanced_accuracy": 1 - balanced if balanced is not None else None,
            "brier": sum((p - y) ** 2 for y, p in rows) / n,
            "log_loss": -sum(y * math.log(p) + (1 - y) * math.log1p(-p)
                             for y, p in clipped) / n,
            "log_loss_clip_epsilon": eps,
            "accuracy_wilson_95": [max(0., center - radius), min(1., center + radius)]}


def score_predictions(key, predictions):
    if not isinstance(key, dict) or not isinstance(key.get("records"), list) or not key["records"]:
        raise ValueError("key must contain nonempty records")
    expected = {}
    for record in key["records"]:
        if not isinstance(record, dict) or not {"id", "origin", "family"} <= record.keys():
            raise ValueError("invalid key record")
        rid = _id(record["id"])
        if rid in expected:
            raise ValueError("duplicate key id: " + rid)
        if record["origin"] not in ORIGINS or not isinstance(record["family"], str) or not record["family"]:
            raise ValueError("invalid key origin/family")
        expected[rid] = record
    if not isinstance(predictions, list):
        raise ValueError("predictions must be a JSON list")
    received = {}
    for prediction in predictions:
        if not isinstance(prediction, dict) or not {"id", "p_autoral", "tells"} <= prediction.keys():
            raise ValueError("prediction requires id, p_autoral, tells")
        rid = _id(prediction["id"])
        if rid in received:
            raise ValueError("duplicate prediction id: " + rid)
        p = prediction["p_autoral"]
        if isinstance(p, bool) or not isinstance(p, (int, float)) or not math.isfinite(p) or not 0 <= p <= 1:
            raise ValueError("p_autoral must be finite and in [0, 1]")
        if not isinstance(prediction["tells"], list) or not all(isinstance(t, str) for t in prediction["tells"]):
            raise ValueError("tells must be a list of strings")
        if "contamination" in prediction and not isinstance(prediction["contamination"], bool):
            raise ValueError("contamination must be a boolean")
        received[rid] = prediction
    if received.keys() != expected.keys():
        raise ValueError("coverage mismatch: missing=%s extra=%s" %
                         (sorted(expected.keys() - received.keys()), sorted(received.keys() - expected.keys())))
    rows, families, origins, items = [], {}, {}, []
    all_rows, all_families, all_origins = [], {}, {}
    contaminated = []
    for rid, record in expected.items():
        prediction = received[rid]
        row = (int(record["origin"] == "Autoral"), prediction["p_autoral"])
        all_rows.append(row)
        all_families.setdefault(record["family"], []).append(row)
        all_origins.setdefault(record["origin"], []).append(row)
        contamination = prediction.get("contamination", False)
        if contamination:
            contaminated.append(rid)
        else:
            rows.append(row)
            families.setdefault(record["family"], []).append(row)
            origins.setdefault(record["origin"], []).append(row)
        items.append({"id": rid, "origin": record["origin"], "family": record["family"],
                      "p_autoral": row[1], "correct": (row[1] >= .5) == bool(row[0]),
                      "tells": prediction["tells"], "contamination": contamination})
    return {"version": VERSION, "coverage": 1.0, "threshold": .5,
            "threshold_tie": "Autoral", "overall": _metrics(rows) if rows else None,
            "overall_all": _metrics(all_rows),
            "contamination": {"count": len(contaminated), "ids": contaminated,
                              "primary_n": len(rows), "total_n": len(all_rows),
                              "policy": "Self-reported contaminated items excluded from primary metrics; all-item metrics retained. Unreported familiarity cannot be detected."},
            "by_family": {k: _metrics(v) for k, v in sorted(families.items())},
            "by_origin": {k: _metrics(v) for k, v in sorted(origins.items())},
            "by_family_all": {k: _metrics(v) for k, v in sorted(all_families.items())},
            "by_origin_all": {k: _metrics(v) for k, v in sorted(all_origins.items())},
            "items": items, "interpretation": INTERPRETATION,
            "key_sha256": _digest(key), "predictions_sha256": _digest(predictions)}


def _read(path):
    def reject(value):
        raise ValueError("invalid JSON constant: " + value)
    def unique_pairs(pairs):
        result = {}
        for k, v in pairs:
            if k in result:
                raise ValueError("duplicate JSON key: " + k)
            result[k] = v
        return result
    return json.loads(Path(path).read_text(encoding="utf-8"),
                      parse_constant=reject, object_pairs_hook=unique_pairs)


def _write_new(path, value, private=False):
    payload = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600 if private else 0o644)
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        stream.write(payload)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("build")
    build.add_argument("--input", required=True)
    build.add_argument("--output", required=True, help="new run directory; must not exist")
    build.add_argument("--seed", required=True, type=int)
    build.add_argument("--mode", choices=("front", "front_extra"), default="front_extra")
    score = commands.add_parser("score")
    score.add_argument("--key", required=True)
    score.add_argument("--predictions", required=True)
    score.add_argument("--output", required=True, help="new private score JSON file")
    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            blind, key = build_batch(_read(args.input), args.seed, args.mode)
            output = Path(args.output)
            output.mkdir(mode=0o700, parents=True, exist_ok=False)
            _write_new(output / "private-key.json", key, private=True)
            _write_new(output / "blind.json", blind)
            print("Built %d items; give only blind.json to the judge." % len(blind))
        else:
            result = score_predictions(_read(args.key), _read(args.predictions))
            _write_new(Path(args.output), result, private=True)
            print(json.dumps(result["overall"], allow_nan=False))
    except (ValueError, OSError, TypeError) as exc:
        parser.exit(2, "card_mirror: %s\n" % exc)


if __name__ == "__main__":
    main()
