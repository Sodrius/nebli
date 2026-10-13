# BT03 v3 (run uc08-bt03-20260929a) — correção após F-C44. Calibração: slides (texto) + roteiro prático
# + Osmosis "Stomach: Histology" e Ninja Nerd "Enteric Nervous System" (legendas lidas) + Junqueira cap. 15
# (figuras 15-14 a 15-21 do acervo Histology) + AnKing FirstAid/Costanzo. Boca/dente: poucos, azuis (Davi 29/09).
RUN_ID = "uc08-bt03-20260929a"
VERSION = "v3"
LESSON = "2026-uc08-biologia-tecidual-03-estrutura-estomago"
DECK = "NEBLI::UC08::P1::Biologia Tecidual::Estrutura geral do estômago"
CRITERIOS = "README/CONTRATO/BANDEIRAS/ESTILO/TRADUCAO 29/09 + F-C43/F-C44 + respostas 23/09"

CR = '<span style="font-size: 10pt;"><em>{}</em></span>'
LAYERS = ('<img src="f7114acc00def107eaa664fd4737aeac.jpg" width="700"><br>' + CR.format(
    'Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Layers_of_the_GI_Tract_english.svg">Goran tek-en</a>, '
    '<a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>, via Wikimedia Commons'))
J = lambda f, fig: f'<img src="{f}"><br>' + CR.format(f"Junqueira, Histologia Básica, fig. {fig}")
OPENSTAX = ('<img src="83c9486db063297d7bc66b0a27fe7b49.png"><br>' + CR.format(
    'Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:2415_Histology_of_StomachN.jpg">OpenStax College</a>, '
    '<a href="https://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>, via Wikimedia Commons'))
ANTRAL = ('<img src="1d2db30a9f25deb66973726150208c4e.png"><br>' + CR.format(
    'Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Histology_of_normal_antral_mucosa.png">Carrasco G, Corvalan AH</a>, '
    '<a href="https://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>, via Wikimedia Commons'))
JPOGI = ('<img src="5496b2facd4097e7044621b58e1ad6c2.jpg" width="510"><br>' + CR.format(
    'Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Parietal_cells.jpg">Jpogi at English Wikipedia</a>, domínio público, via Wikimedia Commons'))
HAGG = lambda f, w=487: (f'<img src="{f}" width="{w}"><br>' + CR.format(
    'Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Parietal_cell_and_chief_cells.png">Mikael Häggström</a>, CC0, via Wikimedia Commons, setas acrescentadas'))
SEC = '<img src="088d1869ef3e541e74f413ba4928a07c.png" width="1100">'
V, A = 3, 4

def C(key, src, origin, slide, text, extra, flags, alvo, motivo, **kw):
    return dict(key=key, src=src, origin=origin, slide=slide, text=text, extra=extra, flags=flags, alvo=alvo, motivo=motivo, **kw)

