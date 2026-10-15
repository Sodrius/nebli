# Especificação curada — Regulação da expressão gênica em procariotos: o modelo do operon (UC03 P2, Biologia Molecular, aula 29;
# Prof. Alexandre Bruni-Cardoso; 46 lâminas). Gerada a partir de inventario.py (escrito antes). Refeita em 10/10/2026: o deck de 01/10
# (corrida deck-aula-uc03-biomol-operon-2026-10-01) não tem nota viva; serviu só como banco de candidatos.
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-bm29-20261010a"
SHORT = "bm29"
LESSON = "2026-uc03-biologia-molecular-29-operon-procariotos"
DECK = "NEBLI::UC03::P2::Biologia Molecular::Operon em procariotos"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-05) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt e busca/anking2.txt: operon, lac*, allolactose/IPTG/X-gal, "
         "repressor/operator, CAP/cAMP/catabolite, sigma, -10/-35/Pribnow/consensus, cis/trans/partial diploid, polycistronic, "
         "constitutive, trp/attenuation, inducer/corepressor), 10/10: ")
EXCLUIDOS = [
(1554571855936, "MCAT operon induzível: cloze de 4 palavras e dica '::repressible or inducible'; lac induzível e indutor já cobertos"),
 (1554570859931, "MCAT 'repressor turns the operon off': trivial diante de neg-pos e do mecanismo do operador"),
 (1554571040595, "MCAT 'activator turns the operon on': idem, coberto por neg-pos e cap-recruta"),
 (1554570215237, "MCAT 'promoter = sítio da RNA polimerase': revisão; o promotor entra pela oclusão da lâmina 7 e pelos cards de σ"),
 (1554508314889, "MCAT 'polycistronic mRNA': repete o AnKing de mRNA policistrônico em sentido inverso, sem ganho"),
 (1467833432548, "Shine-Dalgarno inicia a tradução: aula de tradução (UC02); o ponto da aula (um RBS por cistron) fica no autoral rbs"),
 (1554579520751, "MCAT 'Lac operon contains genes…': impreciso ('digest it into glucose') e sem ganho sobre lacZ/lacY"),
 (1489873889112, "Fidaxomicina inibe σ: farmacologia da aula de Antibióticos"),
 (1467833865131, "Rifamicinas e RNA polimerase procariótica: aula de Antibióticos"),
 (1467927049625, "Procariotos têm uma só RNA polimerase: aula de transcrição (UC02)"),
 (1467833654903, "TATA/CAAT: promotor eucariótico, já vivo em Eucariotos I"),
]
FORA_DO_RECORTE = [
 "Lâmina 2 (dogma central) e transcrição reversa/replicação de RNA: revisão de UC01/UC02",
 "Operon trp em detalhe (peptídeo líder, atenuação): a aula só o usa como exemplo; atenuação vive em RNAs não codificadores (bm54)",
 "Tamanhos dos genes no mapa (1040, 3510, 780, 825 pb), massa do monômero (36 kDa) e operadores secundários O2/O3 (Lehninger)",
 "Lâmina 40 (lista de promotores de E. coli) além da ideia de promotor forte para rRNA/tRNA",
 "Experimento de 35S e teoria de Yudkin (texto bibliográfico): história além do que a aula cobra",
 "Link de vídeo da lâmina 24",
]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def io(key, page, name, cor, bloco, alvo, motivo, lines=(), search=(), rects=(), mask_rects=(), remarks=""):
    return dict(key=key, kind="slideio", page=page, half="full", title_size=99, lines=list(lines), search=list(search), rects=list(rects),
                mask_rects=list(mask_rects), name=name, remarks=remarks, aponta="estrutura", flags={1: cor}, bloco=bloco, alvo=alvo,
                evid=f"Slide {page}", motivo=motivo, busca=BUSCA + "nenhuma figura de esquema de operon com rótulos nos acervos (só o Operon.jpg do MCAT, sem sítio do ativador nem gene regulador).")


LAC = [1467772031664, 1467772025117]
MUT = [1467772031664, 1467833662315]
COND = [1467772056515, 1467772038626]
PROM = [1467833662315, 1520972924816]
A_, B_, C_, D_, E_, F_, G_, H_, I_ = ("A-niveis-e-logica", "B-operon", "C-operon-lac", "D-mutantes", "E-diploide-parcial", "F-repressor",
                                      "G-basal", "H-glicose-cap", "I-promotor")
