"""Bandeira rosa (5) = card muito lateral (Davi, 30/09: "garante que detalhe possa ser cards, só nao vire quando
realmente não vale a pena. vamos criar uma bandeira rosa para cards muuuuito laterais, tipo esses que foram
excluídos"; escolheu aplicar já na Imuno). Recoloca como rosa os autorais retirados por serem detalhe (não os que
só repetiam AnKing) e copia como rosa os AnKing laterais antes excluídos. Nenhum desses tinha estudo.
Uso: python3 adicionar_rosas.py [--aplicar]
"""
import json, re, sys
from datetime import datetime
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita
from nebli.lint_cards import check

MODEL = "NEBLI AnKing independente - v3"
COMP = ("NEBLI::UC03::P2::Imunologia::Sistema complemento", "NEBLI::2026-uc03-imunologia-31-sistema-complemento")
INFL = ("NEBLI::UC03::P2::Imunologia::Inflamação: início e resolução", "NEBLI::2026-uc03-imunologia-37-inflamacao-inicio-resolucao")
BAD_IMG = ("8f4ce0ed345e5153fbff4de0c723fa52.webp", "a77c863c3f99e7fd03c5b5fe248eefdb.webp")  # esquemas com erro
RESOURCE = {"Sketchy", "Sketchy 2", "Sketchy Extra", "Bootcamp", "Pixorize", "Physeo", "OME", "Picmonic",
            "Additional Resources", "Boards and Beyond", "Pathoma", "First Aid", "ankihub_id", "One by one"}
RUN = "NEBLI::run::uc03-imuno-rosa-20260930"
ROSA = 5

# Autorais retirados por serem detalhe (voltam rosa, Extra vazio: o porquê fica no Tab)
AUTORAIS = [1790781880793, 1790781883117, 1790781885393, 1790781885593, 1790806713995, 1790806714143,
            1790806714292, 1790806714567, 1790806714718, 1790781920189, 1790781920414, 1790781920992]
# AnKing laterais antes excluídos
ANKING = {
    COMP: [1478995034893, 1478995016809, 1478995007169, 1478995013918, 1478995020091, 1478995028457,
           1478995038587, 1478995055944, 1478995063743, 1478995072125, 1478995078338, 1497203766572,
           1497203670771, 1578248124988, 1517365303958, 1578248499297],
    INFL: [1520905749524, 1520906298520, 1520906322080, 1520906371581, 1487642668958, 1487642671204,
           1487642687838, 1487642693791, 1487642705376, 1487642630321, 1487642640045, 1581896116295,
           1487642595787, 1552605404493, 1487642791049, 1463883801028, 1582068541475, 1520444212406,
           1520444263822, 1520444509518, 1520444679068, 1520445197524, 1587591432462, 1487550504664,
           1474580768287],
}


def strip_bad(value):
    for img in BAD_IMG:
        value = re.sub(rf'<img[^>]*{re.escape(img)}[^>]*>', "", value)
    return value


def plan(A):
    snap = json.loads(sorted(HERE.glob("reducao-autorais-before-*.json"))[-1].read_text())
    old = {n["noteId"]: n for n in snap["notas"]}
    target = A("modelFieldNames", modelName=MODEL)
    notes, problems = [], []
    for nid in AUTORAIS:
        n = old[nid]
        lesson = COMP if COMP[1] in n["tags"] else INFL
        fields = {k: "" for k in target}
        fields["Text"] = n["fields"]["Text"]["value"]
        hard = [m for lvl, m in check(nid, fields["Text"]) if lvl == "dura"]
        if hard:
            problems.append(f"autoral {nid}: {hard}")
        tags = sorted(set(n["tags"]) | {RUN, "NEBLI::lateral"})
        notes.append({"deckName": lesson[0], "modelName": MODEL, "fields": fields, "tags": tags, "_src": f"autoral {nid}"})
    for lesson, srcs in ANKING.items():
        for src, n in zip(srcs, A("notesInfo", notes=srcs)):
            if A("findNotes", query=f'"tag:NEBLI::source::nid-{src}"'):
                problems.append(f"cópia viva já existe {src}"); continue
            fields = {k: ("" if k in RESOURCE else strip_bad(n["fields"].get(k, {}).get("value", ""))) for k in target}
            tags = sorted(set(n["tags"]) | {lesson[1], "NEBLI::escopo::aula", "NEBLI::origem::AnKing", "NEBLI::lateral",
                                            f"NEBLI::source::nid-{src}", RUN})
            notes.append({"deckName": lesson[0], "modelName": MODEL, "fields": fields, "tags": tags, "_src": f"AnKing {src}"})
    return notes, problems


def main(apply):
    A = Anki()
    notes, problems = plan(A)
    print(f"{len(notes)} notas rosa a criar ({sum(n['_src'].startswith('autoral') for n in notes)} autorais, "
          f"{sum(n['_src'].startswith('AnKing') for n in notes)} AnKing). Problemas: {problems or 'nenhum'}")
    if problems or not apply:
        return
    (HERE / f"rosas-plano-{datetime.now():%H%M%S}.json").write_text(json.dumps(notes, ensure_ascii=False, indent=1))
    created = []
    with escrita(A, "Imuno P2: cards laterais com bandeira rosa"):
        for n in notes:
            nid = A("addNote", note={k: v for k, v in n.items() if k != "_src"} | {"options": {"allowDuplicate": True}})
            cids = A("findCards", query=f"nid:{nid}")
            for cid in cids:
                A("setSpecificValueOfCard", card=cid, keys=["flags"], newValues=[ROSA], warning_check=True)
            created.append({"src": n["_src"], "nid": nid, "cards": cids})
    info = A("cardsInfo", cards=[c for x in created for c in x["cards"]])
    wrong = [c["cardId"] for c in info if c["flags"] != ROSA or c["queue"] == -1]
    receipt = {"notas": len(created), "cards": len(info), "fora_do_padrao": wrong, "criadas": created}
    (HERE / "rosas-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=1))
    print({k: receipt[k] for k in ("notas", "cards", "fora_do_padrao")})


if __name__ == "__main__":
    main("--aplicar" in sys.argv)
