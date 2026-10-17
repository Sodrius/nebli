# Especificação curada — Tomografia computadorizada: princípios da TC (UC03 P1, Radiologia; Preceptoria 2024; 96 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing → associados da 02, da 04 e de outras aulas por sh() → autoral SÓ para lacuna provada em busca/cobertura.tsv (gate duro).
# Modelo vivo: arquivos-trabalho/deck-aula-uc03-rd04-radiografia-ultrassom-v2-2026-10-16/spec.py (16/10).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06: todo AnKing do conteúdo entra
    "_FirstAid_12_Neurology_03_Pathology_07_Intracranial_hemorrhage_Basics.txt",
]
AUTORAL_EXCECAO = ("Aula de física da TC: Hounsfield, janela/nível, fases do contraste, helicoidal, voxel e artefato de metal não têm nenhum "
                   "card em AnKing, MCAT, Ankisthesia ou NEBLI vivo (busca/anking.txt: 0 notas para janelas e fases; busca/semantica.jsonl)")
PIPELINE = "anking-primeiro"  # F-20261015-CLAUDE-06: liga os gates duros (cobertura_anking, cores_rubrica, inducao_clozes); não remover
RUN_ID = "uc03-rd05-20261016a"
SHORT = "rd05"
LESSON = "2026-uc03-radiologia-05-tomografia"
DECK = "NEBLI::UC03::P1::Radiologia::Tomografia computadorizada"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 16/10/2026"
_IMGS = ("resolucao", "reconstrucao", "helicoidal", "voxel", "hu", "janela", "janela-ampla", "fases", "metal", "stranding")
MEDIA = {f"rd05-{n}.png": f"img/rd05-{n}.png" for n in _IMGS}
IMG = lambda n, w=420: f'<img src="rd05-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (16/10): seções de recurso do AnKing (FirstAid hemorragia intracraniana, Bootcamp imagem axial, AMBOSS de TC; busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt: vidro fosco, Hounsfield, janelas, hiperdenso, fases, endurecimento do feixe); "
         "significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
# Cards da 04 (lateralidade e duas incidências), associados depois de a 04 estar instalada (16/10).
RD04_ORIENT, RD04_DUAS = 1792238916074, 1792238914748
EXCLUIDOS = [
 (1581465560589, "seção FirstAid hemorragia intracraniana: sintomas clínicos (cefaleia, rebaixamento) são da neurologia, não da imagem"),
 (1561067734495, "MCAT: definição genérica de TC; a 02 já tem o princípio (sh-1792141770757)"),
 (1705849921739, "isquemia hipodensa em 6–24 h: já existe a cópia NEBLI da GR2 (sh-1791054020270)"),
 (1481771891686, "isquemia visível na TC após 6–24 h: repete sh-1791054020270"),
 (1583523972057, "TC sem contraste como exame inicial no AVC: repete ak-tc-avc"),
 (1481772072075, "hematoma epidural em lente biconvexa: forma do hematoma é da neurologia; aqui basta o sangue agudo hiperdenso"),
 (1481771971776, "identificar HSA na imagem: diagnóstico neurológico, fora dos princípios"),
 (1550581908063, "sinal da ACM hiperdensa: sinal específico de neurorradiologia, não dado na aula"),
 (1494887543794, "fat stranding da colite isquêmica: outra doença; a aula usa a apendicite (au-stranding)"),
 (1555757418112, "TC com contraste na pancreatite duvidosa: indicação clínica, não princípio"),
 (1532541092056, "TC com contraste no carcinoma renal: indicação clínica"),
 (1581521840826, "vidro fosco na embolia gordurosa: doença específica; o vidro fosco entra pela contusão (ak-vidro-contusao)"),
 (1500337338985, "vidro fosco da pneumocistose no RX: doença específica de outra aula"),
 (1555536756446, "imagem da litíase em adulto × criança: repete ak-helicoidal-calculo"),
]
FORA_DO_RECORTE = [
 "Gerações de 1ª a 5ª, scout e álgebra da retroprojeção (lâminas 24, 27–28, 39–41): história e detalhe técnico, sem prova.",
 "Anatomia seccional do abdome (lâminas 72–84): aulas de anatomia e de correlação radiologia-patologia.",
 "Volume parcial, ruído, kV/mAs e dose em mSv (bibliografia): física acima do recorte.",
 "Reações ao contraste iodado em detalhe: aula 56 Contrastes radiológicos.",
 "Forma de cada hematoma (epidural × subdural × HSA): aulas de neurologia e correlação.",
]
A_, B_, C_, D_, E_, F_, G_, H_ = ("A-resolucao-lateralidade", "B-equipamento-contraste", "C-reconstrucao-aquisicao", "D-hounsfield",
                                  "E-janelas", "F-fases", "G-artefatos", "H-achados-indicacao")

