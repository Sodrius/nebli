#!/usr/bin/env python3
"""
NEBLI -- gerar_neblicards_acao_hormonal.py

Constroi o deck-aula autoral de `bioq-10-acao-hormonal` (UC03, Bioquimica e
Biologia Molecular -- "Acao hormonal").

Contexto desta corrida: o container remoto nao alcanca o AnkiConnect do Davi
(localhost na maquina dele) e o `anking-v12-export.txt` e gitignored, entao a
ordem canonica de fontes (AnKing curado -> deck externo -> NEBLIcard autoral)
nao pode ser executada. O deck sai 100% autoral, calibrado no formato AnKing
(R13/R18): rotulo tematico neutro, cloze unico em negrito de 1-3 palavras,
frente em ingles medico, Extra em portugues com causa -> mecanismo ->
consequencia, e ancora literal na E1 (gate B2 -- nada orfao).

Escopo: o slide regula O QUE entra; a profundidade Step 1 regula ATE ONDE.
Nenhum card sai do recorte da aula.

Uso:
    python3 flashcards/scripts/gerar_neblicards_acao_hormonal.py
    python3 flashcards/scripts/lint_neblicard.py flashcards/cards-nebli/bioq-10-acao-hormonal.json
"""

import json
from pathlib import Path

SLUG = "bioq-10-acao-hormonal"
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "flashcards" / "cards-nebli" / f"{SLUG}.json"

