"""E6/E7 da aula 04 — revisão do plano materializado antes de instalar (rodar depois de fechar_e5.py).
Grava compreensao-aula.json › fidelidade (uma relação por item de aprender, cards conferidos por bloco) e
mapa-de-profundidade.json › revisao (passo explicado com os cards, perguntas-teste, releitura das transcrições)."""
from pathlib import Path
import json, re

R = Path(__file__).parent
P = json.loads((R / "plan.json").read_text())
C = json.loads((R / "compreensao-aula.json").read_text())
M = json.loads((R / "mapa-de-profundidade.json").read_text())
KEYS = {e["key"]: e for e in P["entries"]} | {f"sh-{k}": v for k, v in P["compartilhados"].items()}
UNID = {k: int(re.search(r"\d+", str(e.get("evid", "0"))).group()) for k, e in KEYS.items()}

REL = {
 0: [(["sh-1792697125350", "sh-1792572870657"], "Cérebro = telencéfalo + diencéfalo; o diencéfalo identificado como a parte menor."),
     (["diencefalo-escondido"], "O porquê da vista medial: o telencéfalo cresce e esconde o diencéfalo."),
     (["diencefalo-partes-org"], "As quatro partes num organizador; o Extra traz o metatálamo de alguns autores.")],
 1: [(["diencefalo-partes-org", "sh-1792345309393"], "Sulco hipotalâmico separa tálamo (acima) de hipotálamo (abaixo), com identificação Kenhub do sulco."),
     (["diencefalo-partes-org"], "Subtálamo lateral ao hipotálamo, invisível na vista medial, na linha do organizador."),
     (["sh-1792588687081", "sh-1792345306369"], "Aderência intertalâmica liga os tálamos através do III ventrículo.")],
 2: [(["sh-1792258845028", "sh-1792345644467", "sh-1792572870653", "sh-1792572870652"], "Tubérculo anterior, pulvinar e geniculados identificados no tálamo."),
     (["talamo-limites-org", "sh-1792588687027", "sh-1792588687028"], "Os cinco limites do tálamo no organizador do corte coronal, com dois cards da reserva para os limites superior e medial."),
     (["nucleo-x-ganglio"], "Núcleo dentro do SNC, gânglio fora; tálamo é cinzento.")],
 3: [(["talamo-nucleos-org", "sh-1792345975792"], "Anteriores e mediais ao sistema límbico, identificados no Kenhub."),
     (["talamo-nucleos-org", "sh-1792345977592"], "Laterais: motricidade e sensibilidade."),
     (["ak-1481418712049", "ak-1481418725172"], "Geniculado lateral = visão; medial = audição (AnKing, com o mnemônico do professor no Extra)."),
     (["talamo-nucleos-org", "sh-1792345989291"], "Medianos com função pouco conhecida.")],
 4: [(["hipotalamo-limites-org", "sh-1792588687033"], "Limites superior, lateral e medial do hipotálamo."),
     (["hipotalamo-limites-org", "sh-1792244790744", "sh-1792244786725", "sh-1792244858168"], "Assoalho de diante para trás: quiasma, túber + infundíbulo, corpos mamilares."),
     (["sh-1792244787869", "sh-1792261731096", "ak-1461884702127"], "Infundíbulo prende a hipófise ao túber; ADH e ocitocina descem por ele.")],
 5: [(["hipotalamo-nucleos-org"], "Regiões nomeadas pelo assoalho abaixo de cada uma."),
     (["hipotalamo-nucleos-org", "sh-1792346373316", "sh-1792346374740", "sh-1792346376214"], "Região supraóptica e seus três núcleos."),
     (["hipotalamo-nucleos-org", "io-nucleo-arqueado", "sh-1792346381716", "sh-1792346383240"], "Região tuberal: ventromedial, dorsomedial, arqueado."),
     (["hipotalamo-nucleos-org"], "Região mamilar: mamilares e posteriores.")],
 6: [(["sh-1792572870699"], "Epitálamo identificado na parte posterior do diencéfalo."),
     (["ak-1481418839841", "sh-1792244839896", "sh-1792345317795", "sh-1792572870700"], "Pineal, habênula e comissuras do epitálamo."),
     (["ak-1481418839841"], "Habênula ligada ao sistema límbico (Extra)."),
     (["subtalamo-limites-org", "sh-1792572870698"], "Quatro limites do subtálamo."),
     (["sh-1792347675113", "ak-1481162464655"], "Núcleo subtalâmico motor; hemibalismo na lesão.")],
 7: [(["sh-1792345648666", "sh-1792345652643"], "Septo pelúcido e fórnix identificados entre os ventrículos laterais.")],
 8: [(["faces-hemisferio"], "Três faces do hemisfério."),
     (["giro-x-sulco"], "Giros e sulcos."),
     (["sh-1792261811748", "sh-1792348020020", "sh-1792572870709"], "Sulcos lateral e central, com epônimos no Extra."),
     (["lobos-limites-org", "sh-1792572870660", "sh-1793966747229", "sh-1793966747231", "sh-1793966747230"], "Lobos pelos sulcos e ossos, identificados."),
     (["sh-1792348020020", "lobos-limites-org"], "O central separa frontal e parietal; o cloze de ponta a ponta saiu porque o sulco habitualmente não alcança o lateral.")],
 9: [(["sh-1792261811050"], "Giro pré-central = motor primário."),
     (["sh-1792572870710", "sh-1792572870711", "sh-1792572870713", "sh-1792572870719", "sh-1792572870720"], "Giros e sulcos frontais identificados."),
     (["sh-1792588687051", "sh-1792588687068", "sh-1792588687067"], "Partes do giro frontal inferior e ramos do sulco lateral."),
     (["ak-1481513311304", "sh-1793966747239", "sh-1793889229460"], "Broca no frontal inferior esquerdo; afasia não fluente."),
     (["ak-1481513127112", "sh-1792572870721"], "Giro pós-central = somestésico.")],
 10: [(["sh-1792588687061", "sh-1792348482310"], "Sulco intraparietal separa os lóbulos."),
      (["sh-1792588687059", "sh-1792348479235", "sh-1792572870718"], "Supramarginal e angular no lóbulo inferior."),
      (["sh-1792572870712", "sh-1792572870714", "sh-1792572870715", "sh-1792572870722"], "Giros e sulco temporais."),
      (["sh-1792261728496"], "Ínsula no fundo do sulco lateral (Extra: giros curtos e longo).")],
 11: [(["corpo-caloso-partes-org", "sh-1792572870701"], "Corpo caloso liga os hemisférios."),
      (["corpo-caloso-partes-org", "sh-1792349646457", "sh-1792439186574", "sh-1792349644730"], "Rostro, joelho, tronco e esplênio."),
      (["sh-1792588687078", "sh-1792572870728", "io-sulco-cingulo"], "Giro do cíngulo entre os dois sulcos."),
      (["sh-1792572870724", "sh-1792572870725", "sh-1792572870726"], "Lóbulo paracentral entre paracentral e marginal.")],
 12: [(["io-sulco-parietoccipital", "lobos-limites-org"], "Sulco parietoccipital separa parietal e occipital."),
      (["sh-1792588687071", "sh-1792588687075", "sh-1792572870723", "sh-1792572870727"], "Pré-cúneo e cúneo pelos sulcos que os limitam."),
      (["ak-1481244690823", "sh-1792588687076", "sh-1792345655366"], "Calcarino com a área visual."),
      (["face-inferior-org", "sh-1792349636706", "sh-1792340080484", "sh-1792340082028", "sh-1792349638181"], "Giros da face inferior."),
      (["face-inferior-org"], "Úncus e para-hipocampal no sistema límbico (Extra)."),
      (["achar-sulco-central"], "Achar o sulco central pelos dois giros paralelos.")],
 13: [(["ak-1481162002789"], "Núcleos da base no centro branco, modulando o movimento."),
      (["corte-horizontal-org", "sh-1792338023839", "sh-1792338022186", "sh-1792572870679"], "Sequência do corte horizontal."),
      (["estriado-org", "ak-1481162303980", "sh-1792347668041"], "Lentiforme = putâmen + pálido."),
      (["estriado-org", "sh-1792572870707"], "Corpo estriado = lentiforme + caudado (aula)."),
      (["capsula-interna-partes-org", "sh-1792338018612", "ak-1480389641277"], "Cápsula interna e suas partes."),
      (["corte-horizontal-org", "sh-1792572870736", "sh-1792572870737"], "Cápsulas extrema e externa na sequência do corte.")],
 14: [(["ak-1522347007612", "sh-1792328837674"], "Vertebral pelos forames transversos, identificada."),
      (["vertebrobasilar-org", "ak-1480995292746", "sh-1792350091972"], "PICA, ramo da vertebral."),
      (["vertebrobasilar-org", "sh-1792696998756", "sh-1792350094380"], "Basilar pela união das vertebrais no sulco basilar."),
      (["vertebrobasilar-org", "sh-1792350098581"], "Artéria do labirinto no meato acústico interno (Extra)."),
      (["sh-1792350101581", "sh-1792588687095"], "Cerebelar superior para cerebelo e mesencéfalo."),
      (["sh-1792588687093", "vertebrobasilar-org"], "Basilar termina nas cerebrais posteriores."),
      (["ak-1481513222026", "ak-1481244840641", "sh-1792350088057"], "Território da cerebral posterior e déficit visual.")],
 15: [(["aci-ramos-org", "sh-1792350121479"], "Carótida interna sem ramos no pescoço (Extra)."),
      (["aci-ramos-org"], "Oftálmica antes da dura."),
      (["aci-ramos-org", "sh-1792588687092", "sh-1792350077380", "sh-1792350083556"], "Três ramos intracranianos."),
      (["territorios-org", "sh-1792350083811", "sh-1792348025216", "ak-1481562751403"], "Cerebral média e a face lateral; déficit na face e no membro superior."),
      (["territorios-org", "sh-1792350077635", "sh-1792350077936", "ak-1481562744652"], "Cerebral anterior e a face medial; déficit no membro inferior.")],
 16: [(["willis-org", "sh-1792350075605", "ak-1481772047979"], "Comunicante anterior liga as cerebrais anteriores; aneurisma comprime o quiasma."),
      (["willis-org", "sh-1792350086331", "ak-1481772053364"], "Comunicante posterior liga carótida à cerebral posterior; aneurisma comprime o III."),
      (["willis-org"], "Polígono de Willis na base."),
      (["sh-1792346808763"], "Hipofisária superior da carótida interna.")],
}
NOTA = {
 0: "Abertura do professor pela divisão anatômica, depois o porquê do diencéfalo escondido; partes num organizador, sem exemplo clínico.",
 1: "Sulco hipotalâmico como marco da vista medial e aderência intertalâmica, como no desenho da lousa; identificações Kenhub junto.",
 2: "Divisão e limites do tálamo saem do mesmo corte coronal que o professor desenha; o conceito de núcleo prepara o próximo bloco.",
 3: "Grupos de núcleos com função simples, sem descer aos núcleos específicos (VPL, VPM ficam para a fisiologia), e o mnemônico olho/orelha.",
 4: "Limites do hipotálamo pelo mesmo corte e pelo assoalho; clínica só como associação imediata (quiasma, mamilares) depois do princípio.",
 5: "Regiões pelo assoalho e núcleos por região num organizador; funções clássicas por AnKing nos núcleos que o professor nomeia.",
 6: "Epitálamo e subtálamo curtos como na fala; hemibalismo como a única associação clínica do núcleo subtalâmico.",
 7: "Bloco de imagens: o septo pelúcido e o fórnix entram por identificação; o resto repete os blocos anteriores.",
 8: "Faces, giros/sulcos, três sulcos e quatro lobos na ordem da lousa, com a frase do professor sobre o sulco central.",
 9: "Lobo frontal com as áreas motora, de Broca e somestésica; a afasia vem da Anatomia 01 por associação.",
 10: "Parietal, temporal e ínsula; o occipital lateral sem conteúdo, como o professor diz.",
 11: "Face medial a partir do corpo caloso, subindo pelos sulcos paralelos até o lóbulo paracentral.",
 12: "Occipital medial e face inferior; o achado prático do sulco central fecha o telencéfalo.",
 13: "Núcleos da base pela apostila (sem vídeo): sequência do corte, conjuntos e cápsulas; Huntington e Parkinson como clínica imediata.",
 14: "Sistema vertebrobasilar na ordem do trajeto, com território e uma associação clínica por artéria (bulbo lateral, visão).",
 15: "Sistema carotídeo e territórios corticais pelas faces da aula de telencéfalo; déficit de cada artéria depois do território.",
 16: "Comunicantes e polígono de Willis; aneurismas como relação clínica das comunicantes.",
 17: "Prática: repetição das aulas 03 e 04; nenhum card novo nasce aqui.",
}
blocos = C["blocos"]
fid = []
for i, b in enumerate(blocos):
    lam = b["laminas"]
    do_bloco = sorted(k for k, u in UNID.items() if lam[0] <= u <= lam[1])
    rels = []
    for j, ap in enumerate(b.get("aprender") or []):
        cards, jul = REL[i][j]
        falta = [c for c in cards if c not in KEYS]
        assert not falta, (i, j, falta)
        rels.append({"aprender": ap, "cards": cards, "estado": "recuperavel", "julgamento": jul})
    conf = sorted(set(do_bloco) | {c for r in rels for c in r["cards"]})
    fid.append({"laminas": lam, "bate": True, "nota": NOTA[i], "cards_conferidos": conf or sorted(KEYS)[:1], "relacoes": rels})
