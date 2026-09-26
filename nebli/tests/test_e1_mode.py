"""Guardas de composição; não certificam didática nem renderização científica."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


def module(filename, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'typst-build' / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


builder = module('gerar_main.py', 'nebli_e1_builder')
checker = module('precompile-check.py', 'nebli_e1_checker')


class E1ModeTests(unittest.TestCase):
    def test_only_e1_has_no_question_includes(self):
        with tempfile.TemporaryDirectory() as td:
            folder = Path(td)
            card = folder / 'tema.yml'
            card.write_text('slug: teste\ntitulo: Teste\nsumario: []\n', encoding='utf-8')
            for name in ('pre-aula.typ', 'etapa1.typ', 'resumindo.typ'):
                (folder / name).write_text('// fixture', encoding='utf-8')
            target = folder / 'main.typ'
            builder.gerar_main(card, target, somente_e1=True)
            text = target.read_text(encoding='utf-8')
            self.assertIn('#include "etapa1.typ"', text)
            self.assertIn('#include "resumindo.typ"', text)
            self.assertIn('#include "pre-aula.typ"', text)
            self.assertNotIn('etapa2.typ', text)
            self.assertNotIn('etapa3.typ', text)
            self.assertNotIn('#gabarito', text)
            self.assertEqual(checker.check_somente_e1(folder), [])
            import_line = next(x for x in text.splitlines() if x.startswith('#import'))
            import_path = import_line.split('"')[1]
            self.assertEqual((folder / import_path).resolve(),
                             ROOT / 'typst-template/nebli_v2_apostila.typ')

    def test_missing_e1_material_is_not_silently_accepted(self):
        with tempfile.TemporaryDirectory() as td:
            errors = checker.check_somente_e1(Path(td))
            self.assertEqual(len(errors), 4)

    def test_stale_questions_in_main_are_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            folder = Path(td)
            (folder / 'main.typ').write_text('#include "etapa2.typ"\n#gabarito-page(())', encoding='utf-8')
            self.assertTrue(any('questões/gabarito' in e for e in checker.check_somente_e1(folder)))

    def test_stale_toc_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            folder = Path(td)
            card = folder / 'tema.yml'
            card.write_text('slug: teste\nsumario:\n  - titulo: Etapa 2\n', encoding='utf-8')
            with self.assertRaises(ValueError):
                builder.gerar_main(card, folder / 'main.typ', somente_e1=True)

    def test_legacy_generation_still_available_explicitly(self):
        with tempfile.TemporaryDirectory() as td:
            folder = Path(td)
            card = folder / 'tema.yml'
            card.write_text('slug: teste\nsumario: []\n', encoding='utf-8')
            target = folder / 'main.typ'
            builder.gerar_main(card, target)
            self.assertIn('etapa2.typ', target.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
