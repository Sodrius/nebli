"""Correções encontradas na renderização; registro separado do lote aplicado."""
import json,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parents[1]))
from nebli.decks import Anki,escrita
from nebli.preflight import chunks
A=Anki();P=json.loads((BASE/'plan.json').read_text());N={n['noteId']:n for n in P['notes']}
name='NEBLI UC08 Visceral Anatomy v1'
before=A('modelStyling',modelName=name)['css']
after=before+'''\n/* IDs antigos têm especificidade maior: garantir contraste noturno. */
.nightMode.card [id], .night_mode .card [id] { color: inherit !important; }
.nightMode.card #answer, .night_mode .card #answer { color: #4297f9 !important; }
'''
updates={
 1790173050491:'Bactérias usam ferro em enzimas essenciais. O hospedeiro o mantém ligado a proteínas, dificultando o crescimento microbiano. Sideróforos capturam esse ferro e permitem sua entrada na bactéria.<details><summary>Regulação por Fur</summary>Com pouco ferro, o repressor Fur perde sua ação: a bactéria aumenta a produção de sistemas de captação.</details>',
 1790173050816:'Respiração anaeróbia usa cadeia transportadora, com aceptores como nitrato ou sulfato no lugar de O₂. Fermentação transfere elétrons do NADH para uma molécula orgânica, regenerando NAD⁺ para a glicólise continuar produzindo ATP.<details><summary>Uma distinção importante</summary>A respiração anaeróbia também pode usar aceptores orgânicos, como fumarato. O que a distingue da fermentação é o uso da cadeia respiratória.</details>',
}
# Figuras de apoio continuam disponíveis, sem ocupar três telas de explicação.
for nid in [1790271540358,1790271540623]:
 extra=N[nid]['after']['Extra'];i=extra.index('<img')
 updates[nid]=extra[:i].rstrip('<br>')+'<details><summary>Ver imagens de apoio</summary>'+extra[i:]+'</details>'
ferm=N[1790173050816]['after']['Extra'];i=ferm.index('<img')
updates[1790173050816]+='<details><summary>Ver esquema da aula</summary>'+ferm[i:]+'</details>'
record={'status':'planejado','reason':'Contraste testado em WebKit; retirar figura com texto distorcido; recolher imagens/nuance secundárias.',
 'model':{'name':name,'before':before,'after':after},
 'notes':[{'noteId':nid,'before':N[nid]['after']['Extra'],'after':extra} for nid,extra in updates.items()]}
path=BASE/'acabamento-recibo.json'
assert not path.exists()
path.write_text(json.dumps(record,ensure_ascii=False,indent=1))
def states(ids):
 return {c['cardId']:{k:c[k] for k in ['note','ord','flags','type','queue','due','interval','reps','lapses','factor','left']} for b in chunks(ids,100) for c in A('cardsInfo',cards=b)}
ids=[c['cardId'] for c in json.loads((BASE/'cards-after.json').read_text())]
with escrita(A,'Acabamento visual do lote 28/09'):
 current=states(ids)
 assert A('modelStyling',modelName=name)['css']==before
 for r in record['notes']:
  assert A('notesInfo',notes=[r['noteId']])[0]['fields']['Extra']['value']==r['before']
 A('updateModelStyling',model={'name':name,'css':after})
 for r in record['notes']:
  A('updateNoteFields',note={'id':r['noteId'],'fields':{'Extra':r['after']}})
  assert A('notesInfo',notes=[r['noteId']])[0]['fields']['Extra']['value']==r['after']
 assert A('modelStyling',modelName=name)['css']==after
 assert states(ids)==current,'Histórico/flags mudou durante a verificação'
 record['status']='conferido';path.write_text(json.dumps(record,ensure_ascii=False,indent=1))
record['sync']='retornou sem erro';path.write_text(json.dumps(record,ensure_ascii=False,indent=1))
cards=[c for b in chunks(ids,100) for c in A('cardsInfo',cards=b)]
(BASE/'cards-after-final.json').write_text(json.dumps(cards,ensure_ascii=False,indent=1))
print('Acabamento aplicado e conferido: quatro versos e contraste de um modelo. Sync sem erro.')
