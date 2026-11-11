"""E6 (revisão com raciocínio no plano) e E7 (fidelidade aula ↔ cards) da 67."""
import json, re
plan = json.load(open("plan.json"))
ordem = {e["key"]: int(e["order"]) for e in plan["entries"]}
ordem.update({f"sh-{k}": v["order"] for k, v in plan["compartilhados"].items()})
REL = {
 (1, 2): [["k-malt", "sh-1791023357519", "sh-1791983685881"], ["k-tres-tarefas"], ["sh-1791147098269", "k-fumo", "sh-1791592724520"]],
 (3, 8): [["ex1701979294684-tonsilas"], ["sh-1790980914855", "sh-1790980914730"], ["sh-1791625425757"], ["k-iel-cd8"], ["k-nodulo-colon", "sh-1791023302370"]],
 (9, 10): [["k-iel-cd8"], ["k-infl-fisiologica"], ["k-infl-fisiologica"]],
 (11, 13): [["sh-1790980913229", "k-caliciforme", "sh-1791023297666"], ["k-microbiota", "sh-1791780601643", "ak1506179807216"], ["sh-1791000315902"], ["sh-1790980915172", "sh-1791780605649"], ["k-dc-mesenterico", "k-dc-dendritos"], ["k-homing", "k-alfa4beta7"], ["ak1497204171184", "sh-1791629598422"]],
 (14, 17): [["k-tres-tarefas", "sh-1791780602055", "k-tolerancia-oral"], ["k-ac-retinoico"], ["k-dc-il10-ido", "sh-1791625433083"], ["k-dc-proinfl", "k-dc-viral"]],
 (18, 19): [["k-prr-basolateral"], ["k-prr-basolateral"], ["k-prr-basolateral", "sh-1791780608272", "sh-1792240191394", "ak1521772146512"]],
 (20, 21): [["k-iga-neutraliza", "k-iga-aglutina", "sh-1792241813071", "sh-1792241812821"], ["sh-1791629594773"], ["sh-1791629596747", "sh-1791629596922"], ["sh-1791629597045"], ["sh-1790980915277"],
            ["sh-1791629596622", "sh-1791629597172", "sh-1791629597547", "ak1487121965148"], ["sh-1792241812572", "sh-1791629591820"]],
 (22, 27): [["k-reguladoras"], ["k-il10-colite"], ["k-treg-th17", "sh-1791625432907"], ["k-treg-th17", "sh-1791625432733"], ["sh-1791625422173", "sh-1791625422039"],
            ["k-balanco-treg", "sh-1791625432007"], ["k-higiene", "sh-1791780613803", "k-fases"], ["sh-1791625434757", "sh-1791625435233"], ["sh-1791625435657", "sh-1791983683185"], ["sh-1792242114021"], ["sh-1791780353019"]],
 (28, 29): [["k-olho"], ["k-olho"], ["k-olho", "sh-1791625430882"]],
}
NOTA = {
 (1, 2): "Lâmina 2 apresenta MALT, GALT e BALT; o deck abre com o organizador por local, a definição de MALT da aula 07 e o card que separa MALT constitutivo de folículo terciário. A capa (1) não tem card.",
 (3, 8): "Histologia do GALT na ordem das lâminas: tonsila (recorte do Histology com a figura da lâmina 3), Peyer no íleo e centro germinativo (figuras 4 e 6 no verso das cópias NEBLI), IEL e nódulo solitário do cólon com as figuras 7 e 8.",
 (9, 10): "O professor insiste que o infiltrado do intestino saudável parece inflamação crônica mas é fisiológico; o organizador contrasta isso com a chegada de neutrófilos na invasão, e o card dos IEL CD8 vem antes, como na lâmina 9.",
 (11, 13): "Barreiras (Paneth, caliciformes, microbiota), as duas vias de indução (célula M sobre Peyer e dendrítica até o linfonodo mesentérico, com o esquema da lâmina 13) e o retorno dos linfócitos ativados, que a lâmina 11 pergunta e a fala responde.",
 (14, 17): "Bloco que abre os mecanismos de tolerância: as três tarefas, a microbiota que treina tolerância, o ácido retinoico condicionando a dendrítica, IL-10/IDO com Treg induzida e a minoria de dendríticas pró-inflamatórias que permite responder.",
 (18, 19): "PRR fora da face apical: TLR basolateral e NLR citosólico (figura do Abbas da lâmina 19 sem legenda) e o macrófago da lâmina própria que mata o que penetra, fechando a ideia de que só a invasão provoca resposta.",
 (20, 21): "IgA na sequência da fala: anticorpo da mucosa que só neutraliza, troca por TGF-β, dímero com cadeia J, receptor poli-Ig, transcitose e componente secretor, e os plasmócitos de IgA da lâmina 21; os AnKing HY de IgA vêm juntos, todos já vivos em outras aulas.",
 (22, 27): "Células reguladoras (Treg, Th3, Tr1), IL-10 com a colite de quem não a produz, a IL-6 decidindo Th3 × Th17 com as figuras 25–26, citocinas e neutrófilos do Th17, efetores balanceados, Th2 e eosinófilos contra helmintos e a hipótese da higiene da fala.",
 (28, 29): "Olho imunoprivilegiado: organizador com córnea sem vasos, humor com TGF-β e epitélio com FasL e PD-L1, mais o card HY do FasL induzindo apoptose; a divisória (28) não tem card.",
}
c = json.load(open("compreensao-aula.json"))
blocos = []
todos = set()
for b in c["blocos"]:
    t = tuple(b["laminas"])
    rel = [{"aprender": a, "estado": "recuperavel", "cards": ks} for a, ks in zip(b["aprender"], REL[t])]
    assert len(rel) == len(b["aprender"]), (t, len(rel), len(b["aprender"]))
    conf = sorted({k for k, o in ordem.items() if t[0] <= o <= t[1]} | {k for r in rel for k in r["cards"]}, key=lambda k: ordem.get(k, 0))
    todos |= set(conf)
    blocos.append({"laminas": list(t), "bate": True, "nota": NOTA[t], "cards_conferidos": conf, "relacoes": rel})
