"""Monta, reconcilia e confere o deck final de uma unidade da UC07 (Kenhub + acervos), com gates duros.

Entrada: `itens.json` da coleta (fora do repo) + `curadoria.json` da corrida. O deck vivo é RECONCILIADO: nota que já existe é
atualizada no lugar (mesmo id: histórico, bandeiras pessoais e comentários de Davi preservados — troca de tipo por
`updateNoteModel`), o que falta é criado e o que saiu do plano é apagado (só sem comentário e sem revisão; senão, retirado).

Tipos de card (nebli.kenhub.modelo):
  IO    (NEBLI Kenhub IO v1)   Kenhub (máscara no verde + seta) · Netter (rótulo coberto + seta na linha-guia) ·
                               AnKing “ID” (máscara no ID, nome no mesmo lugar) · nível do tronco (figura inteira é a pergunta)
  Cloze (NEBLI UC07 Cloze v1)  AnatoKing (só o nome em PT; modelo com seta + peça, tudo à vista) · AnKing conceitual traduzido

Gates duros (o comando só termina com sucesso se TODOS passarem; ids em nebli/kenhub/feedbacks.json):
  PRÉ    cobertura 100% · Kenhub primeiro · máscara cobre o verde · nome em PT · mídia do acervo presente ·
         cloze só com o nome, em português · direcionamento (seta/âncora/pergunta) · lacunas originais preservadas
  PÓS    lido do Anki: estruturas cobertas; nada suspenso; bandeiras; histórico (revisões) preservado; comentário em toda nota
  RENDER deck inteiro, frente e verso, PC e celular (nebli.kenhub.render)

Uso: python -m nebli.kenhub.deck <corrida> [--dry-run]
"""
import base64
import json
import os
import re
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from PIL import Image

from nebli.decks import SYNC_PENDENTE, Anki, escrita
from nebli.kenhub import fontes_io, glossario, mascara, modelo
from nebli.kenhub.caminhos import RAIZ
from nebli.rotulos import canonical

TAG_KENHUB = "NEBLI::fonte::kenhub"
FLAG = {"verde": 3, "azul": 4, "rosa": 5}
PESSOAIS = {1, 2}                     # vermelha/laranja: marcas de Davi, nunca sobrescrever
ROOT = Path(__file__).resolve().parents[2]
CLOZE_RE = re.compile(r"\{\{c(\d+)::(.*?)(?:::[^}]*)?\}\}", re.S)
INGLES = re.compile(r"\b(the|of|and|is|are|which|from|with|located|between|nerve|structure)\b", re.I)
SEPARADORES = re.compile(r"\s/\s|;|\s[-–—]\s|:|·")
VERSAO_MIDIA = "8"                    # nome de arquivo novo a cada mudança de desenho (o Anki guarda imagem em cache)


class AnkiPaciente(Anki):
    """Davi está sempre no Anki (F-20261017-CLAUDE-03): se o Anki estiver ocupado, espera em vez de falhar."""

    def __call__(self, action, **params):
        espera = 0.0
        while True:
            try:
                return super().__call__(action, **params)
            except RuntimeError as err:
                msg = str(err)
                ocupado = "lifecycle operation is active" in msg
                editor = "Close the affected editor" in msg   # janela de edição aberta (Davi ou outro executor): esperar fechar
                if not (ocupado or editor) or espera > 300:
                    raise
                if editor and espera == 0:
                    print("Anki com janela de edição aberta: esperando fechar (até 5 min)…", file=sys.stderr, flush=True)
                time.sleep(2 if ocupado else 10)
                espera += 2 if ocupado else 10


