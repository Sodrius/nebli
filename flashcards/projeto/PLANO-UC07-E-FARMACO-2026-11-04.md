# Planejamento UC07 e Farmacologia — 04/11/2026

Executor dos decks: Claude. Planejamento com Davi; este documento registra diretrizes já pedidas e decisões ainda abertas. Não é ordem para gerar ou reformular decks agora. Ler também MEMORY e o pipeline vigente.

## UC07 — organização e seleção

A unidade do deck é o conteúdo do cronograma. Usar em conjunto material de veteranos, provas, bibliografia e aulas/transcrições; a ordem é a do cronograma. A fala mais recente de Davi substitui a restrição antiga de incluir uma estrutura apenas se mencionada literalmente na transcrição: bibliografia e materiais de veteranos/provas também fundamentam a seleção, e cabe um pequeno aprofundamento além deles.

Antes de gerar, montar matriz por aula: estrutura/relação, fonte e página/questão, objetivo (identificar, situar, comparar, explicar função ou relacionar lesão), prioridade, imagem disponível e notas de acervo existentes. Registrar acréscimos além dos materiais como tal, com ganho explicado. Não importar automaticamente todo o atlas: escolher poucas estruturas extras de valor anatômico, funcional ou clínico. A quantidade final será calibrada com Davi ao ver o inventário, sem percentual inventado como regra já aprovada.

### Estratificação proposta para discutir

| Bandeira | Critério | Papel no estudo |
|---|---|---|
| Verde | estruturas/relações essenciais à compreensão, alvos recorrentes de prova ou centrais dos materiais | núcleo duradouro de cada aula |
| Azul | cobertura importante dos materiais e bibliografia; relações, função e distinções que completam o núcleo | domínio consistente do assunto |
| Rosa | poucos acréscimos além do conjunto de materiais, com utilidade anatômica/funcional/clínica clara | aprofundamento selecionável |

Estar na prova não é o único critério de importância; frequência, papel de fundamento e ganho de compreensão contam. O tipo do card (imagem/organizador/função/clínica) não determina a bandeira. Preservar a bandeira vermelha como sinal de problema do usuário. Se três faixas não bastarem, propor subdivisões por etiquetas, com filtro de estudo, sem consumir cores usadas pelos comandos pessoais. Esta tabela é proposta de operacionalização, não calibração numérica concluída.

### Composição de cada deck

- **Imagem Kenhub + AnKing primeiro:** identificação com imagem Kenhub e destaque/seta conforme o padrão aprovado; buscar AnKing para relações, mecanismos, função e associação clínica. Outros acervos entram quando a fonte preferida não atende; autoral apenas para lacuna demonstrada.
- **Organizadores em quantidade suficiente:** abrir conjuntos e trajetos, distinguir estruturas parecidas, conectar posição, componentes e função. Cada organizador deve testar a relação essencial e coexistir com os cards visuais que têm ganho próprio. Não criar um resumo longo nem um organizador por estrutura por obrigação.
- **Função integrada:** para cada bloco anatômico, explicar o que faz e como sua posição/conexões permitem a função. Selecionar as relações recuperáveis mais importantes e usar o Extra para apoio.
- **Clínica associada:** integrar localização de lesão, déficit esperado ou associação clássica que dê sentido à anatomia. Preferir acervo AnKing e o nível do curso; não preencher quota clínica nem transformar cada estrutura numa ficha de doença.
- **Percurso:** situar região/conjunto → identificar estruturas → recuperar relações/organização → função → aplicação clínica pertinente. Manter a ordem das aulas do cronograma, com retomadas de pré-requisitos no ponto de uso.

A auditoria final deve conferir cobertura das fontes, acréscimos limitados e justificados, distribuição real de prioridades, imagens, organizadores e relações de função/clínica por bloco. Ausência de card funcional/clínico precisa ser julgada no bloco; uma frase decorativa no Extra não prova cobertura.

## Transcrição das aulas baixadas

Davi informou que já baixou todas as aulas e quer transcrição com Whisper antes da geração pelo Claude. **Nesta sessão a transcrição ainda não começou.** Antes do lote: localizar pasta exata, cruzar nomes/duração com cronograma e transcrições existentes, listar o que falta e conferir espaço/modelo disponível no `whisper-local`. Não baixar novamente material já disponível.

Criar manifesto com arquivo original, aula do cronograma, duração, hash, saída, modelo/idioma e estado (pendente/concluído/falha/revisado). Produzir texto pesquisável e versão com tempos quando suportada, sem substituir originais ou transcrições existentes; processar incrementalmente, preservando saída de cada aula para retomada. Vocabulário anatômico duvidoso deve ser conferido com slides/bibliografia e marcado quando incerto. Transcrição automática não equivale a aula lida nem libera gerar deck sem E2/E3.

Guardar áudio/vídeo e transcrições integrais em armazenamento privado/local; Git recebe scripts, manifesto sem dados sensíveis e plano, não vídeos nem material protegido integral. Antes de entregar ao Claude, informar caminhos reais dos arquivos (ainda não identificados), aulas concluídas e pendentes.

## Farmacologia — revisar o plano existente com o material acumulado

Presumir UC19 conforme o histórico; confirmar no inventário se houver material de outra UC. Ler [PLANO-DECK-PROVA-UC19](PLANO-DECK-PROVA-UC19-2026-10-29.md). Já existem três lotes instalados no histórico; a afirmação de Davi de que ainda não começou a estudar não significa que não há deck. Conferir estado vivo antes de planejar substituição ou criar cópias.

Inventariar material novo de veteranos, provas e gabaritos, apostilas/objetivos e bibliografia, com versão e recorte. Reconciliar a matriz anterior: coberto, parcial, ausente, redundante, divergente. Apresentar a organização final por assunto da prova, progressão de princípios e os lotes que realmente precisam de complemento/revisão. Manter AnKing primeiro, mecanismos, organizadores úteis e aplicação clínica que explique o princípio, conforme o plano vigente. Não transpor automaticamente a proporção de imagens ou de estruturas extras da UC07 para Farmacologia.

Planejar com Davi antes da geração pelo Claude: aproveitar material novo para completar e melhorar o percurso, preservando histórico e decisões pessoais. Falta verificar fontes novas e os três lotes existentes, inclusive pendências de entrega do lote 3; este documento não declara essa auditoria concluída.

## Retomada pelo Claude

1. Ler AGENTS, ESTADO-ATUAL, MEMORY e este documento; respeitar a intenção atual de planejar antes de gerar.
2. Localizar os materiais baixados e montar os inventários UC07 e Farmacologia, sem declarar leitura não feita.
3. Apresentar a Davi organização por aula/assunto, critérios das bandeiras, acréscimos e composição dos decks com exemplos reais do material.
4. Fechar com Davi as escolhas de profundidade/estratificação e só então executar a geração autorizada pelo pipeline.

## Estudo temporário dos suspensos

“Estudar tudo” passa a incluir suspensos, inclusive quando acionado num subdeck. O Anki exige liberação temporária para estudar no filtrado; o add-on registra antes a suspensão por card no perfil local. Ao sair do filtrado ou apagá-lo, restaura a suspensão original fora da revisão. O registro sobrevive a reinício; cards que continuam no filtrado permanecem disponíveis. O recálculo de memória FSRS continua usando o histórico de respostas e não deve dessuspender os cards restaurados. A restauração automática exige abrir o perfil com o add-on ativo neste computador; o registro é local e não acompanha AnkiWeb. Conferência visual do fluxo no Anki ainda pendente; não afirmar validação real por testes simulados.
