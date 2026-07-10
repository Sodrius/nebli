"""
classificar_por_cronograma.py — Auditor (read-only) da relação entre as
questões do banco e o cronograma vigente da UC.

Semântica canonizada (Davi, 2026-05-22):
  - Campo `prova:` no frontmatter = prova HISTÓRICA de origem (a prova
    real de onde a questão veio, no ano de ingestão). Pode divergir do
    cronograma vigente — uma aula pode ter mudado de prova entre anos.
  - Campo `aula:` (slug) = critério VIGENTE. O gerador de cadernos
    consulta o slug + cronograma em runtime para decidir em qual
    caderno cada questão entra.

Este script NÃO modifica nenhum arquivo. Ele audita e classifica
o banco em quatro categorias úteis para o pipeline de geração:

  1. Pronta:  tem `aula:` com slug presente no cronograma vigente.
  2. Órfã:   tem `aula:` mas o slug não está no cronograma vigente
             (aula descontinuada, renomeada ou de outra UC).
  3. Sem aula: aula vazia, irá para caderno histórico-ampliado
             ou ficar fora dos cadernos.
  4. Divergente histórica: tem `aula:` no cronograma vigente E `prova:`
             declarada — informativo, sinaliza que a prova histórica
             difere da prova vigente do mesmo conteúdo.

Output: arquivos-trabalho/classificacao-cronograma-{UC}.md

Uso:
  python banco/classificar_por_cronograma.py --uc UC1
"""

from __future__ import annotations
import argparse
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
QUESTOES_DIR = ROOT / "questoes"
OUT_DIR = ROOT.parent / "arquivos-trabalho"

FRONT_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def load_cronograma(uc: str) -> dict[str, dict]:
    uc_num = uc.replace("UC", "").lstrip("0") or "1"
    yaml_path = ROOT / f"aulas_uc{int(uc_num):02d}.yml"
    if not yaml_path.exists():
        yaml_path = ROOT / f"aulas_uc{uc_num}.yml"
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    return {a["slug"]: a for a in data.get("aulas", [])}


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = FRONT_RE.match(text)
    if not m:
        return {}
    fm = {}
    for fm_match in re.finditer(r"^(\w+):\s*(.*)$", m.group(1), re.MULTILINE):
        k, v = fm_match.group(1), fm_match.group(2).strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
            v = v[1:-1]
        fm[k] = v
    return fm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--uc", default="UC1")
    args = ap.parse_args()

    cronograma = load_cronograma(args.uc)
    print(f"Cronograma {args.uc}: {len(cronograma)} aulas mapeadas")

    prontas: list[tuple[str, str, str, str]] = []   # (file, qid, aula, prova_vigente)
    orfas: list[tuple[str, str, str]] = []
    sem_aula: list[tuple[str, str, str]] = []
    divergentes_hist: list[tuple[str, str, str, str, str]] = []

    # Contagem por prova vigente (decidida pelo slug)
    contagem_por_prova: Counter = Counter()
    contagem_por_aula: Counter = Counter()

    for path in sorted(QUESTOES_DIR.glob("q-*.md")):
        fm = parse_frontmatter(path)
        if fm.get("uc_origem", "").strip() != args.uc:
            continue
        qid = fm.get("id", path.stem)
        aula = fm.get("aula", "").strip()
        prova_hist = fm.get("prova", "").strip()
        tags = fm.get("tags", "")

        if aula and aula in cronograma:
            prova_vig = cronograma[aula]["prova"]
            prontas.append((path.name, qid, aula, prova_vig))
            contagem_por_prova[prova_vig] += 1
            contagem_por_aula[aula] += 1
            if prova_hist and prova_hist != prova_vig:
                divergentes_hist.append((path.name, qid, aula, prova_hist, prova_vig))
        elif aula:
            orfas.append((path.name, qid, aula))
            contagem_por_prova["HISTÓRICO"] += 1
        else:
            sem_aula.append((path.name, qid, tags[:80]))
            contagem_por_prova["SEM-CLASSIFICAÇÃO"] += 1

    write_report(args.uc, cronograma, prontas, orfas, sem_aula,
                 divergentes_hist, contagem_por_prova, contagem_por_aula)


