"""Planejamento a partir das 72 lâminas vistas, transcrição, exercícios, monitoria, apostila e bibliografia docente; antes da busca e seleção. Destinos são chaves pedagógicas provisórias, não cards já escolhidos."""
PREFIXO='pt47'
AULA='Inflamação granulomatosa (UC03 P3; Amaro Duarte Neto e Luiz Fernando Ferraz da Silva)'
JUSTIFICATIVAS={'revisao':'Repetição do mesmo alvo nas partes I/II; destino consta na primeira ocorrência, sem duplicar a recuperação.'}
D={}
def s(n,t,*itens):
 D[n]=(n,'conteudo',t,[(k,txt,k) for k,txt in itens])
s(2,'Definição e finalidade',('definicao','Granuloma: agregado organizado de macrófagos epitelioides em inflamação crônica'),('persistencia','Estímulo persistente pouco degradável motiva contenção localizada'),('conter-nao-esterilizar','Conter o agente não implica esterilização nem eliminação da infecção'))
s(3,'Etiologias',('tb-prototipo','Tuberculose como protótipo de granuloma infeccioso'),('fungos','Paracoccidioides e Histoplasma podem provocar granulomas'),('imune-corpoestranho','Distinguir granuloma imune e de corpo estranho'),('sarcoidose-causa','Sarcoidose: doença granulomatosa imunomediada de causa desconhecida'),('gpa','Granulomatose com poliangiite como exemplo não infeccioso'),('tipoiv','Reação granulomatosa imune pode ser hipersensibilidade tardia tipo IV'))
s(4,'Origem e ativação dos macrófagos',('monocito','Monócitos recrutados se diferenciam em macrófagos teciduais'),('residentes','Macrófagos alveolares constituem defesa residente inicial'),('epitelioide','Células epitelioides derivam de macrófagos, não de epitélio'))
s(5,'Fenótipo ativado',('ativacao-lisossomos','Ativação aumenta enzimas lisossomais e atividade microbicida'),('ativacao-morfologia','Macrófago ativado aumenta tamanho, organelas e metabolismo'))
s(6,'Acúmulo e funções dos macrófagos',('recrutamento','Recrutamento contínuo de monócitos por quimiotaxia aumenta macrófagos'),('mcp1','MCP-1/CCL2 recruta monócitos'),('c5a','C5a participa do recrutamento quimiotático'),('proliferacao','Proliferação local também aumenta a população macrofágica'),('mif','MIF historicamente descrito como fator de inibição da migração e retenção local'),('proteases','Elastases/colagenases degradam matriz e contribuem para lesão'),('ros','ROS/RNS microbicidas também causam dano ao hospedeiro'),('complemento','Macrófagos produzem mediadores de complemento/coagulação, amplificando a inflamação'),('m2','IL-4/IL-13 favorecem programa de reparo macrofágico'),('tgfb','TGF-beta promove produção de colágeno/fibrose'),('pdgf','Fatores de crescimento como PDGF promovem proliferação fibroblástica'))
s(7,'Entrada e persistência do bacilo',('inalacao','Bacilos inalados alcançam alvéolos'),('manose','Receptor de manose reconhece componentes micobacterianos e permite captação'),('cr3','CR3 participa da entrada de micobactérias em macrófagos'),('fagolisossomo','M. tuberculosis impede maturação/fusão fagolisossomal'),('intracelular','Persistência intracelular protege de anticorpos/complemento extracelulares'),('replicacao','Macrófago não ativado pode servir de nicho de replicação'))
s(8,'Início da resposta adaptativa',('linfonodo','Apresentação inicial/priming de T ocorre no linfonodo drenante'),('mhcii','Antígeno apresentado por MHC II ativa linfócitos CD4'),('il2','IL-2 promove expansão clonal autócrina de células T'),('retorno-t','Linfócitos efetores retornam pelo sangue ao foco pulmonar'),('il1','IL-1 integra sinalização inflamatória inicial, não substitui reconhecimento/coestimulação'))
s(9,'Ciclo Th1–macrófago',('il12','IL-12 favorece diferenciação Th1'),('il18','IL-18 coopera com IL-12 na produção de IFN-gamma'),('ifng','IFN-gamma ativa macrófagos para controle intracelular'),('tnf','TNF contribui para recrutamento e manutenção da resposta granulomatosa'),('cd8','CD8 pode destruir macrófagos infectados'),('feedback','Apresentação/IL-12 e IFN-gamma mantêm circuito de ativação enquanto persiste antígeno'))
s(10,'Arquitetura do granuloma',('palisada','Células epitelioides formam paliçada em torno do centro'),('rima','Linfócitos periféricos mantêm ativação dos macrófagos'),('gigante-fusao','Células gigantes multinucleadas resultam principalmente da fusão de macrófagos'),('langhans','Núcleos periféricos em ferradura caracterizam célula gigante de Langhans'),('gigante-estranho','Núcleos irregulares/dispersos caracterizam gigante de corpo estranho'),('nao-obrigatorio','Necrose e células gigantes não são obrigatórias para definir granuloma'),('io-epitelioide','Reconhecer célula epitelioide em histologia'),('io-langhans','Reconhecer célula gigante de Langhans em histologia'))
s(11,'Visão panorâmica pulmonar',('io-granuloma','Reconhecer nódulos granulomatosos no parênquima pulmonar'))
s(12,'Vários granulomas coexistentes',('heterogeneidade','Granulomas no mesmo pulmão podem estar em fases distintas'))
s(13,'Granuloma antigo',('io-caseosa','Reconhecer material necrótico amorfo central'),('io-fibrose','Reconhecer colágeno/fibrose delimitando granuloma'),('io-antracose','Distinguir pigmento antracótico negro de micobactérias e calcificação'),('calcificacao','Necrose pode sofrer calcificação distrófica sem hipercalcemia'))
s(14,'Demonstração de bacilos',('ziehl','Ziehl-Neelsen demonstra BAAR vermelhos em fundo azul'),('io-baar','Identificar BAAR na coloração especial'),('baar-limite','BAAR identifica padrão de acidorresistência, não sozinho espécie/viabilidade'))
s(15,'Fibrose e caseificação',('fibrose-persistencia','Fibrose e caseificação podem coexistir no granuloma'))
s(16,'Reativação em lesão fibrótica',('io-exsudacao','Reconhecer foco exsudativo em granuloma fibrosado'),('reativacao-fibrose','Cicatriz/fibrose não garante erradicação, pode haver reativação'))
s(17,'Variações epitelioides',('sem-caseosa','Granuloma tuberculoso pode não apresentar necrose caseosa na amostra'),('miliar-vasos','Relação perivascular de granulomas permite entender disseminação hematogênica'))
s(18,'Evolução e reparo',('io-calcificacao','Reconhecer focos de calcificação em lesão granulomatosa'),('fibrose-funcao','Fibrose pulmonar residual compromete difusão/função do parênquima'))
s(19,'Necrose e persistência',('dna-rna','DNA micobacteriano não prova viabilidade; RNA pode ser indicador de atividade, com limitações'),('necrose-dissemina','Necrose de macrófagos libera bacilos e pode favorecer disseminação'))
s(20,'Tuberculose primária',('ghon-foco','Foco de Ghon corresponde à lesão pulmonar primária subpleural'),('ghon-complexo','Foco pulmonar + linfonodo hilar drenante constituem complexo de Ghon'),('ranke','Calcificação do complexo primário corresponde ao complexo de Ranke'),('io-primaria','Reconhecer padrão macroscópico de tuberculose primária'))
s(21,'Tuberculose secundária',('secundaria','Tuberculose secundária pode decorrer de reativação ou reinfecção'),('cavitacao','Necrose/liquefação e drenagem para via aérea produzem cavidade'),('apice','Reativação tem predileção apical, relacionada à alta tensão de oxigênio'),('io-cavidade','Reconhecer cavitação pulmonar na peça e radiografia'))
s(22,'Disseminação no pulmão',('bronquios','Drenagem de conteúdo bacilífero para brônquios dissemina infecção pelo pulmão'))
s(23,'Tuberculose miliar',('miliar','Disseminação hematogênica gera pequenos granulomas difusos'),('io-miliar','Reconhecer padrão miliar macro/radiográfico'))
s(24,'TB e AIDS',('aids-cd4','Perda CD4 compromete ativação macrofágica/organização granulomatosa'),('io-malformado','Reconhecer granuloma malformado e rima escassa em imunossupressão'))
s(25,'TB e AIDS, lesão exsudativa',('neutrofilos','Defeito de imunidade celular pode acompanhar resposta exsudativa/neutrofílica com dano e carga bacilar maior'))
s(26,'Sarcoidose',('sarcoidose-morfologia','Granulomas sarcoidóticos são tipicamente não necrosantes'),('io-sarcoidose','Reconhecer granulomas epitelioides compactos não caseosos'),('sarcoidose-exclusao','Morfologia isolada não exclui infecção nem estabelece sarcoidose'))
s(27,'Corpo asteroide',('io-asteroide','Identificar inclusão citoplasmática estrelada em célula gigante'),('asteroide-inespecifico','Corpos asteroides não são específicos da sarcoidose'))
s(28,'Corpo de Schaumann',('io-schaumann','Reconhecer inclusão calcificada laminada intracelular'))
s(29,'Inclusões cristalinas',('io-cristais','Reconhecer inclusões cristalinas de oxalato/carbonato em células gigantes'))
s(30,'Hamazaki–Wesenberg',('io-hamazaki','Reconhecer corpúsculos elípticos pigmentados de material ceroide'))
s(31,'Corpo estranho vegetal',('io-vegetal','Identificar material vegetal circundado por gigantes'),('celulose','Celulose indigerível após aspiração perpetua estímulo de corpo estranho'),('estranho-sem-t','Granuloma de corpo estranho não requer resposta T antígeno-específica'))
s(32,'Sutura',('io-sutura','Reconhecer reação granulomatosa a fio de sutura'),('sutura-persiste','Sutura não absorvível retida pode perpetuar reação de corpo estranho'))
s(33,'Silicose',('silica','Inalação de sílica em atividades como jateamento provoca persistência e lesão macrofágica'),('io-silicose','Reconhecer nódulo silicótico fibroso com colágeno concêntrico'),('silica-tb','Disfunção macrofágica na silicose aumenta suscetibilidade à tuberculose'))
s(34,'Sericita',('sericita','Poeira de sericita pode provocar pneumoconiose com reação granulomatosa'),('polarizacao','Luz polarizada evidencia partículas birrefringentes'))
s(35,'Asbesto',('asbesto','Fibras longas dificultam fagocitose completa e persistem'),('io-asbesto','Reconhecer corpos ferruginosos/asbesto revestidos por material ferroproteico'))
s(39,'Função e limites do granuloma',('dinamico','Granuloma é estrutura dinâmica, não barreira física impermeável'),('inato-inicial','Agregação granulomatosa inicial pode anteceder imunidade adaptativa, conforme modelo experimental'))
s(41,'Fase inicial da tuberculose',('atraso-adaptativo','Atraso do priming/recrutamento efetor permite expansão bacilar inicial'))
s(42,'Parede micobacteriana',('micolico','Ácidos micólicos relacionam parede lipídica à acidorresistência'),('arabinogalactano','Arabinogalactano conecta peptidoglicano à camada de ácidos micólicos'),('lam-parede','Lipoarabinomanano integra envelope micobacteriano'))
s(43,'Mecanismos de virulência',('corda','Fator corda é trealose dimicolato associado à virulência'),('corda-tnf','Fator corda estimula TNF e lesão macrofágica'),('corda-migracao','Fator corda pode inibir migração leucocitária'),('lam-apresentacao','LAM interfere em apresentação antigênica/resposta a IFN-gamma'),('catalase','Catalase reduz dano por peróxido de hidrogênio'),('amonia','Amônia pode aumentar pH fagossomal'),('pkng','PknG contribui para bloqueio da maturação fagossomal'),('vatpase','Exclusão/redução de V-ATPase impede acidificação adequada do fagossomo'))
s(46,'Resposta adaptativa efetora',('inos','IFN-gamma induz iNOS e produção de NO microbicida'),('ppd','Resposta à tuberculina exemplifica hipersensibilidade tardia mediada por T'))
s(52,'Regulação e amplificação',('il10','IL-10 limita ativação/apresentação por APCs e pode reduzir resposta protetora'),('ifng-mhcii','IFN-gamma aumenta apresentação por MHC II'),('esat6-mmp9','Modelo experimental: ESAT-6 induz MMP9 epitelial e recrutamento de novos macrófagos'),('reinfecta-macrofagos','Fagocitose de restos de macrófagos infectados pode transferir bacilos a novas células'),('saem-infectados','Macrófagos infectados podem sair e semear granulomas secundários'),('treg-persistencia','Treg podem atrasar expansão/recrutamento de efetores e favorecer persistência'),('tnf-equilibrio','Resposta TNF insuficiente ou excessiva pode favorecer necrose e falha de controle'))
SLIDES=[D.get(n,(n,'capa' if n in [1,36,37,71,72] else 'revisao','Capa/encerramento' if n in [1,36,37,71,72] else 'Repetição de imagens e mecanismos da parte I',[])) for n in range(1,73)]
CAPITULO=[('Robbins, cap. 2, pp. 71–74 (PDF 92–95)',[(k,t,k) for k,t in [('imune-corpoestranho','Distinção de patogênese imune/corpo estranho'),('langhans','Núcleos em ferradura'),('gigante-estranho','Núcleos distribuídos irregularmente'),('tgfb','Fibrose associada ao reparo')]]),('Ramakrishnan 2012, bibliografia docente, pp. 352–363',[(k,t,k) for k,t in [('dinamico','Granuloma dinâmico'),('inato-inicial','Formação precoce pela imunidade inata em modelos'),('esat6-mmp9','Recrutamento explorado pelo bacilo'),('reinfecta-macrofagos','Transferência após fagocitose de célula infectada'),('saem-infectados','Disseminação via macrófagos'),('tnf-equilibrio','TNF e capacidade microbicida'),('atraso-adaptativo','Atraso da resposta adaptativa'),('treg-persistencia','Regulação e persistência'),('conter-nao-esterilizar','Conter não equivale a eliminar')]])]
EXERCICIOS=[('Monitoria P2 aula 8, PDF 7–8; apostila Patologia capítulo 7, PDF 39–40',[(k,t,k) for k,t in [('feedback','Ativação recíproca'),('fibrose-funcao','Consequência funcional da fibrose'),('aids-cd4','Falha da resposta CD4'),('nao-obrigatorio','Necrose e gigantócitos não obrigatórios')]]),('Palavras-cruzadas docente e gabarito',[(k,t,k) for k,t in [('crohn','Crohn pode ter granulomas não caseosos no intestino'),('hanseniase','Hanseníase pode cursar com granulomas'),('gigante-fusao','Origem de gigantócitos'),('ziehl','Coloração BAAR'),('il2','Expansão T'),('ghon-complexo','Complexo primário'),('estranho-sem-t','Ausência de resposta linfocitária específica no corpo estranho')]]),('Provas 2024 P3 2.7, 2023 P2 3.5, 2016 P2 3.4, 2015 P2 1.1–1.3',[(k,t,k) for k,t in [('ifng','IFN-gamma e ativação'),('aids-cd4','CD4 e organização'),('gigante-fusao','Formação da célula gigante'),('rima','Função da rima linfocitária'),('tgfb','Fibroblastos e reparo'),('estranho-sem-t','Granuloma sem imunidade adaptativa')]])]
# Exercícios pertencem à aula: ancoragem na primeira seção etiológica, sem adicionar clínica alheia.
D[3][3].extend([('crohn','Crohn pode ter granulomas não caseosos no intestino','crohn'),('hanseniase','Hanseníase pode cursar com granulomas','hanseniase')])

