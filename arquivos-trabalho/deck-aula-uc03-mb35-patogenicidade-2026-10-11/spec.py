# Especificação curada — Patogenicidade bacteriana (UC03 P2, Microbiologia; Profa. Carla Taddei, 41 lâminas de 2026 + lâminas I–III e transcrição da Profa. Elisabete Vicente, ICB-USP).
# Ordem = lâminas de 2026; itens que só estão nas lâminas da turma ou na transcrição ficam ancorados na lâmina de 2026 do mesmo assunto.
import json, re, urllib.request
RUN_ID = "uc03-mb35-20261011a"
SHORT = "mb35"
LESSON = "2026-uc03-microbiologia-35-patogenicidade-bacteriana"
DECK = "NEBLI::UC03::P2::Microbiologia::Patogenicidade bacteriana"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261011-CLAUDE-03) + plano vigente, 11/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, ~45 consultas), cópias NEBLI vivas de Morfologia, Fisiologia bacteriana, "
         "Controle microbiológico e Estrutura do estômago conferidas (compartilhados), 11/10: ")
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


A_, B_, C_, D_, E_, F_ = ("A-conceitos", "B-adesao-e-invasao", "C-toxinas", "D-enzimas-e-evasao", "E-ferro-biofilme-quorum", "F-exemplos")
ESP = [1500571366378, 1500571132898]
CARDS = [
 # ---------- A. Conceitos (lâminas 2–10) ----------
 au("infeccao-def", "Infection is the contamination, penetration and {{c1::multiplication}} of a pathogen in the body", Z, A_,
    "Infecção", "2; turma I p.3", "central", "AnKing não define infecção.", [1500571366378, 1500571132898], "Azul: lâmina 2.",
    extra="- Disease is the tissue damage that impairs the functions of the host"),
 au("patogenicidade-virulencia", "{{c1::Pathogenicity}} is the capacity of a bacterium to cause infection, whereas {{c1::virulence}} is the quantitative measure of its ability to cause disease", V, A_,
    "Patogenicidade × virulência", "5", "central", "AnKing cobre fatores de virulência isolados.", [1484872713454, 1484872744972], "Verde: lâmina 5.",
    extra="- Virulent and opportunistic bacteria differ in how readily they cause disease"),
 au("koch", "Koch's postulates require isolating the suspected pathogen, growing it in {{c1::pure culture}} and reproducing the disease in a healthy animal", Z, A_,
    "Postulados de Koch", "5; turma I p.2", "central", "AnKing não traz os postulados.", [1500571366378, 1484872713454], "Azul: lâmina 5, turma I.",
    extra="- The same pathogen must then be re-isolated from the sick animal"),
 au("ld50", "The LD50 is the dose of bacteria that kills {{c1::50%}} of the test animals and estimates virulence", Z, A_,
    "LD50", "5; turma I p.6", "central", "sem card nos acervos.", [1500571366378, 1484872713454], "Azul: turma I.",
    extra="- Streptococcus pneumoniae needs far fewer cells than Salmonella typhi to reach the LD50"),
 au("oportunista", "Opportunistic pathogens, such as Pseudomonas, cause disease mainly in {{c1::debilitated or immunosuppressed}} hosts", Z, A_,
    "Patógeno oportunista", "5; aula", "central", "AnKing trata de organismos específicos.", [1484872713454, 1500571132898], "Azul: lâmina 5 e transcrição.",
    extra="- Primary pathogens such as Mycobacterium tuberculosis cause disease whenever they are found"),
 au("ecoli-patogenica", "A commensal species such as E. coli becomes pathogenic by acquiring {{c1::virulence}} genes from a bacteriophage or plasmid", V, A_,
    "Cepa patogênica adquire genes de virulência", "5; aula", "central", "AnKing não une o conceito.", [1510188828704, 1510189138014], "Verde: transcrição.",
    extra="- A species is therefore not simply pathogenic or non-pathogenic"),
 au("fases-infeccao", "The phases of an infection are incubation, prodromal, {{c1::acute}} disease and convalescence", Z, A_,
    "Fases do processo infeccioso", "7", "central", "sem card nos acervos.", [1500571366378, 1484872713454], "Azul: lâmina 7.",
    extra="- Incubation runs from exposure to the first symptoms"),
 au("prodromica", "The prodromal phase brings nonspecific symptoms such as prostration, {{c1::low fever}}, nausea and body aches", R, A_,
    "Fase prodrômica", "7", "lateral", "sem card nos acervos.", [1500571366378, 1484872713454], "Rosa: lâmina 7.",
    extra="- Specific symptoms appear in the acute phase"),
 au("portas-entrada", "Pathogens enter through mucous membranes, the skin and the {{c1::parenteral}} route", Z, A_,
    "Portas de entrada", "9, 10", "central", "sem card nos acervos.", [1500571366378, 1484872713454], "Azul: lâminas 9 e 10.",
    extra="- Mucosae include the respiratory, gastrointestinal and genitourinary tracts and the conjunctiva"),
 au("transferrina", "Transferrin limits the free {{c1::iron}} available to bacteria in blood and tissues", Z, A_,
    "Defesa do hospedeiro: transferrina", "3", "central", "sem card nos acervos.", [1500571366378, 1484872713454], "Azul: tabela da lâmina 3.",
    extra="- Pathogens counter this with siderophores"),
 au("nutrientes-patogeno", "Pathogens such as Salmonella, unable to compete for luminal nutrients with the microbiota, invade host tissues to obtain {{c1::nutrients}}", R, A_,
    "Simbionte × patógeno", "6", "lateral", "sem card nos acervos.", [1500571366378, 1484872713454], "Rosa: figura da lâmina 6.",
    extra="- Symbionts such as Bacteroides use dietary polysaccharides"),
 au("fatores-virulencia", "Virulence factors are bacterial structures and metabolites used for adhesion, invasion, {{c1::immune evasion}} and toxin production", V, A_,
    "Fatores de virulência", "11, 12", "central", "AnKing cobre fatores isolados.", [1484872713454, 1500571366378], "Verde: lâminas 11–12.",
    extra="- They are also called the weapons of the bacterium"),
 au("antigenos", "Bacterial antigens include LPS, capsule, flagella, pili and {{c1::secreted proteins}}", R, A_,
    "Antígenos bacterianos", "13, 14", "lateral", "sem card nos acervos.", [1500571132898, 1500571366378], "Rosa: lâminas 13 e 14.",
    extra="- Toxins are also antigens"),
 au("etapas-infeccao", "After adhesion a bacterium must {{c1::colonize}} the site by dividing and forming a colony before it can disseminate", Z, A_,
    "Adesão, colonização e disseminação", "10; turma I p.8", "central", "sem card nos acervos.", [1500571366378, 1484872713454], "Azul: turma I.",
    extra="- Dissemination occurs through the blood or lymph, causing bacteremia or septicemia"),
 # ---------- B. Adesão e invasão (lâminas 15–23) ----------
 au("adesinas", "Adhesins are bacterial surface molecules, mostly glycoproteins or lipoproteins, that bind specific host {{c1::receptors}}", V, B_,
    "Adesinas", "15, 16", "central", "AnKing não define adesina.", [1500405708411, 1510190520330], "Verde: lâmina 15.",
    extra="- Pili, fimbriae and non-fimbrial adhesins all work this way"),
 au("adesinas-tipos", "Adhesins can be fimbrial (pili) or {{c1::non-fimbrial}} (globular surface proteins)", Z, B_,
    "Adesinas fimbriais e não fimbriais", "15, 21; aula", "central", "sem card nos acervos.", [1500405708411, 1510190520330], "Azul: lâminas 15 e 21 e transcrição.",
    extra="- Non-fimbrial examples include Opa, FHA of Bordetella pertussis and MSCRAMMs of Gram-positive cells"),
 au("pili-flagelo", "Pili mediate adhesion, whereas flagella give motility and are made of the protein {{c1::flagellin}}", Z, B_,
    "Pili × flagelos", "14; turma I p.12", "central", "sem card nos acervos.", [1500405708411, 1510190520330], "Azul: turma I.",
    extra="- Sex pili transfer DNA in conjugation"),
 ak("pili-neisseria", 1500405708411, Z, B_, "Pili de N. gonorrhoeae e variação antigênica", "16; turma I p.19", "Azul: exemplo de pili na turma I."),
 au("opa", "The Opa (opacity-associated) protein of Neisseria gonorrhoeae is a non-fimbrial adhesin that binds receptors on the {{c1::epithelium}}", Z, B_,
    "Proteína Opa", "21; turma I p.20", "central", "AnKing não traz Opa.", [1500405708411, 1492873583182], "Azul: turma I.",
    extra="- This species also uses pili for adhesion"),
 au("strepto-adesao", "In Streptococcus pyogenes, M and F proteins associated with {{c1::lipoteichoic acid}} fibrils mediate adhesion to the respiratory mucosa", Z, B_,
    "Adesão de S. pyogenes", "16; turma I p.13", "central", "sem card nos acervos.", [1484704852145, 1475376417766], "Azul: turma I.",
    extra="- The typical disease is pharyngitis"),
 ak("upec-pili", 1510190520330, Z, B_, "E. coli uropatogênica adere por fímbrias tipo I e pili P", "16; turma I p.89", "Azul: turma I, resumo de E. coli."),
 ak("epec-sem-toxina", 1510188828704, V, B_, "EPEC não produz toxina e adere ao epitélio", "16; turma I p.17", "Verde: exemplo central de adesão."),
 au("epec-adesao", "EPEC first adheres weakly through the plasmid-encoded {{c1::BFP}} fimbria and then intimately through intimin", Z, B_,
    "EPEC: adesão fraca e íntima", "16; turma I p.17", "central", "AnKing não cobre as duas fases.", [1510188828704, 1510189838380], "Azul: turma I.",
    extra="- Intimin is encoded by the chromosomal gene eae"),
 au("epec-tir", "The EPEC intimin binds the translocated receptor {{c1::Tir}}, which the bacterium itself injects into the host cell", Z, B_,
    "Intimina e Tir", "16, 17; turma I p.17", "central", "sem card nos acervos.", [1510188828704, 1510189838380], "Azul: turma I.",
    extra="- Tir is delivered by the type III secretion system"),
 au("lesao-ae", "EPEC causes {{c1::attaching and effacing}} lesions, with loss of microvilli and pedestal formation", Z, B_,
    "Lesão A/E", "17; turma II p.12", "central", "sem card nos acervos.", [1510188828704, 1510189838380], "Azul: figura da lâmina 17.",
    extra="- The pedestal forms beneath the adherent bacterium"),
 au("epec-crianca", "EPEC is the most frequent cause of diarrhea in infants up to about {{c1::6 months}} in Brazil", R, B_,
    "EPEC e diarreia infantil", "16; turma I p.18", "lateral", "sem card nos acervos.", [1510188828704, 1510189838380], "Rosa: turma I.",
    extra="- Only certain serotypes are associated with disease, such as O111:H-"),
 au("t3ss", "A type III secretion system injects effector proteins directly into the host cell through a needle-like {{c1::syringe}}", V, B_,
    "Sistema de secreção tipo III", "18, 22", "central", "AnKing cita o T3SS em exemplos, não a estrutura.", [1510104324862, 1510187242637], "Verde: lâmina 18.",
    extra="- The syringe forms pores in the host membrane with pore-forming proteins secreted by the system itself"),
 au("t3ss-flagelo", "The type III secretion system has more than 20 highly conserved genes, similar to those of the {{c1::flagellum}}", Z, B_,
    "T3SS é semelhante ao flagelo", "18", "central", "sem card nos acervos.", [1510104324862, 1510187242637], "Azul: lâmina 18.",
    extra="- Salmonella has two rings and Shigella a bulb and neck"),
 ak("t3ss-salmonella", 1510104324862, Z, B_, "Salmonella usa o sistema de secreção tipo III", "18", "Azul: lâmina 18."),
 ak("t3ss-shigella", 1510187242637, Z, B_, "Shigella secreta efetores pelo sistema tipo III", "18, 19", "Azul: lâmina 18 e 19."),
 au("secrecao-sete", "Seven bacterial secretion systems are known, from single-protein pores to complexes of more than {{c1::20}} proteins", R, B_,
    "Sete sistemas de secreção", "23", "lateral", "sem card nos acervos.", [1510104324862, 1510187242637], "Rosa: lâmina 23.",
    extra="- They move proteins across the cytoplasmic and outer membranes"),
 au("invasao-disenteria", "Shigella, Salmonella and enteroinvasive E. coli (EIEC) invade cells and cause {{c1::bacillary dysentery}}", Z, B_,
    "Bactérias invasoras e disenteria", "19; turma I p.64", "central", "AnKing cobre Shigella isolada.", [1510105444986, 1591903555024], "Azul: turma I.",
    extra="- Dysentery is diarrhea with mucus and blood and abdominal pain"),
 au("shigella-celulaM", "Shigella crosses the intestinal epithelium through {{c1::M cells}} and is taken up by macrophages", Z, B_,
    "Shigella entra por células M", "19, 20, 40", "central", "sem card nos acervos.", [1510105444986, 1510187242637], "Azul: lâminas 19, 20 e 40.",
    extra="- IpaB/C/D/A mediate entry and macrophage cell death"),
 ak("shigella-actina", 1510105444986, V, B_, "Shigella se espalha usando filamentos de actina", "20", "Verde: lâmina 20."),
 ak("eiec-shigella", 1591903555024, Z, B_, "EIEC lembra Shigella clinicamente", "19; turma I p.64", "Azul: turma I."),
 # ---------- C. Toxinas (lâminas 24–29) ----------
 au("toxinas-def", "Toxins are soluble substances that alter the normal metabolism of host cells, causing {{c1::deleterious}} effects", Z, C_,
    "Toxinas", "24", "central", "sem card nos acervos.", [1500571366378, 1500571132898], "Azul: lâmina 24.",
    extra="- They are divided into exotoxins and endotoxins"),
 ak("exotoxinas-proteinas", 1500571366378, V, C_, "Exotoxinas são proteínas secretadas", "24, 27", "Verde: lâmina 24."),
 ak("endotoxina-membrana", 1500571132898, V, C_, "Endotoxina é componente da membrana de Gram-negativas", "24, 26", "Verde: lâmina 24, HY 1."),
 ak("endotoxina-morte", 1500571354019, Z, C_, "Endotoxina é liberada quando a bactéria morre", "24", "Azul: lâmina 24."),
 ak("endotoxina-lps", 1500571400832, Z, C_, "Endotoxinas são lipopolissacarídeos", "24, 28", "Azul: lâmina 28."),
 sh(1791163032499, "azul", C_, "O lipídeo A do LPS é o componente tóxico", 26, "Azul: lâmina 26, card da Morfologia."),
 au("exotoxina-propriedades", "Exotoxins are relatively unstable, highly immunogenic and highly toxic, and usually do not cause {{c1::fever}}", V, C_,
    "Propriedades das exotoxinas", "24, 27", "central", "AnKing cobre definições separadas.", [1500571366378, 1500571132898], "Verde: lâminas 24 e 27.",
    extra="- They are produced by Gram-positive and Gram-negative bacteria"),
 au("endotoxina-propriedades", "Endotoxins are relatively stable, weakly immunogenic and moderately toxic, and usually cause {{c1::fever}}", V, C_,
    "Propriedades das endotoxinas", "24, 28", "central", "AnKing cobre definições separadas.", [1500571366378, 1500571132898], "Verde: lâminas 24 e 28.",
    extra="- They cannot be converted into toxoids"),
 au("genes-toxinas", "Exotoxin genes are often extrachromosomal, whereas endotoxin synthesis is directed by {{c1::chromosomal}} genes", Z, C_,
    "Genes de exo e endotoxinas", "27, 28", "central", "AnKing cita exotoxinas em plasmídeos e fagos, não o contraste.", [1500581524674, 1500571132898], "Azul: lâminas 27–28.",
    extra="- Plasmids and phages carry most exotoxin genes"),
 ak("toxoide", 1500581215531, Z, C_, "Toxoide é exotoxina inativada usada em vacina", "28", "Azul: lâmina 28."),
 au("lps-efeitos", "Endotoxin effects include fever, leukopenia, hypoglycemia and {{c1::hypotension}}", V, C_,
    "Efeitos do LPS", "26, 29; turma I p.34", "central", "AnKing cobre DIC e citocinas separadamente.", [1474059980809, 1500572167638], "Verde: lâmina 26.",
    extra="- Disseminated intravascular coagulation (DIC) can follow"),
 ak("lps-cid", 1474059980809, Z, C_, "CID na sepse por Gram-negativas", "26; turma I p.34", "Azul: efeito do LPS na turma I."),
 sh(1791014719025, "azul", C_, "LPS ativa macrófagos por CD14 e TLR4", 29, "Azul: lâmina 29, card da Secreção gástrica."),
 ak("lps-citocinas", 1500572167638, Z, C_, "LPS libera IL-1, IL-6, TNF-α e NO", "29", "Azul: lâmina 29, colapso cardiovascular e choque."),
 au("lps-gram", "LPS from Enterobacteriaceae, Neisseria and Bordetella pertussis causes cytokine release, cardiovascular collapse and {{c1::shock}}", Z, C_,
    "LPS e choque", "29", "central", "sem card nos acervos.", [1500572167638, 1474059980809], "Azul: lâmina 29.",
    extra="- Peptidoglycan of Gram-positive bacteria has similar but weaker effects"),
 au("ab-toxina", "In A–B exotoxins the B subunit binds the host receptor and the A subunit has the {{c1::enzymatic}} toxic activity", Z, C_,
    "Toxinas A–B", "24; monitoria", "prova", "AnKing não cobre o esquema A–B.", [1500571366378, 1510190230312], "Azul: monitoria P2.",
    extra="- Other exotoxins form pores or act as superantigens"),
 ak("superantigeno", 1500581596511, Z, C_, "Superantígenos ativam CD4+ de forma inespecífica", "24; monitoria", "Azul: monitoria P2."),
 au("colera", "Cholera toxin {{c1::ADP-ribosylates}} the G protein, raising cAMP and causing intense watery diarrhea", V, C_,
    "Enterotoxina colérica", "25", "central", "AnKing cobre só a LT da ETEC.", [1510190230312, 1482115609366], "Verde: lâmina 25.",
    extra="- Vibrio cholerae acts on the epithelial cells of the small intestine"),
 ak("etec-lt", 1510190230312, Z, C_, "LT da ETEC aumenta cAMP", "25; turma I p.36", "Azul: exemplo da turma I."),
 ak("etec-viajante", 1510189838380, Z, C_, "ETEC causa diarreia aquosa do viajante", "25; turma I p.36", "Azul: turma I."),
 au("etec-toxinas", "ETEC produces plasmid-encoded enterotoxins, the heat-labile LT and the heat-{{c1::stable}} ST", Z, C_,
    "Toxinas da ETEC", "25; turma I p.36", "central", "AnKing cobre só LT.", [1510190230312, 1510189838380], "Azul: turma I.",
    extra="- ETEC is not invasive, so stools have no leukocytes"),
 ak("ehec-disenteria", 1510189138014, Z, C_, "EHEC causa disenteria", "25; turma I p.38", "Azul: turma I."),
 ak("ehec-vero", 1473986334978, Z, C_, "Toxina Vero da EHEC lesa o endotélio", "25; turma I p.38", "Azul: turma I."),
 au("ehec-stx", "EHEC causes intimate adhesion like EPEC and produces a Shiga-like toxin also called {{c1::Vero}} toxin", Z, C_,
    "EHEC: adesão íntima e toxina Shiga-like", "25; turma I p.38", "central", "AnKing cobre a toxina, não a adesão.", [1473986334978, 1510189138014], "Azul: turma I.",
    extra="- Hemolytic uremic syndrome is the feared complication"),
 au("eritrogenica", "The erythrogenic toxin of Streptococcus pyogenes injures capillaries under the skin and produces a(n) {{c1::rash}}", Z, C_,
    "Toxina eritrogênica", "25", "central", "AnKing traz a escarlatina mas não o mecanismo.", [1484703771544, 1484872061892], "Azul: lâmina 25.",
    extra="- It is associated with scarlet fever"),
 ak("estafilo-enterotoxina", 1402456236692, Z, C_, "Enterotoxinas pré-formadas do S. aureus", "25", "Azul: lâmina 25."),
 ak("tetano-toxina", 1402526056674, V, C_, "Tetanospasmina causa o tétano", "35; turma I p.39", "Verde: turma I e transcrição."),
 ak("tetano-espastica", 1506125081830, V, C_, "Tétano causa paralisia espástica", "35; turma I p.46", "Verde: turma I."),
 ak("tetano-snare", 1506125601303, Z, C_, "Tetanospasmina cliva proteínas SNARE", "35; turma I p.42", "Azul: turma I."),
 ak("tetano-glicina", 1506125720122, Z, C_, "Tetanospasmina bloqueia a liberação de GABA e glicina", "35; turma I p.42", "Azul: turma I."),
 au("tetano-formas", "Generalized tetanus presents with a sardonic smile and an arched (opisthotonic) posture, whereas neonatal tetanus begins with {{c1::difficulty sucking}}", R, C_,
    "Formas clínicas do tétano", "35; turma I p.43", "lateral", "sem card nos acervos.", [1402526056674, 1506125081830], "Rosa: turma I.",
    extra="- Localized tetanus causes painful spasms near the wound"),
 au("botulinica", "Botulinum toxin blocks the release of {{c1::acetylcholine}} at neuromuscular junctions, causing flaccid paralysis", V, C_,
    "Toxina botulínica", "35; turma I p.45", "central", "AnKing não traz o mecanismo.", [1506125081830, 1402526056674], "Verde: turma I.",
    extra="- Tetanus toxin blocks inhibitory glycine and causes spastic paralysis"),
 au("botox", "Purified botulinum toxin type A is used therapeutically for conditions such as {{c1::dystonia}}", R, C_,
    "Uso terapêutico da toxina botulínica", "35; turma I p.49", "lateral", "sem card nos acervos.", [1506125081830, 1402526056674], "Rosa: turma I.",
    extra="- The therapeutic strain is Hall, from Clostridium botulinum"),
 au("difteria-toxina", "Diphtheria toxin inactivates elongation factor {{c1::eEF-2}}, blocking protein synthesis of host cells", V, C_,
    "Toxina diftérica", "35; turma I p.58", "central", "AnKing cita eEF-2 só na tradução.", [1468090131838, 1506188909667], "Verde: turma I.",
    extra="- It causes a pseudomembrane in the throat"),
 ak("perfringens-alfa", 1500580593418, V, C_, "Toxina alfa do C. perfringens degrada fosfolipídeos", "35; turma I p.51", "Verde: turma I, HY 1."),
 ak("perfringens-lecitinase", 1506185728358, Z, C_, "Toxina alfa é uma fosfolipase (lecitinase)", "35; turma I p.51", "Azul: turma I."),
 au("gangrena-gasosa", "Gas gangrene caused by Clostridium perfringens can be treated with a {{c1::hyperbaric}} chamber", R, C_,
    "Gangrena gasosa e câmara hiperbárica", "35; turma I p.53", "lateral", "sem card nos acervos.", [1500580593418, 1506185728358], "Rosa: turma I.",
    extra="- The bacterium is an obligate anaerobe"),
 ak("cdiff-toxinas", 1506180067784, V, C_, "C. difficile produz as toxinas A e B", "35; turma I p.54", "Verde: turma I."),
 ak("cdiff-toxinab", 1506180588008, Z, C_, "Toxina B despolimeriza actina", "35; turma I p.54", "Azul: turma I."),
 au("cdiff-colite", "Antibiotic therapy can select Clostridioides difficile, causing pseudomembranous {{c1::colitis}}", V, C_,
    "Colite pseudomembranosa", "35; turma I p.54", "central", "AnKing cobre toxinas e IBP.", [1506180067784, 1461624994016], "Verde: turma I.",
    extra="- Colitis is inflammation of the large intestine"),
 # ---------- D. Enzimas e evasão (lâminas 30–32) ----------
 ak("hialuronidase", 1503087501301, Z, D_, "Hialuronidase do S. pyogenes", "30; turma I p.62", "Azul: lâmina 30."),
 ak("estreptoquinase", 1484703690599, Z, D_, "Estreptoquinase é fator de virulência do GAS", "30; turma I p.62", "Azul: lâmina 30."),
 ak("coagulase", 1484871806725, Z, D_, "S. aureus é o único estafilococo coagulase-positivo", "30; turma I p.62", "Azul: lâmina 30."),
 ak("leucocidina", 1667231457578, R, D_, "Leucocidina de Panton-Valentine", "30; turma I p.62", "Rosa: lâmina 30, detalhe."),
 au("enzimas-tecido", "Tissue-degrading enzymes of bacteria include lecithinase, collagenase, coagulase, hyaluronidase and {{c1::streptokinase}}", Z, D_,
    "Enzimas que degradam tecidos", "30", "central", "AnKing cobre enzimas separadas.", [1503087501301, 1484703690599], "Azul: lâmina 30.",
    extra="- They help bacteria spread, as in Staphylococcus aureus and Streptococcus pyogenes"),
 ak("iga-protease", 1402675655473, V, D_, "IgA protease cliva IgA secretora de Neisseria", "30, 31", "Verde: lâminas 30–31, HY 1."),
 au("iga-especies", "IgA1 protease is a virulence factor of N. gonorrhoeae, N. meningitidis, H. influenzae and {{c1::S. pneumoniae}}", Z, D_,
    "IgA1 protease em quatro espécies", "30, 31", "central", "AnKing cobre Neisseria e pneumococo separadamente.", [1402675655473, 1485804696636], "Azul: lâmina 31.",
    extra="- It degrades secretory IgA on mucosal surfaces"),
 au("c5a-peptidase", "C5a peptidase interferes with complement signaling by cleaving {{c1::C5a}}", Z, D_,
    "C5a peptidase", "31", "central", "sem card nos acervos.", [1402675655473, 1485804696636], "Azul: lâmina 31 e 40.",
    extra="- Some bacteria also acquire host components to coat their surface"),
 au("variacao-antigenica", "Antigenic variation changes the expression of virulence {{c1::genes}}, as in Salmonella and the pili of Neisseria gonorrhoeae", Z, D_,
    "Variação antigênica", "31", "central", "AnKing cobre os pili da Neisseria.", [1500405708411, 1402675655473], "Azul: lâmina 31.",
    extra="- It helps the bacterium escape the immune response"),
 au("salmonella-fase", "Salmonella evades the immune response by switching between flagellin {{c1::H1 and H2}} through a transposable insertion sequence", Z, D_,
    "Variação de fase da Salmonella", "31; turma II p.29", "central", "sem card nos acervos.", [1500405708411, 1402675655473], "Azul: turma II.",
    extra="- Phase variation changes the flagellar antigen"),
 sh(1791163040622, "verde", D_, "Cápsula inibe a fagocitose", 32, "Verde: lâmina 32, card da Morfologia."),
 au("capsula-repulsao", "The capsule acts against phagocytosis by electrochemical repulsion and reduces {{c1::complement}} activation", V, D_,
    "Ação antifagocítica da cápsula", "32", "central", "AnKing cobre a cápsula em organismos específicos.", [1503186270564, 1485804778061], "Verde: lâmina 32.",
    extra="- Capsules are present in Gram-positive and Gram-negative bacteria"),
 au("pneumococo-capsula", "Encapsulated (smooth) strains of Streptococcus pneumoniae are pathogenic, whereas {{c1::unencapsulated}} (rough) strains are not", V, D_,
    "Pneumococo capsulado é patogênico", "32; turma I p.68", "central", "AnKing cobre pacientes com asplenia.", [1503186270564, 1485804778061], "Verde: turma I.",
    extra="- Untreated bacteremic pneumonia has about 30% mortality and treated about 10%"),
 au("capsula-neisseria", "The capsule of Neisseria meningitidis confers adhesion and resistance to {{c1::phagocytosis}}", Z, D_,
    "Cápsula de N. meningitidis", "32; turma I p.70", "central", "sem card nos acervos.", [1503186270564, 1485804778061], "Azul: turma I.",
    extra="- Klebsiella pneumoniae and Haemophilus influenzae also have capsules"),
 ak("proteina-a", 1484872713454, Z, D_, "Proteína A é fator de virulência do S. aureus", "32; turma I p.71", "Azul: turma I."),
 ak("proteina-a-mecanismo", 1484872744972, V, D_, "Proteína A liga a região Fc da IgG", "32; turma I p.71", "Verde: turma I."),
 au("proteina-m", "The M protein of Streptococcus pyogenes, with more than 100 types, promotes evasion of phagocytosis and explains {{c1::recurrent}} pharyngitis", Z, D_,
    "Proteína M", "32; turma I p.73", "central", "AnKing cobre a febre reumática e a GNPE.", [1484704852145, 1475376417766], "Azul: turma I.",
    extra="- The M protein is also a target of cross-reactive antibodies in rheumatic fever"),
 ak("febre-reumatica", 1484704852145, Z, D_, "Proteína M e reação cruzada com miosina cardíaca", "32; turma I p.91", "Azul: turma I, sequela do S. pyogenes."),
 ak("gnpe-proteina-m", 1475376417766, R, D_, "GNPE por cepas nefritogênicas com proteína M", "32; turma I p.91", "Rosa: turma I, clínica lateral."),
 au("tb-fagossomo", "Mycobacterium tuberculosis survives inside macrophages by blocking {{c1::phagosome–lysosome}} fusion", V, D_,
    "TB bloqueia a fusão fagossomo-lisossomo", "32; turma I p.77", "central", "AnKing não traz o mecanismo de evasão.", [1485804778061, 1503186270564], "Verde: turma I.",
    extra="- It also neutralizes reactive oxygen species"),
 au("tb-manlam", "The cell wall lipoarabinomannan (ManLAM) of M. tuberculosis interferes with {{c1::phagosome}} maturation", R, D_,
    "ManLAM", "32; turma I p.77", "lateral", "sem card nos acervos.", [1485804778061, 1503186270564], "Rosa: turma I.",
    extra="- The mycolic acid layer makes the wall hydrophobic and waxy"),
 au("tb-tratamento", "The basic Brazilian tuberculosis regimen starts with rifampicin, isoniazid, pyrazinamide and {{c1::ethambutol}}", R, D_,
    "Esquema básico da tuberculose", "32; turma I p.84", "lateral", "sem card nos acervos.", [1485804778061, 1503186270564], "Rosa: turma I.",
    extra="- The maintenance phase keeps rifampicin and isoniazid"),
 au("tb-formas", "Skeletal tuberculosis (Pott disease) is {{c1::not}} contagious because bacilli are not released into the air", R, D_,
    "TB óssea não é contagiosa", "32; turma I p.83", "lateral", "sem card nos acervos.", [1485804778061, 1503186270564], "Rosa: turma I.",
    extra="- Active pulmonary tuberculosis is the most contagious form"),
 au("hpylori-vaca", "Helicobacter pylori VacA induces {{c1::vacuoles}} in gastric epithelial cells, one way the bacterium evades host defenses", Z, D_,
    "Vacúolos de H. pylori", "32; turma I p.67", "central", "AnKing cobre urease e CagA.", [1482275983368, 1482275947242], "Azul: turma I.",
    extra="- The Cag pathogenicity island is the other main virulence factor"),
 sh(1790980015534, "azul", D_, "H. pylori alcaliniza o meio com urease", 32, "Azul: card da Estrutura do estômago."),
 au("salmonella-spi1", "Pathogenicity island SPI-1 of Salmonella encodes a type III secretion system used for {{c1::invasion}} of host cells", Z, D_,
    "Ilha de patogenicidade SPI-1", "18; turma III p.22", "central", "sem card nos acervos.", [1510104324862, 1510187242637], "Azul: turma III.",
    extra="- It carries a cluster of virulence genes"),
 au("antigeno-o", "Alterations in the O antigen prevent formation of the membrane attack complex and promote {{c1::serum}} resistance", Z, D_,
    "Antígeno O e resistência ao soro", "40", "central", "sem card nos acervos.", [1500571132898, 1474059980809], "Azul: tabela da lâmina 40.",
    extra="- Capsules and C5a peptidase also interfere with complement"),
 au("proteinas-toxicas", "Toxic proteins kill phagocytes and reduce the strength of the oxidative {{c1::burst}}", R, D_,
    "Proteínas tóxicas contra fagócitos", "40", "lateral", "sem card nos acervos.", [1500571132898, 1474059980809], "Rosa: tabela da lâmina 40.",
    extra="- Yersinia Yops are an example"),
 au("celulas-m", "Some bacterial substances bind and favor invasion of {{c1::M cells}}, using them as a portal to deeper tissues", Z, D_,
    "Invasão de células M", "40", "central", "sem card nos acervos.", [1510105444986, 1510187242637], "Azul: tabela da lâmina 40.",
    extra="- Shigella is the example"),
 au("motilidade", "Motility and {{c1::chemotaxis}} help pathogens reach regions of the mucosal surface", R, D_,
    "Motilidade e quimiotaxia", "40", "lateral", "sem card nos acervos.", [1510105444986, 1510187242637], "Rosa: tabela da lâmina 40.",
    extra="- Flagella provide the motility"),
 # ---------- E. Ferro, biofilme e quorum sensing (lâminas 33–38) ----------
 sh(1791647814244, "verde", E_, "Sideróforos capturam o ferro do hospedeiro", 33, "Verde: lâmina 33, card da Fisiologia bacteriana."),
 sh(1791647814120, "azul", E_, "Imunidade nutricional prende o ferro", 33, "Azul: lâmina 33, card da Fisiologia bacteriana."),
 sh(1791647814370, "azul", E_, "Fur reprime sideróforos e toxinas com ferro alto", 33, "Azul: lâmina 33, card da Fisiologia bacteriana."),
 au("biofilme-def", "A biofilm is a community of microcolonies embedded in {{c1::exopolysaccharides}} on biotic or abiotic surfaces", V, E_,
    "Biofilme", "34, 35; turma I p.27", "central", "AnKing cobre biofilme em organismos específicos.", [1503084290841, 1475452940682], "Verde: lâmina 34.",
    extra="- Mature biofilms form mushroom-shaped aggregates with channels"),
 au("biofilme-protecao", "Bacteria in a biofilm are protected from the immune system and from {{c1::antibiotics}}", V, E_,
    "Proteção do biofilme", "34", "central", "AnKing cobre próteses e cateteres.", [1503084290841, 1475452940682], "Verde: lâmina 34.",
    extra="- A biofilm is a constant source of bacteria that cause infections"),
 ak("biofilme-epidermidis", 1503084290841, Z, E_, "S. epidermidis forma biofilme em próteses", "34", "Azul: exemplo de biofilme."),
 au("mutans-placa", "Streptococcus mutans produces extracellular glucans that build the dental plaque {{c1::biofilm}}, favoring caries", Z, E_,
    "S. mutans e a placa dentária", "34; turma I p.28", "central", "sem card nos acervos.", [1503084290841, 1475452940682], "Azul: turma I.",
    extra="- The slimy layer creates an anaerobic environment"),
 au("quorum-def", "Quorum sensing is cell-to-cell communication that depends on {{c1::population density}} and activates or represses many genes", V, E_,
    "Quorum sensing", "36", "central", "sem card nos acervos.", [1503084290841, 1475452940682], "Verde: lâmina 36.",
    extra="- It leads to new phenotypes such as biofilm formation and virulence"),
 au("quorum-gramneg", "In Gram-negative bacteria quorum sensing is mediated by {{c1::acyl homoserine lactones}}", Z, E_,
    "Quorum sensing por AHL", "36", "central", "sem card nos acervos.", [1503084290841, 1475452940682], "Azul: lâmina 36.",
    extra="- AHL binds a receptor that activates transcription of target genes"),
 au("quorum-grampos", "In Gram-positive bacteria quorum sensing is mediated by {{c1::peptides}}", Z, E_,
    "Quorum sensing por peptídeos", "37", "central", "sem card nos acervos.", [1503084290841, 1475452940682], "Azul: lâmina 37.",
    extra="- The AI-2 system works in both Gram-positive and Gram-negative bacteria"),
 au("quorum-ai2", "The AI-2 quorum-sensing system is a furanosyl borate diester used by {{c1::both}} Gram-positive and Gram-negative bacteria", R, E_,
    "Sistema AI-2", "37", "lateral", "sem card nos acervos.", [1503084290841, 1475452940682], "Rosa: lâmina 37.",
    extra="- It allows communication between species"),
 au("quorum-ai3", "The AI-3 system allows communication between bacteria and the {{c1::host}}", R, E_,
    "Sistema AI-3", "38", "lateral", "sem card nos acervos.", [1503084290841, 1475452940682], "Rosa: lâmina 38.",
    extra="- It is linked to host hormones such as epinephrine"),
 # ---------- F. Epidemiologia e E. coli (turma I) ----------
 au("periodo-latente", "The latent period runs from infection until the host is able to {{c1::transmit}} the agent to another host", Z, F_,
    "Período latente", "7; turma I p.85", "central", "sem card nos acervos.", [1500571366378, 1484872713454], "Azul: turma I.",
    extra="- The incubation period covers the multiplication cycle until symptoms appear"),
 au("eaec-daec", "Besides EPEC, ETEC, EHEC and EIEC, E. coli pathotypes include {{c1::enteroaggregative}} (EAEC) and diffusely adherent strains", R, F_,
    "Patotipos de E. coli", "16; turma I p.88", "lateral", "sem card nos acervos.", [1510188828704, 1510189138014], "Rosa: turma I.",
    extra="- Each pathotype combines adhesion, toxin and invasion in a different way"),
 ak("ecoli-itu", 1510188570426, V, F_, "E. coli é a causa mais comum de ITU", "16; turma I p.89", "Verde: turma I, HY 1."),
 au("pielonefrite", "E. coli with P fimbriae adheres to the urinary tract mucosa, and fecal strains reach the upper tract by {{c1::ascending}} from the urethra", Z, F_,
    "ITU por E. coli", "16; turma I p.89", "prova", "AnKing cobre pili P, não a via ascendente.", [1510190520330, 1510188570426], "Azul: prova 2025 P2 1.3.",
    extra="- Siderophores and hemolysin also help uropathogenic strains"),
]

