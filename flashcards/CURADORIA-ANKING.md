# CURADORIA-ANKING.md — busca card a card

Objetivo: usar o AnKing como **primeira fonte de cards**, sem deixar a disponibilidade do deck decidir o currículo da aula.

## Entrada

1. E1 já redigida.
2. `arquivos-trabalho/checklist-<slug>.tsv` gerado por `gerar_checklist.py`.
3. Checklist revisada: `<EN?>` resolvidos, redundâncias fundidas e cada conceito classificado `nuclear | supporting | no_card`.

`no_card` não entra na busca. `supporting` só segue se houver motivo claro para recuperação ativa.

## Busca

1. `buscar_tags_lote.py checklist.tsv --md` encontra tags candidatas para os conceitos selecionados.
2. `extrair_cards_anking.py` + `prefiltrar_pool.py` reduzem o pool.
3. `curar_anking_v2.py ... --checklist checklist.tsv` pode rankear uma shortlist por conceito/subtópico.

O output do v2 é **pool de candidatos**. `ANCORADO`, hit textual, cloze único, Extra longo ou imagem são sinais úteis para ordenar leitura; nenhum deles aprova semanticamente o card.

## Keep/drop fino

Para cada conceito, ler a frente/cloze real e perguntar:

- o que exatamente este card força recuperar?
- isso é o mesmo retrieval target do conceito da E1?
- a resposta depende de conhecimento não apresentado?
- já existe um card melhor/igual no lote?
- o Extra explica sem introduzir uma segunda aula?
- se há imagem, ela é pertinente ao alvo ou só ao tema?

Manter o menor conjunto que cubra o conceito bem. Um card pode ser excelente e ainda assim ser `DROP — outra aula`.

## Gap analysis

Depois do AnKing:

- lacuna visual/anatômica/histológica → procurar primeiro nos decks de `referencias-externas/`;
- lacuna conceitual → procurar o deck externo apropriado se houver;
- só quando essas fontes forem ausentes/insuficientes → autoral.

Autoral é criado **na mesma corrida**, mas como último recurso e com as rejeições registradas. Não existe mais `PENDENTE-GERADO` como estado de entrega.

Se uma fonte preferida adequada aparecer depois para o mesmo retrieval target, substitui o autoral; não soma.

## Registro mínimo

O manifesto de curadoria deve conseguir responder para cada keep:

- concept id;
- card ref/GUID;
- fonte;
- retrieval target;
- motivo do keep;
- âncora E1;
- decisão visual quando aplicável.

Para cada autoral, deve conseguir provar que AnKing e outros decks foram tentados e por que os candidatos foram insuficientes.

## Volume

Não há alvo 30–50, quota por subtópico nem “top N” que precise ser preenchido. O volume emerge dos retrieval targets aprovados. Guardrails gerais: pequena ~15–25; média ~25–40; grande/densa ~35–55; acima de 60 exige revisão explícita de redundância.

## Apply e estudo

Cards aprovados recebem `NEBLI::<slug>` e são **copiados** para `NEBLI::<UC>::<Prova>::<Matéria>::<Aula>`, preservando as fontes. A lista do manifesto é autoritativa; uma tag sozinha não autoriza cópia.

`configurar_ritmo_anking.py` mantém o topo `NEBLI` em 25 novos/dia. Cram usa temporariamente o subdeck da prova, sem cards duplicados.
