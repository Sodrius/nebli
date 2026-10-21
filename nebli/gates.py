"""Porta única de entrega de um deck-aula: falha se faltar evidência de qualquer passo do pipeline.

    python3 -m nebli.gates arquivos-trabalho/<corrida> [--sem-anki] [--sem-drive]

Verifica evidências estruturais; não substitui revisão semântica nem certifica funções planejadas.
A corrida precisa de `fontes.json` e `plan.json`. Sai com código 1 se algo falhar.
Em fontes.json, escopo="cards" dispensa E1; o padrão é escopo="e1+cards".

fontes.json:
  {"nome": "<Nome da aula>", "drive_pasta": "UCxx/<Componente>/<NN - Aula>",
   "slides": {"arquivo": "fontes/slides.pdf", "todas_vistas": true},
   "livros": [{"livro": "Aires cap. 62", "texto": "<arquivo com o capítulo extraído>", "lido": true}],
   "canais": [{"canal": "MK Fisiologia", "transcricao": "<arquivo>", "lido": "integral" | "trechos"}],
   "provas": {"estado": "consultada" | "não localizada", "busca": "<onde procurei>"},
   "exercicios": {...mesmo formato...}, "caoc": {...mesmo formato...}}
"""
from __future__ import annotations

import os
import argparse
import html
import hashlib
import json
import re
import sys
from pathlib import Path

ESTADOS = {"consultada", "não localizada", "inacessível", "não aplicável"}
MIN_CANAIS = 1  # F-20261021-CLAUDE-06: “tem que buscar algum do yt, não só Ninja Nerd, de preferência os que gosto”
MAX_AUTORAL = 0.15  # gatilho de auditoria da busca, não cota da aula
MAX_IDENT_HISTO = 0.25
MAX_CLOZE = 3  # F-20261003-CLAUDE-18: cloze de 1–2 palavras no geral, até 3 (era 4)
MAX_TEXTO = 250  # F-20261003-CLAUDE-14: "cards enormes... melhor recortar e fazer vários menores"
CLASSES_SLIDE = {"capa", "logistica", "conteudo", "revisao", "fora_do_recorte"}
GENERIC_EXTRAS = (
    "connect the fact to inhaled pollutants and the tissue response described in this lesson",
    "in this lesson, use this card for",
    "in this lesson, this term identifies",
)

# Registro de exceções históricas, mantido para interpretar corridas anteriores.
AUTHOR_EXCEPTIONS = {
    "2026-uc03-microbiologia-43-biologia-fungos": "F-20261004-CODEX-02",
}
# F-20261009-CLAUDE-03: "decks-anking like ... (só se realmente forem, se não só aumentamos a qtd de autorais para refletir melhor a
# aula)". Completude prevalece sobre o teto quando a busca registrada mostra que os acervos não cobrem a aula; vale só com o
# inventário atômico aprovado (todo autoral ligado a item do material de base) e lint sem reprovação dura.
COMPLETUDE_EXCEPTIONS = {
    "2026-uc03-microbiologia-43-biologia-fungos": "micologia geral ausente do AnKing/MCAT",
    "2026-uc03-microbiologia-26-morfologia-estrutura-bacteriana": "bacteriologia geral parcial no AnKing",
    "2026-uc08-fisiologia-09-motilidade-ii": "motilidade fina ausente dos acervos",
    "2026-uc03-patologia-23-edema-congestao": "cavidades, linfedema e histologia da aula sem AnKing",
    "2026-uc03-patologia-24-patologia-ambiental": "poluição atmosférica ausente do AnKing (só antracose)",
    "2026-uc03-patologia-radiologia-19-correlacao-2": "leitura das imagens da própria aula (US, TC, peças) sem equivalente nos acervos",
    "2026-uc03-microbiologia-44-micoses-cutaneas": "micologia de bancada (habitat, localização por gênero, cultivo e identificação das espécies) e micoses superficiais raras ausentes do AnKing",
    "2026-uc03-microbiologia-28-pratica-1": "aula prática: biossegurança, corantes/mordente e meios específicos (mínimo, Mueller-Hinton, manitol-sal, cetrimida) ausentes do AnKing; o resto é associado de Morfologia e Fisiologia",
    "2026-uc03-microbiologia-27-fisiologia-bacteriana": "nutrição, fatores físicos, imunidade nutricional, fermentação × respiração, fases da curva e meios brasileiros (SS, Rugai, cromogênicos) ausentes ou só listados no AnKing",
    "2026-uc03-bioquimica-25-integracao-metabolica-i": "papel de cada tecido, controle por Km/afinidade, PP1, glucagon × epinefrina, metabolismo cardíaco e hemácia ausentes como cards no AnKing",
    "2026-uc03-biologia-molecular-52-expressao-eucariotos-ii": "remodeladores dependentes de ATP, HAT/HDAC, código de histonas, HP1, DNMT de manutenção, ilhas CpG e epigenética ausentes ou dispersos no AnKing",
    "2026-uc03-microbiologia-50-micoses-sistemicas": "epidemiologia brasileira da PCM (P. lutzii, tatu, café, 15:1, estradiol), parede e dimorfismo, macroconídios tuberculados, identificação laboratorial de Candida e C. gattii ausentes do AnKing",
    "2026-uc03-biologia-molecular-54-rnas-nao-codificadores": "atenuação trp, riboswitches, biologia do CRISPR, via Dicer/RISC/Drosha, siRNA × miRNA, miR-31, lncRNA e Xist ausentes do AnKing",
    "2026-uc03-imunologia-49-ativacao-celulas-b": "B-1 × B-2, edição do receptor, CD19/CD22, mecanismo TI/conjugada, AID, CDR, FDC e cinética primária × secundária ausentes do AnKing",
    "2026-uc03-microbiologia-48-micoses-subcutaneas": "cromomicose, eumicetoma, doença de Jorge Lobo e epidemia brasileira por gatos ausentes do AnKing",
    "2026-uc03-biologia-molecular-46-expressao-eucariotos-i": "maquinaria eucariótica (Mediador, TBP), Gal4 (universalidade, modularidade) e sinalização a fatores de transcrição ausentes do AnKing",
    "2026-uc03-imunologia-45-ativacao-linfocitos-t": "sinapse, IL-2 autócrina, AICD, contração/memória, apresentação cruzada e Treg × Th17 ausentes do AnKing",
}


def sources(run, data):
    out = []
    def material(path):
        candidate = run / path
        return candidate.is_file() and candidate.stat().st_size > 0
    slides = data.get("slides", {})
    out.append(("slides: arquivo não vazio na corrida e todas as lâminas vistas", bool(slides.get("todas_vistas")) and material(slides.get("arquivo", "_"))))
    # F-20261016-CLAUDE-05: “não há slide para isso, é necessário criar a lógica da aula”. Sem PDF de lâminas, só vale aula
    # declarada sem lâminas por Davi (fala literal + id do feedback) com o roteiro da aula escrito na corrida no lugar do PDF.
    if not str(slides.get("arquivo", "")).lower().endswith(".pdf"):
        sl = data.get("sem_laminas") or {}
        out.append(("[duro] aula sem lâminas: declarada por Davi (fala + F-id) e roteiro da aula na corrida",
                    bool(str(sl.get("fala", "")).strip() and re.match(r"F-\d{8}-", str(sl.get("feedback", ""))) and material(slides.get("arquivo", "_")))))
    books = [b for b in data.get("livros", []) if b.get("lido") and material(b.get("texto", "_"))]
    out.append(("bibliografia da UC: capítulo da aula extraído e lido", bool(books)))
    channels = [c for c in data.get("canais", []) if c.get("lido") == "integral" and material(c.get("transcricao", "_"))]
    blocked = canais_bloqueados(data)
    out.append((f"canais que Davi acompanha: pelo menos {MIN_CANAIS} aulas com transcrição lida" + (_nota(blocked) if blocked else ""),
                len(channels) >= MIN_CANAIS or bool(blocked)))
    # F-20261021-CLAUDE-06: sai o gate só do Ninja Nerd; entra a leitura de vídeo de qualquer canal que Davi acompanha (dispensa revogada).
    uncal = [c.get("canal", "?")[:40] for c in channels if not str(c.get("calibracao", "")).strip()]
    out.append(("cada canal com 'calibracao': o que mudou ou confirmou no deck" + (f" (faltam: {uncal[:3]})" if uncal else ""), not uncal))
    for kind in ("provas", "exercicios", "caoc", "veteranos"):
        item = data.get(kind, {})
        ok = item.get("estado") in ESTADOS and (item.get("estado") == "consultada" or bool(str(item.get("busca", "")).strip()))
        out.append((f"{kind}: consultado, ou busca no Drive registrada", ok))
    out += source_evidence(run, data)
    out.append(class_folder(run, data))
    out += uc_materials(run, data)
    return out


NAO_LIVRO = re.compile(r"transcri|slides?\b|grupo|plataforma|relat[oó]rio|apresenta", re.I)


def _arquivos(pasta):
    import os
    pasta = Path(os.path.expanduser(str(pasta)))
    if not pasta.is_dir():
        return []
    return sorted(p for p in pasta.rglob("*") if p.is_file() and not p.name.startswith(".") and p.suffix.lower() not in {".mp4", ".mov", ".m4a"})


