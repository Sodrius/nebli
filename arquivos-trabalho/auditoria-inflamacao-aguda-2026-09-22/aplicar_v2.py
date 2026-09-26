"""Aplicação limitada ao plano auditado; originais, flags e agendamento preservados.

Não implementa o pipeline geral. `check` é read-only no Anki. `apply` exige
o plano conferido, exporta backup, usa precondições e registra cada operação.
"""
import argparse, base64, hashlib, html, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from inspecionar_v2 import call, ROOT
from preparar_v2 import digest, OUT, LESSON

TAG=f'NEBLI::{LESSON}'
CLONE='NEBLI AnKing independente - piloto v2'
HIST='NEBLI Histology independente - piloto v2'

def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def plain_fields(n):return {k:v['value'] for k,v in n['fields'].items()}
def key_tag(e):return f'NEBLI::source::nid-{e["source_nid"]}' if e.get('source_nid') else f'NEBLI::lesson-local::{LESSON}::{e["key"]}'
def flags(deck):return {str(i):call('findCards',query=f'deck:"{deck}" flag:{i}') for i in range(1,8)}
def fingerprint(cards):
    return {c['cardId']:{k:c.get(k) for k in ['note','ord','type','queue','due','interval','factor','reps','lapses','left','odue','odid']} for c in cards}
def desired_tags(e):
    group={'durable':'nucleo','exam':'prova','reserve':'reserva'}[e['retention_group']]
    y={'HY':'HY','HY relativo':'HY-relativo','HY provisório':'HY-provisorio','LY':'LY','não classificado':'nao-classificado'}[e['step_yield']]
    return [TAG,key_tag(e),'NEBLI::revisao::inflamacao-v2',f'NEBLI::IA::grupo::{group}',f'NEBLI::IA::faculdade::{e["local_priority"]}',f'NEBLI::IA::step::{y}']

def preflight(plan):
    if call('getMediaDirPath')!=plan['profile_evidence']:raise RuntimeError('Perfil mudou')
    assert len({e['key'] for e in plan['entries']})==len(plan['entries'])
    sources=call('notesInfo',notes=[n['noteId'] for n in plan['sources']])
    original={n['noteId']:n for n in sources}
    problems=[]
    for e in plan['entries']:
        if e.get('source_nid') and digest(original[e['source_nid']]['fields'])!=e['source_hash']:
            problems.append('Origem alterada '+e['key'])
        found=call('findNotes',query=f'tag:"{key_tag(e)}"')
        if len(found)>1:problems.append('Cópias duplicadas '+e['key'])
        if e.get('existing_nid'):
            if found!=[e['existing_nid']]:problems.append('Identidade mudou '+e['key'])
            else:
                now=plain_fields(call('notesInfo',notes=found)[0])
                # Uma reexecução aceita somente o antes ou o depois planejados, nunca edição alheia.
                for k,v in e['fields'].items():
                    if now[k] not in [e['before_fields'][k],v]:problems.append('Edição concorrente '+e['key']+'/'+k)
        elif found:
            n=call('notesInfo',notes=found)[0]
            if any(n['fields'].get(k,{}).get('value')!=v for k,v in e['fields'].items()):problems.append('Conflito preexistente '+e['key'])
        text=e['fields'].get('Text',(e.get('before_fields') or {}).get('Text',''))
        assert e['clozes']==sorted({int(c) for c in re.findall(r'\{\{c(\d+)::',text)}),e['key']
    if problems:raise RuntimeError('\n'.join(problems))
    return {'entries':len(plan['entries']),'expected_cards':sum(len(e['clozes']) for e in plan['entries']),'profile':plan['profile_evidence'],'checks':'identity, source fields, concurrent edits, clozes'}

def ensure_model(name,source):
    if name in call('modelNames'):return
    fields=call('modelFieldNames',modelName=source)
    templates=call('modelTemplates',modelName=source)
    css=call('modelStyling',modelName=source)['css']
    call('createModel',modelName=name,inOrderFields=fields,css=css,isCloze=True,cardTemplates=[{'Name':k,**v} for k,v in templates.items()])
    assert call('modelTemplates',modelName=name)==templates
    assert call('modelStyling',modelName=name)['css']==css

