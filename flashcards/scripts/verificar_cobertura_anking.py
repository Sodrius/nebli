#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verificar_cobertura_anking.py -- prova de cobertura da curadoria por aula.

Análogo, para a curadoria AnKing, do relatório de ratio Q01-Q30 do questionador:
torna a cobertura da aula um ARTEFATO EXPLÍCITO em vez de vibe. Lê o manifesto
flashcards/curadoria/<slug>.md -- a matriz conceito×card do gap-analysis -- e
responde a pergunta do Davi ("os cards cobrem TUDO da aula?") com um número:

    Cobertura AnKing: X/Y conceitos COBERTOS

Regras que valida (erros que travam o fechamento do bloco):
  1. Todo conceito da "Checklist-alvo" aparece no gap-analysis (nenhum some).
  2. Todo conceito LACUNA/PARCIAL/PENDENTE-GERADO nomeia a fonte externa (regra
     do Davi: sempre apontar o que falta e onde pegar). Fonte vazia ou "—" é erro.

Status reconhecidos no gap-analysis:
  COBERTO          -- >=1 card real do AnKing carrega o conceito.
  PARCIAL          -- so um aspecto; fonte externa completa o resto.
  LACUNA           -- 0 cards; cobrir por fonte externa (Netter/Moore/slide/deck).
  PENDENTE-GERADO  -- 0 cards reais bons; ENFILEIRADO pra card NEBLI gerado numa
                      sessao futura de calibracao (ver calibrar-antes-de-gerar-cards).
                      Status terminal VALIDO (nao trava), contado a parte de COBERTO.

Emite tambem arquivos-trabalho/cobertura-<slug>.json (legivel por maquina) com
as listas por status -- e o que alimenta a fila de geracao futura.

Não é gate hard de compilação -- é o validador que a sessão roda no passo 11 do
/resumo antes do apply, e cuja linha final vai pra coluna "Cobertura AnKing" do
_INDEX.md. Ver flashcards/CURADORIA-ANKING.md passos 4-6.

Uso:
    python flashcards/scripts/verificar_cobertura_anking.py anato-06-circulatorio-linfatico-II