VERSO = {}
DUPLICACAO = {}
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
 "infeccao-def": ["Infection", "pathogen"], "patogenicidade-virulencia": ["bacterium", "ability to cause disease"], "koch": ["Koch's postulates", "healthy animal"],
 "ld50": ["LD50", "virulence"], "oportunista": ["Opportunistic pathogens", "Pseudomonas"], "ecoli-patogenica": ["commensal species", "bacteriophage or plasmid"],
 "fases-infeccao": ["phases of an infection", "convalescence"], "prodromica": ["prodromal phase", "nonspecific symptoms"], "portas-entrada": ["Pathogens", "mucous membranes"],
 "transferrina": ["Transferrin", "free"], "nutrientes-patogeno": ["Salmonella", "luminal nutrients"], "fatores-virulencia": ["Virulence factors", "adhesion"],
 "antigenos": ["Bacterial antigens", "LPS, capsule, flagella, pili"], "etapas-infeccao": ["adhesion", "disseminate"], "adesinas": ["Adhesins", "host"],
 "adesinas-tipos": ["Adhesins", "fimbrial (pili)"], "pili-flagelo": ["Pili", "flagella"], "opa": ["Opa (opacity-associated) protein", "Neisseria gonorrhoeae"],
 "strepto-adesao": ["Streptococcus pyogenes", "M and F proteins"], "epec-adesao": ["EPEC", "intimin"], "epec-tir": ["EPEC intimin", "translocated receptor"],
 "lesao-ae": ["EPEC", "microvilli"], "epec-crianca": ["EPEC", "diarrhea in infants"], "t3ss": ["type III secretion system", "effector proteins"],
 "t3ss-flagelo": ["type III secretion system", "20 highly conserved genes"], "secrecao-sete": ["secretion systems", "single-protein pores"],
 "invasao-disenteria": ["Shigella, Salmonella", "enteroinvasive E. coli (EIEC)"], "shigella-celulaM": ["Shigella", "intestinal epithelium"], "toxinas-def": ["Toxins", "host cells"],
 "exotoxina-propriedades": ["Exotoxins", "unstable, highly immunogenic"], "endotoxina-propriedades": ["Endotoxins", "stable, weakly immunogenic"],
 "genes-toxinas": ["Exotoxin genes", "endotoxin synthesis"], "lps-efeitos": ["Endotoxin effects", "fever, leukopenia"], "lps-gram": ["LPS", "Enterobacteriaceae, Neisseria"],
 "ab-toxina": ["A–B exotoxins", "B subunit"], "colera": ["Cholera toxin", "G protein"], "etec-toxinas": ["ETEC", "plasmid-encoded enterotoxins"], "ehec-stx": ["EHEC", "Shiga-like toxin"],
 "eritrogenica": ["erythrogenic toxin", "Streptococcus pyogenes"], "tetano-formas": ["Generalized tetanus", "neonatal tetanus"], "botulinica": ["Botulinum toxin", "neuromuscular junctions"],
 "botox": ["Purified botulinum toxin type A", "therapeutically"], "difteria-toxina": ["Diphtheria toxin", "protein synthesis"], "gangrena-gasosa": ["Gas gangrene", "Clostridium perfringens"],
 "cdiff-colite": ["Antibiotic therapy", "Clostridioides difficile"], "enzimas-tecido": ["Tissue-degrading enzymes", "lecithinase, collagenase"],
 "iga-especies": ["IgA1 protease", "N. gonorrhoeae, N. meningitidis"], "c5a-peptidase": ["C5a peptidase", "complement signaling"], "variacao-antigenica": ["Antigenic variation", "virulence"],
 "salmonella-fase": ["Salmonella", "insertion sequence"], "capsula-repulsao": ["capsule", "electrochemical repulsion"], "pneumococo-capsula": ["Encapsulated (smooth) strains", "Streptococcus pneumoniae"],
 "capsula-neisseria": ["capsule", "Neisseria meningitidis"], "proteina-m": ["M protein", "Streptococcus pyogenes"], "tb-fagossomo": ["Mycobacterium tuberculosis", "macrophages"],
 "tb-manlam": ["lipoarabinomannan (ManLAM)", "M. tuberculosis"], "tb-tratamento": ["Brazilian tuberculosis regimen", "rifampicin, isoniazid"], "tb-formas": ["Skeletal tuberculosis (Pott disease)", "contagious"],
 "hpylori-vaca": ["Helicobacter pylori VacA", "gastric epithelial cells"], "salmonella-spi1": ["Pathogenicity island SPI-1", "type III secretion system"],
 "antigeno-o": ["O antigen", "membrane attack complex"], "proteinas-toxicas": ["Toxic proteins", "phagocytes"], "celulas-m": ["Some bacterial substances", "deeper tissues"],
 "motilidade": ["Motility", "mucosal surface"], "biofilme-def": ["biofilm", "microcolonies"], "biofilme-protecao": ["Bacteria in a biofilm", "immune system"],
 "mutans-placa": ["Streptococcus mutans", "dental plaque"], "quorum-def": ["Quorum sensing", "activates or represses many genes"], "quorum-gramneg": ["Gram-negative bacteria", "quorum sensing"],
 "quorum-grampos": ["Gram-positive bacteria", "quorum sensing"], "quorum-ai2": ["AI-2 quorum-sensing system", "furanosyl borate diester"], "quorum-ai3": ["AI-3 system", "bacteria"],
 "periodo-latente": ["latent period", "infection"], "eaec-daec": ["E. coli pathotypes", "EPEC, ETEC, EHEC"], "pielonefrite": ["E. coli with P fimbriae", "urinary tract mucosa"],
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


