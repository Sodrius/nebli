# Guia de imagens em cards NEBLI

Canonizado em 2026-07-14 a partir de debate com 5 agentes e pesquisa externa.

## Regra principal

Imagem nao e decoracao nem meta estetica. Imagem entra quando melhora uma destas
funcoes cognitivas:

- reconhecimento visual;
- relacao espacial/localizacao;
- mecanismo ou fluxo;
- comparacao entre entidades parecidas;
- padrao clinico/diagnostico;
- ancora mnemonica realmente util.

A metrica correta nao e "quantos cards tem imagem". A metrica correta e:
**a necessidade visual do card foi satisfeita?**

Regra dura de pertinencia: a imagem precisa servir ao **card especifico**. Uma
imagem do mesmo tema, sistema, aula ou slide nao conta como resolvida se nao
mostra, organiza ou compara exatamente o alvo cobrado. Imagem por tema recebe
`NEBLI::image_status::context_needs_specific_review` e deve ser substituida,
recortada, anotada ou removida.

Trocar "imagem por tema" por "imagem por intencao". A intencao da imagem deve
ser uma frase curta: identificar, localizar, comparar, demonstrar mecanismo,
reconhecer padrao ou fixar relacao espacial. Se a intencao nao e clara para o
card especifico, a imagem nao pertence ao card.

## Decisao por card

Todo card novo deve receber uma decisao visual:

```json
{
  "visual_need": "required|recommended|optional|none",
  "image_role": "recognition|localization|mechanism|comparison|schema|context|none",
  "visual_task": "o que a imagem treina ou que erro ela previne",
  "image": "image_key_or_null",
  "image_score": 0,
  "image_status": "approved|pending_review|context_only|needs_specific_review|needs_credit|missing|rejected"
}
```

Definicoes:

- `required`: sem imagem/IO o card fica incompleto. Padrao para anatomia,
  histologia, radiologia, dermatologia, ECG, patologia visual e exame fisico
  quando o objetivo e reconhecer algo.
- `recommended`: imagem melhora muito a compreensao ou retencao, mas o card
  ainda pode existir sem ela.
- `optional`: imagem pode ajudar, mas nao deve ser forçada.
- `none`: imagem nao agrega; nao colocar figura decorativa.

## Decisao por imagem

Toda imagem usada deve ter metadados:

```json
{
  "file": "...",
  "url": "...",
  "source_type": "local_figures|slide|external_deck|atlas|junqueira|web|manual|generated",
  "credit": "...",
  "license_status": "open_ok|noncommercial_ok|private_only|unknown_reject|internal",
  "license_note": "...",
  "retrieved_at": "YYYY-MM-DD",
  "modifications": "crop, arrows, contrast, etc.",
  "hash": "..."
}
```

Separar sempre qualidade pedagogica de direitos:

- `image_score` mede qualidade visual/didatica.
- `license_status` mede se pode usar/redistribuir.
- Imagem privada pode servir ao estudo local, mas deve ficar marcada
  `private_only` e bloqueada para exportacao publica.

## Score 0-3

- `3`: excelente; diretamente ligada ao card, clara, especifica, reutilizavel
  como imagem canonica.
- `2`: boa; agrega ao card e resolve a necessidade visual.
- `1`: fraca/contextual; pode entrar provisoriamente com revisao marcada.
- `0`: nao usar; decorativa, errada, ilegivel, generica demais, sem fonte
  aceitavel ou entrega o cloze.

`visual_need=required` exige `image_score >= 2` ou IO aprovado.

## Quando usar IO

Use Image Occlusion quando a resposta depende de localizar ou reconhecer algo na
imagem:

- estrutura anatomica;
- camada/celula/tecido em histologia;
- orgao/vaso/nervo/musculo em peca ou atlas;
- estrutura em corte axial/coronal/sagital;
- achado radiologico, dermatologico, ECG ou patologico visual.

Estruturas dentro de cortes histologicos sao sempre candidatas fortes a IO. Se
o card cobra uma camada, celula, corpusculo, glandula, vaso, foliculo, zona ou
padrao em lamina, buscar ativamente IO/micrografia especifica em `tag:H::*`,
`"magnified image"`, `tag:#FDN1_Block::Histology_Practical` e
`tag:@Medical_School::Histology::*`. Se nao existir card externo bom, criar IO
manual com `io_manual_from_image.py`.

Micrografia ampla sem marcacao so e suficiente quando a pergunta e reconhecer o
tecido/orgao/padrao global. Se o card cobra estrutura menor (ducto, celula,
camada, corpusculo, vaso, foliculo, tubulo), a imagem precisa de seta, recorte,
zoom ou IO sobre o alvo.

Use cloze normal com imagem no `Extra` quando a pergunta e conceitual/verbal e a
imagem serve para explicar, organizar ou consolidar.

