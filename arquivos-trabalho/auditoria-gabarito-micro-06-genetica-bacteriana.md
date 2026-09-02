# Auditoria de gabarito — micro-06-genetica-bacteriana

**Veredito: VERDE.**

**Executor:** sessão principal, à mão, item a item. O subagente `revisor-gabarito` não pôde ser disparado nesta corrida — o stub `.claude/agents/revisor-gabarito.md` declara `tools: read, bash` em minúsculas e o runtime recusa o spawn ("would be spawned with zero tools"). Vale para os 9 stubs. Registrado como pendência; **não foi corrigido nesta corrida** para não alterar configuração compartilhada sem pedido.

Conferência automática complementar: `verificar_gabarito_resumo.py micro-06-genetica-bacteriana` → *OK, 0 avisos* (30 questões, 20 MC + 10 CE, 30 itens no gabarito).

---

## 1. Impresso == correta real (checagem bloqueadora)

### Múltipla escolha (20)

| Q | Gab. | Por que essa é a correta |
|---|---|---|
| 01 | D | Topoisomerases mantêm o superenovelamento gastando energia; a girase é o alvo das quinolonas. As demais atribuem o feito a histonas, à dobra passiva, à polimerase ou a fragmentação do anel. |
| 03 | B | UV forma ligação covalente entre pirimidinas vizinhas da mesma fita e deforma a hélice sem trocar informação. A descreve ionizante; C, desaminação; D, intercalante; E, alquilante. |
| 04 | B | **Incorreta pedida.** Replicação é semiconservativa: cada filha recebe uma fita antiga e uma nova. A, C, D, E são verdadeiras. |
| 05 | E | Os três destinos canônicos: restauração, morte por ausência de reparo, e reparo que tolera a lesão e deixa erro. |
| 07 | A | Transformação define-se pelo veículo — DNA nu do meio, sem intermediário e sem contato. B é transdução; C, conjugação; D, transposição; E, Hfr. |
| 08 | C | Repetições invertidas como sítio de reconhecimento + transposase codificada no interior. B descreve integron; D, conjugação; E, profago. |
| 09 | E | Plasmídeo se distribui com o citoplasma sem segregação ativa; sem pressão seletiva as células que o perderam permanecem na população. |
| 12 | D | A desaminação da 5-metilcitosina gera timina, base legítima — o sistema de vigilância não a reconhece como intrusa. E confunde com a citosina não metilada (uracila, removida por glicosilase). |
| 13 | D | 10⁹ células × 4,6 × 10⁶ pb = 4,6 × 10¹⁵ bases copiadas; ÷ 10⁸ = 4,6 × 10⁷. E dá o total de bases; B ignora a população; C e A erram a unidade da taxa. |
| 15 | A | **Incorreta pedida.** Fragmento linear captado não tem origem de replicação e desaparece se não recombinar. B, C, D, E descrevem barreiras reais. |
| 17 | C | Conjugação traz o plasmídeo de outra espécie; o transposon fixa os genes no cromossomo — daí a proporção de GC destoante e a estabilidade. |
| 18 | B | Fago de sítio fixo → excisão imprecisa → só a vizinhança do sítio viaja: transdução especializada. A descreve a generalizada; E, Hfr. |
| 20 | E | RNA guia derivado do espaçador + nuclease Cas cortando a sequência complementar do plasmídeo antes da replicação dele. |
| 21 | E | **Incorreta pedida.** Uracila **não** é base normal do DNA e **é** removida por glicosilase. A, B, C, D são correspondências corretas lesão↔reparo. |
| 23 | A | Genoma reduzido por perda de vias biossintéticas → dependência de precursores prontos → meio enriquecido. C inverte a direção evolutiva; E troca exigência nutricional por osmótica. |
| 25 | C | O tubo em U (retém células, deixa passar DNA) abolindo os recombinantes é o que prova que o contato é indispensável. |
| 26 | D | Quatro resistências não relacionadas, de uma vez, sem exposição prévia = plasmídeo conjugativo de amplo espectro carregando o bloco. |
| 27 | B | Resistência a uma classe só, à droga em uso, surgida durante o tratamento = mutação na girase favorecida pela resposta ao dano que a própria quinolona dispara. |
| 29 | C | O gene da toxina diftérica vem no profago; sem ele, a bactéria é comensal de orofaringe. |
| 30 | E | GC divergente + repetições nas bordas = assinatura de aquisição horizontal fixada por transposição. |

### Certo/Errado (10 · 4 itens I–IV cada)

Sequências lidas item a item **depois** de escritas as assertivas (procedimento de `ERROS.md` #23 — nada foi sorteado antes):

| Q | Sequência | Itens falsos e por quê |
|---|---|---|
| 02 | C E E C | II: identidade está no cromossomo, não no plasmídeo. III: nem todo plasmídeo é conjugativo. |
| 06 | C C E E | III: descreve excisão de **base**, e ligase não preenche a lacuna. IV: tolerância não restaura sequência. |
| 10 | C E E E | II: quinolona inibe girase/topo IV, não a polimerase. III: superenovelamento consome energia. IV: resistência é por mutação cromossômica, não gene adquirido. |
| 11 | C E C C | II: fotoliase só desfaz dímero de pirimidina, nunca quebra de dupla fita. |
| 14 | E C C E | I: a resposta suprime a revisão e eleva a taxa de mutação. IV: dose subletal de quinolona **aumenta** a taxa. |
| 16 | C C C E | IV: a doadora transfere uma fita e ressintetiza a outra — ambas ficam com o plasmídeo. |
| 19 | E C E E | I: integron não se move sozinho. III: as IR são sítio de reconhecimento, não codificam a enzima. IV: transposto ao cromossomo o gene fica **mais** estável. |
| 22 | E C C C | I: Ames conta revertentes his⁺, não sobreviventes. |
| 24 | C C E C | III: o módulo não impede a perda — ele mata a filha que perdeu. |
| 28 | E E C E | I: o antibiótico aumenta a liberação de toxina. II: o gene vem de profago. IV: a SHU é toxina circulante, não bacteremia. |

**Divergências encontradas: 0/30.**

## 2. Corrida degenerada

- **MC, na ordem das questões:** D B B E A C E D D A C B E E A C D B C E — corrida máxima = 2. Sem 4+ iguais.
- **C/E:** nenhuma sequência é `CCCC`, `EEEE`, `CECE` ou `ECEC`. Nenhuma das 10 se repete (10 padrões distintos dos 12 admissíveis).
- Distribuição de contagem por questão variada — 4 questões 2C-2E, 4 questões 3C-1E, 2 questões 1C-3E. Não há o padrão "quase tudo 2C-2E" que o aluno explora.

## 3. Distribuição

- **MC:** A 3 (15%) · B 4 (20%) · C 4 (20%) · D 4 (20%) · E 5 (25%). Teto de ~40% respeitado com folga.
- **C/E:** 21 C e 19 E em 40 itens. Equilibrado sem ser 50/50 forçado.

**Nenhum reposicionamento foi necessário** — nenhuma correta foi trocada nem movida para caber numa letra-alvo.