# (concept_id, subtopico, rotulo, frente, extra_pt, ancora_literal_na_E1)
CARDS = [
    # ---------------- 1.1 tres velocidades de regulacao ----------------
    ("1.1", "Tres alavancas de regulacao", "Bioquímica",
     "Allosteric enzymes follow a <b>{{c1::sigmoid}}</b> velocity curve instead of a hyperbolic one.",
     "A curva em S torna a enzima um interruptor: dentro de uma faixa estreita de substrato ela sai de quase parada para quase máxima.",
     "Enzimas que respondem assim costumam ter curva de velocidade em S, e não a hipérbole clássica de Michaelis-Menten"),

    ("1.1", "Tres alavancas de regulacao", "Bioquímica",
     "The enzyme class that reverses kinase action is the <b>{{c1::phosphatases}}</b>.",
     "Quinase pendura fosfato usando ATP; fosfatase o devolve à água. O par é o que torna a modificação covalente reversível, e não um carimbo definitivo.",
     "Quem pendura é uma quinase, usando ATP como frasco de fosfato; quem retira é uma fosfatase"),

    ("1.1", "Tres alavancas de regulacao", "Metabolismo",
     "The regulatory lever that takes hours to act works by changing <b>{{c1::gene expression}}</b>.",
     "Alostérico responde no tempo de uma colisão; fosforilação, em segundos; fabricar proteína nova, em horas. A escala de tempo separa as classes de hormônio adiante.",
     "Modular alostericamente uma enzima que já existe leva o tempo de uma colisão molecular. Fosforilar uma cascata inteira leva segundos. Fabricar proteína nova leva horas."),

    # ---------------- 1.2 o que define um hormonio ----------------
    ("1.2", "Definicao de hormonio", "Endocrinologia",
     "A mediator acting on the very cell that released it is called <b>{{c1::autocrine}}</b>.",
     "O mecanismo intracelular é idêntico nos três modos; o que muda é o alcance da entrega — corrente sanguínea, vizinhança ou a própria célula.",
     "quando a célula secreta uma molécula que age sobre ela mesma, é autócrina"),

    ("1.2", "Definicao de hormonio", "Endocrinologia",
     "A mediator that diffuses only to neighbouring cells acts in a <b>{{c1::paracrine}}</b> fashion.",
     "Parácrino não entra na circulação: age onde foi produzido. É o modo típico dos eicosanoides, como as prostaglandinas.",
     "Quando ela apenas se difunde para as células vizinhas, sem entrar na circulação, a sinalização é parácrina"),

    ("1.2", "Definicao de hormonio", "Endocrinologia",
     "Epinephrine reaching a distant target through blood is a hormone; released at a synapse it is a <b>{{c1::neurotransmitter}}</b>.",
     "Mesma molécula, mesmo tipo de receptor — muda apenas a rota de entrega. Mostra que a categoria está no modo de operar, não na estrutura química.",
     "a adrenalina é hormônio quando a medula adrenal a lança no sangue e neurotransmissor quando um neurônio a libera numa fenda sináptica"),

    # ---------------- 1.3 sete pontos de regulacao ----------------
    ("1.3", "Sete pontos de regulacao", "Endocrinologia",
     "Only the fraction of hormone not bound to carrier protein is <b>{{c1::biologically active}}</b>.",
     "A fração ligada funciona como reserva: protege da degradação e vai repondo a fração livre aos poucos. Por isso hormônio muito carreado tem meia-vida longa.",
     "só a fração livre é ativa e ela vai sendo reposta aos poucos pela fração ligada"),

    ("1.3", "Sete pontos de regulacao", "Endocrinologia",
     "In type 2 diabetes the defect sits mainly at the step of hormone <b>{{c1::recognition}}</b>.",
     "O pâncreas fabrica e secreta; quem falha é a célula-alvo. Por isso a sulfonilureia, que age na secreção, ainda ajuda — aumenta a oferta para vencer a resistência.",
     "cujas células-alvo respondem mal, falha no reconhecimento, e é exatamente esse o problema central da resistência à insulina"),

    # ---------------- 1.4 solubilidade e endereco do receptor ----------------
    ("1.4", "Solubilidade e receptor", "Bioquímica",
     "Steroid hormones cross the membrane unaided since they are <b>{{c1::lipid soluble}}</b>.",
     "A membrana é um muro de gordura. Quem se dissolve em gordura passa e encontra o receptor dentro; quem se dissolve em água fica na portaria.",
     "Do lado lipossolúvel estão os hormônios esteroides, derivados do colesterol, como o cortisol. Eles atravessam a membrana"),

    ("1.4", "Solubilidade e receptor", "Endocrinologia",
     "Despite deriving from tyrosine, thyroid hormones bind a receptor sitting in the <b>{{c1::nucleus}}</b>.",
     "É a exceção que testa a regra: o que decide o endereço do receptor não é a origem da molécula, e sim se ela atravessa a membrana. Iodada e apolar, ela atravessa.",
     "Origem em aminoácido, mecanismo de esteroide."),

    ("1.4", "Solubilidade e receptor", "Bioquímica",
     "Water-soluble hormones change activity of preexisting enzymes; lipid-soluble ones change the <b>{{c1::amount of protein}}</b>.",
     "É a raiz da diferença de velocidade: mudar o estado do que já existe leva segundos; fabricar do zero exige transcrever, traduzir e dobrar.",
     "altera a atividade de enzima preexistente"),

    ("1.4", "Solubilidade e receptor", "Bioquímica",
     "Prostaglandins are local mediators built from twenty-carbon <b>{{c1::fatty acids}}</b>.",
     "Origem lipídica e ação predominantemente parácrina: agem perto de onde nascem, em vez de viajar pelo sangue como a insulina.",
     "Os eicosanoides completam o quadro pelo lado lipídico, com atuação predominantemente local"),

    ("1.4", "Solubilidade e receptor", "Endocrinologia",
     "A response that requires new protein synthesis starts only after <b>{{c1::hours}}</b>.",
     "A lentidão não é defeito: é o custo de transcrever e traduzir. Em troca, o efeito sobrevive à queda do hormônio no sangue.",
     "Como o efeito só aparece quando a proteína nova estiver pronta, a resposta demora horas"),

    # ---------------- 1.5 cascata do AMPc ----------------
    ("1.5", "Cascata do AMPc", "Bioquímica",
     "The G protein stays switched on for as long as it holds <b>{{c1::GTP}}</b>.",
     "É um interruptor com temporizador embutido: a própria proteína hidrolisa o GTP em GDP e se desliga sozinha, limitando a duração do sinal.",
     "um interruptor que fica ligado enquanto segura GTP e se desliga sozinho quando corta esse GTP em GDP"),

    ("1.5", "Cascata do AMPc", "Bioquímica",
     "Adenylyl cyclase turns ATP into the second messenger <b>{{c1::cAMP}}</b>.",
     "A enzima fecha o ATP num anel. O segundo mensageiro difunde pelo citoplasma e leva adiante a ordem que o hormônio deixou do lado de fora.",
     "uma enzima de membrana que pega ATP e o fecha num anel, produzindo AMPc"),

    ("1.5", "Cascata do AMPc", "Bioquímica",
     "Binding of cAMP releases the catalytic subunits of <b>{{c1::PKA}}</b>.",
     "Liberada, ela fosforila os alvos do tecido. O repertório de alvos é o que faz o mesmo mensageiro produzir efeitos diferentes em fígado e músculo.",
     "ele se difunde pelo citoplasma e ativa a PKA"),

    ("1.5", "Cascata do AMPc", "Bioquímica",
     "Cascade amplification multiplies rather than adds since every tier acts <b>{{c1::catalytically}}</b>.",
     "Um receptor ocupado ativa várias proteínas G, cada ciclase faz muitos AMPc, cada PKA fosforila muitos alvos. O produto dos degraus é a explosão do efeito.",
     "Como cada nível multiplica o anterior em vez de somar, o efeito final é o produto de quatro fatores de amplificação"),

    ("1.5", "Cascata do AMPc", "Endocrinologia",
     "Hormone receptors must show high affinity to detect ligand at <b>{{c1::nanomolar concentrations}}</b>.",
     "Detectar tão pouco resolve metade do problema; a outra metade é a amplificação em cascata, que transforma poucos eventos de ligação em muito efeito.",
     "afinidade alta significa que o receptor consegue capturar seu hormônio mesmo quando ele está presente em concentração nanomolar ou menor"),

    # ---------------- 2.1 processamento da insulina ----------------
    ("2.1", "Processamento da insulina", "Bioquímica",
     "The signal peptide of preproinsulin is clipped on entry into the <b>{{c1::endoplasmic reticulum}}</b>.",
     "O prefixo pré é apenas um endereço: leva a cadeia recém-sintetizada ao compartimento certo e é cortado assim que ela chega.",
     "O prefixo \"pré\" corresponde a um peptídeo-sinal, o endereço que leva a cadeia recém-sintetizada para dentro do retículo endoplasmático"),

    ("2.1", "Processamento da insulina", "Bioquímica",
     "Mature insulin holds its two chains together through <b>{{c1::disulfide bonds}}</b>.",
     "As pontes se formam ainda na pró-insulina dobrada. Por isso as cadeias A e B continuam unidas depois que o trecho central é removido.",
     "mantidas juntas pelas pontes dissulfeto que já haviam se formado"),

    ("2.1", "Processamento da insulina", "Bioquímica",
     "Cleavage of proinsulin in the granule yields insulin plus <b>{{c1::C peptide}}</b>.",
     "Os dois saem do mesmo precursor e são secretados em quantidade equivalente — o que transforma um subproduto em marcador de produção própria.",
     "liberando duas moléculas: a insulina madura ... e o trecho central que foi removido, o peptídeo C"),

    ("2.1", "Processamento da insulina", "Endocrinologia",
     "Hypoglycaemia with high insulin and an absent C peptide points to <b>{{c1::injection}}</b>.",
     "Insulina aplicada não vem acompanhada de peptídeo C. Peptídeo C alto no mesmo quadro aponta produção endógena, como num tumor de células beta.",
     "Insulina aplicada por injeção não vem acompanhada de peptídeo C"),

    # ---------------- 2.2 celula beta como sensor ----------------
    ("2.2", "Celula beta como sensor", "Bioquímica",
     "Beta cells take up sugar through the transporter <b>{{c1::GLUT2}}</b>.",
     "Baixa afinidade e sem saturação na faixa fisiológica: quanto mais glicose fora, mais entra. A entrada acompanha a glicemia em vez de travar num teto.",
     "A glicose entra na célula beta pelo transportador GLUT2, que tem baixa afinidade e não satura na faixa de glicemia fisiológica"),

    ("2.2", "Celula beta como sensor", "Bioquímica",
     "The low-affinity beta-cell enzyme that phosphorylates sugar is <b>{{c1::glucokinase}}</b>.",
     "Ela não está ali para gerar energia, e sim para não saturar: com folga para acelerar, sua velocidade vira uma leitura fiel da glicemia.",
     "A glicoquinase não está ali para gerar energia; ela está ali justamente para não saturar"),

    ("2.2", "Celula beta como sensor", "Bioquímica",
     "Glucokinase keeps responding at high sugar because it never reaches <b>{{c1::saturation}}</b>.",
     "Uma enzima de alta afinidade já estaria no máximo em glicemia normal e não distinguiria 90 de 180 — as duas dariam a mesma resposta.",
     "Uma enzima de alta afinidade, como a hexoquinase dos outros tecidos, já estaria trabalhando na velocidade máxima em glicemia normal"),

    ("2.2", "Celula beta como sensor", "Bioquímica",
     "Unlike glucokinase, hexokinase is shut down by its own product, <b>{{c1::glucose 6-phosphate}}</b>.",
     "A inibição pelo produto é o que impede a hexoquinase de servir como medidor: ela satura cedo e se autolimita.",
     "A mesma lógica explica por que o fígado usa glicoquinase"),

    ("2.2", "Celula beta como sensor", "Bioquímica",
     "Rising ATP inside the beta cell shuts the channel carrying <b>{{c1::potassium}}</b>.",
     "É o passo que converte química em elétrica: sem o vazamento do íon, a face interna da membrana deixa de ser mantida negativa.",
     "é o ATP que fecha um canal de potássio específico da membrana"),

    ("2.2", "Celula beta como sensor", "Bioquímica",
     "Closing the potassium channel makes the beta-cell membrane <b>{{c1::depolarise}}</b>.",
     "Com o canal fechado o potássio para de sair, a carga interna sobe e a membrana perde o repouso — o gatilho elétrico da secreção.",
     "o potássio deixa de vazar para fora, a face interna da membrana fica menos negativa e a célula despolariza"),

    ("2.2", "Celula beta como sensor", "Bioquímica",
     "Depolarisation opens voltage-gated channels that admit <b>{{c1::calcium}}</b>.",
     "O íon que entra é o gatilho final: dispara a fusão dos grânulos com a membrana e a saída da insulina por exocitose.",
     "A despolarização abre canais de cálcio dependentes de voltagem, o cálcio entra, e é o cálcio que dispara a fusão dos grânulos"),

    # ---------------- 2.3 farmacologia do canal ----------------
    ("2.3", "Farmacologia do canal", "Farmacologia",
     "Sulfonylureas shut the ATP-sensitive potassium channel and raise <b>{{c1::insulin secretion}}</b>.",
     "A droga substitui o sensor em vez de obedecê-lo: fecha o canal por conta própria, sem esperar o ATP subir.",
     "As sulfonilureias fecham o canal por conta própria, sem esperar que o ATP suba"),

    ("2.3", "Farmacologia do canal", "Farmacologia",
     "The characteristic adverse effect of sulfonylureas is <b>{{c1::hypoglycaemia}}</b>.",
     "Consequência direta do mecanismo: como a secreção é forçada mesmo com glicemia baixa, o freio fisiológico deixa de existir.",
     "o efeito adverso característico é a hipoglicemia: a droga força secreção mesmo quando a glicemia já está baixa"),

    ("2.3", "Farmacologia do canal", "Farmacologia",
     "Sulfonylureas only work while there is residual functioning <b>{{c1::beta cells}}</b>.",
     "A droga estimula quem ainda existe; não repõe hormônio. Por isso serve no diabetes tipo 2, em que a periferia responde mal mas a ilhota ainda produz.",
     "desde que ainda haja célula beta funcionante para ser estimulada"),

    ("2.3", "Farmacologia do canal", "Endocrinologia",
     "In a beta-cell tumour, hypoglycaemia coexists with inappropriately high <b>{{c1::insulin}}</b>.",
     "Secreção autônoma ignora a glicemia. O tratamento definitivo é cirúrgico; enquanto isso, abrir o canal de potássio contém a secreção.",
     "um tumor de células beta que secreta insulina de forma autônoma e produz hipoglicemia com insulina inapropriadamente alta"),

    ("2.3", "Farmacologia do canal", "Farmacologia",
     "Holding the ATP-sensitive potassium channel open stops the membrane from <b>{{c1::depolarising}}</b>.",
     "É a imagem espelhada da sulfonilureia: mesmo canal, sentido contrário. Sem despolarização não entra cálcio, e a secreção é contida.",
     "um agonista do canal de potássio, que o mantém aberto ... a membrana não despolariza, o cálcio não entra e a secreção é contida"),

    # ---------------- 2.4 glucagon ----------------
    ("2.4", "Glucagon", "Endocrinologia",
     "Glucagon is made by the islet cells named <b>{{c1::alpha}}</b>.",
     "Os dois sinais opostos nascem lado a lado, no mesmo microambiente da ilhota — o que facilita a coordenação entre eles.",
     "produzido pelas células alfa das mesmas ilhotas de Langerhans que abrigam as células beta"),

    ("2.4", "Glucagon", "Endocrinologia",
     "A protein-rich, carbohydrate-poor meal raises glucagon, guarding against <b>{{c1::low blood sugar}}</b>.",
     "A refeição proteica sobe a insulina, que jogaria a glicemia para baixo. A subida simultânea de glucagon é o contrapeso — por isso bife puro não derruba o açúcar.",
     "a subida simultânea de glucagon protege contra essa hipoglicemia. É a razão pela qual comer bife puro não derruba o açúcar"),

    ("2.4", "Glucagon", "Endocrinologia",
     "Ketone bodies and urea suppress glucagon <b>{{c1::secretion}}</b>.",
     "São sinais de que combustível alternativo já está disponível ou de que a quebra de proteína foi longe demais — não faz sentido mobilizar mais.",
     "a secreção é inibida pela própria insulina, por corpos cetônicos e pela ureia"),

    ("2.4", "Glucagon", "Farmacologia",
     "Injected glucagon rescues severe hypoglycaemia when the oral route is <b>{{c1::unavailable}}</b>.",
     "O hormônio mobiliza reserva hepática e eleva a glicemia em minutos, sem depender de o paciente conseguir engolir.",
     "faz do glucagon injetável o socorro para uma hipoglicemia grave em que não se consegue dar açúcar por via oral"),

    # ---------------- 2.5 fosforilase e sintase ----------------
    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "Phosphorylation turns glycogen phosphorylase into its <b>{{c1::active}}</b> form.",
     "Mesmo fosfato, sentidos opostos nas duas enzimas do glicogênio — é essa oposição que impede síntese e degradação simultâneas.",
     "Fosforilar a fosforilase a ativa; fosforilar a sintase a inativa"),

    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "Phosphorylation of glycogen synthase leaves the enzyme <b>{{c1::inactive}}</b>.",
     "O sentido da mudança é propriedade da enzima, não do fosfato. Quem guarda \"fosforilou, ligou\" conclui errado que glucagon estimula síntese de glicogênio.",
     "A mesma PKA, na mesma célula, no mesmo instante, ativa a glicogênio fosforilase e inativa a glicogênio sintase"),

    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "Coordinated control of glycogen spares the cell a wasteful <b>{{c1::futile cycle}}</b>.",
     "Construir e destruir o mesmo polímero ao mesmo tempo só gastaria ATP. A reciprocidade garante que apenas um sentido esteja ligado por vez.",
     "Essa reciprocidade é o que impede o desperdício de um ciclo fútil"),

    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "In muscle, phosphorylase is allosterically switched on by rising <b>{{c1::AMP}}</b>.",
     "AMP alto denuncia consumo de ATP. Assim o músculo quebra glicogênio no início do esforço, antes mesmo de qualquer hormônio chegar.",
     "o AMP faz o contrário, empurrando a enzima para a forma relaxada e ativa, porque AMP alto significa que o ATP está sendo consumido"),

    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "ATP and glucose 6-phosphate push muscle phosphorylase towards the <b>{{c1::T state}}</b>.",
     "São os sinais de fartura energética local: com energia sobrando, não há motivo para abrir a reserva.",
     "ATP e glicose-6-fosfato favorecem a forma tensa, menos ativa, sinalizando que há energia de sobra"),

    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "In liver, the allosteric signal that switches phosphorylase off is free <b>{{c1::glucose}}</b>.",
     "O fígado quebra glicogênio para servir ao sangue; basta a glicemia estar reposta para ele parar. O músculo, que serve a si, usa outro sensor.",
     "no fígado o sensor é outro ... quem regula é a glicose livre, que se liga à forma ativa da enzima e a empurra de volta ao estado inativo"),

    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "Muscle keeps its sugar inside since it lacks <b>{{c1::glucose 6-phosphatase}}</b>.",
     "A carga do fosfato impede a saída pela membrana. Por isso a glicogenólise muscular sustenta a contração e só a hepática sustenta a glicemia.",
     "O músculo não possui glicose-6-fosfatase. A glicose-6-fosfato que ele obtém do próprio glicogênio fica presa dentro da célula"),

    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "Insulin switches glycogen synthase on by promoting its <b>{{c1::dephosphorylation}}</b>.",
     "A insulina não precisa de via separada para cada enzima: remove os fosfatos, e a reciprocidade já existente entre fosforilase e sintase faz o resto.",
     "ela promove a remoção dos fosfatos, e a reciprocidade que já existia entre as duas enzimas faz o resto"),

    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "Insulin increases muscle and fat sugar uptake by recruiting the transporter <b>{{c1::GLUT4}}</b>.",
     "É o transportador dependente de insulina: sem o hormônio ele fica guardado em vesículas. Explica por que músculo e adiposo captam pouco no jejum.",
     "aumenta a captação de glicose pelo transportador GLUT4 no músculo e no tecido adiposo"),

    ("2.5", "Fosforilase e sintase", "Bioquímica",
     "Insulin lowers plasma triacylglycerol by inducing the endothelial enzyme <b>{{c1::lipoprotein lipase}}</b>.",
     "A enzima quebra o triacilglicerol das lipoproteínas na parede do vaso, liberando ácidos graxos para o tecido estocar.",
     "Repare que o hormônio não faz uma coisa só"),

    # ---------------- 2.6 desligar o sinal ----------------
    ("2.6", "Desligar o sinal", "Bioquímica",
     "The enzyme that ends the cAMP signal by opening its ring is a <b>{{c1::phosphodiesterase}}</b>.",
     "Sem segundo mensageiro, a quinase volta ao estado inibido e a cascata para de escrever novos fosfatos — mas os já pendurados continuam lá.",
     "A primeira é a fosfodiesterase, que abre o anel do AMPc e o converte em AMP comum"),

    ("2.6", "Desligar o sinal", "Bioquímica",
     "Stripping phosphate groups off the glycogen enzymes is the job of <b>{{c1::PP1}}</b>.",
     "São necessárias duas apagadoras em momentos diferentes: uma corta o mensageiro, a outra desfaz a mensagem que já tinha sido escrita.",
     "a PP1, que remove os fosfatos já pendurados"),

    ("2.6", "Desligar o sinal", "Bioquímica",
     "Activating PP1 shuts down breakdown and at the same time turns on <b>{{c1::synthesis}}</b>.",
     "Um só gesto, dois efeitos opostos — porque desfosforilar inativa a fosforilase e ativa a sintase. É como a insulina fecha o circuito.",
     "Quebra desligada e síntese ligada, com um único movimento"),

    # ---------------- 3.1 catecolaminas ----------------
    ("3.1", "Catecolaminas", "Bioquímica",
     "The precursor amino acid for catecholamine synthesis is <b>{{c1::tyrosine}}</b>.",
     "Via curta e bem definida, com quatro conversões até a adrenalina. A origem em aminoácido não impede o hormônio de agir por receptor de superfície.",
     "Ela pertence às catecolaminas, sintetizadas a partir da tirosina numa via curta e bem definida"),

    ("3.1", "Catecolaminas", "Bioquímica",
     "The rate-limiting step of catecholamine synthesis is run by tyrosine <b>{{c1::hydroxylase}}</b>.",
     "O primeiro passo determina o quanto de catecolamina o tecido consegue produzir — é ali que a produção é regulada.",
     "o passo inicial, catalisado pela tirosina hidroxilase, é o passo limitante da velocidade"),

    ("3.1", "Catecolaminas", "Bioquímica",
     "Dopamine appears when DOPA undergoes <b>{{c1::decarboxylation}}</b>.",
     "Tirosina vira dopa por hidroxilação, dopa vira dopamina por perda do grupo carboxila, e dopamina segue para noradrenalina.",
     "a dopa é descarboxilada e vira dopamina"),

    ("3.1", "Catecolaminas", "Endocrinologia",
     "The final methylation step happens almost only in the <b>{{c1::adrenal medulla}}</b>.",
     "Por isso ela é a fonte da adrenalina circulante, enquanto os neurônios liberam sobretudo noradrenalina.",
     "a última conversão, de noradrenalina em adrenalina, ocorre essencialmente na medula da glândula adrenal"),

    ("3.1", "Catecolaminas", "Farmacologia",
     "Epinephrine is used clinically in cardiac arrest, shock and <b>{{c1::anaphylaxis}}</b>.",
     "Nos três cenários buscam-se os mesmos efeitos — coração acelerado, via aérea dilatada, fluxo redistribuído — obtidos em segundos pela cascata do AMPc.",
     "faz da adrenalina uma droga de emergência, usada em parada cardíaca, choque e anafilaxia"),

    # ---------------- 3.2 hormonios tireoidianos ----------------
    ("3.2", "Hormonios tireoidianos", "Endocrinologia",
     "The thyroid hormone form that actually acts inside target tissues is <b>{{c1::T3}}</b>.",
     "A tireoide secreta sobretudo T4; o hormônio ativo é gerado no próprio tecido, o que dá a cada órgão controle local sobre a dose que recebe.",
     "a molécula que efetivamente age nos tecidos é a tri-iodotironina, o T3"),

    ("3.2", "Hormonios tireoidianos", "Bioquímica",
     "The enzymes converting T4 into its active form are the <b>{{c1::deiodinases}}</b>.",
     "Elas retiram um átomo de iodo dentro do tecido-alvo. É uma camada de controle que escapa ao comando da glândula.",
     "Enzimas chamadas desiodases retiram um iodo do T4 já dentro do tecido-alvo"),

    ("3.2", "Hormonios tireoidianos", "Endocrinologia",
     "Because T4 circulates abundantly with a long half-life, it behaves as a <b>{{c1::reservoir}}</b>.",
     "O estoque circulante amortece oscilações: cada tecido saca dele a quantidade de hormônio ativo que quiser, quando quiser.",
     "o T4 funciona como um reservatório circulante de meia-vida longa"),

    ("3.2", "Hormonios tireoidianos", "Endocrinologia",
     "On DNA the thyroid hormone receptor pairs up with <b>{{c1::RXR}}</b>.",
     "O par se instala sobre a região reguladora do gene e altera a transcrição — mecanismo de esteroide, apesar da origem em aminoácido.",
     "liga-se ao seu receptor, que se associa a um parceiro sobre a região reguladora do gene, e altera a transcrição"),

    ("3.2", "Hormonios tireoidianos", "Endocrinologia",
     "Cold intolerance, weight gain and constipation mark a thyroid state that is <b>{{c1::underactive}}</b>.",
     "Não é lista para decorar: com o gasto basal derrubado, tudo desacelera junto — trânsito, batimento, raciocínio, depuração de colesterol.",
     "No hipotireoidismo, com pouco hormônio, o gasto cai e o corpo desacelera em várias frentes ao mesmo tempo"),

    ("3.2", "Hormonios tireoidianos", "Endocrinologia",
     "Heat intolerance, weight loss and tremor mark a thyroid state that is <b>{{c1::overactive}}</b>.",
     "O mesmo eixo lido no sentido oposto: com a taxa metabólica alta, o paciente perde peso apesar de comer mais.",
     "No hipertireoidismo, tudo acelera: perda de peso apesar do apetite aumentado"),

    ("3.2", "Hormonios tireoidianos", "Endocrinologia",
     "Thyroid hormone sets the resting <b>{{c1::metabolic rate}}</b>.",
     "Ele age como termostato: mexe no nível em que a máquina inteira funciona, e por isso a doença tireoidiana produz sintomas espalhados.",
     "os hormônios tireoidianos são o ajuste fino do termostato — mexem no nível em que a máquina inteira funciona"),

    # ---------------- 3.3 cortisol e receptor nuclear ----------------
    ("3.3", "Cortisol e receptor nuclear", "Bioquímica",
     "Every steroid hormone is built from <b>{{c1::cholesterol}}</b>.",
     "A origem lipídica é o que permite atravessar a membrana sem transportador e encontrar o receptor já dentro da célula.",
     "o representante dos hormônios esteroides, todos derivados do colesterol"),

    ("3.3", "Cortisol e receptor nuclear", "Bioquímica",
     "Before ligand arrives, the steroid receptor is held inactive by a <b>{{c1::chaperone}}</b>.",
     "A chegada do esteroide desfaz essa associação e muda o formato do receptor — o primeiro passo da sequência que termina em transcrição.",
     "esse receptor fica preso a proteínas acompanhantes que o mantêm inativo; a chegada do esteroide desfaz essa associação"),

    ("3.3", "Cortisol e receptor nuclear", "Bioquímica",
     "Two hormone-receptor complexes join on DNA as a <b>{{c1::dimer}}</b>.",
     "É o par, não a unidade solta, que reconhece a sequência reguladora do gene-alvo.",
     "Dois complexos hormônio-receptor se juntam formando um dímero"),

    ("3.3", "Cortisol e receptor nuclear", "Bioquímica",
     "The short DNA stretch read by the hormone-receptor complex is the <b>{{c1::response element}}</b>.",
     "É o endereço que define quais genes aquele hormônio controla — a especificidade da resposta lenta mora aqui.",
     "o elemento de resposta"),

    ("3.3", "Cortisol e receptor nuclear", "Bioquímica",
     "Full switching on of transcription needs recruitment of <b>{{c1::coactivators}}</b>.",
     "Ligar no DNA não basta: o complexo precisa chamar as proteínas que efetivamente acionam a maquinaria de transcrição.",
     "ele recruta proteínas coativadoras, e o conjunto liga a transcrição daquele gene"),

    ("3.3", "Cortisol e receptor nuclear", "Endocrinologia",
     "The pituitary hormone driving cortisol output is <b>{{c1::ACTH}}</b>.",
     "O hipotálamo estimula a hipófise, a hipófise estimula o córtex adrenal, e o cortisol produzido volta inibindo os dois andares acima.",
     "que libera ACTH para o córtex da adrenal; e o cortisol produzido volta inibindo os dois andares acima"),

    ("3.3", "Cortisol e receptor nuclear", "Endocrinologia",
     "Cortisol supplies gluconeogenic substrate by breaking down <b>{{c1::muscle protein}}</b>.",
     "O fio condutor é mobilizar substrato para um período de demanda: aminoácidos saem do músculo e viram glicose no fígado.",
     "favorece a quebra de proteína no músculo para fornecer aminoácidos à produção hepática de glicose"),

    # ---------------- 3.4 quando o eixo quebra ----------------
    ("3.4", "Quando o eixo quebra", "Endocrinologia",
     "Autoimmune destruction of the adrenal cortex defines <b>{{c1::Addison disease}}</b>.",
     "Sem cortisol, o freio sobre os andares de cima desaparece e o comando hipofisário dispara.",
     "Na doença de Addison, o córtex adrenal é destruído — classicamente por um ataque autoimune contra o próprio tecido"),

    ("3.4", "Quando o eixo quebra", "Endocrinologia",
     "Skin darkening in primary adrenal failure follows the shared sequence between ACTH and <b>{{c1::MSH}}</b>.",
     "Os primeiros aminoácidos do ACTH correspondem ao hormônio estimulante de melanócitos. O achado é o excesso do hormônio de cima ficando visível na pele.",
     "Os primeiros aminoácidos da molécula de ACTH correspondem ao hormônio estimulante de melanócitos"),

    ("3.4", "Quando o eixo quebra", "Endocrinologia",
     "Central obesity, muscle wasting and hyperglycaemia describe an excess of <b>{{c1::glucocorticoid}}</b>.",
     "Nada disso precisa ser decorado: são as funções normais do hormônio levadas ao exagero e mantidas no tempo.",
     "Os achados são o efeito fisiológico do cortisol levado ao exagero e mantido no tempo"),

    ("3.4", "Quando o eixo quebra", "Farmacologia",
     "Long-term steroid therapy suppresses the axis, so withdrawal has to be <b>{{c1::gradual}}</b>.",
     "Com hormônio vindo do comprimido, o córtex adrenal atrofia. Parar de repente deixa o paciente agudamente sem cortisol, como num Addison.",
     "Por isso a retirada é feita em degraus, dando tempo para o eixo religar"),

    ("3.4", "Quando o eixo quebra", "Endocrinologia",
     "An environmental molecule that occupies a hormone receptor without switching it on acts as a <b>{{c1::blocker}}</b>.",
     "A precisão do sistema é também sua fragilidade: um receptor que reconhece nanomolar é, por construção, sensível a impostores.",
     "outros ocupam o receptor sem ativá-lo e impedem o hormônio verdadeiro de trabalhar"),
]


