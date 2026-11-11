"""E3 da 75 Biologia e crescimento dos tumores: uma tabela de itens gera inventario.py, mapa-de-profundidade.json,
motivacoes.json, escopo.json e matriz-fontes.json. Chaves k-* são conceitos; a E4 decide AnKing (ak/sh) ou autoral."""
import json
import pathlib

H = pathlib.Path(__file__).parent

# passo: (título, lâminas, [(id, tipo, o que, fonte, termos, chave)])
PASSOS = [
 ("Conceitos gerais e nomenclatura", "1-2", [
  ("p1-1", "distinguir", "Toda neoplasia é um tumor, mas nem todo tumor é neoplasia; câncer é a neoplasia maligna.", "lâmina 2; objetivo 1; palavras-cruzadas 22", ["neoplasia"], "k-tumor-neoplasia-cancer"),
  ("p1-2", "explicar", "Neoplasia é massa de crescimento excessivo e autônomo que persiste após cessar o estímulo, porque a alteração genética passa às filhas (clonal).", "Robbins p.260; lâmina 2", ["clonal"], "k-neoplasia-def"),
  ("p1-3", "distinguir", "O tumor tem parênquima (células neoplásicas, que dão nome e comportamento) e estroma reativo; estroma colagenoso abundante é desmoplasia.", "lâmina 2; Robbins p.260", ["parenchyma"], "k-parenquima-estroma"),
  ("p1-4", "organizar", "Nomenclatura: benigno -oma (adenoma, papiloma, lipoma, leiomioma); maligno epitelial carcinoma (adenocarcinoma, carcinoma de células escamosas), mesenquimal sarcoma.", "objetivos 2–3; Robbins p.260–261 e tabela 7-1; palavras-cruzadas 3, 20, 21", ["carcinoma", "sarcoma"], "k-nomenclatura"),
  ("p1-9", "organizar", "Carcinomas nomeados pelo órgão: urotelial, hepatocelular, de células renais, coriocarcinoma.", "aula 74 lâminas 10–11; Robbins tabela 7-1", ["hepatocellular"], "k-nomenclatura-orgaos"),
  ("p1-5", "decorar", "Exceções: linfoma, melanoma, mesotelioma e seminoma são malignos com nome de benigno.", "objetivo 4; Robbins p.262; palavras-cruzadas 11, 29", ["melanoma"], "k-excecoes"),
  ("p1-6", "decorar", "Teratoma tem tecidos de mais de um folheto germinativo (células totipotentes).", "Robbins p.261–262; palavras-cruzadas 12", ["teratoma"], "k-teratoma"),
  ("p1-7", "distinguir", "Hamartoma é massa desorganizada de tecido do próprio local; coristoma é resto heterotópico de tecido normal.", "Robbins p.262 (exceções)", ["hamartoma"], "k-hamartoma"),
  ("p1-8", "decorar", "Adenoma pleomórfico (tumor misto) vem de um clone que diferencia em epitélio e mioepitélio.", "Robbins p.261", ["pleomorphic adenoma"], "k-tumor-misto"),
 ]),
 ("Os quatro eixos: critérios de malignidade", "3", [
  ("p2-1", "organizar", "Benigno e maligno se separam por diferenciação/anaplasia, taxa de crescimento, invasão local e metástase.", "lâmina 3; objetivo 10; Robbins p.262", ["metastasis"], "k-criterios"),
  ("p2-2", "explicar", "Metástase define malignidade sem dúvida; invasão é o critério mais confiável depois dela.", "lâmina 3; Robbins p.268–269; prova 2018 1.2", ["metastasis"], "k-criterios"),
  ("p2-3", "distinguir", "Benigno cresce lento, circunscrito e móvel; maligno rápido, infiltrativo e fixo.", "lâmina 3; objetivo 11", ["mobile"], "k-criterios"),
 ]),
 ("Diferenciação, anaplasia, displasia e carcinoma in situ", "4-6", [
  ("p3-1", "explicar", "Diferenciação é a semelhança morfológica e funcional com a célula normal; anaplasia é a falta dela, marca de malignidade.", "lâmina 4; objetivo 5; Robbins p.262–263; palavras-cruzadas 7, 14", ["anaplasia"], "k-diferenciacao"),
  ("p3-2", "organizar", "Anaplasia: pleomorfismo, núcleo hipercromático e grande, mitoses atípicas, perda de polaridade, células gigantes.", "lâmina 4; objetivo 5; Robbins p.263–264; prova 2018 1.2; palavras-cruzadas 24, 26", ["pleomorphic"], "k-anaplasia-achados"),
  ("p3-3", "decorar", "Na anaplasia a relação núcleo-citoplasma chega a 1:1 (normal 1:4 a 1:6).", "Robbins p.263; prova 2017 1.4", ["nuclear"], "k-nc"),
  ("p3-4", "distinguir", "Mitose não define malignidade (medula, hiperplasia); mitoses atípicas e bizarras sim.", "lâmina 4; Robbins p.264; palavras-cruzadas 15", ["atypical"], "k-mitoses"),
  ("p3-5", "explicar", "Displasia é perda da uniformidade e da orientação arquitetural, não invasiva, nem sempre progride (leve pode regredir).", "lâmina 5; objetivo 6; Robbins p.265", ["dysplasia"], "k-displasia"),
  ("p3-6", "distinguir", "Displasia é alteração tecidual (arquitetura) e anaplasia é alteração celular (diferenciação).", "objetivo 6; prova 2018 1.2", ["architecture"], "k-displasia-anaplasia"),
  ("p3-7", "decorar", "Carcinoma in situ: displasia de toda a espessura com membrana basal íntegra; romper a membrana basal = invasão.", "lâmina 6; Robbins p.265; prova 2016 1.4; palavras-cruzadas 4", ["basement membrane"], "k-cis"),
  ("p3-10", "organizar", "Sequência normal → hiperplasia → displasia → carcinoma in situ → invasor (ruptura da membrana basal).", "lâmina 6; provas 2016 P3 1.1 e 1.4", ["basement membrane"], "k-sequencia-cis"),
  ("p3-11", "explicar", "Células-tronco tumorais se autorrenovam e sustentam o tumor; resistem à terapia.", "lâmina 4; Robbins p.263 e 267", ["stem cells"], "k-celula-tronco"),
  ("p3-9", "explicar", "Quando o tumor é anaplásico, a imuno-histoquímica (citoqueratina, vimentina) identifica o tecido de origem.", "apostila de veteranos (Aula 14)", ["cytokeratin"], "k-ihc"),
  ("p3-8", "e-se", "Quanto mais diferenciado, mais o tumor retém função (hormônio, queratina, bile); anaplásico perde ou ganha funções novas.", "Robbins p.265", ["hormones"], "k-funcao"),
 ]),
 ("Teorias e etapas da transformação", "7-11", [
  ("p4-1", "distinguir", "Teoria da mutação somática (alteração genética da célula) × teoria do campo de organização tecidual (perturbação da interação com o microambiente).", "lâmina 7", ["microenvironment"], "k-teorias"),
  ("p4-2", "explicar", "Evento de iniciação gera célula iniciada que se expande clonalmente (a mutação passa às filhas).", "lâminas 8–10; objetivo 9; palavras-cruzadas 10, 18", ["mutations"], "k-iniciacao"),
  ("p4-3", "explicar", "Na progressão, novas mutações criam subclones e heterogeneidade (mais agressivos, invasivos, metastáticos).", "lâminas 8–10; objetivo 9; palavras-cruzadas 8", ["subclones"], "k-progressao"),
  ("p4-7", "explicar", "Metilação silencia genes do câncer sem mudar a sequência (epigenética).", "palavras-cruzadas 9", ["methylation"], "k-metilacao"),
  ("p4-5", "e-se", "Subclones diferentes fazem a metástase ter mutações ausentes no primário, e a terapia-alvo funciona só em parte.", "prova 2025 P4 2.6; lâminas 9–10", ["targeted"], "k-heterogeneidade-terapia"),
  ("p4-6", "decorar", "Exemplos concretos de cada hallmark: autossuficiência em sinais, insensibilidade ao TGF-β, telomerase, VEGF/FGF, efeito Warburg, MHC I reduzido.", "lâmina 11; prova 2017 P4 4.1", ["telomerase"], "k-hallmarks-exemplos"),
  ("p4-4", "organizar", "Hallmarks: proliferação sustentada, escape de supressores, resistência à morte, imortalidade replicativa, angiogênese, invasão e metástase; habilitados por instabilidade genômica e inflamação.", "lâmina 11; Hanahan & Weinberg 2011", ["angiogenesis"], "k-hallmarks"),
 ]),
 ("Ritmo e fração de crescimento", "12-15", [
  ("p5-1", "explicar", "O tumor cresce quando a proliferação supera a remoção (morte, perda celular).", "lâmina 12", ["exceeds"], "k-prolif-remocao"),
  ("p5-2", "decorar", "Cerca de 30 duplicações levam uma célula a 10^9 células (1 g, menor massa detectável) e só mais 10 a 1 kg.", "lâmina 13; Robbins p.265", ["30"], "k-30-duplicacoes"),
  ("p5-3", "organizar", "Ritmo depende do tempo de duplicação, da fração de crescimento e da perda celular.", "lâmina 14; objetivo 7; Robbins p.266", ["growth fraction"], "k-tres-fatores"),
  ("p5-4", "decorar", "Fração de crescimento é a proporção de células no grupo replicativo; cai com o tamanho, até 20% na fase clínica.", "lâmina 15; objetivo 8; Robbins p.266", ["20%"], "k-fracao"),
  ("p5-5", "e-se", "Fração baixa torna o tumor refratário à quimioterapia; cirurgia/radioterapia recrutam células de G0 (base da neoadjuvante).", "lâmina 15; objetivo 8; Robbins p.266", ["chemotherapy"], "k-fc-quimio"),
  ("p5-6", "decorar", "O ciclo da célula tumoral não é mais curto que o normal.", "Robbins p.266", ["not shorter"], "k-ciclo-nao-curto"),
 ]),
 ("Bases moleculares gerais", "16", [
  ("p6-1", "explicar", "O cerne da carcinogênese é dano genético não letal passado à prole.", "lâmina 16; Robbins p.271; palavras-cruzadas 17", ["nonlethal"], "k-dano-nao-letal"),
  ("p6-3", "e-se", "Se os genes de reparo falham, mutações se acumulam nos outros genes (instabilidade).", "lâmina 16; prova 2015 P3 2.2", ["DNA repair"], "k-quatro-classes"),
  ("p6-2", "organizar", "Alvos: proto-oncogenes, supressores de tumor, genes da apoptose e genes de reparo do DNA.", "lâmina 16; objetivo 14", ["DNA repair"], "k-quatro-classes"),
 ]),
 ("Invasão local", "17", [
  ("p7-1", "explicar", "Benigno cresce expansivo com cápsula fibrosa (do tecido comprimido), móvel e enucleável.", "lâmina 17; objetivo 11; Robbins p.268; palavras-cruzadas 16", ["capsule"], "k-capsula"),
  ("p7-2", "distinguir", "Maligno infiltra sem plano de clivagem; exige margem e dificulta a ressecção; invasão é o critério mais confiável depois da metástase.", "lâmina 17; objetivo 10–11; Robbins p.268; palavras-cruzadas 5", ["invasion"], "k-invasao"),
  ("p7-3", "explicar", "A invasão exige perder E-caderina, degradar a membrana basal (metaloproteinases) e migrar.", "prova 2016 1.5", ["E-cadherin"], "k-invasao-etapas"),
 ]),
 ("Ciclo celular e checkpoints (exemplo RB)", "18", [
  ("p8-1", "explicar", "Ciclinas e CDK comandam o ciclo fosforilando alvos como RB, liberando G1→S.", "lâmina 18", ["Rb"], "k-ciclina-rb"),
  ("p8-2", "distinguir", "Checkpoint G1/S checa dano no DNA (reparo ou apoptose); G2/M checa DNA completo antes da mitose.", "lâmina 18", ["DNA damage"], "k-checkpoints"),
 ]),
 ("Metástases e vias", "19", [
  ("p9-1", "distinguir", "Metástase é implante descontínuo do primário; invasão por contiguidade não é metástase.", "lâmina 19; objetivo 12; Robbins p.269; palavras-cruzadas 1", ["discontinuous"], "k-metastase-def"),
  ("p9-2", "organizar", "Predizem metástase a agressividade, a velocidade de crescimento e o tamanho.", "lâmina 19; Robbins p.269", ["size"], "k-preditores"),
  ("p9-3", "organizar", "Vias: linfática (carcinomas), hematogênica (sarcomas) e implante direto em cavidades.", "lâmina 19; objetivo 13; Robbins p.269–270; palavras-cruzadas 28, 31", ["lymphatic"], "k-vias"),
  ("p9-9", "organizar", "Três vias: linfática (carcinomas), hematogênica (sarcomas) e cavidades.", "lâmina 19; objetivo 13", ["lymphatic"], "k-vias-org"),
  ("p9-4", "explicar", "Fígado e pulmão são os sítios mais comuns da disseminação hematogênica (porta e cava).", "Robbins p.270; palavras-cruzadas 6", ["liver"], "k-figado-pulmao"),
  ("p9-5", "decorar", "Linfonodo sentinela é o primeiro da bacia que drena o tumor.", "Robbins p.270; palavras-cruzadas 2", ["sentinel"], "k-sentinela"),
  ("p9-6", "decorar", "Implante em cavidade: carcinoma de ovário reveste o peritônio.", "Robbins p.269", ["peritoneal"], "k-cavidade"),
  ("p9-7", "e-se", "Gliomas e carcinoma basocelular invadem mas raramente metastatizam.", "Robbins p.269", ["basal cell"], "k-sem-metastase"),
  ("p9-8", "organizar", "Estadiamento TNM: tamanho do tumor, linfonodos e metástase a distância.", "prova 2017 1.9", ["TNM"], "k-tnm"),
 ]),
 ("Condições predisponentes não hereditárias", "20", [
  ("p10-1", "explicar", "Hiperplasia, metaplasia e displasia são solo fértil para a transformação (mais divisões, mais erros).", "lâmina 20; palavras-cruzadas 19", ["metaplasia"], "k-solo-fertil"),
  ("p10-2", "explicar", "Inflamação crônica com regeneração ativa progenitoras e gera instabilidade por estresse oxidativo.", "lâmina 20; prova 2025 3.3", ["oxidative stress"], "k-inflamacao-cronica"),
  ("p10-3", "e-se", "Condições pré-cancerosas (gastrite atrófica, queratose solar, colite ulcerativa, leucoplasia, adenoma viloso) aumentam o risco.", "Robbins p.271", ["precursor"], "k-pre-cancerosas"),
 ]),
 ("Epidemiologia dos tumores (aula 74, absorvida)", "20", [
  ("p11-1", "organizar", "Fatores epidemiológicos: geográficos e ambientais (dominantes), idade e predisposição genética.", "aula 74 lâmina 7; cruzadas da aula 74", ["age"], "k-epi-fatores"),
  ("p11-2", "explicar", "A incidência cresce com a idade porque mutações somáticas se acumulam.", "aula 74 lâmina 7; cruzadas da aula 74 (6)", ["somatic"], "k-epi-idade"),
  ("p11-3", "e-se", "Mama é a mais incidente em mulheres mas não a mais letal por causa do diagnóstico precoce.", "aula 74 lâminas 2–6; cruzadas 11 e 15", ["early diagnosis"], "k-epi-diag-precoce"),
  ("p11-4", "decorar", "Mais incidentes: próstata (homens) e mama (mulheres); maior mortalidade: pulmão; colorretal é o 3º.", "aula 74 lâminas 2–6 (Siegel 2019)", ["lung"], "k-epi-ranking"),
  ("p11-5", "explicar", "Rastreamento (Papanicolau, mamografia, colonoscopia) pega a displasia ou o carcinoma inicial.", "cruzadas da aula 74 (4); prova 2017 P4 2.4", ["screening"], "k-epi-rastreamento"),
  ("p11-6", "decorar", "Exemplos de fatores: BRCA1/2, Barrett, H. pylori, álcool e fumo.", "cruzadas da aula 74 (1, 5, 7, 12, 13)", ["BRCA1"], "k-epi-exemplos"),
 ]),
]

