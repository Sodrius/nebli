import json,sys,collections
from datetime import datetime,timezone
from ak import call
sys.stdout.reconfigure(encoding='utf-8')
plan=json.load(open('plan.json',encoding='utf-8'));rc=json.load(open('receipt.json',encoding='utf-8'))
red=json.load(open('reduction.json',encoding='utf-8'))
BASE=plan['base_deck']
D_CORE=BASE+'::1 - Essencial UC21'
D_DET=BASE+'::2 - Complemento (suspenso)::Roteiro - detalhes'
D_ALEM=BASE+'::2 - Complemento (suspenso)::DM além do roteiro'
res={r['key']:r for r in rc['results']}
core=set(red['core_keys'])
all_cards=[c for r in rc['results'] for c in r['cards']]
before=call('cardsInfo',cards=all_cards)
if any(c.get('type',0)!=0 or c.get('reps',0) for c in before): raise SystemExit('Há cards já estudados; parar.')
json.dump([{'cardId':c['cardId'],'deck':c['deckName'],'queue':c['queue'],'flags':c['flags']} for c in before],open('before-reduction.json','w',encoding='utf-8'))
for d in (D_CORE,D_DET,D_ALEM): call('createDeck',deck=d)
moves=collections.defaultdict(list); tagc=[];tagr=[]; susp=[]
for r in rc['results']:
    e_scope=r['scope']
    if r['key'] in core: moves[D_CORE]+=r['cards']; tagc.append(r['new_nid'])
    else:
        moves[D_DET if e_scope=='roteiro' else D_ALEM]+=r['cards']; tagr.append(r['new_nid']); susp+=r['cards']
for d,cs in moves.items(): call('changeDeck',cards=cs,deck=d)
call('addTags',notes=tagc,tags='NEBLI::reducao::essencial-uc21')
call('addTags',notes=tagr,tags='NEBLI::reducao::complemento-suspenso-2026-09-23')
call('suspend',cards=susp)
# remove old now-empty subdecks
old=[BASE+'::1 - Roteiro do caso',BASE+'::2 - DM além do roteiro']
empty=[d for d in old if not call('findCards',query=f'"deck:{d}"')]
if empty: call('deleteDecks',decks=empty,cardsToo=False)
after=call('cardsInfo',cards=all_cards)
flags_same=all(a['flags']==b['flags'] for a,b in zip(sorted(before,key=lambda x:x['cardId']),sorted(after,key=lambda x:x['cardId'])))
out={'at':datetime.now(timezone.utc).isoformat(),'core_cards':len(moves[D_CORE]),'detalhes_cards':len(moves[D_DET]),'alem_cards':len(moves[D_ALEM]),
 'suspended':len(call('findCards',query=f'"deck:{BASE}" is:suspended')),'active':len(call('findCards',query=f'"deck:{BASE}" -is:suspended')),
 'active_by_flag':{k:len(call('findCards',query=f'"deck:{D_CORE}" flag:{k}')) for k in (0,3,5)},
 'flags_unchanged':flags_same,'deleted_empty_decks':empty,'decks':[D_CORE,D_DET,D_ALEM]}
json.dump(out,open('reduction-receipt.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(json.dumps(out,ensure_ascii=False,indent=1))
