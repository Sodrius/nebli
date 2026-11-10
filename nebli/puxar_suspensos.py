"""Puxar para a aula nova o card que Davi suspendeu em outro deck (F-20261101-CLAUDE-03).

Davi (01/11): "se tem um card de uma aula que acabamos de criar e ele já está em outro deck, mas suspenso, puxe-o para a
aula nova, porque daí reavalio se vou suspendê-lo ou não / isso é para não perdermos bons cards porque suspendi há mt
tempo, quando o certo era suspender, mas quero rever agora".

- Candidato: nota NEBLI de outra aula, achada na busca por significado (acervo NEBLI-vivo, sim ≥ SIM e rank ≤ RANK numa
  chave da corrida), com todos os cards suspensos e sem `NEBLI::retirado::*` (retirada do pipeline não é suspensão de Davi).
- Gate: todo candidato entra por sh() (o apply move para o deck novo, dessuspende e marca `NEBLI::reavaliar::<aula>`) ou
  fica em EXCLUIDOS com motivo; cópia nova do mesmo AnKing (mesmo source::nid) no lugar da suspensa reprova.

F-20261110-CLAUDE-03 (Davi, 10/11): "quando vc puxa um associado de outro deck que estava suspenso, quero que o procedimento
padrão sempre seja o seguinte agora: deixa ele como principal do deck novo e associado ao antigo, dessuspenso no deck novo
para eu decidir o que farei com ele ao revê-lo".
- Vale também para nota com só PARTE dos cards suspensos: os cards suspensos vêm para o deck novo, dessuspensos; os ativos
  ficam onde Davi os estuda. A etiqueta da aula antiga fica (associação); a da aula nova é a principal (ordem e cor).
- EXCLUIDOS só aceita candidato suspenso cujo motivo comece por "outro assunto:" (parecido só no vocabulário). Conteúdo da
  aula não se exclui: vem por sh().
"""
OUTRO = "outro assunto:"
import json
import re
from pathlib import Path

SIM, RANK = 0.80, 3
TAG = "NEBLI::reavaliar::"


def _src(tags):
    return next((t.split("::")[-1] for t in tags if "source::nid" in t), None)


def suspensa_de_davi(nota, cards):
    """Algum card suspenso por Davi (F-20261110-CLAUDE-03: parcial também), fora retirada do pipeline."""
    return bool(cards) and any(c["queue"] == -1 for c in cards) and not any(t.startswith("NEBLI::retirado") for t in nota["tags"])


def candidatos(run, plan, A):
    run = Path(run)
    aula = "NEBLI::" + str(plan.get("lesson_id", ""))
    hits = {}
    p = run / "busca" / "semantica.jsonl"
    for linha in (p.read_text(encoding="utf-8").splitlines() if p.exists() else []):
        x = json.loads(linha)
        for t in x.get("top", []):
            if t.get("acervo") == "NEBLI-vivo" and t.get("sim", 0) >= SIM and t.get("rank_sem", 99) <= RANK:
                hits.setdefault(int(t["nid"]), x["chave"])
    if not hits:
        return []
    out = []
    for n in A("notesInfo", notes=sorted(hits)):
        if not n or aula in n["tags"]:
            continue
        cards = A("cardsInfo", cards=n["cards"])
        if suspensa_de_davi(n, cards):
            out.append({"nid": n["noteId"], "chave": hits[n["noteId"]], "src": _src(n["tags"]),
                        "decks": sorted({c["deckName"] for c in cards})})
    return out


