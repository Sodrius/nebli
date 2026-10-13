# Execução de deck-aula — fontes, revisão e entrega

Roteiro técnico consolidado em 29/09/2026. Preferências e critérios somente no [MEMORY](../../MEMORY.md); decisões/casos em [FEEDBACKS](FEEDBACKS.md). Este roteiro orienta a sessão assistida: não é promessa de um gerador ou serviço já implementado. Não executar scripts antigos de aula, nem `nebli/anki_apply.py`, como gerador universal.

> **Cobertura UC08 (F-20261004-CODEX-05):** antes de procurar cards, criar
> `inventario-aula.json` com todas as páginas classificadas e cada elemento
> ensinável atômico. Depois da instalação, cada id precisa apontar em
> `cobertura.json` para card vivo e receber veredicto em
> `revisao-inventario.json`. A porta `nebli.gates` reprova corrida sem esses
> três artefatos, item sem card, página de conteúdo vazia, alvo visual sem
> imagem/justificativa ou Extra-modelo. O esquema e a campanha de refação estão
> em [REFACAO-UC03-PADRAO-UC08.md](REFACAO-UC03-PADRAO-UC08.md).

## 1. Recuperar contexto e estado

Seguir [README](README.md), inclusive em mensagem comum. Identificar pedido, UC/prova, componente, aula e escopo E1 + cards ou exceção. Para UC08, ler [fila atual](RECONSTRUCAO-UC08.md); registrar início, executor, run_id e pasta quando houver produção autorizada. Revisão própria obrigatória; papéis/ritmo seguem o pedido atual, sem gate fixo de outra IA.

Ler feedbacks novos e os casos aprovados/rejeitados pertinentes do MEMORY; abrir exemplos reais para calibrar a forma antes de redigir. Documentos antigos não revogam as respostas de 29/09. Não iniciar aula quando o pedido for só organização/planejamento. Auditoria sem correção solicitada não escreve no Anki/Drive.

Usar uma pasta privada `arquivos-trabalho/deck-aula-<slug>-<data>/`, com versões/identificadores sem sobrescrever evidência anterior. Confirmar perfil vivo, acesso AnkiConnect e ferramentas Drive disponíveis no computador atual. Não assumir caminhos Windows ou nome de ferramenta de outra sessão.

```text
python3 -m nebli.preflight --catalog --output arquivos-trabalho/deck-aula-<slug>-<data>/catalogo.json
```

Preflight é leitura: descobre raízes, modelos e estado; não aprova conteúdo. Resolver erro/partial antes de escrita insegura. Reconciliar edições, flags, comentários (mesmo sem cor), suspensões e cards removidos. Não recriar apagados nem restaurar estado de snapshot antigo.

## 2. Fontes e cobertura integral

Usar [ACERVOS-REFERENCIA](ACERVOS-REFERENCIA.md) para livros, canais, modelos e descoberta. Buscar material docente atual no Drive, incluindo roteiro/extras/transcrição. Considerar seis famílias: material docente, provas pertinentes, E1 existente quando aplicável, bibliografia, vídeos e Step do mesmo conteúdo. Provas no começo, junto com slides: UC03 pelo índice `referencias-externas/uc03/consultar.py --slug <slug>`; outras UCs pela pasta de provas e nomes dos temas antes de declarar ausência.

Registrar fonte/localizador, versão/hash quando disponível, trecho/páginas e estado `consultada / não localizada / inacessível / substituída / não aplicável`. Não chamar figura citada no slide de capítulo lido nem metadados de vídeo assistido. Buscar substituto adequado quando necessário. **Fonte importante ainda ausente impede instalar a aula** (Q020); avançar na preparação sem mascarar a falta. Fonte opcional ausente não vira bloqueio artificial.

Percorrer toda a aula, inclusive figuras e prática. Mapear cada bloco a: alvos que exigem recuperação, apoio suficiente ou exclusão justificada como ilustração/futuro/fora do recorte. A lista de objetivos criada pelo executor não basta para certificar cobertura. Conferir depois se cada alvo recuperável está de fato testado por card/cloze/identificação, sem trocar uma recuperação necessária por menção no verso.

