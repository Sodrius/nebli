import argparse,hashlib,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
from inventory import call
from prepare import ROOT,DECK,DECK_ALEM,LESSON,digest

sys.stdout.reconfigure(encoding='utf-8')
TAG=f'NEBLI::{LESSON}'
MODELS={'AnKingOverhaul (AnKing Step Deck / AnKingMed)':'NEBLI AnKing independente - v3',
        'AnKingMCAT (AnKing-MCAT / AnKingMed)':'NEBLI AnKingMCAT independente - v1'}
AUTHORED_MODEL='AnKingOverhaul (AnKing Step Deck / AnKingMed)'
GLOBAL_LOCK=ROOT.parent/'ANKI-ESCRITA.lock'   # compartilhado com o Codex (fila do lote)

def save(name,value): (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
def plain(note): return {k:v['value'] for k,v in note['fields'].items()}
def snapshot(plan):
    ids=[e['source_nid'] for e in plan['entries'] if e['source_nid']]
    return {n['noteId']:n for n in call('notesInfo',notes=ids)}
def model_snapshot():
    return {m:{'fields':call('modelFieldNames',modelName=m),'templates':call('modelTemplates',modelName=m),'styling':call('modelStyling',modelName=m)} for m in MODELS}
def studied(card): return card.get('type',0)!=0 or card.get('queue',0) not in (0,-1)

def check(plan,resume=False):
    issues=[]
    if call('getMediaDirPath')!=plan['profile_evidence']: issues.append('Perfil ativo mudou')
    if plan['target_deck']!=DECK or plan['lesson_id']!=LESSON: issues.append('Plano de outra aula')
    if len({e['key'] for e in plan['entries']})!=len(plan['entries']): issues.append('Chaves duplicadas')
    names=call('modelNames')
    for s,t in MODELS.items():
        if t not in names or call('modelFieldNames',modelName=t)!=call('modelFieldNames',modelName=s): issues.append(f'Modelo NEBLI incompatível: {t}')
    sources=snapshot(plan)
    for e in plan['entries']:
        if e['source_nid']:
            n=sources.get(e['source_nid'])
            if not n or digest(n['fields'])!=e['source_fields_hash']: issues.append(f'Fonte mudou: {e["source_nid"]}')
            idtag=f'NEBLI::source::nid-{e["source_nid"]}'
        else: idtag=f'NEBLI::author::{e["key"]}'
        found=call('findNotes',query=f'tag:"{idtag}"')
        if found and not resume: issues.append(f'Cópia já existente: {e["key"]} → {found}')
        if found and resume:
            if len(found)!=1: issues.append(f'Cópias ambíguas: {e["key"]}')
            else:
                ex=call('notesInfo',notes=found)[0]
                if TAG not in ex['tags']: issues.append(f'Cópia de outra aula: {e["key"]}')
                if any(studied(c) for c in call('cardsInfo',cards=ex['cards'])): issues.append(f'Cópia já estudada: {e["key"]}')
        if e['expected_cards']!=len(set(re.findall(r'{{c(\d+)::',e['fields']['Text']))): issues.append(f'Clozes divergentes: {e["key"]}')
    for a in plan['associate_existing']:
        n=call('notesInfo',notes=[a['nid']])
        if not n or digest(n[0]['fields'])!=a['fields_hash']: issues.append(f'Nota a associar mudou/ausente: {a["nid"]}')
    existing=call('findCards',query=f'"deck:{DECK}"')
    if existing and not resume: issues.append(f'Deck já contém {len(existing)} cards')
    for m in call('getMediaFilesNames',pattern='*') if False else []: pass
    if issues: raise RuntimeError('\n'.join(issues))
    return {'profile':plan['profile_evidence'],'notes':len(plan['entries']),'cards':plan['totals']['cards'],'associate':len(plan['associate_existing'])}

def apply(plan):
    with GLOBAL_LOCK.open('x',encoding='utf-8') as f: f.write(json.dumps({'executor':'Claude','aula':LESSON,'at':datetime.now(timezone.utc).isoformat()}))
    journal=ROOT/'journal.jsonl'
    def log(action,value):
        with journal.open('a',encoding='utf-8') as f: f.write(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'action':action,'value':value},ensure_ascii=False)+'\n')
    try:
        check(plan,resume=True)
        originals=snapshot(plan); models=model_snapshot()
        save('before-apply.json',{'notes':list(originals.values()),'models':models,'associate_before':call('notesInfo',notes=[a['nid'] for a in plan['associate_existing']])})
        log('snapshot',{'source_notes':len(originals)})
        call('createDeck',deck=DECK)
        for src,name in plan.get('media',[]):
            call('storeMediaFile',filename=name,path=str((ROOT/src).resolve()))
        log('media',plan.get('media',[]))
        results=[]; green=[]; pink=[]
        for e in plan['entries']:
            target=MODELS[e['source_model'] or AUTHORED_MODEL]
            dest=DECK_ALEM if e['scope']=='alem' else DECK
            fields={name:'' for name in call('modelFieldNames',modelName=target)}
            fields.update(e['fields'])
            if 'ankihub_id' in fields: fields['ankihub_id']=''
            id_tag=f'NEBLI::source::nid-{e["source_nid"]}' if e['source_nid'] else f'NEBLI::author::{e["key"]}'
            tags=list(dict.fromkeys(e['source_tags']+[TAG,f'NEBLI::objetivo::{e["objective"]}',f'NEBLI::origem::{e["origin"]}',f'NEBLI::escopo::{e["scope"]}',id_tag]))
            existing=call('findNotes',query=f'tag:"{id_tag}"')
            log('before-add',{'key':e['key'],'existing':existing})
            nid=existing[0] if existing else call('addNote',note={'deckName':dest,'modelName':target,'fields':fields,'tags':tags,'options':{'allowDuplicate':True}})
            if not nid: raise RuntimeError(f'Add falhou: {e["key"]}')
            note=call('notesInfo',notes=[nid])[0]
            if plain(note)!=fields: raise RuntimeError(f'Campos divergentes: {e["key"]}')
            cards=call('cardsInfo',cards=note['cards'])
            if len(cards)!=e['expected_cards']: raise RuntimeError(f'Contagem divergente: {e["key"]}: {len(cards)}')
            wrong=[c for c in cards if c['deckName']!=dest]
            if wrong:
                if any(studied(c) for c in wrong): raise RuntimeError(f'Card estudado fora do deck: {e["key"]}')
                call('changeDeck',cards=[c['cardId'] for c in wrong],deck=dest)
            ids=[c['cardId'] for c in cards]
            if e['pink']: pink.extend(ids)
            elif e['high_yield']: green.extend(ids)
            r={'key':e['key'],'source_nid':e['source_nid'],'new_nid':nid,'cards':ids,'origin':e['origin'],'objective':e['objective'],'high_yield':e['high_yield'],'pink':e['pink'],'scope':e['scope']}
            results.append(r); log('created',r)
        for cid in green: call('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[3],warning_check=True)
        for cid in pink: call('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[5],warning_check=True)
        for a in plan['associate_existing']:
            call('addTags',notes=[a['nid']],tags=f"{TAG} NEBLI::objetivo::{a['objective']}")
            after=call('notesInfo',notes=[a['nid']])[0]
            if TAG not in after['tags'] or digest(after['fields'])!=a['fields_hash']: raise RuntimeError(f"Associação falhou: {a['nid']}")
            log('associated',{'nid':a['nid']})
        all_cards=call('findCards',query=f'"deck:{DECK}"')
        if len(all_cards)!=plan['totals']['cards']: raise RuntimeError(f'Total final: {len(all_cards)}')
        if call('findCards',query=f'"deck:{DECK}" is:suspended'): raise RuntimeError('Card suspenso inesperado')
        if set(call('findCards',query=f'"deck:{DECK}" flag:3'))!=set(green): raise RuntimeError('Verdes divergentes')
        if set(call('findCards',query=f'"deck:{DECK}" flag:5'))!=set(pink): raise RuntimeError('Rosas divergentes')
        for nid,old in originals.items():
            now=call('notesInfo',notes=[nid])[0]
            if old['fields']!=now['fields'] or old['tags']!=now['tags']: raise RuntimeError(f'Fonte alterada: {nid}')
        if model_snapshot()!=models: raise RuntimeError('Modelo fonte alterado')
        package=ROOT/'Patogenicidade bacteriana.apkg'
        if not call('exportPackage',deck=DECK,path=str(package.resolve()),includeSched=True): raise RuntimeError('Exportação falhou')
        receipt={'at':datetime.now(timezone.utc).isoformat(),'lesson_id':LESSON,'deck':DECK,'plan_sha256':digest(plan),'notes':len(results),'cards':len(all_cards),
                 'counts':plan['totals'],'green':len(green),'pink':len(pink),'red':len(call('findCards',query=f'"deck:{DECK}" flag:1')),'suspended':0,
                 'sources_unchanged':True,'package':str(package.resolve()),'package_sha256':hashlib.sha256(package.read_bytes()).hexdigest(),
                 'results':results,'associated':[a['nid'] for a in plan['associate_existing']]}
        save('receipt.json',receipt); log('complete',{k:v for k,v in receipt.items() if k!='results'})
        print(json.dumps({k:v for k,v in receipt.items() if k!='results'},ensure_ascii=False,indent=2))
    finally: GLOBAL_LOCK.unlink(missing_ok=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['check','apply']);a=p.parse_args()
    plan=json.loads((ROOT/'plan.json').read_text(encoding='utf-8'))
    if GLOBAL_LOCK.exists() and a.mode=='apply': sys.exit(f'Outro executor está escrevendo no Anki: {GLOBAL_LOCK.read_text(encoding="utf-8")}')
    print(json.dumps(check(plan),ensure_ascii=False,indent=2)) if a.mode=='check' else apply(plan)
