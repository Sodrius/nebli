"""
pipeline_caderno.py — Orquestra a geração de um caderno de questões de ponta a ponta.

Etapas em sequência (qualquer falha aborta o pipeline):
  1. Valida cronograma: a prova existe em aulas_uc<N>.yml? (HISTORICO sempre vale)
  2. gerar_caderno.py        → typst-build/_cadernos/caderno-uc<N>-<p>.typ
  3. render_caderno.py       → resumos-gerados/CADERNO-UC<N>-<PROVA>.pdf
  4. auditar_caderno_pdf.py  → arquivos-trabalho/auditoria-pdf-CADERNO-UC<N>-<PROVA>.md
  5. verificar_gabarito_ordem.py --apenas → arquivos-trabalho/verificacao-gabarito-CADERNO-UC<N>-<PROVA>.md

Uso:
  python typst-build/pipeline_caderno.py --uc UC1 --prova P1
  python typst-build/pipeline_caderno.py --uc UC1 --prova HISTORICO
"""
from __future__ import annotations
import argparse
import re
import subprocess
import sys
from pathlib import Path

# Força stdout/stderr em UTF-8 (Windows cp1252 quebra com emojis e acentos).
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import yaml

ROOT = Path(__file__).resolve().parent.parent
TYPST_BUILD = ROOT / "typst-build"
CADERNOS_DIR = TYPST_BUILD / "_cadernos"
PDF_OUT_DIR = ROOT / "resumos-gerados"
AUDIT_DIR = ROOT / "arquivos-trabalho"

VALID_PROVAS = {"P1", "P2", "P3", "HISTORICO"}


def uc_num(uc: str) -> int:
    return int(uc.replace("UC", "").lstrip("0") or "1")


def uc_canonico(uc: str) -> str:
    """'uc1' / 'UC01' / 'UC1' → 'UC1'."""
    n = uc_num(uc)
    return f"UC{n}"


def caderno_label(uc: str, prova: str) -> str:
    return f"CADERNO-UC{uc_num(uc):02d}-{prova}"


def validar_cronograma(uc: str, prova: str) -> tuple[bool, str]:
    n = uc_num(uc)
    yaml_path = ROOT / "banco" / f"aulas_uc{n:02d}.yml"
    if not yaml_path.exists():
        yaml_path = ROOT / "banco" / f"aulas_uc{n}.yml"
    if not yaml_path.exists():
        return False, f"cronograma não encontrado: aulas_uc{n:02d}.yml"
    if prova == "HISTORICO":
        return True, "HISTORICO sempre válido (questões fora do cronograma)"
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    aulas = data.get("aulas", []) or []
    com_prova = [a for a in aulas if str(a.get("prova", "")).strip() == prova]
    if not com_prova:
        return False, f"nenhuma aula com prova={prova} no cronograma de UC{n}"
    return True, f"{len(com_prova)} aulas mapeadas para {prova} em UC{n}"


def _ascii_safe(s: str) -> str:
    return s.encode("ascii", "replace").decode("ascii")


def run_step(label: str, cmd: list[str]) -> tuple[int, str, str]:
    print(_ascii_safe(f"\n=== [{label}] {' '.join(cmd)}"))
    try:
        result = subprocess.run(cmd, capture_output=True, text=True,
                                encoding="utf-8", errors="replace", timeout=300)
    except FileNotFoundError as e:
        print(f"  ERRO: executavel nao encontrado -- {e}")
        return 127, "", str(e)
    if result.stdout.strip():
        print(_ascii_safe(result.stdout.rstrip()))
    if result.stderr.strip():
        print("STDERR:", _ascii_safe(result.stderr.rstrip()))
    return result.returncode, result.stdout, result.stderr