Aplicar as fronteiras do MEMORY: mecanismos necessários, clínica compreensível diretamente ligada e HY do mesmo conteúdo; prova antiga sozinha não acrescenta tema ausente dos slides atuais. Não usar rotina ou prazo como orçamento de cards. Quando Davi respondeu “depende”, justificar a escolha naquele alvo; não criar regra universal.

Se houver E1, ler [didatica/E1.md](../../didatica/E1.md) e suas referências, usando as mesmas fontes/objetivos. Build isolado, somente E1; revisão textual/visual do PDF e figuras. Na UC08, E1 é não aplicável somente quando o pedido atual não a inclui; pedido explícito de E1 + deck prevalece.

## 3. Buscar, selecionar e redigir

Primeiro procurar identidade NEBLI viva. Depois AnKing → alternativos pertinentes → AnatoKing/MCAT quando pertinentes → autoria por último. Buscar conteúdo/sinônimos, sistemas, tags de recursos, vizinhança e campos de modelos visuais; duas rotas AnKing e externos adequados antes da autoria. Ler candidatos/recusas; tag ou consulta vazia não prova lacuna. Registrar a busca por alvo, sem repetir aquisição de acervo já disponível. **A busca em Referências Externas é obrigatória antes de qualquer autoral** e fica gravada na corrida (`busca/ext.txt`, apontada por `"busca_externos"` no plano; o lint reprova sem ela).

Selecionar irmãos pertinentes individualmente, sem os cortes excessivos e sem importar outro assunto. Comparar alvo + resposta + habilidade na seleção viva, incluindo compartilhados. Prática adicional exige ganho; básico não é redundante por parecer fácil. Autoral só para lacuna relevante real. Comparar a forma com AnKing de verdade, conforme MEMORY: contexto, resposta, ocultações, verso, imagem e carga de recuperação; CSS/contagem de palavras não são qualidade.

**Autoral indistinguível do AnKing (F-20260930-CLAUDE-16):** uma frase que ensina o processo e oculta um nome; sem “;” juntando afirmações nem “:” como rótulo; ≤ ~20 palavras; preferencialmente um cloze; frente e Extra em inglês. Autoral para lacuna útil sem candidato adequado, priorizando alvo central ou de prova e admitindo detalhe que realmente valha aprender, com `"autoria": "central" | "prova" | "lateral"` e `"busca"` no `spec`/plano; Extra vazio ou em bullets `- ` curtos, sem parágrafo nem metacomentário. **Cada autoral é escrito a partir de 2–3 espelhos AnKing** (candidatos vizinhos lidos na busca ou `python3 -m nebli.espelhos <termos>`), como irmão do espelho de função mais parecida, com os nids em `"espelhos"` no plano; método em `.claude/agents/card-author.md`. Rodar `python3 -m nebli.lint_cards <corrida>/plan.json` antes do dry-run (zero reprovação dura) e uma amostra cega com o agente `card-mirror` (autorais + AnKing embaralhados); examinar as pistas e corrigir defeitos editoriais/pedagógicos sustentados, sem mudar bom card apenas para enganar o detector. Registrar os dois resultados na REVISAO-DE-QUALIDADE.

**Mídia dos autorais:** quando houver ganho visual, procurar figuras nos AnKing candidatos e próximos do mesmo alvo, mesmo que o texto do card não seja aproveitável. Registrar imagem escolhida ou motivo de não uso no plano da corrida, junto com nota de origem/arquivo, relação com o alvo e inspeção de precisão, legibilidade e resposta vazada. Renderizar com o texto/cloze final; texto novo não valida automaticamente imagem herdada. Preservar mídia original e usar arquivo acessível ao modelo autoral. Não exibir rodapé de fonte/crédito da imagem em novos cards, inclusive HTML herdado; manter proveniência no registro técnico. Legenda didática continua quando necessária. Não alterar cards antigos em lote por essa preferência.

Novas cópias/autorais em inglês (Q056–060). Idioma novo não autoriza converter decks anteriores. Manter proveniência e separar fonte original de adaptação curada; originais, modelos compartilhados de referência e AnkiHub preservados. Clone independente não herda vínculo ativo: `ankihub_id` vazio. Conservar referências científicas úteis no registro de proveniência; aplicar a dispensa de créditos visíveis das imagens do MEMORY e retirar recurso/clínica lateral na curadoria da cópia. Links de vídeo ficam no guia/chat.

## 4. Plano, bandeiras e revisão

