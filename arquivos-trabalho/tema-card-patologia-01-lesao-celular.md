# Tema Card — Lesão celular (mecanismos de lesão e morte celular)

## Seção A — Escopo

- **Tema:** Lesão celular — causas, mecanismos e o ponto sem retorno
- **Slug:** `patologia-01-lesao-celular`
- **Disciplina:** Patologia (Patologia geral — Parte 1 de Lesão Celular)
- **Fonte de entrada:** transcrição integral da aula (PDF, 44 páginas de fala), sem slides em imagem
- **Onde estudar:** Robbins & Cotran cap. 2 · Robbins Patologia Básica cap. 1–2
- **Alvo de páginas E1:** piso 2, **teto 22** — alvo 16–20 (tema denso, pedido explícito de aprofundar)
- **`profundidade:` `fundo`** — Davi pediu "aprofundar bem e ser bem completo e direto, mas fluido". Dial ativo: mais injeções mecanísticas por subtópico, blocos clínicos maiores, limiar de admissão afrouxado.
- **Recorte slide × tema:** a aula é a **Parte 1** de um bloco de duas semanas. Ela cobre o organograma (homeostase → adaptação → lesão reversível → irreversível → morte), as causas, a morfologia da lesão reversível, os critérios de irreversibilidade, a leitura clínica pelas enzimas, e os quatro mecanismos (ATP, mitocôndria, radicais livres/reperfusão, cálcio), fechando em proteínas mal dobradas/dano ao DNA. Adaptação celular e infarto têm aula própria depois — entram aqui **só** como enquadramento. Necrose e apoptose são retomadas "de leve" pelo professor: entram como o **destino** dos mecanismos, com a profundidade de fechamento (o que diferencia as duas, por que ATP decide qual acontece), não como aula inteira de morte celular.
- **Prioridades desta corrida (do § Diário de revisões do MEMORY.md):**
  1. **Entrada sem slide ≠ resumo sem figura** (entrada 2026-05-29, peso alto). O tema tem coreografia espacial e cadeias multi-passo (cascata da isquemia, hub do cálcio, geração de EROs, convergência no dano de membrana). Figuras são **obrigatórias** — construídas como esquemas Typst nativos na identidade NEBLI, já que não há slide do professor para extrair.
  2. Cadeia ≥4 setas sem figura adjacente (ERROS #12) — cada cascata ganha esquema ao lado.
  3. Cota de boxes: 1–2 vermelhos/gold por PARTE; clínica em prosa entre travessões + `#clinica-box` só quando a cadeia pede 4–6 linhas.

## Seção B — Esqueleto (3 PARTES × 4 subtópicos) + plano de figuras

**PARTE I — Do equilíbrio à irreversibilidade**
- 1.1 Adaptação, lesão e o limiar entre elas (intensidade × duração)
- 1.2 As causas: sete portas para a mesma casa
- 1.3 A ordem dos acontecimentos: bioquímica antes da morfologia (+ morfologia da lesão reversível)
- 1.4 O ponto sem retorno: membrana e DNA — e como isso se lê no sangue
- *Figuras:* (F1) organograma homeostase→adaptação→reversível→irreversível→morte, esquema; (F2) linha do tempo bioquímica→função→ultraestrutura→ME de luz→macroscopia com a linha pontilhada por tipo celular; (F3) tabela reversível × irreversível (comparativo 3+ dimensões — caso (a) da regra de tabelas)

**PARTE II — A cascata da isquemia**
- 2.1 Queda de ATP: a bomba de sódio para e a célula incha
- 2.2 A mitocôndria no centro: poro de transição, citocromo c e a bifurcação
- 2.3 Cálcio citosólico: o segundo mensageiro que vira demolidor
- 2.4 Dano de membrana: a via final comum
- *Figuras:* (F4) cascata ↓O₂→↓ATP com os três ramos; (F5) mitocôndria — duas portas (PTPM→necrose · citocromo c→apoptose); (F6) hub do cálcio com as quatro enzimas e seus alvos; (F7) convergência das quatro forças sobre a membrana

**PARTE III — O paradoxo do oxigênio, os danos que fogem à regra e os dois destinos**
- 3.1 Radicais livres: o custo de respirar e as defesas que o pagam
- 3.2 Lesão de isquemia-reperfusão: quando salvar machuca
- 3.3 Proteínas mal dobradas e dano direto ao DNA: a outra rota
- 3.4 Os dois destinos: necrose e apoptose
- *Figuras:* (F8) cadeia O₂→superóxido→H₂O₂→hidroxila com SOD/catalase/GPx e Fenton; (F9) curva de função pós-reperfusão (queda e recuperação); (F10) proteína mal dobrada → chaperona/ERAD → apoptose; (F11) tabela necrose × apoptose

## Seção B.bis — Registro de abertura por subtópico (sem pergunta âncora)

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | analogia concreta (sol de fim de semana, cigarro) |
| 1.3 | ponto-de-quebra (a morfologia chega atrasada) |
| 1.4 | integração-posterior (o que o sangue conta) |
| 2.1 | enquadramento |
| 2.2 | ponto-de-quebra (a mesma organela decide duas mortes) |
| 2.3 | analogia concreta (mensageiro vira demolidor) |
| 2.4 | integração-anterior (as quatro forças convergem) |
| 3.1 | enquadramento |
| 3.2 | ponto-de-quebra (o tratamento machuca) |
| 3.3 | integração-anterior (o que não passa pelos quatro) |
| 3.4 | integração-posterior (para onde a lesão irreversível vai) |

## Seção B.ter — Pré-requisitos cruzados (frase-âncora pronta, ≤25 palavras)

| Pré-requisito | Frase pronta |
|---|---|
| Fosforilação oxidativa | "A mitocôndria usa o oxigênio como aceptor final de elétrons para bombear prótons e, com esse gradiente, fabricar ATP." |
| Bomba Na⁺/K⁺-ATPase | "A bomba de sódio e potássio gasta ATP para jogar sódio para fora e trazer potássio para dentro, mantendo a célula desinchada." |
| Glicólise anaeróbia | "Sem oxigênio, a célula ainda tira pouco ATP da glicose no citosol, mas o piruvato para em lactato." |
| Cálcio como segundo mensageiro | "O cálcio fica quase todo guardado fora do citosol; quando entra, é sinal — e enzimas o obedecem." |
| Apoptose (via intrínseca) | "O citocromo c fora da mitocôndria monta o apoptossomo e liga a cascata de caspases." |

## Seção C — Distribuição da E2 (PADRÃO 10 · 15 · 5) e alvos técnicos

- Consolidação Q01–Q10 · Integração Q11–Q25 · Aplicação Q26–Q30
- **C/E (4 itens I–IV, gate hard):** Q03, Q05, Q08 · Q12, Q15, Q19, Q22, Q25 · Q28, Q30 → 10 itens (~1/3)
- **"Assinale a incorreta":** Q06, Q17, Q23 (3, sinalizado no stem)
- Paridade banda dupla 0.80–1.25 em todas as MC
- **Termos-nota alvo (6–10):** homeostase · hipóxia · isquemia · esteatose · blebs · picnose · poro de transição de permeabilidade mitocondrial · peroxidação lipídica · chaperona · autólise
- **Siglas com footnote:** ATP, ADP, EROs, SOD, GPx, CK-MB, RE, PTPM, IAM

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** tratar hipóxia e isquemia como sinônimos.
  Correção: a hipóxia tira só o oxigênio; a isquemia tira oxigênio, substrato e a remoção de metabólitos ao mesmo tempo — por isso mata mais rápido.
- **Quebra:** achar que a célula morre porque acaba o oxigênio, direto.
  Correção: acaba o ATP; a morte vem da falência das bombas, do cálcio livre e do dano de membrana que se seguem.
- **Quebra:** ler a enzima elevada no sangue como "inflamação".
  Correção: enzima intracelular na circulação significa membrana rompida — marca lesão irreversível, não intensidade de dor.
- **Quebra:** esperar ver a lesão reversível no microscópio de luz.
  Correção: nessa fase só há edema celular e, às vezes, esteatose; o resto é ultraestrutural — a morfologia chega sempre atrasada em relação à bioquímica.
- **Quebra:** achar que reperfundir é sempre e apenas benéfico.
  Correção: a reentrada de oxigênio gera um pico de radicais livres que empurra células limítrofes para a morte — o saldo é positivo, mas há custo, e ele cresce com o tempo de isquemia.
- **Quebra:** confundir a queda de pH com "só o lactato".
  Correção: o lactato contribui, mas a acidose tem componente sistêmico e da hidrólise de ATP; a resposta da cromatina é à acidez, não ao lactato em si.
- **Quebra:** achar que a mitocôndria escolhe entre necrose e apoptose por acaso.
  Correção: quem decide é o ATP restante — a apoptose é um programa que consome energia; sem ATP, o desfecho é necrose.
- **Quebra:** tratar a doença por proteína mal dobrada como caso de isquemia.
  Correção: ela não passa pela queda de ATP nem pelo cálcio — o gatilho é o acúmulo de proteína anômala no retículo, que dispara morte por via própria.

## Seção E — Exemplares-âncora

- **Cat. 1 (mecanismo parágrafo a parágrafo)** — acerta em dar um trabalho discreto a cada parágrafo (contexto → família → mecanismo A → mecanismo B) e mostrar a cadeia completa em vez do nome. Vou usar em 2.1 e 2.3, onde a tentação é enfileirar setas.
- **Cat. 8 (`atencao-box`)** — acerta em reservar o vermelho para inversão com consequência. Vou usar uma vez na PARTE I (enzima no sangue = irreversível) e uma na PARTE III (reperfusão).
- **Cat. 14 (siglas em footnote)** — acerta em nunca deixar sigla nua na prosa. Vou usar em ATP/EROs/PTPM/CK-MB.
- **Cat. 17 (cadência dialogal)** — acerta em variar abertura, pingar avaliação narrativa ("o ponto fino é"), encenar a confusão antes da caixa. Vou usar sobretudo em 1.3, 2.2 e 3.2, que são os subtópicos com maior risco de sair planos.
- **Cat. 9 (`clinica-box`)** — acerta em dar cadeia clínica de 4–6 linhas com gancho explícito doença↔mecanismo. Vou usar em angina × infarto (1.4), pancreatite (1.4, inline), e função retardada do enxerto renal (3.2).
