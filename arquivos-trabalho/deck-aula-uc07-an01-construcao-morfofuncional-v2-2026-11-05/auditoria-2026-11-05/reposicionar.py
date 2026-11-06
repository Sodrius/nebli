from pathlib import Path
import sys,json,re,time
R=Path(__file__).resolve().parent.parent;ROOT=R.parents[1];sys.path.insert(0,str(ROOT))
from nebli.decks import Anki,escrita,em_tela
A=Anki();p=json.loads((R/'plan.json').read_text());rec=json.loads((R/'receipt.json').read_text());ns=A('notesInfo',notes=[x['nid'] for x in rec['notes']]+list(map(int,p['compartilhados'])));by={n['noteId']:n for n in ns};known={x['key']:x['nid'] for x in rec['notes']};seq=sorted([(e['order'],known[e['key']])for e in p['entries']]+[(e['order'],int(nid))for nid,e in p['compartilhados'].items()]);cs=A('cardsInfo',cards=[c for n in ns for c in n['cards']]);ci={c['cardId']:c for c in cs};ids=[]
for _,nid in seq:
 n=by[nid];ords={int(x)-1 for x in re.findall(r'\{\{c(\d+)::',n['fields']['Text']['value'])}if 'Text'in n['fields']else None
 ids.extend(c for c in sorted(n['cards'],key=lambda c:ci[c]['ord'])if (ords is None or ci[c]['ord']in ords)and ci[c]['type']==0 and ci[c]['reps']==0 and ci[c]['queue']==0)
q={'acao':'reposicionar','deck':p['deck'],'inicio':3970000,'cards':ids};req=ROOT/'arquivos-trabalho/anki-acao-pedido.json';res=ROOT/'arquivos-trabalho/anki-acao-resposta.json'
with escrita(A,'UC07 AN01 ordem dos novos',sync=False):
 if em_tela(A):raise RuntimeError('Anki em revisão; adiar reposição')
 req.write_text(json.dumps(q,ensure_ascii=False))
 for _ in range(200):
  time.sleep(.25)
  try:d=json.loads(res.read_text())
  except (OSError,ValueError):continue
  if d.get('pedido')==q:break
 else:raise RuntimeError('Sem resposta nativa')
 (R/'auditoria-2026-11-05/reposicao-nativa.json').write_text(json.dumps(d,ensure_ascii=False,indent=2));print(d)
