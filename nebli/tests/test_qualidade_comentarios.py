from nebli.qualidade_comentarios import negrito_contexto, step2_only
from nebli.spec_lib import dicas
from nebli.verificador_casos import forma_das_lacunas
from nebli.gates import inducao_clozes


def test_negrito_tem_que_continuar_visivel_em_cada_criterio():
    assert negrito_contexto('<div data-nebli-organizacao="true"><b>Title</b><br>Effect: {{c1::<b>name</b>}}</div>') == [2]
    assert not negrito_contexto('<div data-nebli-organizacao="true"><b>Title</b><br><b>Effect</b>: {{c1::name}}</div>')


def test_only_step2_nao_confunde_conceito_com_tag_compartilhada():
    assert step2_only([{'noteId':1,'tags':['#AK_Step2_v12::x','#AK_Step1_v12::x']}, {'noteId':2,'tags':['#AK_Other::Only_Step_2']}]) == [2]


def test_escolha_literal_sem_iniciais_sobrevive_ao_gerador_e_gates():
    t='<div data-nebli-organizacao="true"><b>Mediators</b><br>A: {{c1::histamine}}<br>B: {{c1::leukotrienes}}<br>C: {{c1::cytokines}}<br>D: {{c1::tryptase}}</div>'
    pref='Davi, 05/11: retirar iniciais neste organizador; comentário preservado.'
    assert dicas(t,pref)==t
    e={'key':'mediators','origin':'Autoral','organizador':True,'fields':{'Text':t},'dicas_preferencia_davi':pref}
    assert not any('sem a dica' in p for p in forma_das_lacunas(e))
    assert inducao_clozes({'pipeline_versao':9,'entries':[e]})[0][1]
    assert '::h…' in dicas(t)


def test_sigla_curta_nao_recebe_inicial_que_revela_a_resposta():
    t='{{c1::IgE}} {{c1::IgG/IgM}} {{c1::GLP-1}}'
    assert dicas(t)==t
    e={'fields':{'Text':'<div data-nebli-organizacao="true">{{c1::IgE::I…}}</div>'}}
    assert any('sigla curta' in p for p in forma_das_lacunas(e))


def test_stats_identificam_io_pelo_modelo_e_pelo_contrato_de_campos():
    from nebli.stats_formatos import tipo
    assert tipo({'Image':'x.png','Question Mask':'q.svg'},'Enhanced')=='identificacao-visual'
    assert tipo({'Imagem Frente':'x.jpg'},'NEBLI Kenhub')=='identificacao-visual'
    assert tipo({'Text':'<div data-nebli-organizacao="true">{{c1::a}}</div>'},'Cloze')=='organizador'
    assert tipo({'Front':'What causes this?'},'Basic')=='pergunta-resposta'


def test_stats_nao_confundem_estudo_temporario_com_aprovacao_da_nota():
    from nebli.stats_formatos import suspensao_observada
    s=suspensao_observada({'id':1,'queue':2,'odid':50},{'1':60})
    assert s['suspenso'] and s['ativo_temporario_no_filtrado']
    assert suspensao_observada({'id':1,'queue':-1,'odid':0},{})['suspenso']
    assert not suspensao_observada({'id':1,'queue':2,'odid':0},{})['suspenso']


def test_conjunto_misto_nao_exige_iniciais_reveladoras_para_siglas():
    t='<div data-nebli-organizacao="true"><b>Effectors</b><br>I: {{c1::IgE}}<br>II: {{c1::IgG/IgM}}<br>III: {{c1::immune complexes}}<br>IV: {{c1::T cells}}</div>'
    e={'key':'mixed','origin':'Autoral','organizador':True,'fields':{'Text':t}}
    assert inducao_clozes({'pipeline_versao':9,'entries':[e]})[0][1]
    assert not any('sem a dica' in p for p in forma_das_lacunas(e))


def test_gate_do_badge_reprova_vazio_sobreposicao_e_saida_da_tela():
    from nebli.qualidade_comentarios import badge_layout_ok
    assert not badge_layout_ok({})
    base={'encontrado':True,'coracao_visivel':True,'bandeira_visivel':True}
    assert not badge_layout_ok(dict(base,gap=-5))
    assert badge_layout_ok(dict(base,gap=12))
    assert not badge_layout_ok(dict(base,coracao_visivel=False,gap=12))
    assert badge_layout_ok(dict(base,bandeira_visivel=False,gap=None))
