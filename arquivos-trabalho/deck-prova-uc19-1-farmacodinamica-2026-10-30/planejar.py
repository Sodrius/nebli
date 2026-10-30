"""Planejamento do lote 1 do deck-prova UC19 (Farmacodinâmica), fonte única da E3 em diante (F-20261029-CLAUDE-04).

    /usr/bin/python3 planejar.py      # grava mapa-de-profundidade.json, motivacoes.json, matriz-prova.json, inventario.py, escopo.json

ITENS é o que a prova cobra, tirado das fontes base (objetivos, resumo da aula 1, questões orientadoras, Ferro et al., banco) e
conferido no Rang cap. 2. CARDS (item → chaves do spec) é preenchido depois da busca (E4/E5); a matriz e o mapa saem daqui.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.base_prova import texto_paginas  # noqa: E402

# id: (bloco/página da base, tipo, o que Davi tem de saber, fonte, termos que o card precisa conter)
ITENS = {
 "f1": (1, "distinguir", "Farmacodinâmica é o que o fármaco faz ao organismo; farmacocinética, o que o organismo faz ao fármaco (ADME).", "objetivos 1; resumo p.1; orientadoras 4–5", ["pharmacodynamics"]),
 "f2": (1, "distinguir", "Fármaco é o princípio ativo; medicamento é fármaco + excipientes; remédio é qualquer recurso benéfico (todo medicamento é remédio, nem todo remédio é medicamento).", "objetivos 1; resumo p.2; Ferro p.3–4; orientadoras 3 e 7", ["excipient"]),
 "f3": (3, "decorar", "Phármakon significa remédio e veneno; Paracelso: a dose separa medicamento de veneno.", "Ferro p.2; orientadoras 1–2", ["dose"]),
 "f4": (1, "decorar", "Toxicologia estuda os efeitos adversos de agentes químicos e é subárea da farmacologia.", "objetivos 1", ["toxicology"]),
 "f5": (2, "organizar", "Desenvolvimento de fármacos: ensaios pré-clínicos e fases clínicas antes do registro; fármacos vão de moléculas pequenas a anticorpos e vacinas.", "resumo p.2; Emer 1; orientadora 10", ["phase"]),
 "f6": (2, "explicar", "Etapas da ação: biofarmacêutica (liberação e dissolução) → farmacocinética (ADME até a biofase) → farmacodinâmica (alvo, resposta, efeito).", "resumo p.2–3", ["dissolution"]),
 "a1": (7, "organizar", "Classes de alvo farmacológico: receptores, canais iônicos, transportadores, enzimas e ácidos nucleicos.", "objetivos 2; resumo p.3; orientadoras 6, 11–13; Emer 4", ["receptor"]),
 "a2": (7, "organizar", "Famílias de receptores: ionotrópicos, acoplados à proteína G, ligados a quinases e nucleares.", "resumo p.3; Emer 2–3", ["G protein"]),
 "a3": (10, "explicar", "Nitroglicerina libera NO, que ativa a guanilato ciclase, eleva o GMPc e relaxa o músculo liso vascular.", "Ferro p.15–16; orientadoras 15 e 31", ["cGMP"]),
 "a4": (10, "e-se", "Inibir a PDE5 (sildenafil, tadalafila) impede a degradação do GMPc e prolonga o sinal do NO.", "Ferro p.16; orientadora 16", ["PDE5"]),
 "a5": (7, "decorar", "Cisplatina e doxorrubicina têm o DNA como alvo; doxorrubicina causa cardiotoxicidade e cisplatina, nefrotoxicidade.", "resumo p.4; orientadoras 14, 20, 33, 34", ["cisplatin"]),
 "a6": (7, "explicar", "Fármacos sem alvo: manitol (osmose no túbulo), antiácido (neutralização), quelante (complexo com metal).", "resumo p.4; orientadoras 10, 17–19, 32", ["mannitol"]),
 "a7": (8, "explicar", "Especificidade vem da estrutura (relação estrutura-atividade, Bovet); Ehrlich propôs a toxicidade seletiva (bala mágica).", "objetivos 3; Ferro p.4 e p.8; orientadora 9", ["selective"]),
 "a8": (11, "e-se", "Clavulanato inibe a β-lactamase e protege a amoxicilina da inativação.", "orientadoras 8 e 35", ["clavulan"]),
 "a9": (12, "decorar", "Exemplos de alvo: bomba de prótons (omeprazol), cotransportador Na-K-2Cl (diurético de alça), canal de Na voltagem-dependente (lidocaína).", "lâmina 66; orientadoras 12–13", ["proton pump"]),
 "c1": (15, "distinguir", "Afinidade é a capacidade de ligar ao alvo; eficácia (atividade intrínseca) é a de ativá-lo depois de ligado.", "objetivos 6; resumo p.5; orientadoras 21–22", ["affinity"]),
 "c2": (15, "decorar", "Potência é a concentração ou dose para 50% do efeito máximo (CE50/DE50); menor CE50, mais potente.", "resumo p.5; orientadora 23; Stephen 3", ["EC50"]),
 "c3": (18, "distinguir", "Na curva, eficácia é a altura do platô (Emax) e potência é a posição no eixo da dose.", "orientadoras 23–24; Medicosis", ["efficacy"]),
 "c4": (13, "explicar", "Curva graduada (resposta de um indivíduo) × quantal (fração da população com o efeito); dela saem DE50, DT50 e DL50.", "objetivos 4; resumo p.8", ["quantal"]),
 "c5": (16, "decorar", "Índice terapêutico = DT50 (ou DL50) / DE50; IT baixo (digoxina, varfarina, lítio) é margem estreita.", "resumo p.8; lâmina 60; orientadora 40", ["therapeutic index"]),
 "c6": (16, "decorar", "Janela terapêutica é a faixa entre a concentração mínima eficaz e a mínima tóxica.", "objetivos 4; resumo p.8", ["therapeutic window"]),
 "c7": (15, "explicar", "Receptores de reserva: o agonista pleno dá resposta máxima ocupando poucos receptores, por isso a CE50 pode ser menor que a Kd.", "Rang cap. 2 p.41 (um pouco mais)", ["spare receptors"]),
 "g1": (21, "explicar", "O receptor oscila entre R e R*; o agonista pleno estabiliza R* e dá o efeito máximo do sistema.", "resumo p.6; lâmina 45; objetivos 5", ["full agonist"]),
 "g2": (21, "explicar", "Agonista parcial tem Emax menor que o pleno em qualquer dose e, junto com o pleno, reduz a resposta total.", "resumo p.6; orientadora 24", ["partial agonist"]),
 "g3": (21, "e-se", "Buprenorfina (parcial opioide) precipita abstinência em quem usa agonista pleno, como a morfina.", "resumo p.6; orientadora 37", ["buprenorphine"]),
 "g4": (22, "distinguir", "Agonista inverso reduz a atividade constitutiva abaixo do basal (loratadina no H1); antagonista neutro só impede o agonista.", "resumo p.6; orientadoras 25–26; Stephen 1", ["inverse agonist"]),
 "g5": (23, "decorar", "Agonista tendencioso ativa preferencialmente uma via do mesmo receptor (proteína G × β-arrestina).", "resumo p.6; orientadora 28", ["biased"]),
 "n1": (26, "explicar", "Antagonista competitivo reversível aumenta a CE50 (curva à direita) sem mudar o Emax; excesso de agonista supera o bloqueio (gráfico de Schild).", "resumo p.7; orientadora 27; Ferro p.9", ["competitive"]),
 "n2": (26, "e-se", "Antagonista irreversível (covalente: aspirina, omeprazol, iMAO) reduz o Emax e não é superado pelo agonista.", "objetivos 7; resumo p.7; lâmina 54", ["irreversible"]),
 "n3": (26, "explicar", "Antagonista não competitivo (outro sítio ou depois do receptor) reduz o Emax sem mudar a potência aparente.", "resumo p.8", ["noncompetitive"]),
 "n4": (26, "organizar", "Antagonismo químico (dimercaprol, infliximabe), farmacocinético (fenobarbital induz CYP e reduz a varfarina) e fisiológico (insulina × glucagon).", "objetivos 7; resumo p.8; orientadora 39; banco p.25–26", ["physiologic"]),
 "n5": (30, "decorar", "Propranolol é antagonista competitivo β; atropina, competitivo muscarínico.", "orientadora 36; lâmina 56; Stephen 2", ["propranolol"]),
 "n6": (27, "explicar", "Sítio alostérico é distinto do ortostérico; modulador alostérico positivo (PAM) potencializa e negativo (NAM) atenua o agonista.", "objetivos 8; resumo p.4; orientadora 29", ["allosteric"]),
 "n7": (27, "explicar", "Enantiômeros têm a mesma fórmula e arranjo espacial diferente; podem diferir em atividade e toxicidade.", "resumo p.4; orientadora 30; Medicosis", ["enantiomer"]),
 "n8": (28, "explicar", "Langley: pilocarpina e atropina se anulam em proporção definida agindo na célula efetora, a origem da ideia de substância receptiva (receptor).", "Ferro p.7", ["receptor"]),
 "r1": (33, "distinguir", "Taquifilaxia ou dessensibilização é perda rápida do efeito com doses repetidas; tolerância é perda gradual (dias a semanas).", "objetivos 9; Rang p.41; Medicosis", ["tachyphylaxis"]),
 "r2": (33, "explicar", "Mecanismos de perda de resposta: alteração e perda de receptores, depleção de mediadores, mais metabolismo, adaptação fisiológica, extrusão ativa.", "Rang p.41–42", ["desensitization"]),
 "r3": (33, "decorar", "Resistência é a perda de eficácia de antimicrobianos e antineoplásicos; refratariedade, a perda de eficácia terapêutica.", "objetivos 9; Rang p.41", ["resistance"]),
 "x1": (35, "e-se", "No envenenamento colinérgico (acúmulo de acetilcolina), a atropina reverte os efeitos muscarínicos por antagonismo competitivo.", "Emer 5", ["atropine"]),
 "x2": (34, "explicar", "Hipercalemia despolariza o potencial de repouso dos cardiomiócitos e altera a condução, favorecendo arritmias.", "orientadora 38", ["hyperkalemia"]),
}

PASSOS = [("Fundamentos", ["f1", "f2", "f3", "f4", "f5", "f6"]), ("Alvos farmacológicos", ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]),
          ("Curva dose-resposta e segurança", ["c1", "c2", "c3", "c7", "c4", "c5", "c6"]), ("Agonismo", ["g1", "g2", "g3", "g4", "g5"]),
          ("Antagonismo, alosterismo e quiralidade", ["n8", "n1", "n2", "n3", "n4", "n5", "n6", "n7"]), ("Perda de resposta", ["r1", "r2", "r3"]),
          ("Aplicação (casos clínicos)", ["x1", "x2"])]

CARDS_SRC = {  # item → nids de acervo (resolvidos para a chave do plano) ou chaves de autoral/compartilhado (E5, 30/10)
 "f1": [1565120487647], "f2": ["farmaco-medicamento"], "f3": ["dose-veneno"], "f4": ["farmaco-medicamento"],
 "f5": [1485913667420, 1485913675748, 1485913688921, 1485913697186], "f6": ["sh-1791762409798"],
 "a1": ["classes-alvo"], "a2": [1484768461819, 1555083517363, 1522203660054, 1461866207939, 1461867085192],
 "a3": [1461865849072, 1461865801747, 1472747780684, 1712002843254], "a4": [1463081026525, 1461857288204, 1472747945251],
 "a5": [1509225252310, 1509225571827, 1509235247004, 1509235473720], "a6": [1475636907165, "sh-1791762415623", 1490137896605],
 "a7": ["seletividade"], "a8": [1503672347649], "a9": [1461624498591, 1475023258287, 1484950518844],
 "c1": ["sh-1791762418025"], "c2": [1490066290359, 1490066293330], "c3": [1490066276769, 1490066280055, "sh-1791826286643", "sh-1791826286795"],
 "c4": ["sh-1791762425949"], "c5": [1490066320396, 1490066323578, 1490066326802], "c6": ["janela"], "c7": ["agonismo-org"],
 "g1": ["agonismo-org"], "g2": [1490066314616], "g3": [1484950415236, 1484950383414, 1484950460397, 1477447295771, 1489960356460], "g4": ["sh-1791762419072", "sh-1791762419199"], "g5": ["sh-1791762421022"],
 "n1": [1490066300391, 1490066305390, 1472426576894, 1472426619514, 1472426609949, 1472426626716],
 "n2": [1488847696894, 1485048808436, 1477432981161, 1472426585896, 1472426621969, 1472426614133, 1472426629660, 1461624498591],
 "n3": [1490066308677, 1490066311609, 1472426624361, 1472426616871, 1472426631686],
 "n4": ["antagonismo-sem-receptor", 1490066214478, 1490066222678, 1490066217772], "n5": [1484950422509, "antagonismo-sem-receptor"],
 "n6": ["sh-1791762416798", 1484768430296, 1484768435794, 1484768467897, 1484768472408, 1484768629105], "n7": [1554208492401, 1555560638891, 1701897271054],
 "n8": ["classes-alvo"],
 "r1": ["perda-resposta", 1490066226073, 1695594779845, 1472747925827, 1560780655468, 1560791719068],
 "r2": [1605210863862, 1610988344275, 1484768590208, 1461852748718], "r3": ["perda-resposta", 1518398747905],
 "x1": [1485382222368, 1485382227392, 1485382192161, 1485382187439], "x2": [1470880181246, 1475704571141],
}
TERMOS = {"f1": ["pharmacokinetics"], "f2": ["medicine"], "f3": ["dose"], "f4": ["toxicology"], "f5": ["phase"], "f6": ["dissolve"],
          "a1": ["transporters"], "a2": ["receptor"], "a3": ["cGMP"], "a4": ["PDE"], "a5": ["DNA"], "a6": ["osmotic"], "a7": ["structure"],
          "a8": ["clavulan"], "a9": ["channels"], "c1": ["intrinsic activity"], "c2": ["potency"], "c3": ["efficacy"], "c4": ["quantal"],
          "c5": ["therapeutic index"], "c6": ["therapeutic window"], "c7": ["spare receptors"], "g1": ["full"], "g2": ["partial"],
          "g3": ["withdrawal"], "g4": ["inverse"], "g5": ["biased"], "n1": ["competitive"], "n2": ["irreversible"], "n3": ["competitive"],
          "n4": ["chemical"], "n5": ["propranolol"], "n6": ["allosteric"], "n7": ["enantiomers"], "n8": ["langley"], "r1": ["tolerance"],
          "r2": ["desensitization"], "r3": ["resistance"], "x1": ["atropine"], "x2": ["hyperkalemia"]}


def _resolver():
    try:
        plan = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
    except OSError:
        return {}
    chaves = {e["key"] for e in plan["entries"]} | {f"sh-{k}" for k in plan.get("compartilhados", {})}
    por_fonte = {str(v.get("source_nid")): f"sh-{k}" for k, v in plan.get("compartilhados", {}).items() if v.get("source_nid")}
    out = {}
    for item, xs in CARDS_SRC.items():
        ks = []
        for x in xs:
            k = x if isinstance(x, str) else (f"ak{x}" if f"ak{x}" in chaves else por_fonte.get(str(x)))
            if k not in chaves:
                raise SystemExit(f"{item}: {x} não está no plano")
            ks.append(k)
        out[item] = ks
    return out


CARDS = _resolver()

# Matriz: (id, fonte, tipo, âncora do trecho literal, itens) — questões numeradas pelo próprio enunciado
F = {"O": ("fontes/objetivos.pdf", 1, 7), "R": ("fontes/resumo-aula1.pdf", 1, 8), "Q": ("fontes/orientadoras-fd.pdf", 1, 14),
     "H": ("fontes/historia.pdf", 1, 21), "T": ("fontes/todas-questoes.pdf", 25, 26)}
QUESTOES = {1: ["f3"], 2: ["f3"], 3: ["f2"], 4: ["f1"], 5: ["f1"], 6: ["a1"], 7: ["f2"], 8: ["a8"], 9: ["a7"], 10: ["a6", "f5"],
            11: ["a1"], 12: ["a1", "a9"], 13: ["a1", "a9"], 14: ["a5"], 15: ["a3"], 16: ["a4"], 17: ["a6"], 18: ["a6"], 19: ["a6"], 20: ["a5"],
            21: ["c1"], 22: ["c1"], 23: ["c2", "c3"], 24: ["g2", "c3"], 25: ["g4"], 26: ["g4"], 27: ["n1"], 28: ["g5"], 29: ["n6"], 30: ["n7"],
            31: ["a3"], 32: ["a6"], 33: ["a5"], 34: ["a5"], 35: ["a8"], 36: ["n5"], 37: ["g3"], 38: ["x2"], 39: ["n4"], 40: ["c5"]}
OUTRAS = [  # (id, chave de F, tipo, âncora, itens ou ("fora", motivo, porquê))
 ("obj1", "O", "item", "1) O que é farmacologia", ["f1", "f2", "f4"]), ("obj2", "O", "item", "2) O que são alvos farmacológicos?", ["a1"]),
 ("obj3", "O", "item", "3) De onde decorre a especificidade", ["a7"]), ("obj4", "O", "item", "4) O que é “curva dose-resposta”", ["c4", "c5", "c6"]),
 ("obj5", "O", "item", "5) Sobre agonismo farmacológico", ["g1", "g2", "g4", "g5"]), ("obj6", "O", "item", "6) Sobre agonismo farmacológico", ["c1", "c2"]),
 ("obj7", "O", "item", "7) O que é antagonismo farmacológico?", ["n1", "n2", "n4"]), ("obj8", "O", "item", "8) O que é alosterismo farmacológico?", ["n6"]),
 ("obj9", "O", "item", "9) A que se pode relacionar a perda", ["r1", "r2", "r3"]),
 ("emer1", "O", "questao", "1) Qual afirmação sobre o processo de descoberta", ["f5"]), ("emer2", "O", "questao", "2) Como são chamadas as estruturas de proteínas", ["a2"]),
 ("emer3", "O", "questao", "3) Qual dos seguintes não é um tipo de receptor", ["a2"]), ("emer4", "O", "questao", "4) Na farmacodinâmica, a droga deve se ligar", ["a1"]),
 ("emer5", "O", "questao", "5) Uma das unidades do exército foi atacada", ["x1"]), ("steph1", "O", "questao", "1) Diferencie antagonistas de agonistas inversos.", ["g4"]),
 ("steph2", "O", "questao", "2) Dê exemplo de medicamento agonista pleno", ["g1", "n5"]), ("steph3", "O", "questao", "3) O que é o EC50 na farmacologia?", ["c2"]),
 ("banco-fisio", "T", "questao", "São exemplos de fármacos que se antagonizam", ["n4"]),
 ("res-temas", "R", "item", "Os tópicos gerais da UC19 são farmacodinâmica", ["f1"]), ("res-defs", "R", "item", "Fármaco é uma substância de estrutura química conhecida", ["f2"]),
 ("res-historia", "R", "item", "Os neandertais já faziam uso medicinal", ("fora", "fora-do-escopo", "Plantas pré-históricas e Lavoisier são a ilustração histórica da aula; nenhum objetivo nem questão os cobra.")),
 ("res-desenv", "R", "item", "Atualmente, o desenvolvimento de fármacos", ["f5"]), ("res-etapas", "R", "item", "Biofarmacêutica: após administrado", ["f6"]),
 ("res-alvos", "R", "item", "5 principais alvos moleculares", ["a1", "a2"]),
 ("res-druggable", "R", "item", "Druggable Genome", ("fora", "fora-do-escopo", "Número conflitante entre as fontes (3.000 de 30.000 genes no resumo; 667 proteínas, cerca de 2%, em Ferro et al.); nenhuma questão cobra.")),
 ("res-dna", "R", "item", "Cisplatina e Doxorrubicina penetram", ["a5"]), ("res-sem-alvo", "R", "item", "Fármacos podem atuar por mecanismos físico-químicos", ["a6"]),
 ("res-isomero", "R", "item", "Isomerismo óptico e estereoisomerismo", ["n7"]), ("res-orto", "R", "item", "Sítios ortostéricos vs. Sítios alostéricos", ["n6"]),
 ("res-propr", "R", "item", "Para produzir um efeito terapêutico, o fármaco precisa", ["c1", "c2"]), ("res-agonismo", "R", "item", "Considera que o receptor existe num equilíbrio", ["g1", "g2", "g3", "g4", "g5"]),
 ("res-antag", "R", "item", "Reversível: agonista e antagonista competem", ["n1", "n2"]), ("res-naocomp", "R", "item", "Antagonismo não-competitivo", ["n3", "n4"]),
 ("res-seguranca", "R", "item", "Índice Terapêutico (IT): razão numérica", ["c5", "c6"]),
 ("hist-pharmakon", "H", "item", "curioso que o termo fármaco", ["f3"]), ("hist-remedio", "H", "item", "Consideramos importante nesse momento", ["f2"]),
 ("hist-ehrlich", "H", "item", "Desta forma, Ehrlich", ["a7"]), ("hist-langley", "H", "item", "John Newport Langley é conhecido", ["n8"]),
 ("hist-bovet", "H", "item", "Em 1947, Daniel Bovet", ["a7"]), ("hist-black", "H", "item", "Em 1950, Sir James Black", ["n1", "n5"]),
 ("hist-no", "H", "item", "Furchgott propôs, em 1982", ["a3", "a4"]),
 ("hist-resto", "H", "item", "Selman Abraham Waksman", ("fora", "fora-do-escopo", "Nobel de antibióticos, insulina, neurotransmissão e eicosanoides é a parte histórica do artigo; os objetivos e as questões não cobram.")),
]


def _txt(chave):
    f, a, z = F[chave]
    return texto_paginas(HERE / f, a, z)


def matriz():
    txts = {k: _txt(k) for k in F}
    linhas = []
    for n, itens in QUESTOES.items():
        m = re.search(rf"(?<![\d]){n}\. (.{{20,70}}?\S)(?=\s)", txts["Q"])
        linhas.append({"id": f"q{n}", "fonte": F["Q"][0], "tipo": "questao", "trecho": m.group(0), "itens": itens})
    for id_, k, tipo, ancora, alvo in OUTRAS:
        i = txts[k].find(ancora)
        if i < 0:
            raise SystemExit(f"âncora da matriz não achada: {id_} {ancora!r}")
        linha = {"id": id_, "fonte": F[k][0], "tipo": tipo, "trecho": txts[k][i:i + max(len(ancora), 40)]}
        if isinstance(alvo, tuple):
            linha.update({"fora": alvo[1], "porque": alvo[2]})
        else:
            linha["itens"] = alvo
        linhas.append(linha)
    for x in linhas:
        if "itens" in x:
            x["cards"] = sorted({c for it in x["itens"] for c in CARDS.get(it, [])})
    q = {}
    for x in linhas:
        if x["tipo"] == "questao":
            q[x["fonte"]] = q.get(x["fonte"], 0) + 1
    return {"_como": "uma linha por item das fontes base e por questão; cards = união dos cards dos itens (planejar.py)",
            "questoes_por_fonte": q, "linhas": linhas}


def mapa():
    return {"objetivos_da_aula": "Objetivos cognitivos de farmacodinâmica (itens 1–9) e as 49 questões do material",
            "cronograma": {"aulas_vizinhas": ["UC19 01 Introdução à farmacologia e mecanismos de ação (05/10)", "UC19 04 Farmacodinâmica: agonistas e antagonistas (09/11)",
                                              "Deck-prova 2 Farmacocinética", "Deck-prova 3 Farmacocinética quantitativa"],
                           "conferido": "Cronograma 2026 da UC19 lido: farmacodinâmica nas aulas do Prof. Emer (05/10 e 09/11); indução de CYP e absorção ficam no lote 2 e cinética de saturação no lote 3, por isso entram aqui só como antagonismo farmacocinético."},
            "passos": [{"passo": nome, "laminas": ITENS[ids[0]][0], "itens": [
                {"id": i, "tipo": ITENS[i][1], "o_que": ITENS[i][2], "fonte": ITENS[i][3], "termos": TERMOS.get(i, ITENS[i][4]), "cards": CARDS.get(i, [])}
                for i in ids]} for nome, ids in PASSOS],
            "fora": [{"o_que": x[3], "motivo": x[4][2]} for x in OUTRAS if isinstance(x[4], tuple)]}


def motivacoes():
    return {"motivacoes": [{"id": f"m-{i}", "item_mapa": i, "reconstruir": ITENS[i][2],
                            "por_que_dura": f"Item {ITENS[i][1]} cobrado em {ITENS[i][3]}; sem ele a questão correspondente da prova não se responde.",
                            "depois_de": "", "atendida_por": CARDS.get(i, [])} for i in ITENS]}


FAMILIA = [("Objetivos", "objetivos"), ("Resumo", "resumo"), ("orientadora", "orientadora"), ("Ferro", "Ferro"), ("Lâmina", "lâmina"),
           ("Banco", "banco"), ("questões de prova", "Emer")]


def inventario():
    """inventario.py para nebli.inventario: cada página da base com os itens que ela ensina (mesmo bloco e mesma fonte)."""
    ind = json.loads((HERE / "fontes" / "base-prova-indice.json").read_text(encoding="utf-8"))
    linhas, dmap = [], {}
    for pg in ind:
        ids = PASSOS[pg["bloco"] - 1][1]
        fam = next((f for r, f in FAMILIA if r.lower() in pg["titulo"].lower()), None)
        its = [i for i in ids if fam and fam.lower() in ITENS[i][3].lower()] or ids[:1]
        if pg["bloco"] == 7:
            its = ids
        regs = []
        for k, i in zip("abcdefghijklmnop", its):
            dmap[f"{pg['pagina']}{k}"] = i
            regs.append(f"(\"{k}\", {json.dumps(ITENS[i][2][:90], ensure_ascii=False)}, D.get(\"{pg['pagina']}{k}\", \"\"))")
        linhas.append(f" ({pg['pagina']}, \"conteudo\", {json.dumps(pg['titulo'][2:110], ensure_ascii=False)}, [{', '.join(regs)}]),")
    ex = []
    for x in matriz()["linhas"]:
        if x["tipo"] == "questao" and x.get("itens"):
            dmap[x["id"]] = x["itens"][0]
            ex.append(f"  (\"{x['id']}\", {json.dumps(x['trecho'][:80], ensure_ascii=False)}, D.get(\"{x['id']}\", \"\")),")
    cap = []
    for i in ("c7", "r1", "r2", "n3"):
        dmap["rang-" + i] = i
        cap.append(f"  (\"rang-{i}\", {json.dumps(ITENS[i][2][:90], ensure_ascii=False)}, D.get(\"rang-{i}\", \"\")),")
    D = {k: CARDS.get(i, []) for k, i in dmap.items() if CARDS.get(i)}
    return "\n".join([
        '"""Inventário atômico do deck-prova UC19 lote 1 (Farmacodinâmica), gerado por planejar.py a partir da base da prova',
        '(fontes/slides.pdf: 35 páginas de excertos literais) e dos itens da E3. Destinos (D) preenchidos depois da busca."""',
        'PREFIXO = "dp1"', 'AULA = "Deck-prova 1 — Farmacodinâmica (UC19 P1; Farmacologia; Prof. Emer)"', "EXC = \"EXC: \"",
        f"D = {json.dumps(D, ensure_ascii=False)}", "", "SLIDES = [", *linhas, "]", "JUSTIFICATIVAS = {}",
        'CAPITULO = [("Rang & Dale cap. 2: receptores de reserva, antagonismo, dessensibilização e tolerância (pp. 41–42)", [', *cap, "])]",
        'EXERCICIOS = [("Questões do material (orientadoras FD, professores, banco)", [', *ex, "])]", ""])


