import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validar_e1_formatacao.py"
SPEC = importlib.util.spec_from_file_location("validar_e1_formatacao", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


def review():
    return {
        "canonical_template_used": True,
        "all_pages_rendered": True,
        "layout_reviewed": True,
        "paragraph_hierarchy_preserved": True,
        "images_legible_and_integrated": True,
        "no_clipping_or_overflow": True,
        "independent_visual_review_passed": True,
        "unresolved_visual_defects": [],
        "summary": "Revisão visual integral concluída.",
    }


def write_canonical(tmp_path: Path):
    (tmp_path / "etapa1.typ").write_text(
        '#import "../../typst-template/nebli_v2_apostila.typ": *\n'
        '#intro-box[Introdução.]\n#parte-title("PARTE I", primeira: true)\n'
        '#subtopico("1.1 — Tema")\nTexto.\n#conclusao-box[Conclusão.]\n',
        encoding="utf-8",
    )
    (tmp_path / "main.typ").write_text(
        '#import "../../typst-template/nebli_v2_apostila.typ": *\n'
        '#show: pagina-padrao\n#capa("Título", "Sub", ())\n#sumario(())\n'
        '#etapa-header("Etapa 1")\n#include "etapa1.typ"\n#include "resumindo.typ"\n',
        encoding="utf-8",
    )
    (tmp_path / "resumindo.typ").write_text(
        '#import "../../typst-template/nebli_v2_apostila.typ": *\n'
        '#resumindo-page((("Síntese", [Texto.]),))\n',
        encoding="utf-8",
    )


def test_canonical_source_and_visual_review_pass(tmp_path):
    write_canonical(tmp_path)
    errors = MODULE.validate_e1_formatting(
        {"e1_source": "etapa1.typ", "e1_format_review": review()},
        tmp_path / "deck-data.json",
    )
    assert errors == []


def test_local_page_and_paragraph_overrides_fail(tmp_path):
    write_canonical(tmp_path)
    source = tmp_path / "etapa1.typ"
    source.write_text("#set page(margin: 8mm)\n#set par(justify: false)\n" + source.read_text(), encoding="utf-8")
    errors = MODULE.validate_e1_formatting(
        {"e1_source": "etapa1.typ", "e1_format_review": review()},
        tmp_path / "deck-data.json",
    )
    assert any("#set page" in error for error in errors)
    assert any("#set par" in error for error in errors)


def test_unresolved_visual_defect_fails(tmp_path):
    write_canonical(tmp_path)
    visual = review()
    visual["unresolved_visual_defects"] = ["imagem cortada"]
    errors = MODULE.validate_e1_formatting(
        {"e1_source": "etapa1.typ", "e1_format_review": visual},
        tmp_path / "deck-data.json",
    )
    assert any("unresolved_visual_defects" in error for error in errors)
