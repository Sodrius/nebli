# Especificação curada — Operon em procariotos (UC03 P2, Biologia Molecular, aula 29, prof. Alexandre Bruni-Cardoso).
# Refeito do zero em 01/10/2026 a pedido de Davi (F-20261001-CLAUDE-08/09): o deck de 24/09 foi apagado por ele.
# Fontes: slides (46 lâminas, Drive 1-XtK14vY0EPLKGSoYlt1gdAIyESikR_-), exercícios da aula 29 (Drive 1COJwRfforQfRlkHh3y4P5NqgKohR6nlK),
# P2 antigas (2019, 2024, 2025). Ordem de busca: AnKing Step -> outros acervos -> MCAT -> autoral.
RUN_ID = "uc03-operon-20261001a"
SHORT = "operon"
LESSON = "2026-uc03-biomol-29-operon-procariotos"
DECK = "NEBLI::UC03::P2::Biologia Molecular::Operon em procariotos"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261001-CLAUDE-09) + EXECUCAO-DECK-AULA, 01/10/2026"

_S = [7, 8, 9, 17, 19, 23, 24, 25, 27, 29, 30, 31, 32, 35, 36, 37, 39, 41, 43, 45]
MEDIA = {f"nebli-uc03-operon-s{n:02d}.png": f"fontes/m{n:02d}.png" for n in _S}
CR = '<br><span style="font-size: 10pt;"><i>Photo credit: Bruni-Cardoso, USP lecture slides</i></span>'


def S(n, w=520):
    return f'<img src="nebli-uc03-operon-s{n:02d}.png" width="{w}">' + CR


def E(text="", img=None, w=520):
    return text + ("<br><br>" if text and img else "") + (S(img, w) if img else "")


BUSCA = ("AnKing Step por texto (operon, lac, repressor, operator, allolactose, CAP/cAMP, sigma, promoter, constitutive, "
         "galactosidase, permease, cis/trans, helix-turn-helix) e por tags First Aid 09_Lac_operon / Bootcamp 06_Lac_Operon; "
         "MCAT e demais Referências Externas pelos mesmos termos: ")


def ak(key, src, flags, bloco, alvo, evid, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=evid, motivo=motivo, **kw)


def au(key, flags, bloco, text, extra, alvo, evid, autoria, falta, motivo):
    return dict(key=key, kind="autoral", flags=flags, bloco=bloco, text=text, extra=extra, alvo=alvo, evid=evid,
                autoria=autoria, busca=BUSCA + falta, motivo=motivo)


V, Z, R = 3, 4, 5  # verde, azul, rosa

