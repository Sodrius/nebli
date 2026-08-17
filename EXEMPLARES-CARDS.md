# EXEMPLARES-CARDS.md — exemplos canônicos

Este arquivo exemplifica `FLASHCARDS.md`. Exemplos não criam regras novas.

Ao surgir feedback recorrente, adicionar aqui o contraste entre comportamento aprovado e reprovado e, quando possível, criar regressão executável.

## 1. Seleção: pré-requisito versus ganho da aula

### Reprovado — recapitular conteúdo anterior

Contexto curricular:

- aula anterior: Potencial de ação;
- aula atual: Sinapse.

A aula atual diz que a chegada do potencial de ação ao terminal pré-sináptico abre canais de Ca²⁺.

Card ruim:

`A fase ascendente do potencial de ação depende da entrada de {{c1::Na+}}.`

**Por que reprova:** o potencial de ação é pré-requisito. A aula atual o usa; não está ensinando novamente a fase ascendente.

Classificação: `pre_requisito` → sem card.

### Aprovado — relação nova envolvendo conhecimento prévio

`No terminal pré-sináptico, a chegada do potencial de ação abre canais de {{c1::Ca²⁺}} dependentes de voltagem.`

**Por que passa:** o ganho desta aula é a relação potencial de ação → abertura de canais de Ca²⁺ → liberação vesicular.

Classificação: `relacao_nova`.

## 2. Seleção: termo mencionado versus conceito ensinado

Slide sobre diferenciação de Tfh menciona CD4, MHC II, TCR e BCL6.

### Reprovado

`Linfócitos T CD4 reconhecem antígenos apresentados por {{c1::MHC II}}.`

**Problema:** CD4/MHC II é usado como base. A aula não está construindo esse conhecimento.

### Aprovado

`A diferenciação de Tfh depende do fator de transcrição {{c1::BCL6}}.`

**Por que passa:** BCL6 é desenvolvido como mecanismo específico do novo fenótipo estudado.

## 3. Seleção: exemplo versus regra

A aula usa deficiência de uma enzima apenas como exemplo de uma regra metabólica.

### Reprovado

Criar card perguntando um detalhe incidental do caso clínico que não é retomado nem explicado.

Classificação: `exemplo`.

### Aprovado

Criar card sobre a regra metabólica que o exemplo foi usado para demonstrar.

Classificação: `foco_novo` ou `relacao_nova`.

## 4. Relação nova entre peças antigas

O aluno já conhece insulina, PI3K/Akt e GLUT4. A aula atual ensina a cadeia funcional.

### Reprovados

`A insulina é secretada pelas células {{c1::beta}}.`

`GLUT4 é um transportador de {{c1::glicose}}.`

Ambos revisam peças.

### Aprovado

`No músculo e tecido adiposo, a sinalização por insulina promove a translocação de {{c1::GLUT4}} para a membrana.`

O retrieval target é a relação nova construída nesta aula.

## 5. E1 autocontida não significa deck inchado

A E1 pode explicar rapidamente o que é MHC para que um aluno sem base acompanhe uma aula de coestimulação.

Isso **não autoriza** card definindo MHC.

Aprovado: E1 explica o pré-requisito; `release_gate.concepts` o marca como `pre_requisito`, `retention_class=e1_only`, `card_keys=[]`.

## 6. Step 1 dentro do mesmo ganho

A aula introduz receptor X e explica seu mecanismo proximal.

### Aprovado

Adicionar à E1 e eventualmente ao deck uma etapa molecular diretamente necessária para reconstruir a sinalização de X.

### Reprovado

Aproveitar que o receptor aparece em rim e adicionar uma nefropatia high-yield que exigiria outra árvore de pré-requisitos.

## 7. Cloze — uma recuperação

### Preferido

`A fixação imediata preserva a arquitetura ao impedir a {{c1::autólise}}.`

A resposta é específica e o mecanismo determina o termo.

### Reprovado — indução

`A fixação impede a autólise e preserva a {{c1::arquitetura}}.`

“Morfologia”, “estrutura” e outras palavras cabem. O cloze esconde o resultado genérico, não o mecanismo relevante.

## 8. Cloze — tamanho

### Preferido — uma palavra

