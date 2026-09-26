"""Ajuste pós-feedback (Davi, 24/09/2026):
- rosa = está na aula, mas não vale guardar a longo prazo (não "além da aula");
- o que a aula não traz sai do deck, exceto o que provavelmente foi abordado em aula sem estar no slide.
"""
import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
from inventory import call
from prepare import ROOT,DECK,DECK_ALEM,LESSON,HY
sys.stdout.reconfigure(encoding='utf-8')
GLOBAL_LOCK=ROOT.parent/'ANKI-ESCRITA.lock'
KEEP={1503603239057,1500403421264,1489341109037,'authored-sulfa-seletividade'}   # provavelmente abordados em aula
ROSA_AULA={1503682928728,1505264663531,1506032108460,'authored-quimioterapico'}  # da aula, sem valor a longo prazo
def key(r): return r['source_nid'] or r['key']
def log(action,value):
    with (ROOT/'journal.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'action':action,'value':value},ensure_ascii=False)+'\n')
rec=json.loads((ROOT/'receipt.json').read_text(encoding='utf-8'))
alem=[r for r in rec['results'] if r['scope']=='alem']
remove=[r for r in alem if key(r) not in KEEP]; keep=[r for r in alem if key(r) in KEEP]
with GLOBAL_LOCK.open('x',encoding='utf-8') as f: f.write(json.dumps({'executor':'Claude','aula':LESSON,'at':datetime.now(timezone.utc).isoformat()}))
try:
    ids=[r['new_nid'] for r in remove]
    backup={'notes':call('notesInfo',notes=ids),'cards':call('cardsInfo',cards=[c for r in remove for c in r['cards']])}
    if not (ROOT/'before-ajuste-escopo.json').exists(): (ROOT/'before-ajuste-escopo.json').write_text(json.dumps(backup,ensure_ascii=False,indent=1),encoding='utf-8')
    if any(c.get('type',0)!=0 for c in backup['cards']): raise SystemExit('Há card já estudado entre os removidos; parar.')
    live=[n['noteId'] for n in backup['notes'] if n]
    if live: call('deleteNotes',notes=live)
    log('deleted_out_of_scope',{'notes':ids})
    for r in keep:
        call('changeDeck',cards=r['cards'],deck=DECK)
        call('removeTags',notes=[r['new_nid']],tags='NEBLI::escopo::alem'); call('addTags',notes=[r['new_nid']],tags='NEBLI::escopo::aula')
        r['scope']='aula'
    log('kept_moved',[r['new_nid'] for r in keep])
    if call('findCards',query=f'"deck:{DECK_ALEM}"'): raise SystemExit('Subdeck não ficou vazio')
    call('deleteDecks',decks=[DECK_ALEM],cardsToo=True)
    results=[r for r in rec['results'] if r not in remove]
    green=[];pink=[];plain=[]
    for r in results:
        if key(r) in ROSA_AULA: pink+=r['cards']; r['pink']=True
        elif r['high_yield']: green+=r['cards']; r['pink']=False
        else: plain+=r['cards']; r['pink']=False
    for cid in green: call('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[3],warning_check=True)
    for cid in pink: call('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[5],warning_check=True)
    for cid in plain: call('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[0],warning_check=True)
    all_cards=call('findCards',query=f'"deck:{DECK}"')
    expect=sum(len(r['cards']) for r in results)
    if len(all_cards)!=expect: raise SystemExit(f'Total {len(all_cards)} != {expect}')
    if set(call('findCards',query=f'"deck:{DECK}" flag:5'))!=set(pink) or set(call('findCards',query=f'"deck:{DECK}" flag:3'))!=set(green): raise SystemExit('Flags divergentes')
    package=ROOT/'Antibióticos e resistência.apkg'; package.unlink(missing_ok=True)
    if not call('exportPackage',deck=DECK,path=str(package.resolve()),includeSched=True): raise SystemExit('Exportação falhou')
    rec.update({'at':datetime.now(timezone.utc).isoformat(),'results':results,'notes':len(results),'cards':len(all_cards),'green':len(green),'pink':len(pink),
                'removed_out_of_scope':len(remove),'package_sha256':hashlib.sha256(package.read_bytes()).hexdigest(),
                'counts':{'AnKing':sum(len(r['cards']) for r in results if r['origin']=='AnKing'),'AnKing-MCAT':sum(len(r['cards']) for r in results if r['origin']=='AnKing-MCAT'),
                          'Autoral':sum(len(r['cards']) for r in results if r['origin']=='Autoral')}})
    (ROOT/'receipt.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8'); log('ajuste_escopo_ok',{k:rec[k] for k in ('notes','cards','green','pink','removed_out_of_scope','counts')})
    print(json.dumps({k:rec[k] for k in ('notes','cards','green','pink','removed_out_of_scope','counts')},ensure_ascii=False,indent=1))
finally: GLOBAL_LOCK.unlink(missing_ok=True)
