# Especificação curada — Diagnóstico radiológico: ferramentas do diagnóstico radiológico (UC03 P1, Radiologia; Profa. Claudia Leite; 61 lâminas).
# Pipeline AnKing-primeiro + F-20261016-CLAUDE-01 (cor pela rubrica, dica de 1ª letra, guarda-chuva × aulas específicas). Ordem = lâminas.
# A 02 fica com a identidade de cada método; física/janelas/fases/sequências ficam em 04, 05, 12 e 56. Aula antiga: entra suspensa. Sem Tab.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar

PIPELINE = "anking-primeiro"
RUN_ID = "uc03-rd02-20261016a"
SHORT = "rd02"
LESSON = "2026-uc03-radiologia-02-diagnostico-radiologico"
DECK = "NEBLI::UC03::P1::Radiologia::Diagnóstico radiológico"
CRITERIOS = "MEMORY.md §3/§5/§6/§8 (AnKing-primeiro, rubrica de cores, indução, fronteira da radiologia) + ANTI-EXEMPLARES, 16/10/2026"
MEDIA = {f"rd02-{n}.png": f"img/rd02-{n}.png" for n in ("us", "tc", "rm", "rx", "angio", "pet", "planos")}
IMG = lambda n, w=420: f'<img src="rd02-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (16/10): seções de recurso do AnKing (FirstAid radiação, B&B chest x-rays, Bootcamp imagem; busca/secoes); palavra-chave em "
         "AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos (busca/semantica.jsonl). ")
EXCLUIDOS = [
 (1555870659908, "MCAT: US “compara densidades” — formulação errada (o US depende de reflexão do eco/impedância)"),
 (1591177353117, "PET com glicose radioativa no cérebro: repete mc-pet"),
 (1534797012431, "AnatoKing “Radiography”: card só com o nome, sem imagem nem fato"),
 (1584310188149, "RM e implante coclear: clínica estreita; au-rm cobre o princípio (objetos ferromagnéticos)"),
 (1583460473557, "DSA na isquemia de membro: clínica estreita"),
 (1703734111719, "1/r²: fórmula de física da radioproteção acima do ciclo básico desta aula"),
 (1701743548002, "frequência × resolução do US: física da aula 04"),
]
FORA_DO_RECORTE = [
 "Física do RX (tubo, densidades), incidências PA/perfil, ecogenicidade, sombra/reforço acústico, Doppler em detalhe: aula 04 Radiografia e ultrassom.",
 "Hounsfield, janelas, fases do contraste, reconstruções 3D/MIP, artefatos da TC: aula 05 Tomografia computadorizada.",
 "T1/T2, fat sat, sequências e fases na RM: aula 12 Ressonância magnética.",
 "Reações e nefrotoxicidade dos contrastes: aula 56 Contrastes radiológicos.",
]
A_, B_, C_, D_, E_, F_, G_ = "A-por-que-e-escolha", "B-metodos-e-planos", "C-ultrassom", "D-tc", "E-rm", "F-rx", "G-angio-mn"