def _limpo(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>|&nbsp;", " ", html)).strip()


def _imgs(html):
    return re.findall(r'<img[^>]+src="[^"]+"[^>]*>', html)


def _cor_hy(tags):
    for t in tags:
        m = re.search(r"(\d)-(?:High|Low|Medium|Mid)\w*Yield", t)
        if m:
            return "verde" if m.group(1) in "12" else "azul"
    return "azul"


def _local(campos, media):
    """`src="http://127.0.0.1:<porta>/x"` (sessão antiga do Anki) vira o nome do arquivo local, quando ele existe."""
    def troca(m):
        nome = urllib.parse.unquote(m.group(2))
        return f'{m.group(1)}"{nome}"' if os.path.exists(os.path.join(media, nome)) else m.group(0)
    return {k: re.sub(r'(src=)"http://127\.0\.0\.1:\d+/([^"]+)"', troca, v) for k, v in campos.items()}


def _midia_faltando(html, media):
    return [u for u in re.findall(r'<img[^>]+src="([^"]*)"', html)
            if u and (u.startswith("http") or not os.path.exists(os.path.join(media, urllib.parse.unquote(u))))]


def _ponta_no_fundo(imagem, ponta):
    """Fração de pixels quase brancos em volta da ponta da seta (G13: a seta tem de terminar sobre a anatomia)."""
    a = np.asarray(Image.open(imagem).convert("L")).astype(int)
    x, y = int(ponta[0]), int(ponta[1])
    viz = a[max(0, y - 6):y + 7, max(0, x - 6):x + 7]
    return float((viz > 235).mean()) if viz.size else 1.0


def _fracao_vermelha(imagem):
    """Fração de vermelho saturado na figura: seta vermelha = pouco (0,02–4,5%; cabeça em corte sagital tem língua e músculo vermelhos); região pintada de vermelho = muito."""
    a = np.asarray(Image.open(imagem).convert("RGB")).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return float(((r > 180) & (g < 80) & (b < 80)).mean())


def _chave_txt(t):
    return re.sub(r"[^a-z0-9]+", "", t.lower().translate(str.maketrans("áàâãéêíóôõúç", "aaaaeeiooouc")))


def nome_pt(cur, i):
    return cur.get("nome_pt", {}).get(i["slug"], i["nome_pt"])


# ----------------------------------------------------------------------------------------------------------- plano
def plano(corrida: Path, A):
    cur = json.loads((corrida / "curadoria.json").read_text())
    base = RAIZ / cur["modulo"] / cur["unidade"]
    itens = json.loads((base / "itens.json").read_text())["itens"]
    excluir = cur.get("kenhub_excluir", {})
    media = A("getMediaDirPath")
    problemas, entradas = [], []
    gerados = corrida / "midia"
    gerados.mkdir(exist_ok=True)
    for s in excluir:  # F-20261017-CLAUDE-05: “deixa sempre kenhub como gate-hard” — toda figura do Kenhub entra, sem exceção
        problemas.append(f"[kenhub-sempre] figura do Kenhub excluída ({s}): toda estrutura com figura no Kenhub tem card do Kenhub")

    def depois(slug):
        for n in cur.get("netter", []):
            if n["slug"] == slug:
                yield {**n, "tipo": "netter", "chave": f"netter-{slug}", "cobre": [slug]}
        for a in cur.get("acervo", []):
            if a["apos"] == slug:
                yield {**a, "tipo": "acervo", "chave": f"nid-{a['nid']}"}
        for a in cur.get("anking_io", []):
            if a.get("apos") == slug:
                yield {**a, "tipo": "anking_io", "chave": f"nid-{a['nid']}", "cobre": a.get("cobre", [])}

    # cards de texto/AnKing que tratam de uma estrutura vêm logo depois dos cards dela (F-20261018-CLAUDE-05: “cards que cobram a
    # mesma estrutura têm que vir juntos na ordem da aula”); os que não tratam de estrutura específica ficam no fim
    ancorados, soltos = {}, []
    for a in cur.get("anking", []):
        e = {**a, "tipo": "anking", "chave": f"nid-{a['nid']}", "cobre": a.get("cobre", [])}
        if a.get("estrutura") in {i["slug"] for i in itens}:
            est = a["estrutura"]
        else:
            it = _casar_estrutura(a["text_pt"], base, a.get("estrutura"))
            est = it["slug"] if it else None
        (ancorados.setdefault(est, []) if est else soltos).append(dict(e, estrutura=est))
    for t in cur.get("texto", []):   # fatos da unidade (objetivos, parágrafos, tabela-resumo) que o quiz cobra
        e = {**t, "tipo": "texto", "chave": f"txt-{t['id']}", "cobre": t.get("cobre", [])}
        if t.get("estrutura") in {i["slug"] for i in itens}:   # estrutura dada na curadoria (vale também para as sem figura no Kenhub)
            est = t["estrutura"]
        else:
            it = _casar_estrutura(t["text_pt"], base, t.get("estrutura") if not (t.get("img") or "").startswith("cap:") else None)
            est = it["slug"] if it else None
        (ancorados.setdefault(est, []) if est else soltos).append(dict(e, estrutura=est))
    slugs_itens = {i["slug"] for i in itens}
    for i in itens:
        s = i["slug"]
        if s not in cur["cores"]:
            problemas.append(f"[cobertura] sem cor: {s}")
        if not i.get("sem_figura") and s not in excluir:  # prioridade Kenhub (F-20261017-CLAUDE-02)
            entradas.append({"tipo": "kenhub", "chave": f"kh-{s}", "slug": s, "item": i, "cobre": [s], "estrutura": s})
        for d_ in depois(s):
            entradas.append(dict(d_, estrutura=d_.get("apos") or d_.get("slug") or s))
        entradas.extend(ancorados.get(s, []))
    for a in cur.get("anking_io", []):
        if not a.get("apos"):
            entradas.append({**a, "tipo": "anking_io", "chave": f"nid-{a['nid']}", "cobre": a.get("cobre", []), "estrutura": None})
    for e in soltos:
        entradas.append(e)
    for k, e in enumerate(entradas, 1):
        e["ordem"] = k
    fora = _em_outras_unidades(A, cur["lesson_id"])
    for e in entradas:   # sem duplicata (F-20261017-CLAUDE-05/plano): já tem nota em outra unidade → associar
        if e["chave"] in fora:
            e["associar"] = fora[e["chave"]]
            e["cor"] = cur["cores"].get(e.get("slug") or e.get("apos")) or "azul"
    for e in entradas:
        if e.get("associar"):
            continue
        try:
            _montar(e, cur, base, gerados, media, A)
        except Exception as err:  # o gate pré lista todos os problemas antes de escrever qualquer coisa
            problemas.append(f"[montagem] {e['chave']}: {err}")
    for e in entradas:   # id de card de texto igual ao de outra unidade, com texto diferente: associaria o card errado
        if e["tipo"] == "texto" and e.get("associar"):
            antigo = A("notesInfo", notes=[e["associar"]])[0]["fields"].get("Text", {}).get("value", "")
            norm_ = lambda t: glossario.norm(_limpo(CLOZE_RE.sub(lambda m: m.group(2), t)))
            if norm_(antigo) != norm_(e["text_pt"]):
                problemas.append(f"[chave de texto repetida] {e['chave']}: já existe em outra unidade com outro texto — renomeie o id ou tire o card (duplicata)")
    cobertas = {s for e in entradas for s in e.get("cobre", []) if e.get("campos") or e.get("associar")}
    for i in itens:
        if i["slug"] not in cobertas:
            problemas.append(f"[cobertura] estrutura sem card planejado: {i['slug']} ({i['nome_en']})")
    por_estrutura = {}
    for e in entradas:   # F-20261018-CLAUDE-05: de dois cards da mesma estrutura, só um pode ser bandeira verde (o do Kenhub, que vem primeiro)
        if e.get("estrutura") and not e.get("associar"):
            por_estrutura.setdefault(e["estrutura"], []).append(e)
    for grupo in por_estrutura.values():
        for e in [x for x in grupo if x.get("cor") == "verde"][1:]:
            e["cor"] = "azul"
    problemas += gates_pre(entradas, cur)
    problemas += gate_estruturas(entradas)
    problemas += gate_quiz_texto(base, entradas)
    problemas += modelo.conferir_formato(A)
    return cur, base, itens, entradas, problemas, cobertas


def gate_estruturas(entradas):
    """[G25 estrutura junta] cards da mesma estrutura em sequência na ordem da aula; [G26 uma verde por estrutura] no máximo uma
    bandeira verde por estrutura (F-20261018-CLAUDE-05)."""
    p, posicoes = [], {}
    for e in entradas:
        if e.get("estrutura"):
            posicoes.setdefault(e["estrutura"], []).append(e["ordem"])
    for est, pos in posicoes.items():
        if pos != list(range(pos[0], pos[0] + len(pos))):
            p.append(f"[G25 estrutura junta] {est}: cards da mesma estrutura espalhados na ordem ({pos[:8]})")
    for est in posicoes:
        verdes = [e["chave"] for e in entradas if e.get("estrutura") == est and e.get("cor") == "verde" and not e.get("associar")]
        if len(verdes) > 1:
            p.append(f"[G26 uma verde por estrutura] {est}: {len(verdes)} cards verdes ({verdes[:3]})")
    return p


def _kt(chave):
    """chave do trecho de texto → etiqueta (sem espaço nem dois-pontos)."""
    return re.sub(r"[^a-z0-9]+", "-", chave.lower()).strip("-")


def gate_quiz_texto(base, entradas):
    """[cobertura-quiz] F-20261018-CLAUDE-01: o quiz da unidade tem questões de texto além das estruturas — todo trecho do texto
    de estudo (objetivos, parágrafos, legendas do atlas, tabela-resumo) precisa estar coberto por algum card (`cobre_texto`)."""
    d = json.loads((base / "itens.json").read_text())
    if "texto" not in d:
        return ["[cobertura-quiz] texto da unidade não coletado (rode: venv/bin/python -m nebli.kenhub.coleta_texto)"]
    cob = {k for e in entradas for k in e.get("cobre_texto", []) if e.get("campos") or e.get("associar")}
    desconhecidas = cob - {t["chave"] for t in d["texto"]}
    p = [f"[cobertura-quiz] chave de texto inexistente: {k}" for k in sorted(desconhecidas)]
    p += [f"[cobertura-quiz] trecho sem card: {t['chave']} ({t['en'][:70].replace(chr(10), ' / ')})" for t in d["texto"] if t["chave"] not in cob]
    return p


VERBOS = ("é", "são", "tem", "têm", "contém", "contêm", "transmite", "transmitem", "forma", "formam", "fica", "ficam", "saem", "sai",
          "emergem", "emerge", "divide-se", "dividem-se", "origina-se", "originam-se", "localiza-se", "corresponde", "correspondem",
          "inclui", "incluem", "percorre", "passa", "passam", "levam", "leva", "começa", "termina", "conduz", "regula", "controla",
          "retransmite", "participa", "apresenta", "estende-se", "estendem-se", "inerva", "inervam", "supre", "suprem", "recebe",
          "carrega", "carregam", "fornece", "fornecem", "emite", "emitem", "contêm", "funde-se", "reflete-se", "unem-se", "une-se",
          "relaciona-se", "relacionam-se", "ligam-se", "liga-se", "entram", "entra", "existe", "existem", "ocorre", "ocorrem",
          "lesão", "há", "marcam", "marca", "processa", "monitora", "conecta", "conectam", "descem", "desce", "aloja", "envia",
          "dividem", "divide", "limita", "limitam", "ladeia", "fixa-se", "usam", "fazem", "faz", "atuam", "atua", "mede", "medem")
QUALIFICADORES = ("anterior", "posterior", "superior", "inferior", "medial", "lateral", "ventral", "dorsal", "ipsilateral",
                  "contralateral", "motor", "motora", "sensitivo", "sensitiva", "consciente", "inconsciente")


def _fora_cloze(texto):
    """Trechos do texto fora das lacunas: [(início, fim)]."""
    pos, out = 0, []
    for m in CLOZE_RE.finditer(texto):
        out.append((pos, m.start()))
        pos = m.end()
    out.append((pos, len(texto)))
    return out


def _formatar(texto, e):
    """Formatação AnKing clássica (MEMORY §5: “negrito como no AnKing: 1–2 trechos de contexto/sujeito, sublinhado para qualificador”):
    o sujeito do enunciado em negrito (a menos que a entrada já traga negrito ou ‘negrito’/‘sublinhado’ explícitos)."""
    if "<b>" in texto:
        return texto
    for trecho in e.get("negrito", []):
        texto = texto.replace(trecho, f"<b>{trecho}</b>", 1)
    for trecho in e.get("sublinhado", []):
        texto = texto.replace(trecho, f"<u>{trecho}</u>", 1)
    if "<b>" in texto:
        return texto
    FUNCAO = {"de", "do", "da", "dos", "das", "no", "na", "nos", "nas", "em", "e", "ou", "a", "o", "ao", "aos", "com", "por", "para",
              "que", "como", "um", "uma", "os", "as", "se", "são", "é", "qual", "quais", "quantos", "quantas", "que", "entre"}
    primeira = texto.find("{{")
    antes = texto[:primeira] if primeira > 0 else ""
    # 1) sujeito = trecho antes do primeiro verbo (ou da primeira lacuna), sem artigo
    alvo = None
    ps = antes.split(" ")
    corte = len(ps)
    for k, w in enumerate(ps):
        if re.sub(r"[^\wà-úÀ-Ú-]", "", w).lower() in VERBOS and k > 0:
            corte = k
            break
    PREP = {"de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas", "por", "para", "com", "que"}
    cand = [w for w in ps[:corte] if w]
    for k, w in enumerate(cand):   # núcleo do sujeito: até a primeira preposição/vírgula (“face dorsal da ponte” → “face dorsal”)
        if k >= 1 and (re.sub(r"[^\wà-ú-]", "", w).lower() in PREP or cand[k - 1].endswith(",")):
            cand = cand[:k]
            break
    if corte == len(ps) and len(cand) > 3:
        cand = cand[:3]
    while cand and re.sub(r"[^\wà-ú-]", "", cand[0]).lower() in FUNCAO:
        cand = cand[1:]
    while cand and re.sub(r"[^\wà-ú-]", "", cand[-1]).lower() in FUNCAO:
        cand = cand[:-1]
    if cand and len(cand) <= 7 and not all(re.sub(r"[^\wà-ú-]", "", w).lower() in VERBOS for w in cand):
        alvo = " ".join(cand).strip(" ,.;:")
    if not alvo:   # 2) lacuna logo no início: o contexto está depois dela (primeiro trecho de texto fora das lacunas)
        for a, b in _fora_cloze(texto):
            seg = texto[a:b].strip(" ,.;:?")
            ws = [w for w in seg.split(" ") if w]
            ws2 = []
            for w in ws:
                if re.sub(r"[^\wà-ú-]", "", w).lower() in VERBOS and ws2:
                    break
                ws2.append(w)
            while ws2 and re.sub(r"[^\wà-ú-]", "", ws2[0]).lower() in FUNCAO | set(VERBOS):
                ws2 = ws2[1:]
            while ws2 and re.sub(r"[^\wà-ú-]", "", ws2[-1]).lower() in FUNCAO:
                ws2 = ws2[:-1]
            for k, w in enumerate(ws2):
                if k >= 1 and re.sub(r"[^\wà-ú-]", "", w).lower() in PREP:
                    ws2 = ws2[:k]
                    break
            if ws2 and len(ws2) <= 5:
                alvo = " ".join(ws2).strip(" ,.;:")
                break
    if not alvo:   # 3) última tentativa: primeiro par de palavras de conteúdo fora das lacunas (“nervo periférico”)
        ign = FUNCAO | set(VERBOS) | PREP
        for a, b in _fora_cloze(texto):
            run = []
            for w in texto[a:b].split(" "):
                n = re.sub(r"[^\wà-ú-]", "", w).lower()
                if n and n not in ign and len(n) > 3 and not n[0].isdigit():
                    run.append(w.strip(" ,.;:?()"))
                    if len(run) == 2 or w.endswith((",", ".")):
                        break
                elif run:
                    break
            if run:
                alvo = " ".join(run)
                break
    if alvo and "{{" not in alvo and alvo in texto:
        ini = texto.find(alvo)
        suj = " ".join(f"<u>{w}</u>" if re.sub(r"[^\wà-ú]", "", w).lower() in QUALIFICADORES else w for w in alvo.split(" "))
        texto = texto[:ini] + f"<b>{suj}</b>" + texto[ini + len(alvo):]
    return texto


GENERICAS = {"medula", "espinal", "nervo", "tronco", "encefalico", "parte", "cerebral", "sistema", "nervoso", "do", "da", "de", "dos", "das"}
_ITENS = {}


def _explicacoes(texto_pt, extra):
    """Termo técnico pouco comum no enunciado → explicação curta no Extra (F-20261018-CLAUDE-05: “pode ter no comentário alguma
    informação dessa área, tipo o que é somestésica”). Lista em glossario_explicacoes.json."""
    tabela = json.loads((Path(__file__).with_name("glossario_explicacoes.json")).read_text())
    alvo = " " + glossario.norm(_limpo(CLOZE_RE.sub(lambda m: m.group(2), texto_pt))) + " "
    linhas = []
    for termo, exp in tabela.items():
        if f" {glossario.norm(termo)} " in alvo and exp not in extra and exp not in linhas:
            linhas.append(exp)
    return extra + "".join(f"<br>- {x}" for x in linhas) if linhas else extra



def _itens(base):
    return _ITENS.setdefault(str(base), json.loads((base / "itens.json").read_text()))


def _casar_estrutura(texto_pt, base, forca=None):
    """Estrutura do Kenhub de que o card de texto trata (nome da estrutura no enunciado), ou None."""
    texto = glossario.norm(_limpo(CLOZE_RE.sub(lambda m: m.group(2), texto_pt)))
    escolha, melhor = None, 0
    for i in _itens(base)["itens"]:
        if i.get("sem_figura") or not i.get("nome_pt"):
            continue
        if forca and i["slug"] != forca:
            continue
        nome = glossario.norm(i["nome_pt"])
        especificas = set(nome.split()) - GENERICAS
        casa = nome and f" {nome} " in f" {texto} "
        if not casa and especificas and especificas <= set(texto.split()) and (len(especificas) >= 2 or max(map(len, especificas)) >= 8):
            casa = True   # “núcleo marginal” no enunciado ↔ “Núcleo marginal da medula espinal”
        if forca or (casa and len(nome) > melhor):
            escolha, melhor = i, len(nome)
    return escolha


def _imagem_texto(e, base):
    """Figura do Extra do card de texto (“IMAGEM NO CLOZE”, F-20261018-CLAUDE-04): a figura do Kenhub da estrutura de que o card trata
    (nome da estrutura no enunciado), ou a do atlas da unidade; `img` na curadoria força (slug de estrutura ou `cap:<id>`)."""
    d = _itens(base)
    forca = e.get("img")
    escolha = _casar_estrutura(e["text_pt"], base, None if (forca or "").startswith("cap:") else (forca or e.get("estrutura")))
    if escolha:
        return f"kh-{escolha['slug']}.jpg", base / escolha["arquivo"]
    texto = glossario.norm(_limpo(CLOZE_RE.sub(lambda m: m.group(2), e["text_pt"])))
    caps = [c for c in d.get("overview", []) if (c["id"] and (not forca or forca == f"cap:{c['id']}"))]
    if caps:
        palavras = set(texto.split())
        caps.sort(key=lambda c: -len(palavras & set(glossario.norm(c["title"]).split())))
        return f"kh-cap-{caps[0]['id']}.jpg", base / caps[0]["arquivo"]
    raise ValueError("card de texto sem figura (nem estrutura no enunciado, nem figura do atlas): coletar `overview` ou informar `img`")


def _overlay_arquivos(e, gerados, q, r, meta):
    nq, nr = f"u7-{e['chave']}-Q{VERSAO_MIDIA}.png", f"u7-{e['chave']}-R{VERSAO_MIDIA}.png"
    (gerados / nq).write_bytes(q)
    (gerados / nr).write_bytes(r)
    e["midia"].update({nq: gerados / nq, nr: gerados / nr})
    e["meta"] = meta
    return nq, nr


def _montar(e, cur, base, gerados, media, A):
    """Preenche e['campos'], e['modelo'], e['midia'], e['cor'], e['meta'] (sem escrever no Anki)."""
    e["midia"] = {}
    cor = lambda s: cur["cores"].get(s, "azul")
    if e["tipo"] == "kenhub":
        i, s = e["item"], e["slug"]
        arq = base / i["arquivo"]
        m = mascara.regiao(str(arq))
        # F-20261018-CLAUDE-04: sem IO nas estruturas — o Kenhub já destaca a estrutura em verde; basta a seta (frente) e o nome na ponta (verso)
        q, r, meta = mascara.overlays(Image.open(arq).size, m, nome_pt(cur, i), cobrir=False)
        meta["ponta_fundo"] = _ponta_no_fundo(str(arq), meta["ponta"])
        nq, nr = _overlay_arquivos(e, gerados, q, r, meta)
        img = f"kh-{s}.jpg"
        e["midia"][img] = arq
        e.update(modelo=modelo.NOME, cor=cor(s), fonte="Kenhub", base_frente=str(arq), campos={
            "Nome PT": nome_pt(cur, i), "Latim": i.get("latim") or "", "Nome EN": i["nome_en"],
            "Sinonimos": "; ".join(x for x in (i.get("sinonimos_pt") or []) if x), "Imagem": f'<img src="{img}">',
            "MascaraP": f'<img src="{nq}">', "MascaraR": f'<img src="{nr}">', "Pergunta": "", "Fonte": "", "Extra": "",
            "ID (hidden)": f"nebli-{cur['lesson_id']}-{s}"})
    elif e["tipo"] == "netter":
        img = f"u7-{e['chave']}.jpg"
        arq = gerados / img
        m, ponta, cauda = fontes_io.netter(e["pagina"], e["rotulo"], str(arq))
        q, r, meta = mascara.overlays(Image.open(arq).size, m, e["pt"], ponta=ponta, cauda=cauda)
        meta["guia"] = True
        meta["ponta_fundo"] = _ponta_no_fundo(str(arq), meta["ponta"])
        nq, nr = _overlay_arquivos(e, gerados, q, r, meta)
        e["midia"][img] = arq
        e.update(modelo=modelo.NOME, cor=cor(e["slug"]), fonte="Netter", base_frente=str(arq), campos={
            "Nome PT": e["pt"], "Latim": "", "Nome EN": e["rotulo"], "Sinonimos": "", "Imagem": f'<img src="{img}">',
            "MascaraP": f'<img src="{nq}">', "MascaraR": f'<img src="{nr}">', "Pergunta": "",
            "Fonte": "", "Extra": "", "ID (hidden)": f"nebli-{cur['lesson_id']}-{e['chave']}"})
    elif e["tipo"] == "anking_io":
        src = A("notesInfo", notes=[e["nid"]])[0]
        campos = _local({k: v["value"] for k, v in src["fields"].items()}, media)
        figs = re.findall(r'<img[^>]+src="([^"]+)"', campos["Text"])
        if not figs:
            raise ValueError("card do AnKing sem figura no Text")
        c1 = CLOZE_RE.search(campos["Text"])
        en = _limpo(c1.group(2)) if c1 else ""
        figs = [urllib.parse.unquote(f) for f in figs]
        if e.get("pergunta") and len(figs) > 1:
            # nível do tronco: a figura da frente é a SEM legenda (a legendada entrega a resposta e vai para o verso)
            figs.sort(key=lambda f: len(" ".join(fontes_io.textos(os.path.join(media, f)))))
        fig = figs[0]
        caminho = os.path.join(media, fig)
        # F-20261017-CLAUDE-05: uma figura por card — imagens que o card não usa saem; no nível, a legendada é a resposta (verso)
        extra_imgs = "".join(f'<img src="{f}">' for f in figs[1:]) if e.get("pergunta") else ""
        extra = (e.get("extra_pt", "") + ("<br>" if e.get("extra_pt") and extra_imgs else "") + extra_imgs).strip()
        nq = nr = ""
        if e.get("pergunta"):
            e["meta"] = {"pergunta": e["pergunta"]}
        else:
            caixa = fontes_io.rotulo_id(caminho)
            if not caixa:
                raise ValueError("“ID” não encontrado na figura (reconhecimento de texto)")
            im = Image.open(caminho)
            m = np.zeros((im.height, im.width), bool)
            x0, y0, x1, y1 = map(int, caixa)
            m[max(0, y0 - 3):y1 + 4, max(0, x0 - 3):x1 + 4] = True
            q, r, meta = mascara.overlays(im.size, m, e["pt"], ancora=((x0 + x1) / 2, (y0 + y1) / 2))
            nq, nr = _overlay_arquivos(e, gerados, q, r, meta)
        e.update(modelo=modelo.NOME, cor=cur["cores"].get(e.get("apos")) or _cor_hy(src["tags"]), fonte="AnKing",
                 tags_origem=src["tags"], base_frente=caminho, campos={
                     "Nome PT": e["pt"], "Latim": "", "Nome EN": en.split(" - ")[0], "Sinonimos": "",
                     "Imagem": f'<img src="{fig}">', "MascaraP": f'<img src="{nq}">' if nq else "",
                     "MascaraR": f'<img src="{nr}">' if nr else "", "Pergunta": e.get("pergunta", ""), "Fonte": "",
                     "Extra": extra, "ID (hidden)": f"nebli-{cur['lesson_id']}-{e['chave']}"})
        e["falta_midia"] = [u for u in _midia_faltando(" ".join(e["campos"].values()), media) if u not in e["midia"]]
    elif e["tipo"] == "acervo":  # AnatoKing → cloze só com o nome em PT, modelo (seta) + peça à vista
        src = A("notesInfo", notes=[e["nid"]])[0]
        campos = _local({k: v["value"] for k, v in src["fields"].items()}, media)
        if not src["modelName"].startswith("AnatoKing"):
            raise ValueError(f"acervo de tipo inesperado: {src['modelName']}")
        if not _imgs(campos.get("Model", "")):
            raise ValueError("AnatoKing sem figura de modelo (sem seta): não há direcionamento")
        modelos = _imgs(campos.get("Model", ""))
        imagens = modelos[0]   # uma figura na frente: o modelo com a seta vermelha (bater o olho e saber onde está)
        arq_modelo = os.path.join(media, urllib.parse.unquote(re.search(r'src="([^"]+)"', imagens).group(1)))
        e["vermelho_modelo"] = _fracao_vermelha(arq_modelo) if os.path.exists(arq_modelo) else 0.0
        nome_modelo = urllib.parse.unquote(re.search(r'src="([^"]+)"', imagens).group(1))
        # figura genérica (a mesma foto numerada serve a vários cards do AnatoKing) não aponta a estrutura deste card
        e["usos_modelo"] = len(A("findNotes", query=f'"deck:Referências::Referências Externas::AnatoKing" "Model:*{nome_modelo}*"'))
        e["base_frente_cloze"] = arq_modelo
        verso = ""   # F-20261018-CLAUDE-01 (“faltou tirar uma image”): uma só figura no card; peça/imagem de apoio não entra
        en = _limpo(CLOZE_RE.search(campos["Text"]).group(2)).split(" / ")[0]
        e.update(modelo=modelo.CLOZE, cor=cor(e["apos"]), fonte="AnatoKing", tags_origem=src["tags"], campos={
            "Text": f"Qual estrutura a seta indica? {{{{c1::{e['pt']}}}}}", "Imagens": imagens, "Extra": verso,
            "Nome EN": en, "Fonte": "", "ID (hidden)": f"nebli-{cur['lesson_id']}-{e['chave']}"})
        e["falta_midia"] = _midia_faltando(imagens + verso, media)
    elif e["tipo"] == "anking":  # AnKing conceitual, traduzido; só o nome no cloze
        src = A("notesInfo", notes=[e["nid"]])[0]
        campos = _local({k: v["value"] for k, v in src["fields"].items()}, media)
        imgs = "".join(_imgs(campos.get("Extra", "")))
        if not imgs:   # F-20261018-CLAUDE-04 “IMAGEM NO CLOZE”: AnKing sem figura no Extra ganha a figura do Kenhub da estrutura / do atlas
            img, arq_img = _imagem_texto(e, base)
            e["midia"][img] = arq_img
            imgs = f'<img src="{img}">'
        txt_extra = _explicacoes(e["text_pt"], e.get("extra_pt", ""))
        txt_extra = txt_extra[4:] if txt_extra.startswith("<br>") else txt_extra
        extra = (txt_extra + ("<br><br>" if txt_extra and imgs else "") + imgs).strip()
        e.update(modelo=modelo.CLOZE, cor=_cor_hy(src["tags"]), fonte="AnKing", tags_origem=src["tags"], campos={
            "Text": _formatar(e["text_pt"], e), "Imagens": "", "Extra": extra, "Nome EN": _limpo(CLOZE_RE.sub(lambda m: m.group(2), campos["Text"])), "Fonte": "",
            "ID (hidden)": f"nebli-{cur['lesson_id']}-{e['chave']}"})
        e["falta_midia"] = [u for u in _midia_faltando(extra, media) if u not in e["midia"]]
        e["clozes_origem"] = sorted({int(n) for n, _ in CLOZE_RE.findall(campos["Text"])})
    elif e["tipo"] == "texto":   # fato do texto de estudo do Kenhub, em PT, cloze curto, formatação AnKing, figura no Extra
        img, arq_img = _imagem_texto(e, base)
        e["midia"][img] = arq_img
        txt_extra = _explicacoes(e["text_pt"], e.get("extra_pt", ""))
        txt_extra = txt_extra[4:] if txt_extra.startswith("<br>") else txt_extra
        extra = (txt_extra + "<br><br>" if txt_extra else "") + f'<img src="{img}">'
        e.update(modelo=modelo.CLOZE, cor=cur.get("cor_texto", "azul"), fonte="Kenhub", tags_origem=[], campos={
            "Text": _formatar(e["text_pt"], e), "Imagens": "", "Extra": extra, "Nome EN": e.get("en", ""), "Fonte": "",
            "ID (hidden)": f"nebli-{cur['lesson_id']}-{e['chave']}"})
        e["falta_midia"] = []
    else:
        raise ValueError(f"tipo de entrada desconhecido: {e['tipo']!r}")
    if e.get("base_frente_cloze"):
        e["ocr_frente"] = fontes_io.textos(e["base_frente_cloze"])
    if e.get("modelo") == modelo.NOME and e.get("base_frente"):
        frente = Image.open(e["base_frente"]).convert("RGBA")
        mq = e["campos"]["MascaraP"]
        if mq:
            nome_q = re.search(r'src="([^"]+)"', mq).group(1)
            sobre = Image.open(e["midia"][nome_q]).convert("RGBA")
            frente = Image.alpha_composite(frente, sobre.resize(frente.size, Image.LANCZOS) if sobre.size != frente.size else sobre)
        e["ocr_frente"] = fontes_io.textos(frente)


# ----------------------------------------------------------------------------------------------------------- gates
def gates_pre(entradas, cur):
    p = []
    for e in entradas:
        if e.get("associar"):
            continue
        if "campos" not in e:   # nunca passar no vazio: entrada que não montou reprova
            p.append(f"[montagem] {e['chave']}: entrada sem campos montados (tipo {e['tipo']!r})")
            continue
        k = e["chave"]
        if any(CLOZE_RE.search(v) for kk, v in e["campos"].items() if kk != "Text"):   # o Anki recusa a nota (“unknown reason”)
            p.append(f"[montagem] {k}: marcação de cloze fora do campo Text")
        if e["campos"].get("Fonte"):
            p.append(f"[G14 sem fonte] {k}: campo Fonte preenchido ({e['campos']['Fonte'][:30]!r})")
        if e.get("falta_midia"):
            p.append(f"[G4 mídia] {k}: {len(e['falta_midia'])} imagem(ns) ausente(s) na mídia (ex.: {e['falta_midia'][0][:40]})")
        if e["modelo"] == modelo.NOME:
            nome = e["campos"]["Nome PT"]
            if SEPARADORES.search(nome) or len(nome.split()) > 8:
                p.append(f"[G8 só o nome] {k}: nome {nome!r} não é só o nome")
            if INGLES.search(nome):
                p.append(f"[G8 português] {k}: nome {nome!r} parece inglês")
            if e["tipo"] == "kenhub" and nome.strip().lower() == e["item"]["nome_en"].strip().lower() \
                    and e["slug"] not in cur.get("nome_igual_ok", []):
                p.append(f"[G8 português] {k}: nome em PT igual ao inglês (traduzir em 'nome_pt')")
            meta = e.get("meta", {})
            if e["tipo"] == "kenhub":
                w_, h_ = Image.open(e["base_frente"]).size
                if meta.get("comprimento_seta", 0) < 0.04 * (w_ * w_ + h_ * h_) ** 0.5:
                    p.append(f"[G17 seta evidente] {k}: seta curta demais para se ver de relance ({meta.get('comprimento_seta', 0):.0f} px)")
                if not (meta.get("seta") and meta.get("ponta_na_mascara")):
                    p.append(f"[G10 direcionamento] {k}: seta ausente ou não toca a estrutura (verde)")
                if meta.get("retangulos") or meta.get("formas"):
                    p.append(f"[G21 sem IO nas estruturas] {k}: o card do Kenhub não leva máscara sobre a estrutura")
            elif e["tipo"] == "netter" and not (meta.get("seta") and meta.get("guia")):
                p.append(f"[G10 direcionamento] {k}: seta não segue a linha-guia")
            elif e["tipo"] == "anking_io" and not (meta.get("ancora") or meta.get("pergunta")):
                p.append(f"[G10 direcionamento] {k}: sem âncora no “ID” nem pergunta")
            if e["tipo"] in ("netter", "anking_io") and not glossario.atestado(nome):
                p.append(f"[G18 tradução oficial] {k}: nome {nome!r} não consta no Kenhub PT nem no Machado (confirme em fonte oficial e ajuste)")
            if e["tipo"] == "netter" and meta.get("ponta_fundo", 0) > 0.6:   # no Kenhub a seta encosta na máscara (G10)
                p.append(f"[G13 seta na anatomia] {k}: a ponta da seta cai no fundo ({meta['ponta_fundo']:.0%} branco)")
            # G12: a frente, como aparece (figura + máscara), não pode mostrar a resposta (lida pelo reconhecimento de texto)
            lido = _chave_txt(" ".join(e.get("ocr_frente", [])))
            for resp in (e["campos"]["Nome PT"], e["campos"].get("Nome EN", "")):
                palavras = [w for w in re.findall(r"[a-zà-ú]{4,}", resp.lower())]
                if palavras and all(_chave_txt(w) in lido for w in palavras):
                    p.append(f"[G12 resposta vazada] {k}: a frente mostra {resp!r}")
        else:
            texto = e["campos"]["Text"]
            clozes = CLOZE_RE.findall(texto)
            if not clozes:
                p.append(f"[G8] {k}: cloze sem lacuna")
            for _, resp in clozes:
                r = _limpo(resp)
                if SEPARADORES.search(r) or len(r.split()) > 4:
                    p.append(f"[G8 só o nome] {k}: cloze {r!r} tem mais que o nome")
            if INGLES.search(_limpo(CLOZE_RE.sub(lambda m: m.group(2), texto))):
                p.append(f"[G8 português] {k}: texto do cloze parece inglês")
            if e["tipo"] in ("anking", "texto"):   # formatação AnKing clássica: sujeito em negrito, poucos trechos, nada de negrito nas lacunas
                fora = "".join(e["campos"]["Text"][a:b] for a, b in _fora_cloze(e["campos"]["Text"]))
                negritos = re.findall(r"<b>", fora)
                if not 1 <= len(negritos) <= 3:
                    p.append(f"[G22 formatação AnKing] {k}: {len(negritos)} trechos em negrito fora da lacuna (esperado 1 a 3: sujeito/contexto)")
            if e["tipo"] in ("texto", "anking") and "<img" not in e["campos"].get("Extra", ""):
                p.append(f"[G23 imagem no cloze] {k}: card de texto sem figura no Extra")
            if e["tipo"] == "acervo" and (len(_imgs(e["campos"]["Imagens"] + e["campos"].get("Extra", ""))) != 1):
                p.append(f"[G20 uma figura] {k}: o card do AnatoKing deve ter uma só figura (tem {len(_imgs(e['campos']['Imagens'] + e['campos'].get('Extra', '')))})")
            for _, resp in clozes:   # G18: tradução oficial — o termo precisa estar no Kenhub PT ou no Machado
                if e["tipo"] in ("anking", "texto", "acervo") and not glossario.atestado(_limpo(resp)):
                    p.append(f"[G18 tradução oficial] {k}: termo {_limpo(resp)!r} não consta no Kenhub PT nem no Machado (confirme em fonte oficial e ajuste)")
            if e["tipo"] == "anking":
                nov = sorted({int(n) for n, _ in clozes})
                if nov != e.get("clozes_origem"):
                    p.append(f"[histórico] {k}: lacunas {nov} != originais {e.get('clozes_origem')} (cards se perderiam)")
            if e["tipo"] == "acervo" and e.get("seta_ok") is not True:   # “seta ruim”: seta fina/preta/apagada reprova; só entra com a seta conferida à vista
                p.append(f"[G10 seta evidente] {k}: seta do AnatoKing não conferida (seta_ok) — só entra figura com seta evidente")
            if e["tipo"] in ("anking", "texto"):
                falta = [x for x in json.loads(Path(__file__).with_name("glossario_explicacoes.json").read_text()).items()
                         if f" {glossario.norm(x[0])} " in " " + glossario.norm(_limpo(CLOZE_RE.sub(lambda m: m.group(2), e["campos"]["Text"]))) + " "
                         and x[1] not in re.sub(r"<[^>]+>", " ", e["campos"].get("Extra", "")).replace("  ", " ") and x[1] not in e["campos"].get("Extra", "")]
                for termo, _ in falta:
                    p.append(f"[G27 termo explicado] {k}: o termo {termo!r} não está explicado no Extra")
            if e["tipo"] == "acervo" and not e["campos"]["Imagens"]:
                p.append(f"[G10 direcionamento] {k}: AnatoKing sem imagens")
            if e["tipo"] == "acervo" and e.get("usos_modelo", 1) > 1:
                p.append(f"[G10 direcionamento] {k}: figura do modelo é genérica (a mesma em {e['usos_modelo']} cards do AnatoKing) — não aponta esta estrutura")
            if e["tipo"] == "acervo" and not (0.0001 <= e.get("vermelho_modelo", 0) <= 0.045):
                p.append(f"[G10 direcionamento] {k}: figura do modelo sem seta vermelha (vermelho {e.get('vermelho_modelo', 0):.2%})")
            if e["tipo"] == "acervo":   # G12 também no cloze: a figura da frente não pode trazer a resposta escrita (legenda)
                lido = _chave_txt(" ".join(e.get("ocr_frente", [])))
                for resp in (e.get("pt", ""), e["campos"].get("Nome EN", "")):
                    palavras = re.findall(r"[a-zà-ú]{4,}", resp.lower())
                    if palavras and all(_chave_txt(w) in lido for w in palavras):
                        p.append(f"[G12 resposta vazada] {k}: a figura da frente mostra {resp!r}")
    return p


def pode_gravar_bandeira(A):
    """O AnkiConnect recusa gravar em card com qualquer editor aberto. Testa antes de escrever: regrava, com o mesmo valor, a
    bandeira de uma carta de referência (AnatoKing, que não é de estudo de Davi); nada muda se passar."""
    ids = A("findCards", query='"deck:Referências::Referências Externas::AnatoKing"')[:1]
    if not ids:
        return True
    atual = A("cardsInfo", cards=ids)[0]["flags"]
    try:
        A("setSpecificValueOfCard", card=ids[0], keys=["flags"], newValues=[atual], warning_check=True)
    except RuntimeError as err:
        if "editor" in str(err).lower():
            return False
        raise
    return True


def _faixa(short):
    cfg_path = ROOT / "config" / "fila-novos.json"
    cfg = json.loads(cfg_path.read_text())
    if short not in cfg["faixas"]:
        cfg["faixas"][short] = max(cfg["faixas"].values(), default=0) + 20000
        cfg_path.write_text(json.dumps(cfg, indent=1))
    return cfg["faixas"][short]


def _chaves_nota(n):
    out = [t.split("::", 2)[2] for t in n["tags"] if t.startswith("NEBLI::chave::")]
    if TAG_KENHUB in n["tags"] and not out:   # notas antigas sem etiqueta de chave; as novas (texto/AnKing) também levam “estrutura” e não são a figura
        out += [f"kh-{t.split('::')[-1]}" for t in n["tags"] if t.startswith("NEBLI::estrutura::")]
    out += [f"nid-{t.split('-')[-1]}" for t in n["tags"] if t.startswith("NEBLI::source::nid-")]
    return out


def _em_outras_unidades(A, lesson):
    """chave → nota da UC07 que já existe em OUTRA unidade (a mesma figura/nota não vira card repetido: é associada)."""
    out = {}
    q = '"tag:NEBLI::uc07" -"tag:NEBLI::retirado::*"'
    for n in A("notesInfo", notes=A("findNotes", query=q)):
        # “desta unidade” = tem a etiqueta da unidade SEM a marca de associação; associada a ela continua sendo de outra
        if f"NEBLI::{lesson}" in n["tags"] and f"NEBLI::uc07::assoc::{lesson}" not in n["tags"]:
            continue
        for k in _chaves_nota(n):
            out.setdefault(k, n["noteId"])
    return out


def _existentes(A, lesson_tag):
    """chave → nota existente (pela etiqueta de chave; nas notas antigas, pela estrutura do Kenhub ou pela nota de origem)."""
    out = {}
    lesson = lesson_tag.split("::", 1)[1]
    for n in A("notesInfo", notes=A("findNotes", query=f'"tag:{lesson_tag}"')):
        if f"NEBLI::uc07::assoc::{lesson}" in n["tags"]:
            continue
        chave = next((t.split("::", 2)[2] for t in n["tags"] if t.startswith("NEBLI::chave::")), None)
        if not chave and TAG_KENHUB in n["tags"]:
            chave = next((f"kh-{t.split('::')[-1]}" for t in n["tags"] if t.startswith("NEBLI::estrutura::")), None)
        if not chave:
            chave = next((f"nid-{t.split('-')[-1]}" for t in n["tags"] if t.startswith("NEBLI::source::nid-")), None)
        if chave:
            out[chave] = n
    return out


def _campos_modelo(e):
    """Campos como o Anki os guarda. Cloze = tipo AnKing (clone do NEBLI AnKing independente): figura da frente vai dentro do Text,
    como nos cards do AnKing; os demais campos do AnKing ficam vazios."""
    c = e["campos"]
    if e["modelo"] != modelo.CLOZE:
        return dict(c)
    texto = c["Text"] + (f"<br><br>{c['Imagens']}" if c.get("Imagens") else "")
    return {f: "" for f in modelo.CLOZE_CAMPOS} | {"Text": texto, "Extra": c.get("Extra", "")}


def instalar(A, cur, entradas):
    deck, lesson = cur["deck"], cur["lesson_id"]
    lesson_tag = f"NEBLI::{lesson}"
    run = "uc07-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M")
    faixa = _faixa(cur["short"])
    resultados, recusados, antes = [], [], {}
    with escrita(A, f"{cur['short'].upper()} {run}", sync=False):   # sem sync aqui: Davi está estudando (F-20261018-CLAUDE-04)
        modelo.garantir(A)
        existentes = _existentes(A, lesson_tag)
        for n in existentes.values():
            antes[n["noteId"]] = {c["cardId"]: c["reps"] for c in A("cardsInfo", cards=n["cards"])}
        A("createDeck", deck=deck)
        root = A("getDeckConfig", deck="NEBLI")
        chain = ["::".join(deck.split("::")[:k]) for k in range(2, deck.count("::") + 2)]
        wrong = [d for d in chain if A("getDeckConfig", deck=d)["id"] != root["id"]]
        if wrong:
            A("setDeckConfigId", decks=wrong, configId=root["id"])
        planejadas = set()
        for e in entradas:
            if e.get("associar"):
                nid = e["associar"]
                n = A("notesInfo", notes=[nid])[0]
                velhas = [t for t in n["tags"] if t.startswith(f"NEBLI::ordem::{cur['short']}-") or t.startswith(f"NEBLI::cor::{lesson}::")]
                if velhas:
                    A("removeTags", notes=[nid], tags=" ".join(velhas))
                A("addTags", notes=[nid], tags=" ".join([lesson_tag, f"NEBLI::ordem::{cur['short']}-{e['ordem']:03d}",
                                                          f"NEBLI::uc07::assoc::{lesson}", f"NEBLI::cor::{lesson}::{e['cor']}"]
                                                         + [f"NEBLI::estrutura::{c}" for c in e.get("cobre", [])]
                                                         + [f"NEBLI::texto::{_kt(c)}" for c in e.get("cobre_texto", [])]))
                planejadas.add(nid)
                resultados.append({"ordem": e["ordem"], "chave": e["chave"], "tipo": e["tipo"], "nid": nid, "cor": e["cor"],
                                   "cobre": e.get("cobre", []), "modelo": n["modelName"], "associada": True})
                continue
            for nome, caminho in e["midia"].items():
                if nome.startswith("u7-") or not A("retrieveMediaFile", filename=nome):
                    A("storeMediaFile", filename=nome, data=base64.b64encode(Path(caminho).read_bytes()).decode())
            tags = [lesson_tag, f"NEBLI::ordem::{cur['short']}-{e['ordem']:03d}", f"NEBLI::run::{run}", "NEBLI::uc07",
                    f"NEBLI::escopo::{cur['modulo']}", f"NEBLI::chave::{e['chave']}", f"NEBLI::origem::{e['fonte']}",
                    f"NEBLI::cor::{lesson}::{e['cor']}"] + [f"NEBLI::estrutura::{c}" for c in e.get("cobre", [])] \
                + [f"NEBLI::texto::{_kt(c)}" for c in e.get("cobre_texto", [])]
            if e.get("estrutura") and e["estrutura"] not in e.get("cobre", []):
                tags.append(f"NEBLI::estrutura::{e['estrutura']}")
            if e["tipo"] in ("kenhub", "texto"):
                tags.append(TAG_KENHUB)
            if "nid" in e:
                tags.append(f"NEBLI::source::nid-{e['nid']}")
            tags += [t for t in e.get("tags_origem", []) if not t.startswith("NEBLI::")]
            atual = existentes.get(e["chave"])
            if atual:
                nid = atual["noteId"]
                campos = _campos_modelo(e)
                campos["NEBLI_Comentario"] = atual["fields"].get("NEBLI_Comentario", {}).get("value", "")  # comentário de Davi fica
                if atual["modelName"] != e["modelo"]:
                    A("updateNoteModel", note={"id": nid, "modelName": e["modelo"], "fields": campos, "tags": tags})
                else:
                    A("updateNote", note={"id": nid, "fields": campos, "tags": tags})
                    velhas = [t for t in atual["tags"] if t not in tags]
                    if velhas:
                        A("removeTags", notes=[nid], tags=" ".join(velhas))
            else:
                nid = A("addNote", note={"deckName": deck, "modelName": e["modelo"], "fields": dict(_campos_modelo(e), NEBLI_Comentario=""),
                                         "tags": tags, "options": {"allowDuplicate": True}})
            planejadas.add(nid)
            cards = A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))
            fora = [c["cardId"] for c in cards if canonical(c["deckName"]) != deck]
            if fora:
                A("changeDeck", cards=fora, deck=deck)
            for c in cards:
                if c["flags"] not in PESSOAIS and c["flags"] != FLAG[e["cor"]]:
                    A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[FLAG[e["cor"]]], warning_check=True)
                if c["type"] == 0:  # só cards novos entram na fila na ordem do Kenhub
                    due = faixa + e["ordem"] * 10 + c["ord"]
                    try:
                        A("setSpecificValueOfCard", card=c["cardId"], keys=["due"], newValues=[due], warning_check=True)
                    except RuntimeError as err:
                        if "protected state" not in str(err):
                            raise
                        recusados.append((due, c["cardId"]))
            if any(c["queue"] == -1 for c in cards):
                A("unsuspend", cards=[c["cardId"] for c in cards])
            resultados.append({"ordem": e["ordem"], "chave": e["chave"], "tipo": e["tipo"], "nid": nid, "cor": e["cor"],
                               "cobre": e.get("cobre", []), "modelo": e["modelo"]})
        # o que saiu do plano: apagar só sem comentário e sem revisão; senão, retirar (suspenso + etiqueta), nunca perder histórico
        retiradas = []
        for nid in A("findNotes", query=f'"tag:NEBLI::uc07::assoc::{lesson}"'):
            if nid not in planejadas:   # associação desfeita: só tira as etiquetas desta unidade; a nota é da unidade de origem
                n = A("notesInfo", notes=[nid])[0]
                tira = [t for t in n["tags"] if t in (lesson_tag, f"NEBLI::uc07::assoc::{lesson}") or t.startswith(f"NEBLI::ordem::{cur['short']}-")
                        or t.startswith(f"NEBLI::cor::{lesson}::")]
                A("removeTags", notes=[nid], tags=" ".join(tira))
                retiradas.append({"nid": nid, "chave": "assoc", "acao": "associação desfeita"})
        for chave, n in existentes.items():
            if n["noteId"] in planejadas:
                continue
            cs = A("cardsInfo", cards=n["cards"])
            com = n["fields"].get("NEBLI_Comentario", {}).get("value", "").strip()
            if com or any(c["reps"] > 0 for c in cs):
                A("addTags", notes=[n["noteId"]], tags="NEBLI::retirado::uc07-v2")
                A("removeTags", notes=[n["noteId"]], tags=lesson_tag)
                A("suspend", cards=[c["cardId"] for c in cs])
                retiradas.append({"nid": n["noteId"], "chave": chave, "acao": "retirada (comentário/revisão preservados)"})
            else:
                A("deleteNotes", notes=[n["noteId"]])
                retiradas.append({"nid": n["noteId"], "chave": chave, "acao": "apagada (sem comentário nem revisão)"})
    return run, resultados, recusados, antes, retiradas


