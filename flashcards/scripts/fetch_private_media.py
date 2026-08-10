#!/usr/bin/env python3
"""fetch_private_media.py — puxa do Drive só a mídia dos cards escolhidos.

A mídia do AnKing está em 67 shards de ~89 MB (5,9 GB no total). Baixar um shard
inteiro para extrair uma figura é absurdo, e baixar todos é impossível. Este
script lê **apenas os bytes necessários**: a API do Drive aceita `Range`, e um
ZIP permite localizar um membro pelo diretório central, que fica no fim do
arquivo. Uma imagem de 120 KB custa ~120 KB de download, não 89 MB.

Fluxo por arquivo pedido:
  manifesto de shards → em qual shard está
  cauda do shard      → End of Central Directory
  diretório central   → offset e tamanho do membro
  range do membro     → bytes, inflados localmente

Uso:
  python flashcards/scripts/fetch_private_media.py --inspect-manifest
  python flashcards/scripts/fetch_private_media.py --out-dir flashcards/private-cache/media \\
      paste-abc123.jpg tralha-xyz.png
  python flashcards/scripts/fetch_private_media.py --from-json midias.json
"""
from __future__ import annotations

import argparse
import io
import json
import struct
import sys
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from fetch_private_index import (  # noqa: E402
    API,
    Falha,
    achar_pasta,
    baixar,
    listar,
    obter_token,
)

RAIZ = Path(__file__).resolve().parents[2]
CACHE = RAIZ / "flashcards/private-cache"
MANIFESTO_MIDIA = "media-shards-manifest.json"
EOCD_ASSINATURA = b"PK\x05\x06"
CAUDA = 128 * 1024


def _range(url: str, token: str, inicio: int, fim: int) -> bytes:
    import urllib.error
    import urllib.request

    requisicao = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Range": f"bytes={inicio}-{fim}",
    })
    try:
        with urllib.request.urlopen(requisicao, timeout=300) as resposta:
            if resposta.status not in (200, 206):
                raise Falha(f"esperava 206 Partial Content, veio {resposta.status}")
            return resposta.read()
    except urllib.error.HTTPError as erro:
        detalhe = erro.read().decode("utf-8", "replace")[:300]
        raise Falha(f"Drive respondeu {erro.code} num range: {detalhe}") from None


def tamanho_do_arquivo(token: str, file_id: str) -> int:
    from fetch_private_index import _get

    dados = _get(f"{API}/files/{file_id}?fields=size&supportsAllDrives=true", token) or {}
    if "size" not in dados:
        raise Falha(f"o Drive não informou o tamanho de {file_id}")
    return int(dados["size"])


def diretorio_central(token: str, file_id: str, tamanho: int) -> dict[str, tuple[int, int, int]]:
    """{nome: (offset do cabeçalho local, tamanho comprimido, método)}."""
    inicio = max(0, tamanho - CAUDA)
    cauda = _range(f"{API}/files/{file_id}?alt=media&supportsAllDrives=true", token,
                   inicio, tamanho - 1)
    posicao = cauda.rfind(EOCD_ASSINATURA)
    if posicao == -1:
        raise Falha("não achei o End of Central Directory na cauda do shard "
                    "(zip64 com comentário longo?)")
    entradas, cd_tamanho, cd_offset = struct.unpack("<HLL", cauda[posicao + 10:posicao + 20])

    if cd_offset == 0xFFFFFFFF or entradas == 0xFFFF:
        raise Falha("shard em formato zip64; o leitor precisaria do locator zip64")

    if cd_offset >= inicio:
        bruto = cauda[cd_offset - inicio:cd_offset - inicio + cd_tamanho]
    else:
        bruto = _range(f"{API}/files/{file_id}?alt=media&supportsAllDrives=true", token,
                       cd_offset, cd_offset + cd_tamanho - 1)

    indice, ponteiro = {}, 0
    for _ in range(entradas):
        if bruto[ponteiro:ponteiro + 4] != b"PK\x01\x02":
            break
        metodo = struct.unpack("<H", bruto[ponteiro + 10:ponteiro + 12])[0]
        comprimido = struct.unpack("<L", bruto[ponteiro + 20:ponteiro + 24])[0]
        n_nome, n_extra, n_com = struct.unpack("<HHH", bruto[ponteiro + 28:ponteiro + 34])
        offset_local = struct.unpack("<L", bruto[ponteiro + 42:ponteiro + 46])[0]
        nome = bruto[ponteiro + 46:ponteiro + 46 + n_nome].decode("utf-8", "replace")
        indice[nome] = (offset_local, comprimido, metodo)
        ponteiro += 46 + n_nome + n_extra + n_com
    return indice


def extrair_membro(token: str, file_id: str, entrada: tuple[int, int, int]) -> bytes:
    offset_local, comprimido, metodo = entrada
    url = f"{API}/files/{file_id}?alt=media&supportsAllDrives=true"
    cabecalho = _range(url, token, offset_local, offset_local + 29)
    if cabecalho[:4] != b"PK\x03\x04":
        raise Falha("cabeçalho local do zip não confere")
    n_nome, n_extra = struct.unpack("<HH", cabecalho[26:30])
    inicio = offset_local + 30 + n_nome + n_extra
    bruto = _range(url, token, inicio, inicio + comprimido - 1)
    if metodo == 0:
        return bruto
    if metodo == 8:
        return zlib.decompress(bruto, -zlib.MAX_WBITS)
    raise Falha(f"método de compressão {metodo} não suportado")


