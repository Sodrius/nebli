"""Gates v12 e pacote do verificador por casos que deram certo (F-20261101-CLAUDE-01).

Davi (01/11): deck que ensina a aula + AnKing/Step junto, poucos e fortes; quatro tipos de card; AnKing fora da aula
"entra se ensina"; autoral = lacuna ou fio da aula; "imagem sempre que visual"; "deixa tudo isso como gate e com um
agente para verificar tudo baseado em casos que deram certo".

E3: a corrida grava `tipos.tsv` (chave, tipo, principio, visual, papel). E7: `preparar` gera o pacote, o agente segue
`config/verificador-casos.md` e grava o parecer; `verificar` é o gate.

    python3 -m nebli.verificador_casos preparar <corrida>
    python3 -m nebli.verificador_casos verificar <corrida>
"""
import html
import json
import re
import sys
from pathlib import Path

from nebli import casos as _casos
from nebli.revisor_autorais import sha

TIPOS = ("mecanismo", "comparacao", "base-clinica", "fato-chave")
PAPEIS = ("lacuna", "fio")
COLS = ["chave", "tipo", "principio", "visual", "papel"]
ENTRADA, PARECER = "verificador-casos-entrada.json", "verificador-casos-parecer.json"
RUBRICA = Path(__file__).resolve().parent.parent / "config" / "verificador-casos.md"
_IMG = re.compile(r'<img[^>]+src="([^"]+)"', re.I)
_CLOZE = re.compile(r"\{\{c\d+::((?:(?!\}\}).)*?)\}\}", re.S)


