#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEBLI -- curar_anking_v2.py
Localizador de CANDIDATOS AnKing dirigido por conceitos já classificados.
Consome a checklist revisada + E1 e produz uma shortlist para julgamento
semântico. Não aprova cards e não monta deck-aula.

Diferença da v1:
- v1: 1 keyword blob → top-N global. Sem verificação de cobertura, sem
  distinguir on-aula de on-disciplina.
- v2 atual: checklist classificada → busca dirigida por retrieval concept;
  heurísticas apenas ORDENAM a leitura. Aprovação final é humana/LLM card a card.

Uso:
    python3 flashcards/scripts/curar_anking_v2.py <slug> --e1 typst-build/etapa1.typ \
      --checklist arquivos-trabalho/checklist-<slug>.tsv \
      [--max-candidates-per-concept 8] [--sections "Step 1/Zanki Step Decks/Zanki GI"] \
      [--emit-parking]

Saídas:
    flashcards/curadoria/<slug>-anking-v11-candidatos.json   (shortlist; PENDING_REVIEW)
    arquivos-trabalho/curadoria-anking-<slug>.md              (relatório de cobertura + sugestões de patch E1)
    figuras/<slug>_anking/*                                   (imagens do AnKing)

`--emit-parking` é opt-in para investigações específicas. A corrida normal não
materializa centenas de cards off-aula só porque pertencem ao mesmo sistema.
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


def parse_checklist(path: Path) -> dict:
    """Lê checklist já classificada e devolve somente nuclear/supporting.

    REVIEW/AUDIT_ONLY bloqueiam: o extrator nunca decide sozinho o que merece card.
    Cada linha vira sua própria unidade de busca, evitando quotas por subtópico.
    """
    subtopicos = []
    all_keywords = set()
    pending = []
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        cols = raw.split("\t")
        if len(cols) < 4:
            raise ValueError("checklist canônica exige 4 colunas, incluindo card_decision")
        cid, frase, termos, decision = (c.strip() for c in cols[:4])
        decision = decision.lower()
        if decision == "no_card":
            continue
        if decision not in {"nuclear", "supporting"}:
            pending.append(f"{cid}:{cols[3].strip()}")
            continue
        keywords = {t.strip().lower() for t in termos.split("|")
                    if t.strip() and t.strip() != "<EN?>"}
        if not keywords:
            raise ValueError(f"{cid}: conceito selecionado sem termo de busca")
        subtopicos.append({"id": cid, "titulo": frase, "conceitos": keywords,
                           "card_decision": decision})
        all_keywords |= keywords
    if pending:
        raise ValueError("classifique antes de buscar: " + ", ".join(pending[:12]))
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
    """Score 0-3 de FORMA, usado somente para ordenar candidatos:
    - Cloze único (apenas c1) = +1
    - Extra >= 15 palavras = +1
    - Tem imagem em algum field = +1
    Máximo 3. Não mede adequação semântica e nunca aprova um card.
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


def curar(slug: str, e1_path: Path, checklist_path: Path, sections: list, max_candidates: int,
          meta_uc: str, meta_prova: str, meta_materia: str, meta_aula: str,
          score_min: int = 0, emit_parking: bool = False):

    # 1. Parse E1
    print(f"-> parseando E1: {e1_path.relative_to(ROOT)}")
    # O parser da E1 continua útil como fallback técnico, mas a lista do que merece
    # spaced repetition vem exclusivamente da checklist revisada.
    parse_e1(e1_path)
    e1_map = parse_checklist(checklist_path)
    print(f"   {len(e1_map['subtopicos'])} conceitos selecionados (nuclear/supporting)")

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

    # 3. Para cada conceito, rankeia uma SHORTLIST para leitura. O cap controla
    #    custo de inspeção, não quantidade de cards no deck final.
    fig_dir = ROOT / f"figuras/{slug}_anking"
    fig_dir.mkdir(parents=True, exist_ok=True)

    ancorados_por_subtop = defaultdict(list)  # id → lista de (card, hits, score)
    parking_step1 = []
    ja_selecionados_nids = set()  # dedupe entre subtópicos

    for sub in e1_map["subtopicos"]:
        candidatos = []
        for card in all_cards:
            categoria, hits, anc_id = classificar_ancoragem(card, sub, e1_map["aula_keywords"])
            if categoria in ("ANCORADO", "ANCORAVEL"):
                score = rubrica_qualidade(card)
                if score >= score_min:
                    candidatos.append((card, hits, score, categoria))

        # Rank: (categoria ANCORADO > ANCORAVEL), (score desc), (# hits desc)
        cat_order = {"ANCORADO": 0, "ANCORAVEL": 1}
        candidatos.sort(key=lambda x: (cat_order[x[3]], -x[2], -len(x[1])))
        top = candidatos[:max_candidates]
        for card, hits, score, categoria in top:
            ja_selecionados_nids.add(card["meta"]["nid"])
            ancorados_por_subtop[sub["id"]].append((card, hits, score, categoria))

    # 4. Parking off-aula é opt-in: útil em investigação, ruído na corrida normal.
    if emit_parking:
        for card in all_cards:
            nid = card["meta"].get("nid")
            if nid in ja_selecionados_nids:
                continue
            for sub in e1_map["subtopicos"]:
                cat, _, _ = classificar_ancoragem(card, sub, e1_map["aula_keywords"])
                if cat == "BASE-STEP1":
                    parking_step1.append(card)
                    break

    print(f"-> {sum(len(v) for v in ancorados_por_subtop.values())} candidatos para revisão semântica")
    if emit_parking:
        print(f"-> {len(parking_step1)} cards BASE-STEP1 pra parking (opt-in)")

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
            tags.append("NEBLI::anking-v11-candidato")
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
                "_decision": "PENDING_REVIEW",
                "_card_decision": sub.get("card_decision"),
            })

    ancorados_json = ROOT / f"flashcards/curadoria/{slug}-anking-v11-candidatos.json"
    ancorados_json.parent.mkdir(parents=True, exist_ok=True)
    ancorados_json.write_text(json.dumps({
        "meta": {
            "uc": meta_uc, "prova": meta_prova, "materia": meta_materia,
            "aula_curta": meta_aula, "slug": f"{slug}-anking",
            "fonte": "curar_anking_v2 candidate finder (langfield/anking-v11)",
            "score_min_form_only": score_min,
            "max_candidates_per_concept": max_candidates,
            "warning": "CANDIDATOS; nenhum card deste arquivo está aprovado automaticamente",
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

    parking_json = None
    if emit_parking:
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
        f"**Config:** score_min_form_only={score_min}, max_candidates_per_concept={max_candidates}, sections={sections}",
        f"",
        f"## Shortlist por conceito — cobertura só existe após keep/drop semântico",
        f"",
        f"| Subtópico | Cards | ANCORADO | ANCORÁVEL | Score médio | Veredito |",
        f"|---|---|---|---|---|---|",
    ]
    total_cards = 0
    for sub in e1_map["subtopicos"]:
        cards = ancorados_por_subtop.get(sub["id"], [])
        n = len(cards)
        anc = sum(1 for c in cards if c[3] == "ANCORADO")
        acv = sum(1 for c in cards if c[3] == "ANCORAVEL")
        avg = sum(c[2] for c in cards) / n if n else 0
        veredito = "REVISAR" if n else "SEM CANDIDATO"
        linhas.append(f"| **{sub['id']}** {sub['titulo'][:35]} | {n} | {anc} | {acv} | {avg:.1f} | {veredito} |")
        total_cards += n

    linhas += [
        f"",
        f"**Total na shortlist:** {total_cards} candidatos em {len(e1_map['subtopicos'])} conceitos",
        f"**Conceitos com ao menos um candidato:** {sum(1 for v in ancorados_por_subtop.values() if v)}/{len(e1_map['subtopicos'])}",
        f"**Nota Cards×E1:** pendente de curadoria semântica",
        f"",
        f"## Candidatos ANCORÁVEIS",
        f"",
        f"ANCORÁVEL aqui significa apenas hit no Extra/First Aid. Inspecionar a frente; não usar o hit para expandir a E1 automaticamente.",
        f"",
    ]

    for sub in e1_map["subtopicos"]:
        cards = ancorados_por_subtop.get(sub["id"], [])
        acvs = [c for c in cards if c[3] == "ANCORAVEL"]
        if not acvs:
            continue
        linhas.append(f"### {sub['id']} {sub['titulo']}")
        for card, hits, score, _ in acvs[:3]:
            text_short = " ".join(strip_html(card["fields"]["Text"]).split())[:150]
            linhas.append(f"- `anking-v11-{card['meta']['nid']}` (score {score}, hits: {', '.join(hits[:3])}): {text_short}...")
        linhas.append("")

    rel_path.write_text("\n".join(linhas), encoding="utf-8")

    print(f"\n=== Relatório ===")
    print(f"Total de candidatos na shortlist: {total_cards}")
    print(f"Conceitos com candidato: {sum(1 for v in ancorados_por_subtop.values() if v)}/{len(e1_map['subtopicos'])}")
    print("Nota Cards×E1: pendente de curadoria semântica")
    print(f"→ {ancorados_json.relative_to(ROOT)}")
    if parking_json:
        print(f"→ {parking_json.relative_to(ROOT)}")
    print(f"→ {rel_path.relative_to(ROOT)}")

    return {
        "candidatos_total": total_cards,
        "total_conceitos": len(e1_map["subtopicos"]),
        "nota_cards_e1": None,
        "parking_size": len(parking_step1) if emit_parking else None,
        "candidatos_json": str(ancorados_json.relative_to(ROOT)),
        "parking_json": str(parking_json.relative_to(ROOT)) if parking_json else None,
        "relatorio": str(rel_path.relative_to(ROOT)),
    }


def main():
    ap = argparse.ArgumentParser(description="Localiza candidatos AnKing por conceito classificado.")
    ap.add_argument("slug")
    ap.add_argument("--e1", default="typst-build/etapa1.typ")
    ap.add_argument("--checklist", required=True)
    ap.add_argument("--sections", default="Step 1/Zanki Step Decks/Zanki GI")
    ap.add_argument("--max-candidates-per-concept", type=int, default=8,
                    help="cap de leitura por conceito; NÃO é quota de cards")
    ap.add_argument("--score-min", type=int, default=0,
                    help="filtro heurístico de forma; 0 recomendado para não perder bons cards")
    ap.add_argument("--emit-parking", action="store_true",
                    help="materializa cards off-aula; desligado por padrão")
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

    checklist_path = ROOT / args.checklist
    if not checklist_path.exists():
        raise SystemExit(f"x checklist não encontrada: {checklist_path}")

    curar(args.slug, e1_path, checklist_path, sections, args.max_candidates_per_concept,
          args.uc, args.prova, args.materia, aula, args.score_min, args.emit_parking)


if __name__ == "__main__":
    main()
