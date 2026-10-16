"""Mantém síndromes por cima e HIV/hipersensibilidade apenas como pontes."""
from nebli import explicacoes


TEXTOS = {
    1792166978490: """Quando a imunidade celular falha, perde-se parte da vigilância que contém vírus latentes e elimina clones linfocitários anormais. Por isso imunodeficiências, inclusive a causada pelo HIV, aumentam o risco de neoplasias de linfócitos; a reativação do vírus Epstein–Barr em células B é um mecanismo importante dessa associação.

O exemplo clássico é o linfoma não Hodgkin, que pode produzir linfonodos aumentados em várias regiões e sintomas B, como febre, sudorese noturna e perda de peso. A síndrome serve aqui para mostrar uma consequência da falha imune, não para aprofundar a classificação dos linfomas.""",
    1792166989443: """Na deficiência seletiva de IgA, o organismo não produz IgA e pode reconhecer como estranha a IgA presente em sangue ou imunoglobulina administrada. Após formar anticorpos contra essa proteína, uma nova exposição pode desencadear uma reação sistêmica rápida.

Essa reação é a anafilaxia: ativação ampla de células inflamatórias causa vasodilatação, aumento da permeabilidade e broncoconstrição. Aqui ela funciona apenas como ponte para hipersensibilidade; o ponto da imunodeficiência é entender por que a ausência de IgA permite reagir contra a IgA recebida.""",
    1792166995970: """O HIV reduz progressivamente os linfócitos T CD4+, que coordenam a imunidade celular e ajudam outras células da resposta adaptativa. A contagem dessas células no sangue funciona, portanto, como uma medida do grau de imunodeficiência.

O critério numérico de AIDS é uma contagem de CD4 abaixo de 200 células por mm³. O outro caminho é ter HIV confirmado e uma condição definidora de AIDS, como determinadas infecções oportunistas. Ambos os critérios representam a mesma falha central: perda grave da defesa dependente de células T CD4+.""",
}


def main():
    db = explicacoes.open_store()
    version = explicacoes.style_version(explicacoes.STYLE.read_text(encoding="utf-8"))
    for card_id, texto in TEXTOS.items():
        problema = explicacoes.problema_estilo(texto)
        if problema:
            raise SystemExit(f"{card_id}: {problema}")
        changed = db.execute(
            "update explicacoes set status='ok', texto=?, motivo=null, estilo=?, modelo='curadoria-codex', gerado_em=datetime('now','localtime') where card_id=?",
            (texto, version, card_id),
        ).rowcount
        if changed != 1:
            raise SystemExit(f"card ausente: {card_id}")
    db.commit()
    print(f"{len(TEXTOS)} Tabs ajustados à fronteira da aula 51.")


if __name__ == "__main__":
    main()
