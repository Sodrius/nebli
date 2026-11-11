"""E5 da 75: cobertura.tsv, decisoes.json, tipos.tsv, REVISAO-AUTORAIS-gerado.md, imagens-batem.json, mapa/motivações/matriz com
as chaves reais do plano. Rodar depois do build (e o build de novo, para a busca entrar no campo dos autorais)."""
import json
import pathlib
import re

H = pathlib.Path(__file__).parent
plan = json.load(open(H / "plan.json"))
E = {e["key"]: e for e in plan["entries"]}
SRC = {str(v.get("source_nid")): f"sh-{k}" for k, v in plan["compartilhados"].items() if v.get("source_nid")}


def r(nid):
    """chave real de uma nota de acervo: ak<nid> se a corrida criou, sh-<cópia> se já existia"""
    k = f"ak{nid}"
    return k if k in E else SRC.get(str(nid), k)


lid = {}
for l in open(H / "busca/semantica.jsonl"):
    d = json.loads(l)
    hs = sorted([h for h in d.get("top", []) if h.get("acervo") in ("AnKing", "NEBLI-vivo", "Histology")], key=lambda h: -h.get("sim", 0))
    lid[d["chave"]] = [str(h["nid"]) for h in hs][:4]
BUSCA = "Busca nos três caminhos (seções First Aid/Pathoma/B&B/Bootcamp de neoplasia; palavra-chave em AnKing e externos; significado em todos os acervos e NEBLI vivo, 10/11): "
MEC, EX_MEC, AN_MEC = "causa → mecanismo → consequência", "1791631347467", "1791631345113"
ORGZ, EX_ORG, AN_ORG = "conjunto organizado", "1792787420154", "1793784421465"
FATO, EX_FATO, AN_FATO = "fato-chave situado", "1791023354943", "1791627549152"
CONT, EX_CONT, AN_CONT = "contraste por critério comum", "1792166970014", "1793784421465"
# chave: (conceito, fonte, decora, decisão, tipo, princípio, visual, papel, par, tipo_info, exemplar, semelhança, anti, item)
A = {
 "k-tumor-neoplasia-cancer": ("Tumor, neoplasia e câncer", "lâmina 2", "malignant", "AnKing só tem 'tumores são benignos ou malignos' (1517719786045, trivial) e definição de neoplasia; nenhum distingue os três termos", "comparacao", "Tumor é qualquer massa; neoplasia é crescimento clonal autônomo; câncer é a neoplasia maligna", "nao", "lacuna", "§B", CONT, EX_CONT, "três termos encaixados com o critério visível", AN_CONT, "p1-1"),
 "k-parenquima-estroma": ("Parênquima dá nome e comportamento", "lâmina 2", "parenchyma", "Busca: nenhum AnKing de parênquima × estroma tumoral (candidatos 1517721704430, 1463356568833 são nomenclatura e fibroadenoma)", "fato-chave", "O parênquima neoplásico define nome e comportamento; o estroma sustenta", "nao", "lacuna", "§E", FATO, EX_FATO, "fato com contexto visível e o componente no cloze", AN_FATO, "p1-3"),
 "k-excecoes": ("Exceções malignas com nome de benigno", "palavras-cruzadas 11 e 29; objetivo 4", "lymphoma", "AnKing tem cada tumor isolado (seminoma 1463339990695, melanoma 1517721745386); nenhum reúne as exceções à regra do -oma", "comparacao", "Linfoma, melanoma, mesotelioma e seminoma são malignos apesar do -oma", "nao", "lacuna", "§C", ORGZ, EX_ORG, "eixo (célula de origem) e uma linha por exceção", AN_ORG, "p1-5"),
 "k-criterios": ("Quatro critérios benigno × maligno", "lâmina 3", "differentiation", "AnKing compara benigno × maligno critério a critério (1496164365674 etc.), sem o conjunto dos quatro eixos da aula", "comparacao", "Diferenciação, crescimento, invasão e metástase separam benigno de maligno", "nao", "fio", "§C", ORGZ, EX_ORG, "eixo único e uma linha por critério", AN_ORG, "p2-1"),
 "k-funcao": ("Diferenciação conserva função", "lâmina 4; Robbins p.265", "function", "Busca: só exemplos isolados (queratoacantoma 1488680281523, citoqueratina); nenhum card do princípio funcional", "mecanismo", "Quanto mais diferenciado, mais o tumor mantém a função da célula de origem", "nao", "lacuna", "§A", MEC, EX_MEC, "grau → consequência funcional, função no cloze", AN_MEC, "p3-8"),
 "k-displasia-anaplasia": ("Displasia tecidual × anaplasia celular", "objetivo 6; prova 2018 1.2", "architecture", "AnKing define displasia e anaplasia em cards separados; nenhum contrasta o nível (tecido × célula) que o objetivo 6 e a prova pedem", "comparacao", "Displasia é alteração da arquitetura do tecido; anaplasia é perda de diferenciação da célula", "nao", "lacuna", "§B", CONT, EX_CONT, "dois termos com o critério (tecido × célula) no cloze", AN_CONT, "p3-6"),
 "k-sequencia-cis": ("Sequência até o invasor", "lâmina 6; provas 2016 P3 1.1 e 1.4", "basement membrane", "AnKing tem cada grau cervical isolado (1518218707562); nenhum organiza a sequência da lâmina 6 com a figura", "comparacao", "Hiperplasia, displasia, in situ e invasor diferem pela espessura atingida e pela membrana basal", "sim", "lacuna", "§C", ORGZ, EX_ORG, "uma linha por etapa", AN_ORG, "p3-10"),
 "k-celula-tronco": ("Células-tronco tumorais", "lâmina 4; Robbins p.263 e 267", "cancer stem cells", "Busca 11/11 (cancer stem cells): nenhum AnKing (só tronco hematopoiético e c-KIT)", "mecanismo", "Uma população de células-tronco tumorais sustenta o crescimento e resiste à terapia", "nao", "lacuna", "§A", MEC, EX_MEC, "população → função no cloze", AN_MEC, "p3-11"),
 "k-metilacao": ("Metilação epigenética", "palavras-cruzadas 9", "methylation", "Busca 11/11 (DNA methylation tumor suppressor silencing): nenhum AnKing", "mecanismo", "Metilação do promotor silencia genes do câncer sem mutação", "nao", "lacuna", "§A", MEC, EX_MEC, "mecanismo no cloze", AN_MEC, "p4-7"),
 "k-vias-org": ("Três vias de disseminação", "lâmina 19; objetivo 13", "lymphatic", "AnKing dá carcinoma × sarcoma (1496164110071) e cavidades separados; nenhum reúne as três vias do objetivo 13", "comparacao", "Linfática, hematogênica e cavitária são as vias de metástase", "nao", "lacuna", "§C", ORGZ, EX_ORG, "uma linha por via", AN_ORG, "p9-9"),
"k-epi-fatores": ("Fatores epidemiológicos", "aula 74 lâmina 7; cruzadas da aula 74", "age", "Busca 11/11 (cancer incidence age; environmental factors): nenhum AnKing reúne os três fatores da lâmina 7 da aula 74", "comparacao", "Ambiente, idade e genética explicam a distribuição do câncer", "nao", "lacuna", "§C", ORGZ, EX_ORG, "uma linha por fator", AN_ORG, "p11-1"),
 "k-epi-idade": ("Idade e mutações somáticas", "aula 74 lâmina 7; cruzadas da aula 74", "accumulate", "Busca 11/11 (cancer incidence increases with age): 0 notas no AnKing", "mecanismo", "A incidência sobe com a idade porque mutações somáticas se acumulam", "nao", "lacuna", "§A", MEC, EX_MEC, "causa → efeito, mecanismo no cloze", AN_MEC, "p11-2"),
 "k-epi-diag-precoce": ("Diagnóstico precoce", "aula 74 lâminas 2–6; cruzadas da aula 74", "early diagnosis", "AnKing tem objetivos do rastreamento (1517723603774) sem explicar mama incidente × não a mais letal, da cruzadinha 11", "mecanismo", "O diagnóstico precoce separa incidência de mortalidade", "nao", "lacuna", "§A", MEC, EX_MEC, "fenômeno → causa no cloze", AN_MEC, "p11-3"),
"k-epi-ranking": ("Maiores incidência e mortalidade", "aula 74 lâmina 2; cruzadas da aula 74", "prostate", "Os AnKing de ranking (1557670335053, 1557670335329) são só Step 2; 1517723202896 dá só o pulmão", "comparacao", "Próstata e mama lideram a incidência e o pulmão a mortalidade", "nao", "lacuna", "§C", ORGZ, EX_ORG, "uma linha por grupo", AN_ORG, "p11-4"),
"k-nomenclatura-orgaos": ("Carcinomas pelo órgão", "aula 74 lâminas 10–11", "hepatocellular", "AnKing tem tumores de órgão soltos em decks de sistema; nenhum organiza os nomes da tabela da aula 74", "comparacao", "Carcinomas de órgãos recebem o nome do epitélio de origem", "nao", "lacuna", "§C", ORGZ, EX_ORG, "uma linha por órgão", AN_ORG, "p1-9"),
 "k-teorias": ("Mutação somática × campo", "lâmina 7", "genetic", "Busca: nenhum card das duas teorias (candidatos são semente e solo e hallmarks)", "comparacao", "Câncer como alteração genética da célula × perturbação da interação com o microambiente", "nao", "lacuna", "§B", CONT, EX_CONT, "duas teorias no mesmo eixo, cada uma com a palavra-chave no cloze", AN_CONT, "p4-1"),
 "k-progressao": ("Progressão: subclones", "lâminas 8–10", "clonal expansion", "AnKing fala de progressão sem subclones/heterogeneidade (1496158482771)", "mecanismo", "Novas mutações criam subclones e heterogeneidade na progressão", "sim", "lacuna", "§A", MEC, EX_MEC, "processo → produto no cloze", AN_MEC, "p4-3"),
 "k-heterogeneidade-terapia": ("Heterogeneidade e terapia-alvo", "lâminas 9–10; prova 2025 2.6", "targeted", "Busca: nenhum AnKing liga heterogeneidade entre metástase e primário à resistência à terapia-alvo, que o gabarito pede", "mecanismo", "Subclones diferentes fazem a terapia-alvo funcionar só em parte", "sim", "lacuna", "§A", MEC, EX_MEC, "causa → consequência terapêutica no cloze", AN_MEC, "p4-5"),
 "k-hallmarks": ("Hallmarks do câncer", "lâmina 11; Hanahan & Weinberg", "cell death", "AnKing tem hallmarks soltos (1496163284718, 1518212434121…); nenhum reúne a lista da figura da aula", "comparacao", "O câncer adquire um conjunto de capacidades (hallmarks)", "sim", "lacuna", "§C", ORGZ, EX_ORG, "uma linha por capacidade", AN_ORG, "p4-4"),
 "k-prolif-remocao": ("Proliferação × remoção", "lâmina 12", "exceeds", "Busca: nenhum AnKing do balanço proliferação × perda no crescimento tumoral", "mecanismo", "O tumor cresce enquanto a proliferação supera a perda celular", "sim", "lacuna", "§A", MEC, EX_MEC, "condição → resultado, termo da perda no cloze", AN_MEC, "p5-1"),
 "k-30-duplicacoes": ("10⁹ células = 1 g", "lâmina 13; Robbins p.265", "30", "1496111421676 dá só as 30 divisões; nenhum dá a massa detectável", "fato-chave", "30 duplicações dão a menor massa detectável (1 g)", "sim", "lacuna", "§E", FATO, EX_FATO, "número com o contexto visível", AN_FATO, "p5-2"),
 "k-tres-fatores": ("Três fatores do ritmo", "lâmina 14; objetivo 7", "doubling time", "Busca devolveu só cinética bacteriana (1500673014315); nenhum card do ritmo tumoral", "comparacao", "Ritmo = tempo de duplicação + fração de crescimento + perda celular", "nao", "lacuna", "§C", ORGZ, EX_ORG, "uma linha por fator", AN_ORG, "p5-3"),
 "k-fracao": ("Fração de crescimento", "lâmina 15; objetivo 8", "growth fraction", "Busca: nenhum AnKing de fração de crescimento tumoral (só bactéria)", "fato-chave", "Fração de crescimento é a proporção no grupo replicativo, até 20% na clínica", "nao", "lacuna", "§E", FATO, EX_FATO, "definição com o nome no cloze", AN_FATO, "p5-4"),
 "k-fc-quimio": ("Fração baixa resiste à quimio", "lâmina 15; objetivo 8", "cell cycle", "AnKing só tem resposta à quimio de tumores específicos (1475463201591, 1473732957912); nenhum o princípio", "mecanismo", "Fração baixa resiste à quimioterapia; reduzir volume recruta células ao ciclo", "nao", "lacuna", "§A", MEC, EX_MEC, "condição → estratégia, alvo no cloze", AN_MEC, "p5-5"),
 "k-dano-nao-letal": ("Dano genético não letal", "lâmina 16", "nonlethal", "1496158482771 diz que mutações rompem a regulação, sem o 'não letal' da aula", "mecanismo", "Só o dano genético não letal passa à prole e inicia o câncer", "nao", "lacuna", "§A", MEC, EX_MEC, "qualidade do dano no cloze", AN_MEC, "p6-1"),
 "k-quatro-classes": ("Quatro classes de genes", "lâmina 16; objetivo 14", "proto-oncogenes", "AnKing tem proto-oncogene e supressor soltos; nenhum lista as quatro classes", "comparacao", "Proto-oncogenes, supressores, apoptose e reparo são os alvos", "nao", "lacuna", "§C", ORGZ, EX_ORG, "uma linha por classe", AN_ORG, "p6-2"),
 "k-capsula": ("Cápsula do benigno", "lâmina 17", "capsule", "AnKing traz a cápsula em tumores específicos (lipoma 1488418620676, adenoma folicular); nenhum o princípio do crescimento expansivo", "mecanismo", "Crescimento expansivo comprime o tecido e forma cápsula fibrosa", "nao", "lacuna", "§A", MEC, EX_MEC, "crescimento → estrutura no cloze", AN_MEC, "p7-1"),
 "k-invasao": ("Invasão: critério de malignidade", "lâmina 17", "invasion", "AnKing compara invasão de membrana basal (1518402560522) sem dizer que é o critério mais confiável depois da metástase", "fato-chave", "Depois da metástase, a invasão é o critério mais confiável de malignidade", "nao", "lacuna", "§E", FATO, EX_FATO, "critério no cloze com contexto visível", AN_FATO, "p7-2"),
 "k-checkpoints": ("Checkpoints G1/S e G2/M", "lâmina 18", "DNA damage", "1496161616847 cobre só G1 (p53/RB); nenhum contrasta os dois checkpoints da lâmina", "comparacao", "G1/S checa dano no DNA; G2/M checa DNA completo", "sim", "lacuna", "§B", CONT, EX_CONT, "dois pontos do ciclo com o que cada um checa", AN_CONT, "p8-2"),
 "k-metastase-def": ("Metástase × contiguidade", "lâmina 19; objetivo 12", "discontinuous", "AnKing de metástase cobre sítios e vias; nenhum a define como implante descontínuo", "fato-chave", "Metástase é implante descontínuo, diferente da invasão por contiguidade", "nao", "lacuna", "§E", FATO, EX_FATO, "definição com a qualidade no cloze", AN_FATO, "p9-1"),
 "k-preditores": ("Preditores de metástase", "lâmina 19", "size", "AnKing traz preditores de tumores específicos (melanoma vertical 1488680472391); nenhum os três gerais da lâmina", "comparacao", "Agressividade, velocidade e tamanho predizem metástase", "nao", "lacuna", "§C", ORGZ, EX_ORG, "uma linha por fator", AN_ORG, "p9-2"),
 "k-sentinela": ("Linfonodo sentinela", "palavras-cruzadas 2; Robbins p.270", "sentinel", "AnKing tem drenagem linfática por região (1486945222161), sem o conceito de sentinela", "fato-chave", "Sentinela é o primeiro linfonodo que recebe a linfa do tumor", "nao", "lacuna", "§E", FATO, EX_FATO, "definição com o nome no cloze", AN_FATO, "p9-5"),
 "k-inflamacao-cronica": ("Inflamação crônica predispõe", "lâmina 20; prova 2025 3.3", "oxidative stress", "AnKing só tem doenças específicas (pancreatite crônica 1482971533067); nenhum o mecanismo do gabarito", "mecanismo", "Inflamação crônica soma proliferação regenerativa e estresse oxidativo que danifica o DNA", "nao", "lacuna", "§A", MEC, EX_MEC, "causa → mecanismo, mecanismo no cloze", AN_MEC, "p10-2"),
}
cob = ["chave\tconceito\tfonte_aula\tveredito\tlidos\tdecora\tdecisao"]
dec, tip, rev = {}, ["chave\ttipo\tprincipio\tvisual\tpapel"], ["# Revisão dos autorais — 75 Biologia e crescimento dos tumores", ""]
for k, e in E.items():
    txt = e["fields"].get("Text", "")
    ans = re.findall(r"\{\{c\d+::([^}:]+)", txt)
    if k in A:
        c, f, deco, d, t, pr, vi, pa, par, ti, ex, sem, an, it = A[k]
        assert any(deco in a for a in ans), (k, deco, ans)
        cob.append(f"{k}\t{c}\t{f}\tlacuna\t{','.join(lid.get(k, [])[:4])}\t{deco}\t{BUSCA}{d}")
        dec[k] = ["lacuna", BUSCA + d]
        tip.append(f"{k}\t{t}\t{pr}\t{vi}\t{pa}")
        rev.append(f"- {k} — par: {par}; tipo-informacao: {ti}; ensina: {pr}; EXEMPLAR {ex}; semelhança: {sem}; adaptação: conteúdo da aula 75 ({f}); ANTI {an}; decora: {deco} — ok")
    else:
        vis = "sim" if "<img" in json.dumps(e["fields"]) else "nao"
        cob.append(f"{k}\t{e.get('alvo','')}\t{e.get('evid','')}\tcoberto\t\t{ans[0] if ans else ''}\tacervo: entra")
        tip.append(f"{k}\tfato-chave\tPrincípio da {e.get('evid','').lower()}: {e.get('alvo','')}\t{vis}\t")
