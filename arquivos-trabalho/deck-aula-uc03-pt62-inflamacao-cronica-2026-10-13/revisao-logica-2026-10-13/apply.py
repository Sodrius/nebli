import json, re, sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
sys.path.insert(0, str(RUN.parents[1]))
from nebli.decks import Anki, escrita, em_tela
from nebli.delta import same, base_of

A = Anki()
plan = json.loads((RUN / "plan.json").read_text())
receipt = json.loads((RUN / "receipt.json").read_text())
ids = {n["key"]: n["nid"] for n in receipt["notes"]}
lesson = plan["lesson_id"]
lesson_tag = f"NEBLI::{lesson}"
short = plan["short"]
base = base_of(RUN, short)
want = {e["key"] for e in plan["entries"]}
shown = set(em_tela(A))

live_ids = list(ids.values())
live = {n["noteId"]: n for n in A("notesInfo", notes=live_ids) if n}
all_cards = [cid for n in live.values() for cid in n["cards"]]
backup = HERE / "before-delete.json"
if not backup.exists():
    backup.write_text(json.dumps({
        "at": datetime.now(timezone.utc).isoformat(),
        "notes": live,
        "cards": A("cardsInfo", cards=all_cards),
        "reviews": A("getReviewsOfCards", cards=all_cards),
    }, ensure_ascii=False, indent=1))

deleted, pending = [], []
with escrita(A, "PT62 revisão lógica e exclusão de redundâncias", sync=False):
    # Excluir somente notas próprias desta corrida que saíram do plano. O
    # backup acima preserva campos, cartões e histórico de revisão.
    for key, nid in list(ids.items()):
        if key in want or nid not in live:
            continue
        if nid in shown:
            pending.append(key)
            continue
        note = A("notesInfo", notes=[nid])[0]
        assert lesson_tag in note["tags"], key
        assert not any(t.startswith("NEBLI::2026-") and t != lesson_tag for t in note["tags"]), key
        A("deleteNotes", notes=[nid])
        assert not A("findNotes", query=f"nid:{nid}")
        deleted.append(key)

    # Atualizar texto, verso, tags, cor e ordem preservando identidade,
    # comentário, histórico e marcas pessoais vermelha/laranja.
    for entry in plan["entries"]:
        key = entry["key"]
        nid = ids.get(key)
        if not nid:
            nid = A("addNote", note={"deckName": plan["deck"], "modelName": entry["model"],
                                      "fields": entry["fields"], "tags": entry["tags"],
                                      "options": {"allowDuplicate": True}})
            ids[key] = nid
        if nid in shown:
            pending.append(key)
            continue
        note = A("notesInfo", notes=[nid])[0]
        updates = {f: v for f, v in entry["fields"].items()
                   if f in ("Text", "Extra") and f in note["fields"] and not same(note["fields"][f]["value"], v)}
        if updates:
            A("updateNoteFields", note={"id": nid, "fields": updates})
        note = A("notesInfo", notes=[nid])[0]
        stale = [t for t in note["tags"] if t.startswith(f"NEBLI::ordem::{short}-") or t.startswith(f"NEBLI::cor::{lesson}::")]
        if stale:
            A("removeTags", notes=[nid], tags=" ".join(stale))
        A("addTags", notes=[nid], tags=" ".join(entry["tags"]))
        cards = A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))
        expected = {x["ord"]: x["flag"] for x in entry["cards"]}
        assert set(c["ord"] for c in cards) == set(expected), (key, cards, expected)
        for card in cards:
            if card["flags"] not in (1, 2) and card["flags"] != expected[card["ord"]]:
                A("setSpecificValueOfCard", card=card["cardId"], keys=["flags"], newValues=[expected[card["ord"]]], warning_check=True)
            if card["type"] == 0:
                A("setSpecificValueOfCard", card=card["cardId"], keys=["due"], newValues=[base + entry["order"] * 10 + card["ord"]], warning_check=True)

    # Compartilhadas recebem só a associação desta aula; conteúdo, baralho e
    # histórico permanecem na aula de origem.
    wanted_shared = {int(x) for x in plan["compartilhados"]}
    current_shared = set(A("findNotes", query=f'"tag:{lesson_tag}" "tag:NEBLI::compartilhado::{short}"'))
    for nid in current_shared - wanted_shared:
        if nid in shown:
            pending.append(str(nid)); continue
        note = A("notesInfo", notes=[nid])[0]
        stale = [t for t in note["tags"] if t == lesson_tag or t == f"NEBLI::compartilhado::{short}" or
                 t.startswith(f"NEBLI::ordem::{short}-") or t.startswith(f"NEBLI::cor::{lesson}::")]
        if stale:
            A("removeTags", notes=[nid], tags=" ".join(stale))
    flag_of = {"verde": 3, "azul": 4, "rosa": 5}
    for raw, shared in plan["compartilhados"].items():
        nid = int(raw)
        if nid in shown:
            pending.append(str(nid)); continue
        note = A("notesInfo", notes=[nid])[0]
        stale = [t for t in note["tags"] if t.startswith(f"NEBLI::ordem::{short}-") or t.startswith(f"NEBLI::cor::{lesson}::")]
        if stale:
            A("removeTags", notes=[nid], tags=" ".join(stale))
        A("addTags", notes=[nid], tags=f'{lesson_tag} NEBLI::compartilhado::{short} NEBLI::cor::{lesson}::{shared["cor"]} {shared["ordem_tag"]}')
        for card in A("cardsInfo", cards=note["cards"]):
            if card["flags"] not in (1, 2):
                # Não baixar uma prioridade maior herdada da aula de origem.
                target = flag_of[shared["cor"]]
                if card["flags"] == 0 or target < card["flags"]:
                    A("setSpecificValueOfCard", card=card["cardId"], keys=["flags"], newValues=[target], warning_check=True)

results = []
for entry in plan["entries"]:
    key, nid = entry["key"], ids[entry["key"]]
    note = A("notesInfo", notes=[nid])[0]
    cards = A("cardsInfo", cards=note["cards"])
    if key not in pending:
        assert all(same(note["fields"][f]["value"], entry["fields"][f]) for f in ("Text", "Extra")), key
        assert next(t for t in note["tags"] if t.startswith(f"NEBLI::ordem::{short}-")) == next(t for t in entry["tags"] if t.startswith(f"NEBLI::ordem::{short}-"))
    results.append({"key": key, "nid": nid, "cards": {str(c["cardId"]): {"ord": c["ord"], "flag": c["flags"]} for c in cards}})

flags = [c["flag"] for n in results for c in n["cards"].values()]
receipt.update(notes=results, selection_hash=plan["selection_hash"],
               cards_tag_aula=len(A("findCards", query=f'"tag:{lesson_tag}"')),
               cards_new_lesson=len(flags), expected=plan["totais"]["cards"],
               green=flags.count(3), blue=flags.count(4), pink=flags.count(5),
               compartilhados_tag=[int(x) for x in plan["compartilhados"]],
               problems=pending, at=datetime.now(timezone.utc).isoformat())
(RUN / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=1))
if not pending:
    (RUN / "plan-aplicado.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
result = {"deleted": deleted, "pending": pending, "own_cards": len(flags), "tagged_cards": receipt["cards_tag_aula"]}
(HERE / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=1))
print(json.dumps(result, ensure_ascii=False))
