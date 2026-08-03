#!/usr/bin/env python3
"""Materializa a seleção card-a-card AnKing para o deck-teste completo."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bioq-20-pentoses-radicais-livres-teste-completo"
POOL_SLUG = "bioq-20-pentoses-radicais-livres-teste"
DECK = "NEBLI::TESTE_APAGAR::Bioquímica::Via das pentoses — completo"

# Seleção deliberada do pool real: cada GUID foi lido no pool e casa um fato da E1.
KEEP = [
    ("De1m5OEf4j", "localização", "citosol"), ("RaEDQ5]]10", "G6PD", "passo limitante"),
    ("kD4h(2?{>4", "NADPH", "função biossintética"), ("dxAS[ISwR7", "ribose", "precursor de nucleotídeos"),
    ("HPd&LdGTSj", "visão geral", "sinônimo HMP"), ("DkO](+hW%-", "visão geral", "não usa ATP"),
    ("o8,26,Y&]~", "tecidos", "tecidos de alta atividade"), ("e,lljGR7?S", "oxidativa", "G6P até ribulose"),
    ("sVq]8w|)=y", "oxidativa", "saldo NADPH e CO2"), ("PRUpVM*i5+", "oxidativa", "irreversibilidade"),
    ("ih8HIyFIk-", "ribose", "ribulose para ribose"), ("Iyy]|!MP+X", "NADPH", "lipogênese hepática"),
    ("yWqtbkb`0^", "NADPH", "oxidase de neutrófilos"), ("rKBHTacy;)", "hemácia", "redução de H2O2"),
    ("kg.u)A]t,2", "glutationa", "GSSG para GSH"), ("mE}6gDA!&i", "glutationa", "glutationa redutase usa NADPH"),
    ("jUF4v|84_]", "G6PD", "primeira reação produz NADPH"), ("0*#qZdz=w", "glutationa", "GSH para GSSG"),
    ("CP:0.`KnC.`", "glutationa", "peroxidase remove H2O2"), ("pwbs?YbRFb", "G6PD deficiência", "Heinz bodies"),
    ("BL/E.K+A{j", "G6PD deficiência", "hemoglobina desnaturada"), ("y<S*dg#:?{", "não oxidativa", "B1 para transcetolase"),
    ("k8$^{ST^)3", "G6PD deficiência", "herança ligada ao X"), ("i+FczPGWU9", "hemácia", "fonte de estresse oxidativo"),
    ("Jk/cgK.iLY", "glutationa", "GSH neutraliza H2O2"), ("bK!25KI#Qc", "glutationa", "G6PD-NADPH-GSH"),
    ("M_4=n14ge$", "G6PD deficiência", "suscetibilidade oxidativa"), ("z;/L<+/|1.", "G6PD deficiência", "proteção parcial contra malária"),
    ("end43ObgsH", "G6PD deficiência", "cadeia oxidativa até Heinz"), ("b0#~aAYzGn", "gatilhos", "infecção"),
    ("w+]0}+^93D", "gatilhos", "favas"), ("n5fCjT7B|r", "gatilhos", "primaquina"),
]


def main() -> None:
    pool_path = ROOT / "arquivos-trabalho" / f"anking-pool-{POOL_SLUG}.json"
    pool = json.loads(pool_path.read_text(encoding="utf-8"))["cards"]
    by_guid = {row["guid"]: row for row in pool}
    missing = [guid for guid, *_ in KEEP if guid not in by_guid]
    if missing:
        raise SystemExit("GUIDs ausentes do pool: " + ", ".join(missing))
    kept = [{"guid": guid, "conceito": concept, "motivo": reason,
             "raw0": by_guid[guid]["raw0"], "front": by_guid[guid]["front"]}
            for guid, concept, reason in KEEP]
    spec = {"slug": SLUG, "target_deck": DECK, "tag_ancora": f"NEBLI::{SLUG}", "kept": kept}
    out = ROOT / "flashcards" / "curadoria" / f"{SLUG}-curado.json"
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = ROOT / "flashcards" / "curadoria" / f"{SLUG}.md"
    lines = ["# Curadoria AnKing — Via das pentoses (deck-teste completo)", "", f"**Deck:** `{DECK}`", "", f"**Cards reais selecionados:** {len(kept)}", "", "| GUID | Conceito E1 | Motivo |", "|---|---|---|"]
    lines += [f"| `{x['guid']}` | {x['conceito']} | {x['motivo']} |" for x in kept]
    lines += ["", "Cobertura adicional autoral só é permitida para lacunas de rearranjo não-oxidativo, cenários de fluxo e regulação; todos os fatos clínicos e bioquímicos existentes no pool foram priorizados acima."]
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OK: {len(kept)} reais -> {out}")


if __name__ == "__main__":
    main()