# ---- bandeiras HY (11/10): mecanismo central das lâminas 2026 = verde; exemplo da turma 2020/clínica = lateral ----
def _c(key):
    return next(c for c in CARDS if c["key"] == key)


for _k in ("t3ss-shigella", "toxoide", "lps-citocinas", "superantigeno"):
    _c(_k)["flags"] = {n: V for n in _c(_k)["flags"]}
for _c_ in CARDS:
    if _c_["kind"] == "text" and V not in _c_["flags"].values():
        _c_["clinica_lateral"] = True
# biofilme do S. epidermidis já existe vivo (Morfologia): compartilhar em vez de copiar
_i = next(i for i, c in enumerate(CARDS) if c["key"] == "biofilme-epidermidis")
CARDS[_i] = sh(1791576680215, "azul", CARDS[_i]["bloco"], CARDS[_i]["alvo"], CARDS[_i]["evid"].replace("Slide ", ""), "Azul: exemplo de biofilme, card da Morfologia.")


# ---- lacunas do material de base (monitoria P2 aulas 6 e 8; Trabulsi 17.1, da Profa. Taddei; 17.2–19; provas) ----
import re as _re
_ESP = [1500571366378, 1510104324862]


def _novo(key, text, cor, bloco, alvo, slide, autoria, extra):
    n = sorted({int(x) for x in _re.findall(r"\{\{c(\d+)::", text)})
    CARDS.append(au(key, text, cor, bloco, alvo, slide, autoria,
                    "AnKing sem o conceito no recorte da aula (busca/anking.txt).", _ESP, "Lacuna do material de base.", extra=extra))


