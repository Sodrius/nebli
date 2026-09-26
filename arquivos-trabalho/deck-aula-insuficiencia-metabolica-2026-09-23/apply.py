import argparse,base64,copy,hashlib,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
from ak import call
from prepare import ROOT,LESSON,digest

sys.stdout.reconfigure(encoding='utf-8')
TAG=f'NEBLI::{LESSON}'
ANKING='AnKingOverhaul (AnKing Step Deck / AnKingMed)'
MCAT='AnKingMCAT (AnKing-MCAT / AnKingMed)'
MODELS={ANKING:'NEBLI AnKing independente - v3',
        'AnKingOverhaul (NEBLI glicogenio)':'NEBLI AnKing independente - v3',
        MCAT:'NEBLI AnKingMCAT independente - v1'}
TEMPLATE_SOURCE={'NEBLI AnKing independente - v3':ANKING,'NEBLI AnKingMCAT independente - v1':MCAT}

def save(name,value): (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=1),encoding='utf-8')
def plain(note): return {k:v['value'] for k,v in note['fields'].items()}
def id_tag(e): return f'NEBLI::source::nid-{e["source_nid"]}' if e['source_nid'] else f'NEBLI::author::{e["key"]}'
def snapshot(plan):
    ids=[e['source_nid'] for e in plan['entries'] if e['source_nid']]
    out={}
    for s in range(0,len(ids),200):
        for n in call('notesInfo',notes=ids[s:s+200]): out[n['noteId']]=n
    return out
def model_snapshot():
    return {m:{'fields':call('modelFieldNames',modelName=m),'templates':call('modelTemplates',modelName=m),'styling':call('modelStyling',modelName=m)} for m in set(MODELS)}

def check(plan,resume=False):
    issues=[]
    if call('getMediaDirPath')!=plan['profile_evidence']: issues.append('Perfil ativo mudou')
    if plan['lesson_id']!=LESSON: issues.append('Plano de outra aula')
    if len({e['key'] for e in plan['entries']})!=len(plan['entries']): issues.append('Chaves duplicadas')
    sources=snapshot(plan)
    for e in plan['entries']:
        if e['source_nid']:
            n=sources.get(e['source_nid'])
            if not n or digest(n['fields'])!=e['source_fields_hash']: issues.append(f'Fonte mudou: {e["source_nid"]}')
        found=call('findNotes',query=f'tag:"{id_tag(e)}"')
        if found and not resume: issues.append(f'Cópia já existente: {e["key"]} → {found}')
        if found and resume and len(found)!=1: issues.append(f'Cópias ambíguas: {e["key"]}')
        if e['expected_cards']!=len(set(re.findall(r'{{c(\d+)::',e['fields']['Text']))): issues.append(f'Clozes divergentes: {e["key"]}')
    existing=call('findCards',query=f'"deck:{plan["base_deck"]}"')
    if existing and not resume: issues.append(f'Deck já contém {len(existing)} cards')
    if issues: raise RuntimeError('\n'.join(issues[:40]))
    return {'profile':plan['profile_evidence'],'notes':len(plan['entries']),'cards':plan['totals']['cards']}

