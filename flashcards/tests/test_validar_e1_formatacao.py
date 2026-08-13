from conftest import lesson
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'scripts'))
from validar_e1_formatacao import validate_e1_formatting

def test_canonical_typst_structure(tmp_path):
    deck,data=lesson(tmp_path); assert validate_e1_formatting(data['release_gate'],deck)==[]
    (tmp_path/'etapa1.typ').write_text('#set page(margin: 1mm)',encoding='utf-8')
    assert any('#set page' in e for e in validate_e1_formatting(data['release_gate'],deck))
