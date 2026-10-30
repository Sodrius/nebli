"""Decisão de cada nota das seções de recurso (SECOES_DA_AULA) que não entra no lote 1, com motivo da lista fechada do modo prova
(gate deck_prova: duplica <nid no deck> | clinico-especifico | autonomico | toxicologia-especifica | lote-N | outra-uc). Lidas uma a uma
em busca/secoes/*.txt em 30/10; as regras abaixo só agrupam o que foi lido, e cada exceção está em MANUAL.

    /usr/bin/python3 excluidos.py     # grava excluidos.json (lido pelo spec)
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
spec = (HERE / "spec.py").read_text(encoding="utf-8")
NO_DECK = set(re.findall(r"K\((\d{13})", spec))
SECOES = re.findall(r'"(_[^"]+)"', spec.split("_SEC = ")[1].split("SECOES_DA_AULA")[0])

MANUAL = {
 "1490066286562": "duplica 1490066314616 (parcial tem menos eficácia; fica a versão da curva que desce)",
 "1490066326803": "duplica 1490066326802 (mesmo mnemônico do índice terapêutico estreito)",
 "1485126747494": "duplica 1490066326802 (lítio já está no mnemônico do IT estreito)",
 "1484950408050": "duplica 1484950383414 (buprenorfina agonista μ parcial)",
 "1472426600174": "duplica 1472426585896 (irreversível muda Vmax, já dito com o não competitivo)",
 "1472747773497": "duplica 1461865849072 (NO eleva GMPc no músculo liso)",
 "1497378335881": "duplica 1461865849072 (NO → guanilato ciclase → GMPc)",
 "1461865838545": "duplica 1461865849072 (NO age pela guanilato ciclase citosólica)",
 "1484950499429": "clinico-especifico: pentazocina e nalbufina",
 "1485382082442": "autonomico: anticolinesterásicos nos receptores muscarínicos e nicotínicos",
 "1485382321484": "autonomico: bloqueadores neuromusculares e receptor NM",
 "1476919655451": "autonomico: antimuscarínicos e frequência cardíaca",
 "1475107702619": "autonomico: colinomiméticos imitam a acetilcolina",
 "1490137873320": "toxicologia-especifica: ciguatoxina",
 "1490137877026": "toxicologia-especifica: ciguatoxina",
 "1470880187380": "outra-uc: fisiologia cardíaca (condutância ao K+ em repouso); o princípio da hipercalemia entra por 1470880181246",
 "1474922409905": "outra-uc: transporte de glicose pelos GLUT (fisiologia)",
 "1461857120583": "outra-uc: GEF na ativação da proteína G (bioquímica de sinalização)",
 "1461857134573": "outra-uc: GAP na proteína G (bioquímica de sinalização)",
 "1475029140220": "outra-uc: dissociação da subunidade α-GTP (bioquímica de sinalização)",
 "1461865864883": "outra-uc: aminoácidos fosforilados por PKA e PKC (bioquímica)",
 "1461866979051": "outra-uc: RTK dimérico (detalhe estrutural de receptor)",
 "1467833758513": "outra-uc: dedo de zinco dos receptores nucleares (detalhe estrutural)",
 "1497373274959": "outra-uc: contração do músculo esquelético (fisiologia)",
}
LOTE3 = {"1472426494725", "1472426513341", "1472426541101", "1472426549510", "1472426560728", "1472426537468"}
REGRAS = [
 (r"\bα\s?[12]\b|\bβ\s?[123]\b|β-adrenergic|β adrenergic|adrenergic|muscarinic|\bM [123]\b|sympath|parasympath|ganglion|ganglia|"
  r"\bD [12]\b|dopamine|H [12] |histamine|nicotinic|cholinomimetic|bethanechol|pilocarpine|methacholine|adrenal medulla|ANS\b",
  "autonomico: receptor ou via do sistema autônomo/histaminérgico (farmacologia autonômica, fora da UC19)"),
 (r"ADH|V [12] |vasopressin|desmopressin|aquaporin|thyroid|T 3|TSH|Graves|insulin|IGF|growth hormone|natriuretic|ANP",
  "outra-uc: fisiologia endócrina/renal de receptor (UC de fisiologia)"),
 (r"neuron|axon|dendrite|myelin|conduction velocity|space \(|time constant", "outra-uc: neurofisiologia"),
]


def motivo(nid, frente):
    if nid in MANUAL:
        return MANUAL[nid]
    if nid in LOTE3:
        return "lote-3: cinética enzimática (Michaelis-Menten, Km, Vmax, Lineweaver-Burk) entra com a cinética de saturação (ordem zero)"
    for rx, m in REGRAS:
        if re.search(rx, frente):
            return m
    if re.search(r"Proton pump|probenecid|Tetracyclines, fluoroquinolones|chelation", frente):
        return "lote-2: interação farmacocinética de absorção ou excreção (farmacocinética)"
    return None


out, sem = [], []
for s in SECOES:
    for l in (HERE / "busca" / "secoes" / f"{s}.txt").read_text(encoding="utf-8").splitlines()[1:]:
        m = re.match(r"(\d{13}) \S+ (.*)", l)
        if not m or m.group(1) in NO_DECK or any(m.group(1) == x[0] for x in out):
            continue
        mo = motivo(m.group(1), m.group(2))
        (out.append([m.group(1), mo]) if mo else sem.append(l[:150]))
(HERE / "excluidos.json").write_text(json.dumps([[int(n), mo] for n, mo in out], ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(out)} excluídas com motivo; sem regra: {len(sem)}")
for l in sem:
    print("  ", l)
