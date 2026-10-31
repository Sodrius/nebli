"""Decisão de cada nota das seções de recurso (SECOES_DA_AULA) que não entra no lote 2, com motivo da lista fechada do modo prova
(gate deck_prova: duplica <nid no deck> | clinico-especifico | autonomico | toxicologia-especifica | lote-N | outra-uc). As 31 seções
foram lidas uma a uma em busca/secoes/*.txt em 30/10; HY 1–2 só sai por duplica ou lote-N (F-20261030-CLAUDE-01).

    /usr/bin/python3 excluidos.py     # grava excluidos.json (lido pelo spec)
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
plan = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
NO_DECK = {str(e["src"]) for e in plan["entries"] if e.get("src")}
for k, v in plan.get("compartilhados", {}).items():
    NO_DECK |= {k, str(v.get("source_nid", ""))}
L3 = "lote-3: cinética quantitativa ({}) entra no deck-prova 3"
L1 = "lote-1: {} já está no deck-prova 1 (Farmacodinâmica)"
MANUAL = {
 "1472426521266": L3.format("primeira ordem"), "1472426529103": L3.format("ordem zero"), "1485127516413": L3.format("fenitoína em ordem zero"),
 "1490066229194": L3.format("ordem zero"), "1490066232397": L3.format("primeira ordem"), "1490066236446": L3.format("curva linear da ordem zero"),
 "1490066239613": L3.format("curva exponencial da primeira ordem"), "1490066244440": L3.format("fármacos de ordem zero"),
 "1490066195477": L3.format("fórmula da meia-vida"), "1490066198198": L3.format("tempo até o estado de equilíbrio"),
 "1490066204599": L3.format("dose de ataque"), "1490066207488": L3.format("dose de manutenção"), "1488765248074": L3.format("meia-vida da varfarina"),
 "1472426494725": L3.format("Km de Michaelis-Menten, base da cinética de saturação"), "1472426513341": L3.format("Vmax e enzima"),
 "1472426537468": L3.format("Vmax e Km"), "1474254039590": L3.format("álcool desidrogenase em ordem zero"),
 "1490066320396": L1.format("índice terapêutico"), "1490066323578": L1.format("índice terapêutico"), "1490066326802": L1.format("mnemônico do IT estreito"),
 "1490066326803": L1.format("mnemônico do IT estreito"), "1490066214478": L1.format("interação aditiva"), "1490066217772": L1.format("interação permissiva"),
 "1490066222678": L1.format("interação sinérgica"), "1490066226073": L1.format("taquifilaxia"), "1518398747905": L1.format("P-gp e resistência tumoral"),
 "1484778245242": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1485127406267": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1485127272816": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1503259126424": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1503264783060": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1490137911734": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1490137927528": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1509750647708": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1461616635772": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1472091209218": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1503259023522": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1506796830726": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1508367985399": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1490137917396": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1490137951449": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1490137955804": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1490137960049": "duplica 1505674844706 (organizador amplo de indutores e inibidores de CYP450, pedido de Davi no card em 27/10)",
 "1505674705547": "duplica 1505674844706 (claritromicina e eritromicina estão no organizador de CYP450)",
 "1514516254198": "duplica 1505674844706 (ciprofloxacino está no organizador de CYP450)",
 "1506790116654": "clinico-especifico: ITRNN e CYP (antirretroviral)", "1509750774216": "clinico-especifico: griseofulvina na porfiria",
 "1461797760919": "clinico-especifico: simeprevir (antiviral de hepatite C)", "1509752522497": "clinico-especifico: equinocandinas",
 "1509219348292": "clinico-especifico: classes de alquilantes ativadas pelo CYP (a ciclofosfamida representa)",
 "1509219472431": "clinico-especifico: ifosfamida (a ciclofosfamida representa a ativação)",
 "1497786364086": "clinico-especifico: analgésicos e varfarina", "1530807383669": "toxicologia-especifica: tratamento da intoxicação por paracetamol",
 "1582766305895": "toxicologia-especifica: bicarbonato na intoxicação por tricíclico",
 "1475101814090": "outra-uc: clearance de água livre (fisiologia renal)", "1486522482841": "outra-uc: Crigler-Najjar (bilirrubina; Gilbert representa a UGT)",
 "1486522486856": "outra-uc: Crigler-Najjar (bilirrubina)", "1474254001079": "outra-uc: órgão do metabolismo do etanol (bioquímica)",
 "1474746839955": "outra-uc: medida da água corporal (fisiologia)", "1484879673290": "clinico-especifico: coeficiente sangue:gás de anestésico inalatório",
 "1518399103440": "clinico-especifico: P-gp no carcinoma adrenocortical",
}
SECOES = json.loads(json.dumps([s for s in __import__("runpy").run_path(str(HERE / "spec.py"), run_name="x")["SECOES_DA_AULA"]]))
out, sem = [], []
for s in SECOES:
    for l in (HERE / "busca" / "secoes" / s).read_text(encoding="utf-8").splitlines()[1:]:
        m = re.match(r"(\d{13}) \S+ (.*)", l)
        if not m or m.group(1) in NO_DECK or any(m.group(1) == x[0] for x in out):
            continue
        (out.append([m.group(1), MANUAL[m.group(1)]]) if m.group(1) in MANUAL else sem.append(l[:150]))
(HERE / "excluidos.json").write_text(json.dumps([[int(n), mo] for n, mo in out], ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(out)} excluídas com motivo; sem regra: {len(sem)}")
for l in sem:
    print("  ", l)
