# Especificação curada da FI05 (run uc08-fi05-20260929a). Material real da pasta FI05: Aula-3 "Digestão e absorção dos nutrientes".
RUN_ID = "uc08-fi05-20260929a"
SHORT = "fi05"
LESSON = "2026-uc08-fisiologia-05-digestao-absorcao-nutrientes"
DECK = "NEBLI::UC08::P2::Fisiologia::Digestão e absorção dos nutrientes"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20260929-CLAUDE-02) + EXECUCAO-DECK-AULA + RECONSTRUCAO-UC08, 29/09/2026"

MEDIA = {
    "nebli-uc08-fi05-s04-carboidratos.png": "fontes/s04.png",
    "nebli-uc08-fi05-s06-lipidios.png": "fontes/s06.png",
    "nebli-uc08-fi05-s07-agua.png": "fontes/s07.png",
    "nebli-uc08-fi05-s12-juncoes.png": "fontes/s12.png",
}
CR = '<br><span style="font-size: 10pt;"><em>{}</em></span>'
SLIDE = lambda f, ref, w=480: f'<img src="{f}" width="{w}">' + CR.format(f"Figure from the lecture slides (Goulart da Silva, UC08 Physiology); {ref}")

def ak(key, src, flags, bloco, alvo, evid, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=evid, uso=kw.pop("uso", "Fisiologia GI; Step 1."), motivo=motivo, **kw)

