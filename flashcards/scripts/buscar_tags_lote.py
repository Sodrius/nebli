#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""buscar_tags_lote.py -- Camada 1 DIRIGIDA PELA CHECKLIST da E1.

Irmão em lote do buscar_tags_anking.py. Aquele busca UM termo por vez e o
curador tem que lembrar de digitar cada palavra-chave -- é por onde vaza o
recall (o conceito cuja keyword ninguém digitou nunca tem tag buscada). Este
recebe a CHECKLIST-alvo da aula (um conceito por linha, com sinônimos) e roda a
busca para a UNIÃO de todos os termos DE UMA VEZ, anotando, para cada tag
achada, QUAIS conceitos a motivaram. Assim os termos saem da aula, não da
memória do curador -- ver flashcards/CURADORIA-ANKING.md passo 1-2.

Formato canônico do arquivo de checklist:
    <id>\t<frase-alvo>\t<termo1|termo2|...>\t<nuclear|supporting|no_card>
Linhas no_card são ignoradas. REVIEW/AUDIT_ONLY bloqueiam a busca para impedir
que o extrator decida silenciosamente o que merece spaced repetition.
Linhas em branco e começadas por # são ignoradas. Aceita também o formato
mínimo "<id>\t<termos>" (sem frase) ou só "<termos>" (id vira o nº da linha).

Uso:
    python flashcards/scripts/buscar_tags_lote.py arquivos-trabalho/checklist-<slug>.tsv
    python flashcards/scripts/buscar_tags_lote.py checklist.tsv --step 1 --md
