#!/usr/bin/env python3
"""AnkiConnect emulado — a porta 8765 sem o Anki aberto.

Sobe um servidor que fala o protocolo do AnkiConnect em 127.0.0.1:8765, mas por
baixo opera a coleção pela lib oficial, sincronizada com o AnkiWeb
(`anki_collection_backend.py`). Para qualquer script do NEBLI é indistinguível do
AnkiConnect real — inclusive para os ~31 que abrem `urllib` na mão em vez de usar
o helper `nebli_anki`.

    python flashcards/scripts/ankiconnect_local.py            # sobe e segura
    python flashcards/scripts/ankiconnect_local.py --porta 8765

Ganho lateral que importa no tablet: a coleção é aberta e sincronizada **uma vez**
enquanto o servidor vive, em vez de uma vez por script.

Encerrar com Ctrl-C (ou SIGTERM) sincroniza as mudanças de volta ao AnkiWeb.
"""
import argparse
import json
import os
import signal
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import anki_collection_backend as backend  # noqa: E402

_LOCK = threading.Lock()  # a coleção não é thread-safe; serializa as ações


class Handler(BaseHTTPRequestHandler):
    def _responde(self, payload, status=200):
        corpo = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def do_GET(self):
        # o AnkiConnect real responde a versão em texto puro no GET
        corpo = b"AnkiConnect v.6"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def do_POST(self):
        try:
            n = int(self.headers.get("Content-Length") or 0)
            req = json.loads(self.rfile.read(n) or b"{}")
        except Exception as e:
            return self._responde({"result": None, "error": f"payload inválido: {e}"})

        acao = req.get("action") or ""
        params = req.get("params") or {}
        try:
            with _LOCK:
                resultado = backend.call(acao, **params)
            self._responde({"result": resultado, "error": None})
        except Exception as e:
            # mesmo formato de erro do AnkiConnect: HTTP 200 + campo error
            self._responde({"result": None, "error": str(e)})

    def log_message(self, fmt, *args):
        if os.environ.get("NEBLI_ANKI_VERBOSE") == "1":
            sys.stderr.write("[anki] " + fmt % args + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--porta", type=int, default=8765)
    p.add_argument("--host", default="127.0.0.1")
    a = p.parse_args()

    # aquece: abre e sincroniza a coleção antes de aceitar a primeira chamada
    print("[anki] abrindo a coleção…", file=sys.stderr)
    n = len(backend.call("deckNames"))
    print(f"[anki] coleção pronta — {n} decks. Servindo AnkiConnect em "
          f"http://{a.host}:{a.porta}", file=sys.stderr)

    srv = ThreadingHTTPServer((a.host, a.porta), Handler)

    def encerra(*_):
        print("\n[anki] encerrando — sincronizando de volta…", file=sys.stderr)
        srv.shutdown()

    signal.signal(signal.SIGTERM, encerra)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        encerra()


if __name__ == "__main__":
    main()
