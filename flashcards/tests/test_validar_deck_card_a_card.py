import copy, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'scripts'))
from validar_deck_card_a_card import validate_report, validate_card
from conftest import lesson

def one(card, **extra):
    return validate_report({'cards':[card],'expected_card_count':1,'card_budget_hard_max':2,**extra})

def test_authored_only_golden_and_hashes(tmp_path):
    _, data=lesson(tmp_path); result=validate_report(data)
    assert result['ok'], result['cards']
    assert len(result['ordered_card_set_sha256'])==64
    assert all(len(row['content_sha256'])==64 for row in result['cards'])

def test_blocks_anking_english_cloze_and_ambiguity(tmp_path):
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0]); bad['source']='anking'; bad['text']='The valve is {{c2::very long hidden answer}}.'; bad.pop('semantic_review')
    failures = one(bad)['cards'][0]['failures']
    assert 'source_not_allowed_in_authored_only' in failures

def test_io_two_masks_and_geometry(tmp_path):
    _, data=lesson(tmp_path); assert one(data['cards'][1])['ok']
    data['cards'][1]['masks'][1]['x']=.95
    assert not one(data['cards'][1])['ok']

# --- Fase 1: idioma medido na frente, não declarado -------------------------

def test_blocks_english_front_even_with_portuguese_extra(tmp_path):
    """O lote UC03 inteiro passou porque o Extra português diluía a frente."""
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0])
    bad['text']='Routine tissue fixation prevents autolysis and preserves {{c1::architecture}}.'
    bad['extra']='A formalina estabiliza os componentes celulares antes do processamento.'
    assert 'front_appears_english' in one(bad)['cards'][0]['failures']

def test_accepts_portuguese_front_with_english_medical_term(tmp_path):
    _, data=lesson(tmp_path); card=copy.deepcopy(data['cards'][0])
    card['text']='As extremidades codificantes são seladas como {{c1::hairpins}} pela RAG.'
    card['retrieval_target']='Identificar a forma que sela as extremidades codificantes.'
    card['memory_gain']='A forma fechada que a RAG deixa nas extremidades codificantes.'
    card['ablation_loss']='Sem ele some o passo que exige abertura posterior por Artemis antes da junção.'
    assert 'front_appears_english' not in one(card)['cards'][0]['failures']

# --- Fase 2: resposta abstrata e discriminador fora da frente ---------------

def test_blocks_generic_answer(tmp_path):
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0])
    bad['text']='O retorno do eco determina a profundidade pelo {{c1::tempo}}.'
    assert 'generic_cloze' in one(bad)['cards'][0]['failures']

def test_blocks_card_whose_discriminator_lives_only_in_extra(tmp_path):
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0])
    bad['text']='A montagem final depende da {{c1::ligase}}.'
    bad['retrieval_target']='Recuperar qual complexo sela extremidades codificantes processadas.'
    bad['extra']='O complexo sela as extremidades codificantes já processadas pelo NHEJ.'
    assert 'discriminator_only_in_extra' in one(bad)['cards'][0]['failures']

def test_requires_cue_quality_contract(tmp_path):
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0]); bad.pop('cue_quality')
    assert 'cue_quality_missing' in one(bad)['cards'][0]['failures']

def test_rejects_unlisted_cloze_role(tmp_path):
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0])
    bad['cue_quality']={**bad['cue_quality'],'cloze_role':'curiosidade'}
    assert 'cue_quality.cloze_role' in one(bad)['cards'][0]['failures']

# --- Fase 3: ablação e orçamento -------------------------------------------

def test_requires_ablation_contract(tmp_path):
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0]); bad.pop('ablation_loss')
    assert 'ablation.ablation_loss' in one(bad)['cards'][0]['failures']

def test_blocks_ablation_loss_that_only_restates_the_card(tmp_path):
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0])
    bad['ablation_loss']='O aumento da pressão abre a de saída.'
    assert 'ablation_loss_restates_card' in one(bad)['cards'][0]['failures']

def test_missing_budget_blocks_instead_of_defaulting_to_expected(tmp_path):
    _, data=lesson(tmp_path); payload={'cards':data['cards']}
    result=validate_report(payload)
    assert not result['ok']
    assert 'card_budget_hard_max_missing' in result['report_failures']

