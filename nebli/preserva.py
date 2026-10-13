"""Depois de refazer plan.json pelo build, devolve às oclusões os campos gravados fora do spec (busca, rotulo, parcial).

    python3 -m nebli.preserva arquivos-trabalho/<corrida> [plano-antigo.json]

Sem plano antigo, usa o mais recente plan-antes-*.json da corrida. O build não conhece esses campos (vêm de nebli.io_busca
e nebli.io_refazer); sem isto o gate de oclusão reprova depois de qualquer rebuild.
"""
import json
import sys
from pathlib import Path

run = Path(sys.argv[1])
old = Path(sys.argv[2]) if len(sys.argv) > 2 else max(run.glob("plan-antes-*.json"), key=lambda p: p.stat().st_mtime)
prev = {e["key"]: e for e in json.loads(old.read_text())["entries"]}
plan = json.loads((run / "plan.json").read_text()); n = 0
for e in plan["entries"]:
    o = prev.get(e["key"])
    if o:
        for k in (("busca", "busca_decisao", "rotulo", "parcial") if e.get("kind") == "slideio" else ("duplicacao_ok",)):
            if o.get(k) and not e.get(k):
                e[k] = o[k]; n += 1
(run / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
print(f"{run.name}: {n} campos devolvidos de {old.name}")
