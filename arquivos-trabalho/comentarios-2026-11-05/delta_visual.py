import json,re
from pathlib import Path
C=Path(__file__).parent;P=json.load(open(C/'propostas.json'))
for p in P.values():
 for k,v in list(p['fields'].items()):
  if k=='Extra':
   v=v.replace('Host defenses enable invasion','Impaired host defenses favor invasion')
   v=v.replace('font-size:16px;','font-size:16px!important;').replace('style="padding:5px;','style="font-size:16px!important;padding:5px;')
   p['fields'][k]=v
P['1792786399910']['fields']['Extra']=P['1792786399910']['fields']['Extra'].replace('rnai-dicer-risc-20261031.png','nebli-bm54-sirna-via-p22-20261025.jpeg')
P['1792081484462']['fields']['Extra']='Post-primary TB commonly affects upper-lobe segments. The arrows on this radiograph indicate a right upper-lobe cavity. The image illustrates location; it does not by itself demonstrate the oxygen-related mechanism.<br><br><img src="nebli-0511-tb-merck.jpg" style="width:100%;max-width:950px;height:auto">'
P['1792328914296']['fields']['Text']='<div data-nebli-organizacao="true"><b>Segmentos da medula espinal</b><br><b>Corno lateral simpático</b>: {{c1::T1–L2}}<br><b>Intumescência cervical</b>: {{c2::C5–T1}}<br><b>Intumescência lombossacral</b>: {{c2::L2–S3}}</div>'
P['1792328914296']['fields']['Extra']='The sympathetic lateral horn is prominent in the thoracolumbar cord. Enlargements contain more neurons serving the limbs; these are spinal-segment ranges, not vertebral levels. L2–S3 follows the course guide and the external spinal-cord anatomy reference.<br><br>'
for label,name in [('Cervical','cervical'),('Thoracic, with lateral horn','thoracic'),('Lumbar','lumbar'),('Sacral','sacral')]:P['1792328914296']['fields']['Extra']+='<b>'+label+'</b><br><img src="nebli-0511-medula-'+name+'.png" style="width:100%;max-width:600px;height:auto"><br>'
P['1793476864207']['fields']['Extra']='GLP-1 (glucagon-like peptide 1) and GIP (glucose-dependent insulinotropic polypeptide) enhance glucose-dependent insulin release. CCK (cholecystokinin) stimulates pancreatic enzymes and gallbladder contraction. Enterochromaffin serotonin signals to enteric nerves; gastric ghrelin promotes hunger. These labels describe predominant products, not exclusive one-hormone cell types.<br><br><picture><source media="(max-width:600px)" srcset="nebli-0511-entero-coluna.png"><img src="nebli-0511-entero-tipos.jpg" style="width:100%;max-width:950px;height:auto"></picture>'
P['1792328914296']['motivo']+=' Fonte conferida distingue nível medular de vértebra e indica L2–S3; figura vertebral substituída por quatro cortes reais da medula.'
P['1792081484462']['motivo']+=' Revisão independente rejeitou RX anterior por não demonstrar ápice; substituído por imagem institucional com cavidade visível e setas.'
json.dump(P,open(C/'propostas.json','w'),ensure_ascii=False,indent=1)
n=json.load(open(C/'novo-scid.json'));n['fields']['Extra']=n['fields']['Extra'].replace('font-size:16px;','font-size:16px!important;').replace('style="padding:5px;','style="font-size:16px!important;padding:5px;');json.dump(n,open(C/'novo-scid.json','w'),ensure_ascii=False,indent=1)
