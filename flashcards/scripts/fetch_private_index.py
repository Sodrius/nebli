#!/usr/bin/env python3
"""fetch_private_index.py — traz o índice privado do AnKing para a sessão.

O elo que faltava para a curadoria acontecer. `index_private_apkg.py` constrói o
índice e `search_private_index.py` sabe buscar nele; o que nunca existiu foi o
passo de **colocar o arquivo dentro do ambiente onde a aula é produzida**.

Por que não pelo conector do Drive: aquele canal devolve o arquivo em base64
dentro do contexto do modelo, e o índice tem 103 MB comprimido. Aqui a conversa
é direta com a API do Drive por HTTPS — o arquivo vai para o disco e nunca passa
pelo contexto.

Credencial, por variável de ambiente, em um dos dois formatos:

  NEBLI_DRIVE_SA_JSON        conta de serviço (JSON inteiro ou caminho do arquivo)
  — ou —
  NEBLI_DRIVE_CLIENT_ID      cliente OAuth instalado
  NEBLI_DRIVE_CLIENT_SECRET
  NEBLI_DRIVE_REFRESH_TOKEN

Escopo suficiente: `drive.readonly`. Com conta de serviço, basta compartilhar a
pasta privada com o e-mail dela — nada mais do Drive fica exposto.

Uso:
  python flashcards/scripts/fetch_private_index.py            # baixa se faltar
  python flashcards/scripts/fetch_private_index.py --check    # só diz o que falta
  python flashcards/scripts/fetch_private_index.py --force
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DESTINO = RAIZ / "flashcards/private-cache"
API = "https://www.googleapis.com/drive/v3"
TOKEN_URL = "https://oauth2.googleapis.com/token"
ESCOPO = "https://www.googleapis.com/auth/drive.readonly"
PASTA_PADRAO = "AnKing-index-v2"
MANIFESTO = "index-package-manifest.json"


class Falha(RuntimeError):
    pass


# --------------------------------------------------------------------- auth
def _b64url(dados: bytes) -> str:
    return base64.urlsafe_b64encode(dados).rstrip(b"=").decode()


def _post_form(url: str, campos: dict) -> dict:
    corpo = urllib.parse.urlencode(campos).encode()
    requisicao = urllib.request.Request(
        url, corpo, {"Content-Type": "application/x-www-form-urlencoded"}
    )
    try:
        with urllib.request.urlopen(requisicao, timeout=60) as resposta:
            return json.load(resposta)
    except urllib.error.HTTPError as erro:
        detalhe = erro.read().decode("utf-8", "replace")[:400]
        raise Falha(
            f"o Google recusou a credencial ({erro.code}). Resposta: {detalhe}"
        ) from None


def token_conta_de_servico(bruto: str) -> str:
    try:
        import rsa
    except ImportError as erro:
        raise Falha("conta de serviço exige o pacote `rsa` (pip install rsa)") from erro

    caminho = Path(bruto)
    credencial = json.loads(caminho.read_text(encoding="utf-8") if caminho.exists() else bruto)
    agora = int(time.time())
    cabecalho = _b64url(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    reivindicacao = _b64url(json.dumps({
        "iss": credencial["client_email"],
        "scope": ESCOPO,
        "aud": TOKEN_URL,
        "iat": agora,
        "exp": agora + 3600,
    }).encode())
    assinatura = rsa.sign(
        f"{cabecalho}.{reivindicacao}".encode(),
        rsa.PrivateKey.load_pkcs1(credencial["private_key"].encode(), format="PEM")
        if "RSA PRIVATE KEY" in credencial["private_key"]
        else _carregar_pkcs8(credencial["private_key"]),
        "SHA-256",
    )
    jwt = f"{cabecalho}.{reivindicacao}.{_b64url(assinatura)}"
    resposta = _post_form(TOKEN_URL, {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt,
    })
    return resposta["access_token"]


def _carregar_pkcs8(pem: str):
    """Contas de serviço do Google entregam a chave em PKCS#8; `rsa` quer PKCS#1."""
    import rsa

    corpo = "".join(
        linha for linha in pem.splitlines() if "-----" not in linha
    )
    der = base64.b64decode(corpo)
    # PrivateKeyInfo ::= SEQUENCE { version, algorithm, privateKey OCTET STRING }
    marcador = der.find(b"\x04\x82")
    if marcador == -1:
        raise Falha("não reconheci o formato da chave privada da conta de serviço")
    tamanho = int.from_bytes(der[marcador + 2:marcador + 4], "big")
    interno = der[marcador + 4:marcador + 4 + tamanho]
    try:
        return rsa.PrivateKey._load_pkcs1_der(interno)
    except Exception as erro:
        raise Falha(f"não consegui ler a chave PKCS#8 da conta de serviço: {erro}") from None


def obter_token() -> str:
    conta = os.environ.get("NEBLI_DRIVE_SA_JSON", "").strip()
    if conta:
        return token_conta_de_servico(conta)

    cliente = os.environ.get("NEBLI_DRIVE_CLIENT_ID", "").strip()
    segredo = os.environ.get("NEBLI_DRIVE_CLIENT_SECRET", "").strip()
    refresh = os.environ.get("NEBLI_DRIVE_REFRESH_TOKEN", "").strip()
    if cliente and segredo and refresh:
        resposta = _post_form(TOKEN_URL, {
            "client_id": cliente,
            "client_secret": segredo,
            "refresh_token": refresh,
            "grant_type": "refresh_token",
        })
        return resposta["access_token"]

    raise Falha(
        "nenhuma credencial do Drive no ambiente. Defina NEBLI_DRIVE_SA_JSON "
        "ou o trio NEBLI_DRIVE_CLIENT_ID / _CLIENT_SECRET / _REFRESH_TOKEN."
    )


