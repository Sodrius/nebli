# Pesquisa para calibração NEBLI — 25/10/2026

Pesquisa dirigida, não revisão sistemática. Escopo: recuperação espaçada em medicina, transferência, estudantes de alto desempenho, práticas de Anki em Reddit/YouTube e implementação no GitHub. Sínteses abaixo distinguem resultados, experiências e inferências para o projeto. Consultas iniciadas em 24/10 e encerradas em 25/10.

## Estudos primários

1. [Larsen, Butler e Roediger, 2009](https://pubmed.ncbi.nlm.nih.gov/19930508/), ensaio randomizado com residentes de pediatria/emergência. Resumo consultado no resultado indexado; abertura direta posterior limitada. Recuperação repetida após ensino apresentou 39% versus 26% no teste após mais de seis meses, diferença de 13 pontos percentuais. Sustenta testar recuperação ao longo do tempo; não determina formato cloze, negrito ou superioridade do Anki.

2. [Butler, 2010](https://andymatuschak.org/files/papers/Butler%20-%202010%20-%20Repeated%20Testing%20Produces%20Superior%20Transfer%20of%20Learning%20Relative%20to%20Repeated.pdf), quatro experimentos, texto do artigo acessível. Após uma semana, testes repetidos superaram releitura em retenção e perguntas inferenciais novas. Não é ensaio clínico nem validação de qualquer deck. Inferência para NEBLI: incluir avaliação com perguntas novas que preservem o conceito, separada de acertar a frase habitual.

3. [Mehta et al., 2023](https://pubmed.ncbi.nlm.nih.gov/37886276/), estudo retrospectivo com logs de Anki e desempenho em três provas. Grupo de maior desempenho começou antes e estudou mais cards ao longo do período. Resumo e discussão/limitações consultados. Associação não estabelece causalidade; diferenças prévias e outras estratégias confundem resultados. Não justifica aumentar automaticamente o volume ou prometer aprendizagem permanente.

4. [Understanding Excellence, 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8368812/), estudo qualitativo de estudantes com desempenho superior a 90% numa avaliação nacional padronizada. Trechos indexados consultados; página direta devolveu verificação de navegador. Recuperação ativa e repetição espaçada são estratégias frequentemente relatadas. Autorreporte e seleção dos bem-sucedidos impedem atribuir sucesso a uma ferramenta. Aqui “elite acadêmica” é operacionalizada como alto desempenho observado, não prestígio institucional.

5. [Self-regulated learning among high performing medical students, 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8178823/), estudo qualitativo. Trechos indexados consultados; abertura direta bloqueada por verificação. Planejamento, monitoramento e ajuste das estratégias aparecem nos relatos. Inferência: retorno de erros deve mudar a produção e ser verificado nas entregas posteriores, não somente registrado.

## Síntese localizada, ainda sem avaliação integral

[Revisão sobre repetição espaçada/recuperação em graduandos de medicina, 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13657408/): resumo/conclusões indexados relatam 21 estudos, heterogeneidade e vieses importantes, especialmente em uso autodirigido de flashcards. Não usar como revisão integralmente lida nem como prova de benefício causal de uma configuração de Anki. Foi usada para localizar limites e estudos primários.

## Prática de alunos e comunidade

6. [UW Medicine, AOA Pearls 2023](https://education.uwmedicine.org/career-advising/wp-content/uploads/sites/4/2023/07/AOA-Pearls-2023.pdf): PDF acessível, consulta focal aos trechos sobre recursos/estudo. Guia de experiências e aconselhamento de alunos, não experimento. Anki e bancos de questões aparecem no repertório; não transformar uso por alunos selecionados em receita causal nem transplantar rotina Step para o ciclo básico de Davi.

7. [Reddit: aprender conteúdo ou reconhecer padrões?](https://www.reddit.com/r/medicalschoolanki/comments/18k8uza/): postagem e comentários consultados. Há preocupação com pistas lexicais e relatos de utilidade de perguntas de aplicação, mas opiniões divergem. Fonte de hipóteses/usabilidade; não evidencia que cloze seja ineficaz. Reconhecer rapidamente não é, sozinho, sinal de falsa aprendizagem. Testar capacidade de usar a relação fora da frase.

8. [Reddit: How to avoid pattern recognition?](https://www.reddit.com/r/medicalschoolanki/comments/1eptpc8/): trechos indexados. Relatos sugerem paráfrase e contextualização, com custo de tempo. Não implementar reformulação aleatória de cards nem respostas longas em toda revisão por causa dessas sugestões.

9. [YouTube: Anki — Making Effective Cards, The AnKing, 2018](https://www.youtube.com/watch?v=b1NIQeFYQFQ): título, data e descrição consultados por busca. Abertura direta falhou; vídeo/transcrição NÃO assistidos/lidos integralmente. A descrição trata de lembrança, eficiência e refinamento dos cards com uso. Serve como referência prática a aprofundar, não como evidência de uma regra detalhada de negrito. [Página oficial do minicurso](https://www.theanking.com/free-course) localizada; conteúdo do curso não acessado.

## GitHub: implementação, não eficácia pedagógica

10. [AnKing-VIP/AnKing-Note-Types](https://github.com/AnKing-VIP/AnKing-Note-Types): README/estrutura consultados, além do [JSON do modelo](https://github.com/AnKing-VIP/AnKing-Note-Types/blob/master/Note%20Types/AnKing/AnKing.json). Campos Text, Extra, Personal Notes, Missed Questions e One by one permitem distinguir funções do conteúdo. Template não define se uma pergunta é boa. Inferência: manter compatibilidade e separar estilo de validação semântica; não copiar configuração como se fosse estudo de aprendizagem.

11. [FSRS — The Optimal Retention](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-optimal-retention): documentação consultada. Expõe relação entre retenção desejada, esquecimento e carga de revisão. A grandeza modelada depende da probabilidade de recordar cards; não mede por si só entendimento/transferência. Não alterar preset nem propor porcentagem universal nesta etapa.

## Implicações propostas para discutir

- Preservar recuperação espaçada; avaliar separadamente lembrança do alvo, reconstrução do processo e aplicação a uma pergunta diferente.
- Planejar a partir das capacidades da aula; usar acervos para atendê-las.
- Não inferir aprendizagem a longo prazo de uma revisão imediata bem-sucedida. Piloto precisa de retorno após uso; prazo/forma a definir depois das respostas.
- A posição exata do negrito, comprimento máximo e dica ideal não foram estabelecidos pelos estudos consultados. São hipóteses de design a calibrar com exemplos e resultados.
- Separar falha objetiva (mídia ausente, resposta vazada, etapas faltantes) de julgamento semântico; uma regex causal e um texto de 30 caracteres não certificam mecanismo ou qualidade.
- Não existe respaldo aqui para apagar clozes, aumentar volume indiscriminadamente, exigir raciocínio extenso em cada revisão ou mudar o algoritmo antes de resolver conteúdo.

## Sete problemas → evidência a exigir no plano posterior

| Problema | Evidência proposta |
|---|---|
| Aula mal compreendida | Cada capacidade ligada a recuperação concreta, com teste de reconstrução |
| Gates declaratórios | Regressões reais reprovadas; revisão substantiva com trechos de suporte |
| Autoria superficial | Comparações aprovadas de alvo/contexto/Extra e caso-limite |
| Regras contraditórias | MEMORY, roteiro, molde e código coerentes; versões antigas arquivadas |
| Feedback pouco aproveitado | Antes/depois/literal/aceite separados e família checada na próxima entrega |
| Profundidade e continuidade | Cards isoladamente compreensíveis e conjunto reconstruível; Tab com ganho próprio |
| Imagens inadequadas | Figura conferida junto da pergunta, em tamanho legível, sem vazamento |

Estas são propostas de critérios, não mudanças já aplicadas ao pipeline.
