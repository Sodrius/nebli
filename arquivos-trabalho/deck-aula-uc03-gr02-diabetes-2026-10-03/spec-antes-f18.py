# Especificação curada — Grand Round 2, diabetes melito (UC03 P2, aula 21; Dra. Sharon Nina Admoni, Endocrinologia HC-FMUSP).
# 57 lâminas: caso clínico de DM1 (1–14), teoria de DM, AGEs e complicações (15–45), radiologia (46–57; InRad).
# Feita em 03/10/2026 a partir de planejamento.json (escrito antes). Ordem = slides. Critérios até F-20261003-CLAUDE-19.
# AnKing → outros acervos → autoral (13 autorais, só o que importa e não se achou: Schiff/Amadori/AGE, RAGE, frutosamina,
# lua de mel, definição, sensor, US renal, escore de cálcio, angioTC, RM da osteomielite).
RUN_ID = "uc03-gr02-20261003a"
SHORT = "gr02"
LESSON = "2026-uc03-grand-round-21-diabetes"
DECK = "NEBLI::UC03::P2::Grand Round::Grand Round 2 (diabetes)"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261003-CLAUDE-19) + PLANO-GERACAO-ANO, 03/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt, 61 consultas, e busca/sessao2-anking-ext.txt, 31 consultas, 03/10); "
         "Referências Externas (MCAT, Histology, LLU, Dope, AnatoKing, Dorian) pelos mesmos alvos (busca/ext.txt): ")
