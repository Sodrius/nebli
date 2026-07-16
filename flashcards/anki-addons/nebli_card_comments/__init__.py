# -*- coding: utf-8 -*-
"""NEBLI card comments.

Reviewer:
  Ctrl+Shift+C opens a dialog for the current card.
  The comment is appended to NEBLI_Comentario and tagged NEBLI_comentario::pendente.
  Categories: problema, qualidade, imagem, explicacao, escopo, outro.

The fields are created on the current note type if missing, so this works for
AnKingOverhaul, IO-one by one, BlueLink IOE+, Dope Anatomy and other copied notes.
"""
from datetime import datetime

from aqt import mw
from aqt.qt import QAction, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox, QShortcut, QKeySequence
from aqt.reviewer import Reviewer
from aqt.utils import showInfo, tooltip

CFIELD = "NEBLI_Comentario"
AFIELD = "NEBLI_Resposta"
PENDING = "NEBLI_comentario::pendente"
TAG_PREFIX = "NEBLI_comentario::tipo::"


def ensure_fields(note):
    model = note.note_type()
    changed = False
    names = [f["name"] for f in model["flds"]]
    for name in (CFIELD, AFIELD):
        if name not in names:
            field = mw.col.models.new_field(name)
            mw.col.models.add_field(model, field)
            changed = True
    if changed:
        mw.col.models.save(model)
        note.load()


def append_comment(note, category, text):
    ensure_fields(note)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"[{stamp}] [{category}] {text.strip()}"
    old = note[CFIELD].strip() if CFIELD in note else ""
    note[CFIELD] = (old + "<br>" + entry) if old else entry
    note.flush()
    mw.col.tags.bulk_add([note.id], f"{PENDING} {TAG_PREFIX}{category}")
    mw.col.set_schema_modified()


def current_note():
    if mw.state != "review" or not getattr(mw, "reviewer", None) or not mw.reviewer.card:
        return None
    return mw.reviewer.card.note()


def show_comment_dialog():
    note = current_note()
    if not note:
        showInfo("Nenhum card em revisão.")
        return
    dlg = QDialog(mw)
    dlg.setWindowTitle("Comentar card NEBLI")
    layout = QVBoxLayout(dlg)
    layout.addWidget(QLabel("Tipo de comentário"))
    combo = QComboBox()
    combo.addItems(["problema", "qualidade", "imagem", "explicacao", "escopo", "formatacao", "outro"])
    layout.addWidget(combo)
    layout.addWidget(QLabel("Comentário"))
    text = QTextEdit()
    text.setMinimumWidth(520)
    text.setMinimumHeight(180)
    layout.addWidget(text)
    row = QHBoxLayout()
    save = QPushButton("Salvar")
    cancel = QPushButton("Cancelar")
    row.addWidget(save)
    row.addWidget(cancel)
    layout.addLayout(row)

    def do_save():
        body = text.toPlainText().strip()
        if not body:
            tooltip("Comentário vazio.")
            return
        append_comment(note, combo.currentText(), body)
        tooltip("Comentário NEBLI salvo.")
        dlg.accept()

    save.clicked.connect(do_save)
    cancel.clicked.connect(dlg.reject)
    dlg.exec()


_orig_shortcut_keys = Reviewer._shortcutKeys


def _shortcut_keys(self):
    keys = _orig_shortcut_keys(self)
    keys.append(("Ctrl+Shift+C", show_comment_dialog))
    return keys


Reviewer._shortcutKeys = _shortcut_keys


def setup_menu():
    action = QAction("Comentar card NEBLI", mw)
    action.triggered.connect(show_comment_dialog)
    mw.form.menuTools.addAction(action)


setup_menu()
