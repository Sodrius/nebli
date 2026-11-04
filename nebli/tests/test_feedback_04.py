from nebli.imagens_cards import fontes_visiveis_sob_imagem
from nebli.verificador_casos import forma_das_lacunas


def test_fonte_visivel_sob_imagem_reprova():
    bad = {"entries": [{"key": "a", "fields": {"Extra": '<img src="x.png"><br><small>Aula MB60, slide 22</small>'}}]}
    good = {"entries": [{"key": "a", "fields": {"Extra": '<img src="x.png"><br>O foco contém células transformadas.'}}]}
    assert fontes_visiveis_sob_imagem(bad)
    assert not fontes_visiveis_sob_imagem(good)


def test_pista_de_sigla_curta_reprova_em_organizador():
    entry = {"fields": {"Text": '<div data-nebli-organizacao="true">- L cells: {{c1::GLP-1::G…}}</div>'}}
    assert any("sigla curta" in p for p in forma_das_lacunas(entry))
