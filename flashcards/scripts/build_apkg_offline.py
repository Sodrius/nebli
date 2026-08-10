#!/usr/bin/env python3
"""build_apkg_offline.py — monta o `.apkg` da aula sem Anki e sem AnkiConnect.

`docs/canon/APKG.md` exige montagem e auditoria offline; o montador antigo
(`montar_deck_aula.py`) fala com o AnkiConnect em localhost:8765 e por isso não
serve ao pipeline canônico. Este script escreve diretamente uma coleção Anki
legada (schema 11), que as versões modernas do Anki importam sem conversão.

Entrada: o `contrato-cobertura.json` da aula — os cards moram lá, não aqui.
Saída: `<Nome curto>.apkg` + relatório JSON da montagem.

Os note types não são inventados: são lidos de um pacote NEBLI já existente,
para preservar templates, CSS e comportamento de renderização. O note type de
cloze é derivado com um campo `Tema`, porque o original trazia o cabeçalho da
aula fixo no template.

Uso:
  python flashcards/scripts/build_apkg_offline.py \
      arquivos-trabalho/<slug>/contrato-cobertura.json \
      --notetype-source "flashcards/decks-apkg/P3 - UC02 completo.apkg" \
      --out "arquivos-trabalho/<slug>/<Nome curto>.apkg"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sqlite3
import tempfile
import time
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
IMG_RE = re.compile(r'src="([^"]+)"')

SCHEMA = """
CREATE TABLE col (id integer primary key, crt integer not null, mod integer not null,
  scm integer not null, ver integer not null, dty integer not null, usn integer not null,
  ls integer not null, conf text not null, models text not null, decks text not null,
  dconf text not null, tags text not null);
CREATE TABLE notes (id integer primary key, guid text not null, mid integer not null,
  mod integer not null, usn integer not null, tags text not null, flds text not null,
  sfld integer not null, csum integer not null, flags integer not null, data text not null);
CREATE TABLE cards (id integer primary key, nid integer not null, did integer not null,
  ord integer not null, mod integer not null, usn integer not null, type integer not null,
  queue integer not null, due integer not null, ivl integer not null, factor integer not null,
  reps integer not null, lapses integer not null, left integer not null, odue integer not null,
  odid integer not null, flags integer not null, data text not null);
CREATE TABLE revlog (id integer primary key, cid integer not null, usn integer not null,
  ease integer not null, ivl integer not null, lastIvl integer not null, factor integer not null,
  time integer not null, type integer not null);
