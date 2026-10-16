# Como classificar o que é importante (cores) — pesquisa de 16/10/2026

Pedido de Davi (F-20261016-CLAUDE-01): “não pode ser tudo verde… nem tudo é tão importante… pesquisa sites, pesquisas, repos e reddit… pensei numa base de dados com prova de residência”.

## O que achei

- **Tags HY do AnKing** ([AnkiHub: o que é a tag High Yield](https://community.ankihub.net/t/what-is-the-high-yield-tag-and-how-should-i-use-it/574770)): a equipe AnKing pontuou cada card de 1 a 5 com uma única pergunta, “quanto preciso deste card para responder questões de prática?” (Step 1). 1 = aparece repetidamente nas questões; 2 = útil, um degrau abaixo; 3 = temporário (apoia matéria posterior e depois pode ser suspenso); 4–5 = baixo retorno. A própria equipe avisa que LowYield não garante ausência em prova. **Conclusão:** HY mede rendimento em questão de Step 1, não o que a aula/prova da FMUSP cobra nem o que Davi precisa manter por anos. Usar “HY 1–2 = verde” (regra antiga do MEMORY) pintou 104 de 125 cards da 09 de verde.
- **Prática dos estudantes** (blogs e guias; Reddit sem fio aproveitável nesta busca): prioridade = retorno sobre o tempo (“produz pontos em muitas questões e muitos sistemas?”); desuspender por aula; deixar de lado o que não rende. Sem método formal publicado.
- **Literatura:** não há estudo que valide uma escala de importância de cards; os estudos com Anki em medicina medem volume e precocidade do uso (ex.: [Monash, farmacologia](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9063128/)). A literatura de “judgments of learning” mostra que alunos priorizam mal sozinhos — argumento para uma rubrica explícita.
- **Provas de residência:** há estatísticas por banca (ex.: [Estratégia, USP-SP](https://portal.estrategia.com/medicina/residencia-medica/usp-sp-temas-mais-recorrentes-na-prova-de-residencia-medica/); guias da Medway por estado, com cadastro). Elas mostram peso de grandes áreas clínicas (pediatria, preventiva, cirurgia); ciclo básico quase não aparece como tema próprio.

## Rubrica adotada (MEMORY §8; gate duro `cores_rubrica`)

Cada card recebe um código no início do `motivo`; a cor sai do código, não da tag HY.

| Código | Cor | Quando |
|---|---|---|
| V-pilar | verde | princípio ou mecanismo central da aula que as próximas UCs e a clínica reutilizam (está em `ESCOPO["centrais"]`) |
| V-prova | verde | central **e** cobrado em prova antiga da UC (índice de provas) ou HY 1 do recorte |
| A-aula | azul | ensinado na aula, importante para a prova, mas sem uso longo (detalhe que se apoia no princípio, exemplo-chave, imagem a reconhecer) |
| A-step | azul | HY 1–2 ligado à aula que não é pilar |
| R-detalhe | rosa | detalhe pertinente, HY 3–5, aprofundamento, sinônimo de outro card, exemplo |
| R-org | rosa | organizador de lista que só serve para reconhecer o conjunto (o pilar já tem card) |

Organizador é verde só quando a classificação é ela mesma o pilar (ex.: tipos de necrose); os demais azul ou rosa. Verde acima de ~50% dos cards reprova a corrida: sinal de que a rubrica não foi aplicada.

## Base de provas de residência — minha opinião

Vale, mas não agora como fonte principal do ciclo básico: residência pesa clínica e quase não pergunta ciclo básico isolado. Ordem sugerida: (1) já: provas antigas da UC (índice `referencias-externas/uc03`) + HY do AnKing como proxies de frequência; (2) quando entrar a clínica (UC21 em diante): base de residência (USP-SP, UNIFESP, SUS-SP, HIAE) com questões etiquetadas por tema — serve para pesar os cards clínicos e escolher quais cards de ciclo básico viram verde por reaparecer na clínica. Custo: coletar PDFs/gabaritos, extrair texto e etiquetar por tema (LLM + conferência); dá para começar com as estatísticas públicas por banca.
