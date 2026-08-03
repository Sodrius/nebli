# Piloto v2 — cards para revisão

Status: aguardando apontamentos do usuário. Nenhum card integral foi aprovado.

## 001 — etim-v2-fnd-morfema

**Texto:** Palavras como nefrite dividem-se em unidades significativas chamadas {{c1::morfemas}}.

**Extra:** Cada morfema contribui uma pista de sentido.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

Aqui, não há a necessidade de palavras como nefrite. A indução do cloze permite muitas palavras como resposta correta, como sílabas ou letras. 
É essencial que o cloze indique a indução e o card faça lembrar mesmo o que quer ensinar, não ficar associando outras coisas.
Uma substituição boa poderia ser: 
A menor unidade estrutural de uma palavra que possui significado ou função gramatical chama-se {{c1::morfema}}.
E o comentário: 
Por exemplo, na palavra infelizes, temos três morfemas:in-: prefixo que indica negação.feliz: radical que carrega o significado central.-es: desinência que indica o plural.
Coloca que o comentário pode ter mais palavras (até 25)

Depois, ainda nesse mesmo tema, faria um card explicando mais exemplos de morfema (1 só card pra isso, pra aprofundar um pouco)

## 002 — etim-v2-fnd-prefixo

**Texto:** Em subcutâneo, <b>sub-</b> ocupa o início e funciona como {{c1::prefixo}}.

**Extra:** Ele modifica o sentido da raiz cutane-.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

Bom card, vamos aumentar a quantidade de palavras permitida por card e por comentário, mantendo só que ainda é bom que haja 1 ou 2 palavras por cloze. 
Também seria melhor aqui um card assim: 
Em subcutâneo, <b>sub-</b> funciona morfologicamente como {{c1::prefixo}}.

Veja que cards básicos assim são necessários poucos, não há necessidade de redundância para ensinar o que é um prefixo, porque é algo muito simples. 
Redundância, na maior parte dos casos, não serve um valor. 

Vamos também adicionar uma regra para a geração de todos os cards a partir de agora, de etimologia ou não. Tem que entrar como gate-hard na geração de cards no pipeline NEBLI canônico para geração de resumos. A regra é que todo card vai ser introduzido pelo seu tema antes. Por exemplo, um card de etimologia vai ficar assim: 

**Etimologia.** Em subcutâneo, <b>sub-</b> funciona morfologicamente como {{c1::prefixo}}.

É para ter uma ou duas palavras aqui somente (QUE NÃO DEEM A RESPOSTA DO CARD) para situar o card onde ele estar. 

Um card de bioquímica teria: 

**Bioquímica.** ...

Um card de sistema digestório teria: 

**Sistema digestório** ...

É para ser algo simples, pra dar uma indicação da localização do card, e é muito importante que não indique a resposta e nem dê dicas nessa palavra introdutória de cada card, ela está ali pra identificar onde o card se situa no universo da medicina, porque quando acumularem muitos isso vai facilitar a compreensão dos conceitos como um todo. 
Adiciona isso como regra pra geração dos próximos. 

## 003 — etim-v2-fnd-raiz

**Texto:** Em hepatite, <b>hepat-</b> carrega o referente anatômico como {{c1::raiz}}.

**Extra:** A raiz concentra o núcleo semântico.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

Aqui, a utilização de referente anatômico é estranha, não compreendo tão bem. 
Não vou repetir erros já elaborados em outras explicações também, então tudo que for pontuando você deve varrer para ver quais outros cards repetem esse padrão de erro, corrrigir isso e gravar de alguma maneira para não cometer mais. 

## 004 — etim-v2-fnd-sufixo

**Texto:** Em gastrite, <b>-ite</b> encerra e classifica o termo como {{c1::sufixo}}.

**Extra:** O sufixo costuma indicar processo, condição ou procedimento.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

Extra aqui ficou ruim, analisa os comentários do anking pra aprender a fazer bons comentários.
Para o card ficar melhor: 
**Etimologia**. Em gastrite, <b>-ite</b> age, morfologicamente, como {{c1::**sufixo**}}.

Também sinto que os clozes devem sempre ficarem em negrito quando revelados, pra dar mais destaque a eles.

## 005 — etim-v2-fnd-forma-combinatoria

**Texto:** Em cardiologia, <b>cardi/o</b> é raiz mais vogal: uma {{c1::forma combinatória}}.

**Extra:** A barra separa raiz e vogal de ligação.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