HISTORIA = ("Fármaco é a molécula que muda a função da célula; em dose certa é remédio, em excesso, veneno. Ele age ligando-se a um alvo "
            "(receptor, canal, transportador, enzima, DNA) ou por química pura. Ligado, a afinidade diz quanto ocupa e a eficácia quanto ativa; "
            "a curva dose-resposta mostra os dois e a distância entre dose eficaz e tóxica mede a segurança. Quem ativa pode ser pleno, parcial, "
            "inverso ou tendencioso; quem bloqueia compete pelo sítio, liga-se de vez, age noutro ponto ou nem toca o receptor. E com o uso "
            "repetido a resposta cai: taquifilaxia, tolerância, resistência.")
LINHA = [("O que é fármaco e onde ele age: princípio ativo ligado a um alvo", "Ligado ao alvo, o efeito cresce com a dose até um platô", ["f2", "a1"]),
         ("Curva dose-resposta na população: DE50, DT50 e índice terapêutico", "A mesma curva, num indivíduo, separa ligar de ativar", ["c4", "c5", "c6"]),
         ("Afinidade, eficácia e potência lidas na curva (platô × posição)", "A eficácia depende de quanto o ligante desloca o receptor para o estado ativo", ["c1", "c2", "c3"]),
         ("Agonismo: pleno, parcial, inverso e tendencioso pelo estado do receptor", "Quem ocupa o receptor sem ativá-lo bloqueia o agonista", ["g1", "g2", "g4"]),
         ("Antagonismo: competitivo desloca a curva, não competitivo baixa o platô", "Repetir o estímulo também muda o receptor e a resposta cai", ["n1", "n3"]),
         ("Perda de resposta: taquifilaxia, tolerância, refratariedade e resistência", "", ["r1", "r2"])]
