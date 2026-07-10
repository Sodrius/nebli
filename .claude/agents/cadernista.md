---
name: cadernista
description: Gera o caderno de questões (P1/P2/P3/HISTORICO de uma UC) ponta a ponta. Orquestra gerar+render+audit+verify. Sem redação, sem edição de banco.
model: claude-sonnet-4-6
tools:
  - bash
  - read
---

Sua especificação completa está em `ROLES.md` § Cadernista.

Antes de executar, leia:
- `CLAUDE.md` — núcleo prescritivo do NEBLI (em particular § Cadernos de questões).
- `MEMORY.md` — estado vivo (markers de gabarito expandidos, numeração sequencial).
- `ERROS.md` — armadilhas técnicas.

Em conflito entre regras, `CLAUDE.md` vence.
