"""Abertura e evidência de corrida de deck-aula (campanha de 08/10; um comando por etapa, sem decidir conteúdo).

    python3 -m nebli.corrida abrir <pasta> --slides a.pdf [b.pdf ...] [--transcricao t.pdf] [--extra rótulo=arquivo ...]
        cria <pasta>/{fontes,livros,canais,busca,visual,img,io}; junta os slides em fontes/slides.pdf (ordem dada),
        extrai texto por página em fontes/slides.txt, copia transcrição/extras (PDF → .pdf + .txt) e gera
        visual/folha-NN.png (6 lâminas por folha, para ver todas antes de planejar).
    python3 -m nebli.corrida livro <pasta> <pdf> <pag-ini> <pag-fim> <nome>   # capítulo → livros/<nome>.txt (+ páginas)
    python3 -m nebli.corrida video <pasta> <url-youtube> <canal> <nome>        # transcrição → canais/<nome>.txt
    python3 -m nebli.corrida youtube "<busca>"                                # vídeos (id | título | canal) da busca do YouTube
    python3 -m nebli.corrida evidencias <pasta>                                # recalcula sha256 de fontes.json["evidencias"]
    python3 -m nebli.corrida molde <pasta>                                     # copia spec/inventario/build/apply/compreensao-aula do molde (nebli/molde), sem sobrescrever
    python3 -m nebli.corrida fontes <pasta>                                    # fontes-decl.json (declaração curta, escrita depois de ler) → fontes.json com hashes e alvos
    python3 -m nebli.corrida cego <pasta> [n]                                  # amostra cega card-mirror: n autorais + n AnKing da aula (card-mirror/entrada.txt + gabarito.json)
    python3 -m nebli.corrida revisado <pasta> [--corrigidos k1,k2]             # revisao-inventario.json item a item a partir de cobertura.json + receipt.json

Nada aqui marca leitura: o registro de que a fonte foi lida e o que mudou no plano é escrito à mão em fontes.json,
depois de ler. O gate (`nebli.gates --fontes`) confere arquivo, hash, localizador, contribuição e alvos.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
import re
import shutil
from pathlib import Path

import fitz


def _txt(pdf: Path, out: Path):
    with fitz.open(pdf) as d:
        out.write_text("\n".join(f"===== página {i} =====\n{p.get_text()}" for i, p in enumerate(d, 1)), encoding="utf-8")


def abrir(pasta: Path, slides: list[str], transcricao: str | None, extras: list[str]):
    for sub in ("fontes", "livros", "canais", "busca", "visual", "img", "io"):
        (pasta / sub).mkdir(parents=True, exist_ok=True)
    out = fitz.open()
    for s in slides:
        with fitz.open(s) as d:
            out.insert_pdf(d)
    out.save(pasta / "fontes" / "slides.pdf")
    n = len(out)
    _txt(pasta / "fontes" / "slides.pdf", pasta / "fontes" / "slides.txt")
    if transcricao:
        shutil.copy(transcricao, pasta / "fontes" / "transcricao.pdf")
        _txt(pasta / "fontes" / "transcricao.pdf", pasta / "fontes" / "transcricao.txt")
    for e in extras:
        nome, arq = e.split("=", 1)
        dst = pasta / "fontes" / f"{nome}{Path(arq).suffix.lower()}"
        shutil.copy(arq, dst)
        if dst.suffix == ".pdf":
            _txt(dst, dst.with_suffix(".txt"))
    folhas(pasta, n)
    print(f"{pasta}: {n} lâminas; folhas em visual/")


def folhas(pasta: Path, n: int, por=6, largura=560):
    d = fitz.open(pasta / "fontes" / "slides.pdf")
    for f in range(0, n, por):
        doc = fitz.open()
        r0 = d[0].rect
        h = largura * r0.height / r0.width
        page = doc.new_page(width=largura * 2, height=(h + 18) * 3)
        for k, i in enumerate(range(f, min(f + por, n))):
            x, y = (k % 2) * largura, (k // 2) * (h + 18)
            page.insert_text((x + 4, y + 13), f"lâmina {i + 1}", fontsize=12, color=(0.8, 0, 0))
            page.show_pdf_page(fitz.Rect(x, y + 16, x + largura, y + 16 + h), d, i)
        page.get_pixmap(dpi=80).save(pasta / "visual" / f"folha-{f // por + 1:02d}.png")


def livro(pasta: Path, pdf: str, ini: int, fim: int, nome: str):
    with fitz.open(pdf) as d:
        txt = "\n".join(f"===== pdf p. {i + 1} =====\n{d[i].get_text()}" for i in range(ini - 1, fim))
    (pasta / "livros" / f"{nome}.txt").write_text(txt, encoding="utf-8")
    print(pasta / "livros" / f"{nome}.txt", len(txt.split()), "palavras")


def video(pasta: Path, url: str, canal: str, nome: str):
    from youtube_transcript_api import YouTubeTranscriptApi
    vid = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", url).group(1)
    try:
        partes = YouTubeTranscriptApi().fetch(vid, languages=["en", "pt", "pt-BR"])
        texto = " ".join(p.text for p in partes)
    except AttributeError:  # versões antigas da biblioteca
        texto = " ".join(p["text"] for p in YouTubeTranscriptApi.get_transcript(vid, languages=["en", "pt", "pt-BR"]))
    (pasta / "canais" / f"{nome}.txt").write_text(f"{canal} — {url}\n\n{texto}", encoding="utf-8")
    print(pasta / "canais" / f"{nome}.txt", len(texto.split()), "palavras")


def youtube(busca: str):
    import urllib.parse, urllib.request
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(busca)
    h = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read().decode("utf-8", "replace")
    for m in re.finditer(r'"videoRenderer":\{"videoId":"([\w-]{11})".*?"title":\{"runs":\[\{"text":"(.*?)"\}.*?"ownerText":\{"runs":\[\{"text":"(.*?)"', h):
        print(f"https://youtu.be/{m.group(1)} | {m.group(2)[:80]} | {m.group(3)}")


def evidencias(pasta: Path):
    f = json.loads((pasta / "fontes.json").read_text())
    for fam, recs in f.get("evidencias", {}).items():
        for r in recs:
            if r.get("estado") == "consultada":
                r["sha256"] = hashlib.sha256((pasta / r["arquivo"]).read_bytes()).hexdigest()
    (pasta / "fontes.json").write_text(json.dumps(f, ensure_ascii=False, indent=1))
    print("hashes atualizados")


MOLDE = Path(__file__).parent / "molde"


def molde(pasta: Path):
    pasta.mkdir(parents=True, exist_ok=True)
    for f in ("spec.py", "inventario.py", "build.py", "apply.py", "compreensao-aula.json"):
        if not (pasta / f).exists():
            shutil.copy(MOLDE / f, pasta / f)
            print("copiado", f)


def fontes(pasta: Path):
    """fontes-decl.json: {"nome","escopo":"cards"|"e1+cards","drive_pasta","pasta_turma","turma_lidos":[..],"turma_descartados":{..},
    "slides":"fontes/slides.pdf","n_laminas":N,
    "familias":{"slides":[{"arquivo","localizador","contribuicao","alvos":"slides"|"todos"|"cap"|"prova"|[ids]}],
                "bibliografia":[...], "veteranos":[...], "provas":[...],
                "caoc"|"exercicios"|"youtube": {"estado":"não localizada"|"inacessível","busca","impacto"}},
    "livros":[{"livro","texto"}], "canais":[{"canal","url","transcricao","calibracao"}], "canais_bloqueados":{...},
    "materiais_uc":{"<nome do arquivo>": {"texto": "fontes/x.txt", "secao": "pp. 12–18"} | {"descartado": "motivo"}},
    "pastas_extra":["<pasta absoluta a varrer inteira>"]}
    Só declara o que foi lido; o hash e a lista de alvos vêm do disco e do planejamento.json."""
    d = json.loads((pasta / "fontes-decl.json").read_text())
    # F-20261021-CLAUDE-06: a dispensa de vídeos foi revogada; ler pelo menos um vídeo de canal que Davi acompanha
    # (`corrida youtube "<busca>"` e `corrida video ...`) e declarar em "canais" e em familias.youtube.
    if not d.get("canais"):
        raise SystemExit("fontes-decl.json sem 'canais': ler ≥ 1 vídeo do YouTube (canal que Davi acompanha) antes de declarar as fontes.")
    scope = d.get("escopo", "cards")
    if scope not in {"cards", "e1+cards"}:
        raise ValueError(f"escopo inválido em fontes-decl.json: {scope!r}")
    alvos = [a["id"] for a in json.loads((pasta / "planejamento.json").read_text())["alvos"]]
    grupos = {"slides": [a for a in alvos if re.search(r"-s\d\d", a)], "cap": [a for a in alvos if "-cap-" in a],
              "prova": [a for a in alvos if "-prova-" in a], "todos": alvos}
    ev = {}
    for fam, recs in d["familias"].items():
        if isinstance(recs, dict):
            ev[fam] = [{"estado": recs["estado"], "essencial": False, "busca": recs["busca"], "impacto": recs["impacto"]}]
            continue
        ev[fam] = []
        for r in recs:
            al = r.get("alvos", "slides")
            al = grupos[al] if isinstance(al, str) else al
            ev[fam].append({"estado": "consultada", "arquivo": r["arquivo"], "sha256": hashlib.sha256((pasta / r["arquivo"]).read_bytes()).hexdigest(),
                            "leitura": "integral", "localizador": r["localizador"], "contribuicao": r["contribuicao"],
                            "lida_antes_da_selecao": True, "alvos": al or alvos[:1]})
        if fam == "youtube":
            for r, src in zip(ev[fam], recs):
                r.update(canal=src["canal"], url=src["url"])
    estado = lambda fam: (ev.get(fam) or [{}])[0].get("estado", "não localizada")
    out = {"nome": d["nome"], "escopo": scope, "drive_pasta": d.get("drive_pasta", ""),
           "slides": {"arquivo": d.get("slides", "fontes/slides.pdf"), "todas_vistas": True, "obs": f"{d.get('n_laminas', '?')} lâminas vistas em visual/folha-NN"},
           "livros": [dict(l, lido=True) for l in d.get("livros", [])],
           "canais": [dict(c, lido="integral") for c in d.get("canais", [])],
           "evidencias": ev, "pasta_turma": d.get("pasta_turma", {"nao_ha": "busca não registrada"}),
           "turma_arquivos_lidos": d.get("turma_lidos", []), "turma_descartados": d.get("turma_descartados", {})}
    for fam in ("provas", "exercicios", "caoc", "veteranos"):
        rec = d["familias"].get(fam)
        out[fam] = ({"estado": "consultada", "contribuicao": "; ".join(r["contribuicao"] for r in rec)} if isinstance(rec, list)
                    else {"estado": rec["estado"], "busca": rec["busca"], "impacto": rec["impacto"]} if rec else {"estado": "não localizada", "busca": "não registrada"})
    # F-20261015-CLAUDE-05: gate duro de materiais da UC (apostilas, Outros, Material para Estudos, pasta pessoal da aula).
    out["materiais_uc"] = d.get("materiais_uc", {})
    out["pastas_extra"] = d.get("pastas_extra", [])
    if d.get("sem_laminas"):  # F-20261016-CLAUDE-05: aula sem lâminas; o roteiro da aula ocupa o lugar do PDF
        out["sem_laminas"] = d["sem_laminas"]
        out["slides"]["obs"] = f"aula sem lâminas: roteiro da aula em {out['slides']['arquivo']} ({d['sem_laminas'].get('feedback')})"
    for k in ("canais_bloqueados", "ninja_nerd_busca"):
        if d.get(k):
            out[k] = d[k]
    (pasta / "fontes.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    pl = json.loads((pasta / "planejamento.json").read_text())
    pl["fontes"] = {fam: {"estado": estado(fam), "contribuicao": "; ".join(r.get("contribuicao", r.get("impacto", "")) for r in ev.get(fam, [])) or "não registrada"}
                    for fam in ("slides", "bibliografia", "caoc", "youtube", "veteranos", "provas", "exercicios")}
    (pasta / "planejamento.json").write_text(json.dumps(pl, ensure_ascii=False, indent=1))
    print("fontes.json e planejamento.json['fontes'] escritos;", {k: len(v) for k, v in ev.items()})


def cego(pasta: Path, n: int = 12):
    import random
    plan = json.loads((pasta / "plan.json").read_text())
    au = [e for e in plan["entries"] if e["origin"] == "Autoral"]; ak = [e for e in plan["entries"] if e["origin"] == "AnKing"]
    rnd = random.Random(plan["run_id"])
    itens = [("Autoral", e) for e in rnd.sample(au, min(n, len(au)))] + [("AnKing", e) for e in rnd.sample(ak, min(n, len(ak)))]
    rnd.shuffle(itens)
    norm = lambda x: (re.sub(r"(?i)(photo credit|image licensed).*", "", re.sub(r"<img[^>]*>", "[figure]", x or "")).strip() or "(empty)")
    (pasta / "card-mirror").mkdir(exist_ok=True)
    (pasta / "card-mirror" / "entrada.txt").write_text("\n".join(f"C{i}\nFRONT: {norm(e['fields'].get('Text'))}\nEXTRA: {norm(e['fields'].get('Extra'))}\n"
                                                         for i, (_, e) in enumerate(itens, 1)))
    (pasta / "card-mirror" / "gabarito.json").write_text(json.dumps({f"C{i}": {"orig": o, "id": e["key"]} for i, (o, e) in enumerate(itens, 1)}, indent=1))
    print(f"{len(itens)} cards em card-mirror/entrada.txt; gabarito separado (não dar ao juiz)")


def revisado(pasta: Path, corrigidos: list[str]):
    cov = json.loads((pasta / "cobertura.json").read_text())
    rec = {x["key"]: x["nid"] for x in json.loads((pasta / "receipt.json").read_text())["notes"]}
    itens = {}
    for i in cov["itens"]:
        cards = i.get("cards") or []
        if cards:
            fix = [c for c in cards if c in corrigidos]
            itens[i["id"]] = {"veredito": "corrigido" if fix else "ok", "card_visto": ", ".join(f"{c} ({rec.get(c, c[3:] if c.startswith('sh-') else '?')})" for c in cards),
                              "nota": "lido no despejo vivo (python3 -m nebli.revisar)" + (f"; corrigido: {', '.join(fix)}" if fix else "")}
        else:
            itens[i["id"]] = {"veredito": "ok", "card_visto": "exclusão: " + str(i.get("excluido", ""))[:100]}
    (pasta / "revisao-inventario.json").write_text(json.dumps({"feita_depois_de_instalar": True, "itens": itens}, ensure_ascii=False, indent=1))
    print(len(itens), "itens revisados")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("abrir"); a.add_argument("pasta"); a.add_argument("--slides", nargs="+", required=True)
    a.add_argument("--transcricao"); a.add_argument("--extra", nargs="*", default=[])
    l = sp.add_parser("livro"); l.add_argument("pasta"); l.add_argument("pdf"); l.add_argument("ini", type=int); l.add_argument("fim", type=int); l.add_argument("nome")
    v = sp.add_parser("video"); v.add_argument("pasta"); v.add_argument("url"); v.add_argument("canal"); v.add_argument("nome")
    e = sp.add_parser("evidencias"); e.add_argument("pasta")
    y = sp.add_parser("youtube"); y.add_argument("busca")
    for c in ("molde", "fontes"):
        sp.add_parser(c).add_argument("pasta")
    cg = sp.add_parser("cego"); cg.add_argument("pasta"); cg.add_argument("n", nargs="?", type=int, default=12)
    rv = sp.add_parser("revisado"); rv.add_argument("pasta"); rv.add_argument("--corrigidos", default="")
    x = ap.parse_args(argv)
    if x.cmd == "youtube":
        return youtube(x.busca)
    p = Path(x.pasta)
    if x.cmd == "abrir":
        abrir(p, x.slides, x.transcricao, x.extra)
    elif x.cmd == "livro":
        livro(p, x.pdf, x.ini, x.fim, x.nome)
    elif x.cmd == "video":
        video(p, x.url, x.canal, x.nome)
    elif x.cmd == "molde":
        molde(p)
    elif x.cmd == "fontes":
        fontes(p)
    elif x.cmd == "cego":
        cego(p, x.n)
    elif x.cmd == "revisado":
        revisado(p, [c for c in x.corrigidos.split(",") if c])
    else:
        evidencias(p)


if __name__ == "__main__":
    main()