Para estruturas importantes, fazer par:

1. card visual/IO para reconhecer;
2. cloze conceitual para funcao, origem, relacao, inervacao, drenagem, clinica.

## Posicionamento da imagem

- Imagem no front: quando ela e o estimulo da pergunta.
- Imagem no back/Extra: quando ela explica, compara ou consolida.
- IO: quando o card testa identificacao visual.

Nao colocar no front uma imagem que revele o cloze por texto, rotulo, titulo ou
OCR.

## Hierarquia de fontes

1. Imagens locais ja curadas em `figuras/<slug>/`.
2. Slides da aula, quando uso for pessoal/local.
3. Decks externos importados e ja mapeados: BlueLink, Dope, Histology, LLU,
   Dorian/100 Concepts.
4. Acervo local/livros/atlas para uso privado, com `private_only`.
5. Fontes abertas na internet com licenca verificavel.
6. Fallback: `NEBLI::needs_image` ou `image_status=missing`; nao preencher com
   imagem generica.

Para web, abrir a pagina original da imagem. Google Images nao e fonte.

Fontes abertas uteis:

- Wikimedia Commons: verificar a licenca arquivo por arquivo.
- OpenStax Anatomy & Physiology: esquemas didaticos; verificar licenca da versao.
- Servier Medical Art: ilustracoes medicas em CC BY 4.0.
- CDC PHIL: microbiologia, parasitologia, saude publica; checar cada item.
- NCI Visuals Online / Cancer.gov: oncologia, patologia e imagens institucionais.
- Wellcome Collection: imagens biomedicas/historicas; checar licenca.
- Radiopaedia: radiologia, geralmente nao comercial; usar com atribuicao e
  apenas quando compatível com o uso.

## Bloqueios

Bloquear publicacao/aplicacao como aprovado se houver:

- `img::errada`;
- `img::entrega_cloze`;
- `img::ilegivel`;
- `img::fonte_revisar` em deck redistribuivel;
- `image_score=0`;
- paciente identificavel sem permissao clara;
- watermark invasiva;
- estrutura ou achado nao visivel.

Pode entrar como pendente/revisao:

- `image_score=1`;
- imagem de contexto;
- fonte privada/local;
- imagem boa mas sem crop/legenda adequada.

## Tags canonicas

Usar poucas tags acionaveis:

- `NEBLI::image_extra`
- `NEBLI::needs_image`
- `NEBLI::image_context_needs_specific_review`
- `NEBLI::image_status::<approved|pending_review|context_only|needs_specific_review|needs_credit|missing|rejected>`
- `NEBLI::image_source::<slide|external_deck|web|atlas|junqueira|manual|generated>`
- `img::ok`
- `img::ausente`
- `img::revisar`
- `img::substituir`
- `img::errada`
- `img::generica`
- `img::ilegivel`
- `img::sem_contexto`
- `img::entrega_cloze`
- `img::fonte_revisar`

Tags sao para acao humana. Metadados detalhados ficam no manifesto/staging, nao
em uma explosao de tags.

## Metricas

Relatorio por deck/aula:

- cobertura de `visual_need=required`;
- cobertura de `visual_need=recommended`;
- media de `image_score`;
- porcentagem de imagens com fonte/licenca verificavel;
- numero de `img::errada`, `img::entrega_cloze`, `img::ilegivel`;
- numero de cards visuais obrigatorios sem imagem;
- numero de imagens `context_only`.

Comparacao com decks prontos (amostra 2026-07-14):

- BlueLink/Dope ensinam anatomia visual com IO especifico; NEBLI deve copiar
  esse padrao para estrutura/localizacao, nao usar imagem geral no Extra.
- Histology/LLU trazem micrografias e cards praticos; usar como fonte primaria
  para estruturas em cortes, mas evitar despejar muitas imagens no Extra sem
  foco no alvo.
- AnKing usa imagem forte quando ha dermatologia, comparacao, mecanismo visual
  ou esquema util, e aceita card sem imagem quando o conceito e textual.
- Dorian/100 Concepts e util para correlatos clinico-anatomicos com imagem.
- NEBLI pode reutilizar uma imagem em cards diferentes quando ela agrega a cada
  alvo. O defeito mecanicamente bloqueado e a mesma imagem aparecer duas vezes
  na mesma face renderizada. Reuso intercard so deve ser revisto quando a figura
  for generica ou nao cumprir a tarefa visual daquele card.

Metas iniciais:

- anatomia/histologia visual: 90-100% dos `required` resolvidos;
- radiologia/dermato/patologia visual/ECG: 85-100%;
- fisiologia/farmaco/bioquimica: imagem quando houver mecanismo, esquema,
  comparacao ou mapa realmente util, sem forcar cobertura global.

