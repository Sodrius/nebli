import hashlib, json, subprocess, sys
from pathlib import Path
from conftest import lesson
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
