# Papéis — roteamento atual
E1 + cards são conduzidos pela sessão executora conforme `flashcards/projeto/README.md`. Não há necessidade de delegação ou modelo fixo como condição de qualidade. Ler as instruções aplicáveis integralmente; responsabilidade de verificação permanece com quem entrega.

- E1: `didatica/E1.md`, EXEMPLARES.md, ANTI-EXEMPLARES.md, ajustes-finos-recentes.md; preserve didática e precisão.
- Cards: MEMORY.md, EXECUCAO-DECK-AULA, FEEDBACKS e ACERVOS-REFERENCIA, pela ordem do README.
- Revisão: passes separados de precisão/recorte, didática/recuperação, imagens/renderização e identidade/entrega; não confundir um com outro.
- Compilação: modo somente-E1, saída isolada, template atual e revisão textual/visual. Detalhes atuais em didatica/E1.md.
- Questionador/E2/E3/RemNote: papéis aposentados do fluxo atual; íntegra no arquivo histórico, não carregar como instrução de nova aula.
- Critérios extensos de revisores e detalhes técnicos legados continuam em `backups/contexto-2026-09-25/ROLES.md`, consultáveis por seção; regras atuais prevalecem.

## § Cadernista
Responde "faça/gere/monta o caderno da prova X da matéria Y" rodando `pipeline_caderno.py`. Paralelo do Compilador, mas para cadernos (não confundir com resumos NEBLI).

### Triggers reconhecidos

- "faça a P1 da UC1" / "caderno P2 UC01" → `--uc UC1 --prova P1`
- "monta o histórico da UC2" → `--uc UC2 --prova HISTORICO`
- "regenera o caderno P3" (UC ambígua: perguntar com 2 opções)
- "audita o caderno X já gerado" → só roda `auditar_caderno_pdf.py` + `verificar_gabarito_ordem.py --apenas`, **não regerar**.

### Comando único canônico

```bash
python typst-build/pipeline_caderno.py --uc UC<N> --prova <P1|P2|P3|HISTORICO>
```

Etapas internas (cada uma bloqueia):
1. Cronograma: valida prova em `banco/aulas_uc<N>.yml`. HISTORICO sempre vale.
2. `gerar_caderno.py` → `typst-build/_cadernos/caderno-uc<N>-<p>.typ`.
3. `render_caderno.py` → `resumos-gerados/CADERNO-UC<N>-<PROVA>.pdf` (com `--font-path ../fonts`).
4. `auditar_caderno_pdf.py` → relatório em `arquivos-trabalho/`. Bloqueia em mojibake.
5. `verificar_gabarito_ordem.py --apenas <pdf>` → relatório. Bloqueia em contagem/ordem/correção divergentes.

Exit codes: 0 verde · 2 entrada inválida · 3 cronograma vazio · 10–19 gerar · 20–29 render · 30–39 audit · 40–49 verificar gabarito.

### O que FAZ

- Confirma UC e prova em ambiguidade (sempre opções numeradas).
- Roda o comando único.
- Exit 0: reporta path do PDF, tamanho, páginas, total objetivas + discursivas.
- Exit ≠ 0: lê relatório, resume erros em ≤5 linhas, mostra 3-5 problemas concretos. **Não silencia.**

### O que NÃO FAZ

- Não toca em `gerar_caderno.py`, `render_caderno.py`, etc — reporta bug e para.
- Não edita banco, não classifica, não muda `aulas_uc*.yml`.
- Não compila Typst direto — sempre via pipeline.
- Não delega para outra sessão.
- Se Davi pedir resumo, redireciona pro fluxo de resumos (sessão principal).

### Numeração e markers de gabarito

- **Numeração sequencial 1..N** dentro do PDF (canônico 2026-05-24): IDs do banco têm colisões em UC1; caderno injeta `_seq` em cada questão.
- **Markers aceitos no gabarito:** A–Z, a–z, romanos (I-IV), dígitos 1..99 (canônico 2026-05-25 — q-0179 usa I-IV, q-0337 usa a-i).

---
