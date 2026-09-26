import argparse,copy,hashlib,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
from inventory import call
from prepare import ROOT,DECK,LESSON,digest

sys.stdout.reconfigure(encoding='utf-8')
TAG=f'NEBLI::{LESSON}'
ANKING='AnKingOverhaul (AnKing Step Deck / AnKingMed)'
MODELS={ANKING:'NEBLI AnKing independente - v3'}

def save(name,value): (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
def plain(note): return {k:v['value'] for k,v in note['fields'].items()}
def snapshot(plan):
    ids=[e['source_nid'] for e in plan['entries'] if e['source_nid']]
    return {n['noteId']:n for n in call('notesInfo',notes=ids)}
def model_snapshot():
    return {m:{'fields':call('modelFieldNames',modelName=m),'templates':call('modelTemplates',modelName=m),'styling':call('modelStyling',modelName=m)} for m in MODELS}

def check(plan, resume=False):
    issues=[]
    if call('getMediaDirPath')!=plan['profile_evidence']: issues.append('Perfil ativo mudou')
    if plan['target_deck']!=DECK or plan['lesson_id']!=LESSON: issues.append('Plano de outra aula')
    if len(set(e['key'] for e in plan['entries']))!=len(plan['entries']): issues.append('Chaves duplicadas')
    sources=snapshot(plan)
    for e in plan['entries']:
        if e['source_nid']:
            n=sources.get(e['source_nid'])
            if not n or digest(n['fields'])!=e['source_fields_hash']: issues.append(f'Fonte mudou: {e["source_nid"]}')
            found=call('findNotes',query=f'tag:"NEBLI::source::nid-{e["source_nid"]}"')
            if found and not resume: issues.append(f'Cópia já existente: {e["source_nid"]} → {found}')
            if found and resume:
                if len(found)!=1: issues.append(f'Cópias ambíguas: {e["source_nid"]} → {found}')
                else:
                    existing_note=call('notesInfo',notes=found)[0]
                    if TAG not in existing_note['tags']: issues.append(f'Cópia de outra aula: {e["source_nid"]}')
                    existing_cards=call('cardsInfo',cards=existing_note['cards'])
                    if any(c['reps']!=0 for c in existing_cards): issues.append(f'Cópia já estudada: {e["source_nid"]}')
        else:
            found=call('findNotes',query=f'tag:"NEBLI::author::{e["key"]}"')
            if found and not resume: issues.append(f'Autoral já existente: {e["key"]}')
            if found and resume and (len(found)!=1 or TAG not in call('notesInfo',notes=found)[0]['tags']): issues.append(f'Autoral ambíguo: {e["key"]}')
        if e['expected_cards']!=len(set(int(x) for x in re.findall(r'{{c(\d+)::',e['fields']['Text']))): issues.append(f'Clozes divergentes: {e["key"]}')
    existing=call('findCards',query=f'deck:"{DECK}"')
    if existing and not resume: issues.append(f'Deck já contém {len(existing)} cards')
    if len(existing)>plan['totals']['cards']: issues.append(f'Deck contém cards excedentes: {len(existing)}')
    if issues: raise RuntimeError('\n'.join(issues))
    return {'profile':plan['profile_evidence'],'notes':len(plan['entries']),'cards':plan['totals']['cards'],'models':list(MODELS.values())}

def ensure_models():
    names=call('modelNames')
    for source,target in MODELS.items():
        fields=call('modelFieldNames',modelName=source)
        templates=copy.deepcopy(call('modelTemplates',modelName=source))
        css=call('modelStyling',modelName=source)['css']
        if target not in names:
            call('createModel',modelName=target,inOrderFields=fields,css=css,isCloze=True,cardTemplates=[{'Name':n,**t} for n,t in templates.items()])
        if call('modelFieldNames',modelName=target)!=fields: raise RuntimeError(f'Campos incompatíveis: {target}')

def apply(plan):
    lock=ROOT/'apply.lock'
    with lock.open('x',encoding='utf-8') as f: f.write(datetime.now(timezone.utc).isoformat())
    journal=ROOT/'journal.jsonl'
    def log(action,value):
        with journal.open('a',encoding='utf-8') as f: f.write(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'action':action,'value':value},ensure_ascii=False)+'\n')
    try:
        check(plan,resume=True)
        originals=snapshot(plan); models=model_snapshot()
        save('before-apply.json',{'notes':list(originals.values()),'models':models,'deck_cards':[]})
        log('snapshot',{'source_notes':len(originals)})
        ensure_models()
        call('createDeck',deck=DECK)
        results=[]; green=[]
        for e in plan['entries']:
            source=e['source_model'] or ANKING
            target=MODELS[source]
            fields={name:'' for name in call('modelFieldNames',modelName=target)}
            fields.update(e['fields'])
            if 'ankihub_id' in fields: fields['ankihub_id']=''
            tags=list(dict.fromkeys(e['source_tags']+[TAG,f'NEBLI::objetivo::{e["objective"]}',f'NEBLI::origem::{e["origin"].replace(" ","-")}']+([f'NEBLI::source::nid-{e["source_nid"]}'] if e['source_nid'] else [f'NEBLI::author::{e["key"]}'])))
            id_tag=f'NEBLI::source::nid-{e["source_nid"]}' if e['source_nid'] else f'NEBLI::author::{e["key"]}'
            existing=call('findNotes',query=f'tag:"{id_tag}"')
            log('before-add',{'key':e['key'],'existing':existing})
            nid=existing[0] if existing else call('addNote',note={'deckName':DECK,'modelName':target,'fields':fields,'tags':tags,'options':{'allowDuplicate':True}})
            if not nid: raise RuntimeError(f'Add falhou: {e["key"]}')
            note=call('notesInfo',notes=[nid])[0]
            if plain(note)!=fields: raise RuntimeError(f'Campos divergentes: {e["key"]}')
            cards=call('cardsInfo',cards=note['cards'])
            if len(cards)!=e['expected_cards']: raise RuntimeError(f'Contagem divergente: {e["key"]}: {len(cards)}')
            misplaced=[c for c in cards if c['deckName']!=DECK]
            if misplaced:
                if any(c['reps']!=0 for c in misplaced): raise RuntimeError(f'Card estudado fora do deck: {e["key"]}')
                call('changeDeck',cards=[c['cardId'] for c in misplaced],deck=DECK)
                cards=call('cardsInfo',cards=note['cards'])
            if any(c['deckName']!=DECK for c in cards): raise RuntimeError(f'Card fora do deck: {e["key"]}')
            ids=[c['cardId'] for c in cards]
            if e['high_yield']: green.extend(ids)
            result={'key':e['key'],'source_nid':e['source_nid'],'new_nid':nid,'cards':ids,'origin':e['origin'],'objective':e['objective'],'high_yield':e['high_yield']}
            results.append(result); log('created',result)
        for cid in green: call('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[3],warning_check=True)
        for a in plan['associate_existing']:
            now=call('notesInfo',notes=[a['nid']])[0]
            if digest(now['fields'])!=a['fields_hash']: raise RuntimeError(f"Nota associada mudou: {a['nid']}")
            call('addTags',notes=[a['nid']],tags=f"{TAG} NEBLI::objetivo::{a['objective']}")
            after=call('notesInfo',notes=[a['nid']])[0]
            if TAG not in after['tags'] or digest(after['fields'])!=a['fields_hash']: raise RuntimeError(f"Associação falhou: {a['nid']}")
            log('associated',{'nid':a['nid'],'tags_after':after['tags']})
        all_cards=call('findCards',query=f'deck:"{DECK}"')
        if len(all_cards)!=plan['totals']['cards']: raise RuntimeError(f'Total final: {len(all_cards)}')
        if call('findCards',query=f'deck:"{DECK}" is:suspended'): raise RuntimeError('Card suspenso inesperado')
        if set(call('findCards',query=f'deck:"{DECK}" flag:3'))!=set(green): raise RuntimeError('Flags verdes divergentes')
        for nid,old in originals.items():
            now=call('notesInfo',notes=[nid])[0]
            if old['fields']!=now['fields'] or old['tags']!=now['tags']: raise RuntimeError(f'Fonte alterada: {nid}')
        if model_snapshot()!=models: raise RuntimeError('Modelo fonte alterado')
        package=ROOT/'Sistema complemento.apkg'
        if not call('exportPackage',deck=DECK,path=str(package.resolve()),includeSched=True): raise RuntimeError('Exportação falhou')
        receipt={'at':datetime.now(timezone.utc).isoformat(),'lesson_id':LESSON,'deck':DECK,'plan_sha256':digest(plan),'notes':len(results),'cards':len(all_cards),'counts':plan['totals'],'green':len(green),'red':len(call('findCards',query=f'deck:"{DECK}" flag:1')),'suspended':0,'sources_unchanged':True,'package':str(package.resolve()),'package_sha256':hashlib.sha256(package.read_bytes()).hexdigest(),'results':results,'associated':[a['nid'] for a in plan['associate_existing']]}
        save('receipt.json',receipt); log('complete',{k:v for k,v in receipt.items() if k!='results'})
        print(json.dumps({k:v for k,v in receipt.items() if k!='results'},ensure_ascii=False,indent=2))
    finally: lock.unlink(missing_ok=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['check','apply']);args=p.parse_args()
    plan=json.loads((ROOT/'plan.json').read_text(encoding='utf-8'))
    if args.mode=='check': print(json.dumps(check(plan),ensure_ascii=False,indent=2))
    else: apply(plan)
