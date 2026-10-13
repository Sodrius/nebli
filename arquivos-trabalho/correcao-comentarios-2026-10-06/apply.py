"""Dry-run by default; updates only reviewed fields and adds independent etymology targets."""
import html,json,re,sqlite3,sys
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki,escrita,in_scope
from nebli.rotulos import canonical
from nebli.explicacoes import open_store,card_hash,style_version,STYLE
from tabs import TABS,OLD
P=Path(__file__).resolve().parent
A=Anki()
if '--verify' in sys.argv:
    receipt=json.loads((P/'receipt.json').read_text())
    before=json.loads((P/'apply-before.json').read_text())
    cs=json.loads((P/'changes.json').read_text())
    ns=A('notesInfo',notes=[c['nid'] for c in cs])
    byid={n['noteId']:n for n in ns}
    assert all(byid[c['nid']]['fields'][k]['value']==v for c in cs for k,v in c['fields'].items())
    assert all(byid[c['nid']]['cards']==next(n['cards'] for n in before['notes'] if n['noteId']==c['nid']) for c in cs)
    allcards=A('cardsInfo',cards=[c['cardId'] for c in before['cards']]+[cid for n in receipt['new_notes'] for cid in n['cards']])
    db=open_store()
    tab_issues=[]
    for c in allcards:
        row=db.execute('select hash,status,texto from explicacoes where card_id=?',(c['cardId'],)).fetchone()
        values=[v['value'] for v in sorted(c['fields'].values(),key=lambda f:f['order'])]
        if not row or row[0]!=card_hash(values,c['ord']) or row[1]!='ok' or not row[2]:tab_issues.append(c['cardId'])
    commented=A('notesInfo',notes=A('findNotes',query='NEBLI_Comentario:_*'))
    unmarked=[{'nid':n['noteId'],'comment':n['fields']['NEBLI_Comentario']['value']} for n in commented if 'CORRIGIDO' not in n['fields']['NEBLI_Comentario']['value']]
    result={'field_readback':'ok','existing_ids_preserved':True,'affected_cards':len(allcards),'tab_hash_or_status_issues':tab_issues,'comments':len(commented),'unmarked_comments':unmarked,'sync':receipt['sync']}
    (P/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=False));sys.exit(bool(tab_issues))
changes=json.loads((P/'changes.json').read_text())
newnotes=json.loads((P/'new-notes.json').read_text())
snapshot={n['noteId']:n for n in json.loads((P/'snapshot.json').read_text())}
ids=sorted({c['nid'] for c in changes}|{OLD[str(cid)]['note_id'] for cid in TABS})
live={n['noteId']:n for n in A('notesInfo',notes=ids)}
cards=A('cardsInfo',cards=[cid for n in live.values() for cid in n['cards']])
assert A('getActiveProfile')=='User 1'
assert all(in_scope(c['deckName']) for c in cards)
for c in changes:
    n=live[c['nid']]
    assert n['cards']==snapshot[c['nid']]['cards'],('Irmãos mudaram',c['nid'])
    for k,before in c['before'].items():
        assert n['fields'][k]['value'] in [before,c['fields'][k]],('Edição concorrente',c['nid'],k)
    if 'Text' in c['fields']:
        cz=lambda s:set(re.findall(r'\{\{c(\d+)::',s))
        assert cz(c['before']['Text'])==cz(c['fields']['Text']),('Índices de cloze mudaram',c['nid'])
    for value in c['fields'].values():
        for asset in re.findall(r'<img[^>]+src="([^"]+)"',value):
            assert (Path.home()/'Library/Application Support/Anki2/User 1/collection.media'/asset).exists(),asset
db=open_store();db.row_factory=sqlite3.Row
saved={row['card_id']:dict(row) for row in db.execute('select * from explicacoes')}
for cid in TABS:
    assert saved[cid]['texto'] in [OLD[str(cid)]['texto'],TABS[cid]],('Tab concorrente',cid)
by_note={}
for c in cards: by_note.setdefault(c['note'],[]).append(c)
for n in newnotes:
    assert len(by_note[n['parent']])==1
    assert len(re.findall(r'\{\{c1::',n['Text']))==1
    assert saved.get(by_note[n['parent']][0]['cardId'],{}).get('status')=='ok'

