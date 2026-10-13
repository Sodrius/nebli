# Especificação curada — Homem, ambiente e microrganismo (UC03 P2, Microbiologia; Profa. Carla Taddei, 43 lâminas de 2026 + lâminas da Profa. Elisabete Vicente, 2025, lâminas 44–96).
# Ordem = lâminas. Itens da Vicente que repetem assunto da Taddei ficam na lâmina de 2026; epidemiologia e discussão ficam nas lâminas 44–96 (turma I p.N = lâmina 43+N).
import json, re, urllib.request
RUN_ID = "uc03-mb39-20261012a"
SHORT = "mb39"
LESSON = "2026-uc03-microbiologia-39-homem-ambiente-microrganismo"
DECK = "NEBLI::UC03::P2::Microbiologia::Homem, ambiente e microrganismo"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261011-CLAUDE-06) + plano vigente, 12/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt e anking2.txt, ~40 consultas; busca/ext.txt), cópias NEBLI vivas de Patogenicidade, "
         "Morfologia, Antibióticos, Controle microbiológico, Fisiologia e Biologia tecidual UC08 conferidas (compartilhados), 12/10: ")
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
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor={V: "verde", Z: "azul", R: "rosa"}.get(cor, cor), bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_, G_ = ("A-conceitos", "B-pele-vias-aereas-genital-boca", "C-trato-digestivo", "D-microbiota-intestinal-origem-funcoes",
                              "E-barreira-e-metabolismo", "F-composicao-probioticos-disfuncoes", "G-epidemiologia-infeccao")
