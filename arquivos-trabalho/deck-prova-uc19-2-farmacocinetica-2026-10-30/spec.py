# Especificação curada — Deck-prova UC19 2: Farmacocinética (UC19 P1, Farmacologia; modo prova, base = apostila + extras; F-20261029-CLAUDE-04).
# Davi (29/10): "deck-prova de farmáco independente das minhas aulas, mas cobrindo tudo da apostila e tudo dos materiais extras",
# "vou querer principalmente anking", "realmente cobrindo tudo e um pouco mais"; (30/10) "garante sempre cobertura ampla e que vc esteja
# cobrindo bem as coisas do anking e step + as coisas da prova". A base da prova (fontes/slides.pdf, 32 páginas de excertos literais) faz o
# papel das lâminas. Ordem: química e membranas → vias e tipos → absorção → distribuição → metabolismo → excreção e clearance → casos.
# Os cards de acervo vêm de tabela.tsv (a mesma tabela liga cada card ao item da prova em planejar.py); cópias NEBLI vivas (decks antigos
# Farmacocinética I e II) entram por acervo() com o histórico; os autorais antigos mais fortes da FC voltam por sh().
import pathlib as _pl, re as _re, sys as _sys, json as _json
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo, _call  # noqa: E402

PIPELINE_VERSAO = 11
MODO = "prova"
SECOES_MOTIVO = ""  # 30/10: as 31 seções de farmacocinética lidas inteiras entram todas
_SEC = list((HERE / "busca" / "secoes").glob("*.txt"))
SECOES_DA_AULA = sorted(s.name for s in _SEC)
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc19-dp2-20261030a"
SHORT = "dp2"
LESSON = "2026-uc19-deck-prova-2-farmacocinetica"
DECK = "NEBLI::UC19::P1::Farmacologia::Deck-prova 2 — Farmacocinética"
CRITERIOS = "MEMORY.md + pipeline v11 (modo prova) + FEEDBACKS até F-20261030-CLAUDE-01 + GUIA-1 a GUIA-4 + PLANO-DECK-PROVA-UC19, 30/10"
MEDIA = {}
BUSCA = ("Três caminhos (30/10): seções de recurso de farmacocinética do AnKing (First Aid, B&B, Bootcamp, Sketchy, Physeo; busca/secoes); "
         "palavra-chave com sinônimos em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e no NEBLI vivo, uma consulta "
         "por item planejado (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


def F(loc, trecho):
    return [{"localizador": loc, "trecho": trecho}]


BL = {"q": "1-quimica-membranas", "v": "2-vias-tipos", "b": "3-absorcao", "d": "4-distribuicao", "m": "5-metabolismo", "e": "6-excrecao-clearance", "x": "7-casos"}
BASE = "fontes/slides.txt"
ITENS = __import__("runpy").run_path(str(HERE / "planejar.py"), run_name="spec")["ITENS"]


def pagina(item):
    return ITENS[item][0]


def motivo_de(item):
    return f"{ITENS[item][3]}; item {item} da matriz"


AUT = {
 "passagem-membrana": au("passagem-membrana", ORG("<b>Ways a drug crosses the gut membrane</b>, by the drug:<br>- most drugs, lipid- or water-soluble: {{c1::passive diffusion::p…}}<br>- drugs resembling natural metabolites, on a carrier with no energy: {{c1::facilitated diffusion::f…}}<br>- the same, on a carrier against the gradient: {{c1::active transport::a…}}<br>- drugs too large for the membrane: {{c1::endocytosis::e…}}"),
    "V-pilar", BL["q"], "Quatro modos de atravessar a membrana", pagina("q3"), "objetivos FC a.iii; apostila p.14; questões de prova (banco p.62 e p.74)", motivacao="m-q3", organizador=True,
    organizacao_fonte=BASE, organizacao_trecho="os fármacos podem ser absorvidos pelo trato gastrointestinal por difusão passiva, difusão facilitada, transporte ativo ou endocitose.",
    fontes=F("apostila, aula 2, cap. 2, p.14", "No âmbito da difusão passiva, a maioria dos fármacos é absorvida por este meio."),
    sem_imagem="organizador; sem figura na base",
    extra="Water-soluble drugs diffuse through channels and aquaporins; lipid-soluble ones move straight through the bilayer.<br>Carriers can saturate and be competed for; diffusion cannot."),
 "vias-org": au("vias-org", ORG("<b>Routes of administration</b>, in three groups:<br>- enteral, by mouth: oral and {{c1::sublingual::s…}}<br>- parenteral, straight into the body: {{c1::intravenous::i…}}, intramuscular and {{c1::subcutaneous::s…}}<br>- other routes: rectal, inhaled, topical and transdermal, epidural, intradural, intraosseous, intra-arterial"),
    "V-pilar", BL["v"], "Vias enterais, parenterais e outras", pagina("v1"), "apostila p.11–12 (caps. 2 a 4); objetivos FC b.iv; questões de prova (banco p.57)", motivacao="m-v1", organizador=True,
    organizacao_fonte=BASE, organizacao_trecho="as principais vias de administração incluem a via enteral, a via parenteral e outras distintas vias.",
    fontes=F("apostila, aula 1, cap. 2, p.11", "A via enteral envolve a administração pela boca."),
    sem_imagem="organizador; sem figura na base",
    extra="Rectal falls under the other routes: half of its venous drainage skips the portal vein.<br>Parenteral routes avoid first-pass metabolism and give tighter dose control, but cannot be undone."),
 "via-iv": au("via-iv", "<b>Intravenous</b> injection gives immediate absorption and a precise level, at the risk of infection and local {{c1::thrombosis::t…}}",
    "A-aula", BL["v"], "IV: imediata e precisa, com trombose local", pagina("v2"), "apostila p.11; questões de prova (banco p.24, p.55, p.60 e p.91)", motivacao="m-v2",
    fontes=F("apostila, aula 1, cap. 3, p.11", "suas desvantagens incluem a possibilidade de promover infecções caso a administração não seja feita corretamente, podendo ainda provocar quadros de trombose local"),
    sem_imagem="definição, sem figura na base",
    extra="The whole dose reaches the blood (bioavailability 100%), and the dose can be changed or stopped at once.<br>High early peaks can cause adverse effects, and drug mixtures that precipitate cannot go IV."),
 "liberacao": au("liberacao", "An <b>extended-release</b> form slows the drug's absorption and flattens peaks and troughs, but does not change its {{c1::elimination half-life}}",
    "A-aula", BL["v"], "Liberação prolongada muda a absorção", pagina("v9"), "questão de prova (orientadora FC 10); objetivos FC b.v", motivacao="m-v9",
    fontes=F("questão orientadora FC 10", "reduzindo a flutuação temporal da concentração plasmática sem alterar a meia-vida de eliminação"),
    sem_imagem="conceito, sem figura na base",
    extra="Once-daily extended-release morphine replaces six oral doses: absorption was slowed, not elimination.<br>Depot IM forms work the same way; PEGylation instead enlarges the molecule and slows its renal clearance."),
 "fatores-absorcao": au("fatores-absorcao", ORG("<b>Factors that set drug absorption</b> at the site of absorption:<br>- {{c1::pH::p…}}<br>- {{c1::blood flow::b…}}<br>- {{c1::surface area::s…}}<br>- {{c1::contact time::c…}}<br>- {{c1::P-glycoprotein::P…}} expression"),
    "V-pilar", BL["b"], "Cinco fatores da absorção", pagina("b3"), "apostila p.14; objetivos FC b.ii–iii; questões de prova (apostila ex.8; banco p.51 e p.56)", motivacao="m-b3", organizador=True,
    organizacao_fonte=BASE, organizacao_trecho="os fatores que influenciam a absorção destes fármacos são",
    fontes=F("apostila, aula 2, cap. 2, p.14", 'Valor de pH; \uf0b7 Fluxo de sangue no local de absorção; \uf0b7 Área ou superfície de absorção; \uf0b7 Tempo de contato com essa superfície; \uf0b7 Expressão de glicoproteína P.'),
    sem_imagem="organizador; sem figura na base",
    extra="The small intestine absorbs most drugs: its area and blood flow outweigh the pH effect.<br>Epinephrine with lidocaine cuts local blood flow, so less drug leaves the injection site."),
 "pgp-loperamida": au("pgp-loperamida", "<b>P-glycoprotein</b> pumps <b>loperamide</b> out of the brain, so taking a P-gp inhibitor with loperamide risks {{c1::CNS depression}}",
    "A-aula", BL["b"], "Inibir a P-gp põe a loperamida no SNC", pagina("b5"), "questões de prova (apostila ex.7; banco p.3); apostila p.14", motivacao="m-b5",
    fontes=F("apostila, aula 2, cap. 2, p.14", "ela “bombeia” fármacos para fora das células e, portanto, em grandes concentrações ela retarda a absorção de fármacos."),
    sem_imagem="caso, sem figura na base",
    extra="CNS: central nervous system; loperamide reaching it acts as an opioid.<br>P-gp sits on the apical side of gut cells, brain capillaries, bile canaliculi and renal tubules and pumps substrates back out.<br>Inhibitors such as grapefruit, verapamil and ketoconazole raise substrate levels."),
 "dialise-vd": au("dialise-vd", "In an overdose, <b>hemodialysis</b> removes a drug well only if its <b>volume of distribution</b> is {{c1::small::size}}",
    "A-aula", BL["d"], "Hemodiálise só remove Vd pequeno", pagina("d9"), "questões de prova (banco p.43 q1, p.55 e p.65)", motivacao="m-d9",
    fontes=F("banco de questões, p.43", "Qual desses fármacos seria mais efetivamente eliminado por hemodiálise no tratamento de uma superdosagem?"),
    sem_imagem="conceito, sem figura na base",
    extra="A drug spread into fat and tissues (large Vd) leaves almost nothing in the blood for the dialyzer.<br>High protein binding has the same effect, because only free drug crosses the dialysis membrane."),
 "cyp3a4": au("cyp3a4", "The <b>cytochrome P450</b> isoform that metabolizes the <b>largest share</b> of drugs (about a third) is {{c1::CYP3A4/5}}",
    "V-prova", BL["m"], "CYP3A4 metaboliza a maior parte", pagina("m3"), "questão de prova (orientadora FC 22); De Nucci p.12; objetivos FC d.iv", motivacao="m-m3",
    fontes=F("De Nucci, cap. 1, fig. 1.21", "3A4/5 36%"),
    sem_imagem="dado, a figura da base é um gráfico de setores sem rótulo legível",
    extra="Next come CYP2D6 (about 21%) and CYP2C8/9 (about 17%).<br>That is why CYP3A4 inhibitors (ketoconazole, clarithromycin, grapefruit) cause so many interactions."),
 "eliminacao-org": au("eliminacao-org", ORG("<b>Drug excretion routes</b>:<br>- main: {{c1::kidney::k…}}<br>- {{c1::bile::b…}} and feces<br>- {{c1::lungs::l…}}, the main route only for inhaled anesthetics<br>- minor: sweat and milk"),
    "V-pilar", BL["e"], "Vias de excreção", pagina("e1"), "objetivos FC e.i, e.ii e e.vi; questões de prova (banco p.52)", motivacao="m-e1", organizador=True,
    organizacao_fonte=BASE, organizacao_trecho="Principais locais de excreção de fármacos: renal, biliar/alimentar, pulmonar (a via principal apenas para agentes inalatórios). Locais menores de excreção de fármacos: suor e leite",
    fontes=F("objetivos cognitivos FC, item e.ii", "Locais menores de excreção de fármacos: suor e leite"),
    sem_imagem="organizador; sem figura na base",
    extra="Excretion is the drug or its metabolite leaving the body.<br>Elimination is broader: metabolism plus excretion."),
 "fumo-1a2": au("fumo-1a2", "<b>Cigarette smoke</b> induces {{c1::CYP1A2}}, so a smoker who quits can reach toxic <b>theophylline</b> levels",
    "A-aula", BL["x"], "Fumo induz CYP1A2 (teofilina)", pagina("x3"), "questões de prova (orientadoras FC 5 e 25)", motivacao="m-x3",
    fontes=F("questão orientadora FC 5", "Hidrocarbonetos do fumo de tabaco são indutores do CYP1A2; a suspensão do tabagismo causou redução do clearance da teofilina e consequente elevação dos níveis plasmáticos."),
    sem_imagem="caso, sem figura na base",
    extra="The inducers are polycyclic hydrocarbons in the smoke, not nicotine.<br>Induction builds and fades over days, so toxicity appears days after quitting at the same dose."),
}

_LINHAS = [l for l in (HERE / "tabela.tsv").read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
_HY = {}
for _n in _call("notesInfo", notes=[int(l.split("\t")[0]) for l in _LINHAS if l.split("\t")[0].isdigit()]):
    _m = next((_re.search(r"Yield::(\d)-", x) for x in _n["tags"] if _re.search(r"Yield::(\d)-", x)), None)
    _HY[_n["noteId"]] = int(_m.group(1)) if _m else None


def codigo(nid, dado):
    """Sem código na tabela: HY 1–2 → V-hy (verde), HY 3 → A-step (azul), resto → R-detalhe (rosa)."""
    if dado:
        return dado
    return {1: "V-hy", 2: "V-hy", 3: "A-step"}.get(_HY.get(nid), "R-detalhe")


CARDS = []
for _l in _LINHAS:
    _x, _item, _alvo, *_cod = _l.split("\t")
    _cod = (_cod[0].strip() if _cod else "") or None
    _bl = BL[_item[0]]
    if _x in AUT:
        CARDS.append(AUT[_x])
    elif _x.startswith("sh-"):
        CARDS.append(sh(int(_x[3:]), "azul", _bl, _alvo, pagina(_item), f"A-aula: autoral antigo da FC (decks Farmacocinética I/II), reaproveitado com o histórico; {motivo_de(_item)}"))
    else:
        CARDS.append(K(int(_x), codigo(int(_x), _cod), _bl, _alvo, pagina(_item), motivo_de(_item)))
assert set(AUT) <= {c["key"] for c in CARDS}

finalizar(CARDS, HERE, BUSCA)

VERSO = {}  # porquê em uma linha para nota de acervo sem verso explicativo (preenchido depois do build, nota a nota)
_v = HERE / "verso.json"
if _v.exists():
    VERSO = _json.loads(_v.read_text(encoding="utf-8"))
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

# F-20261031-CLAUDE-01: card de fármaco específico vai para o subdeck "Fármacos específicos" e o verso diz o princípio que ilustra
_REORG = _json.loads((HERE.parent / "reorganizacao-deck-prova-uc19.json").read_text(encoding="utf-8"))
_ESPEC = _REORG["lotes"].get(HERE.name, {})
for c in CARDS:
    if c["key"] in _ESPEC:
        c["subdeck"] = "Fármacos específicos"
        c["extra_add"] = f"Illustrates: {_REORG['en'][c['key']]}." + ("<br>" + c["extra_add"] if c.get("extra_add") else "")

DUPLICACAO = {"fumo-1a2": "ganho: o AnKing cita o CYP1A2 só numa tabela de substratos; só este liga o fumo à indução do CYP1A2 e à intoxicação por teofilina (orientadoras FC 5 e 25)",
              "liberacao": "ganho: o AnKing diz que glargina e PEGuilação prolongam a ação; só este card diz que a liberação estendida muda a absorção e não a meia-vida de eliminação (orientadora 10)",
              "fatores-absorcao": "ganho: o AnKing tem fatores soltos (esvaziamento, quelação, IBP); este é o conjunto da apostila p.14 que o banco cobra lado a lado",
              "eliminacao-org": "ganho: o AnKing cita a excreção renal e casos de bile e pulmão; este lista as vias de excreção do objetivo FC e.ii"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {"objetivo": "Farmacocinética qualitativa da prova de Farmacologia Básica: como o fármaco atravessa membranas, entra pelas vias, chega ao sangue (biodisponibilidade), se distribui, é metabolizado e é excretado, e como o clearance mede essa saída.",
          "centrais": [["membranas", "passagem-membrana", "sh-1793275928565"], ["vias", "vias-org", "via-iv"], ["absorção", "fatores-absorcao", "sh-1793274288090"],
                       ["metabolismo", "cyp3a4"], ["excreção", "eliminacao-org", "sh-1792624465549"]],
          "exemplos": [], "outras_aulas": ["Deck-prova 1 Farmacodinâmica (janela terapêutica, quiralidade)", "Deck-prova 3 Farmacocinética quantitativa (ke, t½, Css, doses)"]}

EXCLUIDOS = []  # preenchido por excluidos.py (lido aqui para o build)
_exc = HERE / "excluidos.json"
if _exc.exists():
    EXCLUIDOS = [tuple(x) for x in _json.loads(_exc.read_text(encoding="utf-8"))]
FORA_DO_RECORTE = ["Cinética quantitativa (ke, t½, bolus, infusão, Css, dose de ataque e de manutenção, ordem zero, Michaelis-Menten): deck-prova 3.",
                   "Janela terapêutica e quiralidade (objetivos FC a.v e b.i): já no deck-prova 1."]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
