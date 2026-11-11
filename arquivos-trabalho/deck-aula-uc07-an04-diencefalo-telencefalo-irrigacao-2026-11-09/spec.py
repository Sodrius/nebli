# Especificação curada — Anatomia 04: diencéfalo, núcleos da base, telencéfalo e irrigação do encéfalo
# (UC07 P1, 27/10/2026, Prof. Alfredo Jacomo; sem lâminas: 62 unidades do percurso). F-20261109-CLAUDE-01: IO do Kenhub de toda
# estrutura, subdecks por estrutura, AnKing HY 1–3 de relação clínica, organizadores para as listas da aula, poucos clozes.
import json as _json, pathlib as _pl, re as _re, sys as _sys, urllib.request as _u
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
_sys.path.insert(0, str(HERE))
from nebli.spec_lib import ak, au, sh, kh, ORG, finalizar
import curadoria as _cur, textos as _tx, decisoes_secoes as _dec, plano as _plano

PIPELINE_VERSAO = 17
PIPELINE = "anking-primeiro"
MODO = "aula"
RUN_ID = "uc07-an04-20261109"
SHORT = "u7an04"
LESSON = "2026-uc07-anatomia-04-diencefalo-telencefalo-irrigacao"
DECK = "NEBLI::UC07::P1::Anatomia::04 Diencéfalo, núcleos da base, telencéfalo e irrigação"
CRITERIOS = "MEMORY e guias vigentes até F-20261109-CLAUDE-01 (IO Kenhub de toda estrutura, subdecks, AnKing HY 1–3, uma estrutura = um card, aplicar ao fim de cada aula)."
BUSCA = ("Três caminhos (09/11): seções FirstAid/B&B/Bootcamp/Pixorize/DirtyMedicine de diencéfalo, córtex, núcleos da base e irrigação (busca/secoes, 51 seções decididas); "
         "significado por chave em AnKing, Referências Externas, Kenhub e NEBLI-vivo (busca/semantica.jsonl, 166 consultas); Kenhub da Referência por nome. ")
AUTORAL_EXCECAO = ""
SECOES_MOTIVO = ""
SECOES_DA_AULA = sorted(p.name for p in (HERE / "busca/secoes").glob("*.txt"))
MEDIA = {"u7an04-hipotalamo-focal.jpg":"img/u7an04-hipotalamo-focal.jpg"}
SHARED_FIELDS = {}


def _ac(a, **p):
    return _json.load(_u.urlopen(_u.Request("http://127.0.0.1:8765", _json.dumps({"action": a, "version": 6, "params": p}).encode())))["result"]


_res_nids = [r[3] for r in _cur.R if r[2] in ("res", "an01")]
_live = {n["noteId"]: n for n in _ac("notesInfo", notes=_res_nids)}
_ak_nids = [r[3] for r in _cur.R if r[2] == "ak"]
_akinfo = {n["noteId"]: n for n in _ac("notesInfo", notes=_ak_nids)}
def _imgs(s):
    tags = _re.findall(r"<img[^>]*>", s or "")
    out = []
    for tag in tags:
        tag = _re.sub(r'\s+(?:style|width|height)\s*=\s*(?:"[^"]*"|\x27[^\x27]*\x27|[^\s>]+)', '', tag, flags=_re.I)
        tag = _re.sub(r'\s*/?>$', ' style="width:100%;max-width:850px;height:auto">', tag)
        out.append(tag)
    return ''.join(out)
_FIG = '<br><br>'


def _bloco(u):
    return "A-%02d" % (1 if u <=21 else 22 if u<=42 else 43 if u<=46 else 47)