CARDS = [
 # ---------- A. Níveis e lógica da regulação (slides 3–12) ----------
 au("niveis", {1: V}, "A-regulacao",
    'Bacteria regulate most genes at the level of {{c1::transcription initiation}}',
    E("Avoids wasting energy on unneeded mRNA and protein"),
    "Iniciação da transcrição como principal ponto de controle", "Slide 3", "central", "nenhum card sobre níveis de regulação em bactérias.", "Verde: ideia que organiza a aula."),
 au("neg-pos", {1: V, 2: V}, "A-regulacao",
    'Regulation by a repressor is called {{c1::negative}} control, whereas regulation by an activator is called {{c2::positive}} control',
    E("Lac repressor = negative, CAP = positive", 8),
    "Regulação negativa × positiva", "Slides 5, 8–12; exercício 1b", "central", "MCAT só tem 'repressor turns off / activator turns on', sem os termos.", "Verde: vocabulário cobrado no exercício 1 e na P2."),
 ak("mcat-repressor", 1554570859931, {1: Z}, "A-regulacao", "Repressor desliga o operon", "Slide 5", "Azul: básico de apoio.", uncloze=[2], origin="MCAT"),
 ak("mcat-activator", 1554571040595, {1: Z}, "A-regulacao", "Ativador liga o operon", "Slide 5", "Azul: básico de apoio.", uncloze=[2], origin="MCAT"),
 au("cis", {1: V}, "A-regulacao",
    'Regulatory DNA sequences (e.g. promoter, operator) act in {{c1::cis}}, only on the same DNA molecule',
    E("", 7),
    "Elementos em cis", "Slides 6–7; P2 2024 q1.13; exercício 3b", "prova", "zero resultado para cis-acting/trans-acting em regulação gênica.", "Verde: cobrado na P2 2024."),
 au("trans", {1: V}, "A-regulacao",
    'Diffusible regulatory proteins (e.g. Lac repressor) act in {{c1::trans}}, even on another DNA molecule',
    E("", 7),
    "Produtos em trans", "Slides 6–7, 27", "prova", "zero resultado para cis-acting/trans-acting em regulação gênica.", "Verde: par do cis."),
 ak("mcat-inducer", 1554571646783, {1: V, 2: Z}, "A-regulacao", "Indutor", "Slides 8, 12, 18", "c1 verde (nome); c2 azul.", origin="MCAT"),
 ak("mcat-inducible", 1554571855936, {1: Z, 2: Z}, "A-regulacao", "Operon induzível: repressor ligado por padrão", "Slide 8", "c2 verde (tipo); c1 azul.", origin="MCAT"),
 ak("mcat-repressible", 1554572295481, {1: Z, 2: Z}, "A-regulacao", "Operon repressível: transcreve por padrão", "Slide 9", "c2 verde (tipo); c1 azul.", origin="MCAT"),
 au("corepressor", {1: Z}, "A-regulacao",
    'A repressible operon is turned off when a(n) {{c1::co-repressor}} lets the repressor bind the operator',
    E("Tryptophan is the co-repressor of the <i>trp</i> operon", 9),
    "Co-repressor", "Slides 9, 12", "central", "MCAT cita corepressor só no Extra do card de operon repressível.", "Azul: termo da aula, menor peso que o lac."),
 # ---------- B. Operon e mRNA policistrônico (13–14) ----------
 ak("mcat-operon", 1554569675116, {1: V, 2: Z, 3: Z}, "B-operon", "Definição de operon", "Slide 13", "c1/c3 verdes; c2 azul.", origin="MCAT"),
 ak("policistronico", 1520972924816, {1: V}, "B-operon", "mRNA bacteriano policistrônico", "Slides 13–14", "Verde (RelativelyHighYield)."),
 ak("mcat-policistronico", 1554508314889, {1: Z}, "B-operon", "Nome 'policistrônico'", "Slide 14", "Azul: sentido inverso do AnKing (cobra o nome).", uncloze=[2], origin="MCAT"),
 ak("shine-dalgarno", 1467833432548, {1: Z}, "B-operon", "RBS/Shine-Dalgarno em cada gene do mRNA", "Slide 14 (RBS)", "Azul: aparece só como legenda."),
 ak("mcat-promoter", 1554570215237, {1: Z, 2: Z}, "B-operon", "Promotor = sítio da RNA polimerase", "Slides 4, 7", "c2 verde; c1 azul.", uncloze=[3], origin="MCAT"),
 ak("mcat-operator", 1554570550202, {1: V, 2: Z, 3: Z}, "B-operon", "Operador = sítio do repressor, sobreposto ao promotor", "Slides 7, 33", "c1 verde; c2/c3 azuis.", uncloze=[4], origin="MCAT"),
 # ---------- C. Operon lac: genes e indução (15–20) ----------
 au("jacob-monod", {1: R}, "C-lac",
    'The operon model was proposed by {{c1::Jacob and Monod}}',
    "",
    "Jacob e Monod", "Slide 16", "lateral", "sem card histórico.", "Rosa: história."),
 au("lacz", {1: V}, "C-lac",
    'In the lac operon, <i>lacZ</i> encodes the enzyme {{c1::β-galactosidase}}',
    E("Cleaves lactose into glucose + galactose", 17),
    "lacZ", "Slides 17–19; P2 2024 q1.12", "prova", "AnKing/MCAT não nomeiam os genes; só 'proteins that transport and digest lactose'.", "Verde: cobrado em 2019 e 2024."),
 au("lacy", {1: V}, "C-lac",
    'In the lac operon, <i>lacY</i> encodes the transporter {{c1::lactose permease}}',
    E("", 17),
    "lacY", "Slides 17, 19; exercício 4", "prova", "AnKing/MCAT não nomeiam os genes.", "Verde."),
 au("laca", {1: R}, "C-lac",
    'In the lac operon, <i>lacA</i> encodes {{c1::thiogalactoside transacetylase}}',
    "",
    "lacA", "Slide 19 (gene A no mapa); gabarito P2 2024", "lateral", "sem card.", "Rosa: só aparece no mapa."),
 au("laci", {1: V}, "C-lac",
    'The Lac repressor is encoded by the regulatory gene {{c1::<i>lacI</i>}}',
    E("Has its own promoter, upstream of the lac operon", 19),
    "lacI e seu promotor", "Slide 19; P2 2019 q2.6", "prova", "nenhum card nomeia lacI.", "Verde: esquema pedido na P2 2019."),
 ak("mcat-lac-inducible", 1554579870544, {1: V}, "C-lac", "Lac é induzível", "Slide 19", "Verde.", origin="MCAT"),
 ak("lac-repressor-sai", 1467772031664, {1: V, 2: V, 3: V}, "C-lac", "Lactose alta solta o repressor do operador", "Slide 20", "Verdes: núcleo do modelo, nos três sentidos."),
 ak("mcat-allolactose", 1554580220779, {1: V, 2: Z, 3: Z}, "C-lac", "Alolactose liga o repressor", "Slides 17, 20, 32", "c1/c3 verdes; c2 azul.", origin="MCAT"),
 au("allolactose-bgal", {1: Z}, "C-lac",
    'β-galactosidase converts some lactose into {{c1::allolactose}}, the lac operon inducer',
    E("", 17),
    "Origem da alolactose", "Slide 17", "central", "MCAT diz 'some lactose is converted' só no Extra, sem a enzima.", "Azul."),
 au("basal", {1: V}, "C-lac",
    'A repressed lac operon still has low {{c1::basal}} expression, which provides the permease needed to import lactose',
    "",
    "Expressão basal", "Slide 34", "central", "AnKing usa 'basal' só como resposta de glicose alta + lactose.", "Verde: pergunta-problema da aula."),
 # ---------- D. Mutantes e ferramentas de Jacob e Monod (21–25) ----------
 au("laci-menos", {1: V}, "D-mutantes",
    'What lac phenotype results from a <i>lacI</i><sup>-</sup> mutation whose repressor cannot bind the operator?<br><br>{{c1::Constitutive expression}}',
    E("", 23),
    "lacI− constitutivo", "Slides 22–23; P2 2019 q2.8–2.9", "prova", "zero card sobre mutantes do lac.", "Verde: cobrado."),
 au("oc", {1: V}, "D-mutantes",
    'An operator mutation (O<sup>c</sup>) that cannot bind the repressor causes {{c1::constitutive}} lac expression',
    E("", 23),
    "Oc constitutivo", "Slide 23; P2 2024 q1.13; exercício 3", "prova", "zero card sobre mutantes do lac.", "Verde: cobrado."),
 au("laci-s", {1: V}, "D-mutantes",
    'A <i>lacI</i><sup>S</sup> super-repressor cannot bind the inducer, leaving the lac operon {{c1::non-inducible}}',
    E("", 23),
    "lacIS não induzível", "Slide 23", "central", "zero card sobre mutantes do lac.", "Verde."),
 au("lacz-menos", {1: Z}, "D-mutantes",
    'Which lac operon protein is still induced by IPTG in a <i>lacZ</i><sup>-</sup> mutant?<br><br>{{c1::Permease (<i>lacY</i>)}}',
    "",
    "lacZ− × lacIS", "Slide 23 ('como distinguir?'); exercício 5", "central", "zero card sobre mutantes do lac.", "Azul."),
 au("lacy-menos", {1: Z}, "D-mutantes",
    'A <i>lacY</i><sup>-</sup> mutant cannot be induced by lactose because {{c1::lactose cannot enter the cell}}',
    "",
    "lacY− não induz", "Exercício 4", "central", "zero card sobre mutantes do lac.", "Azul: exercício da aula."),
 ak("promotor-mutacao", 1467833662315, {1: Z}, "D-mutantes", "Mutação no promotor derruba a transcrição (P−)", "Exercício 5 (P−)", "Azul."),
 au("iptg", {1: V}, "D-mutantes",
    '{{c1::IPTG}} is a non-metabolizable lactose analog that induces the lac operon',
    E("", 24),
    "IPTG", "Slide 24; P2 2019 q2.7, 2024 q1.13, 2025 q1.9", "prova", "zero resultado para IPTG.", "Verde: cobrado em três provas."),
 au("xgal", {1: V}, "D-mutantes",
    'β-galactosidase cleaves {{c1::X-gal}} into a blue product, marking colonies that express <i>lacZ</i>',
    E("White colonies = no β-galactosidase activity", 25, 360),
    "X-gal", "Slides 24–25; P2 2019 q2.7", "prova", "zero resultado para X-gal.", "Verde: cobrado."),
 au("merozigoto", {1: Z}, "D-mutantes",
    'Partial diploids (merozygotes) carry a second copy of the lac operon on a(n) {{c1::plasmid}}',
    E("Transferred by conjugation", 24),
    "Diploide parcial por conjugação", "Slide 24; exercício 5", "central", "zero resultado para merodiploid/partial diploid.", "Azul."),
 # ---------- E. Diploide parcial: dominância, cis e trans (26–29) ----------
 au("dip-laci", {1: V}, "E-diploide",
    'In a partial diploid, <i>lacI</i><sup>-</sup> is {{c1::recessive}} because wild-type repressor acts in trans',
    E("", 27),
    "lacI− recessivo", "Slides 26–27", "prova", "zero card sobre diploide parcial.", "Verde."),
 au("dip-oc", {1: V}, "E-diploide",
    'In a partial diploid, is an O<sup>c</sup> mutation dominant or recessive?<br><br>{{c1::Dominant}}',
    E("Repressor cannot bind the mutant operator", 29),
    "Oc dominante", "Slides 28–29; P2 2024 q1.13; exercício 3a", "prova", "zero card sobre diploide parcial.", "Verde: cobrado."),
 au("dip-oc-cis", {1: V}, "E-diploide",
    'An O<sup>c</sup> mutation affects only the genes on its own DNA molecule, acting in {{c1::cis}}',
    E("", 29),
    "Oc atua em cis", "Slide 29; P2 2024 q1.13b; exercícios 3b–c e 5", "prova", "zero card sobre diploide parcial.", "Verde: cobrado."),
 au("dip-is", {1: Z}, "E-diploide",
    'A <i>lacI</i><sup>S</sup> super-repressor is {{c1::dominant}} in a partial diploid',
    E("Blocks both operators (trans)"),
    "lacIS dominante", "Slide 23 + lógica do slide 27", "central", "zero card sobre diploide parcial.", "Azul: dedução, não está escrita no slide."),
 # ---------- F. Estrutura do repressor (30–33) ----------
 au("tetramero", {1: R}, "F-repressor",
    'The Lac repressor is a(n) {{c1::tetramer}} (two dimers)',
    E("Each dimer binds a palindromic operator site", 30),
    "Repressor tetramérico", "Slides 30–31", "lateral", "sem card estrutural do repressor.", "Rosa: detalhe estrutural."),
 au("hth", {1: Z}, "F-repressor",
    'The Lac repressor binds DNA through a(n) {{c1::helix-turn-helix}} domain',
    E("N-terminal, fits the major groove", 31, 420),
    "Domínio HTH", "Slides 30–32", "central", "zero resultado para helix-turn-helix.", "Azul."),
 au("alosterico", {1: Z}, "F-repressor",
    'Inducer binding changes the shape of the Lac repressor, a(n) {{c1::allosteric}} protein',
    E("", 32),
    "Repressor alostérico", "Slide 32", "central", "MCAT cobre 'change shape', sem o termo.", "Azul."),
 # ---------- G. Glicose, cAMP e CAP (35–37, 44–46) ----------
 ak("glicose-camp", 1467772018848, {1: V, 2: V}, "G-cap", "Glicose baixa → adenilil ciclase → cAMP", "Slide 37", "Verdes."),
 ak("cap", 1467772025117, {1: V}, "G-cap", "cAMP ativa a CAP, a montante do promotor", "Slides 36–37, 44", "Verde."),
 au("crp", {1: R}, "G-cap",
    'CAP is also known as {{c1::CRP (cAMP receptor protein)}}',
    "",
    "CAP = CRP", "Slide 36", "lateral", "sem card.", "Rosa: sinônimo."),
 au("repressao-catabolica", {1: V}, "G-cap",
    'Glucose inhibition of lac operon expression is called {{c1::catabolite repression}}',
    E("Glucose → low cAMP → CAP off the DNA", 37),
    "Repressão por catabólito", "Slides 35–37; gabarito P2 2025 q1.9; exercício 6", "prova", "o termo só aparece no nome da CAP.", "Verde: termo do gabarito de 2025."),
 ak("cond-forte", 1467772038626, {1: V}, "G-cap", "Glicose baixa + lactose → expressão forte", "Slides 35, 46; exercício 2", "Verde."),
 ak("cond-basal", 1467772056515, {1: V}, "G-cap", "Glicose alta + lactose → basal", "Slides 35, 46; exercício 6", "Verde."),
 ak("cond-sem-lactose", 1467772050415, {1: Z}, "G-cap", "Glicose baixa sem lactose → nada", "Slides 35, 46", "Verde: CAP sozinha não basta."),
 ak("cond-nada", 1467772044746, {1: Z}, "G-cap", "Glicose alta sem lactose → nada", "Slides 35, 46; exercício 2c", "Azul: dedutível das outras."),
 ak("mcat-duas-condicoes", 1554580007473, {1: Z}, "G-cap", "Duas condições para expressar", "Slides 35, 46", "Azul: sentido inverso dos quatro cenários.", origin="MCAT"),
 au("camp-exogeno", {1: Z}, "G-cap",
    'Adding {{c1::cAMP}} to a medium with glucose and lactose restores lac operon expression',
    E("CAP-cAMP binds DNA despite glucose"),
    "cAMP exógeno", "Exercício 2e", "central", "sem card.", "Azul: exercício da aula."),
 au("cap-perda", {1: Z}, "G-cap",
    'Without CAP, lac operon expression stays {{c1::basal}} even with lactose present and glucose low',
    E("Same for loss of the CAP site"),
    "Mutante de CAP / sítio CAP", "P2 2019 q2.8", "prova", "sem card.", "Azul: questão de 2019."),
 # ---------- H. Promotor bacteriano e recrutamento da RNAP (38–45) ----------
 au("sigma", {1: V}, "H-promotor",
    'The {{c1::σ (sigma)}} subunit of bacterial RNA polymerase recognizes the promoter',
    E("Binds the -10 and -35 elements", 41),
    "Subunidade σ", "Slide 41", "central", "AnKing só tem σ como alvo da fidaxomicina.", "Verde."),
 au("menos10-35", {1: Z}, "H-promotor",
    'The key elements of a bacterial promoter lie at positions {{c1::-10 and -35}}',
    E("~17 bp apart", 39),
    "Elementos −10 e −35", "Slides 38–40", "central", "AnKing só tem TATA/CAAT eucarióticos e 'AT-rich'.", "Azul."),
 au("consenso-10", {1: R}, "H-promotor",
    'The consensus sequence of the bacterial -10 promoter element is {{c1::TATAAT}}',
    E("Also called the Pribnow box", 39),
    "Consenso −10", "Slides 39, 43", "lateral", "sem card.", "Rosa: sequência."),
 au("consenso-35", {1: R}, "H-promotor",
    'The consensus sequence of the bacterial -35 promoter element is {{c1::TTGACA}}',
    E("", 39),
    "Consenso −35", "Slides 39, 43", "lateral", "sem card.", "Rosa: sequência."),
 au("promotor-fraco", {1: Z}, "H-promotor",
    'A promoter that deviates from the consensus sequence is a(n) {{c1::weak}} promoter',
    E("The lac promoter is a weak promoter", 43),
    "Promotor fraco", "Slides 42–43", "central", "sem card.", "Azul."),
 au("cap-recruta", {1: V}, "H-promotor",
    'CAP activates the weak lac promoter by {{c1::recruiting RNA polymerase}}',
    E("Direct CAP-RNA polymerase contact", 45),
    "Ativador recruta a RNAP", "Slides 42, 45", "central", "AnKing diz só 'increased transcription'.", "Verde: mecanismo do ativador."),
 au("alfa-ctd", {1: R}, "H-promotor",
    'CAP contacts the {{c1::α}} subunit of RNA polymerase',
    E("C-terminal domain (αCTD)"),
    "CAP–αCTD", "Slides 36, 45", "lateral", "sem card.", "Rosa: detalhe da figura."),
]

