"""O registro de regressões precisa ser executável, não decorativo.

Cada entrada marcada `enforced_by: python` com um `reproved_example` é rodada
contra o gate real. Uma entrada que não reprova o próprio exemplo é uma
regressão que não existe — e o teste falha.
"""
import copy, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'scripts'))
from validar_deck_card_a_card import validate_report, validate_card
from feedback_regressions import load, regression_failures
from conftest import lesson

REGISTRY = json.loads((Path(__file__).parent/'feedback_regressions.json').read_text(encoding='utf-8'))
ENTRIES = REGISTRY['regressions']

def entries_with_examples():
    return [e for e in ENTRIES if e.get('enforced_by')=='python' and e.get('reproved_example')]

def test_registry_is_well_formed():
    assert REGISTRY['schema']=='nebli-feedback-regressions-v1'
    ids=[e['id'] for e in ENTRIES]
    assert len(ids)==len(set(ids)), 'ids duplicados no registro'
    for entry in ENTRIES:
        for key in ('id','pattern','origin','comment','enforced_by','required_after_fix'):
            assert str(entry.get(key) or '').strip(), f"{entry.get('id')}: campo {key} vazio"
        assert entry['enforced_by'] in {'python','java','manual'}

def test_every_python_regression_still_blocks_its_own_example(tmp_path):
    _, data = lesson(tmp_path)
    for entry in entries_with_examples():
        card = copy.deepcopy(data['cards'][0])
        card.update(entry['reproved_example'])
        failures = validate_card(card)
        assert entry['expected_failure'] in failures, (
            f"{entry['id']}: o gate deixou passar o exemplo reprovado. "
            f"esperado {entry['expected_failure']}, obtido {failures}"
        )

def test_report_level_regressions_block(tmp_path):
    _, data = lesson(tmp_path)
    # teto ausente
    assert 'card_budget_hard_max_missing' in validate_report({'cards':data['cards']})['report_failures']
    # recuperação duplicada
    twin = copy.deepcopy(data['cards'][0]); twin['card_key']='twin'
    result = validate_report({'cards':[data['cards'][0],twin],'expected_card_count':2,'card_budget_hard_max':4})
    assert 'duplicate_retrieval' in result['cards'][1]['failures']

def test_trofia_content_pair_is_enforced_and_fix_passes():
    bad = {'text':'Em <b>hipertrofia</b>, -trofia indica <b>{{c1::crescimento}}</b>.'}
    assert 'regression:trofia-desenvolvimento' in regression_failures(bad)
    good = {'text':'Em <b>hipertrofia</b>, -trofia indica <b>{{c1::desenvolvimento}}</b>.'}
    assert regression_failures(good)==[]

def test_java_entries_name_the_test_that_enforces_them():
    for entry in ENTRIES:
        if entry['enforced_by']=='java':
            assert str(entry.get('test') or '').strip(), f"{entry['id']}: entrada java sem teste nomeado"
