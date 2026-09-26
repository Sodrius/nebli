# Relatório para revisão externa — sistema NEBLI de decks-aula (Anki)

Autor: Claude (Opus), executor do pipeline. Data: 23/09/2026. Escrito para outra IA avaliar de forma independente. Tudo aqui é opinião do executor, que tem interesse em parecer competente; por isso incluo os meus próprios erros e peço que você desconfie das partes em que eu elogio o sistema.

---

## 1. Contexto mínimo

- **Usuário:** Davi, estudante de Medicina na FMUSP, 1º ano, 2º semestre. Objetivo: aprender e lembrar o conteúdo da faculdade e construir, aos poucos, base para o USMLE Step 1, pensado para o fim do 4º ano. Rotina-alvo: ~50 min/dia de Anki (novos + revisões). Dispositivos: Mac (principal), Android e Windows (onde o Anki roda com AnkiConnect e onde eu opero).
- **Produto:** para cada aula, um **deck-aula** no Anki que cobre o que foi ensinado ou cobrado naquela aula, montado **AnKing-first**:
  1. cópias independentes dos cards do AnKing Step 1 v12, com os originais preservados;
  2. outros decks acessíveis quando fazem sentido (atlas de anatomia, histologia);
  3. cards autorais só como último recurso.
- **Entregas por aula:**
  - no Anki: o deck;
  - no Drive privado: um guia de estudo curto ("E1-GUIA"), um mapa de escopo e o APKG (por decisão de Davi em 23/09, o APKG agora fica só local).
