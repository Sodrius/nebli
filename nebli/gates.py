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

import argparse
import html
import hashlib
import json
import re
import sys
from pathlib import Path

ESTADOS = {"consultada", "não localizada", "inacessível", "não aplicável"}
MIN_CANAIS = 3
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
    books = [b for b in data.get("livros", []) if b.get("lido") and material(b.get("texto", "_"))]
    out.append(("bibliografia da UC: capítulo da aula extraído e lido", bool(books)))
    channels = [c for c in data.get("canais", []) if c.get("lido") == "integral" and material(c.get("transcricao", "_"))]
    blocked = canais_bloqueados(data)
    out.append((f"canais que Davi acompanha: pelo menos {MIN_CANAIS} aulas com transcrição lida" + (_nota(blocked) if blocked else ""),
                len(channels) >= MIN_CANAIS or bool(blocked)))
    # F-20261003-CLAUDE-14: "calibrou tudo com a aula do ninja nerd e outros canais também? importante". O Ninja Nerd da aula
    # é lido inteiro (ou a busca mostra que não há); cada canal diz o que mudou ou confirmou no deck (chaves, cores).
    nn = [c for c in channels if "ninja nerd" in c.get("canal", "").lower() and c.get("lido") == "integral"]
    nn_ok = bool(nn) or bool(str(data.get("ninja_nerd_busca", "")).strip()) or bool(blocked)
    out.append(("Ninja Nerd da aula lido inteiro (ou busca registrada em 'ninja_nerd_busca' mostrando que não há)", nn_ok))
    uncal = [c.get("canal", "?")[:40] for c in channels if not str(c.get("calibracao", "")).strip()]
    out.append(("cada canal com 'calibracao': o que mudou ou confirmou no deck" + (f" (faltam: {uncal[:3]})" if uncal else ""), not uncal))
    for kind in ("provas", "exercicios", "caoc", "veteranos"):
        item = data.get(kind, {})
        ok = item.get("estado") in ESTADOS and (item.get("estado") == "consultada" or bool(str(item.get("busca", "")).strip()))
        out.append((f"{kind}: consultado, ou busca no Drive registrada", ok))
    out += source_evidence(run, data)
    out.append(class_folder(run, data))
    return out



def _nota(blocked):
    return f" ({blocked})" if blocked.startswith("vídeos dispensados") else f" (PENDENTE: {blocked})"


def canais_bloqueados(data):
    """10/10/2026: o YouTube bloqueou transcrições por IP (youtube_transcript_api IpBlocked; yt-dlp 'page needs to be reloaded').
    Não se finge leitura: fontes.json › canais_bloqueados registra data, erro real e ≥ MIN_CANAIS vídeos identificados pela busca
    (canal, url); a pendência aparece no rótulo do gate e no ESTADO-ATUAL, e os vídeos são lidos quando o bloqueio passar."""
    b = data.get("canais_bloqueados") or {}
    # F-20261013-CLAUDE-01: Davi dispensou vídeos (F-20261010-CLAUDE-06) e aprovou não exigir mais busca de vídeos para passar.
    if b.get("dispensado") is True and b.get("em"):
        return "vídeos dispensados por Davi (F-20261010-CLAUDE-06), sem busca exigida"
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
    ok = all(data.get(k, {}).get("ok") is True and str(data[k].get("evidencia", "")).strip() for k in REVISAO)
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
    if e.get("origin") == "AnKing":  # AnKing usa "{{c1::macro}}vesicular" e dica de contagem ("::2") de propósito
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
    extra += [(f"card curto: texto visível ≤ {MAX_TEXTO} caracteres fora do AnKing" + (f" (longos: {big[:4]})" if big else ""), not big),
              ("nota do Histology entra recortada em cards de uma frase (nebli.hx_cortes)" + (f": {hxlong[:4]}" if hxlong else ""), not hxlong),
              ("cloze de palavra inteira, sem 'x ou y' nem dica '::s/::x/::related/::all/::número' fora do AnKing" + (f": {badcz[:4]}" if badcz else ""), not badcz)]
    # F-20261003-CLAUDE-15: "tá faltando comentário": todo card tem no verso uma explicação curta, não só figura
    def back_text(e):
        f = e.get("fields") or {}
        return re.sub(r"\s+|&nbsp;|/", "", html.unescape(re.sub(r"<[^>]+>", "", f.get("Extra", "") or f.get("Back Extra", "") or "")))
    bare = [e["key"] for e in entries if e.get("kind") in ("text", "autoral") and not back_text(e)]
    longcz = [e["key"] for e in entries if e.get("origin") != "AnKing" and e.get("kind") in ("text", "autoral")
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
    out.append(("ordem estrita dos slides no plano (nenhum recuo; compartilhados na mesma sequência)",
                all(slides) and all(a <= b for a, b in zip(slides, slides[1:]))))
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
