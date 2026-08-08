#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gerar_checklist.py -- semeia candidatos a conceito a partir da E1.

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
a sessao poda, funde, completa em ingles e classifica como nuclear, supporting
ou no_card. E2 e apenas auditoria opt-in; nao cria alvos de card por default.

Uso:
    python flashcards/scripts/gerar_checklist.py <slug>
    python flashcards/scripts/gerar_checklist.py <slug> --print   # so imprime
    python flashcards/scripts/gerar_checklist.py <slug> --include-e2  # auditoria, não card targets
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


def localizar_etapa(slug, etapa):
    """Mesma cascata do método: _par_ -> etapas-anteriores -> serial."""
    candidatos = [
        os.path.join(RAIZ, "typst-build", f"_par_{slug}", f"etapa{etapa}.typ"),
        os.path.join(RAIZ, "arquivos-trabalho", "etapas-anteriores", slug, f"etapa{etapa}.typ"),
        os.path.join(RAIZ, "typst-build", f"etapa{etapa}.typ"),
    ]
    for c in candidatos:
        if os.path.exists(c):
            return c
    return None


def localizar_etapa1(slug):
    return localizar_etapa(slug, 1)


def localizar_etapa2(slug):
    return localizar_etapa(slug, 2)


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


def extrair_alvos_e2(texto):
    """Semeia alvos auditáveis da E2: termos/siglas e enunciados de questão.

    A E2 não define automaticamente novos fatos para card; ela torna visível o
    que a aula avalia para que cada alvo receba card, justificativa de escopo ou
    seja devolvido à E1. IDs ``E2.n`` evitam parecer que são subtópicos da E1.
    """
    candidatos = []
    for _titulo, corpo in segmentar_partes(texto):
        candidatos.extend(frase for frase, _pt, _en in extrair_conceitos(corpo))
        matches = list(re.finditer(r"#(?:quest[aã]o|pergunta|question)(?:-[\w]+)?\s*\(", corpo, re.I))
        for pos, m in enumerate(matches):
            end = matches[pos + 1].start() if pos + 1 < len(matches) else len(corpo)
            start = corpo.find("[", m.end(), end)
            if start < 0:
                continue
            enunciado, _ = _ler_bracket(corpo, start)
            enunciado = _FMT.sub("", enunciado).strip()
            if enunciado:
                candidatos.append(enunciado)
    vistos, linhas = set(), []
    for frase in candidatos:
        chave = re.sub(r"\s+", " ", frase).casefold().strip()
        if chave and chave not in vistos:
            vistos.add(chave)
            linhas.append((f"E2.{len(linhas) + 1}", frase, _termos_subtopico(frase)))
    return linhas


def render_tsv(linhas, alvos_e2=None):
    out = []
    out.append("# checklist-alvo semeada da E1 por gerar_checklist.py")
    out.append("# formato: <id>\\t<frase-alvo>\\t<termo_pt|termo_en>\\t<card_decision>")
    out.append("# AJUSTAR: complete <EN?>, funda/remova redundancias e troque REVIEW por")
    out.append("# nuclear | supporting | no_card. So nuclear/supporting seguem para busca.")
    for item in linhas:
        if item[0] == "#":
            out.append(f"# {item[1]}")
        else:
            cid, frase, termos = item
            out.append(f"{cid}\t{frase}\t{termos}\tREVIEW")
    if alvos_e2:
        out.append("# E2 — alvos avaliados; cada um exige card, escopo justificado ou retorno à E1")
        for cid, frase, termos in alvos_e2:
            out.append(f"{cid}\t{frase}\t{termos}\tAUDIT_ONLY")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Semeia a checklist-alvo da curadoria a partir da E1.")
    ap.add_argument("slug", help="slug da aula")
    ap.add_argument("--print", dest="imprimir", action="store_true",
                    help="imprime no terminal em vez de gravar")
    ap.add_argument("--include-e2", action="store_true",
                    help="acrescenta alvos da E2 como AUDIT_ONLY; não viram card targets")
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
    etapa2 = localizar_etapa2(args.slug) if args.include_e2 else None
    alvos_e2 = extrair_alvos_e2(open(etapa2, encoding="utf-8").read()) if etapa2 else []
    tsv = render_tsv(linhas, alvos_e2)

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
    if args.include_e2:
        print(f"  E2 audit-only: {len(alvos_e2)} alvos" + ("" if etapa2 else " (etapa2.typ não encontrada)"))
    else:
        print("  E2: não incluída (default; use --include-e2 apenas para auditoria)")
    print("  -> revise o .tsv, classifique REVIEW, complete <EN?> e só então rode buscar_tags_lote.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
