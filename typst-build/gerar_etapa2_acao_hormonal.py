#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEBLI -- gerador da Etapa 2 de `bioq-10-acao-hormonal`.

Existe para tornar auditavel o gate de paridade: as alternativas ficam em
estruturas Python, o script conta as palavras de cada uma, calcula o ratio
correta/maior-distratora (definicao canonica do CLAUDE.md, banda 0.80-1.25)
e so entao emite `etapa2.typ`. Ajustar comprimento vira edicao de uma linha
em vez de recontagem manual.

Ordem canonica de redacao respeitada: distratoras primeiro (25-35 palavras,
com mecanismo plausivel-mas-errado vindo de `mapa-confusoes/bioq-10-acao-hormonal.md`),
correta calibrada por ultimo para cair na banda.

Uso: python3 typst-build/gerar_etapa2_acao_hormonal.py
"""

import re
from pathlib import Path

OUT = Path(__file__).resolve().parent / "etapa2.typ"

# ---------------------------------------------------------------- gabarito
GAB = {
    1: "E", 2: "EECE", 3: "A", 4: "C", 5: "ECCE", 6: "E", 7: "B", 8: "A",
    9: "EEEC", 10: "B", 11: "D", 12: "EEEC", 13: "B", 14: "E", 15: "A",
    16: "CCEE", 17: "D", 18: "B", 19: "CCCE", 20: "E", 21: "A", 22: "ECCC",
    23: "D", 24: "C", 25: "EECC", 26: "A", 27: "CECC", 28: "D", 29: "D",
    30: "CECC",
}

BADGE = {}
for n in range(1, 11):
    BADGE[n] = "badge-consolidacao"
for n in range(11, 26):
    BADGE[n] = "badge-integracao"
for n in range(26, 31):
    BADGE[n] = "badge-aplicacao"

MC = {}   # n -> (enunciado, {letra: texto})
CE = {}   # n -> (enunciado, [(marcador, texto) x4])

# ============================================================ CONSOLIDAÇÃO

MC[1] = ("Um hormônio peptídico ocupa seu receptor na face externa da membrana de um hepatócito e, segundos depois, enzimas citoplasmáticas já mudaram de atividade. A sequência que liga um evento ao outro é:", {
 "A": "o hormônio atravessa a membrana por difusão simples, encontra a adenilato ciclase no citoplasma e a ativa diretamente, dispensando qualquer proteína intermediária entre o receptor de superfície e o segundo mensageiro produzido.",
 "B": "o receptor ocupado hidrolisa ATP em AMP cíclico por conta própria, e esse mensageiro migra até o núcleo para induzir a transcrição das enzimas que serão necessárias na resposta metabólica seguinte.",
 "C": "o receptor ativa uma proteína G que permanece funcional enquanto retém GDP; essa proteína estimula a adenilato ciclase, e o AMP cíclico produzido fosforila diretamente as enzimas-alvo do hepatócito.",
 "D": "o hormônio é internalizado junto com o receptor, e o complexo formado migra até o núcleo, onde altera a transcrição dos genes das enzimas que executarão a resposta metabólica em poucos segundos.",
 "E": "o receptor ocupado ativa uma proteína G, que só permanece funcional enquanto retém GTP; ela estimula a adenilato ciclase, o AMP cíclico gerado libera as subunidades catalíticas da PKA, e esta fosforila as enzimas-alvo.",
})

CE[2] = ("Julgue os itens sobre as formas de regulação metabólica e sobre o endereço do receptor de cada classe de hormônio:", [
 ("I", "A modulação alostérica de uma enzima envolve ligação covalente do efetor ao sítio ativo, o que torna a mudança de atividade permanente até a degradação da proteína."),
 ("II", "A regulação por expressão gênica é a mais rápida das três, por dispensar a síntese de proteínas novas e agir sobre enzimas que já se encontram prontas no citoplasma."),
 ("III", "Hormônios lipossolúveis atravessam a membrana sem transportador e encontram seu receptor no interior da célula, alterando a quantidade de proteína recém-sintetizada."),
 ("IV", "Hormônios hidrossolúveis dispensam segundo mensageiro, pois conseguem atravessar a bicamada lipídica e modificar diretamente a atividade das enzimas que já existem no citoplasma."),
])

MC[3] = ("A célula beta expressa glicoquinase, e não a hexoquinase encontrada na maioria dos tecidos. A razão mecanística dessa escolha é que a glicoquinase:", {
 "A": "tem baixa afinidade pela glicose e não é inibida pelo próprio produto, de modo que sua velocidade continua acompanhando a glicemia em toda a faixa fisiológica e serve como medidor.",
 "B": "tem afinidade muito alta pela glicose, o que garante velocidade máxima já na glicemia basal e permite que a célula beta produza ATP suficiente mesmo durante períodos prolongados de jejum.",
 "C": "é inibida pela glicose-6-fosfato acumulada, mecanismo que protege a célula beta contra a sobrecarga de substrato e mantém a secreção de insulina estável independentemente da glicemia do momento.",
 "D": "funciona em sentido inverso ao da hexoquinase, retirando o fosfato da glicose-6-fosfato e devolvendo glicose livre ao sangue, o que sustenta a glicemia durante os intervalos entre as refeições.",
 "E": "possui afinidade idêntica à da hexoquinase, mas está presente em concentração muito maior, o que aumenta a velocidade absoluta da via sem alterar a forma da curva de resposta ao substrato.",
})

MC[4] = ("A proteína quinase A fosforila tanto a glicogênio fosforilase quanto a glicogênio sintase. O efeito dessa fosforilação sobre as duas enzimas é:", {
 "A": "ativação de ambas, o que explica por que o glicogênio é sintetizado e degradado simultaneamente durante o jejum, garantindo renovação contínua do polímero armazenado no hepatócito.",
 "B": "inativação de ambas, mecanismo que congela o metabolismo do glicogênio enquanto o hormônio estiver presente e evita que a reserva seja consumida em situações de demanda energética elevada.",
 "C": "ativação da fosforilase e inativação da sintase, porque o sentido da mudança é propriedade da enzima, não do fosfato; essa oposição garante que a célula nunca construa e destrua a mesma reserva simultaneamente.",
 "D": "inativação da fosforilase e ativação da sintase, o que faz do glucagon um estímulo à síntese de glicogênio hepático e explica o aumento da reserva durante períodos de jejum prolongado.",
 "E": "efeito nulo sobre as duas, já que ambas são reguladas exclusivamente por moduladores alostéricos, cabendo à fosforilação apenas marcar as enzimas para degradação posterior pelo proteassoma da célula.",
})

CE[5] = ("Julgue os itens sobre o processamento pós-traducional da insulina e sobre o peptídeo C:", [
 ("I", "O peptídeo-sinal da pré-pró-insulina é removido apenas no grânulo de secreção, imediatamente antes da exocitose do conteúdo para a corrente sanguínea."),
 ("II", "As pontes dissulfeto que mantêm as cadeias A e B unidas já estão formadas na pró-insulina, antes de o trecho central ser removido por proteases."),
 ("III", "O peptídeo C é secretado em quantidade equivalente à da insulina, o que permite estimar a produção endógena do pâncreas daquele paciente."),
 ("IV", "Um paciente com hipoglicemia, insulina alta e peptídeo C indetectável tem, muito provavelmente, produção endógena excessiva por tumor de células beta."),
])

MC[6] = ("Na via de síntese das catecolaminas, a etapa que limita a velocidade de produção do tecido é catalisada pela:", {
 "A": "feniletanolamina N-metil transferase, enzima da etapa final, cuja distribuição restrita à medula adrenal impõe o teto de produção de todas as catecolaminas do organismo.",
 "B": "DOPA descarboxilase, que retira o grupo carboxila e cuja atividade determina quanto da dopa formada seguirá adiante na via até se transformar em dopamina e depois em noradrenalina.",
 "C": "dopamina beta-hidroxilase, responsável por inserir a hidroxila lateral, etapa que representa o gargalo da via por exigir cofator específico presente em concentração limitante no citoplasma.",
 "D": "fenilalanina hidroxilase, que fornece a tirosina inicial e cuja deficiência limitaria toda a produção subsequente de catecolaminas por escassez do aminoácido precursor da via.",
 "E": "tirosina hidroxilase, enzima do primeiro passo, cuja velocidade determina quanto de catecolamina o tecido consegue produzir e que por isso é o ponto regulado da via.",
})

MC[7] = ("Sobre a definição de hormônio e sobre os pontos em que sua ação pode ser regulada, assinale a alternativa *incorreta*:", {
 "A": "Hormônios não constituem uma classe química única: peptídeos, derivados de colesterol e derivados de ácidos graxos operam todos como mensageiros, e o que os define é o modo de agir a distância.",
 "B": "A fração do hormônio ligada à proteína carreadora é a biologicamente ativa, enquanto a fração livre serve apenas como reserva circulante protegida da degradação enzimática no plasma.",
 "C": "A mesma molécula pode funcionar como hormônio ou como neurotransmissor conforme a rota de entrega, como acontece com a adrenalina liberada na circulação ou numa fenda sináptica.",
 "D": "Uma falha no reconhecimento pela célula-alvo produz quadro clínico mesmo com síntese e secreção preservadas, situação que corresponde ao problema central da resistência à insulina.",
 "E": "A velocidade de degradação do hormônio é um ponto de regulação legítimo, porque determina por quanto tempo o sinal permanece atuando sobre os tecidos que possuem o receptor.",
})

MC[8] = ("Um hormônio esteroide atravessa a membrana de sua célula-alvo. A sequência de eventos que leva desse momento até a mudança de fenótipo celular é:", {
 "A": "o hormônio liga o receptor citoplasmático, a chaperona se solta, dois complexos formam um dímero que reconhece o elemento de resposta no DNA e recrutam coativadores, ligando a transcrição.",
 "B": "o hormônio ativa uma proteína G da face interna da membrana, elevando o AMP cíclico, e a PKA resultante fosforila fatores de transcrição que se ligam ao elemento de resposta do gene-alvo.",
 "C": "o receptor já se encontra livre no citoplasma e, ao ligar o hormônio, atua como monômero sobre o promotor do gene, dispensando dimerização e recrutamento de proteínas coativadoras adicionais.",
 "D": "o complexo hormônio-receptor permanece no citoplasma e altera diretamente a atividade das enzimas já existentes, o que explica a rapidez característica da resposta aos hormônios esteroides.",
 "E": "a chaperona acompanha o receptor até o núcleo e é ela que reconhece o elemento de resposta, cabendo ao hormônio apenas estabilizar essa ligação enquanto durar a transcrição do gene.",
})

CE[9] = ("Julgue os itens sobre os hormônios tireoidianos:", [
 ("I", "A forma que efetivamente age nos tecidos-alvo é o T4, e a conversão em T3 ocorre exclusivamente dentro da própria glândula tireoide antes da secreção."),
 ("II", "Por derivarem do aminoácido tirosina, os hormônios tireoidianos agem em receptores de membrana acoplados a proteína G, como as catecolaminas."),
 ("III", "No hipotireoidismo espera-se perda de peso, intolerância ao calor e taquicardia, pelo aumento generalizado da taxa metabólica basal."),
 ("IV", "As desiodases retiram um átomo de iodo do T4 dentro do tecido-alvo, o que dá a cada tecido controle local sobre a quantidade de hormônio ativo."),
])

MC[10] = ("Uma célula hepática foi estimulada por glucagon e, minutos depois, retorna ao estado basal mesmo com o hormônio ainda presente em concentração reduzida. O mecanismo responsável por esse desligamento é:", {
 "A": "a difusão passiva do AMP cíclico para fora da célula, que reduz sua concentração citoplasmática até o ponto em que a proteína quinase A não consegue mais permanecer no estado ativo.",
 "B": "a ação combinada da fosfodiesterase, que abre o anel do AMP cíclico, e da proteína fosfatase 1, que remove os fosfatos já pendurados nas enzimas-alvo pela cascata.",
 "C": "a internalização de todos os receptores de superfície do hepatócito, único processo capaz de encerrar a sinalização depois que a cascata de amplificação já foi disparada pelo hormônio.",
 "D": "a saturação irreversível da adenilato ciclase pelo próprio produto, que impede a formação de novas moléculas de segundo mensageiro e devolve as enzimas-alvo ao estado desfosforilado original.",
 "E": "a degradação proteolítica da proteína quinase A pelo proteassoma, processo que precisa ser seguido de nova síntese enzimática antes que a célula possa responder a um novo estímulo hormonal.",
})

# ============================================================ INTEGRAÇÃO

MC[11] = ("Uma criança apresenta hipoglicemia de jejum e hepatomegalia por deficiência da enzima que retira o fosfato da glicose-6-fosfato no fígado. Mesmo com glucagon elevado e cascata do AMP cíclico plenamente ativada, a glicemia não sobe. A explicação é que:", {
 "A": "a cascata do AMP cíclico não alcança a glicogênio fosforilase hepática, de modo que o glicogênio permanece intacto e nenhum resíduo de glicose chega a ser retirado do polímero armazenado.",
 "B": "o glucagon, sem essa enzima, passa a ativar preferencialmente a glicogênio sintase, e o fígado responde ao jejum acumulando ainda mais glicogênio em vez de mobilizar sua reserva.",
 "C": "a ausência da enzima impede a formação de AMP cíclico no hepatócito, e sem segundo mensageiro a proteína quinase A não consegue fosforilar a fosforilase que inicia a glicogenólise.",
 "D": "a cascata funciona e libera glicose-6-fosfato, mas sem a fosfatase o fígado fica na mesma situação do músculo: a carga do fosfato impede a saída, e o açúcar não alcança o sangue.",
 "E": "a fosforilase fica permanentemente presa à forma tensa por excesso de glicose livre intracelular, o que bloqueia a glicogenólise apesar de toda a sinalização hormonal estar preservada.",
})

CE[12] = ("Julgue os itens que relacionam a solubilidade do hormônio ao endereço de seu receptor e à velocidade da resposta:", [
 ("I", "A rapidez da resposta às catecolaminas decorre de sua natureza hidrossolúvel em si, e não do tipo de alvo sobre o qual a cascata termina agindo."),
 ("II", "Os hormônios tireoidianos, por derivarem de aminoácido, respondem em segundos, como os demais mensageiros de origem proteica."),
 ("III", "Um hormônio esteroide teria resposta rápida caso seu receptor estivesse na membrana, já que a lentidão é propriedade intrínseca da molécula de colesterol."),
 ("IV", "Tanto o receptor de hormônio tireoidiano quanto o de glicocorticoide terminam alterando a transcrição, e por isso ambos produzem resposta na escala de horas."),
])

MC[13] = ("Um paciente com diabetes tipo 2 e resistência periférica à insulina passa a usar sulfonilureia. O mecanismo pelo qual a droga melhora a glicemia, e a razão de ela poder causar hipoglicemia, são respectivamente:", {
 "A": "a droga aumenta a afinidade do receptor de insulina nos tecidos periféricos, corrigindo o defeito primário; a hipoglicemia surge porque a captação de glicose passa a ocorrer mesmo sem hormônio circulante.",
 "B": "a droga fecha o canal de potássio sensível ao ATP da célula beta e força a secreção; a hipoglicemia ocorre porque ela substitui o sensor de glicemia em vez de obedecê-lo.",
 "C": "a droga inibe a glicoquinase da célula beta, reduzindo o consumo de glicose pela ilhota; a hipoglicemia decorre do acúmulo de glicose-6-fosfato dentro do hepatócito durante o período de jejum.",
 "D": "a droga mantém aberto o canal de potássio da célula beta e prolonga a despolarização; a hipoglicemia resulta da entrada continuada de cálcio nas células, com exocitose sustentada dos grânulos.",
 "E": "a droga bloqueia a secreção de glucagon pelas células alfa da ilhota; a hipoglicemia aparece porque o organismo perde a principal defesa contra a queda da glicemia durante o jejum noturno.",
})

MC[14] = ("Um paciente chega ao pronto-socorro com hipoglicemia sintomática. A dosagem mostra insulina plasmática elevada e peptídeo C indetectável. A interpretação correta desse par de resultados é:", {
 "A": "há tumor de células beta secretando insulina de forma autônoma, e o peptídeo C indetectável reflete o consumo acelerado desse fragmento pelos tecidos periféricos durante o episódio de hipoglicemia.",
 "B": "há deficiência das proteases do grânulo de secreção, de modo que a pró-insulina é liberada intacta e o laboratório não consegue detectar o fragmento central da molécula no plasma.",
 "C": "há resistência periférica à insulina, e a discrepância entre os dois marcadores reflete a captação preferencial do peptídeo C pelos tecidos que perderam a capacidade de responder ao hormônio.",
 "D": "há falha do eixo hipotálamo-hipófise-adrenal, e a ausência de cortisol impede a resposta contrarreguladora, o que explica tanto a hipoglicemia quanto a queda do fragmento peptídico no plasma.",
 "E": "a insulina não veio do pâncreas do próprio paciente, pois hormônio produzido internamente sai do grânulo acompanhado de peptídeo C em quantidade equivalente, o que não ocorre com insulina administrada.",
})

MC[15] = ("Tanto a célula beta quanto o hepatócito usam glicoquinase em vez de hexoquinase. O que essa escolha comum garante a cada um dos dois tecidos é:", {
 "A": "que ambos só trabalhem em proporção à oferta: a célula beta traduz a glicemia em secreção, e o fígado captura glicose em massa apenas na abundância, sem competir com o cérebro no jejum.",
 "B": "que ambos mantenham velocidade máxima de fosforilação mesmo em glicemia baixa, o que assegura suprimento constante de glicose-6-fosfato para as duas células durante longos períodos de restrição alimentar.",
 "C": "que ambos sejam protegidos da sobrecarga de substrato pela inibição da enzima pelo próprio produto, mecanismo que impede o acúmulo tóxico de intermediários fosforilados no citoplasma dessas células.",
 "D": "que ambos possam exportar glicose livre para a circulação, já que a glicoquinase catalisa a reação nos dois sentidos conforme a concentração relativa de substrato e produto no meio intracelular.",
 "E": "que ambos independam de sinalização hormonal, pois a enzima é constitutivamente ativa e sua expressão não sofre qualquer influência da insulina ou dos demais mensageiros circulantes no plasma.",
})

CE[16] = ("Julgue os itens que relacionam os pontos de regulação hormonal aos mecanismos de droga e de doença:", [
 ("I", "A sulfonilureia atua no ponto de secreção, e por isso depende de haver células beta funcionantes remanescentes para produzir efeito."),
 ("II", "A resistência à insulina se instala no ponto de reconhecimento, com síntese e secreção do hormônio inicialmente preservadas ou até aumentadas."),
 ("III", "Um hormônio que circula predominantemente ligado a proteína carreadora tem meia-vida curta, porque a fração ligada é rapidamente depurada pelo fígado."),
 ("IV", "Um agonista do canal de potássio da célula beta age no ponto de biossíntese, reduzindo a transcrição do gene da insulina no núcleo."),
])

MC[17] = ("Comparando a regulação por modificação covalente com a regulação por expressão gênica exercida pelo cortisol, assinale a alternativa *incorreta*:", {
 "A": "A modificação covalente age sobre enzimas que já existem, razão pela qual o efeito do glucagon sobre o glicogênio aparece em segundos e não depende de síntese proteica nova.",
 "B": "O cortisol precisa que o receptor se solte da chaperona, dimerize sobre o elemento de resposta e recrute coativadores antes de qualquer proteína nova começar a ser fabricada pela célula.",
 "C": "O efeito do cortisol sobrevive à queda do hormônio no plasma, porque a proteína recém-sintetizada continua trabalhando depois que a molécula que a encomendou já foi degradada.",
 "D": "A modificação covalente é irreversível dentro da vida útil da enzima, de modo que o retorno ao estado basal exige degradação da proteína fosforilada e síntese de uma cópia nova.",
 "E": "As duas formas de regulação convivem no mesmo tecido, e o cortisol pode alterar a quantidade de enzimas cuja atividade é ajustada minuto a minuto pela fosforilação.",
})

MC[18] = ("Durante uma corrida, a adrenalina eleva o AMP cíclico tanto no hepatócito quanto na fibra muscular esquelética. O destino da glicose mobilizada difere entre os dois tecidos porque:", {
 "A": "a fibra muscular não expressa glicogênio fosforilase e depende inteiramente da glicose exportada pelo fígado, o que torna a mobilização hepática a única fonte de combustível durante o exercício.",
 "B": "o músculo não possui glicose-6-fosfatase, e a glicose-6-fosfato retirada do seu glicogênio permanece presa na célula e é oxidada localmente; apenas o fígado exporta glicose livre para o sangue.",
 "C": "o músculo converte toda a glicose-6-fosfato de volta em glicogênio assim que a adrenalina cai, enquanto o fígado a acumula na forma livre até que o glucagon determine sua liberação no plasma.",
 "D": "a fosforilase muscular responde apenas a moduladores alostéricos e é insensível à fosforilação, de modo que a adrenalina age exclusivamente sobre o hepatócito durante o esforço físico intenso.",
 "E": "o fígado utiliza um transportador dependente de insulina para exportar a glicose formada, enquanto o músculo carece desse transportador e por isso retém internamente todo o açúcar que mobiliza.",
})

CE[19] = ("Julgue os itens sobre a interrupção do sinal hormonal e sua relação com a cascata que o produziu:", [
 ("I", "A fosfodiesterase encerra o sinal cortando o anel do AMP cíclico, mas não desfaz sozinha os fosfatos já ligados às enzimas-alvo."),
 ("II", "Ao ativar a proteína fosfatase 1, a insulina inativa a glicogênio fosforilase e ativa a glicogênio sintase num único movimento."),
 ("III", "Uma substância que iniba a fosfodiesterase prolonga o efeito hormonal sem que nenhuma molécula adicional de hormônio tenha chegado à célula."),
 ("IV", "O término da sinalização é um processo puramente passivo, que depende apenas da queda espontânea da concentração de hormônio no plasma."),
])

MC[20] = ("Após uma refeição rica em proteína e pobre em carboidrato, dosam-se insulina e glucagon: ambos estão elevados. A explicação fisiológica desse achado é:", {
 "A": "a refeição proteica estimula diretamente as células beta e inibe as células alfa, e a elevação simultânea observada decorre apenas do atraso na depuração hepática do glucagon secretado previamente.",
 "B": "os aminoácidos inibem a secreção de ambos os hormônios, e os valores altos refletem a liberação dos estoques pré-formados nos grânulos das duas populações celulares da ilhota pancreática.",
 "C": "a insulina elevada é resposta ao carboidrato residual da refeição, e o glucagon alto reflete a hipoglicemia já instalada, que corresponde à falha da contrarregulação nesse tipo de dieta.",
 "D": "o glucagon elevado inibe a secreção de insulina pelas células beta vizinhas, de modo que o achado indica desregulação da comunicação parácrina entre os dois tipos celulares da ilhota.",
 "E": "os aminoácidos estimulam as duas células: a insulina joga aminoácidos para dentro dos tecidos, e o glucagon simultâneo evita que a glicemia caia demais na ausência de carboidrato na refeição.",
})

MC[21] = ("Uma prostaglandina produzida numa área de inflamação age sobre as células imediatamente vizinhas, sem alcançar concentração relevante na circulação. Comparando esse mensageiro com a insulina, é correto afirmar que:", {
 "A": "a prostaglandina deriva de ácido graxo e age de modo parácrino, enquanto a insulina é peptídica e endócrina; ainda assim, ambas dependem de receptor específico na célula que vai responder.",
 "B": "a prostaglandina age de modo endócrino, porém em concentração menor, e a diferença em relação à insulina está apenas na potência do mensageiro, não no alcance ou no tipo de receptor envolvido.",
 "C": "a prostaglandina dispensa receptor por ser lipídica e atravessar livremente a membrana, ao contrário da insulina, cuja natureza peptídica exige reconhecimento por uma proteína de superfície específica.",
 "D": "ambas derivam de aminoácidos e diferem apenas na velocidade de degradação plasmática, o que faz com que uma permaneça local e a outra alcance órgãos distantes do sítio onde foi produzida.",
 "E": "a prostaglandina age como neurotransmissor por ser liberada em fenda estreita, e a insulina como hormônio clássico, de modo que os dois mensageiros pertencem a categorias funcionais distintas.",
})

CE[22] = ("Uma paciente apresenta fadiga, hipotensão e escurecimento progressivo da pele. Investigação revela destruição autoimune do córtex adrenal. Julgue os itens:", [
 ("I", "O escurecimento da pele é consequência direta do excesso de cortisol circulante sobre os melanócitos da derme."),
 ("II", "Espera-se ACTH elevado, porque a queda do cortisol remove a inibição que ele exercia sobre hipotálamo e hipófise."),
 ("III", "A hiperpigmentação se explica porque os primeiros resíduos da molécula de ACTH coincidem com o hormônio estimulante de melanócitos."),
 ("IV", "A tendência à hipoglicemia se explica pela perda do efeito do cortisol de mobilizar substrato para a produção hepática de glicose."),
])

MC[23] = ("A tireoide secreta predominantemente T4, mas o hormônio que ocupa o receptor nuclear é o T3. A consequência funcional dessa conversão ocorrer no tecido-alvo, e não na glândula, é:", {
 "A": "que a resposta ao hormônio tireoidiano passa a ocorrer em segundos, já que o T3 formado localmente encontra receptores de membrana prontos para transmitir o sinal por segundo mensageiro.",
 "B": "que a glândula perde qualquer controle sobre a intensidade da resposta, ficando a produção hormonal inteiramente determinada pela quantidade de iodo disponível na dieta do indivíduo.",
 "C": "que o T4 deixa de ter função e passa a ser considerado apenas produto de degradação, cabendo à tireoide secretá-lo somente quando a demanda periférica por T3 estiver reduzida.",
 "D": "que o T4 funciona como reservatório circulante de meia-vida longa e cada tecido regula localmente quanto hormônio ativo deseja produzir, camada de controle fora do alcance da glândula.",
 "E": "que a resposta se torna independente da transcrição gênica, pois o T3 gerado no citoplasma age diretamente sobre enzimas prontas, o que explica a rapidez do efeito sobre o gasto basal.",
})

MC[24] = ("A insulina eleva a captação de glicose pelo músculo e pelo tecido adiposo, mas não altera de modo comparável a captação pelo cérebro. A base dessa diferença é:", {
 "A": "que o cérebro capta glicose apenas na vigência de glucagon, hormônio que recruta para a membrana neuronal os transportadores responsáveis pela entrada do açúcar no tecido nervoso.",
 "B": "que a insulina age no cérebro elevando a glicoquinase neuronal, mecanismo distinto do observado no músculo, o que mantém a captação encefálica constante independentemente da glicemia.",
 "C": "que músculo e adiposo dependem do GLUT4, transportador que fica guardado em vesículas e só é recrutado para a membrana pela insulina, enquanto o cérebro usa transportadores independentes do hormônio.",
 "D": "que o cérebro é o único tecido a expressar GLUT2, transportador de alta afinidade cuja saturação em glicemia basal impede qualquer aumento adicional de captação mediado por sinalização hormonal.",
 "E": "que a insulina inibe ativamente a entrada de glicose no tecido nervoso, mecanismo protetor que preserva o substrato circulante para os tecidos periféricos durante o período pós-prandial imediato.",
})

CE[25] = ("Julgue os itens sobre amplificação, afinidade do receptor e interferência ambiental na sinalização hormonal:", [
 ("I", "A amplificação da cascata é aditiva: cada degrau soma um número fixo de moléculas ao efeito produzido pelo degrau anterior."),
 ("II", "A alta afinidade do receptor é dispensável, pois a amplificação em cascata compensa integralmente qualquer falha na detecção do hormônio."),
 ("III", "Um disruptor endócrino pode ocupar o receptor sem ativá-lo, impedindo que o hormônio verdadeiro produza sua resposta."),
 ("IV", "A mesma alta afinidade que permite detectar concentrações nanomolares torna o sistema vulnerável a moléculas ambientais de formato semelhante."),
])

# ============================================================ APLICAÇÃO

MC[26] = ("Um homem saudável está em jejum há dezoito horas. Sobre o estado hormonal e metabólico esperado, assinale a alternativa *incorreta*:", {
 "A": "A glicogênio sintase hepática encontra-se predominantemente desfosforilada e ativa, de modo que o fígado segue incorporando glicose ao seu estoque de glicogênio ao longo de todo o período de jejum.",
 "B": "O glucagon está elevado e a razão insulina/glucagon está baixa, situação que favorece a fosforilação das enzimas hepáticas do metabolismo do glicogênio pela proteína quinase A.",
 "C": "A glicogênio fosforilase hepática está predominantemente na forma fosforilada e ativa, mobilizando glicose do estoque para sustentar a glicemia dos tecidos que dela dependem.",
 "D": "A captação de glicose pelo músculo e pelo tecido adiposo está reduzida, porque o GLUT4 permanece retido em vesículas na ausência de estímulo suficiente pela insulina.",
 "E": "O fígado consegue exportar glicose livre para o sangue porque dispõe de glicose-6-fosfatase, enzima que o músculo não possui e cuja ausência prende o açúcar dentro da fibra muscular.",
})

CE[27] = ("Uma mulher de 34 anos, sem diabetes, tem episódios repetidos de confusão que melhoram após ingerir açúcar. Durante um episódio: glicemia 38 mg/dL, insulina alta e peptídeo C alto. Julgue os itens:", [
 ("I", "O peptídeo C alto indica que a insulina circulante foi produzida pelo próprio pâncreas da paciente."),
 ("II", "O quadro é compatível com uso indevido de insulina exógena, já que o peptídeo C acompanha a insulina administrada por via subcutânea."),
 ("III", "Um tumor de células beta secretando de forma autônoma explica a hipoglicemia com insulina inapropriadamente elevada."),
 ("IV", "Enquanto a cirurgia não é realizada, um fármaco que mantenha aberto o canal de potássio da célula beta reduz a secreção do hormônio."),
])

MC[28] = ("Um idoso com diabetes tipo 2 em uso de sulfonilureia pulou o almoço e foi encontrado sonolento e sudoreico, com glicemia capilar de 42 mg/dL. O mecanismo que explica esse episódio é:", {
 "A": "a droga reduziu a afinidade do receptor de insulina nos tecidos periféricos, o que aumentou a captação de glicose pelo músculo e pelo tecido adiposo mesmo na ausência de refeição.",
 "B": "a droga bloqueou a glicogenólise hepática ao inibir a proteína quinase A, impedindo que o fígado respondesse ao glucagon liberado durante o intervalo prolongado entre as refeições do dia.",
 "C": "a droga estimulou as células alfa da ilhota a secretar glucagon em excesso, o que consumiu rapidamente o estoque hepático de glicogênio e deixou o paciente sem reserva para o jejum.",
 "D": "a droga mantém o canal de potássio fechado e a secreção de insulina continua mesmo sem glicose chegando, porque ela substitui o sensor da célula beta em vez de obedecer à glicemia.",
 "E": "a droga induziu a expressão de glicoquinase no tecido muscular, o que aumentou o consumo periférico de glicose a ponto de superar a capacidade hepática de repor o açúcar circulante.",
})

MC[29] = ("Uma paciente em uso de prednisona há oito meses interrompeu a medicação por conta própria e, dois dias depois, apresentou fraqueza intensa, hipotensão e hipoglicemia. O mecanismo do quadro é:", {
 "A": "reação alérgica tardia ao corticoide, com liberação de mediadores inflamatórios que produzem vasodilatação sistêmica e consumo periférico acelerado de glicose pelos tecidos comprometidos.",
 "B": "excesso persistente de glicocorticoide armazenado no tecido adiposo, que continua sendo liberado após a suspensão e produz os achados típicos da síndrome de hipercortisolismo prolongado.",
 "C": "destruição autoimune aguda do córtex adrenal desencadeada pela retirada da medicação, com ACTH baixo e hiperpigmentação cutânea instalando-se ao longo das primeiras quarenta e oito horas.",
 "D": "supressão prolongada do eixo pela retroalimentação negativa, com atrofia do córtex adrenal; retirada a fonte externa, a produção própria ainda não consegue assumir e falta cortisol de imediato.",
 "E": "resistência periférica ao cortisol induzida pelo uso prolongado, de modo que o hormônio endógeno, embora produzido em quantidade normal, não consegue exercer seus efeitos sobre os tecidos-alvo.",
})

CE[30] = ("Um homem de 28 anos procura atendimento por perda de 9 kg em três meses, palpitações, tremor de extremidades, intolerância ao calor e insônia. O apetite está aumentado. Julgue os itens:", [
 ("I", "O conjunto dos achados é compatível com elevação da taxa metabólica basal por excesso de hormônio tireoidiano."),
 ("II", "A perda de peso apesar do apetite aumentado contraria a hipótese de hipertireoidismo e sugere causa exclusivamente psiquiátrica."),
 ("III", "O receptor envolvido é nuclear, e a resposta aos hormônios tireoidianos se instala ao longo de dias, não de segundos."),
 ("IV", "Espera-se que as desiodases dos tecidos-alvo continuem convertendo T4 em T3, ampliando localmente o efeito do excesso circulante."),
])

# ---------------------------------------------------------------- paridade
_TYPST = re.compile(r"[*_#]|\\")


def count_words(t):
    return len(_TYPST.sub("", t).split())


def relatorio():
    linhas = []
    fora = 0
    for n in sorted(MC):
        alts = MC[n]
        correta = GAB[n]
        wc = count_words(alts[1][correta])
        dis = [count_words(v) for k, v in alts[1].items() if k != correta]
        mx = max(dis)
        med = sorted(dis)[len(dis) // 2]
        r = wc / mx
        rmed = wc / med
        ok = 0.80 <= r <= 1.25
        if not ok:
            fora += 1
        linhas.append(
            f"Q{n:02d} — correta={correta} {wc}p · distratoras={sorted(dis)} · "
            f"maior={mx} · ratio={r:.2f} · ratio_mediana={rmed:.2f} → "
            f"{'PASS' if ok else ('FAIL curta' if r < 0.80 else 'FAIL longa')}")
    return linhas, fora


# ---------------------------------------------------------------- emissao
def esc(t):
    return t


def emit():
    out = ['#import "../typst-template/nebli_v2_apostila.typ": *', ""]
    for n in range(1, 31):
        badge = BADGE[n]
        if n in MC:
            enun, alts = MC[n]
            out.append(f'#questao-mc("{n:02d}", {badge},')
            out.append(f'  [{esc(enun)}],')
            pares = []
            for L in "ABCDE":
                pares.append(f'   ("{L}", [{esc(alts[L])}])')
            out.append("  (" + ",\n".join(pares).lstrip() + "))")
        else:
            enun, itens = CE[n]
            out.append(f'#questao-ce("{n:02d}", {badge},')
            out.append(f'  [{esc(enun)}],')
            pares = [f'   ("{m}", [{esc(t)}])' for m, t in itens]
            out.append("  (" + ",\n".join(pares).lstrip() + "))")
        out.append("")
    OUT.write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    assert len(MC) + len(CE) == 30, f"{len(MC)} MC + {len(CE)} CE"
    for n, g in GAB.items():
        if n in CE:
            assert len(g) == 4 and set(g) <= {"C", "E"}, f"Q{n} gabarito CE invalido"
            assert len(CE[n][1]) == 4, f"Q{n} precisa de 4 itens"
        else:
            assert g in "ABCDE" and len(g) == 1, f"Q{n} gabarito MC invalido"
    emit()
    linhas, fora = relatorio()
    print(f"ok {OUT}  ({len(MC)} MC + {len(CE)} C/E)")
    print("\n".join(linhas))
    print(f"\nMC fora da banda 0.80-1.25: {fora}/{len(MC)}")
