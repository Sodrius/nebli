# Especificação curada — Secreção gástrica (UC08 P2, Fisiologia, Profa. Fran Goulart; Aula-4_MED_2026.pdf, 11 lâminas:
# secreção gástrica 1–7, "informações extras" sobre microbiota 8–11). Feita em 03/10/2026 a partir de planejamento.json.
# AnKing → outros acervos (Histology = Junqueira) → autoral. Ordem = slides. Critérios até F-20261003-CLAUDE-13.
RUN_ID = "uc08-fi06-20261003a"
SHORT = "fi06"
LESSON = "2026-uc08-fisiologia-06-secrecao-gastrica"
DECK = "NEBLI::UC08::P2::Fisiologia::Secreção gástrica"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261003-CLAUDE-13) + PLANO-GERACAO-ANO, 03/10/2026"
MEDIA = {f"nebli-uc08-fi06-p{p:02d}f.png": f"io/nebli-uc08-fi06-p{p:02d}f.png" for p in (3, 4, 7, 9, 10, 11)}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt, 27 consultas em 03/10); Referências Externas "
         "(Histology, MCAT, LLU, Ankisthesia) pelos mesmos alvos (busca/ext.txt, 9 consultas): ")
F = lambda p, w=460: f'<img src="nebli-uc08-fi06-p{p:02d}f.png" width="{w}">'


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_ = "A-suco-e-barreira", "B-fases", "C-somatostatina", "D-celula-parietal", "E-pepsinogenio-e-regulacao", "F-microbiota"
CARDS = [
 # ---------- A. Suco gástrico e barreira mucosa (slide 2) ----------
 ak("defesas-mucosa", 1482275730166, {1: V, 2: V, 3: Z}, A_, "Defesas da mucosa: muco, HCO3-, prostaglandinas, fluxo sanguíneo", 2, "Verdes: 'barreira mucosa gástrica' no slide 2; azul: fluxo."),
 ak("aine-gastrite", 1482275748424, {1: V, 2: V}, A_, "AINE reduz PGE2 e causa gastrite aguda", 2, "Verdes: HY (1); 'AINES → inibição da PG → gastrite' no slide 2."),
 ak("gastrite-aguda", 1482275713023, {1: Z}, A_, "Gastrite aguda: dano ácido à mucosa", 2, "Azul: 'gastrite' no slide 2."),
 ak("choque-ulcera", 1482275770410, {1: V}, A_, "Choque causa úlceras de estresse por isquemia", 2, "Verde: HY (1); 'estresse → gastrite' no slide 2."),
 # ---------- B. Fases e taxa de secreção (slide 3) ----------
 ak("fase-cefalica-30", 1482115200729, {1: Z}, B_, "Fase cefálica: 30% do HCl", 3, "Azul: '30%' no slide 3."),
 ak("fase-cefalica-vago", 1482115208173, {1: Z, 2: Z}, B_, "Fase cefálica mediada só pelo vago", 3, "Azuis: 'fase cefálica neural' no slide 3."),
 ak("fase-gastrica-60", 1482115213179, {1: Z}, B_, "Fase gástrica: 60% do HCl", 3, "Azul: '60%' no slide 3."),
 ak("fase-gastrica-mecanismo", 1482115220459, {1: Z}, B_, "Fase gástrica: vago e gastrina", 3, "Azul: 'fase gástrica neuro-hormonal' no slide 3."),
 au("fase-intestinal", "The {{c1::intestinal}} phase accounts for only about 10% of <b>gastric acid secretion</b>", {1: R}, B_,
    "Fase intestinal: 10%, hormonal", "3; Aires cap. 61", "lateral", "AnKing só traz as fases cefálica e gástrica; nenhum externo tem as fases.", [1482115200729, 1482115213179],
    "Rosa: '10%, hormonal' no slide 3.", extra=F(3)),
 # ---------- C. Somatostatina e pH no interdigestivo (slide 4) ----------
 ak("somatostatina-d", 1482021961866, {1: Z, 2: Z}, C_, "Somatostatina das células D", 4, "Azuis: 'somatostatina' no slide 4."),
 ak("somatostatina-gastrina", 1482021753483, {1: V}, C_, "Somatostatina inibe a gastrina", 4, "Verde: HY (1); 'indireto: gastrina e histamina' no slide 4."),
 ak("gastrina-ph-alto", 1482021715220, {1: V, 2: V}, C_, "pH alto estimula a gastrina", 4, "Verdes: HY (1); regulação do pH intragástrico no slide 4."),
 ak("somatostatina-vago", 1482021971578, {1: Z}, C_, "Vago diminui a somatostatina", 4, "Azul: controle da somatostatina (Aires)."),
 au("somatostatina-acido", "A low <b>intragastric pH</b> triggers the release of {{c1::somatostatin}}, which inhibits acid secretion between meals", {1: Z}, C_,
    "Ácido estimula somatostatina (pH 4 × 6)", "4; Aires cap. 61", "prova", "AnKing tem somatostatina inibindo gastrina e o efeito do vago, não o estímulo pelo ácido; externos sem o alvo.",
    [1482021753483, 1482021961866], "Azul: 'regulação do pH intragástrico no período interdigestivo' no slide 4.", extra=F(4), duplicacao_ok="resposta 'somatostatin' também é do card das células D; aqui o alvo é o estímulo pelo pH ácido"),
 # ---------- D. Célula parietal (slide 5) ----------
 ak("ach-m3", 1482030356723, {1: V, 2: V}, D_, "ACh nos receptores M3 da parietal", 5, "Verdes: HY (2); 'M3, Gq' no slide 5."),
 ak("gastrina-cckb", 1482030372145, {1: Z}, D_, "Gastrina nos receptores CCKB", 5, "Azul: 'CCKB, Gq' no slide 5."),
 ak("histamina-h2", 1482030352837, {1: V, 2: V}, D_, "Histamina nos H2 aumenta o H+", 5, "Verdes: 'H2, Gs' no slide 5."),
 ak("histamina-gs", 1461615074564, {1: Z}, D_, "H2 acoplado a Gs na membrana basolateral", 5, "Azul: 'Gs' no slide 5."),
 ak("histamina-ecl", 1482030348639, {1: Z, 2: Z}, D_, "Histamina das células ECL", 5, "Azuis: origem da histamina (slides 5 e 7)."),
 ak("gastrina-ecl", 1482030376868, {1: V}, D_, "Gastrina libera histamina das ECL", 5, "Verde: via indireta da gastrina."),
 ak("gastrina-ecl-principal", 1482030383962, {1: V}, D_, "Gastrina age sobretudo via ECL", 5, "Verde: HY (2)."),
 ak("parietal-estimulos", 1702217002761, {4: Z, 5: Z}, D_, "Estímulos da parietal: parassimpático, histamina e gastrina parácrinas", 5,
    "Azuis: estimuladores do slide 7 pelo Junqueira (nota Histology).", origin="Histology"),
 ak("mare-alcalina", 1482030339793, {1: Z, 2: Z}, D_, "Maré alcalina após a secreção ácida", 5, "Azul: HCO3- vai ao sangue na membrana basolateral (slide 5; Aires)."),
 # ---------- E. Pepsinogênio e regulação do suco (slides 6–7) ----------
 ak("pepsinogenio-estimulos", 1482115252126, {1: V, 2: V}, E_, "Pepsinogênio: vago e H+ local", 6, "Verdes: 'nervo vago' e 'H+ estimula a secreção de pepsinogênio' no slide 6."),
 sh(1791000306927, "verde", E_, "Digestão de proteínas começa pela pepsina", 6, "Já vivo na FI05."),
 au("h-secretina-pepsinogenio", "Acid releases {{c1::secretin}}, which stimulates <b>pepsinogen</b> secretion by chief cells", {1: Z}, E_,
    "H+ estimula pepsinogênio via secretina", "6; Aires cap. 61", "prova", "AnKing tem a secretina só na inibição do ácido e no bicarbonato.", [1482115252126, 1482021911657],
    "Azul: '(2) via secretina, via circulação' no slide 6; o Aires (cap. 61) acha essa via improvável.", extra="- Aires considers this route unlikely, since secretin inhibits acid secretion"),
 ak("gastrina-g", 1482021686946, {1: V, 2: V, 3: Z, 4: V}, E_, "Gastrina das células G do antro e do duodeno", 7, "Verdes: HY (1); 'gastrina' entre os estimuladores do slide 7; azul c3."),
 ak("gastrina-h", 1482021696583, {1: V}, E_, "Gastrina aumenta o H+", 7, "Verde: estimulador do slide 7."),
 ak("gastrina-distensao", 1482021710999, {1: V}, E_, "Distensão é o maior estímulo da gastrina", 7, "Verde: HY (2)."),
 ak("grp", 1482021723937, {1: V}, E_, "Vago libera gastrina via GRP", 7, "Verde: HY (2)."),
 ak("atropina-g", 1482021728193, {1: V}, E_, "Atropina não bloqueia o vago nas células G", 7, "Verde: HY (1); consequência do GRP."),
 au("gastrina-somatostatina-feedback", "<b>Gastrin</b> stimulates the release of {{c1::somatostatin}}, closing a negative feedback loop on gastrin secretion", {1: Z}, E_,
    "Retroalimentação negativa gastrina–somatostatina", "7; Aires cap. 61", "prova", "AnKing tem só a inibição da gastrina pela somatostatina, sem a alça.", [1482021753483, 1482021686946],
    "Azul: 'retroalimentação negativa gastrina-somatostatina' no slide 7.", extra=F(7), duplicacao_ok="resposta 'somatostatin' também é do card do pH ácido; aqui o estímulo é a gastrina (alça do slide 7)"),
 ak("zes-gastrina", 1482021770777, {1: V}, E_, "Zollinger-Ellison: gastrina muito alta", 7, "Verde: HY (2); 'hipersecreção de gastrina = úlcera, Zollinger-Ellison' no slide 7."),
 ak("zes-ulceras", 1482021777590, {1: V, 2: V}, E_, "Zollinger-Ellison: úlceras no duodeno e jejuno", 7, "Verdes: HY (2); '(*duodeno)' no slide 7."),
 sh(1790979867810, "verde", D_, "Célula parietal: HCl e fator intrínseco", 5, "Já vivo na BT03."),
 sh(1790980017909, "azul", D_, "Anidrase carbônica na parietal", 5, "Já vivo na BT03; 'anidrase carbônica' no slide 5."),
 sh(1790980018034, "verde", D_, "H+/K+-ATPase", 5, "Já vivo na BT03; bomba do slide 5."),
 sh(1790980018159, "azul", D_, "Trocador Cl-/HCO3- basolateral", 5, "Já vivo na BT03."),
 sh(1790979869285, "verde", E_, "Célula principal: pepsinogênio e lipase", 6, "Já vivo na BT03; 'célula principal' no slide 6."),
 sh(1790979869685, "verde", E_, "H+ converte pepsinogênio em pepsina", 6, "Já vivo na BT03; 'o H+ estimula a conversão' no slide 6."),
 sh(1790999835629, "verde", E_, "Secretina diminui o ácido e contrai o piloro", 7, "Já vivo na FI09; 'secretina (−): inibição das células parietais e G' no slide 7."),
 # ---------- F. Microbiota intestinal (slides 8–11, "informações extras") ----------
 au("microbiota-filos", "Most <b>gut bacteria</b> belong to two phyla, Firmicutes and {{c1::Bacteroidetes}}", {1: R}, F_,
    "Firmicutes e Bacteroidetes (90%)", "9", "lateral", "zero card de Firmicutes/Bacteroidetes no AnKing e nos externos.", [1520709952510, 1487640028986],
    "Rosa: slide 9, informação extra.", extra=F(9)),
 au("microbiota-local", "<b>Gut bacteria</b> are most abundant in the {{c1::colon}}", {1: R}, F_,
    "Microbiota no íleo terminal e ceco", "9", "lateral", "nenhum card nos acervos.", [1520709952510, 1473995752044], "Rosa: slide 9."),
 ak("flora-vitaminas", 1520709952510, {1: V}, F_, "Flora intestinal produz vitaminas K e B9", 9, "Verde: HY (1); 'fermentação bacteriana: vitaminas K/B' no slide 9."),
 au("probiotico", "Live microorganisms that benefit the host are called {{c1::probiotics}}", {1: R}, F_,
    "Probiótico × prebiótico", "9", "lateral", "zero resultado para probiotic/prebiotic nos acervos.", [1520709952510, 1473995752044], "Rosa: slide 9."),
 au("butirato", "Bacterial fermentation of fiber yields {{c1::butyrate}}, the short-chain fatty acid that nourishes <b>colonocytes</b>", {1: Z}, F_,
    "Butirato e integridade da barreira", "9–10", "prova", "MCAT só cita ácidos graxos de cadeia curta na absorção; nenhum card do butirato.", [1520709952510, 1560040389887],
    "Azul: 'butirato, integridade da barreira' nos slides 9–10.", extra=F(10)),
 ak("lps-tlr4", 1500572039288, {2: V, 3: V}, F_, "LPS ativa macrófagos via CD14 e TLR4", 11, "Verdes: HY (1); 'LPS → TLR4 → inflamação' no slide 11."),
 au("disbiose-lps", "In <b>dysbiosis</b>, a leakier gut lets bacterial {{c1::LPS}} reach the blood and cause low-grade inflammation", {1: R}, F_,
    "Disbiose, LPS e inflamação de baixo grau", "11", "lateral", "nenhum card da endotoxemia metabólica nos acervos.", [1500572039288, 1487640028986],
    "Rosa: modelo de dieta hiperlipídica do slide 11 (pesquisa).", extra=F(11)),
]