assert set(ordem) <= todos, set(ordem) - todos
c["fidelidade"] = {"_como": "E7 sobre o plano e o despejo do plano (v14: antes de instalar)", "blocos": blocos,
 "conclusao": "O deck acompanha as 29 lâminas e a fala na ordem: GALT e histologia, inflamação fisiológica, indução e retorno, os quatro mecanismos de tolerância e a IL-6 trocando Treg por Th17, e o olho. Nenhum bloco é exemplo e nenhum card de doença ocupa o lugar de princípio; patógenos (poliovírus, Shigella, Giardia), deficiência de IgA e fármacos ficaram fora com motivo."}
json.dump(c, open("compreensao-aula.json", "w"), ensure_ascii=False, indent=1)
m = json.load(open("mapa-de-profundidade.json"))
m["revisao"] = {"passos": [
 {"passo": "MALT, GALT e BALT", "cards_usados": ["k-malt", "sh-1791023357519", "k-tres-tarefas"],
  "explicacao_com_os_cards": "As mucosas têm tecido linfoide próprio, o MALT, feito de nódulos e células livres da mucosa e da submucosa (sh-1791023357519). As placas de Peyer e os linfócitos da lâmina própria formam o GALT, e o tecido linfoide das vias aéreas é o BALT (k-malt). Esse sistema existe à parte porque o intestino precisa tolerar comida e bactérias comensais e ainda responder aos patógenos (k-tres-tarefas), o que um padrão sistêmico agressivo não faria."},
 {"passo": "Onde ficam os linfócitos da mucosa", "cards_usados": ["ex1701979294684-tonsilas", "sh-1790980914855", "sh-1791625425757", "k-iel-cd8", "k-nodulo-colon"],
  "explicacao_com_os_cards": "Na entrada da boca e do nariz ficam as tonsilas, massas linfoides que encontram os antígenos que entram (ex1701979294684-tonsilas). No íleo, as placas de Peyer são tecido linfoide sem cápsula na lâmina própria e submucosa (sh-1790980914855), com centros germinativos claros onde o B prolifera (sh-1791625425757); o cólon tem só nódulos solitários (k-nodulo-colon). Dentro do epitélio ficam linfócitos principalmente CD8, e abaixo dele a lâmina própria cheia de linfócitos e plasmócitos (k-iel-cd8)."},
 {"passo": "Inflamação fisiológica e o que muda na invasão", "cards_usados": ["k-infl-fisiologica", "k-iel-cd8", "k-tres-tarefas", ],
  "explicacao_com_os_cards": "A lâmina própria cheia de linfócitos, plasmócitos e macrófagos responde a comida e comensais sem lesar o tecido: é inflamação fisiológica (k-infl-fisiologica), porque o sistema imune do intestino tolera comida e bactérias comensais e ainda responde a patógenos (k-tres-tarefas),. Quando um patógeno invade, entram neutrófilos rapidamente (k-infl-fisiologica). Os linfócitos intraepiteliais CD8 fazem parte desse exército em alerta (k-iel-cd8)."},
 {"passo": "Barreiras, indução e retorno dos linfócitos", "cards_usados": ["sh-1790980913229", "k-caliciforme", "sh-1790980915172", "k-dc-mesenterico", "k-homing", "sh-1790980915277"],
  "explicacao_com_os_cards": "Antes da resposta imune, o muco das caliciformes afasta as bactérias do epitélio (k-caliciforme), as células de Paneth secretam defensinas (sh-1790980913229) e as comensais impedem a colonização por competição (k-microbiota). O antígeno entra por células M das placas de Peyer (sh-1790980915172), que o passam ao tecido linfoide abaixo, ou por dendríticas que levam o antígeno ao linfonodo mesentérico (k-dc-mesenterico). Os linfócitos ativados voltam à lâmina própria como efetores (k-homing), e o B do centro germinativo de Peyer vira plasmócito de IgA ali (sh-1790980915277)."},
 {"passo": "Dendrítica tolerogênica", "cards_usados": ["k-ac-retinoico", "k-dc-il10-ido", "k-dc-proinfl", "k-homing"],
  "explicacao_com_os_cards": "O ácido retinoico, derivado da vitamina A feito pelo epitélio e pela própria dendrítica, torna a dendrítica da mucosa tolerogênica (k-ac-retinoico). Ela secreta IL-10 e IDO, que tira triptofano dos T vizinhos, e favorece células T reguladoras (k-dc-il10-ido); o mesmo ácido retinoico imprime nos linfócitos o retorno ao intestino (k-homing). A maioria das dendríticas é tolerogênica, mas uma minoria é pró-inflamatória e inicia a defesa contra patógenos (k-dc-proinfl)."},
 {"passo": "PRR fora da superfície apical", "cards_usados": ["k-prr-basolateral", "k-caliciforme", "k-iga-neutraliza", "k-infl-fisiologica"],
  "explicacao_com_os_cards": "O epitélio intestinal guarda os TLR na membrana basolateral e os NLR no citosol, sem receptores na face apical (k-prr-basolateral). Assim, a bactéria que fica no lúmen, separada pelo muco das caliciformes (k-caliciforme) e neutralizada pela IgA (k-iga-neutraliza), não provoca resposta; só a que invade a célula ou chega à lâmina própria é reconhecida, e então chegam os neutrófilos da invasão (k-infl-fisiologica)."},
 {"passo": "IgA secretora", "cards_usados": ["k-iga-neutraliza", "sh-1792241813071", "sh-1791629594773", "sh-1791629591820", "sh-1791629596747", "sh-1791629596922", "sh-1791629597045", "sh-1790980915277"],
  "explicacao_com_os_cards": "A resposta humoral da mucosa é a IgA, que protege por neutralização, bloqueando adesão e toxinas sem complemento nem inflamação (k-iga-neutraliza, sh-1792241813071) e aglutina micróbios no muco, que saem nas fezes (k-iga-aglutina). O TGF-β abundante no intestino promove a troca para IgA (sh-1791629594773); os plasmócitos de IgA ficam na lâmina própria (sh-1790980915277) e secretam um dímero unido pela cadeia J (sh-1791629591820), que liga o receptor de imunoglobulina polimérica (sh-1791629596747) e atravessa a célula por transcitose (sh-1791629596922); no lúmen, parte do receptor fica como componente secretor e protege a IgA das proteases (sh-1791629597045)."},
 {"passo": "Células reguladoras e a troca Treg → Th17", "cards_usados": ["k-reguladoras", "sh-1791625434757", "k-il10-colite", "k-treg-th17", "sh-1791625432907", "sh-1791625432733", "sh-1792242114021", "sh-1791625422039", "k-balanco-treg"],
  "explicacao_com_os_cards": "A mucosa favorece Treg FoxP3+ induzidas, Th3 que fazem TGF-β e Tr1 que fazem IL-10 (k-reguladoras, sh-1791625434757); sem IL-10 a resposta aos comensais escapa e há colite (k-il10-colite). No TGF-β do intestino, sem IL-6 o CD4 vira Th3/Treg, e com IL-6 vira Th17 (k-treg-th17, sh-1791625432907, sh-1791625432733); a IL-6 vem de macrófagos ativados (sh-1792242114021) e o Th17 recruta neutrófilos (sh-1791625422039). Na invasão o MALT induz Th1 contra micróbios intracelulares ou Th2 contra helmintos (k-balanco-treg), e o Th2 recruta eosinófilos (sh-1791625432007)."},
 {"passo": "Olho imunoprivilegiado", "cards_usados": ["k-olho", "sh-1791625430882", "sh-1791983683185"],
  "explicacao_com_os_cards": "A câmara anterior do olho não pode ficar opaca, então limita a resposta imune: a córnea não tem vasos, o humor aquoso tem TGF-β e o epitélio expressa Fas ligand e PD-L1 (k-olho). O Fas ligand faz o linfócito que chega morrer por apoptose ao ligar o Fas, ativando a caspase-8 (sh-1791625430882), e o TGF-β também inibe a inflamação (sh-1791983683185). É a mesma ideia da mucosa, regulação própria do tecido, por outros meios."}],
 "perguntas_teste": [
  {"pergunta": "Onde ficam os linfócitos do GALT e como se chamam os agregados do íleo?", "cards": ["sh-1790980914855", "k-iel-cd8", "k-nodulo-colon"]},
  {"pergunta": "O que é MALT, GALT e BALT?", "cards": ["k-malt", "sh-1791023357519"]},
  {"pergunta": "Por que a lâmina própria cheia de células não é inflamação crônica?", "cards": ["k-infl-fisiologica", "k-tres-tarefas"]},
  {"pergunta": "O que aparece quando um patógeno invade a mucosa?", "cards": ["k-infl-fisiologica", "sh-1791625422039"]},
  {"pergunta": "Prova: como a IgA de mucosa é gerada a partir da infecção epitelial?", "cards": ["k-dc-mesenterico", "sh-1790980915172", "sh-1791629594773", "k-homing", "sh-1790980915277", "sh-1791629596747", "sh-1791629597045"]},
  {"pergunta": "Por que os linfócitos ativados na mucosa voltam a ela?", "cards": ["k-homing"]},
  {"pergunta": "O que torna a dendrítica da mucosa tolerogênica e o que ela produz?", "cards": ["k-ac-retinoico", "k-dc-il10-ido"]},
  {"pergunta": "Por que o epitélio não inflama com as bactérias do lúmen?", "cards": ["k-prr-basolateral", "k-infl-fisiologica"]},
  {"pergunta": "Prova: qual o papel da IgA secretora na contenção de vírus entéricos?", "cards": ["k-iga-neutraliza", "sh-1792241813071"]},
  {"pergunta": "Como a IgA chega ao lúmen e por que não é digerida?", "cards": ["sh-1791629596747", "sh-1791629596922", "sh-1791629597045"]},
  {"pergunta": "Que citocina troca a tolerância por defesa no intestino e qual célula resulta?", "cards": ["k-treg-th17", "sh-1791625432733"]},
  {"pergunta": "O que acontece com um animal que não produz IL-10?", "cards": ["k-il10-colite"]},
  {"pergunta": "Que células reguladoras a mucosa induz?", "cards": ["k-reguladoras"]},
  {"pergunta": "Que células do epitélio fazem muco e defensinas?", "cards": ["k-caliciforme", "sh-1790980913229"]},
  {"pergunta": "Como as comensais ajudam a proteger a mucosa?", "cards": ["k-microbiota"]},
  {"pergunta": "Onde ficam os plasmócitos de IgA e de onde vieram?", "cards": ["sh-1790980915277"]},
  {"pergunta": "Qual a forma da IgA no sangue e nas secreções?", "cards": ["sh-1792241812572", "sh-1791629591820"]},
  {"pergunta": "Que citocinas o Th17 faz e o que elas causam?", "cards": ["sh-1791625422173", "sh-1791625422039"]},
  {"pergunta": "Que resposta o MALT induz contra helmintos e qual célula ela recruta?", "cards": ["k-balanco-treg", "sh-1791625432007", "sh-1791780353019"]},
  {"pergunta": "Por que a falta de exposição microbiana aumentaria alergias?", "cards": ["k-higiene"]},
  {"pergunta": "Onde estão as tonsilas e o que fazem?", "cards": ["ex1701979294684-tonsilas"]},
  {"pergunta": "Como o olho evita inflamação na câmara anterior?", "cards": ["k-olho", "sh-1791625430882"]}],
 "releitura_da_transcricao": "10/11: reli a transcrição inteira (78 pp.) e as 29 lâminas conferindo cada fala com o plano: GALT/BALT, tonsila, Peyer e centro claro, IEL CD8 αβ/γδ, inflamação fisiológica × PMN, Paneth, caliciformes e microbiota, célula M e dendrítica até o linfonodo mesentérico, retorno dos linfócitos, dendrítica soft com ácido retinoico/IL-10/IDO, PRR basolateral, IgA (Fc inócua, TGF-β, pIgR, peça secretória, plasmócitos), Treg/Th3/Tr1, IL-10 knockout, IL-6 e Th17, Th1/Th2, hipótese da higiene e olho. Acrescentei o MALT constitutivo, o macrófago que mata o que penetra e os AnKing de IL-6, TGF-β, IL-10 e eosinófilo; o desenvolvimento neonatal ficou fora (fala sem lâmina e sem objetivo cobrado)."}
json.dump(m, open("mapa-de-profundidade.json", "w"), ensure_ascii=False, indent=1)
print("ok", len(todos))
