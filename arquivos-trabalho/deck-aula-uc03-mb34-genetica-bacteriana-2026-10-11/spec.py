# Especificação curada — Genética bacteriana (UC03 P2, Microbiologia; Profa. Carla Romano Taddei, ICB-USP; 44 lâminas 2026 + transcrição da aula).
# Ordem = lâminas. AnKing → compartilhado (Morfologia, Antibióticos, Operon, RNAs não codificadores, Controle microbiológico) → autoral curto.
import json, re, urllib.request
RUN_ID = "uc03-mb34-20261011a"
SHORT = "mb34"
LESSON = "2026-uc03-microbiologia-34-genetica-bacteriana"
DECK = "NEBLI::UC03::P2::Microbiologia::Genética bacteriana"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261011-CLAUDE-02) + plano vigente, 11/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking*.txt, ~120 consultas), cópias NEBLI vivas de Morfologia, Antibióticos, Controle microbiológico, "
         "Operon e RNAs não codificadores conferidas (compartilhados), 11/10: ")
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


A_, B_, C_, D_, E_, F_, G_, H_ = ("A-genoma", "B-estrutura-do-dna", "C-replicacao", "D-mutacao-e-reparo", "E-recombinacao", "F-transposons", "G-dna-recombinante", "H-operon-lac-e-crispr")
ESP = [1500738431745, 1500738522738]  # transdução (AnKing), usado como vizinhança de estilo
CARDS = [
 # ---------- A. Genoma bacteriano (lâminas 2–6, 18–19) ----------
 au("nucleoide", "The bacterial chromosome is packed into a compact {{c1::nucleoid}} through DNA interaction with the proteins HU and H-NS", Z, A_,
    "Cromossomo compacto: nucleoide", "2", "central", "sem card nos acervos.", [1500405795435, 1467771801123], "Azul: lâmina 2.",
    extra="- The nucleoid has no membrane around it"),
 sh(1791576675592, "azul", A_, "Procarioto: DNA circular; eucarioto: linear", 3, "Azul: lâmina 3, card da Morfologia."),
 au("supertorcido", "Bacterial DNA is {{c1::supercoiled}}, which favors the action of enzymes such as gyrase and topoisomerases", V, A_,
    "DNA supertorcido", "3, 5", "central", "AnKing cobre as enzimas, não o estado supertorcido.", [1467771801123, 1467771810893], "Verde: lâminas 3–5.",
    extra="- Gyrase and ATP introduce negative supercoils; topoisomerases relax them"),
 ak("topoisomerase", 1467771801123, V, A_, "Topoisomerase relaxa o DNA por quebras", "5", "Verde: lâmina 5, HY 2."),
 ak("girase", 1467771810893, V, A_, "Topoisomerase II procariótica = girase", "5", "Azul: lâmina 5."),
 sh(1791668521839, "azul", A_, "Quinolonas inibem girase e topoisomerase IV", 5, "Azul: ligação com a girase (Antibióticos)."),
 au("dna-tamanho", "The E. coli chromosome is about 1.7 mm long, roughly {{c1::850}} times the length of the cell", Z, A_,
    "DNA muito maior que a célula", "6", "central", "sem card nos acervos.", [1500405795435, 1467771762899], "Azul: lâmina 6, valor do Trabulsi.",
    extra="- It must be heavily compacted to fit inside the cell"),
 au("genoma-cromossomal", "A bacterial species is defined by its {{c1::chromosomal}} DNA, whereas plasmids add optional traits", V, A_,
    "Identidade pelo DNA cromossomal", "18; aula", "central", "AnKing cobre o plasmídeo, não a identidade.", [1500405795435, 1500581524674], "Verde: ideia explícita da aula.",
    extra="- A cell that loses a plasmid stays the same species and loses only the extra trait"),
 sh(1791163035024, "azul", A_, "Plasmídeos replicam independentemente", 18, "Azul: lâmina 18, card da Morfologia."),
 au("plasmideo-replicon", "Plasmids replicate autonomously from their own origin, so each one is a(n) {{c1::replicon}}", Z, A_,
    "Plasmídeo é um replicon", "18; aula", "central", "sem card nos acervos.", [1500405795435, 1467771762899], "Azul: transcrição e Trabulsi.",
    extra="- Plasmid copies are shared between the daughter cells"),
 au("plasmideo-perda", "Low-copy-number plasmids can be {{c1::lost}} during cell division, so some daughter cells end up without them", Z, A_,
    "Plasmídeo de baixo número de cópias se perde", "18; aula", "central", "sem card nos acervos.", [1500405795435, 1500581524674], "Azul: transcrição.",
    extra="- Plating on antibiotic medium shows who kept a resistance plasmid"),
 sh(1791576667593, "azul", A_, "Plasmídeos e outras estruturas não essenciais", 18, "Azul: complementa o conceito de DNA extracromossômico."),
 au("genoma-micoplasma", "The smallest bacterial genomes, such as that of Mycoplasma genitalium, encode only about {{c1::480}} genes", R, A_,
    "Tamanho de genomas bacterianos", "19", "lateral", "sem card nos acervos.", [1500405795435, 1467771762899], "Rosa: lâmina 19, número da aula.",
    extra="- Free-living bacteria encode about 2,000 to 5,000 genes"),
 au("genoma-streptomyces", "Streptomyces, producers of many antibiotics, have a large genome of about 8 Mb on a {{c1::linear}} chromosome", R, A_,
    "Streptomyces: genoma grande e linear", "19", "lateral", "sem card nos acervos.", [1500405795435, 1467771762899], "Rosa: lâmina 19, exceção ao cromossomo circular.",
    extra="- The E. coli genome has about 4.6 Mb"),
 # ---------- B. Estrutura do DNA (lâminas 7–17) ----------
 au("dna-antiparalelo", "The two strands of the DNA double helix run {{c1::antiparallel}}, one 5'→3' and the other 3'→5'", Z, B_,
    "Dupla hélice antiparalela", "7, 10", "central", "AnKing cita 'antiparalelo' só em contextos específicos.", [1467771853847, 1467833332774], "Azul: lâminas 7 e 10.",
    extra="- One nucleotide is inverted in relation to the other"),
 au("nucleotideo", "A DNA nucleotide has a phosphate, a pentose sugar called {{c1::deoxyribose}} and a nitrogenous base", Z, B_,
    "Partes do nucleotídeo", "8, 11", "central", "sem card nos acervos.", [1467771853847, 1467683757507], "Azul: lâminas 8 e 11.",
    extra="- RNA has ribose instead"),
 au("purinas-pirimidinas", "Adenine and guanine are {{c1::purines}}, whereas cytosine and thymine are {{c2::pyrimidines}}", Z, B_,
    "Purinas e pirimidinas", "13", "central", "AnKing cobre purinas em outro contexto.", [1467771958669, 1467771962365], "Azul: lâmina 13, base das mutações por transição.",
    extra="- Purines have two rings and pyrimidines have one"),
 au("pontes-hidrogenio", "A–T pairs form {{c1::two}} hydrogen bonds, whereas G–C pairs form {{c2::three}}", V, B_,
    "Pontes de hidrogênio A–T e G–C", "9, 10, 12", "central", "sem card nos acervos.", [1467683854499, 1467771853847], "Verde: lâminas 9, 10 e 12.",
    extra="- A–T pairs are bound less strongly than G–C pairs"),
 ak("gc-tm", 1467683854499, Z, B_, "Mais G–C aumenta a temperatura de fusão", "16", "Azul: consequência das três pontes (lâmina 16)."),
 au("fosfodiester", "Nucleotides are joined by {{c1::phosphodiester}} bonds between the 3' hydroxyl and the 5' phosphate", Z, B_,
    "Ligação fosfodiéster", "14", "central", "sem card nos acervos.", [1467771897291, 1467771853847], "Azul: lâmina 14.",
    extra="- DNA ligase forms this bond between fragments"),
 au("desnaturacao", "DNA denaturation separates the strands by breaking the {{c1::hydrogen}} bonds, which heat or chemicals can cause", Z, B_,
    "Desnaturação do DNA", "16", "central", "AnKing só traz PCR.", [1467683854499, 1468605428299], "Azul: lâmina 16.",
    extra="- Covalent bonds in each strand are not broken"),
 au("renaturacao", "Renaturation is the {{c1::reannealing}} of separated DNA strands", R, B_,
    "Renaturação", "16", "lateral", "sem card nos acervos.", [1467683854499, 1468605437554], "Rosa: lâmina 16.",
    extra="- In PCR the primers anneal after the heat step"),
 # ---------- C. Replicação (lâminas 18–23) ----------
 ak("origem-replicacao", 1467771762899, Z, C_, "Origem de replicação", "20, 21", "Azul: lâminas 20–21."),
 au("replicacao-bidirecional", "Replication of the circular bacterial chromosome starts at one origin and proceeds {{c1::bidirectionally}} with two forks", V, C_,
    "Replicação bidirecional", "20", "central", "AnKing não cobre o cromossomo circular.", [1467771762899, 1467771785512], "Verde: lâmina 20 e Trabulsi.",
    extra="- The forks meet at the terminus, about 180° from oriC"),
 au("replicacao-semiconservativa", "Bacterial DNA replication is {{c1::semiconservative}}, so each daughter chromosome keeps one parental strand", Z, C_,
    "Replicação semiconservativa", "18; aula", "central", "sem card nos acervos.", [1467771762899, 1467771842612], "Azul: lâmina 18 e guia.",
    extra="- The new strand is complementary to the parental strand"),
 au("replicacao-teta", "Replication of a circular chromosome creates a(n) {{c1::theta (θ)}}-shaped intermediate seen by electron microscopy", Z, C_,
    "Estrutura θ", "20", "central", "sem card nos acervos.", [1467771762899, 1467771785512], "Azul: lâmina 20.",
    extra="- Ter sites mark where the two forks end"),
 au("replicacao-velocidade", "The bacterial replication fork advances at about {{c1::50,000}} base pairs per minute", Z, C_,
    "Velocidade da forquilha", "20", "central", "sem card nos acervos.", [1467771842612, 1467771762899], "Azul: lâmina 20.",
    extra="- About 800 bp per second in E. coli"),
 au("oric-sequencias", "The replication origin oriC is highly conserved and has repeats of 9 and 13 bp rich in {{c1::A–T}}", Z, C_,
    "OriC: repetições de 9 e 13 pb", "21", "central", "sem card nos acervos.", [1467771762899, 1467771785512], "Azul: lâmina 21.",
    extra="- DnaA binds the 9-bp boxes; A–T pairs melt more easily"),
 au("oric-gatc", "OriC is enriched in the palindromic sequence {{c1::GATC}}, a target of enzymatic adenine methylation", R, C_,
    "OriC e metilação GATC", "21", "lateral", "sem card nos acervos.", [1467771762899, 1467682225986], "Rosa: lâmina 21.",
    extra="- Methylation helps distinguish old from new strands"),
 ak("helicase", 1467771785512, V, C_, "Helicase abre a forquilha", "22", "Verde: lâmina 22, HY 2."),
 ak("ssb", 1467771793359, V, C_, "SSB impede o reanelamento", "22", "Azul: lâmina 22."),
 ak("primase", 1467771834622, V, C_, "Primase faz o primer de RNA", "22", "Verde: lâmina 22, HY 2."),
 ak("pol3-alonga", 1467771842612, V, C_, "DNA polimerase III alonga a fita", "22, 23", "Verde: lâminas 22–23, HY 2."),
 ak("pol3-revisao", 1467771872364, V, C_, "DNA polimerase III revisa por exonuclease 3'→5'", "23, 24", "Verde: lâminas 23–24, HY 2."),
 ak("pol1-exonuclease", 1521932837174, V, C_, "Polimerase I tem exonuclease 3'→5' e 5'→3'", "23", "Verde: lâmina 23, HY 2."),
 au("pol2-reparo", "Bacterial DNA polymerase {{c1::II}} is an alternative repair polymerase that can also replicate a damaged template", Z, C_,
    "DNA polimerase II", "23", "central", "AnKing não cita a polimerase II.", [1521932837174, 1467771842612], "Azul: tabela da lâmina 23.",
    extra="- Polymerase I fills small gaps; polymerase III is the main replicative enzyme"),
 ak("ligase", 1467771897291, V, C_, "DNA ligase une fragmentos de Okazaki", "22", "Azul: lâmina 22."),
 # ---------- D. Mutação e reparo (lâminas 24–27) ----------
 au("variacao-genetica", "Bacterial genetic variation can arise only by {{c1::mutation}} or {{c2::recombination}}", V, D_,
    "Variação por mutação ou recombinação", "24; aula", "central", "AnKing cobre cada processo isolado.", [1500738431745, 1467771941535], "Verde: ideia central da aula.",
    extra="- Mutation is a random (stochastic) event"),
 au("mutagenico", "Physical or chemical agents that alter DNA are called {{c1::mutagenic}} or genotoxic", Z, D_,
    "Agentes mutagênicos ou genotóxicos", "24", "central", "sem card nos acervos.", [1473732879162, 1496159743226], "Azul: lâmina 24.",
    extra="- Spontaneous mutations also arise without any agent"),
 au("mutacao-tautomero", "Spontaneous replication errors arise because bases undergo {{c1::tautomeric}} shifts that make them pair incorrectly", Z, D_,
    "Mutação espontânea por tautomeria", "24; aula", "central", "sem card nos acervos.", [1467771872364, 1467819727512], "Azul: transcrição.",
    extra="- Proofreading still lets one wrong base slip through per about 10<sup>8</sup> bases"),
 ak("silenciosa", 1467771941535, V, D_, "Mutação silenciosa é a menos grave", "25", "Azul: figura da lâmina 25."),
 ak("sem-sentido", 1467771988825, V, D_, "Mutação sem sentido gera códon de parada", "25", "Azul: figura da lâmina 25."),
 au("sentido-errado", "A point mutation that changes one codon into the codon of another amino acid is a(n) {{c1::missense}} mutation", Z, D_,
    "Mutação de sentido errado", "25", "central", "AnKing cobre silenciosa, sem sentido e fase de leitura, não a missense.", [1467771941535, 1467771988825], "Azul: figura da lâmina 25.",
    extra="- Insertions or deletions shift the reading frame"),
 ak("fase-leitura", 1467771949843, V, D_, "Mutação de fase de leitura é a mais grave", "25", "Azul: figura da lâmina 25."),
 ak("transicao", 1467771958669, R, D_, "Transição troca purina por purina", "aula", "Rosa: a professora diz que o termo importa pouco."),
 ak("transversao", 1467771962365, R, D_, "Transversão troca purina por pirimidina", "aula", "Rosa: idem."),
 ak("uv-dimeros", 1496159950271, V, D_, "Radiação não ionizante forma dímeros de pirimidina", "26", "Verde: lâmina 26, HY 1."),
 sh(1791666344741, "azul", D_, "UV mata micróbios por dímeros de timina", 26, "Azul: card de Controle microbiológico."),
 au("uv-bloqueia", "UV-induced pyrimidine dimers distort the strand and {{c1::block}} DNA replication", Z, D_,
    "Dímeros distorcem a fita e bloqueiam a replicação", "26", "central", "AnKing não liga o dímero ao bloqueio.", [1496159950271, 1467819685605], "Azul: lâmina 26.",
    extra="- A covalent bond joins the adjacent pyrimidines"),
 au("uv-penetracao", "UV light penetrates only a few millimeters, so its mutagenic damage and cancer risk are confined to the {{c1::skin}}", Z, D_,
    "UV só atinge a superfície", "26; aula", "central", "sem card nos acervos.", [1496159950271, 1467819717437], "Azul: transcrição.",
    extra="- Ionizing radiation penetrates deeply"),
 au("ionizante-quebras", "Ionizing radiation such as X-rays causes {{c1::single- and double-strand}} breaks in DNA", Z, D_,
    "Radiação ionizante: quebras de fita", "26", "central", "AnKing cobre o reparo, não a lesão.", [1496159743226, 1467819823153], "Azul: lâmina 26.",
    extra="- Heat also causes several types of lesions"),
 sh(1791630179144, "rosa", D_, "Transposons como fonte de variação", 31, "Rosa: card de RNAs não codificadores sobre transposons."),
 au("planar-etidio", "Planar molecules such as {{c1::ethidium bromide}} intercalate between DNA bases and interrupt polymerase synthesis", Z, D_,
    "Moléculas planares intercalam no DNA", "27", "central", "AnKing não traz o brometo de etídio como mutagênico.", [1496159743226, 1467819727512], "Azul: lâmina 27.",
    extra="- SDS (sodium dodecyl sulfate) is another chemical mutagen of this kind"),
 au("alquilantes", "Alkylating agents such as EMS covalently add {{c1::alkyl}} (methyl or ethyl) groups to DNA", Z, D_,
    "Agentes alquilantes", "27", "central", "AnKing trata de quimioterápicos alquilantes.", [1495738313876, 1473732879162], "Azul: lâmina 27.",
    extra="- EMS is ethyl methanesulfonate"),
 au("peroxido", "Hydrogen peroxide is a chemical mutagen that {{c1::oxidizes}} DNA", R, D_,
    "Água oxigenada oxida o DNA", "27", "lateral", "sem card nos acervos.", [1496159743226, 1473732879162], "Rosa: lâmina 27.",
    extra="- It damages many components of the cell"),
 au("lesao-destino", "When DNA repair is overwhelmed, the cell tolerates the lesions by inserting random bases, which generates {{c1::mutants}}", V, D_,
    "Reparo, morte ou mutante", "aula", "central", "AnKing cobre cada reparo isolado.", [1467819685605, 1467819733331], "Verde: ideia central da aula (eventos possíveis).",
    extra="- Without any repair the cell dies, and with correct repair the DNA is restored"),
 au("sos", "In the SOS response, activated RecA cleaves the {{c1::LexA}} repressor and derepresses the DNA repair genes", Z, D_,
    "Resposta SOS: RecA e LexA", "aula; Trabulsi cap. 5", "prova", "sem card nos acervos.", [1467819685605, 1467819733331], "Azul: livro da UC.",
    extra="- UV is the main inducer of the SOS system"),
 au("fotoliase", "DNA photolyase, activated by visible light, repairs {{c1::pyrimidine dimers}}", V, D_,
    "Fotorreativação por fotoliase", "aula", "central", "sem card nos acervos.", [1467819685605, 1467819699712], "Verde: ideia central do reparo na aula.",
    extra="- It is the only lesion that visible light can undo"),
 ak("ner", 1467819685605, V, D_, "Reparo por excisão de nucleotídeos corrige dano por UV", "aula", "Verde: HY 1."),
 ak("excisao-endonuclease", 1467819699712, V, D_, "Endonuclease de excisão corta o dímero", "aula", "Azul: HY 1, mesma via."),
 au("reparo-recombinacional", "In the dark, recombinational repair uses the intact copy of DNA present after replication to fix a damaged {{c1::strand}}", Z, D_,
    "Reparo recombinacional", "aula", "central", "AnKing trata de HR eucariótica.", [1467819823153, 1467819685605], "Azul: transcrição.",
    extra="- Excision-resynthesis is the other repair mechanism that works without light"),
 ak("xeroderma", 1467819717437, V, D_, "Xeroderma pigmentoso: defeito no reparo por excisão", "aula", "Rosa: clínica lateral ao reparo."),
 au("mutantes-aplicacao", "Radiation and mutagens can be used to select mutants with higher production of {{c1::antibiotics}}", R, D_,
    "Obtenção de mutantes", "aula", "lateral", "sem card nos acervos.", [1467771941535, 1467819727512], "Rosa: aplicação citada na aula.",
    extra="- Penicillium strains now make over 10,000 times more penicillin after rounds of mutation and selection"),
 au("auxotrofico", "A mutant unable to synthesize an amino acid or vitamin is {{c1::auxotrophic}}, whereas the wild type is prototrophic", Z, D_,
    "Mutante auxotrófico", "aula; Trabulsi cap. 5", "central", "sem card nos acervos.", [1467771941535, 1467819727512], "Azul: base do teste de Ames e de Lederberg e Tatum.",
    extra="- Reverting a his⁻ mutant gives his⁺ revertants"),
 au("ames", "The Ames test scores mutagens by the number of {{c1::his⁺ revertant}} colonies grown from a histidine-requiring Salmonella strain", V, D_,
    "Teste de Ames", "aula", "central", "AnKing não traz o teste de Ames.", [1467771941535, 1473732879162], "Verde: aplicação principal da aula.",
    extra="- Cells are plated on a medium without histidine"),
 au("cromoteste", "The chromotest uses an E. coli strain with a β-galactosidase gene fusion that gives a {{c1::yellow}} color when a mutagen damages DNA", R, D_,
    "Cromoteste", "aula", "lateral", "sem card nos acervos.", [1467771941535, 1473732879162], "Rosa: segundo teste citado na aula.",
    extra="- Color intensity is read in a spectrophotometer"),
 au("mutagenico-cancer", "A substance that is mutagenic in bacteria is potentially {{c1::carcinogenic}} in humans", V, D_,
    "Mutagênico é potencialmente cancerígeno", "aula", "central", "AnKing trata de carcinógenos específicos.", [1473732879162, 1496159950271], "Verde: justificativa dos testes.",
    extra="- New drugs are tested first with these bacterial assays"),
 # ---------- E. Recombinação: transformação, conjugação, transdução (lâminas 28–36) ----------
 au("transformacao-def", "In transformation, a bacterium takes up free DNA from the medium, which requires the {{c1::competent}} state", V, E_,
    "Transformação e competência", "29", "central", "AnKing não cobre transformação bacteriana.", [1500738431745, 1500673825876], "Verde: lâmina 29.",
    extra="- The result is a change in the genotype of the recipient cell"),
 au("griffith", "In 1928 Griffith showed that heat-killed smooth (encapsulated) pneumococci transformed live {{c1::rough}} cells into virulent smooth cells", Z, E_,
    "Experimento de Griffith", "29; aula", "central", "AnKing não traz Griffith.", [1500738431745, 1500673825876], "Azul: transcrição.",
    extra="- The smooth strain has a capsule and kills mice; the rough strain does not"),
 au("avery", "In 1944 Avery, MacLeod and McCarty showed that the transforming principle is {{c1::DNA}}", V, E_,
    "O princípio transformante é o DNA", "29; aula", "central", "AnKing não traz o experimento.", [1500738431745, 1500673825876], "Verde: transcrição, ponto central da natureza do material genético.",
    extra="- Only the nucleic acid fraction transformed the rough strain, and RNA is too unstable"),
 au("transf-especies", "{{c1::Streptococcus pneumoniae}} takes up linear DNA fragments, whereas Escherichia coli preferentially takes up plasmids", Z, E_,
    "Pneumococo capta DNA linear, E. coli plasmídeo", "29; aula", "central", "sem card nos acervos.", [1500738431745, 1500673825876], "Azul: transcrição.",
    extra="- There is a limit to how much DNA a cell can take up"),
 au("transf-fita", "During transformation only {{c1::one strand}} of the captured DNA enters the cell and pairs with the homologous recipient DNA", R, E_,
    "Só uma fita entra na transformação", "29; Trabulsi cap. 5", "lateral", "sem card nos acervos.", [1500738431745, 1500673825876], "Rosa: livro da UC.",
    extra="- The protected strand forms the eclipse complex"),
 au("transf-calcio", "In artificially induced competence, {{c1::calcium}} ions help the DNA adhere to the bacterial envelope", R, E_,
    "Cálcio e adesão do DNA", "30", "lateral", "sem card nos acervos.", [1500738431745, 1500673825876], "Rosa: figura da lâmina 30.",
    extra="- Cell wall, membranes and phospholipids form the adhesion zone"),
 au("recombinacao-reca", "General (homologous) recombination in bacteria depends on the {{c1::RecA}} protein", Z, E_,
    "Recombinação geral depende de RecA", "28, 36; Trabulsi cap. 5", "prova", "sem card nos acervos.", [1467819823153, 1467771941535], "Azul: livro da UC.",
    extra="- Site-specific recombination does not need RecA"),
 sh(1791576677366, "verde", E_, "Conjugação pelo pilus sexual", 34, "Verde: lâmina 34 e 35, card da Morfologia."),
 au("lederberg-tatum", "In the U-tube experiment of Lederberg and Tatum, no recombinants appeared when two auxotrophs were separated, showing that {{c1::cell contact}} is required", V, E_,
    "Experimento de Lederberg e Tatum", "34; aula", "central", "AnKing não traz o experimento.", [1500673825876, 1500674235789], "Verde: transcrição.",
    extra="- Only young cultures mixed together produced prototrophic colonies"),
 au("fator-f", "The F (fertility) plasmid encodes the sex pilus and the machinery for its own {{c1::transfer}}", V, E_,
    "Plasmídeo F", "34, 35; aula", "central", "AnKing cobre Hfr, não o plasmídeo F.", [1500674235789, 1500674026608], "Verde: lâmina 34.",
    extra="- An F⁺ cell donates, and an F⁻ cell receives"),
 au("conj-fita", "During conjugation only {{c1::one strand}} of the plasmid passes to the recipient, and both cells resynthesize the complementary strand", Z, E_,
    "Conjugação transfere uma fita", "34; aula", "central", "sem card nos acervos.", [1500674235789, 1500674026608], "Azul: lâmina 34 e transcrição.",
    extra="- Afterwards donor and recipient each carry a complete plasmid"),
 ak("conj-plasmideo", 1500674235789, V, E_, "Conjugação normal transfere só plasmídeo", "34", "Verde: lâmina 34, HY 3."),
 au("hfr-def", "A cell with the F plasmid integrated into the chromosome is called {{c1::Hfr}}, for high frequency of recombination", V, E_,
    "Célula Hfr", "34", "central", "AnKing define Hfr de forma imprecisa.", [1500674026608, 1500673915770], "Verde: lâmina 34.",
    extra="- Hfr cells transfer chromosomal genes at a much higher frequency than F⁺ cells"),
 ak("hfr-genoma", 1500674026608, Z, E_, "Hfr transfere genoma bacteriano com o plasmídeo", "34", "Azul: lâmina 34."),
 ak("hfr-mapa", 1500674448942, V, E_, "Conjugação de Hfr permite mapeamento", "34", "Azul: lâmina 34 e transcrição."),
 au("hfr-tempo", "Conjugation of an Hfr strain transfers the whole E. coli chromosome in about {{c1::90–100}} minutes", R, E_,
    "Tempo de transferência do cromossomo", "34; aula", "lateral", "sem card nos acervos.", [1500674026608, 1500674448942], "Rosa: transcrição e livro.",
    extra="- Interrupting the mating at different times maps the genes"),
 au("conj-gram", "Conjugation with a sex pilus occurs mainly in {{c1::Gram-negative}} bacteria", R, E_,
    "Pilus de conjugação em Gram-negativas", "35; aula", "lateral", "sem card nos acervos.", [1500673825876, 1500674235789], "Rosa: transcrição.",
    extra="- Gram-positive cells seem to transfer DNA after direct contact"),
 au("plasmideo-r", "R plasmids carry resistance genes and the transfer factor RTF, which encodes the {{c1::pilus}}", Z, E_,
    "Plasmídeo R e RTF", "aula; Trabulsi cap. 5", "central", "AnKing não detalha o plasmídeo R.", [1525228314739, 1500674235789], "Azul: livro da UC e transcrição.",
    extra="- Resistance determinants without RTF cannot be transferred by conjugation"),
 au("plasmideo-col", "Col plasmids of E. coli encode {{c1::colicins}}, proteins that inhibit other enterobacteria", R, E_,
    "Plasmídeo Col", "aula", "lateral", "sem card nos acervos.", [1500674235789, 1500674026608], "Rosa: transcrição.",
    extra="- Other plasmids carry virulence, enterotoxin or heavy-metal resistance genes"),
 au("plasmideo-promiscuo", "Promiscuous plasmids such as RP4 can be transferred from E. coli to unrelated Gram-negative bacteria such as {{c1::Pseudomonas}}", Z, E_,
    "Plasmídeos promíscuos", "aula", "central", "sem card nos acervos.", [1500674235789, 1525228314739], "Azul: transcrição.",
    extra="- RP4 carries resistance to several antibiotics"),
 au("plasmideo-ti", "The Ti plasmid of Agrobacterium tumefaciens causes tumors in {{c1::plants}}", R, E_,
    "Plasmídeo Ti", "aula", "lateral", "sem card nos acervos.", [1500674235789, 1500405795435], "Rosa: transcrição.",
    extra="- Plasmids can also carry enterotoxin genes of E. coli"),
 ak("plasmideo-exotoxina", 1500581524674, V, E_, "Genes de exotoxinas estão em plasmídeos e bacteriófagos", "33, 35", "Verde: ponte entre conjugação, transdução e patogenicidade."),
 ak("transducao-def", 1500738431745, V, E_, "Transdução: transferência de DNA por bacteriófago", "33", "Verde: lâmina 33."),
 ak("transducao-generalizada", 1500738726042, V, E_, "Transdução generalizada empacota DNA cromossomal", "33", "Verde: lâmina 33."),
 ak("transducao-especializada", 1500738801391, V, E_, "Transdução especializada carrega genes vizinhos do sítio de integração", "33", "Verde: lâmina 33."),
 au("fago-engano", "In generalized transduction a lytic phage mistakenly packages {{c1::bacterial}} DNA instead of its own and injects it into the next cell", Z, E_,
    "Erro de empacotamento do fago", "33; aula", "central", "AnKing não detalha o erro de empacotamento.", [1500738726042, 1500738565627], "Azul: transcrição.",
    extra="- The phage is a vehicle that attaches by electrostatic attraction"),
 ak("lisogenico", 1500739784197, V, E_, "Ciclo lisogênico integra o fago ao genoma", "33", "Azul: contexto da transdução especializada."),
 ak("lisogenia-toxina", 1500739993439, V, E_, "Lisogenia dá toxinas a cepas não tóxicas", "33", "Verde: conversão lisogênica, HY 1."),
 au("conversao-lisogenica", "A bacterium that carries a toxin-encoding prophage has undergone {{c1::lysogenic conversion}}", Z, E_,
    "Conversão lisogênica", "33; aula", "central", "AnKing cobre toxinas, não o termo.", [1500739993439, 1506188306308], "Azul: transcrição.",
    extra="- Corynebacterium diphtheriae causes diphtheria only after a phage brings the toxin gene"),
 ak("difteria-profago", 1506188306308, Z, E_, "Toxina diftérica codificada por β-prófago", "33", "Azul: exemplo da aula."),
 # ---------- F. Transposons (lâminas 31–32) ----------
 ak("transposicao", 1500740499801, V, F_, "Transposição: transposon salta de um sítio a outro", "31", "Verde: lâmina 31, HY 1."),
 au("transposase", "A transposon is a resistance gene flanked by inverted repeats, and the enzyme {{c1::transposase}} moves it to another site", V, F_,
    "Transposon e transposase", "31; aula", "central", "AnKing não cita a transposase.", [1500740499801, 1500740742100], "Verde: lâmina 31 e transcrição.",
    extra="- The repeats act like adhesive tape that finds a matching sequence"),
 au("is-classe1", "Class I (composite) transposons have a marker gene flanked by two copies of an {{c1::insertion sequence (IS)}}", Z, F_,
    "Transposon composto flanqueado por IS", "31, 32; Trabulsi cap. 5", "prova", "sem card nos acervos.", [1500740499801, 1500740742100], "Azul: lâmina 31 e livro.",
    extra="- Class II transposons are flanked by inverted repeats without IS elements"),
 au("tn10", "Transposon Tn10 carries resistance to {{c1::tetracycline}}", Z, F_,
    "Tn10 tetraciclina", "31", "central", "sem card nos acervos.", [1500740742100, 1514427571713], "Azul: figura da lâmina 31.",
    extra="- It is flanked by IS10 elements"),
 au("tn3", "Transposon Tn3 carries resistance to {{c1::ampicillin}} through a β-lactamase gene", Z, F_,
    "Tn3 ampicilina", "32; guia", "prova", "sem card nos acervos.", [1500740742100, 1525228314739], "Azul: lâmina 32 e guia.",
    extra="- Tn3 also carries the transposase and resolvase genes"),
 au("tn5", "Transposon Tn5 carries resistance to {{c1::kanamycin}}", Z, F_,
    "Tn5 canamicina", "32; guia", "prova", "sem card nos acervos.", [1500740742100, 1514427571713], "Azul: lâmina 32 e guia.",
    extra="- Tn4 carries ampicillin, streptomycin and sulfonamide resistance"),
 au("tn9", "Transposon Tn9 carries resistance to {{c1::chloramphenicol}}", R, F_,
    "Tn9 cloranfenicol", "32; aula", "lateral", "sem card nos acervos.", [1500740742100, 1403561122259], "Rosa: transcrição.",
    extra="- It is flanked by IS1 elements in direct orientation"),
 ak("transposon-plasmideo", 1500740742100, V, F_, "Transposon pode ir a um plasmídeo e ser transferido por conjugação", "32", "Azul: lâmina 32."),
 au("transposon-estabilidade", "When a transposon moves from a plasmid to the chromosome, the resistance becomes more {{c1::stable}} because it is no longer lost with the plasmid", Z, F_,
    "Transposição ao cromossomo aumenta a estabilidade", "32; aula", "central", "sem card nos acervos.", [1500740742100, 1500405795435], "Azul: transcrição.",
    extra="- The same jump can copy virulence genes into the chromosome"),
 au("ilha-patogenicidade", "A cluster of transposed virulence genes in the chromosome forms a(n) {{c1::pathogenicity island}}", Z, F_,
    "Ilha de patogenicidade", "32; aula", "central", "AnKing trata de ilhas só na patogenicidade.", [1500740742100, 1500581524674], "Azul: transcrição.",
    extra="- Its GC content differs from the rest of the genome, revealing where it came from"),
 au("mcclintock", "Barbara McClintock discovered mobile genetic elements in {{c1::maize}} (corn)", R, F_,
    "McClintock e o milho", "aula", "lateral", "sem card nos acervos.", [1500740499801, 1500740742100], "Rosa: transcrição.",
    extra="- Her observations of variable kernel colors could not be explained by mutation or recombination"),
 au("transposicao-reca", "Transposition does not require homology, so it occurs at the same frequency in {{c1::recA}} mutants", R, F_,
    "Transposição independe de RecA", "Trabulsi cap. 5", "lateral", "sem card nos acervos.", [1500740499801, 1467771941535], "Rosa: livro da UC.",
    extra="- Homologous recombination depends on RecA"),
 au("integron", "Integrons capture antibiotic resistance gene cassettes by means of an {{c1::integrase}}", R, F_,
    "Integrons", "Trabulsi cap. 5", "lateral", "sem card nos acervos.", [1500740499801, 1525228314739], "Rosa: livro da UC.",
    extra="- They are common in Gram-negative enterobacteria"),
 # ---------- G. DNA recombinante (lâminas 36–40) ----------
 ak("palindromo", 1468549155531, Z, G_, "Palíndromo: sequência igual nas duas fitas", "37", "Azul: lâmina 37, HY 4."),
 ak("endonuclease", 1468549176064, Z, G_, "Endonucleases cortam no meio da fita", "37", "Azul: lâmina 37."),
 au("extremidades", "Cleavage at the axis of symmetry produces {{c1::blunt}} ends, whereas staggered cleavage produces {{c1::cohesive}} ends", V, G_,
    "Extremidades abruptas e coesivas", "37", "central", "sem card nos acervos.", [1468549155531, 1468549176064], "Verde: lâmina 37.",
    extra="- Cohesive (sticky) ends pair with complementary ends cut by the same enzyme"),
 au("ecori", "EcoRI, named after E. coli, cuts the palindromic sequence {{c1::GAATTC}}", R, G_,
    "Enzimas de restrição e organismos de origem", "38", "lateral", "sem card nos acervos.", [1468549155531, 1468549176064], "Rosa: tabela da lâmina 38.",
    extra="- Each restriction enzyme is named after the bacterium it comes from"),
 ak("recombinante", 1468548523778, V, G_, "DNA recombinante junta DNA de duas fontes", "39", "Verde: lâmina 39, HY 3."),
 au("ligase-recombinante", "Plasmid and human DNA cut with the same restriction enzyme can be joined by {{c1::DNA ligase}} into a hybrid plasmid", V, G_,
    "Plasmídeo híbrido por ligase", "36, 39", "central", "AnKing cobre a clonagem em geral.", [1468549196500, 1468549202187], "Verde: lâminas 36 e 39.",
    extra="- The compatible cohesive ends anneal before ligation"),
 ak("clonagem-vetor", 1468549196500, Z, G_, "Clonagem em plasmídeo com resistência a antibiótico", "36, 40", "Azul: lâmina 36."),
 ak("clonagem-transformacao", 1468549202187, Z, G_, "Plasmídeo recombinante é transformado em bactéria", "36, 39", "Azul: lâminas 36 e 39."),
 au("puc18", "The cloning vector pUC18 carries an {{c1::ampicillin}} resistance gene and a lacZ fragment with a multiple cloning site", Z, G_,
    "Vetor pUC18", "40", "central", "sem card nos acervos.", [1468549196500, 1468549202187], "Azul: figura da lâmina 40.",
    extra="- The plasmid has 2,686 bp"),
 # ---------- H. Operon lac e CRISPR (lâminas 41–44) ----------
 sh(1791664581182, "azul", H_, "Operon lac: Jacob e Monod", 41, "Azul: lâmina 41, card do Operon."),
 sh(1791664580657, "azul", H_, "lacZ codifica β-galactosidase", 41, "Azul: lâmina 41."),
 sh(1791664580774, "azul", H_, "lacY codifica a permease", 41, "Azul: lâmina 41."),
 sh(1791664581049, "azul", H_, "lacI codifica o repressor", 41, "Azul: lâmina 41."),
 sh(1791664582020, "verde", H_, "O repressor impede a ligação da RNA polimerase", 41, "Verde: mecanismo central do operon."),
 sh(1791630174170, "verde", H_, "CRISPR guarda DNA de fago", 43, "Verde: lâmina 43."),
 sh(1791630174296, "azul", H_, "Espaçadores entre repetições", 44, "Azul: lâmina 44."),
 sh(1791630174420, "azul", H_, "crRNA e tracrRNA", 44, "Azul: lâmina 44."),
 sh(1791630174671, "azul", H_, "CRISPR/Cas9 como ferramenta de edição", 43, "Azul: lâmina 43."),
 au("crispr-etapas", "CRISPR immunity proceeds through spacer acquisition, crRNA biogenesis and {{c1::interference}}", Z, H_,
    "Etapas da imunidade CRISPR", "44", "central", "Os cards de RNAs não codificadores não dão as etapas.", [1519849478653, 1519849576725], "Azul: figura da lâmina 44.",
    extra="- Interference destroys the viral DNA when the phage reinfects"),
 au("cas1-cas2", "The Cas1–Cas2 complex inserts a fragment of viral DNA into the CRISPR array as a new {{c1::spacer}}", Z, H_,
    "Cas1–Cas2 e aquisição de espaçador", "44", "central", "sem card nos acervos.", [1519849478653, 1519849576725], "Azul: figura da lâmina 44.",
    extra="- Repeats (R) and spacers (S) alternate in the array"),
]

