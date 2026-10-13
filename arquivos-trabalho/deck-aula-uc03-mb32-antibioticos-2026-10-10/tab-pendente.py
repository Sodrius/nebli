"""Completa manualmente nove Tabs interrompidos pela cota do gerador; sem tocar a coleção."""
from datetime import datetime, timezone

from nebli.decks import Anki
from nebli.explicacoes import STYLE, item, open_store, problema_estilo, style_version

TEXT = {
1791668523738: """Base: suscetibilidade significa que um antibiótico ainda consegue inibir uma bactéria nas condições interpretadas pelo laboratório. Antibióticos são agrupados em categorias; vários medicamentos da mesma categoria não equivalem a várias categorias diferentes.
Base: XDR, ou resistência extensiva, indica que a bactéria perdeu a suscetibilidade em quase todas as categorias avaliáveis para ela.
Por quê: a definição padronizada considera XDR quando o isolado não é suscetível a pelo menos um agente de todas as categorias, exceto uma ou duas. Restam, portanto, apenas uma ou duas categorias nas quais ainda existem opções potencialmente ativas.
Por quê: isso pode ocorrer porque a bactéria acumula diferentes mecanismos de resistência, como enzimas que degradam drogas, alterações de alvos e barreiras de entrada. Cada mecanismo pode retirar mais uma opção do tratamento.
Mais a fundo: a categoria disponível não garante que todo medicamento dela funcionará, nem que alcance o local da infecção. A escolha final depende do antibiograma e do contexto clínico.
Na aula: XDR aprofunda a escala apresentada após MDR e mostra por que preservar as opções terapêuticas importa.
Não confundir: MDR exige perda de suscetibilidade em pelo menos três categorias; PDR significa perda em todas as categorias.""",
1791668523615: """Base: resistência significa que a bactéria não é adequadamente inibida por um antibiótico nas condições usadas para interpretar o teste. Um mesmo grupo de antibióticos forma uma categoria quando seus membros compartilham propriedades relevantes.
Base: MDR, ou multirresistência, descreve um padrão de resistência adquirida que alcança várias categorias, e não simplesmente muitos comprimidos diferentes.
Por quê: se pelo menos um agente de cada uma de três categorias ou mais não funciona contra o isolado, a bactéria satisfaz a definição padronizada de MDR. Contar três medicamentos da mesma categoria como três categorias inflaria artificialmente o resultado.
Por quê: mutações e genes transferidos podem alterar alvos, destruir drogas ou reduzir sua entrada. A pressão seletiva do uso de antibióticos favorece os microrganismos que reúnem esses mecanismos.
Mais a fundo: MDR não diz que todos os fármacos falharam; ainda é preciso consultar o antibiograma para saber quais opções mantêm atividade.
Na aula: a definição organiza a progressão entre resistência comum, multirresistência e perfis ainda mais extensos.
Não confundir: XDR restringe a suscetibilidade a apenas uma ou duas categorias; resistência a todos os agentes de todas as categorias é PDR.""",
1791668527164: """Base: a concentração inibitória mínima, ou CIM, é a menor quantidade de antibiótico que impede crescimento visível de uma bactéria em um teste. Ausência de turbidez mostra que ela não cresceu naquela condição, mas não demonstra que morreu.
Base: a concentração bactericida mínima, ou CBM, pergunta algo diferente: qual é a menor concentração capaz de matar o microrganismo testado.
Por quê: o laboratório prepara tubos com concentrações crescentes do medicamento e observa onde o crescimento deixa de aparecer. Para distinguir inibição de morte, retira material dos tubos claros e o semeia em meio sem antibiótico.
Por quê: se ainda surgirem colônias, havia bactérias viáveis, apenas impedidas de crescer pela droga. Quando a subcultura não mostra recuperação dentro do critério do ensaio, identifica-se a concentração bactericida.
Mais a fundo: por isso a CBM costuma ser igual ou maior que a CIM; são medidas laboratoriais de efeitos relacionados, porém não equivalentes.
Na aula: o contraste entre diluição, CIM e CBM ensina a interpretar o que cada ensaio de suscetibilidade realmente mede.
Não confundir: um tubo claro isolado basta para ler a CIM, mas não prova a CBM.""",
1791668527289: """Base: no antibiograma por disco-difusão, uma placa é coberta por uma suspensão padronizada da bactéria. Discos contendo antibióticos são colocados sobre o ágar, e cada droga se difunde para fora do disco.
Base: a região sem crescimento ao redor de um disco é o halo de inibição. Seu tamanho é medido pelo diâmetro, em milímetros, atravessando o centro do disco.
Por quê: perto do disco a concentração do antibiótico é maior; ela cai à medida que a distância aumenta. A bactéria cresce onde a concentração já não impede sua multiplicação. Assim, a borda do halo transforma a interação entre droga e isolado em uma medida observável.
Por quê: o laboratório compara esse diâmetro com pontos de corte próprios para a combinação de bactéria e antibiótico. A categoria relatada resulta dessa comparação, não da impressão visual de que o círculo parece grande.
Mais a fundo: inóculo, meio, incubação e quantidade de droga no disco precisam ser padronizados para que os diâmetros sejam comparáveis.
Na aula: Kirby–Bauer aparece como o método de disco-difusão que converte um halo medido em interpretação de suscetibilidade.""",
1791668527413: """Base: um halo de inibição é a área em torno do disco de antibiótico onde a bactéria não cresceu. A droga sai do disco e sua concentração diminui com a distância.
Por quê: para a mesma droga testada nas mesmas condições, um isolado mais suscetível pode ser impedido de crescer mesmo mais longe do disco. Por isso a borda de crescimento se desloca para fora e o diâmetro do halo tende a ser maior.
Por quê: um isolado menos suscetível consegue crescer mais perto do disco e tende a produzir um halo menor. Essa relação é inversa à da CIM: em geral, uma CIM menor significa que menos droga basta para inibir o crescimento.
Mais a fundo: o diâmetro só ganha categoria clínica ao ser confrontado com pontos de corte para aquela espécie e aquele antibiótico. Não se deve comparar diretamente o tamanho de halos de antibióticos diferentes para decidir qual é melhor.
Na aula: a leitura dos halos liga o método de Kirby–Bauer ao raciocínio de suscetibilidade que também aparece na CIM.
Não confundir: halo maior é uma tendência dentro de condições comparáveis, não uma regra universal entre discos diferentes.""",
1791668527539: """Base: um antibiograma informa quais antibióticos podem agir contra a bactéria isolada. O laboratório pode testar mais medicamentos do que convém mostrar de rotina no laudo.
Base: o agrupamento A, B e C organiza a seleção e o relato dos agentes segundo utilidade habitual e critérios de laboratório; não mede a intensidade da resistência de uma bactéria.
Por quê: os agentes do grupo A representam escolhas principais para teste e relato rotineiros. Ao apresentá-los primeiro, o laudo favorece opções adequadas antes de recorrer indiscriminadamente a alternativas de reserva.
Por quê: grupos B e C podem ser testados e liberados de modo seletivo, conforme o organismo, a origem da amostra, a suscetibilidade encontrada e a necessidade clínica. Assim, um resultado não exibido inicialmente não significa que o fármaco jamais tenha sido avaliado.
Mais a fundo: essa convenção de grupos depende do sistema e da tabela adotados pelo laboratório; a escolha terapêutica ainda considera foco da infecção e paciente.
Na aula: a classificação A/B/C entra na interpretação do antibiograma como ferramenta de uso racional dos antibióticos.
Não confundir: grupo A é prioridade de relato, não uma garantia de que todo isolado seja suscetível a seus medicamentos.""",
1791668527663: """Base: o teste de suscetibilidade compara a concentração necessária para inibir a bactéria com a exposição ao antibiótico que pode ser alcançada no paciente. O resultado intermediário fica entre as interpretações de suscetível em exposição habitual e resistente.
Por quê: algumas bactérias exigem uma exposição maior ao medicamento para que o tratamento tenha boa chance de êxito. Isso pode vir de um esquema de dose ajustado ou de uma concentração naturalmente alta no local da infecção.
Por quê: por esse motivo, um resultado intermediário não equivale automaticamente a falha terapêutica. Ele pede que se verifique se a exposição necessária é alcançável com segurança naquela situação clínica.
Mais a fundo: na terminologia EUCAST, a letra I significa suscetível com exposição aumentada. Tabelas e sistemas de interpretação podem empregar termos diferentes; deve-se seguir o padrão do laboratório.
Na aula: a categoria intermediária mostra por que o antibiograma é uma previsão contextual, e não uma propriedade absoluta da bactéria isolada.
Não confundir: aumentar a dose por conta própria não é a definição completa de I; via, intervalo e concentração no sítio também importam.""",
1791668527790: """Base: no teste de disco-difusão, o antibiótico sai do disco e produz uma região de menor crescimento bacteriano ao redor dele. O laboratório precisa transformar a borda dessa região em um diâmetro mensurável.
Base: às vezes aparecem duas bordas concêntricas, dando a impressão de um halo externo e outro interno. A borda adicional pode representar crescimento tênue, colônias ou interferência técnica, por isso exige leitura atenta.
Por quê: na regra ensinada para o duplo halo da aula, mede-se o diâmetro da borda interna. Ela delimita a região de inibição mais clara e evita contar a faixa externa parcial como se tivesse o mesmo grau de ausência de crescimento.
Por quê: a medida só tem valor se a placa, o inóculo e o tipo de crescimento atenderem aos critérios do método. Um padrão duvidoso pode exigir repetição ou revisão pelo laboratório.
Mais a fundo: a classificação final ainda depende dos pontos de corte próprios para o microrganismo e o antibiótico, mesmo após a leitura correta do halo.
Na aula: esse é um detalhe de controle da leitura do Kirby–Bauer, após compreender o princípio geral dos halos.""",
1791668527914: """Base: um antibiograma presume que as colônias testadas pertençam a uma cultura pura, derivada de um único tipo de bactéria. Uma colônia isolada é uma unidade separada das vizinhas, adequada para iniciar novamente a preparação do inóculo.
Base: colônias satélites dentro do halo ou sinais de cultura mista tornam difícil atribuir o crescimento a um único isolado. Nesse caso, o número obtido pode não representar a suscetibilidade da bactéria de interesse.
Por quê: se duas populações diferentes foram espalhadas na mesma placa, cada uma pode responder de modo distinto ao antibiótico. Mesmo uma população única pode produzir achados irregulares que exigem investigação.
Por quê: repetir o teste a partir de uma colônia isolada busca restabelecer a pureza da amostra e as condições padronizadas antes de interpretar halos e categorias.
Mais a fundo: crescimento no halo também pode levantar hipótese de heterorresistência, mas essa conclusão não deve ser tirada apenas da aparência da placa.
Na aula: critérios de qualidade da disco-difusão protegem contra uma interpretação falsa de resistência ou suscetibilidade.
Não confundir: repetir a leitura do mesmo halo não corrige um inóculo contaminado; é preciso voltar à colônia isolada.""",
1791668528039: """Base: a tuberculose é uma infecção por Mycobacterium tuberculosis cujo tratamento dura meses. Durante esse tempo, bactérias podem persistir e, por mutações, surgir variantes resistentes a um dos medicamentos usados.
Base: antibióticos com mecanismos de ação diferentes atingem alvos bacterianos distintos. Uma mutação que protege contra uma droga geralmente não protege automaticamente contra todas as demais.
Por quê: se apenas um fármaco é empregado e uma bactéria resistente a ele já existe ou surge, essa variante ganha vantagem e pode dominar a população. Com vários fármacos ativos ao mesmo tempo, ela ainda é atingida pelos outros.
Por quê: para escapar do esquema inteiro, a mesma linhagem precisaria reunir resistência aos componentes relevantes, evento menos provável do que resistência a um só agente. A associação reduz, portanto, a seleção de resistência durante a terapia prolongada.
Mais a fundo: combinar drogas não corrige adesão inadequada ou escolha de medicamentos sem atividade; o esquema precisa ser eficaz e seguido pelo tempo indicado.
Na aula: a tuberculose exemplifica por que o uso racional inclui associações planejadas quando o risco de seleção de resistência é alto.""",
}

if __name__ == "__main__":
    A = Anki()
    db = open_store()
    version = style_version(STYLE.read_text(encoding="utf-8"))
    stamp = datetime.now(timezone.utc).isoformat()
    cards = A("cardsInfo", cards=list(TEXT))
    if {c["cardId"] for c in cards} != set(TEXT):
        raise RuntimeError("Algum card não foi encontrado")
    for card in cards:
        payload, digest, nid = item(A, card)
        explanation = TEXT[card["cardId"]]
        if issue := problema_estilo(explanation):
            raise RuntimeError(f"{card['cardId']}: {issue}")
        db.execute("insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)",
                   (card["cardId"], nid, digest, "ok", explanation, None, version, "manual-codex", stamp))
    db.commit()
    print(f"{len(cards)} explicações atuais registradas")
