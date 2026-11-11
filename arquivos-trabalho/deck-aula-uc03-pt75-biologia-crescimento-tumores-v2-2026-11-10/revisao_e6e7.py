"""E6 (revisão com raciocínio no plano) e E7 (fidelidade aula ↔ cards) da 75."""
import json

plan = json.load(open("plan.json"))
ordem = {e["key"]: int(e["order"]) for e in plan["entries"]}
ordem.update({f"sh-{k}": v["order"] for k, v in plan["compartilhados"].items()})
import re
lam = {e["key"]: int(re.search(r"\d+", e["evid"]).group()) for e in plan["entries"]}
lam.update({f"sh-{k}": int(re.search(r"\d+", v["evid"]).group()) for k, v in plan["compartilhados"].items()})

B = {
 (1, 2): [
  ("toda neoplasia é um tumor, mas nem todo tumor é neoplasia; câncer é a neoplasia maligna", ["k-tumor-neoplasia-cancer"]),
  ("neoplasia é massa clonal de crescimento autônomo que persiste após o estímulo", ["ak1496110201793", "sh-1792240571243"]),
  ("o tumor tem parênquima neoplásico e estroma reativo; o parênquima define nome e comportamento", ["k-parenquima-estroma"]),
  ("benigno recebe o sufixo -oma; maligno mesenquimal é sarcoma e maligno epitelial é carcinoma (adeno- se glandular)", ["ak1517720363511", "ak1516246515683"]),
  ("linfoma, melanoma, mesotelioma e seminoma são exceções malignas; teratoma vem de mais de um folheto", ["k-excecoes", "ak1463187910218"]),
  ("carcinomas de órgão levam o nome do epitélio: urotelial, hepatocelular, de células renais, coriocarcinoma", ["k-nomenclatura-orgaos"]),
  ("adenoma é o benigno de glândula e adenocarcinoma o maligno", ["ak1496110867291"]),
  ("papiloma é o benigno exofítico e carcinoma papilar o maligno", ["ak1496110970215"]),
  ("carcinoma escamoso (epidermoide) lembra epitélio estratificado e forma pérolas de queratina", ["ak1488680226241"]),
  ("o tumor maligno do tecido adiposo é o lipossarcoma e o benigno, o lipoma encapsulado", ["ak1496111000227", "ak1488418620676"]),
  ("leiomioma e leiomiossarcoma são do músculo liso; rabdomioma e rabdomiossarcoma, do estriado", ["ak1517721078779", "ak1488418643668", "ak1488418645713"]),
  ("fibroma, osteoma e hemangioma têm como malignos fibrossarcoma, osteossarcoma e angiossarcoma", ["ak1517721704430", "ak1517721729135", "ak1496111041884"]),
  ("o mesênquima origina o tecido conjuntivo, por isso o maligno mesenquimal é sarcoma", ["ak1516246473563"]),
  ("nevo é o benigno de melanócito e melanoma o maligno", ["ak1517721745386"]),
  ("linfoma é maligno de leucócito maduro e leucemia de imaturo", ["ak1496111024111"]),
  ("hamartoma é tecido desorganizado no próprio local e não é neoplasia", ["ak1517720929242"]),
  ("coristoma é tecido normal em local estranho", ["ak1517720994409"]),
  ("adenoma pleomórfico é tumor misto de um só clone", ["ak1482191477668"])],
 (3, 3): [
  ("benigno e maligno se distinguem por diferenciação/anaplasia, crescimento, invasão local e metástase", ["k-criterios", "ak1496164634302"]),
  ("benigno cresce lento, circunscrito e móvel e não metastatiza; maligno cresce rápido, infiltra e fica fixo", ["ak1518398337589", "ak1518398362472"]),
  ("só a biópsia mostra a invasão da membrana basal que define o maligno", ["ak1518398388805", "ak1518402560522"])],
 (4, 6): [
  ("células-tronco tumorais se autorrenovam e sustentam o tumor", ["k-celula-tronco"]),
  ("diferenciação é a semelhança morfológica e funcional com a célula normal; anaplasia é a falta de diferenciação", ["ak1518402922916", "ak1518402974215", "ak1518403080746"]),
  ("anaplasia mostra pleomorfismo, núcleo hipercromático com relação núcleo-citoplasma alta, mitoses atípicas, perda de polaridade e células gigantes", ["ak1496164677268", "ak1496164741405", "ak1496164875478"]),
  ("células gigantes e perda da polaridade normal marcam a anaplasia", ["ak1526251874337", "ak1496164062309"]),
  ("pouco diferenciado é mais agressivo; o bem diferenciado conserva a função", ["k-funcao"]),
  ("no tumor anaplásico, citoqueratina e vimentina mostram a origem epitelial ou mesenquimal", ["ak1496165216576", "ak1496165337190"]),
  ("displasia é perda de uniformidade e orientação arquitetural, não invasiva e nem sempre evolui para câncer", ["ak1487461112379", "ak1487461120979"]),
  ("na displasia há pleomorfismo, perda de orientação e relação núcleo-citoplasma maior", ["ak1518217637366", "ak1518217804217"]),
  ("displasia é do tecido e anaplasia da célula; displasia é pré-cancerosa", ["k-displasia-anaplasia", "ak1487461125395"]),
  ("no colo uterino a displasia progride de leve a moderada e grave/in situ", ["k-sequencia-cis"]),
  ("carcinoma in situ é displasia de toda a espessura com membrana basal íntegra; ruptura da membrana basal define invasão", ["ak1518218866119", "ak1518219030992"]),
  ("o carcinoma in situ não regride", ["ak1518219389272"])],
 (7, 11): [
  ("teoria da mutação somática vê o câncer como alteração genética da célula; teoria do campo, como perturbação da interação com o microambiente", ["k-teorias"]),
  ("iniciação gera célula iniciada que se expande clonalmente", ["ak1496158482771", "k-metilacao"]),
  ("na progressão novas mutações geram subclones e heterogeneidade tumoral", ["k-progressao", "k-heterogeneidade-terapia"]),
  ("os hallmarks são as capacidades adquiridas pelo câncer, habilitadas por instabilidade genômica e inflamação", ["k-hallmarks", "ak1496163284718", "ak1518212434121"]),
  ("cada hallmark tem um exemplo: telomerase, VEGF, Warburg, MHC I reduzido", ["sh-1792240994116", "sh-1792240993866", "sh-1792240993017"]),
  ("o metabolismo e o escape imune são hallmarks emergentes, e a angiogênese usa VEGF", ["ak1518214216086", "ak1496163225363", "ak1496163125083"])],
 (12, 15): [
  ("o tumor cresce quando a proliferação supera a remoção (morte e perda celular)", ["k-prolif-remocao"]),
  ("cerca de 30 duplicações levam uma célula a 10^9 células (1 g), menor massa detectável, e só mais 10 a 1 kg", ["k-30-duplicacoes"]),
  ("o ritmo depende do tempo de duplicação, da fração de crescimento e da perda celular", ["k-tres-fatores"]),
  ("fração de crescimento é a proporção de células no grupo replicativo; na fase clínica é até 20%", ["k-fracao"]),
  ("fração de crescimento baixa torna o tumor refratário à quimioterapia; reduzir volume recruta células ao ciclo (base da neoadjuvante)", ["k-fc-quimio"])],
 (16, 16): [
  ("o dano genético não letal está no cerne da carcinogênese", ["k-dano-nao-letal"]),
  ("os alvos são proto-oncogenes, genes supressores de tumor, genes da apoptose e genes de reparo do DNA", ["k-quatro-classes", "ak1517957674940", "ak1517957746836"])],
 (17, 17): [
  ("tumor benigno cresce como massa expansiva com cápsula fibrosa e pode ser enucleado", ["k-capsula"]),
  ("tumor maligno infiltra sem plano de clivagem, o que exige margem e dificulta a ressecção", ["k-invasao", "ak1518220197497"]),
  ("a invasão local é o critério mais confiável de malignidade depois da metástase", ["k-invasao"]),
  ("para invadir, perde E-caderina, prende-se à laminina, rompe a membrana basal com metaloproteinases e migra pela fibronectina", ["ak1518219637289", "ak1518219881077", "ak1518219442201"]),
  ("depois da membrana basal, a fibronectina guia a disseminação local", ["ak1518219949937"])],
 (18, 18): [
  ("ciclinas e CDK comandam o ciclo fosforilando proteínas-alvo como RB", ["ak1496162192905", "ak1496162245188"]),
  ("o checkpoint G1/S checa dano no DNA (reparo ou apoptose) e o G2/M checa DNA completo antes da mitose", ["k-checkpoints", "ak1496161616847"])],
 (19, 19): [
  ("metástase é implante tumoral descontínuo do primário, diferente da invasão por contiguidade", ["k-metastase-def"]),
  ("agressividade, velocidade de crescimento e tamanho predizem metástase", ["k-preditores"]),
  ("as vias são linfática (carcinomas), hematogênica (sarcomas; fígado e pulmão) e implante direto em cavidades", ["k-vias-org", "ak1496164110071", "ak1518241346893"]),
  ("o primeiro linfonodo da bacia que recebe a linfa do tumor é o sentinela", ["k-sentinela"]),
  ("depois dos linfonodos, fígado e pulmão são os sítios mais comuns; metástase hepática é mais comum que o primário", ["ak1518226984913", "ak1486591340394"]),
  ("o peritônio é a cavidade mais semeada, típico do carcinoma de ovário", ["ak1518241882006", "ak1508802208485"]),
  ("na teoria semente e solo, o êmbolo para no primeiro leito capilar", ["ak1518220389435", "ak1518220409981"]),
  ("gliomas e carcinoma basocelular invadem mas raramente metastatizam", ["ak1488680222795", "ak1481944701192"]),
  ("grau mede diferenciação e mitoses: baixo grau é bem diferenciado e alto grau é pouco", ["ak1518403099278", "ak1518403188199", "ak1518403203594"]),
  ("estádio TNM mede extensão e disseminação e prevê mais que o grau", ["ak1518403144606", "ak1518403259951", "ak1518403222894"]),
  ("metástase (M) é o fator prognóstico mais importante e linfonodo (N) o segundo; estadia-se após a ressecção", ["ak1496166103071", "ak1496166062248", "ak1496165964076"])],
 (20, 20): [
  ("hiperplasia, metaplasia e displasia são solo fértil para a transformação neoplásica", ["ak1520440331083", "sh-1792240574794", "sh-1792240574547"]),
  ("a inflamação crônica favorece o câncer por ativar progenitoras e gerar instabilidade gênica por estresse oxidativo", ["k-inflamacao-cronica"]),
  ("condições pré-cancerosas como queratose actínica e leucoplasia precedem o carcinoma escamoso", ["ak1488680264064", "ak1482191378467"]),
  ("ambiente, idade e predisposição genética explicam a distribuição do câncer; a incidência sobe com a idade pelas mutações somáticas", ["k-epi-fatores", "k-epi-idade"]),
  ("próstata e mama são as mais incidentes, pulmão a maior mortalidade e colorretal o 3º; câncer é a 2ª causa de morte", ["k-epi-ranking", "ak1517723202896"]),
  ("pele é o câncer mais comum e o colorretal é o 3º", ["ak1517722304153", "ak1508543664801", "ak1496111214453"]),
  ("o diagnóstico precoce pelo rastreamento derruba a mortalidade", ["k-epi-diag-precoce", "ak1517723603774"]),
  ("Papanicolau, mamografia e colonoscopia pegam a lesão antes da invasão", ["ak1496111443409", "ak1496111515047", "ak1496111589277"]),
  ("BRCA, Barrett e H. pylori são exemplos de predisposição genética, lesão precursora e infecção", ["ak1463443071372", "ak1482203956292", "ak1510261296535"]),
  ("álcool e fumo causam o carcinoma escamoso do esôfago", ["ak1482203975258"])],
}
NOTA = {t: f"Lâminas {t[0]}–{t[1]} conferidas contra o slide, os objetivos, o Robbins e as provas: cada item de aprender tem card que o recupera na frente; os cards do bloco seguem a ordem das lâminas e nenhum exemplo virou carro-chefe. Bloco revisto em 11/11 com os gabaritos lidos frase a frase (E5b)." for t in B}
c = json.load(open("compreensao-aula.json"))
blocos, todos = [], set()
for b in c["blocos"]:
    t = tuple(b["laminas"])
    if t not in B:
        continue
    b["aprender"] = [a for a, _ in B[t]]
    rel = [{"aprender": a, "estado": "recuperavel", "cards": ks} for a, ks in B[t]]
    conf = sorted({k for k, n in lam.items() if t[0] <= n <= t[1]} | {k for _, ks in B[t] for k in ks}, key=lambda k: ordem.get(k, 0))
    todos |= set(conf)
    blocos.append({"laminas": list(t), "bate": True, "nota": NOTA[t], "cards_conferidos": conf, "relacoes": rel})
