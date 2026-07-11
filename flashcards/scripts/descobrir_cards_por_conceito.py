#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""descobrir_cards_por_conceito.py -- Camada 1 por CONTEUDO (nao por caminho de tag).

Correcao do Estagio 1 (2026-07-11): o buscar_tags_lote casava as palavras-chave
contra o NOME da tag num export estatico -> lacunas fantasma (mismatch, conjugacao,
proofreading davam 0 mesmo com o AnKing cobrindo). Este script busca no CONTEUDO
real do card via AnkiConnect (findNotes sobre o texto), coleta as tags das notas
que casam e devolve, por conceito da checklist:
  - quantas notas o conceito tem (0 = LACUNA REAL, provada, nao presumida)
  - as leaf-tags candidatas ranqueadas (feed pro extrair_cards_anking.py)

Assim acha o card ONDE ELE MORA (mata a lacuna tipo-b: existe no AnKing mas fora
da subarvore que o curador lembrou de puxar).

Filtros: IDF descarta tokens comuns/ruidosos (factor/base/mutation) por frequencia;
meta-tags (#Low/HighYield, #OME_banner, IDs AMBOSS/NBME) saem do tally.
LIMITE conhecido: busca por keyword sofre de POLISSEMIA ("repair" casa hernia/osso).
Logo o relatorio e RECALL-orientado -- as tags sao candidatas, a Camada 2
(leitura card-a-card) faz a precisao. Lacuna real se confirma pelo termo
distintivo (findNotes "photolyase" = 0). Conserto definitivo = busca semantica
por embeddings (ver flashcards/PLANO-PESQUISA-CARDS-IA.md, Corrente 4).

Uso:
    python flashcards/scripts/descobrir_cards_por_conceito.py <slug>
    python flashcards/scripts/descobrir_cards_por_conceito.py <slug> --step 1 --min-tag 2

Le  arquivos-trabalho/checklist-<slug>.tsv (linhas <id>\\t<frase>\\t<pt>|<en>).
Grava arquivos-trabalho/descoberta-<slug>.md (relatorio) e imprime o resumo.
"""
import json, sys, os, re, argparse, urllib.request, collections

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ANKICONNECT = "http://localhost:8765"
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
STOP = {"acid", "acids", "the", "and", "via", "from", "with", "into", "que",
        "para", "como", "dos", "das", "por", "vs", "e"}
_TOK = re.compile(r"[a-z0-9][a-z0-9-]{2,}")
# meta/organizacionais: nao sao subarvore de conteudo -> fora do tally
_META = ("highyield", "loweryield", "image_update", "_banner", "^systems",
         "^physeo", "::extra", "#tags", "#tips", "#ak_clinical",
         "#amboss", "#nbme", "#uworld", "#free", "#firstaid_")


def _eh_meta(leaf):
    l = leaf.lower()
    return l.startswith("^") or any(m in l for m in _META)


def _invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]


def _ler_checklist(slug):
    caminho = os.path.join(RAIZ, "arquivos-trabalho", f"checklist-{slug}.tsv")
    conceitos = []
    with open(caminho, encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("#") or not linha.strip():
                continue
            partes = linha.rstrip("\n").split("\t")
            if len(partes) < 3:
                continue
            cid, frase, termos = partes[0], partes[1], partes[2]
            en = termos.split("|")[-1] if "|" in termos else termos
            conceitos.append((cid, frase, en))
    return conceitos


def _tokens(txt):
    out = []
    for t in _TOK.findall(txt.lower()):
        if t not in STOP and t not in out:
            out.append(t)
    return out


_FREQ = {}  # token -> nº de notas AnKing que o contêm (cache IDF)


def _freq(tok, step):
    if tok not in _FREQ:
        _FREQ[tok] = len(_invoke("findNotes", query=f'"tag:#AK_Step{step}_v12::*" {tok}'))
    return _FREQ[tok]


def _distintivos(toks, step, cap):
    """Fica só com os tokens raros (freq <= cap) — os que identificam o conceito.
    Se todos forem comuns, usa os 2 mais raros. É o filtro IDF que mata o ruído
    de 'factor/base/mutation/resistance'."""
    raros = [t for t in toks if _freq(t, step) <= cap]
    if raros:
        return raros
    return sorted(toks, key=lambda t: _FREQ.get(t, 0))[:2]


def _query(toks, step):
    if not toks:
        return None
    return f'"tag:#AK_Step{step}_v12::*" ({" OR ".join(toks)})'


def _leaf(tag):
    # tira o prefixo #AK_StepN_v12:: -> caminho usavel pelo extrair_cards
    parts = tag.split("::")
    return "::".join(parts[1:]) if len(parts) > 1 else tag


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--step", default="1")
    ap.add_argument("--min-tag", type=int, default=2,
                    help="tag entra na lista de extracao se >= N notas a sustentam")
    ap.add_argument("--cap", type=int, default=600,
                    help="token com freq > cap e comum demais (ruido) -> descartado (filtro IDF)")
    args = ap.parse_args()

    conceitos = _ler_checklist(args.slug)
    pfx = f"#AK_Step{args.step}_v12"

    # 1 findNotes por conceito (so tokens distintivos por IDF); junta ids -> 1 notesInfo.
    por_conceito = {}
    todos = set()
    for cid, frase, en in conceitos:
        toks = _distintivos(_tokens(en), args.step, args.cap)
        q = _query(toks, args.step)
        nids = set(_invoke("findNotes", query=q)) if q else set()
        por_conceito[cid] = {"frase": frase, "toks": toks, "nids": nids}
        todos |= nids

    tagmap = {}
    if todos:
        for n in _invoke("notesInfo", notes=sorted(todos)):
            tagmap[n["noteId"]] = [t for t in n.get("tags", []) if t.startswith(pfx)]

    # tally por conceito (so tags de conteudo) + acumula extracao global
    extrair_global = collections.Counter()
    linhas_md = ["# Descoberta por conteúdo — " + args.slug,
                 "", "> Camada 1 por CONTEÚDO (findNotes no texto do card, não no caminho da tag).",
                 "> Recall-orientado: as tags são candidatas; a Camada 2 faz a precisão.",
                 "> **Sinal fraco** (top-tag < %d notas) = subárvore não carrega o conceito →" % args.min_tag,
                 "> verificar com o termo distintivo (`findNotes \"<enzima/doença>\"`); se 0, é lacuna real → card NEBLI da E1.",
                 "", "| Concept | Sinal | Top leaf-tags de conteúdo (contagem) |", "|---|---|---|"]
    fracos = []
    for cid, frase, en in conceitos:
        d = por_conceito[cid]
        tally = collections.Counter()
        for nid in d["nids"]:
            for t in tagmap.get(nid, []):
                leaf = _leaf(t)
                if not _eh_meta(leaf):
                    tally[leaf] += 1
        top = tally.most_common(6)
        sinal = top[0][1] if top else 0
        if sinal < args.min_tag:
            fracos.append((cid, frase))
        for leaf, c in top:
            if c >= args.min_tag:
                extrair_global[leaf] += c
        top_str = " · ".join(f"`{l}` ({c})" for l, c in top[:5]) or "—"
        linhas_md.append(f"| **{cid}** {frase[:44]} | {sinal} | {top_str} |")

    linhas_md += ["", "## Sinal fraco — verificar termo distintivo (candidatos a lacuna real)"]
    linhas_md += ([f"- **{cid}** {frase}" for cid, frase in fracos] or ["- (nenhum)"])
    linhas_md += ["", "## Tags sugeridas para extrair_cards_anking.py (top de conteúdo, >= min-tag)"]
    sug = [l for l, _ in extrair_global.most_common()]
    linhas_md += (["```", *(f'"{l}"' for l in sug), "```"] if sug else ["- (nenhuma)"])

    destino = os.path.join(RAIZ, "arquivos-trabalho", f"descoberta-{args.slug}.md")
    with open(destino, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas_md) + "\n")

    fortes = len(conceitos) - len(fracos)
    print(f"{args.slug}: {fortes}/{len(conceitos)} conceitos com subárvore forte | "
          f"{len(fracos)} sinal fraco (verificar) | {len(sug)} tag(s) sugerida(s)")
    print(f"-> {os.path.relpath(destino, RAIZ)}")


if __name__ == "__main__":
    main()
