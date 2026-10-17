# Especificação curada — Princípios físicos da ressonância magnética (UC03 P1, Radiologia; 99 lâminas, partes I e II).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing → cards da 02 e do GR3 por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv): a física da RM não existe nos acervos.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06 (só notas do baralho AnKing)
    "_FirstAid_Neuro_Ischemic_stroke_Treatment.txt",
]
AUTORAL_EXCECAO = ("Aula de física da RM: hidrogênio e spin, pulso de RF e ressonância, relaxamento T1/T2, ponderações, TE/TR, gadolínio, "
                   "fibrose nefrogênica e contraindicações não têm nenhum card em AnKing, MCAT, Ankisthesia ou NEBLI vivo "
                   "(busca/anking.txt: 0 notas para gadolínio e para T1/T2-weighted; busca/semantica.jsonl)")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-rd12-20261017a"
SHORT = "rd12n"
LESSON = "2026-uc03-radiologia-12-ressonancia-magnetica"
DECK = "NEBLI::UC03::P1::Radiologia::Ressonância magnética"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"rd12-{n}.png": f"img/rd12-{n}.png" for n in ("sequencias", "gadolinio")}
IMG = lambda n, w=440: f'<img src="rd12-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (FirstAid AVC isquêmico, tumores cerebrais; busca/secoes); palavra-chave em "
         "AnKing e Referências Externas (busca/anking.txt: ponderações, gadolínio, física, contraindicações, difusão); significado em todos "
         "os acervos e NEBLI vivo (busca/semantica.jsonl). ")
EXCLUIDOS = [
 (1481771888224, "seção AVC: TC sem contraste antes do tPA — card da aula 05"),
 (1481771899132, "seção AVC: tPA em 3–4,5 h — tratamento, aula de neurologia"),
 (1561067971846, "MCAT: princípio da RM — entra a cópia NEBLI da 02 (sh-1792141772957)"),
 (1488154325513, "RM é a melhor para osteomielite aguda — entra a cópia NEBLI do GR3 (sh-1791054020796)"),
 (1552988128371, "osteomielite precoce = RM: repete sh-1791054020796"),
 (1524015599855, "mielotomografia quando não dá para fazer RM: detalhe clínico estreito"),
]
FORA_DO_RECORTE = [
 "História (Rabi, Bloch, Purcell), equação de Larmor em números, T2*, chemical shift, bobinas de reforço: detalhe físico sem prova.",
 "Angio-RM, perfusão, tractografia e RM funcional (lâminas 92–97): só ilustradas.",
 "Sequências GRE, SWI e FIESTA: citadas na lâmina 83 sem explicação.",
]
A_, B_, C_, D_, E_ = ("A-sinal", "B-relaxamento-ponderacoes", "C-contraste", "D-seguranca", "E-aplicacoes")

