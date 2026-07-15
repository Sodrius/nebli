#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""monitor_email_anking.py -- email de monitor NEBLI dos cards errados.

Modos disponíveis:
  --diario            cards reprovados HOJE (nota Again) nos blocos NEBLI::, explicados
                      em voz NEBLI (causa -> mecanismo -> consequência).
  --semanal           leeches (tag:leech OU lapses>=3) da semana, explicação sucinta.
  --bandeira          cards com flag:1 (vermelha). Suspende → explica 2 parágrafos cada
                      → envia email → dessuspende + remove flag. Sempre sob demanda.
  --suspender-vermelhos  suspende imediatamente todos os cards flag:1 sem email. Uso:
                      durante o estudo, antes de rodar --bandeira depois.
  --laranja           [DESCONTINUADO — Davi não usa mais bandeira laranja]

Roda NO PC (fala com AnkiConnect em localhost). Puxa os cards, chama a API Claude
pra redigir as explicações, e envia por Gmail SMTP para dpbdes@gmail.com.
Sempre acionado pelo Davi via pedido no chat (NUNCA automático).

Segredos por variável de ambiente (NUNCA no git):
  ANTHROPIC_API_KEY   chave da API Claude
  GMAIL_USER          remetente (default dpbdes@gmail.com)
  GMAIL_APP_PASSWORD  App Password do Gmail (16 chars, não a senha normal)

Uso:
  python flashcards/scripts/monitor_email_anking.py --bandeira
  python flashcards/scripts/monitor_email_anking.py --suspender-vermelhos
  python flashcards/scripts/monitor_email_anking.py --diario --dry-run
  python flashcards/scripts/monitor_email_anking.py --semanal
