"""
Phase B: pre-processamento das apostilas historicas.

Para cada PDF em resumos-gerados/apostilas-historicas/:
  1. pdftotext -layout -> arquivos-trabalho/apostilas-historicas/<slug>.txt
  2. PyMuPDF extrai metadata por pagina e selecao de paginas-amostra
     -> arquivos-trabalho/apostilas-historicas/<slug>-estrutura.json
"""

from __future__ import annotations
import json
import re
import subprocess
from pathlib import Path

import fitz  # type: ignore

ROOT = Path(r"C:\AI use\nebli")
PDFS = ROOT / "resumos-gerados" / "apostilas-historicas"
OUT = ROOT / "arquivos-trabalho" / "apostilas-historicas"

def detectar_sumario(page) -> bool:
    txt = page.get_text("text")
    linhas = [l for l in txt.split("\n") if l.strip()]
    # heuristica: titulo "SUMARIO"/"INDICE" OU >= 5 linhas com ponto-leader ou numero de pagina final
    if any(re.search(r"\b(sum[áa]rio|[íi]ndice|conte[úu]do)\b", l, re.I) for l in linhas[:3]):
        return True
    leaders = sum(1 for l in linhas if re.search(r"\.{3,}\s*\d+\s*$", l) or re.search(r"\s{2,}\d+\s*$", l))
    return leaders >= 5

def detectar_resumindo(page) -> bool:
    txt = page.get_text("text").lower()
    return "resumindo" in txt[:300] or "resumindo a" in txt or "em resumo" in txt[:200]

def detectar_e2(page) -> bool:
    txt = page.get_text("text")
    return bool(re.search(r"(quest[ãa]o\s*0?1\b|etapa\s*2|exerc[íi]cios objetiv)", txt, re.I))

def detectar_gabarito(page) -> bool:
    txt = page.get_text("text").lower()
    return "gabarito" in txt[:500]

def selecionar_paginas_amostra(doc, paginas_meta: list[dict]) -> list[int]:
    """Devolve 5-8 paginas 1-indexed cobrindo: capa, sumario, parte, mais densa,
    mais figuras, resumindo, e2, gabarito."""
    n = len(paginas_meta)
    escolhidas: dict[str, int] = {}
    escolhidas["capa"] = 1
    for p in paginas_meta:
        idx = p["pagina"]
        if "sumario" not in escolhidas and detectar_sumario(doc[idx - 1]):
            escolhidas["sumario"] = idx
        if "resumindo" not in escolhidas and detectar_resumindo(doc[idx - 1]):
            escolhidas["resumindo"] = idx
        if "e2" not in escolhidas and detectar_e2(doc[idx - 1]):
            escolhidas["e2"] = idx
    # pagina mais densa (mais palavras)
    densa = max(paginas_meta, key=lambda p: p["palavras"])
    escolhidas["densa"] = densa["pagina"]
    # pagina com mais figuras
    figs = max(paginas_meta, key=lambda p: p["imagens"])
    if figs["imagens"] > 0:
        escolhidas["figuras"] = figs["pagina"]
    # ultima pagina (gabarito provavel)
    escolhidas["ultima"] = n
    # abertura de parte: pagina com densidade baixa de texto e titulo grande
    candidatos_parte = [p for p in paginas_meta if 30 < p["palavras"] < 200]
    if candidatos_parte:
        escolhidas["parte"] = candidatos_parte[len(candidatos_parte) // 2]["pagina"]
    # dedup e limita a 8
    paginas = sorted(set(escolhidas.values()))[:8]
    return paginas

def processar_pdf(pdf: Path) -> dict:
    slug = pdf.stem
    txt_out = OUT / f"{slug}.txt"
    json_out = OUT / f"{slug}-estrutura.json"

    # 1) pdftotext -layout
    subprocess.run(
        ["pdftotext", "-layout", str(pdf), str(txt_out)],
        check=True,
        capture_output=True,
    )

    # 2) PyMuPDF
    doc = fitz.open(pdf)
    paginas_meta = []
    for i, page in enumerate(doc, start=1):
        txt = page.get_text("text")
        palavras = len(txt.split())
        imagens = len(page.get_images(full=False))
        # primeira linha nao vazia como "titulo da pagina"
        primeira_linha = ""
        for l in txt.split("\n"):
            if l.strip():
                primeira_linha = l.strip()[:140]
                break
        paginas_meta.append({
            "pagina": i,
            "palavras": palavras,
            "imagens": imagens,
            "primeira_linha": primeira_linha,
        })

    paginas_amostra = selecionar_paginas_amostra(doc, paginas_meta)
    total_pag = len(doc)
    total_imgs = sum(p["imagens"] for p in paginas_meta)
    total_palavras = sum(p["palavras"] for p in paginas_meta)
    doc.close()

    estrutura = {
        "slug": slug,
        "pdf_path": str(pdf).replace("\\", "/"),
        "txt_path": str(txt_out).replace("\\", "/"),
        "total_paginas": total_pag,
        "total_palavras": total_palavras,
        "total_imagens": total_imgs,
        "media_palavras_pagina": round(total_palavras / total_pag, 1) if total_pag else 0,
        "paginas_amostra": paginas_amostra,
        "paginas_amostra_str": ",".join(str(p) for p in paginas_amostra),
        "paginas": paginas_meta,
    }
    json_out.write_text(json.dumps(estrutura, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "slug": slug,
        "paginas": total_pag,
        "palavras": total_palavras,
        "imagens": total_imgs,
        "amostra": paginas_amostra,
    }

def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(p for p in PDFS.glob("*.pdf"))
    print(f"Processando {len(pdfs)} PDFs.")
    resumo = []
    for pdf in pdfs:
        try:
            info = processar_pdf(pdf)
            resumo.append(info)
            print(f"  ok {info['slug']}: {info['paginas']}pp, {info['palavras']}pal, {info['imagens']}img, amostra={info['amostra']}")
        except Exception as e:  # noqa: BLE001
            print(f"  ERRO {pdf.name}: {e}")
    # sumario csv-ish
    (OUT / "_resumo-estrutura.md").write_text(
        "# Resumo estrutural\n\n| Slug | Pag | Palavras | Imagens | Amostra |\n|---|---|---|---|---|\n"
        + "\n".join(
            f"| {r['slug']} | {r['paginas']} | {r['palavras']} | {r['imagens']} | {r['amostra']} |"
            for r in resumo
        ),
        encoding="utf-8",
    )
    print(f"\nResumo estrutural em {OUT / '_resumo-estrutura.md'}")

if __name__ == "__main__":
    main()
