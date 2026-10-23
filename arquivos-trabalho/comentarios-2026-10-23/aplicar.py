#!/usr/bin/env python3
"""Comentários pendentes de 23/10/2026 (F-20261023-CLAUDE-01): imagens reais (Langman, MSA, Kenhub na UC07), reescritas, negrito de
contexto nos autorais da BC10 e da 59, organizador de indutores/inibidores do CYP450 (UC19-01), artérias do intestino primitivo
associadas à BC10, altura das intumescências na UC07 e o card vermelho do óxido nítrico. Uma única janela de escrita."""
import base64, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from nebli.decks import Anki, escrita, em_tela
from nebli.kenhub.renomear import renomear

A = Anki()
MARK = "CORRIGIDO, 23, 10, 26."
img = lambda f, w=460: f'<img src="{f}" width="{w}">'
L = lambda n: img(f"langman-{n}.png")
MIDIA = {p.name: p for p in (HERE / "img").glob("langman-*.png")}

NEW = {
 # UC08 fisiologia 09: imagem melhor dos constritores
 1791575026219: {"Extra": "- The wave runs from the superior to the middle and inferior constrictors, which overlap like stacked cups<br>- The cricopharyngeal part then relaxes and lets the bolus into the esophagus<br>" + img("MSA-Muscles_of_Pharynx_342.jpg")},
 # Imuno 45
 1791625435907: {"Text": "<b>Tregs</b> cannot make their own {{c1::<b>IL-2</b>}} and survive on the IL-2 secreted by activated conventional T cells",
                 "Extra": "- FOXP3 represses the IL-2 gene, yet Tregs carry high CD25, the IL-2 receptor α chain<br>- By consuming IL-2 they also starve nearby effector T cells, one of their ways to suppress"},
 # Biomol 46
 1791627549403: {"Text": "Yeast <b>Gal4</b> activating a TATA + UAS reporter even in human cells shows the {{c1::<b>universality</b>}} principle",
                 "Extra": "- Activators and the basal machinery they recruit are conserved in all eukaryotes<br>- So what is learned about gene activation in yeast applies to human cells"},
 1791627550702: {"Text": "Insulin, via AKT, phosphorylates <b>FOXO1</b> and keeps it out of the {{c1::<b>nucleus</b>}}, so {{c2::<b>gluconeogenic</b>}} genes stay off",
                 "Extra": "- Moving a transcription factor out of the nucleus switches genes off fast, without degrading it<br>- In fasting, low insulin lets FOXO1 return to the nucleus and turn gluconeogenesis on"},
 # Biomol 52
 1791631346842: {"Text": "<b>Methylated cytosines</b> silence genes by recruiting {{c1::<b>histone deacetylases</b>}} and nucleosome {{c1::<b>remodelers</b>}}",
                 "Extra": "- <b>Histone deacetylases</b> remove acetyl groups, so histones grip the DNA tightly<br>- <b>Nucleosome remodelers</b> slide nucleosomes over the promoter and hide it<br>- Methylated CpG islands also attract histone methyltransferases"},
 # GR4 / micoses sistêmicas
 1792065187180: {"Text": '<div data-nebli-organizacao="true">Clinical forms of <b>paracoccidioidomycosis</b>:<br>- chronic (adult): a latent focus in the {{c1::<b>lungs</b>}} reactivates and reaches the mucosa<br>- acute (juvenile): spreads to the {{c2::<b>reticuloendothelial</b>}} system, nodes, liver and spleen</div>',
                 "Extra": "- The adult form is about 90% of cases, mostly in men: estrogen blocks the mold-to-yeast switch<br>- The juvenile form (3–5%) follows a weak Th1 response and is the most severe"},
 # UC07
 1792588686967: {"Text": '<div data-nebli-organizacao="true"><b>Via eferente visceral</b> (autônoma):<br>- neurônio pré-ganglionar: corpo no {{c1::SNC}}<br>- sinapse no {{c2::gânglio autônomo}}<br>- neurônio pós-ganglionar: do gânglio ao {{c3::órgão efetor}}</div>',
                 "Extra": "- Na via somática basta um neurônio do SNC ao músculo; na visceral são dois, com sinapse no gânglio<br>" + img("kh-autonomic-ganglion.jpg")},
 1792588686980: {"Text": '<div data-nebli-organizacao="true">A <b>cavidade do tubo neural</b> origina, no tronco e na medula:<br>- mesencéfalo: {{c1::aqueduto cerebral::a…}}<br>- ponte e bulbo: {{c1::quarto ventrículo::q…}}<br>- medula espinal: {{c1::canal central::c…}}</div>',
                 "Extra": "- No prosencéfalo a mesma cavidade forma os ventrículos laterais e o terceiro ventrículo<br>" + img("kh-cap-3490.jpg")},
 1792696993158: {"Extra": "- Fica entre a medula e o diencéfalo e à frente do cerebelo, que cobre sua face posterior<br>" + img("kh-brainstem.jpg")},
 1792697127074: {"Extra": "- É ali, no forame magno, que o bulbo continua como medula espinal<br>" + img("khref-abfdce9d7a55f0e8fa23-back.jpg")},
 1792697128629: {"Text": '<div data-nebli-organizacao="true"><b>Plexos</b> por região da medula:<br>- cervical: plexos {{c1::cervical}} (pescoço) e {{c2::braquial}} (membro superior)<br>- lombossacral: plexo {{c3::lombossacral}} (membro inferior)<br>- torácica: {{c4::nenhum}}</div>',
                 "Extra": "- Os plexos se formam onde muitas raízes vão ao mesmo território; no tórax cada nervo intercostal segue sozinho<br>" + img("kh-brachial-plexus.jpg")},
 # UC19
 1792624465974: {"Text": '<div data-nebli-organizacao="true">Hepatic clearance depends on the <b>extraction ratio</b> (fraction removed in one pass):<br>- high-extraction drugs (lidocaine): {{c1::<b>blood flow</b>}}<br>- low-extraction drugs (warfarin): {{c2::<b>enzyme activity</b>}}</div>',
                 "Extra": "- A high-extraction liver clears almost all that arrives, so only more flow clears more<br>- A low-extraction liver is limited by its enzymes and by the free fraction"},
 1792657543181: {"Text": "Organ clearance is <b>blood flow</b> times extraction ratio, so it can never exceed the organ's {{c1::<b>blood flow</b>}}",
                 "Extra": "- Extraction ratio: fraction of drug removed in one pass, from 0 to 1<br>- When it is 1, everything that arrives is cleared and clearance equals blood flow"},
 1791762412899: {"Extra": "- cGMP activates protein kinase G, which lowers cytosolic Ca<sup>2+</sup> and lets myosin light chain be dephosphorylated: relaxation<br>- Nitrates give NO, and PDE5 inhibitors slow cGMP breakdown, so both act on this pathway"},
 # UC03 58
 1792695019665: {"Text": "HIV {{c2::<b>gp120</b>}} binds CD4 and a coreceptor, which exposes {{c1::<b>gp41</b>}} to fuse the envelope with the cell membrane",
                 "Extra": "- gp120 binds CD4 → changes shape → binds CCR5 or CXCR4<br>- gp41 harpoons into the cell membrane and folds back like a zipper, pulling the two membranes together<br>- Enfuvirtide binds gp41 and blocks this fold"},
 # UC08 BC10 embriologia (imagem, negrito de contexto, contexto embriológico)
 1792659585105: {"Text": "<b>Cephalocaudal and lateral folding</b> of the embryo pull the endoderm inside and close it into the {{c1::<b>primitive gut</b>}} tube",
                 "Extra": "- The yolk sac stays outside, connected by the vitelline duct<br>- The tube ends blind at both ends, in the foregut and hindgut<br>" + L("15-1")},
 1792659586974: {"Text": '<div data-nebli-organizacao="true"><b>Embryonic origin</b> of the gut wall layers:<br>- epithelium and glands: {{c1::<b>endoderm</b>}}<br>- muscle, connective tissue, serosa: {{c1::<b>splanchnic mesoderm</b>}}</div>',
                 "Extra": "- Splanchnic mesoderm lines the gut, while somatic mesoderm lines the body wall<br>" + L("15-3")},
 1792659587475: {"Text": "In the embryo, the <b>septum transversum</b> receives the growing {{c1::<b>liver</b>}} and later forms the central tendon of the {{c2::<b>diaphragm</b>}}",
                 "Extra": "- It is mesoderm between the heart and the yolk-sac stalk<br>- Around the liver it gives the capsule, the lesser omentum and the falciform ligament<br>" + L("15-15")},
 1792659588552: {"Text": "<b>Rotation of the stomach</b> in the embryo pulls the dorsal mesogastrium left, opening the {{c1::<b>omental bursa</b>}} behind it",
                 "Extra": "- The bursa opens to the rest of the peritoneal cavity through the epiploic foramen<br>" + L("15-9")},
 1792659592051: {"Text": "After the embryonic gut returns, the <b>ascending and descending colon</b> fuse posteriorly and become {{c1::<b>secondarily retroperitoneal</b>}}",
                 "Extra": "- Their mesocolon fuses with the posterior parietal peritoneum<br>- The mesentery proper of the small intestine stays free<br>" + L("15-30")},
 1792659596102: {"Text": "In the embryo, the <b>foregut endoderm</b> buds out the {{c1::<b>liver</b>}} and the {{c1::<b>pancreas</b>}}",
                 "Extra": "- Both buds grow from the duodenal region into the surrounding mesoderm, which gives their connective tissue<br>" + L("15-19")},
 1792659596600: {"Text": "The <b>embryonic liver</b> starts in week 3 as the {{c1::<b>hepatic bud</b>}}, an outgrowth of foregut endoderm into the septum transversum",
                 "Extra": "- Its connection with the gut narrows into the bile duct<br>" + L("15-14")},
 1792659598025: {"Text": "In the <b>embryonic liver</b>, hepatic cords grow around the vitelline and umbilical veins, whose branches become the {{c1::<b>sinusoids</b>}}",
                 "Extra": "- So gut blood (vitelline, later the portal vein) and placental blood (umbilical) pass between hepatocytes<br>- The vitelline veins later form the portal vein<br>" + L("13-47")},
 1792659598275: {"Text": "<b>Rotation of the stomach</b> in the embryo moves the liver to the {{c1::<b>right</b>}} and the spleen to the {{c1::<b>left</b>}}",
                 "Extra": "- The liver was at first on the midline<br>- The spleen develops in the dorsal mesogastrium, which swings left with the stomach<br>" + L("15-10")},
 1792659598525: {"Text": "The embryonic <b>pancreas</b> forms from a {{c1::<b>dorsal</b>}} and a {{c1::<b>ventral</b>}} bud of duodenal endoderm",
                 "Extra": "- Dorsal bud: most of the gland, body and tail<br>- Ventral bud: uncinate process and lower head, next to the bile duct<br>" + L("15-19")},
 1792659598777: {"Text": "As the <b>embryonic duodenum</b> rotates, the {{c1::<b>ventral</b>}} pancreatic bud swings behind it and fuses with the dorsal bud",
                 "Extra": "- The main pancreatic duct joins the ventral duct with the distal dorsal duct<br>- If the ducts fail to fuse, the result is pancreas divisum<br>" + L("15-20")},
 1792659601153: {"Text": "The embryonic <b>pancreas</b> becomes {{c1::<b>retroperitoneal</b>}} when the duodenum and its mesentery fuse with the posterior wall",
                 "Extra": "- The dorsal mesoduodenum disappears, so the gland lies against the posterior wall<br>" + L("15-17")},
}
EXTRA_ADD = {  # notas de acervo: só acrescentar a figura no verso
 1792659597350: L("15-16"), 1792659597673: L("15-10"), 1792659599275: L("15-20"), 1792659600102: L("15-20"),
}
BOLD = {  # negrito de contexto (fora do cloze), primeiro termo encontrado
 1792659587805: "90° turn of the stomach", 1792659588053: "posterior wall of the stomach", 1792659590325: "midgut herniates",
 1792659596852: "ventral mesentery", 1792659601722: "Pancreatic acinar cells", 1792659603225: "liver", 1792659603475: "pig liver",
 1792659604802: "Hepatic sinusoids", 1792659606725: "Bile canaliculi", 1792659606977: "hepatocyte", 1792659607326: "hepatic acinus",
 1792659608252: "Acinus zone 1",
 1792677732277: "obligate intracellular parasites", 1792695018040: "new infectious virions", 1792695053292: "RNA viruses",
 1792753603464: "portal of entry", 1792753604544: "respiratory tract", 1792753606720: "Localized viral infections",
 1792753606970: "Virus in the blood", 1792753609843: "Latency", 1792753615215: "Acute viral infections",
 1792753616942: "host's own inflammatory response", 1792753617191: "Viral infections", 1792753617439: "viral receptor",
 1792753618769: "no longer cause disease", 1792753623542: "rotavirus", 1792753628995: "Influenza strains", 1792753631568: "Alcohol gel",
 1792753632392: "Poliovirus and rhinovirus", 1792753634465: "latency", 1792753634717: "transfusion of HBV-infected blood",
 1792753635466: "injected into blood", 1792753635966: "HPV", 1792753636286: "RNA viruses", 1792753637244: "outcome of a viral infection",
}
INTUMESC = {1792572870673: "Intumescência cervical (C4–T1)", 1792697128127: "Intumescência lombossacral (L1–S2)"}
RESP = {
 1791631347467: "Anotado como modelo de custo-efetividade (23/10): uma função + o efeito de inibi-la + verso que aprofunda; regra no MEMORY §6.",
 1792659598275: "Corrigido em 23/10. O deck já tinha intestino anterior, médio e posterior (3 AnKing) e a rotação da alça média; faltava o suprimento arterial: associados os 3 cards AnKing (tronco celíaco, mesentérica superior, inferior) depois dos de origem.",
 1791762424899: "Corrigido em 23/10: organizador novo de indutores × inibidores do CYP450 logo depois deste card (o AnKing só tem cards soltos por fármaco).",
 1791762412899: "Bandeira vermelha lida em 23/10: o verso só repetia a frente; agora explica o que o cGMP faz e onde nitratos e inibidores de PDE5 atuam.",
}
CYP = {"Text": '<div data-nebli-organizacao="true"><b>CYP450</b> interactions:<br>- inducers ({{c1::<b>rifampin</b>}}, phenytoin, carbamazepine, phenobarbital) lower other drugs<br>- inhibitors ({{c2::<b>macrolides</b>}}, azoles, ritonavir, cimetidine, grapefruit) raise them</div>',
       "Extra": "- Inducer: faster metabolism, less warfarin effect, risk of clotting<br>- Inhibitor: slower metabolism, more warfarin effect, risk of bleeding"}
