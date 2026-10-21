"""Prova que os gates reprovam o caso ruim e nunca passam no vazio (MEMORY §15). Uso: python -m nebli.kenhub.teste_gates

Cada feedback de Davi (nebli/kenhub/feedbacks.json) precisa de: o gate existir no código e um caso ruim reprovado aqui.
"""
import json
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

from nebli.kenhub import deck, modelo, render

TAG = deck.TAG_KENHUB

RAIZ = Path(__file__).resolve().parents[2]


def _io(chave, nome, **meta):
    return {"chave": chave, "tipo": "netter", "modelo": modelo.NOME, "meta": {"seta": True, "guia": True, **meta},
            "campos": {"Nome PT": nome, "Nome EN": "Pons"}, "ocr_frente": []}


def main():
    falhas = []

    def espera(cond, msg):
        if not cond:
            falhas.append(msg)

    # registro: todo gate citado em feedbacks.json existe no código
    reg = json.loads((Path(__file__).parent / "feedbacks.json").read_text())
    for f in reg["feedbacks"]:
        for g in f["gates"]:
            espera(g["codigo"] in (RAIZ / g["arquivo"]).read_text(), f"{f['id']}: gate {g['codigo']!r} sumiu de {g['arquivo']}")
    cur = {"nome_igual_ok": []}
    # G8: nome com inglês ou com duas línguas reprova; nome em PT passa
    espera(any("G8" in p for p in deck.gates_pre([_io("a", "Pyramid of the medulla / Pirâmide do bulbo")], cur)), "G8 aceitou nome com duas línguas")
    espera(not any("G8" in p for p in deck.gates_pre([_io("b", "Pirâmide do bulbo")], cur)), "G8 reprovou nome correto")
    clz = {"chave": "c", "tipo": "acervo", "modelo": modelo.CLOZE, "campos": {"Text": "Qual estrutura? {{c1::Optic canal - Exit for CN II}}", "Imagens": "<img src=x>"}}
    espera(any("G8" in p for p in deck.gates_pre([clz], cur)), "G8 aceitou cloze longo em inglês")
    # G12: a frente que mostra o nome reprova
    e = _io("d", "Ponte")
    e["ocr_frente"] = ["Pons", "Medulla"]
    espera(any("G12" in p for p in deck.gates_pre([e], cur)), "G12 aceitou frente com a resposta")
    # G13: ponta da seta no fundo branco reprova
    espera(any("G13" in p for p in deck.gates_pre([_io("e", "Ponte", ponta_fundo=1.0)], cur)), "G13 aceitou seta no branco")
    with tempfile.TemporaryDirectory() as d:
        im = Image.new("RGB", (100, 100), "white")
        ImageDraw.Draw(im).rectangle((40, 40, 60, 60), fill=(150, 100, 80))
        im.save(Path(d) / "x.png")
        espera(deck._ponta_no_fundo(str(Path(d) / "x.png"), (50, 50)) < 0.1, "G13 errou a medida no tecido")
        espera(deck._ponta_no_fundo(str(Path(d) / "x.png"), (5, 5)) > 0.9, "G13 errou a medida no fundo")
        # G6: nunca passa no vazio
        f, _ = render.renderizar('"tag:NEBLI::nao-existe-xyz"', Path(d), [])
        espera(any("G6" in x for x in f), "G6 passou no vazio")
        f, _ = render.renderizar('"tag:NEBLI::nao-existe-xyz"', Path(d), [1, 2, 3])
        espera(any("G6" in x for x in f), "G6 passou com plano não vazio e nada renderizado")
    # F-05: Fonte preenchida reprova; máscara padrão AnKing é retângulo
    e = _io("f", "Ponte")
    e["campos"]["Fonte"] = "Kenhub"
    espera(any("G14" in p for p in deck.gates_pre([e], cur)), "G14 aceitou campo Fonte preenchido")
    from nebli.kenhub import mascara
    reg_ = np.zeros((400, 400), bool)
    reg_[100:120, 100:110] = True        # parte pequena → retângulo
    reg_[200, 300:340] = True            # linha fina (sulco) → retângulo
    m_, cx_, fm_ = mascara.retangulos(reg_, pad=1, area_min=5)
    espera(len(cx_) == 2 and not fm_.any() and m_[99:121, 99:111].all(), "máscara pequena não virou retângulo do padrão AnKing")
    grande_ = np.zeros((400, 400), bool)
    grande_[50:250, 50:250] = True       # lobo/cérebro (25% da figura) → forma, não retângulo que apaga o contexto
    _, cx2_, fm2_ = mascara.retangulos(grande_)
    espera(fm2_.any() and not cx2_, "estrutura grande virou retângulo e apagaria o contexto")
    # G17: máscara minúscula reprova; modelo genérico do AnatoKing reprova
    from PIL import Image as _I
    import tempfile as _t
    with _t.TemporaryDirectory() as dd:
        _I.new("RGB", (1000, 1000), "white").save(Path(dd) / "f.png")
        k = {"chave": "k", "tipo": "kenhub", "modelo": modelo.NOME, "base_frente": str(Path(dd) / "f.png"),
             "meta": {"seta": True, "ponta_na_mascara": True, "comprimento_seta": 5, "retangulos": 0, "formas": 0},
             "item": {"nome_en": "Pons"}, "slug": "pons", "campos": {"Nome PT": "Ponte", "Nome EN": "Pons"}, "ocr_frente": []}
        espera(any("G17" in p for p in deck.gates_pre([k], cur)), "G17 aceitou seta minúscula")
        k2 = dict(k, meta=dict(k["meta"], comprimento_seta=300, retangulos=2))
        espera(any("G21" in p for p in deck.gates_pre([k2], cur)), "G21 aceitou máscara (IO) sobre a estrutura do Kenhub")
    ac = {"chave": "a", "tipo": "acervo", "modelo": modelo.CLOZE, "pt": "Ponte", "usos_modelo": 17, "vermelho_modelo": 0.001,
          "campos": {"Text": "Qual estrutura? {{c1::Ponte}}", "Imagens": "<img src=x>", "Nome EN": "Pons"}, "ocr_frente": []}
    espera(any("genérica" in p for p in deck.gates_pre([ac], cur)), "gate de modelo genérico aceitou figura repetida em 17 cards")
    # F-20261018: AnatoKing com duas figuras; texto sem card; termo inventado × termo do Machado; revisão
    ac2 = dict(ac, usos_modelo=1, vermelho_modelo=0.01)
    ac2["campos"] = dict(ac["campos"], Imagens="<img src=x>", Extra="<img src=y>")
    espera(any("G20" in p for p in deck.gates_pre([ac2], cur)), "G20 aceitou AnatoKing com duas figuras")
    with tempfile.TemporaryDirectory() as dt:
        (Path(dt) / "itens.json").write_text(json.dumps({"texto": [{"chave": "txt:1", "tipo": "txt", "en": "x"}]}))
        espera(any("[cobertura-quiz]" in p for p in deck.gate_quiz_texto(Path(dt), [])), "cobertura do quiz aceitou trecho sem card")
        espera(not deck.gate_quiz_texto(Path(dt), [{"campos": {"a": 1}, "cobre_texto": ["txt:1"]}]), "cobertura do quiz reprovou trecho coberto")
        (Path(dt) / "itens.json").write_text(json.dumps({"itens": []}))
        espera(any("não coletado" in p for p in deck.gate_quiz_texto(Path(dt), [])), "cobertura do quiz passou sem texto coletado")
    from nebli.kenhub import glossario
    espera(glossario.atestado("bulbo-pontino") and glossario.atestado("fossa romboide"), "glossário recusou termo do Machado/Kenhub")
    espera(glossario.atestado("blorbo quadrigemoide") is None, "glossário aceitou termo inventado")
    espera("AGUARDANDO REVISÃO" in (RAIZ / "nebli/kenhub/painel.py").read_text() and "def revisado" in (RAIZ / "nebli/kenhub/pipeline.py").read_text(), "revisão card a card sumiu")
    # F-20261018-04: formatação AnKing, figura no cloze, sem regravar à toa
    tx = {"chave": "t", "tipo": "texto", "modelo": modelo.CLOZE, "campos": {"Text": "O nervo é {{c1::misto}}", "Imagens": "", "Extra": "<img src=x>", "Nome EN": ""}}
    espera(any("G22" in p for p in deck.gates_pre([tx], cur)), "G22 aceitou card sem negrito")
    tx2 = dict(tx, campos=dict(tx["campos"], Text="O <b>nervo</b> é {{c1::misto}}", Extra=""))
    espera(any("G23" in p for p in deck.gates_pre([tx2], cur)), "G23 aceitou card de texto sem figura")
    espera("<b>" in deck._formatar("A raiz anterior contém fibras {{c1::motoras}}", {}), "formatação AnKing não pôs negrito no sujeito")
    espera("sem regravar à toa" in (RAIZ / "nebli/kenhub/deck.py").read_text(), "gate de regravação sumiu")
    # F-20261018-05: estrutura junta, uma verde por estrutura, formato AnKing, figura grande
    sep = [{"ordem": 1, "estrutura": "a", "cor": "azul"}, {"ordem": 2, "estrutura": "b", "cor": "azul"}, {"ordem": 3, "estrutura": "a", "cor": "azul"}]
    espera(any("G25" in p for p in deck.gate_estruturas(sep)), "G25 aceitou cards da mesma estrutura espalhados")
    dois = [{"ordem": 1, "estrutura": "a", "cor": "verde", "chave": "x"}, {"ordem": 2, "estrutura": "a", "cor": "verde", "chave": "y"}]
    espera(any("G26" in p for p in deck.gate_estruturas(dois)), "G26 aceitou dois cards verdes da mesma estrutura")
    espera(not deck.gate_estruturas([dois[0], dict(dois[1], cor="azul")]), "G26 reprovou uma verde + uma azul")
    espera("G24 formato AnKing" in (RAIZ / "nebli/kenhub/modelo.py").read_text() and "ANKING_BASE" in (RAIZ / "nebli/kenhub/modelo.py").read_text(), "gate de formato AnKing sumiu")
    espera("960px" in (RAIZ / "nebli/kenhub/modelo.py").read_text().replace(" ", "") and "ESCALA = 2" in (RAIZ / "nebli/kenhub/mascara.py").read_text(), "figuras maiores/overlay nítido sumiram")
    # F-20261019-CODEX-01: fila na ordem oficial; nota ativa associa, totalmente suspensa migra
    from nebli.kenhub import painel
    espera(not painel.gate_ordem_kenhub([1, 2, 3]), "G29 reprovou sequência correta do Kenhub")
    espera(any("G29" in x for x in painel.gate_ordem_kenhub([1, 3, 2])), "G29 aceitou sequência fora da ordem do Kenhub")
    from nebli.kenhub.ordem_decks import nome_deck, plano_renomeacao
    primeiro = nome_deck("Introdução ao sistema nervoso", "Sistema nervoso central: introdução ao encéfalo", "basic-anatomy-of-the-brain")
    espera(primeiro == "NEBLI::UC07::01 Introdução ao sistema nervoso::01 Sistema nervoso central: introdução ao encéfalo",
           "G29 não põe Introdução em primeiro lugar na árvore do Anki")
    plano_nomes = plano_renomeacao()
    espera(len(plano_nomes) > 51 and len(set(plano_nomes.values())) == len(plano_nomes), "G29 plano de renomeação vazio/duplicado")
    espera(deck._destino_reuso([{"queue": 0}]) == "associar", "G30 tentou migrar nota ativa")
    espera(deck._destino_reuso([{"queue": -1}, {"queue": -1}]) == "migrar", "G30 associou nota totalmente suspensa")
    # F-20261020-CODEX-02: seleção ativa nunca passa vazia nem sem evidência.
    from nebli.kenhub import seleciona_estudo
    for ruim, msg in (({"notas": []}, "manifesto vazio passou"),
                      ({"notas": [{"nid": 1, "card_ids": [1], "selecionado": True}]}, "selecionado sem evidência passou")):
        try:
            seleciona_estudo.gate(ruim)
        except SystemExit:
            pass
        else:
            espera(False, msg)
    # F-20261018-05 (comentários): seta ruim do AnatoKing e termo sem explicação
    ac3 = dict(ac, usos_modelo=1, vermelho_modelo=0.01)
    espera(any("seta evidente" in p for p in deck.gates_pre([ac3], cur)), "AnatoKing sem seta_ok passou")
    espera(not any("seta evidente" in p for p in deck.gates_pre([dict(ac3, seta_ok=True)], cur)), "AnatoKing com seta_ok reprovou")
    tz = {"chave": "z", "tipo": "texto", "modelo": modelo.CLOZE, "campos": {"Text": "O giro é a área <b>somestésica</b> {{c1::primária}}", "Imagens": "", "Extra": "<img src=x>", "Nome EN": ""}}
    espera(any("G27" in p for p in deck.gates_pre([tz], cur)), "G27 aceitou termo técnico sem explicação")
    gz = {"chave": "g", "tipo": "texto", "modelo": modelo.CLOZE, "campos": {"Text": "Na figura, o grupo anterior aparece em {{c1::roxo}}", "Imagens": "", "Extra": "<img src=x>", "Nome EN": ""}}
    espera(any("G28" in x for x in deck.gates_pre([gz], cur)), "G28 aceitou card que pergunta a cor da figura")
    # entrada sem campos (tipo desconhecido) reprova
    espera(any("[montagem]" in p for p in deck.gates_pre([{"chave": "z", "tipo": "id"}], cur)), "entrada sem campos passou")
    # seta em estrutura fina e curva (centroide fora dela): o planejador não pode desistir (unidade IX, ramo lingual)
    from nebli.kenhub import mascara
    fina = np.zeros((600, 600), dtype=bool)
    for t in np.linspace(0, np.pi, 900):
        y, x = int(300 + 220 * np.sin(t)), int(300 - 220 * np.cos(t))
        fina[y:y + 3, x:x + 3] = True
    try:
        mascara.planejar_seta(fina, (180, 40))
    except ValueError:
        espera(False, "planejar_seta desistiu de uma estrutura fina e curva")
    # F-03: navegador do Kenhub invisível
    espera("headless=True" in (RAIZ / "nebli/kenhub/navegador.py").read_text(), "navegador do Kenhub voltou a abrir janela")
    if falhas:
        print("TESTE DOS GATES REPROVADO:", *falhas, sep="\n  ")
        raise SystemExit(1)
    print(f"teste dos gates ok: {len(reg['feedbacks'])} feedbacks com gate no código e caso ruim reprovado")


if __name__ == "__main__":
    main()
