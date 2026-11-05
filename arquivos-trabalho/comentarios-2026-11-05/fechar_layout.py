import json,re,sys
from pathlib import Path
C=Path(__file__).parent.resolve();sys.path.insert(0,str(C.parents[1]));from nebli.decks import Anki,escrita,em_tela
A=Anki();P=json.load(open(C/'propostas.json'));updates=[]
for nid in [1791626776253,1792588686960]:
 n=A('notesInfo',notes=[nid])[0]
 if nid==1791626776253:
  old=n['fields']['Text']['value'];css='<style>.nebli-reference-table,.nebli-reference-table *{font-size:16px!important}.nebli-reference-table{width:100%!important;table-layout:fixed}.nebli-reference-table td,.nebli-reference-table th{overflow-wrap:anywhere;white-space:normal;padding:4px}</style>'
  t=re.sub(r'<table\b([^>]*)>',lambda m:'<table'+re.sub(r'\sclass="[^"]*"','',m[1])+' class="nebli-reference-table">',old,count=1);fields={'Text':css+t}
 else:
  old=n['fields']['Extra']['value'];fields={'Extra':old+'<style>.ankihub-view-note{max-width:100%;font-size:14px!important;white-space:normal;overflow-wrap:anywhere;display:inline-block;box-sizing:border-box}</style>'}
 updates.append({'nid':nid,'antes':n['fields']['Text'if nid==1791626776253 else'Extra']['value'],'fields':fields})
with escrita(A,'comentários05/11: tabela original e rodapé no celular',sync=False):
 for u in updates:
  assert u['nid']not in em_tela(A)
  key=next(iter(u['fields']));assert A('notesInfo',notes=[u['nid']])[0]['fields'][key]['value']==u['antes']
  A('updateNoteFields',note={'id':u['nid'],'fields':u['fields']});P[str(u['nid'])]['fields'].update(u['fields'])
 # Onze irmãos antigos sem alvo: dez estavam ativos; nenhum tem histórico de estudo.
 empty=json.load(open(C/'irmaos-sem-alvo.json'));pending=[r['cardId']for r in empty if r['queue']!=-1];assert all(r['reps']==0 for r in empty)
 assert not({r['note']for r in empty}&em_tela(A));A('suspend',cards=pending)
(C/'propostas.json').write_text(json.dumps(P,ensure_ascii=False,indent=1));(C/'layout-final-recibo.json').write_text(json.dumps({'updates':updates,'irmaos_sem_alvo_suspensos':pending,'excluidos':[]},ensure_ascii=False,indent=1));print('layout2notas;10irmãos vazios suspensos,11preservados;0exclusões')
