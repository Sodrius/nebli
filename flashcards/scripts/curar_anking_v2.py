#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEBLI -- curar_anking_v2.py
Curadoria dirigida-por-subtópico + rubrica de qualidade + classificação de
ancoragem + parking Step 1 + relatório de cobertura. Consome a E1 compilada
(etapa1.typ) e o AnKing v11 clonado, produz um deck-aula 100% ancorado.

Diferença da v1:
- v1: 1 keyword blob → top-N global. Sem verificação de cobertura, sem
  distinguir on-aula de on-disciplina.
- v2: subtópicos extraídos da E1 → busca dirigida por subtópico com quota
  local; classifica cada candidato em ANCORADO/ANCORÁVEL/BASE-STEP1/FORA;
  rubrica automática 0-3; deck-aula final só admite ANCORADO+ANCORÁVEL com
  score ≥ 2; BASE-STEP1 vai pro parking pra aula futura; relatório de
  cobertura por subtópico (nota 0-10 via rubrica R6).

Uso:
    python3 flashcards/scripts/curar_anking_v2.py <slug> --e1 typst-build/etapa1.typ [--limit-per-subtopic 5] [--sections "Step 1/Zanki Step Decks/Zanki GI"] [--uc UC-8 --prova P1 --materia Anatomia --aula "Esôfago, estômago e delgado"]

