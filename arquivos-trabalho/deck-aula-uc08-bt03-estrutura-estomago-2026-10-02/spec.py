# Especificação curada — Estrutura do estômago (UC08 P1, Biologia Tecidual, Profa. Patrícia Gama; 52 slides, um por página:
# Módulo 1 "Estrutura geral" do tubo digestório, slides 1–17; Módulo 2 "Estômago", slides 18–51).
# Feita em 02/10/2026 a partir de planejamento.json (escrito antes). Ordem = slides.
RUN_ID = "uc08-bt03-20261002a"
SHORT = "bt03"
LESSON = "2026-uc08-biologia-tecidual-03-estrutura-estomago"
DECK = "NEBLI::UC08::P1::Biologia Tecidual::Estrutura do estômago"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261003-CLAUDE-13) + PLANO-GERACAO-ANO, v2 de 03/10/2026"
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


def hx(key, src, flags, bloco, alvo, slide, motivo):
    """Nota original do acervo Histology (Junqueira/Mescher cap. 15 em cards): texto inteiro, só os clozes do plano (v2, F-20261003-CLAUDE-13)."""
    return dict(key=key, kind="text", src=src, origin="Histology", manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


def io(key, page, name, cor, bloco, alvo, motivo, lines=(), search=(), rects=(), mask_rects=(), remarks="", por_linha=False):
    return dict(key=key, kind="slideio", page=page, half="full", title_size=99, por_linha=por_linha, lines=list(lines), search=list(search), rects=list(rects),
                mask_rects=list(mask_rects), name=name, remarks=remarks, aponta="estrutura", flags={1: cor}, bloco=bloco, alvo=alvo,
                evid=f"Slide {page}", motivo=motivo)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_ = "A-cavidade-oral", "B-parede-do-tubo", "C-regioes-do-estomago", "D-superficie-e-protecao", "E-glandula-gastrica", "F-enteroendocrinas"
PR = "Azul: rótulo da figura da própria aula."
CARDS = [
 # v2 (03/10, F-20261003-CLAUDE-13): teoria do Junqueira pelo deck Histology no lugar de oclusões e autorais que ele cobre;
 # oclusões só onde o roteiro pede identificação na lâmina. Chaves mantidas = mesma nota viva.
 # ---------- A. Cavidade oral e glândulas anexas (slides 2–11) ----------
 hx("papilas-tipos", 1702140950842, {1: Z, 2: Z, 6: R}, A_, "Tipos de papilas linguais", 4,
    "Azuis c1/c2: os quatro tipos de papila da figura do slide 4 (Kierszenbaum; Junqueira cap. 15). Rosa: superfície áspera da filiforme."),
 hx("botoes-papilas", 1702143581747, {2: Z, 3: R}, A_, "Botões gustativos nas papilas, não nas filiformes", 6, "Azul: botão gustativo do slide 6; rosa: valadas × filiformes."),
 hx("epitelio-oral", 1702139225813, {1: Z}, A_, "Boca revestida por epitélio estratificado pavimentoso", 7, "Azul: base da mucosa oral (Junqueira, cavidade oral)."),
 hx("mucosa-oral-tipos", 1702139641938, {1: Z, 2: Z}, A_, "Mucosa mastigatória queratinizada × de revestimento", 7, "Azuis: tipos de mucosa oral; a face ventral da língua (slide 7) é de revestimento."),
 hx("lingua-musculo", 1702140194813, {1: Z}, A_, "Língua: músculo estriado coberto por mucosa", 7, "Azul: estrutura da língua (slide 7)."),
 hx("lingua-superficies", 1702140426233, {1: Z, 2: R, 5: R}, A_, "Face ventral lisa, dorso com papilas, sulco terminal", 7, "Azul c1: 'língua, superfície ventral' do slide 7; rosas: dorso e sulco terminal."),
 hx("dente-composicao", 1702208297305, {1: Z, 4: Z, 2: R, 3: R}, A_, "Esmalte, cemento, dentina, polpa e ligamento periodontal", 9,
    "Azuis: os tecidos rotulados no slide 9 (esmalte, dentina, cemento) e onde ficam; rosas: polpa e ligamento. Substitui as cinco oclusões da v1."),
 hx("odontoblastos", 1702208460704, {1: R}, A_, "Odontoblastos formam a dentina", 9, "Rosa: dente em crescimento do slide 9 (Junqueira, dentina)."),
 hx("ameloblastos", 1702210071880, {1: R}, A_, "Ameloblastos formam o esmalte", 9, "Rosa: idem (Junqueira, esmalte)."),
 hx("ligamento-periodontal", 1702211317364, {3: R}, A_, "Ligamento periodontal liga cemento ao osso alveolar", 9, "Rosa: ligamento periodontal e osso alveolar rotulados no slide 9."),
 hx("parotida", 1702296274795, {1: Z, 2: R}, A_, "Parótida: ácinos exclusivamente serosos, amilase", 10, "Azul c1: tipo de ácino de cada glândula (slides 10–11; apostila da monitoria); rosa: amilase."),
 hx("submandibular", 1702296410763, {1: Z, 5: R}, A_, "Submandibular: mista, com semiluas serosas", 10, "Azul: glândula mista; rosa: semilua serosa."),
 hx("sublingual", 1702296589459, {1: Z, 3: Z}, A_, "Sublingual: predominantemente mucosa", 10, "Azuis: menor glândula maior e predominantemente mucosa."),
 hx("celula-serosa", 1702294558765, {1: Z, 5: R}, A_, "Célula serosa forma ácino", 11, "Azul: célula serosa na lâmina do slide 11 (Kierszenbaum); rosa: ácino."),
 hx("celula-mucosa-salivar", 1702294697860, {1: Z, 4: R}, A_, "Célula mucosa: mucinas, cora pouco", 11, "Azul: célula mucosa; rosa: por que cora pouco no HE."),
 hx("mioepitelial", 1702294881426, {1: R}, A_, "Células mioepiteliais em torno dos ácinos", 11, "Rosa: estrutura dos ácinos no slide 11."),
 # ---------- B. Parede do tubo digestório (slides 12–17) ----------
 ak("mucosa-camadas", 1482021549752, {1: V, 2: V, 3: V}, B_, "Mucosa: epitélio, lâmina própria e muscular da mucosa", 12, "Verdes: plano geral do tubo, objetivo 3 do roteiro."),
 ak("submucosa-posicao", 1482021556058, {1: Z}, B_, "Submucosa por fora da mucosa", 12, "Azul: sequência das camadas."),
 ak("muscular-externa-posicao", 1482021561377, {1: Z}, B_, "Muscular externa por fora da submucosa", 12, "Azul: sequência das camadas."),
 ak("serosa", 1482021584289, {1: V}, B_, "Serosa: camada externa dos segmentos intraperitoneais", 12, "Verde: par serosa × adventícia, cobrado no roteiro (esôfago: adventícia)."),
 ak("adventicia", 1482021589803, {1: V}, B_, "Adventícia: camada externa dos segmentos retroperitoneais", 12, "Verde: par do anterior."),
 hx("lamina-propria", 1702137863607, {3: Z}, B_, "Lâmina própria: tecido conjuntivo frouxo", 12, "Azul: composição da mucosa (Junqueira, estrutura geral)."),
 hx("muscular-mucosa", 1702214620102, {1: Z}, B_, "Muscular da mucosa separa mucosa e submucosa", 12, "Azul: limite que o roteiro manda achar em toda lâmina."),
 hx("submucosa-conteudo", 1702137933347, {1: Z}, B_, "Submucosa: conjuntivo denso, plexo de Meissner, glândulas e tecido linfoide", 12, "Azul: o que há na submucosa."),
 hx("serosa-mesotelio", 1702138739648, {3: Z}, B_, "Serosa revestida por mesotélio", 12, "Azul: o que reveste a serosa (Junqueira)."),
 hx("malt", 1702138880755, {1: R}, B_, "MALT na mucosa e submucosa", 12, "Rosa: tecido linfoide associado à mucosa (Junqueira, estrutura geral)."),
 ak("esofago-epitelio", 1486608389324, {1: V}, B_, "Epitélio do esôfago", 13, "Verde: lâmina do esôfago é a primeira do roteiro prático (epitélio?)."),
 hx("esofago-glandulas", 1702212450000, {6: Z, 4: R}, B_, "Glândulas esofágicas na submucosa; cárdicas perto do estômago", 13, "Azul: glândulas do esôfago (lâmina do roteiro); rosa: glândulas cárdicas do esôfago."),
 io("io-camada-mucosa", 13, "Mucosa", Z, B_, "Mucosa no corte de esôfago", PR, search=["camada mucosa"], por_linha=True),
 io("io-camada-submucosa", 13, "Submucosa", Z, B_, "Submucosa no corte de esôfago", PR, search=["camada submucosa"], por_linha=True),
 io("io-tunicas-musculares", 13, "Muscularis externa (muscular layers)", Z, B_, "Túnicas musculares no corte de esôfago", PR, search=["túnicas musculares"], por_linha=True),
 io("io-serosa-adventicia", 13, "Serosa or adventitia", Z, B_, "Serosa ou adventícia no corte", PR, lines=["camada serosa ou adventícia"], por_linha=True),
 ak("meissner-camada", 1482021594676, {1: V}, B_, "Plexo de Meissner na submucosa", 16, "Verde: HY (2)."),
 ak("meissner-funcao", 1482021680972, {1: V}, B_, "Plexo submucoso controla secreção e fluxo sanguíneo", 16, "Verde: HY (1)."),
 io("io-plexo-submucoso", 16, "Submucosal (Meissner) plexus", Z, B_, "Plexo submucoso na lâmina", PR, ["Plexo submucoso"]),
 ak("muscular-externa", 1482021567159, {1: V}, B_, "Muscular externa: circular interna e longitudinal externa", 17, "Verde: organização que se repete em todo o tubo."),
 ak("auerbach-camada", 1482021603417, {1: V}, B_, "Plexo de Auerbach na muscular externa", 17, "Verde: HY (2)."),
 ak("auerbach-funcao", 1482021684208, {1: V}, B_, "Plexo mioentérico controla a motilidade", 17, "Verde: HY (1); título dos slides 15–17 é 'Motilidade e trânsito'."),
 io("io-plexo-mioenterico", 17, "Myenteric (Auerbach) plexus", Z, B_, "Plexo mioentérico na lâmina", PR, ["Plexo mioentérico"]),
 # ---------- C. Estômago: parede e regiões (slides 19–28) ----------
 sh(1790972067261, "verde", C_, "Camada muscular oblíqua do estômago", 20, "Já vivo na AN01 (autoral camada-obliqua); o slide 20 rotula as fibras oblíquas."),
 hx("esfincter-pilorico", 1702221209267, {6: Z}, C_, "Esfíncter pilórico: espessamento da camada circular", 20, "Azul: camadas musculares do estômago no slide 20 (Junqueira)."),
 hx("rugas", 1702213597922, {1: Z}, C_, "Rugas: pregas de mucosa e submucosa", 21, "Azul: o que forma a prega (canal Osmosis; Junqueira)."),
 hx("juncao-esofagogastrica", 1702213752722, {1: V, 3: Z}, C_, "Transição esôfago–estômago", 21, "Verde: 'transições da mucosa' é item do roteiro prático; azul: fossetas gástricas."),
 au("mucosa-desmame", "In rodents, the gastric glands grow and the mucosa completes its maturation around {{c1::<b>weaning</b>}}, in the third postnatal week", {1: R}, C_,
    "Maturação pós-natal da mucosa gástrica", "23", "lateral", "nenhum card nos acervos (Histology e LLU sem desenvolvimento pós-natal); é a linha de pesquisa da professora.", [1482289524478, 1482275085375],
    "Rosa: três slides (22–24) sobre desenvolvimento da mucosa em animais de laboratório."),
 hx("cardia-piloro-glandulas", 1702220517802, {3: V, 4: Z, 5: Z}, C_, "Cárdia e piloro: fossetas longas, glândulas enoveladas mucosas, sem parietais", 26,
    "Verde c3: critério de reconhecer cárdia e piloro na lâmina (slides 26 e 28); azuis: secretam muco e não têm parietais nem principais. Substitui três autorais e uma oclusão da v1."),
 hx("fundo-corpo-iguais", 1702214781032, {1: V}, C_, "Fundo e corpo são iguais na histologia", 27, "Verde: 'Estômago região do corpo + fundo' (slides 27 e 34); base das três regiões histológicas."),
 dict(key="regiao-fundica-he", kind="text", src=1667460205460, origin="LLU", identificacao=True, flags={1: Z}, bloco=C_, alvo="Reconhecer a região do corpo/fundo em HE", evid="Slide 27",
      motivo="Azul: diagnóstico da região na lâmina, item 3 do roteiro prático."),
 dict(key="regiao-pilorica-he", kind="text", src=1667460370853, origin="LLU", identificacao=True, flags={1: Z}, bloco=C_, alvo="Reconhecer a região pilórica em HE", evid="Slide 28",
      motivo="Azul: diagnóstico da região na lâmina."),
 # ---------- D. Superfície, fosseta e proteção (slides 29–33) ----------
 io("io-istmo", 29, "Isthmus of the gastric gland", Z, E_, "Istmo", PR, ["Istmo"]),
 io("io-colo", 29, "Neck of the gastric gland", Z, E_, "Colo", PR, ["Colo"]),
 io("io-base", 29, "Base of the gastric gland", Z, E_, "Base", PR, ["Base"]),
 ak("fossetas", 1486608728772, {1: V}, D_, "Fossetas gástricas", 30, "Verde: unidade que o roteiro manda achar primeiro (fosseta + glândula)."),
 hx("mucosas-superficiais", 1702214216607, {1: V, 3: Z}, D_, "Células mucosas superficiais e camada de muco", 30, "Verde: 'superfície do estômago: fosseta, células produtoras de muco'; azul: camada de muco protege."),
 ak("muco-bicarbonato", 1482115272152, {1: Z}, D_, "Muco retém bicarbonato", 30, "Azul: mecanismo de proteção do slide 30 (tag 5)."),
 ak("hpylori-antro", 1510261416840, {1: V}, D_, "H. pylori coloniza o antro", 32, "Verde: HY (1), 'infecção na região antro pilórico, principalmente'."),
 ak("hpylori-urease", 1482275983368, {1: V}, D_, "H. pylori produz urease", "33", "Verde: HY (2); 'fase ativa: produção de amônia' no slide 33."),
 # ---------- E. Glândula gástrica do corpo (slides 34–44) ----------
 ak("glandulas-corpo", 1486608734803, {1: Z}, E_, "Glândulas do corpo: mucosas, principais e parietais", 34, "Azul: lista dos tipos celulares (tag 5)."),
 hx("celulas-tronco-istmo", 1702214416325, {2: Z, 5: R}, E_, "Células-tronco no istmo", 35, "Azul: 'compartimento proliferativo' dos slides 25 e 35 (linha de pesquisa da professora); rosa: progenitoras sobem."),
 hx("progenitoras-glandula", 1702214504475, {1: R}, E_, "Progenitoras descem e viram células secretoras", 35, "Rosa: renovação mais lenta na glândula (slide 35)."),
 io("io-celula-mucosa-superficial", 36, "Surface mucous cell", Z, E_, "Célula mucosa superficial na lâmina", "Azul: tipo celular do roteiro, na fotomicrografia da aula.", ["Célula mucosa superficial"]),
 io("io-celula-parietal", 36, "Parietal (oxyntic) cell", V, E_, "Célula parietal na lâmina", "Verde: item 3 do roteiro prático (identificar e diferenciar).", ["Célula parietal"]),
 io("io-celula-mucosa-colo", 36, "Mucous neck cell", Z, E_, "Célula mucosa do colo na lâmina", "Azul: item 3 do roteiro prático.", ["Célula mucosa do colo"]),
 io("io-celula-zimogenica", 36, "Chief (zymogenic) cell", V, E_, "Célula zimogênica na lâmina", "Verde: item 3 do roteiro prático.", ["Célula zimogênica"]),
 ak("parietal-hcl", 1482030311506, {1: V, 2: V, 3: Z, 4: V}, E_, "Célula parietal: HCl e fator intrínseco", 37, "c1, c2 e c4 verdes: HY (1); c3 azul (localização)."),
 ak("parietal-eosinofila", 1486608745216, {1: V, 2: Z}, E_, "Parietal é eosinófila", 37, "c1 verde: HY (1), é como se reconhece na lâmina; c2 azul."),
 hx("parietal-estrutura", 1702215619877, {3: Z, 5: Z, 6: Z}, E_, "Parietal: entre as mucosas do colo, eosinófila pelas mitocôndrias, canalículo intracelular", 38,
    "Azuis: posição na glândula, razão da eosinofilia e canalículo rotulado no slide 38. Substitui dois autorais, uma reescrita e duas oclusões da v1."),
 au("parietal-ativacao", "When a <b>parietal cell</b> is stimulated, its {{c1::<b>tubulovesicles</b>}} fuse with the canaliculus, expanding the membrane that carries the proton pumps", {1: Z}, E_,
    "Ativação: tubulovesículas se fundem ao canalículo", "39; Junqueira p. 312", "prova", "nenhum card nos acervos sobre repouso × atividade (Histology 1702215619877 só descreve o canalículo).", [1482030319798, 1482022134697],
    "Azul: sequência repouso → estímulo → ativo do slide 39.", extra="<img src=\"nebli-uc08-bt03-p38f.png\" width=\"460\">"),
 ak("anidrase-carbonica", 1482030322556, {1: Z}, E_, "Anidrase carbônica na célula parietal", "40", "Azul: primeiro passo do esquema do slide 40 (tag 5)."),
 ak("bomba-protons", 1482030326785, {1: Z}, E_, "H+/K+ ATPase", "40", "Azul: bomba desenhada no slide 40 (tag 4); a secreção em si é da P2."),
 ak("cl-hco3", 1482030334468, {1: R}, E_, "Trocador Cl-/HCO3- basolateral", "40", "Rosa: detalhe do esquema (tag 4)."),
 hx("mucosas-colo", 1702215136161, {1: Z, 3: R}, E_, "Células mucosas do colo", 42, "Azul: tipo celular do roteiro; rosa: núcleo redondo e grânulos apicais."),
 au("mucosas-colo-mucina", "<b>Mucous neck cells</b> secrete a mucin different from that of the surface cells, with {{c1::<b>antibiotic</b>}} properties", {1: R}, E_,
    "Mucina do colo tem ação antibiótica", "42; Junqueira p. 312; apostila da monitoria", "lateral", "nenhum card nos acervos (Histology 1702215136161 só diz que o muco é menos alcalino).", [1482115272152, 1482115265611],
    "Rosa: detalhe do slide 42 (mucina 6, TFF2, antibiótico).", extra="<img src=\"nebli-uc08-bt03-p36f.png\" width=\"460\">"),
 ak("principal-pepsinogenio", 1482030315536, {1: V, 2: Z, 3: V}, E_, "Célula principal: pepsinogênio e lipase gástrica", 44, "c1 e c3 verdes: HY (1); c2 azul (localização)."),
 ak("principal-basofila", 1486608739171, {1: V, 2: Z}, E_, "Principal é basófila", 44, "c1 verde: HY (1), reconhecimento na base da glândula; c2 azul."),
 ak("pepsinogenio-pepsina", 1482030319798, {1: Z, 2: Z}, E_, "Pepsinogênio → pepsina com H+", 44, "Azuis: destino do produto da célula zimogênica (canal Dr Mike)."),
 hx("principal-rer", 1702217278951, {3: Z}, E_, "Principal secreta proteína, rica em RER", 44, "Azul: ultraestrutura que explica a basofilia (Junqueira)."),
 # ---------- F. Células enteroendócrinas (slides 45–47) ----------
 ak("grelina", 1482022013033, {1: V}, F_, "Grelina aumenta o apetite", 45, "Verde: HY (1); caixa 'Ghrelina: aumento do apetite' no slide 45."),
 au("grelina-celula", "Which hormone, produced by enteroendocrine cells of the <b>gastric body</b>, increases appetite and promotes growth?<br><br>{{c1::Ghrelin}}", {1: Z}, F_,
    "Grelina vem do corpo gástrico", "45; Junqueira p. 313", "prova", "AnKing diz só 'secretada no estômago'; Histology sem grelina.", [1482022013033, 1486605738754],
    "Azul: origem e os dois efeitos listados no slide 45."),
 hx("enteroendocrinas-estomago", 1702217830783, {1: Z, 5: Z, 3: R}, F_, "Enteroendócrinas: G no piloro, serotonina no fundo", 46,
    "Azuis: célula enteroendócrina e célula G do antro (slide 46). Substitui o autoral celula-g da v1."),
 ak("bypass-b12", 1476583770861, {1: V, 2: Z}, F_, "Cirurgia gástrica causa deficiência de B12", "47", "c1 verde: HY (1), liga as cirurgias dos slides 47–48 ao fator intrínseco da célula parietal; c2 azul."),
]

EXCLUIDOS = [
 (1667448707885, "LLU glândula salivar: aula só mostra esquema e uma lâmina, sem diagnóstico pedido"), (1667459978330, "LLU junção esofagogástrica: imagens não mostram a transição com clareza"),
 (1667460073729, "LLU fúndico em menor aumento: redundante com o de maior aumento"), (1667460314025, "LLU pilórico em menor aumento: idem"),
 (1702213513286, "Histology regiões do estômago: lista sob um cloze"),
 (1702215793425, "Histology síntese de HCl (7 clozes): AnKing anidrase, bomba e trocador já cobrem o esquema do slide 40"), (1702217002761, "Histology fator intrínseco (6 clozes): coberto pelo AnKing da parietal"),
 (1482021686946, "Gastrina de células G (4 clozes): regulação, P2"),
 (1482021663832, "Sinapses nos plexos: fisiologia (FI08)"), (1482021669311, "Sistema nervoso entérico autônomo: FI08"), (1489112951090, "Origem do plexo na crista neural: embriologia"),
 (1482030330644, "Canal de Cl- na parietal: detalhe da secreção (P2)"), (1482030372145, "Gastrina e CCKB: regulação (P2)"), (1461615595492, "Vago e M3: regulação (P2)"),
 (1482021700392, "Efeito trófico da gastrina: regulação (P2)"), (1482115265611, "Células mucosas em vários órgãos: genérico"), (1482014886764, "Mucosa é a camada mais interna: trivial"),
]
FORA_DO_RECORTE = [
 "Desenvolvimento pré e pós-natal da mucosa gástrica em roedores (slides 22–24): pesquisa da professora, sem alvo no roteiro",
 "Síntese e regulação do HCl, gastrina, histamina (slides 39–41, 45–46 em parte): fisiologia da secreção, P2",
 "Fases da infecção por H. pylori (slide 33): patologia",
 "Cirurgias bariátricas (slides 47–48) e organoides (slides 49–51): contexto de pesquisa e clínica, sem objetivo no roteiro",
 "Microcirculação gástrica (slide 41)",
]

# F-20261003-CLAUDE-14: notas longas do Histology recortadas em cards de uma frase
from nebli.hx_cortes import recortar
from hx_cortes import CORTES
CARDS = recortar(CARDS, CORTES)

# F-20261003-CLAUDE-15: figura de livro/AnKing no verso dos cards de estrutura
from nebli.ilustrar import ilustrar
from imagens import IMAGENS, SEM_IMAGEM
CARDS = ilustrar(CARDS, IMAGENS, SEM_IMAGEM)
from nebli.ilustrar import anotar
from notas import NOTAS
CARDS = anotar(CARDS, NOTAS)