**Arquitetura da seleção (F-20261002-CODEX-02):** executar em etapas com resultados verificáveis:

1. Reconstruir o percurso docente: bloco/slide → objetivo demonstrável → alvo recuperável; registrar inferências e excluir expansão externa sem encaixe excepcional.
2. Mapear a preparação da prova: confrontar os alvos com exercícios/provas e fontes; identificar lacunas de mecanismo, distinção e reconhecimento, sem preencher volume com clínica ou rosas. Ausência em provas disponíveis não elimina objetivo central da aula.
3. Selecionar o núcleo longitudinal: para cada candidato verde, justificar uso futuro concreto, centralidade, custo de esquecer e ganho sobre os verdes já selecionados. Rebaixar detalhes de baixo ganho e remover redundância sem perder recuperação central; comparar o núcleo agregado entre aulas antes de aceitar a carga.
4. Buscar/escrever os cards e atribuir verde/azul/rosa segundo o MEMORY. Manter rastreabilidade card → alvo → fonte → posição da aula; priorizar qualidade do candidato, não sua origem nominal.
5. Revisar de forma independente três aspectos: fidelidade/cobertura da aula e prova; seletividade dos verdes entre aulas; precisão, recuperação e estilo AnKing. Na autoria, usar teste cego com conjunto novo após refinamento. Registrar discordâncias e corrigir antes de aceitar o lote.
6. Conferir ordem apresentada e cobertura real; relatar separadamente total útil da aula, núcleo verde único entre aulas, lacunas e limites da evidência. Documentar o procedimento não comprova execução nem implementa a interface.

Comentários reais deixados por Davi no Anki são exemplos prioritários para calibrar autoria: ler pelo fluxo existente antes das próximas rodadas, preservar texto e marca pessoal e registrar a resolução. O pedido futuro de base de provas de residência/Step, cursinhos e livros não autoriza criar agora uma base indiscriminada; usar o acervo disponível com localizadores verificáveis.

**Calibração entre aulas (F-20261002-CODEX-01):** antes de alegar critério calibrado, montar uma amostra de aulas de perfis contrastantes e confrontar seus alvos com provas, Step 1 e cursinhos realmente acessados. Registrar por alvo localizadores das evidências, relevância para a prova, utilidade longitudinal, cor e incerteza. Reservar outras aulas para validação; comparar decisões e motivos, não forçar contagens iguais. Relatar carga verde agregada e novas identidades únicas, separando compartilhados; 40 novos/dia mais todas as revisões é a rotina declarada (F-20261002-CODEX-06), não teto de cards da aula; configurar a meta na execução própria. Evidência e resultados vão à corrida, preferências permanecem no MEMORY.

**Ordem visível da aula (implementada em 02/10):** a ordem do plano é a sequência em que o professor deu o conteúdo (slide a slide; dentro do slide, do conceito ao detalhe), não agrupamento por origem, cor ou tema escolhido pela IA. Cada nota da aula, **inclusive compartilhada e cópia AnKing**, recebe `NEBLI::ordem::<curto>-<NN>` (`nebli.ordem.tag`), com `<curto>` exclusivo da aula, e `NEBLI::objetivo::<bloco>`; `evid` de cada entrada começa pelo slide (“Slide 12; exercício 3”). Instalar as notas nessa ordem, para que criação e fila de novos também a sigam. Gate antes de entregar: `python3 -m nebli.ordem verificar NEBLI::<lesson_id> --plan <corrida>/plan.json` sem FALHA; cada “recuo de slide” avisado é conferido e justificado na REVISAO-DE-QUALIDADE (o professor voltou ao tema) ou corrigido. No Browser, a coluna “Ordem da aula” do add-on `nebli_decks` mostra posição e bloco e ordena por eles: buscar `"tag:NEBLI::<lesson_id>"` e clicar no cabeçalho. Não alterar vencimentos/histórico para simular ordem. AnkiDroid não tem a coluna; lá vale a ordem de criação/fila.

**Revisão cega autorizada:** usar autor e avaliadores em contextos separados, avaliadores sem origem/gabarito, com AnKing real e autorais comparáveis por assunto/tipo. Separar crítica científica/pedagógica de identificação de estilo; corrigir e retestar em amostra nova, preservando resultados anteriores. Chamar de avaliação cega da origem; só chamar duplo-cego quando ambos os lados relevantes estiverem efetivamente cegados (o autor conhece a própria autoria). Seguir o método existente de `card-mirror`, sem declarar convergência por uma rodada pequena ou por juiz que aceita tudo.

