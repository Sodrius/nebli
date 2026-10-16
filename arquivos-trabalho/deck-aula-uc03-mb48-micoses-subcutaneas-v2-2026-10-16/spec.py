# Especificação curada — 48 Micoses subcutâneas (UC03 P3, Microbiologia; Prof. Benedito Corrêa; 42 lâminas). Refação v2 (F-20261016-CLAUDE-08/09).
# AnKing primeiro (esporotricose; Actinomyces/Nocardia para o micetoma bacteriano); cromomicose, eumicetoma e lobomicose não têm card de acervo:
# só os autorais antigos essenciais (corrigidos por Davi ou centrais) e dois organizadores novos que substituem os antigos de vários cards.
# Escopo pelo Trabulsi cap. 68 (esporotricose, cromoblastomicose, feo-hifomicose, eumicetoma, lobomicose): feo-hifomicose com cobertura mínima.
# Imagens que Davi pediu entram no verso das notas mantidas (EXTRA_VIVO, aplicado por nebli.extra_vivo). Ordem = slides.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ("Três das quatro micoses da aula (cromomicose, eumicetoma, lobomicose) e a feo-hifomicose não têm nenhuma nota no AnKing nem nos acervos "
                   "externos (palavra-chave e significado em busca/); Davi autorizou até 30% na Micro P3 (F-20261016-CLAUDE-09).")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-mb48-20261016a"
SHORT = "mb48"
LESSON = "2026-uc03-microbiologia-48-micoses-subcutaneas"
DECK = "NEBLI::UC03::P3::Microbiologia::Micoses subcutâneas"
CRITERIOS = "EXECUCAO-DECK-AULA (passos 0–7) + MEMORY §2–§8 + ANTI-EXEMPLARES + F-20261016-CLAUDE-08/09, 16/10/2026"
MEDIA = {f"mb48-{n}.png": f"img/mb48-{n}.png" for n in ("esporotricose-linfocutanea",)}
BUSCA = ("Três caminhos (16/10): seções (busca/secoes: Sporothrix ×4; Chromoblastomycosis, Mycetoma, Subcutaneous sem seção); palavra-chave "
         "(busca/anking.txt: cromo/lobo/feo = 0 notas); significado em todos os acervos e decks NEBLI vivos (busca/semantica.jsonl). ")
A = lambda nid, cod, bloco, alvo, slide, motivo, **kw: acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)
IMG = lambda n, w=360: f'<img src="mb48-{n}.png" width="{w}">'
# Imagens no verso de notas mantidas (pedidas por Davi nos comentários): nid -> imagem
EXTRA_VIVO = {1791628674574: "sporothrix-levedura", 1791628675323: "cromomicose-membro", 1791628675571: "corpos-escleroticos",
              1791628675824: "micetoma-graos", 1791628676373: "lacazia-cadeias", 1791628676621: "lobomicose-queloide"}

EXCLUIDOS = []
FORA_DO_RECORTE = [
 "Histórico da esporotricose (Schenck, Smith, Hektoen & Perkins, Beurmann, África do Sul, Howard) e números das epidemias: Tab (§4).",
 "Tipos de conidiação da cromomicose (acrógena, acropleurógena, fialófora) e cultivo das espécies: identificação, aula 55.",
 "Actinomicose e nocardiose além do oxigênio, dos grânulos e do micetoma cervicofacial: bacteriologia (P2).",
]
A_, B_, C_, D_, E_ = "A-subcutaneas", "B-esporotricose", "C-cromomicose", "D-micetoma", "E-lobomicose"

