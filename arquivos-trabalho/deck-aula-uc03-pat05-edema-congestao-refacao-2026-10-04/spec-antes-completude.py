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
ak("leucotrienos-permeabilidade",1487640108934,{1:Z},C,"Leucotrienos mantêm aumento de permeabilidade no edema inflamatório",12,
   "Azul: mediador indicado no esquema da lâmina e na prova antiga."),
au("morfologia-pulmonar-s13", '<img src="nebli-pat05-refacao-s13.png"><br>The pink fluid occupying alveolar spaces represents {{c1::pulmonary edema}}', {1:Z}, D,
   "Reconhecer edema alveolar no corte histológico do slide 13",13,[1471914969111,1473707295145],"Azul: reconhecimento microscópico ensinado diretamente na lâmina.",
   extra="Alveolar air spaces become filled by eosinophilic edema fluid, reducing the space available for gas exchange."),
au("morfologia-pulmonar-s14", '<img src="nebli-pat05-refacao-s14.png"><br>Engorged septal capillaries indicate {{c1::pulmonary congestion}}', {1:Z}, D,
   "Reconhecer congestão capilar pulmonar no corte do slide 14",14,[1471914938644,1471914979068],"Azul: separa sangue retido no vaso de líquido no alvéolo.",
   extra="Congestion expands septal capillaries with erythrocytes; associated alveolar fluid may coexist."),
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
ak("cardiogenico-versus-permeabilidade",1532735591750,{1:V},C,
   "Comparar edema pulmonar cardiogênico e não cardiogênico pelo mecanismo",12,
   "Verde: une as duas imagens pulmonares por hidrostática versus permeabilidade."),
]
CARDS = [c for c in CARDS if c["key"] not in {
    "hiperemia-reativa", "permeabilidade", "obstrucao-veia-hepatica",
    "edema-dependente", "linfedema", "figado-noz-moscada",
    "kf-permeabilidade-capilar", "lesao-capilar-kf", "congestao-centrolobular",
    "starling"
}]
SLIDES = {
    "transudato-proteina": 6, "exsudato-proteina": 12,
    "hidrostatica": 5, "sodio-agua": 8, "linfedema-obstrucao": 7,
    "congestao-hepatica": 11, "congestao-centrolobular": 11,
    "celulas-insuficiencia-cardiaca": 15, "figado-noz-moscada": 11,
    "gradiente-hidrostatico-capilar": 4, "kf-permeabilidade-capilar": 4,
}
EXTRAS = {
    "edema": "Edema occupies the interstitium or a serous cavity. Slide 3 also contrasts it with blood retained within vessels.",
    "hidrotorax": "Hydrothorax names fluid in the pleural cavity; slide 2 lists it alongside the other serous effusions.",
    "hidropericardio": "Hydropericardium names fluid in the pericardial sac, regardless of the mechanism producing it.",
    "ascite": "Ascites is peritoneal fluid. In slide 11, portal hypertension and sodium retention combine to increase that fluid.",
    "anasarca": "Anasarca means widespread subcutaneous edema, illustrated clinically by the diffuse swelling on slide 7.",
    "hiperemia-ativa": "In active hyperemia, arteriolar dilation increases oxygenated inflow; slide 3 contrasts this with passive venous congestion.",
    "congestao": "Impaired venous drainage traps deoxygenated blood in a tissue and can lead to hypoxia and edema.",
    "starling": "The slide 4 diagram contrasts outward capillary hydrostatic pressure with inward plasma oncotic pressure and lymphatic drainage.",
    "oncotica": "Albumin provides most plasma oncotic pressure. Losing albumin reduces the force retaining water in vessels.",
    "filtracao": "On slide 4, hydrostatic pressure favors outward flow at the arterial side of the illustrated capillary.",
    "reabsorcao": "On slide 4, the relative fall in hydrostatic pressure favors inward flow on the venous side of the illustrated capillary.",
    "linfa-retorno": "The lymphatic network above the capillary on slide 4 returns residual fluid and escaped proteins to the circulation.",
    "gradiente-hidrostatico-capilar": "The drop in capillary hydrostatic pressure from arterial to venous end changes the net direction of fluid movement.",
    "kf-permeabilidade-capilar": "A damaged barrier increases filtration capacity, allowing fluid and proteins to leave the circulation more easily.",
    "transudato-proteina": "Low protein indicates a mostly intact endothelial barrier, as in hydrostatic or oncotic edema.",
    "exsudato-proteina": "High protein indicates loss of vascular selectivity, as in inflammatory edema on slide 12.",
    "hidrostatica": "Venous outflow impairment raises upstream capillary pressure and drives fluid into dependent tissue.",
    "insuficiencia-esquerda": "Left ventricular failure raises pulmonary venous pressure; retained fluid then enters the alveoli.",
    "insuficiencia-esquerda-congestao": "The lung is upstream of the left ventricle, so left heart failure produces pulmonary venous congestion.",
    "insuficiencia-direita": "The systemic venous bed is upstream of the right ventricle, producing peripheral and hepatic congestion.",
    "disfuncao-bomba": "Reduced forward output and venous backup coexist in the heart failure circuit on slide 8.",
    "sodio-agua": "Renal sodium and water retention increases circulating volume and can worsen hydrostatic edema.",
    "raas-insuficiencia-cardiaca": "Reduced renal perfusion triggers renin release despite excess body fluid in the heart failure circuit.",
    "raas-agrava-edema": "RAAS and ADH conserve sodium and water, raising volume and worsening the congestion that initiated the response.",
    "edema-pulmonar-venoso": "Pulmonary venous hypertension from left heart failure pushes low-protein fluid into the lung.",
    "hipertensao-venosa-pulmonar": "Raised left atrial pressure travels backward through pulmonary veins to the alveolar capillaries.",
    "sindrome-nefrotica": "Proteinuria reduces plasma albumin; renal sodium retention adds a second drive toward edema.",
    "cirrose-edema": "Reduced albumin synthesis lowers oncotic pressure, while the portal circulation adds a hydrostatic component.",
    "hipertensao-portal-cirrose": "Portal pressure is the first box in the slide 11 cascade ending in ascites.",
    "ascite-portal": "Portal hypertension increases splanchnic filtration, contributing to peritoneal fluid accumulation.",
    "linfedema-obstrucao": "When lymphatic drainage fails, interstitial liquid and proteins accumulate despite an intact capillary barrier.",
    "permeabilidade-exsudato": "Inflammatory endothelial injury allows protein-rich liquid to escape, giving the effusion an exudative composition.",
    "edema-proteico-ards": "The damaged alveolo-capillary interface in slide 12 leaks protein-rich fluid into air spaces.",
    "permeabilidade-capilar-edema": "Slide 12 shows endothelial and epithelial injury increasing the leak across the alveolar barrier.",
    "lesao-capilar-kf": "Toxins or inflammation enlarge the effective leak, increasing the filtration coefficient.",
    "lesao-alveolocapilar": "Damage to endothelium and pneumocytes lets plasma proteins enter air spaces.",
    "membrana-hialina": "Protein-rich fluid and epithelial debris line damaged alveoli as hyaline membranes.",
    "congestao-hepatica": "In slide 11, the mottled liver image is compatible with chronic venous backup and centrilobular congestion.",
    "congestao-centrolobular": "Centrilobular hepatocytes are most vulnerable to venous stasis and low oxygen delivery.",
    "nutmeg-direita": "Right heart failure transmits venous pressure to the liver and can create a nutmeg cut surface.",
    "celulas-insuficiencia-cardiaca": "Chronic pulmonary congestion can cause alveolar hemorrhage; macrophages ingest the iron and become hemosiderin-laden.",
    "figado-noz-moscada": "Dark centrilobular congestion alternating with paler liver tissue creates the mottled gross appearance.",
    "edema-pulmonar-rx": "The radiograph on slide 9 illustrates bilateral pulmonary opacity and pleural fluid in hydrostatic edema.",
    "transudato-hidrostatica": "An intact endothelial barrier retains protein even when elevated capillary pressure causes a large effusion.",
    "histamina-permeabilidade": "Early histamine signaling opens endothelial gaps and produces the protein-rich edema of acute inflammation.",
    "bradicinina-permeabilidade": "Bradykinin combines vasodilation with increased permeability, contributing to the early inflammatory exudate.",
    "leucotrienos-permeabilidade": "Leukotrienes sustain the vascular leak after the immediate histamine and bradykinin phase.",
    "retencao-renal-primaria": "The slide 10 diagram also shows direct renal sodium retention; it can expand plasma volume even before the underfill response to hypoalbuminemia.",
    "nefrite-retencao-sal": "On slide 10, a diseased glomerulus filters less sodium; retention raises intravascular volume, then capillary hydrostatic pressure and edema.",
    "nefrite-versus-nefrotica": "The renal branch in slide 10 is primary sodium retention from impaired filtration; the nephrotic branch begins with protein loss and low oncotic pressure.",
    "psgn-edema": "This is the acute glomerular example used in the exercise for renal sodium retention that starts the edema mechanism.",
    "nefrite-aguda-anasarca": "The vignette gathers severe consequences of renal sodium and water retention, linking the slide 10 pathway to generalized and pulmonary edema.",
    "vasodilatacao-esplancnica": "Portal hypertension causes splanchnic arterial dilation and lowers effective arterial filling despite total body fluid excess.",
    "raas-cirrose": "Perceived underfilling activates RAAS; the kidney retains sodium and water, feeding ascites.",
    "cardiogenico-versus-permeabilidade": "The slide 9 lung is driven by hydrostatic pressure, whereas slide 12 shows a leaky alveolo-capillary barrier.",
}
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
    "raas-cirrose": 11, "congestao-hepatica": 11,
    "congestao-centrolobular": 11, "figado-noz-moscada": 11,
    "lesao-alveolocapilar": 12, "membrana-hialina": 12, "neutrofilos-lesao-alveolar": 12,
    "permeabilidade-capilar-edema": 12, "permeabilidade-exsudato": 12,
    "celulas-insuficiencia-cardiaca": 14,
    "cardiogenico-versus-permeabilidade": 12,
}
for card in CARDS:
    key = card["key"]
    slide = SLIDES.get(key)
    if slide:
        card["evid"] = f"Slide {slide}"
    if key in EXTRAS:
        image_slide = VISUAL_IMAGES.get(key)
        card["extra"] = EXTRAS[key] + (f'<br><img src="nebli-pat05-refacao-s{image_slide:02d}.png">' if image_slide else "")
    if key not in VISUAL_IMAGES and key not in {"morfologia-pulmonar-s09", "morfologia-pulmonar-s13", "morfologia-pulmonar-s14"}:
        card.pop("slide_sem_alternativa", None)
        card["sem_imagem"] = "O alvo cobra relação causal ou definição verbal; não exige reconhecimento de figura."
    if key.startswith("morfologia-pulmonar-s"):
        card["duplicacao_ok"] = "O card AnKing cobra a associação verbal; este testa o reconhecimento independente da imagem específica da aula."
    if key == "morfologia-pulmonar-s14":
        card["extra_add"] = 'Slide 15 repeats the pulmonary pattern in paired histologic fields.<br><img src="nebli-pat05-refacao-s15.png">'
EXCLUIDOS=[]
FORA_DO_RECORTE=["tratamento farmacológico dos edemas", "síndromes de derrame pleural específicas", "edema cerebral e angioedema sem alvo nos slides"]
