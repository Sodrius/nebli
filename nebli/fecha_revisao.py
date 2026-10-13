"""Grava em revisao-final.json["cards"] o veredito da revisão final card a card (F-20261003-CLAUDE-15).

    python3 -m nebli.fecha_revisao arquivos-trabalho/<corrida> --desde <ISO> [--notas notas-revisao.json]

Só depois de ler o despejo `python3 -m nebli.revisar` da aula inteira (frente, verso, figura, cor, comentário).
Chave com operação no journal desde --desde (troca de nota, campos, cor, tags) vira "corrigido" com a lista do que mudou;
o resto vira "ok". notas-revisao.json ({chave: texto}) acrescenta o que foi visto ou decidido em cada card.
"""
import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("corrida"); ap.add_argument("--desde", required=True); ap.add_argument("--notas")
    a = ap.parse_args(); run = Path(a.corrida)
    plan = json.loads((run / "plan.json").read_text())
    keys = [e["key"] for e in plan["entries"]] + [f"sh-{n}" for n in plan.get("compartilhados", {})]
    ops = {}
    for l in (json.loads(x) for x in (run / "journal.jsonl").read_text().splitlines() if x.strip()):
        if l.get("at", "") < a.desde: continue
        k = l.get("key")
        if k: ops.setdefault(k, set()).add({"addNote": "nota nova", "campos": "campos " + ",".join(l.get("campos", [])), "cor": "cor recalibrada",
                                            "tags": "tags", "ordem": "ordem"}.get(l["op"], l["op"]))
    extra = json.loads(Path(a.notas).read_text()) if a.notas else {}
    path = run / "revisao-final.json"; rf = json.loads(path.read_text()) if path.exists() else {}
    cards = {}
    for k in keys:
        what = sorted(ops.get(k, set()))
        note = "; ".join(filter(None, [", ".join(what), extra.get(k, "")]))
        cards[k] = {"veredito": "corrigido" if what else "ok", "nota": note or "lido no deck vivo: frente, verso, figura e cor conferem"}
    rf["cards"] = cards
    path.write_text(json.dumps(rf, ensure_ascii=False, indent=1))
    print(run.name, sum(v["veredito"] == "corrigido" for v in cards.values()), "corrigidos de", len(cards))


if __name__ == "__main__":
    main()
