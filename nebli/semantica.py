"""Busca do AnKing e de TODOS os acervos externos por significado + palavra (fusão RRF) e leitura de seções de recurso (F-20261015-CLAUDE-06).

Rotas de busca obrigatórias antes de qualquer autoral (MEMORY §5, gate `cobertura_anking`):
  (a) palavra: termos e sinônimos (pontuação BM25 local sobre o mesmo texto do índice);
  (b) seção de recurso: tags #FirstAid/#Pathoma/#B&B/#Sketchy*/#NinjaNerd… do tema, lidas inteiras;
  (c) significado (inclui os cards NEBLI já instalados de outras aulas, acervo “NEBLI-vivo”): embeddings locais (fastembed, BAAI/bge-small-en-v1.5; nada sai do Mac).
(a) e (c) são fundidas por Reciprocal Rank Fusion, como no anki-semantic-search.

    /usr/bin/python3 -m nebli.semantica indexar                       # uma vez (e quando o AnKing atualizar)
    /usr/bin/python3 -m nebli.semantica buscar <corrida> "chave=frase em inglês" ["chave=..." ...] [--k 12]
    /usr/bin/python3 -m nebli.semantica secoes <corrida> "termo da tag" [...]   # lista seções e grava as notas de cada uma

Saídas na corrida (evidência lida pelo gate): busca/semantica.jsonl (uma linha por consulta) e busca/secoes/<tag>.txt +
busca/secoes.jsonl. O índice fica em .cache/indice-anking/ (fora do git).
"""
from __future__ import annotations

import html
import json
import math
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDX = ROOT / ".cache" / "indice-anking"
MODEL = "BAAI/bge-small-en-v1.5"  # base levava ~45 min para 45 mil notas no M5; small ~12 min
DECK = '"deck:Referências::Anking Step Deck*"'
# F-20261015-CLAUDE-06: "SEMPRE BUSCA EM TODOS ESSES DECKS DE REF EXTERNA - GATE HARD". Toda consulta roda em cada acervo.
ACERVOS = {
    "AnKing": DECK,
    "AnKing-MCAT": '"deck:Referências::Referências Externas::AnKing-MCAT*"',
    "Histology": '"deck:Referências::Referências Externas::Histology"',
    "LLU Histology": '"deck:Referências::Referências Externas::LLU Histology"',
    "BlueLink": '"deck:Referências::Referências Externas::University of Michigan - BlueLink Atlas*"',
    "AnatoKing": '"deck:Referências::Referências Externas::AnatoKing*"',
    "Dope Anatomy": '"deck:Referências::Referências Externas::Dope Anatomy*"',
    "Ankisthesia": '"deck:Referências::Referências Externas::Ankisthesia*"',
    "Dorian 100": '"deck:Referências::Referências Externas::100 Concepts (Dorian)*"',
    "Lab Values": '"deck:Referências::Referências Externas::USMLE Lab Values*"',
}
K_EXTERNO = 4  # melhores de cada acervo externo, além dos k do AnKing
RECURSOS = ("#FirstAid", "#Pathoma", "#B&B", "#SketchyMicro", "#SketchyPath", "#SketchyPharm", "#SketchyBiochem",
            "#SketchyPhysiology", "#NinjaNerd", "#DirtyMedicine", "#Costanzo", "#Bootcamp", "#Physeo", "#Pixorize", "#OME", "#AMBOSS")


def call(a, **p):
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        "http://127.0.0.1:8765", json.dumps({"action": a, "version": 6, "params": p}).encode()), timeout=300))
    if r["error"]:
        raise RuntimeError(r["error"])
    return r["result"]


def clean(s):
    s = re.sub(r"\{\{c\d+::(.*?)(::[^}]*)?\}\}", r"\1", s or "")
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def texto(fields):
    for k in ("Text", "Front", "Header"):
        if k in fields and fields[k]["value"].strip():
            frente = clean(fields[k]["value"])
            break
    else:
        frente = clean(next(iter(fields.values()))["value"])
    extra = clean(fields.get("Extra", {}).get("value", "") or fields.get("Back", {}).get("value", ""))[:300]
    return frente, extra


def tokens(s):
    return re.findall(r"[a-z0-9α-ω]+", s.lower())


