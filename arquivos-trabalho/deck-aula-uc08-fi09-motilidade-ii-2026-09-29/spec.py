# Especificação curada da FI09 (run uc08-fi09-20260929a). Somente cards, sem E1. Novos cards em inglês.
RUN_ID = "uc08-fi09-20260929a"
SHORT = "fi09"
LESSON = "2026-uc08-fisiologia-09-motilidade-absorcao-intestinal-ii"
DECK = "NEBLI::UC08::P1::Fisiologia::Motilidade e absorção intestinal II"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20260929-CLAUDE-02) + EXECUCAO-DECK-AULA + RECONSTRUCAO-UC08, 29/09/2026"

MEDIA = {
    "nebli-uc08-fi09-s03-ondas.png": "fontes/s03_ondas.png",
    "nebli-uc08-fi09-s09-esvaziamento.png": "fontes/s09_esvaz.png",
    "nebli-uc08-fi09-s12-colon.png": "fontes/s12_colon.png",
    "nebli-uc08-fi09-s13-evacuacao-v2.png": "fontes/s13_evac2.png",
}
CR = '<br><span style="font-size: 10pt;"><em>{}</em></span>'
SLIDE = lambda f, ref, w=460: f'<img src="{f}" width="{w}">' + CR.format(f"Figure from the lecture slides (Goulart da Silva, UC08 Physiology); {ref}")

def ak(key, src, flags, bloco, alvo, evid, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=evid, uso=kw.pop("uso", "Fisiologia GI; Step 1."), motivo=motivo, **kw)

