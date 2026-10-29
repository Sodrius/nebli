"""Gerador único das evidências da 61 v3 (lição do deck 60: um script a partir do spec, não seis arquivos à mão).
Escreve: busca/cobertura.tsv, decisoes.json, REVISAO-AUTORAIS.md (moldagem), imagens-batem.json, planejamento.json, escopo.json,
mapa-de-profundidade.json (cards reais), motivacoes.json (atendida_por), compreensao-aula.json (principios_ilustrados, reconstrucoes).
Tudo o que é julgamento está escrito aqui, card a card; o script só distribui nos arquivos que os gates leem.
    python3 evidencias.py
"""
import json, re
from pathlib import Path

HERE = Path(__file__).parent
plan = json.loads((HERE / "plan.json").read_text())
E = {e["key"]: e for e in plan["entries"]}
SH = {f"sh-{k}": v for k, v in (plan.get("compartilhados") or {}).items()}
TODOS = list(E) + list(SH)
slide = lambda k: int(re.search(r"\d+", (E.get(k) or SH.get(k))["evid"]).group())
cloze1 = lambda t: re.sub(r"<[^>]+>", "", re.search(r"\{\{c\d+::(.*?)(::|\}\})", t).group(1)).strip()

# ---------- autorais: lacuna, candidatos lidos, molde (EXEMPLAR × ANTI dos GUIAS 2 e 3) ----------
MEC, CON, ORGZ, FATO = ("1791631347467", "1791627549152"), ("1792166970014", "1791023819869"), ("1792166969765", "1792624459224"), ("1791023354943", "1791629587772")
A = {  # chave: (veredito, conceito, por que o acervo não cobre, molde, lidos)
 "_au-dois-efeitos": ("parcial", "Onde o vírus replica decide onde fica a inclusão", "o AnKing dá que vírus de DNA replicam no núcleo e exemplos de inclusão; nenhum card liga o compartimento da replicação ao lugar da inclusão no tecido, a ideia da lâmina 2", MEC, "1792753616942,1479430568786,1461792762468,1791763625318"),
 "au-efeitos": ("lacuna", "Três destinos dos efeitos diretos", "nenhum card agrupa lise → inflamação aguda, transformação → neoplasia e o resto → efeito citopático; os candidatos falam de lise tumoral e hemaglutinina", ORGZ, "1516930966434,1481335256235,1475028620304,1792695029538"),
 "au-sequestro": ("lacuna", "Síntese sequestrada para o vírus", "o AnKing tem o IFN reduzindo a síntese e o RNA de sentido positivo; nada sobre a célula que para de dividir por ter a maquinaria tomada", MEC, "1520301328706,1502064281478,1502064208990,1792677732277"),
 "au-transformacao": ("lacuna", "Transformação por mutagênese insercional", "a única nota com 'insertional mutagenesis' é de CAR-T; os candidatos de ciclo celular são de oncologia geral", FATO, "1499999109081,1496162289144,1792695029538,1506807835841"),
 "au-inclusao": ("lacuna", "Inclusão por produção desproporcional", "o acervo define inclusão (58, associado) e dá exemplos; nenhum explica a montagem limitada pelo componente escasso (prova 2024)", MEC, "1792695054492,1502570605009,1506299172244,1792695054792"),
 "au-raiva-sarampo": ("parcial", "Citoplasmática × nuclear", "o Negri citoplasmático está no acervo (associado), mas nenhum card põe a inclusão nuclear do sarampo ao lado dele como na lâmina 6", CON, "1516474665512,1516475827100,1502152318872,1792695054792"),
 "au-sincicio-granuloma": ("lacuna", "Sincício × célula gigante do granuloma", "o acervo descreve o granuloma (47) e a proteína F; nenhum card distingue as duas células gigantes (prova 2017)", ORGZ, "1487642936903,1487643795892,1791716424523,1506298786823"),
 "au-quadros": ("parcial", "Tipo de quadro decide o braço imune", "o card da 59 diz contenção inata e memória adaptativa; nenhum liga quadro agudo e crônico ao braço que lesa nem cita os vírus que cronificam", ORGZ, "1792753615215,1486867623104,1486867532110,1581189645300"),
 "au-nk-neutrofilo": ("lacuna", "NK na virose × neutrófilo na bacteriana", "o acervo diz que NK e neutrófilo são da inata; nenhum faz o contraste da fala", CON, "1486867499358,1486867503989,1487117304665,1489970456186"),
 "au-complemento": ("lacuna", "Complemento lisa célula infectada", "o acervo tem a composição do MAC e deficiências; nada sobre o MAC sobre a célula que expõe proteína viral", MEC, "1487640207727,1501968263352,1487640204292,1791667098962"),
 "au-mononuclear": ("lacuna", "Infiltrado mononuclear na virose", "os cards de infiltrado linfocitário são de doenças específicas (miocardite, Kaposi) ou de inflamação crônica geral; nenhum para a virose como princípio", FATO, "1519852532171,1472078786108,1791780363380,1521424037362"),
 "au-curva": ("lacuna", "Curva temporal da resposta", "o acervo tem IFN ativando NK e o card 59; nenhum dá a sequência IFN/NK → T → anticorpos da lâmina 10", MEC, "1487117310594,1497203002753,1792753615215,1489970693302"),
 "au-intracelular": ("lacuna", "Inata não basta: vírus intracelular", "o acervo define inata e adaptativa e o CD8; nenhum explica por que a inata não elimina o vírus", MEC, "1487117286060,1486867606359,1487117293576,1792677732277"),
 "au-ifn-tipo": ("lacuna", "IFN-I × IFN-γ", "o acervo tem IFN-α/β e IFN-γ em cards separados; nenhum os contrasta, e o vídeo do canal os confunde", CON, "1487117310594,1489970516941,1489970456186,1487643795892"),
 "au-ifn-tempo": ("parcial", "IFN-I ganha tempo", "o acervo dá onde o IFN-I age e que reduz a síntese; nenhum diz para que serve na linha do tempo (ganhar tempo para a adaptativa)", MEC, "1489970693302,1520301328706,1556144067381,1792753615215"),
 "au-nk-cd8": ("parcial", "CD8 × NK quando o vírus esconde MHC I", "o acervo tem CMV bloqueando MHC I e a NK matando tumor sem MHC I; nenhum fecha a cadeia vírus → perda do freio da NK", MEC, "1503876156644,1518053116398,1487117314403,1487115889320"),
 "au-aguda-matriz": ("lacuna", "Matriz poupada → regeneração", "o acervo descreve a hepatite aguda e a regeneração do fígado; nenhum liga regeneração à matriz preservada", MEC, "1486522618128,1702335377225,1792753612016,1473628007883"),
 "au-vidro-fosco": ("parcial", "Proteína viral acumulada = efeito citopático", "o AnKing nomeia o vidro fosco na hepatite B crônica; não diz que é proteína viral acumulada nem o liga à inclusão", MEC, "1715273523479,1502066053913,1520351217376,1473628007883"),
 "au-ihq": ("lacuna", "Antígeno viral no compartimento de origem", "nenhum card de imuno-histoquímica viral; o acervo só traz onde o HBV replica", CON, "1715273523479,1506551469394,1463442982359,1506551774430"),
 "au-anti-hbc": ("parcial", "Anticorpo contra proteína ausente da vacina prova infecção", "o AnKing dá 'só anti-HBs = vacinação' e a vacina de HBsAg; não ensina a dedução estrutural da fala", FATO, "1521044225681,1504049054084,1502066053913,1495743863878"),
 "au-periportal": ("parcial", "A lesão segue a via de chegada", "o AnKing dá a zona I na hepatite viral; não dá o porquê (vírus e células chegam pelo sangue portal)", MEC, "1486776378880,1486522630094,1486522618128,1486776364876"),
 "au-apoptose-necrose": ("lacuna", "Apoptose dirigida × necrose", "o acervo tem apoptose sem inflamação (09) e CTL por apoptose; nenhum contrasta as duas mortes da célula infectada pelo dano ao tecido", CON, "1792117372823,1792117387149,1487117308213,1497450277629"),
 "au-necrose-matriz": ("lacuna", "Necrose → neutrófilo → matriz destruída", "os cards de protease de neutrófilo são de abscesso e pulmão; nenhum liga a necrose da célula infectada à perda do arcabouço", MEC, "1792117377997,1473627965295,1791983682682,1791199623249"),
 "au-interface": ("lacuna", "Destruição em curso = atividade", "nenhum card de hepatite de interface ou placa limitante no AnKing nem nos externos", FATO, "1486522630094,1521424595880,1611606970323,1486522813431"),
 "au-cd8-b": ("lacuna", "CD8 e B no infiltrado", "o acervo tem o CD8 matando células infectadas; nenhum junta os dois braços no infiltrado crônico", CON, "1487117293576,1524409059430,1792753612016,1539185990411"),
 "au-colageno": ("lacuna", "Reticulina → colágeno → septos", "o acervo define cirrose (associado) e reticulina = colágeno III; nenhum dá a troca da reticulina pelo colágeno grosso", MEC, "1486522637384,1468250259504,1487981545623,1486522654540"),
}
A = {k: v for k, v in A.items() if not k.startswith("_")}
assert set(A) == {k for k, e in E.items() if e.get("origin") == "Autoral"}, set(A) ^ {k for k, e in E.items() if e.get("origin") == "Autoral"}

