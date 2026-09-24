import tempfile
import unittest
from pathlib import Path
from nebli.registry import connect
class RegistryTests(unittest.TestCase):
    def test_migrations_are_idempotent(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/"state.sqlite"; first=connect(path); first.close(); second=connect(path)
            self.assertEqual(second.execute("SELECT COUNT(*) FROM schema_migration").fetchone()[0],1)
            second.close()
if __name__ == "__main__": unittest.main()
