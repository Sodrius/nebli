# FI08 v3 (run uc08-fi08-20260929a) — correção após F-C44: cobertura da aula inteira, irmãos AnKing
# preservados, autorais curtos no padrão AnKing com imagem AnKing, verde generoso nos fundamentos.
# Calibração: slide (6 lâminas) + Ninja Nerd "Enteric Nervous System" e "Smooth Muscle" + Medicosis
# "Smooth muscle MLCK/phosphatase" (legendas lidas) + OpenStax A&P 10.8/23.1 + AnKing Costanzo GI.
RUN_ID = "uc08-fi08-20260929a"
VERSION = "v3"
LESSON = "2026-uc08-fisiologia-08-motilidade-absorcao-intestinal-i"
DECK = "NEBLI::UC08::P1::Fisiologia::Motilidade e absorção intestinal I"
CRITERIOS = "README/CONTRATO/BANDEIRAS/ESTILO/TRADUCAO 29/09 + F-C43/F-C44 + respostas 23/09 (Q1 todo AnKing do assunto; Q5/Q6 vídeos+bibliografia; Q10 autoral curto)"

CR = '<span style="font-size: 10pt;"><em>{}</em></span>'
ESO = '<img src="17690823319c36bcd3d6b68a81dc0bf9.png" width="{w}">'
ENS = '<img src="54b501f67e312dbb191af3fb9c8c5806.png" width="500">'
LAYERS = ('<img src="f7114acc00def107eaa664fd4737aeac.jpg" width="700"><br>' + CR.format(
    'Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Layers_of_the_GI_Tract_english.svg">Goran tek-en</a>, '
    '<a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>, via Wikimedia Commons'))
SM = '<img src="0659475fc2c5617c08097d5ea6c77acf.webp" width="664">'
ACAL = '<img src="744243dba396cf9271ef8ece44c02c52.webp" width="1084">'
MEGA = ('<img src="1497189500f1b9702bc482e038b7cfee.webp"><br>' + CR.format(
    'Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Chagas_megaseophagus.JPG">CDC</a>, domínio público, via Wikimedia Commons'))
JNE = '<img src="nebli-uc08-fi08-juncao-neuroefetora.jpeg" width="400"><br>' + CR.format("Figura do slide da aula (Motilidade do TGI, aula 1, lâmina 5)")
MNEMO = ('<b>K</b>inase makes muscle <b>K</b>ontracted<br><div><div><b>PH</b>osphatase makes muscle <b>PH</b>laccid</div></div>'
         '<div><i>(mnemônico em inglês: cinase → contraído; fosfatase → flácido)</i></div>')
V, A = 3, 4  # verde, azul

def C(key, src, origin, slide, text, extra, flags, alvo, motivo, **kw):
    return dict(key=key, src=src, origin=origin, slide=slide, text=text, extra=extra, flags=flags, alvo=alvo, motivo=motivo, **kw)