itens = [it for _, _, its in PASSOS for it in its]
chaves = sorted({i[5] for i in itens})
base = "da biologia tumoral, base de oncogenes, carcinogênese, metástase e de todo laudo de patologia nas próximas UCs"

mapa = {"objetivos_da_aula": json.load(open(H / "compreensao-aula.json"))["o_que_a_aula_ensina"],
        "cronograma": {"aulas_vizinhas": ["74 Epidemiologia dos tumores", "76 Oncogenes e supressores", "77 Carcinógenos físicos e químicos", "78 Carcinógenos biológicos",
                                           "79 Carcinogênese sequencial", "80 Telômeros e reparo", "81 Imunologia dos tumores", "83 Metabolismo tumoral", "84 Angiogênese e metástase"],
                       "conferido": "Pastas UC03/Patologia (aulas 17–24 da turma) e banco/aulas_uc03.yml: a 75 dá conceitos e morfologia; genes (76), cascata metastática (84) e carcinógenos (77/78) têm aula própria."},
        "passos": [{"passo": t, "laminas": l, "itens": [{"id": i, "tipo": tp, "o_que": o, "fonte": f, "termos": te, "cards": [k]} for i, tp, o, f, te, k in its]} for t, l, its in PASSOS],
        "fora": [{"o_que": "Detalhe molecular de oncogenes, supressores e cascata metastática", "porque": "aulas 76 e 84", "motivo": "genes e cascata metastática têm aula própria (76, 84)"},
                 {"o_que": "Epidemiologia, incidência e rastreamento", "porque": "aula 74", "motivo": "epidemiologia e rastreamento são a aula 74, no mesmo dia"}],
        "extras_fora_da_aula": [], "revisao": ""}
