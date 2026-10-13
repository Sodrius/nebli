# MEMORY — o que Davi quer (regra única e vigente)

Reorganizada em 13/10/2026 (F-20261013-CLAUDE-02) a partir de todas as falas registradas em [FEEDBACKS](flashcards/projeto/FEEDBACKS.md). **Este é o único documento de preferências.** Procedimento: [EXECUCAO-DECK-AULA](flashcards/projeto/EXECUCAO-DECK-AULA.md). Estado e fila: [ESTADO-ATUAL](ESTADO-ATUAL.md). A versão anterior, em camadas, está em `arquivo/2026-10-13-reorganizacao/MEMORY.md` e **não é norma**.

**Como manter:** feedback novo de Davi → literal em FEEDBACKS → a regra correspondente aqui é **reescrita no lugar** (não se acrescenta outra camada; o que ela substitui sai) → se for mecanizável, vira check no `lint_cards`/`gates`. A fala mais recente prevalece. Não pedir que Davi reensine nada que está aqui.

## 1. Como trabalhar com Davi

- **Um pedido curto basta.** “Faz a aula X”, “continua”, `/deck-aula X` ou só o nome da aula = rodar o roteiro inteiro até o deck instalado, revisado e entregue. Sem briefing, sem plano para aprovar, sem pedir permissão (“gosto que vc já faça”; “nunca mais pede permissão”). Só perguntar o que for indispensável ou decisão realmente dele.
- **Sem agente.** O executor faz o deck direto, do começo ao fim (agentes reliam todo o contexto e paravam no limite de uso). Passos mecânicos por `python3 -m nebli.artefatos`, que mostra só falhas. Economizar tokens: sem releituras, sem despejos inteiros de busca, sem polling, Tab em segundo plano.
- **Contínuo até Davi mandar parar.** Ao fim de cada deck: relato curto no chat (formato no §11) e dúvidas objetivas com a suposição adotada, também no ESTADO-ATUAL; seguir sem esperar resposta. Qualidade acima de velocidade.
- **Outro executor (Codex) trabalha em paralelo.** Antes de começar uma aula, conferir e registrar a reivindicação no ESTADO-ATUAL (“Com Claude/Com Codex”); nunca mexer em corrida, aula ou arquivo de trabalho reivindicado por outro. Reler o arquivo antes de gravar e mesclar, sem sobrescrever trabalho concorrente.
- **Davi estuda no Anki enquanto o executor trabalha; isso não bloqueia.** Nunca alterar a nota em exibição (`guiCurrentCard`) nem seus irmãos (adiar só essas); não mexer na tela; escrita com `sync=False` enquanto ele revisa e sync quando ocioso; readback após cada lote.
- **Entrega padrão: só o deck** (com Tab). E1–E3 apenas sob pedido explícito (“E1 + deck” inclui ambos).
- **Feedback muda as próximas entregas.** Deck anterior só é corrigido quando Davi pede (inclusive revisões incrementais que ele autorizou), mas erro achado na aula em produção é corrigido antes de entregar.
- Não fabricar leitura, busca, teste ou revisão. Gate aprovado não prova julgamento; documento atualizado não prova implementação; carregar sem erro não prova que funciona na tela de Davi.

## 2. O deck que Davi quer

**Para que serve (F-20261013-CLAUDE-03):** o deck cobre a aula, na ordem da aula, para Davi fixar os conceitos do curso, mais os aspectos do Step 1 associados, sobretudo os HY e mais importantes. Ele estuda ~50 min/dia e faz cram antes da prova: memória de curto prazo (ter o conceito “na bag” para entender o próximo) e de longo prazo (40 novos/dia + revisões), para chegar ao fim do curso com base de compreensão e de memorização. É **ciclo básico**: entender bem o básico, às vezes com um exemplo de ilustração; não é aula de clínica, semiologia nem fisiopatologia elevada.

