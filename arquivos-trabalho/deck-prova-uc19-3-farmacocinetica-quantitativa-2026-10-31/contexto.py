"""revisor-autorais-contexto.json: origem e campos vivos de cada nota reaproveitada (sh-), para o revisor independente (leitura do Anki).
Autoral antigo da UC19 que Davi aprovou ou corrigiu: campos vivos + motivação congelada + trecho literal da base da prova.
    /usr/bin/python3 contexto.py
"""
import json
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
plan = json.loads((HERE / "plan.json").read_text())


def call(a, **p):
    return json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps({"action": a, "version": 6, "params": p}).encode())))["result"]


AUT = {  # nid: (motivação, localizador, trecho literal da base)
 1792657545614: ("m-k1", "De Nucci, cap. 1, p.4", "o t1/2 de um fármaco é constante, independentemente da concentração"),
 1792624457204: ("m-k2", "De Nucci, cap. 1, p.3", "C = C(0) × e–kt"),
 1792624458275: ("m-k3", "De Nucci, cap. 1, p.4", "A tangente indica a constante k"),
 1792624463275: ("m-h2", "De Nucci, cap. 1, p.4", "Após 2 meias-vidas, 25%, após 3, 12,5%"),
 1792657541196: ("m-h3", "De Nucci, cap. 1, p.4", "O t1/2 e seu conhecimento são úteis para determinar quanto tempo levará para o organismo entrar"),
 1792657537231: ("m-h5", "apostila, aula 2, cap. 4, p.15", "qualquer fator que aumente o Vd pode aumentar também a meia-vida"),
 1792657544384: ("m-h5", "apostila, aula 2, cap. 5, p.15", "a meia-vida do fármaco, em geral, é usada para medir a CL do fármaco"),
 1792624466325: ("m-c3", "De Nucci, cap. 1, p.10", "R0 = Cl × Css"),
 1792657541958: ("m-c4", "objetivos cognitivos FC, item f.i(3c)", "(c) cálculo da dose de carga"),
 1793274287022: ("m-o1", "objetivos cognitivos FC, item f.i(2a)", "efeito de ka, ke e dose em Cmax, tmax e AUC"),
}
cards = {}
comp = plan.get("compartilhados") or {}
vivas = {n["noteId"]: n for n in call("notesInfo", notes=[int(k) for k in comp])}
for k, v in comp.items():
    if v.get("source_nid"):
        aula = next((t.split("::", 1)[1] for t in vivas[int(k)]["tags"] if t.startswith("NEBLI::2026-")), "?")
        cards[f"sh-{k}"] = {"origin": "AnKing", "source_nid": str(v["source_nid"]),
                            "motivo": f"cópia NEBLI da nota de acervo {v['source_nid']}, viva em {aula}"}
        continue
    mot, loc, trecho = AUT[int(k)]
    n = vivas[int(k)]
    cards[f"sh-{k}"] = {"origin": "Autoral", "kind": "autoral", "fields": {f: x["value"] for f, x in n["fields"].items()},
                        "motivo": "autoral antigo de cinética da UC19 (deck Farmacocinética I) que Davi estudou ou corrigiu; volta com o histórico",
                        "motivacao": mot, "fontes": [{"localizador": loc, "trecho": trecho}],
                        "busca": "Nota viva achada pela busca por significado no NEBLI vivo (busca/semantica.jsonl); nenhum acervo tem o item "
                                 "(ver busca/cobertura.tsv e busca/anking.txt); reaproveitada em vez de reescrita, como manda o MEMORY §5 (refação)."}
(HERE / "revisor-autorais-contexto.json").write_text(json.dumps({"_como": "Notas reaproveitadas: origem e campos vivos materializados para o revisor (30/10).",
                                                                 "cards": cards}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(cards), sum(1 for c in cards.values() if c["origin"] == "Autoral"), "autorais")