`plan.json` registra lesson_id/run_id, fontes/versões, sequência docente, alvo, evidência na aula, uso futuro concreto, necessidade de recuperação ativa, comparação com cobertura existente, decisão/motivo/incerteza, recomendação/cor; origem real, IDs de nota/card, cloze/template, identidade existente/nova, campos/mídia, associação a outras aulas, busca/autoria e ganho de pares mantidos. A cor nasce com a seleção, não de uma classificação genérica posterior da matéria. Respeitar marcas pessoais; registrar recomendação separada quando necessário.

**Gate de seleção e bandeiras para toda próxima entrega (F-20261002-CODEX-05):** a REVISAO-DE-QUALIDADE deve mostrar o mapa completo de blocos cobertos/excluídos e uma amostra rastreável de decisões de cada cor presente, mais os casos limítrofes. Para verde: uso futuro concreto, centralidade e ganho incremental; azul: necessidade para a prova; rosa: ganho para desempenho com menor prioridade. Apontar exclusões de conteúdo externo e duplicações evitadas. Comparar o núcleo com aulas pertinentes já disponíveis, sem copiar percentuais. Informar carga verde única agregada, sem impor 50/aula nem alterar preset. Critério sem evidência ou lacuna central não permite declarar a seleção revisada. Ausência de uma cor não exige inventar cards para preenchê-la.

Cobertura é conferida contra todos os blocos da aula. Verificar alvos essenciais ausentes, verdes equivalentes e exclusões injustificadas; revisar recorte/precisão, didática/recuperação, imagens/renderização e identidade/entrega separadamente.

**Q040 permite revisão por amostra quando o restante segue o mesmo padrão.** Selecionar exemplos representativos das origens, modelos e tipos presentes; incluir autorais/adaptações e casos de risco conhecidos. Registrar exatamente o que foi lido/renderizado/inspecionado e o que ficou fora. Erro encontrado amplia a revisão da parte afetada antes da entrega. Amostragem editorial não dispensa mapa integral de cobertura, seleção justificada nem conferência estrutural do conjunto. Não afirmar que todas as imagens ou todos os cards passaram por leitura individual se isso não ocorreu; não exigir auditoria do usuário para compensar.

Na amostra, ler frente/verso renderizados: resposta vazada, cloze ambíguo, pergunta que depende do nome do deck, informação lateral, imagem errada/ilegível, máscara/legenda e fidelidade ao modelo. Clínica deve ensinar a relação com ganho real. Erro científico conhecido, resposta vazada ou imagem errada impede liberar o card afetado; contagem/teste não o aprova.

## 5. Dry-run e escrita segura

Antes de aplicar, validar **todo o conjunto estrutural**: perfil, IDs/origens/GUIDs, campos/templates/clozes selecionados, mídia existente, condicionais, irmãos que seriam gerados e colisões de identidade. Dry-run precisa ser somente leitura, sem `createDeck`/`addNotes` escondido. Fazer snapshot/backup e registrar precondições de versão/hash; mudanças pessoais desde a leitura exigem reconciliação, não sobrescrita.

Toda escrita no Anki passa por **`with nebli.decks.escrita(Anki(), "<aula>"):`**. O contexto adquire `arquivos-trabalho/ANKI-ESCRITA.lock`, espera os nomes canônicos sem os totais do add-on, libera seu lock e solicita sync após sucesso. Não atropelar lock existente nem criar árvore paralela usando nome com sufixo `(N)`. Usar `nebli.rotulos.canonical`. Se o add-on necessário não estiver funcionando no perfil atual, resolver isso antes de escrever; não contornar o mecanismo com lock manual.

**Campo de comentário:** todo tipo de nota usado recebe `NEBLI_Comentario` vazio (F-20260930-CLAUDE-01). Clone novo (`createModel`) acrescenta o campo ao fim de `inOrderFields`; nunca preencher com curadoria. Antes de instalar em tipo já existente, rodar `python3 flashcards/scripts/garantir_campo_comentario.py`. Se ele listar falta, acrescentar o campo é mudança de esquema (confirmação na tela + sync completo): pedir a Davi que sincronize os outros aparelhos antes e aplicar com `--aplicar` só com a autorização dele.

