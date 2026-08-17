import json
from pathlib import Path
import jsonschema
from conftest import lesson

SCHEMA=Path(__file__).parents[1]/"schemas"/"deck-data-v13.schema.json"


def test_real_v13_fixture_matches_single_schema(tmp_path):
    _,data=lesson(tmp_path)
    schema=json.loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.validate(instance=data,schema=schema)