CONEXAO = ["janela", "agonismo-org", "perda-resposta"]


def escopo():
    linha = [{"passo": p, "mecanismo": True, "liga_ao_proximo": l, "cards": sorted({c for i in its for c in CARDS.get(i, [])})} for p, l, its in LINHA]
    return {"ciclo": "básico", "justificativa": "Deck-prova independente das aulas (F-20261029-CLAUDE-04): farmacodinâmica geral dos objetivos cognitivos; fármaco por nome só como exemplo que o material cobra.",
            "clinica_lateral": [], "clinica_e_tema": False, "motivo_tema": "", "ordem_da_fala": [], "historia": HISTORIA, "linha_logica": linha,
            "cards_de_conexao": CONEXAO, "provas": [{"id": _qid(x), "cards": x.get("cards", [])} for x in matriz()["linhas"] if x["tipo"] == "questao"],
            "uso_das_fontes": {f: sorted({c for i in its for c in CARDS.get(i, [])}) for f, its in USO.items()}}


USO = {"aula": ["f2", "a1", "c5", "g1", "n1", "r1"],  # base da prova: objetivos e resumo da aula 1
       "prova": ["f3", "a3", "c3", "g3", "n4", "x1"],  # questões orientadoras, exemplos dos professores e banco
       "bibliografia": ["r2", "n3"],  # Rang cap. 2: mecanismos de perda de resposta e antagonismo não competitivo
       "apostila": ["f5", "a5", "a6", "n6"]}  # resumo da aula 1 feito por aluno (veteranos) e Ferro et al.