json.dump(mapa, open(H / "mapa-de-profundidade.json", "w"), ensure_ascii=False, indent=1)

mot = {"_como": "F-20261023-CLAUDE-04: cada conceito que Davi precisa reconstruir; congelado na E3",
       "motivacoes": [{"id": f"m{n}", "item_mapa": i, "reconstruir": o, "por_que_dura": f"Passo '{t}' {base}; {f}.", "depois_de": "", "atendida_por": [k]}
                      for n, (t, (i, tp, o, f, te, k)) in enumerate(((t, it) for t, _, its in PASSOS for it in its), 1)]}
json.dump(mot, open(H / "motivacoes.json", "w"), ensure_ascii=False, indent=1)

# inventário por lâmina
SL = {1: ("capa", "Capa", []), 21: ("encerramento", "Lâmina de humor, sem conteúdo", [])}
TIT = {2: "Conceitos gerais", 3: "Biologia dos tumores: quatro eixos", 4: "Diferenciação e anaplasia", 5: "Displasia", 6: "Carcinoma in situ (figura)",
       7: "Teorias: campo × mutação somática", 8: "Iniciação, expansão clonal, progressão (figura)", 9: "Expansão clonal e variantes (figura Robbins)",
       10: "Árvore de mutações (figura)", 11: "Hallmarks (figura)", 12: "Proliferação × remoção (figura)", 13: "30 + 10 divisões (figura)", 14: "Fatores do ritmo",
       15: "Fração de crescimento", 16: "Bases moleculares gerais", 17: "Invasão local", 18: "Ciclo celular (figura)", 19: "Metástases", 20: "Condições predisponentes"}