_FIGURA_DE = {"ak-1481162464655": 1792347675113, "ak-1481562763561": 1792350083556, "ak-1481562772354": 1792350083556, "ak-1481562774888": 1792350083556, "ak-1483845113686": 1792350083556, "ak-1481772047979": 1792350075605, "ak-1481418712049": 1792572870653, "ak-1481418725172": 1792572870652, "ak-1461884702127": 1792244787869, "ak-1481418766004": 1792346374740, "ak-1481418757045": 1792346373316, "ak-1481418763459": 1792346376214, "ak-1481418777586": 1792346381716}
_SEM_IMAGEM = {k: "Organizador ou cloze verbal da lista da aula; cada estrutura citada tem IO Kenhub próprio no mesmo subdeck, que é a imagem para decorar." for k in ("diencefalo-partes-org", "talamo-limites-org", "talamo-nucleos-org", "hipotalamo-limites-org", "hipotalamo-nucleos-org", "subtalamo-limites-org", "lobos-limites-org", "corpo-caloso-partes-org", "face-inferior-org", "corte-horizontal-org", "estriado-org", "capsula-interna-partes-org", "aci-ramos-org", "vertebrobasilar-org", "territorios-org", "willis-org", "diencefalo-escondido", "nucleo-x-ganglio", "faces-hemisferio", "giro-x-sulco", "achar-sulco-central")}
IMAGENS_LOCAIS = {}
_FIG_LOCAL = {}


def _figura(nid):
    f = _ac("notesInfo", notes=[nid])[0]["fields"]
    for k in ("Imagem", "Imagem Verso", "Image", "Extra", "Text"):
        if k in f and "<img" in f[k]["value"]:
            m = _re.search(r'<img[^>]*src="([^"]+)"[^>]*>', f[k]["value"])
            if m:
                return f'<img src="{m.group(1)}" style="width:100%;max-width:820px;height:auto">'
    return ""


