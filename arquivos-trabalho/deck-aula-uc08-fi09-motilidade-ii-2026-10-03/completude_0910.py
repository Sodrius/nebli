"""F-20261009-CLAUDE-02: insere no spec.py os cards das lacunas da FI09 (auditoria Codex 08/10 + P1 2026 Q1/Q2).
Rodado uma vez sobre spec-antes-completude.py; mantido como registro do que entrou e onde."""
import re
from pathlib import Path

HERE = Path(__file__).parent
s = (HERE / "spec-antes-completude.py").read_text()


def after(key, block):
    global s
    i = s.index(f'("{key}"')
    m = re.compile(r"\n ?(ak|au|sh)\(|\n # |\n\]").search(s, i + 10)
    s = s[:m.start()] + "\n" + block.strip("\n") + s[m.start():]


after("picos-forca", '''
 # F-20261009-CLAUDE-02 (auditoria Codex + P1 2026 Q2): limiar contrátil × elétrico como alvo próprio
 au("limiar-contratil", "A slow wave that reaches only the {{c1::<b>contractile</b>}} threshold, with no spike potentials, still causes a weak contraction", {1: V}, A_,
    "Limiar contrátil: contração fraca sem potenciais", "3; Aires cap. 60 (Fig. 60.12); P1 2026 Q2", "prova",
    "AnKing só tem a onda lenta, os canais e a frequência; 'contractile threshold' sem card nos acervos (busca 09/10).", [1482022069057, 1482022108336],
    "Verde: 'o que significa atingir o limiar contrátil ou elétrico?' no slide 3; caiu na P1 2026 (Q2).",
    extra="- <b>Contractile</b> threshold: small Ca²⁺ rise, weak contraction<br>- <b>Electrical</b> threshold: spikes bring more Ca²⁺, strong contraction<br><br>" + F(3)),
 au("canais-l", "<b>Spike potentials</b> of GI smooth muscle depend on {{c1::L-type Ca²⁺}} channels, which take no part in slow waves", {1: Z}, A_,
    "Canais de Ca2+ tipo L: picos, não ondas lentas", "3; Aires cap. 60", "central", "'L-type' só em card de bloqueador de canal de cálcio no AnKing.", [1472502461817, 1482022108336],
    "Azul: 'canais de cálcio tipo L não participam das ondas lentas' no slide 3.", extra="- Slow waves come from cation channels (Ca²⁺, Na⁺, K⁺) paced by Cajal cells<br>- Calcium channel blockers act on the <b>spike</b> Ca²⁺ influx"),
 au("ach-amplitude", "{{c1::Acetylcholine}} and stretch of the gut wall raise slow-wave amplitude, so more spike potentials ride on each wave", {1: Z}, A_,
    "SNE/SNA e distensão aumentam a amplitude das ondas lentas", "4; Aires cap. 60 (Fig. 60.24)", "central", "nenhum card nos acervos liga ACh ou distensão à amplitude da onda lenta.", [1482022069057, 1482022061641],
    "Azul: 'como o SN potencializa a amplitude das ondas lentas?' no slide 4.", extra="Norepinephrine lowers slow-wave amplitude and spike frequency"),''')
after("pterigoideo-lateral", '''
 au("receptores-degluticao", "Touch receptors of the {{c1::oropharynx}}, stimulated by the bolus, start the reflex phases of swallowing", {1: Z}, C_,
    "Receptores da orofaringe disparam as fases reflexas", "5; Aires cap. 60 (p. 884)", "central", "AnKing e MCAT sem o gatilho sensorial da deglutição.", [1482022111185, 1480640527660],
    "Azul: 'receptores sensoriais no teto da cavidade oral → fases reflexas da deglutição' no slide 5.", extra="Afferents reach the swallowing center in the medulla mainly through CN IX and CN X"),''')
after("palato-mole", '''
 au("constritores", "In the pharyngeal phase, a peristaltic wave of the {{c1::pharyngeal constrictors}} pushes the bolus toward the esophagus", {1: V}, C_,
    "Constritores da faringe propelem o bolo", "6; Aires cap. 60 (p. 884)", "central", "AnKing só cita os constritores no Extra de embriologia (1489115667759); AnatoKing dá origem e inserção, não a sequência.",
    [1489115667759, 1482022111185], "Verde: passo 2 da fase faríngea no slide 6.", extra="The wave runs from the superior to the middle and inferior constrictors"),''')
after("epiglote", '''
 au("respiracao-degluticao", "During the pharyngeal phase of swallowing, the brainstem briefly {{c1::inhibits breathing}}", {1: Z}, C_,
    "Supressão da respiração na fase faríngea", "6; Aires cap. 60 (p. 884)", "central", "sem card nos acervos (busca 'swallow* apnea/breath*').", [1482022114115, 1480875955623],
    "Azul: passo 4 da fase faríngea no slide 6.", extra="- Together with the closed larynx, it keeps food out of the trachea"),
 au("ees", "The upper esophageal sphincter {{c1::relaxes}} ahead of the pharyngeal wave, then {{c2::contracts}} once the bolus is in the esophagus", {1: V, 2: Z}, C_,
    "EES relaxa e depois contrai", "6; Aires cap. 60 (p. 885); monitoria", "central", "'upper esophageal sphincter' só em Zenker e anestesia nos acervos.", [1482203693998, 1482022131650],
    "Verde c1: 'relaxamento do EES' (fase faríngea) no slide 6; azul c2: 'contração do EES' abre a fase esofágica.",
    extra="At rest it stays closed (about 40 mmHg), keeping air out of the esophagus"),
 au("peristalse-primaria", "<b>Primary peristalsis</b> of the esophagus is started by {{c1::swallowing}} and run by the brainstem swallowing center", {1: Z}, C_,
    "Peristalse primária: deglutição, centro bulbar", "6; Aires cap. 60 (p. 885)", "central", "zero card sobre peristalse primária nos acervos.", [1482203810412, 1556157808107],
    "Azul: 'peristalse 1ª' da fase esofágica no slide 6.", extra="It travels at 1–3 cm/s and relaxes the LES ahead of the bolus"),''')
