"""NEBLI — atalhos de revisão pedidos por Davi em 30/09/2026.

Durante a revisão:
    a s d f     De novo / Difícil / Bom / Fácil (no lugar de 1 2 3 4; só com a resposta à vista)
    1 2 3 4     bandeira (guia do Davi sobre o card): vermelha = tem problema, conserta e volta a
                bandeira de antes / verde = levar para a vida / azul = importante, ver se leva /
                rosa = detalhe, pode esquecer
    q w e r     COMANDO (tag na nota, para cumprir na revisão; não mexe na bandeira; tecla de novo
                desfaz): imagem ruim ou faltando / comentário ruim / escrita ruim / dois ou mais problemas
    Caps Lock suspende o card atual; Caps Lock + 9 suspende HY (um só toque, mesmo no verde); Caps Lock sozinho no verde pede dois toques
    '           enterra o card atual (volta amanhã); F-20261003-CLAUDE-19: “coloca o enterrar pro botão de '”
    c           comentário (Enter salva, Shift+Enter quebra a linha): abre o campo NEBLI_Comentario da nota para escrever
    v           voltar: desfaz a última ação e volta ao card anterior (Cmd/Ctrl+Z também)
    Ctrl + / -  aumenta / reduz o zoom em todas as janelas (persistente entre sessões)

A explicação com Tab é outro add-on (nebli_explicacoes), para quem quiser só ela.

Conflitos resolvidos só na tela de revisão: atalhos globais e de menu nas mesmas
teclas (a Adicionar, s Estudar, d Baralhos, f Criar filtrado...) ficam desligados
enquanto se revisa e voltam nas outras telas; e (Editar) e r (repetir áudio) viram bandeiras. F5 continua repetindo o áudio
e o botão Editar continua no rodapé; v deixa de tocar a gravação de voz.

Instalar/atualizar pelo repositório: python -m nebli.decks instalar-addon
(reiniciar o Anki depois). Carregamento e erros vão para user_files/log.txt.
"""
import html
import json
import re
import sys
import time
import traceback
from pathlib import Path

from aqt import gui_hooks, mw
from aqt.qt import (QAction, QApplication, QDialog, QDialogButtonBox, QEvent, QKeySequence, QLabel,
                    QObject, QPlainTextEdit, QShortcut, Qt, QTextCursor, QTimer, QVBoxLayout, QWidget)
from aqt.utils import tooltip

ANSWER = {"a": 1, "s": 2, "d": 3, "f": 4}
# Bandeira e comando são coisas diferentes: bandeira orienta o Davi sobre o card; comando é uma
# ordem para cumprir quando ele pedir a revisão dos cards (como o x de "gostei").
COMMANDS = {  # tecla -> (tag na nota, ícone, significado)
    "q": ("NEBLI::comando::imagem", "", "faltou imagem ou imagem ruim (não é bandeira vermelha)"),
    "w": ("NEBLI::comando::comentario", "", "comentário ruim"),
    "e": ("NEBLI::comando::escrita", "", "escrita ruim"),
    "r": ("NEBLI::comando::multiplos", "", "dois ou mais problemas / não sei dizer"),
}
NUMBER_FLAGS = {"1": 1, "2": 3, "3": 4, "4": 5}  # cores: vermelha, verde, azul, rosa
FLAG_MEANINGS = {
    1: ("vermelha", "tem um problema: consertar e voltar a bandeira de antes"),
    3: ("verde", "levar para a vida"),
    4: ("azul", "importante: ver se leva para a vida"),
    5: ("rosa", "detalhe: pode esquecer"),
}
COMMENT_KEY = "c"
UNDO_KEY = "v"
REDO_KEY = "z"  # F-20261013-CLAUDE-03: z refaz o que o v desfez (como Ctrl+Y)
BURY_KEY = "'"  # F-20261003-CLAUDE-19 (era Shift sozinho)
TAKEN = set("1234") | set(ANSWER) | set(COMMANDS) | {COMMENT_KEY, UNDO_KEY, REDO_KEY, BURY_KEY}
FIELD = "NEBLI_Comentario"
PENDING = "NEBLI_comentario::pendente"
USER = Path(__file__).resolve().parent / "user_files"
ZOOM_FILE = USER / "zoom.json"
FLAG_HISTORY = USER / "flag-history.jsonl"
ZOOM_STEP = 0.10
ZOOM_MIN = 0.50
ZOOM_MAX = 2.50


