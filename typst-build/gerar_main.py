#!/usr/bin/env python3
"""
NEBLI -- gerar_main.py
Gera typst-build/main.typ a partir de um Tema Card YAML + os etapaN.typ.

Frente C3 do plano de economia (2026-05-16):
  O COMPILADOR hoje escreve main.typ a mao a cada resumo
  (~10-15k tokens). Script torna a montagem deterministica
  e elimina erro de transcricao (#4 saiu com "Davi Sousa --
  Turma 114" no rodape porque o COMPILADOR copiou rodape antigo).

Input -- Tema Card YAML:
  slug: acidos-nucleicos
  titulo: "Estrutura dos ácidos nucleicos"
  subtitulo: "Biologia Molecular · UC01 · Aula 32"
  meta:  # canonico 2026-05-26: "Nota de uso" REMOVIDA
    - ["Disciplina", "Biologia Molecular (UC01)"]
    - ["Onde estudar", "Alberts Cap. 4 + Cap. 6..."]
  sumario:
    - titulo: "Etapa 1 — Texto didático"
      blocos:
        - titulo: "PARTE I — As peças"
          subtopicos:
            - "1.1 Bases nitrogenadas"
            - "1.2 Açúcar pentose"
            - "1.3 Fosfato e ligação N-glicosídica"
        - titulo: "PARTE II — A montagem"
          subtopicos: [...]
  gabarito:
    consolidacao:  # Q01-Q10
      - ["01", "C"]
      - ["02", "CEEC"]
      ...
    integracao:    # Q11-Q25
      ...
    aplicacao:     # Q26-Q30
      ...

Uso:
  python3 typst-build/gerar_main.py TEMA_CARD.yml
  python3 typst-build/gerar_main.py TEMA_CARD.yml --out typst-build/main.typ
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def _esc_typst_str(s: str) -> str:
    """Escapa string para uso em string Typst (entre aspas)."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def _esc_typst_content(s: str) -> str:
    """Escapa string para uso em MODO CONTEÚDO Typst, preservando `*` (negrito).

    Usado nos itens do bloco "Onde aprofundar" (capa), que misturam `*rótulo*`
    em negrito com caminhos de tag do AnKing cheios de `#` e `_` (que o Typst
    leria como código/ênfase). Escapa os caracteres perigosos um a um; `*` fica
    intacto para o negrito funcionar.
    """
    especiais = set('#_$@<>`\\~[]')
    return "".join("\\" + ch if ch in especiais else ch for ch in s)


def _quebrar_tags_longas(s: str) -> str:
    """Insere pontos de quebra invisiveis (U+200B) nas tags AnKing longas.

    Os caminhos de tag (`#FirstAid::12_Neurology::...::01_Cells_of_the_nervous_system`)
    sao um unico token sem espacos -- o Typst nao consegue quebra-lo e ele
    transborda a margem direita da capa. Inserindo zero-width-space depois de
    cada `::` e de cada `_`, o Typst passa a poder quebrar nesses limites
    naturais da tag, sem mudar o texto visivel nem a busca no Anki Browse.
    Aplicado so aos itens do bloco "Onde aprofundar" (valor em lista).
    """
    zwsp = "​"
    return s.replace("::", "::" + zwsp).replace("_", "_" + zwsp)


def render_capa(titulo, subtitulo, meta):
    lines = [f'#capa(']
    lines.append(f'  "{_esc_typst_str(titulo)}",')
    lines.append(f'  "{_esc_typst_str(subtitulo)}",')
    lines.append(f'  (')
    for rotulo, valor in meta:
        # canonico 2026-07-07: bloco "Onde aprofundar" REMOVIDO da capa a pedido
        # do Davi (2x). Filtra aqui qualquer linha meta cujo rotulo mencione
        # "aprofundar" -- garante que nao renderiza em resumo novo mesmo que o
        # Tema Card ainda a traga. Ver MEMORY.md § Pendencias / Historico.
        if "aprofund" in str(rotulo).lower():
            continue
        if isinstance(valor, (list, tuple)):
            # Bloco em topicos (ex.: "Onde aprofundar" -- plataformas AnKing/
            # UWorld/B&B/Sketchy/Pathoma). Cada item vira um bullet navy numa
            # linha. Itens sao conteudo Typst cru: negrito *...* eh permitido,
            # o autor do cache (referencias-externas/onde-aprofundar.md) controla.
            lines.append(f'    ("{_esc_typst_str(rotulo)}", [')
            lines.append('      #set text(size: 7.3pt)')
            lines.append('      #set par(leading: 0.55em, justify: false, first-line-indent: 0em, hanging-indent: 0.9em)')
            n = len(valor)
            for i, item in enumerate(valor):
                quebra = ' \\' if i < n - 1 else ''
                lines.append(f'      #text(fill: navy, weight: "bold", "• ") {_esc_typst_content(_quebrar_tags_longas(item))}{quebra}')
            lines.append('    ]),')
        else:
            lines.append(f'    ("{_esc_typst_str(rotulo)}", "{_esc_typst_str(valor)}"),')
    lines.append(f'  ),')
    lines.append(f')')
    return "\n".join(lines)


