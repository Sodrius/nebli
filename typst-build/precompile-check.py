#!/usr/bin/env python3
"""
NEBLI -- precompile-check.py
Criado em 2026-05-14 para resolver o problema de truncamento silencioso
de Edit/append em arquivos .typ grandes.

Estendido em 2026-05-15 (v2) para tres bugs persistentes da Geracao 20:
  (a) Truncamento de ULTIMA LINHA -- o Write pode cortar a ultima frase
      sem deixar NULL byte. Detectado em #3 aminoacidos, #4 compartimentos,
      #5 carboidratos. Nova regra: ultima linha nao-vazia deve fechar em
      `]`, `)`, `}` OU em palavra alfanumerica COMPLETA seguida de fim
      de linha. Pega o caso "empurr" (truncamento no meio de "empurra").

  (b) Threshold da E4 -- exigia >=8 prova-blocks, mas E4 enxuta de tema
      SUPERFICIAL tem 3-7. Falso-positivo em 3 dos 5 relatorios. Novo
      criterio: >=3 questoes totais (prova-mc + prova-ce + prova-discursiva
      + alias legacy prova-block + discursiva).

  (c) Paridade de alternativas MC da E2 -- regra canonica 80-120%
      violada SISTEMATICAMENTE (21 de 23 MC no #5 Carboidratos, ratio
      medio 210%, max 467%). Novo modulo: parseia etapa2.typ + main.typ,
      calcula ratio correta vs distratora-mediana, alerta cada questao
      fora da faixa 0.80-1.30.

Roda ANTES de `typst compile`. Se falhar com erro, NAO compilar.
Warnings nao bloqueiam (a menos que --strict).

Validacoes (resumo):
  Para cada arquivo .typ:
    1. Existe e nao esta vazio
    2. Nao contem NULL bytes (\x00)
    3. Brackets balanceados: (), [], {}
    4. Estrutura minima esperada (regras por arquivo)
    5. Ultima linha nao-vazia fecha limpa (truncamento detectado)
    6. v3: acentuacao PT-BR, markdown leakage, math mode quimica, helpers
       duplicados no template.
    7. v4 (2026-05-22): 4 regras canonicas da E2 -- ordem invertida,
       paridade intra-questao, Mapa de Confusoes, sorteio do gabarito.

  Por arquivo:
    - etapa1.typ:    >=1 #intro-box, >=1 #conclusao-box, >=1 #sigla
    - etapa2.typ:    exatamente 30 chamadas de #questao-mc OU #questao-ce
    - etapa3.typ:    exatamente 5 chamadas de #discursiva
    - etapa4.typ:    NAO validada (E4 removida do pipeline em 2026-05-22).
    - resumindo.typ: >=1 chamada de #resumindo-page OU `#let secoes-resumindo`
    - nebli_v2_apostila.typ: todos os helpers canonicos, >15kB, fim limpo.

  Passo (f) -- TAIL VISUAL (2026-05-18, propostas-pos-g20 1.5):
    Imprime as ultimas 3 linhas nao-vazias de cada .typ. Auxilio visual
    para o caso onde o conteudo do meio truncou mas o fim aparente
    continua sao (check_clean_ending so olha o ultimo char). Humano
    bate o olho e julga: se as ultimas linhas nao parecem fechamento
    canonico (`]`, `)`, `})`), suspeitar de Edit incompleto antes de
    compilar.

  Modulo opcional (so se etapa2.typ + main.typ ambos presentes):
    - PARIDADE MC: ratio correta/distratora-mediana entre 0.80-1.30 por questao.
    - E2-REGRAS (canonico 2026-05-22, redesenho de 2026-05-18): valida
      as 4 regras do QUESTIONADOR introduzidas no .claude/agents/questionador.md:
        (a) ordem invertida -- proxy: correta nao sistematicamente em A
            (>40% em A = warning; >=60% = erro -- sugere correta redigida 1o).
        (b) paridade intra-questao -- correta <= 1.25 x MAIOR distratora em
            palavras (regra: nunca encurtar correta, engordar distratoras).
        (c) Mapa de Confusoes -- exige `mapa-confusoes/<slug>.md` com >=4
            confusoes por subtopico `## X.Y`. Slug inferido do CWD
            (`_par_<slug>/`) ou via --slug NOME.
        (d) sorteio do gabarito -- nenhuma letra A-E ocupa >=50% (warn)
            ou >=67% (erro); sequencias monotonicas >=5 iguais (warn) /
            >=6 (erro). 3 iguais seguidas e canonico (regra do questionador).

Uso:
  python3 precompile-check.py              # checa tudo no cwd + template
  python3 precompile-check.py FILE.typ     # checa so esse arquivo
  python3 precompile-check.py --no-template  # pula validacao do template
  python3 precompile-check.py --no-paridade  # pula auditoria de paridade MC
  python3 precompile-check.py --no-e2-regras # pula 4 regras canonicas da E2
  python3 precompile-check.py --slug NOME    # forca slug para checar mapa-confusoes
  python3 precompile-check.py --strict     # warnings viram erro

Exit codes:
  0 = ok
  1 = erro de estrutura / helper ausente / paridade
  2 = erro de bracket (provavel truncamento)
  3 = arquivo faltando, vazio, NULL bytes, ou ultima linha truncada
"""

import re
import sys
from pathlib import Path

# Windows cp1252 quebra ao imprimir Unicode (subscripts, setas) — forcar UTF-8
# no stdout/stderr. Canonico 2026-05-22 (bug pego ao reprocessar F0F1 → F₀F₁
# no sumario do tema cadeia-respiratoria).
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, Exception):
    pass

# ============================================================
# v3 (2026-05-16) -- frente B4 do plano de economia de tokens.
# Adicionados 4 checks novos:
#   - check_acentuacao (PT-BR sem acento = bug catastrofico #6)
#   - check_helpers_duplicados (template com `resumindo-page` 2x)
#   - check_markdown_leakage (`**bold**` em Typst)
#   - check_math_mode_quimica (`$Ka$` com identificador multi-letra)
# ============================================================

ACENTOS_SET = set("áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ")
LIMIAR_ACENTOS_ERRO = 0.005   # < 0.5% -> erro
LIMIAR_ACENTOS_WARN = 0.015   # < 1.5% -> warning

# Identificadores multi-letra problemáticos em math mode Typst.
# `Ka`, `CO2`, `HCO3` -- viram variaveis indefinidas em $...$.
# Detecta `$...$` curto contendo 2+ letras maiusculas seguidas, ou
# `\b[A-Z][a-z]+\b` dentro do math.
MATH_QUIMICA_RE = re.compile(r"\$[^$\n]{1,80}?\$")
MATH_QUIMICA_TRIGGERS = re.compile(r"\b(?:Ka|Kb|Kw|CO2|HCO3|H2O|NaCl|HCl|NaOH|H2CO3|"
                                   r"H2PO4|HPO4|NH3|NH4)\b")

# Markdown `**bold**` vazado (Typst usa `*bold*`).
MARKDOWN_BOLD_RE = re.compile(r"(?<!\*)\*\*([^\s*][^*]*?[^\s*])\*\*(?!\*)")