Extra deve explicar o que é uma forma combinatória, porque possivelmente não sei e não quero ter que pesquisar. Esse tipo de card tem que ter uma explicação, quando o termo é apresentado assim

## 006 — etim-v2-fnd-vogal-de-ligacao

**Texto:** Em cardiologia, o <b>o</b> une cardi- a -logia como {{c1::vogal de ligação}}.

**Extra:** Ela facilita a pronúncia; não acrescenta sentido.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

Extra aqui deveria explicar o que é uma vogal de ligação
Esse card poderia ser fundido com o card 5. Esse tipo de coisa que vai permitir um deck mais enxuto de mais qualidade, em que posso revisar mais em menos tempo. Veja o padrão para entender como aplicar em outros casos, sem exagerar. 

Poderia ficar assim o card: 
**Etimologia**: Em cardiologia, <b>cardi/o</b> é raiz mais vogal - uma {{c1::forma combinatória}} - e o b>o</b> une cardi- a -logia como {{c1::vogal de ligação}}.

Daí você coloca um extra que explica os dois termos

## 007 — etim-v2-fnd-decomposicao

**Texto:** Separar pancitopenia em pan- + cit/o + -penia é {{c1::decomposição}}.

**Extra:** A separação torna as pistas morfológicas visíveis.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

reformulado para melhorar indução: 
**Etimologia.** Separar pancitopenia em pan- + cit/o + -penia é um processo de {{c1::decomposição}}.

## 008 — etim-v2-fnd-composicao

**Texto:** Unir nefr/o a -logia para formar nefrologia é {{c1::composição}}.

**Extra:** A palavra resulta da união de elementos.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

mesma correção do 7

## 009 — etim-v2-fnd-derivacao

**Texto:** Acrescentar hiper- a tensão forma hipertensão por {{c1::derivação}}.

**Extra:** Aqui, a derivação ocorre por prefixação.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 010 — etim-v2-fnd-cognato

**Texto:** Renal e ren/o descendem da mesma forma latina; são {{c1::cognatos}}.

**Extra:** Cognatos compartilham origem, não necessariamente uso idêntico.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

teria que explicar cognatos...
vou parar de repetir dicas de coisas que já expliquei o porquê e o como consertar anteriormente.

## 011 — etim-v2-fnd-transliteracao

**Texto:** Escrever νεφρός como nephrós em alfabeto latino é {{c1::transliteração}}.

**Extra:** Transliteração troca escrita, não traduz o significado.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 012 — etim-v2-fnd-eponimo

**Texto:** Parkinson nomeia uma doença a partir de pessoa; é {{c1::epônimo}}.

**Extra:** Epônimos não se decompõem em morfemas médicos.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 013 — etim-v2-fnd-acronimo

**Texto:** A sigla pronunciável <b>laser</b> funciona como {{c1::acrônimo}}.

**Extra:** Acrônimos exigem conhecer a expansão histórica.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 014 — etim-v2-fnd-polissemia

**Texto:** <b>miel/o</b> pode indicar medula óssea ou espinal; isso é {{c1::polissemia}}.

**Extra:** O contexto decide qual sentido está ativo.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 015 — etim-v2-fnd-glosa-literal

**Texto:** Somar os sentidos de nefr/o e -patia produz a {{c1::glosa literal}}.

**Extra:** A glosa orienta; não determina o diagnóstico.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 016 — etim-v2-fnd-definicao-clinica

**Texto:** O uso médico vigente, não só os morfemas, determina a {{c1::definição clínica}}.

**Extra:** Termos históricos podem desviar do sentido literal.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 017 — etim-v2-fnd-ponte-ph-f

**Texto:** Em português, <b>phleb/o</b> corresponde a {{c1::fleb/o}}.

**Extra:** Assim, phlebitis corresponde a flebite.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 018 — etim-v2-fnd-ponte-th-t

**Texto:** Em português, <b>thorac/o</b> corresponde a {{c1::torac/o}}.

**Extra:** Assim, thoracotomy corresponde a toracotomia.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 019 — etim-v2-fnd-ponte-y-i

**Texto:** Em português, <b>glyc/o</b> corresponde a {{c1::glic/o}}.

**Extra:** Assim, glycemia corresponde a glicemia.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 020 — etim-v2-fnd-ponte-rh-r

**Texto:** Em português, <b>rhino-</b> corresponde a {{c1::rino-}}.

**Extra:** Assim, rhinitis corresponde a rinite.
achei esse tipo de card desnecessário, tipo o 18 e 19, muito óbvios, basta 1 para explicar que isso pode acontecer, dar fundamento e seguir a vida.

