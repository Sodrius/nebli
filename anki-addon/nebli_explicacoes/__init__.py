"""NEBLI — explicação do card com Tab (Anki desktop).

No verso do card, Tab mostra abaixo do texto a explicação daquele card; Tab ou qualquer
outra tecla fecha (a tecla de resposta responde na mesma hora). Uma explicação por
card (irmãos de cloze têm a sua), lida de user_files/explicacoes.sqlite, que é
gerada fora do Anki por `python -m nebli.explicacoes gerar`. Nada vai para a coleção.
Cada Tab é anotado em user_files/tab-log.jsonl (para achar os cards que mais pegam).

Não mexe em nenhuma outra tecla. Guia: GUIA-EXPLICACOES-TAB.md na raiz do NEBLI.
Instalar/atualizar: python -m nebli.explicacoes instalar (reiniciar o Anki depois).
"""
import hashlib
import html
import json
import sqlite3
import time
import traceback
from pathlib import Path

from aqt import gui_hooks, mw
from aqt.qt import QApplication, QEvent, QObject, Qt, QTimer

USER = Path(__file__).resolve().parent / "user_files"
STORE = USER / "explicacoes.sqlite"
LABELS = ("Base:", "Por quê:", "Na aula:", "Liga com:", "Não confundir:")
# Bloco logo abaixo do texto do card (dentro de #qa, como um comentário), fonte grande.
POPUP_JS = """(function(body){
  var old = document.getElementById('nebli-tab'); if (old) old.remove();
  var night = document.body.classList.contains('nightMode') || document.documentElement.classList.contains('night-mode');
  var d = document.createElement('div'); d.id = 'nebli-tab'; d.innerHTML = body;
  d.style.cssText = 'display:block;box-sizing:border-box;width:100%;max-width:960px;margin:22px auto 12px;'
    + 'padding:16px 22px;border-radius:12px;text-align:left;font:21px/1.6 -apple-system,system-ui,sans-serif;'
    + (night ? 'background:#23272e;color:#ececec;border-left:5px solid #6ea8fe;'
             : 'background:#f4f7fc;color:#1f2328;border-left:5px solid #3b6fd8;');
  d.setAttribute('role', 'note'); d.setAttribute('aria-label', 'Explicação do card');
  var texts = Array.from(document.querySelectorAll('#text')).filter(function(n){
    return n.getClientRects().length > 0;
  });
  var anchor = texts[texts.length - 1];
  if (anchor) anchor.insertAdjacentElement('afterend', d);
  else (document.getElementById('qa') || document.body).appendChild(d);
  d.scrollIntoView({block: 'nearest'});
})(__BODY__);"""
_popup = {"open": False}


def _log(message):
    USER.mkdir(exist_ok=True)
    with (USER / "log.txt").open("a", encoding="utf-8") as handle:
        handle.write(time.strftime("%Y-%m-%d %H:%M:%S ") + message + "\n")


def _reviewer():
    reviewer = getattr(mw, "reviewer", None)
    return reviewer if mw.state == "review" and reviewer and reviewer.card else None


def _card_hash(card):
    return hashlib.sha1(("\x1f".join(card.note().fields) + f"\x1e{card.ord}").encode("utf-8")).hexdigest()


def _lookup(card):
    if not STORE.exists():
        return None
    db = sqlite3.connect(f"file:{STORE}?mode=ro", uri=True)
    try:
        return db.execute("select status, texto, motivo, hash from explicacoes where card_id=?",
                          (card.id,)).fetchone()
    finally:
        db.close()


def _render(row, card):
    if not row:
        return "<i>Ainda sem explicação para este card.</i>", False
    status, text, reason, digest = row
    if status != "ok":
        return f"<i>Card marcado para revisão:</i> {html.escape(reason or '')}", True
    lines = []
    for line in html.escape(text or "", quote=False).splitlines():
        for label in LABELS:
            if line.startswith(label):
                line = f"<b>{label}</b>{line[len(label):]}"
        lines.append(line)
    body = "<br>".join(lines)
    if digest != _card_hash(card):
        body += "<div style='margin-top:6px;font-size:12px;opacity:.6'>O card mudou depois desta explicação.</div>"
    return body, True


def _close_popup(*_args):
    """Remove sempre (barato), mesmo se o card já mudou antes do fechamento agendado."""
    _popup["open"] = False
    reviewer = getattr(mw, "reviewer", None)
    if reviewer and reviewer.web:
        reviewer.web.eval("var n=document.getElementById('nebli-tab'); if(n) n.remove();")


def _toggle():
    try:
        reviewer = _reviewer()
        if not reviewer or reviewer.state != "answer":
            return
        if _popup["open"]:
            _close_popup()
            return
        card = reviewer.card
        body, found = _render(_lookup(card), card)
        reviewer.web.eval(POPUP_JS.replace("__BODY__", json.dumps(body)))
        _popup["open"] = True
        USER.mkdir(exist_ok=True)
        with (USER / "tab-log.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"em": time.strftime("%Y-%m-%d %H:%M:%S"), "card": card.id,
                                     "nota": card.nid, "deck": card.did, "achou": found}) + "\n")
    except Exception:
        _log(traceback.format_exc())


class _TabKey(QObject):
    def eventFilter(self, obj, event):
        if event.type() != QEvent.Type.KeyPress or event.isAutoRepeat():
            return False
        active = QApplication.activeWindow() is mw and _reviewer()
        if event.key() == Qt.Key.Key_Tab and not event.modifiers() and active:
            QTimer.singleShot(0, _toggle)
            return True  # Tab não passa adiante (no Anki ele só mudaria o foco)
        if _popup["open"]:
            QTimer.singleShot(0, _close_popup)  # qualquer tecla fecha; a tecla segue valendo
        return False


_tab = _TabKey()
QApplication.instance().installEventFilter(_tab)
gui_hooks.reviewer_did_show_question.append(_close_popup)
gui_hooks.reviewer_did_show_answer.append(_close_popup)
_log("carregado")
