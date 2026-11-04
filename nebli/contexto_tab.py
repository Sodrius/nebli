"""Contexto de planejamento local para explicar cards sem consultas adicionais ao Anki.

Não usa o plano como fonte científica: intenção e vizinhos são rotulados como tal.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'arquivos-trabalho'

def read(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return {}

def index(root=ROOT):
    result = {}
    # Mais recente por timestamp do recibo de instalação, não por edição do plano.
    receipts = sorted(Path(root).glob('*/receipt.json'), key=lambda p:p.stat().st_mtime)
    for receipt_path in receipts:
        run=receipt_path.parent
        plan=read(run/'plan-aplicado.json') or read(run/'plan.json')
        if not isinstance(plan,dict): continue
        entries=plan.get('entries',[])
        if not isinstance(entries,list): continue
        by_key={e.get('key'):e for e in entries if isinstance(e,dict)}
        for nid,shared in plan.get('compartilhados',{}).items():
            if not isinstance(shared,dict): continue
            key=nid if nid.startswith('sh-') else 'sh-'+nid
            by_key.setdefault(key, shared)
        receipt=read(receipt_path)
        if not isinstance(receipt,dict): continue
        installed=receipt.get('notes',[])
        if not isinstance(installed,list): installed=[]
        mapping={x.get('key'):x.get('nid') for x in installed if isinstance(x,dict)}
        for key in set(by_key) | set(plan.get('compartilhados',{})):
            if key and key.startswith('sh-') and key[3:].isdigit(): mapping[key]=int(key[3:])
        motives=read(run/'motivacoes.json').get('motivacoes',[])
        depth=read(run/'mapa-de-profundidade.json').get('passos',[])
        for key,nid in mapping.items():
            if not nid: continue
            entry=by_key.get(key,{})
            items=[i for p in depth for i in p.get('itens',[]) if key in i.get('cards',[])]
            needs=[m for m in motives if key in m.get('atendida_por',[])]
            if not items and not needs and not entry.get('alvo'): continue
            result[int(nid)]={
                'natureza':'Intenção de planejamento; conferir ciência nas fontes, não tomar este texto como evidência científica.',
                'corrida':run.name,
                'objetivo':plan.get('escopo',{}).get('objetivo',''),
                'alvo_planejado':entry.get('alvo',''),
                'capacidades':[{'tipo':i.get('tipo'),'o_que':i.get('o_que'),'fonte':i.get('fonte')} for i in items],
                'reconstruir':[m.get('reconstruir','') for m in needs],
                'encaixe':[m.get('depois_de','') for m in needs],
            }
    return result