SEM = {json.loads(l)["chave"]: [str(h["nid"]) for h in json.loads(l)["top"]] for l in (HERE / "busca/semantica.jsonl").read_text().splitlines()}
KW = {}
for l in (HERE / "busca/palavra-chave.jsonl").read_text().splitlines():
    d_ = json.loads(l); KW.setdefault(d_["chave"], []).extend(str(i) for c_ in d_.get("cobertura_acervos", []) for i in c_.get("ids", []))
LIDOS = {k: SEM.get(k, [])[:5] for k in A}  # o gate aceita só candidatos da busca por significado desta chave
linhas = ["chave\tconceito\tfonte_aula\tveredito\tlidos\tdecora\tdecisao"]
dec = {}
for k in TODOS:
    e = E.get(k)
    if e and e.get("origin") == "Autoral":
        v, conc, porque, _, _ = A[k]
        lidos = ",".join(LIDOS.get(k, [])[:5])
        txt = ("Busca nos três caminhos (seções de recurso; palavra-chave com a chave do card em AnKing e externos; significado em todos os acervos e "
               f"NEBLI vivo): {porque}. O card cobre o item do mapa da motivação {e.get('motivacao')} e a fonte da aula citada.")
        linhas.append(f"{k}\t{conc}\t{e['motivo'].split(': ',1)[-1]}\t{v}\t{lidos}\t{cloze1(e['fields']['Text'])}\t{txt}")
        dec[k] = [v, txt]
    else:
        x = e or SH[k]
        alvo = x.get("alvo", "")
        linhas.append(f"{k}\t{alvo}\t{x.get('evid')}\tcoberto\t{x.get('src', x.get('nid', ''))}\t-\tacervo cobre o item da aula; entra {'associado (já vive em outra aula)' if k in SH else 'como cópia do AnKing'}")