Uma identidade/histórico por card. Tag pertence à nota e pode incluir irmãos indevidos; associações precisam do conjunto exato de IDs/clozes. Não mover/duplicar compartilhados para simular duas aulas. Antes de alterar campo de nota ou excluir nota, conferir todos os irmãos, associações e histórico afetados. Preservar edições, bandeiras e suspensões pessoais. Novas preferências não disparam correção retroativa sem pedido.

Criar ancestrais e manter a hierarquia `NEBLI::UCxx::Px::Componente::Aula`, sem inventar prova ou reorganizar outra aula. Preset comum; quando necessário, alinhamento por `flashcards/scripts/nebli_novos.py --alinhar`, sem restaurar valores antigos de novos/revisões. Instalar depois de fontes importantes e revisão resolvidas; sincronizar na mesma execução. Após timeout, ler identidade/estado antes de repetir a operação.

## 6. Readback e evidência da entrega

**Cores no plano:** verde 3, azul 4 e **rosa 5 para conteúdo útil ao desempenho na prova, de menor prioridade e pouco ganho longitudinal** (tag `NEBLI::lateral`), em vez de excluir detalhe que ainda vale ter; o `build.py` herdado das corridas só conhece 3/4 e precisa aceitar 5. Cada card da aula, inclusive compartilhado, recebe `NEBLI::cor::<lesson_id>::<cor>`; bandeira visível = maior cor entre as aulas, sem baixar bandeira existente nem mexer em marca pessoal (MEMORY, Bandeiras).

Conferir plano versus coleção: notas/cards/clozes e origens, campos/modelos/mídia (incluindo `NEBLI_Comentario` presente e vazio em toda nota nova), cores previstas com marcas pessoais preservadas, IDs selecionados, história/agendamento e integridade dos originais. Verificação estrutural completa e revisão editorial por amostra são evidências diferentes.

Compartilhados: provar associação por IDs vivos e consulta com conjunto conferido. Se só existe busca no navegador, dizer; não anunciar botão de estudo na segunda aula pronto. Não duplicar para contornar limitação da interface. Sync aceito pelo AnkiWeb não comprova chegada em Mac/Android/Windows.

**Explicações do Tab (F-20260930-CLAUDE-11/16):** depois da instalação, gerar uma explicação por card da aula com `python3 -m nebli.explicacoes gerar '"tag:NEBLI::<lesson_id>"'`. A tag da aula já inclui os compartilhados. **Nunca** `deck:"NEBLI::..."` exato: os nomes vivos levam o total e a busca volta vazia; o gerador agora para com aviso. Cada card tem a sua, inclusive irmãos. A base fica fora da coleção e o estilo em `config/explicacao-tab.md`. Preservar o formato de Tab aprovado e conferir que exames/termos novos recebem base suficiente. Ler uma amostra (irmãos, autorais, imagem e todos os “revisar”) e registrar na REVISAO-DE-QUALIDADE; card marcado “revisar” é achado da própria revisão. **Gate de entrega:** `python3 -m nebli.explicacoes resumo '"tag:NEBLI::<lesson_id>"'` com `faltando: 0`, `desatualizada: 0` e `revisar: 0` (conferir este estado mesmo se o comando não o tratar como erro). Se a geração cair (limite da assinatura, Anki fechado), retomar o mesmo comando, que pula o que já está atual.

Manter na mesma corrida `plan.json`, snapshot anterior, `journal.jsonl`, `receipt.json`, `verification.json` e `REVISAO-DE-QUALIDADE.md`. A revisão sintetiza, com links às evidências existentes:

- Versão/escopo, fontes realmente consultadas e varredura integral da aula; lacunas e exclusões relevantes.
- Escolhas concretas que demonstram o padrão de Davi: recuperação preservada, alternativa consultada, autoria necessária, relação clínica pertinente, imagem e bibliografia, núcleo sem quota.
- Inglês dos novos cards; forma comparada aos exemplos reais. Se houver revisão de tradução antiga explicitamente pedida, comparar base/resultado e declarar alcance real.
- Revisão realizada, amostra e limites; achados corrigidos ou pendentes; IDs dos feedbacks aplicados e versão dos critérios.
- Estados distintos: conteúdo revisado, instalação, acesso aos compartilhados, pacote, publicação e sync. Outra IA só assina sua revisão efetiva.