CYP_TAGS = ["NEBLI::2026-uc19-farmacologia-01-introducao-mecanismos", "NEBLI::cor::2026-uc19-farmacologia-01-introducao-mecanismos::azul",
            "NEBLI::origem::Autoral", "NEBLI::escopo::aula", "NEBLI::objetivo::E-antagonismo", "NEBLI::feedback::comentarios-20261023"]
DECK_FA01 = "NEBLI::UC19::P1::Farmacologia::Introdução à farmacologia e mecanismos de ação"
BC10 = "NEBLI::2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas"
ARTERIAS = [1790981513725, 1790981520801, 1790981523653]  # cópias NEBLI de 1486767159823/163689/179344 (HY1)
CLOZE = re.compile(r"\{\{c\d+::.*?\}\}", re.S)


def bold_fora(texto, termo):
    partes = CLOZE.split(texto); clozes = CLOZE.findall(texto)
    for i, p in enumerate(partes):
        j = p.find(termo)
        if j >= 0:
            partes[i] = p[:j] + f"<b>{termo}</b>" + p[j + len(termo):]
            break
    else:
        raise SystemExit(f"termo não achado fora do cloze: {termo!r}")
    return "".join(x for par in zip(partes, clozes + [""]) for x in par)


def inserir_ordem(prefixo, depois, n):
    """Abre n posições depois de <prefixo>-<depois>, empurrando as seguintes."""
    ids = A("findNotes", query=f'"tag:NEBLI::ordem::{prefixo}-*"')
    mov = []
    for x in A("notesInfo", notes=ids):
        for t in x["tags"]:
            m = re.match(rf"NEBLI::ordem::{re.escape(prefixo)}-(\d+)$", t)
            if m and int(m.group(1)) > depois:
                mov.append((x["noteId"], t, f"NEBLI::ordem::{prefixo}-{int(m.group(1)) + n:02d}"))
    for nid, velho, novo in sorted(mov, key=lambda m: -int(m[1].rsplit("-", 1)[1])):
        A("removeTags", notes=[nid], tags=velho); A("addTags", notes=[nid], tags=novo)
    return [f"NEBLI::ordem::{prefixo}-{depois + k:02d}" for k in range(1, n + 1)]


