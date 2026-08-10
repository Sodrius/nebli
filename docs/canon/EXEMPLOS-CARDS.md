# Exemplos canônicos de cards

Os exemplos abaixo definem forma; não são artefatos de uma aula.

## Cloze

**Preferido — uma palavra e uma recuperação**

`The esophagus is lined by {{c1::squamous}} epithelium.`

**Aceitável — duas palavras que formam uma unidade**

`The distal esophagus is supplied by the {{c1::left gastric}} artery.`

**Excepcional — três palavras**

`The lower sphincter is a {{c1::physiologic high-pressure zone}}.`

Só aceitar o terceiro caso quando dividir destruir a expressão médica e registrar
o motivo em `cloze_exception_reason`.

**Reprovados**

- esconder uma oração ou lista longa;
- usar `c1` e `c2` na mesma nota;
- duas ocorrências de cloze que cobram fatos lembráveis separadamente;
- frente que já contém a resposta por sigla, definição ou pista gramatical.

## Image Occlusion

**Bom mapa rotulado**

Para identificar partes de um órgão em um único esquema, recortar com contexto,
manter as estruturas visíveis e cobrir exatamente todos os rótulos-resposta. Usar
`hide_all_guess_all`, marcar `coherent_visual_map` e revisar dois previews:
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

Uma aula média com teto 40 pode terminar com 34 cards. Se a curadoria propõe 44,
não cortar conceitos nucleares ao acaso nem exportar 44: deduplicar, atomizar sem
fragmentar e revisar escopo. Se 44 continuar necessário, reabrir o contrato e
justificar o novo teto antes do APKG.