_FIG_INDICE = {"ak-1481562846112": 1, "ak-1481244778741": 1, "ak-1481944929569": 0, "ak-1481857900096": 0, "ak-1481857835449": 0, "ak-1480389641277": 0, "ak-1520976098044": 1, "ak-1480995212247": 0, "ak-1480995292746": 1, "ak-1480995205801": 0, "ak-1480995225262": 0, "ak-1480995329569": 1, "ak-1480995318517": 1, "ak-1481047476591": 1, "ak-1481513222026": 0, "ak-1481244840641": 1, "ak-1481562751403": 0, "ak-1481562744652": 0, "ak-1481772053364": 0}
_FIG_TROCA = {"ak-1481162464655": 1792347675113, "ak-1481562763561": 1792350083556, "ak-1481562772354": 1792350083556, "ak-1481562774888": 1792350083556, "ak-1483845113686": 1792350083556, "ak-1481772047979": 1792350075605}
_FIG_TROCA_KH = {}
_FIG_NENHUMA = {"ak-1481418744155":"Relação sensitiva e evolução pós-AVC, sem alvo de identificação; a topografia talâmica tem IO próprio no mesmo bloco.","ak-1481418842065": "Relação clínica/funcional sem figura própria no acervo; a estrutura tem IO Kenhub no mesmo subdeck.", "ak-1481162002789": "Relação clínica/funcional sem figura própria no acervo; a estrutura tem IO Kenhub no mesmo subdeck.", "ak-1481836514209": "Relação clínica/funcional sem figura própria no acervo; a estrutura tem IO Kenhub no mesmo subdeck."}
CARDS = []
META = {}
PLANKEY = {}
for (u, key, kind, nid, cod, alvo) in _cur.R:
    motivo = f"{cod}: {alvo} (unidade {u} do percurso)."
    cor = {"V": "verde", "A": "azul", "R": "rosa"}[cod[0]]
    if kind in ("res", "an01"):
        c = sh(nid, cor, _bloco(u), alvo, u, motivo)
        PLANKEY[key] = c["key"]
        if kind in ("res", "an01"):
            n = _live[nid]; f = {k: v["value"] for k, v in n["fields"].items()}
            edit = {}
            if nid in _tx.TEXT_RES:
                edit["Text"] = _tx.TEXT_RES[nid]
            if nid in _tx.EXTRA_RES and "Extra" in f:
                edit["Extra"] = _tx.EXTRA_RES[nid] + (_FIG + _imgs(f["Extra"]) if _imgs(f["Extra"]) else "")
            if nid in _tx.RENOMEAR:
                from nebli.kenhub.renomear import renomear
                novos, midia = renomear(f, _tx.RENOMEAR[nid], HERE / "img", _pl.Path(_ac("getMediaDirPath")))
                edit.update(novos)
                MEDIA.update({k: str(v.relative_to(HERE)) for k, v in midia.items()})
            if edit:
                SHARED_FIELDS[str(nid)] = edit
    elif kind == "kh":
        c = kh(key, nid, cod, _bloco(u), alvo, u, motivo)
    elif kind == "khnome":
        c = kh(key, nid, cod, _bloco(u), alvo, u, motivo, nome={1792244823068: "Trígono do nervo vago"}[nid])
    elif kind == "khtxt":
        f = {k: v["value"] for k, v in _ac("notesInfo", notes=[nid])[0]["fields"].items()}
        figs = _figura(_FIG_TROCA_KH[key]) if key in _FIG_TROCA_KH else _imgs(f.get("Extra", ""))
        c = ak(key, nid, cod, _bloco(u), alvo, u, motivo, origin="Kenhub", text=_tx.KH_TEXTO.get(nid, f["Text"]), extra=_tx.KH_TXT[nid] + (_FIG + figs if figs else ""), copia_traducao_uc07=True)
    elif kind == "ak":
        txt, ext = _tx.AK[nid]
        f = {k: v["value"] for k, v in _akinfo[nid]["fields"].items()}
        figs = _imgs(f.get("Extra", "")) + _imgs(f.get("Image", "")) + _imgs(f.get("Front", ""))
        _todas = _re.findall(r"<img[^>]*>", figs)
        if key in _FIG_TROCA:
            figs = _figura(_FIG_TROCA[key])
        elif key in _FIG_NENHUMA:
            figs = ""
        elif key in _FIG_INDICE and _todas:
            figs = _todas[min(_FIG_INDICE[key], len(_todas) - 1)]
        if not figs and key in _FIGURA_DE and key not in _FIG_NENHUMA:
            figs = _figura(_FIGURA_DE[key])
        c = ak(key, nid, cod, _bloco(u), alvo, u, motivo, origin="AnKing", text=txt, extra=ext + (_FIG + figs if figs else ""), copia_traducao_uc07=True)
    elif kind == "au":
        txt, ext = _tx.AU[key]
        mot = "m-" + next(i[1] for i in _plano.ITENS if i[0] == u) if any(i[0] == u for i in _plano.ITENS) else "m-u%02d" % u
        figs = _FIG_LOCAL.get(key) or (_figura(_FIGURA_DE[key]) if key in _FIGURA_DE else "")
        c = au(key, txt, cod, _bloco(u), alvo, u, _tx.AU_FONTE[key], extra=ext + (_FIG + figs if figs else ""), motivacao=mot,
               espelhos=(1481162303980, 1481513119712, 1481418839841), organizador="data-nebli-organizacao" in txt)
        if key in _SEM_IMAGEM:
            c["sem_imagem"] = _SEM_IMAGEM[key]
    elif kind == "livroio":
        continue  # materializado abaixo, com fonte e máscara do livro
    else:
        raise SystemExit(kind)
    if key in _FIG_NENHUMA:
        c["sem_imagem"] = _FIG_NENHUMA[key]
    PLANKEY.setdefault(key, c["key"])
    CARDS.append(c)
    META[c["key"]] = {"unidade": u, "label": key, "tipo_fonte": kind}

# Identificações sem IO disponível no Kenhub: fallback focal do Machado.
import io_machado as _livroio
_bookcards, _bookmedia = _livroio.construir()
MEDIA.update(_bookmedia)
for _b in _bookcards:
    _c = {"key":_b['key'],"kind":"livroio","cod":"A-aula","flags":{1:3},"fields_override":_b['fields'],
          "bloco":_bloco(_b['u']),"alvo":_b['nome'],"evid":f"Slide {_b['u']}",
          "motivo":"IO: estrutura ensinada na aula; busca Kenhub sem identificação recuperável, fallback em Machado.",
          "fonte_livro":f"Machado 3ed PDF{_b['pagina']}","sem_alternativa":"IO Kenhub não disponível no inventário vivo/corpus local consultado; relação escrita não substitui identificação visual."}
    CARDS.append(_c)
    META[_c['key']]={"unidade":_b['u'],"label":_b['key'],"tipo_fonte":"livroio"}

finalizar(CARDS, HERE, BUSCA)

