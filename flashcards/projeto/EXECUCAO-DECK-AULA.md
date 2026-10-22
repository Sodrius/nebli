# PIPELINE DE GERAÇÃO DE DECK — v6 (fixo desde 22/10/2026)

**Este é o pipeline único e fixo de todo deck-aula** (Davi, 22/10: “deixa isso fixo como pipeline de geração de deck, daí quando formos mudar algo, mudamos um pipeline já estruturado”). Modelo vivo: 57 Princípios gerais dos vírus (`arquivos-trabalho/deck-aula-uc03-mb57-principios-virus-v2-2026-10-22`, gates 88/88). O **porquê** de cada regra está no [MEMORY](../../MEMORY.md); aqui está **o que fazer, em que ordem, e o que cada etapa entrega**. Versão anterior: `arquivo/2026-10-22-pipeline-v5/EXECUCAO-DECK-AULA-antes-2c0a75762f48.md`.

## Mapa das etapas

| # | Etapa | Entrada | Saída (arquivo da corrida) | Gate duro |
|---|---|---|---|---|
| E0 | Abrir | ESTADO-ATUAL, FEEDBACKS novos, EXEMPLARES/ANTI | corrida + molde, reivindicação, `exemplares-lidos.json` | `exemplares_lidos` |
| E1 | Ler todo o material | lâminas, transcrição, apostilas, monitoria, provas, livro, ≥1 vídeo de canal de Davi | `fontes-decl.json`, `fontes/`, `livros/`, `canais/` | fontes (`sources`, `uc_materials`) |
| E2 | **Compreender a aula** | todo o material lido, relido com as provas e a bibliografia | `compreensao-aula.json` (o que ensina, onde se encaixa, o que lembrar, blocos com papel e **processo**, **reconstruções** pedidas pelas provas) + resumo no chat | `compreensao_aula` |
| E3 | Planejar | compreensão | `inventario.py`, `mapa-de-profundidade.json`, `escopo.json` (história, linha lógica, provas, fontes) | `profundidade`, `linha_e_provas`, `escopo_basico` |
| E4 | Buscar nos acervos | planejamento | `busca/` (seções, palavra-chave, significado por chave de card) | `cobertura_anking` (três caminhos, todos os acervos) |
| E5 | Montar o deck | busca | `spec.py` → `plan.json`; `busca/cobertura.tsv`, `decisoes.json`, `REVISAO-AUTORAIS.md`, `imagens-batem.json` | lint, `autorais_com_motivo`, `imagens_batem`, cores, `artefatos pre` |
| E6 | Instalar e ler o vivo | plano aprovado no pre | deck suspenso, `revisao-despejo.txt` lido, revisão com raciocínio | `revisao_raciocinio`, ordem viva |
| E7 | Fidelidade ao slide | deck vivo + lâminas | `compreensao-aula.json` › `fidelidade` | `fidelidade_ao_slide` |
| E8 | Entregar | gates 100% | pacote da UC, slides no Drive, ESTADO-ATUAL, commit/push, sync, relato | `nebli.gates` 100% |

Princípios que atravessam todas as etapas: o deck **segue o slide** em ordem e conteúdo; **princípio antes do exemplo**, exemplo clínico nunca é carro-chefe; ciclo básico; **acervo primeiro** (AnKing e todas as Referências Externas; autoral sem teto, só para lacuna provada e cards de conexão); deck sem teto de cards; Davi no Anki (uma janela curta de escrita, nada na tela dele).

## Como mudar o pipeline (controle de mudança)
1. Feedback de Davi → literal em FEEDBACKS.
2. Identificar **qual etapa (E0–E8)** ele altera e reescrever essa etapa no lugar, aqui e na regra correspondente do MEMORY (sem acrescentar camada).
3. Se for mecanizável, gate em `nebli/gates.py` (com teste em `nebli/tests/test_gates.py`) e, se mudar arquivos da corrida, o molde em `nebli/molde/`.
4. Mudança de estrutura (etapa nova, arquivo novo, gate novo que corridas antigas não têm) → subir `PIPELINE_VERSAO` no molde, arquivar esta versão em `arquivo/` com hash e registrar no Histórico abaixo.
5. Nunca contornar um gate: se ele reprova um deck bom, muda-se o gate por pedido de Davi, não o deck nem o arquivo de evidência.