todos = {c for f in fid for c in f["cards_conferidos"]}
assert todos >= set(KEYS), sorted(set(KEYS) - todos)[:10]
C["fidelidade"] = {"blocos": fid, "conclusao": (
    "Deck relido na ordem das 62 unidades do percurso (aula sem lâminas): cada relação que o professor ensina tem card do plano; "
    "a maioria do deck são identificações Kenhub (uma por estrutura) e AnKing de relação clínica, com organizadores para as listas da lousa "
    "e poucos clozes autorais; as provas de 2023 e 2025 acrescentaram vias direta/indireta, D1/D2, dor talâmica e alça de Meyer.")}
(R / "compreensao-aula.json").write_text(json.dumps(C, ensure_ascii=False, indent=1))

EXP = {
 0: ("O cérebro é telencéfalo mais diencéfalo, e o diencéfalo é a parte menor. Como o telencéfalo cresce muito, ele esconde o diencéfalo: de lado só se veem telencéfalo e cerebelo, "
     "e o diencéfalo aparece na vista medial, depois do corte sagital mediano. Lá se separam quatro partes, tálamo, hipotálamo, epitálamo e subtálamo; o metatálamo de alguns autores fica dentro do tálamo.",
     ["sh-1792697125350", "diencefalo-escondido", "diencefalo-partes-org"]),
 1: ("Na vista medial, o sulco hipotalâmico corre na parede do III ventrículo: acima dele está o tálamo, abaixo o hipotálamo, atrás o epitálamo. O subtálamo fica lateral ao hipotálamo e por isso "
     "não aparece nessa vista. A aderência intertalâmica atravessa o III ventrículo ligando os dois tálamos, como o corpo caloso liga os hemisférios.",
     ["sh-1792345309393", "diencefalo-partes-org", "sh-1792588687081"]),
 2: ("O tálamo tem o tubérculo anterior na frente e o pulvinar atrás, onde ficam os corpos geniculados. Num corte coronal visto por trás, acima dele está o ventrículo lateral, medialmente o "
     "III ventrículo, lateralmente a cápsula interna, embaixo o hipotálamo (medial) e o subtálamo (lateral). O tálamo é substância cinzenta organizada em núcleos, acúmulos de corpos no SNC.",
     ["sh-1792258845028", "sh-1792345644467", "talamo-limites-org", "nucleo-x-ganglio"]),
 3: ("Os núcleos do tálamo se agrupam pela posição: anteriores e mediais vão ao sistema límbico, laterais à motricidade e sensibilidade, medianos têm função pouco conhecida e os posteriores "
     "trazem os geniculados. O lateral fica mais alto, como o olho, e cuida da visão; o medial fica mais baixo, como a orelha, e cuida da audição.",
     ["talamo-nucleos-org", "ak-1481418712049", "ak-1481418725172"]),
 4: ("O hipotálamo tem o tálamo acima, o subtálamo ao lado e o III ventrículo medialmente. O assoalho, de diante para trás, é quiasma óptico, túber cinéreo com o infundíbulo e corpos mamilares; "
     "o infundíbulo prende a hipófise, por onde descem ADH e ocitocina. A comissura anterior fica na frente e não é limite inferior.",
     ["hipotalamo-limites-org", "sh-1792244790744", "sh-1792244787869", "ak-1461884702127"]),
 5: ("Cada região do hipotálamo tem o nome da estrutura do assoalho abaixo dela: supraóptica sobre o quiasma, tuberal sobre o túber, mamilar sobre os corpos mamilares. "
     "Supraóptica guarda supraóptico, supraquiasmático e paraventricular; tuberal guarda ventromedial, dorsomedial e arqueado; mamilar, mamilares e posteriores. O AnKing dá a função clássica de cada um.",
     ["hipotalamo-nucleos-org", "ak-1481418766004", "ak-1481418757045", "ak-1481418777586"]),
 6: ("O epitálamo fica atrás, com a pineal (que secreta melatonina), a habênula límbica e as comissuras posterior e habenular. O subtálamo fica abaixo do tálamo, acima do mesencéfalo, "
     "medial à cápsula interna e lateral ao hipotálamo; seu núcleo subtalâmico é motor, e a lesão dele dá hemibalismo do outro lado.",
     ["ak-1481418839841", "ak-1481418842065", "subtalamo-limites-org", "ak-1481162464655"]),
 7: ("No corte coronal pelos corpos mamilares e na vista medial, o septo pelúcido fica entre o corpo caloso e o fórnix, separando os dois ventrículos laterais; o resto do bloco de imagens "
     "repete o que já tem card. As identificações do septo e do fórnix mostram onde ficam para a prova prática, no laboratório e nas imagens.",
     ["sh-1792345648666", "sh-1792345652643", "sh-1792572870704"]),
 8: ("O hemisfério tem três faces, e nelas giros (saliências) separados por sulcos. Na face superolateral, os sulcos central e lateral e limites convencionais delimitam os lobos frontal, parietal, "
     "occipital e temporal, cada um sob o osso homônimo. O central separa frontal de parietal e costuma terminar antes do sulco lateral.",
     ["faces-hemisferio", "giro-x-sulco", "lobos-limites-org", "achar-sulco-central"]),
 9: ("À frente do sulco central fica o giro pré-central, área motora; atrás, o pós-central, somestésica. Os sulcos frontais superior e inferior criam três giros frontais. No hemisfério esquerdo, "
     "os ramos anterior e ascendente do sulco lateral dividem o giro frontal inferior em partes orbital, triangular e opercular: Broca corresponde às partes triangular e opercular no hemisfério dominante.",
     ["sh-1792261811050", "ak-1481513127112", "sh-1792588687051", "ak-1481513311304", "sh-1793889229460"]),
 10: ("No parietal, o sulco intraparietal separa os lóbulos superior e inferior, e o inferior tem os giros supramarginal e angular. No temporal, os sulcos temporais criam três giros. "
      "Abrindo o sulco lateral aparece a ínsula, que não fica sob osso nenhum. O occipital lateral não tem nada importante para a aula.",
      ["sh-1792588687061", "sh-1792588687059", "sh-1792572870712", "sh-1792261728496"]),
 11: ("Na face medial, o corpo caloso liga os hemisférios, com rostro, joelho, tronco e esplênio. Acima dele, o sulco do corpo caloso e o sulco do cíngulo cercam o giro do cíngulo. "
      "O sulco paracentral e o marginal delimitam o lóbulo paracentral; à frente dele, o giro frontal superior continua da face lateral para a medial.",
      ["corpo-caloso-partes-org", "sh-1792588687078", "io-sulco-cingulo", "sh-1792572870724"]),
 12: ("O sulco parietoccipital separa parietal de occipital; o pré-cúneo fica antes dele e o cúneo entre ele e o calcarino, onde está o córtex visual. Na face inferior, o grande giro tem três nomes, "
      "occipitotemporal medial, para-hipocampal e úncus, ao lado do occipitotemporal lateral. Na peça, o sulco central fica entre os dois giros paralelos.",
      ["io-sulco-parietoccipital", "sh-1792588687071", "ak-1481244690823", "face-inferior-org", "achar-sulco-central"]),
 13: ("Por dentro do hemisfério, o centro branco guarda os núcleos da base. No corte horizontal, de fora para dentro: córtex da ínsula, cápsula extrema, claustro, cápsula externa, putâmen, globo pálido, "
      "cápsula interna, e caudado e tálamo. Putâmen e pálido formam o lentiforme; com o caudado, o corpo estriado. A cápsula interna leva o trato corticoespinal na perna posterior.",
      ["corte-horizontal-org", "estriado-org", "ak-1481162303980", "capsula-interna-partes-org", "ak-1480389641277"]),
 14: ("A vertebral, ramo da subclávia, sobe pelos forames transversos, entra pelo forame magno e dá a cerebelar inferior posterior, que irriga o bulbo lateral (Wallenberg). As vertebrais formam a "
      "basilar no sulco basilar, que dá a cerebelar inferior anterior, a do labirinto, os pontinos e a cerebelar superior, e termina nas cerebrais posteriores: occipital e temporal inferomedial, incluindo o córtex visual.",
      ["ak-1522347007612", "vertebrobasilar-org", "ak-1480995292746", "sh-1792696998756", "ak-1481244840641"]),
 15: ("A carótida interna sobe sem ramos, entra pelo canal carotídeo e faz o sifão; dá a oftálmica antes da dura e depois a cerebral média, a anterior e a comunicante posterior. A média corre no sulco "
      "lateral e irriga a face lateral (face e membro superior); a anterior vai à fissura longitudinal e irriga a face medial e a faixa superior (membro inferior).",
      ["aci-ramos-org", "territorios-org", "ak-1481562751403", "ak-1481562744652"]),
 16: ("A comunicante anterior une as duas cerebrais anteriores na frente do quiasma; a posterior liga a carótida interna à cerebral posterior. Com as cerebrais formam o polígono de Willis, que une os "
      "sistemas carotídeo e vertebrobasilar. Os aneurismas dessas comunicantes comprimem o quiasma e o oculomotor, vizinhos delas.",
      ["willis-org", "ak-1481772047979", "ak-1481772053364", "sh-1792350075605"]),
}
PT = [
 ("Por que o diencéfalo não aparece na vista lateral?", "O telencéfalo cresce e o esconde.", ["diencefalo-escondido"]),
 ("Quais as partes do diencéfalo?", "Tálamo, hipotálamo, epitálamo, subtálamo.", ["diencefalo-partes-org"]),
 ("O que separa tálamo de hipotálamo?", "O sulco hipotalâmico.", ["diencefalo-partes-org", "sh-1792345309393"]),
 ("O que liga os dois tálamos?", "A aderência intertalâmica.", ["sh-1792588687081"]),
 ("O que fica lateral ao tálamo?", "A cápsula interna.", ["talamo-limites-org"]),
 ("O que fica abaixo e lateral ao tálamo?", "O subtálamo.", ["talamo-limites-org"]),
 ("Qual geniculado é da visão?", "O lateral.", ["ak-1481418712049"]),
 ("Que núcleos do tálamo são límbicos?", "Anteriores e mediais.", ["talamo-nucleos-org"]),
 ("Qual estrutura forma o limite inferior posterior do hipotálamo?", "Os corpos mamilares.", ["hipotalamo-limites-org"]),
 ("O que prende a hipófise?", "O infundíbulo, no túber cinéreo.", ["sh-1792244787869", "hipotalamo-limites-org"]),
 ("Em que região fica o núcleo arqueado?", "Tuberal.", ["hipotalamo-nucleos-org"]),
 ("Qual núcleo do hipotálamo regula o ritmo circadiano?", "Supraquiasmático.", ["ak-1481418766004"]),
 ("Quais estruturas formam o epitálamo?", "Pineal e habênula, com as comissuras.", ["ak-1481418839841"]),
 ("Lesão de qual núcleo dá hemibalismo?", "Subtalâmico, contralateral.", ["ak-1481162464655"]),
 ("O que separa os ventrículos laterais?", "O septo pelúcido.", ["sh-1792345648666"]),
 ("Quais as três faces do hemisfério?", "Superolateral, medial e inferior.", ["faces-hemisferio"]),
 ("Qual sulco separa frontal de parietal?", "O central.", ["lobos-limites-org"]),
 ("Qual giro é a área motora primária?", "Pré-central.", ["sh-1792261811050"]),
 ("Onde fica a área de Broca?", "Giro frontal inferior esquerdo.", ["sh-1793966747239", "ak-1481513311304"]),
 ("O que divide os lóbulos parietais?", "O sulco intraparietal.", ["sh-1792588687061"]),
 ("Onde fica a ínsula?", "No fundo do sulco lateral.", ["sh-1792261728496"]),
 ("Quais as partes do corpo caloso?", "Rostro, joelho, tronco, esplênio.", ["corpo-caloso-partes-org"]),
 ("O que limita o lóbulo paracentral?", "Sulcos paracentral e marginal.", ["sh-1792572870724"]),
 ("Onde fica o córtex visual?", "Nos lábios do sulco calcarino.", ["ak-1481244690823"]),
 ("Qual a ponta anterior do giro para-hipocampal?", "O úncus.", ["face-inferior-org"]),
 ("O que forma o núcleo lentiforme?", "Putâmen e globo pálido.", ["ak-1481162303980", "estriado-org"]),
 ("O que fica entre claustro e putâmen?", "A cápsula externa.", ["corte-horizontal-org"]),
 ("Por onde descem as fibras corticoespinais na cápsula interna?", "Perna posterior.", ["ak-1480389641277"]),
 ("De onde sai a PICA?", "Da artéria vertebral.", ["vertebrobasilar-org"]),
 ("Qual artéria irriga o bulbo lateral?", "A PICA.", ["ak-1480995292746"]),
 ("Como termina a basilar?", "Nas cerebrais posteriores.", ["sh-1792588687093"]),
 ("Qual artéria irriga o lobo occipital?", "Cerebral posterior.", ["ak-1481513222026"]),
 ("Qual o primeiro ramo da carótida interna no crânio?", "Oftálmica.", ["aci-ramos-org"]),
 ("Qual artéria irriga a face lateral?", "Cerebral média.", ["territorios-org"]),
 ("AVC de qual artéria pega o membro inferior?", "Cerebral anterior.", ["ak-1481562744652"]),
 ("O que liga as duas cerebrais anteriores?", "A comunicante anterior.", ["willis-org"]),
 ("Aneurisma de qual comunicante comprime o III?", "Posterior.", ["ak-1481772053364"]),
]
for _, _, ks in PT:
    assert all(k in KEYS for k in ks), ks