def carregar_manifesto(token: str, pasta: str) -> dict:
    local = CACHE / MANIFESTO_MIDIA
    if not local.exists():
        arquivos = {a["name"]: a for a in listar(token, f"'{pasta}' in parents and trashed = false")}
        if MANIFESTO_MIDIA not in arquivos:
            raise Falha(f"'{MANIFESTO_MIDIA}' não está na pasta do índice")
        print(f"baixando {MANIFESTO_MIDIA}…", file=sys.stderr)
        baixar(token, arquivos[MANIFESTO_MIDIA]["id"], local)
    return json.loads(local.read_text(encoding="utf-8"))


def mapa_de_shards(manifesto) -> dict[str, str]:
    """Normaliza o manifesto para {nome do arquivo: nome do shard}.

    O manifesto foi gerado por outro notebook e o formato exato não está
    documentado; aceitamos as formas plausíveis e falamos claro se não bater.
    """
    if isinstance(manifesto, dict):
        for chave in ("files", "media", "mapping", "index"):
            if isinstance(manifesto.get(chave), dict):
                manifesto = manifesto[chave]
                break
        if all(isinstance(valor, str) for valor in list(manifesto.values())[:20]):
            return manifesto
        if all(isinstance(valor, dict) for valor in list(manifesto.values())[:20]):
            return {
                nome: valor.get("shard") or valor.get("archive") or valor.get("zip")
                for nome, valor in manifesto.items()
            }
    if isinstance(manifesto, list):
        return {
            item["name"]: item.get("shard") or item.get("archive") or item.get("zip")
            for item in manifesto if isinstance(item, dict) and "name" in item
        }
    raise Falha("não reconheci o formato de media-shards-manifest.json; "
                "rode com --inspect-manifest e me mostre a saída")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivos", nargs="*", help="nomes de mídia, como aparecem no campo da nota")
    ap.add_argument("--from-json", help="JSON com uma lista de nomes de mídia")
    ap.add_argument("--folder", default="AnKing-index-v2")
    ap.add_argument("--out-dir", default=str(CACHE / "media"))
    ap.add_argument("--inspect-manifest", action="store_true",
                    help="só descreve a estrutura do manifesto de shards")
    args = ap.parse_args()

    token = obter_token()
    pasta = achar_pasta(token, args.folder)
    manifesto = carregar_manifesto(token, pasta)

    if args.inspect_manifest:
        amostra = manifesto
        forma = {"tipo": type(manifesto).__name__}
        if isinstance(manifesto, dict):
            forma["chaves_de_topo"] = list(manifesto)[:8]
            primeira = next(iter(manifesto.items()), None)
            if primeira:
                forma["primeiro_par"] = [primeira[0], primeira[1] if not isinstance(primeira[1], (dict, list)) else str(primeira[1])[:200]]
        elif isinstance(manifesto, list):
            forma["itens"] = len(amostra)
            forma["primeiro_item"] = str(amostra[0])[:200] if amostra else None
        print(json.dumps(forma, ensure_ascii=False, indent=2))
        return 0

    desejados = list(args.arquivos)
    if args.from_json:
        desejados += json.loads(Path(args.from_json).read_text(encoding="utf-8"))
    if not desejados:
        raise Falha("informe ao menos um nome de mídia")

    mapa = mapa_de_shards(manifesto)
    shards_no_drive = {a["name"]: a["id"]
                       for a in listar(token, f"'{pasta}' in parents and trashed = false")}

    por_shard: dict[str, list[str]] = {}
    ausentes = []
    for nome in desejados:
        shard = mapa.get(nome)
        if not shard:
            ausentes.append(nome)
            continue
        por_shard.setdefault(shard, []).append(nome)

    saida = Path(args.out_dir)
    saida.mkdir(parents=True, exist_ok=True)
    escritos, bytes_baixados = [], 0

    for shard, nomes in sorted(por_shard.items()):
        if shard not in shards_no_drive:
            ausentes.extend(nomes)
            continue
        file_id = shards_no_drive[shard]
        tamanho = tamanho_do_arquivo(token, file_id)
        indice = diretorio_central(token, file_id, tamanho)
        for nome in nomes:
            entrada = indice.get(nome)
            if entrada is None:
                ausentes.append(nome)
                continue
            dados = extrair_membro(token, file_id, entrada)
            (saida / nome).write_bytes(dados)
            escritos.append(nome)
            bytes_baixados += entrada[1]

    print(json.dumps({
        "solicitados": len(desejados),
        "escritos": len(escritos),
        "ausentes": ausentes,
        "shards_tocados": len(por_shard),
        "bytes_transferidos_aprox": bytes_baixados,
        "out_dir": str(saida),
    }, ensure_ascii=False, indent=2))
    return 1 if ausentes else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Falha as erro:
        print(json.dumps({"status": "error", "detail": str(erro)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
