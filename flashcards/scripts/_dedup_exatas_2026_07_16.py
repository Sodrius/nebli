#!/usr/bin/env python3
"""Dedup de cards EXATAMENTE duplicados (mesmo texto sem cloze + mesma imagem, mesmo slug).
Feedback 2026-07-16 (A9/A10 — redundancia). REVERSIVEL: suspende a copia e marca
NEBLI::dup-removido-2026-07-16 (nao deleta). Mantem a nota com historico de revisao
(mais reps); empate -> nota mais antiga."""
import json, urllib.request, sys, re, collections
sys.stdout.reconfigure(encoding="utf-8")

def call(a, **p):
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        "http://localhost:8765",
        data=json.dumps({"action": a, "version": 6, "params": p}).encode(),
        headers={"Content-Type": "application/json"})))
    if r.get("error"):
        raise RuntimeError("%s: %s" % (a, r["error"]))
    return r["result"]

# Reviewer inativo?
try:
    cur = call("guiCurrentCard")
    if cur:
        sys.exit("ABORTA: Reviewer ativo.")
except RuntimeError as e:
    if "not currently active" not in str(e) and "not available" not in str(e).lower():
        raise

info = call("notesInfo", notes=call("findNotes", query="tag:NEBLI::*"))

def frontf(f):
    for n in ("Text", "Front", "Pergunta", "Cloze"):
        if n in f:
            return n
    return list(f.keys())[0]

def norm(h):
    t = re.sub(r"\{\{c\d+::|\}\}", " ", h or "")
    t = re.sub(r"&nbsp;", " ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).strip().lower()

def images(f):
    s = " ".join(v["value"] for v in f.values())
    return frozenset(re.findall(r'<img[^>]*src="([^"]+)"', s))

# assinatura de duplicata exata
groups = collections.defaultdict(list)
for n in info:
    f = n["fields"]
    slug = tuple(sorted(t for t in n.get("tags", []) if t.startswith("NEBLI::") and t.count("::") == 1))
    sig = (slug, norm(f[frontf(f)]["value"]), images(f))
    groups[sig].append(n["noteId"])

dupgroups = {k: v for k, v in groups.items() if len(v) > 1}
print("Grupos de duplicata EXATA:", len(dupgroups))
total_extra = sum(len(v) - 1 for v in dupgroups.values())
print("Cópias redundantes (a suspender):", total_extra, "\n")

# reps por nota
all_note_ids = [nid for v in dupgroups.values() for nid in v]
reps = {}
if all_note_ids:
    cards = call("findCards", query=" OR ".join("nid:%d" % n for n in all_note_ids))
    for c in call("cardsInfo", cards=cards):
        reps[c["note"]] = reps.get(c["note"], 0) + c.get("reps", 0)

to_suspend = []
report = []
for (slug, text, imgs), nids in sorted(dupgroups.items(), key=lambda x: -len(x[1])):
    keep = sorted(nids, key=lambda n: (-reps.get(n, 0), n))[0]
    drop = [n for n in nids if n != keep]
    to_suspend += drop
    report.append((slug[0] if slug else "?", text[:60], keep, drop, [reps.get(n, 0) for n in nids]))

# aplica: suspende cards das copias + tag
if to_suspend:
    dropcards = call("findCards", query=" OR ".join("nid:%d" % n for n in to_suspend))
    call("suspend", cards=dropcards)
    call("addTags", notes=to_suspend, tags="NEBLI::dup-removido-2026-07-16")

print("Suspensas+marcadas:", len(to_suspend), "notas /", len(dropcards) if to_suspend else 0, "cards\n")
for slug, text, keep, drop, allreps in report[:40]:
    print("  [%s] '%s'" % (slug.replace("NEBLI::", ""), text))
    print("     mantém %d | remove %s (reps=%s)" % (keep, drop, allreps))

# pos: quantos cards ativos sobraram
info2 = call("notesInfo", notes=call("findNotes", query="tag:NEBLI::* -tag:NEBLI::dup-removido-2026-07-16"))
print("\nNotas NEBLI ativas após dedup:", len(info2))