def test_budget_exceeded_blocks(tmp_path):
    _, data=lesson(tmp_path)
    result=validate_report({**data,'card_budget_hard_max':2})
    assert not result['ok']
    assert any(f.startswith('card_budget_exceeded') for f in result['report_failures'])

def test_detects_duplicate_retrieval_across_cards(tmp_path):
    _, data=lesson(tmp_path); twin=copy.deepcopy(data['cards'][0]); twin['card_key']='pressao-valvula-2'
    twin['text']='O gradiente de pressão escancara a {{c1::válvula}} distal.'
    result=validate_report({'cards':[data['cards'][0],twin],'expected_card_count':2,'card_budget_hard_max':4})
    assert not result['ok']
    assert 'duplicate_retrieval' in result['cards'][1]['failures']
    assert result['duplicate_retrievals']

def test_duplicate_retrieval_allowed_with_declared_derivation(tmp_path):
    _, data=lesson(tmp_path); twin=copy.deepcopy(data['cards'][0]); twin['card_key']='pressao-valvula-2'
    twin['text']='O gradiente de pressão escancara a {{c1::válvula}} distal.'
    twin['derivation_rationale']='Recupera a mesma peça em outro território, exigido pelo contrato de cobertura.'
    result=validate_report({'cards':[data['cards'][0],twin],'expected_card_count':2,'card_budget_hard_max':4})
    assert 'duplicate_retrieval' not in result['cards'][1]['failures']

# --- Fase 5: prova visual do IO, não booleano ------------------------------

def io(data, **patch):
    card=copy.deepcopy(data['cards'][1]); card.update(patch); return one(card)['cards'][0]['failures']

def test_requires_rendered_previews(tmp_path):
    _, data=lesson(tmp_path)
    assert 'io_visual_evidence_missing' in io(data, visual_evidence=None)

def test_blocks_crop_that_is_the_whole_slide(tmp_path):
    _, data=lesson(tmp_path); ev=dict(data['cards'][1]['visual_evidence']); ev['crop_ratio']=0.97
    assert 'io_crop_is_whole_slide' in io(data, visual_evidence=ev)

def test_blocks_leak_even_when_no_leak_declared_true(tmp_path):
    """O manifesto dizia no_leak=true enquanto o título revelava a resposta."""
    _, data=lesson(tmp_path); ev=dict(data['cards'][1]['visual_evidence']); ev['leaked_terms']=['entrada']
    failures=io(data, visual_evidence=ev)
    assert 'io_answer_leaks_outside_mask' in failures
    assert data['cards'][1]['visual_review']['no_leak'] is True

def test_requires_every_answer_listed_as_forbidden_term(tmp_path):
    _, data=lesson(tmp_path); ev=dict(data['cards'][1]['visual_evidence']); ev['forbidden_terms']=['entrada']
    assert 'io_answer_not_listed_as_forbidden_term' in io(data, visual_evidence=ev)

def test_blocks_pair_rationale_that_only_repeats_the_labels(tmp_path):
    _, data=lesson(tmp_path)
    assert 'io_pair_rationale_only_repeats_labels' in io(data, pair_rationale='Entrada e saída, entrada e saída.')

# --- comentários novos: alternativas na resposta e termo não ensinado -------

def test_blocks_answer_offering_alternatives(tmp_path):
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0])
    bad['text']='Em disjunção, dis- indica {{c1::separação ou afastamento}}.'
    assert 'cloze_answer_offers_alternatives' in one(bad)['cards'][0]['failures']

def test_allows_compound_name_with_declared_reason(tmp_path):
    _, data=lesson(tmp_path); card=copy.deepcopy(data['cards'][0])
    card['text']='A clivagem V(D)J é iniciada pelo núcleo {{c1::RAG1/RAG2}}.'
    card['compound_answer_reason']='RAG1 e RAG2 formam um único complexo; separar destrói o nome da enzima.'
    assert 'cloze_answer_offers_alternatives' not in one(card)['cards'][0]['failures']

def test_blocks_answer_absent_from_e1_anchor(tmp_path):
    """"não sei o que é evaginação sacular": o card estreava o termo."""
    _, data=lesson(tmp_path); bad=copy.deepcopy(data['cards'][0])
    bad['text']='A forma diverticul/o refere-se a uma {{c1::evaginação}}.'
    assert 'answer_not_in_e1_anchor' in one(bad)['cards'][0]['failures']
