"""Dry-run offline com snapshots vivos: nenhuma escrita externa. Text/cloze apenas."""
import hashlib,html,importlib.util,json,re,sys
from pathlib import Path
HERE=Path(__file__).parent; ROOT=HERE.parents[1]; sys.path.insert(0,str(ROOT))
MODEL='NEBLI AnKing independente - v3'
MODELS=json.loads((HERE/'models.json').read_text())
NOTES={n['noteId']:n for n in json.loads((HERE/'live-notes.json').read_text()) if n}
NOTES.update({n['noteId']:n for n in json.loads((HERE/'busca/alternativos-notes.json').read_text()) if n})
for filename in ['extra-notes.json','final-notes.json']:
 NOTES.update({n['noteId']:n for n in json.loads((HERE/'busca'/filename).read_text()) if n})
LIVE={n['noteId']:n for n in NOTES.values() if any(t.startswith('NEBLI::') for t in n['tags'])}
CI={c['cardId']:c for c in json.loads((HERE/'live-cards.json').read_text())}
MEDIA=Path.home()/'Library/Application Support/Anki2/User 1/collection.media'
RESOURCE={'Sketchy','Sketchy 2','Sketchy Extra','Bootcamp','Pixorize','Physeo','OME','Picmonic','Additional Resources','Boards and Beyond','Pathoma','First Aid','ankihub_id','One by one','NEBLI_Comentario','NEBLI_Resposta'}
def h(x): return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def values(n): return {k:v['value'] for k,v in n['fields'].items()}
def load(folder):
 s=importlib.util.spec_from_file_location(folder,HERE/folder/'spec-revisada.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main(folder):
 s=load(folder);tag=f'NEBLI::{s.LESSON}'; entries=[];shared={}; issues=[]
 def share(nid,why,ords=None):
  n=LIVE.get(nid)
  if not n: issues.append(f'Compartilhado ausente {nid}');return
  ids=[cid for cid in n['cards'] if ords is None or CI[cid]['ord'] in ords]
  if ords is not None and {CI[cid]['ord'] for cid in ids}!=set(ords): issues.append(f'Irmão ausente em cópia viva {nid}; não recriar apagado')
  if not ids: issues.append(f'Compartilhado sem card {nid}')
  shared[str(nid)]={'reason':why,'card_ids':ids,'fields_hash':h(values(n)),'cards_before':{str(cid):{k:CI[cid][k] for k in ['ord','flags','queue','type','reps','lapses','due','interval','deckName']} for cid in ids},'tags_before':n['tags']}
 for nid,why in s.COMPARTILHADOS.items():
  # Na aula de complemento, apenas c2/C5a desse compartilhado; demais irmãos são de Inflamação.
  share(nid,why,[1] if folder=='complemento' and nid==1790253143896 else None)
 for order,c in enumerate(s.CARDS,1):
  src=c.get('src'); source=NOTES.get(src);base=values(source) if source else {}
  if src and not source: issues.append(f'Fonte ausente {src}');continue
  if src:
   copies=[n for n in LIVE.values() if f'NEBLI::source::nid-{src}' in n['tags']]
   if copies:
    if len(copies)!=1: issues.append(f'Identidade duplicada {src}');continue
    share(copies[0]['noteId'],'Mesma identidade AnKing já viva: '+c['alvo'],[k-1 for k in c['flags']]);continue
  fields={k:'' for k in MODELS[MODEL]['fields']}
  for k in fields:
   if k in base and k not in RESOURCE: fields[k]=base[k]
  for k,v in [('Text',c.get('text')),('Extra',c.get('extra'))]:
   if v is not None: fields[k]=v
  fields.update(c.get('fields_override',{}))
  fields['Extra']=c.get('extra_prefix','')+fields['Extra']
  # Remover apenas a ocultação de irmãos excluídos; o contexto visível permanece.
  fields['Text']=re.sub(r'\{\{c(\d+)::(.*?)(?:::(.*?))?\}\}',lambda m:m[0] if int(m[1]) in c['flags'] else m[2],fields['Text'],flags=re.S)
  got={int(n) for n in re.findall(r'\{\{c(\d+)::',fields['Text'])}
  if got!=set(c['flags']): issues.append(f'Clozes {c["key"]}: {got} != {set(c["flags"])}')
  if not fields['Text'].strip(): issues.append(f'Frente vazia {c["key"]}')
  imgs=re.findall(r'''(?:src\s*=\s*["'])([^"']+)''',' '.join(fields.values()),re.I)
  for img in imgs:
   if img.startswith(('http:','https:','data:')): issues.append(f'Mídia remota {c["key"]}: {img}')
   elif not (MEDIA/html.unescape(img)).is_file(): issues.append(f'Mídia ausente {c["key"]}: {img}')
  tags=[tag,'NEBLI::escopo::aula',f'NEBLI::objetivo::{c["bloco"]}',f'NEBLI::ordem::{s.SHORT}-{order:02}',f'NEBLI::run::{s.RUN_ID}']+c.get('extra_tags',[])
  origin=c.get('origin') or ('AnKing' if src else 'Autoral')
  tags += [f'NEBLI::origem::{origin}']
  if src: tags += source['tags']+[f'NEBLI::source::nid-{src}']
  else: tags += [f'NEBLI::author::uc03-{s.SHORT}-{c["key"]}']
  e=dict(c);e.update(order=order,fields=fields,fields_hash=h(fields),source_fields_hash=h(base) if src else None,model=MODEL,
   origin=origin,tags=sorted(set(tags)),media=imgs,cards=[{'ord':n-1,'n':n,'flag':flag} for n,flag in sorted(c['flags'].items())]);entries.append(e)
 plan=dict(run_id=s.RUN_ID,short=s.SHORT,lesson_id=s.LESSON,deck=s.DECK,profile='User 1',E1='não aplicável — pedido explícito (só decks)',
  criterios=s.CRITERIOS,entries=entries,shared=shared,excluidos=s.EXCLUIDOS,fora_do_recorte=s.FORA_DO_RECORTE,issues=issues,
  model_snapshot=MODELS[MODEL],source_evidence=['fontes/complemento-drive.txt','fontes/inflamacao-drive.txt','fontes/abbas.txt','fontes/provas-complemento.json','fontes/provas-inflamacao.json'])
 plan['selection_hash']=h(entries)
 plan['totals']={'notes':len(entries),'cards':sum(len(e['cards']) for e in entries),'flags':{str(f):sum(x['flag']==f for e in entries for x in e['cards']) for f in (3,4)},
  'origin_cards':{o:sum(len(e['cards']) for e in entries if e['origin']==o) for o in ['AnKing','AnKing-MCAT','Autoral']},'shared_notes':len(shared),'shared_cards':sum(len(n['card_ids']) for n in shared.values())}
 (HERE/folder/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=1))
 print(folder,plan['totals'],'ISSUES',issues)
 if issues: raise SystemExit(1)
if __name__=='__main__':
 for folder in sys.argv[1:] or ['complemento','inflamacao']: main(folder)
