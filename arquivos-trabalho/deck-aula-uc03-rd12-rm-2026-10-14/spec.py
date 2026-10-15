# Especificação curada — Princípios da ressonância magnética (UC03 P1, Radiologia; Dr. César Alves (I, 40 lâminas) + Profa. Claudia Leite (II, 59); 99 lâminas).
# Aula 02 (Diagnóstico radiológico) já cobre RM sem radiação ionizante, gadolínio, T1/T2 do líquido, hiper/hipointenso e risco do ferromagnético: entram por sh().
RUN_ID = "uc03-rd12-20261014a"
SHORT = "rd12"
LESSON = "2026-uc03-radiologia-12-ressonancia-magnetica"
DECK = "NEBLI::UC03::P1::Radiologia::Ressonância magnética"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {f"rd12-cranio-{n}.png": f"img/rd12-cranio-{n}.png" for n in ("t1", "t2")}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (MRI, gadolinium, nephrogenic systemic fibrosis, T1/T2-weighted, FLAIR, pacemaker MRI, diffusion-weighted, Larmor, proton density, "
         "ferromagnetic, functional MRI, MR angiography, tractography; busca/anking.txt) e cópias NEBLI vivas da aula 02, 14/10: ")
EXCLUIDOS = [(1585502300974, "lobo temporal em T1: caso de encefalite, fora da aula")]
FORA_DO_RECORTE = ["Animação da detecção do sinal (lâminas 59–65): ilustra o FID; um card.", "Acidentes com objetos (73–77): ilustram o ferromagnético (sh da aula 02).",
                   "Abscesso e tumor pós-contraste (85, 87): exemplos de realce; card de barreira hematoencefálica.", "Perfusão (rCBV, MTT) em detalhe: só Tab."]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok="", **kw):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok, **kw)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
G = lambda *k: {i: V for i in k}
NAO = "o AnKing não tem física, sequências nem segurança da RM como card."
EP = [1481771894987, 1585502300974, 1791810581147]
A_, B_, C_, D_, E_ = "A-hidrogenio-e-sinal", "B-relaxamento-e-ponderacao", "C-contraste", "D-equipamento-e-seguranca", "E-sequencias-e-tecnicas"
SLIDE_OK = "imagens de RM de crânio normal da própria aula, sem rótulo; o AnKing não tem par T1/T2 de crânio normal"