def gates_pos(A, cur, itens, resultados, antes, texto):
    deck, lesson = cur["deck"], cur["lesson_id"]
    falhas = []
    ids = A("findNotes", query=f'"tag:NEBLI::{lesson}"')
    if set(ids) != {r["nid"] for r in resultados}:
        falhas.append(f"[pós] notas da unidade no Anki ({len(ids)}) != planejadas ({len(resultados)})")
    cobertas = set()
    for r in resultados:
        n = A("notesInfo", notes=[r["nid"]])[0]
        if "NEBLI_Comentario" not in n["fields"]:
            falhas.append(f"[G7 comentário] {r['chave']}: nota sem campo de comentário ({n['modelName']})")
        if n["modelName"] != r["modelo"] and not r.get("associada"):
            falhas.append(f"[pós] {r['chave']}: tipo {n['modelName']} != {r['modelo']}")
        cs = A("cardsInfo", cards=n["cards"])
        if not cs:
            falhas.append(f"[pós] nota sem card: {r['chave']}")
        for c in cs:
            if r.get("associada"):
                continue   # nota de outra unidade, só associada: deck e bandeira são os da origem
            if canonical(c["deckName"]) != deck:
                falhas.append(f"[pós] deck errado: {r['chave']} em {c['deckName']}")
            if c["queue"] == -1:
                falhas.append(f"[pós] card suspenso: {r['chave']}")
            if c["flags"] not in PESSOAIS and c["flags"] != FLAG[r["cor"]]:
                falhas.append(f"[pós] bandeira {c['flags']} != {FLAG[r['cor']]}: {r['chave']}")
        reps_antes = sum(antes.get(r["nid"], {}).values())
        if reps_antes and sum(c["reps"] for c in cs) < reps_antes:
            falhas.append(f"[histórico] {r['chave']}: revisões caíram de {reps_antes} para {sum(c['reps'] for c in cs)}")
        cobertas.update(x for x in r["cobre"] if x)
    for i in itens:
        if i["slug"] not in cobertas:
            falhas.append(f"[cobertura] estrutura sem card no deck final: {i['slug']}")
    tags_texto = {t.split("::", 2)[2] for r in resultados for t in A("notesInfo", notes=[r["nid"]])[0]["tags"] if t.startswith("NEBLI::texto::")}
    for t in texto:
        if _kt(t["chave"]) not in tags_texto:
            falhas.append(f"[cobertura-quiz] trecho sem card no deck final: {t['chave']}")
    falhas += duplicatas(A)
    return falhas


