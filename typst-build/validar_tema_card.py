#!/usr/bin/env python3
"""
NEBLI -- validar_tema_card.py
Validação de Tema Card YAML antes de delegar redação ao REDATOR/QUESTIONADOR.

Motivação:
  Tema Card com slug errado, soma de gabaritos quebrada, balanceamento óbvio
  de letras ou menção a "P1/P2" no enunciado custa retrabalho da E2 inteira
  (~30-45 min). Este validador pega esses casos em ~2 segundos.

Categorias:
  ERROR  -- bloqueia delegação (rodar redator com isso = retrabalho garantido)
  WARN   -- sinaliza problema; redator pode prosseguir, orquestrador decide

Uso:
  python3 typst-build/validar_tema_card.py arquivos-trabalho/tema_card_gliconeogenese.yml

Exit codes:
  0 = sem ERROR (pode delegar; WARN reportados mas não bloqueiam)
  1 = ERROR detectado (não delegar até consertar)
  2 = arquivo não encontrado ou YAML inválido
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    print("x PyYAML nao instalado. Rodar: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parent.parent
AULAS_UC01 = ROOT / "banco" / "aulas_uc01.yml"
AULAS_UC02 = ROOT / "banco" / "aulas_uc02.yml"

# Distribuição esperada por profundidade (CLAUDE.md > Tema Card > Seção C)
DISTRIBUICAO = {
    "SUPERFICIAL": {"cons": (12, 13), "int": (12, 13), "apl": (5, 5)},
    "PADRAO": {"cons": (10, 10), "int": (15, 15), "apl": (5, 5)},
    "PROFUNDO": {"cons": (8, 8), "int": (17, 17), "apl": (5, 5)},
}

# Letras válidas de gabarito MC + padrões C/E
RE_GAB_MC = re.compile(r"^[A-E]$")
RE_GAB_CE = re.compile(r"^[CE]{2,5}$")

# Proibições absolutas no PDF (CLAUDE.md > Capa)
RE_PROVA = re.compile(r"\b(P[1-4]|prova\s*[1-4])\b", re.IGNORECASE)
RE_NUM_AULA = re.compile(r"\baula\s+\d+\s*(de|/)\s*\d+\b", re.IGNORECASE)


class Validacao:
    def __init__(self):
        self.errors: list[str] = []
        self.warns: list[str] = []
        self.ok: list[str] = []

    def err(self, msg): self.errors.append(msg)
    def warn(self, msg): self.warns.append(msg)
    def passou(self, msg): self.ok.append(msg)


def carregar_slugs_validos() -> set[str]:
    slugs = set()
    for p in [AULAS_UC01, AULAS_UC02]:
        if p.exists():
            with open(p, encoding="utf-8") as f:
                d = yaml.safe_load(f)
            for a in d.get("aulas", []):
                slugs.add(a["slug"])
    return slugs


def validar_seccao_a(card: dict, slugs_validos: set[str], v: Validacao) -> None:
    """Seção A: identidade do resumo."""
    # slug
    slug = card.get("slug")
    if not slug:
        v.err("falta campo `slug` no Tema Card")
    elif slug not in slugs_validos:
        v.err(f"slug '{slug}' nao existe em aulas_uc01.yml ou aulas_uc02.yml")
    else:
        v.passou(f"slug '{slug}' valido")

    # titulo
    if not card.get("titulo"):
        v.err("falta campo `titulo`")
    else:
        v.passou(f"titulo: '{card['titulo']}'")

    # meta — Disciplina + Onde estudar (canonico 2026-05-26: "Nota de uso" REMOVIDA)
    meta = card.get("meta", [])
    if not meta:
        v.err("falta secao `meta` (Disciplina, Onde estudar)")
        return

    meta_dict = {}
    for item in meta:
        if isinstance(item, list) and len(item) == 2:
            meta_dict[item[0]] = item[1]

    obrigatorios = ["Disciplina", "Onde estudar"]
    for campo in obrigatorios:
        if campo not in meta_dict:
            v.err(f"falta `meta.{campo}`")
        else:
            v.passou(f"meta.{campo} presente")

    # Aviso se "Nota de uso" foi declarada por engano (canonico 2026-05-26: removida)
    if "Nota de uso" in meta_dict:
        v.warn(
            "campo `Nota de uso` foi removido do bloco meta em 2026-05-26 "
            "(canonico atual: Disciplina + Onde estudar apenas). Remover do tema-card."
        )

    # Proibições no titulo/subtitulo/meta
    texto_publico = " ".join([
        str(card.get("titulo", "")),
        str(card.get("subtitulo", "")),
        " ".join(str(v) for v in meta_dict.values()),
    ])
    if RE_PROVA.search(texto_publico):
        v.err(
            f"menção a P1/P2/P3/P4 detectada no Tema Card publico — "
            f"PROIBIDO no PDF (CLAUDE.md > Capa)"
        )
    if RE_NUM_AULA.search(texto_publico):
        v.err(f"menção a 'aula N de M' detectada — PROIBIDO no PDF")


def validar_seccao_b(card: dict, v: Validacao) -> None:
    """Seção B: esqueleto E1 com 3 PARTES."""
    sumario = card.get("sumario", [])
    if not sumario:
        v.err("falta `sumario` (esqueleto da E1)")
        return

    # Encontrar bloco da Etapa 1
    e1 = None
    for s in sumario:
        if isinstance(s, dict) and "etapa 1" in str(s.get("titulo", "")).lower():
            e1 = s
            break

    if e1 is None:
        v.warn("nao consegui localizar Etapa 1 no sumario (titulo nao bate 'Etapa 1')")
        return

    partes = e1.get("blocos", [])
    if len(partes) != 3:
        v.warn(f"Etapa 1 tem {len(partes)} PARTES (canonico: 3)")
    else:
        v.passou(f"Etapa 1 com 3 PARTES")

    for i, parte in enumerate(partes, 1):
        if not isinstance(parte, dict):
            continue
        subs = parte.get("subtopicos", [])
        titulo_parte = parte.get("titulo", f"PARTE {i}")
        if len(subs) < 2:
            v.warn(
                f"{titulo_parte}: {len(subs)} subtopicos "
                f"(recomendado: 3-4 para densidade adequada)"
            )
        elif len(subs) > 5:
            v.warn(
                f"{titulo_parte}: {len(subs)} subtopicos "
                f"(muitos — risco de E1 inchada; considere agrupar)"
            )
        else:
            v.passou(f"{titulo_parte}: {len(subs)} subtopicos")


def validar_seccao_c(card: dict, v: Validacao) -> None:
    """Seção C: distribuição e gabaritos da E2."""
    gab = card.get("gabarito", {})
    if not gab:
        v.err("falta `gabarito` (sequencia dos 30 gabaritos da E2)")
        return

    cons = gab.get("consolidacao", [])
    intg = gab.get("integracao", [])
    apl = gab.get("aplicacao", [])

    n_cons, n_int, n_apl = len(cons), len(intg), len(apl)
    total = n_cons + n_int + n_apl

    if total != 30:
        v.err(
            f"soma de gabaritos = {total} (cons={n_cons} + int={n_int} + apl={n_apl}); "
            f"esperado 30"
        )
    else:
        v.passou(f"30 gabaritos distribuidos: {n_cons} Cons + {n_int} Int + {n_apl} Apl")

    # casa com alguma profundidade canônica?
    perfil_detectado = None
    for nome, faixas in DISTRIBUICAO.items():
        c_min, c_max = faixas["cons"]
        i_min, i_max = faixas["int"]
        a_min, a_max = faixas["apl"]
        if (c_min <= n_cons <= c_max) and (i_min <= n_int <= i_max) and (a_min <= n_apl <= a_max):
            perfil_detectado = nome
            break

    if perfil_detectado:
        v.passou(f"distribuicao bate com perfil {perfil_detectado}")
    elif total == 30:
        v.warn(
            f"distribuicao {n_cons}/{n_int}/{n_apl} nao bate com SUPERFICIAL/PADRAO/PROFUNDO — "
            f"declare a parametrizacao no Tema Card se for intencional"
        )

    # gabaritos válidos
    todos = [g for grupo in (cons, intg, apl) for g in grupo]
    invalidos = []
    letras_mc = []
    for item in todos:
        if not isinstance(item, list) or len(item) < 2:
            invalidos.append(str(item))
            continue
        qnum, resp = item[0], str(item[1])
        if RE_GAB_MC.match(resp):
            letras_mc.append(resp)
        elif RE_GAB_CE.match(resp):
            pass  # C/E ok
        else:
            invalidos.append(f"Q{qnum}={resp}")

    if invalidos:
        v.err(f"gabaritos invalidos: {invalidos[:5]}")

    # balanceamento óbvio de letras (sorteio nao pode parecer manual)
    if len(letras_mc) >= 10:
        cnt = Counter(letras_mc)
        n = len(letras_mc)
        maior = max(cnt.values())
        menor = min(cnt.values()) if len(cnt) == 5 else 0

        # Se TODAS as 5 letras aparecem em quantidade quase igual (diff <=1),
        # cheira a balanceamento manual
        if len(cnt) == 5 and (maior - menor) <= 1:
            v.warn(
                f"distribuicao de letras MC muito uniforme ({dict(cnt)}) — "
                f"sorteio independente nao gera isso quase nunca. Conferir se foi balanceado manualmente."
            )
        # Se uma letra concentra >40%, sorteio improvavel mas valido
        elif maior / n > 0.40:
            v.warn(
                f"letra '{cnt.most_common(1)[0][0]}' concentra {100*maior/n:.0f}% das MC "
                f"({maior}/{n}) — possivel mas suspeito. Conferir se sorteio foi feito."
            )
        else:
            v.passou(f"distribuicao MC plausivelmente aleatoria: {dict(cnt)}")


def validar_e4_ausente(card: dict, v: Validacao) -> None:
    """E4 foi removida do pipeline em 2026-05-22 (CHANGELOG > P30)."""
    sumario = card.get("sumario", [])
    for s in sumario:
        if isinstance(s, dict):
            titulo = str(s.get("titulo", "")).lower()
            if "etapa 4" in titulo or "fundamentos" in titulo:
                v.warn(
                    "Tema Card menciona Etapa 4/fundamentos — E4 foi removida do "
                    "pipeline em 2026-05-22. Remova essa entrada do sumario antes "
                    "de delegar para o REDATOR."
                )
                return
    v.passou("sem mencao a Etapa 4 (canonico pos 2026-05-22)")


def imprimir_relatorio(card_path: Path, v: Validacao) -> None:
    print(f"\n=== validacao do Tema Card: {card_path.name} ===\n")
    if v.ok:
        print(f"v {len(v.ok)} verificacoes OK")
    if v.warns:
        print(f"\n! {len(v.warns)} WARN (sinalizacao, nao bloqueia):")
        for w in v.warns:
            print(f"  - {w}")
    if v.errors:
        print(f"\nx {len(v.errors)} ERROR (bloqueia delegacao):")
        for e in v.errors:
            print(f"  - {e}")
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tema_card", help="Caminho para o Tema Card YAML")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="lista tambem as verificacoes OK")
    args = parser.parse_args()

    path = Path(args.tema_card)
    if not path.exists():
        print(f"x arquivo nao encontrado: {path}", file=sys.stderr)
        sys.exit(2)

    try:
        with open(path, encoding="utf-8") as f:
            card = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"x YAML invalido: {e}", file=sys.stderr)
        sys.exit(2)

    if not isinstance(card, dict):
        print(f"x Tema Card deve ser dict no topo, recebi {type(card).__name__}", file=sys.stderr)
        sys.exit(2)

    slugs_validos = carregar_slugs_validos()

    val = Validacao()
    validar_seccao_a(card, slugs_validos, val)
    validar_seccao_b(card, val)
    validar_seccao_c(card, val)
    validar_e4_ausente(card, val)

    imprimir_relatorio(path, val)

    if args.verbose and val.ok:
        print("Verificacoes OK detalhadas:")
        for o in val.ok:
            print(f"  v {o}")
        print()

    if val.errors:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
