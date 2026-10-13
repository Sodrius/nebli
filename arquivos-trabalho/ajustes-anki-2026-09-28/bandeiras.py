"""Decisões editoriais sobre as frentes lidas, sem inferir prioridade de HY/tag.

Os intervalos são os índices do catálogo fixo, não filtros aplicados à coleção viva.
Preserva cores já existentes, salvo feedback resolvido e exceções justificadas.
Não certifica cobertura da aula nem revisão bibliográfica integral.
"""
import json, re, html
from pathlib import Path
from collections import Counter
BASE=Path(__file__).parent
S=json.loads((BASE/'snapshot.json').read_text())
P=json.loads((BASE/'plan.json').read_text())
IDS=json.loads((BASE/'index.json').read_text())
C={c['cardId']:c for c in S['cards']};N={n['noteId']:n for n in S['notes']}
F={cid:int(flag) for flag,ids in S['flags'].items() for cid in ids}

GROUPS=[
 (0,56,'Regulação de expressão gênica: entender a resposta da célula à disponibilidade de substrato.'),
 (57,106,'Integração metabólica: distinguir fontes de energia, tecidos e estados alimentares.'),
 (107,254,'Integração metabólica: relações entre insulina/glucagon, jejum, combustíveis e vias centrais.'),
 (255,321,'Diabetes: reconhecer mecanismos, manifestações e interpretação de dados clínicos fundamentais.'),
 (322,382,'Inflamação: ligação causal entre reconhecimento, mediadores, alterações vasculares e resolução.'),
 (383,428,'Complemento: ativação e efeitos de opsonização, inflamação e lise; relações com deficiência.'),
 (429,540,'Antibióticos: mecanismo, alvo e resistência com uso recorrente na formação médica.'),
 (541,570,'Controle microbiano: distinguir esterilização, desinfecção e mecanismos que sustentam sua aplicação.'),
 (571,615,'Fisiologia bacteriana: metabolismo, crescimento e condições que explicam o comportamento bacteriano.'),
 (616,659,'Genética bacteriana: herança, transferência de genes e mecanismos de variabilidade/resistência.'),
 (660,694,'Microbiota: localização, barreiras e relações funcionais entre microrganismos e hospedeiro.'),
 (695,793,'Morfologia bacteriana: reconhecer estruturas e sua relação com coloração, função e patogenicidade.'),
 (794,981,'Patogenicidade: relacionar mecanismo de virulência, agente e manifestações características.'),
 (982,1052,'Patologia e radiologia: ligar alteração estrutural a manifestações e reconhecimento de doença.'),
 (1053,1088,'Edema e congestão: mecanismos de acúmulo de líquido, morfologia e reconhecimento de sinais.'),
 (1089,1148,'Inflamação aguda: mecanismos e sequência funcional da resposta, com morfologia associada.'),
 (1149,1172,'Patologia ambiental: compreender mecanismos principais de lesão e exposições relevantes.'),
 (1173,1232,'Anatomia digestiva: reconhecer estruturas principais e relações espaciais úteis em outras aulas.'),
 (1233,1277,'Intestino grosso e canal anal: identificação e relações com continência, vascularização e inervação.'),
 (1278,1373,'Vascularização visceral: territórios, trajetos e anastomoses que sustentam raciocínio anatômico.'),
 (1374,1408,'Histologia gástrica: reconhecer células/camadas e relacionar sua estrutura à função.'),
 (1409,1450,'Histologia intestinal: reconhecimento dos segmentos, barreira e renovação epitelial.'),
 (1451,1483,'Motilidade: controle neural e muscular que explica os movimentos do tubo digestivo.'),
 (1484,1536,'Motilidade: coordenação funcional da deglutição, trânsito e evacuação.')]

# Detalhes válidos, mas com menor custo de esquecimento que os mecanismos/estruturas centrais.
BLUE={}
def blue(indices,reason):
 for i in indices: BLUE[i]=reason
