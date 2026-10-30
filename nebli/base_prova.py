"""Base da prova do modo deck-prova (F-20261029-CLAUDE-04, pipeline v11).

    /usr/bin/python3 -m nebli.base_prova <corrida>            # monta fontes/slides.pdf, fontes/slides.txt e o índice
    /usr/bin/python3 -m nebli.base_prova <corrida> --conferir # só confere se cada excerto ainda é literal

Davi: “deck-prova de farmáco independente das minhas aulas, mas cobrindo tudo da apostila e tudo dos materiais extras” e “pode
usar lâmina de vez em quando”. No modo prova as lâminas não organizam o deck: a base da prova faz o papel delas. Cada página da base
é um excerto literal de uma fonte (apostila, objetivos, questões, texto do professor), puxado do PDF por âncoras — nunca digitado —,
na ordem dos blocos de assunto; lâmina entra como página inteira só com motivo. Assim os gates que já existem para lâminas
(compreensão por bloco, ordem do deck, fidelidade, exemplo × princípio) valem para a base sem contorno.

base-prova.json (na corrida):
  {"fontes_base": ["fontes/apostila.pdf", ...],
   "blocos": [{"titulo": "1 Fundamentos",
               "excertos": [{"fonte": "fontes/objetivos.pdf", "paginas": [1, 1], "de": "1) O que é farmacologia", "ate": "e excreção."},
                            {"lamina": "fontes/laminas/intro.pdf", "pagina": 12, "motivo": "curva dose-resposta: figura real"}]}]}
O título de cada página (linha '# …') é o título do bloco mais o rótulo da fonte; é nele que o gate procura o rótulo de exemplo
(“caso clínico”), porque um “por exemplo” no meio do texto da apostila não é o professor chamando o bloco de exemplo.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import fitz

LARG, ALT, MARG = 595, 842, 40


def norm(t: str) -> str:
    t = t.replace("­", "").replace("‑\n", "").replace("‑", "-")
    t = re.sub(r"-\n(?=[a-zà-ú])", "", t)  # hifenização de fim de linha
    return re.sub(r"\s+", " ", t).strip()


def texto_paginas(pdf: Path, a: int, z: int) -> str:
    with fitz.open(pdf) as d:
        return norm(" ".join(d[i].get_text() for i in range(a - 1, z)))


def excerto(run: Path, x: dict) -> str:
    """Trecho literal entre as âncoras 'de' e 'ate' (inclusive). Erro se a âncora não estiver na fonte."""
    a, z = (list(x["paginas"]) + list(x["paginas"]))[:2]
    txt = texto_paginas(run / x["fonte"], int(a), int(z))
    de, ate = norm(x["de"]), norm(x["ate"])
    i = txt.find(de)
    if i < 0:
        raise ValueError(f"âncora 'de' não encontrada em {x['fonte']} p{a}-{z}: {de[:60]!r}")
    j = txt.find(ate, i + len(de) - len(ate) if len(ate) <= len(de) else i)
    if j < 0:
        raise ValueError(f"âncora 'ate' não encontrada em {x['fonte']} p{a}-{z}: {ate[:60]!r}")
    return txt[i:j + len(ate)]


def _rotulo(x: dict) -> str:
    if x.get("lamina"):
        return f"Lâmina {Path(x['lamina']).stem}, p. {x['pagina']}"
    a, z = (list(x["paginas"]) + list(x["paginas"]))[:2]
    return f"{x.get('rotulo') or Path(x['fonte']).stem}, p. {a}" + (f"–{z}" if z != a else "")


def _pagina_texto(doc, titulo: str, corpo: str):
    """Uma ou mais páginas A4 com o título e o excerto; reduz a fonte até 6 pt e continua em outra página se precisar."""
    caixa = fitz.Rect(MARG, MARG + 44, LARG - MARG, ALT - MARG)
    restante, n = corpo, 0
    while restante:
        t = titulo + (" (cont.)" if n else "")
        p = doc.new_page(width=LARG, height=ALT)
        p.insert_textbox(fitz.Rect(MARG, MARG, LARG - MARG, MARG + 40), t, fontsize=11, fontname="helv")
        parte = restante
        while True:  # insert_textbox não escreve nada quando não cabe: tenta 9 → 7 pt e, se não couber, metade do texto
            if any(p.insert_textbox(caixa, parte, fontsize=fs, fontname="helv") >= 0 for fs in (9, 8, 7)):
                break
            parte = parte[:parte.rfind(" ", 0, len(parte) // 2)]
        restante = restante[len(parte):].lstrip()
        n += 1
        yield t, parte


def montar(run: Path) -> list[dict]:
    run = Path(run)
    base = json.loads((run / "base-prova.json").read_text(encoding="utf-8"))
    doc = fitz.open()
    indice, txt = [], []
    for bi, b in enumerate(base["blocos"], 1):
        for x in b["excertos"]:
            titulo = f"# {b['titulo']} - {_rotulo(x)}"  # hífen: a fonte base do PDF (helv) não tem travessão
            if x.get("lamina"):
                if len(str(x.get("motivo", "")).strip()) < 20:
                    raise ValueError(f"lâmina sem motivo (≥ 20 caracteres): {x}")
                with fitz.open(run / x["lamina"]) as src:
                    p = doc.new_page(width=LARG, height=ALT)
                    p.insert_textbox(fitz.Rect(MARG, MARG, LARG - MARG, MARG + 40), titulo, fontsize=11, fontname="helv")
                    pix = src[int(x["pagina"]) - 1].get_pixmap(dpi=110)  # o pixmap já sai na rotação de leitura da lâmina
                    p.insert_image(fitz.Rect(MARG, MARG + 44, LARG - MARG, ALT - MARG), pixmap=pix, keep_proportion=True)
                    corpo = norm(src[int(x["pagina"]) - 1].get_text())
                paginas = [(titulo, corpo)]
            else:
                corpo = excerto(run, x)
                paginas = list(_pagina_texto(doc, titulo, corpo))
            for t, parte in paginas:
                indice.append({"pagina": len(indice) + 1, "bloco": bi, "titulo_bloco": b["titulo"], "titulo": t,
                               **{k: x[k] for k in ("fonte", "paginas", "de", "ate", "lamina", "motivo", "rotulo") if k in x},
                               **({"pagina_lamina": x["pagina"]} if x.get("lamina") else {}),
                               "sha256": hashlib.sha256(corpo.encode()).hexdigest()})
                txt.append(f"===== página {len(indice)} =====\n{t}\n{parte}\n")
    (run / "fontes").mkdir(exist_ok=True)
    doc.save(run / "fontes" / "slides.pdf")
    (run / "fontes" / "slides.txt").write_text("\n".join(txt), encoding="utf-8")
    (run / "fontes" / "base-prova-indice.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1), encoding="utf-8")
    return indice


def conferir(run: Path) -> list[str]:
    """Problemas da base: excerto que deixou de ser literal, fonte base sem excerto, lâmina sem motivo."""
    run = Path(run)
    try:
        base = json.loads((run / "base-prova.json").read_text(encoding="utf-8"))
        indice = json.loads((run / "fontes" / "base-prova-indice.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ["base-prova.json ou fontes/base-prova-indice.json ausente: rodar nebli.base_prova"]
    probs = []
    usadas = set()
    for b in base.get("blocos", []):
        for x in b.get("excertos", []):
            if x.get("lamina"):
                if len(str(x.get("motivo", "")).strip()) < 20:
                    probs.append(f"lâmina {x.get('lamina')} p{x.get('pagina')} sem motivo")
                continue
            usadas.add(x["fonte"])
            try:
                sha = hashlib.sha256(excerto(run, x).encode()).hexdigest()
            except (ValueError, OSError, RuntimeError) as e:
                probs.append(str(e)); continue
            if not any(i.get("sha256") == sha and i.get("fonte") == x["fonte"] for i in indice):
                probs.append(f"excerto de {x['fonte']} ('{x['de'][:30]}…') mudou desde a montagem: rodar nebli.base_prova")
    falta = [f for f in base.get("fontes_base", []) if f not in usadas]
    if not base.get("fontes_base"):
        probs.append("base-prova.json sem 'fontes_base'")
    if falta:
        probs.append(f"fonte base sem nenhum excerto na base: {falta}")
    return probs


if __name__ == "__main__":
    r = Path(sys.argv[1])
    if "--conferir" in sys.argv:
        ps = conferir(r)
        print("\n".join(ps) or "base da prova íntegra")
        sys.exit(1 if ps else 0)
    ind = montar(r)
    print(f"{len(ind)} páginas na base; {len({i['bloco'] for i in ind})} blocos")
