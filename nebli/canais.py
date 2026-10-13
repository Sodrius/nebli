"""Aulas dos canais que Davi acompanha: busca no YouTube e transcrição.

    python3 -m nebli.canais busca "<termo>" [n]
    python3 -m nebli.canais transcricao <video_id> <saida.txt>

A busca lê o ytInitialData da página de resultados (sem chave de API). A transcrição usa youtube_transcript_api
(inglês ou português). Transcrição baixada não é transcrição lida: declarar em fontes.json só o que foi lido.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request


def busca(q, n=8):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q)
    html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en"}), timeout=30).read().decode()
    data = json.loads(re.search(r"var ytInitialData = (\{.*?\});</script>", html).group(1))
    out = []

    def walk(o):
        if isinstance(o, dict):
            if "videoRenderer" in o:
                v = o["videoRenderer"]
                out.append((v["videoId"], "".join(r["text"] for r in v["title"]["runs"]),
                            "".join(r["text"] for r in v.get("ownerText", {}).get("runs", [])), v.get("lengthText", {}).get("simpleText", "")))
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk(data)
    return out[:n]


def transcricao(vid, path):
    from youtube_transcript_api import YouTubeTranscriptApi
    try:
        text = " ".join(s.text for s in YouTubeTranscriptApi().fetch(vid, languages=["en", "pt"]))
    except AttributeError:
        text = " ".join(s["text"] for s in YouTubeTranscriptApi.get_transcript(vid, languages=["en", "pt"]))
    text = re.sub(r"\s+", " ", text)
    open(path, "w").write(text)
    return len(text)


if __name__ == "__main__":
    if sys.argv[1] == "busca":
        for v in busca(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 8):
            print(" | ".join(v))
    else:
        print(sys.argv[3], transcricao(sys.argv[2], sys.argv[3]))