# Alvo já vivo em outra aula: associa por tag, sem copiar (um card, um histórico).
COMPARTILHADOS = {1790166169397: ("Genética bacteriana · promotores ricos em AT — slides 38–40", "azul")}

EXCLUIDOS = [
 (1554579520751, "MCAT 'Lac operon contains genes…': impreciso ('digest it into glucose') e sem ganho sobre lacZ/lacY"),
 (1467833420202, "mRNA procariótico sem processamento: não está na aula (aula de transcrição)"),
 (1467833441597, "Promotor por gene em eucariotos: aula seguinte (regulação em eucariotos)"),
 (1467833689549, "Silencers / enhancers (1467833693475, 1467833724957): eucariotos, aula seguinte"),
 (1489873889112, "Fidaxomicina e σ; rifampicina (1467833865131 etc.): farmacologia, aula de Antibióticos"),
 (1467833654903, "TATA/CAAT (Hogness): promotor eucariótico"),
 (1468086171259, "30S e Shine-Dalgarno (também 1468090032393, 1554559721653): tradução, outra aula"),
]
FORA_DO_RECORTE = [
 "Slide 2 (dogma central) e slide 4 (promotor/terminador): revisão de aulas anteriores",
 "Slide 3, 'por que existe regulação nas outras camadas?': pergunta de discussão, fica no Extra do card de níveis e no Tab",
 "Slides 10–11 (regulação positiva induzível/repressível): cobertos por negativo×positivo, indutor e co-repressor; sem exemplo próprio na aula",
 "Slide 40 (lista de promotores fortes de E. coli) e espaçamento de 17 pb: ilustração; 17 pb vai no Extra",
 "Atenuação do operon trp, exclusão do indutor: não estão nos slides",
]