EXCLUIDOS = [
 (1461615595492, "Vago e M3: redundante com 1482030356723"), (1474571591865, "H2 acoplado a Gs: redundante com 1461615074564"),
 (1461616559615, "Secreção com bloqueador H2: farmacologia"), (1461624946809, "IBP: farmacologia"),
 (1482021793271, "Teste da secretina no Zollinger-Ellison: diagnóstico"), (1462327862046, "Teste da secretina: diagnóstico"),
 (1482275742402, "Úlcera de Curling: fora da aula"), (1482275763392, "Úlcera de Cushing: fora da aula"),
 (1487640028986, "CD14 coreceptor: redundante com 1500572039288"), (1482369554930, "DII em mulheres jovens: epidemiologia fora do slide"),
]
FORA_DO_RECORTE = [
 "Doença inflamatória intestinal em detalhe (Crohn × colite ulcerativa): só citada no slide 10 como exemplo de disbiose",
 "Farmacologia antissecretora e diagnóstico do Zollinger-Ellison",
]

# F-20261003-CLAUDE-14: notas longas do Histology recortadas em cards de uma frase
from nebli.hx_cortes import recortar
from hx_cortes import CORTES
CARDS = recortar(CARDS, CORTES)

# F-20261003-CLAUDE-15: explicação curta no verso
from nebli.ilustrar import anotar
from notas import NOTAS
CARDS = anotar(CARDS, NOTAS)