def uc_materials(run, data):
    """F-20261015-CLAUDE-05 (gate duro): “verificar slide + bibliografia + apostila de veterano + o que mais houver na pasta ou em
    outras pastas, tipo outros”. Em 14–15/10 várias corridas declararam a transcrição como 'veteranos' e 'bibliografia' e saíram
    rasas. Cada arquivo de: apostilas de veteranos da UC (`UCxx/Outros/Apostilas de veteranos`), pasta pessoal da aula,
    `Material para Estudos` do componente no drive da turma e `pastas_extra` está em `materiais_uc` como lido (texto extraído na
    corrida + seção) ou descartado com motivo; a bibliografia tem de ser um livro, não transcrição/slides/relatório."""
    from nebli import entrega
    out = []
    import unicodedata
    nfc = lambda x: unicodedata.normalize("NFC", str(x))
    mats = {nfc(k): v for k, v in (data.get("materiais_uc", {}) or {}).items()}
    lidos = {nfc(os.path.basename(str(x))) for x in data.get("turma_arquivos_lidos", [])}
    lidos |= {nfc(os.path.basename(str(r.get("arquivo", "")))) for recs in data.get("evidencias", {}).values() if isinstance(recs, list)
              for r in recs if isinstance(r, dict)}

    def conta(nome):
        nome = nfc(nome)
        m = mats.get(nome)
        if isinstance(m, dict) and str(m.get("descartado", "")).strip():
            return True
        if isinstance(m, dict) and m.get("texto") and str(m.get("secao", "")).strip():
            f = run / str(m["texto"])
            return f.is_file() and f.stat().st_size > 0
        return nome in lidos

    livros = [b for b in data.get("livros", []) if not NAO_LIVRO.search(f"{b.get('livro', '')} {b.get('texto', '')}")]
    out.append(("bibliografia é livro da UC (não transcrição, slides nem relatório de grupo)", bool(livros)))
    parts = Path(str(data.get("drive_pasta", ""))).parts
    uc = parts[0] if parts and re.fullmatch(r"UC\d\d", parts[0]) else None
    grupos = []
    if uc:
        ap = [p for p in _arquivos(entrega.ROOT / uc / "Outros") if "veteran" in str(p).lower()]
        grupos.append(("apostilas de veteranos da UC", ap, True))
        pessoal = [p for p in _arquivos(entrega.ROOT / Path(*parts)) if p.suffix.lower() != ".apkg"
                   and not p.name.startswith(str(data.get("nome", "\0")) + " - ")]
        grupos.append(("pasta pessoal da aula", pessoal, False))
    turma = data.get("pasta_turma")
    if isinstance(turma, str) and os.path.isdir(os.path.expanduser(turma)):
        comp = Path(os.path.expanduser(turma)).parent
        grupos.append(("Material para Estudos do componente", [p for p in _arquivos(comp) if "material para estudo" in str(p).lower()], False))
    for extra in data.get("pastas_extra", []):
        grupos.append((f"pasta extra {Path(extra).name}", _arquivos(extra), False))
    if not uc and not data.get("pastas_extra"):
        out.append(("materiais da UC: drive_pasta sem UC reconhecida e sem 'pastas_extra'", False))
    for rotulo, arquivos, precisa_lido in grupos:
        faltam = [p.name for p in arquivos if not conta(p.name)]
        ok = not faltam
        if precisa_lido and arquivos:
            ok = ok and any(isinstance(mats.get(nfc(p.name)), dict) and mats[nfc(p.name)].get("texto") for p in arquivos)
        out.append((f"{rotulo}: cada arquivo lido (com seção) ou descartado com motivo" + (f"; faltam {faltam[:4]}" if faltam else "")
                    + ("; nenhuma lida" if precisa_lido and arquivos and not faltam and not ok else ""), ok))
    return out



def _nota(blocked):
    return f" ({blocked})" if blocked.startswith("vídeos dispensados") else f" (PENDENTE: {blocked})"


def canais_bloqueados(data):
    """10/10/2026: o YouTube bloqueou transcrições por IP (youtube_transcript_api IpBlocked; yt-dlp 'page needs to be reloaded').
    Não se finge leitura: fontes.json › canais_bloqueados registra data, erro real e ≥ MIN_CANAIS vídeos identificados pela busca
    (canal, url); a pendência aparece no rótulo do gate e no ESTADO-ATUAL, e os vídeos são lidos quando o bloqueio passar."""
    b = data.get("canais_bloqueados") or {}
    # F-20261021-CLAUDE-06: a dispensa de vídeos (F-20261010-CLAUDE-06) foi revogada; só vale o bloqueio real do YouTube.
    videos = [v for v in b.get("videos", []) if str(v.get("url", "")).startswith("https://") and v.get("canal")]
    if b.get("erro") and b.get("em") and len(videos) >= MIN_CANAIS:
        return f"YouTube bloqueado desde {b['em']}, {len(videos)} vídeos a ler"
    return ""


def class_folder(run, data):
    """F-20261009-CLAUDE-02/03: a Morfologia usou só o PDF I (havia II e III com respostas da lista), o Edema e a Ambiental
    ignoraram Edema II, Ambiental II (mudanças climáticas) e as palavras-cruzadas. Toda corrida declara a pasta da aula no
    drive da turma ('pasta_turma': caminho) e cada arquivo de lá está nas evidências (mesmo nome de arquivo) ou em
    'turma_descartados' com motivo; sem pasta, 'pasta_turma': {"nao_ha": "<busca feita>"}."""
    import os
    label = "pasta da aula no drive da turma: todo arquivo lido (evidência) ou descartado com motivo"
    pasta = data.get("pasta_turma")
    if isinstance(pasta, dict):
        return label + " (sem pasta: busca registrada)", bool(str(pasta.get("nao_ha", "")).strip())
    if not pasta or not os.path.isdir(os.path.expanduser(pasta)):
        return label + " (falta 'pasta_turma')", False
    usados = {os.path.basename(str(r.get("arquivo", ""))) for recs in data.get("evidencias", {}).values() if isinstance(recs, list)
              for r in recs if isinstance(r, dict)}
    usados |= {os.path.basename(str(a)) for a in data.get("turma_arquivos_lidos", [])}
    descartados = data.get("turma_descartados", {})
    faltam = [f for f in sorted(os.listdir(os.path.expanduser(pasta))) if not f.startswith(".")
              and f not in usados and not str(descartados.get(f, "")).strip()]
    return label + (f": faltam {faltam[:4]}" if faltam else ""), not faltam

def source_evidence(run, data):
    """Evidência verificável por família, sem aceitar um booleano como leitura.

    Não prova que uma pessoa/IA leu: verifica artefato, integridade, localizador,
    leitura integral declarada e contribuição rastreável ao plano. Ausência de
    fonte essencial bloqueia; ausência opcional exige busca e impacto explícitos.
    """
    evidence = data.get("evidencias", {})
    try:
        plan = json.loads((run / "planejamento.json").read_text())
    except (OSError, ValueError):
        plan = {}
    targets = {t.get("id") for t in plan.get("alvos", []) if isinstance(t, dict) and t.get("id")}
    checks = []
    for family in FONTES_PLANO:
        records = evidence.get(family, [])
        ok = isinstance(records, list) and bool(records)
        for r in records if isinstance(records, list) else []:
            if not isinstance(r, dict):
                ok = False
                continue
            state = r.get("estado")
            if state == "consultada":
                path = run / str(r.get("arquivo", "_"))
                valid_file = path.is_file() and path.stat().st_size > 0
                digest = hashlib.sha256(path.read_bytes()).hexdigest() if valid_file else None
                refs = r.get("alvos", [])
                ok = ok and bool(valid_file and r.get("sha256") == digest
                    and r.get("leitura") == "integral" and r.get("localizador")
                    and r.get("contribuicao") and r.get("lida_antes_da_selecao") is True
                    and isinstance(refs, list) and refs and all(t in targets for t in refs))
                if family == "youtube":
                    ok = ok and bool(r.get("canal") and str(r.get("url", "")).startswith("https://"))
            elif state in {"não localizada", "inacessível", "não aplicável"}:
                # Slides e bibliografia nunca podem ser dispensados por esta rota.
                ok = ok and family not in {"slides", "bibliografia"}
                ok = ok and r.get("essencial") is False and bool(r.get("busca") and r.get("impacto"))
            else:
                ok = False
        # Não aceitar evidência que dispense uma fonte declarada consultada no resumo.
        summary = data.get(family, {})
        if isinstance(summary, dict) and summary.get("estado") == "consultada":
            ok = ok and any(isinstance(r, dict) and r.get("estado") == "consultada" for r in records or [])
        if family in {"slides", "bibliografia"} or (family == "youtube" and not canais_bloqueados(data)):
            ok = ok and any(isinstance(r, dict) and r.get("estado") == "consultada" for r in records or [])
        checks.append((f"fonte obrigatória {family}: leitura integral rastreável e contribuição ao plano", bool(ok)))
    # Cada livro/vídeo declarado precisa estar na evidência, sem duplicar uma
    # transcrição três vezes para passar o mínimo de aulas.
    videos = evidence.get("youtube", [])
    urls = {r.get("url") for r in videos if isinstance(r, dict) and r.get("estado") == "consultada"}
    declared = {c.get("url") for c in data.get("canais", [])}
    blocked = canais_bloqueados(data)
    checks.append(("vídeos distintos e todos rastreados na evidência" + (_nota(blocked) if blocked else ""),
                   bool(len(urls) >= MIN_CANAIS and None not in declared and declared <= urls) or bool(blocked and not data.get("canais"))))
    for key, family, field in (("livros", "bibliografia", "texto"), ("canais", "youtube", "transcricao")):
        paths = {str((run / str(r.get("arquivo", "_"))).resolve()) for r in evidence.get(family, []) if isinstance(r, dict) and r.get("estado") == "consultada"}
        if key == "canais" and blocked and not data.get(key):
            checks.append(("canais: nenhum declarado como lido" + _nota(blocked), True))
            continue
        checks.append((f"{key}: todos os materiais declarados têm evidência", bool(data.get(key)) and all(str((run / str(r.get(field, "_"))).resolve()) in paths for r in data.get(key, []))))
    return checks


