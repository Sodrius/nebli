RUN_ID = "uc03-pat05-refacao-20261004"
SHORT = "pat05"
LESSON = "2026-uc03-patologia-23-edema-congestao"
DECK = "NEBLI::UC03::P2::Patologia::Edema e congestão"
CRITERIOS = "MEMORY.md + F-20261004-CODEX-05; inventário atômico e fontes completas antes da seleção"
MEDIA = {f"nebli-pat05-refacao-s{n:02d}.png": f"visual-slide-{n:02d}.png" for n in range(2, 17)}
V, Z, R = 3, 4, 5
BUSCA = "AnKing Step e acervos externos: busca/ext.json; consultas por edema, transudate, exudate, hydrostatic pressure, oncotic pressure, lymphatic obstruction, hyperemia, congestion, anasarca, ascites, hydrothorax, hydropericardium e pulmonary edema em 04/10. "

def ak(key, src, flags, bloco, alvo, slide, motivo, **kw):
    image = f'<br><img src="nebli-pat05-refacao-s{slide:02d}.png">' if isinstance(slide, int) and 2 <= slide <= 16 else ""
    kw.setdefault("extra", f"- In this lesson, use this card for {alvo.lower()} on slide {slide}.{image}")
    if image and image not in kw["extra"]:
        kw["extra"] += image
    return dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo,
                slide_sem_alternativa="a figura original do slide é a evidência visual ensinada nesta aula", **kw)

def au(key, text, flags, bloco, alvo, slide, espelhos, motivo, extra=""):
    image = f'<br><img src="nebli-pat05-refacao-s{slide:02d}.png">' if isinstance(slide, int) and 2 <= slide <= 16 else ""
    extra = extra or f"- In this lesson, this term identifies {alvo.lower()} on slide {slide}.{image}"
    if image and image not in extra:
        extra += image
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria="central",
                busca=BUSCA+"nenhum card recuperável com este termo anatômico da aula.", espelhos=espelhos, motivo=motivo,
                slide_sem_alternativa="a figura original do slide é a evidência visual ensinada nesta aula")