def verificar(run, plan, A=None):
    if A is None:
        try:
            from nebli.decks import Anki
            A = Anki()
            A("version")
        except Exception as e:  # sem Anki não dá para saber o que está suspenso
            return [("[duro] v12: cards suspensos de outras aulas puxados para a aula nova (Anki indisponível: " + str(e)[:60] + ")", False)]
    cand = candidatos(run, plan, A)
    shs = {int(k) for k in (plan.get("compartilhados") or {})}
    shs |= {int(e["nid"]) for e in plan.get("entries", []) if e.get("kind") == "compartilhado"}
    fora = {int(x["nid"]) for x in plan.get("excluidos", []) if str(x.get("motivo", "")).strip().lower().startswith(OUTRO)
            and str(x.get("nid", "")).isdigit()}
    novos_src = {str(e.get("src")) for e in plan.get("entries", []) if e.get("src")}
    sem = [c["nid"] for c in cand if c["nid"] not in shs and c["nid"] not in fora]
    copia = [c["nid"] for c in cand if c["nid"] not in shs and c["src"] and c["src"] in novos_src]
    return [(f"[duro] v12: card suspenso de outra aula ({len(cand)}) puxado por sh() para o deck novo, dessuspenso (EXCLUIDOS só com 'outro assunto:'; F-20261110-CLAUDE-03)"
             + (f": sem decisão {sem[:5]}" if sem else ""), not sem),
            ("[duro] v12: sem cópia nova do AnKing quando a cópia suspensa com histórico existe"
             + (f": puxar {copia[:5]}" if copia else ""), not copia)]


def puxar(A, nota, cards, deck, aula, log):
    """Chamado pelo apply dentro de escrita(): move para o deck da aula nova, dessuspende e marca para reavaliação."""
    if not suspensa_de_davi(nota, cards):
        return False
    ids = [c["cardId"] for c in cards if c["queue"] == -1]  # só os suspensos; os ativos ficam onde Davi estuda
    A("changeDeck", cards=ids, deck=deck)
    A("unsuspend", cards=ids)
    A("addTags", notes=[nota["noteId"]], tags=TAG + aula)
    log(op="puxado-para-reavaliar", nid=nota["noteId"], cards=ids, de=sorted({c["deckName"] for c in cards if c["queue"] == -1}), para=deck)
    return True


def pendentes(A, lesson, deck):
    """Notas com a etiqueta da aula cujos cards em OUTRO deck estão suspensos por Davi (F-20261110-CLAUDE-03)."""
    from nebli.rotulos import canonical as canon
    out = []
    for n in A("notesInfo", notes=A("findNotes", query=f'"tag:NEBLI::{lesson}" -"tag:NEBLI::retirado::*"')):
        cards = [c for c in A("cardsInfo", cards=n["cards"]) if canon(c["deckName"]) != deck]
        if cards and suspensa_de_davi(n, cards):
            out.append((n, cards))
    return out


def main(argv=None):
    """python3 -m nebli.puxar_suspensos aplicar <corrida> [--seco]: aula já instalada recebe os associados suspensos."""
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("acao", choices=["aplicar"])
    ap.add_argument("corrida")
    ap.add_argument("--seco", action="store_true")
    a = ap.parse_args(argv)
    run = Path(a.corrida).resolve()
    plan = json.loads((run / "plan.json").read_text())
    lesson, deck = plan["lesson_id"], plan["deck"]
    from nebli.decks import Anki, escrita, em_tela
    A = Anki()
    pend = pendentes(A, lesson, deck)
    for n, cs in pend:
        print(n["noteId"], [c["cardId"] for c in cs if c["queue"] == -1], sorted({c["deckName"].split("::")[-1][:30] for c in cs}))
    if a.seco or not pend:
        print(len(pend), "nota(s) a puxar" + (" (seco)" if a.seco else ""))
        return
    log = []
    with escrita(A, f"puxar-suspensos-{lesson}", sync=False):
        tela = em_tela(A)
        feitos = [n["noteId"] for n, cs in pend if n["noteId"] not in tela and puxar(A, n, cs, deck, lesson, lambda **k: log.append(k))]
    with open(run / "journal.jsonl", "a", encoding="utf-8") as f:
        for x in log:
            f.write(json.dumps(dict(x, fonte="F-20261110-CLAUDE-03"), ensure_ascii=False) + "\n")
    print(len(feitos), "puxada(s);", len(pend) - len(feitos), "em tela (rodar de novo depois)")


if __name__ == "__main__":
    main()