CARDS = [
 # ---------- ELETROFISIOLOGIA ----------
 ak("ondas-lentas", 1482022069057, {1: 3}, "A-eletro", "Ondas lentas = oscilações do potencial de membrana", "Slides 2–3", "Verde."),
 ak("cajal", 1482022105272, {1: 3}, "A-eletro", "Células intersticiais de Cajal = marca-passo", "Slide 2", "Verde (2-RelativelyHighYield)."),
 ak("ondas-ionica", 1482022108336, {1: 4, 2: 4}, "A-eletro", "Base iônica da onda lenta", "Slides 2–3", "Azul.",
    extra_prefix='In the lecture: slow waves depend on cation channels (Ca²⁺, Na⁺, K⁺); L-type Ca²⁺ channels do not generate the slow wave — they fire the spike potentials on its crest.<br><br>',
    correcao="Formulação AnKing (Ca²⁺→K⁺) mantida (Q027); nuance do slide (canais catiônicos; tipo L só nos picos) acrescentada no verso."),
 dict(key="picos-forca", kind="autoral", flags={1: 3, 2: 4}, bloco="A-eletro",
  text=('GI smooth muscle contracts only when a slow wave reaches threshold and fires {{c1::spike (action) potentials}}; '
        'the more spikes on the crest of a wave, the {{c2::stronger}} the contraction'),
  extra=('Slow waves set the maximum frequency of contraction; stretch of the wall, the enteric and autonomic (parasympathetic) nervous systems raise their amplitude, '
         'so more waves reach threshold.<br><br>' + SLIDE("nebli-uc08-fi09-s03-ondas.png", "slow waves, spike potentials and contractile force", 600)),
  alvo="Limiar, potenciais em pico e força; SN potencializa amplitude", evid="Slides 3–4", uso="Base de toda a motilidade.",
  motivo="c1 verde; c2 azul.", busca="AnKing 1482022069057 só no Extra ('determine the rate'); nenhum card cobra pico × força; lacuna."),
 ak("freq-estomago", 1482022076569, {1: 4}, "A-eletro", "Estômago 3 ondas/min", "Slide 2 ('ondas lentas/min')", "Azul (5-LowYield)."),
 ak("freq-duodeno", 1482022079663, {1: 4}, "A-eletro", "Duodeno 12 ondas/min", "Slide 2", "Azul."),
 # ---------- MASTIGAÇÃO E DEGLUTIÇÃO ----------
 ak("mastigacao-v3", 1480640329896, {1: 3}, "B-deglutição", "V3 inerva os músculos da mastigação", "Slide 5 (n. trigêmeo, ramo mandibular)", "Verde (1-HighYield)."),
 ak("mastigacao-musculos", 1480640336965, {1: 4, 2: 4, 3: 4, 4: 4}, "B-deglutição", "Masseter, temporal, pterigóideo medial fecham a mandíbula", "Slide 5 (principais músculos)", "Azul.",
    extra_prefix='The lateral pterygoid opens the jaw. Sensory feedback from the mouth adjusts force, direction and number of chewing strokes.<br><br>'),
 ak("palato-mole", 1482022111185, {1: 3}, "B-deglutição", "Palato mole sobe (bloqueia nasofaringe)", "Slide 6 (fase faríngea 1)", "Verde."),
 ak("epiglote", 1482022114115, {1: 3}, "B-deglutição", "Epiglote fecha a laringe", "Slide 6 (fase faríngea 3)", "Verde."),
 ak("vago-degluticao", 1480640527660, {1: 4}, "B-deglutição", "Vago (CN X) na deglutição/palato", "Slide 6 (tronco encefálico)", "Azul."),
 dict(key="fases-degluticao", kind="autoral", flags={1: 3, 2: 4}, bloco="B-deglutição",
  text=('Swallowing starts with a {{c1::voluntary}} oral phase; the pharyngeal and esophageal phases are {{c2::reflex}}, coordinated by the brainstem swallowing center'),
  extra=('Pharyngeal phase: soft palate elevates, pharyngeal constrictors contract, the laryngeal opening closes and breathing is briefly inhibited; then the UES relaxes. '
         'Esophageal phase: UES contracts again, primary peristalsis runs down, and the LES and gastric fundus relax.'),
  alvo="Fases da deglutição e integração no tronco", evid="Slides 5–6", uso="Disfagia; aspiração (futuro).", motivo="c1 verde; c2 azul.",
  busca="AnKing cobre palato/epiglote/VIP no EEI, não as fases; lacuna."),
 dict(key="peristalse-secundaria", kind="autoral", flags={1: 4}, bloco="B-deglutição",
  text='If a bolus remains in the esophagus after primary peristalsis, local distension triggers {{c1::secondary}} peristalsis, which is not part of the swallowing reflex',
  extra='It is organized by the enteric nervous system and vagal reflexes, clearing residue and refluxed material.',
  alvo="Peristalse secundária", evid="Slide 6 ('peristalse secundária – não faz parte do reflexo')", uso="Clearance esofágico; DRGE.", motivo="Azul.",
  busca="Nenhum acervo; lacuna."),
 ak("vip-eei", 1482022131650, {1: 4}, "B-deglutição", "VIP relaxa o EEI na deglutição", "Slide 6 (relaxamento do EEI)", "Azul (FI08 cobre VIP/NO em geral)."),
 # ---------- ESTÔMAGO ----------
 ak("relaxamento-receptivo", 1482022134697, {1: 3}, "C-estomago", "Relaxamento receptivo (vagovagal)", "Slide 8", "Verde.",
    extra_prefix='It lets the stomach store 1–1.5 L with little rise in pressure; after vagotomy, pressure rises at much smaller volumes.<br><br>'),
 ak("caudal-mistura", 1482022152555, {1: 4}, "C-estomago", "Região caudal faz as contrações de mistura", "Slide 9 (sístole antral)", "Azul."),
 dict(key="sistole-antral", kind="autoral", flags={1: 3}, bloco="C-estomago",
  text=('During antral systole, the peristaltic wave reaches the pylorus as it closes, so most chyme is pushed back into the body ({{c1::retropulsion}}), mixing and grinding it'),
  extra='Only a small amount passes to the duodenum with each wave, matching emptying to the duodenum\'s processing capacity.<br><br>' + SLIDE("nebli-uc08-fi09-s09-esvaziamento.png", "gastric emptying", 400),
  alvo="Sístole antral e retropropulsão", evid="Slide 9", uso="Esvaziamento; gastroparesia (futuro).", motivo="Verde.",
  busca="AnKing só orad/caudad; lacuna."),
 ak("secretina-piloro", 1482021903019, {1: 4}, "C-estomago", "Secretina ↑ contração do piloro, ↓ ácido", "Slides 9–10", "Azul (acidez no card verde de esvaziamento, FI08)."),
 ak("cck-esvaziamento", 1482021853417, {1: 3}, "C-estomago", "CCK ↓ esvaziamento gástrico", "Slides 9–10", "Verde (HY)."),
 dict(key="celulas-hormonios", kind="autoral", flags={1: 4, 2: 4, 3: 4, 4: 4}, bloco="C-estomago",
  text=('Duodenal acid stimulates {{c1::S}} cells to release secretin; digested nutrients stimulate {{c2::I}} cells (CCK), {{c3::K}} cells (GIP) and {{c4::L}} cells (GLP-1, GLP-2, PYY)'),
  extra='Together they relax the stomach and contract the pylorus, slowing emptying to the rate the duodenum can handle; ghrelin, in contrast, relaxes the pylorus.',
  alvo="Células enteroendócrinas → hormônios do esvaziamento", evid="Slides 9–10", uso="Hormônios GI (P2 secreções).", motivo="Azul.",
  busca="AnKing só PYY/L cell; lacuna para S/I/K."),
 ak("cck-vesicula", 1482021838448, {1: 4}, "C-estomago", "CCK contrai a vesícula", "Slide 10 (CCK)", "Azul (secreções são P2)."),
 ak("incretinas", 1482021939459, {1: 3, 2: 4}, "C-estomago", "Glicose oral > IV (GIP, GLP-1)", "Slide 10 (GLP-1/2, GIP → insulina)", "c1 verde (HY); c2 azul."),
 ak("glp1-insulina", 1482021958480, {1: 4}, "C-estomago", "GLP-1 ↑ insulina, ↓ glucagon", "Slide 10", "Azul."),
 ak("pyy-apetite", 1482022025284, {1: 4}, "C-estomago", "PYY ↓ apetite", "Slide 10 (saciedade)", "Azul."),
 # ---------- DELGADO E CÓLON ----------
 ak("segmentacao", 1482022169992, {1: 3}, "D-intestino", "Segmentação mistura", "Slide 11", "Verde."),
 ak("peristalse-delgado", 1482022178624, {1: 3}, "D-intestino", "Peristalse propulsiona", "Slide 11", "Verde.",
    extra_prefix='Short peristaltic waves (10–14 cm) move chyme aborally; small-intestine transit takes about 2–4 h, and the ileocecal sphincter relaxes to let it into the cecum.<br><br>'),
 ak("gastrocolico", 1482022185671, {1: 3}, "D-intestino", "Reflexo gastrocólico", "Slide 12", "Verde."),
 dict(key="colon-padroes", kind="autoral", flags={1: 3, 2: 4}, bloco="D-intestino",
  text=('In the colon, {{c1::haustral contractions}} mix contents and favor water absorption, while {{c2::mass movements}} (a few times a day) push feces toward the rectum'),
  extra=('Proximal colon: water and electrolyte absorption; distal colon: stores and compacts feces. Colonic transit can take up to 48 h. '
         'Mass movements often follow meals (gastrocolic reflex) and fill the rectum, starting the defecation reflex.<br><br>'
         + SLIDE("nebli-uc08-fi09-s12-colon.png", "motor patterns of the large intestine", 420)),
  alvo="Haustrações × movimentos de massa", evid="Slide 12", uso="Constipação; diarreia (futuro).", motivo="c1 verde; c2 azul.",
  busca="AnKing só haustra em RCU/megacólon tóxico; lacuna."),
 dict(key="reflexo-evacuacao", kind="autoral", flags={1: 3, 2: 3}, bloco="D-intestino",
  text=('Rectal stretch triggers a spinal (S2–S4) reflex via the {{c1::pelvic (parasympathetic)}} nerves: the rectum contracts and the {{c2::internal}} anal sphincter relaxes involuntarily'),
  extra=('Defecation proceeds only if the external anal sphincter and puborectalis relax voluntarily, with a Valsalva effort of abdominal and respiratory muscles.<br><br>'
         + SLIDE("nebli-uc08-fi09-s13-evacuacao-v2.png", "puborectalis and anal sphincters at rest and during defecation", 360)),
  alvo="Reflexo da evacuação", evid="Slide 13 (medula S1–S4, nervo pélvico, EAI involuntário, EAE/puborretal voluntários)", uso="Incontinência; lesão medular.",
  motivo="Verde c1/c2.", correcao="Slide escreve S1–S4; Guyton/AnKing (pélvicos S2–S4) — card usa S2–S4, conflito registrado.",
  busca="Histology 1702234616745 só diz que o EAE controla a defecação; lacuna do reflexo."),
 # ---------- VÔMITO ----------
 ak("nts-vomito", 1461597220648, {1: 3, 2: 4}, "E-vomito", "Centro do vômito (NTS) e aferências", "Slide 14 (estímulos e integrador no tronco)", "c1 verde; c2 azul."),
 ak("area-postrema", 1461597624636, {1: 3, 2: 4}, "E-vomito", "Área postrema no 4º ventrículo", "Slide 14", "c1 verde; c2 azul."),
 ak("area-postrema-emeticos", 1461597712293, {1: 4}, "E-vomito", "Área postrema responde a quimioterápicos", "Slide 14 (quimio-radioterapia)", "Azul."),
 ak("vomito-sequencia", 1461597313002, {1: 4}, "E-vomito", "NTS coordena a sequência motora do vômito", "Slide 14 (efetor)", "Azul.",
    extra_prefix='Sequence in the lecture: salivation, deep inspiration, abdominal contraction raising intra-abdominal pressure, reverse contraction of the proximal intestine, sphincter relaxation.<br><br>'),
]

