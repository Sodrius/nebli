"""Monta plan.json a partir de spec.py e faz dry-run somente leitura (identidades, clozes/rótulos, mídia, modelos)."""
import hashlib, json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1]))
import spec
from nebli.decks import Anki

A = Anki()
M_TEXT = "NEBLI AnKing independente - v3"
M_DOPE = "NEBLI Anatomy independente - v1"
M_IOE = "NEBLI Image Occlusion Enhanced+ independente - v1"
M_AK = "NEBLI UC08 AnatoKing V2 v1"
MODEL = {"text": M_TEXT, "autoral": M_TEXT, "dope": M_DOPE, "bluelink": M_IOE, "anatoking": M_AK}
RESOURCE = {"Sketchy", "Sketchy 2", "Sketchy Extra", "Bootcamp", "Pixorize", "Physeo", "OME", "Picmonic",
            "Additional Resources", "Boards and Beyond", "Pathoma", "First Aid", "ankihub_id", "One by one"}
DOPE_EXTRA = ["Origin", "Insertion", "Attachments", "Innervation", "Actions"]
LESSON_TAG = f"NEBLI::{spec.LESSON}"
ORIGIN = {"Cloze-b12d6": "Dorian", "Cloze deletion": "Dope", "Anatomy": "Dope", "Image Occlusion Enhanced+": "BlueLink",
          "AnatoKingOverhaul V2": "AnatoKing"}


def h(x): return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]
def clozes(t): return sorted({int(n) for n in re.findall(r"\{\{c(\d+)::", t)})


def fields_of(model):
    try: return A("modelFieldNames", modelName=model)
    except Exception:
        return A("modelFieldNames", modelName="Image Occlusion Enhanced+") if model == M_IOE else None