Não gerar um novo arquivo de política por aula. Relatório ao usuário é curto: onde estudar, cobertura/limites, núcleo, poucos exemplos e contagens (notas/cards únicos, novos/reutilizados/compartilhados, origens, autorais, cores/suspensos; aula e união da UC). Gerar a tabela final pelo Anki vivo com `python3 arquivos-trabalho/relatorio_decks.py "NEBLI::UCxx"` (somente leitura; origem por tag `NEBLI::origem::*`, associados pela tag da aula). Contagens não certificam qualidade. Guia pode oferecer seleção mais ampla de vídeos pertinentes, conforme Q028.

## 7. E1, guia e pacote por UC

E1/guia, quando aplicáveis, vão para a pasta privada existente da aula após revisão e conforme autorização vigente; sem inventar destino. Preservar organização e trabalho concorrente. E1 e pacote seguem o escopo e a autorização mais recente do MEMORY.

```text
python3 -m nebli.package_uc --uc UC03 --output <corrida>/NEBLI-UC03.apkg
```

Gerar da **UC inteira viva**, com compressão interna DEFLATE 9, mídia sem perdas e zero flags somente no arquivo. Não limpar/repor cores da coleção para exportar; conservar IDs/GUIDs e estudo. O utilitário verifica ZIP/SQLite/mídia, IDs e readback das flags, gera `.publication-ready.json` e não faz upload. Recusa saída existente, UC vazia, escopo divergente e formato `.anki21b` (trata SQLite legado `collection.anki21`/`collection.anki2`). Não restaurar APKG antigo para resolver falha.

Limite: exportação física. Compartilhados fisicamente em outra UC exigem união lógica isolada ainda não implementada; não mover/duplicar cards vivos nem anunciar pacote completo sem conferir essa diferença. **Upload privado reautorizado em F-20261002-CLAUDE-03/04.** Para publicar: ler `config/publicacoes-uc.json`, inicializar do `.example.json` só se ausente, resolver pasta privada e atualizar o file_id existente da UC; após timeout fazer readback. Verificar nome/bytes/pasta/permissões e só então registrar hash, IDs incluídos e confirmação. Não confundir arquivos antigos por aula com o arquivo da UC.

## 8. Manutenção solicitada e continuidade

Ferramenta disponível: `python3 -m nebli.decks status [trecho]`, `suspender|dessuspender <trecho> [--simular]`, `desfazer <registro>`, `liberar <trecho> [--treino] [--encerrar]` (`--treino` = cram sem reagendar), `instalar-addon`. Mudança de ramo inclui subdecks e só alcança raízes NEBLI, nunca AnKing/Referências. Ver o conjunto antes de aplicar. Registros em `arquivos-trabalho/deck-ops/` permitem desfazer os IDs exatos. Usar apenas para a manutenção solicitada, sem tarefa paralela durante geração de memória.

Add-on `nebli_decks`: lógica em `nebli/anki_addon.py`, total nos nomes, identidade pelo nome canônico. `liberar` usa `config/anki-decks.json` e filtrado acima da árvore para todos os novos do ramo; `--encerrar` devolve às aulas. Não recriar filtrados ou mudar opções por inferência. A contagem ao clicar usa `anki-contagem-pedido.json` / `anki-contagem-resposta.json` na pasta de trabalho (`nebli.decks.count_on_click`). Confirmar funcionamento no computador vivo; não presumir instalação pelo código.

Add-on `nebli_atalhos` (mesmo instalador, reiniciar o Anki): a/s/d/f respostas, q/w/e/r bandeiras vermelha/verde/azul/rosa, Caps Lock suspende (recusa verde), `'` enterra (F-20261003-CLAUDE-19), `v` volta (desfaz), `c` comentário; no AnkiDroid o mesmo mapa é configurado à mão em Controles; log em `addons21/nebli_atalhos/user_files/log.txt`. Carregar sem erro não prova que as teclas funcionam; só o uso de Davi confirma. A explicação por Tab existe no add-on separado `nebli_explicacoes`: balão flutuante na parte inferior, fonte 21 px, somente no verso. Instalar com `python3 -m nebli.explicacoes instalar` e reiniciar o Anki. A etapa AnkiDroid continua planejada no MEMORY.

