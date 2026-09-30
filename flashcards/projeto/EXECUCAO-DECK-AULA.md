# Execução de deck-aula — fontes, revisão e entrega

Roteiro técnico consolidado em 29/09/2026. Preferências e critérios somente no [MEMORY](../../MEMORY.md); decisões/casos em [FEEDBACKS](FEEDBACKS.md). Este roteiro orienta a sessão assistida: não é promessa de um gerador ou serviço já implementado. Não executar scripts antigos de aula, nem `nebli/anki_apply.py`, como gerador universal.

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

Se houver E1, ler [didatica/E1.md](../../didatica/E1.md) e suas referências, usando as mesmas fontes/objetivos. Build isolado, somente E1; revisão textual/visual do PDF e figuras. Na UC08 atual, E1 é `não aplicável — pedido explícito`; não torná-la requisito.

## 3. Buscar, selecionar e redigir

Primeiro procurar identidade NEBLI viva. Depois AnKing → alternativos pertinentes → AnatoKing quando anatômico → autoria por último. Buscar conteúdo/sinônimos, sistemas, tags de recursos, vizinhança e campos de modelos visuais; duas rotas AnKing e externos adequados antes da autoria. Ler candidatos/recusas; tag ou consulta vazia não prova lacuna. Registrar a busca por alvo, sem repetir aquisição de acervo já disponível.

Selecionar irmãos pertinentes individualmente, sem os cortes excessivos e sem importar outro assunto. Comparar alvo + resposta + habilidade na seleção viva, incluindo compartilhados. Prática adicional exige ganho; básico não é redundante por parecer fácil. Autoral só para lacuna relevante real. Comparar a forma com AnKing de verdade, conforme MEMORY: contexto, resposta, ocultações, verso, imagem e carga de recuperação; CSS/contagem de palavras não são qualidade.

Novas cópias/autorais em inglês (Q056–060). Idioma novo não autoriza converter decks anteriores. Manter proveniência e separar fonte original de adaptação curada; originais, modelos compartilhados de referência e AnkiHub preservados. Clone independente não herda vínculo ativo: `ankihub_id` vazio. Conservar fontes científicas úteis; retirar recurso/clínica lateral na curadoria da cópia, sem confundir bibliografia com propaganda. Links de vídeo ficam no guia/chat.

## 4. Plano, bandeiras e revisão

`plan.json` registra lesson_id/run_id, fontes/versões, sequência docente, alvo, evidência na aula, uso futuro concreto, necessidade de recuperação ativa, comparação com cobertura existente, decisão/motivo/incerteza, recomendação/cor; origem real, IDs de nota/card, cloze/template, identidade existente/nova, campos/mídia, associação a outras aulas, busca/autoria e ganho de pares mantidos. A cor nasce com a seleção, não de uma classificação genérica posterior da matéria. Respeitar marcas pessoais; registrar recomendação separada quando necessário.

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

Conferir plano versus coleção: notas/cards/clozes e origens, campos/modelos/mídia (incluindo `NEBLI_Comentario` presente e vazio em toda nota nova), cores previstas com marcas pessoais preservadas, IDs selecionados, história/agendamento e integridade dos originais. Verificação estrutural completa e revisão editorial por amostra são evidências diferentes.

Compartilhados: provar associação por IDs vivos e consulta com conjunto conferido. Se só existe busca no navegador, dizer; não anunciar botão de estudo na segunda aula pronto. Não duplicar para contornar limitação da interface. Sync aceito pelo AnkiWeb não comprova chegada em Mac/Android/Windows.

**Explicações do Tab (F-20260930-CLAUDE-11):** depois da instalação, gerar uma explicação por card da aula com `python3 -m nebli.explicacoes gerar 'deck:"<deck da aula>"'`. Cada card tem a sua, inclusive irmãos. A base fica fora da coleção e o estilo em `config/explicacao-tab.md`. Ler uma amostra (irmãos, autorais, imagem e todos os “revisar”) e registrar na REVISAO-DE-QUALIDADE; card marcado “revisar” é achado da própria revisão. `resumo` mostra explicações em estilo antigo.

Manter na mesma corrida `plan.json`, snapshot anterior, `journal.jsonl`, `receipt.json`, `verification.json` e `REVISAO-DE-QUALIDADE.md`. A revisão sintetiza, com links às evidências existentes:

- Versão/escopo, fontes realmente consultadas e varredura integral da aula; lacunas e exclusões relevantes.
- Escolhas concretas que demonstram o padrão de Davi: recuperação preservada, alternativa consultada, autoria necessária, relação clínica pertinente, imagem e bibliografia, núcleo sem quota.
- Inglês dos novos cards; forma comparada aos exemplos reais. Se houver revisão de tradução antiga explicitamente pedida, comparar base/resultado e declarar alcance real.
- Revisão realizada, amostra e limites; achados corrigidos ou pendentes; IDs dos feedbacks aplicados e versão dos critérios.
- Estados distintos: conteúdo revisado, instalação, acesso aos compartilhados, pacote, publicação e sync. Outra IA só assina sua revisão efetiva.

