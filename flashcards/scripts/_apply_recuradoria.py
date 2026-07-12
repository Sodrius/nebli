#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Apply da re-curadoria 2026-07-12 no deck-alvo vivo (AnkiConnect).
- Move os cards CORTADOS para subdeck _cortados-recuradoria-20260712 + suspende + tag (reversivel).
- Adiciona os NEBLIcards gerados (gaps confirmados por prova/E1) ao deck-alvo.
Uso: python _apply_recuradoria.py [--apply]   (default = dry-run)
"""
import json, urllib.request, sys, re, os
sys.stdout.reconfigure(encoding="utf-8")
APPLY = "--apply" in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CUR = os.path.join(ROOT, "flashcards", "curadoria")
BAK = os.path.join(ROOT, "backups", "tecnicos")
NEBLIDIR = os.path.join(ROOT, "flashcards", "cards-nebli")

def call(a, **p):
    req = urllib.request.Request("http://localhost:8765",
        json.dumps({"action": a, "version": 6, "params": p}).encode(), {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=40))
    if r.get("error"): raise RuntimeError(r["error"])
    return r["result"]

def norm(h):
    t = re.sub("<[^>]+>", "", h or "")
    t = t.replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    t = re.sub(r"\{\{c\d+::", "", t).replace("}}", "")
    return re.sub(r"[^a-z0-9]", "", t.lower())

DECKS = {
  "bioq-23-aminoacidos-ureia": "UC02::Bioquímica::Metabolismo dos aminoácidos",
  "bioq-21-lipideos-rotas": "UC02::Bioquímica::Metabolismo dos lipídeos",
}
CORTADOS_DECK = "UC02::Bioquímica::_cortados-recuradoria-20260712"
TAG_CORT = "NEBLI::recuradoria-cortado-20260712"
MODEL = "Medicina — Cloze atômico com imagem opcional"

# ---- NEBLIcards gerados (gaps confirmados; R9 cloze unico + Extra) ----
GEN = {
 "bioq-21-lipideos-rotas": [
   {"Texto":"A síntese de ácidos graxos repete um ciclo de quatro reações na ordem {{c1::condensação → redução → desidratação → redução}} — o espelho invertido da β-oxidação.",
    "Extra":"Inverso da β-oxidação (desidrogenação → hidratação → oxidação → tiólise), mas usa NADPH como doador de elétrons nas duas reduções; cada volta adiciona 2 carbonos vindos do malonil-CoA. Caiu na P2/2023 (numerar a ordem do ciclo).",
    "Topico":"3.3 síntese de AG — ciclo da FAS (q-0265)"},
   {"Texto":"A oxidação completa de um palmitato (16 C) rende {{c1::129}} ATP líquidos (131 brutos − 2 da ativação), pelos valores clássicos do material.",
    "Extra":"São 7 voltas da β-oxidação (não 8) → 8 acetil-CoA; somam 31 NADH, 15 FADH₂ e 8 GTP. Desconta-se 2 porque a ativação quebra ATP até AMP + PPi.",
    "Topico":"2.1 conta de ATP do palmitato"},
   {"Texto":"Ativar um ácido graxo (acil-CoA sintetase) custa o equivalente a {{c1::2}} ATP, porque o ATP é clivado a AMP + PPi e o pirofosfato ainda é hidrolisado.",
    "Extra":"Não é ATP → ADP + Pi (1 ligação), e sim ATP → AMP + PPi (2 ligações de alta energia). Esse “−2” é o desconto do saldo final do palmitato.",
    "Topico":"1.3 ativação do ácido graxo"},
 ],
 "bioq-23-aminoacidos-ureia": [
   {"Texto":"O balanço de nitrogênio (N ingerido − N excretado) fica {{c1::negativo}} no jejum, trauma e infecção — perda líquida de proteína.",
    "Extra":"Cerca de 90% do N excretado sai como ureia na urina. O adulto saudável fica em balanço zero; positivo (crescimento, gravidez) não é “bom” nem negativo “ruim” — descrevem só a direção do fluxo de nitrogênio.",
    "Topico":"1.2 balanço de nitrogênio"},
   {"Texto":"A desaminação libera o nitrogênio como amônia livre: a {{c1::glutamato desidrogenase}} retira o grupo amino do glutamato e regenera α-cetoglutarato.",
    "Extra":"É o passo que de fato TIRA o N do esqueleto — a transaminação só o havia transferido para o glutamato. Enzima mitocondrial hepática; usa NAD⁺/NADP⁺. Distingue “transferir” de “eliminar”.",
    "Topico":"2.4 desaminação oxidativa"},
 ],
}

def main():
    print("MODO:", "APPLY" if APPLY else "DRY-RUN")
    if APPLY:
        existing = call("deckNames")
        if CORTADOS_DECK not in existing:
            call("createDeck", deck=CORTADOS_DECK)
    for slug, deck in DECKS.items():
        old = json.load(open(os.path.join(BAK, slug+"-curado.json.pre-recuradoria-20260712"), encoding="utf-8"))
        new = json.load(open(os.path.join(CUR, slug+"-curado.json"), encoding="utf-8"))
        keep_guids = {c["guid"] for c in new["kept"]}
        cut_raw = {norm(c["raw0"]): c for c in old["kept"] if c["guid"] not in keep_guids}
        keep_raw = {norm(c["raw0"]) for c in new["kept"]}
        ids = call("findNotes", query='deck:"%s"' % deck)
        info = call("notesInfo", notes=ids)
        matched_cut, matched_keep, unmatched = [], 0, []
        for n in info:
            f1 = list(n["fields"].values())[0]["value"]
            k = norm(f1)
            if k in cut_raw:
                matched_cut.append(n["noteId"])
            elif k in keep_raw:
                matched_keep += 1
            else:
                unmatched.append(re.sub("<[^>]+>","",f1)[:70])
        print("\n[%s] deck=%d  keep-match=%d  cut-match=%d  unmatched=%d  gerar=%d"
              % (slug, len(info), matched_keep, len(matched_cut), len(unmatched), len(GEN[slug])))
        for u in unmatched: print("   UNMATCHED:", u)
        if APPLY:
            if matched_cut:
                call("changeDeck", cards=call("cardsFromNotes", notes=matched_cut) if False else
                     sum([call("findCards", query="nid:%d"%nid) for nid in matched_cut], []), deck=CORTADOS_DECK)
                cids = sum([call("findCards", query="nid:%d"%nid) for nid in matched_cut], [])
                call("suspend", cards=cids)
                call("addTags", notes=matched_cut, tags=TAG_CORT)
            added = 0
            for card in GEN[slug]:
                note = {"deckName": deck, "modelName": MODEL,
                        "fields": {"Texto": card["Texto"], "Extra": card["Extra"], "Topico": card["Topico"]},
                        "tags": ["NEBLI::"+slug, "NEBLI::gerado"]}
                try:
                    call("addNote", note=note); added += 1
                except RuntimeError as e:
                    print("   addNote falhou:", e)
            print("   -> movidos+suspensos=%d  NEBLIcards add=%d" % (len(matched_cut), added))
        # salvar gerados sempre
        os.makedirs(NEBLIDIR, exist_ok=True)
        json.dump({"slug": slug, "gerados": GEN[slug]}, open(os.path.join(NEBLIDIR, slug+".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if APPLY:
        call("sync")
        print("\nsync disparado.")

main()
