# Mapa de Confusões — Potencial de repouso da membrana

**Aula UC01:** `fisio-03-potencial-repouso` · **Construído antes da redação da E2.**

Estoque de erros mecanísticos que o aluno do 1º semestre comete neste tema. Distratoras da E2 encarnam confusões deste mapa (anotar qual confusão cada distratora cobre no relatório final).

---

## 1.1 — Por que a membrana separa cargas (capacitor)

1. **Volume IC carregado em massa.** Acha que o interior inteiro da célula está carregado de "−" e o exterior inteiro de "+". Na verdade a célula é eletricamente neutra como um todo; só a fina camada de cargas junto à membrana é que está desbalanceada. (origem: banco NEBLI candidatas + livro-texto Boron cap. 6)
2. **Membrana como resistor puro.** Trata a membrana só como barreira que deixa ou não íons passarem. Esquece que ela armazena cargas opostas em superfícies opostas — é também capacitor. (origem: armadilha do guia editorial UC1)
3. **Neutralidade global ⇒ sem potencial.** Conclui que, se o número total de cargas + e − dentro e fora é igual, não pode existir Vm. Não consegue conciliar "neutro" com "polarizado". (origem: livro-texto Costanzo cap. 1)
4. **Potencial = quantidade de cargas.** Confunde diferença de potencial (V, em volts) com número de íons em desequilíbrio. Pequeníssima assimetria iônica (ppm da população total) já gera dezenas de milivolts. (origem: armadilha clínica derivada — hipercalemia muda Em sem mudar [K+] mensuravelmente)

## 1.2 — Convenção Vm = Vint − Vext

1. **Inversão de sinal.** Calcula Vm = Vext − Vint e fica com +70 mV em vez de −70 mV. Erro sistemático: a tabela do Boron usa Vint − Vext, a do Hammond às vezes o inverso. (origem: armadilha clínica + livro-texto)
2. **"Negativo" como excesso de Cl⁻ intracelular.** Acha que o sinal negativo decorre de Cl⁻ estar dentro da célula. Cl⁻ está em MAIOR concentração FORA; o sinal negativo vem do conjunto do desequilíbrio, dominado por K⁺ saindo. (origem: banco NEBLI candidatas)
3. **Despolarização × hiperpolarização invertidos.** Define despolarização como ficar mais negativo (errado) e hiperpolarização como ficar mais positivo (errado). Despolarização = Vm sobe (vai para 0 e além); hiperpolarização = Vm desce (fica mais negativo que -70). (origem: armadilha clássica do guia editorial)
4. **−70 mV = "muito negativo".** Trata −70 mV como se fosse magnitude absoluta, sem entender que é diferença Vint vs Vext. Se mudar a referência, o número muda. (origem: armadilha pedagógica)

## 1.3 — Concentrações iônicas desiguais

1. **K⁺ alto fora.** Trocaria K⁺ por Na⁺ no extracelular. K⁺ é 100 mM IC e 5 mM EC; Na⁺ é 15 mM IC e 150 mM EC. (origem: banco NEBLI q-0010, q-0011)
2. **Cl⁻ "do intracelular".** Confunde Cl⁻ (alto EC, 150 mM; baixo IC, 13 mM) com íon predominantemente IC. Cl⁻ é EC junto com Na⁺. (origem: banco NEBLI candidatas)
3. **Ânions impermeáveis móveis.** Acha que os A⁻ intracelulares (proteínas com carga negativa, fosfatos orgânicos, sulfatos) podem atravessar a membrana e equilibrar cargas. Eles são impermeáveis por definição e mantêm a assimetria. (origem: livro-texto Boron cap. 6)
4. **Gradiente Na⁺ mantido só por canais.** Esquece que a bomba Na/K-ATPase é quem efetivamente mantém os gradientes de Na⁺ e K⁺ contra o que os canais de vazamento dissipariam. (origem: armadilha clínica — uso de ouabaína)

## 1.4 — Duas forças: química e elétrica

1. **Só a força química conta.** Trata o íon como se difundisse até esgotar o gradiente. Esquece que o próprio movimento gera campo elétrico que se opõe e estabelece equilíbrio. (origem: banco NEBLI + Boron cap. 6)
2. **Inverte sinal de Δμ químico ou da energia elétrica.** Em fórmulas usa RT ln([X]_int/[X]_ext) onde deveria ser ([X]_ext/[X]_int) ou vice-versa, ou troca zF·ΔV por -zF·ΔV. (origem: armadilha matemática do slide)
3. **Forças se somam, nunca se cancelam.** No equilíbrio elas se cancelam — magnitude igual, direções opostas. Quem soma sem checar sinal nunca chega ao equilíbrio. (origem: pedagógica)
4. **Eletroquímico = só químico.** Trata "gradiente eletroquímico" como sinônimo de "gradiente de concentração". O eletroquímico é a soma vetorial dos dois componentes (μ_quim + zFV). (origem: livro-texto)