CREATE TABLE graves (usn integer not null, oid integer not null, type integer not null);
CREATE INDEX ix_notes_usn on notes (usn);
CREATE INDEX ix_cards_usn on cards (usn);
CREATE INDEX ix_revlog_usn on revlog (usn);
CREATE INDEX ix_cards_nid on cards (nid);
CREATE INDEX ix_cards_sched on cards (did, queue, due);
CREATE INDEX ix_revlog_cid on revlog (cid);
CREATE INDEX ix_notes_csum on notes (csum);
"""

BASE91 = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
          "!#$%&()*+,-./:;<=>?@[]^_`{|}~")


def guid_estavel(semente: str) -> str:
    """GUID novo e reproduzível: reimportar atualiza a nota em vez de duplicá-la."""
    valor = int.from_bytes(hashlib.sha256(semente.encode()).digest()[:8], "big")
    saida = []
    while valor and len(saida) < 10:
        valor, resto = divmod(valor, len(BASE91))
        saida.append(BASE91[resto])
    return "".join(saida) or "a"


def checksum(primeiro_campo: str) -> int:
    texto = re.sub(r"\[sound:[^]]+\]", "", primeiro_campo)
    texto = re.sub(r"<[^>]+>", "", texto).strip()
    return int(hashlib.sha1(texto.encode("utf-8")).hexdigest()[:8], 16)


def texto_puro(valor: str) -> str:
    return re.sub(r"<[^>]+>", "", valor or "").strip()


def carregar_notetypes(pacote: Path) -> dict:
    with zipfile.ZipFile(pacote) as zf:
        nomes = set(zf.namelist())
        for candidato in ("collection.anki21", "collection.anki2"):
            if candidato in nomes:
                bruto = zf.read(candidato)
                break
        else:
            raise SystemExit(f"{pacote} não tem coleção legível")
    with tempfile.NamedTemporaryFile(suffix=".anki2", delete=False) as tmp:
        tmp.write(bruto)
        caminho = tmp.name
    con = sqlite3.connect(caminho)
    modelos = json.loads(con.execute("select models from col").fetchone()[0])
    con.close()
    Path(caminho).unlink(missing_ok=True)
    return {modelo["name"]: modelo for modelo in modelos.values()}


def derivar_cloze_nebli(base: dict) -> dict:
    """Cloze NEBLI com o tema em campo, não no template.

    O note type de origem trazia `BIOQUÍMICA · METABOLISMO DO GLICOGÊNIO` escrito
    dentro do template — o cabeçalho de uma aula antiga aparecia em toda aula nova.
    """
    modelo = json.loads(json.dumps(base))
    modelo["name"] = "Cloze NEBLI - Aula"
    nomes = [campo["name"] for campo in modelo["flds"]]
    if "Tema" not in nomes:
        molde = json.loads(json.dumps(modelo["flds"][1]))
        molde.update({"name": "Tema", "ord": len(modelo["flds"])})
        modelo["flds"].append(molde)
    for template in modelo["tmpls"]:
        for chave in ("qfmt", "afmt"):
            template[chave] = re.sub(
                r'<div class="meta">[^<]*</div>',
                '<div class="meta">{{Tema}}</div>',
                template[chave],
            )
    modelo["css"] = CLOZE_CSS
    return modelo


CLOZE_CSS = """
.card { font-family: -apple-system, "Segoe UI", system-ui, sans-serif;
        font-size: 20px; line-height: 1.55; text-align: left;
        color: #1F2E3D;
        padding: 24px clamp(16px, 4vw, 40px) 40px; }
@media (min-width: 900px) { .card { font-size: 22px; } }

/* Uma coluna só. O cabeçalho fora do contêiner era o que desalinhava o card:
   `.meta` colava na borda e o texto ficava centralizado num miolo estreito. */
.meta, .prompt, .extra, .media, .source, hr#answer {
  max-width: 44rem; margin-left: auto; margin-right: auto; }