1. **O deck é a aula.** Davi abre o Browser e reconhece a aula na ordem em que foi dada, como se o professor tivesse planejado os cards. Cada card aponta para objetivo e fonte da aula.
2. **Permite percorrer a aula inteira para rever seus conceitos e mantê-los a longo prazo** (F-20261013-CODEX-04). Reduzir especificidades exige reconstruir a progressão dos mecanismos e conferir os conceitos centrais ausentes; uma lista menor ainda pode conter assuntos deslocados e lacunas. **Cobre as capacidades e relações centrais da aula inteira**, com profundidade, dentro do recorte. Cada objetivo ensinado tem recuperação própria (sequência: transições decisivas; comparação: diferença decisiva; imagem: reconhecer sem legenda quando isso é objetivo). Menção no Extra não substitui recuperação.
3. **Princípio claro antes do detalhe, e os dois na ordem lógica.** Não adianta perguntar quando usar gentamicina se antes não houver card do que é um antibiótico, do mecanismo geral e do que é um aminoglicosídeo (exemplo de Davi; também corantes sem a distinção de colorações). Toda aula costuma ter os dois níveis e os dois são cobertos: o princípio vem primeiro na ordem do deck; quando a aula é aprofundada no detalhe, o detalhe é coberto também. Se o princípio foi dado em aula anterior, associar o card existente (`sh()`) antes dos detalhes; se nenhuma aula o deu, criar o card de princípio. Ordem de prioridade: fundação → distinção/mecanismo → aplicação/detalhe pertinente.
4. **Mecanismo geral que permite entender vários casos** (F-20261013-CODEX-02). O núcleo recuperável explica como e por que o processo acontece, independentemente da doença usada como exemplo. Os detalhes entram para aprofundar essa compreensão; não basta acumular nomes de mediadores, patógenos ou achados específicos. Clínica serve só de ilustração do mecanismo, preferencialmente no Extra/Tab; card clínico próprio apenas quando for alvo explícito da aula/prova. Inflamação granulomatosa é a regressão concreta: excesso de especificidades sem explicação suficiente do mecanismo geral.
5. **Autoral que Davi não distingue do AnKing** (§6). AnKing original preservado.
6. **Tamanho é consequência**, sem teto e sem quota de cards ou de cores. Uma aula introdutória raramente passa de ~100 cards; uma aula densa pode ter muito mais.

Referências positivas: Antibióticos v3 (“agora sim gostei”), Correlação 2, Vascularização das vísceras e BT04 (imagem da migração epitelial). Regressões a não repetir: UC19 FA01 (tabelas de fármacos no lugar de agonismo/antagonismo/curvas), Diagnóstico radiológico (oclusões de exemplo e física das aulas específicas), Diagnóstico patológico (aterosclerose/infarto), Genética bacteriana (pormenores e cor alta), Edema piloto (mini-aulas de doenças), Intestinos (listas de marcadores). Antes/depois concretos em `arquivos-trabalho/revisao-pontual-claude-2026-10-12/REVISAO.md` (critérios, não números).

## 3. Escopo da aula (decidir antes de escolher cards)

- **Ler o cronograma** (pasta da turma, “grade não oficial”; lista de aulas na pasta pessoal) e os títulos/objetivos das aulas vizinhas, passadas e futuras. Escrever um mapa curto: objetivo da aula → conceitos centrais → exemplos ilustrativos → subtemas com aula própria. Conferir os decks vizinhos já feitos.
- **Aula introdutória = guarda-chuva:** cobrir muito bem os conceitos gerais e as relações que permitem entender os exemplos; não aprofundar o que a aula específica vai dar.
- **Nem tudo que é exemplo da aula vira card.** Muitas vezes é só ilustração: passa batido ou vira um pequeno comentário no Extra do card do conceito (nem oclusão de imagem). Vira card só se a aula exige reconhecê-lo, se distingue uma aplicação importante ou se é cobrado diretamente.
- **Cada assunto mora numa aula.** Se há aula própria no cronograma, aqui ele no máximo vira uma linha de Extra. Card repetido entre decks fica num só (o da aula feita primeiro); a outra aula associa a nota existente (`sh()`), com sua própria cor. Se uma aula posterior mostra que um card anterior está no lugar errado, remanejar associação/posição preservando identidade e histórico, sem duplicar.
- **Detalhe só entra quando a aula o ensina como alvo ou a prova o cobra**; aí é rosa (número, nome de experimento, lista, exemplo lateral) ou azul se a prova exige. Detalhe que só aparece de passagem, de outra aula ou de assunto externo não entra “por segurança”: Extra, aula própria ou pergunta a Davi. A P2 da UC03 ficou com cards demais por repetição e por detalhe que não era para entrar.
- **Profundidade de ciclo básico** (Radio e Pato da P1 ficaram com detalhe demais): entender o princípio do método/da lesão e reconhecer o básico; nada de semiologia, conduta, manejo ou fisiopatologia elevadíssima, salvo quando a aula ensina aquilo como alvo.
- **Sem repetição**: o mesmo fato não é cobrado duas vezes na UC (nem em duas aulas, nem em dois cards da aula) sem ganho próprio declarado; a análise do deck-prova (§12) procura repetições na prova inteira.
- **Item de prova antiga e item do material da aula sempre têm card** (rosa se lateral). Item do livro que pertence a outra aula pode ser excluído com o motivo citando essa aula. Prova antiga sozinha não amplia o recorte além dos slides atuais.
- **Fonte docente desatualizada ou contraditória:** registrar a divergência e usar a formulação correta; não ensinar um absoluto falso.
- Antes de instalar, conferir **o núcleo separadamente da contagem**: os conceitos centrais aparecem como tarefas recuperáveis? Algum card de exemplo ocupa o lugar de um princípio ausente? Os casos de fronteira entre aulas estão resolvidos?

