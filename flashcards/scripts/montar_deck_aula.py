#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""montar_deck_aula.py -- monta e exporta um deck-aula P3.

Fluxo do deck-prova novo (curar real > autorar):
  1. Cards REAIS aprovados vivem nos decks de Referencia e no AnKing. Este script
     os COPIA para o deck-aula alvo, mas SOMENTE se o card_ref estiver no manifesto
     final. A tag NEBLI::<slug> so encontra candidatos; nao e autorizacao de entrada.
  2. Cards AUTORAIS (EN, craft corrigido) ja foram add direto no deck-aula por
     build_card.py -- este script nao mexe neles.
  3. Opcional: exportPackage do deck-aula para .apkg.

Uso:
  python flashcards/scripts/montar_deck_aula.py --slug histo-09-vasos \
      --deck "NEBLI::UC02::P3::Bio celular e tecidual::Histologia dos vasos" \
      --manifest arquivos-trabalho/matriz-deck-aula-histo-09-vasos.json \
      [--export "flashcards/decks-apkg/Histologia dos vasos.apkg"] [--dry]
"""
import argparse, json, os, re, sys, urllib.request
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

AC = "http://localhost:8765"
_WS = re.compile(r"\s+"); _TAG = re.compile(r"<[^>]+>")

def call(action, **params):
    req = urllib.request.Request(AC, json.dumps(
        {"action": action, "version": 6, "params": params}).encode("utf-8"),
        {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=90))
    if r.get("error"): raise RuntimeError(f"{action}: {r['error']}")
    return r["result"]

def norm(s):  # texto bruto do campo, sem html/cloze, colapsado
    s = re.sub(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", r"\1", s or "", flags=re.I)
    return _WS.sub(" ", _TAG.sub("", s).replace("​", "")).strip().casefold()

def first_field_val(fields):
    return next(iter(fields.values()), {}).get("value", "") if fields else ""



THEME_BY_SLUG = {
    "anato": "Anatomy", "biocel": "Cell Biology", "biomol": "Molecular Biology",
    "bioq": "Biochemistry", "embrio": "Embryology", "fisio": "Physiology",
    "histo": "Histology", "etim": "Etymology",
}

def _theme_label(slug):
    return THEME_BY_SLUG.get((slug or "").split("-", 1)[0], "Medicine")

def _with_english_theme(value, slug):
    if not value or value.lstrip().startswith("<b>"):
        return value
    return f"<b>{_theme_label(slug)}.</b> " + value

def _manifest_refs(path):
    spec = json.load(open(path, encoding="utf-8-sig"))
    refs = []
    for fact in spec.get("facts", []):
        route = fact.get("route") or {}
        if route.get("source") in {"anking", "other_deck"}:
            refs.extend(norm(str(x)) for x in route.get("card_refs", []) if norm(str(x)))
    return refs

def _approved(key, refs):
    # Trechos curtos ("ATP", "SMA") geram falso positivo perigoso. Ref curta só
    # vale se for o campo inteiro; substring exige um trecho realmente distintivo.
    return any(key == ref or (len(ref) >= 16 and ref in key) for ref in refs)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--deck", required=True)
    ap.add_argument("--manifest", required=True,
                    help="manifesto final; somente card_refs aprovados podem ser copiados")
    ap.add_argument("--export")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    approved_refs = _manifest_refs(a.manifest)

    call("createDeck", deck=a.deck)
    # o que ja existe no deck-aula (por texto do 1o campo) -> nao duplicar
    existing = set()
    for nid in call("findNotes", query=f'deck:"{a.deck}"'):
        pass
    tgt_ids = call("findNotes", query=f'deck:"{a.deck}"')
    if tgt_ids:
        for n in call("notesInfo", notes=tgt_ids):
            existing.add(norm(first_field_val(n["fields"])))

    # cards reais curados p/ esta aula, que ainda NAO estao no deck-aula
    src_ids = call("findNotes", query=f'tag:NEBLI::{a.slug} -deck:"{a.deck}"')
    copied = skipped = 0
    for n in call("notesInfo", notes=src_ids) if src_ids else []:
        key = norm(first_field_val(n["fields"]))
        if not _approved(key, approved_refs):
            continue
        if key in existing:
            skipped += 1; continue
        fields = {k: v["value"] for k, v in n["fields"].items()
                  if k not in ("ankihub_id",)}
        if "Text" in fields:
            fields["Text"] = _with_english_theme(fields["Text"], a.slug)
        tags = list(dict.fromkeys(n["tags"] + [f"NEBLI::{a.slug}"]))
        note = {"deckName": a.deck, "modelName": n["modelName"],
                "fields": fields, "tags": tags,
                "options": {"allowDuplicate": True}}
        if a.dry: copied += 1; continue
        try:
            call("addNote", note=note); copied += 1; existing.add(key)
        except Exception as e:
            print("  ERRO copy:", key[:50], "::", str(e)[:80])

    total = len(call("findNotes", query=f'deck:"{a.deck}"'))
    print(f"[{a.slug}] copiados {copied} reais, {skipped} ja presentes | deck-aula total: {total}")

    if a.export and not a.dry:
        os.makedirs(os.path.dirname(a.export), exist_ok=True)
        ok = call("exportPackage", deck=a.deck, path=os.path.abspath(a.export),
                  includeSched=False)
        print(f"  export {'OK' if ok else 'FALHOU'} -> {a.export}")

if __name__ == "__main__":
    sys.exit(main() or 0)