def require_sources(run):
    """Bloqueio antes de escrever seleção no Anki; não admite bypass de fontes."""
    run = Path(run)
    try:
        data = json.loads((run / "fontes.json").read_text())
        failed = [label for label, ok in sources(run, data) if ok is not True]
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        raise SystemExit(f"Fontes sem evidência válida: {exc}. Nada instalado.") from exc
    if failed:
        raise SystemExit("Fontes incompletas; nada instalado:\n- " + "\n- ".join(failed))


def coverage(run, plan):
    """Conferência final item a item (F-20261002-CLAUDE-09): todo rótulo/estrutura dos slides, do roteiro prático e dos
    exercícios aparece em cobertura.json com os cards que o cobrem. Item de roteiro ou exercício não pode ser excluído."""
    label = "cobertura.json: todo item de slide, roteiro e exercício com card (conferência final item a item)"
    path = run / "cobertura.json"
    if not path.exists():
        return label, False
    data = json.loads(path.read_text(encoding="utf-8"))
    keys = {e["key"] for e in plan["entries"]} | {f"sh-{n}" for n in plan.get("compartilhados", {})}
    items = data.get("itens", [])
    sources = {str(i.get("fonte", "")).split()[0].lower() for i in items if str(i.get("fonte", "")).strip()}
    # F-20261003-CLAUDE-13: "tem que cobrir bem de acordo com toda a bibliografia": as seções do capítulo do livro
    # também entram, com card ou com motivo de ficar fora (outra aula, fora do recorte)
    ok = bool(items) and data.get("conferido_depois_de_instalar") is True and "slide" in sources and "livro" in sources
    for i in items:
        cards = i.get("cards") or []
        if cards:
            ok = ok and all(c in keys for c in cards)
        else:
            fonte = str(i.get("fonte", "")).lower()  # F-20261013-CLAUDE-03: material de apoio (não prova) pode ficar sem card, com motivo
            ok = ok and bool(str(i.get("excluido", "")).strip()) and (fonte.startswith(("slide", "livro")) or "prova" not in fonte)
    return label.replace("exercício com card", "exercício com card; seções do livro com card ou motivo"), ok


def orphans(run, plan):
    """F-20261009-CLAUDE-02: "tem coisa que não foi dada". Todo card precisa apontar para um item do material de base
    (lâmina, material docente, apostila/monitoria, prova ou livro) em cobertura.json; card sem item é fuga da aula.
    Cards de conexão declaram 'conexao' no spec (ligam dois itens já cobertos)."""
    label = "revisão contra o material de base: todo card ligado a um item ensinado (sem card fora da aula)"
    path = run / "cobertura.json"
    if not path.exists():
        return label, False
    used = {c for i in json.loads(path.read_text(encoding="utf-8")).get("itens", []) for c in (i.get("cards") or [])}
    keys = [e["key"] for e in plan["entries"] if not e.get("conexao")] + [f"sh-{n}" for n in plan.get("compartilhados", {})]
    loose = [k for k in keys if k not in used]
    return label + (f": {len(loose)} sem item ({loose[:5]})" if loose else ""), not loose


def _inventory_items(data):
    """Normaliza os três locais do inventário que podem conter itens atômicos."""
    out = []
    for slide in data.get("slides", []):
        for item in slide.get("itens", []):
            out.append((item, "slide", slide))
    for section in ("exercicios", "capitulo"):
        for entry in data.get(section, []):
            if isinstance(entry, dict) and isinstance(entry.get("itens"), list):
                out.extend((item, section, entry) for item in entry["itens"])
            elif isinstance(entry, dict):
                out.append((entry, section, {}))
    return out


def inventory(run, plan):
    """F-20261004-CODEX-05: cobertura só vale depois do inventário de cada lâmina."""
    label = "inventário atômico: todas as páginas classificadas e cada item de conteúdo ligado ao card instalado"
    path = run / "inventario-aula.json"
    review_path = run / "revisao-inventario.json"
    coverage_path = run / "cobertura.json"
    if not (path.exists() and review_path.exists() and coverage_path.exists()):
        return label, False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        review = json.loads(review_path.read_text(encoding="utf-8"))
        covered = json.loads(coverage_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return label, False
    slides = data.get("slides", [])
    if not data.get("lido_antes_da_selecao") or not slides:
        return label, False
    numbers = [s.get("numero") for s in slides if isinstance(s, dict)]
    if (len(numbers) != len(slides) or len(set(numbers)) != len(numbers)
            or not all(isinstance(n, int) for n in numbers)
            or numbers != list(range(numbers[0], numbers[0] + len(numbers)))):
        return label, False
    source_file = run / "fontes.json"
    if source_file.exists():
        try:
            source = json.loads(source_file.read_text(encoding="utf-8"))
            pdf = run / source.get("slides", {}).get("arquivo", "_")
            if pdf.is_file() and pdf.suffix.lower() == ".pdf":
                import fitz
                with fitz.open(pdf) as doc:
                    if len(doc) != len(slides):
                        return label, False
        except (json.JSONDecodeError, OSError, ImportError):
            return label, False
    if any(s.get("classe") not in CLASSES_SLIDE or
           (s.get("classe") == "conteudo" and not s.get("itens")) or
           (s.get("classe") != "conteudo" and not str(s.get("justificativa", "")).strip())
           for s in slides):
        return label, False
    atomic = _inventory_items(data)
    ids = [i.get("id") for i, _, _ in atomic if isinstance(i, dict)]
    if not ids or len(ids) != len(atomic) or len(set(ids)) != len(ids):
        return label, False
    planning_file = run / "planejamento.json"
    if planning_file.exists():
        try:
            targets = json.loads(planning_file.read_text(encoding="utf-8")).get("alvos", [])
            if {t.get("id") for t in targets} != set(ids):
                return label, False
        except (json.JSONDecodeError, OSError):
            return label, False
    entries = {e["key"]: e for e in plan.get("entries", [])}
    entries.update({f"sh-{n}": {} for n in plan.get("compartilhados", {})})
    cov = {i.get("id"): i for i in covered.get("itens", []) if i.get("id")}
    reviewed = review.get("itens", {})
    for item, source, _ in atomic:
        rec = cov.get(item["id"], {})
        cards = rec.get("cards") or []
        excluded = str(rec.get("excluido", "")).strip()
        if cards:
            if not all(card in entries for card in cards):
                return label, False
        elif not (excluded and item.get("exclusao_permitida") is True
                  and (source == "slide" or (source in ("livro", "capitulo") and "aula" in excluded.lower())
                       or item.get("apoio") is True)):  # F-20261012-CLAUDE-01; apoio (não prova) por F-20261013-CLAUDE-03
            return label, False
        verdict = reviewed.get(item["id"], {})
        if verdict.get("veredito") not in ("ok", "corrigido") or not str(verdict.get("card_visto", "")).strip():
            return label, False
        if item.get("visual") == "necessaria" and cards:
            if not any(has_img(entries[c]) for c in cards if c in entries) and not str(rec.get("sem_imagem", "")).strip():
                return label, False
    return label, review.get("feita_depois_de_instalar") is True


def specific_extras(plan):
    """Recusa o texto-modelo que tornou Extras intercambiáveis entre aulas."""
    label = "Extra específico da aula em cada card externo (sem texto-modelo reutilizado)"
    bad = []
    for entry in plan.get("entries", []):
        if entry.get("origin") == "Autoral":
            continue
        fields = entry.get("fields", {})
        raw = fields.get("Extra", "") or fields.get("Back Extra", "")
        clean = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw))).strip().lower()
        if any(phrase in clean for phrase in GENERIC_EXTRAS):
            bad.append(entry.get("key", "?"))
    return label + (f": {bad[:4]}" if bad else ""), not bad


FONTES_PLANO = ("slides", "bibliografia", "caoc", "youtube", "veteranos", "provas", "exercicios")
REVISAO = ("cobertura_item_a_item", "ordem_estrita_dos_slides", "imagens_vistas", "autorais_conferidos_no_livro", "autoral_sem_duplicar_alvo",
           "dope_so_sem_alternativa", "sem_credito_visivel", "ingles_nos_cards", "hy_verde", "tab_lido_por_amostra", "erros_anteriores_do_memory")


def answers(entry):
    """Respostas que a entrada cobra: clozes do texto, nome em negrito do verso das oclusões, rótulos de prancha."""
    import html, re
    fields = entry.get("fields", {})
    clean = lambda v: re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v))).strip().lower())
    out = [clean(m.split("::")[0]) for m in re.findall(r"\{\{c\d+::(.*?)\}\}", fields.get("Text", ""), flags=re.S)]
    bold = re.match(r"\s*<b>(.*?)</b>", fields.get("Remarks", ""), flags=re.S)
    if bold: out.append(clean(bold.group(1)))
    out += [clean(v) for k, v in fields.items() if re.fullmatch(r"\d+a", k) and v.strip()]
    return [a for a in out if len(a) > 3]


def planning(run):
    label = "planejamento.json: alvos por slide a partir de todas as fontes de direcionamento, antes de montar o deck"
    path = run / "planejamento.json"
    if not path.exists():
        return label, False
    data = json.loads(path.read_text(encoding="utf-8"))
    sources = data.get("fontes", {})
    ok = all(sources.get(k, {}).get("estado") in ESTADOS and str(sources[k].get("contribuicao", "")).strip() for k in FONTES_PLANO)
    targets = data.get("alvos", [])
    ok = ok and len(targets) >= 5 and all(str(t.get("slide", "")).strip() and t.get("alvo") and t.get("fontes") and t.get("origem_prevista") for t in targets)
    return label, bool(ok)


