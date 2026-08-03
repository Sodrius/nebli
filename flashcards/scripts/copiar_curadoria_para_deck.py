#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""copiar_curadoria_para_deck.py -- COPIA os notes curados para um deck-aula separado.

Diferente de aplicar_curadoria_anking.py (que marca a tag NEBLI:: e dessuspende
os cards ONDE eles ja estao, dentro da arvore AnKing), este script CRIA COPIAS
novas dos notes curados dentro de uma arvore de deck separada
(ex.: UC02::Bioquimica::Metabolismo dos lipideos), deixando o AnKing intacto.

Le flashcards/curadoria/<slug>-curado.json (schema novo):
    {
      "slug": "...",
      "tag_ancora": "NEBLI::<slug>",
      "target_deck": "UC02::Componente::Aula",
      "kept": [ {"guid":..., "conceito":"1.1", "raw0":"<campo1 bruto>"}, ... ]
    }

Casa cada kept com o note real da colecao pelo TEXTO BRUTO do campo 1 (raw0),
le modelo+campos+tags via notesInfo e cria uma copia (addNote, allowDuplicate)
no target_deck, adicionando a tag-ancora NEBLI::<slug>.

Uso:
    python flashcards/scripts/copiar_curadoria_para_deck.py <slug> --dry-run
    python flashcards/scripts/copiar_curadoria_para_deck.py <slug>
"""
import json, sys, os, argparse, re, urllib.request, urllib.error

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ANKICONNECT = "http://localhost:8765"
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
_WS = re.compile(r"\s+")


def _norm(txt):
    return _WS.sub(" ", (txt or "").replace("​", "")).strip()


def _invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]


def _first_field(note):
    campos = note.get("fields", {})
    if not campos:
        return ""
    return next(iter(campos.values()), {}).get("value", "")




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

def _build_index(pool_tags):
    """normalized raw0 -> notesInfo, varrendo os notes das tags do pool."""
    nids = set()
    for tag in pool_tags:
        nids |= set(_invoke("findNotes", query=f'"tag:{tag}" OR "tag:{tag}::*"'))
    idx = {}
    if nids:
        for n in _invoke("notesInfo", notes=sorted(nids)):
            idx.setdefault(_norm(_first_field(n)), n)
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--deck", help="sobrescreve o target_deck do manifesto; útil para testes isolados")
    ap.add_argument("--pool-slug", help="pool AnKing de origem quando a curadoria foi ampliada")
    args = ap.parse_args()

    cur_path = os.path.join(RAIZ, "flashcards", "curadoria", f"{args.slug}-curado.json")
    with open(cur_path, encoding="utf-8") as f:
        spec = json.load(f)
    target = args.deck or spec["target_deck"]
    ancora = spec.get("tag_ancora") or f"NEBLI::{args.slug}"
    kept = spec["kept"]

    pool_slug = args.pool_slug or args.slug
    pool_path = os.path.join(RAIZ, "arquivos-trabalho", f"anking-pool-{pool_slug}.json")
    with open(pool_path, encoding="utf-8") as f:
        pool = json.load(f)
    pool_tags = sorted({t for c in pool["cards"] for t in c.get("tags", [])})

    print(f"Alvo: deck '{target}' | tag-ancora {ancora} | {len(kept)} kept")
    print(f"Indexando colecao por {len(pool_tags)} tag(s)...")
    idx = _build_index(pool_tags)
    print(f"  notes indexados: {len(idx)}")

    casados, faltas = [], []
    for k in kept:
        n = idx.get(_norm(k.get("raw0", "")))
        (casados if n else faltas).append((k, n))

    print(f"  casados: {len(casados)} | nao casados: {len(faltas)}")
    for k, _ in faltas:
        print(f"   ! sem match: {k.get('conceito','?')} :: {k.get('front','')[:70]}")

    if args.dry_run:
        print("\n[DRY-RUN] criaria", len(casados), "copias em", target)
        return

    _invoke("createDeck", deck=target)
    existentes = {
        _norm(_first_field(n))
        for n in _invoke("notesInfo", notes=_invoke("findNotes", query=f'deck:"{target}"'))
    }
    criados, pulados, erros = 0, 0, 0
    for k, n in casados:
        if _norm(_first_field(n)) in existentes:
            pulados += 1
            continue
        fields = {name: v["value"] for name, v in n["fields"].items()}
        if "Text" in fields:
            fields["Text"] = _with_english_theme(fields["Text"], args.slug)
        # copias auto-contidas: descarta tags AnKing (#AK*) pra que uma futura
        # suspensao "por tag" do AnKing nao varra os decks-aula de teste.
        origem = [t for t in n.get("tags", []) if not t.startswith("#AK")]
        tags = list(dict.fromkeys(origem + [ancora]))
        note = {"deckName": target, "modelName": n["modelName"], "fields": fields,
                "tags": tags, "options": {"allowDuplicate": True}}
        try:
            _invoke("addNote", note=note)
            criados += 1
            existentes.add(_norm(_first_field(n)))
        except (RuntimeError, urllib.error.URLError) as e:
            erros += 1
            print(f"   ! addNote falhou ({k.get('conceito','?')}): {e}")
    print(f"\nCriadas {criados} copias, {pulados} já existentes em '{target}' (tag {ancora}); {erros} erro(s).")


if __name__ == "__main__":
    main()
