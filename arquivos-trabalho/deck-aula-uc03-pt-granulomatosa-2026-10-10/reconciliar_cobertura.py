"""Liga IDs do inventário aos cards físicos curados, sem presumir cobertura por nome.

As associações sem card independente são deliberadas: um card recupera a
relação, ou o detalhe de baixo ganho fica no Extra. Revisão pós-Anki é separada.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
plan = json.loads((HERE / "plan.json").read_text())
valid = {e["key"] for e in plan["entries"]} | {f"sh-{nid}" for nid in plan["compartilhados"]}
coverage = json.loads((HERE / "cobertura.json").read_text())
alias = {
    "residentes": "sh-1791147097386", "ativacao-morfologia": "ativacao-lisossomos",
    "mhcii": "sh-1791625427059", "il2": "sh-1791625429033", "ifng": "sh-1791625436658",
    "io-epitelioide": "visual-arquitetura", "io-langhans": "langhans", "io-granuloma": "visual-arquitetura",
    "heterogeneidade": "fases", "io-caseosa": "visual-caseosa-fibrose",
    "io-fibrose": "visual-caseosa-fibrose", "io-antracose": "visual-caseosa-fibrose",
    "calcificacao": "calcificacao-distrofica", "io-baar": "visual-baar",
    "fibrose-persistencia": "visual-caseosa-fibrose", "io-exsudacao": "visual-exsudacao",
    "reativacao-fibrose": "reativacao-cicatriz", "miliar-vasos": "miliar",
    "io-calcificacao": "calcificacao-distrofica", "dna-rna": "dna-viabilidade",
    "io-primaria": "visual-primaria", "io-cavidade": "visual-cavidade",
    "bronquios": "cavitacao", "io-miliar": "visual-miliar",
    "aids-cd4": "cd4-malformado", "io-malformado": "visual-malformado",
    "neutrofilos": "cd4-malformado", "io-sarcoidose": "visual-nao-caseoso",
    "io-asteroide": "visual-asteroide", "asteroide-inespecifico": "asteroide",
    "io-schaumann": "schaumann", "io-cristais": "cristais",
    "io-hamazaki": "hamazaki", "io-vegetal": "visual-vegetal",
    "estranho-sem-t": "corpoestranho-sem-th1", "io-sutura": "sutura",
    "sutura-persiste": "sutura", "io-silicose": "visual-silicose",
    "asbesto": "asbesto-fagocitose", "io-asbesto": "visual-asbesto",
    "micolico": "acidos-micolicos", "lam-parede": "lam-envelope",
    "corda": "fator-corda", "corda-tnf": "fator-corda-tnf",
    "inos": "sh-1791625430632", "ifng-mhcii": "sh-1791625430332",
    "reinfecta-macrofagos": "eferocitose", "saem-infectados": "saem-macrofagos",
    "treg-persistencia": "treg",
}
for item in coverage["itens"]:
    mapped = [alias.get(key, key) for key in item.get("cards", [])]
    if item["id"] == "pt47-s43-corda":
        mapped.append("fator-corda-quimica")
    if item["id"] == "pt47-s13-io-caseosa":
        mapped.append("caseosa")
    if item["id"] == "pt47-s35-io-asbesto":
        mapped.append("asbesto-corpo")
    if item["id"] == "pt47-s43-corda-migracao":
        item["cards"] = []
        item["excluido"] = "Detalhe isolado de baixo ganho (inibição de migração por fator corda); mecanismo de virulência e TNF já recuperados."
        continue
    missing = set(mapped) - valid
    if missing:
        raise ValueError(f'{item["id"]}: referências não físicas {missing}')
    item["cards"] = list(dict.fromkeys(mapped))
    if item["id"] == "pt47-s10-io-langhans":
        item["observacao"] = "Padrão nuclear recuperado em texto; figura docente não mostra núcleos com nitidez suficiente para ID visual independente."
    if item["id"] in ("pt47-s18-io-calcificacao", "pt47-s28-io-schaumann", "pt47-s29-io-cristais", "pt47-s30-io-hamazaki"):
        item["observacao"] = "Detalhe de imagem de baixo ganho: identificação conceitual, sem segundo card visual isolado."
coverage.setdefault("conferido_depois_de_instalar", False)
coverage.setdefault("como", "Inventário atômico ligado a chaves físicas do plano; revisão visual/semântica e readback pós-Anki ainda necessários.")
(HERE / "cobertura.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n")
print("itens", len(coverage["itens"]), "referências", sum(len(i.get("cards", [])) for i in coverage["itens"]))