CARDS = [
 # ---------- Cavidade oral (slides iniciais) — poucos, azuis ----------
 C("dente-tecidos", 1702208297305, "Histology", "oral",
   '<div>No dente, o {{c1::esmalte}}, acelular, recobre a coroa; o {{c2::cemento}} recobre a raiz; e a {{c3::dentina}} forma a maior parte do dente</div>',
   'A polpa, no centro, é conjuntivo frouxo vascularizado e inervado; o ligamento periodontal prende o cemento ao osso alveolar.',
   {1: A, 2: A, 3: A}, "Tecidos do dente", "Azul: slide inicial de boca (pedido de Davi: poucos, azuis).",
   curadoria="Nota em lista (9 clozes) reescrita numa frase com os três tecidos do slide."),
 C("parotida-serosa", 1702296274795, "Histology", "oral",
   '<div>A glândula {{c1::parótida}} tem ácinos exclusivamente serosos, ricos em α-amilase</div>',
   'Sublingual: predominantemente mucosa. Submandibular: mista, com predomínio seroso.', {1: A},
   "Parótida serosa", "Azul.", curadoria="Nota em lista reescrita em uma frase."),
 C("sublingual-mucosa", 1702296589459, "Histology", "oral",
   '<div>A glândula salivar {{c1::sublingual}}, a menor das maiores, é predominantemente mucosa</div>',
   'Parótida: serosa. Submandibular: mista, com predomínio seroso e semiluas serosas.', {1: A},
   "Sublingual mucosa", "Azul.", curadoria="Nota em lista reescrita em uma frase."),
 C("submandibular-mista", 1702296410763, "Histology", "oral",
   '<div>A glândula {{c1::submandibular}} é mista, com predomínio de ácinos serosos, e produz cerca de dois terços da saliva</div>',
   'Nas unidades mistas, as células serosas formam as semiluas serosas.', {1: A},
   "Submandibular mista", "Azul.", curadoria="Nota em lista reescrita em uma frase."),
 C("lingua-ventral", 1702140426233, "Histology", "oral",
   '<div>A face ventral (inferior) da língua é lisa, revestida por mucosa de {{c1::revestimento}}, sem papilas</div>',
   'O dorso tem mucosa especializada com papilas nos dois terços anteriores e tonsila lingual no terço posterior.', {1: A},
   "Face ventral da língua", "Azul: slide 'Língua — superfície ventral'.", curadoria="Nota em lista reescrita em uma frase."),
 # ---------- Plano geral da parede ----------
 C("mucosa-camadas", 1482021549752, "AnKing", "parede",
   '<div>A <b>mucosa</b> da <u>parede do tubo digestório</u> tem três camadas: {{c1::epitélio}}, {{c2::lâmina própria}} e {{c3::muscular da mucosa}}</div>',
   f'A muscular da mucosa (músculo liso) separa a mucosa da submucosa.<br><br>{LAYERS}', {1: A, 2: V, 3: V},
   "Subcamadas da mucosa", "c2/c3 verdes: plano geral usado em toda a histologia/patologia do tubo."),
 C("submucosa-posicao", 1482021556058, "AnKing", "parede",
   '<div>Externamente à <u>camada mucosa</u> da parede do tubo fica a {{c1::<b>submucosa</b>}}</div>', LAYERS, {1: V},
   "Ordem: submucosa", "Verde: ordem das camadas (base)."),
 C("muscular-externa-posicao", 1482021561377, "AnKing", "parede",
   '<div>Externamente à <u>camada submucosa</u> da parede do tubo fica a {{c1::<b>muscular externa</b>}}</div>', LAYERS, {1: V},
   "Ordem: muscular externa", "Verde: ordem das camadas."),
 C("muscular-externa", 1482021567159, "AnKing", "parede",
   '<div>A <b>muscular externa</b> da parede do tubo tem uma camada {{c1::circular}} <u>interna</u> e uma {{c1::longitudinal}} <u>externa</u></div>',
   f'No estômago há ainda uma camada oblíqua, a mais interna.<br><br>{LAYERS}', {1: V},
   "Circular interna / longitudinal externa", "Verde: disposição base."),
 C("estomago-obliqua", None, "Autoral", "parede",
   '<div>A muscular externa do estômago tem, além da circular e da longitudinal, uma camada {{c1::oblíqua}} interna</div>',
   f'Ajuda a misturar e triturar o conteúdo gástrico.<br><br>{OPENSTAX}', {1: A},
   "Camada oblíqua do estômago", "Azul.", lacuna="AnKing/Histology sem card; slides (anatomia externa) e Osmosis mostram."),
 C("serosa", 1482021584289, "AnKing", "parede",
   '<div>A camada mais <u>externa</u> da <b>parede do tubo</b> é a {{c1::serosa}} (quando intraperitoneal)</div>',
   f'<b>Adventícia</b> quando retroperitoneal<br><br>{LAYERS}', {1: A}, "Serosa", "Azul."),
 C("adventicia", 1482021589803, "AnKing", "parede",
   '<div>A camada mais externa da parede do tubo é a {{c1::<b>adventícia</b>}} (quando retroperitoneal)</div>',
   f'Serosa quando intraperitoneal. O esôfago torácico tem adventícia; o estômago, serosa.<br><br>{LAYERS}', {1: A},
   "Adventícia", "Azul."),
 C("meissner-camada", 1482021594676, "AnKing", "parede",
   '<div>Qual <u>camada da parede do tubo</u> contém o <b>plexo de Meissner</b>? </div><br><div>{{c1::Submucosa}}</div>',
   f'<div>Por isso também é chamado plexo submucoso</div><br><div>{LAYERS}</div>', {1: A}, "Meissner na submucosa", "Azul."),
 C("auerbach-camada", 1482021603417, "AnKing", "parede",
   '<div>Qual <u>camada da parede do tubo</u> contém o <b>plexo de Auerbach</b>? </div><br><div>{{c1::Muscular externa}}</div>',
   f'<div>Por isso também é chamado plexo mioentérico</div><br><div>{LAYERS}</div>', {1: A}, "Auerbach na muscular externa", "Azul."),
 C("rugas", 1702213597922, "Histology", "parede",
   '<div>A mucosa e a submucosa do estômago formam pregas longitudinais, as {{c1::rugas (rugae)}}, que se achatam quando o estômago se enche</div>',
   J("82605678fa1ed99d7ea5012425fc98d3.webp", "15-14"), {1: A}, "Rugas gástricas", "Azul.",
   curadoria="Nota em lista reescrita em uma frase."),
 # ---------- Esôfago e junção ----------
 C("esofago-epitelio", 1486608389324, "AnKing", "roteiro-esofago",
   'Que tipo de <u>epitélio</u> reveste o <b>esôfago</b>? <br><br><div>{{c1::Epitélio estratificado pavimentoso não queratinizado}}</div>',
   '<img src="8cdfa5fc71b70e51af98dcbc8041e650.png"><br>' + CR.format('Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Thuc_quan.jpg">Nva1991</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0">CC BY-SA 3.0</a>, via Wikimedia Commons'),
   {1: V}, "Epitélio do esôfago", "Verde."),
 C("juncao-esofagogastrica", 1702213752722, "Histology", "roteiro-transicoes",
   '<div>Na junção esofagogástrica, o epitélio estratificado pavimentoso muda abruptamente para {{c1::cilíndrico simples}}</div>',
   f'Do lado gástrico, o epitélio se invagina em fossetas que levam às glândulas.<br><br>{J("82605678fa1ed99d7ea5012425fc98d3.webp", "15-14")}',
   {1: V}, "Transição esofagogástrica", "Verde.", curadoria="Nota em lista reescrita em uma frase."),
 # ---------- Regiões ----------
 C("fundo-corpo-iguais", 1702214781032, "Histology", "regiao-corpo-fundo",
   '<div>Histologicamente, o fundo e o {{c1::corpo}} do estômago são iguais: ambos têm as glândulas gástricas (oxínticas)</div>',
   f'É a região funcional mais importante: ácido e pepsina.<br><br>{J("b8647af3199815237f7622aff1f2a0fc.webp", "15-17")}', {1: A},
   "Fundo = corpo", "Azul.", curadoria="Nota em lista reescrita em uma frase."),
 C("cardia-piloro-muco", 1702220517802, "Histology", "regiao-cardia-antro",
   '<div>Comparadas às glândulas do corpo, as glândulas da cárdia e do piloro secretam principalmente {{c1::muco}}</div>',
   f'Não têm células parietais e principais; na cárdia são enoveladas.<br><br>{J("a66ad2c7955fb8ca4c079ca9af584855.webp", "15-21")}', {1: V},
   "Cárdia/piloro mucosas", "Verde: contraste regional central.", curadoria="Nota em lista reescrita; título errado e tabela lateral retirados."),
 C("piloro-fossetas", None, "Autoral", "regiao-antro",
   '<div>Na região pilórica, as fossetas gástricas são {{c1::profundas}} (cerca de metade da mucosa) e as glândulas, curtas e enoveladas</div>',
   f'No corpo é o contrário: fossetas rasas e glândulas longas.<br><br>{ANTRAL}', {1: A},
   "Fossetas profundas no piloro", "Azul.", lacuna="Histology 1702220517802 só diz 'fossetas longas'; slide e Osmosis explicitam."),
 C("regiao-fundica-he", 1667460205460, "LLU", "regiao-corpo-fundo",
   'Esta é uma&nbsp;<b>imagem em maior aumento</b>&nbsp;de&nbsp;{{c1::estômago oxíntico/fúndico}}<br><br><img src="paste-285af7c65716abbec41ced6e635e74ff448f45f5.png" width="590"><br><img src="paste-438815d1674aec9e56d5491223223627e1a70d65.png" width="592"><br><img src="paste-5fd70752adbdef98c597af64c2c4cc55bf70fcd3.png" width="593">',
   'Células principais + células parietais = estômago fúndico (corpo/fundo)<br>As células-tronco ficam na transição istmo–colo', {1: A},
   "Reconhecer mucosa do corpo em HE", "Azul."),
 C("regiao-pilorica-he", 1667460370853, "LLU", "regiao-antro",
   'Esta é uma <b>imagem em maior aumento</b>&nbsp;de&nbsp;{{c1::estômago antral/pilórico}}<br><br><img src="paste-3c60c7c15a904453246835ff33ccaf3d3c6a6c83.png" width="599"><img src="paste-d7c5ef5cd521a3cf957a7db2d65f6b58bfaa2489.png" width="599">',
   'Glândulas claras porque secretam muco; fossetas profundas e glândulas curtas.', {1: A},
   "Reconhecer mucosa pilórica em HE", "Azul."),
 # ---------- Superfície, fossetas, glândulas ----------
 C("fossetas", 1486608728772, "AnKing", "superficie",
   '<div>A superfície do <u>estômago</u> é marcada <i>histologicamente</i> por sulcos próximos chamados {{c1::<b>fossetas</b>}} <b>gástricas</b>, nas quais desembocam várias glândulas gástricas</div>',
   f'Também chamadas fovéolas (daí "células foveolares").<br><br>{OPENSTAX}<br>{ANTRAL}', {1: V},
   "Fossetas", "Verde: organização da mucosa gástrica."),
 C("glandulas-corpo-celulas", 1486608734803, "AnKing", "mucosa-corpo",
   '<div>As {{c1::<b>glândulas</b>}} <b>gástricas</b> do <u>corpo do estômago</u> contêm <b>células mucosas</b>, <b>células principais</b> e <b>células parietais</b></div>',
   f'{OPENSTAX}<br><br>{ANTRAL}', {1: A}, "Glândulas do corpo e suas células", "Azul."),
 C("mucosas-superficiais", 1702214216607, "Histology", "superficie",
   '<div>Nas fossetas gástricas, as células {{c1::mucosas superficiais}} produzem a camada protetora de muco</div>',
   f'Formam um epitélio cilíndrico simples; o muco é espesso, aderente e rico em bicarbonato.<br><br>{J("f7b405d94c64b5542191f31360f7f555.webp", "15-16")}',
   {1: A}, "Mucosas superficiais", "Azul.", curadoria="Nota em lista reescrita em uma frase."),
 C("muco-bicarbonato", 1482115272152, "AnKing", "superficie",
   '<div>O <u>muco</u> que recobre o <b>epitélio</b> <b>gástrico</b> <i>retém</i> {{c1::HCO<sub>3</sub><sup>-</sup>}}, neutralizando o HCl que atravessa a barreira de muco </div>',
   'O principal componente do muco (mucina) é secretado pelas células <b>foveolares </b>do estômago', {1: A},
   "Muco retém HCO3⁻", "Azul: função das mucosas superficiais."),
 C("hpylori-antro", 1510261416840, "AnKing", "superficie",
   '<div>O <i>Helicobacter pylori</i> coloniza mais comumente o {{c1::antro::região}} gástrico, mas não o invade</div>',
   'Especificamente, a <b>pequena curvatura do antro</b><br><br><img src="4513cb2d9ae02edfe3503b8f011d67ab.png" width="600">', {1: A},
   "H. pylori no antro", "Azul: relação clínica do slide."),
 C("istmo-celulas-tronco", 1702214416325, "Histology", "mucosa-corpo",
   '<div>Nas glândulas gástricas, as células-tronco ficam no {{c1::istmo}}, na transição entre a fosseta e a glândula</div>',
   f'Suas progenitoras renovam as células mucosas superficiais (a cada 4–7 dias) e as da glândula.<br><br>{J("b8647af3199815237f7622aff1f2a0fc.webp", "15-17")}',
   {1: A}, "Células-tronco no istmo", "Azul.", curadoria="Nota em lista reescrita em uma frase."),
 # ---------- Células ----------
 C("parietal-hcl", 1482030311506, "AnKing", "parietal",
   '<div>As {{c4::<b>células parietais</b>}} ficam no {{c3::<u>corpo</u>}} do estômago e secretam {{c1::<b>HCl</b>}} e {{c2::<b>fator intrínseco</b>}}</div>',
   f'<div>Têm <u>muitas</u> <b>mitocôndrias</b> e um <b>sistema tubulovesicular</b> <u>intracelular</u> que lhes permite <u>secretar grandes quantidades</u> de <b>HCl</b> e <b>fator intrínseco</b></div><br><div>{SEC}<br></div>',
   {1: V, 2: V, 3: V, 4: V}, "Parietal: local e produtos", "Verdes (HY; relação célula–função)."),
 C("parietal-eosinofila", 1486608745216, "AnKing", "parietal",
   '<div>As células {{c2::<b>parietais</b>::principais ou parietais}} do <u>estômago</u> são {{c1::<b>eosino</b>}}<b>fílicas</b></div>',
   ('<div><b>P</b>arietal = <b>P</b>ink (rosa)<br>Predominam na porção superior das glândulas (istmo e colo).</div>'
    '<div>A eosinofilia se deve à grande quantidade de mitocôndrias e de membranas.</div><br>' + HAGG("3b736377bf811a11f71f531e4b04aa5d.webp") + '<br><br>' + JPOGI),
   {1: V, 2: V}, "Parietal eosinófila", "Verdes: critério de identificação.",
   correcao="Extra original atribuía a eosinofilia ao fator intrínseco; corrigido (Junqueira 15-17)."),
 C("parietal-imagem", None, "Autoral", "parietal",
   f'<div>Nesta glândula gástrica, a célula apontada, grande e rosa, com núcleo central, é uma célula {{{{c1::parietal}}}}</div><br>{JPOGI}',
   'Eosinófila pelas mitocôndrias; predomina no istmo e no colo das glândulas do corpo e do fundo.', {1: V},
   "Identificar parietal em HE", "Verde: representante visual (imagem na frente).", lacuna="Imagem AnKing (Jpogi) sem card de identificação; roteiro exige reconhecer."),
 C("parietal-canaliculo", 1702215619877, "Histology", "parietal",
   '<div>A célula parietal tem um {{c1::canalículo intracelular}} revestido de microvilos, que se amplia quando ela é estimulada a secretar HCl</div>',
   f'Em repouso, túbulo-vesículas armazenam as bombas; ao estímulo, fundem-se à membrana do canalículo.<br><br>{J("4534b7a2f4a6be49ccb02757d26c2325.webp", "15-18")}',
   {1: A}, "Canalículo da parietal", "Azul.", curadoria="Nota em lista reescrita em uma frase."),
 C("mucosas-colo", 1702215136161, "Histology", "colo",
   '<div>Entre as parietais, na porção média das glândulas do corpo, as células {{c1::mucosas do colo}} secretam muco</div>',
   f'São menores e claras em HE; o muco é menos alcalino que o das mucosas superficiais.<br><br>{J("b8647af3199815237f7622aff1f2a0fc.webp", "15-17")}',
   {1: A}, "Mucosas do colo", "Azul.", curadoria="Nota em lista reescrita em uma frase."),
 C("principal-basofila", 1486608739171, "AnKing", "base",
   '<div>As células {{c2::<b>principais</b>::principais ou parietais}} do <u>estômago</u> são {{c1::<b>baso</b>}}<b>fílicas</b></div>',
   ('<div>- <u><b>CHIEF</b></u>s need to report at <b><u>BAS</u></b>e <i>(mnemônico em inglês: principais → base, basófilas)</i></div><br>'
    '<div>- Secretam pepsinogênio, que se converte em pepsina no pH gástrico; a pepsina inicia a digestão de proteínas</div><br>'
    '<div>- Basófilas pelo retículo endoplasmático rugoso abundante (síntese de proteína)</div><br>'
    '<div>- Predominam na <u>base</u> das glândulas gástricas</div><br>' + HAGG("f59a172e63351c7e6236cf58efec45bd.png")),
   {1: V, 2: A}, "Principal basófila", "c1 verde; c2 azul."),
 C("principal-pepsinogenio", 1482030315536, "AnKing", "base",
   '<div>As {{c3::<b>células principais</b>}} (zimogênicas) ficam no {{c2::<u>corpo</u>}} do estômago e secretam {{c1::<b>pepsinogênio</b>::<b>proenzima</b>}} e {{c1::<b>lipase gástrica</b>::<b>enzima</b>}}</div>',
   SEC, {1: V, 2: A, 3: V}, "Principal: pepsinogênio", "c1/c3 verdes (HY); c2 azul."),
 C("pepsinogenio-pepsina", 1482030319798, "AnKing", "base",
   '<div>O <b>pepsinogênio</b> (inativo) é convertido em {{c1::<b>pepsina</b>}} (ativa) na presença de {{c2::<b>H<sup>+</sup></b>}}</div>',
   '', {1: A, 2: A}, "Ativação do pepsinogênio", "Azul."),
 C("principal-imagem", 1667460205460, "LLU", "base", None, None, {}, "", "", skip=True),
 C("grelina", 1482022013033, "AnKing", "enteroendocrinas",
   'A <b>grelina</b> é secretada por células gástricas e {{c1::aumenta}} o apetite',
   'Produzida por células enteroendócrinas (X/A-like) das glândulas do corpo e do fundo.', {1: A}, "Grelina", "Azul."),
]
CARDS = [c for c in CARDS if not c.get("skip")]