# Revisão de mecanismo de 13/10: destinos físicos e exclusões explícitas.
_ALIAS = {'residentes': 'sh-1791147097386', 'ativacao-morfologia': 'ativacao-lisossomos', 'mhcii': 'sh-1791625427059', 'il2': 'sh-1791625429033', 'ifng': 'sh-1791625436658', 'io-epitelioide': 'visual-arquitetura', 'io-langhans': 'langhans', 'io-granuloma': 'visual-arquitetura', 'heterogeneidade': 'fases', 'io-caseosa': 'visual-caseosa-fibrose', 'io-fibrose': 'visual-caseosa-fibrose', 'io-antracose': 'visual-caseosa-fibrose', 'calcificacao': 'calcificacao-distrofica', 'io-baar': 'visual-baar', 'fibrose-persistencia': 'visual-caseosa-fibrose', 'io-exsudacao': 'visual-exsudacao', 'reativacao-fibrose': 'reativacao-cicatriz', 'miliar-vasos': 'miliar', 'io-calcificacao': 'calcificacao-distrofica', 'dna-rna': 'dna-viabilidade', 'io-primaria': 'visual-primaria', 'io-cavidade': 'visual-cavidade', 'bronquios': 'cavitacao', 'io-miliar': 'visual-miliar', 'aids-cd4': 'cd4-malformado', 'io-malformado': 'visual-malformado', 'neutrofilos': 'cd4-malformado', 'io-sarcoidose': 'visual-nao-caseoso', 'io-asteroide': 'visual-asteroide', 'asteroide-inespecifico': 'asteroide', 'io-schaumann': 'schaumann', 'io-cristais': 'cristais', 'io-hamazaki': 'hamazaki', 'io-vegetal': 'visual-vegetal', 'estranho-sem-t': 'corpoestranho-sem-th1', 'io-sutura': 'sutura', 'sutura-persiste': 'sutura', 'io-silicose': 'visual-silicose', 'asbesto': 'asbesto-fagocitose', 'io-asbesto': 'visual-asbesto', 'micolico': 'acidos-micolicos', 'lam-parede': 'lam-envelope', 'corda': 'fator-corda', 'corda-tnf': 'fator-corda-tnf', 'inos': 'sh-1791625430632', 'ifng-mhcii': 'sh-1791625430332', 'reinfecta-macrofagos': 'eferocitose', 'saem-infectados': 'saem-macrofagos', 'treg-persistencia': 'treg'}
_REMOVED = ['tb-prototipo', 'sarcoidose-causa', 'gpa', 'c5a', 'complemento', 'pdgf', 'inalacao', 'manose', 'cr3', 'retorno-t', 'il1', 'il18', 'cd8', 'palisada', 'reativacao-cicatriz', 'visual-exsudacao', 'dna-viabilidade', 'ghon-foco', 'visual-primaria', 'ranke', 'secundaria', 'apice', 'visual-cavidade', 'visual-miliar', 'sarcoidose-exclusao', 'asteroide', 'visual-asteroide', 'schaumann', 'cristais', 'hamazaki', 'celulose', 'sutura', 'silica', 'visual-silicose', 'silica-tb', 'sericita', 'polarizacao', 'asbesto-corpo', 'visual-asbesto', 'inato-inicial', 'atraso-adaptativo', 'acidos-micolicos', 'arabinogalactano', 'lam-envelope', 'fator-corda', 'fator-corda-quimica', 'fator-corda-tnf', 'lam-apresentacao', 'catalase', 'amonia', 'pkng', 'vatpase', 'ppd', 'esat6-mmp9', 'eferocitose', 'saem-macrofagos', 'treg']
def _mechanism_dest(d):
    if isinstance(d, (tuple, list)): return [_mechanism_dest(x) for x in d]
    k = _ALIAS.get(d, d)
    if k in _REMOVED or k == "corda-migracao": return "EXC: F-20261013-CODEX-02; exemplo ou especificidade sem recuperação própria necessária para o mecanismo geral desta aula; recorte reduzido por pedido explícito de Davi"
    return k