"""
import json, os, sys, argparse, datetime, html, re, smtplib, ssl
import subprocess, shutil
import urllib.request, urllib.error
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ANKICONNECT = "http://localhost:8765"
API_URL = "https://api.anthropic.com/v1/messages"
MODELO = os.environ.get("NEBLI_MONITOR_MODEL", "claude-sonnet-4-6")
DESTINO = "dpbdes@gmail.com"

# Paleta NEBLI real (typst-template/nebli_v2_apostila.typ) — CSS inline do email.
PALETA = {
    "navy": "#1E3A5F", "gold": "#C58A1D", "creme": "#FDF6E3",
    "texto": "#1F2E3D", "texto_claro": "#5B6B7A", "teal": "#0E6B7A",
    "borda": "#D8D2C5", "fundo": "#FBFAF6", "gold_bg": "#FBF1D8",
}
# Fonte do email: Inter (mesma vibe do The News) — sans-serif natural de newsletter,
# título e corpo na mesma família, distinção só por peso. Fallback email-safe cobre o Gmail.
# O @import carrega o Inter real onde o cliente suporta (Apple Mail); no Gmail cai no fallback nativo.
FONT_TIT = "Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
FONT_BODY = "Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"

# Gatilho da caixa "Vale estudar mais": nº de cards do mesmo tema.
DICA_MIN_DIARIO = 3
DICA_MIN_SEMANAL = 2

REF_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_ROOT = os.path.dirname(os.path.dirname(REF_DIR))

_TAG_HTML = re.compile(r"<[^>]+>")
_CLOZE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", re.DOTALL)
_CLOZE_NUM = re.compile(r"\{\{c(\d+)::(.*?)\}\}", re.DOTALL)
_IMG = re.compile(r"<img[^>]*>", re.IGNORECASE)
_WS = re.compile(r"\s+")


def limpar(campo):
    if not campo:
        return ""
    t = _IMG.sub(" [img] ", campo)
    t = _CLOZE.sub(r"[\1]", t)
    t = t.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    t = _TAG_HTML.sub(" ", t)
    return _WS.sub(" ", html.unescape(t)).strip()


_NOISE = re.compile(r"photo credit|wikimedia|cc by|\[img\]", re.IGNORECASE)


def partir_card(raw0, back_raw, is_cloze, ord):
    """Separa PERGUNTA (com lacuna) e RESPOSTA. Cloze: esconde só a lacuna deste card,
    revela as outras (é o que o aluno viu na frente); básico: front x back.
    Detecta cloze pelo MARKUP no campo (o nome do modelo do AnKing não traz 'cloze')."""
    if _CLOZE_NUM.search(raw0):
        alvo = ord + 1
        respostas = []

        def repl(m):
            num, inner = int(m.group(1)), m.group(2)
            texto, _, hint = inner.partition("::")
            if num == alvo:
                ans = limpar(texto)
                if ans:
                    respostas.append(ans)
                h = limpar(hint)
                return f"[ {h} ]" if h else "[ ____ ]"
            return texto   # outros clozes ficam revelados, como na frente do card

        pergunta = limpar(_CLOZE_NUM.sub(repl, raw0))
        if not respostas:   # ord não bateu: esconde todas e coleta todas
            respostas = [limpar(m[1]) for m in _CLOZE_NUM.findall(raw0)]
            pergunta = limpar(_CLOZE_NUM.sub("[ ____ ]", raw0))
        resposta = " · ".join(dict.fromkeys(r for r in respostas if r))
        return pergunta, resposta
    # card básico (pergunta/resposta em campos separados)
    pergunta = limpar(raw0)
    resposta = limpar(back_raw)
    if not resposta or _NOISE.search(resposta) or len(resposta) > 160:
        resposta = ""
    return pergunta, resposta


def _invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]


def _anki_vivo():
    try:
        _invoke("version")
        return True
    except (urllib.error.URLError, OSError, RuntimeError):
        return False


def sincronizar():
    """Dispara sync no container antes de ler os erros — puxa o que o celular subiu."""
    try:
        _invoke("sync")
        import time; time.sleep(8)   # sync é assíncrono; espera terminar
    except (urllib.error.URLError, OSError, RuntimeError):
        pass   # se falhar, segue mesmo assim (melhor email atrasado que nenhum)


def remover_bandeira(card_ids):
    """Zera a bandeira vermelha (flag) dos cards já explicados — reseta o ciclo
    pra o Davi re-marcar amanhã. Tenta o setter nativo do AnkiConnect; se a versão
    não expõe, cai pro fallback de tag (NEBLI::explicado::<data>) e o Davi tira a
    bandeira na mão. Retorna (metodo, n_ok)."""
    if not card_ids:
        return "nada", 0
    # 1) caminho ideal: setFlag nativo (AnkiConnect recente)
    try:
        _invoke("setFlag", cards=card_ids, flag=0)
        return "setFlag", len(card_ids)
    except (urllib.error.URLError, OSError, RuntimeError):
        pass
    # 2) escrita direta do campo 'flags' do card. IMPORTANTE: o valor tem que ser
    #    INTEIRO (0), não string "0" — com string o AnkiConnect faz no-op silencioso
    #    (verificado 2026-07-04 nesta coleção: só o int surte efeito).
    ok = 0
    for cid in card_ids:
        try:
            _invoke("setSpecificValueOfCard", card=cid,
                    keys=["flags"], newValues=[0], warning_check=True)
            ok += 1
        except (urllib.error.URLError, OSError, RuntimeError):
            ok = 0
            break
    if ok:
        return "setSpecificValueOfCard", ok
    # 3) fallback sem escrita de flag: marca como explicado hoje (o Davi desmarca)
    try:
        hoje = datetime.date.today().isoformat()
        notes = _invoke("cardsToNotes", cards=card_ids)
        _invoke("addTags", notes=notes, tags=f"NEBLI::explicado::{hoje}")
        return "tag-fallback", len(card_ids)
    except (urllib.error.URLError, OSError, RuntimeError):
        return "falhou", 0


def suspender_cards(card_ids, suspender=True):
    """Suspende ou dessuspende cards da fila de revisão.

    Usado no fluxo --bandeira: parqueia os cards enquanto o email ainda não chegou
    (suspender=True), depois os devolve à fila quando a explicação é enviada
    (suspender=False). Retorna n de cards processados; erros são não-fatais."""
    if not card_ids:
        return 0
    acao = "suspend" if suspender else "unsuspend"
    try:
        _invoke(acao, cards=card_ids)
        return len(card_ids)
    except (urllib.error.URLError, OSError, RuntimeError) as e:
        verbo = "suspender" if suspender else "dessuspender"
        print(f"(aviso: não conseguiu {verbo} cards via AnkiConnect: {e})")
        return 0


def coletar(modo):
    if modo == "diario":
        query = "tag:NEBLI::* -tag:NEBLI::zerado::* rated:1:1"
        teto = 8
    elif modo == "bandeira":
        # bandeira vermelha = flag:1; o Davi marca o que quer entender a fundo
        query = "tag:NEBLI::* -tag:NEBLI::zerado::* flag:1"
        # Nao cortar silenciosamente o feedback do Davi. 50 ainda protege o
        # tamanho do email, mas cobre com folga uma rodada normal de bandeiras.
        teto = 50
    else:
        query = "tag:NEBLI::* -tag:NEBLI::zerado::* (tag:leech OR prop:lapses>=3)"
        teto = 10
    card_ids = _invoke("findCards", query=query)
    if not card_ids:
        return []
    info = _invoke("cardsInfo", cards=card_ids)
    cards = []
    for c in info:
        campos = c.get("fields", {})
        if not campos:
            continue
        vals = list(campos.values())
        raw0 = vals[0]["value"]
        back_raw = vals[1]["value"] if len(vals) > 1 else ""
        is_cloze = bool(_CLOZE_NUM.search(raw0))
        pergunta, resposta = partir_card(raw0, back_raw, is_cloze, c.get("ord", 0))
        aula = next((t.split("::", 1)[1] for t in c.get("tags", [])
                     if t.startswith("NEBLI::") and not t.startswith("NEBLI::zerado")), "")
        cards.append({"cardId": c.get("cardId"),   # p/ tirar a bandeira depois
                      "pergunta": pergunta, "resposta": resposta,
                      "contexto": limpar(raw0),   # texto com resposta revelada, p/ o LLM
                      "lapses": c.get("lapses", 0), "aula": aula, "cloze": is_cloze})
    cards.sort(key=lambda x: -x["lapses"])
    return cards[:teto]


def agrupar(cards):
    """dict ordenado slug -> [cards], preservando a ordem por lapsos de coletar()."""
    grupos = {}
    for c in cards:
        grupos.setdefault(c["aula"] or "outros", []).append(c)
    return grupos


def _prettify_slug(slug):
    if not slug or slug == "outros":
        return "Outros"
    s = re.sub(r"^[a-z]+-\d+-", "", slug)          # tira prefixo tipo "anato-06-"
    s = s.replace("-", " ").strip()
    return s[:1].upper() + s[1:] if s else slug


_TITULOS_CACHE = None


def _mapa_titulos():
    """Lê os headings '### <slug> — <Título>' das referências (título acentuado)."""
    global _TITULOS_CACHE
    if _TITULOS_CACHE is not None:
        return _TITULOS_CACHE
    _TITULOS_CACHE = {}
    padrao = re.compile(r"^###\s+([a-z0-9\-]+)\s+[—-]\s+(.+?)\s*$")
    for nome in ("onde-aprofundar.md", "blueprint-step1.md"):
        caminho = os.path.join(REF_DIR, nome)
        try:
            with open(caminho, encoding="utf-8") as f:
                for linha in f:
                    m = padrao.match(linha)
                    if m and m.group(1) not in _TITULOS_CACHE:
                        _TITULOS_CACHE[m.group(1)] = m.group(2)
        except OSError:
            pass
    return _TITULOS_CACHE


def titulo_tema(slug):
    # 1) manifesto da curadoria (mais específico, título acentuado)
    caminho = os.path.join(PROJ_ROOT, "flashcards", "curadoria", f"{slug}.md")
    try:
        with open(caminho, encoding="utf-8") as f:
            for linha in f:
                m = re.match(r"\*\*Título:\*\*\s*(.+?)\s*$", linha)
                if m:
                    return m.group(1)
    except OSError:
        pass
    # 2) headings das referências; 3) prettify do slug
    return _mapa_titulos().get(slug) or _prettify_slug(slug)


def dica_blueprint(slug):
    """Célula 'Aprofundar na E1' da linha do slug no blueprint — hint do aprofundamento."""
    caminho = os.path.join(REF_DIR, "blueprint-step1.md")
    try:
        with open(caminho, encoding="utf-8") as f:
            for linha in f:
                if linha.lstrip().startswith("|") and slug in linha:
                    celulas = [c.strip() for c in linha.strip().strip("|").split("|")]
                    if len(celulas) >= 3 and celulas[2] not in ("—", "-", ""):
                        return celulas[2]
    except OSError:
        pass
    return None


PROMPT_SISTEMA = (
    "Você é um monitor de medicina no estilo NEBLI: explica em prosa fluida de "
    "monitor, sempre causa → mecanismo → consequência, sem empilhar siglas. "
    "Para cada flashcard que o aluno ERROU, escreva UM parágrafo curto (≤60 palavras) "
    "explicando o porquê do conteúdo — o mecanismo que faz a resposta ser aquela — "
    "não só repita a resposta. Tom direto, encorajador, de quem quer que ele entenda. "
    "Responda em texto simples, um bloco por card, começando com '• '."
)


def _cards_em_texto(cards):
    return "\n\n".join(
        f"[{i}] (errou {c['lapses']}x) {c['pergunta']}\nResposta: {c['resposta'][:300]}"
        for i, c in enumerate(cards, 1))


def _tarefa(modo, linhas):
    quando = "hoje" if modo == "diario" else "na semana"
    return (f"Cards que o aluno errou ({quando}). "
            f"Explique cada um em voz NEBLI:\n\n{linhas}")


def _via_claude_cli(prompt_completo, timeout=180):
    """Explicação pela ASSINATURA do Claude Code (claude -p), sem API paga."""
    exe = os.environ.get("NEBLI_CLAUDE_BIN") or shutil.which("claude") or "claude"
    # No Windows, `claude` é um shim .cmd — resolver via shell garante o PATHEXT.
    if os.name == "nt":
        cmd, usar_shell = f'"{exe}" -p', True
    else:
        cmd, usar_shell = [exe, "-p"], False
    try:
        p = subprocess.run(cmd, input=prompt_completo, shell=usar_shell,
                           capture_output=True, text=True,
                           encoding="utf-8", timeout=timeout)
    except (OSError, subprocess.SubprocessError):
        return None
    if p.returncode != 0:
        return None
    return (p.stdout or "").strip() or None


def _via_api(modo, linhas):
    """Comportamento legado: API paga (só roda se ANTHROPIC_API_KEY existir)."""
    chave = os.environ.get("ANTHROPIC_API_KEY")
    if not chave:
        return None
    corpo = {
        "model": MODELO,
        "max_tokens": 1500,
        "system": PROMPT_SISTEMA,
        "messages": [{"role": "user", "content": _tarefa(modo, linhas)}],
    }
    req = urllib.request.Request(
        API_URL, json.dumps(corpo).encode("utf-8"),
        headers={"x-api-key": chave, "anthropic-version": "2023-06-01",
                 "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.load(resp)
    return "".join(b.get("text", "") for b in data.get("content", []))


def bloco_colavel(modo, linhas):
    """Bloco pronto pra Davi copiar e colar num chatbot (Gemini/ChatGPT/Claude)."""
    modelo = os.environ.get("NEBLI_MODELO_COLAR", "Gemini 2.5 Flash (ou qualquer chatbot grátis)")
    return (
        "🔁 Cole o bloco abaixo num chatbot para a explicação card a card "
        f"(sugestão de modelo: {modelo}):\n"
        "──────────── copie a partir daqui ────────────\n"
        f"{PROMPT_SISTEMA}\n\n{_tarefa(modo, linhas)}\n"
        "──────────── até aqui ────────────")


def redigir(cards, modo, cerebro):
    """Retorna (explicacao|None, linhas_cruas). None => main decide o fallback."""
    linhas = _cards_em_texto(cards)
    if cerebro == "nenhum":
        return None, linhas
    if cerebro == "colar":
        return None, linhas          # o corpo vira o bloco colável (montado em main)
    if cerebro == "api":
        return _via_api(modo, linhas), linhas
    # cerebro == "claude" (padrão): assinatura do Claude Code, sem API
    return _via_claude_cli(f"{PROMPT_SISTEMA}\n\n{_tarefa(modo, linhas)}"), linhas


PROMPT_ESTRUT = (
    "Você é um monitor de medicina no estilo NEBLI: prosa fluida de monitor, sempre "
    "causa → mecanismo → consequência, sem empilhar siglas, tom direto e encorajador. "
    "O aluno ERROU os flashcards abaixo. Devolva SOMENTE um JSON válido, sem cercas de "
    "código, exatamente neste formato:\n"
    '{"cards": ["explicação do card 1", "explicação do card 2", ...], '
    '"dicas": {"<slug>": {"revisar": "...", "aprofundar": "..."}}}\n'
    "Regras: (1) 'cards' tem UMA explicação por card, na mesma ordem, ≤60 palavras, "
    "explicando o mecanismo que faz a resposta ser aquela (não repita a resposta). "
    "(2) 'dicas' só contém os slugs que eu marcar como TEMA COM MUITOS ERROS; para cada, "
    "'revisar' = o conceito base a refixar (1 linha) e 'aprofundar' = um passo além, uma "
    "nuance/mecanismo um tiquinho mais fundo (1 linha curta). Tudo em conceito puro, SEM "
    "nomes de plataforma/curso. Se não houver tema marcado, deixe 'dicas' vazio {}."
)


PROMPT_BANDEIRA = (
    "Você é um monitor de medicina no estilo NEBLI: prosa fluida de monitor, sempre "
    "causa → mecanismo → consequência, sem empilhar siglas, tom direto e encorajador. "
    "O aluno MARCOU estes flashcards com bandeira porque quer entendê-los a fundo — "
    "não errou durante revisão, escolheu eles de propósito. Devolva SOMENTE um JSON "
    "válido, sem cercas de código, exatamente neste formato:\n"
    '{"cards": ["explicação card 1", "explicação card 2", ...], '
    '"padroes": "síntese dos padrões frágeis", "dicas": {}}\n'
    "Regras:\n"
    "(1) 'cards': UMA explicação por card, na mesma ordem. Cada explicação tem DOIS "
    "PARÁGRAFOS separados por \\n\\n:\n"
    "  §1 — o mecanismo do card (o que ele testa, por que a resposta é aquela, "
    "causa → mecanismo → consequência, ≤80 palavras)\n"
    "  §2 — contexto: por que esse conceito importa para a aula do bloco NEBLI em "
    "questão, como se liga ao tema, o que mudaria se fosse diferente (≤60 palavras)\n"
    "(2) 'padroes': UM parágrafo de síntese (≤100 palavras) identificando quais "
    "mecanismos ou conceitos parecem frágeis a partir dos cards marcados. Não é lista "
    "de cards — é o padrão que os conecta. Ex: 'Você marcou 3 cards sobre transporte "
    "ativo. O padrão é que o gasto de ATP no contra-transporte parece inseguro...'\n"
    "(3) 'dicas': deixe sempre vazio {}.\n"
    "Sem nomes de plataforma, sem 'Step 1', sem 'USMLE'."
)


def _llm(prompt, cerebro):
    """Chama o cérebro (claude -p ou API) com um prompt livre. Retorna texto ou None."""
    if cerebro == "api":
        chave = os.environ.get("ANTHROPIC_API_KEY")
        if not chave:
            return None
        corpo = {"model": MODELO, "max_tokens": 2000,
                 "messages": [{"role": "user", "content": prompt}]}
        try:
            req = urllib.request.Request(
                API_URL, json.dumps(corpo).encode("utf-8"),
                headers={"x-api-key": chave, "anthropic-version": "2023-06-01",
                         "content-type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.load(resp)
            return "".join(b.get("text", "") for b in data.get("content", []))
        except (urllib.error.URLError, OSError, ValueError):
            return None
    return _via_claude_cli(prompt)   # claude (padrão)


def _extrair_json(texto):
    """Extrai o primeiro objeto JSON do texto (tolera cercas/prosa em volta)."""
    if not texto:
        return None
    for tentativa in (texto, texto[texto.find("{"): texto.rfind("}") + 1]):
        try:
            return json.loads(tentativa)
        except (json.JSONDecodeError, ValueError):
            continue
    return None


def redigir_estruturado(cards, slugs_gatilho, modo, cerebro):
    """Retorna (explicacoes: list[str], dicas: dict, padroes: str) ou (None, {}, '')."""
    linhas = "\n\n".join(
        f"[{i}] (errou {c['lapses']}x, tema={c['aula'] or 'outros'}) Pergunta: {c['pergunta']}"
        f"\nResposta: {c['resposta'][:300]}"
        for i, c in enumerate(cards, 1))
    if modo == "bandeira":
        rotulo = "marcados com bandeira"
        prompt = f"{PROMPT_BANDEIRA}\n\nCards ({rotulo}):\n\n{linhas}"
    else:
        marcados = ""
        if slugs_gatilho:
            marcados = "\n\nTEMAS COM MUITOS ERROS (gere 'dicas' para estes slugs):\n" + "\n".join(
                f"- {s} ({titulo_tema(s)})"
                + (f" · hint de aprofundamento: {dica_blueprint(s)}" if dica_blueprint(s) else "")
                for s in slugs_gatilho)
        rotulo = {"diario": "hoje", "semanal": "da semana"}.get(modo, "")
        prompt = f"{PROMPT_ESTRUT}\n\nCards ({rotulo}):\n\n{linhas}{marcados}"
    dados = _extrair_json(_llm(prompt, cerebro))
    if not isinstance(dados, dict):
        return None, {}, ""
    exps = dados.get("cards")
    if not isinstance(exps, list) or len(exps) < len(cards):
        return None, {}, ""
    dicas = dados.get("dicas") if isinstance(dados.get("dicas"), dict) else {}
    padroes = str(dados.get("padroes", "")).strip() if modo == "bandeira" else ""
    return [str(e) for e in exps[:len(cards)]], dicas, padroes


def montar_email(cards, explicacao, modo, auto=True):
    hoje = datetime.date.today().strftime("%d/%m/%Y")
    titulo = {"diario": "NEBLI · seus erros de hoje",
              "bandeira": "NEBLI · os cards que você marcou",
              }.get(modo, "NEBLI · resumo semanal dos cards que mais erra")
    if modo == "bandeira":
        quantos = f"Você marcou {len(cards)} card(s) com bandeira vermelha."
    else:
        quantos = f"{len(cards)} card(s) caíram {'hoje' if modo=='diario' else 'nesta semana'}."
    abertura = (f"{quantos} Aqui vai o porquê de cada um, em voz de monitor:" if auto
                else f"{quantos} O bloco abaixo está pronto pra colar num chatbot:")
    corpo = f"{titulo} — {hoje}\n\n{abertura}\n\n{explicacao}\n\n— NEBLI (monitor automático)"
    return titulo, corpo


def _subtitulo(modo):
    if modo == "bandeira":
        return "os cards que você marcou pra entender a fundo"
    return "seus erros de hoje" if modo == "diario" else "o que mais te derruba — resumo semanal"


def _resumo_contagem(grupos, modo):
    total = sum(len(v) for v in grupos.values())
    partes = [f"{len(v)} de {titulo_tema(s)}" for s, v in grupos.items()]
    if modo == "bandeira":
        return total, (f"Você marcou {total} card(s) com bandeira vermelha — "
                       + ", ".join(partes) + ". Aqui vai o mecanismo de cada um.")
    quando = "hoje" if modo == "diario" else "nesta semana"
    return total, f"{total} card(s) caíram {quando} — " + ", ".join(partes) + "."


def estatisticas_semana():
    """Estatísticas dos blocos NEBLI:: para o rodapé motivacional do semanal."""
    def n(q):
        try:
            return len(_invoke("findCards", query=q))
        except (urllib.error.URLError, OSError, RuntimeError):
            return 0
    base = "tag:NEBLI::* -tag:NEBLI::zerado::*"
    rev = n(f"{base} rated:7")
    again = n(f"{base} rated:7:1")
    retencao = round(100 * (1 - again / rev)) if rev else None
    maduros = n(f"{base} is:mature")
    total = n(base)
    leeches = n(f"{base} tag:leech")
    dias = 0
    try:
        lim = datetime.date.today() - datetime.timedelta(days=6)
        for d in _invoke("getNumCardsReviewedByDay") or []:
            try:
                if datetime.date.fromisoformat(d[0]) >= lim and d[1] > 0:
                    dias += 1
            except (ValueError, IndexError, TypeError):
                pass
    except (urllib.error.URLError, OSError, RuntimeError):
        pass
    return {"revisoes": rev, "retencao": retencao, "maduros": maduros,
            "total": total, "leeches": leeches, "dias": dias}


def obter_stats_hoje():
    """Estatísticas dos cards NEBLI revisados hoje — usadas no email de bandeira."""
    def n(q):
        try:
            return len(_invoke("findCards", query=q))
        except (urllib.error.URLError, OSError, RuntimeError):
            return 0
    base = "tag:NEBLI::* -tag:NEBLI::zerado::*"
    total = n(f"{base} rated:1")
    erros = n(f"{base} rated:1:1")
    leeches = n(f"{base} (tag:leech OR prop:lapses>=3)")
    ativos = n(f"{base} -is:suspended")
    return {
        "revisoes_hoje": total,
        "erros_hoje": erros,
        "retencao_hoje": round(100 * (1 - erros / total)) if total else None,
        "leeches": leeches,
        "ativos": ativos,
    }


def _tile(P, numero, rotulo):
    return (f'<td width="25%" align="center" valign="top" style="padding:16px 8px">'
            f'<div style="font-family:{FONT_TIT};font-size:26px;font-weight:700;color:{P["navy"]};'
            f'line-height:1">{numero}</div>'
            f'<div style="font-family:{FONT_TIT};font-size:9.5px;letter-spacing:.8px;'
            f'text-transform:uppercase;color:{P["texto_claro"]};margin-top:6px">{rotulo}</div></td>')


def _bloco_stats(P, stats, grupos):
    if not stats:
        return ""
    ret = f'{stats["retencao"]}%' if stats["retencao"] is not None else "—"
    tiles = (_tile(P, stats["revisoes"], "revisões")
             + _tile(P, ret, "retenção")
             + _tile(P, f'{stats["dias"]}/7', "dias estudados")
             + _tile(P, stats["maduros"], "cards maduros"))
    tema = max(grupos, key=lambda s: len(grupos[s])) if grupos else None
    linha_tema = ""
    if tema:
        linha_tema = (f'<tr><td colspan="4" style="border-top:1px solid {P["borda"]};'
                      f'padding:11px 16px;text-align:center;font-family:{FONT_BODY};'
                      f'font-size:12px;color:{P["texto_claro"]}">O que mais te derrubou: '
                      f'<b style="color:{P["texto"]}">{html.escape(titulo_tema(tema))}</b>'
                      f' · leeches ativos: <b style="color:{P["texto"]}">{stats["leeches"]}</b></td></tr>')
    return (f'<tr><td style="padding:0 0 24px">'
            f'<table width="100%" cellpadding="0" cellspacing="0" '
            f'style="background:{P["creme"]};border-radius:12px">'
            f'<tr>{tiles}</tr>{linha_tema}</table></td></tr>')


def _bloco_stats_hoje(P, stats):
    """Stats do dia (bandeira): revisões hoje, retenção hoje, leeches, cards ativos."""
    if not stats:
        return ""
    ret = f'{stats["retencao_hoje"]}%' if stats["retencao_hoje"] is not None else "—"
    tiles = (_tile(P, stats["revisoes_hoje"], "revisões hoje")
             + _tile(P, ret, "retenção hoje")
             + _tile(P, stats["leeches"], "leeches")
             + _tile(P, stats["ativos"], "cards ativos"))
    return (f'<tr><td style="padding:0 0 24px">'
            f'<table width="100%" cellpadding="0" cellspacing="0" '
            f'style="background:{P["creme"]};border-radius:12px">'
            f'<tr>{tiles}</tr></table></td></tr>')


def montar_html(grupos, dicas, modo, stats=None, padroes=""):
    P = PALETA
    esc = html.escape
    hoje = datetime.date.today().strftime("%d/%m/%Y")
    _, resumo = _resumo_contagem(grupos, modo)

    secoes = []
    contador = 0
    for slug, cards in grupos.items():
        cab = (f'<tr><td style="padding:34px 0 4px">'
               f'<div style="font-family:{FONT_TIT};font-size:11px;font-weight:700;letter-spacing:2px;'
               f'text-transform:uppercase;color:{P["navy"]}">{esc(titulo_tema(slug))}</div>'
               f'<div style="font-family:{FONT_TIT};font-size:10px;letter-spacing:1px;'
               f'color:{P["texto_claro"]};margin-top:4px">{len(cards)} card(s)</div>'
               f'<div style="width:30px;height:2px;background:{P["gold"]};margin-top:11px"></div></td></tr>')
        linhas = [cab]
        for c in cards:
            contador += 1
            resp = ""
            if c.get("resposta"):
                resp = (f'<div style="font-family:{FONT_TIT};margin:12px 0 3px;font-size:10px;'
                        f'letter-spacing:1.5px;text-transform:uppercase;color:{P["texto_claro"]}">Resposta</div>'
                        f'<div style="font-family:{FONT_BODY};font-size:15px;line-height:1.5;'
                        f'color:{P["gold"]};font-weight:700">{esc(c["resposta"])}</div>')
            exp = esc(c.get("_exp", "")).replace("\n", "<br>")
            idx = (f'<span style="font-family:{FONT_TIT};color:{P["gold"]};font-size:12px;'
                   f'font-weight:700;letter-spacing:1px">{contador:02d}</span>'
                   f'<span style="color:{P["borda"]}">&nbsp;&nbsp;</span>')
            linhas.append(
                f'<tr><td style="padding:24px 0;border-bottom:1px solid {P["borda"]}">'
                f'<div style="font-family:{FONT_TIT};font-size:10px;letter-spacing:1.5px;'
                f'text-transform:uppercase;color:{P["texto_claro"]};margin-bottom:6px">Pergunta</div>'
                f'<div style="font-family:{FONT_BODY};font-size:16px;line-height:1.55;'
                f'color:{P["texto"]};font-weight:700">{idx}{esc(c["pergunta"])}</div>{resp}'
                f'<div style="font-family:{FONT_TIT};margin:14px 0 3px;font-size:10px;'
                f'letter-spacing:1.5px;text-transform:uppercase;color:{P["teal"]}">Por que</div>'
                f'<div style="font-family:{FONT_BODY};font-size:15px;line-height:1.8;'
                f'color:{P["texto"]}">{exp}</div></td></tr>')
        if slug in dicas and isinstance(dicas[slug], dict):
            d = dicas[slug]
            rev = esc(d.get("revisar", "")) if d.get("revisar") else ""
            apr = esc(d.get("aprofundar", "")) if d.get("aprofundar") else ""
            corpo_d = ""
            if rev:
                corpo_d += (f'<div style="margin-bottom:6px"><b style="color:{P["navy"]}">Revê. </b>{rev}</div>')
            if apr:
                corpo_d += (f'<div><b style="color:{P["navy"]}">Aprofunda um tiquinho. </b>{apr}</div>')
            if corpo_d:
                linhas.append(
                    f'<tr><td style="padding:22px 0 6px">'
                    f'<table width="100%" cellpadding="0" cellspacing="0">'
                    f'<tr><td style="background:{P["creme"]};border-radius:14px;padding:20px 22px;'
                    f'font-family:{FONT_BODY};font-size:13.5px;line-height:1.7;color:{P["texto"]}">'
                    f'<div style="font-family:{FONT_TIT};font-weight:700;color:{P["gold"]};'
                    f'text-transform:uppercase;font-size:10px;letter-spacing:2px;margin-bottom:11px">'
                    f'Vale estudar mais</div>{corpo_d}</td></tr></table></td></tr>')
        secoes.append(
            f'<table width="100%" cellpadding="0" cellspacing="0">{"".join(linhas)}</table>')

    if modo == "bandeira":
        rodape = ("Marcou porque quis entender — esse é o jeito certo de usar o deck. "
                  "A bandeira já foi tirada; amanhã marque de novo o que ainda não fixou.")
    elif modo == "diario":
        rodape = ("Leia com calma, uma lacuna de cada vez. Cada card que você entende hoje "
                  "é um pedaço da prova que já não te pega amanhã.")
    else:
        rodape = ("Repetiu o erro? Volte ao mecanismo, não à resposta — é ele que fica. "
                  "Toda semana que você encara estes, eles ficam menores.")
    bloco_stats_html = (_bloco_stats_hoje(P, stats) if modo == "bandeira"
                        else _bloco_stats(P, stats, grupos))
    bloco_padroes_html = ""
    if padroes and modo == "bandeira":
        bloco_padroes_html = (
            f'<table width="100%" cellpadding="0" cellspacing="0" style="margin-top:28px">'
            f'<tr><td style="background:{P["navy"]};border-radius:14px;padding:22px 26px">'
            f'<div style="font-family:{FONT_TIT};font-size:10px;font-weight:700;letter-spacing:2.5px;'
            f'text-transform:uppercase;color:{P["gold"]};margin-bottom:12px">Padrões frágeis</div>'
            f'<div style="font-family:{FONT_BODY};font-size:14.5px;line-height:1.75;color:#D4DDE7">'
            f'{esc(padroes)}</div>'
            f'</td></tr></table>')
    return (
        f'<!DOCTYPE html><html><head><meta charset="utf-8">'
        f'<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<link rel="preconnect" href="https://fonts.googleapis.com">'
        f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        f'<link href="https://fonts.googleapis.com/css2?'
        f'family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
        f"<style>@import url('https://fonts.googleapis.com/css2?"
        f"family=Inter:wght@400;500;600;700&display=swap');</style>"
        f'</head><body style="margin:0;padding:0;background:{P["fundo"]}">'
        f'<table width="100%" cellpadding="0" cellspacing="0" style="background:{P["fundo"]}">'
        f'<tr><td align="center" style="padding:28px 12px">'
        f'<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px">'
        # cabeçalho navy — sóbrio
        f'<tr><td style="background:{P["navy"]};border-radius:14px 14px 0 0;padding:26px 30px">'
        f'<div style="font-family:{FONT_TIT};color:{P["gold"]};font-size:12px;letter-spacing:6px;'
        f'font-weight:700">NEBLI</div>'
        f'<div style="font-family:{FONT_TIT};color:#fff;font-size:19px;font-weight:600;'
        f'margin-top:10px;line-height:1.3">{_subtitulo(modo)}</div>'
        f'<div style="font-family:{FONT_BODY};color:#98A8BA;font-size:12px;margin-top:5px">{hoje}</div></td></tr>'
        # corpo — branco, arejado
        f'<tr><td style="background:#fff;border:1px solid {P["borda"]};border-top:none;'
        f'border-radius:0 0 14px 14px;padding:26px 30px 30px">'
        f'<div style="font-family:{FONT_BODY};font-size:14px;line-height:1.6;color:{P["texto_claro"]};'
        f'margin-bottom:22px">{esc(resumo)}</div>'
        f'<table width="100%" cellpadding="0" cellspacing="0">{bloco_stats_html}</table>'
        f'{"".join(secoes)}'
        f'{bloco_padroes_html}'
        f'<div style="font-family:{FONT_BODY};margin-top:26px;padding-top:16px;'
        f'border-top:1px solid {P["borda"]};font-size:12px;line-height:1.6;color:{P["texto_claro"]}">'
        f'{rodape}<br><span style="font-family:{FONT_TIT};letter-spacing:2px;color:{P["navy"]};'
        f'font-size:11px">NEBLI</span> · monitor automático</div>'
        f'</td></tr></table></td></tr></table></body></html>')


def montar_texto(grupos, dicas, modo, stats=None, padroes=""):
    """Fallback texto puro, já enriquecido (contagem + agrupado + dica)."""
    hoje = datetime.date.today().strftime("%d/%m/%Y")
    _, resumo = _resumo_contagem(grupos, modo)
    out = [f"NEBLI · {_subtitulo(modo)} — {hoje}", "", resumo, ""]
    if stats:
        if modo == "bandeira":
            ret = f'{stats["retencao_hoje"]}%' if stats["retencao_hoje"] is not None else "—"
            out += [f"Hoje: {stats['revisoes_hoje']} revisões · retenção {ret} · "
                    f"{stats['leeches']} leeches · {stats['ativos']} cards ativos", ""]
        else:
            ret = f'{stats["retencao"]}%' if stats["retencao"] is not None else "—"
            out += [f"Semana: {stats['revisoes']} revisões · retenção {ret} · "
                    f"{stats['dias']}/7 dias · {stats['maduros']} cards maduros · "
                    f"{stats['leeches']} leeches ativos", ""]
    for slug, cards in grupos.items():
        out.append(f"== {titulo_tema(slug)} ({len(cards)}) ==")
        out.append("")
        for i, c in enumerate(cards, 1):
            out.append(f"[{i:02d}] Pergunta: {c['pergunta']}")
            if c.get("resposta"):
                out.append(f"     Resposta: {c['resposta']}")
            out.append(f"     Por que: {c.get('_exp','')}")
            out.append("")
        if slug in dicas and isinstance(dicas[slug], dict):
            d = dicas[slug]
            if d.get("revisar"):
                out.append(f">> VALE ESTUDAR MAIS — Revê: {d['revisar']}")
            if d.get("aprofundar"):
                out.append(f"   Aprofunda um tiquinho: {d['aprofundar']}")
            out.append("")
    if padroes and modo == "bandeira":
        out += ["", "== PADRÕES FRÁGEIS ==", "", padroes, ""]
    out.append("— NEBLI (monitor automático)")
    return "\n".join(out)


def enviar(assunto, corpo, html_corpo=None):
    user = os.environ.get("GMAIL_USER", DESTINO)
    senha = os.environ.get("GMAIL_APP_PASSWORD")
    if not senha:
        raise RuntimeError("GMAIL_APP_PASSWORD ausente — configure para enviar.")
    if html_corpo:
        msg = MIMEMultipart("alternative")
        msg.attach(MIMEText(corpo, "plain", "utf-8"))
        msg.attach(MIMEText(html_corpo, "html", "utf-8"))
    else:
        msg = MIMEText(corpo, "plain", "utf-8")
    msg["Subject"] = assunto
    msg["From"] = user
    msg["To"] = DESTINO
    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as s:
        s.login(user, senha)
        s.sendmail(user, [DESTINO], msg.as_string())


def main():
    ap = argparse.ArgumentParser(description="Email de monitor NEBLI dos cards errados.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--diario", action="store_const", dest="modo", const="diario")
    g.add_argument("--semanal", action="store_const", dest="modo", const="semanal")
    g.add_argument("--bandeira", action="store_const", dest="modo", const="bandeira",
                   help="explica os cards com bandeira vermelha (flag:1), suspende-os "
                        "enquanto gera o email, dessuspende após enviar e tira a bandeira")
    g.add_argument("--suspender-vermelhos", action="store_const", dest="modo",
                   const="suspender-vermelhos",
                   help="suspende imediatamente todos os cards flag:1 sem enviar email — "
                        "use durante o estudo para parquear cards; rode --bandeira depois "
                        "para receber as explicações e devolvê-los à fila")
    ap.add_argument("--cerebro", choices=["claude", "colar", "api", "nenhum"],
                    default=os.environ.get("NEBLI_MONITOR_CEREBRO", "claude"),
                    help="quem redige a explicação: claude (assinatura Claude Code, sem API, padrão) "
                         "| colar (bloco pronto pro Gemini) | api (paga) | nenhum (cards crus)")
    ap.add_argument("--dry-run", action="store_true", help="imprime o email, não envia")
    ap.add_argument("--send", action="store_true", help="confirma envio SMTP e mutações pós-entrega")
    ap.add_argument("--apply", action="store_true", help="confirma mutação sem email (suspender-vermelhos)")
    ap.add_argument("--sync", action="store_true", help="sincroniza explicitamente antes da coleta")
    ap.add_argument("--read-only", action="store_true",
                    help="força cerebro=nenhum, sem sync, SMTP, mutação ou escrita de preview")
    args = ap.parse_args()

    if args.read_only:
        args.dry_run = True
        args.send = False
        args.apply = False
        args.sync = False
        args.cerebro = "nenhum"
    if not args.send:
        args.dry_run = True

    if not _anki_vivo():
        print("AnkiConnect fora do ar — abra o Anki/Docker com o add-on 2055492159.")
        sys.exit(3)

    # Modo especial: suspender cards vermelhos sem enviar email
    if args.modo == "suspender-vermelhos":
        if not args.apply:
            print("[PREVIEW] suspender-vermelhos não alterou nada. Use --apply para confirmar.")
            return
        if args.sync:
            sincronizar()
        flagged = _invoke("findCards", query="tag:NEBLI::* -tag:NEBLI::zerado::* flag:1")
        if not flagged:
            print("Nenhum card com bandeira vermelha para suspender.")
            return
        n = suspender_cards(flagged, suspender=True)
        print(f"{n} card(s) com bandeira vermelha suspensos da fila.")
        print("Rode --bandeira quando quiser receber a explicação — eles voltam à fila após o email.")
        return

    if args.sync:
        sincronizar()   # puxa erros do celular somente quando solicitado

    cards = coletar(args.modo)

    # Bandeira: suspende apenas cards ativos. O snapshot impede que cards já
    # suspensos por outro motivo sejam dessuspensos cegamente no final.
    ids_suspensos_pelo_fluxo = []
    if args.modo == "bandeira" and args.send and cards:
        ids_flag = [c["cardId"] for c in cards if c.get("cardId")]
        try:
            estados = _invoke("areSuspended", cards=ids_flag)
            ids_suspensos_pelo_fluxo = [cid for cid, susp in zip(ids_flag, estados) if susp is False]
        except (urllib.error.URLError, OSError, RuntimeError):
            ids_suspensos_pelo_fluxo = []
        n_susp = suspender_cards(ids_suspensos_pelo_fluxo, suspender=True)
        if n_susp:
            print(f"{n_susp} card(s) suspensos da fila enquanto preparo a explicação...")
    if not cards:
        vazio = {"diario": "Nenhum card errado hoje.",
                 "bandeira": "Nenhum card com bandeira vermelha.",
                 "semanal": "Nenhum card recorrente na semana."}.get(args.modo, "Nada.")
        print(f"{vazio} Nada a enviar 👏")
        return

    assunto = {"diario": "NEBLI · seus erros de hoje",
               "bandeira": "NEBLI · os cards que você marcou",
               "semanal": "NEBLI · o que mais te derruba (semanal)"}[args.modo]
    corpo, html_corpo = None, None

    if args.cerebro in ("claude", "api"):
        grupos = agrupar(cards)
        # bandeira não gera caixa "vale estudar mais" — é explicação pura
        if args.modo == "bandeira":
            gatilho = []
        else:
            limiar = DICA_MIN_DIARIO if args.modo == "diario" else DICA_MIN_SEMANAL
            gatilho = [s for s, v in grupos.items() if s != "outros" and len(v) >= limiar]
        explicacoes, dicas, padroes = redigir_estruturado(cards, gatilho, args.modo, args.cerebro)
        if explicacoes is not None:
            for c, e in zip(cards, explicacoes):
                c["_exp"] = e
            if args.modo == "semanal":
                stats = estatisticas_semana()
            elif args.modo == "bandeira":
                stats = obter_stats_hoje()
            else:
                stats = None
            corpo = montar_texto(grupos, dicas, args.modo, stats, padroes)
            html_corpo = montar_html(grupos, dicas, args.modo, stats, padroes)
        else:   # JSON/LLM falhou — degrada pro bloco colável apenas em preview
            print("(cérebro indisponível ou JSON inválido — caindo pro bloco colável)\n")
            if args.send:
                print("Envio cancelado: o email estruturado não ficou pronto; bandeiras preservadas.")
                return 5
            _, crus = redigir(cards, args.modo, "colar")
            _, corpo = montar_email(cards, bloco_colavel(args.modo, crus), args.modo, auto=False)
    else:   # colar / nenhum — caminho simples de texto, inalterado
        explicacao, crus = redigir(cards, args.modo, args.cerebro)
        if explicacao is None:
            explicacao = crus if args.cerebro == "nenhum" else bloco_colavel(args.modo, crus)
        _, corpo = montar_email(cards, explicacao, args.modo, auto=False)

    # bandeira: SEMPRE grava o registro HTML local do dia (fallback + histórico)
    if args.modo == "bandeira" and html_corpo:
        os.makedirs(os.path.join(PROJ_ROOT, "arquivos-trabalho"), exist_ok=True)
        registro = os.path.join(PROJ_ROOT, "arquivos-trabalho",
                                f"bandeira-{datetime.date.today().isoformat()}.html")
        with open(registro, "w", encoding="utf-8") as f:
            f.write(html_corpo)
        print("Registro HTML salvo em:", registro)

    if args.dry_run:
        print("===== [DRY-RUN] email que seria enviado =====")
        print("Para:", DESTINO, "| Assunto:", assunto)
        if html_corpo and args.modo != "bandeira":
            os.makedirs(os.path.join(PROJ_ROOT, "arquivos-trabalho"), exist_ok=True)
            prev = os.path.join(PROJ_ROOT, "arquivos-trabalho", f"preview-email-{args.modo}.html")
            with open(prev, "w", encoding="utf-8") as f:
                f.write(html_corpo)
            print("Preview HTML salvo em:", prev)
        if args.modo == "bandeira":
            print("(dry-run: bandeira NÃO foi removida)")
        print("-" * 50)
        print(corpo)
        return

    if args.modo == "bandeira":
        # email é best-effort; o HTML local já garante a entrega
        delivered = False
        try:
            enviar(assunto, corpo, html_corpo)
            delivered = True
            print(f"Email da bandeira enviado para {DESTINO} ({len(cards)} cards).")
        except (RuntimeError, OSError, ssl.SSLError, smtplib.SMTPException) as e:
            print(f"Email não enviado: {e}. Bandeiras e suspensão foram preservadas.")
        if not delivered:
            suspender_cards(ids_suspensos_pelo_fluxo, suspender=False)
            return 4
        # reset do ciclo: tira a bandeira dos cards já explicados
        ids = [c["cardId"] for c in cards if c.get("cardId")]
        metodo, n = remover_bandeira(ids)
        print(f"Bandeira removida de {n} card(s) via {metodo}"
              + (" — amanhã re-marque o que ainda não fixou." if metodo != "falhou" else
                 " (FALHOU — tire a bandeira na mão no Anki)."))
        # Devolve os cards à fila — email foi enviado, hora de revisar com o contexto
        n_dess = suspender_cards(ids_suspensos_pelo_fluxo, suspender=False)
        if n_dess:
            print(f"{n_dess} card(s) devolvidos à fila — leia o email antes de revisá-los.")
        return

    enviar(assunto, corpo, html_corpo)
    print(f"Email {args.modo} enviado para {DESTINO} ({len(cards)} cards).")


if __name__ == "__main__":
    raise SystemExit(main() or 0)
