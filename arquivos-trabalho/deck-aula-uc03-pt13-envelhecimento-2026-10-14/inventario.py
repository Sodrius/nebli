"""Inventário de Envelhecimento celular e tecidual (UC03 P1; Patologia; 22 lâminas), escrito antes da seleção (14/10).
Material: lâminas (visual/folha-01..04), transcrição da aula, palavras-cruzadas com gabarito, provas pat-04, Robbins cap. 1 (envelhecimento)."""
PREFIXO = "pt13"
AULA = "Envelhecimento celular e tecidual (UC03 P1; Patologia)"
EXC = "EXC: "
S = lambda n: f"sh-{n}"
SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Definições: senescência e senilidade", [("a1", "Senescência × senilidade", "a-senescencia")]),
 (3, "conteudo", "Reserva funcional", [("a2", "Reserva funcional", "a-reserva")]),
 (4, "conteudo", "Mecanismos gerais", [("a3", "Esquema geral", "b-mecanismos")]),
 (5, "conteudo", "Senescência celular", [("a4", "Replicação reduzida", "b-telomeros"), ("a4b", "Reparo lento no idoso", "b-cicatrizacao")]),
 (6, "conteudo", "Telômeros", [("a5", "Encurtamento", "b-telomeros"), ("a6", "Células germinativas/tronco", "b-celulas-telomerase"), ("a7", "Câncer", "ak-telomerase-cancer"), ("a7b", "TTAGGG, transcriptase reversa, DNA quebrado", ["ak-ttaggg", "ak-telomerase-rt", "b-dna-quebrado"])]),
 (7, "conteudo", "Dano ao DNA", [("a8", "Mutações", "b-mecanismos")]),
 (8, "conteudo", "Radicais livres", [("a9", "Fontes e dano; antioxidantes", [S(1792026498880), "b-antioxidantes"])]),
 (9, "conteudo", "Homeostase proteica", [("a10", "Proteínas danificadas", ["b-mecanismos", "b-proteostase"])]),
 (10, "conteudo", "Sensores de nutrientes", [("a11", "Insulina/IGF, TOR, sirtuínas", ["b-sirtuinas", "b-igf"])]),
 (11, "conteudo", "Síndrome de Werner", [("a12", "Envelhecimento precoce", "b-werner")]),
 (12, "conteudo", "Aspectos gerais", [("a13", "Pele", "ak-rugas"), ("a14", "Presbiacusia", "ak-presbiacusia"), ("a15", "Presbiopia", "ak-presbiopia"), ("a15b", "Estatura, água, pele, sentidos", "c-gerais"),
   ("a16", "Estatura, peso, água, pelos, olfato", "c-gerais")]),
 (13, "conteudo", "Respiratório", [("a17", "Elasticidade pulmonar", "ak-complacencia-pulmonar")]),
 (14, "conteudo", "Respiratório: VEF1", [("a18", "Queda do VEF1", ["ak-complacencia-pulmonar", "c-pulmao-idoso", "c-tabagismo"])]),
 (15, "conteudo", "Sistema nervoso", [("a19", "Perda neuronal", ["a-senescencia", "c-cerebro"]), ("a19b", "Uso mantém reserva", "c-uso"), ("a20", "Lipofuscina", S(1792026992843))]),
 (16, "conteudo", "Alzheimer × normal", [("a21", "Alzheimer como senilidade", "a-senescencia")]),
 (17, "conteudo", "Cardiovascular", [("a22", "Rigidez vascular; valvas e ventrículo", ["ak-rigidez-arterial", "c-coracao"])]),
 (18, "conteudo", "Urinário", [("a23", "Queda da TFG e do fluxo", ["c-tfg", "c-fluxo-renal"]), ("a23b", "Concentração urinária", "c-urina"), ("a23c", "Doação de rim e hiperplasia compensatória", "c-doacao")]),
 (19, "conteudo", "Locomotor", [("a24", "Massa muscular e óssea (sarcopenia, creatinina)", "c-sarcopenia")]),
 (20, "conteudo", "Coração (lipofuscina, débito)", [("a25", "Débito e rigidez", "ak-rigidez-arterial")]),
 (21, "conteudo", "Resumo (tabela)", [("a26", "Tabela", "c-sistemas")]),
 (22, "capa", "Ilustração", []),
]
JUSTIFICATIVAS = {1: "capa", 22: "ilustração"}
CAPITULO = [("Robbins cap. 1 (envelhecimento celular)", [("l1", "Mecanismos", "b-mecanismos"), ("l2", "Telômeros", "b-telomeros"), ("l3", "Sirtuínas", "b-sirtuinas")])]
EXERCICIOS = [
 ("Provas UC03 (pat-04)", [("p1", "2024 P1 1.3: senescência × senilidade", "a-senescencia"), ("p2", "2017 P1 1.5: TFG do idoso", "c-tfg"), ("p2b", "creatinina baixa no idoso", "c-sarcopenia"),
   ("p3", "2016 P1 3.5, 2015 P1sub 3.6, 2019 P1 1.3: reserva funcional", "a-reserva"), ("p4", "2016 P3 2.5: telomerase", ["ak-telomerase-cancer", "b-telomeros"])]),
 ("Palavras-cruzadas", [("x1", "Metade (TFG)", "c-tfg"), ("x2", "Somáticas/germinativas", "b-celulas-telomerase"), ("x3", "Sirtuínas", "b-sirtuinas"),
   ("x4", "Elasticidade/turgor", "ak-rugas"), ("x5", "Telômeros/encurtamento/senescência", "b-telomeros"), ("x6", "Lipofuscina", S(1792026992843)),
   ("x7", "Werner", "b-werner"), ("x8", "Senilidade", "a-senescencia"), ("x9", "Reserva funcional", "a-reserva"), ("x10", "Dose menor", "c-tfg")]),
]
