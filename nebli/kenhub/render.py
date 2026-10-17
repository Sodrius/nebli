"""Renderiza o deck inteiro como o Anki monta (frente e verso, PC e celular) e reprova o que renderiza mal.

Gate duro de renderização (F-20261017-CLAUDE-02: “sempre tem que renderizar o deck todo no final para ver”). Cada gate leva o
id do feedback de Davi que o criou (registro: nebli/kenhub/feedbacks.json); feedback novo vira gate novo aqui ou no deck.py.

  G1  frente-só-imagem     IO: a frente não tem texto além da Pergunta (quando a figura inteira é a pergunta).
  G2  resposta-sem-rolar   IO: o nome em PT no topo do verso; Cloze: a lacuna revelada — dentro da primeira tela (PC e celular).
  G4  imagens-inteiras     nenhuma imagem quebrada; a figura do IO cabe inteira na tela.
  G5  máscara-esconde      Kenhub: na frente a marcação verde não aparece; no verso ela aparece.
  G6  deck-todo            todos os cards planejados renderizados (nunca passa no vazio).
  G9  sem-escolher-imagem  nenhum botão no card e nenhuma imagem escondida (nada de escolher entre cadáver e modelo).
  G11 resposta-no-lugar    IO com seta/ID: o verso tem a sobreposição com o nome escrito na figura.

Saída: <saida>/grandes/gNN.jpg (folhas para olhar) + relatorio.json. Uso: python -m nebli.kenhub.render '"tag:NEBLI::<lição>"' [saida]
"""
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

from nebli.kenhub import modelo

TELAS = {"pc": ({"width": 1280, "height": 800}, False), "cel": ({"width": 390, "height": 844}, True)}
JS = """() => {
  const r = e => { const b = e.getBoundingClientRect(); return {top: b.top, bottom: b.bottom, w: b.width, h: b.height}; };
  const q = s => document.querySelector(s);
  const imgs = [...document.images].filter(i => (i.getAttribute('src') || '') !== '')
     .map(i => ({src: i.getAttribute('src'), ok: i.complete && i.naturalWidth > 0,
                 visivel: i.offsetParent !== null && getComputedStyle(i).visibility !== 'hidden'}));
  const wrap = q('#kh-wrap'), nome = q('#kh-nome'), cloze = q('.cloze');
  return {texto: (document.getElementById('content')?.innerText || '').trim(), imgs, vh: window.innerHeight,
          botoes: document.querySelectorAll('button').length, sobre: document.querySelectorAll('.kh-over img').length,
          wrap: wrap ? r(wrap) : null, nome: nome ? r(nome) : null, nomeTexto: nome ? nome.innerText.trim() : '',
          cloze: cloze ? r(cloze) : null};
}"""


def _anki(acao, **params):
    corpo = json.dumps({"action": acao, "version": 6, "params": params}).encode()
    for tentativa in range(60):  # Anki ocupado com operação da coleção: esperar, não falhar
        r = json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", corpo), timeout=120))
        if r.get("error") and "lifecycle operation is active" in r["error"] and tentativa < 59:
            time.sleep(2)
            continue
        if r.get("error"):
            raise RuntimeError(f"{acao}: {r['error']}")
        return r["result"]


def _norm(t):
    """Compara textos sem depender de &amp;, pontuação, acento ou caixa."""
    return re.sub(r"[^a-z0-9]+", "", html.unescape(t).lower().translate(str.maketrans("áàâãéêíóôõúç", "aaaaeeiooouc")))


def _verde(arr):
    r, g, b = (arr[..., i].astype(int) for i in range(3))
    return int(((g > 70) & (g - r > 22) & (g - b > 8)).sum())


def _pagina(corpo, css, media, mobile):
    return (f'<html><head><meta charset="utf-8"><base href="file://{media}/"><style>{css}</style></head>'
            f'<body class="{"mobile" if mobile else ""}"><div id="content" class="card">{corpo}</div></body></html>')


