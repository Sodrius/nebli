# Especificação curada — Motilidade II (UC08 P1, Fisiologia, Profa. Fran Goulart da Silva; 15 lâminas, uma por página).
# Feita em 03/10/2026 a partir de planejamento.json (escrito antes). Ordem = slides. Critérios até F-20261003-CLAUDE-13.
# AnKing → outros acervos → autoral; os externos quase não cobrem a aula (busca/ext.txt), daí os autorais de deglutição,
# estômago, cólon e defecação, conferidos no Aires cap. 60.
RUN_ID = "uc08-fi09-20261003a"
SHORT = "fi09"
LESSON = "2026-uc08-fisiologia-09-motilidade-ii"
DECK = "NEBLI::UC08::P1::Fisiologia::Motilidade II"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261003-CLAUDE-13) + PLANO-GERACAO-ANO, 03/10/2026"
MEDIA = {f"nebli-uc08-fi09-p{p:02d}f.png": f"io/nebli-uc08-fi09-p{p:02d}f.png" for p in (3, 4, 6, 8, 9, 10, 11, 12, 13, 14)}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt, 39 consultas em 03/10); Referências Externas "
         "(MCAT, Histology, LLU, Dope, AnatoKing) pelos mesmos alvos (busca/ext.txt, 11 consultas): ")
F = lambda p, w=460: f'<img src="nebli-uc08-fi09-p{p:02d}f.png" width="{w}">'


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_, G_, H_ = ("A-eletrofisiologia", "B-mastigacao", "C-degluticao", "D-estomago-e-esvaziamento", "E-hormonios-do-esvaziamento",
                                  "F-intestino-delgado", "G-intestino-grosso-e-defecacao", "H-vomito")
