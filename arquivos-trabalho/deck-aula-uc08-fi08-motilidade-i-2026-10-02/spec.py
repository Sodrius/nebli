# Especificação curada — Motilidade I (UC08 P1, Fisiologia, Profa. Fran Goulart da Silva; 6 lâminas, uma por página).
# Feita em 03/10/2026 a partir de planejamento.json (escrito antes). Ordem = slides. Critérios até F-20261003-CLAUDE-13:
# AnKing → outros acervos (Histology = Junqueira) → autoral; deslizamento e excitação-contração do Aires cap. 59–60.
RUN_ID = "uc08-fi08-20261003a"
SHORT = "fi08"
LESSON = "2026-uc08-fisiologia-08-motilidade-i"
DECK = "NEBLI::UC08::P1::Fisiologia::Motilidade I"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261003-CLAUDE-13) + PLANO-GERACAO-ANO, 03/10/2026"
MEDIA = {f"nebli-uc08-fi08-p{p:02d}f.png": f"io/nebli-uc08-fi08-p{p:02d}f.png" for p in (3, 4, 5, 6)}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt, 35 consultas em 03/10); Referências Externas "
         "(Histology, LLU, MCAT, Ankisthesia, Dope) pelos mesmos alvos (busca/ext.txt, 13 consultas): ")
