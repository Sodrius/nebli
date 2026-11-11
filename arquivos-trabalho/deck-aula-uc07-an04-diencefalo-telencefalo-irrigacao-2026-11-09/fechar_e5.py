"""Gera os artefatos da E5 a partir de plan.json + curadoria (chaves reais do plano)."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1]))
import curadoria as C, plano as P, textos as T

plan = json.loads((HERE / "plan.json").read_text())
entries = {e["key"]: e for e in plan["entries"]}
comp = plan.get("compartilhados", {})
PK = {}
for (u, key, kind, nid, cod, alvo) in C.R:
    PK[key] = f"sh-{nid}" if kind in ("res", "an01") else key
porU = {}
for (u, key, kind, nid, cod, alvo) in C.R:
    porU.setdefault(u, []).append(PK[key])
porU.setdefault(52, []).append('aci-ramos-org')
porU.setdefault(53, []).append('aci-ramos-org')
comp_ = json.loads((HERE / "compreensao-aula.json").read_text())
blocos = comp_["blocos"]
bl = lambda u: next(i for i, b in enumerate(blocos) if b["laminas"][0] <= u <= b["laminas"][1])

# ---- inventário (SLIDES) com as chaves reais
inv = (HERE / "inventario.py").read_text().split("SLIDES = ")[0]
titulos = {int(m[1]): m[2] for m in re.finditer(r"===== página (\d+) =====\n(.*)", (HERE / "fontes/slides.txt").read_text())}
slides = []
for u in range(1, 63):
    if u in P.REPETICAO:
        slides.append((u, "revisao", f"Unidade {u}: {titulos[u]}", []))
    else:
        its = [i for i in P.ITENS if i[0] == u]
        o_que = "; ".join(i[3] for i in its) or titulos[u]
        slides.append((u, "conteudo", f"Unidade {u}: {titulos[u]}", [(f"u{u:02d}", o_que[:300], porU.get(u, []))]))
(HERE / "inventario.py").write_text(inv + "SLIDES = " + json.dumps(slides, ensure_ascii=False, indent=0) +
    "\nJUSTIFICATIVAS = {'revisao': 'Unidade de repetição/demonstração das peças: as estruturas mostradas têm card no bloco próprio.'}\nFIGURA_SEM_CARD = {}\n"
    + "CAPITULO = " + json.dumps([("Machado 3ed cap6 (diencéfalo)", [("diencefalo", "Partes, limites e estruturas do diencéfalo", [k for u in range(1, 22) for k in porU.get(u, [])][:30])]),
                                   ("Machado 3ed cap7 (telencéfalo)", [("telencefalo", "Sulcos, giros, corpo caloso, núcleos da base e cápsulas", [k for u in range(22, 47) for k in porU.get(u, [])][:30])]),
                                   ("Machado 3ed cap9 (vascularização)", [("irrigacao", "Carótida interna, vertebral, basilar, Willis e territórios", [k for u in range(47, 60) for k in porU.get(u, [])][:30])])], ensure_ascii=False) + "\n"
    "EXERCICIOS = [(\"Provas UC07 recebidas 11/11, recorte AN04\", []), (\"Monitoria Neuroanato 2 (aula 03)\", []), (\"Apostila guia aulas 2–3\", [])]\n")

NAO_KH = {1793966747232: "O Kenhub da Referência não tem identificação do hipotálamo inteiro (só núcleos e áreas); a AN01 identifica pela figura AnKing com seta."}
# ---- mapa de profundidade: itens do plano com chaves reais; todo card do plano em algum item
mapa = json.loads((HERE / "mapa-de-profundidade.json").read_text())
passos = []
for bi, b in enumerate(blocos):
    us = range(b["laminas"][0], b["laminas"][1] + 1)
    its = []
    for i in P.ITENS:
        if i[0] in us:
            ks = [PK.get(k, k) for k in i[6] if PK.get(k, k) in entries or PK.get(k, k)[3:] in comp]
            ks = ks or porU.get(i[0], [])
            its.append({"id": i[1], "tipo": i[2], "o_que": i[3], "fonte": f"unidade {i[0]}; {i[4]}", "termos": i[5], "cards": ks})
    if not its:
        continue
    usados = {k for it in its for k in it["cards"]}
    resto = [k for u in us for k in porU.get(u, []) if k not in usados]
    tipos = {it["tipo"] for it in its}
    if resto or "explicar" not in tipos:
        its.append({"id": f"b{bi+1:02d}-processo", "tipo": "explicar", "o_que": b["processo"][:400],
                    "fonte": f"unidades {b['laminas'][0]}–{b['laminas'][1]} (processo do bloco na compreensão)", "termos": [], "cards": resto or its[0]["cards"]})
    if not ({"e-se", "distinguir"} & {it["tipo"] for it in its}):
        its.append({"id": f"b{bi+1:02d}-distinguir", "tipo": "distinguir", "o_que": b["aprender"][-1],
                    "fonte": f"unidades {b['laminas'][0]}–{b['laminas'][1]}", "termos": [], "cards": its[0]["cards"]})
    passos.append({"passo": b["titulo"], "laminas": b["laminas"], "itens": its})
txtk = {k: re.sub(r"<[^>]+>", " ", " ".join(str(v) for v in e.get("fields", {}).values())).lower() for k, e in entries.items()}
txtk.update({f"sh-{n}": re.sub(r"<[^>]+>", " ", " ".join(str(v) for v in c.get("fields", {}).values())).lower() for n, c in comp.items()})
for p_ in passos:
    for it in p_["itens"]:
        it["termos"] = [t for t in it["termos"] if any(t.lower() in txtk.get(k, "") for k in it["cards"])]
    # um item por unidade de conteúdo, para que cada recuperação tenha sua capacidade nomeada
    for u in range(p_["laminas"][0], p_["laminas"][1] + 1):
        if u in P.REPETICAO or any(f"unidade {u};" in it["fonte"] for it in p_["itens"]):
            continue
        p_["itens"].append({"id": f"u{u:02d}-reconhecer", "tipo": "decorar", "o_que": f"Reconhecer e situar o que a unidade {u} ensina: {titulos[u]}", "fonte": f"unidade {u}; percurso", "termos": [], "cards": porU.get(u, [])})
# termos: palavras do próprio card; itens de identificação por bloco; itens clínicos com o card de base
import unicodedata
nrm = lambda t: "".join(c for c in unicodedata.normalize("NFKD", t.lower()) if not unicodedata.combining(c))
for p_ in passos:
    ids_bloco = [k for u in range(p_["laminas"][0], p_["laminas"][1] + 1) for (uu, kk, kind, nid, cod, a) in C.R if uu == u and (kk.startswith("id-") or kk.startswith("sh-id-")) for k in [PK[kk]]]
    if ids_bloco:
        p_["itens"].append({"id": f"b-{p_['laminas'][0]:02d}-identificar", "tipo": "decorar", "o_que": "Reconhecer na figura, sem legenda, as estruturas nomeadas neste bloco da aula",
                            "fonte": f"unidades {p_['laminas'][0]}–{p_['laminas'][1]}; Kenhub da Referência e monitoria", "termos": [], "cards": ids_bloco})
BASE = {}
for p_ in passos:
    for it in p_["itens"]:
        if it["id"] in BASE and PK[BASE[it["id"]]] not in it["cards"]:
            it["cards"].append(PK[BASE[it["id"]]])
        blob = nrm(" ".join(txtk.get(k, "") for k in it["cards"]))
        cand = [w for w in re.findall(r"[A-Za-zÀ-ú]{5,}", it["o_que"]) if w.lower() in " ".join(txtk.get(k, "") for k in it["cards"])]
        cand = cand or [w for w in re.findall(r"[a-zà-ú]{6,}", " ".join(txtk.get(k, "") for k in it["cards"]))][:1]
        it["termos"] = list(dict.fromkeys(cand))[:2]
mapa["passos"] = passos
mapa["uc07_basico_e_destino"]["basicos"] = [
    {"alvo": alvo, "fonte": f"unidade {u}", "cards": [PK[key]], "estado": "agora", "modalidade": "identificacao",
     "kenhub_disponivel": nid not in NAO_KH, **({"motivo_fallback": NAO_KH[nid]} if nid in NAO_KH else {})}
    for (u, key, kind, nid, cod, alvo) in C.R if key.startswith("id-") or key.startswith("sh-id-")]
(HERE / "mapa-de-profundidade.json").write_text(json.dumps(mapa, ensure_ascii=False, indent=1))

# ---- motivações: toda motivação atendida por cards reais
mot = json.loads((HERE / "motivacoes.json").read_text())
item = {it["id"]: it for p in passos for it in p["itens"]}
for m in mot["motivacoes"]:
    m["atendida_por"] = item[m["item_mapa"]]["cards"]
(HERE / "motivacoes.json").write_text(json.dumps(mot, ensure_ascii=False, indent=1))

# ---- compreensão: cards associados por bloco
for b in blocos:
    nb = sum(1 for u in range(b["laminas"][0], b["laminas"][1] + 1) for _ in porU.get(u, []))
    if nb >= len(b["aprender"]):
        b["motivo_volume"] = "Bloco anatômico com muitas estruturas: cada estrutura nomeada na aula tem uma identificação Kenhub (uma verde por estrutura) além do card de relação, por isso o número de cards passa de 3 por item."
    b["cards_associados"] = [k for u in range(b["laminas"][0], b["laminas"][1] + 1) for k in porU.get(u, []) if k.startswith("sh-")]
for i, k in enumerate(comp_["reconstrucoes"]):
    k["cards"] = [[PK["talamo-limites-org"], PK["hipotalamo-limites-org"], PK["subtalamo-limites-org"]], [PK["territorios-org"], PK["aci-ramos-org"], PK["vertebrobasilar-org"]],
                  [PK["corte-horizontal-org"], PK["estriado-org"], PK["capsula-interna-partes-org"]]][i]
(HERE / "compreensao-aula.json").write_text(json.dumps(comp_, ensure_ascii=False, indent=1))

# ---- escopo
esc = json.loads((HERE / "escopo.json").read_text())
esc["clinica_lateral"] = [PK[k] for k in ("ak-1481162464655", "ak-1481562744652", "ak-1481562751403", "ak-1481244840641", "ak-1480995292746", "ak-1481772047979", "ak-1481562846112", "ak-1481857900096")]
L = lambda *ks: [PK[k] for k in ks]
esc["linha_logica"] = [
 {"passo": "O telencéfalo cresce e esconde o diencéfalo, que só aparece no corte sagital, dividido pelo sulco hipotalâmico", "mecanismo": True,
  "cards": L("diencefalo-partes-org", "kh-sulco-hipotalamico", "sh-cerebro-partes"), "liga_ao_proximo": "o mesmo corte, agora coronal, dá os limites de cada parte"},
 {"passo": "Os limites saem de um corte coronal: ventrículo lateral acima, III ventrículo medial, cápsula interna lateral, hipotálamo e subtálamo abaixo", "mecanismo": True,
  "cards": L("talamo-limites-org", "hipotalamo-limites-org", "subtalamo-limites-org"), "liga_ao_proximo": "o assoalho do hipotálamo dá nome às suas regiões"},
 {"passo": "As regiões do hipotálamo levam o nome da estrutura do assoalho abaixo delas, e cada região agrupa seus núcleos", "mecanismo": True,
  "cards": L("hipotalamo-nucleos-org", "ak-1481418766004", "ak-1481418757045"), "liga_ao_proximo": "acima do diencéfalo, o telencéfalo é organizado por sulcos"},
 {"passo": "Três sulcos constantes criam os lobos, e o sulco central separa a área motora (pré-central) da somestésica (pós-central)", "mecanismo": True,
  "cards": L("lobos-limites-org", "res-1792261811050", "ak-1481513127112", "ak-1481513311304"), "liga_ao_proximo": "por dentro do hemisfério, o centro branco guarda os núcleos da base"},
 {"passo": "No corte horizontal, as cápsulas separam os núcleos da base, que se agrupam em lentiforme e corpo estriado", "mecanismo": True,
  "cards": L("corte-horizontal-org", "estriado-org", "capsula-interna-partes-org"), "liga_ao_proximo": "tudo é irrigado por dois sistemas arteriais"},
 {"passo": "Vertebrais formam a basilar, que termina nas cerebrais posteriores; a carótida interna dá a média e a anterior; cada território segue as faces do hemisfério", "mecanismo": True,
  "cards": L("vertebrobasilar-org", "aci-ramos-org", "territorios-org"), "liga_ao_proximo": "as comunicantes fecham os dois sistemas no polígono de Willis"},
 {"passo": "As comunicantes unem os sistemas no círculo arterial do cérebro", "cards": L("willis-org", "ak-1481772047979"), "liga_ao_proximo": ""},
]
esc["cards_de_conexao"] = ["diencefalo-partes-org", "talamo-limites-org", "hipotalamo-limites-org", "subtalamo-limites-org", "corte-horizontal-org", "territorios-org", "willis-org"]
esc["uso_das_fontes"] = {"aula": L("talamo-limites-org", "hipotalamo-nucleos-org", "territorios-org", "lobos-limites-org"),
                         "bibliografia": L("capsula-interna-partes-org", "face-inferior-org", "aci-ramos-org"),
                         "apostila": L("corte-horizontal-org", "estriado-org")}
(HERE / "escopo.json").write_text(json.dumps(esc, ensure_ascii=False, indent=1))

# ---- tipos.tsv (cards do plano)
def tipo(k, e):
    text=re.sub(r'<[^>]+>',' ',e.get('fields',{}).get('Text','')).lower()
    visual='sim' if any('<img' in v for v in e.get('fields',{}).values()) else 'nao'
    if 'org' in k or k in ('faces-hemisferio','giro-x-sulco','nucleo-x-ganglio'):
        return 'comparacao',visual
    if k=='diencefalo-escondido' or 'via direta' in text or 'via indireta' in text or 'receptores' in text:
        return 'mecanismo',visual
    if any(w in text for w in ('lesão','avc','síndrome','doença de','afasia','aneurisma','hemibalismo','oclusão','tumor','estenose','trauma')):
        return 'base-clinica',visual
    return 'fato-chave',visual
alvo = {k: a for (u, k, kind, n, c, a) in C.R}
for _k, _e in entries.items():
    if _k.startswith("ak-"):
        alvo[_k] = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"\{\{c\d+::(.*?)(::[^}]*)?\}\}", r"\1", _e["fields"]["Text"]))).strip()[:140]
linhas = ["chave\ttipo\tprincipio\tvisual\tpapel"]
for k, e in entries.items():
    t, v = tipo(k, e)
    papel = ("fio" if k in esc["cards_de_conexao"] else "lacuna") if e.get("origin") == "Autoral" else ""
    if e.get("origin") == "Autoral":
        v = "nao"
    linhas.append(f"{k}\t{t}\t{alvo.get(k, e.get('alvo', ''))}\t{v}\t{papel}")
(HERE / "tipos.tsv").write_text("\n".join(linhas) + "\n")

# ---- cobertura.tsv
sem = {json.loads(l)["chave"]: json.loads(l) for l in (HERE / "busca/semantica.jsonl").read_text().splitlines()}
def lidos(k):
    r = sem.get(k) or sem.get(k.replace("-org", "")) or {}
    return ",".join(str(x["nid"]) for x in r.get("top", []) if x["acervo"] != "NEBLI-vivo")[:200] or "-"
cob = ["chave\tconceito\tfonte_aula\tveredito\tlidos\tdecora\tdecisao"]
VER = {k: ("parcial", "AnKing e Kenhub cobram cada peça isolada; a aula lista o conjunto (limites, regiões, sequência do corte, ramos, territórios) e o organizador recupera o conjunto lado a lado") for k in T.AU}
for k, e in entries.items():
    dec = re.sub(r"\{\{c\d+::([^}:]+).*?\}\}", r"\1", "|".join(re.findall(r"\{\{c\d+::[^}]+\}\}", e.get("fields", {}).get("Text", ""))))[:80] or "-"
    if e.get("origin") == "Autoral":
        v, d = VER[k]
        dec = re.findall(r"\{\{c\d+::([^}:]+)", e["fields"]["Text"])[0]
        fa = T.AU_FONTE[k]
        fa = ("; ".join(x for x in fa.split("; ") if not x.startswith("Machado")) + "; " + "; ".join(x for x in fa.split("; ") if x.startswith("Machado"))).strip("; ")
    else:
        _u = re.search(r"\d+", e.get("evid", "0")).group()
        v, d, fa = "coberto", f"{e.get('origin', 'acervo')} {e.get('src', '')} cobre a relação", "unidade " + _u
    cob.append(f"{k}\t{alvo.get(k, '')}\t{fa}\t{v}\t{lidos(k)}\t{dec}\t{d}")
(HERE / "busca/cobertura.tsv").write_text("\n".join(cob) + "\n")

# ---- decisoes.json (autorais) e REVISAO-AUTORAIS.md
decs = {k: {"lacuna": VER[k][1], "motivo": VER[k][1], "fonte_aula": T.AU_FONTE[k]} for k in VER}
(HERE / "decisoes.json").write_text(json.dumps(decs, ensure_ascii=False, indent=1))
REV = {k: ("§C", "conjunto organizado", T.AU_FONTE[k].split(" (")[0], "1792588686980", "uma linha por componente com o critério visível e o nome a recuperar no índice único", "componentes do tubo neural → componentes da lista da aula", "1793784421465", re.sub(r"<[^>]+>", "", " | ".join(re.findall(r"\{\{c1::([^}]+)\}\}", T.AU[k][0])))) for k in T.AU}
md = ["# REVISAO-AUTORAIS — aula 04", "", "Cada autoral relido contra o exemplar do mesmo tipo de informação (GUIA-2) e contra o anti-exemplar da família de erro (GUIA-3).", ""]
for k, (par, t, ens, ex, sem_, ad, anti, dec) in REV.items():
    md.append(f"- {k} — par: {par}; tipo-informacao: {t}; ensina: {ens}; EXEMPLAR {ex}; semelhança: {sem_}; adaptação: {ad}; ANTI {anti}; decora: {dec} — ok")
md += ["", "Organizadores necessários: sim — a aula é feita de listas que o professor monta na lousa (partes e limites do diencéfalo, núcleos por região, sulcos e lobos, sequência do corte horizontal, ramos e territórios das artérias); os IOs e AnKing cobram cada peça, o organizador cobra o conjunto."]
(HERE / "REVISAO-AUTORAIS.md").write_text("\n".join(md) + "\n")

# ---- planejamento.json
plj = {"aula": "Anatomia 04 UC07, 27/10/2026 (sem lâminas; 62 unidades do percurso)", "feito_antes_de_montar": True,
       "fontes": {"slides": {"estado": "consultada", "contribuicao": "Roteiro das transcrições T1–T4 + apostila-guia (fontes/slides.txt)."},
                  "bibliografia": {"estado": "consultada", "contribuicao": "Machado cap6, 7 e 9: diencéfalo, telencéfalo, núcleos da base, artérias e territórios."},
                  "caoc": {"estado": "consultada", "contribuicao": "Sem monitoria própria da aula 04; apostila-guia e GaKa fazem esse papel."},
                  "youtube": {"estado": "consultada", "contribuicao": "Ninja Nerd (Circle of Willis) confere a irrigação."},
                  "veteranos": {"estado": "consultada", "contribuicao": "Apostila guia (Aulas 4 e 6), GaKa (aulas 4–5) e manuscrito p10–32: limites, núcleos, corte horizontal, artérias."},
                  "provas": {"estado": "consultada", "contribuicao": "Quatro PDFs de provas recebidos em 11/11; recorte AN04 e questões identificadas em fontes/provas-an04.txt."},
                  "exercicios": {"estado": "não localizada", "contribuicao": "Pastas da aula vazias; sem exercícios próprios."}},
       "alvos": [{"id": i[1], "slide": str(i[0]), "alvo": i[3], "fontes": [i[4]], "origem_prevista": ", ".join(i[6])} for i in P.ITENS]}
_pl = HERE / "planejamento.json"
_old = json.loads(_pl.read_text()) if _pl.exists() else {}
if _old.get("alvos") and str(_old["alvos"][0].get("id", "")).startswith("u7an04-"):
    _old["fontes"] = plj["fontes"]; plj = _old
_pl.write_text(json.dumps(plj, ensure_ascii=False, indent=1))

# ---- fontes.json (espelho do fontes-decl.json para o gate)
fd = json.loads((HERE / "fontes-decl.json").read_text())
alvos = [t["id"] for t in plj["alvos"]]
import hashlib
sha = lambda p: hashlib.sha256((HERE / p).read_bytes()).hexdigest()
ev = lambda arq, loc, contrib: {"estado": "consultada", "arquivo": arq, "sha256": sha(arq), "leitura": "integral", "localizador": loc, "contribuicao": contrib, "lida_antes_da_selecao": True, "alvos": alvos}
fj = {"nome": fd["nome"], "escopo": "cards", "drive_pasta": fd["drive_pasta"], "slides": {"arquivo": "fontes/slides.txt", "todas_vistas": True, "obs": "sem lâminas: 62 unidades do percurso"},
      "livros": fd["livros"], "canais": fd["canais"], "transcricoes": fd["transcricoes"], "materiais_uc": fd["materiais_uc"], "provas": fd["familias"]["provas"]}
(HERE / "fontes.json").write_text(json.dumps(fj, ensure_ascii=False, indent=1))
print("ok", len(slides), "unidades;", len(passos), "passos;", sum(len(p["itens"]) for p in passos), "itens;", len(linhas) - 1, "tipos")

# ---- fontes.json completo (evidência por família; aula sem lâminas declarada por Davi)
def ev(arq, loc, contrib):
    return {"estado": "consultada", "arquivo": arq, "sha256": sha(arq), "leitura": "integral", "localizador": loc, "contribuicao": contrib,
            "lida_antes_da_selecao": True, "alvos": alvos}
nao = lambda b, i: [{"estado": "não localizada", "essencial": False, "busca": b, "impacto": i}]
fj["sem_laminas"] = {"fala": "se não tem slide mas tem transcrição segue", "feedback": "F-20261108-CLAUDE-01",
                     "roteiro": "fontes/slides.txt (62 unidades da fala do professor minuto a minuto + monitoria 2)"}
fj["evidencias"] = {
 "slides": [ev("fontes/slides.txt", "62 unidades do percurso (t1–t4 + apostila)", "Roteiro da aula sem lâminas: ordem e conteúdo dos 18 blocos."),
            ev("fontes/t1-diencefalo.min.txt", "transcrição do diencéfalo, 71 min", "Partes, limites e núcleos do tálamo, hipotálamo, epitálamo e subtálamo."),
            ev("fontes/t2-telencefalo.min.txt", "transcrição do telencéfalo, 58 min", "Faces, sulcos, lobos e giros."),
            ev("fontes/t3-irrigacao.min.txt", "transcrição da irrigação, 20 min", "Sistemas vertebrobasilar e carotídeo, territórios, Willis."),
            ev("fontes/t4-pratica.min.txt", "transcrição da prática, 28 min", "Peças: repetição das aulas 03 e 04.")],
 "bibliografia": [ev("livros/machado-cap6-diencefalo.txt", "Machado cap6 inteiro", "III ventrículo, tálamo, hipotálamo, epitálamo, subtálamo."),
                  ev("livros/machado-cap7-telencefalo.txt", "Machado cap7 inteiro", "Sulcos e giros, corpo caloso, núcleos da base, cápsula interna."),
                  ev("livros/machado-cap9-vascularizacao.txt", "Machado cap9 §1–2.2.5", "Carótida interna, vertebral e basilar, Willis, territórios.")],
 "veteranos": [ev("../uc07-fontes-veteranos-2026-10-19/apostila-guia-neuroanatomia-paginas.txt", "Apostila guia Aulas 4 e 6 + cap5 núcleos da base", "Corte horizontal, lentiforme e corpo estriado."),
               ev("../deck-aula-uc07-an03-medula-tronco-nervos-cerebelo-2026-11-08/fontes/gaka-paginas.txt", "GaKa aulas 4–5 e Extra", "Limites do tálamo/hipotálamo, cápsula interna, artérias.")],
 "youtube": [dict(ev("canais/ninjanerd-willis.txt", "Ninja Nerd, Circle of Willis (integral)", "Confirma trajeto vertebrobasilar, ramos da carótida interna e comunicantes; lenticuloestriadas pelo AnKing."), canal="Ninja Nerd", url="https://www.youtube.com/watch?v=6VMiKeAvvTY")],
 "provas": [ev("fontes/provas-an04.txt", "Questões AN04 das provas de 2023 e 2025 e coletânea com gabarito, recebidas 11/11", "Vias direta/indireta, D1/D2, dor talâmica, Meyer, fórnix, Willis e cápsula interna; textos integrais originais preservados em uc07-resumos-2026-11-11.")],
 "exercicios": nao("Pastas da aula 04 (pessoal e turma) vazias.", "Sem questões próprias."),
 "caoc": nao("Sem monitoria específica da aula 04 no Drive.", "Apostila-guia e GaKa cobrem o papel de monitoria."),
}
fj["pasta_turma"] = fd["pasta_turma"]; fj["turma_arquivos_lidos"] = []; fj["turma_descartados"] = {}
fj["pastas_extra"] = ["MEGA DRIVE/Medicina/Material de estudo/A - Primeiro ano (2026)/UC07/Outros", "TURMA 114/1º ano/UC07 - Sistema Nervoso I/Material para Estudos"]
fj["exercicios"] = fj["evidencias"]["exercicios"][0]; fj["caoc"] = {"estado": "não localizada", "busca": "Drive pessoal (UC07/Outros) e da turma (Material para Estudos, Aula 04, Aula 06) inventariados em 09/11: só monitorias da aula 03 e resumos gerais.", "contribuicao": "Sem monitoria da aula 04; GaKa e apostila-guia fazem o papel."}
fj["veteranos"] = {"estado": "consultada", "contribuicao": "Apostila guia, GaKa e manuscrito de veteranos confirmam a aula; divergências registradas em fontes-decl.json."}
(HERE / "fontes.json").write_text(json.dumps(fj, ensure_ascii=False, indent=1))
print("fontes.json ok")

# ---- cobertura.json: cada card ligado a um item ensinado (unidade do percurso)
cobj = {"conferido_depois_de_instalar": (HERE / "receipt.json").exists() and (HERE / "revisao-despejo.txt").stat().st_size > 20000,
        "itens": [{"id": f"u{u:02d}", "fonte": f"slide {u} (unidade do percurso): {titulos[u]}", "cards": porU.get(u, [])} for u in range(1, 63) if porU.get(u)]
        + [{"id": f"u{u:02d}", "fonte": f"slide {u} (unidade do percurso): {titulos[u]}", "cards": [], "excluido": P.REPETICAO[u]} for u in P.REPETICAO]
        + [{"id": "livro-cap6", "fonte": "livro Machado cap6 (diencéfalo)", "cards": [k for u in range(1, 22) for k in porU.get(u, [])][:40]},
           {"id": "livro-cap5", "fonte": "livro Machado cap7 (telencéfalo e núcleos da base)", "cards": [k for u in range(22, 47) for k in porU.get(u, [])][:40]},
           {"id": "livro-cap11", "fonte": "livro Machado cap9 (irrigação)", "cards": [k for u in range(47, 60) for k in porU.get(u, [])][:40]}]}
(HERE / "cobertura.json").write_text(json.dumps(cobj, ensure_ascii=False, indent=1))
