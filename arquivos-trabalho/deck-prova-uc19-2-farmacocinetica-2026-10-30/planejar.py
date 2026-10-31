"""Planejamento do lote 2 do deck-prova UC19 (Farmacocinética qualitativa), fonte única da E3 em diante (F-20261029-CLAUDE-04).

    /usr/bin/python3 planejar.py      # grava mapa-de-profundidade.json, motivacoes.json, matriz-prova.json, inventario.py, escopo.json

ITENS é o que a prova cobra, tirado das fontes base (objetivos FC a–e, apostila, De Nucci cap. 1, questões orientadoras FC, banco) e
conferido no Rang caps. 8–9. CARDS (item → chaves do spec) é preenchido depois da busca (E4/E5); a matriz e o mapa saem daqui.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.base_prova import texto_paginas  # noqa: E402

# id: (página da base, tipo, o que Davi tem de saber, fonte, termos que o card precisa conter)
ITENS = {

 "q1": (1, "explicar", "Ácido fraco fica não ionizado em meio ácido e base fraca em meio alcalino (Henderson-Hasselbalch); só a forma não ionizada atravessa membrana.", "objetivos a.i; apostila p.14; De Nucci p.11; banco p.64", ["ionized"]),
 "q2": (1, "explicar", "Lipossolubilidade (coeficiente de partição óleo/água) e baixo peso molecular facilitam a difusão; acima de cerca de 1.000 Da não atravessa.", "objetivos a.ii; De Nucci p.6; banco p.7 e p.64", ["lipid"]),
 "q3": (1, "organizar", "Passagem por membrana: difusão passiva (a maioria), poros aquosos, difusão facilitada, transporte ativo e endocitose/pinocitose.", "objetivos a.iii; apostila p.14; banco p.62 e p.74", ["diffusion"]),
 "q4": (4, "e-se", "Captura iônica: ácido fraco se concentra no compartimento alcalino e base fraca no ácido (estômago, urina).", "objetivos a.iv; De Nucci p.11", ["trap"]),
 "q5": (5, "e-se", "Ácido fraco (AAS, clorotiazida) absorve melhor em pH abaixo do pKa; base fraca (anfetamina) quase não absorve no estômago.", "apostila ex.3; banco p.31 e p.68", ["acidic"]),
 "q6": (3, "organizar", "Transportadores SLC (OAT, OCT) e ABC (P-gp) carregam fármacos; OAT e OCT secretam no túbulo proximal.", "De Nucci p.8; apostila p.14", ["OAT"]),
 "v1": (6, "organizar", "Vias enterais (oral e sublingual), parenterais (IV, IM, SC) e outras (retal, aérea, epidural, intradural, intra-óssea, intra-arterial, intracavernosa, intraperitoneal).", "apostila p.11–12; objetivos b.iv; banco p.57", ["route"]),
 "v2": (6, "distinguir", "IV: absorção imediata, F = 100%, dose ajustável; riscos de infecção, trombose local e precipitação de misturas.", "apostila p.11; banco p.24, p.55 e p.60", ["intravenous"]),
 "v3": (6, "explicar", "Oral: cômoda, mas sofre pH gástrico, alimento, enzimas, microbiota e primeira passagem; absorção lenta e variável.", "apostila p.11; banco p.5 e p.32", ["oral"]),
 "v4": (6, "distinguir", "Sublingual evita a primeira passagem (nitroglicerina); retal evita em parte, porque as veias retais inferiores drenam para a cava.", "apostila p.11; banco p.12 e p.65", ["sublingual"]),
 "v5": (6, "distinguir", "IM é mais rápida que SC; preparações de depósito liberam devagar; SC absorve por capilares e linfáticos.", "apostila p.12; banco p.3 e p.5", ["intramuscular"]),
 "v6": (6, "explicar", "Inalatória: absorção rápida pela área alveolar e efeito local com pouca dose sistêmica; transdérmica libera contínuo e evita a primeira passagem.", "apostila p.12; objetivos b.vi–vii; banco p.30", ["transderm"]),
 "v7": (7, "distinguir", "Referência (inovador, marca, patente); genérico (mesmo princípio ativo, dose e forma, vendido pelo princípio, intercambiável); similar (marca própria).", "apostila p.12–13; banco p.23, p.29, p.58, p.68, p.82", ["generic"]),
 "v8": (7, "explicar", "Equivalência farmacêutica é in vitro; bioequivalência é in vivo, com ASC (extensão) e Cmáx/Tmáx (velocidade) equivalentes.", "apostila p.13; banco p.29 e p.55", ["bioequivalen"]),
 "v9": (8, "explicar", "Formulação muda a absorção ou o clearance, não a eliminação intrínseca: liberação prolongada (morfina), depósito, PEGuilação, glargina.", "questões orientadoras 10, 39 e 40; objetivos b.v", ["release"]),
 "b1": (11, "decorar", "Biodisponibilidade (F) é a fração da dose que chega inalterada à circulação sistêmica; IV = 100%; F = ASC oral / ASC IV.", "objetivos b.viii; apostila p.14; banco p.21 e p.63", ["bioavailability"]),
 "b2": (11, "explicar", "Primeira passagem: intestino e fígado (veia porta) metabolizam o fármaco antes da circulação sistêmica e reduzem a F oral.", "objetivos b.iii; apostila p.14; banco p.1, p.5 e p.78", ["bioavailability"]),
 "b3": (10, "organizar", "Fatores da absorção: lipossolubilidade, ionização, fluxo sanguíneo, área, tempo de contato, esvaziamento gástrico, alimento, formulação.", "objetivos b.ii–iii; apostila ex.8; banco p.51 e p.56", ["blood flow"]),
 "b4": (12, "explicar", "Glicoproteína P (MDR1, ABC) bombeia fármaco para fora: no enterócito reduz a absorção, na BHE impede a entrada no SNC, excreta na bile e na urina.", "apostila p.14; De Nucci p.8", ["P-glycoprotein"]),
 "b5": (12, "e-se", "Inibir a P-gp (toranja, verapamil, cetoconazol) aumenta o substrato: loperamida entra no SNC e deprime.", "apostila ex.7; banco p.3 e p.89", ["P-glycoprotein"]),
 "b6": (11, "distinguir", "Biodisponibilidade absoluta compara com a IV; relativa compara duas formulações pela mesma via.", "banco p.78", ["AUC"]),
 "b7": (10, "explicar", "Idade e doença mudam a absorção (acloridria, esvaziamento gástrico, fluxo; neonato e idoso).", "objetivos b.ix; banco p.56", ["absorption"]),
 "d1": (16, "decorar", "Compartimentos (70 kg): plasma cerca de 3–4 L, extracelular cerca de 14 L, água corporal total cerca de 42 L.", "De Nucci p.5; banco p.43", ["plasma"]),
 "d2": (16, "explicar", "Vd = quantidade no corpo / concentração plasmática; é aparente: baixo quando o fármaco fica no plasma (grande, muito ligado), alto quando se acumula em tecidos.", "objetivos c.vi; De Nucci p.5; apostila ex.9; banco p.8 e p.11", ["volume of distribution"]),
 "d3": (17, "explicar", "Só a fração livre age, se distribui, é metabolizada e filtrada; ácidos ligam à albumina, bases à α1-glicoproteína ácida.", "objetivos c.i; De Nucci p.6–7; banco p.4 e p.80", ["free"]),
 "d4": (17, "e-se", "Deslocar a ligação (varfarina + AAS ou sulfa) ou a hipoalbuminemia aumentam a fração livre; importa no fármaco muito ligado e de IT estreito.", "De Nucci p.6; banco p.87", ["warfarin"]),
 "d5": (18, "explicar", "Barreira hematoencefálica: endotélio com junções firmes, sem fenestras, com P-gp; passa o lipofílico pequeno.", "objetivos c.v; De Nucci p.9", ["blood-brain barrier"]),
 "d6": (14, "explicar", "A placenta deixa passar o fármaco lipofílico (risco fetal); o capilar sinusoide hepático é fenestrado.", "objetivos c.v; banco p.66", ["placenta"]),
 "d7": (19, "explicar", "Redistribuição: lipofílico IV vai primeiro ao cérebro e aos órgãos muito irrigados, depois ao músculo e à gordura; o efeito acaba antes da eliminação (tiopental).", "objetivos c.iv; questão orientadora 35; banco p.76 e p.78", ["redistribution"]),
 "d8": (14, "e-se", "Acúmulo em tecidos: gordura (tiopental), osso e dente (tetraciclina), pulmão e fígado (amiodarona).", "banco p.78", ["tetracycline"]),
 "d9": (16, "e-se", "Hemodiálise só remove bem fármaco de Vd pequeno e pouco ligado.", "banco p.55 e p.65", ["dialysis"]),
 "d10": (14, "explicar", "Idade e doença mudam a distribuição: idoso tem mais gordura e menos água; neonato e hipoalbuminemia mudam a ligação.", "objetivos c.vii; banco p.66", ["elderly"]),
 "m1": (21, "explicar", "Metabolizar torna o fármaco mais polar para ser excretado, porque o rim reabsorve o lipofílico; ocorre sobretudo no fígado.", "objetivos d.i; apostila p.17; banco p.68", ["polar"]),
 "m2": (21, "organizar", "Fase I (oxidação, redução, hidrólise; CYP450 no retículo liso) e fase II (conjugação: glicuronidação, sulfatação, acetilação, glutationa).", "objetivos d.iii; apostila p.17; questão orientadora 21; banco p.32", ["phase"]),
 "m3": (22, "decorar", "CYP3A4/5 metaboliza a maior parte dos fármacos; depois vêm CYP2D6, 2C9, 1A2, 2C19 e 2E1.", "objetivos d.iv; De Nucci p.12; questão orientadora 22", ["CYP3A4"]),
 "m4": (22, "e-se", "Indutores (rifampicina, fenitoína, carbamazepina, fenobarbital, álcool crônico, erva-de-são-joão, fumo no CYP1A2) aumentam o metabolismo e baixam o nível do substrato.", "objetivos d.v; questões orientadoras 3, 5 e 25; banco p.48 e p.84", ["inducer"]),
 "m5": (22, "e-se", "Inibidores (cetoconazol, macrolídeos, toranja, cimetidina, ritonavir; fluvoxamina no 1A2; dissulfiram no 2E1) sobem o nível do substrato.", "objetivos d.vi; questões orientadoras 2, 24, 26 e 30; banco p.49", ["inhibitor"]),
 "m6": (22, "explicar", "Pró-fármaco é ativado pelo metabolismo (enalapril, codeína pela 2D6, clopidogrel pela 2C19); metabólito pode ser ativo ou tóxico (paracetamol → NAPQI).", "objetivos d.ii; questão orientadora 23; banco p.63", ["prodrug"]),
 "m7": (23, "e-se", "Farmacogenética: acetilador lento (NAT2) acumula isoniazida; CYP2D6 ultrarrápido e codeína; CYP2C19 lento e clopidogrel; CYP2C9 e varfarina.", "De Nucci p.13–14; questões orientadoras 4 e 27", ["acetylator"]),
 "m8": (22, "explicar", "Idade e doença: neonato e idoso têm menos fase I; a cirrose reduz o metabolismo (AUC sobe com o Child-Pugh); a glicuronidação é mais preservada.", "objetivos d.vii; questões orientadoras 6, 28 e 29", ["elderly"]),
 "e1": (25, "distinguir", "Eliminação = metabolismo + excreção; excreção é a saída do fármaco ou do metabólito: rim, bile e fezes, pulmão (anestésicos inalatórios), leite, suor.", "objetivos e.i–ii e e.vi; banco p.52", ["excret"]),
 "e2": (27, "explicar", "Excreção renal: filtração glomerular (só o livre), secreção ativa no túbulo proximal (OAT ânions, OCT cátions; probenecid compete) e reabsorção passiva do lipofílico.", "objetivos e.iii; apostila p.17; De Nucci p.10", ["filtration"]),
 "e3": (27, "e-se", "Alcalinizar a urina (bicarbonato) acelera a excreção de ácido fraco (salicilato, fenobarbital); acidificar acelera a de base fraca (anfetamina).", "De Nucci p.11; banco p.9 e p.87", ["urine"]),
 "e4": (25, "explicar", "Circulação êntero-hepática: o conjugado excretado na bile é desconjugado pelas bactérias e reabsorvido, prolongando a ação.", "objetivos e.iv; banco p.35", ["enterohepatic"]),
 "e5": (28, "decorar", "Clearance = taxa de eliminação / concentração (volume depurado por tempo); os clearances se somam (total = renal + hepático + outros).", "objetivos e.vii; De Nucci p.9; questões orientadoras 11, 18 e 19; banco p.75", ["clearance"]),
 "e6": (26, "explicar", "Cl do órgão = E × Q, com E = (Ca − Cv)/Ca; alta extração (lidocaína, morfina, propranolol) depende do fluxo; baixa (varfarina, diazepam), da enzima e da fração livre.", "objetivos e.vii; apostila p.17; questões orientadoras 12–17 e 20", ["extraction"]),
 "e7": (29, "explicar", "Clearance renal = U × V / P; a inulina mede a TFG; a creatinina estima (Cockcroft-Gault) e superestima na IRA, na cirrose e na obesidade.", "De Nucci p.11; questões orientadoras 36–38; banco p.59", ["clearance"]),
 "e8": (25, "e-se", "Na insuficiência renal, fármaco de eliminação renal (aminoglicosídeo) precisa de dose menor ou intervalo maior.", "banco p.18, p.55 e p.65", ["renal"]),
 "e9": (31, "e-se", "Cilastatina inibe a desidropeptidase I renal e protege o imipenem.", "questão orientadora 9", ["cilastatin"]),
 "x1": (32, "e-se", "Cetoconazol inibe o CYP3A4: a terfenadina acumula e prolonga o QT.", "questão orientadora 2", ["QT"]),
 "x2": (32, "explicar", "Rifampicina induz o CYP2C9 e o 3A4: o nível da varfarina cai e o INR baixa.", "questão orientadora 3", ["warfarin"]),
 "x3": (32, "e-se", "O fumo induz o CYP1A2: parar de fumar eleva a teofilina a nível tóxico.", "questão orientadora 5", ["theophylline"]),
 "q1b": (1, "decorar", "Quando o pH é igual ao pKa, metade do fármaco está ionizada; pKa baixo deixa mais base não ionizada em pH fisiológico.", "objetivos a.i; De Nucci p.11", ["pK"]),
 "v4b": (6, "explicar", "O reto acima da linha pectínea drena para a porta e abaixo para a circulação sistêmica; por isso a via retal escapa só em parte da primeira passagem.", "apostila p.12; banco p.12", ["portal"]),
 "v5b": (6, "e-se", "Preparações de depósito (penicilina benzatina, DMPA, antipsicóticos de depósito) liberam o fármaco devagar a partir do músculo.", "apostila p.11–12; objetivos b.v", ["depot"]),
 "v6b": (6, "explicar", "Corticoide inalatório age no pulmão com pouco efeito sistêmico, porque a dose que chega à circulação é pequena.", "apostila p.12; objetivos b.vii", ["inhaled"]),
 "v9b": (8, "e-se", "PEGuilação aumenta a molécula e prolonga a meia-vida; a glargina tem ação longa por absorção lenta.", "questões orientadoras 39 e 40", ["glargine"]),
 "b2b": (11, "e-se", "Nitrato oral exige dose alta pela primeira passagem; carcinoide com metástase hepática escapa da primeira passagem e causa síndrome carcinoide.", "objetivos b.viii; banco p.78", ["first pass"]),
 "b3b": (10, "e-se", "Interações de absorção: quelação de tetraciclina e quinolona por cátions, IBP e antiácido mudando o pH, resina de ácido biliar retendo estatina.", "objetivos b.iii; questão orientadora 30", ["chelat"]),
 "d1b": (16, "decorar", "Em 70 kg: água corporal total 42 L, intracelular 28 L, extracelular 14 L (interstício 10 L, plasma 4 L).", "De Nucci p.5; banco p.43", ["42"]),
 "d2b": (16, "explicar", "O Vd depende da molécula: grande, carregada ou ligada a proteína plasmática tem Vd baixo; pequena hidrofílica, médio; pequena lipofílica, alto.", "De Nucci p.5; apostila ex.9; banco p.11", ["charged"]),
 "d2c": (16, "decorar", "Vd baixo deixa o fármaco no vaso, médio no extracelular, alto em todos os tecidos, inclusive gordura.", "De Nucci p.5; banco p.8", ["compartment"]),
 "d3b": (17, "distinguir", "Albumina liga fármacos ácidos e neutros; α1-glicoproteína ácida liga básicos.", "De Nucci p.6–7; banco p.80", ["albumin"]),
 "d3c": (17, "explicar", "Ligação extensa a proteína retarda a eliminação, porque só a fração livre é filtrada e metabolizada.", "objetivos c.i; De Nucci p.7", ["protein binding"]),
 "d5b": (18, "e-se", "Anti-H1 de 1ª geração (lipofílico) cruza a BHE e seda; os de 2ª geração não cruzam.", "objetivos c.v; De Nucci p.9", ["blood-brain"]),
 "d7b": (19, "organizar", "Depois do bolus o fármaco passa do plasma aos órgãos muito irrigados, depois ao músculo e por fim à gordura.", "questão orientadora 35; banco p.76", ["compartment"]),
 "m2b": (21, "explicar", "Fase II conjuga (glicuronidação, sulfatação, acetilação, metilação) e gera metabólito muito polar e em geral inativo.", "objetivos d.iii; banco p.32", ["Phase II"]),
 "m2c": (21, "e-se", "A UGT glicuronida também a bilirrubina; atividade baixa da UGT explica a síndrome de Gilbert.", "De Nucci p.12 (UGT)", ["glucuronosyltransferase"]),
 "m3b": (22, "decorar", "Isoformas e substratos clássicos: estatinas pelo CYP (exceto pravastatina), etanol pelo CYP2E1, opioides orais pelo CYP2D6.", "objetivos d.iv; De Nucci p.12", ["CYP"]),
 "m4b": (22, "e-se", "Rifampicina induz o CYP e derruba inibidores de protease do HIV; por isso se usa rifabutina.", "objetivos d.v", ["Rifabutin"]),
 "m4c": (22, "e-se", "Anticonvulsivantes indutores aceleram o metabolismo da vitamina D (CYP24A1) e causam osteopenia.", "objetivos d.v (anticonvulsivantes)", ["osteopenia"]),
 "m5b": (22, "distinguir", "Entre os inibidores: ritonavir é o mais potente, voriconazol o azólico mais propenso, azitromicina é o macrolídeo que não inibe.", "objetivos d.vi", ["Azithromycin"]),
 "m6b": (22, "e-se", "Metabólito tóxico: o paracetamol forma NAPQI, que esgota a glutationa hepática.", "objetivos d.ii (metabólitos tóxicos)", ["NAPQI"]),
 "m6c": (22, "e-se", "Pró-fármacos ativados pelo CYP no fígado: nitrosoureias e ciclofosfamida; colecalciferol vira 25-OH no fígado.", "objetivos d.ii; De Nucci p.14", ["activated"]),
 "m7b": (23, "e-se", "Acetiladores lentos têm mais lúpus induzido por hidralazina, procainamida e isoniazida (HEαPS PIMP).", "De Nucci p.13", ["lupus"]),
 "m7c": (23, "e-se", "Polimorfismos: VKORC1 e CYP2C9 mudam a dose da varfarina; CYP2D6 ativa codeína, oxicodona e hidrocodona.", "De Nucci p.13–14; questão orientadora 27", ["CYP2D6"]),
 "m8b": (22, "e-se", "Neonato tem pouca UGT: síndrome do bebê cinzento com cloranfenicol e icterícia fisiológica.", "objetivos d.vii; questão orientadora 28", ["glucuronosyltransferase"]),
 "m8c": (22, "e-se", "Na doença hepática preferem-se benzodiazepínicos só glicuronidados (lorazepam, oxazepam, temazepam: LOT).", "questão orientadora 29 (Child-Pugh)", ["LOT"]),
 "e2b": (27, "e-se", "Probenecida inibe o OAT do túbulo proximal, reduz a secreção da penicilina e aumenta o nível dela.", "objetivos e.iii; De Nucci p.10", ["Probenecid"]),
 "e3b": (27, "e-se", "Superdose de ácido fraco (aspirina, fenobarbital, metotrexato) trata-se com bicarbonato para alcalinizar a urina; acidificar para bases não se usa mais.", "De Nucci p.11; banco p.9", ["bicarbonate"]),
 "e6b": (26, "distinguir", "Alta extração (propofol, lidocaína) depende do fluxo hepático; baixa extração (benzodiazepínicos, diazepam) depende da enzima.", "apostila p.17; questões orientadoras 16 e 17", ["extraction"]),
 "e7b": (29, "distinguir", "Inulina mede a TFG (filtrada, sem secreção nem reabsorção); a creatinina estima e superestima um pouco, porque é secretada.", "De Nucci p.11; questões orientadoras 37 e 38", ["inulin"]),
 "e8b": (25, "decorar", "A função renal cai com a idade, e a insuficiência renal predispõe à toxicidade da digoxina.", "banco p.66; objetivos e.v", ["renal"]),
 "x4": (32, "e-se", "Omeprazol inibe o CYP2C19 e reduz a ativação do clopidogrel.", "questão orientadora 7", ["clopidogrel"]),
}

PASSOS = [("Química e membranas", ["q3", "q2", "q1", "q1b", "q4", "q5", "q6"]), ("Vias e tipos de medicamento", ["v1", "v2", "v3", "v4", "v4b", "v5", "v5b", "v6", "v6b", "v7", "v8", "v9", "v9b"]),
          ("Absorção e biodisponibilidade", ["b3", "b3b", "b7", "b1", "b2", "b2b", "b6", "b4", "b5"]), ("Distribuição", ["d6", "d8", "d10", "d1", "d1b", "d2", "d2b", "d2c", "d9", "d3", "d3b", "d3c", "d4", "d5", "d5b", "d7", "d7b"]),
          ("Metabolismo", ["m1", "m2", "m2b", "m2c", "m3", "m3b", "m4", "m4b", "m4c", "m5", "m5b", "m6", "m6b", "m6c", "m8", "m8b", "m8c", "m7", "m7b", "m7c"]), ("Excreção e clearance", ["e1", "e4", "e8", "e8b", "e6", "e6b", "e2", "e2b", "e3", "e3b", "e5", "e7", "e7b", "e9"]),
          ("Aplicação (casos clínicos)", ["x1", "x2", "x3", "x4"])]

def _tabela():
    """item → nids/chaves, lido de tabela.tsv (a mesma tabela monta o spec); EXTRA liga o card a um segundo item que ele também atende."""
    out = {}
    for l in (HERE / "tabela.tsv").read_text(encoding="utf-8").splitlines():
        if l.startswith("#") or not l.strip():
            continue
        x, item = l.split("\t")[:2]
        out.setdefault(item, []).append(int(x) if x.isdigit() else x)
    for item, xs in EXTRA.items():
        out[item] = out.get(item, []) + xs
    return out


EXTRA = {"q4": [1474922575831, 1474922592292, 1490066246680], "b7": [1461625020267, 1482022155210], "m6": ["sh-1792624476548"],
         "x1": [1610226160551], "m5": [1505674844706, 1474580933087], "b1": [1506725542995], "v5": [1503601179202], "d2": [1521932728741]}
CARDS_SRC = _tabela()
TERMOS = {}
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


CARDS = _resolver() if __name__ != "spec" else {}  # o spec só lê ITENS

# Matriz: (id, fonte, tipo, âncora do trecho literal, itens) — questões numeradas pelo próprio enunciado
F = {"O": ("fontes/objetivos.pdf", 3, 6), "A": ("fontes/apostila.pdf", 18, 20), "Q": ("fontes/orientadoras-fc.pdf", 1, 10),
     "T": ("fontes/todas-questoes.pdf", 1, 91)}
L3 = lambda o: ("fora", "fora-do-escopo", f"Cálculo de farmacocinética quantitativa ({o}): entra no deck-prova 3, que cobre ke, t½, Css e doses.")
L1 = lambda o: ("fora", "fora-do-escopo", f"Coberto no deck-prova 1 (Farmacodinâmica): {o}.")
QUESTOES = {1: L3("dose de ataque pela aminofilina"), 2: ["x1", "m5"], 3: ["x2", "m4"], 4: ["m7"], 5: ["x3", "m4"], 6: ["m8"], 7: ["x4", "m6"],
            8: L3("Vd, ke e t½ de um bolus"), 9: ["e9", "e2"], 10: ["v9"], 11: ["e5"], 12: ["e6"], 13: ["e6"], 14: ["e6"], 15: ["e6"], 16: ["e6"],
            17: ["e6", "d3"], 18: ["e5"], 19: ["e5"], 20: ["e6"], 21: ["m2"], 22: ["m3"], 23: ["m6"], 24: ["m5"], 25: ["m4"], 26: ["m5"], 27: ["m7"],
            28: ["m8"], 29: ["m8"], 30: ["m5", "b5"], 31: L3("fase de distribuição do bolus"), 32: L3("modelo monocompartimental"),
            33: L3("linearização ln C"), 34: L3("t½ = 0,693/ke"), 35: ["d7"], 36: ["e7"], 37: ["e7"], 38: ["e7"], 39: ["v9"], 40: ["v9"]}
OUTRAS = [  # (id, chave de F, tipo, âncora, itens ou ("fora", motivo, porquê))
 ("obj-a1", "O", "item", "i. Ácidos e bases fracas; a equação de Henderson-Hasselbalch", ["q1"]),
 ("obj-a2", "O", "item", "ii. Solubilidade em lipídios de espécies de fármacos", ["q2"]),
 ("obj-a3", "O", "item", "iii. Propriedades das membranas biológicas", ["q3", "q6"]),
 ("obj-a4", "O", "item", "iv. Captura iônica de fármacos", ["q4", "e3"]),
 ("obj-a5", "O", "item", "v. Quiralidade", L1("enantiômeros, item n7")),
 ("obj-b1", "O", "item", "i. Conceito de janela terapêutica", L1("janela terapêutica, item c6")),
 ("obj-b2", "O", "item", "ii. Relação de lipossolubilidade, fluxo sanguíneo", ["b3"]),
 ("obj-b3", "O", "item", "iii. Efeito do pH; absorção de ácidos e bases fracas", ["q5", "b2", "b7"]),
 ("obj-b4", "O", "item", "iv. Absorção por via oral, IM, SC e outras vias", ["v1", "v3", "v5"]),
 ("obj-b5", "O", "item", "v. Manipulação de absorção", ["v9", "v5"]),
 ("obj-b6", "O", "item", "vi. Locais especiais de absorção", ["v4", "v6"]),
 ("obj-b7", "O", "item", "vii. Absorção sistêmica de fármacos aplicadas para efeitos locais", ["v6"]),
 ("obj-b8", "O", "item", "viii. Conceito de biodisponibilidade", ["b1", "b2"]),
 ("obj-b9", "O", "item", "ix. Mudanças no desenvolvimento, aspectos relacionados à idade e às doenças na absorção", ["b7"]),
 ("obj-c1", "O", "item", "i. Ligação às proteínas plasmáticas, seus efeitos", ["d3", "d4"]),
 ("obj-c2", "O", "item", "ii. O sistema linfático e a distribuição", ["v5"]),
 ("obj-c3", "O", "item", "iii. Fatores que afetam a distribuição", ["d2", "d8"]),
 ("obj-c4", "O", "item", "iv. Distribuição (\"redistribuição\")", ["d7"]),
 ("obj-c5", "O", "item", "v. Distribuição de medicamentos em compartimentos especiais", ["d5", "d6", "b4"]),
 ("obj-c6", "O", "item", "vi. Conceito de volumes aparentes de distribuição", ["d1", "d2"]),
 ("obj-c7", "O", "item", "vii. Mudanças no desenvolvimento, relacionados à idade e às doenças e relações com a distribuição", ["d10"]),
 ("obj-d1", "O", "item", "i. Importância do metabolismo de fármacos para a excreção", ["m1"]),
 ("obj-d2", "O", "item", "ii. Biotransformação: ativação vs. inativação", ["m6"]),
 ("obj-d3", "O", "item", "iii. Principais vias de metabolismo: Fase I vs. Fase II", ["m2"]),
 ("obj-d4", "O", "item", "iv. O sistema citocromo P450", ["m3"]),
 ("obj-d5", "O", "item", "v. Indução enzimática", ["m4"]),
 ("obj-d6", "O", "item", "vi. Inibição de enzimas", ["m5"]),
 ("obj-d7", "O", "item", "vii. Mudanças no desenvolvimento (ontogenia)", ["m8"]),
 ("obj-e1", "O", "item", "i. Definição de excreção como a saída", ["e1"]),
 ("obj-e2", "O", "item", "ii. Principais locais de excreção de fármacos", ["e1"]),
 ("obj-e3", "O", "item", "iii. Excreção renal: papel da filtração", ["e2", "e3"]),
 ("obj-e4", "O", "item", "iv. Excreção biliar/alimentar", ["e4"]),
 ("obj-e5", "O", "item", "v. Mudanças no desenvolvimento, relacionadas à idade e doenças e suas relações com a excreção", ["e8"]),
 ("obj-e6", "O", "item", "vi. Diferencie a excreção do conceito farmacológico de eliminação", ["e1"]),
 ("obj-e7", "O", "item", "vii. Clearance (Cl) como o parâmetro", ["e5", "e6"]),
 ("ap1", "A", "questao", "1. A substância B possui", L3("taxa de infusão para Css")), ("ap2", "A", "questao", "2. Um paciente de 35 anos e 70kg", L3("Vd por dose/C0")),
 ("ap3", "A", "questao", "3. A clorotiazida é um ácido fraco", ["q5"]), ("ap4", "A", "questao", "4. Qual dos seguintes tipos de fármacos tem biodisponibilidade", ["b3", "q2"]),
 ("ap5", "A", "questao", "5. Um fármaco com meia-vida de 10 horas", L3("tempo até o equilíbrio")),
 ("ap6", "A", "questao", "6. Assinale a alternativa incorreta em relação as diferentes vias", ["v5", "v2", "v3", "v6"]),
 ("ap7", "A", "questao", "7. Um paciente que faz uso contínuo de um inibidor da glicoproteína P", ["b5"]),
 ("ap8", "A", "questao", "8. Muitas vezes se administra um anestésico junto a um vasoconstritor", ["b3"]),
 ("ap9", "A", "questao", "9. Qual das seguintes moléculas deve apresentar um volume de distribuição", ["d2"]),
 ("ap10", "A", "questao", "10. Foi injetado, por via endovenosa, 200mg", L3("t½ por concentrações")),
]
BANCO = [  # questões do banco dos grupos (fontes/todas-questoes.pdf), lidas inteiras em 30/10; cálculo vai para o lote 3
 ("t-g1a1", "1. Assinale a alternativa em que o meio de administração apresenta efeito de primeira passagem", ["b2", "v4"]),
 ("t-g1a3", "3. Um indivíduo sadio, de 70 kg, dá entrada", L3("t½ da dipirona")),
 ("t-g1b1", "1. Assinale a alternativa INCORRETA: a. Via intramuscular é mais rápida", ["v5"]),
 ("t-g1b2", "2. Um paciente que faz uso contínuo de um inibidor da glicoproteína P", ["b5"]),
 ("t-g1b4", "4. Várias etapas estão envolvidas no processo de desenvolvimento", ["v8"]),
 ("t-g1b5", "5. Leia as seguintes afirmações sobre a interação dos fármacos com células sanguíneas", ["d3"]),
 ("t-g1b6", "6. Muitas vezes se administra um anestésico junto a um vasoconstritor", ["b3"]),
 ("t-g2a1", "1) Propanolol é um bloqueador beta-adrenérgico", ["d3", "d10"]),
 ("t-g2a2", "2) Sobre a administração oral de fármacos, assinale a alternativa INCORRETA", ["v3"]),
 ("t-g2a3", "3) Sobre a administração de fármacos pela via subcutânea", ["v5"]),
 ("t-g2a5", "5) O efeito de primeira passagem se refere ao metabolismo", ["b2"]),
 ("t-g2b1", "1) Um novo fármaco está sendo desenvolvido, esse fármaco possui importante ação intracelular", ["q2"]),
 ("t-g2b4", "4) O volume de distribuição é fundamental para o cálculo da dose", ["d2"]),
 ("t-g3a1", "1) Alcalinização da urina é um tratamento", ["e3"]),
 ("t-g3a4", "4) Segundo a Farmacologia, o conceito de CLEARENCE", ["e5"]),
 ("t-g3b3", "3- Qual das seguintes moléculas deve apresentar um volume de distribuição aparente mais elevado", ["d2"]),
 ("t-g3b5", "5- A via sublingual é utilizada em alguns tratamentos", ["v4"]),
 ("t-g4a2", "2) O clonazepam é o princípio ativo do Rivotril", ["d1"]),
 ("t-g4a3", "3) Considerando que cada gráfico representa uma das seguintes vias", ["v2", "v5"]),
 ("t-g4b1", "1) Os diuréticos de alça são fármacos utilizados", ["d3", "d2"]),
 ("t-g4b4", "4) Na bula de Dipirona Monoidratada", ["e8", "m8"]),
 ("t-g5-1", "1) Em relação a placebo, nocebo e seus efeitos", L1("placebo e nocebo são farmacodinâmica e não caem no roteiro FC")),
 ("t-g5-3", "3) Conhecendo-se as vias de administração dos medicamentos, sabe-se que", ["v1", "b2"]),
 ("t-g5-4", "4) Sobre biodisponibilidade, assinale a alternativa correta", ["b1"]),
 ("t-g6-2", "2) Faça a correspondência das informações com o tipo de medicamento", ["v7"]),
 ("t-g6-5", "5) As vias de administração medicamentosa apresentam vantagens e desvantagens", ["v2"]),
 ("t-g6b3", "Questão 3) Considere dois medicamentos para tratamento de hipertensão arterial", ["d3"]),
 ("t-g7a2", "2. Observe o gráfico abaixo : A área em destaque", ["b1", "v8"]),
 ("t-g7a3", "Sobre os tipos de medicamentos em", ["v7", "v8"]),
 ("t-g7a4", "4. Um paciente sofreu um acidente e se encontra inconsciente", ["v2", "v5"]),
 ("t-g7a5", "5. Sobre a via pulmonar para administração de fármacos", ["v6"]),
 ("t-g8-1", "1- No processo de biotransformação de drogas, os processos de conjugação", ["m2"]),
 ("t-g8-2", "2- Paciente, que sofre de mal de Parkinson", ["v1"]),
 ("t-g8-3", "3- Tendo em vista as facilidades na administração", ["v3"]),
 ("t-g8-5", "5- O preço de um medicamento de referência", ["v7", "v8"]),
 ("t-107-2", "Selecione a alternativa correta: A) Os principais compartimentos de distribuição", ["d1"]),
 ("t-107-flu", "Fluvoxamina é um fármaco inibidor seletivo da recaptação", ["m5"]),
 ("t-107-var", "A varfarina é um fármaco com ação anticoagulante. Baseando-se", ["m4", "x2"]),
 ("t-107-luz", "Os processos por quais o fármaco passa, de sua ingestão até o local de medida", ["b2"]),
 ("t-107-sim", "Assinale a alternativa correta: a) O medicamento similar", ["v7"]),
 ("t-107-fat", "Assinale a alternativa na qual todos são fatores que influenciam a biodisponibilidade", ["b3"]),
 ("t-107-exc", "Qual das seguintes vias / processos NÃO participam da excreção", ["e1"]),
 ("t-107-int", "O volume de distribuição aparente se refere a um aspecto físico", ["d2", "v8"]),
 ("t-107-iv", "As diferentes vias de administração medicamentosas podem apresentar", ["v2"]),
 ("t-107-usos", "Sobre os usos da farmacocinética", ["e8", "d9"]),
 ("t-107-beq", "dois fármacos são bioequivalentes quando", ["v8"]),
 ("t-107-f", "o seguinte gráfico aparece para ilustrar e construir o conhecimento acerca do conceito de biodisponibilidade", ["b7", "b1"]),
 ("t-107-abs", "Quanto ao processo de absorção de um fármaco, assinale a alternativa incorreta", ["b3"]),
 ("t-107-ent", "Quando falamos da Via Enteral podemos dizer que ela engloba", ["v1"]),
 ("t-107-cl", "Tendo em vista o conceito de depuração (clearence)", ["e5"]),
 ("t-107-vias", "A) A via intra-dural deve ser administrada logo abaixo", ["v1"]),
 ("t-107-oxiv", "Se pacientes tomam um medicamento via oral e um via endovenosa", ["m4"]),
 ("t-107-gen", "Acerca dos medicamentos genéricos, a única alternativa ERRADA", ["v7"]),
 ("t-107-clren", "calcule a CL ren para uma substância X", ["e7"]),
 ("t-107-ivp", "Sobre a aplicação intravenosa de fármacos, pode-se destacar", ["v2"]),
 ("t-107-tgi", "A grande parte da absorção pelo TGI ocorre por processos passivos", ["q3", "v4"]),
 ("t-107-pino", "Como ocorre a absorção de fármacos?", ["q3"]),
 ("t-107-cod", "Levando em conta o uso médico, essa droga", ["m6"]),
 ("t-107-f0", "Se um medicamento tem biodisponibilidade absoluta igual a 0", ["b1"]),
 ("t-107-memb", "A partir da consideração dos movimentos dos fármacos através das barreiras celulares", ["q1", "q2", "q4"]),
 ("t-107-liof", "A liofilização é um processo de secagem a frio", ["b3"]),
 ("t-107-subl", "Sobre a via de administração sublingual, assinale a alternativa incorreta", ["v4"]),
 ("t-107-vdhd", "Se Vd for grande, a hemodiálise será uma maneira eficaz", ["d9", "e8"]),
 ("t-107-clrf", "Com relação ao clearance renal das drogas, assinale a alternativa falsa", ["e5", "e7"]),
 ("t-107-idoso", "Os pacientes idosos requerem atenção especial", ["d10", "d6"]),
 ("t-107-vdap", "O volume de distribuição (Vd) representa um volume aparente", ["d2"]),
 ("t-107-fnao", "Quais dos itens abaixo", ["b3"]),
 ("t-107-bio", "Sobre a biotransformação é correto", ["m1"]),
 ("t-107-pka", "qual das substâncias terá pior absorção no estômago", ["q5"]),
 ("t-107-gxr", "Qual a diferença entre medicamento genérico e medicamento de referência", ["v7"]),
 ("t-107-fat2", "Quanto aos fatores intervenientes na farmacocinética", ["m1", "d3"]),
 ("t-107-mod", "Sabe-se que o modelo monocompartimental", L3("modelos compartimentais")),
 ("t-107-barr", "A respeito do movimento de fármacos através das barreiras celulares", ["q1", "q3"]),
 ("t-107-fmax", "Qual dos seguintes tipos de fármacos tem biodisponibilidade oral máxima?", ["b3", "b4"]),
 ("t-107-adme", "Sobre o trajeto do fármaco e seu sequenciamento", ["m1", "e1"]),
 ("t-107-adit", "A depuração por vários órgãos de eliminação é aditiva", ["e5"]),
 ("t-107-4c", "utilizando o modelo de 4 compartimentos", ["d7"]),
 ("t-107-fabr", "Qual a diferença entre biodisponibilidade absoluta e relativa", ["b6"]),
 ("t-107-1p", "A fim de reduzir a perda de concentração de um fármaco no metabolismo de", ["b2", "v2"]),
 ("t-107-gord", "Sobre partição dos fármacos na gordura corporal", ["d8", "d7"]),
 ("t-107-pk", "O termo \"Farmacocinética\" pode ser definido", L1("farmacocinética × farmacodinâmica, item f1")),
 ("t-107-prot", "Sobre a interação de fármacos com outras proteínas", ["d3"]),
 ("t-107-graf", "A partir do gráfico de concentração plasmática do", ["b1", "q2"]),
 ("t-107-jul", "Julgue as seguintes afirmações", ["d2", "e5"]),
 ("t-107-ref", "Medicamento referência é um medicamento produzido por um laboratório inovador", ["v7"]),
 ("t-107-gen2", "Sobre os medicamentos genéricos: I- Apresentam eficácia", ["v7", "v8"]),
 ("t-bdz", "Os benzodiazepínicos (BDZ) são ansiolíticos", ["q2", "d7"]),
 ("t-alend", "O alendronato, um medicamento da classe dos bisfosfonatos", ["b3", "d8"]),
 ("t-rif", "O antibiótico rifampicina apresenta importante interação", ["m4"]),
 ("t-gc1", "Sobre vias de administração de medicamentos, assinale a", ["v4", "v1"]),
 ("t-gc2", "Sobre a metabolização e excreção de drogas, assinale a correta", ["e3", "m6"]),
 ("t-gc3", "Interação medicamentosa que não afeta metabolismo ou excreção", ["d4", "m2"]),
 ("t-gc4", "em relação aos conceitos farmacocinéticos fundamentais", ["b1", "m6", "e5"]),
 ("t-gc5", "São processos estudados pela farmacocinética, exceto", L1("farmacocinética × farmacodinâmica, item f1")),
 ("t-gc6", "Qual a condição mais básica para que haja absorção", ["q2"]),
 ("t-gc7", "A glicoproteína P é uma importante proteína responsável pela excreção", ["b5"]),
]


def _txt(chave):
    f, a, z = F[chave]
    return texto_paginas(HERE / f, a, z)


def _linha(id_, k, tipo, txt, ancora, alvo):
    i = txt.find(ancora)
    if i < 0:
        raise SystemExit(f"âncora da matriz não achada: {id_} {ancora!r}")
    linha = {"id": id_, "fonte": F[k][0], "tipo": tipo, "trecho": txt[i:i + max(len(ancora), 40)]}
    if isinstance(alvo, tuple):
        linha.update({"fora": alvo[1], "porque": alvo[2]})
    else:
        linha["itens"] = alvo
    return linha


def matriz():
    txts = {k: _txt(k) for k in F}
    linhas = []
    for n, alvo in QUESTOES.items():
        m = re.search(rf"Questão {n} (.{{20,70}}?\S)(?=\s)", txts["Q"])
        linhas.append(_linha(f"q{n}", "Q", "questao", txts["Q"], m.group(0), alvo))
    for id_, k, tipo, ancora, alvo in OUTRAS:
        linhas.append(_linha(id_, k, tipo, txts[k], ancora, alvo))
    for id_, ancora, alvo in BANCO:
        linhas.append(_linha(id_, "T", "questao", txts["T"], ancora, alvo))
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
    return {"objetivos_da_aula": "Objetivos cognitivos de farmacocinética, itens a–e (química, absorção, distribuição, metabolismo, excreção), "
                                 "as 40 questões orientadoras FC, os exercícios da apostila e o banco de questões dos grupos",
            "cronograma": {"aulas_vizinhas": ["Deck-prova 1 Farmacodinâmica", "UC19 Farmacocinética aulas 1–4 (Prof. Gilberto)", "Deck-prova 3 Farmacocinética quantitativa"],
                           "conferido": "Cronograma 2026 da UC19 lido: farmacocinética nas aulas do Prof. Gilberto; o lote 2 cobre os itens a–e do roteiro e o lote 3, o item f (cinética quantitativa)."},
            "passos": [{"passo": nome, "laminas": ITENS[ids[0]][0], "itens": [
                {"id": i, "tipo": ITENS[i][1], "o_que": ITENS[i][2], "fonte": ITENS[i][3], "termos": TERMOS.get(i, ITENS[i][4]), "cards": CARDS.get(i, [])}
                for i in ids]} for nome, ids in PASSOS],
            "fora": [{"o_que": x[3], "motivo": x[4][2]} for x in OUTRAS if isinstance(x[4], tuple)]}


def motivacoes():
    return {"motivacoes": [{"id": f"m-{i}", "item_mapa": i, "reconstruir": ITENS[i][2],
                            "por_que_dura": f"Item {ITENS[i][1]} cobrado em {ITENS[i][3]}; sem ele a questão correspondente da prova não se responde.",
                            "depois_de": "", "atendida_por": CARDS.get(i, [])} for i in ITENS]}


FAMILIA = [("Objetivos", "objetivos"), ("Apostila", "apostila"), ("De Nucci", "De Nucci"), ("orientadora", "orientadora"), ("Banco", "banco")]


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
    for i in ("q3", "d3", "d7", "m2", "m4", "e2", "e6"):
        dmap["rang-" + i] = i
        cap.append(f"  (\"rang-{i}\", {json.dumps(ITENS[i][2][:90], ensure_ascii=False)}, D.get(\"rang-{i}\", \"\")),")
    D = {k: CARDS.get(i, []) for k, i in dmap.items() if CARDS.get(i)}
    return "\n".join([
        '"""Inventário atômico do deck-prova UC19 lote 2 (Farmacocinética), gerado por planejar.py a partir da base da prova',
        '(fontes/slides.pdf: 32 páginas de excertos literais) e dos itens da E3. Destinos (D) preenchidos depois da busca."""',
        'PREFIXO = "dp2"', 'AULA = "Deck-prova 2 — Farmacocinética (UC19 P1; Farmacologia; Prof. Gilberto)"', "EXC = \"EXC: \"",
        f"D = {json.dumps(D, ensure_ascii=False)}", "", "SLIDES = [", *linhas, "]", "JUSTIFICATIVAS = {}",
        'CAPITULO = [("Rang & Dale caps. 8–9: absorção, distribuição, metabolismo e eliminação", [', *cap, "])]",
        'EXERCICIOS = [("Questões do material (orientadoras FC, apostila, banco)", [', *ex, "])]", ""])


