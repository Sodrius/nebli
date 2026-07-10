#!/usr/bin/env python3
"""Ad-hoc: extrai texto + imagens de um .pptx para slide-XX.png + MAPA_CONTEUDO.txt."""
import sys, zipfile, re, shutil
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
}

def main():
    pptx_path = Path(sys.argv[1])
    tema = sys.argv[2]
    out = Path(__file__).resolve().parent.parent / "figuras" / tema
    out.mkdir(parents=True, exist_ok=True)

    z = zipfile.ZipFile(pptx_path)
    # ordenar slides numericamente
    slide_names = sorted(
        [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)],
        key=lambda n: int(re.search(r'slide(\d+)', n).group(1))
    )

    mapa = [
        f"# MAPA_CONTEUDO -- {tema}",
        f"# Slide-fonte: {pptx_path.name}",
        f"# Gerado por extrair_pptx.py",
        "",
    ]

    for idx, sname in enumerate(slide_names, 1):
        slide_id = f"slide-{idx:02d}"
        # texto
        root = ET.fromstring(z.read(sname))
        texts = [t.text for t in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t') if t.text]
        text = " ".join(" ".join(t.split()) for t in texts).strip()

        # imagem principal: olha _rels
        rels_name = sname.replace('slides/', 'slides/_rels/') + '.rels'
        img_target = None
        if rels_name in z.namelist():
            rels_root = ET.fromstring(z.read(rels_name))
            for rel in rels_root:
                tgt = rel.attrib.get('Target', '')
                if '/media/' in tgt and tgt.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    img_target = tgt
                    break  # primeira imagem
        if img_target:
            # resolver path relativo
            img_path = ('ppt/' + img_target.replace('../', '')).replace('//', '/')
            ext = Path(img_target).suffix.lower()
            dest = out / f"{slide_id}{ext}"
            with z.open(img_path) as src, open(dest, 'wb') as dst:
                shutil.copyfileobj(src, dst)
            origin = img_path
        else:
            origin = "[sem imagem embutida]"

        preview = text[:300] + ("..." if len(text) > 300 else "")
        if len(text) < 5:
            mapa.append(f"{slide_id}: [VISUAL ou title-only] | imagem: {origin}")
        else:
            mapa.append(f"{slide_id}: {preview} | imagem: {origin}")

    (out / "MAPA_CONTEUDO.txt").write_text("\n".join(mapa) + "\n", encoding="utf-8")
    print(f"OK {len(slide_names)} slides em {out}")
    for line in mapa[4:9]:
        print(" ", line[:180])

if __name__ == "__main__":
    main()
