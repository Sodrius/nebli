# EXEMPLARES-CARDS.md — few-shot de bons cards

> Referência dupla, como o `EXEMPLARES.md` dos resumos: (a) **gesto** — o que um bom card testa e por quê; (b) **forma** — a voz cloze do AnKing v12, que os cards NEBLI autorais devem imitar para ficarem indistinguíveis no deck. Ler antes de gerar qualquer card autoral. Sementes vindas da aula embrio-gastrulacao-neurulacao (2026-07-10).

## Princípios (o que faz um card ser bom)

1. **Um fato atômico por card.** Um cloze, uma ideia. Se o card testa duas coisas, vira dois cards.
2. **Ancorado numa frase da E1.** A resposta do card tem de estar escrita no resumo daquela aula (R1). Se não está, ou a E1 sobe (loop) ou o card sai.
3. **Testa o mecanismo, não só o rótulo.** Preferir "por que / como" a "qual o nome de". Um card de nível 3 na rubrica R6 cobra a relação causal, não só o termo.
4. **Contexto suficiente no enunciado.** O card sozinho tem de fazer sentido sem o Davi lembrar de onde veio — senão auto-suspende e distorce o algoritmo (filosofia: precisão > recall).
5. **Voz AnKing:** enunciado curto, cloze `{{c1::...}}`, dica de campo quando ajuda a desambiguar (`{{c1::motor::motor ou sensitivo}}`).

## Exemplares por gesto

### G1 — Origem/derivado (o formato que o AnKing faz bem)
Bom quando o subtópico da E1 é uma tabela de derivados.
```
What is the embryonic origin of the kidneys? {{c1::Meso::Endo/Meso/Ecto}}derm
```
Por que é bom: atômico, dica de campo desambigua as três opções, casa direto com "mesoderma intermediário → rins" da E1. Nível 2 (fato central; o "porquê intermediário" ficaria nível 3).

### G2 — Indução/mecanismo (o que eleva para nível 3)
```
The {{c2::notochord}} induces the overlying ectoderm to form the {{c1::neural plate (neuroectoderm)}}
```
Por que é bom: testa a **relação causal** (quem induz quem), não só um nome. Reconstrói a espinha dorsal da neurulação. Nível 3.

### G3 — Consequência clínica ancorada no mecanismo
```
Supplemental maternal {{c2::folic acid (vitamin B9)}} in early pregnancy decreases risk of {{c1::neural tube}} defects
```
Por que é bom: liga a vitamina ao desfecho; o campo-extra ("tomar ≥1 mês antes da concepção") carrega o *porquê* da janela. Casa com o box de ácido fólico da E1. Nível 3.

### G4 — Contraste que fixa a fronteira (anti-confusão)
```
The embryonic {{c1::notochord}} becomes the {{c2::nucleus pulposus}} of the intervertebral discs in adults
```
Por que é bom: fixa exatamente a pegadinha que a E1 alerta ("notocorda vira só o núcleo pulposo, não o corpo da vértebra"). Nível 3.

## Como um card NEBLI autoral deve sair (lacuna de processo)

**Formato obrigatório (R9):** cloze deletion, **um único cloze por card** (só `{{c1::...}}`), **Extra** com explicação sucinta (1–2 frases, o *porquê*), e **imagem quando viável** (slide do professor ou figura de card AnKing). Quando o AnKing não cobre um subtópico de **processo** (EMT, dobramentos, membranas), gerar destilando da frase da própria E1. Exemplos-alvo para embrio (a validar contra o padrão real antes de aplicar — ver pendência):

```
# Subtópico 1.2 — EMT / ingressão  (LACUNA no AnKing)
Texto:  To ingress through the primitive streak, an epiblast cell undergoes {{c1::epithelial–mesenchymal transition (EMT)}}.
Extra:  Perde junções e polaridade apical-basal e vira migratória. A mesma maquinaria reaparece na crista neural e, patológica, na metástase.
Imagem: slide-14 (bottle cell / migração pela linha primitiva).

# Subtópico 3.2 — dobramento (LACUNA no AnKing)
Texto:  The folding that curves the cranial and caudal ends ventrally into a C shape is the {{c1::cephalocaudal}} folding.
Extra:  Visto em corte sagital; ocorre junto ao fechamento do tubo neural, empurrado pela expansão da cavidade amniótica.
Imagem: slide-53 (dobramento céfalo-caudal, corte sagital).

# Subtópico 3.3 — membranas (LACUNA no AnKing)
Texto:  The two points where no mesoderm lies between ecto- and endoderm are the {{c1::buccopharyngeal and cloacal}} membranes.
Extra:  Por não terem mesoderma no meio, rompem-se para abrir boca (anterior) e ânus (posterior); se a cloacal não rompe → ânus imperfurado.
Imagem: slide-64 (tubo endodérmico, boca/ânus).
```

> **Nota de calibração (pendência):** antes de aplicar cards autorais num deck, destilar o padrão dos cards reais do AnKing daquele sistema e validar o formato (ver memória [[calibrar-antes-de-gerar-cards]]). Os exemplos acima são rascunho de forma, não versão final.
