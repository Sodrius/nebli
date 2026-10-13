# Especificação curada — Introdução à farmacologia e mecanismos de ação dos fármacos (UC19 P1, Farmacologia básica; 69 lâminas).
# Gerada a partir de inventario.py. Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card.
# Refeita em 11/10 no pipeline atual (F-20261011-CLAUDE-05); a instalação de 06/10 não existe mais no Anki. Seleção AnKing de 06/10
# (refacao_spec.py da corrida anterior) reaproveitada e conferida; conflitos científicos de leitura-fontes.md aplicados.
RUN_ID = "uc19-fa01-20261011a"
SHORT = "fa01"
LESSON = "2026-uc19-farmacologia-01-introducao-mecanismos"
DECK = "NEBLI::UC19::P1::Farmacologia::Introdução à farmacologia e mecanismos de ação"
CRITERIOS = "MEMORY.md (UC19 F-20261006-CODEX-02/04; protocolo 11/10) + FEEDBACKS F-20261011-CLAUDE-05 + plano 08/10, 11/10"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 85 consultas, 11/10) e seleção de 06/10 "
         "(busca-externos.md da corrida anterior): ")
EXCLUIDOS = [
 (1490066326802, "mnemônico de índice terapêutico estreito: lista de memorização, a aula dá três exemplos e o card próprio cobra os três"),
 (1695592254772, "Lightyea calcula IT como ED50 − LD50 (subtração): errado; IT é razão"),
 (1467833798088, "talidomida por homeodomínio: mecanismo embriológico fora do recorte de estereoisomeria"),
]
FORA_DO_RECORTE = ["história da farmacologia (lâminas 4–15): sem autorais históricos (F-20261006-CODEX-02)",
                   "doses e nomes comerciais de anestésicos odontológicos (lâmina 69)",
                   "farmacocinética quantitativa (aulas seguintes)"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_, G_, H_ = ("A-o-que-e-farmacologia", "B-alvos", "C-interacao-farmaco-alvo", "D-agonismo", "E-antagonismo",
                                  "F-janela-terapeutica", "G-perda-de-resposta", "H-extras")
EF = [1565120487647, 1490066276769]  # espelhos de conceito geral
CARDS = [
 # ---------- A. O que é farmacologia (lâminas 2–24) ----------
 ak("camp-ac", 1461857237570, {1: V, 2: V}, A_, "Gs → adenilato ciclase → AMPc", 2, "Verde: AMPc como segundo mensageiro (lâmina 2, Sutherland); base da sinalização da aula."),
 ak("camp-pka", 1461857273344, {1: V, 2: V}, A_, "AMPc ativa PKA", 2, "Verde: cadeia AMPc → PKA → fosforilação (fosforilase) da lâmina 2."),
 au("dose-veneno", "The difference between a <b>medicine</b> and a <b>poison</b> lies in the {{c1::dose}}", {1: V}, A_, "Princípio dose-toxicidade (Paracelso)", "9; 60",
    "central", "sem card do princípio nos acervos (busca 'paracelso').", [1490066320396, 1490066323578], "Verde: princípio que a aula retoma no índice terapêutico (lâmina 60).",
    extra="- The same drug can have therapeutic, toxic and lethal doses"),
 au("pequenas-complexas", "<b>Drugs</b> can be small molecules such as aspirin or complex {{c1::biologics}} such as insulin, vaccines and monoclonal antibodies",
    {1: Z}, A_, "Fármacos pequenos × complexos", "3; 16", "central", "busca 'biofarmaco' só traz anticorpos específicos.", [1489968442057, 1565120487647],
    "Azul: objetivo 3 (massa molecular, fármaco convencional × biofármaco).", extra="- Size and chemical nature affect pharmacodynamics and pharmacokinetics"),
 ak("fase1", 1485913667420, {1: V}, A_, "Fase I", 16, "Verde: fases clínicas (lâmina 16), HY 1 e duradouro."),
 ak("fase2", 1485913675748, {1: V}, A_, "Fase II", 16, "Verde: fases clínicas, HY 1."),
 ak("fase3", 1485913688921, {1: V}, A_, "Fase III", 16, "Verde: fases clínicas, HY 1."),
 ak("fase4", 1485913697186, {1: V}, A_, "Fase IV", 16, "Verde: farmacovigilância pós-comercialização, HY 1 (a lâmina põe 1–5 antes do paciente; card corrige)."),
 au("farmaco-def", "A <b>drug</b> is a substance of known {{c1::structure}} that alters cell function, usually by acting on a pharmacological target",
    {1: V}, A_, "Definição de fármaco", "17; 18", "central", "AnKing não define fármaco.", EF, "Verde: definição pedida no objetivo 1.",
    extra="- Some drugs act without a target, such as osmotic diuretics and antacids"),
 au("medicamento", "A <b>medication</b> is the {{c1::drug}} formulated with excipients for administration to the patient", {1: V}, A_,
    "Medicamento = fármaco + excipiente", 18, "central", "sem card nos acervos.", EF, "Verde: distinção fármaco × medicamento × remédio (objetivo 1).",
    extra="- Amoxicillin–clavulanate suspension lists its excipients (xanthan gum, aspartame, flavors)"),
 au("remedio", "A <b>remedy</b> is any substance or resource with a beneficial effect, used to obtain cure or {{c1::relief}}", {1: Z}, A_,
    "Remédio", 18, "central", "sem card nos acervos.", EF, "Azul: terceiro termo da lâmina 18.", extra="- A remedy need not be a drug"),
 sh(1791668521339, "azul", A_, "Associação: clavulanato inibe β-lactamase", 19, "Azul: exemplo de associação medicamentosa (lâmina 19); card de Antibióticos (mb32)."),
 au("farmacologia-medica", "<b>Medical pharmacology</b> studies drugs used for the diagnosis, {{c1::prevention}} and treatment of disease", {1: Z}, A_,
    "Farmacologia médica", 20, "central", "sem card nos acervos.", EF, "Azul: definição do objetivo 1.",
    extra="- Its major areas are pharmacokinetics, pharmacodynamics and toxicology"),
 au("toxicologia", "<b>Toxicology</b>, usually treated as a subarea of pharmacology, studies the {{c1::adverse}} effects of chemical agents on living systems",
    {1: Z}, A_, "Toxicologia", 20, "central", "busca 'toxicologia' sem resultado.", EF, "Azul: objetivo 1."),
 ak("pk-pd", 1565120487647, {1: V}, A_, "Farmacocinética × farmacodinâmica", "21, 22", "Verde: o que o corpo faz ao fármaco × o que o fármaco faz ao corpo.", origin="Referências Externas"),
 au("adme", "<b>Pharmacokinetics</b> follows the drug through absorption, distribution, {{c1::metabolism}} and excretion", {1: V}, A_, "ADME", 21,
    "central", "sem card ADME nos acervos.", [1565120487647, 1485913667420], "Verde: ADME (lâmina 21; objetivo 1).",
    extra="- Elimination happens by metabolism or by excretion"),
 au("pd-def", "<b>Pharmacodynamics</b> covers drug–target interactions, {{c1::dose–response}} phenomena and mechanisms of therapeutic and toxic action",
    {1: V}, A_, "Farmacodinâmica", 22, "central", "Lightyea só tem a frase PK × PD.", [1565120487647, 1490066276769], "Verde: lâmina 22."),
 au("fase-biofarmaceutica", "After oral intake, the <b>tablet</b> must disintegrate and {{c1::dissolve}} (<b>biopharmaceutical phase</b>) before the drug can be absorbed",
    {1: Z}, A_, "Fase biofarmacêutica", 23, "central", "sem card nos acervos.", [1565120487647, 1485913667420], "Azul: lâmina 23 (administração → efeito).",
    extra="- Then come pharmacokinetics and pharmacodynamics"),
 au("alvo-sem-endereco", "A drug acts wherever its <b>target</b> is expressed, so it cannot {{c1::choose}} the painful site", {1: Z}, A_,
    "Fármaco não sabe onde dói", "24; 35", "central", "sem card nos acervos.", [1522203660054, 1565120487647], "Azul: lâmina 24 (Dorflex).",
    extra="- The same target in other tissues explains adverse effects"),

 # ---------- B. Alvos farmacológicos (lâminas 25–34) ----------
 au("alvos-quatro", "The main <b>drug targets</b> are receptors, ion channels, enzymes and {{c1::transporters}}", {1: V}, B_, "Quatro alvos proteicos", 25,
    "central", "sem card de lista de alvos.", [1461866207939, 1472487477564, 1484950518844], "Verde: lâmina 25; objetivo 2.",
    extra="- Nucleic acids are also targets, as for anticancer drugs"),
 ak("ionotropico", 1555083517363, {1: Z, 2: Z}, B_, "Receptor ionotrópico", 25, "Azul: tipos de receptor da lâmina 25.", origin="Referências Externas"),
 ak("gpcr", 1522203660054, {1: V, 2: V}, B_, "GPCR", 25, "Verde: GPCR, maior família de alvos (lâminas 25–26)."),
 ak("gq", 1477005434793, {1: V, 2: V}, B_, "Gq → PLC → IP3/Ca", 25, "Verde: sinalização GPCR."),
 ak("gs", 1477011384108, {1: V, 2: V}, B_, "Gs → AMPc", 25, "Verde: sinalização GPCR."),
 ak("gi", 1477011377426, {1: V, 2: V}, B_, "Gi ↓ AMPc", 25, "Verde: sinalização GPCR."),
 ak("rtk", 1461866207939, {1: V}, B_, "Receptor ligado a quinase", 25, "Verde: tipo de receptor da lâmina 25."),
 sh(1791627550153, "verde", B_, "Receptor nuclear", 25, "Verde: tipo de receptor da lâmina 25; card de Eucariotos I (bm46)."),
 ak("gaba-canal", 1484768461819, {1: V}, B_, "Canal controlado por ligante (GABA-A)", 25, "Verde: representante do canal controlado por ligante (tipo de alvo, lâmina 25), HY 2."),
 au("druggable", "<b>GPCRs</b> are the largest single family of targets of {{c1::approved}} drugs", {1: R}, B_, "Genoma 'druggable'", 26,
    "lateral", "sem card nos acervos.", [1522203660054, 1461866207939], "Rosa: gráfico da lâmina 26 (~33% dos alvos).",
    extra="- About 667 human targets were known for approved drugs in 2017"),
 ak("cisplatina", 1509225165945, {1: Z}, B_, "Cisplatina forma ligações cruzadas no DNA", 27, "Azul: ácidos nucleicos como alvo (lâmina 27).", clinica_lateral=True),
 ak("doxo-dna", 1509235247004, {1: Z, 2: Z}, B_, "Doxorrubicina intercala e inibe topo II", 27, "Azul: corrige a lâmina (antraciclina não faz crosslink).", clinica_lateral=True),
 ak("cis-nefro", 1509225955344, {1: Z}, B_, "Nefrotoxicidade da cisplatina", 28, "Azul: efeito adverso principal (lâmina 28).", clinica_lateral=True),
 ak("doxo-cardio", 1509235473720, {1: Z}, B_, "Cardiotoxicidade da doxorrubicina", 28, "Azul: efeito adverso principal (lâmina 28).", clinica_lateral=True),
 ak("doxo-alopecia", 1509234614416, {1: R}, B_, "Alopecia por antraciclina", 28, "Rosa: efeito adverso secundário da lâmina 28."),
 au("nitro-prodroga", "<b>Nitroglycerin</b> is a {{c1::prodrug}} that releases nitric oxide in vascular smooth muscle", {1: V}, B_,
    "Nitroglicerina é pró-fármaco", "29; 30", "central", "AnKing não tem nitroglicerina como pró-fármaco.", [1472743774495, 1461865849072],
    "Verde: lâmina 29 ('na verdade, pró-fármacos').", extra="- Headaches in dynamite workers came from the same vasodilation"),
 ak("nitrato-no", 1472743774495, {1: V}, B_, "Nitrato → NO", 30, "Verde: mecanismo da nitroglicerina."),
 ak("nitrato-angina", 1471880414063, {2: Z}, B_, "Nitrato alivia angina", 30, "Azul: uso clínico da lâmina 30.", clinica_lateral=True),
 ak("nitrato-tolerancia", 1472747925827, {1: V}, B_, "Tolerância a nitratos", 29, "Verde: tolerância (segunda-feira × fim de semana), objetivo 9."),
 sh(1791625430456, "verde", B_, "NOS produz NO da arginina", 30, "Verde: NO a partir de L-arginina; card da Ativação de linfócitos T (im45)."),
 au("nos-isoformas", "Nitric oxide is made by three <b>NO synthases</b>, endothelial, neuronal and {{c1::inducible}} (eNOS, nNOS, iNOS)", {1: R}, B_,
    "Três isoformas da NOS", 30, "lateral", "AnKing só tem a iNOS isolada.", [1461865844254, 1497451553581], "Rosa: detalhe da lâmina 30."),
 ak("gc", 1461865849072, {1: V}, B_, "NO ativa guanilato ciclase solúvel", 30, "Verde: NO → heme da GC → GMPc."),
 ak("gmpc-pkg", 1461865801747, {1: V}, B_, "GMPc → PKG → relaxamento", 30, "Verde: cadeia NO."),
 ak("gmpc-vaso", 1472747773497, {1: V}, B_, "Nitrato ↑ GMPc", 30, "Verde: cadeia NO → GMPc → relaxamento do músculo liso (lâmina 30), HY 1."),
 sh(1791147106101, "rosa", B_, "NO inibe agregação plaquetária (endotélio: PGI2 e NO)", 30, "Rosa: efeito antiagregante do NO citado na lâmina 30; card já vivo em outra aula."),
 ak("pde5", 1463081026525, {1: V, 2: V, 3: V}, B_, "Sildenafil inibe PDE5", 30, "Verde: PDE5 degrada GMPc (lâmina 30)."),
 ak("pde5-nitrato", 1472747945251, {1: Z}, B_, "Nitrato + PDE5 → hipotensão", 30, "Azul: consequência direta da cadeia.", clinica_lateral=True),
 ak("eca", 1474686237808, {1: Z}, B_, "IECA inibe ECA", 31, "Azul: tabela de enzimas (lâmina 31).", clinica_lateral=True),
 sh(1791743346085, "verde", B_, "Aspirina acetila COX", 31, "Verde: AINE/COX e inibição irreversível (lâminas 31 e 54); card de Inflamação início/resolução (im37)."),
 ak("carbidopa", 1485226910732, {1: Z, 2: Z}, B_, "Carbidopa inibe DOPA descarboxilase", 31, "Azul: tabela de enzimas.", clinica_lateral=True),
 ak("mtx-dhfr", 1509139733312, {1: Z}, B_, "Metotrexato inibe DHFR", 31, "Azul: tabela de enzimas.", clinica_lateral=True),
 ak("irinotecano", 1509288185655, {1: R}, B_, "Irinotecano inibe topo I", 31, "Rosa: detalhe da tabela.", clinica_lateral=True),
 ak("citarabina", 1509215835845, {1: R}, B_, "Citarabina e DNA polimerase", 31, "Rosa: detalhe da tabela.", clinica_lateral=True),
 ak("estatina", 1475982725907, {1: Z}, B_, "Estatina inibe HMG-CoA redutase", 31, "Azul: tabela de enzimas.", clinica_lateral=True),
 ak("nrti", 1502070062514, {1: R, 2: R, 3: R}, B_, "AZT inibe transcriptase reversa", 31, "Rosa: detalhe da tabela.", clinica_lateral=True),
 ak("protease-hiv", 1502070156173, {1: R}, B_, "Inibidor de protease do HIV", 31, "Rosa: detalhe da tabela."),
 ak("digoxina", 1472487477564, {1: Z}, B_, "Digoxina inibe Na/K-ATPase", 31, "Azul: tabela de enzimas.", clinica_lateral=True),
 ak("ibp", 1461624498591, {1: Z, 2: Z}, B_, "Omeprazol inibe H/K-ATPase", 31, "Azul: tabela de enzimas e transportadores.", clinica_lateral=True),
 ak("pde3", 1472487655906, {1: R}, B_, "Milrinona inibe PDE3", 31, "Rosa: detalhe da tabela.", clinica_lateral=True),
 ak("manitol", 1475636907165, {1: V, 2: V}, B_, "Manitol: diurético osmótico", 32, "Verde: fármaco sem alvo (lâmina 32)."),
 ak("manitol-cerebro", 1475636911457, {1: Z, 2: Z}, B_, "Manitol reduz edema cerebral", 32, "Azul: uso da lâmina 32.", clinica_lateral=True),
 au("antiacido", "<b>Antacids</b> act without a drug target, by {{c1::chemically neutralizing}} gastric acid in the lumen", {1: V}, B_,
    "Antiácido neutraliza", 33, "central", "AnKing de antiácido só traz efeitos adversos.", [1461624498591, 1405722949047], "Verde: segundo exemplo sem alvo.",
    extra="- A proton-pump inhibitor instead blocks new acid secretion"),
 ak("quelante-k", 1532613551528, {2: Z}, B_, "Quelantes de K na hipercalemia crônica", 34, "Azul: lâminas 34 e 65."),
 au("hipercalemia-mecanismo", "In severe <b>hyperkalemia</b>, the depolarized myocardial membrane progressively {{c1::inactivates}} voltage-gated Na⁺ channels",
    {1: R}, B_, "Hipercalemia inativa canais de Na", 34, "lateral", "AnKing tem só o ECG.", [1573310478617, 1535225879303], "Rosa: texto lateral da lâmina 34.",
    extra="- Conduction slows and malignant ventricular arrhythmias become likely<br>- Kidney failure is the most common cause"),

 # ---------- C. Interação fármaco-alvo (lâminas 35–38) ----------
 au("cadeia-efeito", "The chain of <b>drug action</b> runs from drug–target binding to a {{c1::cellular response}} and then to the <b>therapeutic effect</b>", {1: V}, C_,
    "Fármaco → alvo → resposta → efeito", 35, "central", "sem card nos acervos.", [1522203660054, 1472747773497], "Verde: lâmina 35."),
 au("forcas-ligacao", "<b>Drugs</b> bind their targets mainly through <u>reversible</u> forces such as electrostatic, van der Waals and {{c1::hydrogen}} bonds", {1: Z}, C_,
    "Forças da ligação fármaco-alvo", 36, "central", "sem card nos acervos.", [1472426609949, 1488847696894], "Azul: figura da procaína (lâmina 36); objetivo 3.",
    extra="- A covalent bond makes the interaction irreversible, as with aspirin"),
 ak("zanamivir", 1516324778471, {1: Z, 2: Z}, C_, "Zanamivir inibe neuraminidase", 36, "Azul: desenho racional (lâmina 36).", clinica_lateral=True),
 au("estereo", "<b>Enantiomers</b> have the same formula but different spatial arrangement, so a {{c1::stereoselective}} target can bind them differently",
    {1: Z}, C_, "Estereoisomeria", 37, "central", "Externos só trazem química orgânica.", [1461986072634, 1484950587301], "Azul: lâmina 37; objetivo 3.",
    extra="- One enantiomer may be active and the other inactive or toxic"),
 au("talidomida", "<b>S-thalidomide</b> is {{c1::teratogenic}}, and giving the R form is not safe because the enantiomers interconvert in vivo", {1: R}, C_,
    "Talidomida S teratogênica", 37, "lateral", "AnKing não tem estereoisomeria da talidomida.", [1467833798088, 1461986072634], "Rosa: exemplo da tabela (conflito corrigido)."),
 au("bupi-r", "Of the two <b>bupivacaine</b> enantiomers, the {{c1::R}} form carries more <b>cardiotoxicity</b>", {1: R}, C_, "Bupivacaína R cardiotóxica", 37,
    "lateral", "sem card de enantiômero.", [1484950587301, 1484950512131], "Rosa: exemplo da tabela (levobupivacaína é a forma S).",
    extra="- Ibuprofen is mainly active as the S form"),
 au("ortosterico", "The site where the <b>endogenous ligand</b> binds is the {{c1::orthosteric}} site, and other binding sites are <b>allosteric</b>", {1: V}, C_,
    "Ortostérico × alostérico", 38, "central", "AnKing não define ortostérico.", [1484768430296, 1494990914793], "Verde: lâmina 38; objetivo 8."),
 ak("bzd-sitio", 1484768430296, {1: V}, C_, "Sítio benzodiazepínico ≠ sítio do GABA", 38, "Verde: exemplo de alosterismo."),
 ak("bzd-pam", 1484768435794, {1: V}, C_, "Benzodiazepínico aumenta frequência de abertura", 38, "Verde: modulação alostérica positiva."),
 au("nam", "An <b>allosteric modulator</b> that <u>weakens</u> the response to the endogenous agonist is a {{c1::negative}} allosteric modulator", {1: Z}, C_,
    "PAM × NAM", 38, "central", "AnKing não tem NAM.", [1484768430296, 1484768435794], "Azul: figura da lâmina 38."),
 ak("cinacalcete", 1494990914793, {1: R, 2: R}, C_, "Cinacalcete ativa CaSR", 38, "Rosa: exemplo terapêutico de alostérico (objetivo 8).", clinica_lateral=True),

 # ---------- D. Afinidade, eficácia, potência e agonismo (lâminas 39–52, 64) ----------
 ak("eficacia", 1490066276769, {1: V}, D_, "Eficácia", "39; 64", "Verde: objetivo 6."),
 ak("potencia", 1490066290359, {1: V}, D_, "Potência", 39, "Verde: objetivo 6."),
 ak("ec50", 1490066293330, {1: V}, D_, "CE50", 39, "Verde: potência pela CE50."),
 ak("afinidade", 1461852748718, {1: Z}, D_, "Afinidade", "39; 64", "Azul: sensibilidade do alvo muda pelo número ou pela afinidade dos receptores; a definição verde é afinidade-eficacia."),
 au("afinidade-eficacia", "<b>Affinity</b> is the ability to bind the target, whereas {{c1::intrinsic activity}} is the ability to activate it once bound",
    {1: V}, D_, "Afinidade × atividade intrínseca", "39; 64", "central", "AnKing não contrasta os dois termos.", [1461852748718, 1490066276769],
    "Verde: diagrama de Venn da lâmina 64."),
 ak("emax", 1490066280055, {1: V}, D_, "Platô = eficácia", 40, "Verde: leitura da curva (lâmina 40)."),
 au("curva-esquerda", "On a <b>log dose–response curve</b>, the drug whose curve lies further to the {{c1::left}} is the more <b>potent</b>", {1: V}, D_,
    "Ler potência na curva", 40, "central", "sem card de leitura da curva.", [1490066290359, 1490066293330], "Verde: fármacos A × B da lâmina 40.",
    extra="- Drug A and drug B reach the same maximum, so they have equal efficacy"),
 au("curva-c", "A drug whose curve is <u>shifted right</u> and has a <u>lower plateau</u> has lower <b>potency</b> and lower {{c1::efficacy}}", {1: Z}, D_,
    "Fármaco C da lâmina 40", 40, "central", "sem card nos acervos.", [1490066290359, 1490066280055], "Azul: fármaco C da lâmina 40."),
 au("kd-ec50", "Because of signal amplification and {{c1::spare receptors}}, <b>EC<sub>50</sub></b> need not equal the dissociation constant <b>K<sub>d</sub></b>", {1: Z}, D_,
    "CE50 ≠ Kd; receptores de reserva", "39; Rang cap. 2", "central", "sem card de receptor de reserva.", [1490066293330, 1461852748718],
    "Azul: Rang cap. 2 (conflito: potência ≠ afinidade)."),
 au("agonista-def", "An <b>agonist</b> binds a receptor and {{c1::activates}} it, triggering a cellular response", {1: V}, D_, "Agonista", 41,
    "central", "AnKing não define agonista isolado.", [1477011581106, 1490066286562], "Verde: lâmina 41."),
 au("antagonista-def", "An <b>antagonist</b> binds the receptor without activating it, because it has no {{c1::intrinsic activity}}", {1: V}, D_,
    "Antagonista sem atividade intrínseca", 41, "central", "sem card nos acervos.", [1490066300391, 1485382377464], "Verde: lâmina 41."),
 ak("fenilefrina", 1477011581106, {1: Z}, D_, "Fenilefrina: agonista α1", 41, "Azul: exemplo de agonista.", clinica_lateral=True),
 au("agonismo-tipos", "<b>Pharmacological agonism</b> includes full, partial, {{c1::inverse}} and biased agonists", {1: Z}, D_, "Tipos de agonismo", 43,
    "central", "sem card de lista.", [1490066286562, 1484950383414], "Azul: lâmina 43; objetivo 5."),
 au("dois-estados", "In the <b>two-state model</b>, agonists stabilize the receptor in its {{c1::active}} (R*) state", {1: V}, D_,
    "Modelo dos dois estados: agonista → R*", 44, "central", "AnKing não tem o modelo.", [1490066276769, 1490066286562], "Verde: lâmina 44."),
 au("inverso", "An <b>inverse agonist</b> stabilizes the inactive state (R) and lowers {{c1::constitutive}} receptor activity below baseline", {1: V}, D_,
    "Agonista inverso", "42; 45", "central", "AnKing não tem agonismo inverso.", [1490066276769, 1490066286562], "Verde: lâminas 42 e 45.",
    extra="- It shows negative intrinsic activity"),
 au("neutro", "A <b>neutral antagonist</b> blocks agonist binding without changing the receptor's {{c1::basal}} activity", {1: V}, D_,
    "Antagonista neutro × inverso", 42, "central", "sem card nos acervos.", [1490066300391, 1484768629105], "Verde: gráfico da lâmina 42.",
    extra="- An inverse agonist instead lowers the basal activity"),
 ak("loratadina", 1474571788333, {1: Z}, D_, "Loratadina: anti-H1 de 2ª geração", 46, "Azul: exemplo da lâmina 46.", clinica_lateral=True),
 au("h1-inverso", "Many <b>H1 antihistamines</b> such as loratadine act as inverse agonists because the H1 receptor has {{c1::constitutive}} activity",
    {1: Z}, D_, "Anti-H1 como agonista inverso", 46, "central", "sem card nos acervos.", [1474571788333, 1490066276769], "Azul: lâmina 46."),
 ak("pleno", 1490066286562, {1: V}, D_, "Agonista pleno × parcial", 47, "Verde: agonista pleno produz efeito máximo (lâmina 47)."),
 au("pleno-endogeno", "A <b>full agonist</b> mimics the regulatory effect of the endogenous {{c1::signaling}} compound and produces the maximal response",
    {1: Z}, D_, "Agonista pleno simula o endógeno", "47; 48", "central", "sem card nos acervos.", [1490066286562, 1477011581106], "Azul: lâminas 47–48.",
    extra="- Examples of endogenous signals are acetylcholine, dopamine, norepinephrine, serotonin, glutamate, GABA and endorphins"),
 ak("parcial-emax", 1490066314616, {1: V}, D_, "Parcial não atinge o máximo", 49, "Verde: efeito máximo parcial independente da concentração."),
 ak("vareniclina", 1475115425348, {1: Z, 2: Z, 3: Z}, D_, "Vareniclina: agonista parcial nicotínico", "49; 55", "Azul: exemplo de agonista parcial.", clinica_lateral=True),
 ak("bupre", 1484950383414, {1: V}, D_, "Buprenorfina: agonista parcial μ", 50, "Verde: exemplo da lâmina 50."),
 ak("bupre-abstinencia", 1484950415236, {1: V, 2: V}, D_, "Buprenorfina precipita abstinência", 50, "Verde: parcial antagoniza o pleno."),
 au("parcial-antagoniza", "In the presence of a full agonist, a high-affinity <b>partial agonist</b> can {{c1::reduce}} the total receptor response",
    {1: V}, D_, "Parcial como antagonista", 50, "central", "AnKing só tem o exemplo da buprenorfina.", [1484950383414, 1484950415236],
    "Verde: pergunta-chave do curso (leitura-fontes, item 5).", extra="- It displaces the full agonist but signals less",
    duplicacao_ok="ganho: princípio geral, além do exemplo da buprenorfina"),
 au("bupre-seguranca", "<b>Buprenorphine</b> causes less {{c1::respiratory depression}} in overdose than morphine because of its ceiling effect", {1: Z}, D_,
    "Buprenorfina mais segura", 50, "central", "AnKing de buprenorfina não traz o teto.", [1484950383414, 1484950415236], "Azul: lâmina 50."),
 au("tendencioso", "A <b>biased agonist</b> preferentially activates one signaling pathway, such as G protein over {{c1::β-arrestin}}, through the same receptor",
    {1: Z}, D_, "Agonista tendencioso", "51; 52", "central", "busca 'beta-arrestina' e 'oliceridina' sem resultado.", [1522203660054, 1484768590208],
    "Azul: lâminas 51–52; objetivo 5.", extra="- β-arrestin also drives receptor desensitization and internalization"),
 au("oliceridina", "<b>Oliceridine</b> is a G protein–biased μ-opioid agonist proposed to widen the opioid therapeutic {{c1::window}}", {1: R}, D_,
    "Oliceridina", 52, "lateral", "sem card nos acervos.", [1484950383414, 1522203660054], "Rosa: exemplo da lâmina 52.",
    extra="- Respiratory depression and constipation still occur; bias does not remove these risks"),

 # ---------- E. Antagonismo (lâminas 53–59) ----------
 au("antagonista-bloqueia", "<b>Antagonist</b> drugs block or reduce the action of an {{c1::agonist}}", {1: Z}, E_, "Antagonistas bloqueiam agonistas", 53,
    "central", "sem card nos acervos.", [1490066300391, 1485382377464], "Azul: lâmina 53.", duplicacao_ok="ganho: definição de antagonismo por efeito, além da atividade intrínseca"),
 au("irreversivel", "<b>Irreversible</b> inhibitors such as aspirin, omeprazole and MAO inhibitors bind through {{c1::covalent}} bonds", {1: V}, E_,
    "Antagonismo/inibição irreversível", 54, "central", "AnKing tem casos isolados.", [1488847688890, 1485048808436], "Verde: lâmina 54; objetivo 7.",
    extra="- Their effect ends only when new target protein is made<br>- Aspirin, omeprazole and MAO inhibitors act on enzymes, not receptors"),
 ak("imao-irrev", 1485048808436, {1: Z}, E_, "IMAO irreversível", 54, "Azul: exemplo da lâmina 54.", clinica_lateral=True),
 au("reversivel", "<b>Reversible</b> antagonists such as antihistamines and atropine bind through {{c1::non-covalent}} interactions", {1: V}, E_,
    "Antagonismo reversível", 54, "central", "sem card nos acervos.", [1485382222368, 1474571788333], "Verde: lâmina 54; objetivo 7."),
 ak("atropina", 1485382222368, {1: Z, 2: Z}, E_, "Atropina: antagonista competitivo muscarínico", 54, "Azul: exemplo da lâmina 54.", clinica_lateral=True),
 ak("comp-direita", 1490066300391, {1: V}, E_, "Competitivo desloca a curva para a direita", 54, "Verde: curva do antagonista competitivo."),
 ak("comp-emax", 1490066305390, {1: V}, E_, "Competitivo preserva Emax", 54, "Verde: superável com mais agonista."),
 ak("naocomp-emax", 1490066311609, {1: V}, E_, "Não competitivo reduz Emax", 54, "Verde: curva do não competitivo."),
 au("comp-afinidade", "<b>Competitive antagonists</b> reduce the agonist's apparent {{c1::affinity}}, whereas <b>noncompetitive antagonists</b> reduce its efficacy", {1: V}, E_,
    "Competitivo × não competitivo pela definição", 54, "central", "AnKing cobra só as curvas.", [1490066300391, 1490066311609], "Verde: texto da lâmina 54.",
    extra="- Noncompetitive and irreversible are not synonyms"),
 ak("flumazenil", 1484768629105, {1: Z, 2: Z}, E_, "Flumazenil compete no sítio BZD", 54, "Azul: antagonista competitivo.", clinica_lateral=True),
 ak("nmj-competitivo", 1485382377464, {1: V, 2: V}, E_, "Bloqueadores não despolarizantes competem com ACh", 55, "Verde: exemplo da lâmina 55."),
 ak("tubocurarina", 1485382373819, {1: Z}, E_, "Tubocurarina não despolarizante", 55, "Azul: miorrelaxante destacado na lâmina 55."),
 au("bungarotoxina", "<b>α-Bungarotoxin</b> blocks the muscle nicotinic receptor almost {{c1::irreversibly}}, unlike tubocurarine", {1: R}, E_,
    "α-bungarotoxina", 55, "lateral", "busca sem resultado.", [1485382377464, 1485382373819], "Rosa: tabela da lâmina 55 (conflito corrigido)."),
 au("propranolol", "<b>Propranolol</b> competitively blocks β receptors and prevents the effects of {{c1::catecholamines}}", {1: Z}, E_,
    "β-bloqueador competitivo", 56, "central", "AnKing de propranolol só traz usos clínicos.", [1477011505650, 1475704406483], "Azul: lâmina 56."),
 ak("beta1-coracao", 1477011505650, {1: Z, 2: Z}, E_, "β1 no coração", 56, "Azul: débito cardíaco (lâmina 56).", clinica_lateral=True),
 ak("beta1-renina", 1475704406483, {1: Z}, E_, "β-bloqueio reduz renina", 56, "Azul: secreção de renina (lâmina 56).", clinica_lateral=True),
 au("quimico", "In <b>chemical antagonism</b>, a drug {{c1::binds and neutralizes}} another substance directly, without acting on its receptor", {1: V}, E_,
    "Antagonismo químico", 57, "central", "busca sem resultado.", [1503672347649, 1490137896605], "Verde: lâmina 57; objetivo 7.",
    extra="- Examples are the chelator dimercaprol and infliximab binding TNF-α"),
 ak("dimercaprol", 1490137896605, {1: Z}, E_, "Dimercaprol quelante", 57, "Azul: exemplo de antagonismo químico.", clinica_lateral=True),
 ak("infliximab", 1489968442057, {1: Z}, E_, "Infliximabe contra TNF-α", 57, "Azul: exemplo de antagonismo químico.", clinica_lateral=True),
 au("farmacocinetico", "In <b>pharmacokinetic antagonism</b>, one drug lowers the {{c1::concentration}} of another at its site of action", {1: V}, E_,
    "Antagonismo farmacocinético", 58, "central", "busca sem resultado.", [1503259126424, 1565120487647], "Verde: lâmina 58; objetivo 7.",
    extra="- It can act through absorption, metabolism or excretion"),
 ak("cyp-inducao", 1503259126424, {1: Z}, E_, "Indução de CYP reduz outro fármaco", 59, "Azul: varfarina + fenobarbital (lâmina 59).", clinica_lateral=True),
 au("varfarina-fenobarbital", "<b>Phenobarbital</b> induces CYP enzymes and so {{c1::reduces}} the anticoagulant effect of warfarin", {1: Z}, E_,
    "Varfarina × fenobarbital", 59, "prova", "AnKing não tem a dupla.", [1503259126424, 1490066326802], "Azul: exemplo da lâmina 59; questão da rifampicina.",
    extra="- Phenytoin and carbamazepine are also potent inducers"),
 ak("lidocaina-epi", 1535326196678, {1: Z}, E_, "Vasoconstritor prolonga anestésico local", 59, "Azul: antagonismo farmacocinético desejado."),
 au("fisiologico", "In <b>physiological antagonism</b>, two drugs act on different receptors and produce {{c1::opposite}} effects", {1: V}, E_,
    "Antagonismo fisiológico", "57; objetivo 7; questão", "prova", "busca sem resultado.", [1490066300391, 1462128028823], "Verde: objetivo 7 e questão de prova.",
    extra="- Insulin and glucagon have opposite effects on blood glucose"),
 au("funcional", "<b>Epinephrine</b> reverses histamine bronchoconstriction through a different receptor on the same smooth muscle, an example of {{c1::functional}} antagonism",
    {1: Z}, E_, "Antagonismo funcional", "57; objetivo 7", "prova", "busca 'functional antagonism' e 'physiologic antagonism' sem card do conceito.",
    [1490066300391, 1462128028823], "Azul: objetivo 7 lista o antagonismo funcional ao lado do fisiológico.",
    extra="- Both agonists act on the same tissue and their effects cancel out", duplicacao_ok="resposta própria (funcional); o fisiológico cobra 'opposite'"),

 # ---------- F. Janela e índice terapêutico (lâmina 60) ----------
 ak("it", 1490066320396, {1: V}, F_, "IT = TD50/ED50", 60, "Verde: índice terapêutico (objetivo 4)."),
 ak("it-direcao", 1490066323578, {1: V}, F_, "IT alto = mais seguro", 60, "Verde: leitura do IT."),
 au("it-letal", "In animal studies, the <b>therapeutic index</b> is calculated as the {{c1::LD50}} divided by the ED50", {1: Z}, F_, "IT com LD50", 60,
    "central", "o Lightyea traz a fórmula errada (subtração).", [1490066320396, 1490066323578], "Azul: fórmula da lâmina 60.",
    extra="- In humans TD50 replaces LD50"),
 au("janela", "The <b>therapeutic window</b> is the dose range that balances {{c1::efficacy}} and toxicity", {1: V}, F_, "Janela terapêutica", 60,
    "central", "AnKing só tem janela da levodopa.", [1490066320396, 1490066323578], "Verde: lâmina 60; objetivo 4."),
 au("it-baixo", "<b>Digoxin</b>, warfarin and {{c1::lithium}} have a low therapeutic index", {1: Z}, F_, "IT baixo: digoxina, varfarina, lítio", 60,
    "central", "o mnemônico AnKing é lista longa.", [1490066320396, 1485126747494], "Azul: exemplos da lâmina 60.",
    extra="- Paracetamol and aspirin have a high index, though overdose is still toxic"),
 ak("litio-it", 1485126747494, {1: Z}, F_, "Lítio IT estreito", 60, "Azul: exemplo."),
 au("curvas-quantais", "<b>Quantal dose–response curves</b> plot the percentage of <u>individuals</u> showing the therapeutic, toxic and {{c1::lethal}} effect at each dose",
    {1: Z}, F_, "Curvas quantais: ED50, TD50, LD50", 60, "central", "sem card nos acervos.", [1490066320396, 1490066323578], "Azul: gráfico da lâmina 60; objetivo 4."),

 # ---------- G. Perda de resposta (objetivo 9; lâminas 29 e 51) ----------
 ak("tolerancia", 1560780655468, {1: V}, G_, "Tolerância", "29; objetivo 9", "Verde: objetivo 9 (só o c1: o c2 é uma frase longa).", origin="Referências Externas"),
 ak("dessensibilizacao", 1610988344275, {1: V}, G_, "Dessensibilização", "51; objetivo 9", "Verde: objetivo 9 (β-arrestina, lâmina 51).", origin="Referências Externas"),
 ak("taquifilaxia", 1695594779845, {1: Z}, G_, "Taquifilaxia", "51; objetivo 9", "Azul: objetivo 9; retirada a captura de texto que trata tolerância e taquifilaxia como sinônimos.", origin="Referências Externas", extra='<img src="paste-6da0d1a439a4473a285011671e84e9157857b3d2.jpg"><br>- Develops within minutes of repeated doses'),
 ak("downreg", 1484768590208, {1: V}, G_, "Downregulation", "51; objetivo 9", "Verde: downregulation como mecanismo de tolerância (lâmina 51; objetivo 9), HY 2."),
 au("refratariedade", "Gradual loss of a drug's <b>therapeutic efficacy</b> during continued treatment of a patient is called {{c1::refractoriness}}", {1: Z}, G_,
    "Refratariedade", "51; objetivo 9", "prova", "busca 'refractor' só traz período refratário cardíaco/neural.", [1484768590208, 1472747925827],
    "Azul: objetivo 9 lista refratariedade com tolerância e resistência (Rang cap. 2).",
    extra="- Tachyphylaxis develops in minutes, tolerance in days to weeks"),
 au("resistencia", "Loss of drug effect because the <b>microorganism</b> or tumor itself changes, rather than the patient's receptors, is drug {{c1::resistance}}", {1: Z}, G_,
    "Resistência", "19; objetivo 9", "central", "sem card geral.", [1503672347649, 1610988344275], "Azul: objetivo 9; β-lactamase (lâmina 19).",
    extra="- β-lactamase-producing bacteria are an example"),

 # ---------- H. Extras (lâminas 65–69) ----------
 au("sps", "<b>Sodium polystyrene sulfonate</b> exchanges Na⁺ for K⁺ in the colon and acts {{c1::slowly}}", {1: R}, H_, "Poliestirenossulfonato", 65,
    "lateral", "AnKing só tem a classe.", [1532613551528, 1535225879303], "Rosa: tabela da lâmina 65.", extra="- K⁺ bound to the resin leaves in the feces"),
 au("patiromer", "<b>Patiromer</b> exchanges Ca²⁺ for K⁺ in the gut and can cause {{c1::hypomagnesemia}}", {1: R}, H_, "Patirômer", 65,
    "lateral", "AnKing só tem a classe.", [1532613551528, 1496611078059], "Rosa: tabela da lâmina 65.", extra="- It is used for chronic control in patients on RAAS inhibitors"),
 au("szc", "<b>Sodium zirconium cyclosilicate</b> traps K⁺ selectively and has the {{c1::fastest}} onset of the oral K⁺ binders", {1: R}, H_, "Ciclossilicato de zircônio", 65,
    "lateral", "AnKing só tem a classe.", [1532613551528, 1535225879303], "Rosa: tabela da lâmina 65.",
    extra="- Oral binders do not replace emergency measures in life-threatening hyperkalemia"),
 au("transportador-modos", "Drugs act on <b>transporters</b> either as inhibitors or as false {{c1::substrates}} that accumulate an abnormal compound", {1: Z}, H_,
    "Inibidor × falso substrato", 66, "central", "sem card nos acervos.", [1485042559919, 1504365294081], "Azul: figura da lâmina 66."),
 ak("tca-net", 1485042559919, {1: Z}, H_, "Tricíclicos inibem recaptação de NE", 66, "Azul: tabela de transportadores.", clinica_lateral=True),
 au("anfetamina", "<b>Amphetamine</b> and methyldopa act on the norepinephrine transporter as false {{c1::substrates}}", {1: R}, H_,
    "Falsos substratos do NET", 66, "lateral", "AnKing de anfetamina não traz falso substrato.", [1485042559919, 1504365294081], "Rosa: tabela da lâmina 66.",
    extra="- Tricyclic antidepressants and cocaine instead inhibit the transporter"),
 ak("probenecida", 1504365294081, {1: Z}, H_, "Probenecida bloqueia transporte de ácidos fracos", 66, "Azul: tabela de transportadores.", clinica_lateral=True),
 ak("nkcc2", 1475023258287, {1: Z, 2: Z}, H_, "Diuréticos de alça inibem NKCC2", 66, "Azul: tabela (corrige 'Na2+')."),
 au("canal-modos", "Drugs act on <b>ion channels</b> either as blockers of permeation or as {{c1::modulators}} of opening probability", {1: Z}, H_,
    "Bloqueador × modulador de canal", 67, "central", "sem card nos acervos.", [1484950518844, 1484768435794], "Azul: figura da lâmina 67."),
 ak("tetrodotoxina", 1490137861396, {1: R}, H_, "Tetrodotoxina bloqueia canal de Na", 67, "Rosa: tabela de canais.", clinica_lateral=True),
 ak("enac", 1475803118764, {1: Z, 2: Z, 3: Z}, H_, "Amilorida bloqueia ENaC", 67, "Azul: tabela de canais.", clinica_lateral=True),
 ak("aldosterona", 1475803101293, {1: R}, H_, "Aldosterona e ENaC", 67, "Rosa: modulador da tabela (via receptor nuclear).", clinica_lateral=True),
 ak("ca-l", 1472500374903, {1: Z}, H_, "Bloqueadores de canal de Ca tipo L", 67, "Azul: di-hidropiridinas da tabela.", clinica_lateral=True),
 ak("gabapentina", 1502344277221, {1: R, 2: R}, H_, "Gabapentinoides ligam α2δ", 67, "Rosa: tabela de canais."),
 ak("katp", 1462127903018, {1: Z}, H_, "Sulfonilureias fecham KATP", 67, "Azul: tabela de canais.", clinica_lateral=True),
 ak("anestesico-na", 1484950518844, {1: V}, H_, "Anestésico local bloqueia canal de Na", "67; 68", "Verde: mecanismo da lâmina 68."),
 ak("anestesico-uso", 1484950522069, {1: R}, H_, "Bloqueio preferencial de fibras ativas", 68, "Rosa: detalhe do mecanismo.", clinica_lateral=True),
 ak("amidas", 1484950512131, {1: R}, H_, "Anestésicos amida", 69, "Rosa: tabela da lâmina 69."),
 ak("bupi-cardio", 1484950587301, {1: Z, 2: Z}, H_, "Bupivacaína cardiotóxica", 69, "Azul: toxicidade da lâmina 69.", clinica_lateral=True),
 au("anestesico-toxico", "Systemic overdose of a <b>local anesthetic</b> causes CNS toxicity such as tremor and {{c1::seizures}}", {1: Z}, H_,
    "Toxicidade sistêmica de anestésico local", "68; 69", "central", "AnKing tem só a bupivacaína.", [1484950587301, 1484950518844], "Azul: lâminas 68–69."),
]

VERSO = {
 'toxicologia': '- Toxic effects follow the same dose–response logic as therapeutic ones',
 'pd-def': '- In short, what the <b>drug does to the body</b>',
 'gs': '- Gs activates adenylyl cyclase → ↑ cAMP → PKA',
 'gi': '- Gi inhibits adenylyl cyclase → ↓ cAMP',
 'rtk': '- Ligand binding → dimerization and autophosphorylation (e.g., insulin receptor)',
 'gaba-canal': '- Cl⁻ influx hyperpolarizes the neuron (inhibition)',
 'cisplatina': '- Platinum forms <b>DNA cross-links</b>, blocking replication',
 'doxo-cardio': '- Free radicals damage cardiomyocytes; risk rises with cumulative dose',
 'doxo-alopecia': '- Hair follicles are rapidly dividing cells',
 'nitrato-no': '- NO activates guanylyl cyclase → ↑ cGMP → smooth muscle relaxation',
 'nitrato-angina': '- Venodilation ↓ preload and myocardial O₂ demand',
 'nos-isoformas': '- iNOS is expressed by macrophages during inflammation',
 'gmpc-pkg': '- PKG lowers intracellular Ca²⁺ → <b>vasodilation</b>',
 'carbidopa': '- Blocks peripheral conversion, so more levodopa reaches the brain',
 'mtx-dhfr': '- Less tetrahydrofolate → less thymidine and purine synthesis',
 'citarabina': '- Pyrimidine analog acting in S phase',
 'estatina': '- HMG-CoA reductase is the rate-limiting step of cholesterol synthesis',
 'nrti': '- Reverse transcriptase copies viral RNA into DNA',
 'digoxina': '- ↑ intracellular Na⁺ → less Ca²⁺ extrusion by NCX → ↑ contractility',
 'cadeia-efeito': '- Binding alone is not the effect: signaling and tissue response come in between',
 'talidomida': '- Stereoisomers share the formula but differ in spatial arrangement',
 'ortosterico': '- Allosteric ligands change how the orthosteric ligand binds or acts',
 'bzd-sitio': '- BZDs need GABA present; they do not open the channel alone',
 'nam': '- Positive modulators (PAMs) enhance the response instead',
 'eficacia': '- Read as the height of the <b>plateau (Emax)</b>',
 'potencia': '- Read as the position of the curve on the x-axis (EC50)',
 'afinidade': '- Fewer receptors (downregulation) also lowers responsiveness',
 'afinidade-eficacia': '- Antagonists have affinity but zero intrinsic activity',
 'kd-ec50': '- With spare receptors, a maximal response needs only part of the receptors occupied',
 'curva-c': '- Potency = position on the x-axis; efficacy = height of the plateau',
 'agonista-def': '- Activating the receptor may increase or decrease cell function',
 'antagonista-def': '- It blocks the agonist by occupying the receptor',
 'agonismo-tipos': '- They differ in the maximal response and in the pathway they favor',
 'dois-estados': '- Inverse agonists favor R; neutral antagonists favor neither',
 'loratadina': '- Second generation crosses the blood–brain barrier less → less sedation',
 'h1-inverso': '- Constitutive activity = signaling without ligand',
 'pleno': '- Even at full occupancy, a partial agonist gives a submaximal response',
 'bupre-seguranca': '- Partial μ agonist: the effect plateaus as the dose rises',
 'antagonista-bloqueia': '- Antagonists have affinity without efficacy',
 'imao-irrev': '- Recovery requires synthesis of new enzyme',
 'reversivel': '- More agonist can displace them',
 'comp-direita': '- Higher agonist concentrations overcome the block',
 'comp-emax': '- Emax is reached with enough agonist',
 'naocomp-emax': '- Adding agonist cannot restore the maximal response',
 'tubocurarina': '- Competes with ACh at the nicotinic receptor → flaccid paralysis',
 'bungarotoxina': '- Snake toxin used to label nicotinic receptors',
 'propranolol': '- Nonselective β1/β2 blocker',
 'beta1-coracao': '- β1 also ↑ contractility (cardiac output)',
 'beta1-renina': '- Less renin → less angiotensin II and aldosterone',
 'dimercaprol': '- Chelators bind the metal directly (chemical antagonism)',
 'infliximab': '- Neutralizes the mediator instead of blocking its receptor',
 'lidocaina-epi': '- Prolongs the local block and lowers systemic toxicity',
 'it-direcao': '- TI = TD50/ED50; wider gap between toxic and effective doses',
 'janela': '- Narrow window drugs need monitoring of levels (digoxin, lithium)',
 'curvas-quantais': '- They describe a population, not the intensity in one person',
 'transportador-modos': '- Amphetamine is a false substrate of NET',
 'tca-net': '- Blocking reuptake leaves more transmitter in the synapse',
 'canal-modos': '- Local anesthetics block; benzodiazepines modulate',
 'tetrodotoxina': '- Puffer fish toxin; blocks the channel from outside',
 'enac': '- Less Na⁺ entry → less K⁺ secretion (K⁺-sparing)',
 'aldosterona': '- Acts by gene regulation via a nuclear receptor, not by opening the channel directly',
 'katp': '- Closed K<sub>ATP</sub> → depolarization → Ca²⁺ entry → insulin release',
 'anestesico-na': '- No action potential propagates → no pain signal',
 'anestesico-toxico': '- High levels also cause arrhythmias',
 'bupi-cardio': '- The R enantiomer is more cardiotoxic',
}
DUPLICACAO = {
 "curva-c": "leitura gráfica da lâmina 40 (curva à direita e platô baixo): aplica a eficácia a uma curva, não a define",
 "comp-afinidade": "contraste competitivo × não competitivo pelo parâmetro alterado; o card afinidade cobra a sensibilidade do alvo",
 "bungarotoxina": "irreversibilidade no receptor nicotínico (lâmina 55), distinta do IMAO (enzima)",
 "janela": "janela terapêutica (lâmina 60) equilibra eficácia e toxicidade; o card eficacia define o Emax",
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


# ---- escopo da aula (F-20261012-CLAUDE-01): a introdução cobre o núcleo de farmacodinâmica (alvos, interação, curvas, agonismo,
# antagonismo, perda de resposta, índice terapêutico); exemplos de fármacos das tabelas (enzimas, canais, transportadores, toxicidades)
# são ilustração e saem (nebli.retira, lista em retirar-escopo.txt). Gráficos das lâminas 40, 42, 54 e 60 viram cards de leitura. ----
_RETIRAR = set(open(__import__("pathlib").Path(__file__).with_name("retirar-escopo.txt")).read().split())
_SH_FORA = {1791625430456, 1791147106101, 1791743346085, 1791668521339}  # NOS, NO antiagregante, aspirina, clavulanato: exemplos
CARDS[:] = [c for c in CARDS if c["key"] not in _RETIRAR and not (c["kind"] == "compartilhado" and c["nid"] in _SH_FORA)]
MEDIA.update({f"fa01-g-{n}.png": f"img/fa01-g-{n}.png" for n in ("potencia", "agonismo", "antagonismo", "quantal")})
_G = [1490066276769, 1490066290359]
_im = lambda n: f'<img src="fa01-g-{n}.png"><br>'
_ESC = "gráfico da lâmina sem card nos acervos (F-20261012-CLAUDE-01: núcleo da aula)."
CARDS += [
 au("acidos-nucleicos", "Besides proteins, {{c1::nucleic acids}} are <b>drug targets</b>, as for anticancer drugs that bind DNA", {1: Z}, B_,
    "Ácidos nucleicos como alvo", 27, "central", "sem card do conceito.", [1490066276769, 1489968442057], "Azul: lâmina 27 (alvo não proteico).",
    extra="- Cisplatin cross-links DNA and doxorubicin intercalates"),
 au("g-potencia", _im("potencia") + "On these <b>dose–response curves</b>, drug {{c1::A}} is the most potent, reaching 50% of its effect at the lowest concentration",
    {1: V}, D_, "Ler potência no gráfico", 40, "central", _ESC, _G, "Verde: leitura de curva (lâmina 40), núcleo da aula.",
    extra="- Potency is read on the x-axis (EC<sub>50</sub>)"),
 au("g-eficacia", _im("potencia") + "<b>Drugs A and B</b> reach the same plateau, so they share the same {{c1::efficacy}} despite different potencies",
    {1: V}, D_, "Ler eficácia no gráfico", 40, "central", _ESC, _G, "Verde: leitura de curva (lâmina 40).",
    extra="- Efficacy is read on the y-axis (E<sub>max</sub>)<br>- Drug C has lower potency and lower efficacy", duplicacao_ok="leitura gráfica; o card eficacia define o termo"),
 au("g-inverso", _im("agonismo") + "The curves that fall <b>below the baseline</b> response belong to {{c1::inverse}} agonists",
    {1: V}, D_, "Agonista inverso no gráfico", 42, "central", _ESC, _G, "Verde: gráfico da lâmina 42.",
    extra="- They need a receptor with constitutive activity", duplicacao_ok="leitura gráfica do agonismo inverso"),
 au("g-neutro", _im("agonismo") + "The <b>flat curve</b> at zero response belongs to a {{c1::neutral antagonist}}",
    {1: Z}, D_, "Antagonista neutro no gráfico", 42, "central", _ESC, _G, "Azul: gráfico da lâmina 42.",
    extra="- It binds without changing basal activity"),
 au("g-parcial", _im("agonismo") + "The curve that rises but levels off near <b>50%</b> belongs to a {{c1::partial}} agonist",
    {1: Z}, D_, "Agonista parcial no gráfico", 42, "central", _ESC, _G, "Azul: gráfico da lâmina 42.",
    extra="- Full agonists reach 100%", duplicacao_ok="leitura gráfica do agonismo parcial"),
 au("g-competitivo", _im("antagonismo") + "In the <b>upper graph</b>, the antagonist shifts the agonist curve to the right but the maximum is still reached, typical of {{c1::competitive}} antagonism",
    {1: V}, E_, "Competitivo no gráfico", 54, "central", _ESC, _G, "Verde: gráfico da lâmina 54.",
    extra="- More agonist overcomes the block", duplicacao_ok="leitura gráfica"),
 au("g-naocompetitivo", _im("antagonismo") + "In the <b>lower graph</b>, the antagonist lowers the maximal response, typical of {{c1::noncompetitive}} antagonism",
    {1: V}, E_, "Não competitivo no gráfico", 54, "central", _ESC, _G, "Verde: gráfico da lâmina 54.",
    extra="- Adding agonist cannot restore the maximum", duplicacao_ok="leitura gráfica"),
 au("g-quantal", _im("quantal") + "The farther apart the <b>ED<sub>50</sub></b> and <b>TD<sub>50</sub></b> curves, the {{c1::wider}} the margin of safety",
    {1: Z}, F_, "Margem de segurança no gráfico", 60, "central", _ESC, _G, "Azul: curvas quantais da lâmina 60.",
    extra="- TI = TD<sub>50</sub>/ED<sub>50</sub>"),
]

# ---- cores recalibradas (12/10): verde só o núcleo duradouro; exemplo ou repetição de um verde vira azul ----
def _cc(key):
    return next(c for c in CARDS if c["key"] == key)
for _k in ("fase1", "fase2", "fase3", "fase4", "gaba-canal", "nitrato-tolerancia", "gc", "manitol", "bzd-sitio", "bzd-pam", "bupre",
           "bupre-abstinencia", "anestesico-na"):
    _cc(_k)["flags"] = {n: Z for n in _cc(_k)["flags"]}; _cc(_k)["clinica_lateral"] = True  # exemplo de fármaco/clínica na introdução
for _k in ("gq", "gs", "gi", "rtk", "emax", "comp-direita", "comp-emax", "naocomp-emax", "it-direcao"):
    _cc(_k)["flags"] = {n: Z for n in _cc(_k)["flags"]}; _cc(_k)["hy_repete"] = True  # o representante verde é outro card
for _k in ("medicamento", "adme", "pd-def", "nitro-prodroga", "pde5", "curva-esquerda", "g-eficacia", "g-inverso"):
    _cc(_k)["flags"] = {n: Z for n in _cc(_k)["flags"]}

# Revisão pontual Codex 12/10/2026 — evidência em revisao-pontual-claude-2026-10-12
_AJUSTES_CODEX_1210 = {'g-potencia': {'fields_override': {'Text': '<img src="fa01-g-potencia.png"><br>Which drug is <b>most potent</b>? '
                                            '{{c1::A}}',
                                    'Extra': '- A has the lowest EC<sub>50</sub>, read at half of its own maximal '
                                             'response.<br>- A and B reach the same plateau despite different '
                                             'potencies.'},
                'motivo': 'Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no '
                          'Extra. Mesmos IDs/clozes.'},
 'g-eficacia': {'fields_override': {'Text': '<img src="fa01-g-potencia.png"><br>Which drugs have the <b>same '
                                            'maximal efficacy</b>? {{c1::A and B}}',
                                    'Extra': '- A and B reach the same plateau. C reaches a lower maximum.<br>- '
                                             'Compare plateau height for efficacy and EC<sub>50</sub> for '
                                             'potency.'},
                'motivo': 'Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no '
                          'Extra. Mesmos IDs/clozes.'},
 'g-inverso': {'fields_override': {'Text': '<img src="fa01-g-agonismo.png"><br>The <b>red diamonds and purple '
                                           'triangles</b> represent {{c1::inverse agonists}}',
                                   'Extra': '- Both curves fall below the basal response, indicating suppression '
                                            'of constitutive activity.<br>- The flat blue curve represents a '
                                            'neutral antagonist.'},
               'motivo': 'Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no '
                         'Extra. Mesmos IDs/clozes.'},
 'g-neutro': {'fields_override': {'Text': '<img src="fa01-g-agonismo.png"><br>The <b>blue triangles</b> represent '
                                          'a {{c1::neutral antagonist}}',
                                  'Extra': '- Basal activity remains unchanged as concentration increases.<br>- '
                                           'An inverse agonist would lower activity below baseline.'},
              'motivo': 'Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no '
                        'Extra. Mesmos IDs/clozes.'},
 'g-parcial': {'fields_override': {'Text': '<img src="fa01-g-agonismo.png"><br>The <b>green squares</b> represent '
                                           'a {{c1::partial agonist}}',
                                   'Extra': '- The plateau is lower than that of the full agonist shown in '
                                            'black.<br>- The value near 50% belongs to this example; partial '
                                            'agonists do not all have a 50% maximum.'},
               'motivo': 'Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no '
                         'Extra. Mesmos IDs/clozes.'},
 'g-competitivo': {'fields_override': {'Text': '<img src="fa01-g-antagonismo.png"><br>Which type of '
                                               '<b>antagonism</b> is shown in the upper graph? '
                                               '{{c1::Competitive}}',
                                       'Extra': '- The agonist curve shifts right, but its maximum is '
                                                'preserved.<br>- A higher agonist concentration overcomes the '
                                                'blockade.'},
                   'motivo': 'Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam '
                             'no Extra. Mesmos IDs/clozes.'},
 'g-naocompetitivo': {'fields_override': {'Text': '<img src="fa01-g-antagonismo.png"><br>Which type of '
                                                  '<b>antagonism</b> is shown in the lower graph? '
                                                  '{{c1::Noncompetitive}}',
                                          'Extra': '- The maximum falls despite increasing the agonist '
                                                   'concentration.<br>- The upper graph instead shows a '
                                                   'surmountable, competitive blockade.'},
                      'motivo': 'Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio '
                                'ficam no Extra. Mesmos IDs/clozes.'},
 'g-quantal': {'fields_override': {'Text': '<img src="fa01-g-quantal.png"><br>Which curves determine the '
                                           '<b>therapeutic index</b>? {{c1::Therapeutic and toxic}}',
                                   'Extra': '- Read ED<sub>50</sub> and TD<sub>50</sub> at 50% of individuals, '
                                            'then calculate TD<sub>50</sub>/ED<sub>50</sub>.<br>- This is a '
                                            'population response, not half of the maximal effect in one person.'},
               'motivo': 'Frente exige interpretar a figura; a descrição do sinal visual e o raciocínio ficam no '
                         'Extra. Mesmos IDs/clozes.'},
 'alvo-sem-endereco': {'fields_override': {'Text': 'A drug can cause <b>adverse effects</b> by acting on its '
                                                   'target in {{c1::other tissues}}',
                                           'Extra': '- Target distribution helps explain why the desired effect '
                                                    'may be accompanied by effects elsewhere.'},
                       'motivo': 'Troca a lacuna genérica choose por relação farmacológica recuperável; lâminas '
                                 '24/35.'},
 'gpcr': {'fields_override': {'Text': '{{c1::<b>G protein–coupled</b>}} receptors transmit extracellular '
                                      '{{c2::ligand}} binding to heterotrimeric G proteins inside the cell',
                              'Extra': '- Receptor activation couples an extracellular signal to intracellular '
                                       'enzymes or ion channels.'},
          'motivo': 'Corrige generalização bind glycoproteins na cópia NEBLI e retira patologias laterais do '
                    'Extra; IUPHAR Receptors. Original preservado.'},
 'rtk': {'fields_override': {'Extra': '- Ligand binding activates receptor kinase signaling and phosphorylation '
                                      'of intracellular proteins.'},
         'motivo': 'Retira generalização de dimerização que não descreve corretamente todos os receptores do '
                   'exemplo; mantém princípio da lâmina 25.'},
 'gc': {'fields_override': {'Extra': '- NO activates soluble guanylyl cyclase → increased cGMP → smooth-muscle '
                                     'relaxation.'},
        'motivo': 'Extra passa a explicar a cadeia da aula, sem farmacoterapia de hipertensão pulmonar.'},
 'bupre': {'fields_override': {'Extra': '- A partial agonist produces a lower maximal receptor response than a '
                                        'full agonist.<br>- Buprenorphine illustrates this property at μ-opioid '
                                        'receptors.'},
           'motivo': 'Retira conduta de início de tratamento; conserva conexão com agonismo parcial.; Exemplo '
                     'específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. Não '
                     'impõe proporção de cores.',
           'flags': {1: 5},
           'clinica_lateral': True},
 'atropina': {'fields_override': {'Extra': '- Atropine illustrates competitive antagonism at muscarinic '
                                           'receptors.<br>- The receptor subtype matters: nicotinic effects are '
                                           'not blocked by atropine.'},
              'motivo': 'Mantém exemplo cobrado em prova e mecanismo; retira sequência terapêutica lateral.'},
 'nitro-prodroga': {'fields_override': {},
                    'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem '
                              'recuperáveis. Não impõe proporção de cores.',
                    'flags': {1: 5}},
 'nitrato-tolerancia': {'fields_override': {},
                        'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais '
                                  'seguem recuperáveis. Não impõe proporção de cores.',
                        'flags': {1: 5},
                        'clinica_lateral': True},
 'pde5': {'fields_override': {},
          'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem '
                    'recuperáveis. Não impõe proporção de cores.',
          'flags': {1: 5, 2: 5, 3: 5}},
 'manitol': {'fields_override': {},
             'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem '
                       'recuperáveis. Não impõe proporção de cores.',
             'flags': {1: 5, 2: 5},
             'clinica_lateral': True},
 'h1-inverso': {'fields_override': {},
                'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem '
                          'recuperáveis. Não impõe proporção de cores.',
                'flags': {1: 5}},
 'bupre-abstinencia': {'fields_override': {},
                       'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem '
                                 'recuperáveis. Não impõe proporção de cores.',
                       'flags': {1: 5, 2: 5},
                       'clinica_lateral': True},
 'varfarina-fenobarbital': {'fields_override': {},
                            'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais '
                                      'seguem recuperáveis. Não impõe proporção de cores.',
                            'flags': {1: 5}},
 'it-baixo': {'fields_override': {},
              'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem '
                        'recuperáveis. Não impõe proporção de cores.',
              'flags': {1: 5}},
 'anestesico-na': {'fields_override': {},
                   'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem '
                             'recuperáveis. Não impõe proporção de cores.',
                   'flags': {1: 5},
                   'clinica_lateral': True},
 'gq': {'fields_override': {},
        'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. '
                  'Não impõe proporção de cores.',
        'flags': {1: 5, 2: 5},
        'clinica_lateral': True},
 'gs': {'fields_override': {},
        'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. '
                  'Não impõe proporção de cores.',
        'flags': {1: 5, 2: 5},
        'clinica_lateral': True},
 'gi': {'fields_override': {},
        'motivo': 'Exemplo específico/subtipo é apoio de menor prioridade; conceitos gerais seguem recuperáveis. '
                  'Não impõe proporção de cores.',
        'flags': {1: 5, 2: 5},
        'clinica_lateral': True}}
for _c in CARDS:
    if _c["key"] in _AJUSTES_CODEX_1210:
        _fix = _AJUSTES_CODEX_1210[_c["key"]]
        _c.setdefault("fields_override", {}).update(_fix["fields_override"])
        _c["motivo"] = _fix["motivo"]
        if "flags" in _fix: _c["flags"] = _fix["flags"]
        if _fix.get("clinica_lateral"): _c["clinica_lateral"] = True
        if _fix.get("metadata"): _c.update(_fix["metadata"])