Não gerar um novo arquivo de política por aula. Relatório ao usuário é curto: onde estudar, cobertura/limites, núcleo, poucos exemplos e contagens (notas/cards únicos, novos/reutilizados/compartilhados, origens, autorais, cores/suspensos; aula e união da UC). Gerar a tabela final pelo Anki vivo com `python3 arquivos-trabalho/relatorio_decks.py "NEBLI::UCxx"` (somente leitura; origem por tag `NEBLI::origem::*`, associados pela tag da aula). Contagens não certificam qualidade. Guia pode oferecer seleção mais ampla de vídeos pertinentes, conforme Q028.

## 7. E1, guia e pacote por UC

E1/guia, quando aplicáveis, vão para a pasta privada existente da aula após revisão e conforme autorização vigente; sem inventar destino. Preservar organização e trabalho concorrente. A reativação de E1 não reativa upload de APKG.

```text
python3 -m nebli.package_uc --uc UC03 --output <corrida>/NEBLI-UC03.apkg
```

Gerar da **UC inteira viva**, com compressão interna DEFLATE 9, mídia sem perdas e zero flags somente no arquivo. Não limpar/repor cores da coleção para exportar; conservar IDs/GUIDs e estudo. O utilitário verifica ZIP/SQLite/mídia, IDs e readback das flags, gera `.publication-ready.json` e não faz upload. Recusa saída existente, UC vazia, escopo divergente e formato `.anki21b` (trata SQLite legado `collection.anki21`/`collection.anki2`). Não restaurar APKG antigo para resolver falha.

Limite: exportação física. Compartilhados fisicamente em outra UC exigem união lógica isolada ainda não implementada; não mover/duplicar cards vivos nem anunciar pacote completo sem conferir essa diferença. **Upload APKG permanece pausado.** Se Davi o reautorizar: ler `config/publicacoes-uc.json`, inicializar do `.example.json` só se ausente, resolver pasta privada e atualizar o file_id existente da UC; após timeout fazer readback. Verificar nome/bytes/pasta/permissões e só então registrar hash, IDs incluídos e confirmação. Não confundir arquivos antigos por aula com o arquivo da UC.

## 8. Manutenção solicitada e continuidade

Ferramenta disponível: `python3 -m nebli.decks status [trecho]`, `suspender|dessuspender <trecho> [--simular]`, `desfazer <registro>`, `liberar <trecho> [--treino] [--encerrar]` (`--treino` = cram sem reagendar), `instalar-addon`. Mudança de ramo inclui subdecks e só alcança raízes NEBLI, nunca AnKing/Referências. Ver o conjunto antes de aplicar. Registros em `arquivos-trabalho/deck-ops/` permitem desfazer os IDs exatos. Usar apenas para a manutenção solicitada, sem tarefa paralela durante geração de memória.

Add-on `nebli_decks`: lógica em `nebli/anki_addon.py`, total nos nomes, identidade pelo nome canônico. `liberar` usa `config/anki-decks.json` e filtrado acima da árvore para todos os novos do ramo; `--encerrar` devolve às aulas. Não recriar filtrados ou mudar opções por inferência. A contagem ao clicar usa `anki-contagem-pedido.json` / `anki-contagem-resposta.json` na pasta de trabalho (`nebli.decks.count_on_click`). Confirmar funcionamento no computador vivo; não presumir instalação pelo código.

Add-on `nebli_atalhos` (mesmo instalador, reiniciar o Anki): a/s/d/f respostas, q/w/e/r bandeiras vermelha/verde/azul/rosa, Caps Lock suspende (recusa verde), Shift sozinho edita, `v` volta (desfaz), `c` comentário; no AnkiDroid o mesmo mapa é configurado à mão em Controles; log em `addons21/nebli_atalhos/user_files/log.txt`. Carregar sem erro não prova que as teclas funcionam; só o uso de Davi confirma. A explicação por Tab está planejada no MEMORY e não existe ainda.

Q068 registra o desejo de suspender azuis após prova; **não existe agendamento automático comprovado por este roteiro**. Implementação futura exige datas atuais, associação exata card/aula/prova, proteção de compartilhados ainda necessários e intervenções pessoais, simulação, registro e readback. Não aplicar durante esta consolidação. Monitor contínuo/tutor/macros não são requisitos da produção: prioridades no MEMORY.

Antes de fechar: reler FEEDBACKS e alterações concorrentes. Registrar todo retorno recebido nesta sessão e atualizar a preferência no MEMORY em seu lugar; mudanças técnicas neste roteiro, fontes no mapa e estado na fila. Feedback melhora próximas entregas; anteriores só quando pedidos. Evidência local não é sync entre PCs: numa troca, levar a versão atual do projeto e reconciliar os artefatos privados/Anki necessários. Não exigir novo questionário por falta de leitura.
