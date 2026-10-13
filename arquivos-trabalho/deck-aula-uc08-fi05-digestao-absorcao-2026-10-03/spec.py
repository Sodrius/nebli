# Especificação curada — Digestão e absorção dos nutrientes (UC08 P2, Fisiologia, Fran Goulart, Aula-3_MED_2026.pdf, 12 lâminas).
# Refeita do zero em 02/10/2026 (piloto do pipeline; o deck de 29/09 foi apagado por Davi). Ordem = sequência dos slides.
import json
from pathlib import Path
HERE = Path(__file__).parent
RUN_ID = "uc08-fi05-20261003a"
SHORT = "fi05"
LESSON = "2026-uc08-fisiologia-05-digestao-absorcao-nutrientes"
DECK = "NEBLI::UC08::P2::Fisiologia::Digestão e absorção dos nutrientes"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261003-CLAUDE-13) + PLANO-GERACAO-ANO, refeita 03/10/2026"

_S = [2, 4, 5, 6, 7, 9, 10, 11, 12]
MEDIA = {f"nebli-uc08-fi05-s{n:02d}.png": f"fontes/s{n:02d}.png" for n in _S}
AK_IMG = {"amido": "4a8ba294e04f55662e07c7bfb3f43ed7.png", "sglt": "28f38c4892f40525fdb651ffa8badb2d.png",
          "peptideos": "1dfde8c3299bf92dd21fa42834c4cc5a.jpg", "lipidios": "341242f96d2a6d0cffb5e18bcfcc1e5d.jpg",
          "ferro": "3a35111470df6ac145ebfb635e652424.png"}
AUTH = {a["id"]: a for a in json.loads((HERE / "authors.json").read_text())}
MIRR = json.loads((HERE / "author-briefs-private.json").read_text())
BUSCA = ("AnKing Step por texto e pelo bloco Costanzo GI 05 Digestion/First Aid (ver busca/ e q.py: plicae, microvilli, colipase, "
         "bile salts, cholesterol esterase, phospholipase A2, Na+-H+, ENaC colon, solvent drag, unstirred, TRPV6, limit dextrin, "
         "maltase/isomaltase, menaquinone, claudins, MLCK); Referências Externas pelos mesmos termos: ")
V, Z, R = 3, 4, 5


def img(ref, w=520):
    if isinstance(ref, int):
        return f'<img src="nebli-uc08-fi05-s{ref:02d}.png" width="{w}">'
    return f'<img src="{AK_IMG[ref]}">'


def ak(key, src, flags, bloco, alvo, slide, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)


