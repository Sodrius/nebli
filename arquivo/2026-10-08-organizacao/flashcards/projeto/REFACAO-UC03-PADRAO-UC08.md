# Refação UC03 no padrão UC08

Data: 04/10/2026  
Escopo: refazer a qualidade dos decks UC03 já produzidos e usar o mesmo método nos próximos decks.

## Diagnóstico que orienta a mudança

Os decks UC08 não ficaram melhores por terem apenas mais cards. Eles partiram de um mapa atômico da aula: cada figura, rótulo, relação causal e bloco teórico recebeu card, conjunto de cards ou exclusão justificada. O mapa foi comparado ao deck já instalado.

| Corrida | Slides / recorte | Itens de cobertura | Cards | Sinais de qualidade |
| --- | --- | ---: | ---: | --- |
| UC08 AN01 | 21 slides de conteúdo | 114 | 123 | 112 cards com imagem e extras específicos |
| UC08 BT03 | 44 slides de conteúdo | 89 | 121 | 108 cards com imagem e 32 referências de slides |
| UC08 FI05 | 12 slides | 116 | 95 | modelo granular, extras específicos |
| UC03 Edema | slides 2–15 | 19 | 41 | 1 card com imagem |
| UC03 Patologia ambiental | slides 20–47 | 36 | 41 | 0 imagens e 27 extras genéricos repetidos |
| UC03 Morfologia bacteriana | 45 páginas | 33 | 36 | 2 cards com imagem |

O problema foi método de seleção, não um total de cards. A cobertura atual de UC03 registra tópicos amplos, permitindo que vários elementos ensinados por uma lâmina fiquem sem destino. O gate aceitou esse registro porque só confere se há itens mapeados, não se todo o conteúdo da aula foi inventariado.

## Resultado exigido para cada aula

Um deck está pronto somente quando uma pessoa que não viu o tema consegue estudar a aula inteira pelos cards, na ordem da aula, sem conteúdo externo deslocado. Isso exige:

1. Todo slide é classificado como capa, logística, conteúdo, revisão ou fora do recorte. Uma classificação sem conteúdo traz justificativa.
2. Todo elemento ensinável de slide de conteúdo, exercício e capítulo tem um identificador atômico e um destino: card instalado, card complementar instalado ou exclusão com justificativa pedagógica e fonte.
3. Cada card externo explica por que pertence àquela aula, no campo Extra, com contexto específico. Texto-modelo repetido não vale como adaptação.
4. Estruturas, morfologias, lesões, trajetos e mecanismos que dependem de reconhecimento visual usam imagem quando ela ajuda a responder. A ausência é justificada por o conceito ser estritamente verbal.
5. A revisão compara o inventário ao Anki já instalado, não somente aos arquivos de planejamento.

Não há teto de cards. As cores vêm depois da cobertura: verde mantém a rotina de 40 novos/dia; azul completa o necessário para a prova; rosa fica restrito a complementos realmente úteis. O teto de autorais continua valendo, mas nunca autoriza omitir conteúdo: a busca externa continua até esgotar os acervos e o autoral cobre apenas lacuna importante.

## Artefatos obrigatórios da corrida

Todos ficam em `arquivos-trabalho/<corrida>/` antes da escrita no Anki.

| Artefato | Momento | Conteúdo mínimo |
| --- | --- | --- |
| `fontes.json` | busca | fonte, localização, busca feita e ausência declarada quando aplicável |
| `leitura-fontes.md` | leitura | lâminas, prova, exercício, CAOC, capítulo e vídeo; localizador e o que cada fonte acrescenta |
| `inventario-aula.json` | antes da seleção | todas as páginas, itens atômicos por página, exercícios e pontos do capítulo que a aula ensina |
| `busca/ext.txt` | curadoria | consultas e resultados reais em AnKing e demais acervos |
| `planejamento.json` | seleção | cada alvo vinculado ao id do inventário, origem e decisão de cor |
| `cobertura.json` | após instalar | cada id atômico ligado à chave de card instalada; exclusões justificadas |
| `revisao-inventario.json` | revisão final | veredicto item a item contra o Anki, card visto e correção feita |
| `qualidade.md` | fechamento | amostra concreta de frente, verso, Extra, imagem e pendência verdadeira |

### Esquema do inventário

Cada página aparece mesmo sem alvo. Uma página de conteúdo tem pelo menos um item.

```json
{
  "lido_antes_da_selecao": true,
  "slides": [
    {
      "numero": 14,
      "classe": "conteudo",
      "itens": [
        {
          "id": "s14-parede-gram-negativa-lps",
          "alvo": "Relacionar LPS da membrana externa à estrutura da parede Gram-negativa",
          "habilidade": "explicar",
          "fontes": ["slide 14", "Trabulsi cap. ..."],
          "visual": "nao-necessaria"
        }
      ]
    }
  ],
  "exercicios": [],
  "capitulo": []
}
```

`cobertura.json` deixa de aceitar apenas uma frase ampla. Cada `id` acima precisa listar chaves de cards instalados. Se o item for excluído, informa a lâmina, o motivo e por que não é uma repetição ou conteúdo cobrado. Exclusão não é mecanismo para reduzir o deck.

## Fluxo para toda aula

### 0. Travar o critério antes da produção

