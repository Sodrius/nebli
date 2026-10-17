# Especificação curada — Radiografia e ultrassom: princípios da radiografia convencional e da ultrassonografia (UC03 P1, Radiologia;
# Preceptoria 2024; 41 lâminas). Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing → externos (Ankisthesia, MCAT) → associados da 02 por sh() → autoral SÓ para lacuna provada em busca/cobertura.tsv (gate duro).
# Modelo vivo: arquivos-trabalho/deck-aula-uc03-rd02-diagnostico-radiologico-v2-2026-10-16/spec.py (16/10).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4  # 3 = teto de autoral (20%; 35% com AUTORAL_EXCECAO); 4 = todo AnKing das SECOES_DA_AULA entra ou é excluído com motivo
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06: todo AnKing do conteúdo entra
    "_FirstAid_04_Pathology_03_Neoplasia_10_Carcinogens_Radiation_Ionizing.txt",
    "_Bootcamp_Cardiology_02_Anatomy_02_Cardiac_Silhouette_Chest_Radiography.txt",
]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"  # F-20261015-CLAUDE-06: liga os gates duros (cobertura_anking, cores_rubrica, inducao_clozes); não remover
RUN_ID = "uc03-rd04-20261016a"
SHORT = "rd04"
LESSON = "2026-uc03-radiologia-04-radiografia-ultrassom"
DECK = "NEBLI::UC03::P1::Radiologia::Radiografia e ultrassom"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-10 + ANTI-EXEMPLARES §1–16, 16/10/2026"
MEDIA = {f"rd04-{n}.png": f"img/rd04-{n}.png" for n in ("tubo", "densidades", "magnificacao", "pa-ap", "silhueta", "sombra", "reforco")}
IMG = lambda n, w=420: f'<img src="rd04-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (16/10): seções de recurso do AnKing (FirstAid radiação ionizante, Bootcamp silhueta cardíaca, B&B chest x-rays; busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
EXCLUIDOS = [
 (1496159700902, "seção FirstAid ionizante: cânceres associados (LMA, LMC, tireoide) são carcinogênese da aula de neoplasia; a 02 já tem a tireoide"),
 (1555890636349, "duplicata MCAT de E = hc/λ = hf (fica 1554150651306, um card só)"),
 (1701779472592, "mnemônico PGR repete ext-frequencia (alta frequência = resolução, baixa = penetração)"),
 (1701744971045, "faixa 3–12 MHz e < 5 cm: número de sonda, sem ganho sobre ext-frequencia"),
 (1701780430346, "frequências e profundidades de sondas Sonosite: equipamento específico"),
 (1701783439046, "profundidade de plexos para bloqueio anestésico: fora do recorte"),
 (1701793231648, "zona focal: física avançada não dada na aula"),
 (1701809310916, "resolução axial e lateral: só no texto de apoio, sem lâmina nem fala"),
 (1701745110911, "ângulo de insonação e resolução temporal: física avançada"),
 (1701745337516, "visualização de agulha: US intervencionista"),
 (1701805714594, "anisotropia: US musculoesquelético, fora da aula"),
 (1701808670261, "anisotropia por tipo de tecido: US musculoesquelético"),
 (1701781530436, "aparência de nervo e músculo: US de bloqueio anestésico"),
 (1712696475481, "ângulo do Doppler < 20°: detalhe técnico não dado"),
 (1554151136934, "equação do Doppler (MCAT): física quantitativa"),
 (1555869007455, "definição genérica do Doppler: a 02 já tem a definição (sh-1792141769904)"),
 (1555857927065, "som é onda longitudinal: a aula ensina que precisa de meio (mc-vacuo), não o tipo de onda"),
 (1532044924215, "TC no estável × FAST no instável: repete ak-fast-hemorragia (o resto é manejo do trauma)"),
 (1493074820825, "conduta com FAST positivo: manejo do trauma, não objetivo da aula"),
 (1536707052087, "algoritmo do trauma abdominal fechado: manejo, fora da aula de princípios"),
 (1695746467105, "catarata por radiação apesar da blindagem: detalhe ocupacional"),
 (1475453229159, "cálculo de estruvita radiopaco: repete a ideia de ak-calculo-calcio"),
 (1475453306198, "cistina levemente radiopaca: gradação fina, sem ganho"),
 (1482978405717, "cálculo de colesterol radiotransparente: repete ak-calculo-urico"),
]
FORA_DO_RECORTE = [
 "Efeitos fotoelétrico e Compton, filme de sais de prata, grade antiespalhamento, kV/mA e dosimetria (bibliografia e e-book): nem lâmina, nem fala, nem prova.",
 "Qualidade técnica do RX de tórax (penetração, inspiração, rotação) e causas de hemitórax opaco (apostila guia): aulas de correlação radiologia-patologia.",
 "Imagem em espelho, imagem dupla e resolução axial/lateral (bibliografia do US): só no texto de apoio.",
 "Mamografia com compressão (monitoria): aplicação lateral; a ideia de espessura está em au-atenuacao.",
 "Escolha da modalidade por caso clínico e contrastes em detalhe: aulas 02 e 56 (associados por sh).",
]
A_, B_, C_, D_, E_, F_, G_, H_, I_, J_, K_ = ("A-radiacao", "B-tubo", "C-imagem-densidades", "D-efeito-biologico", "E-projecao-incidencias",
                                              "F-silhueta-orientacao", "G-us-vantagens", "H-fisica-us", "I-orientacao-ecogenicidade", "J-artefatos", "K-fast")

