# MEMORY.md — estado vivo do NEBLI

Atualizado em 2026-08-12. Histórico e regras antigas permanecem em `docs/legacy/` e no Git.

## Estado atual

- Pipeline canônico: `e1-deck-v9`.
- A entrega só libera com `nebli-e1-deck-release-v1`: E1 fonte/PDF congeladas,
  revisão semântica independente, core nuclear 100% coberto e todo card ligado a
  uma âncora. Para Davi aparecem somente E1/PDF e manifesto do Companion.
- Produto padrão: **E1 + Deck-Aula completo no AnkiDroid**.
- Backend normal: AnkiDroid via Nebli Companion.
- Schema final: `nebli-ankidroid-deck-v3`.
- E2, E3 e RemNote desligados.
- Retenção longitudinal: 25 novos/dia; revisões 9999/dia.
- Desktop/APKG/Drive/Colab não pertencem ao fluxo normal.
- **Atualizar o Companion do tablet:** o APK sai do CI. Workflow
  `Android Companion` no GitHub → run verde do branch → artefato
  `nebli-ankidroid-companion-debug` → instalar o `app-debug.apk` no tablet.
  Build mais recente aprovado (2026-08-12, commit `ad6c1f9`, run 106):
  https://github.com/Sodrius/nebli/actions/runs/31596148326/artifacts/9141201203
  — inclui o alias de vocabulário de IO, o preflight de contrato e o recibo com
  `companion_io_modes`. O
  artefato só é publicado quando os testes unitários E o round trip real com o
  AnkiDroid no emulador passam — APK sem teste real continua bloqueado.
  Depois de instalar e confirmar por um recibo real, trocar
  `config/pipeline.json → ankidroid.installed_companion.io_mode_token` para
  `hide_two_guess_two` e anotar a data.
- O Nebli Companion instalado no tablet foi compilado do commit `942e665` (#18)
  e **não conhece o token `hide_two_guess_two`**. Enquanto não for reinstalado, o
  manifesto sai com o alias `hide_all_guess_all`, controlado por
  `config/pipeline.json → ankidroid.installed_companion`. O Companion deste repo
  aceita os dois nomes.

## O que o Companion final suporta

- buscar AnKing diretamente na coleção local;
- copiar AnKing com note type/campos/HTML/clozes/tags/mídia preservados;
- usar deck externo local com filtro/ranking e a mesma política de cópia segura;
- criar cards autorais diretamente no AnkiDroid;
- importar mídia nova para Extra de autorais, exigindo função cognitiva e crédito;
- criar Image Occlusion diretamente, com o contrato `hide_two_guess_two` (no
  máximo duas máscaras, duas respostas coerentes), aceito também pelo nome
  antigo `hide_all_guess_all`;
- separar opcionais em `<Deck>::Optional`;
- criar o deck com nome canônico `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`;
- resetar scheduling das cópias sem alterar a fonte;
- suspender siblings não selecionados;
- instalar de forma idempotente;
- fazer rollback das notas novas em falha parcial;
- selecionar/abrir o deck correto no AnkiDroid ao concluir.

## Referências externas do Davi

- **Diário de Estudo 2026** (Google Sheets, `1T1RZ_vpqtchmdM8U2BXYmlHk7e-Ov-iCGM51PFIEqMU`,
  título "2026"): registro diário de horas de estudo em blocos de 25 minutos, com
  meta de 45–50 h por semana e o assunto de cada bloco (UC, disciplina, NEBLI,
  trabalho, francês). Serve para dimensionar carga e ritmo quando o pipeline
  precisar decidir volume de cards ou cadência de revisão.
  https://docs.google.com/spreadsheets/d/1T1RZ_vpqtchmdM8U2BXYmlHk7e-Ov-iCGM51PFIEqMU/edit

## Decisões vigentes de card

- Ordem: AnKing adequado → deck externo adequado → autoral.
- Um card = uma recuperação independente, específica e relevante.
- Todo card deve ter âncora literal na E1.
- Não criar cards por cota; respeitar teto congelado da aula.
- Autorais: frente em inglês médico natural, Extra curto em português, exatamente um `c1`.
- Cloze: 1 palavra por padrão; 2 quando necessário; 3 raramente e com justificativa; 4+ bloqueia.
- IO: só quando reconhecimento/localização agrega; máscara cobre o rótulo-resposta, não a estrutura; usar uma ou duas máscaras, com `pair_rationale` quando forem duas.
- Card autoral procura primeiro mídia local do AnKing; slide/externa exige rejeição documentada. Toda imagem exige propósito cognitivo, crédito e QA didático.
- AnKing/deck externo nunca é reescrito e a fonte nunca é modificada.

## Validação

- O relatório card-a-card é **derivado** do `deck-data.json`
  (`derivar_validacao_cards.py`), nunca escrito à mão. O finalizador recusa
  relatório que divirja do conteúdo real dos cards.
- O lint de qualidade funcional (`lint_qualidade_funcional.py`) roda dentro do
  gerador no caminho estrito: cloze genérico, resposta vazada, meia-parcela de
  par canônico, enumeração e duplicata funcional bloqueiam o lote.
- A procedência da busca AnKing é declarada em `anking_search_mode`
  (`session_local` / `device_deferred` / `unavailable`) e aparece no manifesto.
- Gate final é **card a card, sem amostragem**.
- `expected_card_count == validated_card_count == passed_card_count` e `failed_card_count == 0`.
- CI mantém regressão realista de 40 cards, mas uma aula real valida o número real do deck.
- Um único card inválido bloqueia o lote.
- O recibo do Companion precisa confirmar `installed_card_count == expected_card_count`.

## Última corrida real

`imuno-01-reconhecimento-inato` (UC03 · P1 · Imunologia), 2026-08-12:
E1 de 22 páginas, 53 cards (51 autorais + 2 IO), 37 conceitos, 28 nucleares
todos cobertos, gate 53/53, manifesto v3 gerado e conferido contra o gate Java
real do Companion. Diagnóstico das falhas de
pipeline encontradas na corrida em `arquivos-trabalho/DIAGNOSTICO-PIPELINE-2026-08-12.md`.

## Próxima corrida real

A próxima sessão deve receber os PDFs/arquivos da aula, ler `NEXT-SESSION.md` e rodar `/resumo` até o fim. Não pedir curadoria manual de cards. Entregar E1/PDF e **um único manifesto `.ankidroid.json`**; o usuário apenas abre esse arquivo no Companion para instalar o deck completo.

Não há pendência de infraestrutura que justifique voltar ao índice de 6 GB, Drive/Colab ou APKG como caminho normal. Se surgir falha nova numa aula real, corrigir o pipeline canônico e registrar em `ERROS.md` antes de considerar a aula concluída.
