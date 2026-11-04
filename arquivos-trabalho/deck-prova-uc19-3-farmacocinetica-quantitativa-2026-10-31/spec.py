# Especificação curada — Deck-prova UC19 3: Farmacocinética quantitativa (UC19 P1, Farmacologia; modo prova, base = apostila + extras; F-20261029-CLAUDE-04).
# Davi (29/10): "deck-prova de farmáco independente das minhas aulas, mas cobrindo tudo da apostila e tudo dos materiais extras",
# "vou querer principalmente anking", "realmente cobrindo tudo e um pouco mais"; (30/10) "garante sempre cobertura ampla e que vc esteja
# cobrindo bem as coisas do anking e step + as coisas da prova". A base da prova (fontes/slides.pdf, 13 páginas de excertos literais) faz o
# papel das lâminas. Ordem: bolus e ke → meia-vida e equilíbrio → Vd, clearance e infusão → oral, doses repetidas e não linear → cálculos.
# Os cards de acervo vêm de tabela.tsv (a mesma tabela liga cada card ao item da prova em planejar.py); cópias NEBLI vivas (decks antigos
# Farmacocinética I e II) entram por acervo() com o histórico; os autorais antigos de cinética da FC (deixados para o lote 3) voltam por sh().
import pathlib as _pl, re as _re, sys as _sys, json as _json
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo, _call  # noqa: E402

PIPELINE_VERSAO = 11
MODO = "prova"
SECOES_MOTIVO = ("31/10: lidas inteiras, mas fora do recorte: Bootcamp Nephrology 03 (clearance de PAH, hematócrito: fisiologia renal), "
                 "FirstAid Enzyme kinetics Basics (ΔG, energia de ativação: bioquímica) e NinjaNerd Michaelis-Menten (hexoquinase × glicoquinase: bioquímica); "
                 "delas entram só as notas do assunto (Cx × TFG e inulina já estão no lote 2)")
_FORA_SEC = ("Nephrology", "Enzyme_kinetics_Basics", "NinjaNerd")
_SEC = [x for x in (HERE / "busca" / "secoes").glob("*.txt") if not any(f in x.name for f in _FORA_SEC)]
SECOES_DA_AULA = sorted(s.name for s in _SEC)
AUTORAL_EXCECAO = ("GUIA-1 §1, cobertura antes do teto: 10 dos 15 autorais são os antigos de cinética que Davi já estudava, de volta com histórico; "
                   "só 5 são novos (14% dos cards novos, gate deck_prova), cada um numa lacuna provada do objetivo f")