def au(key, flags, bloco, alvo, slide, autoria, falta, motivo, imagem=None):
    a = AUTH[key]
    extra = a.get("extra", "")
    if imagem is not None:
        extra += ("<br><br>" if extra else "") + img(imagem)
    return dict(key=key, kind="autoral", flags=flags, bloco=bloco, text=a["text"], extra=extra, alvo=alvo, evid=f"Slide {slide}",
                autoria=autoria, busca=BUSCA + falta, espelhos=MIRR[key]["mirror_nids"], motivo=motivo,
                imagem=(f"slide {imagem}" if isinstance(imagem, int) else f"AnKing {AK_IMG[imagem]}") if imagem is not None else "sem figura: fato simples")


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_, G_, H_ = "A-epitelio", "B-carboidratos", "C-proteinas", "D-lipidios", "E-ions-agua", "F-minerais", "G-vitaminas", "H-paracelular"
CARDS = [
 # ---------- A. Epitélio absortivo (slides 2–3) ----------
 sh(1790980910107, "azul", A_, "Vilosidades e microvilosidades ampliam a superfície", 2, "Já vivo na BT04; aqui é a base da amplificação."),
 sh(1790972071061, "azul", A_, "Pregas circulares no jejuno", 2, "Já vivo na AN01."),
 sh(1791023296918, "azul", A_, "Pregas 3×, vilos 10×, microvilos 20× (enterócito, Junqueira)", 2, "Já vivo na BT04 (nota Histology, clozes da borda e da amplificação); substitui o autoral do piloto."),
 ak("tj-paracelular", 1488502337028, {1: V}, A_, "Junção de oclusão limita a via paracelular", 2, "Verde: conceito que sustenta transcelular × paracelular em todo epitélio."),
 au("jejuno", {1: Z}, A_, "Jejuno como principal sítio de absorção", 3, "prova", "AnKing só tem absorção de folato/B12 por segmento.", "Azul: mensagem do slide 3."),
 # ---------- B. Carboidratos (slide 4) ----------
 ak("amilase-salivar", 1482030269123, {1: Z}, B_, "Amilase salivar inicia a digestão de carboidratos", 4, "Azul: básico de apoio."),
 ak("amilase-14", 1482115420919, {1: V, 2: Z}, B_, "α-amilases rompem ligações α-1,4 do amido", 4, "c1 verde (enzima e ligação); c2 azul."),
 ak("amido-estomago-hx", 1702213017666, {1: Z}, B_, "Digestão do amido pela amilase salivar continua no estômago", 4, "Azul: percentuais do professor. F-18: substitui o autoral; recorte do Histology/Junqueira.", origin="Histology", text="Carbohydrate digestion begun by salivary amylase continues in the {{c1::stomach}}", extra=img("amido")),
 ak("amilase-ativa", 1482115442644, {1: R}, B_, "Amilase pancreática é secretada ativa", 4, "Rosa: contraste com as proteases, pouco ganho."),
 ak("so-monossacarideos", 1482115408306, {1: V}, B_, "Só monossacarídeos são absorvidos", 4, "Verde: regra que explica as oligossacaridases."),
 au("dextrinase", {1: Z}, B_, "α-dextrinase rompe α-1,6", 4, "prova", "AnKing só tem lactase e sucrase.", "Azul: enzima da borda em escova listada no slide.", imagem="amido"),
 au("maltase", {1: Z}, B_, "Maltase", 4, "prova", "AnKing só tem lactase e sucrase.", "Azul: enzima da borda em escova listada no slide; F-18: um cloze só (glicose ficou no texto)."),
 ak("sacarase", 1474165401226, {1: Z, 2: Z}, B_, "Sacarase", 4, "Azul: enzima da borda em escova listada no slide."),
 sh(1790980912530, "verde", B_, "Lactase na borda em escova", 4, "Já vivo em BT04; verde aqui pela relação com intolerância à lactose."),
 ak("lactase-diarreia", 1474164990441, {1: V}, B_, "Deficiência de lactase → diarreia osmótica", 4, "Verde: única clínica do bloco, encaixe direto com a borda em escova."),
 ak("sglt1", 1482115445612, {1: V}, B_, "SGLT1: glicose e galactose com Na+", 4, "Verde: transportador central."),
 ak("sglt1-quais", 1482115451005, {1: Z}, B_, "Quais açúcares usam SGLT1", 4, "Azul: sentido inverso do anterior."),
 ak("glut5", 1482115460996, {1: V}, B_, "GLUT5: frutose", 4, "Verde: transportador central."),
 ak("glut2", 1482115455383, {1: V}, B_, "GLUT2 basolateral", 4, "Verde: saída comum dos três açúcares."),
 ak("glut2-quais", 1482115473217, {1: Z}, B_, "Quais açúcares saem por GLUT2", 4, "Azul: sentido inverso."),
 # ---------- C. Proteínas (slide 5) ----------
 sh(1790979869285, "azul", C_, "Célula principal: pepsinogênio e lipase gástrica", 5, "Já vivo na BT03."),
 sh(1790979869685, "azul", C_, "Pepsinogênio → pepsina com H+", 5, "Já vivo na BT03."),
 ak("pepsina-inicio", 1482115484108, {1: V}, C_, "Pepsina inicia a digestão proteica", 5, "Verde: primeiro passo."),
 sh(1790999836655, "verde", C_, "Aminoácidos e ácidos graxos estimulam a CCK", 5, "Já vivo na FI09; elo entre produtos da digestão e suco pancreático."),
 ak("cck-enzimas", 1482115334134, {1: V}, C_, "CCK libera o componente enzimático do pâncreas", 5, "Verde: mecanismo central dos slides 5 e 6."),
 ak("proteases-inativas", 1482115500165, {1: Z}, C_, "Proteases pancreáticas secretadas como zimogênios", 5, "Azul: básico de apoio."),
 ak("tripsinogenio", 1482115490061, {1: V}, C_, "Tripsinogênio → tripsina é o primeiro passo", 5, "Verde."),
 ak("enteropeptidase", 1482115492876, {1: V}, C_, "Enteropeptidase da borda em escova", 5, "Verde: enzima-chave da cascata."),
 ak("tripsina-todas", 1482115504921, {1: V}, C_, "Tripsina ativa todos os zimogênios", 5, "Verde."),
 ak("tripsina-auto", 1482115525140, {1: Z}, C_, "Autocatálise da tripsina", 5, "Azul: o 'T+' do slide."),
 ak("quimotripsinogenio", 1482115509710, {1: Z}, C_, "Quimotripsinogênio", 5, "Azul: zimogênio listado."),
 ak("proelastase", 1482115513922, {1: Z}, C_, "Pró-elastase", 5, "Azul: zimogênio listado."),
 ak("procarboxipeptidase", 1482115518484, {1: Z}, C_, "Pró-carboxipeptidase", 5, "Azul: zimogênio listado."),
 ak("enteropeptidase-def", 1521768510367, {1: R}, C_, "Deficiência de enteropeptidase", 5, "Rosa: clínica rara, reforça o papel da enzima."),
 ak("pept1", 1482115537298, {1: V}, C_, "Di/tripeptídeos entram com H+ (PepT1)", 5, "Verde: transportador central."),
 ak("aa-na", 1482115532737, {1: Z}, C_, "Aminoácidos entram com Na+", 5, "Azul."),
 ak("porta-hx", 1702318251919, {1: V}, C_, "Nutrientes absorvidos chegam ao fígado pela veia porta", 5, "Verde: contraste portal × linfa organiza toda a absorção. F-18: substitui o autoral; recorte do Histology/Junqueira.", origin="Histology", text="Nutrients absorbed in the small intestine reach the liver through the {{c1::portal vein}}", extra=""),
 # ---------- D. Lipídios (slide 6) ----------
 ak("lipase-lingual", 1482030273275, {1: Z}, D_, "Lipase lingual", 6, "Azul: básico de apoio."),
 ak("cck-bile", 1482115365440, {1: V}, D_, "CCK é o maior estímulo para ejeção de bile", 6, "Verde: mecanismo central do slide."),
 ak("cck-vesicula", 1482021838448, {1: Z}, D_, "CCK contrai a vesícula biliar", 6, "Azul: CCK libera o suco biliar no slide 6."),
 ak("sais-anfipaticos", 1482115357618, {1: V}, D_, "Sais biliares anfipáticos emulsificam", 6, "Verde: por que a emulsificação funciona."),
 ak("lipases-pancreaticas", 1482115541696, {1: V}, D_, "Lipases pancreáticas", 6, "Verde; o Extra lista lipase, colesterol-éster-hidrolase e fosfolipase A2."),
 au("colipase", {1: Z}, D_, "Colipase", 6, "prova", "zero resultado para 'colipase'.", "Azul: aparece na figura da micela.", imagem=6),
 ak("monoglicerideo-hx", 1702225193904, {1: Z}, D_, "Produtos da lipase: glicerol, ácidos graxos e monoglicerídeos", 6, "Azul. F-18: substitui o autoral; recorte do Histology/Junqueira.", origin="Histology", text="Gastric and pancreatic lipases digest fats into fatty acids and {{c1::monoglycerides}}", extra=img("lipidios")),
 au("fosfolipase", {1: Z}, D_, "Fosfolipase A2 → lisofosfolipídio", 6, "prova", "AnKing só tem PLA2 em inflamação.", "Azul: 'lisofos' no slide."),
 au("colesterol-esterase", {1: Z}, D_, "Colesterol-éster-hidrolase", 6, "prova", "AnKing só tem éster de colesterol em lipoproteínas (LCAT, CETP, quilomícron); externos sem a enzima pancreática (busca de 03/10).",
    "Azul: 'Colesterol-éster-hidrolase' no slide 6; calibração Ninja Nerd (F-14)."),
 ak("lipase-ph", 1482115547887, {1: Z}, D_, "pH baixo inativa a lipase pancreática", 6, "Azul."),
 ak("micelas-solubilizam", 1482115554891, {1: V}, D_, "Micelas solubilizam os produtos", 6, "Verde."),
 ak("micelas-borda", 1482115562039, {1: V}, D_, "Micelas levam os produtos à borda em escova", 6, "Verde."),
 ak("reesterificacao", 1482115566901, {1: Z}, D_, "Reesterificação no enterócito", 6, "Azul."),
 ak("quilomicrons", 1482115570847, {1: V}, D_, "Quilomícrons", 6, "Verde."),
 sh(1790980913479, "verde", D_, "Quilomícrons entram nos lácteos", 6, "Já vivo na BT04."),
 sh(1790981519924, "azul", D_, "Linfa → ducto torácico", 6, "Já vivo na AN07."),
 # ---------- E. Íons e água (slide 7) ----------
 au("volume-absorcao", {1: Z}, E_, "Delgado 7,5 L; grosso 1,4 L", 7, "prova", "nenhum card com o balanço hídrico.", "c1 azul; o 1,4 L do cólon (era rosa) virou texto (F-14)."),
 au("agua-osmose", {1: V}, E_, "Água segue os solutos por osmose", 7, "central", "AnKing só trata de osmose em diarreia/laxativos.", "Verde: princípio de toda absorção de água."),
 au("bomba", {1: V}, E_, "Na+/K+-ATPase basolateral mantém o gradiente", 7, "central", "AnKing só no néfron.", "Verde: motor de todos os cotransportes da aula.", imagem="sglt"),
 au("nhe3", {1: Z}, E_, "NHE3", 7, "prova", "AnKing só tem o trocador no túbulo proximal.", "Azul: destacado com *** no slide."),
 au("enac", {1: Z}, E_, "ENaC no cólon", 7, "prova", "AnKing só tem ENaC renal.", "Azul."),
 au("arraste", {1: Z}, E_, "Arraste pelo solvente", 7, "prova", "zero resultado para 'solvent drag'.", "Azul."),
 ak("k-delgado", 1482115592577, {1: Z}, E_, "K+ absorvido passivamente no delgado", 7, "Azul: faixa verde do slide (via paracelular)."),
 ak("k-colon", 1482115594816, {1: R, 2: R}, E_, "K+ secretado no cólon", 7, "Rosa: contraste que o slide não mostra; liga a hipocalemia na diarreia."),
 # ---------- F. Informações extras: HCO3-, ferro, cálcio (slides 8–9) ----------
 ak("ferro-fe2", 1482115585152, {1: V, 2: V}, F_, "Ferro absorvido como Fe2+ no duodeno", 9, "Verde: núcleo duradouro do ferro."),
 ak("ferro-heme", 1476661053401, {1: Z, 2: Z}, F_, "Ferro heme e HCP-1", 9, "Azul."),
 ak("ferro-nao-heme", 1476661061176, {1: Z, 2: Z}, F_, "Fe3+ → Fe2+ por Dcytb/vitamina C", 9, "Azul."),
 ak("vit-c-ferro", 1476583830053, {2: Z}, F_, "Vitamina C aumenta a absorção de ferro", 9, "Azul: facilitador do slide.", uncloze=[1, 3]),
 ak("dmt1", 1476661066773, {1: V}, F_, "DMT-1", 9, "Verde."),
 ak("ferritina", 1478834050609, {1: Z}, F_, "Ferritina armazena o ferro intracelular", 9, "Azul."),
 ak("ferroportina", 1476661073431, {1: V}, F_, "Ferroportina", 9, "Verde."),
 ak("ferroxidase", 1476661078631, {1: Z}, F_, "Ferroxidase (hefestina)", 9, "Azul."),
 ak("transferrina", 1476661087790, {1: Z}, F_, "Fe3+ ligado à transferrina", 9, "Azul."),
 ak("hepcidina", 1476661104838, {1: V, 2: V, 3: V}, F_, "Hepcidina bloqueia a ferroportina", 9, "Verde: controle sistêmico, base de anemias futuras."),
 ak("calbindina", 1462146169234, {1: V}, F_, "Vitamina D aumenta a absorção de Ca2+ via calbindina", 9, "Verde: regulação que volta em endócrino."),
 ak("calcitriol", 1494989429488, {1: Z}, F_, "Calcitriol aumenta absorção de Ca2+ e fosfato", 9, "Azul."),
 # ---------- G. Vitaminas (slide 10) ----------
 ak("lipossoluveis", 1476583124449, {1: V, 2: Z}, G_, "Lipossolúveis dependem de íleo, pâncreas e bile", 10, "c1 verde; c2 azul."),
 au("vit-lipo-linfa", {1: Z}, G_, "Lipossolúveis saem nos quilomícrons", 10, "prova", "AnKing só trata da má absorção.", "Azul: esquema do slide.", imagem=10),
 ak("vit-k-flora", 1520709952510, {1: V}, G_, "Microbiota produz vitamina K", 10, "Verde: HY 1 (Q048); F-18: AnKing achado na nova busca substitui o autoral da K2."),
 ak("vitk-recem-nascido", 1473995743024, {1: V, 2: V}, G_, "Recém-nascido sem vitamina K (sem flora colônica)", 10, "Verdes: 'RN não tem vitamina K' no slide 10."),
 ak("vit-k-hemorragia", 1476584046114, {1: V}, G_, "Deficiência de vitamina K → hemorragia neonatal", 10, "Verde: destacado no slide."),
 ak("varfarina", 1474340640502, {1: Z, 2: Z}, G_, "Varfarina inibe a epóxido redutase", 10, "Azul: 'VARFARINA' no slide."),
 ak("vit-d-uv", 1462145970044, {1: Z}, G_, "Vitamina D3 da pele por UV", 10, "Azul: caixa de síntese do slide."),
 ak("vit-d-25", 1494988708228, {3: Z}, G_, "1ª hidroxilação no fígado", 10, "Azul."),
 ak("vit-d-rim", 1475704481414, {1: Z}, G_, "2ª hidroxilação no rim", 10, "Azul."),
 ak("b12-r", 1476661138357, {1: Z, 2: R}, G_, "B12 ligada à haptocorrina (R-binder)", 10, "c1 azul; c2 rosa (origem salivar)."),
 ak("b12-proteases", 1476661144103, {1: V, 2: V}, G_, "Proteases pancreáticas liberam a B12 para o fator intrínseco", 10, "Verde: sequência central do slide."),
 ak("b12-fi-essencial", 1482115259111, {1: V}, G_, "Fator intrínseco é a única secreção gástrica essencial", 10, "Verde."),
 ak("b12-ileo", 1482115590320, {1: V}, G_, "B12 absorvida no íleo terminal", 10, "Verde."),
 ak("b12-complexo", 1476661158569, {1: Z}, G_, "Complexo B12-FI endocitado no íleo", 10, "Azul."),
 ak("b12-pancreas", 1478898351508, {1: V}, G_, "Insuficiência pancreática → deficiência de B12", 10, "Verde: 'PANCREATITE' no slide, com mecanismo."),
 sh(1790980019633, "azul", G_, "Cirurgia gástrica → deficiência de B12", 10, "Já vivo na BT03; 'GASTRECTOMIA' no slide 10."),
 ak("b12-resseccao", 1476583774604, {1: Z}, G_, "Ressecção do íleo → deficiência de B12", 10, "Azul: 'RESSECÇÃO DO ÍLEO' no slide."),
 # ---------- H. Via paracelular (slides 11–12) ----------
 ak("tj-proteinas", 1488502340989, {1: Z}, H_, "Claudinas e ocludinas", 12, "Azul."),
 au("claudinas", {1: R}, H_, "Claudinas 2 e 15 devolvem Na+ ao lúmen", 11, "lateral", "AnKing só tem composição da junção e C. perfringens.", "Rosa: dado de artigo, slide extra.", imagem=11),
]
EXCLUIDOS = [
 (1482115437677, "Trealase: fora do slide"), (1482115477908, "Teste da D-xilose: clínica diagnóstica lateral"),
 (1482115316095, "HCO3- pelos ductos pancreáticos: aula de secreções"), (1482115326502, "Secretina: aula de secreções"),
 (1482115609366, "cAMP e canais de Cl-: secreção intestinal"), (1525915981730, "Inflamação aumenta hepcidina: além do slide"),
 (1525916402432, "Hipóxia reduz hepcidina: além do slide"), (1476661164427, "Transcobalamina II: além do slide"),
 (1476583684909, "Folato no jejuno: slide só cita 'complexo B'"), (1482115602773, "Fluxo e secreção de K+ no cólon: além do slide"),
 (1474165267922, "Deficiência primária de lactase (série de 10 notas): só a consequência osmótica entra"),
]
FORA_DO_RECORTE = ["Secreção gástrica, pancreática e biliar (aula de secreções, ainda sem material)", "Síndromes de má absorção (celíaca, Whipple, etc.)",
                   "Metabolismo do ferro fora do enterócito (TIBC, anemias)", "Slide 3: dados de equinacosídeo (só a mensagem 'jejuno')"]

