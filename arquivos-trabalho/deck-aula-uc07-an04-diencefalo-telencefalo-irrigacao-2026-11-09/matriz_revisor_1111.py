"""Matriz editorial de recuperação; não escreve cards nem no Anki."""
from pathlib import Path
import json,importlib.util,hashlib,re
P=Path(__file__).resolve().parent
D=json.loads((P/'plan.json').read_text())
ALL={e['key']:e for e in D['entries']}|{'sh-'+k:v for k,v in D['compartilhados'].items()}
sp=importlib.util.spec_from_file_location('percurso_revisor',P/'percurso.py'); mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
# Cada escolha abaixo foi editorial: não é busca por coincidência de termos.
M={
1:('sh-1792697125350 sh-1792572870657 sh-1792572870656','Divisão cérebro/telencéfalo/diencéfalo na frente; identificação das duas estruturas.'),
2:('diencefalo-escondido','Telencéfalo recobre o diencéfalo na vista lateral; não afirma exclusividade de vista medial.'),
3:('diencefalo-partes-org','Recupera quatro partes por posição; metatálamo é nomenclatura alternativa explicada no Extra.'),
4:('sh-1792572870704 sh-1792572870701 sh-1792588687027','Identifica ventrículo lateral/corpo caloso; o assoalho ventricular formado pelo tálamo é recuperado no texto.'),
5:('sh-1792345309393 diencefalo-partes-org','IO do sulco e organizador usam acima/abaixo para recuperar tálamo/hipotálamo; subtálamo lateral.'),
6:('sh-1792588687081 sh-1792345306369','Texto recupera os tálamos unidos; IO mostra aderência através da cavidade. Variação de presença fica no Extra.'),
7:('sh-1792258845028 sh-1792345644467 sh-1792572870653 sh-1792572870652','Identificações dos quatro alvos talâmicos nas posições mostradas pela aula.'),
8:('talamo-limites-org sh-1792588687027 sh-1792588687028 sh-1792338018612','Organizador recupera cada limite; textos complementam as paredes ventriculares e IO identifica cápsula.'),
9:('nucleo-x-ganglio','Distingue aglomerado neuronal dentro e fora do SNC; nome núcleo fundamenta o caráter cinzento do tálamo.'),
10:('talamo-nucleos-org sh-1792345975792','Grupo anterior é reconhecido visualmente e sua associação límbica é exigida no organizador.'),
11:('ak-1481418712049 ak-1481418725172 sh-1792572870653 sh-1792572870652','Lateral recebe via visual e medial via auditiva; ambos têm IO. Mnemônico de altura é só auxílio, não fato extra a decorar.'),
12:('talamo-nucleos-org sh-1792345977592 sh-1792345989291 sh-1792345992490','Grupos e função geral recuperados; não exige decorar ignorância sobre função mediana. Funções talâmicas detalhadas pertencem à fisiologia.'),
13:('hipotalamo-limites-org','Recupera tálamo superior, III ventrículo medial e subtálamo lateral.'),
14:('hipotalamo-limites-org sh-1792244790744 sh-1792244786725 sh-1792244787869 sh-1792244858168','Recupera quatro marcos do assoalho em sequência, com identificação independente de cada um.'),
15:('hipotalamo-nucleos-org','Regiões supraóptica/tuberal/mamilar organizam a recuperação de seus núcleos. O nome da região está visível, a associação aos núcleos é recuperada.'),
16:('hipotalamo-nucleos-org io-nucleo-arqueado sh-1792346373316 sh-1792346374740 sh-1792346376214 sh-1792346381716 sh-1792346383240 sh-1792346386189','Conjunto por região e IO dos núcleos; arqueado agora é identificado no hipotálamo do Machado, sem homônimo bulbar.'),
17:('diencefalo-partes-org sh-1792572870699','Organizador recupera epitálamo posterior e IO o situa.'),
18:('ak-1481418839841 sh-1792244839896 sh-1792572870700 sh-1792345317795 sh-1792438779776','Pineal e habênula são componentes recuperados em texto; comissuras/elementos do epitálamo são reconhecidos por IO. Não se confunde glândula com comissuras.'),
19:('subtalamo-limites-org sh-1792572870698','Quatro limites e identificação do subtálamo; posição lateral ao hipotálamo explica não aparecer na superfície medial.'),
20:('sh-1792347675113 ak-1481162464655','IO identifica núcleo subtalâmico; hemibalismo contralateral recupera consequência motora de lesão.'),
21:('sh-1792345648666 sh-1792345652643 sh-1792244787869 sh-1792572870700 sh-1792572870704','Revisão visual das estruturas da fala; septo, fórnix, infundíbulo, comissura e ventrículo identificados. Relações já retomadas em unidades anteriores.'),
22:('sh-1792697125350 sh-1792346803714','Repetição da divisão cerebral; lâmina terminal identificada. Não cria um segundo card cérebro=telencéfalo+diencéfalo.'),
23:('faces-hemisferio','Recupera nomes das três faces; remoção de tronco/cerebelo é orientação para visualizar a base, não nova classificação.'),
24:('giro-x-sulco','Recupera giros como saliências e sulcos como depressões.'),
25:('lobos-limites-org sh-1792348020020 sh-1792572870709 io-sulco-semilunar','Central/lateral identificados, semilunar nomeado como variável e identificado no IO real do Machado, sem transformá-lo em limite universal.'),
26:('lobos-limites-org sh-1792572870660 sh-1793966747229 sh-1793966747231 sh-1793966747230','Lobos identificados e separados pelos sulcos centrais relevantes; não usa lunatus como limite universal.'),
27:('sh-1792348020020 achar-sulco-central','Reconhecimento do sulco central e dos giros que o ladeiam. Correção da fala: não afirmar que sempre toca o sulco lateral, pois há prega cortical entre eles (Machado cap7§2).'),
28:('sh-1792572870661 io-sulco-precentral sh-1792261811050','IO do giro e do sulco pré-central; função motora primária recuperada no AnKing.'),
29:('sh-1792572870710 sh-1792572870711 sh-1792572870713 sh-1792572870719 sh-1792572870720','Identifica três giros e os dois sulcos que os delimitam na superfície frontal.'),
30:('sh-1793966747239 sh-1793889229460 ak-1481513311304 sh-1792588687051 sh-1792588687068 sh-1792348470659 io-parte-opercular io-parte-orbital','Frontal inferior dominante/Broca e afasia não fluente; partes orbital/triangular/opercular no texto, ramo ascendente discriminado entre triangular/opercular; IO triangular Kenhub e IOs orbital/opercular reais Machado; nenhum alvo homônimo inventado.'),
31:('kh-giro-poscentral-recuperado sh-1792572870721 ak-1481513127112','IO pós-central e sulco; função somestésica primária recuperada em texto.'),
32:('sh-1792588687061 sh-1792588687059 sh-1792572870716 sh-1792572870717 sh-1792572870718 sh-1792348479235 sh-1792348482310','Intraparietal entre lóbulos superior/inferior e supramarginal no inferior; IOs identificam lóbulos/giros/sulco.'),
33:('sh-1793966747231 io-sulco-parietoccipital ak-1481244690823','A lateral occipital não introduz alvo novo na fala; lobo, limite medial e córtex visual já são recuperados nos cards pertinentes.'),
34:('sh-1792572870712 sh-1792572870714 sh-1792572870715 sh-1792572870722 io-sulco-temporal-inferior','Identifica três giros temporais e ambos os sulcos delimitadores.'),
35:('sh-1792261728496 io-giros-curtos-insula io-giro-longo-insula io-sulco-central-insula','Quatro identificações da ínsula, com divisões anterior/posterior visíveis. Audição primária está no giro temporal transverso, não transferida para a ínsula.'),
36:('corpo-caloso-partes-org io-rostro-corpo-caloso sh-1792349646457 sh-1792439186574 sh-1792349644730','Quatro partes do corpo caloso recuperadas em sequência e identificadas em IO.'),
37:('sh-1792588687078 sh-1792572870728 sh-1792572870729 io-sulco-cingulo','Texto recupera giro entre corpo caloso e sulco do cíngulo, com os dois sulcos e o giro identificados.'),
38:('sh-1792572870724 sh-1792572870725 sh-1792572870726 sh-1792348871085','Reconhecimento do lóbulo paracentral, seus sulcos e continuação medial frontal; relação espacial fica na imagem focal, não apenas no nome.'),
39:('io-sulco-parietoccipital sh-1792345655366 sh-1792572870723 sh-1792572870727 sh-1792588687071 sh-1792588687075 ak-1481244690823','Identifica sulcos/pré-cúneo/cúneo, cobra lobo de cada região e calcarino como separação de áreas visuais.'),
40:('sh-1792588687028 sh-1792588687033 sh-1792345652643 sh-1792345648666','Não memoriza absoluto falso abaixo do corpo caloso=diencéfalo: fórnix/septo também são telencefálicos. Substitui pela topografia precisa do tálamo/hipotálamo e IO das estruturas vizinhas.'),
41:('face-inferior-org sh-1792349636706 sh-1792340080484 sh-1792340082028 sh-1792349638181 io-sulco-hipocampo sh-1792572870730 sh-1792572870731 sh-1792349631780','Sequência occipitotemporal medial/parahipocampal/úncus e identificações; sulcos hipocampal, colateral, rinal e occipitotemporal reconhecidos nas imagens.'),
42:('achar-sulco-central sh-1792572870661 kh-giro-poscentral-recuperado sh-1792348020020','Recupera os dois giros paralelos usados para localizar o sulco central e identifica os três.'),
43:('nucleo-x-ganglio ak-1481162002789 sh-1792347668041 sh-1792572870679 sh-1792338022186','Definição de núcleo como agregado neuronal e identificação das massas profundas; função moduladora dos núcleos da base recuperada no AnKing.'),
44:('corte-horizontal-org capsula-interna-partes-org sh-1792338023839 sh-1792338022186 sh-1792572870679 sh-1792338018612','Organizador recupera sequência ínsula/cápsulas/claustro/putâmen/pálido/cápsula interna; organizador da cápsula recupera vizinhos caudado/tálamo. Conjunto permite reconstruir corte sem depender só do Extra.'),
45:('ak-1481162303980 estriado-org sh-1792572870707 sh-1792347678017 sh-1792340079308','Lentiforme=putâmen+pálido e corpo estriado macroscópico=caudado+lentiforme; IO do accumbens e corpo amigdaloide. Não confunde estriado funcional com nomenclatura macroscópica.'),
46:('corte-horizontal-org capsula-interna-partes-org sh-1792572870737 sh-1792572870736 sh-1792338018612','Sequência espacial exige cápsulas extrema/externa/interna; partes da interna são discriminadas pelos vizinhos, sem duplicação do IO da cápsula inteira.'),
47:('ak-1522347007612 sh-1792328837674 sh-1792696998756','Trajeto vertebral pelos forames transversos e identificação do vaso; união das duas vertebrais em basilar. Origem subclávia é explicada no Extra, mas não alvo isolado desta frente.'),
48:('vertebrobasilar-org sh-1792350091972 sh-1792350096755 ak-1480995292746 ak-1480995329569','PICA de vertebral no organizador; PICA/AICA reconhecidas por IO e associadas aos territórios bulbar/pontino laterais. Origem da AICA corrigida contra esquema da fala: usualmente basilar.'),
49:('sh-1792696998756 sh-1792588687095 sh-1792350094380 sh-1792350098581','Basilar por união de vertebrais e artéria do labirinto irrigando orelha interna recuperadas; origens variáveis e meato comVII/VIII no Extra.'),
50:('sh-1792350100078 sh-1792350101581 sh-1792588687093 vertebrobasilar-org','IO ramos pontinos e cerebelar superior; bifurcação basilar em cerebrais posteriores recuperada em texto.'),
51:('territorios-org ak-1481513222026 ak-1481244840641 sh-1792350088057','ACP=occipital/temporal inferomedial e déficit visual; corrige simplificação de que toda face inferior seria exclusivamente ACP.'),
52:('aci-ramos-org sh-1792350121479 sh-1792342678377','Segmento cervical sem ramos, canal carotídeo e sifão devem ser recuperados na frente revisada; IO carotídeo complementa trajeto.'),
53:('aci-ramos-org kh-arteria-oftalmica','Oftálmica recuperada como ramo e pelo território bulbo ocular/anexos, com identificação IO própria.'),
54:('aci-ramos-org sh-1792350077380 sh-1792350083556 sh-1792350086331','Ramos ACA/ACM/comunicante posterior por direção e identificações do vaso.'),
55:('sh-1792350083811 sh-1792348025216 ak-1481562751403 ak-1481562763561 ak-1481562772354','Território lateral ACM recuperado, com déficit face/MS e associações corticais dominância/afasia/negligência.'),
56:('sh-1792350077635 sh-1792350077936 sh-1792350078186 ak-1481562744652','Território medial frontal/parietal e faixa superior ACA, com déficit de membro inferior contralateral.'),
57:('sh-1792346808763 sh-1792346819863','Identifica artérias hipofisárias superior e inferior; sua distribuição faz parte da imagem da hipófise.'),
58:('willis-org sh-1792350075605 sh-1792350086331 ak-1481772047979 ak-1481772053364','Organizador recupera comunicantes anterior/posterior pelos sistemas unidos; aneurismas exemplificam relações com quiasma/III.'),
59:('willis-org sh-1792350073731','Comunicantes e circulação colateral são recuperadas; Extra ressalva calibres/variantes e não garante proteção absoluta.'),
60:('', 'Repetição do tronco/nervos/pedúnculos da AN03 instalada: o bloco não ensina conteúdo novo de AN04. Original integral preservado; estudo correspondente pertence à aula03, sem duplicar seus cards.'),
61:('sh-1792244839896 sh-1792345309393 sh-1792345648666 corpo-caloso-partes-org io-rostro-corpo-caloso sh-1792345652643 io-sulco-parietoccipital sh-1792345655366','Revisão prática das estruturas de diencéfalo/telencéfalo, já recuperadas e identificadas; sem transformar repetição em novas notas.'),
62:('lobos-limites-org','Três sulcos que separam frontal/parietal/temporal/occipital recuperados em organizador único.')}
linhas=[];faltas=[]
def add(fonte,ref,item,keys,recuperacao,arquivo='',**kw):
 requested=keys.split() if isinstance(keys,str) else keys
 present=[k for k in requested if k in ALL]; missing=[k for k in requested if k not in ALL]
 row=dict(fonte=fonte,ref=str(ref),item=item,cards=present,recuperacao=recuperacao,arquivo=arquivo,estado='recuperavel')
 if missing:row.update(estado='pendente_build_ou_falta',cards_ausentes=missing);faltas.append({'fonte':fonte,'ref':str(ref),'o_que_falta':'Cards previstos ausentes do plano: '+', '.join(missing),'sugestao':'Conferir rebuild e incluir somente se os textos/figuras realmente recuperarem a relação.'})
 if not requested:row.update(estado='outra_aula_repeticao',motivo=recuperacao)
 linhas.append(row|kw)
