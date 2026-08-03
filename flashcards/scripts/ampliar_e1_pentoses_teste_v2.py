#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().parents[2] / "typst-build/_par_bioq-20-pentoses-radicais-livres-teste/etapa1.typ"
text = path.read_text(encoding="utf-8")
tag = '#subtopico("3.5 — Dois usos adicionais do NADPH'
if tag not in text:
    text += r'''

#subtopico("3.5 — Dois usos adicionais do NADPH que explicam por que a via aparece em tantos tecidos")

O NADPH não serve apenas para fabricar lipídios ou manter a glutationa carregada. No fígado, ele alimenta o sistema do citocromo P450, que participa do metabolismo de moléculas lipossolúveis. Já nos neutrófilos, o mesmo poder redutor é entregue à NADPH oxidase durante o surto respiratório: a enzima transfere elétrons ao oxigênio para formar espécies reativas que ajudam a matar microrganismos no fagolisossomo. A mesma moeda pode sustentar síntese, detoxificação ou defesa antimicrobiana; o contexto celular decide a enzima que recebe seus elétrons.

#subtopico("3.6 — O detalhe que integra vitaminas e rearranjo de carbonos")

A transcetolase da fase não-oxidativa precisa de pirofosfato de tiamina, a forma coenzimática da vitamina B1. Isso explica por que uma enzima que transfere uma unidade de dois carbonos não é apenas um nome da rota: a tiamina estabiliza esse fragmento durante a transferência. A fase não-oxidativa combina, assim, uma ferramenta química específica com a função precisa de contabilidade de carbonos.

#conclusao-box[
  A via das pentoses-fosfato transforma a glicose-6-fosfato em duas reservas que a célula usa quando construir e proteger importa mais que produzir ATP: ribose para nucleotídeos e NADPH para doação de elétrons. A fase oxidativa fabrica esse poder redutor; a não-oxidativa redistribui os carbonos conforme a demanda. Na hemácia, G6PD, NADPH e glutationa formam uma única linha de defesa contra peróxidos: quebrar qualquer elo permite oxidação da hemoglobina, corpos de Heinz e hemólise. Esse mesmo NADPH também explica a lipogênese hepática, o P450 e o surto respiratório dos neutrófilos — uma via curta, com usos metabólicos muito diferentes porque fornece a mesma moeda redutora a enzimas distintas.
]
'''
    path.write_text(text, encoding="utf-8")
print("OK: E1 recebeu aprofundamento Step 1 e conclusão integradora")