F = lambda p, w=460: f'<img src="nebli-uc08-fi08-p{p:02d}f.png" width="{w}">'


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    """Nota do acervo com só os clozes do plano (os demais ficam como texto visível)."""
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_ = "A-inervacao", "B-reflexos-e-neurotransmissores", "C-esfincteres-e-contracao", "D-acoplamento-excitacao-contracao", "E-sinalizacao-e-sensibilizacao"
CARDS = [
 # ---------- A. Inervação intrínseca e extrínseca (slide 2) ----------
 sh(1790972063876, "azul", A_, "Terço superior do esôfago estriado, resto liso", 2, "Já vivo na AN01; 'músculo esquelético (1/3), músculo liso (2/3)' no slide 2."),
 ak("ens-autonomo", 1482021669311, {1: V}, A_, "SNE comanda o tubo mesmo sem inervação extrínseca", 2, "Verde: HY (2); 'mini-cérebro' do tubo (Aires cap. 59; Dr Mike)."),
 ak("mioenterico-local", 1482021572867, {1: V}, A_, "Plexo mioentérico entre as camadas circular e longitudinal", 2, "Verde: HY (1); 'plexo mioentérico, mm circular e longitudinal' no slide 2."),
 sh(1790979864785, "verde", A_, "Plexo mioentérico controla a motilidade", 2, "Já vivo na BT03; 'contração/relaxamento' do plexo mioentérico no slide 2."),
 ak("submucoso-local", 1482021579186, {1: V}, A_, "Plexo submucoso entre a submucosa e a circular interna", 2, "Verde: HY (1); 'plexo submucoso, secreção' no slide 2."),
 sh(1790979864034, "verde", A_, "Plexo submucoso controla secreção e fluxo", 2, "Já vivo na BT03; '-secreção-' no slide 2."),
 ak("extrinseco-sinapses", 1482021663832, {1: Z}, A_, "Fibras simpáticas e parassimpáticas fazem sinapse nos plexos", 2, "Azul: integração da inervação intrínseca com a extrínseca (slides 2–3; Aires)."),
 ak("atropina-motilidade", 1476919773069, {1: V}, A_, "Bloquear o parassimpático (atropina) diminui a motilidade", 2, "Verde: HY (2); 'parassimpático (estimulação)' no slide 2, pelo efeito da atropina."),
 au("simpatico-inibe", "<b>Sympathetic</b> activity {{c1::inhibits}} GI motility and secretion but contracts the sphincters", {1: V}, A_,
    "Simpático inibe motilidade e secreção, contrai esfíncteres", "2; Aires cap. 59; Dr Mike; Medicosis", "central",
    "AnKing só tem o efeito da atropina (parassimpático) e o íleo; nenhum card do simpático na motilidade; Histology e MCAT sem o alvo.", [1476919773069, 1482021663832],
    "Verde: 'simpático (inibição)' no slide 2; par do parassimpático."),
 # ---------- B. Reflexos e neurotransmissores (slide 3) ----------
 au("reflexo-curto", "A {{c1::short}} (intramural) <b>reflex</b> runs entirely within the gut wall, from mechanoreceptors to <b>enteric plexus</b> neurons", {1: V}, B_,
    "Reflexo curto ou intramural", "3; Aires cap. 59 (Fig. 59.4)", "central", "AnKing só tem o reflexo vagovagal; 'short reflex', 'intramural' e 'local reflex' sem card nos acervos.",
    [1482021618596, 1482021669311], "Verde: 'reflexo curto, reflexo intramural' no slide 3.", extra=F(3)),
 ak("vagovagal", 1482021618596, {1: V}, B_, "Reflexo longo vagovagal", 3, "Verde: 'reflexo longo, reflexo vago-vagal' no slide 3."),
 ak("vip-relaxa", 1482022030441, {1: V}, B_, "VIP relaxa o músculo liso e os esfíncteres", 3, "Verde: 'nn inibitório – VIP' no slide 3."),
 ak("vip-parassimpatico", 1482022027494, {1: Z}, B_, "VIP vem de neurônios parassimpáticos", 3, "Azul: origem do VIP (Aires Quadro 59.1)."),
 ak("vip-distensao", 1482022039214, {1: R}, B_, "Distensão e vago aumentam o VIP", 3, "Rosa: estímulos do VIP (enchimento do tubo no slide 3)."),
 ak("no-relaxa", 1486831442651, {1: V}, B_, "NO relaxa o músculo liso e os esfíncteres", 3, "Verde: NO entre os neuromediadores do slide 3; par do VIP."),
 ak("no-gmpc", 1497378335881, {1: R}, B_, "NO ativa a guanilil ciclase (GMPc)", 3, "Rosa: como o NO relaxa (liga com a fosfatase do slide 5)."),
 au("peristalse-polaridade", "During peristalsis, the circular muscle on the oral side of the bolus {{c1::contracts}} while the segment just aboral to it relaxes", {1: V}, B_,
    "Reflexo peristáltico: contrai atrás, relaxa à frente", "3; Aires cap. 59; Ninja Nerd (Enteric Nervous System)", "central",
    "AnKing e externos sem o reflexo peristáltico ('peristalsis' com oral/aboral, ACh, substância P: 0 notas; busca de 03/10 na calibração F-14).",
    [1482022183423, 1482022030441], "Verde: 'nn excitatório – ACh, nn inibitório – VIP, contração e relaxamento' no slide 3; o Ninja Nerd dá o reflexo como o núcleo do SNE (calibração F-14).",
    extra="Behind the bolus, excitatory motor neurons release acetylcholine and substance P. Ahead of it, inhibitory neurons release VIP and NO."),
 ak("serotonina-peristalse", 1482022183423, {1: Z}, B_, "Serotonina nos neurônios aferentes inicia a peristalse", 3, "Azul: serotonina listada no slide 3; reflexo peristáltico (Aires Fig. 59.5)."),
 sh(1790972065836, "verde", B_, "Chagas: megacólon e megaesôfago", 3, "Já vivo na AN01/AN02; frase do slide 3."),
 sh(1790972065961, "verde", B_, "Chagas destrói o plexo mioentérico", 3, "Já vivo na AN01; 'o T. cruzi destrói o plexo mioentérico' no slide 3."),
 sh(1790972066061, "verde", B_, "Acalasia secundária a Chagas", 3, "Já vivo na AN01; megaesôfago chagásico é acalasia."),
 ak("acalasia-eei", 1482203787030, {1: V, 2: Z}, B_, "Acalasia: EEI não relaxa", 3, "Verde c1: HY (1), clínica de encaixe direto com o neurônio inibitório e o esfíncter (slides 3–4); azul c2: o nome da doença."),
 ak("acalasia-plexo", 1482203793099, {1: V}, B_, "Acalasia primária: perda de neurônios do plexo mioentérico", 3, "Verde: liga o plexo e os inibitórios NO/VIP à doença."),
 ak("acalasia-no-vip", 1482343170021, {1: Z}, B_, "Na acalasia faltam NO e VIP", 3, "Azul: os dois neurotransmissores inibitórios do slide 3."),
 ak("hirschsprung-ganglios", 1482886567135, {1: V, 2: Z}, B_, "Hirschsprung: falta de células ganglionares nos plexos", 3, "Verde c1: HY (1), ausência do SNE no cólon distal (Aires cap. 60), contraponto ao Chagas; azul c2: nome da doença."),
 # ---------- C. Esfíncteres e tipos de contração (slide 4) ----------
 ak("fasica", 1482022053859, {1: V}, C_, "Contração fásica: periódica, com relaxamento", 4, "Verde: 'contração fásica' no slide 4 (corpo do esôfago, antro, intestinos)."),
 ak("tonica", 1482022061641, {1: V}, C_, "Contração tônica: mantida, nos esfíncteres e no fundo", 4, "Verde: 'contração tônica' no slide 4."),
 sh(1790972064160, "azul", C_, "Esfíncter esofágico superior", 4, "Já vivo na AN01; EES no slide 4."),
 sh(1790972065536, "azul", C_, "Esfíncter esofágico inferior", 4, "Já vivo na AN01; EEI no slide 4."),
 sh(1791023359842, "azul", C_, "Esfíncter pilórico: espessamento da camada circular", 4, "Já vivo na BT03; P no slide 4."),
 sh(1791052036733, "azul", C_, "Esfíncter anal interno: músculo liso", 4, "Já vivo na AN02; EAI no slide 4."),
 sh(1790974699480, "azul", C_, "Esfíncter anal externo: músculo esquelético", 4, "Já vivo na AN02; EAE no slide 4."),
 au("esfincter-distensao", "<b>Distension</b> of the segment just before a GI <b>sphincter</b> makes that sphincter {{c1::relax}}", {1: V}, C_,
    "Distensão do tubo relaxa o esfíncter adiante", "4; Aires cap. 59–60", "central", "AnKing só tem o relaxamento receptivo do estômago (FI09); Histology e MCAT sem o alvo.",
    [1482022134697, 1482022030441], "Verde: 'distensão do tubo = relaxamento dos esfíncteres' no slide 4.", extra=F(4)),
 au("piloro-regulacao", "The <b>pylorus</b> relaxes ahead of each antral peristaltic wave, but chyme arriving in the duodenum makes it {{c1::contract}}", {1: Z}, C_,
    "Piloro: regulação antral anterógrada e duodenal retrógrada", "4; Aires cap. 60, p. 888 (o piloro relaxa à frente das contrações antrais; quimo no duodeno o contrai)", "prova", "AnKing tem só o efeito de gordura e H+ no esvaziamento, sem o piloro.",
    [1482022155210, 1482022134697], "Azul: 'regulação antral-anterógrada (relaxamento), duodenal-retrógrada (contração)' no slide 4.", extra=F(4)),
 # ---------- D. Junção neuroefetora e acoplamento excitação-contração (slide 5) ----------
 ak("varicosidades", 1701640720206, {1: Z, 3: Z}, D_, "Varicosidades liberam ACh ou noradrenalina sobre o músculo liso", 5,
    "Azuis: 'junção neuroefetora' com varicosidades no slide 5 (Junqueira cap. 10; Aires Fig. 60.1).", origin="Histology"),
 ak("juncoes-comunicantes", 1701640783272, {1: V}, D_, "Junções comunicantes fazem o músculo liso contrair junto", 5,
    "Verde: músculo liso visceral unitário é um sincício (Aires cap. 60); base da contração coordenada.", origin="Histology"),
 ak("ca-calmodulina", 1497378148913, {1: V, 3: Z}, D_, "Ca2+ entra por canal L e liga a calmodulina", 5, "Verde c1: 'Ca2+/CAM' no slide 5; azul c3: canal tipo L."),
 ak("mlck", 1497378477763, {1: V}, D_, "Ca2+-calmodulina ativa a MLCK, que fosforila a miosina", 5, "Verde: HY (1); 'miosina-K → contração' no slide 5."),
 ak("sem-troponina", 1701639573483, {1: Z}, D_, "Músculo liso não usa troponina", 5, "Azul: contraste com o esquelético (Junqueira cap. 10; Dr Mike).", origin="Histology"),
 ak("ca-remocao-mcat", 1715879950299, {1: Z}, D_, "Recaptação do Ca2+ pela SERCA no relaxamento", 5, "Azul: 'extrusão' e 'RES Ca2+ ATPase' no slide 5. F-18: card do AnKing-MCAT achado na nova busca substitui o autoral; cloze encurtado para a sigla.", origin="MCAT", text="Following muscle contraction, {{c1::SERCA}} pumps calcium back into the sarcoplasmic reticulum to restore the calcium gradient", extra=""),
 ak("fosfatase", 1472747780684, {1: V, 2: V}, D_, "Fosfatase desfosforila a miosina e relaxa", 5, "Verdes: HY (1); '(+) miosina fosfatase' no slide 5."),
 # ---------- E. Sinalização intracelular (slide 6) ----------
 ak("m3-liso", 1475115110904, {1: V}, E_, "Receptor M3 no músculo liso", 6, "Verde: HY (1); GPCR do slide 6 para a ACh."),
 ak("m3-gq", 1475114985396, {1: V}, E_, "M3 acoplado a Gq", 6, "Verde: HY (2); 'Gq/11 → PLCβ' no slide 6."),
 ak("ip3-ca", 1461857362486, {1: V, 2: V}, E_, "IP3 libera Ca2+ do retículo", 6, "Verdes: HY (1); 'IP3 → RS → Ca2+' no slide 6."),
 au("rho-quinase", "<b>RhoA</b> activates {{c1::Rho kinase}}, which inhibits <b>myosin light chain phosphatase</b> and raises the Ca<sup>2+</sup> sensitivity of smooth muscle", {1: Z}, E_,
    "RhoA/ROK inibe a fosfatase (sensibilização ao Ca2+)", "6", "prova", "zero resultado para Rho kinase, RhoA, ROCK e fasudil no AnKing e nos externos.",
    [1472747780684, 1497378477763], "Azul: 'inibição da sinalização intracelular do relaxamento' no slide 6.", extra=F(6)),
]

