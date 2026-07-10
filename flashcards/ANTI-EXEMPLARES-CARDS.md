# ANTI-EXEMPLARES-CARDS.md — o que NÃO fazer

> Catálogo de padrões de card ruins e de **matches falsos** (o card parece cobrir o subtópico, mas não permite reter). Cada item: o padrão, por que é ruim, e o conserto. Sementes da aula embrio-gastrulacao-neurulacao (2026-07-10).

## A1 — Match falso: "conceito similar" contado como cobertura (o que o Davi sentiu)
O subtópico da E1 é **processo**, mas o único card que o toca cobra um **fato de timing/rótulo** adjacente. A rubrica R6 chama isso de nível 1 — não deve contar como "forte".
```
During which week of gestation does the primitive streak appear? {{c1::Week 3}}
```
Por que é ruim como cobertura de "1.2 Linha primitiva, nó e ingressão (EMT)": responde *quando* a linha aparece, não o que ela **faz** (organizador, eixo, simetria, cílios/lateralidade) nem a EMT. O Davi decora a semana e continua sem reter o mecanismo.
**Conserto:** manter o card de timing (é bom no que faz), mas marcar o subtópico como RASO e gerar cards de mecanismo (nó organizador; EMT) — via loop Card→E1 + cards autorais.

## A2 — Card de próxima-aula infiltrado (escopo)
Toca um termo que **é** subtópico da E1 ("tubo neural / neuroectoderma"), mas num nível que a aula não abre — é conteúdo da aula seguinte (organogênese do tubo neural).
```
The embryonic brainstem and spinal cord have a(n) {{c2::dorsally}}-located {{c1::alar}} plate
The alar plate and basal plate are separated by the {{c1::sulcus limitans}}
The neural tube begins as {{c1::three::number}} primary vesicles
```
Por que é ruim: viola R1 (Davi esbarra em "placa alar", "sulco limitante", "vesículas primárias" — nada disso está na E1) e R4 (é próxima-aula, não aprofundamento da atual).
**Conserto:** **drop** (balde FORA). Não é candidato a loop — não force a E1 a abrir a próxima aula.

## A3 — Pegadinha de nível celular fora do escopo do slide
```
What is the embryonic origin of microglia? {{c1::Mesoderm}}   (M icroglia = M esoderm)
What is the embryonic origin of dura mater? {{c1::Meso::Endo/Meso/Ecto}}derm
```
Por que é ruim aqui: oligodendrócito/astrócito/micróglia/dura são embriologia neural fina, clássica de banca Step 1 **mas de outra aula** (histologia/neuro do SNC). A aula é gastrulação→dobramento. Cai em FORA por escopo, mesmo sendo high-yield noutro contexto.
**Conserto:** drop nesta aula; reaproveitar quando a aula do sistema nervoso for curada (mora no deck daquela aula).

## A4 — Card só-Step-2 (fora do alvo do Davi)
Qualquer nota de manejo/tratamento avançado, estadiamento, conduta — tag `#AK_Step2_v12::` ou equivalente.
Por que é ruim: Davi se prepara para o **Step 1** (R7). Step 2 é ruído de pool.
**Conserto:** podar no `prefiltrar_pool.py` **antes** do keep/drop fino.

## A5 — Card não-atômico (dois fatos num cloze só)
```
The foregut runs from the {{c1::lower esophagus}} to the {{c2::proximal duodenum}}, supplied by the {{c3::celiac trunk}}
```
Por que costuma ser ruim: se o Davi sabe uma metade e erra a outra, o card inteiro conta como falha e vira leech. Além disso, limites anatômicos precisos de fore/mid/hindgut podem ser mais fundos que a E1 (que só nomeia as três regiões + irrigação por artéria própria) → checar R6/R1.
**Conserto:** quebrar em cards atômicos **e** confirmar ancoragem na E1; se a E1 não dá o limite anatômico, ou sobe (loop) ou o card sai.

## Checklist rápido antes de manter um card
- [ ] A resposta está numa frase da E1 desta aula? (R1) — senão: loop ou drop
- [ ] É desta aula, não da próxima? (R4/A2)
- [ ] Não é só-Step-2? (R7/A4)
- [ ] Um fato atômico? (A5)
- [ ] Cobra mecanismo, não só rótulo/timing? (sobe o nível R6)