def _log(message):
    USER.mkdir(exist_ok=True)
    with (USER / "log.txt").open("a", encoding="utf-8") as handle:
        handle.write(time.strftime("%Y-%m-%d %H:%M:%S ") + message + "\n")


def _guarded(fn):
    def run(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:
            _log(traceback.format_exc())
            tooltip("Atalho NEBLI falhou; detalhes em user_files/log.txt do add-on.")
    return run


def _reviewer():
    reviewer = getattr(mw, "reviewer", None)
    return reviewer if mw.state == "review" and reviewer and reviewer.card else None


def _load_zoom():
    try:
        return min(ZOOM_MAX, max(ZOOM_MIN, float(json.loads(ZOOM_FILE.read_text())["factor"])))
    except (FileNotFoundError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        return 1.0


_zoom = _load_zoom()


def _apply_zoom():
    for window in QApplication.topLevelWidgets():
        if window.isVisible():
            _apply_zoom_to_window(window)


def _apply_zoom_to_window(window):
    """Amplia controles nativos e todo conteúdo web visível da janela."""
    try:
        base = window.property("_nebli_zoom_base_point")
        if base is None:
            base = window.font().pointSizeF()
            if base <= 0:
                base = QApplication.font().pointSizeF()
            if base <= 0:
                base = 12.0
            window.setProperty("_nebli_zoom_base_point", base)
        font = window.font()
        font.setPointSizeF(max(6.0, float(base) * _zoom))
        window.setFont(font)
        _set_web_zoom(window)
        for widget in window.findChildren(QWidget):
            if widget.isVisible() and callable(getattr(widget, "setZoomFactor", None)):
                widget.setZoomFactor(_zoom)
    except RuntimeError:
        pass  # janela fechada durante a atualização


def _set_web_zoom(widget):
    try:
        if widget.isVisible() and callable(getattr(widget, "setZoomFactor", None)):
            widget.setZoomFactor(_zoom)
    except RuntimeError:
        pass


@_guarded
def _change_zoom(delta):
    global _zoom
    _zoom = round(min(ZOOM_MAX, max(ZOOM_MIN, _zoom + delta)), 2)
    USER.mkdir(exist_ok=True)
    ZOOM_FILE.write_text(json.dumps({"factor": _zoom}) + "\n", encoding="utf-8")
    _apply_zoom()
    tooltip(f"Zoom do Anki: {round(_zoom * 100)}%")


@_guarded
def _answer(ease):
    reviewer = _reviewer()
    if reviewer and reviewer.state == "answer":
        reviewer._answerCard(ease)


@_guarded
def _flag(flag, reason=""):
    reviewer = _reviewer()
    if reviewer:
        old_flag = reviewer.card.user_flag()
        if flag == 1 and old_flag != 1:
            USER.mkdir(exist_ok=True)
            with FLAG_HISTORY.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps({"card": reviewer.card.id, "previous_flag": old_flag,
                                         "reason": reason, "at": time.strftime("%Y-%m-%d %H:%M:%S")},
                                        ensure_ascii=False) + "\n")
        reviewer.set_flag_on_current_card(flag)
        QTimer.singleShot(50, _show_flag_status)


def _show_flag_status(*_args):
    """Davi, 01/11/2026: "tira a mensagem que fica lá embaixo sempre pequena dizendo o significado da bandeira e dos
    comandos". Não mostra mais nada no rodapé; só apaga o rótulo deixado por versões anteriores."""
    reviewer = _reviewer()
    if reviewer:
        reviewer.web.eval("(function(){const el=document.getElementById('nebli-flag-status'); if (el) el.remove();})();")


# Davi, 03/10/2026 (F-20261003-CLAUDE-15): "só não quero suspender hy, se tiver a tag"; "para suspender verde
# quero clicar 2x no caps lock"; "quero enterrar card no shift tb".
HY_TAGS = ("#Low/HighYield::1-HighYield", "NEBLI::IA::step::HY")
DOUBLE = 2.5  # tempo para repetir o atalho no mesmo card verde
CAPS_9_WINDOW = 1.2  # no Mac, Caps Lock é uma tecla de alternância, não um modificador Qt


def _is_hy(card):
    return any(t.endswith(HY_TAGS[0]) or t.lower() == HY_TAGS[1].lower() for t in card.note().tags)


_green_armed = {"cid": None, "at": 0.0}


@_guarded
def _command(key):
    """q/w/e/r: liga ou desliga a tag-comando na nota, sem tocar na bandeira."""
    reviewer = _reviewer()
    if not reviewer:
        return
    tag, _icon, meaning = COMMANDS[key]
    note = reviewer.card.note()
    on = not any(t.lower() == tag.lower() for t in note.tags)
    if on:
        note.add_tag(tag)
    else:
        note.remove_tag(tag)
    try:
        from aqt.operations.note import update_note
        update_note(parent=mw, note=note).success(
            lambda _: QTimer.singleShot(50, _show_flag_status)).run_in_background()
    except ImportError:
        mw.col.update_note(note)
        QTimer.singleShot(50, _show_flag_status)
    tooltip(f"Comando: {meaning}" if on else f"Comando removido: {meaning}")


@_guarded
def _suspend(allow_hy=False, expected_card_id=None):
    reviewer = _reviewer()
    if not reviewer:
        return
    card = reviewer.card
    if expected_card_id is not None and card.id != expected_card_id:
        return
    if _is_hy(card) and not allow_hy:
        tooltip("Card HY: use Caps Lock + 9 para suspender.")
        return
    # Davi, 31/10: "TÔ TENDO QUE PRESSIONAR CAPS + 9 2x, quero que seja só uma / tá duplicando por ser verde" — Caps Lock + 9 já é
    # uma confirmação deliberada; o segundo toque no verde vale só para o Caps Lock sozinho.
    if card.user_flag() == 3 and not allow_hy:
        now = time.monotonic()
        if _green_armed["cid"] == card.id and now - _green_armed["at"] <= DOUBLE:
            _green_armed["cid"] = None
            reviewer.suspend_current_card()
        else:
            _green_armed.update(cid=card.id, at=now)
            tooltip("Card verde: repita o mesmo atalho para suspender.")
        return
    reviewer.suspend_current_card()


@_guarded
def _bury():
    reviewer = _reviewer()
    if reviewer:
        reviewer.bury_current_card()


@_guarded
def _undo():
    if _reviewer():
        (getattr(mw, "undo", None) or mw.onUndo)()


@_guarded
def _redo():
    if _reviewer():
        redo = getattr(mw, "redo", None)
        if redo:
            redo()
        else:
            mw.form.actionRedo.trigger()


@_guarded
def _edit():
    if _reviewer():
        mw.onEditCurrent()


def _as_text(value):
    value = re.sub(r"<br\s*/?>|</div>|</p>", "\n", value, flags=re.I)
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


class _CommentBox(QPlainTextEdit):
    """Enter salva o comentário; Shift+Enter quebra a linha."""

    def __init__(self, text, on_save):
        super().__init__(text)
        self._on_save = on_save

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter) \
                and not event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self._on_save()
            return
        super().keyPressEvent(event)


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
    layout.addWidget(QLabel("O que há de errado ou a melhorar neste card? Enter salva, Shift+Enter quebra a linha, Esc cancela."))
    old_text = _as_text(note[FIELD]).rstrip()
    box = _CommentBox(old_text + "\n\n" if old_text else "", dialog.accept)
    box.setMinimumSize(520, 180)
    layout.addWidget(box)
    buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Save
                               | QDialogButtonBox.StandardButton.Cancel)
    buttons.accepted.connect(dialog.accept)
    buttons.rejected.connect(dialog.reject)
    layout.addWidget(buttons)
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
    shortcuts.extend((key, lambda key=key: _command(key)) for key in COMMANDS)
    shortcuts.extend((key, lambda flag=flag, key=key: _flag(flag, key)) for key, flag in NUMBER_FLAGS.items())
    shortcuts.append((COMMENT_KEY, _comment))
    shortcuts.append((UNDO_KEY, _undo))
    shortcuts.append((REDO_KEY, _redo))
    shortcuts.append((BURY_KEY, _bury))