## Histórico de versões
- **v6 (22/10, F-20261022-CLAUDE-08):** E2 no nível do processo (campo `processo` por bloco) e `reconstrucoes` das provas; casos que resolvem um problema são conteúdo, não exemplo; lint duro contra cloze genérico. Modelo: 58 refeita (`…mb58…-v3-2026-10-22`).
- **v5 (22/10, F-20261022-CLAUDE-06):** etapa E2 (compreensão da aula) e E7 (fidelidade ao slide) como gates duros; autoral sem teto, só com lacuna provada em todos os acervos.
- v4 (16/10): todo AnKing das seções da aula entra ou é excluído com motivo; deck sem teto de cards.
- v3 (16/10): teto de autoral (removido na v5).

---
Detalhe de cada etapa (os números abaixo são os passos do roteiro; E0 = passo 0, E1 = 1, E2 = 1b, E3 = 2, E4 = 3, E5 = 4–5, E6 = 6.1–6.3 e 6.5, E7 = 6.4, E8 = 7).

Todo comando com `/usr/bin/python3` (tem PyMuPDF e fastembed). Gates com `NEBLI_SEM_TAB=1` (o Tab é do Codex). **Gates duros não se contornam: se um reprova, corrige-se o deck, não o gate.**

## 0. Abrir (5 min)
1. ESTADO-ATUAL › Retomar aqui: qual aula, quem está com ela. Registrar “Com Claude: <aula>”.
2. FEEDBACKS: ler só as entradas novas. `EXEMPLARES-CARDS.md` + `ANTI-EXEMPLARES-CARDS.md`: procurar os casos reais mais parecidos e tentar ficar semelhante aos bons, evitando os ruins.
3. Ritmo (F-20261016-CLAUDE-11): **um deck por vez, inteiro, e em seguida o próximo da fila, até Davi pedir para parar** (nunca parar no meio de um deck).
4. Corrida nova `arquivos-trabalho/deck-aula-<uc>-<curto>-<slug>-v2-<data>`; se existe corrida antiga da aula, copiar `fontes/ livros/ visual/ fontes-decl.json` (fontes já extraídas), nunca o spec. `python3 -m nebli.corrida molde <corrida>` (o molde já traz `PIPELINE_VERSAO = 5` e `compreensao-aula.json`: compreensão da aula, todo AnKing das seções da aula e autoral sem teto mas com lacuna provada, gates duros). Prefixo `<curto>` livre (`"tag:NEBLI::ordem::<curto>-*"` vazio; se só restam tags de compartilhados antigos, removê-las por `nebli.decks.escrita`). **Refação de aula em estudo** (F-20261016-CLAUDE-08; modelo: 43 Fungos v2): ler os comentários de Davi nas notas antigas; no spec, `sh()` das notas antigas que ficam; antes do apply, `nebli.retira <corrida antiga> --recibo <cópia do receipt> chave:refacao-v2 …` para as que saem (exceto as usadas por outra aula, que só perdem as tags desta) e remover das mantidas as tags antigas `ordem::<curto>-*` e `cor::<lesson>::*` — tudo isso num só comando: `python3 -m nebli.refacao <corrida nova>` (logo antes do apply; ele só limpa o prefixo novo — tags `ordem::<curto antigo>-*` e `compartilhado::<curto antigo>` saem à mão numa janela de `nebli.decks.escrita`). No spec, `acervo(nid, …, lesson=LESSON, run_id=RUN_ID)` usa a cópia NEBLI viva quando existe (histórico) e `ak()` quando não; imagens pedidas por Davi no verso de notas mantidas: `EXTRA_VIVO` no spec + `python3 -m nebli.extra_vivo <corrida>` depois do apply. Ao fim, `python3 -m nebli.apaga_retirados refacao-v2` (backup em `arquivos-trabalho/backups-apagadas/`).