## 4. Fontes (ler antes de selecionar)

- **Base da aula:** lâminas (versão 2026 na pasta pessoal `Medicina/Material de estudo/A - Primeiro ano (2026)/UC<NN>/<componente>/<NN - aula>/` primeiro; a pasta da turma pode ter versão antiga ou outro professor), **pasta inteira da aula no drive da turma** (`TURMA 114/1º ano/<UC>/<componente>/Aula NN`: lâminas I/II, transcrição, exercícios, palavras-cruzadas, bibliografia; vídeos `.mp4` descartados com motivo), monitoria da prova (`<componente>/Material para Estudos/`, só a seção da aula), apostilas de veteranos (`UC03/Outros/Apostilas de veteranos`, só a seção), provas antigas (`python3 referencias-externas/uc03/consultar.py --slug <slug>`, ler as questões diretas) e o capítulo da aula no livro da UC.
- **Livros da UC:** UC01 Lehninger/Alberts/Guyton; UC02 Junqueira/Netter (+ apostila de lâminas, Histology Guide); UC03 Abbas/Janeway (Imuno), Robbins (Pato; também em `Patologia/Bibliografia Básica` da turma), Lehninger/Alberts (Biomol), Trabulsi (Micro), ESR/Mello (Radio); UC08 Guyton/Aires/Junqueira/Moore/Netter; UC17 Angelo Machado; UC19 Rang & Dale + `UC19/Outros`; UC21: caso guia cobertura, perguntas/HY guiam verde. Livro desconhecido após consultar aqui → perguntar a Davi.
- **Vídeos dispensados** (F-20261010-CLAUDE-06): não transcrever videoaulas nem YouTube; não buscar vídeos para cumprir gate.
- Material NEBLI (“etapas 1 a 3”, E1 antiga) não é base: pode confirmar, nunca originar alvo.
- **Fonte essencial ausente (lâminas) → não instalar**; preparar o possível e relatar. Fonte opcional ausente não bloqueia: registrar busca e impacto. Antes de declarar o drive da turma inacessível: `pgrep -f "Google Drive"`; se fechado, `open -a "Google Drive"` e tentar de novo.
- Divergência entre AnKing e slide/livro: AnKing é a referência preferida, mas erro demonstrado é corrigido na cópia e registrado. Canal ou fonte que contradiz a aula perde.

## 5. Busca e seleção

- **Ordem:** cópia NEBLI viva (`"tag:NEBLI::source::nid-<nid>"` → `sh()`) → AnKing → Referências Externas (MCAT, Histology, AnatoKing; Dope só sem alternativa) → autoral por último. Buscar por frases e sinônimos (`nebli.busca_acervos`), não siglas curtas; ler candidatos e motivos de recusa. “Não achei” após uma consulta não prova lacuna.
- **Irmãos clozes pertinentes à aula entram todos**; irmão de outro assunto não. Dois cards equivalentes sem ganho são redundância; básico útil não é redundante por ser fácil.
- **Autoral só para alvo que importa e não se achou**, com ganho próprio de recuperação; detalhe sem card e sem ganho fica no Extra ou no Tab. Mais de 15% de autorais é gatilho para auditar a busca, não limite.
- **HY 1–2 do recorte é verde**, salvo HY que repete o alvo de outro card (azul, com `hy_repete`) ou clínica lateral justificada (`clinica_lateral`). Etiqueta HY não autoriza importar irmão lateral.
- Poucos cards de conexão entre blocos, rosas, só com ganho real e construção AnKing.

## 6. Escrita (padrão AnKing real)

