"""Inventário atômico de Reconhecimento pelo sistema imune na resposta adquirida (UC03 P1; Imunologia; Prof. José Alexandre Barbuto),
escrito ANTES de escolher cards (17/10, pipeline v4). Sequência = 18 lâminas (fontes/slides.pdf = Anb.pdf da turma; o .ppsx pessoal tem as
mesmas 18 + uma 19ª só com leitura complementar), vistas inteiras nesta sessão (io/g0..g1). Lido nesta sessão: transcrição integral,
provas imuno-03 (22 itens), monitoria P1, apostila guia de Imunologia, apostila UC3, mapa imunológico 1, Abbas Básica cap. 4 (anticorpos).
Ênfase do professor: a troca de classe muda a avidez, não a especificidade nem a afinidade.
Fronteira (MEMORY §3): estrutura do BCR, classes de Ig e troca de classe têm cópias vivas da 49 (Ativação de células B) e da 18
(Recombinação) → sh(); especificidade e memória da resposta adaptativa são da 07 (vaga IM07 no spec); restrição ao MHC é da 20 → sh().
"""
PREFIXO = "im17"
AULA = "Reconhecimento pelo sistema imune na resposta adquirida (UC03 P1; Imunologia)"
EXC = "EXC: "
ESP, MEM = "sh-IM07-ESPEC", "sh-IM07-MEMORIA"

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Objetivos: seleção de receptores, anticorpos, troca de classes", [("a1", "Objetivos", EXC + "lista de objetivos; cada item tem card")]),
 (3, "conteudo", "Repertório completo gerado ao acaso + seleção nos órgãos linfoides primários",
  [("a2", "Um receptor por linfócito, repertório completo", ["sh-1791629587397", "ak-tcr-unico"])]),
 (4, "conteudo", "Reconhecimento composto: APC, linfócito T e B; B reconhece direto",
  [("a3", "TCR só vê antígeno com MHC", ["sh-1791625424832", "sh-1791629588997"])]),
 (5, "conteudo", "Especificidade e memória (bactéria X × Y atenuada)", [("a4", "Especificidade e memória", [ESP, MEM])]),
 (6, "conteudo", "Imunidade humoral (soro) × celular (células)",
  [("a5", "Transferência por soro × células", "au-humoral-celular"), ("a6", "Humoral: anticorpos de plasmócitos", ["ak-humoral", "sh-1791625429833"])]),
 (7, "conteudo", "Eletroforese do soro; hiperimunização aumenta gamaglobulinas", [("a7", "Anticorpos são gamaglobulinas", "au-gamaglobulinas")]),
 (8, "conteudo", "Gamaglobulinas heterogêneas; mieloma múltiplo com pico monoclonal",
  [("a8", "Mieloma: plasmócitos monoclonais e pico M", ["ak-mm-monoclonal", "ak-mm-spike", "ak-mm-igg"])]),
 (9, "conteudo", "Dreyer & Bennett 1965: porção comum e variável nas proteínas do mieloma", [("a9", "Constante × variável", ["au-tonegawa", "ak-mm-bence-jones"])]),
 (10, "conteudo", "Troca de classes: IgM → IgG com mesma especificidade e afinidade",
  [("a10", "Troca de classes", ["au-avidez", "sh-1791629594646", "sh-1791629594096", "sh-1791625431383", "sh-1791629594773", "ak-switch-ige"])]),
 (11, "conteudo", "Estrutura: papaína (Fab/Fc), pepsina (Fab'2), cadeias L e H, domínios, C e V, κ e λ",
  [("a11", "Papaína e pepsina", ["ak-papaina", "ak-pepsina"]), ("a12", "Cadeias pesadas e leves", ["sh-1791629588622", "sh-1791629588747", "sh-1791629588145", "sh-1791629590722"]),
   ("a13", "Sítio de ligação nas regiões variáveis", "au-cdr")]),
 (12, "conteudo", "Isotipos, alotipos, idiotipos", [("a14", "Isotipo e idiotipo", ["sh-1791629588447", "sh-1791629588272"]), ("a15", "Alotipos", "au-alotipos")]),
 (13, "conteudo", "Propriedades: ligação pelo Fab; neutralização, bloqueio, transporte, opsonização, complemento, ativação (Fc)",
  [("a16", "Funções do Fc", ["sh-1791629595321", "sh-1791629595747", "sh-1791629597298", "sh-1791629597547", "sh-1791629595996"])]),
 (14, "conteudo", "IgM no início; IgG madura; IgE emergências; IgA mucosas",
  [("a17", "IgM", ["sh-1791629591646", "sh-1791629597922", "ak-igm-primaria", "ak-igm-placenta", "ak-igm-10", "ak-valencia", "ak-igm-valencia"]),
   ("a18", "IgG", ["sh-1791629598047", "ak-igg-abundante", "ak-afinidade", "ak-igg-afinidade"]),
   ("a19", "IgE", ["sh-1791629596372", "ak-ige-hipersensibilidade", "sh-1791629596247", "ak-ige-rara"]),
   ("a20", "IgA", ["sh-1791629596622", "ak-iga-monomero", "sh-1791629591820", "sh-1791629596922", "ak-iga-tgi", "sh-1791629597172", "ak-iga-complemento",
                   "ak-iga-placenta", "sh-1791629596747", "sh-1791629597045"])]),
 (15, "conteudo", "O tipo de Ig não afeta a especificidade", [("a21", "IgM e IgD no B naive; um isotipo por plasmócito",
  ["sh-1791629591997", "ak-plasmocito-um", "ak-monomero", "sh-1791629591146"])]),
 (16, "conteudo", "Geração de diversidade: Jerne, Tonegawa, recombinação somática",
  [("a22", "Tonegawa", "au-tonegawa"), ("a23", "V(D)J, RAG, TdT, combinação H/L, hipermutação",
   ["sh-1791629589497", "sh-1791629589672", "sh-1791629589797", "sh-1791629589372", "ak-tdt", "sh-1791629589120", "sh-1791629594472"])]),
 (17, "conteudo", "TCR: diversidade pelo mesmo mecanismo (Allison, Davis)",
  [("a24", "TCR αβ, CD3, rígido, clonalidade", ["sh-1791629588872", "sh-1791625428158", "ak-tcr-rigido", "ak-tcr-clonalidade"])]),
 (18, "conteudo", "Resumo", [("a25", "Resumo", ["au-humoral-celular", "au-avidez", "au-tonegawa"])]),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo"}
