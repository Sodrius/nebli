#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gerar_checklist.py -- semeia a checklist-alvo da curadoria a partir da E1.

Passo 1 do metodo de curadoria (CURADORIA-ANKING.md), automatizado. Antes, a
checklist-<slug>.tsv era digitada de memoria -- e por ai vazava recall: conceito
cuja keyword em ingles ninguem digitou nunca era buscado. Aqui a fonte-verdade
e a E1 JA REDIGIDA: o script varre etapa1.typ e extrai os conceitos que a
propria aula marcou como dignos de nota -- #termo-nota[..][..] e #sigla("..",[..])
-- agrupados por PARTE (#parte-title). Cada um vira uma linha pre-preenchida da
checklist, com id estavel (k.n), frase-alvo e um termo de busca em pt. Quando a
sigla/termo traz o ingles embutido ("do ingles *mucosa-associated ...*"), o
ingles ja entra como termo de busca; senao, deixa o marcador <EN?> pra sessao
completar numa passada leve.

NAO substitui o julgamento da sessao: e um ESQUELETO generoso (recall alto) que
a sessao poda, funde e completa com o(s) termo(s) em ingles. Ver passo 1-2 do
metodo. Saida colavel/edit em arquivos-trabalho/checklist-<slug>.tsv.

Uso:
    python flashcards/scripts/gerar_checklist.py <slug>
    python flashcards/scripts/gerar_checklist.py <slug> --print   # so imprime
"""
import argparse
import collections
import os
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ingles costuma vir marcado no corpo da nota: "do ingles *texto ingles*"
_EN_INLINE = re.compile(r"do ingl[eê]s[^*]*\*([^*]+)\*", re.IGNORECASE)
# binomios latinos em italico: _Thermus aquaticus_
_LATIM = re.compile(r"_([A-Z][a-z]+ [a-z]+)_")
_FMT = re.compile(r"[*_`]")


def localizar_etapa1(slug):
    """Mesma cascata do metodo: _par_ -> etapas-anteriores -> serial."""
    candidatos = [
        os.path.join(RAIZ, "typst-build", f"_par_{slug}", "etapa1.typ"),
        os.path.join(RAIZ, "arquivos-trabalho", "etapas-anteriores", slug, "etapa1.typ"),
        os.path.join(RAIZ, "typst-build", "etapa1.typ"),
    ]
    for c in candidatos:
        if os.path.exists(c):
            return c
    return None


def _ler_bracket(texto, i):
    """texto[i] == '['; devolve (conteudo, indice_apos_o_fecho)."""
    assert texto[i] == "["
    prof = 0
    n = len(texto)
    j = i
    while j < n:
        c = texto[j]
        if c == "[":
            prof += 1
        elif c == "]":
            prof -= 1
            if prof == 0:
                return texto[i + 1:j], j + 1
        j += 1
    return texto[i + 1:], n


def segmentar_partes(texto):
    """Devolve [(titulo, corpo)] por PARTE, na ordem do arquivo."""
    marca = "#parte-title("
    pos = [m.start() for m in re.finditer(re.escape(marca), texto)]
    if not pos:
        return [("(sem PARTE declarada)", texto)]
    partes = []
    for k, p in enumerate(pos):
        ini_arg = p + len(marca)
        # titulo = primeira string "..."
        m = re.search(r'"([^"]*)"', texto[ini_arg:ini_arg + 400])
        titulo = m.group(1) if m else f"PARTE {k+1}"
        fim = pos[k + 1] if k + 1 < len(pos) else len(texto)
        partes.append((titulo.strip(), texto[ini_arg:fim]))
    return partes


def _seed_en(definicao):
    """Extrai termo de busca em ingles da definicao, se houver."""
    m = _EN_INLINE.search(definicao)
    if m:
        return _FMT.sub("", m.group(1)).strip()
    return None


def _en_de_chunk(chunk):
    """Se o chunk (ex.: expansao de sigla) ja e ingles (ASCII, >=2 palavras),
    usa como termo de busca EN. 'nucleotide excision repair' -> serve;
    'radiacao ultravioleta B' tem acento -> nao serve."""
    c = _FMT.sub("", chunk).strip()
    if not c or not c.isascii():
        return None
    palavras = [p for p in re.split(r"\s+", c) if p.isalpha()]
    return c if len(palavras) >= 2 else None


def extrair_conceitos(corpo):
    """Extrai conceitos de um corpo de PARTE, na ordem de aparicao.

    Retorna [(frase_pt, termo_pt, termo_en_ou_None)]."""
    conceitos = []
    vistos = set()

    def add(frase, termo_pt, termo_en):
        chave = termo_pt.lower().strip()
        if not chave or chave in vistos:
            return
        vistos.add(chave)
        conceitos.append((frase.strip(), termo_pt.strip(), termo_en))

    # #termo-nota[termo][definicao]
    i = 0
    alvo = "#termo-nota["
    while True:
        j = corpo.find(alvo, i)
        if j == -1:
            break
        termo, apos = _ler_bracket(corpo, j + len(alvo) - 1)
        definicao = ""
        if apos < len(corpo) and corpo[apos] == "[":
            definicao, apos = _ler_bracket(corpo, apos)
        termo_lp = _FMT.sub("", termo).strip()
        frase = termo_lp
        add(frase, termo_lp, _seed_en(definicao))
        i = apos

    # #sigla("SIG", [expansao])
    for m in re.finditer(r'#sigla\("([^"]+)"\s*,\s*\[', corpo):
        sig = m.group(1).strip()
        exp, _ = _ler_bracket(corpo, m.end() - 1)
        # frase = expansao ate o primeiro travessao/virgula
        frase = re.split(r"[—–,]", _FMT.sub("", exp))[0].strip() or sig
        # EN: marcado "do ingles *...*", ou a propria expansao curta se ja e ingles
        en = _seed_en(exp) or _en_de_chunk(frase)
        add(f"{sig} — {frase}", sig, en)

    # binomios latinos (nome de especie): bom termo de busca pt==en
    for m in _LATIM.finditer(corpo):
        nome = m.group(1).strip()
        add(nome, nome, nome)

    return conceitos


def ler_subtopicos_card(slug):
    """Le os subtopicos da Etapa 1 no Tema Card YAML, agrupados por nº de PARTE.

    O Tema Card e a fonte-verdade do ESQUELETO da aula -- o mesmo eixo da regra
    canonica 'todo subtopico da E1 -> >=2 questoes da E2'. Ancorar a checklist
    aqui conserta o recall que vazava quando ela nascia so dos #termo-nota: orgao,
    zona ou etapa que a E1 ensina em prosa mas nao marcou como nota agora entra
    como alvo de cobertura. Retorna {parte_num: [(id, frase)]} ou {} se nao
    achar card/yaml (fallback = comportamento antigo, so termo-notas)."""
    if yaml is None:
        return {}
    card = None
    for nome in (f"tema_card_{slug}.yml", f"tema-card-{slug}.yml"):
        p = os.path.join(RAIZ, "arquivos-trabalho", nome)
        if os.path.exists(p):
            try:
                card = yaml.safe_load(open(p, encoding="utf-8"))
            except Exception:
                card = None
            break
    if not card:
        return {}
    sumario = card.get("sumario", []) or []
    etapa1 = next((et for et in sumario
                   if "etapa 1" in str(et.get("titulo", "")).lower()), None)
    if etapa1 is None:
        etapa1 = next((et for et in sumario if et.get("blocos")), None)
    if not etapa1:
        return {}
    # Os subtopicos reais do Tema Card sao FRASES PURAS, sem prefixo "1.1"
    # (a doc do gerar_main mostrava numerado, mas o dado gravado nao e). Numera
    # por POSICAO: PARTE = indice do bloco (1-based), subtopico = posicao no bloco.
    # Usa o prefixo "N.M" so quando ele de fato existir na frase.
    out = collections.defaultdict(list)
    for k, bloco in enumerate(etapa1.get("blocos", []) or [], 1):
        for n, sub in enumerate(bloco.get("subtopicos", []) or [], 1):
            m = re.match(r"\s*(\d+\.\d+)\s+(.*)", str(sub))
            if m:
                sid, frase = m.group(1), m.group(2).strip()
            else:
                sid, frase = f"{k}.{n}", str(sub).strip()
            out[k].append((sid, frase))
    return dict(out)


def _termos_subtopico(frase):
    """Deriva um termo de busca pt do subtopico + placeholder <EN?> pra sessao
    completar o ingles. Pega as ate 3 palavras 'de conteudo' (>=4 letras)."""
    ws = [w for w in re.findall(r"[A-Za-zÀ-ÿ]+", frase) if len(w) >= 4][:3]
    pt = " ".join(ws) if ws else frase.strip()
    return f"{pt}|<EN?>"


def montar_linhas(partes, card_subs):
    linhas = []
    for k, (titulo, corpo) in enumerate(partes, 1):
        # titulo ja costuma comecar com "PARTE I — ..."; nao duplicar o rotulo
        rot = titulo if re.match(r"(?i)^\s*PARTE\b", titulo) else f"PARTE {k} — {titulo}"
        linhas.append(("#", rot))
        subs = card_subs.get(k, [])
        # 1) subtopicos do Tema Card = esqueleto oficial da aula (UNIDADE de cobertura).
        #    Isto e o conserto do recall: o que a E1 ensina mas nao marcou como
        #    termo-nota (orgao, zona, etapa) agora vira alvo explicito.
        for sid, frase in subs:
            linhas.append((sid, frase, _termos_subtopico(frase)))
        # 2) termo-notas/siglas/binomios = termos de busca ricos (recall EN),
        #    numerados APOS os subtopicos pra nao colidir de id.
        conceitos = extrair_conceitos(corpo)
        n0 = len(subs)
        for n, (frase, termo_pt, termo_en) in enumerate(conceitos, 1):
            cid = f"{k}.{n0 + n}"
            if termo_en and termo_en.lower() != termo_pt.lower():
                termos = f"{termo_pt}|{termo_en}"
            else:
                termos = f"{termo_pt}|<EN?>"
            linhas.append((cid, frase, termos))
        if not subs and not conceitos:
            linhas.append(("#", "  (sem subtopico no Tema Card nem termo-nota; adicionar a mao)"))
    return linhas


def render_tsv(linhas):
    out = []
    out.append("# checklist-alvo semeada da E1 por gerar_checklist.py")
    out.append("# formato: <id>\\t<frase-alvo>\\t<termo_pt|termo_en>")
    out.append("# AJUSTAR: complete os <EN?>, funda/remova conceitos redundantes,")
    out.append("# e acrescente subtopico que a E1 ensina mas nao marcou como termo-nota.")
    for item in linhas:
        if item[0] == "#":
            out.append(f"# {item[1]}")
        else:
            cid, frase, termos = item
            out.append(f"{cid}\t{frase}\t{termos}")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Semeia a checklist-alvo da curadoria a partir da E1.")
    ap.add_argument("slug", help="slug da aula")
    ap.add_argument("--print", dest="imprimir", action="store_true",
                    help="imprime no terminal em vez de gravar")
    args = ap.parse_args()

    etapa1 = localizar_etapa1(args.slug)
    if not etapa1:
        print(f"ERRO: etapa1.typ nao encontrado para '{args.slug}'.", file=sys.stderr)
        print("  procurei em typst-build/_par_<slug>/, arquivos-trabalho/etapas-anteriores/<slug>/, "
              "typst-build/", file=sys.stderr)
        return 2

    texto = open(etapa1, encoding="utf-8").read()
    partes = segmentar_partes(texto)
    card_subs = ler_subtopicos_card(args.slug)
    n_subs = sum(len(v) for v in card_subs.values())
    linhas = montar_linhas(partes, card_subs)
    conceitos = [l for l in linhas if l[0] != "#"]
    en_faltando = sum(1 for l in conceitos if l[2].endswith("<EN?>"))
    tsv = render_tsv(linhas)

    if args.imprimir:
        print(tsv)
    else:
        destino = os.path.join(RAIZ, "arquivos-trabalho", f"checklist-{args.slug}.tsv")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8") as f:
            f.write(tsv)
        print(f"OK: {os.path.relpath(destino, RAIZ)}")
    fonte_subs = f"{n_subs} do Tema Card" if n_subs else "0 do Tema Card (nao achado -- so termo-notas)"
    print(f"  PARTES: {len(partes)} | conceitos semeados: {len(conceitos)} "
          f"({fonte_subs}) | faltando termo EN: {en_faltando}")
    print("  -> revise o .tsv, complete os <EN?> e rode buscar_tags_lote.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