**Deck:** `NEBLI::Etimologia::01_Fundamentos::01_Prefixo_raiz_sufixo`

## 021 — etim-v2-pre-a-an

**Texto:** O prefixo <b>a-/an-</b> indica {{c1::ausência ou negação}}.

**Extra:** Ex.: anóxia; referente a ausência ou negação.

Gostei desse

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 022 — etim-v2-pre-endo

**Texto:** O prefixo <b>endo-</b> indica {{c1::interno}}.

**Extra:** Ex.: endocárdio; referente a interno.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 023 — etim-v2-pre-epi

**Texto:** O prefixo <b>epi-</b> indica {{c1::sobre}}.

**Extra:** Ex.: epiderme; referente a sobre.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 024 — etim-v2-pre-exo

**Texto:** O prefixo <b>exo-</b> indica {{c1::externo}}.

**Extra:** Ex.: exocitose; referente a externo.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 025 — etim-v2-pre-inter

**Texto:** O prefixo <b>inter-</b> indica {{c1::entre}}.

**Extra:** Ex.: intercostal; referente a entre.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 026 — etim-v2-pre-intra

**Texto:** O prefixo <b>intra-</b> indica {{c1::dentro}}.

**Extra:** Ex.: intracelular; referente a dentro.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 027 — etim-v2-pre-peri

**Texto:** O prefixo <b>peri-</b> indica {{c1::ao redor}}.

**Extra:** Ex.: pericárdio; referente a ao redor.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 028 — etim-v2-pre-sub

**Texto:** O prefixo <b>sub-</b> indica {{c1::abaixo}}.

**Extra:** Ex.: subcutâneo; referente a abaixo.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 029 — etim-v2-pre-trans

**Texto:** O prefixo <b>trans-</b> indica {{c1::através}}.

**Extra:** Ex.: transdérmico; referente a através.
Gostei disso de ter exemplo no extra

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 030 — etim-v2-pre-poli

**Texto:** O prefixo <b>poli-</b> indica {{c1::muitos}}.

**Extra:** Ex.: poliúria; referente a muitos.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 031 — etim-v2-pre-oligo

**Texto:** O prefixo <b>oligo-</b> indica {{c1::poucos}}.

**Extra:** Ex.: oligúria; referente a poucos.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 032 — etim-v2-pre-pan

**Texto:** O prefixo <b>pan-</b> indica {{c1::todo}}.

**Extra:** Ex.: pancitopenia; referente a todo.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 033 — etim-v2-pre-hiper

**Texto:** O prefixo <b>hiper-</b> indica {{c1::excesso ou acima}}.

**Extra:** Ex.: hiperglicemia; referente a excesso ou acima.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 034 — etim-v2-pre-hipo

**Texto:** O prefixo <b>hipo-</b> indica {{c1::deficiência ou abaixo}}.

**Extra:** Ex.: hipoglicemia; referente a deficiência ou abaixo.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 035 — etim-v2-pre-bradi

**Texto:** O prefixo <b>bradi-</b> indica {{c1::lento}}.

**Extra:** Ex.: bradicardia; referente a lento.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 036 — etim-v2-pre-taqui

**Texto:** O prefixo <b>taqui-</b> indica {{c1::rápido}}.

**Extra:** Ex.: taquipneia; referente a rápido.

**Deck:** `NEBLI::Etimologia::02_Prefixos::05_Intensidade_relacao_e_semelhanca`

## 037 — etim-v2-suf-ite

**Texto:** O sufixo <b>-ite</b> indica {{c1::inflamação}}.

**Extra:** Ex.: gastrite; referente a inflamação.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 038 — etim-v2-suf-penia

**Texto:** O sufixo <b>-penia</b> indica {{c1::redução numérica}}.

**Extra:** Ex.: leucopenia; referente a redução numérica.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 039 — etim-v2-suf-megalia

**Texto:** O sufixo <b>-megalia</b> indica {{c1::aumento}}.

**Extra:** Ex.: hepatomegalia; referente a aumento.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 040 — etim-v2-suf-plasia

**Texto:** O sufixo <b>-plasia</b> indica {{c1::formação ou crescimento}}.

**Extra:** Ex.: hiperplasia; referente a formação ou crescimento.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 041 — etim-v2-suf-trofia

**Texto:** O sufixo <b>-trofia</b> indica {{c1::nutrição ou tamanho}}.