## 1. Ler TODO o material (gate duro de fontes)
1. Lâminas como imagem (`visual/folha-NN.png`), todas. **Aula sem lâminas:** montar a lógica da aula (livro da UC + aulas vizinhas + resumos/monitoria + provas) em `percurso-aula.md` antes do inventário (MEMORY §4).
2. Transcrição inteira; apostila guia e demais apostilas de veteranos (só a seção da aula); monitoria; UC3.pdf (seção da aula); provas antigas (`fontes/provas-*.txt` ou `referencias-externas/uc03/consultar.py`); palavras-cruzadas/exercícios; capítulo do livro da UC (confirma, não origina).
3. `fontes-decl.json` com `materiais_uc`: **cada** arquivo de `UCxx/Outros/Apostilas de veteranos`, da pasta pessoal da aula e de `Material para Estudos` lido (texto + seção) ou descartado com motivo. Nada declarado como lido sem ter sido lido nesta sessão.

## 1b. Compreensão da aula (gate duro `compreensao_aula`, F-20261022-CLAUDE-06) — antes de qualquer planejamento
Com todo o material lido, responder em `compreensao-aula.json` a pergunta que a E1 fazia: **o que esta aula busca ensinar? o que o professor está ensinando com cada slide? onde ela se encaixa no todo (aulas antes e depois)? o que deve ser lembrado?** Dividir as lâminas em blocos (todas, inclusive repetição) e dar a cada bloco o papel — motivação, princípio, exemplo, resumo, repetição — e o que o professor ensina ali. Para cada bloco de princípio ou exemplo, escrever o **processo**: o que acontece, como, por quê e o que muda se falhar (não o título da lâmina); quando a aula apresenta casos que resolvem um problema (cada família de vírus, cada classe de fármaco numa etapa), os casos são conteúdo. Ler as provas e listar em `reconstrucoes` o que Davi tem de conseguir reconstruir só com o deck. Exemplo clínico fica marcado como exemplo (`cards_exemplo`): entra depois do princípio que ilustra, e não em maior número sem motivo. Postar no chat um resumo curto e seguir. Tudo o que vem depois (inventário, mapa, busca, cards) nasce daqui; o deck acompanha esses blocos em ordem e conteúdo. Curto e pensado, sem virar formulário.

## 2. Inventário e escopo (antes de buscar)
1. `inventario.py`: cada lâmina → itens → chave do card (ou `EXC: motivo`); provas, cruzadas, apostilas e livro também. Item de prova nunca é excluído.
2. Fronteira com aulas vizinhas (MEMORY §3): aula guarda-chuva fica com o geral; o específico mora na aula específica. **O que já tem card em outra aula é associado (`sh()`), não repetido** — e isso não trava o deck.
3. `percurso-aula.md` com blocos e **Casos de fronteira**.
4. Imagens que ensinam: recortar das lâminas para `img/` (sem título/legenda que entregue), ver o recorte.

5. **Mapa de profundidade (gate duro, F-20261022-CLAUDE-04), antes de buscar e escrever.** `mapa-de-profundidade.json`:
   `{"objetivos_da_aula": "...", "cronograma": {"aulas_vizinhas": [...], "conferido": "como verifiquei que nada é de outra aula"},
   "passos": [{"passo": "...", "itens": [{"id": "p1-1", "tipo": "decorar|explicar|distinguir|e-se|organizar", "o_que": "...", "fonte": "lâmina 12 / transcrição / Machado p. 40", "termos": ["termo que o card tem de conter"], "cards": ["chave"]}]}],
   "fora": [{"o_que": "...", "motivo": "ilustrativo / outra aula: X"}], "extras_fora_da_aula": [{"o_que": "...", "cards": [...], "por_que_essencial": "...", "nao_e_de_outra_aula": "aula conferida no cronograma"}]}`.
   Pensar como professor e aluno: o que Davi tem de **lembrar para a vida** desta aula (nomes, locais, números ditos), **explicar** (cadeia causal), **distinguir** (pares confundíveis), **prever** (e-se) e **organizar** (conjuntos). Ilustração não vira item. Cada passo tem explicar e e-se/distinguir. Os cards nascem do mapa: um card pode cumprir vários itens (vários clozes, Extra com o porquê, imagem, ligação ao conceito anterior), sem virar Frankenstein.