# --------------------------------------------------------------------- drive
def _get(url: str, token: str, binario_para: Path | None = None) -> dict | None:
    requisicao = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        resposta = urllib.request.urlopen(requisicao, timeout=900)
    except urllib.error.HTTPError as erro:
        detalhe = erro.read().decode("utf-8", "replace")[:400]
        raise Falha(f"Drive respondeu {erro.code} para {url.split('?')[0]}: {detalhe}") from None
    with resposta:
        if binario_para is None:
            return json.load(resposta)
        binario_para.parent.mkdir(parents=True, exist_ok=True)
        with binario_para.open("wb") as saida:
            shutil.copyfileobj(resposta, saida, length=8 * 1024 * 1024)
        return None


def listar(token: str, consulta: str) -> list[dict]:
    parametros = urllib.parse.urlencode({
        "q": consulta,
        "fields": "files(id,name,size,mimeType)",
        "pageSize": "200",
        "supportsAllDrives": "true",
        "includeItemsFromAllDrives": "true",
    })
    return (_get(f"{API}/files?{parametros}", token) or {}).get("files", [])


def achar_pasta(token: str, nome: str) -> str:
    consulta = (f"name = '{nome}' and mimeType = 'application/vnd.google-apps.folder' "
                f"and trashed = false")
    achados = listar(token, consulta)
    if not achados:
        raise Falha(f"pasta '{nome}' não encontrada no Drive desta credencial. "
                    f"Com conta de serviço, confira se a pasta foi compartilhada com ela.")
    return achados[0]["id"]


def baixar(token: str, file_id: str, destino: Path) -> None:
    _get(f"{API}/files/{file_id}?alt=media&supportsAllDrives=true", token, binario_para=destino)


def sha256(caminho: Path) -> str:
    digest = hashlib.sha256()
    with caminho.open("rb") as fluxo:
        for pedaco in iter(lambda: fluxo.read(8 * 1024 * 1024), b""):
            digest.update(pedaco)
    return digest.hexdigest()


# ---------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", default=PASTA_PADRAO, help="pasta do pacote de índice no Drive")
    ap.add_argument("--out-dir", default=str(DESTINO))
    ap.add_argument("--check", action="store_true", help="não baixa nada; só relata o estado")
    ap.add_argument("--force", action="store_true", help="rebaixa mesmo se o hash já bater")
    ap.add_argument("--keep-parts", action="store_true")
    args = ap.parse_args()

    destino = Path(args.out_dir)
    estado = {"index": None, "status": "unknown", "bytes": 0}

    try:
        token = obter_token()
    except Falha as erro:
        estado.update(status="no_credential", detail=str(erro))
        print(json.dumps(estado, ensure_ascii=False, indent=2))
        return 0 if args.check else 2

    pasta = achar_pasta(token, args.folder)
    arquivos = {arquivo["name"]: arquivo for arquivo in listar(token, f"'{pasta}' in parents and trashed = false")}
    if MANIFESTO not in arquivos:
        raise Falha(f"'{MANIFESTO}' não está em '{args.folder}'")

    manifesto_local = destino / MANIFESTO
    baixar(token, arquivos[MANIFESTO]["id"], manifesto_local)
    manifesto = json.loads(manifesto_local.read_text(encoding="utf-8"))

    indice = destino / manifesto["source_index"]
    if indice.exists() and not args.force:
        atual = sha256(indice)
        if atual == manifesto["source_sha256"]:
            estado.update(index=str(indice), status="already_current", bytes=indice.stat().st_size)
            print(json.dumps(estado, ensure_ascii=False, indent=2))
            return 0
        estado["stale_sha256"] = atual

    if args.check:
        estado.update(status="download_required",
                      needs=[parte["name"] for parte in manifesto["parts"]],
                      archive_bytes=manifesto["archive_bytes"])
        print(json.dumps(estado, ensure_ascii=False, indent=2))
        return 0

    partes = []
    for parte in manifesto["parts"]:
        if parte["name"] not in arquivos:
            raise Falha(f"parte '{parte['name']}' ausente na pasta do Drive")
        caminho = destino / parte["name"]
        if not (caminho.exists() and caminho.stat().st_size == parte["bytes"]
                and sha256(caminho) == parte["sha256"]):
            print(f"baixando {parte['name']} ({parte['bytes'] / 1e6:.0f} MB)…", file=sys.stderr)
            baixar(token, arquivos[parte["name"]]["id"], caminho)
            if sha256(caminho) != parte["sha256"]:
                raise Falha(f"sha256 não confere em {parte['name']}")
        partes.append(caminho)

    arquivo_zip = destino / manifesto["archive"]
    with arquivo_zip.open("wb") as saida:
        for caminho in partes:
            with caminho.open("rb") as entrada:
                shutil.copyfileobj(entrada, saida, length=8 * 1024 * 1024)
    if sha256(arquivo_zip) != manifesto["archive_sha256"]:
        raise Falha("sha256 do arquivo remontado não confere com o manifesto")

    with zipfile.ZipFile(arquivo_zip) as zf:
        zf.extract(manifesto["source_index"], destino)
    if sha256(indice) != manifesto["source_sha256"]:
        raise Falha("sha256 do índice extraído não confere com o manifesto")

    arquivo_zip.unlink(missing_ok=True)
    if not args.keep_parts:
        for caminho in partes:
            caminho.unlink(missing_ok=True)

    estado.update(index=str(indice), status="downloaded", bytes=indice.stat().st_size)
    print(json.dumps(estado, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Falha as erro:
        print(json.dumps({"status": "error", "detail": str(erro)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