def build():
    issues, entries = [], []
    info = {n["noteId"]: n for n in A("notesInfo", notes=[c["src"] for c in spec.CARDS if c.get("src")])}
    for order, c in enumerate(spec.CARDS, 1):
        kind, model = c["kind"], MODEL[c["kind"]]
        tf = fields_of(model); fields = {f: "" for f in tf}
        tags = [LESSON_TAG, "NEBLI::escopo::aula", f"NEBLI::objetivo::{c['bloco']}", f"NEBLI::ordem::{spec.SHORT}-{order:02d}"]
        src = c.get("src"); base = None
        if src:
            n = info.get(src)
            if not n: issues.append(f"fonte ausente {src}"); continue
            base = {k: v["value"] for k, v in n["fields"].items()}
            origin = c.get("origin") or ORIGIN.get(n["modelName"], "AnKing")
            for k in tf:
                if k in base and k not in RESOURCE: fields[k] = base[k]
            tags = n["tags"] + tags + [f"NEBLI::source::nid-{src}"]
            if A("findNotes", query=f'"tag:NEBLI::source::nid-{src}"'): issues.append(f"cópia NEBLI viva já existe para {src}")
            if n["modelName"] in ("Cloze-b12d6", "Cloze deletion"):
                fields["Text"], fields["Extra"] = base.get("Text", ""), base.get("Extra", "")
        else:
            origin = "Autoral"; tags.append(f"NEBLI::author::uc08-{spec.SHORT}-{c['key']}")
            if A("findNotes", query=f'"tag:NEBLI::author::uc08-{spec.SHORT}-{c["key"]}"'): issues.append(f"autoral já existe {c['key']}")
        tags.append(f"NEBLI::origem::{origin}")
        if "text" in c: fields["Text"] = c["text"]
        if "extra" in c: fields["Extra"] = c["extra"]
        for k, v in c.get("fields_override", {}).items(): fields[k] = v
        if "extra_prefix" in c: fields["Extra"] = c["extra_prefix"] + fields["Extra"]
        if kind in ("text", "autoral", "anatoking"):
            want = sorted(c["flags"])
            got = clozes(fields["Text"])
            if got != want: issues.append(f"{c['key']}: clozes {got} != plano {want}")
            cards = [{"n": k, "ord": k - 1, "flag": v} for k, v in sorted(c["flags"].items())]
            if kind == "anatoking" and not re.sub(r"<[^>]+>|&nbsp;|\s", "", fields["Header"]):
                fields["Header"] = "ID structure"
        elif kind == "dope":
            for i in range(1, 21):
                if i not in c["labels"]: fields[f"{i}a"] = ""
                elif not fields[f"{i}a"].strip(): issues.append(f"{c['key']}: rótulo {i}a vazio")
            for k in DOPE_EXTRA: fields[k] = ""
            if c.get("clinical_new"): fields["Clinical"] = c["clinical_new"]
            cards = [{"n": k, "ord": k - 1, "flag": v} for k, v in sorted(c["labels"].items())]
        elif kind == "bluelink":
            fields["ID (hidden)"] = f"nebli-{spec.SHORT}-" + re.sub(r"<[^>]+>", "", base["ID (hidden)"])
            fields["Remarks"] = c.get("remarks", "")
            cards = [{"n": 1, "ord": 0, "flag": c["flags"][1]}]
        for img in re.findall(r'src="([^"]+)"', " ".join(fields.values())):
            if img in spec.MEDIA: continue
            if not A("retrieveMediaFile", filename=img): issues.append(f"{c['key']}: mídia ausente {img}")
        for x in cards: x["cor"] = {3: "verde", 4: "azul"}[x["flag"]]
        e = {k: v for k, v in c.items() if k not in ("text", "extra", "extra_prefix", "clinical_new", "remarks", "fields_override")}
        e.update(order=order, origin=origin, model=model, tags=sorted(set(tags)), fields=fields, fields_hash=h(fields), cards=cards,
                 source_fields_hash=h(base) if base else None)
        entries.append(e)
    for f in spec.MEDIA.values():
        if not (HERE / f).exists(): issues.append(f"mídia local ausente {f}")
    for nid in spec.COMPARTILHADOS:
        if not A("notesInfo", notes=[nid])[0]: issues.append(f"compartilhado ausente {nid}")
    tot = lambda f: sum(1 for e in entries for x in e["cards"] if f(e, x))
    plan = {"run_id": spec.RUN_ID, "short": spec.SHORT, "lesson_id": spec.LESSON, "deck": spec.DECK, "criterios": spec.CRITERIOS,
            "E1": "não aplicável — pedido explícito (UC08 só cards)", "entries": entries,
            "compartilhados": {str(k): v for k, v in spec.COMPARTILHADOS.items()},
            "excluidos": [{"nid": n, "motivo": m} for n, m in spec.EXCLUIDOS], "fora_do_recorte": spec.FORA_DO_RECORTE,
            "media": spec.MEDIA,
            "totais": {"notas": len(entries), "cards": tot(lambda e, x: True), "verdes": tot(lambda e, x: x["flag"] == 3),
                       "azuis": tot(lambda e, x: x["flag"] == 4), "autorais": sum(e["origin"] == "Autoral" for e in entries),
                       "origens_notas": {o: sum(e["origin"] == o for e in entries) for o in sorted({e["origin"] for e in entries})},
                       "origens_cards": {o: sum(len(e["cards"]) for e in entries if e["origin"] == o) for o in sorted({e["origin"] for e in entries})},
                       "compartilhados_associados": len(spec.COMPARTILHADOS)}}
    plan["selection_hash"] = h([(e["key"], e["fields_hash"], e["cards"]) for e in entries])
    return plan, issues


if __name__ == "__main__":
    plan, issues = build()
    (HERE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
    print(json.dumps(plan["totais"], ensure_ascii=False), plan["selection_hash"])
    print("ISSUES:", issues or "nenhuma")
    print("deck existe:", spec.DECK in [re.sub(r" \(\d+\)", "", d) for d in A("deckNames")])
    print("modelo IOE NEBLI existe:", M_IOE in A("modelNames"))