for u,(src,mins,title,txt) in enumerate(mod.U,1):
 keys,rec=M[u]
 add('lamina',u,title+': '+txt,keys,rec,'fontes/slides.txt',natureza='unidade de roteiro derivada, não lâmina original')
 if src==mod.AP:continue
 fname='t1-diencefalo.min.txt' if src==mod.T1 else 't2-telencefalo.min.txt' if src==mod.T2 else 't3-irrigacao.min.txt' if src==mod.T3 else 't4-pratica.min.txt'
 add('transcricao',f'{src} {mins}',title,keys,rec,'fontes/'+fname,unidade=u)
# Apostila e resumo: linhas por ponto concreto, vinculadas às recuperações manuais acima.
for ref,units in [('Guia PDF28: IIIventrículo/sulco/aderência',[3,5,6,8,14]),('Guia PDF29: hipotálamo/epitálamo',[13,14,17,18]),('Guia PDF30: subtálamo',[19,20]),('Guia PDF38: faces/lobos/frontal',[22,23,24,25,26,28,29,30]),('Guia PDF39: temporal/parietal/ínsula',[31,32,34,35]),('Guia PDF40: face medial',[36,37,38,39]),('Guia PDF41: face inferior',[41]),('Guia PDF42: núcleos/cápsulas',[43,44,45,46])]:
 for u in units:add('apostila',f'{ref} · u{u}',mod.U[u-1][2],M[u][0],M[u][1],'fontes/apostila-guia.txt')
