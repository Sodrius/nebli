# Plano operacional: aula, cards e Tabs — 14/10/2026

Preferências: MEMORY §§2, 6 e 9. Este documento é um procedimento e uma proposta de implantação, não evidência de que os decks existentes já foram revistos.

## Resultado desejado

Depois de assistir à aula e percorrer cards + Tabs, Davi consegue explicar o núcleo, nomear estruturas/achados importantes, reconstruir os conjuntos que organizam o assunto e relacionar os detalhes ao mecanismo. O aprofundamento vem principalmente de explicar por que, como, em quais condições e com quais consequências. Alguns detalhes clínicos ilustram essas relações; não se converte a aula básica em revisão de condutas.

Completude é do conjunto: cada card continua pequeno e focal, e cada Tab continua do tamanho do caminho necessário, sem virar capítulo. Este plano refina a forma atual dos decks; não justifica reescrever o que já funciona nem aumentar decks de modo indiscriminado (F-20261014-CLAUDE-02).

Cards também cobram parte do aprofundamento extra, inclusive detalhe básico relevante que só complete o conhecimento do assunto, sem aplicação imediata nem cobrança em prova (MEMORY §2). O filtro é pertinência, importância e custo de revisão; curiosidades isoladas, enumerações sem propósito e temas com aula própria ficam no Tab ou saem. O que ficar em dúvida vai para a seção **Casos de fronteira** do `percurso-aula.md` (item · fonte · decisão adotada · motivo) e entra no relato, para Davi calibrar a profundidade.

Quatro funções legítimas de card: entender um mecanismo, recuperar um nome, reconstruir uma organização e recuperar parte do aprofundamento extra. Um card não precisa fazer todas. Um card de tríade pode ter ganho distinto de cards que explicam cada elemento. Registrar esse ganho evita tanto cortar sínteses úteis por aparente repetição quanto criar três cobranças equivalentes sem necessidade.

## Planejar antes de buscar cards

Criar `percurso-aula.md` na corrida com a tabela abaixo. Usar blocos conceituais, não uma linha por slide repetido. Seguir estritamente a ordem dos slides (confirmado por Davi). Não antecipar nem reagrupar blocos; explicar brevemente pré-requisitos no ponto de uso.

| Bloco e fontes (arquivo/página) | O que Davi deve explicar, nomear ou organizar | Chaves dos cards e função | O que o Tab acrescenta | Ponte ao bloco seguinte | Evidência após revisão |
|---|---|---|---|---|---|
| Fundamento | definição, propósito, problema | princípio | termos e relações necessários | por que surge a próxima questão | IDs/irmãos e texto conferidos |
| Desenvolvimento | mecanismo e suas condições | mecanismo/distinção | passos intermediários e consequências | relação com o próximo fenômeno | fonte do aprofundamento |
| Organização | conjunto curto e relevante | tríade/classificação/nomenclatura | significado e relação dos componentes | como o conjunto explica os casos | conferir cada irmão |
| Integração | aplicar o princípio | aplicação, se alvo real | exemplo clínico curto e limites | fechamento do tema | registrar o que ficou fora |

Para cada conteúdo da fonte, decidir: **recuperação em card**, **explicação em Tab** ou **exclusão com motivo**. Usar o inventário já existente como base; não manter duas listas de cobertura incompatíveis. Um objetivo central não pode ser considerado coberto só por menção no Tab. Um esclarecimento auxiliar pode ficar só no Tab, mas precisa ter card anfitrião e fonte identificados no percurso. Não produzir card artificial só para abrir um balão.

Separar, dentro de “O que o Tab acrescenta”: fundamento necessário, aprofundamento básico sustentado pelo livro e detalhe clínico ilustrativo, quando útil. Não estipular quota nem obrigar os três em todo texto. Sem fonte suficiente, registrar lacuna em vez de inventar profundidade.

## Exemplo de organização proposto por Davi

Modelo editorial, ainda não instalado. Conferir a terminologia na fonte da aula antes de substituir uma nota existente. “Cicatriz” é a pista de Davi; a explicação deve esclarecer o componente de reparo/fibrose conforme a fonte, sem ensinar que toda inflamação crônica já apresenta cicatriz madura.