CARDS = [
 # A. Micoses subcutâneas (lâminas 2–4)
 sh(1791628672372, "verde", A_, "Implantação traumática", 2, "V-pilar: lâmina 2; apostila e Trabulsi; autoral corrigido por Davi em 15/10"),
 au("au-subcutaneas", ORG("Main <b>subcutaneous mycoses</b> (agent):<br>1. {{c1::Sporotrichosis}} (Sporothrix brasiliensis)<br>2. {{c1::Chromoblastomycosis}} (Fonsecaea pedrosoi)<br>"
                          "3. {{c1::Eumycetoma}} (Madurella grisea)<br>4. {{c1::Lobomycosis}} (Lacazia loboi)<br>5. {{c1::Phaeohyphomycosis}} (dark molds)"),
    "V-pilar", A_, "Principais micoses subcutâneas", 3, "lâmina 3; transcrição; Trabulsi cap. 68 (inclui a feo-hifomicose, cobertura mínima)",
    extra="- Phaeohyphomycosis shows dark septate hyphae in tissue, unlike the sclerotic bodies of chromoblastomycosis or the grains of mycetoma<br>"
          "- All come from soil and plants and enter through a wound",
    espelhos=(1500054719314, 1500052358184, 1510012087056)),
 # B. Esporotricose (5–25)
 A(1500054558583, "A-aula", B_, "Esporotricose = Sporothrix", 5, "lâmina 5"),
 sh(1791628672748, "azul", B_, "S. brasiliensis, a espécie mais frequente", 7, "A-aula: lâminas 7 e 11; transcrição (só por métodos moleculares); autoral antigo mantido"),
 A(1500054719314, "V-hy", B_, "Espinhos, plantas: inoculação", 8, "lâminas 8 e 10"),
 sh(1791628672623, "azul", B_, "Gatos na epidemia do Rio", 9, "A-aula: lâmina 6 e 9; transcrição (via indireta por arranhadura de gatos); autoral antigo mantido"),
 A(1500054777136, "V-hy", B_, "Sporothrix é dimórfico", 11, "lâmina 11 (25 °C bolor, 37 °C levedura)"),
 A(1500151811249, "V-hy", B_, "Levedura no tecido, bolor na planta", 11, "lâmina 11; nota corrigida por Davi (agora com a imagem da fase Y)"),
 au("au-formas-esporotricose", ORG("Clinical forms of <b>sporotrichosis</b>:<br>1. {{c1::Lymphocutaneous}}, the most common<br>2. {{c1::Fixed cutaneous}}<br>"
                                  "3. {{c1::Extracutaneous}}<br>4. {{c1::Pulmonary}}, after inhalation<br>5. {{c1::Disseminated}}, in the immunocompromised"),
    "A-aula", B_, "Formas clínicas da esporotricose", 11, "lâmina 11; transcrição (linfocutânea 80–90%; disseminada em imunodeprimidos); apostila; Trabulsi",
    extra=f"- Lymphocutaneous: ulcer at the wound and nodules climbing the lymphatics; fixed: stays at the inoculation site<br>{IMG('esporotricose-linfocutanea')}",
    espelhos=(1500055367426, 1500056181436, 1500055544157)),
 A(1500055544157, "V-hy", B_, "Úlcera no local e nódulos nos linfáticos", 12, "lâminas 12–18"),
 A(1500055367426, "V-hy", B_, "Disseminação ascendente pelos linfáticos", 15, "lâminas 15–18 (forma linfocutânea)"),
 A(1500056181436, "V-hy", B_, "Linfangite ascendente e leveduras em charuto", 15, "lâminas 15–22"),
 A(1503960067023, "R-detalhe", B_, "Caso: jardineiro com nódulos no antebraço", 16, "lâminas 15–18"),
 A(1500055361936, "V-hy", B_, "Levedura em charuto", 22, "lâmina 22 (exame direto)"),
 A(1500055687581, "A-aula", B_, "Cultura confirma", 23, "lâminas 23–24"),
 A(1500054938635, "R-detalhe", B_, "Hifas a 25 °C", 24, "lâmina 24 (cultivo a 25 °C)"),
 A(1500055049050, "R-detalhe", B_, "Hifas ramificadas como roseira", 24, "lâmina 24"),
 A(1500055726473, "V-hy", B_, "Biópsia: granuloma com leveduras em charuto", 25, "lâmina 25 (fase Y no tecido); transcrição (Grocott)"),
 A(1500151965518, "V-hy", B_, "Lesões granulomatosas", 25, "lâmina 25"),
 A(1500055896708, "V-hy", B_, "Itraconazol na esporotricose", 25, "apostila e monitoria (tratamento); Trabulsi"),
 A(1500056127804, "V-hy", B_, "Iodeto de potássio na esporotricose", 25, "apostila (iodeto de potássio em doses crescentes); Trabulsi"),
 A(1509746332128, "V-hy", B_, "Itraconazol nas formas locais dos dimórficos", 25, "monitoria (itraconazol)"),
 # C. Cromomicose (26–32)
 sh(1791628675198, "azul", C_, "Fungos demáceos, Fonsecaea pedrosoi", 26, "A-aula: lâmina 26; apostila; Trabulsi; autoral antigo mantido"),
 sh(1791628675323, "azul", C_, "Membros inferiores (trauma)", 27, "A-aula: lâmina 27; corrigido por Davi em 14/10; imagem da lâmina 27 no verso"),
 sh(1791628675571, "verde", C_, "Corpos escleróticos", 29, "V-pilar: lâminas 29 e 32 (achado que define o diagnóstico); imagem no verso"),
 # D. Micetoma (33–37)
 sh(1791628675824, "verde", D_, "Tríade: tumor, fístula, grãos", 35, "V-pilar: lâmina 35; Trabulsi; imagem dos grãos no verso"),
 A(1500498780974, "V-hy", D_, "Actinomyces: anaeróbio", 34, "lâmina 34 (actinomicose: bactérias anaeróbias)"),
 A(1506203795560, "V-hy", D_, "Nocardia: aeróbio", 34, "lâmina 34 (nocardiose: bactérias aeróbias)"),
 A(1510012087056, "V-hy", D_, "Grânulos de enxofre: Actinomyces", 34, "lâminas 34–36 (grãos do micetoma actinomicótico)"),
 A(1510011869046, "V-hy", D_, "Micetoma cervicofacial por Actinomyces", 34, "lâmina 34"),
 sh(1791628672497, "azul", D_, "Madurella grisea: grãos negros", 36, "A-aula: lâminas 3 e 36; transcrição; autoral antigo mantido"),
 # E. Doença de Jorge Lobo (38–42)
 sh(1791628676373, "azul", E_, "Lacazia loboi", 38, "A-aula: lâmina 38; imagem das cadeias da lâmina 42 no verso"),
 sh(1791628676621, "azul", E_, "Lesões queloidianas", 40, "A-aula: lâmina 40; imagem no verso (Davi pediu)"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1500054558583": "- Sporothrix brasiliensis is the main agent in Brazil",
 "ak1500054777136": "- Mold at 25 °C in soil and plants, yeast at 37 °C in tissue",
 "ak1500055367426": "- The fungus travels in lymph from the inoculation site toward the regional nodes",
 "ak1500056181436": "- The ulcer at the wound and a chain of nodules up the arm are the classic picture",
 "ak1503960067023": "- Gardeners and farmers handle soil and plants that carry the mold",
 "ak1500055726473": "- Few yeasts are seen; silver (Grocott) stain shows them best",
 "ak1500151965518": "- The host contains the yeasts in granulomas of macrophages and giant cells",
 "ak1500055049050": "- The conidia cluster like a daisy at the tips of the conidiophores",
 "ak1509746332128": "- Azoles block ergosterol synthesis and are well absorbed orally",
 "ak1510012087056": "- The grains are clumps of filamentous bacteria with Splendore-Hoeppli material",
 "ak1510011869046": "- Bacterial (actinomycotic) mycetoma; the fungal one is eumycetoma",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"au-subcutaneas": "ganho: organiza as cinco micoses subcutâneas com o agente; o card AnKing só nomeia a infecção pelo Sporothrix"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "mb48-esporotricose-linfocutanea.png": "lâmina 16: nódulos em cadeia subindo o braço, sem legenda",
 "mb48-sporothrix-levedura.png": "lâmina 25: leveduras alongadas no tecido (fase Y), sem legenda — verso da nota levedura/bolor",
 "mb48-cromomicose-membro.png": "lâmina 27: lesões verrucosas no pé e na perna, sem o título — verso da nota de membros inferiores",
 "mb48-corpos-escleroticos.png": "lâmina 29: corpo esclerótico acastanhado septado, sem legenda — verso da nota dos corpos escleróticos",
 "mb48-micetoma-graos.png": "lâmina 36: grãos no histopatológico, sem o título — verso da nota da tríade",
 "mb48-lacazia-cadeias.png": "lâmina 42: células refringentes de parede grossa em cadeia (exame direto e Grocott), sem título — verso da nota da Lacazia",
 "mb48-lobomicose-queloide.png": "lâmina 40: lesões queloidianas na orelha, sem a legenda — verso da nota das lesões queloidianas",
}
REVISAO = {"despejo": "Despejo lido inteiro (13 notas novas) e as 21 mantidas relidas; imagens no verso de 6 notas mantidas conferidas (readback). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Entender a micose subcutânea (implantação traumática de fungos do solo e plantas) e reconhecer esporotricose (agente, transmissão, dimorfismo, formas, diagnóstico), "
             "cromomicose (demáceos, corpos escleróticos), micetoma (tríade, grãos; fúngico × bacteriano) e doença de Jorge Lobo; feo-hifomicose com cobertura mínima.",
 "centrais": [
   ("implantação traumática", "sh-1791628672372", "au-subcutaneas"),
   ("corpos escleróticos", "sh-1791628675571"),
   ("tríade do micetoma", "sh-1791628675824"),
 ],
 "exemplos": ["histórico da esporotricose", "epidemia na África do Sul", "fotos de cães e gatos", "tipos de conidiação da cromomicose"],
 "outras_aulas": ["43 Biologia dos fungos (dimorfismo)", "44 Micoses cutâneas (classificação)", "50 Micoses sistêmicas", "55 Prática de micologia", "P2 bacteriologia (Actinomyces, Nocardia)"],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
