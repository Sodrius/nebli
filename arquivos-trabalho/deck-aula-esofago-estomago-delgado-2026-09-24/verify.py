"""Read-only audit of installed X3, sources and selected media."""
import json,re,hashlib
from pathlib import Path
from apply import PLAN,HERE,call,ident,digest,save,TAG

def main():
    receipt=json.loads((HERE/'receipt.json').read_text(encoding='utf-8'))
    rows=receipt['created'];cids=[cid for row in rows for cid in row['card_ids']]
    cards=[]
    for at in range(0,len(cids),100):cards+=call('cardsInfo',cards=cids[at:at+100])
    nids=[row['note_id'] for row in rows]
    notes=[]
    for at in range(0,len(nids),100):notes+=call('notesInfo',notes=nids[at:at+100])
    sources=[e['source_nid'] for e in PLAN['entries'] if e['source_nid']]
    original=[]
    for at in range(0,len(sources),100):original+=call('notesInfo',notes=sources[at:at+100])
    failures=[];media=Path(call('getMediaDirPath'))
    bycard={c['cardId']:c for c in cards};bynote={n['noteId']:n for n in notes}
    if len(notes)!=PLAN['totals']['notes'] or len(cards)!=PLAN['totals']['cards']:failures.append('Count mismatch')
    for e,row in zip(PLAN['entries'],rows):
        n=bynote[row['note_id']]
        if ident(e) not in n['tags'] or TAG not in n['tags']:failures.append(f'Tag mismatch {row["note_id"]}')
        for k,v in e['fields'].items():
            if n['fields'][k]['value']!=v:failures.append(f'Field mismatch {row["note_id"]} {k}')
            for name in re.findall(r'<img[^>]+src="([^"]+)"',v):
                if not (media/name).is_file():failures.append(f'Missing media {name}')
        for cid in row['card_ids']:
            c=bycard[cid]
            if c['deckName']!=PLAN['target_deck']:failures.append(f'Wrong deck {cid}')
            if c['queue']<0:failures.append(f'Suspended {cid}')
            if c['flags']!=row['flag']:failures.append(f'Flag mismatch {cid}')
            if not re.search(r'cloze|question',c['question'],re.I) or not c['answer']:failures.append(f'Empty render {cid}')
    origby={n['noteId']:n for n in original}
    for e in PLAN['entries']:
        nid=e['source_nid']
        if nid and digest({k:v['value'] for k,v in origby[nid]['fields'].items()})!=e['source_fields_hash']:failures.append(f'Original changed {nid}')
    shared=call('notesInfo',notes=[PLAN['shared_note_id']])[0]
    if TAG not in shared['tags']:failures.append('Shared note not tagged')
    inv=json.loads((HERE/'inventory.json').read_text(encoding='utf-8'))
    oldcards={c['cardId']:c for n in inv['notes'] for c in n['cards'] if n['nid'] in sources}
    for at in range(0,len(oldcards),100):
        for c in call('cardsInfo',cards=list(oldcards)[at:at+100]):
            old=oldcards[c['cardId']]
            if c['flags']!=old['flags'] or c['queue']!=old['queue'] or c['deckName']!=old['deckName']:failures.append(f'Source state changed {c["cardId"]}')
    result={'profile':call('getActiveProfile'),'notes':len(notes),'cards':len(cards),'pink':sum(c['flags']==5 for c in cards),'green':sum(c['flags']==3 for c in cards),'suspended':sum(c['queue']<0 for c in cards),'shared_note':PLAN['shared_note_id'],'originals_checked':len(original),'failures':failures}
    save('verification.json',result)
    print(json.dumps(result,ensure_ascii=False))
    if failures:raise SystemExit(1)
if __name__=='__main__':main()
