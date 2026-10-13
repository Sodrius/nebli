"""Refaz as oclusões de slide de uma corrida com o slide_io atual e atualiza as notas vivas no lugar (mesmo nid; estudo preservado).

    python3 -m nebli.io_refazer arquivos-trabalho/<corrida> [--seco]

F-20261003-CLAUDE-13: as oclusões feitas linha a linha cortavam o nome (o verso mostrava só um pedaço) e juntavam caixas
vizinhas numa máscara gigante. Este comando reconstrói as máscaras por rótulo inteiro, grava `rotulo` e `parcial` em cada
entrada do plan.json (o gate exige rótulo inteiro), envia as SVG novas ao Anki e troca só Image/Question/Answer/Original Mask.
Remarks, tags, bandeiras e agendamento não mudam. Monta folhas de prévia em <corrida>/visual/io-r2-folhaN.png para conferir
a olho antes de dar por pronto. `--seco` só reconstrói e monta as folhas.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import importlib
import json
import sys
from pathlib import Path

MASK_FIELDS = ("Image", "Question Mask", "Answer Mask", "Original Mask", "Remarks")


def _h(x):
    return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]


def nids(run):
    out = {}
    for name in ("receipt.json", "receipt-reconciliado.json"):
        path = run / name
        if path.exists():
            for n in json.loads(path.read_text(encoding="utf-8")).get("notes", []):
                if n.get("nid"):
                    out[n["key"]] = n["nid"]
    return out


def sheets(run, made, keys):
    import fitz
    for k0 in range(0, len(keys), 20):
        doc = fitz.open(); W, H = 360, 300; pg = doc.new_page(width=W * 5, height=H * 4)
        for j, k in enumerate(keys[k0:k0 + 20]):
            r = fitz.Rect((j % 5) * W, (j // 5) * H, (j % 5 + 1) * W, (j // 5 + 1) * H - 14)
            pg.insert_image(r, filename=str(run / "io" / f"{k}-preview.png"))
            flag = " PARCIAL" if made[k]["parcial"] else ""
            pg.insert_text(((j % 5) * W + 4, (j // 5 + 1) * H - 3), f"{k}: {made[k]['rotulo'][:46]}{flag}", fontsize=8, color=(0, 0, .7))
        pg.get_pixmap(dpi=100).save(run / "visual" / f"io-r2-folha{k0 // 20 + 1}.png")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corrida"); ap.add_argument("--seco", action="store_true")
    args = ap.parse_args(argv)
    run = Path(args.corrida).resolve()
    sys.path.insert(0, str(run)); sys.modules.pop("spec", None)
    spec = importlib.import_module("spec")
    from nebli import slide_io
    items = [c for c in spec.CARDS if c["kind"] == "slideio"]
    if not items:
        print("sem oclusões de slide"); return 0
    (run / "visual").mkdir(exist_ok=True)
    made = slide_io.build(run, "fontes/slides.pdf", f"nebli-uc08-{spec.SHORT}", items, out="io")
    keys = [c["key"] for c in items]
    sheets(run, made, keys)
    partial = [k for k in keys if made[k]["parcial"]]
    print(f"{len(made)} oclusões; parciais: {partial or 'nenhuma'}; folhas em visual/io-r2-folha*.png")
    if args.seco:
        return 0
    plan_path = run / "plan.json"; plan = json.loads(plan_path.read_text(encoding="utf-8"))
    entries = {e["key"]: e for e in plan["entries"]}
    live = nids(run)
    missing = [k for k in keys if k not in live or k not in entries]
    if missing:
        print("sem nota viva ou entrada no plano:", missing); return 1
    from nebli.decks import Anki, escrita
    A = Anki()
    with escrita(A, f"{spec.SHORT}: oclusões por rótulo inteiro (F-20261003-CLAUDE-13)"):
        for k in keys:
            for name, rel in made[k]["media"].items():
                A("storeMediaFile", filename=name, data=base64.b64encode((run / rel).read_bytes()).decode())
            new = {f: made[k]["fields"][f] for f in MASK_FIELDS}
            A("updateNoteFields", note={"id": live[k], "fields": new})
            e = entries[k]; e["fields"].update(new); e["fields_hash"] = _h(e["fields"])
            e["rotulo"], e["parcial"] = made[k]["rotulo"], made[k]["parcial"]
            plan["media"].update(made[k]["media"])
    got = {n["noteId"]: n["fields"]["Question Mask"]["value"] for n in A("notesInfo", notes=[live[k] for k in keys])}
    bad = [k for k in keys if slide_io.VERSAO not in got.get(live[k], "")]
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"atualizadas {len(keys) - len(bad)}/{len(keys)} notas; readback falhou: {bad or 'nenhuma'}")
    return 1 if bad or partial else 0


if __name__ == "__main__":
    sys.exit(main())
