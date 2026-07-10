"""
render_caderno.py — Compila um .typ de caderno para PDF.

Comando canônico:
  typst compile --root <projeto> --font-path <projeto>/fonts entrada.typ saida.pdf

Uso:
  python typst-build/render_caderno.py --in typst-build/_cadernos/caderno-uc1-p3.typ \
                                       --out resumos-gerados/CADERNO-UC01-P3.pdf
"""

from __future__ import annotations
import argparse
import subprocess
import sys
import time
from pathlib import Path


def render(typ_in: Path, pdf_out: Path) -> None:
    typ_in = typ_in.resolve()
    pdf_out = pdf_out.resolve()
    pdf_out.parent.mkdir(parents=True, exist_ok=True)

    # root é o diretório raiz do projeto (onde fica banco/, fonts/, etc).
    # Para .typ em typst-build/_cadernos/, root é typst-build/_cadernos/../../ = projeto.
    projeto_root = typ_in.parent.parent.parent
    fonts_dir = projeto_root / "fonts"

    args = [
        "typst", "compile",
        "--root", str(projeto_root),
        "--font-path", str(fonts_dir),
        str(typ_in),
        str(pdf_out),
    ]
    print(f"Compilando: {typ_in.name}")
    print(f"  root: {projeto_root}")
    print(f"  fonts: {fonts_dir}")
    t0 = time.time()
    result = subprocess.run(args, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=120)
    dt = time.time() - t0
    def safe(s: str) -> str:
        return s.encode("ascii", "replace").decode("ascii")
    if result.stdout.strip():
        print("STDOUT:", safe(result.stdout))
    if result.stderr.strip():
        print("STDERR:", safe(result.stderr))
    if result.returncode != 0:
        sys.exit(result.returncode)
    if not pdf_out.exists():
        print(f"ERRO: PDF não foi gerado em {pdf_out}")
        sys.exit(3)
    size = pdf_out.stat().st_size
    print(f"PDF gerado: {pdf_out} ({size:,} bytes, {dt:.1f}s)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="typ_in", required=True, type=Path)
    ap.add_argument("--out", dest="pdf_out", required=True, type=Path)
    args = ap.parse_args()
    if not args.typ_in.exists():
        print(f"Typst não existe: {args.typ_in}")
        sys.exit(1)
    render(args.typ_in, args.pdf_out)


if __name__ == "__main__":
    main()