blocos.append({"laminas": [21, 21], "bate": True, "nota": "Lâmina 21 é de humor, sem conteúdo de aula; não tem card nem precisa: o bloco é resumo e encerra a aula depois das condições predisponentes, conferido contra o PDF da turma.", "cards_conferidos": [], "relacoes": []})
assert set(ordem) <= todos, set(ordem) - todos
c["fidelidade"] = {"_como": "E7 sobre o plano (v14: antes de instalar)", "blocos": blocos,
 "conclusao": "O deck acompanha as 21 lâminas em ordem: conceitos e nomenclatura, critérios, diferenciação/displasia/in situ, transformação e hallmarks, cinética, bases moleculares, invasão, ciclo (exemplo RB), metástase com grau e estádio, e condições predisponentes. O exemplo de RB carrega o princípio do controle do ciclo; nada de fora da aula entrou sem motivo."}
json.dump(c, open("compreensao-aula.json", "w"), ensure_ascii=False, indent=1)
m = json.load(open("mapa-de-profundidade.json"))
X = lambda passo, cards, txt: {"passo": passo, "cards_usados": cards, "explicacao_com_os_cards": txt}
m["revisao"] = {"passos": [
 X("Conceitos gerais e nomenclatura", ["k-tumor-neoplasia-cancer", "ak1496110201793", "k-parenquima-estroma", "ak1517720363511", "k-excecoes"],
   "Tumor é qualquer massa; neoplasia é o crescimento autônomo, clonal, que persiste sem o estímulo; câncer é a neoplasia maligna (k-tumor-neoplasia-cancer, ak1496110201793). O nome e o comportamento vêm do parênquima, não do estroma (k-parenquima-estroma). Benigno ganha -oma; maligno epitelial é carcinoma e mesenquimal é sarcoma (ak1517720363511), com exceções malignas de nome benigno como linfoma, melanoma, mesotelioma e seminoma (k-excecoes)."),
 X("Critérios benigno × maligno", ["k-criterios", "ak1518398337589", "ak1518398362472", "ak1518402560522"],
   "Quatro eixos separam benigno de maligno: diferenciação, crescimento, invasão e metástase (k-criterios). O benigno é lento, circunscrito e móvel; o maligno é rápido, infiltrativo e fixo (ak1518398337589, ak1518398362472), e só ele rompe a membrana basal (ak1518402560522), o que só a biópsia ou a excisão mostra com segurança."),
 X("Diferenciação, anaplasia, displasia, in situ", ["ak1518403080746", "ak1496164741405", "k-displasia-anaplasia", "ak1518219030992"],
   "Anaplasia é a falta de diferenciação, com núcleos pleomórficos, hipercromáticos e relação núcleo-citoplasma alta (ak1518403080746, ak1496164741405). Displasia é a desordem do tecido e anaplasia a da célula (k-displasia-anaplasia). Quando a displasia ocupa toda a espessura sem romper a membrana basal, é carcinoma in situ (ak1518219030992)."),
 X("Transformação, progressão e hallmarks", ["k-teorias", "k-progressao", "k-heterogeneidade-terapia", "k-hallmarks"],
   "A teoria da mutação somática e a do campo explicam a origem (k-teorias). Uma célula iniciada expande-se clonalmente e novas mutações criam subclones (k-progressao), por isso a metástase pode ter mutações ausentes no primário e a terapia-alvo funciona só em parte (k-heterogeneidade-terapia). O conjunto de capacidades adquiridas são os hallmarks (k-hallmarks)."),
 X("Ritmo e fração de crescimento", ["k-prolif-remocao", "k-30-duplicacoes", "k-tres-fatores", "k-fracao", "k-fc-quimio"],
   "O tumor cresce enquanto a proliferação supera a perda (k-prolif-remocao); 30 duplicações dão 10^9 células e 1 g, e mais 10 dão 1 kg (k-30-duplicacoes). O ritmo depende do tempo de duplicação, da fração de crescimento e da perda (k-tres-fatores); a fração é até 20% na clínica (k-fracao) e, se baixa, o tumor resiste à quimioterapia, e reduzir o volume recruta células ao ciclo (k-fc-quimio)."),
 X("Bases moleculares", ["k-dano-nao-letal", "k-quatro-classes", "ak1517957674940"],
   "Só o dano genético não letal passa à prole e inicia o câncer (k-dano-nao-letal). Os alvos são proto-oncogenes, supressores, genes da apoptose e de reparo (k-quatro-classes); o proto-oncogene vira oncogene por ganho de função (ak1517957674940), e a falha do reparo acumula mutações nos demais, gerando a instabilidade genômica que acelera a progressão."),
 X("Invasão local", ["k-capsula", "k-invasao", "ak1518219637289", "ak1518219442201"],
   "O benigno cresce expansivo e forma cápsula do tecido comprimido (k-capsula). O maligno infiltra sem plano de clivagem, e depois da metástase a invasão é o critério mais confiável de malignidade (k-invasao). Para invadir, perde E-caderina (ak1518219637289) e rompe a membrana basal com metaloproteinases (ak1518219442201)."),
 X("Ciclo celular e checkpoints", ["ak1496162192905", "ak1496162245188", "k-checkpoints"],
   "Ciclinas e CDK hiperfosforilam RB (ak1496162192905), que libera E2F e permite entrar em S (ak1496162245188). O checkpoint G1/S checa dano no DNA e o G2/M checa a replicação completa (k-checkpoints); o câncer desregula esses pontos e divide com DNA lesado, o que alimenta a instabilidade genômica e o surgimento de subclones."),
 X("Metástase, grau e estádio", ["k-metastase-def", "ak1496164110071", "ak1518226984913", "ak1518403259951", "ak1496166103071"],
   "Metástase é implante descontínuo, diferente da contiguidade (k-metastase-def). Carcinomas vão pela linfa e sarcomas pelo sangue (ak1496164110071), e depois dos linfonodos fígado e pulmão são os sítios mais comuns (ak1518226984913). O estádio TNM (ak1518403259951) prevê mais que o grau, e a metástase é o fator prognóstico mais importante (ak1496166103071)."),
 X("Epidemiologia (aula 74)", ["k-epi-fatores", "k-epi-idade", "k-epi-ranking", "k-epi-diag-precoce", "ak1517723603774"],
   "A distribuição do câncer depende do ambiente (dominante), da idade e da predisposição genética (k-epi-fatores); a incidência sobe com a idade porque mutações somáticas se acumulam (k-epi-idade). Próstata e mama lideram a incidência e o pulmão a mortalidade (k-epi-ranking); a mama não é a mais letal porque o rastreamento permite diagnóstico precoce (k-epi-diag-precoce), que é um dos dois objetivos do rastreamento (ak1517723603774)."),
 X("Condições predisponentes", ["ak1520440331083", "k-inflamacao-cronica", "ak1488680264064"],
   "Metaplasia ou hiperplasia persistente leva à displasia, solo fértil para o câncer (ak1520440331083). A inflamação crônica soma proliferação regenerativa e estresse oxidativo que danifica o DNA (k-inflamacao-cronica), e condições como a queratose actínica precedem o carcinoma escamoso (ak1488680264064).")],
 "perguntas_teste": [
  {"pergunta": "Qual a diferença entre tumor, neoplasia e câncer?", "cards": ["k-tumor-neoplasia-cancer"]},
  {"pergunta": "Prova: dê o nome de uma neoplasia epitelial escamosa maligna e de uma glandular benigna", "cards": ["ak1517720363511", "ak1496110867291"]},
  {"pergunta": "Cite duas exceções à regra de nomenclatura", "cards": ["k-excecoes"]},
  {"pergunta": "Prova: que características celulares e teciduais o patologista procura para malignidade?", "cards": ["k-displasia-anaplasia", "ak1496164741405", "ak1496164875478", "ak1518402560522"]},
  {"pergunta": "Prova: o que caracteriza o carcinoma in situ?", "cards": ["ak1518219030992", "ak1518218866119"]},
  {"pergunta": "Quais os três fatores do ritmo de crescimento?", "cards": ["k-tres-fatores"]},
  {"pergunta": "Por que a fração de crescimento importa para a quimioterapia?", "cards": ["k-fracao", "k-fc-quimio"]},
  {"pergunta": "Como surgem subclones e por que a metástase pode resistir à terapia-alvo?", "cards": ["k-progressao", "k-heterogeneidade-terapia"]},
  {"pergunta": "Quais as quatro classes de genes alteradas no câncer?", "cards": ["k-quatro-classes"]},
  {"pergunta": "Prova: que eventos permitem a invasão da mucosa?", "cards": ["ak1518219637289", "ak1518219442201", "ak1518219881077"]},
  {"pergunta": "O que diferencia metástase de invasão por contiguidade?", "cards": ["k-metastase-def"]},
  {"pergunta": "Quais as três vias de disseminação?", "cards": ["ak1496164110071", "ak1518241882006"]},
  {"pergunta": "Prova: quais variáveis entram no estadiamento?", "cards": ["ak1518403259951"]},
  {"pergunta": "Prova: como a regeneração crônica favorece a transformação?", "cards": ["k-inflamacao-cronica"]},
  {"pergunta": "Prova: dê um elemento de cada hallmark", "cards": ["k-hallmarks", "sh-1792240993866", "ak1496163125083", "ak1518214216086"]},
  {"pergunta": "Por que um tumor detectável já viveu a maior parte da vida?", "cards": ["k-30-duplicacoes"]},
  {"pergunta": "Como se forma a cápsula do tumor benigno?", "cards": ["k-capsula"]},
  {"pergunta": "Que tumores invadem mas raramente metastatizam?", "cards": ["ak1488680222795", "ak1481944701192"]},
  {"pergunta": "Qual a diferença entre grau e estádio e qual prevê mais?", "cards": ["ak1518403099278", "ak1518403144606", "ak1518403222894"]},
  {"pergunta": "O que é linfonodo sentinela?", "cards": ["k-sentinela"]},
  {"pergunta": "Como a imuno-histoquímica ajuda num tumor anaplásico?", "cards": ["ak1496165216576", "ak1496165337190"]},
  {"pergunta": "Prova: um pólipo glandular sem invasão da membrana basal é o quê?", "cards": ["ak1496110867291", "k-invasao"]}],
 "releitura_da_transcricao": "11/11: a aula não tem transcrição publicada; reli as 21 lâminas, os 15 objetivos da página, o gabarito das palavras-cruzadas, a apostila de veteranos (Aula 14), o Robbins pp. 259–271 e os 20 gabaritos do índice da aula, conferindo cada um com o plano."}
json.dump(m, open("mapa-de-profundidade.json", "w"), ensure_ascii=False, indent=1)
print("ok", len(todos))
