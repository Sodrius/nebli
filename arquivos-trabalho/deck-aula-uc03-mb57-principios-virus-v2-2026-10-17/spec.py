# Especificação curada — 57 Princípios gerais dos vírus (UC03 P3, Microbiologia; Prof. Enrique Boccardo; 127 lâminas = Propriedades
# Gerais dos Vírus I (1–73) + II (74–127, repetição da I)). Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# Seções AnKing de estrutura e genoma viral declaradas (FirstAid, Physeo, Bootcamp): toda nota entra ou sai com motivo (replicação → 58,
# patologia das inclusões → 61, vacinas → imuno, bacteriófagos → 34). Cópias NEBLI vivas das aulas 26, 30, 34 e 35 entram por sh().
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb57-20261017a"
SHORT = "mb57n"
LESSON = "2026-uc03-microbiologia-57-principios-gerais-virus"
DECK = "NEBLI::UC03::P3::Microbiologia::Princípios gerais dos vírus"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"mb57-{n}.jpg": f"img/mb57-{n}.jpg" for n in ("baltimore", "estruturas")}
IMG = lambda n, w=460: f'<img src="mb57-{n}.jpg" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (estrutura viral, genomas de DNA e RNA, características dos vírus de DNA, "
         "Physeo estruturas e genomas, Bootcamp organização viral; busca/secoes); palavra-chave em AnKing e Referências Externas "
         "(busca/anking.txt: Baltimore, nucleocapsid, capsid, envelope, naked, Koch, interferon, Mycoplasma/Chlamydia/Rickettsia, "
         "parvovirus, poxvirus, hemagglutinin, HIV gag/env/pol); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
_58 = "replicação (local, polimerases): aula 58 Multiplicação viral"
_61 = "corpúsculos de inclusão e doença clínica: aula 61 Patologia da infecção viral"
EXCLUIDOS = [
 (1502152021975, _58), (1483913062659, _58), (1502570386887, _58), (1502570452327, _58),
 (1502065688092, "vacinas recombinantes: imunologia/vacinas, fora das lâminas"), (1502066053913, "vacina da hepatite B: imunologia, fora das lâminas"),
 (1500739563441, "ciclo lítico dos fagos: aula 34 Genética bacteriana"), (1500739784197, "ciclo lisogênico: cópia viva na 34 Genética bacteriana"),
 (1500739908171, "fago virulento: aula 34"), (1500739979224, "fago temperado: aula 34"),
 (1502570605009, _61), (1502571454317, _61), (1502571972870, _61), (1516475620459, _61), (1516475827100, _61),
 (1502571002064, "varíola como membro dos poxvírus: a aula cita a varíola só na história (Ramsés V)"),
 (1516320933265, "repete ak-rna-ss (genomas de RNA são de fita simples)"),
 (1523806216737, "reassortment em detalhe: genética viral, aula 58"), (1523806616492, "reassortment em detalhe: genética viral, aula 58"),
 (1502064476771, "orientação 5'→3' do RNA positivo: detalhe de biologia molecular sem cobrança"),
 (1502064737111, "orientação 3'→5' do RNA negativo: detalhe de biologia molecular sem cobrança"),
 (1506273247348, "contradiz a lâmina 25 (Rickettsia tem metabolismo gerador de ATP; a Chlamydia é que não tem)"),
 (1500499548289, "generaliza a falta de ATP a todas as intracelulares obrigatórias, o que contradiz a lâmina 25 (Rickettsia)"),
]
FORA_DO_RECORTE = [
 "Fatos curiosos (massa dos fagos, mortes por causa) e história (múmias, Mayer, Iwanowski, Beijerinck, Loeffler e Frosch, Twort): ilustração; entram Koch e o fago.",
 "Taxonomia do ICTV (ordem, família, gênero, espécie) e tamanhos/genomas de cada família: Tab (§4).",
 "A parte II (lâminas 74–127) repete a parte I lâmina a lâmina; o inventário aponta para os mesmos cards.",
]
A_, B_, C_, D_, E_ = "A-definicao-comparacao", "B-historia", "C-classificacao", "D-estrutura", "E-envelope-componentes"

