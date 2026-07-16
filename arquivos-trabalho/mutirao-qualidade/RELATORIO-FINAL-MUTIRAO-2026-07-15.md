# Relatório final — mutirão de qualidade dos decks Anki

Data: 2026-07-15  
Escopo real: árvore `NEBLI::*`, excluindo `NEBLI::STAGING::*` nas métricas finais.

## Resultado executivo

O mutirão terminou com o Anki sincronizado, backup antes/depois, piloto promovido e carga ativa abaixo do teto longitudinal. O estado é **seguro e calibrado**, mas não é chamado de `FINAL` para toda a P3: nove notas com necessidade visual obrigatória ainda não têm ativo aprovado e foram suspensas, e os manifestos antigos ainda não possuem notas de cobertura R6 (0–3).

| Métrica | Antes | Depois | Variação |
|---|---:|---:|---:|
| Notas | 247 | 256 | +9 |
| Cards totais | 468 | 477 | +9 |
| Cards ativos | 466 | 384 | -82 |
| Cards suspensos | 2 | 93 | +91 |
| Flags vermelhas | 25 | 25 | preservadas |
| Flags verdes | 2 | 2 | preservadas |
| `required` pendente ativo | n/a | 0 | gate fechado |

A queda de carga ativa é deliberada e reversível: 56 alvos periféricos de pranchas anatômicas, 11 cards visualmente bloqueados, originais substituídos e irmãos de cloze obsoletos foram suspensos, não apagados.

## Piloto padrão-ouro

Foram selecionadas 30 notas representativas, incluindo as 25 notas únicas com flag vermelha, controles verdes, card autoral, card AnKing, histologia, anatomia/IO, mecanismo e ponte longitudinal.

- 20 `rewrite`;
- 3 `replace_and_rewrite`;
- 3 `replace` por cards reais superiores;
- 1 `split` (meninges: duas recuperações atômicas);
- 1 `keep_with_credit_fix` (neurônio multipolar IO);
- 2 controles verdes mantidos.

O staging materializou 36 notas/39 cards. Gate textual final: 33 `PASS`, 3 `NOT_APPLICABLE` (IO/controle), 0 `REJECT`. A promoção preservou IDs/histórico autoral, criou 9 cópias com proveniência, suspendeu originais substituídos e registrou rollback.

### Amostras antes → depois

1. Idade materna: de uma explicação causal excessivamente simples (“represados no diplóteno”) para `Advanced maternal age increases the risk of meiotic {{c1::nondisjunction}}`, com coesão/fuso no Extra.
2. Zona pelúcida: de “ZP3 dispara” como regra única para `Binding to zona pellucida glycoproteins triggers sperm {{c1::acrosomal exocytosis}}`, explicitando a participação humana de ZP1/ZP3/ZP4.
3. Linfático: de `lacks tight junctions` para `discontinuous {{c1::button junctions}}`; a E1 editável também foi corrigida.
4. Meninges: de um card c1+c2 com imagem genérica para dois cards atômicos com diagrama específico de Gray no Extra.

## Imagens e Image Occlusion

### O que estava errado

- A taxonomia marcava toda nota de anatomia/histologia como `visual_need=required` apenas pelo slug.
- Imagens genéricas do mesmo tema eram repetidas em cards cujo alvo era outro.
- Dez pranchas Dope Anatomy geravam 87 perguntas, incluindo muitos rótulos periféricos.
- IO podia ser considerado pronto sem preview, crédito/licença, hash ou teste de vazamento.

### O que foi aplicado

- Separação formal de dois pipelines: `image_occlusion` (a imagem é a pergunta) e `explanatory_image`/`image_prompt` (a imagem explica ou serve de frente de reconhecimento).
- Manifesto visual com `visual_task`, papel, modo, placement, preview, leakage, fonte, crédito/licença, modificações e SHA-256.
- Gate automatizado que falha fechado para `required` sem aprovação, falta de preview/proveniência e vazamento.
- Três necessidades obrigatórias do piloto foram aprovadas: neurônio multipolar IO + duas micrografias de artéria elástica. Meninges recebeu imagem explicativa recomendada.
- As dez pranchas anatômicas foram inspecionadas semanticamente. Permaneceram 31 alvos nucleares (3 por prancha; 4 na circulação fetal); 56 foram suspensos.
- No deck completo há 11 notas `required+approved`. Nove notas/11 cards `required` ainda pendentes foram bloqueados e suspensos. Portanto, não existe `required` pendente ativo.