def final_review(run):
    label = "revisao-final.json: cada checagem da revisão final feita no deck instalado, com evidência"
    path = run / "revisao-final.json"
    if not path.exists():
        return label, False
    data = json.loads(path.read_text(encoding="utf-8"))
    # Sem Tab (Codex depois): o Tab fica 'pendente' e nunca é declarado lido (EXECUCAO passo 6.3)
    sem_tab = os.environ.get("NEBLI_SEM_TAB") == "1"
    feito = lambda k: (data.get(k, {}).get("ok") is True and str(data[k].get("evidencia", "")).strip()) or (
        sem_tab and k == "tab_lido_por_amostra" and str(data.get(k, {}).get("pendente", "")).strip())
    ok = all(feito(k) for k in REVISAO)
    return label, bool(ok and data.get("feita_depois_de_instalar") is True)


def frontier_cases(run):
    """F-20261014-CLAUDE-02: “Registre casos de fronteira para calibrarmos a profundidade.”
    Só vale para corridas com percurso-aula.md (PLANO-CARDS-TABS); a seção pode dizer “nenhum”."""
    path = run / "percurso-aula.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    ok = any(line.lstrip("#").strip().lower().startswith("casos de fronteira")
             for line in text.splitlines() if line.startswith("#"))
    return ("percurso-aula.md: seção “Casos de fronteira” (profundidade em dúvida, decisão e motivo)", ok)


def card_review(run, plan):
    """F-20261003-CLAUDE-15: "sinto que ainda falta a revisão final do deck". Cada card do deck vivo (notas da aula e
    compartilhados) é lido depois de instalar e recebe veredito em revisao-final.json["cards"][chave]:
    {"veredito": "ok" | "corrigido", "nota": "<o que foi visto ou mudado>"}; "corrigido" exige a nota."""
    label = "revisão final card a card no deck instalado (revisao-final.json 'cards')"
    path = run / "revisao-final.json"
    if not path.exists():
        return label, False
    cards = json.loads(path.read_text(encoding="utf-8")).get("cards", {})
    keys = [e["key"] for e in plan["entries"]] + [f"sh-{n}" for n in plan.get("compartilhados", {})]
    missing = [k for k in keys if k not in cards]
    bad = [k for k, v in cards.items() if v.get("veredito") not in ("ok", "corrigido") or (v.get("veredito") == "corrigido" and not str(v.get("nota", "")).strip())]
    if missing or bad:
        label += f": faltam {len(missing)}" + (f", sem nota {bad[:3]}" if bad else "")
    return label, not missing and not bad


CLOZE_RE = re.compile(r"\{\{c\d+::((?:(?!\}\}).)*?)\}\}", re.S)
PARTIAL = re.compile(r"[A-Za-z]\{\{c\d+::|\}\}[A-Za-z]")
BAD_HINT = re.compile(r"^(s|x|related.*|all .*|\d+)$", re.I)


IMG = re.compile(r'<img[^>]+src="([^"]+)"', re.I)
SLIDE_IMG = re.compile(r"^nebli-uc\d+-[a-z]+\d*-(s|p)\d+", re.I)


def has_img(e):
    f = e.get("fields") or {}
    return any(IMG.search(f.get(k, "") or "") for k in f)


def only_slide_img(e):
    f = e.get("fields") or {}
    srcs = [m for k in f for m in IMG.findall(f.get(k, "") or "")]
    return bool(srcs) and all(SLIDE_IMG.match(x) for x in srcs)


def visible(e):
    t = (e.get("fields") or {}).get("Text", "") or ""
    t = CLOZE_RE.sub(lambda m: m.group(1).split("::")[0], t)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t))).strip()


def bad_cloze(e):
    t = (e.get("fields") or {}).get("Text", "") or ""
    if e.get("origin") == "AnKing" or (e.get("kind") == "text" and e.get("manter")):  # AnKing e acervos externos originais (16/10) ficam como são
        return False
    if PARTIAL.search(t):
        return True
    if any(re.search(r"\b(or|ou)\b", re.sub(r"<[^>]+>", " ", m.split("::")[0]), re.I) for m in CLOZE_RE.findall(t)):
        return True  # comentários de Davi (F-15): cloze de um termo, nunca "x ou y"
    return any("::" in m and BAD_HINT.match(m.split("::", 1)[1].strip()) for m in CLOZE_RE.findall(t))


def past_errors(plan):
    """Erros apontados por Davi em F-20261002-CLAUDE-10 viram reprovação."""
    entries = plan["entries"]
    dope = [e["key"] for e in entries if e.get("origin") == "Dope" and not str(e.get("sem_alternativa", "")).strip()]
    others = {}
    for e in entries:
        if e.get("origin") != "Autoral":
            for a in answers(e): others.setdefault(a, e["key"])
    dup = [e["key"] for e in entries if e.get("origin") == "Autoral" and not str(e.get("duplicacao_ok", "")).strip()
           and any(a == o or (min(len(a), len(o)) >= 8 and (a in o or o in a)) for a in answers(e) for o in others)]
    legend = [e["key"] for e in entries if e.get("kind") == "slideio" and e.get("aponta") != "estrutura"]
    blocks = {}
    for e in entries:
        b = blocks.setdefault(e.get("bloco"), {"slides": set(), "texto": 0})
        b["slides"].add(str(e.get("evid", "")).split(";")[0])
        b["texto"] += e.get("kind") in ("text", "autoral")
    thin = [k for k, b in blocks.items() if b["texto"] < len(b["slides"])]
    # F-20261003-CLAUDE-13: oclusão do slide é autoral (busca antes) e mascara o rótulo inteiro (verso mostra o nome todo)
    ios = [e for e in entries if e.get("kind") == "slideio"]
    cut = [e["key"] for e in ios if not str(e.get("rotulo", "")).strip() or e.get("parcial")]
    unsearched = [e["key"] for e in ios if not str(e.get("busca", "")).strip()]
    extra = [("oclusão do slide com rótulo inteiro, refeita pelo slide_io r2 (nenhum nome cortado)" + (f": {cut[:4]} (+{len(cut) - 4})" if len(cut) > 4 else f": {cut}" if cut else ""), not cut),
             ("oclusão do slide só depois de procurar o alvo no AnKing e nos externos (campo 'busca')" + (f": faltam {len(unsearched)}" if unsearched else ""), not unsearched),
             ("oclusão do slide aponta uma estrutura na figura (não legenda/lista ao lado)" + (f": {legend[:4]}" if legend else ""), not legend),
             ("cada bloco tem cards de texto (função, relação, definição), não só identificação" + (f": {thin}" if thin else ""), not thin)]
    # F-20261003-CLAUDE-14: card enorme não tem repetição espaçada; Histology entra recortado; cloze limpo
    big = [e["key"] for e in entries if e.get("origin") != "AnKing" and e.get("kind") in ("text", "autoral") and len(visible(e)) > MAX_TEXTO]
    hxlong = [e["key"] for e in entries if e.get("origin") == "Histology" and e.get("manter")]
    badcz = [e["key"] for e in entries if bad_cloze(e)]
    # F-20261020-CODEX-03: "negrito" em todos os autorais, conferido card a card.
    sem_negrito = []
    for e in entries:
        if e.get("origin") != "Autoral" and e.get("kind") != "autoral":
            continue
        txt = (e.get("fields") or {}).get("Text", "") or ""
        clozes = CLOZE_RE.findall(txt)
        if any(not re.search(r"<(?:b|strong)>", c, re.I) for c in clozes):
            sem_negrito.append(e["key"])
    extra += [(f"card curto: texto visível ≤ {MAX_TEXTO} caracteres fora do AnKing" + (f" (longos: {big[:4]})" if big else ""), not big),
              ("nota do Histology entra recortada em cards de uma frase (nebli.hx_cortes)" + (f": {hxlong[:4]}" if hxlong else ""), not hxlong),
              ("cloze de palavra inteira, sem 'x ou y' nem dica '::s/::x/::related/::all/::número' fora do AnKing" + (f": {badcz[:4]}" if badcz else ""), not badcz)]
    extra += [("[duro] toda resposta de cloze autoral está em negrito, conferida card a card"
               + (f": {sem_negrito[:6]}" if sem_negrito else ""), not sem_negrito)]
    # F-20261003-CLAUDE-15: "tá faltando comentário": todo card tem no verso uma explicação curta, não só figura
    def back_text(e):
        f = e.get("fields") or {}
        return re.sub(r"\s+|&nbsp;|/", "", html.unescape(re.sub(r"<[^>]+>", "", f.get("Extra", "") or f.get("Back Extra", "") or "")))
    bare = [e["key"] for e in entries if e.get("kind") in ("text", "autoral") and not back_text(e)]
    longcz = [e["key"] for e in entries if e.get("origin") != "AnKing" and e.get("kind") in ("text", "autoral") and not (e.get("kind") == "text" and e.get("manter"))
              and any(len(re.sub(r"<[^>]+>", " ", m.split("::")[0]).split()) > MAX_CLOZE for m in CLOZE_RE.findall((e.get("fields") or {}).get("Text", "") or ""))]
    extra += [(f"cloze curto (até {MAX_CLOZE} palavras) fora do AnKing" + (f": {longcz[:4]}" if longcz else ""), not longcz)]
    extra += [("verso com explicação curta (não só figura)" + (f": faltam {len(bare)} ({bare[:3]})" if bare else ""), not bare)]
    # F-20261003-CLAUDE-15: card de estrutura leva imagem (livro da UC ou AnKing; slide só sem alternativa)
    if re.search(r"anatomia|biologia-tecidual|patologia|radiologia", plan.get("lesson_id", "")):
        noimg = [e["key"] for e in entries if e.get("kind") in ("text", "autoral") and not has_img(e) and not str(e.get("sem_imagem", "")).strip()]
        slide_only = [e["key"] for e in entries if e.get("kind") in ("text", "autoral") and has_img(e) and only_slide_img(e)
                      and not str(e.get("slide_sem_alternativa", "")).strip()]
        extra += [("card de estrutura com imagem no verso (ou 'sem_imagem' com motivo)" + (f": faltam {len(noimg)} ({noimg[:3]})" if noimg else ""), not noimg),
                  ("imagem de livro ou AnKing; do slide só com 'slide_sem_alternativa'" + (f": {len(slide_only)} ({slide_only[:3]})" if slide_only else ""), not slide_only)]
    extra += images_checked(plan)
    return [(f"Dope Anatomy só sem alternativa (sem justificativa: {dope[:5]})" if dope else "Dope Anatomy só sem alternativa, justificada", not dope),
            (f"autoral não repete alvo já cobrado no deck (conferir: {dup[:6]})" if dup else "autoral não repete alvo já cobrado no deck", not dup)] + extra


