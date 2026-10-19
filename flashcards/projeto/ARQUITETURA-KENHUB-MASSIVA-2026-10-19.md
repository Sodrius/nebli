# Arquitetura Kenhub massiva — decisão de 19/10/2026

## Dois destinos, sem misturar papéis

1. `modo=neuro_uc07`: Neuroanatomia completa permanece em `NEBLI::UC07`, com Kenhub-first, AnKing/AnatoKing pertinente, função, relações, texto do quiz e complementos necessários. A árvore visível segue a ordem oficial do Kenhub por prefixos numéricos estáveis.
2. `modo=referencia_kenhub`: todo o restante entra inicialmente como acervo puro em `Referências::Referências Externas::Kenhub`. Não recebe AnKing, AnatoKing nem complemento autoral nessa etapa.
3. `modo=aula_anatomia`: quando uma aula específica usar aquele conteúdo, o deck didático parte do Kenhub-first e só então seleciona AnKing/AnatoKing e poucos cards de função, relações e lacunas. O acervo Kenhub passa a ser mais uma fonte, não uma aula pronta.

## Pipeline massivo proposto

1. Manifesto determinístico: IDs, ordem oficial de módulo/unidade, destino, títulos sem prefixo e hashes.
2. Coleta incremental e cacheada: estruturas, texto/quiz e mídia; nenhuma IA.
3. Normalização local: identidade global de estrutura/vista, português oficial, mídia, duplicatas e cobertura.
4. Produtor Luna por unidade/estrutura: recebe somente fonte ligada, regras condensadas e JSON schema fechado; nunca toca o Anki.
5. Gates locais em 100%: schema, cobertura, ordem, identidade, mídia, privacidade, formato, fontes permitidas e idempotência.
6. Revisor Luna independente: compara cards apenas com a fonte da unidade.
7. Regulador forte por exceção: lê divergências, baixa confiança, tradução não atestada, duplicata aproximada, relação ambígua, falha semântica e uma amostra aleatória dos aprovados.
8. Renderização fora do Anki; revisão por risco/amostra no modo massivo. A Neuro/UC07 mantém a revisão integral prometida.
9. Uma escrita idempotente em lote quando o Anki estiver livre; sync apenas no fechamento combinado.

## Gates a implementar antes da escala

- G31 árvore exibida: hierarquia viva do Anki coincide com o manifesto numerado.
- G32 modo puro: referência Kenhub não contém AnKing, AnatoKing ou autoral.
- G33 composição: aula anatômica começa por Kenhub quando houver material correspondente.
- G34 proveniência estruturada, sem fonte escrita no card.
- G35 identidade global: sinônimos não duplicam estrutura; vistas pedagogicamente diferentes não são colapsadas.
- G36 função/relação: no modo aula, estrutura-chave recebe cobrança útil de função e/ou relação quando aplicável.
- G37 pacote mínimo e métrica de tokens.
- G38 toda divergência/baixa confiança chega ao regulador.
- G39 hash idêntico não escreve no Anki.
- G40 orçamento e qualidade: tokens/card, cache, escaladas, falhas e retrabalho.

## Segurança da promoção referência → aula

- Nota ativa pode ser associada.
- Nota totalmente suspensa pode migrar para a aula nova sem associação, preservando ID, histórico e comentário.
- Nunca remover tags pessoais ou associações de outras aulas.
- Toda migração tem snapshot e rollback.
- Nada é apagado automaticamente; retirada é suspensa e recuperável.

## Sequência

1. Passagem rápida nas 41 unidades existentes da UC07.
2. Ordenar de verdade a árvore visível da UC07.
3. Terminar as dez unidades restantes de Neuroanatomia na ordem do Kenhub.
4. Fazer a revisão profunda das unidades existentes na rodada combinada.
5. Congelar o manifesto global, excluindo Neuro da fila externa.
6. Pilotar `referencia_kenhub` em 2–3 unidades não neuroanatômicas diferentes.
7. Medir custo e erro; só então liberar produção massiva.

## Economia de tokens sem perda de qualidade

- Tudo que é ordenação, cobertura, schema, mídia, hash e duplicação fica em código.
- Cache por `hash(fonte + prompt + schema + glossário)`.
- Uma unidade por chamada; no máximo 2–3 exemplos realmente análogos.
- Luna produz; outro Luna revisa; regulador forte lê somente exceções e amostra.
- Erro recorrente vira gate determinístico, reduzindo chamadas futuras.
- Lotes seguem blocos de estrutura, não um número arbitrário de cards.
