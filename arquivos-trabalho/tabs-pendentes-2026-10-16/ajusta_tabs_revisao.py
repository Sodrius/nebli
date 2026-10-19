"""Qualifica afirmações ambíguas nos Tabs sem editar os cards correspondentes."""

import time

from nebli.decks import Anki
from nebli.explicacoes import STYLE, card_hash, open_store, style_version


TEXTOS = {
    1791668527790: """No teste de difusão em ágar, o halo de inibição representa a região em que a concentração do antimicrobiano impede crescimento visível. A leitura padronizada mede o limite de inibição completa e o compara com pontos de corte definidos para a combinação específica de microrganismo, fármaco e método.

Quando aparecem dois contornos, o halo interno costuma corresponder à borda nítida de inibição total, enquanto o externo pode refletir crescimento parcial, colônias isoladas ou outro efeito de difusão. A regra de medir o halo interno só deve ser aplicada quando o protocolo daquela técnica a especifica; sem saber o teste e o agente, o desenho isolado não permite atribuir um mecanismo único.""",
    1791163031470: """O lipopolissacarídeo, ou LPS, é um componente da membrana externa das bactérias Gram-negativas. Sua porção lipídio A fica ancorada na membrana e é reconhecida pelo sistema imune inato, especialmente por TLR4, desencadeando liberação de citocinas e podendo contribuir para sepse.

Ligado ao lipídio A está o polissacarídeo central, ou core, que conecta a molécula ao antígeno O. O antígeno O também é polissacarídico, mas se projeta para fora e varia entre cepas; por isso, ao separar os três componentes, o nome preciso da região intermediária é polissacarídeo central.""",
    1791625422532: """A IL-4 organiza respostas do tipo 2: promove a diferenciação de linfócitos CD4+ em Th2, favorece troca de classe para IgE e contribui para a ativação alternativa de macrófagos. Uma vez diferenciadas, as células Th2 secretam IL-4 e reforçam esse próprio programa por retroalimentação.

Th2 é, portanto, a resposta central quando a pergunta procura a subpopulação de linfócitos T auxiliar associada à IL-4. Mastócitos, basófilos e células linfoides inatas do tipo 2 também podem produzi-la, sobretudo no início de respostas alérgicas ou contra helmintos, antes de a resposta adaptativa estar plenamente estabelecida.""",
    1791625430332: """O IFN-γ produzido por células NK, Th1 e linfócitos T citotóxicos aumenta a capacidade de apresentação de antígenos. Ele induz componentes do processamento antigênico e eleva intensamente a expressão de MHC II nas células apresentadoras profissionais, como macrófagos e células dendríticas.

Também pode induzir MHC II em diversos outros tipos celulares sob estímulo inflamatório, mas o efeito não deve ser entendido como literalmente universal. IFN-α e IFN-β, em contraste, destacam-se por aumentar MHC I nas células nucleadas, facilitando o reconhecimento de infecção viral por linfócitos T CD8+.""",
    1791625433210: """A diferenciação dos linfócitos T CD4+ é estabilizada por fatores de transcrição mestres que convertem sinais de citocinas em programas duradouros de expressão gênica. T-bet dirige o perfil Th1 e a produção de IFN-γ; GATA3 dirige Th2 e citocinas como IL-4, IL-5 e IL-13.

RORγt estabelece o programa Th17, associado à produção de IL-17 e ao recrutamento de neutrófilos. Esses circuitos também se inibem mutuamente, ajudando cada clone ativado a assumir uma função efetora coerente; nas células T reguladoras, o fator correspondente é FOXP3.""",
    1791625436032: """TGF-β pode conduzir um linfócito CD4+ virgem a destinos diferentes conforme as citocinas presentes durante a ativação. Em ambiente não inflamatório, sua ação junto à IL-2 favorece a expressão de FOXP3 e o desenvolvimento de células T reguladoras, que limitam respostas imunes.

Quando células dendríticas ativadas fornecem IL-6, o mesmo TGF-β passa a colaborar com sinais que induzem RORγt e diferenciação Th17. Assim, IL-6 funciona como a mudança de contexto que desloca o programa regulador para um programa inflamatório produtor de IL-17.""",
    1791647350071: """A lipólise no adipócito mobiliza triacilgliceróis armazenados quando há necessidade de combustível. A epinefrina liga-se a receptores β-adrenérgicos, eleva cAMP e ativa PKA, que fosforila perilipina e a lipase sensível a hormônio, facilitando o acesso às gotículas lipídicas.

Esse efeito é uma ativação aguda da maquinaria já existente, e não principalmente a indução da síntese da enzima. A epinefrina é o estímulo fisiológico direto mais bem estabelecido no tecido adiposo humano; glucagon e cortisol têm papéis diferentes e não devem ser agrupados automaticamente na mesma via.""",
    1791647350072: """O cortisol é um hormônio esteroide que entra na célula, liga-se a um receptor intracelular e modifica a expressão gênica. Em situações de estresse prolongado, ele favorece a disponibilidade de combustíveis e pode aumentar a resposta do tecido adiposo às catecolaminas.

Sua ação sobre a mobilização de gordura é lenta e permissiva, não uma ativação direta da lipase sensível a hormônio por cAMP e PKA. A fosforilação aguda dessa maquinaria é produzida sobretudo pela sinalização adrenérgica, enquanto o cortisol prepara o contexto metabólico em outra escala temporal.""",
    1791647350073: """O glucagon sinaliza por receptor acoplado a Gs, cAMP e PKA principalmente no fígado, onde estimula glicogenólise, gliconeogênese e oxidação de ácidos graxos. Essa organização ajuda a manter a glicemia durante o jejum.

No tecido adiposo humano, porém, o glucagon não é considerado um regulador fisiológico importante da lipólise. A ativação aguda da lipase sensível a hormônio é atribuída sobretudo às catecolaminas; por isso, a via bioquímica do glucagon não implica que ele tenha o mesmo peso em todos os tecidos.""",
    1791647352121: """A glicogênio sintase alonga as cadeias de glicogênio e fica mais ativa quando está desfosforilada. A insulina estimula fosfatases e inibe quinases que manteriam a enzima fosforilada, direcionando a glicose para armazenamento após uma refeição.

Esse controle combina o sinal hormonal de abundância com a disponibilidade de substrato. Assim, a insulina é o principal regulador hormonal positivo da síntese de glicogênio, especialmente em músculo e fígado, enquanto o cortisol tende a antagonizar a ação periférica da insulina em vez de integrar esse grupo de ativadores.""",
    1791647352122: """A glicose-6-fosfato liga-se alostericamente à glicogênio sintase e aumenta sua atividade. Quando a glicose entra na célula em quantidade superior à demanda glicolítica imediata, esse metabólito sinaliza disponibilidade de substrato e favorece seu armazenamento como glicogênio.

A regulação alostérica pela glicose-6-fosfato coopera com a ativação por desfosforilação promovida pela insulina. O cortisol não é um ativador positivo clássico da glicogênio sintase muscular: sua ação sistêmica é contrarreguladora e favorece a disponibilidade de combustível durante o estresse.""",
    1791762418274: """A eficácia descreve o maior efeito que um fármaco consegue produzir e é representada pelo platô da curva dose–resposta, convencionalmente chamado Emax. Já a potência indica quanto fármaco é necessário para obter determinado efeito e costuma ser comparada pela EC50.

O card usa Vmax para esse efeito máximo, uma notação que pode aparecer informalmente no material, mas que em farmacologia é menos precisa que Emax. Vmax é reservada com frequência à velocidade máxima da cinética enzimática; aqui, a ideia correta a reter é que a altura máxima da resposta informa a eficácia, não a potência.""",
    1791762421523: """A exposição repetida a um fármaco pode reduzir sua resposta por adaptação de receptores, mudanças na sinalização celular ou aumento de sua eliminação. Quando essa perda se desenvolve ao longo de dias ou semanas, o termo geral é tolerância; quando aparece rapidamente, em minutos ou após poucas doses, é chamada taquifilaxia.

Refratariedade pode ser usada em contextos clínicos para indicar que uma doença ou um paciente deixou de responder ao tratamento, mas não é o nome farmacológico mais geral para a perda gradual descrita. O mecanismo temporal aponta principalmente para tolerância, e a rapidez distingue esse fenômeno da taquifilaxia.""",
    1791780345306: """O exsudato se forma quando inflamação aumenta a permeabilidade vascular, permitindo a saída de proteínas e células para o espaço extravascular. Como contém mais células e proteínas que um transudato, costuma apresentar atividade de LDH relativamente elevada.

Nos derrames pleurais, a interpretação usa comparação com o soro: razão LDH do líquido/LDH sérica acima de 0,6 ou LDH do líquido acima de dois terços do limite superior sérico favorece exsudato. “Aumentada” significa elevada em relação a esses critérios, não necessariamente maior que o valor absoluto do soro.""",
    1791780346430: """A gravidade específica estima quanto material dissolvido existe em um líquido. Exsudatos são ricos em proteínas e células por causa do aumento inflamatório da permeabilidade vascular, por isso tendem a ser mais densos que transudatos.

O corte tradicional é gravidade específica acima de 1,020 para exsudato; a escrita “1020” omite a vírgula decimal. Hoje a classificação de derrame pleural é feita preferencialmente pelos critérios de Light, pois a densidade isolada é menos confiável.""",
    1791647347996: """A PFK-1 controla uma etapa comprometida da glicólise e responde ao estado energético da célula. ATP e citrato sinalizam abundância de energia e a inibem; AMP sinaliza baixa carga energética e favorece sua atividade.

A frutose-2,6-bisfosfato também ativa fortemente a PFK-1 e integra a glicólise ao controle hormonal. AMP e frutose-2,6-bisfosfato são, portanto, ativadores alostéricos, não exemplos de feedback positivo no sentido estrito.""",
    1791647354296: """A célula β pancreática precisa detectar a glicose sanguínea para ajustar a secreção de insulina. A entrada de glicose, seu metabolismo e o aumento da razão ATP/ADP fecham canais de K+ sensíveis a ATP, despolarizam a membrana e promovem entrada de Ca2+ e exocitose de insulina.

Nos modelos clássicos com roedores, o GLUT2 faz a entrada de glicose e funciona como parte desse sensor por sua alta capacidade. Em células β humanas, GLUT1 e GLUT3 têm participação importante e o GLUT2 é menos expresso; a associação exclusiva com GLUT2 é uma simplificação do modelo experimental.""",
    1791647354421: """Nas primeiras horas entre refeições, o fígado degrada seu glicogênio e libera glicose para sustentar a glicemia. Essa glicogenólise hepática atende sobretudo tecidos dependentes de glicose, como hemácias, e ajuda a manter o suprimento cerebral.

Ela é a principal fonte de glicose circulante nesse período, mas não o único combustível energético do organismo. O tecido adiposo libera ácidos graxos, e muitos tecidos aumentam sua oxidação para poupar glicose.""",
    1791647354671: """Após cerca de um dia de jejum, o glicogênio hepático está muito reduzido e a gliconeogênese passa a sustentar a maior parte da glicose sanguínea. O fígado, e progressivamente o rim, convertem lactato, glicerol e aminoácidos glicogênicos em glicose.

Gliconeogênese é a principal fonte de glicose entre um e três dias de jejum, não a principal fonte de toda a energia corporal. Muitos tecidos obtêm ATP principalmente da oxidação de ácidos graxos, enquanto a glicose é preservada para tecidos com maior dependência dela.""",
    1791729320762: """Insulina promove a translocação de GLUT4 de vesículas intracelulares para a membrana de músculo esquelético e tecido adiposo. No jejum, a queda da insulina mantém a maior parte do GLUT4 dentro da célula e reduz intensamente a captação estimulada de glicose.

A captação não se torna absolutamente zero: existe transporte basal, e a contração muscular pode recrutar GLUT4 por uma via parcialmente independente de insulina. O efeito metabólico central é captar muito menos glicose e priorizar outros combustíveis.""",
    1791729320888: """Durante o jejum, a baixa insulina reduz a captação dependente de GLUT4 no músculo e no tecido adiposo. Isso ajuda a reservar a glicose para tecidos com necessidade contínua e transportadores independentes de insulina, como cérebro, hemácias e medula renal.

Esses são exemplos de tecidos fortemente dependentes de glicose, não uma lista exclusiva de quem pode captá-la. Fígado, córtex renal e outros órgãos também possuem transportadores independentes de insulina; o que muda é a prioridade metabólica e a intensidade do uso de glicose.""",
    1791729324361: """O diabetes tipo 1 resulta da destruição autoimune das células β e produz deficiência absoluta de insulina. A apresentação clássica ocorre na infância ou adolescência, muitas vezes com poliúria, polidipsia, perda de peso e risco de cetoacidose.

Início antes dos 20 anos e aspecto magro ajudam a reconhecer o padrão clássico, mas não são critérios obrigatórios. A doença pode começar em qualquer idade, inclusive em adultos, e o estado corporal varia entre as pessoas.""",
    1791729324486: """O diabetes tipo 2 combina resistência à ação da insulina com falência progressiva das células β. Excesso de adiposidade, sedentarismo, idade e predisposição genética aumentam o risco, e a instalação costuma ser gradual.

Começar após os 40 anos em uma pessoa com obesidade descreve o padrão clássico, não uma fronteira diagnóstica. A doença também ocorre em adultos jovens, adolescentes e pessoas sem obesidade; o mecanismo metabólico é mais informativo que o estereótipo de idade ou corpo.""",
    1790980019633: """A absorção de vitamina B12 depende da liberação da vitamina dos alimentos pelo ácido e pela pepsina, da ligação ao fator intrínseco produzido pelas células parietais e da absorção do complexo no íleo terminal. Cirurgias que reduzem a função gástrica podem prejudicar vários desses passos.

Tanto o bypass em Y de Roux quanto a gastrectomia vertical podem favorecer deficiência de B12, embora sejam técnicas diferentes: o primeiro desvia segmentos do tubo digestório, enquanto o sleeve apenas reduz o volume do estômago. O termo abrangente correto é cirurgia bariátrica, não “bypass” para ambas.""",
    1790980019634: """O estômago contribui para a absorção de vitamina B12 ao fornecer ácido, pepsina e fator intrínseco. A redução da massa e da função gástrica diminui a liberação da vitamina alimentar e pode reduzir o fator intrínseco disponível, favorecendo deficiência ao longo do tempo.

O Y de Roux é um bypass gástrico; a gastrectomia vertical, ou sleeve, restringe o estômago sem criar um desvio intestinal. Os dois procedimentos pertencem à cirurgia bariátrica e podem afetar a B12, mas apenas o primeiro deve ser chamado de bypass.""",
    1790981518578: """As anastomoses portossistêmicas são comunicações entre tributárias da veia porta e veias da circulação sistêmica. No esôfago inferior, a veia gástrica esquerda pertence ao território portal, enquanto as veias esofágicas drenam para o sistema ázigos, que termina na veia cava superior.

Quando a pressão portal aumenta, o sangue pode ser desviado por essa comunicação e dilatar as veias submucosas do esôfago, formando varizes. O trajeto sistêmico relevante é esofágicas → ázigos → veia cava superior; a veia cava inferior não recebe diretamente a ázigos.""",
    1792175891607: """Fungos dimórficos ambientais crescem como bolor fora do hospedeiro e assumem outra forma nos tecidos. A escolha do antifúngico depende do agente, do local, da intensidade dos sintomas e do risco do hospedeiro; formas graves ou disseminadas frequentemente exigem anfotericina B inicial.

O itraconazol é uma opção oral importante para várias formas localizadas ou leves a moderadas, incluindo esporotricose e formas selecionadas de histoplasmose, blastomicose e paracoccidioidomicose. A associação serve como regra geral para doença localizada, mas não substitui as indicações próprias de cada micose.""",
    1791746129003: """A coagulase converte fibrinogênio em fibrina e é um marcador clássico de virulência e identificação de Staphylococcus aureus. Na rotina clínica humana, a oposição mais útil é entre S. aureus coagulase-positivo e os estafilococos coagulase-negativos mais comuns.

Essa regra é prática, não taxonômica: outras espécies, como S. pseudintermedius e S. schleiferi subsp. coagulans, também podem produzir coagulase. Portanto, “positivo” caracteriza classicamente S. aureus no contexto usual, mas “único” não vale para todo o gênero.""",
    1791746129004: """Staphylococcus aureus é o estafilococo coagulase-positivo de maior importância na microbiologia clínica humana. A enzima favorece a formação de fibrina e o teste ajuda a separá-lo dos estafilococos coagulase-negativos encontrados com frequência em amostras humanas.

A identificação não deve ser entendida como exclusividade absoluta do gênero. S. pseudintermedius e algumas outras espécies também podem ser coagulase-positivas; a associação com S. aureus é uma regra de triagem do contexto clínico habitual.""",
    1792044818052: """Sangue, líquido cerebrospinal, líquido sinovial e líquido pleural são compartimentos normalmente estéreis. O crescimento de uma bactéria nesses materiais merece atenção porque pode representar invasão de um local que não possui microbiota residente.

Isso não torna todo crescimento automaticamente verdadeiro: a coleta pode introduzir contaminantes da pele. A espécie isolada, o número de frascos ou amostras positivos, o tempo até a positividade, a técnica de coleta e o quadro clínico distinguem infecção de contaminação.""",
    1792044818557: """Na sífilis primária, Treponema pallidum multiplica-se no ponto de inoculação e produz um cancro tipicamente único, endurecido e indolor. A ausência de dor é uma característica mais definidora do que a região anatômica.

A lesão é frequentemente genital porque essa é uma via comum de transmissão, mas pode ser anal, oral ou surgir em qualquer área de contato. “Genital” descreve a localização mais comum, não uma condição obrigatória do cancro sifilítico.""",
    1792044823780: """A resistência antimicrobiana é favorecida quando a exposição ao fármaco elimina bactérias sensíveis e permite a sobrevivência e expansão das resistentes. Uso sem indicação, escolha inadequada, dose incorreta e duração desnecessariamente longa ampliam essa pressão seletiva.

O paciente deve seguir a duração prescrita, que precisa ser baseada na infecção e nas evidências atuais. MRSA resulta da seleção e disseminação populacional de linhagens resistentes de S. aureus; não é consequência automática de uma interrupção precoce isolada.""",
    1791743343033: """Para aderir firmemente ao endotélio, o leucócito precisa converter suas integrinas de um estado de baixa afinidade para um estado de alta afinidade. Quimioatraentes apresentados na superfície endotelial ativam sinais intracelulares no leucócito que promovem essa mudança conformacional e aumentam a avidez da ligação.

C5a e LTB4 participam dessa ativação e favorecem a adesão firme e a migração. O efeito central é a ativação funcional das integrinas já presentes, e não simplesmente o aumento de sua expressão na membrana.""",
    1791743343034: """LTB4 e C5a são mediadores quimiotáticos que ativam leucócitos durante o recrutamento inflamatório. Seus sinais mudam as integrinas para conformações de maior afinidade e organizam sua agregação, permitindo ligação forte aos ligantes endoteliais.

Assim, esses mediadores aumentam funcionalmente a adesão mediada por integrinas. A expressão “aumentar a expressão” simplifica em excesso o mecanismo, cujo passo decisivo é a mudança de afinidade e avidez.""",
    1791629587647: """Células B de memória são descendentes de linfócitos B ativados que persistem após a resposta e respondem com rapidez a um novo encontro com o antígeno. Muitas passaram pela reação do centro germinativo e exibem imunoglobulinas de alta afinidade após troca de classe.

Por isso, IgG, IgA ou IgE de superfície são frequentes em células B de memória, mas não as definem universalmente. Também existem populações de memória IgM, com ou sem IgD; o traço essencial é a memória imunológica, não um isótipo único.""",
    1791629588272: """As regiões variáveis das cadeias pesada e leve formam o sítio de ligação ao antígeno, chamado parátopo. Diferenças de sequência nessas regiões, sobretudo nas alças hipervariáveis, determinam quais estruturas moleculares podem ser reconhecidas.

O idiotipo é o conjunto de determinantes antigênicos próprios dessas regiões variáveis. Elas ficam no fragmento Fab, mas Fab também contém domínios constantes; portanto, a formulação mais precisa liga o idiotipo à região variável e o reconhecimento do antígeno ao parátopo.""",
    1791629588273: """Cada imunoglobulina possui particularidades nas regiões variáveis que podem ser reconhecidas como determinantes antigênicos; o conjunto desses determinantes constitui o idiotipo. Próximo a eles, o parátopo é a superfície que efetivamente se liga ao antígeno.

Ambos estão na porção variável contida no Fab, mas não são sinônimos de todo o fragmento Fab. O Fab inclui também regiões constantes, enquanto o idiotipo se refere às características particulares das regiões variáveis.""",
    1791629588872: """O receptor de antígeno da maioria dos linfócitos T é um heterodímero formado por uma cadeia α e uma cadeia β. As duas cadeias contribuem para um único sítio de reconhecimento, por isso o TCR é funcionalmente monovalente e reconhece peptídeo associado ao MHC.

Há também uma população distinta de linfócitos T com receptor formado por cadeias γ e δ. Assim, αβ descreve o TCR convencional e majoritário, mas não todos os linfócitos T.""",
    1791629590723: """O receptor do linfócito B é uma imunoglobulina ligada à membrana, associada às proteínas sinalizadoras Igα e Igβ. A arquitetura das imunoglobulinas permite alguma flexibilidade entre os braços que ligam antígeno e a porção constante.

Uma região de dobradiça clássica existe em algumas classes, como IgG, IgA e IgD. IgM e IgE usam um domínio constante adicional em vez dessa dobradiça; portanto, a flexibilidade não deve ser atribuída a uma estrutura idêntica em todo BCR.""",
    1791629591022: """Em uma população policlonal de células B, cadeias leves κ costumam ser mais frequentes que cadeias λ. Em muitos tecidos humanos a proporção é aproximadamente 2:1, embora valores próximos de 3:1 possam aparecer conforme o material, o método e o intervalo adotado pelo laboratório.

Uma restrição intensa a apenas κ ou apenas λ sugere expansão clonal, mas não existe um único corte universal. A interpretação deve considerar o tipo de amostra e os limites validados pelo método, especialmente porque a razão sérica de cadeias leves livres segue referências próprias.""",
    1791629591820: """A IgA circulante no sangue é predominantemente monomérica. Nas mucosas, plasmócitos produzem IgA principalmente como dímero, cujos monômeros são unidos pela cadeia J; essa forma liga-se ao receptor de imunoglobulina polimérica para atravessar o epitélio.

Durante o transporte, parte do receptor permanece ligada como componente secretor, protegendo a IgA contra proteólise. Portanto, o dímero com cadeia J caracteriza sobretudo a IgA secretória das mucosas, não toda IgA existente no organismo.""",
    1791629592997: """Na resposta dependente de linfócito T, a ativação do B começa quando o antígeno se liga ao BCR. O complexo é internalizado, degradado e seus peptídeos são exibidos em MHC II na superfície da célula B.

Um linfócito T auxiliar reconhece o complexo peptídeo–MHC II pelo TCR e fornece sinais como CD40L e citocinas. A apresentação em MHC II é, portanto, essencial para a cooperação T–B, mas ocorre depois do reconhecimento inicial do antígeno pelo BCR.""",
    1791629593245: """A vacina contra Haemophilus influenzae tipo b liga o polissacarídeo capsular PRP a uma proteína carreadora. Essa conjugação permite que a célula B apresente peptídeos da proteína a linfócitos T auxiliares, produzindo memória e resposta eficaz mesmo em crianças pequenas.

As formulações podem usar toxoide tetânico, CRM197 derivada da toxina diftérica, toxoide diftérico ou proteína de membrana externa meningocócica. Dizer apenas “toxóide diftérico” descreve algumas formulações, mas a proteína mais usada varia com a vacina e o local.""",
    1791629594473: """A especificidade inicial dos anticorpos nasce principalmente da recombinação V(D)J durante o desenvolvimento do linfócito B, somada à diversidade das junções e à combinação entre cadeias pesada e leve. Isso produz receptores capazes de reconhecer muitos antígenos antes da exposição.

Após a ativação, a hipermutação somática introduz variantes nas regiões variáveis. A seleção das células que adquiriram ligação mais forte gera maturação da afinidade; o processo refina a especificidade existente, em vez de ser sua fonte inicial exclusiva.""",
    1791629594474: """A hipermutação somática ocorre após a ativação do linfócito B e cria mutações pontuais nas regiões variáveis das imunoglobulinas. Algumas variantes ligam o antígeno com maior força e recebem sinais de sobrevivência no centro germinativo.

A seleção repetida dessas células constitui a maturação da afinidade. A especificidade básica já havia sido produzida pela recombinação V(D)J; a hipermutação e a seleção refinam o reconhecimento e elevam a afinidade média da resposta.""",
    1790974697906: """A drenagem linfática acompanha os vasos e muda conforme o segmento. O reto superior acompanha os vasos retais superiores até linfonodos mesentéricos inferiores, enquanto o reto médio e inferior drena principalmente para linfonodos ilíacos internos.

No canal anal, a linha pectínea separa territórios: acima dela, a drenagem segue sobretudo para ilíacos internos; abaixo, segue para inguinais superficiais. Portanto, “ilíacos internos” é preciso para o canal anal acima da linha, mas “reto acima da linha” exige distinguir a porção retal.""",
}


def main():
    anki = Anki()
    cards = {card["cardId"]: card for card in anki("cardsInfo", cards=list(TEXTOS))}
    db = open_store()
    version = style_version(STYLE.read_text(encoding="utf-8"))
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    for card_id, texto in TEXTOS.items():
        card = cards[card_id]
        ordered = [field["value"] for field in sorted(card["fields"].values(), key=lambda field: field["order"])]
        db.execute(
            "insert or replace into explicacoes values (?,?,?,?,?,?,?,?,?)",
            (card_id, card["note"], card_hash(ordered, card["ord"]), "ok", texto, None,
             version, "curadoria-codex", stamp),
        )
    db.commit()
    print(f"{len(TEXTOS)} Tabs qualificados sem alterar os cards.")


if __name__ == "__main__":
    main()
