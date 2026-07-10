#!/usr/bin/env python3
"""
NEBLI -- extrair_armadilhas.py
Canonico 2026-05-22 (P44, frente 2.1 "Banco como calibrador da E1").

Le os .md classificados de uma aula, extrai o campo `armadilha:` do
frontmatter YAML, sanitiza vocabulario de prova e emite JSON para
consumo INTERNO do ORQUESTRADOR.

REGRA DE INVISIBILIDADE DO BANCO (canonica): o leitor do PDF jamais
sabe que existe um banco. Este JSON eh artefato interno. A Secao D
do Tema Card eh redigida pelo ORQUESTRADOR com voz de mecanismo
(o aluno entende errado X, o caminho certo eh Y), nunca com voz de
prova ("isso cai", "questao classica", "pegadinha").

Uso:
  python3 banco/extrair_armadilhas.py <slug>
  python3 banco/extrair_armadilhas.py bioq-15-glicolise

Saida:
  arquivos-trabalho/armadilhas/<slug>.json
"""

import sys
import re
import json
from pathlib import Path

# UTF-8 forcado no stdout (Windows cp1252 quebra com acentos / subscripts)
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, Exception):
    pass

# ============================================================
# Vocabulario PROIBIDO no texto que vai para a Secao D do Tema Card
# e para os boxes da E1. Marca no extrator; ORQUESTRADOR reescreve.
# ============================================================
VOCAB_PROIBIDO_RE = re.compile(
    r"\b("
    r"prova|provas|cai|caiu|caem|caiam|cair[aá]|cobranc[aá]|cobrad[oa]s?|"
    r"banca|pegadinha|pegadinhas|"
    r"quest[aã]o|quest[oõ]es|gabarito|examinador|examinadora|enunciado|"
    r"vestibular|enare|usmle|fmusp|cespe|ufrgs|residencia|"
    r"p1|p2|p3|simulado|simulados"
    r")\b",
    re.IGNORECASE,
)


def sanitize(texto):
    """Retorna (texto_original, marcadores). Nao reescreve -- marca.
    O ORQUESTRADOR eh quem redige a Secao D com voz limpa."""
    matches = VOCAB_PROIBIDO_RE.findall(texto)
    palavras = sorted(set(m.lower() for m in matches))
    return texto, palavras


