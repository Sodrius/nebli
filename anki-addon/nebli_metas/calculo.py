"""Quanto falta para as metas de cards novos do GoalBar (semana, mês, ano).

Puro, sem aqt: o painel no Anki e o aviso do Claude (~/.claude/hooks/nebli_metas_aviso.py)
usam as mesmas contas. Períodos e contagem iguais aos do GoalBar: semana começa na segunda,
mês civil, ano a partir de start_month/start_day; card novo = primeira revisão no período,
sem contar suspensos.
"""
from datetime import date, datetime, time, timedelta

PERIODOS = (("weekly", "Semana"), ("monthly", "Mês"), ("yearly", "Ano"))


def janela(periodo, hoje, start_month=1, start_day=1):
    """(início, fim) do período que contém `hoje`; fim exclusivo."""
    if periodo == "weekly":
        inicio = hoje - timedelta(days=hoje.weekday())
        return inicio, inicio + timedelta(days=7)
    if periodo == "monthly":
        inicio = hoje.replace(day=1)
        fim = inicio.replace(year=inicio.year + 1, month=1) if inicio.month == 12 else inicio.replace(month=inicio.month + 1)
        return inicio, fim
    inicio = _data(hoje.year, start_month, start_day)
    if hoje < inicio:
        inicio = _data(hoje.year - 1, start_month, start_day)
    return inicio, _data(inicio.year + 1, start_month, start_day)


def anterior(periodo, inicio, start_month=1, start_day=1):
    return janela(periodo, inicio - timedelta(days=1), start_month, start_day)


def _data(ano, mes, dia):
    while True:
        try:
            return date(ano, mes, dia)
        except ValueError:
            dia -= 1


def _ms(dia):
    return int(datetime.combine(dia, time.min).astimezone().timestamp() * 1000)


def novos(scalar, deck_ids, inicio, fim):
    """Cards cuja primeira revisão caiu em [inicio, fim). `scalar(sql, *params)` devolve um valor."""
    if not deck_ids:
        return 0
    marcas = ", ".join("?" for _ in deck_ids)
    return int(scalar(
        f"SELECT COUNT(*) FROM (SELECT cid FROM revlog WHERE cid IN "
        f"(SELECT id FROM cards WHERE did IN ({marcas}) AND queue != -1) "
        f"GROUP BY cid HAVING MIN(id) >= ? AND MIN(id) < ?)",
        *deck_ids, _ms(inicio), _ms(fim)) or 0)


def situacao(scalar, deck_ids, metas, hoje, start_month=1, start_day=1):
    """Uma linha por meta ativa: feito, falta, dias, por dia, ritmo e o período anterior."""
    linhas = []
    for periodo, rotulo in PERIODOS:
        alvo = metas.get(periodo)
        if not alvo:
            continue
        inicio, fim = janela(periodo, hoje, start_month, start_day)
        feito = novos(scalar, deck_ids, inicio, fim)
        total_dias = (fim - inicio).days
        passados = (hoje - inicio).days  # dias inteiros antes de hoje, como o marcador do GoalBar
        restam = (fim - hoje).days  # contando hoje
        esperado = round(alvo * passados / total_dias)
        falta = max(0, alvo - feito)
        ant_inicio, ant_fim = anterior(periodo, inicio, start_month, start_day)
        linhas.append({
            "periodo": periodo,
            "rotulo": rotulo,
            "alvo": alvo,
            "feito": feito,
            "falta": falta,
            "restam_dias": restam,
            "por_dia": -(-falta // restam) if restam else falta,
            "media_ate_aqui": round(feito / (passados + 1), 1),
            "pct_meta": round(100 * feito / alvo),
            "pct_tempo": round(100 * passados / total_dias),
            "ritmo": feito - esperado,  # > 0 à frente, < 0 atrás
            "fim": fim.isoformat(),
            "anterior": {
                "inicio": ant_inicio.isoformat(),
                "fim": ant_fim.isoformat(),
                "feito": novos(scalar, deck_ids, ant_inicio, ant_fim),
            },
        })
    return linhas


def metas_do_goalbar(config):
    """[(deck_id, {periodo: alvo}, start_month, start_day)] das metas de cards novos ativas."""
    saida = []
    for deck in (config or {}).get("decks", []):
        metas = {}
        for periodo, _ in PERIODOS:
            meta = deck.get(periodo) or {}
            if meta.get("enabled") and meta.get("metric") == "new_cards" and int(meta.get("target") or 0) > 0:
                metas[periodo] = int(meta["target"])
        if metas:
            ano = deck.get("yearly") or {}
            saida.append((int(deck["deck_id"]), metas, int(ano.get("start_month") or 1), int(ano.get("start_day") or 1)))
    return saida