if __name__ == "__main__":
    simular = "--simular" in sys.argv
    pasta = Path(A("getMediaDirPath"))
    notas = {n["noteId"]: n for n in A("notesInfo", notes=list(set(NEW) | set(EXTRA_ADD) | set(BOLD) | set(INTUMESC) | set(RESP)))}
    plano = {}
    for nid, f in NEW.items():
        plano[nid] = dict(f)
    for nid, add in EXTRA_ADD.items():
        plano[nid] = {"Extra": notas[nid]["fields"]["Extra"]["value"].rstrip() + "<br>" + add}
    for nid, termo in BOLD.items():
        base = plano.get(nid, {}).get("Text") or notas[nid]["fields"]["Text"]["value"]
        plano.setdefault(nid, {})["Text"] = bold_fora(base, termo)
    midia_ki = {}
    for nid, nome in INTUMESC.items():
        campos = {k: v["value"] for k, v in notas[nid]["fields"].items()}
        novos, midia = renomear(campos, nome, HERE / "img", pasta)
        plano[nid] = novos; midia_ki.update(midia)
    falta = [m for m in re.findall(r'src="([^"]+)"', json.dumps(plano)) if m not in MIDIA and not (pasta / m).exists() and m not in midia_ki]
    if falta:
        raise SystemExit(f"mídia ausente: {falta}")
    print(json.dumps({"notas": len(plano), "midia_nova": sorted(MIDIA) + sorted(midia_ki)}, ensure_ascii=False))
    if simular:
        sys.exit()
    atual = em_tela(A); feitos, pulados = [], []
    with escrita(A, "comentários 23/10", sync=False):
        for nome, p in list(MIDIA.items()) + list(midia_ki.items()):
            A("storeMediaFile", filename=nome, data=base64.b64encode(Path(p).read_bytes()).decode())
        for nid, f in plano.items():
            if nid in atual: pulados.append(nid); continue
            A("updateNoteFields", note={"id": nid, "fields": f}); feitos.append(nid)
        A("addTags", notes=feitos, tags="NEBLI::feedback::comentarios-20261023")
        # cards novos de c2 (FOXO1, gp41/gp120): mesma cor e suspensão do c1
        for nid in (1791627550702, 1792695019665):
            cs = A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))
            flag = next((c["flags"] for c in cs if c["flags"]), 0)
            for c in cs:
                if not c["flags"] and flag:
                    A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[flag], warning_check=True)
        # organizador do CYP450 logo depois do fenobarbital (fa01-88)
        pos = inserir_ordem("fa01", 88, 1)
        cyp = A("addNote", note={"deckName": DECK_FA01, "modelName": "NEBLI AnKing independente - v3", "fields": CYP,
                                 "tags": CYP_TAGS + pos, "options": {"allowDuplicate": False}})
        for c in A("findCards", query=f"nid:{cyp}"):
            A("setSpecificValueOfCard", card=c, keys=["flags"], newValues=[4], warning_check=True)
        # artérias do intestino primitivo na BC10, depois de origem de anterior/médio/posterior (bc10-04..06)
        pos = inserir_ordem("bc10", 6, 3)
        for nid, t in zip(ARTERIAS, pos):
            A("addTags", notes=[nid], tags=f"{BC10} NEBLI::cor::{BC10.split('::')[1]}::verde NEBLI::compartilhado::bc10 {t}")
        # marcar comentários
        for nid in [n for n in plano if "NEBLI_Comentario" in notas[n]["fields"] and notas[n]["fields"]["NEBLI_Comentario"]["value"].strip()] + [1791631347467]:
            if nid in pulados: continue
            old = A("notesInfo", notes=[nid])[0]["fields"]["NEBLI_Comentario"]["value"].rstrip()
            if not old or old.endswith(MARK): continue
            A("updateNoteFields", note={"id": nid, "fields": {"NEBLI_Comentario": old + "<br>" + MARK,
                                                               "NEBLI_Resposta": RESP.get(nid, "Corrigido em 23/10/2026.")}})
            A("addTags", notes=[nid], tags="NEBLI_comentario::respondido"); A("removeTags", notes=[nid], tags="NEBLI_comentario::pendente")
        for nid in (1791762412899,):
            A("updateNoteFields", note={"id": nid, "fields": {"NEBLI_Resposta": RESP[nid]}})
    # cartões que ficaram vazios (tubo neural: c2/c3 → c1)
    vazios = [c["cardId"] for c in A("cardsInfo", cards=A("findCards", query="nid:1792588686980")) if c["ord"] > 0]
    (HERE.parents[0] / "anki-acao-pedido.json").write_text(json.dumps({"acao": "remover_vazios", "deck": "", "cards": vazios}))
    print(json.dumps({"alterados": len(feitos), "pulados_em_tela": pulados, "cyp": cyp, "vazios_pedidos": vazios}))