Q068 registra o desejo de suspender azuis após prova; **não existe agendamento automático comprovado por este roteiro**. Implementação futura exige datas atuais, associação exata card/aula/prova, proteção de compartilhados ainda necessários e intervenções pessoais, simulação, registro e readback. Não aplicar durante esta consolidação. Monitor contínuo/tutor/macros não são requisitos da produção: prioridades no MEMORY.

Antes de fechar: reler FEEDBACKS e alterações concorrentes. Registrar todo retorno recebido nesta sessão e atualizar a preferência no MEMORY em seu lugar; mudanças técnicas neste roteiro, fontes no mapa e estado na fila. Feedback melhora próximas entregas; anteriores só quando pedidos. Evidência local não é sync entre PCs: numa troca, levar a versão atual do projeto e reconciliar os artefatos privados/Anki necessários. Não exigir novo questionário por falta de leitura.

## 9. Campanha de regeneração de 02/10 — próxima sessão Claude

Escopo F-20261002-CODEX-09/10: **UC08 P1 primeiro → UC03 P2, somente decks, sem E1**, entregues aula por aula completa e revisada. Demais provas são backlog. Preferências no MEMORY, sem novo handoff. Reset já feito por Davi: não excluir novamente nem restaurar pacotes/scripts antigos. Preservar estudo que já tiver começado.

### Preparação comum, antes da primeira entrega

1. Executar pesquisa atual de Anki/AnKing/Steps prevista em ANALISTA-RETENCAO: fontes oficiais, cobertura/limites, botões, tempo de recuperação e carga. Atualizar esse plano com resultados e fontes efetivamente lidas. Implementar leitor/analista sob pedido conforme o plano; não esperar semanas de histórico para entregar aulas nem inventar diagnóstico individual sem dados.
2. Conferir perfil/preset vivo. Configurar **40 novos globais por dia nos decks médicos NEBLI**, não 40 por aula/UC; verificar limites dos ancestrais e filhos e acesso a todas as revisões devidas. Preservar agendamento, estudo e outras opções. Implementar heatmap com novos únicos/dia do Anki, verde em ≥40, revisão pendente mostrada separadamente. Testes de 39/40/41, repetição, desfazer e virada de dia conforme ANALISTA-RETENCAO.
3. Implementar Tab curto (~5 linhas) e longo (cerca de 20, podendo passar um pouco), lado a lado, conforme GUIA-EXPLICACOES-TAB. Cache/versionamento por card, migração preservando o anterior, geração conjunta, concordância e cobertura das duas versões. Testar pequena amostra e interação real antes de gerar o lote completo.
4. Adequar a porta única `nebli.gates` ao escopo real antes de entregar. Correções locais F-20261002-CODEX-11: `fontes.json` aceita `"escopo": "cards"` (dispensa E1; padrão `e1+cards`); cobertura estruturada do Tab atual e reprovação de cobertura vazia/pendente/inconclusiva; plano vazio reprovado. **Ainda pendente:** conferência HY → verde por card com evidência e validação das duas versões do Tab, que ainda não foram implementadas. Não usar o gate do formato antigo como certificação do Tab duplo. Não usar `--sem-anki`/`--sem-drive` como certificado final. Motivo textual preenchido não comprova qualidade sem revisão semântica do §4. Acesso ao acervo CAOC indicado depende da conta FMUSP (ACERVOS-REFERENCIA); não marcar consultado com listagem vazia/404 do Gmail.

### Inventário e ordem de produção

- **UC08 P1:** AN01 → AN02 → BT03 → BT04 → AN07 → FI08 → FI09, conforme percurso docente conhecido; fontes/pastas na fila UC08. Confirmar conteúdo atual. Motilidade entra; bloco de secreções/digestão FI05/FI06 fica na P2, fora desta campanha. Relações célula–função ou efeitos motores ensinados na P1 não são removidos só por envolver hormônio.
- **UC03 P2:** levantar a lista com `python3 referencias-externas/uc03/consultar.py --listar --prova P2` e reconciliar `banco/aulas_uc03.yml` com pastas/slides atuais. A consulta em 02/10 listou 18 entradas específicas P2, mais 4 transversais PT/RD: edema/congestão, integração metabólica I/II, correlação PT/RD 2, patologia ambiental, oito entradas de Micro, operon, complemento, inflamação aguda, inflamação início/resolução e GR2. Transversais não autorizam reconstruir P1/P3/P4 inteiras; incluir somente alvos necessários à P2, sem duplicar identidades. Material introdutório/prática recebe tratamento conforme objetivos, não deck artificial por nome de pasta.
- Criar na corrida um inventário com aula, pasta, slides, prova/questão, exercícios/CAOC, livro/capítulo, vídeos, estado e pendência. Marcar o andamento da UC08 na fila existente; UC03 nos registros da campanha/corridas. Contagens antigas são referência histórica, nunca metas ou evidência de instalação atual.