SLIDES = [(n,t,tit,[(i,x,_mechanism_dest(d)) for i,x,d in items]) for n,t,tit,items in SLIDES]
CAPITULO = [(t,[(i,x,_mechanism_dest(d)) for i,x,d in items]) for t,items in CAPITULO]
EXERCICIOS = [(t,[(i,x,_mechanism_dest(d)) for i,x,d in items]) for t,items in EXERCICIOS]

# Necrose caseosa: aspecto macroscópico + reconhecimento no corte.
SLIDES = [(n,t,tit,[(i,x,["caseosa","visual-caseosa-fibrose"] if i=="io-caseosa" else d) for i,x,d in items]) for n,t,tit,items in SLIDES]

_RESTORE = ['ghon-foco', 'secundaria', 'acidos-micolicos']
def _restore_dest(i,d):
 k=_ALIAS.get(i,i)
 return k if k in _RESTORE else d
SLIDES=[(n,t,tit,[(i,x,_restore_dest(i,d)) for i,x,d in items]) for n,t,tit,items in SLIDES]
CAPITULO=[(t,[(i,x,_restore_dest(i,d)) for i,x,d in items]) for t,items in CAPITULO]

_PRINCIPIOS = [(2, 'padrao-cronico', 'Padrão organizado de inflamação crônica'), (2, 'funcao-contencao', 'Organização limita dispersão do estímulo'), (3, 'imune-antigeno', 'Antígeno persistente sustenta cooperação T-macrófago'), (5, 'ativacao-microbicida', 'IFN-γ aumenta capacidade microbicida'), (6, 'reparo-fibroblasto', 'Sinais macrofágicos estimulam fibroblastos a depositar colágeno'), (10, 'necrose-imunolesao', 'Lesão imune contribui para necrose central'), (10, 'caseoso-padrao', 'Padrão caseoso com necrose central')]
SLIDES=[(n,t,tit,items+[(k,x,k) for slide,k,x in _PRINCIPIOS if slide==n]) for n,t,tit,items in SLIDES]

