"""Qualifica afirmações ambíguas nos Tabs sem editar os cards correspondentes."""

import time

from nebli.decks import Anki
from nebli.explicacoes import STYLE, card_hash, open_store, style_version


TEXTOS = {
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
