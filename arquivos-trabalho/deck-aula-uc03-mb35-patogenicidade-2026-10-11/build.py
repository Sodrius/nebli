"""Monta plan.json a partir de spec.py e faz dry-run somente leitura (identidades, clozes/rótulos, mídia, modelos, ordem, créditos)."""
import hashlib, json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1]))
import spec
from nebli import ordem
from nebli.decks import Anki

A = Anki()
M_TEXT = "NEBLI AnKing independente - v3"
# Clones v2: iguais aos v1 já curados, com NEBLI_Comentario ao fim (os v1 não têm o campo; criar clone evita mudar esquema de tipo existente).
CLONES = {"NEBLI Anatomy independente - v2": "NEBLI Anatomy independente - v1",
          "NEBLI Image Occlusion Enhanced+ independente - v2": "NEBLI Image Occlusion Enhanced+ independente - v1",
          "NEBLI AnatoKing independente - v2": "NEBLI UC08 AnatoKing V2 v1"}
M_DOPE, M_IOE, M_AK = CLONES
MODEL = {"text": M_TEXT, "autoral": M_TEXT, "dope": M_DOPE, "bluelink": M_IOE, "anatoking": M_AK, "slideio": M_IOE}
DOPE_EXTRA = ["Origin", "Insertion", "Attachments", "Innervation", "Actions"]
COR = {3: "verde", 4: "azul", 5: "rosa"}
LESSON_TAG = f"NEBLI::{spec.LESSON}"
UC = re.search(r"(?:^|-)uc\d+(?:-|$)", spec.LESSON, re.I)
if not UC:
    raise ValueError(f"LESSON sem identificador de UC: {spec.LESSON}")
UC = UC.group(0).strip("-").lower()
IDENTITY = f"{UC}-{spec.SHORT}"
ORIGIN = {"Anatomy": "Dope", "Image Occlusion Enhanced+": "BlueLink", "AnatoKingOverhaul V2": "AnatoKing"}
CLOZE = re.compile(r"\{\{c(\d+)::((?:(?!\}\}).)*?)(?:::((?:(?!\}\}).)*?))?\}\}", re.S)
KHAN = re.compile(r"(<br>\s*)*<div>\s*<a[^>]*khanacademy[^>]*>.*?</a>\s*(<br>)?\s*</div>|(<br>\s*)*<a[^>]*(khanacademy|youtu)[^>]*>.*?</a>", re.I | re.S)
WHITE = re.compile(r'\s*style="color: rgb\(255 255 255[^"]*"')
CREDIT = re.compile(r"(?:\s*<br\s*/?>\s*)*(?:<(?:em|span|i|div)[^>]*>\s*)*(?:Photo credit|Image credit|Image licensed|Image\(s\) provided)[\s\S]*?(?=<img|\Z)", re.I)


def h(x): return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]
def clozes(t): return sorted({int(n) for n in re.findall(r"\{\{c(\d+)::", t)})
def uncloze(t, nums): return CLOZE.sub(lambda m: m.group(2) if int(m.group(1)) in nums else m.group(0), t)


CREDIT2 = re.compile(r"(?:\s*<br\s*/?>\s*)*<(em|i|span)\b[^>]*>(?:(?!</\1>)[\s\S])*?(?:Wikimedia Commons|Public domain|CC BY)(?:(?!</\1>)[\s\S])*?</\1>", re.I)


def strip_credit(extra):
    removed = [re.sub(r"<[^>]+>", "", m.group(0)).strip() for m in CREDIT.finditer(extra)] + [re.sub(r"<[^>]+>", "", m.group(0)).strip() for m in CREDIT2.finditer(CREDIT.sub("", extra))]
    extra = CREDIT2.sub("", CREDIT.sub("", extra))
    return re.sub(r"(?:\s*<br\s*/?>\s*)+$", "", CREDIT.sub("", extra)).strip(), removed


def fields_of(model):
    return A("modelFieldNames", modelName=CLONES.get(model, model)) + (["NEBLI_Comentario"] if model in CLONES else [])