### Ciclo de cada aula e entrega incremental

1. Fechar fontes antes da seleção: todas as lâminas, provas antigas e exercícios específicos, CAOC, capítulo pertinente da bibliografia confirmada e transcrições dos canais acompanhados. Perguntar só livro realmente desconhecido/ambíguo. Registrar busca e impacto de ausências; fonte importante pendente impede instalar.
2. Aplicar §§2–4: mapa slide → alvo → fonte → card. **Sem voar:** aprofundar o que pertence à aula, sem transformar capítulo/vídeo em curso paralelo. Prova antiga calibra recuperação/profundidade; não redefine o recorte. Sem teto de cards por aula e sem cortar alvos úteis para caber em 40/dia.
3. Priorizar AnKing → outros → MCAT/AnatoKing/Dope → autoral minoritário (gate ≤15%, F-20261003-CLAUDE-18), com busca externa real, 2–3 espelhos, inglês, frente curta e teste cego. Não omitir cobertura para cumprir percentual: melhorar busca/formulação e resolver o conflito antes da entrega.
4. Auditar cores por card: HY efetivo do recorte → verde; verde também para fundamentos duradouros sem HY. Justificar uso futuro, azul necessário à prova e rosa útil de menor prioridade. Demonstrar casos de fisiologia/anatomia/clínica e detalhes moleculares limítrofes sem classificar disciplinas inteiras automaticamente. Marcas pessoais preservadas e recomendação registrada separadamente se houver conflito.
5. Dry-run, escrita protegida, readback, ordem docente, ambas as explicações atuais e revisão visual. Registrar a cobertura completa e exemplos reais de cada decisão; não declarar validação longitudinal concluída.
6. Rodar `python3 -m nebli.gates arquivos-trabalho/<corrida>` sem falhas/checagens desconhecidas; publicar artefatos de cards no Drive conforme autorização vigente e escopo sem E1. Não gerar E1 para satisfazer uma checagem antiga. Verificar pacote, compartilhados, idioma e recebimento; pacote inglês não é tradução portuguesa concluída.
7. Entregar a aula com link/local, contagens vivas de origem/cores/estado, núcleo único e pendências honestas; continuar a aula seguinte sem exigir nova autorização para cada uma. UC08 P1 completa antes de iniciar UC03 P2. Interrupção deve deixar a próxima aula e pendências claras na corrida.

O total produzido pode ultrapassar 280 cards por semana; 280 é entrada planejada em sete dias. Todas as revisões devidas são adicionais. A ordem do Browser segue os slides; o agendador continua decidindo a ordem das revisões.

### Atualização de 02/10, depois da AN01 (F-20261002-CLAUDE-09)

- **Campanha em massa:** UC08 (P1, P2) → UC03 (P2, P3) → UC21 (insuficiência metabólica, depois o resto; verde = perguntas oficiais do caso) → UC01 e UC02 (núcleo pelas provas antigas). Organizar/renomear pastas bagunçadas no padrão; avisar slides faltantes.
- **Calibração contínua:** todo ajuste pedido numa aula entra em gate ou regra e é aplicado às aulas já entregues nesta campanha; manter em RECONSTRUCAO-UC08 a coluna de correções pendentes por aula.
- **Passo novo no ciclo, entre 5 e 6:** conferência final item a item com `cobertura.json` (slides, roteiro, exercícios → cards) feita no deck instalado; faltas corrigidas antes do gate. Anatomia: oclusões do próprio slide com `python3 -m nebli.slide_io`; Netter conferido.
- **Ordem:** entradas ordenadas pelo primeiro slide citado em `evid`, sem recuo; `due` dos novos igual à ordem.