CARDS = [
 # ---------- A. De onde vem o sinal (lâminas 3–16, 35–38, 46–56) ----------
 au("au-hidrogenio", "<b>MRI</b> signal comes mainly from {{c1::hydrogen}} nuclei, which behave like tiny magnets and fill the body's water and fat",
    "V-prova", A_, "O sinal vem do hidrogênio", 3, "lâminas 3–9, 24, 46–49; provas 2024 P3 2.1 e 2023 P2 1.2 (mecanismo de formação); bibliografia da aula",
    extra="- Step 1: in the strong field (0.2–3 T) slightly more protons align parallel than antiparallel, giving a net magnetization<br>"
          "- Superconducting magnet cooled by liquid helium; gradient coils localize the signal and cause the noise"),
 sh(1792141772957, "azul", A_, "Princípio da RM: campo, gradientes, rádio", 3, "lâmina 46 (três passos); card da 02"),
 au("au-pulso-rf", "A <b>radiofrequency pulse</b> at the protons' Larmor frequency tips the magnetization into the {{c1::transverse}} plane, in phase",
    "V-prova", A_, "Ressonância: o pulso de RF", 14, "lâminas 10–16 e 50–56; provas 2024 P3 2.1 e 2023 P2 1.2",
    extra="- The longitudinal magnetization cannot be measured inside the huge field, so it must be tipped<br>"
          "- Larmor frequency rises with field strength (ω = γB0)<br>- RF energy heats tissue: limited by the SAR, worse at high field"),
 # ---------- B. Relaxamento e ponderações (lâminas 18–32, 57–72, 81–83) ----------
 au("au-t1-t2", "After the <b>RF pulse</b>, longitudinal regrowth is {{c1::T1}} relaxation and transverse decay is {{c1::T2}} relaxation",
    "V-pilar", B_, "Relaxamento T1 e T2", 18, "lâminas 18–23 e 57–66; transcrição; provas 2024 P3 e 2023 P2 (relaxamento)",
    extra="- T2 decay is much faster than T1 recovery<br>- Each tissue has its own T1 and T2, and that difference is the image contrast"),
 au("au-pesos", "Fat is bright on T1-weighted MRI, while {{c1::water}} is bright on <b>T2-weighted</b> MRI",
    "V-prova", B_, "T1 × T2: gordura e água", 26, "lâminas 25–32 e 81–83; prova 2024 P3 2.2 (diferença entre T2 e T1); apostila ilustrativa (T1 anatomia, T2 água)",
    extra="- Fat: short T1 and short T2; water/CSF: long T1 and long T2<br>- FLAIR is T2 with the CSF signal suppressed; proton density minimizes T1/T2 effects<br>" + IMG("sequencias", 460)),
 au("au-te-tr", "A <b>short TR and short TE</b> give {{c1::T1}}-weighted images, while long TR and TE give T2",
    "A-aula", B_, "TE e TR", 71, "lâminas 68–72 (sequência de pulso: TE e TR); monitoria",
    extra="- TR: time between pulses; TE: time from pulse to echo (spin-echo uses 90° then 180°)"),
 sh(1792141774955, "verde", B_, "Termos de cada método (hipersinal, hipossinal)", 82, "lâmina 82; prova 2024 P3 2.3 (descrever hipersinal); card da 02"),
 # ---------- C. Contraste (lâminas 33–34, 85–91) ----------
 au("au-gadolinio", "<b>Gadolinium</b> shortens T1, so lesions that break the {{c1::blood-brain barrier}} enhance brightly on post-contrast T1",
    "V-prova", C_, "Gadolínio e realce", 87, "lâminas 33–34, 85–87 (abscesso e tumor pós-contraste); transcrição (quebra da barreira); monitoria",
    extra="- Free Gd³⁺ is very toxic, so it is given chelated (e.g., Gd-DTPA)<br>- Used with T1 images; it is paramagnetic, not iodinated<br>" + IMG("gadolinio", 420)),
 sh(1792141769157, "azul", C_, "Contraste de cada método (gadolínio na RM)", 86, "lâmina 86; card da 02"),
 au("au-fns", "In severe <b>renal failure</b>, gadolinium can trigger nephrogenic systemic {{c1::fibrosis}}",
    "V-prova", C_, "Fibrose nefrogênica sistêmica", 88, "lâminas 88–91; prova 2016 P3 2.7 (gadolínio no paciente dialítico)",
    extra="- Thick, hard skin and joint contractures<br>- Described in 2000; since 2007 gadolinium is restricted in moderate to severe renal failure"),
 # ---------- D. Segurança (lâminas 42–43, 74–80) ----------
 au("au-contraindicacoes", ORG("Classic contraindications to <b>MRI</b>:<br>1. Cardiac {{c1::pacemaker::p…}}<br>2. Aneurysm {{c1::clip::c…}}<br>3. Metallic ear (otologic) {{c1::prosthesis::p…}}"),
    "V-pilar", D_, "Contraindicações da RM", 78, "lâminas 74–80; provas 2018 P1 2.1 e 2016 P1 5.2 (clip de aneurisma)",
    extra="- The magnet pulls ferromagnetic objects (even a gun fired); ask actively about implants before the exam<br>- Tattoo inks can heat up"),
 ak("ak-implante-coclear", 1584310188149, "A-step", D_, "Implante coclear impede a RM", 78, "lâmina 78 (prótese metálica otológica)"),
 sh(1792141775531, "azul", A_, "RM e US não usam radiação ionizante", 53, "lâminas 52–53; card da 02"),
 sh(1792141773206, "azul", D_, "Forças e limites da RM", 81, "lâmina 81 (vantagens e limites); monitoria; card da 02"),
 # ---------- E. Aplicações (lâminas 81–94) ----------
 sh(1792141773608, "verde", E_, "Reconhecer a RM", 83, "provas 2017 P1 1.1, 2016 P1 2.5 e 3.6; card da 02"),
 ak("ak-rm-tumor", 1583729350529, "A-step", E_, "RM para tumores do SNC", 87, "lâmina 87 (tumor)"),
 ak("ak-dwi", 1481771894987, "A-aula", E_, "Difusão mostra AVC isquêmico em 3–30 min", 94, "lâmina 94 (difusão no infarto agudo); seção FirstAid AVC"),
 ak("ak-rm-avc", 1583592047108, "A-step", E_, "RM é mais sensível que TC para AVC isquêmico", 94, "lâmina 94; seção FirstAid AVC"),
 ak("ak-tc-avc-tempo", 1481771891686, "R-detalhe", E_, "TC só mostra a isquemia após 6–24 h", 94, "contraste com a difusão; seção FirstAid AVC"),
 ak("ak-cunha", 1583597283550, "R-detalhe", E_, "Oclusão proximal: isquemia em cunha", 94, "seção FirstAid AVC"),
 sh(1791054020796, "azul", E_, "RM é a melhor para osteomielite aguda", 94, "prova 2023 P2 1.3 (RM vê o que o RX não vê); card do GR3"),
 sh(1791054020921, "rosa", E_, "Osteomielite: medula com hipersinal em T2 com saturação de gordura", 94, "card do GR3"),
]

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "princípio físico sem estrutura a reconhecer; as figuras que ensinam (sequências do crânio e realce pelo gadolínio) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula, sem equivalente nos acervos (busca sem acerto para o conceito)"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "rd12-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {
 "ak-implante-coclear": "- Its magnet and electronics are pulled and damaged by the field",
 "ak-rm-tumor": "- Superior soft-tissue contrast, plus gadolinium enhancement",
 "ak-dwi": "- Restricted water diffusion in swollen ischemic cells shows up within minutes",
 "ak-rm-avc": "- Diffusion-weighted MRI detects infarcts that CT still misses",
 "ak-tc-avc-tempo": "- That is why CT first excludes hemorrhage, while MRI confirms early ischemia",
 "ak-cunha": "- The wedge follows the vascular territory of the occluded artery",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