for ref,units in [('GaKa PDF15: diencéfalo/tálamo',[3,5,7,8,10,11,12]),('GaKa PDF16–17: hipotálamo/epitálamo/base',[13,14,15,16,18,19,43,44,45,46]),('GaKa PDF18: face lateral',[25,28,29,30,31,32,34,35]),('GaKa PDF19: medial/inferior',[36,37,38,39,41]),('GaKa PDF25: irrigação',[47,48,49,50,51,52,53,54,55,56,58,59])]:
 for u in units:add('resumo',f'{ref} · u{u}',mod.U[u-1][2],M[u][0],M[u][1],'fontes/gaka-paginas.txt')
# Referência: as seções bibliográficas do recorte, não título genérico do livro.
for ref,units in [('Machado6§1 Generalidades',[1,2,3]),('Machado6§2 IIIventrículo',[5,6,14]),('Machado6§3 Tálamo',[7,8,11]),('Machado6§4 Hipotálamo',[13,14,15,16]),('Machado6§5 Epitálamo',[17,18]),('Machado6§6 Subtálamo',[19,20]),('Machado7§1 Generalidades',[22,23,36]),('Machado7§2 Sulcos/giros',[24,25,26,27]),('Machado7§3.1.1 Frontal',[28,29,30]),('Machado7§3.1.2 Temporal',[34]),('Machado7§3.1.3 Parietal/occipital',[31,32,33]),('Machado7§3.1.4 Ínsula',[35]),('Machado7§3.2 Face medial',[36,37,38,39]),('Machado7§3.3 Face inferior',[41]),('Machado7§4 Ventrículos laterais',[4,21]),('Machado7§5.1 Núcleos da base',[43,44,45]),('Machado7§5.2 Centro branco/cápsulas',[44,46]),('Machado9§2.2.2 Carótida interna',[52,53,54]),('Machado9§2.2.3 Vertebrobasilar',[47,48,49,50]),('Machado9§2.2.4 Círculo arterial',[58,59]),('Machado9§2.2.5 Territórios corticais',[51,55,56])]:
 ch='6-diencefalo' if ref.startswith('Machado6') else '7-telencefalo' if ref.startswith('Machado7') else '9-vascularizacao'
 for u in units:add('livro',f'{ref} · u{u}',mod.U[u-1][2],M[u][0],M[u][1],f'livros/machado-cap{ch}.txt')