EXCLUIDOS = [
 (1462327309654, "nomes dos corpos cetônicos: já no Extra do card de lipólise → cetonas (1462327286091)"),
 (1475178090922, "ácidos não voláteis no DM1: redundante com corpos cetônicos"),
 (1462849116753, "asparte para o pico pós-prandial: redundante com o card de ação rápida"),
 (1462122681020, "insulina e peptídeo C equimolares: vai no verso do card do peptídeo C"),
 (1570740722568, "volume extracelular cai na CAD/EHH: coberto pela poliúria/diurese osmótica"),
 (1462327441833, "EHH > 600 mg/dL e > 320 mOsm: números de clínica fora do slide; contraste fica no card de cetose"),
 (1475364102374, "glicação da MBG: redundante com 'primeira alteração renal'"),
 (1580249534259, "microalbuminúria precoce: redundante com o card de hiperfiltração → microalbuminúria"),
 (1471819186977, "arteriolosclerose hialina em HAS e DM: redundante com o card da glicação de pequenos vasos"),
 (1474686354906, "IECA na nefropatia: tratamento fora da aula"),
 (1489968613360, "anti-VEGF: farmacologia fora da aula"),
 (1524013224124, "sintomas neuroglicopênicos: não estão na aula"),
 (1471811955341, "mnemônico das artérias com aterosclerose: card enorme, um cloze só para cinco artérias"),
 (1475353745252, "necrose papilar (SAND): mnemônico longo; pielonefrite já coberta"),
 (1543505166905, "três complicações microvasculares e exames: lista longa"),
 (1462913285372, "exemplos de glitazonas: nomes de fármacos fora da aula"),
]
FORA_DO_RECORTE = ["tratamento detalhado da CAD (ânion gap, dextrose, bicarbonato)", "algoritmo de antidiabéticos e SGLT2",
                   "MODY, diabetes neonatal, lipoatrófico", "neoplasias endócrinas do pâncreas", "slide 32 (figura de artigo)"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_, G_, H_ = ("A-caso-clinico", "B-definicao-e-tipos", "C-metabolismo-dm1", "D-dm2-resistencia", "E-tratamento",
                                  "F-ages", "G-complicacoes", "H-radiologia")
CARDS = [
 # ---------- A. Caso clínico: homem de 26 anos com DM1 (slides 2–14) ----------
 ak("vinheta-dm1", 1516202686282, {1: Z}, A_, "Poliúria, polidipsia e perda de peso sugerem DM1", 2, "Azul: apresentação do caso (slide 2)."),
 ak("glicemia-acaso", 1584121453264, {1: V}, A_, "Glicemia ao acaso > 200 com sintomas é diagnóstica", 4, "Verde: HY (1); glicemia 397 no PS (Robbins)."),
 ak("k-serico-dm1", 1462327341080, {1: V}, A_, "K sérico alto no DM1 recém-diagnosticado", 4, "Verde: HY (1); K 4,4 conferido antes da insulina (veterano)."),
 ak("k-intracelular", 1462327346466, {1: Z}, A_, "K intracelular baixo no DM1", 4, "Azul: estoque corporal baixo apesar do K sérico."),
 ak("insulina-k", 1475028551112, {1: V}, A_, "Insulina põe K na célula pela Na+/K+-ATPase", 4, "Verde: HY (1); por que medir K antes da insulina (veterano, Ninja Nerd)."),
 ak("tratamento-crise", 1462327382493, {1: V}, A_, "Crise hiperglicêmica: fluidos EV, insulina e K", 4, "Verde: HY (1); conduta do PS no slide 4."),
 ak("jejum-126", 1462327178225, {1: V}, A_, "Glicemia de jejum ≥ 126 mg/dL", 5, "Verde: HY (1); critério diagnóstico (Robbins)."),
 ak("ttgo-200", 1462327189114, {1: V}, A_, "TTGO 2 h ≥ 200 mg/dL", 5, "Verde: HY (1); critério diagnóstico (Robbins)."),
 ak("hba1c-65", 1462327170017, {1: V}, A_, "HbA1c ≥ 6,5% é diagnóstica", 5, "Verde: HY (1); HbA1c 8,8% no slide 5."),
 au("frutosamina", "<b>Fructosamine</b> is glycated serum {{c1::albumin}}, so it reflects mean glucose over the previous 2–3 weeks", {1: Z}, A_,
    "Frutosamina = albumina glicada", "5; prova 2024 P1 2.9; veterano", "prova", "zero resultado para fructosamine/glycated albumin no AnKing e nos externos.",
    [1462327161497, 1462327641370], "Azul: exame do caso e resposta da prova de 2024.", extra="- <b>HbA1c</b> covers about 3 months (red cell lifespan)"),
 ak("peptideo-c", 1462122701249, {1: V}, A_, "Peptídeo C avalia a célula β em quem usa insulina", 5, "Verde: HY (1); peptídeo C 1,32 no caso (reserva de células β)."),
 ak("anti-gad", 1462326961450, {3: V}, A_, "Anti-GAD marca o DM1 autoimune", 5, "Verde: HY (1); AcGAD65 1082 no slide 5. Só o cloze do anticorpo (CD8 e β em outros cards)."),
 ak("aps2", 1686427339913, {1: R, 2: R}, A_, "TSH e cortisol: DM1 associa-se a tireoidite e adrenalite autoimunes (APS-2)", 5,
    "Rosa: explica por que o caso pede TSH, T4 livre e cortisol (veterano)."),
 au("sensor", "Continuous glucose sensors measure glucose in the {{c1::interstitial}} fluid, a few minutes behind blood glucose", {1: R}, A_,
    "Sensor contínuo mede glicose intersticial", "6–7, 10–11, 13–14; veterano", "lateral", "zero resultado para continuous glucose/interstitial no AnKing e nos externos.",
    [1462327161497, 1502846199357], "Rosa: relatórios AGP do caso; detalhe de monitorização.", extra="- Reports show <b>time in range</b> (70–180 mg/dL)"),
 ak("insulina-longa", 1462849196492, {1: V}, A_, "Degludeca, glargina, detemir: ação longa (basal)", 8, "Verde: HY (1); degludeca do caso."),
 ak("insulina-rapida", 1462849107376, {1: V}, A_, "Asparte, lispro, glulisina: ação rápida (bolus)", 8, "Verde: HY (1); asparte por contagem de carboidratos."),
 ak("hba1c-3meses", 1462327161497, {1: V}, A_, "HbA1c reflete os 3 meses anteriores", 9, "Verde: HY (2); queda de 8,8 para 5,2% em 4 meses."),
 ak("hba1c-alvo", 1502846199357, {1: Z}, A_, "Alvo de controle: HbA1c < 7%", 9, "Azul: leitura da evolução do caso."),
 au("lua-de-mel", "Soon after T1DM diagnosis, residual β cells keep insulin needs low, the so-called {{c1::honeymoon}} period", {1: Z}, A_,
    "Período de lua de mel do DM1", "12; Robbins p. 1151", "prova", "zero resultado para honeymoon/residual β cell no AnKing e nos externos.",
    [1462122701249, 1462327016536], "Azul: explica a dose de 1 UI de degludeca e o peptídeo C normal (Robbins).",
    extra="- Detectable <b>C-peptide</b> shows the residual secretion<br>- Needs rise as the last β cells are destroyed"),
 ak("glucagon-im", 1524258762201, {1: V}, A_, "Hipoglicemia grave fora do hospital: glucagon IM", 12, "Verde: HY (1); Glucagen 1 mg do slide 12."),
 # ---------- B. Definição e tipos (slides 16–18) ----------
 au("definicao", "<b>Diabetes mellitus</b> is chronic hyperglycemia caused by defective insulin secretion, defective insulin {{c1::action}}, or both", {1: V}, B_,
    "Definição de DM", "16; Robbins p. 1139; prova 2023 P1 2.1", "central", "AnKing só tem 'Type 1 is characterized by insulin deficiency' (resposta: o número 1); externos sem a definição.",
    [1462326105448, 1462327139204], "Verde: a definição que organiza toda a aula.",
    extra="- Type 1 → absolute insulin deficiency<br>- Type 2 → insulin resistance plus relative deficiency"),
 ak("peso-dm1", 1523412094194, {1: Z}, B_, "Perda de peso caracteriza o DM1", 17, "Azul: 'indivíduo magro, emagrecimento' na tabela do slide 17."),
 ak("gemeos-dm1", 1462327016536, {1: V}, B_, "DM1: predisposição genética fraca (50% em gêmeos)", 17, "Verde: HY (1); 'herança HLA' × 'poligênica' no slide 17."),
 ak("gemeos-dm2", 1462327023070, {1: V}, B_, "DM2: predisposição genética forte (90% em gêmeos)", 17, "Verde: HY (1); par do anterior."),
 ak("hla-dr3-dr4", 1487983956917, {1: V}, B_, "HLA-DR3 e DR4 no DM1", 17, "Verde: HY (1); 'herança associada ao sistema HLA'."),
 ak("cad-dm1", 1462327211125, {1: V}, B_, "Complicação temida do DM1: cetoacidose", 17, "Verde: HY (2); 'descompensação tipo cetoacidose'."),
 ak("ehh-dm2", 1462327389480, {1: V}, B_, "Complicação temida do DM2: estado hiperosmolar", 17, "Verde: HY (2); 'descompensação tipo coma hiperosmolar'."),
 ak("cd8-dm1", 1584129194060, {1: V}, B_, "DM1: destruição das células β por linfócitos T CD8+", 18, "Verde: HY (1); 'reação autoimune que destrói as células beta'."),
 # ---------- C. DM1 como jejum: metabolismo (slides 19–20) ----------
 ak("insulina-glucagon", 1462131783153, {1: V}, C_, "Insulina inibe a secreção de glucagon", 19, "Verde: HY (1); 'não há inibição da síntese de glucagon pela insulina'."),
 ak("glucagon-glicemia", 1462131802276, {1: V}, C_, "Glucagon aumenta glicogenólise e gliconeogênese", 19, "Verde: HY (1); 'hiperglucagonemia agrava a hiperglicemia'."),
 ak("glut4", 1462128186045, {1: Z, 2: V}, C_, "Insulina insere GLUT-4 no músculo e no tecido adiposo", 19,
    "c2 verde: HY (1), 'deficiência de insulina impede o aproveitamento de glicose'; c1 azul (tecidos)."),
 ak("perda-peso-mecanismo", 1462327073683, {1: V}, C_, "Perda de peso: lipólise e proteólise pelo glucagon sem oposição", 20, "Verde: HY (2); 'lipólise, proteólise, balanço nitrogenado negativo'."),
 ak("lipolise-cetonas", 1462327286091, {1: V, 2: Z}, C_, "Lipólise → ácidos graxos → corpos cetônicos no fígado", 20, "c1 verde: HY (2), cetogênese do slide 20; c2 azul."),
 ak("halito-cetonico", 1462327320519, {1: V, 2: Z}, C_, "CAD: hálito frutado pela acetona", 20, "c1 verde: HY (1); c2 azul."),
 ak("kussmaul", 1462327329868, {1: V, 2: Z}, C_, "CAD: respiração de Kussmaul compensa a acidose", 20, "c1 verde: HY (1); c2 azul."),
 ak("anion-gap", 1462327363797, {1: Z}, C_, "CAD: acidose metabólica com ânion gap alto", 20, "Azul: tipo da acidose."),
 ak("poliuria", 1462327089156, {1: V}, C_, "Poliúria e polidipsia: glicose filtrada arrasta água", 20, "Verde: HY (2); 'hiperosmolaridade aumenta a sobrecarga renal'."),
 ak("ehh-sem-cetose", 1462327461738, {1: V}, C_, "EHH sem cetoacidose: a insulina residual inibe a cetogênese", 20, "Verde: HY (2); contraste CAD × coma hiperosmolar (slides 17 e 20)."),
 # ---------- D. DM2: resistência e falência da célula β (slides 21–26) ----------
 ak("insulina-dm2", 1462327053167, {1: Z}, D_, "DM2: insulina alta no início, baixa depois", 21, "Azul: 'podem ter níveis normais ou elevados de insulina'."),
 ak("downregulation", 1462327139204, {1: V}, D_, "Obesidade reduz os receptores de insulina", 21, "Verde: HY (2); 'alteração na via de resposta à insulina'."),
 ak("sm-resistencia", 1500920723465, {1: Z}, D_, "Resistência à insulina é a base da síndrome metabólica", 22, "Azul: 'associada à síndrome metabólica'."),
 ak("gordura-visceral", 1584135730369, {1: V}, D_, "Gordura visceral abdominal causa resistência à insulina", 22, "Verde: HY (1); obesidade do slide 22."),
 ak("glicolipotoxicidade", 1584134939832, {1: Z}, D_, "Glicose e ácidos graxos em excesso lesam a célula β", 22, "Azul: 'estimulação crônica das células beta levam à sua falência'."),
 ak("serina-irs", 1524705541467, {1: Z, 2: V}, D_, "Fosforilação em serina do receptor e do IRS-1 causa resistência", 23,
    "c2 verde: HY (1), o elo 'serina-cinases → IRS' da figura do músculo (slide 23); c1 azul."),
 ak("adipocinas", 1584134136210, {1: Z}, D_, "Adipocinas e AGL causam resistência na obesidade", 24, "Azul: 'increased lipolysis in visceral fat' (slide 24)."),
 sh(1790999836955, "verde", D_, "Efeito incretina: glicose oral libera mais insulina (GIP, GLP-1)", 25, "Já vivo na FI09; HY (2); 'impaired incretin effect' no slide 25."),
 ak("incretina-dm2", 1584133969374, {1: Z}, D_, "GLP insuficiente contribui para a disfunção β no DM2", 25, "Azul: defeito intestinal do slide 25."),
 # ---------- E. Tratamento (slides 27–28) ----------
 ak("exercicio-glut4", 1473285099079, {2: V}, E_, "Exercício aumenta GLUT-4 no músculo", 27, "Verde: HY (1); 'dieta e exercício' do slide 27."),
 ak("metformina-1a", 1462913151403, {1: V}, E_, "Metformina é o fármaco de 1ª linha no DM2", 27, "Verde: HY (1); 'reduz produção de glicose pelo fígado'."),
 ak("metformina-gng", 1462913162803, {1: V}, E_, "Metformina reduz a gliconeogênese hepática", 27, "Verde: HY (1); ação listada no slide 27."),
 ak("tzd-sensibilidade", 1462913300610, {1: V}, E_, "Tiazolidinedionas aumentam a sensibilidade à insulina", 27, "Verde: HY (1); 'promover a absorção de açúcares pelas células'."),
 ak("sulfonilureias", 1462849248763, {1: V, 2: Z}, E_, "Sulfonilureias fecham o canal de K+ ATP-dependente da célula β", 27, "c1 verde: HY (1), 'estimular a secreção de insulina'; c2 azul."),
 ak("acarbose", 1462913702538, {1: V}, E_, "Inibidores de α-glicosidase retardam a absorção de carboidratos", 27, "Verde: HY (1); 'retardar a digestão e absorção de carboidratos'."),
 ak("glp1-fisiologia", 1482021958480, {1: Z}, E_, "GLP-1 estimula insulina e inibe glucagon", 28, "Azul: fisiologia da figura do slide 28."),
 ak("glp1-analogos", 1462849394748, {1: V}, E_, "Análogos de GLP-1: mais insulina e saciedade", 28, "Verde: HY (1); figura do slide 28 (pâncreas e cérebro)."),
 sh(1791052302525, "verde", E_, "GLP-1: saciedade por esvaziamento gástrico mais lento", 28, "Já vivo na FI09; HY (2); 'increased satiety' do slide 28."),
 ak("glp1-hipoglicemia", 1462849475077, {1: V}, E_, "Agonistas de GLP-1 não causam hipoglicemia", 28, "Verde: HY (2); secreção glicose-dependente (veterano)."),
 # ---------- F. AGEs (slides 29–33) ----------
 au("schiff", "Glucose binds protein amino groups without any enzyme, first forming a reversible {{c1::Schiff base}}", {1: V}, F_,
    "Base de Schiff (reversível)", "29–31; prova 2024 P1 2.9; Catalyst", "central", "zero resultado para Schiff base/Amadori no AnKing e nos externos; AnKing só fala em glicação não enzimática.",
    [1462327641370, 1462327481691], "Verde: primeiro passo da sequência cobrada na prova de 2024.", extra="- Forms within hours and reverses if glucose falls"),
 au("amadori", "Over days, the Schiff base rearranges into a stable {{c1::Amadori}} product, the form measured as HbA1c", {1: V}, F_,
    "Produto de Amadori (HbA1c)", "29–31; prova 2024 P1 2.9; Catalyst", "central", "zero resultado para Amadori no AnKing e nos externos.",
    [1462327641370, 1462327545263], "Verde: segundo passo da prova; liga a glicação ao exame do caso.", extra="- <b>Fructosamine</b> is the Amadori product of albumin"),
 au("age-irreversivel", "Over weeks to months, Amadori products cross-link into irreversible {{c1::advanced glycation}} end products", {1: V}, F_,
    "AGE irreversível", "29–31; prova 2024 P1 2.9; Robbins p. 1146", "central", "AnKing cita AGEs só como causa de aterosclerose, sem a formação.",
    [1462327481691, 1584446910693], "Verde: o produto final que explica as complicações crônicas.", extra="- AGEs persist even after glucose is controlled"),
 ak("hba1c-glicacao", 1462327641370, {1: Z}, F_, "HbA1c vem da glicação não enzimática da hemoglobina", 30, "Azul: Hb glicada como exemplo de glicação (prova 2024)."),
 ak("glicacao-mb", 1462327481691, {1: V}, F_, "Glicação não enzimática das membranas basais vasculares", 30, "Verde: HY (2); 'ligação a polipeptídeos – colágeno' do slide 30."),
 ak("glicacao-aterosclerose", 1462327545263, {1: V}, F_, "Glicação de vasos médios e grandes → aterosclerose", 30, "Verde: HY (2); LDL glicada e aterosclerose (prova 2024)."),
 ak("dm-aterosclerose", 1584446910693, {1: Z}, F_, "DM acelera a aterosclerose por inflamação, oxidação lipídica e AGEs", 30, "Azul: 'induz à oxidação lipídica' do slide 30."),
 ak("mbg-primeira", 1475364140189, {1: V}, F_, "Primeira alteração renal no DM: glicação da MBG", 31, "Verde: HY (1); membrana basal da figura dos slides 31 e 40."),
 au("rage", "AGEs bind their receptor RAGE on {{c1::monocytes}} and endothelium, which then release cytokines and growth factors", {1: V}, F_,
    "AGE–RAGE em monócitos e endotélio", "33; Robbins p. 1146; Catalyst", "central", "RAGE sem resultado útil no AnKing; externos só com receptores de outros temas.",
    [1584446910693, 1584134136210], "Verde: via que liga os AGEs à inflamação vascular (slide 33).",
    extra="- Also: <b>reactive oxygen species</b>, procoagulant activity, smooth muscle proliferation, more matrix"),
 # ---------- G. Complicações (slides 34–45) ----------
 ak("eferente", 1475364110524, {1: V}, G_, "A glicação atinge primeiro a arteríola eferente", 34, "Verde: HY (1); 'rim: aumento da filtração glomerular'."),
 ak("hiperfiltracao", 1475364112776, {1: V}, G_, "Eferente rígida → GFR aumentada (hiperfiltração)", 34, "Verde: HY (2); par do anterior."),
 ak("sorbitol", 1462327651340, {1: Z, 2: V, 3: V}, G_, "Glicose → sorbitol pela aldose redutase: dano osmótico", 34,
    "c2 e c3 verdes: HY (1), mecanismo do nervo e do cristalino (slides 34 e 37); c1 azul."),
 ak("schwann", 1462327670273, {1: Z, 2: V}, G_, "Dano osmótico às células de Schwann: neuropatia", 34, "c2 verde: HY (1), 'nervos: queda da velocidade de condução'; c1 azul."),
 ak("insulite", 1462327031605, {1: V}, G_, "DM1: insulite (infiltrado leucocitário nas ilhotas)", 35, "Verde: HY (1); lâmina do pâncreas (slide 35)."),
 ak("amilina", 1487550549393, {1: V}, G_, "DM2: amiloide de amilina nas ilhotas", 35, "Verde: HY (1); lâmina do pâncreas (slide 35)."),
 ak("pericitos", 1462327681826, {1: Z}, G_, "Dano aos pericitos retinianos → microaneurismas", 36, "Azul: 'fragilidade de vasos – microaneurismas'."),
 ak("rdnp-vinheta", 1505746867430, {1: Z}, G_, "Retinopatia não proliferativa: microaneurismas, hemorragias, exsudatos", 37, "Azul: 1º item do slide 37."),
 ak("rdp", 1484603685634, {1: Z}, G_, "Retinopatia proliferativa: neovasos e tração", 37, "Azul: 'retinite proliferante'."),
 ak("rdp-hemorragia", 1584395533879, {1: V}, G_, "Neovasos da retinopatia proliferativa sangram", 37, "Verde: HY (2); hemorragia e descolamento (slide 36)."),
 ak("catarata", 1462327695261, {1: V}, G_, "Catarata por dano osmótico ao cristalino", 37, "Verde: HY (1); '2º – cataratas'."),
 ak("glaucoma-iris", 1484603569313, {1: Z}, G_, "Neovascularização da íris → glaucoma de ângulo fechado", 37, "Azul: '3º – alterações da íris' e glaucoma do slide 36."),
 ak("microaneurismas", 1584394820483, {1: Z}, G_, "Microaneurismas: retinopatia não proliferativa inicial", 38, "Azul: lâmina do slide 38."),
 ak("microalbuminuria", 1475364115656, {1: V}, G_, "Hiperfiltração → microalbuminúria", 39, "Verde: HY (2); 'aumento da permeabilidade da MB – albuminúria'."),
 ak("mesangio", 1475364123204, {1: V}, G_, "Nefropatia diabética: expansão mesangial", 39, "Verde: HY (1); 'esclerose glomerular' (Robbins)."),
 ak("nodular", 1462327588618, {1: V}, G_, "Glomerulosclerose nodular (Kimmelstiel-Wilson)", 39, "Verde: HY (2); lesão típica (Robbins fig. 24-37)."),
 ak("kimmelstiel", 1475364125638, {1: V}, G_, "Nódulos de Kimmelstiel-Wilson", 39, "Verde: HY (1); o nome no sentido inverso do anterior."),
 ak("hialina", 1462327605465, {1: V}, G_, "Arteriolosclerose hialina renal", 39, "Verde: HY (1); 'hialinização arteriolar – hipertensão'."),
 ak("itu", 1475452928405, {1: V}, G_, "DM predispõe a infecção urinária", 39, "Verde: HY (2); 'predisposição a infecções – pielonefrite'."),
 ak("dap-amputacao", 1462327570500, {1: V}, G_, "Doença arterial periférica: principal causa de amputação não traumática", 41, "Verde: HY (1); 'aterosclerose periférica – isquemia'."),
 ak("ulcera-neuropatia", 1500922191457, {1: V}, G_, "Neuropatia é o principal fator da úlcera do pé", 41, "Verde: núcleo do pé diabético (slide 41)."),
 ak("neuropatia-sensibilidade", 1522550552770, {1: V, 2: Z}, G_, "Neuropatia: perde vibração, propriocepção e temperatura", 41, "c1 verde: HY (1), propriocepção (slide 56); c2 azul."),
 ak("infeccao-dm", 1584393298504, {1: Z}, G_, "DM predispõe a infecções recorrentes", 41, "Azul: 'alterações do sistema de coagulação e recorrência das lesões'."),
 ak("gangrena", 1588632141576, {1: Z}, G_, "Úlcera infectada → gangrena → amputação", 43, "Azul: fotos dos slides 42–43."),
 ak("iam-morte", 1462327558597, {1: V}, G_, "IAM é a principal causa de morte no DM", 44, "Verde: HY (1); esquema das complicações (slides 44–45; Robbins)."),
 ak("controle-micro", 1502564999736, {1: Z}, G_, "Controle glicêmico estrito reduz sobretudo as complicações microvasculares", 44, "Azul: 'alterações metabólicas' no topo do esquema do slide 44."),
 # ---------- H. Radiologia (slides 46–57) ----------
 au("rim-inicio", "Early in diabetic nephropathy, ultrasound shows {{c1::enlarged}} kidneys from glomerular hyperfiltration", {1: Z}, H_,
    "US: rins aumentados no início", "47; veterano", "prova", "nenhum card de imagem renal do diabetes no AnKing nem nos externos.",
    [1475364112776, 1475364140189], "Azul: primeira linha do slide 47.", extra="- Late disease: small kidneys with a thin, hyperechoic cortex"),
 au("rim-final", "End-stage diabetic kidneys are small on ultrasound, with a thin and {{c1::hyperechoic}} cortex", {1: Z}, H_,
    "US: rins pequenos e hiperecogênicos no fim", "47; veterano; Robbins fig. 24-38", "prova", "nenhum card de imagem renal do diabetes no AnKing nem nos externos.",
    [1462327588618, 1475364123204], "Azul: estágio final do slide 47.", extra="- Corticomedullary differentiation is lost"),
 ak("angina-instavel", 1471880433632, {2: V}, H_, "Angina instável: ruptura de placa com oclusão incompleta", 48, "c2 verde: HY (1); placa vulnerável do esquema do slide 48."),
 ak("iam-oclusao", 1471898867686, {2: V}, H_, "IAM: ruptura de placa com oclusão completa", 48, "c2 verde: HY (1); contraste com a angina instável."),
 au("agatston", "Coronary calcium scoring by non-contrast CT quantifies calcified plaque with the {{c1::Agatston}} method", {1: Z}, H_,
    "Escore de cálcio (Agatston)", "49–50; veterano", "prova", "zero resultado para calcium score/Agatston no AnKing e nos externos.",
    [1497384403639, 1471880384775], "Azul: protocolo do slide 50.", extra="- Calcium = above <b>130 HU</b><br>- Risk stratification in <b>asymptomatic</b> patients"),
 au("angiotc", "Coronary CT angiography has a negative predictive value near 100%, so it is best to {{c1::exclude}} coronary disease", {1: Z}, H_,
    "AngioTC exclui doença coronariana", "51–52; veterano", "prova", "zero resultado para coronary CTA no AnKing e nos externos.",
    [1497384403639, 1550526492215], "Azul: indicação e limites dos slides 51–52.",
    extra="- For symptomatic patients with <b>low or intermediate</b> probability<br>- Severe lesion or high probability → invasive angiography"),
 ak("cateterismo", 1497384403639, {1: Z}, H_, "Alta probabilidade pré-teste → angiografia coronariana invasiva", 53, "Azul: padrão-ouro que também trata (slide 53)."),
 ak("avc-hipodenso", 1705849921739, {1: V}, H_, "AVC isquêmico: área hipodensa na TC sem contraste", 54, "Verde: 'mais escuro = AVC' no slide 54; leitura duradoura."),
 ak("charcot", 1584392259000, {1: V}, H_, "Neuropatia → artropatia de Charcot", 56, "c1 verde: neuropatia → destruição articular (slide 56)."),
 ak("charcot-rx", 1557250925426, {1: Z}, H_, "Radiografia do Charcot: destruição, osteófitos, perda do espaço articular", 56, "Azul: leitura das radiografias do slide 56."),
 ak("osteomielite-contigua", 1504048169634, {1: Z}, H_, "Osteomielite diabética: contígua à úlcera, polimicrobiana", 57, "Azul: complicação do pé (slide 57)."),
 ak("osteomielite-rm", 1488154325513, {1: V}, H_, "RM é o melhor exame para osteomielite aguda", 57, "Verde: HY (1); RM T1/T2/T1 C+ do slide 57."),
 au("osteo-sinal", "In osteomyelitis, the infected marrow is dark on T1 and {{c1::bright}} on fat-suppressed T2 MRI", {1: Z}, H_,
    "Sinal da osteomielite na RM", "57; veterano", "prova", "zero resultado para osteomyelitis MRI T1/T2 no AnKing e nos externos.",
    [1488154325513, 1488154340055], "Azul: leitura das sequências do slide 57.", extra="- Enhances after gadolinium (T1 C+)"),
 ak("sequestro", 1488154340055, {1: Z}, H_, "Radiografia: sequestro lítico e invólucro esclerótico", 57, "Azul: fase crônica (veterano)."),
]

# F-20261003-CLAUDE-15/19: figura do livro (Robbins), recortada, e explicação curta no verso
from nebli.ilustrar import ilustrar, anotar
from imagens import IMAGENS, LIVRO
from notas import NOTAS
MEDIA.update(LIVRO)
CARDS = anotar(ilustrar(CARDS, IMAGENS, {}), NOTAS)