# Segunda leitura: não converter exemplos clínicos e nomenclatura isolada em
# obrigações de memorização. Permanecem nas lâminas e nos Extras dos princípios.
_SECOND_REMOVED = {'fungos','crohn','hanseniase','mcp1','mif','proteases','m2',
 'caseosa','fases','calcificacao-distrofica','sem-caseosa',
 'ghon-foco','ghon-complexo','secundaria','cavitacao','miliar','sarcoidose-morfologia',
 'visual-nao-caseoso','ziehl','visual-baar','baar-limite','acidos-micolicos','il10'}
_SECOND_REMOVED.add('ifng-mhcii')
def _second_dest(i, d):
    candidates = [i]
    if isinstance(d, (list, tuple)): candidates += list(d)
    candidates += [_ALIAS.get(x, x) for x in candidates]
    if any(x in _SECOND_REMOVED for x in candidates):
        return 'EXC: F-20261013-CODEX-04; detalhe clínico, morfológico ou molecular mantido como ilustração, sem cartão próprio no recorte de mecanismo geral pedido por Davi'
    return d
SLIDES = [(n,t,tit,[(i,x,_second_dest(i,d)) for i,x,d in items]) for n,t,tit,items in SLIDES]
CAPITULO = [(t,[(i,x,_second_dest(i,d)) for i,x,d in items]) for t,items in CAPITULO]
EXERCICIOS = [(t,[(i,x,_second_dest(i,d)) for i,x,d in items]) for t,items in EXERCICIOS]

# O mesmo conceito aparece na monitoria e nas provas. Cada ocorrência precisa
# ter ID próprio no inventário, embora ambas possam apontar ao mesmo card.
EXERCICIOS = [(t, [(f'prova-{i}' if t.startswith('Provas ') else i, x, d)
                   for i,x,d in items]) for t,items in EXERCICIOS]