# Provas: pergunta+justificativa do recorte, sem converter erro de gabarito em fato.
Q={
'P1-2025 Q4':('ak-1481162377083 ak-1481162387832 ak-1481162415359 sh-1792347675467 sh-1792347683193','Via indireta e desinibição: estriado inibeGPe; STN excitaGPi; GPi inibe tálamo; interromper o freio pode aumentar movimento.'),
'P1-2025 Q5':('ak-1480389641277 ak-1481562774888 ak-1483845113686','Corticoespinal na perna posterior antes da decussação; lesão pode causar déficit contralateral. Corrige gabarito: cápsula também tem fibras sensitivas; motor puro depende de lesão seletiva.'),
'P1-2025 Q6':('ak-1481418744155','Déficit sensitivo contralateral apósAVCtalâmico é explicitamente recuperado; corticospinal não atravessa tálamo.'),
'P1-2025 Q16':('sh-1792347682942 sh-1792347671169 sh-1792347664967 sh-1792347683444 ak-1481162436810','D1 facilita via direta e movimento; retirar facilitação aumenta influência relativa da via indireta. Etapas necessárias são recuperadas, não apenas citadas.'),
'P1-2025 Q22':('ak-1481857859641 ak-1481857835449','Bradicinesia, rigidez e tremor de repouso no organizadorParkinson; perda dopaminérgica nigral explica princípio.'),
'P1-2025 Q25':('ak-1481244817525','Alça deMeyer temporal→quadrantanopsia homônima superior contralateral, com exemplo esquerda→direita noExtra.'),
'2023 Q6':(M[5][0],M[5][1]),'2023 Q7':(M[58][0]+' sh-1792350073731',M[58][1]+' Circulação colateral é recuperada no card específico.'),
'2023 Q14':('ak-1483930154512 ak-1481562800018 sh-1792345652947 sh-1792346392190 talamo-nucleos-org','Papez com ponte mamilares→fascículo mamilotalâmico→tálamo anterior; reconhecimento límbico e fórnix. Confirmar memória episódica como alvo e parahipocampal na frente, não só noExtra.'),
'2023 Q16':(M[14][0],M[14][1]),'2023 Q17':('sh-1792345652947 ak-1483930154512','Fórnix conduz fibras hipocampo→mamilares; comissura dofórnix é distinta das projeções do fórnix.'),
'Coletanea Q6':(M[59][0]+' '+M[58][0],M[59][1]),
'Coletanea Q7':(M[28][0]+' '+M[29][0]+' '+M[30][0]+' '+M[31][0]+' sh-1792348031994','Sulcos frontais, pré/pós-central e função motora/sensitiva; área auditiva primária no giro temporal transverso anterior, Broca no dominante geralmente esquerdo.'),
'Coletanea Q13':('capsula-interna-partes-org sh-1792345652947','Perna anterior entre caudado/lentiforme; fórnix e cápsula como projeção. Gabarito que chama fórnix inteiro de comissural é corrigido; comissura dofórnix é outra estrutura.'),
'Coletanea Q20':('ak-1483930154512 ak-1481562800018 sh-1792345652947 talamo-nucleos-org','Mesmo conteúdo de2023Q14: circuito/associação límbica; colículos não pertencem ao circuito clássico.'),
'Coletanea Q21':(M[5][0],M[5][1]),'Coletanea Q1':(M[45][0]+' sh-1792338023839',M[45][1]+' Claustro também é identificado; amígdala não é caudado+lentiforme.')}
for ref,(keys,rec) in Q.items():add('prova',ref,'Reconstruir '+ref+' pelo conteúdo da questão e comentários conferidos',keys,rec,'fontes/provas-an04.txt')
# Pontos que não podem ser autoaprovados enquanto só aparecerem no Extra.
def front(key):return ALL.get(key,{}).get('fields',{}).get('Text','')
checks=[('u52','aci-ramos-org',lambda t:('sem ramos' in t or 'sem <' in t) and 'sif' in t and 'carot' in t,'Carótida interna: ausência de ramos cervicais/canal/sifão só noExtra no plano observado.'),('u53','aci-ramos-org',lambda t:('ocular' in t or 'olho' in t) and 'oft' in t,'Oftálmica: recuperar território ocular/anexos, não somente nome do ramo.'),('2023 Q14','ak-1483930154512',lambda t:bool(re.search(r'\{\{c\d+::[^}]*memória',t,re.I)),'Memória episódica relacionada ao circuitoPapez ainda só noExtra.'),('Coletanea Q20','ak-1481562800018',lambda t:'hipocampal' in t.lower(),'Pertencimento do giro parahipocampal ao sistema límbico ainda só noExtra.')]
for ref,key,test,msg in checks:
 if not test(front(key)):faltas.append({'fonte':'transcricao' if ref.startswith('u') else 'prova','ref':ref,'o_que_falta':msg,'sugestao':'Revisar o alvo da frente ou associar card recuperável existente, sem criar autoral por automatismo.'})
