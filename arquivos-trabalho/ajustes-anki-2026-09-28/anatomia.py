"""Pedido de 28/09: uma recomendação verde por estrutura repetida; fontes em ordem."""
import json
from pathlib import Path
BASE=Path(__file__).parent
P=json.loads((BASE/'plan.json').read_text())
all_rows=json.loads((BASE/'triagem-frentes-NAO-APLICAR.json').read_text())['rows']
focused={r['cardId']:r for r in json.loads((BASE/'bandeiras.json').read_text())}
R={r['index']:r for r in all_rows}

# (estrutura, representante, demais recuperações da mesma estrutura).
# Escolha manual após ler todas as 201 frentes de Anatomia. Não agrupar
# por qualquer ocorrência do nome no enunciado: considera o alvo cobrado.
GROUPS=[
 ('estômago',1225,[1190]),
 ('papila duodenal maior',1182,[1209]),
 ('hiato esofágico',1220,[1189]),
 ('jejuno e íleo: distinção entre segmentos',1218,[1211,1212,1217,1324]),
 ('pregas circulares',1223,[1191,1215,1216]),
 ('tênias do cólon',1257,[1243,1268]),
 ('tronco celíaco',1278,[1330,1334]),
 ('artéria hepática comum',1297,[1279,1339]),
 ('artéria esplênica',1293,[1280,1291,1334]),
 ('artéria gástrica esquerda',1295,[1281,1342]),
 ('artéria hepática própria',1282,[1284,1335]),
 ('artéria gastroduodenal',1298,[1283,1286,1288,1337]),
 ('artéria gástrica direita',1296,[1285,1301,1336]),
 ('artéria gastro-omental direita',1294,[1287,1300,1322,1338]),
 ('artéria gastro-omental esquerda',1292,[1289,1340]),
 ('artérias gástricas curtas',1299,[1290,1304,1341]),
 ('linfonodos celíacos',1305,[1306]),
 ('linfonodos mesentéricos superiores',1311,[1310,1312]),
 ('artéria mesentérica superior',1309,[1323,1325,1333,1343]),
 ('artéria mesentérica inferior',1314,[1315,1326,1331,1353]),
 ('vasa recta',1222,[1345]),
 ('veias retais superiores',1361,[1370]),
 ('veias esplênica e mesentérica superior',1328,[1357,1364]),
]
# Pregas gástricas não são pregas circulares intestinais: manter entidades separadas.
GROUPS[4]=('pregas circulares intestinais',1223,[1215,1216])
for structure,representative,others in GROUPS:
 for index in [representative]+others:
  row=R[index].copy()
  if row['before'] in (1,2,5,6,7): continue
  row['after']=3 if index==representative else 4
  row['reason']=(f'{structure}: representante para retenção a longo prazo, escolhido entre as cópias existentes; AnKing primeiro, outros acervos antes de AnatoKing.'
                  if index==representative else
                  f'{structure}: outra recuperação mantida disponível; o único verde deste grupo é o card {R[representative]["cardId"]}.')
  row['status']='regra de anatomia solicitada por Davi em 28/09'
  focused[row['cardId']]=row
for index in [1197,1198]:
 row=R[index].copy();row['after']=1
 row['status']='pendência visual detectada, não recomendação de retenção'
 focused[row['cardId']]=row
rows=sorted(focused.values(),key=lambda r:r['index'])
for structure,representative,others in GROUPS:
 assert sum(focused[R[i]['cardId']]['after']==3 for i in [representative]+others)==1, structure
P['flags']=[r for r in rows if r['before']!=r['after']]
(BASE/'plan.json').write_text(json.dumps(P,ensure_ascii=False,indent=1))
(BASE/'bandeiras.json').write_text(json.dumps(rows,ensure_ascii=False,indent=1))
(BASE/'anatomia-estruturas.json').write_text(json.dumps([
 {'structure':s,'representative':R[a]['cardId'],'other_cards':[R[i]['cardId'] for i in b]}
 for s,a,b in GROUPS],ensure_ascii=False,indent=1))
print(json.dumps({'scope':len(rows),'flag_changes':len(P['flags']),'anatomy_groups':len(GROUPS)}))