def indexar():
    from fastembed import TextEmbedding
    import numpy as np
    IDX.mkdir(parents=True, exist_ok=True)
    meta = []
    for acervo, q in ACERVOS.items():
      nids = call("findNotes", query=q)
      for i in range(0, len(nids), 500):
        for n in call("notesInfo", notes=nids[i:i + 500]):
            frente, extra = texto(n["fields"])
            hy = next((t.split("::")[-1] for t in n["tags"] if "HighYield" in t), "")
            rec = sorted({t.split("::")[1] for t in n["tags"] if t.startswith("#AK_Step1_v12::#")})
            meta.append({"acervo": acervo, "nid": n["noteId"], "modelo": n["modelName"], "hy": hy, "frente": frente, "extra": extra, "recursos": rec})
    docs = [f"{m['frente']} {m['extra']}"[:600] for m in meta]
    (IDX / "meta.jsonl").write_text("\n".join(json.dumps(m, ensure_ascii=False) for m in meta) + "\n", encoding="utf-8")
    emb = TextEmbedding(MODEL)
    vec = []
    for i, v in enumerate(emb.embed(docs, batch_size=64)):
        vec.append(v)
        if i % 5000 == 0:
            print(f"{i}/{len(docs)}", flush=True)
    vec = np.array(vec, dtype="float32")
    vec /= np.linalg.norm(vec, axis=1, keepdims=True)
    np.save(IDX / "vetores.npy", vec)
    (IDX / "meta.jsonl").write_text("\n".join(json.dumps(m, ensure_ascii=False) for m in meta) + "\n", encoding="utf-8")
    (IDX / "info.json").write_text(json.dumps({"modelo": MODEL, "notas": len(meta), "acervos": dict(Counter(m["acervo"] for m in meta))}, ensure_ascii=False), encoding="utf-8")
    print(f"índice: {len(meta)} notas, modelo {MODEL}:", dict(Counter(m["acervo"] for m in meta)))


class Indice:
    def __init__(self):
        import numpy as np
        from fastembed import TextEmbedding
        self.np = np
        self.meta = [json.loads(l) for l in (IDX / "meta.jsonl").read_text(encoding="utf-8").splitlines() if l]
        self.vec = np.load(IDX / "vetores.npy")
        self.emb = TextEmbedding(MODEL)
        self.docs = [Counter(tokens(f"{m['frente']} {m['extra']}")) for m in self.meta]
        self.df = Counter(t for d in self.docs for t in d)
        self.avg = sum(sum(d.values()) for d in self.docs) / len(self.docs)
        self.acervos = sorted({m["acervo"] for m in self.meta}, key=lambda a: (a != "AnKing", a))
        self._vivo()

    def _vivo(self):
        """F-20261016-CLAUDE-03 (“os decks não se repitam nas informações”): os cards NEBLI já instalados de outras aulas entram na
        busca como acervo “NEBLI-vivo”; o que já existe é associado por sh() em vez de virar card novo. Embutidos na hora (~1 min)."""
        np = self.np
        excl = getattr(self, "excluir_tag", "")
        nids = call("findNotes", query='"tag:NEBLI::2026-*"' + (f' -"tag:{excl}"' if excl else ""))
        meta = []
        for i in range(0, len(nids), 500):
            for n in call("notesInfo", notes=nids[i:i + 500]):
                frente, extra = texto(n["fields"])
                aula = next((t for t in n["tags"] if re.fullmatch(r"NEBLI::2026-uc\d\d-[^:]+", t)), "")
                meta.append({"acervo": "NEBLI-vivo", "nid": n["noteId"], "modelo": n["modelName"], "hy": aula[7:], "frente": frente, "extra": extra, "recursos": []})
        if not meta:
            return
        vec = np.array(list(self.emb.embed([f"{m['frente']} {m['extra']}"[:600] for m in meta], batch_size=64)), dtype="float32")
        vec /= np.linalg.norm(vec, axis=1, keepdims=True)
        self.vec = np.vstack([self.vec, vec])
        self.meta += meta
        docs = [Counter(tokens(f"{m['frente']} {m['extra']}")) for m in meta]
        self.docs += docs
        for d in docs:
            self.df.update(d.keys())
        self.acervos.append("NEBLI-vivo")

    def bm25(self, q, n_top=100, k1=1.2, b=0.75):
        qt = set(tokens(q)); n = len(self.docs); out = []
        for i, d in enumerate(self.docs):
            s = 0.0; ln = sum(d.values())
            for t in qt:
                if t in d:
                    idf = math.log(1 + (n - self.df[t] + 0.5) / (self.df[t] + 0.5))
                    s += idf * d[t] * (k1 + 1) / (d[t] + k1 * (1 - b + b * ln / self.avg))
            if s:
                out.append((s, i))
        return [i for _, i in sorted(out, reverse=True)[:n_top]]

    def semantica(self, q, n_top=100):
        v = self.np.array(next(iter(self.emb.query_embed([q]))), dtype="float32")
        v /= self.np.linalg.norm(v)
        sims = self.vec @ v
        top = self.np.argsort(-sims)[:n_top]
        return [int(i) for i in top], sims

    def buscar(self, q, k=12):
        """k melhores do AnKing + K_EXTERNO de cada acervo externo (cada acervo é buscado em toda consulta)."""
        sem, sims = self.semantica(q, 3000)
        kw = self.bm25(q, 3000)
        out = []
        for acervo in self.acervos:
            s_ = [i for i in sem if self.meta[i]["acervo"] == acervo][:100]
            k_ = [i for i in kw if self.meta[i]["acervo"] == acervo][:100]
            score = Counter()
            for lista in (s_, k_):
                for r, i in enumerate(lista):
                    score[i] += 1 / (60 + r)
            top = [i for i, _ in score.most_common(k if acervo == "AnKing" else K_EXTERNO)]
            out += [dict(self.meta[i], sim=round(float(sims[i]), 3), rank_sem=(s_.index(i) + 1 if i in s_ else None),
                         rank_kw=(k_.index(i) + 1 if i in k_ else None)) for i in top]
        return out