CARDS = [
 # ---------- CARBOIDRATOS ----------
 ak("amilase-salivar", 1482030269123, {1: 4}, "A-carb", "Amilase salivar inicia o amido", "Slide 4 (boca: amilase)", "Azul."),
 ak("amilase-alfa14", 1482115420919, {1: 3, 2: 4}, "A-carb", "α-amilases quebram ligações α-1,4", "Slide 4 (endoamilase, α[1,4])", "c1 verde; c2 azul.",
    extra_prefix='They cannot cut α-1,6 branch points or the terminal bonds, so they leave maltose, maltotriose and α-limit dextrins for the brush border.<br><br>'),
 ak("amilase-ativa", 1482115442644, {1: 4}, "A-carb", "Amilase pancreática secretada ativa", "Slide 4", "Azul."),
 ak("so-monossacarideos", 1482115408306, {1: 3}, "A-carb", "Só monossacarídeos são absorvidos", "Slide 4 (oligossacaridases da borda em escova)", "Verde (1-HighYield)."),
 dict(key="oligossacaridases", kind="autoral", flags={1: 3}, bloco="A-carb",
  text='Maltose, maltotriose, α-limit dextrins, lactose and sucrose are split into monosaccharides by {{c1::brush-border oligosaccharidases}} (maltase, α-dextrinase, sucrase, lactase)',
  extra='Most starch digestion is intestinal: luminal amylase makes the oligosaccharides, and the enterocyte surface finishes the job.<br><br>' + SLIDE("nebli-uc08-fi05-s04-carboidratos.png", "carbohydrate digestion and absorption", 520),
  alvo="Oligossacaridases da borda em escova", evid="Slide 4", uso="Intolerância à lactose; inibidores de α-glicosidase.", motivo="Verde.",
  busca="AnKing tem lactase e trealase isoladas; nenhum card do conjunto; lacuna."),
 ak("sglt1", 1482115445612, {1: 3}, "A-carb", "Glicose/galactose entram por SGLT1", "Slide 4", "Verde."),
 ak("sglt1-quais", 1482115451005, {1: 4}, "A-carb", "SGLT1 = glicose e galactose", "Slide 4", "Azul (par de recuperação inversa)."),
 ak("glut5", 1482115460996, {1: 3}, "A-carb", "Frutose entra por GLUT5", "Slide 4", "Verde."),
 ak("glut2", 1482115455383, {1: 3}, "A-carb", "Saída basolateral por GLUT2", "Slide 4", "Verde."),
 ak("glut2-quais", 1482115473217, {1: 4}, "A-carb", "GLUT2 = glicose, galactose, frutose", "Slide 4", "Azul."),
 # ---------- PROTEÍNAS ----------
 ak("pepsina-inicio", 1482115484108, {1: 3}, "B-prot", "Digestão proteica começa com pepsina", "Slide 5 (estômago: pepsina 10–15%)", "Verde (1-HighYield)."),
 ak("zimogenios", 1482115500165, {1: 4}, "B-prot", "Proteases pancreáticas secretadas inativas", "Slide 5", "Azul."),
 ak("tripsinogenio", 1482115490061, {1: 3}, "B-prot", "1º passo: tripsinogênio → tripsina", "Slide 5", "Verde."),
 ak("enteropeptidase", 1482115492876, {1: 3}, "B-prot", "Enteropeptidase ativa o tripsinogênio", "Slide 5", "Verde."),
 ak("tripsina-ativa-todas", 1482115504921, {1: 3}, "B-prot", "Tripsina ativa todas as proenzimas", "Slide 5", "Verde."),
 ak("tripsina-autocatalise", 1482115525140, {1: 4}, "B-prot", "Tripsina ativa mais tripsinogênio", "Slide 5 (T+)", "Azul."),
 ak("quimotripsinogenio", 1482115509710, {1: 4}, "B-prot", "Quimotripsinogênio → quimotripsina", "Slide 5", "Azul."),
 ak("proelastase", 1482115513922, {1: 4}, "B-prot", "Pró-elastase → elastase", "Slide 5", "Azul."),
 ak("procarboxipeptidase", 1482115518484, {1: 4}, "B-prot", "Pró-carboxipeptidase → carboxipeptidase", "Slide 5", "Azul."),
 ak("cck-enzimas", 1482115334134, {1: 3}, "B-prot", "CCK estimula o componente enzimático pancreático", "Slide 5 (produtos proteicos → CCK → suco pancreático)", "Verde."),
 ak("pept1", 1482115537298, {1: 3}, "B-prot", "Di/tripeptídeos entram com H+ (PEPT1)", "Slide 5", "Verde."),
 ak("aa-na", 1482115532737, {1: 4}, "B-prot", "Aminoácidos entram com Na+", "Slide 5", "Azul."),
 ak("enteropeptidase-deficiencia", 1521768510367, {1: 4}, "B-prot", "Deficiência de enteropeptidase", "Slide 5", "Azul: aplicação.", uso="Clínica direta (Q044)."),
 # ---------- LIPÍDIOS ----------
 ak("lipase-lingual", 1482030273275, {1: 4}, "C-lip", "Lipase lingual", "Slide 6 (boca)", "Azul."),
 ak("lipases-pancreaticas", 1482115541696, {1: 3}, "C-lip", "Lipases pancreáticas digerem a gordura", "Slide 6", "Verde.",
    extra_prefix='Bile salts first emulsify the fat, giving the lipases a large surface to work on.<br><br>'),
 ak("lipase-ph", 1482115547887, {1: 4}, "C-lip", "Lipase pancreática inativada por pH baixo", "Slides 6, 9 (HCO3– do suco pancreático)", "Azul."),
 ak("micelas-bile", 1482115554891, {1: 3}, "C-lip", "Ácidos biliares formam micelas", "Slide 6", "Verde."),
 ak("micelas-borda", 1482115562039, {1: 3}, "C-lip", "Micelas levam os lipídios à borda em escova", "Slide 6", "Verde."),
 ak("reesterificacao", 1482115566901, {1: 4}, "C-lip", "Reesterificação no enterócito", "Slides 6, 10", "Azul."),
 ak("quilomicrons", 1482115570847, {1: 3}, "C-lip", "Quilomícrons (lipídios + apolipoproteínas)", "Slide 6 (QMC → linfa)", "Verde."),
 dict(key="cck-lipidios", kind="autoral", flags={1: 3}, bloco="C-lip",
  text='Fatty acids and monoglycerides in the duodenum stimulate {{c1::CCK}}, which triggers gallbladder contraction and pancreatic enzyme secretion',
  extra='Bile salts emulsify the fat and pancreatic lipases digest it; this links the arrival of fat to the release of the tools to handle it.<br><br>' + SLIDE("nebli-uc08-fi05-s06-lipidios.png", "lipid digestion and absorption", 480),
  alvo="CCK coordena bile + suco pancreático diante de lipídios", evid="Slide 6 (CCK → liberação de suco pancreático e biliar)", uso="Colecistite; esteatorreia.",
  motivo="Verde.", busca="AnKing CCK/vesícula e CCK/enzimas separados; ligação com lipídios ausente; lacuna."),
 # ---------- ÍONS, ÁGUA, HCO3 ----------
 dict(key="agua-volumes", kind="autoral", flags={1: 3, 2: 4}, bloco="D-agua",
  text=('About 9 L of fluid enter the gut each day (≈2 L ingested plus secretions); most is absorbed in the {{c1::small intestine}}, and the colon absorbs about {{c2::1.4 L}}'),
  extra=('Water follows solute: absorption is driven by Na⁺ transport (Na⁺–glucose/galactose/amino acid cotransport, Na⁺–Cl⁻ cotransport, Na⁺/H⁺ exchange by NHE3, and ENaC in the distal colon), '
         'with the basolateral Na⁺/K⁺-ATPase keeping cell Na⁺ low. Loss of NHE3 causes diarrhea.<br><br>' + SLIDE("nebli-uc08-fi05-s07-agua.png", "absorption of ions and water", 480)),
  alvo="Balanço hídrico intestinal e absorção de Na⁺/água", evid="Slide 7 (volumes; 7,5 L proximal, 1,4 L distal; transportadores)", uso="Diarreias.",
  motivo="c1 verde; c2 azul.", busca="AnKing só K⁺ e cAMP/Cl⁻; lacuna."),
 ak("k-delgado", 1482115592577, {1: 4}, "D-agua", "K+ absorvido passivamente no delgado", "Slide 7 (paracelular)", "Azul."),
 ak("k-colon", 1482115594816, {1: 4, 2: 4}, "D-agua", "K+ secretado no cólon", "Slide 7", "Azul."),
 ak("hco3-ductal", 1482115316095, {1: 4}, "D-agua", "Ductos pancreáticos secretam HCO3-", "Slide 9 (suco pancreático, anidrase carbônica)", "Azul (secreção detalhada é P2 secreções)."),
 # ---------- FERRO E CÁLCIO ----------
 ak("ferro-fe2-duodeno", 1482115585152, {1: 3, 2: 3}, "E-minerais", "Ferro absorvido como Fe2+ no duodeno", "Slide 9", "Verde (1-HighYield)."),
 ak("ferro-heme", 1476661053401, {1: 4, 2: 4}, "E-minerais", "Heme absorvido pelo transportador de heme", "Slide 9 (HCP-1)", "Azul."),
 ak("ferro-dcytb", 1476661061176, {1: 4, 2: 4}, "E-minerais", "Fe3+ → Fe2+ pelo citocromo b (Dcytb)", "Slide 9", "Azul.",
    extra_prefix='Antacids, gastric acid inhibitors and caffeine reduce iron absorption (lecture).<br><br>'),
 ak("ferro-dmt1", 1476661066773, {1: 3}, "E-minerais", "DMT1 capta Fe2+", "Slide 9", "Verde."),
 ak("ferroportina", 1476661073431, {1: 3}, "E-minerais", "Ferroportina exporta Fe2+", "Slide 9", "Verde."),
 ak("hepcidina", 1476661104838, {1: 3, 2: 3, 3: 3}, "E-minerais", "Hepcidina inibe a ferroportina", "Slide 9 (controle sistêmico)", "Verde (1-HighYield)."),
 ak("hepcidina-sobe", 1525915981730, {1: 4}, "E-minerais", "Ferro alto e inflamação ↑ hepcidina", "Slide 9", "Azul."),
 ak("hepcidina-desce", 1525916402432, {1: 4}, "E-minerais", "Hipóxia/eritropoese ↓ hepcidina", "Slide 9", "Azul."),
 ak("ferritina", 1478834050609, {1: 4}, "E-minerais", "Ferritina armazena ferro", "Slide 9 (ferritina no enterócito)", "Azul."),
 ak("calcio-calbindina", 1462146169234, {1: 3}, "E-minerais", "Calcitriol ↑ absorção intestinal de Ca2+ via calbindina", "Slide 9 (vitamina D, Ca2+/calbindina)", "Verde."),
 ak("calcitriol-intestino", 1494989429488, {1: 4}, "E-minerais", "Calcitriol ↑ absorção de Ca2+ e fosfato", "Slide 9", "Azul."),
 # ---------- VITAMINAS ----------
 ak("lipossoluveis", 1476583124449, {1: 3, 2: 4}, "F-vit", "Vitaminas lipossolúveis dependem de íleo, pâncreas e bile", "Slide 10 (A, D, E, K → quilomícrons → linfa)", "c1 verde; c2 azul."),
 ak("vitk-rn-hemorragia", 1476584046114, {1: 3}, "F-vit", "Deficiência de vitamina K → hemorragia neonatal", "Slide 10 ('RN não tem vitamina K… risco de hemorragia')", "Verde (1-HighYield)."),
 ak("b12-r-binder", 1476661138357, {1: 4, 2: 4}, "F-vit", "B12 ligada à haptocorrina (R-binder) salivar", "Slide 10", "Azul."),
 ak("b12-proteases", 1476661144103, {1: 3, 2: 3}, "F-vit", "Proteases pancreáticas liberam B12 → fator intrínseco", "Slide 10", "Verde."),
 ak("b12-ileo-terminal", 1482115590320, {1: 3}, "F-vit", "B12 absorvida no íleo terminal", "Slide 10", "Verde (HY)."),
 ak("b12-receptor-ileo", 1476661158569, {1: 4}, "F-vit", "Complexo IF–B12 endocitado no íleo terminal", "Slide 10", "Azul."),
 ak("b12-transcobalamina", 1476661164427, {1: 4}, "F-vit", "Transcobalamina II no enterócito", "Slide 10", "Azul."),
 ak("b12-pancreatite", 1478898351508, {1: 3}, "F-vit", "Insuficiência pancreática → déficit de B12", "Slide 10 (pancreatite)", "Verde.", uso="Clínica direta (Q044)."),
 ak("fi-gastrectomia", 1482115259111, {1: 3}, "F-vit", "Fator intrínseco é a única secreção gástrica essencial", "Slide 10 (gastrectomia)", "Verde."),
 ak("folato-jejuno", 1476583684909, {1: 4}, "F-vit", "Folato absorvido no jejuno", "Slide 10 (complexo B)", "Azul."),
 ak("vitd-figado", 1494988708228, {3: 4}, "F-vit", "25-hidroxilação no fígado", "Slide 10 (síntese de vitamina D)", "Azul."),
 ak("vitd-rim", 1475704481414, {1: 4}, "F-vit", "1α-hidroxilação no túbulo proximal", "Slide 10", "Azul."),
 # ---------- JUNÇÕES / PARACELULAR ----------
 ak("tight-junctions", 1488502340989, {1: 4}, "G-paracel", "Junções oclusivas: claudinas e ocludinas", "Slide 12", "Azul."),
 dict(key="claudinas-mlck", kind="autoral", flags={1: 4, 2: 4}, bloco="G-paracel",
  text=('Claudins 2 and 15 form paracellular {{c1::Na⁺}} channels in the small intestine; after a meal, SGLT1 activity triggers {{c2::MLCK}}, contracting the perijunctional actomyosin ring and opening tight junctions'),
  extra=('Recycled Na⁺ feeds Na⁺-coupled nutrient uptake, and the widened paracellular path lets water and small solutes follow; mice lacking claudins 2 and 15 die of malabsorption.<br><br>'
         + SLIDE("nebli-uc08-fi05-s12-juncoes.png", "post-absorptive × post-prandial tight junctions", 460)),
  alvo="Via paracelular e sua regulação pós-prandial", evid="Slides 11–12", uso="Barreira intestinal; diarreia.", motivo="Azul: ponto de pesquisa ensinado.",
  busca="AnKing só composição das junções; lacuna."),
]

