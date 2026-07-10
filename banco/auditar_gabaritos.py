"""
auditar_gabaritos.py — Auditoria de integridade dos gabaritos do banco.

Filosofia: três categorias de saída.
  - ok          → nada a fazer
  - corrigido   → fix inequívoco aplicado in-place, registrado no relatório
  - bloqueante  → ambiguidade ou inconsistência que exige decisão humana

Auto-correções aplicadas:
  * gabarito MC em caixa baixa ("c" → "C")
  * gabarito MC sem espaço acidental
  * gabarito ausente quando a explicação cita inequivocamente UMA letra
    via padrões fixos ("alternativa correta é X", "resposta: X", etc.)

Não auto-corrige: CE com formato malformado, MC com explicação
ambígua (cita 2+ letras), discrepância entre gabarito declarado e
o que a explicação afirma.

Uso:
  python banco/auditar_gabaritos.py --uc UC1
  python banco/auditar_gabaritos.py --uc UC1 --dry-run   (não grava)
"""

from __future__ import annotations
import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUESTOES_DIR = ROOT / "questoes"
OUT_DIR = ROOT.parent / "arquivos-trabalho"

FRONT_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
FIELD_RE = re.compile(r"^(\w+):\s*(.*)$", re.MULTILINE)

# Padrões inequívocos no texto da explicação que indicam UMA letra correta.
# Ordem importa: mais específico primeiro.
EXPL_PATTERNS = [
    re.compile(r"alternativa\s+correta\s+(?:é|:)\s*\(?([A-E])\)?", re.IGNORECASE),
    re.compile(r"resposta\s+correta\s+(?:é|:)\s*\(?([A-E])\)?", re.IGNORECASE),
    re.compile(r"gabarito\s*:\s*\(?([A-E])\)?\b", re.IGNORECASE),
    re.compile(r"a\s+resposta\s+(?:é|seria)\s*\(?([A-E])\)?", re.IGNORECASE),
]


@dataclass
class Finding:
    file: str
    qid: str
    level: str   # ok | corrigido | bloqueante | aviso
    motivo: str
    detalhe: str = ""


@dataclass
class Report:
    total: int = 0
    ok: int = 0
    findings: list[Finding] = field(default_factory=list)

    def add(self, f: Finding) -> None:
        self.findings.append(f)
        if f.level == "ok":
            self.ok += 1


def parse_question(path: Path) -> tuple[dict, str, str]:
    """Retorna (frontmatter_dict, frontmatter_raw, body)."""
    text = path.read_text(encoding="utf-8")
    m = FRONT_RE.match(text)
    if not m:
        return {}, "", text
    front_raw, body = m.group(1), m.group(2)
    fm = {}
    for fm_match in FIELD_RE.finditer(front_raw):
        k, v = fm_match.group(1), fm_match.group(2).strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
            v = v[1:-1]
        fm[k] = v
    return fm, front_raw, body


