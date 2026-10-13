"""Delta 2 (F-20261002-CLAUDE-05): calibração pelo Aires caps. 62–63 e pelas aulas dos canais. Acrescenta hormônios e íleo (AnKing),
reescreve 3 autorais, retira 1, reordena tudo na sequência da aula. Uso: update2.py"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1]))
import build as B
from nebli import ordem
from nebli.decks import Anki, escrita
A = Anki(); plan = json.loads((HERE / "plan.json").read_text()); rec = json.loads((HERE / "receipt.json").read_text())
nid_of = {r["key"]: r["nid"] for r in rec["notes"]}
LESSON, SHORT = plan["lesson_id"], plan["short"]; LT = f"NEBLI::{LESSON}"
Na = "Na<sup>+</sup>"
REMOVE = {}
REWRITE = {
 "agua-osmose": ("<b>Water</b> is absorbed in the intestine by {{c1::osmosis}}, following absorbed solutes such as NaCl", None,
                 "Auditoria dos autorais: resposta binária (active/passive) era induzível; agora cobra o mecanismo."),
}
RECOLOR = {}
ADD = [
 ("aa-na", dict(key="mcat-aminopeptidase", src=1556163027557, flags={1: 4, 3: 4}, uncloze=[2], origin="MCAT", bloco="C-proteinas", evid="Slide 5", alvo="Aminopeptidase da borda em escova remove aminoácidos da ponta N-terminal",
                motivo="Azul: 'PROTEASES' da borda em escova no slide; Aires e MK Fisiologia nomeiam a aminopeptidase.")),
 ("lipase-ph", dict(key="ze-esteatorreia", src=1482021783566, flags={1: 4}, bloco="D-lipidios", evid="Slide 6", alvo="Zollinger-Ellison → esteatorreia por inativação da lipase",
                    motivo="Azul: aplicação direta do pH da lipase, citada no Aires cap. 62.")),
 ("b12-ileo", dict(key="b12-estoque", src=1476583759387, flags={1: 4}, uncloze=[2, 3], bloco="G-vitaminas", evid="Slide 10", alvo="Estoque hepático de B12 dura 3–4 anos",
                   motivo="Azul: explica por que a deficiência demora (Aires cap. 62).")),
 ("b12-complexo", dict(key="b12-transcobalamina", src=1476661164427, flags={1: 4}, bloco="G-vitaminas", evid="Slide 10", alvo="No ileócito a B12 passa para a transcobalamina II",
                       motivo="Azul: etapa presente no Aires e nas aulas de B12 dos canais.")),
]


def main():
    tf = A("modelFieldNames", modelName=B.MODEL)
    with escrita(A, f"FI05 {plan['run_id']} delta3"):
        entries = [e for e in plan["entries"]]
        for k in REMOVE:
            nid = nid_of.pop(k)
            if not A("findNotes", query=f"nid:{nid}"):  # já apagada numa execução interrompida
                entries = [e for e in entries if e["key"] != k]; continue
            if any(c["reps"] for c in A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))): raise SystemExit(f"{k} já estudado")
            A("deleteNotes", notes=[nid]); entries = [e for e in entries if e["key"] != k]
        for k, (text, extra, why) in REWRITE.items():
            e = next(e for e in entries if e["key"] == k); nid = nid_of[k]
            if any(c["reps"] for c in A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))): raise SystemExit(f"{k} já estudado")
            if text: e["fields"]["Text"] = text
            if extra is not None:
                im = re.search(r"<img[^>]*>", e["fields"]["Extra"]); e["fields"]["Extra"] = extra.replace("__IMG__", im.group(0) if im else "").rstrip("<br>") if im else extra.replace("<br><br>__IMG__", "")
            A("updateNoteFields", note={"id": nid, "fields": {"Text": e["fields"]["Text"], "Extra": e["fields"]["Extra"]}})
            e["fields_hash"] = B.h(e["fields"]); e["reescrito"] = why
        for k, flags in RECOLOR.items():
            e = next(e for e in entries if e["key"] == k)
            for c in A("cardsInfo", cards=A("findCards", query=f"nid:{nid_of[k]}")):
                A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[flags[c["ord"] + 1]], warning_check=True)
            e["cards"] = [{"n": n, "ord": n - 1, "flag": f, "cor": B.COR[f]} for n, f in sorted(flags.items())]; e["flags"] = {str(n): f for n, f in flags.items()}
            cor = sorted({c["cor"] for c in e["cards"]})
            A("removeTags", notes=[nid_of[k]], tags=" ".join(f"NEBLI::cor::{LESSON}::{x}" for x in ("verde", "azul", "rosa")) + " NEBLI::lateral")
            A("addTags", notes=[nid_of[k]], tags=" ".join(f"NEBLI::cor::{LESSON}::{x}" for x in cor))
            e["tags"] = sorted(set(t for t in e["tags"] if "::cor::" not in t and t != "NEBLI::lateral") | {f"NEBLI::cor::{LESSON}::{x}" for x in cor})
        for after, s in ADD:
            n = A("notesInfo", notes=[s["src"]])[0]; base = {k: v["value"] for k, v in n["fields"].items()}
            existing = A("findNotes", query=f'"tag:NEBLI::source::nid-{s["src"]}" "tag:{LT}"')  # criada numa execução interrompida
            fields = {f: "" for f in tf}
            fields["Text"] = B.uncloze(base["Text"], set(s.get("uncloze", [])))
            fields["Extra"], removed = B.strip_credit(B.WHITE.sub("", B.KHAN.sub("", base.get("Extra", ""))))
            assert B.clozes(fields["Text"]) == sorted(s["flags"]), (s["key"], B.clozes(fields["Text"]))
            assert not re.search(r"credit|licensed by", fields["Extra"], re.I), s["key"]
            cards = [{"n": k, "ord": k - 1, "flag": v, "cor": B.COR[v]} for k, v in sorted(s["flags"].items())]
            tags = sorted(set(n["tags"] + [LT, "NEBLI::escopo::aula", f"NEBLI::objetivo::{s['bloco']}", f"NEBLI::run::{plan['run_id']}",
                                           f"NEBLI::source::nid-{s['src']}", f"NEBLI::origem::{s.get('origin', 'AnKing')}"] + [f"NEBLI::cor::{LESSON}::{c['cor']}" for c in cards]))
            e = dict(s, kind="text", flags={str(k): v for k, v in s["flags"].items()}, origin=s.get("origin", "AnKing"), model=B.MODEL, tags=tags, fields=fields,
                     fields_hash=B.h(fields), cards=cards, source_fields_hash=B.h(base), credito_removido=removed, acrescentado="delta3: Aires + canais")
            new = existing[0] if existing else A("addNote", note={"deckName": plan["deck"], "modelName": B.MODEL, "fields": fields, "tags": tags, "options": {"allowDuplicate": True}})
            for c in A("cardsInfo", cards=A("findCards", query=f"nid:{new}")):
                A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[next(x["flag"] for x in cards if x["ord"] == c["ord"])], warning_check=True)
            nid_of[s["key"]] = new
            i = next(i for i, x in enumerate(entries) if x["key"] == after); entries.insert(i + 1, e)
        # reordenar: entradas e compartilhadas numa só sequência
        seq = [("e", e) for e in entries]
        for nid, s in sorted(plan["compartilhados"].items(), key=lambda kv: kv[1]["order"]):
            pos = next((i for i, (t, x) in enumerate(seq) if t == "e" and "order" in x and x["order"] > s["order"]), len(seq))
            seq.insert(pos, ("s", (nid, s)))
        dues = sorted(c["due"] for e in entries for c in A("cardsInfo", cards=A("findCards", query=f"nid:{nid_of[e['key']]}")) if c["type"] == 0)
        base_due = dues[0] if dues else 0
        for order, (t, x) in enumerate(seq, 1):
            new_tag = ordem.tag(SHORT, order)
            nid = nid_of[x["key"]] if t == "e" else int(x[0])
            old = [tg for tg in A("notesInfo", notes=[nid])[0]["tags"] if tg.startswith(f"NEBLI::ordem::{SHORT}-")]
            if old != [new_tag]:
                if old: A("removeTags", notes=[nid], tags=" ".join(old))
                A("addTags", notes=[nid], tags=new_tag)
            if t == "e":
                x["order"] = order; x["tags"] = sorted(set(tg for tg in x["tags"] if not tg.startswith(f"NEBLI::ordem::{SHORT}-")) | {new_tag})
                for c in A("cardsInfo", cards=A("findCards", query=f"nid:{nid}")):
                    if c["type"] == 0:
                        A("setSpecificValueOfCard", card=c["cardId"], keys=["due"], newValues=[base_due + order * 10 + c["ord"]], warning_check=True)
            else:
                x[1]["order"] = order; x[1]["ordem_tag"] = new_tag
        plan["entries"] = entries
        plan.setdefault("retirados_pos_instalacao", []).extend({"key": k, "motivo": v} for k, v in REMOVE.items())
        plan["calibracao"] = {"livro": "Aires, Fisiologia, caps. 62 e 63 (arquivos-trabalho/livros/)", "aulas": "transcrições em arquivos-trabalho/videos-fi05/"}
        tot = lambda f: sum(1 for e in entries for x in e["cards"] if f(e, x)); orig = sorted({e["origin"] for e in entries})
        plan["totais"].update(notas=len(entries), cards=tot(lambda e, x: True), verdes=tot(lambda e, x: x["flag"] == 3), azuis=tot(lambda e, x: x["flag"] == 4),
                              rosas=tot(lambda e, x: x["flag"] == 5), origens_notas={o: sum(e["origin"] == o for e in entries) for o in orig},
                              origens_cards={o: sum(len(e["cards"]) for e in entries if e["origin"] == o) for o in orig})
        plan["selection_hash"] = B.h([(e["key"], e["fields_hash"], e["cards"]) for e in entries])
        problems = []
        for e in entries:
            n = A("notesInfo", notes=[nid_of[e["key"]]])[0]
            if any(n["fields"][k]["value"] != v for k, v in e["fields"].items()): problems.append(f"campos {e['key']}")
            if set(n["tags"]) != set(e["tags"]): problems.append(f"tags {e['key']}")
            for c in A("cardsInfo", cards=n["cards"]):
                if c["flags"] != next(x["flag"] for x in e["cards"] if x["ord"] == c["ord"]): problems.append(f"flag {e['key']}")
        live = len(A("findCards", query=f'"deck:{plan["deck"]}"'))
        rec.update(notes=[{"key": e["key"], "nid": nid_of[e["key"]]} for e in entries], cards_new_lesson=live, expected=plan["totais"]["cards"], problems=problems)
        (HERE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1)); (HERE / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
        print(json.dumps(plan["totais"], ensure_ascii=False), "vivos:", live, "problemas:", problems)
        if problems or live != plan["totais"]["cards"]: raise SystemExit("readback divergente")


if __name__ == "__main__":
    main()