"""
import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# reusa a lógica canônica de Camada 1; carregar_tags lê o export UMA vez só
from buscar_tags_anking import carregar_tags

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass


def ler_checklist(path):
    """Devolve [(id, frase, termos_str)] a partir do .tsv da checklist."""
    itens = []
    pendentes = []
    with open(path, encoding="utf-8") as f:
        for n, linha in enumerate(f, 1):
            linha = linha.rstrip("\n")
            if not linha.strip() or linha.lstrip().startswith("#"):
                continue
            partes = linha.split("\t")
            if len(partes) >= 4:
                cid, frase, termos = partes[0].strip(), partes[1].strip(), partes[2].strip()
                decisao = partes[3].strip().lower()
                if decisao == "no_card":
                    continue
                if decisao not in {"nuclear", "supporting"}:
                    pendentes.append(f"{cid}:{partes[3].strip() or 'REVIEW'}")
                    continue
            elif len(partes) >= 3:
                cid, frase, termos = partes[0].strip(), partes[1].strip(), partes[2].strip()
            elif len(partes) == 2:
                cid, frase, termos = partes[0].strip(), "", partes[1].strip()
            else:
                cid, frase, termos = str(n), "", partes[0].strip()
            if termos:
                itens.append((cid, frase, termos))
    if pendentes:
        raise ValueError("classifique a checklist antes da busca: " + ", ".join(pendentes[:12]))
    return itens


def rodar(itens, step="1"):
    """Para cada conceito, busca a UNIÃO dos termos e mapeia tag -> {conceitos, count}.

    Carrega o export UMA vez (Counter tag->#cards) e filtra em memória por
    conceito -- evita reler os 92 MB por linha da checklist. Retorna
    (por_recurso, conceitos_com_hit) onde por_recurso[recurso] é lista de
    (tag, count, {ids_conceito})."""
    pfx = f"#AK_Step{step}_v12"
    tags = carregar_tags()                       # {tag: #cards}, uma leitura só
    step_tags = [(t, c) for t, c in tags.items() if t.startswith(pfx)]

    # Pré-normaliza cada tag UMA vez num conjunto de palavras minúsculas (>=3
    # letras). Tags usam '::' e '_' como separadores e prefixos numéricos
    # (12_Neurology::Pulmonary_circulation). Normalizar as DUAS pontas e casar
    # por palavra-inteira mata os dois erros do matching antigo (substring-regex):
    #   (a) termo multi-palavra "pulmonary circulation" NUNCA casava a tag
    #       "Pulmonary_circulation" (espaço != '_') -> LACUNA falsa (o "20/24"
    #       do Davi quando o real era ~87%);
    #   (b) palavra curta casava ruído DENTRO de outra ("ankle" em "rankle",
    #       o placeholder "<EN?>" virava quantificador regex '?') -> cobertura falsa.
    def _toks(s):
        return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) >= 3}

    tag_tokens = {t: _toks(t) for t, _ in step_tags}

    def _frases(termos_str):
        """'atrium|pulmonary circulation' -> [['atrium'], ['pulmonary','circulation']].
        Cada alternativa (separada por '|') vira uma frase; a frase casa a tag se
        TODAS as suas palavras aparecem inteiras na tag. Descarta o marcador <EN?>."""
        frases = []
        for alt in termos_str.split("|"):
            if alt.strip() == "<EN?>":
                continue
            ws = [w for w in re.findall(r"[a-z0-9]+", alt.lower()) if len(w) >= 3]
            if ws:
                frases.append(ws)
        return frases

    tag_count = {}
    tag_conceitos = collections.defaultdict(set)
    tag_recurso = {}
    conceitos_com_hit = set()

    for cid, _frase, termos in itens:
        frases = _frases(termos)
        if not frases:
            continue
        for tag, count in step_tags:
            toks = tag_tokens[tag]
            if not any(all(p in toks for p in fr) for fr in frases):
                continue
            partes = tag.split("::")
            recurso = partes[1] if len(partes) > 1 else "(raiz)"
            tag_count[tag] = count
            tag_recurso[tag] = recurso
            tag_conceitos[tag].add(cid)
            conceitos_com_hit.add(cid)

    agrupado = collections.defaultdict(list)
    for tag, count in tag_count.items():
        agrupado[tag_recurso[tag]].append((tag, count, tag_conceitos[tag]))
    return agrupado, conceitos_com_hit


def _ordena_ids(ids):
    def chave(s):
        try:
            return tuple(int(p) for p in s.split("."))
        except ValueError:
            return (9999, s)
    return sorted(ids, key=chave)


def imprimir(itens, agrupado, conceitos_com_hit, step, md):
    total_tags = sum(len(v) for v in agrupado.values())
    ids_todos = [cid for cid, _, _ in itens]
    lacunas = [cid for cid in ids_todos if cid not in conceitos_com_hit]

    bar = "|" if md else " "
    print(f"# Camada 1 dirigida pela checklist — {total_tags} tag(s) candidata(s) "
          f"em #AK_Step{step}_v12, de {len(itens)} conceito(s)\n")

    if md:
        print("| Leaf-tag (recurso::caminho) | #cards | Conceitos | Classe | Decisão |")
        print("|---|---|---|---|---|")

    for recurso in sorted(agrupado, key=lambda r: -sum(c for _, c, _ in agrupado[r])):
        if not md:
            soma = sum(c for _, c, _ in agrupado[recurso])
            print(f"## {recurso} — {soma} cards")
        for tag, count, ids in sorted(agrupado[recurso], key=lambda x: -x[1]):
            leaf = "::".join(tag.split("::")[2:])
            conc = ",".join(_ordena_ids(ids))
            if md:
                print(f"| {recurso}::{leaf} | {count} | {conc} |  |  |")
            else:
                print(f"   {count:4d}  [{conc}]  {leaf}")
        if not md:
            print()

    # o ponto do script: conceito buscado que NÃO achou tag = LACUNA declarada,
    # não silêncio. Vira fonte externa no gap-analysis (passo 4 do método).
    print("\n## Conceitos SEM tag candidata (LACUNA de AnKing — apontar fonte externa)")
    if lacunas:
        frase_por_id = {cid: frase for cid, frase, _ in itens}
        for cid in _ordena_ids(lacunas):
            frase = frase_por_id.get(cid, "")
            print(f"- **{cid}** {frase} — 0 tags no AnKing Step{step}. "
                  f"Cobrir por fonte externa (slide / Netter-Moore / deck dedicado).")
    else:
        print("- (nenhum — todo conceito da checklist achou ao menos uma tag)")


def main():
    ap = argparse.ArgumentParser(description="Camada 1 em lote dirigida pela checklist da E1.")
    ap.add_argument("checklist", help="arquivo .tsv: <id>\\t<frase>\\t<termo1|termo2|...>")
    ap.add_argument("--step", default="1")
    ap.add_argument("--md", action="store_true",
                    help="tabela markdown colável na Camada 1 do manifesto")
    args = ap.parse_args()

    itens = ler_checklist(args.checklist)
    if not itens:
        print(f"(checklist vazia em {args.checklist})")
        return
    agrupado, conceitos_com_hit = rodar(itens, step=args.step)
    imprimir(itens, agrupado, conceitos_com_hit, args.step, args.md)


if __name__ == "__main__":
    main()
