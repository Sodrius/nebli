#!/usr/bin/env python3
"""Comprime um PDF do NEBLI reamostrando as imagens embutidas, para gerar
uma cópia leve pronta pra upar no Drive / anexar em e-mail.

Motivação (canônico 2026-07-03): o extrair_slides.py exporta slides em
resolucao nativa altissima (~3000 px). Isso infla o PDF final (dezenas de MB)
sem ganho visivel — a ~290 DPI numa figura de 13 cm o olho e a impressora ja
saturam. Reamostrar pra metade em JPEG q85 corta ~10x o tamanho mantendo as
figuras legiveis (figura = mecanismo continua valendo: 290 DPI preserva o
mecanismo).

Uso:
    python comprimir_pdf.py <entrada.pdf> [saida.pdf] [--dpi-target N]
                            [--dpi-threshold N] [--quality N]

Se <saida.pdf> for omitida, grava ao lado da entrada com sufixo "-leve".
Nunca sobrescreve a entrada. Se a compressao nao reduzir o tamanho, mantem
a copia mesmo assim (idempotente) mas avisa no stderr.
"""
import argparse
import os
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("ERRO: PyMuPDF (fitz) nao instalado. `pip install pymupdf`.")


def comprimir(entrada, saida, dpi_threshold=250, dpi_target=225, quality=85):
    if not os.path.isfile(entrada):
        sys.exit(f"ERRO: entrada nao encontrada: {entrada}")
    if os.path.abspath(entrada) == os.path.abspath(saida):
        sys.exit("ERRO: saida nao pode ser igual a entrada (nao sobrescrevo o master).")

    orig_mb = os.path.getsize(entrada) / 1e6
    doc = fitz.open(entrada)
    doc.rewrite_images(
        dpi_threshold=dpi_threshold,
        dpi_target=dpi_target,
        quality=quality,
        lossless=True,
        lossy=True,
        color=True,
        gray=True,
    )
    os.makedirs(os.path.dirname(os.path.abspath(saida)), exist_ok=True)
    doc.save(saida, garbage=4, deflate=True, clean=True)

    # validacao: reabre e confere contagem de paginas + render da 1a pagina
    chk = fitz.open(saida)
    n_in = doc.page_count
    n_out = chk.page_count
    if n_out != n_in:
        sys.exit(f"ERRO: saida com {n_out} paginas, esperado {n_in}. Abortando.")
    chk[0].get_pixmap(dpi=72)  # levanta excecao se a pagina estiver corrompida

    out_mb = os.path.getsize(saida) / 1e6
    fator = orig_mb / out_mb if out_mb else 0
    print(f"[comprimir_pdf] {os.path.basename(entrada)}: "
          f"{orig_mb:.1f} MB -> {out_mb:.2f} MB ({fator:.1f}x menor) -> {saida}")
    if out_mb >= orig_mb:
        print("[comprimir_pdf] AVISO: compressao nao reduziu o tamanho "
              "(PDF talvez ja fosse leve ou sem imagens grandes).", file=sys.stderr)
    if out_mb > 25:
        print(f"[comprimir_pdf] AVISO: {out_mb:.1f} MB ainda acima de 25 MB "
              "(limite de anexo de e-mail). Considere --dpi-target menor.",
              file=sys.stderr)
    return saida


def main():
    ap = argparse.ArgumentParser(description="Comprime PDF NEBLI (copia leve).")
    ap.add_argument("entrada")
    ap.add_argument("saida", nargs="?", default=None)
    ap.add_argument("--dpi-threshold", type=int, default=250)
    ap.add_argument("--dpi-target", type=int, default=225)
    ap.add_argument("--quality", type=int, default=85)
    args = ap.parse_args()

    saida = args.saida
    if saida is None:
        base, ext = os.path.splitext(args.entrada)
        saida = f"{base}-leve{ext}"

    comprimir(args.entrada, saida,
              dpi_threshold=args.dpi_threshold,
              dpi_target=args.dpi_target,
              quality=args.quality)


if __name__ == "__main__":
    main()
