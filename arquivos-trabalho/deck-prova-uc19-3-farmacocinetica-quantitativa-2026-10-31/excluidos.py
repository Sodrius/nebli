"""Decisão de cada nota das seções de recurso (SECOES_DA_AULA) que não entra no lote 3, com motivo da lista fechada do modo prova.
Nota já decidida nos lotes 1 ou 2 (no deck ou excluída por duplica do organizador de CYP) sai como lote-1/lote-2; as outras, em MANUAL.
Seções lidas inteiras em busca/secoes/*.txt em 31/10.

    /usr/bin/python3 excluidos.py     # grava excluidos.json (lido pelo spec)
"""
import json
import re
import runpy
from pathlib import Path

HERE = Path(__file__).parent
plan = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
NO_DECK = {str(e["src"]) for e in plan["entries"] if e.get("src")}
for k, v in plan.get("compartilhados", {}).items():
    NO_DECK |= {k, str(v.get("source_nid", ""))}


def lote(n):
    p = json.loads((HERE.parent / {1: "deck-prova-uc19-1-farmacodinamica-2026-10-30", 2: "deck-prova-uc19-2-farmacocinetica-2026-10-30"}[n] / "plan.json").read_text())
    s = {str(e.get("src")) for e in p["entries"]} | {str(v.get("source_nid")) for v in p["compartilhados"].values()}
    return s | {str(x["nid"]) for x in p.get("excluidos", []) if not str(x.get("motivo", "")).startswith("lote-")}


L1, L2 = lote(1), lote(2)
MANUAL = {
 "1490066326803": "lote-1: mnemônico do índice terapêutico estreito decidido no deck-prova 1",
}
SECOES = runpy.run_path(str(HERE / "spec.py"), run_name="x")["SECOES_DA_AULA"]
out, sem = [], []
for s in SECOES:
    for l in (HERE / "busca" / "secoes" / s).read_text(encoding="utf-8").splitlines()[1:]:
        m = re.match(r"(\d{13}) \S+ (.*)", l)
        if not m or m.group(1) in NO_DECK or any(m.group(1) == x[0] for x in out):
            continue
        n = m.group(1)
        mo = MANUAL.get(n) or ("lote-2: decidida no deck-prova 2 (Farmacocinética)" if n in L2 else "lote-1: decidida no deck-prova 1 (Farmacodinâmica)" if n in L1 else None)
        (out.append([n, mo]) if mo else sem.append(l[:150]))
(HERE / "excluidos.json").write_text(json.dumps([[int(n), mo] for n, mo in out], ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(out)} excluídas com motivo; sem regra: {len(sem)}")
for l in sem:
    print("  ", l)
