"""Inventário atômico do Grand Round 3 — Espondilodiscite tuberculosa (UC03 P3; Profa. Gisela Serra Rodrigues Costa e equipe, 48 lâminas),
escrito ANTES de escolher cards, a partir do material de base lido inteiro: lâminas (visual/folha-01..08 e fontes/slides.txt),
pasta da turma (só o PDF das lâminas), monitoria P3 de Micro (não traz o GR3), apostilas de veteranos (Guia de Micro/Patologia/Imuno,
Radiologia "Tudo que você precisa saber de RD"; a UC3.pdf traz outro GR3, de aterosclerose, descartado), provas (índice gr-03 e busca
por tuberculose), Trabulsi 6ª ed. cap. 56 (Micobactérias) e Robbins (inflamação granulomatosa, tuberculose, osteomielite tuberculosa).
Cada ideia aponta para o card que a pergunta (chave do spec, lista, "sh-<nid>" ou "EXC: motivo" só em lâmina). Menção no verso não conta.
"""
PREFIXO = "gr03"
AULA = "Grand Round 3 — Espondilodiscite tuberculosa (UC03 P3; Grand Round, Micobactérias e diagnóstico de TB)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"

SLIDES = [
 (1, "conteudo", "Caso: identificação e antecedentes", [
   ("hiv", "Paciente com HIV: imunossupressão favorece reativação da TB e granulomas mal formados",
    ["reativacao", S(1791716438427)]),
   ("antecedentes", "TARV, hepatopatia crônica por HCV, sífilis, HAS/DRC e medicações de uso contínuo",
    EXC + "antecedentes e medicações do caso, sem alvo de recuperação sobre TB; o HIV (item acima) é o único que o caso usa")]),
 (2, "conteudo", "Caso: história da moléstia", [
   ("quadro", "Lombalgia progressiva, dor em membro, perda de 12 kg, sem febre referida", ["pott-clinica", "osteo-vertebral-clinica", "osteo-vertebral-local"]),
   ("dx-imagem", "RM mostrou espondilodiscite L2-L3: infecção do disco e das vértebras vizinhas", ["espondilodiscite", "pott-def"]),
   ("epidemio", "Nega contato com sintomáticos respiratórios ou TB em tratamento", EXC + "dado epidemiológico do caso; o raciocínio de risco está em HIV e Pott"),
   ("ppd", "PPD de 0 mm em paciente com HIV", "ppd-hiv-falso")]),
 (3, "conteudo", "Caso: exame físico e conduta inicial", [
   ("exame", "Emagrecido, descorado, T 38,4 °C, ausculta e neurológico normais", EXC + "sinais do caso; a febre e o emagrecimento entram em pott-clinica"),
   ("empirico", "Avaliação pré-operatória e ceftriaxona + clindamicina empíricas", EXC + "conduta do caso sem alvo da aula; a lição está em pedir cultura de micobactérias (lâmina 6)")]),
 (4, "conteudo", "RM da coluna lombossacra", [
   ("rm", "RM sagital: disco e corpos vertebrais comprometidos (T1 escuro, T2 com supressão de gordura brilhante)",
    ["rm-espond", S(1791054020796), S(1791054020921)])]),
 (5, "conteudo", "Exames complementares", [
   ("rx", "Radiografia de tórax e hemograma/função renal e hepática do caso", EXC + "exames do caso; só os marcadores inflamatórios têm alvo (item abaixo)"),
   ("pcr", "PCR 145,7 e VHS 135 elevados", "pcr-vhs")]),
 (6, "conteudo", "Cirurgia", [
   ("cirurgia", "Laminectomia L2-L3 e dreno portovac", EXC + "técnica cirúrgica do caso, fora do recorte do deck"),
   ("pedir-tb", "Infectologia acrescentou cultura para micobactérias e fungos, PCR-TB e TC de tórax", "pedir-micobacteria")]),
 (7, "conteudo", "TC de tórax", [
   ("tc", "TC de tórax com micronódulos difusos aleatórios (padrão miliar)", "tc-miliar")]),
 (8, "conteudo", "Microbiologia do caso", [
   ("culturas", "Culturas aeróbia, anaeróbia, fungos e micobactérias do fragmento ósseo", ["paucibacilar", "cultura-tempo"])]),
 (9, "conteudo", "Evolução", [
   ("evolucao", "Dreno retirado, analgesia controlada, hemograma e PCR de 10 e 17/11", EXC + "evolução clínica e laboratorial do caso"),
   ("aerossol", "Broncoscopia solicitada e precaução para aerossóis instituída", ["aerossol-precaucao", S(1791746131901)])]),
 (10, "conteudo", "Broncoscopia", [
   ("traqueia", "Aumento do diâmetro anteroposterior e desvio da traqueia", EXC + "achado endoscópico do caso sem alvo da aula"),
   ("lba", "LBA: pesquisa de BAAR negativa, PMN frequentes, sem micro-organismos, culturas negativas", "paucibacilar"),
   ("biopsia", "Biópsia transbrônquica com pigmento antracótico", S(1791592721894))]),
 (11, "conteudo", "Laudo anatomopatológico da biópsia transbrônquica", [
   ("sem-granuloma", "Sem granulomas na biópsia pequena e com artefatos: não exclui TB", S(1791716431615))]),
 (12, "conteudo", "TRM do LBA", [
   ("trace", "Complexo MTB detectado em traços, resistência à rifampicina indeterminada", ["trace"]),
   ("trace-regra", "Traços contam como positivo em HIV, criança < 10 anos ou amostra extrapulmonar", "trace-interpret")]),
 (13, "conteudo", "TRM do material intraoperatório", [
   ("trm-osso", "Xpert em fragmento ósseo: MTB detectado, resistência à rifampicina não detectada", "trm-amostras")]),
 (14, "conteudo", "Anatomopatológico do material intraoperatório", [
   ("laudo", "Processo inflamatório crônico granulomatoso, granulomas com necrose; BAAR e fungos inconclusivos", "granuloma-osso")]),
 (15, "conteudo", "Esquema do granuloma imune", [
   ("apc-il12", "APC apresenta antígeno e libera IL-12, que diferencia Th1", S(1791716421256)),
   ("ifng", "Th1 libera IFN-γ, que ativa macrófagos e forma epitelioides e células gigantes", S(1791625436658)),
   ("tnf", "TNF mantém o granuloma", S(1791716422184)),
   ("def", "Granuloma: agregado de macrófagos epitelioides com células gigantes e coroa de linfócitos", S(1791716404503)),
   ("celular", "A imunidade contra micobactérias é celular, não por anticorpos", S(1791763624470))]),
 (16, "conteudo", "Histologia: granuloma caseoso", [
   ("caseoso", "Necrose caseosa central com fibrose periférica", [S(1791716427876), S(1791716427402)])]),
 (17, "conteudo", "Histologia: células gigantes de Langhans", [
   ("langhans", "Células gigantes de Langhans com núcleos periféricos", S(1791716425027))]),
 (18, "conteudo", "Histologia: granuloma na medula óssea", [
   ("medula", "Granuloma com célula gigante multinucleada na medula óssea", "granuloma-osso-img")]),
 (19, "conteudo", "Macroscopia pulmonar miliar", [
   ("miliar-pulmao", "Nódulos brancos pequenos disseminados no pulmão (miliar, como grãos de painço)", S(1791716437955)),
   ("miliar-sangue", "TB miliar resulta de disseminação hematogênica", S(1791716437500))]),
 (20, "conteudo", "Histologia: granuloma no pulmão", [
   ("granuloma-pulmao", "Agregado circunscrito de macrófagos epitelioides no parênquima", S(1791716426458))]),
 (21, "conteudo", "Histologia: granulomas coalescentes", [
   ("graus", "Granulomas do mesmo pulmão variam em necrose e fibrose", S(1791716426943)),
   ("hiv-granuloma", "Sem Th1 no HIV, o granuloma tem coroa linfocitária escassa", S(1791716438930))]),
 (22, "conteudo", "Miliar no baço e no fígado e BAAR", [
   ("miliar-orgaos", "Granulomas miliares em baço, fígado, suprarrenal e meninges", "miliar-orgaos"),
   ("baar-visual", "Bacilos vermelhos finos em fundo azul são BAAR", S(1791716429751))]),
 (23, "conteudo", "Taxonomia de Mycobacterium", [
   ("taxonomia", "Filo/classe Actinobacteria, ordem Actinomycetales, família Mycobacteriaceae", "taxonomia"),
   ("baar", "Bacilos álcool-ácido resistentes", S(1791576674292)),
   ("aerobio", "Aeróbios, imóveis (M. tuberculosis aeróbio estrito)", "aerobio"),
   ("intracelular", "Intracelulares facultativos", S(1791746122586)),
   ("esporos", "Não formam esporos, mas entram em dormência", "dormencia"),
   ("espectro", "Saprófitos, oportunistas ou patógenos obrigatórios", "espectro")]),
 (24, "conteudo", "Velocidade de crescimento", [
   ("rapido", "Crescimento rápido < 7 dias, maioria ambiental", "rapido"),
   ("lento", "Crescimento lento > 7 dias, complexo M. tuberculosis (semanas)", "lento"),
   ("td", "Replicação de M. tuberculosis muito mais lenta que a da E. coli", "td-ecoli")]),
 (25, "conteudo", "Parede micobacteriana", [
   ("lipideos", "Lipídeos complexos: cerca de 60% da parede, ácidos micólicos", "parede-lipidos"),
   ("glicolipideos", "Glicolipídeos LAM e PIM", S(1791716451309)),
   ("arabinogalactano", "Arabinogalactano liga o peptidoglicano aos ácidos micólicos", S(1791716450848)),
   ("gram", "Parede diferente de Gram+ e Gram−: só fracamente Gram-positiva", "gram-fraco"),
   ("resistencia-fisica", "Parede cerosa resiste a desinfetantes e dessecação", S(1791666340566)),
   ("colonias", "Colônias de aspecto seco e rugoso e frascos de meio verde", EXC + "fotografia de colônias sem alvo próprio; o meio verde (LJ) tem card na lâmina 38")]),
 (26, "conteudo", "Modelo molecular do envelope", [
   ("envelope", "Camadas: micomembrana, arabinogalactano, peptidoglicano, periplasma, membrana plasmática",
    S(1791716450848))]),
 (27, "conteudo", "Coloração de Ziehl-Neelsen", [
   ("zn", "Ziehl-Neelsen: carbol fucsina e BAAR em vermelho", S(1791576674542)),
   ("nomes", "Franz Ziehl e Friedrich Neelsen", EXC + "nomes dos autores da técnica; o eponímo já é o nome do card")]),
 (28, "conteudo", "Método de Ziehl-Neelsen", [
   ("fixar", "Esfregaço fixado (biossegurança)", EXC + "passo preparatório sem alvo próprio; a ordem fucsina, ácido-álcool, azul fica nos cards seguintes"),
   ("fucsina", "Fucsina fenicada a quente", S(1791576674542)),
   ("descorante", "Ácido-álcool 3% descora tudo, menos o BAAR", "zn-descorante"),
   ("azul", "Azul de metileno cora o fundo e as bactérias não BAAR", "zn-contra")]),
 (29, "conteudo", "Tuberculose: biossegurança", [
   ("nb3", "Laboratório de biossegurança 3", "nb3"),
   ("aerossol", "Transmissão por aerossol e uso de EPI", "aerossol-transm"),
   ("notificacao", "Notificação obrigatória", EXC + "norma administrativa sem alvo de mecanismo; vale como contexto")]),
 (30, "conteudo", "Complexo Mycobacterium tuberculosis", [
   ("clonal", "Evolução clonal, >99% de identidade, sem transferência horizontal de genes", "mtbc-clonal"),
   ("tropismo", "Tropismos variados por hospedeiros e virulência", "mtbc-hospedeiros")]),
 (31, "conteudo", "Filogenia do complexo", [
   ("bcg", "BCG é M. bovis com deleção da região RD1", "bcg-rd1")]),
 (32, "conteudo", "Espécies do complexo e hospedeiros", [
   ("hospedeiros", "M. tuberculosis e M. africanum em humanos; M. bovis em bovinos e humanos; outras em animais", "mtbc-hospedeiros")]),
 (33, "conteudo", "Mecanismos de virulência", [
   ("macrofago", "Célula-alvo do complexo: macrófagos", S(1791716419358)),
   ("fusao", "Inibição da fusão do fagossomo com o lisossomo", S(1791746131503)),
   ("lam", "Micobactérias impedem a fusão por glicolipídeos como o ManLAM", S(1791746131627)),
   ("acido", "Se o fagossomo acidifica, a bactéria ainda resiste (bomba de efluxo)", "resiste-acido"),
   ("citosol", "A bactéria pode escapar do fagossomo e ficar livre no citosol", "fagossomo-citosol"),
   ("dormencia", "Dormência: antibióticos não agem", "dormencia"),
   ("tratamento", "Tratamento prolongado por causa da dormência e da associação de drogas", ["dormencia-tratamento", S(1791668528039)])]),
 (34, "conteudo", "Granuloma, principal lesão da TB", [
   ("fortaleza", "Fortaleza de células que elimina ou contém o patógeno", [S(1791716448950), S(1791716405608)]),
   ("tipos", "Granuloma sólido, caseoso e cavitário", "granuloma-tipos"),
   ("cavidade", "Cavidade que drena para a via aérea", S(1791716436082)),
   ("bacilifero", "Paciente bacilífero", "bacilifero")]),
 (35, "conteudo", "Diagnóstico laboratorial", [
   ("ativa", "TB ativa: clínica e imagem + baciloscopia, cultura, TRM, TB-LAM, testes de susceptibilidade",
    ["bacilo-sens", "cultura-tempo", "xpert-def", "tblam", "lpa1"]),
   ("latente", "TB latente: tuberculinização e IGRA", ["latente", S(1791763642743)])]),
 (36, "conteudo", "Teste do escarro", [
   ("naoh", "Descontaminação com NaOH 2%", "escarro-naoh"),
   ("nalc", "Liquefação com N-acetil-L-cisteína e citrato", "escarro-nalc"),
   ("pbs", "Neutralização com PBS e depois baciloscopia/cultivo", "escarro-pbs")]),
 (37, "conteudo", "Baciloscopia direta", [
   ("sens", "Sensibilidade de 60 a 80%, paucibacilar 20–30%", "bacilo-sens"),
   ("limiar", "Necessita 1.000 a 10.000 CFU/mL", "bacilo-limiar"),
   ("especificidade", "Não diferencia o MTBC de outras micobactérias", S(1791716430209)),
   ("seriada", "Coletas seriadas (até 3)", "bacilo-seriada"),
   ("indicacao", "Sintomáticos respiratórios, suspeita clínica ou radiológica, TB extrapulmonar", "bacilo-indicacao")]),
 (38, "conteudo", "Isolamento e cultivo", [
   ("mgit", "BACTEC MGIT 960: indicador fluorescente, crescimento consome oxigênio", ["mgit", "middlebrook"]),
   ("lj", "Löwenstein-Jensen: ovos, asparagina, amido, glicerol, verde de malaquita e polimixina B", ["lj", "lj-composicao", "lj-polimixina"]),
   ("stonebrink", "Stonebrink para M. bovis: sem glicerol, com piruvato", "stonebrink")]),
 (39, "conteudo", "Cultivo: tempo e sensibilidade", [
   ("tempo", "LJ 21–60 dias, MGIT 7–14 dias", "cultura-tempo"),
   ("sens", "Sensibilidade LJ 80–85%, MGIT 90–95%", "cultura-sens"),
   ("resistencia", "Importante para o perfil de resistência, pouco útil para diagnóstico rápido", "cultura-resistencia")]),
 (40, "conteudo", "Teste rápido molecular: Xpert MTB/RIF Ultra", [
   ("rrdr", "Detecta mutações da RRDR, responsáveis por 95% dos casos de resistência à rifampicina", ["rrdr-95", "rpob"]),
   ("xpert", "Detecta MTB e resistência à rifampicina no mesmo teste", "xpert-def"),
   ("cobertura", "Cobertura de cerca de 50% dos pacientes no estado de São Paulo", EXC + "dado de cobertura regional, sem alvo conceitual")]),
 (41, "conteudo", "TRM: amostras e desempenho", [
   ("amostras", "Escarro, líquido pleural ou cerebroespinhal, LBA, aspirados, linfonodos, fezes, biópsias, urina", "trm-amostras"),
   ("desempenho", "Sensibilidade e especificidade por condição", "trm-sens")]),
 (42, "conteudo", "TB-LAM", [
   ("lam", "Detecta lipoarabinomanano na urina de pacientes com TB e HIV", "tblam"),
   ("sens", "Sensibilidade depende do avanço da doença (CD4 baixo)", "tblam-sens"),
   ("poc", "Point-of-care, resultado em 25 minutos", EXC + "atributo operacional sem alvo conceitual próprio")]),
 (43, "conteudo", "Susceptibilidade: testes fenotípicos", [
   ("fenotipico", "Concentração crítica em meio semissólido ou MGIT; CIM por diluições", "dst-fenotipico")]),
 (44, "conteudo", "Susceptibilidade: LPA-1", [
   ("lpa1", "MTBDRplus: MTBC mais resistência a rifampicina e isoniazida", "lpa1")]),
 (45, "conteudo", "Susceptibilidade: LPA-2 e drogas", [
   ("lpa2", "MTBDRsl: fluoroquinolonas, aminoglicosídeos e etambutol", "lpa2"),
   ("primeira", "Rifampicina, isoniazida, pirazinamida e etambutol", S(1791746131779)),
   ("pza", "M. bovis é intrinsecamente resistente à pirazinamida", "pza-bovis"),
   ("segunda", "Fluoroquinolonas, linezolida, etionamida, delamanida, bedaquilina, clofazimina e pretomanida", "drogas-novas")]),
 (46, "conteudo", "Fluxograma SP-SUS", [
   ("grupos", "Doze grupos com indicação de cultura e Xpert (retratamento, prisões, rua, HIV...)", "fluxo-grupos"),
   ("resist", "Xpert com resistência segue para LPA-1 e LPA-2 simultaneamente", "fluxo-xpert-resist"),
   ("sem-xpert", "Sem Xpert ou RIF negativo vai primeiro ao LPA-1", "fluxo-xpert-neg"),
   ("fenotipico", "Resistência inferida no LPA-2 leva aos testes fenotípicos", "dst-fenotipico")]),
 (47, "conteudo", "TB latente: prova tuberculínica", [
   ("hsr", "A tuberculina mede hipersensibilidade tardia mediada por células T", S(1791625436533)),
   ("leitura", "Medição da induração (pápula), leitura correta × incorreta", "ppd-leitura"),
   ("tempo", "Leitura em 72 h", "ppd-72h"),
   ("bcg", "BCG pode dar falso positivo", "bcg-falso"),
   ("app", "Aplicativo PrevenirTB", EXC + "ferramenta de notificação sem alvo de conhecimento")]),
 (48, "conteudo", "TB latente: IGRA", [
   ("igra", "IGRA mede IFN-γ liberado pelos linfócitos T estimulados com antígenos de TB", ["igra-medida", "igra-passos"]),
   ("bcg", "IGRA não reage com a BCG (antígenos ESAT-6 e CFP-10)", ["igra-bcg", "igra-antigenos"])]),
]
JUSTIFICATIVAS = {}
CAPITULO = [("Trabulsi 6ª ed., cap. 56 Micobactérias (pdf pp. 513–531)", [
   ("parede-60", "Cerca de 60% da parede é lipídio (ácidos micólicos de 60–90 C) ligados ao arabinogalactano", "parede-lipidos"),
   ("gram-fraco", "Fracamente Gram-positivas, BAAR", ["gram-fraco", "zn-descorante"]),
   ("hipersens", "Manifestações decorrem da resposta imune celular; tuberculina mede hipersensibilidade tardia", S(1791625436533)),
   ("rpob", "96% da resistência à rifampicina por mutações em rpoB (subunidade beta da RNA polimerase)", "rpob"),
   ("mdr", "MDR-TB é resistência a pelo menos isoniazida e rifampicina", "mdr"),
   ("bcg-prova", "BCG também reage ao PPD, reduzindo a confiabilidade do teste", "bcg-falso"),
   ("lento", "Crescimento lento, colônias secas e rugosas em semanas", "lento")]),
 ("Robbins, cap. 8 (tuberculose) e cap. 26 (osteomielite tuberculosa)", [
   ("pott", "Doença de Pott: infecção rompe os discos, envolve várias vértebras e forma abscessos nos tecidos moles", ["pott-def", "pott-abscesso"]),
   ("pott-clinica", "Dor à mobilização, sensibilidade local, febre baixa e perda de peso", "pott-clinica"),
   ("pott-complicacao", "Colapso vertebral causa cifose e déficit neurológico por compressão", "pott-complicacao"),
   ("hiv-tb", "Em HIV avançado os granulomas são mal formados e o BAAR no escarro pode ser negativo", S(1791716438427)),
   ("granuloma", "Granuloma é esforço celular para conter agente difícil de erradicar; TB é o protótipo", S(1791716404503)),
   ("baar-tecido", "BAAR deve ser pesquisado em qualquer granuloma, com ou sem caseação", S(1791716430209))])]