RUN = {"dir": None}


def images_checked(plan):
    """F-20261003-CLAUDE-19: "imagens do livro não são boas [...] cortar aquele texto ao lado das imagens"; "qualidade da
    imagem importante e intencionalidade também". Toda imagem de card fora do AnKing (livro, acervo externo, slide) é vista
    e julgada em imagens-vistas.json {src: {"qualidade": "boa"|"aceitável", "intencao": "<o que mostra do alvo>"}};
    figura com versão recortada em imagens-recortadas.json não pode continuar com a original."""
    run = RUN["dir"]
    seen = json.loads((run / "imagens-vistas.json").read_text()) if run and (run / "imagens-vistas.json").exists() else {}
    cropped = json.loads((run / "imagens-recortadas.json").read_text()) if run and (run / "imagens-recortadas.json").exists() else {}
    srcs, raw = set(), set()
    for e in plan["entries"]:
        if e.get("kind") == "slideio":
            continue
        for v in (e.get("fields") or {}).values():
            for m in IMG.findall(v or ""):
                if e.get("origin") == "AnKing" and m not in plan.get("media", {}):
                    continue
                srcs.add(m)
                if m in cropped:
                    raw.add(m)
    unseen = sorted(s for s in srcs if not (isinstance(seen.get(s), dict) and seen[s].get("qualidade") in ("boa", "aceitável")
                                            and str(seen[s].get("intencao", "")).strip()))
    return [("imagens fora do AnKing vistas e julgadas (qualidade e intenção, imagens-vistas.json)" + (f": faltam {len(unseen)} ({unseen[:3]})" if unseen else ""), not unseen),
            ("figura de livro recortada, só a imagem (sem título nem legenda ao lado)" + (f": {sorted(raw)[:3]}" if raw else ""), not raw)]


def plan_checks(run, plan):
    from nebli import lint_cards
    out = []
    entries = plan["entries"]
    out.append(("plano contém cards", bool(entries)))
    cards = lambda es: sum(len(e.get("cards", [])) or 1 for e in es)
    authored = [e for e in entries if e.get("origin") == "Autoral"]
    share = cards(authored) / max(1, cards(entries))
    exception = AUTHOR_EXCEPTIONS.get(plan.get("lesson_id"))
    completude = COMPLETUDE_EXCEPTIONS.get(plan.get("lesson_id"))
    # A porcentagem sinaliza nova revisão da busca; não decide a cobertura da aula.
    # Lint, inventário e órfãos continuam como gates separados. Para proporção alta,
    # cada autoral precisa deixar rastreável a busca e os espelhos que o motivaram.
    allowed = author_volume_supported(plan)
    suffix = (f"; completude: {completude}" if completude and share > MAX_AUTORAL
              else f"; exceção histórica {exception}" if exception and share > MAX_AUTORAL else "")
    if pipeline_novo(run, plan):  # F-20261015-CLAUDE-06: exceções de completude não valem; vale a prova de lacuna por autoral
        out += cobertura_anking(run, plan)
        out += cores_rubrica(plan) + inducao_clozes(plan)  # F-20261016-CLAUDE-01
        out += escopo_basico(run, plan)  # F-20261021-CLAUDE-01
        out += linha_e_provas(run, plan)  # F-20261021-CLAUDE-02
        out += exemplares_lidos(run)  # F-20261021-CLAUDE-06
    else:
        out.append((f"autoria {share:.0%} dos cards; acima de {MAX_AUTORAL:.0%} exige busca externa e espelhos por autoral{suffix}", allowed))
    if "biologia-tecidual" in plan.get("lesson_id", ""):  # F-20261003-CLAUDE-13: aprender, não visualizar em excesso
        ident = cards([e for e in entries if e.get("kind") == "slideio" or e.get("identificacao")]) / max(1, cards(entries))
        out.append((f"histologia: teoria é maioria; identificação por imagem {ident:.0%} dos cards (teto {MAX_IDENT_HISTO:.0%})", ident <= MAX_IDENT_HISTO))
        # F-20261003-CODEX-20: haustros são anatomia macroscópica, sem objetivo histológico na BT04.
        if "bt04" in plan.get("lesson_id", ""):
            off_scope = [e["key"] for e in entries if "haustra" in str(e.get("alvo", "")).lower()
                         or e["key"] == "grosso-mucosa-haustros"]
            out.append(("BT04 sem card cujo alvo é apenas haustros (anatomia macroscópica)"
                        + (f": {off_scope[:3]}" if off_scope else ""), not off_scope))
    hard = [key for key, text, extra, extra_problems in lint_cards.from_plan(run / "plan.json")
            if any(level == "dura" for level, _ in (lint_cards.check(key, text, extra) if text else []) + extra_problems)]
    out.append(("lint dos autorais sem reprovação dura (busca nos externos, espelhos, forma AnKing)", not hard))
    orders = [e.get("order") for e in entries]
    out.append(("ordem da aula: toda entrada com posição e slide em 'evid'", all(orders) and all(str(e.get("evid", "")).lower().startswith("slide") for e in entries)))
    from nebli import ordem, rotulos
    slides = [ordem.slide(e.get("evid")) for e in sorted(entries, key=lambda e: e.get("order") or 0)]
    # F-20261021-CLAUDE-05: o deck acompanha a aula como foi dada; quando o professor não segue a ordem do PDF, escopo.json declara
    # 'ordem_da_fala' (faixas de lâminas na ordem falada, conferida na transcrição) e a ordem estrita vale dentro dessa sequência.
    try:
        faixas = json.loads((run / "escopo.json").read_text(encoding="utf-8")).get("ordem_da_fala") or []
    except (OSError, ValueError):
        faixas = []
    def chave(s):
        for i, f in enumerate(faixas):
            if f[0] <= s <= f[1]:
                return (i, s)
        return (len(faixas), s)
    ks = [chave(s) for s in slides if s]
    out.append(("ordem estrita dos slides no plano (nenhum recuo; na ordem falada se 'ordem_da_fala' declarada no escopo.json)",
                all(slides) and all(a <= b for a, b in zip(ks, ks[1:]))))
    out.append(coverage(run, plan))
    out.append(orphans(run, plan))
    out.append(inventory(run, plan))
    out.append(planning(run))
    out.append(final_review(run))
    frontier = frontier_cases(run)
    if frontier:
        out.append(frontier)
    out.append(card_review(run, plan))
    out += past_errors(plan)
    out.append(specific_extras(plan))
    out.append(("cada cor justificada em 'motivo'", all(str(e.get("motivo", "")).strip() for e in entries)))
    out.append(("REVISAO-DE-QUALIDADE.md na corrida", (run / "REVISAO-DE-QUALIDADE.md").exists()))
    return out


# ---------------------------------------------------------------------------------------------------------------
# F-20261015-CLAUDE-06 — pipeline AnKing-primeiro, gates duros. Davi: "criar autoral SÓ PARA LACUNAS REAIS […] em último
# do último caso (gate-hard nisso)"; "SEMPRE BUSCA EM TODOS ESSES DECKS DE REF EXTERNA - GATE HARD, UM DECK NÃO PODE
# TERMINAR SEM PASSAR POR TODOS ESSES GATES HARDS"; "pode puxar todos os irmãos, eu suspendo". Prova autoral por autoral
# de que nenhum acervo tinha o card e, desde F-20261016-CLAUDE-04, teto de autoral (MAX_AUTORAL; exceção até MAX_AUTORAL_EXCECAO).
PIPELINE_DESDE = 20261016
COB_COLS = ["chave", "conceito", "fonte_aula", "veredito", "lidos", "decora", "decisao"]
FONTE_AULA = re.compile(r"slide|l[âa]mina|prova|apostila|monitoria|transcri|exerc[íi]cio|palavras|gabarito|caso", re.I)


def pipeline_novo(run, plan):
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", Path(run).name)
    return plan.get("pipeline") == "anking-primeiro" or bool(m and int("".join(m.groups())) >= PIPELINE_DESDE)


