# Exemplos canônicos de cards

Os exemplos abaixo definem forma; não são artefatos de uma aula.

## Cloze

**Preferido — uma palavra e uma recuperação**

`O esôfago é revestido por epitélio {{c1::escamoso}}.`

**Aceitável — duas palavras que formam uma unidade**

`O esôfago distal recebe irrigação da artéria {{c1::gástrica esquerda}}.`

**Excepcional — três palavras**

`O esfíncter inferior corresponde a uma {{c1::zona fisiológica hipertensiva}}.`

Só aceitar o terceiro caso quando dividir destruir a expressão médica e registrar
o motivo em `cloze_exception_reason`.

**Reprovados**

- esconder uma oração ou lista longa;
- usar `c1` e `c2` na mesma nota;
- duas ocorrências de cloze que cobram fatos lembráveis separadamente;
- frente que já contém a resposta por sigla, definição ou pista gramatical.

**Anti-indução — preferido**

`A fixação imediata preserva a arquitetura ao impedir a {{c1::autólise}}.`

**Anti-indução — reprovado**

`A fixação impede a autólise e preserva a {{c1::arquitetura}}.`

O segundo branco admite “morfologia”, “estrutura” e outras respostas e ainda
oculta o termo mais previsível, não o mecanismo que merece retenção.

## Image Occlusion

**Bom mapa rotulado**

Para identificar partes de um órgão em um único esquema, recortar com contexto,
manter as estruturas visíveis e cobrir exatamente todos os rótulos-resposta. Usar
`hide_two_guess_two`, ocultar no máximo dois rótulos coerentes, justificar o par e revisar dois previews:
pergunta (todos os rótulos ocultos) e resposta (rótulos revelados).

**IO reprovado**

- a máscara cobre a estrutura anatômica em vez do texto que a nomeia;
- um rótulo duplicado continua visível em outra parte da imagem;
- o crop remove os marcos necessários para orientação;
- micrografia sem rótulos é coberta por um retângulo opaco, apagando a pista;
- o manifesto diz “approved”, mas não há preview de pergunta e resposta.

Em imagem não rotulada, adicionar marcador e prompt visual; não chamar de IO uma
caixa que simplesmente esconde o tecido.

## Volume

Uma aula média com teto 20 pode terminar com 16 cards. Se a curadoria propõe 24,
não cortar conceitos nucleares ao acaso: deduplicar, procurar relações geradoras
e revisar o escopo. Se o excesso continuar necessário, dividir a aula ou
justificar explicitamente a exceção antes do manifesto.
