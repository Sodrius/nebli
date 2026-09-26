"""Add-on NEBLI: total de cards no nome dos decks e limite de novos por deck.

É só um carregador. A lógica fica em <repo>/nebli/anki_addon.py e é recarregada
quando o arquivo muda, sem reiniciar o Anki. Instalar/atualizar pelo repositório:
    python -m nebli.decks instalar-addon
Erros e mudanças ficam em user_files/log.txt desta pasta.
"""
import importlib
import sys
import time
import traceback
from pathlib import Path

from aqt import gui_hooks, mw
from aqt.qt import QTimer

USER = Path(__file__).resolve().parent / "user_files"
_state = {"mtime": None, "module": None, "error": None}


def _log(message):
    USER.mkdir(exist_ok=True)
    with (USER / "log.txt").open("a", encoding="utf-8") as handle:
        handle.write(time.strftime("%Y-%m-%d %H:%M:%S ") + message + "\n")


def _module():
    repo = Path(mw.addonManager.getConfig(__name__)["repo"])
    sources = [repo / "nebli" / "rotulos.py", repo / "nebli" / "anki_addon.py"]
    mtime = tuple(path.stat().st_mtime for path in sources)
    if _state["mtime"] != mtime:
        if str(repo) not in sys.path:
            sys.path.insert(0, str(repo))
        import nebli.anki_addon
        import nebli.rotulos
        importlib.reload(nebli.rotulos)
        _state["module"] = importlib.reload(nebli.anki_addon)
        _state["mtime"] = mtime
        _log(f"lógica carregada de {repo}")
    return _state["module"]


def _tick():
    if mw.col is None or mw.progress.busy():
        return
    try:
        _module().tick(mw, USER, _log)
        _state["error"] = None
    except Exception:
        error = traceback.format_exc()
        if error != _state["error"]:
            _log(error)
            _state["error"] = error


_timer = QTimer(mw)
_timer.timeout.connect(_tick)
gui_hooks.profile_did_open.append(lambda: _timer.start(2000))
gui_hooks.profile_will_close.append(_timer.stop)
gui_hooks.sync_did_finish.append(_tick)
