# Especificação curada — Correlação patológica-radiológica 2 (UC03 P2, Patologia + Radiologia, aula 19; 33 lâminas só com imagens:
# caso 1 hemangioma hepático 2–9, caso 2 doença hepática alcoólica 10–31). Feita em 03/10/2026 a partir de planejamento.json.
# AnKing → outros acervos → autoral. Imagens da aula entram no Extra dos autorais de correlação (a aula é leitura de imagem).
RUN_ID = "uc03-pr02-20261003a"
SHORT = "pr02"
LESSON = "2026-uc03-patologia-radiologia-19-correlacao-2"
DECK = "NEBLI::UC03::P2::Patologia::Correlação patológica-radiológica 2"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261003-CLAUDE-13) + PLANO-GERACAO-ANO, 03/10/2026"
_P = (3, 4, 8, 9, 11, 13, 18, 22, 24, 27, 28, 30, 31)
MEDIA = {f"nebli-uc03-pr02-p{p:02d}f.png": f"io/nebli-uc03-pr02-p{p:02d}f.png" for p in _P}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt, 19 consultas em 03/10); Referências Externas "
         "(MCAT, Histology, LLU, Dope, AnatoKing) pelos mesmos alvos (busca/ext.txt): ")
F = lambda p, w=460: f'<img src="nebli-uc03-pr02-p{p:02d}f.png" width="{w}">'


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_ = "A-hemangioma", "B-figado-normal", "C-esteatose", "D-cirrose-e-chc", "E-hipertensao-portal"
CARDS = [
 # ---------- A. Caso 1: hemangioma cavernoso (slides 2–9) ----------
 au("hemangioma-us", "An incidental, well-defined <b>hyperechoic</b> liver nodule in a young asymptomatic woman is most likely a {{c1::hemangioma}}", {1: Z}, A_,
    "Hemangioma: nódulo hiperecogênico incidental", "3; E1 da aula", "prova", "AnKing tem o hemangioma sem o achado de ultrassom; externos sem o alvo.", [1525564242390, 1580590159680],
    "Azul: ultrassom do caso 1 (slide 3).", extra=F(3), duplicacao_ok="resposta 'hemangioma' coincide com os cards AnKing da doença; alvo próprio: reconhecer o nódulo hiperecogênico incidental no ultrassom"),
 au("hemangioma-tc", "On contrast CT, a hepatic hemangioma shows peripheral nodular enhancement in the arterial phase with {{c1::centripetal}} fill-in on later phases", {1: V}, A_,
    "Padrão dinâmico do hemangioma", "4; E1 da aula", "central", "nenhum card de imagem do hemangioma no AnKing nem nos externos.", [1580585590157, 1486591272185],
    "Verde: o padrão que fecha o diagnóstico na aula (slide 4, ART/PORT/EQUIL).", extra=F(4)),
 ak("hemangioma-assintomatico", 1525564242390, {1: Z}, A_, "Hemangioma costuma ser assintomático", 2, "Azul: 'assintomática, exames de rotina' no slide 2."),
 ak("hemangioma-mulheres", 1580590159680, {1: R}, A_, "Massas hepáticas benignas em mulheres em idade reprodutiva", 2, "Rosa: perfil da paciente do caso 1."),
 ak("hemangioma-pele-figado", 1471825973147, {1: Z}, A_, "Hemangiomas na pele e no fígado", 5, "Azul: sítio do hemangioma."),
 ak("hemangioma-cavernoso", 1486591267339, {1: Z}, A_, "Hemangioma cavernoso: benigno, em tecidos profundos como o fígado", 5, "Azul: tipo de hemangioma das peças dos slides 5–8."),
 au("hemangioma-macro", "Grossly, a hepatic hemangioma is a well-circumscribed, {{c1::dark red}}, spongy subcapsular lesion", {1: Z}, A_,
    "Macroscopia do hemangioma", "8; Robbins cap. 18", "prova", "AnKing descreve só a histologia.", [1580585590157, 1486591267339], "Azul: peça do slide 8.", extra=F(8)),
 ak("hemangioma-histologia", 1580585590157, {1: V}, A_, "Histologia: espaços cavernosos cheios de hemácias", 9, "Verde: lâmina do slide 9, correlação com o padrão de contraste."),
 ak("hemangioma-biopsia", 1486591272185, {1: V}, A_, "Não biopsiar hemangioma cavernoso", 9, "Verde: HY (2); consequência prática do diagnóstico por imagem."),
 # ---------- B. Fígado normal (slides 6–7) ----------
 ak("triade-portal", 1486775502282, {1: V, 2: V, 3: V}, B_, "Tríade portal: ducto biliar, artéria hepática, veia porta", 7, "Verdes: HY (1); espaço porta da lâmina normal do slide 7."),
 ak("fluxo-portal-central", 1486776242882, {1: Z}, B_, "Sangue flui do espaço porta para a veia central", 7, "Azul: base das zonas 1–2–3 do slide 7."),
 ak("zona-3", 1486776374938, {1: V, 2: V}, B_, "Zona 3 = centrolobular", 7, "Verdes: HY (1); números 1, 2, 3 no slide 7."),
 ak("zona-3-isquemia", 1486776390497, {1: V}, B_, "Zona 3 sofre primeiro com isquemia", 7, "Verde: HY (2)."),
 ak("zona-3-alcool", 1486776403243, {1: V}, B_, "Hepatite alcoólica começa na zona 3", 7, "Verde: HY (2); liga o fígado normal ao caso 2."),
 # ---------- C. Caso 2: álcool e esteatose (slides 10–16) ----------
 ak("alcool-causa", 1486522786197, {1: V}, C_, "Álcool é a causa mais comum de doença hepática no Ocidente", 10, "Verde: HY (1); 'etilista' no slide 10."),
 ak("esteatose-macro", 1486522804267, {1: V, 2: V}, C_, "Esteatose: alteração gordurosa macrovesicular", 11, "Verdes: HY (1)."),
 ak("esteatose-peso", 1486522799728, {1: Z}, C_, "Fígado gorduroso: pesado e untuoso", 11, "Azul: peça amarela do caso 2."),
 ak("esteatose-reversivel", 1486522811003, {1: Z}, C_, "Esteatose reverte com abstinência", 11, "Azul: Robbins (alteração gordurosa reversível)."),
 au("esteatose-us", "On ultrasound, a fatty liver looks brighter than the {{c1::renal cortex}}", {1: V}, C_,
    "Esteatose no ultrassom: fígado hiperecogênico", "11–12; E1 da aula", "central", "zero card de ultrassom hepático no AnKing e nos externos.", [1486522804267, 1486522799728],
    "Verde: ultrassom do caso 2 comparado ao normal (slides 11–12).", extra=F(11)),
 au("esteatose-tc", "On non-contrast CT, a fatty liver appears less dense than the {{c1::spleen}}, reversing the normal relationship", {1: V}, C_,
    "Esteatose na TC: fígado menos denso que o baço", "13–16; E1 da aula", "central", "'Hounsfield' e 'CT attenuation' sem card nos acervos.", [1486522804267, 1486522811003],
    "Verde: TC do caso 2 comparada à normal (slides 13–16).", extra=F(13)),
 ak("hepatite-alcoolica", 1486522813431, {1: V, 2: Z}, C_, "Hepatite alcoólica: balonização, necrose, neutrófilos", 17, "Verde c1: HY (1); passo entre esteatose e cirrose (Robbins)."),
 ak("ast-alt", 1486522828840, {1: V, 2: Z}, C_, "Hepatite alcoólica: AST > ALT", 17, "Verde c1: HY (2)."),
 ak("acetaldeido", 1486522822101, {1: V}, C_, "Acetaldeído media o dano alcoólico", 17, "Verde: HY (1)."),
 # ---------- D. Cirrose, colestase e CHC (slides 17–24) ----------
 ak("cirrose-definicao", 1486522637384, {1: V, 2: V}, D_, "Cirrose: fibrose em faixas e nódulos de regeneração", 18, "Verdes: HY (1); peças dos slides 18–21 e lâminas 22–23."),
 ak("estreladas-tgfb", 1486522654540, {1: V, 2: V}, D_, "Fibrose da cirrose: células estreladas e TGF-β", 22, "Verdes: HY (1)."),
 ak("estreladas-mec", 1486776353051, {1: Z, 2: Z}, D_, "Estreladas ativadas produzem matriz no espaço de Disse", 22, "Azuis: Robbins (patogenia da fibrose)."),
 au("micro-macronodular", "Early alcoholic cirrhosis forms uniform regenerative nodules smaller than {{c1::3 mm}}, the micronodular pattern", {1: Z}, D_,
    "Cirrose micronodular × macronodular", "18–19; Robbins cap. 18", "prova", "AnKing define cirrose sem o tamanho dos nódulos.", [1486522637384, 1486522654540],
    "Azul: peças micro e macronodular dos slides 18–19.", extra=F(18)),
 au("reticulina", "A silver {{c1::reticulin}} stain outlines the regenerative nodules of cirrhosis with black fibers", {1: R}, D_,
    "Reticulina mostra septos e nódulos", "22–23", "lateral", "nenhum card sobre coloração de reticulina na cirrose.", [1486522637384, 1486776353051],
    "Rosa: lâmina de reticulina do slide 23.", extra=F(22)),
 ak("chc-mais-comum", 1486591276598, {1: V}, D_, "CHC: tumor maligno primário mais comum do fígado", 24, "Verde: HY (2); peça do slide 24."),
 ak("chc-afp", 1486591331907, {1: V}, D_, "AFP é o marcador do CHC", 24, "Verde: HY (2)."),
 ak("chc-rastreio", 1495729974126, {1: Z}, D_, "Cirrótico: ultrassom a cada 6 meses", 24, "Azul: vigilância do CHC na cirrose."),
 # ---------- E. Hipertensão portal (slides 25–31) ----------
 sh(1790981519128, "verde", E_, "Formação da veia porta", 26, "Já vivo na AN07; esquema do sistema porta do slide 26."),
 ak("hp-cirrose-causa", 1486522673379, {1: V}, E_, "Cirrose é a causa mais comum de hipertensão portal", 28, "Verde: HY (1); 'hipertensão portal' no slide 28."),
 ak("hp-cirrose", 1486522667060, {1: Z}, E_, "Cirrose complicada por hipertensão portal", 28, "Azul: mecanismo (fibrose aumenta a pressão sinusoidal)."),
 ak("hp-shunts", 1486522684741, {1: V, 2: Z}, E_, "Hipertensão portal abre derivações portossistêmicas", 27, "Verde c1: HY (2); colaterais do slide 27."),
 sh(1790981518578, "verde", E_, "Varizes esofágicas: anastomose portossistêmica", 27, "Já vivo na AN07."),
 sh(1790981527126, "azul", E_, "Varizes anorretais", 27, "Já vivo na AN07; 'hemorrhoidal veins' no slide 27."),
 ak("cabeca-medusa", 1486771285047, {1: V, 2: V}, E_, "Cabeça de medusa: paraumbilicais × epigástricas", 27, "Verdes: HY (1); 'caput medusae' no slide 27."),
 au("hp-tc", "On CT, portal hypertension shows a nodular liver, ascites, collateral veins and an enlarged {{c1::spleen}}", {1: Z}, E_,
    "Sinais de hipertensão portal na TC", "28–29; E1 da aula", "prova", "nenhum card de imagem da hipertensão portal nos acervos.", [1486522690115, 1486522681611],
    "Azul: TC do slide 28, com o contorno delineado.", extra=F(28), duplicacao_ok="resposta 'spleen' também é do card da esteatose na TC; aqui é o baço aumentado da hipertensão portal"),
 ak("hp-ascite", 1486522681611, {1: V}, E_, "Hipertensão portal causa ascite", 28, "Verde: líquido livre na TC do slide 28."),
 ak("hp-esplenomegalia", 1486522690115, {1: V}, E_, "Esplenomegalia congestiva e hiperesplenismo", 30, "Verde: baço do slide 30."),
 ak("hp-plaquetas", 1486591413282, {1: V}, E_, "Plaquetopenia pela esplenomegalia", 30, "Verde: HY (1); consequência do hiperesplenismo."),
 au("baco-congesto", "In portal hypertension, the cut surface of the enlarged spleen is homogeneous and {{c1::dark red}} from chronic passive congestion", {1: R}, E_,
    "Baço congesto ao corte", "30; E1 da aula", "lateral", "AnKing tem a esplenomegalia sem a macroscopia.", [1486522690115, 1486591413282],
    "Rosa: peça do slide 30.", extra=F(30), duplicacao_ok="resposta 'dark red' também é do hemangioma; aqui o alvo é o baço congesto"),
 ak("varizes-terco-inferior", 1482203751576, {1: V}, E_, "Varizes: veias submucosas do terço inferior do esôfago", 31, "Verde: histologia e endoscopia do slide 31."),
 ak("varizes-hp", 1482203756188, {1: V}, E_, "Varizes vêm da hipertensão portal", 31, "Verde: HY (2); o Extra explica a gástrica esquerda."),
 ak("varizes-hematemese", 1482203769705, {1: V, 2: Z}, E_, "Varizes rompem com hematêmese indolor", 31, "Verde c1: HY (1)."),
 ak("varizes-morte", 1482203779331, {1: V, 2: Z}, E_, "Varizes: causa comum de morte na cirrose", 31, "Verde c1: HY (2)."),
]

