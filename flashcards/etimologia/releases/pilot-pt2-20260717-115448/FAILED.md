# Execução incompleta

A sincronização criou e suspendeu as notas, mas o verificador inicial procurou um campo `suspended` inexistente em `cardsInfo`.

O gate foi corrigido para consultar `is:suspended`. A release válida e completa é `pilot-pt2-20260717-115546`.

