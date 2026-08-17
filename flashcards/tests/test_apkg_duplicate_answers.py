import copy, sys
from pathlib import Path
from conftest import lesson
SCRIPTS=Path(__file__).parents[1]/"scripts"; sys.path.insert(0,str(SCRIPTS))
from audit_apkg import audit
from exportar_apkg_canonico import canonical_deck_name, export_apkg


def test_apkg_duplicate_answer_matches_source_derivation_contract(tmp_path):
    deck,data=lesson(tmp_path)
    twin=copy.deepcopy(data["cards"][0]); twin["card_key"]="outra-valvula"; twin["text"]="Em outra relação ensinada, a peça reguladora também é a {{c1::válvula}}."; twin["retrieval_target"]="Identificar a peça reguladora da segunda relação."; twin["derivation_rationale"]="A mesma palavra nomeia uma recuperação funcional diferente e independente."; data["cards"][0]["derivation_rationale"]="A mesma palavra é recuperada aqui como resposta a uma relação causal distinta."
    data["cards"].append(twin); out=tmp_path/"justificado.apkg"; export_apkg(data,deck,out); result=audit(out,canonical_deck_name(data)); assert result["passed"],result["errors"]; assert result["justified_duplicate_answers"]==1
    bad=copy.deepcopy(data); bad["cards"][-1].pop("derivation_rationale",None); out2=tmp_path/"sem-justificativa.apkg"; export_apkg(bad,deck,out2); failed=audit(out2,canonical_deck_name(bad)); assert not failed["passed"]; assert failed["unjustified_duplicate_answers"]==1
