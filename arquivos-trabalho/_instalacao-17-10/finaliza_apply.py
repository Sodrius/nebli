"""Completa um apply que parou em pedir_reposicao (pedido pendente do add-on): readback, receipt, plan-aplicado e pedido na fila própria.
uso: finaliza_apply.py <corrida>"""
import json, sys, importlib.util
from pathlib import Path
from datetime import datetime, timezone
run = Path(sys.argv[1]).resolve()
sys.argv = [str(run / "apply.py")]
spec = importlib.util.spec_from_file_location("ap", run / "apply.py"); ap = importlib.util.module_from_spec(spec); spec.loader.exec_module(ap)
A, plan = ap.A, ap.plan
adds = {}
for l in open(run / "journal.jsonl"):
    d = json.loads(l)
    if d.get("op") == "addNote": adds[d["key"]] = d["nid"]
problems, results, recusados = [], [], []
for e in plan["entries"]:
    nid = adds[e["key"]]; n = A("notesInfo", notes=[nid])[0]
    if any(n["fields"][k]["value"] != v for k, v in e["fields"].items()): problems.append(f"campos {e['key']}")
    if set(n["tags"]) != set(e["tags"]): problems.append(f"tags {e['key']}")
    ci = A("cardsInfo", cards=n["cards"]); r = {"key": e["key"], "nid": nid, "cards": {}}
    for c in ci:
        exp = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
        if c["flags"] != exp: problems.append(f"flag {e['key']}")
        if ap.canonical(c["deckName"]) != ap.DECK: problems.append(f"deck {e['key']}")
        r["cards"][str(c["cardId"])] = {"ord": c["ord"], "flag": c["flags"]}
        recusados.append((ap.BASE + e["order"] * 10 + c["ord"], c["cardId"]))
    results.append(r)
flags = [c["flag"] for r in results for c in r["cards"].values()]
rec = {"run_id": plan["run_id"], "selection_hash": plan["selection_hash"], "deck": ap.DECK, "notes": results,
       "cards_tag_aula": len(A("findCards", query=f'"tag:{ap.LESSON_TAG}"')), "cards_new_lesson": len(flags), "expected": plan["totais"]["cards"],
       "green": flags.count(3), "blue": flags.count(4), "pink": flags.count(5), "compartilhados_tag": [int(k) for k in plan["compartilhados"]],
       "problems": problems, "at": datetime.now(timezone.utc).isoformat(), "finalizado_por": "finaliza_apply.py (pedido de reposição pendente)"}
ordem = sorted(recusados)
fila = Path.home() / "NEBLI/arquivos-trabalho/_instalacao-17-10/fila-reposicao" / f"{plan['short']}.json"
fila.write_text(json.dumps({"acao": "reposicionar", "deck": ap.DECK, "inicio": ordem[0][0], "cards": [c for _, c in ordem]}))
rec["reposicao_pedida"] = len(ordem)
(run / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
print(json.dumps({k: rec[k] for k in ("cards_new_lesson", "expected", "green", "blue", "pink", "cards_tag_aula", "problems")}, ensure_ascii=False))
if not problems and rec["cards_new_lesson"] == plan["totais"]["cards"]:
    (run / "plan-aplicado.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
