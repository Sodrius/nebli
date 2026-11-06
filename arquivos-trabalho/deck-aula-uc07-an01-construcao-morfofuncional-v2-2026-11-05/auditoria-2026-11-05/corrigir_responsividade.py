from pathlib import Path
import json,sys
from datetime import datetime,timezone
R=Path(__file__).resolve().parent.parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki,escrita,em_tela
A=Anki();ids=[1792588686968,1792588686971,1792588686967,1792588686961,1792588686964];p=json.loads((R/'plan.json').read_text());style='<style>.mobile .ankihub-view-note{box-sizing:border-box;max-width:100%;margin-right:0;left:auto;white-space:normal;overflow-wrap:anywhere}</style>'
ns=A('notesInfo',notes=ids);patch={n['noteId']:n['fields']['Extra']['value']+style for n in ns if style not in n['fields']['Extra']['value']}
with escrita(A,'UC07 AN01 correção de largura do botão no celular',sync=False):
 if em_tela(A)&set(ids):raise RuntimeError('Nota afetada em tela')
 A('multi',actions=[{'action':'updateNoteFields','params':{'note':{'id':nid,'fields':{'Extra':v}}}}for nid,v in patch.items()])
for nid,v in patch.items():p['compartilhados'][str(nid)]['fields']['Extra']=v
(R/'plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2));(R/'plan-aplicado.json').write_text(json.dumps(p,ensure_ascii=False,indent=2));f=R/'auditoria-2026-11-05/campos-mantidos.json';d=json.loads(f.read_text())
for nid,v in patch.items():d.setdefault(str(nid),{})['Extra']=v
f.write_text(json.dumps(d,ensure_ascii=False,indent=2));after=A('notesInfo',notes=ids);assert all(n['fields']['Extra']['value']==p['compartilhados'][str(n['noteId'])]['fields']['Extra']for n in after)
(R/'auditoria-2026-11-05/responsividade-recibo.json').write_text(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'notas':list(patch),'campos':['Extra'],'alteracao':'CSS local do botão AnkiHub para não alargar página móvel; sem mudar texto/cards/agendamento'},ensure_ascii=False,indent=2));print(len(patch),'notas com CSS responsivo')
