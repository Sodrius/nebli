#!/usr/bin/env python3
"""
NEBLI -- preparar_materiais.py
Catalogador único de materiais de entrada de uma aula.

Aceita slide, pergunta orientadora, textos de leitura, PDFs de referência,
notas do professor -- e produz um INDICE.md que o Orquestrador consome ao
montar o Tema Card Seção B, com o papel editorial de cada peça.

Uso:
    python3 typst-build/preparar_materiais.py <slug>

Lê de:  slides/<slug>/    (pasta canônica de entrada; qualquer arquivo lá)
Emite:
    figuras/<slug>/slide-XX.png + MAPA_CONTEUDO.txt  (se houver slide.pdf/foto)
    arquivos-trabalho/materiais/<slug>/INDICE.md
    arquivos-trabalho/materiais/<slug>/<extraidos>.txt  (texto de PDFs/perguntas)

Convenções de nome dentro de slides/<slug>/ (case-insensitive):
    slide*.pdf | slide*.png | slide*.jpg  -> slide do professor (figuras + escopo)
    perguntas*.txt | perguntas*.md | orient*.txt          -> âncora editorial
    leitura*.pdf | texto*.pdf | referencia*.pdf | *.pdf   -> aprofundamento validado
    leitura*.md  | texto*.md  | *.md                       -> aprofundamento validado
    README.md                                              -> nota do professor / meta-info

Qualquer outro arquivo é catalogado com papel "extra -- revisar" pra Orquestrador decidir.
"""

from __future__ import annotations
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

try:
    import fitz  # pymupdf