HISTORIA = ("O fármaco só age se chegar ao alvo, e para chegar precisa atravessar membranas: passa o pequeno, lipossolúvel e não ionizado. "
            "A via decide quanto entra e quão rápido: IV entra todo; oral perde na luz, na parede do intestino e no fígado (biodisponibilidade). "
            "No sangue, só a parte livre sai do vaso e se espalha; o Vd mostra quanto ficou fora do plasma. Para sair do corpo, o rim só "
            "elimina o polar, então o fígado metaboliza (fase I, CYP, fase II), e indutores e inibidores mudam esse ritmo. Por fim o rim filtra, "
            "secreta e reabsorve conforme o pH, e o clearance mede a eficiência dessa saída.")
LINHA = [("Atravessar membrana: pequeno, lipossolúvel e não ionizado (pH e pKa)", "A via decide quanto do fármaco atravessa até o sangue", ["q3", "q2", "q1"]),
         ("Vias e formulações: IV entra todo, oral perde na absorção e na primeira passagem", "O que chega ao sangue é a biodisponibilidade", ["v1", "v2", "v3", "v9"]),
         ("Biodisponibilidade: fração que chega inalterada; primeira passagem e P-gp", "No sangue, só a fração livre se distribui", ["b3", "b1", "b2", "b5"]),
         ("Distribuição: fração livre, Vd aparente, barreiras e redistribuição", "Para sair, o lipofílico distribuído precisa virar polar", ["d3", "d2", "d9"]),
         ("Metabolismo: fase I e II, CYP, indução e inibição, pró-fármaco", "O polar é excretado sobretudo pelo rim", ["m2", "m4", "m5"]),
         ("Excreção e clearance: filtração, secreção, reabsorção e Cl = E × Q", "", ["e1", "e2", "e5", "e6"])]