- **Regras centrais** (documentadas pelo Davi em `flashcards/projeto/README.md`, `EXECUCAO-DECK-AULA.md`, `CALIBRACAO-DECK-AULA-V3.md`):
  - o material docente define **o que** entra; provas antigas calibram profundidade; livro e vídeo só esclarecem;
  - separar conteúdo ensinado de exemplo do professor; exemplo não vira card;
  - sem cota de cards; cada frente precisa justificar recuperação ativa ("economia de cards");
  - o verso conta como cobertura: não criar frente para o que o verso já ensina;
  - verso limpo: nada de clínica ou recurso lateral herdado do AnKing (limpar só na cópia);
  - bandeiras: **verde** = tag literal `1-HighYield` do AnKing; **vermelho** = feedback do Davi; nenhuma outra semântica;
  - nada de suspender card ruim: corrigir ou excluir (com backup); suspender só card bom que o Davi decidiu adiar;
  - frente e resposta em inglês; explicação em português quando útil;
  - **novas em 23/09:** autoral leva imagem por padrão (preferência: outro card AnKing > slide > internet livre); vídeos dos canais preferidos (Ninja Nerd, Medicosis Perfectionalis, Patologia Fácil, Dirty Medicine, Armando Hasudungan, Osmosis, Professor Dave, Shomu's Biology) vão junto do deck; APKG não sobe ao Drive por enquanto.

---

## 2. Estado dos decks (todos no perfil Windows; nenhum validado em Mac/Android)

| Aula | Notas / cards | AnKing | Outros decks | Autorais | Verdes | Status |
|---|---|---|---|---|---|---|
| Inflamação aguda (Patologia) | 46 / 68 | 65 | 1 Histology | 2 | 10 | Recalibrado após feedback; referência de "exclusão de excesso" |
| Vascularização das vísceras (Anatomia) | 47 / 88 | 43 | 42 Dope Anatomy, 2 Dorian | 1 | 37 | **Único aprovado explicitamente** pelo Davi |
| Intestinos (Histologia) | 37 / 41 | 20 | 4 LLU Histology | 17 | 6 | Aguarda feedback |
| Sistema complemento (Imunologia) | 43 / 56 | 35 | — | 21 | 4 | Aguarda feedback; **feito antes das regras de verso/imagem/vídeo, está desatualizado** |
| Genética bacteriana (Microbiologia) | 36 / 44 | 34 | — | 10 | 7 | Feedback parcial: faltava imagem nos autorais (corrigido); vídeos adicionados |
| Fisiologia bacteriana (Microbiologia) | 29 / 35 | 26 | — | 9 | 5 | Gerado hoje, já com as regras novas; aguarda feedback |

Total: ~332 cards em 6 aulas. A proporção autoral varia de 1% a 37%; volto a isso na seção 5.

---

## 3. Como uma aula é executada hoje (método real, não o ideal)

1. **Localizar o material** no Drive (pasta da aula), baixar os slides e a E1 NEBLI antiga, se houver. A data da aula vem da planilha, aba Mês.
2. **Ler os slides** em texto e **em imagem** (folhas de contato das páginas). Muitas páginas são só imagem.
3. **Ler as provas antigas** pertinentes (P2 2024 e 2025 da UC03) para calibrar.
4. **Mapa de escopo:** alvos ensinados, cobrados, pontes, exemplos, pré-requisitos, outra aula e fora do recorte.
5. **Pool AnKing:**
   - união das tags de recurso do tema (First Aid, B&B, Bootcamp, Sketchy…);
   - depois, varredura textual com termos específicos. Buscas curtas geram milhares de falsos positivos por substring de nome de mídia.
6. **Ler frente, verso e campos de recurso** de cada candidato. Selecionar com justificativa; registrar as recusas em `candidate-decisions.md`.
7. **Editar apenas as cópias:**
   - desfazer cloze irmão trivial;
   - aparar Extra lateral;
   - esvaziar campos de recurso de tema lateral;
   - completar o verso com 1 frase quando isso evita uma frente nova;
   - corrigir erro factual.
8. **Autorais** curtos em inglês, no modelo clonado do AnKing, com imagem.
9. **Plano imutável** (`plan.json`) → checagem de pré-condições → aplicação com journal e readback → exportação do APKG → verificação:
   - contagens;
   - deck correto;
   - bandeiras;
   - clozes renderizados;
   - mídia presente na coleção e no pacote;
   - origens inalteradas.
10. **Inspeção visual** de todas as imagens de verso (folha de contato), com correção do que estiver errado.
11. **Guia, mapa e registro de aprendizados;** publicação no Drive privado com readback.

Os scripts são **por aula** (copiados e adaptados da aula anterior). Não existe CLI genérica.

---

## 4. O que considero bom (com a ressalva do conflito de interesse)

- **Separar "o que entra" de "que profundidade"** (slide × prova antiga) é a decisão mais valiosa do sistema. Ela impediu, por exemplo, que Genética importasse mecanismos de resistência (outra aula) ou que Complemento virasse um bloco de HPN e angioedema.
- **Cópias independentes com origem intacta,** verificadas por hash a cada corrida. Até hoje nenhuma nota AnKing original foi alterada.
- **Inspeção visual obrigatória das imagens de verso.** Achou erro real em 3 aulas seguidas:
  - figura de transformação num card de Hfr;
  - promotor eucariótico num card de origem de replicação bacteriana;
  - algoritmo de identificação num card de MacConkey.
  Checagem por texto ou contagem não pegaria nenhum deles.
- **Leitura do verso do AnKing** achou um erro factual hoje: o card 1500497965459 diz "only aerobic bacteria perform cellular respiration", o que contradiz a respiração anaeróbia que a própria aula ensina. Foi corrigido na cópia.
- **Rastreabilidade:** cada corrida tem plan, receipt, journal, verification e candidate-decisions. Dá para auditar qualquer card até a origem e o motivo.
- **Regra "sem material docente, não roda":** Antibióticos e resistência tem pasta vazia, então não gerei deck, em vez de inventar o recorte.

---

## 5. O que considero fraco, arriscado ou mal resolvido

### 5.1 Qualidade do conteúdo

1. **A proporção autoral depende da matéria, não do esforço.** Onde a aula é mecanística básica e o AnKing é orientado a Step 1 clínico, falta pergunta: Complemento ficou com 37% autoral, Intestinos com 41%. Ninguém revisa os autorais além de mim, que os escrevi. **Risco:** erro factual meu entrar num deck sem segundo par de olhos. Hoje, por exemplo, afirmei "*M. tuberculosis* duplica em ~18–24 h", valor que veio do gabarito da prova (a literatura costuma dar 15–20 h). Não é errado para o objetivo, mas mostra que eu repito a fonte sem triangular.
2. **A limpeza de verso é subjetiva e feita por regex de tema.** Em cada aula escrevo uma lista `ON_TOPIC`/`LATERAL` diferente. É frágil: hoje ela removeu, por engano, um vídeo do próprio tema porque o título continha "Repair"; percebi e corrigi. Não há teste automatizado dessa regra.
3. **Os cards AnKing seguem o recorte do Step 1, não o da faculdade.** Exemplos:
   - "*E. coli* doubles in 20 min" não existe no AnKing, mas foi cobrado em prova;
   - o AnKing traz a nomenclatura nova (C4b2b) enquanto o slide usa a antiga (C4b2a);
   - clozes com dica binária ("Generalized or Specialized") são fáceis de chutar.
   Resolvo nota a nota, mas não há padrão sistemático.
4. **As tags AnKing aparecem no rodapé de cada card** (por exemplo `Streptococcus_pneumoniae` num card de hemólise). Não é conteúdo, mas polui visualmente e confunde a varredura de "clínica lateral". Ninguém decidiu ainda se isso importa.
5. **Idioma:** as frentes estão em inglês e as provas da FMUSP são em português, com terminologia às vezes diferente ("fase log" × "exponential phase"; "extremidades abruptas" × "blunt ends"). Não há evidência de que isso atrapalhe, mas também não foi testado.

### 5.2 Processo e engenharia

6. **Sem CLI genérica:** cada aula copia os scripts da anterior e os adapta. Deriva e bugs novos a cada cópia. Hoje cometi um: ao reaproveitar um crédito de foto, a regex capturou a tag `<img>` e duplicou a imagem no verso. O readback pegou, mas não era para acontecer.
7. **A "mesma pergunta em duas aulas" não tem boa UX.** No Complemento, associei por tag 2 cards que já existiam no deck de Inflamação. O card continua morando no deck da Inflamação; quem estudar pelo deck do Complemento não o vê. É fiel à regra (uma identidade, um histórico), mas talvez não ao que o Davi espera.
8. **Distribuição quebrada:** o APKG de 26 MB (Complemento) não coube em nenhum canal. Não há rclone instalado, a extensão do Chrome estava desconectada e o conector do Drive não sobe binário grande. Hoje o Davi suspendeu o upload. Sincronização Mac/Android: **nunca testada**. O deck só existe de fato no Windows até ele sincronizar.
9. **Decks antigos ficam defasados quando as regras mudam.** O Complemento não tem imagem nos autorais, não tem vídeos e mantém recursos laterais no verso. Não há rotina de "migrar decks para a regra nova".
10. **Carga de revisão não medida.** A regra fala em economia, mas não calculo o impacto de ~332 cards no orçamento de 50 min/dia nem a projeção das revisões. A economia é aplicada por julgamento, sem métrica.

### 5.3 Vídeos

11. **Cobertura fraca dos canais preferidos em microbiologia básica.**
    - Achei bons: Ninja Nerd *Bacterial Genetics*, com capítulos e links já no minuto certo; Shomu para Hfr, transposons e curva de crescimento; Medicosis para replicação; Professor Dave para CRISPR.
    - Não achei nada, nos canais listados, para meios de cultura, oxigênio, ferro, fermentação × respiração, mutação e enzimas de restrição.
    - Verifico **canal, título e capítulos**, nunca o conteúdo: não assisto aos vídeos. Um link pode estar certo no metadado e ser ruim no conteúdo.

### 5.4 Validação

12. **Só 1 dos 6 decks foi aprovado pelo usuário** (Vascularização). As regras evoluem por feedback esparso. Não há medição de retenção ou de desempenho em prova. É cedo, mas hoje o sistema otimiza o que **eu** acho boa curadoria.
13. **As provas antigas são poucas** (P2 2024 e 2025 da UC03, com gabarito comentado). Calibrar pela prova tem risco de sobreajuste a dois anos.

---

## 6. Recomendações, por prioridade

1. **Revisão cruzada dos autorais** por um segundo modelo ou pelo Davi, com checklist factual e fonte, antes de entrar no deck. É o maior risco de erro que eu não consigo ver sozinho.
2. **Migrar o deck do Complemento para as regras de 23/09** (imagens, vídeos, limpeza de verso) e criar uma rotina de "rebase" dos decks antigos sempre que uma regra canônica mudar.
3. **Extrair uma biblioteca comum** (uncloze, limpeza de recursos, edição de Extra, armazenamento de mídia, readback), com testes. Parar de copiar scripts entre aulas.
4. **Decidir com o Davi:**
   - (a) se as tags AnKing devem aparecer nas cópias;
   - (b) como cards compartilhados entre aulas devem aparecer em cada deck (filtro por tag, deck filtrado, ou mover);
   - (c) se os campos Sketchy/Bootcamp ficam mesmo quando são do tema, já que ele não lista esses recursos.
5. **Resolver distribuição e sincronização uma vez:** autorizar o rclone, ou usar o sync do AnkiWeb com um teste real no Mac/Android.
6. **Medir a carga:** projetar novos/dia e revisões para os ~332 cards contra os 50 min, antes de gerar as próximas aulas.
7. **Vídeos:** se os canais preferidos não cobrem microbiologia básica, perguntar ao Davi se aceita um canal "curinga" por tema, ou se prefere a lacuna declarada.

---

## 7. Perguntas para você (IA revisora)

- A regra "o verso conta como cobertura" está reduzindo demais a recuperação ativa? Exemplos: fator F, competência e Tn10 ficaram só no verso na Genética.
- 37% de autoral (Complemento) é sinal de escopo inflado, de AnKing inadequado para imunologia básica, ou de busca insuficiente minha?
- Frente em inglês para um aluno de 1º ano no Brasil: vale o custo pelo alinhamento com o Step 1, ou deveria ser bilíngue?
- A decisão de corrigir o AnKing na cópia (em vez de só marcar para revisão) é segura, dado que eu também posso errar?
- O que está faltando neste processo que você faria diferente?

---

## 8. Onde está tudo (repositório local do Davi)

- Regras: `flashcards/projeto/README.md`, `EXECUCAO-DECK-AULA.md`, `CALIBRACAO-DECK-AULA-V3.md`.
- Aprendizados por aula: `flashcards/projeto/APRENDIZADOS-*.md`.
- Corridas: `arquivos-trabalho/deck-aula-<aula>-2026-09-23/` (plan.json, receipt.json, journal.jsonl, verification.json, candidate-decisions.md, MAPA-ESCOPO.md, E1-GUIA.md, APKG).