## Internet: regra pratica

Pode usar imagem da internet quando:

1. a imagem melhora o card;
2. a fonte original foi aberta;
3. autor/instituicao, URL, licenca e data foram salvos;
4. a licenca permite o uso pretendido ou o card esta marcado `private_only`;
5. a imagem nao e generica, errada, ilegivel nem redundante.

Se a licenca nao fica clara rapidamente, nao usar em deck publicavel. Usar como
referencia para recriar esquema proprio ou procurar alternativa aberta.

## Referencias externas usadas

- Mayer/Multimedia Learning: coerencia, sinalizacao e contiguidade espacial
  orientam evitar imagem decorativa e aproximar texto relevante da figura.
- Anki Manual: Anki 23.10+ tem Image Occlusion nativo; midias ficam na pasta
  de media da colecao e sincronizam como arquivos do Anki.
- Creative Commons: atribuicao exige autor/fonte/licenca e indicacao de mudancas.
- Servier Medical Art: biblioteca medica em CC BY 4.0.
- OpenStax Anatomy & Physiology: esquemas de A&P com licenca aberta/NC conforme
  versao, exigindo atribuicao.

## Pipeline operacional por aula (refinado no mutirao de 2026-07-15)

O processo visual tem dois trilhos. Eles nao sao intercambiaveis.

### Trilho A — Image Occlusion

Usar quando a propria imagem e a pista e o aluno precisa reconhecer, localizar
ou comparar uma estrutura. Fluxo obrigatorio:

1. escrever `visual_task` antes de buscar a figura;
2. escolher imagem-mae anatomica/histologica que mostre o alvo com resolucao;
3. definir apenas alvos nucleares ancorados na E1 (`target_count` explicito);
4. criar mascaras justas e conferir todas as repeticoes do mesmo rotulo;
5. renderizar preview no tamanho real do Anki;
6. procurar vazamento por rotulo, painel lateral, titulo, OCR, crop e gabarito;
7. conferir cada alvo no preview, nao apenas a nota como um todo;
8. registrar fonte, credito, licenca, hash e modificacoes;
9. aprovar somente com `image_score >= 2` e `answer_leakage=false`.

IO com muitos rotulos nao e automaticamente melhor. Comecar com 2–4 alvos
nucleares por placa; acima disso, justificar papeis distintos ou dividir por
subtopico. Um rotulo repetido que permanece visivel reprova a nota inteira.

### Trilho B — imagem explicativa no Extra

Usar quando a frente e textual, mas uma figura ajuda a compreender mecanismo,
comparar entidades ou consolidar uma relacao. Fluxo obrigatorio:

1. escrever qual erro ou relacao a imagem explica;
2. buscar a menor figura que resolve essa tarefa;
3. recortar/assinalar o alvo quando a figura ampla exigir procura visual;
4. colocar no `Extra`, nunca como pista frontal que entregue o cloze;
5. verificar legibilidade no celular e remover texto editorial irrelevante;
6. registrar os mesmos metadados de fonte/licenca do IO;
7. remover a imagem se ela apenas repete o tema da aula.

Uma figura geral do sistema nervoso nao explica microglia, transporte axonal,
no de Ranvier e meninges ao mesmo tempo. Reuso amplo entre alvos diferentes e
sinal de imagem contextual, nao de eficiencia.

### Manifesto e gate mecanico

Cada card visual deve entrar no manifesto consumido por:

```powershell
python flashcards/scripts/validar_manifesto_visual.py caminho/do/manifesto.json
```

Campos minimos: `note_id`, `visual_need`, `image_role`, `visual_task`,
`card_mode`, `image_status`, `image_score`, `answer_leakage`, `preview_path` e
`asset` com arquivo, localizador da fonte, credito, licenca, data, hash e
modificacoes. IO acrescenta `target_count` e `all_duplicate_labels_masked`.

O validador falha fechado quando um `required` nao esta aprovado, quando falta
preview/credito/licenca, quando ha vazamento ou quando `context` tenta resolver
necessidade obrigatoria. A classificacao continua humana: o script impede
declaracoes incompletas, mas nao substitui a revisao visual card a card.

### Erros de processo detectados em 2026-07-15

- classificar toda Anatomia/Histologia como `required` por slug;
- contar imagem presente como imagem pertinente;
- distribuir uma figura tematica por dezenas de cards;
- aprovar correspondencia por overlap lexical sem abrir a imagem;
- gerar IO por OCR sem verificar rotulos repetidos, truncamento e crop;
- usar credito generico do deck sem URL/autor/licenca;
- considerar comentario administrativamente resolvido como requisito editorial
  atendido.

Protecao permanente: taxonomia por operacao cognitiva, manifesto por card,
preview real, dupla revisao para `required` e validador antes de aplicar.