CARDS = [
 # ---------- A. Lateralidade e resolução (lâminas 3–6) ----------
 au("au-resolucao", "<b>Contrast resolution</b> tells apart similar intensities, while {{c1::spatial}} resolution tells apart two adjacent small structures",
    "A-aula", A_, "Resolução espacial × de contraste", 4, "lâmina 4 (estrela do professor)",
    extra="- Spatial resolution rises with more pixels; contrast resolution improves with contrast media<br>"
          "- CT has excellent spatial and good contrast resolution (lâmina 89)<br>" + IMG("resolucao", 380)),
 sh(1792141768903, "azul", A_, "Contraste intrínseco × exógeno", 4, "lâmina 4 (contraste aumenta a resolução de contraste); card da 02"),
 sh(1792141766560, "azul", A_, "Métodos de imagem", 6, "lâmina 6 (lista dos métodos); card da 02"),
 # ---------- B. Equipamento e contraste (lâminas 9–15) ----------
 sh(1792141772255, "verde", B_, "Reconhecer a TC", 9, "provas pedem a modalidade (2024 P1, 2023 P1, 2017); card da 02"),
 sh(1792141770757, "verde", B_, "Princípio da TC: tubo que gira", 10, "lâminas 10–13, 23, 25, 38; provas 2024 P1, 2023 P1, 2017 P1 (princípio); card da 02"),
 sh(1792141769157, "azul", B_, "Contraste de cada método (iodo, bário)", 14, "lâminas 14–15, 59–60, 67; card da 02"),
 # ---------- C. Reconstrução e aquisição (lâminas 16–42) ----------
 au("au-reconstrucao", "CT acquires its data in the {{c1::axial}} plane, and the computer reconstructs sagittal, coronal and <b>3D</b> images from it",
    "V-prova", C_, "Aquisição axial, reconstrução multiplanar", 16, "lâminas 16–17 (estrelas); provas 2024 P1 e 2023 P1 (“reconstruídas nos diferentes planos”)",
    extra="- One acquisition: no new scan for each plane; also MIP (brightest voxels, for vessels) and MinIP (darkest, for airways)<br>"
          "- Thin slices make good reconstructions<br>" + IMG("reconstrucao", 460)),
 sh(1792141772506, "azul", C_, "Planos na TC", 17, "lâmina 17; card da 02"),
 au("au-helicoidal", "CT in which the table advances continuously while the tube keeps rotating, tracing a <b>spiral</b>, is called {{c1::helical}} CT",
    "A-aula", C_, "TC helicoidal (e multislice)", 30, "lâminas 26, 29–34 (estrela na 34); monitoria (cortes helicoidais, vários cortes por giro)",
    extra="- Slip rings let the tube spin without cables winding up<br>- Multislice: several detector rows acquire many slices per rotation (64 rows at HC)<br>"
          "- Result: faster exam and thinner slices, so better resolution<br>" + IMG("helicoidal", 360)),
 ak("ak-helicoidal-calculo", 1535195599425, "A-step", C_, "TC helicoidal sem contraste para cálculo renal", 30, "lâmina 30 (helicoidal); exemplo clínico do método",
    extra_add="- Stones are bright even without contrast; contrast would hide them in the collecting system"),
 au("au-voxel", "Each CT image element has depth, the <b>slice thickness</b>, so it is a 3D {{c1::voxel}} rather than a pixel",
    "A-aula", C_, "Voxel", 37, "lâminas 37 (estrela) e 42; transcrição (“não forma um pixel, forma um voxel”)",
    extra="- X and Y come from the matrix (512 × 512); Z is the slice thickness<br>- Each voxel gets one attenuation value (in HU)<br>" + IMG("voxel", 460)),
 # ---------- D. Hounsfield (lâminas 45–48) ----------
 au("au-hu", "<b>Hounsfield units</b> express CT attenuation relative to {{c1::water}}, which is set at 0 HU",
    "V-pilar", D_, "Escala Hounsfield", 47, "lâminas 45–48 (estrela na 46); apostila guia; monitoria",
    extra="- Air −1000 HU, fat negative (about −50 to −100), brain +20 to +40, fresh blood +65 to +95, bone up to +1000<br>"
          "- HU = 1000 × (μ tissue − μ water) / μ water<br>" + IMG("hu", 400)),
 ak("ak-sangue-agudo", 1525116681341, "V-prova", D_, "Sangue agudo é hiperatenuante na TC sem contraste", 48, "lâmina 48 (sangue 65–95 UH > encéfalo); prova 2018 P3 3.5; seção FirstAid",
    extra_add="- Clotted blood packs hemoglobin, so it attenuates more than brain"),
 ak("ak-avc-hemorragico", 1550944864586, "A-step", D_, "AVC hemorrágico: hiperdenso já na hora", 48, "par do anterior; transcrição (hematoma no idoso que bateu a cabeça)",
    extra_add="- Ischemic stroke takes 6–24 h to darken; hemorrhage is bright at once"),
 # ---------- E. Janelas (lâminas 49–56) ----------
 au("au-janela", "The CT window <b>level</b> is the {{c1::center}} HU value of the displayed gray scale",
    "V-pilar", E_, "Janela e nível", 50, "lâminas 49–51 (estrela na 50); monitoria (centro e largura)",
    extra="- Window width is the HU range shown; above it everything is white, below it black<br>"
          "- Example: level 50, width 200 → −50 (black) to 150 (white)<br>"
          "- Why: CT has ≥ 2000 HU values, but the eye tells apart only about 20 gray shades<br>" + IMG("janela", 380)),
 au("au-janela-ampla", "<b>Wide</b> CT windows suit {{c1::lung and bone}}, whereas narrow windows suit the {{c2::brain}} and soft tissue",
    "V-prova", E_, "Janela ampla × estreita", 55, "lâminas 52–55; prova 2024 P1 1.2 (janela óssea)",
    extra="- Wide: tissues with very different attenuation (air and lung, cortex and marrow)<br>"
          "- Narrow: similar tissues, such as ischemic versus normal brain<br>" + IMG("janela-ampla", 460)),
 sh(1791054020270, "verde", E_, "Isquemia: hipodensa em 6–24 h", 54, "lâmina 54 (AVC mais escuro); provas 2019 P1, 2018 P3 (lesão hipoatenuante isquêmica); card da GR2"),
 sh(1792141774955, "verde", E_, "Termos de cada método (hiper/hipoatenuante)", 56, "lâmina 56 (estrela); provas 2025, 2018, 2017 (descrever com o termo certo); card da 02"),
 # ---------- F. Fases do contraste (lâminas 58–67) ----------
 au("au-fases", "After <b>IV contrast</b>, the CT phase near 30 s is {{c1::arterial}}, and near 70 s, {{c2::portal}}",
    "A-aula", F_, "Fases do contraste", 58, "lâminas 58 (estrela), 61–66; monitoria (fases); prova 2023 P1 1.4 (aorta hiperatenuante pelo contraste)",
    extra="- Angiographic 15 s · arterial 30 s (hypervascular nodules, renal cortex) · portal 70 s (portal veins)<br>"
          "- Nephrographic 90 s · equilibrium 3 min · excretory 7 min (collecting system)<br>" + IMG("fases", 460)),
 sh(1791022169824, "rosa", F_, "Hemangioma na fase arterial", 63, "lâmina 63 (nódulo hipervascular na fase arterial); card da correlação 2"),
 # ---------- G. Artefatos (lâminas 68–70) ----------
 au("au-metal", "Dental fillings and other <b>metal</b> cause bright and dark streaks on CT, called {{c1::beam hardening}} artifact",
    "A-aula", G_, "Artefato de endurecimento do feixe", 68, "lâmina 68; transcrição; monitoria (metais dão efeito “strike”)",
    extra="- Metal absorbs the low-energy photons, so detectors behind it get almost no signal<br>"
          "- Motion artifact: the patient moves or breathes and structures blur or double<br>" + IMG("metal", 300)),
 # ---------- H. Achados e indicação (lâminas 86–93) ----------
 au("au-stranding", "Inflamed <b>fat</b> around the appendix becomes denser on CT, a sign called fat {{c1::stranding}}",
    "A-aula", H_, "Densificação da gordura na apendicite", 86, "lâmina 86; transcrição (gordura mais hiperatenuante pelo líquido inflamatório)",
    extra="- In Portuguese: densificação da gordura; exudate raises fat attenuation toward water<br>"
          "- With a thick-walled appendix: acute appendicitis<br>" + IMG("stranding", 320)),
 sh(1791022172025, "azul", H_, "Esteatose: fígado menos denso que o baço", 87, "lâmina 87 (fígado hipoatenuante, perto da gordura); card da correlação 2"),
 ak("ak-pneumotorax", 1570224895162, "A-step", H_, "Pneumotórax: linha pleural visceral", 88, "lâmina 88 (RX e TC do pneumotórax)",
    extra_add="- On CT lung window, pleural air is pure black, darker than lung, which still holds blood"),
 ak("ak-vidro-contusao", 1570492962412, "R-detalhe", H_, "Vidro fosco na contusão pulmonar", 88, "prova 2024 P3 1.4 (vidro fosco: atenuação intermediária); janela de pulmão",
    extra_add="- Ground glass: attenuation between normal lung and consolidation; vessels still visible through it"),
 sh(1792141770406, "azul", H_, "Forças e limites da TC", 89, "lâminas 89 (estrela) e 93; prova 2017 P2 (dose maior que o RX); card da 02"),
 ak("ak-contraste-nta", 1475353585796, "A-step", H_, "Contraste iodado e necrose tubular aguda", 89, "lâmina 89 (desvantagem: contraste); provas 2025 P3 4.5 e 2017 P3 2.2 (contraste e rim)",
    extra_add="- The lecture notes the risk is smaller than once believed; still check kidney function first"),
 ak("ak-contraste-hidratacao", 1532616085999, "R-detalhe", H_, "Prevenção da nefropatia por contraste: hidratação", 89, "par do anterior (cuidado com o contraste, prova 2017 P3)"),
 ak("ak-tc-avc", 1481771888224, "A-step", H_, "TC sem contraste antes do trombolítico", 90, "lâmina 90 e transcrição (achados que não esperam o radiologista)",
    extra_add="- Blood shows bright without contrast; contrast would also be bright and confuse it"),
 ak("ak-sdh-agudo", 1481772132777, "A-step", H_, "Hematoma subdural agudo: hiperdenso", 90, "transcrição (idoso que bateu a cabeça: hematoma, desvio da linha média)"),
 ak("ak-sdh-cronico", 1481772139865, "A-step", H_, "Hematoma subdural crônico: hipodenso", 90, "par do anterior: sangue velho perde densidade",
    extra_add="- Over weeks the clot breaks down and approaches CSF density"),
 ak("ak-sdh-agudizado", 1581465229917, "R-detalhe", H_, "Subdural agudizado: hiperdenso sobre hipodenso", 90, "par dos anteriores"),
 sh(1792141767159, "rosa", H_, "ACR Appropriateness Criteria", 91, "lâminas 91–92; card da 02"),
 sh(1792141771005, "azul", H_, "Radiação cumulativa e teratogênica", 93, "lâmina 93 (radiação ionizante; ponderar jovens); prova 2017 P2; card da 02"),
]
if RD04_ORIENT:
    CARDS.append(sh(RD04_ORIENT, "azul", A_, "Convenção de lateralidade", 3, "lâmina 3 (estrela); card da 04"))