ES1 = [1500498491769, 1510011540019]
ES2 = [1520709952510, 1473995752044]
ES3 = [1516129796813, 1547916062228]
ES4 = [1592688777796, 1482959865798]
ES5 = [1502152410992, 1510103483272]
ES6 = [1506285248660, 1516067829624]
ES7 = [1403561490959, 1472072097648]
NF = "AnKing e externos não têm card sobre este alvo. "
CARDS = [
 # ---------- A. Conceitos (lâminas 4–5, 47–53) ----------
 au("microbiota-def", "<b>Microbiota</b> is the set of microorganisms that reside on the body, permanently or not, without causing {{c1::infection}} in normal conditions", V, A_, "Definição de microbiota", "4; Trabulsi cap. 12", "central", NF, ES1, "Verde: lâmina 4.",
    extra="- It lives on the skin and mucosae, which contact the external environment"),
 au("microbiota-sitios", "The human microbiota lives on the <b>skin</b> and <b>mucosae</b>, the surfaces in contact with the {{c1::external environment}}", Z, A_, "Distribuição da microbiota", "4; guia veteranos", "central", NF, ES1, "Azul: lâmina 4.",
    extra="- Each site has its own microbiota, so the distribution is not homogeneous"),
 au("transitoria", "The <b>microbiota</b> that stays only a short time on the body without colonizing it is called {{c1::transient}}", V, A_, "Microbiota transitória", "4; Trabulsi cap. 12", "central", NF, ES1, "Verde: lâmina 4, residente × transitória.",
    extra="- It is also called allochthonous"),
 au("residente", "The <b>resident</b> (indigenous) microbiota colonizes a site for an indefinite time in {{c1::symbiosis}} with the host", Z, A_, "Microbiota residente", "4; Trabulsi cap. 12", "central", NF, ES1, "Azul: lâmina 4.",
    extra="- It is also called autochthonous"),
 au("antagonismo", "The main benefit of the resident microbiota is {{c1::bacterial antagonism}}, which blocks colonization by potential pathogens", V, A_, "Antagonismo bacteriano", "4; Trabulsi cap. 12", "central", NF, ES1, "Verde: benefício principal da lâmina 4.",
    extra="- Mechanisms are competition for nutrients and adhesion sites, antimicrobial substances and pH changes"),
 sh(1791576665465, Z, A_, "Maioria comensal ou mutualista", 4, "Azul: a microbiota é em geral comensal (lâmina 4)."),
 sh(1791746115903, V, A_, "Infecção endógena", 5, "Verde: lâmina 5, infecções pela própria microbiota; criado na Patogenicidade."),
 au("ambiente-solo", "<b>Soil</b> holds about {{c1::10<sup>7</sup>}} bacteria and 10<sup>5</sup> fungi per gram, making it a source of exogenous infection", R, A_, "Solo como ambiente microbiano", "47; turma I p.4 e p.41", "lateral", NF, ES6, "Rosa: número da lâmina 47 e 84 (a figura da p.4 traz 10^8).",
    extra="- Water and air are other environmental sources"),
 au("tres-desfechos", "Contact between a human and a microorganism can lead to transient colonization, permanent colonization or {{c1::disease}}", Z, A_, "Desfechos do contato", "48; turma I p.5", "central", NF, ES1, "Azul: lâmina 48."),
 sh(1791746114850, Z, A_, "Colonização × infecção", 48, "Azul: colonização transitória/permanente × infecção."),
 au("mnch-raramente", "Members of the normal <b>microbiota</b> rarely cause disease, mainly in {{c1::immunosuppressed}} hosts", Z, A_, "MNCH raramente causa doença", "49; turma I p.6; monitoria", "central", NF, ES1, "Azul: lâmina 49.",
    extra="- Pathogens always or frequently cause disease"),
 sh(1791746115653, Z, A_, "Patógeno oportunista", 49, "Azul: 'frequentemente' na lâmina 49."),
 au("nao-uniforme", "The microbiota is not uniform and varies in quality and quantity with the site, <b>age</b> and {{c1::diet}}", R, A_, "Variação da microbiota", "50; turma I p.7", "lateral", NF, ES1, "Rosa: lâmina 50."),
 au("sem-microbiota", "In a host without gut <b>microbiota</b>, a small load of Salmonella, Shigella or {{c1::Clostridioides difficile}} can establish an infection", Z, A_, "Proteção contra Salmonella e C. difficile", "51; turma I p.8; guia veteranos", "central", NF, ES7, "Azul: benefícios 3 e 4 da lâmina 51."),
 au("protecao-pele-mucosas", "The resident microbiota also protects the <b>skin</b> and {{c1::mucosae}} against microbial infections, by competition", Z, A_, "Proteção da pele e das mucosas", "51; turma I p.8", "central", NF, ES1, "Azul: benefícios 5 e 6 da lâmina 51."),
 au("imune-estimulo-pele", "Contact with the resident microbiota stimulates the development of the host {{c1::immune}} <b>defenses</b>", Z, A_, "Estímulo imunológico (benefício 2)", "51; turma I p.8", "central", NF, ES1, "Azul: benefício 2 da lâmina 51.", extra="- The gut is the main site of this stimulation"),
 au("cdiff-metronidazol", "<b>Metronidazole</b> is activated by enzymatic reduction in anaerobes, and its nitro radicals damage bacterial {{c1::DNA}}", R, A_, "Mecanismo do metronidazol", "52; turma I p.9", "lateral", NF, ES7, "Rosa: texto da lâmina 52."),
 sh(1791746140352, V, A_, "Disbiose → C. difficile", 52, "Verde: lâmina 52, disbiose após antibiótico."),
 ak("clinda-colite", 1403561490959, Z, A_, "Clindamicina e colite pseudomembranosa", 52, "Azul: exemplo de disbiose; HY repete o alvo do card de C. difficile.", hy_repete=True),
 ak("metronidazol-anaerobios", 1500499083027, R, A_, "Metronidazol contra anaeróbios", 52, "Rosa: tratamento da lâmina 52; clínica lateral.", clinica_lateral=True),
 ak("cdiff-primeira-linha", 1506181129475, R, A_, "Tratamento atual de C. difficile", 52, "Rosa: a tabela da lâmina 52 (2012) usa metronidazol; AnKing traz a recomendação atual, que prevalece.", clinica_lateral=True),
 au("endogena-uti", "Patients in the <b>ICU</b>, debilitated and with invasive tubes, are prone to {{c1::endogenous}} infections", Z, A_, "UTI e infecção endógena", "53; turma I p.10", "central", NF, ES1, "Azul: lâmina 53."),
 au("endogena-causas", "Surgery, trauma, catheters and low immunity let the <b>normal microbiota</b> reach a new site, causing an {{c1::endogenous}} infection", Z, A_, "Causas da infecção endógena", "53; turma I p.10 e p.33", "central", NF, ES1, "Azul: lâminas 53 e 76.", duplicacao_ok="direção causa → tipo; o card compartilhado cobra tipo → definição"),
 au("prova-aureus-translocacao", "<b>Staphylococcus aureus</b> of the normal skin microbiota becomes pathogenic when an ulcer {{c1::translocates}} it to the bloodstream", Z, A_, "S. aureus normal × patogênico", "53; prova 2023 P2 1.10", "prova", NF, ES1, "Azul: prova 2023 P2 1.10.",
    extra="- Loss of the mechanical barrier moves it to a site where it is not controlled"),
 au("prova-ecoli-itu", "<b>E. coli</b> of the gut microbiota can reach the urethra of women through anal proximity, causing {{c1::urinary tract}} infection", Z, A_, "E. coli da microbiota e ITU", "53; prova 2017 P2 1.8", "prova", NF, ES1, "Azul: prova 2017 P2 1.8.",
    extra="- Its presence in a stool culture is expected"),
 # ---------- B. Pele, vias aéreas, conjuntiva, genital, boca (lâminas 6–15, 54–59, 71–72) ----------
 au("pele-regioes", "The <b>skin</b> microbiota is densest in the humid and warm {{c1::axillae and perineum}}", Z, B_, "Regiões densas da pele", "6; Trabulsi cap. 12", "central", NF, ES1, "Azul: lâmina 6."),
 au("pele-numeros", "Axillae and perineum hold about {{c1::10<sup>6</sup>}} <b>bacteria</b>/cm², and other skin regions about 10<sup>4</sup>", R, B_, "Densidade da pele", "6", "lateral", NF, ES1, "Rosa: números da lâmina 6."),
 au("pele-generos", "The predominant genera of the <b>skin</b> microbiota are {{c1::Staphylococcus}}, {{c2::Corynebacterium}} and {{c3::Propionibacterium}}", Z, B_, "Gêneros da pele", "6; turma I p.11", "central", NF, ES1, "Azul: lâmina 6."),
 au("propionibacterium", "<b>Propionibacterium</b> prefers lipid-rich {{c1::sebaceous}} skin regions and is the bacterium of acne", Z, B_, "Propionibacterium e glândula sebácea", "6; turma I p.11; guia veteranos", "central", NF, ES1, "Azul: lâmina 6."),
 ak("acne-lipases", 1488502547035, R, B_, "Cutibacterium acnes", 6, "Rosa: AnKing de acne, detalhe da lâmina 6."),
 au("pele-camadas", "Skin bacteria live on the surface of the {{c1::stratum corneum}} and inside the <b>hair follicle</b>", Z, B_, "Onde vivem as bactérias da pele", "6", "central", NF, ES1, "Azul: lâmina 6."),
 au("pele-nao-residente", "Low <b>pH</b>, fatty acids of sebum and {{c1::lysozyme}} help eliminate the non-resident flora of the skin", Z, B_, "Eliminação da flora não residente", "6", "central", NF, ES1, "Azul: lâmina 6."),
 au("ouvido", "The <b>ear</b> has a microbiota similar to that of the {{c1::skin}}", R, B_, "Ouvido", "6", "lateral", NF, ES1, "Rosa: lâmina 6."),
 au("pele-oito-horas", "After the surface flora is removed, the resident <b>skin</b> microbiota is restored within about {{c1::8 hours}}", Z, B_, "Recolonização em 8 horas", "7; Trabulsi cap. 12", "central", NF, ES1, "Azul: lâmina 7."),
 au("pele-lavagem", "Washing and bathing do not change the resident <b>skin</b> flora, which recolonizes from the {{c1::hair follicle}}", V, B_, "Lavagem não elimina a flora residente", "7; guia veteranos", "central", NF, ES1, "Verde: figura da lâmina 7."),
 sh(1791763650166, Z, B_, "S. epidermidis na pele", 54, "Azul: lâmina 54."),
 au("epidermidis-90", "<b>S. epidermidis</b> is the main skin colonizer, present in about {{c1::90%}} of people", R, B_, "S. epidermidis 90%", "54; turma I p.11", "lateral", NF, ES1, "Rosa: número da lâmina 54."),
 au("aureus-percentual", "<b>S. aureus</b> colonizes 10–40% of skins and {{c1::50–70%}} of nasal fossae", R, B_, "S. aureus pele e fossas nasais", "54; turma I p.11", "lateral", NF, ES1, "Rosa: números da lâmina 54."),
 ak("epidermidis-hemocultura", 1491774985388, Z, B_, "S. epidermidis contamina hemocultura", 54, "Azul: consequência da microbiota da pele; clínica lateral.", clinica_lateral=True),
 au("peptococcus", "<b>Peptococcus</b> and Peptostreptococcus are Gram-positive {{c1::anaerobic}} cocci of the skin microbiota", R, B_, "Peptococcus", "54; turma I p.11", "lateral", NF, ES1, "Rosa: lâmina 54."),
 au("pele-fungos", "The skin may also harbor fungi such as {{c1::Candida}} and Malassezia", R, B_, "Fungos da pele", "54; turma I p.11", "lateral", NF, ES1, "Rosa: lâmina 54."),
 sh(1791630908669, R, B_, "Candida na microbiota", 54, "Rosa: Candida como flora normal."),
 au("nares-generos", "The nasal fossae are colonized predominantly by <b>Staphylococcus</b> and {{c1::Corynebacterium}}", Z, B_, "Fossas nasais", "8; turma I p.12", "central", NF, ES1, "Azul: lâmina 8."),
 sh(1791763647093, Z, B_, "S. aureus nas narinas", 8, "Azul: portador nasal."),
 au("nares-betalactamico", "Treatment with {{c1::β-lactams}} suppresses the resident nasal microbiota and selects <b>Klebsiella</b>, E. coli and Pseudomonas", Z, B_, "β-lactâmicos e microbiota nasal", "8; turma I p.12", "central", NF, ES7, "Azul: lâmina 8.",
    extra="- This matters in health-care workers"),
 au("faringe", "Alpha-hemolytic streptococci, <b>Neisseria</b> and {{c1::Haemophilus}} colonize the pharynx and trachea", R, B_, "Faringe e traqueia", "8", "lateral", NF, ES1, "Rosa: lista da lâmina 8."),
 au("vias-inferiores", "The <b>bronchioles</b> and alveoli are normally {{c1::sterile}}", V, B_, "Vias aéreas inferiores estéreis", "8", "central", NF, ES1, "Verde: lâmina 8."),
 au("conjuntiva-esteril", "The <b>conjunctiva</b> is normally {{c1::sterile}}", V, B_, "Conjuntiva estéril", "8; turma I p.28", "central", NF, ES1, "Verde: lâmina 8."),
 au("conjuntiva-lagrima", "The conjunctival microbiota is controlled by the flow of {{c1::tears}}, which contain <b>lysozyme</b>", Z, B_, "Lágrima e lisozima", "8; guia veteranos", "central", NF, ES1, "Azul: lâmina 8.",
    extra="- Lysozyme breaks the peptidoglycan of Gram-positive and Gram-negative bacteria"),
 au("conjuntivite", "<b>Bacterial conjunctivitis</b> is caused by Staphylococcus aureus, Streptococcus pneumoniae or {{c1::Neisseria gonorrhoeae}}", R, B_, "Conjuntivite bacteriana", "71; turma I p.28", "lateral", NF, ES6, "Rosa: lâmina 71."),
 ak("tracoma", 1444703682182, R, B_, "Tracoma", 71, "Rosa: lâmina 71."),
 sh(1791576673916, R, B_, "Chlamydia não corada pelo Gram", 71, "Rosa: nota da lâmina 71 (Chlamydia pequena, não corada)."),
 ak("chlamydia-atp", 1500499548289, R, B_, "Intracelular obrigatório não faz ATP", 71, "Rosa: nota da lâmina 71 (vive dentro de células por não sintetizar ATP)."),
 ak("conjuntivite-neonatal-gono", 1402678005051, R, B_, "Conjuntivite neonatal gonocócica", 71, "Rosa: lâmina 71 cita N. gonorrhoeae; clínica lateral.", clinica_lateral=True),
 au("vag-estrogenio", "In a newborn girl, maternal <b>estrogen</b> favors {{c1::Lactobacillus}}, which keeps the vaginal pH low", Z, B_, "Lactobacillus no recém-nascido", "9; turma I p.29", "central", NF, ES3, "Azul: lâmina 9."),
 au("vag-varia", "The <b>vaginal</b> microbiota varies with age, pH and {{c1::hormonal}} secretion", Z, B_, "Variação da microbiota vaginal", "9; turma I p.29", "central", NF, ES3, "Azul: lâmina 9.",
    extra="- Menstrual cycle, contraceptives and sexual activity also change it"),
 ak("vag-lactobacillus", 1516129796813, Z, B_, "Lactobacillus na vagina", 9, "Azul: lâmina 9."),
 au("vag-doderlein", "From puberty to menopause the vaginal microbiota is dominated by <b>Döderlein bacilli</b>, {{c1::Lactobacillus acidophilus}}", Z, B_, "Bacilos de Döderlein", "9; turma I p.29", "central", NF, ES3, "Azul: lâmina 9 e turma I p.29."),
 au("vag-pre-pos", "Before <b>puberty</b> and after menopause, lactobacilli give way to a {{c1::mixed}} microbiota with Corynebacterium, S. epidermidis and E. coli", Z, B_, "Infância e pós-menopausa", "9 e 11; turma I p.29", "central", NF, ES3, "Azul: lâminas 9 e 11."),
 au("vag-glicogenio", "<b>Lactobacilli</b> ferment vaginal {{c1::glycogen}} to lactic acid, keeping the pH acidic", V, B_, "Lactobacilos, glicogênio e pH", "9 e 10; guia veteranos; Trabulsi cap. 12", "central", NF, ES3, "Verde: lâmina 9 e figura da lâmina 10."),
 au("vag-pullulanase", "<b>L. crispatus</b> degrades glycogen with pullulanase, raising lactic acid and {{c1::lowering}} the vaginal pH", R, B_, "L. crispatus × G. vaginalis (figura)", "10", "lateral", NF, ES3, "Rosa: figura da lâmina 10.",
    extra="- Gardnerella vaginalis biofilm degrades glycogen communally and lowers lactic acid"),
 au("vag-staph-ecoli", "The external vagina may carry coagulase-negative <b>staphylococci</b> and {{c1::E. coli}} from skin and gut contamination", R, B_, "Staphylococcus CoNS e E. coli na vagina", "9", "lateral", NF, ES3, "Rosa: lâmina 9."),
 ak("saprophyticus-flora", 1503085944063, V, B_, "S. saprophyticus na vagina", 9, "Verde: HY 1; Trabulsi liga ao ITU de jovens."),
 ak("vag-disbiose", 1516128968450, V, B_, "Supressão de lactobacilos e Candida/Gardnerella", 11, "Verde: HY 1; lâmina 11, leveduras ou bactérias aumentam."),
 ak("vag-vaginose", 1547916062228, Z, B_, "Vaginose bacteriana e lactobacilos", 11, "Azul: consequência da lâmina 11."),
 au("muco-cervical", "<b>Cervical mucus</b> contains {{c1::lysozyme}} and has antibacterial activity", Z, B_, "Muco cervical", "11", "central", NF, ES3, "Azul: lâmina 11."),
 ak("vag-estrogenio-ph", 1547916111318, R, B_, "Estrogênio baixo e pH vaginal", 11, "Rosa: menopausa na lâmina 11."),
 au("uretra", "The male urethra carries <b>Staphylococcus epidermidis</b>, Corynebacterium, Streptococcus and {{c1::E. coli}}", R, B_, "Microbiota da uretra", "12; turma I p.29", "lateral", NF, ES1, "Rosa: lista da lâmina 12."),
 au("uretra-exames", "The urethral microbiota must be considered when interpreting {{c1::secretion and urine}} exams", Z, B_, "Uretra e exames", "12", "central", NF, ES1, "Azul: lâmina 12."),
 au("oral-diversa", "The <b>oral</b> cavity has a highly {{c1::diverse}} microbiota", Z, B_, "Boca muito diversificada", "13; Trabulsi cap. 12", "central", NF, ES1, "Azul: lâmina 13.",
    extra="- More than 700 species live there, many uncultivable"),
 au("oral-numeros", "Saliva contains about 10<sup>8</sup> <b>bacteria</b>/ml and dental plaque about {{c1::10<sup>11</sup>}} bacteria/cm", R, B_, "Densidade oral", "13", "lateral", NF, ES1, "Rosa: lâmina 13 (turma I traz 10^10 para a placa).", duplicacao_ok="número da placa; o card de densidade intestinal cobra outra faixa"),
 au("oral-generos", "Staphylococcus, Streptococcus, Neisseria, Bacteroides, Actinomyces, Treponema and Mycoplasma are the predominant {{c1::oral}} genera", R, B_, "Gêneros orais", "13", "lateral", NF, ES1, "Rosa: lista da lâmina 13."),
 au("oral-importancia", "Caries, periodontitis, actinomycosis and {{c1::subacute endocarditis}} can be caused by members of the <b>oral</b> microbiota", V, B_, "Importância médica da microbiota bucal", "13; turma I p.13", "central", NF, ES7, "Verde: lâmina 13."),
 ak("oral-anaerobios", 1500498491769, V, B_, "Anaeróbios obrigatórios no intestino e na boca", 13, "Verde: HY 1."),
 ak("actinomyces-flora", 1510011540019, V, B_, "Actinomyces na boca, TGI e TGU", 13, "Verde: HY 1; Actinomyces da lâmina 13."),
 ak("viridans-endocardite", 1472072097648, V, B_, "Endocardite subaguda após procedimento dental", 13, "Verde: HY 1; endocardite subaguda da lâmina 13."),
 ak("viridans-placa", 1485805407413, V, B_, "Viridans na placa dental", 13, "Verde: HY 2."),
 sh(1791576680517, Z, B_, "S. mutans e mitis causam cárie", 13, "Azul: cárie da lâmina 13."),
 au("esofago", "The esophagus has no resident microbiota, and its organisms come from {{c1::saliva}} and food", Z, B_, "Esôfago", "14", "central", NF, ES1, "Azul: lâmina 14."),
 au("estomago-acido", "<b>Gastric acid</b> keeps the stomach population at a minimum and protects against some {{c1::enteric}} pathogens", Z, C_, "Estômago e acidez", "14", "central", NF, ES1, "Azul: lâmina 14."),
 au("intestino-ph-alcalino", "As the pH of the intestinal contents becomes {{c1::alkaline}}, the resident <b>microbiota</b> gradually increases", Z, C_, "pH e microbiota ao longo do TGI", "14", "central", NF, ES1, "Azul: lâmina 14."),
 au("h-pylori", "<b>Helicobacter pylori</b> colonizes the stomach of many people without symptoms but is linked to {{c1::ulcers}}, gastritis and gastric carcinoma", R, C_, "H. pylori no estômago", "14; guia veteranos; Trabulsi cap. 12", "lateral", NF, ES1, "Rosa: apostila e livro, ausente nas lâminas."),
 au("dentes", "The flora colonizing the <b>teeth</b> includes Streptococcus mutans, Bacteroides, Fusobacterium and {{c1::Actinomyces}}", R, B_, "Flora dos dentes (mapa)", "15", "lateral", NF, ES1, "Rosa: mapa da lâmina 15."),
 ak("fusobacterium-oral", 1582141138562, R, B_, "Fusobacterium na flora oral", 15, "Rosa: mapa da lâmina 15."),
 au("pele-mapa", "The skin map also lists <b>Pseudomonas aeruginosa</b>, Candida, Torulopsis and {{c1::Pityrosporum}} among colonizers", R, B_, "Mapa da pele", "15", "lateral", NF, ES1, "Rosa: mapa da lâmina 15."),
 au("oral-bacteroides-gram", "<b>Bacteroides</b> are Gram-{{c1::negative}} anaerobic bacilli", Z, B_, "Bacteroides", "57; turma I p.14", "central", NF, ES4, "Azul: lâmina 57."),
 ak("bfragilis-flora", 1592688777796, Z, B_, "B. fragilis na flora colônica", 57, "Azul: lâmina 57."),
 ak("bfragilis-abscesso", 1500498875772, V, B_, "B. fragilis anaeróbio e abscesso", 57, "Verde: HY 1; lâmina 57, sepse e abscessos abdominais."),
 sh(1791746132577, V, B_, "S. mutans: biofilme e cárie", 58, "Verde: lâmina 58, biofilme sobre o esmalte."),
 au("mutans-anaerobiose", "<b>S. mutans</b> biofilm on enamel creates {{c1::anaerobiosis}}, favoring anaerobic bacteria and the progression of caries", Z, B_, "S. mutans cria anaerobiose", "58; turma I p.15", "central", NF, ES4, "Azul: lâmina 58."),
 au("aa-periodontite", "<b>Aggregatibacter actinomycetemcomitans</b> is a Gram-negative bacterium linked to {{c1::periodontitis}}", R, B_, "Aggregatibacter", "58; turma I p.15", "lateral", NF, ES4, "Rosa: lâmina 58.",
    extra="- It is a facultative anaerobe and rarely causes endocarditis"),
 ak("hacek", 1472072157675, R, B_, "HACEK e endocardite", 58, "Rosa: Aa causa endocardite (lâmina 58); clínica lateral.", clinica_lateral=True),
 au("aa-colonia", "<b>A. actinomycetemcomitans</b> colonies are translucent with a {{c1::star-shaped}} center under the microscope", R, B_, "Colônia em estrela", "59; turma I p.16", "lateral", NF, ES4, "Rosa: figura da lâmina 59."),
 # ---------- D. Microbiota intestinal: origem e funções (lâminas 17–22) ----------
 au("feto-esteril", "The fetal <b>gastrointestinal tract</b> is {{c1::sterile}} in the uterus, and the microbiota begins to form at birth", V, D_, "TGI fetal estéril", "17; Trabulsi cap. 12", "central", NF, ES4, "Verde: lâmina 17."),
 sh(1791763663067, V, D_, "Facultativos colonizam o recém-nascido", 17, "Verde: lâmina 17, facultativos primeiro."),
 au("anaerobios-obrigatorios", "As facultative bacteria consume oxygen, the gut is colonized by {{c1::obligate anaerobes}}", V, D_, "Sucessão para anaeróbios obrigatórios", "17 e 37", "central", NF, ES4, "Verde: lâmina 17."),
 au("estabilidade-2anos", "The intestinal microbiota becomes stable around the {{c1::2nd year}} of life", Z, D_, "Estabilidade aos 2 anos", "17", "central", NF, ES4, "Azul: lâmina 17."),
 au("fatores-internos", "Peristalsis, bile acids, pH and immune response are {{c1::internal}} factors shaping the <b>gut microbiota</b>", Z, D_, "Fatores internos", "18 e 19", "central", NF, ES4, "Azul: lâminas 18 e 19."),
 au("fatores-externos", "Maternal microbiota, mode of birth, feeding and antibiotic use are {{c1::external}} factors shaping the <b>gut microbiota</b>", Z, D_, "Fatores externos", "18 e 19", "central", NF, ES4, "Azul: lâminas 18 e 19.",
    extra="- Environmental contaminants are also external factors"),
 au("parto-vaginal", "<b>Vaginal</b> delivery gives the newborn its first microbiota from the maternal {{c1::fecal}} flora, unlike cesarean section", Z, D_, "Tipo de parto", "19; Trabulsi cap. 12", "central", NF, ES4, "Azul: lâmina 19.",
    extra="- After cesarean birth, colonization comes later from skin, environment and staff"),
 au("fator-bifido", "<b>Breast milk</b> contains the {{c1::bifidus factor}}, which favors the growth of Bifidobacterium", Z, D_, "Fator bífido do leite materno", "19; Trabulsi cap. 12", "central", NF, ES4, "Azul: lâmina 19.",
    extra="- It is methyl-N-acetyl-D-glucosamine"),
 au("leite-formula", "Breastfed infants have more <b>Bifidobacterium</b>, whereas formula-fed ones have more {{c1::enterococci}} and clostridia", R, D_, "Aleitamento × mamadeira", "19; Trabulsi cap. 12", "lateral", NF, ES4, "Rosa: Trabulsi, ilustra lâmina 19."),
 au("tgi-harmonia", "The gut microbiota lives in harmony with the host, kept stable by bacteria–bacteria and bacteria–{{c1::host}} interactions", Z, D_, "Estabilidade da microbiota", "20", "central", NF, ES4, "Azul: lâmina 20."),
 au("tgi-patogenica", "The gut microbiota becomes pathogenic when its ecosystem is disturbed by intestinal infections, antibiotics or {{c1::immunosuppressants}}", V, D_, "Perturbação do ecossistema", "20", "central", NF, ES7, "Verde: lâmina 20."),
 au("tgi-populacao", "The intestinal microbial population reaches 10<sup>11</sup> to {{c1::10<sup>12</sup>}} CFU/mL of luminal content", R, D_, "População do TGI", "20", "lateral", NF, ES4, "Rosa: número da lâmina 20."),
 sh(1791668518814, Z, D_, "Antibióticos de amplo espectro destroem a microbiota", 20, "Azul: lâmina 20, antibióticos perturbam o ecossistema."),
 au("funcao-protecao", "The gut microbiota protects the host by competing for adhesion sites and nutrients and by producing {{c1::antimicrobial}} substances", V, D_, "Função: proteção", "21; Trabulsi cap. 12", "central", NF, ES2, "Verde: lâmina 21.",
    extra="- Also called colonization resistance or barrier effect"),
 au("funcao-imune", "The gut microbiota stimulates the development of the immune system and {{c1::tolerance}}", V, D_, "Função: modulação imunológica", "21", "central", NF, ES2, "Verde: lâmina 21."),
 au("intestino-orgao-imune", "The <b>intestine</b> is the largest immune organ, with about 80% of the body's {{c1::antibody-producing}} cells", Z, D_, "Intestino, maior órgão imunológico", "21; Trabulsi cap. 12", "central", NF, ES2, "Azul: lâmina 21.",
    extra="- Its predominant isotype is IgA"),
 sh(1791023301592, Z, D_, "IgA no lúmen intestinal", 21, "Azul: isótipo do intestino."),
 sh(1791051804825, V, D_, "Vitaminas K e B produzidas pela flora", 21, "Verde: lâmina 21, nutrição e metabolismo; criado na Fisiologia UC08."),
 ak("vitk-antibiotico", 1473995752044, V, D_, "Antibióticos e deficiência de vitamina K", 21, "Verde: HY 2; disbiose reduz a vitamina K."),
 au("funcao-fermentacao", "Gut bacteria contribute to nutrition by {{c1::fermenting}} carbohydrates that the host cannot digest", Z, D_, "Função: fermentação de carboidratos", "21", "central", NF, ES2, "Azul: lâmina 21."),
 au("funcao-ph-motilidade", "The microbiota changes intestinal pH and motility, favoring the absorption of {{c1::ions and water}}", Z, D_, "pH, motilidade e absorção", "21", "central", NF, ES2, "Azul: lâmina 21."),
 au("funcao-snc", "Metabolites of the gut microbiota interact with the {{c1::vagus nerve}} and modulate the <b>CNS</b>", Z, D_, "Modulação do SNC", "21", "central", NF, ES2, "Azul: lâmina 21."),
 au("desafios", "To persist in the gut, a bacterium must meet its nutritional needs while facing competitors and host {{c1::defenses}}", R, D_, "Desafios da microbiota", "22", "lateral", NF, ES2, "Rosa: lâmina 22."),
 # ---------- E. Barreira e metabolismo (lâminas 23–28, 60–62) ----------
 au("colon-muco", "In the colon, the dense <b>inner mucus layer</b> excludes bacteria, whereas the outer layer is {{c1::colonized}} by commensals", Z, E_, "Camadas de muco do cólon", "23 e 28", "central", NF, ES2, "Azul: figuras das lâminas 23 e 28."),
 au("microvilosidades", "Intestinal epithelial cells have <b>microvilli</b> rich in {{c1::actin}}", R, E_, "Microvilosidades", "24", "lateral", NF, ES2, "Rosa: item a da lâmina 24."),
 sh(1791000304527, Z, E_, "Junções oclusivas", 24, "Azul: item b da lâmina 24."),
 au("glicocalice", "The <b>glycocalyx</b> of the epithelial surface is part of the barrier that limits microbial {{c1::contact}}", R, E_, "Glicocálix", "24", "lateral", NF, ES2, "Rosa: item c da lâmina 24."),
 sh(1791023299492, Z, E_, "Peptídeos antimicrobianos (Paneth)", 24, "Azul: item d da lâmina 24."),
 sh(1790980915172, Z, E_, "Células M", 24, "Azul: item e da lâmina 24."),
 au("folículo-apc", "In the Peyer's patch follicle, antigen-presenting cells such as {{c1::dendritic cells}} receive antigens sampled by <b>M cells</b>", R, E_, "APCs do folículo e células dendríticas", "24", "lateral", NF, ES2, "Rosa: itens f e g da lâmina 24."),
 au("eubiose", "In <b>eubiosis</b> the intestinal barrier keeps a {{c1::tolerant}} immune response with IgA and antimicrobial peptides", Z, E_, "Eubiose", "25", "central", NF, ES2, "Azul: lâmina 25."),
 au("disbiose-barreira", "<b>Dysbiosis</b> damages the tight junctions and causes a barrier defect called {{c1::leaky gut}}", V, E_, "Disbiose e barreira defeituosa", "25", "central", NF, ES2, "Verde: lâmina 25."),
 sh(1791014719199, Z, E_, "Disbiose: LPS atinge o sangue", 25, "Azul: lâmina 25."),
 sh(1791000315902, Z, E_, "Claudinas e ocludinas", 25, "Azul: proteínas das junções da lâmina 25."),
 sh(1791014718900, V, E_, "Butirato nutre colonócitos", 26, "Verde: AGCC como energia (lâmina 26)."),
 au("agcc-nomes", "The main <b>short-chain fatty acids</b> are acetate, propionate and {{c1::butyrate}}", Z, E_, "AGCC", "26; Trabulsi cap. 12", "central", NF, ES2, "Azul: lâmina 26."),
 au("agcc-genes", "Short-chain fatty acids can enter intestinal epithelial cells and alter {{c1::gene}} expression", R, E_, "AGCC e expressão gênica", "62; turma I p.19", "lateral", NF, ES2, "Rosa: lâmina 62."),
 au("colipase", "The microbiota stimulates tissue production of {{c1::colipase}}, involved in lipid metabolism", R, E_, "Colipase", "26", "lateral", NF, ES2, "Rosa: lâmina 26."),
 au("gluconato-biliares", "The microbiota also takes part in gluconate and {{c1::bile acid}} metabolism", R, E_, "Gluconato e ácidos biliares", "26", "lateral", NF, ES2, "Rosa: lâmina 26."),
 au("simbionte-polissacarideos", "A symbiont such as <b>Bacteroides</b> degrades luminal {{c1::polysaccharides}} with many carbohydrate-degrading enzymes", Z, E_, "Bacteroides e polissacarídeos", "27", "central", NF, ES2, "Azul: figura da lâmina 27."),
 sh(1791746116201, Z, E_, "Salmonella não compete por nutrientes", 27, "Azul: figura da lâmina 27."),
 sh(1791629596747, Z, E_, "Transporte de IgA por pIgR", 28, "Azul: figura da lâmina 28."),
 au("macrofago-bacterias", "<b>Macrophages</b> of the lamina propria kill bacteria that {{c1::penetrate}} the epithelium", R, E_, "Macrófago mata bactérias que penetram", "28", "lateral", NF, ES2, "Rosa: figura da lâmina 28."),
 # ---------- F. Composição, probióticos, disfunções (lâminas 29–43, 60–70) ----------
 au("densidade-aumenta", "<b>Bacterial density</b> increases along the GI tract and is highest in the {{c1::colon}}", V, F_, "Densidade crescente até o cólon", "29", "central", NF, ES4, "Verde: lâmina 29."),
 au("densidade-numeros", "The small intestine holds 10<sup>4</sup> to {{c1::10<sup>8</sup>}} CFU/ml, versus 10<sup>10</sup>–10<sup>12</sup> in the colon", R, F_, "Números por segmento", "29 e 35", "lateral", NF, ES4, "Rosa: números das lâminas 29 e 35."),
 au("anaerobios-razao", "In the colon, <b>anaerobes</b> outnumber aerobes by about {{c1::100 to 1,000}} times", R, F_, "Anaeróbios × aeróbios", "35; turma I p.17", "lateral", NF, ES4, "Rosa: tabela da lâmina 35 e turma I p.17."),
 au("quatrocentas-especies", "The gut has about 400 species, but only {{c1::40}} are dominant", R, F_, "40 espécies dominantes", "30", "lateral", NF, ES4, "Rosa: lâmina 30."),
 au("filos-dominantes", "The dominant phyla of the gut microbiota are {{c1::Bacteroidetes and Firmicutes}}", V, F_, "Filos dominantes", "30; turma I p.22", "central", NF, ES4, "Verde: lâmina 30.",
    extra="- Together they make up about 90% of the gut microbiota"),
 au("generos-anaerobios", "Bacteroides, Bifidobacterium, Clostridium and Eubacterium are the dominant {{c1::anaerobic}} genera of the <b>gut</b>", Z, F_, "Gêneros anaeróbios", "30", "central", NF, ES4, "Azul: lâmina 30."),
 au("generos-aerobios", "Escherichia, Enterococcus, Streptococcus and Klebsiella are the dominant {{c1::aerobic}} (facultative) genera of the <b>gut</b>", Z, F_, "Gêneros aeróbios", "30", "central", NF, ES4, "Azul: lâmina 30."),
 au("quatro-filos", "In healthy adults, 80% of the fecal microbiota belongs to Bacteroidetes, Firmicutes, Proteobacteria and {{c1::Actinobacteria}}", R, F_, "Quatro filos", "30; turma I p.22", "lateral", NF, ES4, "Rosa: turma I p.22."),
 au("bacteroidetes-filo", "<b>Bacteroidetes</b> are mostly Gram-negative fermentative bacteria that modulate the {{c1::immune system}}", R, F_, "Filo Bacteroidetes", "65; turma I p.22", "lateral", NF, ES4, "Rosa: turma I p.22."),
 au("firmicutes-filo", "<b>Firmicutes</b> include Lactobacillus and {{c1::Clostridium}}, and most are Gram-positive", R, F_, "Filo Firmicutes", "64 e 65; turma I p.21", "lateral", NF, ES4, "Rosa: turma I p.21–22."),
 au("proteobacteria-filo", "{{c1::Proteobacteria}} include Escherichia, Salmonella, Vibrio and Helicobacter", R, F_, "Filo Proteobacteria", "64; turma I p.21", "lateral", NF, ES4, "Rosa: turma I p.21."),
 au("dieta-modula", "The main modulator of the gut microbiota is {{c1::diet}}", Z, F_, "Alimentação modula a microbiota", "65; turma I p.22", "central", NF, ES4, "Azul: turma I p.22."),
 au("obesidade-firmicutes", "Obese individuals have more {{c1::Firmicutes}} and fewer Bacteroidetes than lean ones", R, F_, "Microbiota e obesidade", "67; turma I p.24", "lateral", NF, ES4, "Rosa: turma I p.24.",
    extra="- The obese gut microbiome has a greater capacity for energy harvest"),
 au("bacteroides-grupos", "Bacteroidetes and Firmicutes contain both beneficial genera and species linked to {{c1::inflammation}}", R, F_, "Dupla face dos filos", "65; turma I p.22", "lateral", NF, ES4, "Rosa: turma I p.22."),
 au("benefica-lacto-bifido", "<b>Bifidobacteria</b> and lactobacilli are beneficial gut bacteria because they have no {{c1::pathogenicity}} factors for humans", Z, F_, "Bifidobactérias e lactobacilos benéficos", "36; Trabulsi cap. 12", "central", NF, ES4, "Azul: lâmina 36."),
 au("nocivas", "Gut bacteria such as <b>Pseudomonas aeruginosa</b>, Proteus, staphylococci, clostridia and Veillonella may produce {{c1::toxins}}", R, F_, "Bactérias nocivas (figura)", "36", "lateral", NF, ES4, "Rosa: figura da lâmina 36.",
    extra="- Harmful effects include diarrhea, liver damage and cancer"),
 au("lacto-adesao", "<b>Lactobacilli</b> adhere to the intestinal {{c1::epithelium}}, as seen in electron microscopy", R, F_, "Adesão de Lactobacillus", "31", "lateral", NF, ES4, "Rosa: figura da lâmina 31."),
 sh(1791666339316, V, F_, "Probiótico", 32, "Verde: definição da lâmina 32; criado no Controle microbiológico."),
 au("prebiotico-def", "<b>Prebiotics</b> are food ingredients not absorbed by the intestine that {{c1::selectively stimulate}} beneficial bacteria", V, F_, "Prebiótico", "32; Trabulsi cap. 12", "central", NF, ES2, "Verde: definição da lâmina 32."),
 au("probioticos-generos", "The most common probiotics are <b>Lactobacillus</b> and {{c1::Bifidobacterium}}", Z, F_, "Probióticos comuns", "32; turma I p.26", "central", NF, ES2, "Azul: lâmina 32."),
 au("boulardii", "The yeast {{c1::Saccharomyces boulardii}} is also a <b>probiotic</b>", R, F_, "S. boulardii", "69; turma I p.26", "lateral", NF, ES2, "Rosa: turma I p.26."),
 au("prebioticos-colon", "<b>Prebiotics</b> escape digestion by human enzymes, reach the colon and are {{c1::fermented}} by the microbiota", Z, F_, "Prebióticos chegam ao cólon", "33 e 34; turma I p.26", "central", NF, ES2, "Azul: lâminas 33 e 34."),
 au("prebioticos-exemplos", "Common prebiotics are inulin, FOS, GOS and {{c1::lactulose}}", R, F_, "Exemplos de prebióticos", "34 e 69", "lateral", NF, ES2, "Rosa: lista das lâminas 34 e 69."),
 au("fermentacao-agcc", "Fermentation of prebiotics yields {{c1::short-chain fatty acids}} and gases, which reduce facultative anaerobes and stabilize the microbiota", Z, F_, "Fermentação de prebióticos", "33", "central", NF, ES2, "Azul: figura da lâmina 33."),
 au("bifidogenico", "Prebiotics have a {{c1::bifidogenic}} effect, stimulating the growth of bifidobacteria in the <b>colon</b>", Z, F_, "Efeito bifidogênico", "34; Trabulsi cap. 12", "central", NF, ES2, "Azul: figura da lâmina 34."),
 au("probiotico-imune", "<b>Probiotics</b> stimulate host immunity by raising antibody levels and {{c1::macrophage}} activity", Z, F_, "Probióticos estimulam a imunidade", "34", "central", NF, ES2, "Azul: figura da lâmina 34."),
 au("probiotico-calcio", "<b>Probiotics</b> may increase the absorption of {{c1::calcium}}", R, F_, "Probióticos e cálcio", "34", "lateral", NF, ES2, "Rosa: figura da lâmina 34."),
 au("probiotico-transitorio", "Current <b>probiotics</b> do not colonize the gut permanently and act only while being {{c1::consumed}}", Z, F_, "Efeito transitório dos probióticos", "32; Trabulsi cap. 12", "central", NF, ES2, "Azul: Trabulsi."),
 au("probiotico-requisitos", "A <b>probiotic</b> must lack virulence, survive in the gut, adhere to mucosa and {{c1::inhibit pathogens}}", R, F_, "Requisitos do probiótico", "32; Trabulsi cap. 12", "lateral", NF, ES2, "Rosa: Trabulsi."),
 au("sucessao-dia1", "On the first day of life the gut is colonized by facultative anaerobes such as E. coli and {{c1::Streptococcus}}", V, F_, "Sucessão: primeiro dia", "37", "central", NF, ES4, "Verde: lâmina 37."),
 au("sucessao-bifido", "Once oxygen is consumed, anaerobes such as {{c1::Bifidobacterium}} take over and produce short-chain fatty acids", V, F_, "Sucessão: anaeróbios e AGCC", "37", "central", NF, ES4, "Verde: lâmina 37."),
 au("sucessao-1mes", "By one month the gut contains Bifidobacterium, E. coli, Lactobacillus, Bacteroides and {{c1::Prevotella}}", R, F_, "Sucessão: um mês", "37", "lateral", NF, ES4, "Rosa: lâmina 37."),
 au("janela-th", "In the first year the immune system is moldable, a window to regulate the {{c1::Th1:Th2}} balance", V, F_, "Janela de regulação imune", "38", "central", NF, ES4, "Verde: lâmina 38."),
 au("th-doenca", "A Th2 > Th1 ratio favors {{c1::atopic}} disease, whereas Th1 > Th2 favors {{c2::autoimmune}} disease", V, F_, "Relação Th1:Th2 e doença", "38", "central", NF, ES4, "Verde: gráfico da lâmina 38.",
    extra="- Th2 = Th1 corresponds to health"),
 au("janela-meses", "The window for immune regulation spans roughly the first {{c1::12 months}} of life", R, F_, "Duração da janela", "38", "lateral", NF, ES4, "Rosa: gráfico da lâmina 38."),
 au("higiene", "According to the <b>hygiene hypothesis</b>, excessive environmental hygiene {{c1::increases}} atopy and autoimmune disease", V, F_, "Teoria da higiene", "39; Trabulsi cap. 12", "central", NF, ES4, "Verde: lâmina 39.",
    extra="- A contaminated environment stimulates regulation of TH cells"),
 au("tres-funcoes", "The three functions of the gut microbiota are antibacterial, immunomodulatory and {{c1::nutritional-metabolic}}", Z, F_, "Resumo das funções", "40", "central", NF, ES2, "Azul: lâmina 40."),
 au("disfuncoes-curto", "Necrotizing enterocolitis, pseudomembranous colitis and antibiotic-associated diarrhea are {{c1::short-term}} consequences of gut dysbiosis", V, F_, "Disfunções a curto prazo", "41", "central", NF, ES7, "Verde: lâmina 41."),
 au("disfuncoes-longo", "Allergy is a medium-term consequence of gut <b>dysbiosis</b>, whereas IBD and colon cancer are {{c1::long-term}} ones", Z, F_, "Disfunções a médio e longo prazo", "41", "central", NF, ES7, "Azul: lâmina 41."),
 ak("nec-prematuro", 1482959865798, V, F_, "Enterocolite necrosante em prematuros", 41, "Verde: HY 2; lâmina 41."),
 ak("nec-invasao", 1523210715916, Z, F_, "NEC: invasão bacteriana da parede", 41, "Azul: lâmina 41."),
 au("diarreia-antibiotico", "<b>Antibiotic-associated</b> diarrhea results from loss of the normal {{c1::microbiota}}", Z, F_, "Diarreia por antibiótico", "41", "central", NF, ES7, "Azul: lâmina 41."),
 au("probiotico-nec", "<b>Probiotics</b> in preterm infants reduce the frequency and mortality of {{c1::necrotizing enterocolitis}}", R, F_, "Probióticos e NEC", "41; Trabulsi cap. 12", "lateral", NF, ES7, "Rosa: Trabulsi."),
 au("eixo-intestino-cerebro", "Neural, immune and endocrine pathways, including the vagus nerve, link the gut microbiota to the {{c1::brain}}", R, F_, "Eixo cérebro-intestino", "42", "lateral", NF, ES2, "Rosa: figura da lâmina 42."),
 au("desequilibrio-fatores", "Unbalanced diet, alcohol, smoking, infection, antibiotics, aging and stress cause {{c1::dysbiosis}} of the gut microbiota", Z, F_, "Fatores de desequilíbrio", "43", "central", NF, ES7, "Azul: lâmina 43."),
 # ---------- C. Digestivo (turma I) ----------
 au("tgi-fonte", "The intestinal microbiota is the main source of normal microbiota and the most important cause of {{c1::endogenous}} infections", V, C_, "Intestino: fonte e infecção endógena", "60; turma I p.17", "central", NF, ES1, "Verde: turma I p.17."),
 au("fezes-peso", "More than {{c1::50%}} of the weight of feces is <b>bacteria</b>", R, C_, "Peso das fezes", "60; turma I p.17", "lateral", NF, ES1, "Rosa: turma I p.17."),
 au("ftm-colite", "<b>Fecal microbiota transplantation</b> cures more than 90% of C. difficile colitis by correcting {{c1::dysbiosis}}", V, C_, "Transplante de microbiota fecal", "66; turma I p.23", "central", NF, ES7, "Verde: lâmina 66."),
 au("ftm-china", "Fecal transplantation was already used in China in the {{c1::4th century}}", R, C_, "FMT na China", "66; turma I p.23", "lateral", NF, ES7, "Rosa: lâmina 66."),
 au("ftm-einstein", "The first fecal transplant in Brazil was done in {{c1::2013}} at Hospital Israelita Albert Einstein", R, C_, "FMT no Brasil", "68; turma I p.25", "lateral", NF, ES7, "Rosa: lâmina 68."),
 # ---------- G. Epidemiologia (lâminas 74–96) ----------
 au("di-formula", "Infectious disease depends on the infecting dose and virulence and is inversely proportional to host {{c1::resistance}}", V, G_, "DI = N×V/R", "74; turma I p.31; monitoria", "central", NF, ES5, "Verde: lâmina 74, fórmula."),
 au("exogena-def", "An <b>exogenous</b> infection is acquired from an external {{c1::reservoir}}", V, G_, "Infecção exógena", "75; turma I p.32", "central", NF, ES5, "Verde: lâmina 75.", extra="- Endogenous infections come from the normal microbiota"),
 au("fonte-homem", "In most exogenous infections the source is a <b>human</b>, either a sick person or a healthy {{c1::carrier}}", Z, G_, "Fonte humana", "77; turma I p.34", "central", NF, ES5, "Azul: lâmina 77."),
 au("antroponose-zoonose", "<b>Anthroponoses</b> are transmitted between humans, whereas {{c1::zoonoses}} come from animal reservoirs", Z, G_, "Antroponoses × zoonoses", "77; turma I p.34", "central", NF, ES5, "Azul: lâmina 77."),
 au("typhoid-mary", "<b>Typhoid Mary</b> was a healthy {{c1::carrier}} of Salmonella typhi who infected dozens of people as a cook", Z, G_, "Portador são: Mary Mallon", "79; turma I p.36", "central", NF, ES5, "Azul: lâmina 79."),
 ak("typhi-vesicula", 1510103483272, V, G_, "Portador crônico de S. typhi: vesícula", 79, "Verde: HY 2; portador são da lâmina 79."),
 au("typhoid-transmissao", "<b>Typhoid fever</b> is transmitted by food or water contaminated with {{c1::feces}}", R, G_, "Transmissão da febre tifoide", "79; turma I p.36", "lateral", NF, ES5, "Rosa: quadro da lâmina 79.", extra="- Incubation lasts 6–30 days"),
 sh(1791593042493, Z, G_, "Aedes transmite dengue", 81, "Azul: vetor da lâmina 81."),
 au("aedes-doencas", "<b>Aedes aegypti</b> transmits dengue, Zika, chikungunya and {{c1::yellow fever}}", R, G_, "Doenças do Aedes", "81 e 82; turma I p.38", "lateral", NF, ES6, "Rosa: lâminas 81 e 82."),
 ak("peste-pulgas", 1506285248660, Z, G_, "Peste: vetor pulga", 81, "Azul: peste da lâmina 81; clínica lateral.", clinica_lateral=True),
 au("dengue-incidencia", "In the last 50 years the incidence of <b>dengue</b> rose about {{c1::30}}-fold", R, G_, "Dengue: incidência", "82; turma I p.39", "lateral", NF, ES6, "Rosa: número da lâmina 82."),
 au("contato-direto", "<b>Direct contact</b> may be immediate, as in STDs, or {{c1::mediate}}, as in tuberculosis", Z, G_, "Contato direto imediato e mediato", "84; turma I p.41", "central", NF, ES5, "Azul: lâmina 84."),
 au("vias-lista", "Direct contact, vectors, soil, food, water, air and contaminated therapeutic solutions are {{c1::routes of transmission}} of <b>exogenous</b> infection", V, G_, "Vias de transmissão", "84; turma I p.41", "central", NF, ES5, "Verde: lâmina 84, pergunta de revisão 8."),
 ak("lepto-agua", 1516067829624, R, G_, "Leptospira: água com urina animal", 84, "Rosa: leptospirose é vetor e fonte na lâmina 84; clínica lateral.", clinica_lateral=True),
 au("fonte-via", "The <b>source</b> is where the agent lives and multiplies, whereas the {{c1::route of transmission}} carries it to the host", V, G_, "Fonte × via de transmissão", "89 e 90; turma I p.46–47", "central", NF, ES5, "Verde: lâmina 89 e perguntas 9–10 da lâmina 90."),
 ak("transmissao-vertical", 1502152410992, Z, G_, "Transmissão vertical", 85, "Azul: lâmina 85."),
 au("transmissao-horizontal", "<b>Horizontal</b> transmission occurs between individuals regardless of {{c1::kinship}}", Z, G_, "Transmissão horizontal", "85; turma I p.42", "central", NF, ES5, "Azul: lâmina 85."),
 au("portas-lista", "Skin, mucosae, airways and the oral (fecal–oral) route are {{c1::portals of entry}} of <b>exogenous</b> infection", V, G_, "Portas de entrada", "87; turma I p.44", "central", NF, ES5, "Verde: lâmina 87, pergunta de revisão 7."),
 au("porta-congenita", "<b>Congenital</b> infection reaches the fetus through the {{c1::placenta}}", Z, G_, "Porta de entrada congênita", "87; turma I p.44", "central", NF, ES5, "Azul: lâmina 87."),
 au("porta-iatrogenica", "{{c1::Iatrogenic}} infection enters through contaminated <b>blood</b>, instruments, needles or vaccines", Z, G_, "Porta de entrada iatrogênica", "87; turma I p.44", "central", NF, ES5, "Azul: lâmina 87."),
 au("modo-transmissao", "For prevention, knowing the {{c1::mode of transmission}} can matter more than identifying the causative agent", V, G_, "Modo de transmissão × agente", "88; turma I p.45", "central", NF, ES5, "Verde: lâmina 88.", extra="- AIDS is the classic example"),
 sh(1791746114724, V, G_, "Infecção", 91, "Verde: lâmina 91."),
 au("infeccao-doenca", "A bacterium establishes an infection when it settles in the host, but causes <b>disease</b> only if it {{c1::overcomes}} the host defenses", V, G_, "Infecção não é sinônimo de doença", "91; turma I p.48; monitoria", "central", NF, ES5, "Verde: lâmina 91, pergunta central."),
 sh(1791746116702, Z, G_, "Iceberg: infecção subclínica", 92, "Azul: pergunta da lâmina 92."),
 sh(1791746115228, Z, G_, "Patogenicidade × virulência", 93, "Azul: pergunta 2 da lâmina 93."),
 au("incubacao", "The <b>incubation period</b> is the time the bacterium needs to {{c1::multiply}} enough to cause the first clinical manifestations", Z, G_, "Período de incubação", "91 e 94; turma I p.51", "central", NF, ES5, "Azul: lâminas 91 e 94."),
 sh(1791746116575, Z, G_, "Período latente", 94, "Azul: lâmina 94."),
 au("transmissibilidade", "During the period of <b>transmissibility</b> an infected person can {{c1::transmit}} the agent, sick or not", Z, G_, "Período de transmissibilidade", "94; turma I p.51", "central", NF, ES5, "Azul: lâmina 94."),
 au("john-snow", "<b>John Snow</b> traced the 1854 London cholera outbreak to a contaminated {{c1::water pump}} in Soho", Z, G_, "John Snow", "94; turma I p.51", "central", NF, ES5, "Azul: lâmina 94.", extra="- He is considered the father of modern epidemiology"),
 au("epidemiologia-def", "<b>Epidemiology</b> identifies the causes of a disease by quantitatively studying its determinants in the {{c1::population}}", R, G_, "Definição de epidemiologia", "94; Trabulsi cap. 13", "lateral", NF, ES5, "Rosa: lâmina 94."),
 au("incidencia-prevalencia", "<b>Incidence</b> counts {{c1::new}} cases in a period, whereas prevalence counts existing cases", R, G_, "Incidência × prevalência", "94; Trabulsi cap. 13", "lateral", NF, ES5, "Rosa: Trabulsi cap. 13, indicadores de morbidade; ausente nas lâminas."),
 sh(1791746115530, Z, G_, "LD50", 95, "Azul: lâmina 95."),
 au("ld50-pneumo", "<b>Streptococcus pneumoniae</b> is highly virulent and reaches the LD50 with {{c1::few}} cells", R, G_, "Virulência e LD50", "95; turma I p.52", "lateral", NF, ES5, "Rosa: lâmina 95."),
 au("hospital-ambiente", "Controlling microbial contamination of the <b>hospital</b> environment prevents {{c1::nosocomial}} infections in vulnerable patients", Z, G_, "Ambiente hospitalar", "96; turma I p.53", "central", NF, ES5, "Azul: pergunta 10 da lâmina 96."),
]