if '--apply' not in sys.argv:
    media=Path.home()/'Library/Application Support/Anki2/User 1/collection.media'
    header='<html><meta charset="utf-8"><style>body{font:21px Arial;background:#fff;color:#222;margin:12px}img{max-width:100%;height:auto}section{padding:14px 0;border-bottom:1px solid #888}h2{font-size:14px}table{color:#222}</style>'
    all_sections=[]
    for c in changes:
        f={k:v['value'] for k,v in live[c['nid']]['fields'].items()};f.update(c['fields'])
        content=f.get('Text',f.get('Header',''))+'<hr>'+f.get('Extra',f.get('Remarks',''))
        content=re.sub(r'\{\{c\d+::(.*?)(?:::[^}]*)?\}\}',r'<b style="color:#23539b">\1</b>',content)
        content=re.sub(r'src="([^"]+)"',lambda m:'src="'+(media/m[1]).as_uri()+'"',content)
        s=f'<section><h2>{c["nid"]}</h2>{content}</section>'
        all_sections.append(s)
        if c['nid'] in [1791023355444,1791023362817,1791023364242,1791023353818,1791023354569,1790999833204,1790999835379,1791023357394,1791023270196,1790979869685]:
            (P/f'preview-{c["nid"]}.html').write_text(header+s+'</html>')
    (P/'preview.html').write_text(header+''.join(all_sections)+'</html>')
    result={'notes':len(changes),'existing_cards_in_scope':len(cards),'new_notes':len(newnotes),'tab_text_updates':len(TABS),'preconditions':'ok','writes_to_anki':0}
    (P/'preflight.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result));sys.exit()

stamp=lambda:datetime.now(timezone.utc).isoformat()
backup=P/'apply-before.json'
if not backup.exists(): backup.write_text(json.dumps({'notes':list(live.values()),'cards':cards,'tabs':{cid:saved.get(cid) for cid in [c['cardId'] for c in cards]}},ensure_ascii=False,indent=2))
def log(**d):
    with (P/'journal.jsonl').open('a') as h:h.write(json.dumps(dict(d,at=stamp()),ensure_ascii=False)+'\n')
new_created=[];updated_tabs=[]
with escrita(A,'Comentários e padrões 06/10/2026'):
    for c in changes:
        cur=A('notesInfo',notes=[c['nid']])[0]
        for k,before in c['before'].items():assert cur['fields'][k]['value'] in [before,c['fields'][k]],('Mudou durante aplicação',c['nid'],k)
        A('updateNoteFields',note={'id':c['nid'],'fields':c['fields']})
        log(op='fields',nid=c['nid'],fields=list(c['fields']))
    for n in newnotes:
        parent=live[n['parent']]; pc=by_note[n['parent']][0]
        existing=A('findNotes',query='tag:'+n['key'])
        assert len(existing)<=1
        if existing: nid=existing[0]
        else:
            fields={k:'' for k in parent['fields']}
            fields.update(Text=n['Text'],Extra=n['Extra'])
            tags=[t for t in parent['tags'] if not t.startswith(('NEBLI_comentario','NEBLI::feedback-split'))]+[n['key']]
            nid=A('addNote',note={'deckName':canonical(pc['deckName']),'modelName':parent['modelName'],'fields':fields,'tags':tags,'options':{'allowDuplicate':False}})
            assert nid
            log(op='add',nid=nid,parent=n['parent'],key=n['key'])
            ni=A('notesInfo',notes=[nid])[0]
            if pc['queue']==-1:A('suspend',cards=ni['cards'])
        ni=A('notesInfo',notes=[nid])[0]
        assert ni['fields']['Text']['value']==n['Text']
        new_created.append({'nid':nid,'parent':n['parent'],'cards':ni['cards'],'key':n['key']})
    after=A('notesInfo',notes=ids)
    after_byid={n['noteId']:n for n in after}
    for c in changes:
        assert after_byid[c['nid']]['cards']==live[c['nid']]['cards']
        assert after_byid[c['nid']]['tags']==live[c['nid']]['tags']
        for k,v in c['fields'].items(): assert after_byid[c['nid']]['fields'][k]['value']==v,(c['nid'],k)
    all_cids=[c['cardId'] for c in cards]+[cid for n in new_created for cid in n['cards']]
    after_cards=A('cardsInfo',cards=all_cids)
    oldcards={c['cardId']:c for c in cards}
    newmap={cid:n for n in new_created for cid in n['cards']}
    differences=[]
    for c in after_cards:
        cid=c['cardId']
        if cid in oldcards:
            for k in ['queue','type','due','interval','factor','reps','lapses','left','odue','odid','flags']:
                if c.get(k)!=oldcards[cid].get(k): differences.append([cid,k,oldcards[cid].get(k),c.get(k)])
            old=saved.get(cid)
            if not old or old['status']!='ok':continue
            text=TABS.get(cid,old['texto'])
        else:
            parent_cid=by_note[newmap[cid]['parent']][0]['cardId']
            old=saved[parent_cid]
            text=TABS.get(parent_cid,old['texto'])
            answer=re.search(r'\{\{c1::(.*?)\}\}',c['fields']['Text']['value'])[1]
            text='Neste alvo, recupere '+re.sub('<[^>]+>','',answer)+'.\n'+text
        assert text
        values=[v['value'] for v in sorted(c['fields'].values(),key=lambda f:f['order'])]
        version=style_version(STYLE.read_text()) if cid in TABS or cid in newmap else old['estilo']
        db.execute('insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)',(cid,c['note'],card_hash(values,c['ord']),'ok',text,'',version,'revisao-comentarios-2026-10-06',stamp()))
        updated_tabs.append(cid)
    db.commit()
    receipt={'changed_notes':len(changes),'existing_cards':len(cards),'new_notes':new_created,'tab_text_updates':len(TABS),'tabs_saved':len(updated_tabs),'personal_state_differences':differences,'field_readback':'ok','at':stamp()}
    (P/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2))
    (P/'after.json').write_text(json.dumps({'notes':after,'cards':after_cards},ensure_ascii=False,indent=2))
    assert not differences,('Mudanças pessoais concorrentes; nenhum estado pessoal sobrescrito',differences)
receipt['sync']='AnkiConnect sync retornou sem erro; aparelhos não conferidos'
(P/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2))
print(json.dumps({k:(len(v) if k=='new_notes' else v) for k,v in receipt.items()},ensure_ascii=False))