Não foi usada geração sintética para anatomia/histologia: quando o treino exige reconhecimento médico exato, foram preferidos diagramas/micrografias reais já existentes ou Commons com proveniência. Geração pode ser útil para esquemas causais, mas não deve substituir peça, lâmina ou atlas quando fidelidade visual é o alvo.

## Cobertura E1 e camada longitudinal

- Piloto: 30/30 decisões têm anchor de E1; as pontes de idade materna, zona pelúcida humana e junções em botão foram registradas.
- A E1 editável de vasos/linfáticos foi corrigida no fonte.
- Embriologia estava disponível apenas em PDF compilado; os patches exatos ficaram registrados para a próxima fonte editável.
- O verificador de cobertura agora exige nota R6 0–3 e importância por subtópico; manifesto legado sem nota não pode declarar fechamento. Subtópico nuclear em 0–1 falha o gate.
- O filtro AnKing agora separa cards `Step2-only`, mas preserva cards que também têm âncora Step1.

Limitação honesta: não existe ainda uma matriz R6 completa e atualizada para todos os 256 notes; portanto não se afirma “100% da E1 em 2–3” para a árvore inteira.

## Divergências resolvidas

- Cards reais AnKing/LLU foram preferidos quando superiores, mas duas cópias foram adaptadas para uma única recuperação atômica; os originais de referência ficaram intocados.
- O controle verde com c1/c2/c3 foi mantido como controle histórico e excluído do gate do lote; a regra nova continua proibindo múltiplos índices em card novo.
- Imagem privada de deck externo pode ser usada no estudo pessoal com marca `private_only`, mas não é tratada como redistribuível.
- Flags não foram apagadas: servem como trilha de feedback até 2–3 semanas de uso confirmarem a melhora.

## Aprendizados para a próxima curadoria

### 1. Escrever a tarefa visual antes de buscar imagem — confiança alta

- Erro: figura “do tema” usada para cumprir quota.
- Causa-raiz: busca começou pelo assunto, não pela ação cognitiva.
- Sinal: não se consegue completar “esta imagem permite ao aluno ___”.
- Correção: campo `visual_task` obrigatório + manifesto validado.
- Regra: procurar a imagem somente depois de decidir `recognition`, `localization`, `mechanism`, `comparison` ou `schema`.
- Impacto: `required` pendente ativo caiu a zero; o que ainda falta ficou suspenso.
- Próximo experimento: medir Again/tempo de cards com imagem específica versus os antigos contextuais.

### 2. IO é seleção semântica, não “um card por rótulo” — confiança alta

- Erro: 87 perguntas em dez pranchas.
- Causa-raiz: note type gerou todos os campos preenchidos sem dosagem curricular.
- Sinal: prancha com mais de quatro alvos iniciais ou rótulos que não têm anchor nuclear.
- Correção: inspeção do plate + lista explícita de targets.
- Regra: 2–4 alvos nucleares por prancha inicial; placas adicionais só quando cobrem outro cluster.
- Impacto medido: 87 → 31 alvos ativos; 56 suspensos; carga total ativa 451 → 395 naquele passo.
- Próximo experimento: comparar retenção e tempo por prancha após 2–3 semanas.

### 3. Disciplina não define necessidade visual — confiança alta

- Erro: todas as notas de anatomia/histologia viravam `required`.
- Causa-raiz: inferência pelo prefixo do slug.
- Sinal: mecanismo verbal sem tarefa visual marcado como bloqueante.
- Correção: `required` agora exige IO real, `visual_gate::required` ou candidato IO explícito; teste cobre regressão.
- Regra: classificar pelo cue do card, nunca pela disciplina.
- Impacto: taxonomia deixou de mascarar o backlog real e permitiu bloquear apenas nove notas concretas.

### 4. Um cloze lógico deve gerar uma recuperação — confiança alta

- Erro: múltiplos índices e mecanismo visível no stem aumentavam carga e adivinhabilidade.
- Causa-raiz: frases-resumo tratadas como cards.
- Sinal: `c1,c2,c3` ou mais de três spans ocultos.
- Correção: linter rejeita índices distintos; Nissl/TCR foram adaptados; meninges foi dividido.
- Regra: um índice `c1` por card; múltiplos spans só quando são uma única relação recuperada junto.
- Próximo experimento: monitorar se o controle verde multi-cloze realmente supera a versão atômica.

