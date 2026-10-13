RUN_ID = "uc03-pat05-20261004a"
SHORT = "pat05"
LESSON = "2026-uc03-patologia-23-edema-congestao"
DECK = "NEBLI::UC03::P2::Patologia::Edema e congestão"
CRITERIOS = "MEMORY.md + FEEDBACKS até F-20261004-CODEX-04; fontes completas em fontes.json e planejamento-v2.md"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = "AnKing Step e acervos externos: busca/ext.json; consultas por edema, transudate, exudate, hydrostatic pressure, oncotic pressure, lymphatic obstruction, hyperemia, congestion, anasarca, ascites, hydrothorax, hydropericardium e pulmonary edema em 04/10. "

def ak(key, src, flags, bloco, alvo, slide, motivo, **kw):
    kw.setdefault("extra", "- Relate this finding to the pressure, permeability, or drainage mechanism that explains fluid accumulation")
    return dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, sem_imagem="alvo é relação, definição ou mecanismo; a imagem disponível não adiciona recuperação independente", **kw)

def au(key, text, flags, bloco, alvo, slide, espelhos, motivo, extra=""):
    extra = extra or "- The term identifies where fluid accumulates; the mechanism must be inferred separately"
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria="central", busca=BUSCA+"nenhum card recuperável com este termo anatômico da aula.", espelhos=espelhos, motivo=motivo, sem_imagem="a localização é definida pelo termo; não há figura de livro que aumente a recuperação sem entregar a resposta")

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
ak("edema-pulmonar-rx",1555363764010,{1:Z},D,"Edema pulmonar na radiografia",15,"Azul: reconhecimento da morfologia radiológica.",extra="- Cardiothoracic ratio above 50% is assessed on a PA chest radiograph; AP portable films magnify the heart"),
]
EXCLUIDOS=[]
FORA_DO_RECORTE=["tratamento farmacológico dos edemas", "síndromes de derrame pleural específicas", "edema cerebral e angioedema sem alvo nos slides"]