# Vocabulario de PROVA proibido no corpo da E1 e Resumindo (regra 10
# do redator-e1.md, canonico 2026-05-22). Banco eh calibracao invisivel;
# leitor jamais sabe que existe banco de questoes.
VOCAB_PROVA_RE = re.compile(
    r"\b("
    r"prova|provas|banca|pegadinha|pegadinhas|"
    r"quest[aã]o|quest[oõ]es|gabarito|examinador|examinadora|enunciado|"
    r"vestibular|enare|usmle|fmusp|cespe|ufrgs|"
    r"simulado|simulados"
    # P1/P2/P3 com palavra "prova" proxima -- tratado em check separado.
    r")\b",
    re.IGNORECASE,
)
# "cai/caiu/caem em prova", "isso cai" -- so quando contexto deixa claro.
VOCAB_PROVA_CAI_RE = re.compile(
    r"\b(cai|caiu|caem|caiam)\b\s+(em|na|no|nas|nos)\s+(prova|exame|simulado|quest[aã]o)",
    re.IGNORECASE,
)
# Bloco de prova explicito (P1, P2, P3) usado como referencia
VOCAB_PROVA_BLOCO_RE = re.compile(r"\b(P1|P2|P3)\b(?=[\s,.;:—\-])")

# ============================================================
# Path do template canonico
# ============================================================

TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "typst-template" / "nebli_v2_apostila.typ"
TEMPLATE_MIN_BYTES = 15000

# Mapa de Confusoes (canonico 2026-05-18): exigido pelo QUESTIONADOR antes da E2.
MAPA_CONFUSOES_DIR = Path(__file__).resolve().parent.parent / "mapa-confusoes"

TEMPLATE_HELPERS = [
    "pagina-padrao", "set-etapa", "etapa-header", "parte-title", "subtopico",
    "intro-box", "atencao-box", "confusao-prevista", "clinica-box", "sintese-box",
    "mini-resumo", "conclusao-box",
    "figura-nebli",
    "figura-lateral",
    "mapa-parte",
    "badge-consolidacao", "badge-integracao", "badge-aplicacao", "badge-prioritario",
    "questao-mc", "questao-ce", "discursiva",
    "prova-mc", "prova-ce", "prova-discursiva", "prova-block",
    "neblicard", "cloze",
    "termo-nota", "sigla",
    "glossario-siglas-page",
    "capa", "sumario", "gabarito-bloco", "gabarito-page", "resumindo-page",
    "pre-aula-page",
]

# ============================================================
# Configuracao por arquivo
# ============================================================

EXPECTATIONS = {
    # "Antes da aula" (canonico 2026-08-28) -- secao de abertura entre capa e
    # sumario. GATE HARD desde 2026-08-29 (pedido de Davi): todo resumo novo
    # PRECISA do arquivo, e ele passa por `check_pre_aula` (2 paginas, prosa
    # continua, sem figura, sem pergunta, termos plantados em negrito). Para
    # REGERAR um resumo historico que nasceu sem a secao, use `--legado`.
    "pre-aula.typ": {
        "needs": [(r"#pre-aula-page\b", 1, ">=1", "pre-aula-page")],
    },
    "etapa1.typ": {
        "needs": [
            (r"#intro-box\b",     1, ">=1", "intro-box"),
            # conclusao-box VOLTA a ser gate (canonico 2026-07-03): a E1 fecha
            # sempre na conclusao integradora (4 camadas). Reverte a suspensao
            # de 2026-07-01 que a tornara opcional.
            (r"#conclusao-box\b", 1, ">=1", "conclusao-box"),
            (r"#sigla\b",         1, ">=1", "siglas"),
        ],
    },
    "etapa2.typ": {
        "needs": [(r"#questao(?:-mc|-ce)?\(", 30, "=30", "questoes MC/CE")],
        "exact": True,
    },
    "etapa3.typ": {
        "needs": [(r"#discursiva\b", 5, "=5", "discursivas")],
        "exact": True,
    },
    # E4 removida do pipeline canonico em 2026-05-22 (banco vira calibracao).
    # etapa4.typ nao e mais validada nem exigida; arquivo leftover de resumos
    # antigos no diretorio e ignorado.
    "resumindo.typ": {
        "needs": [
            (r"(#let\s+secoes-resumindo|#resumindo-page)\b", 1, ">=1",
             "secoes-resumindo OU resumindo-page"),
        ],
    },
}

# Todo arquivo .typ deve terminar em fechamento limpo. A regra antiga aplicava
# so a etapa1; agora aplica a TODOS (canonico 2026-05-15 -- detectar
# truncamento da ultima linha que nao deixa NULL nem bracket extra).
GLOBAL_END_CHARS = {"]", ")", "}"}

# ============================================================
# Validacoes basicas
# ============================================================

def check_null_bytes(path, fname):
    try:
        raw = path.read_bytes()
    except OSError as e:
        return [f"  x {fname}: erro lendo bytes -- {e}"]
    if b"\x00" in raw:
        n = raw.count(b"\x00")
        return [f"  x {fname}: contem {n} NULL byte(s) -- provavel TRUNCAMENTO de Write/Edit"]
    return []


def check_brackets(content, fname):
    """Brackets balanceados. Ignora strings, comentarios e padroes
    conhecidos de markup (rotulos `*#letra)*` em pad/block)."""
    content_clean = re.sub(r"//[^\n]*", "", content)
    content_clean = re.sub(r"/\*.*?\*/", "", content_clean, flags=re.DOTALL)
    content_clean = re.sub(r'"(?:[^"\\]|\\.)*"', '""', content_clean)
    content_clean = re.sub(r"\*#\w+\)\*", "**", content_clean)

    counts = {"(": 0, "[": 0, "{": 0}
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in content_clean:
        if ch in counts:
            counts[ch] += 1
        elif ch in pairs:
            counts[pairs[ch]] -= 1

    errors = []
    for open_ch, n in counts.items():
        close_ch = {"(": ")", "[": "]", "{": "}"}[open_ch]
        if n > 0:
            errors.append(f"  x {fname}: {n} `{open_ch}` sem `{close_ch}` correspondente -- provavel TRUNCAMENTO")
        elif n < 0:
            errors.append(f"  x {fname}: {-n} `{close_ch}` extras -- provavel erro de digitacao")
    return errors


def check_structure(content, fname, spec):
    errors = []
    exact = spec.get("exact", False)
    for pattern, expected, label, name in spec["needs"]:
        found = len(re.findall(pattern, content))
        if exact and found != expected:
            errors.append(f"  x {fname}: encontrou {found} {name}, esperado {label}")
        elif not exact and found < expected:
            errors.append(f"  x {fname}: encontrou {found} {name}, esperado {label}")
    return errors


# ============================================================
# Checks v3 (2026-05-16, frente B4 do plano de economia)
# ============================================================

def check_acentuacao(content, fname):
    """Conta letras acentuadas em texto Typst. PT-BR normal tem
    >= 1.5% de acentos. < 0.5% = bug catastrofico (#6 Acidos Nucleicos)."""
    # Remove import lines, comentarios, helpers (so quer letras de prosa)
    text = re.sub(r"^#import .*$", "", content, flags=re.MULTILINE)
    text = re.sub(r"//[^\n]*", "", text)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    text = re.sub(r'"[^"\n]*"', "", text)  # strings (paths, sigla abbr)
    letras = [c for c in text if c.isalpha()]
    n = len(letras)
    if n < 500:
        return [], []  # amostra pequena (resumindo.typ pode ser curto)
    n_acentos = sum(1 for c in letras if c in ACENTOS_SET)
    pct = n_acentos / n
    if pct < LIMIAR_ACENTOS_ERRO:
        return ([f"  x {fname}: {n_acentos}/{n} letras acentuadas = {pct*100:.2f}% "
                 f"(piso {LIMIAR_ACENTOS_ERRO*100:.1f}%). Texto PT-BR sem acento -- "
                 f"BLOQUEAR (cenario #6 Acidos Nucleicos)."], [])
    if pct < LIMIAR_ACENTOS_WARN:
        return ([], [f"  ! {fname}: acentuacao baixa ({pct*100:.2f}%). "
                     f"Esperado >= {LIMIAR_ACENTOS_WARN*100:.1f}% em PT-BR. Conferir."])
    return [], []