FONTE_Q = {"fontes/orientadoras-fd.pdf": "FD", "fontes/objetivos.pdf": "Prof", "fontes/todas-questoes.pdf": "Banco"}


def _qid(x):
    return f"{FONTE_Q[x['fonte']]} {x['id']}"


def indice_provas():
    """fontes/provas-deck-prova.txt no formato do índice de provas ('── [fonte] id texto'), lido pelo gate de calibragem."""
    return "\n".join(f"── [{FONTE_Q[x['fonte']]}] {x['id']} {x['trecho']}" for x in matriz()["linhas"] if x["tipo"] == "questao") + "\n"


if __name__ == "__main__":
    (HERE / "matriz-prova.json").write_text(json.dumps(matriz(), ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "mapa-de-profundidade.json").write_text(json.dumps(mapa(), ensure_ascii=False, indent=1), encoding="utf-8")
    mot = HERE / "motivacoes.json"
    congelado = HERE / "etapas" / "E3-motivacoes.json"
    if not congelado.exists():  # depois da E3 as motivações ficam congeladas; só 'atendida_por' muda
        mot.write_text(json.dumps(motivacoes(), ensure_ascii=False, indent=1), encoding="utf-8")
    else:
        d = json.loads(mot.read_text(encoding="utf-8"))
        for x in d["motivacoes"]:
            x["atendida_por"] = CARDS.get(x["item_mapa"], [])
        mot.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "inventario.py").write_text(inventario(), encoding="utf-8")
    (HERE / "fontes" / "provas-deck-prova.txt").write_text(indice_provas(), encoding="utf-8")
    esc = HERE / "escopo.json"
    e = escopo()
    if esc.exists():  # campos escritos à mão depois (uso_das_fontes, cards_de_conexao) ficam
        velho = json.loads(esc.read_text(encoding="utf-8"))
    esc.write_text(json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(ITENS)} itens; matriz com {len(matriz()['linhas'])} linhas")
