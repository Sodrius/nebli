#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""card-mirror: monta o LOTE CEGO de uma rodada de treino (cards NEBLI de treino vs
cards AnKing reais do mesmo tema), para colar no agente discriminador `card-mirror`.
Uso: python card_mirror_blind.py <topico> [K=12] [termos_busca_separados_por_virgula]
Lê flashcards/treino/<topico>-treino.json; amostra K dos meus + K AnKing reais;
embaralha; remove qualquer marca; salva chave em arquivos-trabalho/treino-key-<topico>.json
e imprime o lote numerado (cole no card-mirror)."""
import json, urllib.request, sys, re, random, os
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOP = sys.argv[1] if len(sys.argv) > 1 else "glicogenio"
K = int(sys.argv[2]) if len(sys.argv) > 2 else 12
TERMS = (sys.argv[3].split(",") if len(sys.argv) > 3
         else ["glycogen synthase","glycogen phosphorylase","debranching","glucose-6-phosphatase",
               "glycogenin","von Gierke","McArdle","glycogen storage"])

def call(a, **p):
    req = urllib.request.Request("http://localhost:8765",
        json.dumps({"action": a, "version": 6, "params": p}).encode(), {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=40))["result"]
def clean(h):
    h = re.sub(r'<img[^>]+>', '', h); h = re.sub(r'<br\s*/?>', ' ', h); h = re.sub(r'<[^>]+>', '', h)
    h = h.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    return re.sub(r'\s+', ' ', h).strip()

train = json.load(open(os.path.join(ROOT, "flashcards", "treino", TOP + "-treino.json"), encoding="utf-8"))
mae = train.get("img_mae", "")
pool = []
mine = train["cards"][:]; random.Random(3).shuffle(mine)
for c in mine[:K]:
    ex = c["Extra"].replace("img", "").strip() or "(vazio)"
    pool.append({"o": "NEBLI", "f": c["Text"], "v": ex, "img": c.get("img", mae)})
seen, ank = set(), []
for q in TERMS:
    for nid in call("findNotes", query=q):
        if nid not in seen: seen.add(nid); ank.append(nid)
random.Random(5).shuffle(ank)
for n in call("notesInfo", notes=ank[:K * 2]):
    t = clean(n["fields"].get("Text", {}).get("value", "")); e = clean(n["fields"].get("Extra", {}).get("value", ""))
    img = None
    for fv in n["fields"].values():
        m = re.findall(r'<img src="([^"]+)"', fv["value"])
        if m: img = m[0]; break
    if t:
        pool.append({"o": "ANKING", "f": t, "v": e or "(vazio)", "img": img})
    if sum(1 for p in pool if p["o"] == "ANKING") >= K: break
random.Random(random.randint(1, 9999)).shuffle(pool)
key, lines = {}, []
for i, c in enumerate(pool, 1):
    key[i] = c["o"]
    im = ("[img %s]" % c["img"]) if c["img"] else "[sem img]"
    lines.append("#%d F: %s | V: %s | %s" % (i, c["f"], c["v"][:180], im))
os.makedirs(os.path.join(ROOT, "arquivos-trabalho"), exist_ok=True)
json.dump(key, open(os.path.join(ROOT, "arquivos-trabalho", "treino-key-%s.json" % TOP), "w"))
print("\n".join(lines))
print("\n(total %d; NEBLI=%d ANKING=%d) — chave em arquivos-trabalho/treino-key-%s.json" %
      (len(pool), sum(v == 'NEBLI' for v in key.values()), sum(v == 'ANKING' for v in key.values()), TOP))
