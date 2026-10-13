"""Inventário atômico de Regulação da expressão gênica em eucariotos II (UC03 P3, Biologia Molecular; Prof. Alexandre Bruni-Cardoso;
53 lâminas; pasta pessoal 52 vazia). Escrito em 10/10/2026 antes da seleção: lâminas (visual/folha-NN), "transcrição" da turma (texto da
versão anterior, com objetivos e o bloco de iPS), monitoria P3 aula 5 (fontes/monitoria-p3.txt; erro notado: HP1 tem cromodomínio, não
bromodomínio), provas do índice biomol-07/08 (cromatina: 2025 P3 1.5, 2024 P3 2.10), Alberts 5ª cap. 4/7.
"""
PREFIXO = "bm52"
AULA = "Regulação da expressão gênica em eucariotos II (UC03 P3; Prof. Alexandre Bruni-Cardoso)"
EXC = "EXC: "

SLIDES = [
 (1, "capa", "Capa", []),
 (2, "conteudo", "Tópicos", [("topicos", "Cromatina, remodeladores, silenciamento, epigenética", "basal-restritivo")]),
 (3, "conteudo", "Procariotos × eucariotos", [("basal", "Mesmos princípios; em eucariotos o estado basal é restritivo (transcrição)", "basal-restritivo")]),
 (4, "conteudo", "Fibras de 10 e 30 nm", [("fibras", "Colar de pérolas 10 nm; fibra de 30 nm", ["nucleossomo", "fibra-30"])]),
 (5, "conteudo", "Cromatina formada por nucleossomos", [("nucleossomo", "Nucleossomo", "nucleossomo")]),
 (6, "conteudo", "Histonas do core", [("core", "H2A, H2B, H3, H4 em pares", "octamero")]),
 (7, "conteudo", "Estrutura do nucleossomo", [("estrutura", "DNA enrola ~2 voltas no octâmero", "octamero")]),
 (8, "conteudo", "Histona H1", [("h1", "H1 é histona de ligação", "h1")]),
 (9, "conteudo", "Afinidade das histonas pelo DNA", [("carga", "Proteínas básicas (lisina, arginina) × DNA negativo", "lisina-arginina")]),
 (10, "conteudo", "Caudas e fibra de 30 nm", [("caudas", "Caudas necessárias para a fibra de 30 nm", "caudas")]),
 (11, "capa", "Tópicos (divisória)", []),
 (12, "conteudo", "Como fatores encontram o DNA", [("pergunta", "Pergunta da aula", "tf-remodelador")]),
 (13, "conteudo", "Três estratégias", [("estrategias", "Ligar após replicação; ligar cromatina fechada e recrutar remodeladores; remodeladores afrouxam", "tf-remodelador")]),
 (14, "conteudo", "Três estratégias (figura)", [("estrategias-fig", "Esquema 1–3", "tf-remodelador")]),
 (15, "conteudo", "Cromatina dinâmica", [("dinamica", "Modificações não covalentes e covalentes", "remodelador-atp")]),
 (16, "conteudo", "Remodeladores dependentes de ATP", [("remodel", "Reposicionam nucleossomos (deslocamento, transferência, afrouxamento)", "remodelador-atp")]),
 (17, "conteudo", "Transcrição desaloja nucleossomos", [("transcricao", "Octâmero deslocado e reassociado", "pol-desaloja")]),
 (18, "conteudo", "Modificações covalentes", [("covalentes", "Modificações das caudas", "hat")]),
 (19, "conteudo", "HAT e HDAC", [("hat", "HAT acetila ε-amino da lisina", "hat"), ("hdac", "HDAC remove", "hdac")]),
 (20, "conteudo", "Lisinas acetiladas", [("lisinas", "Lisinas (K) acetiladas/desacetiladas", ["hat", "hdac"])]),
 (21, "conteudo", "Pergunta: acetilação compacta ou descompacta?", [("perg", "Pergunta", "acetil-carga")]),
 (22, "conteudo", "Acetilação diminui afinidade", [("afinidade", "Menos afinidade pelo DNA; enfraquece nucleossomos adjacentes", ["acetil-carga", "sh-1791627547302", "desacetilada"])]),
 (23, "conteudo", "Metilação e fosforilação", [("outras", "Histonas também metiladas e fosforiladas", "outras-mod")]),
 (24, "conteudo", "Tabela de modificações", [("tabela", "Modificações em cadeias laterais", "outras-mod")]),
 (25, "conteudo", "Modificações dinâmicas (vídeo Allis)", [("allis", "Link de vídeo", EXC + "link externo")]),
 (26, "conteudo", "Modificações recrutam proteínas", [("recruta", "Recrutam proteínas específicas", "leitores")]),
 (27, "conteudo", "Complexo reader", [("reader", "Combinação reconhecida por reader (código de histonas)", ["codigo", "leitores"])]),
 (28, "conteudo", "Ativadores descondensam", [("ativ", "Menor condensação", "ativador-cromatina")]),
 (29, "conteudo", "Ativadores recrutam remodeladores", [("ativ2", "Maquinaria + remodeladores + HAT (Swi5/SBF no HO)", ["ativador-cromatina", "ho-swi5"])]),
 (30, "conteudo", "Repressores condensam", [("rep", "Maior condensação", "repressor-cromatina")]),
 (31, "capa", "Tópicos (divisória)", []),
 (32, "conteudo", "Heterocromatina × eucromatina", [
   ("hetero", "Heterocromatina condensada, inativa", ["sh-1791627547178", "hetero-condensada"]),
   ("const", "Constitutiva: centrômeros, repetições", "constitutiva"),
   ("fac", "Facultativa: tipo celular, ciclo, X", "facultativa"),
   ("eu", "Eucromatina menos condensada, ativa", "eucromatina-me")]),
 (33, "conteudo", "Eucromatina e heterocromatina (ME)", [("me", "Aparência na microscopia eletrônica", ["hetero-me", "eucromatina-me"])]),
 (34, "conteudo", "Modificações e heterocromatina", [("hp1", "HMT metila H3 → HP1 → silenciamento", "hp1")]),
 (35, "conteudo", "Metilação do DNA", [("dnmt", "DNMT + SAM → 5-metilcitosina em CG", "dnmt")]),
 (36, "conteudo", "Ilhas CpG", [("ilhas", "CpG concentradas em promotores", "ilhas-cpg")]),
 (37, "conteudo", "~80% dos CpG metilados", [("80", "Maioria metilada; ilhas não", "cpg-80")]),
 (38, "conteudo", "Metilação define promotor ativo", [("promotor", "Metilação silencia o promotor", "cpg-reprime")]),
 (39, "conteudo", "Citosinas metiladas recrutam HDAC", [("recruta-hdac", "Recrutam HDACs e remodeladores", "dna-hdac")]),
 (40, "conteudo", "CpG metiladas e metilases de histonas", [("hmt", "Metilação de DNA e histona se reforçam", ["hp1", "cpg-reprime"])]),
 (41, "capa", "Tópicos (divisória)", []),
 (42, "conteudo", "Definição de epigenética", [("def", "Herdável sem mudar a sequência", "epigenetica")]),
 (43, "conteudo", "Modificações epigenéticas", [("tipos", "Histonas e metilação do DNA, herdadas nas divisões", "epigenetica")]),
 (44, "conteudo", "Modificações de histonas herdadas", [("heranca-hist", "Marcas de histona copiadas", "epigenetica")]),
 (45, "conteudo", "DNMT de manutenção", [("manutencao", "Mantém metilação após replicação", "manutencao")]),
 (46, "conteudo", "Figura 7-87", [("fig", "Herança da metilação", "manutencao")]),
 (47, "conteudo", "Gêmeos monozigóticos", [("gemeos", "Diferenças de metilação com a idade", "gemeos")]),
 (48, "conteudo", "Abelha rainha", [("abelha", "Nutrição e epigenética", "abelha")]),
 (49, "conteudo", "Geleia real e Dnmt3", [("geleia", "Reduz Dnmt3; siRNA contra dnmt3 gera rainhas", "abelha")]),
 (50, "conteudo", "Epigenética transgeracional", [("transgeracional", "Herança entre gerações (figura)", "epigenetica")]),
 (51, "conteudo", "Alvos terapêuticos", [("terapia", "Marcas epigenéticas como alvo", ["hdaci", "hdaci-drogas"])]),
 (52, "conteudo", "Tratamentos epigenéticos", [("drogas", "Tabela de drogas", "hdaci-drogas")]),
 (53, "capa", "Bibliografia", []),
]
JUSTIFICATIVAS = {"capa": "capa, divisória ou bibliografia, sem conteúdo"}

