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
 1791762409798: ("m-f6", "resumo da aula 1, p.3", "Biofarmacêutica: após administrado o fármaco, o princípio ativo é liberado é desintegrado, desagregado e dissolvido, disponibilizando o fármaco em solução"),
 1791762415623: ("m-a6", "resumo da aula 1, p.4; orientadora 18", "Fármacos podem atuar por mecanismos físico-químicos (sem interação com receptores)."),
 1791762425949: ("m-c4", "objetivos cognitivos FD, item 4", "conceituar efeitos terapêuticos (desejados), tóxicos (indesejados) e letais de um mesmo fármaco ou medicamento."),
 1791762418025: ("m-c1", "resumo da aula 1, p.5", "Afinidade: capacidade de o fármaco reconhecer e se ligar ao alvo farmacológico (relaciona-se à taxa de ocupação do receptor)."),
 1791826286643: ("m-c3", "questão orientadora FD 23", "Dois fármacos produzem o mesmo efeito máximo, mas um deles necessita de concentração menor para atingir 50% desse efeito."),
 1791826286795: ("m-c3", "questão orientadora FD 24", "Mesmo em concentrações elevadas, o fármaco X produz uma resposta máxima menor que a do fármaco Y."),
 1791762419072: ("m-g4", "resumo da aula 1, p.6", "o agonista inverso liga-se preferencialmente ao estado inativo (R), estabilizando-o e reduzindo a sinalização abaixo dos níveis basais"),
 1791762419199: ("m-g4", "questão orientadora FD 26", "Liga-se ao receptor sem ativá-lo e impede ou reduz a ação do agonista, sem reduzir por si só a atividade constitutiva do receptor."),
 1791762421022: ("m-g5", "resumo da aula 1, p.6", "Agonista Tendencioso (Biased Agonist): ligante estabiliza conformações específicas do receptor que ativam preferencialmente uma via de sinalização"),
 1791762416798: ("m-n6", "resumo da aula 1, p.4", "Sítio ortostérico: sítio de ligação primário e nativo do receptor, onde se liga o ligante endógeno ou o agonista/antagonista direto."),
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
                        "motivo": "autoral antigo da UC19 (aula 01) que Davi aprovou, melhorou ou corrigiu; volta com o histórico",
                        "motivacao": mot, "fontes": [{"localizador": loc, "trecho": trecho}],
                        "busca": "Nota viva achada pela busca por significado no NEBLI vivo (busca/semantica.jsonl); nenhum acervo tem o item "
                                 "(ver busca/cobertura.tsv e busca/anking.txt); reaproveitada em vez de reescrita, como manda o MEMORY §5 (refação)."}
(HERE / "revisor-autorais-contexto.json").write_text(json.dumps({"_como": "Notas reaproveitadas: origem e campos vivos materializados para o revisor (30/10).",
                                                                 "cards": cards}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(cards), sum(1 for c in cards.values() if c["origin"] == "Autoral"), "autorais")
