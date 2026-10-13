"""Exclui somente as retiradas de escopo já autorizadas, com APKG de recuperação."""
import json,sqlite3,tempfile,zipfile
from pathlib import Path
from nebli.decks import Anki,escrita,em_tela,now
H=Path(__file__).resolve().parent;ROOT=H.parents[1];A=Anki()
candidates={}
for short in ('fa01','rd02','pt03','mb39'):
    s=json.loads((H/f'{short}-snapshot.json').read_text());r=ROOT/s['run']
    for n in json.loads((r/'retirados.json').read_text()): candidates[n['nid']]={'short':short,**n}
live={n['noteId']:n for n in A('notesInfo',notes=list(candidates)) if n}
pending=[];eligible=[]
for nid,n in live.items():
    tags=n['tags']
    if not any(t.startswith('NEBLI::retirado::') for t in tags) or any(t.startswith('NEBLI::2026-') for t in tags):
        pending.append(nid)
    else: eligible.append(nid)
print('Já ausentes:',len(candidates)-len(live),'retiradas sem associação:',len(eligible),'preservadas por associação:',pending,flush=True)
(H/'exclusao-antes.json').write_text(json.dumps({'em':now(),'notes':list(live.values()),'candidates':candidates},ensure_ascii=False,indent=1))
with escrita(A,'retiradas de escopo autorizadas por Davi 12/10',sync=False):
    if em_tela(A)&set(eligible): raise SystemExit('Uma nota elegível entrou na revisão; adiar lote.')
    decks={c['deckName'] for c in A('cardsInfo',cards=[c for nid in eligible for c in live[nid]['cards']])}
    for i,deck in enumerate(sorted(decks)):
        backup=H/f'backup-retiradas-{i}.apkg'
        if not backup.exists():
            assert A('exportPackage',deck=deck,path=str(backup),includeSched=True)
        with zipfile.ZipFile(backup) as z, tempfile.TemporaryDirectory() as tmp:
            dbname=next(n for n in ('collection.anki21','collection.anki2') if n in z.namelist())
            z.extract(dbname,tmp);con=sqlite3.connect(str(Path(tmp)/dbname));saved={r[0] for r in con.execute('select id from notes')};con.close()
        needed={nid for nid in eligible if any(c['deckName']==deck for c in A('cardsInfo',cards=live[nid]['cards']))}
        assert needed<=saved,(deck,needed-saved)
    deleted=[]
    for start in range(0,len(eligible),15):
        batch=eligible[start:start+15]
        assert not em_tela(A)&set(batch)
        fresh=A('notesInfo',notes=batch)
        assert all(n and n['tags']==live[n['noteId']]['tags'] and n['fields']==live[n['noteId']]['fields'] for n in fresh)
        A('deleteNotes',notes=batch);deleted+=batch
        assert not any(A('notesInfo',notes=batch))
        (H/'exclusao-recibo.json').write_text(json.dumps({'em':now(),'deleted':deleted,'preservadas':pending,'ja_ausentes':len(candidates)-len(live)},indent=1))
print('Apagadas:',len(deleted),flush=True)