CARDS = [
 # ---------- B. História (lâminas 12–20) ----------
 sh(1791746115401, "azul", B_, "Postulados de Koch", 13, "A-aula: lâminas 12–13; card da 35"),
 ak("ak-fago", 1500738380739, "A-aula", B_, "Bacteriófago infecta bactérias", 20, "lâmina 20 (Twort e d'Herelle)"),
 # ---------- A. Definição e comparação (lâminas 21–27) ----------
 au("au-definicao", "<b>Viruses</b> never grow or divide, because each new virion is {{c1::assembled}} from preformed components",
    "V-pilar", A_, "Vírion é montado, não cresce nem se divide", 21, "lâmina 21 (definição); resumo geral (lâmina 72)",
    extra="- They lack ribosomes and ATP-generating metabolism, so they are obligate intracellular parasites<br>"
          "- To understand a virus one must understand the cell it infects"),
 ak("ak-sem-metabolismo", 1502063041178, "A-aula", A_, "Vírus sem atividade metabólica", 21, "lâminas 21 e 27; seção FirstAid"),
 sh(1791576666292, "azul", A_, "Vírus de 20–200 nm, só ao microscópio eletrônico", 21, "A-aula: lâminas 21 (submicroscópicos) e 44; card da 26"),
 sh(1791576675192, "azul", A_, "Mycoplasma sem parede celular", 24, "A-aula: lâmina 24 (sem ácido murâmico); card da 26"),
 ak("ak-rickettsia", 1500030503730, "A-aula", A_, "Rickettsia é intracelular obrigatória", 25, "lâmina 25 (não cresce em meio artificial)"),
 ak("ak-rickettsia-coa", 1500030789039, "R-detalhe", A_, "Rickettsia não produz CoA nem NAD⁺", 25, "lâmina 25 (depende da célula, mas gera ATP)"),
 ak("ak-chlamydia-atp", 1501983641086, "V-hy", A_, "Chlamydia não produz ATP", 26, "lâmina 26 (metabolismo gerador de ATP: não)"),
 sh(1791576673916, "rosa", A_, "Intracelulares coram mal pelo Gram", 26, "R-detalhe: lâminas 25–26; card da 26"),
 ak("ak-interferon", 1556144067381, "A-aula", A_, "Interferon interfere na replicação viral", 27, "lâmina 27 (vírus: sensíveis a interferon, não a antibióticos)", origin="MCAT"),
 sh(1791666344216, "azul", A_, "Filtro de 0,22 µm deixa passar vírus", 27, "A-aula: lâminas 15 e 27 (passa por filtros bacteriológicos); card da 30"),
 # ---------- C. Classificação (lâminas 28–42) ----------
 au("au-hierarquico", "The hierarchical classification groups <b>viruses</b> by nucleic acid, {{c1::capsid symmetry}}, envelope and virion size",
    "A-aula", C_, "Classificação hierárquica: 4 critérios", 30, "lâminas 29–30 (Lwoff, Horne e Tournier, 1962)",
    extra="- Viruses are grouped by their own features, not by the cells they infect<br>- Order → family → genus → species (ICTV)"),
 au("au-baltimore", "The <b>Baltimore classification</b> groups viruses by the route each genome takes to make {{c1::mRNA}}",
    "V-prova", C_, "Classificação de Baltimore: caminho até o mRNA", 38, "lâminas 38–42; provas 2018 P3 1.3 (febre amarela, grupo IV) e 2015 P2 2.3",
    extra="- I dsDNA · II ssDNA · III dsRNA · IV (+)ssRNA · V (−)ssRNA · VI ssRNA-RT (retrovirus) · VII dsDNA-RT (hepatitis B)<br>"
          "- Every virus depends on the cell's translation machinery<br>" + IMG("baltimore")),
 ak("ak-polaridade", 1502064066857, "V-prova", C_, "RNA de polaridade + ou −", 39, "lâminas 39–40; prova 2015 P2 4.5 (RNA fita simples positivo); seção FirstAid"),
 ak("ak-rna-mrna", 1502064208990, "A-aula", C_, "RNA + tem a estrutura do mRNA", 39, "lâminas 39 e 70 (o RNA pode funcionar como mRNA?)"),
 ak("ak-rna-mais-uso", 1502064281478, "A-aula", C_, "RNA + é traduzido de imediato", 39, "lâmina 39 (grupo IV direto ao mRNA)"),
 ak("ak-rna-menos", 1502064367585, "A-aula", C_, "RNA − precisa virar + antes", 39, "lâmina 39 (grupo V)"),
 ak("ak-rna-menos-pol", 1516320850504, "A-aula", C_, "RNA − carrega a própria RNA polimerase", 39, "lâminas 39 e 65 (polimerase no vírion)"),
 ak("ak-rna-menos-infec", 1502065503059, "A-aula", C_, "Genoma RNA − sozinho não é infeccioso", 39, "lâmina 39; seção FirstAid"),
 ak("ak-transcricao-reversa", 1467683646912, "A-aula", C_, "Transcrição reversa: RNA → DNA", 39, "lâmina 39 (grupos VI e VII)"),
 # ---------- D. Estrutura (lâminas 43–64) ----------
 ak("ak-parvo-menor", 1516927385593, "V-hy", D_, "Parvovírus: menor vírus de DNA", 46, "lâminas 45–46 (tamanho relativo)"),
 ak("ak-pox-maior", 1502570964320, "A-aula", D_, "Poxvírus: maior vírus de DNA", 46, "lâminas 44–46 e 50; seção Physeo"),
 au("au-nucleocapsideo", "The viral <b>genome</b> plus its protein <b>capsid</b> forms the {{c1::nucleocapsid}}, sometimes wrapped in an envelope",
    "V-pilar", D_, "Genoma + capsídeo = nucleocapsídeo", 51, "lâmina 51 (componentes virais); prova 2015 P2 4.2 (capsídeo × nucleocapsídeo × envelope)",
    extra="- The capsid is built of capsomeres<br>- The envelope comes from host cell membranes"),
 ak("ak-capsideo", 1502062962846, "A-aula", D_, "DNA ou RNA dentro do capsídeo", 51, "lâmina 51; seção FirstAid"),
 ak("ak-dna-genoma", 1502065388242, "V-hy", D_, "Genoma de DNA: circular ou linear, em geral dupla fita", 53, "lâmina 53; seção FirstAid"),
 ak("ak-parvo-ss", 1516927536764, "V-hy", D_, "Parvovírus: único DNA de fita simples", 53, "lâmina 53 (simples fita)"),
 ak("ak-rna-ss", 1502063700798, "V-hy", D_, "Genoma de RNA: fita simples e linear", 53, "lâmina 53; seção FirstAid"),
 ak("ak-reo-ds", 1516321085226, "V-hy", D_, "Reovírus: RNA de dupla fita", 53, "lâmina 53 (double stranded segmented)"),
 ak("ak-segmentado", 1523926575639, "V-hy", D_, "Vírus segmentados fazem rearranjo", 53, "lâmina 53 (segmentado); seção Bootcamp"),
 ak("ak-formas", 1502063077047, "A-aula", D_, "Capsídeo icosaédrico ou helicoidal", 54, "lâminas 54–60; seção FirstAid"),
 au("au-estruturas", ORG("<b>Viral structures</b>:<br>- naked icosahedral: {{c1::poliovirus}}<br>- enveloped icosahedral: {{c2::herpesvirus}}<br>"
    "- naked helical: {{c3::tobacco mosaic virus}}<br>- enveloped helical: {{c4::influenza}}<br>- complex: {{c5::poxvirus}}"),
    "A-aula", D_, "Cinco estruturas básicas com exemplos", 54, "lâminas 54–55 (cinco estruturas básicas)",
    extra="- Other examples: adenovirus and hepatitis A (naked icosahedral), yellow fever (enveloped icosahedral), rabies and measles (enveloped helical)<br>" + IMG("estruturas")),
 ak("ak-nus-icosa", 1502063631440, "V-hy", D_, "Todo vírus nu é icosaédrico", 54, "lâmina 54; seção FirstAid"),
 ak("ak-envelopados-forma", 1502063652542, "V-prova", D_, "Envelopado: icosaédrico ou helicoidal", 54, "lâminas 54 e 61; prova 2015 P2 4.1 (simetria e envoltório na ME)"),
 ak("ak-helicoidais-menos", 1516663881703, "A-step", D_, "RNA − de capsídeo helicoidal: seis famílias", 61, "lâminas 61–62 (raiva, influenza, sarampo, caxumba)"),
 ak("ak-pox-dna", 1502570163043, "A-aula", D_, "Poxvírus: dsDNA linear envelopado", 63, "lâminas 63–64; seção Physeo"),
 ak("ak-pox-tijolo", 1502572273268, "A-aula", D_, "Poxvírus: forma de tijolo, sem simetria icosaédrica", 63, "lâminas 63–64 (simetria complexa); seção Physeo"),
 ak("ak-pox-halter", 1502570911606, "R-detalhe", D_, "Poxvírus: núcleo em halter", 64, "lâmina 64 (core do poxvírus); seção Physeo"),
 ak("ak-pox-envelope", 1502570324908, "R-detalhe", D_, "Poxvírus faz o próprio envelope", 64, "lâmina 64; seção Physeo"),
 # ---------- E. Outros componentes e envelope (lâminas 65–72) ----------
 ak("ak-ha", 1516323222471, "V-hy", E_, "Hemaglutinina liga ácido siálico", 65, "lâmina 65 (hemaglutinina e neuraminidase do influenza)"),
 ak("ak-na", 1516401726231, "V-hy", E_, "Neuraminidase libera o vírion", 65, "lâmina 65"),
 ak("ak-hiv-p24", 1502147310499, "V-hy", E_, "p24: capsídeo do HIV", 66, "lâmina 66 (componentes do HIV)"),
 ak("ak-hiv-env", 1502066575758, "V-hy", E_, "env: gp120 e gp41", 66, "lâmina 66"),
 ak("ak-hiv-pol", 1502066968224, "V-hy", E_, "pol: transcriptase reversa, protease, integrase", 66, "lâmina 66"),
 ak("ak-envelope", 1502063659167, "A-aula", E_, "Envelope vem da membrana da célula", 67, "lâminas 51, 67–68 (brotamento); seção FirstAid"),
 ak("ak-glicoproteinas", 1502063688789, "V-prova", E_, "Glicoproteínas do envelope: ligação e antígeno", 67, "lâminas 67–68; provas 2018 P3 5.2 (importância do envelope), 2015 P2 4.4 (espículas)"),
 ak("ak-alcool", 1525619441985, "V-prova", E_, "Álcool destrói o envelope", 67, "lâmina 67; prova 2015 P2 4.2 (sensibilidade ao éter e a detergentes)"),
 sh(1791666340816, "azul", E_, "Envelopados: os menos resistentes a desinfetantes", 67, "A-aula: lâmina 67; card da 30"),
 sh(1791666340691, "azul", E_, "Poliovírus resiste mais que o HIV", 67, "A-aula: lâminas 54 e 67 (nu × envelopado); card da 30"),
 au("au-nu", "Without a lipid envelope, <b>naked viruses</b> withstand acid, bile and drying, so many spread by the {{c1::fecal-oral}} route",
    "V-prova", E_, "Vírus nu: resiste ao trato digestivo", 68, "lâminas 54 e 67–68; provas 2025 P3 2.3 (por que não ser envelopado), 2024 P3 1.5 e 2019 P3 3.2 (estrutura → via de transmissão)",
    extra="- Enveloped viruses dry out easily and spread mostly by respiratory droplets, sex or blood<br>- Examples of naked fecal-oral viruses: polio, hepatitis A, rotavirus"),
 ak("ak-retro-diploide", 1502064775742, "A-aula", E_, "Retrovírus: genoma diploide", 70, "lâmina 70 (genoma diploide: retrovírus); seção FirstAid"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak-fago": "- Described by Twort (1915) and d'Herelle (1917), who named them bacteriophages",
 "ak-sem-metabolismo": "- No ribosomes and no ATP generation: they use the host's machinery",
 "ak-rickettsia": "- In the lecture's table: does not grow on artificial media, but has ATP-generating metabolism",
 "ak-rickettsia-coa": "- That dependence on the host keeps it obligate intracellular",
 "ak-chlamydia-atp": "- An 'energy parasite'; still has DNA, RNA and ribosomes, unlike viruses",
 "ak-interferon": "- Viruses are not sensitive to antibiotics, but are sensitive to interferon",
 "ak-polaridade": "- (+) sense = same polarity as mRNA; (−) sense = complementary to mRNA",
 "ak-rna-mrna": "- Baltimore group IV goes straight to translation",
 "ak-rna-mais-uso": "- That is why purified (+) RNA genomes are infectious",
 "ak-rna-menos": "- Baltimore group V: genome → (+) mRNA by the viral polymerase",
 "ak-rna-menos-pol": "- The cell has no RNA-dependent RNA polymerase, so the virion must bring one",
 "ak-rna-menos-infec": "- Naked (−) RNA cannot be translated without the virion's polymerase",
 "ak-transcricao-reversa": "- Group VI (retroviruses) and group VII (hepatitis B) use reverse transcriptase",
 "ak-parvo-menor": "- About 20 nm; poxviruses are the largest, about 300 nm",
 "ak-pox-maior": "- Large enough to approach the limit of light microscopy",
 "ak-capsideo": "- Each virus has one type of nucleic acid, never both",
 "ak-dna-genoma": "- Exceptions: parvovirus (single-stranded) and hepatitis B (partially double-stranded)",
 "ak-parvo-ss": "- The rest of the DNA viruses are double-stranded",
 "ak-rna-ss": "- Exception: reovirus (double-stranded, segmented)",
 "ak-reo-ds": "- Its genome is also segmented",
 "ak-segmentado": "- Segmented genomes: influenza, rotavirus/reovirus, bunyavirus, arenavirus",
 "ak-formas": "- A third form is complex (poxvirus, bacteriophage)",
 "ak-nus-icosa": "- Naked helical viruses exist in plants (tobacco mosaic virus)",
 "ak-envelopados-forma": "- Enveloped icosahedral: herpes, yellow fever, rubella; enveloped helical: influenza, rabies, measles",
 "ak-helicoidais-menos": "- All human helical viruses are enveloped",
 "ak-pox-dna": "- Complex symmetry, the largest and most elaborate virions",
 "ak-pox-tijolo": "- Its core holds the DNA and virion enzymes",
 "ak-pox-halter": "- Seen on electron microscopy (lâmina 64)",
 "ak-pox-envelope": "- Most enveloped viruses take their envelope from host membranes",
 "ak-ha": "- Influenza spikes: hemagglutinin (entry) and neuraminidase (exit)",
 "ak-na": "- Neuraminidase inhibitors (oseltamivir) block release",
 "ak-hiv-p24": "- gag gene: p24 (capsid) and p17 (matrix)",
 "ak-hiv-env": "- gp120 binds CD4; gp41 mediates fusion",
 "ak-hiv-pol": "- The virion carries these enzymes inside the capsid",
 "ak-envelope": "- Acquired by budding through a host membrane",
 "ak-glicoproteinas": "- These spikes are the envelope glycoproteins (e.g., hemagglutinin)",
 "ak-alcool": "- Ether and detergents also dissolve the envelope; naked viruses resist them",
 "ak-retro-diploide": "- Two copies of (+) single-stranded RNA per virion",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (Baltimore, cinco estruturas) estão nos cards do conceito"
SLIDE_SEM_ALT = "esquema da própria aula, sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "mb57-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {"au-baltimore": "a resposta mRNA aparece em cards de polaridade, mas aqui o alvo é o critério da classificação de Baltimore",
              "au-estruturas": "poxvírus é resposta também em ak-pox-maior (tamanho); aqui é exemplo da simetria complexa no organizador das cinco estruturas"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "mb57-baltimore.jpg": "Lâmina 40: esquema de Baltimore com os grupos I–VII convergindo para o +mRNA; verso de au-baltimore.",
 "mb57-estruturas.jpg": "Lâmina 55: cinco tipos de simetria (icosaédrica, icosaédrica envelopada, helicoidal, helicoidal envelopada, complexa); verso de au-estruturas.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Definir vírus e diferenciá-lo de bactérias intracelulares, classificar pelos sistemas hierárquico e de Baltimore, "
             "e descrever a estrutura (genoma, capsídeo, nucleocapsídeo, simetrias, envelope e espículas) e suas consequências.",
 "centrais": [
   ("definição", "au-definicao", "ak-sem-metabolismo"),
   ("classificação", "au-baltimore", "ak-polaridade"),
   ("estrutura", "au-nucleocapsideo", "ak-envelopados-forma", "ak-glicoproteinas", "ak-alcool"),
   ("nus × envelopados", "au-nu"),
 ],
 "exemplos": ["múmias com poliomielite e varíola", "fatos curiosos dos fagos", "árvore do ICTV"],
 "outras_aulas": [("replicação viral", "58 Multiplicação viral"), ("inclusões virais", "61 Patologia da infecção viral"),
                  ("Koch", "35 Patogenicidade bacteriana (sh)"), ("filtros e desinfetantes", "30 Controle microbiológico (sh)"),
                  ("Mycoplasma e intracelulares", "26 Morfologia bacteriana (sh)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