## Proteções permanentes

- `validar_manifesto_visual.py` + testes;
- `lint_neblicard.py` com gate de múltiplos índices + testes;
- auditor visual sem inferência por slug + teste;
- bloqueio automático de `required` pendente;
- dosagem IO com seleção explícita e rollback;
- R6 0–3 no template/verificador de cobertura;
- filtro `Step2-only` no pool AnKing.

## Verificação, backups e rollback

- Backup antes: `backups/NEBLI-mutirao-qualidade-2026-07-15-before.apkg`
- Backup depois: `backups/NEBLI-mutirao-qualidade-2026-07-15-after.apkg`
- Snapshot antes da promoção e script `rollback_piloto_mutirao.py`.
- Snapshot de dosagem IO e script `rollback_reducao_io_anatomia_p3.py`.
- Snapshot de bloqueio visual e script `rollback_bloqueio_required_visual.py`.
- Testes: 13 casos passaram; scripts críticos passaram em `py_compile`.
- Sync do Anki concluído depois da comparação antes/depois e criação dos rollbacks.

## Fontes externas usadas nas correções

- Idade materna/cohesina: https://pmc.ncbi.nlm.nih.gov/articles/PMC3491123/ e https://pubmed.ncbi.nlm.nih.gov/38134935/
- Zona pelúcida/acrossoma humana: https://pubmed.ncbi.nlm.nih.gov/18667750/ e https://pubmed.ncbi.nlm.nih.gov/9239670/
- Junções em botão: https://perspectivesinmedicine.cshlp.org/content/12/12/a041178.full.pdf
- Neurônio multipolar: https://commons.wikimedia.org/wiki/File:Blausen_0657_MultipolarNeuron.png
- Meninges/Gray 770: https://commons.wikimedia.org/wiki/File:Gray770-en.svg

## Adendo de fechamento do feedback — 2026-07-15

Este adendo substitui a decisão anterior de preservar flags. Por pedido do usuário, o novo padrão é: depois de analisar o comentário/bandeira/suspensão, corrigir e validar o card, arquivar o evento em ledger, limpar comentário e flag e devolver o card de estudo à fila. Originais substituídos e clozes tornados obsoletos continuam suspensos como arquivo estrutural.

- 18 ocorrências de imagem duplicada intranota foram removidas: 16 por `src` idêntica e duas por bytes idênticos com nomes diferentes. O pós-check final encontrou zero duplicatas intrafield. Reuso de uma imagem entre cards diferentes permanece permitido quando ela agrega.
- Os feedbacks textuais foram arquivados e os campos operacionais limpos. Estado final: zero comentários pendentes e zero flags na árvore NEBLI.
- O card de junções em botão foi corrigido e reativado. Os dois irmãos do controle verde que haviam sido suspensos por uma regra ampla de `ord > 0` foram restaurados; essa regra ampla foi rejeitada.
- Duas novas flags de linfonodo, criadas durante a execução, receberam diagrama/micrografia específicos, foram validadas e encerradas.
- O card de córtex/medula do timo foi substituído por duas notas atômicas de Image Occlusion, uma por alvo, usando crop revisado sem rótulo-resposta secundário visível.
- O staging de 36 notas/39 cards foi apagado após confirmação de que os 30 destinos-fonte e nove destinos criados estavam vivos e promovidos (39/39).
- Inventário final: 260 notas, 481 cards, zero flags, 98 suspensões estruturais/anteriores e zero `required` pendente ativo.
- Incidente operacional registrado: mutações AnkiConnect durante o Reviewer fizeram cards virados voltar à frente. Scripts mutáveis agora verificam `guiCurrentCard` e adiam a aplicação enquanto houver revisão ativa.

Artefatos finais:

- `final/INVENTARIO-final-pos-feedback-2026-07-15.json`
- `final/DEDUP-INTRAFIELD-FINAL-2026-07-15.json`
- `final/RECIBO-FECHAMENTO-FEEDBACK-STAGING-2026-07-15.json`
- `PESQUISA-IA-CARDS-MEDICOS-2026-07-15.md`