CONEXAO = ["passagem-membrana", "vias-org", "liberacao", "fatores-absorcao", "pgp-loperamida", "dialise-vd", "eliminacao-org"]


def escopo():
    linha = [{"passo": p, "mecanismo": True, "liga_ao_proximo": l, "cards": sorted({c for i in its for c in CARDS.get(i, [])})} for p, l, its in LINHA]
    return {"ciclo": "básico", "justificativa": "Deck-prova independente das aulas (F-20261029-CLAUDE-04): farmacocinética qualitativa dos objetivos cognitivos a–e; fármaco por nome só como exemplo que o material cobra.",
            "clinica_lateral": [], "clinica_e_tema": False, "motivo_tema": "", "ordem_da_fala": [], "historia": HISTORIA, "linha_logica": linha,
            "cards_de_conexao": CONEXAO, "provas": [dict({"id": _qid(x), "cards": x.get("cards", [])}, **({"fora": x["porque"]} if x.get("fora") else {})) for x in matriz()["linhas"] if x["tipo"] == "questao"],
            "uso_das_fontes": {f: sorted({c for i in its for c in CARDS.get(i, [])}) for f, its in USO.items()}}


USO = {"aula": ["q1", "v1", "b1", "d2", "m2", "e5"],  # base da prova: objetivos FC e apostila
       "prova": ["q5", "v7", "b5", "d9", "m4", "x1"],  # questões orientadoras FC, exercícios da apostila e banco
       "bibliografia": ["d3", "m3", "e6"],  # Rang caps. 8–9
       "apostila": ["v4", "b4", "d1", "e7"]}  # apostila guia (veteranos) e De Nucci
FONTE_Q = {"fontes/orientadoras-fc.pdf": "FC", "fontes/apostila.pdf": "Apostila", "fontes/todas-questoes.pdf": "Banco", "fontes/objetivos.pdf": "Prof"}


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
