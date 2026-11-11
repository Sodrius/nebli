"""Linha lógica, provas e uso das fontes da 75 (roda depois de planejar.py, que reescreve escopo.json)."""
import json
p = json.load(open("plan.json")); E = {e["key"] for e in p["entries"]} | {f"sh-{k}" for k in p["compartilhados"]}
e = json.load(open("escopo.json"))
e["cards_de_conexao"] = ["k-progressao", "k-prolif-remocao", "k-dano-nao-letal", "k-metastase-def", "k-sequencia-cis", "k-vias-org", "k-epi-diag-precoce"]
e["uso_das_fontes"] = {"aula": ["k-criterios", "k-prolif-remocao", "k-30-duplicacoes", "k-fracao", "k-metastase-def"],
 "prova": ["k-displasia-anaplasia", "k-heterogeneidade-terapia", "ak1518219030992", "ak1518219637289", "ak1518403259951"],
 "bibliografia": ["k-capsula", "k-hallmarks", "k-sentinela", "k-funcao"], "apostila": ["k-tumor-neoplasia-cancer", "ak1496165216576", "k-tres-fatores", "k-metilacao", "k-epi-diag-precoce"]}
P = lambda *c: {"cards": list(c)}; F = lambda m: {"fora": m}
pv = {"2025 P4 3.3": P("k-inflamacao-cronica", "sh-1792240574794"), "2019 P4 2.11": P("ak1518241882006", "ak1518403144606", "k-metastase-def"),
 "2018 P4 1.2": P("k-displasia-anaplasia", "ak1496164741405", "ak1496164875478", "ak1496164677268", "ak1518402560522"), "2018 P4 1.3": F("diagnóstico molecular e receptores hormonais da mama: aula integrada (GR) e aula 76"),
 "2017 P4 1.4": P("ak1496110867291", "ak1496164741405", "k-invasao"), "2017 P4 1.8": P("ak1517957674940", "k-quatro-classes"), "2017 P4 1.9": P("ak1518403259951", "ak1518403144606"),
 "2017 P4 2.4": P("ak1496111443409", "ak1517723603774"), "2016 P3 1.1": P("ak1487461112379", "ak1518218866119", "k-sequencia-cis"), "2016 P3 1.2": F("HPV-16 e coilocitose como carcinógeno: carcinógenos biológicos são a aula 78"),
 "2016 P3 1.4": P("ak1518219030992", "k-sequencia-cis"), "2016 P3 1.5": P("ak1518219637289", "ak1518219442201", "ak1518219881077"), "2016 P3 1.8": P("ak1517723603774", "k-epi-diag-precoce"),
 "2016 P3 2.2": P("ak1517720363511", "ak1488680226241"), "2016 P3 2.3": P("ak1496161616847", "k-checkpoints"), "2016 P3 2.5": P("sh-1792240993866", "sh-1792240993017"),
 "2015 P3 2.1": P("ak1496110867291", "k-invasao"), "2015 P3 2.2": P("k-quatro-classes"), "2015 P3 2.4": P("ak1518219637289", "ak1518219442201"), "2015 P3 2.7": P("k-epi-diag-precoce", "ak1496111589277"),
 "2015 P3sub 2.1": P("k-criterios", "ak1518402560522", "ak1496164875478", "ak1526251874337")}
for v in pv.values():
    if "cards" in v: assert set(v["cards"]) <= E, set(v["cards"]) - E
e["provas"] = [dict(id=k, **v) for k, v in pv.items()]
L = lambda passo, mec, liga, *c: {"passo": passo, "mecanismo": mec, "liga_ao_proximo": liga, "cards": list(c)}
e["linha_logica"] = [
 L("Neoplasia é crescimento clonal autônomo; o nome vem do parênquima (-oma, carcinoma, sarcoma) com exceções", False, "nomeado o tumor, falta saber se é benigno ou maligno", "k-tumor-neoplasia-cancer", "k-parenquima-estroma", "k-excecoes"),
 L("A perda de diferenciação dá anaplasia; a desordem do tecido é displasia; displasia de toda a espessura sem romper a membrana basal é carcinoma in situ", True, "a transformação vem de dano genético e expansão clonal", "k-displasia-anaplasia", "k-sequencia-cis", "ak1518219030992"),
 L("Dano genético não letal numa célula a faz expandir-se clonalmente; novas mutações criam subclones", True, "a massa cresce quando a proliferação supera a perda", "k-dano-nao-letal", "k-progressao", "k-heterogeneidade-terapia"),
 L("O tumor cresce porque a proliferação supera a perda; 30 duplicações dão 1 g, e a fração de crescimento decide a resposta à quimioterapia", True, "crescendo, o maligno infiltra e o benigno empurra", "k-prolif-remocao", "k-30-duplicacoes", "k-fracao", "k-fc-quimio"),
 L("Benigno cresce expansivo com cápsula; maligno infiltra sem plano de clivagem e invade a membrana basal", True, "ao invadir vasos e linfáticos, o maligno metastatiza", "k-capsula", "k-invasao", "ak1518219637289"),
 L("Metástase é implante descontínuo por linfa, sangue ou cavidades; grau e estádio (TNM) medem o prognóstico", True, "proliferação crônica e inflamação são o terreno que inicia tudo isso", "k-metastase-def", "k-vias-org", "ak1518403259951"),
 L("Hiperplasia, metaplasia, displasia e inflamação crônica aumentam divisões e dano ao DNA, favorecendo a transformação", True, "a distribuição do câncer na população mostra o peso do ambiente, da idade e da genética", "k-inflamacao-cronica", "sh-1792240574794"),
 L("A epidemiologia mostra ambiente, idade e genética como fatores, e o diagnóstico precoce derruba a mortalidade", True, "fim da aula", "k-epi-fatores", "k-epi-idade", "k-epi-diag-precoce")]
for x in e["linha_logica"]:
    assert set(x["cards"]) <= E, set(x["cards"]) - E
json.dump(e, open("escopo.json", "w"), ensure_ascii=False, indent=1)
print("escopo ok")
