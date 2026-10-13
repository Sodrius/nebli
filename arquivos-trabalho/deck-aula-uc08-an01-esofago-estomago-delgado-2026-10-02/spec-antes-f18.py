# Especificação curada — Esôfago, estômago e intestino delgado (UC08 P1, Anatomia, Profa. Patricia Castelucci; PDF de 24 páginas, 2 lâminas por página).
# Refeita do zero em 02/10/2026 (o deck de 29/09 foi apagado por Davi). Ordem = sequência dos slides; "Slide N" = página N do PDF.
RUN_ID = "uc08-an01-20261002a"
SHORT = "an01"
LESSON = "2026-uc08-anatomia-01-esofago-estomago-delgado"
DECK = "NEBLI::UC08::P1::Anatomia::Esôfago, estômago e intestino delgado"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261002-CLAUDE-08) + EXECUCAO-DECK-AULA §9, 02/10/2026"

MEDIA = {
    "nebli-uc08-an01-s07-juncao.jpeg": "fontes/p07_img2.jpeg",
    "nebli-uc08-an01-s08-mittal.jpeg": "fontes/p08_img0.jpeg",
    "nebli-uc08-an01-s10-moore.jpeg": "fontes/p10_img4.jpeg",
    "nebli-uc08-an01-s11-aberto.jpeg": "fontes/p11_img2.jpeg",
    "nebli-uc08-an01-s19-quadrantes.jpeg": "fontes/p19_img0.jpeg",
    "nebli-uc08-an01-s21-jejuno.jpeg": "fontes/p21_img1.jpeg",
    "nebli-uc08-an01-s21-ileo.jpeg": "fontes/p21_img2.jpeg",
}
IMG = lambda f, w=480: f'<img src="{f}" width="{w}">'
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt e busca/complemento.txt, 46 consultas em 02/10); Referências Externas "
         "(Dope, Dorian, BlueLink, AnatoKing, MCAT, Histology) pelos mesmos alvos (busca/ext.txt, 27 consultas): ")
DUO = "Duodenum ≈ 25 cm, C-shaped around the head of the pancreas. Parts: superior (L1), descending (L1–L3), horizontal (L3), ascending (L3–L2)."
JI = "Jejunum ≈ 2/5 and ileum ≈ 3/5 of the small intestine beyond the duodenum (together 6–7 m)."


def ak(key, src, flags, bloco, alvo, slide, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)


# Nome da estrutura marcada em cada oclusão BlueLink: vai em negrito no início de Remarks (só no verso), para o verso dizer em texto
# o que a máscara mostra e para o gerador do Tab conhecer o alvo (o rótulo só existe nos pixels da imagem).
NOME = {"esofago-toracico-bl": "Thoracic esophagus", "esofago-abdominal-bl": "Abdominal esophagus", "piloro-bl": "Pylorus",
        "esfincter-pilorico-bl": "Pyloric sphincter", "curvatura-menor-bl": "Lesser curvature", "curvatura-maior-bl": "Greater curvature",
        "pregas-gastricas-bl": "Gastric folds (rugae)", "duodeno-superior-bl": "Superior (1st) part of the duodenum",
        "duodeno-descendente-bl": "Descending (2nd) part of the duodenum", "duodeno-horizontal-bl": "Inferior (3rd) part of the duodenum",
        "duodeno-ascendente-bl": "Ascending (4th) part of the duodenum", "papila-maior-bl": "Major duodenal papilla",
        "papila-menor-bl": "Minor duodenal papilla", "mesenterio-bl": "Mesentery", "jejuno-bl": "Jejunum", "ileo-bl": "Ileum",
        "juncao-ileocecal-bl": "Ileocecal junction", "pregas-circulares-bl": "Circular folds"}


def bl(key, src, cor, bloco, alvo, slide, motivo, remarks=""):
    remarks = f"<b>{NOME[key]}</b>" + (f"<br>{remarks}" if remarks else "")
    return dict(key=key, kind="bluelink", src=src, flags={1: cor}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, remarks=remarks)