except ImportError:
    print("x pymupdf nao instalado. Rode: pip install pymupdf --break-system-packages", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = ROOT / "slides"
FIGURAS_DIR = ROOT / "figuras"
MATERIAIS_DIR = ROOT / "arquivos-trabalho" / "materiais"


def classificar(nome: str) -> str:
    low = nome.lower()
    if re.match(r"^(slide|apresentacao|apresentação)", low) and low.endswith((".pdf", ".png", ".jpg", ".jpeg")):
        return "slide"
    if re.match(r"^(perguntas?|orient|guia)", low) and low.endswith((".txt", ".md")):
        return "pergunta-orientadora"
    if re.match(r"^(leitura|texto|referencia|referência|artigo|capitulo|capítulo)", low):
        return "leitura"
    if low == "readme.md":
        return "nota-professor"
    if low.endswith(".pdf"):
        return "leitura"  # default para PDFs não-classificados
    if low.endswith((".txt", ".md")):
        return "leitura"
    if low.endswith((".png", ".jpg", ".jpeg", ".webp")):
        return "figura-avulsa"
    return "extra"


PAPEL_EDITORIAL = {
    "slide":                 "ESCOPO + FIGURAS -- fonte primária do que entra no resumo. E1 cita `slide-XX.png` via MAPA_CONTEUDO.",
    "pergunta-orientadora":  "ÂNCORA EDITORIAL -- toda pergunta orientadora VIRA subtópico ou é cobrada explicitamente em E2/E3. Declarar cobertura no Tema Card Seção B.",
    "leitura":               "APROFUNDAMENTO VALIDADO -- fonte de mecanismo/nuance que sobe a profundidade da E1 SEM depender do AnKing. Rank > conhecimento base.",
    "nota-professor":        "META-INFO -- recorte, ênfase, bibliografia recomendada. Ler antes do Tema Card.",
    "figura-avulsa":         "FIGURA COMPLEMENTAR -- avaliar se cobre lacuna do slide (foto de peça, esquema do prof).",
    "extra":                 "REVISAR -- classificação automática falhou; Orquestrador decide papel manualmente.",
}


def extrair_pdf_texto(pdf_path: Path, saida_txt: Path, max_chars: int = 8000):
    """Extrai texto digital de um PDF (sem OCR). Trunca em max_chars com sinalizacao."""
    doc = fitz.open(str(pdf_path))
    partes = [f"# {pdf_path.name} -- {len(doc)} paginas"]
    total = 0
    for i, page in enumerate(doc, start=1):
        t = page.get_text("text").strip()
        t = " ".join(t.split())
        if not t:
            continue
        partes.append(f"\n## p{i}\n{t}")
        total += len(t)
        if total > max_chars:
            partes.append(f"\n\n[... texto truncado em ~{max_chars} chars; abrir PDF direto se precisar do resto]")
            break
    saida_txt.parent.mkdir(parents=True, exist_ok=True)
    saida_txt.write_text("\n".join(partes) + "\n", encoding="utf-8")


def rodar_extrair_slides(slide_pdf: Path, slug: str):
    """Delega para extrair_slides.py -- não duplica lógica."""
    script = ROOT / "typst-build" / "extrair_slides.py"
    r = subprocess.run(
        [sys.executable, str(script), str(slide_pdf), slug],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        print(f"! extrair_slides falhou:\n{r.stderr}", file=sys.stderr)
    else:
        print(r.stdout.strip())


def preparar(slug: str):
    entrada = SLIDES_DIR / slug
    if not entrada.exists():
        print(f"x pasta de entrada nao existe: {entrada}", file=sys.stderr)
        print(f"  crie e coloque os materiais dentro (slide.pdf, perguntas-orientadoras.txt, leitura-*.pdf ...)", file=sys.stderr)
        sys.exit(1)

    arquivos = sorted([p for p in entrada.iterdir() if p.is_file()])
    if not arquivos:
        print(f"x pasta vazia: {entrada}", file=sys.stderr)
        sys.exit(1)

    print(f"-> {len(arquivos)} material(is) em {entrada.relative_to(ROOT)}")

    saida_materiais = MATERIAIS_DIR / slug
    saida_materiais.mkdir(parents=True, exist_ok=True)

    catalogados: list[tuple[str, Path, Optional[Path]]] = []  # (papel, entrada, extraido)

    for arq in arquivos:
        papel = classificar(arq.name)
        extraido: Optional[Path] = None

        if papel == "slide" and arq.suffix.lower() == ".pdf":
            print(f"  [slide] {arq.name} -> extrair_slides.py")
            rodar_extrair_slides(arq, slug)
        elif papel in ("leitura",) and arq.suffix.lower() == ".pdf":
            saida_txt = saida_materiais / (arq.stem + ".txt")
            print(f"  [leitura] {arq.name} -> {saida_txt.relative_to(ROOT)}")
            extrair_pdf_texto(arq, saida_txt)
            extraido = saida_txt
        elif papel in ("pergunta-orientadora", "leitura", "nota-professor") and arq.suffix.lower() in (".txt", ".md"):
            destino = saida_materiais / arq.name
            shutil.copy2(arq, destino)
            extraido = destino
            print(f"  [{papel}] {arq.name} -> {destino.relative_to(ROOT)}")
        else:
            print(f"  [{papel}] {arq.name}")

        catalogados.append((papel, arq, extraido))

    indice = saida_materiais / "INDICE.md"
    linhas = [
        f"# Materiais catalogados -- {slug}",
        f"",
        f"Gerado por `preparar_materiais.py`. **Orquestrador**: use este índice ao montar a Seção B do Tema Card.",
        f"Cada linha da tabela abaixo declara o **papel editorial** do material -- perguntas orientadoras viram âncora,",
        f"leituras viram fonte de aprofundamento sem depender do AnKing, slide continua sendo escopo + figuras.",
        f"",
        f"| Papel | Arquivo original | Extraído para | Papel editorial |",
        f"|---|---|---|---|",
    ]
    for papel, orig, ext in catalogados:
        orig_rel = orig.relative_to(ROOT)
        ext_rel = ext.relative_to(ROOT) if ext else "-"
        linhas.append(f"| **{papel}** | `{orig_rel}` | `{ext_rel}` | {PAPEL_EDITORIAL[papel]} |")

    linhas += [
        "",
        "## Nota pro Tema Card",
        "",
        "- Se houver `pergunta-orientadora`, **liste cada pergunta na Seção B** e marque em qual subtópico da E1 ela será respondida + em qual questão da E2/E3 ela será cobrada. Pergunta orientadora sem cobertura em E2/E3 = lacuna que trava o fechamento.",
        "- Se houver `leitura`, **cite explicitamente na Seção B** como fonte de aprofundamento (sobe o teto de profundidade da E1 SEM depender do AnKing/Step 1). Ranking: leitura do prof > AnKing > conhecimento base.",
        "- Se **não houver slide**, marque no Tema Card Seção A `slide: ausente` e declare recorte via leituras/perguntas orientadoras.",
    ]
    indice.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"\n-> INDICE em {indice.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser(description="Cataloga materiais de uma aula (slide, perguntas orientadoras, leituras).")
    ap.add_argument("slug", help="slug da aula (pasta em slides/<slug>/)")
    args = ap.parse_args()
    preparar(args.slug)


if __name__ == "__main__":
    main()