def check_markdown_leakage(content, fname):
    """Detecta `**bold**` (markdown) em texto Typst. Typst usa `*bold*`."""
    matches = MARKDOWN_BOLD_RE.findall(content)
    if not matches:
        return [], []
    amostra = matches[:3]
    return ([], [f"  ! {fname}: {len(matches)} `**bold**` (markdown) detectado(s). "
                 f"Typst usa `*bold*`. Exemplos: {amostra}"])


def check_vocab_prova(content, fname):
    """Detecta vocabulario de prova em etapa1.typ / resumindo.typ.
    Canonico 2026-05-22 (regra 10 do redator-e1.md, frente 2.1):
    banco eh calibracao invisivel; leitor jamais sabe que existe banco.

    Aplicado SO em etapa1.typ e resumindo.typ -- a E2 e E3 podem
    legitimamente usar 'questao' (sao questoes, ora), e o `discursiva`
    no JSON do gabarito tambem nao deve disparar."""
    if fname not in ("etapa1.typ", "resumindo.typ"):
        return [], []
    # Remove comentarios para nao disparar em meta-notas dos redatores.
    text = re.sub(r"//[^\n]*", "", content)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)

    achados = []

    # Padrao 1: vocabulario direto
    for m in VOCAB_PROVA_RE.finditer(text):
        # contexto: 30 chars antes/depois
        start = max(0, m.start() - 30)
        end = min(len(text), m.end() + 30)
        contexto = text[start:end].replace("\n", " ").strip()
        achados.append((m.group(0).lower(), contexto))

    # Padrao 2: "cai/caiu em prova"
    for m in VOCAB_PROVA_CAI_RE.finditer(text):
        start = max(0, m.start() - 30)
        end = min(len(text), m.end() + 30)
        contexto = text[start:end].replace("\n", " ").strip()
        achados.append((m.group(0).lower(), contexto))

    # Padrao 3: P1/P2/P3 em contexto de bloco de prova
    for m in VOCAB_PROVA_BLOCO_RE.finditer(text):
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + 40)
        contexto = text[start:end].replace("\n", " ").strip()
        # so dispara se "prova" ou "bloco" aparece no contexto
        if re.search(r"\b(prova|bloco|exame|simulado|p[12]?3?)\b", contexto, re.IGNORECASE):
            achados.append((m.group(0), contexto))

    if not achados:
        return [], []

    # Quebra identidade do produto -- ERROR, nao warning.
    msgs = [f"  x {fname}: vocabulario de PROVA detectado "
            f"({len(achados)} ocorrencia(s)) -- regra 10 do redator-e1.md: "
            f"banco eh calibracao invisivel, leitor jamais sabe que existe banco. "
            f"Reescrever em voz de mecanismo:"]
    for palavra, ctx in achados[:6]:
        ctx_trunc = ctx[:90] + ("..." if len(ctx) > 90 else "")
        msgs.append(f"      `{palavra}` em: ...{ctx_trunc}...")
    if len(achados) > 6:
        msgs.append(f"      ... e mais {len(achados)-6} ocorrencia(s)")
    return msgs, []


def check_math_mode_quimica(content, fname):
    """Detecta `$...$` com identificadores quimicos multi-letra (Ka, CO2...).
    Typst trata como variavel indefinida em math mode."""
    erros_questoes = []
    for m in MATH_QUIMICA_RE.finditer(content):
        bloco = m.group(0)
        gat = MATH_QUIMICA_TRIGGERS.search(bloco)
        if gat:
            erros_questoes.append((bloco[:50], gat.group(0)))
    if not erros_questoes:
        return [], []
    amostra = erros_questoes[:3]
    return ([], [f"  ! {fname}: {len(erros_questoes)} equacao(s) quimica(s) em math mode `$...$` "
                 f"-- usar `#align(center, text(...))` + Unicode. Triggers: "
                 f"{', '.join(g for _, g in amostra)}"])


def check_helpers_duplicados(content, fname, helpers_list):
    """Cada helper canonico deve aparecer com `#let NOME (` exatamente 1x.
    Mais de 1 = bug (caso real do `resumindo-page` duplicado no template
    descoberto durante o #6)."""
    erros = []
    for helper in helpers_list:
        h_esc = re.escape(helper)
        pattern = rf"#let\s+{h_esc}\s*(?:\(|=)"
        matches = re.findall(pattern, content)
        if len(matches) > 1:
            erros.append(f"  x {fname}: helper `#let {helper}` aparece {len(matches)}x "
                         f"-- DUPLICATA. Apagar a copia obsoleta.")
    return erros, []


# ----- NOVA regra de truncamento da ultima linha (canonico 2026-05-15) -----

def check_clean_ending(content, fname):
    """Detecta truncamento que deixa a ultima linha cortada no meio de uma
    palavra OU sem o fechamento canonico. Pega o caso 'empurr' (sem 'a')
    que NULL-byte-check nao pega, mas que quebra a compilacao."""
    lines = [ln.rstrip() for ln in content.splitlines() if ln.strip()]
    if len(lines) < 2:
        return [f"  x {fname}: arquivo com menos de 2 linhas nao-vazias -- corrompido ou vazio"]
    last = lines[-1].rstrip()
    if not last:
        return [f"  x {fname}: ultima linha nao-vazia esta vazia apos trim -- corrompido"]
    last_char = last[-1]
    # Fechamento canonico: parentese / bracket / chave fecha
    if last_char in GLOBAL_END_CHARS:
        return []
    # Aceita tambem fim em "//", "*/" para comentarios e em virgula/pontuacao
    # com palavra completa antes (caso de linha de import ou let de uma
    # linha so).
    if last.endswith(("*/", "//")):
        return []
    # Caso aceitavel: ultima linha termina em palavra alfanumerica completa
    # (>=2 chars antes do final, sem corte no meio). Mas se nao terminou em
    # bracket de fechamento, e suspeito -- e WARNING, nao erro.
    if re.search(r"\w{2,}$", last):
        return [f"  ! {fname}: ultima linha termina em palavra (`...{last[-20:]}`) -- "
                f"esperado `]`, `)` ou `}}`. Conferir se nao truncou"]
    # Caso ruim: terminou em char solto ou pedaco de palavra
    return [f"  x {fname}: ultima linha termina em `{last[-20:]}` -- "
            f"provavel TRUNCAMENTO no meio da linha. Conferir antes de compilar"]


# ============================================================
# TAIL VISUAL -- passo (f) (2026-05-18, propostas-pos-g20 1.5)
# ============================================================

def print_tail(path, fname, n=3):
    """Imprime as ultimas n linhas nao-vazias do arquivo, com
    marcador `|`. Pega o caso de truncamento no MEIO do .typ que
    deixa o fim aparentemente sao -- check_clean_ending so olha o
    ultimo char, este passo joga as 3 linhas para o humano julgar
    rapidamente se o fechamento parece canonico.
    Nao gera erro nem warning -- so log informacional."""
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return
    lines = [ln.rstrip() for ln in content.splitlines() if ln.strip()]
    if not lines:
        return
    ultimas = lines[-n:]
    print(f"  tail -{n}:")
    for ln in ultimas:
        # trunca em 70 chars para nao poluir o log com linhas longas
        mostra = ln if len(ln) <= 70 else ln[:67] + "..."
        print(f"    | {mostra}")


