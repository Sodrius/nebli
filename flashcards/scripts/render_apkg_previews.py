#!/usr/bin/env python3
"""render_apkg_previews.py — renderiza os cards do APKG num navegador real.

`docs/canon/APKG.md` exige renderizar os autorais e todos os Image Occlusion do
pacote entregue. Relatório JSON não basta: o que quebra num deck de anatomia é
justamente o que só aparece na tela — máscara fora do rótulo, imagem ausente,
JS do note type de IO que não desenha oclusão nenhuma.

O script extrai o pacote, monta o HTML de pergunta e de resposta de cada card
aplicando o template do note type (incluindo o filtro `cloze:`), serve tudo de
uma pasta local e fotografa as duas faces com Chromium.

Uso:
  python flashcards/scripts/render_apkg_previews.py aula.apkg --out-dir previews
  python flashcards/scripts/render_apkg_previews.py aula.apkg --out-dir previews \
      --only io-09-canal-anal --only c24
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sqlite3
import tempfile
import zipfile
from pathlib import Path

from apkg_utils import collection_bytes

CLOZE_RE = re.compile(r"\{\{c(\d+)::(.*?)(?:::(.*?))?\}\}", re.S)
COND_RE = re.compile(r"\{\{#([^}]+)\}\}(.*?)\{\{/\1\}\}", re.S)
NEG_RE = re.compile(r"\{\{\^([^}]+)\}\}(.*?)\{\{/\1\}\}", re.S)

PAGINA = """<!doctype html><html><head><meta charset="utf-8">
<style>
body {{ margin:0; padding:18px; background:#fff; font-family: system-ui, sans-serif; }}
#qa {{ max-width: 1100px; margin: 0 auto; }}
img {{ max-width: 100%; height: auto; }}
{css}
</style></head><body><div id="qa">{corpo}</div></body></html>"""


def render_cloze(texto: str, ordinal: int, resposta: bool) -> str:
    """Filtro `cloze:` do Anki: esconde o ordinal pedido, revela os demais."""
    def troca(match: re.Match) -> str:
        numero, conteudo, dica = int(match.group(1)), match.group(2), match.group(3)
        if numero != ordinal:
            return conteudo
        if resposta:
            return f'<span class="cloze">{conteudo}</span>'
        return f'<span class="cloze">[{dica or "..."}]</span>'
    return CLOZE_RE.sub(troca, texto)


def preencher(template: str, campos: dict[str, str], ordinal: int, resposta: bool) -> str:
    """Substituição de campos suficiente para pré-visualizar um card."""
    def secao(match: re.Match, negada: bool) -> str:
        nome = match.group(1).strip()
        cheio = bool((campos.get(nome) or "").strip())
        return match.group(2) if (cheio != negada) else ""

    html = COND_RE.sub(lambda m: secao(m, False), template)
    html = NEG_RE.sub(lambda m: secao(m, True), html)
    html = html.replace("{{FrontSide}}", "<!-- FrontSide -->")

    def campo(match: re.Match) -> str:
        nome = match.group(1).strip()
        if nome.startswith("cloze:"):
            return render_cloze(campos.get(nome[6:].strip(), ""), ordinal, resposta)
        if nome.startswith("text:"):
            return re.sub(r"<[^>]+>", "", campos.get(nome[5:].strip(), ""))
        if nome in ("Tags", "Type", "Deck", "Subdeck", "Card"):
            return ""
        return campos.get(nome, "")

    return re.sub(r"\{\{([^#^/][^}]*)\}\}", campo, html)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("apkg")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--width", type=int, default=1120)
    ap.add_argument("--chromium", default="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
                    help="binário do Chromium já presente no ambiente")
    args = ap.parse_args()

    saida = Path(args.out_dir)
    saida.mkdir(parents=True, exist_ok=True)
    trabalho = Path(tempfile.mkdtemp(prefix="nebli-render-"))

    with zipfile.ZipFile(args.apkg) as zf:
        nome, bruto = collection_bytes(zf)
        (trabalho / "collection.db").write_bytes(bruto)
        mapa = json.loads(zf.read("media").decode("utf-8"))
        for indice, arquivo in mapa.items():
            (trabalho / arquivo).write_bytes(zf.read(indice))

    con = sqlite3.connect(trabalho / "collection.db")
    modelos = json.loads(con.execute("select models from col").fetchone()[0])

    linhas = con.execute(
        "select c.ord, n.flds, n.mid, n.tags from cards c join notes n on n.id = c.nid order by c.id"
    ).fetchall()

    from playwright.sync_api import sync_playwright

    resultados = []
    with sync_playwright() as pw:
        binario = args.chromium if Path(args.chromium).exists() else None
        navegador = pw.chromium.launch(executable_path=binario, args=["--no-sandbox"])
        pagina = navegador.new_page(viewport={"width": args.width, "height": 900})

        for ordinal, flds, mid, tags in linhas:
            modelo = modelos[str(mid)]
            nomes = [campo["name"] for campo in modelo["flds"]]
            campos = dict(zip(nomes, flds.split("\x1f")))
            identificador = next(
                (tag.split("::")[-1] for tag in tags.split() if tag.startswith("NEBLI::")), ""
            )
            rotulo = re.sub(r"[^\w.-]+", "-", (campos.get("Header") or campos.get("Text") or "card"))[:60]
            chave = f"{len(resultados):02d}-{rotulo}"
            if args.only and not any(alvo in flds or alvo in rotulo for alvo in args.only):
                continue

            template = modelo["tmpls"][0 if modelo["type"] == 1 else ordinal]
            frente_html = preencher(template["qfmt"], campos, ordinal + 1, False)
            verso_html = preencher(template["afmt"], campos, ordinal + 1, True)

            faces = {}
            for face, corpo in (("pergunta", frente_html), ("resposta", verso_html)):
                arquivo = trabalho / f"{chave}-{face}.html"
                arquivo.write_text(PAGINA.format(css=modelo["css"], corpo=corpo), encoding="utf-8")
                pagina.goto(arquivo.as_uri())
                pagina.wait_for_timeout(450)
                destino = saida / f"{chave}-{face}.png"
                pagina.screenshot(path=str(destino), full_page=True)
                faces[face] = destino.name

            imagens = re.findall(r'src="([^"]+)"', flds)
            resultados.append({
                "key": chave,
                "note_type": modelo["name"],
                "images_referenced": imagens,
                "images_present": [nome for nome in imagens if (trabalho / nome).exists()],
                "previews": faces,
            })

        navegador.close()

    quebradas = [item for item in resultados
                 if len(item["images_present"]) != len(item["images_referenced"])]
    relatorio = {
        "apkg": args.apkg,
        "rendered_cards": len(resultados),
        "broken_media_cards": quebradas,
        "cards": resultados,
    }
    (saida / "render-report.json").write_text(
        json.dumps(relatorio, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    shutil.rmtree(trabalho, ignore_errors=True)
    print(json.dumps({"rendered": len(resultados), "broken_media": len(quebradas)}))
    return 1 if quebradas else 0


if __name__ == "__main__":
    raise SystemExit(main())
