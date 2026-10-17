# Especificação curada — 55 Prática de micologia (UC03 P3, Microbiologia; Profa. Kelly Ishida e equipe; 122 lâminas = Micologia
# Prática I–IV da turma: sequência diagnóstica e antifúngicos, aula de candidíase e criptococose, roteiros das práticas 1–4 e pranchas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas. Seções AnKing de Candida e Cryptococcus declaradas (as mesmas da 50):
# toda nota entra pela cópia NEBLI viva (50, 43, 44) ou sai com o motivo da 50. Os 7 cards de imagem "Which fungus is shown below?"
# que a 43, a 44 e a 50 deixaram para esta aula entram como AnKing. Bolores, dermatófitos, Sporothrix, Histoplasma e PCM das pranchas
# entram pelas cópias vivas das aulas 43/44/48/50. Autoral SÓ para lacuna provada (busca/cobertura.tsv).
import json as _json, pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb55-20261017a"
SHORT = "mb55n"
LESSON = "2026-uc03-microbiologia-55-pratica-micologia"
DECK = "NEBLI::UC03::P3::Microbiologia::Prática de micologia"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"mb55-{n}.jpg": f"img/mb55-{n}.jpg" for n in ("zimograma", "niger", "penicillium", "rubrum", "biofilme")}
IMG = lambda n, w=460: f'<img src="mb55-{n}.jpg" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (Candida e Cryptococcus em Bootcamp, FirstAid, Physeo, Pixorize, SketchyMicro; "
         "Dermatophytes, Tinea, Malassezia, Sporothrix, Aspergillus, Mucor e antifúngicos para conferir cópias; busca/secoes); palavra-chave "
         "em AnKing e Referências Externas (busca/anking.txt: zymogram, auxanogram, krusei/glabrata, biofilm, niger/melanin, urease em "
         "dermatófitos, fungicidal, Penicillium, rubrum, germ tube, chlamydospore, CHROMagar, India ink, 'Which fungus is shown'); "
         "significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")

# Notas das seções: entra a cópia NEBLI viva; sai com o motivo da 50 o que a 50 recusou (toxicidade, imunodeficiências, conduta).
_TOX = "toxicidade/administração de antifúngico: farmacologia clínica, fora do recorte"
_IMU = "imunologia (imunodeficiências/hipersensibilidade): aulas 51/64"
_SAI = {
 1500234392681: _IMU, 1486952733427: _IMU, 1487642773652: _IMU, 1487727763491: _IMU, 1520351135706: _IMU, 1585609953732: _IMU,
 1474580722813: "conduta após corticoide inalado", 1500236384725: "Gardnerella: outro assunto",
 1516128968450: "vaginose por Gardnerella: outro assunto", 1584393298504: "infecções no diabetes em geral: outro assunto",
 1502068052536: "critério de AIDS: virologia (HIV)", 1581259369271: "esofagite viral: outro assunto",
 1509743058195: "repete o card dos polienos que se ligam ao ergosterol (sh-1791557942183)",
 1509745961686: "fluconazol na candidíase vaginal: conduta", 1509746017401: "tratamento da esofagite candidiásica no HIV: conduta",
 1509742681361: _TOX,
}
for _n in (1509743284999, 1509743336397, 1509743451213, 1509743517947, 1509743634123, 1509743670062, 1509743767890, 1509743833529,
           1509743957410, 1509744002911, 1509744066944, 1509744667080, 1509744794419, 1509747124822, 1509747259788, 1509752610104,
           1509755342899, 1509755647704, 1509747054868):
    _SAI[_n] = _TOX
