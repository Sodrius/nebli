"""Tipos de nota da UC07 (só usados por ela; podem ser atualizados no lugar sem afetar outras notas de Davi).

NEBLI Kenhub IO v1 — oclusão com seta (Kenhub, Netter, AnKing com “ID”, níveis do tronco):
  frente: só a figura com a estrutura mascarada, a seta e o “?” (campo Pergunta só quando a figura inteira é a pergunta);
  verso: o nome em português no topo + a mesma figura com o nome escrito no lugar do “?” (F-20261017-CLAUDE-02/04).
NEBLI UC07 Cloze v1 — cloze em português com o nome só (AnatoKing e AnKing conceitual), todas as imagens à vista, sem botões
  de escolher entre cadáver e modelo (F-20261017-CLAUDE-04). Ambos têm NEBLI_Comentario (Davi comenta em todo card).
"""

NOME = "NEBLI Kenhub IO v1"
CAMPOS = ["Nome PT", "Latim", "Nome EN", "Sinonimos", "Imagem", "MascaraP", "Fonte", "Extra", "ID (hidden)", "NEBLI_Comentario",
          "MascaraR", "Pergunta"]

FRENTE = """{{#Imagem}}
<div id="kh-topo">{{#Pergunta}}<div id="kh-perg">{{Pergunta}}</div>{{/Pergunta}}</div>
<div id="kh-wrap">
  <div id="kh-img">{{Imagem}}</div>
  <div class="kh-over">{{MascaraP}}</div>
</div>
{{/Imagem}}"""

VERSO = """<div id="kh-topo"><div id="kh-nome">{{Nome PT}}</div></div>
<div id="kh-wrap">
  <div id="kh-img">{{Imagem}}</div>
  <div class="kh-over">{{MascaraR}}</div>
</div>
{{#Extra}}<div id="kh-extra">{{Extra}}</div>{{/Extra}}
<div id="kh-fonte">{{Fonte}}</div>"""

CSS = """.card {
  font-family: Helvetica, Arial, sans-serif;
  text-align: center;
  color: black;
  background-color: white;
  margin: 0;
  padding: 4px;
}
.nightMode .card, .night_mode .card { color: #eee; background-color: #2b2b2b; }

/* topo de altura fixa: a figura não pula ao virar o card e o nome nunca exige rolar */
#kh-topo { height: 64px; overflow: hidden; display: flex; align-items: center; justify-content: center; }
#kh-nome { font-size: 1.7em; font-weight: bold; line-height: 1.1; }
#kh-perg { font-size: 1.15em; }
/* a figura (de qualquer proporção) cabe inteira abaixo do topo; as sobreposições acompanham o tamanho dela */
#kh-wrap { position: relative; display: inline-block; line-height: 0; max-width: 100%; }
#kh-img img { display: block; max-width: 100%; max-height: calc(100vh - 80px); width: auto; height: auto; }
.kh-over { position: absolute; top: 0; left: 0; right: 0; bottom: 0; }
.kh-over img { width: 100%; height: 100%; }
#kh-extra { font-size: 0.85em; margin: 8px auto 0; max-width: 900px; text-align: left; line-height: 1.35; }
#kh-extra img { max-width: 100%; max-height: 60vh; }
#kh-fonte { font-size: 0.6em; color: #999; margin-top: 2px; line-height: 1.2; }
.mobile #kh-nome { font-size: 1.3em; }
"""

CLOZE = "NEBLI UC07 Cloze v1"
CLOZE_CAMPOS = ["Text", "Imagens", "Extra", "Nome EN", "Fonte", "ID (hidden)", "NEBLI_Comentario"]
CLOZE_FRENTE = """<div id="u7-texto">{{cloze:Text}}</div>
{{#Imagens}}<div id="u7-imagens">{{Imagens}}</div>{{/Imagens}}"""
CLOZE_VERSO = """<div id="u7-texto">{{cloze:Text}}</div>
{{#Imagens}}<div id="u7-imagens">{{Imagens}}</div>{{/Imagens}}
{{#Extra}}<div id="u7-extra">{{Extra}}</div>{{/Extra}}
<div id="u7-fonte">{{Fonte}}</div>"""
CLOZE_CSS = """.card {
  font-family: Helvetica, Arial, sans-serif;
  text-align: center;
  color: black;
  background-color: white;
  margin: 0;
  padding: 6px;
}
.nightMode .card, .night_mode .card { color: #eee; background-color: #2b2b2b; }
#u7-texto { font-size: 1.25em; line-height: 1.3; margin: 4px auto 8px; max-width: 1000px; }
.cloze { font-weight: bold; color: #0645ad; }
.nightMode .cloze, .night_mode .cloze { color: #8ab4f8; }
/* todas as imagens à vista, lado a lado no PC e empilhadas no celular — nunca atrás de botão */
#u7-imagens { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; }
#u7-imagens img { max-width: 49%; max-height: calc(100vh - 120px); width: auto; height: auto; }
.mobile #u7-imagens img { max-width: 100%; max-height: 62vh; }
#u7-extra { font-size: 0.9em; margin: 10px auto 0; max-width: 1000px; line-height: 1.35; }
#u7-extra img { max-width: 100%; max-height: 60vh; }
#u7-fonte { font-size: 0.6em; color: #999; margin-top: 4px; }
"""


def _garantir_um(A, nome, campos, frente, verso, css, cloze, rotulo):
    if nome not in A("modelNames"):
        A("createModel", modelName=nome, inOrderFields=campos, css=css, isCloze=cloze,
          cardTemplates=[{"Name": rotulo, "Front": frente, "Back": verso}])
    atuais = A("modelFieldNames", modelName=nome)
    for c in campos:
        if c not in atuais:
            A("modelFieldAdd", modelName=nome, fieldName=c, index=len(A("modelFieldNames", modelName=nome)))
    if A("modelFieldNames", modelName=nome) != campos:
        raise SystemExit(f"{nome}: campos {A('modelFieldNames', modelName=nome)} != {campos}")
    t = A("modelTemplates", modelName=nome)
    nome_tpl = next(iter(t))
    if t[nome_tpl]["Front"] != frente or t[nome_tpl]["Back"] != verso:
        A("updateModelTemplates", model={"name": nome, "templates": {nome_tpl: {"Front": frente, "Back": verso}}})
    if A("modelStyling", modelName=nome)["css"] != css:
        A("updateModelStyling", model={"name": nome, "css": css})


def garantir(A):
    """Cria ou atualiza no lugar os dois tipos da UC07 (só a UC07 os usa)."""
    _garantir_um(A, NOME, CAMPOS, FRENTE, VERSO, CSS, False, "Estrutura")
    _garantir_um(A, CLOZE, CLOZE_CAMPOS, CLOZE_FRENTE, CLOZE_VERSO, CLOZE_CSS, True, "Cloze")