Saídas:
    flashcards/curadoria/<slug>-anking-v11-ancorados.json     (deck-aula: só ANCORADO+ANCORÁVEL score>=2)
    flashcards/curadoria/<slug>-anking-step1-parking.json     (BASE-STEP1: aula futura)
    arquivos-trabalho/curadoria-anking-<slug>.md              (relatório de cobertura + sugestões de patch E1)
    figuras/<slug>_anking/*                                   (imagens do AnKing)
"""

from __future__ import annotations
import argparse
import hashlib
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent.parent
ANKING_ROOT = Path("/workspace/langfield/anking-v11")

FIELD_HEADERS = ["Text", "Extra", "Lecture Notes", "Missed Questions",
                 "Pathoma", "Boards and Beyond", "First Aid", "Sketchy",
                 "Pixorize", "Physeo", "OME", "Additional Resources",
                 "One by one"]


# =========================================================
# PARSER DA E1
# =========================================================

SUBTOPIC_RE = re.compile(r"^==\s+([\d.]+)\s+(.+?)$", re.MULTILINE)
BOLD_RE = re.compile(r"\*([^\*\n]{2,60})\*")
TERMO_NOTA_RE = re.compile(r"#termo-nota\[([^\]]+)\]")
SIGLA_RE = re.compile(r'#sigla\(\s*"([^"]+)"')


def parse_e1(e1_path: Path) -> dict:
    """Extrai subtópicos e conceitos nucleares da E1 compilada.

    Retorna:
      {
        "aula_keywords": set(...),           # todas as palavras-chave da aula
        "subtopicos": [
          {
            "id": "1.1",
            "titulo": "Um tubo entre a faringe e o estômago",
            "conceitos_nucleares": [...],    # bolded terms + termo-nota + siglas
            "keywords_search": [...],         # traduzido/expandido pra inglês
          },
          ...
        ]
      }
    """
    txt = e1_path.read_text(encoding="utf-8")
    subs = list(SUBTOPIC_RE.finditer(txt))
    subtopicos = []
    all_keywords = set()

    for i, m in enumerate(subs):
        sid = m.group(1)
        stitle = m.group(2).strip()
        start = m.end()
        end = subs[i+1].start() if i+1 < len(subs) else len(txt)
        block = txt[start:end]

        # conceitos = bolded + termo-nota + siglas
        bolds = set(BOLD_RE.findall(block))
        termos = set(TERMO_NOTA_RE.findall(block))
        siglas = set(SIGLA_RE.findall(block))
        conceitos = {t.lower().strip() for t in (bolds | termos | siglas) if len(t) >= 3}

        subtopicos.append({
            "id": sid,
            "titulo": stitle,
            "conceitos": conceitos,
        })
        all_keywords |= conceitos

    return {"aula_keywords": all_keywords, "subtopicos": subtopicos}


# =========================================================
# TRADUÇÃO PT→EN + EXPANSÃO DE KEYWORDS
# =========================================================

TRADUCOES = {
    # Anatomia GI PT→EN
    "esôfago": ["esophagus", "esophageal"],
    "esofágico": ["esophageal", "esophagus"],
    "estômago": ["stomach", "gastric"],
    "gástrico": ["gastric", "stomach"],
    "cárdia": ["cardia", "gastroesophageal junction"],
    "fundo": ["fundus", "gastric fundus"],
    "corpo": ["body", "corpus"],
    "antro": ["antrum", "pyloric antrum"],
    "piloro": ["pylorus", "pyloric"],
    "curvatura maior": ["greater curvature"],
    "curvatura menor": ["lesser curvature"],
    "incisura angular": ["angular incisure", "angularis"],
    "incisura cárdica": ["cardiac notch"],
    "duodeno": ["duodenum", "duodenal"],
    "duodenal": ["duodenal", "duodenum"],
    "jejuno": ["jejunum", "jejunal"],
    "íleo": ["ileum", "ileal"],
    "papila duodenal maior": ["ampulla of vater", "major duodenal papilla", "papilla of vater"],
    "papila maior": ["ampulla of vater", "major duodenal papilla"],
    "ampola hepatopancreática": ["hepatopancreatic ampulla", "ampulla of vater"],
    "colédoco": ["common bile duct", "cbd", "choledochus"],
    "ducto pancreático": ["pancreatic duct", "duct of wirsung"],
    "esfíncter de oddi": ["sphincter of oddi"],
    "ligamento de treitz": ["ligament of treitz", "suspensory ligament"],
    "ligamento suspensor do duodeno": ["suspensory ligament of duodenum", "ligament of treitz"],
    "flexura duodenojejunal": ["duodenojejunal flexure", "duodenojejunal junction"],
    "hiato esofágico": ["esophageal hiatus"],
    "veia cava inferior": ["inferior vena cava", "ivc"],
    "hiato aórtico": ["aortic hiatus"],
    "hérnia hiatal": ["hiatal hernia", "hiatus hernia"],
    "ligamento frênico-esofágico": ["phrenoesophageal ligament", "phrenicoesophageal"],
    "ângulo de his": ["angle of his"],
    "linha z": ["z-line", "gastroesophageal junction"],
    "doença de chagas": ["chagas disease", "chagas"],
    "megaesôfago": ["megaesophagus", "achalasia"],
    "plexo mientérico": ["myenteric plexus", "auerbach plexus"],
    "constrição": ["constriction", "narrowing"],
    "constrições": ["constrictions", "narrowings"],
    "cricofaríngea": ["cricopharyngeus", "cricopharyngeal"],
    "esfíncter esofágico superior": ["upper esophageal sphincter", "ues"],
    "esfíncter esofágico inferior": ["lower esophageal sphincter", "les"],
    "broncoaórtica": ["bronchoaortic", "aortic arch"],
    "quimo": ["chyme"],
    "úlcera": ["ulcer", "peptic ulcer"],
    "úlcera perfurada": ["perforated ulcer", "peptic perforation"],
    "úlcera péptica": ["peptic ulcer", "peptic ulcer disease", "pud"],
    "aine": ["nsaid", "nsaids"],
    "artéria gastroduodenal": ["gastroduodenal artery"],
    "artéria mesentérica superior": ["superior mesenteric artery", "sma"],
    "veia mesentérica superior": ["superior mesenteric vein", "smv"],
    "vasos retos longos": ["long vasa recta", "vasa recta"],
    "vasos retos curtos": ["short vasa recta", "vasa recta"],
    "arcos arteriais": ["arterial arcades", "arterial arches"],
    "arcadas": ["arcades"],
    "mesentério": ["mesentery", "mesenteric"],
    "raiz do mesentério": ["mesenteric root", "root of mesentery"],
    "isquemia mesentérica": ["mesenteric ischemia", "acute mesenteric ischemia"],
    "divertículo de meckel": ["meckel diverticulum", "meckel"],
    "ducto onfalomesentérico": ["omphalomesenteric duct", "vitelline duct"],
    "junção íleocecocólica": ["ileocecal junction", "ileocecal valve"],
    "placas de peyer": ["peyer patches", "peyer's patches"],
    "pregas circulares": ["plicae circulares", "circular folds"],
    "bolsa omental": ["omental bursa", "lesser sac"],
    "cabeça do pâncreas": ["pancreatic head", "head of pancreas"],
    "corpo do pâncreas": ["pancreatic body", "body of pancreas"],
    "epitélio pavimentoso": ["squamous epithelium", "stratified squamous"],
    "metaplasia de barrett": ["barrett esophagus", "barrett metaplasia"],
    "câncer de esôfago": ["esophageal cancer", "esophageal carcinoma"],
    "adenocarcinoma": ["adenocarcinoma"],
    "carcinoma escamocelular": ["squamous cell carcinoma", "escc"],
    # Extra util
    "retroperitoneal": ["retroperitoneal", "secondarily retroperitoneal"],
    "intraperitoneal": ["intraperitoneal"],
    "peritônio": ["peritoneum", "peritoneal"],
    "diafragma": ["diaphragm", "diaphragmatic"],
    "cricoide": ["cricoid"],
    "arco aórtico": ["aortic arch"],
    "brônquio esquerdo": ["left main bronchus", "left bronchus"],
    "sma": ["sma", "superior mesenteric artery"],
    "smv": ["smv", "superior mesenteric vein"],
    "les": ["les", "lower esophageal sphincter"],
    "ues": ["ues", "upper esophageal sphincter"],
    "vci": ["ivc", "inferior vena cava"],
}


def traduzir(conceito: str) -> list:
    """PT→EN. Retorna lista de termos de busca (o próprio termo + traduções)."""
    low = conceito.lower().strip()
    resultado = {low}
    if low in TRADUCOES:
        resultado.update(TRADUCOES[low])
    # Também tenta substring simples
    for pt, ens in TRADUCOES.items():
        if pt in low or low in pt:
            resultado.update(ens)
    return list(resultado)


# =========================================================
# PARSER DE CARDS ANKING (mesmo formato da v1)
# =========================================================

def parse_card(path: Path) -> Optional[dict]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    lines = text.split("\n")
    meta = {}
    fields = {}

    i = 0
    if lines and lines[0].strip() == "## Note":
        i = 1
    while i < len(lines) and not lines[i].startswith("### "):
        line = lines[i].strip()
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
        i += 1

    current_field = None
    current_lines = []
    while i < len(lines):
        line = lines[i]
        if line.startswith("### "):
            if current_field:
                fields[current_field] = "\n".join(current_lines).strip()
            current_field = line[4:].strip()
            current_lines = []
        else:
            current_lines.append(line)
        i += 1
    if current_field:
        fields[current_field] = "\n".join(current_lines).strip()

    return {"meta": meta, "fields": fields, "path": str(path.relative_to(ANKING_ROOT))}


def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", " ", s)


def extract_images(html: str) -> list:
    return re.findall(r'<img\s+[^>]*src="([^"]+)"', html)


def find_media_file(name: str) -> Optional[Path]:
    for d in ANKING_ROOT.rglob("_media"):
        p = d / name
        if p.exists():
            return p
    return None


# =========================================================
# CLASSIFICADOR DE ANCORAGEM + RUBRICA
# =========================================================

def classificar_ancoragem(card: dict, subtopico: dict, aula_keywords: set) -> tuple:
    """Retorna (categoria, keywords_hit, subtopico_id_ancorado).

    ANCORADO: conceito nuclear do subtópico aparece no TEXT do card
    ANCORÁVEL: conceito no Extra/First Aid (não no Text principal)
    BASE-STEP1: alguma keyword da aula toda mas não do subtópico específico
    FORA: nada
    """
    text_low = strip_html(card["fields"].get("Text", "")).lower()
    extra_low = strip_html(card["fields"].get("Extra", "") + " " + card["fields"].get("First Aid", "")).lower()

    # Expande conceitos do subtópico via tradução PT→EN
    subtopic_keywords = set()
    for c in subtopico["conceitos"]:
        subtopic_keywords.update(traduzir(c))
    # Também inclui palavras do titulo do subtópico
    for w in subtopico["titulo"].lower().split():
        if len(w) >= 5:  # evita "de", "do", "a"
            subtopic_keywords.update(traduzir(w))

    hits_text = [k for k in subtopic_keywords if k in text_low]
    hits_extra = [k for k in subtopic_keywords if k in extra_low]

    if hits_text:
        return ("ANCORADO", hits_text, subtopico["id"])
    if hits_extra:
        return ("ANCORAVEL", hits_extra, subtopico["id"])

    # Fallback: casa alguma keyword da aula (mas não deste subtópico)
    aula_kws_en = set()
    for c in aula_keywords:
        aula_kws_en.update(traduzir(c))
    hits_aula = [k for k in aula_kws_en if k in text_low or k in extra_low]
    if hits_aula:
        return ("BASE-STEP1", hits_aula, None)

    return ("FORA", [], None)


def rubrica_qualidade(card: dict) -> int:
    """Score 0-3 baseado em heurística automática:
    - Cloze único (apenas c1) = +1
    - Extra >= 15 palavras = +1
    - Tem imagem em algum field = +1
    Máximo 3.
    """
    score = 0
    text = card["fields"].get("Text", "")
    extra = card["fields"].get("Extra", "")

    clozes = set(re.findall(r"\{\{c(\d+)::", text))
    if len(clozes) == 1:
        score += 1

    extra_words = len(strip_html(extra).split())
    if extra_words >= 15:
        score += 1

    all_fields = " ".join(card["fields"].values())
    if "<img" in all_fields:
        score += 1

    return score


# =========================================================
# CURADORIA
# =========================================================

def guid_from_nid(nid: str) -> str:
    return hashlib.sha256(f"anking-v11-{nid}".encode()).hexdigest()[:16]


def curar(slug: str, e1_path: Path, sections: list, limit_per_subtopic: int,
          meta_uc: str, meta_prova: str, meta_materia: str, meta_aula: str,
          score_min: int = 2):

    # 1. Parse E1
    print(f"-> parseando E1: {e1_path.relative_to(ROOT)}")
    e1_map = parse_e1(e1_path)
    print(f"   {len(e1_map['subtopicos'])} subtópicos, {len(e1_map['aula_keywords'])} conceitos nucleares únicos")

    # 2. Carrega todos os cards das seções
    print(f"-> carregando cards do AnKing v11 (sections={sections})")
    all_cards = []
    for section in sections:
        section_path = ANKING_ROOT / section
        if not section_path.exists():
            print(f"   ! seção não existe: {section}", file=sys.stderr)
            continue
        for md in section_path.rglob("*.md"):
            card = parse_card(md)
            if card and card.get("fields", {}).get("Text"):
                all_cards.append(card)
    print(f"   {len(all_cards)} cards carregados")

    # 3. Pra cada subtópico, classifica + rankeia + seleciona top N
    fig_dir = ROOT / f"figuras/{slug}_anking"
    fig_dir.mkdir(parents=True, exist_ok=True)

    ancorados_por_subtop = defaultdict(list)  # id → lista de (card, hits, score)
    parking_step1 = []
    ja_selecionados_nids = set()  # dedupe entre subtópicos

    for sub in e1_map["subtopicos"]:
        candidatos = []
        for card in all_cards:
            nid = card["meta"].get("nid")
            if nid in ja_selecionados_nids:
                continue
            categoria, hits, anc_id = classificar_ancoragem(card, sub, e1_map["aula_keywords"])
            if categoria in ("ANCORADO", "ANCORAVEL"):
                score = rubrica_qualidade(card)
                if score >= score_min:
                    candidatos.append((card, hits, score, categoria))

        # Rank: (categoria ANCORADO > ANCORAVEL), (score desc), (# hits desc)
        cat_order = {"ANCORADO": 0, "ANCORAVEL": 1}
        candidatos.sort(key=lambda x: (cat_order[x[3]], -x[2], -len(x[1])))
        top = candidatos[:limit_per_subtopic]
        for card, hits, score, categoria in top:
            ja_selecionados_nids.add(card["meta"]["nid"])
            ancorados_por_subtop[sub["id"]].append((card, hits, score, categoria))

    # 4. Cards que não foram ancorados a nenhum subtópico mas casam a aula toda → parking
    for card in all_cards:
        nid = card["meta"].get("nid")
        if nid in ja_selecionados_nids:
            continue
        # Classifica contra qualquer subtópico
        best_cat = "FORA"
        for sub in e1_map["subtopicos"]:
            cat, _, _ = classificar_ancoragem(card, sub, e1_map["aula_keywords"])
            if cat == "BASE-STEP1":
                best_cat = "BASE-STEP1"
                break
        if best_cat == "BASE-STEP1":
            parking_step1.append(card)

    print(f"-> {sum(len(v) for v in ancorados_por_subtop.values())} cards ANCORADOS/ANCORÁVEIS (score >= {score_min})")
    print(f"-> {len(parking_step1)} cards BASE-STEP1 pra parking (aula futura)")

    # 5. Copia imagens
    def coleta_imagem(card):
        for source_field_name in ["Text", "Extra", "First Aid"]:
            imgs = extract_images(card["fields"].get(source_field_name, ""))
            for img_src in imgs:
                img_name = re.sub(r"%20", " ", img_src)
                media = find_media_file(img_name)
                if media:
                    dst = fig_dir / media.name
                    if not dst.exists():
                        try:
                            shutil.copy2(media, dst)
                        except Exception:
                            pass
                    return media.name
        return None

    # 6. Constrói JSON ancorados
    cards_out = []
    for sub in e1_map["subtopicos"]:
        for card, hits, score, categoria in ancorados_por_subtop.get(sub["id"], []):
            img_name = coleta_imagem(card)
            text_clean = re.sub(r'<img\s+[^>]*/?>', '', card["fields"].get("Text", "")).strip()
            extra_clean = re.sub(r'<img\s+[^>]*/?>', '', card["fields"].get("Extra", "") or card["fields"].get("First Aid", "")).strip()

            tags = [t for t in card["meta"].get("tags", "").split(", ") if t.strip()]
            tags.append(f"NEBLI::{slug}")
            tags.append("NEBLI::anking-v11-curado")
            tags.append(f"NEBLI::anking-ancoragem::{categoria}")
            tags.append(f"NEBLI::anking-subtopico::{sub['id'].replace('.', '_')}")

            cards_out.append({
                "id": f"anking-v11-{card['meta']['nid']}",
                "type": "cloze",
                "front": text_clean,
                "extra": extra_clean,
                "image": f"figuras/{slug}_anking/{img_name}" if img_name else "",
                "tags": tags,
                "_ancoragem": categoria,
                "_subtopico": sub["id"],
                "_subtopico_titulo": sub["titulo"],
                "_score": score,
                "_hits": hits[:5],
            })

    ancorados_json = ROOT / f"flashcards/curadoria/{slug}-anking-v11-ancorados.json"
    ancorados_json.parent.mkdir(parents=True, exist_ok=True)
    ancorados_json.write_text(json.dumps({
        "meta": {
            "uc": meta_uc, "prova": meta_prova, "materia": meta_materia,
            "aula_curta": meta_aula, "slug": f"{slug}-anking",
            "fonte": "curar_anking_v2 (langfield/anking-v11)",
            "score_min": score_min,
            "limit_per_subtopic": limit_per_subtopic,
        },
        "cards": cards_out,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # 7. Parking
    parking_out = []
    for card in parking_step1[:200]:  # cap arbitrário
        parking_out.append({
            "id": f"anking-v11-{card['meta']['nid']}",
            "text": card["fields"].get("Text", ""),
            "extra": card["fields"].get("Extra", ""),
            "tags_anking": card["meta"].get("tags", ""),
            "path": card["path"],
        })

    parking_json = ROOT / f"flashcards/curadoria/{slug}-anking-step1-parking.json"
    parking_json.write_text(json.dumps({
        "meta": {"origem_slug": slug, "descricao": "Cards on-disciplina mas off-aula. Puxar quando aula específica for redigida."},
        "cards": parking_out,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # 8. Relatório de cobertura
    rel_path = ROOT / f"arquivos-trabalho/curadoria-anking-{slug}.md"
    rel_path.parent.mkdir(parents=True, exist_ok=True)
    linhas = [
        f"# Curadoria AnKing v11 — {slug}",
        f"",
        f"**Fonte:** `langfield/anking-v11` (24k+ cards, Step 1)",
        f"**Config:** score_min={score_min}, limit_per_subtopic={limit_per_subtopic}, sections={sections}",
        f"",
        f"## Cobertura por subtópico (rubrica R6, meta ≥3 nucleares)",
        f"",
        f"| Subtópico | Cards | ANCORADO | ANCORÁVEL | Score médio | Veredito |",
        f"|---|---|---|---|---|---|",
    ]
    total_cards = 0
    nucleares_ok = 0
    for sub in e1_map["subtopicos"]:
        cards = ancorados_por_subtop.get(sub["id"], [])
        n = len(cards)
        anc = sum(1 for c in cards if c[3] == "ANCORADO")
        acv = sum(1 for c in cards if c[3] == "ANCORAVEL")
        avg = sum(c[2] for c in cards) / n if n else 0
        veredito = "COBERTO" if n >= 3 else ("RASO" if n >= 1 else "LACUNA")
        if n >= 3: nucleares_ok += 1
        linhas.append(f"| **{sub['id']}** {sub['titulo'][:35]} | {n} | {anc} | {acv} | {avg:.1f} | {veredito} |")
        total_cards += n

    nota_cobertura = round(10 * nucleares_ok / len(e1_map["subtopicos"]), 1)
    linhas += [
        f"",
        f"**Total ancorados:** {total_cards} cards em {len(e1_map['subtopicos'])} subtópicos",
        f"**Subtópicos COBERTOS (≥3 cards):** {nucleares_ok}/{len(e1_map['subtopicos'])}",
        f"**Nota Cards×E1 (rubrica R6):** {nota_cobertura}/10",
        f"**Parking Step 1 (aula futura):** {len(parking_step1)} cards",
        f"",
        f"## Sugestões de patch da E1 (opcional — R16e: não altera silenciosamente)",
        f"",
        f"Cards ANCORÁVEIS podem virar ANCORADOS se a E1 receber 1-2 frases explicando o conceito. Sugestões abaixo pra Davi aplicar ou ignorar:",
        f"",
    ]

    for sub in e1_map["subtopicos"]:
        cards = ancorados_por_subtop.get(sub["id"], [])
        acvs = [c for c in cards if c[3] == "ANCORAVEL"]
        if not acvs:
            continue
        linhas.append(f"### {sub['id']} {sub['titulo']}")
        for card, hits, score, _ in acvs[:3]:
            text_short = strip_html(card["fields"]["Text"])[:150]
            linhas.append(f"- `anking-v11-{card['meta']['nid']}` (score {score}, hits: {', '.join(hits[:3])}): {text_short}...")
        linhas.append("")

    rel_path.write_text("\n".join(linhas), encoding="utf-8")

    print(f"\n=== Relatório ===")
    print(f"Total cards ancorados: {total_cards}")
    print(f"Subtópicos COBERTOS (≥3): {nucleares_ok}/{len(e1_map['subtopicos'])}")
    print(f"Nota Cards×E1 (R6): {nota_cobertura}/10")
    print(f"Parking Step 1: {len(parking_step1)}")
    print(f"→ {ancorados_json.relative_to(ROOT)}")
    print(f"→ {parking_json.relative_to(ROOT)}")
    print(f"→ {rel_path.relative_to(ROOT)}")

    return {
        "ancorados_total": total_cards,
        "cobertos": nucleares_ok,
        "total_subtopicos": len(e1_map["subtopicos"]),
        "nota_cards_e1": nota_cobertura,
        "parking_size": len(parking_step1),
        "ancorados_json": str(ancorados_json.relative_to(ROOT)),
        "parking_json": str(parking_json.relative_to(ROOT)),
        "relatorio": str(rel_path.relative_to(ROOT)),
    }


def main():
    ap = argparse.ArgumentParser(description="Cura AnKing v11 por subtópico com rubrica + cobertura.")
    ap.add_argument("slug")
    ap.add_argument("--e1", default="typst-build/etapa1.typ")
    ap.add_argument("--sections", default="Step 1/Zanki Step Decks/Zanki GI")
    ap.add_argument("--limit-per-subtopic", type=int, default=5)
    ap.add_argument("--score-min", type=int, default=2)
    ap.add_argument("--uc", default="UC-8")
    ap.add_argument("--prova", default="P1")
    ap.add_argument("--materia", default="Anatomia")
    ap.add_argument("--aula", default="")
    args = ap.parse_args()

    e1_path = ROOT / args.e1
    if not e1_path.exists():
        raise SystemExit(f"x etapa1.typ não encontrada: {e1_path}")

    sections = [s.strip() for s in args.sections.split(";") if s.strip()]
    aula = args.aula or args.slug

    curar(args.slug, e1_path, sections, args.limit_per_subtopic,
          args.uc, args.prova, args.materia, aula, args.score_min)


if __name__ == "__main__":
    main()
