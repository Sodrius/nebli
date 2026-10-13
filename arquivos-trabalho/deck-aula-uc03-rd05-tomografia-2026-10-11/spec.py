# Especificação curada — Tomografia computadorizada (UC03 P1, Radiologia; Preceptoria 2024, Dr. João Vitor Vieira; 96 lâminas).
# Ordem = lâminas de fontes/slides.pdf (versão 2024 = pptx da pasta pessoal); a transcrição é da versão 2023 (mesma aula, lâminas quase idênticas).
# Aula 02 (Diagnóstico radiológico) já cobre o conceito de TC, janelas, fases, hiper/hipodenso, artefatos e radiação: aqui entram por sh(); esta aula
# acrescenta a física (aquisição, voxel, reconstrução), Hounsfield, janelas em detalhe e as fases com seus tempos. Complicações de contraste = aula 56.
RUN_ID = "uc03-rd05-20261012a"
SHORT = "rd05"
LESSON = "2026-uc03-radiologia-05-tomografia"
DECK = "NEBLI::UC03::P1::Radiologia::Tomografia computadorizada"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261012-CLAUDE-01) + plano vigente, 12/10/2026"
MEDIA = {f"rd05-{n}.png": f"img/rd05-{n}.png" for n in (
    "janela-partes-moles", "janela-pulmao", "janela-osso", "fase-sem", "fase-arterial", "fase-portal", "fase-tardia",
    "plano-axial", "plano-sagital", "plano-coronal", "recon-3d", "artefato-metal", "artefato-movimento", "scout", "hu-escala")}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 30 consultas sobre Hounsfield, janelas, fases, helicoidal/multislice, voxel, "
         "MIP, artefatos, scout, bário, resolução; busca/ext.txt, 8 consultas), cópias NEBLI vivas da aula 02 conferidas (compartilhados), 12/10: ")
FALTA = "AnKing e externos não têm card de física/janelas/fases da TC (só clínica de AVC, litíase e bário em outros exames)."
EXCLUIDOS = [
 (1550944864586, "AVC hemorrágico como hiperdenso: caso de doença; a aula usa o sangue só como ponto da escala de Hounsfield (card autoral)"),
 (1550581908063, "sinal da ACM hiperdensa: neurologia, fora da aula"),
 (1535195599425, "TC helicoidal sem contraste para litíase renal: clínica de nefrologia"),
 (1535922156637, "hemorragia subaracnoide: clínica de neurologia"),
 (1481771888224, "TC sem contraste antes do tPA: manejo do AVC, fora do recorte"),
 (1482203812587, "sinal do bico de pássaro na acalasia (bário): radiografia contrastada, aula de contrastes"),
]
FORA_DO_RECORTE = [
 "Exemplos de achados (apendicite, esteatose, pneumotórax, AVC na janela estreita): ilustram a escala de Hounsfield e as janelas; a doença pertence às correlações radiológicas.",
 "Anatomia da TC de abdome (lâminas 71–84, sem rótulos): anatomia do abdome é de UC08; a aula só passa 'rapidão'.",
 "Gestalt, Aunt Minnie e lateralidade (versão 2023, lâminas 4–8): o professor disse que 'não vai cair na prova'.",
 "Gerações 2ª–5ª da TC (feixe de elétrons da 5ª): pergunta ao Davi.",
]
B = "BUSCA"


def ak(key, src, cor, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags={1: cor}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, cor, bloco, alvo, slide, autoria, espelhos, motivo, extra=""):
    import re
    n = sorted({int(x) for x in re.findall(r"\{\{c(\d+)::", text)})
    return dict(key=key, kind="autoral", text=text, extra=extra, flags={i: cor for i in n}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + FALTA, espelhos=espelhos, motivo=motivo, duplicacao_ok="")


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


EP_CT = [1550944864586, 1561067734495, 1481771894987]
EP_TERM = [1475287477002, 1550944864586, 1578744787353]
EP_PHYS = [1701782440595, 1701779007226, 1561067971846]
EP_CTR = [1532616085999, 1584310188149, 1561067971846]
EP_IMG = [1511234010517, 1530303581189, 1495151598103]
EP_SAFE = [1584310188149, 1532616085999, 1462228665661]

A_ = "A-resolucao-e-metodo"
B_ = "B-equipamento"
C_ = "C-aquisicao-e-evolucao"
D_ = "D-reconstrucao"
E_ = "E-hounsfield"
F_ = "F-janelas"
G_ = "G-tecnicas-e-fases"
H_ = "H-artefatos"
I_ = "I-balanco"

# nids vivos da aula 02 (conferidos em 12/10/2026 após a revisão Codex)
S_TCDEF, S_NAOHIER, S_HIST = 1791810567122, 1791810569096, 1791810565746
S_RXSEC, S_RECON, S_RAPIDO, S_RADIACAO = 1791810569222, 1791810576172, 1791810573868, 1791810574120
S_FASEC, S_FASEF, S_ENH = 1791810576422, 1791810576547, 1791810576298
S_VO, S_JOSSEA, S_HIPER, S_HIPO, S_ISO = 1791810577296, 1791810577972, 1791810578222, 1791810578347, 1791810578471
S_ARTDEF, S_ARTMET, S_ARTMOV = 1791810579220, 1791810579347, 1791810579472
S_ACR, S_ACRN, S_JANELA = 1791810568546, 1791810568671, 1791810575497
S_CIV = 1791810574747

