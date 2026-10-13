"""Revisão do suporte após leitura dos parágrafos causais e dos alvos novos."""
import json,re
from pathlib import Path
P=Path(__file__).resolve().parent
OLD=json.loads((P/'tabs-before.json').read_text())
NIDS={n['noteId'] for n in json.loads((P/'snapshot.json').read_text())}
TABS={}
for key,t in OLD.items():
    if t['note_id'] not in NIDS or not t.get('texto'): continue
    text=t['texto']
    if re.search(r'(?:^|\n|Por quê:)\s*1[.)]',text):
        # Existing causal sentences were read together; preserve the explanation,
        # join them into prose and remove the classroom exercise numbering.
        def prose(m):
            sentences=re.split(r'\s+\d+[.)]\s+',m[1].strip())
            out=[]
            for s in sentences:
                s=re.sub(r'^\d+[.)]\s*','',s).strip()
                if not s: continue
                if s.endswith(';'): s=s[:-1]+'.'
                s=s[0].upper()+s[1:]
                out.append(s)
            return 'Por quê: '+' '.join(out)
        text=re.sub(r'Por quê:\s*(1[.)][^\n]+)',prose,text)
        TABS[int(key)]=text

BY_NOTE={
1791054012719:'''Base: insulina é um hormônio das células beta do pâncreas que ajuda a controlar a glicose. Para agir, liga-se a um receptor na superfície das células. O receptor inicia uma cadeia de sinais dentro delas. Hiperinsulinemia significa que há muita insulina circulando; downregulation é a redução da disponibilidade de receptores.
Por quê: quando a exposição ao hormônio permanece elevada, a célula pode diminuir os receptores disponíveis. Pense numa mensagem repetida por muito tempo: a resposta celular ao estímulo é regulada, e uma das formas de regulação é reduzir os pontos que recebem essa mensagem. É essa adaptação específica que a lacuna cobra.
Mais a fundo: na obesidade, a resistência à insulina também envolve defeitos depois do receptor. Excesso de lipídios e sinais inflamatórios podem prejudicar a transmissão intracelular. Por isso, menos receptores não explica sozinho toda a doença. No músculo e no tecido adiposo, a sinalização da insulina favorece a chegada de GLUT4 à membrana; no fígado, ela regula principalmente a produção e o armazenamento de glicose.
Não confundir: resistência à insulina não significa necessariamente pouca insulina. O pâncreas pode secretar mais hormônio para compensar uma resposta reduzida dos tecidos.''',
1790999833204:'''Base: a membrana de uma célula muscular mantém uma diferença de voltagem entre seu interior e o exterior. No tubo digestivo, essa voltagem oscila em ondas lentas, ligadas à atividade das células intersticiais de Cajal. A onda lenta é uma oscilação graduada, diferente de um potencial de ação.
Por quê: acompanhe a subida da curva. A membrana fica menos negativa e se aproxima do nível necessário para ativar canais dependentes de voltagem. Quando a despolarização cruza o limiar elétrico, aparecem potenciais em espícula, ou spike potentials, sobre a onda lenta. A pergunta cobra o nome desses eventos rápidos, não o adjetivo “elétrico”.
Mais a fundo: os spikes favorecem a entrada de cálcio nas células musculares. O cálcio ativa a maquinaria contrátil, e uma maior atividade de spikes costuma produzir uma contração mais forte. A relação entre onda lenta e força depende do segmento e das propriedades das células; não transforme isso na regra absoluta de que toda onda lenta necessariamente produz, ou nunca produz, contração.
Na aula: no gráfico, separe a oscilação de voltagem, os picos rápidos sobre ela e a curva de tensão muscular abaixo. São fenômenos relacionados, mas diferentes.''',
1791023360742:'''Base: o estômago possui glândulas na mucosa, mas elas não têm a mesma composição em todas as regiões. No corpo e no fundo, são comuns células parietais, que secretam ácido e fator intrínseco, e células principais, que produzem pepsinogênio. No piloro predominam glândulas mucosas.
Por quê: compare a função dominante de cada região. As glândulas do corpo e do fundo participam intensamente da secreção necessária à digestão. A glândula pilórica típica tem maior proporção de células produtoras de muco. Por isso, em comparação com uma glândula fúndica, apresenta menos células parietais e principais. Cada irmão do card cobra um desses dois tipos celulares.
Mais a fundo: “menos” é diferente de “nenhuma”. A mucosa antral humana pode apresentar glândulas mistas com células parietais e principais. A organização regional é útil para reconhecer o padrão predominante, mas não sustenta uma ausência absoluta em toda preparação humana.
Não confundir: célula parietal produz ácido; célula principal produz pepsinogênio. Ambas podem aparecer na mesma glândula, porém têm aspectos e produtos diferentes. Use a distribuição das glândulas e o conjunto das células para reconhecer a região, sem depender de uma única célula isolada.''',
1791023256867:'''Base: células parietais são as células do estômago que secretam ácido. Elas recebem sinais nervosos e químicos. Entre os sinais químicos estão a histamina, liberada pelas células ECL, e a gastrina, produzida pelas células G, principalmente no antro.
Por quê: a histamina sai de uma célula ECL e alcança células parietais próximas. Ao ativar receptores H2, favorece a secreção ácida. Como age localmente sobre células vizinhas, seu modo de ação é chamado parácrino. A gastrina percorre outro caminho: entra no sangue e chega à mucosa do corpo e fundo. Esse transporte pela circulação caracteriza um hormônio endócrino.
Mais a fundo: a gastrina também estimula as células ECL a liberar histamina. Assim, os dois sinais podem participar da mesma sequência, mesmo tendo origens e formas de transporte distintas. Não é necessário escolher um único estimulador para explicar toda a produção de ácido; a célula parietal integra vários estímulos.
Na aula: ao lembrar histamina, associe ECL e ação local. Ao lembrar gastrina, associe célula G e transporte pelo sangue. O card antigo chamava os dois sinais de parácrinos; essa formulação foi corrigida porque confundia a via de chegada da gastrina.''',
1791054007769:'''Base: glicemia é a concentração de glicose no sangue. Uma medida aleatória pode ser colhida a qualquer hora, independentemente de jejum. Diabetes mellitus envolve hiperglicemia persistente; seus sintomas clássicos incluem urinar muito, sentir muita sede e perder peso sem explicação.
Por quê: quando esses sintomas estão presentes e a glicemia plasmática aleatória é igual ou superior a 200 mg/dL, o conjunto permite estabelecer o diagnóstico de diabetes. O número não deve ser lembrado separado do contexto: uma elevação isolada em alguém sem sintomas não tem a mesma interpretação de uma medida acompanhada de manifestações típicas.
Mais a fundo: sem hiperglicemia inequívoca, o diagnóstico precisa de confirmação apropriada. Essa confirmação pode usar testes como glicemia de jejum, hemoglobina glicada ou teste oral de tolerância à glicose, conforme o caso. Não basta substituir isso pela regra de que qualquer glicemia aleatória elevada em duas ocasiões resolve toda dúvida diagnóstica.
Não confundir: esse critério diagnostica diabetes, mas não determina sozinho se é tipo 1 ou tipo 2. A classificação depende do contexto clínico e, quando necessário, de investigação adicional. Neste card, recupere o limiar de 200 mg/dL mantendo a condição dos sintomas em mente.''',
1791163038218:'''Base: uma bactéria possui um cromossomo e pode carregar plasmídeos, pequenas moléculas de DNA que se replicam separadamente. O plasmídeo F contém genes que permitem a transferência de DNA por conjugação. Uma célula F positiva possui esse plasmídeo; uma célula F negativa não o possui.
Por quê: a bactéria doadora estabelece contato com a receptora e monta a maquinaria de transferência. Uma das fitas do plasmídeo é encaminhada à outra célula enquanto a síntese de DNA repõe e completa as fitas necessárias. Ao final da conjugação comum entre F positiva e F negativa, a receptora pode adquirir uma cópia funcional do plasmídeo F.
Mais a fundo: isso explica por que a resposta é plasmídeo, e não cromossomo, nesse tipo de cruzamento. Entretanto, a conjugação bacteriana não está limitada a essa situação. Se o fator F se integra ao cromossomo, a doadora pode tornar-se uma célula Hfr, capaz de iniciar a transferência de sequências cromossômicas durante a conjugação.
Não confundir: conjugação envolve contato entre bactérias e transferência de DNA. Transformação envolve captar DNA livre do ambiente; transdução envolve um bacteriófago. O card especifica F positiva × F negativa para que a resposta não seja ambígua.''',
1791000311952:'''Base: o ferro dos alimentos pode estar associado a estruturas diferentes. Heme é um complexo em que um átomo de ferro ocupa o centro de um anel orgânico chamado porfirina. Esse grupo aparece, por exemplo, na hemoglobina e na mioglobina dos alimentos de origem animal.
Por quê: no ferro heme, o metal já está incorporado a esse anel. O enterócito pode captar o complexo, em vez de precisar primeiro receber o ferro livre pela mesma rota usada para o ferro não heme. Dentro da célula, a degradação do heme libera o ferro para seu processamento, armazenamento ou transferência ao sangue.
Mais a fundo: compare os dois elementos da associação. “Heme” nomeia o complexo que contém ferro; “porfirina” nomeia o anel que o envolve. Os dois irmãos agora cobram esses conceitos, sem mostrar uma segunda ocorrência da resposta heme na parte visível da pergunta.
Na aula: a distinção ajuda a entender por que a forma química do ferro influencia sua absorção. O ferro não heme possui etapas próprias de solubilização e transporte, incluindo a captação de Fe²⁺ por DMT1. Não use o nome de um transportador do ferro não heme como sinônimo da absorção do complexo heme.''',
}