blue([21,22,23,24,28,44,*range(48,54)],'Nomenclatura ou configuração experimental local; o mecanismo geral merece maior retenção que esse detalhe.')
blue([94,104], 'Detalhe de distribuição ou proporção; utilidade local maior que necessidade de recuperação duradoura.')
blue([*range(325,330),352,378,380,400,401,421,422,424,427], 'Nome, estequiometria ou etapa acessória: aprender ajuda, mas o mecanismo principal tem maior custo de esquecimento.')
blue([452,469,474,475,494,503,509,520,524,532,540], 'Detalhe de membro, nomenclatura ou mecanismo específico; os alvos gerais e resistências principais recebem prioridade maior.')
blue([551,553,554,555,562,564,566,570,590,594,595,597,602,603,607], 'Parâmetro/nome de método ou condição de cultivo que pode ser recuperado conforme a necessidade.')
blue([620,651,659,734,793], 'Detalhe de nomenclatura, sequência específica ou história; menor utilidade duradoura que o princípio associado.')
blue([810,811,812,839,862,863,904,906,938,947,948], 'Detalhe de identificação ou mecanismo específico; vale conhecer, com menor prioridade de manutenção.')
blue([1025,1040,1041,1159,1166,1167,1168,1169], 'Número, lista ou contexto histórico/local; menor custo futuro de esquecer que os mecanismos fundamentais.')
blue([1173,1200,1201,1202,1215,1216,1229,1230,1247,1249,1250,1268,1270,1275,1308,1313,1327,1355,1358,1359,1360,1362], 'Subdivisão, nome secundário ou detalhe de posição; manter disponível sem equiparar aos marcos anatômicos principais.')
blue([1450,1486,1487,1523,1524,1532], 'Marcador, frequência ou detalhe de uma sequência; o entendimento funcional global tem maior valor de retenção.')

# Dúvidas concretas: não promover a verde/azul sem resolver formulação, escopo ou duplicação.
DOUBTS={}
def doubt(indices, reason):
 for i in indices: DOUBTS[i]=reason
doubt([13,14,15],'A expressão "operons em procariontes apenas" precisa de qualificação; não certificar uma exclusividade biológica falsa.')
doubt([32,33,34],'A digestão da lactose omite galactose na formulação; confirmar o conjunto de clozes antes de corrigir.')
doubt([110,111,182,183,184],'Separar efeito indireto do glucagon no estado de jejum de ação lipolítica direta em adipócitos humanos.')
doubt([119,134],'GLUT2 em célula beta exige distinção entre modelo didático/roedores e fisiologia humana.')
doubt([179],'Lista BRICKLIPS agrupa muitas recuperações no mesmo card; condensação requer preservar o alvo e verificar irmãos.')
doubt([181,202,232],'Formulação metabólica absoluta ou imprecisa; conferir a enzima/tecido e restringir a afirmação antes da cor.')
doubt([285],'Sequestro ósseo não deve ser definido simplesmente como foco lítico; revisar com a figura da aula.')
doubt([286,305],'Indicação de exame ou valor preditivo depende do contexto; falta qualificar o enunciado.')
doubt([371,1093],'Possível repetição de recuperação PRR/PAMP entre aulas; confirmar ganho e associações por cloze.')
doubt([381],'Histamina e serotonina em mastócitos exigem qualificação por espécie/fonte; não assumir equivalência humana.')
doubt([476,479,481,486],'Afirmação ampla sobre indicação/resistência: qualificar carbapenemases, ESBL ou localização genética.')
doubt([491,498,517,521,522,528,558],'Antes de elevar prioridade, reconfirmar recorte da aula para indicação clínica/toxicidade/triagem; não importar clínica lateral.')
doubt([501],'Muitas classes/mecanismos num único cloze; reformulação precisa evitar duplicar os cards específicos existentes.')
doubt([530,531,539],'Formulação de antibiograma/combinação pode sugerir regra absoluta; conferir limites do exemplo.')
doubt([545,547,559,560,568,569],'Qualificar condição de uso ou resistência ao desinfetante; não transformar afirmação simplificada em regra universal.')
doubt([571,575,580,581,584,585],'Enunciado de fisiologia/cultivo tem exclusividade ou generalização que precisa de ajuste.')
doubt([615,690],'Possível sobreposição da recuperação de AGCC: texto comentado foi corrigido, mas a equivalência entre aulas ainda precisa de decisão.')
doubt([747,754,767,774],'Rever absoluto/nomenclatura ou pertinência do método diagnóstico antes de promover a prioridade.')
doubt([802,803,804,825,900,950],'Precisão pendente: localização genética, frequência ou exemplo/exclusividade não devem ser tomados como regra universal.')
doubt([1005,1009],'Absoluto/epidemiologia no enunciado merece atualização bibliográfica antes de recomendar retenção.')
doubt([1057,1065,1067,1068,1072,1073,1078,1087],'Possível recuperação equivalente no próprio deck de edema; comparar alvo e ganho, sem apagar histórico nesta passagem.')
doubt([1146,1147,1148],'Limites numéricos de exsudato precisam de unidade/tipo de líquido e fonte: não certificar uso universal.')
doubt([1197,1198],'Mesma figura e destaque para respostas diferentes (região pilórica/piloro), aparentemente sobre o antro; referência visual precisa ser reconciliada.')
doubt([1263,1264],'Dor em hemorroida depende de complicações, como trombose; qualificar o absoluto.')
doubt([1316,1318,1319,1321,1372,1373],'Linha pectínea é marco do canal anal: revisar o uso de "rectum" e limites de drenagem/irrigação.')
doubt([1414],'Pregas circulares não são exclusivas do jejuno; a identificação precisa de critérios adicionais.')
doubt([1448],'Marcador em figura pode ser ilustração e não alvo da aula; verificar roteiro antes de dar prioridade.')
doubt([1453,1462,1535],'Rever localização do plexo/segmentos sacrais ou confirmar escopo do exemplo de doença.')