**Extra:** Ex.: hipertrofia; referente a nutrição ou tamanho.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 042 — etim-v2-suf-dipsia

**Texto:** O sufixo <b>-dipsia</b> indica {{c1::sede}}.

**Extra:** Ex.: polidipsia; referente a sede.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 043 — etim-v2-suf-pneia

**Texto:** O sufixo <b>-pneia</b> indica {{c1::respiração}}.

**Extra:** Ex.: taquipneia; referente a respiração.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 044 — etim-v2-suf-rreia

**Texto:** O sufixo <b>-rreia</b> indica {{c1::fluxo ou secreção}}.

**Extra:** Ex.: diarreia; referente a fluxo ou secreção.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 045 — etim-v2-suf-capnia

**Texto:** O sufixo <b>-capnia</b> indica {{c1::dióxido de carbono}}.

**Extra:** Ex.: hipercapnia; referente a dióxido de carbono.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 046 — etim-v2-suf-iase

**Texto:** O sufixo <b>-íase</b> indica {{c1::condição ou formação}}.

**Extra:** Ex.: litíase; referente a condição ou formação.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 047 — etim-v2-suf-ectomia

**Texto:** O sufixo <b>-ectomia</b> indica {{c1::remoção cirúrgica}}.

**Extra:** Ex.: gastrectomia; referente a remoção cirúrgica.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 048 — etim-v2-suf-tomia

**Texto:** O sufixo <b>-tomia</b> indica {{c1::incisão}}.

**Extra:** Ex.: laparotomia; referente a incisão.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 049 — etim-v2-suf-stomia

**Texto:** O sufixo <b>-stomia</b> indica {{c1::criação de abertura}}.

**Extra:** Ex.: colostomia; referente a criação de abertura.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 050 — etim-v2-suf-grafia

**Texto:** O sufixo <b>-grafia</b> indica {{c1::processo de registro}}.

**Extra:** Ex.: angiografia; referente a processo de registro.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 051 — etim-v2-suf-grama

**Texto:** O sufixo <b>-grama</b> indica {{c1::registro produzido}}.

**Extra:** Ex.: eletrocardiograma; referente a registro produzido.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 052 — etim-v2-suf-metria

**Texto:** O sufixo <b>-metria</b> indica {{c1::processo de medição}}.

**Extra:** Ex.: espirometria; referente a processo de medição.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 053 — etim-v2-suf-scopia

**Texto:** O sufixo <b>-scopia</b> indica {{c1::exame visual}}.

**Extra:** Ex.: endoscopia; referente a exame visual.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 054 — etim-v2-suf-genese

**Texto:** O sufixo <b>-gênese</b> indica {{c1::formação ou origem}}.

**Extra:** Ex.: angiogênese; referente a formação ou origem.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 055 — etim-v2-suf-poiese

**Texto:** O sufixo <b>-poiese</b> indica {{c1::produção ou formação}}.

**Extra:** Ex.: hematopoiese; referente a produção ou formação.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 056 — etim-v2-suf-lise

**Texto:** O sufixo <b>-lise</b> indica {{c1::quebra ou dissolução}}.

**Extra:** Ex.: hemólise; referente a quebra ou dissolução.

**Deck:** `NEBLI::Etimologia::03_Sufixos::01_Condicoes_e_processos`

## 057 — etim-v2-rai-cit-o

**Texto:** A forma <b>cit/o</b> refere-se a {{c1::célula}}.

**Extra:** Ex.: citologia; referente a célula.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::01_Celula_tecidos_e_embriologia`

## 058 — etim-v2-rai-hist-o

**Texto:** A forma <b>hist/o</b> refere-se a {{c1::tecido}}.

**Extra:** Ex.: histologia; referente a tecido.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::01_Celula_tecidos_e_embriologia`

## 059 — etim-v2-rai-blast-o

**Texto:** A forma <b>blast/o</b> refere-se a {{c1::broto ou precursor}}.

**Extra:** Ex.: blastocisto; referente a broto ou precursor.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::01_Celula_tecidos_e_embriologia`

## 060 — etim-v2-rai-cardi-o

**Texto:** A forma <b>cardi/o</b> refere-se a {{c1::coração}}.

**Extra:** Ex.: cardiologia; referente a coração.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::02_Cardiovascular_e_hematologico`

## 061 — etim-v2-rai-angi-o

**Texto:** A forma <b>angi/o</b> refere-se a {{c1::vaso}}.

