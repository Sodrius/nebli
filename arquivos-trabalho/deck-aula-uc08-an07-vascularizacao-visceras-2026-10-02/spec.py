# Especificação curada — Irrigação visceral abdominal (UC08 P1, Anatomia, Profa. Patricia Castelucci; PDF de 25 páginas, 2 lâminas por página, 49 lâminas).
# Feita em 02/10/2026 a partir de planejamento.json (escrito antes). Ordem = páginas do PDF ("Slide N" = página N).
import json
from pathlib import Path
HERE = Path(__file__).parent
RUN_ID = "uc08-an07-20261002a"
SHORT = "an07"
LESSON = "2026-uc08-anatomia-07-vascularizacao-visceras"
DECK = "NEBLI::UC08::P1::Anatomia::Vascularização das vísceras"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261002-CLAUDE-12) + PLANO-GERACAO-ANO, 02/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt, 20 consultas em 02/10); Referências Externas "
         "(Dorian, AnatoKing, BlueLink, MCAT; Dope só para registro) pelos mesmos alvos (busca/ext.txt, 6 consultas): ")
CLIP = {"t": (60, 60, 480, 372), "b": (60, 405, 480, 725)}
_prev = {}
for _run in ("deck-aula-uc08-an01-esofago-estomago-delgado-2026-10-02", "deck-aula-uc08-an02-intestino-grosso-canal-anal-2026-10-02"):
    _prev.update({n["key"]: n["nid"] for n in json.loads((HERE.parent / _run / "receipt.json").read_text())["notes"]})