CARDS = [
 # ---------- Lâmina 2: organização do TGI e inervação intrínseca × extrínseca ----------
 C("esofago-estriado", 1482022116564, "AnKing", 2,
   '<div>A <b>faringe</b> e o <b><u>terço superior</u> do esôfago</b> são formados por músculo {{c1::estriado}}</div>',
   ESO.format(w=438), {1: V}, "1/3 superior do esôfago estriado", "Verde: estrutura–função do esôfago (deglutição, distúrbios motores)."),
 C("esofago-liso", 1482022121968, "AnKing", 2,
   '<div>Os <b><u>dois terços inferiores</u> do esôfago</b> são formados por músculo {{c1::liso}}</div>',
   f'O terço médio pode ter músculo esquelético e liso<br><br><div>{ESO.format(w=500)}<br></div>', {1: A},
   "2/3 inferiores lisos", "Azul: par do anterior (AnKing tem os dois; Q13)."),
 C("sne-independente", 1482021669311, "AnKing", 2,
   '<div>O <b>sistema nervoso</b> {{c1::<b>entérico</b>}} pode comandar todas as funções do <b>trato gastrointestinal</b>, mesmo na <u>ausência</u> de inervação extrínseca (p. ex., simpática/parassimpática)</div>',
   f'<div>Localizado em gânglios dos plexos <i>mioentérico</i> e <i>submucoso</i> </div><br><div>{ENS}<br></div>', {1: V},
   "SNE intrínseco e autônomo", "Verde: conceito organizador intrínseco × extrínseco."),
 C("mioenterico-local", 1482021572867, "AnKing", 2,
   '<div>O <b>plexo nervoso</b> {{c1::<b>mioentérico (de Auerbach)</b>}} fica entre as camadas musculares <u>circular</u> e <u>longitudinal</u> da parede do tubo digestório</div>',
   f'Não confundir com o <b>plexo nervoso submucoso (de Meissner),</b> que fica entre a <u>submucosa</u> e a <u>camada muscular circular interna</u> da parede do tubo<br><br>{LAYERS}',
   {1: V}, "Posição do plexo mioentérico", "Verde: posição que explica o comando da muscular (HY AnKing)."),
 C("submucoso-local", 1482021579186, "AnKing", 2,
   '<div>O <b>plexo nervoso</b> {{c1::<b>submucoso (de Meissner)</b>}} fica entre a <u>submucosa</u> e a <u>camada muscular circular interna</u> da parede do tubo digestório</div>',
   f'Não confundir com o <b>plexo nervoso mioentérico (de Auerbach)</b>, que fica entre as camadas musculares <u>circular</u> e <u>longitudinal</u><br><br>{LAYERS}',
   {1: A}, "Posição do plexo submucoso", "Azul: contraparte da posição do mioentérico."),
 C("mioenterico-motilidade", 1482021684208, "AnKing", 2,
   '<div><div>O <b>plexo</b> {{c1::<b>mioentérico (de Auerbach)</b>}} da <u>parede do tubo</u> controla principalmente a <b>motilidade</b></div></div>',
   '- <b><u>S</u></b>ubmucoso: <b><u>S</u></b>ecreção<div>-<b> <u>M</u></b>ioentérico: <b><u>M</u></b>otilidade</div>', {1: V},
   "Mioentérico → motilidade", "Verde: distinção central (HY)."),
 C("submucoso-secrecao", 1482021680972, "AnKing", 2,
   '<div><div>O <b>plexo</b> {{c1::<b>submucoso (de Meissner)</b>}} da <u>parede do tubo</u> controla principalmente a <b>secreção</b> e o<b> fluxo sanguíneo</b></div></div>',
   '- <b><u>S</u></b>ubmucoso: <b><u>S</u></b>ecreção<br><br><div>-<b> <u>M</u></b>ioentérico: <b><u>M</u></b>otilidade</div>', {1: V},
   "Submucoso → secreção/fluxo", "Verde: distinção central (HY)."),
 C("sna-divisoes", None, "Autoral", 2,
   '<div>No tubo digestório, o estímulo parassimpático {{c1::aumenta}} a motilidade e a secreção; o simpático as reduz</div>',
   f'O simpático é o "freio" do tubo; o parassimpático, o "acelerador".<br><br>{ENS}', {1: V},
   "Direção do SNA no tubo", "Verde: regulação autonômica do tubo, base de fármacos e estados de estresse.",
   lacuna="AnKing sem card direto (buscas sympathetic/parasympathetic × motility/peristalsis); MCAT oculta listas inteiras."),
 C("simpatico-esfincteres", 1477011431858, "AnKing", 2,
   '<div>A <u>ativação</u> do receptor adrenérgico {{c2::<b>α<sub>1</sub></b>}} causa {{c1::<u>contração</u>}} dos <b>músculos <i>esfincterianos</i> intestinais</b> e <b>vesicais</b><br></div>',
   '<img alt="File:Adrenoceptor-Signal transduktion.PNG" src="0d731d7f68c85bcc4adb70261d1af71d.webp" width="422"><br><i><span style="font-size: 10pt;">Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Adrenoceptor-Signal_transduktion.PNG">Sven Jähnichen. Partially translated by Mikael Häggström</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>, via Wikimedia Commons </span></i>',
   {1: V, 2: A}, "Simpático contrai esfíncteres (exceção à inibição)", "c1 verde: exceção central (o simpático inibe o tubo, mas fecha os esfíncteres); c2 azul: receptor."),
 C("vago-pelvicos", 1482021615074, "AnKing", 3,
   '<div>Quais <u>nervos</u> levam as fibras <b>parassimpáticas</b> ao <b>trato gastrointestinal</b>? </div><br><div>{{c1::Vago e esplâncnicos pélvicos::2}}</div>',
   '', {1: A}, "Vago e esplâncnicos pélvicos", "Azul: via anatômica retomada em AN14."),
 # ---------- Lâmina 3: integração, reflexos, neurotransmissores, Chagas ----------
 C("sinapse-plexos", 1482021663832, "AnKing", 3,
   '<div>Os neurônios <u>simpáticos</u> <i>pós-ganglionares</i> e os <u>parassimpáticos</u> <i>pré-ganglionares</i> que suprem o <b>trato gastrointestinal</b> fazem sinapse nos plexos {{c1::<b>mioentérico</b>}} ou {{c1::<b>submucoso</b>}}</div>',
   ENS, {1: A}, "SNA modula o SNE fazendo sinapse nos plexos", "Azul: detalhe da integração."),
 C("vagovagal", 1482021618596, "AnKing", 3,
   '<div>Reflexos cujas vias <u>aferente</u> e <u>eferente</u> estão ambas no <b>nervo vago</b> são chamados <b>reflexos {{c1::vagovagais}}</b></div>',
   'É o reflexo <b>longo</b>: a aferência sobe até o tronco encefálico e a resposta volta pelo vago à parede.', {1: V},
   "Reflexo longo = vagovagal", "Verde: reflexo reutilizado em motilidade e secreção."),
 C("reflexo-curto", None, "Autoral", 3,
   '<div>Um reflexo que se fecha nos plexos da própria parede do tubo, sem passar pelo SNC, é um reflexo {{c1::curto (intramural)}}</div>',
   f'Receptor (distensão/químico) → plexo → músculo ou glândula. O longo (vagovagal) passa pelo tronco encefálico.<br><br>{ENS}', {1: V},
   "Reflexo curto", "Verde: contraste com o longo.", lacuna="AnKing/externos sem card (short/local/intramural/peristaltic reflex)."),
 C("ach-excitatorio", None, "Autoral", 3,
   '<div>Nos plexos entéricos, os neurônios motores excitatórios liberam {{c1::acetilcolina}}, que contrai o músculo liso; os inibitórios liberam VIP e NO</div>',
   f'A substância P também é excitatória.<br><br>{ENS}', {1: V},
   "ACh excitatória", "Verde: par excitatório × inibitório.", lacuna="AnKing sem card; atropina/tratamento de íleo são laterais."),
 C("vip-relaxa", 1482022030441, "AnKing", 3,
   '<div>O <b>peptídeo intestinal vasoativo</b> (VIP) causa {{c1::<u>relaxamento</u>}} do <b>músculo liso gastrointestinal</b> e dos <b>esfíncteres</b> (incluindo o EEI) </div>',
   'EEI = esfíncter esofágico inferior', {1: V}, "VIP inibitório", "Verde: transmissor inibitório central."),
 C("vip-parassimpatico", 1482022027494, "AnKing", 3,
   '<div>O <b>peptídeo intestinal vasoativo</b> (VIP) é secretado por neurônios {{c1::<u>parassimpáticos</u>}} na vesícula biliar, no intestino delgado e nos esfíncteres</div>',
   '', {1: A}, "VIP de neurônios parassimpáticos", "Azul: complemento do VIP."),
 C("no-relaxa", 1486831442651, "AnKing", 3,
   '<div>O <b>óxido nítrico</b> causa {{c1::<u>relaxamento</u>}} do <b>músculo liso gastrointestinal</b> e dos <b>esfíncteres</b> (incluindo o EEI) </div>',
   'EEI = esfíncter esofágico inferior', {1: V}, "NO inibitório", "Verde: cotransmissor inibitório (acalasia/Chagas)."),
 C("serotonina-ipan", 1482022183423, "AnKing", 3,
   '<div>A <b>peristalse intestinal</b> é desencadeada pela ligação de {{c1::<b>5-HT </b>(serotonina)}} aos<b> neurônios aferentes primários intrínsecos</b> (IPANs)</div>',
   '', {1: A}, "5-HT ativa os neurônios sensoriais do SNE", "Azul: neuromediador citado na aula."),
 C("distensao-esfincter", None, "Autoral", 4,
   '<div>A distensão do tubo por um bolo faz o esfíncter à frente {{c1::relaxar}}, abrindo passagem</div>',
   f'Neurônios descendentes do plexo mioentérico liberam VIP e NO à frente do bolo; atrás dele, ACh contrai a camada circular.<br><br>{ENS}',
   {1: V}, "Distensão relaxa o esfíncter a jusante", "Verde: princípio destacado no slide; base da peristalse.",
   lacuna="AnKing só por doença (acalasia/Hirschsprung); slide: 'distensão do tubo = relaxamento dos esfíncteres'."),
 C("chagas-plexo", None, "Autoral", 3,
   '<div>O <i>Trypanosoma cruzi</i> destrói neurônios do plexo {{c1::mioentérico}}, e o tubo se dilata, sobretudo como megaesôfago e megacólon</div>',
   f'Perdem-se principalmente os neurônios inibitórios (VIP/NO): o esfíncter não relaxa e o segmento acima se dilata.<br><br>{ACAL}', {1: V},
   "Chagas → plexo mioentérico", "Verde: ponte clínica do próprio slide.", lacuna="AnKing sem card que ligue Chagas ao plexo."),
 C("chagas-mega", 1403046909909, "AnKing", 3,
   '{{c1::<b>Doença de Chagas</b>}} é uma <u>infecção protozoária</u> visceral que se apresenta com <b>cardiomiopatia</b> dilatada, <b>mega</b>{{c3::<b>cólon</b>}} e <b>mega</b>{{c3::<b>esôfago</b>}}',
   f'<div>Na fase crônica, alterações gastrointestinais como acalasia, megacólon e megaesôfago.</div><br><div>{MEGA}</div>',
   {1: A, 3: A}, "Chagas → megacólon/megaesôfago", "Azul: complementa o autoral mecanístico.",
   curadoria="c2 (cardiomiopatia) desfeito: fora da aula; sinais agudos (chagoma, Romaña) e mapa retirados do verso."),
 C("chagas-acalasia", 1509815200893, "AnKing", 3,
   'Qual infecção protozoária <i>crônica</i> pode causar <b>acalasia</b>?<br><br><div>{{c1::Doença de Chagas (<i>Trypanosoma cruzi</i>)}}</div>',
   f'O <i>T. cruzi</i> destrói os neurônios do plexo mioentérico.<br><br><div>{MEGA}</div>', {1: A},
   "Chagas causa acalasia", "Azul: direção inversa, AnKing.", curadoria="Sinais agudos, cardíacos e imagens laterais retirados."),
 C("acalasia-eei", 1482203787030, "AnKing", 3,
   '<div>A {{c2::<b>acalasia</b>}} caracteriza-se por <u>motilidade esofágica desordenada</u> pela <i>incapacidade</i> de relaxar o <b>esfíncter esofágico</b> {{c1::<b>inferior</b>}} </div>',
   f'<b><u>A</u></b>calasia = <u><b>A</b></u>usência de relaxamento <br><br>{ACAL}', {1: V, 2: A},
   "Acalasia: EEI não relaxa", "c1 verde: consequência direta da perda de neurônios inibitórios; c2 azul.",
   curadoria="Radiografias/fotos do verso reduzidas à ilustração do mecanismo. Mnemônico funciona em PT (Acalasia = Ausência)."),
 C("acalasia-no-vip", 1482343170021, "AnKing", 3,
   'A perda de quais <u>neurotransmissores</u> está implicada na patogênese da <b>acalasia</b>?<br><br>{{c1::NO e VIP::2}}',
   f'<u>Aumento</u> do <b>tônus do EEI</b> por menor relaxamento<br><br>{ACAL}', {1: V},
   "Acalasia = perda de NO/VIP", "Verde: liga os inibitórios da aula à doença."),
 # ---------- Lâmina 4: fásica × tônica, esfíncteres, piloro ----------
 C("contracao-fasica", 1482022053859, "AnKing", 4,
   '<div>As <b>contrações</b> {{c1::<b>fásicas</b>}} do <u>músculo liso gastrointestinal</u> são <b>contrações periódicas</b> <i>seguidas</i> de <b>relaxamento</b> </div>',
   'Ocorrem no esôfago, no antro gástrico e no intestino delgado', {1: V}, "Fásica", "Verde: par fásica/tônica da lâmina 4."),
 C("contracao-tonica", 1482022061641, "AnKing", 4,
   '<div>As <b>contrações</b> {{c1::<b>tônicas</b>}} do <u>músculo liso gastrointestinal</u> mantêm um <b>nível constante de contração</b>, <i>sem</i> períodos regulares de relaxamento </div>',
   'Ocorrem na região superior do estômago e nos esfíncteres esofágico inferior, ileocecal e anal interno<i> </i><br><br>A força se mantém mesmo com Ca<sup>2+</sup> e fosforilação da miosina já reduzidos (pontes em trava, <i>latch</i>).',
   {1: V}, "Tônica (esfíncteres)", "Verde: padrão dos esfíncteres."),
 C("ees-funcao", 1482022126258, "AnKing", 4,
   '<div>O <b>esfíncter esofágico</b> {{c1::<b>superior</b>}} impede a entrada de <u>ar</u> no esôfago</div>', ESO.format(w=300), {1: A},
   "Função do EES", "Azul."),
 C("eei-funcao", 1482022129277, "AnKing", 4,
   '<div>O <b>esfíncter esofágico</b> {{c1::<b>inferior</b>}} impede que o <u>conteúdo gástrico</u> entre no esôfago</div>', ESO.format(w=300), {1: V},
   "Função do EEI", "Verde: base do refluxo e da acalasia."),
 C("piloro-duodeno", None, "Autoral", 4,
   '<div>Ácido e gordura no duodeno fazem o piloro {{c1::contrair}}, retardando o esvaziamento gástrico (regulação duodenal retrógrada)</div>',
   '<img src="4513cb2d9ae02edfe3503b8f011d67ab.png" width="500"><br>Já a distensão do antro relaxa o piloro (regulação antral anterógrada).', {1: A},
   "Regulação duodenal retrógrada do piloro", "Azul: detalhado na FI09.", lacuna="AnKing cobra o efeito no esvaziamento, não o piloro; slide lâmina 4."),
 C("esvaziamento-gordura-acido", 1482022155210, "AnKing", 4,
   '<div>A velocidade do <b>esvaziamento gástrico</b> é <u>reduzida</u> principalmente por {{c1::<b>gorduras</b>}} e {{c2::<b>H<sup>+</sup></b>}} no <b>duodeno</b> </div>',
   '- Via CCK e reflexos do sistema nervoso entérico, respectivamente<br><br>- Dá tempo para a digestão das gorduras e a neutralização do H<sup>+ </sup>',
   {1: A, 2: A}, "Duodeno freia o esvaziamento", "Azul: aprofundado na FI09."),
 # ---------- Lâmina 5: junção neuroefetora e contração/relaxamento ----------
 C("varicosidades", 1701640720206, "Histology", 5,
   '<div>No músculo liso, os axônios autonômicos liberam neurotransmissores por dilatações chamadas {{c1::varicosidades}}, sem placa motora especializada</div>',
   f'O transmissor se difunde e age em várias células; as junções comunicantes propagam a excitação.<br><br>{JNE}', {1: A},
   "Junção neuroefetora: varicosidades", "Azul.", curadoria="Nota Histology em lista reescrita em uma frase (F-C44)."),
 C("calmodulina", 1497378148913, "AnKing", 5,
   '{{c4::<b>Ca<sup>2+</sup></b>}} entra nas células do <u>músculo liso</u> por canais de {{c4::<b>Ca<sup>2+</sup></b>}} do <b>tipo</b> {{c3::<b>L</b>}} e se <i>liga</i> à {{c1::<u>calmodulina</u>}}, levando à {{c2::<b>contração</b>}} do músculo liso',
   f'<div>A <u>calmodulina</u> ativa a <b>cinase da cadeia leve da miosina (MLCK)</b></div><div>Receptores acoplados a G<sub>q</sub> também liberam Ca<sup>2+</sup> do retículo sarcoplasmático, via IP<sub>3</sub>.</div><br><div>{SM}<br></div>',
   {1: V, 2: A, 3: A, 4: A}, "Ca²⁺ → calmodulina (não troponina)", "c1 verde: diferença central com o estriado; demais azuis."),
 C("mlck", 1497378477763, "AnKing", 5,
   'O complexo <i>Ca<sup style="">2+</sup>-calmodulina</i> ativa a {{c1::<b>cinase da cadeia leve da miosina</b> (MLCK)}}, que {{c1::<b>fosforila</b>::fosforila/desfosforila}} a miosina e {{c2::<b>contrai</b>}} o <u>músculo liso</u>',
   f'{MNEMO}<br><div>{SM}<br></div>', {1: V, 2: A}, "MLCK fosforila → contração", "c1 verde (HY)."),
 C("mlcp", 1497378395390, "AnKing", 5,
   'O <b>GMPc</b> estimula a {{c1::<i>fosfatase da cadeia leve da miosina</i>}}, que {{c1::<b>desfosforila</b>::fosforila/desfosforila}} a <b>miosina</b> e {{c2::relaxa}} o <u>músculo liso</u>',
   f'{MNEMO}<div>Relaxar também exige tirar o Ca<sup>2+</sup> do citosol: Ca<sup>2+</sup>-ATPases da membrana e do retículo sarcoplasmático.</div><div><br>{SM}<br></div>',
   {1: V, 2: A}, "Fosfatase → relaxamento", "c1 verde."),
 C("gmpc-desfosforila", 1472747780684, "AnKing", 5,
   '<div>O <u>aumento</u> de <b>GMPc</b> causa {{c2::<b>desfosforilação</b>}} da {{c1::<b>cadeia leve da miosina</b>}}, <u>impedindo</u> sua interação com a actina</div>',
   f'O GMPc estimula a <b>fosfatase da cadeia leve da miosina</b>, que desfosforila a miosina e impede sua interação com a actina<br><br>{SM}',
   {1: A, 2: A}, "GMPc → desfosforilação (via do NO)", "Azul: mesma via por outro ângulo (AnKing)."),
 # ---------- Lâmina 6: GPCR, Gq e sensibilização ----------
 C("m3-gq", 1475114985396, "AnKing", 6,
   '<div>A qual <b>proteína G</b> o receptor muscarínico <b>M<sub>3</sub></b> está acoplado?<br></div><div><br><div>{{c1::G<sub>q</sub>}}</div></div>',
   'A G<sub>q</sub> estimula a PLC, que cliva o PIP<sub>2</sub> em IP<sub>3</sub> e DAG; eles levam, respectivamente, ao aumento do Ca<sup>2+</sup> intracelular e à ativação da PKC<br><br><img src="f826f724045847ea9be8a5b2c440a5d4.png" width="400">',
   {1: A}, "ACh (M3) → Gq → IP3/DAG", "Azul: via da lâmina 6 (ativação da contração)."),
 C("rho-cinase", None, "Autoral", 6,
   '<div>A Rho-cinase (ROCK) inibe a {{c1::miosina fosfatase}}, mantendo o músculo liso contraído com menos Ca<sup>2+</sup></div>',
   f'É a sensibilização ao Ca<sup>2+</sup>; a PKC faz o mesmo via CPI-17.<br><br>{SM}', {1: A},
   "Inibição do relaxamento", "Azul.", lacuna="AnKing sem Rho-cinase no músculo liso."),
]