**Extra:** Ex.: angiografia; referente a vaso.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::02_Cardiovascular_e_hematologico`

## 062 — etim-v2-rai-hemat-o

**Texto:** A forma <b>hemat/o</b> refere-se a {{c1::sangue}}.

**Extra:** Ex.: hematologia; referente a sangue.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::02_Cardiovascular_e_hematologico`

## 063 — etim-v2-rai-leuk-o

**Texto:** A forma <b>leuk/o</b> refere-se a {{c1::branco}}.

**Extra:** Ex.: leucócito; referente a branco.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::02_Cardiovascular_e_hematologico`

## 064 — etim-v2-rai-tromb-o

**Texto:** A forma <b>tromb/o</b> refere-se a {{c1::coágulo}}.

**Extra:** Inglês: thromb/o; ex.: trombose.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::02_Cardiovascular_e_hematologico`

## 065 — etim-v2-rai-rin-o

**Texto:** A forma <b>rin/o</b> refere-se a {{c1::nariz}}.

**Extra:** Inglês: rhin/o; ex.: rinite.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::03_Respiratorio`

## 066 — etim-v2-rai-bronc-o

**Texto:** A forma <b>bronc/o</b> refere-se a {{c1::brônquio}}.

**Extra:** Inglês: bronch/o; ex.: broncoscopia.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::03_Respiratorio`

## 067 — etim-v2-rai-pneum-o

**Texto:** A forma <b>pneum/o</b> refere-se a {{c1::ar ou pulmão}}.

**Extra:** Ex.: pneumotórax; referente a ar ou pulmão.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::03_Respiratorio`

## 068 — etim-v2-rai-gastr-o

**Texto:** A forma <b>gastr/o</b> refere-se a {{c1::estômago}}.

**Extra:** Ex.: gastrite; referente a estômago.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::04_Gastrointestinal_e_hepatobiliar`

## 069 — etim-v2-rai-hepat-o

**Texto:** A forma <b>hepat/o</b> refere-se a {{c1::fígado}}.

**Extra:** Ex.: hepatite; referente a fígado.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::04_Gastrointestinal_e_hepatobiliar`

## 070 — etim-v2-rai-nefr-o

**Texto:** A forma <b>nefr/o</b> refere-se a {{c1::rim}}.

**Extra:** Inglês: nephr/o; ex.: nefrite.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::05_Renal_e_urinario`

## 071 — etim-v2-rai-pyel-o

**Texto:** A forma <b>pyel/o</b> refere-se a {{c1::pelve renal}}.

**Extra:** Ex.: pielonefrite; referente a pelve renal.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::05_Renal_e_urinario`

## 072 — etim-v2-rai-lith-o

**Texto:** A forma <b>lith/o</b> refere-se a {{c1::cálculo}}.

**Extra:** Ex.: litotripsia; referente a cálculo.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::05_Renal_e_urinario`

## 073 — etim-v2-rai-neur-o

**Texto:** A forma <b>neur/o</b> refere-se a {{c1::nervo}}.

**Extra:** Ex.: neurologia; referente a nervo.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::06_Nervoso_e_sentidos`

## 074 — etim-v2-rai-miel-o

**Texto:** A forma <b>miel/o</b> refere-se a {{c1::medula óssea ou espinal}}.

**Extra:** Inglês: myel/o; ex.: mielopatia.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::06_Nervoso_e_sentidos`

## 075 — etim-v2-rai-oftalm-o

**Texto:** A forma <b>oftalm/o</b> refere-se a {{c1::olho}}.

**Extra:** Inglês: ophthalm/o; ex.: oftalmologia.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::06_Nervoso_e_sentidos`

## 076 — etim-v2-rai-oste-o

**Texto:** A forma <b>oste/o</b> refere-se a {{c1::osso}}.

**Extra:** Ex.: osteologia; referente a osso.
Exemplo de card muito óbvio, tem vários assim. vou colocar alguns nos extras, daí você identifica o padrão e não faz mais e tira os que são demais. não vou colocar todos, porque daria muito trabalho pra mim. 
Os extras também poderiam buscar palavras um pouco mais desconhecidas e que são um tequinho mais avançada, tipo aqui poderia ser Osteoporose, com uma explicação de que é osteo + porose, assim já mata dois conceitos em um só card + extra, permitindo criar um deck mais enxuto. Vários daria pra fazer isso de forma a melhorar o deck e cobrir tudo com menos cards, mas sem exagerar também. não vou indicar outros que poderiam ser assim, mas exstem vários extras nesse estilo que podem conectar conceitos e ideias. 
**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::07_Musculoesqueletico`