EXERCICIOS = [("Provas UC03 (índice gr-03 e busca por tuberculose)", [
   ("2025-curva", "2025 P2 3.2: curva de crescimento da E. coli × M. tuberculosis (lag longa, crescimento lento)", "td-ecoli"),
   ("2025-esteriliza", "2025 P2 3.3: micobactérias resistem a desinfetantes por parede lipídica", S(1791666340566)),
   ("2025-persistencia", "2025 P2 3.4: bloqueio do fagolisossomo, bomba de efluxo e escape citosólico", ["resiste-acido", "fagossomo-citosol", S(1791746131503)]),
   ("2025-igra", "2025 P2 5.1: IGRA mede IFN-γ com ESAT-6/CFP-10 e não reage com a BCG; PPD positivo isolado sugere BCG", ["igra-bcg", "igra-antigenos", "bcg-falso"]),
   ("2025-tc-coluna", "2025 P2 3.1 (RD): TC de coluna torácica com lesão de centro hipoatenuante e contorno espesso, biópsia com granulomas BAAR+", "pott-tc"),
   ("2023-gram", "2023 P2 3.3: por que não corar pelo Gram: parede com ácido micólico, Ziehl-Neelsen", ["gram-fraco", "zn-descorante"]),
   ("2023-terapia", "2023 P2 3.4: várias drogas por tempo prolongado, crescimento lento e bacilos dentro de macrófagos", ["dormencia-tratamento", S(1791668528039)]),
   ("2016-hiv", "2016 P2 3.4: HIV leva a granuloma mal formado, com poucos linfócitos", [S(1791716438427), S(1791716438930)]),
   ("2015-ifng", "2015 P2 1.1/1.2: IFN-γ é o mediador do granuloma, célula gigante e coroa linfocitária", [S(1791625436658), S(1791716425027)])]),
 ("Monitoria P3 de Micro: não traz o GR3 (só o GR4 de febre amarela)", []),
 ("Apostilas de veteranos: Guia de Patologia (granuloma/TB) e RD 'Tudo que você precisa saber' (espondilodiscite)", [
   ("vet-granuloma", "Guia de Patologia cap. 7: TB impede o fagolisossomo, Th1/IFN-γ, retroalimentação positiva", [S(1791625436658), S(1791716421256)]),
   ("vet-rd", "RD: lesão vertebral inflamatória, centro hipoatenuante (osteólise) com contorno espesso hiperatenuante", "pott-tc")])]
