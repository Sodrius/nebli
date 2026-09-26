"""Busca de lacunas no AnKing e acervos externos (somente leitura)."""
import json, re, html, sys, urllib.request
def call(action, **p):
    r = urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps({"action":action,"version":6,"params":p}).encode()), timeout=120)
    d = json.load(r)
    if d.get("error"): raise RuntimeError(d["error"])
    return d["result"]
def clean(s):
    s = re.sub(r"<img[^>]*>", "[IMG]", s); s = re.sub(r"<br\s*/?>", " / ", s); s = re.sub(r"<[^>]+>", "", s)
    return " ".join(html.unescape(s).split())
SCOPE = '(deck:"Referências::Anking Step Deck" or "deck:Referências::Referências Externas*")'
queries = json.load(open(sys.argv[1], encoding="utf-8"))
out = {}
for label, q in queries.items():
    nids = call("findNotes", query=f"{SCOPE} ({q})")
    notes = call("notesInfo", notes=nids[:25]) if nids else []
    out[label] = []
    print(f"\n### {label}  [{len(nids)} notas] q={q}")
    for n in notes:
        f = n["fields"]
        main = next((f[k]["value"] for k in ("Text","Front","Header") if k in f and f[k]["value"].strip()), "")
        hy = next((t.split("::")[-1] for t in n["tags"] if "HighYield" in t or "LowYield" in t or "Low/High" in t), "")
        line = f"{n['noteId']} [{n['modelName'][:18]}] {hy[:12]} | {clean(main)[:220]}"
        out[label].append({"nid": n["noteId"], "text": clean(main), "model": n["modelName"], "tags": n["tags"]})
        print(line)
json.dump(out, open(sys.argv[1].replace(".json", "-resultado.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
