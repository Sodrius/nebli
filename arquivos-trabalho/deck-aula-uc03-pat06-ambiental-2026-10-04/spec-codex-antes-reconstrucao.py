RUN_ID='uc03-pat06-20261004a'
SHORT='pat06'
LESSON='2026-uc03-patologia-24-patologia-ambiental'
DECK='NEBLI::UC03::P2::Patologia::Patologia ambiental'
CRITERIOS='MEMORY.md + FEEDBACKS até F-20261004-CODEX-04; leitura documentada em fontes.json e planejamento.json'
MEDIA={}
V,Z=3,4
BUSCA='AnKing e acervos externos pesquisados em busca/ext.txt; nenhum candidato recuperável para este alvo específico.'

def ak(key,src,flags,bloco,alvo,slide,motivo,**kw):
 kw.setdefault('extra','- Connect the fact to inhaled pollutants and the tissue response described in this lesson')
 return dict(key=key,kind='text',src=src,manter=True,flags=flags,bloco=bloco,alvo=alvo,evid=f'Slide {slide}',motivo=motivo,sem_imagem='alvo é mecanismo ou relação; imagem não acrescenta recuperação independente',**kw)
def au(key,text,flags,bloco,alvo,slide,espelhos,motivo,extra):
 return dict(key=key,kind='autoral',text=text,extra=extra,flags=flags,bloco=bloco,alvo=alvo,evid=f'Slide {slide}',autoria='central',busca=BUSCA,espelhos=espelhos,motivo=motivo,sem_imagem='definição ou relação causal sem figura que melhore a recuperação')

