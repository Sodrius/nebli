import json
import tempfile
import unittest
from pathlib import Path
from nebli.acervos import (MINIMOS, catalogar, digest, validar_indice, registrar,
                           salvar_catalogo, verificar_amplitude, file_hash)
from nebli.semantica import Indice


class AcervosTests(unittest.TestCase):
    def catalog(self):
        entries = [{'nome': n, 'total': 1, 'ids_sha256': digest([i]), 'status': 'disponivel',
                    'deck': n, 'consulta': f'deck:"{n}"'} for i, n in enumerate(sorted(MINIMOS))]
        c = {'schema_version': 1, 'corpora': entries}
        c['sha256'] = digest(c)
        return c

    def test_small_corpus_survives_global_3000(self):
        ix = Indice.__new__(Indice)
        ix.meta = [{'acervo': 'AnKing', 'nid': i} for i in range(3100)] + [{'acervo': 'Kenhub', 'nid': 9999}]
        ix.acervos = ['AnKing', 'Kenhub']
        def semantic(q, n_top):
            self.assertIsNone(n_top)
            return list(range(3101)), [0.9] * 3100 + [0.5]
        ix.semantica = semantic
        ix.bm25 = lambda q, n_top: []
        result = ix.buscar('anatomy')
        self.assertEqual([r['nid'] for r in result if r['acervo'] == 'Kenhub'], [9999])
        self.assertEqual(result[-1]['rank_sem'], 1)

    def test_missing_corpus_blocks_index(self):
        c = self.catalog()
        meta = [{'acervo': e['nome'], 'nid': i} for i, e in enumerate(c['corpora'])][:-1]
        with self.assertRaisesRegex(RuntimeError, 'Reindexar'):
            validar_indice(c, meta, c)

    def test_added_ids_block_index(self):
        c = self.catalog()
        meta = [{'acervo': e['nome'], 'nid': i} for i, e in enumerate(c['corpora'])]
        validar_indice(c, meta, c)
        meta[0]['nid'] = 55555
        with self.assertRaisesRegex(RuntimeError, 'Reindexar'):
            validar_indice(c, meta, c)

    def test_dynamic_discovery_and_reserve_exclusion(self):
        roots = {'BlueLink': 'University of Michigan - BlueLink Atlas', 'Dorian 100': '100 Concepts (Dorian)',
                 'Lab Values': 'USMLE Lab Values', 'AnKing': 'Anking Step Deck'}
        decks = [('Referências::' if n == 'AnKing' else 'Referências::Referências Externas::') + roots.get(n, n)
                 for n in MINIMOS | {'Kenhub', 'Reserva histórica UC07'}]
        def call(action, **kwargs):
            return decks if action == 'deckNames' else [1]
        c = catalogar(call)
        self.assertIn('Kenhub', {e['nome'] for e in c['corpora']})
        self.assertEqual(len(c['excluidos']), 1)
        with self.assertRaisesRegex(RuntimeError, 'vazio'):
            catalogar(lambda action, **kwargs: decks if action == 'deckNames' else [])

    def test_receipts_and_tampering(self):
        with tempfile.TemporaryDirectory() as d:
            run = Path(d)
            c = self.catalog()
            salvar_catalogo(run, c)
            artifact = run / 'busca/anking.txt'
            artifact.write_text('results')
            coverage = [{'acervo': e['nome'], 'total_acervo': 1, 'status': 'sem_resultados', 'consulta': 'foo', 'ids': [], 'encontrados': 0, 'exibidos': 0, 'truncado': False} for e in c['corpora']]
            for route in ('palavra-chave', 'semantica'):
                route_coverage = coverage if route == 'palavra-chave' else [dict(e, status='consultado', avaliados=1, retornados=1) for e in coverage]
                registrar(run, route, {'chave': 'concept', 'consulta': 'foo', 'catalogo_sha256': c['sha256'],
                    'cobertura_acervos': route_coverage, 'top': [{'acervo': e['nome'], 'nid': i} for i, e in enumerate(c['corpora'])], 'arquivo': 'busca/anking.txt', 'arquivo_sha256': file_hash(artifact)})
            self.assertEqual(verificar_amplitude(run, ['concept']), [])
            self.assertTrue(verificar_amplitude(run, ['missing']))
            artifact.write_text('modified')
            self.assertTrue(verificar_amplitude(run, ['concept']))


if __name__ == '__main__':
    unittest.main()