def write_report(uc, cronograma, prontas, orfas, sem_aula,
                 divergentes_hist, contagem_por_prova, contagem_por_aula):
    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / f"classificacao-cronograma-{uc}.md"

    total = len(prontas) + len(orfas) + len(sem_aula)

    lines = [
        f"# Classificação por cronograma — {uc}",
        "",
        "*Read-only.* Este relatório informa o estado da classificação",
        "do banco frente ao cronograma vigente. Nenhum arquivo foi alterado.",
        "",
        f"- Total {uc}: **{total}**",
        f"- ✅ Prontas (aula no cronograma vigente): **{len(prontas)}**",
        f"- 📚 Órfãs (aula fora do cronograma): {len(orfas)} → vão para CADERNO histórico-ampliado",
        f"- ❓ Sem aula declarada: {len(sem_aula)} → ficam fora dos cadernos principais",
        f"- ⚠ Divergências históricas (informativo): {len(divergentes_hist)}",
        "",
        "## Distribuição por prova vigente (regra do cronograma 2026)",
        "",
    ]
    for prova in ["P1", "P2", "P3", "HISTÓRICO", "SEM-CLASSIFICAÇÃO"]:
        lines.append(f"- **{prova}**: {contagem_por_prova.get(prova, 0)} questões")
    lines.append("")

    lines.append("## Distribuição por aula (apenas as prontas)")
    lines.append("")
    by_prova_aula = {}
    for path, qid, aula, prova in prontas:
        by_prova_aula.setdefault(prova, Counter())[aula] += 1
    for prova in sorted(by_prova_aula.keys()):
        lines.append(f"### {prova}")
        lines.append("")
        for aula, n in sorted(by_prova_aula[prova].items(), key=lambda x: -x[1]):
            titulo = cronograma.get(aula, {}).get("titulo", "")
            lines.append(f"- `{aula}` — {n} questões — *{titulo}*")
        lines.append("")

    if sem_aula:
        lines.append("## ❓ Questões sem aula declarada (precisam classificação manual)")
        lines.append("")
        for path, qid, tags in sem_aula:
            lines.append(f"- `{path}` (id={qid}) — tags: `{tags}`")
        lines.append("")

    if orfas:
        lines.append("## 📚 Questões órfãs (aula fora do cronograma vigente)")
        lines.append("")
        for path, qid, aula in orfas:
            lines.append(f"- `{path}` (id={qid}) — aula declarada: `{aula}`")
        lines.append("")

    if divergentes_hist:
        lines.append("## ⚠ Divergências históricas (informativo — não-acionável)")
        lines.append("")
        lines.append("Estas questões têm aula no cronograma vigente, mas a `prova:` declarada")
        lines.append("(prova HISTÓRICA de origem) difere da prova vigente da mesma aula.")
        lines.append("Esperado: o cronograma muda ano a ano, conteúdo migra entre P1/P2/P3.")
        lines.append("")
        for path, qid, aula, prova_hist, prova_vig in divergentes_hist[:30]:
            lines.append(f"- `{path}` (id={qid}) — aula=`{aula}` · histórico=**{prova_hist}** · vigente=**{prova_vig}**")
        if len(divergentes_hist) > 30:
            lines.append(f"- ... e mais {len(divergentes_hist)-30} casos")
        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Relatório: {out}")
    print(f"  Prontas: {len(prontas)}")
    print(f"  Órfãs: {len(orfas)}")
    print(f"  Sem aula: {len(sem_aula)}")
    print(f"  Divergências históricas: {len(divergentes_hist)}")
    print(f"  Distribuição: {dict(contagem_por_prova)}")


if __name__ == "__main__":
    main()
