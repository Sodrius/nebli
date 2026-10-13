# Especificação curada — Intestinos (UC08 P1, Biologia Tecidual, Profa. Patrícia Gama; 36 slides, um por página, "Módulo 3 - Intestinos").
# Feita em 02/10/2026 a partir de planejamento.json (escrito antes). Ordem = slides.
RUN_ID = "uc08-bt04-20261002a"
SHORT = "bt04"
LESSON = "2026-uc08-biologia-tecidual-04-intestinos"
DECK = "NEBLI::UC08::P1::Biologia Tecidual::Intestinos"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261003-CLAUDE-13), v2 de 03/10 + PLANO-GERACAO-ANO, 02/10/2026"
MEDIA = {f"nebli-uc08-bt04-p{p:02d}f.png": f"io/nebli-uc08-bt04-p{p:02d}f.png" for p in (13, 14, 20, 22, 27)}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt, 17 consultas em 02/10); Referências Externas "
         "(Histology, LLU Histology, MCAT) pelos mesmos alvos (busca/ext.txt, 7 consultas): ")
F = lambda p, w=460: f'<img src="nebli-uc08-bt04-p{p:02d}f.png" width="{w}">'


def ak(key, src, flags, bloco, alvo, slide, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)


def hs(key, src, text, flags, bloco, alvo, slide, motivo, extra="", origin="Histology"):
    return dict(key=key, kind="text", src=src, origin=origin, text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


def hx(key, src, flags, bloco, alvo, slide, motivo):
    """Nota original do acervo Histology (Junqueira/Mescher cap. 15 em cards): texto inteiro, só os clozes do plano (v2, F-20261003-CLAUDE-13)."""
    return dict(key=key, kind="text", src=src, origin="Histology", manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def io(key, page, name, cor, bloco, alvo, motivo, lines=(), search=(), rects=(), mask_rects=(), remarks=""):
    return dict(key=key, kind="slideio", page=page, half="full", title_size=99, lines=list(lines), search=list(search), rects=list(rects),
                mask_rects=list(mask_rects), name=name, remarks=remarks, aponta="estrutura", flags={1: cor}, bloco=bloco, alvo=alvo,
                evid=f"Slide {page}", motivo=motivo)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_ = "A-parede-e-superficie", "B-renovacao-e-linhagens", "C-celulas-do-epitelio", "D-vilosidade-e-cripta", "E-segmentos-do-delgado", "F-intestino-grosso"
CARDS = [
 # ---------- A. Parede, transição e aumento de superfície (slides 2–9) ----------
 sh(1790979862409, "verde", A_, "Mucosa: epitélio, lâmina própria e muscular da mucosa", 2, "Já vivo na BT03; o slide 2 repete o corte geral do tubo."),
 ak("epitelio-intestinal", 1486608749626, {1: V}, A_, "Epitélio cilíndrico simples nos intestinos", 6, "Verde: HY (1); 'qual o tipo de epitélio?' é pergunta do roteiro prático."),
 io("io-transicao-estomago", 6, "Stomach (pyloric mucosa, with gastric pits)", Z, A_, "Lado gástrico da transição", "Azul: 'transições da mucosa' é item do roteiro prático.", ["Estômago"],
    mask_rects=[(160, 495, 560, 525)]),
 io("io-transicao-duodeno", 6, "Small intestine (duodenum, with villi)", Z, A_, "Lado duodenal da transição", "Azul: idem.", ["Intestino delgado", "duodeno"], mask_rects=[(160, 495, 560, 525)]),
 ak("vilos-microvilos", 1486608754106, {1: V}, A_, "Vilosidades e microvilosidades ampliam a superfície", 7, "Verde: estrutura que define o delgado (slides 7–9)."),
 dict(key="vilos-area", kind="text", src=1556167083570, origin="MCAT", flags={1: Z, 2: Z}, bloco=A_,
      text="{{c1::Villi}} are small finger-like projections that increase the intestinal {{c2::surface area}}", alvo="Vilosidade: projeção em dedo que aumenta a área", evid="Slide 8",
      motivo="Azuis: definição e função, lâmina 'intestino delgado' do slide 8."),
 sh(1790972071061, "azul", A_, "Pregas circulares distinguem o jejuno", 9, "Já vivo na AN01; 'primeiro grau de pregueamento' no slide 9."),
 hx("delgado-mucosa", 1702222533504, {1: Z, 2: Z, 8: Z, 10: Z, 11: R}, A_, "Pregas circulares, eixo do vilo de lâmina própria com lácteo", 9,
    "Azuis: pregas (mucosa + submucosa, jejuno) e eixo do vilo de conjuntivo frouxo da lâmina própria com plasmócitos e lácteo (slides 9 e 20); rosa: capilares fenestrados. Substitui a reescrita e dois autorais da v1."),
 # ---------- B. Renovação epitelial e linhagens (slides 10–16) ----------
 ak("criptas-delgado", 1486608758394, {1: Z}, B_, "Criptas de Lieberkühn nos três segmentos", 10, "Azul: nome da glândula intestinal."),
 ak("celulas-tronco-cripta", 1486608763486, {1: V}, B_, "Células-tronco ficam nas criptas", 10, "Verde: HY (1); eixo da aula (slides 10–16)."),
 hx("criptas-epitelio", 1702224421203, {2: Z}, B_, "Criptas: glândulas tubulares curtas entre os vilos", 10, "Azul: o que é a cripta (Junqueira)."),
 au("cripta-proliferacao", "The {{c1::<b>crypt</b>::villus / crypt}} is the proliferative compartment of the intestinal epithelium, as shown by Ki67 staining", {1: V}, B_,
    "Cripta é o compartimento proliferativo", "13; roteiro prático; Junqueira p. 317", "central", "AnKing diz onde estão as células-tronco, não onde há proliferação.", [1486608763486, 1482359449381],
    "Verde: resposta do roteiro ('na cripta há células em divisão, por quê?').", extra=F(13), duplicacao_ok="resposta 'crypt' coincide com cards que definem a cripta e a sede das células-tronco; aqui é o compartimento proliferativo (Ki67), pergunta do roteiro"),
 au("vilo-apoptose", "Epithelial cells die by apoptosis and are shed at the {{c1::<b>tip of the villus</b>}}, as shown by TUNEL staining", {1: Z}, B_,
    "Apoptose e descamação no topo do vilo", "13; Junqueira p. 316", "prova", "nenhum card nos acervos.", [1486608763486, 1482359431570], "Azul: par do anterior no slide 13.", extra=F(13)),
 au("migracao", "Cells born in the <b>crypt</b> differentiate as they migrate {{c1::<b>up the villus</b>}}, except Paneth cells, which stay at the crypt base", {1: Z}, B_,
    "Sentido da migração; Paneth fica na base", "14; Junqueira p. 316", "prova", "nenhum card nos acervos.", [1486608768857, 1486608763486], "Azul: esquema das linhagens do slide 14.", extra=F(14)),
 au("lgr5", "Active intestinal stem cells at the crypt base are identified by the marker {{c1::<b>Lgr5</b>}}", {1: Z}, B_,
    "Lgr5 marca a célula-tronco ativa", "15; Junqueira p. 320", "prova", "zero resultado para Lgr5 nos acervos.", [1482289502594, 1486608768857],
    "Azul: slide 15 'nicho de células-tronco intestinal' e slide 16.", extra="- Quiescent stem cells sit at position +4 (Bmi1)"),
 au("desenvolvimento-vilos", "In rodents, intestinal <b>villi</b> form before birth, whereas the {{c1::<b>crypts</b>}} develop only after birth", {1: R}, B_,
    "Vilos antes do nascimento, criptas depois", "11", "lateral", "nenhum card nos acervos; pesquisa da professora.", [1482289524478, 1482275085375],
    "Rosa: slides 11–12 (fase pré e pós-natal).", duplicacao_ok="resposta 'crypts' coincide com cards que definem a cripta; aqui é quando ela se forma (depois do nascimento), outro alvo"),
 # ---------- C. Células do epitélio intestinal (slides 17–19) ----------
 io("io-enterocito", 17, "Enterocytes (absorptive cells)", V, C_, "Enterócito na fotomicrografia", "Verde: item 4 do roteiro prático (identificar células absortivas).", ["Enterócitos"]),
 io("io-caliciforme", 17, "Goblet cell", V, C_, "Célula caliciforme na fotomicrografia", "Verde: item 4 do roteiro prático.", search=["Caliciformes"]),
 io("io-enteroendocrina", 17, "Enteroendocrine cell", Z, C_, "Célula enteroendócrina na fotomicrografia", "Azul: tipo celular do slide 17.", search=["Enteroendócrinas"]),
 io("io-paneth", 17, "Paneth cell", Z, C_, "Célula de Paneth na fotomicrografia", "Azul: tipo celular do slide 17.", ["Células de Paneth"]),
 hx("enterocito", 1702224810842, {1: Z, 3: V, 4: Z, 8: Z}, C_, "Enterócito: borda estriada, glicocálice, ampliação da superfície", 17,
    "Verde c3: borda em escova, primeira característica do slide 17; azuis: forma, glicocálice e quanto pregas, vilos e microvilos ampliam a área (slide 9)."),
 ak("lactase-borda", 1474164981030, {1: Z, 2: Z}, C_, "Lactase na borda em escova", 17, "Azuis: 'lactase e sacarase' no slide 17 (tag 3)."),
 ak("lactase-intolerancia", 1482355178454, {1: V}, C_, "Intolerância à lactose: lactase do enterócito", 17, "Verde: HY (1), clínica de encaixe direto com a enzima da borda em escova.", duplicacao_ok="resposta 'crypts' coincide com cards que definem a cripta; aqui é quando ela se forma (depois do nascimento), outro alvo"),
 au("vilina", "The actin core of each <b>microvillus</b> is bundled by the structural protein {{c1::<b>villin</b>}}", {1: R}, C_,
    "Vilina", "17; Junqueira p. 317", "lateral", "AnKing só classifica microvilos como microfilamentos.", [1468250042681, 1468250019616], "Rosa: 'proteína estrutural vilina' no slide 17."),
 hx("caliciforme", 1702225273915, {1: Z, 3: Z}, C_, "Caliciformes secretam mucinas", 17, "Azuis: célula caliciforme e mucina ('mucina 2' no slide 17). Substitui o autoral da v1."),
 ak("caliciformes-ileo", 1486608796832, {1: V}, C_, "Mais caliciformes no íleo", 17, "Verde: HY (1); 'note sua distribuição' no roteiro."),
 ak("paneth", 1486608768857, {1: V}, C_, "Paneth: defensinas e lisozima", 17, "Verde: célula que a aula destaca (antimicrobianos e nicho); tag 4, mantido verde por ser alvo central do slide 17."),
 hx("enteroendocrina-aberta", 1702228246553, {1: Z}, C_, "Enteroendócrina aberta tem quimiorreceptores", 17, "Azul: 'secreta hormônios, regula a digestão' no slide 17."),
 hx("enteroendocrina-efeitos", 1702220109656, {1: Z}, C_, "Hormônios enteroendócrinos: peristalse, secreção, saciedade", 17, "Azul: o que os hormônios regulam (Junqueira)."),
 sh(1790979867932, "azul", C_, "Microvilos são microfilamentos de actina", 18, "placeholder"),
 # ---------- D. Vilosidade e cripta em detalhe (slides 20–22) ----------
 hx("absorcao-carbo-prot", 1702224934484, {1: Z, 2: R}, D_, "Dissacaridases e peptidases no glicocálice", 19, "Azul: enzimas da borda em escova no esquema do slide 19 (Kierszenbaum); rosa: hidrólise e transporte ativo."),
 hx("absorcao-gordura", 1702225193904, {4: Z, 6: R, 9: Z}, D_, "Micelas, reesterificação e quilomícrons no enterócito", 19, "Azuis: sais biliares e micelas, formação de quilomícrons (slide 19); rosa: reesterificação no REL."),
 ak("lacteal", 1482115575316, {1: V}, D_, "Quilomícrons entram nos lácteos", 20, "Verde: capilar linfático central do vilo (slides 19–20), base da absorção de gordura; tag 4, mantido verde pelo valor duradouro."),
 hx("vilo-musculo", 1702228779127, {3: Z, 1: R}, D_, "Músculo liso do vilo vem da muscular da mucosa", 20, "Azul: 'glatte Muskelzelle' no eixo do vilo (slide 20); rosa: movimento do vilo."),
 hx("paneth-celula", 1702228171156, {1: Z, 3: Z, 8: Z}, D_, "Paneth: base da cripta, grânulos eosinófilos, imunidade inata e microambiente da cripta", 22,
    "Azuis: reconhecimento na lâmina do slide 22 (P) e papel no nicho (slide 17). Substitui uma reescrita e o autoral do nicho da v1."),
 # ---------- E. Segmentos do delgado e tecido linfoide (slides 23–28) ----------
 ak("brunner-distingue", 1486608774946, {1: V}, E_, "Glândulas de Brunner distinguem o duodeno", 23, "Verde: critério de diagnóstico do segmento (slides 23–24)."),
 ak("brunner-muco", 1482115268611, {1: V}, E_, "Brunner secreta muco", 24, "Verde: HY (2)."),
 ak("brunner-hco3", 1486608779650, {1: Z}, E_, "Secreção de Brunner tem bicarbonato", 24, "Azul: muco alcalino que neutraliza o quimo (Junqueira).", extra='<img src="e4793eaf6f95edad5055c9014b757e35.png">',
    correcao="Extra do AnKing dizia que as glândulas de Brunner secretam CCK e secretina; frase retirada da cópia."),
 dict(key="duodeno-he", kind="text", src=1668632250119, origin="LLU", identificacao=True, flags={1: Z}, bloco=E_, alvo="Reconhecer duodeno em HE", evid="Slide 24", motivo="Azul: estudo complementar do roteiro (duodeno e íleo)."),
 dict(key="delgado-he", kind="text", src=1668633014837, origin="LLU", identificacao=True, flags={1: Z}, bloco=E_, alvo="Reconhecer intestino delgado (jejuno) em HE", evid="Slide 25",
      motivo="Azul: jejuno é a lâmina do roteiro prático (LV 485)."),
 au("vilos-forma", "<b>Villi</b> are leaf-shaped in the {{c1::<b>duodenum</b>}} and become finger-shaped toward the ileum", {1: R}, E_,
    "Forma dos vilos por segmento", "23; Junqueira p. 317", "lateral", "nenhum card nos acervos.", [1486608782562, 1486608796832], "Rosa: legenda do slide 23.", duplicacao_ok="mesma palavra-resposta (duodeno) de outro card, pergunta diferente: aqui é a forma do vilo"),
 io("io-placas-peyer", 26, "Peyer patches (ileum)", V, E_, "Placas de Peyer na lâmina de íleo", "Verde: critério de diagnóstico do íleo, na lâmina da aula.", ["placas de Peyer"]),
 io("io-muscular-mucosa", 26, "Muscularis mucosae", Z, E_, "Muscular da mucosa na lâmina de íleo", "Azul: rótulo do slide 26.", ["muscular da mucosa"]),
 ak("peyer-ileo", 1486608789738, {1: V}, E_, "Placas de Peyer distinguem o íleo", 26, "Verde: completa a tríade duodeno (Brunner), jejuno (pregas), íleo (Peyer)."),
 ak("peyer-local", 1486831445995, {1: V, 2: V}, E_, "Placas de Peyer: lâmina própria e submucosa do íleo", 26, "Verdes: HY (1)."),
 dict(key="ileo-he", kind="text", src=1668632387853, origin="LLU", identificacao=True, flags={1: Z}, bloco=E_, alvo="Reconhecer íleo em HE", evid="Slide 26", motivo="Azul: estudo complementar do roteiro."),
 ak("celulas-m", 1486831448616, {1: V}, E_, "Células M nas placas de Peyer", 27, "Verde: HY (1); epitélio associado ao folículo, slide 27."),
 ak("iga", 1486831451445, {1: Z}, E_, "Plasmócitos de IgA na lâmina própria", 28, "Azul: slides 27–28 (centro germinativo com células produtoras de IgA); tag 3."),
 hx("iga-transcitose", 1702139120831, {3: Z, 4: Z}, E_, "IgA atravessa o epitélio ligada ao componente secretor", 28, "Azuis: vigilância imune do slide 28 (IgA para o lúmen)."),
 # ---------- F. Intestino grosso (slides 29–33) ----------
 ak("grosso-criptas", 1486608800197, {1: Z}, F_, "Intestino grosso tem criptas", 29, "Azul: 'no intestino grosso: identificar as criptas' (roteiro, item 5)."),
 hx("grosso-mucosa", 1702231576196, {1: V, 3: R}, F_, "Grosso sem vilos nem pregas; haustros", 29, "Verde: critério central para diferenciar delgado e grosso na lâmina; rosa: haustros."),
 ak("grosso-caliciformes", 1486608813182, {1: V}, F_, "Abundância de caliciformes no grosso", 31, "Verde: HY (2); característica que o roteiro manda observar."),
 dict(key="colon-he", kind="text", src=1668633106589, origin="LLU", identificacao=True, flags={1: Z}, bloco=F_, alvo="Reconhecer colo em HE", evid="Slide 31", motivo="Azul: lâmina do roteiro prático (LV 484)."),
 dict(key="delgado-colon-he", kind="text", src=1668632756215, origin="LLU", identificacao=True, flags={1: Z}, bloco=F_, alvo="Diferenciar delgado e colo lado a lado", evid="Slide 31",
      motivo="Azul: 'entender as características do intestino grosso' (objetivo 9)."),
 hx("grosso-regioes", 1702231182251, {1: Z}, F_, "Grosso forma as fezes do material não digerido", 29, "Azul: função que explica a mucosa sem vilos e rica em muco."),
 hx("grosso-lamina-propria", 1702234152170, {1: Z, 3: R, 4: R}, F_, "Nódulos linfoides na lâmina própria do grosso; apêndice como MALT", 30,
    "Azul: nódulos das lâminas dos slides 29, 30 e 33; rosas: por que há tanto MALT e o apêndice."),
 hx("grosso-glandulas", 1702233842140, {2: Z, 4: Z, 5: R}, F_, "Glândulas do grosso: caliciformes e colonócitos; caliciformes aumentam até o reto", 31,
    "Azuis: células da glândula do colo (slide 31) e gradiente de caliciformes; rosa: microvilos irregulares do colonócito."),
 hx("tenias", 1702234271737, {3: Z}, F_, "Tênias do colo: camada longitudinal externa em três faixas", 33, "Azul: muscular do grosso na lâmina do slide 33."),
 au("dcs", "In the colon, which lacks Paneth cells, the stem cell niche is supported by {{c1::<b>deep crypt secretory</b>}} cells", {1: R}, F_,
    "Células secretoras profundas da cripta", "32", "lateral", "nenhum card nos acervos; artigo de 2023.", [1486608768857, 1486608763486], "Rosa: slide 32, pesquisa recente.", duplicacao_ok="resposta 'deep crypt secretory' contém 'crypt'; alvo próprio: células que fazem o nicho no colo, sem Paneth"),
]
CARDS = [c for c in CARDS if c.get("motivo") != "placeholder"]

EXCLUIDOS = [
 (1702228317349, "Histology células M: AnKing 1486831448616 preferido"), (1500056732694, "IgA contra Giardia: microbiologia"), (1482115579210, "Quilomícrons e ducto torácico: P2/AN07"),

 (1556166448314, "MCAT vilos cobertos por microvilos: redundante com AnKing 1486608754106"), (1668633375606, "LLU junção ileocecal: lâmina não mostrada na aula"),
 (1482359431570, "Doença celíaca: atrofia de vilos — doença não ensinada"), (1482359449381, "Doença celíaca: hiperplasia de criptas — idem"),
 (1468250042681, "Microvilos são microfilamentos: citoesqueleto geral (UC01/02)"), (1482115490061, "Tripsinogênio e enteropeptidase: P2"), (1482115562039, "Micelas: P2"),
]
FORA_DO_RECORTE = [
 "Transportadores da absorção (SGLT1, carreadores de peptídeos, slide 19): fisiologia da P2",
 "Motilidade e trânsito (slides 3–4): esquema das camadas já coberto na BT03; fisiologia em FI08/FI09",
 "Marcadores além de Lgr5 (Ascl2, Olfm4, Tert, Hopx), vias Wnt/BMP/Notch (slides 10, 15, 32)",
 "Recirculação de linfócitos e detalhes da imunidade de mucosa (slides 27–28)",
 "Ilustrações e capa do livro (slides 5, 34, 35)",
]

# F-20261003-CLAUDE-14: notas longas do Histology recortadas em cards de uma frase
from nebli.hx_cortes import recortar
from hx_cortes import CORTES
CARDS = recortar(CARDS, CORTES)

# F-20261003-CLAUDE-15: figura de livro/AnKing e explicação curta no verso
from nebli.ilustrar import ilustrar, anotar
from imagens import IMAGENS, SEM_IMAGEM
from notas import NOTAS
CARDS = anotar(ilustrar(CARDS, IMAGENS, SEM_IMAGEM), NOTAS)
