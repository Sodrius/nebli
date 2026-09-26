# Aprendizados — UC21 · Insuficiência metabólica (Caso 5, DM)

23/09/2026, executado pelo Claude (primeira aula ponta a ponta pelo Claude). Artefatos: `arquivos-trabalho/deck-aula-insuficiencia-metabolica-2026-09-23/`.

## Resultado

- Versão completa instalada: 477 notas / 575 cards (566 AnKing, 6 AnKing-MCAT, 3 autorais = 0,5%), 136 verdes, 269 rosas, 0 suspensos, em dois subdecks ("Roteiro do caso" 397 / "DM além do roteiro" 178). Verificação passou.
- Feedback de Davi: "gostei dele, mas ficou gigante" → pediu versão reduzida direcionada à UC21. Núcleo calculado: 179 notas / 224 cards (`reduction.json`).
- Depois da instalação, as notas UC21 foram apagadas da coleção (modelos e mídias ficaram). Não restaurei: aguarda decisão de Davi.
- E1 e guia publicados como Google Docs em `NEBLI pessoal/2026/UC21/Insuficiência metabólica/`. **Upload de APKG ao Drive abandonado por decisão de Davi (23/09, noite).**

## O que esta aula ensinou

1. **Aula de caso integrativo (DIC) ≠ aula expositiva.** O roteiro (objetivos, competências, perguntas) é o "slide". O relatório do grupo é fonte útil, mas tinha erros (DI em vez de diurese osmótica; hipercalemia mal explicada). A E1 deve corrigir o grupo explicitamente.
2. **"O mais completo possível" + "prova integrativa" geram deck gigante.** 575 cards para 14 dias ≈ 41/dia. Para UC de caso, o padrão deve ser **núcleo direcionado (~150–250) primeiro**. O DM completo fica como camada opcional (sugestão da próxima vez: já entregar em duas camadas e perguntar só se quer ativar a segunda).
3. **Marcar "o que é à parte" com subdeck físico funcionou para Davi** (pedido explícito), junto com tags `NEBLI::escopo::*`. Rosa continua só como sinal pós-prova.
4. **Critério de núcleo que funcionou:** roteiro sem rosa, menos duplicatas (mesma pergunta em 2–3 formulações), enzimologia de regulação (fosforilação de glicogênio-sintase/fosforilase, hexocinase × glicocinase em detalhe), definições triviais ("insulin is anabolic") e mnemônicos só de nome. Somar ao núcleo o mínimo de farmacologia/manejo ligado ao mecanismo (metformina, sulfonilureia, SGLT2i, GLP-1, insulinas rápida/longa, K⁺ na CAD).
5. **Busca por tags do First Aid + B&B + Pathoma cobre bem endócrino; busca textual traz muito ruído** ("MODY" casa trauma/hemodinâmica; "splay", "GAD", "Kussmaul sign"). Ler tudo que vier de texto antes de aceitar.
6. **AnKing não tem PKC/DAG, RAGE nem hexosamina em DM; o MCAT também não.** Foram os únicos autorais. O MCAT resolveu endócrina/parácrina/autócrina.
7. **Verificador de "meta visível" precisa ignorar `<script>` e o rodapé de tags do template AnKing.** Senão acusa as próprias tags NEBLI como visíveis (falso positivo corrigido em `verify.py`).
8. **Conector Drive do Claude:** cria pastas e Google Docs a partir de HTML (bom para E1/guia), mas não sobe binário grande por caminho local; o Chrome limita a 10 MB. Moot agora que o APKG não sobe mais.
9. **Imagens herdadas:** 2 trocas em 276 (acidez titulável num card de HCO₃⁻ normal; fluxograma de acromegalia). Folha de contato continua obrigatória.
10. `cardsInfo` não traz `reps` nesta versão; usar `type`/`queue` para checar se um card é novo.

## Para repetir

- Em UC de caso, entregar núcleo pequeno e perguntar sobre a camada completa. Não despejar 500+ novos a 2 semanas da prova.
- Ler o relatório do grupo e corrigir erros na E1.
- Publicar E1/guia como Google Doc; APKG só local (backup), sem upload.
