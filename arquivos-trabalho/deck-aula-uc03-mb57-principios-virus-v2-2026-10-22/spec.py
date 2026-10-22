# Especificação curada — 57 Princípios gerais dos vírus (UC03 P3, Microbiologia; Prof. Enrique Boccardo; 127 lâminas = Propriedades
# Gerais dos Vírus I (1–73) + II (74–127, repetição da I sem a história)). Refação 22/10 pelo pipeline da compreensão (F-20261022-CLAUDE-06):
# o deck nasce de compreensao-aula.json e segue os blocos das lâminas, princípio antes do exemplo; famílias e doenças só como exemplo.
# História do deck: o agente que passava pelo filtro e escapava a Koch → o que é um vírus (montado, sem ribossomo) → o que só ele tem na
# tabela → como se classifica (traços do vírion; caminho até o mRNA) → como é construído (genoma, capsídeo, simetrias, cinco estruturas)
# → o que ele carrega e o envelope (brotamento, glicoproteínas, fragilidade → transmissão) → todo genoma viaja empacotado num vírion.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 5  # 5 = compreensao-aula.json + fidelidade ao slide; autoral sem teto, cada um com lacuna provada em todos os acervos
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb57-20261022a"
SHORT = "mb57v"
LESSON = "2026-uc03-microbiologia-57-principios-gerais-virus"
DECK = "NEBLI::UC03::P3::Microbiologia::Princípios gerais dos vírus"
CRITERIOS = "MEMORY.md §2/§3/§5/§6/§7/§8 + FEEDBACKS até F-20261022-CLAUDE-06 + EXEMPLARES/ANTI-EXEMPLARES regenerados, 22/10/2026"
MEDIA = {f"mb57-{n}.jpg": f"img/mb57-{n}.jpg" for n in ("baltimore", "estruturas")}
IMG = lambda n, w=460: f'<img src="mb57-{n}.jpg" width="{w}">'
BUSCA = ("Três caminhos (22/10): seções de recurso do AnKing (estrutura e genomas virais do FirstAid, Physeo e Bootcamp; Mycoplasma, Rickettsia e "
         "Chlamydia lidas; busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em AnKing, nos 9 acervos "
         "externos e no NEBLI vivo, uma consulta por conceito da compreensão da aula (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


_58 = "replicação (local, polimerases, estratégia de cada grupo): aula 58 Multiplicação viral"
_61 = "corpúsculos de inclusão e doença: aula 61 Patologia da infecção viral"
_FAM = "detalhe de família (poxvírus): a aula usa o poxvírus só como exemplo de simetria complexa, coberto por ak1502572273268"
EXCLUIDOS = [
 (1502065688092, "vacinas recombinantes de HBV e HPV: imunologia/vacinas, fora das lâminas"),
 (1502066053913, "vacina da hepatite B: imunologia/vacinas, fora das lâminas"),
 (1502152021975, _58), (1483913062659, _58), (1502570386887, _58), (1502570452327, _58),
 (1502064208990, "equivalente a ak1502064281478 (RNA positivo funciona como mRNA), que entra; dois cards do mesmo fato sem ganho"),
 (1516320933265, "repete ak1502063700798 (genomas de RNA são de fita simples)"),
 (1502064476771, "orientação 5'→3' do RNA positivo: detalhe de biologia molecular que a aula não dá"),
 (1502064737111, "orientação 3'→5' do RNA negativo: detalhe de biologia molecular que a aula não dá"),
 (1523806216737, "rearranjo (reassortment): genética viral, aula 58"), (1523806616492, "rearranjo (reassortment): genética viral, aula 58"),
 (1523926575639, "rearranjo em vírus segmentados: genética viral, aula 58; aqui o genoma segmentado entra em au-genoma-tipos"),
 (1500739563441, "ciclo lítico dos fagos: aula 34 Genética bacteriana"), (1500739784197, "ciclo lisogênico: aula 34 Genética bacteriana"),
 (1500739908171, "fago virulento: aula 34"), (1500739979224, "fago temperado: aula 34"),
 (1502570163043, _FAM), (1502570324908, _FAM), (1502570911606, _FAM), (1502570964320, _FAM + "; tamanho de família"),
 (1502571002064, "varíola como poxvírus: a aula cita a varíola só na história (Ramsés V)"),
 (1502570605009, _61), (1502571454317, _61), (1502571972870, _61), (1516475620459, _61), (1516475827100, _61),
]
FORA_DO_RECORTE = [
 "Fatos curiosos, mortes por causa e mapa de infecções (lâminas 1–7) e múmias com pólio e varíola (8–11): motivação (resposta de Davi em 22/10).",
 "Famílias de vírus e ICTV (lâminas 31–37, 41–42, 46–49, 69): exemplos dos critérios; as famílias citadas ficam nos versos.",
 "Vírus gigantes (lâmina 50) e ebolavírus (60): exemplos de tamanho e de nucleocapsídeo helicoidal, no verso.",
 "Proteínas do HIV (lâmina 66) e hemaglutinina/neuraminidase (65): exemplos de componentes do vírion, no verso; HIV e influenza têm aulas e cards próprios.",
 "Rickettsia e Chlamydia sem ATP (ak1402344288287, ak1506273247348, ak1500499548289): contradizem a lâmina 25, em que a Rickettsia tem metabolismo gerador de ATP; a formulação da aula é a correta (só a Chlamydia é parasita energético).",
 "A parte II (lâminas 74–127) repete a parte I; o inventário aponta para os mesmos cards.",
]
B_, A_, T_, C_, D_, E_, F_, G_, H_ = ("B-historia", "A-definicao", "T-comparacao", "C-classificacao", "D-componentes", "E-estruturas",
                                      "F-outros-componentes", "G-envelope", "H-resumo")

CARDS = [
 # ---------- Como se chegou ao vírus (lâminas 12–20) ----------
 sh(1791746115401, "azul", B_, "Postulados de Koch exigem cultura pura", 13, "A-aula: lâminas 12–13; card da 35"),
 au("au-koch-virus", "Viruses could not fulfill <b>Koch's postulates</b> because they grow only inside {{c1::living cells}}, never in pure culture",
    "V-pilar", B_, "Vírus escapam aos postulados de Koch", 13, "lâminas 12–13; apostila UC3 e guia de Micro (os postulados não explicam os vírus, que só crescem em culturas celulares)",
    extra="- Postulate II asks to grow the agent in pure culture on artificial media<br>"
          "- Iwanowski (1892) and Beijerinck (1898) showed the tobacco mosaic agent passes bacterial filters, and Loeffler and Frosch found the same in foot-and-mouth disease"),
 sh(1791666344216, "azul", B_, "Filtro de 0,22 µm retém bactérias e deixa passar vírus", 15, "A-aula: lâmina 15 (filtros de cerâmica de Iwanowski) e lâmina 27 (passa por filtros); card da 30"),
 K(1500738380739, "A-aula", B_, "Bacteriófago: vírus que infecta bactérias", 20, "lâmina 20 (Twort e d'Herelle); seção Bootcamp"),
 # ---------- Definição (lâmina 21) ----------
 K(1556156067303, "A-aula", A_, "Vírus: partícula de proteína e DNA ou RNA que infecta célula viva", 21, "lâmina 21 (definição)", origin="MCAT"),
 K(1554006092985, "A-aula", A_, "Vírion: a partícula viral completa, fora da célula", 21, "lâminas 21 e 51 (vírions); Jawetz cap. 29 (vírion = partícula completa)", origin="MCAT"),
 au("au-montado", "<b>Virions</b> do not grow or divide, because each new particle is {{c1::assembled}} from components the host cell made",
    "V-pilar", A_, "Vírion é montado, não cresce nem se divide", 21, "lâmina 21 (montadas a partir de componentes preexistentes); apostila UC3 (linha de montagem)",
    extra="- Bacteria and fungi grow by adding components and then divide<br>- The viral genome makes the cell produce the parts, like an assembly line"),
 au("au-ribossomo", "Viruses are obligate intracellular parasites because they have no {{c1::ribosomes}} and no ATP-generating metabolism",
    "V-pilar", A_, "Sem ribossomo nem metabolismo: parasita intracelular obrigatório", 21, "lâmina 21 (carecem da informação para energia e síntese proteica); apostila UC3",
    extra="- They must use the host's translation machinery and energy<br>- So to understand a virus we must understand the cell it infects"),
 K(1502063041178, "A-aula", A_, "Vírus sem atividade metabólica própria", 21, "lâmina 21; seção FirstAid"),
 # ---------- Comparação com outros microrganismos (lâminas 22–27) ----------
 sh(1791576675192, "azul", T_, "Mycoplasma sem parede (sem ácido murâmico)", 24, "A-aula: lâmina 24 (ácido murâmico: não); card da 26"),
 K(1500030503730, "A-aula", T_, "Rickettsia é intracelular obrigatória", 25, "lâmina 25 (não cresce em meio artificial)"),
 K(1501983641086, "A-aula", T_, "Chlamydia não produz o próprio ATP", 26, "lâmina 26 (metabolismo gerador de ATP: não)"),
 K(1690899377178, "A-aula", T_, "Chlamydia sem ácido murâmico na parede", 26, "lâmina 26 (ácido murâmico: não)"),
 au("au-tabela", ORG("<b>Only viruses</b>, unlike Mycoplasma, Rickettsia and Chlamydia:<br>- one {{c1::nucleic acid}} type<br>"
                     "- no {{c1::binary fission}}<br>- no {{c2::antibiotic}} effect<br>- blocked by {{c2::interferon}}"),
    "V-pilar", T_, "O que só o vírus tem na tabela comparativa", 27, "lâmina 27 (coluna dos vírus); monitoria P3 (sensíveis a interferon, não a antibióticos)",
    extra="- Antibiotics hit bacterial targets such as the wall and ribosomes, which viruses lack<br>- Viruses also pass through bacteriological filters"),
 # ---------- Classificação (lâminas 28–42) ----------
 au("au-hierarquico", ORG("<b>Hierarchical classification</b> uses four virion features:<br>- {{c1::nucleic acid}} type<br>"
                          "- capsid {{c1::symmetry}}<br>- {{c2::envelope}}<br>- virion {{c2::size}}"),
    "A-aula", C_, "Classificação hierárquica: quatro características", 30, "lâminas 29–30 (Lwoff, Horne e Tournier, 1962); monitoria P3",
    extra="- Viruses are grouped by their own features, not by the cells they infect<br>- Family names end in -viridae, as in Picornaviridae and Herpesviridae"),
 au("au-baltimore", "Since every virus depends on the host's ribosomes, the <b>Baltimore system</b> groups viruses by how their genome produces {{c1::mRNA}}",
    "V-pilar", C_, "Baltimore: o caminho do genoma até o mRNA", 38, "lâmina 38 (dependência absoluta da tradução celular; todo vírus produz mRNA); monitoria P3",
    extra="- This is why the type of genome decides the first steps of infection<br>- The hierarchical system looks at the particle, Baltimore at the strategy"),
 au("au-baltimore-grupos", ORG("<b>Baltimore groups</b>:<br>- I: dsDNA<br>- II: {{c1::ssDNA}}<br>- III: {{c1::dsRNA}}<br>- IV: {{c2::(+) ssRNA}}<br>"
                               "- V: {{c2::(-) ssRNA}}<br>- VI and VII: {{c3::reverse transcriptase}}"),
    "V-pilar", C_, "Os sete grupos de Baltimore", 39, "lâminas 39–40; provas 2018 P3 1.3 (febre amarela, grupo IV) e 2015 P2 2.3 (grupo de Baltimore)",
    extra="- VI is an RNA virus (retrovirus) and VII a DNA virus (hepatitis B)<br>" + IMG("baltimore")),
 K(1502064066857, "V-prova", C_, "RNA de polaridade positiva ou negativa", 39, "lâminas 39–40; prova 2015 P2 4.5 (RNA fita simples positivo); seção FirstAid"),
 K(1502064281478, "A-aula", C_, "RNA positivo é traduzido de imediato", 39, "lâminas 39 e 70 (o RNA de fita simples pode funcionar como mRNA?)"),
 K(1502064367585, "A-aula", C_, "RNA negativo precisa virar positivo antes", 39, "lâmina 39 (grupo V)"),
 K(1467683646912, "A-aula", C_, "Transcrição reversa: RNA → DNA", 39, "lâmina 39 (grupos VI e VII)"),
 # ---------- Tamanho e componentes (lâminas 43–53) ----------
 sh(1791576666292, "azul", D_, "Vírus de 20–200 nm, só ao microscópio eletrônico", 44, "A-aula: lâminas 21 (submicroscópicos) e 44–50; card da 26"),
 K(1502062962846, "A-aula", D_, "DNA ou RNA dentro do capsídeo", 51, "lâmina 51 (componentes virais); seção FirstAid"),
 au("au-capsomero", "The viral capsid is a protein shell built from many identical repeating subunits called {{c1::capsomers}}",
    "A-aula", D_, "Capsídeo feito de capsômeros", 51, "lâminas 51 e 56 (capsômeros); apostila UC3 (cada capsídeo é composto por capsômeros); Jawetz cap. 29",
    extra="- Genetic economy: a small genome codes a few proteins that repeat many times<br>- The number of capsomers is one feature of the virion (lâmina 70)"),
 au("au-nucleocapsideo", "The viral <b>genome</b> plus its protein <b>capsid</b> forms the {{c1::nucleocapsid}}, which is the whole virion in naked viruses",
    "V-pilar", D_, "Genoma + capsídeo = nucleocapsídeo", 51, "lâmina 51; prova 2015 P2 4.2 (capsídeo × nucleocapsídeo × envelope)",
    extra="- In enveloped viruses the nucleocapsid sits inside a lipid envelope<br>- The capsid protects the genome from nucleases and helps it enter new cells"),
 au("au-genoma-funcoes", ORG("<b>The viral genome</b> encodes how to:<br>- replicate and {{c1::transcribe}} itself<br>"
                             "- {{c1::package}} itself into virions<br>- alter the {{c2::structure}} of the host cell"),
    "A-aula", D_, "O que o genoma viral garante", 52, "lâmina 52 (os genomas virais contêm informação que...); apostila UC3",
    extra="- The cell supplies ribosomes, energy and building blocks<br>- The virus supplies only the instructions"),
 au("au-genoma-tipos", ORG("<b>Viral genomes</b> vary in:<br>- strands: single or {{c1::double}}<br>- shape: linear or {{c1::circular}}<br>"
                           "- pieces: one molecule or {{c2::segmented}}<br>- RNA polarity: {{c2::positive}} or negative"),
    "A-aula", D_, "Como variam os genomas virais", 53, "lâminas 53 e 70; apostila UC3 (diversidade genômica)",
    extra="- Each virus has only DNA or only RNA<br>- Retroviruses are the diploid exception, with two RNA copies"),
 K(1502065388242, "A-aula", D_, "Genoma de DNA: em geral dupla fita, circular ou linear", 53, "lâmina 53; seção FirstAid"),
 K(1502063700798, "A-aula", D_, "Genoma de RNA: em geral fita simples e linear", 53, "lâmina 53; seção FirstAid"),
 # ---------- Cinco estruturas e simetrias (lâminas 54–64) ----------
 K(1502063077047, "V-prova", E_, "Capsídeo icosaédrico ou helicoidal", 54, "lâminas 51 e 54; prova 2015 P2 4.1 (simetria na ME); seção FirstAid"),
 au("au-cinco", ORG("<b>Five basic structures</b>:<br>- naked icosahedral: {{c1::poliovirus}}<br>- enveloped icosahedral: {{c1::herpesvirus}}<br>"
                    "- naked helical: {{c2::tobacco mosaic virus}}<br>- enveloped helical: {{c2::influenza}}<br>- complex: {{c3::poxvirus}}"),
    "A-aula", E_, "Cinco estruturas básicas, um exemplo de cada", 55, "lâminas 54–55 (cinco estruturas básicas com exemplos); apostila UC3",
    extra="- Each structure combines a capsid symmetry with the presence or absence of an envelope<br>" + IMG("estruturas")),
 au("au-icosaedro", "An icosahedral capsid is a closed shell of {{c1::20}} triangular faces built from capsomers",
    "A-aula", E_, "Icosaedro: 20 faces triangulares", 57, "lâminas 57–58 (simetria icosaédrica); Jawetz cap. 29 (20 faces, 12 vértices); monitoria P3",
    extra="- It is the most efficient way to close a shell with identical subunits<br>- Most icosahedral viruses look spherical under the microscope"),
 au("au-helicoidal", "In helical symmetry, capsid proteins bind along the {{c1::nucleic acid}} and coil with it into a tube",
    "A-aula", E_, "Hélice: proteínas enroladas ao longo do ácido nucleico", 59, "lâminas 59–62 (mosaico do tabaco, VSV, raiva, influenza); Jawetz cap. 29; monitoria P3",
    extra="- Without nucleic acid no helical particle forms, unlike icosahedral capsids<br>- In human viruses the helical nucleocapsid is RNA and is wrapped in an envelope"),
 K(1502063631440, "V-hy", E_, "Todo vírus humano nu é icosaédrico", 61, "lâminas 54 e 61; seção FirstAid"),
 K(1502063652542, "V-prova", E_, "Envelopado: icosaédrico ou helicoidal", 61, "lâminas 54 e 61; prova 2015 P2 4.1 (simetria e envoltório na ME)"),
 K(1502572273268, "A-aula", E_, "Poxvírus: forma de tijolo, simetria complexa", 63, "lâminas 63–64 (simetria complexa); seção Physeo"),
 K(1554005863426, "A-aula", E_, "Bacteriófago: cabeça e cauda que injeta o genoma", 63, "lâmina 63 (fago T, simetria complexa); lâmina 56", origin="MCAT"),
 # ---------- Outros componentes (lâminas 65–66) ----------
 K(1516320850504, "A-aula", F_, "Vírus de RNA negativo trazem a própria RNA polimerase", 65, "lâmina 65 (RNA polimerase do influenza); Jawetz cap. 29"),
 # ---------- Envelope (lâminas 67–69) ----------
 K(1502063659167, "A-aula", G_, "Envelope vem da membrana da célula hospedeira", 68, "lâminas 51 e 67–68 (brotamento); seção FirstAid"),
 K(1502063688789, "V-prova", G_, "Glicoproteínas do envelope: ligação ao receptor e antígeno", 68, "lâminas 67–68; provas 2018 P3 5.2 (importância do envelope) e 2015 P2 4.4 (espículas)"),
 K(1524752474746, "V-prova", G_, "Éter e solventes destroem o envelope", 68, "lâmina 67; prova 2015 P2 4.2 (sensibilidade ao éter e a detergentes); Jawetz cap. 29"),
 K(1525619441985, "A-aula", G_, "Álcool destrói o envelope", 68, "lâmina 67; seção Bootcamp"),
 sh(1791666340816, "azul", G_, "Envelopados: os menos resistentes a desinfetantes", 68, "A-aula: lâminas 67–68; card da 30"),
 au("au-transmissao", "Lacking a lipid envelope, <b>naked viruses</b> survive stomach acid, bile and drying and often spread by the {{c1::fecal-oral}} route",
    "V-prova", G_, "Vírus nu resiste e se transmite por via fecal-oral", 68,
    "lâminas 54 e 67–68; provas 2025 P3 2.3 (por que não ser envelopado), 2024 P3 1.5 e 2019 P3 3.2 (estrutura → via de transmissão)",
    extra="- Enveloped viruses dry out quickly, so they spread by respiratory droplets, sex, blood or direct contact<br>- Poliovirus and hepatitis A are naked and fecal-oral"),
 sh(1791666340691, "azul", G_, "Poliovírus resiste mais que o HIV", 68, "A-aula: exemplo de nu × envelopado (lâminas 54 e 67); card da 30"),
 # ---------- Resumo geral (lâminas 70–72) ----------
 K(1502065503059, "A-aula", H_, "Genoma de RNA negativo sozinho não é infeccioso", 70, "lâmina 70 (caso o RNA seja simples fita, pode funcionar como mRNA?); seção FirstAid"),
 K(1502064775742, "A-aula", H_, "Retrovírus: genoma diploide", 70, "lâmina 70 (se o genoma for diploide: retrovírus); seção FirstAid"),
 au("au-conx-pacote", "Every viral genome travels packaged in a {{c1::virion}}, which protects it and delivers it to a permissive cell",
    "A-aula", H_, "Todo genoma viaja empacotado num vírion", 72, "lâmina 72 (resumo geral); apostila UC3 (resumindo)",
    extra="- Inside the cell the genome has all the instructions to complete the infectious cycle<br>- How it enters, copies itself and leaves is the next lesson"),
]

for c in CARDS:  # F-20261022-CLAUDE-04: a resposta do cloze autoral vai em negrito, como no AnKing
    if c["kind"] == "autoral":
        c["text"] = _re.sub(r"\{\{(c\d+)::(.*?)\}\}", lambda m: m.group(0) if "<b>" in m.group(2) else "{{%s::<b>%s</b>}}" % m.groups(), c["text"])
finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1500738380739": "- Described by Twort (1915) and d'Herelle (1917), who named them bacteriophages",
 "ak1556156067303": "- A virus has only one kind of nucleic acid, never both",
 "ak1502063041178": "- No ribosomes and no ATP generation: they use the host's machinery",
 "ak1500030503730": "- In the lecture's table it does not grow on artificial media, but it still makes its own ATP",
 "ak1501983641086": "- An energy parasite, yet it has DNA, RNA and ribosomes, unlike viruses",
 "ak1690899377178": "- Mycoplasma also lacks muramic acid, but because it has no wall at all",
 "ak1502064066857": "- (+) sense has the same polarity as mRNA, and (−) sense is complementary to it",
 "ak1502064281478": "- This is Baltimore group IV, which goes straight to translation",
 "ak1502064367585": "- This is Baltimore group V: genome → (+) mRNA by the viral polymerase",
 "ak1467683646912": "- Groups VI (retroviruses) and VII (hepatitis B) use reverse transcriptase",
 "ak1502062962846": "- Genome plus capsid is the nucleocapsid",
 "ak1502065388242": "- Exceptions: parvovirus is single-stranded and hepatitis B is partially double-stranded",
 "ak1502063700798": "- Exception: reovirus is double-stranded and segmented",
 "ak1502063077047": "- A third form, complex, has neither simple symmetry (poxvirus, bacteriophage)",
 "ak1502063631440": "- Among human viruses; the plant tobacco mosaic virus is a naked helical virus",
 "ak1502063652542": "- Enveloped icosahedral: herpes, yellow fever, rubella. Enveloped helical: influenza, rabies, measles",
 "ak1502572273268": "- Its large particle has outer and inner membranes and a core with the DNA and many enzymes",
 "ak1554005863426": "- The head is icosahedral and the tail helical, so the whole particle has complex symmetry",
 "ak1516320850504": "- The cell has no RNA-dependent RNA polymerase, so the virion must carry one<br>- Retroviruses such as HIV likewise carry reverse transcriptase, integrase and protease",
 "ak1502063659167": "- Acquired by budding: viral glycoproteins insert into a host membrane (plasma, or nuclear in herpesviruses) and the nucleocapsid buds through it",
 "ak1502063688789": "- These are the spikes (peplomers) seen on electron microscopy<br>- Influenza spikes: hemagglutinin binds sialic acid to enter, neuraminidase releases new virions",
 "ak1525619441985": "- Ether and detergents dissolve the envelope too; naked viruses resist them",
 "ak1502065503059": "- (+) RNA alone can be translated, so purified (+) RNA genomes are infectious",
 "ak1502064775742": "- Two copies of (+) single-stranded RNA in each virion",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (Baltimore, cinco estruturas) estão nos cards do conceito"
SLIDE_SEM_ALT = "esquema da própria aula, sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "mb57-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {
 "au-baltimore": "a resposta mRNA aparece em cards de polaridade, mas aqui o alvo é o critério da classificação de Baltimore",
 "au-cinco": "poliovírus e poxvírus aparecem em outros cards (sh do pólio × HIV, ak do poxvírus); aqui são o exemplo de cada estrutura da lâmina 54",
 "au-hierarquico": "nucleic acid também é resposta em au-tabela; lá é o que só o vírus tem, aqui é o primeiro critério da classificação",
 "au-genoma-tipos": "o AnKing dá a regra de DNA (dupla fita) e de RNA (fita simples); este organiza as quatro dimensões da lâmina 53",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
STRIP_IMG = {  # F-20261022-CLAUDE-01: imagens do Extra que não batem com o cloze
 "ak1502063700798": ["8a5367066fd941f4fb6cb20402b6a809.webp"],  # mapa de famílias de RNA por polaridade, não mostra fita simples nem linear
 "ak1502064775742": ["aacb7afba5b4ddacc0439349e0bb7f71.webp", "2d7ec7fa20c74336b35e28f972bfb3d7.webp", "68e6f2885007cc627dd5019398700852.webp",
                     "37c4dd9b59b4b4bc4eeaf4a11d3aa38c.webp", "dde3cf690b013d1355b1896a1aeaa0d3.webp", "fb1617ebcc759d875ae3dd9119e84256.webp",
                     "84fd1acaab29e290b61207daaa6fc962.webp"],  # quadros da replicação do HIV: aula 58
}
IMAGENS_VISTAS = {
 "Bacteriophage.png": "Esquema do fago T (cabeça com DNA, colar, bainha, placa basal, fibras): mostra a cauda que injeta o genoma do card MCAT.",
 "f9d4abad708094fc63cfa93add96d1b0.png": "Esquema de vírion envelopado (genes de DNA ou RNA, capsídeo, envelope, proteínas): ilustra a definição do card MCAT.",
 "mb57-baltimore.jpg": "Lâmina 40: esquema de Baltimore com os grupos I–VII convergindo para o +mRNA; verso de au-baltimore-grupos.",
 "mb57-estruturas.jpg": "Lâmina 55: cinco tipos de simetria (icosaédrica, icosaédrica envelopada, helicoidal, helicoidal envelopada, complexa); verso de au-cinco.",
}
REVISAO = {"despejo": "Despejo lido inteiro em 22/10 (42 notas novas, 57 cards; frentes, clozes, versos, imagens e cores conferidos; as duas imagens retiradas saíram). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Acompanhar a aula: o vírus definido pelo que lhe falta (montado, sem ribossomo, intracelular obrigatório), separado dos outros microrganismos, "
             "classificado pelos traços do vírion e pelo caminho até o mRNA, e desmontado em genoma, capsídeo, simetrias, envelope e componentes.",
 "centrais": [
   ("definição", "au-montado", "au-ribossomo", "ak1502063041178"),
   ("por que o vírus escapa a Koch", "au-koch-virus"),
   ("tabela comparativa", "au-tabela"),
   ("classificação", "au-hierarquico", "au-baltimore-grupos"),
   ("baltimore", "au-baltimore", "ak1502064066857"),
   ("estrutura", "au-nucleocapsideo", "au-genoma-tipos"),
   ("simetrias", "ak1502063077047", "ak1502063652542", "au-cinco"),
   ("envelope", "ak1502063659167", "ak1502063688789", "ak1524752474746", "au-transmissao"),
 ],
 "exemplos": ["múmias com poliomielite e varíola", "fatos curiosos dos fagos", "famílias e ICTV", "proteínas do HIV e do influenza", "vírus gigantes", "ebolavírus"],
 "outras_aulas": [("replicação viral e rearranjo", "58 Multiplicação viral"), ("inclusões virais", "61 Patologia da infecção viral"),
                  ("ciclo lítico e lisogênico dos fagos", "34 Genética bacteriana"), ("Koch", "35 Patogenicidade bacteriana (sh)"),
                  ("filtros e desinfetantes", "30 Controle microbiológico (sh)"), ("Mycoplasma e tamanho", "26 Morfologia bacteriana (sh)"),
                  ("interferon e resposta antiviral", "63 Resposta imune a vírus")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