IMAGENS_VISTAS = {
 "rd12-sequencias.png": "Lâmina 83: RM de crânio em T1, T2, FLAIR, GRE, T1 pós-contraste, T2 coronal, FIESTA sagital e difusão, com legendas; verso de au-pesos.",
 "rd12-gadolinio.png": "Lâmina 87: RM axial com tumor de fossa posterior antes e depois do gadolínio (realce intenso); verso de au-gadolinio.",
}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (14 notas novas, 16 cards; frentes, clozes, versos, imagens e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Entender como a RM forma a imagem (hidrogênio no campo forte, pulso de RF na frequência de Larmor, relaxamento T1 e T2), "
             "ler as ponderações T1 e T2, o papel de TE/TR, o gadolínio e seus riscos, as contraindicações e as aplicações (difusão no AVC).",
 "centrais": [
   ("formação do sinal", "au-hidrogenio", "au-pulso-rf", "au-t1-t2"),
   ("ponderações", "au-pesos", "au-te-tr"),
   ("contraste", "au-gadolinio", "au-fns"),
   ("segurança", "au-contraindicacoes"),
 ],
 "exemplos": ["tumor e abscesso com realce", "AVC isquêmico na difusão", "osteomielite", "clip de aneurisma"],
 "outras_aulas": [("forças e limites, termos, contrastes", "02 (sh)"), ("TC no AVC", "05"), ("osteomielite", "GR3 (sh)"),
                  ("reações aos contrastes", "56 Contrastes radiológicos")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