A,B,C,D = "A-definicoes", "B-forcas", "C-mecanismos", "D-morfologia"
CARDS = [
au("edema", "Edema is an abnormal accumulation of fluid in the {{c1::interstitial}} space", {1:V}, A, "Definição de edema", 3, [1474746760064,1474746809538], "Verde: conceito central de toda a aula."),
au("hidrotorax", "Fluid accumulating in the pleural cavity is called {{c1::hydrothorax}}", {1:Z}, A, "Hidrotórax", 2, [1474503771577,1495736334643], "Azul: definição explícita nos objetivos."),
au("hidropericardio", "Fluid accumulating in the pericardial cavity is called {{c1::hydropericardium}}", {1:Z}, A, "Hidropericárdio", 2, [1474503771577,1514512820505], "Azul: definição explícita nos objetivos."),
ak("ascite",1576690231792,{1:V},A,"Ascite",2,"Verde: termo recorrente em prova e aula.",text="Right-sided heart failure may cause {{c1::<i>ascites</i>}} through systemic venous congestion"),
au("anasarca", "Generalized severe subcutaneous edema is called {{c1::anasarca}}", {1:Z}, A, "Anasarca", 2, [1496606992901,1475363769043], "Azul: definição explícita nos objetivos."),
ak("hiperemia-ativa",1471468263016,{1:V},A,"Hiperemia ativa",3,"Verde: entrada arterial aumentada distingue hiperemia de congestão.",extra="- Active arteriolar vasodilation increases flow in response to local metabolic demand"),
ak("hiperemia-reativa",1471468271265,{1:Z},A,"Hiperemia reativa",3,"Azul: ilustra aumento ativo do fluxo após isquemia breve."),
au("congestao", "Congestion is passive accumulation of blood caused by impaired {{c1::venous outflow}}", {1:V}, A, "Congestão passiva",3,[1471914938644,1577916403894],"Verde: contraste central com hiperemia."),
ak("starling",1471466751292,{1:V},B,"Forças de Starling",4,"Verde: equação organiza o balanço de fluidos mostrado na lâmina."),
ak("oncotica",1471466733838,{1:V},B,"Pressão oncótica por proteínas",4,"Verde: albumina mantém a força que retém líquido intravascular."),
ak("filtracao",1471466778315,{1:Z},B,"Filtração capilar",4,"Azul: fluxo líquido para o interstício."),
ak("reabsorcao",1471466782113,{1:Z},B,"Reabsorção capilar",4,"Azul: fluxo líquido de volta ao capilar."),
ak("linfa-retorno",1471466870844,{1:V},B,"Drenagem linfática",4,"Verde: dreno final do excedente filtrado."),
ak("transudato-proteina",1474503781327,{1:V,2:Z},B,"Transudato tem baixa proteína",5,"Verde: distinção de prova; azul: tipo de derrame."),
ak("exsudato-proteina",1474512820505,{1:V,2:Z},B,"Exsudato tem alta proteína",5,"Verde: distinção de prova; azul: tipo de derrame."),
ak("hidrostatica",1471915101703,{1:V},C,"Edema por pressão hidrostática",6,"Verde: mecanismo maior da aula e prova."),
ak("insuficiencia-esquerda",1522350837813,{1:V,2:V},C,"Falência esquerda causa edema pulmonar",8,"Verdes: mecanismo e manifestação pulmonar do slide."),
ak("insuficiencia-esquerda-congestao",1471914938644,{1:V},C,"Falência esquerda causa congestão pulmonar",8,"Verde: fixa o território que precede o ventrículo esquerdo."),
ak("insuficiencia-direita",1471914999950,{1:V},C,"Falência direita causa congestão sistêmica",8,"Verde: corrige a distinção de territórios no circuito de insuficiência cardíaca."),
ak("disfuncao-bomba",1471911062062,{1:Z},C,"Disfunção de bomba combina congestão e baixa perfusão",8,"Azul: frase integradora que liga a congestão à ativação renal mostrada no slide."),
ak("sodio-agua",1521169448163,{1:V},C,"Retenção de sódio e água",9,"Verde: mecanismo que agrava o edema."),
ak("sindrome-nefrotica",1475363769043,{1:V,2:Z,3:Z},C,"Síndrome nefrótica e hipoalbuminemia",10,"Verde: proteína plasmática baixa; azuis: manifestação e resposta renal.",extra="- Protein loss lowers plasma oncotic pressure\n- Renal sodium retention can be primary or secondary and worsens edema"),
ak("cirrose-edema",1486522767302,{1:V},C,"Cirrose com edema por hipoalbuminemia",11,"Verde: exemplo direto de pressão oncótica reduzida."),
ak("linfedema",1521170206006,{1:V},C,"Obstrução linfática causa edema",12,"Verde: quinto mecanismo da aula.",extra="- Lymphatic drainage normally returns excess interstitial fluid and proteins to the circulation"),
ak("permeabilidade",1473548436921,{1:V,2:Z},C,"Exsudato por permeabilidade aumentada",13,"Verde: mecanismo inflamatório cobrado; azul: localização alveolar de exemplo."),
ak("congestao-hepatica",1577916403894,{1:V},D,"Congestão hepática passiva",14,"Verde: correlação morfológica da congestão.",extra="- Right heart failure is a common cause, but hepatic venous outflow obstruction can also produce passive congestion"),
ak("congestao-centrolobular",1486591317696,{1:V},D,"Congestão lesa a zona centrolobular",14,"Verde: mecanismo morfológico que sustenta o padrão hepático do slide."),
ak("obstrucao-veia-hepatica",1486591304104,{1:V,2:Z},D,"Obstrução venosa produz congestão hepática",14,"Verde: mecanismo; azul: exemplo anatômico sem abrir uma aula de Budd-Chiari."),
ak("edema-dependente",1471915101703,{1:V},D,"Edema dependente com cacifo",14,"Verde: sinal morfológico de alta prioridade, explícito no Robbins e no exercício."),
ak("celulas-insuficiencia-cardiaca",1471914979068,{1:V,2:Z,3:Z},D,"Macrófagos com hemossiderina na congestão pulmonar crônica",15,"Verde: morfologia central; azuis: nome e localização."),
au("figado-noz-moscada", "Chronic passive hepatic congestion produces a {{c1::nutmeg}} liver", {1:Z}, D, "Fígado em noz-moscada", 15, [1577916403894,1486591317696], "Azul: morfologia da congestão hepática no slide e no Robbins.", extra="- Centrilobular congestion and hepatocyte injury create the mottled gross appearance"),
ak("edema-pulmonar-rx",1555363764010,{1:Z},D,"Edema pulmonar na radiografia",9,"Azul: reconhecimento da morfologia radiológica.",extra="- The chest radiograph in slide 9 illustrates pulmonary edema with bilateral opacity and accompanying pleural fluid."),
ak("gradiente-hidrostatico-capilar",1471466831564,{1:V},B,"Gradiente de pressão hidrostática ao longo do capilar",4,"Verde: explica a direção da filtração no esquema de Starling."),
ak("kf-permeabilidade-capilar",1471466790491,{1:Z},B,"Coeficiente de filtração como permeabilidade da parede capilar",4,"Azul: completa o diagrama de troca capilar sem importar fisiologia fora da aula."),
ak("edema-pulmonar-venoso",1471914969111,{1:V,2:Z},D,"Hipertensão venosa pulmonar produz edema pulmonar",9,"Verde: mecanismo da morfologia pulmonar; azul: manifestação associada."),
ak("permeabilidade-exsudato",1474503784942,{1:V,2:Z},C,"Derrame exsudativo por permeabilidade vascular aumentada",12,"Verde: conecta barreira lesada e proteína; azul: aplicação em cavidade serosa."),
ak("lesao-alveolocapilar",1473707295145,{1:V},C,"Lesão da interface alvéolo-capilar aumenta sua permeabilidade",12,"Verde: mecanismo mostrado no esquema de barreira lesada."),
ak("membrana-hialina",1473707313998,{1:V},D,"Membrana hialina após extravasamento de fluido rico em proteína",12,"Verde: morfologia específica do dano grave da barreira."),
ak("hipertensao-portal-cirrose",1486522667060,{1:V},C,"Hipertensão portal na cirrose",11,"Verde: parte do mecanismo de ascite mostrado na cascata."),
ak("raas-insuficiencia-cardiaca",1471914992993,{1:V},C,"Baixa perfusão renal ativa RAAS na falência esquerda",8,"Verde: elo central do ciclo de retenção do slide."),
ak("raas-agrava-edema",1576685673761,{1:V},C,"RAAS e ADH agravam edema na insuficiência cardíaca",8,"Verde: fecha o ciclo de retroalimentação do slide."),
ak("ascite-portal",1486522681611,{1:V},C,"Hipertensão portal leva à ascite",11,"Verde: relação direta entre pressão portal e coleção peritoneal."),
ak("permeabilidade-capilar-edema",1471466900946,{1:V},C,"Permeabilidade capilar aumentada causa edema",12,"Verde: mecanismo da barreira lesada."),
ak("lesao-capilar-kf",1471466916768,{1:V},C,"Lesão capilar aumenta o coeficiente de filtração",12,"Verde: relaciona dano endotelial ao aumento de filtração."),
ak("hipertensao-venosa-pulmonar",1472058995902,{1:V},D,"Pressão atrial esquerda elevada congestiona pulmão",9,"Verde: exemplo de elevação retrógrada da pressão venosa pulmonar."),
ak("nutmeg-direita",1471915035278,{1:Z},D,"Falência direita causa fígado em noz-moscada",11,"Azul: correlação etiológica com a morfologia hepática."),
ak("linfedema-obstrucao",1521170206006,{1:V},C,"Obstrução linfática produz edema",7,"Verde: explica membro edemaciado por falha de drenagem."),
ak("transudato-hidrostatica",1474503768203,{1:V,2:Z},C,"Hidrostática aumentada produz transudato",6,"Verde: mecanismo; azul: composição do derrame."),
ak("edema-proteico-ards",1473707300427,{1:V},C,"Lesão da barreira pulmonar produz edema rico em proteína",12,
   "Verde: contrasta com o edema cardiogênico transudativo."),
ak("histamina-permeabilidade",1474571630796,{1:V},C,"Histamina aumenta a permeabilidade vascular no edema inflamatório",12,"Verde: mediador precoce cobrado em exercício e prova."),
ak("bradicinina-permeabilidade",1487640236977,{1:Z},C,"Bradicinina causa vasodilatação e aumento da permeabilidade",12,"Azul: mediador precoce da resposta vascular."),
ak("leucotrienos-permeabilidade",1487640108934,{1:R},C,"Leucotrienos mantêm aumento de permeabilidade no edema inflamatório",12,
   "Rosa: a lâmina 13 só cita leucotrienos entre os produtos dos neutrófilos; o tipo (C4–E4) é detalhe."),
au("morfologia-pulmonar-s13", '<img src="nebli-pat05-refacao-s15.png"><br>Protein-rich alveolar exudate with {{c1::hyaline membranes}} marks edema from increased permeability', {1:V}, D,
   "Reconhecer edema por permeabilidade (exsudato, membranas hialinas) no corte da lâmina 15",15,[1471914969111,1473707295145],"Verde: contraste da monitoria (hidrostático = transudato pálido; permeabilidade = exsudato e membranas hialinas).",
   extra="Many cells and hyaline membranes at the alveolar walls, unlike the pale, cell-poor fluid of hydrostatic edema"),
au("morfologia-pulmonar-s14", '<img src="nebli-pat05-refacao-s14.png"><br>Pale, cell-poor fluid filling alveoli around engorged septal capillaries is {{c1::hydrostatic}} pulmonary edema', {1:V}, D,
   "Reconhecer edema hidrostático (transudato) com congestão no corte da lâmina 14",14,[1471914938644,1471914979068],"Verde: imagem da monitoria (líquido pobre e claro, capilares dilatados).",
   extra="Congested capillaries hold the blood; the alveoli hold the transudate"),
au("morfologia-pulmonar-s09", '<img src="nebli-pat05-refacao-s09.png"><br>Foamy fluid on the cut surface of this lung indicates {{c1::pulmonary edema}}', {1:Z}, D,
   "Reconhecer edema pulmonar na macroscopia do slide 9",9,[1471914969111,1522350837813],"Azul: reconhecimento macroscópico mostrado diretamente na aula.",
   extra="Elevated pulmonary venous pressure drives fluid into the lung, making it heavy and wet on section."),
au("contracao-endotelial", "In acute inflammatory edema, histamine opens postcapillary venules through {{c1::endothelial contraction}}", {1:V}, C,
   "Contração endotelial nas vênulas pós-capilares aumenta permeabilidade",12,[1474571630796,1487640326189],
   "Verde: mecanismo diretamente cobrado na P2 de 2025.",
   extra="Histamine and bradykinin act within minutes; larger endothelial gaps permit plasma proteins to leave and form an exudate."),
ak("retencao-renal-primaria",1496607648594,{1:V},C,"Retenção renal primária de sódio por dano glomerular",10,
   "Verde: no mecanismo primário, a queda da filtração renal inicia a retenção; não é resposta à hipoalbuminemia."),
ak("nefrite-retencao-sal",1475376396532,{1:V,2:Z,3:Z},C,"Síndrome nefrítica: retenção de sal, edema e hipertensão",10,
   "Verde: ancora a retenção renal primária em sua apresentação clínica; azuis: consequências diretas no exercício."),
ak("nefrite-versus-nefrotica",1555536071965,{1:Z},C,"Distinguir edema da síndrome nefrítica por retenção de sódio",10,
   "Azul: a aula contrasta retenção renal primária com hipoalbuminemia da síndrome nefrótica."),
ak("psgn-edema",1475376433919,{1:V},C,"Edema na glomerulonefrite pós-estreptocócica",10,
   "Verde: exemplo clínico direto de redução da filtração e retenção de sódio descrito no exercício."),
ak("nefrite-aguda-anasarca",1496606992901,{1:Z},C,"Síndrome nefrítica aguda como causa de anasarca e edema pulmonar",10,
   "Azul: integra a expansão de volume renal às formas graves de edema ilustradas na aula."),
au("neutrofilos-lesao-alveolar", "In diffuse alveolar damage, recruited neutrophils release proteases and reactive oxygen species that injure the {{c1::alveolar-capillary barrier}}", {1:V}, C,
   "Neutrófilos lesam a barreira alvéolo-capilar no dano alveolar difuso",12,[1473548462128,1473707295145],
   "Verde: fecha a sequência agente lesivo, neutrófilo, barreira rompida e edema rico em proteína do exercício.",
   extra="The exercise links neutrophil degranulation to endothelial and pneumocyte injury. Once that barrier is damaged, protein-rich plasma enters the alveolus and can form hyaline membranes."),
ak("vasodilatacao-esplancnica",1581191946613,{1:V},C,"Vasodilatação arterial esplâncnica diminui volume arterial efetivo na cirrose",11,
   "Verde: primeiro elo causal da cascata de ascite no slide."),
ak("raas-cirrose",1581193044398,{1:V},C,"Cirrose ativa RAAS por redução do volume circulante efetivo",11,
   "Verde: liga vasodilatação esplâncnica à retenção renal de sódio."),
ak("empiema",1474503790995,{1:Z,2:R},A,"Empiema (piema): pus na pleura",3,"Azul: termo da monitoria para exsudato purulento na cavidade pleural."),
au("derrame", "Edema fluid that collects in a body cavity rather than the interstitium is called an {{c1::effusion}}", {1:Z}, A, "Derrame em cavidade", "6; apostila veteranos aula 6; monitoria P1", [1474503771577,1474503781327],
   "Azul: apostila e monitoria (derrame pleural, pericárdico, peritoneal).", extra="- Blood in a cavity: hemothorax, hemopericardium, hemoperitoneum"),
au("edema-generalizado", "Edema from low plasma oncotic pressure is {{c1::generalized}}, whereas edema from venous obstruction is localized", {1:V}, C, "Oncótico generalizado × hidrostático localizado", "5; monitoria P1; apostila veteranos aula 6", [1475363769043,1471915101703],
   "Verde: contraste explícito da monitoria e da apostila.", extra="- Generalized edema settles in the legs over the day because of gravity"),
au("ducto-toracico", "Lymph returns to the blood through the {{c1::thoracic duct}}, which drains into the left subclavian vein", {1:R}, B, "Ducto torácico", 4, [1471466870844,1474503795880],
   "Rosa: rótulo do esquema da lâmina 4.", extra="- Lymph from most of the body ends there"),
ak("filariose",1509920166742,{1:Z,2:R},C,"Elefantíase por linfedema crônico (filariose)",7,"Azul: linfedema crônico (apostila); rosa: o parasita."),
au("linfedema-mastectomia", "Removal of axillary lymph nodes during breast cancer surgery can cause {{c1::lymphedema}} of the arm", {1:Z}, C, "Linfedema iatrogênico", 7, [1521170206006,1509920166742],
   "Azul: exemplo iatrogênico da apostila (mastectomia).", extra="- Iatrogenic: a complication of treatment, not necessarily an error"),

ak("hepatorrenal",1486522693430,{1:Z},C,"Síndrome hepatorrenal",11,"Azul: último quadro da cascata da lâmina 11."),
ak("pbe",1486591357720,{1:R},C,"Peritonite bacteriana espontânea na ascite",11,"Rosa: monitoria (translocação bacteriana no hepatopata soma permeabilidade)."),
ak("mixedema",1462223793144,{1:Z,2:V,3:Z},C,"Mixedema (hipotireoidismo)",7,"Verde c2 (HY 1): mixedema na Edema II (lâmina 19); azuis: GAG e hipotireoidismo."),
au("edema-mole-duro", "Transudate gives a soft, {{c1::pitting}} edema that shifts with gravity, whereas inflammatory exudate gives a firmer edema", {1:Z}, C, "Edema mole (cacifo) × duro", "7; Edema II 18", [1471915101703,1474512820505],
   "Azul: quadro transudato × exsudato da Edema II.", extra="- Exudate is richer in protein and cells, so the tissue is more viscous"),
ak("light",1495890671464,{1:Z},B,"Critério de Light: proteína pleural/sérica > 0,5",6,"Azul: análise do derrame pleural (Edema II, lâmina 22)."),
au("gsaa", "A serum-ascites albumin gradient of 1.1 g/dL or more points to {{c1::portal hypertension}}", {1:R}, C, "Gradiente soro-ascite de albumina", "12; Edema II 27", [1486522681611,1486591357720],
   "Rosa: avaliação laboratorial da ascite (Edema II).", extra="- The fluid is also checked for color, cell count, protein, LDH, glucose, amylase and AFB"),
au("underfill-overflow", "Cirrhotic ascites is explained by the {{c1::underfill}} theory (low effective volume) and the overflow theory (primary sodium retention), neither of which fits alone", {1:R}, C, "Teorias da ascite na cirrose", "12; Edema II 24–25", [1581191946613,1581193044398],
   "Rosa: discussão da Edema II.", extra="- RAAS and vasopressin rise, which overflow alone would not predict"),
au("edema-horario", "Edema worse in the {{c1::morning}}, around the eyes, suggests low oncotic pressure, while evening edema of the legs suggests a gravitational cause", {1:V}, D, "Anamnese: horário e localização", "16; Edema II 30", [1471915101703,1475363769043],
   "Verde: anamnese da Edema II (matutino = oncótico; vespertino = gravitacional).", extra="- The face swells first because its subcutaneous tissue is loose<br>- Fast onset suggests trauma; heart failure worsens over time"),
au("estase-jugular", "On examination, jugular venous {{c1::distension}} points to systemic venous congestion", {1:R}, D, "Exame físico: estase jugular", "16; Edema II 37", [1471914999950,1471447248110],
   "Rosa: último item do exame físico da Edema II.", extra="- Also check pitting, inflammatory signs, cavity effusions and heart and lung sounds"),
ak("cardiogenico-versus-permeabilidade",1532735591750,{1:V},C,
   "Comparar edema pulmonar cardiogênico e não cardiogênico pelo mecanismo",12,
   "Verde: une as duas imagens pulmonares por hidrostática versus permeabilidade."),
]
CARDS = [c for c in CARDS if c["key"] not in {
    "hiperemia-reativa", "permeabilidade", "obstrucao-veia-hepatica",
    "edema-dependente", "linfedema", "figado-noz-moscada",
    "kf-permeabilidade-capilar", "lesao-capilar-kf", "congestao-centrolobular",
    "starling", "psgn-edema", "nefrite-aguda-anasarca", "hipertensao-venosa-pulmonar"
}]
SLIDES = {
    "congestao-hepatica": 12, "nutmeg-direita": 12, "lesao-alveolocapilar": 13, "membrana-hialina": 13,
    "neutrofilos-lesao-alveolar": 13, "permeabilidade-capilar-edema": 13, "permeabilidade-exsudato": 13, "edema-proteico-ards": 13,
    "cardiogenico-versus-permeabilidade": 13, "histamina-permeabilidade": 13, "bradicinina-permeabilidade": 13,
    "leucotrienos-permeabilidade": 13, "contracao-endotelial": 13,
    "transudato-proteina": 6, "exsudato-proteina": 13,
    "hidrostatica": 5, "sodio-agua": 8, "linfedema-obstrucao": 7,
    "celulas-insuficiencia-cardiaca": 15, "figado-noz-moscada": 11,
    "gradiente-hidrostatico-capilar": 4, "kf-permeabilidade-capilar": 4,
}
EXTRAS = {'edema': 'Edema occupies the interstitium; in a body cavity it is called an effusion',
 'hidrotorax': 'Often follows heart failure',
 'hidropericardio': 'Often follows pericarditis',
 'ascite': 'Often follows cirrhosis (portal hypertension plus low albumin)',
 'anasarca': 'Seen in heart failure, nephrotic syndrome, cirrhosis and renal failure',
 'hiperemia-ativa': 'Active and red (oxygenated blood), unlike passive congestion',
 'congestao': 'Passive: venous blood backs up, as in heart failure or venous obstruction',
 'oncotica': 'Albumin provides most of it; losing albumin lets water leave the vessels',
 'filtracao': 'Hydrostatic pressure pushes fluid out at the arterial end',
 'reabsorcao': 'Oncotic pressure pulls fluid back at the venous end',
 'linfa-retorno': 'Whatever the veins do not reabsorb, the lymphatics take back',
 'gradiente-hidrostatico-capilar': 'Filtration falls along the capillary as hydrostatic pressure drops',
 'transudato-proteina': 'Intact endothelium: clear, cell-poor and protein-poor',
 'exsudato-proteina': 'Damaged endothelium lets proteins and cells through',
 'hidrostatica': 'Venous outflow obstruction raises upstream capillary pressure',
 'insuficiencia-esquerda': 'Fluid backs up into the lungs: alveolar edema and hydrothorax',
 'insuficiencia-esquerda-congestao': 'The lung lies upstream of the left ventricle',
 'insuficiencia-direita': 'Liver and legs lie upstream of the right ventricle',
 'disfuncao-bomba': 'Low forward output and venous backup happen together',
 'sodio-agua': 'Retained sodium and water expand volume and feed the edema',
 'raas-insuficiencia-cardiaca': 'The macula densa and carotid baroreceptors sense low flow as hypovolemia',
 'raas-agrava-edema': 'A vicious circle: more volume, more congestion',
 'edema-pulmonar-venoso': 'Pulmonary venous hypertension pushes a transudate into the alveoli',
 'sindrome-nefrotica': 'Protein loss lowers oncotic pressure; renal sodium retention adds to it',
 'cirrose-edema': 'Hepatic disease is mixed: portal hypertension plus low albumin',
 'hipertensao-portal-cirrose': 'Portal hypertension raises hydrostatic pressure in the splanchnic bed',
 'ascite-portal': 'Low albumin and sodium retention add to the portal pressure',
 'linfedema-obstrucao': 'Fluid and protein stay in the interstitium despite an intact capillary',
 'permeabilidade-exsudato': 'Inflammatory mediators loosen endothelial junctions',
 'edema-proteico-ards': 'Diffuse alveolar damage: protein-rich edema with hyaline membranes',
 'permeabilidade-capilar-edema': 'The injured alveolar-capillary barrier also thickens',
 'lesao-alveolocapilar': 'Endothelium and pneumocytes are both injured',
 'membrana-hialina': 'Protein-rich fluid and cell debris line the damaged alveoli',
 'congestao-hepatica': 'Centrilobular blood backs up behind a failing right heart',
 'nutmeg-direita': 'Dark congested centers alternate with paler liver tissue',
 'celulas-insuficiencia-cardiaca': 'Chronic congestion leaks red cells; macrophages store their iron',
 'edema-pulmonar-rx': 'Cephalization and Kerley B lines reflect interstitial edema',
 'transudato-hidrostatica': 'The endothelium is intact, so the fluid stays protein-poor',
 'histamina-permeabilidade': 'With bradykinin, the first mediator of inflammatory edema (minutes)',
 'bradicinina-permeabilidade': 'Acts within minutes, with histamine',
 'leucotrienos-permeabilidade': 'Released by neutrophils in diffuse alveolar damage',
 'retencao-renal-primaria': 'Primary sodium retention expands plasma volume before any protein loss',
 'nefrite-retencao-sal': 'Less sodium filtered, more volume, more capillary pressure',
 'nefrite-versus-nefrotica': 'Nephrotic edema begins with protein loss instead',
 'vasodilatacao-esplancnica': 'Effective arterial volume falls despite total body fluid excess',
 'raas-cirrose': 'Perceived underfilling makes the kidney retain sodium and water',
 'cardiogenico-versus-permeabilidade': 'Cardiogenic: pale transudate; non-cardiogenic: exudate with hyaline membranes',
 'filariose': 'The worms block lymphatics; the limb becomes huge, firm and fibrotic',
 'contracao-endotelial': 'Histamine and bradykinin act within minutes; wider endothelial gaps let proteins out as an exudate',
 'neutrofilos-lesao-alveolar': 'Macrophages call in neutrophils (TNF, IL-8); their proteases and radicals break the barrier',
 'mixedema': 'Not true edema: glycosaminoglycans hold water in the tissue (hypothyroidism)',
 'light': 'Any of the three criteria (protein or LDH ratios) makes it an exudate',
 'derrame': 'Pleural, pericardial or peritoneal; with blood it is hemothorax, hemopericardium, hemoperitoneum',
 'hepatorrenal': 'Renal vasoconstriction from the same underfilling that drives ascites'}