CARDS = [
 # ---------- A. Por que RX; radiação (lâminas 2–5) ----------
 sh(1792141773857, "azul", A_, "Forças e limites do RX", 2, "lâmina 2 (rápido, barato, acessível, leito); card da 02"),
 ak("ak-radon", 1473732893483, "R-detalhe", A_, "Fonte natural de radiação: radônio", 4, "lâmina 4 e transcrição (radionuclídeos, radiação natural)",
    extra_add="- Natural sources: unstable radionuclides and cosmic radiation; artificial: reactors, accelerators, X-ray tubes"),
 ak("ak-exposicao", 1517859988325, "A-step", A_, "Fontes artificiais: acidente nuclear e radioterapia", 4, "lâminas 4 e 14 (reatores; radioterapia); seção FirstAid ionizante"),
 ak("mc-espectro", 1555875239904, "A-aula", A_, "Espectro eletromagnético", 5, "lâmina 5 (raio X no espectro, entre UV e gama)", origin="MCAT",
    extra="- X-rays lie above ultraviolet and below gamma rays<br>- Wavelength about 10⁻¹² m: high energy, so they cross the body"),
 ak("mc-foton", 1554150651306, "R-detalhe", A_, "Energia do fóton cresce com a frequência", 5, "lâmina 5 e bibliografia (energia ∝ frequência; λ curto = alta energia)", origin="MCAT",
    extra_add="- So the short-wavelength X-ray has enough energy to ionize atoms"),
 # ---------- B. Tubo de raios X (lâminas 6–8) ----------
 au("au-tubo", "In the <b>X-ray tube</b>, a heated {{c1::tungsten}} filament releases electrons that high voltage accelerates to the anode",
    "V-prova", B_, "Produção do raio X no tubo", 6, "lâminas 6–8; provas 2024/2023/2018/2017 (“aquecimento de um filamento de tungstênio”); bibliografia aula 1",
    extra="- On hitting the tungsten target, about 99% of the energy becomes heat; most X-rays come from electrons braking near nuclei (bremsstrahlung)<br>"
          "- Tungsten: high atomic number and melting point<br>- Lead housing with one window aims the beam; oil cools; vacuum inside<br>" + IMG("tubo", 460)),
 # ---------- C. Formação da imagem e densidades (lâminas 9–13) ----------
 au("au-atenuacao", "Radiographic <b>brightness</b> reflects X-ray {{c1::attenuation}}, since tissues that absorb more leave the detector unexposed",
    "V-prova", C_, "Atenuação forma a imagem", 10, "lâminas 9–10 e 24; provas 2024 P2, 2023 P2, 2018 P1 (mecanismo: atenuação → radiopaco)",
    extra="- Attenuation grows with thickness, density and atomic number<br>- Air barely attenuates, so it is black (radiolucent)"),
 au("au-densidades", ORG("<b>Radiographic densities</b>, from black to white:<br>1. {{c1::Air}}<br>2. {{c1::Fat}}<br>3. {{c1::Water}} (soft tissue)<br>"
                         "4. {{c1::Calcium}} (bone)<br>5. {{c1::Metal}}"),
    "V-pilar", C_, "Cinco densidades radiológicas", 11, "lâminas 11–12; monitoria e bibliografia (cinco densidades); provas pedem o termo",
    extra="- Egg: air pocket black, yolk (fat) slightly darker than the white (water), shell (calcium) bright<br>" + IMG("densidades", 300)),
 sh(1792141774955, "verde", C_, "Termos de cada método (radiopaco, hiperecoico…)", 11, "lâminas 11 e 37; provas 2016/2015 (termo por modalidade); card da 02"),
 ak("ak-calculo-calcio", 1475453191411, "A-step", C_, "Cálculo de cálcio é radiopaco", 12, "densidade cálcio (lâmina 12); exemplo HY"),
 ak("ak-calculo-urico", 1475453264320, "A-step", C_, "Cálculo de ácido úrico é radiotransparente", 12, "par do anterior: sem cálcio, não atenua"),
 ak("ak-ferro-aspirina", 1538866997617, "R-detalhe", C_, "Ferro aparece no RX, aspirina não", 12, "densidade metal × partes moles (lâmina 12)"),
 ak("ak-enfisema", 1572812619218, "A-step", C_, "Enfisema: hipertransparência", 12, "prova 2025 P3 3.1 (hiperinsuflação); ar a mais escurece"),
 ak("ak-hemitorax", 1526312872269, "A-step", C_, "Pulmão colapsado: hemitórax opaco", 12, "ar a menos clareia (lâminas 11–12); apostila guia (hemitórax opaco)"),
 ak("ak-mieloma", 1481335826686, "A-step", C_, "Mieloma: lesões líticas radiotransparentes", 12, "prova 2024 P1 1.1 (lesões radiotransparentes do mieloma)",
    extra_add="- On X-ray: round, well-defined radiolucent areas where bone was destroyed"),
 sh(1792141768903, "azul", C_, "Contraste intrínseco × exógeno", 13, "lâmina 13 (densidades iguais → contraste); card da 02"),
 sh(1792141769157, "azul", C_, "Contraste de cada método (bário, iodo)", 13, "lâmina 13 e transcrição (bário no intestino, iodo nos vasos); card da 02"),
 # ---------- D. Efeito biológico (lâmina 14) ----------
 sh(1792117369271, "azul", D_, "Radiação ioniza a água em •OH", 14, "lâmina 14 (efeito indireto); card da 09"),
 ak("ak-radicais", 1496159743226, "A-step", D_, "Radicais hidroxila e carcinogênese", 14, "lâmina 14; seção FirstAid ionizante",
    extra_add="- Direct effect: radiation hits DNA itself; indirect effect: it splits water into •OH, which then damages DNA"),
 au("au-estocastico", "<b>Radiation effects</b> without a threshold, whose probability (not severity) rises with dose, are called {{c1::stochastic}}",
    "A-aula", D_, "Efeito estocástico: sem limiar", 14, "lâmina 14 (“nem sempre dose dependente”) e transcrição (estocásticos, acumulativos e silenciosos)",
    extra="- Example: cancer years after exposure<br>- Effects with a threshold (skin burn, cataract) are deterministic"),
 sh(1792141771005, "azul", D_, "Radiação cumulativa e teratogênica", 14, "lâmina 14; monitoria (efeito cumulativo e teratogênico); card da 02"),
 sh(1792141771761, "azul", D_, "Princípios da radioproteção", 14, "lâmina 14; prova 2017 P4 1.3; card da 02"),
 sh(1792141772006, "rosa", D_, "ALARA", 14, "lâmina 14 (proteção radiológica); card da 02"),
 # ---------- E. Projeção, incidências, magnificação (lâminas 15–24) ----------
 ak("ak-duas-incidencias", 1544202588173, "A-aula", E_, "Duas incidências perpendiculares", 16, "lâminas 16–20 (a projeção perde uma dimensão; PA + perfil)",
    extra_add="- A single view loses depth: an opacity on a PA film may lie in front of, inside or behind the lung; the lateral view places it"),
 sh(1792141767554, "azul", E_, "Plano sagital", 18, "lâmina 18 (planos e eixos); card da 02"),
 sh(1792141767807, "azul", E_, "Plano coronal", 18, "lâmina 18; card da 02"),
 sh(1792141768057, "azul", E_, "Plano transverso", 18, "lâmina 18; card da 02"),
 au("au-magnificacao", "An object far from the <b>detector</b> projects an enlarged image, an effect called {{c1::magnification}}",
    "V-pilar", E_, "Magnificação", 22, "lâminas 21–22 (pedras de tamanhos diferentes; sombra da lâmpada); monitoria; prova 2015 P1",
    extra="- X-rays diverge from a point source, like the shadow of an object moved toward a lamp<br>" + IMG("magnificacao", 360)),
 au("au-pa-ap", "A bedside <b>AP</b> chest film magnifies the heart and can mimic {{c1::cardiomegaly}}, so chest films are taken PA",
    "V-prova", E_, "PA × AP: falsa cardiomegalia", 23, "lâmina 23; prova 2015 P1 1.1 (por que PA); apostila ilustrativa",
    extra="- In PA the anterior chest, and so the heart, lies against the detector<br>- Bedridden patients can only be filmed AP<br>" + IMG("pa-ap", 460)),
 # ---------- F. Silhueta e orientação (lâminas 25–27) ----------
 au("au-silhueta", "Two structures of the same <b>density</b> in contact lose the border between them, called the {{c1::silhouette}} sign",
    "V-prova", F_, "Sinal da silhueta", 26, "lâminas 24–26; prova 2019 P1 1.11 (localizar a opacidade); monitoria",
    extra="- Air between them keeps both borders: the aorta shows in the chest (lung around it), not in the abdomen<br>"
          "- Right heart border lost → right middle lobe; left border lost → lingula<br>" + IMG("silhueta", 460)),
 ak("ak-atrio-silhueta", 1521427099917, "A-step", F_, "Átrio direito forma a borda direita do coração", 26, "seção Bootcamp silhueta; base do sinal da silhueta no lobo médio"),
 au("au-orientacao", "On a frontal <b>radiograph</b>, the patient's right side appears on the viewer's {{c1::left}}",
    "A-aula", F_, "Convenção de lateralidade", 27, "lâmina 27 (DIR à esquerda da imagem)",
    extra="- As if facing the patient; axial CT and transverse ultrasound use the same convention"),
 # ---------- G. US: vantagens, limites, Doppler (lâminas 28–30) ----------
 sh(1792141768558, "azul", G_, "Forças e limites do US", 29, "lâminas 29–30; card da 02"),
 sh(1792141775531, "verde", G_, "Métodos sem radiação ionizante", 29, "lâmina 29; prova 2025 P2 (vantagem do US); card da 02"),
 sh(1792141769904, "azul", G_, "Efeito Doppler", 29, "lâmina 29 (Doppler); prova 2024 P1 2.7; card da 02"),
 ak("mc-doppler-perto", 1555869206450, "A-aula", G_, "Doppler: aproximação aumenta a frequência", 29, "prova 2024 P1 2.7 (frequência sobe quando o sangue se aproxima)", origin="MCAT",
    extra_add="- In Doppler ultrasound, blood flowing toward the probe raises the echo frequency"),
 ak("mc-doppler-longe", 1555869246686, "R-detalhe", G_, "Doppler: afastamento diminui a frequência", 29, "par do anterior (prova 2024 P1 2.7)", origin="MCAT",
    extra_add="- Blood flowing away from the probe lowers the echo frequency"),
 ak("ext-doppler-cor", 1610488754352, "R-detalhe", G_, "Doppler colorido: velocidade no matiz", 29, "Mello (cor pelo sentido, matiz pela velocidade)", origin="Ankisthesia",
    extra="- BART: blue away, red toward the probe<br><img src=\"aw.png\">"),
 ak("ext-bamb", 1701779007226, "R-detalhe", G_, "Atenuação: osso > ar > músculo > sangue", 30, "lâmina 30 (gás e osso limitam o US)", origin="Ankisthesia",
    text="Tissues ranked by ultrasound <b>attenuation</b> (BAMB): {{c1::Bone::B…}} &gt; {{c1::Air::A…}} &gt; {{c1::Muscle::M…}} &gt; {{c1::Blood::B…}}",
    extra="- Bone and gas block the beam, so structures behind them cannot be seen; fat in obesity also attenuates"),
 # ---------- H. Física do US (lâminas 31–34) ----------
 ak("mc-vacuo", 1555867838526, "A-aula", H_, "Som precisa de meio", 31, "lâmina 31 (onda mecânica que precisa de meio)", origin="MCAT",
    extra="- Ultrasound is a mechanical wave, unlike X-rays (electromagnetic), which cross a vacuum"),
 ak("mc-audivel", 1560650706114, "A-aula", H_, "Audição humana: 20–20.000 Hz", 31, "lâmina 31 e transcrição (ultrassom acima de 20 mil Hz)", origin="MCAT",
    extra_add="- Ultrasound is sound above 20,000 Hz; medical probes use millions of hertz (MHz)"),
 ak("mc-velocidade", 1558886211382, "R-detalhe", H_, "Velocidade do som: sólido > líquido > gás", 31, "bibliografia aula 2 (340, 1200, 5000 m/s)", origin="MCAT",
    text="Arrange the following three media based on the speed at which <b>sound</b> propagates through them: gas, liquid, solid.<br>Fastest: {{c1::solid::s…}}<br>Middle: {{c1::liquid::l…}}<br>Slowest: {{c1::gas::g…}}",
    extra_add="- Scanners assume 1540 m/s in soft tissue and turn echo return time into depth"),
 sh(1792141768308, "verde", H_, "Transdutor piezoelétrico", 32, "lâmina 32; provas 2024/2023/2019/2018 (mecanismo do US); card da 02"),
 ak("ext-gel", 1701804937884, "A-aula", H_, "Gel elimina o ar", 32, "transcrição (gel melhora a condução, elimina o ar)", origin="Ankisthesia"),
 ak("ext-impedancia", 1712509799325, "A-aula", H_, "Impedância acústica", 33, "lâmina 33 (pulso-eco); bibliografia (reflexão pela diferença de impedância)", origin="Ankisthesia",
    extra="- Reflection at an interface grows with the impedance difference between the two tissues<br>- Later echoes are drawn deeper on the screen"),
 ak("ext-frequencia", 1701743548002, "V-pilar", H_, "Frequência × resolução × penetração", 34, "lâmina 34 e transcrição (frequência alta: melhor imagem, menos profundidade)", origin="Ankisthesia",
    extra="- High-frequency linear probes: thyroid, breast; low-frequency convex probes: abdomen, pelvis"),
 ak("ext-atenuacao-us", 1701775518633, "A-aula", H_, "Atenuação cresce com a frequência", 34, "bibliografia aula 2 (atenuação ∝ frequência)", origin="Ankisthesia",
    extra="- Bone and air attenuate about 1,000 times more than water<br>- That is why deep organs need low-frequency probes"),
 # ---------- I. Orientação e ecogenicidade (lâminas 35–37) ----------
 ak("ext-marcador", 1701805150138, "R-detalhe", I_, "Marcador do transdutor", 35, "lâminas 35–36 (orientação transversal e longitudinal)", origin="Ankisthesia",
    text="By convention, ultrasound <b>transducer markers</b> are placed {{c1::anterior::a…}}, {{c1::cephalad::c…}}, or {{c1::lateral::l…}}",
    extra="- Top of the screen = nearest the probe (anterior)<br>- Transverse scan gives an axial image; longitudinal scan gives a sagittal image"),
 ak("ak-cisto-renal", 1475287477002, "A-step", I_, "Cisto simples é anecoico", 37, "lâmina 37 (anecogênica = líquido); prova 2016 P1 4.2"),
 # ---------- J. Artefatos (lâminas 38–39) ----------
 sh(1792141766310, "azul", J_, "US para cálculo biliar", 38, "lâmina 38 (cálculo na vesícula); card da 02"),
 au("au-sombra", "A <b>gallstone</b> reflects nearly all the beam, leaving a dark posterior acoustic {{c1::shadow}} behind it",
    "V-prova", J_, "Sombra acústica posterior", 38, "lâmina 38; provas 2023 P1 1.2, 2015 P1 2.1, 2015 sub (mecanismo da sombra)",
    extra="- Kidney stones, calcifications and bone also cast it; bowel gas casts a weaker, “dirty” shadow<br>" + IMG("sombra", 380)),
 au("au-reforco", "Because fluid attenuates sound little, tissue behind a <b>cyst</b> looks brighter, called posterior acoustic {{c1::enhancement}}",
    "V-prova", J_, "Reforço acústico posterior", 39, "lâmina 39; prova 2016 P1 4.2 (cisto anecoico com reforço); prova 2016 P2 2.7",
    extra="- Seen behind the bladder, gallbladder, vessels and cysts<br>" + IMG("reforco", 380)),
 # ---------- K. FAST (lâmina 40) ----------
 ak("ak-fast-hemorragia", 1530471987357, "A-step", K_, "FAST: hemorragia intraperitoneal no trauma instável", 40, "lâmina 40 e transcrição (FAST pesquisa sangramento)",
    extra_add="- Free blood is anechoic (black) between liver and kidney"),
 ak("ak-fast-trauma", 1532785810173, "A-step", K_, "FAST no trauma contuso ou penetrante", 40, "lâmina 40"),
 ak("ak-fast-retro", 1536157834210, "R-detalhe", K_, "FAST não vê o retroperitônio", 40, "limite do FAST (extra AnKing)"),
]

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (tubo, densidades, magnificação, PA×AP, silhueta, sombra, reforço, FAST) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula, sem equivalente nos acervos (busca sem acerto para o conceito)"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "rd04-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {  # chave: "- linha curta" para nota de acervo sem Extra útil
 "ak-radon": "",
 "mc-audivel": "",
 "ext-gel": "- Air reflects almost all the sound, so any air gap blanks the image",
 "ak-fast-trauma": "- It looks for free fluid around the heart, liver, spleen and bladder",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"au-atenuacao": "ganho: o mecanismo (atenuação → brilho); a tabela da 02 (sh-1792141774955) cobra só o nome dos termos"}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "rd04-tubo.png": "Lâmina 6: esquema do tubo (filamento de tungstênio aquecido, elétrons, alvo de tungstênio, ânodo de cobre, envelope a vácuo); verso de au-tubo.",
 "rd04-densidades.png": "Lâmina 11: radiografia de um ovo com ar, água, gordura e cálcio rotulados; verso de au-densidades (o verso pode mostrar a resposta).",
 "rd04-magnificacao.png": "Lâmina 22: esquema da aula com fonte puntiforme, objeto perto e longe do anteparo e sombras de tamanhos diferentes; verso de au-magnificacao.",
 "rd04-pa-ap.png": "Lâmina 23: RX de tórax PA e AP lado a lado (coração maior no AP); verso de au-pa-ap.",
 "rd04-silhueta.png": "Lâmina 26: dois RX de tórax com setas na borda cardíaca apagada e preservada; verso de au-silhueta.",
 "rd04-sombra.png": "Lâmina 38: US de vesícula com cálculo hiperecogênico e sombra acústica posterior; verso de au-sombra.",
 "rd04-reforco.png": "Lâmina 39: US de cisto anecoico com faixa clara atrás (seta amarela); verso de au-reforco.",
 "b8850be99c8b9b2d49fcf10380fa79c9.png": "MCAT/AnKing: ilustração da ambulância (frequência maior quando se aproxima); ensina o Doppler; verso dos dois cards do Doppler.",
 "aw.png": "Ankisthesia: escala de cor do Doppler (vermelho em direção, azul se afastando, matiz pela velocidade); verso de ext-doppler-cor (a captura de texto sobre Doppler esofágico foi retirada).",
 "paste-0fcf1af07da2c6ca1b0d07839e9e40af572b95e7.jpg": "Ankisthesia: US com perda de sinal por ar entre transdutor e pele (acoustic dropout); verso de ext-gel.",
}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (39 notas novas, 42 cards; frentes, clozes, versos, imagens e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Entender como se formam a radiografia (tubo, atenuação, densidades, projeção, magnificação, silhueta) e a ultrassonografia "
             "(onda mecânica, transdutor piezoelétrico, impedância, frequência, ecogenicidade, sombra e reforço), os efeitos da radiação ionizante e o FAST.",
 "centrais": [
   ("produção e efeito da radiação", "mc-espectro", "au-tubo", "ak-radicais", "au-estocastico"),
   ("formação da imagem no RX", "au-atenuacao", "au-densidades", "au-magnificacao", "au-pa-ap", "au-silhueta"),
   ("formação da imagem no US", "mc-vacuo", "ext-impedancia", "ext-frequencia", "ak-cisto-renal"),
   ("artefatos do US", "au-sombra", "au-reforco"),
 ],
 "exemplos": ["cálculos renais", "enfisema", "mieloma", "pneumonia do lobo médio", "colelitíase", "cisto renal", "trauma abdominal"],
 "outras_aulas": [("forças e limites, termos, contrastes, planos, piezoelétrico, Doppler, radioproteção", "02 Diagnóstico radiológico (sh)"),
                  ("Hounsfield, janelas, fases", "05 Tomografia computadorizada"), ("T1/T2", "12 Ressonância magnética"),
                  ("reações aos contrastes", "56 Contrastes radiológicos")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
