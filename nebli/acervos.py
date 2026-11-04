"""Catálogo e recibos verificáveis das buscas. Nenhuma escrita na coleção."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from nebli.preflight import discover_corpora, deck_query

ALIASES = {'anking step deck': 'AnKing', 'university of michigan - bluelink atlas': 'BlueLink',
           '100 concepts (dorian)': 'Dorian 100', 'usmle lab values': 'Lab Values'}
MINIMOS = {'AnKing', 'AnKing-MCAT', 'Histology', 'LLU Histology', 'BlueLink', 'AnatoKing',
           'Dope Anatomy', 'Ankisthesia', 'Dorian 100', 'Lab Values'}


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def catalogar(call):
    decks = sorted(call('deckNames'))
    corpora, excluded = [], []
    for root, use in discover_corpora(decks).items():
        name = root.split('::')[-1]
        if name.casefold().startswith('reserva histórica'):
            excluded.append({'deck': root, 'motivo': 'Reserva histórica explícita; não é referência externa'})
            continue
        name = ALIASES.get(name.casefold(), name)
        ids = sorted(set(call('findNotes', query=deck_query(root))))
        corpora.append({'nome': name, 'deck': root, 'consulta': deck_query(root), 'uso': use,
                        'total': len(ids), 'ids_sha256': digest(ids), 'status': 'disponivel' if ids else 'vazio'})
    result = {'schema_version': 1, 'origem': 'deckNames', 'corpora': corpora, 'excluidos': excluded}
    errors = validar_catalogo(result)
    if errors:
        raise RuntimeError('; '.join(errors))
    result['sha256'] = digest(result)
    return result


def validar_catalogo(catalog):
    entries = catalog.get('corpora', [])
    errors = []
    missing = MINIMOS - {c['nome'] for c in entries}
    if missing:
        errors.append('Acervos mínimos ausentes: ' + ', '.join(sorted(missing)))
    names = [c['nome'] for c in entries]
    if len(names) != len(set(names)):
        errors.append('Acervos com nomes ambíguos; resolver raízes duplicadas')
    for c in entries:
        if c.get('total', 0) <= 0 or c.get('status') != 'disponivel':
            errors.append(f"Acervo vazio/indisponível: {c['nome']}")
    return errors


def validar_indice(catalog, metadata, indexed_catalog=None):
    errors = validar_catalogo(catalog)
    if not indexed_catalog:
        errors.append('Índice sem catálogo verificável')
    elif indexed_catalog.get('sha256') != catalog.get('sha256'):
        errors.append('Catálogo do índice desatualizado')
    for c in catalog['corpora']:
        ids = sorted({m['nid'] for m in metadata if m['acervo'] == c['nome']})
        if len(ids) != c['total'] or digest(ids) != c['ids_sha256']:
            errors.append(f"Índice incompleto/desatualizado: {c['nome']}")
    if errors:
        raise RuntimeError('; '.join(errors) + '. Reindexar: python3 -m nebli.semantica indexar')


def salvar_catalogo(run, catalog):
    folder = Path(run) / 'busca'
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'acervos.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')


def registrar(run, route, record):
    """Hash de cada registro cobre consulta, catálogo, resultados e contagens."""
    record = dict(record, schema_amplitude=1)
    record['registro_sha256'] = digest(record)
    with (Path(run) / 'busca' / f'{route}.jsonl').open('a') as stream:
        stream.write(json.dumps(record, ensure_ascii=False) + '\n')


def verificar_amplitude(run, chaves=None):
    """Validação offline; não prova relevância, leitura humana nem atualidade viva."""
    run = Path(run)
    errors = []
    try:
        catalog = json.loads((run / 'busca/acervos.json').read_text())
        expected_hash = catalog.pop('sha256')
        if digest(catalog) != expected_hash:
            errors.append('Hash do catálogo diverge')
        catalog['sha256'] = expected_hash
        errors.extend(validar_catalogo(catalog))
        expected = {c['nome']: c for c in catalog['corpora']}
        for route in ('palavra-chave', 'semantica'):
            records = [json.loads(line) for line in (run / 'busca' / f'{route}.jsonl').read_text().splitlines() if line]
            # Histórico antigo preservado; o último recibo por chave é o vigente.
            latest = {r['chave']: r for r in records}
            keys = set(chaves) if chaves is not None else set(latest)
            if not keys:
                errors.append(f'{route}: nenhuma consulta')
            for key in sorted(keys):
                r = latest.get(key, {})
                h = r.get('registro_sha256')
                if not h or digest({k: v for k, v in r.items() if k != 'registro_sha256'}) != h:
                    errors.append(f'{route}/{key}: recibo ausente ou hash inválido')
                    continue
                if r.get('catalogo_sha256') != expected_hash or not r.get('consulta'):
                    errors.append(f'{route}/{key}: catálogo divergente ou consulta vazia')
                actual = {c['acervo']: c for c in r.get('cobertura_acervos', [])}
                for name, c in expected.items():
                    found = actual.get(name, {})
                    if found.get('total_acervo') != c['total'] or found.get('status') not in ('consultado', 'sem_resultados') or not found.get('consulta'):
                        errors.append(f'{route}/{key}: acervo não consultado: {name}')
                    if route == 'semantica':
                        returned = [x for x in r.get('top', []) if x.get('acervo') == name]
                        if found.get('avaliados') != c['total'] or not returned or found.get('retornados') != len(returned):
                            errors.append(f'{route}/{key}: ranking incompleto: {name}')
                    else:
                        ids = found.get('ids', [])
                        count = found.get('encontrados')
                        shown = found.get('exibidos')
                        if (count != len(set(ids)) or not isinstance(shown, int) or not isinstance(count, int)
                                or not 0 <= shown <= count or count > c['total']
                                or found.get('truncado') != (shown < count)
                                or found.get('status') != ('consultado' if count else 'sem_resultados')):
                            errors.append(f'{route}/{key}: contagens inconsistentes: {name}')
                if route == 'palavra-chave':
                    artifact = run / r.get('arquivo', '')
                    if not artifact.is_file() or file_hash(artifact) != r.get('arquivo_sha256'):
                        errors.append(f'{route}/{key}: artefato ausente/modificado')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Evidência de amplitude ausente/inválida: {exc}')
    return errors