CARDS = [
 # A — hidrogênio, spin, os três passos (3–16; 44–56)
 au("a-hidrogenio", "<b>MRI</b> builds images from the nuclei of {{c1::hydrogen}}, abundant in the water and fat of the body",
    G(1), A_, "Por que o hidrogênio", "3; 44; provas 2023 P2 1.2 e 2024 P3 2.1", "prova", NAO, EP, "Verde: lâminas 3 e 44; provas pedem o mecanismo.",
    extra="- Its single (odd) proton leaves a net magnetic moment<br>- Water content differs between normal and diseased tissue, which creates contrast"),
 au("a-momento", "A spinning <b>proton</b> generates its own small magnetic field, called its {{c1::magnetic moment}}",
    {1: R}, A_, "Spin e momento magnético", "4; 6", "lateral", NAO, EP, "Rosa: lâminas 4–6; física de apoio (revisão 15/10).",
    extra="- So each hydrogen nucleus behaves like a tiny magnet"),
 au("a-passos", ORG("Steps of the <b>MRI signal</b>:<br>1. {{c1::alignment}} of spins in B0<br>2. {{c2::excitation}} by an RF pulse<br>3. {{c3::relaxation}}, when the signal is read"),
    G(1, 2, 3), A_, "Três passos do sinal", "7; 46; provas 2023 e 2024", "prova", NAO, EP, "Verde: lâmina 46; provas 2023 P2 1.2 e 2024 P3 2.1.",
    extra="- A receiver coil captures the energy released and the computer turns it into an image"),
 au("a-paralelo", "Because slightly more <b>spins</b> align parallel than antiparallel to B0, a small {{c1::net magnetization}} (M0) forms along the field",
    {1: Z}, A_, "Paralelo × antiparalelo", "9; 49", "central", NAO, EP, "Azul: lâminas 9 e 49.",
    extra="- Parallel alignment needs less energy<br>- The Earth's field is far too weak to align them"),
 au("a-transversal", "The <b>RF pulse</b> tips the net magnetization into the {{c1::transverse}} plane, because along B0 it cannot be measured",
    G(1), A_, "Por que tirar do eixo longitudinal", "10; 16; 55", "central", NAO, EP, "Verde: lâminas 10, 16 e 55; transcrição (água no oceano).",
    extra="- A 90° pulse moves Mz into Mxy"),
 au("a-precessao", "Besides spinning, each <b>proton</b> wobbles around B0 like a spinning top, a motion called {{c1::precession}}",
    G(1), A_, "Precessão", "12; 13; 50", "central", NAO, EP, "Verde: lâminas 12–13 e 50."),
 au("a-larmor", "<b>Protons</b> absorb energy from an RF pulse only at their precession frequency, given by the {{c1::Larmor}} equation (ω0 = γ·B0)",
    G(1), A_, "Ressonância e Larmor", "13; 14", "central", NAO, EP, "Verde: lâminas 13–14; transcrição.",
    extra="- Matching that frequency is the resonance effect<br>- The frequency rises with field strength"),
 au("a-fase", "During the <b>RF pulse</b>, the spins absorb energy and start precessing {{c1::in phase}}",
    {1: Z}, A_, "Spins em fase", "15; 56", "central", NAO, EP, "Azul: lâminas 15 e 56."),
 au("a-campo", "A stronger <b>MRI magnetic field</b> improves the {{c1::signal-to-noise ratio}} and spatial resolution, at the cost of more tissue heating",
    {1: Z}, A_, "Alto campo", "47; 48", "central", NAO, EP, "Azul: lâminas 47–48 (0,2–3 T).",
    extra="- Clinical magnets range from about 0.2 to 3 tesla"),
 sh(1791810579895, "verde", A_, "RM sem radiação ionizante", "53", "Verde: lâmina 53; viva na aula 02."),
 au("a-sar", "<b>RF energy</b> can heat tissue and burn the patient, so it is limited by the {{c1::specific absorption rate}} (SAR)",
    {1: Z}, A_, "Aquecimento e SAR", "54", "central", NAO, EP, "Azul: lâmina 54.",
    extra="- The risk grows with field strength"),
 # B — relaxamento e ponderação (18–31; 57–72)
 au("b-t1-t2", ORG("After the <b>RF pulse</b> is switched off:<br>- T1 relaxation: recovery of {{c1::longitudinal}} magnetization (energy lost to the surroundings)<br>- T2 relaxation: loss of {{c1::transverse}} magnetization (spins dephase)"),
    G(1), B_, "T1 e T2", "18; 58", "central", NAO, EP, "Verde: lâminas 18 e 58; transcrição.",
    extra="- T2 decay is much faster than T1 recovery<br>- Each tissue has its own T1 and T2, which creates contrast"),
 au("b-fid", "The <b>signal</b> picked up as transverse magnetization fades after the pulse is the {{c1::free induction decay}} (FID)",
    {1: R}, B_, "FID", "66; 59", "lateral", NAO, EP, "Rosa: lâminas 59–66."),
 au("b-gordura-t1", "On <b>T1-weighted</b> MRI, {{c1::fat}} appears bright, because it recovers longitudinal magnetization quickly (short T1)",
    G(1), B_, "Gordura brilha em T1", "26; 27; prova 2024 P3 2.2", "prova", NAO, EP, "Verde: lâmina 26 e transcrição (“para lembrar”); prova 2024.",
    extra="- Water has long T1 and long T2: dark on T1, bright on T2"),
 sh(1791810582322, "verde", B_, "Líquido escuro em T1", "26", "Verde: lâmina 26; viva na aula 02."),
 sh(1791810582199, "verde", B_, "Líquido claro em T2", "26", "Verde: lâmina 26; viva na aula 02."),
 sh(1791810582570, "verde", B_, "Hiperintenso", "32", "Verde: vocabulário do laudo; viva na aula 02."),
 sh(1791810582696, "verde", B_, "Hipointenso", "32", "Verde: vocabulário do laudo; viva na aula 02."),
 au("b-dp", "<b>Proton density</b> weighting minimizes T1 and T2 effects, so contrast reflects how many {{c1::hydrogen nuclei}} each tissue has",
    {1: Z}, B_, "Densidade de prótons", "30; 31; 32", "central", NAO, EP, "Azul: lâminas 30–32; transcrição."),
 au("b-cortical", "<b>Cortical bone</b> appears dark on MRI because it has few {{c1::mobile hydrogen}} nuclei",
    {1: Z}, B_, "Osso cortical sem sinal", "32; prova 2016 P1 3.6", "prova", NAO, EP, "Azul: gabarito da prova 2016 P1 3.6."),
 au("b-eco", "In the <b>spin-echo</b> sequence, a {{c1::180°}} pulse after the 90° pulse rephases the spins and produces the echo that is measured",
    {1: Z}, B_, "Spin-eco", "68; 71", "central", NAO, EP, "Azul: lâminas 68–71.",
    extra="- The runners analogy: turning around at TE/2 brings them back together"),
 au("b-tr-te", "In a <b>pulse sequence</b>, {{c1::TR::TR/TE}} is the interval between RF pulses and {{c1::TE::TR/TE}} the time from pulse to echo",
    G(1), B_, "TR e TE", "71", "central", NAO, EP, "Verde: lâmina 71."),
 au("b-ponderacao", "With short TR and short TE, the <b>MRI</b> image is {{c1::T1::T1/T2}}-weighted",
    {1: Z}, B_, "Como se pondera", "71; 28; 29", "central", NAO, EP, "Azul: lâminas 28–29 e 71; transcrição (pulsos curtos × longos).",
    extra="- Long TR and long TE give T2 weighting; long TR with short TE gives proton density"),
 au("img-t1", '<img src="rd12-cranio-t1.png"><br>What <b>MRI</b> weighting is shown in the image above? {{c1::T1}}',
    G(1), B_, "Reconhecer T1", "83; 82; prova 2024 P3 2.2", "prova", NAO, EP, "Verde: prova 2024 pede diferenciar T1 de T2 pela imagem.",
    extra="- Dark CSF in the ventricles; white matter brighter than gray matter", slide_sem_alternativa=SLIDE_OK),
 au("img-t2", '<img src="rd12-cranio-t2.png"><br>What <b>MRI</b> weighting is shown in the image above? {{c1::T2}}',
    G(1), B_, "Reconhecer T2", "83; 82; prova 2024 P3 2.2", "prova", NAO, EP, "Verde: prova 2024.",
    extra="- Bright CSF in the ventricles and sulci; white matter darker than gray matter", slide_sem_alternativa=SLIDE_OK),
 # C — contraste (33–34; 86–91)
 sh(1791810581147, "verde", C_, "Gadolínio", "33; 86", "Verde: lâminas 33 e 86; viva na aula 02."),
 sh(1791810581523, "verde", C_, "Gadolínio aumenta sinal em T1", "34", "Verde: lâmina 34; viva na aula 02."),
 au("c-quelato", "Free <b>gadolinium</b> is highly toxic, so it is always given bound to a {{c1::chelator}} such as DTPA",
    G(1), C_, "Quelação", "33; 88", "central", NAO, EP, "Verde: lâminas 33 e 88; transcrição.",
    extra="- Gadolinium is a paramagnetic lanthanide that shortens T1"),
 au("c-bhe", "In the brain, <b>gadolinium</b> enhances a lesion only where the {{c1::blood-brain barrier}} is broken",
    G(1), C_, "Realce e barreira hematoencefálica", "87; 85", "central", NAO, EP, "Verde: lâminas 85 e 87; transcrição.",
    extra="- Tumors and abscesses enhance on post-contrast T1"),
 au("c-fns", "In patients with severe kidney failure, <b>gadolinium</b> can cause {{c1::nephrogenic systemic fibrosis}}",
    G(1), C_, "Fibrose nefrogênica sistêmica", "88; 89; prova 2016 P3 2.7", "prova", NAO, EP, "Verde: lâminas 88–91; prova 2016.",
    extra="- Thickened, hardened skin; restricted use in moderate to severe renal failure since 2007"),
 # D — equipamento e segurança (35–38; 73–80)
 au("d-helio", "The superconducting <b>MRI magnet</b> is cooled with liquid {{c1::helium}} to about 4 K, where its electrical resistance drops to zero",
    {1: R}, D_, "Magneto supercondutor", "36; 35", "lateral", NAO, EP, "Rosa: lâminas 35–36; engenharia do aparelho (revisão 15/10).",
    extra="- Niobium–titanium alloy; strong fields with low operating cost"),
 au("d-bobinas", ORG("<b>MRI coils</b>:<br>- RF coils: send pulses, receive signal<br>- {{c1::shim}} coils: make the field homogeneous<br>- {{c2::gradient}} coils: localize the signal"),
    {1: R, 2: V}, D_, "Bobinas", "37; 38", "central", NAO, EP, "Verde/rosa: lâminas 37–38.",
    extra="- Gradient switching makes the loud noise of MRI"),
 sh(1791810580396, "verde", D_, "Objetos ferromagnéticos atraídos", "74", "Verde: lâminas 73–77; viva na aula 02."),
 au("d-contraindicacoes", ORG("Classic contraindications to <b>MRI</b>:<br>- cerebral {{c1::aneurysm clip}}<br>- metallic {{c2::middle-ear}} prosthesis<br>- cardiac {{c3::pacemaker}}"),
    G(1, 2, 3), D_, "Contraindicações", "78; provas 2016 P1 5.2 e 2018 P1 2.1", "prova", NAO, EP, "Verde: lâmina 78; provas 2016 e 2018.",
    extra="- Ask actively about implants, prostheses and tattoos before the exam"),
 # E — sequências e técnicas (81–97)
 au("e-flair", "<b>FLAIR</b> is a T2-weighted sequence that suppresses the {{c1::CSF}} signal, so lesions next to the ventricles stand out",
    {1: Z}, E_, "FLAIR", "81; 83", "central", NAO, EP, "Azul: lâminas 81 e 83."),
 ak("ak-difusao", 1481771894987, {1: Z}, E_, "Difusão no infarto agudo", "94; 81", "Azul: lâmina 94 (infarto agudo na difusão).",
    extra_add="- Diffusion is one of the basic brain sequences"),
 au("e-tecnicas", ORG("Advanced <b>MRI</b> techniques:<br>- MR {{c1::angiography}}: blood vessels<br>- {{c2::perfusion}}: cerebral blood volume and transit time<br>- {{c3::tractography}}: white-matter tracts<br>- {{c4::functional}} MRI: brain areas activated by a task"),
    {1: Z, 2: Z, 3: Z, 4: Z}, E_, "Outras funcionalidades", "92; 93", "central", NAO, EP, "Azul: lâminas 92–97."),
]
SEM_IMAGEM = "princípio físico ou regra de exame, sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {
 "a-precessao": "- Its frequency depends on the element and the field strength",
 "a-fase": "- In-phase spins add up to a measurable transverse magnetization",
 "b-fid": "- It decays with T2* (T2 plus field inhomogeneity)",
 "b-dp": "- Uses long TR and short TE",
 "b-cortical": "- Fat-rich marrow inside the bone is bright on T1",
 "b-tr-te": "- TR = repetition time; TE = echo time<br>- Both are set by the operator to choose the weighting",
 "e-flair": "- Fluid-attenuated inversion recovery",
 "e-tecnicas": "- Perfusion shows blood volume (rCBV) and mean transit time (MTT)",
}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
IMAGENS_VISTAS = {"rd12-cranio-t1.png": "lâmina 83, T1 axial de crânio normal, sem rótulo; conferida 14/10", "rd12-cranio-t2.png": "lâmina 83, T2 axial de crânio normal, sem rótulo; conferida 14/10"}
REVISAO = {}
ESCOPO = {
 "objetivo": "Explicar como a RM forma imagem (hidrogênio, alinhamento, excitação por RF, relaxamento T1/T2), reconhecer T1 e T2, e saber o uso e os riscos do gadolínio e as contraindicações.",
 "centrais": [
   ("hidrogênio e sinal", "a-hidrogenio", "a-momento", "a-passos", "a-paralelo", "a-transversal", "a-precessao", "a-larmor", "a-fase", "a-campo", "sh-1791810579895", "a-sar"),
   ("relaxamento e ponderação", "b-t1-t2", "b-fid", "b-gordura-t1", "sh-1791810582322", "sh-1791810582199", "sh-1791810582570", "sh-1791810582696", "b-dp", "b-cortical",
    "b-eco", "b-tr-te", "b-ponderacao", "img-t1", "img-t2"),
   ("contraste", "sh-1791810581147", "sh-1791810581523", "c-quelato", "c-bhe", "c-fns"),
   ("equipamento e segurança", "d-helio", "d-bobinas", "sh-1791810580396", "d-contraindicacoes"),
   ("sequências e técnicas", "e-flair", "ak-difusao", "e-tecnicas"),
 ],
 "exemplos": ["arma puxada pelo magneto", "acidentes com objetos", "tatuagens", "abscesso e tumor pós-contraste"],
 "outras_aulas": [("RM no panorama dos métodos", "02 Diagnóstico radiológico"), ("contrastes", "aula de Contrastes (P3)")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