def build():
    cards = []
    for i, (cid, sub, rotulo, frente, extra, ancora) in enumerate(CARDS, 1):
        cards.append({
            "id": f"{SLUG}-{i:03d}",
            "concept_id": cid,
            "topico": f"{cid} {sub}",
            "text": f"<b>{rotulo}.</b> {frente}",
            "extra": extra,
            "e1_anchor": {"quote": ancora, "arquivo": "typst-build/etapa1.typ"},
            "papel": "core_atomic",
            "objetivo": "fmusp+step1",
            "idioma": "en",
            "visual_need": "none",
            "image_role": "none",
            "visual_task": "conceito verbal — sem alvo de reconhecimento visual",
            "image_status": "not_required",
            "card_mode": "cloze",
            "placement": "text",
            "tags": [f"NEBLI::{SLUG}", "NEBLI::gerado"],
        })
    return {
        "slug": SLUG,
        "aula": "Ação hormonal",
        "uc": "UC03",
        "componente": "Bioquímica e biologia molecular",
        "modelo": "AnKingOverhaul (AnKing Step Deck / AnKingMed)",
        "idioma": "en",
        "pipeline_contract": "e1-e2-v1",
        "fonte": "autoral — AnKing e decks externos inacessíveis neste ambiente "
                 "(sem AnkiConnect e sem anking-v12-export.txt)",
        "cards": cards,
        "gerados": [{"Text": c["text"], "Extra": c["extra"], "Topico": c["topico"]}
                    for c in cards],
    }


if __name__ == "__main__":
    data = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"ok {OUT}  ({len(data['cards'])} cards)")
    from collections import Counter
    for cid, n in sorted(Counter(c["concept_id"] for c in data["cards"]).items()):
        print(f"  {cid}: {n}")