EXCLUIDOS = [
 (1482022131650, "VIP relaxa o EEI na deglutição — deglutição é FI09 (associar lá)"),
 (1482022134697, "Relaxamento receptivo — FI09"),
 (1482022105272, "Células de Cajal/ondas lentas — FI09"),
 (1482203793099, "Acalasia primária autoimune — doença lateral"),
 (1476919773069, "Atropina reduz motilidade — farmacologia lateral"),
 (1482203808143, "Manometria na acalasia — diagnóstico lateral"),
]

# ---- v3b: calibração pelo card-mirror (29/09): frente factual curta, cloze no termo de maior valor,
# verso telegráfico (fragmentos) ou só imagem; sem mecanismo/finalidade na frente, sem metáfora.
OVERRIDES = {
 "sna-divisoes": dict(text='<div>O sistema nervoso {{c1::parassimpático}} aumenta a motilidade e a secreção gastrointestinais</div>',
                      extra=f'Simpático: ↓ motilidade e secreção; contrai esfíncteres<br><br>{ENS}'),
 "reflexo-curto": dict(text='<div>Reflexos {{c1::curtos}} do trato gastrointestinal têm aferência e eferência restritas aos plexos entéricos</div>',
                       extra=f'Longos (vagovagais): via tronco encefálico<br><br>{ENS}'),
 "ach-excitatorio": dict(text='<div>Os neurônios motores excitatórios do sistema nervoso entérico liberam {{c1::acetilcolina}}</div>',
                         extra=f'Também substância P<br>Inibitórios: VIP e NO<br><br>{ENS}'),
 "distensao-esfincter": dict(text='<div>A distensão do tubo digestório causa {{c1::relaxamento}} do esfíncter a jusante</div>',
                             extra=f'Via VIP e NO (neurônios inibitórios descendentes)<br><br>{ENS}'),
 "chagas-plexo": dict(text='<div>Na doença de Chagas, o megaesôfago resulta da destruição do plexo {{c1::mioentérico}}</div>',
                      extra=f'Perda de neurônios inibitórios (VIP/NO)<br><br>{ACAL}'),
 "piloro-duodeno": dict(text='<div>Ácido e gordura no duodeno causam {{c1::contração}} do esfíncter pilórico</div>',
                        extra='Distensão do antro: relaxamento do piloro<br><br><img src="4513cb2d9ae02edfe3503b8f011d67ab.png" width="500">'),
 "rho-cinase": dict(text='<div>A Rho-cinase (ROCK) inibe a {{c1::fosfatase da cadeia leve da miosina}} no músculo liso</div>',
                    extra=f'↑ sensibilidade ao Ca<sup>2+</sup><br>PKC → CPI-17: mesmo efeito<br><br>{SM}'),
 "varicosidades": dict(text='<div>No músculo liso, os axônios autonômicos liberam neurotransmissores a partir de {{c1::varicosidades}}</div>',
                       extra=f'Sem placa motora especializada<br><br>{JNE}'),
 "vagovagal": dict(extra='Reflexo longo (via tronco encefálico)'),
 "contracao-tonica": dict(extra='Ocorrem na região superior do estômago e nos esfíncteres esofágico inferior, ileocecal e anal interno<i> </i><br><br>Pontes em trava (<i>latch</i>): força mantida com pouco Ca<sup>2+</sup>'),
 "calmodulina": dict(extra=f'<div>A <u>calmodulina</u> ativa a <b>cinase da cadeia leve da miosina (MLCK)</b></div><div>G<sub>q</sub> → IP<sub>3</sub> → Ca<sup>2+</sup> do retículo sarcoplasmático</div><br><div>{SM}<br></div>'),
 "mlcp": dict(extra=f'{MNEMO}<div>Retirada do Ca<sup>2+</sup>: Ca<sup>2+</sup>-ATPases da membrana e do retículo sarcoplasmático</div><div><br>{SM}<br></div>'),
 "chagas-mega": dict(extra=f'<div>Crônica: acalasia, megacólon e megaesôfago</div><br><div>{MEGA}</div>'),
 "chagas-acalasia": dict(extra=f'Destruição do plexo mioentérico<br><br><div>{MEGA}</div>'),
}
for c in CARDS:
    c.update(OVERRIDES.get(c["key"], {}))

