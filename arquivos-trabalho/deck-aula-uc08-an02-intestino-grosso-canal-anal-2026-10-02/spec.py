# Especificação curada — Intestino grosso e canal anal (UC08 P1, Anatomia, Profa. Patricia Castelucci; PDF de 27 páginas, 2 lâminas por página).
# Feita em 02/10/2026 a partir de planejamento.json (escrito antes). Ordem = slides; "Slide N" = página N do PDF.
RUN_ID = "uc08-an02-20261002a"
SHORT = "an02"
LESSON = "2026-uc08-anatomia-02-intestino-grosso-canal-anal"
DECK = "NEBLI::UC08::P1::Anatomia::Intestino grosso e canal anal"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261002-CLAUDE-10) + PLANO-GERACAO-ANO, 02/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step por texto e sinônimos (busca/anking.txt, 18 consultas em 02/10); Referências Externas "
         "(Dorian, BlueLink, AnatoKing, MCAT, Histology, Dope) pelos mesmos alvos (busca/ext.txt, 13 consultas): ")
NETTER = dict(pdf="fontes/netter-pranchas.pdf", clip=(15, 55, 625, 785), tag="netter375")


def ak(key, src, flags, bloco, alvo, slide, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)


def bl(key, src, nome, cor, bloco, alvo, slide, motivo, remarks=""):
    return dict(key=key, kind="bluelink", src=src, flags={1: cor}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo,
                remarks=f"<b>{nome}</b>" + (f"<br>{remarks}" if remarks else ""))


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def io(key, page, half, name, cor, bloco, alvo, motivo, lines=(), rects=(), remarks="", mask_rects=(), slide=None, **src):
    return dict(key=key, kind="slideio", page=page, half=half, lines=list(lines), rects=list(rects), mask_rects=list(mask_rects), name=name,
                remarks=remarks, flags={1: cor}, bloco=bloco, alvo=alvo, evid=f"Slide {slide or page}", motivo=motivo, aponta="estrutura", **src)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_ = "A-partes", "B-caracteristicas", "C-ceco-apendice", "D-clinica", "E-reto", "F-canal-anal"
