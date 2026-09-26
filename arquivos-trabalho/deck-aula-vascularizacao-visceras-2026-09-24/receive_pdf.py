"""Materialize one authenticated Drive PDF from streamed base64 chunks."""
import base64
import hashlib
import sys
from pathlib import Path

output = Path(__file__).with_name("slides.pdf")
h = hashlib.sha256()
size = 0
with output.open("wb") as file:
    for line in sys.stdin.buffer:
        if line.strip() == b"END":
            break
        chunk = base64.b64decode(line.strip(), validate=True)
        file.write(chunk)
        h.update(chunk)
        size += len(chunk)
print(f"{size} {h.hexdigest()}", flush=True)