# ============================================================
# AUDITORIA DE PARIDADE MC (modulo novo 2026-05-15)
# ============================================================

WORD_RE = re.compile(r"\w+", re.UNICODE)

def count_words(text):
    """Conta palavras em texto Typst, ignorando markup simples."""
    # Remove chamadas inline tipo #sigla("X", [...]) -- pega so o conteudo legivel
    clean = re.sub(r"#\w+(?:\([^)]*\))?", " ", text)
    # Remove bracketed labels remanescentes
    clean = re.sub(r"[\[\]\*_]+", " ", clean)
    return len(WORD_RE.findall(clean))


def parse_questao_mc(content):
    """Extrai (numero, {A: texto, B: ..., E: ...}) para cada #questao-mc.
    Estrategia robusta: localiza cada `#questao-mc(`, encontra o `)` que
    fecha o call por contagem de parenteses, depois busca dentro do bloco
    as tuplas (`"A", [...]`) por busca de bracket aninhado."""
    out = []
    i = 0
    pattern = "#questao-mc("
    while True:
        idx = content.find(pattern, i)
        if idx == -1:
            break
        # Avanca contando parenteses para achar o ) que fecha a chamada
        depth = 0
        j = idx + len(pattern) - 1  # posiciona no "("
        in_string = False
        in_bracket = 0  # nivel de [...] (content blocks do Typst)
        while j < len(content):
            ch = content[j]
            if ch == '"' and (j == 0 or content[j-1] != "\\"):
                in_string = not in_string
            elif not in_string:
                if ch == "[":
                    in_bracket += 1
                elif ch == "]":
                    in_bracket -= 1
                elif ch == "(" and in_bracket == 0:
                    depth += 1
                elif ch == ")" and in_bracket == 0:
                    depth -= 1
                    if depth == 0:
                        break
            j += 1
        if j >= len(content):
            break
        body = content[idx+len(pattern):j]
        # Numero da questao: primeiro argumento, string entre aspas
        m_num = re.match(r'\s*"([^"]+)"\s*,', body)
        if not m_num:
            i = j + 1
            continue
        numero = m_num.group(1)
        # Alternativas: tuplas (`"LETRA", [...]`) com letra em A-E
        alts = {}
        for m in re.finditer(r'\(\s*"([A-E])"\s*,\s*\[', body):
            letra = m.group(1)
            start = m.end()  # posicao logo depois de '['
            depth_b = 1
            k = start
            while k < len(body) and depth_b > 0:
                if body[k] == "[":
                    depth_b += 1
                elif body[k] == "]":
                    depth_b -= 1
                k += 1
            if depth_b == 0:
                texto = body[start:k-1]
                alts[letra] = texto
        if len(alts) >= 4:
            out.append((numero, alts))
        i = j + 1
    return out


GABARITO_PAT = re.compile(r'\(\s*"(\d+)"\s*,\s*"([A-EICE\[\],\s]+)"\s*\)')

def parse_gabarito(main_content):
    """Extrai {numero (sem zeros): letra} para questoes MC do gabarito-page
    em main.typ. Pula entradas C/E (multiplos chars)."""
    out = {}
    for num, ans in GABARITO_PAT.findall(main_content):
        ans = ans.strip()
        # Aceita so resposta unica A-E (MC); ignora C/E "CCEE"
        if len(ans) == 1 and ans in "ABCDE":
            num_clean = num.lstrip("0") or "0"
            out[num_clean] = ans
    return out


