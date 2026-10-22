"""UC07 por aula do cronograma: aplica o plano de uma aula (seções na ordem da aula) e confere os gates duros.

F-20261022-CLAUDE-09 (“falta de estruturas com card, falta de cards anking, falta de cobertura da aula como um todo /
se baseia na apostila e volta complementando… / preferência para anking + kenhub / quero que o deck seja completo e
siga uma linha de raciocínio / … bandeira de forma correta + consertar os ankihubs que vieram zuados”).

O plano (um módulo Python na corrida, com AULAS = {...}) descreve cada aula em seções, na ordem da aula. Entradas:
  keep    nota que já está na aula (pode trocar figura, texto ou responder comentário)
  kh      cópia de nota do Kenhub (estrutura, referência ou texto) da Referência Externa
  ak      AnKing traduzido para o PT (tipo NEBLI UC07 AnKing v1), com a figura do próprio AnKing
  au      autoral em PT, só com 'busca' (onde se procurou antes) e 'motivo'
  assoc   nota de outra aula da UC07 que esta aula usa (etiqueta, sem duplicar)
e, fora das seções, 'mover' (nota de outra aula do cronograma) e 'retirar' (fora da aula: suspensa, etiquetada e
levada à Reserva histórica). Nada é apagado. Notas novas entram suspensas (F-20261022-CLAUDE-04: Davi dessuspende).

Gates duros (check): plano cobre todas as notas vivas da aula; ordem única e contínua; toda carta com bandeira; uma verde
por estrutura; todo termo do texto da aula em algum card; AnKing traduzido com figura do AnKing (ou escolha explícita);
autoral com busca, motivo, negrito, lacuna não genérica e verso que não repete a frente; nunca passa no vazio.

Uso:
  python3 -m nebli.uc07_aula <plano.py> <aula> [--aplicar]   # sem --aplicar: só mostra o que faria
  python3 -m nebli.uc07_aula <plano.py> <aula> --gates
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import json
import re
import sys
import unicodedata
from pathlib import Path

FLAG = {"verde": 3, "azul": 4, "rosa": 5}
PESSOAIS = {1, 2}
MODELO_TEXTO = "NEBLI UC07 AnKing v1"
RESERVA = "Referências::Referências Externas::Reserva histórica UC07"
RETIRADO = "NEBLI::retirado::uc07-v3"
GENERICOS_PT = {"nervo", "nervos", "estrutura", "estruturas", "função", "funções", "sistema", "célula", "células",
                "neurônio", "neurônios", "fibra", "fibras", "parte", "região", "órgão", "proteína", "tecido"}
VAZIAS = {"para", "pela", "pelo", "pelos", "pelas", "como", "mais", "entre", "sobre", "cada", "esse", "essa", "este",
          "esta", "isso", "onde", "quando", "também", "seus", "suas", "dele", "dela", "porque", "assim"}
CLOZE = re.compile(r"\{\{c(\d+)::(.*?)(?:::.*?)?\}\}", re.S)


def plain(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t or ""))).strip()


def norm(t):
    t = unicodedata.normalize("NFD", plain(CLOZE.sub(lambda m: m.group(2), t or "")).lower())
    return re.sub(r"[^a-z0-9]+", " ", "".join(c for c in t if unicodedata.category(c) != "Mn")).strip()


def imagens(*campos):
    return re.findall(r'<img[^>]+src="([^"]+)"', " ".join(campos))


def carregar(caminho):
    spec = importlib.util.spec_from_file_location("plano_uc07", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.AULAS


def entradas(aula):
    """Entradas em ordem, com o número de ordem e a seção."""
    n = 0
    for s, (titulo, itens) in enumerate(aula["secoes"], 1):
        for e in itens:
            if e["tipo"] == "assoc":
                yield s, titulo, None, e
                continue
            n += 1
            yield s, titulo, n, e


# ---------------------------------------------------------------- gates puros (testáveis sem Anki)

def checar_autoral(e):
    """Problemas de um autoral do plano (F-20261022-CLAUDE-08/09)."""
    p = []
    if not str(e.get("busca", "")).strip() or not str(e.get("motivo", "")).strip():
        p.append("autoral sem 'busca' e 'motivo' (Kenhub e AnKing procurados antes)")
    texto = e.get("text", "")
    if not re.search(r"<b>", CLOZE.sub("", texto)):
        p.append("autoral sem negrito fora da lacuna (sujeito em negrito)")
    lacunas = [plain(m.group(2)).lower().strip(" .") for m in CLOZE.finditer(texto)]
    if not lacunas:
        p.append("autoral sem lacuna")
    gen = [x for x in lacunas if x in GENERICOS_PT]
    if gen:
        p.append(f"lacuna genérica ({', '.join(gen)}): esconder o termo que se decora")
    pal = lambda t: {w for w in norm(t).split() if len(w) > 3 and w not in VAZIAS}
    ext, fre = pal(re.sub(r"<img[^>]*>", "", e.get("extra", ""))), pal(texto)
    if not ext:
        p.append("autoral sem verso: o Extra tem de trazer o porquê ou a consequência")
    elif len(ext) >= 3 and len(ext & fre) / len(ext) >= 0.7:
        p.append("Extra repete a frente: trazer o porquê, a consequência ou o contraste")
    if not e.get("img") and not imagens(e.get("extra", "")):
        p.append("autoral sem figura no Extra (G23)")
    return p


def checar_plano(aula):
    """Gates do plano antes de gravar: cada entrada completa, cores válidas, uma verde por estrutura."""
    p, verdes, vistos = [], {}, set()
    for s, titulo, n, e in entradas(aula):
        t = e["tipo"]
        chave = e.get("nid") or e.get("src") or e.get("chave")
        if t not in ("keep", "kh", "ak", "au", "assoc"):
            p.append(f"{chave}: tipo desconhecido {t}")
        if t != "assoc" and e.get("cor") not in FLAG:
            p.append(f"{chave}: cor ausente ou inválida ({e.get('cor')})")
        if (t, chave) in vistos:
            p.append(f"{chave}: entrada repetida")
        vistos.add((t, chave))
        if t == "au":
            p += [f"{chave}: {x}" for x in checar_autoral(e)]
        if t == "ak" and not (e.get("text") and CLOZE.search(e["text"])):
            p.append(f"{chave}: AnKing traduzido sem texto com lacuna")
        if e.get("est") and e.get("cor") == "verde":
            if e["est"] in verdes:
                p.append(f"estrutura {e['est']}: duas verdes ({verdes[e['est']]} e {chave})")
            verdes[e["est"]] = chave
    if not any(True for _ in entradas(aula)):
        p.append("aula sem entradas (gate nunca passa no vazio)")
    return p


def checar_termos(termos, textos):
    """Termos do texto da aula sem card (textos = frentes/nomes normalizados das notas da aula e associadas)."""
    corpo = " | ".join(textos)
    return [t for t in termos if not any(norm(alt) in corpo for alt in t.split("|"))]


# ---------------------------------------------------------------- Anki

def _anki():
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from nebli.decks import Anki
    return Anki()


def _deck_da_aula(A, aula):
    from nebli.rotulos import canonical
    nomes = {canonical(d) for d in A("deckNames")}
    alvo = [d for d in nomes if d.startswith("NEBLI::UC07::P1::Neuroanatomia::" + aula["prefixo"])]
    if len(alvo) != 1:
        raise SystemExit(f"deck da aula {aula['prefixo']} não encontrado sem ambiguidade: {alvo}")
    return alvo[0]


def _notas_do_deck(A, deck):
    from nebli.rotulos import canonical
    import time
    for _ in range(15):  # logo depois de uma escrita o add-on ainda está renomeando os decks
        real = [d for d in A("deckNames") if canonical(d) == deck]  # fora da escrita o add-on põe a contagem no nome
        if len(real) == 1 and A("findNotes", query=f'"deck:{real[0]}"'):
            break
        time.sleep(2)
    if len(real) != 1:
        raise SystemExit(f"deck {deck}: {len(real)} nomes reais")
    deck = real[0]
    nids = A("findNotes", query=f'"deck:{deck}" -"deck:{deck}::*"')
    return {n["noteId"]: n for n in A("notesInfo", notes=nids)} if nids else {}


def _copias_uc07(A, src):
    return A("findNotes", query=f'"deck:NEBLI*::UC07*" "tag:NEBLI::source::nid-{src}"')


def _campos(n):
    return {k: v["value"] for k, v in n["fields"].items()}


def _trocar_imgs(extra, novas):
    sem = re.sub(r"(<br\s*/?>\s*)*<img[^>]*>(\s*<br\s*/?>)*", "", extra or "").strip()
    figs = "".join(f'<br><br><img src="{f}">' for f in novas)
    return (sem + figs) if sem else figs.removeprefix("<br><br>")


def planejar(A, aula, tag):
    """Traduz o plano em operações concretas contra o estado vivo (sem gravar)."""
    deck = _deck_da_aula(A, aula)
    vivas = _notas_do_deck(A, deck)
    ops, sem_plano = [], set(vivas)
    for s, titulo, n, e in entradas(aula):
        t = e["tipo"]
        if t == "keep":
            if e["nid"] not in vivas:
                raise SystemExit(f"keep {e['nid']}: a nota não está na aula {aula['prefixo']}")
            sem_plano.discard(e["nid"])
            ops.append(dict(e, ordem=n, secao=s, acao="atualizar", nid=e["nid"]))
        elif t == "assoc":
            ops.append(dict(e, secao=s, acao="associar"))
        else:
            existentes = _copias_uc07(A, e["src"]) if t in ("kh", "ak") else \
                A("findNotes", query=f'"deck:NEBLI*::UC07*" "tag:NEBLI::chave::{e["chave"]}"')
            aqui = [x for x in existentes if x in vivas]
            if aqui:
                sem_plano.discard(aqui[0])
                ops.append(dict(e, ordem=n, secao=s, acao="atualizar", nid=aqui[0]))
            elif existentes:
                ops.append(dict(e, secao=s, acao="associar", nid=existentes[0]))
            else:
                ops.append(dict(e, ordem=n, secao=s, acao="criar"))
    for m in aula.get("mover", []):
        sem_plano.discard(m["nid"])
        ops.append(dict(m, acao="mover"))
    for r in aula.get("retirar", []):
        sem_plano.discard(r["nid"])
        ops.append(dict(r, acao="retirar"))
    if sem_plano:
        raise SystemExit(f"GATE plano-cobre-tudo: notas vivas da aula fora do plano: {sorted(sem_plano)}")
    return deck, vivas, ops


def _nota_nova(A, e, deck, tag, run):
    base = ["NEBLI::uc07", f"NEBLI::2026-uc07::{tag}", f"NEBLI::run::{run}", "NEBLI::uc07-aula-v3"]
    if e["tipo"] == "kh":
        src = A("notesInfo", notes=[e["src"]])[0]
        campos = _campos(src)
        if "ID (hidden)" in campos:
            campos["ID (hidden)"] = (campos["ID (hidden)"] or f"kh-{e['src']}") + f"-uc07-aula-{tag}"
        if "NEBLI_Comentario" in campos:
            campos["NEBLI_Comentario"] = ""
        if e.get("img") and "Extra" in campos:
            campos["Extra"] = _trocar_imgs(campos["Extra"], [e["img"]])
        tags = [x for x in src["tags"] if not x.startswith(("NEBLI::referencia-externa", "NEBLI::reserva-historica"))]
        tags += base + [f"NEBLI::source::nid-{e['src']}", "NEBLI::origem::Kenhub"]
        return {"deckName": deck, "modelName": src["modelName"], "fields": campos, "tags": tags,
                "options": {"allowDuplicate": True}}
    if e["tipo"] == "ak":
        src = A("notesInfo", notes=[e["src"]])[0]
        sc = _campos(src)
        figs = e.get("img") or imagens(sc.get("Extra", ""))
        frente_figs = e.get("frente") or imagens(sc.get("Text", ""))
        largura = f' width="{e["largura_frente"]}"' if e.get("largura_frente") else ""
        texto = e["text"] + "".join(f'<br><br><img src="{f}"{largura}>' for f in frente_figs)
        extra = e.get("extra", "") + "".join(f'<br><br><img src="{f}">' for f in figs)
        tags = [x for x in src["tags"] if x.startswith("#AK_")] + base + [
            f"NEBLI::source::nid-{e['src']}", "NEBLI::origem::AnKing", f"NEBLI::chave::nid-{e['src']}"]
        if e.get("img"):
            tags.append("NEBLI::img::escolhida")
        return {"deckName": deck, "modelName": MODELO_TEXTO, "fields": {"Text": texto, "Extra": extra.removeprefix("<br><br>"),
                "ankihub_id": f"-uc07-aula-{tag}"}, "tags": tags, "options": {"allowDuplicate": True}}
    extra = e.get("extra", "") + (f'<br><br><img src="{e["img"]}">' if e.get("img") else "")
    return {"deckName": deck, "modelName": MODELO_TEXTO, "fields": {"Text": e["text"], "Extra": extra},
            "tags": base + ["NEBLI::origem::Autoral", f"NEBLI::chave::{e['chave']}", "NEBLI::img::escolhida"],
            "options": {"allowDuplicate": True}}


def aplicar(caminho, chave, aplicar_de_fato=False):
    from nebli.decks import escrita, em_tela
    from nebli.rotulos import canonical
    aulas = carregar(caminho)
    aula = aulas[chave]
    tag, run = aula["tag"], aula.get("run", "uc07-aula-v3")
    probs = checar_plano(aula)
    if probs:
        raise SystemExit("GATE plano:\n  " + "\n  ".join(probs))
    A = _anki()
    deck, vivas, ops = planejar(A, aula, tag)
    resumo = {k: sum(1 for o in ops if o["acao"] == k) for k in ("atualizar", "criar", "associar", "mover", "retirar")}
    print(json.dumps({"aula": chave, "deck": deck, **resumo}, ensure_ascii=False))
    if not aplicar_de_fato:
        for o in ops:
            if o["acao"] != "atualizar":
                print(f"  {o['acao']:9} {o.get('tipo','')} {o.get('nid') or o.get('src') or o.get('chave')} {plain(o.get('text',''))[:90]}")
        return ops
    tocadas = {o["nid"] for o in ops if o.get("nid")}
    if em_tela(A) & tocadas:
        raise SystemExit("ADIADO SEM ESCRITA: nota desta aula está na tela de Davi")
    rel = {"aula": chave, "criadas": [], "movidas": [], "retiradas": [], "associadas": []}
    with escrita(A, f"UC07 aula {chave} (F-20261022-CLAUDE-09)", sync=False):
        deck = _deck_da_aula(A, aula)
        for o in ops:
            if o["acao"] == "criar":
                spec = _nota_nova(A, o, deck, tag, run)
                nid = A("addNote", note=spec)
                cards = A("findCards", query=f"nid:{nid}")
                A("suspend", cards=cards)
                o["nid"] = nid
                rel["criadas"].append(nid)
        base_due = 7_000_000 + int(chave) * 10_000
        for o in ops:
            nid = o.get("nid")
            if o["acao"] == "associar":
                A("addTags", notes=[nid], tags=f"NEBLI::uc07::assoc::{tag}")
                rel["associadas"].append(nid)
                continue
            if o["acao"] == "mover":
                destino = _deck_da_aula(A, {"prefixo": o["para"]})
                info = A("notesInfo", notes=[nid])[0]
                velhas = [x for x in info["tags"] if x.startswith(("NEBLI::2026-uc07::", "NEBLI::cor::", "NEBLI::ordem::"))]
                if velhas:
                    A("removeTags", notes=[nid], tags=" ".join(velhas))
                A("addTags", notes=[nid], tags=f"NEBLI::2026-uc07::{o['tag_destino']} NEBLI::cor::{o['tag_destino']}::{o.get('cor', 'azul')}")
                A("changeDeck", cards=info["cards"], deck=destino)
                rel["movidas"].append(nid)
                continue
            if o["acao"] == "retirar":
                info = A("notesInfo", notes=[nid])[0]
                velhas = [x for x in info["tags"] if x.startswith(("NEBLI::2026-uc07::", "NEBLI::cor::", "NEBLI::ordem::"))]
                if velhas:
                    A("removeTags", notes=[nid], tags=" ".join(velhas))
                A("addTags", notes=[nid], tags=f"{RETIRADO} NEBLI::retirado::motivo::{re.sub(r'[^a-z0-9]+', '-', norm(o['motivo']))[:60]}")
                A("suspend", cards=info["cards"])
                A("changeDeck", cards=info["cards"], deck=RESERVA)
                rel["retiradas"].append(nid)
                continue
            # atualizar ou recém-criada: campos, etiquetas de ordem/cor, bandeira e posição na fila
            info = A("notesInfo", notes=[nid])[0]
            campos, novos = _campos(info), {}
            if o.get("img") and o["acao"] == "atualizar" and "Extra" in campos:
                novos["Extra"] = _trocar_imgs(o.get("extra_novo", campos["Extra"]), [o["img"]] if isinstance(o["img"], str) else o["img"])
            elif o.get("extra_novo") and o["acao"] == "atualizar":
                novos["Extra"] = o["extra_novo"]
            if o.get("text_novo"):
                novos["Text"] = o["text_novo"]
            if o["tipo"] in ("au", "ak") and o["acao"] == "atualizar":  # o plano é a fonte dos autorais e das traduções
                alvo = _nota_nova(A, o, deck, tag, run)["fields"]
                novos.update({k: v for k, v in alvo.items() if k in ("Text", "Extra") and v != campos.get(k)})
            if o.get("resposta"):
                coment = campos.get("NEBLI_Comentario", "")
                if "CORRIGIDO 22/10/26" not in coment:
                    novos["NEBLI_Comentario"] = f"{coment} CORRIGIDO 22/10/26 (Claude): {o['resposta']}".strip()
            if novos:
                A("updateNoteFields", note={"id": nid, "fields": novos})
            velhas = [x for x in info["tags"] if x.startswith(("NEBLI::ordem::", f"NEBLI::cor::{tag}::", "NEBLI::uc07::secao::"))
                      or x == "NEBLI_comentario::pendente" and o.get("resposta")]
            if velhas:
                A("removeTags", notes=[nid], tags=" ".join(velhas))
            extras = [f"NEBLI::ordem::uc07a-{chave}-{o['ordem']:03d}", f"NEBLI::cor::{tag}::{o['cor']}",
                      f"NEBLI::uc07::secao::{chave}-{o['secao']:02d}", f"NEBLI::2026-uc07::{tag}", "NEBLI::uc07-aula-v3"]
            if o.get("est"):
                extras.append(f"NEBLI::estrutura::{o['est']}")
            if o.get("img"):
                extras.append("NEBLI::img::escolhida")
            A("addTags", notes=[nid], tags=" ".join(extras))
            for c in A("cardsInfo", cards=info["cards"]):
                if c["flags"] not in PESSOAIS and c["flags"] != FLAG[o["cor"]]:
                    A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[FLAG[o["cor"]]], warning_check=True)
                if canonical(c["deckName"]) != deck:
                    A("changeDeck", cards=[c["cardId"]], deck=deck)
                if c["type"] == 0:
                    try:
                        A("setSpecificValueOfCard", card=c["cardId"], keys=["due"], newValues=[base_due + o["ordem"] * 10 + c["ord"]],
                          warning_check=True)
                    except RuntimeError as err:
                        if "protected state" not in str(err):
                            raise
    saida = Path(caminho).parent / f"aplicacao-{chave}.json"
    saida.write_text(json.dumps(rel, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: len(v) if isinstance(v, list) else v for k, v in rel.items()}, ensure_ascii=False))
    return rel


def gates(caminho, chave):
    """Gates duros no estado vivo. Devolve a lista de reprovações (vazia = passou)."""
    aula = carregar(caminho)[chave]
    tag = aula["tag"]
    A = _anki()
    deck = _deck_da_aula(A, aula)
    vivas = _notas_do_deck(A, deck)
    p = [f"[plano] {x}" for x in checar_plano(aula)]
    if not vivas:
        return p + ["[vazio] a aula não tem notas (gate nunca passa no vazio)"]
    ordens, verdes, textos = {}, {}, []
    for nid, n in vivas.items():
        o = [t for t in n["tags"] if t.startswith(f"NEBLI::ordem::uc07a-{chave}-")]
        if len(o) != 1:
            p.append(f"[ordem] {nid}: {len(o)} etiquetas de ordem desta aula (precisa de exatamente 1)")
        else:
            ordens[o[0]] = nid
        cor = [t.rsplit("::", 1)[1] for t in n["tags"] if t.startswith(f"NEBLI::cor::{tag}::")]
        est = [t for t in n["tags"] if t.startswith("NEBLI::estrutura::")]
        if cor == ["verde"]:
            for e in est:
                verdes.setdefault(e, []).append(nid)
        f = _campos(n)
        textos.append(norm(" ".join(f.get(k, "") for k in ("Text", "Nome PT", "Sinonimos", "Pergunta"))))
        if "NEBLI::origem::AnKing" in n["tags"] and n["modelName"] == MODELO_TEXTO and "NEBLI::img::escolhida" not in n["tags"]:
            src = [int(t.rsplit("-", 1)[1]) for t in n["tags"] if t.startswith("NEBLI::source::nid-")]
            if src:
                sinfo = A("notesInfo", notes=src[:1])[0]
                permitidas = set(imagens(*_campos(sinfo).values()))
                fora = [x for x in imagens(f.get("Extra", "")) if x not in permitidas]
                if fora:
                    p.append(f"[figura-ankihub] {nid}: figura que não é do AnKing de origem ({fora[0]}) sem escolha registrada")
    for c in A("cardsInfo", cards=[x for n in vivas.values() for x in n["cards"]]):
        if c["flags"] == 0:
            p.append(f"[bandeira] carta {c['cardId']} (nota {c['note']}) sem bandeira")
    for e, ns in verdes.items():
        if len(ns) > 1:
            p.append(f"[verde-única] {e}: {len(ns)} notas verdes {ns}")
    esperado = 0
    for _, _, n, e in entradas(aula):
        if not n:
            continue
        if e["tipo"] in ("kh", "ak"):  # cópia que já mora em outra aula vira associação, sem posição aqui
            copias = _copias_uc07(A, e["src"])
            if copias and not set(copias) & set(vivas):
                continue
        esperado += 1
    if len(ordens) != esperado:
        p.append(f"[ordem] {len(ordens)} posições vivas para {esperado} planejadas")
    assoc = {e["nid"] for _, _, _, e in entradas(aula) if e["tipo"] == "assoc"}
    assoc |= set(A("findNotes", query=f'"tag:NEBLI::uc07::assoc::{tag}"'))
    for n in A("notesInfo", notes=sorted(assoc)) if assoc else []:
        textos.append(norm(" ".join(_campos(n).get(k, "") for k in ("Text", "Nome PT", "Sinonimos"))))
    falta = checar_termos(aula.get("termos", []), textos)
    p += [f"[termo-sem-card] {t}" for t in falta]
    return p


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("plano")
    ap.add_argument("aula")
    ap.add_argument("--aplicar", action="store_true")
    ap.add_argument("--gates", action="store_true")
    a = ap.parse_args(argv)
    if a.gates:
        p = gates(a.plano, a.aula)
        print("\n".join(p) if p else f"aula {a.aula}: todos os gates duros ok")
        sys.exit(1 if p else 0)
    aplicar(a.plano, a.aula, a.aplicar)


if __name__ == "__main__":
    main()