after("relaxamento-receptivo", '''
 au("capacidade-estomago", "Receptive relaxation lets the stomach hold about {{c1::1–1.5 L}} of food without a rise in pressure", {1: R}, D_,
    "Capacidade de armazenamento 1–1,5 L", "8; Aires cap. 60 (p. 888)", "lateral", "sem card de capacidade gástrica nos acervos.", [1482022134697, 1482022076569],
    "Rosa: número do slide 8 ('1,0–1,5 L').", extra="- Food waits in the fundus for 1–2 h before mixing"),''')
after("cck-esvaziamento", '''
 au("grelina-piloro", "{{c1::Ghrelin}} relaxes the pylorus and speeds gastric emptying, unlike secretin and CCK", {1: Z}, D_,
    "Grelina relaxa o piloro", "9; Camilleri (slide 9)", "central", "grelina no AnKing só para apetite e hipotálamo.", [1482022013033, 1482021903019],
    "Azul: 'promove relaxamento do piloro: grelina' no slide 9; o card de apetite (BT03) não cobria o piloro.", extra="- Ghrelin rises during fasting"),''')
after("pyy", '''
 au("esvaziamento-integracao", "Acid and digested nutrients in the duodenum release hormones that slow gastric emptying by relaxing the {{c1::stomach}} and contracting the {{c2::pylorus}}", {1: V, 2: V}, E_,
    "Inibição do esvaziamento: relaxa o estômago, contrai o piloro", "10; Aires cap. 60; monitoria; P1 2026 Q1", "prova",
    "AnKing tem cada hormônio isolado (1482022155210, 1482021903019), sem o efeito integrado sobre estômago e piloro.", [1482022155210, 1482021903019],
    "Verde: 'inibição do esvaziamento: relaxamento muscular do estômago e contração do piloro' no slide 10; caiu na P1 2026 (Q1).",
    extra="- Acid releases <b>secretin</b>; nutrients release <b>CCK</b>, <b>GIP</b>, <b>GLP-1</b> and <b>PYY</b><br>- Emptying matches what the duodenum can process<br><br>" + F(10)),''')
after("segmentacao", '''
 au("peristalse-curta", "In the small intestine, {{c1::short peristaltic}} contractions propel chyme, while segmentation only mixes it", {1: Z}, F_,
    "Peristalses curtas propelem", "11; Aires cap. 60 (p. 894)", "central", "AnKing define segmentação e peristalse em geral (MCAT), sem as peristalses curtas do delgado.", [1482022169992, 1556157808107],
    "Azul: 'peristalses curtas (10–14 cm): propulsão' no slide 11.", extra="When they reach the terminal ileum, the ileocecal sphincter relaxes"),
 au("transito", "Transit time is about {{c1::2–4 h}} in the small intestine and up to {{c2::48 h}} in the colon", {1: R, 2: R}, F_,
    "Tempo de trânsito: delgado 2–4 h, grosso até 48 h", "11; 12", "lateral", "sem card de tempo de trânsito nos acervos.", [1482022076569, 1482021953235],
    "Rosas: números dos slides 11 e 12.", extra="- The colon absorbs water slowly, which explains the long transit"),''')
after("reflexo-defecacao", '''
 au("defecacao-voluntaria", "Voluntary defecation adds contraction of the {{c1::abdominal and respiratory}} muscles (deep breath, closed glottis), raising intra-abdominal pressure", {1: V}, G_,
    "Defecação voluntária: mm. abdominais e respiratórios", "13; Aires cap. 60 (p. 899)", "central", "sem card de defecação voluntária nos acervos (busca 'defecation abdominal', 'valsalva').", [1471378832213, 1790974694881],
    "Verde: 'contração mm abdominais e respiratórios, voluntário' no slide 13.", extra="If defecation is postponed, the sphincters regain tone and feces move back to the sigmoid"),''')
after("area-postrema-emeticos", '''
 ak("causas-vomito", 1461596362186, {1: Z}, H_, "Estímulos do vômito: infecção, fármacos, vestíbulo, quimiorradioterapia", 14, "Azul: lista de estímulos do slide 14 (fármacos, sistema vestibular, quimio-radioterapia)."),''')
after("nts-coordena", '''
 au("vomito-retroperistalse", "Retching begins with {{c1::reverse peristalsis}} of the proximal small intestine, which pushes its contents back into the stomach", {1: Z}, H_,
    "Contração reversa do intestino proximal", "14; Aires cap. 60 (p. 892)", "central", "o AnKing dá a sequência só no Extra do NTS (1461597313002), sem a peristalse reversa.", [1461597313002, 1461597220648],
    "Azul: 'contração reversa – intestino proximal' no slide 14.", extra="- Strong antral contractions then push gastric contents through the relaxed LES"),
 au("vomito-pressao", "In vomiting, deep inspiration and abdominal muscle contraction raise {{c1::intra-abdominal}} pressure and force gastric contents out", {1: Z}, H_,
    "Inspiração profunda e pressão intra-abdominal no vômito", "14; Aires cap. 60 (p. 892)", "central", "idem; só no Extra do NTS.", [1461597313002, 1471378832213],
    "Azul: 'inspiração profunda, contração mm abdominal, elevação da pressão intra-abdominal' no slide 14.", extra="The sphincters relax and the closed glottis protects the airway"),''')
(HERE / "spec.py").write_text(s)
print("ok")
