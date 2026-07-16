# NEBLI Etimologia — plano de implementação

> Status: fundação iniciada em 2026-07-15. Este projeto é um **bootcamp finito de linguagem médica**, separado do deck longitudinal por UC/prova.

## 1. Resultado pretendido

Ao concluir o bootcamp, o estudante deve conseguir:

1. reconhecer prefixos, raízes/formas combinantes e sufixos produtivos;
2. decompor um termo médico novo e propor uma glosa literal plausível;
3. distinguir a glosa literal do significado médico vigente;
4. relacionar formas em inglês, português e, quando relevante, latim anatômico;
5. reconhecer quando a palavra é opaca, híbrida, eponímica ou perigosa para inferência;
6. usar o vocabulário com menor latência ao ler, ouvir e produzir linguagem médica.

O alvo não é aprender grego ou latim clássicos completos. História e etimologia profunda entram apenas quando ajudam a memorizar, discriminar ou compreender.

## 2. Ciclo de vida

- **Tipo:** curso intensivo com começo e fim.
- **Duração planejada:** 10–12 semanas, 6 dias por semana.
- **Ritmo inicial:** 8 novos/dia; faixa permitida de 7–10.
- **Teto de conteúdo:** 500–600 cards aprovados; 600 é limite, não meta.
- **Revisões:** sem teto artificial; pausar novos se a carga ultrapassar 20–25 minutos por 3 dias.
- **Fim:** após os gates de formatura, suspender/arquivar o deck principal.
- **Retenção:** teste frio após 30 dias. Reabrir somente `10_Resgate` se necessário.

Este bootcamp terá preset próprio. Seu ritmo não deve alterar o limite longitudinal de UC/prova.

## 3. Arquitetura

A fonte canônica da árvore é `deck_structure.json`:

1. `01_Fundamentos` — gramática mínima de formação das palavras;
2. `02_Prefixos` — operadores transversais;
3. `03_Sufixos` — processos, estados, exames e procedimentos;
4. `04_Raizes_por_sistema` — formas combinantes anatômicas e funcionais;
5. `05_Processos_medicos` — vocabulário transversal das disciplinas;
6. `06_Familias_e_contrastes` — redução de interferência;
7. `07_Excecoes_e_armadilhas` — quando não inferir;
8. `08_Transferencia` — aplicar elementos conhecidos a termos novos;
9. `09_Avaliacoes` — diagnóstico, checkpoints e provas finais;
10. `10_Resgate` — único bloco potencialmente reaberto após a formatura.

## 4. Orçamento de conteúdo

| Bloco | Cards-alvo | Conteúdo |
|---|---:|---|
| Fundamentos | 20–25 | estrutura, vogal de ligação, transliteração, assimilação, plurais |
| Prefixos | 40–50 | forma produtiva em termo real, não lista nua |
| Sufixos | 50–60 | condição, patologia, exame, cirurgia, especialidade |
| Raízes + aplicações por sistema | 230–270 | cerca de 80 raízes e 150–190 decomposições |
| Processos médicos | 45–60 | patologia, micro, fármaco, laboratório, imagem e clínica |
| Famílias e contrastes | 35–45 | pares grego–latim, falsos equivalentes e procedimentos |
| Exceções e armadilhas | 25–35 | polissemia, epônimo, sigla, híbrido e falsa segmentação |
| Transferência no Anki | 15–25 | treino guiado; itens realmente inéditos ficam fora do SRS |
| **Total** | **460–570** | teto absoluto de 600 |

Exemplos embutidos no verso não contam como cards. Uma nota de morfema mostra 2–4 integrantes da família sem gerar automaticamente irmãos para todos eles.

## 5. Sequência semanal

### Semanas 1–2 — gramática e operadores

- diagnóstico inicial sem estudo;
- prefixo, raiz, sufixo, forma combinante e vogal de ligação;
- 30–40 afixos de maior produtividade;
- grego × latim, transliteração, assimilação e variantes;
- primeiro checkpoint com termos nunca apresentados.

### Semanas 3–8 — famílias por sistemas

- ordenar os sistemas conforme o currículo atual do primeiro ano;
- em cada sistema: raízes nucleares → famílias → termos reais → contraste;
- misturar 20–30% de revisão intersistemas;
- introduzir PT-BR/EN e latim anatômico somente quando houver uso real.

### Semanas 9–10 — processos e linguagem clínica

- patologia geral, microbiologia, imunologia e farmacologia;
- laboratório, imagem, exame físico e procedimentos;
- terminações de fármacos apenas como pistas de classe, nunca como prova de mecanismo ou indicação.

### Semanas 11–12 — transferência e formatura

- nenhum morfema novo na última semana;
- termos inéditos decomponíveis;
- termos não decomponíveis e armadilhas;
- contexto clínico curto;
- provas finais A e B separadas por 7 dias.

## 6. Formatos de card

Todos os cards continuam no `AnKingOverhaul`, com um único `{{c1::...}}`, frente curta em inglês médico natural e Extra em português. O dado rico vive no JSON versionado; Text/Extra são sua projeção no Anki.

### A. Morfema em contexto — padrão

```text
In pericarditis, peri- means {{c1::around}}.
```

Extra: forma, origem, 2–4 termos da família, tradução e limite.

### B. Decomposição de termo

```text
Splenomegaly literally describes {{c1::enlargement of the spleen}}.
```

