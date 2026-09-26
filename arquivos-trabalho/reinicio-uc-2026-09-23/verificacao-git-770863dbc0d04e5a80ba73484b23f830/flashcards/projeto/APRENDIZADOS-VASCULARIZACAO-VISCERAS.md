# Aprendizados — Vascularização das vísceras

Estado efetivamente entregue em 22/09/2026 e **aprovado explicitamente por Davi em 23/09/2026** (“gostei muito de como ficou”). Este é o exemplar preferido para anatomia/atlas. O arquivo registra o que foi feito, o que foi excluído e o que deve ser repetido nos próximos decks-aula.

## Resultado

- Deck no Anki: `NEBLI::UC08::Anatomia::Vascularização das vísceras`.
- 47 notas e 88 cards ativos.
- 43 cards AnKing, 42 cards provenientes do Dope Anatomy e 2 cards Dorian.
- Um card autoral curto, no modelo AnKing independente, sobre a origem da artéria retal média.
- 37 cards com bandeira verde, todos derivados de notas AnKing com a tag literal `#AK_Step1_v12::#Low/HighYield::1-HighYield`.
- Zero bandeiras vermelhas e zero cards suspensos na entrega.
- Originais, tags, campos e modelos-fonte preservados.
- Pacote exportado com agendamento e 87 arquivos de mídia; as 77 mídias referenciadas pelos cards foram encontradas no perfil vivo e no APKG.

O pacote e a E1 estão na pasta privada [07 - Vascularização das vísceras](https://drive.google.com/drive/folders/1AxHow4Bfn0Fv-EzWg3vOVozN8uktopgd). O APKG está em [Vascularização das vísceras.apkg](https://drive.google.com/file/d/1DlJxUSydxPhkOz9HNJ9gAQpvtbM7gRLR/view?usp=drivesdk).

## Fontes docentes usadas

Pasta docente: [07 - Vascularização das vísceras](https://drive.google.com/drive/folders/1anr09zp44SG100cQsQ-4jMVk6b0rcM2W).

- `Alunos - Irrigação visceral abdominal 2026.pdf` — slides principais.
- `Roteiro 2026 irrigação visceral Versão Final.pdf` — objetivos e recorte prático.
- `Irrigação Visceral Abdominal.docx.pdf` — questões orientadoras.
- Bibliografia indicada nos slides: D’Angelo/Fattini, Moore, Gray, Sobotta, Prometheus, Netter e anatomia clínica.

Não foi localizada prova antiga específica desta aula na pasta nem nas buscas realizadas no Drive. Portanto, prova antiga não foi alegada como evidência de cobertura ou prioridade.

## Recorte aplicado

Entraram os alvos ensinados/exigidos:

- tronco celíaco e árvore de ramos relevante;
- irrigação do estômago, pâncreas e duodeno;
- artéria mesentérica superior, ramos jejunoileais, arcadas e vasos retos;
- artéria mesentérica inferior e vascularização do intestino grosso;
- irrigação e drenagem venosa retal;
- formação e tributárias principais da veia porta;
- drenagem linfática regional pedida no roteiro;
- identificação visual dos vasos nas pranchas anatômicas.

Isquemia mesentérica, hemorroidas e volvo de sigmoide foram tratados como aplicações/exemplos do professor. Não se expandiu para fisiopatologia, diagnóstico, tratamento ou manejo dessas doenças. Também ficaram fora embriologia, inervação, anatomia abdominal geral e vasos sem relação direta com o roteiro.

## Por que o deck tem 88 cards

Anatomia exige duas camadas diferentes:

1. relações e árvores de ramos, bem atendidas pelo AnKing e por poucos clozes externos;
2. reconhecimento visual, que exige cards de atlas por estrutura apontada.

Os 42 cards contabilizados como Dope Anatomy incluem 37 cards de identificação em cinco pranchas e cinco clozes anatômicos. Eles não representam expansão de conteúdo: são outra forma de recuperar os mesmos alvos da aula. O volume maior decorre do componente visual, não de transformar cada frase dos slides em pergunta.

A auditoria final de cobertura acrescentou dois cards AnKing sobre drenagem linfática retal acima/abaixo da linha pectínea. A artéria retal média era conteúdo explícito do slide e não apareceu após buscas específicas no AnKing, Dope Anatomy e demais decks acessíveis; por isso recebeu o único card autoral, curto e no mesmo modelo visual do AnKing. Ele não recebeu bandeira verde.

## Correção técnica aprendida

O modelo `Anatomy` original possui uma condição especial no template 1: quando `2a` está preenchido, ele também pode gerar um card 1 mesmo com `1a` vazio. O primeiro lote de teste foi interrompido pela pós-condição de contagem, fotografado em JSON e excluído por completo; eram 40 notas/53 cards novos, todos com zero revisões.

Na cópia independente `NEBLI Anatomy independente - v1`, o template 1 foi corrigido para existir somente quando `1a` estiver preenchido. O modelo Dope original não foi alterado. Esta checagem deve virar parte permanente do pipeline: em modelos com templates condicionais, contar os cards realmente gerados antes de promover o deck.

## Regras confirmadas para as próximas aulas

- AnKing-first descreve a ordem de busca, não uma cota artificial. Em anatomia visual, um atlas/deck anatômico pode fornecer muitos cards sem contrariar a prioridade do AnKing.
- Antes de autorar, procurar no AnKing, em decks anatômicos/histológicos e em outros decks realmente acessíveis. Nesta aula, isso limitou a autoria a uma única lacuna explícita e comprovada.
- Uma prancha não deve gerar todos os seus rótulos automaticamente. Copiar a nota para um modelo independente e esvaziar os campos fora do recorte.
- Conteúdo útil no verso conta para aprendizagem. Não duplicar uma pergunta apenas para transformar toda informação acessória em frente.
- Casos do professor calibram o uso da anatomia, mas não autorizam importar um bloco de doença.
- Bandeira verde continua restrita ao HY explícito do AnKing. Ausência de verde não significa baixa importância para a faculdade.
- Nenhum comentário de “faculdade”, “núcleo”, “prova” ou “reserva” deve ser impresso no card.
- Card ruim não deve ser suspenso; deve ser corrigido ou excluído. Suspensão fica para card bom que o usuário não quer estudar agora.

## Evidências locais

- Plano: `arquivos-trabalho/vascularizacao-visceras-2026-09-22/plan.json`.
- Recibo inicial: `arquivos-trabalho/vascularizacao-visceras-2026-09-22/receipt.json`.
- Recibo final: `arquivos-trabalho/vascularizacao-visceras-2026-09-22/receipt-v2.json`.
- Verificação final: `arquivos-trabalho/vascularizacao-visceras-2026-09-22/verification-v2.json`.
- E1: `arquivos-trabalho/vascularizacao-visceras-2026-09-22/E1-GUIA.md`.
- Mapa de escopo: `arquivos-trabalho/vascularizacao-visceras-2026-09-22/MAPA-ESCOPO.md`.

Limite ainda aberto: a sincronização com AnkiWeb e o comportamento no Mac/Android não foram testados deste Windows. O deck vivo no perfil Windows e o APKG foram verificados; abrir/sincronizar no dispositivo principal continua sendo uma validação do usuário.
