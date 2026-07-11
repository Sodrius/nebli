#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""aplicar_deck_export.py -- cria o deck-aula adicionando NOVOS notes a partir do
conteudo do EXPORT anking-v12-export.txt (nao depende da colecao viva do Davi, que
e um subset/versao diferente do export). Fallback deterministico do
copiar_curadoria_para_deck.py quando o raw0 nao casa ao vivo.

Para cada slug:
  - AnKing curados (curadoria/<slug>-curado.json .kept[].guid) -> model AnKingOverhaul,
    Text = campo Text (col 3), Extra = campo Extra (col 4) do export; tag NEBLI::<slug> + NEBLI::anking-curado
  - NEBLIcards (cards-nebli/<slug>.json .cards[]) -> model 'Cloze Medicina - Mecanismo unico',
    Text/Extra/Image/Source; tags do proprio card
Uso: python flashcards/scripts/aplicar_deck_export.py <slug> [--dry-run]
"""
import csv, json, os, sys, argparse, urllib.request
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ANKI="http://localhost:8765"
RAIZ=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
EXPORT=os.path.join(os.path.dirname(__file__),"anking-v12-export.txt")
GUID,TEXT,EXTRA=0,3,4
MODEL_ANKING="AnKingOverhaul (AnKing Step Deck / AnKingMed)"
MODEL_NEBLI="Cloze Medicina - Mecanismo único"

def inv(a,**p):
    r=json.load(urllib.request.urlopen(urllib.request.Request(ANKI,json.dumps({"action":a,"version":6,"params":p}).encode()),timeout=120))
    if r.get("error"): raise RuntimeError(f"{a}: {r['error']}")
    return r["result"]

def load_export():
    rows={}
    with open(EXPORT,encoding="utf-8",newline="") as f:
        for row in csv.reader((l for l in f if not l.startswith("#")),delimiter="\t",quotechar='"'):
            if len(row)>EXTRA: rows[row[GUID]]=(row[TEXT],row[EXTRA])
    return rows

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("slug"); ap.add_argument("--dry-run",action="store_true")
    a=ap.parse_args()
    cur=json.load(open(os.path.join(RAIZ,"flashcards","curadoria",f"{a.slug}-curado.json"),encoding="utf-8"))
    target=cur["target_deck"]; ancora=cur["tag_ancora"]
    nebli_path=os.path.join(RAIZ,"flashcards","cards-nebli",f"{a.slug}.json")
    nebli=json.load(open(nebli_path,encoding="utf-8")) if os.path.exists(nebli_path) else {"cards":[]}
    rows=load_export()

    notes=[]
    for k in cur["kept"]:
        tx=rows.get(k["guid"])
        if not tx: print("  ! guid ausente no export:",k["guid"]); continue
        notes.append({"deckName":target,"modelName":MODEL_ANKING,
            "fields":{"Text":tx[0],"Extra":tx[1]},
            "tags":[ancora,"NEBLI::anking-curado"],
            "options":{"allowDuplicate":True}})
    for c in nebli["cards"]:
        notes.append({"deckName":target,"modelName":MODEL_NEBLI,
            "fields":{"Text":c["texto"],"Extra":c.get("extra",""),
                      "Image":c.get("imagem") or "","Source":c.get("fonte_e1","")},
            "tags":c.get("tags",[ancora,"NEBLI::gerado"]),
            "options":{"allowDuplicate":True}})

    print(f"Deck '{target}': {len(cur['kept'])} AnKing + {len(nebli['cards'])} NEBLI = {len(notes)} notes")
    if a.dry_run:
        print("[DRY-RUN] nada adicionado."); return
    inv("createDeck",deck=target)
    res=inv("addNotes",notes=notes)
    ok=[r for r in res if r]; fail=[i for i,r in enumerate(res) if not r]
    print(f"  adicionados: {len(ok)} | falhas: {len(fail)}")
    if fail: print("  indices com falha:",fail[:20])

if __name__=="__main__": main()
