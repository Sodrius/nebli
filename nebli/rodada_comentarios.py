"""Rodada de comentários em sete passos, com gate (F-20261101-CLAUDE-04).

Davi (01/11): "aprende a sempre ler os comentários seguindo o seguinte passo a passo: ver os novos / reavaliar cards
com problemas similares / pensar porque teve aquele problema / pensar como não ter mais esse problema de forma
definitiva, mesmo em outra conversa (no geral com gates + indicações precisas e exemplos) / anotar nos exemplares,
anti-exemplares e guia / corrigir os cards todos com problema, seja comentário seja comando / aplicar tudo de volta".

    python3 -m nebli.rodada_comentarios abrir <pasta>      # passo 1: pendências vivas → <pasta>/RODADA.json
    python3 -m nebli.rodada_comentarios verificar <pasta>  # gate dos passos 2–7 (lê o Anki)

Pendência = comentário com fala de Davi depois do último CORRIGIDO (crítica) ou VISTO (elogio aprendido), tag `NEBLI::comando::*` ou bandeira vermelha.
Para cada item, RODADA.json registra:
  similares   {"busca": como procurou, "nids": [inspecionados], "corrigidos": [com o mesmo defeito, corrigidos]}
  causa       por que o card teve o problema (≥ 40 caracteres)
  prevencao   {"gate": função em nebli/ que agora reprova, ou "nao_mecanizavel": motivo; "indicacao": regra precisa
              escrita no GUIA-1; "exemplo": antes → depois}
  anotado     o nid aparece no GUIA-2 (elogio/X) ou GUIA-3 (erro), e a indicação no GUIA-1
  corrigido   true, ou "pendente: motivo" (pedido de interface que depende de reinício)
Itens da mesma família podem repetir causa e prevenção ("familia": nome). O passo 7 (aplicar) é conferido no vivo:
comentário termina em CORRIGIDO, tag de comando removida, bandeira vermelha devolvida, e "sync": true.
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GUIAS = {g: RAIZ / "flashcards" / "projeto" / f"{g}.md" for g in ("GUIA-1-REGRAS", "GUIA-2-EXEMPLARES", "GUIA-3-ANTI")}
COMANDO = "NEBLI::comando::"
_CORR = re.compile(r"\b(?:CORRIGIDO|VISTO)\s*,?\s*\d{1,2}\s*[,/]\s*\d{1,2}\s*[,/]\s*\d{2,4}\s*\.?(?:\s*\((?:Claude|Codex)\)[^.]*(?:\.|$))?", re.I)


def _clean(s):
    import html
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def fala_pendente(comentario):
    """Texto de Davi depois do último CORRIGIDO (vazio = nada pendente)."""
    partes = _CORR.split(_clean(comentario))
    return partes[-1].strip(" .") if partes else ""


def pendencias(A):
    itens = {}
    nids = A("findNotes", query='"deck:NEBLI*" NEBLI_Comentario:_*')
    for i in range(0, len(nids), 500):
        for n in A("notesInfo", notes=nids[i:i + 500]):
            f = fala_pendente(n["fields"].get("NEBLI_Comentario", {}).get("value", ""))
            if f:
                itens[n["noteId"]] = {"nid": n["noteId"], "tipos": ["comentario"], "fala": f}
    cmd = A("findNotes", query=f'"deck:NEBLI*" "tag:{COMANDO}*"')
    for n in A("notesInfo", notes=cmd) if cmd else []:
        tags = [t.split("::")[-1] for t in n["tags"] if t.startswith(COMANDO)]
        it = itens.setdefault(n["noteId"], {"nid": n["noteId"], "tipos": [], "fala": ""})
        it["tipos"].append("comando:" + ",".join(tags))
    red = A("findCards", query='"deck:NEBLI*" flag:1')
    for c in A("cardsInfo", cards=red) if red else []:
        it = itens.setdefault(c["note"], {"nid": c["note"], "tipos": [], "fala": ""})
        if "bandeira-vermelha" not in it["tipos"]:
            it["tipos"].append("bandeira-vermelha")
    return itens


def abrir(pasta, A):
    pasta = Path(pasta); pasta.mkdir(parents=True, exist_ok=True)
    itens = pendencias(A)
    for nid, it in itens.items():
        n = A("notesInfo", notes=[nid])[0]
        it["card"] = _clean(n["fields"].get("Text", n["fields"].get("Front", {"value": ""}))["value"])[:300]
        it["aula"] = next((t[7:] for t in n["tags"] if t.startswith("NEBLI::2026-")), "")
        it.update({"familia": "", "similares": {"busca": "", "nids": [], "corrigidos": []}, "causa": "",
                   "prevencao": {"gate": "", "nao_mecanizavel": "", "indicacao": "", "exemplo": ""}, "corrigido": False})
    r = {"aberta_em": datetime.now(timezone.utc).isoformat(), "itens": [itens[k] for k in sorted(itens)], "sync": False}
    (pasta / "RODADA.json").write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(itens)


def _gates_existentes():
    nomes = set()
    for p in (RAIZ / "nebli").glob("*.py"):
        defs = set(re.findall(r"(?m)^def (\w+)", p.read_text(encoding="utf-8")))
        nomes |= defs | {f"{p.stem}.{d}" for d in defs}
    return nomes


def verificar(pasta, A):
    pasta = Path(pasta)
    try:
        r = json.loads((pasta / "RODADA.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return [("[duro] passo 1: RODADA.json aberto por `nebli.rodada_comentarios abrir`", False)]
    itens = {int(i["nid"]): i for i in r.get("itens", [])}
    guia = {k: p.read_text(encoding="utf-8") if p.exists() else "" for k, p in GUIAS.items()}
    gates = _gates_existentes()
    out, por_passo = [], {k: [] for k in range(2, 8)}
    for nid, it in itens.items():
        s = it.get("similares") or {}
        if len(str(s.get("busca", "")).strip()) < 15 or not s.get("nids"):
            por_passo[2].append(nid)
        if len(str(it.get("causa", "")).strip()) < 40:
            por_passo[3].append(nid)
        pv = it.get("prevencao") or {}
        mecan = pv.get("gate") in gates or len(str(pv.get("nao_mecanizavel", "")).strip()) >= 40
        if not mecan or len(str(pv.get("indicacao", "")).strip()) < 30 or len(str(pv.get("exemplo", "")).strip()) < 20:
            por_passo[4].append(nid)
        ind = str(pv.get("indicacao", "")).strip()[:60]
        if str(nid) not in guia["GUIA-2-EXEMPLARES"] + guia["GUIA-3-ANTI"] or (ind and ind not in guia["GUIA-1-REGRAS"]):
            por_passo[5].append(nid)
        if it.get("corrigido") is not True and not str(it.get("corrigido", "")).startswith("pendente:"):
            por_passo[6].append(nid)
    # passo 7, no vivo: o que foi dado como corrigido não continua pendente
    vivos = pendencias(A)
    for nid, it in itens.items():
        if it.get("corrigido") is True and nid in vivos:
            por_passo[7].append(nid)
    novos = sorted(set(vivos) - set(itens))
    rot = {2: "reavaliou cards com problema similar (busca + nids inspecionados)",
           3: "pensou por que teve o problema (causa)",
           4: "prevenção definitiva: gate existente (ou motivo de não ser mecanizável) + indicação precisa + exemplo",
           5: "anotou nos exemplares/anti-exemplares (nid no GUIA-2/3) e a indicação no GUIA-1",
           6: "corrigiu todos os cards com problema, de comentário ou comando",
           7: "aplicou de volta: nada dado como corrigido segue pendente no Anki"}
    out.append((f"[duro] passo 1: todas as pendências vivas estão na rodada" + (f": novas {novos[:6]}" if novos else ""), not novos))
    for k in range(2, 8):
        out.append((f"[duro] passo {k}: {rot[k]}" + (f": faltam {por_passo[k][:6]}" if por_passo[k] else ""), not por_passo[k]))
    out.append(("[duro] passo 7: sincronizado depois da escrita (\"sync\": true)", r.get("sync") is True))
    return out


def main(argv=None):
    a = argv if argv is not None else sys.argv[1:]
    if len(a) != 2 or a[0] not in ("abrir", "verificar"):
        print(__doc__); return 2
    from nebli.decks import Anki
    A = Anki()
    if a[0] == "abrir":
        print(f"{abrir(a[1], A)} pendência(s) → {Path(a[1]) / 'RODADA.json'}"); return 0
    falhas = 0
    for nome, ok in verificar(a[1], A):
        print(("OK   " if ok else "FALHA ") + nome); falhas += not ok
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