if RD04_DUAS:
    CARDS.append(sh(RD04_DUAS, "azul", C_, "Duas incidências: uma vista não basta", 22, "lâminas 21–22 (“one view is no view”); card da 04"))

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (Hounsfield, janelas, fases, voxel, helicoidal, artefato, apendicite) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula, sem equivalente nos acervos (busca sem acerto para o conceito)"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "rd05-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {  # chave: "- linha curta" para nota de acervo sem Extra útil
 "ak-contraste-hidratacao": "- Hydration dilutes contrast in the tubules and speeds its excretion",
 "ak-sdh-agudo": "- Bridging veins tear between dura and arachnoid; fresh blood is bright",
 "ak-sdh-agudizado": "- A new bleed (bright) layers over old, darker blood",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"au-reconstrucao": "ganho: de onde vêm os planos (aquisição axial reconstruída); o card da 02 (sh-1792141772506) só nomeia os planos na imagem"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "rd05-resolucao.png": "Lâmina 4: mão em RX de referência e três versões (ruído, baixa resolução espacial, baixo contraste); verso de au-resolucao.",
 "rd05-reconstrucao.png": "Lâmina 17: TC em axial, sagital, coronal e reformatação 3D do crânio; verso de au-reconstrucao.",
 "rd05-helicoidal.png": "Lâmina 30: esquema de livro do caminho espiral do tubo com a mesa avançando (eixo z e tempo); verso de au-helicoidal.",
 "rd05-voxel.png": "Lâmina 37: esquemas de pixel 2D × voxel 3D com Δx, Δy, Δz sobre corte de abdome; verso de au-voxel.",
 "rd05-hu.png": "Lâmina 47: tubo, TC de abdome, detectores e barras ar −1000, água 0, osso +1000 UH; verso de au-hu.",
 "rd05-janela.png": "Lâmina 51: exemplo nível 50 / janela 200 com limites −50 e 150 e escala de cinza; verso de au-janela.",
 "rd05-janela-ampla.png": "Lâmina 52: mesmo corte de tórax em janela de partes moles, de pulmão e de osso; verso de au-janela-ampla (mostra a resposta, só no verso).",
 "rd05-fases.png": "Lâmina 66: mesmo corte de abdome sem contraste, arterial, portal, nefrográfica e equilíbrio; verso de au-fases.",
 "rd05-metal.png": "Lâmina 68: TC axial da face com raias claras e escuras saindo das restaurações dentárias; verso de au-metal.",
 "rd05-stranding.png": "Lâmina 86: TC da pelve com seta no apêndice espessado e gordura densificada; verso de au-stranding.",
}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (21 notas novas, 25 cards; frentes, clozes, versos, imagens e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Entender como a TC forma e mostra a imagem (tubo que gira, aquisição helicoidal/multislice, voxel, reconstrução, Hounsfield, "
             "janela e nível, fases do contraste, artefatos), descrever achados com hiper/hipoatenuante e reconhecer os achados que não esperam o radiologista.",
 "centrais": [
   ("formação da imagem", "sh-1792141770757", "au-reconstrucao", "au-helicoidal", "au-voxel"),
   ("quantificação e exibição", "au-hu", "au-janela", "au-janela-ampla", "sh-1792141774955"),
   ("contraste", "sh-1792141769157", "au-fases"),
   ("achados", "ak-sangue-agudo", "sh-1791054020270", "au-stranding", "sh-1791022172025"),
 ],
 "exemplos": ["AVC hemorrágico e isquêmico", "hematoma subdural", "apendicite", "esteatose", "pneumotórax", "nódulo hepático hipervascular"],
 "outras_aulas": [("princípio, forças e limites, planos, contrastes, termos, ACR", "02 Diagnóstico radiológico (sh)"),
                  ("lateralidade, duas incidências, atenuação", "04 Radiografia e ultrassom (sh)"),
                  ("T1/T2", "12 Ressonância magnética"), ("reações aos contrastes", "56 Contrastes radiológicos")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
