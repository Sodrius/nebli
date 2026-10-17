"""Inventário atômico de Geração de diversidade de anticorpos por recombinação (UC03 P1; Biologia Molecular; Prof. Alexandre
Bruni-Cardoso), escrito ANTES de escolher cards (17/10, pipeline v4). Sequência = 25 lâminas (fontes/slides.pdf = pasta pessoal = turma,
mesmo texto), vistas inteiras nesta sessão (io/g0..g2). Lido nesta sessão: as quatro transcrições (vídeos I–IV), exercícios da aula,
provas biomol-02 (3 itens), monitoria P1, apostila guia de Biologia Molecular, apostila UC3, Abbas Básica cap. 4 (V(D)J).
Correções à transcrição (seguida a literatura): a Artemis não é exclusiva do linfócito B (falta dela causa SCID); a atividade catalítica
do complexo é da RAG1; junções fora de fase são cerca de 2/3 (o vídeo diz “30%… logo 60%”).
Fronteira (MEMORY §3): V(D)J, RAG, combinação H/L, hipermutação e troca de classe têm cópias vivas (49/51/antiga 18) → sh(); TdT,
papaína/pepsina e troca para IgE são instalados pela 17 (vaga IM17 no spec); estrutura da Ig é da 17.
"""
PREFIXO = "bm18"
AULA = "Geração de diversidade de anticorpos por recombinação (UC03 P1; Biologia Molecular)"
EXC = "EXC: "
TDT, SWE = "sh-1792241814320", "sh-1792241808513"

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "As aulas do professor", [("a1", "Lista de aulas", EXC + "logística")]),
 (3, "conteudo", "Bibliografia (Alberts, Watson, Lewin)", [("a2", "Bibliografia", EXC + "referências")]),
 (4, "conteudo", "Meta e objetivos", [("a3", "Objetivos", EXC + "lista de objetivos; cada item tem card")]),
 (5, "conteudo", "Antígeno, anticorpo, epítopo de 10–12 aminoácidos", [("a4", "Desafio: ~10^13 epítopos possíveis", "au-desafio")]),
 (6, "conteudo", "Seleção clonal e expansão (Lewin, Alberts)", [("a5", "Um clone, uma especificidade", "au-desafio")]),
 (7, "conteudo", "Desenvolvimento de B e T (medula, timo)", [("a6", "V(D)J nos linfócitos imaturos", "sh-1791629589247")]),
 (8, "conteudo", "Estrutura das Ig: sítio de ligação nas regiões variáveis", [("a7", "Cadeias kappa ou lambda", "sh-1791629590897")]),
 (9, "conteudo", "Mais de 10^12 Ig com ~25.000 genes", [("a8", "Genes insuficientes", "au-desafio")]),
 (10, "conteudo", "Regiões V e C; tabela das classes", [("a9", "Classes pela região constante", EXC + "estrutura e classes: aula 17")]),
 (11, "conteudo", "Recombinação V–J (kappa) e locus da cadeia pesada", [("a10", "Recombinação irreversível", ["au-irreversivel", "sh-1791627547052"]),
  ("a11", "VJ na leve, VDJ na pesada; D-J primeiro", ["sh-1791629589797", "sh-1791629589497", "sh-1791629589672"])]),
 (12, "conteudo", "Diversificação combinatória (35×5 kappa; 40×23×6 pesada; ×H/L)", [("a12", "Combinatória", ["au-desafio", "sh-1791629589120"])]),
 (13, "conteudo", "RSS: heptâmero, espaçador 12 ou 23, nonâmero; regra 12/23", [("a13", "Regra 12/23", "au-regra-12-23")]),
 (14, "conteudo", "Exclusão alélica", [("a14", "Exclusão alélica", "au-exclusao-alelica")]),
 (15, "conteudo", "Primeiro passo: RAG1 e RAG2", [("a15", "RAG1/RAG2", ["sh-1791629589372", "sh-1792166982691"])]),
 (16, "conteudo", "RAG: corte, sinapse, grampo", [("a16", "Grampo", "au-regra-12-23")]),
 (17, "conteudo", "Diversidade juncional: perda e inserção de nucleotídeos; TdT", [("a17", "Nucleotídeos P e N", ["au-juncional", TDT])]),
 (18, "conteudo", "Segundo passo: JNHE", [("a18", "JNHE", ["ak-nhej-ciclo", "ak-artemis"])]),
 (19, "conteudo", "Recombinação homóloga (cromátide irmã) × JNHE", [("a19", "HR × JNHE", ["ak-ds-break", "ak-hr-cromatide", "ak-hr-fiel", "sh-1791630175220"])]),
 (20, "conteudo", "JNHE: Ku, nucleases, polimerases, ligase; perde nucleotídeos", [("a20", "JNHE é mutagênica", ["sh-1791630175220", "ak-reparo-scid", "ak-ataxia"])]),
 (21, "conteudo", "Segundo passo da V(D)J: grampo aberto, junção codificadora, círculo descartado", [("a21", "Junção", "au-juncional")]),
 (22, "conteudo", "Hipermutação somática: AID, U:G, UNG, sítio abásico, polimerases translesão",
  [("a22", "AID e hipermutação", ["au-aid", "sh-1791629595072", "sh-1791629594472", "ak-desaminacao"]), ("a23", "UNG e sítio AP", ["ak-ber-desaminacao", "ak-glicosilase"])]),
 (23, "conteudo", "Troca de classe por recombinação (não gera diversidade)",
  [("a24", "Troca de classe", ["au-troca-dna", "sh-1791629594096", "sh-1791625431383", "sh-1791629594773", SWE, "sh-1792166990290", "sh-1792166990541"])]),
 (24, "conteudo", "Mecanismos que geram diversidade", [("a25", "Combinatória, juncional, H/L, JNHE, hipermutação", ["au-desafio", "sh-1791629589120", "au-juncional", "au-aid"])]),
 (25, "conteudo", "Consequências: B sem Ig funcional ou autorreativo", [("a26", "Junção fora de fase não produtiva", "au-juncional"),
  ("a27", "Filtragem dos autorreativos", EXC + "tolerância central: aula de imunologia (pergunta provocativa)")]),
]
JUSTIFICATIVAS = {"capa": "capa sem conteúdo"}
CAPITULO = [("Abbas Básica cap. 4 (recombinação V(D)J) e Alberts cap. 24", [
 ("l1", "Segmentos V, D, J e recombinação", ["au-irreversivel", "sh-1791629589497"]), ("l2", "RSS e RAG", ["au-regra-12-23", "sh-1791629589372"]),
 ("l3", "Diversidade juncional e TdT", "au-juncional"), ("l4", "AID e hipermutação", "au-aid")])]
EXERCICIOS = [
 ("Exercícios da aula", [
   ("e1", "Antígeno, epítopo, anticorpo", "au-desafio"), ("e3", "Passos da V(D)J na leve e na pesada", ["au-irreversivel", "sh-1791629589672"]),
   ("e4", "Como RAG reconhece os segmentos; V sempre com J", "au-regra-12-23"), ("e5", "Cálculo da diversidade combinatória", "au-desafio"),
   ("e6", "Diversidade juncional", "au-juncional"), ("e7", "Diversidade após ativação", "au-aid"), ("e8", "Resposta policlonal ao gp120", "au-desafio")]),
 ("Provas UC03 (índice biomol-02)", [
   ("p1", "Mecanismos da recombinação para formar IgG (RSS 12/23, RAG) (2024 P1 1.6)", ["au-regra-12-23", "au-troca-dna"]),
   ("p2", "Hipermutação somática: gatilho, mecanismo e consequência (2023 P1 2.8)", ["au-aid", "sh-1791629594472"]),
   ("p3", "Mecanismos de diversidade e troca de classe (2018 P1 1.14)", ["au-juncional", "au-troca-dna"])]),
]