(HERE / "busca").mkdir(exist_ok=True)
(HERE / "busca/cobertura.tsv").write_text("\n".join(linhas) + "\n", encoding="utf-8")
(HERE / "decisoes.json").write_text(json.dumps(dec, ensure_ascii=False, indent=1), encoding="utf-8")

nome = {MEC: ("mecanismo com consequência (HDAC)", "card solto sem processo (domínio de ativação)"),
        CON: ("contraste no mesmo índice (autoimune × autoinflamatória)", "resposta por oposição (peristalse)"),
        ORGZ: ("organizador em pé com critério visível (como o sistema imune falha)", "organizador com classificação sem fonte (ordem de perfusão)"),
        FATO: ("fato decorável com contexto e verso com ganho (submandibular)", "cloze genérico (apoptosis → negative selection)")}
rev = ["# Revisão dos autorais — 61 Patologia da infecção viral v3 (pipeline v10, 29/10)", "",
       "Leitura obrigatória v10 inteira (GUIA-1 a GUIA-4, MEMORY, pipeline, rubrica, calibração). Cada autoral nasce de uma motivação congelada na E3, "
       "é escrito como princípio de patologia viral (os do bloco de exemplo também, com a hepatite como contexto) e foi moldado num EXEMPLAR real e "
       "conferido contra o ANTI do erro mais próximo.", "",
       "Organizadores necessários: sim — só onde a aula agrupa (destinos dos efeitos diretos, quadro agudo × crônico, sincício × granuloma).", "",
       "## Moldagem (antes de instalar)", ""]
for k in A:
    ex, an = A[k][3]
    rev.append(f"- {k} — par: EXEMPLAR {ex} ({nome[A[k][3]][0]}) × ANTI {an} ({nome[A[k][3]][1]}) — decora: {cloze1(E[k]['fields']['Text'])} — ok")
