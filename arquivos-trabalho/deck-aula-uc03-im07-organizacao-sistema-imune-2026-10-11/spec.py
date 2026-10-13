# Especificação curada — <AULA> (<UC> <Pn>, <componente>; <professor>; <N> lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "<ucNN-curto-AAAAMMDDa>"
SHORT = "<curto>"
LESSON = "2026-<ucNN>-<componente>-<NN>-<slug>"
DECK = "NEBLI::<UC>::<Pn>::<Componente>::<Aula>"
CRITERIOS = "MEMORY.md + FEEDBACKS (último lido) + plano vigente, <data>"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 66 consultas; busca/ext.txt, 20 consultas), tags de seção "
         "FirstAid/Bootcamp/Sketchy de T cells (busca/tags-secao.txt), 10/10: ")
EXCLUIDOS = []  # (nid, motivo) de candidatos lidos e recusados
FORA_DO_RECORTE = []


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_ = "A-<bloco>"
CARDS = [
 # ---------- A. <bloco> (slides x–y) ----------
 # ak("chave", nid, {1: V}, A_, "alvo", slide, "Cor: motivo (slide/prova/HY)."),
 # au("chave", "Frase AnKing com {{c1::termo}}", {1: Z}, A_, "alvo", "slide; fonte", "central|prova|lateral", "o que a busca não achou", [nid1, nid2], "Cor: motivo.", extra="- linha"),
 # sh(nid_nebli, "verde", A_, "alvo", slide, "motivo"),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
DUPLICACAO = {}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
