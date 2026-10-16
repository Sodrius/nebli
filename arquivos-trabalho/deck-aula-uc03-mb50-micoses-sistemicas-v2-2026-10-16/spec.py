# Especificação curada — 50 Micoses sistêmicas (UC03 P3, Microbiologia; Prof. Benedito Corrêa; 144 lâminas = Micoses Sistêmicas I + II da turma).
# Refação v2 (F-20261016-CLAUDE-08/09): AnKing primeiro (seções de Histoplasma, Paracoccidioides, Cryptococcus e Candida declaradas: toda nota entra
# ou sai com motivo); autorais antigos só os elogiados/corrigidos por Davi, de prova ou centrais da lâmina. Escopo pelo Trabulsi caps. 69–70:
# coccidioidomicose, blastomicose, aspergilose, mucormicose e pneumocistose (fora das lâminas) com cobertura mínima de AnKing. Ordem = lâminas (I).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb50-20261016a"
SHORT = "mb50"
LESSON = "2026-uc03-microbiologia-50-micoses-sistemicas"
DECK = "NEBLI::UC03::P3::Microbiologia::Micoses sistêmicas"
CRITERIOS = "EXECUCAO-DECK-AULA (passos 0–7) + MEMORY §2–§8 + ANTI-EXEMPLARES + F-20261016-CLAUDE-08/09, 16/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (16/10): seções (busca/secoes: Histoplasm, Paracoccidioid, Cryptococc, Candida, Coccidioid, Blastomyc, Aspergill, Mucor, Pneumocyst); "
         "palavra-chave (busca/anking.txt); significado em todos os acervos e decks NEBLI vivos (busca/semantica.jsonl). ")
A = lambda nid, cod, bloco, alvo, slide, motivo, **kw: acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)
EXTRA_VIVO = {1791630906668: "histoplasma-intracelular", 1791630906243: "histoplasma-macroconidios"}

_TOX = "toxicidade/administração de antifúngico: farmacologia clínica, fora do recorte"
_M43 = "mecanismo dos antifúngicos: aula 43"
_IMU = "imunologia (imunodeficiências/hipersensibilidade): aulas 51/64"
EXCLUIDOS = [(n, _TOX) for n in (1509743451213, 1509744066944, 1509744002911, 1509743833529, 1509743517947, 1509743284999, 1509743957410, 1509743634123,
                                1509743336397, 1509743670062, 1509743767890, 1509744667080, 1509755342899, 1509755647704, 1509744794419, 1509747054868,
                                1509747259788, 1509747124822, 1509752610104)] + \
            [(n, _M43) for n in (1509753380809, 1509743058195, 1509742361304, 1509742681361, 1509742489846, 1509742443199, 1509742586045, 1509743373899)] + \
            [(n, _IMU) for n in (1585609953732, 1486952733427, 1500234392681, 1487642773652, 1487727763491, 1520351135706)] + [
 (1516128968450, "vaginose por Gardnerella: outro assunto"), (1500236384725, "Gardnerella: outro assunto"),
 (1502068052536, "critério de AIDS: virologia (HIV)"), (1581259369271, "esofagite viral: outro assunto"),
 (1473732927285, "nódulo em moeda no RX: radiologia geral"), (1615322596752, "achados cutâneos de vários agentes: outro assunto"),
 (1584393298504, "infecções no diabetes em geral: outro assunto"), (1474580722813, "conduta após corticoide inalado"),
 (1556238830946, "imagem de várias espécies (irmãos de outras aulas)"), (1556238737112, "imagem de várias espécies (irmãos de outras aulas)"),
 (1556238884073, "imagem de várias espécies (irmãos de outras aulas)"), (1556238858660, "imagem de várias espécies (irmãos de outras aulas)"),
 (1522432485269, "profilaxia por contagem de CD4: conduta"), (1504045576164, "esquema e duração do tratamento: conduta"),
 (1509746017401, "tratamento da esofagite candidiásica no HIV: conduta"), (1509745961686, "fluconazol na candidíase vaginal: conduta (aula 44)"),
]
FORA_DO_RECORTE = [
 "Histórico, datas e números de mortalidade da PCM e da histoplasmose; grupos filogenéticos S1/PS2/PS3: Tab (§4).",
 "Coccidioidomicose, blastomicose, aspergilose, mucormicose e pneumocistose só com cobertura mínima (Trabulsi caps. 69–70; não estão nas lâminas).",
 "Toxicidades dos antifúngicos e condutas (profilaxia, esquemas): farmacologia clínica.",
]
A_, B_, C_, M_, D_, O_, E_ = ("A-sistemicas", "B-paracoccidioidomicose", "C-histoplasmose", "M-minimas-endemicas", "D-candidose", "O-minimas-oportunistas", "E-criptococose")

