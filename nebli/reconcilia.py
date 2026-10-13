"""Correções feitas no Anki vivo voltam para a corrida da aula, para que nenhum rebuild as desfaça (plano 08/10 §3).

    python3 -m nebli.reconcilia arquivos-trabalho/<corrida> [--motivo "leva01 comentário 08/10"] [--simular]

Lê o recibo (chave → nid), compara cada campo vivo com o plan.json e grava as diferenças em
`<corrida>/correcoes-vivas.json` ({chave: {campo: valor, "_motivo": ..., "_em": ...}}). `nebli.delta` aplica esse arquivo
sobre o plano antes de comparar e se recusa a escrever enquanto houver divergência não reconciliada. O Anki vivo é a
versão corrigida; mudar de novo a mesma nota exige nova correção registrada, não rebuild do spec antigo.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ARQ = "correcoes-vivas.json"
IGNORAR = {"NEBLI_Comentario"}


def _same(a, b):
    from nebli.delta import same
    return same(a, b)


def carregar(run: Path) -> dict:
    p = run / ARQ
    return json.loads(p.read_text()) if p.exists() else {}


def aplicar_correcoes(run: Path, plan: dict) -> int:
    corr, n = carregar(run), 0
    for e in plan["entries"]:
        for f, v in corr.get(e["key"], {}).items():
            if not f.startswith("_") and f in e.get("fields", {}):
                e["fields"][f] = v; n += 1
    return n


def conflitos(A, plan: dict, nid: dict, aplicado: dict | None = None) -> list[tuple[str, str]]:
    """Campo vivo que difere do último plano aplicado (edição feita no Anki e não reconciliada).
    Sem plano aplicado, compara com o plano dado (modo antigo: só use logo depois de reconciliar)."""
    ref = {e["key"]: e for e in (aplicado or plan)["entries"]}
    ids = [nid[e["key"]] for e in plan["entries"] if e["key"] in nid]
    live = {n["noteId"]: n for n in A("notesInfo", notes=ids) if n} if ids else {}
    out = []
    for e in plan["entries"]:
        n = live.get(nid.get(e["key"]))
        if not n or e["key"] not in ref:
            continue
        for f, v in ref[e["key"]]["fields"].items():
            if f in IGNORAR or f not in n["fields"]:
                continue
            if not _same(n["fields"][f]["value"], v):
                out.append((e["key"], f))
    return out


def main(argv=None):
    from nebli.decks import Anki
    ap = argparse.ArgumentParser()
    ap.add_argument("corrida"); ap.add_argument("--motivo", default="correção no Anki vivo"); ap.add_argument("--simular", action="store_true")
    a = ap.parse_args(argv)
    run = Path(a.corrida)
    plan = json.loads((run / "plan.json").read_text())
    aplicar_correcoes(run, plan)
    rec = json.loads((run / "receipt.json").read_text())
    nid = {n["key"]: int(n["nid"]) for n in rec["notes"]}
    A = Anki()
    ap_path = run / "plan-aplicado.json"
    conf = conflitos(A, plan, nid, json.loads(ap_path.read_text()) if ap_path.exists() else None)
    corr = carregar(run)
    live = {n["noteId"]: n for n in A("notesInfo", notes=sorted({nid[k] for k, _ in conf}))} if conf else {}
    em = datetime.now(timezone.utc).isoformat()
    for k, f in conf:
        d = corr.setdefault(k, {})
        d[f] = live[nid[k]]["fields"][f]["value"]
        d["_motivo"], d["_em"], d["_nid"] = a.motivo, em, nid[k]
    print(f"{run.name}: {len(conf)} campos vivos divergentes do plano" + ("" if a.simular else f" gravados em {ARQ}"))
    for k, f in conf[:30]:
        print("  ", k, f)
    if not a.simular and conf:
        (run / ARQ).write_text(json.dumps(corr, ensure_ascii=False, indent=1))
    if not a.simular:  # estado vivo reconciliado = referência para a próxima delta
        aplicar_correcoes(run, plan)
        (run / "plan-aplicado.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
