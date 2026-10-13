# Grand Round 2 (diabetes) — revisão da corrida

Estado em 03/10/2026: 114 cards da aula e 2 notas compartilhadas instalados no Anki. **Não liberado (gate vermelho).** Faltam Tab completo e gate verde. Os 114 cards novos da UC03 foram suspensos após o último delta (`deck-ops/20261003-172432-suspender.json`). O APKG e os slides foram copiados para a pasta correta no Drive e conferidos por SHA-256; isso é staging, não entrega aprovada. Sem E1 por pedido explícito. Novos cards em inglês.

## Fontes e recorte

As 57 lâminas foram percorridas (caso, teoria, complicações e radiologia). `cobertura.json` relaciona cada uma a cards ou exclusão justificada, além das seções pertinentes do Robbins cap. 24 e das questões antigas. A prova 2024 P1 2.9 deu o teto da sequência de glicação; não puxou tema fora dos slides. O guia do veterano e as transcrições integrais de Ninja Nerd (diabetes), Osmosis (diabetes) e Catalyst (AGEs) foram cotejados; `fontes.json` informa o impacto concreto. Não foram localizados exercícios específicos; CAOC ficou inacessível na conta montada, declarados nas fontes. Tratamento minucioso da cetoacidose, algoritmo SGLT2 e doenças raras do capítulo não entraram por estarem fora desta aula.

## Seleção e forma

114 cards, dos quais 101 AnKing e 13 autorais (11%). Os dois compartilhados pertencem à FI09. AnKing e externos foram buscados por alvo (`busca/anking.txt`, `busca/ext.txt` e `busca/sessao2-anking-ext.txt`). Os autorais cobrem lacunas úteis como frutosamina, lua de mel, sequência Schiff–Amadori–AGE, AGE–RAGE e leitura de imagem da própria aula. Lint: 13 autorais, zero reprovação dura. No teste cego de origem (`card-mirror/` e `card-mirror-r2/`), a primeira rodada reconheceu 12/13 autorais; revisamos pistas editoriais concretas e retestamos sem afirmar que se tornaram indistinguíveis.

Os 71 verdes seguem alvos longitudinais: diagnóstico, deficiência de insulina, potássio antes da insulinoterapia, metabolismo da CAD, resistência à insulina, glicação e complicações típicas. Exemplo de ganho: `insulina-k` explica uma decisão clínica do caso; `cd8-dm1` ancora a patogênese. Azuis (40) incluem a leitura radiológica específica (`angiotc`, `osteo-sinal`) e detalhes da prova; três rosas apoiam contexto de menor prioridade (APS-2 e monitorização). Não há quota de verdes por aula. Hiperfiltração e glomeruloesclerose são recuperadas separadamente; sinônimos e fatos sem ganho próprio foram ao verso.

## Revisão do deck vivo

As frentes, versos, cores, imagens listadas e comentários foram percorridos em `nebli.revisar` após instalar (quatro trechos do conjunto); `revisao-final.json` traz veredito para todas as 103 entradas próprias e 2 compartilhadas. As figuras Robbins 24-30 a 24-39 usadas foram abertas e comparadas com o alvo. Uma incompatibilidade real foi corrigida: 24-34 não ilustrava a arteriolosclerose hialina; `hialina` conserva a foto adequada do AnKing. Outra: 24-38 era peça renal, não ultrassom; `rim-inicio` e `rim-final` agora usam recortes do slide 47, e `osteo-sinal` usa a RM T2-FS do slide 57. As exceções de imagem de slide têm motivo `slide_sem_alternativa` e registro em `imagens-vistas.json`. O readback do delta contou 114 cards e nenhum problema. Ordem verificada pelo gate Anki.

**Pendente real:** explicações Tab. Em 03/10 às ~17h, 115/117 faltavam; a geração automática interrompeu por limite da assinatura e informa reinício às 20h (America/Sao_Paulo). Depois de gerar, ler amostra de autoral, irmão, imagem e clínica; atualizar `revisao-final.json` sem antecipar o resultado. Os 114 cards novos da UC03 foram suspensos; os compartilhados da UC08 não foram tocados. O pacote UC03 foi verificado (`source_sha256` b2a277a7…, saída a78ce943…; 170 cards no export) e seu hash confere com o arquivo presente no Drive; os slides também conferem (90c9b7a6…). Só o gate verde conclui a entrega.

Feedbacks considerados: F-20261003-CLAUDE-13–19 e F-20261003-CODEX-20–22. A próxima aula é a primeira Microbiologia dos Fungos da UC03 P3, **somente depois** de concluir esta corrida.