CARDS = [
 # A. Micoses sistêmicas: classificação e características comuns (2–4)
 sh(1792065182152, "verde", A_, "Principais micoses sistêmicas", 2, "V-pilar: lâminas 2 e 65; organizador elogiado por Davi (“bom card organizador”)"),
 sh(1792065183130, "azul", A_, "Características comuns dos agentes", 4, "A-aula: lâminas 4 e 66; apostila e UC3.pdf"),
 A(1499970409878, "V-prova", A_, "Bolor no solo, levedura no corpo", 4, "lâmina 4; prova 2017 P2 2.6; nota viva da 43"),
 A(1499968803765, "R-detalhe", A_, "Infecção grave no imunossuprimido", 4, "Trabulsi cap. 70 (oportunistas); nota viva da 43"),
 # B. Paracoccidioidomicose (5–20)
 A(1499975610400, "V-hy", B_, "PCM na América do Sul", 5, "lâminas 5 e 73"),
 sh(1791630903017, "azul", B_, "P. brasiliensis e P. lutzii", 6, "A-aula: lâminas 6, 68, 70; autoral antigo mantido"),
 A(1499976310064, "V-hy", B_, "Inalação de esporos", 7, "lâmina 7 (inalação, ferimentos)"),
 sh(1791630903393, "rosa", B_, "Tatu como reservatório", 8, "R-detalhe: lâminas 8 e 71; Trabulsi; autoral antigo mantido"),
 sh(1791630908545, "azul", B_, "Estradiol bloqueia a transição bolor → levedura", 8, "A-aula: lâmina 72; Trabulsi; UC3.pdf"),
 sh(1792065187180, "verde", B_, "Formas aguda/juvenil × crônica do adulto", 10, "V-pilar: lâminas 10 e 76; UC3.pdf; Trabulsi"),
 sh(1791744812782, "azul", B_, "Reativação de foco latente", 10, "A-aula: apostila, UC3.pdf, Trabulsi (forma crônica por reativação)"),
 A(1499976619643, "V-hy", B_, "Úlceras de mucosa oral e respiratória", 11, "lâminas 11, 77–79"),
 A(1499976536055, "V-hy", B_, "Pulmão → linfonodos → granulomas", 11, "lâminas 10–11; nota corrigida e elogiada por Davi"),
 A(1499976355327, "V-hy", B_, "Linfadenopatia na disseminação", 11, "lâmina 10 (forma juvenil, rápida disseminação)"),
 A(1499975827249, "V-hy", B_, "Levedura em roda de leme", 13, "lâminas 12–13, 83–84"),
 A(1499976239948, "V-hy", B_, "Maior que a hemácia", 13, "lâmina 13"),
 A(1499976133630, "V-prova", B_, "PCM é dimórfica", 14, "lâminas 14–16, 81–88; prova 2017 P2 2.6"),
 sh(1791744812583, "verde", B_, "Conídio do bolor inalado, levedura no tecido", 14, "V-prova: lâminas 14–16, 20; card elogiado por Davi (“ficou top”)"),
 sh(1791630904844, "verde", B_, "α-glucana na levedura, β-glucana no bolor", 18, "V-prova: lâminas 18 e 20; prova 2025 P3 1.2"),
 sh(1791744812082, "azul", B_, "Galactomanana imunogênica na fase M", 19, "A-aula: lâminas 19 e 91 (fluxograma de defesa)"),
 sh(1792083296387, "azul", B_, "Proteção pela imunidade celular", 19, "A-aula: apostila, UC3.pdf, Trabulsi"),
 A(1499976865408, "V-hy", B_, "PCM local: azol", 20, "apostila e UC3.pdf (itraconazol)"),
 A(1499976938219, "A-step", B_, "PCM disseminada: anfotericina B", 20, "apostila (anfotericina B)"),
 # C. Histoplasmose (21–33)
 A(1499968846522, "V-hy", C_, "Agente: Histoplasma capsulatum", 21, "lâminas 21 e 93"),
 A(1499968902834, "V-prova", C_, "Fezes de morcego e aves; cavernas e galinheiros", 21, "lâmina 21; prova 2025 P3 1.1 (população de risco)"),
 A(1499969725882, "V-hy", C_, "Endêmica no centro-oeste dos EUA", 21, "Trabulsi; UC3.pdf (Ohio e Mississippi)"),
 A(1499971579973, "V-hy", C_, "Vales do Mississippi e Ohio", 21, "UC3.pdf"),
 sh(1791630905643, "verde", C_, "Microconídios inalados", 22, "V-prova: lâminas 22–24; prova 2025 P3 1.1 (inalação de microconídios)"),
 A(1499969788030, "A-aula", C_, "Transmissão respiratória", 22, "lâmina 22"),
 A(1499970254984, "V-prova", C_, "Histoplasma é dimórfico", 26, "lâminas 26 e 98; prova 2025 P3 1.5"),
 sh(1791744813707, "azul", C_, "Microconídio vira levedura no macrófago", 25, "A-aula: lâminas 25 e 31; monitoria"),
 A(1499970930064, "V-hy", C_, "Alvo: sistema reticuloendotelial", 25, "lâmina 25 (fígado e baço)"),
 A(1499971032936, "V-hy", C_, "Disseminação ao fígado e baço no imunocomprometido", 25, "lâmina 25"),
 A(1499970816194, "V-hy", C_, "Hepatoesplenomegalia", 25, "lâmina 25; UC3.pdf"),
 sh(1791630906243, "rosa", C_, "Macroconídios tuberculados a 25 °C", 28, "R-detalhe: lâminas 27–29, 100–103; imagem da lâmina 28 no verso"),
 A(1499969898257, "V-hy", C_, "Macrófagos com corpos ovais", 31, "lâminas 31 e 105–106"),
 A(1499970198666, "V-hy", C_, "Menor que a hemácia", 31, "lâmina 31"),
 sh(1791630906367, "azul", C_, "Lesões na língua e no palato", 32, "A-aula: lâminas 32–33, 107–108; UC3.pdf"),
 sh(1791630906668, "azul", C_, "Diagnóstico pela cultura", 31, "A-aula: apostila, UC3.pdf, Trabulsi; imagem do parasitismo intracelular no verso (Davi pediu)"),
 A(1499970467218, "V-hy", C_, "Forma crônica parecida com TB", 33, "UC3.pdf; Trabulsi"),
 A(1499970710382, "V-hy", C_, "Eritema nodoso", 33, "Trabulsi (coccidioidomicose/histoplasmose)"),
 A(1499970027867, "A-step", C_, "Antígeno no soro e urina", 33, "Trabulsi (testes imunológicos)"),
 A(1499971065440, "V-hy", C_, "Histoplasmose local: azol", 33, "monitoria (itraconazol)"),
 A(1499971295935, "A-step", C_, "Histoplasmose disseminada: anfotericina B", 33, "apostila; Trabulsi"),
 # M. Cobertura mínima (Trabulsi cap. 69): coccidioidomicose e blastomicose
 A(1499974314372, "A-step", M_, "Coccidioides: bolor no solo, esférulas no corpo", 33, "Trabulsi cap. 69 (cobertura mínima)"),
 A(1499973296557, "V-hy", M_, "Coccidioides no sudoeste dos EUA", 33, "Trabulsi cap. 69"),
 A(1500152894219, "V-hy", M_, "Artroconídios em barril", 33, "Trabulsi cap. 69 (inalação de artroconídios)"),
 A(1499972082394, "V-hy", M_, "Blastomyces: brotamento de base larga", 33, "Trabulsi cap. 69 (cobertura mínima)"),
 A(1499972726166, "A-step", M_, "Blastomicose nos Grandes Lagos", 33, "Trabulsi cap. 69"),
 A(1509747380121, "V-hy", M_, "Itraconazol nas formas locais (histo, blasto, cocci)", 33, "Trabulsi caps. 69"),
 A(1499975201657, "V-hy", M_, "Cocci e Cryptococcus causam meningite", 33, "Trabulsi"),
 A(1509746332128, "V-hy", M_, "Itraconazol nos dimórficos locais", 33, "nota viva da 48"),
 # D. Candidose (34–53, 110–129)
 A(1500233417765, "V-hy", D_, "Candida: oportunista mais comum", 35, "lâminas 35 e 111–113"),
 A(1500234684400, "V-hy", D_, "Candida na microbiota", 35, "lâminas 35 e 112"),
 sh(1791630907168, "azul", D_, "Adesinas", 36, "A-aula: lâminas 36 e 121 (fatores de virulência)"),
 A(1500235637454, "V-hy", D_, "Diabetes predispõe", 37, "lâminas 37 e 114"),
 A(1500234954735, "V-hy", D_, "Imunocomprometido ou corticoide", 37, "lâminas 37 e 114"),
 A(1474580716506, "V-hy", D_, "Corticoide inalado → candidíase orofaríngea", 37, "lâmina 37 (corticoides)"),
 A(1502224452270, "A-aula", D_, "Deficiência de T → superficial", 37, "lâminas 37 e 115"),
 A(1502224462650, "V-hy", D_, "Neutropenia → disseminada", 37, "lâminas 37 e 119"),
 A(1517771826170, "V-hy", D_, "Candidíase mucocutânea crônica: IL-17/AIRE", 37, "Trabulsi cap. 70"),
 A(1500243661654, "V-hy", D_, "Sapinho", 38, "lâminas 38 e 116"),
 A(1500235087296, "V-hy", D_, "Placas que se raspam", 38, "lâmina 38"),
 A(1500235281810, "R-detalhe", D_, "Leucoplasia não se raspa", 38, "lâmina 38"),
 A(1500235389271, "A-step", D_, "Esofagite candidiásica: definidora de AIDS", 38, "Trabulsi cap. 70 (propaga ao esôfago; indicador de AIDS)"),
 A(1500235550523, "V-hy", D_, "Esofagite com CD4 < 100", 38, "Trabulsi cap. 70"),
 A(1482255701661, "V-hy", D_, "Esofagite com pseudomembranas brancas", 38, "Trabulsi cap. 70"),
 A(1535402608704, "A-aula", D_, "Intertrigo", 41, "lâminas 41–42 (lesão interdigital, dobras)"),
 A(1500234829361, "V-hy", D_, "Dermatite da fralda", 41, "lâmina 42"),
 A(1500243739726, "V-hy", D_, "Candidíase vaginal", 41, "lâmina 118 (vulvovaginite)"),
 A(1548722722283, "R-detalhe", D_, "Corrimento em queijo cottage", 41, "lâmina 118"),
 A(1500235811939, "V-hy", D_, "Fármacos que predispõem à vaginite", 41, "lâmina 118 (antibióticos, corticoides, contraceptivos)"),
 A(1500236404263, "V-hy", D_, "pH vaginal > 4,5", 41, "lâmina 118"),
 A(1500236178883, "V-hy", D_, "Candida não muda o pH vaginal", 41, "lâmina 118"),
 A(1522516244657, "V-hy", D_, "Nutrição parenteral: candidemia", 43, "lâminas 119–120 (candidíase sistêmica); Trabulsi (cateteres)"),
 A(1500236481845, "V-hy", D_, "Endocardite candidiásica em usuários de droga IV", 43, "Trabulsi cap. 70 (endocardite)"),
 A(1500236847040, "V-hy", D_, "Endocardite tricúspide", 43, "Trabulsi cap. 70"),
 sh(1791744820656, "azul", D_, "Candidíase sistêmica: rins, cérebro, coração", 43, "A-aula: lâmina 119; Trabulsi"),
 A(1500233665851, "V-hy", D_, "Candida dimórfica", 44, "lâmina 44 (levedura, pseudo-hifa, tubo germinativo)"),
 A(1500234149130, "V-hy", D_, "Levedura com pseudo-hifas a 20 °C", 44, "lâmina 44"),
 A(1500234023725, "V-hy", D_, "Tubo germinativo a 37 °C", 44, "lâminas 44 e 124"),
 A(1500234258289, "R-detalhe", D_, "Inverte o adágio do dimorfismo", 44, "lâmina 44"),
 A(1500243540399, "V-hy", D_, "Teste do tubo germinativo", 44, "lâminas 122 e 124"),
 A(1557752615914, "A-aula", D_, "Pseudo-hifas e brotamento", 43, "lâminas 43 e 123"),
 A(1548722722826, "A-aula", D_, "Pseudo-hifas no KOH", 43, "lâmina 123"),
 A(1500235321247, "V-hy", D_, "KOH no diagnóstico", 43, "lâmina 123 (exame direto)"),
 A(1500234787599, "V-hy", D_, "Candida contamina escarro", 45, "Trabulsi (critério para oportunista: isolamento repetido)"),
 sh(1791630907794, "rosa", D_, "Auxanograma", 51, "R-detalhe: lâminas 51–52 e 127–128"),
 A(1500237136393, "V-hy", D_, "Nistatina na candidíase oral", 53, "Trabulsi cap. 70 (tratamento)"),
 A(1509744422330, "V-hy", D_, "Nistatina age em Candida", 53, "Trabulsi"),
 A(1509744598051, "V-hy", D_, "Nistatina: oral e vaginal", 53, "Trabulsi"),
 A(1500237000985, "V-hy", D_, "Candidíase local: azol tópico", 53, "Trabulsi"),
 A(1500236922530, "V-hy", D_, "Candidíase sistêmica: caspofungina ou anfotericina B", 53, "Trabulsi (caspofungina nos sistêmicos)"),
 A(1509752199075, "A-step", D_, "Anfotericina B ou equinocandina na sistêmica", 53, "Trabulsi"),
 A(1509743217032, "V-hy", D_, "Anfotericina B nas infecções sistêmicas graves", 53, "apostila; Trabulsi"),
 # O. Cobertura mínima (Trabulsi cap. 70): aspergilose, mucormicose, pneumocistose
 A(1500240180987, "V-hy", O_, "Aspergilose invasiva no imunocomprometido", 53, "Trabulsi cap. 70 (cobertura mínima)"),
 A(1500239144039, "V-hy", O_, "ABPA: hipersensibilidade tipo I", 53, "Trabulsi cap. 70 (aspergilose alérgica)"),
 A(1473628203353, "V-hy", O_, "ABPA na asma e fibrose cística", 53, "Trabulsi cap. 70"),
 A(1462327377004, "V-hy", O_, "Mucormicose na cetoacidose diabética", 53, "Trabulsi cap. 70 (cobertura mínima)"),
 A(1500333974625, "V-hy", O_, "Mucor invade parede dos vasos", 53, "Trabulsi cap. 70"),
 A(1500335727221, "V-hy", O_, "Pneumocystis é um fungo", 53, "Trabulsi caps. 64 e 70 (cobertura mínima)"),
 A(1500336907300, "V-hy", O_, "Pneumocistose: AIDS com CD4 < 200", 53, "Trabulsi cap. 70"),
 A(1402963462795, "V-hy", O_, "Pneumocistose: TMP-SMX", 53, "Trabulsi cap. 70"),
 # E. Criptococose (54–63, 130–144)
 A(1500244584091, "V-hy", E_, "Fezes de pombo e solo", 55, "lâminas 55 e 133"),
 sh(1791630908043, "azul", E_, "C. gattii: eucalipto", 55, "A-aula: lâminas 55 e 140"),
 A(1500244699744, "V-hy", E_, "Inalação: infecção primária no pulmão", 56, "lâmina 138"),
 sh(1791630908168, "verde", E_, "Tropismo pelas meninges", 56, "V-pilar: lâminas 56 e 137; corrigido por Davi em 15/10"),
 A(1500244913534, "V-hy", E_, "Causa mais comum de meningite fúngica", 56, "lâminas 56 e 138"),
 A(1481771519577, "A-step", E_, "Meningite fúngica no HIV", 56, "lâmina 139 (aidéticos)"),
 A(1500245231306, "V-hy", E_, "Pneumonia e meningite", 56, "lâmina 138"),
 A(1500246326159, "A-step", E_, "Meningoencefalite indolente", 56, "lâmina 138"),
 A(1500245900584, "V-hy", E_, "Lesões em bolha de sabão no cérebro", 56, "lâmina 56"),
 A(1500244855818, "A-step", E_, "Oportunista no imunocomprometido", 56, "lâmina 139"),
 A(1525446605993, "V-hy", E_, "Levedura com cápsula", 59, "lâminas 59–60; prova 2024 P3 2.4"),
 A(1500243301914, "V-hy", E_, "Fungo encapsulado", 59, "prova 2024 P3 2.4–2.5"),
 A(1500244315193, "V-hy", E_, "Cápsula polissacarídica", 59, "prova 2024 P3 2.5"),
 A(1500244482455, "V-prova", E_, "Cápsula antifagocitária", 59, "prova 2024 P3 2.5"),
 sh(1791744820056, "verde", E_, "Cápsula prejudica apresentação de antígeno e NO", 59, "V-prova: prova 2024 P3 2.5 (literal do gabarito)"),
 A(1500246246409, "A-step", E_, "5–10 µm, brotamento de base estreita", 59, "lâmina 60"),
 A(1500245573893, "V-hy", E_, "Tinta da China (nanquim): halo", 59, "lâminas 58–60 e 143"),
 A(1500245756888, "V-hy", E_, "Látex detecta o antígeno capsular", 59, "Trabulsi (aglutinação do látex)"),
 A(1552904531628, "A-step", E_, "Teste mais sensível no LCR: látex", 59, "Trabulsi"),
 A(1500245338136, "A-step", E_, "Lavado broncopulmonar", 58, "lâmina 58 (coleta)"),
 A(1500245435059, "V-hy", E_, "Mucicarmim ou prata no tecido", 58, "lâmina 141 (mucicarmim); UC3.pdf"),
 A(1500419514988, "R-detalhe", E_, "Prata cora fungos, Pneumocystis, Cryptococcus", 58, "lâmina 141; Trabulsi"),
 A(1500246419118, "V-hy", E_, "Cultivo em Sabouraud", 58, "lâminas 58 e 143"),
 A(1500244771798, "V-hy", E_, "Urease positiva", 63, "lâminas 63 e 144; nota viva com Tab revisto por Davi"),
 A(1500245993331, "V-hy", E_, "Meningite criptocócica: anfotericina B + flucitosina, depois fluconazol", 63, "Trabulsi"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1499976239948": "- Paracoccidioides yeasts are large (10–60 µm) with many buds, unlike the small intracellular Histoplasma",
 "ak1499968846522": "- A dimorphic fungus from soil enriched with bird and bat droppings",
 "ak1499971032936": "- Without T-cell help, infected macrophages carry the yeast to the reticuloendothelial organs",
 "ak1500152894219": "- Inhaled arthroconidia become spherules full of endospores in the lung",
 "ak1509747380121": "- Itraconazole is an oral azole; severe disseminated forms need amphotericin B",
 "ak1482255701661": "- Candida spreads from the mouth to the esophagus when T-cell immunity falls (AIDS)",
 "ak1548722722283": "- The yeast overgrows when lactobacilli fall, as after antibiotics",
 "ak1509752199075": "- Invasive infections need drugs that act systemically, not topical azoles",
 "ak1509743217032": "- A polyene that binds ergosterol; used IV for life-threatening mycoses",
 "ak1500246326159": "- The capsule blunts inflammation, so meningitis develops slowly",
 "ak1500244315193": "- The polysaccharide capsule is antiphagocytic and is the antigen detected by latex agglutination",
 "ak1500245993331": "- Flucytosine adds a second target (DNA synthesis) to the polyene's pores",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
IMAGENS_VISTAS = {
 "mb50-histoplasma-intracelular.png": "lâmina 31: macrófagos cheios de pequenas leveduras (parasitismo intracelular), sem legenda — verso da nota do diagnóstico por cultura",
 "mb50-histoplasma-macroconidios.png": "lâmina 28: macroconídios tuberculados (estalagmósporos), sem legenda — verso da nota dos macroconídios",
}
REVISAO = {"despejo": "Despejo lido inteiro (46 notas novas) e as 82 associadas/mantidas relidas; imagens no verso de 2 notas mantidas conferidas (readback). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Reconhecer as micoses sistêmicas (endêmicas por dimórficos inalados × oportunistas) e, em cada uma — PCM, histoplasmose, candidose e criptococose —, "
             "agente, habitat, contágio, dimorfismo/forma no tecido, formas clínicas, diagnóstico e tratamento por cima; demais micoses do Trabulsi com cobertura mínima.",
 "centrais": [
   ("organizador das sistêmicas", "sh-1792065182152"),
   ("formas da PCM", "sh-1792065187180"),
   ("tropismo pelas meninges", "sh-1791630908168"),
 ],
 "exemplos": ["histórico da PCM e da histoplasmose", "mapas de mortalidade", "grupos filogenéticos", "criptococose em felino"],
 "outras_aulas": ["43 (antifúngicos, dimorfismo)", "44 (candidíase mucocutânea)", "51 (imunodeficiências)", "55 (identificação laboratorial)"],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
