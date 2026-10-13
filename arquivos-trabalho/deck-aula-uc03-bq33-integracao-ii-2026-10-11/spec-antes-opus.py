# Especificação curada — Integração metabólica II: estados alimentares (UC03 P2, Bioquímica; Profa. Deborah, IQ-USP; 102 lâminas = Estados Alimentares I e II).
# Ordem = lâminas da versão II (54–102); a versão I (1–52) repete o mesmo conteúdo. AnKing → compartilhado (Integração I, GR02) → autoral curto.
import json, re, urllib.request
RUN_ID = "uc03-bq33-20261011a"
SHORT = "bq33"
LESSON = "2026-uc03-bioquimica-33-integracao-metabolica-ii"
DECK = "NEBLI::UC03::P2::Bioquímica::Integração metabólica II"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261011-CLAUDE-02) + plano vigente, 11/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 50 consultas), cópias NEBLI vivas de Integração I e GR02 conferidas "
         "(compartilhados), 11/10: ")
EXCLUIDOS = []
FORA_DO_RECORTE = []

_cache = {}
def _nums(src):
    if src not in _cache:
        r = json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps(
            {"action": "notesInfo", "version": 6, "params": {"notes": [src]}}).encode())))["result"][0]
        _cache[src] = sorted({int(n) for n in re.findall(r"\{\{c(\d+)::", r["fields"]["Text"]["value"])})
    return _cache[src]