```html
<div data-nebli-organizacao="true" data-nebli-pista="CID">
A tríade característica da <b>inflamação crônica</b> é constituída por:<br>
C {{c2::cicatriz}}<br>
I {{c1::infiltrado mononuclear}}<br>
D {{c2::destruição tissular}}
</div>
```

A sintaxe Anki precisa de `::`. Esta é **uma nota com dois cards**: c1 recupera infiltrado mononuclear; c2 recupera cicatriz + destruição juntas. O agrupamento respeita a proposta de Davi; na revisão pedagógica, conferir se recuperar os dois juntos é útil. Não trocar automaticamente por três notas ou por uma lacuna contendo a tríade inteira. Iniciais ajudam a evocação e não são consideradas vazamento acidental neste formato explicitamente solicitado. O Tab explica os significados e as relações; não se limita a repetir C/I/D. O português aqui preserva a pista; demais frentes continuam em inglês.

O marcador HTML `data-nebli-organizacao="true"` permite dois-pontos no lint; `data-nebli-pista="CID"` permite o português somente nesse formato declarado. As outras verificações permanecem. Os marcadores não certificam qualidade: revisar extensão, coerência do conjunto, pistas e ganho de recuperação.

## Produção e revisão viáveis hoje

1. Ler fontes e preencher o percurso junto com ESCOPO/inventário, antes da busca.
2. Buscar notas existentes por tarefa de memória; reutilizar e preservar IDs/histórico. Criar organização/nomenclatura quando faltar ganho próprio, sem quota.
3. Escrever/revisar Tabs por bloco com fontes e percurso à vista. O gerador atual recebe cada card, Extra e contexto limitado; **não recebe automaticamente o percurso nem o capítulo**. A saída automática é rascunho até o executor conferir o conjunto.
4. Ler todos os pares card+Tab na ordem: fundamentos antes dos detalhes, nenhum salto indispensável, nenhuma introdução inteira repetida a cada card, nomes conectados aos mecanismos, núcleo coberto e fontes do aprofundamento registradas.
5. Reler cada Tab isoladamente: continua compreensível em revisão aleatória? Irmãos focam o alvo oculto? Compartilhados continuam verdadeiros em todas as aulas? Não presumir que o usuário abriu o Tab anterior.
6. Registrar falhas concretas e correções no percurso e na revisão da corrida; só então executar gates/entrega habituais. Gates estruturais não atestam qualidade didática.

## Implantação por etapas

**Aplicado nesta sessão:** interação X/segundo X, leitura das desmarcações em `ruins`, regras de cards organizadores, exceção explícita no lint, prompt e roteiro do percurso. Não houve alteração de notas nem de Tabs já gerados.

**Piloto na 62 não iniciado: Davi informou que Claude já está trabalhando em outra sessão.** O executor deve integrar este plano ao trabalho autorizado naquela sessão, sem abrir revisão concorrente. Proposta de validação, a adaptar à aula já reivindicada: mapear a aula inteira nas fontes já reunidas; comparar cards existentes com mecanismos/nomes/conjuntos; integrar o exemplo C/I/D onde trouxer ganho; revisar todos os Tabs por blocos; registrar mudanças e exemplos de antes/depois. Preservar a nota em tela, comentários e histórico. Aceitar o piloto só após percorrer todos os blocos e conferir as capacidades da tabela, sem usar número de cards como prova de completude. Uma dúvida concreta de Davi ou uma marca X deve levar ao trecho e à relação que faltaram, não apenas a trocar palavras.

**Automação posterior, após calibrar o piloto:** definir um `percurso-aula.json` derivado da mesma fonte do inventário, com blocos ordenados, chaves de cards, papéis, fontes/trechos e conteúdo explicativo. O build resolve chaves para IDs; o gerador recebe bloco, pré-requisitos, fonte e contribuição de cada Tab. Hash do contexto invalida apenas textos afetados. Referência inexistente ou alvo central sem card reprova preflight. Para compartilhados, manter texto autônomo de contexto compatível; se precisar de narrativas diferentes por aula, será necessária mudança explícita do cache hoje indexado por card. Não prometer essa função antes de implementá-la.

**Expansão:** aplicar aos próximos decks e às revisões pedidas, após o piloto; sem regenerar toda a coleção. O tablet permanece pendente do leitor de Tabs e deverá ter comando equivalente para marcar/desmarcar. Não confundir mudança de prompt com implantação do contexto por aula.