CARDS = [
 # ---------- A. Por que e como escolher (lâminas 2–11) ----------
 ak("ak-us-litiase", 1511234010517, "A-step", A_, "US para cálculo biliar", 3, "caso da lâmina 3 (cálculos ao US); HY clínico amplo"),
 au("au-metodos", ORG("<b>Main diagnostic imaging methods</b>:<br>1. {{c1::Radiography}} (X-ray)<br>2. {{c1::Computed tomography}}<br>3. {{c1::Ultrasound}}<br>"
                      "4. {{c2::Magnetic resonance}}<br>5. {{c2::Angiography}}<br>6. {{c2::Nuclear medicine}}"),
    "A-aula", B_, "Os seis métodos da aula", 7, "lista das lâminas 7–8; organizador do mapa da aula",
    extra="- Interventional radiology uses these images to guide treatment"),
 au("au-angio-intervencao", "<b>Digital angiography</b> images vessels through a catheter and can also treat them, as part of {{c1::interventional radiology}}",
    "A-aula", B_, "Radiologia intervencionista: diagnóstico e terapêutica", 8, "lâminas 8 e 54 (diagnóstico e terapêutica)",
    extra="- Uses X-rays and IV iodinated contrast; the catheter usually enters the femoral artery<br>- Examples: removing a clot in stroke, coils in an aneurysm; US-guided biopsy"),
 au("au-acr", "In the <b>ACR Appropriateness Criteria</b>, an imaging test rated {{c1::7–9}} is usually appropriate and one rated {{c2::1–3}} is usually not",
    "R-detalhe", A_, "Escala do ACR", 9, "escala da lâmina 9; ferramenta citada, pouco usada no dia a dia",
    extra="- 4–6: may be appropriate<br>- Start from the clinical hypothesis and choose the simplest, cheapest test that answers it"),
 # ---------- B. Planos (lâmina 13) ----------
 ak("ak-plano-sagital", 1534797985292, "A-aula", B_, "Plano sagital", 13, "planos da lâmina 13; prova 2024 (plano de reconstrução)"),
 ak("ak-plano-coronal", 1534799229555, "A-aula", B_, "Plano coronal", 13, "planos da lâmina 13"),
 ak("ak-plano-transverso", 1534800473819, "A-aula", B_, "Plano axial (transverso)", 13, "planos da lâmina 13"),
 # ---------- C. Ultrassom (lâminas 14–23) ----------
 ak("ak-piezo", 1701782440595, "A-aula", C_, "Transdutor piezoelétrico", 15, "o transdutor é “a peça-chave” (transcrição); prova 2018 (princípio do US)", origin="Ankisthesia",
    extra='Sound waves are absorbed/reflected by tissues → detected by transducer → converted into electric energy to form an image<br><img src="paste-f225be22a58710ab4f2b5a4e3318beb40419c5c1.jpg">'),
 au("au-us", ORG("<b>Ultrasound</b><br>Strengths: fast, dynamic, bedside, {{c1::no ionizing radiation}}, excellent for {{c1::fluids}}<br>"
                 "Limits: operator-dependent, poor through {{c2::gas}}, {{c2::fat}} and {{c2::bone}}"),
    "A-aula", C_, "Forças e limites do US", 16, "tabela das lâminas 14 e 16; prova 2025 P2 (vantagens do US) e 2018",
    extra="- Gas and bone block the sound; fat attenuates it, so obese patients are hard to scan"),
 au("au-contraste-tipos", "In imaging, <b>contrast</b> is either {{c1::intrinsic::intrinsic/exogenous}} (natural differences between tissues) or {{c1::exogenous::intrinsic/exogenous}} (an agent given to the patient)",
    "A-aula", C_, "Contraste intrínseco × exógeno", 17, "esquema repetido nas lâminas 17, 29 e 42",
    extra="- Intrinsic contrast: echoes (US), attenuation (CT), signal (MRI)"),
 au("au-contraste-agentes", ORG("<table><tr><th><b>Method</b></th><th><b>Exogenous contrast</b></th></tr>"
                                "<tr><td>CT</td><td>{{c1::iodinated}} (IV), also oral or rectal iodine or barium</td></tr>"
                                "<tr><td>MRI</td><td>{{c2::gadolinium}} (IV)</td></tr>"
                                "<tr><td>Ultrasound</td><td>{{c3::microbubbles}}</td></tr></table>"),
    "V-pilar", C_, "Contraste de cada método", 17, "lâminas 17, 29 e 42; prova 2024 P4 (contraste utilizado); apostila guia",
    extra="- Gadolinium is paramagnetic, so it changes the MRI signal"),
 au("au-img-us", "Which <b>imaging modality</b> produced this image? {{c1::Ultrasound}}<br>" + IMG("us"),
    "V-prova", C_, "Reconhecer US", 18, "provas 2025–2016 pedem a modalidade em quase toda questão",
    extra="- Fan-shaped grayscale image from a probe; fluid (gallbladder, vessels) is black (anechoic)"),
 ak("ak-doppler", 1610405450819, "A-aula", C_, "Efeito Doppler", 19, "Doppler mostra fluxo (lâmina 19, transcrição)", origin="Ankisthesia",
    extra="- In ultrasound, this frequency shift shows the direction and speed of blood flow (in color over the gray image)"),
 ak("ak-us-hiv", 1520636289409, "R-detalhe", C_, "US transfontanela: hemorragia intraventricular", 23, "exemplo da lâmina 23 (prematuro, fontanela como janela)",
    extra_add="- The open fontanelle lets sound through, so the newborn brain is scanned at the bedside"),
 # ---------- D. Tomografia (lâminas 24–37) ----------
 au("au-tc-principio", "<b>Computed tomography</b> builds cross-sectional images from {{c1::X-rays}} emitted by a tube that rotates around the patient",
    "V-pilar", D_, "Princípio da TC", 26, "princípio da lâmina 26; prova 2024 P1 (princípio de formação)",
    extra="- Detectors on the opposite side capture the X-rays; the computer turns the data into slices"),
 au("au-tc", ORG("<b>Computed tomography</b><br>Strengths: fast, high {{c1::spatial resolution}}<br>Limits: {{c2::ionizing radiation}} (higher dose than radiography), iodinated contrast, sedation in children"),
    "A-aula", D_, "Forças e limites da TC", 24, "tabela das lâminas 24 e 26; prova 2017 (dose maior que o RX)",
    extra="- Metal (bullets, dental work) creates artifacts around it"),
 au("au-radiacao-cuidados", "<b>Ionizing radiation</b> is {{c1::cumulative}} over a lifetime and {{c2::teratogenic}}, so its dose is minimized in children and avoided in pregnancy",
    "A-aula", D_, "Radiação: cumulativa e teratogênica", 26, "lâmina 26 e transcrição (crianças e grávidas); apostila guia (contraindicação na gravidez)",
    extra="- Every exam adds to the lifetime dose; radiation damages the DNA of dividing (fetal) cells"),
 ak("ak-radiacao-tireoide", 1462228665661, "A-step", D_, "Radiação na infância e carcinoma papilífero", 26, "HY 1: o porquê do cuidado com crianças"),
 au("au-radioprotecao", ORG("<b>Radiation protection</b> principles:<br>1. {{c1::Justification}}<br>2. {{c1::Optimization}} (as low as reasonably achievable)<br>3. {{c1::Dose limitation}}"),
    "A-aula", D_, "Princípios da radioproteção", 26, "prova 2017 P4 1.3 (rad-01); Mello cap. 1",
    extra="- In practice: less time, more distance, shielding"),
 ak("ext-alarp", 1608056287867, "R-detalhe", D_, "ALARA", 26, "prova 2017 P4 (otimização); Ankisthesia", origin="Ankisthesia"),
 au("au-img-tc", "Which <b>imaging modality</b> produced this image? {{c1::Computed tomography}}<br>" + IMG("tc"),
    "V-prova", D_, "Reconhecer TC", 30, "provas 2025–2016 pedem a modalidade",
    extra="- Cross-sectional slice; bone white, air black, organs in shades of gray"),
 au("au-img-planos", "Which <b>planes</b> are shown?<br>A {{c1::axial}} · B {{c2::sagittal}} · C {{c3::coronal}}<br>" + IMG("planos", 560),
    "A-aula", D_, "Reconhecer o plano", 31, "lâmina 31; prova 2024 P4 (plano de reconstrução)",
    extra="- CT acquires axial slices; the computer rebuilds the other planes"),
 # ---------- E. Ressonância (lâminas 38–45) ----------
 ak("mc-rm", 1561067971846, "V-pilar", E_, "Princípio da RM", 40, "princípio da lâmina 40", origin="MCAT"),
 au("au-rm", ORG("<b>MRI</b><br>Strengths: best {{c1::contrast resolution}} (soft tissues), no ionizing radiation<br>"
                 "Limits: slow, sedation for claustrophobic patients, {{c2::ferromagnetic}} objects pulled, {{c2::pacemakers}} can fail"),
    "A-aula", E_, "Forças e limites da RM", 40, "tabela das lâminas 38 e 40; prova 2018 P1 2.1 (cuidados na indicação)",
    extra="- Every patient is interviewed before entering the magnet room<br>- MR cholangiography shows the biliary tree"),
 au("au-img-rm", "Which <b>imaging modality</b> produced this image? {{c1::Magnetic resonance imaging}}<br>" + IMG("rm"),
    "V-prova", E_, "Reconhecer RM", 43, "provas 2025–2016 pedem a modalidade",
    extra="- Fluid very bright, bone cortex dark, excellent soft-tissue detail"),
 # ---------- F. Radiografia (lâminas 46–52) ----------
 au("au-rx", ORG("<b>Radiography</b><br>Strengths: fast, cheap, bedside, good for {{c1::bone}} and {{c1::gas}}<br>"
                 "Limits: {{c2::superimposition}} of structures (not sectional), low spatial and contrast resolution"),
    "A-aula", F_, "Forças e limites do RX", 48, "tabela das lâminas 46 e 48",
    extra="- Main uses: chest (pneumonia), fractures, abdomen (obstruction)"),
 ak("ak-obstrucao", 1579994989766, "R-detalhe", F_, "Nível hidroaéreo na obstrução", 50, "exemplo da lâmina 50 (decúbito × ortostase)"),
 ak("ak-pneumonia", 1495908532054, "A-step", F_, "RX de tórax na pneumonia", 51, "lâmina 51; prova 2017 (primeiro exame)"),
 au("au-img-rx", "Which <b>imaging modality</b> produced this image? {{c1::Radiography}}<br>" + IMG("rx"),
    "V-prova", F_, "Reconhecer RX", 51, "provas 2025–2016 pedem a modalidade",
    extra="- One projection with ribs, heart and spine superimposed; no slices"),
 au("au-termos", ORG("<table><tr><th><b>Method</b></th><th><b>Bright finding</b></th><th><b>Dark finding</b></th></tr>"
                     "<tr><td>Radiography</td><td>{{c1::radiopaque}}</td><td>{{c1::radiolucent}}</td></tr>"
                     "<tr><td>CT</td><td>{{c2::hyperattenuating}}</td><td>{{c2::hypoattenuating}}</td></tr>"
                     "<tr><td>Ultrasound</td><td>{{c3::hyperechoic}}</td><td>{{c3::hypoechoic / anechoic}}</td></tr>"
                     "<tr><td>MRI</td><td>{{c4::hyperintense}}</td><td>{{c4::hypointense}}</td></tr></table>"),
    "V-pilar", F_, "Termos de descrição de cada método", 52, "provas 2025–2016 (“use os termos radiológicos apropriados”); apostila guia (mecanismo por método)",
    extra="- Each term names what forms the image: attenuation of X-rays, reflected echoes or MRI signal"),
 au("au-ionizante", "The imaging methods that do <u>not</u> use <b>ionizing radiation</b> are {{c1::ultrasound}} and {{c1::MRI}}",
    "V-pilar", F_, "Métodos sem radiação ionizante", 52, "tabela da lâmina 52; prova 2025 P2 (vantagem do US)",
    extra="- Radiography, CT and angiography use X-rays; nuclear medicine uses a radioactive tracer"),
 # ---------- G. Angiografia e medicina nuclear (lâminas 53–61) ----------
 au("au-img-angio", "Which <b>imaging modality</b> produced this image? {{c1::Digital angiography}}<br>" + IMG("angio"),
    "A-aula", G_, "Reconhecer angiografia", 56, "lâmina 56",
    extra="- Contrast-filled aorta and branches; the background has been subtracted"),
 au("au-mn", "<b>Nuclear medicine</b> images organ {{c1::function}} with injected radiotracers, but its anatomic resolution is low, so it is fused with an anatomical method such as {{c2::CT}}",
    "A-aula", G_, "Medicina nuclear: função e fusão", 59, "lâminas 57–59; prova 2018 P4 (PET)",
    extra="- Two types: SPECT and PET"),
 ak("mc-pet", 1561068374240, "A-aula", G_, "PET e metabolismo da glicose", 59, "lâminas 59–61 (glicose marcada; tumores captam mais); prova 2018 P4", origin="MCAT"),
 au("au-img-pet", "Which <b>imaging modality</b> produced this image? {{c1::PET-CT}}<br>" + IMG("pet"),
    "R-detalhe", G_, "Reconhecer PET", 61, "lâmina 61",
    extra="- Colored hot spots of glucose uptake laid over CT anatomy"),
]

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "método ou princípio sem estrutura a reconhecer; as imagens que ensinam estão nos cards de reconhecer a modalidade e os planos"
SLIDE_SEM_ALT = "imagem da própria lâmina da aula, sem equivalente nos acervos (busca de cards de modalidade sem acerto)"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "rd02-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {
 "ak-us-litiase": "- Stones are bright with a dark acoustic shadow behind them",
 "ak-plano-sagital": "- Sagittal: divides right from left (side view)",
 "ak-plano-coronal": "- Coronal: divides front from back (frontal view)",
 "ak-plano-transverso": "- Axial (transverse): divides upper from lower; CT acquires in this plane",
 "ak-piezo": "- The same crystals receive the returning echoes and turn them back into electricity",
 "ak-radiacao-tireoide": "- One reason radiation doses are kept low in children",
 "ak-obstrucao": "- An upright film lets gas rise over fluid, forming the levels",
 "ak-pneumonia": "- Consolidated lung is opaque against the air-filled lung around it",
 "mc-rm": "- Hydrogen protons in water and fat produce the signal",
 "mc-pet": "- Tumor cells take up more labeled glucose, so they light up",
 "ext-alarp": "- Achieved by less time, more distance and shielding",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {
 "au-metodos": "ganho: o mapa dos seis métodos; os cards de cada método tratam forças, limites e reconhecimento",
 "au-us": "ganho: forças e limites do US; au-ionizante e au-img-us cobram outra coisa (radiação; reconhecer a imagem)",
 "au-img-us": "ganho: reconhecer a modalidade numa imagem (alvo de prova), não fato sobre o método",
 "au-tc": "ganho: forças e limites da TC; au-tc-principio cobra o princípio",
 "au-img-tc": "ganho: reconhecer a modalidade numa imagem",
 "au-img-planos": "ganho: reconhecer o plano numa TC; os AnatoKing definem os planos no desenho",
 "au-img-rm": "ganho: reconhecer a modalidade numa imagem; mc-rm e au-rm cobram princípio e limites",
 "au-ionizante": "ganho: quais métodos não usam radiação; au-us e au-rm citam a ausência só como força de cada um",
 "au-mn": "ganho: medicina nuclear como exame funcional que se funde à anatomia; mc-pet cobra a glicose",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "paste-f225be22a58710ab4f2b5a4e3318beb40419c5c1.jpg": "Ankisthesia: transdutor emitindo ondas com texto do eco; ensina o princípio; verso de ak-piezo (a figura de transdutores phased array foi retirada).",
 "be36c6149265b8edd418fd3efd825430.jpg": "MCAT: TC, PET e fusão PET-CT coronais lado a lado; mostra por que se funde; verso de mc-pet.",
 "rd02-us.png": "Lâmina 19: US de vesícula e veia porta (rótulo “VEIA PORTA”; título cortado); frente do card de modalidade.",
 "rd02-tc.png": "Lâmina 30: TC de abdome sem contraste, corte axial; título cortado; frente.",
 "rd02-rm.png": "Lâmina 43: RM de abdome superior T2; legenda e logotipo cortados; frente.",
 "rd02-rx.png": "Lâmina 51: RX de tórax PA com círculo na pneumonia; legenda cortada; frente.",
 "rd02-angio.png": "Lâmina 56: angiografia digital da aorta e ramos; título cortado; frente.",
 "rd02-pet.png": "Lâmina 61: PET-CT coronal, axial e MIP com focos de captação; frente.",
 "rd02-planos.png": "Lâmina 31: TC com contraste em axial, sagital e coronal; legendas cortadas (A/B/C no texto); frente.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Conhecer os principais métodos de imagem (RX, TC, US, RM, angiografia, medicina nuclear): o princípio físico, se usa radiação ionizante, o termo de descrição, forças e limites, o contraste típico, os cuidados e como escolher o exame; reconhecer a modalidade numa imagem.",
 "centrais": [
   ("métodos e escolha", "ak-us-litiase", "au-metodos", "au-angio-intervencao", "au-acr"),
   ("radiação e segurança", "au-radiacao-cuidados", "au-radioprotecao", "au-rm", "au-ionizante"),
   ("princípio de cada método", "ak-piezo", "au-tc-principio", "mc-rm", "au-mn", "mc-pet"),
   ("forças, limites e contraste", "au-us", "au-tc", "au-rx", "au-contraste-tipos", "au-contraste-agentes", "au-termos"),
   ("reconhecer a modalidade", "au-img-us", "au-img-tc", "au-img-rm", "au-img-rx", "au-img-angio", "au-img-pet", "au-img-planos"),
 ],
 "exemplos": ["colelitíase", "obstrução intestinal", "pneumonia", "hemorragia em prematuro", "aneurisma de aorta"],
 "outras_aulas": [("física do RX e do US, incidências, ecogenicidade", "04 Radiografia e ultrassom"), ("Hounsfield, janelas, fases, reconstruções", "05 Tomografia computadorizada"),
                  ("T1/T2 e sequências", "12 Ressonância magnética"), ("reações aos contrastes", "56 Contrastes radiológicos")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
