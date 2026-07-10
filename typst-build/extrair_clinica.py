#!/usr/bin/env python3
"""
extrair_clinica.py <slug>

Lê os arquivos Typst de um resumo NEBLI e extrai o material clínico bruto
para alimentar a geração de flashcards (Etapa 4).

Saída: arquivos-trabalho/clinica-bruta-<slug>.json

Fontes parseadas:
  - typst-build/_par_<slug>/etapa1.typ  (modo paralelo, preferido)
    OU typst-build/etapa1.typ  (modo serial, fallback)
  - typst-build/_par_<slug>/resumindo.typ  OU typst-build/resumindo.typ
  - mapa-confusoes/<slug>.md  (tenta variantes de slug)

Blocos extraídos do etapa1:
  - #clinica-box("titulo", [conteúdo])
  - #atencao-box("titulo", [conteúdo])
  - #confusao-prevista(titulo: "...", aluno_acha: [...], mecanismo: [...])

Do resumindo: tuplas (titulo, [corpo]) dentro do #resumindo-page((...)).
Do mapa-confusoes: arquivo .md inteiro como texto bruto.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # nebli/


# --------------------------------------------------------------------------- #
# Localização de arquivos                                                     #
# --------------------------------------------------------------------------- #

def localizar_etapa1(slug: str) -> Path | None:
    candidatos = [
        ROOT / "typst-build" / f"_par_{slug}" / "etapa1.typ",
        ROOT / "typst-build" / "etapa1.typ",
    ]
    for c in candidatos:
        if c.exists():
            return c
    return None


def localizar_resumindo(slug: str) -> Path | None:
    candidatos = [
        ROOT / "typst-build" / f"_par_{slug}" / "resumindo.typ",
        ROOT / "typst-build" / "resumindo.typ",
    ]
    for c in candidatos:
        if c.exists():
            return c
    return None


def localizar_mapa(slug: str) -> Path | None:
    """Mapas de confusões nem sempre têm slug idêntico ao _par_<slug>.
    Tenta variantes na ordem: exato, sem 'de-', sem prefixos disciplinares."""
    pasta = ROOT / "mapa-confusoes"
    if not pasta.exists():
        return None
    candidatos = [slug]
    # ex: ciclo-de-krebs → ciclo-krebs
    sem_de = slug.replace("-de-", "-")
    if sem_de != slug:
        candidatos.append(sem_de)
    # ex: bioq-17-ciclo-krebs → ciclo-krebs (sem prefixo disciplina-NN)
    sem_prefixo = re.sub(r"^[a-z]+-\d+[a-z]?-", "", slug)
    if sem_prefixo != slug:
        candidatos.append(sem_prefixo)
    for nome in candidatos:
        p = pasta / f"{nome}.md"
        if p.exists():
            return p
    return None


# --------------------------------------------------------------------------- #
# Parser balanceado                                                           #
# --------------------------------------------------------------------------- #

def _achar_fechamento(texto: str, inicio: int, abre: str, fecha: str) -> int:
    """Dado que texto[inicio] == abre, devolve o índice do `fecha` balanceado.
    Respeita strings "..." dentro do bloco (apenas escape simples \\")."""
    assert texto[inicio] == abre
    profundidade = 0
    i = inicio
    n = len(texto)
    while i < n:
        c = texto[i]
        if c == '"':
            # pula string
            i += 1
            while i < n and texto[i] != '"':
                if texto[i] == "\\":
                    i += 2
                    continue
                i += 1
            i += 1
            continue
        if c == abre:
            profundidade += 1
        elif c == fecha:
            profundidade -= 1
            if profundidade == 0:
                return i
        i += 1
    raise ValueError(f"sem fechamento balanceado para {abre} em {inicio}")


def _extrair_args_paren(texto: str, pos_paren: int) -> str:
    """Dado o índice do `(` abrindo, devolve a string interna entre `(...)`."""
    fim = _achar_fechamento(texto, pos_paren, "(", ")")
    return texto[pos_paren + 1 : fim]


def _split_args_top(args: str) -> list[str]:
    """Splita por vírgulas só no nível 0 de parens/brackets/strings."""
    pedacos = []
    buf = []
    prof_paren = 0
    prof_bracket = 0
    i = 0
    n = len(args)
    while i < n:
        c = args[i]
        if c == '"':
            buf.append(c)
            i += 1
            while i < n and args[i] != '"':
                if args[i] == "\\":
                    buf.append(args[i])
                    if i + 1 < n:
                        buf.append(args[i + 1])
                    i += 2
                    continue
                buf.append(args[i])
                i += 1
            if i < n:
                buf.append(args[i])
                i += 1
            continue
        if c == "(":
            prof_paren += 1
        elif c == ")":
            prof_paren -= 1
        elif c == "[":
            prof_bracket += 1
        elif c == "]":
            prof_bracket -= 1
        if c == "," and prof_paren == 0 and prof_bracket == 0:
            pedacos.append("".join(buf).strip())
            buf = []
            i += 1
            continue
        buf.append(c)
        i += 1
    final = "".join(buf).strip()
    if final:
        pedacos.append(final)
    return pedacos


def _despir_string(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return s[1:-1]
    return s


def _despir_bracket(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == "[" and s[-1] == "]":
        return s[1:-1].strip()
    return s


def _despir_arg_nomeado(s: str, nome: str) -> str | None:
    """Se s começa com `nome:`, retorna o valor à direita (sem stripear chaves)."""
    s = s.strip()
    prefix = f"{nome}:"
    if s.startswith(prefix):
        return s[len(prefix) :].strip()
    return None


# --------------------------------------------------------------------------- #
# Extratores específicos                                                      #
# --------------------------------------------------------------------------- #

def extrair_caixas(texto: str, nome_funcao: str) -> list[dict]:
    """Extrai todas as ocorrências de #<nome_funcao>(titulo, conteudo) ou
    #<nome_funcao>("titulo", [conteudo])."""
    resultado = []
    pattern = "#" + nome_funcao + "("
    i = 0
    while True:
        j = texto.find(pattern, i)
        if j == -1:
            break
        # garante que não estamos em outro identificador (ex: confusao-prevista é
        # separada porque tem nome próprio, mas atencao-box-X seria match falso)
        pos_paren = j + len(pattern) - 1
        if texto[pos_paren] != "(":
            i = j + 1
            continue
        try:
            args_raw = _extrair_args_paren(texto, pos_paren)
        except ValueError:
            i = j + 1
            continue
        partes = _split_args_top(args_raw)
        if len(partes) < 2:
            i = pos_paren + 1
            continue
        titulo = _despir_string(partes[0])
        conteudo = _despir_bracket(partes[1])
        resultado.append({"titulo": titulo, "conteudo": conteudo})
        i = pos_paren + 1
    return resultado


def extrair_confusoes_previstas(texto: str) -> list[dict]:
    resultado = []
    pattern = "#confusao-prevista("
    i = 0
    while True:
        j = texto.find(pattern, i)
        if j == -1:
            break
        pos_paren = j + len(pattern) - 1
        try:
            args_raw = _extrair_args_paren(texto, pos_paren)
        except ValueError:
            i = j + 1
            continue
        partes = _split_args_top(args_raw)
        item = {"titulo": "", "aluno_acha": "", "mecanismo": ""}
        for p in partes:
            v = _despir_arg_nomeado(p, "titulo")
            if v is not None:
                item["titulo"] = _despir_string(v)
                continue
            v = _despir_arg_nomeado(p, "aluno_acha")
            if v is not None:
                item["aluno_acha"] = _despir_bracket(v)
                continue
            v = _despir_arg_nomeado(p, "mecanismo")
            if v is not None:
                item["mecanismo"] = _despir_bracket(v)
                continue
        resultado.append(item)
        i = pos_paren + 1
    return resultado


def extrair_resumindo(texto: str) -> list[dict]:
    """Lê o argumento de #resumindo-page((...)) e extrai pares (titulo, [corpo])."""
    pattern = "#resumindo-page("
    j = texto.find(pattern)
    if j == -1:
        return []
    pos_paren = j + len(pattern) - 1
    try:
        args_raw = _extrair_args_paren(texto, pos_paren)
    except ValueError:
        return []
    # args_raw é tipicamente "(t, c), (t, c), ..." ou "((t, c), (t, c), ...)"
    s = args_raw.strip()
    # Se vem como tupla externa única: descasca uma camada.
    if s.startswith("(") and s.endswith(")"):
        # cuidado: descasca só se a primeira `(` fecha no último `)`.
        try:
            if _achar_fechamento(s, 0, "(", ")") == len(s) - 1:
                s = s[1:-1].strip()
        except ValueError:
            pass
    # Agora s é "(t, c), (t, c), ..."
    secoes = []
    i = 0
    n = len(s)
    while i < n:
        if s[i].isspace() or s[i] == ",":
            i += 1
            continue
        if s[i] != "(":
            i += 1
            continue
        fim = _achar_fechamento(s, i, "(", ")")
        bloco = s[i + 1 : fim].strip()
        partes = _split_args_top(bloco)
        if len(partes) >= 2:
            titulo = _despir_string(partes[0])
            corpo = _despir_bracket(partes[1])
            secoes.append({"titulo": titulo, "corpo": corpo})
        i = fim + 1
    return secoes


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #

def normalizar_whitespace(s: str) -> str:
    """Compacta whitespace para o JSON ficar legível sem perder semântica."""
    return re.sub(r"\s+", " ", s).strip()


def main(slug: str) -> int:
    etapa1 = localizar_etapa1(slug)
    resumindo = localizar_resumindo(slug)
    if etapa1 is None:
        print(f"ERRO: etapa1.typ não encontrado para slug '{slug}'", file=sys.stderr)
        print(
            f"  procurado em: typst-build/_par_{slug}/etapa1.typ "
            f"e typst-build/etapa1.typ",
            file=sys.stderr,
        )
        return 2
    if resumindo is None:
        print(f"AVISO: resumindo.typ não encontrado para slug '{slug}'", file=sys.stderr)

    texto_e1 = etapa1.read_text(encoding="utf-8")
    clinica = extrair_caixas(texto_e1, "clinica-box")
    atencao = extrair_caixas(texto_e1, "atencao-box")
    confusoes = extrair_confusoes_previstas(texto_e1)

    resumindo_secoes: list[dict] = []
    if resumindo is not None:
        texto_r = resumindo.read_text(encoding="utf-8")
        resumindo_secoes = extrair_resumindo(texto_r)

    mapa = localizar_mapa(slug)
    mapa_raw = None
    if mapa is not None:
        mapa_raw = mapa.read_text(encoding="utf-8")

    # Limpa whitespace nos campos textuais para o JSON ficar manejável.
    for b in clinica:
        b["conteudo"] = normalizar_whitespace(b["conteudo"])
    for b in atencao:
        b["conteudo"] = normalizar_whitespace(b["conteudo"])
    for c in confusoes:
        c["aluno_acha"] = normalizar_whitespace(c["aluno_acha"])
        c["mecanismo"] = normalizar_whitespace(c["mecanismo"])
    for s in resumindo_secoes:
        s["corpo"] = normalizar_whitespace(s["corpo"])

    saida = {
        "slug": slug,
        "gerado_em": date.today().isoformat(),
        "etapa1_path": str(etapa1.relative_to(ROOT)).replace("\\", "/"),
        "resumindo_path": (
            str(resumindo.relative_to(ROOT)).replace("\\", "/") if resumindo else None
        ),
        "mapa_confusoes_path": (
            str(mapa.relative_to(ROOT)).replace("\\", "/") if mapa else None
        ),
        "clinica_boxes": clinica,
        "atencao_boxes": atencao,
        "confusoes_previstas": confusoes,
        "resumindo_secoes": resumindo_secoes,
        "mapa_confusoes_raw": mapa_raw,
    }

    saida_dir = ROOT / "arquivos-trabalho"
    saida_dir.mkdir(exist_ok=True)
    saida_path = saida_dir / f"clinica-bruta-{slug}.json"
    saida_path.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: {saida_path.relative_to(ROOT)}")
    print(f"  clinica_boxes: {len(clinica)}")
    print(f"  atencao_boxes: {len(atencao)}")
    print(f"  confusoes_previstas: {len(confusoes)}")
    print(f"  resumindo_secoes: {len(resumindo_secoes)}")
    print(f"  mapa_confusoes: {'presente' if mapa else 'ausente'}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("uso: python extrair_clinica.py <slug>", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
