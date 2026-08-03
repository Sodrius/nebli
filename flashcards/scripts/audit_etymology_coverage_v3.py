#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Auditoria adversarial do léxico: cobre utilidade, não apenas frequência."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ETIM = Path(__file__).resolve().parents[1] / "etimologia"
LEXICON = ETIM / "data" / "lexicon_master.json"
OUT_JSON = ETIM / "data" / "coverage_gaps_v3.json"
OUT_MD = ETIM / "reports" / "coverage_gaps_v3.md"
HOLDOUT = ETIM / "data" / "inference_holdout_v3.json"

TARGETS = {
    "procedimentos_confundiveis": ["-centese", "-clasia", "-dese", "-ectomia", "-pexia", "-plastia", "-rafia", "-scopia", "-stomia", "-tomia", "-tripsia", "ablação", "excisão", "ressecção", "anastomose", "derivação"],
    "sufixos_menos_expostos": ["-atresia", "-cele", "-ectasia", "-malácia", "-ptose", "-rrexis", "-rragia", "-rreia", "-cinesia", "-estesia", "-acusia", "-opsia", "-osmia", "-geusia", "-dipsia", "-orexia", "-emese"],
    "forma_estrutura_anatomica": ["braqui-", "dolico-", "plati-", "lepto-", "paqui-", "acin/o", "trabecul/o", "papil/o", "vil/o", "fascicul/o", "lobul/o", "foramin/o", "fissur/o", "sulc/o", "antr/o", "lumen", "diverticul/o"],
    "cor_aparencia": ["alb/o", "clor/o", "cian/o", "eritr/o", "rubr/o", "nigr/o", "poli/o", "xant/o", "lute/o", "glauc/o", "purpur/o", "hial/o", "escler/o"],
    "curso_temporal": ["agudo", "subagudo", "crônico", "recorrente", "intermitente", "paroxístico", "persistente", "transitório", "congênito", "adquirido", "neonatal", "perinatal", "remitente", "recidivante", "fulminante"],
    "patologia_discriminadores": ["inflamação × infecção", "infecção × colonização", "exsudato × transudato", "trombo × êmbolo", "isquemia × infarto", "obstrução × oclusão", "estenose × atresia", "erosão × úlcera", "abscesso × fístula", "neoplasia × hiperplasia"],
    "semiologia_discriminadores": ["disfagia × odinofagia", "disfasia × disartria", "parestesia × disestesia", "náusea × vômito × regurgitação", "dispneia × ortopneia", "ortopneia × platipneia", "trepopneia", "anosmia × hiposmia × hiperosmia", "anorexia × hiporexia × hiperorexia", "hematêmese × hemoptise", "melena × hematoquezia"],
    "polissemia_falsa_segmentacao": ["miel/o", "cist/o", "metr/o", "vas/o", "cerat/o", "hematoma", "íleo", "metástase", "diabetes-mellitus-insipidus", "carcinoma-in-situ"],
    "duplas_greco_latinas": ["nefr/o × ren/o", "oftalm/o × ocul/o", "ot/o × aur/o", "odont/o × dent/o", "gloss/o × lingu/o", "derm/o × cutane/o", "fleb/o × ven/o", "pneum/o × pulmon/o", "hister/o × uter/o", "orqu/o × testicul/o", "mast/o × mam/o", "encefal/o × cerebr/o"],
    "farmacologia_linguagem": ["farmacocinética × farmacodinâmica", "potência × eficácia", "agonista total × parcial × inverso", "antagonista competitivo × não competitivo", "tolerância × taquifilaxia", "dependência × abstinência", "efeito adverso × toxicidade × contraindicação"],
    "nomenclatura_anatomica_latina": ["musculus", "nervus", "arteria", "vena", "ligamentum", "foramen", "sulcus", "fossa", "facies", "ramus", "caput", "corpus"],
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = s.replace("-", "").replace("/", "").replace("×", "x")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def covered(target: str, haystacks: list[str]) -> bool:
    n = norm(target)
    # Famílias comparativas só contam como cobertas quando todos os membros aparecem.
    members = [norm(x) for x in re.split(r"\s*×\s*", target)]
    if len(members) > 1:
        return any(all(m in h for m in members) for h in haystacks)
    return any(n == h or n in h for h in haystacks)


def main() -> int:
    rows = json.loads(LEXICON.read_text(encoding="utf-8"))
    hay = [norm(" | ".join(str(r.get(k, "")) for k in
           ("entrada_canonica", "contrastes", "exemplos", "conceito_complementar"))) for r in rows]
    domains = {}
    for domain, targets in TARGETS.items():
        present = [x for x in targets if covered(x, hay)]
        missing = [x for x in targets if x not in present]
        domains[domain] = {"target": len(targets), "covered": len(present),
                           "coverage_pct": round(100 * len(present) / len(targets), 1),
                           "present": present, "missing": missing}
    if HOLDOUT.exists():
        holdout_rows = json.loads(HOLDOUT.read_text(encoding="utf-8"))
        inference_terms = {x["term"] for x in holdout_rows if not x.get("seen_in_cards")}
    else:
        inference_terms = set()
        for r in rows:
            inference_terms.update(x.strip() for x in re.split(r"[;|,]", str(r.get("termos_de_inferencia", ""))) if x.strip())
    payload = {
        "lexicon_entries": len(rows), "domains": domains,
        "reserved_inference_terms": len(inference_terms), "reserved_target": 300,
        "selection_policy_v3": {
            "formula": "Q = 3T + 3C + 2E + 2R + F - 2O",
            "T": "transferência (0–2)", "C": "risco de confusão (0–2)",
            "E": "déficit de exposição (0–2)", "R": "reutilização (0–3)",
            "F": "frequência curricular (0–3)", "O": "obviedade para o estudante (0–2)",
            "rule": "Frequência não vence sozinha; baixa exposição e confusão elevam prioridade, obviedade reduz cards isolados."
        },
        "required_next_blocks": [
            "procedimentos e sufixos raros", "forma e microarquitetura anatômica",
            "semiologia discriminativa", "patologia discriminativa",
            "polissemias e falsas segmentações", "duplas greco-latinas",
            "linguagem farmacológica", "nomenclatura anatômica latina", "300 termos inéditos realmente reservados"
        ]
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Auditoria adversarial de cobertura v3", "",
             f"- Entradas no léxico mestre: {len(rows)}",
             f"- Termos de inferência efetivamente reservados: {len(inference_terms)}/300", "",
             "## Resultado por eixo", "",
             "| Eixo | Cobertos | Meta | Cobertura |", "|---|---:|---:|---:|"]
    for domain, d in domains.items():
        lines.append(f"| {domain.replace('_', ' ')} | {d['covered']} | {d['target']} | {d['coverage_pct']}% |")
    lines += ["", "## Lacunas explícitas", ""]
    for domain, d in domains.items():
        lines += [f"### {domain.replace('_', ' ').title()}", "",
                  (", ".join(d["missing"]) if d["missing"] else "Nenhuma lacuna no inventário mínimo."), ""]
    lines += ["## Mudança de seleção", "",
              "A frequência deixa de ser o principal atalho. O próximo núcleo usa `Q = 3T + 3C + 2E + 2R + F - 2O`.", "",
              "- `E` premia baixa exposição: termos vistos raramente, mas cuja confusão custa rigor.",
              "- `C` premia famílias confundíveis e polissemias.",
              "- `O` penaliza cards isolados óbvios, como derm/o → pele.",
              "- Termos óbvios só entram como suporte de aplicação mais difícil.", "",
              "## Consequência para o deck completo", "",
              "O deck não será uma lista de raízes frequentes. Será organizado em camadas: método, famílias, raízes não óbvias, aplicação inédita e limites da inferência."]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({k: {"covered": v["covered"], "target": v["target"], "pct": v["coverage_pct"]} for k, v in domains.items()}, ensure_ascii=False, indent=2))
    print(f"holdout: {len(inference_terms)}/300")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