`A principal imunoglobulina de mucosa é a {{c1::IgA}}.`

### Aceitável — duas palavras como unidade

`O esôfago distal recebe irrigação da artéria {{c1::gástrica esquerda}}.`

Usar duas palavras somente quando dividir a unidade pioraria a recuperação.

### Excepcional — três palavras

`O esfíncter inferior corresponde a uma {{c1::zona fisiológica hipertensiva}}.`

Exige justificativa explícita no contrato.

### Reprovado

Esconder frase, explicação, oração inteira ou lista.

## 9. Um c1 não garante atomicidade

### Reprovado

`A ativação produz {{c1::proliferação, diferenciação e secreção de citocinas}}.`

Há várias recuperações escondidas sob uma única marca.

### Melhor

Escolher o elo que realmente constitui o ganho da aula ou decompor apenas se cada saída merecer recuperação própria.

## 10. Resposta não pode ser dada pelo Extra

### Reprovado

Frente vaga: `A alteração descrita provoca {{c1::anergia}}.`

Extra: “Isso ocorre quando há sinal 1 sem coestimulação CD28.”

O discriminador foi colocado depois da resposta.

### Aprovado

`O reconhecimento antigênico sem coestimulação adequada favorece {{c1::anergia}} do linfócito T.`

## 11. Par canônico

### Reprovado

`A recombinação depende de RAG1 e {{c1::RAG2}}.`

Se a meta é reter o par, metade da resposta já está impressa.

### Aprovado

Reformular para cobrar uma função discriminante de RAG1/RAG2 ou, se o nome composto for realmente a unidade recuperável, tratar a unidade inteira de forma justificada.

## 12. Duplicação funcional

### Reprovado

Card A e Card B recuperam a mesma resposta e o mesmo mecanismo com frases diferentes.

Trocar palavras não cria novo slot de retenção.

### Aprovado

Duas perguntas podem compartilhar um termo-resposta apenas quando recuperam relações realmente distintas e isso está justificado.

## 13. Image Occlusion

### Aprovado

Mapa anatômico rotulado. O crop mantém marcos espaciais. Uma ou duas etiquetas semanticamente relacionadas são cobertas. A pergunta oculta os rótulos; a resposta mostra a imagem original.

### Reprovados

- cobrir a própria estrutura anatômica em vez do rótulo;
- deixar a resposta visível em título ou legenda;
- usar praticamente o slide inteiro sem recorte;
- agrupar dois rótulos sem relação apenas para alcançar duas máscaras;
- colocar as respostas em texto logo abaixo da imagem;
- criar IO de uma micrografia não rotulada cobrindo a pista morfológica.

## 14. Volume

Uma aula média pode ter teto 20 e terminar com 13 ou 16 cards.

### Reprovado

Adicionar cards de revisão, definições antigas ou detalhes incidentais para aproximar o número de uma meta.

### Aprovado

Parar quando todos os slots de ganho real estão cobertos. O orçamento é teto, não quota.

## 15. Exemplo de matriz de ganho

```json
{
  "concept_id": "sinapse-ca",
  "learning_role": "relacao_nova",
  "lesson_gain": "A chegada do potencial de ação abre canais de Ca2+ no terminal pré-sináptico e inicia a exocitose.",
  "curriculum_ref": "aula-sinapse",
  "teaching_evidence": [
    {
      "source": "e1",
      "locator": "Seção 2.1 — Acoplamento excitação-secreção",
      "rationale": "A E1 desenvolve nesta aula a cadeia causal entre despolarização, Ca2+ e exocitose."
    }
  ],
  "retention_class": "must_recall",
  "card_keys": ["sinapse-ca-01"]
}
```

Contrastando:

```json
{
  "concept_id": "potencial-acao-basico",
  "learning_role": "pre_requisito",
  "curriculum_ref": "aula-potencial-acao",
  "teaching_evidence": [
    {
      "source": "master_sheet",
      "locator": "Aula anterior — Potencial de ação",
      "rationale": "O tema já ocupa uma aula curricular própria e aqui é somente pressuposto para explicar sinapse."
    }
  ],
  "retention_class": "e1_only",
  "exclusion_reason": "É conhecimento de suporte; a aula atual não o desenvolve como objetivo novo.",
  "card_keys": []
}
```
