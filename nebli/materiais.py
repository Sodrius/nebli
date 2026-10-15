"""Materiais da UC para o gate duro de fontes (F-20261015-CLAUDE-05).

    python3 -m nebli.materiais <corrida>                                   # lista o que o gate `uc_materials` ainda cobra
    python3 -m nebli.materiais <corrida> --ler "<arquivo>=<texto extraído>:<linha_ini>-<linha_fim>=<seção>" ...
    python3 -m nebli.materiais <corrida> --descartar "<arquivo>=<motivo>" ...

`--ler` copia o trecho lido (linhas do .txt extraído, p. ex. de `arquivos-trabalho/materiais-uc03/`) para
`<corrida>/fontes/mat-<n>.txt` e registra em `fontes-decl.json › materiais_uc`; depois rodar `python3 -m nebli.corrida fontes <corrida>`.
Registrar só o que foi de fato lido: o comando não lê por você.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def pendentes(run: Path):
    from nebli import gates
    data = json.loads((run / "fontes.json").read_text())
    if (run / "fontes-decl.json").exists():
        data["materiais_uc"] = json.loads((run / "fontes-decl.json").read_text()).get("materiais_uc", {})
    return [label for label, ok in gates.uc_materials(run, data) if not ok]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corrida")
    ap.add_argument("--ler", nargs="*", default=[])
    ap.add_argument("--descartar", nargs="*", default=[])
    a = ap.parse_args(argv)
    run = Path(a.corrida)
    # Corridas anteriores a 10/10 não têm fontes-decl.json: grava direto no fontes.json.
    decl_p = run / "fontes-decl.json" if (run / "fontes-decl.json").exists() else run / "fontes.json"
    decl = json.loads(decl_p.read_text())
    mats = decl.setdefault("materiais_uc", {})
    for item in a.ler:
        nome, fonte, secao = item.split("=", 2)
        caminho, _, linhas = fonte.rpartition(":")
        ini, fim = (int(x) for x in linhas.split("-"))
        texto = Path(caminho).read_text().splitlines()[ini - 1:fim]
        n = len([k for k, v in mats.items() if isinstance(v, dict) and v.get("texto")]) + 1
        dest = run / "fontes" / f"mat-{n:02d}-{re.sub(r'[^a-z0-9]+', '-', nome.lower())[:40]}.txt"
        dest.parent.mkdir(exist_ok=True)
        dest.write_text("\n".join(texto))
        mats[nome] = {"texto": str(dest.relative_to(run)), "secao": secao, "linhas": f"{caminho}:{ini}-{fim}"}
    for item in a.descartar:
        nome, motivo = item.split("=", 1)
        mats[nome] = {"descartado": motivo}
    if a.ler or a.descartar:
        decl_p.write_text(json.dumps(decl, ensure_ascii=False, indent=1))
    from nebli import corrida
    if (a.ler or a.descartar) and decl_p.name == "fontes-decl.json":
        corrida.fontes(run)
    falta = pendentes(run)
    print("gate de materiais: ok" if not falta else "FALTA:\n- " + "\n- ".join(falta))
    return 1 if falta else 0


if __name__ == "__main__":
    raise SystemExit(main())
