"""NEBLI — atalhos de revisão pedidos por Davi em 30/09/2026.

Durante a revisão:
    a s d f     De novo / Difícil / Bom / Fácil (no lugar de 1 2 3 4; só com a resposta à vista)
    q w e r     bandeira vermelha / verde / azul / rosa (apertar de novo tira a bandeira)
    Caps Lock   suspende o card atual, exceto verde (verde nunca é suspenso)
    Shift       sozinho (apertar e soltar): edita o card
    c           comentário: abre o campo NEBLI_Comentario da nota para escrever
    v           voltar: desfaz a última ação e volta ao card anterior (Cmd/Ctrl+Z também)

Tab fica livre para o futuro add-on de explicação por IA.

Conflitos resolvidos só na tela de revisão: atalhos globais e de menu nas mesmas
teclas (a Adicionar, s Estudar, d Baralhos, f Criar filtrado...) ficam desligados
enquanto se revisa e voltam nas outras telas; e (Editar) e r (repetir áudio) viram bandeiras. F5 continua repetindo o áudio
e o botão Editar continua no rodapé; v deixa de tocar a gravação de voz.

Instalar/atualizar pelo repositório: python -m nebli.decks instalar-addon
(reiniciar o Anki depois). Carregamento e erros vão para user_files/log.txt.
"""
import html
import re
import sys
import time
import traceback
from pathlib import Path

from aqt import gui_hooks, mw
from aqt.qt import (QAction, QApplication, QDialog, QDialogButtonBox, QEvent, QKeySequence, QLabel,
                    QObject, QPlainTextEdit, QShortcut, Qt, QTextCursor, QTimer, QVBoxLayout)
from aqt.utils import tooltip

ANSWER = {"a": 1, "s": 2, "d": 3, "f": 4}
FLAGS = {"q": 1, "w": 3, "e": 4, "r": 5}  # vermelha, verde, azul, rosa
COMMENT_KEY = "c"
UNDO_KEY = "v"
TAKEN = set("1234") | set(ANSWER) | set(FLAGS) | {COMMENT_KEY, UNDO_KEY}
FIELD = "NEBLI_Comentario"
PENDING = "NEBLI_comentario::pendente"
USER = Path(__file__).resolve().parent / "user_files"


def _log(message):
    USER.mkdir(exist_ok=True)
    with (USER / "log.txt").open("a", encoding="utf-8") as handle:
        handle.write(time.strftime("%Y-%m-%d %H:%M:%S ") + message + "\n")


def _guarded(fn):
    def run(*args):
        try:
            return fn(*args)
        except Exception:
            _log(traceback.format_exc())
            tooltip("Atalho NEBLI falhou; detalhes em user_files/log.txt do add-on.")
    return run


def _reviewer():
    reviewer = getattr(mw, "reviewer", None)
    return reviewer if mw.state == "review" and reviewer and reviewer.card else None


@_guarded
def _answer(ease):
    reviewer = _reviewer()
    if reviewer and reviewer.state == "answer":
        reviewer._answerCard(ease)


@_guarded
def _flag(flag):
    reviewer = _reviewer()
    if reviewer:
        reviewer.set_flag_on_current_card(flag)


@_guarded
def _suspend():
    reviewer = _reviewer()
    if not reviewer:
        return
    if reviewer.card.user_flag() == 3:
        tooltip("Card verde não é suspenso.")
        return
    reviewer.suspend_current_card()


@_guarded
def _undo():
    if _reviewer():
        (getattr(mw, "undo", None) or mw.onUndo)()


@_guarded
def _edit():
    if _reviewer():
        mw.onEditCurrent()


def _as_text(value):
    value = re.sub(r"<br\s*/?>|</div>|</p>", "\n", value, flags=re.I)
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


