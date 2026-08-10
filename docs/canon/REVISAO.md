# Revisão

Revisores são independentes e somente leitura. Recebem contrato, E1, manifestos
e APKG já produzidos. Não geram conteúdo e não aplicam correções.

Cada relatório separa:

- `BLOCK`: impede entrega;
- `FIX`: correção recomendada;
- `NOTE`: observação sem mudança obrigatória;
- `FALSE_POSITIVE`: regra não aplicável com justificativa.

O revisor de cobertura verifica fontes → E1 → contrato → cards e o limite Step 1.
O revisor de cards/visual verifica atomicidade, origem, pertinência e IO. O
auditor APKG verifica o artefato importável. A sessão principal decide e corrige,
registrando o destino de cada `BLOCK`/`FIX` no checkpoint.
