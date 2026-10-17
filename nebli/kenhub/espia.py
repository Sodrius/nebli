"""Reconhecimento de um módulo do Kenhub: grava as chamadas de rede (HAR) e capturas de tela.

Usa a sessão de Davi (perfil local). Uma página por vez, com pausa; nada é baixado em massa.
Saída: ~/NEBLI-privado/kenhub/recon/<nome>/ (HAR + PNGs). Fora do repo, só uso pessoal.

Uso: ~/NEBLI-privado/kenhub/venv/bin/python -m nebli.kenhub.espia <url> <nome>
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path.home() / "NEBLI-privado" / "kenhub"


def main(url: str, nome: str) -> None:
    saida = RAIZ / "recon" / nome
    saida.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            str(RAIZ / "perfil"), headless=False,
            record_har_path=str(saida / "rede.har"), record_har_content="embed",
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        page.screenshot(path=str(saida / "01-pagina.png"))
        print("Navegue pelo módulo (quiz, revisão, atlas). Feche a janela para salvar o HAR.")
        while ctx.pages:
            ctx.pages[0].wait_for_event("close", timeout=0)
        ctx.close()
    print("Gravado em", saida)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
