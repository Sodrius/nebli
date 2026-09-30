"""Integridade da memória/documentação; não avalia a qualidade semântica de decks."""
from pathlib import Path
import hashlib
import json
import re
import unittest
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "backups/contexto-2026-09-29-consolidacao.zip"
PUBLIC_CONTEXT = (
    "README", "EXECUCAO-DECK-AULA", "ACERVOS-REFERENCIA", "FEEDBACKS",
    "RECONSTRUCAO-UC08", "HISTORICO", "CALIBRACAO-DECK-100-PERGUNTAS",
)


class HandoffTests(unittest.TestCase):
    def test_entrypoints_route_to_current_pipeline(self):
        for path in ("AGENTS.md", "CLAUDE.md", ".claude/commands/deck-aula.md",
                     ".claude/commands/resumo.md", ".claude/commands/flashcards.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            for name in ("README.md", "MEMORY.md", "FEEDBACKS.md", "EXECUCAO-DECK-AULA.md"):
                self.assertIn(name, text, path)
            self.assertIn("E1 + cards", text, path)
            self.assertNotIn("BANDEIRAS-E-PROGRESSAO.md", text, path)
            self.assertNotIn("HANDOFF-CLAUDE.md", text, path)

    def test_required_public_context_and_local_links_exist(self):
        paths = [ROOT / "flashcards/projeto" / f"{name}.md" for name in PUBLIC_CONTEXT]
        paths += [ROOT / name for name in ("MEMORY.md", "AGENTS.md", "CLAUDE.md", "flashcards/README.md")]
        for path in paths:
            self.assertTrue(path.is_file(), str(path))
            # Links in the literal questionnaire/feedback may cite private historical
            # evidence. New active entrypoints must work without those local artifacts.
            if path.name in ("FEEDBACKS.md", "CALIBRACAO-DECK-100-PERGUNTAS.md"):
                continue
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                target = target.split("#", 1)[0]
                self.assertTrue((path.parent / target).exists(), f"{path.name}: {target}")
        self.assertTrue((ROOT / "config/publicacoes-uc.example.json").is_file())

    def test_archived_context_preserved_byte_for_byte(self):
        archive = ROOT / "backups/contexto-2026-09-25"
        manifest = json.loads((archive / "manifest.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(manifest["files"]), 17)
        for item in manifest["files"]:
            data = (archive / item["path"]).read_bytes()
            self.assertEqual(len(data), item["bytes"], item["path"])
            self.assertEqual(hashlib.sha256(data).hexdigest(), item["sha256"], item["path"])

    def test_consolidation_archive_preserves_removed_docs_and_saved_answers(self):
        with ZipFile(ARCHIVE) as archive:
            self.assertEqual(len(archive.namelist()), len(set(archive.namelist())))
            self.assertIsNone(archive.testzip())
            items = json.loads(archive.read("manifest.json"))["files"]
            self.assertEqual(len(items), 41)
            for item in items:
                if item["path"].startswith("flashcards/projeto/"):
                    if Path(item["path"]).stem not in PUBLIC_CONTEXT:
                        self.assertFalse((ROOT / item["path"]).exists(), item["path"])
            self.assertFalse((ROOT / "HANDOFF-CLAUDE.md").exists())
            items += [json.loads(archive.read("respostas-salvas/manifest.json"))]
            items += json.loads(archive.read("rotas-legadas/manifest.json"))["files"]
            for item in items:
                data = archive.read(item["path"])
                self.assertEqual(len(data), item["bytes"], item["path"])
                self.assertEqual(hashlib.sha256(data).hexdigest(), item["sha256"], item["path"])

    def test_questionnaire_bodies_preserve_literal_answers(self):
        def questions(text):
            text = text.split("## Fechamento desta calibração", 1)[0]
            chunks = re.split(r"^#{2,3} (Q\d{3} — [^\n]+)\n", text, flags=re.M)
            return {chunks[i].split(" — ", 1)[0]: chunks[i + 1]
                    for i in range(1, len(chunks), 2)}

        with ZipFile(ARCHIVE) as archive:
            saved = archive.read("respostas-salvas/CALIBRACAO-DECK-100-PERGUNTAS.md").decode("utf-8")
        current = (ROOT / "flashcards/projeto/CALIBRACAO-DECK-100-PERGUNTAS.md").read_text(encoding="utf-8")
        self.assertEqual(len(questions(saved)), 100)
        self.assertEqual(questions(saved), questions(current))


if __name__ == "__main__":
    unittest.main()