CARDS = [
 # ---------- A. Eletrofisiologia do músculo liso (slides 2–4) ----------
 sh(1791023270450, "verde", A_, "Junções comunicantes: músculo liso unitário", 2, "Já vivo na FI08; 'músculo liso unitário' no slide 2."),
 ak("ondas-lentas", 1482022069057, {1: V}, A_, "Ondas lentas: oscilações do potencial de membrana", 2, "Verde: 'oscilações do PM = ondas lentas/REB' no slide 2."),
 ak("cajal", 1482022105272, {1: V}, A_, "Células intersticiais de Cajal são o marca-passo", 2, "Verde: HY (2); 'marca-passo do TGI' no slide 2."),
 ak("ondas-estomago", 1482022076569, {1: Z}, A_, "Estômago: 3 ondas por minuto", 2, "Azul: frequência por região (Aires; 'ondas lentas/min' no slide 2)."),
 ak("ondas-duodeno", 1482022079663, {1: Z}, A_, "Duodeno: 12 ondas por minuto", 2, "Azul: idem."),
 ak("ondas-ileo", 1482022081983, {1: R}, A_, "Íleo: 8 a 9 ondas por minuto", 2, "Rosa: idem, gradiente decrescente."),
 ak("ondas-canais", 1482022108336, {1: V, 2: Z}, A_, "Ondas lentas: canais de Ca2+ despolarizam, K+ repolariza", 3, "Verde c1: HY (2), 'ondas lentas dependem de canais catiônicos' no slide 3; azul c2."),
 au("limiar-eletrico", "A slow wave crossing the contractile threshold causes contraction, but <b>spike potentials</b> appear only above the {{c1::electrical}} threshold", {1: V}, A_,
    "Potenciais em pico só acima do limiar elétrico", "3; Aires cap. 60 (Fig. 60.3); Medicosis", "central",
    "AnKing só define a onda lenta e os canais; 'spike potential' e 'electrical threshold' sem card nos acervos.", [1482022069057, 1482022108336],
    "Verde: 'o que significa atingir o limiar contrátil ou elétrico?' no slide 3.", extra=F(3)),
 au("picos-forca", "The force of a GI smooth muscle contraction rises with the number of {{c1::spike potentials}} on each slow wave", {1: Z}, A_,
    "Mais potenciais na crista, mais força", "3; Aires cap. 60", "prova", "nenhum card nos acervos liga o número de picos à força.", [1482022069057, 1497378148913],
    "Azul: 'quanto maior número de PAs na crista da onda, maior força de contração' no slide 3.", extra=F(3)),
 au("ach-amplitude", "{{c1::Acetylcholine}} raises the amplitude of GI slow waves and the number of spikes on them, increasing contraction force", {1: Z}, A_,
    "SNE e SNA modulam amplitude e frequência", "4; Aires cap. 60 (p. 883)", "prova", "AnKing tem o efeito da atropina na motilidade, não sobre a onda lenta.", [1476919773069, 1482022069057],
    "Azul: 'como o SN potencializa a amplitude das ondas lentas?' no slide 4.", extra=F(4)),
 # ---------- B. Mastigação (slide 5) ----------
 ak("v3-mastigacao", 1480640329896, {1: Z}, B_, "V3 inerva os músculos da mastigação", 5, "Azul: 'n. trigêmeo, ramo mandibular' no slide 5."),
 ak("nucleo-motor-v", 1480874967562, {1: R}, B_, "Núcleo motor do trigêmeo", 5, "Rosa: 'núcleo motor / tronco encefálico' no slide 5."),
 ak("fechar-mandibula", 1480640336965, {1: Z, 2: Z, 3: Z, 4: Z}, B_, "Masseter, temporal e pterigoideo medial fecham a mandíbula", 5, "Azuis: 'principais músculos da mastigação' no slide 5."),
 ak("pterigoideo-lateral", 1480640340625, {1: Z}, B_, "Pterigoideo lateral abre a mandíbula", 5, "Azul: quarto músculo do slide 5."),
 # ---------- C. Deglutição (slide 6) ----------
 au("fase-oral", "The {{c1::oral}} phase is the only voluntary phase of swallowing", {1: V}, C_,
    "Fase oral voluntária, faríngea e esofágica reflexas", "6; Aires cap. 60 (Fig. 60.4); Apostila Guia", "central",
    "AnKing tem palato e epiglote na deglutição, sem as fases; MCAT e Histology sem o alvo.", [1482022111185, 1482022114115],
    "Verde: 'fase voluntária' × 'fases reflexas da deglutição' no slide 6.", extra=F(6), duplicacao_ok="resposta 'oral' coincide com o card das incretinas (glicose oral); assunto diferente"),
 ak("vago-degluticao", 1480640527660, {1: V}, C_, "Vago: deglutição e elevação do palato", 6, "Verde: HY (2); eferência do centro da deglutição (Aires)."),
 ak("nucleo-ambiguo", 1480875955623, {1: R}, C_, "Núcleo ambíguo: motor da faringe e do esôfago superior", 6, "Rosa: 'tronco encefálico, motor' no slide 6."),
 ak("palato-mole", 1482022111185, {1: Z}, C_, "Palato mole sobe e fecha a nasofaringe", 6, "Azul: passo 1 da fase faríngea no slide 6."),
 ak("epiglote", 1482022114115, {1: Z}, C_, "Epiglote fecha a laringe", 6, "Azul: passo 3 da fase faríngea no slide 6."),
 au("respiracao-inibida", "During the pharyngeal phase of swallowing, the swallowing center in the medulla briefly {{c1::inhibits}} breathing", {1: Z}, C_,
    "Supressão neural da respiração", "6; Aires cap. 60 (p. 884)", "prova", "nenhum card nos acervos sobre a pausa respiratória da deglutição.", [1482022114115, 1480640527660],
    "Azul: passo 4 da fase faríngea no slide 6."),
 ak("vip-eei-degluticao", 1482022131650, {1: Z}, C_, "VIP relaxa o EEI na deglutição", 6, "Azul: 'relaxamento do EEI' na fase esofágica (slide 6)."),
 au("peristalse-secundaria", "<b>Secondary peristalsis</b> of the esophagus is triggered by {{c1::distension}} from food left behind by the primary wave", {1: V}, C_,
    "Peristalse secundária: distensão, SNE", "6; Aires cap. 60 (p. 885); Apostila Guia", "central", "zero card sobre peristalse primária × secundária no AnKing e nos externos.",
    [1482022169992, 1482022134697], "Verde: 'peristalse secundária, não faz parte do reflexo' no slide 6."),
 # ---------- D. Estômago (slides 8–9) ----------
 ak("relaxamento-receptivo", 1482022134697, {1: V}, D_, "Relaxamento receptivo vagovagal", 8, "Verde: 'nervo vago e o relaxamento receptivo' no slide 8."),
au("sistole-antral", "In <b>antral systole</b>, the antrum contracts against a closed pylorus, causing {{c1::retropulsion}} of chyme into the body", {1: V}, D_,
    "Sístole antral e retropropulsão", "9; Aires cap. 60 (p. 888)", "central", "'retropulsion' e 'antral' sem card nos acervos.", [1482022155210, 1482022134697],
    "Verde: 'sístole antral, retropropulsão do quimo' no slide 9.", extra=F(9)),
 sh(1790999271207, "azul", D_, "Piloro relaxa à frente da onda antral e contrai com o quimo no duodeno", 9, "Já vivo na FI08; 'regulação antral-anterógrada e duodenal-retrógrada' repetida no slide 9."),
 ak("gastrina-motilidade", 1482021707646, {1: Z}, D_, "Gastrina aumenta a motilidade gástrica", 9, "Azul: gastrina na lista do slide 9."),
 ak("secretina-piloro", 1482021903019, {1: V}, D_, "Secretina contrai o piloro", 9, "Verde: primeiro hormônio da lista 'promove contração do piloro' no slide 9."),
 ak("cck-esvaziamento", 1482021853417, {1: V}, D_, "CCK retarda o esvaziamento gástrico", 9, "Verde: CCK na lista do slide 9."),
 sh(1790979869860, "verde", D_, "Grelina aumenta o apetite", 9, "Já vivo na BT03; 'promove relaxamento do piloro: grelina' no slide 9."),
 au("grelina-piloro", "{{c1::Ghrelin}} relaxes the pylorus and speeds gastric emptying, unlike secretin and CCK, which contract it", {1: Z}, D_,
    "Grelina relaxa o piloro; os demais contraem", "9 (Camilleri, Gastrointestinal Hormones and Regulation of Gastric Emptying)", "prova",
    "AnKing tem grelina só no apetite; nenhum card do efeito no piloro.", [1482022013033, 1482021903019], "Azul: as duas listas do slide 9.", extra=F(9)),
 # ---------- E. Hormônios do esvaziamento (slide 10) ----------
 ak("gordura-h", 1482022155210, {1: V, 2: V}, E_, "Gordura e H+ no duodeno retardam o esvaziamento", 10, "Verdes: 'acidez do quimo' e 'nutrientes digeridos' no slide 10."),
 ak("secretina-s", 1482021883479, {1: V, 2: Z}, E_, "Secretina das células S do duodeno", 10, "Verde c1: '(+) secreção de secretina (S)' no slide 10; azul c2."),
 ak("secretina-estimulo", 1482021911657, {1: V}, E_, "H+ e ácidos graxos liberam secretina", 10, "Verde: 'acidez do quimo' no slide 10."),
 ak("cck-i", 1482021827543, {1: V, 2: Z}, E_, "CCK das células I", 10, "Verde c1: 'CCK (I)' no slide 10; azul c2."),
 ak("cck-estimulo", 1482021864452, {2: Z}, E_, "Ácidos graxos e aminoácidos liberam CCK", 10, "Azul: 'nutrientes digeridos' no slide 10."),
 ak("gip-k", 1482021920866, {1: V, 2: Z}, E_, "GIP das células K", 10, "Verde c1: 'GIP (K)' no slide 10; azul c2."),
 ak("incretinas", 1482021939459, {1: Z, 2: V}, E_, "GIP e GLP-1 aumentam a insulina após glicose oral", 10, "Verde c2: HY (2), '↑GLP-1/2, ↑GIP: insulina' no slide 10; azul c1."),
 au("glp1-l", "<b>GLP-1</b> is released by intestinal {{c1::L}} cells in response to digested nutrients and promotes satiety and insulin release", {1: Z}, E_,
    "GLP-1 das células L: saciedade e insulina", "10; Aires cap. 60", "prova", "AnKing traz o GLP-1 só como incretina e fármaco, sem a célula L; PYY tem a célula L, não o GLP-1.",
    [1482022025284, 1482021920866], "Azul: '(+) secreção de GLP-1/GLP-2/PYY (L)' e 'saciedade' no slide 10.", extra=F(10)),
 ak("pyy", 1482022025284, {1: Z}, E_, "PYY das células L diminui o apetite", 10, "Azul: PYY no slide 10."),
 # ---------- F. Intestino delgado (slide 11) ----------
 ak("segmentacao", 1482022169992, {1: V}, F_, "Segmentação mistura, sem avanço", 11, "Verde: 'segmentações, mistura e renovação' no slide 11."),
 au("ileocecal", "When peristalsis reaches the terminal ileum, the {{c1::ileocecal}} sphincter relaxes", {1: Z}, F_,
    "Relaxamento do esfíncter ileocecal", "11; Aires cap. 60 (p. 896)", "prova", "AnKing cita o ileocecal só no Extra das contrações tônicas.", [1482022061641, 1482022169992],
    "Azul: 'relaxamento do esfíncter ileocecal' no slide 11.", extra=F(11)),
ak("motilina-cmm", 1482021953235, {1: V, 2: V}, F_, "Motilina inicia o complexo motor migratório", 11, "Verdes (calibração Ninja Nerd, F-14): CMM de jejum é ponto central da motilidade do delgado; era azul."),
 ak("motilina-jejum", 1482021949414, {1: R}, F_, "Motilina no jejum", 11, "Rosa: CMM entre as refeições."),
 # ---------- G. Intestino grosso e defecação (slides 12–13) ----------
 au("haustracoes", "{{c1::Haustrations}} mix the contents of the proximal colon and expose them to the mucosa for water absorption", {1: V}, G_,
    "Haustrações: mistura e absorção de água", "12; Aires cap. 60 (resumo do cólon); Ninja Nerd", "central", "haustros só em card de colite ulcerativa no AnKing; MCAT sem o alvo.",
    [1482022169992, 1482374278670], "Verde: 'haustrações, cólon proximal: absorção água/eletrólitos' no slide 12.", extra=F(12)),
 au("movimento-massa", "{{c1::Mass movements}}, a few times a day, push feces from the colon into the rectum", {1: V}, G_,
    "Movimentos de massa levam fezes ao reto", "12; Aires cap. 60; Ninja Nerd", "central", "'mass movement' sem card nos acervos.", [1482022169992, 1461634773558],
    "Verde: 'movimentos de massa, 3–4×/dia, fezes para o reto' no slide 12.", extra=F(12)),
 au("gastrocolico", "Food entering the stomach triggers the {{c1::gastrocolic}} reflex, which increases colonic mass movements", {1: V}, G_,
    "Reflexo gastrocólico", "12; Aires cap. 60; Ninja Nerd", "central", "'gastrocolic' sem card no AnKing nem nos externos.", [1482022134697, 1482021707646],
    "Verde: 'reflexo gastrocólico (SNA, CCK, gastrina)' no slide 12.", extra=F(12)),
 au("reflexo-defecacao", "Rectal distension triggers a sacral reflex through the {{c1::pelvic}} nerves that contracts the rectum and relaxes the internal anal sphincter", {1: V}, G_,
    "Reflexo da evacuação: medula sacral, nervo pélvico", "13; Aires cap. 60 (resumo do cólon); Ninja Nerd", "central", "'defecation reflex' sem card nos acervos.",
    [1486767218479, 1482021615074], "Verde: esquema do reflexo da evacuação no slide 13.", extra=F(13)),
 ak("parassimpatico-tgi", 1482021615074, {1: Z}, G_, "Vago e esplâncnicos pélvicos levam o parassimpático ao tubo", 13, "Azul: 'nn parassimpático, nervo pélvico' no slide 13."),
 sh(1790974699358, "azul", G_, "Esfíncter anal interno: liso, involuntário", 13, "Já vivo na AN02; 'relaxamento do EAI, involuntário' no slide 13."),
 sh(1790974699480, "azul", G_, "Esfíncter anal externo: esquelético, voluntário", 13, "Já vivo na AN02; 'relaxamento do EAE, voluntário' no slide 13."),
 sh(1790974694881, "azul", G_, "Puborretal mantém a flexura anorretal", 13, "Já vivo na AN02; 'relaxamento do mm puborretal' no slide 13."),
 sh(1790974695006, "rosa", G_, "Dissinergia evacuatória", 13, "Já vivo na AN02; falha do relaxamento do puborretal."),
 # ---------- H. Vômito (slide 14) ----------
 ak("area-postrema-local", 1461597624636, {1: Z}, H_, "Área postrema junto ao NTS no 4º ventrículo", 14, "Azul: '1- área postrema' no slide 14."),
 ak("area-postrema-emeticos", 1461597712293, {1: V}, H_, "Área postrema responde a emetogênicos", 14, "Verde: HY (1); fármacos e quimioterapia como estímulo no slide 14."),
 ak("nts-vomito", 1461597220648, {1: Z}, H_, "NTS recebe as aferências do vômito", 14, "Azul: 'integrador (tronco)' no slide 14."),
 ak("nts-coordena", 1461597313002, {1: Z}, H_, "NTS coordena a resposta do vômito", 14, "Azul: sequência dos efetores do slide 14."),
]