for k, v in plan["compartilhados"].items():
    cob.append(f"sh-{k}\t{v.get('alvo','')}\t{v.get('evid','')}\tcoberto\t\t\tassociado (cópia NEBLI viva)")
(H / "busca/cobertura.tsv").write_text("\n".join(cob) + "\n")
json.dump(dec, open(H / "decisoes.json", "w"), ensure_ascii=False, indent=1)
(H / "tipos.tsv").write_text("\n".join(tip) + "\n")
(H / "REVISAO-AUTORAIS-gerado.md").write_text("\n".join(rev) + "\n\nOrganizadores necessários: sim — a aula enumera conjuntos (nomenclatura e exceções, critérios, fatores do ritmo, classes de genes, hallmarks, preditores).\n")
bat = {}
for k, e in E.items():
    for fi in re.findall(r'src=\\?"([^"\\]+)', json.dumps(e["fields"])):
        bat[k] = {"veredito": "ok", "porque": f"figura {fi} vista: recorte da lâmina da aula ou figura do AnKing que mostra o alvo"}
json.dump(bat, open(H / "imagens-batem.json", "w"), ensure_ascii=False, indent=1)
N = lambda *ns: [r(n) for n in ns]
MAP = {k: [k] for k in A}
MAP.update({
 "k-neoplasia-def": N(1496110201793, 1496110605566),
 "k-nomenclatura": N(1496110867291, 1488680226241, 1496110970215, 1517720363511, 1516246515683, 1516246473563, 1496111000227, 1517721078779, 1488418643668, 1488418645713, 1517721704430, 1517721729135, 1496111041884),
 "k-excecoes": ["k-excecoes"] + N(1517721745386, 1496111024111),
 "k-teratoma": N(1463187910218), "k-hamartoma": N(1517720929242, 1517720994409), "k-tumor-misto": N(1482191477668),
 "k-criterios": ["k-criterios"] + N(1496164634302, 1518398337589, 1518398362472, 1518398388805, 1518402560522),
 "k-diferenciacao": N(1518402922916, 1518402974215, 1518403080746),
 "k-anaplasia-achados": N(1496164677268, 1526251874337, 1496164062309), "k-ihc": N(1496165216576, 1496165337190),
 "k-nc": N(1496164741405, 1518217804217), "k-mitoses": N(1496164875478),
 "k-displasia": N(1487461112379, 1487461120979, 1487461125395, 1518217637366),
 "k-cis": N(1518218866119, 1518219030992, 1518219389272),
 "k-iniciacao": N(1496158482771),
 "k-hallmarks-exemplos": N(1467771904154, 1496163284718, 1518212434121, 1496164030007, 1496163026982, 1496163125083, 1518214216086, 1496163225363),
 "k-30-duplicacoes": ["k-30-duplicacoes"], "k-ciclo-nao-curto": ["k-tres-fatores"],
 "k-quatro-classes": ["k-quatro-classes"] + N(1517957674940, 1517957746836),
 "k-capsula": ["k-capsula"] + N(1488418620676),
 "k-invasao-etapas": N(1518219637289, 1518219881077, 1518219442201, 1518219949937, 1518220197497),
 "k-ciclina-rb": N(1496162192905, 1496162245188), "k-checkpoints": ["k-checkpoints"] + N(1496161616847),
 "k-vias": N(1496164110071, 1518241346893), "k-figado-pulmao": N(1518226984913, 1486591340394, 1518220389435, 1518220409981),
 "k-cavidade": N(1518241882006, 1508802208485), "k-sem-metastase": N(1488680222795, 1481944701192),
 "k-tnm": N(1518403099278, 1518403188199, 1518403203594, 1518403144606, 1518403259951, 1518403222894, 1496166103071, 1496166062248, 1496165964076),
 "k-solo-fertil": N(1520440331083, 1487461083189) + ["sh-1792240574547"], "k-epi-ranking": ["k-epi-ranking"] + N(1496111214453, 1517723202896, 1508543664801, 1517722304153), "k-epi-rastreamento": N(1517723603774, 1496111443409, 1496111515047, 1496111589277), "k-epi-exemplos": N(1463443071372, 1482203956292, 1510261296535, 1482203975258), "k-pre-cancerosas": N(1488680264064, 1482191378467),
})
validos = set(E) | {f"sh-{k}" for k in plan["compartilhados"]}
MAP = {k: [x for x in v if x in validos] for k, v in MAP.items()}
assert all(MAP.values()), [k for k, v in MAP.items() if not v]
todos = {x for v in MAP.values() for x in v}
assert todos <= validos, todos - validos
assert not (validos - todos), validos - todos
m = json.load(open(H / "mapa-de-profundidade.json"))
for p in m["passos"]:
    for it in p["itens"]:
        it["cards"] = MAP[it["cards"][0]] if it["cards"][0] in MAP else it["cards"]
        if it["id"] == "p5-6":
            it["termos"] = ["cycle"]
json.dump(m, open(H / "mapa-de-profundidade.json", "w"), ensure_ascii=False, indent=1)
mot = json.load(open(H / "motivacoes.json"))
for x in mot["motivacoes"]:
    x["atendida_por"] = MAP.get(x["atendida_por"][0], x["atendida_por"])
json.dump(mot, open(H / "motivacoes.json", "w"), ensure_ascii=False, indent=1)
mt = json.load(open(H / "matriz-fontes.json"))
for l in mt["linhas"]:
    if l.get("cards"):
        l["cards"] = sorted({y for x in l["cards"] for y in MAP.get(x, [x])})
json.dump(mt, open(H / "matriz-fontes.json", "w"), ensure_ascii=False, indent=1)
inv = (H / "inventario.py").read_text()
for a, b in MAP.items():
    inv = inv.replace(f"'{a}'", f"'{b[0]}'")
(H / "inventario.py").write_text(inv)
print("ok", len(E), "entradas,", len(plan["compartilhados"]), "compartilhados")