CAPITULO = [("Alberts 5ª ed., cap. 4 (cromatina, pdf pp. 245–270) e cap. 7 (metilação do DNA, pp. 500–508)", [
   ("ab-remodel", "Complexos remodeladores dependentes de ATP deslizam/removem nucleossomos", ["remodelador-atp", "tf-remodelador"]),
   ("ab-codigo", "Código das histonas e proteínas leitoras", ["codigo", "leitores"]),
   ("ab-hetero", "Heterocromatina e HP1", "hp1"),
   ("ab-metil", "Ilhas CG; metiltransferase de manutenção copia o padrão", ["ilhas-cpg", "manutencao"])])]

EXERCICIOS = [
 ("Transcrição da turma (versão anterior)", [
   ("tr-objetivos", "Objetivos: 3 maneiras dos remodeladores, HAT/HDAC, código de histonas, ativador → remodelador → HAT, heterocromatina e metilação", ["remodelador-atp", "codigo", "ho-swi5", "hp1"]),
   ("tr-ips", "iPS: 4 genes induzem pluripotência; c-Myc e Klf4 oncogênicos", ["ips", "ips-oncogene"])]),
 ("Monitoria P3, aula 5", [
   ("mon-octamero", "Tetrâmero H3–H4 + dois dímeros H2A–H2B", "octamero"),
   ("mon-carga", "Acetilação neutraliza a carga positiva", "acetil-carga"),
   ("mon-hp1", "Metilação de H3 → HP1 se autoagrega", "hp1")]),
 ("Provas UC03 (índice biomol-07)", [
   ("p2025", "2025 P3 1.5: mecanismos epigenéticos (cromatina) na troca de fase", ["epigenetica", "hat", "cpg-reprime"]),
   ("p2024", "2024 P3 2.10: cromatina esperada para expressar repórter", ["acetil-carga", "sh-1791627547178"])]),
]
