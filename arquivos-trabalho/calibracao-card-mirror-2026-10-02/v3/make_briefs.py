"""Monta os briefs do redator v3: alvo em português + 3 espelhos AnKing vivos (nunca o original nem o corpus de teste)."""
import glob, json, sys
sys.path.insert(0, "/Users/davisousa/NEBLI")
from nebli import card_mirror, espelhos
from nebli.decks import Anki

D1 = "arquivos-trabalho/calibracao-card-mirror-2026-10-01/"
V3 = "arquivos-trabalho/calibracao-card-mirror-2026-10-02/v3/"
which = sys.argv[1]  # dev | test
call = Anki()
corpus = {int(r["id"]) for f in glob.glob(D1 + "*.json") for r in json.load(open(f))
          if isinstance(r, dict) and str(r.get("id", "")).isdigit()}
briefs = []
for t in json.load(open(V3 + "targets.json")):
    if t["set"] != which:
        continue
    siblings = set(call("findNotes", query=f'nid:{t["id"]}'))
    found = espelhos.search(call, t["termos_busca"] + t["recuperar"], corpus | siblings | {int(t["id"])}, n=3)
    mirrors = [{"front": card_mirror.normalize_field(m["text"])[0], "extra": card_mirror.normalize_field(m["extra"])[0]}
               for m in found]
    briefs.append({"id": f"v3-{which}-{len(briefs) + 1:03d}", "family": t["family"], "alvo_pt": t["alvo_pt"],
                   "recuperar": t["recuperar"], "apoio_pt": t.get("apoio_pt", ""), "espelhos": mirrors,
                   "_source_id": t["id"], "_mirror_nids": [m["nid"] for m in found]})
private = {b["id"]: {"source_id": b.pop("_source_id"), "mirror_nids": b.pop("_mirror_nids")} for b in briefs}
json.dump(briefs, open(V3 + f"author-briefs-{which}.json", "w"), ensure_ascii=False, indent=1)
json.dump(private, open(V3 + f"private-brief-map-{which}.json", "w"), ensure_ascii=False, indent=1)
print(which, len(briefs), "briefs; espelhos por brief:", sorted({len(b["espelhos"]) for b in briefs}))
