"""Monta plan.json a partir de spec.py e faz dry-run somente leitura (identidades, clozes, mídia, modelo, ordem, créditos)."""
import hashlib, json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1]))
import spec
from nebli import ordem
from nebli.decks import Anki

A = Anki()
MODEL = "NEBLI AnKing independente - v3"
COR = {3: "verde", 4: "azul", 5: "rosa"}
LESSON_TAG = f"NEBLI::{spec.LESSON}"
CLOZE = re.compile(r"\{\{c(\d+)::((?:(?!\}\}).)*?)(?:::((?:(?!\}\}).)*?))?\}\}", re.S)
KHAN = re.compile(r"(<br>\s*)*<div>\s*<a[^>]*khanacademy[^>]*>.*?</a>\s*(<br>)?\s*</div>|(<br>\s*)*<a[^>]*(khanacademy|youtu)[^>]*>.*?</a>", re.I | re.S)
WHITE = re.compile(r'\s*style="color: rgb\(255 255 255[^"]*"')
# Rodapé de fonte/crédito da imagem: do início das tags que o abrem até a próxima figura ou o fim do campo (F-20261002-CODEX-03).
CREDIT = re.compile(r"(?:\s*<br\s*/?>\s*)*(?:<(?:em|span|i|div)[^>]*>\s*)*(?:Photo credit|Image credit|Image licensed)[\s\S]*?(?=<img|\Z)", re.I)


def h(x): return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]
def clozes(t): return sorted({int(n) for n in re.findall(r"\{\{c(\d+)::", t)})
def uncloze(t, nums): return CLOZE.sub(lambda m: m.group(2) if int(m.group(1)) in nums else m.group(0), t)


def strip_credit(extra):
    removed = [re.sub(r"<[^>]+>", "", m.group(0)).strip() for m in CREDIT.finditer(extra)]
    return re.sub(r"(?:\s*<br\s*/?>\s*)+$", "", CREDIT.sub("", extra)).strip(), removed


