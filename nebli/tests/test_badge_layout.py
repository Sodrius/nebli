"""Executa o JS real do badge contra o ID nativo verificado na janela Anki."""
import ast
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None


@unittest.skipIf(sync_playwright is None, 'Playwright não instalado neste Python')
class BadgeLayoutTest(unittest.TestCase):
    def test_bandeira_nativa_e_estado_sem_bandeira_em_duas_larguras(self):
        path = Path(__file__).resolve().parents[2] / 'anki-addon/nebli_explicacoes/__init__.py'
        tree = ast.parse(path.read_text())
        fn = next(x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == '_show_like_badge')
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            for width in [390, 1280]:
                for flag in [False, True]:
                    for liked in [False, True]:
                        with self.subTest(width=width, flag=flag, liked=liked):
                            page = browser.new_page(viewport={'width': width, 'height': 800})
                            page.set_content('<span id="_flag" style="position:fixed;right:10px;top:10px;width:18px;height:35px;display:' + ('block' if flag else 'none') + '">⚑</span>')
                            scripts = []
                            ns = {'json': json, '_is_liked': lambda cid: liked,
                                  '_reviewer': lambda: SimpleNamespace(card=SimpleNamespace(id=1), web=SimpleNamespace(eval=scripts.append))}
                            exec(compile(ast.Module(body=[fn], type_ignores=[]), str(path), 'exec'), ns)
                            ns['_show_like_badge']()
                            page.evaluate(scripts[0])
                            state = page.evaluate("""()=>{let n=document.querySelector('#nebli-like-badge'),a=n.getBoundingClientRect(),b=document.querySelector('#_flag').getBoundingClientRect();return {visible:a.left>=0&&a.right<=innerWidth,gap:b.left-a.right,text:n.textContent}}""")
                            self.assertTrue(state['visible'])
                            self.assertEqual(state['text'], '♥' if liked else '♡')
                            if flag:
                                self.assertGreaterEqual(state['gap'], 11.9)
                            page.close()
            browser.close()
