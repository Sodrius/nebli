import copy, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'scripts'))
from validar_deck_card_a_card import validate_report
from conftest import lesson

def test_authored_only_golden_and_hashes(tmp_path):
    _, data=lesson(tmp_path); result=validate_report(data)
    assert result['ok']; assert len(result['ordered_card_set_sha256'])==64
    assert all(len(row['content_sha256'])==64 for row in result['cards'])

def test_blocks_anking_english_cloze_and_ambiguity(tmp_path):
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0]); bad['source']='anking'; bad['text']='The valve is {{c2::very long hidden answer}}.'; bad.pop('semantic_review')
    result=validate_report({'cards':[bad],'expected_card_count':1,'card_budget_hard_max':2})
    failures=result['cards'][0]['failures']; assert 'source_not_allowed_in_authored_only' in failures

def test_io_two_masks_and_geometry(tmp_path):
    _, data=lesson(tmp_path); assert validate_report({'cards':[data['cards'][1]]})['ok']
    data['cards'][1]['masks'][1]['x']=.95
    assert not validate_report({'cards':[data['cards'][1]]})['ok']
