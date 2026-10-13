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
REMOVE = {"agua-nao-agitada": "rosa redundante com o card AnKing das micelas; autoria deve ser minoria"}
REWRITE = {
 "enac": (f"In the <b>colon</b>, aldosterone increases {Na} absorption by upregulating {{{{c1::<b>ENaC</b>}}}} channels", None,
          "Aires cap. 63: a aldosterona aumenta ENaC e Na+/K+-ATPase no cólon; liga o canal ao hormônio."),
 "porta": ("Absorbed <b>monosaccharides</b> and <b>amino acids</b> enter the {{c1::portal}} circulation, whereas lipids enter the lymph", None,
           "Tirada a pista 'travel to the liver'; o contraste portal × linfa fica na frente."),
 "pepsina-fracao": (None, "Not essential for protein digestion<br><br>__IMG__", "Aires cap. 62: a ação proteolítica da pepsina não é essencial."),
}
RECOLOR = {"k-colon": {1: 4, 2: 4}}  # Aires cap. 63 trata a secreção de K+ no cólon: azul
ADD = [  # (depois de qual chave, entrada)
 ("sglt1", dict(key="sglt-ativo-secundario", src=1474922383133, flags={1: 3}, bloco="B-carboidratos", evid="Slide 4", alvo="Cotransporte Na+/glicose é transporte ativo secundário",
                motivo="Verde: Aires e as aulas dos canais insistem no nome do mecanismo.")),
 ("pepsina-fracao", dict(key="cck-celulas-i", src=1482021827543, flags={4: 3, 1: 4}, uncloze=[2], bloco="C-proteinas", evid="Slide 5", alvo="CCK vem das células I do duodeno e jejuno",
                         motivo="c4 verde (hormônio), c1 azul (célula). Hormônios: lacuna apontada por Davi.")),
 ("cck-enzimas", dict(key="secretina-hco3", src=1482115326502, flags={1: 3}, bloco="C-proteinas", evid="Slide 5", alvo="Secretina libera o componente aquoso (HCO3-) do suco pancreático",
                      motivo="Verde: par da CCK; sem bicarbonato as enzimas pancreáticas não funcionam (Aires cap. 62).")),
 ("secretina-hco3", dict(key="secretina-celulas-s", src=1482021883479, flags={3: 4}, uncloze=[1, 2], bloco="C-proteinas", evid="Slide 5", alvo="Secretina vem das células S do duodeno",
                         motivo="Azul.")),
 ("secretina-celulas-s", dict(key="secretina-estimulo", src=1482021911657, flags={1: 4}, bloco="C-proteinas", evid="Slide 5", alvo="H+ e ácidos graxos no duodeno estimulam a secretina",
                              motivo="Azul.")),
 ("cck-bile", dict(key="gip-nutrientes", src=1482021928703, flags={1: 4}, bloco="D-lipidios", evid="Slide 6", alvo="Glicose, gordura e proteína estimulam o GIP",
                   motivo="Azul: Aires cita o GIP liberado pelos produtos da lipólise, retardando o esvaziamento gástrico.")),
 ("micelas-borda", dict(key="sais-biliares-ileo", src=1482115382071, flags={1: 3}, bloco="D-lipidios", evid="Slide 6", alvo="Sais biliares são reabsorvidos no íleo terminal",
                        motivo="Verde: fecha o ciclo das micelas (circulação êntero-hepática, Aires cap. 62).")),
]


def main():
    tf = A("modelFieldNames", modelName=B.MODEL)
    with escrita(A, f"FI05 {plan['run_id']} delta2"):
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
                                           f"NEBLI::source::nid-{s['src']}", "NEBLI::origem::AnKing"] + [f"NEBLI::cor::{LESSON}::{c['cor']}" for c in cards]))
            e = dict(s, kind="text", flags={str(k): v for k, v in s["flags"].items()}, origin="AnKing", model=B.MODEL, tags=tags, fields=fields,
                     fields_hash=B.h(fields), cards=cards, source_fields_hash=B.h(base), credito_removido=removed, acrescentado="delta2: Aires + canais")
            new = existing[0] if existing else A("addNote", note={"deckName": plan["deck"], "modelName": B.MODEL, "fields": fields, "tags": tags, "options": {"allowDuplicate": True}})
            for c in A("cardsInfo", cards=A("findCards", query=f"nid:{new}")):
                A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[next(x["flag"] for x in cards if x["ord"] == c["ord"])], warning_check=True)
            nid_of[s["key"]] = new
            i = next(i for i, x in enumerate(entries) if x["key"] == after); entries.insert(i + 1, e)
        # reordenar: entradas e compartilhadas numa só sequência
        seq = [("e", e) for e in entries]
        for nid, s in sorted(plan["compartilhados"].items(), key=lambda kv: kv[1]["order"]):
            pos = next((i for i, (t, x) in enumerate(seq) if t == "e" and "acrescentado" not in x and x["order"] > s["order"]), len(seq))
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
