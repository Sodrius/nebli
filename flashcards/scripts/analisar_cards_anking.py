#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analisar_cards_anking.py -- disseca N cards do AnKing pra destilar 'bom card'.

Amostra estratificada por RECURSO (FirstAid/Bootcamp/Sketchy/...) e por TIPO de
nota, computa features estruturais (nº cloze, imagem, tamanho da frente, Extra,
hint, mnemônico) e despeja: (1) stats agregadas sobre N, (2) amostra qualitativa
densa pra leitura. Base da pesquisa 'como uma IA faz bons cards'.

Uso: python flashcards/scripts/analisar_cards_anking.py --n 500 --qual 70
"""
import csv, re, sys, os, html, argparse, random, collections

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

EXPORT = os.path.join(os.path.dirname(__file__), "anking-v12-export.txt")
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
GUID, NOTETYPE, DECK, TEXT, EXTRA, TAGCOL = 0, 1, 2, 3, 4, 21

_IMG = re.compile(r"<img[^>]*>", re.I)
_CLOZE = re.compile(r"\{\{c(\d+)::(.*?)(?:::([^}]*))?\}\}", re.DOTALL)
_TAGHTML = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_RESRC = re.compile(r"#AK_Step1_v12::(#?[^:]+)")


def limpa(t):
    if not t:
        return ""
    t = _IMG.sub(" [img] ", t)
    t = _CLOZE.sub(lambda m: f"[{m.group(2)}]", t)
    t = t.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ").replace("<div>", " ")
    t = _TAGHTML.sub(" ", t)
    t = html.unescape(t)
    return _WS.sub(" ", t).strip()


def _rows():
    with open(EXPORT, encoding="utf-8", newline="") as f:
        for line in f:
            if line.startswith("#"):
                continue
            row = next(csv.reader([line], delimiter="\t", quotechar='"'))
            if len(row) > TAGCOL:
                yield row


def features(row):
    text_raw = row[TEXT] if len(row) > TEXT else ""
    extra_raw = row[EXTRA] if len(row) > EXTRA else ""
    tags = row[TAGCOL]
    m = _RESRC.search(tags)
    resource = m.group(1) if m else "(outro)"
    clozes = _CLOZE.findall(text_raw)
    cnums = {c[0] for c in clozes}
    front = limpa(text_raw)
    extra = limpa(extra_raw)
    has_hint = any(c[2] for c in clozes)
    mnem = bool(re.search(r"mnemonic|remember|\b[A-Z]{3,}\b", extra_raw + text_raw))
    return {
        "guid": row[GUID], "resource": resource, "notetype": row[NOTETYPE].split(" ")[0],
        "n_cloze_cards": len(cnums), "n_cloze_del": len(clozes),
        "has_img": bool(_IMG.search(text_raw) or _IMG.search(extra_raw)),
        "front_words": len(front.split()), "extra_words": len(extra.split()),
        "has_extra": len(extra.split()) >= 3, "has_hint": has_hint, "mnemonic": mnem,
        "front": front, "extra": extra,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=500)
    ap.add_argument("--qual", type=int, default=70)
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()
    random.seed(args.seed)

    # coleta so notas com tag Step1 (relevantes) e com Text
    todas = []
    for row in _rows():
        if "#AK_Step1_v12" in row[TAGCOL] and (len(row) > TEXT and row[TEXT].strip()):
            todas.append(row)
    random.shuffle(todas)

    # estratifica por recurso: round-robin
    por_rec = collections.defaultdict(list)
    for row in todas:
        f = features(row)
        por_rec[f["resource"]].append(f)
    ordem = sorted(por_rec, key=lambda r: -len(por_rec[r]))
    amostra = []
    i = 0
    while len(amostra) < args.n and any(por_rec[r] for r in ordem):
        r = ordem[i % len(ordem)]
        if por_rec[r]:
            amostra.append(por_rec[r].pop())
        i += 1
    amostra = amostra[:args.n]

    # ---- stats agregadas ----
    n = len(amostra)
    def pct(key): return round(100 * sum(1 for f in amostra if f[key]) / n, 1)
    rescount = collections.Counter(f["resource"] for f in amostra)
    ntype = collections.Counter(f["notetype"] for f in amostra)
    cloze_dist = collections.Counter(min(f["n_cloze_cards"], 5) for f in amostra)
    fw = sorted(f["front_words"] for f in amostra)
    ew = sorted(f["extra_words"] for f in amostra)
    def med(x): return x[len(x)//2] if x else 0

    L = [f"# Dissecação de {n} cards do AnKing v12 — features estruturais", "",
         f"Amostra estratificada por recurso (seed {args.seed}).", "",
         "## Distribuições",
         f"- **Recursos:** " + ", ".join(f"{r}={c}" for r, c in rescount.most_common(12)),
         f"- **Note types:** " + ", ".join(f"{t}={c}" for t, c in ntype.most_common()),
         f"- **Cards por nota (cloze):** " + ", ".join(f"{k}→{v}" for k, v in sorted(cloze_dist.items())) + "  (5 = 5+)",
         f"- **% com imagem:** {pct('has_img')}%",
         f"- **% com Extra (≥3 palavras):** {pct('has_extra')}%",
         f"- **% com hint no cloze:** {pct('has_hint')}%",
         f"- **% com marca de mnemônico/sigla:** {pct('mnemonic')}%",
         f"- **Palavras na frente:** min {fw[0]} · mediana {med(fw)} · p90 {fw[int(n*0.9)]} · max {fw[-1]}",
         f"- **Palavras no Extra:** mediana {med(ew)} · p90 {ew[int(n*0.9)]} · max {ew[-1]}",
         f"- **nº de cloze deletions por nota:** mediana {med(sorted(f['n_cloze_del'] for f in amostra))}",
         ""]
    with open(os.path.join(RAIZ, "arquivos-trabalho", "_anking-stats.md"), "w", encoding="utf-8") as fo:
        fo.write("\n".join(L) + "\n")

    # ---- amostra qualitativa densa (diversa por recurso e nº cloze) ----
    random.shuffle(amostra)
    qual = amostra[:args.qual]
    Q = [f"# Amostra qualitativa — {len(qual)} cards (frente + Extra)", ""]
    for k, f in enumerate(qual, 1):
        Q.append(f"[{k}] «{f['resource']}» cloze={f['n_cloze_cards']} img={'Y' if f['has_img'] else 'N'} "
                 f"front_w={f['front_words']} extra_w={f['extra_words']}")
        Q.append(f"  F: {f['front'][:400]}")
        if f["extra"]:
            Q.append(f"  X: {f['extra'][:320]}")
        Q.append("")
    with open(os.path.join(RAIZ, "arquivos-trabalho", "_anking-sample.txt"), "w", encoding="utf-8") as fo:
        fo.write("\n".join(Q) + "\n")

    print(f"analisados {n} cards | {len(rescount)} recursos | "
          f"stats -> _anking-stats.md | qualitativa ({len(qual)}) -> _anking-sample.txt")


if __name__ == "__main__":
    main()