out={'schema_version':1,'autor':'revisor independente /root/revisor_uc07_an04','selection_hash_observado':D['selection_hash'],'plan_sha256_observado':hashlib.sha256((P/'plan.json').read_bytes()).hexdigest(),'escopo':'62 unidades da aula semslides, transcrições, pontosGuia/GaKa e seçõesMachado do recorte;17questõesAN04. Originais integrais dasprovas preservados no runuc07-resumos-2026-11-11.','linhas':linhas,'faltas_revisor':faltas,'ok_editorial':not faltas,'limites':['Matriz montada por recuperação específica; IO recupera identificação/topografia visual, não prova sozinho todas as relações verbais.','Unidade60 repeteAN03; questões deventrículos/meninges/nervos/cerebelo/propriedadesneuronais/neuroimagem/fármacos/psiquiatria fora deste recorte pertencem às aulaspróprias, com originais preservados.','Não transforma váriantede anatomia ou erro de gabarito em conteúdo verdadeiro para satisfazer cobertura.','Livro: recorte macroscópico/arterial; não expande para pesoencefálico, veias ou barreiras daAN06.']}
for linha in linhas:
 if linha['item']=='Giros e sulcos': linha['item']='Giros como saliências corticais e sulcos como depressões entre os giros'
 elif linha['item']=='Lobo da ínsula': linha['item']='Lobo da ínsula: localização profunda ao sulco lateral, giros curtos e longo separados pelo sulco central da ínsula'
(P/'matriz-fontes.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
(P/'completude-revisor-atual-1111.json').write_text(json.dumps({'execucao':'/root/revisor_uc07_an04','selection_hash':D['selection_hash'],'ok':not faltas,'faltas':faltas,'rasos':[],'linhas':len(linhas),'referencia_matriz':'matriz-fontes.json'},ensure_ascii=False,indent=2))
print(len(linhas),'linhas editoriais;',len(faltas),'faltas/pendências:')
for f in faltas:print(f['ref'],f['o_que_falta'])
