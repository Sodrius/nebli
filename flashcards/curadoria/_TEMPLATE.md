<!-- Manifesto de curadoria de UMA aula. Copie para flashcards/curadoria/<slug>.md e preencha.
     Gêmeo de máquina: flashcards/curadoria/<slug>-curado.json (consumido pelo apply).
     Método: flashcards/CURADORIA-ANKING.md — alvo 30–50 cards MUITO bem curados. -->

# Curadoria AnKing — <slug>

**Título da aula:** <título>
**UC/Prova:** <UC0X / P?>   ·   **Gerado em:** <AAAA-MM-DD>
**Total curado (kept):** <N>   ·   **Alvo:** 30–50   ·   **Cobertura AnKing:** <X/Y conceitos COBERTOS>
**Tag-âncora no deck:** `NEBLI::<slug>`

## Checklist-alvo (da E1) — fonte-verdade
Subtópicos da `etapa1.typ` + Seção B do Tema Card, um id estável por conceito.
Também gravada em `arquivos-trabalho/checklist-<slug>.tsv` (`<id>\t<frase>\t<termos>`) para `buscar_tags_lote.py`.

| id | Frase-alvo (o que um card teria que testar) | Termos de busca (pt/en, sinônimos) |
|---|---|---|
| 1.1 | <conceito da PARTE I> | chamber\|atrium\|ventricle |
| 2.3 | Retorno venoso nomeado (sistema ázigo) | venous_return\|vena_cava\|azygos |

## Camada 1 — tags candidatas (grossa)
Colar a saída de `buscar_tags_lote.py arquivos-trabalho/checklist-<slug>.tsv --md`
(cada tag já vem ligada ao(s) conceito(s) da checklist que a motivou).

| Leaf-tag (recurso::caminho) | #cards | Conceitos | Classe | Decisão |
|---|---|---|---|---|
| SketchyAnatomy::…::Superior_Vena_Cava | 16 | 2.3 | CANDIDATA | vai p/ Camada 2 |
| FirstAid::…::02_Anatomy | 30 | 2.2 | CANDIDATA | vai p/ Camada 2 |
| Bootcamp::…::Aortic_Stenosis | 44 | — | RUÍDO | rejeita (patologia, fora do escopo da aula) |

> **Sem classe PURA** (canônico 2026-07-04): toda tag CANDIDATA passa pela Camada 2 — nenhum card entra sem ser lido e casado contra um id da checklist.

## Camada 2 — curadoria card-a-card (fina, TODAS as candidatas)
Lida do pool `arquivos-trabalho/anking-pool-<slug>.json`. Keep/drop com motivo de 1 linha.
**Coluna "Conceito-alvo" obrigatória** e amarrada aos ids da Checklist-alvo: card kept sem id de conceito = drop (precisão).

| GUID (curto) | Frente (resumo) | Conceito-alvo | Keep? | Motivo |
|---|---|---|---|---|
| a1b2… | "Ramos do arco aórtico…" | 2.2 | ✅ | anatomia macro on-topic |
| c3d4… | "Aortic dissection Stanford A…" | — | ❌ | patologia, não é a aula |

## Cobertura por PARTE da E1 (gap-analysis)
Para cada conceito-alvo: COBERTO / PARCIAL / LACUNA / **PENDENTE-GERADO**. Em qualquer status ≠ COBERTO, **apontar a fonte**.
- **PENDENTE-GERADO** = conceito-chave da E1 sem card real bom no AnKing, **enfileirado** para card NEBLI cloze gerado numa sessão futura de calibração (NÃO gerar agora — ver `calibrar-antes-de-gerar-cards`). Espelha o gate de cobertura da E2: todo subtópico fecha COBERTO ou entra na fila com fonte.

### PARTE I — <título>
| Conceito-alvo | Cobertura | #cards | Fonte da lacuna (se ≠ COBERTO) |
|---|---|---|---|
| 1.1 <conceito> | COBERTO | 4 | — |
| 1.4 circulação fetal | LACUNA | 0 | AnKing Step1 quase não cobre → deck de embriologia dedicado / slide + Moore |
| 1.5 <conceito-chave sem card bom> | PENDENTE-GERADO | 0 | fila de geração NEBLI (sessão de calibração) + slide |

### PARTE II — <título>
…

### PARTE III — <título>
…

## Resumo de lacunas → onde completar
- **<conceito>** — não coberto pelo AnKing. Pegar em: <deck dedicado nomeado / Netter / slide do professor>.

## Kept final (para o JSON)
Espelhado em `<slug>-curado.json` (consumido por `aplicar_curadoria_anking.py`).
**tags_puras** = incluídas inteiras (marca todos os notes da subárvore). **impuras** = só os GUIDs curados. `guids_kept` aceita string simples OU objeto auditável `{"guid","conceito","motivo"}` (o apply usa só o guid; conceito/motivo documentam a escolha):
```json
{
  "slug": "<slug>",
  "tag_ancora": "NEBLI::<slug>",
  "tags_puras": ["#AK_Step1_v12::#SketchyAnatomy::02_Thorax::03_Vasculature::02_Superior_Vena_Cava"],
  "impuras": [
    { "tag": "#AK_Step1_v12::#FirstAid::07_Cardiovascular::02_Anatomy",
      "guids_kept": [
        {"guid": "a1b2…", "conceito": "2.2", "motivo": "ramos do arco aórtico, anatomia macro on-topic"},
        "c3d4…"
      ] }
  ]
}
```