_parked = {}  # atalhos de menu/globais tirados durante a revisão -> atalho original


def _on_state(new_state, _old_state):
    """Tecla com dois donos fica ambígua para o Qt e nenhum dispara (ex.: F de "Criar
    baralho filtrado" no menu Ferramentas). Na revisão, estaciona os outros donos das
    nossas teclas; fora dela, devolve."""
    try:
        if new_state == "review":
            QTimer.singleShot(0, _apply_zoom)
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
    """Caps Lock suspende; 9 logo depois libera a suspensão de HY.

    No Mac, Caps Lock é uma tecla de alternância, não um modificador reconhecido pelo Qt.
    No HY, um toque em Caps Lock arma o 9 seguinte por um curto intervalo.
    """

    last_caps = 0.0
    caps_armed_at = 0.0
    hy_card_id = None

    def _active(self):
        return QApplication.activeWindow() is mw and _reviewer()

    def eventFilter(self, obj, event):
        kind = event.type()
        if kind not in (QEvent.Type.KeyPress, QEvent.Type.KeyRelease) or event.isAutoRepeat():
            return False
        key, now = event.key(), time.monotonic()
        if key == Qt.Key.Key_9 and kind == QEvent.Type.KeyPress:
            reviewer = self._active()
            if (reviewer and reviewer.card.id == self.hy_card_id
                    and now - self.caps_armed_at <= CAPS_9_WINDOW):
                self.caps_armed_at = 0.0
                self.hy_card_id = None
                card_id = reviewer.card.id
                QTimer.singleShot(0, lambda cid=card_id: _suspend(allow_hy=True, expected_card_id=cid))
            return False
        if key != Qt.Key.Key_CapsLock:
            return False
        if kind == QEvent.Type.KeyRelease and sys.platform != "darwin":
            return False
        if now - self.last_caps > 0.2 and self._active():  # 0,2 s: separa toques de verdade de eco do mesmo toque
            self.last_caps = now
            reviewer = _reviewer()
            if _is_hy(reviewer.card):
                self.caps_armed_at = now
                self.hy_card_id = reviewer.card.id
                tooltip("Card HY: pressione 9 para suspender.")
            else:
                self.caps_armed_at = 0.0
                self.hy_card_id = None
                card_id = reviewer.card.id
                QTimer.singleShot(0, lambda cid=card_id: _suspend(expected_card_id=cid))
        return False