EXCLUIDOS = [
 (1482022084524, "Região com menor frequência de ondas lentas: redundante com a frequência do estômago"), (1482022097240, "Maior frequência: redundante com a do duodeno"),
 (1480640343976, "Lesão do V3 desvia a mandíbula: clínica fora da aula"), (1480876216467, "Reflexo mandibular: fora da aula"),
 (1482021955784, "Eritromicina como agonista da motilina: farmacologia"), (1505674402155, "Eritromicina e diarreia: farmacologia"),
 (1482021831523, "CCK e secreção pancreática: secreções, P2"), (1482021838448, "CCK e vesícula: fígado e vias biliares, P2"),
 (1482021886990, "Secretina e HCO3- pancreático: secreções, P2"), (1482021942521, "GIP e secreção de H+: secreções, P2"),
 (1462849402751, "Análogos de GLP-1: farmacologia"), (1461597220648 + 0, ""),
]
EXCLUIDOS = [e for e in EXCLUIDOS if e[1]]
FORA_DO_RECORTE = [
 "Vídeo do slide 7 (sem conteúdo próprio)",
 "Secreções gástrica, pancreática e biliar dos hormônios (P2)",
 "Antieméticos e procinéticos (farmacologia)",
 "Absorção intestinal: o título da aula fala em absorção, mas os slides não trazem o tema",
]

# F-20261003-CLAUDE-15: explicação curta no verso
from nebli.ilustrar import anotar
from notas import NOTAS
CARDS = anotar(CARDS, NOTAS)