---

## 2.1 — Célula só com canal de K⁺ gera potencial sozinha

1. **K⁺ flui até esgotar o gradiente.** Acha que K⁺ continuaria saindo até [K⁺]_int = [K⁺]_ext. Não — para quando a força elétrica gerada (negativa puxa o K⁺ de volta) iguala a força química que o empurra para fora. (origem: banco NEBLI + Boron cap. 6)
2. **Canal "bombeia" K⁺.** Atribui a saída de K⁺ a algum mecanismo ativo. Canal é via passiva; quem fornece energia é o gradiente que a bomba criou previamente. (origem: armadilha clássica)
3. **Em negativo por causa do A⁻.** Acha que o interior fica negativo porque os ânions impermeáveis estão lá. Errado: A⁻ estão lá desde antes, mas o sinal negativo aparece quando K⁺ sai, deixando "déficit" de cargas + na camada interna superficial. (origem: pedagógica)
4. **Pequena perda de K⁺ neutraliza a célula.** Acha que íons EC entram em massa para "compensar" a saída de K⁺. Não — a quantidade de K⁺ que efetivamente sai é minúscula (ppm), suficiente para mudar a polarização de membrana sem afetar [K⁺] global. (origem: Boron — fração de íons que efetivamente migra é < 10⁻⁵ do total)

## 2.2 — Nernst para K⁺ (EK = −80 mV)

1. **Esquece o logaritmo.** Usa razão direta [K⁺]_ext/[K⁺]_int = 5/100 = 0,05 e multiplica por RT/zF. Sem ln, o resultado fica em ordem de magnitude errada. (origem: armadilha do slide-17)
2. **Razão invertida no log.** Usa ln([K⁺]_int/[K⁺]_ext) em vez de ln([K⁺]_ext/[K⁺]_int). Resultado fica +80 mV em vez de −80 mV. (origem: banco NEBLI + livro-texto)
3. **Temperatura errada.** Usa 25 °C (298 K) em vez de 37 °C (310 K) — diferença pequena mas suficiente para errar em prova de cálculo. (origem: armadilha matemática)
4. **Valência z confundida.** Para K⁺ usa z=2 (achou que K era 2+) ou z=-1 (confundiu com Cl⁻). Em ambos os casos o sinal final inverte ou a magnitude muda. (origem: banco NEBLI candidatas)

## 2.3 — ENa = +62 mV e ECl = −65 mV

1. **ENa negativo.** Acha que ENa é negativo "porque Na⁺ entra na célula". A direção do fluxo NÃO determina o sinal de E; o sinal de E é o potencial que faria o íon parar. ENa é positivo porque é preciso deixar o interior + positivo para compensar a força química que empurra Na⁺ para dentro. (origem: armadilha clássica + livro-texto)
2. **ECl positivo por estar fora.** Não usa o sinal de z = −1. Como o Cl⁻ é negativo, o sinal do potencial de equilíbrio inverte, e ECl fica negativo apesar de [Cl⁻]_ext > [Cl⁻]_int. (origem: banco NEBLI + slide-25)
3. **ECl irrelevante porque "Cl⁻ se acomoda passivamente".** Trata ECl como detalhe — ignora que ECl ≈ −65 mV está perto do Em (−70 mV) e o Cl⁻ é importante para a estabilidade da membrana e para inibição sináptica via GABA-A. (origem: armadilha clínica)
4. **ENa "atrai" Na⁺ continuamente.** Conclui que se ENa = +62 mV, Na⁺ está sempre entrando. Esquece que ENa é o potencial em que Na⁺ pararia de fluir — em −70 mV, sim há influxo, mas não infinito; o módulo da driving force importa. (origem: pedagógica)

## 2.4 — Por que −70 mV não é igual a nenhum dos três

1. **Média aritmética simples.** Calcula (-80 + 62 + -65)/3 = -27,7 mV. Errado. O cálculo correto é média ponderada por condutância (GHK), e como gK domina, Em vai para perto de EK. (origem: armadilha matemática)
2. **"Perto do EK porque está perto numericamente".** Não conecta a proximidade ao mecanismo. O motivo real é que gK >> gNa, gCl no repouso — não é coincidência geográfica. (origem: pedagógica)
3. **Condutância g = permeabilidade P.** Trata g e P como sinônimos. P depende só do número e abertura de canais; g depende também das concentrações iônicas presentes. (origem: livro-texto Boron)
4. **Em ≠ Eíon viola Nernst.** Acha que se o Em real (−70) não bate com EK (−80), Nernst está "errado". Não — significa que o K⁺ não está em equilíbrio (há corrente líquida fluindo). Nernst dá o equilíbrio HIPOTÉTICO se aquele íon fosse o único. (origem: armadilha conceitual)