def ak(key, src, cor, bloco, alvo, slide, motivo, origin=None, **kw):
    flags = {n: cor for n in _nums(src)}
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, cor, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    n = sorted({int(x) for x in re.findall(r"\{\{c(\d+)::", text)})
    return dict(key=key, kind="autoral", text=text, extra=extra, flags={i: cor for i in n}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_ = ("A-hormonios", "B-secrecao-de-insulina", "C-periodo-absortivo", "D-periodo-pos-absortivo", "E-jejum", "F-diabetes")
CARDS = [
 # ---------- A. Insulina e glucagon (lâminas 54–57) ----------
 ak("insulina-glicogenio", 1462128205014, V, A_, "Insulina promove síntese de glicogênio no músculo e fígado", 54, "Verde: papel central da insulina (lâmina 54)."),
 sh(1791054011246, "verde", A_, "Glucagon: glicogenólise e gliconeogênese", 54, "Verde: papel central do glucagon, já em Integração I e GR02."),
 sh(1791054011119, "azul", A_, "Insulina inibe a secreção de glucagon", 54, "Azul: curvas espelhadas (lâmina 55), card da GR02."),
 au("curvas-refeicao", "After a meal, plasma insulin rises and peaks within about an hour while plasma glucagon {{c1::falls}}", V, A_,
    "Curvas hormonais espelhadas após a refeição", "55, 57", "central", "AnKing trata cada hormônio isolado.", [1462131726115, 1462131783153],
    "Verde: figura central da aula (lâminas 55 e 57).", extra="- The two curves mirror each other: the insulin/glucagon ratio is what the tissues read"),
 ak("cortisol-gliconeogenese", 1462061167732, V, A_, "Cortisol estimula a gliconeogênese no jejum", 56, "Verde: o cortisol aparece ao lado do glucagon entre as refeições (lâmina 56)."),
 ak("cortisol-proteolise", 1462061124035, V, A_, "Cortisol: proteólise muscular fornece aminoácidos", 56, "Verde: HY 1 e prova 2025 P2 1.8."),
 # ---------- B. Secreção de insulina (lâmina 59) ----------
 sh(1791647354296, "verde", B_, "Glicose entra na célula β por GLUT2", 59, "Verde: primeiro passo da figura da lâmina 59."),
 ak("katp-atp", 1462127781248, V, B_, "Metabolismo da glicose gera ATP na célula β", 59, "Verde: etapa 2 da figura, HY 1."),
 ak("katp-fecha", 1462127805913, V, B_, "ATP/ADP alto fecha o canal K-ATP e despolariza", 59, "Verde: etapa 3, HY 1."),
 ak("katp-calcio", 1462127846011, V, B_, "Despolarização abre canais de Ca²⁺ dependentes de voltagem", 59, "Verde: etapa 4, HY 2."),
 ak("katp-exocitose", 1462127869624, V, B_, "Ca²⁺ intracelular dispara a exocitose dos grânulos de insulina", 59, "Verde: etapa 5, HY 2."),
 # ---------- C. Período absortivo (lâminas 58–73) ----------
 sh(1791647345621, "verde", C_, "Razão insulina/glucagon alta: armazenamento", 58, "Verde: ideia central do período absortivo."),
 au("gk-transloca", "In the fed state, glucose frees glucokinase from its regulatory protein and the enzyme moves from the nucleus to the {{c1::cytoplasm}}", Z, C_,
    "Glicoquinase transloca do núcleo para o citoplasma", "60", "central", "AnKing cobre Km e indução, não a translocação.", [1462127745460, 1462809621604],
    "Azul: texto explícito da lâmina 60.", extra="- This releases a stock of enzyme already made, so the response takes minutes"),
 sh(1791647349695, "azul", C_, "Insulina induz a glicoquinase", 60, "Azul: complementa a translocação."),
 sh(1791647345020, "azul", C_, "Glicose inibe a fosforilase hepática", 60, "Azul: a lâmina 60 destaca essa inibição."),
 au("pkb-gsk3", "Insulin activates PKB, which phosphorylates and inactivates {{c1::GSK-3}}, so glycogen synthase stays dephosphorylated and active", Z, C_,
    "PKB inativa a GSK-3", "61", "central", "AnKing não traz a cascata PKB.", [1472435698856, 1474253707546],
    "Azul: um dos quatro ramos da PKB na lâmina 61.", extra="- PKB is also called Akt"),
 au("pkb-pde", "Insulin lowers cAMP by inactivating PKA and activating {{c1::phosphodiesterase}}", Z, C_,
    "Insulina inativa PKA e ativa a fosfodiesterase", "61", "central", "sem card nos acervos.", [1474164845352, 1472435698856],
    "Azul: ramos da PKB na lâmina 61.", extra="- This switches off the glucagon signal"),
 sh(1791647349819, "verde", C_, "Insulina ativa a PP1", 61, "Verde: ramo principal para sintase ativa e fosforilase inativa."),
 ak("insulina-pfk2", 1474164845352, V, C_, "Insulina: ↓cAMP/PKA, ↑PFK-2, ↓FBPase-2", 62, "Verde: comutação PFK-2/FBPase-2 (lâmina 62)."),
 au("pdh-insulina", "In the fed state insulin favors the active, dephosphorylated {{c1::pyruvate dehydrogenase}} complex, raising acetyl-CoA from glucose", Z, C_,
    "Insulina ativa a PDH", "63", "central", "AnKing não liga a insulina à PDH.", [1474224610331, 1474224602587],
    "Azul: lâmina 63 mostra PDH aumentada.", extra="- Glycolysis, PDH and the citric acid cycle run together"),
 ak("pc-acetilcoa", 1474253931216, V, C_, "Acetil-CoA ativa a piruvato carboxilase", "65, 83", "Verde: aparece no absortivo e no pós-absortivo (lâminas 65 e 83)."),
 sh(1791647344769, "azul", C_, "NADH e ATP freiam o ciclo de Krebs", 66, "Azul: lâminas 65–66."),
 ak("citrato-citosol", 1475896543773, Z, C_, "Citrato sai da mitocôndria para o citosol", 67, "Azul: primeira etapa da síntese de ácidos graxos (lâmina 67)."),
 ak("citrato-liase", 1475896551561, Z, C_, "ATP-citrato liase gera acetil-CoA citosólico", 67, "Azul: lâmina 67."),
 ak("acc-malonil", 1475896559049, Z, C_, "Acetil-CoA carboxilase forma malonil-CoA", 67, "Azul: lâmina 67."),
 ak("malonil-cat1", 1475982778100, V, C_, "Malonil-CoA inibe a carnitina-acil transferase I", 68, "Verde: lâmina 68 destaca essa inibição."),
 ak("cpt1-carnitina", 1475982767539, R, C_, "CPT1 forma acil-carnitina", 68, "Rosa: detalhe do transporte mitocondrial."),
 ak("pentoses-nadph", 1475890910326, V, C_, "Via das pentoses fornece NADPH para síntese de ácidos graxos", 69, "Verde: lâmina 69."),
 au("g6pd-insulina", "Insulin increases the activity of {{c1::glucose-6-phosphate dehydrogenase}}, so the pentose phosphate pathway supplies NADPH for fatty acid synthesis", Z, C_,
    "Insulina estimula a G6PD", "69", "prova", "AnKing só traz a G6PD como limitante.", [1475890802493, 1475890910326],
    "Azul: guia de veteranos, aula 7.", extra="- Fatty acid synthesis consumes NADPH, which in turn pulls glucose 6-phosphate into the pentose pathway"),
 ak("vldl-figado", 1475966653488, V, C_, "Fígado empacota triacilglicerol e colesterol em VLDL", 71, "Verde: lâmina 71, exportação hepática."),
 au("exporta-lipoproteinas", "Hepatic products other than glycogen, such as triacylglycerols, phospholipids and cholesterol, leave the liver as {{c1::lipoproteins}}", Z, C_,
    "Produtos hepáticos exportados como lipoproteínas", "71", "central", "AnKing detalha só o VLDL.", [1475966653488, 1475966673184],
    "Azul: lâmina 71.", extra="- Apoproteins are part of the lipoprotein coat"),
 ak("lpl-vldl", 1475966694960, R, C_, "Lipoproteína lipase libera ácidos graxos do VLDL", 71, "Rosa: destino do VLDL, além do recorte."),
 ak("insulina-proteina", 1462128277353, V, C_, "Insulina: entrada de aminoácidos e síntese proteica", 72, "Verde: lâmina 72."),
 ak("insulina-adiposo", 1462128243453, Z, C_, "Insulina no adiposo: depósito de gordura e inibição da lipólise", 73, "Azul: lâmina 73."),
 sh(1791054011372, "azul", C_, "Insulina insere GLUT4 no músculo e no adiposo", 73, "Azul: captação periférica no absortivo."),
 # ---------- D. Período pós-absortivo (lâminas 74–85) ----------
 sh(1791647354421, "verde", D_, "Glicogenólise hepática entre as refeições", 75, "Verde: lâmina 75."),
 sh(1791647354545, "azul", D_, "Glicogênio hepático se esgota em 12–18 h", 75, "Azul: lâmina 75."),
 sh(1791647354671, "azul", D_, "Gliconeogênese hepática no jejum de 1–3 dias", 75, "Azul: lâmina 75."),
 au("pos-razao", "After the absorptive period the insulin/glucagon ratio falls and the main target of glucagon is the {{c1::liver}}", V, D_,
    "Glucagon sinaliza o jejum, alvo principal fígado", "76", "central", "AnKing não une razão e alvo.", [1462131823875, 1462131831506],
    "Verde: lâmina 76.", extra="- In the liver glucagon blocks glycogen and fatty acid synthesis and favors gluconeogenesis"),
 ak("glucagon-gliconeogenese", 1462131823875, V, D_, "Glucagon: gliconeogênese por queda da frutose-2,6-bisfosfato", 76, "Verde: lâminas 76 e 78."),
 ak("glucagon-lipolise", 1462131831506, Z, D_, "Glucagon reduz síntese de ácidos graxos e aumenta a lipólise", 76, "Azul: lâmina 76."),
 sh(1791647349571, "azul", D_, "Glucagon age por cAMP", 77, "Azul: lâmina 77."),
 sh(1791647347495, "verde", D_, "PFK-2/FBPase-2 é a mesma enzima bifuncional", 79, "Verde: lâmina 79."),
 sh(1791647347621, "azul", D_, "Glucagon, cAMP e PKA invertem a enzima bifuncional", 79, "Azul: lâmina 79."),
 au("glut4-jejum", "Without insulin, GLUT4 stays in intracellular vesicles, so muscle and adipose tissue {{c1::cannot take up}} glucose during fasting", V, D_,
    "Músculo e adiposo não captam glicose no jejum", "80", "prova", "AnKing só traz o GLUT4 estimulado pela insulina.", [1791054011372, 1462809498251],
    "Verde: lâmina 80 e prova 2024 P2 1.3.", extra="- Their glucose uptake depends on insulin"),
 au("tecidos-independentes", "In fasting, glucose uptake is restricted to tissues that do not need insulin, namely the brain, red blood cells and {{c1::renal medulla}}", Z, D_,
    "Cérebro, hemácias e medula renal oxidam apenas glicose", "80", "central", "AnKing não cita a medula renal.", [1462809498251, 1462809621604],
    "Azul: lâmina 80.", extra="- They have transporters besides GLUT4"),
 sh(1791647349946, "azul", D_, "Lipase hormônio-sensível quebra triacilglicerol", 81, "Azul: lâmina 81."),
 sh(1791647350296, "azul", D_, "Insulina inibe a lipase hormônio-sensível", 81, "Azul: lâmina 81."),
 au("ag-albumina", "Fatty acids released by adipocytes travel in the blood bound to {{c1::albumin}}", R, D_,
    "Ácidos graxos no sangue ligados à albumina", "81", "lateral", "sem card nos acervos.", [1475982732554, 1475966773797],
    "Rosa: legenda da figura da lâmina 81.", extra="- The free fatty acids then reach liver, muscle and heart"),
 ak("betaox-acetilcoa", 1475982750794, Z, D_, "β-oxidação gera acetil-CoA", 82, "Azul: lâmina 82."),
 au("pdk4-acetilcoa", "Acetyl-CoA from β-oxidation activates PDK4, which phosphorylates and inhibits the {{c1::pyruvate dehydrogenase}} complex", Z, D_,
    "Acetil-CoA da β-oxidação ativa PDK4 e inibe a PDH", "83", "central", "AnKing não tem PDK4.", [1474224610331, 1474253934255],
    "Azul: lâmina 83.", extra="- Pyruvate is spared for gluconeogenesis, since pyruvate carboxylase is activated at the same time"),
 sh(1791647350421, "azul", D_, "Glicerol do adiposo vira glicose no fígado", 83, "Azul: prova 2023 P1 2.2."),
 au("glicerol-quinase", "Glycerol from lipolysis enters hepatic gluconeogenesis after phosphorylation by {{c1::glycerol kinase}}", Z, D_,
    "Glicerol-quinase abre o caminho do glicerol", "84", "prova", "AnKing não traz a enzima.", [1475982746310, 1462913170662],
    "Azul: prova 2023 P1 2.2 e guia de veteranos.", extra="- Glycerol 3-phosphate is then oxidized to dihydroxyacetone phosphate"),
 ak("metformina-gpdh", 1462913170662, V, D_, "Metformina inibe a glicerol-3-fosfato desidrogenase mitocondrial", 84, "Verde: HY 2 e prova 2023 P1 2.2."),
 sh(1791647348245, "azul", D_, "Músculo não faz gliconeogênese: sem glicose-6-fosfatase", 84, "Azul: figura da lâmina 84."),
 au("jejum-inflamatorio", "In acute infection, cytokines such as TNF-α and IL-6 cause {{c1::insulin resistance}} in muscle and reduce its glucose uptake", Z, D_,
    "Jejum relativo inflamatório", "84", "prova", "AnKing não liga citocinas ao jejum.", [1462061153036, 1462061124035],
    "Azul: prova 2025 P2 1.8.", extra="- Anorexia and the stress hormones (cortisol, catecholamines) add to the catabolic state"),
 # ---------- E. Jejum (lâminas 86–91) ----------
 au("aa-alanina-glutamina", "In fasting, most amino acids are converted to {{c1::alanine}} and {{c2::glutamine}} before leaving muscle", Z, E_,
    "Aminoácidos viram alanina e glutamina", "86", "central", "AnKing cobre transporte de NH3, não o resumo da aula.", [1476241277886, 1476241344675],
    "Azul: lâmina 86.", extra="- Their carbon skeletons are pyruvate and α-ketoglutarate"),
 ak("alanina-musculo", 1476241277886, Z, E_, "Alanina transporta NH₃ do músculo", 86, "Azul: lâmina 86."),
 ak("glutamina-transporte", 1476241344675, Z, E_, "Glutamina é a principal forma de transporte de NH₃", 86, "Azul: lâmina 86."),
 ak("alanina-gliconeogenica", 1502927648775, Z, E_, "Alanina é o principal aminoácido gliconeogênico no fígado", 86, "Azul: lâmina 86 e ciclo alanina-glicose."),
 ak("cetogenicos", 1472426420971, Z, E_, "Leucina e lisina são só cetogênicos", 86, "Azul: figura de aminoácidos glico/cetogênicos da lâmina 86."),
 au("gln-rim", "In fasting, the kidney uses glutamine for gluconeogenesis and releases ammonia that helps {{c1::acid-base}} balance", R, E_,
    "Glutamina na gliconeogênese renal", "86", "lateral", "sem card nos acervos.", [1476241344675, 1502927648775],
    "Rosa: guia de veteranos, detalhe renal.", extra="- The liver makes most glucose but the kidney contributes in prolonged fasting"),
 au("balanco-n-negativo", "Fasting proteolysis without any nitrogen intake creates a {{c1::negative}} nitrogen balance", R, E_,
    "Balanço nitrogenado negativo", "86", "lateral", "sem card nos acervos.", [1476241277886, 1476241344675],
    "Rosa: guia de veteranos.", extra="- The nitrogen leaves as urea"),
 au("reservas-tag", "The triacylglycerols stored in the adipose tissue of a normal-weight adult can fuel basal metabolism for about {{c1::three months}}", R, E_,
    "Reservas de combustível: TAG sustenta cerca de 3 meses", "88; Lehninger cap. 23", "lateral", "sem card nos acervos.", [1476502674112, 1462131726115],
    "Rosa: tabela de combustíveis do capítulo.", extra="- Glycogen lasts only hours to about a day, and protein is the reserve to be spared"),
 sh(1791647351570, "azul", E_, "Ciclo de Cori: piruvato vira lactato", 87, "Azul: lâmina 87."),
 sh(1791647352896, "verde", E_, "Após 3 dias, cetonas são o combustível principal do cérebro", 88, "Verde: gráfico da lâmina 88."),
 ak("cetonas-cerebro-2-3", 1560052544736, Z, E_, "Cérebro obtém até ⅔ da energia de corpos cetônicos no jejum prolongado", 88, "Azul: gráfico da lâmina 88; card MCAT.", origin="MCAT"),
 ak("cetonas-tecidos", 1476154185261, V, E_, "Corpos cetônicos servem cérebro, músculo e rim", "88, 90", "Verde: lâminas 88–90."),
 sh(1791647349321, "azul", E_, "A cetogênese ocorre no fígado", 89, "Azul: lâmina 89."),
 sh(1791647349146, "azul", E_, "Acetil-CoA da β-oxidação: cetogênese ou Krebs", 89, "Azul: lâmina 89."),
 sh(1791647353546, "azul", E_, "Hemácias não usam corpos cetônicos", 89, "Azul: figura da lâmina 89."),
 ak("tres-cetonas", 1476154090457, Z, E_, "Acetoacetato, β-hidroxibutirato e acetona", 90, "Azul: lâmina 90."),
 ak("hmg-sintase", 1476154085131, Z, E_, "HMG-CoA sintase limita a cetogênese", 90, "Azul: lâmina 90."),
 ak("bhb-extra-hepatico", 1476154123577, Z, E_, "β-hidroxibutirato vai aos tecidos extra-hepáticos", 90, "Azul: lâmina 90."),
 ak("acetona-pulmao", 1476154118823, R, E_, "Acetona é exalada", 90, "Rosa: detalhe."),
 ak("tioforase", 1476154138229, R, E_, "Tecidos extra-hepáticos ativam o acetoacetato com tioforase", 90, "Rosa: detalhe."),
 au("cetogenese-oaa", "In prolonged fasting oxaloacetate is drained into gluconeogenesis, so acetyl-CoA from β-oxidation is directed to {{c1::ketone body}} synthesis", V, E_,
    "Por que a cetogênese ocorre", "90", "central", "AnKing não explica a causa.", [1476154095169, 1476154085131],
    "Verde: ideia da lâmina 90.", extra="- The liver exports the ketone bodies but cannot use them"),
 au("cetonas-poupam", "Ketone bodies as fuel for the brain reduce the need for gluconeogenesis from amino acids, thereby {{c1::sparing muscle protein}}", Z, E_,
    "Cetonas poupam proteína muscular", "88, 90", "prova", "AnKing não une cetonas e proteína.", [1476154185261, 1476502674112],
    "Azul: prova 2024 P2 1.3.", extra="- Plasma ketone bodies rise over days of starvation while glucose falls"),
 # ---------- F. Diabetes (lâminas 92–100) ----------
 sh(1791054010222, "verde", F_, "Definição: hiperglicemia por defeito de secreção, ação ou ambos", 92, "Verde: definição da lâmina 92."),
 au("t1-idade", "Type 1 diabetes usually starts before age {{c1::20}}, in lean individuals", Z, F_,
    "DM1: início jovem, magro", "93", "central", "AnKing usa corte de 30 anos, aula usa 20.", [1462326996658, 1462326105448],
    "Azul: lâmina 93.", extra="- Typical symptoms: polydipsia, polyuria, polyphagia and weight loss"),
 au("t2-idade", "Type 2 diabetes usually starts after age {{c1::40}}, in obese, sedentary individuals", Z, F_,
    "DM2: início após os 40, obeso", "93", "central", "AnKing não traz o perfil da aula.", [1462327011039, 1462326951145],
    "Azul: lâmina 93.", extra="- It accounts for more than 90% of diabetes cases"),
 au("t1-absoluta", "Type 1 diabetes is an absolute insulin deficiency, whereas type 2 combines relative deficiency with {{c1::insulin resistance}}", V, F_,
    "DM1 deficiência absoluta, DM2 deficiência relativa e resistência", "93", "central", "AnKing separa os dois tipos em cards isolados.", [1462326105448, 1462326951145],
    "Verde: comparação central da lâmina 93.", extra="- Type 2 may start with normal or high insulin levels"),
 au("t1-hla", "Type 1 diabetes inheritance is associated with the {{c1::HLA}} system", Z, F_,
    "DM1 associado ao HLA", "93", "central", "AnKing cita DR3/DR4, não a associação geral.", [1462326961450, 1462327016536],
    "Azul: lâmina 93.", extra="- Type 2 diabetes inheritance is polygenic"),
 sh(1791054010997, "verde", F_, "DM1: destruição autoimune das células β por CD8+", 94, "Verde: lâmina 94."),
 sh(1791054010347, "azul", F_, "DM1: predisposição genética mais fraca que DM2", 93, "Azul: lâmina 93."),
 sh(1791054010747, "azul", F_, "DM1: cetoacidose", 93, "Azul: lâmina 93."),
 sh(1791054010873, "azul", F_, "DM2: estado hiperosmolar", 93, "Azul: lâmina 93, coma hiperosmolar."),
 au("t1-jejum", "In untreated type 1 diabetes the insulin/glucagon ratio stays low, so the liver runs the {{c1::fasting}} program despite high blood glucose", V, F_,
    "DM1 é semelhante ao jejum", "95", "central", "AnKing não faz a ponte jejum-diabetes.", [1462131802276, 1462327073683],
    "Verde: lâmina 95 'semelhante ao jejum'.", extra="- Gluconeogenesis, lipolysis, proteolysis and ketone body production are all on"),
 sh(1791054011545, "verde", F_, "DM1: glucagon sem oposição", 95, "Verde: lâmina 95, hiperglucagonemia."),
 sh(1791054011671, "verde", F_, "DM1: lipólise e cetogênese", 95, "Verde: lâmina 95."),
 sh(1791054012320, "azul", F_, "Glicose retida no túbulo causa diurese osmótica", 95, "Azul: lâmina 95, sobrecarga renal."),
 sh(1791054015196, "rosa", F_, "Glicação não enzimática da hemoglobina forma HbA1c", 95, "Rosa: proteínas glicadas perdem função (lâmina 95)."),
 au("t2-insulina-normal", "In type 2 diabetes insulin levels may be normal or {{c1::elevated}}, but the tissues respond poorly", Z, F_,
    "DM2: insulina normal ou elevada", "96", "central", "AnKing diz 'variável'.", [1462327053167, 1462326951145],
    "Azul: lâmina 96.", extra="- Late in the disease secretion falls"),
 au("t2-captacao", "Insulin resistance in type 2 diabetes blocks glucose entry into muscle and {{c1::adipose}} tissue", Z, F_,
    "Resistência: inibição da entrada de glicose no músculo e adiposo", "97", "central", "sem card específico nos acervos.", [1462327139204, 1462326951145],
    "Azul: lâmina 97.", extra="- GLUT4 translocation to the membrane is impaired"),
 au("t2-falencia", "Chronic stimulation of the β cells in type 2 diabetes leads to their {{c1::failure}} and deficient insulin secretion", V, F_,
    "Estimulação crônica leva à falência β", "97", "central", "AnKing cita só a falha avançada.", [1462327053167, 1462327139204],
    "Verde: lâminas 97 e 99.", extra="- Compensatory hyperinsulinemia comes first"),
 au("t2-sindrome-metabolica", "Metabolic syndrome in type 2 diabetes includes obesity, high LDL, low HDL and {{c1::hypertension}}", Z, F_,
    "DM2 e síndrome metabólica", "97", "central", "AnKing não lista os componentes do conjunto da aula.", [1462327139204, 1462326951145],
    "Azul: lâmina 97.", extra="- Insulin resistance is the common pathogenic factor"),
 au("t2-triangulo", "In type 2 diabetes hyperglycemia results from deficient insulin secretion, reduced glucose uptake by muscle and fat and increased {{c1::hepatic glucose production}}", V, F_,
    "Defeitos metabólicos do DM2", "98", "central", "AnKing descreve cada defeito isolado.", [1462327053167, 1462327139204],
    "Verde: figura da lâmina 98 (DeFronzo).", extra="- Insulin resistance drives the loop"),
 au("t2-resistencia-antes", "In type 2 diabetes, insulin resistance appears years before the {{c1::compensatory}} rise in plasma insulin", Z, F_,
    "Resistência precede a hiperinsulinemia", "99", "central", "sem card nos acervos.", [1462327139204, 1462128153992],
    "Azul: lâmina 99.", extra="- Hyperinsulinemia keeps glucose near normal until the β cells fail"),
 au("t2-dieta", "Early type 2 diabetes can be managed with {{c1::diet and exercise}}, which reduce the body's need for insulin", Z, F_,
    "DM2 inicial: dieta e exercício", "100", "central", "sem card nos acervos.", [1462913151403, 1462327127564],
    "Azul: lâmina 100.", extra="- Oral antidiabetics are added as the disease progresses"),
 sh(1791054012596, "azul", F_, "DM2: a função β declina e a secreção cai", 97, "Azul: lâmina 97."),
 sh(1791054012719, "azul", F_, "Hiperinsulinemia crônica reduz os receptores", 97, "Azul: lâmina 97."),
 sh(1791054012847, "azul", F_, "Resistência à insulina na síndrome metabólica", 97, "Azul: lâmina 97."),
 sh(1791054013770, "azul", F_, "Metformina: primeira linha no DM2", 100, "Azul: lâmina 100."),
 sh(1791054013895, "azul", F_, "Metformina reduz a gliconeogênese hepática", 100, "Azul: lâmina 100, redução da produção hepática."),
 sh(1791054014146, "azul", F_, "Sulfonilureias e meglitinidas estimulam a secreção de insulina", 100, "Azul: lâmina 100."),
 sh(1791054014320, "azul", F_, "Inibidores da α-glicosidase retardam a absorção de carboidratos", 100, "Azul: lâmina 100."),
 sh(1791054014020, "rosa", F_, "Glitazonas aumentam a sensibilidade à insulina", 100, "Rosa: lâmina 100, captação celular."),
]

VERSO = {
 "insulina-glicogenio": "- Insulin is the hormone of storage: it also stimulates fat and protein synthesis",
 "cortisol-proteolise": "- The amino acids go to the liver for gluconeogenesis",
 "katp-atp": "- Glucokinase makes this step proportional to blood glucose",
 "katp-calcio": "- The Ca2+ rise is the trigger for insulin granule release",
 "pc-acetilcoa": "- Acetyl-CoA accumulates when fatty acids are oxidized in fasting",
 "citrato-liase": "- This enzyme links the mitochondrial citrate to cytosolic fatty acid synthesis",
 "pentoses-nadph": "- Fatty acid synthesis consumes NADPH",
 "vldl-figado": "- VLDL carries triacylglycerol from the liver to peripheral tissues",
 "lpl-vldl": "- Lipoprotein lipase sits on the capillary endothelium of adipose tissue and muscle",
 "glucagon-gliconeogenese": "- Low fructose 2,6-bisphosphate releases the block on fructose 1,6-bisphosphatase",
 "glucagon-lipolise": "- Fatty acids become the fuel, sparing glucose for the brain",
 "cetogenicos": "- Other amino acids are glucogenic or both",
 "cetonas-cerebro-2-3": "- This reduces the brain's need for glucose and spares muscle protein",
 "hmg-sintase": "- It acts in liver mitochondria",
 "bhb-extra-hepatico": "- The liver exports ketone bodies but cannot use them",
 "acetona-pulmao": "- Acetone is the volatile ketone body responsible for the fruity breath",
}
DUPLICACAO = {
 "pos-razao": "ganho: alvo hepático do glucagon logo após o absortivo; sh-glucagon e curvas cobram outros alvos",
 "aa-alanina-glutamina": "ganho: resumo da lâmina 86 (alanina e glutamina); os cards do AnKing cobram o transporte de NH3 por tecido",
 "t1-jejum": "ganho: ponte jejum-diabetes da lâmina 95; os cards da GR02 cobram glucagon e cetose isolados",
 "t2-triangulo": "ganho: três defeitos da figura 98 em uma frase; os cards da GR02 cobram cada defeito isolado",
}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]

