"""Política explícita UC07 (F-20261111-CODEX-01). Cor não significa prioridade."""
import re

def bandeira(modelo, campos, origem):
    texto=campos.get('Text','')
    io=(origem == 'Machado-IO' or 'Kenhub IO' in modelo or 'Kenhub Referência' in modelo
        or 'Image Occlusion' in modelo
        or bool(re.search(r'Qual estrutura a seta|abertura óssea|Identifique o nível',texto)))
    if io: return 3
    if origem.lower().replace('-', '').startswith('anking'): return 4
    return 5

def verificar(plano):
    problemas=[]
    items=[(e['key'],e) for e in plano.get('entries',[])]+[(f'sh-{k}',v) for k,v in plano.get('compartilhados',{}).items()]
    if not items: return ['UC07: plano vazio']
    for key,e in items:
        expected=bandeira(e.get('model',''),e.get('fields',{}),e.get('origin',''))
        got=[c['flag'] for c in e['cards']] if 'cards' in e else [{'verde':3,'azul':4,'rosa':5}.get(e.get('cor'))]
        if not got or any(g!=expected for g in got): problemas.append(f'{key}: bandeira esperada {expected}, obtida {got}')
    return problemas
