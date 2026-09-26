"""Explicitly authorized 25/09 audit corrections. No deck generation; guarded IDs."""
import json,re,uuid
from pathlib import Path
from urllib.request import Request,urlopen
from datetime import datetime,timezone

HERE=Path(__file__).parent;LOCK=HERE.parent/'ANKI-ESCRITA.lock'
snap=json.loads((HERE/'snapshot.json').read_text(encoding='utf-8'))
orig=json.loads((HERE/'verified-origins.json').read_text(encoding='utf-8'))
old={n['noteId']:n for n in snap['notes']}
def call(action,**params):
    req=Request('http://127.0.0.1:8765',json.dumps(dict(action=action,version=6,params=params)).encode(),{'Content-Type':'application/json'})
    with urlopen(req,timeout=45) as r: result=json.load(r)
    if result['error']:raise RuntimeError(f'{action}: {result["error"]}')
    return result['result']
def log(x):
    with (HERE/'fix-journal.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(x,ensure_ascii=False)+'\n')
def values(n):return {k:v['value'] for k,v in n['fields'].items()}
def guarded(nid):
    n=call('notesInfo',notes=[nid])[0]
    assert values(n)==values(old[nid]) and n['tags']==old[nid]['tags'],f'Concurrent edit {nid}'
    assert all(c['deckName'].startswith('NEBLI::UC') for c in call('cardsInfo',cards=n['cards']))
    return n

assert call('getActiveProfile')=='Davi'
token=str(uuid.uuid4())
with LOCK.open('x',encoding='utf-8') as f:json.dump(dict(executor='Codex',task='auditoria-correcoes-autorizadas-25-09',token=token),f)
try:
    # Preserve complete affected notes and scheduling before changes.
    changes={
      1790263385937:{'Text':'Colonies with active β-galactosidase turn {{c1::blue}} when grown with X-gal.'},
      1790265248472:{'Text':'Healthy lower airways contain {{c1::low-biomass microbial communities}}, rather than being strictly sterile.',
        'Extra':values(old[1790265248472])['Extra']+'<br><br>Correção científica: a descrição clássica de esterilidade não representa os achados atuais de microbiota pulmonar. <a href="https://pubmed.ncbi.nlm.nih.gov/28196961/">Dickson et al., 2017</a>.'},
      1790272038619:{'Extra':values(old[1790272038619])['Extra'].replace('São 11 em humanos.','')},
      1790253537706:{'Extra':'These thresholds belong to the lecture table; they are not a universal diagnostic definition of exudate.'},
    }
    deleted=1790271593612
    affected=set(changes)|{deleted}|{r['nid'] for r in orig['mismatch']}
    before=[guarded(nid) for nid in sorted(affected)]
    with (HERE/'before-fixes.json').open('x',encoding='utf-8') as f:json.dump(dict(notes=before,flags=snap['flags'],cards=snap['cards']),f,ensure_ascii=False)
    backup=HERE/'backup-intestinos-before-exclusion.apkg'
    assert not backup.exists()
    assert call('exportPackage',deck='NEBLI::UC08::P1::Biologia Tecidual::Intestinos',path=str(backup.resolve()),includeSched=True)
    assert backup.is_file() and backup.stat().st_size>0
    for nid,fields in changes.items():
        guarded(nid);call('updateNoteFields',note=dict(id=nid,fields=fields))
        after=values(call('notesInfo',notes=[nid])[0])
        assert all(after[k]==v for k,v in fields.items())
        log(dict(action='update_fields',nid=nid,fields=list(fields)))
    # Repair provenance without touching source fields/models.
    seen=set()
    for row in orig['mismatch']:
        nid=row['nid']
        if nid in seen:continue
        seen.add(nid);guarded(nid)
        label={'100 Concepts (Dorian)':'Dorian','LLU Histology':'LLU','Dope Anatomy':'Dope-Anatomy'}.get(row['actual'],row['actual'])
        call('removeTags',notes=[nid],tags='NEBLI::origem::AnKing')
        call('addTags',notes=[nid],tags='NEBLI::origem::'+label)
        after=call('notesInfo',notes=[nid])[0]
        assert 'NEBLI::origem::'+label in after['tags'] and 'NEBLI::origem::AnKing' not in after['tags']
        log(dict(action='origin_tag',nid=nid,origin=label))
    # Previously explicitly rejected authored target, not a suspension candidate.
    n=guarded(deleted);cs=call('cardsInfo',cards=n['cards'])
    assert len(cs)==1 and cs[0]['reps']==0
    assert sum(t.startswith('NEBLI::2026-') for t in n['tags'])==1
    call('deleteNotes',notes=[deleted]);assert not call('findCards',query=f'nid:{deleted}')
    log(dict(action='delete_rejected_authored',nid=deleted,backup=str(backup)))
    # Only snapshot pink cards still pink; no reference/personal other colors changed.
    pink=set(snap['flags']['5']) & set(call('findCards',query='deck:NEBLI::UC* flag:5'))
    for cid in sorted(pink):
        call('setSpecificValueOfCard',card=cid,keys=['flags'],newValues=[4],warning_check=True)
        log(dict(action='pink_to_blue',cid=cid))
    assert pink <= set(call('findCards',query='deck:NEBLI::UC* flag:4'))
    live_ids=call('findCards',query='deck:NEBLI::UC*')
    expected=set(c['cardId'] for c in snap['cards'])-{cs[0]['cardId']}
    assert set(live_ids)==expected,'Collection changed during run; reconcile before claiming final count'
    sync=call('sync')
    result=dict(at=datetime.now(timezone.utc).isoformat(),fields_changed=len(changes),origin_notes_changed=len(seen),origin_cards_changed=len(orig['mismatch']),
      deleted_notes=[deleted],blue_migrated=len(pink),cards=len(live_ids),sync_result=sync,
      originals_not_targeted=True,core_not_classified=True,backup=str(backup),
      flags={i:len(call('findCards',query=f'deck:NEBLI::UC* flag:{i}')) for i in range(8)})
    with (HERE/'fix-receipt.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
    print(json.dumps(result,ensure_ascii=True))
finally:
    if LOCK.exists() and json.loads(LOCK.read_text(encoding='utf-8')).get('token')==token:LOCK.unlink()
