"""Install X3 independent copies with a cross-executor Anki lock and readback."""
import copy,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen

HERE=Path(__file__).parent; LOCK=HERE.parent/'ANKI-ESCRITA.lock'
PLAN=json.loads((HERE/'plan.json').read_text(encoding='utf-8'))
TAG='NEBLI::'+PLAN['lesson_id']
MODELS={
 'AnKingOverhaul (AnKing Step Deck / AnKingMed)':'NEBLI UC08 Visceral AnKing v1',
 'AnatoKingOverhaul V2':'NEBLI UC08 AnatoKing V2 v1',
 'Cloze deletion':'NEBLI UC08 Visceral Dope Cloze v1',
 'Cloze-b12d6':'NEBLI UC08 Visceral Dorian Cloze v1',
 'Anatomy':'NEBLI UC08 Visceral Anatomy v1',
}
def call(action,**params):
    payload=json.dumps({'action':action,'version':6,'params':params}).encode()
    with urlopen(Request('http://127.0.0.1:8765',data=payload,headers={'Content-Type':'application/json'}),timeout=180) as response:r=json.load(response)
    if r['error']:raise RuntimeError(f"{action}: {r['error']}")
    return r['result']
def save(name,obj):(HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def ident(e):return 'NEBLI::source::nid-'+str(e['source_nid']) if e['source_nid'] else 'NEBLI::authored::uc08-x3-'+e['key']
def journal_rows():
    path=HERE/'journal.jsonl'
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()] if path.exists() else []

def check():
    assert call('getActiveProfile')==PLAN['profile']
    ids=[e['source_nid'] for e in PLAN['entries'] if e['source_nid']]
    sources={n['noteId']:n for at in range(0,len(ids),100) for n in call('notesInfo',notes=ids[at:at+100])}
    media=Path(call('getMediaDirPath'))
    completed={r['identity']:r for r in journal_rows()}
    for e in PLAN['entries']:
        nid=e['source_nid']
        if nid and (nid not in sources or digest({k:v['value'] for k,v in sources[nid]['fields'].items()})!=e['source_fields_hash']):raise RuntimeError(f'Source missing/changed: {nid}')
        found=call('findNotes',query=f'tag:"{ident(e)}"')
        if found and (ident(e) not in completed or found!=[completed[ident(e)]['note_id']]):raise RuntimeError(f'Unexpected existing copy: {ident(e)} {found}')
        for val in e['fields'].values():
            for fname in re.findall(r'<img[^>]+src="([^"]+)"',val):
                if not (media/fname).is_file():raise RuntimeError(f'Missing media {fname}')
    existing=call('findCards',query=f'deck:"{PLAN["target_deck"]}"')
    journal_cards={cid for row in completed.values() for cid in row['card_ids']}
    if set(existing)!=journal_cards:raise RuntimeError('Target contains cards outside journal')
    shared=call('notesInfo',notes=[PLAN['shared_note_id']])[0]
    if 'NEBLI::source::nid-1461962333435' not in shared['tags']:raise RuntimeError('Shared note identity changed')
    return sources,shared

def ensure_model(source):
    target=MODELS[source]
    if target in call('modelNames'):return target
    fields=call('modelFieldNames',modelName=source)
    templates=copy.deepcopy(call('modelTemplates',modelName=source))
    css=call('modelStyling',modelName=source)['css']
    call('createModel',modelName=target,inOrderFields=fields,css=css,isCloze=source!='Anatomy',cardTemplates=[{'Name':k,**v} for k,v in templates.items()])
    if call('modelFieldNames',modelName=target)!=fields:raise RuntimeError(f'Model mismatch {target}')
    return target

def main():
    with LOCK.open('x',encoding='utf-8') as f:f.write(json.dumps({'executor':'Codex','lesson':PLAN['lesson_id'],'at':datetime.now(timezone.utc).isoformat()},ensure_ascii=False))
    created=journal_rows(); journal=HERE/'journal.jsonl'; completed={r['identity'] for r in created}
    try:
        sources,shared=check()
        if not (HERE/'before-apply.json').exists():save('before-apply.json',{'profile':PLAN['profile'],'source_notes':list(sources.values()),'shared_note':shared,'target_cards':[]})
        for deck in ['NEBLI','NEBLI::UC08','NEBLI::UC08::P1','NEBLI::UC08::P1::Anatomia',PLAN['target_deck']]:call('createDeck',deck=deck)
        models={m:ensure_model(m) for m in set(e['source_model'] for e in PLAN['entries'])}
        for e in PLAN['entries']:
            if ident(e) in completed:continue
            tags=list(dict.fromkeys(e['source_tags']+[TAG,ident(e),'NEBLI::origem::'+e['origin'].replace(' ','-')]))
            nid=call('addNote',note={'deckName':PLAN['target_deck'],'modelName':models[e['source_model']],'fields':e['fields'],'tags':tags,'options':{'allowDuplicate':True}})
            if not nid:raise RuntimeError(f'addNote returned no ID for {ident(e)}')
            n=call('notesInfo',notes=[nid])[0];cards=call('cardsInfo',cards=n['cards'])
            if len(cards)!=e['expected_cards']:raise RuntimeError(f"Count mismatch {ident(e)}: {len(cards)} != {e['expected_cards']}")
            wrong=[c['cardId'] for c in cards if c['deckName']!=PLAN['target_deck']]
            if wrong:
                if any(c['reps'] for c in cards if c['cardId'] in wrong):raise RuntimeError('Reviewed card landed in wrong deck')
                call('changeDeck',cards=wrong,deck=PLAN['target_deck']);cards=call('cardsInfo',cards=n['cards'])
            flag=5 if e['pink'] else 3 if e['high_yield'] else 0
            if flag:
                for c in cards:call('setSpecificValueOfCard',card=c['cardId'],keys=['flags'],newValues=[flag],warning_check=True)
            row={'identity':ident(e),'source_nid':e['source_nid'],'note_id':nid,'card_ids':[c['cardId'] for c in cards],'origin':e['origin'],'flag':flag}
            created.append(row)
            with journal.open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
        call('addTags',notes=[PLAN['shared_note_id']],tags=TAG)
        if len(created)!=PLAN['totals']['notes']:raise RuntimeError('Created note count mismatch')
        actual=call('findCards',query=f'deck:"{PLAN["target_deck"]}"')
        if len(actual)!=PLAN['totals']['cards']:raise RuntimeError(f'Actual card count {len(actual)}')
        save('receipt.json',{'created':created,'shared_note_id':PLAN['shared_note_id'],'deck':PLAN['target_deck'],'totals':PLAN['totals'],'profile':PLAN['profile']})
        save('sync-initial.json',{'result':call('sync'),'at':datetime.now(timezone.utc).isoformat()})
        print(json.dumps({'created_notes':len(created),'created_cards':len(actual),'shared':PLAN['shared_note_id'],'synced':True},ensure_ascii=False))
    finally:
        LOCK.unlink(missing_ok=True)
if __name__=='__main__':main()