def build():
    issues, entries = [], []
    info = {n["noteId"]: n for n in A("notesInfo", notes=[c["src"] for c in spec.CARDS if c.get("src")]) if n}
    if any(c.get("origin") == "Dope" or c["kind"] == "dope" for c in spec.CARDS) and not all(c.get("sem_alternativa") for c in spec.CARDS if c.get("origin") == "Dope" or c["kind"] == "dope"): issues.append("Dope sem justificativa")
    from nebli import slide_io
    made = slide_io.build(HERE, "fontes/slides.pdf", f"nebli-{IDENTITY}", [c for c in spec.CARDS if c["kind"] == "slideio"])
    for m in made.values(): spec.MEDIA.update(m["media"])
    cards_in_order = sorted(spec.CARDS, key=lambda c: ordem.slide(c["evid"]))  # ordem estrita dos slides (sort estável)
    shared = {}
    for order, c in enumerate(cards_in_order, 1):
        if c["kind"] == "compartilhado":
            if not A("notesInfo", notes=[c["nid"]])[0]: issues.append(f"compartilhado ausente {c['nid']}")
            shared[str(c["nid"])] = {"motivo": c["motivo"], "cor": c["cor"], "order": order, "ordem_tag": ordem.tag(spec.SHORT, order), "bloco": c["bloco"],
                                    "alvo": c["alvo"], "evid": c["evid"]}
            continue
        kind, model = c["kind"], MODEL[c["kind"]]
        tf = fields_of(model); fields = {f: "" for f in tf}
        if "NEBLI_Comentario" not in tf: issues.append(f"{model} sem NEBLI_Comentario")
        tags = [LESSON_TAG, "NEBLI::escopo::aula", f"NEBLI::objetivo::{c['bloco']}", ordem.tag(spec.SHORT, order), f"NEBLI::run::{spec.RUN_ID}"]
        src = c.get("src"); base = None; removed = []
        if src:
            n = info.get(src)
            if not n: issues.append(f"fonte ausente {src}"); continue
            base = {k: v["value"] for k, v in n["fields"].items()}
            origin = c.get("origin") or ORIGIN.get(n["modelName"], "AnKing")
            if kind == "text":
                fields["Text"] = base["Text"]
                fields["Extra"], removed = strip_credit(WHITE.sub("", KHAN.sub("", base.get("Extra", ""))))
                if c.get("uncloze"): fields["Text"] = uncloze(fields["Text"], set(c["uncloze"]))
                if c.get("manter"):  # nota original do acervo: só os clozes do plano ficam (F-20261003-CLAUDE-13)
                    fields["Text"] = uncloze(fields["Text"], set(clozes(fields["Text"])) - set(c["flags"]))
            else:
                for k in tf:
                    if k in base and k != "ankihub_id": fields[k] = base[k]
            tags = n["tags"] + tags + [f"NEBLI::source::nid-{src}"]
            if A("findNotes", query=f'"tag:NEBLI::source::nid-{src}"'): issues.append(f"cópia NEBLI viva já existe para {src}")
        elif kind == "slideio":
            origin = "Slide"; fields.update(made[c["key"]]["fields"]); tags.append(f"NEBLI::slideio::{IDENTITY}-{c['key']}")
            cards = [{"n": 1, "ord": 0, "flag": c["flags"][1]}]
        else:
            origin = "Autoral"; tags.append(f"NEBLI::author::{IDENTITY}-{c['key']}")
            if A("findNotes", query=f'"tag:NEBLI::author::{IDENTITY}-{c["key"]}"'): issues.append(f"autoral já existe {c['key']}")
            if len(c.get("espelhos", [])) < 2: issues.append(f"{c['key']}: menos de 2 espelhos")
        tags.append(f"NEBLI::origem::{origin}")
        if "text" in c: fields["Text"] = c["text"]
        if "extra" in c: fields["Extra"] = c["extra"]
        if c.get("extra_add"): fields["Extra"] = (fields["Extra"] + "<br><br>" if fields["Extra"] else "") + c["extra_add"]  # figura de livro/AnKing (F-15)
        for k, v in c.get("fields_override", {}).items(): fields[k] = v
        if kind in ("text", "autoral", "anatoking"):
            want, got = sorted(c["flags"]), clozes(fields["Text"])
            if got != want: issues.append(f"{c['key']}: clozes {got} != plano {want}")
            cards = [{"n": k, "ord": k - 1, "flag": v} for k, v in sorted(c["flags"].items())]
            if kind == "anatoking" and not re.sub(r"<[^>]+>|&nbsp;|\s", "", fields["Header"]): fields["Header"] = "ID structure"
        elif kind == "dope":
            for i in range(1, 21):
                if i not in c["labels"]: fields[f"{i}a"] = ""
                elif not fields[f"{i}a"].strip(): issues.append(f"{c['key']}: rótulo {i}a vazio")
            for k in DOPE_EXTRA: fields[k] = ""
            if c.get("clinical_new"): fields["Clinical"] = c["clinical_new"]
            cards = [{"n": k, "ord": k - 1, "flag": v} for k, v in sorted(c["labels"].items())]
        elif kind == "bluelink":
            fields["ID (hidden)"] = f"nebli-{IDENTITY}-" + re.sub(r"<[^>]+>", "", base["ID (hidden)"])
            fields["Remarks"] = c.get("remarks", "")
            if fields.get("Sources"): removed = [re.sub(r"<[^>]+>", " ", fields["Sources"]).strip()[:120]]; fields["Sources"] = ""  # crédito fora do card; origem fica no plano
            cards = [{"n": 1, "ord": 0, "flag": c["flags"][1]}]
        allf = " ".join(fields.values())
        if re.search(r"photo credit|image credit|licensed by|wikimedia commons|public domain|CC BY", allf, re.I): issues.append(f"{c['key']}: crédito visível restante")
        for im in re.findall(r'src="([^"]+)"', allf):
            if im in spec.MEDIA: continue
            if not A("retrieveMediaFile", filename=im): issues.append(f"{c['key']}: mídia ausente {im}")
        if not str(c["evid"]).startswith("Slide "): issues.append(f"{c['key']}: evid sem slide")
        for x in cards: x["cor"] = COR[x["flag"]]
        tags += [f"NEBLI::cor::{spec.LESSON}::{x}" for x in sorted({x["cor"] for x in cards})]
        if all(x["flag"] == 5 for x in cards): tags.append("NEBLI::lateral")
        e = {k: v for k, v in c.items() if k not in ("text", "extra", "clinical_new", "remarks", "fields_override", "lines", "rects", "mask_rects", "search")}
        if kind == "slideio": e.update(rotulo=made[c["key"]]["rotulo"], parcial=made[c["key"]]["parcial"])
        e.update(order=order, origin=origin, model=model, tags=sorted(set(tags)), fields=fields, fields_hash=h(fields), cards=cards,
                 source_fields_hash=h(base) if base else None, credito_removido=removed,
                 hy=next((t.split("::")[-1][:1] for t in (info[src]["tags"] if src else []) if "Low/HighYield" in t), None))
        entries.append(e)
    for f in spec.MEDIA.values():
        if not (HERE / f).exists(): issues.append(f"mídia local ausente {f}")
    keys = [c["key"] for c in spec.CARDS if c["kind"] != "compartilhado"]
    issues = [i for i in issues if "já existe" not in i and "já usado" not in i] if "--delta" in sys.argv else issues
    if len(set(keys)) != len(keys): issues.append("chave repetida")
    if A("findNotes", query=f'"tag:NEBLI::ordem::{spec.SHORT}-*"'): issues.append(f"prefixo de ordem '{spec.SHORT}' já usado")
    # HY do recorte precisa de pelo menos um card verde (MEMORY, Q048)
    for e in entries:
        if e["hy"] in ("1", "2") and e["origin"] == "AnKing" and not e.get("hy_repete") and not e.get("clinica_lateral") and not any(x["flag"] == 3 for x in e["cards"]): issues.append(f"{e['key']}: HY {e['hy']} sem verde")
    tot = lambda f: sum(1 for e in entries for x in e["cards"] if f(e, x))
    origens = sorted({e["origin"] for e in entries})
    scope_file = next((HERE / name for name in ("fontes.json", "fontes-decl.json") if (HERE / name).exists()), None)
    source_scope = json.loads(scope_file.read_text()).get("escopo", "cards") if scope_file else "cards"
    plan = {"run_id": spec.RUN_ID, "short": spec.SHORT, "lesson_id": spec.LESSON, "deck": spec.DECK, "criterios": spec.CRITERIOS,
            "E1": "solicitada junto ao deck" if source_scope == "e1+cards" else "não solicitada nesta corrida", "entries": entries, "compartilhados": shared,
            "excluidos": [{"nid": n, "motivo": m} for n, m in spec.EXCLUIDOS], "fora_do_recorte": spec.FORA_DO_RECORTE, "media": spec.MEDIA,
            "clones": CLONES, "busca_externos": "busca/ext.txt", "busca_externos": "busca/ext.txt",
            "totais": {"notas": len(entries), "cards": tot(lambda e, x: True), "verdes": tot(lambda e, x: x["flag"] == 3),
                       "azuis": tot(lambda e, x: x["flag"] == 4), "rosas": tot(lambda e, x: x["flag"] == 5),
                       "origens_notas": {o: sum(e["origin"] == o for e in entries) for o in origens},
                       "origens_cards": {o: sum(len(e["cards"]) for e in entries if e["origin"] == o) for o in origens},
                       "compartilhados_associados": len(shared), "creditos_removidos": sum(bool(e["credito_removido"]) for e in entries)}}
    plan["selection_hash"] = h([(e["key"], e["fields_hash"], e["cards"]) for e in entries])
    return plan, issues


if __name__ == "__main__":
    plan, issues = build()
    if (HERE / "plan.json").exists():  # preserva busca das oclusões gravada por nebli.io_busca fora do spec (F-15)
        prev = {e["key"]: e for e in json.loads((HERE / "plan.json").read_text())["entries"]}
        for e in plan["entries"]:
            for k in ("busca", "busca_decisao", "duplicacao_ok"):
                if prev.get(e["key"], {}).get(k) and not e.get(k): e[k] = prev[e["key"]][k]
    (HERE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
    print(json.dumps(plan["totais"], ensure_ascii=False), plan["selection_hash"])
    print("ISSUES:", issues or "nenhuma")
    if issues and not ("--delta" in sys.argv and all("já usado" in i or "já existe" in i for i in issues)):
        sys.exit(1)  # nunca aplicar plano com pendência (02/10: update interrompido no meio por cloze divergente)
    print("HY×cor:", [(e["key"], e["hy"], [x["cor"] for x in e["cards"]]) for e in plan["entries"] if e["hy"]])