---

## 3.1 — Equação de GHK por condutâncias

1. **Média simples sem ponderação.** Soma EK + ENa + ECl e divide por 3. A fórmula correta pondera cada Eíon pela sua condutância (Em = ΣgᵢEᵢ / Σgᵢ). (origem: armadilha matemática + slide-28)
2. **Pondera por concentração em vez de condutância.** Multiplica cada Eíon por [íon] em vez de g. Não captura o fato de que o que importa é "quanto canal está aberto", não "quanto íon existe". (origem: banco NEBLI candidatas)
3. **Cada íon vota igual.** Trata gK = gNa = gCl. Não percebe que no repouso a célula é "muito mais permeável a K⁺" — os canais de vazamento de K⁺ é que dominam, e isso pesa Em para perto de EK. (origem: pedagógica)
4. **Aumentar gNa hiperpolariza.** Inverte: pensa que aumentar a condutância de um íon puxa Em na direção contrária. Aumentar gNa puxa Em para ENa (+62) — despolariza. Aumentar gK puxa para EK (-80) — hiperpolariza. (origem: armadilha clínica — abertura de canais de Na+ é o gatilho do PA)

## 3.2 — Canal como bateria + resistência

1. **Canal só "bateria" OU só "resistência".** Trata o canal como um ou outro. É os dois: a bateria carrega o potencial de equilíbrio (Eíon), a resistência limita a corrente. Em série. (origem: slide-32)
2. **Driving force = Em.** Calcula corrente como i = Em/R em vez de i = (Em − Eíon)/R. Esquece que a corrente é movida pela diferença entre Em e Eíon, não pelo Em sozinho. (origem: armadilha matemática + livro-texto)
3. **Sinal da corrente invertido.** Não respeita a convenção: corrente positiva = movimento de cargas POSITIVAS do IC para o EC. Cl⁻ entrando = corrente positiva (carga negativa indo no sentido contrário). (origem: armadilha clássica)
4. **Em = Eíon ⇒ corrente máxima.** Acha que quanto mais o Em parece com Eíon, mais corrente flui. É o oposto: se Em = Eíon, driving force = 0 e corrente = 0. (origem: pedagógica)

## 3.3 — Circuito em paralelo, im = 0 no repouso

1. **Cada corrente individual = 0.** Acha que no repouso iK = 0 e iNa = 0 separadamente. Errado — iK ≠ 0 (K⁺ saindo continuamente) e iNa ≠ 0 (Na⁺ entrando), mas a SOMA é zero (ou quase). (origem: banco NEBLI + slide-45)
2. **Sem bomba, im = 0 indefinidamente.** Acha que como im = 0 no repouso, a bomba é supérflua. Não — sem bomba, as correntes de vazamento dissipariam gradualmente os gradientes e o Em iria para zero ao longo do tempo. (origem: armadilha clínica — ouabaína)
3. **Rm em série.** Trata os três canais como resistências em série (Rm = RK + RNa + RCl). Estão em PARALELO: 1/Rm = 1/RK + 1/RNa + 1/RCl. (origem: armadilha matemática + slide-44)
4. **Aumentar gK despolariza.** Confusão direta. Aumentar gK puxa Em para EK (mais negativo) — hiperpolariza. (origem: banco NEBLI candidatas)

## 3.4 — Bomba Na/K: curto vs longo prazo

1. **Bomba mantém Em diretamente.** Acha que a bomba "gera" os -70 mV pelo bombeamento. Não — a bomba mantém os GRADIENTES, e os gradientes (via canais de vazamento) geram o Em. Contribuição direta da bomba ao Em é pequena (~−5 mV pela eletrogenicidade). (origem: armadilha clássica + livro-texto)
2. **Estequiometria simétrica.** Acha que a bomba é 1 Na⁺ por 1 K⁺ ou 2 por 2. É 3 Na⁺ saem para cada 2 K⁺ que entram — eletrogênica, contribui levemente para a polarização. (origem: banco NEBLI + slide-46)
3. **Bloqueio da bomba ⇒ Em = 0 imediatamente.** Acha que ouabaína cancela o Em na hora. CURTO PRAZO: nada muda no Em (gradientes ainda lá, canais ainda funcionam). LONGO PRAZO: gradientes dissipam, Em vai despolarizando até chegar próximo de 0. (origem: armadilha clínica de ouabaína/digoxina)
4. **Ativo primário × secundário.** Confunde a bomba Na/K-ATPase (ativo primário — usa ATP direto) com transportadores secundários (SGLT, NCX — usam o gradiente de Na⁺ criado pela bomba). (origem: pedagógica + aula prévia fisio-02)

---

**Total: 48 confusões. Atualizar este arquivo após a E2 marcando qual confusão foi encarnada em qual distratora.**
