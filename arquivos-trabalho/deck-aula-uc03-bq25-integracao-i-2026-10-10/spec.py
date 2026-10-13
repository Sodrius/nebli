# Especificação curada — Integração metabólica I: especialização por órgãos e tecidos (UC03 P2, Bioquímica; 70 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-bq25-20261010a"
SHORT = "bq25"
LESSON = "2026-uc03-bioquimica-25-integracao-metabolica-i"
DECK = "NEBLI::UC03::P2::Bioquímica::Integração metabólica I"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-04) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 15 consultas), seções FirstAid de metabolismo, glucagon e insulina (busca/tags-secao.txt), 10/10: ")
EXCLUIDOS = [
 (1472435688940, "desfosforilação da fosforilase: recíproco dispensável"),
 (1472435698856, "desfosforilação da sintase: recíproco dispensável"),
 (1474164729347, "MODY: clínica não cobrada (F-20261010-CLAUDE-04)"),
 (1474164725164, "MODY: clínica não cobrada"),
 (1474253749691, "receptor α da epinefrina no fígado: detalhe não citado"),
 (1497375984494, "cor das fibras por mioglobina: a aula fala de mitocôndrias"),
 (1462122709023, "insulinoma/sulfonilureias: clínica fora da aula"),
]
FORA_DO_RECORTE = ["etapas individuais da glicólise e do ciclo de Krebs (UC01)", "doenças de depósito de glicogênio e erros inatos", "farmacologia do diabetes (GR2)"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_, G_ = ("A-regulacao", "B-reservas", "C-figado", "D-musculo", "E-adiposo-cerebro-rim-sangue", "F-pancreas", "G-jejum")
CARDS = [
 # ---------- A. Regulação metabólica (slides 2–18) ----------
 au("quantidade-enzima", "The slowest but most decisive way to control a reaction is to change the amount of {{c1::enzyme}} by synthesis or degradation", {1: Z}, A_,
    "Regulação de longo prazo", "4; transcrição", "central", "sem card nos acervos.", [1474164553998, 1474164712553], "Azul: lâmina 4.",
    extra="- Allosteric and covalent changes are the fast responses"),
 au("feedback", "In feedback inhibition, a pathway's end product {{c1::allosterically}} inhibits an early enzyme", {1: V}, A_,
    "Retroinibição alostérica", "7–8", "central", "sem card geral nos acervos.", [1474164763461, 1474164928483], "Verde: princípio da lâmina 7.",
    extra="- Effectors bind a site other than the active site"),
 au("efetor-duplo", "The same metabolite can be a negative allosteric effector of one pathway and a {{c1::positive}} effector of another", {1: Z}, A_,
    "Efetor com sinais opostos", "7", "central", "sem card nos acervos.", [1474164763461, 1475896509771], "Azul: lâmina 7.",
    extra="- Example: citrate inhibits PFK-1 and activates acetyl-CoA carboxylase"),
 au("krebs-nadh", "High NADH and ATP {{c1::slow}} the citric acid cycle", {1: Z}, A_,
    "Krebs regulado por cofatores", "9", "central", "sem card geral nos acervos.", [1474224610331, 1474164763461], "Azul: lâmina 9.",
    extra="- ADP and NAD+ speed it up"),
 ak("fosforilase-ativa", 1472435673376, {1: V}, A_, "Fosforilação ativa a fosforilase", 13, "Verde: lâminas 13–14."),
 ak("sintase-inativa", 1472435681635, {1: V}, A_, "Fosforilação inativa a sintase", 14, "Verde: par oposto da fosforilase (lâmina 14)."),
 au("pdh-fosforilada", "Phosphorylation of its E1 subunit {{c1::inactivates}} the pyruvate dehydrogenase complex", {1: V}, A_,
    "PDH inativada por fosforilação", "15", "central", "sem card de PDH quinase nos acervos.", [1474224610331, 1474224602587],
    "Verde: lâmina 15.", extra="- PDH kinase is activated by ATP, NADH and acetyl-CoA"),
 ak("pdh-ativadores", 1474224610331, {1: Z, 2: Z, 3: Z}, A_, "PDH ativada por ADP, Ca²⁺, NAD⁺", 15, "Azuis: lâmina 15."),
 au("insulina-alimentado", "In the fed state, a high insulin/glucagon ratio shifts tissues toward fuel {{c1::storage}}", {1: V}, A_,
    "Gangorra insulina × glucagon", "18; transcrição", "central", "AnKing trata cada hormônio isolado.", [1462131802276, 1462121459429],
    "Verde: lâmina 18.", extra="- In fasting, a low ratio shifts them toward fuel mobilization"),
 sh(1791054011246, "verde", A_, "Glucagon: glicogenólise e gliconeogênese", 18, "Verde: nota já existente do Grand Round 2."),
 # ---------- B. Reservas (slides 17–20, transcrição) ----------
 au("reserva-figado-musculo", "{{c1::Liver}} glycogen maintains blood glucose for the whole body", {1: V}, B_,
    "Glicogênio hepático × muscular", "19, 25, 51; transcrição", "central", "sem card nos acervos.", [1474253912958, 1474253771539],
    "Verde: papel central do fígado (lâminas 25 e 51).", extra="- Muscle glycogen, larger in total, is used only by the muscle itself"),
 au("proteina-musculo", "In prolonged fasting, muscle protein is broken down into {{c1::amino acids}} that feed hepatic gluconeogenesis", {1: Z}, B_,
    "Músculo como reserva de proteína", "19, 40; transcrição", "central", "sem card nos acervos.", [1476661001248, 1476502551897],
    "Azul: transcrição.", extra="- Muscle is the largest store of mobilizable protein"),
 # ---------- C. Fígado (slides 21–48) ----------
 au("porta", "The {{c1::portal vein}} carries absorbed nutrients and toxins from the intestine straight to the liver", {1: Z}, C_,
    "Veia porta", "22, 67; transcrição", "central", "sem card metabólico nos acervos.", [1474253910254, 1476502557231], "Azul: lâmina 22."),
 ak("glut2", 1462809621604, {1: V}, C_, "GLUT-2 bidirecional", 30, "Verde: HY; lâminas 29–31."),
 au("glut2-km", "Because GLUT2 has a high Km, glucose inside the hepatocyte stays roughly {{c1::equal}} to blood glucose", {1: V}, C_,
    "GLUT2 de Km alto", "31; transcrição", "central", "AnKing não liga o Km à função hepática.", [1462809621604, 1474164674426],
    "Verde: lâmina 31.", extra="- So the liver takes up glucose mainly when blood glucose is high"),
 ak("glut1", 1462809498251, {1: Z}, C_, "GLUT-1 em hemácia e cérebro", 30, "Azul: lâmina 30."),
 ak("glut3", 1462809626737, {1: R}, C_, "GLUT-3 no cérebro", 30, "Rosa: lâmina 30."),
 sh(1791054011372, "verde", C_, "Insulina insere GLUT-4", 30, "Verde: nota já existente do Grand Round 2."),
 au("aprisionamento", "Phosphorylated glucose stays in the cell because glucose 6-phosphate cannot use {{c1::GLUT}} transporters", {1: Z}, C_,
    "Aprisionamento por fosforilação", "32; transcrição", "central", "sem card nos acervos.", [1474164741147, 1474164736251], "Azul: transcrição."),
 ak("gk-km", 1474164674426, {1: V}, C_, "Glicoquinase de Km alto", 32, "Verde: lâmina 32."),
 ak("hk-km", 1474164568985, {1: Z}, C_, "Hexoquinase de Km baixo", 32, "Azul: HY recíproco de gk-km (F-20261010-CLAUDE-03).", hy_repete="gk-km"),
 ak("gk-g6p", 1474164720011, {1: Z}, C_, "Glicoquinase não inibida por G6P", 32, "Azul: lâmina 32."),
 au("gk-hipoglicemia", "Because glucokinase works only at high glucose, during low blood glucose the liver {{c1::releases}} glucose instead of trapping it", {1: Z}, C_,
    "Glicoquinase poupa glicose na hipoglicemia", "32; transcrição", "central", "sem card nos acervos.", [1474164674426, 1474164741147], "Azul: lâmina 32."),
 au("irreversiveis", "Glycolysis and gluconeogenesis are controlled at the enzymes that catalyze {{c1::irreversible}} reactions", {1: V}, C_,
    "Controle nas reações irreversíveis", "33; transcrição", "central", "sem card geral nos acervos.", [1474164553998, 1474253986881],
    "Verde: lâmina 33.", extra="- Glycolysis: hexokinase, PFK-1, pyruvate kinase; gluconeogenesis: pyruvate carboxylase, PEPCK, FBPase-1, G6Pase"),
 ak("pfk1-limitante", 1474164553998, {1: V}, C_, "PFK-1 limita a glicólise", 34, "Verde: lâmina 34."),
 ak("pfk1-inibe", 1474164763461, {1: Z}, C_, "ATP e citrato inibem PFK-1", 36, "Azul: lâmina 36."),
 ak("pfk1-ativa", 1474164767353, {1: Z}, C_, "AMP e F2,6BP ativam PFK-1", 36, "Azul: lâmina 36."),
 ak("f26-pka", 1474164784750, {1: V}, C_, "PFK-2/FBPase-2 bifuncional regulada pela PKA", 35, "Verde: lâmina 35."),
 ak("f26-glucagon", 1474164831303, {1: V}, C_, "Glucagon ↓ F2,6BP", 35, "Verde: lâmina 35."),
 ak("pfk2-efeito", 1474164853411, {1: Z}, C_, "PFK-2 estimula glicólise e inibe gliconeogênese", 35, "Azul: lâmina 35."),
 ak("fbpase-inibe", 1474253975760, {1: Z}, C_, "F2,6BP e AMP inibem FBPase-1", 36, "Azul: HY que repete o efeito de F2,6BP em pfk1-ativa (F-20261010-CLAUDE-03).", hy_repete="pfk1-ativa"),
 ak("g6pase-musculo", 1474253912958, {1: V}, C_, "Músculo sem glicose-6-fosfatase", 37, "Verde: lâminas 37 e 57."),
 ak("g6pase-re", 1474253994282, {1: R}, C_, "G6Pase no RE", 37, "Rosa: lâmina 37."),
 au("fosforilase-figado-glicose", "In the liver, high glucose shifts phosphorylase a to its inactive {{c1::T}} state", {1: Z}, C_,
    "Glicose inativa a fosforilase hepática", "13, 38", "central", "sem card nos acervos.", [1472435673376, 1474253761770],
    "Azul: lâmina 38.", extra="- This lets the liver stop glycogen breakdown when glucose is plentiful"),
 au("fosforilase-figado-amp", "Unlike the muscle enzyme, liver glycogen phosphorylase is insensitive to {{c1::AMP}}", {1: Z}, C_,
    "Fosforilase hepática ignora AMP", "38", "central", "sem card nos acervos.", [1474253761770, 1472435673376],
    "Azul: lâmina 38.", extra="- Liver phosphorylase is controlled mainly by glucagon and by glucose", duplicacao_ok="ganho: o contraste fígado × músculo; o card AnKing cobra só o músculo"),
 ak("cahill", 1476661001248, {1: Z, 2: V}, C_, "ALT e ciclo alanina-glicose", 40, "Verde c2 (prova 2025 P2 1.8), azul c1."),
 ak("acc-insulina", 1475896509771, {1: V, 2: Z}, C_, "ACC ativada por insulina e citrato", 42, "Verde c1, azul c2; lâmina 42."),
 ak("acc-glucagon", 1475896504605, {1: Z, 2: R}, C_, "ACC inibida por glucagon", 42, "Azul c1, rosa c2."),
 ak("betaox-cetogenese", 1475982812947, {1: V, 2: Z}, C_, "Acetil-CoA da β-oxidação → cetogênese", 42, "Verde c1, azul c2."),
 ak("cetogenese-figado", 1476154069517, {1: V}, C_, "Cetogênese no fígado", 42, "Verde: lâmina 42."),
 au("glicogenio-figado-glucagon", "Glucagon drives liver glycogen breakdown, whereas muscle glycogen breakdown responds to {{c1::epinephrine}}", {1: V}, C_,
    "Glucagon no fígado, epinefrina no músculo", "43, 51", "central", "sem card do contraste nos acervos.", [1462131802276, 1474253744082],
    "Verde: lâminas 43 e 51.", duplicacao_ok="ganho: contraste fígado × músculo; epinefrina-beta cobra a fosforilase pela via β"),
 ak("glucagon-ampc", 1462131799037, {1: V}, C_, "Glucagon age por AMPc", 44, "Verde: lâmina 44."),
 ak("gk-insulina", 1474164712553, {1: V}, C_, "Insulina induz glicoquinase", 45, "Verde: lâmina 45."),
 au("pp1", "Insulin turns glycogen synthase on by activating {{c1::protein phosphatase 1}}", {1: V}, C_,
    "Insulina ativa PP1", "46, 61", "central", "consulta 'protein phosphatase' sem card de PP1.", [1472435681635, 1472435673376],
    "Verde: lâminas 46 e 61.", extra="- The same dephosphorylation turns glycogen phosphorylase off"),
 ak("hsl", 1475982732554, {1: V}, C_, "Lipase hormônio-sensível", 47, "Verde: lâmina 47."),
 ak("hsl-hormonios", 1475982737323, {1: V, 2: V, 3: Z}, C_, "HSL ativada por epinefrina, glucagon, cortisol", 47, "Verdes c1–c2, azul c3."),
 ak("hsl-insulina", 1475982741557, {1: Z}, C_, "Insulina inibe HSL", 48, "Azul: lâmina 48."),
 ak("glicerol", 1475982746310, {1: V}, C_, "Glicerol vira glicose no fígado", 48, "Verde: prova 2023 P1 2.2."),
 # ---------- D. Músculo (slides 49–61) ----------
 ak("epinefrina-beta", 1474253744082, {1: V, 2: Z}, D_, "Epinefrina ativa a fosforilase", 51, "Verde c1, azul c2; lâminas 51–59."),
 au("musculo-sem-glucagon", "Skeletal muscle glycolysis does not respond to glucagon, because muscle lacks {{c1::glucagon receptors}}", {1: V}, D_,
    "Músculo sem resposta ao glucagon", "52", "central", "sem card nos acervos.", [1474253744082, 1462131701878], "Verde: lâmina 52."),
 ak("fibra-lenta", 1497376040736, {1: V, 2: Z}, D_, "Fibra lenta oxidativa", 52, "Verde c1, azul c2; lâmina 52."),
 ak("fibra-rapida", 1497376071663, {1: Z, 2: Z}, D_, "Fibra rápida glicolítica", 52, "Azuis: HY recíproco de fibra-lenta (F-20261010-CLAUDE-03).", hy_repete="fibra-lenta"),
 ak("fosfocreatina", 1476502692147, {1: V}, D_, "Fosfocreatina nos primeiros segundos", 54, "Verde: lâminas 52 e 54."),
 ak("atp-segundos", 1476502688070, {1: Z}, D_, "ATP estocado nos 2 primeiros segundos", 54, "Azul: HY que repete a sequência de fosfocreatina (F-20261010-CLAUDE-03).", hy_repete="fosfocreatina"),
 au("cardiaco", "Heart muscle relies mainly on {{c1::fatty acids}} and ketone bodies, burning them in abundant mitochondria", {1: V}, D_,
    "Metabolismo cardíaco", "53", "central", "sem card nos acervos.", [1476154185261, 1497376040736],
    "Verde: lâmina 53.", extra="- Little stored glycogen; some glucose"),
 ak("cori", 1476660981762, {1: Z, 2: V}, D_, "Ciclo de Cori (LDH)", 55, "Verde c2 (lactato), azul c1."),
 ak("cori-nad", 1476660990515, {1: Z}, D_, "Cori regenera NAD⁺", 55, "Azul: lâmina 55."),
 ak("musculo-g6p", 1474253771539, {1: Z}, D_, "Glicogenólise muscular → G6P", 56, "Azul: lâminas 56–57."),
 ak("fosforilase-amp-musculo", 1474253761770, {1: Z}, D_, "AMP ativa a fosforilase muscular", 57, "Azul: lâmina 57."),
 ak("g6p-sintase", 1474253707546, {1: V, 2: R, 3: Z}, D_, "Insulina e G6P ativam a sintase", 58, "Verde c1, azul c3 (G6P, lâmina 58), rosa c2 (cortisol)."),
 au("fim-sinal", "Epinephrine signaling stops when Gα hydrolyzes its GTP and {{c1::phosphodiesterase}} degrades cAMP", {1: Z}, D_,
    "Fim do estímulo da epinefrina", "60", "central", "sem card nos acervos.", [1474253744082, 1462131799037], "Azul: lâmina 60."),
 # ---------- E. Adiposo, cérebro, rim e sangue (slides 62–68) ----------
 au("adiposo-insulina", "In adipocytes, insulin stimulates glucose uptake and {{c1::glycolysis}}, which feed triacylglycerol synthesis", {1: Z}, E_,
    "Adiposo e insulina", "63", "central", "sem card nos acervos.", [1475982732554, 1475896540810],
    "Azul: lâmina 63.", extra="- Adipose holds the body's largest energy reserve"),
 ak("ucp1", 1474253588459, {1: Z, 2: V}, E_, "UCP1 no tecido adiposo marrom", 63, "Verde c2 (desacoplamento, mecanismo), azul c1; lâmina 63."),
 au("cerebro-glicose", "At rest the brain uses about {{c1::20%}} of the body's oxygen", {1: R}, E_,
    "Consumo cerebral de O₂", "65", "lateral", "sem card nos acervos.", [1476502674112, 1476502551897],
    "Rosa: lâmina 65.", extra="- Neurons burn glucose; glia can also use fatty acids"),
 ak("cetonas-cerebro", 1476502674112, {1: V, 2: Z}, E_, "Cetonas no cérebro após 3 dias de jejum", 65, "Verde c1, azul c2; lâmina 65 e prova 2024."),
 ak("rim-gliconeogenese", 1474253910254, {1: V, 2: V, 3: Z}, E_, "Gliconeogênese no fígado e rim", 66, "Verdes c1–c2, azul c3."),
 au("rim-ureia", "Besides gluconeogenesis, the kidneys excrete the {{c1::urea}} made in the liver", {1: R}, E_,
    "Rim excreta ureia", "66", "lateral", "sem card nos acervos.", [1474253910254, 1476661001248], "Rosa: lâmina 66."),
 au("hemacia-lactato", "Red blood cells lack mitochondria, so they make ATP by anaerobic glycolysis and release {{c1::lactate}}", {1: V}, E_,
    "Hemácia: glicólise anaeróbia", "68", "central", "sem card nos acervos.", [1476502591395, 1476660981762], "Verde: lâmina 68."),
 ak("hemacia-cetona", 1476502591395, {1: V}, E_, "Hemácia não usa cetonas", 68, "Verde: consequência de não ter mitocôndrias."),
 # ---------- F. Pâncreas (slide 70) ----------
 ak("alfa-glucagon", 1462121444354, {1: V, 2: Z}, F_, "Célula α secreta glucagon", 70, "Verde c1, azul c2."),
 ak("beta-insulina", 1462121459429, {1: V, 2: Z}, F_, "Célula β secreta insulina", 70, "Verde c1, azul c2."),
 ak("glucagon-hipoglicemia", 1462131726115, {1: V}, F_, "Hipoglicemia estimula glucagon", 70, "Verde: lâmina 70."),
 ak("insulina-glicose", 1462123239655, {1: Z}, F_, "Glicose regula a insulina", 70, "Azul: lâmina 70."),
 ak("beta-glut2", 1462127745460, {1: Z}, F_, "Célula β usa GLUT-2", 70, "Azul: HY que repete glut2 (F-20261010-CLAUDE-03).", hy_repete="glut2"),
 # ---------- G. Jejum (provas 2024 e 2025; guia de veteranos) ----------
 ak("jejum-entre-refeicoes", 1476502557231, {1: V}, G_, "Glicogenólise entre refeições", 70, "Verde: prova 2024 P2 1.3."),
 ak("glicogenio-12-18", 1476502582683, {1: Z}, G_, "Glicogênio esgota em 12–18 h", 70, "Azul: número do jejum.", hy_repete="jejum-entre-refeicoes"),
 ak("jejum-1-3", 1476502641042, {1: V}, G_, "Gliconeogênese nos dias 1–3", 70, "Verde: provas 2024 e 2025."),
 ak("jejum-ag", 1476502637223, {1: V}, G_, "Músculo e fígado passam a usar ácidos graxos", 70, "Verde: provas 2024 e 2025."),
 ak("jejum-prioridade", 1476502551897, {1: V, 2: V, 3: Z}, G_, "Prioridade: glicose para cérebro e hemácias", 70, "Verdes c1–c2, azul c3."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
 'porta': '- This lets the liver process nutrients and detoxify before they reach the body',
 'glut1': '- High glucose affinity keeps uptake going even at low blood glucose',
 'aprisionamento': '- Hexokinase (muscle) and glucokinase (liver) make glucose 6-phosphate',
 'gk-hipoglicemia': '- Glucokinase has a much higher Km than hexokinase',
 'pfk1-limitante': '- It catalyzes an irreversible step: F6P → F1,6BP',
 'pfk2-efeito': '- Through more fructose 2,6-bisphosphate',
 'pfk1-ativa': '- F2,6BP is the dominant signal in the liver',
 'g6pase-musculo': '- Muscle glucose 6-phosphate stays in the muscle for glycolysis',
 'g6pase-re': '- Active in glycogenolysis and gluconeogenesis, when glycolysis is inhibited',
 'cahill': '- Muscle sends amino groups to the liver as alanine',
 'acc-glucagon': '- Glucagon (via PKA) turns fatty acid synthesis off during fasting',
 'cetogenese-figado': '- The liver makes ketone bodies but does not use them',
 'glicogenio-figado-glucagon': '- Liver glycogen serves the whole body; muscle glycogen serves the muscle',
 'gk-insulina': '- Insulin does not change hepatic glucose uptake, which depends on GLUT2',
 'pp1': '- Insulin also inactivates GSK3 and PKA',
 'hsl-hormonios': '- Through cAMP and PKA',
 'hsl-insulina': '- Insulin dephosphorylates the lipase, blocking triacylglycerol breakdown',
 'epinefrina-beta': '- Through cAMP and PKA, as in the liver',
 'musculo-sem-glucagon': '- Epinephrine and insulin are the hormones that regulate muscle',
 'fosforilase-amp-musculo': '- AMP signals low energy during contraction',
 'g6p-sintase': '- G6P rises when PFK-1 is inhibited, pushing glucose into glycogen',
 'fim-sinal': '- The PKA regulatory subunits then rebind the catalytic ones',
 'cetonas-cerebro': '- This spares glucose and muscle protein',
 'rim-gliconeogenese': '- The kidney also has glucose 6-phosphatase',
 'rim-ureia': '- Urea carries nitrogen from amino acid breakdown',
 'hemacia-lactato': '- The lactate returns to the liver through the Cori cycle',
 'alfa-glucagon': '- Stimuli: low glucose, high amino acids, epinephrine',
 'beta-insulina': '- Stimulus: high blood glucose, sensed through GLUT2 and glucokinase',
 'jejum-ag': '- Free fatty acids come from adipose lipolysis',
 'jejum-prioridade': '- Neurons and red blood cells depend on glucose'}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
DUPLICACAO = {'reserva-figado-musculo': 'ganho: papel do glicogênio hepático na glicemia; cetogenese-figado e rim-gliconeogenese cobram outras funções do fígado', 'musculo-sem-glucagon': 'ganho: por que o músculo ignora o glucagon (sem receptor), não só que o glucagon age no fígado', 'cardiaco': 'ganho: combustível do coração; jejum-ag cobra a troca de combustível no jejum', 'hemacia-lactato': 'ganho: por que a hemácia produz lactato (sem mitocôndria); cori cobra a enzima do ciclo'}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