@_guarded
def _comment():
    reviewer = _reviewer()
    if not reviewer:
        return
    note = reviewer.card.note()
    if FIELD not in note.keys():
        tooltip(f"Este tipo de nota ainda não tem o campo {FIELD}.")
        return
    dialog = QDialog(mw)
    dialog.setWindowTitle("Comentário")
    layout = QVBoxLayout(dialog)
    layout.addWidget(QLabel("Comentário deste card (Cmd/Ctrl+Enter salva, Esc cancela):"))
    box = QPlainTextEdit(_as_text(note[FIELD]))
    box.setMinimumSize(520, 180)
    layout.addWidget(box)
    buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Save
                               | QDialogButtonBox.StandardButton.Cancel)
    buttons.accepted.connect(dialog.accept)
    buttons.rejected.connect(dialog.reject)
    layout.addWidget(buttons)
    QShortcut(QKeySequence("Ctrl+Return"), dialog, activated=dialog.accept)
    box.moveCursor(QTextCursor.MoveOperation.End)
    box.setFocus()
    if not dialog.exec():
        return
    text = box.toPlainText().strip()
    note[FIELD] = html.escape(text, quote=False).replace("\n", "<br>")
    if text:
        note.add_tag(PENDING)
    else:
        note.remove_tag(PENDING)
    try:
        from aqt.operations.note import update_note
        update_note(parent=mw, note=note).success(
            lambda _: tooltip("Comentário salvo.")).run_in_background()
    except ImportError:
        mw.col.update_note(note)
        tooltip("Comentário salvo.")


def _on_shortcuts(state, shortcuts):
    if state != "review":
        return
    shortcuts[:] = [entry for entry in shortcuts
                    if not (isinstance(entry[0], str) and entry[0].lower() in TAKEN)]
    shortcuts.extend((key, lambda ease=ease: _answer(ease)) for key, ease in ANSWER.items())
    shortcuts.extend((key, lambda flag=flag: _flag(flag)) for key, flag in FLAGS.items())
    shortcuts.append((COMMENT_KEY, _comment))
    shortcuts.append((UNDO_KEY, _undo))


_parked = {}  # atalhos de menu/globais tirados durante a revisão -> atalho original


def _on_state(new_state, _old_state):
    """Tecla com dois donos fica ambígua para o Qt e nenhum dispara (ex.: F de "Criar
    baralho filtrado" no menu Ferramentas). Na revisão, estaciona os outros donos das
    nossas teclas; fora dela, devolve."""
    try:
        if new_state == "review":
            own = set(getattr(mw, "stateShortcuts", []) or [])
            for widget in mw.findChildren(QShortcut) + mw.findChildren(QAction):
                if widget in own or widget in _parked:
                    continue
                keys = widget.key() if isinstance(widget, QShortcut) else widget.shortcut()
                if keys.toString().lower() in TAKEN:
                    _parked[widget] = QKeySequence(keys)
                    if isinstance(widget, QShortcut):
                        widget.setKey(QKeySequence())
                    else:
                        widget.setShortcut(QKeySequence())
        else:
            parked = list(_parked.items())
            _parked.clear()
            for widget, keys in parked:
                try:
                    if isinstance(widget, QShortcut):
                        widget.setKey(keys)
                    else:
                        widget.setShortcut(keys)
                except RuntimeError:
                    pass  # atalho de uma tela anterior que o Anki já apagou
    except Exception:
        _log(traceback.format_exc())


class _SoloKeys(QObject):
    """Teclas sozinhas, que não viram atalho comum do Qt.

    Caps Lock: no Mac cada toque chega como liga/desliga, então vale pressionar ou soltar.
    Shift: só quando apertado e solto sem outra tecla no meio (Shift+letra continua normal).
    """

    last_caps = 0.0
    shift_down = None

    def _active(self):
        return QApplication.activeWindow() is mw and _reviewer()

    def eventFilter(self, obj, event):
        kind = event.type()
        if kind not in (QEvent.Type.KeyPress, QEvent.Type.KeyRelease) or event.isAutoRepeat():
            return False
        key, now = event.key(), time.monotonic()
        if key == Qt.Key.Key_Shift:
            if kind == QEvent.Type.KeyPress:
                self.shift_down = self.shift_down or now
            elif self.shift_down and now - self.shift_down < 0.8 and self._active():
                self.shift_down = None
                QTimer.singleShot(0, _edit)
            else:
                self.shift_down = None
            return False
        if kind == QEvent.Type.KeyPress:
            self.shift_down = None
        if key != Qt.Key.Key_CapsLock:
            return False
        if kind == QEvent.Type.KeyRelease and sys.platform != "darwin":
            return False
        if now - self.last_caps > 0.4 and self._active():
            self.last_caps = now
            QTimer.singleShot(0, _suspend)
        return False


_solo = _SoloKeys()
QApplication.instance().installEventFilter(_solo)
gui_hooks.state_shortcuts_will_change.append(_on_shortcuts)
gui_hooks.state_did_change.append(_on_state)
_log("carregado")