# 03/10 (F-20261003-CLAUDE-13 e Q048): toda nota AnKing HY 1–2 do recorte tem ao menos um card verde.
HY_VERDE = {"lipase-ph", "k-delgado", "k-colon", "vit-c-ferro", "transferrina", "calcitriol", "varfarina", "vit-d-uv", "vit-d-25", "vit-d-rim", "b12-r", "b12-complexo", "b12-resseccao"}
for _c in CARDS:
    if _c["key"] in HY_VERDE:
        _k = sorted(_c["flags"])[0]; _c["flags"][_k] = V
        _c["motivo"] = "Verde: HY 1–2 do recorte (Q048). " + _c["motivo"]

# 03/10: coincidências de palavra-resposta conferidas (gate past_errors)
DUP_OK = {"maltase": "resposta 'glucose' coincide com o card da sacarase; aqui o alvo é a maltase e o produto da maltose", "vit-lipo-linfa": "resposta 'chylomicrons' coincide com o card dos quilomícrons; aqui o alvo é a saída das vitaminas lipossolúveis", "vit-k2-old": "resposta 'intestinal bacteria' coincide por palavra com o card da calbindina; alvo próprio: origem da vitamina K2"}
for _c in CARDS:
    if _c["key"] in DUP_OK: _c["duplicacao_ok"] = DUP_OK[_c["key"]]

# F-20261003-CLAUDE-15: explicação curta no verso
from nebli.ilustrar import anotar
from notas import NOTAS
CARDS = anotar(CARDS, NOTAS)
