"""Coleta uma unidade de estudo do Kenhub: estruturas do quiz + uma imagem por estrutura.

Usa o navegador logado de `navegador.py` (aberto antes). Ritmo humano: pausas entre
chamadas e downloads; só baixa o que falta (repetível). Saída fora do repo, só uso pessoal:
~/NEBLI-privado/kenhub/<modulo>/<unidade>/{itens.json, img/<slug>.jpg}

Uso: ~/NEBLI-privado/kenhub/venv/bin/python -m nebli.kenhub.coleta <slug-da-unidade> <modulo> <unidade>
"""
import base64
import json
import random
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

from nebli.kenhub.navegador import RAIZ, conectar

LOTE = 8


def _get(page, url):
    return json.loads(page.evaluate(
        "(u)=>fetch(u,{headers:{Accept:'application/json'}}).then(r=>r.text())", url))


def _baixar(page, url, destino):
    b64 = page.evaluate(
        """async (u)=>{const r=await fetch(u);if(!r.ok)return null;const b=new Uint8Array(await r.arrayBuffer());
        let s='';for(let i=0;i<b.length;i+=8192)s+=String.fromCharCode(...b.subarray(i,i+8192));return btoa(s)}""", url)
    if not b64:
        return False
    destino.write_bytes(base64.b64decode(b64))
    return True


def _pausa(a=1.0, b=2.5):
    time.sleep(random.uniform(a, b))


def main(unidade: str, modulo: str, nome: str) -> None:
    saida = RAIZ / modulo / nome
    (saida / "img").mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        ctx = conectar(p)
        page = ctx.new_page()
        page.goto(f"https://www.kenhub.com/en/study/{unidade}", wait_until="domcontentloaded")
        page.wait_for_timeout(3000)
        quiz_id = page.evaluate("document.querySelector('[data-embedded_study_session-quiz-id-value]')"
                                "?.getAttribute('data-embedded_study_session-quiz-id-value')")
        quiz = _get(page, f"/api/quizzes/{quiz_id}?locale=en&quizJustFinished=false&version=2")
        estruturas = quiz["learnables"]
        itens = []
        for i in range(0, len(estruturas), LOTE):
            slugs = [e["slug"] for e in estruturas[i:i + LOTE]]
            enc = base64.b64encode(json.dumps(slugs).encode()).decode()
            en = {g["slug"]: g for g in _get(page, f"/api/images/gallery?encodedSlugs={enc}&locale=en&version=2")}
            _pausa()
            pt = {g["slug"]: g for g in _get(page, f"/api/images/gallery?encodedSlugs={enc}&locale=pt&version=2")}
            for e in estruturas[i:i + LOTE]:
                g_en, g_pt = en.get(e["slug"]), pt.get(e["slug"])
                if not g_en:
                    itens.append({"slug": e["slug"], "nome_en": e["name"], "sem_figura": True})
                    continue
                itens.append({
                    "slug": e["slug"], "id": e["id"], "nome_en": g_en["name"],
                    "nome_pt": (g_pt or {}).get("name"), "latim": g_en.get("altName"),
                    "sinonimos_pt": (g_pt or {}).get("synonyms", []),
                    "vista": g_en.get("perspective"), "tipo_imagem": g_en.get("imageType"),
                    "tipo": g_en.get("contentType"), "imagem_url": g_en["fullscreenUrl"],
                    "arquivo": f"img/{e['slug']}.jpg",
                })
            _pausa()
        for it in itens:
            if it.get("sem_figura"):
                continue
            destino = saida / it["arquivo"]
            if destino.exists() and destino.stat().st_size > 0:
                continue
            if not _baixar(page, it["imagem_url"], destino):
                it["sem_figura"] = True
            _pausa()
        (saida / "itens.json").write_text(json.dumps(
            {"unidade": unidade, "quiz_id": quiz_id, "titulo_quiz": quiz["title"],
             "questoes": quiz["questionCount"], "itens": itens}, ensure_ascii=False, indent=1))
        page.close()
    ok = sum(1 for i in itens if not i.get("sem_figura"))
    print(f"{len(itens)} estruturas, {ok} com figura, {len(itens) - ok} sem figura -> {saida}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