def ensure_models():
    names=call('modelNames')
    for target,source in TEMPLATE_SOURCE.items():
        fields=call('modelFieldNames',modelName=source)
        if target not in names:
            templates=copy.deepcopy(call('modelTemplates',modelName=source))
            css=call('modelStyling',modelName=source)['css']
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
        save('before-apply.json',{'source_notes':len(originals),'source_hashes':{k:digest(v['fields']) for k,v in originals.items()},'models':models,'deck_cards':call('findCards',query=f'"deck:{plan["base_deck"]}"')})
        log('snapshot',{'source_notes':len(originals)})
        for local,name in plan['media']:
            data=base64.b64encode((ROOT/local).read_bytes()).decode()
            call('storeMediaFile',filename=name,data=data)
            log('media',{'name':name})
        ensure_models()
        for d in plan['decks']: call('createDeck',deck=d)
        results=[]
        for e in plan['entries']:
            target=MODELS[e['source_model'] or ANKING]
            fields={name:'' for name in call('modelFieldNames',modelName=target)}
            fields.update(e['fields'])
            if 'ankihub_id' in fields: fields['ankihub_id']=''
            extra_tags=[TAG,f'NEBLI::objetivo::{e["objective"]}',f'NEBLI::origem::{e["origin"]}',id_tag(e),
                        'NEBLI::escopo::roteiro-do-caso' if e['scope']=='roteiro' else 'NEBLI::escopo::alem-do-roteiro']
            if e['rosa']: extra_tags.append('NEBLI::pos-prova::candidato-suspensao')
            tags=list(dict.fromkeys(e['source_tags']+extra_tags))
            existing=call('findNotes',query=f'tag:"{id_tag(e)}"')
            log('before-add',{'key':e['key'],'existing':existing})
            nid=existing[0] if existing else call('addNote',note={'deckName':e['deck'],'modelName':target,'fields':fields,'tags':tags,'options':{'allowDuplicate':True}})
            if not nid: raise RuntimeError(f'Add falhou: {e["key"]}')
            note=call('notesInfo',notes=[nid])[0]
            if plain(note)!=fields: raise RuntimeError(f'Campos divergentes: {e["key"]}')
            cards=call('cardsInfo',cards=note['cards'])
            if len(cards)!=e['expected_cards']: raise RuntimeError(f'Contagem divergente: {e["key"]}: {len(cards)}')
            misplaced=[c for c in cards if c['deckName']!=e['deck']]
            if misplaced:
                if any(c['reps']!=0 for c in misplaced): raise RuntimeError(f'Card estudado fora do deck: {e["key"]}')
                call('changeDeck',cards=[c['cardId'] for c in misplaced],deck=e['deck'])
            ids=[c['cardId'] for c in cards]
            flag=5 if e['rosa'] else (3 if e['high_yield'] else 0)
            if flag:
                for cid in ids: call('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[flag],warning_check=True)
            result={'key':e['key'],'source_nid':e['source_nid'],'new_nid':nid,'cards':ids,'origin':e['origin'],'objective':e['objective'],'scope':e['scope'],'deck':e['deck'],'high_yield':e['high_yield'],'rosa':e['rosa'],'flag':flag}
            results.append(result); log('created',result)
        all_cards=call('findCards',query=f'"deck:{plan["base_deck"]}"')
        if len(all_cards)!=plan['totals']['cards']: raise RuntimeError(f'Total final: {len(all_cards)}')
        if call('findCards',query=f'"deck:{plan["base_deck"]}" is:suspended'): raise RuntimeError('Card suspenso inesperado')
        now_sources=snapshot(plan)
        for nid,old in originals.items():
            now=now_sources[nid]
            if old['fields']!=now['fields'] or old['tags']!=now['tags']: raise RuntimeError(f'Fonte alterada: {nid}')
        if model_snapshot()!=models: raise RuntimeError('Modelo fonte alterado')
        flags={k:len(call('findCards',query=f'"deck:{plan["base_deck"]}" flag:{k}')) for k in range(8)}
        receipt={'at':datetime.now(timezone.utc).isoformat(),'lesson_id':LESSON,'decks':plan['decks'],'plan_sha256':digest(plan),
          'notes':len(results),'cards':len(all_cards),'totals':plan['totals'],'flags':flags,'suspended':0,'sources_unchanged':True,'results':results}
        save('receipt.json',receipt); log('complete',{k:v for k,v in receipt.items() if k!='results'})
        print(json.dumps({k:v for k,v in receipt.items() if k!='results'},ensure_ascii=False,indent=1))
    finally: lock.unlink(missing_ok=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['check','apply']);a=p.parse_args()
    plan=json.loads((ROOT/'plan.json').read_text(encoding='utf-8'))
    if a.mode=='check': print(json.dumps(check(plan),ensure_ascii=False,indent=1))
    else: apply(plan)