_novo("colonizacao-infeccao", "Unlike simple <b>colonization</b>, {{c1::infection}} provokes a response from the <b>host</b>", Z, A_, "Colonização × infecção", "2; monitoria aula 6", "central", "- Colonization can be intracellular, extracellular or both")
_novo("endogena", "An <b>endogenous infection</b> is caused by the patient's own {{c1::microbiota}} reaching a site where it is not controlled", Z, A_, "Infecção endógena", "5; monitoria aula 6; prova 2023", "prova", "- Triggers include broken barriers, antibiotics and immunosuppression<br>- Exogenous infections come from outside the host")
_novo("iceberg", "Most <b>infections</b> stay {{c1::subclinical}}, forming the base of the infection iceberg below clinical disease", R, A_, "Iceberg da infecção", "7; monitoria aula 6", "lateral", "- Tuberculosis is the classic example")
_novo("adesao-expulsao", "<b>Adherence</b> to mucosa lets bacteria resist {{c1::expulsion}} by cilia, secretion flow and peristalsis", V, B_, "Adesão impede a expulsão", "15; Trabulsi 17.1", "central", "- Adherence is a prerequisite for colonization")
_novo("ciliostase", "Some respiratory pathogens overcome <b>mucociliary clearance</b> by causing {{c1::ciliostasis}}", R, A_, "Ciliostase", "3; monitoria aula 6", "lateral", "- Others compete with the resident microbiota")
_novo("mscramm", "<b>MSCRAMMs</b> are Gram-positive adhesins that bind host {{c1::extracellular matrix}} molecules such as collagen and fibronectin", Z, B_, "MSCRAMM", "21; Trabulsi 17.1; prova 2024", "prova", "- Staphylococcus aureus fibronectin-binding proteins are an example")
_novo("teicoico-adesao", "In <b>Gram-positive</b> bacteria, {{c1::lipoteichoic}} acid helps mediate adhesion to epithelium", Z, B_, "Ácido lipoteicoico na adesão", "21; monitoria aula 8", "central", "- It is anchored in the cell membrane and crosses the peptidoglycan")
_novo("intracelular-facultativo", "<b>Salmonella</b>, Shigella and Yersinia are {{c1::facultative}} intracellular bacteria", Z, B_, "Intracelular facultativo × obrigatório", "19; Trabulsi 17.1; monitoria aula 6", "central", "- Obligate intracellular bacteria survive only inside cells")
_novo("induz-fagocitose", "Invasive bacteria make <b>non-phagocytic cells</b> engulf them by rearranging host {{c1::actin}}", V, B_, "Indução de fagocitose em célula não fagocítica", "40; Trabulsi 17.1", "central", "- Epithelial cells cannot take up large particles on their own")
_novo("invasina-yersinia", "<b>Yersinia</b> invasin triggers entry by high-affinity binding to host {{c1::β1 integrins}}", R, B_, "Invasina da Yersinia", "19; Trabulsi 17.1", "lateral", "- Salmonella and Shigella instead signal to remodel the cytoskeleton")
_novo("t2ss", "In the <b>type II secretion system</b>, proteins first cross the inner membrane into the {{c1::periplasm}}", R, B_, "Sistema de secreção tipo II", "23", "lateral", "- About 12–14 proteins form the system")
_novo("lps-estrutura", "<b>LPS</b> is made of lipid A, a conserved core polysaccharide and a variable {{c1::O antigen}}", Z, C_, "Estrutura do LPS", "26; monitoria aula 6", "central", "- Lipid A is the toxic part")
_novo("peptidoglicano-endotoxina", "Gram-positive <b>peptidoglycan</b> causes effects similar to LPS but {{c1::weaker}}", R, C_, "Peptidoglicano com efeito de endotoxina", "26, 29", "lateral", "- Fever and hypotension are the shared effects")
_novo("exotoxina-tipos", "<b>Exotoxins</b> act as A–B toxins, {{c1::pore-forming}} toxins or superantigens", Z, C_, "Três tipos de exotoxina", "24; monitoria aula 6; Trabulsi 17.2", "central", "- Pore-forming toxins lyse the cell membrane")
_novo("genetica-virulencia", "Most <b>virulence genes</b> spread between bacteria by {{c1::horizontal gene transfer}}", V, C_, "Genética da virulência", "27; monitoria aula 6; Trabulsi 18", "central", "- They travel on plasmids, phages, transposons and pathogenicity islands")
_novo("mimetismo", "In <b>molecular mimicry</b>, bacterial antigens resemble {{c1::host}} molecules, so immunity can attack host tissue", Z, D_, "Mimetismo molecular", "31; monitoria aula 6", "central", "- Rheumatic fever after Streptococcus pyogenes is the classic example")
_novo("camuflagem", "Some bacteria hide from <b>immunity</b> by inserting {{c1::host}} components into their own <b>surface</b>", R, D_, "Aquisição de componentes do hospedeiro", "31", "lateral", "- The host does not recognize its own molecules as foreign")
_novo("ld50-curva", "In highly <b>virulent</b> bacteria, the doses that kill 50% and 100% of test animals are {{c1::close}} together", R, A_, "LD50 e LD100 próximas", "5; monitoria aula 8", "lateral", "- Low-virulence bacteria show a wide gap between the two")
_novo("siderofos-tipos", "<b>Enterobactin</b> is a catecholate siderophore, whereas aerobactin is a {{c1::hydroxamate}}", R, E_, "Tipos de sideróforo", "33; Trabulsi 17.1", "lateral", "- Both bind Fe³⁺ with very high affinity")
# AnKing equivalente encontrado na busca (busca/ext.txt): substitui o autoral
CARDS[:] = [c for c in CARDS if c["key"] not in ("intracelular-facultativo", "lps-estrutura")]
CARDS.append(ak("intracelular-facultativo", 1500500080203, V, B_, "Intracelular facultativo × obrigatório", "19; Trabulsi 17.1; monitoria aula 6", "Verde: HY 2; tipos de invasão (monitoria, Trabulsi 17.1)."))
CARDS.append(ak("lps-estrutura", 1500571431321, Z, C_, "Estrutura do LPS", "26; monitoria aula 6", "Azul: estrutura do LPS (monitoria aulas 6 e 8)."))