# ---- v3c: revisão independente de tradução (29/09) — decalques, pistas, absolutos
MNEMO_PT = '<b>C</b>inase → <b>C</b>ontrai<br><div><b>F</b>osfatase → <b>F</b>lácido</div>'
OVR2 = {
 "chagas-mega": dict(text='A <b>doença de</b> {{c1::<b>Chagas</b>}} é uma <u>protozoose</u> visceral que se manifesta com <b>cardiomiopatia</b> dilatada, <b>mega</b>{{c3::<b>cólon</b>}} e <b>mega</b>{{c3::<b>esôfago</b>}}',
                     extra=f'<div>Fase crônica: acalasia, megacólon e megaesôfago</div><br><div>{MEGA}</div>'),
 "chagas-acalasia": dict(text='Qual infecção <i>crônica</i> por <u>protozoário</u> pode causar <b>acalasia</b>?<br><br><div>{{c1::Doença de Chagas (<i>Trypanosoma cruzi</i>)}}</div>'),
 "acalasia-eei": dict(text='<div>A {{c2::<b>acalasia</b>}} é um <u>distúrbio da motilidade esofágica</u> causado pela <i>incapacidade</i> de relaxar o <b>esfíncter esofágico</b> {{c1::<b>inferior</b>}} </div>'),
 "contracao-tonica": dict(extra='Ocorrem na porção proximal do estômago e nos esfíncteres esofágico inferior, ileocecal e anal interno<i> </i><br><br>Mecanismo de trava (<i>latch</i>): força mantida com pouco Ca<sup>2+</sup> e baixo gasto de energia'),
 "mlck": dict(extra=f'{MNEMO_PT}<br><div>{SM}<br></div>'),
 "mlcp": dict(extra=f'{MNEMO_PT}<div>Retirada do Ca<sup>2+</sup>: Ca<sup>2+</sup>-ATPases da membrana e do retículo sarcoplasmático</div><div><br>{SM}<br></div>'),
 "calmodulina": dict(text='O {{c4::<b>Ca<sup>2+</sup></b>}} entra nas células do <u>músculo liso</u> por canais de {{c4::<b>Ca<sup>2+</sup></b>}} do <b>tipo</b> {{c3::<b>L</b>}} e se <i>liga</i> à {{c1::<u>calmodulina</u>}}, levando à {{c2::<b>contração</b>}} do músculo liso'),
 "m3-gq": dict(extra='A G<sub>q</sub> estimula a PLC, que cliva o PIP<sub>2</sub> em IP<sub>3</sub> e DAG, os quais levam, respectivamente, ao aumento do Ca<sup>2+</sup> intracelular e à ativação da PKC<br><br><img src="f826f724045847ea9be8a5b2c440a5d4.png" width="400">'),
 "simpatico-esfincteres": dict(extra='<img alt="File:Adrenoceptor-Signal transduktion.PNG" src="0d731d7f68c85bcc4adb70261d1af71d.webp" width="422"><br><i><span style="font-size: 10pt;">Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Adrenoceptor-Signal_transduktion.PNG">Sven Jähnichen, tradução parcial de Mikael Häggström</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>, via Wikimedia Commons </span></i>'),
 "reflexo-curto": dict(extra=f'Longos (p. ex., vagovagais): passam pelo SNC<br><br>{ENS}'),
}
import re as _re
for c in CARDS:
    c.update(OVR2.get(c["key"], {}))
    for f in ("text", "extra"):
        c[f] = _re.sub(r"parede do tubo(?! digestório)(</u>)?", lambda m: "parede do tubo digestório" + (m.group(1) or ""), c[f])

# ---- v3d: auditoria de núcleo pelo executor (Davi 29/09: "você que tem que me dizer")
for c in CARDS:
    if c["key"] == "contracao-fasica":
        c["flags"] = {1: 4}; c["motivo"] = "Azul: dedutível pelo contraste com a tônica (verde)."
