#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Recria os 5 NEBLIcards no MESMO estilo visual dos AnKing (modelo AnKingOverhaul),
em INGLES, com imagem do slide do professor (parity 98%) e clozes que induzem melhor.
Apaga os 5 antigos (modelo NEBLI generico) e cria os novos. Uso: [--apply] (default dry-run)."""
import json, urllib.request, sys, os
sys.stdout.reconfigure(encoding="utf-8")
APPLY = "--apply" in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NEBLIDIR = os.path.join(ROOT, "flashcards", "cards-nebli")
MODEL = "AnKingOverhaul (AnKing Step Deck / AnKingMed)"

def call(a, **p):
    req = urllib.request.Request("http://localhost:8765",
        json.dumps({"action": a, "version": 6, "params": p}).encode(), {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=40))
    if r.get("error"): raise RuntimeError(r["error"])
    return r["result"]

DECKS = {
  "bioq-23-aminoacidos-ureia": "UC02::Bioquímica::Metabolismo dos aminoácidos",
  "bioq-21-lipideos-rotas": "UC02::Bioquímica::Metabolismo dos lipídeos",
}
IMG = lambda fn: '<br><img src="%s">' % fn   # sem style inline: idêntico aos AnKing
# selo discreto de NEBLIcard (aparece no verso, canto direito, gold NEBLI mudo)
SELO = '<div style="text-align:right; font-size:10px; letter-spacing:.4px; color:#b8973f; margin-top:10px; font-family:sans-serif; opacity:.85;">&#10022; NEBLIcard</div>'
# imagem-mãe AnKing reusada de cards irmãos (nativa, leve, já no dispositivo = sem lag).
# Preferência declarada por Davi: outros cards do AnKing > internet > slide.
IMG_MAE = {
  "bioq-21-lipideos-rotas": "ad2729aecb1958f43aa4f15be8b16774.jpg",   # figura textbook: β-ox + síntese (22 cards irmãos)
  "bioq-23-aminoacidos-ureia": "Screen Shot 2021-01-07 at 15.17.18.jpg",  # Sketchy ureia/nitrogênio (18 cards irmãos)
}

# v3 (pós card-mirror rodada 1): sem travessão/aspas curvas, sem referência a banca,
# verso telegráfico estilo AnKing, cloze curto, crédito Physeo nos de lipídeo (a imagem é Physeo).
CARDS = {
 "bioq-21-lipideos-rotas": [
   {"Text":"In fatty acid synthesis, the step right after condensation is a {{c1::reduction}} (NADPH), then dehydration, then reduction.",
    "Extra":"NADPH-dependent; mirror of β-oxidation. +2 C per round from malonyl-CoA. Photo credit: Image licensed by Physeo and used with permission.",
    "Topico":"3.3 FA synthesis, FAS cycle"},
   {"Text":"Complete oxidation of one palmitate (16 C) yields {{c1::129}} net ATP.",
    "Extra":"131 gross − 2 (activation). 7 rounds → 8 acetyl-CoA; 31 NADH, 15 FADH2, 8 GTP. Photo credit: Image licensed by Physeo and used with permission.",
    "Topico":"2.1 palmitate ATP count"},
   {"Text":"Fatty acid activation cleaves ATP to {{c1::AMP + PPi}}, not ADP + Pi (costs ~2 ATP).",
    "Extra":"PPi also split → 2 high-energy bonds (−2 in balance). Enzyme: fatty acyl-CoA synthetase. Photo credit: Image licensed by Physeo and used with permission.",
    "Topico":"1.3 fatty-acid activation"},
 ],
 "bioq-23-aminoacidos-ureia": [
   {"Text":"A healthy, well-fed adult sits at {{c1::zero}} nitrogen balance.",
    "Extra":"N in − N out; ~90% urinary urea. Positive: growth, pregnancy, healing. Negative: fasting, trauma, infection.",
    "Topico":"1.2 nitrogen balance"},
   {"Text":"Free ammonia is released from glutamate by {{c1::glutamate dehydrogenase}}, regenerating α-ketoglutarate.",
    "Extra":"Truly removes N (transamination only transferred it to glutamate). Mitochondrial, hepatic. NAD+/NADP+.",
    "Topico":"2.4 oxidative deamination"},
 ],
}

def main():
    print("MODO:", "APPLY" if APPLY else "DRY-RUN")
    for slug, deck in DECKS.items():
        old = call("findNotes", query='deck:"%s" tag:NEBLI::gerado' % deck)
        print("\n[%s] NEBLIcards antigos a apagar=%d  novos a criar=%d" % (slug, len(old), len(CARDS[slug])))
        if not APPLY:
            for c in CARDS[slug]:
                print("   EN:", c["Text"][:95])
            continue
        if old:
            call("deleteNotes", notes=old)
        media = IMG_MAE[slug]   # imagem AnKing nativa, já presente na coleção (sem lag)
        for c in CARDS[slug]:
            note = {"deckName": deck, "modelName": MODEL,
                    "fields": {"Text": c["Text"], "Extra": c["Extra"] + IMG(media) + SELO},
                    "tags": ["NEBLI::"+slug, "NEBLI::gerado"]}
            call("addNote", note=note)
        # persistir
        os.makedirs(NEBLIDIR, exist_ok=True)
        json.dump({"slug": slug, "modelo": MODEL, "idioma": "en", "gerados": CARDS[slug]},
                  open(os.path.join(NEBLIDIR, slug+".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("   -> recriados %d com imagem" % len(CARDS[slug]))
    if APPLY:
        call("sync"); print("\nsync disparado.")

main()
