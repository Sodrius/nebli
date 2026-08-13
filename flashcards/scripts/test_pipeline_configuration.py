import json
from pathlib import Path

CFG=Path(__file__).parents[2]/'config'/'pipeline.json'

def test_authored_only_is_mechanical_authority():
    c=json.loads(CFG.read_text())
    assert c['pipeline_version']=='e1-deck-v11'
    assert c['card_source_mode']=='authored_only'
    assert c['source_priority']==['authored','io']
    assert c['anking']=={'status':'suspended','preserve_infrastructure':True,'allow_runtime_lookup':False,'require_search_before_authorship':False,'allow_source_copy':False}
    assert c['external_decks']['status']=='suspended'
    assert c['image_occlusion']['multi_label_mode']=='hide_two_guess_two'
    assert c['authored_cards']['language']=='pt-BR'