def revisao_md(cur, itens, entradas, resultados, rel, texto):
    """Roteiro da revisão (F-20261018-CLAUDE-03): card a card e o deck como um todo — o que olhar e o que o deck deve cobrir."""
    por = {e["chave"]: e for e in entradas}
    n_cards = sum(1 for _ in resultados)
    L = [f"# Revisão — {cur['deck']}", "",
         "Feita DEPOIS de olhar as folhas de contato (`render/grandes`), card a card e depois o deck todo. "
         "Só então `./kenhub-deck --revisado <corrida> \"observação\"` libera “ENTREGUE”.", "",
         "## O deck como um todo", "",
         f"- Estruturas do quiz: {len(itens)} · cobertas pelos cards: {len({s for r in resultados for s in r['cobre'] if s})}/{len(itens)}",
         f"- Trechos do texto de estudo (objetivos, parágrafos, legendas, tabela-resumo): {len(texto)} · cobertos: "
         f"{len({k for e in entradas for k in e.get('cobre_texto', [])} & {t['chave'] for t in texto})}/{len(texto)}",
         f"- Notas: {n_cards} · folhas de contato: {len(rel['folhas'])}", "",
         "Perguntas da revisão do deck: cobre tudo que o quiz da unidade cobra (identificação, grafia, texto)? "
         "Há estrutura importante da aula (cronograma/Machado) sem card? Ordem didática ok? Nada repetido de outra unidade?", "",
         "## Card a card", "", "| # | Tipo | Nome / enunciado | Cobre | Olhado |", "|---|---|---|---|---|"]
    for r in resultados:
        e = por.get(r["chave"], {})
        nome = e.get("campos", {}).get("Nome PT") or re.sub(r"<[^>]+>", "", e.get("campos", {}).get("Text", ""))[:90] or r["chave"]
        L.append(f"| {r['ordem']} | {r['tipo']} | {nome} | {', '.join(r['cobre'] + e.get('cobre_texto', []))[:70]} | [ ] |")
    return "\n".join(L) + "\n"


