# Ritmo e modos de estudo — NEBLI

> Ajuste de 2026-07-14 após auditoria do repositório, leitura do Anki local, pesquisa oficial e discussão de cinco agentes. Este guia não muda a coleção sozinho.

## Objetivo em três camadas

1. **Faculdade define o escopo.** O card nasce da aula/E1 e ajuda nas provas teóricas ou práticas.
2. **Step 1 regula a profundidade do mesmo mecanismo.** Acrescenta fisiopatologia, integração, dados e reconhecimento macro/microscópico quando naturais; não puxa manejo de Step 2.
3. **Residência HC orienta transferência, não volume.** Desde o ciclo básico, poucos ganchos conectam mecanismo a apresentação, anatomia, lâmina, diagnóstico ou discriminador. Questões complexas ficam no banco; erro recorrente pode justificar reparar um card.

O Anki retém e discrimina; E1 ensina; questões treinam aplicação.

## Modo longitudinal

- Estudar o topo `NEBLI`, misturando matérias, com FSRS.
- `15 novos/dia` é teto, não obrigação. Com backlog ou tempo alto, reduzir novos; revisões vencidas vêm primeiro.
- Teto de revisões alto (`9999`) para não esconder cards devidos. O Anki local estava em `15/9999` nesta auditoria.
- Desired retention inicial `0,90`; não subir por ansiedade nem reschedule em massa. Alterar uma variável e observar 2–3 semanas.
- Poucos learning/relearning steps, todos intradia; ponto de partida simples: `10m`.
- `Again` = falha de recall. `Hard` = lembrou corretamente com esforço; nunca substitui Again.

## Modo prova

Não usar `150 novos hoje` como padrão: isso transforma exposição em aprendizado agendado e cria uma onda de revisões.

```powershell
python flashcards/scripts/planejar_modo_prova.py --deck "NEBLI::UC02::P3"
```

- Devidos e erros: filtered deck com rescheduling **ligado**.
- Novos exam-only: preview com rescheduling **desligado**.
- Ordem: devidos → erros → questões/provas antigas → preview indispensável.
- Depois da prova, esvaziar os filtered decks e voltar ao topo `NEBLI`.

## Tags ortogonais

- `NEBLI::scope::core`: retenção longitudinal.
- `NEBLI::scope::exam`: prioridade local; pode coexistir com `core`.
- `NEBLI::scope::step1`: mecanismo explicitamente útil ao Step 1.
- Candidato não validado fica suspenso, sem preset ou árvore própria.

Não reclassificar o acervo antigo em massa. Aplicar primeiro a cards novos, errados, flagados ou editados.

## Formato e idioma

- Um alvo avaliável por card. Uma nota pode ter c1/c2/c3 apenas se cada card for autônomo e não redundante.
- Inglês não é obrigação universal. Quando EN e PT importarem, manter ambos no mesmo card/Extra, sem duplicar.
- Imagem só quando treina reconhecimento, localização, comparação ou mecanismo; sem quota decorativa.
- IO com muitos alvos sob uma única avaliação mascara falhas parciais; dividir grupos grandes.
- Card-mirror é QA amostral. Correção, discriminação e aderência ao escopo vêm primeiro.

## Métricas por 2–3 semanas

- `is:new -is:suspended` elegíveis, não o total bruto;
- revisões/dia, minutos/dia e backlog;
- Again, retenção madura e leeches;
- flags/comentários;
- desempenho em questões da faculdade e de aplicação.

Não usar `total de cards ÷ 15` como previsão de carga.