COMPARTILHADOS = {
    1790682945825: "FI08 · contrações fásicas — slides 3, 9, 11",
    1790682945928: "FI08 · contrações tônicas — slides 8–9",
    1790690363532: "FI08 · esvaziamento ↓ por gordura e H+ — slides 9–10",
    1790690363434: "FI08 · ácido/gordura no duodeno contraem o piloro — slide 9",
    1790682946029: "FI08 · EES — slide 6",
    1790682946130: "FI08 · EEI — slide 6",
    1790690361962: "FI08 · 5-HT dispara a peristalse — slide 11",
    1790688796864: "BT03 · grelina ↑ apetite — slides 9–10 (grelina relaxa o piloro)",
    1790707995534: "AN02 · flexura anorretal/puborretal — slide 13",
    1790707998135: "AN02 · esfíncter interno liso × externo esquelético — slide 13",
    1790707995634: "AN02 · dissinergia do puborretal — slide 13",
}

EXCLUIDOS = [
 (1482021949414, "Motilina no jejum / CMM — não está no slide"),
 (1482022081983, "Íleo 8–9 ondas/min — frequências de estômago/duodeno bastam"),
 (1482022084524, "Estômago com menor frequência — redundante com freq-estomago"),
 (1482022097240, "Duodeno com maior frequência — redundante"),
 (1482022140828, "Estômago orad — AN01 excluído, aqui coberto por relaxamento receptivo"),
 (1480874967562, "Núcleo motor do trigêmeo — detalhe neuro"),
 (1480875955623, "Núcleo ambíguo — detalhe neuro"),
 (1461601620907, "NK1/substância P na área postrema — farmacologia (antieméticos)"),
 (1481418837143, "Área postrema órgão circunventricular — redundante"),
 (1462849394748, "Análogos de GLP-1 — farmacologia"),
]
FORA_DO_RECORTE = [
 "Absorção (título 'motilidade e absorção'): a aula 2 não tem slides de absorção — nenhum card",
 "Farmacologia de antieméticos e procinéticos",
 "Vídeo (slide 7) e experimento em cão (slide 9): ilustração",
]