"""
import argparse
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATUS = ("COBERTO", "PARCIAL", "LACUNA", "PENDENTE-GERADO")
# escrever "PENDENTE-GERADO" ou "PENDENTE GERADO" -- normaliza pra forma canonica
_PEND = re.compile(r"PENDENTE[ -]?GERAD[OA]")
_ID = re.compile(r"^\s*(\d+(?:\.\d+)+)\b")
VAZIO = {"", "-", "—", "–", "n/a", "na"}


def _celulas(linha):
    """Divide uma linha de tabela markdown em células (sem as bordas '|')."""
    linha = linha.strip()
    if not linha.startswith("|"):
        return None
    partes = [c.strip() for c in linha.strip().strip("|").split("|")]
    return partes


def parse_checklist_ids(texto):
    """IDs declarados na seção 'Checklist-alvo' (Y esperado de conceitos)."""
    ids = []
    dentro = False
    for linha in texto.splitlines():
        low = linha.lower()
        if low.startswith("#") and "checklist" in low:
            dentro = True
            continue
        if dentro and linha.startswith("#"):
            break
        if dentro:
            m = _ID.match(linha.replace("|", " "))
            if m and m.group(1) not in ids:
                ids.append(m.group(1))
    return ids


def parse_gap_analysis(texto):
    """Linhas de tabela cuja 2ª célula é COBERTO/PARCIAL/LACUNA.

    Retorna [(id, conceito, status, ncards, fonte)]."""
    linhas = []
    for linha in texto.splitlines():
        cel = _celulas(linha)
        if not cel or len(cel) < 2:
            continue
        status = cel[1].upper().strip()
        if _PEND.search(status):
            status = "PENDENTE-GERADO"
        if status not in STATUS:
            continue
        conceito = cel[0]
        m = _ID.match(conceito)
        cid = m.group(1) if m else conceito.split()[0] if conceito.split() else "?"
        ncards = cel[2] if len(cel) > 2 else ""
        fonte = cel[3] if len(cel) > 3 else ""
        linhas.append((cid, conceito, status, ncards, fonte))
    return linhas


def verificar(slug):
    manifesto = os.path.join(RAIZ, "flashcards", "curadoria", f"{slug}.md")
    if not os.path.exists(manifesto):
        print(f"ERRO: manifesto não encontrado: {os.path.relpath(manifesto, RAIZ)}")
        return 2
    texto = open(manifesto, encoding="utf-8").read()

    checklist_ids = parse_checklist_ids(texto)
    gap = parse_gap_analysis(texto)
    if not gap:
        print("ERRO: nenhuma linha de gap-analysis (COBERTO/PARCIAL/LACUNA) encontrada.")
        print("      A matriz conceito×card por PARTE precisa estar preenchida.")
        return 2

    ids_gap = {g[0] for g in gap}
    y = len(gap)
    cobertos = [g for g in gap if g[2] == "COBERTO"]
    parciais = [g for g in gap if g[2] == "PARCIAL"]
    lacunas = [g for g in gap if g[2] == "LACUNA"]
    pendentes = [g for g in gap if g[2] == "PENDENTE-GERADO"]
    x = len(cobertos)

    print(f"# Cobertura AnKing — {slug}\n")
    print(f"**Cobertura AnKing: {x}/{y} conceitos COBERTOS** "
          f"({len(parciais)} parcial, {len(lacunas)} lacuna, "
          f"{len(pendentes)} pendente-gerado)\n")

    erros = []

    # regra 1: conceito da checklist ausente do gap-analysis
    if checklist_ids:
        faltando = [cid for cid in checklist_ids if cid not in ids_gap]
        if faltando:
            erros.append("conceitos da checklist ausentes do gap-analysis: "
                         + ", ".join(faltando))

    # regra 2: LACUNA/PARCIAL/PENDENTE-GERADO sem fonte externa nomeada
    sem_fonte = [g for g in (parciais + lacunas + pendentes)
                 if g[4].strip().lower() in VAZIO]
    if sem_fonte:
        for cid, conceito, status, _n, _f in sem_fonte:
            erros.append(f"{status} {cid} ({conceito}) sem fonte externa apontada")

    if lacunas or parciais or pendentes:
        print("## Lacunas / parciais / pendentes → onde completar")
        for cid, conceito, status, _n, fonte in parciais + lacunas + pendentes:
            marca = "" if fonte.strip().lower() not in VAZIO else "  ⚠ SEM FONTE"
            print(f"- **{status} {cid}** {conceito} → {fonte or '(vazio)'}{marca}")
        print()

    if pendentes:
        print("## Fila pendente-gerado (sessao futura de calibracao)")
        print("Conceitos sem card real bom no AnKing, enfileirados pra card NEBLI gerado")
        print("APOS calibrar o padrao (ver calibrar-antes-de-gerar-cards). NAO gerar agora.")
        for cid, conceito, _s, _n, fonte in pendentes:
            print(f"- {cid} {conceito} → {fonte}")
        print()

    # artefato legivel por maquina: alimenta a fila de geracao futura
    cobertura_json = {
        "slug": slug,
        "x_cobertos": x,
        "y_total": y,
        "coberto": [g[0] for g in cobertos],
        "parcial": [g[0] for g in parciais],
        "lacuna": [g[0] for g in lacunas],
        "pendente_gerado": [g[0] for g in pendentes],
        "fonte_por_id": {g[0]: g[4] for g in gap if g[4].strip().lower() not in VAZIO},
        "conceito_por_id": {g[0]: g[1] for g in gap},
    }
    destino = os.path.join(RAIZ, "arquivos-trabalho", f"cobertura-{slug}.json")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(cobertura_json, f, ensure_ascii=False, indent=2)
    print(f"→ gravado {os.path.relpath(destino, RAIZ)}\n")

    # linha pronta pra coluna "Cobertura AnKing" do _INDEX.md
    pend_txt = f"; {len(pendentes)} pendente-gerado" if pendentes else ""
    lac_txt = "; ".join(f"{g[0]}→{g[4]}" for g in lacunas) if lacunas else "—"
    print("## Linha para _INDEX.md")
    print(f"| … | {x}/{y} COBERTOS{pend_txt} | {lac_txt} | … |\n")

    if erros:
        print("## ✗ ERROS a corrigir antes de fechar o bloco")
        for e in erros:
            print(f"- {e}")
        return 1
    print("## ✓ Cobertura consistente — checklist inteira avaliada, toda lacuna/pendente tem fonte.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Prova de cobertura da curadoria AnKing por aula.")
    ap.add_argument("slug", help="slug da aula (nome do manifesto em flashcards/curadoria/)")
    args = ap.parse_args()
    sys.exit(verificar(args.slug))


if __name__ == "__main__":
    main()