NEGRITO = {  # F-20261011-CLAUDE-01: autoral com 1–3 trechos de contexto em negrito (padrão AnKing medido)
 "curvas-refeicao": ["plasma insulin", "plasma glucagon"], "gk-transloca": ["glucokinase", "regulatory protein"], "pkb-gsk3": ["PKB", "glycogen synthase"],
 "pkb-pde": ["cAMP", "PKA"], "pdh-insulina": ["insulin", "acetyl-CoA"], "g6pd-insulina": ["Insulin", "NADPH"], "exporta-lipoproteinas": ["Hepatic products", "cholesterol"],
 "pos-razao": ["insulin/glucagon ratio", "glucagon"], "glut4-jejum": ["GLUT4", "muscle and adipose tissue"], "tecidos-independentes": ["glucose uptake", "brain, red blood cells"],
 "ag-albumina": ["Fatty acids", "adipocytes"], "pdk4-acetilcoa": ["Acetyl-CoA from β-oxidation", "PDK4"], "glicerol-quinase": ["Glycerol", "gluconeogenesis"],
 "jejum-inflamatorio": ["acute infection", "TNF-α and IL-6"], "aa-alanina-glutamina": ["amino acids", "muscle"], "gln-rim": ["kidney", "glutamine"],
 "balanco-n-negativo": ["proteolysis", "nitrogen intake"], "cetogenese-oaa": ["oxaloacetate", "β-oxidation"], "cetonas-poupam": ["Ketone bodies", "brain"],
 "t1-idade": ["Type 1 diabetes", "lean"], "t2-idade": ["Type 2 diabetes", "obese, sedentary"], "t1-absoluta": ["Type 1 diabetes", "type 2"],
 "t1-hla": ["Type 1 diabetes", "inheritance"], "t1-jejum": ["untreated type 1 diabetes", "insulin/glucagon ratio"], "t2-insulina-normal": ["type 2 diabetes", "insulin levels"],
 "t2-captacao": ["Insulin resistance", "muscle"], "t2-falencia": ["β cells", "type 2 diabetes"], "t2-sindrome-metabolica": ["Metabolic syndrome", "obesity"],
 "t2-triangulo": ["type 2 diabetes", "hyperglycemia"], "t2-resistencia-antes": ["insulin resistance", "plasma insulin"], "t2-dieta": ["Early type 2 diabetes", "insulin"], "reservas-tag": ["triacylglycerols", "adipose tissue"],
}
for c in CARDS:
    if c["kind"] == "autoral" and c["key"] in NEGRITO:
        t = c["text"]
        for term in NEGRITO[c["key"]]:
            parts = re.split(r"(\{\{.*?\}\}|<[^>]+>)", t)
            for i, p in enumerate(parts):
                if not (p.startswith("{{") or p.startswith("<")) and term in p:
                    parts[i] = p.replace(term, f"<b>{term}</b>", 1); break
            else:
                raise SystemExit(f"negrito: '{term}' não está fora do cloze em {c['key']}")
            t = "".join(parts)
        c["text"] = t