def buscar(run: Path, pares, k=12):
    plan = run / "plan.json"
    lesson = json.loads(plan.read_text()).get("lesson_id", "") if plan.exists() else ""
    if not lesson and (run / "spec.py").exists():
        m = re.search(r'LESSON = "([^"]+)"', (run / "spec.py").read_text(encoding="utf-8"))
        lesson = m.group(1) if m else ""
    Indice.excluir_tag = f"NEBLI::{lesson}" if lesson else ""
    ix = Indice()
    (run / "busca").mkdir(exist_ok=True)
    with open(run / "busca" / "semantica.jsonl", "a", encoding="utf-8") as f:
        for par in pares:
            chave, q = par.split("=", 1)
            res = ix.buscar(q, k)
            f.write(json.dumps({"chave": chave, "consulta": q, "acervos": ix.acervos,
                                "top": [{x: r[x] for x in ("acervo", "nid", "sim", "rank_sem", "rank_kw", "hy", "frente")} for r in res]}, ensure_ascii=False) + "\n")
            print(f"### {chave} | {q}")
            for r in res:
                print(f"  {r['acervo'][:9]:9s} {r['nid']} {r['sim']:.2f} {r['hy'] or '-'} {r['frente'][:150]}")


def secoes(run: Path, termos):
    tags = [t for t in call("getTags") if t.startswith("#AK_Step1_v12::#") and t.split("::")[1] in RECURSOS]
    pasta = run / "busca" / "secoes"; pasta.mkdir(parents=True, exist_ok=True)
    with open(run / "busca" / "secoes.jsonl", "a", encoding="utf-8") as log:
        for termo in termos:
            alvo = [t for t in tags if termo.lower().replace(" ", "_") in t.lower() and not any(
                o != t and o.startswith(t + "::") for o in tags)]  # só folhas: a seção mais específica
            print(f"### {termo}: {len(alvo)} seções")
            for t in alvo:
                nids = call("findNotes", query=f'{DECK} "tag:{t}"')
                linhas = []
                for n in call("notesInfo", notes=nids):
                    frente, _ = texto(n["fields"])
                    hy = next((x.split("::")[-1] for x in n["tags"] if "HighYield" in x), "")
                    linhas.append(f"{n['noteId']} {hy or '-'} {frente[:200]}")
                nome = re.sub(r"[^A-Za-z0-9]+", "_", t.split("::", 1)[1])[:120]
                (pasta / f"{nome}.txt").write_text(f"# {t} ({len(nids)} notas)\n" + "\n".join(linhas) + "\n", encoding="utf-8")
                log.write(json.dumps({"termo": termo, "tag": t, "notas": len(nids), "arquivo": f"busca/secoes/{nome}.txt"}, ensure_ascii=False) + "\n")
                print(f"  {len(nids):3d}  {t.split('::', 1)[1]}")


def main(argv):
    if not argv or argv[0] not in ("indexar", "buscar", "secoes"):
        print(__doc__); return 2
    if argv[0] == "indexar":
        indexar(); return 0
    k = int(argv[argv.index("--k") + 1]) if "--k" in argv else 12
    args = [a for i, a in enumerate(argv[2:]) if a != "--k" and (i == 0 or argv[2:][i - 1] != "--k")]
    run = Path(argv[1])
    from nebli.etapa import exigir_planejamento
    exigir_planejamento(run, "a busca nos acervos")  # F-20261023-CLAUDE-02
    if argv[0] == "buscar":
        buscar(run, [a for a in args if "=" in a], k)
    else:
        secoes(run, args)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