def _txt(h, lacuna=True):
    h = _CLOZE.sub(lambda m: ("[" + m.group(1).split("::")[0] + "]") if lacuna else m.group(1).split("::")[0], h or "")
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def ler_tipos(run):
    p = Path(run) / "tipos.tsv"
    if not p.exists():
        return None
    linhas = [l.split("\t") for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    if not linhas or [c.strip() for c in linhas[0]] != COLS:
        return None
    return {r[0].strip(): dict(zip(COLS, [c.strip() for c in r] + [""] * len(COLS))) for r in linhas[1:]}


def _respostas(e):
    t = (e.get("fields") or {}).get("Text", "") or ""
    return frozenset(_txt(m.split("::")[0], False).lower() for m in _CLOZE.findall(t))


def _cards(plan, tipos):
    out = []
    for e in plan.get("entries", []):
        f = e.get("fields") or {}
        t = tipos.get(e["key"], {})
        out.append({"chave": e["key"], "origem": e.get("origin", ""), "frente": _txt(f.get("Text") or f.get("Front") or ""),
                    "verso": _txt(f.get("Extra") or f.get("Back Extra") or f.get("Back") or ""),
                    "imagens": sorted({s for v in f.values() for s in _IMG.findall(v or "")}),
                    "tipo": t.get("tipo", ""), "principio": t.get("principio", ""), "visual": t.get("visual", ""),
                    "papel": t.get("papel", "")})
        if int(plan.get("pipeline_versao") or 1) >= 15:
            out[-1]["frente_html"] = f.get("Text") or f.get("Front") or ""
            out[-1]["organizador"] = "data-nebli-organizacao" in out[-1]["frente_html"]
    return out


def _banco(uc):
    todos = _casos.carregar().get("casos", [])
    # mesma UC inteira; das outras, só os aprovados explicitamente por Davi (X, elogio, GUIA-2)
    return [c for c in todos if c.get("uc", "").startswith(uc) or set(c["por_que_deu_certo"]) - {"verde"}]


def _uc(plan, run):
    m = re.search(r"uc(\d+)", str(plan.get("lesson_id") or Path(run).name))
    return f"uc{m.group(1)}" if m else ""


def preparar(run, plan=None):
    run = Path(run)
    plan = plan or json.loads((run / "plan.json").read_text(encoding="utf-8"))
    cards = _cards(plan, ler_tipos(run) or {})
    banco = _banco(_uc(plan, run))
    pacote = {"rubrica": RUBRICA.read_text(encoding="utf-8"), "aula": plan.get("lesson_id", run.name),
              "cards_sha": sha(cards), "banco_sha": sha(banco), "cards": cards, "banco": banco}
    pacote["pipeline_versao"] = plan.get("pipeline_versao", 1)
    (run / ENTRADA).write_text(json.dumps(pacote, ensure_ascii=False, indent=1), encoding="utf-8")
    return run / ENTRADA


_ROTULO = re.compile(r"(?i)<b>\s*(aplicação|decodificação|application|example)\s*:\s*</b>|^(aplicação|decodificação)\s*:")
_FORMAT_NO_CLOZE = re.compile(r"\{\{c\d+::\s*<(b|u|i)>", re.I)


def forma_das_lacunas(e, autoral=None):
    """Rodada 01/11 (F-20261101-CLAUDE-04): os erros de escrita que mais voltaram, conferidos em todo card (AnKing também).
    Devolve a lista de problemas do card."""
    f = e.get("fields") or {}
    texto = f.get("Text") or ""
    extra = f.get("Extra") or f.get("Back Extra") or ""
    org = "data-nebli-organizacao" in texto
    if autoral is None:
        autoral = e.get("origin") == "Autoral"
    probs = []
    por_indice = {}
    for n, corpo in re.findall(r"\{\{c(\d+)::((?:(?!\}\}).)*?)\}\}", texto, re.S):
        resp = _txt(corpo.split("::")[0], False)
        por_indice.setdefault(n, []).append(resp)
        if len(resp.split()) > 3:
            probs.append(f"lacuna com mais de 3 palavras ({resp[:40]})")
        partes = corpo.split("::")
        if org and len(partes) > 1 and re.fullmatch(r"[A-Z][A-Z0-9-]{1,4}", resp) and re.fullmatch(r"[A-Z]…", partes[1].strip()):
            probs.append(f"pista revela inicial de sigla curta ({resp})")
    for n, rs in por_indice.items():
        # organizadores aprovados por Davi têm 4–5 itens no mesmo índice (1792713409954, 1792787420154, 1792588686955), sempre
        # com dica da 1ª letra; o tamanho certo do grupo fica com o verificador (esporotricose 1792175889534: "EXCESSO DE CLOZES")
        dicas = re.findall(r"\{\{c" + n + r"::(?:(?!\}\}).)*?::[^}]*…\}\}", texto)
        if len(rs) > 3 and len(dicas) < len(rs):
            probs.append(f"{len(rs)} lacunas no índice c{n} sem a dica da 1ª letra em cada uma")
        if len(rs) > 2 and not org and autoral:  # par no mesmo índice é contraste aprovado (GUIA-2 B; colédoco 1792713404156)
            probs.append(f"{len(rs)} respostas no índice c{n} fora de organizador")
    if org:
        # rodada 01/11 (b): "escrita ruim" nos organizadores de linhas explicativas; os modelos de Davi têm 3–8 palavras por linha
        # (1792787420154, 1792588686980), e "MAIS CLOZES POR VEZ" quando cada item virava um cartão (1792695033836)
        linhas = [l for l in (_txt(x, False) for x in re.split(r"<br\s*/?>|</div>\s*<div[^>]*>", texto)) if l]
        longas = [] if "<table" in texto else [l for l in linhas[1:] if len(l.split()) > 14]  # tabela não tem linha
        if longas:
            probs.append(f"linha de organizador com mais de 14 palavras ({longas[0][:40]})")
        if len(por_indice) >= 3 and all(len(v) == 1 for v in por_indice.values()):
            probs.append("organizador com uma lacuna por cartão: agrupar no mesmo índice")
    if _FORMAT_NO_CLOZE.search(texto):
        probs.append("negrito/itálico/sublinhado dentro da lacuna")
    fora = _txt(_CLOZE.sub(" ", texto), False).lower()
    for rs in por_indice.values():
        for r in rs:
            if len(r) > 3 and re.search(r"\b" + re.escape(r.lower()) + r"\b", fora):
                probs.append(f"resposta visível na frente ({r[:30]})")
    if _ROTULO.search(extra) or _ROTULO.search(_txt(extra, False)):
        probs.append("rótulo tipo 'Aplicação:' no verso")
    if any(s.lower().endswith(".svg") for s in _IMG.findall(texto + extra)):
        probs.append("esquema desenhado (.svg) no lugar de figura real")
    return probs


def alvos_essenciais(plan, parecer):
    """v15: exige revisão explícita de cada lacuna, vinculada ao texto atual."""
    if int(plan.get("pipeline_versao") or 1) < 15:
        return []
    probs = []
    for e in plan.get("entries", []):
        key = e["key"]
        text = (e.get("fields") or {}).get("Text", "") or ""
        clozes = [m.group(0) for m in _CLOZE.finditer(text)]
        if not clozes:
            continue
        review = ((parecer or {}).get("cards") or {}).get(key) or {}
        targets = review.get("alvos_essenciais")
        if not isinstance(targets, list) or len(targets) != len(clozes):
            probs.append(f"{key}: revisar cada ocorrência de lacuna")
            continue
        for index, (cloze, target) in enumerate(zip(clozes, targets), 1):
            if not isinstance(target, dict):
                probs.append(f"{key}: alvo {index} inválido")
                continue
            answer = _txt(_CLOZE.search(cloze).group(1).split("::")[0], False)
            if (target.get("cloze") != cloze
                    or _txt(str(target.get("resposta_esperada", "")), False).casefold() != answer.casefold()
                    or target.get("essencial") is not True
                    or target.get("inducao_sem_vazamento") is not True
                    or len(str(target.get("porque_dura", "")).strip()) < 30):
                probs.append(f"{key}: alvo {index} secundário, vazado ou sem justificativa atual")
        if "data-nebli-organizacao" in text:
            audit = review.get("avulsos_cobertos") or {}
            if (not isinstance(audit, dict)
                    or len(str(audit.get("busca", "")).strip()) < 15
                    or not isinstance(audit.get("decisoes"), list)
                    or (not audit["decisoes"] and len(str(audit.get("nenhum_porquê", "")).strip()) < 30)):
                probs.append(f"{key}: falta busca de avulsos cobertos")
            else:
                for decision in audit["decisoes"]:
                    if (not isinstance(decision, dict) or not decision.get("nid")
                            or decision.get("acao") not in ("suspender", "manter")
                            or len(str(decision.get("motivo", "")).strip()) < 30):
                        probs.append(f"{key}: decisão de avulso incompleta")
    return probs


def verificar(run, plan):
    """Gates duros do pipeline v12."""
    run = Path(run)
    out = []
    entries = plan.get("entries", [])
    tipos = ler_tipos(run)
    out.append(("[duro] v12: tipos.tsv com cabeçalho " + "|".join(COLS), tipos is not None))
    tipos = tipos or {}
    ruins = []
    for e in entries:
        t = tipos.get(e["key"])
        if not t:
            ruins.append(f"{e['key']}: sem linha")
            continue
        if t["tipo"] not in TIPOS:
            ruins.append(f"{e['key']}: tipo '{t['tipo']}' não é {'/'.join(TIPOS)}")
        if len(t["principio"]) < 20:
            ruins.append(f"{e['key']}: princípio da aula que o card ensina não escrito")
        if t["visual"] not in ("sim", "não", "nao"):
            ruins.append(f"{e['key']}: visual sim/não")
        if e.get("origin") == "Autoral" and t["papel"] not in PAPEIS:
            ruins.append(f"{e['key']}: autoral sem papel lacuna/fio")
    out.append((f"[duro] v12: cada card ({len(entries)}) é mecanismo, comparação, base clínica ou fato-chave e diz o princípio da aula que ensina"
                + (f": {'; '.join(ruins[:4])}" if ruins else ""), bool(tipos) and not ruins))
    sem_img = [e["key"] for e in entries if tipos.get(e["key"], {}).get("visual") == "sim"
               and not any(_IMG.search(v or "") for v in (e.get("fields") or {}).values())]
    out.append(("[duro] v12: imagem sempre que o conceito é visual" + (f": sem figura {sem_img[:5]}" if sem_img else ""), not sem_img))
    vistos, rep = {}, []
    for e in entries:
        r = _respostas(e)
        if r and "data-nebli-organizacao" not in ((e.get("fields") or {}).get("Text") or ""):
            if r in vistos:
                rep.append(f"{vistos[r]}={e['key']}")
            vistos.setdefault(r, e["key"])
    out.append(("[duro] v12: sem dois cards com a mesma resposta (repetição)" + (f": {rep[:4]}" if rep else ""), not rep))
    forma = {e["key"]: forma_das_lacunas(e) for e in entries}
    forma = {k: v for k, v in forma.items() if v}
    out.append(("[duro] v12: forma das lacunas e figuras (≤ 3 palavras, ≤ 3 por índice, uma resposta fora de organizador, sem negrito dentro, "
                "resposta não visível, sem rótulo no verso, sem esquema desenhado)" + (f": {dict(list(forma.items())[:3])}" if forma else ""), not forma))
    # Parecer do agente
    try:
        par = json.loads((run / PARECER).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        par = None
    cards = _cards(plan, tipos)
    banco = _banco(_uc(plan, run))
    nids = {c["nid"] for c in banco}
    if not par:
        out.append(("[duro] v12: parecer do verificador por casos que deram certo (verificador-casos-parecer.json)", False))
        return out
    atual = par.get("cards_sha") == sha(cards) and par.get("banco_sha") == sha(banco)
    alvos = alvos_essenciais(plan, par)
    if int(plan.get("pipeline_versao") or 1) >= 15:
        out.append(("[duro] v15: alvo essencial de cada lacuna e busca de avulsos cobertos" +
                    (f": {'; '.join(alvos[:5])}" if alvos else ""), not alvos))
    out.append(("[duro] v12: parecer do verificador é do deck atual (hashes de cards e banco)", atual))
    res = par.get("cards") or {}
    probs, textos = [], {}
    for c in cards:
        k = c["chave"]; x = res.get(k) or {}
        if not x:
            probs.append(f"{k}: sem parecer"); continue
        if x.get("caso") not in nids:
            probs.append(f"{k}: caso {x.get('caso')} fora do banco")
        for campo in ("comparacao", "motivo"):
            v = str(x.get(campo, "")).strip()
            if len(v) < 40:
                probs.append(f"{k}: {campo} curto")
            elif v in textos and textos[v] != k:
                probs.append(f"{k}: {campo} copiado de {textos[v]}")
            textos.setdefault(v, k)
        if x.get("veredito") != "aprovado":
            probs.append(f"{k}: {x.get('veredito', 'sem veredito')} — {str(x.get('motivo', ''))[:80]}")
    out.append((f"[duro] v12: verificador aprovou cada card contra um caso que deu certo" + (f": {'; '.join(probs[:5])}" if probs else ""), not probs))
    d = par.get("deck") or {}
    ok_deck = all(len(str(d.get(c, "")).strip()) >= 6 for c in ("fio_da_aula", "repetidos", "fora_do_principio"))
    limpo = all(str(d.get(c, "")).strip().lower().startswith("nenhum") for c in ("repetidos", "fora_do_principio"))
    out.append(("[duro] v12: verificador respondeu o deck inteiro sem repetidos nem cards fora do princípio da aula"
                + ("" if limpo else f": repetidos={d.get('repetidos')!r} fora={d.get('fora_do_principio')!r}"), ok_deck and limpo))
    return out


def main(argv=None):
    a = argv if argv is not None else sys.argv[1:]
    if len(a) != 2 or a[0] not in ("preparar", "verificar"):
        print(__doc__); return 2
    run = Path(a[1])
    if a[0] == "preparar":
        print(preparar(run)); return 0
    plan = json.loads((run / "plan.json").read_text(encoding="utf-8"))
    falhas = 0
    for nome, ok in verificar(run, plan):
        print(("OK   " if ok else "FALHA ") + nome); falhas += not ok
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