for i, (txt, ks) in EXP.items():
    assert len(txt) >= 300, (i, len(txt), txt[-60:]); assert all(k in KEYS for k in ks), (i, [k for k in ks if k not in KEYS])
nomes = [p.get("passo", p.get("nome")) for p in M["passos"]]
ordem = [i for i, b in enumerate(blocos) if b.get("papel") != "repeticao"]
M["revisao"] = {
 "momento": "E6/E7 retomada em 11/11, revisão do plano materializado (texto, Extra e figura de cada card) antes de instalar.",
 "passos": [{"passo": nomes[n], "explicacao_com_os_cards": EXP[i][0], "cards_usados": EXP[i][1]} for n, i in enumerate(ordem) if n < len(nomes)],
 "perguntas_teste": [{"pergunta": q, "resposta": a, "cards": ks} for q, a, ks in PT],
 "releitura_da_transcricao": (
  "Relidas as quatro transcrições (T1 diencéfalo, T2 telencéfalo, T3 irrigação, T4 prática) e a apostila-guia dos núcleos da base contra o deck. Conferido: limites do tálamo, hipotálamo e "
  "subtálamo pelo corte coronal; núcleos laterais do tálamo = motricidade e sensibilidade (o manuscrito dos veteranos dizia límbico; vale a aula); corpo estriado macroscópico = lentiforme + caudado, distinto do estriado funcional (caudado + putâmen); "
  "área de Broca nas partes triangular e opercular do hemisfério dominante. Acrescentados seis cards de fio da aula que nenhum acervo cobria (diencéfalo escondido, núcleo × gânglio, faces, giros × sulcos, sulco central único e como achá-lo).")}
(R / "mapa-de-profundidade.json").write_text(json.dumps(M, ensure_ascii=False, indent=1))
print("fidelidade", len(fid), "blocos;", sum(len(f["relacoes"]) for f in fid), "relações;", len(todos), "cards conferidos;", len(PT), "perguntas-teste")