EXCLUIDOS = [
 (1482014886764, "Mucosa é a camada mais interna — trivial"),
 (1667459978330, "LLU junção esofagogástrica — imagens não mostram a transição de forma clara"),
 (1667460073729, "LLU fúndico em menor aumento — já presente no card de maior aumento"),
 (1667460314025, "LLU pilórico em menor aumento — idem"),
 (1702213513286, "Histology regiões — lista sob um cloze"),
 (1702217278951, "Histology célula principal (7 clozes) — coberto pelos AnKing"),
 (1482021686946, "Gastrina de células G — FI05 (P2)"),
]

# ---- v3b: calibração pelo card-mirror (29/09): frente factual curta; verso telegráfico ou só imagem.
OVERRIDES = {
 "dente-tecidos": dict(text='<div>No dente, o {{c1::esmalte}} recobre a coroa, o {{c2::cemento}} recobre a raiz e a {{c3::dentina}} forma a maior parte</div>',
                       extra='Polpa: conjuntivo frouxo vascularizado e inervado'),
 "parotida-serosa": dict(extra='Sublingual: mucosa<br>Submandibular: mista, predomínio seroso'),
 "sublingual-mucosa": dict(extra='Parótida: serosa<br>Submandibular: mista, predomínio seroso'),
 "submandibular-mista": dict(extra='Semiluas serosas nas unidades mistas'),
 "lingua-ventral": dict(extra='Dorso: papilas (2/3 anteriores) e tonsila lingual (1/3 posterior)'),
 "mucosa-camadas": dict(extra=f'Muscular da mucosa: limite com a submucosa<br><br>{LAYERS}'),
 "muscular-externa": dict(extra=f'Estômago: + camada oblíqua (a mais interna)<br><br>{LAYERS}'),
 "estomago-obliqua": dict(extra=f'Ordem: oblíqua (interna), circular, longitudinal (externa)<br><br>{OPENSTAX}'),
 "adventicia": dict(extra=f'Serosa quando intraperitoneal<br>Esôfago torácico: adventícia; estômago: serosa<br><br>{LAYERS}'),
 "juncao-esofagogastrica": dict(extra=f'Lado gástrico: fossetas e glândulas<br><br>{J("82605678fa1ed99d7ea5012425fc98d3.webp", "15-14")}'),
 "fundo-corpo-iguais": dict(extra=f'Glândulas com células parietais e principais<br><br>{J("b8647af3199815237f7622aff1f2a0fc.webp", "15-17")}'),
 "cardia-piloro-muco": dict(extra=f'Sem células parietais e principais<br>Cárdia: glândulas enoveladas<br><br>{J("a66ad2c7955fb8ca4c079ca9af584855.webp", "15-21")}'),
 "piloro-fossetas": dict(text='<div>Na região pilórica, as fossetas gástricas são {{c1::profundas}} e as glândulas, curtas e enoveladas</div>',
                         extra=f'Corpo: fossetas rasas, glândulas longas<br><br>{ANTRAL}'),
 "regiao-pilorica-he": dict(extra='Glândulas claras (secretam muco)<br>Fossetas profundas, glândulas curtas'),
 "mucosas-superficiais": dict(extra=f'Epitélio cilíndrico simples<br>Muco espesso, rico em HCO<sub>3</sub><sup>-</sup><br><br>{J("f7b405d94c64b5542191f31360f7f555.webp", "15-16")}'),
 "istmo-celulas-tronco": dict(extra=f'Renovam as mucosas superficiais a cada 4–7 dias<br><br>{J("b8647af3199815237f7622aff1f2a0fc.webp", "15-17")}'),
 "fossetas": dict(extra=f'= fovéolas (células foveolares)<br><br>{OPENSTAX}<br>{ANTRAL}'),
 "parietal-eosinofila": dict(extra=('<div><b>P</b>arietal = <b>P</b>ink (rosa)<br>Predominam no istmo e no colo das glândulas</div>'
                                    '<div>Eosinofilia: muitas mitocôndrias e membranas</div><br>' + HAGG("3b736377bf811a11f71f531e4b04aa5d.webp") + '<br><br>' + JPOGI)),
 "parietal-imagem": dict(text=f'<div>Qual célula está indicada nesta glândula gástrica?</div><br>{JPOGI}<br><div>{{{{c1::Célula parietal}}}}</div>',
                         extra='Grande, eosinófila, núcleo central<br>Istmo e colo das glândulas do corpo/fundo'),
 "parietal-canaliculo": dict(extra=f'Estímulo: túbulo-vesículas fundem-se ao canalículo<br><br>{J("4534b7a2f4a6be49ccb02757d26c2325.webp", "15-18")}'),
 "mucosas-colo": dict(extra=f'Pequenas e claras em HE<br>Muco menos alcalino que o superficial<br><br>{J("b8647af3199815237f7622aff1f2a0fc.webp", "15-17")}'),
 "principal-basofila": dict(extra=('<div>- <u><b>CHIEF</b></u>s need to report at <b><u>BAS</u></b>e <i>(mnemônico em inglês: principais → base, basófilas)</i></div><br>'
                                   '<div>- Secretam pepsinogênio, convertido em pepsina no pH gástrico</div><br>'
                                   '<div>- Basofilia: RER abundante</div><br>'
                                   '<div>- Predominam na <u>base</u> das glândulas</div><br>' + HAGG("f59a172e63351c7e6236cf58efec45bd.png"))),
 "grelina": dict(extra='Células enteroendócrinas (X/A-like) do corpo/fundo'),
}
for c in CARDS:
    c.update(OVERRIDES.get(c["key"], {}))