VISUAL_IMAGES = {
    "edema": 3, "hiperemia-ativa": 3, "congestao": 3, "hidrostatica": 3,
    "hidrotorax": 6, "hidropericardio": 6,
    "starling": 4, "gradiente-hidrostatico-capilar": 4, "linfa-retorno": 4,
    "anasarca": 7, "ascite": 7, "linfedema-obstrucao": 7,
    "insuficiencia-esquerda": 8, "raas-insuficiencia-cardiaca": 8,
    "raas-agrava-edema": 8, "edema-pulmonar-rx": 9,
    "edema-pulmonar-venoso": 9, "sindrome-nefrotica": 10, "retencao-renal-primaria": 10,
    "nefrite-retencao-sal": 10, "nefrite-versus-nefrotica": 10,
    "psgn-edema": 10, "nefrite-aguda-anasarca": 10,
    "cirrose-edema": 11, "hipertensao-portal-cirrose": 11,
    "ascite-portal": 11, "vasodilatacao-esplancnica": 11,
    "raas-cirrose": 11, "congestao-hepatica": 12,
    "congestao-centrolobular": 12, "figado-noz-moscada": 12, "nutmeg-direita": 12,
    "lesao-alveolocapilar": 13, "membrana-hialina": 15, "neutrofilos-lesao-alveolar": 13,
    "permeabilidade-capilar-edema": 13, "permeabilidade-exsudato": 13,
    "celulas-insuficiencia-cardiaca": 14, "derrame": 6, "filariose": 7, "linfedema-mastectomia": 7,
    "cardiogenico-versus-permeabilidade": 15,
}
for card in CARDS:
    key = card["key"]
    slide = SLIDES.get(key)
    if slide:
        card["evid"] = f"Slide {slide}"
    image_slide = VISUAL_IMAGES.get(key)
    image = f'<br><img src="nebli-pat05-refacao-s{image_slide:02d}.png">' if image_slide else ""
    if card["kind"] == "text":  # AnKing: mantém o Extra original; a nota da aula vem depois
        card.pop("extra", None)
        if key in EXTRAS or image:
            card["extra_add"] = (f"- {EXTRAS[key]}" if key in EXTRAS else "") + image
    elif key in EXTRAS and not key.startswith("morfologia-pulmonar-s"):
        card["extra"] = f"- {EXTRAS[key]}" + image
    if key not in VISUAL_IMAGES and key not in {"morfologia-pulmonar-s09", "morfologia-pulmonar-s13", "morfologia-pulmonar-s14"}:
        card.pop("slide_sem_alternativa", None)
        card["sem_imagem"] = "O alvo cobra relação causal ou definição verbal; não exige reconhecimento de figura."
    if key.startswith("morfologia-pulmonar-s"):
        card["duplicacao_ok"] = "O card AnKing cobra a associação verbal; este testa o reconhecimento independente da imagem específica da aula."
for card in CARDS:
    if card["key"] == "linfedema-obstrucao":
        card["extra"] = '- Impaired removal of excess interstitial fluid leads to swelling &amp; pain<br>- Starts as pitting edema → progresses to nonpitting edema + firm, thickened skin<br>- Etiologies include <u>malignancy</u>, <u>iatrogenic</u> causes (lymph node dissection &amp; radiation), chronic <u>inflammation</u> (recurrent cellulitis), and severe <u>venous insufficiency</u>; obesity is also contributing factor<br>- Classic (but less common) cause is filariasis<br><img src="9756547cec1b9cf4476f5d2d6ef05076.png" width="541">'
for card in CARDS:
    if card["key"] == "linfedema-mastectomia":
        card["duplicacao_ok"] = "ganho: a causa iatrogênica da apostila; o AnKing cobra a obstrução linfática em geral"
    if card["key"] == "gsaa":
        card["duplicacao_ok"] = "ganho: o exame do líquido que aponta a causa; o AnKing cobra a relação portal–ascite"
EXCLUIDOS=[]
FORA_DO_RECORTE=["tratamento farmacológico dos edemas", "síndromes de derrame pleural específicas", "edema cerebral e angioedema sem alvo nos slides"]
