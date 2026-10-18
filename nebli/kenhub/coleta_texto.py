"""Texto de estudo de uma unidade do Kenhub (objetivos, parágrafos e tabela-resumo), para o gate de cobertura do quiz.

F-20261018-CLAUDE-01 (comentário de Davi no card do plexo braquial): “todos têm que cobrir o quiz todo da unidade”.
O quiz tem questões de identificação/grafia (as estruturas) e questões de texto (os fatos da unidade): as duas partes
precisam de card. Cada trecho vira uma chave (`obj:n`, `txt:n`, `resumo:<rótulo>`) que algum card tem de cobrir.

Uso: venv/bin/python -m nebli.kenhub.coleta_texto [<módulo>/<submódulo> ...]   (sem argumentos: todas as unidades coletadas)
"""
import html as _html
import json
import random
import re
import sys
import time

from playwright.sync_api import sync_playwright

from nebli.kenhub.navegador import RAIZ, conectar

IGNORA = ("Review the structures", "Learn more about", "Solidify your", "Keep studying", "Great session",
          "This study session", "Take a quiz", "Watch video", "The following video", "You have watched",
          "Download the following", "While studying the overview")


def analisar(texto: str) -> list[dict]:
    """Texto visível da página → trechos {chave, tipo, en}."""
    a = texto.find("Learning objectives")
    b = texto.find("Continue your learning", a)
    linhas = [l.rstrip() for l in texto[a:b if b > 0 else None].splitlines()]
    out, modo, ultimo = [], "intro", None
    for l in linhas:
        s = l.strip()
        if not s:
            continue
        if s.startswith("After completing this study unit"):
            modo = "obj"
            continue
        if s.startswith("Watch video") and modo == "obj":
            modo = "txt"
            continue
        if s.startswith("Key points about") or s == "Summary":
            modo = "resumo"
            continue
        if s == "Table quiz":
            continue
        if modo == "obj":
            out.append({"chave": f"obj:{sum(1 for o in out if o['tipo'] == 'obj') + 1}", "tipo": "obj", "en": s})
        elif modo == "txt":
            if len(s) >= 80 and not s.startswith(IGNORA):
                out.append({"chave": f"txt:{sum(1 for o in out if o['tipo'] == 'txt') + 1}", "tipo": "txt", "en": s})
        elif modo == "resumo":
            if "\t" in l:
                rot, _, val = l.strip().partition("\t")
                chave = f"resumo:{rot.strip()}"
                repetidas = sum(1 for o in out if o["chave"].split("#")[0] == chave)
                ultimo = {"chave": chave + (f"#{repetidas + 1}" if repetidas else ""), "tipo": "resumo", "en": val.strip()}
                out.append(ultimo)
            elif ultimo and not s.startswith(IGNORA):
                ultimo["en"] += "\n" + s
    return out


def legendas(pagina_html: str) -> list[dict]:
    """Os slides do carrossel (“Browse atlas”) vêm todos em data-captions, mesmo os que não aparecem na tela."""
    out = []
    for m in re.finditer(r'data-captions="([^"]+)"', pagina_html):
        for k, v in json.loads(_html.unescape(m.group(1))).items():
            desc = re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", "", v.get("description", "")))).strip()
            out.append({"chave": f"cap:{k}", "tipo": "cap", "en": f"{v.get('title', '').strip()}: {desc}" if desc else ""})
    return [o for o in out if o["en"]]


def trechos(texto: str, pagina_html: str) -> list[dict]:
    caps = legendas(pagina_html)
    corpo = [t for t in analisar(texto) if not any(t["tipo"] == "txt" and c["en"].split(": ", 1)[-1][:80] == t["en"][:80] for c in caps)]
    return corpo + caps


def main(alvos):
    pastas = [RAIZ / a for a in alvos] if alvos else sorted(p.parent for p in RAIZ.glob("*/*/itens.json"))
    with sync_playwright() as p:
        ctx = conectar(p)
        page = ctx.new_page()
        for pasta in pastas:
            arq = pasta / "itens.json"
            d = json.loads(arq.read_text())
            if d.get("texto"):
                continue
            page.goto(f"https://www.kenhub.com/en/study/{d['unidade']}", wait_until="domcontentloaded")
            page.wait_for_timeout(4000)
            d["texto"] = trechos(page.inner_text("body"), page.content())
            arq.write_text(json.dumps(d, ensure_ascii=False, indent=1))
            print(f"{pasta.name}: {len(d['texto'])} trechos ({', '.join(sorted({t['tipo'] for t in d['texto']}))})")
            time.sleep(random.uniform(2, 4))
        page.close()


if __name__ == "__main__":
    main(sys.argv[1:])
