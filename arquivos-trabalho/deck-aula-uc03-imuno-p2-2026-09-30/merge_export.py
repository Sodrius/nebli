"""União isolada dos exports UC03 e treino: não altera nem esvazia o filtrado vivo."""
import json,sqlite3,zipfile,tempfile,hashlib,sys,re,collections
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parents[1]))
from nebli.decks import Anki
from nebli.rotulos import canonical
from nebli.package_uc import prepare_package,live_snapshot
A=Anki();deck=next(d for d in A('deckNames') if canonical(d)=='NEBLI::UC03');before=live_snapshot(A,deck)
expected=set(before['card_ids']);diff=json.loads((R/'diagnostico-exportacao-diferencas.json').read_text());missing=set(diff['missing']);assert len(missing)==237
with tempfile.TemporaryDirectory(dir=R) as tmp:
 t=Path(tmp);base=t/'base.sqlite';extra=t/'extra.sqlite'
 z1=zipfile.ZipFile(R/'diagnostico-exportacao-raw.apkg');z2=zipfile.ZipFile(R/'diagnostico-exportacao-treino.apkg')
 base.write_bytes(z1.read('collection.anki21'));extra.write_bytes(z2.read('collection.anki21'))
 c=sqlite3.connect(base);s=sqlite3.connect(extra)
 assert {r[0] for r in c.execute('select id from cards')}==expected-missing
 selected=[row for row in s.execute('select * from cards') if row[0] in missing];assert {r[0] for r in selected}==missing
 nids={r[1] for r in selected};nrows=[r for r in s.execute('select * from notes') if r[0] in nids]
 existing={r[0]:r for r in c.execute('select * from notes')}
 for row in nrows:
  if row[0] in existing:assert existing[row[0]]==row
  else:c.execute('insert into notes values ('+','.join('?' for _ in row)+')',row)
 normalization=[]
 for row in selected:
  v=list(row);assert v[15]!=0,'Não está no filtrado'
  # Localização/agendamento original na cópia: odid/odue guardam o deck e due originais.
  normalization.append({'cid':v[0],'did_before':v[2],'did_original':v[15],'queue_before':v[7],'due_original':v[14]})
  v[2]=v[15];v[8]=v[14];v[14]=v[15]=0
  if v[7]>=0:v[7]=v[6] if v[6]!=3 else 1
  c.execute('insert into cards values ('+','.join('?' for _ in v)+')',v)
 for row in s.execute('select * from revlog'):
  if row[1] in missing:c.execute('insert into revlog values ('+','.join('?' for _ in row)+')',row)
 # O export do pai também traz irmãos de notas selecionadas ainda no treino.
 for row in c.execute('select * from cards where odid!=0').fetchall():
  v=list(row);normalization.append({'cid':v[0],'did_before':v[2],'did_original':v[15],'queue_before':v[7],'due_original':v[14]})
  queue=v[7] if v[7]<0 else (v[6] if v[6]!=3 else 1)
  c.execute('update cards set did=odid,due=odue,odid=0,odue=0,queue=? where id=?',(queue,v[0]))
 for field in ['models','decks','dconf']:
  left=json.loads(c.execute('select '+field+' from col').fetchone()[0]);right=json.loads(s.execute('select '+field+' from col').fetchone()[0])
  for k,v in right.items():
   if field=='models' and k in left:assert left[k]==v,'Modelo divergente'
   if k not in left:left[k]=v
  if field=='decks':left={k:v for k,v in left.items() if canonical(v['name'])=='NEBLI::UC03' or canonical(v['name']).startswith('NEBLI::UC03::') or v['name']=='Default'}
  c.execute('update col set '+field+'=?',(json.dumps(left),))
 c.commit();assert c.execute('pragma integrity_check').fetchone()[0]=='ok';assert {r[0] for r in c.execute('select id from cards')}==expected
 # Campos, GUIDs e revlog de cada selecionado conservados; só saída do filtrado na cópia.
 for row in nrows:assert c.execute('select * from notes where id=?',(row[0],)).fetchone()==row
 for row in s.execute('select * from revlog'):
  if row[1] in missing:assert c.execute('select * from revlog where id=?',(row[0],)).fetchone()==row
 fields=' '.join(str(r[0]) for r in c.execute('select flds from notes'))+' '+c.execute('select models from col').fetchone()[0]
 media={};blobs={}
 for z,full in [(z1,True),(z2,False)]:
  for k,name in json.loads(z.read('media')).items():
   if not full and name not in fields and not name.startswith('_'):continue
   data=z.read(k)
   if name in blobs:assert blobs[name]==data,'Mídia divergente '+name
   else:blobs[name]=data
 c.close();s.close()
 raw=R/'UC03-uniao-isolada-raw.apkg'
 with zipfile.ZipFile(raw,'x',compression=zipfile.ZIP_DEFLATED) as z:
  z.write(base,'collection.anki21')
  # Mantém a DB de aviso legado que vem do export Anki, sem substituí-la pela coleção real.
  z.writestr('collection.anki2',z1.read('collection.anki2'))
  for i,(name,data) in enumerate(blobs.items()):media[str(i)]=name;z.writestr(str(i),data)
  z.writestr('media',json.dumps(media))
 result=prepare_package(raw,R/'NEBLI-UC03.apkg',expected,deck)
 after=live_snapshot(A,deck);assert before==after,'Coleção alterada concorrentemente'
 result.update({'uc':'UC03','profile':A('getActiveProfile'),'cards':len(expected),'filtered_cards_added':len(missing),'filtered_cards_included':len(normalization),'filtered_normalization':normalization,'live_card_ids_and_flags_unchanged':True,'fields_guids_and_revlog_preserved':True,'published':False,'import_test':'not_performed','method':'união local de exports; saída do filtrado somente na cópia'})
 (R/'NEBLI-UC03.publication-ready.json').write_text(json.dumps(result,ensure_ascii=False,indent=1))
 print({k:v for k,v in result.items() if k!='filtered_normalization'})
