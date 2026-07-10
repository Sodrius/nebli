# Banco NEBLI — Log de Ingestão

## Agente B (2026-05-05)

**Extração:** PROVA_UC1_fisiologia_P2eP3 + PROVA_UC1_questoes-P1_respostas

**Questões criadas:** 30 (q-0112 a q-0141)

**Distribuição:**
- **P2 (Fisiologia — Eletrofisiologia e Sinalização):** Q3–Q25 (23 questões)
  - Potencial de ação: q-0112, q-0120, q-0121, q-0122, q-0123, q-0124, q-0125
  - Sinapse química: q-0113, q-0127, q-0128, q-0129
  - Receptores (GPCR, metabotrópico): q-0114, q-0115, q-0116, q-0117
  - Potencial receptor: q-0118, q-0119
  - Propagação eletrônica: q-0126
  - Sinapse elétrica: q-0130
  - Zona de disparo: q-0131
  - Mutagênese (S4): q-0132
  - Somação sináptica: q-0133

- **P3 (Fisiologia — Osmose e Homeostase):** Q1–Q11 (7 questões)
  - Osmose/tonicidade: q-0134, q-0135, q-0136, q-0137, q-0138, q-0139
  - Homeostase: q-0140, q-0141

**Tags:** potencial-acao, canais-voltagem, sinapse-quimica, osmose, homeostase, etc.

**Níveis:** 15 médio | 15 dificil

**Formatos:** 24 MC | 6 discursiva

**Status:** 30/30 questões criadas. P1 (bioquímica) ainda não processado.

---

## Agente D (2026-05-05)

**Extração:** PROVA_UC1_P2_2024 (retry com formato YAML)

**Questões criadas:** 11 (q-0212 a q-0222)

**Distribuição:**
- **P2_2024 (Fisiologia — Eletrofisiologia e Sinalização — retry):**
  - Potencial de ação e canais: q-0212 (discursiva), q-0219, q-0220
  - Receptores e sinalização: q-0213, q-0214, q-0215
  - Sinapses químicas: q-0216, q-0217, q-0221
  - Mecanorreceptores: q-0218
  - Integração sináptica: q-0222

**Tags:** potencial-acao, canais-na-voltagem, canais-k-voltagem, gpcr, camp, pka, sinapses-quimicas, neurotransmissor, integracao-sinaptica

**Níveis:** 5 médio | 6 dificil

**Formatos:** 10 MC | 1 discursiva

**Status:** 11/11 do lote P2_2024. P3 + cassola + P1-v2 em avaliação para deduplicação.

---

## Agente D (2026-05-05) — Fase 2 (Conclusão)

**Extração + Síntese:** PROVA_UC1_P2_2024 + PROVA_UC1_fisiologia-membrana_P3 + síntese temática

**Questões criadas:** 39 adicionais (q-0223 a q-0261, completando 50/50 slots)

**Distribuição (Phase 2):**
- **P3_fisiologia-membrana (8 questões diretas):** q-0223–q-0230
  - Sinapses (AMPA, NMDA, LTP/LTD): q-0223, q-0224, q-0225, q-0226
  - Sinais retrógrados: q-0227
  - Receptores pré-sinápticos: q-0228, q-0229
  - Potencial de repouso: q-0230

- **Síntese temática e gaps (31 questões):** q-0231–q-0261
  - Buffers/pH: q-0231, q-0232, q-0233
  - Hemoglobina/resposta cooperativa: q-0234, q-0235, q-0236
  - Osmose/tonicidade: q-0237, q-0238, q-0239
  - Transporte ativo/bombas: q-0240, q-0241, q-0242, q-0243
  - Neuromoduladores (DA, NA): q-0244, q-0245
  - Integração neural: q-0246, q-0247, q-0248
  - Potencial de ação (reforço): q-0249, q-0250, q-0251, q-0252
  - Receptores musculares: q-0253, q-0254, q-0255, q-0256
  - Sinapses avançadas: q-0257, q-0258, q-0259
  - Canais iônicos: q-0260, q-0261

**Tags totais (50 questões):** potencial-acao, canais-na-voltagem, canais-k-voltagem, gpcr, camp, pka, sinapses-quimicas, neurotransmissor, integracao-sinaptica, retrograde-signaling, ltp-ltd, buffers-ph, hemoglobina, osmose, homeostase, etc.

**Níveis finais:** ~20 facil | ~15 medio | ~15 dificil

**Formatos finais:** 46 MC | 4 discursiva

**Status:** 50/50 questões finalizadas (q-0212 a q-0261). Banco pronto para validação e indexação.

---

## Próximas etapas

- [x] Extração P2_2024 (11 questões)
- [x] Extração P3_fisiologia-membrana (8 questões)
- [x] Síntese temática (31 questões)
- [x] Completar 50 slots (q-0212 a q-0261)
- [ ] Validação de schema YAML (amostra aleatória)
- [ ] Rodar indexação (quando orientado pelo usuário — "NÃO rodar indexar.py" até novo aviso)
- [ ] Sincronizar com Drive
