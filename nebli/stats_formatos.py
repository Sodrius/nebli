"""Estatísticas descritivas por formato,UC e exposição; SQLite somente leitura.
Uso: python3 -m nebli.stats_formatos <saida>. Não altera Anki,agenda ou FSRS.
"""
from pathlib import Path
import json,re,sqlite3,statistics,sys,hashlib
from collections import defaultdict
from datetime import datetime,timezone

def tipo(fields,model):
 text=fields.get('Text',fields.get('Front',''))
 if 'data-nebli-organizacao' in text:return 'organizador'
 if ('Kenhub' in model and any(k.startswith('Imagem') for k in fields)) or 'Question Mask' in fields or re.search(r'image.?occlusion|oclus[aã]o',model,re.I):return 'identificacao-visual'
 return 'cloze' if '{{c' in text else 'pergunta-resposta'
def intervalo(last):
 return 'menos-de-1-dia' if last<=0 else '1-6-dias' if last<7 else '7-20-dias' if last<21 else '21-59-dias' if last<60 else '60+-dias'
def suspensao_observada(card,temporarios):
 original=str(card['id']) in temporarios
 return {'suspenso':card['queue']==-1 or original,'suspensao_original_registrada':original,'ativo_temporario_no_filtrado':bool(original and card.get('odid') and card['queue']!=-1)}
def resumo(events):
 valid=[x for x in events if 1<=x['ease']<=4 and x['type'] in (0,1,2)]
 reviews=[x for x in valid if x['type']==1 and x['lastIvl']>=1]
 return {'eventos':len(valid),'revisoes_espacadas':len(reviews),'acerto_revisoes':round(sum(x['ease']>1 for x in reviews)/len(reviews),4) if reviews else None,'intervalo_previo_mediano_dias':statistics.median([x['lastIvl'] for x in reviews]) if reviews else None,'tempo_mediano_ms':statistics.median([x['time'] for x in valid]) if valid else None,'falhas':sum(x['ease']==1 for x in valid),'aprendizagem_ou_reaprendizagem':sum(x['type'] in (0,2) for x in valid)}
def main(argv=None):
 out=Path((argv or sys.argv[1:])[0]);out.mkdir(parents=True,exist_ok=True)
 source=Path.home()/'Library/Application Support/Anki2/User 1/collection.anki2'
 try:temporarios=json.loads((source.parent/'nebli-estudo-suspensos.json').read_text())
 except FileNotFoundError:temporarios={}
 with sqlite3.connect('file:'+str(source)+'?mode=ro',uri=True) as db:
  db.create_collation('unicase',lambda a,b:(a.casefold()>b.casefold())-(a.casefold()<b.casefold()))
  db.row_factory=sqlite3.Row
  fn=defaultdict(list)
  for x in db.execute('select ntid,ord,name from fields order by ntid,ord'):fn[x['ntid']].append(x['name'])
  ns={}
  for n in db.execute("select n.id,n.mid,n.flds,n.tags,t.name from notes n join notetypes t on t.id=n.mid where n.tags like '%NEBLI%'"):
   fields=dict(zip(fn[n['mid']],n['flds'].split('\x1f')));uc=re.search(r'uc\d\d',n['tags'],re.I);ns[n['id']]={'formato':tipo(fields,n['name']),'uc':uc[0].upper() if uc else 'sem-UC','frente':fields.get('Text',fields.get('Front',fields.get('Nome PT',''))),'comentario':fields.get('NEBLI_Comentario',''),'aulas':sorted(set(re.findall(r'NEBLI::2026-[^ ]+',n['tags']))),'conteudo_sha256':hashlib.sha256(json.dumps({'frente':fields.get('Text',fields.get('Front','')),'extra':fields.get('Extra',''),'modelo':n['name']},ensure_ascii=False,sort_keys=True).encode()).hexdigest()}
  cards={c['id']:dict(c) for c in db.execute('select id,nid,reps,lapses,queue,type,ivl,odid from cards') if c['nid'] in ns};events=defaultdict(list)
  for e in db.execute('select id,cid,ease,ivl,lastIvl,time,type from revlog'):
   if e['cid'] in cards:events[e['cid']].append(dict(e))
 by=defaultdict(list);csets=defaultdict(set);individual=[]
 for cid,c in cards.items():
  n=ns[c['nid']];es=events[cid];individual.append({'cid':cid,'nid':c['nid'],**n,'reps':c['reps'],'lapses':c['lapses'],**suspensao_observada(c,temporarios),'idade_primeiro_estudo_dias':round((datetime.now(timezone.utc).timestamp()*1000-min(x['id'] for x in es))/86400000,1) if es else None,**resumo(es)})
  for e in es:
   key=(n['uc'],n['formato'],intervalo(e['lastIvl']),'revisao' if e['type']==1 else 'aprendizagem-ou-outro');by[key].append(e);csets[key].add(cid)
 grouped=[{'uc':k[0],'formato':k[1],'intervalo_previo':k[2],'fase':k[3],'cards':len(csets[k]),**resumo(v)} for k,v in sorted(by.items())]
 limits=['O formato é o atual da nota; não há snapshot do formato em cada revisão passada.','Associação descritiva,não efeito causal do formato.','Comparar UC,assunto,intervalo,idade e exposição; o conteúdo e a seleção pessoal confundem a taxa.','Grupos pequenos e cards sem revisão espaçada não sustentam preferência de retenção.','Facilidade percebida deve ser confrontada com X e comentário literal; suspensão sozinha não é crítica.']
 data={'somente_leitura':True,'gerado_em':datetime.now(timezone.utc).isoformat(),'cards':len(cards),'notas':len(ns),'eventos':sum(map(len,events.values())),'limites':limits,'grupos':grouped};(out/'resumo.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));(out/'cards.json').write_text(json.dumps(individual,ensure_ascii=False,indent=1));print(json.dumps({k:data[k] for k in ('cards','notas','eventos','somente_leitura')}))
if __name__=='__main__':main()
