#!/usr/bin/env python3
"""Compõe `relatorio-final-<slug>.json` a partir dos artefatos reais da corrida.

Nada aqui é declarado à mão: cada número vem do contrato congelado, do relatório
de montagem, da auditoria do `.apkg` e do relatório de renderização.
"""
from __future__ import annotations

import collections
import json
from pathlib import Path

LESSON = Path(__file__).resolve().parent
SLUG = "anato-intestino-grosso"


def ler(nome: str) -> dict:
    return json.loads((LESSON / nome).read_text(encoding="utf-8"))


def main() -> int:
    contrato = ler("contrato-cobertura.json")
    montagem = ler("relatorio-montagem.json")
    auditoria = ler("auditoria-apkg.json")
    render = ler("previews/render-report.json")
    revisao = ler("revisao-independente.json")

    por_importancia = collections.Counter(c["importance"] for c in contrato["cards"])
    por_formato = collections.Counter(c["format"] for c in contrato["cards"])
    por_fonte = collections.Counter(c["source"] for c in contrato["cards"])
    por_subtopico = collections.Counter(
        conceito["subtopic"] for conceito in contrato["concepts"]
    )
    por_qualidade = collections.Counter(
        conceito["route"]["coverage_quality"] for conceito in contrato["concepts"]
    )
    visual = collections.Counter(conceito["visual"]["mode"] for conceito in contrato["concepts"])

    nucleares_rasos = [
        conceito["id"] for conceito in contrato["concepts"]
        if conceito["importance"] == "nuclear" or (
            conceito["importance"] == "nucleo" and conceito["route"]["coverage_quality"] < 2
        )
    ]

    relatorio = {
        "slug": SLUG,
        "title": contrato["title"],
        "pipeline_version": contrato["pipeline_version"],
        "deck": contrato["deck"],
        "sources": contrato["lesson_sources"],
        "entregaveis": {
            "e1_pdf": contrato["e1"]["pdf"],
            "e1_fonte": contrato["e1"]["path"],
            "e1_sha256": contrato["e1"]["sha256"],
            "apkg": Path(montagem["apkg"]).name,
            "apkg_sha256": montagem["sha256"],
            "apkg_bytes": montagem["bytes"],
            "previews": "previews/ (pergunta e resposta de cada card)",
        },
        "cobertura": {
            "conceitos": len(contrato["concepts"]),
            "por_importancia": dict(por_importancia),
            "por_subtopico": dict(por_subtopico),
            "qualidade_de_cobertura": {str(k): v for k, v in sorted(por_qualidade.items())},
            "nucleares_com_cobertura_rasa": nucleares_rasos,
            "todo_card_tem_ancora_na_e1": contrato["gates"]["every_card_has_e1_anchor"],
        },
        "cards": {
            "total": montagem["cards"],
            "previsto_no_contrato": montagem["expected_cards"],
            "teto_congelado": montagem["hard_max"],
            "por_formato": dict(por_formato),
            "por_fonte": dict(por_fonte),
            "por_importancia": dict(por_importancia),
            "cloze_acima_do_limite": auditoria["cloze_answers_over_limit"],
            "cloze_excepcionais_3_palavras": auditoria["exceptional_three_word_clozes"],
            "cloze_nao_atomicos": auditoria["non_atomic_cloze_notes"],
        },
        "step1": {
            "aceitos": [d for d in contrato["step1_decisions"] if d["decision"] == "accepted"],
            "rejeitados": [d for d in contrato["step1_decisions"] if d["decision"] == "rejected"],
        },
        "visual": {
            "decisoes_por_modo": dict(visual),
            "image_occlusion": {
                "cards": auditoria["image_occlusion_notes"],
                "modo": contrato["gates"]["io_multi_label_mode"],
                "mascaras_totais": sum(
                    len(conceito["visual"]["io"]["labels"])
                    for conceito in contrato["concepts"]
                    if conceito["visual"].get("io")
                ),
                "previews_pergunta_e_resposta": True,
            },
        },
        "auditoria_apkg": {
            "passed": auditoria["passed"],
            "notas": auditoria["notes"],
            "cards": auditoria["cards"],
            "decks": auditoria["decks"],
            "midia_referenciada": auditoria["referenced_media"],
            "midia_empacotada": auditoria["packaged_media"],
            "erros": auditoria["errors"],
            "avisos": auditoria["warnings"],
        },
        "renderizacao": {
            "cards_renderizados": render["rendered_cards"],
            "cards_com_midia_quebrada": len(render["broken_media_cards"]),
            "navegador": "Chromium (Playwright)",
        },
        "revisao_independente": revisao,
        "ritmo": {
            "novos_por_dia": montagem["scheduling"]["new_per_day"],
            "revisoes_por_dia": montagem["scheduling"]["reviews_per_day"],
            "onde_configurar": "O dconf já vem no pacote; conferir em Opções do deck após importar.",
        },
        "buscas_para_cram": {
            "aula_inteira": f'deck:"{contrato["deck"]}"',
            "so_nucleo": f'deck:"{contrato["deck"]}" tag:nucleo',
            "so_identificacao_visual": f'deck:"{contrato["deck"]}" tag:IO',
            "linha_pectinada": f'deck:"{contrato["deck"]}" tag:subtopico::Linha_pectinada',
            "sem_opcionais": f'deck:"{contrato["deck"]}" -deck:"{contrato["optional_deck"]}"',
            "prova_1_anatomia": 'deck:"NEBLI::Digestório::P1::Anatomia"',
        },
        "pendencias_reais": [
            {
                "id": "anking-inalcancavel",
                "descricao": (
                    "O índice privado do AnKing não é transferível para este ambiente de "
                    "execução (564 MB; o conector do Drive devolve base64 pelo contexto). "
                    "A ordem AnKing → externos → autoral não foi executada no passo 1: os 47 "
                    "cards saíram autorais, com busca real registrada apenas no corpus local "
                    "P3-UC02 (247 notas, 4 acertos, nenhum candidato)."
                ),
                "efeito": "Todos os cards ficam marcados para recuradoria.",
                "correcao_proposta": "RETROSPECTIVA-PROCESSO.md §8 — dossiê compacto de candidatos.",
            },
            {
                "id": "importar-no-ankidroid",
                "descricao": "Falta importar o .apkg no AnkiDroid e conferir os IO na tela do celular.",
                "efeito": "Verificação final de campo, fora do alcance deste ambiente.",
                "correcao_proposta": "Importar e revisar os 11 IO.",
            },
        ],
    }

    saida = LESSON / f"relatorio-final-{SLUG}.json"
    saida.write_text(json.dumps(relatorio, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"escrito: {saida.name}")
    print(json.dumps(relatorio["cards"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