POR = {}
for t, l, its in PASSOS:
    a, _, z = l.partition("-")
    a, z = int(a), int(z or a)
    for n, it in enumerate(its):
        s = a + min(n * (z - a + 1) // max(len(its), 1), z - a)
        POR.setdefault(s, []).append(it)
for s in range(2, 21):  # lâmina de figura do bloco sem item próprio recebe o item principal do bloco
    if s not in POR:
        bloco = next(its for t, l, its in PASSOS if int(l.split("-")[0]) <= s <= int(l.split("-")[-1]))
        POR[s] = [bloco[0]]
slides = [(1, "capa", "Capa", [])] + [(s, "conteudo", TIT[s], [(f"s{s}-{n}", it[2][:90], it[5]) for n, it in enumerate(POR[s])]) for s in range(2, 21)] + [(21, "capa", "Lâmina de humor, sem conteúdo", [])]
inv = ['"""Inventário da 75 Biologia e crescimento dos tumores (UC03 P4, Patologia), gerado por planejar.py (E3)."""',
       'PREFIXO = "pt75"', 'AULA = "75 Biologia e crescimento dos tumores (UC03 P4)"', 'EXC = "EXC: "', "SLIDES = ["]
inv += [f" {x!r}," for x in slides] + ["]", "JUSTIFICATIVAS = {\"encerramento\": \"lâmina final de humor, sem conteúdo de aula\"}",
        f"CAPITULO = [('Robbins cap. 7 pp. 259–271', {[(i[0], i[2][:80], i[5]) for i in itens if 'Robbins' in i[3]]!r})]",
        f"EXERCICIOS = [('Provas UC03 (pat-15)', {[(i[0], i[2][:80], i[5]) for i in itens if 'prova' in i[3]]!r}), ('Palavras-cruzadas da aula', {[(i[0], i[2][:80], i[5]) for i in itens if 'palavras' in i[3] and 'prova' not in i[3]]!r})]"]
(H / "inventario.py").write_text("\n".join(inv) + "\n")

json.dump({"ciclo": "básico", "justificativa": "Aula de princípio geral de patologia: o que é neoplasia, como se nomeia e como se separa benigno de maligno (diferenciação, crescimento, invasão, metástase), com a cinética e as bases moleculares gerais. Doenças só como exemplo de um princípio.",
           "clinica_lateral": [], "clinica_e_tema": False, "motivo_tema": "", "ordem_da_fala": [[1, 21]],
           "historia": "Uma célula sofre dano genético não letal, expande-se clonalmente e acumula mutações (progressão, subclones, hallmarks). O tumor resultante tem parênquima e estroma e recebe nome pelo parênquima. Benigno e maligno se distinguem por diferenciação (anaplasia × bem diferenciado; displasia e carcinoma in situ antes da invasão), ritmo de crescimento (proliferação × remoção, fração de crescimento que decide a quimioterapia), invasão local (cápsula × infiltração) e metástase (implante descontínuo por linfa, sangue ou cavidades). Proliferação crônica e inflamação são o terreno que favorece tudo isso.",
           "cards_de_conexao": ["k-criterios", "k-iniciacao"], "uso_das_fontes": {"aula": ["k-anaplasia-achados", "k-fracao", "k-vias"], "prova": ["k-cis", "k-displasia-anaplasia", "k-invasao-etapas", "k-tnm"],
           "bibliografia": ["k-30-duplicacoes", "k-capsula", "k-hallmarks"], "apostila": []},
           "provas": [{"id": "2018 P4 1.2", "cards": ["k-anaplasia-achados", "k-displasia-anaplasia"]}, {"id": "2016 P3 1.4", "cards": ["k-cis"]},
                      {"id": "2016 P3 1.5", "cards": ["k-invasao-etapas"]}, {"id": "2016 P3 2.2", "cards": ["k-nomenclatura"]}, {"id": "2017 P4 1.4", "cards": ["k-nc", "k-nomenclatura"]},
                      {"id": "2017 P4 1.9", "cards": ["k-tnm"]}, {"id": "2025 P4 3.3", "cards": ["k-inflamacao-cronica"]}]},
          open(H / "escopo.json", "w"), ensure_ascii=False, indent=1)

# matriz de fontes cruzadas
L = [{"fonte": "lamina", "ref": s, "item": f"Lâmina {s}: {TIT[s]}", "cards": sorted({it[5] for it in POR[s]})} for s in range(2, 21)]
OBJ = {1: ["k-tumor-neoplasia-cancer"], 2: ["k-nomenclatura"], 3: ["k-nomenclatura"], 4: ["k-excecoes", "k-teratoma"], 5: ["k-diferenciacao", "k-anaplasia-achados"],
       6: ["k-displasia-anaplasia"], 7: ["k-tres-fatores"], 8: ["k-fracao", "k-fc-quimio"], 9: ["k-iniciacao", "k-progressao"], 10: ["k-criterios", "k-invasao"],
       11: ["k-capsula", "k-invasao"], 12: ["k-metastase-def"], 13: ["k-vias"], 14: ["k-quatro-classes"], 15: ["k-iniciacao", "k-hallmarks", "k-dano-nao-letal"]}
objs = [l.split(". ", 1)[1] for l in (H / "fontes" / "objetivos-75.txt").read_text().splitlines()[1:]]
L += [{"fonte": "apostila", "ref": f"objetivo {n}", "item": objs[n - 1], "cards": c} for n, c in OBJ.items()]
PC = {"1/5 horizontais: invasão e metástase como critérios": ["k-criterios", "k-invasao"], "3: lipossarcoma; 20: leiomioma; 21: sufixo -oma": ["k-nomenclatura"],
      "6: fígado e pulmão": ["k-figado-pulmao"], "8: subclones": ["k-progressao"], "2 vertical: linfonodo sentinela": ["k-sentinela"], "4: carcinoma in situ": ["k-cis"],
      "7/14: anaplasia e diferenciação": ["k-diferenciacao"], "10/17/18: mutação não letal, expansão clonal": ["k-iniciacao", "k-dano-nao-letal"],
      "11: linfoma; 29: melanoma": ["k-excecoes"], "12: teratoma": ["k-teratoma"], "15: mitoses": ["k-mitoses"], "16: cápsula": ["k-capsula"],
      "19: metaplasia": ["k-solo-fertil"], "22: todo neoplasia é tumor": ["k-tumor-neoplasia-cancer"], "24/26: polaridade, pleomorfismo": ["k-anaplasia-achados"],
      "27/28/31: linfonodos, via linfática, via hematogênica": ["k-vias"], "9: efeito ambiental sobre o DNA (metilação)": ["k-metilacao"]}
for ref, c in PC.items():
    L.append({"fonte": "apostila", "ref": f"palavras-cruzadas {ref.split(':')[0]}", "item": "Palavras-cruzadas da aula (gabarito), " + ref, **({"cards": c} if c else {"motivo": "metilação/epigenética é da aula 76 (oncogenes e supressores) e 79"})})
PROVAS = {"2018 P4 1.2": ("Características celulares (anaplasia) e teciduais (displasia) que o patologista procura para malignidade", ["k-anaplasia-achados", "k-displasia-anaplasia", "k-nc"]),
          "2016 P3 1.4": ("Lesão in situ = ausência de ruptura da membrana basal", ["k-cis"]),
          "2016 P3 1.5": ("Etapas da invasão: perda de E-caderina, metaloproteinases, clivagem de laminina, quimiotaxia", ["k-invasao-etapas"]),
          "2016 P3 2.2": ("Nomenclatura de neoplasia epitelial escamosa: carcinoma epidermoide", ["k-nomenclatura"]),
          "2017 P4 1.4": ("Adenocarcinoma: células epiteliais atípicas formando glândulas e invadindo", ["k-nomenclatura", "k-nc"]),
          "2017 P4 1.9": ("Estadiamento TNM", ["k-tnm"]),
          "2025 P4 3.3": ("Lesão hepática crônica e regeneração favorecem transformação (estresse oxidativo, proliferação)", ["k-inflamacao-cronica", "k-solo-fertil"]),
          "2019 P4 2.11": ("Carcinogênese sequencial e implantes peritoneais", None),
          "2018 P4 1.3": ("Diagnóstico molecular do câncer de mama (receptores)", None),
          "2017 P4 1.8": ("EGFR oncogene dominante", ["k-quatro-classes"]),
          "2017 P4 2.4": ("Queda da incidência de câncer de colo (Papanicolau, vacina HPV)", ["k-epi-rastreamento"]),
          "2016 P3 1.1": ("Papanicolau com atipias sem invasão = displasia", ["k-displasia", "k-cis"]),
          "2016 P3 1.2": ("HPV-16 e coilocitose", None), "2016 P3 2.3": ("p53 supressor que para o ciclo em G1/S", ["k-checkpoints"]), "2016 P3 2.5": ("Telomerase evita a senescência e alonga telômeros", ["k-hallmarks-exemplos"]), "2015 P3 2.1": ("Pólipo glandular sem invasão da membrana basal = adenoma", ["k-nomenclatura", "k-invasao"]), "2015 P3 2.2": ("Genes de reparo de DNA facilitam o acúmulo de mutações", ["k-quatro-classes"]), "2025 P4 2.6": ("Heterogeneidade entre metástase e primário e resistência parcial à terapia-alvo", ["k-heterogeneidade-terapia"]), "2017 P4 4.1": ("Um elemento de cada marca do câncer", ["k-hallmarks", "k-hallmarks-exemplos"]), "2016 P3 1.8": ("Rastreamento reduz mortalidade", ["k-epi-rastreamento", "k-epi-diag-precoce"]), "2015 P3 2.4": ("CD44 e moléculas de invasão", ["k-invasao-etapas"]), "2015 P3 2.7": ("Diagnóstico precoce e seguimento", ["k-epi-diag-precoce", "k-epi-rastreamento"]), "2015 P3sub 2.1": ("Quatro características de malignidade: invasão da membrana basal (critério absoluto), anaplasia, mitoses anômalas, multinucleação", ["k-criterios", "k-anaplasia-achados", "k-mitoses"])}
MOT = {"2019 P4 2.11": "carcinogênese sequencial é a aula 79", "2018 P4 1.3": "diagnóstico molecular da mama é integrado (GR) e aula 76",
       "2017 P4 1.8": "oncogenes e herança dominante são da aula 76", "2017 P4 2.4": "epidemiologia e rastreamento são da aula 74",
       "2016 P3 1.2": "HPV como carcinógeno é da aula 78", "2016 P3 1.8": "rastreamento é da aula 74", "2015 P3 2.4": "moléculas de invasão e metástase são da aula 84", "2015 P3 2.7": "diagnóstico precoce é da aula 74", "2015 P3sub 2.1": "a conferir abaixo"}
for ref, (item, c) in PROVAS.items():
    L.append({"fonte": "prova", "ref": ref, "item": item, **({"cards": c} if c else {"motivo": MOT[ref]})})
for i in itens:
    if "Robbins" in i[3]:
        L.append({"fonte": "livro", "ref": "Robbins " + i[3].split("Robbins ")[1].split(";")[0], "item": i[2][:120], "cards": [i[5]]})
for s74, it74, c74 in [(2, "Siegel 2019: novos casos e mortes por sítio e sexo", ["k-epi-ranking", "k-epi-diag-precoce"]), (3, "Incidência por sítio ao longo do tempo (próstata, mama, pulmão, colorretal)", ["k-epi-ranking"]),
                       (4, "Mortalidade por sítio desde 1930 (pulmão sobe e cai, estômago cai)", ["k-epi-ranking", "k-epi-exemplos"]), (5, "Incidência e mortalidade totais caindo desde 1990", ["k-epi-rastreamento"]),
                       (6, "Mortes evitadas por câncer desde 1990", ["k-epi-rastreamento"]), (7, "Fatores geográficos e ambientais, idade e predisposição genética", ["k-epi-fatores", "k-epi-idade", "k-epi-exemplos"]), (8, "Nomenclatura das benignas: -oma, adenoma, papiloma, cistadenoma", ["k-nomenclatura"]), (9, "Nomenclatura das malignas: sarcoma, carcinoma, adenocarcinoma, epidermoide, tumores mistos", ["k-nomenclatura", "k-nomenclatura-orgaos"]), (10, "Tabela de nomenclatura por tecido", ["k-nomenclatura-orgaos", "k-nomenclatura"]), (11, "Tabela de nomenclatura (continuação)", ["k-nomenclatura-orgaos"])]:
    L.append({"fonte": "lamina", "ref": f"aula74-{s74}", "item": f"Aula 74 lâmina {s74}: {it74}", "cards": c74})
for r74, it74, c74 in [("1", "Gene da predisposição herdada ao câncer de mama (BRCA)", ["k-epi-exemplos"]), ("2", "Fatores ambientais são o risco dominante", ["k-epi-fatores"]), ("4", "Testes de rastreamento como Papanicolau e PSA", ["k-epi-rastreamento"]),
                       ("6", "Mutações somáticas acumulam ao longo da vida", ["k-epi-idade"]), ("3", "Envelhecimento populacional aumenta incidência e prevalência", ["k-epi-idade"]), ("7/8/14", "Lesões precursoras: Barrett e leucoplasia", ["k-epi-exemplos", "k-pre-cancerosas"]), ("9", "Proliferação regenerativa na inflamação crônica", ["k-inflamacao-cronica"]),
                       ("10/11/15", "Maior mortalidade (pulmão) e maior incidência por sexo", ["k-epi-ranking"]), ("11", "Diagnóstico precoce explica mama incidente mas não a mais letal", ["k-epi-diag-precoce"]),
                       ("12/5/13", "H. pylori no estômago, álcool no fígado e esôfago, tabagismo no pulmão", ["k-epi-exemplos"])]:
    L.append({"fonte": "apostila", "ref": f"cruzadas aula 74 {r74}", "item": "Palavras-cruzadas da aula 74 (gabarito), " + it74, "cards": c74})
L.append({"fonte": "livro", "ref": "Hanahan & Weinberg 2011", "item": "Seis hallmarks, duas características habilitadoras e duas emergentes", "cards": ["k-hallmarks"]})
L.append({"fonte": "video", "ref": "Armando Cancer Introduction II", "item": "Transformação, displasia, anaplasia e autonomia", "cards": ["k-diferenciacao", "k-displasia"]})
json.dump({"_como": "F-20261110-CLAUDE-01: fontes cruzadas da 75 (E3); chaves k-* trocadas pelas reais na E5", "linhas": L}, open(H / "matriz-fontes.json", "w"), ensure_ascii=False, indent=1)
print(len(itens), "itens;", len(chaves), "chaves;", len(L), "linhas na matriz;", sum(1 for l in L if not l.get("cards")), "fora")