.meta { font-size: .62em; letter-spacing: .1em; text-transform: uppercase;
        font-weight: 700; color: #0E6B7A; margin-bottom: 1.1em; }
.prompt { text-wrap: pretty; }
.cloze { font-weight: 700; color: #0B5F6B;
         background: rgba(14, 107, 122, .12);
         padding: .05em .3em; border-radius: .25em; }
hr#answer { border: 0; border-top: 1px solid #D8D2C5; margin: 1.6em auto 1.2em; }
.extra { font-size: .84em; color: #3E4C5A; }
.media { margin-top: 1.1em; text-align: center; }
.media img { max-width: 100%; max-height: 62vh; height: auto;
             object-fit: contain; background: #fff; border-radius: 8px;
             box-shadow: 0 1px 4px rgba(0,0,0,.14); }
.source { margin-top: 1.4em; font-size: .55em; color: #8A94A0; }

/* AnkiDroid antigo usa .nightMode; as versões novas usam .night_mode. */
.night_mode .card, .nightMode .card, .card.night_mode { color: #E6EAF0; }
.night_mode .meta, .nightMode .meta { color: #56C4D4; }
.night_mode .cloze, .nightMode .cloze {
  color: #7FDCEA; background: rgba(86, 196, 212, .16); }
.night_mode .extra, .nightMode .extra { color: #C3CEDA; }
.night_mode .source, .nightMode .source { color: #7C8794; }
.night_mode hr#answer, .nightMode hr#answer { border-top-color: #3A424C; }
"""

IO_CSS = """
.card { font-family: -apple-system, "Segoe UI", system-ui, sans-serif;
        font-size: 19px; text-align: center; color: #1F2E3D; }
.night_mode .card, .nightMode .card, .card.night_mode { color: #E6EAF0; }
.io-header { font-size: 17px; font-weight: 600; color: #0E6B7A;
             margin: 0 auto 14px; max-width: 46em; line-height: 1.45; }
.night_mode .io-header, .nightMode .io-header { color: #56C4D4; }
.io-img img { max-width: 100%; height: auto; border-radius: 6px;
              box-shadow: 0 1px 4px rgba(0,0,0,.18); }
hr#answer { border: none; border-top: 1px solid #D8D2C5; margin: 18px auto; max-width: 40em; }
.night_mode hr#answer, .nightMode hr#answer { border-top-color: #3A424C; }
.io-extra { font-size: 16px; margin: 10px auto; max-width: 44em; }
.io-labels { font-size: 15px; color: #475569; margin: 8px auto; max-width: 44em; line-height: 1.6; }
.night_mode .io-labels, .nightMode .io-labels { color: #9FB0C2; }
.io-src { font-size: 12px; color: #8A94A0; margin-top: 14px; }
"""

IO_QFMT = """<div class="io-header">{{Header}}</div>
<div class="io-img">{{ImagemPergunta}}</div>"""

IO_AFMT = """<div class="io-header">{{Header}}</div>
<div class="io-img">{{ImagemResposta}}</div>
<hr id="answer">
{{#Extra}}<div class="io-extra">{{Extra}}</div>{{/Extra}}
{{#Rotulos}}<div class="io-labels">{{Rotulos}}</div>{{/Rotulos}}
{{#Fonte}}<div class="io-src">{{Fonte}}</div>{{/Fonte}}"""


def construir_io_nebli(agora: int) -> dict:
    """Note type de Image Occlusion com as máscaras já queimadas na imagem.

    O note type `IO-one by one` do AnKing não serve ao mapa coerente desta
    aula: a frente dele não mostra imagem alguma ("please flip to the
    backside"), o desenho das oclusões depende de JS do add-on e o template
    referencia mídia do AnKing que não acompanha o pacote.

    Como `hide_all_guess_all` recupera o mapa inteiro de uma vez, duas imagens
    pré-renderizadas — pergunta com todos os rótulos cobertos, resposta com
    todos revelados — dão exatamente o mesmo comportamento sem JS, sem add-on
    e sem diferença entre desktop, AnkiDroid e AnkiMobile. As coordenadas
    continuam no campo `I0` para auditoria e regeração.
    """
    campos = ["Header", "ImagemPergunta", "ImagemResposta", "Extra",
              "Rotulos", "I0", "Fonte", "NEBLI_Comentario", "NEBLI_Resposta"]
    return {
        "name": "IO NEBLI - Image Occlusion (mapa coerente)",
        "type": 0,
        "mod": agora,
        "usn": -1,
        "sortf": 0,
        "did": 1,
        "latexPre": "\\documentclass[12pt]{article}\n\\begin{document}\n",
        "latexPost": "\\end{document}",
        "latexsvg": False,
        "req": [[0, "any", [0, 1]]],
        "tags": [],
        "vers": [],
        "css": IO_CSS,
        "flds": [
            {"name": nome, "ord": indice, "sticky": False, "rtl": False,
             "font": "Arial", "size": 20, "description": "", "plainText": False,
             "collapsed": False, "excludeFromSearch": False}
            for indice, nome in enumerate(campos)
        ],
        "tmpls": [{
            "name": "Mapa coerente", "ord": 0,
            "qfmt": IO_QFMT, "afmt": IO_AFMT,
            "did": None, "bqfmt": "", "bafmt": "", "bfont": "", "bsize": 0,
        }],
    }


UC_RE = re.compile(r"^UC\d{2}$")
PROVA_RE = re.compile(r"^P\d$")


def validar_arvore(deck: str, opcional: str) -> None:
    """A árvore é NEBLI::<UC>::<Prova>::<Componente>::<Aula>, com Optional pendurado nela.

    Existe como gate porque já saiu deck fora do padrão: o cronograma da UC sugeria
    `NEBLI::Digestório::P1::…` e a coleção real usa o código da UC (`NEBLI::UC02::P3::…`).
    Um galho de topo diferente não dá erro em lugar nenhum — só espalha a coleção.
    """
    partes = deck.split("::")
    problemas = []
    if len(partes) != 5:
        problemas.append(
            f"a árvore precisa de 5 níveis (NEBLI::UC::Prova::Componente::Aula), veio {len(partes)}"
        )
    else:
        raiz, uc, prova, componente, aula = partes
        if raiz != "NEBLI":
            problemas.append(f"o primeiro nível é 'NEBLI', veio {raiz!r}")
        if not UC_RE.match(uc):
            problemas.append(
                f"a UC entra como código de dois dígitos (UC02, UC08), veio {uc!r} — "
                "nome por extenso cria um galho separado na coleção"
            )
        if not PROVA_RE.match(prova):
            problemas.append(f"a prova é P1, P2, P3…, veio {prova!r}")
        if not componente.strip() or not aula.strip():
            problemas.append("componente e aula não podem ser vazios")
    if opcional != f"{deck}::Optional":
        problemas.append(f"o subdeck opcional é '{deck}::Optional', veio {opcional!r}")
    if problemas:
        raise SystemExit("árvore de decks fora do padrão:\n  - " + "\n  - ".join(problemas))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("contrato")
    ap.add_argument("--notetype-source", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--novos-dia", type=int, default=25)
    ap.add_argument("--revisoes-dia", type=int, default=9999)
    args = ap.parse_args()

    contrato = json.loads(Path(args.contrato).read_text(encoding="utf-8"))
    contrato_dir = Path(args.contrato).resolve().parent
    slug = contrato["slug"]
    deck_principal = contrato["deck"]
    deck_opcional = contrato["optional_deck"]
    validar_arvore(deck_principal, deck_opcional)

    disponiveis = carregar_notetypes(RAIZ / args.notetype_source)
    if "Cloze Medicina - Mecanismo Único" not in disponiveis:
        raise SystemExit("note type de cloze base não encontrado no pacote de origem")
    agora = int(time.time())
    modelos = {
        "Cloze NEBLI - Aula": derivar_cloze_nebli(disponiveis["Cloze Medicina - Mecanismo Único"]),
        "IO NEBLI - Image Occlusion (mapa coerente)": construir_io_nebli(agora),
    }

    proximo_id = agora * 1000

    def novo_id() -> int:
        nonlocal proximo_id
        proximo_id += 1
        return proximo_id

    modelos_json, mid_por_nome = {}, {}
    for nome, modelo in modelos.items():
        mid = novo_id()
        modelo = json.loads(json.dumps(modelo))
        modelo["id"] = mid
        modelo["mod"] = agora
        modelo["usn"] = -1
        for indice, campo in enumerate(modelo["flds"]):
            campo["ord"] = indice
        for indice, template in enumerate(modelo["tmpls"]):
            template["ord"] = indice
        modelos_json[str(mid)] = modelo
        mid_por_nome[nome] = mid

    # Árvore de decks: cada nível precisa existir para o Anki aninhar corretamente.
    decks_json, did_por_nome = {}, {}
    caminhos = set()
    for completo in (deck_principal, deck_opcional):
        partes = completo.split("::")
        for corte in range(1, len(partes) + 1):
            caminhos.add("::".join(partes[:corte]))
    for nome in sorted(caminhos):
        did = novo_id()
        decks_json[str(did)] = {
            "id": did, "name": nome, "mod": agora, "usn": -1, "desc": "",
            "dyn": 0, "collapsed": False, "browserCollapsed": False,
            "extendNew": 10, "extendRev": 50, "conf": 1, "lrnToday": [0, 0],
            "revToday": [0, 0], "newToday": [0, 0], "timeToday": [0, 0],
        }
        did_por_nome[nome] = did

    dconf = {"1": {
        "id": 1, "name": "NEBLI", "mod": agora, "usn": -1, "maxTaken": 60,
        "autoplay": True, "timer": 0, "replayq": True,
        "new": {"bury": False, "delays": [1.0, 10.0], "initialFactor": 2500,
                "ints": [1, 4, 0], "order": 1, "perDay": args.novos_dia},
        "rev": {"bury": False, "ease4": 1.3, "ivlFct": 1.0, "maxIvl": 36500,
                "perDay": args.revisoes_dia, "hardFactor": 1.2},
        "lapse": {"delays": [10.0], "leechAction": 1, "leechFails": 8,
                  "minInt": 1, "mult": 0.0},
        "dyn": False, "newMix": 0, "newPerDayMinimum": 0, "interdayLearningMix": 0,
        "reviewOrder": 0, "newSortOrder": 0, "newGatherPriority": 0, "buryInterdayLearning": False,
    }}

    conf = {
        "activeDecks": [1], "curDeck": did_por_nome[deck_principal], "newSpread": 0,
        "collapseTime": 1200, "timeLim": 0, "estTimes": True, "dueCounts": True,
        "curModel": mid_por_nome["Cloze NEBLI - Aula"], "nextPos": 1,
        "sortType": "noteFld", "sortBackwards": False, "addToCur": True, "dayLearnFirst": False,
        "schedVer": 2,
    }

    trabalho = Path(tempfile.mkdtemp(prefix="nebli-apkg-"))
    colecao = trabalho / "collection.anki2"
    con = sqlite3.connect(colecao)
    con.executescript(SCHEMA)
    con.execute(
        "insert into col values (1,?,?,?,11,0,0,0,?,?,?,?,?)",
        (agora, agora * 1000, agora * 1000, json.dumps(conf), json.dumps(modelos_json),
         json.dumps(decks_json), json.dumps(dconf), "{}"),
    )

    # ---- mídia: nomes achatados, deduplicação por hash -------------------
    midia_por_hash: dict[str, str] = {}
    midia_arquivos: dict[str, Path] = {}
    colisoes: list[str] = []

    def registrar_midia(nome_destino: str, origem: Path) -> str:
        if not origem.exists():
            raise SystemExit(f"mídia ausente: {origem}")
        digest = hashlib.sha256(origem.read_bytes()).hexdigest()
        if digest in midia_por_hash:
            return midia_por_hash[digest]
        final = nome_destino
        if final in midia_arquivos:
            final = f"nebli-{digest[:8]}-{nome_destino}"
            colisoes.append(f"{nome_destino} → {final}")
        midia_arquivos[final] = origem
        midia_por_hash[digest] = final
        return final

    def resolver_html(valor: str) -> str:
        """Troca caminhos de repositório por nomes de mídia dentro do HTML."""
        def troca(match: re.Match) -> str:
            src = match.group(1)
            if not src.startswith("/figuras/"):
                return match.group(0)
            origem = RAIZ / src.lstrip("/")
            plano = src.lstrip("/").replace("figuras/", "").replace("/", "-")
            return f'src="{registrar_midia(plano, origem)}"'
        return IMG_RE.sub(troca, valor or "")

    notas, cartoes, etiquetas = 0, 0, set()
    relatorio_cards = []

    for card in contrato["cards"]:
        nota = card["note"]
        modelo = modelos_json[str(mid_por_nome[nota["model"]])]
        nomes_campos = [campo["name"] for campo in modelo["flds"]]

        for destino, origem in (nota.get("media") or {}).items():
            registrar_midia(destino, Path(origem))

        campos = [resolver_html(nota["fields"].get(nome, "")) for nome in nomes_campos]
        nid = novo_id()
        tags = " " + " ".join(nota["tags"]) + " "
        etiquetas.update(nota["tags"])
        primeiro = campos[modelo.get("sortf", 0)]
        con.execute(
            "insert into notes values (?,?,?,?,-1,?,?,?,?,0,'')",
            (nid, guid_estavel(f"{slug}:{card['id']}"), modelo["id"], agora, tags,
             "\x1f".join(campos), texto_puro(primeiro), checksum(campos[0])),
        )
        notas += 1

        deck = deck_opcional if card["importance"] == "opcional" else deck_principal
        did = did_por_nome[deck]

        if modelo["type"] == 1:  # cloze: um card por ordinal presente
            ordinais = sorted({int(n) - 1 for n in re.findall(r"\{\{c(\d+)::", campos[0])})
        else:
            ordinais = list(range(len(modelo["tmpls"])))
        if not ordinais:
            raise SystemExit(f"nota sem card gerado: {card['id']}")

        for ordinal in ordinais:
            con.execute(
                "insert into cards values (?,?,?,?,?,-1,0,0,?,0,0,0,0,0,0,0,0,'')",
                (novo_id(), nid, did, ordinal, agora, cartoes + 1),
            )
            cartoes += 1

        relatorio_cards.append({
            "id": card["id"], "deck": deck, "model": nota["model"],
            "importance": card["importance"], "cards": len(ordinais),
        })
        if len(ordinais) != card["generated_card_count"]:
            raise SystemExit(
                f"{card['id']}: contrato prevê {card['generated_card_count']} card(s), "
                f"a montagem gerou {len(ordinais)}"
            )

    con.execute("update col set tags=?", (json.dumps({tag: -1 for tag in sorted(etiquetas)}),))
    con.commit()
    con.close()

    mapa_midia = {}
    for indice, (nome, origem) in enumerate(sorted(midia_arquivos.items())):
        shutil.copyfile(origem, trabalho / str(indice))
        mapa_midia[str(indice)] = nome
    (trabalho / "media").write_text(json.dumps(mapa_midia, ensure_ascii=False), encoding="utf-8")

    destino = Path(args.out)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(colecao, "collection.anki2")
        zf.write(trabalho / "media", "media")
        for indice in mapa_midia:
            zf.write(trabalho / indice, indice)
    shutil.rmtree(trabalho, ignore_errors=True)

    previsto = sum(card["generated_card_count"] for card in contrato["cards"])
    teto = contrato["card_budget"]["hard_max"]
    if cartoes != previsto:
        raise SystemExit(f"total real {cartoes} ≠ previsto no contrato {previsto}")
    if cartoes > teto:
        raise SystemExit(f"total real {cartoes} excede o teto congelado {teto}")

    relatorio = {
        "apkg": str(destino),
        "sha256": hashlib.sha256(destino.read_bytes()).hexdigest(),
        "bytes": destino.stat().st_size,
        "notes": notas,
        "cards": cartoes,
        "expected_cards": previsto,
        "hard_max": teto,
        "decks": sorted(did_por_nome),
        "notetypes": sorted(mid_por_nome),
        "media_files": len(mapa_midia),
        "media_deduplicated": len(midia_por_hash) - len(mapa_midia),
        "media_name_collisions": colisoes,
        "scheduling": {"new_per_day": args.novos_dia, "reviews_per_day": args.revisoes_dia},
        "cards_detail": relatorio_cards,
    }
    (contrato_dir / "relatorio-montagem.json").write_text(
        json.dumps(relatorio, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({chave: relatorio[chave] for chave in
                      ("apkg", "notes", "cards", "expected_cards", "media_files", "bytes")},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
