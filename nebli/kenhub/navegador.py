"""Navegador único do Kenhub: Chromium visível no perfil logado, com porta de depuração local.

O Kenhub aceita um aparelho por vez; manter um só navegador aberto evita derrubar a sessão.
Os outros scripts se conectam por `conectar()` em vez de abrir o perfil de novo.

Uso: ~/NEBLI-privado/kenhub/venv/bin/python -m nebli.kenhub.navegador   (deixa aberto)
"""
import os
import sys

from playwright.sync_api import sync_playwright

from nebli.kenhub.caminhos import PERFIL, RAIZ  # noqa: F401  (RAIZ reexportado para coleta)

PORTA = 9333


def conectar(p):
    """Contexto do navegador já aberto por este módulo."""
    if os.environ.get("NEBLI_KENHUB_PUBLIC") == "1":
        browser = p.chromium.launch(headless=True)
        return browser.new_context(viewport={"width": 1400, "height": 1000})
    browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{PORTA}")
    return browser.contexts[0]


def main(login: bool = False) -> None:
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            str(PERFIL), headless=not login, viewport={"width": 1400, "height": 1000},
            args=[f"--remote-debugging-port={PORTA}", "--remote-debugging-address=127.0.0.1"],
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto("https://www.kenhub.com/en/login" if login else "https://www.kenhub.com/en/dashboard")
        print("login visível" if login else "pronto", flush=True)
        while ctx.pages:
            ctx.pages[0].wait_for_event("close", timeout=0)


if __name__ == "__main__":
    main(sys.argv[1:] == ["--login"])