def avaliar_auditoria(md_path: Path) -> tuple[bool, list[str]]:
    """Lê o .md de auditoria e decide se passa. Bloqueia só em mojibake — a
    contagem de questões e a integridade do gabarito são checadas no passo
    seguinte (verificar_gabarito_ordem.py), com IDs sequenciais que o
    auditar_caderno_pdf.py ainda não conhece. Warnings (ascii residual,
    hifenização, semi-vazias, "cobertura X/Y" desalinhada) só aparecem no
    print, não param o pipeline.
    """
    if not md_path.exists():
        return False, [f"relatorio nao gerado: {md_path}"]
    texto = md_path.read_text(encoding="utf-8")
    erros = []
    if "❌ Mojibake detectado" in texto:
        erros.append("mojibake detectado")
    return (not erros), erros


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--uc", default="UC1", help="UC1 | UC2 | ...")
    ap.add_argument("--prova", required=True, help="P1 | P2 | P3 | HISTORICO")
    args = ap.parse_args()

    uc = uc_canonico(args.uc)
    prova = args.prova.upper().strip()
    if prova not in VALID_PROVAS:
        print(f"ERRO: --prova deve ser uma de {sorted(VALID_PROVAS)}")
        return 2

    print(f"\n## Pipeline caderno -- {uc} / {prova}")
    ok, msg = validar_cronograma(uc, prova)
    print(f"  cronograma: {msg}")
    if not ok:
        print(f"  ❌ {msg}")
        return 3

    pdf_name = f"{caderno_label(uc, prova)}.pdf"
    typ_name = f"caderno-{uc.lower()}-{prova.lower()}.typ"
    typ_path = CADERNOS_DIR / typ_name
    pdf_path = PDF_OUT_DIR / pdf_name

    # 1. gerar .typ
    rc, _, _ = run_step("gerar", ["python", str(TYPST_BUILD / "gerar_caderno.py"),
                                   "--uc", uc, "--prova", prova])
    if rc != 0:
        print(f"\n❌ gerar_caderno falhou (exit {rc})")
        return 10 + rc
    if not typ_path.exists():
        print(f"\n❌ esperado em {typ_path}, não existe")
        return 11

    # 2. render PDF
    rc, _, _ = run_step("render", ["python", str(TYPST_BUILD / "render_caderno.py"),
                                    "--in", str(typ_path), "--out", str(pdf_path)])
    if rc != 0:
        print(f"\n❌ render_caderno falhou (exit {rc})")
        return 20 + rc
    if not pdf_path.exists():
        print(f"\n❌ PDF não foi escrito em {pdf_path}")
        return 21

    # 3. auditar PDF
    rc, _, _ = run_step("audit", ["python", str(TYPST_BUILD / "auditar_caderno_pdf.py"),
                                   str(pdf_path), "--uc", uc, "--prova", prova])
    if rc != 0:
        print(f"\n❌ auditar_caderno_pdf falhou (exit {rc})")
        return 30 + rc
    audit_md = AUDIT_DIR / f"auditoria-pdf-{pdf_path.stem}.md"
    ok_audit, erros_audit = avaliar_auditoria(audit_md)
    if not ok_audit:
        print("\n❌ Auditoria bloqueante:")
        for e in erros_audit:
            print(f"  - {e}")
        print(f"  Relatório: {audit_md}")
        return 31

    # 4. verificar gabarito (contagem + ordem + correção)
    rc, _, _ = run_step("verify", ["python", str(TYPST_BUILD / "verificar_gabarito_ordem.py"),
                                    "--apenas", pdf_name])
    if rc != 0:
        verif_md = AUDIT_DIR / f"verificacao-gabarito-{pdf_path.stem}.md"
        print(f"\n❌ verificar_gabarito_ordem falhou (exit {rc})")
        print(f"  Relatório: {verif_md}")
        return 40 + rc

    # 5. resumo final
    size_kb = pdf_path.stat().st_size // 1024
    print("\n=== ✅ Pipeline completo")
    print(f"  PDF:        {pdf_path}  ({size_kb} KB)")
    print(f"  Auditoria:  {audit_md}")
    print(f"  Gabarito:   {AUDIT_DIR / f'verificacao-gabarito-{pdf_path.stem}.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