## 3. Buscar com afinco — três caminhos, todos os acervos (gates duros)
1. Seções de recurso: `python3 -m nebli.semantica secoes <corrida> "<tag>" …` (FirstAid, Pathoma, B&B, Bootcamp, Sketchy, OME, NinjaNerd) e **ler cada `busca/secoes/*.txt`**.
2. Palavra-chave: `python3 -m nebli.busca_acervos <corrida>/busca/anking.txt "rótulo=termos" …` (AnKing **e** Referências Externas).
3. Significado: `python3 -m nebli.semantica buscar <corrida> "chave=frase em inglês" …` — **uma consulta por conceito, com a chave exata do card**; roda em AnKing, nos 9 acervos externos e nos **decks NEBLI vivos** (achou em NEBLI-vivo → `sh(nid)`).
4. Declarar no spec `SECOES_DA_AULA` (as seções cujo assunto é o da aula): **toda nota delas entra** (`ak`, ou `sh` da cópia NEBLI) ou vai para `EXCLUIDOS` com motivo de estar fora do conteúdo — gate duro, sem limite de cards (F-20261016-CLAUDE-06).
5. Para cada candidato: texto, clozes, HY, imagem; cópia NEBLI viva (`"tag:NEBLI::source::nid-<nid>"`) → `sh()`.

## 4. Escrever o spec (`nebli.spec_lib`, já importado pelo molde)
1. Ordem = lâminas. `ak(chave, nid, código, bloco, alvo, slide, motivo, origin=…)` para acervo — **todos os irmãos entram**; `au(chave, texto, código, …, extra=…)` para autoral; `sh(nid, cor, …)` para compartilhado. `finalizar(CARDS, HERE, BUSCA)` no fim da lista.
2. **Código de cor** (MEMORY §8): V-hy (automático: **todo HY 1–2 do AnKing é verde**), V-pilar, V-prova, A-aula, A-step, R-detalhe, R-org. Organizador verde só se for pilar; os demais azul/rosa.
3. **Autoral só para lacuna provada, sem teto** (F-20261022-CLAUDE-06): só depois de garantir, nos três caminhos, que AnKing e todas as Referências Externas não têm o card; serve à lacuna real e aos cards de conexão e no padrão dos exemplares/anti-exemplares: frase AnKing de **≤ 16 palavras (máximo 20)**, um nome decorado no cloze, contexto concreto, 1–2 trechos em negrito, sem “;”, sem “x ou y” no cloze; organizador em pé, uma linha curta por item (**máximo 26 palavras**), marcado `organizador=True`, com índices diferentes para itens independentes; contraste complementar marcado e no mesmo índice. Índice que esconde 3+ itens recebe a 1ª letra como dica.
4. Verso: cada card com uma linha de porquê (`VERSO`/`extra`); verso herdado ruim de acervo é trocado com `extra=`.
5. `IMAGENS_VISTAS` (toda imagem fora do AnKing, depois de ver), `DUPLICACAO` (ganho quando a resposta coincide), `ESCOPO` (centrais com o princípio antes dos detalhes), `EXCLUIDOS`, `FORA_DO_RECORTE`.

## 5. Provar cada autoral (gates duros) e montar
1. `python3 build.py` (sem cobertura ainda) → `busca/cobertura.tsv`: uma linha por card do plano (`chave conceito fonte_aula veredito lidos decora decisao`); autoral = lacuna/parcial, 3+ nids lidos da busca da própria chave, fonte da aula, `decora` = resposta do cloze, decisão com o porquê.
2. `REVISAO-AUTORAIS.md`: uma linha por autoral `- <chave> — par: §N … — decora: … — ok/corrigido`.
3. `python3 build.py` de novo; `NEBLI_SEM_TAB=1 python3 -m nebli.artefatos pre <corrida>` → só podem faltar os passos pós-instalação.

