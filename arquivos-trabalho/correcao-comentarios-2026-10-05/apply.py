"""Aplica apenas campos revisados, sem alterar cards/agendamento/flags/modelos."""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki, escrita, in_scope
from nebli.explicacoes import open_store, card_hash, style_version, STYLE
from tabs import TABS
P=Path(__file__).resolve().parent
A=Anki()
changes=json.loads((P/'changes.json').read_text())
arrow_media={
    name: Path('/Users/davisousa/NEBLI/arquivos-trabalho/deck-aula-uc08-an01-esofago-estomago-delgado-2026-10-02/io')/name
    for name in (
        'nebli-uc08-an01-io-constricao-cervical-Q-r2.svg',
        'nebli-uc08-an01-io-constricao-broncoaortica-Q-r2.svg',
        'nebli-uc08-an01-io-constricao-diafragmatica-Q-r2.svg',
    )
}
ids=[c['nid'] for c in changes]
live={n['noteId']:n for n in A('notesInfo',notes=ids)}
cards=A('cardsInfo',cards=[cid for n in live.values() for cid in n['cards']])
assert A('getActiveProfile')=='User 1'
assert all(in_scope(c['deckName']) for c in cards)
for change in changes:
    n=live[change['nid']]
    for key,before in change['before'].items():
        if n['fields'][key]['value'] not in (before,change['fields'][key]):
            raise SystemExit(f'Edição concorrente: {change["nid"]} {key}')
    if 'Text' in change['fields']:
        old=set(re.findall(r'\{\{c(\d+)::',n['fields']['Text']['value']))
        new=set(re.findall(r'\{\{c(\d+)::',change['fields']['Text']))
        assert old==new,(change['nid'],old,new)

if '--apply' not in sys.argv:
    html=['<html><meta charset="utf-8"><style>body{font:22px Arial;margin:16px;background:#fff;color:#222}section{border-bottom:2px solid #ccc;padding:16px 0}img{max-width:100%;height:auto}table{color:#222}h2{font-size:18px;color:#666}</style>']
    for change in changes:
        if set(change['fields'])=={'NEBLI_Comentario'}:continue
        n=live[change['nid']]; f={k:v['value'] for k,v in n['fields'].items()};f.update(change['fields'])
        front=f.get('Text',f.get('Header','')+f.get('Image',''))
        front=re.sub(r'\{\{c\d+::(.*?)(?:::[^}]*)?\}\}',r'<b style="color:#275b9b">\1</b>',front)
        content=front+'<hr>'+f.get('Extra',f.get('Remarks',''))
        media=Path.home()/'Library/Application Support/Anki2/User 1/collection.media'
        content=re.sub(r'src="([^"]+)"',lambda m:'src="'+(media/m[1]).as_uri()+'"',content)
        section=f'<section id="n{change["nid"]}"><h2>{change["nid"]}</h2>'+content+'</section>'
        html.append(section)
        (P/f'preview-{change["nid"]}.html').write_text(html[0]+section+'</html>')
    (P/'preview.html').write_text(''.join(html)+'</html>')
    print('Preflight OK;',len(ids),'notas;',len(cards),'cards. Prévia criada; Anki inalterado.')
    sys.exit()

db=open_store();db.row_factory=__import__('sqlite3').Row
saved={c['cardId']:dict(row) for c in cards for row in db.execute('select * from explicacoes where card_id=?',(c['cardId'],))}
backup=P/'apply-before.json'
if not backup.exists():backup.write_text(json.dumps({'notes':list(live.values()),'cards':cards,'tabs':saved},ensure_ascii=False,indent=2))
with escrita(A,'Correção dos comentários 05/10/2026'):
    # O mesmo asset é usado pelos cartões irmãos: a seta elimina a ambiguidade
    # sem alterar notas, modelos ou agendamentos.
    import base64
    for name, path in arrow_media.items():
        A('storeMediaFile', filename=name, data=base64.b64encode(path.read_bytes()).decode())
    for change in changes:
        current=A('notesInfo',notes=[change['nid']])[0]
        for key,old in change['before'].items():
            assert current['fields'][key]['value'] in (old,change['fields'][key]),f'Mudou durante aplicação: {change["nid"]}'
        if any(current['fields'][k]['value']!=v for k,v in change['fields'].items()):
            A('updateNoteFields',note={'id':change['nid'],'fields':change['fields']})
        with (P/'journal.jsonl').open('a') as log:log.write(json.dumps({'nid':change['nid'],'at':datetime.now(timezone.utc).isoformat(),'fields':list(change['fields'])})+'\n')
    after=A('notesInfo',notes=ids)
    after_cards=A('cardsInfo',cards=[c['cardId'] for c in cards])
    byid={n['noteId']:n for n in after}
    for change in changes:
        n=byid[change['nid']]
        assert n['cards']==live[change['nid']]['cards'],f'IDs alterados {n["noteId"]}'
        for k,v in change['fields'].items():assert n['fields'][k]['value']==v,(n['noteId'],k)
    old_cards={c['cardId']:c for c in cards}
    schedule=['queue','type','due','interval','factor','reps','lapses','left','odue','odid','flags']
    diffs=[]
    for c in after_cards:
        for k in schedule:
            if c.get(k)!=old_cards[c['cardId']].get(k):diffs.append([c['cardId'],k,old_cards[c['cardId']].get(k),c.get(k)])
    assert not diffs,('Estado pessoal mudou durante a execução',diffs)
    updated_tabs=[]
    for c in after_cards:
        old=saved.get(c['cardId'])
        replacement=TABS.get(c['note'])
        if isinstance(replacement,dict):replacement=replacement[c['ord']]
        if replacement:
            texto=replacement;status='ok';motivo='';model='revisao-editorial-codex-2026-10-05'
        elif old and old['status']=='ok':
            texto=old['texto'];status=old['status'];motivo=old['motivo'];model=old['modelo']
        else:
            raise RuntimeError(f'Tab ausente ou não aprovado: {c["cardId"]}')
        values=[v['value'] for v in sorted(c['fields'].values(),key=lambda f:f['order'])]
        # Para ajustes só visuais/editoriais, conserva o texto e sua versão de estilo.
        version=style_version(STYLE.read_text()) if replacement else old['estilo']
        db.execute('insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)',(c['cardId'],c['note'],card_hash(values,c['ord']),status,texto,motivo,version,model,datetime.now(timezone.utc).isoformat()))
        updated_tabs.append(c['cardId'])
    db.commit()
    receipt={'notes':len(after),'cards':len(after_cards),'tabs':len(updated_tabs),'schedule_differences':diffs,'field_readback':'ok','after':after,'at':datetime.now(timezone.utc).isoformat()}
    (P/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in receipt.items() if k!='after'},ensure_ascii=False))
