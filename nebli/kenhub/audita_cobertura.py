"""Auditoria somente-leitura da cobertura dos quizzes Kenhub da UC07."""
from __future__ import annotations

import json
from pathlib import Path

from nebli.kenhub import caminhos

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    linhas = ["# Auditoria de cobertura dos quizzes Kenhub — UC07", ""]
    falhas: list[str] = []
    totais = {"unidades": 0, "estruturas": 0, "texto": 0, "notas": 0}
    corridas = sorted((ROOT / "arquivos-trabalho").glob("uc07-kenhub-*/curadoria.json"))
    for arquivo in corridas:
        corrida = arquivo.parent
        cur = json.loads(arquivo.read_text())
        fonte = json.loads((caminhos.RAIZ / cur["modulo"] / cur["unidade"] / "itens.json").read_text())
        rec = json.loads((corrida / "receipt.json").read_text())
        estruturas = {x["slug"] for x in fonte["itens"]}
        cobertas = {s for n in rec["notas"] for s in n.get("cobre", []) if s}
        chaves = {x["chave"] for x in fonte.get("texto", [])}
        blocos = sum((cur.get(k, []) for k in ("texto", "anking", "acervo", "netter", "anking_io")), [])
        texto_coberto = {ch for b in blocos for ch in b.get("cobre_texto", [])}
        faltam_e, faltam_t = sorted(estruturas - cobertas), sorted(chaves - texto_coberto)
        erros = rec.get("falhas_pos", []) + rec.get("falhas_render", [])
        if faltam_e or faltam_t or erros:
            falhas.append(f"{cur['unidade']}: estruturas={faltam_e}; texto={faltam_t}; gates={erros}")
        totais["unidades"] += 1
        totais["estruturas"] += len(estruturas)
        totais["texto"] += len(chaves)
        totais["notas"] += len(rec["notas"])
        linhas.append(
            f"- `{cur['unidade']}`: {len(estruturas - set(faltam_e))}/{len(estruturas)} estruturas; "
            f"{len(chaves - set(faltam_t))}/{len(chaves)} trechos; {len(rec['notas'])} notas; gates "
            f"{'OK' if not erros else 'FALHARAM'}"
        )
    if len(corridas) != 51:
        falhas.append(f"esperadas 51 unidades; encontradas {len(corridas)}")
    cab = (
        f"Resultado: **{totais['unidades']}/51 unidades; {totais['estruturas']} estruturas; "
        f"{totais['texto']} trechos de estudo; {totais['notas']} notas**."
    )
    linhas[2:2] = [cab, "", f"Falhas: **{len(falhas)}**.", ""]
    saida = ROOT / "arquivos-trabalho" / "uc07-auditoria-cobertura-quizzes-2026-10-19.md"
    saida.write_text("\n".join(linhas) + "\n")
    print(cab)
    print(f"falhas: {len(falhas)}; relatório: {saida}")
    if falhas:
        print("\n".join(falhas))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