def render_sumario(estrutura):
    lines = ["#sumario(("]
    for etapa in estrutura:
        titulo = etapa.get("titulo", "")
        blocos = etapa.get("blocos", [])
        lines.append(f'  ("{_esc_typst_str(titulo)}", (')
        if not blocos:
            lines.append(f'    (none, (')
            for desc in etapa.get("descricoes", []):
                lines.append(f'      "{_esc_typst_str(desc)}",')
            lines.append(f'    )),')
        else:
            for bloco in blocos:
                btit = bloco.get("titulo")
                subs = bloco.get("subtopicos", [])
                btit_str = f'"{_esc_typst_str(btit)}"' if btit else "none"
                lines.append(f'    ({btit_str}, (')
                for s in subs:
                    lines.append(f'      "{_esc_typst_str(s)}",')
                lines.append(f'    )),')
        lines.append(f'  )),')
    lines.append("))")
    return "\n".join(lines)


def render_gabarito(gabarito):
    """gabarito = {consolidacao: [...], integracao: [...], aplicacao: [...]}"""
    blocos = [
        ("Consolidação (Q01–Q10)", gabarito.get("consolidacao", [])),
        ("Integração (Q11–Q25)", gabarito.get("integracao", [])),
        ("Aplicação (Q26–Q30)", gabarito.get("aplicacao", [])),
    ]
    lines = ["#gabarito-page(("]
    for titulo, items in blocos:
        lines.append(f'  ("{_esc_typst_str(titulo)}", (')
        for num, letra in items:
            lines.append(f'    ("{_esc_typst_str(str(num))}", "{_esc_typst_str(str(letra))}"),')
        lines.append(f'  )),')
    lines.append("))")
    return "\n".join(lines)


HEADER = '''// ================================================================
// MAIN.TYP -- {slug} | Gerado por gerar_main.py
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
{capa}

// ======= SUMÁRIO =======
{sumario}

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"

// ======= ETAPA 2 =======
#set-etapa("Etapa 2 — 30 objetivas")
#pagebreak()
#etapa-header("Etapa 2 — 30 objetivas")
#include "etapa2.typ"

// ======= ETAPA 3 =======
#set-etapa("Etapa 3 — 5 discursivas")
#pagebreak()
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"

// ======= GABARITO CONSOLIDADO (Etapa 2) =======
{gabarito}
'''

HEADER_SEM_E2 = '''// ================================================================
// MAIN.TYP -- {slug} | Gerado por gerar_main.py (modo sem_e2)
// ================================================================

#import "../typst-template/nebli_v2_apostila.typ": *

#show: pagina-padrao

// ======= CAPA =======
{capa}

// ======= SUMÁRIO =======
{sumario}

// ======= ETAPA 1 =======
#etapa-header("Etapa 1 — Texto didático")
#include "etapa1.typ"

// ======= RESUMINDO =======
#include "resumindo.typ"

// ======= ETAPA 3 =======
#etapa-header("Etapa 3 — 5 discursivas")
#include "etapa3.typ"
'''


def gerar_main(card_path: Path, out_path: Path):
    if yaml is None:
        print("x PyYAML nao instalado. Rode: pip install pyyaml --break-system-packages",
              file=sys.stderr)
        sys.exit(1)
    if not card_path.exists():
        print(f"x Tema Card nao encontrado: {card_path}", file=sys.stderr)
        sys.exit(1)
    card = yaml.safe_load(card_path.read_text(encoding="utf-8"))

    slug = card.get("slug", "?")
    titulo = card.get("titulo", "")
    subtitulo = card.get("subtitulo", "")
    meta = card.get("meta", [])
    sumario = card.get("sumario", [])
    gabarito = card.get("gabarito", {})

    capa_text = render_capa(titulo, subtitulo, meta)
    sumario_text = render_sumario(sumario)
    sem_e2 = bool(card.get("sem_e2", False))

    if sem_e2:
        text = HEADER_SEM_E2.format(
            slug=slug,
            capa=capa_text,
            sumario=sumario_text,
        )
    else:
        gabarito_text = render_gabarito(gabarito)
        text = HEADER.format(
            slug=slug,
            capa=capa_text,
            sumario=sumario_text,
            gabarito=gabarito_text,
        )
    out_path.write_text(text, encoding="utf-8")
    return len(text)


def main():
    parser = argparse.ArgumentParser(description="Gera main.typ a partir de Tema Card YAML")
    parser.add_argument("card", help="Caminho do Tema Card YAML")
    parser.add_argument("--out", default=None, help="Saida (default: typst-build/main.typ)")
    args = parser.parse_args()

    card_path = Path(args.card)
    out_path = Path(args.out) if args.out else Path(__file__).resolve().parent / "main.typ"

    n = gerar_main(card_path, out_path)
    print(f"v {n} chars escritos em {out_path}")


if __name__ == "__main__":
    main()
