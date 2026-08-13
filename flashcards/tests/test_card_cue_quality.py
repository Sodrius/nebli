import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'scripts'))
from canonical_cards import content_sha256
def test_hash_changes_with_learning_content_not_derived_fields():
    a={'card_key':'a','source':'authored','text':'A {{c1::válvula}} abre.','extra':'Explica.','derived':{'x':1}}
    b={**a,'derived':{'x':2}}; assert content_sha256(a)==content_sha256(b)
    b['extra']='Mudou.'; assert content_sha256(a)!=content_sha256(b)
