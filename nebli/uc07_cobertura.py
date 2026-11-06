"""F-20261105-CODEX-06/07: básico recuperável agora; regional com destino.

Valida a rastreabilidade declarada, não substitui o julgamento das fontes.
"""
import json
from pathlib import Path


def problemas(dados, plan):
    erros = []
    entries = {e['key']: e for e in plan.get('entries', [])}
    entries.update({'sh-' + str(n): e for n, e in plan.get('compartilhados', {}).items()})
    basicos = dados.get('basicos') or []
    if not basicos:
        return ['nenhum alvo básico declarado; vazio não prova cobertura']
    for row in basicos:
        nome = row.get('alvo', '?')
        keys = row.get('cards') or []
        if not row.get('fonte') or not keys or not set(keys) <= set(entries):
            erros.append(f'{nome}: falta fonte ou frente recuperável no plano')
            continue
        if row.get('estado') != 'agora':
            erros.append(f'{nome}: básico não pode ser marcado como previsão')
        if row.get('modalidade') == 'identificacao':
            if row.get('kenhub_disponivel'):
                if not any(entries[k].get('origin') == 'Kenhub' and
                           entries[k].get('model') in ('NEBLI Kenhub IO v1', 'NEBLI Kenhub Referência v1')
                           for k in keys):
                    erros.append(f'{nome}: Kenhub disponível sem identificação Kenhub correspondente')
            elif len(row.get('motivo_fallback', '').strip()) < 30:
                erros.append(f'{nome}: fallback sem motivo concreto')
    presentes = {str(e.get('src', e.get('source_nid', ''))) for e in entries.values()}
    for row in dados.get('adiados', []):
        nome = row.get('alvo', '?')
        if not row.get('aula_destino') or not row.get('motivo') or row.get('estado') != 'previsto':
            erros.append(f'{nome}: IO regional sem destino ou contado indevidamente como entregue')
        if str(row.get('src', '')) in presentes:
            erros.append(f'{nome}: IO declarado adiado também está no plano atual')
    return erros


def verificar(run, plan):
    if int(plan.get('pipeline_versao') or 1) < 15 or 'uc07' not in plan.get('lesson_id', '').lower():
        return []
    path = Path(run) / 'mapa-de-profundidade.json'
    try:
        dados = json.loads(path.read_text()).get('uc07_basico_e_destino', {})
        erros = problemas(dados, plan)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        erros = [f'mapa UC07 básico/destino ausente/inválido: {exc}']
    return [('[duro] UC07 básico agora, Kenhub primeiro e IO regional com destino (F-20261105-CODEX-06/07)'
             + (': ' + '; '.join(erros[:3]) if erros else ''), not erros)]