class _GlobalZoom(QObject):
    """Captura o zoom antes dos atalhos locais e alcança janelas abertas depois."""

    def eventFilter(self, obj, event):
        kind = event.type()
        if kind == QEvent.Type.Show:
            if isinstance(obj, QWidget) and obj.isWindow():
                QTimer.singleShot(0, lambda window=obj: _apply_zoom_to_window(window))
            elif callable(getattr(obj, "setZoomFactor", None)):
                QTimer.singleShot(0, lambda widget=obj: _set_web_zoom(widget))
            return False
        if kind not in (QEvent.Type.ShortcutOverride, QEvent.Type.KeyPress):
            return False
        if QApplication.activeWindow() is None:
            return False
        modifiers = event.modifiers()
        control = Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.MetaModifier
        if not modifiers & control or modifiers & Qt.KeyboardModifier.AltModifier:
            return False
        key = event.key()
        if key in (Qt.Key.Key_Plus, Qt.Key.Key_Equal):
            step = ZOOM_STEP
        elif key in (Qt.Key.Key_Minus, Qt.Key.Key_Underscore):
            step = -ZOOM_STEP
        else:
            return False
        if kind == QEvent.Type.ShortcutOverride:
            event.accept()
            return False
        _change_zoom(step)
        return True


_solo = _SoloKeys()
QApplication.instance().installEventFilter(_solo)
_global_zoom = _GlobalZoom()
QApplication.instance().installEventFilter(_global_zoom)
gui_hooks.state_shortcuts_will_change.append(_on_shortcuts)
gui_hooks.state_did_change.append(_on_state)
gui_hooks.reviewer_did_show_question.append(_show_flag_status)
gui_hooks.reviewer_did_show_answer.append(_show_flag_status)
QTimer.singleShot(0, _apply_zoom)
_log("carregado")