def ak(key, src, flags, bloco, alvo, slide, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def io(key, page, half, name, cor, bloco, alvo, motivo, lines=(), search=(), mask_rects=(), rects=()):
    return dict(key=key, kind="slideio", page=page, half="full", clip=CLIP[half], tag=f"p{page:02d}{half}", title_size=14, lines=list(lines), search=list(search),
                rects=list(rects), mask_rects=list(mask_rects), name=name, remarks="", aponta="estrutura", flags={1: cor}, bloco=bloco, alvo=alvo,
                evid=f"Slide {page}", motivo=motivo)


def sh(key, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{_prev[key]}", kind="compartilhado", nid=_prev[key], cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_ = "A-tronco-celiaco", "B-veias-e-linfa", "C-mesenterica-superior", "D-mesenterica-inferior", "E-reto"
PR = "Azul: item do roteiro e das questões (identificar), na prancha da aula."
PC = "Azul: item do roteiro, na peça de cadáver da aula."
LN = "Rosa: linfonodo rotulado no slide, prioridade baixa."
CARDS = [
 # ---------- A. Três ramos da aorta e tronco celíaco (slides 2–7) ----------
 io("io-tronco-celiaco-aorta", 2, "b", "Celiac trunk (T12)", V, A_, "Tronco celíaco na aorta", "Verde: primeiro objetivo da aula.", ["Tronco celíaco", "(T12)"]),
 io("io-ams-aorta", 2, "b", "Superior mesenteric artery (T12/L1)", V, A_, "Mesentérica superior na aorta", "Verde: segundo objetivo da aula.", search=["Superior", "(T12/L1)"]),
 io("io-ami-aorta", 2, "b", "Inferior mesenteric artery (L3)", V, A_, "Mesentérica inferior na aorta", "Verde: terceiro objetivo da aula.", search=["Inferior", "(L3)"]),
 ak("celiaco-nivel", 1486766393958, {1: Z}, A_, "Nível do tronco celíaco", 2, "Azul: nível escrito no slide (tag 4)."),
 ak("celiaco-foregut", 1486767159823, {1: V}, A_, "Tronco celíaco irriga o intestino anterior", 2, "Verde: HY (1)."),
 ak("celiaco-tres-ramos", 1486767263733, {1: V, 2: V, 3: V}, A_, "Três ramos do tronco celíaco", 3, "Verdes: HY (1); questão 1."),
 io("io-gastrica-esquerda", 3, "t", "Left gastric artery", Z, A_, "A. gástrica esquerda", PR, ["1. a. Gástrica esquerda"]),
 io("io-esplenica", 3, "t", "Splenic artery", Z, A_, "A. esplênica", PR, ["2 a. esplênica"]),
 io("io-hepatica-comum", 3, "t", "Common hepatic artery", Z, A_, "A. hepática comum", PR, ["3 a. Hepática comum"]),
 io("io-hepatica-propria", 3, "t", "Proper hepatic artery", Z, A_, "A. hepática própria", PR, ["a. Hepática própria"]),
 io("io-gastroduodenal", 3, "t", "Gastroduodenal artery", Z, A_, "A. gastroduodenal", PR, ["a. gastroduodenal"]),
 io("io-gastrica-direita", 3, "t", "Right gastric artery", Z, A_, "A. gástrica direita", PR, ["4. a. Gástrica", "direita"]),
 ak("gastrica-esq-esofago", 1486767268255, {1: V}, A_, "Gástrica esquerda dá ramos esofágicos", 3, "Verde: HY (1)."),
 ak("hepatica-comum-ramos", 1486767276770, {1: V, 2: V}, A_, "Hepática comum: própria e gastroduodenal", 3, "Verdes: HY (1)."),
 ak("propria-gastrica-direita", 1486767287058, {1: V, 2: Z}, A_, "Hepática própria dá a gástrica direita", 3, "c1 verde: HY (1); c2 azul."),
 ak("gastricas-anastomose", 1486767352903, {1: V}, A_, "Anastomose entre as gástricas", 3, "Verde: HY (1)."),
 ak("curvatura-menor-gastricas", 1486767367274, {1: V}, A_, "Curvatura menor: artérias gástricas", 3, "Verde: HY (1); 'descrever a irrigação do estômago' é objetivo."),
 ak("ulcera-gastrica-esquerda", 1482276034749, {1: V}, A_, "Úlcera da curvatura menor sangra da gástrica esquerda", 3, "Verde: HY (2), clínica de encaixe direto com a artéria."),
 io("io-gastricas-curtas", 4, "t", "Short gastric arteries", Z, A_, "Aa. gástricas curtas", PR, ["a. gástricas", "curtas"]),
 io("io-pd-antero-superior", 4, "t", "Anterior superior pancreaticoduodenal artery", Z, A_, "A. pancreaticoduodenal anterossuperior", "Azul: questão 9.", search=["ântero superior"]),
 io("io-pd-postero-superior", 4, "t", "Posterior superior pancreaticoduodenal artery", R, A_, "A. pancreaticoduodenal posterossuperior", "Rosa: par da anterior.", search=["póstero superior"]),
 ak("esplenica-ramos", 1486767314237, {1: V, 2: V, 3: Z}, A_, "Esplênica dá gastromental esquerda e gástricas curtas", 4, "c1 e c2 verdes: HY (1); c3 azul."),
 ak("gastricas-curtas-fundo", 1486767395683, {1: V}, A_, "Gástricas curtas irrigam o fundo", 4, "Verde: HY (2)."),
 ak("gastroduodenal-pd", 1486767304293, {1: V}, A_, "Gastroduodenal dá as pancreaticoduodenais superiores", 4, "Verde: HY (1)."),
 io("io-peca-tronco-celiaco", 5, "t", "Celiac trunk", V, A_, "Tronco celíaco na peça", "Verde: roteiro prático (item 11), peça da aula.", ["Tronco", "celíaco"]),
 io("io-peca-esplenica", 5, "t", "Splenic artery", Z, A_, "A. esplênica na peça", PC, ["a. esplênica"]),
 io("io-peca-gastroduodenal", 5, "t", "Gastroduodenal artery", Z, A_, "A. gastroduodenal na peça", PC, ["a. gastroduodenal"]),
 io("io-peca-hepatica-propria", 5, "t", "Proper hepatic artery", Z, A_, "A. hepática própria na peça", PC, search=["própria"]),
 io("io-peca-hepatica-comum", 5, "t", "Common hepatic artery", Z, A_, "A. hepática comum na peça", PC, search=["comum"]),
 io("io-peca-gastrica-esquerda", 5, "t", "Left gastric artery", Z, A_, "A. gástrica esquerda na peça", PC, search=["gástrica", "esquerda"]),
 io("io-peca-pd-superior", 5, "b", "Superior pancreaticoduodenal artery", R, A_, "A. pancreaticoduodenal superior na peça", "Rosa: segunda peça.", ["a. Pancreático duodenal superior"]),
 io("io-pd-postero-inferior", 6, "t", "Posterior inferior pancreaticoduodenal artery (from the superior mesenteric artery)", Z, A_, "Pancreaticoduodenal posteroinferior",
    "Azul: questão 10; anastomose entre tronco celíaco e mesentérica superior.", ["a. Pancreático duodenal", "póstero inferior", "(origem da a. mesentérica superior)"]),
 io("io-gastromental-direita", 6, "b", "Right gastro-omental (gastroepiploic) artery", Z, A_, "A. gastromental direita", PR, ["a. gastromental", "direita"]),
 io("io-gastromental-esquerda", 6, "b", "Left gastro-omental (gastroepiploic) artery", Z, A_, "A. gastromental esquerda", PR, ["a. Gastromental", "Esquerda"]),
 ak("gastroduodenal-gastromental", 1486767295417, {1: V, 2: Z}, A_, "Gastroduodenal dá a gastromental direita", 6, "c1 verde: HY (1); c2 azul."),
 ak("gastromentais-anastomose", 1486767349883, {1: V}, A_, "Anastomose entre as gastromentais", 6, "Verde: HY (1); roteiro ('anastomosa-se com a gastromental direita')."),
 ak("curvatura-maior-gastromentais", 1486767364212, {1: V}, A_, "Curvatura maior: gastromentais", 6, "Verde: HY (2)."),
 io("io-peca-gastromental-direita", 7, "t", "Right gastro-omental artery", R, A_, "Gastromental direita na peça", "Rosa: segunda identificação.", search=["Gastromental", "direita"]),
 # ---------- B. Drenagem venosa e linfática do estômago; sistema porta e linfático (slides 7–10) ----------
 io("io-v-gastrica-esquerda", 7, "b", "Left gastric vein", Z, B_, "V. gástrica esquerda", "Azul: tributária da porta rotulada no slide.", ["v. Gástrica esquerda"]),
 io("io-v-porta", 7, "b", "Hepatic portal vein", V, B_, "V. porta", "Verde: vaso central da drenagem do tubo digestório.", ["v. porta"]),
 ak("varizes-esofagicas", 1486770898373, {1: V, 2: Z}, B_, "Varizes esofágicas: gástrica esquerda × ázigo", 7, "c1 verde: HY (1), clínica de encaixe com a v. gástrica esquerda; c2 azul."),
 io("io-v-esplenica", 8, "t", "Splenic vein", Z, B_, "V. esplênica", PR, ["v. esplênica"]),
 io("io-v-mesenterica-superior", 8, "t", "Superior mesenteric vein", Z, B_, "V. mesentérica superior", PR, ["v. Mesentérica superior"]),
 io("io-v-mesenterica-inferior", 8, "t", "Inferior mesenteric vein", Z, B_, "V. mesentérica inferior", PR, ["v. Mesentérica inferior"]),
 dict(key="porta-formacao", kind="text", src=1527683179954, origin="Dorian", flags={1: V, 2: Z}, bloco=B_,
      text="The {{c1::<b>splenic vein</b>}} joins the {{c1::<b>superior mesenteric vein</b>}} to form the portal vein behind the {{c2::<b>neck</b>}} of the pancreas",
      extra="", alvo="Formação da veia porta", evid="Slide 8", motivo="c1 verde: formação da porta, base de toda a hepatologia; c2 azul."),
 au("vmi-esplenica", "The <b>inferior mesenteric vein</b> usually drains into the {{c1::<b>splenic</b>}} vein", {1: Z}, B_, "V. mesentérica inferior drena na esplênica",
    "8; Moore p. 753", "prova", "AnKing só cita no Extra da drenagem do reto.", [1486771346144, 1486767287058], "Azul: trajeto mostrado no slide 8."),
 au("porta-territorio", "The <b>portal system</b> drains the digestive tract from the lower esophagus to the upper {{c1::<b>anal canal</b>}}, plus the spleen, pancreas and gallbladder", {1: Z}, B_,
    "Território do sistema porta", "8; roteiro prático, item 5", "prova", "nenhum card nos acervos com o território.", [1486767243259, 1486767254523], "Azul: frase do roteiro."),
 io("io-cisterna", 9, "t", "Cisterna chyli", Z, B_, "Cisterna do quilo", "Azul: rótulo do slide 9.", ["Cisterna", "do quilo"]),
 io("io-ducto-toracico", 9, "t", "Thoracic duct", Z, B_, "Ducto torácico", "Azul: rótulo do slide 9.", ["Ducto torácico", "L2 e L3"]),
 au("cisterna-troncos", "The <b>cisterna chyli</b> receives the intestinal trunk and the two {{c1::<b>lumbar</b>}} trunks and continues as the thoracic duct", {1: V}, B_,
    "Cisterna do quilo: três troncos, origem do ducto torácico", "9; Moore; texto do slide", "central", "AnKing só tem o ducto torácico no hiato aórtico e nos quilomícrons.",
    [1474511944771, 1486767263733], "Verde: definição escrita no slide 9, base da drenagem linfática do abdome.", duplicacao_ok="cobra os troncos que formam a cisterna; as oclusões só identificam"),
 ak("ducto-quilomicrons", 1475966591010, {1: Z}, B_, "Ducto torácico leva a linfa ao sangue", 9, "Azul: 'transporta linfa e quilo até a junção subclávia–jugular' (tag 3)."),
 io("io-ln-celiacos", 10, "t", "Celiac lymph nodes", Z, B_, "Linfonodos celíacos", "Azul: destino da linfa do estômago.", search=["celíacos"]),
 io("io-ln-gastricos", 10, "t", "Left gastric lymph nodes", R, B_, "Linfonodos gástricos esquerdos", LN, search=["Gástricos", "esquerdos"]),
 io("io-ln-esplenicos", 10, "t", "Splenic lymph nodes", R, B_, "Linfonodos esplênicos", LN, search=["esplênicos"]),
 ak("ln-celiacos-estomago", 1486945231564, {1: V}, B_, "Linfonodos celíacos drenam estômago, baço, fígado e pâncreas", 10, "Verde: HY (1)."),
 ak("ln-celiacos-duodeno", 1486945235222, {1: V}, B_, "Linfonodos celíacos drenam o duodeno proximal", 10, "Verde: HY (1)."),
 # ---------- C. Artéria mesentérica superior (slides 11–17) ----------
 ak("ams-nivel", 1486767143966, {1: Z}, C_, "Nível da mesentérica superior", 11, "Azul: nível escrito no slide (tag 4)."),
 ak("ams-midgut", 1486767163689, {1: V}, C_, "Mesentérica superior irriga o intestino médio", 11, "Verde: HY (1)."),
 io("io-ams", 11, "b", "Superior mesenteric artery", Z, C_, "A. mesentérica superior", PR, ["a. Mesentérica superior"]),
 io("io-vms", 11, "b", "Superior mesenteric vein", Z, C_, "V. mesentérica superior ao lado da artéria", PR, ["v. Mesentérica superior"]),
 io("io-pd-antero-inferior", 11, "b", "Anterior inferior pancreaticoduodenal artery", R, C_, "Pancreaticoduodenal anteroinferior", "Rosa: par da posteroinferior.", search=["ântero inferior"]),
 au("pd-inferior-ams", "The <b>inferior pancreaticoduodenal</b> artery is the first branch of the {{c1::<b>superior mesenteric</b>}} artery", {1: Z}, C_,
    "Pancreaticoduodenal inferior é o 1º ramo da mesentérica superior", "11; Moore p. 733", "prova", "AnKing só tem as superiores (gastroduodenal); Dope 1461962581720 evitado.",
    [1486767304293, 1486767295417], "Azul: título do slide 'a. mesentérica superior, 1º ramo'.", extra="- It anastomoses with the superior pancreaticoduodenal arteries (celiac trunk)"),
 ak("ln-duodeno-distal", 1486945239368, {1: V}, C_, "Linfonodos mesentéricos superiores drenam o duodeno distal", 11, "Verde: HY (1)."),
 io("io-colica-direita", 12, "t", "Right colic artery", Z, C_, "A. cólica direita", PR, ["a. Cólica", "direita"]),
 io("io-ileocolica", 12, "t", "Ileocolic artery", Z, C_, "A. ileocólica", PR, ["a. ileocólica"]),
 io("io-jejunais", 12, "t", "Jejunal arteries", Z, C_, "Aa. jejunais", PR, ["a. jejunais"]),
 io("io-ileais", 12, "t", "Ileal arteries", Z, C_, "Aa. ileais", PR, ["a. ileais"]),
 au("ileocolica-territorio", "The {{c1::<b>ileocolic</b>}} artery supplies the terminal ileum, the cecum and, through its appendicular branch, the appendix", {1: V}, C_,
    "Território da ileocólica", "12; roteiro prático, item 13; Moore p. 743", "central", "AnatoKing só identifica; AnKing sem card.", [1486767395683, 1486767268255],
    "Verde: ramo com território de maior peso clínico (apêndice).", duplicacao_ok="cobra o território; a oclusão só identifica o vaso"),
 au("colica-direita-territorio", "Which branch of the <b>superior mesenteric artery</b> supplies the ascending colon?<br><br>{{c1::Right colic artery}}", {1: Z}, C_,
    "Cólica direita irriga o colo ascendente", "12; roteiro prático, item 13", "prova", "AnatoKing só identifica.", [1486771343412, 1486771372707], "Azul: território do roteiro.",
    duplicacao_ok="cobra o território; a oclusão só identifica o vaso"),
 au("colica-media-territorio", "The <b>middle colic</b> artery, a branch of the superior mesenteric artery, supplies the {{c1::<b>transverse</b>}} colon", {1: Z}, C_,
    "Cólica média irriga o colo transverso", "13; roteiro prático, item 13", "prova", "AnKing só cita a cólica média no Extra da flexura esplênica.", [1486767395683, 1486767364212],
    "Azul: território do roteiro."),
 sh("vasos-retos-jejuno", "verde", C_, "Vasos retos longos no jejuno, curtos no íleo", 13, "Já vivo na AN01; o slide 13 repete as peças."),
 io("io-vv-ileocolica", 14, "t", "Ileocolic vein", R, C_, "V. ileocólica", "Rosa: tributária rotulada.", ["vv. ileocólica"]),
 io("io-ln-mesenterico-superior", 14, "b", "Superior mesenteric lymph nodes", Z, C_, "Linfonodos mesentéricos superiores", "Azul: um dos três grupos pré-aórticos.", search=["superior"]),
 io("io-ln-mesenterico-inferior", 14, "b", "Inferior mesenteric lymph nodes", Z, C_, "Linfonodos mesentéricos inferiores", "Azul: um dos três grupos pré-aórticos.", search=["inferior"]),
 au("ln-pre-aorticos", "The pre-aortic lymph nodes lie in three groups around the celiac, superior mesenteric and {{c1::<b>inferior mesenteric</b>}} arteries", {1: Z}, C_,
    "Três grupos de linfonodos pré-aórticos", "14", "prova", "AnKing cobra o território de cada grupo, não a organização.", [1486767263733, 1486945231564],
    "Azul: 'três grupos de linfonodos situam-se em três troncos de irrigação'."),
 ak("ln-jejuno-ileo", 1486945243332, {1: V}, C_, "Linfonodos mesentéricos superiores drenam jejuno e íleo", 15, "Verde: HY (1); slide 15 'drenagem linfática do jejuno e íleo'."),
 # 03/10 (F-20261003-CLAUDE-13): o alvo era a legenda sobre a foto e a figura da esquerda mostrava o nome; agora o alvo é o
 # rótulo da figura (seta para o tronco) e os demais rótulos impressos na figura ficam cobertos.
 io("io-tronco-intestinal", 15, "b", "Intestinal lymphatic trunk", R, C_, "Tronco intestinal", LN, rects=[(113, 535, 145, 561)],
    mask_rects=[(104, 505, 158, 516), (280, 561, 319, 584), (280, 609, 323, 627), (108, 630, 143, 647)]),
 ak("isquemia-aguda-ams", 1482289647560, {1: V, 2: Z}, C_, "Isquemia mesentérica aguda: oclusão da mesentérica superior", 16, "c1 verde: HY (1), caso clínico dos slides 16–17; c2 azul."),
 ak("embolia-ams", 1556932244893, {1: Z}, C_, "Êmbolo costuma parar na mesentérica superior", 17, "Azul: slide 'oclusão da a. mesentérica superior'."),
 sh("sindrome-ams", "rosa", C_, "3ª porção do duodeno entre a mesentérica superior e a aorta", 17, "Já vivo na AN01; relação mostrada no slide 12 (localização da AMS)."),
 # ---------- D. Artéria mesentérica inferior (slides 18–21) ----------
 ak("ami-nivel", 1486767150807, {1: Z}, D_, "Nível da mesentérica inferior", 18, "Azul: nível (o slide 2 diz L3 e o 18 diz L4; AnKing e Moore dizem L3)."),
 ak("ami-hindgut", 1486767179344, {1: V}, D_, "Mesentérica inferior irriga o intestino posterior", 18, "Verde: HY (1)."),
 io("io-colica-esquerda", 18, "t", "Left colic artery", Z, D_, "A. cólica esquerda", PR, ["a. cólica esquerda"]),
 io("io-sigmoideas", 18, "t", "Sigmoid arteries", Z, D_, "Aa. sigmóideas", PR, ["a. sigmoídeas"]),
 io("io-retal-superior", 18, "t", "Superior rectal artery", Z, D_, "A. retal superior", PR, ["a. Retal superior"]),
 au("ami-ramos", "The three branches of the <b>inferior mesenteric artery</b> are the left colic, the {{c1::<b>sigmoid</b>}} and the superior rectal arteries", {1: V}, D_,
    "Ramos da mesentérica inferior", "18; questão 3; caso do slide 23", "central", "AnKing tem os ramos do tronco celíaco, não os da mesentérica inferior.", [1486767263733, 1486767276770],
    "Verde: 'cite os ramos da a. mesentérica inferior' é a pergunta do caso clínico.", duplicacao_ok="cobra a lista de ramos; a oclusão só identifica as sigmóideas"),
 au("colica-esquerda-territorio", "Which branch of the <b>inferior mesenteric artery</b> supplies the descending colon?<br><br>{{c1::Left colic artery}}", {1: Z}, D_,
    "Cólica esquerda irriga o colo descendente", "18; roteiro prático, item 14", "prova", "AnatoKing só identifica.", [1486771343412, 1486771372707], "Azul: território do roteiro.",
    duplicacao_ok="cobra o território; a oclusão só identifica o vaso"),
 ak("retal-superior-ami", 1486771346144, {1: V}, D_, "Retal superior é ramo da mesentérica inferior", 18, "Verde: HY (2); 'continuação da a. mesentérica inferior' no roteiro."),
 io("io-peca-marginal", 20, "t", "Marginal artery (juxtacolic arcade)", V, D_, "A. marginal na peça", "Verde: roteiro (arco justacólico), peça da aula.", ["A. marginal", "(Arco justaposto)"]),
 io("io-peca-ami", 20, "t", "Inferior mesenteric artery", Z, D_, "A. mesentérica inferior na peça", PC, ["a. Mesentérica inferior"]),
 io("io-peca-sigmoideas", 20, "t", "Sigmoid arteries", R, D_, "Aa. sigmóideas na peça", "Rosa: segunda identificação.", ["a. sigmóideas"]),
 au("marginal", "The anastomotic channel that runs along the mesenteric border of the colon, linking the colic arteries, is the {{c1::<b>marginal artery</b>}}", {1: V}, D_,
    "Artéria marginal (arco justacólico)", "20; roteiro prático, item 13; Moore p. 750", "central", "Dorian cita a marginal dentro de uma resposta composta; AnKing só no Extra.",
    [1486767349883, 1486767352903], "Verde: circulação colateral entre as duas mesentéricas.", duplicacao_ok="cobra a definição; a oclusão reconhece na peça"),
 ak("flexura-esplenica-watershed", 1482886714520, {1: V, 2: V}, D_, "Flexura esplênica: zona limítrofe entre as mesentéricas", 20, "Verdes: HY (1)."),
 ak("sudeck", 1520726446562, {1: V, 2: Z}, D_, "Ponto de Sudeck", 20, "c1 verde: HY (1); c2 azul."),
 io("io-v-retal-superior", 21, "t", "Superior rectal vein", R, D_, "V. retal superior", "Rosa: tributária rotulada.", ["v. Retal superior"]),
 io("io-vmi", 21, "t", "Inferior mesenteric vein", Z, D_, "V. mesentérica inferior", PR, ["v. Mesentérica inferior"]),
 ak("ln-colo-proximal", 1486945247167, {1: V}, D_, "Linfonodos mesentéricos superiores drenam o colo proximal", 21, "Verde: HY (1)."),
 ak("ln-colo-distal", 1486945252224, {1: V}, D_, "Linfonodos mesentéricos inferiores drenam o colo distal", 21, "Verde: HY (1)."),
 io("io-ln-colicos-medios", 21, "b", "Middle colic lymph nodes", R, D_, "Linfonodos cólicos médios", LN, search=["Cólicos médios"]),
 io("io-ln-ileocolicos", 21, "b", "Ileocolic lymph nodes", R, D_, "Linfonodos ileocólicos", LN, search=["íleocólicos"]),
 # ---------- E. Reto (slides 22–23) ----------
 io("io-reto-a-superior", 22, "t", "Superior rectal artery (from the inferior mesenteric artery)", Z, E_, "A. retal superior", PR, search=["retal superior"]),
 io("io-reto-a-media", 22, "t", "Middle rectal artery (from the internal iliac artery)", Z, E_, "A. retal média", "Azul: questão 6.", search=["retal media"]),
 io("io-reto-a-inferior", 22, "t", "Inferior rectal artery (from the internal pudendal artery)", Z, E_, "A. retal inferior", "Azul: questão 6.", search=["retal inferior"]),
 sh("arteria-acima", "verde", E_, "A. retal superior acima da linha pectinada", 22, "Já vivo na AN02."),
 au("retal-media", "The <b>middle rectal</b> artery is a branch of the {{c1::<b>internal iliac</b>}} artery", {1: Z}, E_, "Retal média é ramo da ilíaca interna",
    "22; questão 6; Moore p. 923", "prova", "AnKing tem a origem da retal superior e da inferior, não da média.", [1486771346144, 1486771374861], "Azul: completa as três origens do slide 22."),
 ak("retal-inferior-pudenda", 1486771374861, {1: V}, E_, "Retal inferior é ramo da pudenda interna", 22, "Verde: HY (2)."),
 sh("arteria-abaixo", "verde", E_, "A. retal inferior abaixo da linha pectinada", 22, "Já vivo na AN02."),
 io("io-reto-v-superior", 22, "b", "Superior rectal vein (to the inferior mesenteric vein, portal system)", Z, E_, "V. retal superior", "Azul: questão 8 (origens das veias).",
    search=["v. retal superior"]),
 io("io-reto-v-media", 22, "b", "Middle rectal vein (to the internal iliac vein, systemic)", Z, E_, "V. retal média", "Azul: questão 8.", search=["v. retal media"]),
 io("io-reto-v-inferior", 22, "b", "Inferior rectal vein (to the internal pudendal vein, systemic)", Z, E_, "V. retal inferior", "Azul: questão 8.", search=["v. retal inferior"]),
 sh("veia-acima", "verde", E_, "Acima da linha pectinada: drenagem portal", 22, "Já vivo na AN02."),
 sh("veia-abaixo", "verde", E_, "Abaixo da linha pectinada: drenagem sistêmica", 22, "Já vivo na AN02."),
 ak("varizes-anorretais", 1486771299461, {1: V, 2: Z}, E_, "Varizes anorretais: retal superior × média e inferior", 22, "c1 verde: HY (1), anastomose portossistêmica das veias do slide 22 (questão 8); c2 azul."),
 sh("hemorroida-plexo", "verde", E_, "Hemorroida: distensão do plexo anal", 22, "Já vivo na AN02; a questão 8 trata da doença hemorroidária."),
 sh("linfa-acima", "verde", E_, "Acima da linha pectinada: linfonodos ilíacos internos", 23, "Já vivo na AN02."),
 io("io-ln-retais-superiores", 23, "t", "Superior rectal lymph nodes", R, E_, "Linfonodos retais superiores", LN, search=["Retais superiores"]),
 au("reto-linfa", "Lymph from the upper <b>rectum</b> follows the superior rectal vessels to the {{c1::<b>inferior mesenteric</b>}} lymph nodes", {1: Z}, E_,
    "Linfa do reto superior vai aos linfonodos mesentéricos inferiores", "23; questão 6", "prova", "AnKing cobre do colo ao reto superior num card só; aqui o trajeto do reto.",
    [1486945252224, 1486771351448], "Azul: slide 'drenagem linfática do reto'.", duplicacao_ok="mesma resposta do card AnKing do colo distal, pergunta diferente: aqui é o reto superior"),
]

EXCLUIDOS = [
 (1349477488376, "Prancha Dope do tronco celíaco: Dope só sem alternativa; oclusões do slide e da peça cobrem"), (1349477488369, "Prancha Dope das mesentéricas: idem"),
 (1349477488443, "Prancha Dope da veia porta: idem"), (1461962581720, "Dope texto pancreaticoduodenal inferior: trocado por autoral"),
 (1486767333068, "AnKing ID gástrica esquerda (esquema Physeo): oclusão do slide preferida"), (1486767327881, "AnKing ID esplênica: idem"), (1486767337959, "AnKing ID hepática comum: idem"),
 (1486767341284, "AnKing ID gastroduodenal: idem"), (1486767323251, "AnKing ID gastromental esquerda: idem"), (1486767330571, "AnKing ID gastromental direita: idem"),
 (1486605743531, "Ligamento gastro-hepático contém as gástricas: AN13"), (1486605766963, "Ligamento gastrocólico: AN13"), (1486605777827, "Ligamento gastroesplênico: AN13"),
 (1486605794937, "Ligamento esplenorrenal: AN13"), (1486605719941, "Tríade portal no ligamento hepatoduodenal: AN11/AN13"), (1486775502282, "Tríade portal: AN11"),
 (1486767243259, "Intestino anterior (derivados): embriologia"), (1486767185215, "Nível da a. renal: fora da aula"), (1482971271910, "Baço e intestino anterior: embriologia"),
 (1471812052582, "Isquemia mesentérica crônica: doença além do caso"), (1482289661873, "Isquemia mesentérica crônica: idem"), (1482886719758, "Colite isquêmica (quadro clínico): clínica"),
 (1527680535803, "Dorian necrose da flexura esplênica: redundante com AnKing 1482886714520"), (1527679709579, "Dorian ramos da hepática comum: redundante com AnKing"),
 (1486767235675, "Síndrome da AMS (sintoma): clínica"), (1486767238872, "Síndrome da AMS (gordura): clínica"), (1482276186550, "Nódulo de Virchow: oncologia"),
 (1482115579210, "Quilomícrons e ducto torácico: redundante com 1475966591010"), (1486945272965, "Linfonodos para-aórticos e rim: fora da aula"),
 (1541722661543, "AnatoKing v. mesentérica superior: oclusão do slide preferida"), (1546961824889, "AnatoKing cólica direita: idem"), (1546961947335, "AnatoKing retal superior: idem"),
]
FORA_DO_RECORTE = [
 "Características gerais do sistema linfático (slides 8–9, caixas de texto): UC02; só a cisterna do quilo e o ducto torácico entram",
 "Isquemia e reperfusão, estrangulamento (slide 17): fisiopatologia; só a oclusão arterial entra",
 "Esquemas do Prometheus e do Dângelo com rótulos dentro da figura (slides 3, 4, 12, 13, 19): estruturas cobertas pelas pranchas e peças",
 "Ligamentos e omentos por onde os vasos correm: AN13",
 "Linfonodos regionais menores (gastromentais, pancreáticos, cólicos direitos e esquerdos, retais médios e inferiores, aórticos lombares): rótulos de baixa prioridade, cobertos por amostra rosa",
]

# F-20261003-CLAUDE-15: figura de livro/AnKing e explicação curta no verso
from nebli.ilustrar import ilustrar, anotar
from imagens import IMAGENS, SEM_IMAGEM, LIVRO
from notas import NOTAS
MEDIA.update(LIVRO)
CARDS = anotar(ilustrar(CARDS, IMAGENS, SEM_IMAGEM), NOTAS)
