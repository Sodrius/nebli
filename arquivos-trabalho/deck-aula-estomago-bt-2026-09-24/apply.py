"""Install X5 copies under a write lock while keeping all originals intact."""
import copy,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen

HERE=Path(__file__).parent
ROOT=HERE.parent
PLAN=json.loads((HERE/'plan.json').read_text(encoding='utf-8'))
LOCK=ROOT/'ANKI-ESCRITA.lock'
TAG='NEBLI::'+PLAN['lesson_id']
MODELS={
 'AnKingOverhaul (AnKing Step Deck / AnKingMed)':'NEBLI UC08 Stomach AnKing v1',
 'AnKingOverhaul (LLU Histology / SLin_LLUSOM)':'NEBLI UC08 Stomach LLU v1',
 'Cloze-AnKingMaster-v3 (Histology / ploirodon)':'NEBLI UC08 Stomach Histology v1',
}

def call(action,**params):
    data=json.dumps(dict(action=action,version=6,params=params)).encode()
    with urlopen(Request('http://127.0.0.1:8765',data=data,headers={'Content-Type':'application/json'}),timeout=120) as res:r=json.load(res)
    if r['error']:raise RuntimeError(f'{action}: {r["error"]}')
    return r['result']
def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def ident(e):return ('NEBLI::source::nid-'+str(e['source_nid'])) if e['source_nid'] else ('NEBLI::authored::'+e['key'])
def save(name,x):(HERE/name).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')

def check():
    assert call('getActiveProfile')==PLAN['profile']
    assert not LOCK.exists(),f'Lock exists: {LOCK}'
    assert not call('findCards',query=f'deck:"{PLAN["target_deck"]}"')
    source_ids=[e['source_nid'] for e in PLAN['entries'] if e['source_nid']]
    sources={n['noteId']:n for n in call('notesInfo',notes=source_ids)}
    for e in PLAN['entries']:
        if e['source_nid']:
            assert digest({k:v['value'] for k,v in sources[e['source_nid']]['fields'].items()})==e['source_fields_hash'],e['source_nid']
        assert not call('findNotes',query=f'tag:"{ident(e)}"'),ident(e)
    media=Path(call('getMediaDirPath'))
    for e in PLAN['entries']:
        for value in e['fields'].values():
            for name in re.findall(r'<img[^>]*src="([^"]+)"',value):
                assert (media/name).is_file(),name
    return list(sources.values())

def install():
    sources=check()
    with LOCK.open('x',encoding='utf-8') as f:f.write(json.dumps(dict(executor='Codex',lesson=PLAN['lesson_id'],at=datetime.now(timezone.utc).isoformat())))
    journal=HERE/'journal.jsonl'
    try:
        save('before-apply.json',dict(sources=sources,profile=PLAN['profile']))
        call('createDeck',deck=PLAN['target_deck'])
        for src in sorted({e['source_model'] for e in PLAN['entries']}):
            model=MODELS[src]
            fields=call('modelFieldNames',modelName=src)
            templates=copy.deepcopy(call('modelTemplates',modelName=src))
            css=call('modelStyling',modelName=src)['css']
            if model not in call('modelNames'):
                call('createModel',modelName=model,inOrderFields=fields,css=css,isCloze=True,cardTemplates=[dict(Name=k,**v) for k,v in templates.items()])
            assert call('modelFieldNames',modelName=model)==fields
        rows=[]
        for e in PLAN['entries']:
            tags=list(dict.fromkeys(e['source_tags']+[TAG,ident(e),'NEBLI::origem::'+e['origin']]))
            nid=call('addNote',note=dict(deckName=PLAN['target_deck'],modelName=MODELS[e['source_model']],fields=e['fields'],tags=tags,options=dict(allowDuplicate=True)))
            assert nid,ident(e)
            note=call('notesInfo',notes=[nid])[0]
            cards=call('cardsInfo',cards=note['cards'])
            assert len(cards)==e['expected_cards'],(ident(e),len(cards))
            other=[c['cardId'] for c in cards if c['deckName']!=PLAN['target_deck']]
            if other:
                assert all(c['reps']==0 for c in cards if c['cardId'] in other)
                call('changeDeck',cards=other,deck=PLAN['target_deck'])
                cards=call('cardsInfo',cards=note['cards'])
            flag=5 if e['pink'] else 3 if e['high_yield'] else 0
            if flag:
                for c in cards:call('setSpecificValueOfCard',card=c['cardId'],keys=['flags'],newValues=[flag],warning_check=True)
            row=dict(identity=ident(e),source_nid=e['source_nid'],note_id=nid,card_ids=[c['cardId'] for c in cards],flag=flag,origin=e['origin'])
            rows.append(row)
            with journal.open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
        save('receipt.json',dict(created=rows,totals=PLAN['totals'],deck=PLAN['target_deck'],profile=PLAN['profile']))
    finally:LOCK.unlink(missing_ok=True)
if __name__=='__main__':
    import sys
    if sys.argv[1]=='check':
        check();print('check ok')
    elif sys.argv[1]=='apply':
        install();print('applied',PLAN['totals'])