- **Uma frase que ensina um processo e oculta um nome**: frente natural, contexto suficiente, cloze focal (de preferência uma palavra, no fim quando a frase fica natural; até 3 palavras), ~15 palavras (90% dos AnKing até 23). Pergunta ou afirmação, conforme a forma mais natural. Dois clozes só quando o contraste é o alvo.
- **Nunca** `;` juntando afirmações nem `:` como rótulo na frente. Não reduzir a um nome de exemplo quando o objetivo é o mecanismo; não cortar qualificador só para encurtar.
- **Inglês** na frente e no Extra (Tab em português). Sem metatexto (“slide N”, “the lesson”, “this card”, “in the figure”).
- **Negrito como no AnKing**: 1–2 trechos de contexto/sujeito (raramente dentro do cloze); sublinhado para qualificador. Autoral sem negrito reprova no lint.
- **Extra:** vazio ou bullets `- ` curtos que acrescentam raciocínio, detalhe ou conexão útil; nunca repete a resposta, nunca parágrafo nem curadoria. Extra do AnKing preservado (acrescentar com `extra_add`). Ao limpar Extra herdado, julgar texto e cada imagem separadamente (tabela/algoritmo lateral sai; figura que ensina fica).
- **Cada autoral nasce de 2–3 espelhos AnKing** escolhidos pela função da pergunta (`"espelhos"` no plano). Dica no cloze (`{{c1::x::dica}}`) só em poucos casos realmente ambíguos. Não inventar mnemônico.
- Conferir resposta vazada em cada irmão (texto visível, figura, seta, título, legenda) e frente/verso renderizados.

## 7. Imagens e gráficos

- Imagem quando ensina ou testa o alvo (estrutura, morfologia, patologia, radiologia: reconhecer sem legenda), nunca decoração. Ordem: AnKing → livro da UC recortado (`nebli.img_figura`, sem título nem legenda) → fonte aberta (Histology Guide, Leeds) → lâmina da aula (obrigatória quando a imagem do caso é o objetivo, como nas correlações).
- **Toda figura é vista e julgada** (nitidez, enquadramento, pertinência) e registrada em `spec.IMAGENS_VISTAS`. Cortar título/legenda/seta que entregue a resposta (ex.: “Sinal do menisco” fora da figura).
- **Gráfico exige leitura real da figura:** a pergunta não antecipa deslocamento, platô ou interpretação; identificar curvas por letra, posição ou símbolo; interpretação no Extra.
- Sem crédito de imagem visível no card (proveniência só no plano). Sem cards de foto clínica salvo pedido. Rótulos científicos em inglês preservados.

## 8. Cores (por alvo, por aula, sem quota)

| Cor | Significado |
|---|---|
| Verde (3) | Núcleo da aula que vale manter por anos; HY pertinente; clínica ligada ao alvo pode ser verde. |
| Azul (4) | Essencial para a prova, menor necessidade de manutenção longa. |
| Rosa (5) | Detalhe útil e pertinente à aula, de menor prioridade e pouco ganho longitudinal. Não autoriza assunto externo. |
| Vermelha (1) / Laranja (2) | Marcas de Davi: pedido de rever / comentário pendente. Nunca atribuir. |

- Cor nasce na seleção, com motivo por card. Sem meta de percentual: promover conceitos organizadores e rebaixar exemplos conforme o ganho, nunca “reduzir verdes até N”.
- **Cor é por aula:** tag `NEBLI::cor::<lesson_id>::<cor>`; a bandeira visível é a maior entre as aulas; nunca baixar bandeira existente nem sobrescrever marca pessoal.
- Referência agregada de Davi: ~300 cards dessuspensos por semana de aula e meta de 40 novos/dia; servem para avaliar carga, não para cortar cobertura.

## 9. Tab (explicação por card)