def extract_explicacao(body: str) -> str:
    m = re.search(r"##\s*Explica[çc][ãa]o\s*\n(.*?)(?=\n##\s|\Z)", body, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ""


def extract_itens_letras(body: str, front_raw: str) -> set[str]:
    """Pega as letras das alternativas declaradas no frontmatter (campo itens)."""
    letras = set()
    for m in re.finditer(r"^\s*-\s*letra:\s*([A-E])", front_raw, re.MULTILINE):
        letras.add(m.group(1))
    if letras:
        return letras
    # fallback: parsear o corpo procurando "(A)" ou "A)" no início de linha/bloco
    for m in re.finditer(r"\(([A-E])\)", body):
        letras.add(m.group(1))
    for m in re.finditer(r"^\s*([A-E])\)\s", body, re.MULTILINE):
        letras.add(m.group(1))
    return letras


def infer_letter_from_expl(expl: str) -> tuple[str | None, list[str]]:
    """Tenta inferir UMA letra a partir da explicação. Devolve (letra ou None, todas as detecções)."""
    hits = []
    for pat in EXPL_PATTERNS:
        for m in pat.finditer(expl):
            hits.append(m.group(1).upper())
    if not hits:
        return None, []
    unique = list(dict.fromkeys(hits))  # preserva ordem
    if len(unique) == 1:
        return unique[0], unique
    return None, unique  # ambiguidade


def audit_mc(qid: str, path: Path, fm: dict, front_raw: str, body: str, report: Report, dry_run: bool):
    gab = fm.get("gabarito", "").strip()
    expl = extract_explicacao(body)
    letras_validas = extract_itens_letras(body, front_raw)

    fixed = None

    # Caso 1: gabarito vazio
    if not gab:
        inferred, hits = infer_letter_from_expl(expl)
        if inferred:
            fixed = inferred
            report.add(Finding(path.name, qid, "corrigido",
                "gabarito vazio preenchido a partir da explicação",
                f"inferido: {inferred}"))
        else:
            report.add(Finding(path.name, qid, "bloqueante",
                "gabarito MC vazio e explicação não permite inferência única",
                f"hits ambíguos: {hits}" if hits else "explicação não cita alternativa"))
            return

    # Caso 2: gabarito com caixa errada ou espaços — só normaliza se virar letra válida
    elif gab != gab.upper().strip() and re.fullmatch(r"[A-Ea-e]", gab.strip()):
        fixed = gab.upper().strip()
        report.add(Finding(path.name, qid, "corrigido",
            "normalização de caixa/espaço",
            f"'{gab}' → '{fixed}'"))

    # Caso 3: formato inválido
    g_check = (fixed or gab).strip().upper()
    if not re.fullmatch(r"[A-E]", g_check):
        report.add(Finding(path.name, qid, "bloqueante",
            "gabarito MC não é uma única letra A–E",
            f"valor: '{gab}'"))
        return

    # Caso 4: letra não corresponde às alternativas declaradas
    if letras_validas and g_check not in letras_validas:
        report.add(Finding(path.name, qid, "bloqueante",
            "gabarito não corresponde a nenhuma alternativa declarada",
            f"gabarito='{g_check}' alternativas={sorted(letras_validas)}"))
        return

    # Caso 5: explicação contradiz o gabarito
    inferred, hits = infer_letter_from_expl(expl)
    if inferred and inferred != g_check:
        report.add(Finding(path.name, qid, "bloqueante",
            "gabarito declarado contradiz a explicação",
            f"declarado='{g_check}' explicação aponta='{inferred}'"))
        return

    # Aplicar correção se houve
    if fixed and not dry_run:
        new_text = new_front_or_inject(path.read_text(encoding="utf-8"), fixed)
        path.write_text(new_text, encoding="utf-8")

    if not fixed:
        report.add(Finding(path.name, qid, "ok", "MC íntegra"))


def new_front_or_inject(text: str, value: str) -> str:
    """Garante a existência da linha gabarito: VALOR no frontmatter (substitui se existir, injeta se não)."""
    if re.search(r"^gabarito:.*$", text, re.MULTILINE):
        return re.sub(r"^gabarito:.*$", f"gabarito: {value}", text, count=1, flags=re.MULTILINE)
    # injetar antes do fechamento --- do frontmatter
    return re.sub(r"^---\n(.*?)\n---", lambda m: f"---\n{m.group(1)}\ngabarito: {value}\n---", text, count=1, flags=re.DOTALL)


def audit_ce(qid: str, path: Path, fm: dict, body: str, report: Report):
    gab = fm.get("gabarito", "").strip()
    if not gab:
        report.add(Finding(path.name, qid, "bloqueante", "gabarito CE vazio"))
        return
    # Aceita padrões como "I-V; II-F; III-V; IV-F" ou "CCEEC" ou "1-V; 2-F"
    if re.fullmatch(r"[CEVFcevf]+", gab):
        report.add(Finding(path.name, qid, "ok", f"CE íntegra (formato string: {gab})"))
        return
    if re.fullmatch(r"(?:[IVXivx]+|\d+|[A-Ia-i])\s*-\s*[VFCEvfce](?:\s*;\s*(?:[IVXivx]+|\d+|[A-Ia-i])\s*-\s*[VFCEvfce])*", gab):
        report.add(Finding(path.name, qid, "ok", f"CE íntegra (formato item-valor)"))
        return
    report.add(Finding(path.name, qid, "aviso",
        "gabarito CE em formato não-canônico",
        f"valor: '{gab[:80]}'"))


def audit_discursiva(qid: str, path: Path, fm: dict, body: str, report: Report):
    # Davi pediu: incluir todas, com ou sem modelo. Aqui só sinaliza informativamente.
    has_modelo = bool(re.search(r"##\s*(Modelo|Resposta|Gabarito)", body, re.IGNORECASE))
    if has_modelo:
        report.add(Finding(path.name, qid, "ok", "discursiva com modelo"))
    else:
        report.add(Finding(path.name, qid, "aviso", "discursiva sem modelo no banco (será incluída sem referência)"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--uc", default="UC1", help="UC a auditar (filtro uc_origem)")
    ap.add_argument("--dry-run", action="store_true", help="não escreve arquivos")
    args = ap.parse_args()

    report = Report()
    files = sorted(QUESTOES_DIR.glob("q-*.md"))

    for path in files:
        fm, front_raw, body = parse_question(path)
        if not fm:
            continue
        uc = fm.get("uc_origem", "").strip()
        if uc != args.uc:
            continue
        report.total += 1

        qid = fm.get("id", path.stem)
        formato = fm.get("formato", "").strip().upper()

        if formato == "MC":
            audit_mc(qid, path, fm, front_raw, body, report, args.dry_run)
        elif formato == "CE":
            audit_ce(qid, path, fm, body, report)
        elif formato in {"DISCURSIVA", "DISC"}:
            audit_discursiva(qid, path, fm, body, report)
        else:
            report.add(Finding(path.name, qid, "aviso",
                f"formato desconhecido: '{formato}'"))

    write_report(report, args.uc, args.dry_run)


def write_report(report: Report, uc: str, dry_run: bool) -> None:
    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / f"auditoria-gabaritos-{uc}.md"

    by_level = {"ok": [], "corrigido": [], "aviso": [], "bloqueante": []}
    for f in report.findings:
        by_level.setdefault(f.level, []).append(f)

    lines = [
        f"# Auditoria de gabaritos — {uc}",
        f"",
        f"- Total auditado: **{report.total}**",
        f"- OK: {len(by_level['ok'])}",
        f"- Auto-corrigido: {len(by_level['corrigido'])}",
        f"- Avisos (não-bloqueante): {len(by_level['aviso'])}",
        f"- **Bloqueantes**: {len(by_level['bloqueante'])}",
        f"",
        f"Dry-run: {'sim — nada foi escrito' if dry_run else 'não — correções aplicadas in-place'}",
        f"",
    ]

    for level, label in [
        ("bloqueante", "❌ Bloqueantes (corrigir manualmente antes de gerar PDFs)"),
        ("corrigido", "✏ Auto-corrigidos (registrados para auditoria)"),
        ("aviso", "⚠ Avisos (informativos, não param o pipeline)"),
    ]:
        items = by_level[level]
        if not items:
            continue
        lines.append(f"## {label}")
        lines.append("")
        for f in items:
            lines.append(f"- `{f.file}` (id={f.qid}) — **{f.motivo}**" + (f". {f.detalhe}" if f.detalhe else ""))
        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Relatório: {out}")
    print(f"Total={report.total}  ok={len(by_level['ok'])}  corrigido={len(by_level['corrigido'])}  aviso={len(by_level['aviso'])}  bloqueante={len(by_level['bloqueante'])}")
    if by_level["bloqueante"]:
        sys.exit(2)


if __name__ == "__main__":
    main()
