"""Tira cards de uma aula já instalada, de forma persistente (correções da análise do deck-prova, F-20261013-CLAUDE-03).

    python3 -m nebli.enxuga arquivos-trabalho/<corrida> <nid>:<motivo> [<nid>:<motivo> ...] [--simular]
    python3 -m nebli.enxuga arquivos-trabalho/<corrida> --devolver <nid> [<nid> ...]   # desfaz para notas próprias retiradas por engano

- Nota própria da aula (no receipt.json): `nebli.retira` (suspende, tira tags da aula, marca NEBLI::retirado::<motivo>; comentário preservado).
- Nota compartilhada de outra aula (sh-<nid>): só desassocia (tira tag da aula, compartilhado::<curto>, cor e ordem desta aula); a nota
  continua intacta na aula dona.
- Persistência: spec.py ganha `RETIRADOS_ANALISE` e um filtro de CARDS; inventario.py redireciona os itens que apontavam para essas
  chaves para "EXC: <motivo>" (item de prova continua exigindo card: o gate acusa). Backup em spec-antes-enxuga-<data>.py.
- Avisa quando a nota também está em outra aula (para tirar lá também, se for o caso).
Depois: `python3 build.py --delta` e `python3 -m nebli.delta <corrida>` (rodados aqui), Tab dos afetados e gates.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from nebli.decks import Anki, escrita

ROOT = Path(__file__).resolve().parent.parent


def devolver(run, nids):
    import glob
    plan = json.loads((run / "plan.json").read_text())
    L = plan["lesson_id"]
    old = json.loads(Path(sorted(glob.glob(str(run / "receipt-antes-enxuga-*.json")))[-1]).read_text())
    rec = json.loads((run / "receipt.json").read_text())
    A = Anki()
    for nid in nids:
        ent = next(x for x in old["notes"] if x["nid"] == nid)
        key = ent["key"]
        for f in ("spec.py", "inventario.py"):
            s = (run / f).read_text()
            s = re.sub(rf'\n\s*"{re.escape(key)}": "[^"]*",?', "", s)
            s = re.sub(rf'"{re.escape(key)}": "[^"]*", ?|, ?"{re.escape(key)}": "[^"]*"', "", s)
            (run / f).write_text(s)
        if nid not in {x["nid"] for x in rec["notes"]}:
            rec["notes"].append(ent)
        with escrita(A, f"devolve {key}", sync=False):
            t = [x for x in A("notesInfo", notes=[nid])[0]["tags"] if x.startswith("NEBLI::retirado")]
            if t:
                A("removeTags", notes=[nid], tags=" ".join(t))
            A("addTags", notes=[nid], tags=f"NEBLI::{L}")
        print("devolvido", key)
    (run / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    log = run / "retirados.json"
    if log.exists():
        log.write_text(json.dumps([x for x in json.loads(log.read_text()) if x.get("nid") not in nids], ensure_ascii=False, indent=1))
    subprocess.run([sys.executable, "build.py", "--delta"], cwd=run, capture_output=True)
    d = subprocess.run([sys.executable, "-m", "nebli.delta", str(run)], cwd=ROOT, capture_output=True, text=True)
    print("delta:", (d.stdout + d.stderr).strip().splitlines()[-1][:200])


def main(argv):
    if "--devolver" in argv:
        i = argv.index("--devolver")
        return devolver(Path(argv[0]).resolve(), [int(x) for x in argv[i + 1:]])
    simular = "--simular" in argv
    argv = [a for a in argv if a != "--simular"]
    run = Path(argv[0]).resolve()
    pairs = [(int(a.split(":", 1)[0]), re.sub(r"[^a-z0-9-]+", "-", a.split(":", 1)[1].lower()).strip("-")) for a in argv[1:]]
    plan = json.loads((run / "plan.json").read_text())
    L, short = plan["lesson_id"], plan["short"]
    rec = json.loads((run / "receipt.json").read_text())
    own = {x["nid"]: x["key"] for x in rec["notes"]}
    shared = {int(e["nid"]): e["key"] for e in plan["entries"] if e.get("kind") == "compartilhado"}
    shared.update({int(n): f"sh-{n}" for n in plan.get("compartilhados", {}) if int(n) not in shared})
    A = Anki()
    plano_own, plano_sh, nada = [], [], []
    for nid, motivo in pairs:
        if nid in own:
            plano_own.append((own[nid], nid, motivo))
        elif nid in shared:
            plano_sh.append((shared[nid], nid, motivo))
        else:
            nada.append(nid)
    for key, nid, motivo in plano_own:
        tags = A("notesInfo", notes=[nid])[0]["tags"]
        outras = sorted({t.split("::", 1)[1] for t in tags if re.match(r"NEBLI::20\d\d-uc", t) and L not in t})
        if outras:
            print(f"AVISO {nid} ({key}) também está em: {', '.join(outras)} — tirar lá também se for o caso")
    # item de prova/exercício cuja única cobertura sairia: o card fica (MEMORY §3)
    import importlib.util
    inv_path = run / "inventario.py"
    if inv_path.exists():
        spec_i = importlib.util.spec_from_file_location("inv_enx", inv_path)
        m = importlib.util.module_from_spec(spec_i); spec_i.loader.exec_module(m)
        tirar = {k for k, _, _ in plano_own + plano_sh}
        for titulo, items in getattr(m, "EXERCICIOS", []):
            for iid, texto, dest in items:
                ds = [dest] if isinstance(dest, str) else list(dest)
                if ds and not any(str(d).startswith("EXC") for d in ds) and set(ds) <= tirar:
                    fica = set(ds)
                    plano_own = [x for x in plano_own if x[0] not in fica]
                    plano_sh = [x for x in plano_sh if x[0] not in fica]
                    print(f"MANTIDO {sorted(fica)}: única cobertura do item de prova/exercício {iid} ({texto[:70]})")
    print(f"{len(plano_own)} próprias a retirar, {len(plano_sh)} compartilhadas a desassociar, {len(nada)} fora desta aula {nada}")
    if simular:
        return
    stamp = time.strftime("%Y-%m-%d")
    shutil.copy(run / "spec.py", run / f"spec-antes-enxuga-{stamp}.py")
    keys = {key: motivo for key, _, motivo in plano_own + plano_sh}
    with (run / "spec.py").open("a") as f:
        f.write(f"\n\n# Análise do deck-prova {stamp} (F-20261013-CLAUDE-03): cards tirados desta aula, com motivo.\n"
                f"RETIRADOS_ANALISE = {json.dumps(keys, ensure_ascii=False, indent=1)}\n"
                "CARDS = [c for c in CARDS if c['key'] not in RETIRADOS_ANALISE]\n")
    inv = run / "inventario.py"
    if inv.exists():
        with inv.open("a") as f:
            f.write(f"\n\n# Análise do deck-prova {stamp}: itens cujo card saiu desta aula passam a exclusão com o motivo.\n"
                    f"_RETIRADOS = {json.dumps(keys, ensure_ascii=False)}\n"
                    "def _remap(dest):\n"
                    "    ds = [dest] if isinstance(dest, str) else list(dest)\n"
                    "    if any(isinstance(d, str) and d.startswith('EXC') for d in ds): return dest\n"
                    "    keep = [d for d in ds if d not in _RETIRADOS]\n"
                    "    if keep: return keep[0] if isinstance(dest, str) else keep\n"
                    "    return 'EXC: ' + 'tirado na análise do deck-prova (' + _RETIRADOS[ds[0]] + '): além do nível de ciclo básico desta aula ou repetido em outra aula'\n"
                    "SLIDES = [(n, t, tit, [(i, x, _remap(d)) for i, x, d in items]) for n, t, tit, items in SLIDES]\n"
                    "CAPITULO = [(t, [(i, x, _remap(d)) for i, x, d in items]) for t, items in globals().get('CAPITULO', [])]\n"
                    "EXERCICIOS = [(t, [(i, x, _remap(d)) for i, x, d in items]) for t, items in globals().get('EXERCICIOS', [])]\n")
    if plano_own:
        shutil.copy(run / "receipt.json", run / f"receipt-antes-enxuga-{stamp}.json")
        subprocess.run([sys.executable, "-m", "nebli.retira", str(run), "--recibo", "receipt.json"]
                       + [f"{k}:{m}" for k, _, m in plano_own], cwd=ROOT, check=True)
    if plano_sh:
        with escrita(A, f"desassocia {short}", sync=False):
            for key, nid, motivo in plano_sh:
                tags = A("notesInfo", notes=[nid])[0]["tags"]
                rm = [t for t in tags if t == f"NEBLI::{L}" or t.startswith(f"NEBLI::cor::{L}::") or t == f"NEBLI::compartilhado::{short}"
                      or t.startswith(f"NEBLI::ordem::{short}-")]
                if rm:
                    A("removeTags", notes=[nid], tags=" ".join(rm))
        log = run / "retirados.json"
        old = json.loads(log.read_text()) if log.exists() else []
        log.write_text(json.dumps(old + [{"key": k, "nid": n, "motivo": m, "desassociado": True} for k, n, m in plano_sh], ensure_ascii=False, indent=1))
        print(len(plano_sh), "desassociadas")
    b = subprocess.run([sys.executable, "build.py", "--delta"], cwd=run, capture_output=True, text=True)
    print("build --delta:", (b.stdout + b.stderr).strip().splitlines()[-1][:200] if (b.stdout + b.stderr).strip() else b.returncode)
    d = subprocess.run([sys.executable, "-m", "nebli.delta", str(run)], cwd=ROOT, capture_output=True, text=True)
    print("delta:", "\n".join((d.stdout + d.stderr).strip().splitlines()[-4:]))


if __name__ == "__main__":
    main(sys.argv[1:])
