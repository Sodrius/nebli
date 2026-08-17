import json, subprocess, sys
from pathlib import Path
from conftest import lesson
VALID=Path(__file__).parents[1]/'scripts'/'validar_deck_card_a_card.py'; FINAL=Path(__file__).parents[1]/'scripts'/'finalizar_entrega_canonica.py'


def test_golden_end_to_end_and_stale_report_rejected(tmp_path):
    deck,data=lesson(tmp_path); report=tmp_path/'validation.json'; out=tmp_path/'out'
    p=subprocess.run([sys.executable,str(VALID),str(deck),'--out',str(report)],capture_output=True,text=True); assert p.returncode==0,p.stdout+p.stderr
    p=subprocess.run([sys.executable,str(FINAL),'--slug','aula','--deck-data',str(deck),'--validation-report',str(report),'--out-dir',str(out)],capture_output=True,text=True); assert p.returncode==0,p.stdout+p.stderr; assert (out/'aula.apkg').is_file()
    data['cards'][0]['extra']='Conteúdo alterado depois da validação.'; deck.write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
    p=subprocess.run([sys.executable,str(FINAL),'--slug','aula','--deck-data',str(deck),'--validation-report',str(report),'--out-dir',str(out)],capture_output=True,text=True); assert p.returncode!=0 and 'mudaram depois da validação' in (p.stdout+p.stderr)


def test_e1_matrix_is_gate_without_manifest_backend(tmp_path):
    deck,data=lesson(tmp_path); report=tmp_path/'validation.json'; out=tmp_path/'out'
    p=subprocess.run([sys.executable,str(VALID),str(deck),'--out',str(report)],capture_output=True,text=True); assert p.returncode==0,p.stdout+p.stderr
    data['release_gate']['source_to_e1_matrix']=[]; deck.write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
    p=subprocess.run([sys.executable,str(FINAL),'--slug','aula','--deck-data',str(deck),'--validation-report',str(report),'--out-dir',str(out)],capture_output=True,text=True); assert p.returncode!=0 and 'source_to_e1_matrix' in (p.stdout+p.stderr)
