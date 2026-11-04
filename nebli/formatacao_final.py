"""Gate de revisão visual final por agente, vinculado aos campos vivos no Anki."""
import hashlib
import json
from pathlib import Path

REPORT='formatacao-final-parecer.json'
INPUT='formatacao-final-entrada.json'

def _sha(fields):
    return hashlib.sha256(json.dumps(fields,sort_keys=True,ensure_ascii=False).encode()).hexdigest()

def _authors(plan):
    return {e['key'] for e in plan.get('entries',[]) if e.get('origin')=='Autoral'}

def pacote(run,plan,call):
    run=Path(run);receipt=json.loads((run/'receipt.json').read_text())
    wanted=_authors(plan);ids={x['key']:x['nid'] for x in receipt['notes'] if x['key'] in wanted}
    if set(ids)!=wanted:
        raise ValueError('autoral ausente do recibo da instalação')
    live={n['noteId']:n for n in call('notesInfo',notes=list(ids.values()))}
    out={}
    for key,nid in ids.items():
        n=live[nid];f={k:v['value'] for k,v in n['fields'].items() if k in ('Text','Front','Extra','Back','Back Extra','Imagem','Imagem Verso')}
        out[key]={'nid':nid,'campos':f,'sha256':_sha(f),'cards':sorted(n['cards']),'tem_imagem':any('<img' in v for v in f.values())}
    return out

def preparar(run,plan,call):
    out=pacote(run,plan,call)
    (Path(run)/INPUT).write_text(json.dumps({'cards':out,'instrucoes':'Agente independente: abrir e conferir todas as faces, tamanho do verso, negrito, sublinhado, clozes e figuras no Anki; emitir parecer por card.'},ensure_ascii=False,indent=2))
    return out

def verificar(run,plan,call):
    label='[duro] agente independente conferiu formatação final de todos os autorais vivos, com hashes e imagens'
    if int(plan.get('pipeline_versao') or 1)<9:return [(label,True)]
    try:
        current=pacote(run,plan,call)
        report=json.loads((Path(run)/REPORT).read_text())
    except (OSError,ValueError,KeyError,TypeError):return [(label+': parecer ausente/inválido',False)]
    problems=[]
    if report.get('revisor',{}).get('papel')!='independente' or not report.get('revisor',{}).get('execucao'):
        problems.append('revisor independente sem execução identificável')
    cases=report.get('cards',{})
    if set(cases)!=set(current):problems.append('cobertura de cards incompleta')
    for key,actual in current.items():
        case=cases.get(key,{})
        if case.get('nid')!=actual['nid'] or case.get('sha256')!=actual['sha256'] or sorted(case.get('cards',[]))!=actual['cards']:
            problems.append(f'{key}: versão/cartões divergentes')
        if case.get('veredito')!='aprovado' or len(str(case.get('analise','')).strip())<30:
            problems.append(f'{key}: parecer insuficiente')
        if actual['tem_imagem'] and case.get('imagem_vista') is not True:
            problems.append(f'{key}: imagem não conferida')
    return [(label+(f": {problems[:4]}" if problems else ''),not problems)]
