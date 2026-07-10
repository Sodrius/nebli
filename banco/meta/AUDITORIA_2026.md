# AUDITORIA DO BANCO DE QUESTÕES — 2026-05-13

## Resumo Geral

| Métrica | Valor |
|---------|-------|
| **Total de questões** | 228 |
| **Sem `armadilha`** | 152 (67%) |
| **Sem `ano`** | 91 (40%) |
| **Sem `uc_origem`** | 3 (1%) |
| **Sem `conceito_central`** | 0 ✅ |
| **Sem `id`** | 0 ✅ |
| **Sem `tags`** | 0 ✅ |
| **Sem `nivel`** | 0 ✅ |
| **Sem `formato`** | 0 ✅ |
| **Sem `gabarito`** | 0 ✅ |

---

## Campos Obrigatórios — Status

Todos os 6 campos obrigatórios (`id`, `tags`, `nivel`, `formato`, `conceito_central`, `gabarito`) estão presentes em **100% das 228 questões**. Nenhuma ação necessária.

---

## Campos Pedagógicos — Problemas Encontrados

### 1. Sem `armadilha` — 152 questões (67%)

Padrão identificado: o campo `armadilha` foi introduzido após os primeiros ~75 arquivos e não foi retroativamente preenchido nos blocos q-0076–q-0105, q-0112–q-0141, q-0142–q-0170 e q-0212–q-0279.

**Lista de IDs:**

q-0076, q-0077, q-0078, q-0083, q-0084, q-0085, q-0086, q-0087, q-0088, q-0089,
q-0090, q-0091, q-0092, q-0093, q-0094, q-0095, q-0096, q-0097, q-0098, q-0099,
q-0100, q-0101, q-0102, q-0104, q-0105, q-0112, q-0113, q-0114, q-0115, q-0116,
q-0117, q-0118, q-0119, q-0120, q-0121, q-0122, q-0123, q-0124, q-0125, q-0126,
q-0127, q-0128, q-0129, q-0130, q-0131, q-0132, q-0133, q-0134, q-0135, q-0136,
q-0137, q-0138, q-0139, q-0140, q-0141, q-0142, q-0143, q-0144, q-0145, q-0146,
q-0147, q-0148, q-0149, q-0150, q-0151, q-0152, q-0153, q-0154, q-0155, q-0156,
q-0157, q-0158, q-0159, q-0160, q-0161, q-0162, q-0163, q-0164, q-0165, q-0166,
q-0167, q-0168, q-0169, q-0170, q-0212, q-0213, q-0214, q-0215, q-0216, q-0217,
q-0218, q-0219, q-0220, q-0221, q-0222, q-0223, q-0224, q-0225, q-0226, q-0227,
q-0228, q-0229, q-0230, q-0231, q-0232, q-0233, q-0234, q-0235, q-0236, q-0237,
q-0238, q-0239, q-0240, q-0241, q-0242, q-0243, q-0244, q-0245, q-0246, q-0247,
q-0248, q-0249, q-0250, q-0251, q-0252, q-0253, q-0254, q-0255, q-0256, q-0257,
q-0258, q-0259, q-0260, q-0261, q-0262, q-0263, q-0264, q-0265, q-0266, q-0267,
q-0268, q-0269, q-0270, q-0271, q-0272, q-0273, q-0274, q-0275, q-0276, q-0277,
q-0278, q-0279

---

### 2. Sem `ano` — 91 questões (40%)

Padrão: blocos q-0112–q-0141 e q-0212–q-0261 inteiros sem `ano`; faixa q-0269–q-0279 também.

**Lista de IDs:**

q-0112, q-0113, q-0114, q-0115, q-0116, q-0117, q-0118, q-0119, q-0120, q-0121,
q-0122, q-0123, q-0124, q-0125, q-0126, q-0127, q-0128, q-0129, q-0130, q-0131,
q-0132, q-0133, q-0134, q-0135, q-0136, q-0137, q-0138, q-0139, q-0140, q-0141,
q-0212, q-0213, q-0214, q-0215, q-0216, q-0217, q-0218, q-0219, q-0220, q-0221,
q-0222, q-0223, q-0224, q-0225, q-0226, q-0227, q-0228, q-0229, q-0230, q-0231,
q-0232, q-0233, q-0234, q-0235, q-0236, q-0237, q-0238, q-0239, q-0240, q-0241,
q-0242, q-0243, q-0244, q-0245, q-0246, q-0247, q-0248, q-0249, q-0250, q-0251,
q-0252, q-0253, q-0254, q-0255, q-0256, q-0257, q-0258, q-0259, q-0260, q-0261,
q-0269, q-0270, q-0271, q-0272, q-0273, q-0274, q-0275, q-0276, q-0277, q-0278,
q-0279

---

### 3. Sem `uc_origem` — 3 questões (1%)

**Lista de IDs:** q-0259, q-0260, q-0261

---

## Observações

- O campo `armadilha` é o mais crítico para preenchimento retroativo — afeta 2/3 do banco.
- Os blocos sem `ano` coincidem parcialmente com os sem `armadilha`, sugerindo que foram ingeridos em lote sem esses metadados.
- As 3 questões sem `uc_origem` (q-0259–q-0261) também estão sem `armadilha` e `ano` — verificar origem manual.
- **IDS_SEM_ARMADILHA.txt** foi gerado na mesma pasta para uso em scripts de enriquecimento em lote.

---

*Gerado automaticamente em 2026-05-13*