CARDS = [
 # ---------- A. Resolução e papel da TC entre os métodos (lâminas 3–8) ----------
 au("lateralidade", "On a chest radiograph or CT, the patient's {{c1::right}} side appears on the <b>left</b> of the viewer", R, A_, "Convenção de lateralidade", 3, "lateral",
    EP_IMG, "Rosa: lâmina marcada, convenção geral do radiologista.", extra="- The viewer looks at the patient as if facing them"),
 au("res-espacial", "<b>Spatial resolution</b> is the ability to separate adjacent structures, and it improves with more {{c1::pixels}}", V, A_,
    "Resolução espacial", 4, "prova", EP_PHYS, "Verde: conceito marcado, repetido nas mensagens finais e na prova ('boa resolução espacial').",
    extra="- Fewer pixels blur small adjacent structures into one"),
 au("res-contraste", "<b>Contrast resolution</b> is the ability to distinguish small differences in {{c1::intensity}} between structures", V, A_,
    "Resolução de contraste", 4, "prova", EP_PHYS, "Verde: conceito marcado, par da resolução espacial.",
    extra="- It can be raised by giving contrast media"),
 au("angio-tc", "<b>CT angiography</b> is a CT with intravenous contrast acquired in the {{c1::arterial}} phase", Z, A_, "Angiotomografia", 6, "prova",
    EP_CTR, "Azul: modalidade pedida em P4 2025 (angio-TC de tórax).", extra="- It is listed among the CT techniques with contrast"),
 sh(S_NAOHIER, "azul", A_, "Associação: métodos não são hierárquicos", 7, "Azul: lâmina 7 (riscada) e mensagem final 'se complementam'."),
 sh(S_HIST, "azul", A_, "Associação: pedido com hipótese", 8, "Azul: objetivo da aula é o melhor cuidado e o pedido adequado."),
 sh(S_TCDEF, "verde", B_, "Associação: definição de TC", 9, "Verde: define o método da aula."),

 # ---------- B. Equipamento (lâminas 10–15) ----------
 au("gantry", "The ring of a CT scanner that houses the X-ray tube and detectors is the {{c1::gantry}}", Z, B_, "Gantry", 10, "central", EP_IMG,
    "Azul: componentes rotulados na lâmina 10.", extra="- The table slides the patient through it, and a separate console runs the exam"),
 au("injetora", "A power <b>injector pump</b> delivers {{c1::intravenous}} contrast during the CT", R, B_, "Bomba injetora", 11, "lateral", EP_CTR,
    "Rosa: componente rotulado na lâmina 10 e 11.", extra="- It controls the injection rate so the phases are timed"),
 au("bario-tc", "Besides iodinated contrast, CT can use oral or rectal {{c1::barium}}", R, B_, "Contraste baritado", 15, "lateral", EP_CTR,
    "Rosa: lâminas 15 e 60; uso específico fica para a aula de contrastes.", extra="- Dense barium can cause artifacts on CT"),

 # ---------- C. Aquisição e evolução (lâminas 16–41) ----------
 au("tubo-detectores", "In CT the X-ray tube rotates around the patient while {{c1::detectors}} on the opposite side record the beam", V, C_,
    "Tubo e detectores opostos", 12, "prova", EP_CT, "Verde: mecanismo de formação da imagem pedido em P1 2023, P1 2017 e P1 2024.",
    extra="- The attenuated beam is measured from many angles"),
 au("detector-sinal", "CT detectors turn the photons that reach them into an electrical signal that the computer {{c1::digitizes}}", R, C_,
    "Detector gera sinal analógico e digital", 12, "lateral", EP_PHYS, "Rosa: detalhe do texto da aula (bibliografia).",
    extra="- More photons arriving means a higher voltage"),
 sh(S_RECON, "verde", D_, "Associação: reconstrução em qualquer plano e 3D", 16, "Verde: núcleo da reconstrução."),
 au("axial-nativo", "The only plane CT acquires directly is the {{c1::axial}}, and the others are reconstructed from it", V, D_,
    "Plano axial é o adquirido", 16, "central", EP_CT, "Verde: ideia central para entender reformatação.", extra="- Thin slices make good sagittal and coronal views possible"),
 au("img-axial", '<img src="rd05-plano-axial.png"><br>This <b>CT</b> image is in the {{c1::axial}} plane', Z, D_, "Reconhecer plano axial", 17, "prova", EP_IMG,
    "Azul: lâmina 17 marcada; prova pede o plano de reconstrução.", extra="- It is the plane in which the scanner acquires the data"),
 au("img-sagital", '<img src="rd05-plano-sagital.png"><br>This <b>CT</b> reconstruction is in the {{c1::sagittal}} plane', Z, D_, "Reconhecer plano sagital", 17, "prova",
    EP_IMG, "Azul: prova P4 2024 pede 'plano de reconstrução'.", extra="- The spine is seen in profile"),
 au("img-coronal", '<img src="rd05-plano-coronal.png"><br>This <b>CT</b> reconstruction is in the {{c1::coronal}} plane', Z, D_, "Reconhecer plano coronal", 17, "prova",
    EP_IMG, "Azul: prova P4 2024 pede 'plano de reconstrução'.", extra="- The body is seen from the front"),
 au("img-3d", '<img src="rd05-recon-3d.png"><br>This <b>CT</b> image of the skull is a {{c1::3D}} reformatting', Z, D_, "Reconhecer reformatação 3D", 17, "central",
    EP_IMG, "Azul: quarta reconstrução da lâmina 17.", extra="- Bone and vessels are good targets for 3D rendering"),
 sh(S_RXSEC, "azul", D_, "Associação: radiografia não é seccional", 18, "Azul: lâmina 18 compara anatomia, radiografia e TC."),
 au("projecoes", "Projections taken from several angles let CT separate structures that {{c1::overlap}} on a single projection", V, C_,
    "Várias projeções separam estruturas sobrepostas", 23, "central", EP_CT, "Verde: diferença entre radiografia e TC explicada na lâmina 23 (marcada).",
    extra="- A single beam stacks the sphere, cube and triangle on the film"),
 au("scout", '<img src="rd05-scout.png"><br>This low-dose planning radiograph taken before the scan is the {{c1::scout}}', Z, C_, "Radiografia localizadora", 24, "central",
    EP_IMG, "Azul: lâmina 24 e fala sobre o técnico planejar o corte.", extra="- It defines the region the slices will cover"),
 au("leque", "Radiography uses a pyramidal X-ray beam, while CT uses a {{c1::fan}}-shaped beam", R, C_, "Feixe em leque", 25, "lateral", EP_PHYS,
    "Rosa: detalhe da bibliografia da aula.", extra="- The beam leaves the tube through a narrow slit"),
 au("colimador", "The <b>collimator</b> narrows the X-ray beam and defines the {{c1::slice}} thickness", Z, C_, "Colimador", 26, "central", EP_PHYS,
    "Azul: lâmina 26 marcada, esquema rotulado (tubo, colimador, detectores, computador).", extra="- It is placed between the tube and the patient"),
 au("primeira-geracao", "In the first CT scanners one detector moved with the tube and the table advanced between rotations, making the exam {{c1::slow}}", R, C_,
    "Primeiras gerações da TC", 27, "lateral", EP_CT, "Rosa: história da evolução (lâminas 27–31 e transcrição).", extra="- Later generations added rows of detectors"),
 au("terceira-geracao", "In the most widely used {{c1::third}}-generation scanners, the tube and a detector row rotate together around the patient", R, C_, "3ª geração", 27, "lateral",
    EP_CT, "Rosa: gerações de lâmina 27 e livro (ESR), só a geração em uso.", extra="- The detector row spans the whole fan-shaped beam"),
 au("slip-rings", "<b>Slip rings</b> let the tube rotate continuously without twisting cables, which made {{c1::helical}} CT possible", Z, C_, "Slip rings",
    29, "central", EP_CT, "Azul: avanço de engenharia citado na transcrição (trilho de condução).", extra="- Power and data pass through sliding contacts"),
 au("helicoidal", "In <b>helical</b> CT the tube rotates while the table moves, so the exam is {{c1::continuous}}", V, C_, "TC helicoidal", 34, "central", EP_CT,
    "Verde: lâmina 34 marcada.", extra="- The beam traces a helix around the patient"),
 au("multislice", "<b>Multislice</b> CT acquires several slices in a single {{c1::rotation}} of the tube", V, C_, "TC multislice", 34, "central", EP_CT,
    "Verde: lâmina 34 marcada.", extra="- Modern hospital scanners have 64 rows of detectors"),
 au("single-multi", "Single-slice scanners have one row of detectors, while multislice scanners have {{c1::several rows}}", Z, C_, "Single slice × multislice", 33, "central", EP_CT,
    "Azul: lâmina 33.", extra="- More rows cover more of the body per rotation"),
 au("helicoidal-apneia", "Helical CT scans the whole region in one breath, which avoids {{c1::respiratory}} misregistration", R, C_, "Helicoidal em uma apneia", 34, "lateral", EP_CT,
    "Rosa: vantagem do livro (ESR), sem aprofundar parâmetros.", extra="- Axial scanning stops, acquires one slice and moves the table"),
 au("multislice-ganho", "Helical multislice CT gives more resolution and {{c1::less}} exam time", Z, C_, "Vantagem do helicoidal multislice", 34, "central", EP_CT,
    "Azul: caixa da lâmina 34.", extra="- It is one pass of the patient through the gantry"),

 # ---------- D. Dados brutos, voxel e reconstrução (lâminas 35–42) ----------
 au("voxel", "A <b>voxel</b> is a pixel with depth, whose third dimension is the {{c1::slice}} thickness", V, D_, "Voxel", 37, "central", EP_PHYS,
    "Verde: lâmina 37 marcada.", extra="- Pixel is 2D and voxel is 3D"),
 au("matriz", "The x and y axes of a CT image are defined by the computer {{c1::matrix}}, usually 512 by 512", Z, D_, "Matriz 512 × 512", 37, "central", EP_PHYS,
    "Azul: lâmina 37 marcada.", extra="- The z axis is the slice thickness"),
 au("pixels-260k", "A 512 by 512 matrix holds about {{c1::260,000}} pixels", R, D_, "260.000 pixels", 37, "lateral", EP_PHYS,
    "Rosa: número da lâmina 37.", extra="- More pixels give better spatial resolution"),
 au("fov", "For the same matrix, a smaller <b>field of view</b> makes each pixel cover a {{c1::smaller}} area", R, D_, "Campo de visão", 37, "lateral", EP_PHYS,
    "Rosa: detalhe da bibliografia da aula.", extra="- The inner ear needs a small field of view and the abdomen a large one"),
 au("espessura-corte", "Thinner CT slices improve spatial resolution along the long axis but increase image {{c1::noise}}", R, D_, "Espessura de corte", 37, "lateral", EP_PHYS,
    "Rosa: z do voxel; livro (ESR).", extra="- Thin slices help in lung parenchyma, and thick slices in angiography"),
 au("retroprojecao", "Raw CT data are converted into an image by a mathematical method called {{c1::back projection}}", R, D_, "Retroprojeção", 38, "lateral", EP_PHYS,
    "Rosa: lâminas 38–40 (método) e bibliografia.", extra="- Fourier-based methods are also used"),
 au("mais-projecoes", "The more projections are used, the {{c1::sharper}} the reconstructed image", Z, D_, "Mais projeções, imagem mais nítida", 40, "central", EP_PHYS,
    "Azul: lâmina 40 mostra o ponto com 2 a 32 projeções.", extra="- With few projections a point becomes a star-shaped blur"),
 au("mip", "A <b>MIP</b> reconstruction displays only the {{c1::highest}} attenuation along each ray, highlighting contrast-filled vessels", R, D_, "MIP", 16, "lateral",
    EP_PHYS, "Rosa: o slide lista MIP sem definir; definição do método.", extra="- It is the maximum intensity projection"),
 au("minip", "A <b>MinIP</b> reconstruction displays only the {{c1::lowest}} attenuation along each ray, highlighting air-filled structures", R, D_, "MinIP", 16, "lateral",
    EP_PHYS, "Rosa: o slide lista MinIP sem definir; definição do método.", extra="- It is the minimum intensity projection"),

 # ---------- E. Unidades Hounsfield (lâminas 43–48) ----------
 au("hu-def", "<b>Hounsfield units</b> express the attenuation of a tissue relative to {{c1::water}}", V, E_, "Unidade Hounsfield", 45, "prova", EP_TERM,
    "Verde: conceito central, pedido em prova ('valores de HU').",
    extra="- HU = 1000 × (μ tissue − μ water) / μ water<br>- Air is the darkest and bone the brightest tissue on the scale<br><img src=\"rd05-hu-escala.png\">"),
 au("hu-branco", "The more X-rays a tissue attenuates, the fewer photons reach the detectors and the {{c1::whiter}} it looks", V, E_, "Mais atenuação, mais branco", 47, "central",
    EP_TERM, "Verde: lâmina 47 (tubo, detectores, ar, água, osso).", extra="- Air looks black, water gray and bone white"),
 au("hu-ar", "Air has the lowest attenuation on CT, about {{c1::−1000}} HU", V, E_, "Ar −1000 UH", 46, "prova", EP_TERM, "Verde: ponto fixo da escala (lâminas 33/46/48).",
    extra="- Lung parenchyma lies between air and water"),
 au("hu-agua", "Water is the reference of the scale and measures {{c1::0}} HU", V, E_, "Água 0 UH", 46, "prova", EP_TERM, "Verde: ponto fixo da escala.",
    extra="- Cerebrospinal fluid also measures about 0 HU"),
 au("hu-gordura", "Fat is less attenuating than water, about {{c1::−50 to −100}} HU", Z, E_, "Gordura negativa", 46, "prova", EP_TERM,
    "Azul: escala da lâmina 46 e prova ('processo inflamatório na gordura').", extra="- A fatty liver drifts toward fat values and looks darker"),
 au("hu-osso", "Bone is the densest tissue on CT, reaching about {{c1::+1000}} HU", Z, E_, "Osso +1000 UH", 46, "prova", EP_TERM, "Azul: ponto superior da escala.",
    extra="- Cancellous bone is closer to +300 HU"),
 au("hu-musculo", "Muscle is slightly denser than water, about {{c1::+20 to +40}} HU", R, E_, "Músculo", 48, "lateral", EP_TERM, "Rosa: tabela da lâmina 48.",
    extra="- Soft tissues sit just above water on the scale"),
 au("hu-sangue-agudo", "Acute hemorrhage is denser than brain tissue, about {{c1::+65 to +95}} HU", R, E_, "Hemorragia aguda", 48, "lateral", EP_TERM,
    "Rosa: tabela da lâmina 48, sem aprofundar a doença.", extra="- It looks brighter than the surrounding brain"),
 au("hu-substancia", "On CT, brain white matter is slightly {{c1::less}} dense than gray matter", R, E_, "Substância branca × cinzenta", 48, "lateral", EP_TERM,
    "Rosa: tabela da lâmina 48 (+20 a +30 contra +30 a +40 UH).", extra="- Myelin lipids lower the attenuation of white matter"),
 au("hu-contraste", "Intravenous iodinated contrast can raise the attenuation of vessels to about {{c1::+250}} HU", R, E_, "Contraste IV ~250 UH", 46, "lateral", EP_CTR,
    "Rosa: ponto da escala da lâmina 46.", extra="- That is why opacified vessels look white"),

 # ---------- F. Janelas e níveis (lâminas 49–56) ----------
 au("janela-motivo", "Windows are needed because the eye tells apart far fewer {{c1::gray}} tones than the CT records", V, F_, "Por que janelas", 49, "central", EP_CT,
    "Verde: lâmina 49, raiz do conceito.", extra="- The eye separates about 20 shades, and CT holds at least 2000 values"),
 au("olho-cinzas", "The human eye distinguishes about {{c1::20}} gray shades on average, though CT stores at least 2000 values", R, F_, "Olho 20 tons × TC 2000", 49, "lateral", EP_CT,
    "Rosa: números da lâmina 49.", extra="- At most 64 shades, and only 256 can be shown on screen"),
 au("janela-nivel", "The <b>window level</b> is the {{c1::center}} of the range of attenuation values displayed", V, F_, "Nível da janela", 50, "central", EP_CT,
    "Verde: lâmina 50 marcada.", extra="- The level is the mean HU of the window"),
 au("janela-largura", "The <b>window width</b> is the {{c1::range}} of attenuation values displayed on the gray scale", V, F_, "Largura da janela", 50, "central", EP_CT,
    "Verde: lâmina 50 marcada.", extra="- A wider window shows more values with coarser gray steps"),
 au("janela-limites", "Values above the upper window limit appear {{c1::white}} and values below the lower limit appear {{c2::black}}", V, F_, "Limites da janela", 50, "central",
    EP_CT, "Verde: lâmina 50 (marcada).", extra="- Everything outside the window loses its detail"),
 au("janela-exemplo", "A window with level 50 and width 200 displays from {{c1::−50}} to {{c2::+150}} HU", R, F_, "Exemplo nível 50 largura 200", 51, "lateral", EP_CT,
    "Rosa: exemplo numérico da lâmina 51.", extra="- Half the width lies on each side of the level"),
 au("img-janela-partes-moles", '<img src="rd05-janela-partes-moles.png"><br>This chest <b>CT</b> is displayed in a {{c1::soft tissue}} window', Z, F_,
    "Janela de partes moles", 52, "central", EP_IMG, "Azul: lâmina 52.", extra="- Level near water separates muscle and fat, while lung is black and bone white"),
 au("img-janela-pulmao", '<img src="rd05-janela-pulmao.png"><br>This chest <b>CT</b> is displayed in a {{c1::lung}} window', Z, F_,
    "Janela de pulmão", 52, "central", EP_IMG, "Azul: lâmina 52.", extra="- Low level and wide window reveal the parenchymal vessels"),
 au("img-janela-osso", '<img src="rd05-janela-osso.png"><br>This chest <b>CT</b> is displayed in a {{c1::bone}} window', Z, F_,
    "Janela óssea", 52, "central", EP_IMG, "Azul: lâmina 52.", extra="- High level separates cortical from medullary bone"),
 sh(S_JOSSEA, "azul", F_, "Associação: janela óssea na fratura de calota", 52, "Azul: janela óssea."),
 au("janela-ampla", "A {{c1::wide}} window distinguishes structures with very different attenuation, such as lung and bone", V, F_, "Janela ampla", 55, "prova", EP_CT,
    "Verde: lâmina 55, par com a janela estreita.", extra="- The cost is less contrast between similar tissues"),
 au("janela-estreita", "A {{c1::narrow}} window distinguishes structures with similar attenuation, such as brain parenchyma and soft tissue", V, F_, "Janela estreita", 55, "prova",
    EP_CT, "Verde: lâmina 55.", extra="- The gray scale is spread over a short range of HU"),
 sh(S_HIPER, "verde", F_, "Associação: hiperatenuante", 56, "Verde: termo pedido em quase toda prova de TC; lâmina 56 marcada."),
 sh(S_HIPO, "verde", F_, "Associação: hipoatenuante", 56, "Verde: lâmina 56 marcada."),
 sh(S_ISO, "azul", F_, "Associação: isoatenuante", 56, "Azul: terceiro termo da nomenclatura."),
 au("referencia-lesao", "A lesion is called hyper- or hypoattenuating relative to the {{c1::organ}} that contains it", R, F_, "Tecido de referência", 56, "lateral", EP_TERM,
    "Rosa: regra da bibliografia da aula.", extra="- Without an organ, the window center is taken as isoattenuating"),
 au("calcio-hiper", "On CT, calcium is {{c1::hyperattenuating}} relative to soft tissue, though less than metal", Z, F_, "Cálcio hiperatenuante", 56, "prova", EP_TERM,
    "Azul: pedido em P1 2015.", extra="- Metal attenuates even more and causes artifacts"),

 # ---------- G. Técnicas do exame e fases (lâminas 57–67) ----------
 au("sem-contraste", "Non-contrast CT is advantageous to see bone, calcifications and {{c1::stones}}", Z, G_, "TC sem contraste", 58, "central", EP_CTR,
    "Azul: monitoria P1 e lâmina 58.", extra="- Without contrast the aorta is not brighter than other soft tissues"),
 sh(S_CIV, "verde", G_, "Associação: contraste IV é iodado", 59, "Verde: lâmina 59; prova P3 2015 pergunta o tipo de contraste."),
 au("contraste-realce-vasos", "On CT with intravenous contrast, vessels such as the {{c1::aorta}} become hyperattenuating", Z, G_, "Contraste realça vasos", 59, "prova", EP_CTR,
    "Azul: P1 2023 1.4 e P3 2017 2.2 pedem reconhecer o contraste pela aorta.", extra="- The kidneys also brighten as they excrete the iodine"),
 au("contraste-rim", "Iodinated contrast is excreted by the kidney, so {{c1::renal}} function is checked before contrast CT", Z, G_, "Função renal antes do contraste", 59, "prova",
    EP_SAFE, "Azul: P3 2017 2.2 e P2 2017 2.2.", extra="- Iodinated contrast is cleared by glomerular filtration"),
 au("contraste-multiaquisicao", "With intravenous contrast, CT is no longer a single acquisition, since the scan is repeated in each {{c1::phase}}", Z, G_,
    "Várias aquisições com contraste", 58, "central", EP_CTR, "Azul: fala sobre a lâmina 58.", extra="- Timing follows the movement of contrast through the body"),
 au("fases-ordem", "The phases of contrast CT in order are angiographic, arterial, portal, nephrographic, equilibrium and {{c1::excretory}}", V, G_, "Sequência das fases", 58,
    "prova", EP_CTR, "Verde: tabela da lâmina 58 marcada.", extra="- A non-contrast acquisition comes first, and the angiographic phase is at about 15 seconds"),
 au("tempo-arterial", "The <b>arterial</b> phase is acquired about {{c1::30}} seconds after the contrast injection", Z, G_, "Tempo da fase arterial", 58, "prova", EP_CTR,
    "Azul: tabela marcada na lâmina 58 e na apostila.", extra="- The portal phase comes later, at about 70 seconds"),
 au("tempo-portal", "The <b>portal</b> phase is acquired about {{c1::70}} seconds after the contrast injection", Z, G_, "Tempo da fase portal", 58, "prova", EP_CTR,
    "Azul: tabela marcada na lâmina 58 e na apostila.", extra="- The nephrographic phase follows at about 90 seconds"),
 au("tempo-tardia", "The <b>equilibrium</b> (late) phase is acquired about {{c1::3}} minutes after the contrast injection", Z, G_, "Tempo da fase de equilíbrio", 58, "prova", EP_CTR,
    "Azul: tabela marcada na lâmina 58 e na apostila.", extra="- The excretory phase comes last, at about 7 minutes"),
 au("fase-angiografica", "The angiographic phase, at about 15 s, is best to see {{c1::arteries}} such as the aorta and celiac trunk", Z, G_, "Fase angiográfica", 58, "central",
    EP_CTR, "Azul: monitoria P1.", extra="- It precedes the arterial phase"),
 au("fase-excretora", "The excretory phase, at about 7 min, shows contrast in the {{c1::collecting system}} and ureters", Z, G_, "Fase excretora", 58, "central", EP_CTR,
    "Azul: lâmina 58 e transcrição.", extra="- It is the last phase of the series"),
 au("img-sem-contraste", '<img src="rd05-fase-sem.png"><br>This abdominal <b>CT</b> was acquired {{c1::without}} contrast', Z, G_, "Reconhecer TC sem contraste", 62, "prova", EP_IMG,
    "Azul: lâmina 62 (aorta e rins sem realce).", extra="- Organs look gray and similar, with no bright aorta"),
 au("img-arterial", '<img src="rd05-fase-arterial.png"><br>This abdominal <b>CT</b> was acquired in the {{c1::arterial}} phase', Z, G_, "Reconhecer fase arterial", 63, "prova",
    EP_IMG, "Azul: lâmina 63 e prova ('aorta hiperatenuante').", extra="- Bright aorta and renal cortex, with unenhanced veins"),
 au("fase-arterial-nodulo", "In the arterial phase, {{c1::hypervascular}} liver nodules enhance and become visible", V, G_, "Fase arterial mostra nódulos", 63, "central", EP_CTR,
    "Verde: transcrição e prova P4 2025 ('hipercaptação').", extra="- Arteries brighten before veins"),
 au("fase-arterial-rim", "In the arterial phase the renal {{c1::cortex}} is best defined", Z, G_, "Fase arterial define o córtex renal", 63, "central", EP_CTR,
    "Azul: transcrição e monitoria.", extra="- The medulla is still unenhanced at this time"),
 au("img-portal", '<img src="rd05-fase-portal.png"><br>This abdominal <b>CT</b> was acquired in the {{c1::portal}} phase', Z, G_, "Reconhecer fase portal", 64, "prova", EP_IMG,
    "Azul: lâmina 64.", extra="- Portal and hepatic veins and the spleen are enhanced"),
 au("fase-portal-veias", "The portal phase makes the {{c1::portal}} vein and hepatic veins stand out", Z, G_, "Fase portal mostra veia porta", 64, "central", EP_CTR,
    "Azul: transcrição e monitoria.", extra="- The renal medulla also becomes visible"),
 au("img-tardia", '<img src="rd05-fase-tardia.png"><br>This abdominal <b>CT</b> was acquired in the {{c1::late}} phase', Z, G_, "Reconhecer fase tardia", 65, "prova", EP_IMG,
    "Azul: lâmina 65.", extra="- Contrast fills the renal pelvis, ready to be excreted"),
 au("fase-equilibrio-pelve", "In the equilibrium phase, contrast reaches the renal {{c1::pelvis}} and is ready to be excreted", Z, G_, "Fase de equilíbrio", 65, "central", EP_CTR,
    "Azul: transcrição.", extra="- Late-phase images can reveal stones and scars"),
 au("fase-nefrografica", "The nephrographic phase shows the renal parenchyma {{c1::homogeneously}} enhanced, without separating cortex and medulla", Z, G_, "Fase nefrográfica", 66, "central",
    EP_CTR, "Azul: lâmina 66 e monitoria.", extra="- It is a venous phase tailored to the kidney"),
 au("trifasico", "A triphasic abdominal CT is done without contrast and in the arterial, portal and {{c1::equilibrium}} phases", Z, G_, "Exame trifásico", 61, "central", EP_CTR,
    "Azul: lâmina 61.", extra="- Each acquisition is a separate pass through the gantry"),
 sh(S_FASEC, "azul", G_, "Associação: arterial antes da venosa", 61, "Azul: ordem das fases."),
 sh(S_FASEF, "azul", G_, "Associação: multifásica caracteriza nódulos hepáticos", 63, "Azul: aplicação principal das fases."),
 au("agua-vo", "Drinking water before CT {{c1::distends}} the bowel loops so wall and lumen can be assessed", R, G_, "Água oral", 67, "lateral", EP_CTR,
    "Rosa: lâmina 67 e transcrição.", extra="- Collapsed loops hide lesions and look crowded"),
 sh(S_VO, "rosa", G_, "Associação: contraste oral enche as alças", 67, "Rosa: lâmina 67, contraste VO."),
 au("retal-colo", "Rectal contrast opacifies the {{c1::colon}}, whereas oral contrast reaches the stomach and small bowel", R, G_, "Contraste retal × oral", 67, "lateral", EP_CTR,
    "Rosa: lâmina 67 e apostila.", extra="- Oral contrast also outlines part of the large bowel"),

 # ---------- H. Artefatos (lâminas 68–70) ----------
 sh(S_ARTDEF, "azul", H_, "Associação: definição de artefato", 68, "Azul: lâmina 68."),
 au("img-artefato-metal", '<img src="rd05-artefato-metal.png"><br>The streaks around the teeth are a {{c1::beam-hardening}} artifact from metal', Z, H_,
    "Artefato de endurecimento do feixe", 68, "prova", EP_IMG, "Azul: lâmina 68 e prova (artefato de metal).", extra="- Dental fillings absorb the beam and starve the detectors"),
 sh(S_ARTMET, "azul", H_, "Associação: metal gera artefato", 68, "Azul: lâmina 68."),
 au("img-artefato-mov", '<img src="rd05-artefato-movimento.png"><br>The smeared appearance of this head <b>CT</b> is a {{c1::motion}} artifact', Z, H_,
    "Artefato de movimento", 69, "central", EP_IMG, "Azul: lâmina 69.", extra="- Breathing or moving during the scan blurs the slices"),
 sh(S_ARTMOV, "azul", H_, "Associação: movimento gera artefato", 69, "Azul: lâmina 69."),
 au("endurecimento-feixe", "<b>Beam hardening</b> occurs when dense objects absorb low-energy photons and leave mostly {{c1::high}}-energy photons in the beam", Z, H_,
    "Mecanismo do endurecimento do feixe", 68, "central", EP_PHYS, "Azul: nome do artefato da lâmina 68; mecanismo do livro (ESR).", extra="- Metal implants produce streaks by this mechanism"),
 au("volume-parcial", "When a voxel holds tissues of different attenuation, its value is averaged, causing a {{c1::partial volume}} artifact", R, H_, "Artefato de volume parcial", 69,
    "lateral", EP_PHYS, "Rosa: citado na monitoria P1.", extra="- Thinner slices reduce the effect"),

 # ---------- I. Balanço (lâminas 89–94) ----------
 sh(S_RAPIDO, "azul", I_, "Associação: rápida e boa resolução espacial", 89, "Azul: vantagem da lâmina 89."),
 au("sem-superposicao", "CT removes the {{c1::superposition}} of structures that confounds the radiograph", V, I_, "Remove sobreposição", 89, "central", EP_CT,
    "Verde: vantagem marcada (lâmina 89) e razão de existir da TC.", extra="- It provides sectional images in any plane"),
 au("quantitativa", "CT is a {{c1::quantitative}} method because attenuation is measured in Hounsfield units", Z, I_, "Representação quantitativa", 89, "central", EP_TERM,
    "Azul: vantagem da lâmina 89.", extra="- Densities can be compared numerically between lesions"),
 au("boa-res-contraste", "CT has good {{c1::contrast}} resolution between structures, raised further by contrast media", Z, I_, "Boa resolução de contraste", 89, "central", EP_PHYS,
    "Azul: vantagem da lâmina 89.", extra="- It is still lower than MRI for soft tissues"),
 sh(S_RADIACAO, "verde", I_, "Associação: dose maior que a radiografia", 89, "Verde: desvantagem principal, pedida em prova."),
 au("sem-leito", "Unlike ultrasound, CT cannot be done at the {{c1::bedside}}, since the patient must be transported", Z, I_, "Não vai ao leito", 89, "prova", EP_SAFE,
    "Azul: desvantagem da lâmina 89; P2 2025 1.1.", extra="- The scanner is fixed in a dedicated room"),
 au("achados-urgentes", "Physicians must recognize findings that cannot wait for the {{c1::radiologist}}, such as a head-trauma hematoma", Z, I_, "Achados que não esperam", 90, "central",
    EP_SAFE, "Azul: objetivo declarado da aula (lâmina 90); exemplo só no Extra.", extra="- A midline shift calls for the neurosurgeon urgently"),
 sh(S_ACR, "azul", I_, "Associação: ACR Appropriateness Criteria", 91, "Azul: lâmina 91."),
 sh(S_ACRN, "rosa", I_, "Associação: notas do ACR", 91, "Rosa: classificação 1–9 da lâmina 91."),
 au("hounsfield-nobel", "<b>Godfrey Hounsfield</b> invented {{c1::CT}} and shared the 1979 Nobel Prize in Physiology or Medicine", R, I_, "Hounsfield e o Nobel", 94, "lateral", EP_PHYS,
    "Rosa: lâmina 94 e transcrição.", extra="- The first clinical CT image was of the brain, in 1971"),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
SEM_IMAGEM = "conceito, termo ou comparação sem estrutura própria a identificar; as imagens da aula estão nos cards de reconhecimento de planos, janelas, fases e artefatos"
for c in CARDS:
    if c["kind"] in ("text", "autoral", "anatoking") and "sem_imagem" not in c and "<img" not in c.get("text", ""):
        c["sem_imagem"] = SEM_IMAGEM

BOLD = {
 "gantry": ["CT scanner"], "tubo-detectores": ["X-ray tube"], "detector-sinal": ["CT detectors"], "bario-tc": ["iodinated contrast"],
 "axial-nativo": ["CT acquires"], "projecoes": ["Projections"], "scout": ["planning radiograph"], "leque": ["pyramidal"], "primeira-geracao": ["first CT scanners"],
 "single-multi": ["Single-slice", "multislice"], "helicoidal-apneia": ["Helical CT"], "terceira-geracao": ["most widely used"], "espessura-corte": ["Thinner CT slices"], "endurecimento-feixe": [], "multislice-ganho": ["Helical multislice"], "matriz": ["CT image"], "pixels-260k": ["512 by 512 matrix"],
 "retroprojecao": ["Raw CT data"], "mais-projecoes": ["projections"], "hu-ar": ["Air"], "hu-agua": ["Water"], "hu-gordura": ["Fat"], "hu-osso": ["Bone"],
 "hu-contraste": ["iodinated contrast"], "hu-branco": ["attenuates"], "hu-musculo": ["Muscle"], "hu-sangue-agudo": ["Acute hemorrhage"], "hu-substancia": ["white matter"],
 "janela-motivo": ["Windows"], "olho-cinzas": ["human eye"], "janela-limites": ["upper window limit", "lower limit"], "janela-exemplo": ["level 50", "width 200"],
 "janela-ampla": ["window"], "janela-estreita": ["window"], "referencia-lesao": ["hyper- or hypoattenuating"], "calcio-hiper": ["calcium"],
 "sem-contraste": ["Non-contrast CT"], "contraste-multiaquisicao": ["single acquisition"], "fases-ordem": ["phases of contrast CT"],
 "fase-angiografica": ["angiographic phase"], "fase-excretora": ["excretory phase"], "contraste-realce-vasos": ["intravenous contrast"],
 "contraste-rim": ["Iodinated contrast"], "trifasico": ["triphasic abdominal CT"], "fase-arterial-nodulo": ["arterial phase"], "fase-arterial-rim": ["arterial phase"],
 "fase-portal-veias": ["portal phase"], "fase-equilibrio-pelve": ["equilibrium phase"], "fase-nefrografica": ["nephrographic phase"], "agua-vo": ["Drinking water"],
 "retal-colo": ["Rectal contrast", "oral contrast"], "img-artefato-metal": ["streaks"], "volume-parcial": ["voxel"], "sem-superposicao": ["CT"],
 "quantitativa": ["CT"], "boa-res-contraste": ["CT"], "sem-leito": ["CT"], "achados-urgentes": ["Physicians"],
}
for c in CARDS:
    for ph in BOLD.get(c["key"], []):
        if c["kind"] == "autoral" and f"<b>{ph}</b>" not in c["text"] and ph in c["text"]:
            c["text"] = c["text"].replace(ph, f"<b>{ph}</b>", 1)

# ordem do Browser = ordem crescente das lâminas (sort estável preserva a ordem dentro da lâmina)
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))