_IMAGEM = {1556238737112, 1556238830946, 1556238884073}  # entram como AnKing (cards de imagem)
_COP = _json.loads((HERE / "io" / "copias.json").read_text(encoding="utf-8"))
EXCLUIDOS = [(int(n), _SAI[int(n)]) for n in _COP if int(n) in _SAI] + \
            [(int(n), f"entra a cópia NEBLI viva (sh-{v[2][0][0]})") for n, v in _COP.items() if int(n) not in _SAI and v[2]] + [
 (1556238791179, "imagem de Blastomyces: espécie fora das pranchas desta aula (micoses sistêmicas, aula 50)"),
 (1556238845918, "imagem de Coccidioides: espécie fora das pranchas desta aula (micoses sistêmicas, aula 50)"),
 (1638739018234, "ácido bórico para C. glabrata: conduta"),
]
FORA_DO_RECORTE = [
 "Interações ecológicas entre fungos, metabólitos industriais (ácido cítrico, enzimas, vitaminas, pigmentos) e antimicrobianos naturais (alho, cravo): ilustração da prática.",
 "Números de epidemiologia (incidências, mortalidades, genótipos VNI/VGII por região) e guias de dose (IDSA, SBI): Tab (§4).",
 "Passo a passo de bancada (pour plate, diluição seriada, colônia gigante, método da isca, kits e Vitek): procedimento; entra o princípio de cada teste.",
 "Toxicidades e condutas dos antifúngicos: farmacologia clínica.",
]
A_, B_, C_, D_, E_, F_ = ("A-diagnostico", "B-fungo-e-antifungicos", "C-candida", "D-cryptococcus", "E-praticas", "F-pranchas")