CAPITULO = [("Abbas Básica cap. 4 (anticorpos)", [
 ("l1", "Estrutura, Fab/Fc, regiões hipervariáveis (CDR)", ["au-cdr", "ak-papaina"]), ("l2", "Isotipos e funções", "sh-1791629595321"),
 ("l3", "Troca de classe preserva especificidade", "au-avidez")])]
EXERCICIOS = [
 ("Provas UC03 (índice imuno-03)", [
   ("p1", "Eletroforese de proteínas no mieloma (2024 P1 1.4)", ["ak-mm-spike", "au-gamaglobulinas"]),
   ("p2", "Fragmentos cristalizável e não cristalizável; qual liga o antígeno (2024 P1 1.7)", ["ak-papaina", "sh-1791629588272"]),
   ("p3", "Fab e Fc no BCR × anticorpo secretado (2024 P3 3.2)", ["sh-1791629591997", "sh-1791629591646"]),
   ("p4", "Desenhar a Ig: reconhecimento × funções; mecanismos de diversidade (2018 P1 1.14)", ["au-cdr", "sh-1791629589120", "ak-tdt"]),
   ("p5", "IgM → IgG com a mesma especificidade: mecanismo e vantagem (2017 P1 4.4)", ["au-avidez", "sh-1791629594646"]),
   ("p6", "Mecanismos antivirais dependentes de Fab e Fc (2017 P3 1.6)", ["au-cdr", "sh-1791629595321", "sh-1791629595747"]),
   ("p7", "Identificar IgG materna, IgM e IgE (2015 P2 5.1)", ["sh-1791629597298", "sh-1791629597922", "sh-1791629596372"]),
   ("p8", "Como a IgA chega à luz intestinal (2015 P2 5.3)", ["sh-1791629596747", "sh-1791629597045"]),
   ("p9", "Elemento selecionador do TCR: MHC (2015 P2 6.1)", "sh-1791625424832")]),
]