# ---- decisão de toda nota das seções da aula
_used_src = {c.get("src") for c in CARDS if c.get("src")}
_sh_nids = {int(c["nid"]) for c in CARDS if c["kind"] == "compartilhado"}
_viva = _json.loads((HERE / "busca/secoes-viva.json").read_text())
RES_FORA = {}  # nota viva da reserva/AN01 (cópia de nota da seção) que não entra: motivo
EXCLUIDOS = []
for _f in SECOES_DA_AULA:
    for _l in (HERE / "busca/secoes" / _f).read_text().splitlines()[1:]:
        _m = _re.match(r"(\d{13}) \S+ (.*)", _l)
        if not _m:
            continue
        _n, _t = int(_m[1]), _m[2]
        if _n in _used_src:
            continue
        _copias = [int(x) for x in _viva.get(str(_n), [])]
        if any(x in _sh_nids for x in _copias):
            continue
        if _copias:
            EXCLUIDOS.append((_n, f"Cópia NEBLI viva {_copias[0]} decidida na curadoria da reserva e deixada fora: " + _dec.RES_FORA.get(_copias[0], "duplica outra nota mantida ou não é da aula 03 (ver curadoria.py e REVISAO-DE-QUALIDADE.md).")))
            continue
        _mot = _dec.motivo(_n, _t)
        EXCLUIDOS.append((_n, _mot or "PENDENTE"))
EXCLUIDOS += list(_dec.SUSPENSOS_OUTRAS)
EXCLUIDOS = list(dict(EXCLUIDOS).items())

# organizadores autorais: fonte local e trecho literal
_OF = _json.loads((HERE / "organizadores-fontes.json").read_text())
for _c in CARDS:
    if _c["key"] in _OF:
        _c.update(organizacao_fonte=_OF[_c["key"]]["arquivo"], organizacao_trecho=_OF[_c["key"]]["trecho"])
DUPLICACAO = {k: "ganho: organizador recupera o conjunto que a aula lista lado a lado; os IOs e AnKing avulsos cobram cada peça." for k in ("diencefalo-partes-org", "talamo-limites-org", "talamo-nucleos-org", "hipotalamo-limites-org", "hipotalamo-nucleos-org", "subtalamo-limites-org", "lobos-limites-org", "corpo-caloso-partes-org", "face-inferior-org", "corte-horizontal-org", "estriado-org", "capsula-interna-partes-org", "aci-ramos-org", "vertebrobasilar-org", "territorios-org", "willis-org")}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v

FORA_DO_RECORTE = []
VERSO = {}
IMAGENS_VISTAS = {**{k: v["intencao"] for k, v in _json.loads((HERE / "imagens-vistas.json").read_text()).items()}, **IMAGENS_LOCAIS}
REVISAO = {}
ESCOPO = {"objetivo": "Topografia macroscópica do diencéfalo, telencéfalo, núcleos da base e irrigação arterial para localizar estruturas e ligar artéria a território.",
          "centrais": [(r[1], r[1]) for r in _cur.R if r[4] in ("V-pilar", "V-hy") and r[2] not in ("res", "an01")],
          "exemplos": [], "outras_aulas": ["01 Construção morfofuncional", "03 Medula/tronco/nervos cranianos/cerebelo", "06 Meninges, ventrículos e líquor", "08 Sistema límbico", "09 Córtex"]}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))


META["faces-hemisferio"]["duplicacao_ok"] = "O organizador recupera conjuntamente as três faces e a condição de visualização; os IO identificam estruturas, e o AnKing clínico não testa esse conjunto."

for _c in CARDS:
    if _c['key']=='faces-hemisferio': _c['duplicacao_ok'] = META['faces-hemisferio']['duplicacao_ok']
    if _c['key'] in ('ak-1520976098044','ak-1480995205801'): _c['duplicacao_ok'] = 'Resposta vertebral repetida com princípios distintos: estenose subclávia proximal causa reversão de fluxo no primeiro; irrigação do bulbo medial e déficit por oclusão no segundo. Não são a mesma relação.'

from io_tuberculo import construir as _tuberculo_corrigir
_tub_f,_tub_m = _tuberculo_corrigir()
SHARED_FIELDS.setdefault('1792258845028',{}).update(_tub_f)
MEDIA.update(_tub_m)
