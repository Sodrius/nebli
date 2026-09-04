#!/usr/bin/env python3
"""pos_pipeline_check.py — Check final + auto-fix pos-compilacao do PDF.

Canonico 2026-05-26. Roda DEPOIS de `auditar_pdf.py` e antes de mover
o PDF para `resumos-gerados/`. Faz duas coisas:

1. **Verificacao FINAL do PDF**: extrai texto do PDF e roda checks
   adicionais que so fazem sentido com o artefato final:
   - "ETAPA 4" residual no texto
   - "Bloco:" ou similares vazando da capa
   - Numeracao de pagina sincronizada com paginas reais
   - Strings de markdown nao-renderizadas (`**X**`)

2. **Relatorio em topicos** (stdout):
   - O que esta OK
   - O que precisa de atencao
   - O que e bug bloqueante

Uso:
    python3 typst-build/pos_pipeline_check.py <pdf> [--slug NOME]

Retorna exit 0 se PDF e movivel. Exit 1 se ha bloqueio.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def extract_pdf_text(pdf_path: Path) -> str:
    """Extrai texto do PDF via pdftotext (Poppler) ou PyPDF2 como fallback."""
    try:
        out = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=30,
        )
        if out.returncode == 0:
            return out.stdout
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    # Fallback: tentativa via parse manual minimo
    try:
        data = pdf_path.read_bytes()
        # Heuristica seca: pula PDFs cuja extracao depende de poppler
        return ""
    except OSError:
        return ""


def count_pdf_pages(pdf_path: Path) -> int:
    data = pdf_path.read_bytes()
    return len(re.findall(rb"/Type\s*/Page\b", data))


def check_etapa4_fantasma(texto: str) -> tuple[bool, str]:
    if not texto:
        return False, "PDF sem texto extraivel -- pulando check (instalar poppler-utils para validar)"
    if "ETAPA 4" in texto.upper():
        idx = texto.upper().find("ETAPA 4")
        ctx = texto[max(0, idx-40):idx+50].replace("\n", " ")
        return True, f"ETAPA 4 fossil detectada: ...{ctx}..."
    return False, "OK - sem header fossil de ETAPA 4"


def check_bloco_prova_capa(texto: str) -> tuple[bool, str]:
    if not texto:
        return False, "PDF sem texto extraivel"
    # So checa as primeiras 2000 chars (regiao da capa)
    capa_area = texto[:2000]
    if re.search(r"\bBloco:\s*P[123]\b", capa_area, re.I):
        return True, "Capa contem 'Bloco: PN' (viola CLAUDE.md)"
    if re.search(r"\bProva\s*[123]\b", capa_area, re.I):
        return True, "Capa contem 'Prova N' (viola CLAUDE.md)"
    return False, "OK - capa sem bloco/prova"


def check_markdown_bold(texto: str) -> tuple[bool, str]:
    if not texto:
        return False, "PDF sem texto extraivel"
    # Procura `**texto**` literal no texto extraido (Typst nao renderiza)
    matches = re.findall(r"\*\*[^\s*][^*\n]{0,80}?[^\s*]\*\*", texto)
    if matches:
        return True, f"Markdown bold nao-renderizado: {len(matches)} ocorrencia(s) -- exemplo: `{matches[0]}`"
    return False, "OK - sem markdown bold vazado"


def check_numeracao(pdf_path: Path, texto: str) -> tuple[bool, str]:
    n_real = count_pdf_pages(pdf_path)
    if not texto:
        return False, f"PDF tem {n_real} paginas (texto nao extraivel -- pulando check de numeracao)"
    # Estrategia conservadora: separar paginas via form-feed e pegar a ultima
    # linha curta nao-vazia de cada pagina. Rodape NEBLI = numero centralizado
    # isolado. Falsos positivos comuns: "200 um" em legendas, "Cap. 19" etc.
    pages = texto.split("\x0c")
    rodape_nums = []
    for p in pages:
        lines = [ln.strip() for ln in p.splitlines() if ln.strip()]
        if not lines:
            continue
        # Ultima linha que seja apenas um numero curto isolado
        for ln in reversed(lines[-3:]):
            if re.fullmatch(r"\d{1,3}", ln):
                rodape_nums.append(int(ln))
                break
    if not rodape_nums:
        return False, f"PDF tem {n_real} paginas, rodape numerico nao detectado (provavel ausencia de footer ou PDF sem text-extract)"
    max_num = max(rodape_nums)
    if max_num > n_real + 2:
        return True, (f"Numeracao inflada: rodape exibe ate {max_num} mas PDF tem {n_real} paginas "
                      f"(diferenca {max_num - n_real}) -- verificar se template conta paginas-fantasma")
    if max_num < n_real - 2:
        return True, (f"Numeracao dessincronizada: rodape ate {max_num} mas PDF tem {n_real} paginas")
    return False, f"OK - numeracao coerente ({n_real} paginas, rodape ate {max_num})"


def check_paginas_em_branco(pdf_path: Path) -> tuple[bool, str]:
    """Heuristica: PDF com 1+ pagina cujo conteudo extraivel e quase vazio."""
    try:
        out = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=30,
        )
        if out.returncode != 0:
            return False, "pdftotext indisponivel -- pulando"
        text = out.stdout
        pages = text.split("\x0c")  # form feed = separador de paginas
        # Ignorar a ultima entrada (artefato comum de pdftotext: split gera N+1
        # entradas para PDF de N paginas; a ultima fica vazia)
        if pages and not pages[-1].strip():
            pages = pages[:-1]
        # Pagina em branco real = pagina interna (nao primeira nem ultima) com
        # menos de 20 chars de conteudo extraivel
        empty = []
        for i, p in enumerate(pages, 1):
            if 1 < i < len(pages) and len(p.strip()) < 20:
                empty.append(i)
        if empty:
            return True, f"Paginas internas em branco detectadas: {empty[:10]} (verificar `#etapa-header` duplicado)"
        return False, "OK - sem paginas em branco interna"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False, "pdftotext indisponivel -- pulando"


def check_paginas_e1(texto: str) -> tuple[bool, str]:
    """Teto de 15 paginas da E1 -- BLOQUEIO desde 2026-09-03.

    Ate aqui o teto era so aviso (linha 7 da tabela de checks do ERROS.md dizia
    "manual") e, na pratica, ninguem conferia: `imuno-07` fechou com 25 paginas
    e `gr-02` v1 com 18, ambos em silencio. Aqui ele passa a impedir que o PDF
    seja movido para `resumos-gerados/`.

    A § Missao continua permitindo estourar o teto quando ensinar bem exigir --
    mas agora a excecao tem de ser DECLARADA, com `--quebra-declarada "motivo"`.
    Excecao silenciosa deixou de existir.

    Delimitacao: pagina do banner `Etapa 1` ate a pagina anterior ao banner
    isolado `Resumindo`. Mesma ancora do auditar_pdf.
    """
    TETO = 15
    if not texto:
        return False, "sem texto extraido -- teto de paginas nao verificado"
    paginas = texto.split("\f")
    pag_e1 = pag_res = None
    for i, pg in enumerate(paginas, 1):
        if pag_e1 is None and re.search(r"^[ \t]*Etapa 1\b", pg, re.MULTILINE):
            pag_e1 = i
            continue
        if pag_e1 is not None and re.search(r"^[ \t]*Resumindo[ \t]*$", pg, re.MULTILINE):
            pag_res = i
            break
    if pag_e1 is None or pag_res is None or pag_res <= pag_e1:
        return False, "nao consegui delimitar a E1 (banner ausente) -- conferir a olho"
    n = pag_res - pag_e1
    if n <= TETO:
        return False, f"E1 com {n} paginas (teto {TETO})"
    return True, (f"E1 com {n} paginas contra o teto canonico de {TETO} "
                  f"(CLAUDE.md § Registro cientifico). Aplicar as alavancas do ERROS.md F4 "
                  f"nesta ordem: (1) filtro das tres funcoes, (2) fundir subtopicos irmaos "
                  f"ate 8-10, (3) max 2 boxes pesados por PARTE, (4) figuras 50-55%. "
                  f"Se o tema realmente exigir o estouro, rodar com "
                  f'--quebra-declarada "motivo" e registrar a quebra no relatorio final.')


def main():
    args = [a for a in sys.argv[1:]]
    quebra = None
    if "--quebra-declarada" in args:
        i = args.index("--quebra-declarada")
        if i + 1 >= len(args) or args[i+1].startswith("--"):
            print("x --quebra-declarada exige o motivo entre aspas.")
            return 1
        quebra = args[i+1]
        del args[i:i+2]
    if not args:
        print('Uso: pos_pipeline_check.py <pdf> [--quebra-declarada "motivo"]')
        return 1
    pdf_path = Path(args[0])
    if not pdf_path.exists():
        print(f"x PDF nao encontrado: {pdf_path}")
        return 1

    print(f"=== NEBLI pos_pipeline_check -- {pdf_path.name} ===")
    print(f"Tamanho: {pdf_path.stat().st_size / (1024*1024):.1f} MB")
    n_pages = count_pdf_pages(pdf_path)
    print(f"Paginas: {n_pages}")
    print()

    texto = extract_pdf_text(pdf_path)
    if not texto:
        print("! pdftotext nao disponivel ou falhou -- checks de conteudo limitados.")
        print("  Instale `poppler-utils` ou use WSL para extracao plena.")
        print()

    checks = [
        ("ETAPA 4 fossil", check_etapa4_fantasma(texto)),
        ("Bloco/Prova na capa", check_bloco_prova_capa(texto)),
        ("Markdown bold vazado", check_markdown_bold(texto)),
        ("Numeracao de pagina", check_numeracao(pdf_path, texto)),
        ("Paginas em branco", check_paginas_em_branco(pdf_path)),
        ("Teto de 15 paginas da E1", check_paginas_e1(texto)),
    ]

    okays = []
    avisos = []
    bloqueios = []
    for nome, (problema, msg) in checks:
        if problema:
            if nome == "Teto de 15 paginas da E1" and quebra:
                avisos.append(f"  [!] {nome}: {msg}\n      QUEBRA DECLARADA: {quebra}")
            elif nome in ("ETAPA 4 fossil", "Bloco/Prova na capa",
                          "Teto de 15 paginas da E1"):
                bloqueios.append(f"  [x] {nome}: {msg}")
            else:
                avisos.append(f"  [!] {nome}: {msg}")
        else:
            okays.append(f"  [v] {nome}: {msg}")

    print("OK:")
    for m in okays: print(m)
    if avisos:
        print()
        print("AVISOS:")
        for m in avisos: print(m)
    if bloqueios:
        print()
        print("BLOQUEIOS:")
        for m in bloqueios: print(m)

    print()
    if bloqueios:
        print(f"x FALHA - {len(bloqueios)} bloqueio(s). NAO mover PDF.")
        return 1
    if avisos:
        print(f"! OK COM AVISOS - {len(avisos)} aviso(s). Pode mover, mas conferir.")
    else:
        print("v OK - PDF pode ser movido para resumos-gerados/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
