"""Inventário editorial da leitura integral dos 69 slides; ainda não é seleção de cards."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
# Cada separador delimita uma recuperação/conexão a conferir, não impõe um card.
DATA={
2:'AMPc como segundo mensageiro ligando receptor à ativação enzimática',
3:'Farmacologia integra química, fisiologia e bioquímica para entender efeitos de fármacos|Fármacos incluem moléculas pequenas e biofármacos como insulina e anticorpos',
9:'A dose pode separar benefício terapêutico de toxicidade',
16:'Desenvolvimento racional e purificação/síntese com controle de qualidade|Estudos pré-clínicos precedem estudos clínicos|Fases clínicas I, II, III e farmacovigilância IV têm finalidades distintas',
17:'Fármaco como substância química de estrutura conhecida que modifica função biológica',
18:'Fármaco versus medicamento formulado com excipientes|Remédio é conceito mais amplo que medicamento|Ação farmacológica não exige sempre ligação a receptor ou proteína',
19:'Beta-lactamase inativa penicilinas|Clavulanato inibe beta-lactamase e protege o antibiótico associado',
20:'Farmacologia médica abrange diagnóstico, prevenção e tratamento|Toxicologia estuda efeitos adversos de agentes químicos',
21:'Farmacocinética é o que o organismo faz ao fármaco|Absorção leva do local de administração à circulação|Distribuição leva o fármaco aos tecidos|Metabolismo transforma quimicamente o fármaco|Excreção remove fármaco e metabólitos',
22:'Farmacodinâmica é o que o fármaco faz ao organismo|Dose/concentração-resposta conecta exposição ao efeito terapêutico ou tóxico',
23:'Sequência liberação-dissolução-absorção-distribuição-alvo-resposta|Biodisponibilidade distingue dose administrada da fração que chega à circulação sistêmica',
24:'Fármaco não sabe onde dói; distribuição e alvos determinam o efeito',
25:'Quatro grandes alvos proteicos são receptores, canais, enzimas e transportadores|Receptores ionotrópicos são canais regulados por ligante|GPCRs traduzem ligação por proteína G e mensageiros intracelulares|Receptores ligados a quinases promovem fosforilação/sinalização|Receptores nucleares regulam expressão gênica|Canais regulados por voltagem diferem dos regulados por ligante|Ácidos nucleicos também podem ser alvos não proteicos',
26:'Muitos fármacos convergem em um conjunto menor de classes de alvos',
27:'Cisplatina faz ligações cruzadas no DNA e impede sua função|Doxorrubicina intercala DNA e interfere com topoisomerase II, não compartilhar mecanismo único com cisplatina|Dano ao DNA prejudica proliferação e pode induzir apoptose|Indicações exemplificadas de cisplatina e doxorrubicina contextualizam o mecanismo',
28:'Cisplatina e nefrotoxicidade|Doxorrubicina e cardiotoxicidade cumulativa|Efeito terapêutico e dano a tecidos normais coexistem|Náuseas/vômitos e alopecia como efeitos adversos ilustrativos',
29:'Nitroglicerina é pró-fármaco que promove sinalização por NO|Vasodilatação explica alívio da angina e cefaleia|Exposição continuada aos nitratos pode produzir tolerância',
30:'NO sintase usa L-arginina para formar NO|NO é difusível e alcança guanilato ciclase solúvel|NO ativa guanilato ciclase por grupo heme|Guanilato ciclase converte GTP em GMPc|GMPc promove relaxamento do músculo liso vascular|PDE5 degrada GMPc|Sildenafil e tadalafila inibem PDE5 e prolongam sinal de GMPc|Nitratos com inibidores de PDE5 podem causar hipotensão intensa|NO também reduz agregação plaquetária',
31:'Captopril/enalapril inibem ECA|AINEs inibem ciclo-oxigenase|Carbidopa inibe DOPA descarboxilase periférica|Metotrexato inibe di-hidrofolato redutase|Irinotecano/topotecano inibem topoisomerase I|Citarabina interfere com síntese de DNA/DNA polimerase|Estatinas inibem HMG-CoA redutase|Clavulanato inibe beta-lactamase, reutilizar slide 19|Zidovudina inibe transcriptase reversa|Indinavir/ritonavir inibem protease HIV|Digoxina inibe Na/K ATPase|Omeprazol/pantoprazol inibem H/K ATPase|Milrinona inibe PDE3, sildenafil PDE5',
32:'Manitol age por efeito osmótico sem receptor específico|Manitol no lúmen tubular reduz reabsorção passiva de água|Efeito osmótico do manitol pode deslocar água para o intravascular e reduzir edema cerebral',
33:'Antiácidos neutralizam quimicamente ácido gástrico|Neutralização difere da inibição da secreção por omeprazol',
34:'Ligantes intestinais de potássio aumentam eliminação fecal sem receptor clássico|Insuficiência renal favorece hipercalemia por menor excreção|K extracelular elevado reduz gradiente e despolariza membrana|Despolarização sustentada inativa canais de Na e pode causar arritmias',
35:'Ligação ao alvo, resposta celular e efeito clínico são etapas distintas',
36:'Complementaridade química/espacial determina reconhecimento do alvo|Interações eletrostáticas, hidrogênio e van der Waals ajudam ligação reversível|Ligações covalentes tendem a produzir inibição persistente|Zanamivir ilustra desenho racional de inibidor de neuraminidase',
37:'Estereoisômeros têm a mesma fórmula e arranjos espaciais diferentes|Enantiômeros podem diferir em afinidade, efeito e toxicidade|Talidomida exige ressalva de interconversão in vivo, não há enantiômero clinicamente seguro|Bupivacaína ilustra toxicidade dependente de estereoquímica|Diferenças entre enantiômeros da varfarina/ibuprofeno como exemplos a conferir',
38:'Sítio ortostérico recebe o ligante endógeno|Sítio alostérico é distinto do ortostérico|Modulação alostérica positiva potencializa resposta ao ligante|Modulação alostérica negativa reduz resposta ao ligante|Modulação pode alterar afinidade e/ou eficácia',
39:'Afinidade é tendência de ligação, distinta de ativação|Eficácia é capacidade de produzir resposta após ligação|Potência é quantidade/concentração necessária para efeito definido|EC50 é concentração para metade do Emax do próprio agonista|Kd mede ligação, não é sinônimo de EC50',
40:'Curva à esquerda indica maior potência no mesmo ensaio|Altura do platô informa Emax/eficácia observada|Mesmo Emax não implica mesma potência|Agonista parcial pode ser potente apesar do menor Emax|Identificar EC50 relativa ao próprio platô em gráfico',
41:'Agonista ativa receptor|Antagonista neutro tem afinidade mas eficácia zero|Ativação do receptor pode aumentar ou diminuir função celular, não é sinônimo de estimular órgão',
42:'Atividade constitutiva existe sem ligante|Agonista inverso reduz atividade abaixo do basal|Antagonista neutro sozinho preserva atividade basal|Eficácia positiva, zero e negativa no gráfico|Agonismo inverso não equivale a antagonismo fisiológico',
43:'Distinguir agonismo pleno, parcial, inverso e enviesado',
44:'Equilíbrio entre R inativo e R* ativo|Agonista estabiliza preferencialmente R*',
45:'Agonista inverso estabiliza preferencialmente R|Antagonista neutro não favorece R nem R* no modelo de dois estados',
46:'Anti-histamínicos H1 como loratadina funcionam como agonistas inversos|Anti-histamínicos de primeira e segunda geração exemplificam fármacos da classe, sem decorar catálogo comercial',
47:'Agonista pleno alcança resposta máxima do sistema|Emax depende também do tecido e do acoplamento, não só do ligante',
48:'Agonistas mimetizam sinalização de mediadores endógenos|Glutamato excitatório versus GABA inibitório como ilustração da diversidade de respostas|Opioides endógenos e analgesia contextualizam exemplo da buprenorfina',
49:'Agonista parcial tem Emax menor no mesmo sistema|Aumentar dose do parcial não o transforma em pleno',
50:'Buprenorfina é agonista parcial mu|Alta afinidade permite deslocar agonista pleno e reduzir resposta|Buprenorfina pode precipitar abstinência quando substitui agonista pleno|Efeito teto respiratório relativo não elimina risco de depressão respiratória',
51:'Mesmo GPCR pode sinalizar por proteína G e beta-arrestina|GRK fosforila receptor e favorece recrutamento de beta-arrestina|Beta-arrestina participa de dessensibilização/internalização e de sinalização própria|Agonista enviesado favorece uma via em relação a outra no mesmo receptor',
52:'Oliceridina exemplifica proposta de agonismo enviesado para proteína G|Separar analgesia de efeitos adversos é objetivo, não garantia|Não afirmar beta-arrestina como causa exclusiva de depressão respiratória/constipação',
53:'Antagonista reduz resposta ao agonista sem precisar reduzir sua concentração',
54:'Antagonismo reversível versus ligação irreversível|Antagonista competitivo reversível pode ser superado por agonista|Competitivo reversível aumenta EC50 e mantém Emax no modelo simples|Antagonismo insuperável tipicamente reduz Emax|Não competitivo pode alterar potência também; não impor EC50 invariável|Antagonismo irreversível no mesmo sítio não é igual a alosterismo|Reserva de receptores pode preservar Emax com bloqueio parcial irreversível|Aspirina e omeprazol são inibidores irreversíveis de enzimas, distinguir de antagonistas de receptores',
55:'Tubocurarina bloqueia competitivamente receptores nicotínicos musculares|Bloqueio da transmissão neuromuscular causa relaxamento/paralisia, não analgesia|Não extrapolar todos os ligantes nicotínicos a todos os subtipos do receptor',
56:'Propranolol antagoniza receptores beta-adrenérgicos|Bloqueio beta1 reduz débito cardíaco e liberação de renina|Catecolaminas são os agonistas endógenos nesse exemplo',
57:'Antagonismo químico neutraliza/sequestra a substância ativa|Dimercaprol quelante reduz disponibilidade de metais|Infliximabe se liga ao TNF-alfa e reduz sua ação inflamatória',
58:'Antagonismo farmacocinético reduz concentração do outro fármaco no sítio de ação|Menor absorção, maior metabolismo ou maior excreção podem reduzir exposição|Antagonismo farmacocinético difere de competição pelo receptor',
59:'Fenobarbital induz metabolismo da varfarina e reduz anticoagulação|Vasoconstritor reduz remoção sistêmica do anestésico local|Retenção local prolonga anestesia e pode reduzir toxicidade sistêmica',
60:'Índice terapêutico relaciona dose tóxica/letal e dose eficaz medianas|Distinguir TD50/ED50 clínica e LD50/ED50 experimental|Índice maior geralmente indica maior margem de segurança|Janela terapêutica é intervalo entre exposição eficaz e tóxica|Digoxina, varfarina e lítio têm margem estreita|Curva quantal expressa proporção de indivíduos, não intensidade em um indivíduo|Alta margem relativa não significa ausência de intoxicação por paracetamol/AAS',
64:'Afinidade e atividade intrínseca são diferentes, reutilizar slide 39',
65:'Poliestirenossulfonato troca sódio por potássio e aumenta eliminação fecal|Poliestirenossulfonato pode causar sobrecarga de sódio e lesão intestinal grave|Patiromer troca cálcio por potássio no intestino|Patiromer pode causar hipomagnesemia|Ciclossilicato de zircônio e sódio captura K e pode causar edema por sódio|Ligantes intestinais diferem no início de ação, mas não substituem estabilização emergencial de hipercalemia ameaçadora',
66:'Transportador pode ser inibido ou transportar falso substrato|Tricíclicos/cocaína inibem recaptação de norepinefrina|Anfetamina usa transportadores e favorece liberação de monoaminas|Probenecida inibe transporte tubular de ânions orgânicos|Diuréticos de alça inibem NKCC2|Bombas ATPase também são proteínas transportadoras, reutilizar omeprazol',
67:'Bloqueio do poro difere de modulação da probabilidade de abertura|Anestésicos locais e tetrodotoxina bloqueiam canais de Na voltagem-dependentes por sítios distintos|Amilorida bloqueia ENaC renal|Aldosterona aumenta transporte de sódio por regulação gênica, não abertura direta de ENaC|Gabapentina/pregabalina ligam subunidade alfa2delta de canais de Ca|Di-hidropiridinas bloqueiam canais de Ca tipo L|Sulfonilureias fecham canais KATP pela subunidade SUR|Picrotoxina bloqueia canal GABA-A|Benzodiazepínicos modulam positivamente GABA-A na presença de GABA',
68:'Bloqueio de canais de Na impede propagação de potenciais de ação|Anestésico local reduz sensibilidade dolorosa|Toxicidade sistêmica de anestésicos locais afeta SNC e coração|Vasoconstritor reduz absorção sistêmica, reutilizar slide 59',
69:'Lidocaína exemplifica bloqueio reversível de canais de Na|Articaína ilustra uso por infiltração odontológica|Mepivacaína tem menor vasodilatação intrínseca e pode ser usada sem vasoconstritor|Bupivacaína tem duração longa e maior cardiotoxicidade|Concentração, latência, duração e dose máxima são dependentes de formulação/contexto, não copiar tabela como prescrição universal',
}
EXCLUDED={1:('capa','Título e docente'),4:('fora_do_recorte','História/etimologia: pedido explícito só poucos cards se AnKing existente'),5:('fora_do_recorte','História/etimologia, mesma exceção do pedido'),6:('fora_do_recorte','História neandertal, não criar autoral'),7:('fora_do_recorte','Datas e plantas antigas, não criar autoral'),8:('fora_do_recorte','Terapêutica antiga, não criar autoral'),10:('fora_do_recorte','Lavoisier/história, não criar autoral'),11:('fora_do_recorte','Cronologia industrial, apoio à introdução'),12:('fora_do_recorte','Anúncio histórico, apoio visual'),13:('fora_do_recorte','Anúncio histórico, apoio visual'),14:('fora_do_recorte','Anúncio histórico, apoio visual'),15:('fora_do_recorte','Anúncio histórico, apoio visual'),61:('revisao','Retoma importância da farmacologia, sem novo alvo'),62:('logistica','Bibliografia'),63:('logistica','Separador dos extras')}
VISUAL={25,27,30,32,36,37,38,40,42,44,45,47,49,51,52,54,55,56,57,58,59,60,64,66,67,68}
slides=[]
for page in range(1,70):
    if page in EXCLUDED:
        cls,reason=EXCLUDED[page]; slides.append({'numero':page,'classe':cls,'justificativa':reason,'itens':[]});continue
    items=[]
    for n,alvo in enumerate(DATA[page].split('|'),1):
        items.append({'id':f's{page:02}-{n:02}','alvo':alvo,'habilidade':'explicar/distinguir/aplicar','fontes':[f'Slide {page}'],'visual':'avaliar-imagem' if page in VISUAL else 'nao-necessaria','destino':'pendente de busca AnKing e acervos','observacao':'Inventário não é autorização para copiar erro nem produzir card para cada menção.'})
    slides.append({'numero':page,'classe':'conteudo','itens':items})
out={'lido_antes_da_selecao':True,'fonte':'fontes/slides.pdf','total_paginas':69,'estado':'inventário integral dos slides; cruzamento bibliográfico/provas em andamento; não selecionado','slides':slides,'exercicios':[
{'id':'obj-01','alvo':'Definições, alvos, estrutura-função, curvas, agonismo e antagonismo','fonte':'Objetivos cognitivos PDF 1–2, itens 1–8','destino':'conferir todos os alvos correspondentes'},
{'id':'obj-02','alvo':'Perda de resposta, dessensibilização, taquifilaxia e tolerância','fonte':'Objetivos cognitivos PDF 2 item 9; slides 29 e 51','destino':'aprofundar relações ensinadas, sem curso paralelo'},
{'id':'ex-01','alvo':'Antagonista neutro versus agonista inverso','fonte':'Objetivos cognitivos PDF 7 Stephen questão 1'},
{'id':'ex-02','alvo':'Exemplo clínico de agonista pleno e antagonista','fonte':'Objetivos cognitivos PDF 7 Stephen questão 2'},
{'id':'ex-03','alvo':'Definir e interpretar EC50','fonte':'Objetivos cognitivos PDF 7 Stephen questão 3'},
{'id':'ex-04','alvo':'Identificar alvos e tipos de receptor','fonte':'Objetivos cognitivos PDF 7 Emer questões 2–4'},
{'id':'ex-05','alvo':'Descoberta/desenvolvimento de fármacos','fonte':'Objetivos cognitivos PDF 7 Emer questão 1'},
{'id':'ex-06','alvo':'Antagonismo fisiológico insulina/glucagon','fonte':'Todas as questões PDF 25–26; objetivos PDF 2 item 7','destino':'contraste diretamente pertinente aos antagonismos; Rang cap.2'},
{'id':'ex-07','alvo':'Indução enzimática reduz efeito do outro medicamento','fonte':'Todas as questões PDF 84–85 questão rifampicina/anticoncepcional','destino':'usar para verificar transferência do mecanismo varfarina/fenobarbital sem criar capítulo de contracepção'},
{'id':'ex-08','alvo':'Agente anticolinesterásico e reversão do componente muscarínico por atropina','fonte':'Objetivos cognitivos PDF 7 Emer questão 5','destino':'encaixe do antagonismo, não dizer atropina reverte paralisia nicotínica; conferir fonte antes de incluir'}
], 'capitulo':[], 'limites':['História excluída por instrução explícita, salvo poucos candidatos AnKing pertinentes encontrados posteriormente.','Exemplos de tabela são inventariados todos; escolher recuperação por mecanismo e importância, registrar cada exclusão nominal.','Extras 64–69 pertencem ao arquivo: não omitir silenciosamente, sobretudo transportadores, canais e anestésicos locais.','Questões de farmacocinética quantitativa, doses e outras aulas não expandem o recorte automaticamente.']}
(HERE/'inventario-aula.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('Slides',len(slides),'alvos dos slides',sum(len(s['itens']) for s in slides),'exercicios',len(out['exercicios']))