def duplicatas(A):
    """[sem duplicata] a mesma estrutura do Kenhub (ou a mesma nota de origem) não pode ter duas notas próprias na UC07."""
    donos = {}
    for n in A("notesInfo", notes=A("findNotes", query='"tag:NEBLI::uc07" -"tag:NEBLI::retirado::*"')):
        licoes = [t for t in n["tags"] if t.startswith("NEBLI::2026-uc07-")]
        assoc = {t.split("::")[-1] for t in n["tags"] if t.startswith("NEBLI::uc07::assoc::")}
        if not [l for l in licoes if l.split("::", 1)[1] not in assoc]:
            continue
        for k in set(_chaves_nota(n)):
            donos.setdefault(k, set()).add(n["noteId"])
    return [f"[sem duplicata] {k}: {len(v)} notas próprias na UC07 ({sorted(v)[:3]})" for k, v in donos.items() if len(v) > 1]


def main():
    corrida = Path(sys.argv[1]).resolve()
    dry = "--dry-run" in sys.argv
    A = AnkiPaciente()
    cur, base, itens, entradas, problemas, cobertas = plano(corrida, A)
    tipos = {}
    for e in entradas:
        tipos[e["tipo"]] = tipos.get(e["tipo"], 0) + 1
    print(f"plano: {len(entradas)} notas {tipos}; {len(cobertas)}/{len(itens)} estruturas cobertas")
    if problemas:
        print("GATE PRÉ REPROVADO — nada foi instalado:\n  " + "\n  ".join(problemas))
        raise SystemExit(1)
    if dry:
        print("dry-run: gates pré ok")
        return
    rec_ant = corrida / "receipt.json"
    if rec_ant.exists() and "--forcar" not in sys.argv:   # F-20261018-CLAUDE-04: Davi está estudando — nada de gravar de novo toda hora
        horas = (datetime.now(timezone.utc) - datetime.fromisoformat(json.loads(rec_ant.read_text())["at"])).total_seconds() / 3600
        if horas < 6:
            raise SystemExit(f"[sem regravar à toa] esta unidade foi gravada há {horas:.1f} h; junte as mudanças e grave em lote "
                             "(ou use --forcar, só com motivo)")
    if not pode_gravar_bandeira(A):
        raise SystemExit("O Anki está com uma janela de edição aberta (navegador de cards ou editor) e recusa gravar. "
                         "Feche essa janela (Cmd+W) e rode de novo: a reconciliação conclui o que faltar.")
    run, resultados, recusados, antes, retiradas = instalar(A, cur, entradas)
    SYNC_PENDENTE.write_text(datetime.now(timezone.utc).isoformat(), encoding="utf-8")   # o sync fica para quando Davi estiver ocioso
    falhas = gates_pos(A, cur, itens, resultados, antes, json.loads((base / 'itens.json').read_text()).get('texto', []))
    if recusados:
        pedido = ROOT / "arquivos-trabalho" / "anki-acao-pedido.json"
        if not pedido.exists():
            ordem = sorted(recusados)
            pedido.write_text(json.dumps({"acao": "reposicionar", "deck": cur["deck"], "inicio": ordem[0][0], "cards": [c for _, c in ordem]}))
    from nebli.kenhub import render
    falhas_render, rel = render.renderizar(f'"tag:NEBLI::{cur["lesson_id"]}"', corrida / "render", [r["nid"] for r in resultados])
    cores = [r["cor"] for r in resultados]
    rec = {"run": run, "deck": cur["deck"], "notas": resultados, "retiradas": retiradas, "falhas_pos": falhas,
           "falhas_render": falhas_render, "folhas": rel["folhas"], "at": datetime.now(timezone.utc).isoformat()}
    (corrida / "receipt.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    (corrida / "revisao.md").write_text(revisao_md(cur, itens, entradas, resultados, rel, json.loads((base / "itens.json").read_text()).get("texto", [])))
    (corrida / "revisao.json").unlink(missing_ok=True)   # nova instalação = nova revisão
    print(json.dumps({"deck": cur["deck"], "notas": len(resultados), "verde": cores.count("verde"), "azul": cores.count("azul"),
                      "rosa": cores.count("rosa"), "retiradas": len(retiradas), "falhas_pos": len(falhas),
                      "falhas_render": len(falhas_render), "folhas_para_olhar": len(rel["folhas"]),
                      "pasta": str(corrida / "render")}, ensure_ascii=False))
    for f in (falhas + falhas_render)[:40]:
        print(" -", f)
    if falhas or falhas_render:
        raise SystemExit("GATES REPROVADOS — o deck NÃO está entregue (ver receipt.json)")
    print("GATES OK — olhe as folhas de contato antes de entregar")


if __name__ == "__main__":
    main()
