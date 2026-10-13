# Especificação curada — Estrutura do estômago (UC08 P1, Biologia Tecidual, Profa. Patrícia Gama; 52 slides, um por página:
# Módulo 1 "Estrutura geral" do tubo digestório, slides 1–17; Módulo 2 "Estômago", slides 18–51).
# Feita em 02/10/2026 a partir de planejamento.json (escrito antes). Ordem = slides.
RUN_ID = "uc08-bt03-20261002a"
SHORT = "bt03"
LESSON = "2026-uc08-biologia-tecidual-03-estrutura-estomago"
DECK = "NEBLI::UC08::P1::Biologia Tecidual::Estrutura do estômago"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261002-CLAUDE-11) + PLANO-GERACAO-ANO, 02/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt, 19 consultas em 02/10); Referências Externas "
         "(Histology, LLU Histology, MCAT) pelos mesmos alvos (busca/ext.txt, 12 consultas): ")


def ak(key, src, flags, bloco, alvo, slide, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)


def hs(key, src, text, flags, bloco, alvo, slide, motivo, extra="", origin="Histology"):
    """Nota do acervo Histology (formato apostila, vários clozes) reduzida a uma frase com o alvo da aula."""
    return dict(key=key, kind="text", src=src, origin=origin, text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def io(key, page, name, cor, bloco, alvo, motivo, lines=(), search=(), rects=(), mask_rects=(), remarks=""):
    return dict(key=key, kind="slideio", page=page, half="full", title_size=99, lines=list(lines), search=list(search), rects=list(rects),
                mask_rects=list(mask_rects), name=name, remarks=remarks, aponta="estrutura", flags={1: cor}, bloco=bloco, alvo=alvo,
                evid=f"Slide {page}", motivo=motivo)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_ = "A-cavidade-oral", "B-parede-do-tubo", "C-regioes-do-estomago", "D-superficie-e-protecao", "E-glandula-gastrica", "F-enteroendocrinas"
PR = "Azul: rótulo da figura da própria aula."
CARDS = [
 # ---------- A. Cavidade oral e glândulas anexas (slides 3–11) ----------
 hs("lingua-ventral", 1702140426233, "The <b>ventral</b> surface of the tongue is smooth and covered by {{c1::<b>lining</b>}} mucosa, without papillae", {1: R}, A_,
    "Face ventral da língua: mucosa de revestimento, sem papilas", 7, "Rosa: única lâmina da língua na aula ('língua, superfície ventral')."),
 dict(key="papilas-botoes", kind="text", src=1560721171344, origin="MCAT", flags={1: R, 2: R}, bloco=A_, alvo="Papilas linguais contêm botões gustativos", evid="Slide 4",
      motivo="Rosas: slides 4 e 6 são figuras de livro sobre papilas e botão gustativo, sem objetivo no roteiro."),
 dict(key="papila-filiforme", kind="text", src=1590476939097, origin="MCAT", flags={1: R}, bloco=A_, alvo="Papilas filiformes não têm botões gustativos", evid="Slide 4",
      motivo="Rosa: legenda da figura do slide 4."),
 io("io-esmalte", 9, "Enamel", R, A_, "Esmalte", "Rosa: dente aparece em duas lâminas, sem objetivo próprio.", ["Esmalte"]),
 io("io-dentina", 9, "Dentin", R, A_, "Dentina", "Rosa: idem.", ["Dentina"]),
 io("io-polpa", 9, "Dental pulp", R, A_, "Polpa", "Rosa: idem.", ["Polpa"]),
 io("io-cemento", 9, "Cementum", R, A_, "Cemento", "Rosa: idem.", ["Cemento"]),
 io("io-lig-periodontal", 9, "Periodontal ligament", R, A_, "Ligamento periodontal", "Rosa: idem.", ["Ligamento periodontal"]),
 io("io-parotida", 10, "Parotid gland", Z, A_, "Parótida no esquema", PR, ["parótida"]),
 io("io-submandibular", 10, "Submandibular gland", Z, A_, "Submandibular no esquema", PR, ["submandibular"]),
 io("io-sublingual", 10, "Sublingual gland", Z, A_, "Sublingual no esquema", PR, ["sublingual"]),
 hs("parotida-serosa", 1702296274795, "The {{c1::<b>parotid</b>}} gland has exclusively <b>serous</b> acini, whose secretion is rich in α-amylase", {1: Z}, A_,
    "Parótida: ácinos serosos", 11, "Azul: tipo de ácino de cada glândula (slides 10–11; apostila da monitoria).", extra="<img src=\"nebli-uc08-bt03-p10f.png\" width=\"460\">"),
 hs("submandibular-mista", 1702296410763, "The {{c1::<b>submandibular</b>}} gland is <b>mixed</b>, with mostly serous acini, and produces about two-thirds of the saliva", {1: Z}, A_,
    "Submandibular: mista", 11, "Azul: idem.", extra="<img src=\"nebli-uc08-bt03-p10f.png\" width=\"460\">"),
 hs("sublingual-mucosa", 1702296589459, "The {{c1::<b>sublingual</b>}} gland, the smallest major salivary gland, is predominantly <b>mucous</b>", {1: Z}, A_,
    "Sublingual: mucosa", 11, "Azul: idem.", extra="<img src=\"nebli-uc08-bt03-p10f.png\" width=\"460\">"),
 # ---------- B. Parede do tubo digestório (slides 12–17) ----------
 ak("mucosa-camadas", 1482021549752, {1: V, 2: V, 3: V}, B_, "Mucosa: epitélio, lâmina própria e muscular da mucosa", 12, "Verdes: plano geral do tubo, objetivo 3 do roteiro."),
 ak("submucosa-posicao", 1482021556058, {1: Z}, B_, "Submucosa por fora da mucosa", 12, "Azul: sequência das camadas."),
 ak("muscular-externa-posicao", 1482021561377, {1: Z}, B_, "Muscular externa por fora da submucosa", 12, "Azul: sequência das camadas."),
 ak("serosa", 1482021584289, {1: V}, B_, "Serosa: camada externa dos segmentos intraperitoneais", 12, "Verde: par serosa × adventícia, cobrado no roteiro (esôfago: adventícia)."),
 ak("adventicia", 1482021589803, {1: V}, B_, "Adventícia: camada externa dos segmentos retroperitoneais", 12, "Verde: par do anterior."),
 hs("muscular-mucosa", 1702214620102, "The {{c1::<b>muscularis mucosae</b>}} is the thin layer of smooth muscle that separates the mucosa from the submucosa", {1: Z}, B_,
    "Muscular da mucosa separa mucosa e submucosa", 12, "Azul: limite que o roteiro manda achar em toda lâmina.",
    extra="- Moves the mucosa independently of the rest of the wall<br><br><img src=\"nebli-uc08-bt03-p13f.png\" width=\"460\">"),
 ak("esofago-epitelio", 1486608389324, {1: V}, B_, "Epitélio do esôfago", 13, "Verde: lâmina do esôfago é a primeira do roteiro prático (epitélio?)."),
 io("io-camada-mucosa", 13, "Mucosa", Z, B_, "Mucosa no corte de esôfago", PR, search=["camada mucosa"]),
 io("io-camada-submucosa", 13, "Submucosa", Z, B_, "Submucosa no corte de esôfago", PR, search=["camada submucosa"]),
 io("io-tunicas-musculares", 13, "Muscularis externa (muscular layers)", Z, B_, "Túnicas musculares no corte de esôfago", PR, search=["túnicas musculares"]),
 io("io-serosa-adventicia", 13, "Serosa or adventitia", Z, B_, "Serosa ou adventícia no corte", PR, lines=["camada serosa ou adventícia"]),
 ak("meissner-camada", 1482021594676, {1: V}, B_, "Plexo de Meissner na submucosa", 16, "Verde: HY (2)."),
 ak("meissner-funcao", 1482021680972, {1: V}, B_, "Plexo submucoso controla secreção e fluxo sanguíneo", 16, "Verde: HY (1)."),
 io("io-plexo-submucoso", 16, "Submucosal (Meissner) plexus", Z, B_, "Plexo submucoso na lâmina", PR, ["Plexo submucoso"]),
 ak("muscular-externa", 1482021567159, {1: V}, B_, "Muscular externa: circular interna e longitudinal externa", 17, "Verde: organização que se repete em todo o tubo."),
 io("io-circular-interna", 17, "Inner circular layer of the muscularis externa", Z, B_, "Circular interna na lâmina", PR, ["Circular interna"]),
 io("io-longitudinal-externa", 17, "Outer longitudinal layer of the muscularis externa", Z, B_, "Longitudinal externa na lâmina", PR, ["Longitunal externa"]),
 ak("auerbach-camada", 1482021603417, {1: V}, B_, "Plexo de Auerbach na muscular externa", 17, "Verde: HY (2)."),
 ak("auerbach-funcao", 1482021684208, {1: V}, B_, "Plexo mioentérico controla a motilidade", 17, "Verde: HY (1); título dos slides 15–17 é 'Motilidade e trânsito'."),
 io("io-plexo-mioenterico", 17, "Myenteric (Auerbach) plexus", Z, B_, "Plexo mioentérico na lâmina", PR, ["Plexo mioentérico"]),
 # ---------- C. Estômago: parede e regiões (slides 19–28) ----------
 sh(1790972067261, "verde", C_, "Camada muscular oblíqua do estômago", 20, "Já vivo na AN01 (autoral camada-obliqua); o slide 20 rotula as fibras oblíquas."),
 hs("rugas", 1702213597922, "The mucosa and submucosa of the empty stomach form longitudinal folds called {{c1::<b>rugae</b>}}, which flatten when the stomach fills", {1: Z}, C_,
    "Rugas: pregas de mucosa e submucosa", 21, "Azul: o que forma a prega (canal Osmosis; Junqueira)."),
 hs("juncao-esofagogastrica", 1702213752722, "At the <b>esophagogastric junction</b>, stratified squamous epithelium changes abruptly to {{c1::<b>simple columnar</b>}} epithelium", {1: V}, C_,
    "Transição esôfago–estômago", 21, "Verde: 'transições da mucosa' é item do roteiro prático e estudo complementar."),
 hs("fundo-corpo-iguais", 1702214781032, "Histologically, the <b>fundus</b> and the {{c1::<b>body</b>}} of the stomach are identical, and both contain the gastric (oxyntic) glands", {1: V}, C_,
    "Fundo e corpo são iguais na histologia", 27, "Verde: 'Estômago região do corpo + fundo' (slides 27 e 34); base das três regiões histológicas.", extra="<img src=\"nebli-uc08-bt03-p29f.png\" width=\"460\">"),
 au("mucosa-desmame", "In rodents, the gastric glands grow and the mucosa completes its maturation around {{c1::<b>weaning</b>}}, in the third postnatal week", {1: R}, C_,
    "Maturação pós-natal da mucosa gástrica", "23", "lateral", "nenhum card nos acervos; é a linha de pesquisa da professora.", [1482289524478, 1482275085375],
    "Rosa: três slides (22–24) sobre desenvolvimento da mucosa em animais de laboratório."),
 au("cardia-glandulas", "The glands of the <b>cardia</b> are coiled tubular glands that secrete mainly {{c1::<b>mucus</b>}} and lysozyme", {1: Z}, C_,
    "Glândulas da cárdia: enoveladas, mucosas", "26; Junqueira p. 310", "prova", "Histology 1702220517802 junta cárdia e piloro em 5 clozes; AnKing sem card.", [1486608734803, 1482115265611],
    "Azul: 'células secretoras de muco; glândulas enoveladas, aspecto tortuoso' no slide 26.", extra="<img src=\"nebli-uc08-bt03-p26f.png\" width=\"460\">"),
 io("io-glandulas-enoveladas", 26, "Coiled (tortuous) cardiac glands", R, C_, "Glândulas enoveladas da cárdia na lâmina", "Rosa: reconhecimento de apoio.",
    ["Glândulas enoveladas-", "aspecto tortuoso"]),
 au("piloro-fossetas", "In the <b>pyloric antrum</b>, the gastric pits are {{c1::<b>deep</b>::deep / shallow}} and the glands are short", {1: V}, C_,
    "Antro pilórico: fossetas profundas, glândulas rasas", "28; Junqueira p. 314; canal Osmosis", "central", "Histology 1702220517802 não compara profundidade; LLU só mostra a imagem.",
    [1482022140828, 1482022147543], "Verde: critério para reconhecer a região na lâmina ('fossetas profundas e glândulas rasas')."),
 au("piloro-funcao", "The glands of the <b>pyloric antrum</b> secrete mainly mucus and the hormone {{c1::<b>gastrin</b>}}", {1: Z}, C_,
    "Antro: muco e hormônios", "28; Junqueira p. 314", "prova", "AnKing tem a célula G no antro com 4 clozes (regulação, P2).", [1482030315536, 1482022013033],
    "Azul: 'função principal: produção de muco e de hormônios' no slide 28."),
 dict(key="regiao-fundica-he", kind="text", src=1667460205460, origin="LLU", flags={1: Z}, bloco=C_, alvo="Reconhecer a região do corpo/fundo em HE", evid="Slide 27",
      motivo="Azul: diagnóstico da região na lâmina, item 3 do roteiro prático."),
 dict(key="regiao-pilorica-he", kind="text", src=1667460370853, origin="LLU", flags={1: Z}, bloco=C_, alvo="Reconhecer a região pilórica em HE", evid="Slide 28",
      motivo="Azul: diagnóstico da região na lâmina."),
 # ---------- D. Superfície, fosseta e proteção (slides 29–33) ----------
 io("io-istmo", 29, "Isthmus of the gastric gland", Z, E_, "Istmo", PR, ["Istmo"]),
 io("io-colo", 29, "Neck of the gastric gland", Z, E_, "Colo", PR, ["Colo"]),
 io("io-base", 29, "Base of the gastric gland", Z, E_, "Base", PR, ["Base"]),
 ak("fossetas", 1486608728772, {1: V}, D_, "Fossetas gástricas", 30, "Verde: unidade que o roteiro manda achar primeiro (fosseta + glândula)."),
 hs("mucosas-superficiais", 1702214216607, "The stomach surface and the gastric pits are lined by {{c1::<b>surface mucous</b>}} cells, a simple columnar epithelium that secretes mucus and bicarbonate", {1: V}, D_,
    "Células mucosas superficiais", 30, "Verde: 'superfície do estômago: fosseta, células produtoras de muco'.", extra="<img src=\"nebli-uc08-bt03-p36f.png\" width=\"460\">"),
 ak("muco-bicarbonato", 1482115272152, {1: Z}, D_, "Muco retém bicarbonato", 30, "Azul: mecanismo de proteção do slide 30 (tag 5)."),
 ak("hpylori-antro", 1510261416840, {1: V}, D_, "H. pylori coloniza o antro", 32, "Verde: HY (1), 'infecção na região antro pilórico, principalmente'."),
 ak("hpylori-urease", 1482275983368, {1: V}, D_, "H. pylori produz urease", "33", "Verde: HY (2); 'fase ativa: produção de amônia' no slide 33."),
 # ---------- E. Glândula gástrica do corpo (slides 34–44) ----------
 ak("glandulas-corpo", 1486608734803, {1: Z}, E_, "Glândulas do corpo: mucosas, principais e parietais", 34, "Azul: lista dos tipos celulares (tag 5)."),
 hs("celulas-tronco-istmo", 1702214416325, "In the gastric glands, the <b>stem cells</b> lie in the {{c1::<b>isthmus</b>}} and neck, between the pit and the gland", {1: Z}, E_,
    "Células-tronco no istmo–colo", 35, "Azul: 'compartimento proliferativo' dos slides 25 e 35 (linha de pesquisa da professora).",
    extra="- Daughter cells migrate up to renew the surface and down to renew the gland<br><br><img src=\"nebli-uc08-bt03-p29f.png\" width=\"460\">"),
 io("io-celula-mucosa-superficial", 36, "Surface mucous cell", Z, E_, "Célula mucosa superficial na lâmina", "Azul: tipo celular do roteiro, na fotomicrografia da aula.", ["Célula mucosa superficial"]),
 io("io-celula-parietal", 36, "Parietal (oxyntic) cell", V, E_, "Célula parietal na lâmina", "Verde: item 3 do roteiro prático (identificar e diferenciar).", ["Célula parietal"]),
 io("io-celula-mucosa-colo", 36, "Mucous neck cell", Z, E_, "Célula mucosa do colo na lâmina", "Azul: item 3 do roteiro prático.", ["Célula mucosa do colo"]),
 io("io-celula-zimogenica", 36, "Chief (zymogenic) cell", V, E_, "Célula zimogênica na lâmina", "Verde: item 3 do roteiro prático.", ["Célula zimogênica"]),
 ak("parietal-hcl", 1482030311506, {1: V, 2: V, 3: Z, 4: V}, E_, "Célula parietal: HCl e fator intrínseco", 37, "c1, c2 e c4 verdes: HY (1); c3 azul (localização)."),
 ak("parietal-eosinofila", 1486608745216, {1: V, 2: Z}, E_, "Parietal é eosinófila", 37, "c1 verde: HY (1), é como se reconhece na lâmina; c2 azul."),
 au("parietal-posicao", "Within the gastric gland, <b>parietal cells</b> predominate in the {{c1::<b>isthmus and neck</b>::region}}", {1: Z}, E_,
    "Parietais predominam no istmo e colo", "37; roteiro prático; Junqueira p. 312", "prova", "AnKing só situa a célula no corpo do estômago.", [1482030311506, 1486608745216],
    "Azul: distribuição que o roteiro descreve região por região.", extra="- Chief cells predominate in the <b>base</b><br><br><img src=\"nebli-uc08-bt03-p29f.png\" width=\"460\">"),
 hs("parietal-canaliculo", 1702215619877, "The <b>parietal cell</b> has a deep invagination of its apical membrane, the {{c1::<b>intracellular canaliculus</b>}}, lined by microvilli", {1: Z}, E_,
    "Canalículo intracelular", 38, "Azul: estrutura rotulada no slide 38.", extra="<img src=\"nebli-uc08-bt03-p38f.png\" width=\"460\">"),
 io("io-canaliculo", 38, "Intracellular canaliculus", R, E_, "Canalículo no esquema", "Rosa: reconhecimento de apoio.", ["canalículo"], mask_rects=[(405, 106, 510, 132), (605, 106, 690, 132)]),
 io("io-mitocondrias", 38, "Mitochondria", R, E_, "Mitocôndrias da célula parietal", "Rosa: reconhecimento de apoio.", ["mitocôndrias"], mask_rects=[(405, 106, 510, 132), (605, 106, 690, 132)]),
 au("parietal-mitocondrias", "<b>Parietal cells</b> are packed with {{c1::<b>mitochondria</b>}}, which power the H+/K+ ATPase and make the cytoplasm eosinophilic", {1: Z}, E_,
    "Por que a parietal tem tantas mitocôndrias", "38; Junqueira p. 313", "prova", "AnKing só cita no Extra do card da parietal.", [1486608745216, 1482030311506],
    "Azul: liga a ultraestrutura do slide 38 à coloração.", duplicacao_ok="cobra a razão funcional; a oclusão rosa só aponta a organela", extra="<img src=\"nebli-uc08-bt03-p38f.png\" width=\"460\">"),
 au("parietal-ativacao", "When a <b>parietal cell</b> is stimulated, its {{c1::<b>tubulovesicles</b>}} fuse with the canaliculus, expanding the membrane that carries the proton pumps", {1: Z}, E_,
    "Ativação: tubulovesículas se fundem ao canalículo", "39; Junqueira p. 312", "prova", "nenhum card nos acervos sobre repouso × atividade.", [1482030319798, 1482022134697],
    "Azul: sequência repouso → estímulo → ativo do slide 39.", extra="<img src=\"nebli-uc08-bt03-p38f.png\" width=\"460\">"),
 ak("anidrase-carbonica", 1482030322556, {1: Z}, E_, "Anidrase carbônica na célula parietal", "40", "Azul: primeiro passo do esquema do slide 40 (tag 5)."),
 ak("bomba-protons", 1482030326785, {1: Z}, E_, "H+/K+ ATPase", "40", "Azul: bomba desenhada no slide 40 (tag 4); a secreção em si é da P2."),
 ak("cl-hco3", 1482030334468, {1: R}, E_, "Trocador Cl-/HCO3- basolateral", "40", "Rosa: detalhe do esquema (tag 4)."),
 hs("mucosas-colo", 1702215136161, "Between the parietal cells, in the neck of the gastric glands, lie the {{c1::<b>mucous neck</b>}} cells", {1: Z}, E_,
    "Células mucosas do colo", 42, "Azul: tipo celular do roteiro.", extra="<img src=\"nebli-uc08-bt03-p36f.png\" width=\"460\">"),
 au("mucosas-colo-mucina", "<b>Mucous neck cells</b> secrete a mucin different from that of the surface cells, with {{c1::<b>antibiotic</b>}} properties", {1: R}, E_,
    "Mucina do colo tem ação antibiótica", "42; Junqueira p. 312; apostila da monitoria", "lateral", "nenhum card nos acervos.", [1482115272152, 1482115265611],
    "Rosa: detalhe do slide 42 (mucina 6, TFF2, antibiótico).", extra="<img src=\"nebli-uc08-bt03-p36f.png\" width=\"460\">"),
 ak("principal-pepsinogenio", 1482030315536, {1: V, 2: Z, 3: V}, E_, "Célula principal: pepsinogênio e lipase gástrica", 44, "c1 e c3 verdes: HY (1); c2 azul (localização)."),
 ak("principal-basofila", 1486608739171, {1: V, 2: Z}, E_, "Principal é basófila", 44, "c1 verde: HY (1), reconhecimento na base da glândula; c2 azul."),
 ak("pepsinogenio-pepsina", 1482030319798, {1: Z, 2: Z}, E_, "Pepsinogênio → pepsina com H+", 44, "Azuis: destino do produto da célula zimogênica (canal Dr Mike)."),
 # ---------- F. Células enteroendócrinas (slides 45–46) ----------
 ak("grelina", 1482022013033, {1: V}, F_, "Grelina aumenta o apetite", 45, "Verde: HY (1); caixa 'Ghrelina: aumento do apetite' no slide 45."),
 au("grelina-celula", "Which hormone, produced by enteroendocrine cells of the <b>gastric body</b>, increases appetite and promotes growth?<br><br>{{c1::Ghrelin}}", {1: Z}, F_,
    "Grelina vem do corpo gástrico", "45; Junqueira p. 313", "prova", "AnKing diz só 'secretada no estômago'.", [1482022013033, 1486605738754],
    "Azul: origem e os dois efeitos listados no slide 45."),
 au("celula-g", "In the <b>pyloric antrum</b>, enteroendocrine {{c1::<b>G</b>}} cells are scattered among the mucous cells of the glands", {1: Z}, F_,
    "Células G no antro", "46; Junqueira p. 314", "prova", "AnKing 1482021686946 cobra gastrina, célula e dois sítios em 4 clozes (regulação, P2).", [1482030315536, 1482030311506],
    "Azul: 'célula G gastroendócrina (antro pilórico)' é a figura do slide 46."),
 ak("bypass-b12", 1476583770861, {1: V, 2: Z}, F_, "Cirurgia gástrica causa deficiência de B12", "47", "c1 verde: HY (1), liga as cirurgias dos slides 47–48 ao fator intrínseco da célula parietal; c2 azul."),
]

EXCLUIDOS = [
 (1702208297305, "Histology dente (9 clozes): coberto pelas oclusões do slide 9"), (1702140950842, "Histology papilas linguais (11 clozes): slide 4 é figura de livro, sem objetivo"),
 (1667448707885, "LLU glândula salivar: aula só mostra esquema e uma lâmina, sem diagnóstico pedido"), (1667459978330, "LLU junção esofagogástrica: imagens não mostram a transição com clareza"),
 (1667460073729, "LLU fúndico em menor aumento: redundante com o de maior aumento"), (1667460314025, "LLU pilórico em menor aumento: idem"),
 (1702213513286, "Histology regiões do estômago: lista sob um cloze"), (1702217278951, "Histology célula principal (7 clozes): coberto pelos AnKing"),
 (1702215793425, "Histology síntese de HCl (7 clozes): secreção é da P2"), (1702217002761, "Histology fator intrínseco (6 clozes): coberto pelo AnKing da parietal"),
 (1702217830783, "Histology enteroendócrinas (5 clozes): lista"), (1702220517802, "Histology glândulas da cárdia e piloro (5 clozes): substituído por três cards curtos"),
 (1702221209267, "Histology outras camadas do estômago (7 clozes): camada oblíqua já viva na AN01"), (1482021686946, "Gastrina de células G (4 clozes): regulação, P2"),
 (1482021663832, "Sinapses nos plexos: fisiologia (FI08)"), (1482021669311, "Sistema nervoso entérico autônomo: FI08"), (1489112951090, "Origem do plexo na crista neural: embriologia"),
 (1482030330644, "Canal de Cl- na parietal: detalhe da secreção (P2)"), (1482030372145, "Gastrina e CCKB: regulação (P2)"), (1461615595492, "Vago e M3: regulação (P2)"),
 (1482021700392, "Efeito trófico da gastrina: regulação (P2)"), (1482115265611, "Células mucosas em vários órgãos: genérico"), (1482014886764, "Mucosa é a camada mais interna: trivial"),
]
FORA_DO_RECORTE = [
 "Papilas linguais, botões gustativos e desenvolvimento do dente (slides 4–8): figuras de livro sem objetivo no roteiro",
 "Desenvolvimento pré e pós-natal da mucosa gástrica em roedores (slides 22–24): pesquisa da professora, sem alvo no roteiro",
 "Síntese e regulação do HCl, gastrina, histamina (slides 39–41, 45–46 em parte): fisiologia da secreção, P2",
 "Fases da infecção por H. pylori (slide 33): patologia",
 "Cirurgias bariátricas (slides 47–48) e organoides (slides 49–51): contexto de pesquisa e clínica, sem objetivo no roteiro",
 "Microcirculação gástrica (slide 41)",
]
