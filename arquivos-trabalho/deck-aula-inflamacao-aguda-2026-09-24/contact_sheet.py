"""Read-only contact sheet for media selected into X2."""
import json
import re
from pathlib import Path
from PIL import Image, ImageDraw
from apply import call, HERE

def main():
    plan = json.loads((HERE / "plan.json").read_text(encoding="utf-8"))
    media = Path(call("getMediaDirPath"))
    rows, seen = [], set()
    for e in plan["entries"]:
        for field in e["fields"].values():
            for name in re.findall(r'<img[^>]*src="([^"]+)"', field):
                if name not in seen:
                    seen.add(name)
                    rows.append((e["source_nid"] or e.get("key"), name))
    w, h, columns = 250, 210, 5
    sheet = Image.new("RGB", (w * columns, h * ((len(rows) + columns - 1) // columns)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, (key, name) in enumerate(rows):
        im = Image.open(media / name)
        im.thumbnail((235, 170))
        x, y = (i % columns) * w, (i // columns) * h
        sheet.paste(im.convert("RGB"), (x + 5, y + 25))
        draw.text((x + 5, y + 5), str(key), fill="black")
    sheet.save(HERE / "selected-media-contact.jpg", quality=85)
    print(len(rows))

if __name__ == "__main__":
    main()