def build():
    issues, entries, shared = [], [], {}
    tf = A("modelFieldNames", modelName=MODEL)
    if "NEBLI_Comentario" not in tf: issues.append("modelo sem NEBLI_Comentario")
    info = {n["noteId"]: n for n in A("notesInfo", notes=[c["src"] for c in spec.CARDS if c.get("src")]) if n}
    for order, c in enumerate(spec.CARDS, 1):
        otag = ordem.tag(spec.SHORT, order)
        if c["kind"] == "compartilhado":
            n = A("notesInfo", notes=[c["nid"]])
            if not n or not n[0]: issues.append(f"compartilhado ausente {c['nid']}"); continue
            shared[str(c["nid"])] = {"motivo": c["motivo"], "cor": c["cor"], "order": order, "ordem_tag": otag, "bloco": c["bloco"],
                                    "alvo": c["alvo"], "evid": c["evid"]}
            continue
        fields = {f: "" for f in tf}
        tags = [LESSON_TAG, "NEBLI::escopo::aula", f"NEBLI::objetivo::{c['bloco']}", otag, f"NEBLI::run::{spec.RUN_ID}"]
        src = c.get("src"); base = None; removed = []
        if src:
            n = info.get(src)
            if not n: issues.append(f"fonte ausente {src}"); continue
            base = {k: v["value"] for k, v in n["fields"].items()}
            origin = c.get("origin", "AnKing")
            fields["Text"] = base["Text"]
            fields["Extra"], removed = strip_credit(WHITE.sub("", KHAN.sub("", base["Extra"])))
            if c.get("uncloze"): fields["Text"] = uncloze(fields["Text"], set(c["uncloze"]))
            tags = n["tags"] + tags + [f"NEBLI::source::nid-{src}"]
            if A("findNotes", query=f'"tag:NEBLI::source::nid-{src}"'): issues.append(f"cópia NEBLI viva já existe para {src}")
        else:
            origin = "Autoral"; fields["Text"], fields["Extra"] = c["text"], c["extra"]
            tags.append(f"NEBLI::author::uc08-{spec.SHORT}-{c['key']}")
            if A("findNotes", query=f'"tag:NEBLI::author::uc08-{spec.SHORT}-{c["key"]}"'): issues.append(f"autoral já existe {c['key']}")
            if len(c.get("espelhos", [])) < 2: issues.append(f"{c['key']}: menos de 2 espelhos")
        tags.append(f"NEBLI::origem::{origin}")
        if re.search(r"credit|licensed by", fields["Text"] + fields["Extra"], re.I): issues.append(f"{c['key']}: crédito visível restante")
        if fields["Extra"].count("<span") != fields["Extra"].count("</span") or fields["Extra"].count("<em") != fields["Extra"].count("</em"):
            issues.append(f"{c['key']}: HTML desbalanceado após retirar crédito")
        got, want = clozes(fields["Text"]), sorted(c["flags"])
        if got != want: issues.append(f"{c['key']}: clozes {got} != plano {want}")
        cards = [{"n": k, "ord": k - 1, "flag": v, "cor": COR[v]} for k, v in sorted(c["flags"].items())]
        tags += [f"NEBLI::cor::{spec.LESSON}::{x}" for x in sorted({x["cor"] for x in cards})]
        if all(x["flag"] == 5 for x in cards): tags.append("NEBLI::lateral")
        for im in re.findall(r'src="([^"]+)"', fields["Text"] + fields["Extra"]):
            if im in spec.MEDIA: continue
            if not A("retrieveMediaFile", filename=im): issues.append(f"{c['key']}: mídia ausente {im}")
        e = {k: v for k, v in c.items() if k not in ("text", "extra")}
        e.update(order=order, origin=origin, model=MODEL, tags=sorted(set(tags)), fields=fields, fields_hash=h(fields), cards=cards,
                 source_fields_hash=h(base) if base else None, credito_removido=removed)
        entries.append(e)
    for f in spec.MEDIA.values():
        if not (HERE / f).exists(): issues.append(f"mídia local ausente {f}")
    keys = [c["key"] for c in spec.CARDS]
    if len(set(keys)) != len(keys): issues.append("chave repetida")
    used = [n for n in A("findNotes", query=f'"tag:NEBLI::ordem::{spec.SHORT}-*"')]
    if used: issues.append(f"prefixo de ordem '{spec.SHORT}' já usado em {len(used)} nota(s)")
    tot = lambda f: sum(1 for e in entries for x in e["cards"] if f(e, x))
    origens = sorted({e["origin"] for e in entries})
    plan = {"run_id": spec.RUN_ID, "short": spec.SHORT, "lesson_id": spec.LESSON, "deck": spec.DECK, "criterios": spec.CRITERIOS,
            "E1": "incluída nesta corrida (pedido de 02/10: piloto E1 + deck)", "entries": entries, "compartilhados": shared,
            "excluidos": [{"nid": n, "motivo": m} for n, m in spec.EXCLUIDOS], "fora_do_recorte": spec.FORA_DO_RECORTE, "media": spec.MEDIA,
            "totais": {"notas": len(entries), "cards": tot(lambda e, x: True), "verdes": tot(lambda e, x: x["flag"] == 3),
                       "azuis": tot(lambda e, x: x["flag"] == 4), "rosas": tot(lambda e, x: x["flag"] == 5),
                       "origens_notas": {o: sum(e["origin"] == o for e in entries) for o in origens},
                       "origens_cards": {o: sum(len(e["cards"]) for e in entries if e["origin"] == o) for o in origens},
                       "compartilhados_associados": len(shared), "creditos_removidos": sum(bool(e["credito_removido"]) for e in entries)}}
    plan["selection_hash"] = h([(e["key"], e["fields_hash"], e["cards"]) for e in entries])
    return plan, issues


if __name__ == "__main__":
    plan, issues = build()
    (HERE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1))
    print(json.dumps(plan["totais"], ensure_ascii=False), plan["selection_hash"])
    print("ISSUES:", issues or "nenhuma")
    print("deck existe:", spec.DECK in [re.sub(r" \(\d+\)", "", d) for d in A("deckNames")])