# ---- v3c: revisão independente de tradução (29/09) — pistas na frente, decalques, absolutos, REG
HAGG_SEM_SETAS = lambda f: (f'<img src="{f}" width="487"><br>' + CR.format(
    'Crédito da imagem: <a href="https://commons.wikimedia.org/wiki/File:Parietal_cell_and_chief_cells.png">Mikael Häggström</a>, CC0, via Wikimedia Commons'))
OVR2 = {
 "lingua-ventral": dict(text='<div>A face ventral (inferior) da língua é lisa, coberta por mucosa de {{c1::revestimento}}, sem papilas</div>'),
 "mucosas-colo": dict(text='<div>Entre as parietais, na porção média das glândulas do corpo, ficam as células {{c1::mucosas do colo}}</div>',
                      extra=f'Secretam muco menos alcalino que o superficial<br>Pequenas e claras em HE<br><br>{J("b8647af3199815237f7622aff1f2a0fc.webp", "15-17")}'),
 "mucosas-superficiais": dict(text='<div>O epitélio que reveste a superfície do estômago e as fossetas é formado pelas células {{c1::mucosas superficiais}}</div>'),
 "piloro-fossetas": dict(text='<div>Na região pilórica, as fossetas gástricas são {{c1::profundas}} e as glândulas, {{c1::curtas}} e enoveladas</div>'),
 "dente-tecidos": dict(text='<div>No dente, o {{c1::esmalte}} recobre a coroa, o {{c2::cemento}} recobre as raízes, e a maior parte do dente é formada por {{c3::dentina}}</div>',
                       extra='Polpa: tecido conjuntivo frouxo vascularizado e inervado'),
 "sublingual-mucosa": dict(text='<div>A {{c1::sublingual}}, a menor das glândulas salivares maiores, é predominantemente mucosa</div>'),
 "parotida-serosa": dict(text='<div>A glândula {{c1::parótida}} tem ácinos exclusivamente serosos, com secreção rica em α-amilase</div>'),
 "fossetas": dict(text='<div>A superfície do <u>estômago</u> é marcada <i>histologicamente</i> por pequenas depressões muito próximas entre si, as {{c1::<b>fossetas</b>}} <b>gástricas</b>, nas quais desembocam várias glândulas gástricas</div>'),
 "regiao-fundica-he": dict(text='Esta é uma&nbsp;<b>imagem em maior aumento</b>&nbsp;da região&nbsp;{{c1::oxíntica/fúndica}} do estômago<br><br><img src="paste-285af7c65716abbec41ced6e635e74ff448f45f5.png" width="590"><br><img src="paste-438815d1674aec9e56d5491223223627e1a70d65.png" width="592"><br><img src="paste-5fd70752adbdef98c597af64c2c4cc55bf70fcd3.png" width="593">'),
 "regiao-pilorica-he": dict(text='Esta é uma <b>imagem em maior aumento</b>&nbsp;da região&nbsp;{{c1::antral/pilórica}} do estômago<br><br><img src="paste-3c60c7c15a904453246835ff33ccaf3d3c6a6c83.png" width="599"><img src="paste-d7c5ef5cd521a3cf957a7db2d65f6b58bfaa2489.png" width="599">'),
 "hpylori-antro": dict(text='<div>O <i>Helicobacter pylori</i> coloniza mais comumente o {{c1::antro::região}} gástrico, sem invadir a mucosa</div>'),
 "principal-basofila": dict(extra=('<div>- <u><b>CHIEF</b></u>s need to report at <b><u>BAS</u></b>e <i>(mnemônico em inglês: principais → base, basófilas)</i></div><br>'
                                   '<div>- Secretam pepsinogênio, convertido em pepsina no pH gástrico</div><br>'
                                   '<div>- Basofilia: retículo endoplasmático granuloso (REG) abundante</div><br>'
                                   '<div>- Predominam na <u>base</u> das glândulas</div><br>' + HAGG_SEM_SETAS("f59a172e63351c7e6236cf58efec45bd.png"))),
 "istmo-celulas-tronco": dict(extra=f'Renovam as células mucosas superficiais a cada 4–7 dias<br><br>{J("b8647af3199815237f7622aff1f2a0fc.webp", "15-17")}'),
 "cardia-piloro-muco": dict(extra=f'Poucas ou nenhuma célula parietal e principal<br>Cárdia: glândulas enoveladas<br><br>{J("a66ad2c7955fb8ca4c079ca9af584855.webp", "15-21")}'),
 "adventicia": dict(extra=f'Serosa quando intraperitoneal<br>Esôfago torácico (fora da cavidade peritoneal): adventícia; estômago: serosa<br><br>{LAYERS}'),
}
import re as _re
for c in CARDS:
    c.update(OVR2.get(c["key"], {}))
    for f in ("text", "extra"):
        c[f] = _re.sub(r"parede do tubo(?! digestório)(</u>)?", lambda m: "parede do tubo digestório" + (m.group(1) or ""), c[f])

# ---- v3d: auditoria de núcleo pelo executor
for c in CARDS:
    if c["key"] in ("submucosa-posicao", "muscular-externa-posicao"):
        c["flags"] = {1: 4}; c["motivo"] = "Azul: ordem das camadas reconstruível pelos verdes da mucosa/muscular externa."
    if c["key"] == "parietal-eosinofila":
        c["flags"] = {1: 3, 2: 4}; c["motivo"] = "c1 verde (critério); c2 inverso azul — representante visual é o card de imagem."