EXCLUIDOS = [
 (1486776339459, "Espaço de Disse: anatomia microscópica, coberta pelas células estreladas"), (1486776347708, "Estreladas guardam vitamina A: lateral"),
 (1486522693430, "Síndrome hepatorrenal: fora dos slides"), (1486522702734, "Encefalopatia hepática: fora dos slides"),
 (1486591290032, "Aflatoxina: carcinogênese (aula de carcinógenos, P4)"), (1486591284504, "Hepatites virais e CHC: fora deste caso"),
 (1486591255795, "Adenoma hepático: diagnóstico diferencial, sem slide"), (1580591221930, "Hiperplasia nodular focal: sem slide"),
 (1486770898373, "Varizes esofágicas por anastomose: já vivo na AN07 (autoral)"),
]
FORA_DO_RECORTE = [
 "Tratamento da hipertensão portal e das varizes",
 "Diagnósticos diferenciais de nódulos hepáticos sem slide (adenoma, HNF, metástase)",
 "Hepatites virais e outras causas de cirrose",
]

# F-20261003-CLAUDE-15: figura de livro (Robbins) e explicação curta no verso
from nebli.ilustrar import ilustrar, anotar
from imagens import IMAGENS, SEM_IMAGEM, LIVRO, SLIDE_OK
from notas import NOTAS
MEDIA.update(LIVRO)
CARDS = anotar(ilustrar(CARDS, IMAGENS, SEM_IMAGEM), NOTAS)
CARDS = [dict(c, slide_sem_alternativa=SLIDE_OK[c["key"]]) if c["key"] in SLIDE_OK else c for c in CARDS]