# Remove stale claims in otherwise retained explanations.
REPLACE={
 'o card chama a gastrina de parácrina, mas ela é um hormônio que chega às células pelo sangue.':'a gastrina é um hormônio que chega às células pelo sangue.',
 'Por isso a palavra que falta é electrical: só acima dele aparecem spikes.':'Por isso, ao cruzar o limiar elétrico, aparecem os potenciais em espícula cobrados no card.',
 'por isso a resposta é: hérnia; sutura.':'o termo une o alvo, hérnia, à ação de suturar.',
 'Daí a resposta: articulação; fusão cirúrgica.':'A raiz aponta para a articulação e o sufixo explica a fusão cirúrgica.',
 'o mnemônico MUDPILES lista as causas de gap alto, e a cetoacidose (K) é uma delas.':'a cetoacidose é uma causa de acidose metabólica com aumento do hiato aniônico.',
 'Já para a B12 não há via alternativa fisiológica: sem FI ela não é absorvida no íleo.':'A absorção eficiente de B12 no íleo depende do fator intrínseco; existe uma pequena absorção passiva independente dele, insuficiente na alimentação habitual.',
 'A insulina cai, e só então a glicemia dispara.':'A compensação se torna insuficiente e a hiperglicemia se agrava.',
}
for key,t in OLD.items():
    if t['note_id'] not in NIDS or not t.get('texto'): continue
    text=TABS.get(int(key),t['texto'])
    for a,b in REPLACE.items(): text=text.replace(a,b)
    if text!=t['texto']: TABS[int(key)]=text
for key,t in OLD.items():
    if t['note_id'] in BY_NOTE: TABS[int(key)]=BY_NOTE[t['note_id']]

if __name__=='__main__':
    (P/'tab-changes.json').write_text(json.dumps(TABS,ensure_ascii=False,indent=2))
    print('Tabs revistos',len(TABS))
