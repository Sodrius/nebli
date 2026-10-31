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
 1793275928565: ("m-q2", "De Nucci, cap. 1, p.6", "A permeabilidade da membrana celular ao fármaco depende de vários fatores, como peso molecular, lipofilicidade, grau de ionização do fármaco"),
 1793274291012: ("m-q5", "apostila, aula 2, cap. 2, p.14", "Área ou superfície de absorção"),
 1793275932161: ("m-v7", "apostila, aula 1, cap. 5, p.12", "Todos esses medicamentos possuem ao menos os seguintes elementos em sua confecção"),
 1793274287334: ("m-v8", "apostila, aula 1, cap. 6, p.13", "a extensão da absorção (ASC) e o pico da absorção (Cmáx)."),
 1793274292086: ("m-v8", "apostila, aula 1, cap. 6, p.13", "A equivalência farmacológica é realizada por uma série de testes in vitro"),
 1793274292588: ("m-v8", "apostila, aula 1, cap. 6, p.13", "eles apresentam a mesma eficácia terapêutica e, portanto, são intercambiáveis."),
 1793274288090: ("m-b1", "apostila, aula 2, cap. 1, p.14", "biodisponibilidade é um termo usado para descrever a quantidade de uma dose administrada de uma droga não alterada que atinge a circulação sistêmica."),
 1793274289514: ("m-b2", "apostila, aula 2, cap. 1, p.14", "quando uma medicação se utiliza de outras vias (p.e. via oral), sua biodisponibilidade diminui"),
 1793274287843: ("m-b6", "apostila, aula 1, cap. 6, p.13", "um voluntário ou paciente toma uma dada formulação (medicamento referência) e em outra ocasião ele toma outra dada formulação (formulação teste)."),
 1792624459224: ("m-d7", "questão orientadora FC 35", "a queda da concentração no compartimento vascular (sangue) ocorre paralelamente ao preenchimento sequencial de tecidos conforme sua perfusão."),
 1793274290262: ("m-m5", "questão orientadora FC 30", "Dentre os constituintes de fitoterápicos e medicinas naturais descritos na literatura farmacocinética"),
 1792624466677: ("m-e5", "questão orientadora FC 18", "O clearance sistêmico total (Clsist) de um fármaco que sofre eliminação por múltiplas vias concorrentes"),
 1792624465549: ("m-e6", "questão orientadora FC 15", "A equação geral que relaciona o clearance de um órgão (Cl), seu fluxo sanguíneo (Fx) e sua fração de extração (E)"),
 1792657542582: ("m-e6", "De Nucci, cap. 1, p.10", "Fração de extração (E) = Ca – Cv Ca"),
 1792624465974: ("m-e6", "questão orientadora FC 16", "Fármacos que possuem uma fração de extração hepática elevada (EH > 0,7), como a lidocaína, nitroglicerina e morfina"),
 1792624473125: ("m-x2", "questão orientadora FC 3", "Devido a um quadro infeccioso respiratório grave, seu médico prescreveu rifampicina por via oral."),
 1792624476548: ("m-x4", "questão orientadora FC 7", "sob terapia antiplaquetária com clopidogrel pós-implante de stent coronário, faz uso contínuo de omeprazol para proteção gástrica."),
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
                        "motivo": "autoral antigo da UC19 (decks Farmacocinética I/II) que Davi estudou ou corrigiu; volta com o histórico",
                        "motivacao": mot, "fontes": [{"localizador": loc, "trecho": trecho}],
                        "busca": "Nota viva achada pela busca por significado no NEBLI vivo (busca/semantica.jsonl); nenhum acervo tem o item "
                                 "(ver busca/cobertura.tsv e busca/anking.txt); reaproveitada em vez de reescrita, como manda o MEMORY §5 (refação)."}
(HERE / "revisor-autorais-contexto.json").write_text(json.dumps({"_como": "Notas reaproveitadas: origem e campos vivos materializados para o revisor (30/10).",
                                                                 "cards": cards}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(cards), sum(1 for c in cards.values() if c["origin"] == "Autoral"), "autorais")
