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
IMG = lambda fn: '<br><img src="%s" style="max-width: 100%%;">' % fn
# selo discreto de NEBLIcard (aparece no verso, canto direito, gold NEBLI mudo)
SELO = '<div style="text-align:right; font-size:10px; letter-spacing:.4px; color:#b8973f; margin-top:10px; font-family:sans-serif; opacity:.85;">&#10022; NEBLIcard</div>'

CARDS = {
 "bioq-21-lipideos-rotas": [
   {"slide":"slide-49.png",
    "Text":"In fatty acid synthesis, after the new unit is added (condensation), the three reactions that complete each round occur, in order: {{c1::reduction → dehydration → reduction}}.",
    "Extra":"The mirror image of β-oxidation run in reverse, but using NADPH as the electron donor in both reductions. Each round adds 2 carbons from malonyl-CoA. (FMUSP P2/2023 asked to number this cycle.)",
    "Topico":"3.3 FA synthesis — FAS cycle (q-0265)"},
   {"slide":"slide-21.png",
    "Text":"Complete oxidation of one palmitate (16 C) yields {{c1::129}} net ATP, using the classic yields taught in the course.",
    "Extra":"131 gross − 2 for activation. It takes 7 β-oxidation rounds (not 8) → 8 acetyl-CoA, totaling 31 NADH + 15 FADH₂ + 8 GTP. The −2 comes from activation cleaving ATP to AMP + PPi.",
    "Topico":"2.1 palmitate ATP count"},
   {"slide":"slide-13.png",
    "Text":"Activating a fatty acid costs the equivalent of 2 ATP because the ATP is cleaved all the way to {{c1::AMP + PPi}} (not ADP + Pi), and the pyrophosphate is then hydrolyzed.",
    "Extra":"Cleaving to AMP + PPi plus splitting the PPi = two high-energy bonds spent — hence the “−2” in the palmitate balance. Catalyzed by fatty acyl-CoA synthetase.",
    "Topico":"1.3 fatty-acid activation"},
 ],
 "bioq-23-aminoacidos-ureia": [
   {"slide":"slide-07.png",
    "Text":"A healthy, well-fed adult sits at {{c1::zero}} nitrogen balance — neither positive nor negative.",
    "Extra":"Balance = N ingested − N excreted (~90% as urinary urea). Positive = net retention (growth, pregnancy, healing); negative = net loss (fasting, trauma, infection). Positive isn’t “good” nor negative “bad” — they only describe the direction of nitrogen flux.",
    "Topico":"1.2 nitrogen balance"},
   {"slide":"slide-39.png",
    "Text":"Deamination releases nitrogen as free ammonia: {{c1::glutamate dehydrogenase}} strips the amino group from glutamate, regenerating α-ketoglutarate.",
    "Extra":"This is the step that actually REMOVES nitrogen from the carbon skeleton — transamination had only transferred it onto glutamate. Mitochondrial, hepatic; uses NAD⁺/NADP⁺. It is what separates “transfer” from “eliminate”.",
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
        for c in CARDS[slug]:
            src = os.path.join(ROOT, "figuras", slug, c["slide"])
            media = "nebli-%s-%s" % (slug, c["slide"])
            call("storeMediaFile", filename=media, path=src)
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
