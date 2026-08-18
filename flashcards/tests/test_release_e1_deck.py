import hashlib, json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / 'scripts'))
from conftest import lesson
from validar_release_e1_deck import validate_release
VALID=Path(__file__).parents[1]/'scripts'/'validar_deck_card_a_card.py'; FINAL=Path(__file__).parents[1]/'scripts'/'finalizar_entrega_canonica.py'

def test_golden_end_to_end_and_stale_report_rejected(tmp_path):
    deck,data=lesson(tmp_path); report=tmp_path/'validation.json'; out=tmp_path/'out'
    p=subprocess.run([sys.executable,str(VALID),str(deck),'--out',str(report)],capture_output=True,text=True); assert p.returncode==0,p.stderr
    p=subprocess.run([sys.executable,str(FINAL),'--slug','aula','--deck-data',str(deck),'--validation-report',str(report),'--out-dir',str(out)],capture_output=True,text=True); assert p.returncode==0,p.stderr
    data['cards'][0]['extra']='Conteúdo alterado depois da validação.'; deck.write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
    p=subprocess.run([sys.executable,str(FINAL),'--slug','aula','--deck-data',str(deck),'--validation-report',str(report),'--out-dir',str(out)],capture_output=True,text=True)
    assert p.returncode!=0 and 'mudaram depois da validação' in (p.stdout+p.stderr)

def test_e1_matrix_questions_and_visual_ledger_are_gates(tmp_path):
    deck,data=lesson(tmp_path); data['release_gate']['source_to_e1_matrix']=[]; deck.write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
    p=subprocess.run([sys.executable,str(FINAL.parent/'gerar_manifesto_ankidroid.py'),'--slug','aula','--deck-data',str(deck),'--out',str(tmp_path/'m.json')],capture_output=True,text=True)
    assert p.returncode!=0 and 'source_to_e1_matrix' in (p.stdout+p.stderr)


def test_blocks_all_verbal_deck_when_e1_has_figures(tmp_path):
    """ERROS.md 51: E1 com ledger de figuras não fecha com deck sem card visual.

    Regressão da entrega de Lesão Celular I: 14 figuras revisadas na E1 e zero
    card com imagem, e nenhum gate reclamou.
    """
    deck, data = lesson(tmp_path)
    data['cards'] = [c for c in data['cards'] if c['source'] != 'io']
    data['release_gate']['concepts'] = [
        c for c in data['release_gate']['concepts'] if c['concept_id'] != 'c2'
    ]
    result = validate_release(data, deck.resolve())
    assert any('nenhum card visual' in e for e in result['errors']), result['errors']

    data['release_gate']['visual_card_absence_rationale'] = (
        'Nenhum objetivo da aula envolve reconhecimento visual; as figuras servem à prosa.'
    )
    result = validate_release(data, deck.resolve())
    assert not any('nenhum card visual' in e for e in result['errors']), result['errors']


def test_accepts_deck_with_authored_extra_image(tmp_path):
    deck, data = lesson(tmp_path)
    data['cards'] = [c for c in data['cards'] if c['source'] != 'io']
    data['release_gate']['concepts'] = [
        c for c in data['release_gate']['concepts'] if c['concept_id'] != 'c2'
    ]
    data['cards'][0]['extra_images'] = [{
        'path': 'fluxo.png',
        'source_credit': 'material sintético público',
        'cognitive_purpose': 'reconhecer a peça que se abre',
        'didactic_value_reviewed': True,
    }]
    result = validate_release(data, deck.resolve())
    assert not any('nenhum card visual' in e for e in result['errors']), result['errors']
