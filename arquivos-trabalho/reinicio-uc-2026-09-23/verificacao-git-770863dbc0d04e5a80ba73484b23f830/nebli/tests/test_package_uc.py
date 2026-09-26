import json
import sqlite3
import tempfile
import unittest
import zipfile
from contextlib import closing
from pathlib import Path

from nebli.package_uc import prepare_package, sha256


class PackageTests(unittest.TestCase):
    def fixture(self, directory):
        path = directory / "source.apkg"
        db = directory / "test.anki2"
        with closing(sqlite3.connect(db)) as con:
            con.executescript("create table cards(id integer, nid integer, did integer, flags integer, reps integer);"
                              "create table notes(id integer, guid text, flds text);"
                              "create table col(decks text);")
            con.execute("insert into col values (?)", (json.dumps({"10": {"name": "NEBLI::UC03::Aula"}}),))
            con.executemany("insert into cards values (?,?,?,?,?)", [(1, 2, 10, 5, 7), (3, 2, 10, 11, 8)])
            con.execute("insert into notes values (2,'stable-guid','question')")
            con.commit()
        with zipfile.ZipFile(path, "w") as archive:
            archive.write(db, "collection.anki2")
            archive.writestr("media", json.dumps({"0": "image.svg"}))
            archive.writestr("0", "<svg>" + "abc" * 5000 + "</svg>")
        return path

    def test_flags_only_and_compression(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            source = self.fixture(folder)
            original = sha256(source)
            target = folder / "NEBLI-UC03.apkg"
            result = prepare_package(source, target, [1, 3], "NEBLI::UC03")
            self.assertEqual(sha256(source), original)
            self.assertLess(result["output_bytes"], result["source_bytes"])
            with zipfile.ZipFile(target) as archive:
                self.assertTrue(all(i.compress_type == zipfile.ZIP_DEFLATED for i in archive.infolist()))
                check = folder / "check.anki2"
                check.write_bytes(archive.read("collection.anki2"))
            with closing(sqlite3.connect(check)) as con:
                self.assertEqual(con.execute("select flags,reps from cards order by id").fetchall(), [(0, 7), (8, 8)])
                self.assertEqual(con.execute("select guid from notes").fetchone()[0], "stable-guid")

    def test_mismatched_scope_does_not_produce_package(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            source = self.fixture(folder)
            target = folder / "UC08.apkg"
            with self.assertRaises(ValueError):
                prepare_package(source, target, [1, 3], "NEBLI::UC08")
            self.assertFalse(target.exists())
            with self.assertRaises(ValueError):
                prepare_package(source, target, [1], "NEBLI::UC03")
            self.assertFalse(target.exists())

    def test_refuses_overwrite_and_modern_format(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            source = self.fixture(folder)
            with self.assertRaises(ValueError):
                prepare_package(source, source)
            with zipfile.ZipFile(folder / "modern.apkg", "w") as archive:
                archive.writestr("collection.anki21b", b"not-sqlite")
            with self.assertRaises(ValueError):
                prepare_package(folder / "modern.apkg", folder / "output.apkg")
            self.assertFalse((folder / "output.apkg").exists())


if __name__ == "__main__":
    unittest.main()
