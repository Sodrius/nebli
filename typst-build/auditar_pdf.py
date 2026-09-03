#!/usr/bin/env python3
"""
NEBLI -- auditar_pdf.py
Auditoria do PDF compilado antes de mover para resumos-gerados/.

Frente B3 do plano de economia (2026-05-16):
  No #6 Acidos Nucleicos, 5 arquivos foram compilados SEM NENHUMA
  acentuacao portuguesa e ninguem percebeu ate Davi abrir o PDF.
  Custo: +50k de retrabalho. Este script previne o caso.

Validacoes:
  1. Acentuacao: texto extraido tem >= 1.5% de letras acentuadas
     em amostragem de 3 paginas. Bloqueia < 0.5%.
  2. Paths de figuras existem fisicamente em figuras/[tema]/.
  3. Siglas sem duplicata no helper #sigla(...) da E1.

Uso:
  python3 typst-build/auditar_pdf.py PDF [--etapa1 etapa1.typ] [--tema slug]
  python3 typst-build/auditar_pdf.py resumos-gerados/ACIDOS_NUCLEICOS.pdf \
      --etapa1 typst-build/etapa1.typ --tema acidos-nucleicos

Exit codes:
  0 = ok -- pode mover PDF
  1 = falha de acentuacao
  2 = path de figura nao existe
  3 = sigla duplicada
  4 = PDF nao encontrado ou pdftotext ausente
  5 = fonte errada (fallback ativado, faltou --font-path na compilacao)
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path


ACENTOS = set("áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ")
LIMIAR_ERRO_PCT = 0.5
LIMIAR_AVISO_PCT = 1.5


def pdf_pages(pdf_path: Path) -> int:
    """Conta paginas via pdfinfo, fallback pra 1."""
    try:
        out = subprocess.run(["pdfinfo", str(pdf_path)], capture_output=True, text=True, timeout=10)
        for line in out.stdout.split("\n"):
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except Exception:
        pass
    return 1


def pdf_text(pdf_path: Path, first: int, last: int) -> str:
    """Extrai texto de paginas via pdftotext."""
    try:
        out = subprocess.run(
            ["pdftotext", "-f", str(first), "-l", str(last), str(pdf_path), "-"],
            capture_output=True, timeout=30
        )
        try:
            return out.stdout.decode("utf-8")
        except UnicodeDecodeError:
            return out.stdout.decode("latin-1", errors="replace")
    except FileNotFoundError:
        print("x pdftotext nao encontrado. Instale poppler-utils.", file=sys.stderr)
        sys.exit(4)
    except Exception as e:
        print(f"x pdftotext falhou: {e}", file=sys.stderr)
        return ""


def check_acentuacao(pdf_path: Path) -> tuple[list, list]:
    """Amostra 3 paginas (1, meio, gabarito) e mede acentos."""
    errors, warnings = [], []
    n_pages = pdf_pages(pdf_path)
    samples = [
        ("inicio", 2, min(4, n_pages)),
        ("meio", max(1, n_pages // 2), min(n_pages // 2 + 2, n_pages)),
        ("fim", max(1, n_pages - 2), n_pages),
    ]
    for label, first, last in samples:
        text = pdf_text(pdf_path, first, last)
        # Conta so letras (ignora numeros/punct/whitespace)
        letras = [c for c in text if c.isalpha()]
        if len(letras) < 200:
            warnings.append(f"  ! acentos {label} (p{first}-{last}): texto < 200 letras, "
                            f"amostra pequena (provavel pagina mais grafica)")
            continue
        n_acentos = sum(1 for c in letras if c in ACENTOS)
        pct = n_acentos / len(letras) * 100
        if pct < LIMIAR_ERRO_PCT:
            errors.append(f"  x acentos {label} (p{first}-{last}): "
                          f"{n_acentos}/{len(letras)} letras = {pct:.2f}% "
                          f"(piso {LIMIAR_ERRO_PCT}%). Texto provavelmente sem acentuacao -- BLOQUEAR.")
        elif pct < LIMIAR_AVISO_PCT:
            warnings.append(f"  ! acentos {label} (p{first}-{last}): "
                            f"{pct:.2f}% (esperado >= {LIMIAR_AVISO_PCT}%). Conferir manual.")
        else:
            print(f"  v acentos {label} (p{first}-{last}): {pct:.2f}% ({n_acentos}/{len(letras)})")
    return errors, warnings


def check_figuras_paths(etapa_files: list[Path], project_root: Path) -> tuple[list, list]:
    """Toda chamada a image()/figura-nebli/figura-lateral com path
    absoluto /figuras/... deve apontar pra arquivo existente."""
    errors, warnings = [], []
    path_re = re.compile(r'["\']\s*(/figuras/[^"\']+\.(?:png|jpg|jpeg|svg))\s*["\']', re.IGNORECASE)
    seen = set()
    for f in etapa_files:
        if not f.exists():
            continue
        content = f.read_text(encoding="utf-8")
        for m in path_re.finditer(content):
            rel = m.group(1).lstrip("/")  # tira a / inicial -> figuras/.../slide-XX.png
            abs_path = project_root / rel
            key = (f.name, rel)
            if key in seen:
                continue
            seen.add(key)
            if not abs_path.exists():
                errors.append(f"  x figura {f.name}: /{rel} NAO EXISTE em disco -- BLOQUEAR.")
    if not errors and seen:
        print(f"  v figuras: {len(seen)} paths /figuras/... distintos, todos existem")
    return errors, warnings


def check_siglas_duplicadas(etapa1_path: Path) -> tuple[list, list]:
    """Cada #sigla("X", [...]) com X diferente deve aparecer 1x na 1a aparicao.
    Mesma sigla repetida com expansoes distintas = bug."""
    errors, warnings = [], []
    if not etapa1_path or not etapa1_path.exists():
        return [], []
    content = etapa1_path.read_text(encoding="utf-8")
    pat = re.compile(r'#sigla\(\s*"([^"]+)"\s*,\s*\[([^\]]{1,200})\]', re.DOTALL)
    siglas = {}
    for m in pat.finditer(content):
        abbr = m.group(1).strip()
        expansao = m.group(2).strip()[:80]
        if abbr in siglas and siglas[abbr] != expansao:
            errors.append(f"  x sigla `{abbr}` aparece com 2 expansoes diferentes em {etapa1_path.name}")
        siglas[abbr] = expansao
    if siglas:
        print(f"  v siglas: {len(siglas)} unicas em #sigla(...)")
    return errors, warnings


def check_fonte(pdf_path: Path) -> tuple[list, list]:
    """Salvaguarda contra fallback de fonte.

    Sintoma real (caso #6+ pos-mortem de Carboidratos e Aminoacidos,
    2026-05-17): compilar sem `--font-path ../fonts` faz o Typst cair
    silenciosamente no LibertinusSerif, que tem x-height menor e
    glifos mais finos. Visual divergente do canonico.

    Canonico: corpo = Merriweather, titulos = Montserrat.
    Crimson Pro foi testada em 2026-05-19 e revertida na mesma sessão.

    Regra:
      - PDF DEVE conter pelo menos uma face Merriweather embarcada.
      - PDF NAO DEVE conter LibertinusSerif/LibertinusSans (fallback Typst).
      - Outros fallbacks (DejaVu, NewComputerModern) tambem bloqueiam.
    """
    errors, warnings = [], []
    try:
        out = subprocess.run(["pdffonts", str(pdf_path)],
                             capture_output=True, text=True, timeout=10)
    except FileNotFoundError:
        warnings.append("  ! pdffonts ausente (poppler-utils) -- checagem de fonte pulada")
        return errors, warnings
    except Exception as e:
        warnings.append(f"  ! pdffonts falhou: {e} -- checagem de fonte pulada")
        return errors, warnings

    saida = out.stdout
    # pdffonts imprime cabecalho + uma linha por fonte. Cada linha comeca
    # com o nome (com prefixo de subset tipo ABCDEF+CrimsonPro-Regular).
    fontes = set()
    for linha in saida.splitlines()[2:]:  # pula header e separador
        nome = linha.strip().split()
        if nome:
            # Tira prefixo de subset (6 chars + '+')
            n = nome[0]
            if len(n) > 7 and n[6] == "+":
                n = n[7:]
            fontes.add(n)

    if not fontes:
        warnings.append("  ! nenhuma fonte detectada no PDF (pdffonts vazio)")
        return errors, warnings

    # Canonico: Merriweather no corpo do texto.
    tem_merriweather = any("Merriweather" in f for f in fontes)

    if not tem_merriweather:
        nomes_fontes = ", ".join(sorted(fontes))
        errors.append(
            f"  x fonte: Merriweather ausente no PDF. Recompile com "
            f"`--font-path ../fonts`. Fontes encontradas: {nomes_fontes}. "
            f"BLOQUEAR."
        )
    else:
        # Sanity: Montserrat tambem deveria estar la
        tem_montserrat = any("Montserrat" in f for f in fontes)
        if not tem_montserrat:
            warnings.append("  ! Montserrat ausente -- titulos podem estar usando fallback")
        else:
            print(f"  v fonte: Merriweather + Montserrat embarcados ({len(fontes)} faces)")
    return errors, warnings


def check_palavras_e1(pdf_path: Path) -> tuple[list, list]:
    """B6 (canônico 2026-05-22): conta palavras do miolo da E1 e reporta
    se fora da faixa 3.500-5.000. NUNCA bloqueia -- só sinaliza.

    Miolo da E1 = intro-box + 3 PARTES + conclusão integradora.
    Delimitado pelo banner navy "Etapa 1" (início) e pelo banner gold
    "Resumindo" (fim, vem antes da E2). Capa, sumário, Resumindo, E2,
    E3 e Gabarito ficam fora da contagem.

    Faixa canônica 3.500-5.000 palavras: REDATOR-E1 §regra 2 (piso 2
    teto 20 páginas, sem meta rígida desde 2026-05-18). Esta contagem
    é só um aviso -- tema legítimamente complexo pode inflar.
    """
    errors, warnings = [], []
    n_pages = pdf_pages(pdf_path)
    if n_pages < 4:
        return errors, warnings
    texto_total = pdf_text(pdf_path, 1, n_pages)
    if not texto_total:
        return errors, warnings

    # Boundaries por string. "Etapa 1" e "Resumindo" aparecem como banner.
    # pdftotext quebra linhas, então busca tolerante.
    #
    # ERROS.md #21 (corrigido 2026-08-28): o fim do miolo NAO pode ancorar na
    # palavra "Resumindo" solta. O helper `#mini-resumo` do template imprime
    # SEMPRE a etiqueta "Resumindo ate aqui:" (nebli_v2_apostila.typ:254), de
    # modo que a primeira ocorrencia da palavra cai no PRIMEIRO mini-resumo da
    # E1 -- e a janela fechava na pagina 6 de um miolo de 22 paginas, em TODO
    # resumo que usa o helper (nao so quando o autor comecava a frase com ela).
    # O banner da pagina Resumindo, por ser um bloco de titulo, sai no texto
    # extraido como uma LINHA ISOLADA "Resumindo" -- e e nessa linha que se
    # ancora. Fallback continua sendo o banner da Etapa 2.
    upper = texto_total
    idx_e1 = upper.find("Etapa 1")
    idx_resumindo = -1
    if idx_e1 != -1:
        m_banner = re.search(r"^[ \t]*Resumindo[ \t]*$", upper[idx_e1:], re.MULTILINE)
        if m_banner:
            idx_resumindo = idx_e1 + m_banner.start()
        else:
            pos_e2 = upper.find("Etapa 2", idx_e1)
            idx_resumindo = pos_e2
    if idx_e1 == -1 or idx_resumindo == -1 or idx_resumindo <= idx_e1:
        warnings.append("  ! palavras E1: não consegui delimitar miolo (banner ausente)")
        return errors, warnings

    miolo = texto_total[idx_e1:idx_resumindo]
    palavras = [w for w in re.split(r"\s+", miolo) if w and any(c.isalpha() for c in w)]
    n = len(palavras)

    # Faixa recalibrada em 2026-09-03 com a queda do teto da E1 de 22 para
    # 15 paginas (CLAUDE.md § Registro cientifico). Uma E1 cheia entrega ~450
    # palavras por pagina impressa, legendas e footnotes inclusas, entao
    # 15 paginas ~ 6750 palavras; o teto de aviso fica em 7200 com folga.
    # Historico: 3500-5000 (ate 2026-08-28, E1 de ~12 paginas) ->
    # 3500-10500 (teto 22) -> 3000-7200 (teto 15).
    # Continua sendo aviso, nao bloqueio.
    PISO, TETO = 3000, 7200
    if PISO <= n <= TETO:
        print(f"  v palavras E1: {n} (faixa {PISO}-{TETO})")
    elif n < PISO:
        warnings.append(f"  ! palavras E1: {n} (esperado {PISO}-{TETO}). "
                        f"Miolo curto -- REDATOR pode ter sido raso ou tema é leve.")
    else:
        warnings.append(f"  ! palavras E1: {n} (esperado {PISO}-{TETO}). "
                        f"Miolo inflado -- conferir se REDATOR encheu linguiça.")
    return errors, warnings


def check_paginas_e1(pdf_path: Path) -> tuple[list, list]:
    """Conta as paginas ocupadas pela Etapa 1 e avisa acima do teto canonico.

    CANON 2026-09-03 (CLAUDE.md § Registro cientifico): o teto da E1 caiu de
    22 para 15 paginas. Ate aqui o item #7 do ERROS.md era 'manual' -- ninguem
    conferia, e as duas ultimas corridas fecharam em 18 e 25 paginas sem que
    nenhum auditor dissesse nada. Este check torna o teto auditavel.

    Delimitacao: pagina do banner 'Etapa 1' (o `etapa-header`, que aparece uma
    vez) ate a pagina anterior ao banner isolado 'Resumindo'. Mesma ancora do
    check_palavras_e1, so que contada em paginas em vez de palavras.

    Aviso, nao bloqueio -- coerente com a linha 7 da tabela de checks do
    ERROS.md e com a § Missao (ensinar bem pode vencer o teto, desde que a
    quebra va declarada no relatorio).
    """
    errors, warnings = [], []
    TETO = 15
    n_pages = pdf_pages(pdf_path)
    if n_pages < 4:
        return errors, warnings

    pag_e1 = pag_resumindo = None
    for i in range(1, n_pages + 1):
        txt = pdf_text(pdf_path, i, i)
        if not txt:
            continue
        if pag_e1 is None and re.search(r"^[ \t]*Etapa 1\b", txt, re.MULTILINE):
            pag_e1 = i
            continue
        if pag_e1 is not None and re.search(r"^[ \t]*Resumindo[ \t]*$", txt, re.MULTILINE):
            pag_resumindo = i
            break

    if pag_e1 is None or pag_resumindo is None or pag_resumindo <= pag_e1:
        warnings.append("  ! paginas E1: nao consegui delimitar (banner ausente) -- conferir a olho")
        return errors, warnings

    n = pag_resumindo - pag_e1
    if n <= TETO:
        print(f"  v paginas E1: {n} (teto {TETO})")
    else:
        warnings.append(
            f"  ! paginas E1: {n} paginas contra o teto canonico de {TETO} "
            f"(CLAUDE.md § Registro cientifico, 2026-09-03). Antes de aceitar o estouro, "
            f"aplicar as alavancas do ERROS.md F4 nesta ordem: (1) filtro das tres funcoes, "
            f"(2) fundir subtopicos irmaos ate 8-10, (3) max 2 boxes pesados por PARTE, "
            f"(4) figuras 50-55%. Se ainda assim estourar, declarar a quebra no relatorio.")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Auditoria do PDF compilado antes de mover")
    parser.add_argument("pdf", help="Caminho do PDF compilado")
    parser.add_argument("--etapa1", default=None, help="Caminho do etapa1.typ (para siglas)")
    parser.add_argument("--etapas-dir", default=None,
                        help="Pasta com etapa1/2/3/4.typ (para paths de figuras). "
                             "Default: pasta do PDF se nao em resumos-gerados/, senao typst-build/")
    parser.add_argument("--project-root", default=None,
                        help="Raiz do projeto NEBLI (default: pasta-mae de typst-build/)")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"x PDF nao encontrado: {pdf_path}", file=sys.stderr)
        sys.exit(4)

    project_root = Path(args.project_root) if args.project_root \
        else Path(__file__).resolve().parent.parent
    etapas_dir = Path(args.etapas_dir) if args.etapas_dir \
        else project_root / "typst-build"
    etapa1_path = Path(args.etapa1) if args.etapa1 else etapas_dir / "etapa1.typ"
    etapa_files = [etapas_dir / f for f in ["etapa1.typ", "etapa2.typ", "etapa3.typ", "etapa4.typ"]]

    print(f"=== NEBLI auditar_pdf -- {pdf_path.name} ===")
    print(f"Projeto: {project_root}")
    print(f"Etapas: {etapas_dir}")
    print()

    all_errors, all_warnings = [], []

    print("-> Acentuacao (3 amostras)")
    e, w = check_acentuacao(pdf_path)
    all_errors.extend(e); all_warnings.extend(w)
    for msg in e + w: print(msg)

    print("\n-> Paths de figuras")
    e, w = check_figuras_paths(etapa_files, project_root)
    all_errors.extend(e); all_warnings.extend(w)
    for msg in e + w: print(msg)

    print("\n-> Siglas duplicadas em etapa1")
    e, w = check_siglas_duplicadas(etapa1_path)
    all_errors.extend(e); all_warnings.extend(w)
    for msg in e + w: print(msg)

    print("\n-> Fonte embarcada (Merriweather + Montserrat)")
    e, w = check_fonte(pdf_path)
    all_errors.extend(e); all_warnings.extend(w)
    for msg in e + w: print(msg)

    print("\n-> Paginas da E1 (aviso, não bloqueia)")
    e, w = check_paginas_e1(pdf_path)
    all_errors.extend(e); all_warnings.extend(w)
    for msg in e + w: print(msg)

    print("\n-> Palavras da E1 (aviso, não bloqueia)")
    e, w = check_palavras_e1(pdf_path)
    all_errors.extend(e); all_warnings.extend(w)
    for msg in e + w: print(msg)

    print()
    print(f"Resumo: {len(all_errors)} erro(s), {len(all_warnings)} warning(s)")
    if all_errors:
        print("\nx FALHA -- NAO MOVER PDF. Corrija antes.")
        if any("acentos" in e for e in all_errors):
            sys.exit(1)
        if any("figura" in e for e in all_errors):
            sys.exit(2)
        if any("sigla" in e for e in all_errors):
            sys.exit(3)
        if any("fonte" in e for e in all_errors):
            sys.exit(5)
        sys.exit(1)
    print("\nv OK -- pode mover PDF para resumos-gerados/.")
    sys.exit(0)


if __name__ == "__main__":
    main()
