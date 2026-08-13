import copy, json, subprocess, sys
from pathlib import Path
from conftest import lesson
SCRIPT=Path(__file__).parents[1]/'scripts'/'gerar_manifesto_ankidroid.py'

def run(tmp_path,data):
    path=tmp_path/'deck.json'; path.write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
    return subprocess.run([sys.executable,str(SCRIPT),'--slug','x','--deck-data',str(path),'--out',str(tmp_path/'out.json')],capture_output=True,text=True)

def test_external_sources_are_suspended(tmp_path):
    _,data=lesson(tmp_path); data['cards'][0]['source']='external_deck'
    p=run(tmp_path,data); assert p.returncode!=0 and 'source_not_allowed_in_authored_only' in (p.stdout+p.stderr)

def test_io_requires_credit_and_hide_two(tmp_path):
    _,data=lesson(tmp_path); data['cards'][1]['source_credit']=''; data['cards'][1]['mode']='hide_all_guess_all'
    p=run(tmp_path,data); assert p.returncode!=0 and 'hide_two_guess_two' in (p.stdout+p.stderr)