# ---- pré-gates (11/10): redundâncias, cloze com "ou", Extra dos AnKing sem verso ----
_c("oportunista")["text"] = "<b>Opportunistic pathogens</b>, such as Pseudomonas, cause disease mainly in {{c1::immunosuppressed}} hosts"
_c("ehec-stx")["text"] = "Like EPEC, <b>EHEC</b> attaches by {{c1::intimate adhesion}} (A/E lesions), but it also makes a Shiga-like toxin"
_c("enzimas-tecido")["text"] = "Bacterial <b>lecithinase</b>, collagenase and hyaluronidase favor invasion by {{c1::degrading host tissue}}"
_c("capsula-neisseria")["text"] = "The <b>capsule</b> of Neisseria meningitidis works both as an antiphagocytic factor and as a non-fimbrial {{c1::adhesin}}"
_c("periodo-latente")["duplicacao_ok"] = "ganho: período de transmissibilidade (turma I p. 85), diferente da incubação e da fase prodrômica"
_c("antigenos")["duplicacao_ok"] = "ganho: antígenos bacterianos (lâminas 13–14) como conceito distinto de fator de virulência"
for _k, _x in {
    "intracelular-facultativo": "- Salmonella, Shigella and Yersinia are facultative<br>- Obligate intracellular bacteria (Chlamydia, Rickettsia) cannot live outside cells",
    "shigella-actina": "- Shigella enters through M cells and escapes the macrophage<br>- Actin tails push it into the neighboring enterocyte",
    "exotoxinas-proteinas": "- Exotoxins are unstable, highly antigenic and highly toxic<br>- They can be converted into toxoids",
    "endotoxina-membrana": "- Endotoxin is released when the bacterium lyses",
    "endotoxina-lps": "- Endotoxins are heat-stable and weakly immunogenic",
    "lps-estrutura": "- The core polysaccharide is conserved",
    "toxoide": "- Endotoxins cannot be converted into toxoids",
    "lps-citocinas": "- These cytokines cause fever, hypotension and shock",
    "hialuronidase": "- Hyaluronidase is one of the tissue-degrading enzymes",
    "coagulase": "- Coagulase forms a fibrin coat that protects S. aureus from phagocytosis",
    "tetano-snare": "- Blocking inhibitory neurons causes spastic paralysis",
    "perfringens-lecitinase": "- Lecithinase breaks down cell membranes, causing myonecrosis in gas gangrene",
    "cdiff-toxinas": "- They act after antibiotics disrupt the normal gut microbiota",
    "cdiff-toxinab": "- Toxin A is an enterotoxin; toxin B is a cytotoxin",
}.items():
    _c(_k)["extra_add"] = _x


# ---- revisão final card a card (11/10) ----
_c("pneumococo-capsula")["extra"] = "- The capsule is the main virulence factor of S. pneumoniae"
for _k in ("difteria-toxina", "cdiff-colite"):
    _c(_k)["flags"] = Z if isinstance(_c(_k)["flags"], int) else {n: Z for n in _c(_k)["flags"]}


# ======================================================================================================================
# ---- Revisão Opus (REVISAO-OPUS.md) + aula completa com as 4 lâminas da pasta 35 (F-20261011-CLAUDE-06, 11/10 noite) ----
# Davi: "a aula de patogenicidade envolve os quatro slides que há no drive". Lâminas numeradas em sequência em fontes/slides.pdf:
# 1–41 Taddei (Mecanismos de virulência) · 42–110 cocos Gram+ (staphylo/strepto) · 111–144 bacilos Gram+ · 145–191 bacilos Gram− (Taddei).
# Consequência: tétano, clostrídios, difteria e Listeria TÊM lâmina de 2026 (bacilos Gram+); o "peso de 2025" do Opus (2.1) vale só para
# TB e H. pylori. As decisões do Opus sobre esses exemplos foram reavaliadas com as lâminas novas.
# ======================================================================================================================
G_, H_, I_, J_ = "G-estafilococos", "H-estreptococos", "I-bacilos-gram-positivos", "J-bacilos-gram-negativos"
RETIRADOS_OPUS = {  # chave → motivo (nebli.retira): nota suspensa e fora da aula, comentário preservado
    "tetano-toxina": "nome-tetanospasmina-nao-ensinado", "perfringens-alfa": "duplica-lecitinase", "gangrena-gasosa": "tratamento-fora",
    "cdiff-toxinab": "fora-do-material", "tb-tratamento": "farmacologia-fora", "tb-formas": "lateral-trocado-por-tb-latente",
    "t3ss-salmonella": "redundante-t3ss-shigella", "proteina-a": "redundante-mecanismo", "endotoxina-morte": "redundante-extra",
}
CARDS[:] = [c for c in CARDS if c["key"] not in RETIRADOS_OPUS]


def _cor(key, cor):
    _c(key)["flags"] = {n: cor for n in _c(key)["flags"]}
    if cor == V:
        _c(key).pop("clinica_lateral", None)
    elif _c(key)["kind"] == "text":
        _c(key)["clinica_lateral"] = True  # exemplo/representante repetido: rebaixado pelo Opus


def _ev(key, ev):
    _c(key)["evid"] = "Slide " + ev


# -- cores (Opus 2.1, 2.2, 3; reavaliadas com as lâminas de bacilos Gram+) --
for _k, _x in {"infeccao-def": V, "portas-entrada": V, "fases-infeccao": V, "etapas-infeccao": V, "peptidoglicano-endotoxina": Z,
               "camuflagem": Z, "leucocidina": Z, "opa": R, "salmonella-spi1": R, "proteina-a-mecanismo": Z, "ehec-vero": R, "eaec-daec": R,
               "tetano-espastica": Z, "tetano-glicina": V, "tetano-snare": R, "botulinica": Z, "perfringens-lecitinase": R, "cdiff-toxinas": R,
               "tb-fagossomo": Z, "hpylori-vaca": R}.items():
    _cor(_k, _x)
# -- âncoras: exemplos de bacilos Gram+ vão às lâminas 2026 (Opus 0.1/0.2: a lâmina 35 é a figura do biofilme) --
for _k, _x in {"tetano-espastica": "124; turma I p.46", "tetano-glicina": "124; turma I p.42", "tetano-snare": "124; turma I p.42",
               "tetano-formas": "123; turma I p.43", "botulinica": "128; turma I p.45", "botox": "130; turma I p.49",
               "difteria-toxina": "137; turma I p.58", "perfringens-lecitinase": "118; turma I p.51", "cdiff-toxinas": "132; turma I p.54",
               "cdiff-colite": "132; turma I p.54"}.items():
    _ev(_k, _x)
_c("tetano-formas")["text"] = _c("tetano-formas")["text"]  # mantido: lâmina 123 traz generalizado × localizado
# -- erros científicos (Opus 4) --
_c("oportunista")["extra"] = "- Primary pathogens such as Mycobacterium tuberculosis can cause disease in healthy hosts"
_c("proteina-a-mecanismo")["extra"] = "- Protein A is a cell wall–anchored surface protein of Staphylococcus aureus"
_c("leucocidina")["text"] = ("Some strains of <i>Staphylococcus aureus</i> express {{c1::Panton-Valentine leukocidin (PVL)}}, a <u>pore-forming cytotoxin</u> "
                             "that causes <b>leukocyte death</b> and <b>tissue necrosis</b>")
_c("lps-estrutura")["text"] = ("Lipopolysaccharide <b>endotoxins</b> have a {{c2::<b>lipid A</b>}} anchor <u>responsible for their toxicity</u>, a conserved core "
                               "polysaccharide and a(n) {{c2::<b>O antigen</b>}} <u>that varies among strains</u>")
_c("lps-estrutura")["flags"] = {2: Z}
_c("salmonella-fase")["text"] = "<b>Salmonella</b> switches between flagellin {{c1::H1 and H2}} by inverting a <b>promoter-containing DNA segment</b>"
_c("salmonella-fase")["extra"] = "- The Hin recombinase flips the segment (phase variation)"
_c("endotoxina-membrana")["text"] = "{{c1::Endotoxin::Exo or endotoxin}} is a component of the <b>gram {{c2::negative}}</b> <u>outer membrane</u>"
_c("hpylori-vaca")["text"] = "<b>Helicobacter pylori VacA</b> induces {{c1::vacuoles}} in <b>gastric epithelial cells</b>, damaging the gastric epithelium"
_c("gnpe-proteina-m")["text"] = ("<div><b>PSGN</b> occurs with <u>nephritogenic</u> strains of <i>group A β-hemolytic streptococcus</i>, which carry the "
                                 "{{c1::<b>M protein</b>}} virulence factor, and is caused by glomerular deposition of <b>immune complexes</b></div>")
_c("gnpe-proteina-m")["extra"] = "- The deposited complexes activate complement, which damages the glomerulus"
_c("gnpe-proteina-m")["flags"] = {1: R}
_c("etec-viajante")["extra"] = "- ETEC produces <b>heat labile toxin</b> (LT) similar to cholera toxin, and <b>heat stable toxin</b> (ST)"
# R7: shigella-celulaM passa a cobrar o passo seguinte (N7), sem repetir "M cells"
_c("shigella-celulaM")["text"] = "After escaping the macrophage, <b>Shigella</b> invades enterocytes from their {{c1::basolateral}} side"
_c("shigella-celulaM")["extra"] = "- It reaches the submucosa through M cells"
_c("shigella-celulaM")["alvo"] = "Shigella invade o enterócito pela face basolateral"
_ev("shigella-celulaM", "20, 162; turma I p.64")

_E = {  # espelhos AnKing por tema
    "geral": [1500571366378, 1500571132898], "staph": [1484871950219, 1484871806725], "strep": [1503086807929, 1503086300412],
    "gbs": [1484874299925, 1484874460610], "clost": [1506124869038, 1506185916323], "dif": [1506187604767, 1506188086397],
    "list": [1506190565940, 1506190960748], "gn": [1500752559132, 1500752914634], "pseudo": [1506212646707, 1506212888922],
    "ecoli": [1510188132675, 1510189728852], "qs": [1500571366378, 1510104324862], "tb": [1500500080203, 1500571366378],
}


def _au(key, text, cor, bloco, alvo, slide, autoria, tema, motivo, extra="", falta="busca sem card equivalente (busca/extra-lâminas.txt).", dup=""):
    CARDS.append(au(key, text, cor, bloco, alvo, slide, autoria, falta, _E[tema], motivo, extra=extra, duplicacao_ok=dup))


def _ak(key, nid, cor, bloco, alvo, slide, motivo, **kw):
    CARDS.append(ak(key, nid, cor, bloco, alvo, slide, motivo, **kw))
    if cor != V:
        CARDS[-1]["clinica_lateral"] = True


def _sh(nid, cor, bloco, alvo, slide, motivo):
    CARDS.append(sh(nid, cor, bloco, alvo, slide, motivo))


# -- lacunas do Opus (seção 6), lâminas 1–41 e material da turma --
_au("biofilme-etapas", "In <b>biofilm</b> development, planktonic bacteria attach to a surface and divide into {{c1::microcolonies}}", V, E_,
    "Etapas do biofilme", "35", "central", "geral", "Verde: figura da lâmina 35 (Opus N1).", extra="- The surface can be biotic or abiotic")
