---
tarefa: card-mirror-treino-continuar
objetivo: >
  Continuar o loop adversarial de TREINO de geração de NEBLIcards até ficarem
  indistinguíveis dos cards AnKing. É treino de estilo — aprender a gerar cards
  no formato AnKing com conteúdo de lacuna. Os cards de treino são SANDBOX
  (não vão pro deck vivo; sem E1 não passam no gate B2).
projeto_dir: C:\AI use\nebli
anki: AnkiConnect em http://localhost:8765 (precisa estar vivo — Docker anki-nebli)
tema_treino: glicogenio
ler_primeiro:
  - flashcards/CARD-MIRROR-PLANO.md        # o design do loop (GAN em texto) + extensões
  - flashcards/CARD-MIRROR-TREINO.md       # o protocolo de treino + estado da rodada atual
  - flashcards/CARD-MIRROR-RUBRICA.md       # REGRAS APRENDIDAS — ler e aplicar a cada card
  - .claude/agents/card-mirror.md           # o agente discriminador (carrega no boot da sessão)
artefatos:
  cards_treino: flashcards/treino/glicogenio-treino.json   # 50 cards (sandbox)
  script_lote_cego: flashcards/scripts/card_mirror_blind.py
estado:
  glicogenio: "CONVERGIU em 3 rodadas (2026-07-12): 0/12 pegos, 46% de acuracia, indistinguivel. NAO refazer."
  proximo_passo: "(a) construir flashcards/scripts/lint_neblicard.py da rubrica; OU (b) treinar tema NOVO (gerar <tema>-treino.json ja aplicando a hierarquia de tells da rubrica; deve convergir em menos rodadas)."
  rodadas_feitas: 3
  correcoes_pendentes_rodada_2:
    - "adicionar o crédito exato 'Image licensed by Physeo and used with permission.' aos cards que reusam imagem Physeo (a ausência foi o tell #1)"
    - "cards de doença de depósito (GSD) usam a imagem-mãe de GSD 8412e62f35b76d85fa69d4b05169138d.webp, não a geral efa5f694...webp — mapear imagem por SUBTÓPICO"
    - "imitar o formato AnKing de GSD: 'X disease is also known as glycogen storage disease type {{c1::...}}' + mnemônico ('One Gierke', 'ABCD Andersen→Branching Cori→Debranching')"
    - "manter o verso como glosa telegráfica (Reversible. / Uses Pi, not water.) ou vazio — NÃO virar prosa de monitor"
criterio_de_parada: "discriminador <= ~55-60% de acurácia E >=1 falso-positivo (confunde AnKing real com NEBLI) E veredito 'chute / ≈ indistinguível'. Resíduos inerentes ao conteúdo (número que o AnKing não carda) são aceitos, não perseguidos."
regra_de_ouro: "Card != E1. O Extra é ANOTAÇÃO telegráfica, não explicação. Sem travessão '—', aspas curvas, reticências, nem referência a banca no corpo. Cloze single curto no token de maior valor."
---

# Continuar o treino card-mirror (glicogênio)

Você é a sessão principal (Opus) orquestrando um loop adversarial estilo GAN para aprender a gerar
flashcards indistinguíveis dos do AnKing. Leia os 4 arquivos em `ler_primeiro` e o `estado` acima.
NÃO recomece do zero: o tema é **glicogênio**, já existem **50 cards de treino** e **1 rodada feita**.

## Faça, em ordem:

1. **Aplique as `correcoes_pendentes_rodada_2`** (acima) em lote no `flashcards/treino/glicogenio-treino.json`:
   edite os 50 cards conforme os 4 pontos, e registre cada tell corrigido como linha nova na
   `flashcards/CARD-MIRROR-RUBRICA.md`. (Se o campo `img` do JSON não existir por card, adicione-o
   mapeando por subtópico: GSD → imagem de GSD; resto → imagem-mãe geral.)

2. **Monte o lote cego:**
   ```
   cd "C:\AI use\nebli" && python flashcards/scripts/card_mirror_blind.py glicogenio 12
   ```
   (imprime 12 meus + 12 AnKing reais, embaralhados; chave em `arquivos-trabalho/treino-key-glicogenio.json`).

3. **Discrimine:** rode o agente `card-mirror` (subagent_type: card-mirror; se não existir na lista de
   agentes, use subagent_type: claude e cole as instruções de `.claude/agents/card-mirror.md`). Passe o
   lote cego inteiro. Ele devolve, por card: ANKING|NEBLI + confiança + o tell.

4. **Meça:** compare o veredito do agente com `arquivos-trabalho/treino-key-glicogenio.json`
   (acurácia, falsos-positivos). Colete os tells que ainda pegaram os meus.

5. **Refine em lote** os cards de treino para apagar cada tell novo; registre-o na rubrica.

6. **Repita 2→5** até bater o `criterio_de_parada`. Grave a curva (rodada, acurácia, tells) na tabela
   de log do `CARD-MIRROR-TREINO.md`.

## Quando convergir
- Declare o padrão "aprendido" e proponha construir `flashcards/scripts/lint_neblicard.py`
  (checagem determinística pré-inserção que barra qualquer tell já aprendido).
- A partir daí, todo NEBLIcard de PRODUÇÃO (com E1 + gate B2) herda a garantia de nascer nativo.
- Para treinar outro tema: gere `flashcards/treino/<tema>-treino.json` (50 cards, seguindo a rubrica)
  e rode `card_mirror_blind.py <tema>`; o resto do loop é idêntico.

## Lembretes de segurança
- Cards de treino são SANDBOX: **não aplicar no deck vivo** (sem E1 = viola o gate B2). Só entram no
  Anki de verdade cards de produção, via o pipeline de curadoria normal.
- Anki precisa estar vivo (AnkiConnect 8765). Se cair, subir o container `anki-nebli` (ver INFRA-REMOTO.md).
