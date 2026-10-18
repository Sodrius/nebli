"""Tipos de nota da UC07 (só usados por ela; podem ser atualizados no lugar sem afetar outras notas de Davi).

NEBLI Kenhub IO v1 — IO padrão AnKing com seta (Kenhub, Netter, AnKing com “ID”, níveis do tronco):
  frente: só a figura com o retângulo vermelho sobre a estrutura e a seta (sem frase; Pergunta só quando a figura inteira
  é a pergunta, nos níveis do tronco); verso: a figura com o nome em PT na ponta da seta — sem nome em cima quando há seta
  (F-20261017-CLAUDE-05). Fonte nunca aparece no card (proveniência só nos campos/etiquetas).
NEBLI UC07 Cloze v1 — cloze em português com o nome só (AnatoKing e AnKing conceitual), todas as imagens à vista, sem botões
  de escolher entre cadáver e modelo (F-20261017-CLAUDE-04). Ambos têm NEBLI_Comentario (Davi comenta em todo card).
"""

NOME = "NEBLI Kenhub IO v1"
CAMPOS = ["Nome PT", "Latim", "Nome EN", "Sinonimos", "Imagem", "MascaraP", "Fonte", "Extra", "ID (hidden)", "NEBLI_Comentario",
          "MascaraR", "Pergunta"]

FRENTE = """{{#Imagem}}
{{#Pergunta}}<div id="kh-topo"><div id="kh-perg">{{Pergunta}}</div></div>{{/Pergunta}}
<div id="kh-wrap">
  <div id="kh-img">{{Imagem}}</div>
  <div class="kh-over">{{MascaraP}}</div>
</div>
{{/Imagem}}"""

VERSO = """{{#Pergunta}}<div id="kh-topo"><div id="kh-nome">{{Nome PT}}</div></div>{{/Pergunta}}
<div id="kh-wrap">
  <div id="kh-img">{{Imagem}}</div>
  <div class="kh-over">{{MascaraR}}</div>
</div>
{{#Extra}}<div id="kh-extra">{{Extra}}</div>{{/Extra}}"""

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
/* tamanho adequado (F-20261017-CLAUDE-05): nem gigante em tela grande, nem miúda — até 960 px de altura (F-20261018-CLAUDE-05: um pouco maiores), cabe sem rolar */
#kh-img img { display: block; max-width: 100%; max-height: min(calc(100vh - 56px), 960px); width: auto; height: auto; }
/* cards com pergunta no topo (níveis do tronco): desconta os 64 px do topo para a figura caber sem rolar */
#kh-topo + #kh-wrap #kh-img img { max-height: min(calc(100vh - 124px), 960px); }
.kh-over { position: absolute; top: 0; left: 0; right: 0; bottom: 0; }
.kh-over img { width: 100%; height: 100%; }
#kh-extra { font-size: 0.85em; margin: 8px auto 0; max-width: 900px; text-align: left; line-height: 1.35; }
#kh-extra img { max-width: 100%; max-height: 60vh; }
.mobile #kh-nome { font-size: 1.3em; }
"""

# Cards que não são primariamente de imagem: o MESMO tipo de nota que o NEBLI já usa para o AnKing (clone fiel de
# “NEBLI AnKing independente - v3”, que é o AnKingOverhaul): fonte, fundo, cor do cloze, Extra… tudo AnKing (F-20261018-CLAUDE-05)
ANKING_BASE = "NEBLI AnKing independente - v3"
CLOZE = "NEBLI UC07 AnKing v1"
CLOZE_CAMPOS = ["Text", "Extra", "Lecture Notes", "Missed Questions", "Pathoma", "Boards and Beyond", "First Aid", "Sketchy", "Sketchy 2",
                "Sketchy Extra", "Picmonic", "Pixorize", "Physeo", "Bootcamp", "OME", "Additional Resources", "One by one",
                "NEBLI_Comentario", "NEBLI_Resposta", "ankihub_id"]
CSS_UC07 = """
/* UC07 (F-20261018-CLAUDE-05): figuras do Text e do Extra um pouco maiores; o resto é o AnKing sem alteração */
#text img { max-width: 100%; max-height: min(78vh, 780px); width: auto; height: auto; }
/* figura do Extra (resposta): cabe na tela junto com o texto, sem rolar (infográficos altos, como o da cauda equina) */
#extra img { max-width: 100%; max-height: max(360px, calc(100vh - 280px)); width: auto; height: auto; }
"""


def conferir_formato(A):
    """[G24 formato AnKing] o tipo dos cards de texto tem os modelos de cartão e o CSS do AnKing, sem alteração (só o bloco UC07 no fim)."""
    if ANKING_BASE not in A("modelNames") or CLOZE not in A("modelNames"):
        return []   # ainda não existe: garantir() cria o clone fiel
    p = []
    a, b = A("modelTemplates", modelName=ANKING_BASE), A("modelTemplates", modelName=CLOZE)
    fa, fb = next(iter(a.values())), next(iter(b.values()))
    if (fa["Front"], fa["Back"]) != (fb["Front"], fb["Back"]):
        p.append("[G24 formato AnKing] modelos de cartão do tipo UC07 diferem do AnKing")
    ca, cb = A("modelStyling", modelName=ANKING_BASE)["css"], A("modelStyling", modelName=CLOZE)["css"]
    if cb != ca + CSS_UC07:
        p.append("[G24 formato AnKing] CSS do tipo UC07 difere do AnKing (só o bloco UC07 no fim é permitido)")
    if A("modelFieldNames", modelName=CLOZE) != A("modelFieldNames", modelName=ANKING_BASE):
        p.append("[G24 formato AnKing] campos do tipo UC07 diferem do AnKing")
    return p


def _clonar_anking(A):
    campos = A("modelFieldNames", modelName=ANKING_BASE)
    tpl = next(iter(A("modelTemplates", modelName=ANKING_BASE).items()))
    css = A("modelStyling", modelName=ANKING_BASE)["css"] + CSS_UC07
    if CLOZE not in A("modelNames"):
        A("createModel", modelName=CLOZE, inOrderFields=campos, css=css, isCloze=True,
          cardTemplates=[{"Name": tpl[0], "Front": tpl[1]["Front"], "Back": tpl[1]["Back"]}])
    else:
        t = next(iter(A("modelTemplates", modelName=CLOZE).items()))
        if (t[1]["Front"], t[1]["Back"]) != (tpl[1]["Front"], tpl[1]["Back"]):
            A("updateModelTemplates", model={"name": CLOZE, "templates": {t[0]: {"Front": tpl[1]["Front"], "Back": tpl[1]["Back"]}}})
        if A("modelStyling", modelName=CLOZE)["css"] != css:
            A("updateModelStyling", model={"name": CLOZE, "css": css})
    return campos


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
    global CLOZE_CAMPOS
    CLOZE_CAMPOS = _clonar_anking(A)