## 077 — etim-v2-rai-artr-o

**Texto:** A forma <b>artr/o</b> refere-se a {{c1::articulação}}.

**Extra:** Inglês: arthr/o; ex.: artrite.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::07_Musculoesqueletico`

## 078 — etim-v2-rai-mi-o

**Texto:** A forma <b>mi/o</b> refere-se a {{c1::músculo}}.

**Extra:** Inglês: my/o; ex.: miopatia.
Exemplo de card muito óbvio, tem vários assim. vou colocar alguns nos extras, daí você identifica o padrão e não faz mais e tira os que são demais. não vou colocar todos, porque daria muito trabalho pra mim. 

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::07_Musculoesqueletico`

## 079 — etim-v2-rai-tireoid-o

**Texto:** A forma <b>tireoid/o</b> refere-se a {{c1::tireoide}}.

**Extra:** Inglês: thyroid/o; ex.: tireoidite.

Exemplo de card muito óbvio, tem vários assim. vou colocar alguns nos extras, daí você identifica o padrão e não faz mais e tira os que são demais. não vou colocar todos, porque daria muito trabalho pra mim. 
**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::08_Endocrino_e_metabolico`

## 080 — etim-v2-rai-torac-o

**Texto:** A forma <b>torac/o</b> refere-se a {{c1::tórax}}.

**Extra:** Inglês: thorac/o; ex.: toracotomia.
Exemplo de card muito óbvio, tem vários assim. vou colocar alguns nos extras, daí você identifica o padrão e não faz mais e tira os que são demais. não vou colocar todos, porque daria muito trabalho pra mim. 

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::03_Respiratorio`

## 081 — etim-v2-rai-menstru-o

**Texto:** A forma <b>menstru/o</b> refere-se a {{c1::menstruação}}.

**Extra:** Ex.: menstrual; referente a menstruação.
Exemplo de card muito óbvio, tem vários assim. vou colocar alguns nos extras, daí você identifica o padrão e não faz mais e tira os que são demais. não vou colocar todos, porque daria muito trabalho pra mim. 

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::09_Reprodutor_e_obstetricia`

## 082 — etim-v2-rai-derm-o

**Texto:** A forma <b>derm/o</b> refere-se a {{c1::pele}}.

**Extra:** Ex.: dermatologia; referente a pele.
Exemplo de card muito óbvio, tem vários assim. vou colocar alguns nos extras, daí você identifica o padrão e não faz mais e tira os que são demais. não vou colocar todos, porque daria muito trabalho pra mim. 
aqui é um exemplo de extra que foi mal aplicado, poderia ser Dermatomicose, e já explicar que micose é infecção por fungos. todo mundo sabe  oque é dermatologia, não faz sentido ter um extra pra isso, melhor é buscar expandir o léxico de quem for revisar o deck com algo mais útil

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::10_Pele_imune_e_linfatico`

## 083 — etim-v2-rai-imun-o

**Texto:** A forma <b>imun/o</b> refere-se a {{c1::imunidade}}.