# Análise do deck-prova 2026-10-13 (F-20261013-CLAUDE-03): cards tirados desta aula, com motivo.
RETIRADOS_ANALISE = {
 "lateralidade": "repetido",
 "injetora": "detalhe-tecnico",
 "detector-sinal": "detalhe-tecnico",
 "bario-tc": "detalhe",
 "mip": "detalhe-tecnico",
 "minip": "detalhe-tecnico",
 "leque": "detalhe-tecnico",
 "primeira-geracao": "detalhe-tecnico",
 "terceira-geracao": "detalhe-tecnico",
 "slip-rings": "detalhe-tecnico",
 "single-multi": "repetido",
 "helicoidal-apneia": "detalhe",
 "multislice-ganho": "repetido",
 "matriz": "detalhe-numerico",
 "pixels-260k": "detalhe-numerico",
 "fov": "detalhe-tecnico",
 "espessura-corte": "detalhe-tecnico",
 "retroprojecao": "detalhe-tecnico",
 "mais-projecoes": "detalhe-tecnico",
 "hu-contraste": "detalhe-numerico",
 "hu-branco": "repetido",
 "hu-musculo": "detalhe-numerico",
 "hu-sangue-agudo": "detalhe-numerico",
 "hu-substancia": "detalhe",
 "olho-cinzas": "detalhe-numerico",
 "janela-exemplo": "detalhe-numerico",
 "calcio-hiper": "repetido",
 "tempo-arterial": "detalhe-numerico",
 "tempo-portal": "detalhe-numerico",
 "tempo-tardia": "detalhe-numerico",
 "fase-angiografica": "detalhe-numerico",
 "fase-excretora": "detalhe-numerico",
 "trifasico": "repetido",
 "fase-arterial-rim": "detalhe",
 "fase-equilibrio-pelve": "detalhe",
 "fase-nefrografica": "detalhe",
 "agua-vo": "detalhe",
 "retal-colo": "detalhe",
 "endurecimento-feixe": "detalhe-tecnico",
 "volume-parcial": "detalhe-tecnico",
 "sem-superposicao": "repetido",
 "quantitativa": "repetido",
 "boa-res-contraste": "repetido",
 "sem-leito": "repetido",
 "sh-1791810568671": "detalhe-numerico"
}
CARDS = [c for c in CARDS if c['key'] not in RETIRADOS_ANALISE]
