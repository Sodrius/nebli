"""Impede que um plano antigo reinstale conteúdo ou notas retiradas já corrigidos.

Registro aponta para recibos efetivamente aplicados; propostas não viram norma viva.
"""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REGISTRY=ROOT/'config/correcoes-vigentes.json'
def verificar(run,plan,registry=REGISTRY):
    if not Path(registry).exists():return [("regressões: nenhuma correção implantada registrada",True)]
    label='[duro] não reintroduzir campos superados nem notas retiradas por correção explícita'
    try:
        registry_data=json.loads(Path(registry).read_text())
        rows=registry_data.get('revisoes',[])
        if not rows:raise ValueError('registro vazio')
        current={}
        for row in rows:
            path=ROOT/row['recibo'];raw=path.read_bytes()
            if hashlib.sha256(raw).hexdigest()!=row['sha256']:raise ValueError('recibo alterado')
            data=json.loads(raw)
            if data.get('status')!='aplicado_verificado':raise ValueError('correção não verificada')
            for note in data.get('notas',[]):current[int(note['nid'])]=note
        placements=[]
        for row in registry_data.get('posicoes',[]):
            path=ROOT/row['recibo'];raw=path.read_bytes()
            if hashlib.sha256(raw).hexdigest()!=row['sha256']:raise ValueError('recibo de posição alterado')
            data=json.loads(raw)
            if data.get('status')!='aplicado_verificado':raise ValueError('posição não verificada')
            placements.append((int(row['nid']), {int(cid):deck for cid,deck in row['cards'].items()}))
        path=Path(run)/'receipt.json';receipt=json.loads(path.read_text()) if path.exists() else {}
        installed=receipt.get('notes',[]);installed=installed if isinstance(installed,list) else []
        by_key={x.get('key'):x.get('nid') for x in installed if isinstance(x,dict)}
        errors=[]
        for entry in plan.get('entries',[]):
            nid=entry.get('nid') or by_key.get(entry.get('key'));correction=current.get(int(nid)) if nid else None
            if not correction:continue
            if correction.get('retirado'):errors.append(f'{entry.get("key")}: nota {nid} retirada, escolher substituto')
            for field,expected in correction.get('campos',{}).items():
                if field in ('NEBLI_Comentario','NEBLI_Resposta'):continue
                if entry.get('fields',{}).get(field)!=expected:errors.append(f'{entry.get("key")}/{field}: conteúdo anterior à correção; atualizar spec e revisar')
        for key in plan.get('compartilhados',{}):
            digits=str(key).removeprefix('sh-')
            if digits.isdigit() and current.get(int(digits),{}).get('retirado'):errors.append(f'compartilhado {key} retirado, usar organizador/substituto')
        planned_nids={int(nid) for entry in plan.get('entries',[])
                      if (nid:=entry.get('nid') or by_key.get(entry.get('key')))}
        for nid,cards in placements:
            if nid in planned_nids and any(deck!=plan.get('deck') for deck in cards.values()):
                errors.append(f'nota {nid}: irmãos em decks diferentes; apply comum os reuniria; preservar posição de cada card')
        return [(label+(': '+'; '.join(errors[:8]) if errors else ''),not errors)]
    except (OSError,ValueError,KeyError,TypeError) as exc:return [(label+': '+str(exc),False)]
