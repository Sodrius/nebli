---
description: Gera caderno de questões (UC + prova) via CADERNISTA
argument-hint: <UC1|UC2> <P1|P2|P3|HISTORICO>
---

Argumentos recebidos: $ARGUMENTS

Delegue ao subagente **cadernista** (`.claude/agents/cadernista.md`) com o seguinte prompt:

> Gerar caderno de questões para UC + prova especificados: $ARGUMENTS. Rodar `python typst-build/pipeline_caderno.py --uc <UC> --prova <PROVA>`. Pipeline interno valida cronograma → gera .typ → compila PDF → audita → verifica gabarito. Reportar ao final: caminho do PDF gerado, contagem de questões (objetivas + discursivas), eventuais warnings da auditoria (ascii residual, hifenização). Bloqueia em mojibake ou gabarito inconsistente.

Se argumentos faltarem ou forem inválidos (UC fora de [UC1, UC2] ou prova fora de [P1, P2, P3, HISTORICO]), pergunte ao Davi com opções numeradas antes de delegar.
