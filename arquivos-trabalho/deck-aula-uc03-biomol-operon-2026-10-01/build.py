"""Monta plan.json a partir de spec.py e faz dry-run somente leitura (identidades, clozes, mídia, modelo)."""
import hashlib, json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1]))
import spec
from nebli.decks import Anki

A = Anki()
MODEL = "NEBLI AnKing independente - v3"
COR = {3: "verde", 4: "azul", 5: "rosa"}
LESSON_TAG = f"NEBLI::{spec.LESSON}"
CLOZE = re.compile(r"\{\{c(\d+)::((?:(?!\}\}).)*?)(?:::((?:(?!\}\}).)*?))?\}\}", re.S)
KHAN = re.compile(r"(<br>\s*)*<div>\s*<a[^>]*khanacademy[^>]*>.*?</a>\s*(<br>)?\s*</div>|(<br>\s*)*<a[^>]*(khanacademy|youtu)[^>]*>.*?</a>", re.I | re.S)
BADCREDIT = re.compile(r'<a href=",%20.*?">OpenStax</a>', re.S)
WHITE = re.compile(r'\s*style="color: rgb\(255 255 255[^"]*"')


def h(x): return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]
def clozes(t): return sorted({int(n) for n in re.findall(r"\{\{c(\d+)::", t)})
def uncloze(t, nums): return CLOZE.sub(lambda m: m.group(2) if int(m.group(1)) in nums else m.group(0), t)


def build():
    issues, entries = [], []
    tf = A("modelFieldNames", modelName=MODEL)
    if "NEBLI_Comentario" not in tf: issues.append("modelo sem NEBLI_Comentario")
    info = {n["noteId"]: n for n in A("notesInfo", notes=[c["src"] for c in spec.CARDS if c.get("src")]) if n}
    for order, c in enumerate(spec.CARDS, 1):
        fields = {f: "" for f in tf}
        tags = [LESSON_TAG, "NEBLI::escopo::aula", f"NEBLI::objetivo::{c['bloco']}", f"NEBLI::ordem::{spec.SHORT}-{order:02d}",
                f"NEBLI::run::{spec.RUN_ID}"]
        src = c.get("src"); base = None
        if src:
            n = info.get(src)
            if not n: issues.append(f"fonte ausente {src}"); continue
            base = {k: v["value"] for k, v in n["fields"].items()}
            origin = c.get("origin", "AnKing")
            fields["Text"] = base["Text"]
            fields["Extra"] = BADCREDIT.sub("OpenStax", WHITE.sub("", KHAN.sub("", base["Extra"]))).strip()
            if c.get("uncloze"): fields["Text"] = uncloze(fields["Text"], set(c["uncloze"]))
            tags = n["tags"] + tags + [f"NEBLI::source::nid-{src}"]
            if A("findNotes", query=f'"tag:NEBLI::source::nid-{src}"'): issues.append(f"cópia NEBLI viva já existe para {src}")
        else:
            origin = "Autoral"; fields["Text"], fields["Extra"] = c["text"], c["extra"]
            tags.append(f"NEBLI::author::uc03-{spec.SHORT}-{c['key']}")
            if A("findNotes", query=f'"tag:NEBLI::author::uc03-{spec.SHORT}-{c["key"]}"'): issues.append(f"autoral já existe {c['key']}")
        tags.append(f"NEBLI::origem::{origin}")
        got, want = clozes(fields["Text"]), sorted(c["flags"])
        if got != want: issues.append(f"{c['key']}: clozes {got} != plano {want}")
        cards = [{"n": k, "ord": k - 1, "flag": v, "cor": COR[v]} for k, v in sorted(c["flags"].items())]
        tags += [f"NEBLI::cor::{spec.LESSON}::{x}" for x in sorted({x["cor"] for x in cards})]
        if all(x["flag"] == 5 for x in cards): tags.append("NEBLI::lateral")
        for img in re.findall(r'src="([^"]+)"', fields["Text"] + fields["Extra"]):
            if img in spec.MEDIA: continue
            if not A("retrieveMediaFile", filename=img): issues.append(f"{c['key']}: mídia ausente {img}")
        e = {k: v for k, v in c.items() if k not in ("text", "extra")}
        e.update(order=order, origin=origin, model=MODEL, tags=sorted(set(tags)), fields=fields, fields_hash=h(fields), cards=cards,
                 source_fields_hash=h(base) if base else None)
        entries.append(e)
    for f in spec.MEDIA.values():
        if not (HERE / f).exists(): issues.append(f"mídia local ausente {f}")
    for nid in spec.COMPARTILHADOS:
        if not A("notesInfo", notes=[nid])[0]: issues.append(f"compartilhado ausente {nid}")
    keys = [c["key"] for c in spec.CARDS]
    if len(set(keys)) != len(keys): issues.append("chave repetida")
    tot = lambda f: sum(1 for e in entries for x in e["cards"] if f(e, x))
    origens = sorted({e["origin"] for e in entries})
    plan = {"run_id": spec.RUN_ID, "short": spec.SHORT, "lesson_id": spec.LESSON, "deck": spec.DECK, "criterios": spec.CRITERIOS,
            "E1": "não incluída nesta corrida — pedido de 01/10 é o deck de cards", "entries": entries,
            "compartilhados": {str(k): {"motivo": v[0], "cor": v[1]} for k, v in spec.COMPARTILHADOS.items()},
            "excluidos": [{"nid": n, "motivo": m} for n, m in spec.EXCLUIDOS], "fora_do_recorte": spec.FORA_DO_RECORTE,
            "media": spec.MEDIA,
            "totais": {"notas": len(entries), "cards": tot(lambda e, x: True), "verdes": tot(lambda e, x: x["flag"] == 3),
                       "azuis": tot(lambda e, x: x["flag"] == 4), "rosas": tot(lambda e, x: x["flag"] == 5),
                       "origens_notas": {o: sum(e["origin"] == o for e in entries) for o in origens},
                       "origens_cards": {o: sum(len(e["cards"]) for e in entries if e["origin"] == o) for o in origens},
                       "compartilhados_associados": len(spec.COMPARTILHADOS)}}
    plan["selection_hash"] = h([(e["key"], e["fields_hash"], e["cards"]) for e in entries])
    return plan, issues


if __name__ == "__main__":
    plan, issues = build()
    (HERE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
    print(json.dumps(plan["totais"], ensure_ascii=False), plan["selection_hash"])
    print("ISSUES:", issues or "nenhuma")
    print("deck existe:", spec.DECK in [re.sub(r" \(\d+\)", "", d) for d in A("deckNames")])