CARDS = [
 # ---------- A. Níveis e lógica da regulação (lâminas 3–12) ----------
 au("niveis", "Bacteria regulate most genes at the step of {{c1::transcription initiation}}", {1: V}, A_,
    "Iniciação da transcrição como principal ponto de controle", "3; transcrição I; guia de veteranos", "central", "nenhum card sobre níveis de regulação.", LAC,
    "Verde: ideia que organiza a aula.", extra="- No energy is spent on unneeded mRNA or protein<br>- It is also the best-understood control point"),
 au("outros-niveis", "A longer mRNA {{c1::half-life}} yields more protein from each transcript, another level of gene regulation", {1: Z}, A_,
    "Estabilidade do mRNA como nível de regulação", "3; transcrição I", "central", "sem card de estabilidade do mRNA como regulação.", LAC,
    "Azul: lâmina 3 (por que regular em outras camadas).", extra="- Other levels: RNA processing, translation and protein activity"),
 au("rearranjo", "Some bacteria switch fimbriae on and off by {{c1::inverting}} their promoter through recombination", {1: R}, A_,
    "Rearranjo do DNA como nível de regulação", "3; transcrição I; guia de veteranos", "lateral", "zero resultado para phase variation/inversão de promotor.",
    [1520972924816, 1467833662315], "Rosa: exemplo da transcrição.", extra="- Regulation by DNA rearrangement, like V(D)J recombination"),
 au("pontuacao", "Promoter positions get {{c1::negative}} numbers because they lie upstream of the +1 transcription start site", {1: Z}, A_,
    "Numeração +1, montante e jusante", "4; transcrição I", "central", "sem card de numeração do promotor.", PROM,
    "Azul: base para ler −10 e −35.", extra="- Downstream positions, toward the terminator, are positive"),
 au("neg-pos", "Regulation by a repressor is called {{c1::negative}} control, whereas regulation by an activator is called {{c1::positive}} control", {1: V}, A_,
    "Regulação negativa × positiva", "5, 12; exercício 1b", "prova", "MCAT só tem 'repressor turns off / activator turns on', sem os termos.", LAC,
    "Verde: vocabulário do exercício 1 e da P2.", extra="- The terms name the regulatory protein, not whether a signal turns the gene on or off"),
 au("cis", "Regulatory DNA sequences such as the promoter and operator act in {{c1::cis}}, only on the DNA molecule that carries them", {1: V}, A_,
    "Elementos em cis", "6–7; P2 2024 q1.13; exercício 3b; monitoria", "prova", "zero resultado para cis-acting/trans-acting.", MUT,
    "Verde: cobrado na P2 2024.", extra="- They are not diffusible"),
 au("trans", "Diffusible regulatory proteins such as the Lac repressor act in {{c1::trans}}, even on another DNA molecule", {1: V}, A_,
    "Produtos em trans", "6–7, 27; monitoria", "prova", "zero resultado para cis-acting/trans-acting.", MUT, "Verde: par do cis.",
    extra="- Their gene can lie elsewhere in the genome"),
 ak("mcat-inducer", 1554571646783, {1: V}, A_, "Indutor", 8, "Verde: o termo da lâmina 12; c2 (frase longa) desfeito.", origin="MCAT"),
 ak("mcat-repressible", 1554572295481, {1: Z, 2: Z}, A_, "Operon repressível: transcreve por padrão", 9, "Azul: o lac é induzível; repressível é o contraste.", origin="MCAT"),
 au("corepressor", "In negative repressible control, a {{c1::co-repressor}} binds the repressor so that it attaches to the operator", {1: Z}, A_,
    "Co-repressor", "9, 12; transcrição I (operon trp)", "central", "MCAT cita co-repressor só no Extra.", [1554572295481, 1467772031664],
    "Azul: termo da aula, menor peso que o lac.", extra="- Tryptophan is the co-repressor of the trp operon"),
 au("pos-repressivel", "In positive repressible control, a co-repressor makes the {{c1::activator}} leave the DNA, turning transcription off", {1: Z}, A_,
    "Regulação positiva repressível", "11–12", "central", "sem card dos quatro modos de regulação.", [1554572295481, 1467772025117],
    "Azul: completa os quatro modos das lâminas 8–11."),
 # ---------- B. Operon e mRNA policistrônico (lâminas 7, 13–14) ----------
 io("io-operador", 7, "Operator (repressor-binding site)", Z, B_, "Operador no esquema do operon", "Azul: exercício 1 pede o esquema do operon.", ["Operador"]),
 io("io-promotor", 7, "Promoter", Z, B_, "Promotor no esquema do operon", "Azul: exercício 1.", ["Promotor"]),
 io("io-sitio-ativador", 7, "Activator-binding site", Z, B_, "Sítio do ativador no esquema", "Azul: exercício 1 e P2 2019 (sítio CAP).", rects=[(88, 124, 263, 166)]),
 io("io-gene-regulador", 7, "Regulatory gene", Z, B_, "Gene regulador no esquema", "Azul: exercício 1.", ["Gene", "regulador"]),
 ak("mcat-operon", 1554569675116, {1: V, 2: Z}, B_, "Definição de operon", 13, "c1 verde (objetivo 1); c2 azul; c3 (frase longa) desfeito, coberto por operon-funcao.", origin="MCAT"),
 au("operon-funcao", "Genes in one operon usually encode proteins of the same {{c1::metabolic pathway}}, so a single promoter switches them on together", {1: Z}, B_,
    "Genes do operon têm função relacionada", "13; transcrição I (operon trp); monitoria", "central", "MCAT diz só 'regulated together'.", [1554569675116, 1520972924816],
    "Azul: lâmina 13.", extra="- The trp operon encodes the enzymes of tryptophan synthesis"),
 ak("policistronico", 1520972924816, {1: V}, B_, "mRNA bacteriano policistrônico", 14, "Verde: HY 2 e base do conceito de operon."),
 au("rbs", "Each gene on a bacterial polycistronic mRNA has its own {{c1::ribosome-binding site}}, so it is translated independently", {1: Z}, B_,
    "Um RBS por cistron", "14; transcrição I; guia de veteranos", "central", "AnKing só tem Shine-Dalgarno como início da tradução.", [1520972924816, 1467833662315],
    "Azul: lâmina 14.", extra="- RBS = Shine-Dalgarno sequence, which pairs with 16S rRNA"),
 au("monocistronico", "Eukaryotic mRNAs are monocistronic because the ribosome binds the 5′ {{c1::cap}} and scans to the first AUG", {1: Z}, B_,
    "Por que eucariotos não têm mRNA policistrônico", "14; transcrição I", "central", "sem card do contraste mono × policistrônico.", [1520972924816, 1467833662315],
    "Azul: contraste dado na transcrição."),
 # ---------- C. Operon lac: genes, repressor e indução (lâminas 15–20, 33) ----------
 au("lacz", "In the lac operon, <i>lacZ</i> encodes {{c1::β-galactosidase}}", {1: V}, C_,
    "lacZ", "15, 17; P2 2024 q1.12", "prova", "AnKing/MCAT não nomeiam os genes.", LAC, "Verde: cobrado em 2019 e 2024.",
    extra="- It cleaves lactose into glucose and galactose"),
 au("lacy", "In the lac operon, <i>lacY</i> encodes {{c1::lactose permease}}, which carries lactose into the cell", {1: V}, C_,
    "lacY", "15, 17; exercício 4", "prova", "AnKing/MCAT não nomeiam os genes.", LAC, "Verde: exercícios 4 e 5."),
 au("laca", "In the lac operon, <i>lacA</i> encodes thiogalactoside {{c1::transacetylase}}", {1: R}, C_,
    "lacA", "15; P2 2024 q1.12; Lehninger", "lateral", "sem card.", LAC, "Rosa: função pouco conhecida, só no mapa.",
    extra="- It may modify toxic galactosides for removal"),
 au("laci", "The Lac repressor is encoded by the regulatory gene {{c1::<i>lacI</i>}}", {1: V}, C_,
    "lacI e seu promotor", "15, 19; P2 2019 q2.6; transcrição II", "prova", "nenhum card nomeia lacI.", LAC, "Verde: esquema pedido na P2 2019.",
    extra="- Monocistronic, with its own promoter (P<sub>I</sub>), and expressed constitutively"),
 au("jacob-monod", "The operon model was proposed by {{c1::Jacob and Monod}} from studies of lactose metabolism in <i>Escherichia coli</i>", {1: R}, C_,
    "Jacob e Monod", "16; transcrição III", "lateral", "sem card histórico.", LAC, "Rosa: história.",
    extra="- Nobel Prize 1965, shared with André Lwoff"),
 au("glicose-preferida", "<i>Escherichia coli</i> prefers glucose to lactose because glucose enters {{c1::glycolysis}} without first being cleaved", {1: Z}, C_,
    "Por que a glicose é preferida", "17; transcrição II; guia de veteranos", "central", "sem card da preferência pela glicose.", COND,
    "Azul: dá sentido ao segundo sinal do operon.", extra="- Lactose must first be split by β-galactosidase"),
 au("allolactose-isomero", "The lac inducer allolactose is a(n) {{c1::isomer}} of lactose made by β-galactosidase", {1: Z}, C_,
    "Origem da alolactose", "17, 20; Lehninger", "central", "MCAT diz 'some lactose is converted' só no Extra.", [1554580220779, 1467772031664],
    "Azul: lâminas 17 e 20.", extra="- A side reaction of the few β-galactosidase molecules present before induction"),
 au("por-que-induzir", "Why does <i>Escherichia coli</i> make β-galactosidase only when lactose is present?<br><br>{{c1::It saves energy}}", {1: V}, C_,
    "Sentido da indutibilidade", "18; transcrição II; monitoria", "central", "sem card do porquê da indução.", COND,
    "Verde: lógica da aula.", extra="- A large, fast induction (up to ~10% of cell protein) also gives a competitive edge"),
 ak("mcat-lac-inducible", 1554579870544, {1: V}, C_, "Lac é induzível", 19, "Verde: lâmina 19.", origin="MCAT"),
 ak("mcat-operator", 1554570550202, {1: V, 2: Z, 3: Z}, C_, "Operador sobreposto ao promotor", 19, "c1 verde; c2/c3 azuis; lâminas 19 e 33.", origin="MCAT", uncloze=[4]),
 au("operador-bloqueia", "Bound to the operator, the Lac repressor prevents {{c1::RNA polymerase}} from binding the overlapping promoter", {1: V}, C_,
    "Mecanismo da repressão", "19, 33; transcrição II", "central", "AnKing diz só 'released … increased transcription'.", LAC,
    "Verde: mecanismo da regulação negativa."),
 au("repressao-1000x", "Bound Lac repressor lowers lac operon transcription about {{c1::1000}}-fold", {1: R}, C_,
    "Magnitude da repressão", "19; lâmina 14 da versão II; Lehninger", "lateral", "sem card.", LAC, "Rosa: número."),
 ak("lac-repressor-sai", 1467772031664, {1: V, 2: V, 3: V}, C_, "Lactose solta o repressor do operador", 20, "Verdes: núcleo do modelo."),
 ak("mcat-allolactose", 1554580220779, {1: V, 2: Z}, C_, "Alolactose liga o repressor", 20, "c1 verde; c2 azul; c3 (frase longa) desfeito, coberto por alosterico e lac-repressor-sai.", origin="MCAT"),
 # ---------- D. Mutantes e ferramentas de Jacob e Monod (lâminas 21–25) ----------
 au("laci-menos", "A <i>lacI</i><sup>−</sup> repressor that cannot bind the operator makes lac expression {{c1::constitutive}}", {1: V}, D_,
    "lacI− constitutivo", "21–23; P2 2019 q2.8–2.9; exercício 5", "prova", "zero card sobre mutantes do lac.", MUT, "Verde: cobrado.",
    extra="- Constitutive = β-galactosidase made with or without inducer"),
 au("oc", "Mutation of which DNA element (O<sup>c</sup>) makes lac expression constitutive even with an intact repressor?<br><br>{{c1::Operator}}", {1: V}, D_,
    "Oc constitutivo", "23; P2 2024 q1.13; exercício 3", "prova", "zero card sobre mutantes do lac.", MUT, "Verde: cobrado.",
    extra="- The intact repressor cannot bind the altered operator sequence"),
 au("laci-s", "A <i>lacI</i><sup>S</sup> repressor cannot bind the inducer, leaving the lac operon {{c1::non-inducible}}", {1: V}, D_,
    "lacIS não induzível", "22–23", "central", "zero card sobre mutantes do lac.", MUT, "Verde: lâmina 23.",
    extra="- Non-inducible = little β-galactosidase even with inducer"),
 au("lacy-menos", "A <i>lacY</i><sup>−</sup> mutant is not induced by lactose because lactose cannot {{c1::enter the cell}}", {1: Z}, D_,
    "lacY− não induz", "23; exercício 4; transcrição III", "central", "zero card sobre mutantes do lac.", MUT, "Azul: exercício 4."),
 au("lacz-menos", "In a <i>lacZ</i><sup>−</sup> mutant, IPTG still induces {{c1::permease}}, which distinguishes it from a <i>lacI</i><sup>S</sup> mutant", {1: Z}, D_,
    "Distinguir lacZ− de lacIS", "23 ('como distinguir?'); exercício 5", "central", "zero card sobre mutantes do lac.", MUT, "Azul: pergunta da lâmina 23.",
    duplicacao_ok="ganho: lacy nomeia o produto do gene; aqui a permease é o teste que separa dois mutantes não induzíveis"),
 ak("promotor-mutacao", 1467833662315, {1: Z}, D_, "Mutação no promotor derruba a transcrição (P−)", 23, "Azul: P− do exercício 5; promotor mutante dá fenótipo não induzível."),
 au("iptg", "{{c1::IPTG}} is a lactose analog that induces the lac operon but is not metabolized", {1: V}, D_,
    "IPTG", "24; P2 2019 q2.7, 2024 q1.13, 2025 q1.9", "prova", "zero resultado para IPTG.", LAC, "Verde: cobrado em três provas.",
    extra="- Its sulfur (thio) linkage cannot be cleaved by β-galactosidase"),
 au("iptg-porque", "Jacob and Monod induced with IPTG because lactose is {{c1::consumed}} by the β-galactosidase it induces", {1: Z}, D_,
    "Por que usar indutor não metabolizável", "24; transcrição III", "central", "zero resultado para IPTG.", LAC, "Azul: o porquê da ferramenta."),
 au("xgal", "β-galactosidase cleaves {{c1::X-gal}} into a blue product, marking colonies that express <i>lacZ</i>", {1: V}, D_,
    "X-gal", "24–25; P2 2019 q2.7", "prova", "zero resultado para X-gal.", LAC, "Verde: cobrado.",
    extra="- The released aromatic group dimerizes into a blue dye"),
 au("xgal-nao-indutor", "X-gal does not bind the Lac repressor, so it reports β-galactosidase activity without {{c1::inducing}} the operon", {1: Z}, D_,
    "X-gal não é indutor", "24; transcrição III; P2 2019 q2.7", "prova", "zero resultado para X-gal.", LAC, "Azul: função de cada análogo (P2 2019).",
    extra="- This lets constitutive mutants show up on plates without inducer"),
 au("colonias", "On an X-gal plate without inducer, wild-type <i>Escherichia coli</i> colonies are {{c1::white}}", {1: Z}, D_,
    "Leitura da placa", "25; transcrição III; P2 2019 q2.9", "prova", "zero resultado para X-gal.", LAC, "Azul: leitura da tabela de colônias da P2 2019.",
    extra="- Blue colonies on this plate = constitutive mutants"),
 au("merozigoto", "Jacob and Monod made partial diploids (merodiploids) by transferring a second lac operon on a(n) {{c1::F plasmid}}", {1: Z}, D_,
    "Diploide parcial por conjugação", "24; transcrição III; exercício 5", "central", "zero resultado para merodiploid/partial diploid.", MUT,
    "Azul: ferramenta do experimento.", extra="- Transferred by conjugation; <i>Escherichia coli</i> is otherwise haploid"),
 # ---------- E. Diploide parcial: dominância, cis e trans (lâminas 26–29) ----------
 au("dip-laci", "In a partial diploid, <i>lacI</i><sup>−</sup> is {{c1::recessive}} because wild-type repressor acts in trans", {1: V}, E_,
    "lacI− recessivo", "26–27; transcrição III; monitoria", "prova", "zero card sobre diploide parcial.", MUT, "Verde: pergunta da lâmina 26.",
    extra="- Repressor from the normal copy shuts both operators"),
 au("dip-oc", "In a partial diploid, is an O<sup>c</sup> mutation dominant or recessive?<br><br>{{c1::Dominant}}", {1: V}, E_,
    "Oc dominante", "28–29; P2 2024 q1.13; exercício 3a", "prova", "zero card sobre diploide parcial.", MUT, "Verde: cobrado.",
    extra="- Its own copy stays constitutive despite the normal operator on the other copy"),
 au("dip-oc-cis", "An O<sup>c</sup> mutation affects only the genes on its own DNA molecule, so it acts in {{c1::cis}}", {1: V}, E_,
    "Oc atua em cis", "29; P2 2024 q1.13b; exercícios 3b–c e 5", "prova", "zero card sobre diploide parcial.", MUT, "Verde: cobrado.",
    duplicacao_ok="ganho: cis é a definição geral; aqui é a aplicação ao operador mutante cobrada na P2 2024"),
 au("dip-cis-teste", "Is lacZ expression in the partial diploid I<sup>+</sup> O<sup>c</sup> Z<sup>+</sup> / I<sup>+</sup> O<sup>+</sup> Z<sup>−</sup> constitutive or inducible?<br><br>{{c1::Constitutive}}", {1: V}, E_,
    "Teste cis com lacZ", "29; exercício 3c; P2 2024 q1.13a", "prova", "zero card sobre diploide parcial.", MUT, "Verde: exercício 3c e P2 2024.",
    extra="- The working <i>lacZ</i> sits beside O<sup>c</sup><br>- In I<sup>+</sup> O<sup>c</sup> Z<sup>−</sup> / I<sup>+</sup> O<sup>+</sup> Z<sup>+</sup> it would be inducible",
    duplicacao_ok="ganho: laci-menos dá o fenótipo do mutante; aqui o genótipo do diploide prova a ação em cis"),
 au("dip-trans-teste", "Is β-galactosidase constitutive or inducible in the partial diploid I<sup>−</sup> Z<sup>+</sup> / I<sup>+</sup> Z<sup>−</sup>?<br><br>{{c1::Inducible}}", {1: Z}, E_,
    "Teste trans com lacZ", "27; exercício 5; transcrição III", "prova", "zero card sobre diploide parcial.", MUT, "Azul: par do teste cis.",
    extra="- Repressor from the I<sup>+</sup> copy reaches the operator beside the working <i>lacZ</i>"),
 au("dip-is", "A <i>lacI</i><sup>S</sup> super-repressor is {{c1::dominant}} in a partial diploid because it ignores the inducer and acts in trans", {1: Z}, E_,
    "lacIS dominante", "23 + lógica da 27", "central", "zero card sobre diploide parcial.", MUT, "Azul: dedução da lâmina 27."),
 # ---------- F. Estrutura do repressor (lâminas 30–32) ----------
 au("tetramero", "The Lac repressor is a(n) {{c1::tetramer}} built from two dimers", {1: R}, F_,
    "Repressor tetramérico", "30–31; transcrição II; Lehninger", "lateral", "sem card estrutural do repressor.", LAC, "Rosa: detalhe estrutural.",
    extra="- Each dimer binds a palindromic operator site"),
 au("hth", "The Lac repressor binds the operator through an N-terminal {{c1::helix-turn-helix}} domain", {1: Z}, F_,
    "Domínio HTH", "31–32", "central", "zero resultado para helix-turn-helix.", LAC, "Azul: lâmina 31.",
    extra="- Its recognition helix fits the DNA major groove"),
 au("alosterico", "Inducer binding changes the shape of the Lac repressor, a(n) {{c1::allosteric}} protein that senses the environment", {1: Z}, F_,
    "Repressor alostérico", "32; guia de veteranos", "central", "MCAT cobre 'change shape', sem o termo.", [1554580220779, 1467772031664],
    "Azul: frase-síntese da lâmina 32.", extra="- The inducer binds the core and disorders the DNA-binding domains"),
 # ---------- G. Expressão basal (lâmina 34) ----------
 au("basal", "A repressed lac operon still has low {{c1::basal}} expression, which supplies the permease that first lets lactose in", {1: V}, G_,
    "Expressão basal", "34; transcrição II; Lehninger; monitoria", "central", "AnKing usa 'basal' só como resposta de glicose alta + lactose.", LAC,
    "Verde: pergunta-problema da aula.", extra="- The repressor occasionally leaves the operator",
    duplicacao_ok="ganho: cond-basal cobra o cenário glicose alta + lactose; aqui é o vazamento do operon reprimido que permite a indução"),
 au("feedback", "Lac induction amplifies itself because the inducer brings in more {{c1::permease}}, which brings in more inducer", {1: Z}, G_,
    "Alça positiva da indução", "34; transcrição II", "central", "sem card.", LAC, "Azul: desfecho do problema da lâmina 34.",
    extra="- When lactose runs out, the repressor rebinds and the operon shuts off",
    duplicacao_ok="ganho: lacy nomeia o gene; aqui a permease explica por que a indução se amplifica"),
 # ---------- H. Glicose, cAMP e CAP (lâminas 35–37) ----------
 ak("cond-basal", 1467772056515, {1: V}, H_, "Glicose alta + lactose → basal", 35, "Verde: exercício 6."),
 ak("cond-forte", 1467772038626, {1: V}, H_, "Glicose baixa + lactose → expressão forte", 35, "Verde: exercício 2."),
 ak("cond-sem-lactose", 1467772050415, {1: V}, H_, "Glicose baixa sem lactose → nada", 35, "Verde: o repressor se sobrepõe à CAP (monitoria)."),
 ak("cond-nada", 1467772044746, {1: Z}, H_, "Glicose alta sem lactose → nada", 35, "Azul: dedutível dos outros três."),
 ak("mcat-duas-condicoes", 1554580007473, {1: Z}, H_, "Duas condições para expressar", 35, "Azul: sentido inverso dos quatro cenários.", origin="MCAT"),
 ak("cap", 1467772025117, {1: V}, H_, "cAMP ativa a CAP, a montante do promotor", 36, "Verde: lâmina 36."),
 au("crp", "CAP is also called {{c1::CRP}} (cAMP receptor protein)", {1: R}, H_,
    "CAP = CRP", "36", "lateral", "sem card.", LAC, "Rosa: sinônimo."),
 au("cap-perda", "Without functional CAP, lac expression stays {{c1::low}} even with lactose present and glucose absent", {1: Z}, H_,
    "Mutante de CAP ou do sítio CAP", "36; P2 2019 q2.8", "prova", "sem card.", COND, "Azul: questão de 2019.",
    extra="- Same for a mutant CAP site"),
 au("camp-cap", "CAP binds the CAP site only when it carries {{c1::cAMP}}, which acts as its inducer", {1: V}, H_,
    "cAMP como indutor da CAP", "37, 10; transcrição IV", "central", "AnKing diz só 'cAMP leads to activation of CAP'.", [1467772025117, 1467772018848],
    "Verde: CAP é o exemplo de regulação positiva induzível.", extra="- CAP binds as a dimer, inserting an α-helix into the major groove",
    duplicacao_ok="ganho: glicose-camp liga glicose ao cAMP; aqui o cAMP é o sinal que permite a CAP ligar o DNA"),
 ak("glicose-camp", 1467772018848, {1: V, 2: V}, H_, "Glicose baixa → adenilil ciclase → cAMP", 37, "Verdes: lâmina 37."),
 au("glicose-indireta", "Glucose controls CAP {{c1::indirectly}}, by lowering cAMP rather than binding CAP itself", {1: Z}, H_,
    "Controle indireto pela glicose", "37; transcrição IV; monitoria", "central", "sem card.", [1467772018848, 1467772025117], "Azul: ênfase da transcrição."),
 au("repressao-catabolica", "Glucose inhibition of the lac operon through low cAMP is called {{c1::catabolite repression}}", {1: V}, H_,
    "Repressão por catabólito", "35–37; gabarito P2 2025 q1.9; exercício 6", "prova", "o termo só aparece no nome da CAP.", COND,
    "Verde: termo do gabarito de 2025."),
 au("camp-exogeno", "Adding {{c1::cAMP}} to a medium with glucose and lactose restores strong lac operon expression", {1: Z}, H_,
    "cAMP exógeno", "37; exercício 2e", "central", "sem card.", COND, "Azul: exercício 2e.", extra="- CAP–cAMP then binds DNA despite the glucose",
    duplicacao_ok="ganho: camp-cap é o mecanismo; aqui é a previsão do exercício 2e"),
 # ---------- I. Promotor bacteriano e recrutamento da RNA polimerase (lâminas 38–45) ----------
 au("menos10-35", "The key elements of a bacterial promoter lie at positions {{c1::−10 and −35}}", {1: Z}, I_,
    "Elementos −10 e −35", "38; transcrição IV", "central", "AnKing só tem TATA/CAAT eucarióticos.", PROM, "Azul: lâmina 38.",
    extra="- Separated by 17–19 bp; the spacing also matters for σ binding"),
 au("consenso-seq", "The bacterial promoter consensus is {{c1::TTGACA}} at −35 and {{c2::TATAAT}} at −10", {1: R, 2: R}, I_,
    "Sequências consenso", "38–39, 43; transcrição IV; monitoria", "lateral", "zero resultado para TATAAT/Pribnow.", PROM, "Rosa: sequências.",
    extra="- The −10 element is also called the Pribnow box"),
 au("consenso-def", "A consensus sequence lists the {{c1::most frequent}} base at each position across many promoters", {1: Z}, I_,
    "O que é sequência consenso", "39; transcrição IV", "central", "AnKing só tem Kozak como exemplo de consenso.", PROM, "Azul: lâmina 39.",
    extra="- An idealized sequence; few real promoters match it exactly"),
 au("promotor-genes", "Strong promoters drive genes needed all the time, such as {{c1::rRNA}} genes, whereas regulated genes tend to have weak promoters", {1: Z}, I_,
    "Promotores fortes × fracos por tipo de gene", "40; transcrição IV; guia de veteranos", "central", "sem card.", PROM, "Azul: lâmina 40."),
 au("sigma", "The {{c1::σ (sigma)}} subunit of bacterial RNA polymerase recognizes the −10 and −35 promoter elements", {1: V}, I_,
    "Subunidade σ", "41; transcrição IV", "central", "AnKing só tem σ como alvo da fidaxomicina.", PROM, "Verde: lâmina 41.",
    extra="- In eukaryotes, general transcription factors do this job"),
 au("promotor-forte", "The closer a promoter is to the consensus sequence, the {{c1::stronger}} it is", {1: V}, I_,
    "Força do promotor", "42; transcrição IV", "central", "sem card.", PROM, "Verde: objetivo 3 da lâmina 27 da versão II.",
    extra="- Closer match = higher σ affinity = more frequent initiation"),
 au("lac-fraco", "The lac promoter is a(n) {{c1::weak}} promoter, so without an activator it gives only basal transcription", {1: V}, I_,
    "Promotor lac fraco", "43; transcrição IV; monitoria", "central", "sem card.", COND, "Verde: explica a necessidade da CAP.",
    extra="- It differs from the consensus at both −35 (TTTACA) and −10 (TATGTT)"),
 au("cap-recruta", "CAP activates the weak lac promoter by {{c1::recruiting RNA polymerase}}", {1: V}, I_,
    "Ativador recruta a RNA polimerase", "45, 42; transcrição IV", "central", "AnKing diz só 'increased transcription'.", LAC,
    "Verde: mecanismo do ativador.", extra="- Activators make up for promoters that RNA polymerase binds poorly"),
 au("alfa-ctd", "CAP contacts the C-terminal domain of the {{c1::α}} subunit of RNA polymerase", {1: R}, I_,
    "CAP–αCTD", "45, 36, 42; transcrição IV; monitoria", "lateral", "sem card.", LAC, "Rosa: detalhe da figura."),
 # ---------- J. Síntese (lâmina 46) ----------
 au("dois-sensores", "In the lac operon, the repressor senses {{c1::lactose}}, whereas CAP senses {{c1::glucose}}", {1: V}, H_,
    "Dois sinais, dois reguladores", "46; transcrição IV; P2 2025 q1.9", "prova", "AnKing dá os cenários, não a divisão de papéis.", COND,
    "Verde: frase-síntese da aula.", extra="- Repressor = negative control; CAP = positive control"),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
 'pos-repressivel': '- The four modes: repressor or activator, with inducer or co-repressor',
 'operador-bloqueia': '- The DNA covered by the repressor overlaps the DNA covered by RNA polymerase',
 'lac-repressor-sai': '- The true inducer is allolactose, made from lactose',
 'lacz-menos': '- lacI<sup>S</sup> blocks induction of all three genes',
 'dip-oc-cis': '- The operator is a DNA sequence, not a diffusible product',
 'cond-basal': '- Repressor is off, but CAP is not bound to the weak promoter',
 'cond-forte': '- Repressor off and CAP–cAMP bound',
 'cap': '- CAP binds DNA only with cAMP bound',
 'glicose-camp': '- Glucose lowers cAMP, so CAP works only when glucose is scarce',
 'mcat-inducer': '- In the lac operon the inducer is allolactose',
 'mcat-inducible': '- An inducer removes the repressor and turns the operon on',
 'mcat-repressible': '- A co-repressor turns it off, as tryptophan does for the trp operon',
 'mcat-operon': '- One promoter controls all the genes, made as one polycistronic mRNA',
 'policistronico': '- Each coding region has its own start and stop codons',
 'mcat-lac-inducible': '- Allolactose is the inducer',
 'mcat-operator': '- The lac operator overlaps the region covered by RNA polymerase',
 'promotor-mutacao': '- A lac promoter that cannot bind RNA polymerase gives a non-inducible operon',
 'cond-nada': '- Without lactose the repressor stays on the operator',
 'mcat-duas-condicoes': '- Lactose removes the repressor; low glucose lets CAP–cAMP recruit RNA polymerase',
 'crp': '- Same protein as the catabolite activator protein',
 'repressao-catabolica': '- High glucose → low cAMP → CAP off the DNA',
 'consenso-def': '',
 'alfa-ctd': '- αCTD = α subunit C-terminal domain',
 'repressao-1000x': '- Even repressed, a few β-galactosidase molecules remain',
 'tetramero': '',
 'iptg-porque': '- IPTG keeps a constant inducer level',
 'lacy-menos': '- With no permease, even the basal leak cannot let lactose in',
 'oc': '',
 'promotor-genes': '- Weak promoters leave room for activators to control output',
 'menos10-35': '',
 'jacob-monod': '',
 'laca': '',
 'glicose-indireta': '- High glucose → low cAMP',
 'dip-is': '- So the operon stays off in both copies',
 'monocistronico': '- Initiation can only happen near the 5′ end',
 'rbs': '',
 'lacy': '- Also called galactoside permease',
 'cap-perda': '',
 'cond-sem-lactose': '- The repressor blocks transcription even when CAP–cAMP is bound',
}
VERSO = {k: v for k, v in VERSO.items() if v}
DUPLICACAO = {
 'corepressor': 'ganho: co-repressor é o termo; repressor é a proteína',
 'pos-repressivel': 'ganho: o ativador que sai do DNA no modo repressível; CAP e o sítio são outro alvo',
 'laci-s': 'ganho: non-inducible é o fenótipo do mutante; inducible é o tipo do operon',
 'oc': 'ganho: o elemento mutado que causa o fenótipo; mcat-operator define o operador',
 'dip-is': 'ganho: dominância do super-repressor; dip-oc é a do operador',
 'dip-trans-teste': 'ganho: resultado do diploide que prova ação em trans; inducible do MCAT é o tipo do operon',
}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