Extra: `splen-` + `-megaly`, termo PT-BR e significado clínico.

### C. Contraste

```text
A surgically created opening is an {{c1::-ostomy}}, not an -otomy or -ectomy.
```

### D. Exceção/armadilha

```text
Despite -oma, a hematoma is a {{c1::localized collection of blood}}, not a neoplasm.
```

### E. Produção reversa — seletiva

Somente quando nomear ativamente for útil e a resposta for inequívoca. Não criar espelho automático morfema↔significado.

## 7. Contrato obrigatório do verso

Cada card aprovado separa, quando aplicável:

1. **Parts:** segmentação sincrônica útil;
2. **Literal:** glosa composicional;
3. **Clinical:** significado médico atual;
4. **Limit:** onde a inferência falha ou precisa ser confirmada;
5. **PT-BR:** forma natural usada na medicina brasileira;
6. **Family/contrast:** exemplos ou discriminador.

Etimologia histórica não substitui definição médica. Curiosidade histórica sem ganho cognitivo é cortada.

## 8. Seleção de conteúdo

Um morfema entra se alcançar pelo menos 3 pontos:

- +2 aparece em três ou mais termos relevantes do primeiro ano;
- +2 é transversal a mais de um sistema;
- +1 reduz uma confusão frequente;
- +1 aproxima PT-BR e inglês médico;
- +1 ajuda a decodificar termo novo;
- −2 é raro, historicamente interessante, mas pouco produtivo;
- −2 induz conclusão clínica insegura sem grande valor como armadilha.

Termos reais vêm prioritariamente das aulas, resumos E1, questões E2 e cards já aprovados. Fontes abertas completam famílias, mas não governam o escopo sozinhas.

## 9. Fontes e licenças

Ordem de trabalho:

1. OpenRN *Medical Terminology 2e* (CC BY 4.0) para estrutura e fatos básicos;
2. outro OER CC BY de terminologia para triangulação;
3. FIPAT/Terminologia Anatomica para termos anatômicos oficiais individuais;
4. fonte médica atual para o significado clínico;
5. fonte etimológica independente para casos complexos.

Regras:

- texto pedagógico autoral, sem copiar verbetes ou decks comerciais;
- registrar fontes, licença e data de revisão;
- duas fontes para etimologia contestável, híbrida ou semanticamente desviada;
- QA linguístico e QA médico separados;
- AnkiWeb é benchmark, não licença de reutilização.

## 10. QA e publicação

Estados: `draft → linguistic_review → medical_review → approved → retired`.

Gates automáticos:

- exatamente um `c1`;
- resposta curta e inequívoca;
- sem pista que entregue o cloze;
- fontes etimológica e médica presentes;
- deck declarado no manifesto;
- glosa literal não apresentada como definição clínica sem confirmação;
- exceção para afixos polissêmicos de alto risco;
- deduplicação por UID, texto normalizado e família.

Gates humanos:

- a segmentação é linguística e pedagogicamente defensável?
- o termo PT-BR é o usado de verdade?
- o significado clínico está atualizado?
- o card ensina habilidade reutilizável?
- o Extra esclarece sem virar apostila?

## 11. Avaliação e formatura

Métricas separadas:

- retenção dos cards treinados;
- decodificação de termos inéditos compostos por morfemas treinados;
- compreensão dentro de frase clínica curta;
- reconhecimento de que não é seguro inferir;
- confiança e tempo de resposta.

Formatura exige:

- ≥85% nos termos/morfemas treinados;
- ≥75–80% em inéditos decomponíveis;
- ≤10% de respostas erradas com alta confiança nas armadilhas;
- resultados repetidos nas provas A e B, separadas por 7 dias;
- carga diária tolerável e sem prejuízo do currículo regular.

Depois: suspender o deck principal, manter snapshot e fazer `09_Avaliacoes::06_Retencao_30_dias`. Queda localizada cria módulo de 1–2 semanas em `10_Resgate`; não reativar tudo.

## 12. Entregas

### Fundação — hoje

- [x] manifesto da árvore;
- [x] script idempotente de criação/validação;
- [x] schema do conteúdo-fonte;
- [ ] árvore criada e validada no Anki;
- [ ] preset próprio — aplicar junto do primeiro lote.

### Lote zero — REDIGIDO e aplicado suspenso 2026-07-16 (ver STATUS-2026-07-16.md)

- [x] 20 cards de Fundamentos;
- [x] 20 cards de prefixos/sufixos nucleares;
- [x] 20 aplicações curriculares;
- [x] 15 questões inéditas fora do Anki (`assessments/lote-00-retido.json`);
- [x] lint (`validate_etymology.py`, 0 erros) + apply suspenso (`release_etymology.py`, 60/60);
- [ ] card-mirror + revisão linguística/médica independentes antes de liberar;
- [ ] piloto de 7 dias antes de congelar o template.

> Decisão de idioma (Davi 2026-07-16): **tudo em PT-BR** (frente e verso), substituindo "frente em inglês médico".

### Produção

- lotes de 40–60 cards, um sistema por lote;
- lint + revisão linguística + revisão médica;
- liberar somente após o lote anterior alcançar o checkpoint.

### Encerramento

- congelar versão do deck e fontes;
- provas finais A/B;
- suspensão em massa reversível;
- teste frio de 30 dias e resgate seletivo.