CARDS = [
 # ---------- A. Sequência diagnóstica (lâminas 1–6) ----------
 sh(1791626784376, "verde", A_, "KOH clareia raspados para o exame direto", 1, "V-pilar: lâminas 1, 45, 79 (exame direto com KOH); card da 44"),
 sh(1791630907794, "verde", A_, "Auxanograma: assimilação de C e N", 3, "V-pilar: lâminas 2–3, 49, 85; autoral da 50"),
 au("au-zimograma", "In the <b>zymogram</b>, yeast fermentation of a sugar is read as gas trapped in an inverted {{c1::Durham tube}}",
    "V-pilar", A_, "Zimograma: fermentação com tubo de Durham", 5, "lâminas 4–5, 49 e 85 (zimograma)",
    extra="- The auxanogram tests assimilation (growth); the zymogram tests fermentation<br>"
          "- Together, the two profiles identify the yeast species<br>" + IMG("zimograma")),
 sh(1791630910843, "verde", A_, "Urease: Cryptococcus positivo, Candida negativo", 6, "V-pilar: lâminas 6, 84 e 122; card da 50"),
 # ---------- B. O fungo e os antifúngicos (lâminas 7–19) ----------
 sh(1791557940956, "azul", B_, "Parede de quitina e β-glucana", 7, "A-aula: lâminas 7 e 13 (parede com quitina); card da 43"),
 sh(1791557941506, "azul", B_, "Ribossomos 80S", 7, "A-aula: lâminas 7 e 13; card da 43"),
 sh(1791557941207, "azul", B_, "Ergosterol na membrana fúngica", 9, "A-aula: lâminas 9 e 17 (ergosterol no lugar do colesterol); card da 43"),
 sh(1791557942482, "azul", B_, "Toxicidade da anfotericina B pelo colesterol", 9, "A-aula: lâmina 9 (semelhança entre as células); card da 43"),
 sh(1792170503828, "azul", B_, "Polienos: anfotericina B e nistatina", 11, "A-aula: lâmina 11; card da 43"),
 sh(1791557942183, "azul", B_, "Polienos ligam ergosterol e formam poros", 11, "A-aula: lâminas 11, 18–19 e 53; card da 43"),
 sh(1792170504781, "azul", B_, "Azóis e alilaminas inibem a síntese de ergosterol", 11, "A-aula: lâminas 11 e 53 (esqualeno → ergosterol); card da 43"),
 sh(1792170504428, "azul", B_, "Azóis inibem a 14α-desmetilase", 11, "A-aula: lâminas 11 e 53; card da 43"),
 sh(1792170505829, "azul", B_, "Flucitosina inibe a síntese de DNA/RNA", 12, "A-aula: lâmina 12; card da 43"),
 sh(1791557942752, "azul", B_, "5-FC vira 5-FU na célula fúngica", 12, "A-aula: lâmina 12 (análogo de pirimidina); card da 43"),
 sh(1792170505578, "azul", B_, "Antifúngico metabolizado a 5-FU", 12, "A-aula: lâmina 12; card da 43"),
 sh(1792170506078, "rosa", B_, "Citosina desaminase", 12, "R-detalhe: lâmina 12; card da 43"),
 sh(1792170502028, "azul", B_, "Aflatoxina do Aspergillus e carcinoma hepatocelular", 15, "A-aula: lâminas 15–16 (micotoxinas); card da 43"),
 sh(1792170508078, "rosa", B_, "α-amanitina inibe a RNA polimerase II", 15, "R-detalhe: lâminas 15–16 (micetismo por Amanita); card da 43"),
 sh(1791557942007, "azul", B_, "Equinocandinas inibem a β-glucana sintase", 19, "A-aula: lâminas 18–19 e 53 (caspofungina); card da 43"),
 # ---------- C. Candidíase (lâminas 20–55) ----------
 sh(1792175035737, "azul", C_, "Profundidade de cada micose", 21, "A-aula: lâmina 21 (classificação das micoses); organizador da 44"),
 sh(1792170501780, "azul", C_, "Micose grave no imunocomprometido", 23, "A-aula: lâminas 23–24 (oportunistas); card da 43"),
 sh(1791630908792, "azul", C_, "Candida: oportunista mais comum", 28, "A-aula: lâminas 28 e 32; card da 50"),
 sh(1791630908669, "azul", C_, "Candida na microbiota", 28, "A-aula: lâminas 28–30 (levedura comensal, transmissão endógena); card da 50"),
 sh(1792170507325, "azul", C_, "Candida albicans é dimórfica", 28, "A-aula: lâmina 28 (levedura, pseudo-hifa, tubo germinativo, hifa); card da 43"),
 sh(1792170507578, "rosa", C_, "Candida inverte a regra do dimorfismo", 28, "R-detalhe: lâmina 28; card da 43"),
 sh(1791630907544, "azul", C_, "Levedura com pseudo-hifas a 20 °C", 28, "A-aula: lâminas 28 e 45; card da 50"),
 sh(1791630909466, "azul", C_, "Tubo germinativo (hifa verdadeira) a 37 °C", 28, "A-aula: lâminas 28, 35 e 48; card da 50"),
 sh(1791630909042, "azul", C_, "Vulvovaginite com corrimento em nata", 30, "A-aula: lâminas 30 e 39; card da 50"),
 sh(1792175043258, "azul", C_, "Candidíase oral e esofágica no imunocomprometido", 30, "A-aula: lâminas 30 e 43; card da 44"),
 sh(1792176897909, "azul", C_, "Esofagite candidiásica", 30, "A-aula: lâminas 30 e 43 (sugestiva de AIDS); card da 50"),
 sh(1792176898257, "azul", C_, "Esofagite com CD4 < 100", 30, "A-aula: lâmina 30; card da 50"),
 sh(1792176898506, "azul", C_, "Pseudomembranas brancas no esôfago", 43, "A-aula: lâmina 43 (múltiplas placas esbranquiçadas); card da 50"),
 au("au-krusei", "<b>Candida krusei</b> is intrinsically resistant to {{c1::fluconazole}}, so species identification guides treatment",
    "A-aula", C_, "C. krusei resiste ao fluconazol", 32, "lâmina 32 (perfil epidemiológico mudando)",
    extra="- C. glabrata is less susceptible to fluconazole; C. auris and C. haemulonii are multidrug resistant<br>"
          "- Non-albicans species are rising in candidemia"),
 ak("ak-glabrata", 1638738986293, "A-step", C_, "C. glabrata resiste aos azóis", 32, "lâmina 32 (C. glabrata menos sensível ao fluconazol)"),
 sh(1791630907293, "azul", C_, "Diabetes predispõe", 33, "A-aula: lâminas 33, 39 e 40; card da 50"),
 sh(1791630908917, "azul", C_, "Medicamentos que predispõem à candidíase vaginal", 33, "A-aula: lâmina 33 (antibióticos, corticoides); card da 50"),
 sh(1792175042987, "azul", C_, "Corticoide inalado → candidíase orofaríngea", 33, "A-aula: lâmina 33 (corticosteroides); card da 44"),
 sh(1792176899406, "azul", C_, "Nutrição parenteral e candidemia", 33, "A-aula: lâminas 33 e 44 (cateteres e sondas); card da 50"),
 sh(1791626779153, "azul", C_, "Deficiência de T → candidíase superficial", 33, "A-aula: lâmina 33 (HIV); card da 44"),
 sh(1791630907418, "azul", C_, "Neutropenia → candidíase disseminada", 33, "A-aula: lâminas 33 e 43 (terapia contra o câncer); card da 50"),
 sh(1792175043737, "rosa", C_, "Candidíase mucocutânea crônica: IL-17", 33, "R-detalhe: lâmina 34 (condições do hospedeiro); card da 44"),
 sh(1792176899657, "azul", C_, "Endocardite candidiásica no usuário de droga IV", 33, "A-aula: lâmina 44 (candidemia); card da 50"),
 sh(1792176900006, "rosa", C_, "Endocardite candidiásica: valva tricúspide", 33, "R-detalhe: lâmina 44; card da 50"),
 sh(1791630907168, "azul", C_, "Adesinas", 35, "A-aula: lâmina 35 (adesinas, SAPs, fosfolipases); autoral da 50"),
 au("au-biofilme", "<b>Candida biofilms</b> on catheters and prostheses make the yeast resistant to azoles and {{c1::amphotericin B}}",
    "A-aula", C_, "Biofilme e resistência", 37, "lâminas 36–37 e 44 (biofilme em cateter e prótese)",
    extra="- Biofilm: cells attached to a surface and embedded in an extracellular matrix, with a phenotype different from free cells<br>"
          "- Candidemia often starts from a colonized catheter<br>" + IMG("biofilme")),
 sh(1792176899006, "azul", C_, "Candida não altera o pH vaginal", 39, "A-aula: lâmina 39 (vulvovaginite); card da 50"),
 sh(1792175045486, "rosa", C_, "Candidíase vaginal não ocorre com pH > 4,5", 39, "R-detalhe: lâmina 39; card da 44"),
 sh(1792176898756, "azul", C_, "Corrimento em nata = Candida", 39, "A-aula: lâmina 39; card da 50"),
 sh(1791626779028, "azul", C_, "Sapinho: exsudato branco na mucosa", 40, "A-aula: lâmina 40 (candidíase oral); card da 44"),
 sh(1792175041987, "azul", C_, "Placas que se raspam", 40, "A-aula: lâmina 40 (pseudomembranosa, placas destacáveis); card da 44"),
 sh(1792175042236, "rosa", C_, "Leucoplasia não se raspa", 40, "R-detalhe: lâmina 40 (diferencial); card da 44"),
 sh(1791626779277, "azul", C_, "Candidíase intertriginosa no obeso", 41, "A-aula: lâmina 41; card da 44"),
 sh(1792175044837, "azul", C_, "Dermatite de fralda por Candida", 41, "A-aula: lâmina 41 (crianças que usam fraldas); card da 44"),
 sh(1792176901357, "azul", C_, "Anfotericina B nas infecções graves", 43, "A-aula: lâmina 43 (candidíase disseminada); card da 50"),
 sh(1792176900503, "azul", C_, "Disseminada: caspofungina", 43, "A-aula: lâminas 43 e 53; card da 50"),
 sh(1792176900979, "azul", C_, "Anfotericina B ou equinocandina na candidíase sistêmica", 43, "A-aula: lâminas 43 e 53; card da 50"),
 sh(1791626784503, "azul", C_, "Pseudo-hifas no KOH sugerem Candida", 45, "A-aula: lâminas 45 e 99; card da 44"),
 sh(1791557943483, "azul", C_, "Pseudo-hifas com brotamento: Candida", 45, "A-aula: lâminas 45 e 99; card da 43"),
 sh(1792176900256, "rosa", C_, "Candida contamina cultura de escarro", 45, "R-detalhe: lâmina 45 (escarro como material); card da 50"),
 sh(1791647818820, "azul", C_, "Ágar cromogênico: C. albicans verde", 47, "A-aula: lâmina 47 (CHROMagar Candida); autoral da 27"),
 sh(1791630909341, "verde", C_, "Tubo germinativo positivo indica C. albicans", 48, "V-pilar: lâminas 48, 85 e 121 (soro a 37 °C por 2–3 h); card da 50"),
 ak("ak-img-tubo", 1556238737112, "V-hy", C_, "Imagem: tubos germinativos", 48, "lâminas 48 e 121 (prancha do tubo germinativo)"),
 sh(1792173499322, "azul", C_, "Clamidoconídios", 48, "A-aula: lâminas 48, 85 e 100 (microcultivo em ágar fubá); card da 43"),
 ak("ak-img-candida", 1556238830946, "V-hy", C_, "Imagem: Candida albicans", 48, "lâminas 48, 99 e 100 (pranchas de Candida)"),
 sh(1792175044337, "azul", C_, "Nistatina age contra Candida", 53, "A-aula: lâmina 53 (tratamento das candidíases); card da 44"),
 sh(1792175044587, "azul", C_, "Nistatina na candidíase oral e vaginal", 53, "A-aula: lâmina 53; card da 44"),
 sh(1792175043988, "azul", C_, "Candidíase oral: nistatina", 53, "A-aula: lâmina 53; card da 44"),
 sh(1792175045837, "azul", C_, "Infecção local leve: azol tópico", 53, "A-aula: lâmina 53; card da 44"),
 # ---------- D. Criptococose (lâminas 56–72) ----------
 sh(1791630909592, "verde", D_, "Cryptococcus é encapsulado", 57, "V-pilar: lâminas 57, 63 e 102; card da 50"),
 sh(1791557941633, "azul", D_, "Levedura com cápsula polissacarídica", 57, "A-aula: lâmina 57 (basidiomiceto leveduriforme); card da 43"),
 sh(1792176905980, "rosa", D_, "Cryptococcus de 5–10 µm", 57, "R-detalhe: lâmina 57; card da 50"),
 sh(1791630909844, "azul", D_, "Fezes de pombo e solo", 58, "A-aula: lâmina 58; card da 50"),
 sh(1791630908043, "azul", D_, "C. gattii e eucalipto", 58, "A-aula: lâminas 58 e 61 (C. gattii em imunocompetentes no Norte/Nordeste); autoral da 50"),
 sh(1791630910018, "azul", D_, "Inalação: infecção primária pulmonar", 58, "A-aula: lâminas 58 e 62; card da 50"),
 sh(1791630909718, "azul", D_, "Oportunista do imunocomprometido", 60, "A-aula: lâmina 60 (AIDS); card da 50"),
 sh(1791630910143, "azul", D_, "Causa mais comum de meningite fúngica", 60, "A-aula: lâmina 60; card da 50"),
 sh(1792176904256, "azul", D_, "Meningite fúngica no HIV", 60, "A-aula: lâmina 60; card da 50"),
 sh(1792176905730, "azul", D_, "Cápsula de antígenos polissacarídicos", 63, "A-aula: lâminas 63 e 70 (GXM); card da 50"),
 sh(1791557941758, "azul", D_, "Cápsula: principal fator de virulência", 63, "A-aula: lâmina 63; card da 43"),
 sh(1791744820056, "verde", D_, "Cápsula bloqueia fagocitose e apresentação", 63, "V-prova: lâmina 63; prova 2024 P3 2.5 (vantagens da cápsula); card da 50"),
 sh(1791630908168, "azul", D_, "Tropismo pelas meninges", 65, "A-aula: lâmina 65 (meningoencefalite em 90%); autoral da 50"),
 sh(1792176904507, "azul", D_, "Pneumonia e meningite", 65, "A-aula: lâminas 65–66; card da 50"),
 sh(1792176904857, "azul", D_, "Meningoencefalite de curso indolente", 65, "A-aula: lâmina 65 (cefaleia, febre rara); card da 50"),
 sh(1792176897656, "azul", D_, "Cryptococcus e Coccidioides causam meningite", 65, "A-aula: lâmina 65 (forma disseminada com SNC); card da 50"),
 sh(1792176905108, "rosa", D_, "RM em bolhas de sabão", 65, "R-detalhe: lâmina 65 (RM); card da 50"),
 sh(1791630910669, "azul", D_, "Nanquim mostra a cápsula", 67, "A-aula: lâminas 1, 67, 86 e 102; card da 50"),
 ak("ak-img-cripto", 1556238884073, "V-hy", D_, "Imagem: Cryptococcus no nanquim", 67, "lâminas 67 e 102 (prancha de Cryptococcus)"),
 sh(1792176905479, "rosa", D_, "Lavado broncoalveolar no diagnóstico", 67, "R-detalhe: lâmina 67 (escarro como material); card da 50"),
 sh(1791744819680, "azul", D_, "Mucicarmim cora a cápsula", 68, "A-aula: lâminas 68 e 101; card da 50"),
 sh(1792150762061, "azul", D_, "Prata (GMS) cora fungos", 68, "A-aula: lâminas 68 e 96 (Gomori-Grocott); card do Diagnóstico patológico"),
 sh(1791630910543, "azul", D_, "Cultura em ágar Sabouraud", 69, "A-aula: lâminas 46 e 69; card da 50"),
 au("au-niger", "On <b>niger seed agar</b>, Cryptococcus forms brown colonies because its phenol oxidase produces {{c1::melanin}}",
    "A-aula", D_, "Ágar niger: colônias marrons pela melanina", 69, "lâminas 64 (melanina) e 69 (meio semente de niger)",
    extra="- Melanin protects the fungus against oxidative stress and some antifungals<br>"
          "- On Sabouraud agar the colonies are creamy and mucoid because of the capsule<br>" + IMG("niger")),
 sh(1792176906327, "azul", D_, "Látex detecta o antígeno capsular", 70, "A-aula: lâmina 70; card da 50"),
 sh(1792176906681, "azul", D_, "Látex no líquor: teste mais sensível", 70, "A-aula: lâmina 70 (método de escolha no líquor); card da 50"),
 sh(1792176906931, "azul", D_, "Meningite: anfotericina B + flucitosina", 72, "A-aula: lâmina 72; card da 50"),
 # ---------- E. Roteiros das práticas 1–4 (lâminas 73–97) ----------
 sh(1791557940633, "verde", E_, "Levedura cremosa × bolor cotonoso", 73, "V-prova: lâminas 73 e 76; prova 2024 P3 2.6 (levedura × dermatófito filamentoso); card da 43"),
 sh(1792065024004, "verde", E_, "Formas dos fungos e dimorfismo", 73, "V-prova: lâminas 73–74 e 97; prova 2018 P2 1.1 (dimorfismo térmico); organizador da 43"),
 sh(1792173501367, "azul", E_, "Hifas cenocíticas", 74, "A-aula: lâmina 74 (hifas com ou sem septos); card da 43"),
 sh(1792173501047, "azul", E_, "Conídios × esporangiósporos", 74, "A-aula: lâmina 74 (esporos assexuados); card da 43"),
 sh(1791557943732, "azul", E_, "Aspergillus forma conidióforos", 74, "A-aula: lâminas 74 e 98; card da 43"),
 sh(1792170506578, "azul", E_, "Aspergillus: hifas septadas em ângulo agudo", 75, "A-aula: lâminas 75 e 98; card da 43"),
 sh(1791557944724, "azul", E_, "Mucor/Rhizopus: hifas não septadas em 90°", 75, "A-aula: lâminas 74–75 e 115; card da 43"),
 sh(1791557939905, "rosa", E_, "Rhizopus, bolor do pão", 75, "R-detalhe: lâminas 75 e 115; card da 43"),
 sh(1791626783027, "azul", E_, "Malassezia causa pitiríase versicolor", 77, "A-aula: lâminas 77 e 114; card da 44"),
 sh(1791626784004, "azul", E_, "Malassezia: espaguete com almôndegas", 77, "A-aula: lâminas 77 e 114 (cacho de uva com hifas curtas); card da 44"),
 sh(1792175049087, "azul", E_, "Malassezia produz ácidos que lesam melanócitos", 77, "A-aula: lâmina 77 (manchas de cor variável); card da 44"),
 sh(1792175035986, "verde", E_, "Os três gêneros de dermatófitos", 77, "V-prova: lâminas 77 e 103; prova 2019 P2 3.1 (gêneros e fontes); card da 44"),
 sh(1791557945582, "azul", E_, "Dermatófitos têm queratinase", 77, "A-aula: lâmina 77 (predileção pela queratina); card da 44"),
 sh(1791626776253, "azul", E_, "Sítios de cada gênero", 77, "A-aula: lâmina 77; organizador da 44"),
 sh(1791626775626, "verde", E_, "Geofílicos, zoofílicos e antropofílicos", 78, "V-prova: lâminas 78 e 80; prova 2019 P2 3.1 (prováveis fontes de contato); card da 44"),
 sh(1792175047836, "azul", E_, "Ectotrix × endotrix", 79, "A-aula: lâminas 79, 108 e 120; card da 44"),
 sh(1792175047235, "azul", E_, "Microsporum fluoresce à lâmpada de Wood", 79, "A-aula: lâminas 78, 108 e 120; card da 44"),
 sh(1791626781378, "azul", E_, "Sabouraud com cloranfenicol e cicloheximida", 79, "A-aula: lâminas 79 e 96 (Mycosel); card da 44"),
 au("au-urease-tricho", "Among dermatophytes, <b>Trichophyton mentagrophytes</b> is urease {{c1::positive}}, whereas T. rubrum is urease negative",
    "R-detalhe", E_, "Urease: T. mentagrophytes + × T. rubrum −", 80, "lâminas 80–81 (prova da urease para dermatófitos)",
    extra="- The urease test separates the two species when micromorphology is doubtful"),
 sh(1791668526789, "azul", E_, "Concentração inibitória mínima", 88, "A-aula: lâminas 88–91 (CIM no antifungigrama); card da 32"),
 au("au-cfm", "The lowest <b>antifungal</b> concentration that kills the fungus, rather than only inhibiting it, is the {{c1::minimum fungicidal concentration}}",
    "A-aula", E_, "Concentração fungicida mínima", 88, "lâmina 88 (definições: CIM, CFM, fungistático, fungicida)",
    extra="- Fungistatic drugs inhibit growth (azoles against Candida); fungicidal drugs kill (amphotericin B)<br>"
          "- The antifungigram finds the MIC by standardized broth dilution (CLSI)"),
 sh(1791668527164, "rosa", E_, "Concentração bactericida mínima", 88, "R-detalhe: lâmina 88 (o equivalente bacteriano da CFM); card da 32"),
 sh(1791630904467, "azul", E_, "PCM: roda de leme", 93, "A-aula: lâminas 93 e 112; card da 50"),
 sh(1791630905768, "azul", E_, "Histoplasma: macrófagos com corpos ovais", 94, "A-aula: lâminas 94 e 105 (parasitismo intracelular); card da 50"),
 sh(1791630906243, "azul", E_, "Histoplasma: macroconídios tuberculados a 25 °C", 94, "A-aula: lâminas 94 e 106 (estalagmósporos); card da 50"),
 sh(1791628674574, "azul", E_, "Sporothrix: charuto no tecido, bolor nas plantas", 95, "A-aula: lâminas 95–96 e 116; card da 48"),
 sh(1791628674273, "azul", E_, "Levedura em charuto", 95, "A-aula: lâminas 95–96 (naveta ou charuto); card da 48"),
 sh(1791628672874, "azul", E_, "Espinho de rosa", 95, "A-aula: lâmina 95; card da 48"),
 sh(1792175890134, "azul", E_, "Linfangite nodular ascendente", 95, "A-aula: lâmina 95; card da 48"),
 sh(1792175890736, "rosa", E_, "Hifas como galhos de roseira", 96, "R-detalhe: lâminas 96 e 116 (conídios em margarida); card da 48"),
 # ---------- F. Pranchas (lâminas 98–122) ----------
 ak("ak-img-aspergillus", 1556238807061, "V-hy", F_, "Imagem: Aspergillus fumigatus", 98, "lâmina 98 (prancha de Aspergillus)"),
 ak("ak-img-histo", 1556238858660, "V-hy", F_, "Imagem: Histoplasma capsulatum", 106, "lâminas 105–106 (pranchas de Histoplasma)"),
 ak("ak-img-malassezia", 1556238897815, "V-hy", F_, "Imagem: Malassezia furfur", 107, "lâminas 107 e 114 (pranchas de Malassezia e pitiríase)"),
 sh(1792175048086, "azul", F_, "Macroconídios fusiformes de M. canis", 109, "A-aula: lâmina 109 (Microsporum canis); card da 44"),
 au("au-penicillium", "<b>Penicillium</b> carries chains of conidia on branched conidiophores shaped like a {{c1::brush}}",
    "A-aula", F_, "Penicillium: conidióforo em pincel", 113, "lâminas 15 e 113 (prancha de Penicillium; penicilina)",
    extra="- Aspergillus instead ends in a swollen vesicle<br>- P. notatum and P. chrysogenum produce penicillin<br>" + IMG("penicillium", 400)),
 ak("ak-img-rhizopus", 1556238870116, "V-hy", F_, "Imagem: Rhizopus", 115, "lâmina 115 (prancha de Rhizopus)"),
 au("au-rubrum", "<b>Trichophyton rubrum</b> colonies show a wine-red pigment on the {{c1::reverse}} of the plate",
    "R-detalhe", F_, "T. rubrum: reverso vermelho", 119, "lâmina 119 (prancha de T. rubrum)",
    extra="- T. mentagrophytes has a flat, powdery colony without pigment and many round microconidia<br>" + IMG("rubrum", 400)),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak-glabrata": "- In the lecture: C. glabrata is less susceptible to fluconazole and C. krusei is intrinsically resistant",
 "ak-img-tubo": "- Germ tube test: yeast in serum at 37 °C for 2–3 h; a tube without constriction = C. albicans",
 "ak-img-candida": "- Pseudohyphae with budding yeasts; on cornmeal agar C. albicans forms chlamydoconidia",
 "ak-img-cripto": "- India ink shows a clear halo (capsule) around the yeast; mucicarmine stains the capsule red in tissue",
 "ak-img-aspergillus": "- Septate hyphae branching at acute angles; conidiophore with a vesicle and chains of conidia",
 "ak-img-histo": "- Tissue: small yeasts inside macrophages; culture at 25 °C: tuberculate macroconidia",
 "ak-img-malassezia": "- Skin scraping in KOH: clusters of round yeasts with short hyphae ('spaghetti and meatballs')",
 "ak-img-rhizopus": "- Nonseptate (coenocytic) hyphae, rhizoids and sporangia full of sporangiospores",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (zimograma, biofilme, ágar niger, Penicillium, T. rubrum e os 7 cards de imagem) estão nos cards do conceito"
SLIDE_SEM_ALT = "foto da própria aula ou prancha do laboratório, sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "mb55-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "mb55-zimograma.jpg": "Lâmina 4: dois tubos de fermentação (glicose, lactose) com tubo de Durham invertido; verso de au-zimograma.",
 "mb55-biofilme.jpg": "Lâmina 36: MEV de biofilme de Candida (leveduras, hifas e matriz) e esquema da comunidade aderida; verso de au-biofilme.",
 "mb55-niger.jpg": "Lâmina 69: culturas de Cryptococcus em SDA (creme, mucoide) e em ágar niger (colônias marrons); verso de au-niger.",
 "mb55-penicillium.jpg": "Lâmina 113: prancha de Penicillium (colônia esverdeada; conidióforo em pincel no azul de algodão); verso de au-penicillium.",
 "mb55-rubrum.jpg": "Lâmina 119: prancha de T. rubrum (colônia branca com reverso vermelho; microconídios em lágrima); verso de au-rubrum.",
}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (16 notas novas, 16 cards; frentes, clozes, versos, imagens e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Saber a sequência diagnóstica micológica (KOH, nanquim, cultura, auxanograma, zimograma, urease), identificar Candida "
             "(tubo germinativo, clamidoconídios, ágar cromogênico) e Cryptococcus (cápsula, nanquim, mucicarmim, látex, niger), "
             "reconhecer bolores, dermatófitos e dimórficos nas pranchas e interpretar o antifungigrama (CIM, CFM).",
 "centrais": [
   ("sequência diagnóstica", "sh-1791626784376", "sh-1791630907794", "au-zimograma", "sh-1791630910843"),
   ("identificação de Candida", "sh-1791630909466", "sh-1791630909341"),
   ("Cryptococcus", "sh-1791630909592", "sh-1791744820056", "sh-1791630910669"),
   ("bolor × levedura", "sh-1791557940633", "sh-1792065024004"),
   ("dermatófitos", "sh-1792175035986", "sh-1791626775626"),
 ],
 "exemplos": ["Vitek 2 e kits comerciais", "alho e cravo", "genótipos VNI/VGII", "guias IDSA e SBI"],
 "outras_aulas": [("biologia dos fungos e antifúngicos", "43 Biologia dos fungos (sh)"), ("dermatófitos e Malassezia", "44 Micoses cutâneas (sh)"),
                  ("Sporothrix", "48 Micoses subcutâneas (sh)"), ("Candida, Cryptococcus, Histoplasma, PCM", "50 Micoses sistêmicas (sh)"),
                  ("CIM e CBM", "32 Antibióticos e resistência (sh)"), ("meios cromogênicos", "27 Fisiologia bacteriana (sh)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