- Davi: os Tabs “não ajudam tanto a entender profundamente, estão pouco didáticos”; quer **mais explicação, menos rótulo** e **começar do princípio** (F-20261013-CLAUDE-03). Um Tab por card (inclusive irmãos e compartilhados), em português, **em texto corrido de 2–4 parágrafos, sem rótulos**: começa no princípio mais geral de que o card depende e desce um degrau por vez até o assunto (antibiótico → mecanismo geral → aminoglicosídeo → gentamicina), constrói a resposta pelo mecanismo com o porquê de cada passo (exemplo concreto quando faz a ideia clicar), e fecha situando a ideia na aula e com a confusão real, se houver. Tamanho pelo caminho necessário (200–300 palavras num princípio difícil). Estilo e exemplos em `config/explicacao-tab.md`; o validador recusa rótulos, lista, passos numerados e parágrafo único.
- Gerar pela **tag da aula** (`"tag:NEBLI::<lesson_id>"`), nunca por nome de deck. Entrega só com `resumo` = faltando 0, desatualizada 0, revisar 0, formato_incompleto 0, e uma amostra lida (imagem, autoral, AnKing).
- Segundo Tab com o balão aberto = Davi reprovou aquele Tab: `python3 -m nebli.explicacoes ruins` antes de revisar Tabs de uma aula; reescrever os reprovados.
- Tabs antigos continuam valendo; não regenerar a coleção inteira por mudança de estilo.

## 10. Anki: escrita, suspensão, ordem, comentários

- **Escrita** só por `nebli.decks.escrita()` (lock `arquivos-trabalho/ANKI-ESCRITA.lock`), backup antes e readback depois; regras de Davi estudando do §1. Hierarquia `NEBLI::UCxx::Px::Componente::Aula`.
- **Suspensão por fase** (F-20261011-CLAUDE-06): disponíveis (dessuspensos) UC08 P1/P2, UC03 P3 e aulas novas (UC19 em diante, conforme dadas); **deck novo de aula antiga** (UC03 P1/P2, UC02, UC01; UC21 pela data da aula) **entra suspenso** até Davi analisar. Não suspender em massa deck existente. Suspensão pós-prova é manual de Davi. Ao desassociar compartilhado, restaurar suspensão e bandeira anteriores.
- **Ordem da aula:** ordem crescente das lâminas, inclusive compartilhados; tag `NEBLI::ordem::<curto>-<NN>`; coluna “Ordem da aula” mostra só números. `nebli.ordem verificar` sem falha.
- **Retiradas:** `nebli.retira` suspende com tag `NEBLI::retirado::<motivo>`, preservando comentário. Apagar notas só quando Davi autoriza (“sobre as notas, pode apagar / se for precisar volta”), sempre com backup recuperável e protegendo associações de outras aulas.
- **Comentários de Davi** (campo `NEBLI_Comentario`, vazio em toda nota nova; o executor nunca escreve nele) são feedback. Protocolo aprovado (F-20261011-CLAUDE-01) quando ele pedir “corrige os comentários”: ler todos, inclusive `CORRIGIDO` (vale o texto após o último marcador; positivos calibram) → agrupar por família do defeito → medir o alcance no Anki → corrigir a nota e todas com o mesmo defeito (irmãos, resposta vazada, Tab) → escrita segura → só depois de validar, dessuspender se suspenso e anexar `CORRIGIDO, DD, MM, YY.` preservando o texto → registrar literal, regra e check novo no mesmo dia.
- Uma identidade/histórico por card; preservar IDs, comentários, marcas, suspensões pessoais. Não ressuscitar cards/decks apagados.

## 11. Entrega e relato

- **Drive:** lâminas da aula na pasta pessoal da aula; **um só `.apkg` por UC** (`NEBLI - UCxx.apkg`), republicado a cada deck; nada de `.apkg` por aula. Sync ao final (ou adiado se Davi estiver revisando). Gates 100% (`nebli.gates <corrida>`).
- **Relato no chat (curto, em português):** deck e contagens (notas/cards, verde/azul/rosa, AnKing/autorais, compartilhados; lidas do Anki vivo), o que entrou e o que ficou de fora com o motivo, erros corrigidos na revisão, gates, e as perguntas objetivas com a suposição adotada. Detalhes técnicos ficam na corrida.

## 12. Uso do Anki por Davi (ferramentas existentes; não mudar sem pedido)

- Atalhos (add-on `nebli_atalhos`; no tablet configurados no AnkiDroid): a/s/d/f respostas; q/w/e/r bandeiras vermelha/verde/azul/rosa; Caps Lock suspende (recusa verde); `'` enterra; `v` volta (desfaz); `z` refaz o que o `v` desfez (como Ctrl+Y; F-20261013-CLAUDE-03); `c` comentário; Tab = explicação. Todo atalho novo precisa de equivalente no tablet.
- Browse: J ou Enter alterna suspensão; Delete/Backspace apaga e renumera a ordem; nome do deck mostra total|dessuspensos|novos; nome da aula em negrito. “Estudar tudo” reagenda e recalcula a memória FSRS. Filtrados podem ser apagados à mão (o add-on não recria).
- Preset de novos: conferir o valor vivo; não restaurar valores antigos nem mudar opções por inferência. Rotina de entrada dos decks antigos: Davi decide; não propor quotas.
- **Pedidos futuros registrados (não executar sem pedido):** add-on único NEBLI para compartilhar (`ADD-ON-NEBLI.md`); pacote da UC traduzido para português; Tab no tablet (`userJs1` + mídia oculta); heatmap da meta de novos; analista de retenção (`flashcards/projeto/ANALISTA-RETENCAO.md`); resumo de sanguessugas por e-mail sob pedido. Sem monitor contínuo.