EXCLUIDOS = [
 (1482021594676, "Meissner na submucosa: já vivo na BT03 e coberto pelo card da localização"), (1482021603417, "Auerbach na muscular externa: idem"),
 (1486831439445, "NO também relaxa: redundante com 1486831442651"), (1509815200893, "Chagas e acalasia: já vivo na AN01 (1482203795669)"),
 (1482022134697, "Relaxamento receptivo: estômago, FI09"), (1482022069057, "Ondas lentas e células de Cajal: FI09 (slides 2–3 da aula 2)"),
 (1482959856768, "Colinérgicos no íleo: tratamento; atropina já ensina o papel do parassimpático"), (1559494486589, "MCAT junções comunicantes: redundante com o Histology"),
 (1482022036640, "VIP aumenta secreção intestinal: secreção, P2"), (1482878964408, "Hirschsprung no reto e sigmoide: um card do mecanismo basta"),
 (1505174270651, "Esclerodermia: doença fora da aula"), (1482203808143, "Acalasia na manometria: diagnóstico, fora do recorte"),
 (1486767218479, "Nervos esplâncnicos pélvicos: anatomia da inervação (AN14, P2)"), (1521770267740, "Espasmo esofágico difuso: doença fora da aula"),
]
FORA_DO_RECORTE = [
 "Ondas lentas, potenciais de ação e células intersticiais de Cajal: aula 2 (FI09, slides 2–4)",
 "Deglutição, motilidade gástrica, intestinal e defecação: FI09",
 "Hormônios gastrintestinais que regulam o esvaziamento: FI09 (slides 9–10) e secreções (P2)",
 "Tratamento da acalasia e de Hirschsprung, sorologia do Chagas",
]

# F-20261003-CLAUDE-14: notas longas do Histology recortadas em cards de uma frase
from nebli.hx_cortes import recortar
from hx_cortes import CORTES
CARDS = recortar(CARDS, CORTES)

# F-20261003-CLAUDE-15: explicação curta no verso
from nebli.ilustrar import anotar
from notas import NOTAS
CARDS = anotar(CARDS, NOTAS)
