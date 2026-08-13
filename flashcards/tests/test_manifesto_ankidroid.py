import json, subprocess, sys
from pathlib import Path
from conftest import lesson
SCRIPT=Path(__file__).parents[1]/'scripts'/'gerar_manifesto_ankidroid.py'

def test_golden_manifest_authored_only_compatibility_and_media(tmp_path):
    deck,_=lesson(tmp_path); out=tmp_path/'aula.ankidroid.json'
    p=subprocess.run([sys.executable,str(SCRIPT),'--slug','aula-sintetica','--deck-data',str(deck),'--out',str(out)],capture_output=True,text=True)
    assert p.returncode==0,p.stderr
    m=json.loads(out.read_text()); assert m['pipeline_version']=='e1-deck-v11'; assert m['card_source_mode']=='authored_only'
    assert m['minimum_companion_version']=='0.8.0' and m['minimum_companion_version_code']==13
    assert {c['source'] for c in m['cards']}=={'authored','io'}; assert len(m['ordered_card_set_sha256'])==64
    assert m['optional_subdeck'].endswith('::Optional') and len(m['media'])==1