def renderizar(consulta: str, saida: Path, nids_esperados):
    """Devolve (falhas, relatorio). `consulta`: busca do Anki (etiqueta da unidade — o nome do deck vivo traz contagens).
    `nids_esperados`: notas que o deck deve ter; o G6 reprova se as renderizadas não forem exatamente essas."""
    saida.mkdir(parents=True, exist_ok=True)
    media = _anki("getMediaDirPath")
    ids = sorted(_anki("findCards", query=consulta))
    cards = _anki("cardsInfo", cards=ids) if ids else []
    cards.sort(key=lambda c: (c["due"], c["cardId"]))
    css, falhas, itens, mini = {}, [], [], []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pg = {t: nav.new_context(viewport=vp, device_scale_factor=1).new_page() for t, (vp, _) in TELAS.items()}
        for c in cards:
            mod = c["modelName"]
            css.setdefault(mod, _anki("modelStyling", modelName=mod)["css"])
            io = mod == modelo.NOME
            f = c["fields"]
            fonte = f.get("Fonte", {}).get("value", "")
            pergunta = f.get("Pergunta", {}).get("value", "").strip() if io else ""
            reg = {"card": c["cardId"], "nota": c["note"], "modelo": mod, "falhas": []}
            fotos = {}
            for tela, (vp, mobile) in TELAS.items():
                for lado in ("question", "answer"):
                    arq = saida / f"{c['cardId']}-{tela}-{lado}.html"
                    arq.write_text(_pagina(c[lado], css[mod], media, mobile))
                    pg[tela].goto(f"file://{arq}")
                    pg[tela].wait_for_timeout(200)
                    m = pg[tela].evaluate(JS)
                    png = saida / f"{c['cardId']}-{tela}-{lado}.png"
                    pg[tela].screenshot(path=str(png))
                    fotos[(tela, lado)] = png
                    ruins = [i["src"] for i in m["imgs"] if not i["ok"]]
                    if ruins:
                        reg["falhas"].append(f"G4 imagem quebrada ({tela}/{lado}): {ruins[:2]}")
                    if m["botoes"] or any(not i["visivel"] for i in m["imgs"]):
                        reg["falhas"].append(f"G9 botão ou imagem escondida ({tela}/{lado})")
                    if io:
                        if m["wrap"] and m["wrap"]["bottom"] > m["vh"] + 1:
                            reg["falhas"].append(f"G4 figura não cabe na tela ({tela}/{lado})")
                        if lado == "question":
                            if _norm(m["texto"]) != _norm(pergunta):
                                reg["falhas"].append(f"G1 frente com texto além da pergunta ({tela}): {m['texto'][:40]!r}")
                        else:
                            if not m["nomeTexto"] or (m["nome"] and m["nome"]["bottom"] > m["vh"]):
                                reg["falhas"].append(f"G2 nome em PT ausente ou fora da primeira tela ({tela})")
                            if not pergunta and m["sobre"] < 1:
                                reg["falhas"].append(f"G11 verso sem a figura com o nome no lugar da pergunta ({tela})")
                    elif lado == "answer" and (not m["cloze"] or m["cloze"]["bottom"] > m["vh"]):
                        reg["falhas"].append(f"G2 lacuna revelada ausente ou fora da primeira tela ({tela})")
            if io and fonte == "Kenhub":
                for tela in TELAS:
                    a = _verde(np.asarray(Image.open(fotos[(tela, "answer")]).convert("RGB")))
                    qv = _verde(np.asarray(Image.open(fotos[(tela, "question")]).convert("RGB")))
                    if qv > 40 and qv > 0.2 * a:
                        reg["falhas"].append(f"G5 verde visível na frente ({tela}): {qv}px (verso {a}px)")
                    if a < 40:
                        reg["falhas"].append(f"G5 marcação não aparece no verso ({tela})")
            mini.append((c["cardId"], fotos[("pc", "question")], fotos[("pc", "answer")], reg["falhas"], mod))
            itens.append(reg)
        nav.close()
    achadas, previstas = {c["note"] for c in cards}, set(nids_esperados)
    if not cards or not previstas:
        falhas.append("G6 nada foi renderizado (consulta vazia ou plano vazio) — o gate não passa no vazio")
    elif achadas != previstas:
        falhas.append(f"G6 deck não renderizado por inteiro: faltam {len(previstas - achadas)} notas, sobram {len(achadas - previstas)}")
    for r in itens:
        falhas += [f"[{r['card']}] {x}" for x in r["falhas"]]
    folhas = _folhas(mini, saida / "grandes")
    rel = {"consulta": consulta, "cards": len(cards), "falhas": falhas, "folhas": [str(f) for f in folhas]}
    (saida / "relatorio.json").write_text(json.dumps(rel, ensure_ascii=False, indent=1))
    return falhas, rel


def _folhas(mini, pasta, por=8, W=360, H=225):
    """Folhas de contato: cada card = frente | verso (PC). Rótulo vermelho nos que reprovaram."""
    pasta.mkdir(parents=True, exist_ok=True)
    for f in pasta.glob("g*.jpg"):
        f.unlink()
    out = []
    for n in range(0, len(mini), por):
        g = mini[n:n + por]
        folha = Image.new("RGB", (4 * W + 20, ((len(g) + 1) // 2) * (H + 18)), "white")
        d = ImageDraw.Draw(folha)
        for k, (cid, q, a, falhas, mod) in enumerate(g):
            x, y = (k % 2) * (2 * W + 20), (k // 2) * (H + 18)
            for j, arq in enumerate((q, a)):
                im = Image.open(arq).convert("RGB")
                im.thumbnail((W, H))
                folha.paste(im, (x + j * W, y + 18))
            d.text((x + 2, y + 2), f"{n + k + 1}. {mod[:22]}" + ("  REPROVADO" if falhas else ""),
                   fill=(200, 0, 0) if falhas else (0, 0, 0))
        arq = pasta / f"g{n // por + 1:02d}.jpg"
        folha.save(arq, quality=84)
        out.append(arq)
    return out


if __name__ == "__main__":
    consulta = sys.argv[1]
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("/tmp/kenhub-render")
    f, rel = renderizar(consulta, out, _anki("findNotes", query=consulta))
    print(json.dumps({"cards": rel["cards"], "falhas": len(f), "folhas": len(rel["folhas"]), "saida": str(out)}, ensure_ascii=False))
    for x in f[:30]:
        print(" -", x)
    raise SystemExit(1 if f else 0)
