#!/usr/bin/env python3
"""
NEBLI -- auditar_pdf_visual.py
Camada visual da auditoria de PDF (complementa o auditar_pdf.py textual).

Motivação:
  5 dos 6 primeiros resumos da G20 tiveram bugs visuais pegos depois da
  compilação: Resumindo passando de 2 paginas, header dessincronizado na
  transicao Resumindo->E2 (Liga TCP), paginas com mancha < 40%, categorias
  E2 sem cor (uma virou cinza por engano em sessao antiga). Custo: ~1-3h de
  retrabalho por resumo. Este script bloqueia esses casos antes de mover o PDF.

Validacoes:
  1. **Resumindo cabe em 1-2 paginas**. Erro se > 2.
  2. **Sumario em 1 pagina**. Warn se > 1.
  3. **Paginas em branco** (mancha < threshold). Warn lista paginas suspeitas.
  4. **Header sincronizado**. Erro se primeira pagina apos pagebreak de secao
     ainda mostra header da secao anterior.
  5. **Cores E2 presentes** (proxy textual via etapa2.typ): conferir que os
     tres helpers #prova-consolidacao, #prova-integracao, #prova-aplicacao
     estao sendo usados. Warn se faltar algum.
  6. **Figuras sem cortes**: nao da pra checar via texto. Imprime INFO
     pedindo conferencia manual.

Uso:
  python3 typst-build/auditar_pdf_visual.py PDF [--etapa2 etapa2.typ]
  python3 typst-build/auditar_pdf_visual.py resumos-gerados/GLICONEOGENESE.pdf \\
      --etapa2 typst-build/etapa2.typ

Exit codes:
  0 = ok (sem ERROR; pode mover PDF)
  1 = ERROR (bloqueia movimentacao)
  2 = pdftotext ausente ou PDF nao encontrado
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path


# Limiares
LIMIAR_MANCHA_BAIXA = 350   # caracteres por pagina; abaixo disso = suspeita branco
LIMIAR_PAGINA_NORMAL = 1500 # acima disso = pagina cheia, ignorada para "branco"

# Markers de secao no header (Typst injeta esses textos nas headers configurados)
MARKERS_SECAO = {
    "sumario": ["Sumário", "Sumario"],
    "etapa1": ["Etapa 1", "ETAPA 1"],
    "resumindo": ["Resumindo", "RESUMINDO"],
    "etapa2": ["Etapa 2", "ETAPA 2"],
    "etapa3": ["Etapa 3", "ETAPA 3"],
    "gabarito": ["Gabarito"],
}


class Validacao:
    def __init__(self):
        self.errors: list[str] = []
        self.warns: list[str] = []
        self.infos: list[str] = []
        self.ok: list[str] = []


def pdf_num_pages(pdf: Path) -> int:
    try:
        out = subprocess.run(
            ["pdfinfo", str(pdf)], capture_output=True, text=True, timeout=10
        )
        for line in out.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except Exception:
        pass
    return 0


def pdf_text_per_page(pdf: Path) -> list[str]:
    """Retorna lista com texto de cada pagina (1-indexed na intencao,
    0-indexed no retorno)."""
    n = pdf_num_pages(pdf)
    if n == 0:
        return []
    paginas = []
    for i in range(1, n + 1):
        try:
            out = subprocess.run(
                ["pdftotext", "-f", str(i), "-l", str(i), str(pdf), "-"],
                capture_output=True, text=True, timeout=15,
            )
            paginas.append(out.stdout)
        except FileNotFoundError:
            print("x pdftotext nao encontrado. Instale poppler-utils.", file=sys.stderr)
            sys.exit(2)
        except Exception as e:
            print(f"! pagina {i}: pdftotext falhou ({e})", file=sys.stderr)
            paginas.append("")
    return paginas


def classificar_pagina_por_header(texto: str) -> str | None:
    """Tenta identificar a qual secao a pagina pertence olhando o header
    (primeiras ~5 linhas, onde fica o cabecalho rodando)."""
    cabeca = "\n".join(texto.splitlines()[:6])
    for secao, marcadores in MARKERS_SECAO.items():
        for m in marcadores:
            if m in cabeca:
                return secao
    return None


def classificar_pagina_por_conteudo(texto: str) -> str | None:
    """Fallback: olha o corpo da pagina para inferir a secao."""
    for secao, marcadores in MARKERS_SECAO.items():
        for m in marcadores:
            if m in texto:
                return secao
    return None


def validar_resumindo(paginas: list[str], v: Validacao) -> None:
    """Resumindo deve caber em 1 ou 2 paginas (canonico 2026-05-20)."""
    paginas_resumindo = []
    for i, p in enumerate(paginas, 1):
        # marcador no header indica que estamos NA secao Resumindo
        cabeca = "\n".join(p.splitlines()[:4])
        if "Resumindo" in cabeca and not any(
            outro in cabeca for outro in ["Etapa 2", "Etapa 3", "Gabarito"]
        ):
            paginas_resumindo.append(i)

    if not paginas_resumindo:
        v.warns.append(
            "Resumindo nao detectado em nenhum header de pagina. "
            "Confirmar visualmente que existe e tem header configurado."
        )
        return

    n = len(paginas_resumindo)
    if n > 2:
        v.errors.append(
            f"Resumindo ocupa {n} paginas (paginas {paginas_resumindo}); "
            f"canonico maximo: 2. Comprimir conteudo ou rever spacing/leading."
        )
    elif n == 2:
        v.ok.append(f"Resumindo em 2 paginas (aceitavel — tema denso)")
    else:
        v.ok.append(f"Resumindo em 1 pagina (ideal)")


def validar_sumario(paginas: list[str], v: Validacao) -> None:
    """Sumario deve caber em 1 pagina (CLAUDE.md > Ordem do PDF item 2)."""
    paginas_sumario = []
    for i, p in enumerate(paginas, 1):
        cabeca = "\n".join(p.splitlines()[:4])
        if any(m in cabeca for m in MARKERS_SECAO["sumario"]):
            paginas_sumario.append(i)

    if len(paginas_sumario) > 1:
        v.warns.append(
            f"Sumario ocupa {len(paginas_sumario)} paginas (paginas {paginas_sumario}); "
            f"canonico: 1. Reduzir subitens ou compactar descricoes."
        )
    elif paginas_sumario:
        v.ok.append("Sumario em 1 pagina")


def validar_paginas_em_branco(paginas: list[str], v: Validacao) -> None:
    """Lista paginas com mancha < 40% (proxy: poucos caracteres)."""
    suspeitas = []
    for i, p in enumerate(paginas, 1):
        # ignorar header/footer ao contar (4 linhas no topo + 2 no fim)
        linhas = p.splitlines()
        if len(linhas) > 6:
            miolo = "\n".join(linhas[4:-2])
        else:
            miolo = p
        n_chars = len(miolo.strip())
        if n_chars < LIMIAR_MANCHA_BAIXA:
            suspeitas.append((i, n_chars))

    if suspeitas:
        # Paginas de transicao de secao (uma so com banner) sao OK
        # Filtramos as que tem APENAS marker de secao + nada
        suspeitas_reais = []
        for i, n_chars in suspeitas:
            p = paginas[i - 1]
            # se pagina tem so o banner de secao (ETAPA X) + 1-2 linhas, ok
            if re.search(r"ETAPA [123]\b", p):
                continue
            suspeitas_reais.append((i, n_chars))

        if suspeitas_reais:
            lista = ", ".join(f"p{i} ({n}c)" for i, n in suspeitas_reais[:6])
            v.warns.append(
                f"{len(suspeitas_reais)} pagina(s) com mancha baixa: {lista}. "
                f"Conferir visualmente se sao paginas legitimas (ultima de uma secao) "
                f"ou bug de quebra forcada."
            )
        else:
            v.ok.append(f"sem paginas em branco anomalas")
    else:
        v.ok.append("sem paginas com mancha baixa")


def validar_header_sincronizado(paginas: list[str], v: Validacao) -> None:
    """
    Detecta o bug do Liga TCP: primeira pagina apos uma transicao de secao
    ainda mostra o header da secao anterior.

    Heuristica: olha cada transicao (header muda entre pagina i e i+1).
    Se a pagina i+1 tem CONTEUDO da nova secao mas HEADER da secao antiga,
    sinaliza ERRO.
    """
    # propagar ultimo header conhecido para paginas onde marcador some
    # (ex: paginas internas do gabarito que herdam header da etapa3)
    headers_brutos = [classificar_pagina_por_header(p) for p in paginas]
    headers = []
    ultimo = None
    for h in headers_brutos:
        if h is not None:
            ultimo = h
        headers.append(ultimo)

    erros = []
    avisos = []

    # Transicoes onde herdar header da secao anterior eh design conhecido,
    # nao bug. Sinalizamos como WARN (nao ERROR) para nao bloquear PDFs
    # que ja foram aceitos historicamente com esse comportamento.
    TRANSICOES_TOLERADAS = {
        ("etapa1", "resumindo"),   # Resumindo cola na E1
        ("etapa3", "gabarito"),    # Gabarito vem direto apos E3, sem header proprio
        ("etapa2", "gabarito"),    # caso pos-E4-removida, Gabarito apos E2
    }

    for i in range(1, len(paginas)):
        h_atual = headers[i]
        h_anterior = headers[i - 1]

        # foco: paginas sem header identificado (None) sao suspeitas se
        # tiverem conteudo claro de uma secao no corpo
        if h_atual is None:
            corpo_secao = classificar_pagina_por_conteudo(paginas[i])
            if corpo_secao and corpo_secao != h_anterior:
                msg = (
                    f"pagina {i+1}: header nao identificado mas conteudo bate "
                    f"com '{corpo_secao}'"
                )
                if (h_anterior, corpo_secao) in TRANSICOES_TOLERADAS:
                    avisos.append(msg + " (transicao tolerada — design ou bug aceito)")
                else:
                    erros.append(msg + " (bug header desincronizado?)")
            continue

        # caso classico: header mudou entre paginas. Tudo bem.
        # caso suspeito: pagina i+1 tem header da secao anterior mas conteudo da nova.
        if h_atual == h_anterior:
            linhas = paginas[i].splitlines()
            miolo = "\n".join(linhas[3:])
            for nova_secao, marcadores in MARKERS_SECAO.items():
                if nova_secao == h_atual:
                    continue
                for m in marcadores:
                    if m in miolo and m not in "\n".join(linhas[:3]):
                        msg = (
                            f"pagina {i+1}: header continua '{h_atual}' mas "
                            f"banner de '{nova_secao}' aparece no corpo"
                        )
                        if (h_atual, nova_secao) in TRANSICOES_TOLERADAS:
                            avisos.append(msg + " (transicao tolerada)")
                        else:
                            erros.append(msg + " (BUG header dessincronizado — fix em `set-etapa`)")
                        break

    if erros:
        for e in erros[:3]:
            v.errors.append(e)
        if len(erros) > 3:
            v.errors.append(f"... e mais {len(erros)-3} casos.")
    if avisos:
        for a in avisos[:3]:
            v.warns.append(a)
        if len(avisos) > 3:
            v.warns.append(f"... e mais {len(avisos)-3} transicoes toleradas.")
    if not erros and not avisos:
        v.ok.append("headers sincronizados em todas as transicoes de secao")


def validar_cores_e2_no_source(etapa2_path: Path | None, v: Validacao) -> None:
    """Verifica que os 3 helpers de cor da E2 estao presentes no source."""
    if etapa2_path is None:
        v.infos.append(
            "etapa2.typ nao fornecido (--etapa2); pulando checagem de cores E2"
        )
        return
    if not etapa2_path.exists():
        v.warns.append(f"etapa2.typ nao encontrado em {etapa2_path}")
        return

    texto = etapa2_path.read_text(encoding="utf-8")
    helpers = {
        "Consolidacao": "#prova-consolidacao",
        "Integracao": "#prova-integracao",
        "Aplicacao": "#prova-aplicacao",
    }
    faltando = [nome for nome, h in helpers.items() if h not in texto]
    if faltando:
        v.warns.append(
            f"helpers de cor faltando em etapa2.typ: {faltando}. "
            f"Categoria(s) renderizando sem cor distintiva."
        )
    else:
        v.ok.append("3 helpers de cor da E2 presentes (#prova-consolidacao/integracao/aplicacao)")


def info_figuras_cortadas(v: Validacao) -> None:
    """Sinaliza que figuras precisam de conferencia visual humana."""
    v.infos.append(
        "Figuras sem cortes nas margens: validacao visual humana obrigatoria. "
        "Abra o PDF e folheie as paginas de E1 conferindo se nenhuma figura "
        "esta cortada (especialmente as com `largura: 85%` e `figura-lateral`)."
    )


def imprimir_relatorio(pdf: Path, v: Validacao) -> None:
    print(f"\n=== auditoria visual: {pdf.name} ===\n")
    if v.ok:
        print(f"v {len(v.ok)} verificacoes OK:")
        for o in v.ok:
            print(f"  v {o}")
    if v.infos:
        print(f"\ni {len(v.infos)} INFO (conferencia humana):")
        for inf in v.infos:
            print(f"  i {inf}")
    if v.warns:
        print(f"\n! {len(v.warns)} WARN (sinalizacao):")
        for w in v.warns:
            print(f"  - {w}")
    if v.errors:
        print(f"\nx {len(v.errors)} ERROR (bloqueia movimentacao):")
        for e in v.errors:
            print(f"  - {e}")
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", help="Caminho para o PDF a auditar")
    parser.add_argument("--etapa2", help="Caminho para etapa2.typ (para checar cores)")
    args = parser.parse_args()

    pdf = Path(args.pdf)
    if not pdf.exists():
        print(f"x PDF nao encontrado: {pdf}", file=sys.stderr)
        sys.exit(2)

    etapa2 = Path(args.etapa2) if args.etapa2 else None

    paginas = pdf_text_per_page(pdf)
    if not paginas:
        print(f"x nao consegui extrair texto do PDF (pdftotext ausente?)", file=sys.stderr)
        sys.exit(2)

    v = Validacao()
    validar_resumindo(paginas, v)
    validar_sumario(paginas, v)
    validar_paginas_em_branco(paginas, v)
    validar_header_sincronizado(paginas, v)
    validar_cores_e2_no_source(etapa2, v)
    info_figuras_cortadas(v)

    imprimir_relatorio(pdf, v)

    if v.errors:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
