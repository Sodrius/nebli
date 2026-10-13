"""Oclusão de imagem feita do próprio slide da aula (pedido de Davi em 02/10/2026, F-20261002-CLAUDE-09).

Em aula de anatomia, o que o slide e o roteiro prático mostram entra no deck com a figura da professora: cada rótulo de
texto da lâmina vira uma máscara; o card esconde todos os rótulos e destaca um (esconde tudo, adivinha um), como no BlueLink.
O nome em inglês vai em negrito no início de Remarks (só no verso), que é de onde o Tab lê o alvo.

Uso num spec/build de corrida:

    from nebli import slide_io
    made = slide_io.build(run_dir, "fontes/slides.pdf", prefix="nebli-uc08-an01", items=[
        dict(key="io-esofago-cervical", page=5, half="top", lines=["Porção cervical"], name="Cervical part of the esophagus"),
        dict(key="io-ducto", page=16, half="bottom", rects=[(205, 594, 245, 612)], name="Main pancreatic duct"),
    ])
    # made[key] = {"fields": {...campos do modelo Image Occlusion Enhanced+...}, "media": {nome_no_anki: caminho_relativo}}

`lines` são as linhas de texto do rótulo como estão no PDF (comparação sem acento solto, caixa nem espaços repetidos);
`search` são expressões localizadas dentro de uma linha maior; `title_size` muda o corte entre rótulo e título (slides de uma
lâmina por página usam fonte grande: passar 99 e mascarar títulos junto); `rects` (x0, y0, x1, y1 em pontos da página) serve para rótulo que só existe dentro da figura; `mask_rects` esconde
título ou rótulo desenhado na figura que entregaria a resposta. Linha não encontrada é erro.
Sempre renderizar e olhar as lâminas geradas (`<corrida>/io/*-preview.png`) antes de instalar.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

# PDF de 2 lâminas por página (impressão "folheto" do PowerPoint, A4 retrato 540 × 702 pt).
HALVES = {"top": (40, 50, 500, 345), "bottom": (40, 355, 500, 650), "full": None}
CREDIT = re.compile(r"^(netter|sobotta|moore|foto|prometheus|atlas|v[ií]deo|https?:|\d+$|furness|mittal|current op|j surg)", re.I)
TITLE_SIZE = 12.5  # rótulos ficam abaixo disto; títulos acima
PAD = 2.0
ZOOM = 2.4
VERSAO = "r2"  # máscaras por rótulo inteiro (03/10); nome novo evita o Anki reaproveitar a máscara antiga


def norm(text):
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"\s+", "", text).lower()  # sem espaços: o PDF às vezes parte palavras ("esôfa go") ou solta pontuação


def label_lines(page, clip, title_size=TITLE_SIZE):
    """[(texto, rect)] das linhas de rótulo dentro da lâmina: fonte pequena, sem créditos nem numeração."""
    return [(text, rect) for text, rect, _ in labels(page, clip, title_size, split=False)]


GAP_X = 14.0  # pontos: partes mais afastadas que isto na mesma linha são rótulos diferentes
LIST_ITEM = re.compile(r"^\s*(\d+\s*[.)\-–]|[•\-–]\s)")


def labels(page, clip, title_size=TITLE_SIZE, split=True):
    """Rótulos inteiros: [(texto, rect da união, [rects das partes])].

    Corrige F-20261003-CLAUDE-13 (máscara por linha deixava parte do nome sob outra máscara e o verso mostrava um pedaço;
    caixas lado a lado no mesmo bloco do PDF viravam uma máscara gigante sobre a figura). Partes de texto se juntam num
    rótulo quando estão no mesmo bloco e se tocam: na mesma linha com até GAP_X de distância, ou na linha de baixo com a
    borda esquerda alinhada ou sobreposição horizontal. Item de lista numerada abre outro rótulo."""
    import fitz
    parts = []  # (bloco, texto, rect); partes separadas por espaço largo, mesmo dentro de um trecho ("camada mucosa      camada submucosa")
    for bi, block in enumerate(page.get_text("rawdict", clip=clip)["blocks"]):
        for line in block.get("lines", []):
            run, text, last = [], "", None
            def close():
                if run and text.strip():
                    parts.append((bi, re.sub(r"\s+", " ", text).strip(), _union(run)))
            for span in line["spans"]:
                if span["size"] >= title_size:
                    continue
                for ch in span["chars"]:
                    c = ch["c"]
                    if c.isspace():
                        text += " "; continue
                    r = fitz.Rect(ch["bbox"])
                    gap = r.x0 - last.x1 if last is not None else 0
                    prev = text.split()[-1] if text.split() else ""
                    abbrev = prev.endswith(".") and len(prev) <= 4  # "a. Mesentérica", "v. porta", "m. Puborretal"
                    if last is not None and (gap > GAP_X or (gap > 9 and not abbrev)):
                        close(); run, text = [], ""
                    run.append(r); text += c; last = r
            close()
    parts = [p for p in parts if not CREDIT.match(p[1])]
    if not split:
        return [(t, r, [r]) for _, t, r in parts]
    parent = list(range(len(parts)))
    find = lambda i: i if parent[i] == i else find(parent[i])
    for i, (bi, ti, ri) in enumerate(parts):
        for j, (bj, tj, rj) in enumerate(parts):
            if j <= i:
                continue
            if bi != bj:  # outro bloco do PDF: só junta continuação colada logo abaixo ("... mesentérica" / "inferior)")
                upper, lower, lower_text = (ri, rj, tj) if ri.y0 <= rj.y0 else (rj, ri, ti)
                if 0 <= lower.y0 - upper.y1 <= 0.3 * upper.height and abs(lower.x0 - upper.x0) <= 4 and re.match(r"[a-zà-ú)(]", lower_text):
                    parent[find(j)] = find(i)
                continue
            same_row = abs(ri.y0 - rj.y0) < 2 and max(ri.x0, rj.x0) - min(ri.x1, rj.x1) <= GAP_X
            upper, lower, lower_text = (ri, rj, tj) if ri.y0 <= rj.y0 else (rj, ri, ti)
            stacked = (-2 <= lower.y0 - upper.y1 <= 0.7 * upper.height and not LIST_ITEM.match(lower_text)
                       and (abs(lower.x0 - upper.x0) <= 12 or abs((lower.x0 + lower.x1) - (upper.x0 + upper.x1)) / 2 <= 12
                            or abs(lower.x1 - upper.x1) <= 12))  # alinhado à esquerda, ao centro ou à direita
            if same_row or stacked:
                parent[find(j)] = find(i)
    groups = {}
    for i, p in enumerate(parts):
        groups.setdefault(find(i), []).append(p)
    out = []
    for g in groups.values():
        g.sort(key=lambda p: (round(p[2].y0), p[2].x0))
        out.append((" ".join(t for _, t, _ in g), _union([r for _, _, r in g]), [r for _, _, r in g]))
    return out


def _union(rects):
    import fitz
    u = fitz.Rect(rects[0])
    for r in rects[1:]:
        u |= r
    return u


def merge(rects, gap=3.0, pad_y=1.0):
    """Une retângulos que se tocam ou se sobrepõem (palavras vizinhas viram uma máscara só)."""
    import fitz
    rects = [fitz.Rect(r) for r in rects]
    changed = True
    while changed:
        changed = False
        for i in range(len(rects)):
            for j in range(i + 1, len(rects)):
                a, b = rects[i], rects[j]
                if fitz.Rect(a.x0 - gap, a.y0 - pad_y, a.x1 + gap, a.y1 + pad_y).intersects(b):
                    rects[i] = a | b; del rects[j]; changed = True; break
            if changed:
                break
    return rects


def svg(width, height, shapes):
    body = "\n".join(f'  <rect id="{sid}" x="{r[0]:.1f}" y="{r[1]:.1f}" width="{r[2] - r[0]:.1f}" height="{r[3] - r[1]:.1f}" '
                     f'stroke="#2D2D2D" fill="{fill}"{cls}/>' for sid, r, fill, cls in shapes)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">\n <g>\n  <title>Labels</title>\n </g>\n'
            f' <g>\n  <title>Masks</title>\n{body}\n </g>\n</svg>\n')


def build(run, pdf, prefix, items, out="io"):
    import fitz
    run = Path(run); folder = run / out; folder.mkdir(exist_ok=True)
    docs = {}
    made, pages = {}, {}
    for item in items:
        source = item.get("pdf", pdf)  # item pode vir de outro PDF da corrida (ex.: pranchas do Netter)
        doc = docs.setdefault(source, fitz.open(run / source))
        page = doc[item["page"] - 1]
        box = item.get("clip") or HALVES[item.get("half", "full")]  # clip explícito: prancha de atlas sem cabeçalho/rodapé
        clip = fitz.Rect(box) if box else page.rect
        tag = item.get("tag") or f"p{item['page']:02d}{item.get('half', 'full')[0]}"
        image = f"{prefix}-{tag}.png"
        if tag not in pages:
            pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip)
            pix.save(folder / image)
            # prancha de atlas (outro PDF): colunas de rótulos distintos empilhados; cada linha é um rótulo
            atlas = bool(item.get("pdf")) or item.get("por_linha", False)
            pages[tag] = (pix.width, pix.height, labels(page, clip, item.get("title_size", TITLE_SIZE), split=not atlas))
        width, height, groups = pages[tag]
        wanted = [norm(x) for x in item.get("lines", [])]
        target_groups, missing = [], []
        for w in wanted:  # rótulo exato; senão, o único rótulo que contém a linha pedida
            exact = [g for g in groups if norm(g[0]) == w]
            inside = [g for g in groups if w in norm(g[0])]
            if exact or len(inside) == 1:
                target_groups += [g for g in exact or inside if g not in target_groups]
            elif len(inside) > 1 and [g for g in inside if any(x != w and x in norm(g[0]) for x in wanted)]:
                # linha ambígua: vale o(s) rótulo(s) onde também está outra linha pedida no mesmo item
                for g in inside:
                    if any(x != w and x in norm(g[0]) for x in wanted) and g not in target_groups: target_groups.append(g)
            elif len(inside) > 1 and [g for g in inside if all(x in norm(g[0]) for x in wanted)]:
                # linhas do mesmo rótulo pedidas juntas: o menor rótulo que contém todas (texto explicativo longo fica de fora)
                g = min((g for g in inside if all(x in norm(g[0]) for x in wanted)), key=lambda g: len(g[0]))
                if g not in target_groups: target_groups.append(g)
            elif len(inside) > 1:
                raise SystemExit(f"{item['key']}: '{w}' aparece em mais de um rótulo da página {item['page']}: {[g[0] for g in inside]}")
            else:
                missing.append(w)
        if missing:
            raise SystemExit(f"{item['key']}: rótulo não encontrado na página {item['page']} ({item.get('half')}): {missing}\n"
                             f"  disponíveis: {[g[0] for g in groups]}")
        target = [g[1] for g in target_groups]
        partial = []
        for phrase in item.get("search", []):  # rótulo que divide a caixa com outros: localizar só a expressão
            found = [r for r in page.search_for(phrase) if r.intersects(clip)]
            if not found:
                raise SystemExit(f"{item['key']}: expressão não encontrada na página {item['page']}: {phrase!r}")
            for r in found:
                owner = next((g for g in groups if g[1].intersects(r)), None)
                if owner and not item.get("parcial_ok"):
                    # a expressão só localiza; o alvo é o rótulo inteiro que a contém (nunca um pedaço do nome)
                    if owner not in target_groups: target.append(owner[1]); target_groups.append(owner)
                else:
                    target.append(r); partial.append(phrase)
        target += [fitz.Rect(r) for r in item.get("rects", [])]
        if not target:
            raise SystemExit(f"{item['key']}: sem linhas nem rects")
        target = merge(target)
        others = []
        for text, rect, line_rects in groups:
            if any(g[1] == rect for g in target_groups):
                continue
            if any(rect.intersects(t) for t in target):  # caixa com vários rótulos: esconder o resto, palavras vizinhas juntas
                words = [fitz.Rect(w[:4]) for lr in line_rects for w in page.get_text("words", clip=lr)]
                others += merge([w for w in words if not any(w.intersects(t) for t in target)])
            else:
                others.append(rect)
        others += [fitz.Rect(r) for r in item.get("mask_rects", [])]  # rótulo/título dentro da figura que entregaria a resposta
        others = merge(others, gap=0, pad_y=-1)  # só caixas de fato sobrepostas viram uma máscara
        rotulo = " / ".join(g[0] for g in target_groups) or " / ".join(item.get("search", [])) or "(rect)"
        to_px = lambda r: ((r.x0 - clip.x0 - PAD) * ZOOM, (r.y0 - clip.y0 - PAD) * ZOOM, (r.x1 - clip.x0 + PAD) * ZOOM, (r.y1 - clip.y0 + PAD) * ZOOM)
        hidden = [(f"{item['key']}-o{i}", to_px(r), "#FFEBA2", "") for i, r in enumerate(others)]
        asked = [(f"{item['key']}-t{i}", to_px(r), "#FF7E7E", ' class="qshape"') for i, r in enumerate(target)]
        names = {kind: f"{prefix}-{item['key']}-{kind}-{VERSAO}.svg" for kind in "QAO"}
        (folder / names["Q"]).write_text(svg(width, height, hidden + asked), encoding="utf-8")
        (folder / names["A"]).write_text(svg(width, height, hidden), encoding="utf-8")
        (folder / names["O"]).write_text(svg(width, height, hidden + [(s, r, "#FFEBA2", "") for s, r, _, _ in asked]), encoding="utf-8")
        remarks = f"<b>{item['name']}</b>" + (f"<br>{item['remarks']}" if item.get("remarks") else "")
        made[item["key"]] = {
            "fields": {"ID (hidden)": f"{prefix}-{item['key']}", "Header": "", "Image": f'<img src="{image}">',
                       "Question Mask": f'<img src="{names["Q"]}">', "Footer": "", "Remarks": remarks, "Sources": "", "Extra 1": "",
                       "Extra 2": "", "Answer Mask": f'<img src="{names["A"]}">', "Original Mask": f'<img src="{names["O"]}">'},
            "media": {image: f"{out}/{image}", **{n: f"{out}/{n}" for n in names.values()}},
            "rotulo": rotulo, "parcial": partial,
        }
        # prévia para inspeção: lâmina com as máscaras da pergunta desenhadas
        preview = fitz.open(); pg = preview.new_page(width=width, height=height)
        pg.insert_image(pg.rect, filename=str(folder / image))
        for _, r, fill, _ in hidden + asked:
            pg.draw_rect(fitz.Rect(r), color=(0.18, 0.18, 0.18), fill=(1, 0.49, 0.49) if fill == "#FF7E7E" else (1, 0.92, 0.64))
        pg.insert_text((6, 14), f"{item['key']}: {item['name']}", fontsize=11, color=(0.8, 0, 0))
        pg.get_pixmap(dpi=60).save(folder / f"{item['key']}-preview.png")
    return made
