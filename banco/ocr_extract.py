"""
ocr_extract.py — Utilitário OCR para o banco NEBLI
Converte PDF de imagem em texto usando tesseract + pymupdf.

Uso:
    python3 ocr_extract.py caminho/para/arquivo.pdf [--zoom 2.0] [--lang por]

Saída: texto bruto em stdout, ou salvo em arquivo .txt com mesmo nome do PDF.

Dependências (já instaladas no ambiente):
    pip install pymupdf pytesseract --break-system-packages
    tessdata em /tmp/tessdata/por.traineddata

Notas:
    - zoom=2.0 dá boa qualidade para provas médicas A4 escaneadas
    - lang=por funciona bem; fallback para eng se por não disponível
    - Páginas completamente brancas ou com <50 chars são marcadas [PÁGINA ILEGÍVEL]
"""

import os, sys, io, argparse
import fitz  # pymupdf
import pytesseract
from PIL import Image

# Tessdata baixado em sessão anterior
TESSDATA = os.environ.get("TESSDATA_PREFIX", "/tmp/tessdata")
os.environ["TESSDATA_PREFIX"] = TESSDATA


def ocr_pdf(pdf_path: str, zoom: float = 2.0, lang: str = "por") -> str:
    """Extrai texto de todas as páginas de um PDF via OCR."""
    # Verifica se tessdata existe; fallback para eng
    if not os.path.exists(os.path.join(TESSDATA, f"{lang}.traineddata")):
        print(f"[AVISO] {lang}.traineddata não encontrado em {TESSDATA}, usando eng", file=sys.stderr)
        lang = "eng"

    doc = fitz.open(pdf_path)
    pages_text = []
    mat = fitz.Matrix(zoom, zoom)

    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang=lang)
        text = text.strip()
        if len(text) < 50:
            pages_text.append(f"[PÁGINA {i+1} ILEGÍVEL]")
        else:
            pages_text.append(f"--- Página {i+1} ---\n{text}")

    return "\n\n".join(pages_text)


def main():
    parser = argparse.ArgumentParser(description="OCR de PDF para banco NEBLI")
    parser.add_argument("pdf", help="Caminho para o PDF")
    parser.add_argument("--zoom", type=float, default=2.0)
    parser.add_argument("--lang", default="por")
    parser.add_argument("--out", help="Arquivo de saída .txt (opcional)")
    args = parser.parse_args()

    text = ocr_pdf(args.pdf, zoom=args.zoom, lang=args.lang)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Salvo em {args.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
