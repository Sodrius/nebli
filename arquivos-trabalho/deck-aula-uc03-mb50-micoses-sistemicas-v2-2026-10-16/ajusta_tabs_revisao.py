"""Resolve Tabs que o gerador recusou por ambiguidade, sem alterar os cards."""

import time

from nebli.decks import Anki
from nebli.explicacoes import STYLE, card_hash, open_store, style_version


TEXTOS = {
    1792065031184: """A parede dos fungos contém β-glucanos, polímeros que ajudam a sustentar a célula contra a pressão osmótica. Como células humanas não possuem essa parede, a síntese de β-glucano oferece um alvo com seletividade para o fungo.

As equinocandinas inibem a β-1,3-D-glucano-sintase e enfraquecem a parede celular. Essa é a lógica que distingue seu alvo do ergosterol da membrana, atingido diretamente pelos polienos ou indiretamente pelos azóis.""",
    1792065031185: """A flucitosina entra na célula fúngica por uma permease e é convertida em metabólitos que interferem na síntese de DNA e de RNA. A seletividade depende dessa ativação no fungo, embora a resistência possa surgir rapidamente quando o fármaco é usado sozinho.

Assim, entre os principais alvos dos antifúngicos, a flucitosina corresponde ao bloqueio da síntese de ácidos nucleicos. Ela contrasta com polienos e azóis, que atuam sobre o ergosterol, e com equinocandinas, que reduzem o β-glucano da parede.""",
    1791628676074: """Actinomyces são bacilos Gram-positivos filamentosos que integram a microbiota da boca e de outras mucosas. Muitas espécies clinicamente relevantes crescem melhor em anaerobiose ou em baixa tensão de oxigênio; por isso, chamar todo o gênero de anaeróbio obrigatório é uma simplificação, embora A. israelii seja o exemplo clássico anaeróbio associado à doença humana.

A infecção costuma aparecer quando trauma, procedimento dentário ou outra ruptura da mucosa leva o organismo aos tecidos profundos. O resultado pode ser uma infecção odontogênica crônica com abscessos, trajetos fistulosos e grânulos de enxofre, e não uma invasão espontânea da gengiva íntegra.""",
    1791628676075: """O gênero Actinomyces reúne bacilos Gram-positivos filamentosos da microbiota oral, gastrointestinal e genital. As espécies de importância clínica toleram pouco oxigênio e incluem organismos anaeróbios ou microaerófilos; portanto, “anaeróbio obrigatório” descreve bem o exemplo clássico A. israelii, mas não deve ser tomado como regra absoluta de todo o gênero.

Quando a barreira mucosa é rompida, sobretudo em contexto odontogênico, esses organismos podem alcançar planos profundos e produzir abscessos crônicos, fibrose e fístulas. A localização habitual na boca explica a associação com infecção dentária, enquanto a ruptura tecidual explica a passagem de comensal a patógeno.""",
    1792176897408: """As micoses sistêmicas adquiridas por inalação variam muito em gravidade. Formas pulmonares leves e autolimitadas podem não precisar de antifúngico, enquanto doença sintomática persistente, extensa ou extrapulmonar exige tratamento; a decisão depende do agente, do hospedeiro e da forma clínica.

O itraconazol é uma opção importante para várias formas leves a moderadas de histoplasmose, blastomicose e coccidioidomicose. Ele não é, porém, uma resposta universal para qualquer “infecção local”: quadros graves ou disseminados frequentemente começam com anfotericina B, e cada micose tem indicações e durações próprias.""",
    1792176898257: """A queda de linfócitos T CD4 compromete a imunidade celular que contém Candida nas mucosas. A candidíase esofágica torna-se mais provável na imunossupressão avançada, sendo frequentemente associada a contagens abaixo de 200 células/mm³, mas não existe um limiar biológico rígido a partir do qual ela obrigatoriamente surge.

O valor de 100 células/mm³ pode aparecer como marcador de imunossupressão muito intensa, mas não deve ser memorizado como fronteira exclusiva para esofagite por Candida. Clinicamente, a candidíase esofágica é uma condição definidora de AIDS independentemente da contagem de CD4.""",
    1792176900503: """Na candidemia e em outras formas invasivas, a escolha inicial precisa oferecer atividade sistêmica confiável enquanto se identifica a espécie e sua sensibilidade. Por isso, uma equinocandina como caspofungina é frequentemente usada de início, sobretudo em pacientes graves ou com possibilidade de resistência a azóis.

A anfotericina B é uma alternativa importante em situações selecionadas, mas não funciona como “segunda linha” universal. Fluconazol também pode ser inicial em pacientes estáveis e com baixa probabilidade de resistência; espécie, foco, gravidade, função orgânica e penetração no tecido acometido orientam a escolha e a transição do tratamento.""",
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
