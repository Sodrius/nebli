"""Abre o Chromium com janela visível num perfil local para Davi entrar no Kenhub.

A sessão fica em ~/NEBLI-privado/kenhub/perfil (fora do repo). Senha e cookies nunca
são lidos nem gravados por este script.

Uso: ~/NEBLI-privado/kenhub/venv/bin/python -m nebli.kenhub.login
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

PERFIL = Path.home() / "NEBLI-privado" / "kenhub" / "perfil"


def main() -> None:
    PERFIL.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(str(PERFIL), headless=False)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto("https://www.kenhub.com/")
        print("Entre na sua conta na janela aberta e depois FECHE a janela para terminar.")
        while ctx.pages:
            ctx.pages[0].wait_for_event("close", timeout=0)
        ctx.close()


if __name__ == "__main__":
    main()