corrected={x['noteId'] for x in P['notes']}
UPGRADE={1082:'Ascite é uma forma clínica fundamental de acúmulo de líquido, dentro do recorte de edema.',
1083:'Anasarca é reconhecimento básico de edema generalizado.',1203:'Esfíncter pilórico liga identificação anatômica ao controle da saída gástrica.',
1265:'A diferença visceral/somática explica a sensibilidade acima/abaixo da linha pectínea.',
1266:'A inervação somática explica a sensibilidade abaixo da linha pectínea.',1267:'O nervo pudendo é via central da inervação somática perineal.'}
rows=[]
for i,cid in enumerate(IDS):
 c=C[cid];n=N[c['note']];old=F[cid]
 fields={k:v['value'] for k,v in n['fields'].items()}
 edit=next((v for v in P['notes'] if v['noteId']==c['note']),None)
 if edit:fields.update(edit['after'])
 t=fields.get('Text',fields.get(str(c['ord']+1)+'a',fields.get('Title','')))
 target=re.findall(r'{{c'+str(c['ord']+1)+r'::(.*?)(?:::.*?)?}}',t)
 clean=lambda x:re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',x))).strip()
 reason=next(r for lo,hi,r in GROUPS if lo<=i<=hi)
 new=old;status='cor anterior preservada'
 if i in DOUBTS:
  reason=DOUBTS[i];status='pendência explícita; cor pessoal anterior preservada'
 elif old==0 or (old==1 and c['note'] in corrected):
  new=4 if i in BLUE else 3;reason=BLUE.get(i,reason);status='calibrado por alvo'
 elif i in UPGRADE and old==4:
  new=3;reason=UPGRADE[i];status='prioridade ajustada'
 elif old==1:status='vermelho pessoal preservado'
 if old==1 and c['note'] in corrected and i in DOUBTS:
  # O texto melhorou, mas duplicação/identificação ainda não foi resolvida.
  new=1;status='vermelho mantido por pendência restante'
 row={'index':i,'cardId':cid,'noteId':c['note'],'ord':c['ord'], 'deck':c['deckName'],
      'target':clean(' / '.join(target) if target else t),'before':old,'after':new,
      'reason':reason,'status':status}
 rows.append(row)
# AGENTS.md exige calibração incremental. Esta execução cobre três aulas e as
# notas corrigidas; a triagem global NÃO é autorização para recolorir a coleção.
scope=set(range(571,616)) | set(range(1053,1089)) | set(range(1173,1233))
scope |= {i for i,cid in enumerate(IDS) if C[cid]['note'] in corrected}
focused=[r for r in rows if r['index'] in scope]
P['flags']=[x for x in focused if x['before']!=x['after']]
(BASE/'plan.json').write_text(json.dumps(P,ensure_ascii=False,indent=1))
(BASE/'triagem-frentes-NAO-APLICAR.json').write_text(json.dumps({'status':'triagem preliminar; não validada para migração de bandeiras','rows':rows},ensure_ascii=False,indent=1))
(BASE/'bandeiras.json').write_text(json.dumps(focused,ensure_ascii=False,indent=1))
print(json.dumps({'scope_cards':len(focused),'changes':len(P['flags']),'after_in_scope':dict(Counter(r['after'] for r in focused)),
 'explicit_pending':sum(r['index'] in DOUBTS for r in focused)},ensure_ascii=False))