## 6. Instalar e ler o deck vivo
1. Preparar fora do Anki o lote inteiro (mídia, campos, IDs, destinos, backup e ações). Conferir que o Anki aceita escrita (editor aberto bloqueia; nunca fechar a tela de Davi — esperar) e então aplicar tudo em **uma única janela curta** de `nebli.decks.escrita()`, com ações vetorizadas/`multi`, nenhuma escrita por card e um readback final. `python3 <corrida>/apply.py`; aula antiga: `python3 -m nebli.artefatos suspender <corrida>`; `python3 -m nebli.ordem verificar NEBLI::<lesson> --plan <corrida>/plan.json`.
2. `python3 -m nebli.artefatos despejo <corrida>` e **ler o despejo inteiro**: frente sem campo perdido, cloze certo, imagem certa, verso útil, cor. Corrigir no spec → `build.py --delta` → `python3 -m nebli.delta <corrida>`.
3. **Revisão com raciocínio (gate duro `revisao_raciocinio`)**, no `mapa-de-profundidade.json` › `revisao`: `passos` = para cada passo, `explicacao_com_os_cards` (≥ 300 caracteres, explicando o passo só com o que os cards vivos dizem) e `cards_usados`; `perguntas_teste` (≥ 2 por passo: perguntas da aula, das provas e de um aluno curioso, cada uma com os cards que respondem); `releitura_da_transcricao` (reli a transcrição/apostila do começo ao fim: o que conferi e o que acrescentei). Onde a explicação trava, falta card: criar e reinstalar.
4. **Fidelidade ao slide (gate duro `fidelidade_ao_slide`)**: reler as lâminas bloco a bloco contra os cards vivos e preencher `compreensao-aula.json` › `fidelidade` (cada bloco: bate em ordem e conteúdo? exemplo no lugar de exemplo? algo de fora entrou?) e a `conclusao`; o que não bate é corrigido antes de entregar.
5. `REVISAO` no spec; `REVISAO-DE-QUALIDADE.md`; `NEBLI_SEM_TAB=1 python3 -m nebli.artefatos pos <corrida> --li-despejo [--corrigidos …]`; no `revisao-final.json`, marcar o Tab como pendente (nunca afirmar Tab lido).

## 7. Entregar e fechar
1. Pacote: `python3 -m nebli.package_uc --uc UCxx --output arquivos-trabalho/pacote-ucxx-<data>[b]/NEBLI - UCxx.apkg` + `python3 -m nebli.entrega "<UC>/<Comp>/<NN - Aula>" --nome "<Aula>" --uc-apkg <apkg>`; sync se Davi não estiver revisando.
2. `NEBLI_SEM_TAB=1 python3 -m nebli.gates <corrida>` = 100%.
3. ESTADO-ATUAL, FEEDBACKS→MEMORY→gate de todo feedback novo, memória pessoal, commit e push.
4. **Relato no chat** (formato que Davi aprovou): o que mudou com o feedback; tabela do deck (cards, origens, cores); o que entrou, o que ficou de fora, o que foi corrigido; gates; perguntas. Sem prompt do Codex (F-20261021-CLAUDE-01: ele gera os Tabs por conta própria).

## Referência técnica
- Delta: `build.py --delta` + `nebli.delta` (tolera editor aberto: pula e avisa; rodar de novo depois). `--sobrescrever-vivo <chave>` só quando a diferença viva não é edição de Davi (o `<tbody>` do editor já é ignorado).
- Índice semântico: `python3 -m nebli.semantica indexar` (~12 min) quando o AnKing atualizar.
- Retirar: `nebli.retira`; recolorir: `nebli.recolor`; comentários: protocolo do MEMORY §10.