**Extra:** Inglês: immun/o; ex.: imunologia.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::10_Pele_imune_e_linfatico`

## 084 — etim-v2-rai-lip-o

**Texto:** A forma <b>lip/o</b> refere-se a {{c1::gordura}}.

**Extra:** Ex.: lipólise; referente a gordura.

**Deck:** `NEBLI::Etimologia::04_Raizes_por_sistema::08_Endocrino_e_metabolico`

## 085 — etim-v2-con-001-hiperplasia-hipertrofia

**Texto:** <b>hiperplasia</b> aponta para {{c1::número celular}}; <b>hipertrofia</b>, para {{c2::tamanho celular}}.

**Extra:** Hiperplasia conta células; hipertrofia aumenta cada célula.

gostei disso, o deck junta dois cards em um só, mas aí os dois clozes tem que vir no mesmo card. também dá pra melhorar a indução. aqui como seria bem melhor:

**Etimologia**. A <b>hiperplasia</b> aponta para aumento no {{c1::número celular}}; <b>hipertrofia</b>, para aumento do {{c1::tamanho celular}}.

**Deck:** `NEBLI::Etimologia::06_Familias_e_contrastes::03_Processos_confundiveis`

## 086 — etim-v2-con-002-tomia-ectomia

**Texto:** <b>-tomia</b> aponta para {{c1::incisão}}; <b>-ectomia</b>, para {{c2::remoção cirúrgica}}.

**Extra:** -tomia corta; -ectomia retira parte ou toda estrutura.

aqui os dois clozes poderiam vir juntos, diminuindo a quantidade de cards e obrigando a lembrar, porque se vem separados não sou obrigado a lembrar o que é cada um, posso só pensar que é o oposto do outro que já sei e não ter que ter o esforço de lembrar e associar corretamente, só identificar que há duas respostas e ver que uma já está preenchida. vários estão assim, corrige esse tipo de erro e não comete mais (nem nos de etimologia nem nos normais que vamos criar sempre). 
**Deck:** `NEBLI::Etimologia::06_Familias_e_contrastes::03_Processos_confundiveis`

## 087 — etim-v2-con-003-stomia-tomia

**Texto:** <b>-stomia</b> aponta para {{c1::abertura cirúrgica}}; <b>-tomia</b>, para {{c2::incisão}}.

**Extra:** -stomia cria comunicação; -tomia apenas incisa.

**Deck:** `NEBLI::Etimologia::06_Familias_e_contrastes::03_Processos_confundiveis`

## 088 — etim-v2-con-004-grafia-grama

**Texto:** <b>-grafia</b> aponta para {{c1::processo de registro}}; <b>-grama</b>, para {{c2::registro produzido}}.

**Extra:** -grafia é o exame; -grama, seu produto.
Nesse tipo de card, é essencial que o extra também tenha exemplos comparando palavras e significados com os sufixos ou prefixos abordados. 

**Deck:** `NEBLI::Etimologia::06_Familias_e_contrastes::03_Processos_confundiveis`

## 089 — etim-v2-con-005-metro-metria

**Texto:** <b>-metro</b> aponta para {{c1::instrumento}}; <b>-metria</b>, para {{c2::medição}}.

**Extra:** -metro mede; -metria é o ato ou resultado.
Nesse tipo de card, é essencial que o extra também tenha exemplos comparando palavras e significados com os sufixos ou prefixos abordados. 

**Deck:** `NEBLI::Etimologia::06_Familias_e_contrastes::03_Processos_confundiveis`

## 090 — etim-v2-con-006-aferente-eferente

**Texto:** <b>aferente</b> aponta para {{c1::em direção ao SNC}}; <b>eferente</b>, para {{c2::para fora do SNC}}.

**Extra:** A referência aqui é o sistema nervoso central.
Nesse tipo de card, é essencial que o extra também tenha exemplos comparando palavras e significados com os sufixos ou prefixos abordados. 
Como o card poderia melhorar a indução (esse tipo de detalhe é bom que você pegue e aprenda a aplicar em vários cards através de exemplares de cards com boa-indução. regra fixa não ajudaria aqui, porque fica ruim, exemplar que inspira é melhor): 

**Etimologia.** Um nervo <b>aferente</b> aponta em direção ao {{c1::SNC}}; já o <b>eferente</b>, para fora do {{c1: SNC}}.



**Deck:** `NEBLI::Etimologia::06_Familias_e_contrastes::03_Processos_confundiveis`

## 091 — etim-v2-tra-001-pancitopenia

**Texto:** Pela forma, <b>pancitopenia</b> sugere {{c1::redução das linhagens sanguíneas}}.

**Extra:** Clinicamente, envolve eritrócitos, leucócitos e plaquetas.
cloze está com muitas palavras (MÁXIMO DE 3, sendo que isso é exceção da exceção, 1 é padrão, 2 é para casos especiais e 3 só quando não tem como evitar. 
O extra também poderia melhorar mais, decompôr os morfemas e explicar a palavra realmente

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 092 — etim-v2-tra-002-oligodipsia

**Texto:** Pela forma, <b>oligodipsia</b> sugere {{c1::redução da sede}}.

**Extra:** Partes: oligo- + -dipsia.
O extra também poderia melhorar mais, decompôr os morfemas e explicar a palavra realmente

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 093 — etim-v2-tra-003-bradipneia

**Texto:** Pela forma, <b>bradipneia</b> sugere {{c1::respiração lenta}}.

**Extra:** Partes: bradi- + -pneia.
O extra também poderia melhorar mais, decompôr os morfemas e explicar a palavra realmente

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 094 — etim-v2-tra-004-taquipneia

**Texto:** Pela forma, <b>taquipneia</b> sugere {{c1::respiração rápida}}.

**Extra:** Partes: taqui- + -pneia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 095 — etim-v2-tra-005-polidipsia

**Texto:** Pela forma, <b>polidipsia</b> sugere {{c1::sede aumentada}}.

**Extra:** Partes: poli- + -dipsia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 096 — etim-v2-tra-008-amenorreia

**Texto:** Pela forma, <b>amenorreia</b> sugere {{c1::ausência de menstruação}}.

**Extra:** Partes: a- + men/o + -rreia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 097 — etim-v2-tra-009-leucopenia

**Texto:** Pela forma, <b>leucopenia</b> sugere {{c1::redução de leucócitos}}.

**Extra:** Partes: leuc/o + -penia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 098 — etim-v2-tra-012-trombocitopenia

**Texto:** Pela forma, <b>trombocitopenia</b> sugere {{c1::redução de plaquetas}}.

**Extra:** Partes: tromb/o + cit/o + -penia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 099 — etim-v2-tra-014-hipercapnia

**Texto:** Pela forma, <b>hipercapnia</b> sugere {{c1::CO2 sanguíneo aumentado}}.

**Extra:** Partes: hiper- + -capnia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 100 — etim-v2-tra-016-pneumotorax

**Texto:** Pela forma, <b>pneumotórax</b> sugere {{c1::ar no tórax}}.

**Extra:** Clinicamente, o ar ocupa a cavidade pleural.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 101 — etim-v2-tra-019-nefrolitiase

**Texto:** Pela forma, <b>nefrolitíase</b> sugere {{c1::cálculos renais}}.

**Extra:** Partes: nefr/o + lit/o + -íase.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 102 — etim-v2-tra-021-pielonefrite

**Texto:** Pela forma, <b>pielonefrite</b> sugere {{c1::inflamação da pelve e rim}}.

**Extra:** Pelve renal e parênquima participam da infecção.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 103 — etim-v2-tra-025-gastrectomia

**Texto:** Pela forma, <b>gastrectomia</b> sugere {{c1::remoção do estômago}}.

**Extra:** Partes: gastr/o + -ectomia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 104 — etim-v2-tra-026-gastrostomia

**Texto:** Pela forma, <b>gastrostomia</b> sugere {{c1::abertura no estômago}}.

**Extra:** Partes: gastr/o + -stomia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 105 — etim-v2-tra-027-gastrotomia

**Texto:** Pela forma, <b>gastrotomia</b> sugere {{c1::incisão no estômago}}.

**Extra:** Partes: gastr/o + -tomia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 106 — etim-v2-tra-032-hepatomegalia

**Texto:** Pela forma, <b>hepatomegalia</b> sugere {{c1::aumento do fígado}}.

**Extra:** Partes: hepat/o + -megalia.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 107 — etim-v2-tra-034-angiogenese

**Texto:** Pela forma, <b>angiogênese</b> sugere {{c1::formação de vasos}}.

**Extra:** Partes: angi/o + -gênese.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 108 — etim-v2-tra-035-hematopoiese

**Texto:** Pela forma, <b>hematopoiese</b> sugere {{c1::produção de células sanguíneas}}.

**Extra:** Poiese enfatiza produção de células sanguíneas.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 109 — etim-v2-tra-038-osteogenese

**Texto:** Pela forma, <b>osteogênese</b> sugere {{c1::formação óssea}}.

**Extra:** Partes: oste/o + -gênese.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 110 — etim-v2-tra-041-neurogenese

**Texto:** Pela forma, <b>neurogênese</b> sugere {{c1::formação de neurônios}}.

**Extra:** Partes: neur/o + -gênese.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 111 — etim-v2-tra-042-lipolise

**Texto:** Pela forma, <b>lipólise</b> sugere {{c1::quebra de lipídios}}.

**Extra:** Partes: lip/o + -lise.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 112 — etim-v2-tra-056-intracelular

**Texto:** Pela forma, <b>intracelular</b> sugere {{c1::dentro da célula}}.

**Extra:** Partes: intra- + celular.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 113 — etim-v2-tra-051-endocardio

**Texto:** Pela forma, <b>endocárdio</b> sugere {{c1::camada interna cardíaca}}.

**Extra:** Clinicamente, reveste internamente câmaras e válvulas.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`

## 114 — etim-v2-tra-064-transdermico

**Texto:** Pela forma, <b>transdérmico</b> sugere {{c1::através da pele}}.

**Extra:** Partes: trans- + derm/o.

**Deck:** `NEBLI::Etimologia::08_Transferencia::01_Decodificar_termo_novo`