Implementar no `nebli.gates` o validador do inventário e testar os casos de falha: página de conteúdo sem item, id sem cobertura, card inexistente, Extra genérico, e item visual sem imagem ou justificativa. O gate antigo continua rodando, mas não é mais suficiente para aprovar uma corrida nova.

### 1. Planejar com as fontes, na ordem definida

Ler todas as lâminas e construir o inventário sem olhar para os cards existentes. Depois cruzar prova antiga, exercícios e CAOC oficial; ler o trecho correspondente de Trabulsi/Robbins ou bibliografia indicada; por último, ler as transcrições dos canais indicados. Registrar localizador e contribuição de cada fonte em vez de declarar leitura global.

O capítulo aprofunda apenas o que a aula ensina. Prova, exercício, CAOC e vídeo calibram ênfase, linguagem e armadilhas; não criam bloco externo ao objetivo da aula.

### 2. Selecionar cards em cima do inventário

Para cada item, procurar primeiro AnKing, depois os demais acervos definidos no projeto. O resultado procurado, escolhido e recusado fica em `busca/ext.txt`. Um card copiado recebe um Extra que cita o elemento da aula que ele resolve, por exemplo a relação, a estrutura ou a armadilha daquela lâmina; nenhuma frase genérica repetida é aceita.

Quando uma figura faz parte do que se aprende, procurar a imagem no slide ou em fonte permitida e vinculá-la ao card. Um card sem imagem só é escolhido quando a imagem não melhora reconhecimento ou raciocínio.

### 3. Executar como alteração preservadora

Antes de alterar deck já existente, registrar ids de notas, estado de estudo, flags, suspensões e edições pessoais. A refação acrescenta ou melhora conteúdo sem apagar esse histórico. Quando um card antigo precisar ser substituído e não puder manter a mesma nota, ele recebe marca de substituído e é suspenso apenas se for duplicata exata e isso não apagar uma decisão pessoal do estudante.

Escrever com `nebli.decks.escrita()` e `arquivos-trabalho/ANKI-ESCRITA.lock`. Criar Tabs para 100% dos cards, do básico ao avançado, com 150–220 palavras e exemplos da própria aula. Conferir a ordem `NEBLI::ordem::<curto>-<NN>` após a escrita.

### 4. Revisar o que está instalado

Fazer a revisão em duas passagens.

1. **Inventário:** abrir cada item do `inventario-aula.json`, localizar seu card instalado e registrar em `revisao-inventario.json` a chave, o que ele cobra e a correção aplicada. Nenhum item de conteúdo fica sem veredicto.
2. **Experiência de estudo:** abrir uma amostra distribuída por começo, meio e fim da aula, mais todos os cards visuais e todos os autorais. Conferir frente, resposta, imagem, Extra, Tab, cor e ordem. A amostra é evidência adicional; não substitui a conferência item a item.

Na revisão, procurar ativamente: rótulos de diagramas sem card, comparação que virou fato isolado, mecanismo sem consequência, exceção de prova apagada, imagem decorativa e Extra intercambiável com outra aula.

### 5. Fechar e entregar

Rodar `python3 -m nebli.gates arquivos-trabalho/<corrida>` somente depois da revisão. A entrega ocorre apenas com aprovação: exportar `.apkg`, PDF de slides quando disponível, copiar com `python3 -m nebli.entrega`, conferir os arquivos no Drive e sincronizar AnkiWeb. O relatório informa quantitativos e pendências reais, sem chamar a corrida de completa se uma fonte ou revisão não ocorreu.

## Refação dos decks UC03 já afetados

| Ordem | Aula | Primeiro problema a eliminar | Critério de saída |
| ---: | --- | --- | --- |
| 1 | Edema e congestão | inventário de apenas 19 itens e uma imagem | mapa completo de lâminas, capítulo de edema/Robbins, prova, CAOC, exercícios e vídeos; imagem nos itens morfológicos ou estruturais necessários |
| 2 | Patologia ambiental | cobertura ampla demais, 27 Extras genéricos e nenhuma imagem | substituição de todos os Extras genéricos, mapa por agente/lesão/mecanismo da aula e imagens onde há reconhecimento histopatológico ou anatômico |
| 3 | Morfologia e estrutura das bactérias | 33 itens para 45 páginas e duas imagens | inventário de todas as páginas úteis, relações estrutura–função e figuras/rótulos cobrados |

Cada uma é uma corrida nova, auditável e entregue isoladamente. A primeira refação serve para validar o novo gate; as outras duas usam o mesmo esquema sem relaxar o inventário. Só então a produção segue para a próxima aula pendente de UC03.

## Indicadores que substituem a falsa segurança do gate anterior

- 100% das páginas classificadas; 100% dos slides de conteúdo com item atômico.
- 100% dos ids de conteúdo, exercício e capítulo no recorte com card instalado ou exclusão explicitamente revisada.
- Zero Extras em texto-modelo ou reutilizados sem relação específica com o alvo.
- 100% dos alvos de reconhecimento visual com imagem ou justificativa registrada e aprovada na revisão.
- Todos os cards autorais e imagens abertos na revisão final; Tabs e ordem em 100%.
- Gate, pacote, Drive e sync registrados somente quando realizados.

Estes indicadores medem a cobertura ensinável. Contagem de cards, proporção de origem e aprovação isolada de arquivos continuam úteis como alertas, mas não substituem a conferência do inventário contra o Anki.