RP = "Azul: item do roteiro prático, na figura da própria aula."
CARDS = [
 # ---------- A. Partes e mobilidade (slide 2) ----------
 bl("ceco-bl", 1586747232247, "Cecum", V, A_, "Ceco na peça", 2, "Verde: primeira parte do intestino grosso, base do apêndice e da valva ileocecal."),
 bl("colo-ascendente-bl", 1586747232231, "Ascending colon", V, A_, "Colo ascendente na peça", 2, "Verde: parte do colo."),
 bl("colo-transverso-bl", 1586747232218, "Transverse colon", V, A_, "Colo transverso na peça", 2, "Verde: parte do colo."),
 bl("colo-descendente-bl", 1586747301304, "Descending colon", V, A_, "Colo descendente na peça", 2, "Verde: parte do colo."),
 bl("colo-sigmoide-bl", 1586747301336, "Sigmoid colon", V, A_, "Colo sigmoide na peça", 2, "Verde: parte do colo, sede do vólvulo do caso."),
 bl("reto-bl", 1586747301349, "Rectum", V, A_, "Reto na peça", 2, "Verde: parte terminal."),
 au("mobilidade", "The {{c1::<b>transverse</b>}} and {{c1::<b>sigmoid</b>}} colon are the <b>mobile</b> parts of the colon, each suspended by a mesocolon", {1: V}, A_,
    "Partes móveis do colo", "2; exercício 1.1; Moore pp. 750–752", "central",
    "AnatoKing 1546961507420 põe as duas listas (intra e retroperitoneal) sob um só cloze; AnKing só tem SAID PUCKER (AN13).", [1482289579274, 1482022140828],
    "Verde: resposta do exercício 1.1 e razão anatômica do vólvulo do caso.",
    duplicacao_ok="cobra a mobilidade (por que torcem); as oclusões só identificam os segmentos"),
 au("fixos", "The <b>ascending</b> and <b>descending</b> colon are secondarily {{c1::<b>retroperitoneal</b>::peritoneal relation}}", {1: Z}, A_,
    "Partes fixas do colo", "2; exercício 1.1; Moore pp. 750–752", "prova", "mesma busca do card de mobilidade.", [1482289579274, 1486605746677],
    "Azul: complemento do anterior.", extra="- Fixed to the posterior abdominal wall<br>- The cecum, transverse and sigmoid colon are intraperitoneal"),
 # ---------- B. Características externas (slides 3–5) ----------
 dict(key="tres-caracteristicas", kind="text", src=1527678503720, origin="Dorian", flags={1: V, 2: V, 3: V}, bloco=B_,
      text=("Three external features distinguish the <b>large intestine</b> from the small intestine<br><br>"
            "<div>- {{c1::<b>haustra</b> (sacculations)}}</div><div>- {{c2::<b>omental (epiploic) appendices</b>}}</div><div>- {{c3::<b>taeniae coli</b>}}</div>"),
      extra="- The <b>rectum</b> has none of them", alvo="Três características que diferenciam o grosso do delgado", evid="Slide 3; exercício 1.2",
      motivo="Verdes: resposta do exercício 1.2, critério para reconhecer o colo em cirurgia e imagem."),
 io("io-flexura-direita", 3, "top", "Right colic (hepatic) flexure", Z, B_, "Flexura cólica direita", "Azul: rótulo do slide 3.", ["Flexura cólica direita"]),
 io("io-flexura-esquerda", 3, "top", "Left colic (splenic) flexure", Z, B_, "Flexura cólica esquerda", "Azul: rótulo do slide 3.", ["Flexura cólica", "esquerda"]),
 io("io-haustros", 3, "top", "Haustra (sacculations)", Z, B_, "Haustros na prancha", RP, ["Haustros ou", "saculações"]),
 io("io-corpos-adiposos", 3, "top", "Omental (epiploic) appendices", Z, B_, "Corpos adiposos na prancha", RP, ["Corpos adiposos", "ou", "apêndices", "epiplóicos"]),
 io("io-tenias", 3, "top", "Taeniae coli", Z, B_, "Tênias na prancha", RP, ["tênias"]),
 io("io-apendice", 3, "top", "Vermiform appendix", V, B_, "Apêndice vermiforme na prancha", "Verde: estrutura do roteiro com maior peso clínico.", ["Apêndice", "vermiforme"]),
 io("io-saculacoes-peca", 3, "bottom", "Haustra (sacculations)", R, B_, "Saculações na peça", "Rosa: segundo reconhecimento, na peça.", ["Saculações", "(Hautros)"]),
 au("apendices-gordura", "The <b>omental (epiploic) appendices</b> of the colon are small pouches of peritoneum filled with {{c1::<b>fat</b>}}", {1: Z}, B_,
    "Apêndices omentais são bolsas de peritônio com gordura", "3; slide 4 (peça); Moore p. 742; canal Dr Mike", "prova", "Dorian e AnKing só citam o nome na lista das três características.",
    [1482022140828, 1486608782562], "Azul: rótulo 'corpos adiposos ou apêndices epiploicos' do slide 3 e título do slide 4; define o que a oclusão só aponta."),
 io("io-tenia-livre-peca", 5, "bottom", "Free taenia", Z, B_, "Tênia livre na peça", "Azul: a atividade prática pede a tênia livre com alfinete.", ["Tênia livre"]),
 # ---------- D1. Caso do vólvulo, divertículos (slides 6–7) ----------
 io("io-regiao-ileocecal-peca", 6, "top", "Ileocecal region", Z, C_, "Região ileocecal na peça", "Azul: a atividade prática pede a região ileocecal com alfinete.", ["Região íleocecal"]),
 ak("volvulo", 1482289579274, {1: Z}, D_, "Vólvulo = torção em torno do mesentério", "6", "Azul: definição do caso clínico do slide 6."),
 ak("volvulo-sigmoide", 1482289603147, {1: Z, 2: R}, D_, "Vólvulo de sigmoide no idoso", "6", "c1 azul (segmento do caso); c2 rosa (faixa etária)."),
 ak("diverticulos-falsos", 1482886610798, {1: V}, D_, "Divertículos do colo são falsos", "7", "Verde: HY (2) do único alvo do quadro 'Divertículos'."),
 ak("diverticulos-vasos-retos", 1482886631055, {1: V, 2: Z}, D_, "Divertículos surgem onde os vasos retos perfuram a muscular", "7",
    "c1 verde: HY (2), relação anatômica mostrada na figura do slide; c2 azul."),
 # ---------- Relações (slides 8–10) ----------
 au("flexura-baco", "The <b>left colic flexure</b> lies higher than the right one and is related to the {{c1::<b>spleen</b>}}", {1: Z}, A_,
    "Flexura esquerda e baço", "8; atividade prática II; Moore p. 750", "prova", "AnKing só cita a flexura esplênica como zona de fronteira vascular (AN07).",
    [1486605773525, 1472321238353], "Azul: par cobrado na atividade prática (flexura esplênica ↔ baço).", extra="- The right colic flexure lies under the <b>liver</b>"),
 au("sigmoide-ureter", "Which structure lies behind the apex of the <b>sigmoid mesocolon</b>, on the left common iliac vessels?<br><br>{{c1::Left ureter}}", {1: R}, A_,
    "Ureter esquerdo atrás do mesocolo sigmoide", "10; Moore p. 752", "lateral", "nenhum card nos acervos.", [1486605738754, 1543169132935],
    "Rosa: relação do slide 'Colo sigmoide: vasos e ureter', prioridade baixa."),
 # ---------- C. Região ileocecal, ceco e apêndice (slides 10–15) ----------
 io("io-ileo-distal", 10, "bottom", "Terminal ileum", R, C_, "Íleo distal na prancha", "Rosa: rótulo de apoio.", ["Íleo distal"]),
 io("io-ceco", 10, "bottom", "Cecum", Z, C_, "Ceco na prancha", RP, ["ceco"]),
 dict(au("io-papila-ileal-texto", "The projection of the terminal ileum into the cecum, closing the ileal orifice with two lips, is the {{c1::ileal papilla}}", {1: Z}, C_,
    "Papila ileal", "11; Moore; Netter", "prova",
    "AnKing sem a papila; AnatoKing tem a valva ileocecal em foto com o nome na legenda (entrega a resposta); BlueLink sem a região.",
    [1482289634672, 1482978805608], "Azul: item do roteiro prático. Substitui a oclusão que mascarava o título da prancha (Davi: 'cloze zuado', 03/10).",
    extra='Also called the ileocecal valve; its upper (ileocolic) and lower (ileocecal) lips meet at the ileal orifice'), ),
 io("io-labio-ileocolico", 11, "top", "Ileocolic lip (upper lip of the ileal orifice)", Z, C_, "Lábio ileocólico", RP, ["Lábio íleocólico"]),
 io("io-labio-ileocecal", 11, "top", "Ileocecal lip (lower lip of the ileal orifice)", Z, C_, "Lábio ileocecal", RP, ["Lábio íleocecal"]),
 io("io-ostio-ileal", 11, "top", "Ileal orifice", Z, C_, "Óstio ileal", "Azul: componente da valva ileocecal (exercício 1.3).", ["Óstio ileal"]),
 io("io-ostio-apendice", 11, "top", "Orifice of the vermiform appendix", R, C_, "Óstio do apêndice", "Rosa: rótulo do slide 11.", ["Óstio do apêndice"]),
 ak("apendice-linfoide-hx", 1701983228303, {1: Z}, C_, "Apêndice: tecido linfoide (MALT)", "11", "Azul: caracterização pedida no exercício 1.3. F-18: substitui o autoral; recorte do Histology/Junqueira (a nova busca achou o alvo no livro em cards).", origin="Histology", text="The mucosa of the <b>vermiform appendix</b> is almost completely filled with {{c1::lymphoid}} tissue", extra=""),
 ak("apendicite-mcburney", 1482361859692, {1: V, 2: Z}, C_, "Dor da apendicite migra para o ponto de McBurney", "14", "c1 verde: HY (1), o ponto é o título do slide 14; c2 azul."),
 au("apendice-retrocecal", "What is the most common position of the <b>vermiform appendix</b>?<br><br>{{c1::Retrocecal}}", {1: Z}, C_,
    "Posição mais comum do apêndice", "15; Moore p. 743", "prova", "AnKing 1521075752706 cobra a consequência, não a posição.", [1482289505425, 1482276032069],
    "Azul: número em destaque no slide 15 (64%).", extra="- <b>Pelvic</b> is the second most common position"),
 ak("retrocecal-dor", 1521075752706, {1: R}, C_, "Apêndice retrocecal não desloca a dor para McBurney", "15", "Rosa: consequência clínica da variação (tag 5)."),
 io("io-tenia-livre", 15, "bottom", "Free taenia", Z, B_, "Tênia livre no ceco", RP, ["Tênia livre"]),
 io("io-tenia-mesocolica", 15, "bottom", "Mesocolic taenia", Z, B_, "Tênia mesocólica no ceco", RP, ["Tênia mesocólica"]),
 io("io-tenia-omental", 15, "bottom", "Omental taenia", Z, B_, "Tênia omental no ceco", RP, ["Tênia", "omental"]),
 ak("tenias-apendice", 1521485187473, {1: V}, B_, "Tênias convergem na base do apêndice", "15", "Verde: HY (1); 'início das tênias ↔ apêndice' na atividade prática."),
 # ---------- Tênias (slide 16) ----------
 ak("tenias-hx", 1702234271737, {1: V}, B_, "Tênias = músculo longitudinal", "16", "Verde: definição pedida no exercício 3 e na atividade prática (tênia livre ↔ m. longitudinal). F-18: substitui o autoral; recorte do Histology/Junqueira (a nova busca achou o alvo no livro em cards).", origin="Histology", text="In the colon, the outer {{c1::longitudinal}} muscle layer is gathered into three bands, the <b>taeniae coli</b>", extra=""),
 # ---------- D2. Doença inflamatória e Chagas (slides 17–18) ----------
 ak("crohn", 1482374205403, {1: V, 2: Z}, D_, "Crohn: lesões salteadas, da boca ao ânus", "17", "c1 verde: HY (1), contraste escrito no slide; c2 azul."),
 ak("retocolite", 1482374199572, {1: V, 2: Z}, D_, "Colite ulcerativa: sempre o reto, contínua até o ceco", "17", "c1 verde: HY (1); c2 azul."),
 sh(1790972065836, "azul", D_, "Chagas: megacólon e megaesôfago", 18, "Já vivo na AN01 (cópia do AnKing 1403046909909); aqui é o megacólon do slide 18."),
 sh(1790972065961, "azul", D_, "Chagas: destruição dos neurônios do plexo mioentérico", 18, "Já vivo na AN01; o slide 18 repete o mecanismo para o colo."),
 # ---------- E. Reto (slides 19–21) ----------
 io("io-flexura-sacral", 19, "top", "Sacral flexure of the rectum", Z, E_, "Flexura sacral", RP, ["Flexura", "sacral do", "reto"]),
 io("io-flexura-anorretal", 19, "top", "Anorectal flexure (puborectalis muscle)", Z, E_, "Flexura anorretal", RP, ["Flexura anorretal", "(m. puborretal)"]),
 au("puborretal", "The {{c1::<b>puborectalis</b>}} muscle forms a sling behind the anorectal junction that maintains the <b>anorectal flexure</b>", {1: V}, E_,
    "Puborretal mantém a flexura anorretal", "19; atividade prática II; Moore p. 921", "central", "AnKing 1705597547475 só cobra a disfunção; BlueLink só identifica o músculo.",
    [1482022129277, 1482022126258], "Verde: mecanismo de continência escrito em destaque no slide 19.", extra="- Its tone keeps <b>fecal continence</b><br>- It relaxes during defecation, straightening the junction<br><br><img src=\"nebli-uc08-an02-p19t.png\" width=\"420\">",
    duplicacao_ok="cobra a função do músculo; a oclusão reconhece a flexura na prancha"),
 ak("dissinergia", 1705597547475, {1: R}, E_, "Defecação dissinérgica: puborretal não relaxa", "19", "Rosa: clínica do relaxamento descrito no slide, prioridade baixa."),
 io("io-escavacao-retovesical", 20, "top", "Rectovesical pouch", Z, E_, "Escavação retovesical", "Azul: relação anterior do reto no homem (exercício 2.1).", ["Escavação retovesical"]),
 io("io-prega-transversa", 20, "top", "Transverse fold of the rectum", Z, E_, "Prega transversa", "Azul: rótulo dos slides 20 e 21.", ["Prega transversa"]),
 io("io-ampola-retal", 20, "top", "Rectal ampulla", V, E_, "Ampola retal", "Verde: roteiro prático e atividade prática; reservatório das fezes.", ["Ampola retal"]),
 io("io-escavacao-retouterina", 20, "bottom", "Rectouterine pouch (of Douglas)", Z, E_, "Escavação retouterina", "Azul: atividade prática (espaço entre reto e útero).",
    ["Escavação reto", "uterina"]),
 io("io-escavacao-vesicouterina", 20, "bottom", "Vesicouterine pouch", R, E_, "Escavação vesicouterina", "Rosa: rótulo do slide, fora do reto.", ["Escavação", "vesicouterina"]),
 dict(key="douglas", kind="text", src=1527676305786, origin="Dorian", flags={1: Z}, bloco=E_,
      text="The <b>{{c1::rectouterine pouch}}</b> (of Douglas) is the <b>deepest peritoneal space</b> in the female, where fluid and pelvic abscesses collect",
      extra="- Lies between the <b>rectum</b> and the <b>uterus</b>", alvo="Escavação retouterina é o ponto mais baixo do peritônio feminino", evid="Slide 20",
      motivo="Azul: por que a relação importa."),
 au("reto-prostata", "In the male, the <b>rectum</b> is related anteriorly to the bladder, the seminal glands and the {{c1::<b>prostate</b>}}", {1: Z}, E_,
    "Relações anteriores do reto no homem", "20; exercício 2.1; Moore p. 923", "prova", "AnKing só cita o toque retal em urologia.", [1486605738754, 1472321238353],
    "Azul: resposta do exercício 2.1.", extra="- In the female, the vagina and the <b>rectouterine pouch</b>"),
 au("pregas-tres", "The <b>rectum</b> has {{c1::<b>three</b>}} transverse folds (superior, middle and inferior) that help support the fecal mass", {1: Z}, E_,
    "Três pregas transversas do reto", "21; Moore p. 921", "prova", "BlueLink só identifica as pregas; AnKing sem card.", [1482022140828, 1482289518360],
    "Azul: as três pregas estão nomeadas no slide 21."),
 au("ampola-funcao", "The dilated lower part of the <b>rectum</b>, which stores feces until defecation, is the {{c1::<b>rectal ampulla</b>}}", {1: Z}, E_,
    "Ampola retal armazena as fezes", "21; Moore p. 921", "prova", "nenhum card nos acervos define a ampola.", [1482022140828, 1482022134697],
    "Azul: o que a ampola faz; pedido de Davi por mais texto sobre a região retoanal.", duplicacao_ok="cobra a função; a oclusão só identifica a ampola na prancha"),
 au("reto-vagina", "In the female, the <b>rectum</b> is related anteriorly to the {{c1::<b>vagina</b>}}, with the rectouterine pouch above it", {1: Z}, E_,
    "Relação anterior do reto na mulher", "21; exercício 2.1; Moore p. 923", "prova", "AnKing só tem a escavação retouterina.", [1486605738754, 1472321238353],
    "Azul: completa a resposta do exercício 2.1."),
 bl("pregas-transversas-bl", 1586798253347, "Transverse folds of the rectum", R, E_, "Pregas transversas na peça", 21, "Rosa: reconhecimento na peça.",
    "Three folds (superior, middle, inferior). The rectum is about 15 cm long and has no taeniae or omental appendices."),
 # ---------- F. Canal anal (slides 22–25) ----------
 io("io-coluna-anal", 22, "top", "Anal column", Z, F_, "Coluna anal", RP, ["Coluna anal", "(ramos a. v. retais", "superiores", "Plexo arterial/venoso)"]),
 io("io-juncao-anorretal", 22, "top", "Anorectal junction (upper ends of the anal columns)", Z, F_, "Junção anorretal", "Azul: 'linha anorretal' do exercício 2.2.",
    ["junção", "anorretal", "(porção superior das"]),
 io("io-seio-anal", 22, "top", "Anal sinus (releases mucus)", Z, F_, "Seio anal", RP, ["Seio anal", "(liberam muco)", "(espaço entre as"]),
 io("io-linha-pectinada", 22, "top", "Pectinate (dentate) line", V, F_, "Linha pectinada", "Verde: marco central do canal anal (exercício 2.2).",
    ["Linha pectinada divide:", "(acima revestimento endodérmico do inferior", "revestimento ectodérmico)"]),
 io("io-linha-branca", 22, "top", "White (anocutaneous) line", R, F_, "Linha branca", "Rosa: rótulo do slide 22.", ["Linha Branca", "(anocutânea)"]),
 io("io-plexo-interno", 22, "top", "Internal rectal venous plexus", Z, F_, "Plexo venoso interno", "Azul: base das hemorroidas internas.", ["Plexo venoso interno"]),
 io("io-plexo-externo", 22, "top", "External rectal venous plexus", Z, F_, "Plexo venoso externo", "Azul: base das hemorroidas externas.", ["Plexo venoso externo"]),
 io("io-netter-valvula-anal", 3, "full", "Anal valve", Z, F_, "Válvula anal (Netter)", "Azul: item do roteiro prático que o slide não rotula; prancha 375 do Netter.",
    ["Anal valve"], slide=22, **NETTER),
 io("io-netter-colunas", 3, "full", "Anal columns (of Morgagni)", R, F_, "Colunas anais (Netter)", "Rosa: segundo reconhecimento, com rótulos em inglês.",
    ["Anal columns (Morgagni’s)"], slide=22, **NETTER),
 io("io-netter-pectinada", 3, "full", "Pectinate (dentate) line", Z, F_, "Linha pectinada (Netter)", "Azul: 'base da coluna anal ↔ linha pectinada' na atividade prática.",
    ["Pectinate (dentate) line"], slide=22, **NETTER),
 io("io-netter-esfincter-interno", 3, "full", "Internal anal sphincter", Z, F_, "Esfíncter interno (Netter)", "Azul: reconhecimento em corte.",
    ["Internal sphincter muscle"], slide=22, **NETTER),
 au("juncao-anorretal", "The upper ends of the <b>anal columns</b> mark the {{c1::<b>anorectal</b>}} junction, where the rectum becomes the anal canal", {1: Z}, F_,
    "Linha (junção) anorretal", "22; exercício 2.2; Moore p. 983", "prova", "nenhum card nos acervos define a junção anorretal.", [1486771325323, 1482255441749],
    "Azul: definição pedida no exercício 2.2.", duplicacao_ok="cobra a definição; a oclusão reconhece na prancha"),
 au("valvulas-anais", "The lower ends of the <b>anal columns</b> are joined by the anal {{c1::<b>valves</b>}}, whose free edges form the pectinate line", {1: Z}, F_,
    "Válvulas anais desenham a linha pectinada", "22; atividade prática II; Moore p. 984", "prova", "acervos só identificam a linha pectinada.", [1486771325323, 1482255441749],
    "Azul: 'base da coluna anal ↔ linha pectinada' na atividade prática."),
 au("seios-muco", "What do the <b>anal sinuses</b> release when they are compressed by feces?<br><br>{{c1::Mucus}}", {1: Z}, F_,
    "Seios anais liberam muco", "22; Moore p. 984", "prova", "nenhum card nos acervos.", [1486605738754, 1543169132935], "Azul: '(liberam muco)' no rótulo do slide 22."),
 ak("pectinada-embrio", 1486771325323, {1: V}, F_, "Linha pectinada: endoderma encontra ectoderma", "22", "Verde: HY (2), está escrito no slide 22."),
 ak("arteria-acima", 1486771343412, {1: V}, F_, "Acima: a. retal superior", "23", "Verde: HY (1), 'diferem em drenagem a, v e linfático'."),
 ak("veia-acima", 1486771359798, {1: V}, F_, "Acima: drenagem portal", "23", "Verde: HY (1)."),
 ak("linfa-acima", 1486771351448, {1: V}, F_, "Acima: linfonodos ilíacos internos", "23", "Verde: HY (2), texto do slide 23."),
 ak("inervacao-acima", 1486771354809, {1: V}, F_, "Acima: inervação visceral", "23", "Verde: HY (2), 'Inervação: visceral'."),
 ak("arteria-abaixo", 1486771372707, {1: V}, F_, "Abaixo: a. retal inferior", "23", "Verde: HY (1)."),
 ak("veia-abaixo", 1486771390217, {1: V}, F_, "Abaixo: drenagem sistêmica", "23", "Verde: HY (1)."),
 ak("linfa-abaixo", 1486771380083, {1: V}, F_, "Abaixo: linfonodos inguinais superficiais", "23", "Verde: HY (2), texto do slide 23."),
 ak("inervacao-abaixo", 1486771382893, {1: Z, 2: Z}, F_, "Abaixo: inervação somática (n. pudendo)", "23", "Azuis: 'inervação parietal (abaixo)'; tag 4."),
 ak("hemorroida-plexo", 1521768231806, {1: V}, F_, "Hemorroida = distensão do plexo arteriovenoso anal", "24", "Verde: HY (1)."),
 ak("hemorroida-interna", 1486771334237, {1: V}, F_, "Hemorroida interna: acima da linha pectinada", "24", "Verde: HY (1), figura do slide 24."),
 ak("hemorroida-indolor", 1486771357327, {1: V}, F_, "Hemorroida interna não dói", "24", "Verde: HY (1), consequência da inervação visceral."),
 ak("hemorroida-externa", 1486771365392, {1: V}, F_, "Hemorroida externa: abaixo da linha pectinada", "24", "Verde: HY (1)."),
 ak("hemorroida-dolorosa", 1486771387643, {1: V}, F_, "Hemorroida externa dói", "24", "Verde: HY (1), consequência da inervação somática."),
 ak("fissura-anal", 1486771396183, {1: V, 2: Z}, F_, "Fissura anal: abaixo da linha pectinada", "24", "c1 verde: HY (2); c2 azul (nome da lesão). Aplicação direta da linha pectinada (região de inervação somática, dolorosa)."),
 ak("esfincter-interno-hx", 1702234616745, {1: V}, F_, "Esfíncter interno: camada circular (lisa)", "25", "Verde: distinção que explica continência; par esfíncter interno ↔ m. circular liso na atividade prática. F-18: substitui o autoral; recorte do Histology/Junqueira (a nova busca achou o alvo no livro em cards).", origin="Histology", text="The {{c1::circular}} muscle layer of the rectum forms the <b>internal anal sphincter</b> near the anus", extra=""),
 ak("esfincter-externo-hx", 1702234616745, {1: V}, F_, "Esfíncter externo: músculo voluntário", "25", "Verde: par do anterior. F-18: substitui o autoral; recorte do Histology/Junqueira (a nova busca achou o alvo no livro em cards).", origin="Histology", text="The <b>external anal sphincter</b>, which controls defecation, is made of {{c1::voluntary}} muscle", extra=""),
 io("io-puborretal", 25, "top", "Puborectalis (part of the levator ani)", Z, F_, "Puborretal no corte", RP, ["m. Puborretal", "- m. levantador", "do anus"]),
 io("io-esfincter-externo", 25, "top", "External anal sphincter", Z, F_, "Esfíncter externo no corte", RP, ["Esfíncter", "externo do", "anus"]),
 bl("esfincter-externo-bl", 1586802823301, "External anal sphincter", R, F_, "Esfíncter externo na peça", 25, "Rosa: reconhecimento na peça."),
 bl("esfincter-interno-bl", 1586802823311, "Internal anal sphincter", R, F_, "Esfíncter interno na peça", 25, "Rosa: reconhecimento na peça."),
]

