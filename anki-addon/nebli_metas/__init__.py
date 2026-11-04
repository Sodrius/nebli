"""Painel único de metas de cards novos na parte inferior da tela inicial.

Lê as metas configuradas no GoalBar (1071423745) e substitui apenas a
visualização dele na tela inicial. Contas em calculo.py. Erros em user_files/log.txt.
"""
import sys
import time
import traceback
from datetime import date, timedelta
from html import escape
from pathlib import Path

from aqt import gui_hooks, mw

from . import calculo

GOALBAR = "1071423745"
USER = Path(__file__).resolve().parent / "user_files"


def _log(message):
    USER.mkdir(exist_ok=True)
    with (USER / "log.txt").open("a", encoding="utf-8") as handle:
        handle.write(time.strftime("%Y-%m-%d %H:%M:%S ") + message + "\n")


def _deck_ids(deck_id):
    nomes = {int(d.id): d.name for d in mw.col.decks.all_names_and_ids()}
    nome = nomes.get(deck_id)
    if nome is None:
        return []
    return [i for i, n in nomes.items() if n == nome or n.startswith(nome + "::")]


def _n(valor):
    return f"{valor:,}".replace(",", ".")


def _dias(n):
    return "1 dia" if n == 1 else f"{n} dias"


def _prazo(fim):
    ultimo = date.fromisoformat(fim) - timedelta(days=1)
    mes = ("jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez")[ultimo.month - 1]
    return f"{ultimo.day} {mes} {ultimo.year}"


def _linha(l):
    titulo = escape(l["rotulo"])
    ritmo = l["ritmo"]
    if ritmo > 0:
        rel, cls = f"{_n(ritmo)} à frente", "nm-frente"
    elif ritmo < 0:
        rel, cls = f"{_n(-ritmo)} atrás", "nm-atras"
    else:
        rel, cls = "no ritmo", ""
    largura = min(100, max(0, l["pct_meta"]))
    prazo = _prazo(l["fim"])
    if l["falta"]:
        acao = f'<strong>{_n(l["falta"])}</strong><span>faltam</span>'
        plano = f'<b>{_n(l["por_dia"])} novos/dia</b> por {_dias(l["restam_dias"])}'
    else:
        acao = '<strong>✓</strong><span>meta batida</span>'
        plano = f'Meta batida · {_n(l["feito"] - l["alvo"])} além do alvo'
    return f"""
    <section class="nm-row" aria-label="Meta da {titulo.lower()}">
        <div class="nm-top"><span class="nm-title">{titulo}</span><span class="nm-deadline">até {prazo}</span></div>
        <div class="nm-main">
            <div class="nm-count"><strong>{_n(l['feito'])}</strong><span> / {_n(l['alvo'])} novos</span></div>
            <div class="nm-remaining">{acao}</div>
        </div>
        <div class="nm-meter" role="progressbar" aria-label="Progresso da {titulo.lower()}" aria-valuemin="0" aria-valuemax="{l['alvo']}" aria-valuenow="{min(l['feito'], l['alvo'])}">
            <div class="nm-fill" style="width:{largura}%"></div>
            <div class="nm-tick" style="left:{min(100, max(0, l['pct_tempo']))}%" title="Ponto esperado pelo tempo decorrido"></div>
        </div>
        <div class="nm-bottom"><span>{plano}</span><span class="nm-pace {cls}">{rel}</span></div>
    </section>"""


def painel():
    config = mw.addonManager.getConfig(GOALBAR)
    blocos = []
    for deck_id, metas, start_month, start_day in calculo.metas_do_goalbar(config):
        ids = _deck_ids(deck_id)
        if not ids:
            continue
        linhas = calculo.situacao(mw.col.db.scalar, ids, metas, date.today(), start_month, start_day)
        blocos.append("".join(_linha(l) for l in linhas))
    if not blocos:
        return ""
    corpo = "".join(f'<div class="nm-widget">{b}</div>' for b in blocos)
    return (f'{_STYLE}<div class="nm-wrap">'
            f'<div class="nm-heading">Metas de cards novos</div>'
            f'{corpo}</div>')


def _goalbar_html():
    addon = sys.modules.get(f"{GOALBAR}.goal_tracking_progress_bar.addon")
    service = getattr(addon, "_service", None)
    cache = getattr(service, "_cache", None)
    return getattr(cache, "html", "") or ""


def _render(deck_browser, content):
    try:
        html = painel()
        if not html:
            return
        goalbar = _goalbar_html()
        pos = content.stats.find(goalbar) if goalbar else -1
        if pos >= 0:
            content.stats = content.stats[:pos] + html + content.stats[pos + len(goalbar):]
        else:
            content.stats += html
    except Exception:
        _log(traceback.format_exc())


gui_hooks.deck_browser_will_render_content.append(_render)


_STYLE = """
<style>
.nm-wrap { max-width: 580px; margin: 16px auto 4px; color: var(--fg, #263238); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
.nm-heading { margin: 0 2px 8px; font-size: 12px; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; opacity: .65; text-align: left; }
.nm-widget { padding: 4px 16px; border: 1px solid rgba(127,140,153,.22); border-radius: 14px; background: var(--canvas, rgba(255,255,255,.72)); text-align: left; box-shadow: 0 8px 24px rgba(0,0,0,.035); }
.nm-widget + .nm-widget { margin-top: 10px; }
.nm-row { padding: 12px 0; }
.nm-row + .nm-row { border-top: 1px solid rgba(127,140,153,.18); }
.nm-top, .nm-main, .nm-bottom { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; }
.nm-title { font-size: 13px; font-weight: 700; }
.nm-deadline { font-size: 11px; opacity: .65; }
.nm-main { margin-top: 5px; }
.nm-count strong { font-size: 23px; font-variant-numeric: tabular-nums; letter-spacing: -.04em; }
.nm-count span { font-size: 12px; opacity: .65; }
.nm-remaining { display: flex; align-items: baseline; gap: 4px; color: #2c8657; }
.nm-remaining strong { font-size: 19px; font-variant-numeric: tabular-nums; }
.nm-remaining span { font-size: 11px; }
.nm-meter { position: relative; height: 7px; margin-top: 9px; border-radius: 999px; background: rgba(127,140,153,.17); overflow: visible; }
.nm-fill { height: 100%; border-radius: inherit; background: linear-gradient(90deg,#65ae82,#2c8657); }
.nm-tick { position: absolute; top: -3px; width: 2px; height: 13px; border-radius: 2px; background: #6b7580; }
.nm-bottom { margin-top: 7px; font-size: 11px; line-height: 1.4; }
.nm-bottom b { font-weight: 700; }
.nm-pace { opacity: .72; white-space: nowrap; }
.nm-pace.nm-frente { color: #2c8657; opacity: 1; }
.nm-pace.nm-atras { color: #bf6257; opacity: 1; }
.nightMode .nm-widget, .night_mode .nm-widget { background: rgba(255,255,255,.035); border-color: rgba(255,255,255,.13); }
.nightMode .nm-remaining, .night_mode .nm-remaining, .nightMode .nm-pace.nm-frente, .night_mode .nm-pace.nm-frente { color: #80c89b; }
@media (max-width: 520px) { .nm-widget { padding: 4px 12px; } .nm-count strong { font-size: 20px; } .nm-bottom { gap: 4px; } }
</style>
"""