## 12b. Análise do deck-prova e do deck-UC (F-20261013-CLAUDE-03)

Além de cada aula, o conjunto: quando as aulas de uma prova estiverem feitas (e quando Davi pedir), rodar `python3 -m nebli.analise_prova "NEBLI::UCxx::Pn"` (ou a UC inteira) e julgar, lendo todas as frentes na ordem: **cobertura** (cada aula e o conjunto), **ordem lógica** (a prova ensina numa progressão que faz sentido), **princípios muito importantes têm card antes dos detalhes**, **detalhes se complementam** (sem repetição nem buraco), **peso de ciclo básico** e **qualidade dos Tabs**. Quando a ordem das aulas do curso é bagunçada, **não se reorganizam decks**: acrescentam-se alguns cards-ponte em cada deck (princípio que faltava, ligação entre aulas) para que a revisão do deck-prova inteiro cubra o importante de forma progressiva e didática. Correções vão para os specs das aulas (retirar repetido/detalhe, rebaixar, acrescentar princípio), com Tab regenerado nos cards afetados; o julgamento fica em `RELATORIO.md` da análise.

## 13. Erros que já aconteceram — conferir em toda aula

Os mecanizáveis já são reprovados por lint/gates (ver `nebli/lint_cards.py` e `nebli/gates.py`); a tabela completa de 29/09–12/10 está no MEMORY arquivado. Estes dependem de julgamento:

- Prova com cards demais (UC03 P2): repetição e detalhe que não era para entrar; Radio/Pato P1 com detalhe clínico acima do ciclo básico. → §3 e análise do deck-prova (§12b).
- Detalhe cobrado sem o princípio que o explica (gentamicina sem “o que é antibiótico/aminoglicosídeo”). → `ESCOPO` com princípio antes do detalhe; `pre` reprova a ordem inversa.
- Aula introdutória virou coleção de exemplos; núcleo (gráficos, conceitos gerais) só no Extra. → Mapa de escopo do §3 antes de selecionar; passada pelo núcleo antes de instalar.
- Verdes inflados por trivial, por conteúdo de outra aula ou por HY lateral. → Verde só para núcleo duradouro do recorte.
- Autoral com mecanismo errado ou figura herdada errada. → Conferir cada autoral no livro da matéria; ver toda mídia das cópias.
- Card cobrindo item de prova/material da aula retirado junto com exemplos. → Antes de retirar, listar itens que ficariam sem card.
- Cards na lâmina errada; histologia com imagem de diagrama. → Ver as lâminas antes de numerar.
- Pergunta de gráfico entregando a interpretação; título da figura revelando a resposta. → §7.
- Fonte marcada como lida sem leitura integral. → Ler antes; registrar localizador; fonte ausente é declarada.
- Apagar ou mexer em tags de compartilhado tomando-o por retirado. → Conferir `plan["compartilhados"]` antes.
- Dizer que funciona sem ter visto. → Declarar o que falta Davi testar.
- Mexer na corrida de outro executor. → §1.
- Livro/PDF/dumps perto do commit. → Commitar só código, docs, specs e revisões.

## 14. Outras frentes (preservar; não iniciar sem pedido)

Cadernos (`banco/CLAUDE.md`, `ROLES.md`), Typst (`typst-template/CLAUDE.md`), E1 (`didatica/E1.md`), site NEBLI, Liga Clínica, Etimologia (deck de Davi: nunca apagar nem esconder). Backlog antigo e decisões não revogadas dessas frentes: MEMORY arquivado em `arquivo/2026-10-08-organizacao/MEMORY.md`, § Pendências abertas. Calibração das 100 perguntas: `flashcards/projeto/CALIBRACAO-DECK-100-PERGUNTAS.md` (evidência, não leitura obrigatória).