VERSO = {
 "topoisomerase": "- It relaxes supercoils so that the DNA can be unwound ahead of the fork",
 "girase": "- Fluoroquinolones inhibit gyrase and topoisomerase IV",
 "helicase": "- DnaB is the bacterial replicative helicase",
 "primase": "- Primers of RNA are removed later by DNA polymerase I",
 "pol3-revisao": "- This proofreading lowers the error rate of replication",
 "ner": "- Photolyase repairs the same lesion only in the presence of visible light",
 "transposon-plasmideo": "- This is how resistance genes spread between plasmids and chromosomes",
 "plasmideo-exotoxina": "- Diphtheria toxin is encoded by a prophage",
 "transducao-def": "- The phage is the vehicle that carries the bacterial DNA",
 "transducao-generalizada": "- Any bacterial gene can be transduced",
 "transducao-especializada": "- Only genes next to the prophage integration site are carried",
 "clonagem-vetor": "- The antibiotic resistance gene allows selection of the cells that took up the plasmid",
 "recombinante": "- Restriction enzymes and DNA ligase make the junction",
}
DUPLICACAO = {
 "variacao-genetica": "ganho: síntese da aula (só mutação ou recombinação); os cards de transdução e transformação cobram cada mecanismo",
 "fotoliase": "ganho: fotorreativação pela luz visível; o card de NER cobra o reparo no escuro",
 "fago-engano": "ganho: erro de empacotamento da transdução generalizada; os cards AnKing definem o termo",
 "conversao-lisogenica": "ganho: termo da conversão lisogênica; o card AnKing cobra a toxina",
 "fator-f": "ganho: função do plasmídeo F; hfr-def cobra a forma integrada",
 "ligase-recombinante": "ganho: ligação do plasmídeo com DNA humano; recombinante cobra a definição",
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
 "nucleoide": ["bacterial chromosome", "HU and H-NS"], "supertorcido": ["Bacterial DNA", "gyrase and topoisomerases"], "dna-tamanho": ["E. coli chromosome", "cell"],
 "genoma-cromossomal": ["bacterial species", "plasmids"], "plasmideo-replicon": ["Plasmids", "own origin"], "plasmideo-perda": ["Low-copy-number plasmids", "cell division"],
 "genoma-micoplasma": ["smallest bacterial genomes", "Mycoplasma genitalium"], "genoma-streptomyces": ["Streptomyces", "antibiotics"],
 "dna-antiparalelo": ["DNA double helix", "5'→3'"], "nucleotideo": ["DNA nucleotide", "pentose sugar"], "purinas-pirimidinas": ["Adenine and guanine", "cytosine and thymine"],
 "pontes-hidrogenio": ["A–T pairs", "G–C pairs"], "fosfodiester": ["Nucleotides", "3' hydroxyl"], "desnaturacao": ["DNA denaturation", "heat or chemicals"], "renaturacao": ["Renaturation", "DNA strands"],
 "replicacao-bidirecional": ["circular bacterial chromosome", "one origin"], "replicacao-semiconservativa": ["Bacterial DNA replication", "parental strand"],
 "replicacao-teta": ["circular chromosome", "electron microscopy"], "replicacao-velocidade": ["bacterial replication fork", "base pairs per minute"],
 "oric-sequencias": ["oriC", "9 and 13 bp"], "oric-gatc": ["OriC", "adenine methylation"], "pol2-reparo": ["DNA polymerase", "damaged template"],
 "variacao-genetica": ["Bacterial genetic variation"], "mutagenico": ["Physical or chemical agents"], "mutacao-tautomero": ["Spontaneous replication errors", "pair incorrectly"],
 "sentido-errado": ["point mutation", "another amino acid"], "uv-bloqueia": ["pyrimidine dimers", "replication"], "uv-penetracao": ["UV light", "cancer risk"],
 "ionizante-quebras": ["Ionizing radiation", "X-rays"], "planar-etidio": ["Planar molecules", "DNA bases"], "alquilantes": ["Alkylating agents", "EMS"],
 "peroxido": ["Hydrogen peroxide", "chemical mutagen"], "lesao-destino": ["DNA repair is overwhelmed", "random bases"], "sos": ["SOS response", "RecA"],
 "fotoliase": ["DNA photolyase", "visible light"], "reparo-recombinacional": ["recombinational repair", "damaged"], "mutantes-aplicacao": ["Radiation and mutagens", "mutants"],
 "auxotrofico": ["mutant", "wild type"], "ames": ["Ames test", "histidine-requiring Salmonella"], "cromoteste": ["chromotest", "β-galactosidase gene fusion"],
 "mutagenico-cancer": ["mutagenic in bacteria", "humans"], "transformacao-def": ["transformation", "free DNA"], "griffith": ["Griffith", "smooth (encapsulated) pneumococci"],
 "avery": ["Avery, MacLeod and McCarty", "transforming principle"], "transf-especies": ["linear DNA fragments", "plasmids"], "transf-fita": ["transformation", "captured DNA"],
 "transf-calcio": ["artificially induced competence", "DNA adhere"], "recombinacao-reca": ["General (homologous) recombination", "bacteria"],
 "lederberg-tatum": ["U-tube experiment", "two auxotrophs"], "fator-f": ["F (fertility) plasmid", "sex pilus"], "conj-fita": ["conjugation", "plasmid"],
 "hfr-def": ["F plasmid integrated", "high frequency of recombination"], "hfr-tempo": ["Hfr strain", "E. coli chromosome"], "conj-gram": ["Conjugation", "sex pilus"],
 "plasmideo-r": ["R plasmids", "transfer factor RTF"], "plasmideo-col": ["Col plasmids", "enterobacteria"], "plasmideo-promiscuo": ["Promiscuous plasmids", "Gram-negative bacteria"],
 "plasmideo-ti": ["Ti plasmid", "Agrobacterium tumefaciens"], "fago-engano": ["generalized transduction", "lytic phage"], "conversao-lisogenica": ["toxin-encoding prophage"],
 "transposase": ["transposon", "inverted repeats"], "is-classe1": ["Class I (composite) transposons", "marker gene"], "tn10": ["Transposon Tn10"], "tn3": ["Transposon Tn3", "β-lactamase"],
 "tn5": ["Transposon Tn5"], "tn9": ["Transposon Tn9"], "transposon-estabilidade": ["transposon", "plasmid to the chromosome"], "ilha-patogenicidade": ["transposed virulence genes", "chromosome"],
 "mcclintock": ["Barbara McClintock", "mobile genetic elements"], "transposicao-reca": ["Transposition", "homology"], "integron": ["Integrons", "resistance gene cassettes"],
 "extremidades": ["axis of symmetry", "staggered cleavage"], "ecori": ["EcoRI", "palindromic sequence"], "ligase-recombinante": ["Plasmid and human DNA", "restriction enzyme"],
 "puc18": ["cloning vector pUC18", "multiple cloning site"], "crispr-etapas": ["CRISPR immunity", "spacer acquisition"], "cas1-cas2": ["Cas1–Cas2 complex", "viral DNA"],
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

# Âncora de lâmina para a ordem do Browser dos itens que vêm da transcrição ou do livro (sem lâmina própria).
ANCORA = {"transicao": 25, "transversao": 25, "lesao-destino": 27, "sos": 27, "fotoliase": 27, "ner": 27, "excisao-endonuclease": 27, "reparo-recombinacional": 27,
          "xeroderma": 27, "mutantes-aplicacao": 27, "auxotrofico": 27, "ames": 27, "cromoteste": 27, "mutagenico-cancer": 27, "plasmideo-r": 35, "plasmideo-col": 35,
          "plasmideo-promiscuo": 35, "plasmideo-ti": 35, "mcclintock": 31, "transposicao-reca": 32, "integron": 32}
for c in CARDS:
    if c["key"] in ANCORA:
        c["evid"] = f"Slide {ANCORA[c['key']]}; " + c["evid"].replace("Slide ", "")


# ---- Correções da revisão do Opus e dos comentários de Davi (11/10/2026; REVISAO-OPUS.md, F-20261011-CLAUDE-04) ----
def _c(key):
    return next(c for c in CARDS if c["key"] == key)


def _au(key, text=None, extra=None, cor=None):
    c = _c(key)
    if text:
        c["text"] = text
        c["flags"] = {int(n): (cor or list(c["flags"].values())[0]) for n in sorted({int(x) for x in re.findall(r"\{\{c(\d+)::", text)})}
    if extra is not None:
        c["extra"] = extra
    if cor and not text:
        c["flags"] = {k: cor for k in c["flags"]}


def _ak(key, text=None, extra=None, cor=None, **kw):
    c = _c(key)
    fo = c.setdefault("fields_override", {})
    if text:
        fo["Text"] = text
    if extra is not None:
        c.pop("extra_add", None); fo["Extra"] = extra
    if cor:
        c["flags"] = {k: cor for k in c["flags"]}
    c.update(kw)


# erros (E1–E16)
_au("transposase", text="<b>Transposons</b> are mobile DNA segments flanked by <b>inverted repeats</b> that encode {{c1::transposase}}, the enzyme that inserts them at a new site",
    extra="- Antibiotic resistance genes are often carried as cargo between the repeats")
_au("planar-etidio", extra="- Intercalation causes insertions or deletions (frameshift) when the strand is copied<br>- Acridine dyes act the same way")
_au("lederberg-tatum", text="In the <b>U-tube</b> experiment, two auxotrophic E. coli strains separated by a filter that lets DNA pass gave no prototrophs, so conjugation requires {{c1::cell contact}}",
    extra="- Lederberg and Tatum (1946) first obtained prototrophs by mixing the two auxotrophs<br>- Davis (1950) used the U-tube to show that contact is needed")
_au("avery", extra="- Only the nucleic acid fraction transformed the rough strain<br>- DNase abolished transformation, whereas RNase and proteases did not")
_au("ilha-patogenicidade", text="A chromosomal cluster of <b>virulence genes</b> acquired by <b>horizontal transfer</b> is a(n) {{c1::pathogenicity island}}",
    extra="- Its G+C content differs from the rest of the genome, revealing where it came from")
_au("fago-engano", text="In generalized transduction a {{c1::lytic}} <b>phage</b> mistakenly packages <b>bacterial DNA</b> instead of its own and injects it into the next cell",
    extra="- The phage adsorbs to specific receptors on the bacterial surface")
_au("uv-penetracao", text="<b>UV light</b> barely penetrates tissue, so its mutagenic damage and <b>cancer risk</b> are confined to the {{c1::skin}}",
    extra="- Ionizing radiation penetrates deeply<br>- For the same reason UV only sterilizes surfaces")
_au("genoma-micoplasma", text="<b>Mycoplasma genitalium</b>, one of the smallest bacterial genomes (~0.58 Mb), encodes only about {{c1::480}} genes",
    extra="- Free-living bacteria encode about 2,000 to 5,000 genes")
_au("supertorcido", text="<b>Bacterial DNA</b> is negatively {{c1::supercoiled}}, which compacts it and eases <b>strand separation</b>",
    extra="- DNA gyrase (topoisomerase II) uses ATP to add negative supercoils<br>- Topoisomerase I relaxes them")
_au("sos", text="In the <b>SOS response</b>, RecA activated by single-stranded DNA triggers self-cleavage of the {{c1::LexA}} repressor, derepressing <b>DNA repair genes</b>")
_au("fotoliase", extra="- Pyrimidine dimers are the only DNA lesion that visible light reverses, with no nucleotides removed")
_au("sentido-errado", extra="- Insertions or deletions not in multiples of three shift the reading frame")
_au("uv-bloqueia", extra="- Covalent bonds join adjacent pyrimidines on the same strand")
_au("transf-especies", extra="- E. coli is transformed in the lab after CaCl₂ treatment<br>- There is a limit to how much DNA a cell can take up")
_ak("lisogenico", text="The {{c1::lysogenic::lytic or lysogenic}} cycle is when a phage injects its genetic material into the bacterial cell and it is incorporated into the host DNA")
# clozes que entregavam a resposta
_au("hfr-def", text="A cell with the <b>F plasmid</b> integrated into its <b>chromosome</b> is called a(n) {{c1::Hfr}} cell", extra="- Hfr means high frequency of recombination")
_au("plasmideo-perda", text="{{c1::Low-copy-number}} <b>plasmids</b> can be lost during <b>cell division</b>, so some daughter cells end up without them")
_au("lesao-destino", text="When <b>lesions</b> overwhelm repair, the polymerase loses <b>proofreading</b> and inserts any base, a process called {{c1::lesion tolerance}} that generates mutants",
    extra="- Without any repair the cell dies, and with correct repair the DNA is restored")
_au("reparo-recombinacional", text="In the dark, {{c1::recombinational}} repair uses the intact <b>sister copy</b> present after replication to fix a damaged <b>strand</b>")
_ak("hfr-genoma", text="When high frequency strains of bacteria undergo conjugation, they transfer their {{c1::chromosomal}} genome with the plasmid to the recipient", extra="- Hfr × F⁻ conjugation")
_ak("hfr-mapa", text="Conjugation of high-frequency bacterial strains allows {{c1::genetic mapping}}")
_au("transposon-estabilidade", text="When a <b>transposon</b> moves from a plasmid to the <b>chromosome</b>, the resistance it carries becomes more {{c1::stable}}",
    extra="- It is no longer lost when the plasmid is lost")
_au("mutantes-aplicacao", text="<b>Radiation and mutagens</b> can be used to obtain <b>mutants</b> with higher production of {{c1::antibiotics}}")
# Davi: nucleoide sem o detalhe de HU/H-NS na frente; estrutura do DNA é aula de Biologia Molecular
_au("nucleoide", text="The <b>bacterial chromosome</b> is packed into a compact {{c1::nucleoid}}, which has no membrane around it",
    extra="- Proteins such as HU and H-NS help compact it")
SAI = {"nucleotideo", "pontes-hidrogenio", "fosfodiester", "purinas-pirimidinas", "dna-antiparalelo", "gc-tm", "desnaturacao", "renaturacao",
       "integron", "lisogenia-toxina", "uv-dimeros", "transposicao"}
CARDS[:] = [c for c in CARDS if c["key"] not in SAI]
# detalhe específico vira rosa; fundamento de Biologia Molecular fica azul (F-20261011-CLAUDE-04)
for k in ("replicacao-velocidade", "replicacao-teta", "oric-sequencias", "pol2-reparo", "pol1-exonuclease", "ssb", "mutacao-tautomero", "xeroderma", "transf-especies",
          "hfr-mapa", "tn10", "tn5", "is-classe1", "difteria-profago", "dna-tamanho", "puc18", "cas1-cas2", "plasmideo-promiscuo", "griffith", "sos", "lederberg-tatum"):
    c = _c(k); c["flags"] = {n: R for n in c["flags"]}
    if c["kind"] == "text": c["clinica_lateral"] = True
for k in ("topoisomerase", "girase", "helicase", "primase", "pol3-alonga", "pol3-revisao", "ligase", "silenciosa", "sem-sentido", "fase-leitura", "ner", "excisao-endonuclease"):
    c = _c(k); c["flags"] = {n: Z for n in c["flags"]}; c["clinica_lateral"] = True
# lacunas
_L = lambda key, text, cor, bloco, alvo, slide, autoria, extra, esp: CARDS.append(au(key, text, cor, bloco, alvo, slide, autoria, "sem card nos acervos.", esp, "Revisão do Opus.", extra=extra))
_L("okazaki", "The <b>lagging strand</b> is synthesized discontinuously as {{c1::Okazaki fragments}}, while the leading strand is continuous", Z, C_, "Fita atrasada e fragmentos de Okazaki", "22", "central", "- DNA ligase joins the fragments", [1467771897291, 1467771834622])
_L("tres-mecanismos", "Transfer of <b>naked DNA</b> is {{c1::transformation}}, phage-mediated transfer is {{c2::transduction}} and transfer that requires <b>cell contact</b> is {{c3::conjugation}}", V, E_, "Três mecanismos de transferência", "28", "central", "- Only transformation is blocked by DNase in the medium", [1500738431745, 1500673825876])
_L("destino-receptor", "In F⁺ × F⁻ mating the recipient becomes F⁺, whereas in <b>Hfr × F⁻</b> mating the recipient usually stays {{c1::F⁻}}", Z, E_, "Destino do receptor na conjugação", "34", "central", "- The F sequence is transferred last and the mating breaks first", [1500674026608, 1500674235789])
_L("epissomo", "A <b>plasmid</b> that can integrate into the <b>bacterial chromosome</b> is called a(n) {{c1::episome}}", R, E_, "Epissomo", "34", "lateral", "- Conjugative plasmids tend to be large and low-copy", [1500674026608, 1500673915770])
_L("restricao-modificacao", "<b>Restriction–modification</b> systems let bacteria cut unmethylated {{c1::phage}} DNA while methylating their own", Z, H_, "Restrição-modificação como defesa antifago", "43", "central", "- Restriction enzymes evolved for this defense", [1468549176064, 1468549155531])
CARDS.append(sh(1791664581433, "azul", H_, "Alolactose é o indutor do operon lac", 41, "Azul: lâmina 41, card do Operon."))
CARDS.append(sh(1791664579655, "azul", H_, "CAP liga o sítio CAP com cAMP", 41, "Azul: lâmina 41, card do Operon."))

_c("hfr-genoma")["flags"] = {1: R}

DUPLICACAO.update({"genoma-cromossomal": "ganho: identidade da espécie pelo DNA cromossomal", "tres-mecanismos": "ganho: diferença decisiva entre os três mecanismos (lâmina 28)"})
for c in CARDS:
    if c["key"] in DUPLICACAO: c["duplicacao_ok"] = DUPLICACAO[c["key"]]

# Revisão pontual Codex 12/10/2026 — evidência em revisao-pontual-claude-2026-10-12
_AJUSTES_CODEX_1210 = {'tn3': {'fields_override': {},
         'motivo': 'Associação nominal Tn3–ampicilina é detalhe, como Tn5/Tn9/Tn10; mecanismo geral permanece.',
         'flags': {1: 5}},
 'planar-etidio': {'fields_override': {'Text': 'Planar <b>DNA mutagens</b> can {{c1::intercalate}} between '
                                               'adjacent base pairs',
                                       'Extra': '- Ethidium bromide is an example.<br>- Insertion between base '
                                                'pairs distorts the DNA structure and can disrupt accurate '
                                                'replication.'},
                   'motivo': 'Troca nome específico do exemplo por mecanismo ensinável; exemplo passa ao Extra.'}}
for _c in CARDS:
    if _c["key"] in _AJUSTES_CODEX_1210:
        _fix = _AJUSTES_CODEX_1210[_c["key"]]
        _c.setdefault("fields_override", {}).update(_fix["fields_override"])
        _c["motivo"] = _fix["motivo"]
        if "flags" in _fix: _c["flags"] = _fix["flags"]
        if _fix.get("clinica_lateral"): _c["clinica_lateral"] = True
        if _fix.get("metadata"): _c.update(_fix["metadata"])
