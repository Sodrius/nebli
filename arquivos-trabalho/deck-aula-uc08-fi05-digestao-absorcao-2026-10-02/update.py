"""Delta pós-busca nos acervos externos (F-20261002-CLAUDE-04): troca 2 autorais por MCAT e retira 2 autorais rosa. Uso: update.py"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1]))
import build as B
from nebli.decks import Anki, escrita
A = Anki(); plan = json.loads((HERE / "plan.json").read_text()); rec = json.loads((HERE / "receipt.json").read_text())
nid_of = {r["key"]: r["nid"] for r in rec["notes"]}
LESSON = plan["lesson_id"]; LT = f"NEBLI::{LESSON}"
REMOVE = {"proporcao-monos": "rosa de baixo ganho; autoria deve ser minoria", "ca-atpase": "rosa de baixo ganho; autoria deve ser minoria"}
SWAP = {  # autoral -> cópia MCAT (acervo antes de autoria)
 "jejuno": dict(key="mcat-jejuno-ileo", src=1556166328692, flags={2: 4}, uncloze=[1], alvo="Jejuno e íleo são os segmentos de absorção",
                motivo="Azul: mensagem do slide 3; MCAT cobre o alvo, autoral retirado."),
 "maltase": dict(key="mcat-dissacaridases", src=1556162724731, flags={1: 4, 2: 4}, uncloze=[3], alvo="Dissacaridases da borda em escova (maltose, isomaltose, lactose, sacarose)",
                 motivo="Azul: MCAT cobre maltase/isomaltase como classe; autoral da maltase retirado."),
}
BUSCA_EXT = ("AnKing Step por texto e pelo bloco Costanzo GI 05 Digestion/First Aid (q.py); Referências Externas (MCAT, Histology, Dope, "
             "Ankisthesia) pelos mesmos termos em 02/10 (busca/ext.txt): ")


def main():
    tf = A("modelFieldNames", modelName=B.MODEL)
    with escrita(A, f"FI05 {plan['run_id']} delta"):
        new_entries = {}
        for old, s in SWAP.items():
            e_old = next(e for e in plan["entries"] if e["key"] == old)
            n = A("notesInfo", notes=[s["src"]])[0]; base = {k: v["value"] for k, v in n["fields"].items()}
            if A("findNotes", query=f'"tag:NEBLI::source::nid-{s["src"]}"'): raise SystemExit(f"cópia viva já existe {s['src']}")
            fields = {f: "" for f in tf}
            fields["Text"] = B.uncloze(base["Text"], set(s["uncloze"]))
            fields["Extra"], removed = B.strip_credit(B.WHITE.sub("", B.KHAN.sub("", base.get("Extra", ""))))
            assert B.clozes(fields["Text"]) == sorted(s["flags"]), (s["key"], B.clozes(fields["Text"]))
            cards = [{"n": k, "ord": k - 1, "flag": v, "cor": B.COR[v]} for k, v in sorted(s["flags"].items())]
            otag = next(t for t in e_old["tags"] if t.startswith("NEBLI::ordem::"))
            tags = sorted(set(n["tags"] + [LT, "NEBLI::escopo::aula", f"NEBLI::objetivo::{e_old['bloco']}", otag, f"NEBLI::run::{plan['run_id']}",
                                           f"NEBLI::source::nid-{s['src']}", "NEBLI::origem::MCAT"] + [f"NEBLI::cor::{LESSON}::{c['cor']}" for c in cards]))
            new_entries[old] = dict(key=s["key"], kind="text", src=s["src"], flags={str(k): v for k, v in s["flags"].items()}, bloco=e_old["bloco"],
                                    alvo=s["alvo"], evid=e_old["evid"], motivo=s["motivo"], uncloze=s["uncloze"], order=e_old["order"], origin="MCAT",
                                    model=B.MODEL, tags=tags, fields=fields, fields_hash=B.h(fields), cards=cards, source_fields_hash=B.h(base),
                                    credito_removido=removed, substitui=old)
        log = []
        for old in list(SWAP) + list(REMOVE):
            nid = nid_of[old]; cs = A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))
            if any(c["reps"] for c in cs): raise SystemExit(f"{old} já foi estudado; não apagar")
            due = min(c["due"] for c in cs)
            A("deleteNotes", notes=[nid]); log.append({"op": "deleteNote", "key": old, "nid": nid})
            if old in SWAP:
                e = new_entries[old]
                new = A("addNote", note={"deckName": plan["deck"], "modelName": e["model"], "fields": e["fields"], "tags": e["tags"], "options": {"allowDuplicate": True}})
                for c in A("cardsInfo", cards=A("findCards", query=f"nid:{new}")):
                    flag = next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"])
                    A("setSpecificValueOfCard", card=c["cardId"], keys=["flags", "due"], newValues=[flag, due], warning_check=True)
                log.append({"op": "addNote", "key": e["key"], "nid": new, "due": due}); nid_of[e["key"]] = new
        entries = []
        for e in plan["entries"]:
            if e["key"] in REMOVE: continue
            e = new_entries.get(e["key"], e)
            if e["origin"] == "Autoral": e["busca"] = BUSCA_EXT + e["busca"].split("Referências Externas pelos mesmos termos: ")[-1]
            entries.append(e)
        plan["entries"] = entries
        plan["retirados_pos_instalacao"] = [{"key": k, "motivo": v} for k, v in REMOVE.items()] + [{"key": k, "motivo": f"substituído por {s['key']}"} for k, s in SWAP.items()]
        tot = lambda f: sum(1 for e in entries for x in e["cards"] if f(e, x)); orig = sorted({e["origin"] for e in entries})
        plan["totais"].update(notas=len(entries), cards=tot(lambda e, x: True), verdes=tot(lambda e, x: x["flag"] == 3), azuis=tot(lambda e, x: x["flag"] == 4),
                              rosas=tot(lambda e, x: x["flag"] == 5), origens_notas={o: sum(e["origin"] == o for e in entries) for o in orig},
                              origens_cards={o: sum(len(e["cards"]) for e in entries if e["origin"] == o) for o in orig})
        plan["selection_hash"] = B.h([(e["key"], e["fields_hash"], e["cards"]) for e in entries])
        # readback
        problems = []
        for e in entries:
            n = A("notesInfo", notes=[nid_of[e["key"]]])[0]
            if any(n["fields"][k]["value"] != v for k, v in e["fields"].items()): problems.append(f"campos {e['key']}")
            for c in A("cardsInfo", cards=n["cards"]):
                if c["flags"] != next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"]): problems.append(f"flag {e['key']}")
        live = len(A("findCards", query=f'"deck:{plan["deck"]}"'))
        rec.update(notes=[{"key": e["key"], "nid": nid_of[e["key"]]} for e in entries], cards_new_lesson=live, expected=plan["totais"]["cards"], delta=log, problems=problems)
        (HERE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1)); (HERE / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
        print(json.dumps(plan["totais"], ensure_ascii=False), "vivos no deck:", live, "problemas:", problems)
        if problems or live != plan["totais"]["cards"]: raise SystemExit("readback divergente")


if __name__ == "__main__":
    main()
