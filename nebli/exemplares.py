"""Gera flashcards/projeto/GUIA_CARDS.md, o guia único de escrita de cards (F-20261023-CLAUDE-02/03), só a partir das marcas de Davi.

    python3 -m nebli.exemplares            # regrava o guia

Davi (23/10): “deixa os três .md: exemplares, anti-exemplares e análise num .md só chamado GUIA_CARDS.md, assim toda vez tem que ler e
vai guiar a geração de cards conforme o que já falei / tem que ter: o card antes, o card depois e o meu comentário todas as vezes (se eu
tiver posto comentário 4 vezes coloca o processo inteiro de ajustarmos)”.
- Exemplar = card com X/gostei ativo (tab-log do add-on), com o texto vivo e a análise (por que funciona, como usar).
- Anti-exemplar = nota com comentário de Davi: cada rodada (o card como estava + o comentário daquela vez, de comentarios-cards.jsonl),
  o card depois (vivo hoje) e a análise da família de erro.
As análises ficam em flashcards/projeto/exemplares_analise.py; item sem análise sai marcado “SEM ANÁLISE” e o gate reprova.
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import json
import re
from pathlib import Path

from nebli.decks import Anki
from nebli.explicacoes import liked_cards

ROOT = Path(__file__).resolve().parents[1]
PROJ = ROOT / "flashcards" / "projeto"
LOG = PROJ / "comentarios-cards.jsonl"
GUIA = PROJ / "GUIA_CARDS.md"
ELOGIO = re.compile(r"^(gostei|bom card|imagem top|exemplo de bom card|isso é um bom card|esse deck é referência|card ficou muito bom)", re.I)
MARCA = re.compile(r"CORRIGIDO,?\s*[\d/ ,.]+\d{2}\.?(?:\s*\((?:Claude|Codex)\):[^.]*\.)?", re.I)


def limpo(s):
    s = re.sub(r"<img[^>]*src=\"([^\"]+)\"[^>]*>", r"[IMG \1]", s or "")
    s = re.sub(r"<style.*?</style>", "", s, flags=re.S)
    s = html.unescape(re.sub(r"<br\s*/?>", " / ", s))
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def comentario_limpo(c):
    return re.sub(r"\s+", " ", MARCA.sub(" ", c or "")).strip(" .")


def _analises():
    spec = importlib.util.spec_from_file_location("exemplares_analise", PROJ / "exemplares_analise.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _frente_verso(n):
    f = {k: v["value"] for k, v in (n or {}).get("fields", {}).items()}
    if "Nome PT" in f:  # estrutura (Kenhub/IO): o nome e a figura são o card
        frente = f"[estrutura com seta] {limpo(f.get('Nome PT', ''))}"
        verso = limpo(f.get("Extra", "") or f.get("Imagem", "") or f.get("Imagem Verso", ""))
    else:
        frente = limpo(f.get("Text") or f.get("Front") or "")
        verso = limpo(f.get("Extra") or f.get("Back Extra") or f.get("Back") or "")
    return frente, verso


def _rodadas(hist):
    """Cada versão vista do comentário vira uma rodada: o card como estava e só o texto novo de Davi daquela vez."""
    out, anterior = [], ""
    for r in hist:
        c = re.sub(r"<[^>]+>", " ", r.get("comentario", ""))
        novo = c[len(anterior):] if c.startswith(anterior) else c
        anterior = c
        texto = comentario_limpo(novo)
        if texto:
            out.append((r.get("visto_em", "")[:10], limpo(r.get("card", "")), texto))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=Path)
    args = parser.parse_args()
    if args.snapshot:
        notes = {n["noteId"]: n for n in json.loads((args.snapshot / "notes.json").read_text())}
        cards = {c["cardId"]: c for c in json.loads((args.snapshot / "cards.json").read_text())}
        def A(action, **params):
            if action == "notesInfo": return [notes[n] for n in params["notes"] if n in notes]
            if action == "cardsInfo": return [cards[c] for c in params["cards"] if c in cards]
            if action == "findCards":
                return [cid for cid,c in cards.items() if c.get("queue") == -1 and c.get("reps",0)>0
                        and not any(t.startswith("NEBLI::retirado::") for t in notes.get(c["note"],{}).get("tags",[]))]
            raise ValueError(action)
    else:
        A = Anki()
    an = _analises()
    liked = json.loads((args.snapshot / "likes.json").read_text()) if args.snapshot else (liked_cards() or [])
    cids = [int(e["card"]) for e in liked]
    info = {c["cardId"]: c for c in (A("cardsInfo", cards=cids) if cids else []) if c and "cardId" in c}
    hist = {}
    for l in ((args.snapshot / "comment-history.jsonl") if args.snapshot else LOG).read_text(encoding="utf-8").splitlines():
        r = json.loads(l)
        hist.setdefault(r["nid"], []).append(r)
    if args.snapshot:
        for nid,n in notes.items():
            comment = n.get("fields",{}).get("NEBLI_Comentario",{}).get("value","")
            if comment and (not hist.get(nid) or limpo(hist[nid][-1]["comentario"]) != limpo(comment)):
                hist.setdefault(nid,[]).append({"nid":nid,"comentario":comment,"card":n.get("fields",{}).get("Text",{}).get("value",""),"visto_em":"2026-10-25","campos":{k:v["value"] for k,v in n["fields"].items()}})
    # Histórico misto não é um rótulo negativo da versão atual.
    anti_nids = [nid for nid,h in hist.items() if comentario_limpo(h[-1]["comentario"])]
    nids = sorted({c["note"] for c in info.values()} | set(anti_nids))
    vivos = {}
    for i in range(0, len(nids), 200):
        for n in A("notesInfo", notes=nids[i:i + 200]):
            if n:
                vivos[n["noteId"]] = n
    aula = lambda n: next((t.split("::")[1] for t in (n or {}).get("tags", []) if t.startswith("NEBLI::2026-")), "?")
    sem = 0
    L = ["# GUIA_CARDS — como Davi quer os cards", "",
         "Gerado por `python3 -m nebli.exemplares` (F-20261023-CLAUDE-02/03). **Ler inteiro antes de escrever qualquer card** (gate "
         "`exemplares_lidos`): achar os casos parecidos, moldar o autoral num EXEMPLAR específico e conferir contra o ANTI-EXEMPLAR do mesmo erro. "
         "Nada aqui é escrito à mão: exemplares são os cards com X de Davi; anti-exemplares, os cards que ele comentou; as análises vêm de "
         "`exemplares_analise.py`.", "",
         "## Os dois erros principais (Davi, 23/10)", "",
         "1. **Deck que não entende a aula**: não seguir o passo a passo (compreender o que a aula ensina, bloco a bloco do slide, antes de "
         "buscar) e encher de conteúdo lateral. Gate `passo_a_passo`.",
         "2. **Autoral de baixa qualidade**: cloze no lugar errado, sem negrito, sem porquê, frase estranha, fato solto sem processo. Custo-"
         "efetividade bom = um card carrega algo importante, de forma compreensível, a longo prazo, entendendo e relembrando bem um processo.", "",
         "## Análise geral: o que aprender destes casos", "",
         "Cada anti-exemplar abaixo pertence a uma família de erro; a lista diz o que fazer e quantas vezes Davi apontou o erro. Os "
         "exemplares mostram o certo: modelo de função + consequência (azol, HDAC), contraste no mesmo índice com dica (inata/adaptativa, "
         "ecto/endotrix), organizador em pé com índices deliberados (tolerância periférica, falhas do sistema imune), verso com o porquê "
         "(CTLA-4, GLUT-2) e figura que ensina o que o card cobra.", "", "__FAMILIAS__", "",
         "## Exemplares (X de Davi)", "", "O X aprova a versão vista naquele momento; o conteúdo atual pode ter mudado. Elogio de uma dimensão não aprova automaticamente fonte, imagem ou todos os clozes. Correção do executor não é novo elogio de Davi.", ""]
    for e in sorted(liked, key=lambda x: x.get("em", "")):
        c = info.get(int(e["card"]))
        if not c:
            continue
        n = vivos.get(c["note"])
        frente, verso = _frente_verso(n)
        a = an.EXEMPLARES.get(c["note"])
        sem += not a
        L += [f"### Exemplar · note {c['note']} ({aula(n)}; X em {e.get('em', '')[:10]})",
              f"- **Elogio de Davi:** gostei (X em {e.get('em', '')[:10]}).",
              f"- **Card:** {frente}"]
        if verso:
            L.append(f"- **Verso:** {verso}")
        for data, card, texto in _rodadas(hist.get(c["note"], [])):
            L.append(f"- **Comentário de Davi ({data}):** “{texto[:500]}”")
        L += [f"- **Análise:** {a or 'SEM ANÁLISE'}", ""]
    indisponiveis = [e for e in liked if int(e["card"]) not in info]
    if indisponiveis:
        L += ["## Gostei históricos sem card disponível", "",
              "O X está preservado no registro, mas a nota não foi encontrada na coleção atual. Sem o card, não há análise confiável para usá-lo como modelo.", ""]
        for e in indisponiveis:
            L.append(f"- **Gostei (X em {e.get('em', '')[:10]}):** card {e['card']}, nota {e.get('nota', '?')}; conteúdo indisponível.")
        L.append("")
    liked_nids = {c['note'] for c in info.values()}
    elogios = [nid for nid in anti_nids if nid not in liked_nids and nid in an.EXEMPLARES
               and ELOGIO.match(limpo(comentario_limpo(hist[nid][-1]['comentario'])))]
    if elogios:
        L += ["## Exemplares elogiados por comentário", "",
              "Elogio literal no comentário, sem X; a análise delimita o aspecto aprovado.", ""]
        for nid in elogios:
            n = vivos.get(nid)
            frente, verso = _frente_verso(n)
            L += [f"### Exemplar · note {nid} ({aula(n)}; elogio em comentário)",
                  f"- **Card:** {frente}"]
            if verso:
                L.append(f"- **Verso:** {verso}")
            L += [f"- **Comentário de Davi:** “{limpo(comentario_limpo(hist[nid][-1]['comentario']))[:500]}”",
                  f"- **Análise:** {an.EXEMPLARES[nid]}", ""]
    L += ["## Anti-exemplares e histórico de feedback", "",
          "As críticas mostram o estado que precisa ser evitado e o processo de correção. Elogios e edições também ficam no histórico, sem virar reprovação da versão atual.", ""]
    ordem = sorted(anti_nids, key=lambda nid: hist[nid][0].get("visto_em", ""))
    for nid in ordem:
        h = hist[nid]
        rod = _rodadas(h)
        n = vivos.get(nid)
        frente, verso = _frente_verso(n) if n else ("(nota apagada)", "")
        L.append(f"### Caso de feedback · note {nid} ({h[-1].get('aula') or aula(n)})")
        if rod:
            L.append(f"- **Registro histórico disponível (pode estar truncado; não é um diff completo):** {rod[0][1][:400] or '(sem texto: estrutura/imagem)'}")
        for i, (data, card, texto) in enumerate(rod, 1):
            if i > 1 and card and card != rod[i - 2][1]:
                L.append(f"- **Card na rodada {i}:** {card[:400]}")
            L.append(f"- **Davi, rodada {i} ({data}):** “{texto[:600]}”")
        L.append(f"- **Estado atual consultado (não implica aprovação):** {frente}")
        if verso:
            L.append(f"  - **Verso depois:** {verso}")
        L += [f"- **Análise:** {an.analise_anti(nid, ' '.join(t for _, _, t in rod))}", ""]
    # F-20261023-CLAUDE-04: “analisa os decks, o que suspendi, para compreender o que estou dizendo”. Suspenso por Davi = card de deck
    # NEBLI suspenso depois de estudado (reps > 0), fora de retirada do pipeline.
    sus = A("findCards", query='"deck:NEBLI*" is:suspended -"tag:NEBLI::retirado::*" prop:reps>0') or []
    sinfo = A("cardsInfo", cards=sus) if sus else []
    snotes = {}
    for c in sinfo:
        snotes.setdefault(c["note"], c)
    sn = {}
    ids = list(snotes)
    for i in range(0, len(ids), 200):
        for n in A("notesInfo", notes=ids[i:i + 200]):
            if n:
                sn[n["noteId"]] = n
    porau = {}
    for nid, n in sn.items():
        porau.setdefault(aula(n), []).append(n)
    L += ["## Cards suspensos após estudo (autoria da suspensão não inferida)", "",
          "Suspensão sozinha não indica reprovação: pode refletir fase da prova, carga ou outra decisão. Usar comentário explícito para interpretar qualidade.", ""]
    for au_ in sorted(porau):
        L.append(f"### {au_} — {len(porau[au_])} suspensos")
        for n in sorted(porau[au_], key=lambda n: n["noteId"]):
            orig = "autoral" if "NEBLI::origem::Autoral" in n["tags"] else "acervo"
            frente, _ = _frente_verso(n)
            L.append(f"- ({orig}) note {n['noteId']}: {frente[:220]}")
        L.append("")
    from collections import Counter
    cont = Counter(an.familia(" ".join(t for _, _, t in _rodadas(hist[nid]))) for nid in ordem)
    fam = [f"- **{f}** ({cont.get(f, 0)} casos): {txt}" for f, txt in sorted(an.FAMILIAS.items(), key=lambda kv: -cont.get(kv[0], 0))]
    L[L.index("__FAMILIAS__")] = "\n".join(fam)
    detail = PROJ / "CALIBRACAO-CASOS-2026-10-25.md"
    if detail.exists():
        L.insert(2, detail.read_text(encoding="utf-8"))
    recentes = PROJ / "CORRECOES-COMENTADAS-2026-10-26.md"
    if recentes.exists():
        L.insert(2, recentes.read_text(encoding="utf-8"))
    recentes_27 = PROJ / "CORRECOES-COMENTADAS-2026-10-27-TARDE.md"
    if recentes_27.exists():
        L.insert(2, recentes_27.read_text(encoding="utf-8"))
    clean_blocks = ("\n".join(line.rstrip() for line in block.splitlines()) for block in L)
    GUIA.write_text("\n".join(clean_blocks) + "\n", encoding="utf-8")
    print(f"GUIA_CARDS.md: {len(info)} exemplares vivos, {len(indisponiveis)} X históricos sem card, {len(ordem)} casos de feedback, {sem} sem análise")


if __name__ == "__main__":
    main()