_au("biofilme-quorum", "{{c1::Quorum sensing}} drives the transition from microcolonies to a mature <b>biofilm</b> community", Z, E_,
    "QS no amadurecimento do biofilme", "35", "central", "qs", "Azul: lâmina 35 (Opus N2).", extra="- Mature biofilms form mushroom-shaped towers with water channels")
_au("hipersensibilidade-lesao", "<b>Bacteria</b> injure host cells directly, through toxins or through {{c1::hypersensitivity}} reactions", Z, A_,
    "Três mecanismos de lesão", "10", "central", "geral", "Azul: lâmina 10 (Opus N3).", extra="- Rheumatic fever after Streptococcus pyogenes is an immune-mediated example")
_au("tb-celular", "Because <b>Mycobacterium tuberculosis</b> lives inside macrophages, its control depends on {{c1::cell-mediated}} immunity rather than antibodies", Z, D_,
    "Imunidade celular contra intracelulares", "8; transcrição II p.48", "central", "tb", "Azul: lâmina 8 e transcrição II (Opus N4).",
    extra="- IFN-γ from CD4+ T cells activates macrophages<br>- CD8+ T cells kill infected cells")
_au("espa", "In the <b>EPEC</b> type III secretion system, the syringe filament is made of the protein {{c1::EspA}}", R, B_,
    "EspA forma a seringa", "18", "lateral", "ecoli", "Rosa: lâmina 18 (Opus N5).", extra="- EspA is secreted by the system itself")
_au("bfp-iv", "The <b>bundle-forming pilus</b> (BFP) of EPEC is a type {{c1::IV}} pilus", R, B_,
    "BFP é pilus tipo IV", "16, 22", "lateral", "ecoli", "Rosa: lâminas 16 e 22 (Opus N6).", extra="- Type IV pili are assembled by machinery related to the type II secretion system")
_au("icsa", "The <b>Shigella</b> surface protein {{c1::IcsA}} polymerizes host actin for intracellular motility", R, B_,
    "IcsA", "20", "lateral", "ecoli", "Rosa: lâmina 20 (Opus N8).", extra="- Actin tails push the bacterium into the neighboring cell")
_au("fha", "<b>Filamentous hemagglutinin</b> (FHA) is a non-fimbrial adhesin of {{c1::Bordetella pertussis}}", Z, B_,
    "FHA", "21", "central", "geral", "Azul: lâmina 21 (Opus N9).", extra="- Other non-fimbrial adhesins include outer membrane proteins and LPS")
_au("autotransportador", "<b>Autotransporter</b> proteins cross the outer membrane through a {{c1::pore domain}} of their own", R, B_,
    "Autotransportadoras", "21, 23", "lateral", "geral", "Rosa: lâminas 21 e 23 (Opus N10).", extra="- They are the simplest secretion system")
_au("lps-policlonal", "Besides cytokine release, <b>LPS</b> causes {{c1::polyclonal}} B-cell activation", R, C_,
    "LPS ativa B policlonal", "29", "lateral", "geral", "Rosa: figura da lâmina 29 (Opus N11).", extra="- LPS also activates complement and coagulation")
_au("receptores-ferro", "<b>Gram-negative</b> bacteria take up iron from siderophores, transferrin and heme through specific {{c1::outer membrane}} receptors", R, E_,
    "Receptores de ferro", "33", "lateral", "gn", "Rosa: figura da lâmina 33 (Opus N12).", extra="- Uptake into the cytoplasm uses ATP")
_au("luxr", "In <b>Gram-negative quorum sensing</b>, AHL made by a LuxI-type synthase binds a {{c1::LuxR}}-type receptor that activates target genes", R, E_,
    "LuxI/LuxR", "36", "lateral", "qs", "Rosa: lâmina 36 (Opus N13).", extra="- AHL diffuses freely across membranes", dup="ganho: receptor LuxR; quorum-gramneg cobra o AHL")
_au("dois-componentes", "In <b>Gram-positive quorum sensing</b>, the secreted peptide is detected by a {{c1::two-component}} system", R, E_,
    "Sistema de dois componentes", "37", "lateral", "qs", "Rosa: lâmina 37 (Opus N14).", extra="- A sensor kinase phosphorylates a response regulator")
_au("qsec", "In <b>EHEC</b>, AI-3 and host epinephrine are sensed by {{c1::QseC}}, which activates the LEE genes of attaching and effacing lesions", R, E_,
    "QseC", "38", "lateral", "qs", "Rosa: lâmina 38 (Opus N15).", extra="- Bacteria use it to sense the host as well as each other")
_au("meningite-capsuladas", "The encapsulated bacteria that most often cause <b>meningitis</b> are Neisseria meningitidis, Streptococcus pneumoniae and {{c1::Haemophilus influenzae}}", Z, D_,
    "Tríade capsulada da meningite", "32; turma I p.70", "prova", "geral", "Azul: turma I e transcrição I (Opus N17).", extra="- The capsule lets them evade phagocytosis")
_au("ilha-gc", "<b>Pathogenicity islands</b> are recognized by a {{c1::GC content}} different from the rest of the genome", R, C_,
    "Ilha de patogenicidade e GC", "27; transcrição II p.44", "lateral", "geral", "Rosa: transcrição II (Opus N19).", extra="- They were acquired from phages or plasmids")
_au("septicemia", "Transient <b>bacteremia</b> is cleared by phagocytes, whereas in {{c1::septicemia}} bacteria multiply in the blood", Z, A_,
    "Bacteremia × septicemia", "10; transcrição II p.8; turma I p.61", "central", "geral", "Azul: transcrição II e turma I (Opus N20).", extra="- Tooth brushing causes a transient bacteremia")
_au("igg-protease", "<b>Staphylococcus aureus</b> and Streptococcus pyogenes evade opsonization with {{c1::IgG}} proteases", R, D_,
    "Proteases de IgG", "30; turma I p.72", "lateral", "staph", "Rosa: turma I (Opus N21).", extra="- Neisseria, H. influenzae and S. pneumoniae make IgA proteases")
_au("fator-h-neisseria", "<b>Neisseria meningitidis</b> recruits the host complement regulator factor {{c1::H}} to its surface, blocking complement attack", Z, D_,
    "Neisseria recruta fator H", "31; prova 2018", "prova", "geral", "Azul: prova 2018 P2 2.2 (Opus N22).", extra="- Its capsule and LPS are the other major virulence factors")
_au("tropismo-lipase", "<b>Cutibacterium acnes</b> has tropism for sebaceous skin because it is rich in {{c1::lipases}}", R, A_,
    "Tropismo por enzimas", "9; turma III p.4", "lateral", "geral", "Rosa: turma III e transcrição II (Opus N25).", extra="- Tropism reflects the enzymes a bacterium carries")
_au("tb-latente", "In <b>latent tuberculosis</b> infection, the host has no symptoms and does {{c1::not}} transmit the bacillus", R, D_,
    "TB latente", "32; turma I p.82", "lateral", "tb", "Rosa: turma I (Opus N26; liga com o iceberg).", extra="- Immunosuppression can reactivate it as active disease")
_au("disenteria-antibiotico", "Invasive bacillary <b>dysentery</b> requires antibiotics, whereas toxin-mediated watery diarrhea is treated mainly with {{c1::rehydration}}", R, B_,
    "Disenteria × diarreia por toxina", "19; transcrição II p.38", "lateral", "ecoli", "Rosa: transcrição II (Opus N28).", extra="- Dysentery has blood, mucus and tissue destruction")
_au("acido-gastrico", "Enteric bacteria survive <b>gastric acid</b> by keeping their intracellular {{c1::pH}} with proton pumps and amino acid decarboxylases", R, A_,
    "Resistência ácida", "3; monitoria aula 6", "lateral", "gn", "Rosa: monitoria aula 6 (Opus N29).", extra="- Gram-negative bacteria are also more resistant to bile")

# -- G. Cocos Gram-positivos: estafilococos (lâminas 42–84) --
_au("cgp-catalase-teste", "The <b>catalase test</b> is positive when <b>hydrogen peroxide</b> releases {{c1::oxygen bubbles}} on contact with the colony", Z, G_,
    "Prova da catalase", "49", "central", "staph", "Azul: lâminas 49–50 e 84.", extra="- 2 H₂O₂ → 2 H₂O + O₂")
_ak("cgp-catalase", 1500747567415, V, G_, "Catalase separa os cocos Gram+", "50", "Verde: HY 1; catalase separa Micrococcaceae (+) de Streptococcaceae (−), lâminas 48–50.")
_ak("strepto-catalase-neg", 1500748152278, Z, G_, "Estreptococos são catalase-negativos", "50", "Azul: irmão do verde da catalase (lâmina 84).")
_au("staph-planos", "<b>Staphylococci</b> divide in {{c1::all}} planes, which produces their grape-like clusters", Z, G_,
    "Divisão em todos os planos", "52", "central", "staph", "Azul: lâminas 51–53.", dup="ganho: o mecanismo (planos de divisão); o compartilhado cobra o arranjo")
_sh(1791576666993, "azul", G_, "Cachos = estafilococos", "53", "Azul: lâmina 53; card da Morfologia/Prática 1.")
_ak("aureus-narinas", 1484871950219, V, G_, "S. aureus coloniza as narinas", "56", "Verde: HY 2; lâmina 56 (portador nasal, ~60%).")
_ak("aureus-dourado", 1500420138936, R, G_, "Pigmento dourado do S. aureus", "57", "Rosa: lâmina 57 (nome aureus).")
_au("proteina-a-vwf", "<b>Protein A</b> of Staphylococcus aureus also binds {{c1::von Willebrand factor}}, interfering with coagulation", R, G_,
    "Proteína A liga o fator de von Willebrand", "59", "lateral", "staph", "Rosa: lâmina 59.")
_au("fnbpa", "The <b>S. aureus</b> MSCRAMM FnbpA anchors the bacterium to host tissue by binding {{c1::fibronectin}}", Z, G_,
    "FnbpA liga fibronectina", "60", "central", "staph", "Azul: lâmina 60 (FnbpA e CNA).", extra="- The CNA MSCRAMM binds collagen")
_au("coagulase-mecanismo", "<b>Staphylococcal coagulase</b> binds prothrombin, forming {{c1::staphylothrombin}}, which converts fibrinogen to fibrin", R, G_,
    "Coagulase forma estafilotrombina", "62", "lateral", "staph", "Rosa: esquema da lâmina 62.")
_au("coagulase-tubo", "In the tube <b>coagulase test</b>, Staphylococcus aureus makes rabbit {{c1::plasma}} clot", Z, G_,
    "Prova da coagulase", "63", "central", "staph", "Azul: lâmina 63.")
_ak("furunculo", 1484872971571, Z, G_, "S. aureus causa furúnculo e carbúnculo", "64", "Azul: lâminas 64–65.")
_au("carbunculo", "A <b>carbuncle</b> is a deep suppurative lesion formed when several {{c1::furuncles}} coalesce", R, G_,
    "Carbúnculo", "65", "lateral", "staph", "Rosa: lâmina 65.", extra="- A furuncle is a pustule of a hair follicle")
_au("abscesso-profundo", "A deep staphylococcal <b>abscess</b> is a large encysted pustule that has not {{c1::drained}}", R, G_,
    "Abscesso profundo", "67", "lateral", "staph", "Rosa: lâmina 67.")
_au("aureus-feridas", "<b>Staphylococcus aureus</b> often infects surgical wounds and {{c1::burns}}", R, G_,
    "Feridas cirúrgicas e queimaduras", "68, 71", "lateral", "staph", "Rosa: lâminas 68 e 71.", extra="- Its invasiveness also lets it reach the blood (bacteremia)")
_ak("impetigo", 1488680542646, Z, G_, "Impetigo por S. aureus ou S. pyogenes", "69", "Azul: lâmina 69 (e piodermite estreptocócica, lâmina 103).")
_ak("osteomielite", 1488154292555, Z, G_, "S. aureus é a principal causa de osteomielite", "70", "Azul: lâmina 70.")
_au("aureus-toxinas", "<b>Staphylococcal enterotoxins</b>, TSST-1 and exfoliative toxins all act as {{c1::superantigens}}", Z, G_,
    "Toxinas superantigênicas do S. aureus", "74", "central", "staph", "Azul: lâmina 74 (duas categorias de toxinas).",
    extra="- The other category acts on membranes (α, β, δ, γ hemolysins and leukocidin)", dup="ganho: toxinas do S. aureus; superantigeno cobra o mecanismo")