def parse_frontmatter(content):
    """Parser YAML minimalista para frontmatter `---...---`. Foco no
    campo `armadilha:` que pode ser string entre aspas, possivelmente
    multi-linha. Outros campos sao single-line `chave: valor`."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not m:
        return {}
    body = m.group(1)
    out = {}

    # Campos single-line simples
    for field in ("id", "aula", "nivel", "formato", "conceito_central",
                  "gabarito", "uc_origem", "prova", "ano"):
        rx = re.compile(rf"^{field}:\s*(.+?)\s*$", re.MULTILINE)
        m2 = rx.search(body)
        if m2:
            out[field] = m2.group(1).strip().strip('"').strip("'")

    # Tags: lista entre [ ]
    m_tags = re.search(r"^tags:\s*\[(.+?)\]\s*$", body, re.MULTILINE)
    if m_tags:
        out["tags"] = [t.strip().strip('"').strip("'") for t in m_tags.group(1).split(",")]

    # Armadilha: pode ser "string entre aspas" (possivelmente multi-linha)
    # ou texto solto ate o proximo campo YAML.
    m_arm = re.search(r'^armadilha:\s*"((?:[^"\\]|\\.)*)"\s*$',
                      body, re.MULTILINE | re.DOTALL)
    if m_arm:
        out["armadilha"] = m_arm.group(1).strip()
    else:
        # Fallback: campo sem aspas, lendo ate proxima chave YAML
        m_arm2 = re.search(r"^armadilha:\s*(.+?)(?=^[a-z_]+:|\Z)",
                           body, re.MULTILINE | re.DOTALL)
        if m_arm2:
            out["armadilha"] = m_arm2.group(1).strip().strip('"').strip()

    return out


def dedup_armadilhas(lista):
    """Dedup heuristico: se duas armadilhas compartilham >=10 palavras
    consecutivas, agrupar (somar origens). Conservador -- so funde casos
    obviamente identicos."""
    grupos = []
    for item in lista:
        chave = " ".join(item["descricao"].lower().split()[:10])
        matched = False
        for g in grupos:
            chave_g = " ".join(g["descricao"].lower().split()[:10])
            if chave == chave_g:
                g["origens"].extend(item["origens"])
                g["incidencia"] += 1
                matched = True
                break
        if not matched:
            grupos.append(dict(item))
    # Ordena por incidencia desc
    grupos.sort(key=lambda x: (-x["incidencia"], x["origens"][0] if x["origens"] else ""))
    return grupos


def main():
    if len(sys.argv) < 2:
        print("uso: extrair_armadilhas.py <slug>", file=sys.stderr)
        print("ex:  extrair_armadilhas.py bioq-15-glicolise", file=sys.stderr)
        sys.exit(1)
    slug = sys.argv[1]

    base = Path(__file__).resolve().parent / "questoes"
    if not base.exists():
        print(f"x diretorio {base} nao encontrado", file=sys.stderr)
        sys.exit(2)

    encontradas = []
    sem_armadilha = 0
    for md in sorted(base.glob("q-*.md")):
        try:
            content = md.read_text(encoding="utf-8")
        except OSError:
            continue
        fm = parse_frontmatter(content)
        if fm.get("aula") != slug:
            continue
        arm = (fm.get("armadilha") or "").strip()
        if len(arm) < 20:
            sem_armadilha += 1
            continue
        _, palavras_proibidas = sanitize(arm)
        encontradas.append({
            "descricao": arm,
            "origens": [fm.get("id")],
            "nivel": fm.get("nivel"),
            "conceito": fm.get("conceito_central"),
            "tags": fm.get("tags", []),
            "palavras_proibidas": palavras_proibidas,
            "incidencia": 1,
        })

    grupos = dedup_armadilhas(encontradas)

    output_dir = Path(__file__).resolve().parent.parent / "arquivos-trabalho" / "armadilhas"
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{slug}.json"

    suspeitas = [g for g in grupos if g["palavras_proibidas"]]
    payload = {
        "slug": slug,
        "total_armadilhas_unicas": len(grupos),
        "total_questoes_com_armadilha": sum(g["incidencia"] for g in grupos),
        "questoes_sem_campo_armadilha": sem_armadilha,
        "aviso_invisibilidade": (
            "ARTEFATO INTERNO. Nada deste arquivo aparece no PDF. "
            "O ORQUESTRADOR redige a Secao D 'Pontos de quebra do raciocinio' "
            "do Tema Card com voz de mecanismo. Palavras proibidas (prova, "
            "questao, banca, pegadinha, cai, gabarito etc.) sao MARCADAS, "
            "nao reescritas -- a reescrita acontece na redacao da Secao D."
        ),
        "armadilhas": grupos,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                        encoding="utf-8")

    # ====================================================================
    # Emissao adicional: mapa-confusoes/<slug>.md (canonico 2026-05-26)
    # Resolve o problema de quebra silenciosa: QUESTIONADOR usava mapa
    # antigo de outro tema se esquecesse de criar o .md manualmente.
    # Esqueleto gerado automaticamente -- ORQUESTRADOR/QUESTIONADOR
    # refinam a curadoria depois (mecanismo do erro, origem narrativa).
    # ====================================================================
    mapa_dir = Path(__file__).resolve().parent.parent / "mapa-confusoes"
    mapa_dir.mkdir(parents=True, exist_ok=True)
    mapa_path = mapa_dir / f"{slug}.md"

    if mapa_path.exists():
        # Nao sobrescreve curadoria humana ja existente
        print(f"  i mapa-confusoes/{slug}.md ja existe -- preservado intacto")
    else:
        linhas = []
        linhas.append(f"# Mapa de Confusoes -- {slug}")
        linhas.append("")
        linhas.append(f"**Gerado automaticamente** por `extrair_armadilhas.py` em "
                      f"`arquivos-trabalho/armadilhas/{slug}.json`. Este esqueleto "
                      f"precisa de curadoria do QUESTIONADOR antes da redacao das "
                      f"distratoras: agrupar por subtopico (>=4 por subtopico), "
                      f"reescrever na voz de mecanismo (sem vocabulario de prova) "
                      f"e completar com confusoes do livro-texto quando o banco "
                      f"nao cobre o subtopico.")
        linhas.append("")
        linhas.append(f"**Origem do esqueleto:** {len(grupos)} armadilha(s) unica(s) "
                      f"extraida(s) de {payload['total_questoes_com_armadilha']} "
                      f"questao(oes) classificada(s) na aula `{slug}`.")
        linhas.append("")
        linhas.append("---")
        linhas.append("")
        linhas.append("## Confusoes catalogadas (esqueleto bruto)")
        linhas.append("")
        for i, g in enumerate(grupos, 1):
            origens = ", ".join(g["origens"]) if g["origens"] else "?"
            nivel = g.get("nivel") or "?"
            conceito = g.get("conceito") or "?"
            descricao = g["descricao"].replace("\n", " ").strip()
            flag = ""
            if g["palavras_proibidas"]:
                flag = f"  \n  *VOCAB DE PROVA detectado: {', '.join(g['palavras_proibidas'])} -- reescrever na voz de mecanismo antes de usar.*"
            linhas.append(f"### C{i:02d} -- {conceito}")
            linhas.append("")
            linhas.append(f"**Descricao bruta (do banco):** {descricao}")
            linhas.append("")
            linhas.append(f"- Nivel: {nivel}")
            linhas.append(f"- Origem: banco NEBLI {origens}{flag}")
            linhas.append(f"- Mecanismo do erro: *(refinar pelo QUESTIONADOR -- "
                          f"qual o passo mecanistico que o aluno inverte?)*")
            linhas.append(f"- Subtopico-alvo na E1: *(mapear para PARTE/subtopico)*")
            linhas.append("")
        linhas.append("---")
        linhas.append("")
        linhas.append("## Checklist de curadoria (preencher antes de redigir E2)")
        linhas.append("")
        linhas.append("- [ ] Cada confusao agrupada por subtopico da E1 (>=4 por subtopico).")
        linhas.append("- [ ] Voz de mecanismo: zero ocorrencia de prova/questao/banca/pegadinha/cai/gabarito.")
        linhas.append("- [ ] Adicionar confusoes do livro-texto onde o banco nao cobre.")
        linhas.append("- [ ] Cada confusao tem nome curto + descricao mecanistica + origem rastreavel.")
        linhas.append("")
        mapa_path.write_text("\n".join(linhas), encoding="utf-8")
        print(f"  + mapa-confusoes/{slug}.md gerado (esqueleto para curadoria)")

    print(f"v ok: aula `{slug}`")
    print(f"  {len(grupos)} armadilha(s) unica(s) extraida(s)")
    print(f"  {payload['total_questoes_com_armadilha']} questao(oes) com armadilha")
    print(f"  {sem_armadilha} questao(oes) classificada(s) sem campo armadilha")
    print(f"  -> {out_path.relative_to(Path.cwd()) if out_path.is_relative_to(Path.cwd()) else out_path}")
    if suspeitas:
        print(f"  ! {len(suspeitas)} armadilha(s) contem vocabulario de prova "
              f"(prova/questao/banca/...) -- ORQUESTRADOR REESCREVE na Secao D")


if __name__ == "__main__":
    main()