def _norm(s):
    return re.sub(r"[^a-z0-9α-ω]+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or "")).lower()).strip()


def _jsonl(path):
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


MAX_AUTORAL = 0.20          # F-20261016-CLAUDE-04: autoral é caso especial; acervos (AnKing e externos) têm prioridade máxima
MAX_AUTORAL_EXCECAO = 0.30  # teto absoluto, mesmo com AUTORAL_EXCECAO ("aula introdutória" não basta: a 03, com 68%, foi o excesso)
LEGADO_V2 = {"deck-aula-uc03-pt09-lesao-celular-v2-2026-10-15", "deck-aula-uc03-rd02-diagnostico-radiologico-v2-2026-10-16",
             "deck-aula-uc03-pt03-diagnostico-patologico-v2-2026-10-16"}  # entregues antes do teto


def escopo_basico(run, plan):
    """F-20261021-CLAUDE-01 (feedback do deck 58): (1) “isso é ciclo básico ou clínico?” = básico, declarado em escopo.json;
    (2) clínica lateral (ajuda, mas não é da aula) ≤ 7% dos cards, ≤ 5% se só ilustra princípios, salvo clínica como tema da aula
    (apostila e livro); (3) autoral com cloze único ≤ 50% dos autorais (excesso = escrita fraca, longe dos EXEMPLARES)."""
    run = Path(run)
    out = []
    path = run / "escopo.json"
    d = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    ciclo_ok = str(d.get("ciclo", "")).strip().lower() in ("básico", "basico") and len(str(d.get("justificativa", "")).strip()) >= 40
    entries = plan.get("entries", [])
    n = lambda e: len(e.get("cards", [])) or 1
    total = sum(n(e) for e in entries) + sum(v.get("n_cards", 1) for v in (plan.get("compartilhados") or {}).values())
    lat = set(d.get("clinica_lateral", []))
    desconhecidas = [k for k in lat if k not in {e["key"] for e in entries} and k not in (plan.get("compartilhados") or {}) and not str(k).startswith("sh-")]
    cl = sum(n(e) for e in entries if e["key"] in lat) + sum(v.get("n_cards", 1) for k, v in (plan.get("compartilhados") or {}).items() if f"sh-{k}" in lat)
    tema = bool(d.get("clinica_e_tema")) and len(str(d.get("motivo_tema", "")).strip()) >= 40
    teto = 0.07 if tema else 0.05
    share = cl / max(1, total)
    lat_ok = share <= teto and not desconhecidas and "clinica_lateral" in d
    lat_msg = f"clínica lateral {share:.0%} (teto {teto:.0%}; 7% só se a clínica é tema, com motivo)" + (f"; chaves desconhecidas {desconhecidas[:3]}" if desconhecidas else "")
    DOENCA = re.compile(r"pênfigo|goodpasture|graves|miastenia|l[úu]pus|artrite|poliarterite|febre reum|anemia pernic|glomerulonefrite|diabetes|asma|rinite|anafilaxia|dermatite|trombocitopenia|anemia hemol|doença hemol|transfus|esclerose|hepatite|tuberculose|psor[ií]ase|crohn|vasculite", re.I)
    nd = sum(n(e) for e in entries if DOENCA.search(str(e.get("alvo", "")))) + sum(v.get("n_cards", 1) for v in (plan.get("compartilhados") or {}).values() if DOENCA.search(str(v.get("alvo", ""))))
    out.append((f"[duro] ciclo básico (escopo.json: básico + justificativa; {lat_msg}; doenças no alvo {nd/max(1, total):.0%}, máx. 10%: mecanismo geral, não lista de doenças)",
                bool(ciclo_ok and lat_ok and nd / max(1, total) <= 0.10)))
    aut = [e for e in entries if e.get("origin") == "Autoral"]
    unico = [e for e in aut if len(e.get("cards", [])) <= 1]
    return out


def linha_e_provas(run, plan):
    """F-20261021-CLAUDE-02: (1) todas as fontes (aula, prova, bibliografia, apostila) alimentam cards declarados em escopo.json;
    (2) o deck explica a aula numa linha lógica, com progressão do mecanismo (passos em ordem, cada um com cards, na ordem do deck);
    (3) calibrado com as provas: toda questão não-eco do índice da aula liga a cards ou tem motivo de ficar fora."""
    run = Path(run)
    path = run / "escopo.json"
    d = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    entries = {e["key"]: e for e in plan.get("entries", [])}
    comp = plan.get("compartilhados") or {}
    alias = {f"ak{v.get('source_nid')}": f"sh-{k}" for k, v in comp.items() if v.get("source_nid")}  # card compartilhado também por ak<nid original>
    def ordem(k):
        k = alias.get(k, k)
        if k in entries:
            return int(entries[k].get("order", 0))
        m = re.search(r"(\d+)$", str((comp.get(str(k)[3:]) or {}).get("ordem_tag", "")))
        return int(m.group(1)) if m else None
    valido = lambda k: k in entries or (alias.get(k, k).startswith("sh-") and alias.get(k, k)[3:] in comp)
    out = []
    uso = d.get("uso_das_fontes", {})
    faltam = [f for f in ("aula", "prova", "bibliografia", "apostila")
              if not (isinstance(uso.get(f), list) and uso[f] and all(valido(k) for k in uso[f]))]
    out.append((f"[duro] fontes usadas nos cards (aula, prova, bibliografia, apostila), cada uma com cards válidos em escopo.json 'uso_das_fontes'" +
                (f": faltam {faltam}" if faltam else ""), not faltam))
    passos = d.get("linha_logica", [])
    ok = isinstance(passos, list) and len(passos) >= 4
    pos = []
    for p_ in passos if ok else []:
        ks = p_.get("cards") if isinstance(p_, dict) else None
        if not (isinstance(ks, list) and ks and all(valido(k) for k in ks) and len(str(p_.get("passo", "")).strip()) >= 25):
            ok = False
            break
        pos.append(min(o for o in (ordem(k) for k in ks) if o is not None) if any(ordem(k) is not None for k in ks) else None)
    ok = ok and None not in pos and pos == sorted(pos)
    mecan = sum(1 for p_ in passos if isinstance(p_, dict) and p_.get("mecanismo") is True) if ok else 0
    out.append((f"[duro] linha lógica: a aula explicada em ≥4 passos encadeados (causa→efeito), cada um com cards, em ordem no deck; {mecan} passos de mecanismo (mín. 3)",
                ok and mecan >= 3))
    hist_ok = len(str(d.get("historia", "")).strip()) >= 200 and isinstance(passos, list) and all(
        isinstance(p_, dict) and (i == len(passos) - 1 or len(str(p_.get("liga_ao_proximo", "")).strip()) >= 20) for i, p_ in enumerate(passos))
    conex = d.get("cards_de_conexao", [])
    total = sum(len(e.get("cards", [])) or 1 for e in entries.values()) + sum(v.get("n_cards", 1) for v in comp.values())
    ncon = sum((len(entries[k].get("cards", [])) or 1) for k in conex if k in entries) if isinstance(conex, list) else 0
    no_passo = {k for p_ in passos if isinstance(p_, dict) for k in p_.get("cards", [])} if isinstance(passos, list) else set()
    con_ok = (isinstance(conex, list) and len(conex) >= 2 and all(k in entries and entries[k].get("origin") == "Autoral" and k in no_passo for k in conex)
              and 0.02 <= ncon / max(1, total) <= 0.10)
    out.append((f"[duro] o deck conta uma história: 'historia' (≥200 caracteres), 'liga_ao_proximo' em cada passo e cards de conexão autorais (2–10%, hoje {ncon}/{total}) dentro dos passos",
                bool(hist_ok and con_ok)))
    arquivos = sorted((run / "fontes").glob("provas*"))
    texto = "\n".join(a.read_text(encoding="utf-8", errors="ignore") for a in arquivos)
    ids, eco = [], set()
    for m in re.finditer(r"^── \[([^\]]+)\] (\S+)([^\n]*)", texto, re.M):
        i = f"{m.group(1).strip()} {m.group(2)}"
        ids.append(i)
        if "[eco" in m.group(3):
            eco.add(i)
    ids = list(dict.fromkeys(ids))
    reg = {str(x.get("id")): x for x in d.get("provas", []) if isinstance(x, dict)}
    pend = []
    for i in ids:
        r = reg.get(i)
        if r is None:
            if i in eco:
                continue
            pend.append(i); continue
        if r.get("cards"):
            if not all(valido(k) for k in r["cards"]):
                pend.append(i)
        elif len(str(r.get("fora", "")).strip()) < 30:
            pend.append(i)
    out.append((f"[duro] calibrado com as provas: {len(ids)} questões do índice, cada uma (menos ecos) com cards ou 'fora' justificado em escopo.json 'provas'" +
                (f"; pendentes {pend[:4]}" if pend else ""), bool(ids) and not pend))
    return out


def exemplares_lidos(run):
    """F-20261021-CLAUDE-06: ler EXEMPLARES e ANTI-EXEMPLARES é gate duro. `exemplares-lidos.json` na corrida guarda o sha256 dos dois
    arquivos vigentes (relidos nesta corrida) e ≥ 5 aprendizados concretos (≥ 50 caracteres) que vão orientar a escrita dos autorais."""
    import hashlib
    base = Path(__file__).resolve().parent.parent / "flashcards" / "projeto"
    path = Path(run) / "exemplares-lidos.json"
    d = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    sha = lambda f: hashlib.sha256((base / f).read_bytes()).hexdigest()
    ok = (d.get("exemplares_sha256") == sha("EXEMPLARES-CARDS.md") and d.get("anti_exemplares_sha256") == sha("ANTI-EXEMPLARES-CARDS.md")
          and isinstance(d.get("aprendizados"), list) and sum(1 for x in d["aprendizados"] if len(str(x).strip()) >= 50) >= 5)
    return [("[duro] EXEMPLARES e ANTI-EXEMPLARES lidos nesta corrida (exemplares-lidos.json: sha256 vigente + ≥ 5 aprendizados)", bool(ok))]


def cobertura_anking(run, plan):
    from nebli import semantica
    run = Path(run)
    out = []
    entries = plan.get("entries", [])
    keys = {e["key"]: e for e in entries}
    autorais = [e for e in entries if e.get("origin") == "Autoral"]
    # Rota (a): palavra-chave em AnKing e externos (nebli.busca_acervos)
    kw = run / "busca" / "anking.txt"
    kwtxt = kw.read_text(encoding="utf-8") if kw.exists() else ""
    out.append(("[duro] rota (a) palavra-chave em AnKing E Referências Externas (busca/anking.txt)",
                "| AnKing |" in kwtxt and "| Externos |" in kwtxt))
    # Rota (b): seções de recurso lidas inteiras
    sec = _jsonl(run / "busca" / "secoes.jsonl")
    out.append(("[duro] rota (b) seções de recurso do AnKing lidas (busca/secoes.jsonl)" + (f": {len(sec)}" if sec else ""),
                bool(sec) and all((run / x["arquivo"]).exists() for x in sec)))
    # Rota (c): significado, em TODOS os acervos
    sem = _jsonl(run / "busca" / "semantica.jsonl")
    todos = set(semantica.ACERVOS)
    if int(plan.get("pipeline_versao") or 1) >= 2:  # F-20261016-CLAUDE-03: também os decks NEBLI vivos (sem repetir entre aulas)
        todos = todos | {"NEBLI-vivo"}
    falta_acervo = [x["chave"] for x in sem if not todos <= set(x.get("acervos", []))]
    out.append(("[duro] rota (c) busca por significado em todos os acervos (AnKing + cada deck de Referências Externas)"
                + (f": consultas sem algum acervo {falta_acervo[:3]}" if falta_acervo else ""), bool(sem) and not falta_acervo))
    # Matriz de cobertura
    cob_path = run / "busca" / "cobertura.tsv"
    rows = {}
    if cob_path.exists():
        lines = [l.split("\t") for l in cob_path.read_text(encoding="utf-8").splitlines() if l.strip()]
        if lines and [c.strip() for c in lines[0]] == COB_COLS:
            rows = {r[0].strip(): dict(zip(COB_COLS, [c.strip() for c in r] + [""] * 7)) for r in lines[1:]}
    out.append(("[duro] busca/cobertura.tsv com cabeçalho " + "|".join(COB_COLS), bool(rows)))
    sem_linha = [k for k in keys if k not in rows]
    out.append(("[duro] todo card do plano tem linha na matriz de cobertura" + (f": faltam {sem_linha[:4]}" if sem_linha else ""),
                bool(rows) and not sem_linha))
    vered = [k for k, r in rows.items() if r["veredito"] not in ("coberto", "parcial", "lacuna")]
    out.append(("[duro] veredito coberto|parcial|lacuna em cada linha" + (f": {vered[:4]}" if vered else ""), bool(rows) and not vered))
    # Autoral: só lacuna/parcial, com prova da busca, fonte da aula e cloze no nome decorado
    vistos = {}
    for x in sem:
        vistos.setdefault(x["chave"], set()).update(str(t["nid"]) for t in x.get("top", []))
    ruins = {}
    for e in autorais:
        k = e["key"]; r = rows.get(k); prob = []
        if not r:
            prob.append("sem linha")
        else:
            if r["veredito"] not in ("lacuna", "parcial"):
                prob.append("veredito não é lacuna/parcial")
            if k not in vistos:
                prob.append("sem busca por significado com esta chave")
            lidos = re.findall(r"\d{10,}", r["lidos"])
            if len(lidos) < 3 or not set(lidos) <= vistos.get(k, set()):
                prob.append("menos de 3 candidatos lidos da busca desta chave")
            if not FONTE_AULA.search(r["fonte_aula"]):
                prob.append("fonte da aula ausente (livro sozinho não origina autoral)")
            clozes = [_norm(c) for c in re.findall(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", e.get("fields", {}).get("Text", ""))]
            if not r["decora"] or _norm(r["decora"]) not in clozes:
                prob.append("'decora' não é a resposta de um cloze")
            if len(r["decisao"]) < 25:
                prob.append("decisão sem motivo de os candidatos não servirem")
        if prob:
            ruins[k] = prob
    out.append((f"[duro] cada autoral ({len(autorais)}) prova lacuna: busca nos 3 caminhos, 3+ candidatos lidos, fonte da aula, cloze no nome decorado"
                + (f": {dict(list(ruins.items())[:3])}" if ruins else ""), not ruins))
    # Rechecagem dos autorais contra as referências boas e ruins; decisão
    # explícita sobre organizadores, como Davi pediu nos comentários de 20/10.
    rev = run / "REVISAO-AUTORAIS.md"
    rtxt = rev.read_text(encoding="utf-8") if rev.exists() else ""
    sem_rev = [e["key"] for e in autorais if not re.search(re.escape(e["key"]) + r".*par:", rtxt)]
    out.append(("[duro] REVISAO-AUTORAIS.md: cada autoral relido contra EXEMPLARES e ANTI-EXEMPLARES ('<chave> … par: …')"
                + (f": faltam {sem_rev[:4]}" if sem_rev else ""), not autorais or (rev.exists() and not sem_rev)))
    org_decidido = bool(re.search(r"(?im)^Organizadores necessários:\s*(sim|não)\s*[—:-]\s*\S+", rtxt))
    out.append(("[duro] revisão final responde 'Organizadores necessários: sim|não — motivo'", org_decidido))
    # Irmãos: nota de acervo entra com todos os clozes (Davi suspende)
    irm = []
    for e in entries:
        if e.get("origin") != "Autoral" and e.get("manter") and e.get("fields", {}).get("Text"):
            n = {int(x) for x in re.findall(r"\{\{c(\d+)::", e["fields"]["Text"])}
            if n and n != {c["n"] for c in e.get("cards", [])}:
                irm.append(e["key"])
    out.append(("[duro] notas de acervo com todos os irmãos (clozes) incluídos" + (f": {irm[:4]}" if irm else ""), not irm))
    # F-20261016-CLAUDE-08 (refação): autoral antigo da própria aula mantido por sh() (sem source::nid e no deck da aula) conta como autoral,
    # e todo compartilhado conta no total de cards do deck; corridas antigas sem "n_cards" no plano seguem a conta só das entradas.
    shs = [v for v in (plan.get("compartilhados") or {}).values() if "n_cards" in v]
    au_sh = sum(v["n_cards"] for v in shs if not v.get("source_nid") and v.get("deck_proprio"))
    share = (sum(len(e.get("cards", [])) or 1 for e in autorais) + au_sh) / max(1, sum(len(e.get("cards", [])) or 1 for e in entries) + sum(v["n_cards"] for v in shs))
    # F-20261016-CLAUDE-04: "excesso de autoral… só para casos especiais; no geral, sempre decks outros, AnKing e os outros, prioridade máxima (gate-hard)"
    exc = str(plan.get("autoral_excecao") or "").strip()
    versao = int(plan.get("pipeline_versao") or 1)
    if run.name not in LEGADO_V2:
        out.append(("[duro] PIPELINE_VERSAO ≥ 4 (teto de autoral + todo AnKing das seções da aula) em toda corrida nova", versao >= 4))
    if versao >= 3 and run.name not in LEGADO_V2:
        ok = share <= MAX_AUTORAL or (len(exc) >= 80 and share <= MAX_AUTORAL_EXCECAO)
        out.append((f"[duro] autoral = {share:.0%} dos cards: até {MAX_AUTORAL:.0%}; até {MAX_AUTORAL_EXCECAO:.0%} só com AUTORAL_EXCECAO (≥ 80 caracteres); acima, nunca"
                    + (" — exceção declarada" if share > MAX_AUTORAL and ok else ""), ok))
    else:
        out.append((f"autoral = {share:.0%} dos cards (corrida legada, entregue antes do teto)", True))
    # F-20261016-CLAUDE-06: “se tiver um card anking daquele conteúdo, pode entrar, sem limite de quantos, quanto mais melhor, se
    # realmente for da aula. Só cuidado para não ir para outros conteúdos / deck não tem limite de cards”. Cada seção de recurso que a
    # corrida declara como do conteúdo da aula (SECOES_DA_AULA) tem TODA nota no deck (ak, ou sh de cópia NEBLI) ou em EXCLUIDOS.
    if versao >= 4 and run.name not in LEGADO_V2:
        secs = plan.get("secoes_da_aula") or []
        dentro = {str(e.get("src")) for e in entries if e.get("src")}
        dentro |= {str(v.get("source_nid")) for v in (plan.get("compartilhados") or {}).values() if v.get("source_nid")}
        fora = {str(x["nid"]) for x in plan.get("excluidos", []) if str(x.get("motivo", "")).strip()}
        faltam = []
        for s in secs:
            f = run / "busca" / "secoes" / s
            nids = re.findall(r"(?m)^(\d{13})\b", f.read_text(encoding="utf-8")) if f.exists() else ["arquivo-ausente:" + s]
            faltam += [n for n in nids if n not in dentro and n not in fora]
        out.append((f"[duro] todo AnKing das seções da aula ({len(secs)}) está no deck ou em EXCLUIDOS com motivo"
                    + (f": faltam {sorted(set(faltam))[:6]}" if faltam else ""), bool(secs) and not faltam))
    return out


# F-20261016-CLAUDE-01: "não pode ser tudo verde… nem tudo é tão importante" e "quando for mais de 2 clozes por card garanta que a
# indução está boa / em cards organizadores… deixar a primeira letra". Rubrica em PESQUISA-IMPORTANCIA-2026-10-16.md e MEMORY §6/§8.
RUBRICA = {"V-hy": "verde", "V-pilar": "verde", "V-prova": "verde", "A-aula": "azul", "A-step": "azul", "R-detalhe": "rosa", "R-org": "rosa"}
MAX_VERDE = 0.50
_CLOZE_FULL = re.compile(r"\{\{c(\d+)::(.*?)\}\}", re.S)


def cores_rubrica(plan):
    out = []
    entries = plan.get("entries", [])
    centrais = set()
    for item in (plan.get("escopo") or {}).get("centrais", []):
        centrais.update(item[1:])
    sem_cod, erradas, verde_sem_base, org_verde = [], [], [], []
    for e in entries:
        m = re.match(r"\s*([VAR]-[a-z]+(?:/[VAR]-[a-z]+)*)\s*:", str(e.get("motivo", "")))
        cods = m.group(1).split("/") if m else []
        if not cods or any(c not in RUBRICA for c in cods):
            sem_cod.append(e["key"]); continue
        permitidas = {RUBRICA[c] for c in cods}
        if any(x.get("cor") not in permitidas for x in e.get("cards", [])):
            erradas.append(e["key"])
        if "V-pilar" in cods and e["key"] not in centrais:
            verde_sem_base.append(e["key"])
        if "V-prova" in cods and not (e["key"] in centrais and ("prova" in str(e.get("motivo", "")).lower() or e.get("hy") == "1")):
            verde_sem_base.append(e["key"])
        if "data-nebli-organizacao" in (e.get("fields", {}).get("Text", "")) and "verde" in permitidas and "V-pilar" not in cods:
            org_verde.append(e["key"])
    # F-20261016-CLAUDE-03: todo HY 1–2 do AnKing é verde; o limite de 50% vale para o resto
    eh_hy = lambda e: e.get("origin") == "AnKing" and e.get("hy") in ("1", "2")
    hy_nao_verde = [e["key"] for e in entries if eh_hy(e) and any(x.get("cor") != "verde" for x in e.get("cards", []))]
    vhy_sem_hy = [e["key"] for e in entries if str(e.get("motivo", "")).startswith("V-hy") and not eh_hy(e)]
    out.append(("[duro] todo HY 1–2 do AnKing é verde (V-hy), mesmo acima de 50%" + (f": {hy_nao_verde[:4]}" if hy_nao_verde else "")
                + (f"; V-hy sem HY {vhy_sem_hy[:4]}" if vhy_sem_hy else ""), not hy_nao_verde and not vhy_sem_hy))
    cards = [x for e in entries if not eh_hy(e) for x in e.get("cards", [])]
    verde = sum(x.get("cor") == "verde" for x in cards) / max(1, len(cards))
    out.append(("[duro] cor por rubrica: motivo começa com V-hy|V-pilar|V-prova|A-aula|A-step|R-detalhe|R-org e a cor bate" +
                (f": sem código {sem_cod[:4]}" if sem_cod else "") + (f"; cor divergente {erradas[:4]}" if erradas else ""), not sem_cod and not erradas))
    out.append(("[duro] verde só com base: V-pilar no ESCOPO['centrais']; V-prova central e com prova/HY 1" +
                (f": {verde_sem_base[:4]}" if verde_sem_base else ""), not verde_sem_base))
    out.append(("[duro] organizador verde só se a classificação é pilar (V-pilar)" + (f": {org_verde[:4]}" if org_verde else ""), not org_verde))
    out.append((f"[duro] diversidade de cores: verde {verde:.0%} dos cards que não são HY (máximo {MAX_VERDE:.0%})", verde <= MAX_VERDE))
    return out


def inducao_clozes(plan):
    ruins = []
    organizadores_ruins = []
    for e in plan.get("entries", []):
        if e.get("origin") == "AnKing":
            continue
        txt = e.get("fields", {}).get("Text", "")
        grupos = {}
        for n, corpo in _CLOZE_FULL.findall(txt):
            grupos.setdefault(n, []).append(corpo)
        for n, itens in grupos.items():
            if len(itens) < 3:
                continue
            for corpo in itens:
                partes = corpo.split("::")
                resp = re.sub(r"<[^>]+>", "", partes[0]).strip()
                dica = partes[1].strip() if len(partes) > 1 else ""
                if not dica or (resp and dica[0].lower() != resp[0].lower()):
                    ruins.append(f"{e['key']}/c{n}"); break
        # F-20261020-CODEX-05: organizadores são listas verticais e economizam notas
        # usando irmãos (índices diferentes). Contrastes complementares são a exceção:
        # usam o mesmo índice para um lado não entregar o outro.
        if e.get("organizador"):
            itens = _CLOZE_FULL.findall(txt)
            indices = {n for n, _ in itens}
            vertical = len(re.findall(r"<br\s*/?>", txt, re.I)) >= max(1, len(itens) - 1)
            contraste = bool(e.get("contraste_complementar"))
            indices_ok = len(indices) == 1 if contraste else len(indices) >= min(2, len(itens))
            if len(itens) < 2 or not vertical or not indices_ok:
                organizadores_ruins.append(e["key"])
    return [("[duro] indução: card que esconde 3+ itens tem dica com a 1ª letra em cada lacuna ({{c1::Coagulative::C…}})"
             + (f": {ruins[:4]}" if ruins else ""), not ruins),
            ("[duro] organizador: tópicos verticais e clozes distintos; contraste complementar usa um só índice"
             + (f": {organizadores_ruins[:4]}" if organizadores_ruins else ""), not organizadores_ruins)]


def author_volume_supported(plan):
    """High authorship is acceptable only with a traceable search per card."""
    entries = plan.get("entries", [])
    authored = [e for e in entries if e.get("origin") == "Autoral"]
    cards = lambda es: sum(len(e.get("cards", [])) or 1 for e in es)
    if cards(authored) <= MAX_AUTORAL * max(1, cards(entries)):
        return True
    return bool(plan.get("busca_externos")) and all(
        str(e.get("busca", "")).strip() and len(e.get("espelhos") or []) >= 2
        for e in authored)


def live_checks(plan):
    from nebli import ordem, rotulos
    from nebli.decks import Anki
    call = Anki()
    tag = f"NEBLI::{plan['lesson_id']}"
    notes, others = ordem._live(tag)
    problems, _, _ = ordem.check(tag, notes, others, plan)
    out = [("ordem no Anki confere com o plano (coluna 'Ordem da aula')", bool(notes) and not problems)]
    # 11/10: gates passaram com Extras do plano que a delta recusou gravar; texto visível vivo tem de bater com o plano
    receipt = RUN.get("dir") and Path(RUN["dir"]) / "receipt.json"
    if receipt and receipt.exists():
        nid = {x["key"]: x["nid"] for x in json.loads(receipt.read_text())["notes"]}
        seen = lambda v: re.sub(r"\s+", "", html.unescape(re.sub(r"<[^>]+>", "", v or "")))
        want = {nid[e["key"]]: e for e in plan["entries"] if e["key"] in nid}
        live = {n["noteId"]: n for n in call("notesInfo", notes=list(want)) if n}
        bad = [e["key"] for n, e in want.items() if n not in live or any(
            k in live[n]["fields"] and seen(live[n]["fields"][k]["value"]) != seen(v) for k, v in e["fields"].items() if k in ("Text", "Extra", "Front", "Back"))]
        out.append(("Text/Extra vivos conferem com o plano" + (f": divergem {len(bad)} ({bad[:3]})" if bad else ""), not bad))
    # F-16: a etimologia ficou num "NEBLI-deck::" órfão, fora da árvore, e Davi a perdeu de vista.
    out.append(("nenhum deck NEBLI fora da árvore NEBLI (etimologia incluída)",
                not [n for n in call("deckNames") if n.startswith("NEBLI") and not rotulos.in_tree(n)]))
    from nebli import explicacoes
    if os.environ.get("NEBLI_SEM_TAB") == "1":  # F-20261015-CLAUDE-06: "não gera com tab ainda, vou pedir pro codex gerar depois"
        out.append(("Tab pendente por decisão de Davi (Codex gera depois)", True))
        return out
    try:
        coverage = explicacoes.cobertura(f'"tag:{tag}"', call=call)
        out.append(("Tab em 100% dos cards", coverage.get("atual", 0) > 0 and coverage.get("faltando", 1) == 0 and coverage.get("desatualizada", 1) == 0 and coverage.get("revisar", 1) == 0))
        out.append(("Tab em texto corrido, do princípio ao card, em cada card",
                    coverage.get("formato_incompleto", 1) == 0))
    except AttributeError:
        out.append(("Tab: verificação indisponível; corrigir antes de entregar", False))
    return out


def drive_checks(data):
    from nebli import entrega
    folder = entrega.ROOT / data.get("drive_pasta", "_")
    names = entrega.names(data.get("nome", "_"))
    scope = data.get("escopo", "e1+cards")
    if scope not in ("cards", "e1+cards"):
        return [("escopo reconhecido: cards ou e1+cards", False)]
    # F-20261011-CLAUDE-02: um só .apkg por UC no Drive (NEBLI - UCxx.apkg); .apkg por aula não sobe mais
    kinds = ("slides",) if scope == "cards" else ("e1", "slides")
    if data.get("sem_laminas"):  # F-20261016-CLAUDE-05: aula sem lâminas não tem PDF de slides a entregar
        kinds = tuple(k for k in kinds if k != "slides")
    checks = [(f"Drive: {names[k]}", (folder / names[k]).is_file()) for k in kinds]
    parts = Path(data.get("drive_pasta", "_")).parts
    if parts:
        uc_pkg = entrega.ROOT / parts[0] / f"NEBLI - {parts[0]}.apkg"
        checks.append((f"Drive: pacote único da UC ({uc_pkg.name})", uc_pkg.is_file()))
    return checks


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("corrida"); parser.add_argument("--sem-anki", action="store_true"); parser.add_argument("--sem-drive", action="store_true")
    parser.add_argument("--fontes", action="store_true", help="somente gate duro de fontes, antes da seleção/instalação")
    args = parser.parse_args(argv)
    run = Path(args.corrida)
    if args.fontes:
        require_sources(run)
        print("ok: fontes com evidências rastreáveis; revisão semântica continua obrigatória")
        return 0
    checks = []
    if not (run / "fontes.json").exists():
        checks.append(("fontes.json na corrida", False)); data = {}
    else:
        data = json.loads((run / "fontes.json").read_text(encoding="utf-8")); checks += sources(run, data)
    if not (run / "plan.json").exists():
        checks.append(("plan.json na corrida", False))
    else:
        RUN["dir"] = run
        plan = json.loads((run / "plan.json").read_text(encoding="utf-8")); checks += plan_checks(run, plan)
        if not args.sem_anki:
            checks += live_checks(plan)
    if data and not args.sem_drive:
        checks += drive_checks(data)
    for label, ok in checks:
        print({True: "ok   ", False: "FALHA", None: "?    "}[ok], label)
    failed = [label for label, ok in checks if ok is not True]
    print(f"\n{len(checks) - len(failed)} de {len(checks)} passos com evidência." + ("" if not failed else " Não entregar."))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