A,B,C,D,E='A-contexto','B-poluentes','C-particulado','D-efeitos','E-biomassa'
CARDS=[
au('inversao-termica','A thermal inversion traps pollutants near the {{c1::ground}}',{1:V},A,'Inversão térmica',20,[1473289461901,1473548355407],'Verde: explica o Grande Nevoeiro.','- A warm layer above cooler surface air blocks vertical dispersion and raises inhaled concentration'),
au('iceberg','The largest hidden burden of air pollution is {{c1::subclinical inflammation}}',{1:Z},A,'Iceberg dos efeitos',22,[1473548355407,1473466860013],'Azul: leitura explícita do esquema.','- Death is the visible tip, while mild effects affect many more people'),
au('primario','A pollutant emitted directly from a source is {{c1::primary}}',{1:V},B,'Poluente primário',35,[1473638444755,1524150216368],'Verde: organiza as fontes da lâmina.','- Vehicle exhaust, industry and combustion can emit gases and particles directly'),
au('secundario','Ground-level ozone is a {{c1::secondary}} pollutant',{1:V},B,'Poluente secundário',35,[1473289461901,1473548369834],'Verde: conceito explícito do slide.','- It forms in the atmosphere from precursors under sunlight and acts as an oxidant'),
au('pm-diametro','Particle deposition is determined by its aerodynamic {{c1::diameter}}',{1:V},C,'Diâmetro aerodinâmico',36,[1703597789293,1703596428399],'Verde: princípio que conecta a classificação ao sítio de dano.','- PM10 and PM2.5 describe upper size limits, not different chemical substances'),
ak('coal-dust',1473638444755,{1:V},C,'Carbono como núcleo do particulado',36,'Verde: conecta carbono inalado ao material particulado da aula.'),
ak('dust-macrophage',1703597789293,{2:V},C,'Macrófago alveolar fagocita particulado',37,'Verde: defesa alveolar citada nos slides e prova.'),
ak('alveolar-macrophage',1473289622374,{1:V},C,'Macrófago alveolar',37,'Verde: célula que faz a ponte entre depósito e inflamação.'),
ak('cilia-clearance',1473289461901,{1:V,2:Z},C,'Depuração mucociliar',38,'Verde e azul: defesa alterada pela poluição e biomassa.'),
ak('mucus-traps',1556143323229,{2:Z},C,'Muco prende partículas',38,'Azul: componente da defesa local.'),
ak('smoke-injury',1524150216368,{1:Z},C,'Lesão por inalação de fumaça',39,'Azul: conecta combustão a lesão pulmonar.'),
ak('cohb',1473385249608,{1:V,2:Z},B,'Carboxiemoglobina',35,'Verde e azul: base molecular do CO.'),
ak('co-affinity',1473385253436,{1:V},B,'Afinidade do CO pela hemoglobina',35,'Verde: mecanismo do CO na aula.'),
ak('co-left',1473385257949,{2:V},B,'Curva de dissociação no CO',35,'Verde: explica entrega tecidual reduzida.'),
ak('co-unloading',1473385273967,{2:V},B,'Liberação de oxigênio no CO',35,'Verde: consequência direta do deslocamento.'),
ak('co-capacity',1473385280374,{1:V},B,'Capacidade de transporte no CO',35,'Verde: hipóxia apesar de troca pulmonar.'),
ak('co-pao2',1473385287565,{1:V},B,'PaO2 na intoxicação por CO',35,'Verde: evita confundir pressão dissolvida e conteúdo.'),
ak('co-complexiv',1474253531615,{1:V,3:V},B,'CO e cadeia respiratória',35,'Verde: amplificação celular, explicitada nos exercícios.'),
ak('co-cherry',1487292580228,{1:V},B,'Cor na intoxicação grave por CO',35,'Verde: aplicação clínica de encaixe direto.'),
ak('co-hypoxia',1473466860013,{1:V},B,'CO reduz conteúdo arterial de oxigênio',35,'Verde: efeito final que integra o bloco.'),
ak('oxidized-ldl',1471811979298,{1:V,2:Z,3:Z},D,'LDL oxidada e macrófago',41,'Verde: liga estresse oxidativo à aterosclerose; azuis: mecanismo.'),
ak('foam-cell',1471811989477,{1:V},D,'Célula espumosa',41,'Verde: consequência da captura de LDL oxidada.'),
ak('ecm-plaque',1471811997810,{1:V,2:V},D,'Remodelamento da placa',41,'Verde: explica aumento da espessura da placa.'),
ak('endothelial-no',1474340552038,{1:V,2:Z},D,'Endotélio antitrombótico',42,'Verde: efeito vascular prioritário na prova.'),
ak('pneumonia-defense',1473548355407,{1:V},D,'Defesa prejudicada favorece pneumonia',43,'Verde: prova de 2024 e biomassa de 2025.'),
ak('mucociliary-pneumonia',1473548369834,{1:V},D,'Falha mucociliar favorece pneumonia',43,'Verde: encadeamento cobrado na prova.'),
ak('cilia-motion',1555791674668,{1:Z,2:Z},D,'Movimento ciliar',43,'Azul: mecanismo da remoção de muco.'),
ak('bronchiolar-cilia',1703592029357,{2:Z},D,'Cílios nos bronquíolos',43,'Azul: localização anatômica da defesa.'),
ak('dust-cells',1703596428399,{1:V,2:Z},D,'Células da poeira',43,'Verde e azul: correlato celular da poluição.'),
ak('macrophage-phagocytosis',1701206425104,{1:Z},D,'Macrófago remove material particulado',43,'Azul: função celular de apoio.'),
ak('coal-exposure',1473638444755,{1:V},E,'Inalação crônica de poeira de carbono',47,'Verde: conecta exposição por combustão ao alvo pulmonar.'),
ak('co-scenario',1503840888417,{1:Z},E,'Cefaleia em exposição crônica a CO',47,'Azul: reconhecimento de exposição por combustão.'),
]
EXCLUIDOS=[]
FORA_DO_RECORTE=['tratamento da intoxicação por CO','doenças ocupacionais específicas não ensinadas nos slides','mudança climática em detalhe epidemiológico além das lâminas']
