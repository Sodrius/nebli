# Especificação IM37 — reconstruída a partir de material docente lido e inventário antes da seleção.
# Verde = mecanismo a manter; azul = essencial para a prova desta aula; rosa = detalhe útil para a prova.
from copy import deepcopy
import runpy
_old = runpy.run_path('/Users/davisousa/NEBLI/arquivos-trabalho/deck-aula-uc03-imuno-p2-2026-09-30/inflamacao/spec-revisada.py')
RUN_ID = "uc03-im37-20261011-codex"
SHORT = "imuno37r"
LESSON = "2026-uc03-imunologia-37-inflamacao-inicio-resolucao"
DECK = "NEBLI::UC03::P2::Imunologia::Inflamação: início e resolução"
CRITERIOS = "MEMORY.md + FEEDBACKS até 11/10/2026; seleção recalibrada para revisão longitudinal"
MEDIA = deepcopy(_old.get("MEDIA", {}))
BUSCA = _old.get("BUSCA", "Acervo AnKing e referências externas documentados na corrida anterior; seleção refeita após releitura do material docente.")
EXCLUIDOS = [(1487116849895, 'coestimulação B7–CD28: conteúdo de ativação de T, não ensinado como alvo desta aula'), (1487117308213, 'citotoxicidade por NK: desvio do recorte de inflamação'), (1497451553581, 'iNOS induzível por IFN-γ: detalhe não sustentado como objetivo da aula'), (1475966862515, 'receptor scavenger de LDL oxidada: aterogênese fora do recorte')]
FORA_DO_RECORTE = ["Ativação de linfócitos T (B7–CD28)", "citotoxicidade de NK", "iNOS/IFN-γ como tópico isolado", "aterogênese por LDL oxidada"]
FLAGS = {'ak-1487640028986': {1: 4, 2: 4, 3: 5}, 'ak-1487640050564': {1: 3}, 'ak-1500572039288': {2: 4, 3: 4}, 'ak-1520715624658': {1: 3}, 'ak-1520715849479': {1: 3}, 'ak-1487640248028': {1: 4}, 'ak-1487640253946': {1: 4}, 'ak-1487640263698': {1: 4}, 'ak-1487640274492': {1: 4}, 'ak-1520443529180': {1: 5}, 'ak-1487640261037': {1: 3, 2: 4, 3: 4}, 'ak-1487640269487': {1: 3, 2: 4, 3: 5}, 'ak-1479267395454': {1: 4}, 'ak-1487207084334': {1: 4, 2: 5}, 'ak-1487207091819': {2: 5}, 'ak-1487640132837': {1: 5}, 'ak-1487640136892': {1: 5}, 'ak-1487642579270': {1: 4, 2: 5}, 'ak-1487642582069': {1: 5}, 'ak-1487642620769': {1: 4, 2: 4}, 'ak-1487642625895': {1: 4, 2: 4}, 'ak-1487642632527': {1: 4}, 'ak-1487642637710': {1: 4}, 'ak-1475890914685': {1: 3}, 'ak-1487642733736': {1: 3, 2: 4}, 'ak-1487640225601': {1: 4}, 'ak-1487640230861': {1: 4, 2: 4}, 'ak-1487640059152': {1: 3, 2: 3}, 'ak-1487640061733': {1: 3}, 'ak-1487640068745': {1: 4}, 'ak-1487640078840': {1: 3}, 'ak-1487640089158': {1: 4, 2: 5}, 'ak-1487640101055': {1: 3}, 'ak-1487640108934': {1: 4}, 'ak-1488847671701': {1: 4, 2: 4}, 'ak-1488847679422': {1: 4}, 'ak-1488854922125': {1: 5}, 'ak-1488854930174': {1: 5}, 'ak-1488847688890': {1: 3}, 'ak-1488847696894': {1: 5}, 'ak-1473986398130': {1: 3, 2: 4}, 'ak-1463883753623': {1: 3}, 'ak-1462061188088': {1: 5}, 'ak-1474580819655': {1: 5}, 'ak-1487640278577': {1: 3, 2: 3}, 'ak-1489969950421': {1: 3}, 'ak-1489970026548': {1: 3}, 'ak-1489970181312': {1: 3}, 'ak-1487642795725': {1: 3}, 'ak-1520444046369': {1: 3, 2: 4}, 'ak-1520445108362': {1: 4}, 'ak-1520445157941': {1: 5}, 'ak-1520444298927': {1: 5}, 'ak-1487642784485': {1: 3}, 'ak-1520715124462': {1: 3, 2: 3}, 'ak-1520716108281': {1: 4, 2: 5}, 'ak-1520717070355': {1: 4, 2: 5}, 'ak-1479267468509': {1: 3}, 'tlr-endossomais': {1: 4, 2: 5}, 'nod-rig': {1: 5, 2: 5}, 'dectina': {1: 5}, 'damps': {1: 3}, 'urato-nlrp3': {1: 3}, 'gota-il1': {1: 5}, 'sequencia-vascular': {1: 3, 2: 3}, 'cinetica-celular': {1: 4}, 'eotaxina': {1: 5}, 'nets': {1: 4}, 'neuropeptideos': {1: 5, 2: 5}, 'cinetica-mediadores': {1: 4, 2: 5}, 'lipoxinas-resolvinas': {1: 3, 2: 4}, 'eferocitose': {1: 3}, 'ak-1554063916591': {1: 5, 2: 5}, 'ak-1554064102112': {1: 5, 2: 5}, 'ak-1554064278093': {1: 5, 2: 5}}
COMPARTILHADAS = {
 1500572039288: ("azul", "A-reconhecimento", "TLR4/CD14 e LPS", "Slide 18"),
 1487640136892: ("rosa", "B-celulas-vasos", "ativação de mastócito por IgE", "Slide 32"),
 1487640108934: ("azul", "E-mediadores", "leucotrienos e permeabilidade", "Slide 55"),
 1520716108281: ("azul", "G-resolucao", "polarização M1", "Slide 65"),
 1520717070355: ("azul", "G-resolucao", "polarização M2", "Slide 65"),
 1479267468509: ("verde", "G-resolucao", "ponte inata–adaptativa por DC", "Slide 66"),
}
REVISOES_CEGAS = {
 "ak-1487640068745": {"text":"A prostaglandina mais associada à vasodilatação na inflamação é {{c1::PGE2}}.", "flags":{1:4},
                       "extra":"PGI₂ e PGD₂ também contribuem para vasodilatação; este card recupera o mediador central sem transformar uma lista em uma resposta."},
 "cinetica-celular": {"text":"Após a onda inicial de neutrófilos, {{c1::monócitos}} tornam-se mais proeminentes em cerca de 1–2 dias e diferenciam-se em macrófagos.", "flags":{1:4}},
 "ak-1520715124462": {"text":"IL-10 e TGF-β {{c1::favorecem a resolução}} da inflamação aguda.", "flags":{1:3}},
 "ak-1487640050564": {"text":"A ativação de TLRs ativa {{c1::NF-κB}}, que transloca ao núcleo e induz genes inflamatórios.", "flags":{1:3}},
 "eotaxina": {"text":"{{c1::Eotaxina}} recruta preferencialmente eosinófilos.", "flags":{1:5},
              "extra":"IL-8 e LTB₄ são quimioatraentes importantes de neutrófilos; separar essas associações evita uma lista de três respostas no mesmo card."},
 "ak-1487207084334": {"text":"A resposta imediata dos mastócitos libera {{c1::histamina pré-formada}} e {{c2::triptase}}.", "flags":{1:4,2:5}},
 "ak-1487640101055": {"text":"{{c1::Arachidonic acid}} is converted to leukotrienes via {{c2::5-lipoxygenase}}.", "flags":{1:3,2:3}},
 "ak-1479267395454": {"text":"Macrophages phagocytose bacteria, cellular debris, and {{c1::senescent RBCs}}.", "flags":{1:4}},
 "gota-il1": {"text":"Blocking {{c1::IL-1β}} can suppress crystal-driven inflammation in gout downstream of NLRP3 activation.", "flags":{1:5}},
}
AUTORES_ESPELHOS = {
 "tlr-endossomais":[1487640050564,1500572039288], "nod-rig":[1520715624658,1520715849479],
 "dectina":[1487640028986,1500572039288], "damps":[1520715624658,1520715849479],
 "urato-nlrp3":[1520715624658,1520715849479], "gota-il1":[1520715849479,1487640078840],
 "sequencia-vascular":[1487640261037,1487640269487], "cinetica-celular":[1487640278577,1520444046369],
 "eotaxina":[1487642795725,1487207091819], "nets":[1475890914685,1487642733736],
 "neuropeptideos":[1487640261037,1487640269487], "cinetica-mediadores":[1487207084334,1487640059152],
 "lipoxinas-resolvinas":[1487642784485,1520715124462], "eferocitose":[1487642784485,1520715124462],
}
REMOVIDAS = {"ak-1487207091819":"redundante após separar eotaxina em card autoral atômico", 'ak-1487116849895': 'coestimulação B7–CD28: conteúdo de ativação de T, não ensinado como alvo desta aula', 'ak-1487117308213': 'citotoxicidade por NK: desvio do recorte de inflamação', 'ak-1497451553581': 'iNOS induzível por IFN-γ: detalhe não sustentado como objetivo da aula', 'ak-1475966862515': 'receptor scavenger de LDL oxidada: aterogênese fora do recorte'}
CARDS = []
for _card in deepcopy(_old["CARDS"]):
    _k = _card["key"]
    if _k in REMOVIDAS:
        continue
    if _k not in FLAGS:
        raise RuntimeError(f"Decisão de bandeira ausente: {_k}")
    _card["flags"] = FLAGS[_k]
    _slide = {"A-reconhecimento":15,"B-celulas-vasos":27,"C-migracao":37,"D-efetores":45,"E-mediadores":50,"F-sistemico":60,"G-resolucao":64}[_card["bloco"]]
    _card["evid"] = f"Slide {_slide}"
    if _card.get("src") in COMPARTILHADAS:
        _cor,_bloco,_alvo,_evid = COMPARTILHADAS[_card["src"]]
        CARDS.append(dict(key=f"sh-{{_card['src']}}", kind="compartilhado", nid=_card["src"], cor=_cor, bloco=_bloco, alvo=_alvo, evid=_evid, motivo="Já associado a outra aula; reutilizado sem duplicar nota."))
        continue
    if _card["kind"] == "autoral":
        _card["espelhos"] = AUTORES_ESPELHOS[_k]
    # HY no acervo é sinal de utilidade, não ordem automática de retenção vitalícia.
    # Estes detalhes já estão cobertos por mecanismos verdes da mesma sequência.
    if _card.get("src") in {1479267395454,1487207084334,1487207091819,1487642625895,1487642632527,1487642637710,1487640230861,1487640089158,1488847671701,1488847679422,1488854922125,1488854930174,1488847696894,1462061188088,1474580819655,1520445108362,1520445157941,1520444298927}:
        _card["clinica_lateral"] = True
    if _k in REVISOES_CEGAS:
        _card.update(REVISOES_CEGAS[_k])
    if _k == "ak-1473986398130":
        _card["flags"] = {1:3,2:4,3:4}
    if _k == "ak-1462061188088":
        _card["flags"] = {1:5,2:5}
    if _card.get("hy") in ("1","2") and 3 not in _card["flags"].values():
        _card["clinica_lateral"] = True
    _card["motivo"] = ("Verde: mecanismo transversal, cuja perda compromete imunidade, patologia e farmacologia posteriores."
                       if 3 in _card["flags"].values() else
                       "Azul: necessário para a prova e para acompanhar esta aula, com menor valor de retenção longitudinal."
                       if 4 in _card["flags"].values() else
                       "Rosa: detalhe de prova contextual, deliberadamente fora da revisão de longo prazo.")
    CARDS.append(_card)
VERSO = deepcopy(_old.get("VERSO", {}))
DUPLICACAO = deepcopy(_old.get("DUPLICACAO", {}))
# O verso só complementa; a fonte de imagem não aparece no card.
for c in CARDS:
    k=c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"]=(c.get("extra","")+"<br>" if c.get("extra") else "")+VERSO[k]
        else:
            c["extra_add"]=VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"]=DUPLICACAO[k]
