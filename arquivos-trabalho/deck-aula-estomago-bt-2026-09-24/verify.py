import json,re
from collections import Counter
from pathlib import Path
from apply import call,digest,HERE,PLAN

def main():
    receipt=json.loads((HERE/'receipt.json').read_text(encoding='utf-8'))
    before=json.loads((HERE/'before-apply.json').read_text(encoding='utf-8'))
    ids=[cid for row in receipt['created'] for cid in row['card_ids']]
    live=call('cardsInfo',cards=ids)
    deck_ids=call('findCards',query=f'deck:"{PLAN["target_deck"]}"')
    notes=call('notesInfo',notes=[r['note_id'] for r in receipt['created']])
    srcids=[n['noteId'] for n in before['sources']]
    src={n['noteId']:n for n in call('notesInfo',notes=srcids)}
    plan_ids=[e['source_nid'] for e in PLAN['entries'] if e['source_nid']]
    plan_src={n['noteId']:n for n in call('notesInfo',notes=plan_ids)}
    flags=Counter(c['flags'] for c in live)
    media=Path(call('getMediaDirPath'))
    missing_media=[]
    for n in notes:
        for v in n['fields'].values():
            for filename in re.findall(r'<img[^>]*src="([^"]+)"',v['value']):
                if not (media/filename).exists():missing_media.append([n['noteId'],filename])
    out=dict(profile=call('getActiveProfile'),deck=PLAN['target_deck'],notes=len(notes),cards=len(live),deck_cards=len(deck_ids),ids_match=set(ids)==set(deck_ids),flags=dict(flags),suspended=[c['cardId'] for c in live if c['queue']==-1],changed_source_fields=[n['noteId'] for n in before['sources'] if digest(n['fields'])!=digest(src[n['noteId']]['fields'])],plan_source_changed=[e['source_nid'] for e in PLAN['entries'] if e['source_nid'] and digest({k:v['value'] for k,v in plan_src[e['source_nid']]['fields'].items()})!=e['source_fields_hash']],missing_question=[c['cardId'] for c in live if not re.sub('<[^>]+>','',c.get('question','')).strip()],missing_answer=[c['cardId'] for c in live if not re.sub('<[^>]+>','',c.get('answer','')).strip()],missing_media=missing_media)
    (HERE/'verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(out,ensure_ascii=False))
    assert out['profile']==PLAN['profile'] and out['notes']==PLAN['totals']['notes'] and out['cards']==PLAN['totals']['cards'] and out['ids_match']
    assert flags[5]==PLAN['totals']['pink'] and flags[3]==PLAN['totals']['green']
    assert not (out['suspended'] or out['changed_source_fields'] or out['plan_source_changed'] or out['missing_question'] or out['missing_answer'] or out['missing_media'])
if __name__=='__main__':main()