_au("alfa-toxina", "<b>Staphylococcus aureus</b> alpha-toxin is a {{c1::pore-forming}} toxin that lyses red cells and leukocytes", Z, G_,
    "Toxina alfa forma poros", "74; prova 2024", "prova", "staph", "Azul: lâmina 74; prova 2024 P2 1.11 (Opus N24).", extra="- Leukocidin also forms pores in neutrophils")
_ak("enterotoxina-alimentos", 1403301422588, R, G_, "Alimentos da intoxicação estafilocócica", "75", "Rosa: lâmina 75.")
_au("intoxicacao-4h", "<b>Staphylococcal food poisoning</b> causes vomiting about {{c1::4}} hours after eating and resolves within a day", R, G_,
    "Tempo da intoxicação estafilocócica", "75", "lateral", "staph", "Rosa: lâmina 75 (detalhe numérico).")
_ak("tsst", 1484871963660, V, G_, "TSST-1 causa choque tóxico", "76", "Verde: HY 1; lâmina 76.")
_au("tampao", "Use of highly absorbent <b>tampons</b> is a classic risk factor for staphylococcal {{c1::toxic shock syndrome}}", Z, G_,
    "Tampão e síndrome do choque tóxico", "77", "central", "staph", "Azul: lâmina 77.")
_ak("ssss", 1484872061892, V, G_, "S. aureus causa a pele escaldada", "78", "Verde: HY 1; lâmina 78.")
_ak("ssss-granuloso", 1484872136110, Z, G_, "Toxina exfoliativa no estrato granuloso", "78", "Azul: mecanismo da lâmina 78.")
_ak("epidermidis-pele", 1403297162366, R, G_, "S. epidermidis vive na pele", "79", "Rosa: lâmina 79.")
_ak("epidermidis-protese", 1503083839758, Z, G_, "S. epidermidis infecta próteses", "80", "Azul: lâmina 80.")
_ak("saprophyticus-itu", 1402457468984, Z, G_, "S. saprophyticus causa ITU em mulheres jovens", "81", "Azul: lâmina 81.")
_ak("coag-neg-novobiocina", 1500748485870, Z, G_, "Coagulase-negativos separados pela novobiocina", "82, 83", "Azul: lâminas 82–83.")
_ak("saprophyticus-novo", 1500748596181, Z, G_, "S. saprophyticus resiste à novobiocina", "83", "Azul: chave da lâmina 83.")
_ak("epidermidis-novo", 1500748663818, R, G_, "S. epidermidis é sensível à novobiocina", "83", "Rosa: irmão do saprophyticus.")

# -- H. Estreptococos (lâminas 85–110) --
_sh(1791576666842, "azul", H_, "Cadeias = estreptococos", "85", "Azul: lâminas 85–86; card da Morfologia/Prática 1.")
_au("strepto-plano", "<b>Streptococci</b> divide in a {{c1::single}} plane, forming chains like a pearl necklace", Z, H_,
    "Divisão em um só plano", "85", "central", "strep", "Azul: lâmina 85.", dup="ganho: o mecanismo; o compartilhado cobra o arranjo")
_ak("enterococos", 1503188321724, R, H_, "Enterococcus faecalis e faecium", "87", "Rosa: lâmina 87 (gêneros de importância clínica).")
_sh(1791647818070, "azul", H_, "Alfa-hemólise = parcial", "89", "Azul: lâminas 88–89 e 92; card da Fisiologia/Prática 1.")
_ak("alfa-verde", 1503185267125, R, H_, "Halo esverdeado da alfa-hemólise", "89", "Rosa: lâmina 88 (esverdeado).")
_sh(1791647817944, "azul", H_, "Beta-hemólise = total", "90", "Azul: lâmina 90.")
_sh(1791647818194, "azul", H_, "Gama-hemólise = ausente", "91", "Azul: lâmina 91.")
_au("lancefield", "<b>Lancefield</b> grouping classifies streptococci by the antigens of the cell wall {{c1::C carbohydrate}}", Z, H_,
    "Classificação de Lancefield", "93, 94", "central", "strep", "Azul: lâminas 93–94 (hemólise não bastava).", extra="- Groups are named by capital letters (A, B, C, D…)")
_ak("pyogenes-grupo-a", 1503086013100, Z, H_, "S. pyogenes = grupo A", "95", "Azul: tabela das lâminas 95–96 e 99.")
_ak("grupo-d", 1402524036532, R, H_, "Grupo D vive no intestino e trato urinário", "96", "Rosa: tabela da lâmina 96.")
_ak("pyogenes-faringite", 1503086807929, V, H_, "GAS causa faringite com linfadenopatia cervical", "97", "Verde: HY 1; lâmina 97.")
_au("faringite-complicacoes", "Streptococcal <b>pharyngotonsillitis</b> can rarely spread to adjacent tissues, causing sinusitis, otitis and {{c1::mastoiditis}}", R, H_,
    "Complicações supurativas da faringite", "98", "lateral", "strep", "Rosa: lâmina 98.", extra="- Recurrent cases may need tonsillectomy, since the tonsils can be reservoirs")
_ak("capsula-hialuronica", 1503086300412, Z, H_, "Cápsula de ácido hialurônico do GAS", "101", "Azul: lâmina 101.",
    extra_add="- Hyaluronic acid resembles connective tissue, so the capsule is not immunogenic")
_ak("estreptolisinas", 1503091373073, Z, H_, "Estreptolisinas O e S lisam hemácias e leucócitos", "102", "Azul: lâmina 102.")
_au("slo-imunogenica", "<b>Streptolysin O</b> works only without oxygen and, unlike streptolysin S, is {{c1::immunogenic}}", Z, H_,
    "SLO × SLS", "102", "central", "strep", "Azul: lâmina 102.", extra="- Anti-streptolysin O titers reveal a recent infection")
_ak("erisipela", 1484704460208, Z, H_, "Erisipela pelo GAS", "103", "Azul: lâmina 103.")
_ak("agalactiae-camp", 1484874299925, Z, H_, "CAMP positivo do GBS", "105", "Azul: lâmina 105.")
_ak("agalactiae-hipurato", 1503183012345, R, H_, "GBS hipurato positivo", "105", "Rosa: lâmina 105.")
_ak("gbs-meningite", 1484874460610, V, H_, "GBS é a principal causa de meningite neonatal", "106", "Verde: HY 1; lâmina 106.")
_ak("gbs-parto", 1503184229801, Z, H_, "GBS passa ao bebê no parto vaginal", "106", "Azul: lâmina 106 (colonização materna).")
_sh(1791666341941, "rosa", H_, "Profilaxia intraparto do GBS", "106", "Rosa: consequência da colonização (lâmina 106); card do Controle microbiológico.")
_au("gbs-adulto", "In adults, <b>Streptococcus agalactiae</b> causes postpartum {{c1::endometritis}}, urinary infections and bacteremia", R, H_,
    "GBS no adulto", "107", "lateral", "gbs", "Rosa: lâmina 107.")
_ak("pneumococo-lanceta", 1503185570647, V, H_, "Pneumococo: diplococo lanceolado", "108", "Verde: HY 1; lâmina 108.")

# -- I. Bacilos Gram-positivos (lâminas 111–144) --
_ak("bgp-aerobios", 1500747772412, Z, I_, "Bacilos Gram+ aeróbios", "111", "Azul: lâmina 111.")
_ak("bgp-anaerobios", 1500747878416, Z, I_, "Clostridium é bacilo Gram+ anaeróbio", "111", "Azul: lâmina 111.")
_au("bgp-esporos", "Among <b>Gram-positive rods</b>, Clostridium and {{c1::Bacillus}} form spores", Z, I_,
    "Formadores de esporos", "111", "central", "clost", "Azul: lâmina 111 (formadores × não formadores).", extra="- Corynebacterium and Listeria do not form spores")
_ak("anthracis-cadeias", 1506120594303, Z, I_, "B. anthracis: bacilos grandes em cadeias", "112", "Azul: lâmina 112.")
_ak("antraz-cutaneo", 1506120070374, Z, I_, "Antraz cutâneo", "113", "Azul: lâmina 113.")
_au("cereus", "<b>Bacillus cereus</b> causes food poisoning with vomiting or {{c1::diarrhea}}", R, I_,
    "Toxicoinfecção por B. cereus", "113", "lateral", "clost", "Rosa: lâmina 113.")
_ak("clostridios", 1506124869038, V, I_, "Clostridium: bacilo Gram+, esporulado, anaeróbio obrigatório", "114", "Verde: HY 1; lâminas 114–115.")
_au("clostridio-toxinas", "In <b>clostridial disease</b>, spores germinate in tissue without O₂ and the bacteria cause damage mainly through {{c1::toxins}}", Z, I_,
    "Patogenicidade dos clostrídios", "116", "central", "clost", "Azul: esquema da lâmina 116.", extra="- The toxins are histolytic, enterotoxic or neurotoxic")
_au("perfringens-alimento", "<b>Clostridium perfringens</b> food poisoning follows spores that survive cooking and germinate during slow {{c1::cooling}}", R, I_,
    "Esporos sobrevivem ao cozimento", "117", "lateral", "clost", "Rosa: lâmina 117.")
_ak("dupla-hemolise", 1506185916323, Z, I_, "C. perfringens: dupla zona de hemólise", "119", "Azul: lâminas 119–120.")
_ak("gangrena", 1506185788542, V, I_, "Toxina alfa → mionecrose (gangrena gasosa)", "121", "Verde: HY 1; lâmina 121.")
_au("tetano-anticorpo", "Once <b>tetanus toxin</b> is inside nerve terminals, {{c1::antibodies}} can no longer neutralize it", Z, I_,
    "Toxina tetânica protegida dos anticorpos", "123", "central", "clost", "Azul: esquema da lâmina 123.",
    extra="- Treatment debrides the wound and controls symptoms until synapses recover")
_ak("tetano-neonatal", 1537381943312, Z, I_, "Tétano neonatal", "125", "Azul: lâmina 125 (coto umbilical).")
_au("tetano-antitoxina", "Established <b>tetanus</b> is treated with {{c1::antitoxin}}, because vaccination acts too slowly", R, I_,
    "Antitoxina no tétano", "123; transcrição II p.22", "lateral", "clost", "Rosa: transcrição II (Opus N27).", extra="- Vaccination with toxoid is the prevention")
_ak("tetani-solo", 1506125006424, Z, I_, "Esporos do C. tetani no solo", "127", "Azul: lâmina 127.")
_au("botulismo-descendente", "<b>Botulism</b> is a symmetric {{c1::descending}} paralysis that begins with the cranial nerves", Z, I_,
    "Paralisia descendente", "129", "central", "clost", "Azul: lâmina 129.", extra="- It can progress to the respiratory muscles")
_ak("botulismo-infantil", 1506178697419, Z, I_, "Botulismo infantil por esporos no mel", "129", "Azul: lâminas 128–129.")
_ak("difteria-granulos", 1506187604767, Z, I_, "Grânulos metacromáticos do C. diphtheriae", "135", "Azul: lâmina 135.")
_sh(1791730475232, "azul", I_, "Toxina diftérica codificada por profago", "135", "Azul: lâmina 135 (gene tox por bacteriófago); card da Genética bacteriana (substitui Opus N16).")
_au("difteria-nao-invasiva", "<b>Corynebacterium diphtheriae</b> is not invasive, so the disease comes from its {{c1::exotoxin}}", Z, I_,
    "Difteria não é invasiva", "135", "central", "dif", "Azul: lâmina 135.")
_au("difteria-receptor", "<b>Diphtheria toxin</b> binds receptors on {{c1::heart}} and nerve cells, explaining myocarditis and neuropathy", R, I_,
    "Receptores da toxina diftérica", "135", "lateral", "dif", "Rosa: lâmina 135.")
_ak("difteria-pseudomembrana", 1506188086397, Z, I_, "Pseudomembrana acinzentada", "136", "Azul: lâmina 136.")
_ak("difteria-telurito", 1506188679510, R, I_, "Meios de cultura da difteria", "138", "Rosa: lâmina 138.")
_ak("elek", 1506188790003, Z, I_, "Prova de Elek", "138", "Azul: lâmina 138 (pesquisa da toxina).")
_ak("listeria-gravidez", 1506190960748, Z, I_, "Gestantes e Listeria", "139", "Azul: lâmina 139.")
_ak("listeria-frio", 1506190733039, Z, I_, "Listeria cresce na geladeira", "140", "Azul: lâmina 140.")
_ak("listeria-alimentos", 1506190820678, R, I_, "Laticínios e frios contaminados", "140", "Rosa: lâmina 140.")
_au("listeria-fagossomo", "<b>Listeria monocytogenes</b> escapes the phagosome into the {{c1::cytoplasm}} before it fuses with the lysosome", Z, I_,
    "Listeria escapa do fagossomo", "141", "central", "list", "Azul: esquema da lâmina 141.")