def apply(plan):
    lock=OUT/'apply.lock'
    with lock.open('x',encoding='utf-8') as f:f.write(datetime.now(timezone.utc).isoformat())
    journal=OUT/'journal.jsonl'
    def log(action,result):
        with journal.open('a',encoding='utf-8') as f:f.write(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'action':action,'result':result},ensure_ascii=False)+'\n')
    try:
        preflight(plan)
        baseline=ROOT/'before-v2.json'
        b=json.loads(baseline.read_text(encoding='utf-8'))
        current=call('cardsInfo',cards=[c['cardId'] for c in b['cards']])
        # Usa o agendamento imediatamente antes da escrita, sem apagar revisões após o primeiro snapshot.
        sched=fingerprint(current); initial_flags=flags(plan['target_deck'])
        save('scheduling-before-apply.json',{'cards':current,'flags':initial_flags})
        backup=OUT/'backup-antes-v2.apkg'
        if not backup.exists():
            assert call('exportPackage',deck=plan['target_deck'],path=str(backup.resolve()),includeSched=True)
        log('backup',str(backup))
        original_models={name:{'templates':call('modelTemplates',modelName=name),'styling':call('modelStyling',modelName=name)} for name in {n['modelName'] for n in plan['sources']}}
        for e in plan['entries']:
            if e.get('existing_nid'):continue
            name=HIST if e['origin'].startswith('Histology') else CLONE
            source=e.get('source_model',b['notes'][0]['modelName'])
            ensure_model(name,source)
        for name in plan['media']:
            value=base64.b64encode((OUT/name).read_bytes()).decode()
            existing=call('retrieveMediaFile',filename=name)
            if existing is not False and existing!=value:raise RuntimeError('Mídia com nome conflitante '+name)
            if existing is False:call('storeMediaFile',filename=name,data=value)
        results=[]
        for e in plan['entries']:
            found=call('findNotes',query=f'tag:"{key_tag(e)}"')
            if len(found)>1:raise RuntimeError('Duplicidade '+e['key'])
            if found:
                nid=found[0]; n=call('notesInfo',notes=[nid])[0];fields=plain_fields(n)
                patch={k:v for k,v in e['fields'].items() if fields.get(k)!=v}
                for k in patch:
                    if not e.get('existing_nid') or fields.get(k)!=e['before_fields'][k]:raise RuntimeError('Alteração concorrente '+e['key'])
                if patch:
                    log('before-update',{'nid':nid,'fields':{k:fields[k] for k in patch}})
                    call('updateNoteFields',note={'id':nid,'fields':patch})
                call('addTags',notes=[nid],tags=' '.join(desired_tags(e)))
                status='updated' if patch else 'reused'
            else:
                assert not e.get('existing_nid'),'Nota antiga desapareceu'
                model=HIST if e['origin'].startswith('Histology') else CLONE
                fields={k:'' for k in call('modelFieldNames',modelName=model)}
                fields.update(e['fields']);fields['ankihub_id']=''
                tags=list(dict.fromkeys(e.get('source_tags',[])+desired_tags(e)))
                log('before-add',{'key':e['key'],'identity':key_tag(e)})
                try:
                    nid=call('addNote',note={'deckName':plan['target_deck'],'modelName':model,'fields':fields,'tags':tags,'options':{'allowDuplicate':True}})
                except Exception:
                    reconciled=call('findNotes',query=f'tag:"{key_tag(e)}"')
                    if len(reconciled)!=1:raise
                    nid=reconciled[0]
                status='created'
            note=call('notesInfo',notes=[nid])[0]
            assert all(note['fields'][k]['value']==v for k,v in e['fields'].items()),e['key']
            cards=call('cardsInfo',cards=note['cards'])
            assert sorted(c['ord']+1 for c in cards)==e['clozes'],e['key']
            misplaced=[c for c in cards if c['deckName']!=plan['target_deck']]
            if misplaced:
                # Anki pode criar a nota de modelo recém-clonado no deck padrão.
                # Corrigir só cópias novas desta execução, nunca cards revisados ou compartilhados.
                assert not e.get('existing_nid') and all(c['reps']==0 for c in misplaced),e['key']
                assert 'NEBLI::revisao::inflamacao-v2' in note['tags'],e['key']
                log('place-new-cards',{'key':e['key'],'cards':[c['cardId'] for c in misplaced]})
                call('changeDeck',cards=[c['cardId'] for c in misplaced],deck=plan['target_deck'])
                cards=call('cardsInfo',cards=note['cards'])
            assert all(c['deckName']==plan['target_deck'] for c in cards),e['key']
            result={'key':e['key'],'nid':nid,'cards':[c['cardId'] for c in cards],'status':status}
            results.append(result);log('confirmed',result)
        assert fingerprint(call('cardsInfo',cards=list(sched)))==sched,'Agendamento mudou; revisar antes de continuar'
        assert flags(plan['target_deck'])==initial_flags,'Flags mudaram'
        for name,state in original_models.items():
            assert call('modelTemplates',modelName=name)==state['templates']
            assert call('modelStyling',modelName=name)==state['styling']
        for n in call('notesInfo',notes=[n['noteId'] for n in plan['sources']]):
            original=next(s for s in plan['sources'] if s['noteId']==n['noteId'])
            assert n['fields']==original['fields'] and n['tags']==original['tags'],'Origem alterada'
        nids=[r['nid'] for r in results]; notes=call('notesInfo',notes=nids)
        cards=call('cardsInfo',cards=[c for n in notes for c in n['cards']])
        save('after.json',{'notes':notes,'cards':cards})
        package=OUT/'Inflamacao aguda.apkg'
        assert call('exportPackage',deck=plan['target_deck'],path=str(package.resolve()),includeSched=False)
        receipt={'at':datetime.now(timezone.utc).isoformat(),'lesson_id':LESSON,'plan_hash':digest(plan),'results':results,'notes':len(notes),'cards':len(cards),'originals_and_templates_unchanged':True,'existing_scheduling_and_flags_unchanged':True,'package':str(package.resolve()),'package_sha256':hashlib.sha256(package.read_bytes()).hexdigest(),'sync':'not requested; Mac/Android not verified','next':'UC08 Histologia somente após aprovação'}
        save('receipt.json',receipt)
        print(json.dumps({k:v for k,v in receipt.items() if k!='results'},ensure_ascii=False))
    finally:
        lock.unlink()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['check','apply']);a=p.parse_args()
    plan=json.loads((OUT/'plan.json').read_text(encoding='utf-8'))
    if a.mode=='check':print(json.dumps(preflight(plan),ensure_ascii=False))
    else:apply(plan)