def audit_paridade(etapa2_path, main_path):
    """Roda auditoria de paridade MC. Retorna (errors, warnings).
    Paridade fora da faixa e WARNING; >=4 questoes fora vira ERRO."""
    if not etapa2_path.exists() or not main_path.exists():
        return [], []
    e2 = etapa2_path.read_text(encoding="utf-8")
    mn = main_path.read_text(encoding="utf-8")
    questoes = parse_questao_mc(e2)
    gabarito = parse_gabarito(mn)
    if not questoes or not gabarito:
        return [], [f"  ! paridade-mc: parse vazio (questoes={len(questoes)}, "
                    f"gabarito-mc={len(gabarito)}) -- pulando auditoria"]

    warnings = []
    ratios = []
    fora_faixa = []
    sem_gabarito = []

    for numero, alts in questoes:
        num_clean = numero.lstrip("0") or "0"
        correta = gabarito.get(num_clean) or gabarito.get(numero)
        if not correta or correta not in alts:
            sem_gabarito.append(numero)
            continue
        wc = count_words(alts[correta])
        distratoras = [count_words(t) for L, t in alts.items() if L != correta]
        if not distratoras:
            continue
        distratoras_sorted = sorted(distratoras)
        mediana = distratoras_sorted[len(distratoras_sorted) // 2]
        if mediana == 0:
            continue
        ratio = wc / mediana
        ratios.append((numero, correta, wc, mediana, ratio))
        if ratio < 0.80 or ratio > 1.30:
            fora_faixa.append((numero, correta, wc, mediana, ratio))

    n_total = len(ratios)
    if not n_total:
        return [], [f"  ! paridade-mc: nenhuma MC casada com gabarito -- pulando"]

    media = sum(r[4] for r in ratios) / n_total
    max_ratio = max(r[4] for r in ratios)
    n_fora = len(fora_faixa)

    print(f"  paridade-mc: {n_total} questoes auditadas, "
          f"media ratio {media:.2f}, max {max_ratio:.2f}, "
          f"fora da faixa 0.80-1.30: {n_fora}")

    errors_out = []
    if n_fora >= 4:
        errors_out.append(f"  x paridade-mc: {n_fora} MC fora da faixa 0.80-1.30 -- "
                          f"violacao SISTEMICA. AJUSTAR DISTRATORAS para caber em "
                          f"80-120% da correta (canonico 2026-05-18: nunca encurtar "
                          f"a correta -- ela carrega o mecanismo didatico):")
        for num, corr, wc, med, r in fora_faixa[:10]:
            errors_out.append(f"      Q{num}: correta={corr}, "
                              f"{wc} palavras vs mediana {med} (ratio {r:.2f})")
        if len(fora_faixa) > 10:
            errors_out.append(f"      ... e mais {len(fora_faixa)-10} questoes")
    elif n_fora > 0:
        warnings.append(f"  ! paridade-mc: {n_fora} MC fora da faixa 0.80-1.30:")
        for num, corr, wc, med, r in fora_faixa:
            warnings.append(f"      Q{num}: correta={corr}, "
                            f"{wc} palavras vs mediana {med} (ratio {r:.2f})")

    if sem_gabarito:
        warnings.append(f"  ! paridade-mc: {len(sem_gabarito)} MC sem gabarito casado "
                        f"({', '.join(sem_gabarito[:5])}{'...' if len(sem_gabarito) > 5 else ''})")

    return errors_out, warnings


# ============================================================
# AUDITORIA DAS 4 REGRAS CANONICAS DA E2 (canonico 2026-05-22)
# Redesenho de 2026-05-18 documentado em .claude/agents/questionador.md:
#   (a) ordem invertida -- correta nao sistematicamente em A
#   (b) paridade intra-questao -- correta <= 1.25x MAIOR distratora
#   (c) Mapa de Confusoes -- arquivo + >=4 confusoes por subtopico
#   (d) sorteio do gabarito -- distribuicao A-E nao-monotonica
# ============================================================

def infer_slug(cwd):
    """Tenta inferir slug do diretorio de trabalho.
    Pipeline paralelo grava em `typst-build/_par_<slug>/`; pipeline serial
    usa `typst-build/` raiz e o slug precisa ser fornecido via --slug.
    Retorna None se nao for inferivel."""
    name = cwd.name
    if name.startswith("_par_"):
        return name[len("_par_"):]
    return None


# Aceita qualquer cabecalho `## algo` -- inclui formatos historicos
# `## X.Y — subtopico` (glicolise.md) e `## PARTE I — titulo` (gliconeogenese.md).
SUBTOPICO_RE = re.compile(r"^##\s+\S.*$", re.MULTILINE)
CONFUSAO_ITEM_RE = re.compile(r"^\s{0,3}\d+\.\s+\*\*", re.MULTILINE)


def check_mapa_confusoes(slug):
    """Valida existencia + estrutura minima de mapa-confusoes/<slug>.md.
    Regra (c) do redesenho da E2 (2026-05-18): >=4 confusoes por
    subtopico `## X.Y`. Sem slug, emite warning."""
    if slug is None:
        return [], [f"  ! mapa-confusoes: slug nao inferido do CWD `{Path.cwd().name}` -- "
                    f"passe --slug NOME para validar o mapa, ou rode do diretorio "
                    f"`typst-build/_par_<slug>/`."]
    path = MAPA_CONFUSOES_DIR / f"{slug}.md"
    if not path.exists():
        return ([f"  x mapa-confusoes/{slug}.md AUSENTE -- QUESTIONADOR exige o mapa "
                 f"antes da E2 (canonico 2026-05-18). Construir 4 confusoes por subtopico "
                 f"antes de gerar `etapa2.typ`."], [])
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as e:
        return [f"  x mapa-confusoes/{slug}.md: erro lendo arquivo -- {e}"], []

    # Quebra por subtopico `## N.M ...`
    pos_subt = [m.start() for m in SUBTOPICO_RE.finditer(content)]
    if not pos_subt:
        return [f"  x mapa-confusoes/{slug}.md: nenhum subtopico `## X.Y` encontrado -- formato fora do canonico"], []
    # Anexa fim do arquivo para fechar o ultimo bloco
    pos_subt.append(len(content))
    erros = []
    warnings = []
    subt_count = 0
    for i in range(len(pos_subt) - 1):
        bloco = content[pos_subt[i]:pos_subt[i+1]]
        titulo = bloco.splitlines()[0].strip()
        # Corta titulo grande pra log
        titulo_log = titulo[:60] + ("..." if len(titulo) > 60 else "")
        n_itens = len(CONFUSAO_ITEM_RE.findall(bloco))
        subt_count += 1
        if n_itens < 4:
            erros.append(f"  x mapa-confusoes/{slug}.md: subtopico `{titulo_log}` tem "
                         f"{n_itens} confusao(es) (regra: >=4 por subtopico).")
    if subt_count < 2:
        warnings.append(f"  ! mapa-confusoes/{slug}.md: apenas {subt_count} subtopico(s) `## X.Y` -- "
                        f"E1 tipicamente tem >=6 subtopicos (3 PARTES x 2-3). Conferir cobertura.")
    return erros, warnings


def audit_e2_regras_extra(questoes, gabarito):
    """Roda 3 dos 4 checks da E2 (o de Mapa de Confusoes esta em
    check_mapa_confusoes). Reaproveita o parser ja usado por audit_paridade.

       (a) ordem invertida -- proxy: %A no gabarito
       (b) paridade intra-questao -- correta vs MAIOR distratora
       (d) distribuicao A-E nao-monotonica + sequencias

    Retorna (errors, warnings).
    """
    errors = []
    warnings = []

    # ---- (b) Paridade intra-questao (correta entre 0.80 e 1.25 x maior distratora) ----
    fora = []
    for numero, alts in questoes:
        num_clean = numero.lstrip("0") or "0"
        correta = gabarito.get(num_clean) or gabarito.get(numero)
        if not correta or correta not in alts:
            continue
        wc = count_words(alts[correta])
        distratoras = [count_words(t) for L, t in alts.items() if L != correta]
        if not distratoras:
            continue
        maior = max(distratoras)
        if maior == 0:
            continue
        ratio = wc / maior
        if ratio > 1.25 or ratio < 0.80:
            direcao = "longa" if ratio > 1.25 else "curta"
            fora.append((numero, correta, wc, maior, ratio, direcao))
    if fora:
        bloco = [(f"  {'x' if len(fora) >= 4 else '!'} paridade-intra-questao: "
                  f"{len(fora)} MC fora da banda 0.80-1.25 vs maior distratora "
                  f"(canonico 2026-05-29: banda dupla -- correta nem curta nem longa demais. "
                  f"Se correta curta: enriquecer correta com mecanismo, nao inchar distratora. "
                  f"Se correta longa: enriquecer distratoras, nao encurtar correta):")]
        for num, corr, wc, mx, r, direcao in fora[:8]:
            bloco.append(f"      Q{num}: correta={corr} {direcao} demais "
                         f"({wc} palavras vs maior distratora {mx}, ratio {r:.2f})")
        if len(fora) > 8:
            bloco.append(f"      ... e mais {len(fora)-8} questao(oes)")
        if len(fora) >= 4:
            errors.extend(bloco)
        else:
            warnings.extend(bloco)

    # ---- (a) + (d) Distribuicao A-E do gabarito ----
    if gabarito:
        from collections import Counter
        contagem = Counter(gabarito.values())
        total = sum(contagem.values())
        print(f"  gabarito-distribuicao: {dict(sorted(contagem.items()))} "
              f"(total MC com gabarito casado: {total})")

        # (d) Letra dominante
        letra_top, n_top = contagem.most_common(1)[0]
        pct_top = n_top / total
        if pct_top >= 0.50:
            errors.append(f"  x gabarito-sorteio: letra `{letra_top}` domina {n_top}/{total} = "
                          f"{pct_top*100:.0f}% das questoes -- sorteio AUSENTE (guarda 2026-06-24: "
                          f"nenhuma letra acima de ~40%). Reposicionar corretas.")
        elif pct_top >= 0.40:
            warnings.append(f"  ! gabarito-sorteio: letra `{letra_top}` em {n_top}/{total} = "
                            f"{pct_top*100:.0f}% das questoes -- no limiar de ~40%. Reposicionar algumas.")

        # (d) Sequencia monotonica em ordem numerica das questoes
        ordenadas = sorted(gabarito.items(), key=lambda kv: int(kv[0]))
        seq = [v for _, v in ordenadas]
        run = 1
        max_run = 1
        max_letra = seq[0] if seq else ""
        for i in range(1, len(seq)):
            if seq[i] == seq[i-1]:
                run += 1
                if run > max_run:
                    max_run = run
                    max_letra = seq[i]
            else:
                run = 1
        if max_run >= 5:
            errors.append(f"  x gabarito-sequencia: {max_run} `{max_letra}` consecutivas -- "
                          f"corrida degenerada (guarda 2026-06-24: 4+ ja reposiciona). Conferir.")
        elif max_run >= 4:
            warnings.append(f"  ! gabarito-sequencia: {max_run} `{max_letra}` consecutivas -- "
                            f"3 iguais e aceitavel, 4 ja reposiciona a correta entre alternativas.")

        # (a) Ordem invertida -- proxy: %A no gabarito
        n_A = contagem.get("A", 0)
        if total >= 5:
            pct_A = n_A / total
            if pct_A >= 0.60:
                errors.append(f"  x ordem-invertida: correta em A {n_A}/{total} = {pct_A*100:.0f}% "
                              f"-- sugere correta redigida PRIMEIRO. Regra canonica 2026-05-18: "
                              f"distratoras vem antes, correta por ultimo + sorteio do sinal.")
            elif pct_A >= 0.40:
                warnings.append(f"  ! ordem-invertida: correta em A em {n_A}/{total} = {pct_A*100:.0f}% "
                                f"-- acima da media esperada (~20% por letra). Conferir sorteio.")

    return errors, warnings


# ============================================================
# Validacao do template canonico
# ============================================================

def check_pre_aula(content, fname):
    """Gate HARD da secao "Antes da aula" (canonico 2026-08-28, endurecido 2026-08-29).

    Ate agora `pre-aula.typ` era auditado apenas SE existisse -- na pratica,
    opcional. Davi canonizou como gate hard: todo resumo abre com a leitura de
    vespera. O que se verifica aqui e o que a regra promete:

      - **2 paginas de prosa** -> 800-1300 palavras (alvo 900-1100, fora disso avisa).
      - **prosa fluida contínua** -> sem bullet/lista, sem caixa, sem helper de E1.
      - **sem figura** -> as figuras todas ficam na E1 (canonico).
      - **sem pergunta retorica** -> mesmo banimento da E1 (canonico 2026-05-29).
      - **os topicos/termos mais importantes plantados** -> negrito e o marcador
        do termo sendo plantado; a cota de 2-3 por paragrafo da E1 NAO vale aqui,
        e um pre-aula que planta menos de 15 termos nao esta cumprindo a funcao.

    A presenca do arquivo em si e cobrada no `main()`, nao aqui.
    """
    errors, warnings = [], []

    # --- 2 paginas: contagem de palavras ---
    limpo = re.sub(r"#[\w-]+", "", content)
    palavras = [w for w in re.split(r"\s+", limpo) if any(c.isalpha() for c in w)]
    n = len(palavras)
    if n < 800 or n > 1300:
        errors.append(f"  x {fname}: {n} palavras -- fora de 800-1300, nao fecha as 2 paginas "
                      f"canonicas (alvo 900-1100). Ver CLAUDE.md § \"Antes da aula\".")
    elif n < 900 or n > 1100:
        warnings.append(f"  ! {fname}: {n} palavras -- fora do alvo 900-1100 (ainda dentro do "
                        f"aceitavel de 2 paginas).")
    else:
        print(f"  palavras pre-aula: {n} (alvo 900-1100)")

    # --- prosa continua: sem bullet, sem lista ---
    bullets = re.findall(r"^[ \t]*[-+][ \t]+\S", content, re.MULTILINE)
    if bullets or "#list(" in content:
        errors.append(f"  x {fname}: {len(bullets)} bullet(s)/lista detectada(s) -- a secao e "
                      f"PROSA CONTINUA. Termo importante entra em negrito dentro da frase, "
                      f"nunca como item de lista.")

    # --- sem figura ---
    figuras = [h for h in ("#figura-nebli", "#figura-lateral", "image(") if h in content]
    if figuras:
        errors.append(f"  x {fname}: figura detectada ({', '.join(figuras)}) -- a secao "
                      f"\"Antes da aula\" nao leva figura; as figuras todas ficam na E1.")

    # --- sem helper de E1 (a secao nao e mini-E1) ---
    proibidos = ("#parte-title", "#subtopico", "#intro-box", "#mini-resumo", "#atencao-box",
                 "#clinica-box", "#confusao-prevista", "#sintese-box", "#conclusao-box",
                 "#etapa-header", "#set-etapa")
    achados = [h for h in proibidos if h in content]
    if achados:
        errors.append(f"  x {fname}: helper de E1 dentro do pre-aula ({', '.join(achados)}) -- "
                      f"a secao e narrativa continua, nao mini-E1 nem sumario executivo.")

    # --- sem pergunta retorica (mesmo banimento da E1) ---
    n_perg = content.count("?")
    if n_perg:
        errors.append(f"  x {fname}: {n_perg} interrogacao(oes) -- pergunta ancora/retorica e "
                      f"banida (canonico 2026-05-29). Abertura e afirmacao direta.")

    # --- termos plantados em negrito ---
    negritos = re.findall(r"\*[^*\n]{2,60}\*", content)
    if len(negritos) < 15:
        errors.append(f"  x {fname}: apenas {len(negritos)} termo(s) em negrito -- a funcao dupla "
                      f"da secao e contar a aula E plantar os termos que o professor vai usar "
                      f"como se o aluno ja soubesse. Piso 15; 4-5 por paragrafo e normal aqui.")
    elif len(negritos) < 25:
        warnings.append(f"  ! {fname}: {len(negritos)} termos em negrito -- baixo para 2 paginas; "
                        f"conferir se os principais termos da aula foram plantados.")
    else:
        print(f"  termos plantados: {len(negritos)} em negrito")

    return errors, warnings


def check_template_helpers(content, fname):
    errors = []
    for helper in TEMPLATE_HELPERS:
        h_esc = re.escape(helper)
        pattern = rf"#let\s+{h_esc}\s*(\(|=)"
        if not re.search(pattern, content):
            errors.append(f"  x {fname}: helper canonico `#let {helper}` AUSENTE -- provavel TRUNCAMENTO ou regressao")
    return errors


def check_template_size(path, fname):
    size = path.stat().st_size
    if size < TEMPLATE_MIN_BYTES:
        return [f"  x {fname}: tamanho {size} bytes < piso {TEMPLATE_MIN_BYTES} -- quase certo TRUNCAMENTO catastrofico"]
    return []


def check_template_clean_ending(content, fname):
    lines = [ln for ln in content.splitlines() if ln.strip()]
    if len(lines) < 3:
        return [f"  x {fname}: arquivo com menos de 3 linhas nao-vazias -- corrompido"]
    last = lines[-1].strip()
    if last not in ("}", ")"):
        return [f"  ! {fname}: ultima linha nao-vazia e `{last[:60]}` -- esperado `}}` (fechamento)"]
    return []


def check_template(path):
    fname = path.name
    if not path.exists():
        return [f"  x {fname}: TEMPLATE CANONICO nao encontrado em {path}"], []
    errors = []
    warnings = []
    errors.extend(check_null_bytes(path, fname))
    if errors:
        return errors, warnings
    errors.extend(check_template_size(path, fname))
    content = path.read_text(encoding="utf-8")
    if not content.strip():
        return [f"  x {fname}: arquivo vazio"], []

    # Para o template, ending-check primeiro
    ending_msgs = check_template_clean_ending(content, fname)
    ending_clean = True
    for msg in ending_msgs:
        if msg.lstrip().startswith("x"):
            errors.append(msg)
            ending_clean = False
        else:
            warnings.append(msg)

    # Bracket-counter degrada pra warning se ending OK + size OK + helpers OK.
    # Template tem muitos parenteses em comentarios longos -- falso-positivo
    # cronico do regex de limpeza.
    bracket_msgs = check_brackets(content, fname)
    helpers_msgs = check_template_helpers(content, fname)
    template_healthy = ending_clean and not helpers_msgs and not any(
        "TRUNCAMENTO catastrofico" in e for e in errors
    )
    for msg in bracket_msgs:
        if template_healthy:
            warnings.append("  !" + msg[3:] + " [degradado: ending+helpers+size OK]")
        else:
            errors.append(msg)
    errors.extend(helpers_msgs)

    # v3 check (2026-05-16, frente B4): helpers duplicados no template.
    dup_errors, dup_warnings = check_helpers_duplicados(content, fname, TEMPLATE_HELPERS)
    errors.extend(dup_errors); warnings.extend(dup_warnings)

    return errors, warnings


# ============================================================
# Validacao de arquivos etapa / resumindo
# ============================================================

CE_CALL_RE = re.compile(r"#questao-ce\(", re.MULTILINE)
CE_ITEM_RE = re.compile(r'\(\s*"(?:I{1,3}|IV|V|VI)"\s*,\s*\[')


def check_ce_quatro_itens(content, fname):
    """Cada #questao-ce deve ter EXATAMENTE 4 itens (canonico 2026-07-01).
    Conta os marcadores de item ("I"..."IV") entre uma chamada e a proxima
    fronteira #questao..."""
    erros = []
    starts = [m.start() for m in CE_CALL_RE.finditer(content)]
    if not starts:
        return erros
    # Fronteiras: proxima chamada de #questao-mc OU #questao-ce, ou fim.
    todas = sorted(m.start() for m in re.finditer(r"#questao-(?:mc|ce)\(", content))
    for s in starts:
        # acha a proxima fronteira depois de s
        fim = len(content)
        for t in todas:
            if t > s:
                fim = t
                break
        bloco = content[s:fim]
        # numero da questao para log
        mnum = re.search(r'#questao-ce\(\s*"([^"]+)"', bloco)
        qid = mnum.group(1) if mnum else "??"
        n = len(CE_ITEM_RE.findall(bloco))
        if n != 4:
            erros.append(f"  x {fname}: questao-ce Q{qid} tem {n} item(ns) -- "
                         f"regra canonica: C/E SEMPRE 4 itens (I-IV).")
    return erros


def check_file(path):
    fname = path.name
    if not path.exists():
        return [f"  x {fname}: arquivo nao encontrado"], []
    null_errors = check_null_bytes(path, fname)
    if null_errors:
        return null_errors, []
    content = path.read_text(encoding="utf-8")
    if not content.strip():
        return [f"  x {fname}: arquivo vazio"], []
    spec = EXPECTATIONS.get(fname)
    errors = []
    warnings = []

    # Truncamento de ultima linha e sinal MAIS FORTE de problema real.
    # Roda primeiro -- se passa, bracket-counter pode ser falso-positivo
    # (literais "(a)", "[X]_Y" em prosa).
    ending = check_clean_ending(content, fname)
    ending_clean = True
    for msg in ending:
        if msg.lstrip().startswith("x"):
            errors.append(msg)
            ending_clean = False
        else:
            warnings.append(msg)

    # Bracket-counter: se NULL+ending estao limpos, degrada pra warning
    # (evita falso-positivo de "(a)" literal em E4, "[Na+]_LEC" em prosa,
    # parenteses em comentarios longos do template).
    bracket_msgs = check_brackets(content, fname)
    for msg in bracket_msgs:
        if ending_clean:
            # Reescreve como warning ("!" em vez de "x")
            warnings.append("  !" + msg[3:] + " [degradado: ending OK, provavel literal em conteudo]")
        else:
            errors.append(msg)

    if spec:
        errors.extend(check_structure(content, fname, spec))
    else:
        warnings.append(f"  ! {fname}: sem regras especificas (passou so brackets/NULL/ending)")

    # v3 checks (2026-05-16, frente B4)
    e_ac, w_ac = check_acentuacao(content, fname)
    errors.extend(e_ac); warnings.extend(w_ac)
    e_md, w_md = check_markdown_leakage(content, fname)
    errors.extend(e_md); warnings.extend(w_md)
    e_mq, w_mq = check_math_mode_quimica(content, fname)
    errors.extend(e_mq); warnings.extend(w_mq)

    # v4 check (2026-05-22, regra 10 do redator-e1.md, frente 2.1):
    # banco eh calibracao invisivel -- vocab de prova banido na E1/Resumindo.
    e_vp, w_vp = check_vocab_prova(content, fname)
    errors.extend(e_vp); warnings.extend(w_vp)

    # C/E sempre 4 itens (canonico 2026-07-01) -- so etapa2.typ
    if fname == "etapa2.typ":
        errors.extend(check_ce_quatro_itens(content, fname))

    # "Antes da aula" -- gate hard (canonico 2026-08-29)
    if fname == "pre-aula.typ":
        e_pa, w_pa = check_pre_aula(content, fname)
        errors.extend(e_pa); warnings.extend(w_pa)

    # v6 checks (2026-05-26): siglas em prosa sem #sigla() na 1a aparicao;
    # cadeia >=4 setas sem #figura-nebli adjacente. Aplicaveis so a etapa1.typ.
    if fname == "etapa1.typ":
        # Siglas em prosa cruzadas com #sigla() declaradas
        sigla_decls = set(re.findall(r'#sigla\("([^"]+)"', content))
        # Casos clinicos: NADH, NAD+, ADP, Pi, cAMP, AMPc, CoA, NADP+, FAD, FADH2, GDP
        # Detectar siglas (2+ letras maiusculas com possivel digito/charge) em prosa
        # Ignorar siglas dentro de #sigla() / #termo-nota[] / contextos de #figura-nebli /
        # linhas comecando com #
        plain_text = re.sub(r'#sigla\("[^"]*",\s*\[[^\]]*\]\)', '', content)
        plain_text = re.sub(r'#termo-nota\[[^\]]*\]\[[^\]]*\]', '', plain_text)
        plain_text = re.sub(r'#[a-z-]+\([^)]*\)', '', plain_text)  # remove outros helpers
        plain_text = re.sub(r'image\("[^"]*"\)', '', plain_text)
        siglas_usadas = set(re.findall(r'\b([A-Z]{2,}[0-9]?(?:\+|\-)?)\b', plain_text))
        # Filtrar siglas que provavelmente sao palavras (PARTE, etc) e abrevs comuns
        siglas_ignorar = {"PARTE", "DNA", "RNA", "ATP", "ADP", "AMP", "II", "III", "IV"}
        siglas_usadas -= siglas_ignorar
        nao_declaradas = sorted(siglas_usadas - sigla_decls)
        if nao_declaradas and len(nao_declaradas) > 3:
            warnings.append(f"  ! {fname}: {len(nao_declaradas)} sigla(s) usada(s) em prosa "
                            f"sem `#sigla()` declarado: {nao_declaradas[:8]}{'...' if len(nao_declaradas) > 8 else ''} "
                            f"-- verificar se merecem footnote na 1a aparicao (regra #2 do errosComuns).")

        # Cadeia >=4 setas sem figura adjacente
        # Setas: →, ->, => (sem escape complicado)
        paragrafos = re.split(r'\n\s*\n', content)
        suspeitos = []
        for i, par in enumerate(paragrafos):
            if "#figura-nebli" in par or "#atencao-box" in par[:50] or "#clinica-box" in par[:50]:
                continue
            arrows = par.count("→") + par.count("->") + par.count("=>")
            if arrows >= 4:
                # Tem figura no paragrafo anterior ou seguinte?
                near = ""
                if i > 0:
                    near += paragrafos[i-1]
                if i < len(paragrafos) - 1:
                    near += paragrafos[i+1]
                if "#figura-nebli" not in near:
                    preview = par.strip()[:80].replace("\n", " ")
                    suspeitos.append(f"      ({arrows} setas) ...{preview}...")
        if suspeitos:
            warnings.append(f"  ! {fname}: {len(suspeitos)} paragrafo(s) com >=4 setas causais "
                            f"sem #figura-nebli adjacente (regra: cadeia >=5 atores = figura "
                            f"obrigatoria):")
            warnings.extend(suspeitos[:5])

    # v5 check (2026-05-26): etapa-header / set-etapa duplicados.
    # main.typ ja chama #etapa-header() antes de #include "etapaN.typ".
    # Se etapaN.typ tambem chama, dois pagebreak(weak: true) consecutivos
    # geram pagina em branco antes da etapa (bug observado em
    # diferenciacao-celular.pdf p.48 e em todos os PDFs apos
    # 2026-05-26 caso o redator inclua o helper).
    if fname in ("etapa1.typ", "etapa2.typ", "etapa3.typ", "resumindo.typ"):
        if re.search(r"^#etapa-header\(", content, re.MULTILINE):
            errors.append(f"  x {fname}: contém `#etapa-header(...)` -- o main.typ ja faz isso "
                          f"antes do #include. Chamar de novo gera pagina em branco. Remover.")
        if re.search(r"^#set-etapa\(", content, re.MULTILINE):
            errors.append(f"  x {fname}: contém `#set-etapa(...)` -- o helper `etapa-header` "
                          f"chamado pelo main.typ ja faz set-etapa internamente. Remover.")

    return errors, warnings


# ============================================================
# Main
# ============================================================

def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    no_template = "--no-template" in args
    no_paridade = "--no-paridade" in args
    no_e2_regras = "--no-e2-regras" in args
    # Escape documentado para REGERAR resumo historico anterior a 2026-08-28,
    # que nasceu sem a secao "Antes da aula". Nunca usar em resumo novo.
    legado = "--legado" in args
    # --slug NOME -- forca slug do mapa-confusoes (CWD `_par_<slug>/` infere automatico)
    slug_override = None
    if "--slug" in args:
        idx = args.index("--slug")
        if idx + 1 < len(args):
            slug_override = args[idx + 1]
            args = args[:idx] + args[idx+2:]
    args = [a for a in args if a not in ("--strict", "--no-template", "--no-paridade",
                                        "--no-e2-regras", "--legado")]

    cwd = Path.cwd()

    pre_aula_ausente = None
    if args:
        files = [Path(a) for a in args]
        check_tpl = False
        check_par = False
        check_e2 = False
    else:
        files = []
        for fname in EXPECTATIONS:
            p = cwd / fname
            if p.exists():
                files.append(p)
        check_tpl = not no_template
        check_par = not no_paridade
        check_e2 = not no_e2_regras
        # Gate hard da secao "Antes da aula" (canonico 2026-08-29): a ausencia
        # do arquivo e erro, nao silencio. Antes, `pre-aula.typ` so era auditado
        # se existisse -- o que na pratica o deixava opcional.
        if not legado and not (cwd / "pre-aula.typ").exists():
            pre_aula_ausente = ("  x pre-aula.typ AUSENTE -- a secao \"Antes da aula\" e "
                                "obrigatoria em todo resumo (canonico 2026-08-28, gate hard "
                                "2026-08-29): 2 paginas de prosa continua na voz NEBLI contando "
                                "a historia da aula, sem figura, com os principais termos "
                                "plantados em negrito. Escrever DEPOIS da E1 fechada. "
                                "Regenerando resumo historico? use --legado.")
        else:
            pre_aula_ausente = None

    slug = slug_override or infer_slug(cwd)

    print(f"=== NEBLI precompile-check (v4 2026-05-22) ===")
    print(f"Diretorio: {cwd}")
    print(f"Slug inferido: {slug or '(nao inferido)'}")
    print(f"Arquivos etapa/resumindo: {len(files)}")
    if check_tpl:
        print(f"+ Template canonico: {TEMPLATE_PATH.name}")
    if check_par:
        print(f"+ Auditoria de paridade MC (correta vs distratora-mediana)")
    if check_e2:
        print(f"+ 4 regras canonicas da E2 (ordem invertida, paridade intra-Q, mapa-confusoes, sorteio)")
    print()

    if not files and not check_tpl:
        print("x Nada para checar.")
        sys.exit(3)

    all_errors = []
    all_warnings = []

    if pre_aula_ausente:
        print("-> pre-aula.typ")
        print(pre_aula_ausente)
        all_errors.append(pre_aula_ausente)

    for path in files:
        print(f"-> {path.name}")
        errors, warnings = check_file(path)
        if not errors and not warnings:
            print(f"  v ok")
        for e in errors:
            print(e)
        for w in warnings:
            print(w)
        # Passo (f) -- tail visual (sempre, mesmo se OK).
        # Auxilia detectar truncamento no meio que o resto nao pega.
        print_tail(path, path.name)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    if check_tpl:
        print(f"-> {TEMPLATE_PATH.name} (template canonico)")
        errors, warnings = check_template(TEMPLATE_PATH)
        if not errors and not warnings:
            print(f"  v ok -- {len(TEMPLATE_HELPERS)} helpers canonicos presentes")
        for e in errors:
            print(e)
        for w in warnings:
            print(w)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    if check_par:
        etapa2 = cwd / "etapa2.typ"
        main_t = cwd / "main.typ"
        if etapa2.exists() and main_t.exists():
            print(f"-> paridade-mc (etapa2.typ x main.typ)")
            errors, warnings = audit_paridade(etapa2, main_t)
            for e in errors:
                print(e)
            for w in warnings:
                print(w)
            all_errors.extend(errors)
            all_warnings.extend(warnings)
        else:
            print(f"-> paridade-mc: etapa2.typ ou main.typ ausente -- pulando")

    # ---- 4 regras canonicas da E2 (canonico 2026-05-22) ----
    if check_e2:
        etapa2 = cwd / "etapa2.typ"
        main_t = cwd / "main.typ"
        if etapa2.exists() and main_t.exists():
            print(f"-> e2-regras (ordem invertida + paridade intra-Q + sorteio do gabarito)")
            e2_content = etapa2.read_text(encoding="utf-8")
            mn_content = main_t.read_text(encoding="utf-8")
            questoes = parse_questao_mc(e2_content)
            gabarito = parse_gabarito(mn_content)
            if questoes and gabarito:
                errors, warnings = audit_e2_regras_extra(questoes, gabarito)
                for e in errors:
                    print(e)
                for w in warnings:
                    print(w)
                all_errors.extend(errors)
                all_warnings.extend(warnings)
            else:
                print(f"  ! e2-regras: parse vazio (questoes={len(questoes)}, gabarito-mc={len(gabarito)}) -- pulando")
                all_warnings.append(f"  ! e2-regras: parse de etapa2/main vazio -- pulou auditoria")
        else:
            print(f"-> e2-regras: etapa2.typ ou main.typ ausente -- pulando")

        # Mapa de Confusoes -- roda mesmo sem etapa2.typ (queremos pegar
        # ausencia ANTES da redacao da E2 quando possivel).
        print(f"-> mapa-confusoes (slug: {slug or 'nao inferido'})")
        errors, warnings = check_mapa_confusoes(slug)
        if not errors and not warnings:
            print(f"  v ok")
        for e in errors:
            print(e)
        for w in warnings:
            print(w)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    print()
    print(f"Resumo: {len(all_errors)} erro(s), {len(all_warnings)} warning(s)")

    if strict and all_warnings and not all_errors:
        all_errors.extend(all_warnings)

    if all_errors:
        print("\nx FALHA -- NAO COMPILAR. Corrija os erros acima primeiro.")
        if any("NULL byte" in e or "nao encontrado" in e or "TEMPLATE CANONICO" in e
               or "TRUNCAMENTO no meio da linha" in e for e in all_errors):
            sys.exit(3)
        if any("provavel TRUNCAMENTO" in e or "extras" in e for e in all_errors):
            sys.exit(2)
        sys.exit(1)
    print("\nv OK -- pode compilar.")
    sys.exit(0)


if __name__ == "__main__":
    main()