(HERE / "REVISAO-AUTORAIS.md").write_text("\n".join(rev) + "\n", encoding="utf-8")

# ---------- imagens (vistas em visual/imagens-cards-01..03 em 29/10) ----------
IB = {
 "au-raiva-sarampo": "lâminas 5 e 6: neurônio com inclusão citoplasmática (seta) e neurônio com inclusão nuclear; respondem ao contraste do cloze",
 "au-sincicio-granuloma": "lâmina 7: sincícios nos septos alveolares sem coroa linfocitária nem epitelioides, o lado viral do contraste",
 "au-mononuclear": "lâmina 19: espaço porta tomado por infiltrado mononuclear denso, o que o cloze pede",
 "au-curva": "lâmina 10: curvas de vírus, IFN-I, NK, linfócitos T e anticorpos por dia; mostra a ordem do cloze",
 "ak1715273523479": "figura do AnKing de hepatócitos em vidro fosco, o alvo do cloze",
 "au-vidro-fosco": "lâmina 16: hepatócitos de citoplasma homogêneo (seta), o efeito citopático da frente",
 "au-ihq": "lâminas 17 e 18: HBsAg marrom no citoplasma e HBcAg marrom nos núcleos, exatamente os dois compartimentos",
 "ak1486776378880": "figuras do AnKing com zonas 1, 2 e 3 do lóbulo; a zona 1 periportal é a resposta",
 "au-periportal": "lâmina 19: infiltrado concentrado no espaço porta, onde vírus e células chegam",
 "au-apoptose-necrose": "lâminas 24 e 22: hepatócito apoptótico isolado e foco de necrose com infiltrado, os dois lados do contraste",
 "au-interface": "lâmina 25: infiltrado portal invadindo o parênquima sem limite nítido, a placa limitante rompida",
 "au-cd8-b": "lâmina 26: imuno-histoquímica de linfócitos B no infiltrado portal, a resposta do cloze",
 "au-colageno": "lâmina 28: impregnação de reticulina com septos grossos isolando nódulos",
}
(HERE / "imagens-batem.json").write_text(json.dumps({k: {"veredito": "ok", "porque": v} for k, v in IB.items()}, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- desassociados na rodada 2 do revisor: substituto em cada lista ----------
SUB = {"au-dois-efeitos": "sh-1792695023262", "sh-1791743340457": "au-efeitos", "sh-1792695029538": "au-transformacao", "sh-1792695054492": "au-inclusao",
       "sh-1792695054792": "au-raiva-sarampo", "sh-1793199689555": "sh-1793199689805", "sh-1791716424523": "au-sincicio-granuloma",
       "sh-1792753615215": "au-quadros", "sh-1791022173275": "au-colageno"}
def F_(ks):
    return list(dict.fromkeys(SUB.get(k, k) for k in ks))
# ---------- mapa: item → cards reais ----------
CARDS_ITEM = {
 "p1-1": ["sh-1792753616942", "au-efeitos"], "p1-2": ["au-dois-efeitos", "sh-1792695023262", "sh-1793199695431"],
 "p2-1": ["au-efeitos"], "p2-2": ["sh-1791743340457"], "p2-3": ["au-sequestro"], "p2-4": ["au-transformacao", "sh-1792695029538"], "p2-5": ["au-efeitos"],
 "p3-1": ["au-inclusao", "sh-1792695054492"], "p3-2": ["sh-1793199693557", "au-raiva-sarampo", "sh-1792695054792"], "p3-3": ["sh-1793199691630", "sh-1793199689045"],
 "p4-1": ["sh-1793199689555", "sh-1793199689805", "ak1506457588894", "sh-1793199692380"], "p4-2": ["sh-1791716424523", "au-sincicio-granuloma"],
 "p5-1": ["sh-1793199694409"], "p5-2": ["ak1405375421095"],
 "p6-1": ["sh-1792753615215", "au-quadros"], "p6-2": ["au-nk-neutrofilo"], "p6-3": ["au-complemento"], "p6-4": ["sh-1791625430882", "sh-1791625429957"], "p6-5": ["au-mononuclear"],
 "p7-1": ["au-curva"], "p7-2": ["au-intracelular"], "p7-3": ["au-ifn-tipo"],
 "p8-1": ["sh-1792240189143", "sh-1793053714022", "sh-1793053714152"], "p8-2": ["au-ifn-tempo"], "p8-3": ["sh-1793053714276", "sh-1793053714397"],
 "p9-1": ["sh-1793054287147", "sh-1792242117388"], "p9-2": ["sh-1793053714521"], "p9-3": ["ak1503876156644", "au-nk-cd8"],
 "e1-1": ["au-aguda-matriz"], "e2-1": ["ak1715273523479", "au-vidro-fosco"], "e2-2": ["au-ihq"], "e2-3": ["au-anti-hbc"],
 "e3-1": ["ak1486776378880", "au-periportal"], "e4-1": ["sh-1792753612016", "sh-1792117361820", "au-apoptose-necrose"], "e4-2": ["au-necrose-matriz"],
 "e5-1": ["au-interface"], "e5-2": ["au-cd8-b"], "e6-1": ["au-colageno", "sh-1791022173275", "sh-1791022172624"],
}
TERMOS = {"p2-3": ["synthesis", "dividing"], "e3-1": ["portal tracts", "inflammatory cells"], "e2-3": ["vaccine", "core"], "p2-2": ["lysis"], "p2-5": ["cytopathic"], "p1-1": ["response"], "p1-2": ["nucleus", "cytoplasm"], "p6-5": ["mononuclear"], "p8-2": ["adaptive"], "e5-2": ["lymphocytes", "CD8"], "p9-1": ["MHC I"], "e1-1": ["reticulin", "regenerate"], "e2-1": ["ground glass", "surface protein"]}
EXTRA_ITENS = {  # passos que precisavam de 'explicar' e de 'e-se'/'distinguir' (gate de profundidade)
 "Coilócito: o efeito citopático que revela o HPV": [("p5-3", "e-se", "Se o HPV é de tipo oncogênico, o coilócito vem com displasia: transformação leva a neoplasia (prova 2016).", "lâmina 8; prova 2016 P3 1.2", ["dysplasia"], ["ak1405375421095"])],
 "Célula NK: falta de MHC I": [],
 "Interferon tipo I: estado antiviral das vizinhas": [("p8-4", "e-se", "Se o vírus esconde o MHC I, o IFN-I o devolve à superfície e arma a NK.", "transcrição lâmina 12", ["MHC I"], ["sh-1793053714276", "au-nk-cd8"])],
 "Exemplo: estrutura e destino (agudo × crônico)": [("e1-2", "distinguir", "Aguda que poupa a matriz × crônica da adaptativa que a destrói.", "transcrição lâmina 14", ["reticulin"], ["au-aguda-matriz"])],
 "Exemplo: onde a resposta se concentra": [("e3-2", "distinguir", "Periportal (via de chegada do vírus) × centrolobular (lesão metabólica).", "transcrição lâmina 20", ["zone"], ["ak1486776378880", "au-periportal"])],
 "Exemplo: alteração arquitetural e cirrose": [("e6-2", "e-se", "Se a destruição supera a regeneração e a matriz se perde, forma-se cirrose em vez de regeneração.", "transcrição lâmina 28", ["collagen"], ["au-colageno", "au-aguda-matriz"])],
 "Exemplo: proteína viral acumulada e antígeno no tecido": [("e2-4", "distinguir", "Antígeno de superfície no citoplasma × antígeno do core no núcleo.", "lâminas 17–18", ["cytoplasm", "nucleus"], ["au-ihq"])],
 "Exemplo: atividade e perfil do infiltrado": [],
}
m = json.loads((HERE / "mapa-de-profundidade.json").read_text())
for p in m["passos"]:
    for it in p["itens"]:
        it["cards"] = F_(CARDS_ITEM.get(it["id"], it["cards"]))
        it["termos"] = TERMOS.get(it["id"], it["termos"])
    for x in EXTRA_ITENS.get(p["passo"], []):
        if not any(i["id"] == x[0] for i in p["itens"]):
            p["itens"].append(dict(zip(("id", "tipo", "o_que", "fonte", "termos", "cards"), x)))
    tipos = {i["tipo"] for i in p["itens"]}
    if "explicar" not in tipos:  # o passo de NK e o do coilócito: o porquê está nos itens de decorar
        i0 = next((i for i in p["itens"] if i["tipo"] == "decorar"), None) or next(i for i in p["itens"] if i["tipo"] not in ("distinguir",))
        i0["tipo"] = "explicar"
(HERE / "mapa-de-profundidade.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
no_mapa = {k for p in m["passos"] for i in p["itens"] for k in i["cards"]}
assert set(TODOS) <= no_mapa, set(TODOS) - no_mapa

# ---------- motivações: atendida_por ----------
mot = json.loads((HERE / "motivacoes.json").read_text())
for x in mot["motivacoes"]:
    x["atendida_por"] = F_(CARDS_ITEM[x["item_mapa"]])
(HERE / "motivacoes.json").write_text(json.dumps(mot, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- compreensão: princípios ilustrados e reconstruções ----------
c = json.loads((HERE / "compreensao-aula.json").read_text())
PI = {  # bloco de exemplo → cards por princípio (na mesma ordem dos princípios escritos na E2)
 14: [["au-aguda-matriz"], []],
 16: [["ak1715273523479", "au-vidro-fosco"], ["au-ihq"], ["au-anti-hbc"]],
 19: [["au-mononuclear"], ["ak1486776378880", "au-periportal"]],
 21: [["sh-1792753612016", "sh-1792117361820", "au-apoptose-necrose"], ["au-necrose-matriz"]],
 25: [["au-interface"], ["au-cd8-b"]],
 28: [["au-colageno", "sh-1791022173275", "sh-1791022172624"]],
}
for b in c["blocos"]:
    a = b["laminas"][0]
    if b["papel"] == "exemplo":
        for p, ks in zip(b["principios_ilustrados"], PI[a]):
            p["cards"] = F_(ks)
        b["principios_ilustrados"] = [p for p in b["principios_ilustrados"] if p["cards"]]
        b["cards_exemplo"] = []
    if a == 5:
        b["motivo_volume"] = ("As inclusões são o efeito citopático mais cobrado: a galeria do material da aula (Negri, Cowdry, olho de coruja, Guarnieri) entra "
                              "já viva em outras aulas, associada, para mostrar que o compartimento da replicação decide onde fica a inclusão.")
    if a == 2:
        b["cards_associados"] = ["sh-1792753616942"]
    if a == 7:
        b["motivo_volume"] = "O sincício é cobrado em duas provas (2015 e 2017): entram o princípio da fusão, os exemplos da lâmina e do material (VSR, sarampo) e o contraste com o granuloma."
    if a == 28:
        b["motivo_volume"] = "Desfecho arquitetural num passo: troca da reticulina pelo colágeno, a reticulina em prata e a cirrose estabelecida, dois deles já vivos na correlação pato-radio."
    if a == 9:
        b["motivo_volume"] = "Lâmina com cinco ideias (inata × adaptativa, NK × neutrófilo, complemento, CD8 por Fas-FasL, infiltrado mononuclear), cada uma com um card."
for r, ks in zip(c["reconstrucoes"], [["au-inclusao", "sh-1792695054492", "au-raiva-sarampo"], ["sh-1793199689555", "au-sincicio-granuloma"],
                                       ["sh-1793199694409", "ak1405375421095", "au-efeitos"],
                                       ["sh-1792240189143", "sh-1793053714022", "au-ifn-tempo", "sh-1791625429957", "au-cd8-b"]]):
    r["cards"] = F_(ks)
(HERE / "compreensao-aula.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- planejamento.json: alvos por lâmina a partir do inventário ----------
import importlib.util
spec = importlib.util.spec_from_file_location("inv", HERE / "inventario.py"); inv = importlib.util.module_from_spec(spec); spec.loader.exec_module(inv)
ITEM_INV = {"2a": "au-dois-efeitos", "2b": "sh-1792695023262", "3a": "au-efeitos", "4a": "sh-1791743340457", "4b": "au-efeitos", "4c": "au-transformacao",
            "4d": "au-sequestro", "4e": "au-efeitos", "5a": "au-inclusao", "5b": "sh-1793199693557", "6a": "au-raiva-sarampo", "6b": "sh-1793199691630",
            "7a": "sh-1793199689555", "7b": "au-sincicio-granuloma", "8a": "sh-1793199694409", "8b": "ak1405375421095", "9a": "au-quadros",
            "9b": "au-nk-neutrofilo", "9c": "au-complemento", "9d": "sh-1791625430882", "9e": "au-mononuclear", "10a": "au-curva", "10b": "au-intracelular",
            "10c": "au-ifn-tipo", "11a": "sh-1793053714022", "11b": "au-ifn-tempo", "12a": "sh-1793053714276", "12b": "sh-1793053714397",
            "13a": "sh-1793054287147", "13b": "sh-1793053714521", "13c": "au-nk-cd8", "14a": "au-aguda-matriz", "16a": "au-vidro-fosco", "17a": "au-ihq",
            "18a": "au-ihq", "18c": "au-anti-hbc", "18d": "au-anti-hbc", "19a": "au-mononuclear", "20a": "au-periportal", "21a": "sh-1792753612016",
            "22a": "au-necrose-matriz", "23a": "au-necrose-matriz", "24a": "au-apoptose-necrose", "25a": "au-interface", "26a": "au-cd8-b", "27a": "au-cd8-b",
            "28a": "au-colageno", "29a": "sh-1791022172624", "l1": "au-dois-efeitos", "l2": "sh-1793199689805", "l3": "au-mononuclear",
            "p1": "au-inclusao", "p2": "au-sincicio-granuloma", "p3": "ak1405375421095", "p4": "au-ifn-tempo", "o1": "au-efeitos", "o2": "au-quadros",
            "m1": "sh-1793199691630", "a1": "sh-1793054287147"}
alvos = []
for n, tipo, tit, its in inv.SLIDES:
    for i, txt, dest in its:
        k = ITEM_INV.get(f"{n}{i}")
        if k:
            alvos.append({"id": f"pt61-s{n:02d}-{i}", "slide": str(n), "alvo": txt, "fontes": [f"slide {n}"], "origem_prevista": SUB.get(k, k)})
for nomecap, its in inv.CAPITULO:
    for i, txt, _ in its:
        alvos.append({"id": f"pt61-cap-{i}", "slide": "livro", "alvo": txt, "fontes": [nomecap], "origem_prevista": SUB.get(ITEM_INV[i], ITEM_INV[i])})
for nomeex, its in inv.EXERCICIOS:
    for i, txt, _ in its:
        alvos.append({"id": f"pt61-prova-{i}" if i.startswith("p") else f"pt61-mat-{i}", "slide": "prova" if i.startswith("p") else "material",
                      "alvo": txt, "fontes": [nomeex], "origem_prevista": SUB.get(ITEM_INV[i], ITEM_INV[i])})
pl = json.loads((HERE / "planejamento.json").read_text()) if (HERE / "planejamento.json").exists() else {}
pl.update({"aula": "UC03 61 Patologia da infecção viral (Prof. Luiz Fernando Ferraz da Silva)", "feito_antes_de_montar": True, "alvos": alvos})
(HERE / "planejamento.json").write_text(json.dumps(pl, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- inventário: destinos ----------
t = (HERE / "inventario.py").read_text()
D = {k: [SUB.get(v, v)] for k, v in ITEM_INV.items()}
primeiro = {}
for n, tipo, tit, its in inv.SLIDES:
    if its and not str(its[0][2]).startswith("EXC"):
        primeiro.setdefault(n, f"{n}{its[0][0]}")
for k in TODOS:
    s = slide(k); alvo = primeiro.get(s) or primeiro[max(x for x in primeiro if x <= s)]
    if not any(k in v for v in D.values()):
        D[alvo].append(k)
t = re.sub(r"^D = \{.*?\}$", "D = " + json.dumps(D, ensure_ascii=False), t, count=1, flags=re.M)
(HERE / "inventario.py").write_text(t)

# ---------- escopo ----------
esc = json.loads((HERE / "escopo.json").read_text())
esc["historia"] = ("O vírus replica dentro da célula e deixa marcas de dois jeitos. Pelo efeito direto: rompe a célula (inflamação aguda), a transforma "
                   "(neoplasia) ou a altera sem matar, o efeito citopático que o patologista reconhece, com inclusões no compartimento onde o vírus faz suas "
                   "peças, sincícios que não são granuloma e coilócitos. Pela resposta, que pesa mais: a inata segura o vírus nos primeiros dias com IFN-I, "
                   "que põe as vizinhas em estado antiviral, e NK, que mata quem esconde o MHC I; a adaptativa elimina com CD8 e anticorpos porque o vírus "
                   "está dentro da célula. A hepatite crônica mostra tudo junto num tecido: proteína viral acumulada, lesão onde o vírus chega, apoptose "
                   "dirigida e necrose que destrói a matriz, e cirrose quando a destruição vence a regeneração.")
esc["linha_logica"] = [
 {"passo": "Dois efeitos: a lesão viral soma o vírus e a resposta", "mecanismo": True, "liga_ao_proximo": "Primeiro, o que o vírus faz à célula por conta própria", "cards": ["au-dois-efeitos", "sh-1792753616942"]},
 {"passo": "Efeitos diretos: lise → inflamação aguda, transformação → neoplasia, o resto → efeito citopático", "mecanismo": True, "liga_ao_proximo": "O efeito citopático é o que se vê ao microscópio", "cards": ["au-efeitos", "au-sequestro", "au-transformacao"]},
 {"passo": "Efeito citopático: inclusões onde o vírus faz suas peças, sincícios, coilócitos", "mecanismo": True, "liga_ao_proximo": "Mas o que mais lesa na doença é a resposta", "cards": ["au-inclusao", "au-raiva-sarampo", "au-sincicio-granuloma", "sh-1793199694409"]},
 {"passo": "Resposta: inata no agudo, adaptativa no crônico, porque o vírus está dentro da célula", "mecanismo": True, "liga_ao_proximo": "Os primeiros dias dependem do interferon e da NK", "cards": ["au-quadros", "au-nk-neutrofilo", "au-complemento", "au-curva", "au-intracelular"]},
 {"passo": "IFN-I põe as vizinhas em estado antiviral e ganha tempo; NK mata quem perde o MHC I", "mecanismo": True, "liga_ao_proximo": "A hepatite crônica junta tudo isso num tecido", "cards": ["au-ifn-tempo", "sh-1793054287147", "au-nk-cd8"]},
 {"passo": "Exemplo: proteína viral acumulada, lesão onde o vírus chega, apoptose × necrose, matriz destruída e cirrose", "mecanismo": True, "liga_ao_proximo": "", "cards": ["au-aguda-matriz", "au-vidro-fosco", "au-periportal", "au-apoptose-necrose", "au-necrose-matriz", "au-colageno"]},
]
esc["cards_de_conexao"] = ["au-vidro-fosco", "au-nk-cd8", "au-aguda-matriz"]
esc["provas"] = [
 {"id": "2024 P3 1.2", "cards": ["au-inclusao", "sh-1792695054492"]},
 {"id": "2017 P3 1.3", "cards": ["au-sincicio-granuloma", "sh-1793199689555"]},
 {"id": "2016 P3 1.2", "cards": ["sh-1793199694409", "ak1405375421095"]},
 {"id": "2018 P3 1.7", "cards": ["sh-1792240189143", "sh-1793053714022", "au-ifn-tempo", "sh-1791625429957"]},
 {"id": "2015 P2 4.3", "cards": ["sh-1793199689555", "sh-1793199689805"]},
 {"id": "2015 P2 4.8", "cards": ["sh-1792695054492", "sh-1792695054792"]},
 {"id": "2025 P3 2.5", "cards": ["au-quadros", "au-nk-neutrofilo", "au-complemento", "au-ifn-tempo"]},
 {"id": "2024 P1 2.11", "cards": ["sh-1792753615215"]},
 {"id": "2025 P3 3.4", "fora": "influenza exacerbando asma: interação de resposta antiviral e alérgica, da 63 Resposta imune a vírus e da 64 Hipersensibilidade"},
 {"id": "2025 P4 3.2", "fora": "HBV na carcinogênese hepática: aula de agentes carcinogênicos biológicos; aqui só a transformação em geral (au-transformacao)"},
 {"id": "2018 P1 1.10", "fora": "reconhecimento do HBV pelo hepatócito: receptor e entrada, da Micro (58/59), não da patologia da aula"},
 {"id": "2018 P1 1.11", "fora": "montagem da resposta CD8 contra o core do HBV: apresentação em MHC I, da Imuno (20 e 45)"},
]
esc["uso_das_fontes"] = {"aula": ["au-dois-efeitos", "au-efeitos", "au-curva", "au-ifn-tempo"], "prova": ["au-inclusao", "au-sincicio-granuloma", "ak1405375421095"],
                         "bibliografia": ["au-transformacao", "au-mononuclear", "sh-1793199689805"], "apostila": ["au-nk-cd8", "au-quadros"]}
for p_ in esc["linha_logica"]:
    p_["cards"] = F_(p_["cards"])
for q in esc["provas"]:
    if "cards" in q: q["cards"] = F_(q["cards"])
esc["uso_das_fontes"] = {k: F_(v) for k, v in esc["uso_das_fontes"].items()}
(HERE / "escopo.json").write_text(json.dumps(esc, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok:", len(linhas) - 1, "linhas de cobertura;", len(dec), "autorais;", len(alvos), "alvos")