COMPARTILHADOS = {
    1790708472160: "BT04 · lactase na borda em escova — slide 4",
    1790708472385: "BT04 · quilomícrons → lácteos — slide 6",
    1790715095282: "AN07 · quilomícrons → ducto torácico — slide 6",
    1790690380535: "BT03 · pepsinogênio → pepsina com H+ — slide 5",
    1790688796763: "BT03 · principal → pepsinogênio e lipase gástrica — slides 5–6",
    1790265245246: "UC03 · vitamina K no recém-nascido (bactérias do cólon) — slide 10",
}

EXCLUIDOS = [
 (1482115437677, "Trealase — fora do slide"),
 (1482115477908, "Teste da D-xilose — clínica diagnóstica lateral"),
 (1482115481615, "D-xilose urinária — idem"),
 (1476661171372, "Transcobalamina II → medula/fígado — além do slide"),
 (1482115326502, "Secretina estimula HCO3- — aula de secreções (P2)"),
 (1482115609366, "cAMP e canais de Cl- — secreção intestinal"),
 (1482030234278, "Composição salivar (várias notas) — aula de secreções"),
 (1476661113645, "Ferritina hepática — redundante"),
]
FORA_DO_RECORTE = [
 "Secreção gástrica, pancreática e biliar em detalhe: a pasta FI05 só tem esta aula de digestão/absorção; aula de secreções ainda não localizada (pendência P2)",
 "Estudo de permeabilidade do equinacosídeo (slide 3): ilustração de pesquisa — só a ideia 'jejuno absorve mais'",
 "Amplificação da superfície (3×/10×/20×, slide 2): coberta na BT04",
]