_ak("listeria-actina", 1506190565940, Z, I_, "Cauda de actina da Listeria", "141", "Azul: lâmina 141.")
_ak("listeria-placenta", 1506191723831, Z, I_, "Listeria atravessa a placenta", "142", "Azul: lâmina 142.")
_ak("listeria-neonatal", 1506191146568, R, I_, "Listeria e meningite neonatal", "143", "Rosa: lâmina 143.")

# -- J. Bacilos Gram-negativos (lâminas 145–191) --
_ak("pseudomonas-oxidase", 1506212646707, Z, J_, "Pseudomonas é oxidase positiva", "147", "Azul: lâmina 147.")
_ak("pseudomonas-pigmentos", 1506212888922, Z, J_, "Piocianina e pioverdina", "147", "Azul: lâmina 147.")
_au("of-teste", "In the <b>OF test</b>, a nonfermenter such as Pseudomonas acidifies glucose only in the tube {{c1::open}} to air", R, J_,
    "Teste oxidação-fermentação", "148", "lateral", "pseudo", "Rosa: lâmina 148.", extra="- Fermenters acidify both the open tube and the tube sealed with oil")
_ak("pseudomonas-queimadura", 1506213672983, Z, J_, "Pseudomonas em queimaduras e feridas", "150", "Azul: lâmina 150.")
_ak("pseudomonas-fc", 1474670586711, R, J_, "Pseudomonas na fibrose cística", "150", "Rosa: lâmina 150.")
_au("enterobacterias", "<b>Enterobacteriaceae</b> are facultative anaerobes that ferment glucose, reduce nitrate and are oxidase {{c1::negative}}", Z, J_,
    "Fisiologia das enterobactérias", "152", "central", "gn", "Azul: lâmina 152.")
_au("sorotipo", "In <b>E. coli</b> serotyping, O is the LPS antigen, H the flagellar antigen and K the {{c1::capsular}} antigen", Z, J_,
    "Antígenos O, H e K", "154, 165; prova 2017", "prova", "ecoli", "Azul: lâminas 154 e 165; prova 2017 P2 1.2 (Opus N18).", extra="- O plus H defines the serotype (e.g., O157:H7)")
_ak("k1-meningite", 1510188728983, R, J_, "E. coli com antígeno K causa meningite neonatal", "154", "Rosa: turma III p.29 (Opus N18).")
_au("soroaglutinacao", "<b>Enteropathogens</b> are serotyped by slide {{c1::agglutination}} with specific antisera", R, J_,
    "Soroaglutinação", "155", "lateral", "ecoli", "Rosa: lâmina 155.")
_au("ecoli-microbiota", "<b>E. coli</b> colonizes the newborn gut within hours and is the predominant {{c1::facultative}} bacterium of the intestinal microbiota", Z, J_,
    "E. coli na microbiota", "159", "central", "ecoli", "Azul: lâmina 159.", extra="- The same strains can infect other sites")
_au("adesao-padroes", "<b>Diarrheagenic E. coli</b> are classified by their adherence pattern to cultured cells as localized, aggregative or {{c1::diffuse}}", R, J_,
    "Padrões de adesão", "160", "lateral", "ecoli", "Rosa: lâmina 160.")
_ak("klebsiella-capsula", 1473548512472, Z, J_, "Cápsula da Klebsiella", "169", "Azul: lâmina 169.")
_au("o157-sorbitol", "Unlike most <b>E. coli</b>, the O157:H7 strain does not ferment {{c1::sorbitol}}, so its colonies stay colorless on sorbitol MacConkey", Z, J_,
    "MacConkey sorbitol", "164", "central", "ecoli", "Azul: lâmina 164.")
_ak("o157-shu", 1473986325018, Z, J_, "O157:H7 e SHU em crianças", "164", "Azul: lâmina 164 (sorotipos ligados à SHU).")
_ak("salmonella-lactose", 1510187928398, Z, J_, "Salmonella não fermenta lactose", "165", "Azul: lâmina 165.")
_au("vi", "<b>Salmonella</b> Typhi carries the capsular {{c1::Vi}} antigen, which increases its virulence", R, J_,
    "Antígeno Vi", "165", "lateral", "ecoli", "Rosa: lâmina 165.")
_au("shigella-especies", "<b>Shigella</b> has four species, S. dysenteriae, S. flexneri, S. boydii and S. {{c1::sonnei}}", R, J_,
    "Espécies de Shigella", "167", "lateral", "ecoli", "Rosa: lâmina 167.")
_sh(1791647817219, "azul", J_, "MacConkey: sais biliares inibem Gram+", "172", "Azul: lâminas 171–172; card da Fisiologia/Prática 1.")
_sh(1791647817444, "azul", J_, "MacConkey diferencia fermentadores de lactose", "172", "Azul: lâmina 172.")
_au("ss-agar", "<b>SS agar</b> is a highly selective medium for isolating {{c1::Salmonella}} and Shigella", R, J_,
    "Ágar SS", "173", "lateral", "gn", "Rosa: lâmina 173.", extra="- Thiosulfate and ferric citrate reveal H₂S as black colonies")
_au("tsi", "In <b>TSI agar</b>, an acid (yellow) butt with an alkaline (red) slant means only {{c1::glucose}} was fermented", Z, J_,
    "Leitura do TSI", "176, 177", "central", "gn", "Azul: lâminas 176–177.", extra="- Lactose or sucrose fermenters turn the whole tube yellow")
_au("tsi-h2s", "In TSI, <b>H₂S</b> made from thiosulfate reacts with iron and forms a {{c1::black}} precipitate", R, J_,
    "H₂S no TSI", "179", "lateral", "gn", "Rosa: lâmina 179.")
_ak("gn-h2s", 1500752914634, Z, J_, "Não fermentadores de lactose, oxidase −, H₂S + = Salmonella, Proteus", "179", "Azul: algoritmo (lâminas 176–179).")
_ak("proteus-urease", 1510263345494, Z, J_, "Proteus é urease positivo", "181", "Azul: lâmina 181.")
_au("fenilalanina", "A green color after ferric chloride shows <b>phenylalanine deaminase</b>, typical of {{c1::Proteus}}", R, J_,
    "Fenilalanina desaminase", "182", "lateral", "gn", "Rosa: lâmina 182.")
_au("citrato", "Bacteria that use <b>citrate</b> as their only carbon source alkalinize the medium, turning bromothymol {{c1::blue}}", R, J_,
    "Utilização de citrato", "183", "lateral", "gn", "Rosa: lâmina 183.")
_au("descarboxilase", "<b>Lysine decarboxylase</b> forms {{c1::cadaverine}} and alkalinizes the medium", R, J_,
    "Descarboxilação", "184", "lateral", "gn", "Rosa: lâmina 184.")
_ak("indol", 1520991352934, Z, J_, "Indol distingue E. coli de Enterobacter", "185", "Azul: lâmina 185.")
_au("indol-kovacs", "<b>Tryptophanase</b> splits tryptophan into {{c1::indole}}, detected in red with Kovacs reagent", R, J_,
    "Prova do indol", "185", "lateral", "gn", "Rosa: lâmina 185.")
_au("motilidade-meio", "In <b>semisolid agar</b>, growth spreading away from the stab line shows that the bacterium is {{c1::motile}}", R, J_,
    "Prova de motilidade", "186", "lateral", "gn", "Rosa: lâmina 186.")

# -- verso curto dos cards novos e duplicações justificadas --
VERSO2 = {
 "staph-planos": "- Streptococci divide in one plane and form chains",
 "aureus-narinas": "- About 60% of people carry it without disease (microbiota)",
 "proteina-a-vwf": "- Protein A also binds the Fc of IgG",
 "coagulase-mecanismo": "- The fibrin coat walls off the bacteria",
 "coagulase-tubo": "- Coagulase-negative staphylococci leave the plasma liquid",
 "furunculo": "- A furuncle is a pustule of a hair follicle; a carbuncle joins several",
 "abscesso-profundo": "- Abscesses wall the bacteria off from phagocytes",
 "impetigo": "- Vesicles rupture and leave honey-colored crusts",
 "intoxicacao-4h": "- The toxin is preformed in the food, so onset is fast",
 "tsst": "- TSST-1 bridges the TCR and MHC II outside the antigen groove",
 "tampao": "- TSST-1 is produced in the vagina and absorbed",
 "epidermidis-pele": "- It is part of the normal skin and mucosal microbiota",
 "coag-neg-novobiocina": "- S. saprophyticus is resistant; S. epidermidis is sensitive",
 "strepto-plano": "- Staphylococci divide in all planes and form clusters",
 "alfa-verde": "- Intact red cells remain near the colony",
 "pyogenes-grupo-a": "- Group A is defined by the cell wall C carbohydrate",
 "erisipela": "- It usually affects the face",
 "gbs-adulto": "- In newborns it causes meningitis, sepsis and pneumonia",
 "pneumococo-lanceta": "- It is alpha-hemolytic and forms punctiform colonies",
 "bgp-aerobios": "- Clostridium is the anaerobic Gram-positive rod",
 "anthracis-cadeias": "- B. anthracis and B. cereus are the pathogenic species",
 "cereus": "- It is a spore-forming aerobic Gram-positive rod",
 "perfringens-alimento": "- Most outbreaks come from contaminated food kept warm",
 "tetano-neonatal": "- The first sign is difficulty sucking, 5–13 days after birth",
 "tetani-solo": "- The spore is terminal (drumstick shape)",
 "difteria-nao-invasiva": "- The tox gene comes from a bacteriophage",
 "difteria-receptor": "- The B fragment binds the cell and the A fragment enters it",
 "listeria-fagossomo": "- It then spreads from cell to cell with actin tails",
 "listeria-actina": "- Shigella uses the same strategy",
 "pseudomonas-queimadura": "- It is an opportunistic nonfermenter",
 "enterobacterias": "- Pseudomonas, a nonfermenter, is oxidase positive",
 "soroaglutinacao": "- Done in the clinical lab for E. coli, Salmonella, Shigella and Yersinia",
 "adesao-padroes": "- The six categories are EPEC, EIEC, ETEC, EHEC, EAEC and DAEC",
 "o157-sorbitol": "- O157:H7 and O26:H11 are linked to hemolytic uremic syndrome",
 "salmonella-lactose": "- Shigella does not ferment lactose either",
 "vi": "- Vi is characteristic of the species",
 "shigella-especies": "- S. sonnei has a single serotype",
 "klebsiella-capsula": "- Its pathogenicity depends on the capsule composition",
 "tsi-h2s": "- The reaction needs an acid medium",
 "fenilalanina": "- The product is phenylpyruvic acid",
 "citrato": "- Ammonium salts are the nitrogen source",
 "descarboxilase": "- Ornithine gives putrescine and arginine gives agmatine",
 "indol-kovacs": "- The reagent is p-dimethylaminobenzaldehyde",
 "motilidade-meio": "- TTC turns red where bacteria grow",
}
for _k, _x in VERSO2.items():
    _cc = _c(_k)
    if _cc["kind"] == "autoral":
        _cc["extra"] = (_cc["extra"] + "<br>" if _cc.get("extra") else "") + _x
    else:
        _cc["extra_add"] = _x
for _k, _x in {"iga-especies": "IgA1 protease em quatro espécies; igg-protease cobra IgG",
               "tampao": "fator de risco (tampão), não a toxina; tsst cobra a TSST-1",
               "bgp-esporos": "esporulação; bgp-aerobios cobra o metabolismo",
               "difteria-nao-invasiva": "a difteria é toxigênica e não invasiva; o card geral define exotoxina",
               "enterobacterias": "oxidase das enterobactérias; endotoxina-membrana cobra a coloração de Gram",
               "sorotipo": "antígeno K como cápsula no esquema O/H/K; k1-meningite cobra a meningite neonatal"}.items():
    _c(_k)["duplicacao_ok"] = _x
for _k, _x in {"ecoli-microbiota": "facultativo predominante da microbiota; intracelular-facultativo cobra o nicho celular",
               "ss-agar": "meio SS isola Salmonella; o algoritmo do H2S cobra outra pergunta",
               "fenilalanina": "fenilalanina desaminase do Proteus; proteus-urease cobra a urease"}.items():
    _c(_k)["duplicacao_ok"] = _x
# -- revisão card a card dos novos (11/10 noite) --
_c("lps-estrutura")["extra_add"] = "- The O antigen defines the serogroup"
_c("capsula-hialuronica").pop("extra_add", None)
_c("k1-meningite")["extra"] = "- The K1 capsule lets E. coli evade phagocytosis and complement"