EXCLUIDOS = [
 (1546961507420, "AnatoKing intra × retroperitoneal: duas listas sob um só cloze"), (1486605111359, "SAID PUCKER: AN13"),
 (1486771399646, "Fissura anal: dor e sangue no papel (apresentação clínica)"), (1349477488508, "Prancha Dope da mucosa do intestino grosso: Dope só sem alternativa; coberto por oclusões do slide"),
 (1440926575393, "Dope McBurney: foto de baixa resolução"), (1542147194347, "AnatoKing tênias: oclusão do slide preferida"),
 (1542147221081, "AnatoKing ceco: BlueLink e oclusão do slide preferidos"), (1482289608337, "Vólvulo de ceco em jovens: fora do caso"),
 (1482289593587, "Vólvulo → obstrução e infarto: desfecho clínico"), (1482886634613, "Diverticulose (definição): redundante com os dois cards do slide 7"),
 (1482886658640, "Tríade da diverticulite: clínica"), (1482374194811, "Colite ulcerativa contínua com reto: redundante com 1482374199572"),
 (1482374210189, "Crohn poupa o reto: redundante"), (1482374188222, "Colite: só mucosa e submucosa: patologia"), (1482374191830, "Crohn transmural: patologia"),
 (1486771346144, "A. retal superior é ramo da mesentérica inferior: AN07"), (1486771374861, "A. retal inferior é ramo da pudenda interna: AN07"),
 (1527685886290, "Dorian hemorroida interna → VMI: redundante com AnKing"),
 (1486767254523, "Intestino posterior (embriologia): sem objetivo na aula"), (1536510324583, "Ceco é o local mais comum de perfuração: clínica lateral"),
 (1586747444820, "BlueLink tênias: oclusão do slide cobre"), (1586747444813, "BlueLink haustros: oclusão do slide cobre"),
 (1586747444805, "BlueLink apêndices omentais: oclusão do slide cobre"), (1586747385579, "BlueLink apêndice: oclusão do slide cobre"),
 (1586798253344, "BlueLink ampola retal: oclusão do slide cobre"), (1586800163966, "BlueLink puborretal: oclusão do slide cobre"),
 (1586802765780, "BlueLink linha pectinada: oclusões do slide e do Netter cobrem"),
]
FORA_DO_RECORTE = [
 "Irrigação e drenagem do colo (AN07); peritônio, omento maior e compartimentos (AN13)",
 "Funções do canal anal (retenção, expulsão) e reflexo da defecação: FI09",
 "Fisiopatologia e tratamento de Crohn, colite ulcerativa, hemorroidas e fístula anal",
 "Nove regiões abdominais (slides 7–8): mesma lâmina, já coberta por 6 oclusões na AN01",
 "Atlas Pearson e Prometheus com rótulos dentro da figura (slides 8–10, 13)",
]

# F-20261003-CLAUDE-15: figura de livro/AnKing e explicação curta no verso
from nebli.ilustrar import ilustrar, anotar
from imagens import IMAGENS, SEM_IMAGEM, LIVRO
from notas import NOTAS
MEDIA.update(LIVRO)
CARDS = anotar(ilustrar(CARDS, IMAGENS, SEM_IMAGEM), NOTAS)