def atk(key, src, cor, bloco, alvo, slide, motivo, **kw):
    return dict(key=key, kind="anatoking", src=src, flags={1: cor}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", imagem="sem figura: fato simples", duplicacao_ok=""):
    return dict(duplicacao_ok=duplicacao_ok, key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, imagem=imagem)


A_, B_, C_, D_, E_, F_, G_, H_, I_ = ("A-esofago", "B-constricoes", "C-hiato-juncao", "D-estomago", "E-relacoes", "F-duodeno", "G-treitz",
                                      "H-jejuno-ileo", "I-meckel")
CARDS = [
 # ---------- A. Esôfago: tubo, músculo, esfíncter superior, porções (slides 3–5) ----------
 au("esofago-comprimento", "The <b>esophagus</b> is a muscular tube about {{c1::25}} cm long that runs from the <b>pharynx</b> to the <b>stomach</b>", {1: R}, A_,
    "Esôfago: tubo de ~25 cm da faringe ao estômago", "3; canais Dr Mike e Armando (25 cm)", "lateral",
    "nenhum card com o comprimento do esôfago (consulta 'esophag* length/25 cm' só devolve colecistite).", [1482289518360, 1482022116564],
    "Rosa: número do slide 3, pouco ganho a longo prazo."),
 ak("terco-superior-estriado", 1482022116564, {1: V}, A_, "Terço superior: músculo estriado", "4", "Verde: HY (2) e base da deglutição voluntária × peristalse."),
 ak("dois-tercos-liso", 1482022121968, {1: V}, A_, "Dois terços inferiores: músculo liso", "4", "Verde: HY (2); par do anterior."),
 ak("ees-ar", 1482022126258, {1: Z}, A_, "Esfíncter superior impede entrada de ar", "4", "Azul: função do esfíncter citado no objetivo 4."),
 ak("zenker", 1482203693998, {1: V, 2: Z}, A_, "Disfunção do cricofaríngeo → divertículo de Zenker", "4; canal Armando (Zenker na anatomia clínica do esôfago)",
    "c1 verde: HY (1), clínica de encaixe direto com o cricofaríngeo do slide; c2 azul (mesma relação no sentido inverso)."),
 ak("esofago-traqueia", 1521071357761, {1: Z}, A_, "Esôfago posterior à traqueia", "5; exercício 1 (relações)", "Azul: relação reconstruível."),
 bl("esofago-toracico-bl", 1586748271983, Z, A_, "Identificar a porção torácica", "5", "Azul: identificação do roteiro prático.",
    "The thoracic part is the longest: it descends in the posterior mediastinum behind the trachea, aortic arch, left main bronchus and heart."),
 bl("esofago-abdominal-bl", 1586748493975, V, A_, "Identificar a porção abdominal", "5", "Verde: representante da junção esofagogástrica na peça.",
    "The abdominal part is the shortest (~1.25 cm): from the esophageal hiatus (T10) to the cardiac orifice of the stomach."),
 # ---------- B. Constrições (slide 5; caso do slide 9) ----------
 dict(key="constricoes", kind="text", src=1527616316221, origin="Dorian", flags={1: V, 2: V, 3: Z}, bloco=B_,
      text=('What are the four locations where the <b>esophagus</b> can be <b>constricted</b>?<br><br>'
            '<div>1) origin at the pharynx (cricopharyngeus)</div><div>2) posterior to the {{c1::<b>arch of aorta</b>::vessel}}</div>'
            '<div>3) compression by the {{c3::<b>left main bronchus</b>}}</div><div>4) at the {{c2::<b>esophageal hiatus</b> (<b>T10</b>)}}</div>'),
      extra=('- 2 and 3 together form the <b>bronchoaortic</b> constriction<br>- Foreign bodies lodge and endoscopes meet resistance at these points'
             '<br><br><img src="paste-779055527886849.jpg">'),
      alvo="Três constrições da aula (cervical, broncoaórtica, diafragmática)", evid="Slide 5; exercício 1; caso do slide 9",
      motivo="c1 e c2 verdes: constrições são objetivo da aula e pergunta do caso clínico; c3 azul (brônquio compõe a broncoaórtica)."),
 ak("perfuracao-endoscopia", 1557057012444, {1: Z}, B_, "Perfuração esofágica mais comum é instrumental", "9; exercício 1",
    "Azul: a razão clínica que a professora dá para saber as constrições.",
    extra="- Presents with <b>chest / back pain</b><br>- The instrument meets most resistance at the esophageal <b>constrictions</b>"),
 # ---------- C. Hiato, junção esofagogástrica, Chagas (slides 6–8) ----------
 ak("hiato-t10", 1474511934874, {1: V, 2: Z, 3: Z}, C_, "Hiato esofágico em T10 (esôfago e vagos)", "6", "c1 verde: HY (2), nível do hiato no slide 7; c2 e c3 azuis."),
 ak("forame-vci-t8", 1474511925850, {1: V, 2: Z}, C_, "Forame da veia cava em T8", "6", "c1 verde: HY (2), abertura rotulada no slide; c2 azul."),
 ak("hiato-aortico-t12", 1474511944771, {1: V, 2: Z}, C_, "Hiato aórtico em T12", "6", "c1 verde: HY (2); c2 azul. Ducto torácico e ázigo não são da aula.", uncloze=[3, 4]),
 au("pilar-direito", "The <b>esophageal hiatus</b> is formed by the {{c1::<b>right crus</b>}} of the diaphragm, which acts as an <b>external</b> lower esophageal sphincter", {1: Z}, C_,
    "Pilar direito do diafragma = esfíncter inferior externo", "8; Moore p. 719; canal Dr Mike", "prova",
    "AnKing só tem os níveis vertebrais e o tônus do EEI; nenhum card sobre o pilar direito.", [1474511934874, 1482022129277],
    "Azul: figura de Mittal no slide 8 (EEI interno × externo).", extra=IMG("nebli-uc08-an01-s08-mittal.jpeg"), imagem="slide 8 (Mittal 2013)"),
 ak("eei-refluxo", 1482022129277, {1: V}, C_, "Esfíncter inferior impede refluxo", "7", "Verde: constrição do objetivo 4 e base do refluxo."),
 au("lig-frenoesofagico", "Which ligament attaches the <b>esophagus</b> to the margins of the <b>esophageal hiatus</b>?<br><br>{{c1::Phrenoesophageal ligament}}", {1: Z}, C_,
    "Ligamento frenoesofágico", "7; Moore p. 715", "prova", "'phrenoesophageal' só aparece no verso de cards de hérnia de hiato; sem rótulo nos acervos anatômicos.",
    [1486605738754, 1486605789747], "Azul: estrutura rotulada duas vezes no slide 7 e na figura do slide 8.",
    extra=IMG("nebli-uc08-an01-s07-juncao.jpeg"), imagem="slide 7 (Netter)", duplicacao_ok="texto cobra a função (fixar o esôfago ao hiato); a oclusão rosa só reconhece na prancha"),
 ak("barrett-linha-z", 1482255441749, {1: V}, C_, "Linha Z (junção escamocolunar)", "7; canal Dr Mike (Barrett)", "Verde: HY (1) sobre a linha Z rotulada no slide."),
 ak("chagas-megaesofago", 1403046909909, {1: Z, 3: Z}, C_, "Chagas: megaesôfago e megacólon", "7", "Azul: megaesôfago chagásico é a peça do slide 7; megacólon volta em AN02.", uncloze=[2]),
 au("chagas-neuronios", "<b>Megaesophagus</b> in <b>Chagas</b> disease is caused by destruction of neurons in the {{c1::<b>myenteric (Auerbach)</b>}} plexus of the esophageal wall", {1: Z}, C_,
    "Chagas: perda dos neurônios entéricos (plexo mioentérico)", "7", "prova", "AnKing 1482203793099 trata da acalasia primária (autoimune); nenhum card liga Chagas à perda neuronal.",
    [1482203793099, 1482203795669], "Azul: é o título do slide 7."),
 ak("acalasia-chagas", 1482203795669, {1: V}, C_, "Acalasia secundária a Chagas", "7", "Verde: HY (1), consequência funcional da perda neuronal mostrada no slide."),
 # ---------- D. Estômago: partes, curvaturas, interior, músculos (slides 9–13) ----------
 au("incisura-cardica", "What is the name of the notch between the left border of the <b>esophagus</b> and the <b>fundus</b> of the stomach?<br><br>{{c1::Cardiac notch}}", {1: Z}, D_,
    "Incisura cárdica", "10; Moore p. 719", "prova", "'cardiac notch' só devolve a incisura cardíaca do pulmão esquerdo.", [1543169132935, 1486605738754],
    "Azul: acidente do contorno rotulado nos slides 10 e 11.", extra=IMG("nebli-uc08-an01-s10-moore.jpeg"), imagem="slide 10 (Moore)", duplicacao_ok="texto cobra a definição (entre esôfago e fundo); a oclusão reconhece na prancha"),
 au("incisura-angular", "The {{c1::<b>angular incisure</b>}} on the <b>lesser curvature</b> marks the junction of the <b>body</b> and the <b>pyloric part</b> of the stomach", {1: V}, D_,
    "Incisura angular separa corpo e parte pilórica", "10; Moore p. 722", "central", "AnatoKing 1562607277712 só identifica na figura; nenhum card dá o significado do marco.",
    [1482022140828, 1482022147543], "Verde: marco que delimita as porções, pedido no exercício 8 e no caso do slide 13.", duplicacao_ok="texto cobra o significado do marco (limite corpo × parte pilórica); a oclusão reconhece"),
 atk("porcao-pilorica-ak", 1542147011020, Z, D_, "Parte pilórica", "10", "Azul: termo agregador do roteiro (antro + canal + piloro)."),
 bl("piloro-bl", 1586748600192, V, D_, "Piloro", "11", "Verde: constrição listada no objetivo 4."),
 bl("esfincter-pilorico-bl", 1586748600203, Z, D_, "Esfíncter pilórico", "11", "Azul: anel de músculo circular na peça."),
 bl("curvatura-menor-bl", 1586748539629, V, D_, "Curvatura menor", "10", "Verde: borda fundamental, exercício 8.", "Short, concave right border; the angular incisure lies on it."),
 bl("curvatura-maior-bl", 1586748539613, V, D_, "Curvatura maior", "10", "Verde: borda fundamental, exercício 8.", "Long, convex left border."),
 bl("pregas-gastricas-bl", 1586748639710, Z, D_, "Pregas gástricas", "11", "Azul: identificação do roteiro."),
 au("canal-gastrico", "During swallowing, longitudinal folds along the <b>lesser curvature</b> form the {{c1::<b>gastric canal</b>}}, which carries liquids toward the pylorus", {1: Z}, D_,
    "Canal gástrico", "11; Moore p. 723", "prova", "zero resultado para 'gastric canal/Magenstrasse' em todos os acervos.", [1482022134697, 1482022140828],
    "Azul: estrutura do roteiro prático (item 3).", extra=IMG("nebli-uc08-an01-s11-aberto.jpeg", 440), imagem="slide 11 (Netter)", duplicacao_ok="texto cobra a formação e a função do canal; a oclusão reconhece (atividade prática)"),
 au("camada-obliqua", "In addition to circular and longitudinal layers, the <b>stomach</b> wall has an <b>innermost</b> {{c1::<b>oblique</b>}} muscle layer", {1: V}, D_,
    "Terceira camada muscular (oblíqua)", "12; canal Dr Mike", "central", "AnKing sem resultado para 'stomach oblique'; Histology 1702221209267 junta sete clozes da parede.",
    [1482022116564, 1482022121968], "Verde: particularidade duradoura do estômago, slide 'Músculos – estômago'."),
 ak("ulcera-curvatura-menor", 1482276032069, {1: V}, D_, "Úlcera gástrica na curvatura menor", "13", "Verde: HY (1), a única clínica do caso que usa o mapa gástrico."),
 # ---------- E. Relações do estômago (exercício 9) ----------
 au("estomago-anterior", "The <b>anterior</b> surface of the <b>stomach</b> is related to the diaphragm, the anterior abdominal wall and the {{c1::<b>left lobe</b>}} of the liver", {1: Z}, E_,
    "Relações anteriores do estômago", "13; exercício 9; Moore p. 724", "prova", "nenhum card sobre as relações das faces do estômago; AnKing só tem os ligamentos (AN13).",
    [1486605738754, 1472321238353], "Azul: resposta do exercício 9."),
 au("estomago-posterior", "The <b>posterior</b> surface of the <b>stomach</b> forms most of the anterior wall of the {{c1::<b>omental bursa (lesser sac)</b>}}", {1: Z}, E_,
    "Face posterior = parede anterior da bolsa omental", "13; exercício 9; Moore p. 725", "prova", "AnKing e Dorian só citam a bolsa omental pelos ligamentos e forame.",
    [1486605746677, 1486605727740], "Azul: resposta do exercício 9.", duplicacao_ok="relação da face posterior; o card Dorian cobra a artéria lesada"),
 dict(key="ulcera-posterior-esplenica", kind="text", src=1527677561378, origin="Dorian", flags={1: R}, bloco=E_,
      text='A <b>posterior gastric ulcer</b> may erode into the <b>lesser sac</b>, damaging the {{c1::<b>splenic</b>}} artery',
      extra="- The splenic artery runs along the upper border of the pancreas, in the stomach bed",
      alvo="Úlcera posterior → bolsa omental e a. esplênica", evid="Slide 13; exercício 9", motivo="Rosa: aplicação da relação posterior, prioridade baixa."),
 # ---------- F. Duodeno (slides 14–17) ----------
 bl("duodeno-superior-bl", 1586796524406, V, F_, "1ª porção (superior)", "15", "Verde: porção do bulbo.", DUO),
 bl("duodeno-descendente-bl", 1586796524397, V, F_, "2ª porção (descendente)", "15", "Verde: porção da papila maior.", DUO),
 bl("duodeno-horizontal-bl", 1586796524416, Z, F_, "3ª porção (horizontal)", "15", "Azul: identificação do roteiro.", DUO),
 bl("duodeno-ascendente-bl", 1586796524426, Z, F_, "4ª porção (ascendente)", "15", "Azul: identificação do roteiro.", DUO),
 au("duodeno-niveis", "The <b>superior (1st)</b> part of the duodenum lies at vertebral level {{c1::<b>L1</b>}}, and the <b>horizontal (3rd)</b> part crosses {{c2::<b>L3</b>}}", {1: Z, 2: R}, F_,
    "Níveis vertebrais do duodeno", "15; Moore p. 733", "prova", "zero resultado para níveis vertebrais do duodeno (L1/L3/transpyloric).", [1474511934874, 1474511925850],
    "c1 azul e c2 rosa: níveis escritos em cada rótulo do slide 15, sem valor duradouro próprio."),
 ak("pancreas-2a-porcao", 1521170266917, {1: V}, F_, "Cabeça do pâncreas na concavidade do duodeno", "15; exercício 5", "Verde: HY (2), relação central do duodeno (forma de C)."),
 ak("sindrome-ams", 1486767231234, {1: R}, F_, "3ª porção entre a mesentérica superior e a aorta", "15; exercício 5", "Rosa: relação útil, síndrome rara (tag 5)."),
 dict(key="segunda-porcao-ampola", kind="text", src=1527681160735, origin="Dorian", flags={1: V}, bloco=F_,
      text=('<div>The <b>main pancreatic duct</b> joins with the <b>common bile duct</b> and enters the {{c1::<b>2nd</b>}} part of the duodenum '
            'through the <b>ampulla of Vater</b> (controlled by the <b>sphincter of Oddi</b>)</div>'),
      extra="- The ampulla opens at the <b>major duodenal papilla</b>",
      alvo="Papila maior na 2ª porção", evid="Slide 16; exercícios 4 e 6", motivo="Verde: é o título do slide 16."),
 ak("coledoco-pancreatico", 1486777651171, {1: V, 2: V}, F_, "Colédoco e ducto pancreático principal formam a ampola", "16", "Verdes: HY (2), base da patologia biliopancreática."),
 bl("papila-maior-bl", 1586796571786, V, F_, "Papila maior na peça", "17", "Verde: estrutura central do roteiro (item 5).",
    "On the posteromedial wall of the descending (2nd) part; opening of the hepatopancreatic ampulla."),
 ak("ducto-principal-papila-maior", 1486596689685, {1: Z}, F_, "Ducto principal → papila maior", "16", "Azul: dedutível do anterior."),
 ak("esfincter-oddi", 1486777654795, {1: Z}, F_, "Esfíncter de Oddi", "16", "Azul: 'Ampola de Vater – Esfíncter de Oddi' no slide; função pedida no exercício 4."),
 ak("calculo-ampola", 1486777658795, {1: R}, F_, "Cálculo na ampola bloqueia os dois ductos", "16; exercício 4", "Rosa: consequência clínica da confluência, fora da prova de anatomia."),
 bl("papila-menor-bl", 1586796571780, Z, F_, "Papila menor", "16", "Azul: rotulada no slide 16."),
 ak("ducto-acessorio-papila-menor", 1486596693761, {1: R}, F_, "Ducto acessório → papila menor", "16", "Rosa: detalhe (tag 5) da figura."),
 # ---------- G. Flexura duodenojejunal e ligamento de Treitz (slides 15–16) ----------
 au("treitz-estrutura", "The <b>duodenojejunal flexure</b> is supported by the {{c1::<b>suspensory muscle</b>}} of the duodenum (ligament of Treitz)", {1: Z}, G_,
    "Ligamento de Treitz sustenta a flexura", "15; exercício 7; Moore p. 733", "prova",
    "AnatoKing 1558905073563 recusado (cloze composto com marcação quebrada); AnKing só tem o marco clínico.", [1543169132935, 1537213179739],
    "Azul: estrutura do roteiro (item 4); a importância fica no card seguinte.",
    extra='- Skeletal muscle from the <b>diaphragm</b> plus smooth muscle from the <b>duodenum</b><br><br><img src="477f80c20c979758e5f388cc1e5639dc.webp">',
    imagem="AnKing 477f80c20c979758e5f388cc1e5639dc.webp (nota 1543169132935)", duplicacao_ok="texto cobra o que sustenta a flexura; a oclusão reconhece na prancha"),
 ak("treitz-marco", 1543169132935, {1: V}, G_, "Treitz separa trato digestivo alto e baixo", "15; exercício 7", "Verde: a 'importância' pedida no exercício 7.",
    extra=('- Useful for separating <b>upper GI bleeds</b> (e.g., hemat<u>emesis</u>, melena) vs. <b>lower GI bleeds</b> (e.g., hematochezia)'
           '<br><br><img src="477f80c20c979758e5f388cc1e5639dc.webp">')),
 # ---------- H. Jejuno e íleo (slides 17–21, caso do slide 23) ----------
 au("jejuno-fracao", "The <b>jejunum</b> makes up the proximal {{c1::<b>two-fifths</b>}} of the small intestine beyond the duodenum", {1: Z}, H_,
    "Jejuno 2/5, íleo 3/5", "17; Moore p. 737; canal Dr Mike", "prova", "Dope 1349477488509 só cita a proporção no comentário da prancha.", [1482022116564, 1482022121968],
    "Azul: proporção escrita no slide 17.", extra="- The <b>ileum</b> makes up the distal three-fifths"),
 au("mesenterio", "The {{c1::<b>mesentery</b>}} is the fold of <b>peritoneum</b> that attaches the <b>jejunum</b> and <b>ileum</b> to the posterior abdominal wall", {1: Z}, H_,
    "Mesentério", "17; Moore p. 737", "prova", "AnKing só usa 'mesentery' em volvo e ligamentos; nenhum card define a prega.", [1482289579274, 1486605789747],
    "Azul: definição do slide 17; peritônio é aprofundado em AN13.", duplicacao_ok="texto define a prega; o BlueLink reconhece na peça"),
 bl("mesenterio-bl", 1586747095757, Z, H_, "Identificar o mesentério", "17", "Azul: roteiro prático (itens 6 e 7)."),
 bl("jejuno-bl", 1586747095770, Z, H_, "Identificar o jejuno", "18", "Azul: roteiro prático.", JI),
 bl("ileo-bl", 1586747095740, Z, H_, "Identificar o íleo", "18", "Azul: roteiro prático.", JI),
 bl("juncao-ileocecal-bl", 1586747158541, Z, H_, "Junção ileocecal", "18", "Azul: constrição do objetivo 4, término do íleo; retorna em AN02.",
    "Where the terminal ileum opens into the cecum (cadaver, anterior view of the abdominal cavity); it marks the end of the small intestine."),
 au("quadrantes", "Most of the <b>jejunum</b> lies in the {{c1::<b>left upper</b>}} quadrant, while most of the <b>ileum</b> lies in the {{c1::<b>right lower</b>}} quadrant", {1: Z}, H_,
    "Posição do jejuno e do íleo", "19; Moore p. 737", "prova", "nenhum acervo cobra os quadrantes do jejuno e do íleo.", [1482022140828, 1482022147543],
    "Azul: dois slides inteiros sobre a posição.", extra=IMG("nebli-uc08-an01-s19-quadrantes.jpeg", 420), imagem="slide 19 (Netter)"),
 dict(key="vasos-retos-jejuno", kind="text", src=1461962333435, origin="Dope", sem_alternativa="card de texto (não é prancha): AnKing, BlueLink, Dorian e MCAT não comparam jejuno e íleo por este critério (busca/ext.txt)", flags={1: V}, bloco=H_,
      text="The {{c1::jejunum}} has few, large arterial arcades and long vasa recta (compared with the ileum)",
      extra=('- Jejunum is a longer word and has longer arteries<br>- Ileum has many short arcades and short vasa recta<br><br>'
             + IMG("nebli-uc08-an01-s21-jejuno.jpeg", 260) + " " + IMG("nebli-uc08-an01-s21-ileo.jpeg", 260)),
      alvo="Vasos retos longos e poucas arcadas = jejuno", evid="Slide 20; exercícios 11 e 12; caso do slide 23",
      motivo="Verde: critério que a professora cobra no caso de isquemia mesentérica."),
 dict(key="gordura-ileo", kind="text", src=1461962456152, origin="Dope", sem_alternativa="card de texto (não é prancha): AnKing, BlueLink, Dorian e MCAT não comparam jejuno e íleo por este critério (busca/ext.txt)", flags={1: Z}, bloco=H_, text="The {{c1::ileum}} has more mesenteric fat than the jejunum",
      extra="- In the ileum the fat reaches the bowel wall and hides the vessels", alvo="Mais gordura mesentérica no íleo", evid="Slide 21",
      motivo="Azul: critério secundário, visível nas peças do slide."),
 au("jejuno-parede", "Compared with the <b>ileum</b>, the <b>jejunum</b> has a {{c1::<b>thicker</b>::thicker / thinner}} wall and a larger caliber", {1: Z}, H_, "Parede e calibre do jejuno", "21; exercício 10",
    "prova", "Dope e AnKing só comparam vasos, gordura e pregas.", [1482022140828, 1482022147543], "Azul: linhas da tabela do slide 21."),
 ak("plicas-jejuno", 1486608782562, {1: Z}, H_, "Pregas circulares distinguem o jejuno", "21", "Azul: linha 'pregas circulares' da tabela."),
 bl("pregas-circulares-bl", 1586747113760, R, H_, "Pregas circulares na peça", "21", "Rosa: reconhecimento de apoio.",
    "Mucosal folds seen in an opened segment of jejunum (cadaver specimen); they are tall and numerous in the jejunum and sparse in the ileum."),
 # ---------- I. Divertículo do íleo (slide 22) ----------
 ak("meckel-vitelino", 1482289502594, {1: V}, I_, "Meckel = persistência do ducto vitelino", "22", "Verde: HY (1) do alvo do slide."),
 ak("meckel-mais-comum", 1482289505425, {1: V}, I_, "Meckel é a anomalia congênita mais comum do trato digestivo", "22", "Verde: HY (1) do alvo do slide."),
 ak("meckel-localizacao", 1482289520748, {1: Z}, I_, "Meckel no íleo, perto da valva ileocecal", "22", "Azul: localização anatômica ('divertículos do íleo')."),
 ak("meckel-ectopico", 1482289539018, {1: V, 2: Z}, I_, "Mucosa gástrica ectópica", "22", "c1 verde: HY (1), explica a úlcera da figura de Netter; c2 azul."),
]

# ---------- Oclusões feitas do próprio slide (F-20261002-CLAUDE-09): rótulos dos slides e itens do roteiro prático ----------
def io(key, page, half, name, cor, bloco, alvo, motivo, lines=(), rects=(), remarks="", mask_rects=()):
    return dict(key=key, kind="slideio", page=page, half=half, lines=list(lines), rects=list(rects), mask_rects=list(mask_rects), name=name, remarks=remarks, aponta="estrutura", flags={1: cor},
                bloco=bloco, alvo=alvo, evid=f"Slide {page}", motivo=motivo)


RP = "Azul: item do roteiro prático, na figura da própria aula."
CARDS += [
 io("io-cricofaringeo", 4, "bottom", "Cricopharyngeal part of the inferior pharyngeal constrictor (upper esophageal sphincter)", Z, A_,
    "Parte cricofaríngea na prancha da aula", "Azul: estrutura que forma o esfíncter superior, rotulada no slide 4.",
    ["Porção cricofaríngea", "do m. constritor inferior", "da faringe", "(esfíncter superior do esôfago)"]),
 io("io-musculo-circular", 4, "bottom", "Circular muscle layer of the esophagus (smooth muscle)", R, A_, "Camada circular na prancha", "Rosa: camada rotulada no slide 4; histologia em BT03.",
    ["M circular"]),
 io("io-esofago-cervical", 5, "top", "Cervical part of the esophagus", Z, A_, "Porção cervical na peça da aula", RP, ["Porção cervical"]),
 io("io-esofago-toracico", 5, "top", "Thoracic part of the esophagus", Z, A_, "Porção torácica na peça da aula", RP, ["Porção torácica"]),
 io("io-esofago-abdominal", 5, "top", "Abdominal part of the esophagus", Z, A_, "Porção abdominal na peça da aula", RP, ["Porção abdominal"]),
 io("io-constricao-cervical", 5, "bottom", "Cervical constriction (upper esophageal sphincter, at the cricoid)", Z, B_, "1ª constrição na prancha",
    "Azul: a atividade prática pede as três constrições pelo nome.", ["1. Constrição cervical", "(Esfíncter superior do", "esôfago - cricoide)"]),
 io("io-constricao-broncoaortica", 5, "bottom", "Bronchoaortic constriction", Z, B_, "2ª constrição na prancha",
    "Azul: a atividade prática pede as três constrições pelo nome.", ["2. Constrição", "bronco-aortica"]),
 io("io-constricao-diafragmatica", 5, "bottom", "Diaphragmatic constriction (lower esophageal sphincter)", Z, B_, "3ª constrição na prancha",
    "Azul: a atividade prática pede as três constrições pelo nome.", ["3. Constrição Diafragmática", "(Esfíncter inferior", "do esôfago)"]),
 io("io-hiato-esofagico", 6, "bottom", "Esophageal hiatus", Z, C_, "Hiato esofágico na prancha", "Azul: rótulo do slide 6.", ["Hiato esofágico"], mask_rects=[(128, 364, 424, 386)]),
 io("io-forame-vci", 6, "bottom", "Caval opening (foramen of the inferior vena cava)", Z, C_, "Forame da veia cava na prancha", "Azul: rótulo do slide 6.",
    ["Forâmen da", "veia cava inferior", "Forâmen (orifício) da"]),
 io("io-hiato-aortico", 6, "bottom", "Aortic hiatus", Z, C_, "Hiato aórtico na prancha", "Azul: rótulo do slide 6.", ["Hiato aórtico"]),
 io("io-lig-frenoesofagico", 7, "bottom", "Phrenoesophageal ligament", R, C_, "Ligamento frenoesofágico na prancha", "Rosa: reconhecimento de apoio ao card de texto.",
    ["Lig. Frênico esofágico", "(porção inferior)", "(porção superior)"]),
 io("io-linha-z", 7, "bottom", "Z line (junction of esophageal and gastric mucosa)", Z, C_, "Linha Z na prancha", "Azul: rótulo do slide 7.",
    ["Linha Z –", "(junção da", "mucosa", "do esôfago", "e do estômago", "gástrica)"]),
 io("io-cardia", 10, "top", "Cardia (surrounds the cardiac orifice)", V, D_, "Cárdia", "Verde: região gástrica do roteiro, do exercício 8 e da atividade prática.",
    ["Cárdia (circunda o óstio cárdico)"]),  # 03/10: só o rótulo da figura; a caixa de legenda fica coberta
 io("io-incisura-cardica", 10, "top", "Cardiac notch", Z, D_, "Incisura cárdica na prancha", "Azul: rótulo do slide 10.", ["Incisura cardíca"]),
 io("io-fundo", 10, "top", "Fundus of the stomach", V, D_, "Fundo", "Verde: região gástrica do roteiro.", ["Fundo"]),
 io("io-corpo", 10, "top", "Body of the stomach", V, D_, "Corpo", "Verde: região gástrica do roteiro.", ["Corpo"]),
 io("io-incisura-angular", 10, "top", "Angular incisure (between the body and the pyloric part)", Z, D_, "Incisura angular na prancha", "Azul: reconhecimento do marco.",
    ["Incisura angular"]),  # 03/10: idem
 io("io-antro", 10, "top", "Pyloric antrum", V, D_, "Antro pilórico", "Verde: região gástrica do roteiro.", ["Antro pilórico"]),
 io("io-piloro", 10, "top", "Pylorus", Z, D_, "Piloro na prancha", "Azul: constrição do objetivo 4, na figura da aula.", ["Piloro"]),
 io("io-curvatura-menor", 10, "top", "Lesser curvature", Z, D_, "Curvatura menor na prancha", RP, ["Curvat.", "menor"]),
 io("io-curvatura-maior", 10, "top", "Greater curvature", Z, D_, "Curvatura maior na prancha", RP, ["Curvatura", "maior"]),
 io("io-canal-pilorico", 11, "top", "Pyloric canal", Z, D_, "Canal pilórico na peça da aula", "Azul: subdivisão rotulada na peça.", ["Canal pilórico"]),
 io("io-canal-gastrico", 11, "bottom", "Gastric canal", Z, D_, "Canal gástrico no estômago aberto", "Azul: roteiro prático (item 3) e atividade prática.", ["Canal", "gástrico"]),
 io("io-pregas-gastricas", 11, "bottom", "Gastric folds (rugae)", Z, D_, "Pregas gástricas no estômago aberto", RP, ["Pegas", "gástricas"], mask_rects=[(174, 551, 262, 592)]),
 io("io-regiao-epigastrio", 14, "top", "Epigastric region", Z, E_, "Epigástrio", "Azul: mapa de localização mostrado duas vezes na aula (slides 14 e 18) e de novo em AN02.", ["Epigastrio"]),
 io("io-regiao-hipocondrio", 14, "top", "Right hypochondriac region (hypochondrium)", Z, E_, "Hipocôndrio", "Azul: mapa de localização mostrado duas vezes na aula (slides 14 e 18) e de novo em AN02.", ["Hipocondrio D"]),
 io("io-regiao-umbilical", 14, "top", "Umbilical region", Z, E_, "Região umbilical", "Azul: mapa de localização mostrado duas vezes na aula (slides 14 e 18) e de novo em AN02.", ["Região umbilical"]),
 io("io-regiao-lateral", 14, "top", "Right lateral (lumbar) region, the flank", Z, E_, "Região lateral (flanco)", "Azul: mapa de localização mostrado duas vezes na aula (slides 14 e 18) e de novo em AN02.", ["Região lateral D"]),
 io("io-regiao-inguinal", 14, "top", "Right inguinal (iliac) region", Z, E_, "Região inguinal (fossa ilíaca)", "Azul: mapa de localização mostrado duas vezes na aula (slides 14 e 18) e de novo em AN02.", ["Região Inguinal D"]),
 io("io-regiao-hipogastrio", 14, "top", "Hypogastric (pubic) region", Z, E_, "Hipogástrio", "Azul: mapa de localização mostrado duas vezes na aula (slides 14 e 18) e de novo em AN02.", ["Hipogástrio"]),
 io("io-duodeno-superior", 15, "top", "Superior (1st) part of the duodenum, at L1", Z, F_, "1ª porção na prancha da aula", RP, ["Porção superior (1ͣ) (L1)"]),
 io("io-duodeno-descendente", 15, "top", "Descending (2nd) part of the duodenum, L1–L3", Z, F_, "2ª porção na prancha da aula", RP, ["Porção", "Descendente", "(2ͣ) (L1-L3)"]),
 io("io-duodeno-horizontal", 15, "top", "Inferior (horizontal, 3rd) part of the duodenum, at L3", Z, F_, "3ª porção na prancha da aula", RP,
    ["Porção horizontal ou inferior, 3ª  (L3)"]),
 io("io-duodeno-ascendente", 15, "top", "Ascending (4th) part of the duodenum, L3–L2", Z, F_, "4ª porção na prancha da aula", RP, ["Porção ascendente , 4ª (L3-L2)"]),
 io("io-flexura-duodenojejunal", 15, "top", "Duodenojejunal flexure (held by the ligament of Treitz)", Z, G_, "Flexura duodenojejunal", "Azul: exercício 7.",
    ["Flexura duodeno jejunal", "(Ligamento suspensor o", "duodeno, Ligamento de Treitz)"]),
 io("io-lig-treitz", 15, "bottom", "Suspensory muscle of the duodenum (ligament of Treitz)", Z, G_, "Ligamento suspensor do duodeno", RP,
    ["Ligamento suspensor do", "duodeno, (Ligamento de Treitz) :", "fibras do m diafragma + m liso)", "Ligamento suspensor do duodeno - Ligamento de Treitz"]),
 io("io-coledoco", 16, "bottom", "Common bile duct (carries bile)", Z, F_, "Colédoco", RP, ["Colédoco ( transporta bile)"]),
 io("io-papila-maior", 17, "top", "Major duodenal papilla", Z, F_, "Papila maior na figura da aula", "Azul: roteiro prático (item 5) e atividade prática.",
    ["Papila maior", "do duodeno"], mask_rects=[(122, 58, 294, 84), (160, 303, 365, 330)]),
 io("io-papila-menor", 16, "bottom", "Minor duodenal papilla", Z, F_, "Papila menor na figura da aula", "Azul: rótulo do slide 16.", rects=[(98, 480, 144, 513)]),
 io("io-ducto-pancreatico", 16, "bottom", "Main pancreatic duct", Z, F_, "Ducto pancreático na figura da aula", RP, rects=[(196, 586, 254, 622)]),
 io("io-aa-jejunais", 20, "top", "Jejunal arteries", R, H_, "Artérias jejunais", "Rosa: rótulo do slide 20; irrigação é de AN07.", ["a. jejunais"]),
 io("io-aa-ileais", 20, "top", "Ileal arteries", R, H_, "Artérias ileais", "Rosa: rótulo do slide 20; irrigação é de AN07.", ["a. ileais"]),
 io("io-vasos-retos-longos", 20, "bottom", "Long vasa recta (jejunum)", Z, H_, "Vasos retos longos na peça", "Azul: roteiro prático (item 6) e atividade prática.",
    ["Vasos retos longos - jejuno"]),
 io("io-vasos-retos-curtos", 21, "top", "Short vasa recta (ileum)", Z, H_, "Vasos retos curtos na peça", RP, ["Vasos retos", "curtos", "- íleo"]),
]

EXCLUIDOS = [
] + [(n, "AnatoKing de identificação: trocado em 02/10 pela oclusão do próprio slide (F-20261002-CLAUDE-09)") for n in
     (1548957822372, 1542146989512, 1542147001992, 1542147006993, 1562607277712, 1548959124455, 1542147025458)] + [
 (1482022131650, "VIP relaxa o esfíncter inferior: fisiologia (FI08)"), (1482022134697, "Relaxamento receptivo: FI08"),
 (1482022140828, "Estômago orad: motilidade (FI08/FI09)"), (1482022147543, "Estômago caudad: motilidade"),
 (1556159233701, "MCAT controle por terços do esôfago: redundante com os dois AnKing dos terços"),
 (1509815200893, "Qual protozoose causa acalasia: redundante com 1482203795669"), (1482203793099, "Acalasia primária autoimune: doença fora da aula"),
 (1486831395587, "Hérnia de hiato por deslizamento: doença não ensinada"), (1486831402485, "Hérnia de hiato por deslizamento: idem"),
 (1482203821480, "DRGE: doença não ensinada"), (1472321246872, "Átrio esquerdo comprime o esôfago: relação que o slide não mostra"),
 (1482276026606, "AINE como causa de úlcera: etiologia, o caso é ponte anatômica"), (1482276071848, "Pneumoperitônio na úlcera duodenal anterior: doença duodenal"),
 (1482276034749, "Úlcera da curvatura menor → a. gástrica esquerda: AN07"), (1486767364212, "Gastroepiploicas: AN07"), (1486767367274, "Gástricas: AN07"),
 (1486605738754, "Ligamento gastro-hepático: AN13 (peritônio, P2)"), (1486605763821, "Ligamento gastrocólico: AN13"), (1486605773525, "Ligamento gastroesplênico: AN13"),
 (1486605111359, "SAID PUCKER (retroperitoneais): AN13"), (1349477488593, "Prancha Dope da musculatura do esôfago: trocada pela oclusão do slide 4 (Dope só sem alternativa, F-20261002-CLAUDE-10)"), (1349477488509, "Prancha Dope das arcadas: trocada pelas oclusões dos slides 20–21"),
 (1349477488608, "Prancha Dope do leito gástrico: substituída por dois cards de texto das relações"),
 (1482275004042, "Estenose hipertrófica do piloro (série): doença não ensinada"), (1510261416840, "H. pylori no antro: patologia"),
 (1482021846216, "CCK relaxa o esfíncter de Oddi: fisiologia da P2"), (1535752586086, "Sangramento acima de Treitz: mesma importância de 1543169132935"),
 (1537213179739, "Vômito bilioso distal a Treitz: clínica lateral"), (1486767163689, "Mesentérica superior irriga o intestino médio: AN07"),
 (1461962475986, "Dope pregas circulares jejuno > íleo: redundante com AnKing 1486608782562"), (1527683434688, "Dorian ducto acessório: redundante com AnKing"),
 (1486608796832, "Células caliciformes no íleo: BT04"), (1482289491610, "Meckel é divertículo verdadeiro (camadas): além do slide"),
 (1482289510964, "Regra dos 2: lista mnemônica"), (1482289546088, "Cintilografia no Meckel: diagnóstico"),
 (1558905073563, "AnatoKing Treitz: cloze composto quebrado"), (1542146962028, "AnatoKing pregas gástricas: BlueLink preferido"),
 (1542146968329, "AnatoKing curvatura maior: BlueLink preferido"), (1542146981325, "AnatoKing curvatura menor: BlueLink preferido"),
 (1542147060583, "AnatoKing porções do duodeno: BlueLink preferido"), (1542147117997, "AnatoKing papila maior: BlueLink preferido"),
 (1542146899031, "AnatoKing partes da faringe: faringe é contexto de origem do esôfago, aula de cabeça e pescoço"),
]
FORA_DO_RECORTE = [
 "Faringe e véu palatino (slides 3–4): origem do esôfago, sem objetivo na aula",
 "Nove regiões abdominais (slides 14 e 18): mapa de localização; só os quadrantes do jejuno e do íleo são cobrados",
 "Funções do estômago e do delgado (quimo, reservatório, digestão): fisiologia (FI08/FI09 e P2)",
 "Irrigação, drenagem e inervação: AN07 e AN14; ligamentos peritoneais e omentos: AN13",
 "Casos clínicos (tumor de esôfago, úlcera perfurada, isquemia mesentérica): ponte anatômica, sem diagnóstico ou tratamento",
 "Biografia de Treitz (slide 16)",
]

# F-20261003-CLAUDE-15: figura de livro/AnKing e explicação curta no verso
from nebli.ilustrar import ilustrar, anotar
from imagens import IMAGENS, SEM_IMAGEM, LIVRO
from notas import NOTAS
MEDIA.update(LIVRO)
CARDS = anotar(ilustrar(CARDS, IMAGENS, SEM_IMAGEM), NOTAS)
