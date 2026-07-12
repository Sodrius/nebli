#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sobe um arquivo (PDF de resumo, slide ou .apkg) pra pasta da aula no Drive do Davi,
seguindo a estrutura canônica (referencias-externas/DRIVE-ESTRUTURA.md).
Remote rclone: nebli-drive (service OAuth headless). NÃO mexe em permissões.
Uso: python subir_drive.py <arquivo_local> <slug> [nome_no_drive]
     (se nome_no_drive omitido, usa o nome do arquivo local)
"""
import sys, os, subprocess
sys.stdout.reconfigure(encoding="utf-8")
BASE = "nebli-drive:RESUMOS - Davi Sousa/B - Primeiro ano"
# slug -> "UC/Componente/NN - Aula" (pastas já existentes no Drive; ver DRIVE-ESTRUTURA.md)
MAP = {
 "bioq-20-pentoses-radicais-livres":      "UC02/Bioquímica e biologia molecular/01 - Via das pentoses",
 "biomol-25-mutacao-reparo-recombinacao": "UC02/Bioquímica e biologia molecular/02 - DNA mutação, lesão e reparo",
 "biomol-26-dna-recombinante-pcr":        "UC02/Bioquímica e biologia molecular/03 - DNA recombinante",
 "bioq-21-lipideos-rotas":                "UC02/Bioquímica e biologia molecular/04 - Metabolismo dos lipídeos",
 "bioq-24-glicogenio":                    "UC02/Bioquímica e biologia molecular/05 - Metabolismo do glicogênio",
 "bioq-23-aminoacidos-ureia":             "UC02/Bioquímica e biologia molecular/06 - Metabolismo dos aminoácidos",
 "embrio-01-gametogenese-fertilizacao":   "UC02/Biologia Celular, tecidual e imunologia/11 - Embriologia I",
 "embrio-02-03-gastrulacao-neurulacao":   "UC02/Biologia Celular, tecidual e imunologia/12 - Embriologia II e III",
}

def subir(local, slug, nome=None):
    if slug not in MAP:
        raise SystemExit("slug desconhecido: %s (adicione em MAP/DRIVE-ESTRUTURA.md)" % slug)
    if not os.path.exists(local):
        raise SystemExit("arquivo não existe: %s" % local)
    nome = nome or os.path.basename(local)
    destino = "%s/%s/%s" % (BASE, MAP[slug], nome)
    print("subindo:", local)
    print("    ->  ", destino)
    r = subprocess.run(["rclone", "copyto", local, destino, "--drive-acknowledge-abuse"],
                       capture_output=True, text=True)
    if r.returncode == 0:
        print("OK. Confere:", subprocess.run(["rclone","lsf",os.path.dirname(destino).replace(os.sep,"/")],
              capture_output=True, text=True).stdout.strip()[:200])
    else:
        print("FALHOU:", r.stderr[-400:])
    return r.returncode == 0

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("uso: subir_drive.py <arquivo_local> <slug> [nome_no_drive]")
    subir(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