PIPELINE = "anking-primeiro"
RUN_ID = "uc19-dp3-20261031a"
SHORT = "dp3"
LESSON = "2026-uc19-deck-prova-3-farmacocinetica-quantitativa"
DECK = "NEBLI::UC19::P1::Farmacologia::Deck-prova 3 — Farmacocinética quantitativa"
CRITERIOS = "MEMORY.md + pipeline v11 (modo prova) + FEEDBACKS até F-20261031-CLAUDE-01 + GUIA-1 a GUIA-4 + PLANO-DECK-PROVA-UC19, 31/10"
MEDIA = {}
BUSCA = ("Três caminhos (30/10): seções de cinética do AnKing (B&B, Bootcamp, First Aid, Sketchy, Physeo; busca/secoes); "
         "palavra-chave com sinônimos em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e no NEBLI vivo, uma consulta "
         "por item planejado (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


def F(loc, trecho):
    return [{"localizador": loc, "trecho": trecho}]


BL = {"k": "1-bolus-ke", "h": "2-meia-vida-equilibrio", "c": "3-vd-clearance-infusao", "o": "4-oral-repetidas-nao-linear", "r": "4-oral-repetidas-nao-linear", "z": "4-oral-repetidas-nao-linear", "x": "5-calculos"}
BASE = "fontes/slides.txt"
ITENS = __import__("runpy").run_path(str(HERE / "planejar.py"), run_name="spec")["ITENS"]


def pagina(item):
    return ITENS[item][0]


def motivo_de(item):
    return f"{ITENS[item][3]}; item {item} da matriz"


AUT = {
 "mrt": au("mrt", "In a one-compartment model, the <b>mean residence time</b> (MRT) of a drug equals {{c1::1/ke}}",
    "A-aula", BL["h"], "MRT = 1/ke", pagina("h4"), "apostila p.16 (aula 3, cap. 3); De Nucci p.5", motivacao="m-h4",
    fontes=F("apostila, aula 3, cap. 3, p.16", "é possível calcular o MRT como sendo o inverso da constante de eliminação"),
    sem_imagem="fórmula, sem figura na base",
    extra="ke is the elimination rate constant; MRT is the average time a molecule stays in the body (AUMC/AUC: area under the moment curve over area under the curve).<br>With ke = 0.1 h⁻¹, MRT = 10 h: 10% of the molecules leave per hour, and each stays 10 h on average."),
 "oscilacao": au("oscilacao", "With repeated doses, a longer <b>dosing interval</b> at the same daily dose keeps the average level but widens the {{c1::peak-to-trough}} fluctuation",
    "A-aula", BL["r"], "Intervalo define a oscilação pico-vale", pagina("r1"), "objetivos FC f.i(4b) (roteiro de prova)", motivacao="m-r1",
    fontes=F("objetivos cognitivos FC, item f.i(4)", "variação de pico a vale em função da dose, F, t1 / 2, dosagem intervalo (T)"),
    sem_imagem="conceito, sem figura na base",
    extra="Average steady-state level = D·F / (τ·Cl), with F the bioavailability and τ the interval; absorption speed does not change it.<br>Giving the same dose more often, or as extended release, narrows the swing."),
 "saturacao-fenitoina": au("saturacao-fenitoina", "A small increase in <b>phenytoin</b> dose can raise its plasma level disproportionately, because its metabolizing enzymes are near {{c1::saturation}}",
    "A-aula", BL["z"], "Saturação: pequeno aumento de dose, grande aumento de nível", pagina("z4"), "objetivos FC f.ii(1); questão de prova (banco p.65, fenitoína)", motivacao="m-z4",
    fontes=F("objetivos cognitivos FC, item f.ii(1)", "cinética \"Michaelis- Menten\", definição e implicações, por ex. para dosagem de fenitoína"),
    sem_imagem="conceito, sem figura na base",
    extra="Well above Km the enzyme runs close to Vmax and removes an almost fixed amount per hour (zero order), so the half-life lengthens as the level rises.<br>That is why phenytoin doses are raised in small steps with level monitoring."),
 "saturacao-proteina": au("saturacao-proteina", "In <b>salicylate overdose</b>, plasma protein binding saturates, so the {{c1::free fraction}} rises out of proportion to the dose",
    "A-aula", BL["z"], "Saturação da ligação a proteínas (salicilato)", pagina("z5"), "objetivos FC f.ii(2) (roteiro de prova)", motivacao="m-z5",
    fontes=F("objetivos cognitivos FC, item f.ii(2)", "Saturação da ligação às proteínas plasmáticas, implicações, ex. overdose de salicilato"),
    sem_imagem="conceito, sem figura na base",
    extra="More free drug reaches the tissues, including the brain, and toxicity jumps.<br>Salicylate elimination also saturates at high doses, adding to the accumulation."),
 "absorcao-saturavel": au("absorcao-saturavel", "When a drug is absorbed by a saturable intestinal <b>transporter</b>, raising the dose lowers its oral {{c1::bioavailability}}",
    "R-detalhe", BL["z"], "Absorção por transportador satura", pagina("z6"), "objetivos FC f.ii(3) (roteiro de prova)", motivacao="m-z6",
    fontes=F("objetivos cognitivos FC, item f.ii(3)", "Absorção dependente da dose e biodisponibilidade; transportadores intestinais"),
    sem_imagem="conceito, sem figura na base",
    extra="Once the carrier is saturated, the extra drug stays in the gut, so a larger fraction of the dose is lost.<br>Gabapentin is the classic example."),
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
        CARDS.append(sh(int(_x[3:]), "azul", _bl, _alvo, pagina(_item), f"A-aula: autoral antigo de cinética da FC (deck Farmacocinética I), reaproveitado com o histórico; {motivo_de(_item)}"))
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

DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {"objetivo": "Farmacocinética quantitativa da prova de Farmacologia Básica: como a concentração cai depois do bolus, o que é meia-vida e estado de equilíbrio, como Vd e clearance dão a dose, e quando a cinética deixa de ser de primeira ordem.",
          "centrais": [["primeira ordem", "sh-1792624457204", "sh-1792624458275"], ["meia-vida", "ak1490066195477", "sh-1792624463275"],
                       ["dose", "sh-1792624466325", "sh-1792657541958"], ["saturação", "saturacao-fenitoina"]],
          "exemplos": [], "outras_aulas": ["Deck-prova 2 Farmacocinética (Vd, clearance e extração qualitativos)"]}

EXCLUIDOS = []  # preenchido por excluidos.py (lido aqui para o build)
_exc = HERE / "excluidos.json"
if _exc.exists():
    EXCLUIDOS = [tuple(x) for x in _json.loads(_exc.read_text(encoding="utf-8"))]
FORA_DO_RECORTE = ["Fisiologia renal (PAH, fluxo plasmático renal, hematócrito) e bioquímica de enzimas (ΔG, hexoquinase): outras UCs."]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