VERSO = {
 "pele-regioes": "- Moisture, heat and nutrients such as sweat and sebum allow bacteria to survive",
 "pele-numeros": "- Axillae and perineum are also the regions closest to mucosae",
 "pele-generos": "- Staphylococcus and Corynebacterium are facultative, whereas Propionibacterium is anaerobic",
 "propionibacterium": "- It feeds on sebum lipids inside the follicle",
 "pele-camadas": "- The follicle population recolonizes the surface after washing",
 "pele-nao-residente": "- These factors remove transient bacteria but spare the resident flora",
 "ouvido": "- The external and middle ear resemble the skin",
 "pele-oito-horas": "- Recolonization comes from the hair follicle",
 "pele-lavagem": "- Soap, water, disinfectant and scrubbing only remove the surface bacteria",
 "nares-generos": "- S. aureus colonizes the nose of many healthy people",
 "faringe": "- Mycoplasma and diphtheroids are also found there",
 "vias-inferiores": "- Mucociliary clearance keeps the lower airways sterile",
 "conjuntiva-esteril": "- Tears wash and lyse bacteria that try to settle",
 "vag-estrogenio": "- Maternal estrogen is passed to the newborn girl",
 "vag-lactobacillus": "- It ferments glycogen and acidifies the vagina",
 "vag-doderlein": "- Estrogen sustains glycogen and therefore lactobacilli",
 "vag-pre-pos": "- Low estrogen raises the vaginal pH",
 "vag-glicogenio": "- The low pH blocks bacteria that grow at neutral pH",
 "vag-staph-ecoli": "- They come from contamination by skin and gastrointestinal microbiota",
 "muco-cervical": "- Lysozyme breaks bacterial peptidoglycan",
 "uretra": "- The anterior urethra has a low density of bacteria",
 "uretra-exames": "- Urethral organisms can contaminate samples",
 "oral-numeros": "- Plaque is a biofilm, so its density is far higher than saliva",
 "oral-generos": "- Anaerobes such as Bacteroides and Actinomyces predominate in plaque and gingival crevices",
 "oral-importancia": "- Viridans streptococci reach the blood after dental procedures",
 "esofago": "- It is a transit organ with no stable colonization",
 "estomago-acido": "- Acid pH limits the stomach to about 10<sup>3</sup> CFU/ml",
 "intestino-ph-alcalino": "- The colon holds by far the largest population",
 "h-pylori": "- It survives acid with urease",
 "dentes": "- Plaque anaerobes contribute to caries and periodontitis",
 "fusobacterium-oral": "- It is also an anaerobe of the gingival crevice",
 "pele-mapa": "- Pseudomonas aeruginosa is a transient or opportunistic skin organism",
 "feto-esteril": "- Colonization starts in the birth canal or right after birth",
 "anaerobios-obrigatorios": "- Facultative bacteria such as E. coli lower the redox potential",
 "estabilidade-2anos": "- Adult-like composition is reached by about 2 years",
 "fatores-internos": "- External factors include maternal microbiota, birth mode, feeding and antibiotics",
 "leite-formula": "- Breast milk also lowers the intestinal pH",
 "tgi-harmonia": "- Competition and cooperation among bacteria keep composition steady",
 "tgi-patogenica": "- Imbalance lets opportunists overgrow",
 "tgi-populacao": "- The colon is the densest microbial habitat of the body",
 "funcao-imune": "- Gut bacteria train the immune system without causing inflammation",
 "vitk-antibiotico": "- Gut bacteria normally synthesize vitamin K",
 "funcao-fermentacao": "- Fermentation yields short-chain fatty acids and gases",
 "funcao-ph-motilidade": "- Short-chain fatty acids acidify the lumen and influence motility",
 "funcao-snc": "- Bacterial metabolites signal through the gut–brain axis",
 "desafios": "- Survival requires nutrients, adhesion and escape from host defenses",
 "colon-muco": "- The small intestine has a single thinner mucus layer",
 "microvilosidades": "- Microvilli enlarge the absorptive surface",
 "glicocalice": "- It is a carbohydrate coat on the apical surface",
 "folículo-apc": "- Peyer's patches sample luminal antigens",
 "eubiose": "- Dysbiosis breaks this tolerance",
 "disbiose-barreira": "- Bacterial products such as LPS then cross the barrier",
 "agcc-nomes": "- They are produced by bacterial fermentation of fiber",
 "colipase": "- Colipase anchors pancreatic lipase to fat droplets",
 "gluconato-biliares": "- Bacteria deconjugate and transform bile acids",
 "simbionte-polissacarideos": "- Pathogens such as Salmonella lack these enzymes",
 "macrofago-bacterias": "- Dendritic cells and IgA handle bacteria that stay in the lumen",
 "densidade-aumenta": "- The stomach is nearly empty, the small intestine intermediate",
 "densidade-numeros": "- The stomach has only 10 to 10<sup>3</sup> CFU/ml",
 "quatrocentas-especies": "- Species number is high, but a few dominate",
 "generos-anaerobios": "- Anaerobes dominate the colon",
 "generos-aerobios": "- They are a small fraction of the colonic population",
 "quatro-filos": "- Bacteroidetes and Firmicutes make up about 90%",
 "lacto-adesao": "- Adhesion helps them compete for epithelial sites",
 "prebiotico-def": "- Examples are inulin and oligosaccharides",
 "probioticos-generos": "- The yeast S. boulardii is also used",
 "probiotico-transitorio": "- Benefit lasts only while they are consumed",
 "probiotico-requisitos": "- Not every symbiont qualifies as a probiotic",
 "prebioticos-colon": "- Fermentation feeds bifidobacteria and lactobacilli",
 "fermentacao-agcc": "- The lower pH disfavors facultative anaerobes",
 "prebioticos-exemplos": "- They occur naturally in onion, garlic, chicory and milk",
 "bifidogenico": "- Human milk oligosaccharides are natural bifidogenic factors",
 "probiotico-imune": "- Probiotics also raise specific IgA during infection",
 "probiotico-calcio": "- Absorption of other nutrients may also improve",
 "anaerobios-razao": "- Aerobes and facultative bacteria are a small minority",
 "benefica-lacto-bifido": "- They have never been implicated in gut infections",
 "sucessao-dia1": "- Oxygen is still abundant in the newborn gut",
 "sucessao-bifido": "- Bacteroides and Clostridium follow",
 "sucessao-1mes": "- Obligate anaerobes now dominate",
 "janela-th": "- Th1 and Th2 cells are shaped by early microbial contact",
 "janela-meses": "- The graph marks it between about 3 and 12 months",
 "tres-funcoes": "- Nutritional activity includes vitamins and short-chain fatty acids",
 "disfuncoes-curto": "- Medium-term is allergy, long-term is IBD and colon cancer",
 "disfuncoes-longo": "- Short-term are NEC, pseudomembranous colitis and antibiotic diarrhea",
 "nec-invasao": "- Premature, formula-fed infants are at risk",
 "diarreia-antibiotico": "- Antibiotics remove competitors, so opportunists overgrow",
 "probiotico-nec": "- The ideal strain and dose are still being defined",
 "eixo-intestino-cerebro": "- Diet, probiotics and antibiotics influence it",
 "desequilibrio-fatores": "- Antibiotics are the clearest cause",
 "tres-desfechos": "- Permanent colonization is the normal microbiota",
 "nao-uniforme": "- Each body site has its own community",
 "sem-microbiota": "- Colonization resistance is lost",
 "protecao-pele-mucosas": "- Resident bacteria occupy sites and nutrients",
 "cdiff-metronidazol": "- Only anaerobes and protozoa activate it",
 "endogena-uti": "- ICU patients also take antibiotics",
 "endogena-causas": "- Immunosuppression lowers control of the microbiota",
 "epidermidis-90": "- S. aureus is far less frequent on skin",
 "aureus-percentual": "- Rates are higher in hospital staff and dermatoses",
 "epidermidis-hemocultura": "- A single positive culture is often a contaminant",
 "peptococcus": "- They may be anaerobic or microaerophilic",
 "pele-fungos": "- Malassezia is lipophilic",
 "oral-bacteroides-gram": "- They can be motile or nonmotile",
 "mutans-anaerobiose": "- It builds plaque on enamel",
 "aa-colonia": "- The colonies come from culture of dental plaque",
 "tgi-fonte": "- Gut bacteria are the leading cause of endogenous infection",
 "fezes-peso": "- Gut bacteria form a large share of fecal mass",
 "agcc-genes": "- They also influence immunity and metabolism",
 "firmicutes-filo": "- Mycoplasma lacks a cell wall",
 "proteobacteria-filo": "- Many free-living species are harmless",
 "bacteroidetes-filo": "- In dysbiosis Bacteroides can cause infections and IBD",
 "dieta-modula": "- Diet changes the dominant phyla",
 "bacteroides-grupos": "- Composition, not phylum alone, decides the effect",
 "ftm-colite": "- It restores a diverse community",
 "ftm-china": "- It was used for severe diarrhea",
 "ftm-einstein": "- It was used for recurrent C. difficile infection",
 "boulardii": "- It is sold as capsules and sachets",
 "conjuntivite": "- Chlamydia trachomatis causes trachoma",
 "tracoma": "- Chlamydia trachomatis is the agent",
 "di-formula": "- N is infecting dose, V virulence, R resistance",
 "fonte-homem": "- Mary Mallon is the classic carrier",
 "antroponose-zoonose": "- Antroponoses include STDs",
 "typhoid-mary": "- She kept transmitting while healthy",
 "aedes-doencas": "- Aedes breeds in standing water",
 "dengue-incidencia": "- It reached rural areas and small cities",
 "contato-direto": "- Mediate contact is indirect through objects or particles",
 "vias-lista": "- Knowing the route guides prevention",
 "transmissao-horizontal": "- Vertical is from parent to offspring",
 "portas-lista": "- Congenital and iatrogenic are special portals",
 "porta-congenita": "- It is also called transplacental",
 "porta-iatrogenica": "- Medical procedures cause it",
 "fonte-via": "- The source is not the same as the usual habitat",
 "infeccao-doenca": "- Infection can be subclinical",
 "incubacao": "- It ends when symptoms begin",
 "transmissibilidade": "- Healthy carriers can transmit",
 "epidemiologia-def": "- John Snow is the pioneer",
 "incidencia-prevalencia": "- Both are morbidity indicators",
 "ld50-pneumo": "- Salmonella typhimurium needs many more cells",
 "hospital-ambiente": "- Patients are often immunocompromised",
}
DUPLICACAO = {
 "pele-generos": "ganho: gêneros da pele; os cards de S. epidermidis e S. aureus cobram frequência e local",
 "vag-estrogenio": "ganho: causa hormonal no recém-nascido; os cards do AnKing e de Döderlein cobram a espécie dominante depois da puberdade",
 "vag-doderlein": "ganho: nome Döderlein e espécie L. acidophilus; o card do AnKing cobra apenas o gênero",
 "anaerobios-obrigatorios": "ganho: transição causal do oxigênio; os cards de sucessão cobram os gêneros de cada fase",
 "probiotico-nec": "ganho: aplicação de probióticos; os cards de NEC cobram a doença e o fator de risco",
 "conjuntivite": "ganho: etiologia bacteriana da conjuntivite; os cards de tracoma e conjuntivite neonatal cobram agentes específicos",
 "oral-bacteroides-gram": "ganho: coloração e metabolismo de Bacteroides; outros cards cobram gêneros orais e flora colônica",
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

NEGRITO = {  # F-20261011-CLAUDE-01: 1–3 trechos de contexto em negrito (padrão AnKing medido)
 "antagonismo": ["resident microbiota"], "uretra-exames": ["urethral microbiota"], "oral-generos": ["predominant"], "esofago": ["esophagus"],
 "anaerobios-obrigatorios": ["facultative bacteria"], "estabilidade-2anos": ["intestinal microbiota"], "tgi-harmonia": ["gut microbiota"],
 "tgi-patogenica": ["gut microbiota"], "tgi-populacao": ["intestinal microbial population"], "funcao-protecao": ["gut microbiota"],
 "funcao-imune": ["gut microbiota"], "funcao-fermentacao": ["Gut bacteria"], "funcao-ph-motilidade": ["microbiota"], "desafios": ["bacterium"],
 "colipase": ["microbiota"], "gluconato-biliares": ["microbiota"], "densidade-numeros": ["small intestine"], "quatrocentas-especies": ["gut"],
 "filos-dominantes": ["phyla"], "quatro-filos": ["fecal microbiota"], "fermentacao-agcc": ["prebiotics"], "prebioticos-exemplos": ["prebiotics"],
 "sucessao-dia1": ["facultative anaerobes"], "sucessao-bifido": ["anaerobes"], "sucessao-1mes": ["one month"], "janela-th": ["immune system"],
 "th-doenca": ["Th2 > Th1", "Th1 > Th2"], "janela-meses": ["immune regulation"], "tres-funcoes": ["gut microbiota"], "disfuncoes-curto": ["dysbiosis"],
 "eixo-intestino-cerebro": ["gut microbiota"], "desequilibrio-fatores": ["gut microbiota"], "tres-desfechos": ["microorganism"], "pele-fungos": ["skin"],
 "tgi-fonte": ["intestinal microbiota"], "agcc-genes": ["Short-chain fatty acids"], "proteobacteria-filo": ["Escherichia"], "dieta-modula": ["gut microbiota"],
 "bacteroides-grupos": ["Bacteroidetes and Firmicutes"], "ftm-china": ["Fecal transplantation"], "obesidade-firmicutes": ["Obese"],
 "ftm-einstein": ["fecal transplant"], "di-formula": ["Infectious disease"], "modo-transmissao": ["prevention"],
}
for _c in CARDS:
    if _c["kind"] == "autoral" and _c["key"] in NEGRITO:
        for _t in NEGRITO[_c["key"]]:
            _parts = re.split(r"(\{\{c\d+::.*?\}\})", _c["text"])
            for _i, _p in enumerate(_parts):
                if not _p.startswith("{{c") and _t in _p:
                    _parts[_i] = _p.replace(_t, f"<b>{_t}</b>", 1); break
            _c["text"] = "".join(_parts)


# ---- revisão Opus (12/10): Extras sem apoio no material ou que repetiam a frente ----
def _cc(key):
    return next(c for c in CARDS if c["key"] == key)
for _k, _x in {
    "filos-dominantes": "- Proteobacteria and Actinobacteria are smaller phyla",
    "quatro-filos": "- Bacteroidetes and Firmicutes are the two dominant phyla",
    "probiotico-transitorio": "- They behave as transient members of the microbiota",
    "estabilidade-2anos": "- Before that the composition shifts with feeding and weaning",
    "tgi-fonte": "- Peritonitis after bowel perforation is an example",
    "ouvido": "- The external auditory canal is lined by skin",
}.items():
    _cc(_k)["extra"] = _x
_cc("bfragilis-abscesso")["extra"] = "- Gram-negative anaerobic bacillus<br>- Abscesses are common in diverticulitis and IBD"
_cc("contato-direto")["text"] = "<b>Direct contact</b> transmission can be immediate, as in STDs, or {{c1::mediate}}, through respiratory droplets at short range"
_cc("contato-direto")["extra"] = "- Indirect transmission uses vehicles such as objects, water and food"
CARDS[:] = [c for c in CARDS if c["key"] != "ftm-einstein"]  # fato histórico isolado, sem mecanismo (Tab recusou); saiu por nebli.retira


# ---- escopo da aula (F-20261012-CLAUDE-01): fundamentos da relação homem-ambiente-microrganismo; exemplos de doenças e vetores,
# tratamentos e epidemiologia de outra UC saem (nebli.retira, lista em retirar-escopo.txt) ----
_RETIRAR = set(open(__import__("pathlib").Path(__file__).with_name("retirar-escopo.txt")).read().split())
CARDS[:] = [c for c in CARDS if c["key"] not in _RETIRAR]

# Revisão pontual Codex 12/10/2026 — evidência em revisao-pontual-claude-2026-10-12
_AJUSTES_CODEX_1210 = {'conjuntiva-esteril': {'fields_override': {'Text': 'The healthy <b>conjunctiva</b> has a {{c1::low}} bacterial '
                                                    'biomass, limited by tears and local defenses',
                                            'Extra': '- Low bacterial abundance does not mean absolute '
                                                     'sterility.<br>- Tears and lysozyme help limit '
                                                     'colonization.'},
                        'motivo': 'Corrige contradição esterilidade/microbiota no slide 8; estudo primário '
                                  'PMC5054734. Divergência com fonte docente registrada.'},
 'vias-inferiores': {'fields_override': {'Text': 'Microbes in healthy <b>lower airways</b> reflect a balance '
                                                 'between immigration and {{c1::elimination}}',
                                         'Extra': '- Healthy lungs can contain low-biomass microbial '
                                                  'communities.<br>- Detection of microbes alone does not '
                                                  'establish infection.'},
                     'motivo': 'Corrige esterilidade absoluta do slide 8; estudo primário Dickson et al. 2015, '
                               'PMC4590020.'},
 'esofago': {'fields_override': {'Text': 'The <b>esophageal microbiota</b> is closely linked to microorganisms '
                                         'from the {{c1::oral cavity}}',
                                 'Extra': '- Swallowed saliva contributes organisms, and bacteria can also '
                                          'associate with the esophageal mucosa.<br>- It is not accurate to '
                                          'describe the healthy esophagus as lacking a microbiota.'},
             'motivo': 'Remove ausência absoluta de microbiota; estudo primário PNAS 2004, PMC384727.',
             'metadata': {'duplicacao_ok': 'A resposta oral cavity também aparece no habitat de Actinomyces, mas '
                                           'aqui se recupera a origem/conexão da microbiota esofágica, relação '
                                           'distinta.'}},
 'pele-oito-horas': {'fields_override': {},
                     'motivo': 'Número específico ou exemplo histórico/anatômico lateral; preservar conceitos de '
                               'recolonização, maturação, imunidade e portador.',
                     'flags': {1: 5}},
 'estabilidade-2anos': {'fields_override': {},
                        'motivo': 'Número específico ou exemplo histórico/anatômico lateral; preservar conceitos '
                                  'de recolonização, maturação, imunidade e portador.',
                        'flags': {1: 5}},
 'intestino-orgao-imune': {'fields_override': {},
                           'motivo': 'Número específico ou exemplo histórico/anatômico lateral; preservar '
                                     'conceitos de recolonização, maturação, imunidade e portador.',
                           'flags': {1: 5}},
 'typhoid-mary': {'fields_override': {},
                  'motivo': 'Número específico ou exemplo histórico/anatômico lateral; preservar conceitos de '
                            'recolonização, maturação, imunidade e portador.',
                  'flags': {1: 5}},
 'typhi-vesicula': {'fields_override': {},
                    'motivo': 'Número específico ou exemplo histórico/anatômico lateral; preservar conceitos de '
                              'recolonização, maturação, imunidade e portador.',
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
