"""Monta plan.json e translation-plan.json a partir de spec.py e faz dry-run (somente leitura)."""
import hashlib, json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1]))
import spec
from nebli.decks import Anki

A = Anki()
MODELS = {"AnKing": "NEBLI AnKing independente - v3", "Autoral": "NEBLI AnKing independente - v3",
          "Histology": "NEBLI AnKing independente - v3"}
RESOURCE_FIELDS = {"Sketchy", "Sketchy 2", "Sketchy Extra", "Bootcamp", "Pixorize", "Physeo", "OME", "Picmonic",
                   "Additional Resources", "Boards and Beyond", "Pathoma", "First Aid"}
LESSON_TAG = f"NEBLI::{spec.LESSON}"


def h(x): return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]
def clozes(text): return sorted({int(n) for n in re.findall(r"\{\{c(\d+)::", text)})


def build():
    issues, entries, trans = [], [], []
    srcs = [c["src"] for c in spec.CARDS if c["src"]]
    info = {n["noteId"]: n for n in A("notesInfo", notes=srcs)}
    for order, c in enumerate(spec.CARDS, 1):
        model = MODELS[c["origin"]]
        tfields = A("modelFieldNames", modelName=model)
        fields = {f: "" for f in tfields}
        tags = [LESSON_TAG, "NEBLI::escopo::aula", f"NEBLI::objetivo::{c.get('objetivo', 'lamina-' + str(c['slide']))}", f"NEBLI::origem::{c['origin']}",
                f"NEBLI::ordem::fi08-{order:02d}"]
        base = None
        if c["src"]:
            n = info.get(c["src"])
            if not n: issues.append(f"fonte ausente {c['src']}"); continue
            base = {k: v["value"] for k, v in n["fields"].items()}
            for k in tfields:
                if k in base and k not in RESOURCE_FIELDS and k not in ("ankihub_id",):
                    fields[k] = base[k]
            tags = n["tags"] + tags + [f"NEBLI::source::nid-{c['src']}"]
            if A("findNotes", query=f'"tag:NEBLI::source::nid-{c["src"]}"'):
                issues.append(f"cópia NEBLI viva já existe para {c['src']}")
        else:
            tags.append(f"NEBLI::author::uc08-fi08-{c['key']}")
            if A("findNotes", query=f'"tag:NEBLI::author::uc08-fi08-{c["key"]}"'):
                issues.append(f"autoral já existe {c['key']}")
        fields["Text"], fields["Extra"] = c["text"], c["extra"]
        want = sorted(c["flags"])
        if clozes(c["text"]) != want: issues.append(f"{c['key']}: clozes {clozes(c['text'])} != plano {want}")
        for img in re.findall(r'src="([^"]+)"', c["text"] + c["extra"]):
            if not img.startswith("nebli-") and not A("retrieveMediaFile", filename=img):
                issues.append(f"{c['key']}: mídia ausente {img}")
        e = {k: v for k, v in c.items() if k not in ("text", "extra")}
        e.update(order=order, model=model, tags=sorted(set(tags)), fields_hash=h(fields),
                 cards=[{"cloze": k, "ord": k - 1, "flag": v, "cor": {3: "verde", 4: "azul"}[v]} for k, v in sorted(c["flags"].items())])
        e["fields"] = fields
        entries.append(e)
        trans.append({"key": c["key"], "source_nid": c["src"], "change_kind": ["translation"] + (["curation"] if c["src"] else ["authoring"])
                      + (["didactic_edit"] if c.get("didatico") else []),
                      "en_base": {k: base.get(k, "") for k in ("Text", "Extra")} if base else None,
                      "pt": {"Text": c["text"], "Extra": c["extra"]},
                      "removed_resource_fields": sorted(k for k in RESOURCE_FIELDS if base and base.get(k, "").strip()),
                      "curadoria": c.get("curadoria", ""), "didatico": c.get("didatico", ""),
                      "review": {"semantic": "revisado pelo executor (Claude)", "structure": "clozes conferidos por script",
                                 "visual": "pendente de render após aplicação", "independente": "aguarda revisão Codex"},
                      "state": "reviewed"})
    plan = {"run_id": spec.RUN_ID, "version": getattr(spec, "VERSION", "v1"), "lesson_id": spec.LESSON, "deck": spec.DECK, "criterios": spec.CRITERIOS,
            "E1": "não aplicável — pedido de 29/09", "entries": entries,
            "excluidos": [{"nid": n, "motivo": m} for n, m in spec.EXCLUIDOS],
            "totais": {"notas": len(entries), "cards": sum(len(e["cards"]) for e in entries),
                       "verdes": sum(1 for e in entries for x in e["cards"] if x["flag"] == 3),
                       "azuis": sum(1 for e in entries for x in e["cards"] if x["flag"] == 4),
                       "autorais": sum(1 for e in entries if e["origin"] == "Autoral"),
                       "origens": {o: sum(1 for e in entries if e["origin"] == o) for o in ("AnKing", "Histology", "Autoral")}}}
    plan["selection_hash"] = h([(e["key"], e["fields_hash"], e["cards"]) for e in entries])
    return plan, trans, issues


if __name__ == "__main__":
    plan, trans, issues = build()
    (HERE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
    (HERE / "translation-plan.json").write_text(json.dumps({"run_id": spec.RUN_ID, "glossario": {
        "enteric nervous system": "sistema nervoso entérico (SNE)", "myenteric (Auerbach) plexus": "plexo mioentérico (de Auerbach)",
        "submucosal (Meissner) plexus": "plexo submucoso (de Meissner)", "vagovagal": "vagovagal",
        "LES / UES": "EEI / EES (esfíncter esofágico inferior/superior)", "VIP": "peptídeo intestinal vasoativo (VIP)",
        "MLCK": "cinase da cadeia leve da miosina (MLCK)", "myosin light chain phosphatase": "fosfatase da cadeia leve da miosina",
        "cGMP": "GMPc", "varicosities": "varicosidades", "phasic/tonic": "fásica/tônica"},
        "notes": trans}, ensure_ascii=False, indent=1))
    print(json.dumps(plan["totais"], ensure_ascii=False), plan["selection_hash"])
    print("ISSUES:", issues or "nenhuma")
    print("deck existe:", spec.DECK in [re.sub(r" \(\d+\)", "", d) for d in A("deckNames")])
