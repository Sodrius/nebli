"""Repercute correções verificadas no spec/plano para impedir regressão no rebuild."""
import json, hashlib, pprint, shutil
from pathlib import Path
from nebli.decks import Anki, now
from nebli.delta import same

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
ms=json.loads((HERE/'mudancas.json').read_text())
A=Anki()
h=lambda x:hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:16]
flag={'verde':3,'azul':4,'rosa':5}
for short in sorted({m['short'] for m in ms}):
    snap=json.loads((HERE/f'{short}-snapshot.json').read_text())
    run=ROOT/snap['run']; plan=json.loads((run/'plan.json').read_text())
    selected=[m for m in ms if m['short']==short]
    live={n['noteId']:n for n in A('notesInfo',notes=[m['nid'] for m in selected])}
    for name in ('spec.py','plan.json','plan-aplicado.json','correcoes-vivas.json','receipt.json'):
        if (run/name).exists() and not (HERE/f'{short}-before-{name}').exists(): shutil.copy2(run/name,HERE/f'{short}-before-{name}')
    specs={}
    cp=run/'correcoes-vivas.json'; corr=json.loads(cp.read_text()) if cp.exists() else {}
    for m in selected:
        n=live[m['nid']];e=next(e for e in plan['entries'] if e['key']==m['key'])
        assert all(same(n['fields'][f]['value'],v) for f,v in m['fields'].items()),m['key']
        fields={f:n['fields'][f]['value'] for f in m['fields']}
        e['fields'].update(fields)
        if fields:
            corr.setdefault(m['key'],{}).update(fields)
            corr[m['key']].update(_motivo=m['motivo'],_em=now(),_nid=m['nid'])
        spec={'fields_override':fields,'motivo':m['motivo']}
        if m.get('plan_metadata'):
            e.update(m['plan_metadata']);spec['metadata']=m['plan_metadata']
        if 'cor' in m:
            color=m['cor']['cor'];f=flag[color]
            e['flags']={k:f for k in e['flags']}
            for c in e['cards']: c.update(flag=f,cor=color)
            prefix=f"NEBLI::cor::{plan['lesson_id']}::"
            e['tags']=[t for t in e['tags'] if not t.startswith(prefix) and t!='NEBLI::lateral']+[prefix+color]
            if color=='rosa': e['tags'].append('NEBLI::lateral')
            spec['flags']={int(k):f for k in e['flags']}
            if color!='verde' and e.get('hy') in ('1','2'):
                e['clinica_lateral']=True;spec['clinica_lateral']=True
        e['motivo']=m['motivo'];e['fields_hash']=h(e['fields'])
        e['revisao_pontual']={'em':now(),'evidencia':str(HERE.relative_to(ROOT)),'motivo':m['motivo']}
        specs[m['key']]=spec
    plan['selection_hash']=h([(e['key'],e['fields_hash'],e['cards']) for e in plan['entries']])
    for name,f in [('verdes',3),('azuis',4),('rosas',5)]: plan['totais'][name]=sum(c['flag']==f for e in plan['entries'] for c in e['cards'])
    for name in ('plan.json','plan-aplicado.json'): (run/name).write_text(json.dumps(plan,ensure_ascii=False,indent=1))
    cp.write_text(json.dumps(corr,ensure_ascii=False,indent=1))
    marker='# Revisão pontual Codex 12/10/2026 — evidência em revisao-pontual-claude-2026-10-12'
    src=(run/'spec.py').read_text().split(marker)[0].rstrip()
    src+='\n\n'+marker+'\n_AJUSTES_CODEX_1210 = '+pprint.pformat(specs,width=115,sort_dicts=False)+'\n'
    src+='for _c in CARDS:\n    if _c["key"] in _AJUSTES_CODEX_1210:\n        _fix = _AJUSTES_CODEX_1210[_c["key"]]\n        _c.setdefault("fields_override", {}).update(_fix["fields_override"])\n        _c["motivo"] = _fix["motivo"]\n        if "flags" in _fix: _c["flags"] = _fix["flags"]\n        if _fix.get("clinica_lateral"): _c["clinica_lateral"] = True\n        if _fix.get("metadata"): _c.update(_fix["metadata"])\n'
    compile(src,str(run/'spec.py'),'exec');(run/'spec.py').write_text(src)
    print(short,len(selected),'notas persistidas',plan['totais'])
ids=[m['nid'] for m in ms if m['fields']]
(HERE/'query-campos.txt').write_text(' OR '.join('nid:'+str(n) for n in ids))
